# monitor seetacloud eval status

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_seetacloud-eval-status_20260517T181824_result.json`
- **Structured JSON:** [`790f973ba71445cc32ba.json`](../../sessions/79/790f973ba71445cc32ba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总报告

### GPU 状态

| GPU | 任务 | PID | 进度 | Running Acc | VRAM | Util | 预计剩余 |
|-----|------|-----|------|-------------|------|------|----------|
| **0** | CLS v4 (ckpt-4422, seq8192) | 664774 | 1840/9784 (18.8%) | 69.8% | 32048/32607 MiB | 91% | **~7.9h** |
| **1** | CWM s42 (best, seq4096) | 662946 | 582/9784 (5.9%) | 59.8% | 17345/32607 MiB | 54% | **~30.7h** |
| **2** | CLS s123 (best, seq8192) | 665019 | 1640/9784 (16.8%) | 73.5% | 32048/32607 MiB | 90% | **~9.1h** |
| **3** | CWM s123 (ckpt-8844, seq4096) | 668680 | 228/9784 (2.3%) | 64.5% | 17345/32607 MiB | 62% | **~31.9h** |

**速率估算**：CLS ~15-17 samples/min (batch=4, seq8192)；CWM ~5 samples/min (batch=1, seq4096)。CWM 慢约 3 倍，预计需要跑到明天下午。

### 已完成的 eval 结果

**CLS s123 (best ckpt, seq2048)** — 此前已完成的一轮（短 context）:

| Metric | Value |
|--------|-------|
| Accuracy | **82.62%** |
| Majority baseline | 72.96% |
| Gap vs majority | +9.67pp |
| F1 (macro) | 71.35% |
| F1 (fail/pass) | 53.37 / 89.32 |
| Precision (fail/pass) | 97.3 / 80.95 |
| Recall (fail/pass) | 36.77 / 99.62 |
| Unparseable | 2796/9784 (28.6%) |

当前的 seq8192 重跑就是为了降低这个 28.6% unparseable rate。

### 磁盘

| 挂载点 | 总量 | 已用 | 可用 | 使用率 |
|--------|------|------|------|--------|
| / (overlay) | 30G | 21G | 9.4G | 69% |

`/autodl-tmp` 不存在（未挂载数据盘），所有数据都在 root overlay 上。9.4G 剩余空间需关注，4 个 eval 同时写 predictions 可能会继续增长。

---
