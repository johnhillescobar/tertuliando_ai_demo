from openai import OpenAI
import gradio as gr
from config import LLM_MODEL
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()


def get_embeddings(text: str) -> list[float]:
    response = client.embeddings.create(
        input="Your text string goes here", model="text-embedding-3-small"
    )

    outcome = response.data[0].embedding

    print("La computadora realmente lee esto: ", outcome)


def stream_gpt(
    system_message: str, message_input: str, temperature: float = 0.0
) -> str:
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": message_input},
    ]
    stream = client.chat.completions.create(
        model=LLM_MODEL, messages=messages, temperature=temperature, stream=True
    )
    result = ""
    for chunk in stream:
        result += chunk.choices[0].delta.content or ""
        yield result


def message_chat(default_system_message: str = "", default_temperature: float = 0.0):
    """Launch a Gradio chat interface that lets users experiment with
    different system prompts and temperature values to see how they
    change the AI's responses."""

    system_input = gr.Textbox(
        label="System Prompt (mensaje de sistema):",
        info="Este mensaje le dice a la IA cómo comportarse. Cámbialo para ver cómo afecta las respuestas.",
        # value=default_system_message,
        lines=10,
    )
    temp_input = gr.Slider(
        label="Temperatura:",
        info="0 = respuestas más deterministas y consistentes. 1 = respuestas más creativas y variadas.",
        minimum=0.0,
        maximum=1.0,
        step=0.1,
        value=default_temperature,
    )
    user_input = gr.Textbox(
        label="Tu mensaje:",
        info="Escribe tu pregunta sobre la Biblia aquí.",
        lines=5,
    )
    message_output = gr.Markdown(label="Respuesta:")

    view = gr.Interface(
        fn=stream_gpt,
        title="BIBLE GPT — Demostración de System Prompt y Temperatura",
        inputs=[system_input, user_input, temp_input],
        outputs=[message_output],
        examples=[
            [
                default_system_message,
                "Qué sucede en el día 4 de la creación según la Biblia?",
                0.0,
            ],
            [
                default_system_message,
                "Cuáles fueron las personas que llegaron a la tumba de Jesús?",
                0.0,
            ],
            [
                default_system_message,
                "Cuáles fueron las personas que llegaron a la tumba de Jesús?",
                1.0,
            ],
        ],
        flagging_mode="never",
    )
    view.launch()
