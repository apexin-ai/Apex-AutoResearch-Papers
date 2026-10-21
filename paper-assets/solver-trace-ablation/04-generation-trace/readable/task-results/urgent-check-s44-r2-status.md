# urgent check s44 r2 status

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_urgent_check-s44-r2-status_20260515T191547_result.json`
- **Structured JSON:** [`6ecdc44900c38f5b46cf.json`](../../sessions/6e/6ecdc44900c38f5b46cf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已有完整记录（含 eval 和 taxonomy metrics，conclusion=negative）。

---

## 状态报告：plan018-additive-random-b01-s44-r2

| 项目 | 状态 |
|------|------|
| **进程** | 已完成退出，EXIT_CODE=0 |
| **训练** | 500/500 步，耗时 1h23m |
| **GPU** | cuda:1 已释放 (0 MiB) |
| **磁盘** | 167G/250G (67%), 84G 可用 |

### 训练 Final Stats
- prove_rate: 0.647, mean_isr: 0.081, loss: 0.009

### Eval (proofwriter_fol_100.jsonl)
- **Proved: 89/100 (89%)**
- **Mean ISR: 0.0619 ± 0.1756, Median ISR: 0.0**

### Taxonomy
| 类别 | 数量 | 占比 (of 89 proved) |
|------|------|-----|
| H7 (tautology) | 0 | 0% |
| H1 (conclusion-in-premise) | 73 | 82.0% |
| H8 (conj-collapse) | 16 | 18.0% |
| **Genuine** | **6** | **6.7%** |
| Content-independent | 18 | 20.2% |

### 判断
训练已正常完成，cron 实际已检测到并完成了 eval+taxonomy（registry 中 metrics 已填充，conclusion=negative）。Genuine rate 仅 6.7%，H1 高达 82%，符合 random baseline 的预期表现。

---
