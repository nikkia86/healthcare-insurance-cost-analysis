import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


# Load dataset
df = pd.read_csv("input/insurance.csv")


def scatter(dataframe):
    """
    Displays a 3D scatter plot of Age, BMI and Charges.
    """
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection="3d")

    x = dataframe["age"]
    y = dataframe["bmi"]
    z = dataframe["charges"]

    ax.scatter(x, y, z)
    ax.set_xlabel("Age")
    ax.set_ylabel("BMI")
    ax.set_zlabel("Charges")

    st.pyplot(fig)


def stacked(dataframe):
    """
    Displays a stacked bar chart showing smoker counts by region.
    """
    grouped = dataframe.groupby(["smoker", "region"]).size().unstack()

    fig, ax = plt.subplots()
    grouped.plot(kind="bar", stacked=True, ax=ax)

    ax.set_xlabel("Smoker")
    ax.set_ylabel("Count")
    ax.set_title("Smoker Distribution Across Regions")

    st.pyplot(fig)


def parallel(dataframe):
    """
    Displays a Plotly parallel coordinates plot.
    Converts categorical variables into numeric codes.
    """
    df_copy = dataframe.copy()

    df_copy["smoker"] = df_copy["smoker"].replace({"no": 0, "yes": 1})
    df_copy["sex"] = df_copy["sex"].replace({"male": 0, "female": 1})
    df_copy["region"] = df_copy["region"].replace(
        {"northwest": 0, "northeast": 1, "southwest": 2, "southeast": 3}
    )

    fig = px.parallel_coordinates(
        df_copy,
        color="smoker",
        dimensions=["age", "sex", "bmi", "children", "region", "charges"],
    )

    st.plotly_chart(fig)


def dashboard_body():
    """
    Main dashboard page content.
    """
    st.title("Healthcare Insurance Dashboard")

    st.markdown(
        """
        This dashboard presents visual insights from the healthcare insurance dataset.
        Each section below includes a short explanation to support interpretation.
        """
    )

    st.subheader("1. Relationship Between Age, BMI and Insurance Charges")
    st.markdown(
        """
        This chart helps explore whether insurance charges show visible patterns when compared
        with age and BMI.
        """
    )
    scatter(df)

    st.subheader("2. Smoker Distribution Across Regions")
    st.markdown(
        """
        This chart compares smoker and non-smoker counts across the different regions.
        """
    )
    stacked(df)

    st.subheader("3. Multivariate Comparison Using Parallel Coordinates")
    st.markdown(
        """
        This chart allows comparison across multiple variables at once, and highlights how
        smoker status relates to age, BMI, region, number of children, and charges.
        """
    )
    parallel(df)