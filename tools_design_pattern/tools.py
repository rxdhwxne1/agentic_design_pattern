import streamlit as st
import ollama
import requests


class Calculator:
    def calculate(self, expression):
        try:
            return str(eval(expression))
        except Exception as e:
            return f"Error: {str(e)}"

    def json(self):
        return {
            'type': 'function',
            'function': {
                'name': 'Calculator',
                'description': 'mathematics calculator',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'expression': {
                            'type': 'string',
                            'description': 'mathematics expression'
                        }
                    },
                    'required': ['expression']
                }
            }
        }


class WeatherChecker:
    def check_weather(self, city):
        api = "https://wttr.in/{}?format=%C+%t+%w"
        response = requests.get(api.format(city))
        return response.text

    def json(self):
        return {
            'type': 'function',
            'function': {
                'name': 'WeatherChecker',
                'description': 'check weather',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'city': {
                            'type': 'string',
                            'description': 'city name'
                        }
                    },
                    'required': ['city']
                }
            }
        }


class Translator:
    def translate(self, text, source_language, target_language):
        response = ollama.generate(
            model="llama3.2",
            prompt=f"Translate the text '{text}' from {source_language} to {target_language}"
        )
        return response.get("response")

    def json(self):
        return {
            'type': 'function',
            'function': {
                'name': 'Translator',
                'description': 'text translator',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'text': {
                            'type': 'string',
                            'description': 'text to translate'
                        },
                        'source_language': {
                            'type': 'string',
                            'description': 'source language'
                        },
                        'target_language': {
                            'type': 'string',
                            'description': 'target language'
                        }
                    },
                    'required': ['text', 'source_language', 'target_language']
                }
            }
        }


def tool_method_name(tool_name):
    if tool_name == "Calculator":
        return "calculate"
    if tool_name == "WeatherChecker":
        return "check_weather"
    if tool_name == "Translator":
        return "translate"


class Agent:
    def __init__(self):
        self.tools = {
            "Calculator": Calculator(),
            "WeatherChecker": WeatherChecker(),
            "Translator": Translator()
        }

    def process_request(self, user_input):
        response = ollama.chat(
            model='llama3.2',
            messages=[{'role': 'user', 'content': user_input}],
            tools=[tool.json() for tool in self.tools.values()]
        )

        tool_call = response["message"].get("tool_calls")[0].get("function")
        if tool_call:
            tool_name = tool_call.get("name")
            args = tool_call.get("arguments")
            tool_method = tool_method_name(tool_name)
            total_response = self.use_tool(tool_name, tool_method, **args)
            return total_response
        return "No tool call found"

    def use_tool(self, tool_name, tool_method, **kwargs):
        if tool_name in self.tools and hasattr(self.tools[tool_name], tool_method):
            return getattr(self.tools[tool_name], tool_method)(**kwargs)
        return "Invalid tool or method"


agent = Agent()

st.title("AI Assistant with Ollama and Tools")

user_input = st.text_input("Enter your request:")
if st.button("Process"):
    response = agent.process_request(user_input)
    st.write("Response:", response)
