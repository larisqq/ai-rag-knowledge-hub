from fastapi import APIRouter

router = APIRouter(tags=["Health"])


@router.get("/health")
def health():
    return {
        "status": "healthy"
    }


@router.get("/info")
def info():
    return {
        "application": "AI Knowledge Hub",
        "version": "1.0.0"
    }