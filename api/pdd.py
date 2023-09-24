from pydantic import BaseModel

class pd(BaseModel):
    variance: float
    skewness: float
    curtosis: float
    entropy: float