from typing import Optional
from utils.Logger.index import Logger
import logging

class WayForPayTransaction:
    def __init__(
        self,
        email: str,
        phone: str
    ):
        self.email = email
        self.phone = phone

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            email=data.get('email', ''),
            phone=data.get('phone', '')
        )

class WayForPayService:

    def __init__(self, logger: logging.Logger = None):
        self.logger = logger if logger else self._create_default_logger()

    @staticmethod
    def process_transaction(data: dict) -> dict:
        transaction = WayForPayTransaction.from_dict(data)
        return {
            "status": "processed",
            "email": transaction.email,
            "phone": transaction.phone
        }
    
    @staticmethod
    def _create_default_logger() -> logging.Logger:
        """Creates a default logger."""
        return Logger.create_default_logger("WayForPay", "logs/wayforpay.log")