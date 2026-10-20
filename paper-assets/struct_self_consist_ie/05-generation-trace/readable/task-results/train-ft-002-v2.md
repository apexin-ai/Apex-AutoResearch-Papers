# train ft 002 v2

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_ft_002_v2_20260514T080903_result.json`
- **Structured JSON:** [`2087f86a71df013aa7ef.json`](../../sessions/20/2087f86a71df013aa7ef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

5 分钟监控完成，训练稳定运行。

## ft_002v2 训练报告

| 项目 | 值 |
|------|-----|
| **PID** | 24947 |
| **GPU** | cuda:1, 26804 MiB / 32607 MiB (~82%) |
| **当前进度** | step 132/585 (22%) |
| **速度** | ~2.8s/it |
| **checkpoint** | checkpoint-100 已保存 ✓ |

**Loss 趋势**（每 10 step 记录）：

| Step | Loss | Epoch |
|------|------|-------|
| 10 | 0.7721 | 0.09 |
| 20 | 0.2694 | 0.17 |
| 30 | 0.1639 | 0.26 |
| 40 | 0.1438 | 0.34 |
| 50 | 0.1253 | 0.43 |
| 60 | 0.1193 | 0.52 |
| 70 | 0.1143 | 0.60 |
| 80 | 0.1038 | 0.69 |
| 90 | 0.1064 | 0.77 |
| 100 | 0.1001 | 0.86 |

Loss 从 0.77 快速降至 0.10，收敛良好。OOM 问题已解决——已安全通过原崩溃点 step 70。

**预估完成时间**：剩余 453 steps × 2.8s ≈ 21 分钟，约 16:37 完成。

---
