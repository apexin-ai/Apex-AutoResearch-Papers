# diagnose exp 015 failure

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_015_failure_20260514T025629_result.json`
- **Structured JSON:** [`533c3de4b4bcb1383b9e.json`](../../sessions/53/533c3de4b4bcb1383b9e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整诊断如下：

---

## exp-015 诊断结果

### 1. 失败根因：CUDA OOM

```
torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 26.00 MiB.
GPU 0 total: 23.52 GiB
  Process 55665 (其他实验): 13.36 GiB
  Process 56371 (exp-015 Qwen模型): 9.09 GiB
  Free: 20.06 MiB → 需要 26.00 MiB → 失败
```

exp-015 加载 Qwen2.5-1.5B（`device_map="auto"`, 90% GPU 内存），加上另一个进程占 13.36 GiB，GPU 完全打满。脚本在处理 **Pythia 数据集的第一个 batch** 时 OOM 崩溃。

### 2. 日志包含两次运行

日志中 OOM traceback 后有大量 null bytes（`\x00`），然后是 Qwen-cont 的成功运行。说明：
- **第一次运行**：3 个数据集 → Pythia 第一个 batch OOM，脚本无 try/except，直接崩溃。Pythia/OLMo/Qwen-cont 均未完成。
- **第二次运行**（被追加到同一日志）：仅 Qwen-cont → 成功完成 → SIGHUP 退出

### 3. EXIT_CODE=129 (SIGHUP)

第二次运行实际上**跑完了**并写出了结果，SIGHUP 发生在输出 SUMMARY 之后，不影响数据完整性。可能是 SSH 断连或 tmux 会话被关闭。

### 4. 结果状态

| 数据集 | 状态 | 结果 |
|--------|------|------|
| Pythia | OOM 崩溃 | 无 |
| OLMo | 未执行 | 无 |
| Qwen-cont | 完成 | K\*(neural)=3, K\*(lgbm)=2, acc=0.4335 |

Qwen-cont 结果已写入 `artifacts/exp015_neural_probe_results.json`。

### 5. 数据目录：完整

| 目录 | 大小 | 文件 |
|------|------|------|
| data_exp001_pythia | 36M | depth_0-5.jsonl + features.csv |
| data_exp002_olmo | 41M | depth_0-5.jsonl + features.csv |
| data_exp017_qwen_cont | 43M | depth_0-5.jsonl + features.csv |

### 6. 当前 GPU 状态

- RTX 4090 D, 24564 MiB total
- 当前占用：3852 MiB（PID 57675, python3）
- **空闲 ~20.7 GiB** — 足够重跑

### 修复建议

1. **先确认 PID 57675 是什么**，如果可以释放则释放；Qwen 模型需要 ~9 GiB，当前空间足够
2. **脚本加 per-dataset try/except**，一个数据集失败不影响其他
3. **重跑 Pythia + OLMo**：当前 GPU 有足够空间
4. 用 `nohup` 或确保 tmux 会话稳定，避免再次 SIGHUP

---
