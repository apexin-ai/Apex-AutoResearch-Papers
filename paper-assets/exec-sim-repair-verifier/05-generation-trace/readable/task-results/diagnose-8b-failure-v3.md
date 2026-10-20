# diagnose 8b failure v3

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_8b-failure-v3_20260514T145833_result.json`
- **Structured JSON:** [`25931ab1186d68f913b6.json`](../../sessions/25/25931ab1186d68f913b6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

### 当前状态：两个实验已被成功重启，正在正常训练

| 实验 | PID | GPU | 显存 | Util | 起始步 | 当前进度 | 启动时间 (CST) |
|------|-----|-----|------|------|--------|----------|---------------|
| CWM 8B | 245775 | GPU 2 | 21.2/32.6 GiB | 95% | ckpt-1200 | ~1300/6633 (20%) + eval中 | 22:28 |
| CLS 8B | 248041 | GPU 3 | 26.7/32.6 GiB | 92% | ckpt-2400 | ~2460/6633 (37%) | 22:46 |

### ~14:16 UTC (22:16 CST) 失败根因

**原始训练日志已被多次重启覆盖，无法找到原始 crash traceback。** 但从恢复过程的证据可以推断：

1. **外部终止（非代码 bug）**：没有任何残存日志包含原始运行的 traceback。进程被外杀时不会留下 Python traceback，这与之前 D070-D073 的 "Worker 误杀子进程 / 平台 SIGTERM" 模式一致。

2. **GPU 内存未释放导致连锁 OOM**：`/tmp/cls-8b-s123-recover.log` 记录了 22:32 CST 的恢复尝试失败——在 `model.to(device)` 时 OOM，因为 PID 243778（原始进程的残留）仍占用该 GPU 26.11 GiB。这说明原始进程被 kill 后，GPU 内存没有立即释放。

3. **多次重启尝试**：22:17 → 22:21 → 22:27 → 22:28(CWM 成功) → 22:34 → 22:46(CLS 成功)。CWM 恢复较快（12分钟），CLS 因 GPU 内存释放慢延迟了约 30 分钟。

### 影响范围

- **数据无损失**：CWM 从 ckpt-1200 resume，CLS 从 ckpt-2400 resume，checkpoint 完好
- **训练进度损失**：CWM 丢失了 ckpt-1200 之后约 145 步（~29分钟的训练），CLS 丢失了 ckpt-2400 之后约 30 步（~4分钟的训练）
- **当前运行稳定**：两个实验已正常训练 30+ 分钟，loss 正常（CWM: 0.51-0.54, CLS: 0.88）

### 是否可通过简单修复重启

**无需修复——已经在跑了。** 根因是外部 kill 而非代码问题，`dataloader_num_workers=0` 的 workaround 仍在生效。如果再次被平台 kill，同样可以从最新 checkpoint resume。

---
