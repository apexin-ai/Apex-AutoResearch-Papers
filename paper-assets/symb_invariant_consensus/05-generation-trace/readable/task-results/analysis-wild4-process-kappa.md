# analysis wild4 process kappa

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_wild4-process-kappa_20260520T080636_result.json`
- **Structured JSON:** [`133f4b9e83033605d2f5.json`](../../sessions/13/133f4b9e83033605d2f5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果摘要：

| 指标 | 值 |
|------|-----|
| **Fleiss' κ (3-cat, empty→Unknown)** | **0.4093** |
| Fleiss' κ (4-cat) | 0.3294 |
| Fleiss' κ (3-cat, empty excluded) | 0.5006 |
| Mean answer agreement (P_i) | 0.51 ± 0.22 |
| **Mean process cosine similarity** | **0.6902 ± 0.10** |
| Pearson r(agreement, similarity) | -0.064 (p=0.36, **不显著**) |
| Spearman ρ | -0.047 (p=0.51, **不显著**) |
| **Same answer, different process (cos<0.5)** | **9.3%** (616/6605 pairs) |

关键发现：
- Answer-level κ ≈ 0.41（与预期 0.44 基本一致，差异来自空答案处理方式）
- Process similarity (0.69) 远高于 answer agreement (0.51)——CoT 文本的表面相似度高于答案一致性
- **答案一致性与过程相似度之间几乎没有相关性**（r=-0.06, p=0.36），说明过程相似不等于答案一致
- 9.3% 的同答案 pair 实际推理路径差异大（cosine<0.5），即"殊途同归"现象存在但不算很普遍

文件位置：
- 服务器完整结果：`/root/symb_invariant_consensus/results/wild4_process_kappa/results.json`
- 本地摘要：`artifacts/wild4_process_kappa_results.json`
- 脚本：`/root/symb_invariant_consensus/analysis_process_kappa.py`

---
