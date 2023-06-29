import numpy as np
from locust import HttpUser, task


class GuestUsers(HttpUser):
    @task
    def get_docs(self):
        """Get documentation page."""
        self.client.get("https://aomori-r6wqp4jvva-as.a.run.app/docs")

    @task
    def get_house_price(self):
        """get house price from ML model."""

        median_income_in_block = np.random.randint(low=4, high=9) + np.random.random()
        median_house_age_in_block = np.random.randint(low=18, high=70)
        average_rooms = np.random.randint(low=1, high=9)
        average_bedrooms = np.random.randint(low=1, high=9)
        population_per_block = np.random.randint(low=150, high=400)
        average_house_occ = np.random.randint(low=1, high=5) + np.random.random()
        block_latitude = 36 + np.random.random()
        block_longitude = -122 + np.random.random()

        self.client.post(
            "https://aomori-r6wqp4jvva-as.a.run.app/api/model/predict",
            headers={"token": "1103371a-e057-4874-b5b9-e96417c711f3"},
            json={
                "median_income_in_block": median_income_in_block,
                "median_house_age_in_block": median_house_age_in_block,
                "average_rooms": average_rooms,
                "average_bedrooms": average_bedrooms,
                "population_per_block": population_per_block,
                "average_house_occupancy": average_house_occ,
                "block_latitude": block_latitude,
                "block_longitude": block_longitude,
            },
        )
