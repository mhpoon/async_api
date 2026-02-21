"""
Configuration
"""

CENSUS_GEOCODE_URL = "https://geocoding.geo.census.gov/geocoder/locations/addressbatch"
FEMA_FLOOD_ZONE_URL = "https://hazards.fema.gov/arcgis/rest/services/public/NFHL/MapServer/28/query"
NRI_URL = "https://services.arcgis.com/XG15cJAlne2vxtgt/ArcGIS/rest/services/National_Risk_Index_Census_Tracts/FeatureServer/0/query"

MAX_CONCURRENT_REQUESTS = 10
REQUEST_TIMEOUT = 30

OUTPUT_FILE_NAME = "results.csv"
ERROR_FILE_NAME = "errors.csv"