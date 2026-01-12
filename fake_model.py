class FakeModel:

    def generate(self, prompt: str) -> str:

        parts = prompt.split("<USER>")

        if len(parts) < 2:
            return "I don't know."
        
        last_user_block = parts[-1]
        content = last_user_block.split("</USER>")[0].strip().lower()

        if "hi" in content:
            return "Hello."
        elif "how are you" in content:
            return "I am fine."
        else:
            return "I don't know."