# diag instruct eval logs

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_instruct-eval-logs_20260515T011040_result.json`
- **Structured JSON:** [`0db17c6a38a3dae29916.json`](../../sessions/0d/0db17c6a38a3dae29916.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Clear picture now. Here's the report:

## Findings

**Model download: SUCCESS.** Qwen2.5-0.5B-Instruct was downloaded via ModelScope on 2026-05-14 16:10 to `/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B-Instruct/` (942MB, all files present including `model.safetensors`, tokenizer, config).

**Eval execution: NEVER RAN.** Evidence:
- Zero instruct-related directories in `/root/autodl-tmp/exp001/eval_results/`
- Zero instruct eval log files in `/tmp/`
- No instruct-related tmux session (active sessions: `exp006_oracle_gsm8k_ext_v2`, `exp006_s1only_gsm8k_v2`, `exp_001_eval_05B_raw`, `exp_001_eval_3B_d100_v2_para_aligned`)

**Root cause:** The previous Worker downloaded the model but never launched `evaluate.py`. It likely returned after the download step without proceeding to eval.

**Script compatibility: OK.** `evaluate.py` supports `--adapter-path` as optional (`default=None`). When omitted, it loads the model directly without LoRA merge — exactly what's needed for Instruct.

## What's needed to fix

Run the eval with something like:
```bash
python /root/contamcal-irt-calibration/exp001/evaluate.py \
  --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B-Instruct \
  --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B-Instruct_&lt;suffix> \
  --benchmarks mmlu gsm8k arc_challenge humaneval \
  --mc-format aligned
```

No adapter path needed. The model is already downloaded. The only missing step is actually launching the eval command.

---
