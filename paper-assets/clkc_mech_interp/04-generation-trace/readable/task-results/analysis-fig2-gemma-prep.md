# analysis fig2 gemma prep

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_fig2-gemma-prep_20260523T050143_result.json`
- **Structured JSON:** [`e1daf64b4295527b895d.json`](../../sessions/e1/e1daf64b4295527b895d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。汇报如下：

**Gemma 数据**
- 存在于 `/root/clkc_mech_interp/data/gemma2/probe_results_bootstrap_n2000.json`
- CLKC conflict 数据，residual stream probe，42 层（layer 0-41），4 方向（en_en/zh_zh/en_zh/zh_en）
- bootstrap n=2000，含 mean/ci_lower/ci_upper
- 无 MLP probe 数据（Llama/Qwen 有 MLP，Gemma 面板仅显示 residual stream + CI band）

**脚本修改**
1. `aggregate_layerwise.py`：追加了 Gemma2 数据提取，将 bootstrap mean 作为 residual stream 值，CI 数据单独存储为 `gemma2_bootstrap_ci`
2. `gen_fig2_layerwise_probes.py`：
   - `1×2` → `1×3` 布局，figsize `(7.0, 3.4)` → `(10.5, 3.4)`
   - 添加 `(c) Gemma-2-9B` 面板（42 层，residual stream + CI band，无 MLP）
   - MLP 绘制逻辑改为可选（`mlp_key` 为 None 时跳过）

**Gemma 峰值**
| Direction | Peak Layer | Accuracy |
|-----------|-----------|----------|
| en_en | L24 | 0.7617 |
| zh_zh | L24 | 0.7097 |
| en_zh | L22 | 0.6290 |
| zh_en | L24 | 0.7023 |

**生成文件**
- `/root/clkc_mech_interp/figures/paper/fig2_layerwise_probes.pdf` (40KB)
- `/root/clkc_mech_interp/figures/paper/fig2_layerwise_probes.png` (775KB)
- 图片尺寸 3119×1120，三面板均正确渲染

**视觉验证**：无法通过 SSH 传输大图到本地查看（binary 传输受限）。建议你直接在服务器上查看 PNG，或下载 PDF 到本地确认。

---
