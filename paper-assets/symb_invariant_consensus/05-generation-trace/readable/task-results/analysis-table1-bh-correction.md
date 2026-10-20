# analysis table1 bh correction

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_table1-bh-correction_20260521T021023_result.json`
- **Structured JSON:** [`b4b3437bdd1c9edd1a7d.json`](../../sessions/b4/b4b3437bdd1c9edd1a7d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果：

- **raw 显著**: 2 条（Mistral-7B PW-D5 p=0.014, Qwen2.5-14B PW-D5 p=0.011）
- **BH 校正后显著**: 0 条
- 两条均调整为 adj p=0.112（Qwen2.5-14B 的未校正 BH 值为 0.176，经单调性约束降至 0.112）

与 reviewer 预期一致：Mistral PW adj p≈0.112，Qwen2.5 PW 的 p\*m/i=0.176 但最终 adj=0.112。关键结论不变——BH 校正后无任何条件显著。

产出文件：
- `artifacts/table1_bh_correction.json` — 完整 16 条件数据
- `artifacts/table1_bh_draft.tex` — 可插入论文的 LaTeX 段落

---
