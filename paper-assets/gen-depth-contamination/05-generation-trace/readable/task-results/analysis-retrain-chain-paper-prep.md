# analysis retrain chain paper prep

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_retrain-chain-paper-prep_20260519T025458_result.json`
- **Structured JSON:** [`1b549f2f47b01ebeffaf.json`](../../sessions/1b/1b549f2f47b01ebeffaf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

素材文档已写入 `artifacts/retrain_chain_paper_notes.md` 并注册。核心内容总结：

**数据层面**：
- 完整 7-pair AUC/CI/JSD + per-fold 数值（§A）
- Retrain vs prompt side-by-side 对比表：retrain 在 1v2 处 AUC 高出 +28.6pp (Qwen) / +29.3pp (Pythia)，K\* 差距 5 generations（§B）

**Narrative 层面**（§C）：
- Retrain K\*>>prompt K\* 的机制：LoRA fine-tune 每代引入累积 model-adaptation artifacts（vocabulary narrowing, repetition bias），叠加在 text-intrinsic degradation 之上
- 与 model collapse 文献（Shumailov, Alemohammad）的定位区分：他们关注 model quality degradation，我们关注 discriminability
- 两种 K\* 的 operational 含义：prompt K\*=2 是 data curation boundary（保守/可泛化），retrain K\*=7 是 model archaeology upper bound

**Gap 分析**（§D）：
- 🔴 **正文缺 retrain-chain 专门段落**（目前仅 appendix + limitations 一句话）
- 🔴 **缺 retrain vs prompt 的 side-by-side 对比表**
- 🟡 缺 model collapse 文献的 explicit citation/positioning
- 🟡 Pythia depth extension 结果 pending

**段落建议**（§E）：推荐在 Discussion 加一个 "Retrain-Chain: Upper Bound on Discriminability" 段落（~8 句），cross-reference 已有的 appendix Table 24 和 fig_retrain_decay。

---
