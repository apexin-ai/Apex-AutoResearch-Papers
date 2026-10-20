# research contamination harms performance literature

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_contamination-harms-performance-literature_20260515T050739_result.json`
- **Structured JSON:** [`46b6a41413e59bf7b784.json`](../../sessions/46/46b6a41413e59bf7b784.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调研完成。报告已写入 `artifacts/literature_survey_negative_gamma.md`。

## 核心结论

**负 gamma 现象在文献中没有直接先例，新颖性高。**

具体而言：

1. **有间接支撑但无人做过**：Dekoninck et al. (2024) 提到 contamination 影响可以是"negligible or even negative"，但他们归因于检测误差而非真实现象。DICE (Tu et al., 2024) 证明 in-distribution contamination 导致 OOD 性能下降，但没有做 dose-response 实验。

2. **三个关键机制都有文献基础**：
   - 灾难性遗忘：Kalajdzievski (2024) 的 forgetting scaling law
   - 过训练脆弱性：Springer et al. (2025, ICML) 证明过训练模型更难 fine-tune — **Qwen2.5-0.5B 的 18T tokens / 0.5B params = 36x Chinchilla 恰好是最脆弱的情况**
   - Scale-dependent contamination：Elazar et al. (2024, ICML) 证明小模型从 contamination 获益更少

3. **我们的独特贡献**：
   - 首次在控制实验中观察到 contamination **降低**目标 benchmark 分数
   - 首次用 IRT 的 gamma 参数形式化这个现象
   - 首次将 overtraining fragility 与 contamination 效果联系起来
   - 同一 contamination protocol 下 ARC↓ / GSM8K→ 的 benchmark-specific 异质性未见报道

建议论文中用 **Springer (2025) overtraining + Elazar (2024) scale-dependence + DICE (2024) OOD degradation** 三条线索构建叙事，将负 gamma 定位为这些已知现象的自然但此前未被观察到的极端情况。

---
