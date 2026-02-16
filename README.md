# Tertuliando

Una demostración educativa interactiva sobre cómo funciona la Inteligencia Artificial, con un enfoque especial en cómo los **system prompts** y la **temperatura** pueden manipular las respuestas de un modelo de lenguaje. El caso de estudio utiliza la Biblia como documento de referencia.

## Estructura del Proyecto

```
tertuliando/
├── config.py                        # Configuración de modelos (LLM y embeddings)
├── main.py                          # Punto de entrada principal
├── src/
│   └── helpers.py                   # Funciones auxiliares (embeddings, streaming, Gradio UI)
├── ia_y_fe.ipynb                    # Notebook principal: IA, Fe y sesgo
├── embeddings_demonstration.ipynb   # Notebook: visualización de embeddings
├── embedding_plot.png               # Visualización 3D de embeddings (PCA)
├── requirements.txt                 # Dependencias (pip)
├── pyproject.toml                   # Configuración del proyecto (uv)
└── .env                             # Variables de entorno (no incluido en git)
```

## Notebooks

### `ia_y_fe.ipynb` — IA y Fe: demostración de sesgo en IA

El notebook principal del proyecto. Guía al usuario a través de los siguientes temas:

1. **¿Qué es la IA?** — Desmitifica la IA explicándola como una operación matemática fundamental: `Resultado = Pesos × Inputs`.
2. **¿Cómo "lee" palabras una computadora?** — Demuestra el concepto de embeddings usando un versículo bíblico (Gálatas 5:14), mostrando que la máquina convierte texto en listas de números decimales.
3. **System Prompts y su impacto** — Define cuatro prompts con niveles progresivos de sesgo:
   - `mensaje_de_systema` — Neutral y objetivo. Solo reporta lo que dice el texto bíblico sin interpretaciones.
   - `mensaje_de_systema_extremista` — Subtilmente sesgado. Suena académico pero presenta una sola interpretación como verdad absoluta.
   - `mensaje_de_systema_muy_extremista` — Abiertamente sarcástico y condescendiente. Ridiculiza a quien cuestione.
   - `mensaje_de_systema_muy_sesgado` — Evangelio de la prosperidad. Reinterpreta toda la Biblia como un manual de éxito financiero.
4. **Temperatura** — Explica cómo la temperatura (0 a 1) controla la variabilidad y creatividad de las respuestas.
5. **Interfaz Gradio interactiva** — Permite al usuario experimentar en vivo cambiando el system prompt y la temperatura para observar cómo el mismo modelo produce respuestas radicalmente diferentes.
6. **Conclusiones** — La IA es un espejo del prompt: si el prompt es honesto, el espejo refleja con claridad; si es sesgado, distorsiona con elocuencia.

![Gradio Interface)](assets\biblegpt.png)

### `embeddings_demonstration.ipynb` — Visualización de Embeddings

Notebook complementario que explora el concepto de embeddings con mayor profundidad:

- Tokenización de texto con `tiktoken`.
- Generación de embeddings con los modelos `text-embedding-ada-002` y `text-embedding-3-small`.
- Reducción de dimensionalidad con PCA (SVD).
- Visualización interactiva en 3D con Plotly, comparando cómo ambos modelos representan 30 textos diferentes en el espacio vectorial.

![Embedding Visualizations (PCA → 3D)](assets\embedding_plot.png)

La gráfica muestra cómo los modelos `text-embedding-ada-002` y `text-embedding-3-small` organizan 30 textos en un espacio tridimensional reducido mediante PCA. Cada punto representa un texto; los que están más cercanos entre sí son semánticamente más similares según el modelo.

## Módulos

### `config.py`

Centraliza la configuración de modelos:

- `LLM_MODEL` — Modelo de lenguaje utilizado (`gpt-4.1`).
- `EMBEDDING_MODEL` — Modelo de embeddings (`text-embedding-3-small`).

### `src/helpers.py`

Contiene las funciones principales:

- `get_embeddings(text)` — Genera embeddings para un texto dado usando la API de OpenAI.
- `stream_gpt(system_message, message_input, temperature)` — Envía un mensaje al modelo LLM con streaming, usando un system prompt y temperatura configurables.
- `message_chat(default_system_message, default_temperature)` — Lanza una interfaz Gradio interactiva con tres controles: system prompt editable, campo de mensaje del usuario, y slider de temperatura.

### `main.py`

Punto de entrada simple del proyecto.

## Requisitos

- Python >= 3.12
- Una API key de OpenAI configurada en un archivo `.env`:

```
OPENAI_API_KEY=tu-api-key-aquí
```

## Instalación

```bash
# Clonar el repositorio
git clone <url-del-repositorio>
cd tertuliando

# Crear entorno virtual e instalar dependencias
python -m venv .venv
.venv\Scripts\activate  # Windows
pip install -r requirements.txt

# O con uv:
uv sync
```

## Dependencias principales

| Paquete        | Uso                                              |
|----------------|--------------------------------------------------|
| `openai`       | API de OpenAI (LLM y embeddings)                 |
| `gradio`       | Interfaz web interactiva                         |
| `tiktoken`     | Tokenización de texto                            |
| `numpy`        | Operaciones numéricas y PCA                      |
| `plotly`       | Visualizaciones interactivas 3D                  |
| `python-dotenv`| Carga de variables de entorno desde `.env`       |
| `scikit-learn` | Herramientas de machine learning                 |
| `chromadb`     | Base de datos de vectores                        |

## Uso

1. Abre `ia_y_fe.ipynb` en Jupyter o VS Code y ejecuta las celdas secuencialmente.
2. Experimenta con la interfaz Gradio cambiando el system prompt y la temperatura.
3. Compara las respuestas del prompt neutral con los prompts sesgados para la misma pregunta.
4. Explora `embeddings_demonstration.ipynb` para entender cómo la IA representa texto como números.
