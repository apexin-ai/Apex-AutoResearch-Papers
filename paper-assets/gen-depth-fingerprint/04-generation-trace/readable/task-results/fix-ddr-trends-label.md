# fix ddr trends label

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_ddr-trends-label_20260519T233445_result.json`
- **Structured JSON:** [`a16f7d351e33a2dd2b8a.json`](../../sessions/a1/a16f7d351e33a2dd2b8a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All values now match the original exactly. Verification:

| Feature | ρ | R² | Label |
|---|---|---|---|
| Entropy Mean | -0.598 | 0.969 | [DRIFTING] ✓ |
| Entropy Std | -0.157 | 0.564 | [INTERMEDIATE] ✓ |
| **Entropy Min** | **-0.404** | **0.416** | **[NEAR-STATIONARY]† ✓** |
| Entropy Max | 0.061 | 0.287 | [STATIONARY] ✓ |
| Tail Decay | -0.041 | 0.725 | [STATIONARY] ✓ |
| TTR | -0.625 | 0.930 | [DRIFTING] ✓ |
| Hapax Ratio | -0.640 | 0.897 | [DRIFTING] ✓ |

**结果汇报：**

- **脚本路径**: `/root/gen-depth-fingerprint/scripts/plot_appendix_ddr_trends.py`（原始脚本未找到，基于 PDF 视觉结构和 `generate_figures.py` 风格重建）
- **修改内容**: Entropy Min 标签从 `[INTERMEDIATE]` → `[NEAR-STATIONARY]†`
- **数据源**: 从 `features_all_models.csv`（6 gen）切换到 `features_8gen.csv`（8 gen），与原图一致
- **统计量**: ρ 用 sample-level Spearman，R² 用 depth-mean linear regression，全部与原图数值吻合
- **PDF 已生成**: 远程 `/root/gen-depth-fingerprint/chart/fig_appendix_ddr_trends.pdf`，本地已同步

---
