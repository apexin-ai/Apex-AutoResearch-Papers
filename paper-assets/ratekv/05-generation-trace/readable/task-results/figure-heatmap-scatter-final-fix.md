# figure heatmap scatter final fix

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_figure_heatmap-scatter-final-fix_20260515T010737_result.json`
- **Structured JSON:** [`ad210ea37bb35b287f27.json`](../../sessions/ad/ad210ea37bb35b287f27.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

没有配置 remote。需要你提供 remote URL 才能 push。

以下是已完成的操作汇总：

**Step 1 - 统一 heatmap 脚本** ✅
- 将 `/root/ratekv/generate_hires_heatmap.py` 内容覆盖到 `/root/ratekv/figures/generate_figures.py`
- Gemma-2 路径改为 `gemma2_hires_bf16_2bitonly_profiles.json`，source 改为 `'hires'`
- Mistral 路径为 `mistral_hires_bf16_2bitonly_profiles.json`（来自根目录脚本）
- 已移除 `*` 脚注

**Step 2 - 执行 heatmap 重生成** ✅
- `fig1_head_delta_heatmap.pdf` (57855 bytes) 和 `.png` (157794 bytes)，时间戳 May 15 09:09

**Step 3 - Scatter 修复** ✅
- Gemma-2 concentration `0.223` → `0.229`
- `fig_concentration_scatter.pdf` (29808 bytes) 和 `.png` (122484 bytes)，时间戳 May 15 09:09

**Step 4 - 同步到本地** ✅
- 4 个文件通过 scp 复制到 `docs/paper/figures/`

**Step 5 - 本地 Commit** ✅
- commit `33ee621`: `update heatmap (Gemma-2→hires) and scatter (Gemma-2 conc 0.229) figures`
- **Push 失败**：无配置 remote，需要提供 remote URL

---
