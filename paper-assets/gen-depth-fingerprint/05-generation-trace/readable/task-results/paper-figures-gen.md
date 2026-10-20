# paper figures gen

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_figures-gen_20260515T043641_result.json`
- **Structured JSON:** [`c1fd077aec98f39cbc5e.json`](../../sessions/c1/c1fd077aec98f39cbc5e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 张图全部生成完毕。

### 生成的文件

| 文件 | 路径 |
|------|------|
| Fig 1 PDF/PNG | `/root/gen-depth-fingerprint/paper/figures/fig1_differential_response.{pdf,png}` |
| Fig 2 PDF/PNG | `/root/gen-depth-fingerprint/paper/figures/fig2_logo_performance.{pdf,png}` |
| Fig 3 PDF/PNG | `/root/gen-depth-fingerprint/paper/figures/fig3_baseline_comparison.{pdf,png}` |
| Fig 4 PDF/PNG | `/root/gen-depth-fingerprint/paper/figures/fig4_downstream_negative.{pdf,png}` |

### 数据来源

| 图 | 数据文件 |
|----|----------|
| Fig 1 | `data/features_all_models.csv` (27,529 rows, 6 generators incl. Qwen3-8B) |
| Fig 2 | `data/cross_generator_results.json` (6-gen LOGO with bootstrap CI) |
| Fig 3 | `results/ordinal_baseline_results.json` (5 methods: 7-feature, Avg-LogProb, LD-Score, FastDetectGPT, Binoculars) |
| Fig 4 | `autodl-tmp/.../downstream/*/results.json` (5 variants × 3 seeds = 15 runs) |

### 无缺失数据

所有 4 张图的数据均完整可用。绘图脚本位于 `/root/gen-depth-fingerprint/paper/generate_figures.py`，可随时修改重跑。

---
