from pydantic import BaseModel


class PredictionRequest(BaseModel):
    production_budget: float
    title_year: int
    aspect_ratio: float
    duration: int
    budget: float
    imdb_score: float
    opening_gross: float
    screens: float


class PredictionResponse(BaseModel):
    worldwidegross: float
