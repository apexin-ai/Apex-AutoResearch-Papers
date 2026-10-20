# ssh d049 investigate cuda1

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_d049-investigate-cuda1_20260513T100559_result.json`
- **Structured JSON:** [`cae6813ad0bdf3276419.json`](../../sessions/ca/cae6813ad0bdf3276419.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 调查结果

### 1. PID 139302
**已死亡**，进程不存在。之前占用 cuda:1 的 16.3GB 显存已被释放。cuda:1 当前 0 MiB 占用。

### 2. 当前 GPU 进程

| PID | GPU | 显存 | 运行时间 | 命令 |
|-----|-----|------|---------|------|
| 130031 | cuda:2 | 13,466 MiB | 1h46m | `train_repo_cwm.py` → `/root/autodl-tmp/checkpoints_repo_cwm_v11/` |
| 140060 | cuda:3 | 25,734 MiB | 6m15s | `train_repo_verifier_8b.py` (Qwen3-8B) → `/root/autodl-tmp/checkpoints_repo_cls_8b/` |

### 3. 全面 GPU 状态

| GPU | 利用率 | 显存占用 / 总量 |
|-----|--------|----------------|
| cuda:0 | 0% | 0 / 32,607 MiB (空闲) |
| cuda:1 | 0% | 0 / 32,607 MiB (空闲) |
| cuda:2 | 98% | 13,475 / 32,607 MiB |
| cuda:3 | 86% | 25,743 / 32,607 MiB |

**结论**：PID 139302 已自行退出，无需 kill。cuda:0 和 cuda:1 完全空闲可用。cuda:2 和 cuda:3 上跑的都是本项目的训练任务，状态正常。

---
