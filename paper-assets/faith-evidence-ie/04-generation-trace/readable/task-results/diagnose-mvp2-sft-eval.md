# diagnose mvp2 sft eval

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_mvp2_sft_eval_20260514T124719_result.json`
- **Structured JSON:** [`9ad6179b41209463953d.json`](../../sessions/9a/9ad6179b41209463953d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

### 1. mvp2_sft_eval 失败根因

**收到 SIGHUP 信号被终止**，在 batch 36/247（~14.6%，运行约 56 分钟）时被 `Terminated`。日志末尾无 OOM、CUDA error 或 Python traceback，是外部信号杀死的进程。

证据行：
```
Inference:  15%|█▍  | 36/247 [56:09<5:36:40, 95.74s/it]Terminated
EXIT_CODE=129
```

EXIT_CODE=129 = SIGHUP。可能原因：
- tmux/screen session 断开导致 shell 收到 HUP
- AutoDL 平台层面的进程管理（如实例休眠/资源回收）
- SSH 连接断开且进程未做 nohup 保护（但从 trap 设置看已有 HUP 处理，说明是 wrapper shell 自身收到了信号）

### 2. mvp2_sft_eval_r2 状态

**正在运行**（PID 55410，已运行约 2 分钟）。模型已加载完毕，正在推理阶段（0/62 batches）。注意 r2 用了 `batch_size 16`（r1 用的是 4），所以总 batch 数从 247 降到 62，预计运行时间约 **1.5-2 小时**。使用 GPU 1，显存占用 8469 MiB / 32607 MiB，带 `--quantize` 标志。

### 3. 其他实验健康状态

三个 GRPO 实验全部存活，已运行约 15 小时 50 分钟：

| 实验 | PID | GPU | 运行时间 | 状态 |
|------|-----|-----|---------|------|
| grpo_ced_r5 | 53066 | GPU 0 (13061/32607 MiB, 46%) | 15:51 | ✓ Running |
| grpo_extract_r3 | 53144 | GPU 2 (13061/32607 MiB, 51%) | 15:48 | ✓ Running |
| grpo_flatnli_r3 | 53287 | GPU 3 (13061/32607 MiB, 44%) | 15:44 | ✓ Running |

### 4. 建议下一步

- **r2 已在跑，无需干预**，batch_size=16 + quantize 预计 ~2 小时完成，等它跑完即可
- r1 的 SIGHUP 根因大概率是 AutoDL 平台侧事件或 tmux session 异常断开。如果 r2 也出现相同问题，需要检查 AutoDL 实例是否有自动休眠策略

---
