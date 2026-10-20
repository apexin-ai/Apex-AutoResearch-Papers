# code token selection comparison

**distill kv rag cache** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_token-selection-comparison_20260514T081201_result.json`
- **Structured JSON:** [`42ad9f3cb1c7f7e26d9f.json`](../../sessions/42/42ad9f3cb1c7f7e26d9f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已全部完成，结果已在上方汇总。核心发现是 A/C/D 三个配置在 per-sample PCA 下生成完全相同的文本，说明 token 选择策略的代码路径可能没有真正区分。需要排查 `pipeline.py` 中 `run_single` 的分支逻辑。

---
