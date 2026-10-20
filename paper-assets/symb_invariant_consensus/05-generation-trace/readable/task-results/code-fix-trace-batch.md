# code fix trace batch

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-trace-batch_20260515T122210_result.json`
- **Structured JSON:** [`a71da1cce362a9b77a91.json`](../../sessions/a7/a71da1cce362a9b77a91.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证成功。结果：

| 指标 | 修复前 | 修复后 |
|------|--------|--------|
| Trace gen (n=12) | ~93s | **93s** (无变化，本来就用 n=K) |
| Extraction (12 traces) | ~20+ min | **20s** |
| JSON parse 失败 | 大量 | **0** |
| 总时间/题 | 20+ min | **113s** (1.9 min) |

关键数据：
- 答案正确：`137\frac{1}{2}`
- 26 constraints extracted, 6/12 traces 有 constraints（6 个 empty 是因为简单题 trace 太短）
- **0 JSON parse 失败**（`response_format=json_object` 完全消除了 parse 错误）
- 60 题预计总时间：113s × 60 = ~113 min ≈ 1.9 小时（vs 原来 25-30 小时）

修复内容总结（`sica/constraint_extractor.py` VLLMBackend 类）：
1. `max_tokens: 4096 → 512` — JSON 输出不需要 4096 tokens
2. 添加 `response_format={"type": "json_object"}` — 强制 vLLM 直接输出 JSON，跳过 QwQ-32B 的 `&lt;think>` 推理，消除 parse 失败
3. `max_workers: 4 → 12` — 12 个 extraction 全并发提交给 vLLM

**trace_generator.py 无需修改** — n=K batch 本来就正确实现了，瓶颈不在 trace generation 而在 constraint extraction。

---
