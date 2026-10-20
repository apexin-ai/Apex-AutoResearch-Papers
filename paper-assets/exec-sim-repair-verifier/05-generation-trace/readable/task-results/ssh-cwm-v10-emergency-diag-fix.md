# ssh cwm v10 emergency diag fix

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_cwm-v10-emergency-diag-fix_20260512T235446_result.json`
- **Structured JSON:** [`bffabef3567e5f7b72f0.json`](../../sessions/bf/bffabef3567e5f7b72f0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

### 1. PID 105205：完整训练，正常运行
- **身份**：`train_repo_cwm.py`，从 checkpoint-200 resume，**max_steps=6633（3 epochs 完整训练）**，NOT dry-run
- **当前状态**：运行 ~30min，step **300/6633 (4.5%)**，正在做 eval（~76% 完成）
- **GPU 2**：96% 利用率，21GB 显存占用

### 2. PID 106086：已死
不再运行。registry 记录的 v10 fresh start 进程已退出，对当前训练无影响。

### 3. trainer_state.json 真相
| 文件 | max_steps | global_step | should_training_stop |
|---|---|---|---|
| checkpoint-**205** | **205** | 205 | **true** |
| checkpoint-**200** | **6633** | 200 | **false** |

**checkpoint-205 是旧 dry-run 的产物**，造成了误判。当前进程从 checkpoint-200 resume，使用的是 max_steps=6633。

### 4. 未启动新训练
不需要。当前 PID 105205 就是完整训练，一切健康。

### 5. 最新 loss
- step 250：loss=**6.71**，lr=7.5e-5
- step 300：loss=**4.80**，lr=9.0e-5
- 趋势正常下降（从 step 50 的 28.20 → step 300 的 4.80）

### 6. ETA
~**26.5h** 剩余（含 63 次 eval，每次 ~730s）。预计完成时间约 5/14 02:30 UTC。

### 关键结论
**Reviewer 的 dry-run 担忧是误报**。checkpoint-205 的 trainer_state.json 遗留了 max_steps=205，但当前进程使用的是 checkpoint-200 的状态（max_steps=6633）。ps etime `16:09` 是 16 分 9 秒，不是 16 小时。训练完全正常。

---
