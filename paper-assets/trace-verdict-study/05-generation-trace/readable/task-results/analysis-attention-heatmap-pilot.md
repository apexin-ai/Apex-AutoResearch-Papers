# analysis attention heatmap pilot

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_attention_heatmap_pilot_20260517T004729_result.json`
- **Structured JSON:** [`449b28dde3b572ea2655.json`](../../sessions/44/449b28dde3b572ea2655.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Attention Heatmap Pilot 完成。

**产出文件** (`/root/trace-verdict-study/docs/paper/figures/attention_pilot/`):
- `attention_detail_0/1/2_AssertionError.pdf` — 3 个样本的详细 attention bar chart（按 segment 着色）
- `attention_summary_v2.pdf` — 10 样本汇总图（左：stacked bar 总占比；右：per-token density 对比）
- `attention_pilot_results_v2.json` — 原始数值数据

**核心发现**:

1. **Prompt suffix 是 attention sink**：~43% attention 集中在仅 13 个 token（per-token density 33-37），这是 causal LM 的已知现象，不反映信息利用
2. **排除 sink 后，Source code 获得最高 per-token attention**（2.4-4.7），模型主要从源代码提取判断信号
3. **[ERROR] marker 的 per-token attention 是 locals dump 的 5-10x**（1.5-2.8 vs 0.18-0.51），模型识别到了 error signal 但主要作为"存在/不存在"的 binary cue
4. **Locals dump 占据绝大部分 trace tokens 但信息利用效率极低**（per-token 0.18-0.51），支持"exception trace 中的 locals 信息是冗余噪声"的假设

---
