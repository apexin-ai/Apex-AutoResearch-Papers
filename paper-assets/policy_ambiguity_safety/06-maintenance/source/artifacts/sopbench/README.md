# SOPBench: Evaluating Language Agents at Following Standard Operating Procedures and Constraints


## Overview

<p align="center"><img width="100%" src="assets/overview-v8.png" /></p>

This repository contains the data and code for the paper: "SOPBench: Evaluating Language Agents at Following Standard Operating Procedures and Constraints". This benchmark is used to evaluate Language Agents at Following Standard Operating Procedures and Constraints across seven customer service domains.

## Results

The following table shows model pass rates (%) across seven domains.

| **Model** | **Bank** | **DMV** | **Healthcare** | **Market** | **University** | **Library** | **Hotel** |
|:---------:|:--------:|:-------:|:--------------:|:----------:|:--------------:|:-----------:|:---------:|
| **_Proprietary Reasoning Models_** | | | | | | | |
| GPT-5 (FC) | 71.64 | 84.54 | 76.61 | 69.77 | 88.10 | 66.67 | 67.18 |
| o4-mini-high (FC) | 76.87 | 83.51 | 92.74 | 89.53 | 95.24 | 34.85 | 55.90 |
| GPT-5-mini (FC) | 58.96 | 82.47 | 92.74 | 75.58 | 95.24 | 34.85 | 69.74 |
| Gemini-2.5-Flash (FC) | 67.91 | 81.44 | 87.90 | 77.91 | 83.33 | 51.52 | 42.56 |
| Deepseek-R1 (ReAct) | 54.48 | 81.44 | 54.03 | 70.41 | 76.19 | 54.55 | 50.77 |
| **_Proprietary Non-reasoning Models_** | | | | | | | |
| GPT-4.1 (FC) | 69.40 | 79.38 | 79.03 | 80.81 | 50.00 | 57.58 | 42.56 |
| GPT-4o (FC) | 58.96 | 80.41 | 73.39 | 61.63 | 66.67 | 60.61 | 39.49 |
| Claude-3-7-Sonnet (FC) | 65.67 | 70.10 | 70.97 | 56.98 | 66.67 | 27.27 | 23.59 |
| GPT-4.1-mini (FC) | 57.46 | 76.29 | 66.13 | 56.40 | 35.71 | 18.18 | 7.18 |
| GPT-4o-mini (FC) | 33.58 | 73.20 | 25.00 | 43.60 | 38.10 | 42.42 | 41.03 |
| Claude-3-5-Sonnet (FC) | 71.90 | 50.43 | 39.23 | 43.32 | 52.27 | 33.33 | 15.82 |
| Gemini-2.0-Flash (FC) | 52.99 | 51.55 | 21.77 | 38.37 | 30.95 | 19.70 | 7.18 |
| **_Open-source Models_** | | | | | | | |
| Llama3.1-70B-Instruct (ReAct) | 42.54 | 65.98 | 54.84 | 37.21 | 42.86 | 34.85 | 13.85 |
| Qwen2.5-72B-Instruct (ReAct) | 35.07 | 68.04 | 27.42 | 40.12 | 35.71 | 34.85 | 13.85 |
| Qwen2.5-32B-Instruct (ReAct) | 40.30 | 52.58 | 41.13 | 44.19 | 54.76 | 27.27 | 18.46 |
| Qwen2.5-14B-Instruct (ReAct) | 35.07 | 57.73 | 29.03 | 35.47 | 23.81 | 25.76 | 14.87 |
| Llama3.1-8B-Instruct (ReAct) | 14.93 | 18.56 | 20.16 | 16.28 | 23.81 | 30.30 | 0.00 |
| Qwen2.5-7B-Instruct (ReAct) | 5.22 | 20.62 | 16.94 | 9.30 | 0.00 | 15.15 | 0.51 |

## Getting Started

### Installation

```bash
# Clone the repository
# Create and activate conda environment
conda create -n agent python=3.10
conda activate agent

# Install dependencies
pip install -r requirements.txt
```

### Configuration

#### API Keys Setup

Create a `.env` file in the root directory with your API keys:

```bash
OPENAI_API_KEY=[REDACTED]
ANTHROPIC_API_KEY=[REDACTED]
GEMINI_API_KEY=[REDACTED]
FIREWORKS_API_KEY=[REDACTED]
```

#### Supported Language Models

The framework supports a wide range of language models through unified interfaces for both multi-turn inference and function calling:

##### API-based Models

- **OpenAI Models**
  - GPT-5 Series: `gpt-5`, `gpt-5-mini`
  - GPT-4o Series: `gpt-4o`, `gpt-4o-mini`, `gpt-4.1`
  - "o" Series: `o1`, `o3`, `o3-mini`, `o4-mini`
- **Anthropic Models**
  - Claude 3.5: `claude-3-5-sonnet-20241022`, `claude-3-5-haiku-20241022`
  - Claude 3.7: `claude-3-7-sonnet-20250219`, `claude-3-7-sonnet-20250219-thinking`
- **Google Gemini Models**
  - Gemini 1.5: `gemini-1.5-flash`, `gemini-1.5-pro`
  - Gemini 2.0: `gemini-2.0-flash-001`, `gemini-2.0-flash`, `gemini-2.0-flash-thinking-exp`
  - Gemini 2.5: `gemini-2.5-pro-preview-03-25`, `gemini-2.5-flash-preview-04-17`
- **Fireworks Models**
  - Various models hosted on the Fireworks AI platform

##### Local Inference
- **OSS Models via vLLM**: Run open-source models locally with vLLM for efficient inference

All models use a unified format for multi-turn inference and function calling, with backend-specific implementations that convert responses to a standardized format compatible with OpenAI's API.

##### Adding Custom Models

You can add or customize supported models by modifying the model lists in `swarm/constants.py`.

## Usage

#### Key Parameters

The following command line arguments control the simulation and evaluation:

| Parameter | Description | Options |
|-----------|-------------|---------|
| `--domain` | Test domain | bank, online_market, dmv, healthcare, library, hotel, university |
| `--user_model` | Model for user agent | Any supported model name, "human" for interactive mode, or None (default) |
| `--assistant_model` | Model for assistant agent | Any supported model name |
| `--env_mode` | Environment mode | "prompt" (without code constraint checking), "program" (with code constraint checking) |
| `--tool_list` | Available tools | "full" (all tools), "oracle" (only the oracle-used tools for each case) |
| `--tool_call_mode` | Tool call mode | "fc" (function calling), "react", "act-only" |

#### Data Preparation

The framework comes with pre-generated task data in the `data` folder.

To generate new data (note that generating each task using GPT-4o costs approximately $0.015 USD):

```bash
python run_datagen.py
```

The code will run data generation and verification (format verification and constraint verification). If failed, it will start re-generation. The whole process is fully automated.

#### Running Simulations

```bash
python run_simulation.py \
  --domain [domain] \
  --user_model [user_model] \
  --assistant_model [assistant_model] \
  --env_mode [env_mode] \
  --tool_list [tool_list] \
  --tool_call_mode [tool_call_mode]
```

#### Running Evaluations

```bash
python run_evaluation.py \
  --domain [domain] \
  --user_model [user_model] \
  --assistant_model [assistant_model] \
  --tool_list [tool_list] \
  --tool_call_mode [tool_call_mode]
```

#### Reviewing Agent Trajectories

To view agent trajectories and evaluation results:

```bash
python run_checking.py \
  --output_dir [output_dir] \
  --domain [domain] \
  --assistant_model [assistant_model] \
  --tool_call_mode [tool_call_mode] \
  --default_constraint_option [default_constraint_option] \
  --constraint_descr_format [constraint_descr_format] \
  --tool_list [tool_list]
```

Over 24,000 agent trajectories are provided in the `output/` directory for reference.

## Project Structure

```
SOPBench/
├── swarm/                  # Framework code for agent interaction
│   ├── core.py             # Core agent and swarm classes
│   ├── llm_handler.py      # Unified LLM backend handler
│   ├── types.py            # Type definitions
│   ├── util.py             # Utility functions
│   ├── claude.py           # Claude-specific utilities
│   ├── gemini.py           # Gemini-specific utilities
│   └── constants.py        # Project constants and configurations
├── env/                    # Environment for different domains
│   ├── dependencies.py     # Core program code for constraint checking
│   ├── helpers.py          # Helper functions for environment
│   ├── dep_eval.py         # Evaluation utilities
│   └── domains/            # Domain implementations
│       ├── bank/
│       ├── online_market/
│       ├── dmv/
│       ├── healthcare/
│       ├── library/
│       ├── hotel/
│       └── university/
├── data/                   # Task data for simulation and evaluation
├── scripts/                # Scripts for simulation and evaluation
├── output/                 # Simulation and evaluation results
├── plotting/               # Data visualization utilities
├── run_generation.py       # Task generation script
├── run_simulation.py       # Simulation script
├── run_evaluation.py       # Evaluation script
├── run_checking.py         # Validation script
└── run_operation.py        # Operations script
```
