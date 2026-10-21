# analysis d23 edd bootstrap

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d23_edd_bootstrap_20260515T114730_result.json`
- **Structured JSON:** [`8cc380e901e881b82773.json`](../../sessions/8c/8cc380e901e881b82773.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。结果总结：

## D023 Bootstrap 单尾检验结果

| 模型 | d3v4 AUC | Bootstrap Mean | 95% CI | p-value (H0: AUC ≤ 0.75) |
|------|----------|---------------|--------|---------------------------|
| **Pythia-1.4B** | 0.784 | 0.784 | [0.765, 0.802] | **0.001** |
| **GPT-2 XL** | 0.750 | 0.750 | [0.728, 0.771] | 0.505 |
| **OLMo-1B** | 0.765 | 0.765 | [0.744, 0.785] | 0.091 |

**解读**：
- **Pythia**: p=0.001, 强显著，AUC 显著 > 0.75，支持 EDD=4 的声称
- **GPT-2 XL**: p=0.505, AUC 恰好在阈值上，无法拒绝 H0。论文需诚实报告
- **OLMo**: p=0.091, 边际显著（α=0.10 水平），95% CI 下界 0.744 < 0.75

**产出**：
- 脚本：`src/d23_edd_bootstrap.py`
- 结果：`results/d23_edd_bootstrap.json`

**注意**：Pythia 使用了原始 pipeline 的特征数据（`data/features_all.jsonl` + `data/features_depth_4.jsonl`），因为 `pythia_depth_extension/features_6class.jsonl` 是不同 pipeline 产生的特征，AUC 仅 0.724。GPT-2 XL 和 OLMo 使用各自的 `features_6class.jsonl`，与原始 binary pairwise 评估完全一致。

---
