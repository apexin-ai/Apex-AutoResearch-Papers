# exp gemma cron diagnose

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_gemma_cron_diagnose_20260521T022136_result.json`
- **Structured JSON:** [`34d99979d11940a868f2.json`](../../sessions/34/34d99979d11940a868f2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
exp001_gemma: 部分完成（1/3 precision）
判断依据: 4 GPU 全部崩溃在同一错误 — vLLM 拒绝以 float16 加载 gemma2 模型
  错误: "The model type 'gemma2' does not support float16. Reason: Numerical instability."

已完成部分 (bfloat16):
- Total: 86,400 / 259,200 (33.3%)
- Conditions: 432/1296 (全部 bfloat16 conditions 完成)
- Accuracy: 0.7311
- bfloat16: 0.7311 | float32: 未跑 | float16: 不支持
- T=0.0: 0.7348 | T=0.3: 0.7338 | T=0.7: 0.7248
- Null predictions: 0 (0.0%)
- All 432 conditions have exactly 200 items ✓

未完成部分:
- float32: 432 conditions (86,400 records) — 可恢复，需重跑
- float16: 432 conditions — Gemma2 架构不支持，无法运行

执行顺序: bfloat16 ✓ → float16 ✗(崩溃) → float32 未到达

建议修复方案:
1. 用 `--precision bfloat16` 过滤已跳过（已完成），用 `--precision float32` 单独重跑 float32 部分
2. float16 需要从实验设计中移除或替换（如改为 float8_e5m2），因为 Gemma2 架构层面不支持 float16
```

---
