# AI Travel Planner

An AI-assisted travel planning app built with Streamlit and LangGraph. Enter a trip request to gather flight and hotel information, generate an itinerary, and get a consolidated travel plan. Plans can be downloaded as Markdown and are also saved locally.

> This app provides travel research and planning; it does not book flights or hotels.

## Screenshot

![AI Travel Planner interface](assets/travel-planner-screenshot.png)

## How it works

The request passes through four LangGraph agents in order:

1. **Flight agent** fetches up to five flight records from AviationStack.
2. **Hotel agent** searches the web with Tavily for hotel information.
3. **Itinerary agent** uses Groq to draft an itinerary from the request and research results.
4. **Final agent** combines the results into a travel plan.

PostgreSQL is used by LangGraph's checkpointer to persist conversation state by user ID. The Streamlit interface shows the agent results, offers a Markdown download, and saves each generated plan in `travel_plans/`.

## Requirements

- Python 3.12 or newer
- A PostgreSQL database
- API keys for Groq, Tavily, and AviationStack

## Setup

Create and activate a virtual environment:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install the dependencies:

```powershell
python -m pip install --upgrade pip
python -m pip install streamlit langgraph langgraph-checkpoint-postgres "psycopg[binary]" langchain-core langchain-groq tavily-python requests python-dotenv
```

Create a `.env` file in the project root with these values:

```dotenv
GROQ_API_KEY=your_groq_api_key
AVIATIONSTACK_API_KEY=your_aviationstack_api_key
TAVILY_API_KEY=your_tavily_api_key
DATABASE_URL=postgresql://username:password@localhost:5432/database_name
```

Ensure PostgreSQL is running and the database in `DATABASE_URL` exists and is reachable. The app initializes the LangGraph checkpoint tables when it starts.

## Run the app

From the project root, with the virtual environment active:

```powershell
streamlit run frontend.py
```

Streamlit prints a local URL to open in your browser.

The graph can also be run from the terminal:

```powershell
python main.py
```

## Project structure

```text
.
├── assets/
│   └── travel-planner-screenshot.png
├── tools/
│   ├── flight_tool.py
│   └── tavily_tool.py
├── travel_plans/       # Generated Markdown plans
├── frontend.py         # Streamlit interface
└── main.py             # LangGraph workflow and agents
```

## Notes

- Keep API keys and database credentials in `.env`; do not publish them.
- `thread_id` in the sidebar is the conversation identifier used for checkpoint persistence.
- Flight results depend on the AviationStack account and data available to its API key. Hotel research depends on Tavily search results.
