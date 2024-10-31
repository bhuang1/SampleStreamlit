import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Define your data
INACTIVITY_DATA = {
    "AL": 30.7, "AK": 20.8, "AZ": 23.3, "AR": 31.1, "CA": 21.2,
    "CO": 17.7, "CT": 22.6, "DE": 27.2, "DC": 20.2, "FL": 27.3,
    "GA": 27.4, "HI": 21.7, "ID": 22.2, "IL": 24.9, "IN": 28.5,
    "IA": 24.5, "KS": 24.8, "KY": 32.5, "LA": 30.8, "ME": 24.8,
    "MD": 23.2, "MA": 23.3, "MI": 24.3, "MN": 21.0, "MS": 33.2,
    "MO": 27.8, "MT": 21.5, "NE": 24.3, "NV": 26.0, "NH": 21.5,
    "NJ": -1, "NM": 23.7, "NY": 25.9, "NC": 24.6, "ND": 25.6,
    "OH": 26.9, "OK": 30.5, "OR": 20.7, "PA": 24.7, "RI": 25.3,
    "SC": 27.6, "SD": 25.3, "TN": 18.2, "TX": 19.6, "UT": 23.4,
    "VT": 18.4, "VA": 30.1, "WA": 21.9, "WV": 23.6, "WI": 29.5,
    "WY": 49.4
}

OBESITY_DATA = {
    "WV": 41.0, "LA": 40.1, "OK": 40.0, "MS": 39.5, "TN": 38.9,
    "AL": 38.3, "OH": 38.1, "DE": 37.9, "IN": 37.7, "KY": 37.7,
    "WI": 37.7, "AR": 37.4, "IA": 37.4, "GA": 37.0, "SD": 36.8,
    "MO": 36.4, "KS": 35.7, "TX": 35.5, "ND": 35.4, "NE": 35.3,
    "VA": 35.2, "SC": 35.0, "MI": 34.5, "WY": 34.3, "NC": 34.1,
    "PR": 34.1, "MN": 33.6, "NV": 33.5, "IL": 33.4, "PA": 33.4,
    "AZ": 33.2, "ID": 33.2, "MD": 33.2, "ME": 33.1, "GU": 32.7,
    "NM": 32.4, "AK": 32.1, "VI": 32.1, "WA": 31.7, "FL": 31.6,
    "UT": 31.1, "OR": 30.9, "RI": 30.8, "CT": 30.6, "MT": 30.5,
    "NH": 30.2, "NY": 30.1, "NJ": 29.1, "CA": 28.1, "MA": 27.2,
    "VT": 26.8, "HI": 25.9, "CO": 25.0, "DC": 24.3,
}

FUNDING_DATA = {
    "ND": 341146022.82, "NV": 1719580412.84, "OH": 7680400955.83,
    "GU": 157092386.97, "NY": 17399877294.79, "HI": 694557754.68,
    "IN": 3627529110.5, "WV": 1183408522.9, "NE": 1653317614.45,
    "FL": 8477157892.89, "AR": 1948317584.0, "ME": 966800605.75,
    "CT": 1932864819.22, "SD": 357184282.9, "WY": 207563106.72,
    "LA": 4381918589.41, "MT": 618457549.18, "MI": 8090686034.41,
    "NJ": 4679417447.54, "UT": 1215702428.64, "SC": 2820572858.02,
    "VA": 5461132118.13, "CA": 31471573675.3, "NH": 412794162.87,
    "OR": 878122216.7, "TX": 9145312300.64, "KY": 4638384740.41,
    "NM": 2242138460.1, "MS": 2627470683.66, "AK": 799162157.6,
    "GA": 6438709087.91, "TN": 4513326799.8, "IA": 3276970530.36,
    "CO": 5883074700.57, "PR": 1968275875.5, "MD": 5883074700.57,
    "WA": 6459840625.56, "AL": 2200999380.09, "IL": 6353136933.7,
    "ID": 210706779.42, "AZ": 2470459670.23, "DE": 1551777322.56,
    "NC": 3240214201.54, "MO": 4929085461.66, "FL": 13239497424.09,
}

BIRTH_DATA = {
    "AL": 58149, "AK": 9359, "AZ": 78547, "AR": 35471, "CA": 419104,
    "CO": 62383, "CT": 35332, "DE": 10816, "DC": 8075, "FL": 224433,
    "GA": 126130, "HI": 15535, "ID": 22391, "IL": 128350, "IN": 79649,
    "IA": 36506, "KS": 34401, "KY": 52315, "LA": 56479, "ME": 12093,
    "MD": 68782, "MA": 68584, "MI": 102321, "MN": 64015, "MS": 34675,
    "MO": 68985, "MT": 11175, "NE": 24345, "NV": 33193, "NH": 12077,
    "NJ": 102893, "NM": 21614, "NY": 207774, "NC": 121562, "ND": 9567,
    "OH": 128231, "OK": 48332, "OR": 39493, "PA": 130252, "RI": 10269,
    "SC": 57820, "SD": 11201, "TN": 82265, "TX": 389741, "UT": 45768,
    "VT": 5316, "VA": 95630, "WA": 83333, "WV": 16929, "WI": 60049,
    "WY": 6049, "PR": 19112, "VI": 868,
}

FERTILITY_DATA = {
    "AL": 58.7, "AK": 64.9, "AZ": 54.9, "AR": 60.2, "CA": 52.8,
    "CO": 51.5, "CT": 50.7, "DE": 57.3, "DC": 44.9, "FL": 55.6,
    "GA": 56.0, "HI": 59.3, "ID": 58.4, "IL": 51.8, "IN": 59.7,
    "IA": 59.9, "KS": 60.3, "KY": 61.1, "LA": 61.8, "ME": 49.7,
    "MD": 56.9, "MA": 48.7, "MI": 54.0, "MN": 58.2, "MS": 59.7,
    "MO": 57.7, "MT": 53.2, "NE": 63.6, "NV": 53.2, "NH": 47.9,
    "NJ": 58.1, "NM": 58.9, "NY": 45.7, "NC": 57.5, "ND": 62.2,
    "OH": 57.3, "OK": 61.6, "OR": 56.1, "PA": 52.5, "RI": 48.7,
    "SC": 56.3, "SD": 60.5, "TN": 61.6, "TX": 57.9, "UT": 68.5,
    "VT": 52.4, "VA": 53.9, "WA": 54.8, "WV": 59.3, "WI": 54.3,
    "WY": 59.2, "PR": 61.3
}

DEATH_DATA = {
    "AL": 9360, "AK": 2615, "AZ": 42625, "AR": 2773, "CA": 191123,
    "CO": 39596, "CT": 32765, "DE": 1344, "DC": 1025, "FL": 165149,
    "GA": 54280, "HI": 8706, "ID": 2321, "IL": 111678, "IN": 68834,
    "IA": 30442, "KS": 19898, "KY": 47415, "LA": 68516, "ME": 14707,
    "MD": 50863, "MA": 51064, "MI": 61467, "MN": 38285, "MS": 34655,
    "MO": 56836, "MT": 11078, "NE": 13051, "NV": 18618, "NH": 9715,
    "NJ": 80388, "NM": 24433, "NY": 147264, "NC": 88645, "ND": 3760,
    "OH": 103194, "OK": 39581, "OR": 25883, "PA": 116202, "RI": 9067,
    "SC": 38482, "SD": 8021, "TN": 72420, "TX": 241862, "UT": 22420,
    "VT": 6782, "VA": 63640, "WA": 56959, "WV": 13777, "WI": 64764,
    "WY": 4715, "PR": 34134
}

DEATH_RATE_DATA = {
    "AL": 11.3, "AK": 8.7, "AZ": 6.8, "AR": 8.7, "CA": 7.9,
    "CO": 7.2, "CT": 8.4, "DE": 11.3, "DC": 12.2, "FL": 9.6,
    "GA": 8.5, "HI": 8.3, "ID": 6.8, "IL": 9.3, "IN": 9.4,
    "IA": 9.2, "KS": 8.2, "KY": 9.1, "LA": 12.3, "ME": 10.6,
    "MD": 9.0, "MA": 8.8, "MI": 10.6, "MN": 7.4, "MS": 12.0,
    "MO": 10.0, "MT": 10.6, "NE": 8.5, "NV": 7.8, "NH": 8.7,
    "NJ": 10.0, "NM": 12.4, "NY": 7.4, "NC": 8.9, "ND": 9.7,
    "OH": 10.3, "OK": 10.0, "OR": 8.8, "PA": 10.4, "RI": 10.5,
    "SC": 10.5, "SD": 9.5, "TN": 10.8, "TX": 10.8, "UT": 6.9,
    "VT": 9.3, "VA": 8.0, "WA": 8.4, "WV": 11.4, "WI": 10.2,
    "WY": 8.7, "PR": 8.7
}

# Prepare DataFrame from the data
def prepare_data():
    df = pd.DataFrame({
        "State": INACTIVITY_DATA.keys(),
        "Inactivity": INACTIVITY_DATA.values(),
        "Obesity": [OBESITY_DATA.get(state, np.nan) for state in INACTIVITY_DATA.keys()],
        "Funding": [FUNDING_DATA.get(state, np.nan) for state in INACTIVITY_DATA.keys()],
        "Births": [BIRTH_DATA.get(state, np.nan) for state in INACTIVITY_DATA.keys()],
        "Deaths": [DEATH_DATA.get(state, np.nan) for state in INACTIVITY_DATA.keys()],
        "Death Rate": [DEATH_RATE_DATA.get(state, np.nan) for state in INACTIVITY_DATA.keys()],
        "Fertility": [FERTILITY_DATA.get(state, np.nan) for state in INACTIVITY_DATA.keys()]
    })
    return df.dropna()

# Create scatter plots
def scatter_plot(x, y, df, x_label, y_label):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x=x, y=y)
    sns.regplot(data=df, x=x, y=y, scatter=False, color='red')
    plt.title(f'Scatter Plot of {y_label} vs {x_label}')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    st.pyplot(plt)

# Streamlit application
st.title('Health Data Scatter Plots')

# Prepare data
data = prepare_data()

# Define all possible relationships
scatter_options = {
    "Inactivity vs Obesity": ("Inactivity", "Obesity"),
    "Inactivity vs Funding": ("Inactivity", "Funding"),
    "Inactivity vs Births": ("Inactivity", "Births"),
    "Inactivity vs Deaths": ("Inactivity", "Deaths"),
    "Inactivity vs Death Rate": ("Inactivity", "Death Rate"),
    "Obesity vs Funding": ("Obesity", "Funding"),
    "Obesity vs Births": ("Obesity", "Births"),
    "Obesity vs Deaths": ("Obesity", "Deaths"),
    "Obesity vs Death Rate": ("Obesity", "Death Rate"),
    "Funding vs Births": ("Funding", "Births"),
    "Funding vs Deaths": ("Funding", "Deaths"),
    "Funding vs Death Rate": ("Funding", "Death Rate"),
    "Births vs Deaths": ("Births", "Deaths"),
    "Births vs Death Rate": ("Births", "Death Rate"),
    "Fertility vs Death Rate": ("Fertility", "Death Rate"),
    "Obesity vs Fertility": ("Obesity", "Fertility")

}

selected_plot = st.selectbox("Select a scatter plot to view", list(scatter_options.keys()))

x_col, y_col = scatter_options[selected_plot]
scatter_plot(x_col, y_col, data, x_col, y_col)
