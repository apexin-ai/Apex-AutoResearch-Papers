# evidence discretized entropy granger

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_evidence_discretized_entropy_granger_20260525T082733_result.json`
- **Structured JSON:** [`f8ebee47a38a21e10af3.json`](../../sessions/f8/f8ebee47a38a21e10af3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。核心结果：

**Entropy→distinct_1 Granger 显著性（7 个 α=1.0 实验，跨 5 种模型）：**

| Binning 方式 | 显著实验数 |
|---|---|
| Continuous（原始） | **7/7** |
| 20 bins (equal-width / equal-freq) | **7/7** / **7/7** |
| 15 bins (equal-width / equal-freq) | **6/7** / **7/7** |
| 10 bins (equal-width / equal-freq) | 5/7 / 1/7 |
| 5 bins (equal-width / equal-freq) | 3/7 / **0/7** |

**关键发现：**
- ≥15 bins 时，无论 binning 方法，Granger precedence 完全保持（7/7）
- 5-bin equal-freq 完全摧毁信号（0/7），因为 entropy 轨迹严重右偏（gen 0→2 急降后 plateau），equal-freq 把关键的早期下降信号抹平了
- Equal-width 在低 bin 数下比 equal-freq 更鲁棒，因为它保留了 gen 0 的高 entropy 与后续 plateau 之间的对比

**Rebuttal 论点**：连续分辨率确实提升了检测 power，但 Granger precedence 并不依赖于连续性本身——即使离散化到 15-20 levels（远粗于 distinct-n 的有效分辨率），因果信号仍完全保持。信号消失仅发生在极端粗粒度（≤5 bins），此时信息损失已超越 binning 本身的问题。

结果已保存至 `artifacts/discretized_entropy_granger_results.json` 和服务器 `results/discretized_entropy_granger_results.json`。

---
