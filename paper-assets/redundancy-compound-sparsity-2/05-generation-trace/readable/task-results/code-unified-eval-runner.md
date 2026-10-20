# code unified eval runner

**redundancy compound sparsity 2** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_unified_eval_runner_20260512T153747_result.json`
- **Structured JSON:** [`b02d642c43439b0809a4.json`](../../sessions/b0/b02d642c43439b0809a4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个 `--help` 全部通过。

`/root/carc/eval_runner.py` 已创建，支持：
- **PPL 子命令**：CARC 策略（full/ema_*/random/recency）通过 `run_strategy` 80/20 split 评估，kvpress 策略（h2o/snapkv/streaming_llm/tova/expected_attn/observed_attn/keydiff）通过 `evaluate_ppl_with_press` 滑窗评估
- **MATH-500 子命令**：full 用 `model.generate()`，ema_* 用 `CARCGenerator`，kvpress 用 `press(model)` + `model.generate()`
- 统一 JSON 输出格式，含 summary
- 支持多策略 × 多 budget_ratio 批量运行

---
