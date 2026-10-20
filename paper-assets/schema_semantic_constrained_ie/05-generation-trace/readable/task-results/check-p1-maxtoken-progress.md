# check p1 maxtoken progress

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_p1_maxtoken_progress_20260515T093937_result.json`
- **Structured JSON:** [`f2421a203b05a89ef0cc.json`](../../sessions/f2/f2421a203b05a89ef0cc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验进度报告

**GPU 状态**：cuda:0 (18GB/97GB, 89% util)、cuda:1 (18GB/97GB, 84% util) — 均健康运行

---

**1. `llama_docred_unconstrained_mt6144`** (PID 246947, cuda:0)
- 存活：✅ 已运行 1h 20m 35s
- 进度：**220/998 docs (22.0%)**
- 速率：~22 sec/doc
- 预估剩余：~4h 45min（约 2026-05-15 ~6h 后完成）
- 日志：正常生成中（重复 pad_token_id 提示，属正常）

**2. `llama_docred_full_s1_mt6144`** (PID 247487, cuda:1)
- 存活：✅ 已运行 1h 18m 00s
- 进度：**192/998 docs (19.2%)**
- 速率：~24.4 sec/doc
- 预估剩余：~5h 28min
- 日志：`Grammar-first fallback` 已触发 61 次（semantic mask 会清空 grammar-valid tokens 时回退到 grammar-only）— 符合 full_s1 模式预期

两个实验均健康，无错误。

---
