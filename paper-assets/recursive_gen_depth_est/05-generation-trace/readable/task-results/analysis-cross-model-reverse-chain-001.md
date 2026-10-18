# analysis cross model reverse chain 001

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cross_model_reverse_chain_001_20260516T142302_result.json`
- **Structured JSON:** [`d10068a4fe89c6bdf5a2.json`](../../sessions/d1/d10068a4fe89c6bdf5a2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。

## 结果摘要

**cross_model_reverse_chain_001 → SUCCESS**

| | LR | RF |
|---|---|---|
| 4-class acc | **86.75%** [83.3, 89.8] | **85.75%** [82.0, 89.3] |

关键发现：

- **远超阈值**：86.8% vs 55% 成功标准，vs 25% 随机基线
- **超越同架构单模型**：reverse chain 86.8% > GPT2-XL 单模型 83.3%（5000 samples） > OLMo 78.8%，且本实验仅用 500 samples/depth
- **超越 LOO cross-model**：86.8% vs cross_model_loo_001 的 66.4%
- **AUC 模式一致**：d1v2 仍是最难 pair（0.886），d0 vs 任意 depth 近乎完美（≥0.988）
- **特征不变**：var_surprisal + p90_ppl 主导，与所有先前实验一致

**N4 结论**：Depth signal 在 reverse chain（GPT2-XL→OLMo→Pythia）中跨架构传递，且信号强度不弱于单模型。强力支持 cross-model generalization claim。

Registry 已更新为 DONE/success，分析报告已注册为 artifact。

---
