# exp 010 selection curves

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_010_selection_curves_20260514T144948_result.json`
- **Structured JSON:** [`39835e26d8acc63032fb.json`](../../sessions/39/39835e26d8acc63032fb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。图表和数据已注册。结果分析：

## 核心发现

**1. 哪个信号 N 增加时 F1 增幅最大？**
- **NER (SciERC/CoNLL)**: SJ、FK、logprob 几乎并列（Δ≈+0.02~0.03），差距极小
- **RE (SciERC)**: logprob 最佳（+0.055），voting_conf 次之（+0.053），SJ/FK 相对弱（+0.04）

**2. Saturation point？**
- 所有信号在 N=8 后增长明显放缓。NER SciERC 从 N=8→16 各信号仅提升 <0.01
- RE 的 oracle 仍在快速增长（+0.05 from N=8→16），说明不是数据瓶颈，而是信号能力不足

**3. SJ vs logprob gap 随 N 变化**
- NER: SJ 和 logprob 在 N=16 几乎相同（0.620 vs 0.621）——consistency 和 confidence 信号等价
- RE: logprob 在所有 N 值持续领先 SJ 约 +0.01~0.02——关系抽取中模型内部信心比跨样本一致性更有效

**4. NER vs RE 的 scaling 差异**
- RE 的 oracle headroom 远大于 NER（+0.275 vs +0.189），但实际信号只恢复了约 15-20% 的 headroom
- RE 是更难的任务，信号的绝对改善空间更大，但相对效率低

**5. 一个反常结果**: NER SciERC 的 voting_conf 随 N 增加反而**下降**（0.598→0.585）——在该数据上基于投票置信度的选择不如随机。

**输出文件**:
- PDF/PNG: `artifacts/exp_010_selection_curves/chart/fig_selection_curves.pdf`
- 指标: `artifacts/exp_010_selection_curves/data/exp010_metrics.json`

---
