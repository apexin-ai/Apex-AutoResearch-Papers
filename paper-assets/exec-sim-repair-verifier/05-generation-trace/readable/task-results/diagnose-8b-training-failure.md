# diagnose 8b training failure

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_8b-training-failure_20260514T141805_result.json`
- **Structured JSON:** [`170b1ab3ac41e0407005.json`](../../sessions/17/170b1ab3ac41e0407005.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。关键发现：**两个实验已经被自动恢复，当前正在运行。**

---

## 诊断结果

### 根因：DataLoader worker 被 SIGTERM 杀死（大概率系统内存压力）

两个实验的错误完全相同：
```
RuntimeError: DataLoader worker (pid XXXXX) is killed by signal: Terminated.
```

- **实验 1 (CWM)**: 在 training step 1300 的 eval 阶段（eval 39% 处）崩溃，运行 8h21m
- **实验 2 (CLS)**: 在 training step 2422（刚完成 step 2400 的 eval+checkpoint 保存后）崩溃，运行 8h22m

**两个实验是同一原因**——几乎同时失败，都是 DataLoader worker 收到 SIGTERM（signal 15，不是 OOM killer 的 SIGKILL/signal 9）。

**最可能的触发条件**：服务器同时跑了 4 个 ML 进程（GPU 0/1 上的两个 4B eval + GPU 2/3 上的两个 8B train），eval 阶段 DataLoader workers 的 CPU 内存峰值叠加，触发系统级内存管理机制向子进程发送 SIGTERM。

排除磁盘满：`/root/autodl-tmp/` 54% (118G 空闲)，`/` 64% (11G 空闲)。

### 最后保存的 Checkpoint

| 实验 | 最后 checkpoint | 时间 | 文件完整性 |
|------|----------------|------|-----------|
| CWM 8B | **checkpoint-1200** | 21:47 | 完整（adapter_model.safetensors + optimizer.pt + trainer_state.json 等齐全） |
| CLS 8B seed123 | **checkpoint-2400** | 22:12 | 完整（同上） |

### 恢复训练状态

**已经自动恢复**。`ps aux` 显示两个实验已在 22:17 从 checkpoint 恢复运行：
- PID 242651: `train_repo_cwm.py --resume_from_checkpoint checkpoint-1200`（CUDA:2）
- PID 242727: `train_repo_verifier.py --resume_from_checkpoint checkpoint-2400`（CUDA:3）

### 建议修复方案

1. **减少 DataLoader workers 数量**：如果当前 `num_workers` > 0，降到 2 或 1，减少内存占用
2. **错开 eval 时间**：两个 8B 训练 + 两个 4B eval 同时跑时 CPU 内存峰值过高，考虑等 eval 任务跑完再重启 8B 训练
3. **监控当前恢复的训练**：已恢复的两个进程仍然面临同样的 4 进程共存环境，可能再次失败

---
