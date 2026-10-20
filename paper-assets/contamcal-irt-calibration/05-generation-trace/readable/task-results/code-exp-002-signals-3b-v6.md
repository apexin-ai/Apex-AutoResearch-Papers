# code exp 002 signals 3B v6

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_002_signals_3B_v6_20260515T200807_result.json`
- **Structured JSON:** [`ba1dcf5197bd14fa280c.json`](../../sessions/ba/ba1dcf5197bd14fa280c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**cuda:3 不可用。** PID 627614 正在 cuda:3 上运行 1.5B 的 paraphrase eval 任务（`exp_001_eval_15B_s123_para_aligned_batch`），刚于 04:09 启动。虽然 nvidia-smi 暂时显示 0 MiB，但进程正在加载模型，马上会占用显存。

另外有一个 **seed 不匹配问题**需要确认：

| 项目 | SEED |
|------|------|
| run_batch.py 硬编码 | s42 |
| v5（cuda:4 正在运行） | s42（d025+d100） |
| 你指定的 checkpoint | s123 |

两个 checkpoint 都存在但是不同的模型（不同 inode、不同日期）。如果 d005 用 s123 而 d025/d100 用 s42，signals 不可比。

**需要你确认两件事：**

1. **cuda:3 上的 eval 任务**：是等它跑完再提交 signals，还是你想把 signals 放到别的 GPU？
2. **seed 选择**：d005 用 s42（与 v5 的 d025/d100 一致）还是 s123？如果用 s123，需要修改 run_batch.py 的 SEED 变量或用 `--seed` 参数（目前不支持，需加）。

---
