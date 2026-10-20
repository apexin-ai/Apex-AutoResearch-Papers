# NLP Variance G-Theory — MVP

Generalizability Theory (G-theory) variance decomposition for LLM evaluation
reproducibility.  Quantifies how much evaluation variance comes from
infrastructure factors (hardware, precision) vs methodology factors
(prompt wording, RNG seed, few-shot ordering, temperature) and their
interactions.

## Project Structure

```
src/
├── data/               # MMLU sampling, prompt templates, few-shot orderings
│   ├── sample_mmlu.py
│   ├── prompt_templates.py
│   └── few_shot.py
├── design/             # Factorial design matrix generation
│   └── generate_design.py
├── inference/          # vLLM offline inference pipeline
│   ├── vllm_runner.py
│   └── run_experiment.py
└── analysis/           # G-theory analysis, D-study, visualisation
    ├── variance_decomposition.py
    ├── d_study.py
    └── visualize.py
```

## Setup

```bash
pip install -e .
pip install -r requirements.txt
```

## Quick Start

```bash
# 1. Prepare data
python -m src.data.sample_mmlu
python -m src.data.few_shot

# 2. Generate design matrix (144 conditions)
python -m src.design.generate_design

# 3. Run inference (once per hardware type)
python -m src.inference.run_experiment --hardware gpu_type_1
python -m src.inference.run_experiment --hardware gpu_type_2

# 4. Merge results
cat results/results_*.jsonl > results/all_results.jsonl

# 5. Variance decomposition
python -m src.analysis.variance_decomposition --input results/all_results.jsonl

# 6. D-study projections
python -m src.analysis.d_study --input results/variance_components.json

# 7. Visualise
python -m src.analysis.visualize \
    --components results/variance_components.json \
    --dstudy results/d_study_results.json
```

Or use the pipeline script: `bash run_mvp.sh <hardware_type>`

## Design

**MVP factorial design** (fully crossed):

| Factor          | Levels | Values                                 |
|-----------------|--------|----------------------------------------|
| Model           | 1      | Llama-3.1-8B-Instruct                 |
| Hardware        | 2      | gpu_type_1, gpu_type_2 (placeholder)  |
| Precision       | 2      | bfloat16, float16                      |
| Temperature     | 2      | greedy (T=0), stochastic (T=0.5, p=0.9) |
| Prompt template | 3      | 3 Brittlebench-style paraphrases       |
| Seed            | 3      | 42, 123, 456                           |
| Ordering        | 2      | 2 few-shot example orderings           |

**144 conditions × 50 MMLU items = 7,200 inferences.**

## Analysis

- **G-study**: ANOVA-based variance component estimation (Henderson Method I)
  for all 7 main effects + 21 two-way interactions + residual.
  Bootstrap 95% CIs via item resampling.
- **D-study**: projects G coefficient for different numbers of
  prompt/seed/ordering/item replications.  Reports minimum replications
  needed for G ≥ 0.90 / 0.95 / 0.99.
