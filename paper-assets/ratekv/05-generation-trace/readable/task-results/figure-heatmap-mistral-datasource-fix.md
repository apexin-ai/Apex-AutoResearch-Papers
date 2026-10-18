# figure heatmap mistral datasource fix

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_figure_heatmap-mistral-datasource-fix_20260515T010222_result.json`
- **Structured JSON:** [`b2360f8d48ca918fea89.json`](../../sessions/b2/b2360f8d48ca918fea89.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### 修改内容
**无需修改**——脚本中 Mistral 的 path 已经是目标值 `mistral_hires_bf16_2bitonly_profiles.json`（可能之前已经改过）。直接重跑了脚本。

### Gemma-2 hires 数据文件情况（供 Director 参考）
**hires 版本存在**：
- `/root/ratekv/gemma2_hires_bf16_2bitonly_profiles.json` — 28846 bytes (May 15 07:39)
- `/root/ratekv/gemma2_hires_bf16_2bitonly_results.json` — 同批产出
- `/root/ratekv/gemma2_profiling_results.json` — 58023 bytes (May 15 00:38, 当前脚本使用的 standard 版本)

脚本中 Gemma-2 仍指向 standard `gemma2_profiling_results.json`，**未修改**。Director 可决定是否切到 hires 版。

### 输出文件
脚本输出文件名为 `fig1_head_delta_heatmap.{pdf,png}`（**不带 `_5model` 后缀**，task 描述与实际不符）：
- `/root/ratekv/figures/fig1_head_delta_heatmap.pdf` — 66425 bytes
- `/root/ratekv/figures/fig1_head_delta_heatmap.png` — 178864 bytes

### Top heads（5 模型，新结果）
- Gemma-2-9B (42L×8H, standard): L29H7=0.22, L0H1=0.14, L40H6=0.09
- Llama-3.1-8B (32L×8H, hires): L2H5=15.26, L3H1=0.44, L0H0=0.33
- Mistral-7B-v0.3 (32L×8H, hires): L2H5=0.32, L12H1=0.14, L0H7=0.14
- Qwen2.5-7B (28L×4H, hires): L0H0=6.74, L0H2=2.12, L0H3=1.31
- Yi-1.5-9B (48L×4H, hires): L4H3=13.12, L8H2=0.55, L2H0=0.23

---
