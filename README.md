# Claude API Course Examples

Small Python examples for learning the Anthropic Messages API, prompt engineering, streaming, and tool use.

## Requirements

- Python 3.11 or newer
- An Anthropic API key

## Setup

From the repository root, create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the required packages:

```bash
pip install anthropic python-dotenv
```

Create a `.env` file in the repository root and add your API key:

```env
ANTHROPIC_API_KEY=your_api_key_here
```

The `.env` file is ignored by Git. Do not commit your API key.

## Run Examples

Run all commands from the repository root with the virtual environment activated.

### Messages API

```bash
python hello_api.py
python system_prompt.py
python streaming.py
python json_generation.py
python "looping chatbot.py"
```

- `hello_api.py`: basic request with an optional system prompt and stop sequence.
- `system_prompt.py`: applies a system instruction to a request.
- `streaming.py`: prints generated text as stream events arrive.
- `json_generation.py`: asks the model to return raw JSON.
- `looping chatbot.py`: interactive multi-turn conversation; press `Ctrl+C` to exit.

### Prompt Evaluation

```bash
python prompt_evals.py
python prompt_evals_deterministic.py
python prompt_graders.py
python prompt_execcise.py
python prompting_engineering001.py
python prompting_engineering001_excercise.py
```

The prompt-engineering scripts may generate or overwrite these local artifacts:

- `dataset.json`: generated test scenarios
- `output.json`: evaluation results
- `output.html`: browser-readable evaluation report

Open `output.html` in a browser after an evaluation completes.

### Tool Use

```bash
python 001_tools_functions.py
python 002_tools_schema.py
python 003_tools_handling_shcema_messages.py
python 004_tools_get_tools_responses.py
python "005_tools:muliturn.py"
python 009_web_search.py
```

These examples progressively demonstrate defining tools, publishing schemas, handling tool-use messages, returning tool results, and running a multi-turn tool loop.

`009_web_search.py` uses Anthropic's built-in `web_search` tool. It searches for an answer to the configured user question and prints the complete API response. Update the question or the `allowed_domains` list in the script to change the search behavior.

## Troubleshooting

- `AuthenticationError`: confirm `ANTHROPIC_API_KEY` is present in `.env` and restart the command.
- `messages: at least one message is required`: append a user message before calling `client.messages.create()`.
- `conversation must end with a user message`: remove assistant-message prefills; request the desired output format through the system or user prompt instead.
- `unexpected keyword argument 'temperature'`: the installed SDK does not support `temperature` for `messages.create`; omit it.
- `ModuleNotFoundError`: activate the virtual environment and rerun `pip install anthropic python-dotenv`.
