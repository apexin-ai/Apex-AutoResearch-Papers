# diagnose eval openvla attn k095 goal seed42

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_openvla_attn_k095_goal_seed42_20260527T053357_result.json`
- **Structured JSON:** [`84e867dad90693ff67a8.json`](../../sessions/84/84e867dad90693ff67a8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

### 失败原因：外部 SIGTERM（非 OOM）

- 日志中**无** OOM、CUDA error、Killed、Exception 任何错误信息
- 最后一行是 `Terminated` + `EXIT_CODE=143`（SIGTERM），说明进程被外部信号杀掉
- 最可能原因：**另一个进程抢占了 GPU 1**。当前 GPU 1 上跑的是 PID 972716：`python -u eval_pi05_pruning_libero.py --prune_mode none --suite libero_goal --gpu 0`（注意这个进程声明 `--gpu 0` 但实际跑在 GPU 1 上，可能是 CUDA_VISIBLE_DEVICES 映射）。这个进程启动时间是 12:58，可能在启动时把原来的实验进程挤掉/kill 了

### 进度

- **完成：3/10 tasks（150/500 episodes）**，约 30% 进度
  - Task 1: SR=0.580 (29/50)
  - Task 2: SR=0.920 (46/50)  
  - Task 3: SR=0.840 (42/50)
  - Task 4: 跑到 Ep 40/50 时被杀

### 结果可恢复性

- **无持久化的部分结果**。没有 results 文件生成，只有日志中的打印输出。可以从日志解析前 3 个 task 的 SR，但 task 4-10 需要重跑。

### 重试策略

1. 确认 GPU 1 当前进程（PID 972716）是什么实验、谁启动的，避免冲突
2. 重跑时显式指定空闲 GPU，或等当前 4 卡都有任务跑完后再启动
3. 如果脚本支持断点续跑（从 task 4 开始），用 `--start_task 4` 之类的参数节省时间；否则全量重跑约需 ~8 小时（按 1.3 eps/min 估算 500 episodes）
4. 用 `nohup` 或 `tmux` 保护进程，并在脚本中加 `trap` 处理 SIGTERM 以保存中间结果

---
