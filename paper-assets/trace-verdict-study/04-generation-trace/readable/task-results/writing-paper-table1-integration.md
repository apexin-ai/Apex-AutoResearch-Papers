# writing paper table1 integration

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_paper_table1_integration_20260516T182925_result.json`
- **Structured JSON:** [`f5e1c2f6bc9e3882f9b2.json`](../../sessions/f5/f5e1c2f6bc9e3882f9b2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。以下是所有修改的汇总：

**experiments.tex**:
- Table 1 (`tab:cross_model`): 新增 CodeLlama-13B 列 (exception_only 99.83%, VOTA 98.57%, no_trace 76.50%), 更新 Range 列 (no_trace range: 7.82pp → 9.19pp)
- 替换原来的单段分析为 3 个 `\paragraph{}`:
  - **Exception dominance across families** — 3 家族均达 99.83%, cross-model range 仅 0.50pp
  - **Scale invariance of exception signals** — 1.5B-13B (8.7×) 共享同一 ceiling; no_trace 单调 scaling
  - **VOTA cross-family variation** — 非 truncation 模型的 VOTA range 仅 1.01pp, 证实 DeepSeek deficit 是 truncation artifact

**discussion.tex**:
- Format marker sensitivity 段: 新增 nomarker ablation 数据 (Qwen-7B 96.55%, Qwen-1.5B 97.80%), 量化 format marker 贡献 (3.28pp)
- Irreducible error ceiling 段: 加入 CodeLlama-13B 证据, 扩展为 "三家族三尺度收敛同一 ceiling"

**main.tex (abstract + limitations)**:
- "three models" → "four models", "two architecture families" → "three", "1.5B–7B" → "1.5B–13B"
- Key finding 句重写为 scale-invariance framing

所有定量数字均标注了 exp_id。未改动 claim 强度或 narrative framing。

---
