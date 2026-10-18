# analysis atlas v2 formal

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_atlas_v2_formal_20260515T041305_result.json`
- **Structured JSON:** [`4cd6fa6c24a8939723c7.json`](../../sessions/4c/4cd6fa6c24a8939723c7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Atlas v2 9-cell analysis 已全部完成。4 个 JSON artifact 均已注册，registry 状态 DONE/success。

核心结果：
- **p90_ppl** top-2 命中率 9/9 (100%)
- **var_surprisal** top-2 命中率 7/9（gpt2xl_temp09 和 gpt2xl_topk50 被 p75_ppl 替代）
- **EDD=3 @T=0.75**: 7/9（pythia_topk50 和 olmo_topk50 的 d2v3 AUC 分别为 0.686 和 0.734，未达阈值）
- **跨模型 rank 相关性**: 均值 0.868，范围 [0.619, 0.954]
- **4-class CV5 准确率**: 范围 [0.688, 0.859]

如需进一步分析或可视化，随时说。

---
