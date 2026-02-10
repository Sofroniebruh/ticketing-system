from datetime import datetime


class GatewayService:
    def get_health_status(self) -> dict:
        return {
            "status": "ok",
            "date": datetime.now().isoformat(),
        }


gateway_service = GatewayService()
