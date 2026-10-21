# code exp 028 postprocess scripts

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_028_postprocess_scripts_20260517T131920_result.json`
- **Structured JSON:** [`f764cd242e3de44788d0.json`](../../sessions/f7/f764cd242e3de44788d0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已就绪。关键参数：

| 参数 | 值 |
|------|------|
| Base model | `/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B` |
| LoRA adapter | `checkpoints/qwen3-8b-fewnerd-5epoch-lora/` |
| Merged output | `checkpoints/qwen3-8b-fewnerd-5epoch-merged/` |
| Export config | `export_config_fewnerd_5epoch.yaml` (已存在) |
| Test data | `data/fewnerd_n16_subset/test.json` (5000 instances) |
| Inference output | `output/exp_028_fewnerd_5epoch/samples.jsonl` |
| Analysis output | `output/exp_028_fewnerd_5epoch/analysis_results.json` |
| N=8, T=1.0, seed=42, collect_logprobs | |

脚本结构：
- `01_merge_lora.sh` — 使用已有的 `export_config_fewnerd_5epoch.yaml` 调 `llamafactory-cli export`
- `02_inference.sh` — `run_mvp_pilot.py` N=8 全量推理
- `03_analyze.py` — Constant F1 gold-filtered degeneracy + 5 signals + within-instance rho + LP range + 对比表 + conclusion 判断（≤15% → success, >20% → negative）
- `run_all.sh` — 串联执行

训练完成后执行 `bash scripts/exp_028_postprocess/run_all.sh` 即可。

---
