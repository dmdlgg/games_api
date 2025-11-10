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
            input = f"Gere uma descrição curta para o jogo {instance.nome} do diretor {instance.diretor}, citando suas principais características, seu gênero e sua gameplay. A descrição não deve ulrapassar 8 linhas. "
        )
        instance.sinopse = response.output_text
