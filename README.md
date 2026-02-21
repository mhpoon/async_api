# Flood Risk Pipeline

A batch processing tool that takes a CSV of addresses and returns flood zone and natural hazard risk data for each address using the US Census Geocoder, FEMA ArcGIS, and FEMA National Risk Index (NRI) APIs.

## What It Does

1. Reads a CSV file of addresses
2. Geocodes each address using the Census Geocoder API (lat, lng, FIPS)
3. Queries ArcGIS FEMA for the flood zone designation
4. Queries the FEMA NRI for the natural hazard risk rating
5. Outputs a results CSV with all data combined

## Usage 

```bash

python main.py addresses.csv
```
