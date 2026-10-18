# check v8 diagnostics artifacts

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_v8-diagnostics-artifacts_20260516T012925_result.json`
- **Structured JSON:** [`9a60b61a7e4757673cba.json`](../../sessions/9a/9a60b61a7e4757673cba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断产出检查结果

### v8_step2k_diagnostics/ — 5 个文件全部存在

| 文件 | 大小 |
|------|------|
| `margin_distribution.png` | 139 KB |
| `margin_distribution_stats.json` | 351 B |
| `keep_ratio_sensitivity.png` | 199 KB |
| `keep_ratio_sensitivity.json` | 369 B |
| `token_importance_heatmap.png` | 943 KB |

生成时间：2026-05-16 09:17–09:25

### scripts/ — 5 个诊断脚本

- `analyze_margin_distribution.py`
- `analyze_keep_ratio_sensitivity.py`
- `visualize_token_importance.py`
- `eval_checkpoint_trajectory.py`
- `plot_checkpoint_trajectory.py`

### v8 训练进度

step **23550/30000**（78.5%），loss=0.0355，margin_loss=0.0671，Δ=0.7421，sps=3.1。LIP monitor 正常（spectral_norm=1.0003）。训练运行中。

---
