# fix reml dedup processes

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_reml_dedup_processes_20260521T061805_result.json`
- **Structured JSON:** [`536c5574abe523a4695e.json`](../../sessions/53/536c5574abe523a4695e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

1. **101666 和 101757** — 已成功 kill（SIGTERM，未需 force kill）
2. **102750** — 存活，已运行 4m27s，当前 iter 140，Δ=7.64e-03，收敛正常
3. **日志正常** — sig2e 稳定在 0.051517，total variance 从 0.2025 → 0.2111 逐步收敛，约 3s/iter，500 iter 预计还需 ~18 分钟

**注意：发现额外 REML 进程** — PID **102937** 运行的是 `run_reml_500_v2.py`（不同于 102750 的 `run_reml_500.py`）。如果这也是重复的，需要一并清理。是否 kill 102937？

---
