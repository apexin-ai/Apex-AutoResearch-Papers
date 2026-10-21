# Communication Gating in LLM-Based Multi-Agent Systems

Perturbation-based analysis of inter-agent communication in LLM solver-checker systems, distinguishing structural importance from informational importance. Acknowledgment messages are individually disruptive to remove yet informationally negligible — enabling safe online pruning with no accuracy loss.

## Setup

```bash
pip install -r requirements.txt
```

Key dependencies: [AG2](https://github.com/ag2ai/ag2) (multi-agent framework), OpenAI-compatible API client, sentence-transformers, scipy, statsmodels.

A vLLM server hosting the target model is required for trace collection and end-to-end experiments:

```bash
python -m vllm.entrypoints.openai.api_server \
    --model Qwen/Qwen2.5-7B-Instruct --port 8000
```

## Project Structure

```
configs/                        # Experiment configurations (model, agents, data, topology)
src/
  trace_collection.py           # Collect inter-agent communication traces via AG2
  functional_annotation.py      # LLM-based message function annotation (5-class taxonomy)
  gpt4o_annotation.py           # GPT-4o third-party annotation for inter-annotator agreement
  local_impact.py               # Perturbation-based impact measurement (ablation + LDIM)
  pruning_validation.py         # Main experiment driver: offline simulation & online pruning
  pruning_analysis.py           # Accuracy vs. token trade-off analysis by function type
  pruning_baselines.py          # Random and function-guided pruning baselines
  heuristic_ack_detector.py     # Rule-based acknowledgment classifier
  analysis.py                   # Statistical analysis, figures, and summary generation
  correctness_annotation.py     # Per-message correctness annotation
  cross_domain_analysis.py      # Cross-domain (GSM8K/MATH/ARC/StrategyQA) analysis
  temp_robustness_analysis.py   # Stochastic decoding robustness analysis (t=0.7)
  deepseek_calibration.py       # Cross-generational transfer analysis
  utils.py                      # Shared utilities (answer extraction, model helpers)
  data_utils.py                 # Dataset loading utilities
  arc_utils.py                  # ARC-Challenge dataset utilities
  math_utils.py                 # MATH dataset utilities
  strategyqa_utils.py           # StrategyQA dataset utilities
  humaneval_utils.py            # HumanEval dataset utilities
  mast_utils.py                 # MAST trace format utilities
  metagpt_trace_collection.py   # MetaGPT topology trace collection
  v7_data_analysis.py           # Extended data analysis pipeline
scripts/
  run_5run_replication.sh       # 5-run replication experiment (varying data seeds)
  run_full_scale.sh             # Full-scale experiment runner
  run_mvp.sh                    # Minimal viable pipeline runner
  recalc_accuracy.py            # Recalculate accuracy from existing traces
data/
  gsm8k/                        # GSM8K test set (JSONL)
  human_annotation/             # Human annotation data (3 annotators, IAA scripts)
```

## Reproducing Main Experiments

### 1. Collect Traces

```bash
python src/trace_collection.py --config configs/qwen_gsm8k_rr_replication.yaml \
    --output outputs/traces.jsonl
```

### 2. Functional Annotation

```bash
python src/functional_annotation.py --config configs/qwen_gsm8k_rr_replication.yaml \
    --traces outputs/traces.jsonl --output outputs/annotations.jsonl
```

### 3. Impact Measurement

```bash
python src/local_impact.py --config configs/qwen_gsm8k_rr_replication.yaml \
    --traces outputs/traces.jsonl --output outputs/impact.jsonl
```

### 4. Online Pruning Validation

Oracle-guided (GPT-4o ack classifier):
```bash
python src/pruning_validation.py --mode online_pruning \
    --config configs/qwen_gsm8k_rr_replication.yaml \
    --num-tasks 200 --output outputs/oracle_pruning.json \
    --openai-api-key $OPENAI_API_KEY
```

Heuristic-guided (rule-based, no external API):
```bash
python src/pruning_validation.py --mode online_pruning \
    --config configs/qwen_gsm8k_rr_replication.yaml \
    --detection-mode heuristic --char-threshold 30 \
    --num-tasks 200 --output outputs/heuristic_pruning.json
```

### 5. Five-Run Replication

```bash
bash scripts/run_5run_replication.sh configs/qwen_gsm8k_rr_replication.yaml 200
```

### 6. Statistical Analysis

```bash
python src/analysis.py --traces outputs/traces.jsonl \
    --annotations outputs/annotations.jsonl \
    --impact outputs/impact.jsonl \
    --output-dir outputs/analysis/
```

## Configuration

Each YAML config specifies:
- **model**: name, API endpoint (`api_base`), generation parameters (temperature, top_p, max_tokens)
- **agents**: solver and checker system prompts
- **data**: dataset source, split, sample size, seed
- **trace_collection**: topology (`round_robin` / `sequential` / `selector`), max rounds

All configs use `api_base: "http://localhost:8000/v1"` — point to your vLLM server.

Configs cover three backbones (Qwen2.5-7B, Llama-3.1-8B, Gemma-2-9B), four task domains (GSM8K, MATH, ARC-Challenge, StrategyQA), and multiple topologies.

## Human Annotation

`data/human_annotation/` contains:
- Annotation sheets from 3 independent annotators (CSV format)
- `iaa_analysis.py` / `iaa_3annotator.py`: inter-annotator agreement computation (Cohen's kappa, Fleiss' kappa)
- `annotator.html` / `annotator_standalone.html`: web-based annotation interface

## License

This code is provided for research purposes.
