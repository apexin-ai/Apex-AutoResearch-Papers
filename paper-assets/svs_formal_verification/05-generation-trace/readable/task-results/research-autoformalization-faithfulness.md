# research autoformalization faithfulness

**svs formal verification** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_autoformalization-faithfulness_20260514T105550_result.json`
- **Structured JSON:** [`7a9c4dfc33261adfe75b.json`](../../sessions/7a/7a9c4dfc33261adfe75b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已生成并注册：`art_20260514_0e7b10`

**核心发现**：

1. **SVS 受影响程度中等偏低**：arXiv:2604.19459 的 axiom fabrication 主要发生在 proof generation 阶段，SVS 只做 consistency checking 不做 proving，fabrication 动机显著降低。但 **premise mistranslation 是高风险**——DeepSeek 系列模型的主要问题，且几乎不可检测，直接摧毁 PCV 有效性。

2. **SVS 已有的两个天然缓解**：(a) IC 是相对度量用于 chain selection，对系统性偏差有鲁棒性；(b) 85% formalization rate 隐式过滤了最难翻译的 claim。

3. **最值得做的 post-MVP 实验**：
   - **P0**：人工抽样 50 个 claim formalization，量化实际 faithfulness rate（2-3 天）
   - **P1**：Premise roundtrip check（FOL→NL→FOL'→Z3 等价检查），成本低，保护 PCV
   - **P1**：Dual-formalization consistency check，给 IC 加 formalization confidence 权重

4. **论文策略**：Limitations 引用 arXiv:2604.19459 展示问题意识，同时论证 IC graded scoring 比 binary verification (VeriCoT) 对 faithfulness 问题更鲁棒。

---
