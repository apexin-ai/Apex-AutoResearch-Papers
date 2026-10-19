# code exp004 unified eval prep

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp004-unified-eval-prep_20260519T102457_result.json`
- **Structured JSON:** [`c8bd1c0b7a12bf3c6add.json`](../../sessions/c8/c8bd1c0b7a12bf3c6add.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

语法检查通过。脚本已创建：`/root/contrastive_entrain_calib/eval/run_exp004_unified_eval.sh`

要点：
- 对 checkpoint 500, 1000, 2000, 4000, 8000 依次调用 `eval_unified_preset.py`（D027 标准：ToF/NoF/SYCONScore）
- 使用 `--model_path` (Qwen3-8B base) + `--lora_path` (adapter checkpoint)
- 输出到 `/root/contrastive_entrain_calib/results/exp004_unified_eval/exp004-ckptNNNN/`
- GPU 通过 `CUDA_VISIBLE_DEVICES` 环境变量传入（脚本未硬编码）
- 自动跳过不存在的 checkpoint 和已完成的评估

运行方式：`CUDA_VISIBLE_DEVICES=X bash /root/contrastive_entrain_calib/eval/run_exp004_unified_eval.sh`

---
