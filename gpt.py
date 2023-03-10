import openai
class OpenAi():
    def __init__(self):
        self.api = ""
        self.answer = ""
    def sendResponse(self, question):
        openai.api_key = self.api
        try:
            response = openai.Completion.create(
                    model="text-davinci-003",
                    prompt=question,
                    temperature=0,
                    max_tokens=1000,
                    top_p=1.0,
                    frequency_penalty=0.0,
                    presence_penalty=0.0,
                    stop=["\"\"\""]
                )
        except openai.error.AuthenticationError:
            raise Exception("""Please make sure your key is good and authed in your .env """)
        except openai.error.RateLimitError as e:
             raise Exception("ERROR. SERVER ARE OVERLOADED PLEASE TRY AGAIN LATER")
        self.answer = response['choices'][0]['text']
