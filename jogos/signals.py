from django.db.models.signals import post_save
from django.dispatch import receiver
from jogos.models import Jogo
from openai import OpenAI 
from dotenv import load_dotenv
import os


load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")

@receiver(post_save, sender=Jogo)
def gerar_sinopse(sender, instance, **kwargs):

    if not instance.sinopse:
        client = OpenAI(api_key = API_KEY)
        response = client.responses.create(
            model = "gpt-5-nano",
            input = f"Crie uma descrição concisa do jogo {instance.nome}, dirigido por {instance.diretor}. Destaque suas principais características, o gênero e aspectos da gameplay. A resposta deve ter no máximo 10 linhas e ser entregue apenas em texto simples, sem formatações ou listas."
        )
        instance.sinopse = response.output_text
