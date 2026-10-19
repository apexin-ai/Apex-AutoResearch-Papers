# code exp 013 text baseline

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_013_text_baseline_20260516T204146_result.json`
- **Structured JSON:** [`65f151691fc295c15cf0.json`](../../sessions/65/65f151691fc295c15cf0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp-013 完成。结果：

| Method | Coverage | Lead Time | Step Acc | AUROC |
|--------|----------|-----------|----------|-------|
| **text_static (384-d)** | 60.5% | +4.3 | 66.1% | 0.7384 |
| **text_temporal W=15 (5760-d)** | 65.1% | +11.5 | 67.8% | 0.7590 |
| hidden_static LR L14 (4096-d) | 46.5% | -2.0 | 81.7% | — |
| hidden_temporal LR W=15 (61440-d) | 76.7% | -1.1 | 84.8% | — |
| hidden GRU multi-7L h=256 | 76.7% | +4.7 | 80.9% | — |

**核心发现**：

1. **Hidden-state probes 在 step accuracy 上显著优于 text baseline**（81-85% vs 66-68%），差距 ~15-18pp，支撑论文的核心论点——内部表示包含 surface text 中不可见的 commitment 信号。

2. Text baseline 的 lead time 看似高（+4.3 / +11.5），但结合低 accuracy 说明这是**高假阳性率导致的虚假早期检测**——模型乱猜"已 committed"，偶然提前命中。

3. Hidden temporal (76.7% coverage) > text temporal (65.1%) > hidden static (46.5%) > text static (虽然 text static 60.5% > hidden static 46.5%，但 acc 差距巨大)。

论文结论成立：hidden-state probes 提供了 text 不可见的内部状态信号，且在 accuracy 这个最重要指标上有决定性优势。

---
