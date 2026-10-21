# code result processing template

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_result-processing-template_20260519T181800_result.json`
- **Structured JSON:** [`ea3b3dd2f7503a5ba207.json`](../../sessions/ea/ea3b3dd2f7503a5ba207.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Identical results from both paths. All 3 scripts validated against 72B ZS data.

**Summary:**

### `artifacts/compute_signals.py`
Computes 5 signals (LP/SJ/FK/VC/EM Spearman ρ vs greedy F1) + construction pipeline (greedy, LP selection, MV, consensus θ=2/N, LP-weighted construction, oracle) + degeneracy rates.
```bash
python compute_signals.py --input-dir output/&lt;model_dir> [--dataset scierc conll2003 fewnerd] \
    [--model-size 72] [--regime zs] [--output-dir /path/to/results]
```
Outputs: `full_signal_report.json` + `&lt;dataset>_per_instance.json`

### `artifacts/format_for_scaling.py`
Reads signal report, outputs DATA dict entries for `plot_scaling_curve.py`.
```bash
python format_for_scaling.py --report /path/to/full_signal_report.json \
    --model-size 72 --regime zs
```
Produces copy-paste-ready Python dict entries + summary table.

### `artifacts/bootstrap_construction.py`
Paired bootstrap test (B=10000): greedy F1 vs LP-weighted construction F1, with degeneracy stratification.
```bash
# From raw samples.jsonl
python bootstrap_construction.py --input-dir output/&lt;model_dir> [--dataset scierc]
# From pre-computed per-instance data
python bootstrap_construction.py --per-instance &lt;dataset>_per_instance.json --dataset scierc
```

**Validation (72B ZS):** All values match the known report exactly — LP ρ=0.081, SJ ρ=0.217, VC ρ=0.277, degen=21.0%, construction ΔF1=+1.53pp (p=0.008) for SciERC, and matching values for CoNLL/FewNERD.

---
