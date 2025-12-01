# Market Intel
**Automated Competitive Intelligence & Market Research Engine** 

MarketIntel is a fully autonomous analysis system that transforms a simple input (e.g., a company name) into a complete competitive intelligence report. It gathers data, compares competitors, uncovers market gaps, and produces a polished Markdown report — end to end.


## 🧠 What MarketIntel Does
- Collects real-world competitor data
- Builds structured comparison tables
- Generates SWOT analysis
- Identifies market gaps and opportunities
- Produces a clean, professional Markdown report

**_No spreadsheets. No endless searching. Just automated insights._**

## ⚙️ Requirements
- Python ≥3.10 and <3.14
- UV package manager
- An API key for your chosen LLM provider and tools


## 🚀 Setup & Execution

### **Step 1: Install [uv](https://docs.astral.sh/uv/getting-started/installation/#__tabbed_1_1) (The Python Package Manager)**

- _For macOs and Linux_

    - Use curl to download the script and execute it with ```sh```:
    ``` 
    curl -LsSf https://astral.sh/uv/install.sh | sh 
    ```
    - If your system doesn't have ```curl```, you can use ```wget```:
    ```
    wget -qO- https://astral.sh/uv/install.sh | sh
    ```
- _For Windows_

    - Use ```irm``` to download the script and execute it with ```iex```:
    ```
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    ```

**_After installation you should restart the shell._**

### **Step 2: Initialize Project**

- To initialize project in your local system, direct to your project directory in terminal and run:
    ```
    uv sync
    ```
    _This will create .venv and install deps_

- Create a new file ```.env``` in root directory where your pyproject.toml file exists (inside ```.env``` file):
```
MODEL=gpt-4o
OPENAI_API_KEY=<Your OpenAI API key>
SERPER_API_KEY=<Your SERPER API key>
FIRECRAWL_API_KEY=<Your FIRECRAWL API key>
```
- For [OpenAI API key](https://platform.openai.com/api-keys) visit [Openai](https://openai.com/)

- For [Serper API key](https://serper.dev/api-keys) visit [Serper.dev](https://serper.dev/)

- For [FIRECRAWL API KEY](https://www.firecrawl.dev/app/api-keys) visit [Firecrawl.dev](https://www.firecrawl.dev/)

**Step 3: Execute Project**

In Terminal/PowerShell:
```
crewai run
```
OR
```
uv run main.py
```
**_After running above command Enter Company Name, You want to get data for._**


