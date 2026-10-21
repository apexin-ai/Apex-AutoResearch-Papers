# code prep pythia retrain analysis

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep-pythia-retrain-analysis_20260519T034352_result.json`
- **Structured JSON:** [`96b9b55919a71d6c5e76.json`](../../sessions/96/96b9b55919a71d6c5e76.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本就绪，dry-run 完全通过。核心结果：

**两个模型均 K\*=7（mean 和 CI-conservative 一致）**，确认 retrain K\* >> prompt K\* 跨模型成立。

有意思的细节：Pythia 在 depth 1-3 的 AUC 衰减更慢（1v2: 0.947 vs Qwen 0.897），但在 depth 4-6 衰减更快（4v5: 0.691 vs 0.746），最终 6v7 两者接近（0.634 vs 0.641）。

产出文件：
- 脚本：`scripts/analyze_pythia_retrain_depth7.py`
- JSON：`results/analysis_pythia_retrain_depth7/comparison.json`
- LaTeX：`results/analysis_pythia_retrain_depth7/table_retrain_comparison.tex`

实验完成后直接 `python3 scripts/analyze_pythia_retrain_depth7.py` 即可更新结果（Pythia 实验如果还在跑，当前输出的已经是最新数据）。

---
