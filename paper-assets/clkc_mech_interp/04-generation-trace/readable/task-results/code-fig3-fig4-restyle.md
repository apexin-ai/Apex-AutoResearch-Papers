# code fig3 fig4 restyle

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fig3-fig4-restyle_20260525T131241_result.json`
- **Structured JSON:** [`495a99b4968de37d230a.json`](../../sessions/49/495a99b4968de37d230a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两张图效果满意。总结：

---

### Figure 3 — Layer-wise Probing
- **数据来源**: `artifacts/layerwise_probe_curves.json`（含 Llama-3.1-8B 和 Qwen3-8B 的 4-direction per-layer probe accuracy, residual stream + MLP, Qwen3 含 bootstrap CI）
- **设计**: 2-panel 水平排列（**Gemma-2 无 per-layer 数据，未绘制**）；EN→EN 蓝色实线圆形标记，ZH→ZH 珊瑚实线方形标记，EN→ZH 浅青虚线三角，ZH→EN 深青点划线菱形；MLP 灰色虚线弱化；peak 大标记标注；CI fill_between
- **文件**: 
  - `figures/paper/fig3_layerwise.png` / `.pdf`
  - 生成脚本: `figures/paper/gen_fig3_layerwise.py`

### Figure 4 — Asymmetry Forest Plot
- **数据来源**: 脚本内嵌数据（3 模型 × 2 任务的 bootstrap CI，与原 `gen_fig3_asymmetry_forest.py` 一致）
- **设计**: Forest plot，Conflict 珊瑚色，XNLI 青色，±2pp 灰色等价区间，serif 字体，右侧 monospace 数值标注
- **文件**:
  - `figures/paper/fig4_asymmetry.png` / `.pdf`
  - 生成脚本: `figures/paper/gen_fig4_asymmetry.py`

**注意**: Gemma-2-9B 缺少 per-layer probe 数据（服务器上只有 `probe_results_multiseed.json` summary），Figure 3 只含 2 个 panel。如需补充 Gemma panel，需先在远程跑 4-direction per-layer probe 实验。

---
