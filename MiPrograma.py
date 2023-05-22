import os
from dotenv import load_dotenv
import openai

load_dotenv()

api_key = os.getenv('OPEN_API_KEY')

openai.api_key = api_key

modelo = 'text-davinci-002'
prompt = '¿Que es la vida?'

response = openai.Completion.create(
    engine='text-davinci-003',  # Motor de ChatGPT a utilizar
    prompt=prompt,  # Mensaje de inicio o pregunta
    max_tokens=50,  # Número máximo de tokens en la respuesta generada
    n=1
)
texto_generado = response.choices[0].text.strip()

print(texto_generado)