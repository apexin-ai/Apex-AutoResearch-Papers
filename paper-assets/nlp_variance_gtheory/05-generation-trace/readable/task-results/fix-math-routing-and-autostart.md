# fix math routing and autostart

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_math_routing_and_autostart_20260521T120018_result.json`
- **Structured JSON:** [`0e14de9554b261a596d7.json`](../../sessions/0e/0e14de9554b261a596d7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 Fix 均已完成。

**Fix (a)**: `_build_prompt` 对 `benchmark == "math"` 直接调用 `format_math_prompt()`，不依赖 `BENCHMARK_TEMPLATES["math"]`。`prompt_templates.py` 的 `try/except ImportError: pass` 虽然确实失败（`MATH_TEMPLATES` 是函数局部变量），但没有代码路径受影响。**安全，无需修复。**

**Fix (b)**: `auto_start.sh` 已添加 filesize 检查（Yi ≥ 17GB, OLMo ≥ 13GB），位于 shard 数量检查之后。旧进程 PID 7309 已终止，新进程 PID 11066 已启动并正常运行在下载等待循环中。

---
