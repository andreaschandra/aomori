from locust import HttpUser, task


class HelloWorldUser(HttpUser):
    @task
    def get_docs(self):
        self.client.get("https://aomori-r6wqp4jvva-as.a.run.app/docs")

    @task
    def get_house_price(self):
        self.client.post(
            "https://aomori-r6wqp4jvva-as.a.run.app/api/model/predict",
            headers={'token': '1103371a-e057-4874-b5b9-e96417c711f3'},
            json={
                "median_income_in_block": 8.3252,
                "median_house_age_in_block": 41,
                "average_rooms": 6,
                "average_bedrooms": 1,
                "population_per_block": 322,
                "average_house_occupancy": 2.55,
                "block_latitude": 37.88,
                "block_longitude": -122.23,
            },
        )
