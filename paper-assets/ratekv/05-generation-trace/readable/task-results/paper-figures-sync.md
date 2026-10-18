# paper figures sync

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_figures_sync_20260514T115025_result.json`
- **Structured JSON:** [`29cf8ddd52a11e23acfb.json`](../../sessions/29/29cf8ddd52a11e23acfb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据确认完毕。

## Figures 状态汇报

### 三张主图

| 文件 | 格式 | 大小 | 服务器时间 | 数据源 | 状态 |
|------|------|------|-----------|--------|------|
| `fig1_head_delta_heatmap.pdf` | PDF | 34,672 B | May 14 13:57 | 3个模型的 `*_ppl_profiles_hires.json` | **最新** |
| `fig2_compounding_curve.pdf` | PDF | 17,735 B | May 14 13:57 | `compounding_sweep_results.json` + `compounding_k10_12_results.json` | **最新** |
| `fig3_allocation_comparison.pdf` | PDF | 20,551 B | May 14 16:02 | `compounding_sweep_results.json` | **最新** |

### 本地同步状态
三张图的本地副本（`docs/paper/figures/`）与服务器文件大小完全一致，**已是最新，无需重新下载**。

### 数据新鲜度
- Figures 从 JSON profile 文件动态生成，不含硬编码 PPL 值
- Mistral profile (`mistral_ppl_profiles_hires.json`) 中不含旧的 7.3231，使用的是 per-head delta 数据（baseline_calibration_ppl=5.867）→ 不存在旧数据问题
- 所有数据文件和图表均为今日（May 14）生成

### C4 Cross-Dataset Figure
**不需要额外生成。** 理由：
- Agreement rate 96.4%（108/112 heads），仅 4 个 head 在 2-bit ↔ 4-bit 之间有分歧
- 具体分歧 heads：(3,1), (4,3), (5,1), (5,3)——全部在相邻 bit level 间
- 这个结果用论文正文中一句话 + 数字即可充分表达，单独做 figure 反而稀释信息密度

### 服务器上的辅助图表（可选用于 appendix）
- `allocation_heatmap_full_0.125/0.25/0.5.pdf` — 不同 budget 下的完整 allocation heatmap
- `crossover_scatter.pdf` — crossover scatter plot
- `ppl_comparison.pdf` — PPL 对比图

如需这些辅助图也下载到本地，告知即可。

---
