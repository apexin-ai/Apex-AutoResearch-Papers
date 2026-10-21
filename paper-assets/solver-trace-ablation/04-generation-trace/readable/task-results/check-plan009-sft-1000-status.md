# check plan009 sft 1000 status

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_plan009-sft-1000-status_20260515T122359_result.json`
- **Structured JSON:** [`529a02157de62da44a24.json`](../../sessions/52/529a02157de62da44a24.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

| 项目 | 状态 |
|------|------|
| **实际状态** | **COMPLETED** — 训练已完成 1000/1000 步 |
| **PID 344799** | 已死（训练正常结束退出） |
| **checkpoint** | `checkpoint-1000` 存在，模型文件完整 (~7.5GB safetensors) |
| **输出路径** | `/root/autodl-tmp/outputs/plan009_sft_baseline_s42_1000/` |
| **最终 loss** | 0.0168, token accuracy 99.6% |
| **GPU cuda:0** | 空闲（nvidia-smi 无进程） |
| **Registry** | 已更新为 DONE, conclusion=success |

**后续操作**：需要用 `eval_sta.py` 对该 checkpoint 进行评估（遵循 C004/C008，使用 `--data_path data/proofwriter_fol_100.jsonl`）。

---
