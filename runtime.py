from context import Context
from fake_model import FakeModel

class RunTime:

    def __init__(self):
        
        self.context = Context()
        self.model = FakeModel()
        self.context.add("system", "You are a helpful assistant.")

    def step(self, user_input: str) -> str:
        
        self.context.add("user", user_input)

        prompt = self.context.build()

        response = self.model.generate(prompt)

        self.context.add("assistant", response)

        return response