# eval 05B d025 aligned

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_05B_d025_aligned_20260514T131330_result.json`
- **Structured JSON:** [`3e7c8f7336e385c2c4d6.json`](../../sessions/3e/3e7c8f7336e385c2c4d6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成：

| 项目 | 状态 |
|------|------|
| cuda:5 空闲检查 | 0 MiB, 0% — 通过 |
| C001 进程查重 | 无冲突进程 |
| checkpoint 存在 | adapter_model.safetensors (33MB) ✓ |
| evaluate.py 参数修正 | `--model-path`（非 `--model-name`），无 `--gpu`/`--seed` 参数 |
| registry 注册 | `exp_001_eval_05B_d025_aligned` → RUNNING |
| tmux session | `eval_05B_d025`，PID 374947，cuda:5 占用 1492 MiB |
| 当前进度 | 正在评估 mmlu |

注意：任务模板里的 `--model-name` 实际应为 `--model-path`，`--gpu 0` 和 `--seed 42` 在 evaluate.py 中不存在，已去掉。GPU 通过 `CUDA_VISIBLE_DEVICES=5` 映射。

监控命令：`tail -20 /tmp/eval_05B_d025.log`

---
