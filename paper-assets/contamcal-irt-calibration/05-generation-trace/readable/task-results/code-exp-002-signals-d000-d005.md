# code exp 002 signals d000 d005

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_002_signals_d000_d005_20260515T230319_result.json`
- **Structured JSON:** [`fb5d05a9a7d901ab3fec.json`](../../sessions/fb/fb5d05a9a7d901ab3fec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

发现两个阻塞问题，无法直接提交：

**问题 1: cuda:3 被占用**
- PID 630891 正在跑 `compute_signals.py` (3B_d000_v2_s42/mmlu/signal s4)，占用 7794MiB/64% util
- 违反 C002，不能提交到 cuda:3

**问题 2: run_batch.py SEED 硬编码为 "s42"**
- 脚本第 43 行 `SEED = "s42"`，argparse 无 `--seed` 参数
- `checkpoint_path()` 会拼出 `Qwen2.5-3B_d000_s42/lora_adapter`，而非目标 `Qwen2.5-3B_d000_s123/lora_adapter`
- 直接运行 `--only d000` 会计算 s42 的 signals，不是 s123

**可行方案：**

1. **cuda:3** — 等 PID 630891 跑完，或改用其他空闲 GPU（当前只有 cuda:2 空闲）
2. **SEED 问题** — 需要修改 run_batch.py 添加 `--seed` 参数（或在命令中临时覆盖），使其能指向 s123 路径。或者直接调用底层 `compute_signals.py` 手动传路径。

需要你决定：
- cuda:3 的任务是等还是换 GPU？
- SEED 问题用哪种方式解决？

---
