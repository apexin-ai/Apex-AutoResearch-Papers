# ops anon repo v1 residual fix

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_anon-repo-v1-residual-fix_20260523T203119_result.json`
- **Structured JSON:** [`2243dabe49c0b4c102ad.json`](../../sessions/22/2243dabe49c0b4c102ad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Done. Here's the summary:

**修复了 34 个脚本** (35 files changed including README):

| 类别 | 脚本数 | 修复内容 |
|------|--------|---------|
| 标准 compute_individual_asr + compute_panel_asr | 28 | 添加 `_is_valid_score()` 过滤 |
| compute_panel_asr_all_methods (聚合脚本) | 3 | 同上 |
| K=4 面板 variant | 1 | 同上 (majority_vote_k4) |
| pairwise 多样性指标 (Q/disagreement/kappa) | 1 | 同上 |
| 独立脚本 (run_7model_preview) | 1 | 添加本地 `_is_valid_score` 定义 |

**判定为安全（未修改）的 4 处 `.get('winner', 'tie')`：**
- `src/unified_data_loader.py:_invert_winners` — position_bias swap 逻辑，非 ASR 计算
- `src/correlation.py:_extract_winners` — 下游 MI/agreement 库
- `src/panels.py:Panel.aggregate` — 下游面板聚合库
- `run_7model_preview.py:113` — MI 矩阵计算，需保持向量对齐

**README 修复：**
- 删除 `fig5_forest_plot.py` 引用
- 删除 `fig5_*.py` 项目结构描述
- 添加 V2 Data Correction 段落
- 删除 `scripts/fig5_forest_plot.py` 文件

**Commit**: `bfc4594`

---
