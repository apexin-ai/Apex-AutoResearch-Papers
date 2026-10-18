# code heatmap fix

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_heatmap_fix_20260514T221632_result.json`
- **Structured JSON:** [`1dad3f86dee2eca798b0.json`](../../sessions/1d/1dad3f86dee2eca798b0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Files downloaded successfully (timestamps and sizes match server-side outputs).

## 完成汇报

**Heatmap 已重新生成并部署到论文目录。**

### 各模型 top-3 head deltas（2-bit ΔPPL）

| 模型 | Layers×Heads | 数据源 | Top-3 |
|------|---|---|---|
| Gemma-2-9B | 42×8 | **standard*** | L29H7=0.22, L0H1=0.14, L40H6=0.09 |
| Llama-3.1-8B | 32×8 | hires | **L2H5=15.26**, L3H1=0.44, L0H0=0.33 |
| Mistral-7B-v0.3 | 32×8 | hires | L2H5=0.22, L12H1=0.12, L7H4=0.12 |
| Qwen2.5-7B | 28×4 | hires | **L0H0=6.74**, L0H2=2.12, L0H3=1.31 |
| Yi-1.5-9B | 48×4 | hires | **L4H3=13.12**, L8H2=0.55, L2H0=0.23 |

*Gemma-2 hires 文件不存在（仅有 standard profiling），图中以 `*` 标注并加 footnote 说明。

### 关键观察
- 4/5 模型用 hires；只剩 Gemma-2 standard
- Llama / Qwen / Yi 都有显著 outlier head（>6 ΔPPL），Mistral 分布相对均匀（max 0.22）—— 与 paper 中"集中度差异"叙事一致
- 论文目标路径 `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/docs/paper/figures/` 不存在；实际正确路径为 `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/figures/`，已写入此处覆盖旧 PDF/PNG

---
