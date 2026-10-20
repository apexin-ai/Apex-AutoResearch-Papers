# code seed validation runner

**collapse aware mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_seed-validation-runner_20260513T091004_result.json`
- **Structured JSON:** [`8a0b9548fda5e68a60b3.json`](../../sessions/8a/8a0b9548fda5e68a60b3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个文件已创建，语法验证通过。

- `run_seed_validation.sh` — 串行跑 6 组实验（3 seeds × {PI, fixed}），`FIXED_RATIO` 环境变量可覆盖默认 0.5
- `analyze_seed_validation.py` — 从各 seed 目录读取 G0/G1/G2 final metrics + control_log，输出 mean±std 对比表和 JSON 报告

---
