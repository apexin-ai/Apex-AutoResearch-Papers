# exp aime30 launch

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_aime30-launch_20260515T123853_result.json`
- **Structured JSON:** [`e5b0458dbb050c31eaae.json`](../../sessions/e5/e5b0458dbb050c31eaae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 总结

### 代码一致性验证
**constraint_extractor.py** — VLLMBackend 包含两个 Worker 的所有修复：
- `max_tokens=512` ✅
- `response_format={"type": "json_object"}` ✅
- `max_workers=12` ✅
- 正确的 regex `\s` ✅
- fallback JSON 提取 + `&lt;think>` 剥离 + JSON repair ✅
- `parse_retries=1` ✅

### 发现并修复的问题
1. **trace 截断 bug**：VLLMGenerator 的 `max_tokens=4096` 对 QwQ-32B 太短，12/12 trace 都无法生成 `\boxed{}` 答案。修复：增加到 `10240`
2. **run_full_mvp.py 缺参数**：添加了 `--temperature`、`--max-tokens`、`--no-proofwriter` 参数

### Smoke test 结果（1 题 AIME）
- SICA answer: **73** ✅（ground truth: 73）
- Trace answers: **12/12** non-empty
- Constraints: 66 total, 30 unique
- MaxSAT: 26 sat, 4 excl
- Time: 470.7s

### AIME 30 题实验
- **exp_id**: `sica_aime30_t07`
- **状态**: RUNNING
- **PID**: 119338（tmux session: `sica_aime30_t07`）
- **日志**: `/tmp/sica_aime30_t07.log`
- **预计耗时**: 3-5 小时

---
