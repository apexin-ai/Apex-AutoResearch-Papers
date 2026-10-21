# exp feat ablation parallel

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_feat_ablation_parallel_20260515T193305_result.json`
- **Structured JSON:** [`36932daa56610965d315.json`](../../sessions/36/36932daa56610965d315.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**实验已全部完成，无需加速。**

状态：
- PID 473989 已结束
- `forward_selection.json` 包含全部 9 个 cells（9 cells × 19 steps × 2 = 342 个 "feature" 条目，完整）
- 所有产出文件齐全：`forward_selection.json`、`forward_selection_curve.pdf/png`、`summary.json`、`correlation_heatmap`、`vif` 等
- 最后文件写入时间 03:31（今天），说明脚本已正常跑完

关键结果摘要（来自 summary.json）：
- 全 19 特征平均准确率：**78.47%**（std 4.94%）
- Top-5 特征即达 **76.78%**（95% full 性能）
- 达到 95% full 的平均特征数：**4.2**（最多 5）
- 9 个 cell 最佳类别全部是 **perplexity**
- Forward selection 首选特征：Pythia → `var_surprisal`，GPT2-XL/OLMo → `p90_ppl`

---
