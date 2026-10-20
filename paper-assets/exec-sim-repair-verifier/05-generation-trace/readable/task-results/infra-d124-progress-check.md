# infra d124 progress check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_d124-progress-check_20260518T073911_result.json`
- **Structured JSON:** [`dccc24c0595dccae80b3.json`](../../sessions/dc/dccc24c0595dccae80b3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

| GPU | 任务 | 进度 | running_acc | GPU 利用率 | 显存 |
|-----|------|------|-------------|-----------|------|
| **0** | CLS v5 retrain | **1730/6315** (27%) | — | 98% | 24859 MiB |
| **1** | CWM s42 (epoch 3?) eval | **4463/9784** (46%) | **56.2%** | 50% | 17519 MiB |
| **2** | CWM s42 epoch 2 eval | **1236/9784** (13%) | **66.4%** | 56% | 17851 MiB |
| **3** | CWM s123 eval | **4111/9784** (42%) | **61.3%** | 50% | 17519 MiB |

备注：
- GPU 0 CLS v5 训练 ~9.5s/step，预计还需 ~12h 完成
- GPU 1 的 log 路径为 `/root/autodl-tmp/eval_results/deepseek_cwm_repo_s42_eval.log`（无 epoch 后缀，可能是 epoch 3 或全量 eval）
- GPU 1 的 s42 eval acc 56.2% 明显低于 GPU 2 的 s42 epoch2 eval 66.4%

---
