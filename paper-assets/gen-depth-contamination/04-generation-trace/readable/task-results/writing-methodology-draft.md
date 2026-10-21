# writing methodology draft

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_methodology_draft_20260512T162448_result.json`
- **Structured JSON:** [`6dbdda097f2e9e64849f.json`](../../sessions/6d/6dbdda097f2e9e64849f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Methodology 初稿已写入 `docs/methodology_draft.md`。

涵盖四个 subsection：
- **3.1** 形式化定义、prompt-chain 实现（含精确 prompt 模板）、模型选择理由、解码参数、种子数据、left-padding
- **3.2** 三组 15 维特征的精确公式——surprisal 9D（含一阶/二阶差分）、vocab diversity 3D（TTR/hapax/self-BLEU）、tail-thinning 3D（kurtosis/entropy/LFR），全部从 `run_pipeline.py` 提取
- **3.3** LightGBM 选择理由、pairwise + ordinal 两级评估、5-fold CV 协议、四项指标
- **3.4** $K^*$ 操作性定义（AUC > 0.60）、阈值理由、DPI 理论联系（含 contraction rate scaling）、JSD proxy 及其局限、科学意义

标注了 3 处 `[TODO]` 待补充实验数据，1 处 `[需验证]` 标注不确定的引用。还标注了 doc\_id grouped CV 的设计缺陷需在正式实验中修复。

---
