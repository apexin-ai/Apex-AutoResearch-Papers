# analysis w6 outlier robustness

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_w6_outlier_robustness_20260515T133503_result.json`
- **Structured JSON:** [`ca8003a281590dd52e91.json`](../../sessions/ca/ca8003a281590dd52e91.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

W6 完成。交付清单：

- **JSON**: `/root/autodl-tmp/pacs/analysis_output/w6_outlier_robustness.json` — 16 conditions × 3 levels (original/w5/w10)，含 outlier profiles、phase MMR、dose-response、paired imp vs rand
- **Report**: `artifacts/w6_outlier_robustness/report.md` — 已更新增强版
- **Script**: `/root/autodl-tmp/pacs/w6_outlier_robustness.py` — 已有文件头注释

**关键结论**:
- D_median、G_ratio、Wilcoxon p 在 5%/10% winsorization 下**完全不变**（15/16 conditions 结论不变，1 个边缘 case 是 Qwen random 条件 p 从 0.10→0.046，反而强化了 importance vs random 的对比）
- Outlier 集中在 intermediate_algebra / precalculus（DeepSeek）和 algebra（Qwen），即最难的数学题型
- 低 sparsity phase 的 skewness 最高（6–20），符合 phase boundary 处少数问题经历不成比例的 compound interaction 的预期
- 审稿人提到的 43:1 ratio 实际上低估了——某些 per-phase random 条件达 97,640:1，但 5% winsorization 后全部降至 ≤13×

---
