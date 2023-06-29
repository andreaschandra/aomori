from fastapi import APIRouter, Depends
from starlette.requests import Request

from aomori.core import security
from aomori.models.payload import HousePredictionPayload
from aomori.models.prediction import HousePredictionResult
from aomori.services.models import HousePriceModel

router = APIRouter()


@router.post("/predict", response_model=HousePredictionResult, name="predict")
def post_predict(
    request: Request,
    authenticated: bool = Depends(security.validate_request),
    block_data: HousePredictionPayload = None
) -> HousePredictionResult:

    model: HousePriceModel = request.app.state.model
    prediction: HousePredictionResult = model.predict(block_data)

    return prediction
