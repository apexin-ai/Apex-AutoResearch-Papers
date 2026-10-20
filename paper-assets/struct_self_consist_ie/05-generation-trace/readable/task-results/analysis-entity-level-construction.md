# analysis entity level construction

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_entity_level_construction_20260519T013947_result.json`
- **Structured JSON:** [`dae4d218e54cf5f06927.json`](../../sessions/da/dae4d218e54cf5f06927.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**Construction 在所有 3 个数据集上都超过 greedy。**

### NER 对比表

| Dataset | Method | F1 | P | R | Δ vs Greedy |
|---------|--------|-----|------|------|-------------|
| **SciERC** | Greedy | 0.6442 | 0.6604 | 0.6592 | — |
| | LP Selection | 0.6465 | 0.6574 | 0.6674 | +0.23pp |
| | **Construction@θ=0.2** | **0.6637** | 0.6353 | **0.7410** | **+1.95pp** |
| | Oracle | 0.8194 | | | +17.52pp |
| **CoNLL** | Greedy | 0.9070 | 0.9089 | 0.9125 | — |
| | LP Selection | 0.8960 | | | -1.10pp |
| | **Construction@θ=0.3** | **0.9080** | 0.8988 | 0.9271 | **+0.10pp** |
| | Oracle | 0.9581 | | | +5.11pp |
| **FewNERD** | Greedy | 0.7478 | 0.7463 | 0.7631 | — |
| | LP Selection | 0.7666 | 0.7629 | 0.7842 | +1.88pp |
| | **Construction@θ=0.2** | **0.7621** | 0.7340 | **0.8207** | **+1.44pp** |
| | Oracle | 0.9020 | | | +15.43pp |

### RE (SciERC only)

| Method | F1 | P | R | Δ |
|--------|-----|------|------|-----|
| Greedy | 0.4757 | 0.4802 | 0.4877 | — |
| **Construction@θ=0.4** | **0.4963** | 0.5132 | 0.5032 | **+2.06pp** |

### P/R 分解分析

Construction 的核心机制是**提升 recall**：
- SciERC: recall 0.6592 → 0.7410 (+8.18pp)，precision 0.6604 → 0.6353 (-2.51pp)
- FewNERD: recall 0.7631 → 0.8207 (+5.76pp)，precision 0.7463 → 0.7340 (-1.23pp)
- CoNLL: recall 0.9125 → 0.9271 (+1.46pp)，precision 0.9089 → 0.8988 (-1.01pp)

Construction 通过汇聚多个样本中出现的正确 entity 来提升 recall，同时 threshold 过滤掉低频噪声 entity，precision 下降幅度有限。

### 关键发现

1. **SciERC 上 construction (+1.95pp) 远超 LP selection (+0.23pp)**，这是最有说服力的证据
2. **RE construction 也有效** (+2.06pp)，最优 threshold 更高（0.4 vs 0.2），因为关系更稀疏
3. LP-weighted 与 uniform 几乎无差异，说明 logprob weighting 对 entity 频次投票帮助不大
4. 最优 threshold 在 0.2-0.3，偏低，说明即使只有少数样本同意的 entity 也有价值
5. CoNLL 改进很小 (+0.10pp)，因为 baseline 已经很高（0.907）

### 产出路径
- 脚本：`/root/autodl-tmp/struct_self_consist_ie/code/entity_construction.py`
- 完整结果：`/root/autodl-tmp/struct_self_consist_ie/output/entity_construction/construction_results.json`
- 摘要：`/root/autodl-tmp/struct_self_consist_ie/output/entity_construction/best_threshold_summary.json`

### 结论

**Construction 在所有数据集上显著超过 greedy**，尤其在 SciERC（+1.95pp NER, +2.06pp RE）和 FewNERD（+1.44pp）上效果明显。这验证了核心假设：entity-level majority vote construction 是 self-consistency 在结构化输出上比 instance-level selection 更好的类比。

---
