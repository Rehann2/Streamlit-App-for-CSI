import streamlit as st
import earthpy.plot as ep
import rasterio
import matplotlib.pyplot as plt

st.title("Climate Stress Index (CSI)")
st.write("Climate change is an urgent global issue, with its impacts reverberating across every corner of our planet. From the escalating sea levels to the increasing frequency of extreme weather events, the repercussions of climate change are diverse and far-reaching.The Climate Stress Index a project which i spearheaded in my internship,offers a comprehensive evaluation of the multiple factors contributing to climate stress in a specific region, providing valuable insights for policymakers, researchers, and environmentalists.It is one of a kind high resolution(1x1km) index built using 12 variables from multiple domains.The index provides an opportunity to small or big organisations to study and then create an impact on a reasonable and achievable scale")
# Display the flowchart
st.image("Data/Picture2.png",
         caption="Methodology",
         use_column_width=True)

# Define terms and their descriptions
terms = {
    "Phase 1": "In Phase 1, we initiate our approach with an in-depth exploration of key factors influencing global climate stress. These factors are sourced from reputable institutions like NASA, WRI, and Global Forest Watch. Our data collection ensures comprehensive and reliable information.",
    "Phase 2": "Phase 2 involves data scaling using proprietary functions derived from the RDMI. This includes logarithmic and bisymmetric log transformations to rectify data skewness. We standardize data through z-score normalization, ensuring a mean of 0 and standard deviation of 1. Metric polarity adjustments are made to align with CSI objectives. For example, Water stress and PM2.5 Levels directly influence CSI, while soil thickness inversely affects it. We use sigmoid functions to constrain values within (0,1).",
    "Phase 3": "In Phase 3, we categorize diverse metrics into four key categories: Water-related Factors, Land Use and Agriculture, Air Quality and Atmospheric Conditions, and Human Factors. Each category encapsulates climate stress facets. We aggregate metrics within each category using the median to obtain robust category representations. This approach is resistant to outliers. Our goal is to derive a single value representing overall climate stress for each region through dimension-level aggregation."
}

st.write("## Phases of building the index")
for term, definition in terms.items():
    with st.expander(term):
        st.write(definition)

# Moved the selectbox outside of the loop
option = st.selectbox(
    'Which variable do you want to display?',
    ('PM 2.5 Levels', 'Carbon Footprint', 'Cropland Area', 'Greenhouse Gas Emissions(Cropland)','Soil Thickness','Coastal Eutrophication Potential','Coastal Floods','Drought Risk','Evapotranspiration Anomaly','Riverine Floods','Seasonal Variability','Water Stress')
)

if option == 'PM 2.5 Levels':
    with rasterio.open("Data/Trial Run aggregation-4(Austria)/Air Quality and Atmospheric Conditions/final_output_austria_pm25.tiff") as src:
        img = src.read()
if option == 'Carbon Footprint':
    with rasterio.open("Data/Trial Run aggregation-4(Austria)/Human Factors/final_output_carbonfootprint_austria.tiff") as src:
        img = src.read()
if option == 'Cropland Area':
    with rasterio.open("Data/Trial Run aggregation-4(Austria)/Land Use and Agriculture/final_output_cropland_austria.tiff") as src:
        img = src.read()
if option == 'Greenhouse Gas Emissions(Cropland)':
    with rasterio.open("Data/Trial Run aggregation-4(Austria)/Land Use and Agriculture/Final_output_ghgc_austria.tiff") as src:
        img = src.read()
if option == 'Soil Thickness':
    with rasterio.open("Data/Trial Run aggregation-4(Austria)/Land Use and Agriculture/final_output_Soil_austria.tiff") as src:
        img = src.read()
if option == 'Coastal Eutrophication Potential':
    with rasterio.open("Data/Trial Run aggregation-4(Austria)/Water-related Factors/final_CEP_austria.tiff") as src:
        img = src.read()
if option == 'Coastal Floods':
    with rasterio.open("Data/Trial Run aggregation-4(Austria)/Water-related Factors/final_Coastal_flood_austria.tiff") as src:
        img = src.read()
if option == 'Drought Risk':
    with rasterio.open("Data/Trial Run aggregation-4(Austria)/Water-related Factors/final_Drought_austria.tiff") as src:
        img = src.read()
if option == 'Evapotranspiration Anomaly':
    with rasterio.open("Data/Trial Run aggregation-4(Austria)/Water-related Factors/final_output_ETAnomaly_Austria.tiff") as src:
        img = src.read()
if option == 'Riverine Floods':
    with rasterio.open("Data/Trial Run aggregation-4(Austria)/Water-related Factors/final_Riverine_flood_austria.tiff") as src:
        img = src.read()
if option == 'Seasonal Variability':
    with rasterio.open("Data/Trial Run aggregation-4(Austria)/Water-related Factors/final_Seasonal_Variability_austria.tiff") as src:
        img = src.read()
if option == 'Water Stress':
    with rasterio.open("Data/Trial Run aggregation-4(Austria)/Water-related Factors/final_Water_stress_austria.tiff") as src:
        img = src.read()

fig, ax = plt.subplots(figsize=(10, 10))
ep.plot_bands(img, cmap='coolwarm', title=option, ax=ax)
st.pyplot(fig)
import streamlit as st

# Sample data: category name mapped to its aggregated image and list of variable images
categories = {
    "Water-related Factors": {
        "aggregated": "Data/Water_related_Factors.tiff",
        "variables": [
            "Data/Trial Run aggregation-4(Austria)/Water-related Factors/final_CEP_austria.tiff",
            "Data/Trial Run aggregation-4(Austria)/Water-related Factors/final_Drought_austria.tiff",
            "Data/Trial Run aggregation-4(Austria)/Water-related Factors/final_Water_stress_austria.tiff",
            "Data/Trial Run aggregation-4(Austria)/Water-related Factors/final_Coastal_flood_austria.tiff",
            "Data/Trial Run aggregation-4(Austria)/Water-related Factors/final_output_ETAnomaly_Austria.tiff",
            "Data/Trial Run aggregation-4(Austria)/Water-related Factors/final_Riverine_flood_austria.tiff",
            "Data/Trial Run aggregation-4(Austria)/Water-related Factors/final_Seasonal_Variability_austria.tiff",
        ],
    },
    "Air Quality and Atmospheric Conditions": {
        "aggregated": "Data/Trial Run aggregation-4(Austria)/Air Quality and Atmospheric Conditions/Atmospheric_Conditions.tiff",
        "variables": [
            "Data/Trial Run aggregation-4(Austria)/Air Quality and Atmospheric Conditions/final_output_austria_pm25.tiff"
        ],
    },
    "Land Use and Agriculture": {
        "aggregated": "Data/Trial Run aggregation-4(Austria)/Land Use and Agriculture/Land Use and Agriculture.tiff",
        "variables": [
            "Data/Trial Run aggregation-4(Austria)/Land Use and Agriculture/final_output_cropland_austria.tiff",
            "Data/Trial Run aggregation-4(Austria)/Land Use and Agriculture/Final_output_ghgc_austria.tiff",
            "Data/Trial Run aggregation-4(Austria)/Land Use and Agriculture/final_output_Soil_austria.tiff",
        ],
    },
    "Human Factor": {
        "aggregated": "Data/Trial Run aggregation-4(Austria)/Human Factors/human_factors.tiff",
        "variables": [
            "Data/Trial Run aggregation-4(Austria)/Human Factors/final_output_carbonfootprint_austria.tiff"
        ],
    },
}

st.title("Climate Stress Index (CSI) Categories")

# Sidebar for category selection
selected_category = st.sidebar.radio("Select Sub-Dimension Level Category to Aggregate", list(categories.keys()))

# Main content area
# Display the aggregated image for the selected category as a large tile
aggregated_image_path = categories[selected_category]["aggregated"]
try:
    with rasterio.open(aggregated_image_path) as src:
        img = src.read(1)  # Read the first band of the TIFF file
    fig, ax = plt.subplots(figsize=(8, 8))
    ep.plot_bands(img, title=f"Aggregated Image for {selected_category}", ax=ax, cmap='coolwarm')  # Specify the colormap
    ax.axis('off')
    st.pyplot(fig)
except Exception as e:
    st.error(f"Failed to display the aggregated image at path: {aggregated_image_path}")
    st.error(f"Error: {e}")

# Display the variable images for the selected category
st.write(f"Variables that build up to {selected_category}:")

# Check if there is only one variable in the selected category
if len(categories[selected_category]["variables"]) == 1:
    # Display the single variable as an image
    variable_image_path = categories[selected_category]["variables"][0]
    try:
        with rasterio.open(variable_image_path) as src:
            img = src.read(1)  # Read the first band of the TIFF file
        fig, ax = plt.subplots(figsize=(8, 8))
        ep.plot_bands(img, title=variable_image_path.split('/')[-1].replace('.tiff', ''), ax=ax, cmap='coolwarm')  # Specify the colormap
        ax.axis('off')
        st.pyplot(fig)
    except Exception as e:
        st.error(f"Failed to display the variable image at path: {variable_image_path}")
        st.error(f"Error: {e}")
else:
    # Determine the shape of the subplots grid based on the number of variables
    num_variables = len(categories[selected_category]["variables"])
    num_rows = (num_variables - 1) // 4 + 1  # 4 subplots per row
    num_cols = min(num_variables, 4)  # Maximum 4 subplots per row

    # Create a figure for variable images
    fig, axes = plt.subplots(num_rows, num_cols, figsize=(16, 8))
    axes = axes.ravel()

    # Load and display variable images
    for i, variable_img in enumerate(categories[selected_category]["variables"]):
        with rasterio.open(variable_img) as src:
            img = src.read(1)  # Read the first band of the TIFF file
        ax = axes[i]
        ep.plot_bands(img, cmap='coolwarm', title=variable_img.split('/')[-1].replace('.tiff', ''), ax=ax)
        ax.axis('off')

    # Remove any empty subplots if there are fewer variables than expected
    for i in range(num_variables, num_rows * num_cols):
        fig.delaxes(axes[i])

    # Show the variable images plot
    st.pyplot(fig)

st.title("Climate Stress Index (CSI) for Selected Countries")

# Sample data: country name mapped to its CSI map image
countries = {
    "Vietnam": "Data/trimmed_mean_index_vietnam.png",
    "Austria": "Data/trimmed_mean_index_aus.png",
    "Kenya": "Data/trimmed_mean_index_ken.png",
}

# Tabbed layout for country selection
selected_country = st.selectbox("Select a Country", list(countries.keys()))

# Display the CSI map for the selected country
st.image(countries[selected_country], caption=f"CSI for {selected_country}", use_column_width=True)

# Sample data: country name mapped to its CSI map image
countries = {
    "Vietnam": "Data/Distribution_Vietnam.png",
    "Austria": "Data/Distribution_Austria.png",
    "Kenya": "Data/Distribution_Kenya.png",
}



# Display the CSI map for the selected country
st.image(countries[selected_country], caption=f"CSI for {selected_country}", use_column_width=True)
