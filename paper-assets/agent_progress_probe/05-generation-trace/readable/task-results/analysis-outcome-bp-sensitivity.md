# analysis outcome bp sensitivity

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_outcome-bp-sensitivity_20260514T114949_result.json`
- **Structured JSON:** [`d4aaed0028405e9e9021.json`](../../sessions/d4/d4aaed0028405e9e9021.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。

## 结果

**Probe 不依赖 outcome_backpropagation (OB)。** 去掉 OB 后训练的 probe 在原 test set 上反而高 +1.2pp macro-F1。

### 核心数据

| | Orig 3-LF Probe | Holdout 2-LF Probe | Delta |
|---|---|---|---|
| **Full test macro-F1** | 0.8468 | **0.8593** | **+1.2pp** |
| OB 贡献的子集 (24.7%) | 0.7708 | 0.6546 | -11.6pp |
| OB 未贡献的子集 (75.3%) | 0.8750 | **0.9337** | **+5.9pp** |

### 关键发现

1. **零标签翻转** — OB 从不与另两个 LF 矛盾，只补充覆盖
2. **OB 覆盖 24.2%** 窗口（89% 投 stag），但引入的噪声在 75.3% 多数窗口上拖累了 probe
3. 去掉 OB 后 probe 在多数窗口上大幅提升 (+5.9pp)，足以抵消在 OB 子集上的下降

### Reviewer 可用结论

> Probe 的预测信号来自实时可观测的 LF (file_diff_delta, command_repetition)，不依赖 post-hoc 的 outcome 信息。Hold-out 实验证实去掉 OB 后整体 F1 反而提升。

报告已保存至 `artifacts/outcome_bp_sensitivity_report.md`。服务器产出：`data/embeddings_no_outcome_bp.pt`、`checkpoints_no_outcome_bp/`。

---
