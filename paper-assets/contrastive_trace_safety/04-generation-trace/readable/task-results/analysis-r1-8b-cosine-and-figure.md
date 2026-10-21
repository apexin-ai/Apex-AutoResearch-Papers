# analysis r1 8b cosine and figure

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r1_8b_cosine_and_figure_20260522T182019_result.json`
- **Structured JSON:** [`dc21cd3057228ae6a512.json`](../../sessions/dc/dc21cd3057228ae6a512.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。

### R1-8B Cosine Compression 结果

| 模型 | Shallow Mean | Deep Mean | Ratio | Compression |
|------|-------------|-----------|-------|-------------|
| **R1-8B** (L0-L5 / L24-L31) | 0.3792 | 0.3834 | **0.9889** | 1.1% (极微弱) |
| **Gemma-2-9B** (L0-L5 / L30-L41) | 0.2373 | 0.3055 | **0.7766** | 22.3% (强) |
| **Gemma-4-E4B** (L0-L5 / L30-L41) | 0.1161 | 0.1107 | **1.0486** | 无 (shallow > deep) |

R1-8B 呈现独特的 mid-layer peak 模式（L7-L10 ~0.55），然后单调下降至 deep layers ~0.36。与 Gemma-2 的强 shallow compression 和 Gemma-4 的高度不规则锯齿形 profile 形成鲜明对比。

### 产出
- `artifacts/r1_8b_cosine_compression_results.json`（服务器 + 本地已有数据）
- `docs/paper/figures/fig_cosine_cross_arch.pdf` + `.png`（本地已生成）

---
