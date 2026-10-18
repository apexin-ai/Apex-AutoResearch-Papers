# analysis paper figures validation

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_paper_figures_validation_20260515T005346_result.json`
- **Structured JSON:** [`10805fb4332180349e85.json`](../../sessions/10/10805fb4332180349e85.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the structured report:

---

## 图表数据一致性验证报告

### 1. Heatmap (fig1_head_delta_heatmap)

**脚本**: `generate_hires_heatmap.py` (本地) = `figures/generate_figures.py` (服务器) — 内容一致

| Model | Profile 文件 | Source 标记 | 状态 |
|-------|-------------|-----------|------|
| Gemma-2-9B | `gemma2_profiling_results.json` | **standard** | **⚠ 问题：hires 文件已存在 (`gemma2_hires_bf16_2bitonly_profiles.json`) 但未被使用** |
| Llama-3.1-8B | `llama_hires_bf16_2bitonly_profiles.json` | hires | ✓ |
| Mistral-7B-v0.3 | `mistral_ppl_profiles_hires.json` | hires | ✓ |
| Qwen2.5-7B | `hires_profiles.json` | hires | ✓ |
| Yi-1.5-9B | `yi15_hires_bf16_2bitonly_profiles.json` | hires | ✓ |

**最后生成时间**: 服务器 May 15 06:17 (UTC+8), 本地 May 14 22:18 (UTC) — 已同步

**问题**: 脚本给 Gemma-2 标了 `*` 脚注 "standard profiling (no hires available)"，但 hires profile 文件 `gemma2_hires_bf16_2bitonly_profiles.json` 已存在于服务器。需要更新数据源并移除脚注。

---

### 2. Scatter (fig_concentration_scatter)

**脚本**: `/root/ratekv/figures/gen_scatter_concentration.py`

**Hardcoded concentration 值 vs 预期 hires 值**:

| Model | 脚本中的值 | 预期 hires 值 | 状态 |
|-------|-----------|-------------|------|
| Gemma-2-9B | 0.223 | ~0.23 | ✓ 一致 |
| Mistral-7B-v0.3 | **0.241** | **0.22** | **⚠ 不一致** |
| Llama-3.1-8B | 0.575 | 0.57 | ✓ (精度差异，可接受) |
| Yi-1.5-9B | 0.714 | 0.71 | ✓ (精度差异，可接受) |
| Qwen2.5-7B | **0.616** | **0.61** | **⚠ 可能不一致** — commit bfaea4e 将 Qwen 统一到 0.61 (float32 verified) |

**最后生成时间**: 服务器 May 15 06:36 (UTC+8), 本地 May 14 22:36 (UTC) — 已同步

---

### 3. 本地论文图表文件清单

| 文件 | 修改时间 (UTC) | 状态 |
|------|--------------|------|
| `fig1_head_delta_heatmap.pdf` | May 14 22:18 | 与服务器同步 |
| `fig1_head_delta_heatmap.png` | May 14 22:18 | 与服务器同步 |
| `fig_concentration_scatter.pdf` | May 14 22:36 | 与服务器同步 |
| `fig_concentration_scatter.png` | May 14 22:36 | 与服务器同步 |
| `fig2_compounding_curve.pdf` | May 14 07:44 | 较旧，未在本次验证范围 |
| `fig3_allocation_comparison.pdf` | May 14 08:02 | 较旧，未在本次验证范围 |

---

### 需要修复的问题

1. **[Heatmap] Gemma-2 数据源需更新**: `gemma2_profiling_results.json` (standard) → `gemma2_hires_bf16_2bitonly_profiles.json` (hires)，同时将 source 标记改为 `'hires'`，移除 `*` 脚注
2. **[Scatter] Mistral concentration 值冲突**: 脚本 0.241 vs 预期 0.22。注意 commit e52fb0e 将论文表格中 Mistral 更新为 concentration=0.24 — 需要确认 0.22 vs 0.24 哪个是最终正确值（可能来自不同 profile 文件: `mistral_ppl_profiles_hires.json` vs `mistral_hires_bf16_2bitonly_profiles.json`）
3. **[Scatter] Qwen concentration 精度**: 脚本用 0.616，但 commit bfaea4e 将 Qwen 统一到 0.61 (float32 verified)。如论文文本/表格中报告 0.61，scatter 也应使用 0.61 以保持一致

---
