# diag qwen7b arc s42 completion

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_qwen7b-arc-s42-completion_20260520T173308_result.json`
- **Structured JSON:** [`01a0f342813a26e7f572.json`](../../sessions/01/01a0f342813a26e7f572.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成（DONE/success），cron 已无残留。

## 结果汇总 + 跨种子 V-recovery 分析

**Qwen-7B ARC-Challenge 完整结果：**

| Dosage | s42 | s123 | 种子差 |
|--------|-------|-------|--------|
| d000 (base) | 87.88% | 87.12% | +0.76 |
| d005 | 86.09% | 82.42% | +3.67 |
| d025 | 84.04% | 85.15% | -1.11 |
| d050 | 84.56% | 85.07% | -0.51 |
| d100 | 84.98% | 84.73% | +0.25 |
| **Δ(d100-d000)** | **-2.90pp** | **-2.39pp** | |

**跨种子稳定性分析：**

1. **Δ(d100) 方向一致**：两个种子均为负（s42=-2.90pp, s123=-2.39pp），确认 ARC 上 contamination 导致净性能下降，方向跨种子稳定。

2. **V-shape 不跨种子稳定**：s123 在 d005 出现剧烈暴跌 -4.70pp 后恢复（经典 V-shape），但 s42 的 d005 仅下降 -1.79pp，呈**单调递降到 d025 后微回升**的形态，更接近 U-shape。d005 的种子间差异高达 3.67pp，是所有 dosage 中最大的。

3. **d025-d100 区间趋于一致**：排除 d005 后，两个种子在 d025/d050/d100 的绝对值差距均 <1.1pp，说明中高 dosage 下行为收敛。

4. **结论**：ARC 上 contamination 的净负效应（Δ≈-2.5 to -3pp）跨种子稳定，但低 dosage（d005）的 V-shape 剧烈程度依赖 SFT 随机种子，不宜作为 robust finding 报告。d005 的高方差暗示极低 dosage 下 contamination 对 ARC MCQ 格式的影响不稳定。

---
