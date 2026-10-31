class Customer:
    def __init__(self, customer_id: int, name: str, email: str):
        self.customer_id = customer_id
        self.name = name
        self.email = email

    def to_dict(self) -> dict:
        return {
            "customer_id": self.customer_id,
            "name": self.name,
            "email": self.email
        }