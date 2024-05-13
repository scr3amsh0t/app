from locust import HttpUser, task

class HelloWorldUser(HttpUser):
    @task(1)
    def hello_world(self):
        self.client.get("/")
        self.client.get("/comments")
        self.client.get("/posts")


        