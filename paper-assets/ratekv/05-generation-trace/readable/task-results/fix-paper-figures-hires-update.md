# fix paper figures hires update

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_paper_figures_hires_update_20260515T010628_result.json`
- **Structured JSON:** [`9f999cc4450a2ba7b409.json`](../../sessions/9f/9f999cc4450a2ba7b409.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个脚本在服务器上已经是修复后的版本（Gemma-2 用 `gemma2_hires_bf16_2bitonly_profiles.json` + `'source': 'hires'`，无 `*` 脚注；Qwen concentration = 0.61），重新运行后输出已同步到本地。

生成文件：

| 文件 | 服务器 | 本地 |
|---|---|---|
| `fig1_head_delta_heatmap.pdf` | 59624 B | 59624 B |
| `fig1_head_delta_heatmap.png` | 157566 B | 157566 B |
| `fig_concentration_scatter.pdf` | 29851 B | 29851 B |
| `fig_concentration_scatter.png` | 121979 B | 121979 B |

Heatmap 验证：Gemma-2 显示为 `(42x8, hires)`，top head L0H1=0.19（hires 数据）。所有 5 个模型 source 均为 hires，无脚注。

---
