# code rho02 adaptive tau09 script

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_rho02_adaptive_tau09_script_20260516T092524_result.json`
- **Structured JSON:** [`98bd53d0a725ed9a3593.json`](../../sessions/98/98bd53d0a725ed9a3593.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已就绪：`/root/provenance_weight_training/scripts/run_rho02_adaptive_tau09_seed42.sh`

关键参数确认：
- `--weighting_method adaptive`，`--tau 0.9`，`--n_min 2`
- `--data_path data/scored_data_rho02.jsonl`，`--contamination_ratio 0.2`
- `--output_dir output/models/rho02_adaptive_tau09_seed42`
- `--num_train_tokens 200000000`（与 uniform 一致）
- `WANDB_MODE=offline`，无硬编码 `CUDA_VISIBLE_DEVICES`
- dry-run 参数解析通过

---
