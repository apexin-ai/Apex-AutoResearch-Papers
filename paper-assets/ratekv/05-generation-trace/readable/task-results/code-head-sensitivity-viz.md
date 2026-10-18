# code head sensitivity viz

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_head_sensitivity_viz_20260514T055404_result.json`
- **Structured JSON:** [`6467fbc1fd2a13cfe636.json`](../../sessions/64/6467fbc1fd2a13cfe636.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 张图全部生成并注册完成。

**输出文件** (`westd-37397:/root/ratekv/figures/`):

| 文件 | 大小 | 内容 |
|------|------|------|
| `fig1_head_delta_heatmap.pdf/png` | 34K/158K | 3 模型并排 heatmap，Qwen(28L×4H) / Llama(32L×8H) / Mistral(32L×8H)，统一 YlOrRd 色标，L0 高 delta 标注 |
| `fig2_compounding_curve.pdf/png` | 18K/124K | k vs PPL 曲线，10 个数据点，k=8 最优(11.23)标注，uniform 4-bit 基线虚线(15.45) |
| `fig3_allocation_comparison.pdf/png` | 21K/120K | Uniform vs MCKP(k=8) stacked bar，L0 被保护为 8-bit，L1-L4 有 2-bit 头，其余 4-bit |

脚本：`/root/ratekv/generate_figures.py`

---
