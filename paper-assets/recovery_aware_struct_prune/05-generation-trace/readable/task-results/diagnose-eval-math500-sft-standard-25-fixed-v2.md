# diagnose eval math500 sft standard 25 fixed v2

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_math500_sft_standard_25_fixed_v2_20260524T055418_result.json`
- **Structured JSON:** [`882eb0f7a52f8524c1ae.json`](../../sessions/88/882eb0f7a52f8524c1ae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**核心发现：v2 并未真正失败。** 500/500 题全部跑完，结果文件已保存（154KB），EXIT_CODE=129 是 SSH 断开导致的 SIGHUP，发生在结果保存之后，属于误报。

关键数据：
- MATH-500 准确率：**15.4%** (77/500)
- 63.4% 回复被截断，可能拉低了准确率
- v1 才是真正的失败——在 20% 进度时被 SIGHUP 杀掉

报告已写入 `artifacts/diagnose_eval_math500_sft_standard_25_fixed_v2.md`。

---
