# Generalizability Theory for LLM Evaluation Variance Decomposition

Code and data for applying Generalizability Theory (G-theory) to decompose variance in LLM benchmark evaluations, using Henderson Method I to estimate variance components across evaluation facets (prompt template, temperature, random seed, item ordering).

## Requirements

- Python 3.10+
- GPU with CUDA support (for vLLM inference)

```bash
pip install -r requirements.txt
```

## Quick Start

**1. Prepare data and design matrix**

```bash
python -m src.data.sample_mmlu --output data/mmlu_items.json
python -m src.data.few_shot --output data/few_shot_examples.json
python -m src.design.generate_design --output design_matrix.csv
```

**2. Run inference**

```bash
python -m src.inference.run_experiment \
    --design design_matrix.csv \
    --items data/mmlu_items.json \
    --few-shot data/few_shot_examples.json \
    --output results/all_results.jsonl \
    --gpu-id 0
```

**3. G-study: variance decomposition**

```bash
python -m src.analysis.variance_decomposition \
    --input results/all_results.jsonl \
    --output results/variance_components.json \
    --n-bootstrap 1000
```

**4. D-study: budget optimization**

```bash
python -m src.analysis.d_study \
    --input results/variance_components.json \
    --output results/d_study_results.json
```

The D-study calculator (`src/analysis/d_study.py`) computes generalizability coefficients for alternative designs and finds minimum replications needed to reach target reliability thresholds (G >= 0.90, 0.95, 0.99).

## Repository Structure

```
src/
  data/           Data loading and sampling
  design/         Experimental design matrix generation
  inference/      vLLM-based model inference
  analysis/       G-study, D-study, bootstrap CI, visualization
scripts/          Experiment scripts for reproducing paper results
data/             Benchmark items and few-shot examples (JSON)
paper/            LaTeX source
tests/            Unit tests
```

## License

MIT
