# Experiment Log — comm_gate_mas

**Project:** Communication Gates in Multi-Agent Systems
**Period:** April 2026
**Target venue:** NeurIPS 2026

## Experiments

| ID | Name | Config | Backbone | Topology | Dataset | Tasks | Key Result |
|----|------|--------|----------|----------|---------|-------|------------|
| A | MVP Pipeline | `mvp.yaml` | Qwen2.5-7B | RR | GSM8K | 100 | Pipeline validation |
| B | Full Scale | `full_scale.yaml` | Qwen/Llama/Gemma | RR/SEQ/SEL | GSM8K | 300×9 | 2,693 traces, 8,065 messages |
| C | MATH Cross-domain | `math_*.yaml` | All 3 | RR | MATH L3-5 | 50 | 2/3 modes replicate |
| D | HumanEval Pilot | `metagpt_qwen.yaml` | Qwen | MetaGPT | HumanEval | ~50 | Preliminary |
| E | Temperature Robustness | `temp_robustness_qwen_rr.yaml` | Qwen | RR | GSM8K | 300 | Stable at T=0.7 |
| F | Neutralize Ablation | (part of full_scale) | All 3 | RR/SEQ/SEL | GSM8K | 300×9 | Double dissociation |
| G | Cross-model Annotation | (part of full_scale) | All 3 | — | — | — | κ=0.35–0.67 |
| H | Mistral Exploratory | — | Mistral-7B | RR | GSM8K | 300 | Weakly differentiated mode |
| I | Placeholder Sensitivity | `exp_placeholder_sensitivity.py` | Qwen | RR | GSM8K | 50 | ρ=0.90, p=.037 |
| J | Capability Confound | (analysis on full_scale data) | All 3 | RR | GSM8K | 300 | R² stable across difficulty |

## Infrastructure

- **GPU:** 4× RTX 6000 Pro 96GB (AutoDL)
- **Serving:** vLLM v0.6.6, greedy decoding (T=0, max_tokens=2048)
- **Framework:** AG2 v0.6.1 (AutoGen)
- **Estimated total:** ~96 GPU-hours

## Data Paths (server: autodl-comm-gate)

| Data | Path |
|------|------|
| Traces | `/root/autodl-tmp/comm_gate_mas/outputs/traces/` |
| Annotations | `/root/autodl-tmp/comm_gate_mas/outputs/annotations/` |
| Impact results | `/root/autodl-tmp/comm_gate_mas/outputs/local_impact/` |
| Figures | `/root/autodl-tmp/comm_gate_mas/outputs/figures/` |
