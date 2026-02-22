"""
Define data structures for each stage of the pipeline.
"""

from typing import Optional
from pydantic import BaseModel


class AddressInput(BaseModel):
    """
    A single address row from the input csv.
    """
    id: str
    address: str


class GeoCodeResult(BaseModel):
    """
    Result from the Census Geocoder API.
    """
    lat: float
    lng: float


class FloodZoneResult(BaseModel):
    """
    Result from the FEMA NFHL ArcGIS Layer 28
    """
    flood_zone: str
    flood_zone_subtype: str # ZONE_SUBTY


class NRIResult(BaseModel):
    """
    Result from the FEMA National Risk Index Census Tracts feature services.
    """
    nri_score: Optional[float] = None
    nri_rating: Optional[str] = None
    avalanche_rating: Optional[str] = None
    coastal_flooding_rating: Optional[str] = None
    cold_wave_rating: Optional[str] = None
    drought_rating: Optional[str] = None
    earthquake_rating: Optional[str] = None
    hail_rating: Optional[str] = None
    heat_wave_rating: Optional[str] = None
    hurricane_rating: Optional[str] = None
    ice_storm_rating: Optional[str] = None
    landslide_rating: Optional[str] = None
    lightning_rating: Optional[str] = None
    riverine_flooding_rating: Optional[str] = None
    strong_wind_rating: Optional[str] = None
    tornado_rating: Optional[str] = None
    tsunami_rating: Optional[str] = None
    volcanic_activity_rating: Optional[str] = None
    wildfire_rating: Optional[str] = None
    winter_weather_rating: Optional[str] = None


class FinalResult(AddressInput, GeoCodeResult, FloodZoneResult, NRIResult):
    """
    Combine result row written to results.csv
    """
    pass


class ErrorRow(AddressInput):
    """
    Failed Address written to errors.csv.
    """
    error: str