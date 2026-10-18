# fix paper figures v2

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_paper_figures_v2_20260515T010245_result.json`
- **Structured JSON:** [`27544b8e5991851a506a.json`](../../sessions/27/27544b8e5991851a506a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**执行摘要：**
1. **Heatmap (`generate_figures.py`)**: Gemma-2 数据源已是 hires profile (`gemma2_hires_bf16_2bitonly_profiles.json`)，清除了 `*` 脚注的死代码（`suffix` 逻辑），重新生成图表
2. **Scatter (`gen_scatter_concentration.py`)**: Qwen concentration 已是 `0.61`，无需代码修改，重新生成图表
3. 4 个文件（PDF/PNG × 2）已 scp 回本地 `docs/paper/figures/`

---
