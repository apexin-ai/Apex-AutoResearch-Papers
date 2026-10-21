# ops exp002 task transition monitor

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp002-task-transition-monitor_20260514T120549_result.json`
- **Structured JSON:** [`e87cffb72bf951a9f01f.json`](../../sessions/e8/e87cffb72bf951a9f01f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### 当前 task（从 ps/proc 确认）

**Task [1/9]: d000/mmlu** — PID 353390 仍在运行（State: R，context switches 持续增长: 5149→5183→5213 voluntary, 6066→6320→6560 nonvoluntary）

### v4 run 时间线

| 时间 (CST +0800) | 事件 |
|---|---|
| 18:46:36 | v4 run_batch.py 启动，task [1/9] d000/mmlu 开始 |
| 18:50 | signal_embedding_mmlu.json 写入 (6.1MB) |
| 18:55 | signal_minkpp_mmlu.json 写入 (2.1MB) |
| 19:48:37 | **signal_selfcritique.py 热修复写入** |
| 19:48:48 | **.pyc 重新编译 = 热修复被加载** |
| 现在 | selfcritique 正在计算中，尚无产出文件 |

### 热修复验证

**已生效。** 证据链：
1. compute_signals.py 延迟 import（line 66: `from signal_selfcritique import compute_selfcritique_signal`）
2. .py 修改时间 19:48:37 → .pyc 编译时间 19:48:48 → 进程在运行到 selfcritique 阶段时加载了新版本
3. 当前版本 `BATCH_SIZE = 32`（旧版 .bak 无此常量）

### v4 产出文件清单

**d000_s42 目录**（v4 产出，时间 >= 18:46）:
- `signal_embedding_mmlu.json` (18:50, 6.1MB) ✓
- `signal_minkpp_mmlu.json` (18:55, 2.1MB) ✓
- `signal_selfcritique_mmlu.json` — 尚未写入（计算中）

**d000_s42 目录**（旧 run 残留）:
- `signal_embedding_gsm8k.json` (18:38) — 第一次 run 产出
- `signal_embedding_arc_challenge.json` (18:41) — 第一次 run 产出
- `signal_embedding_mmlu_Qwen2.5-0.5B_d000_s42.json` (16:00) — 更早的残留

**d005_s42 目录**（旧 run 残留）:
- `signal_embedding_mmlu.json` (18:45) — 第一次 run 产出

**其他**:
- `batch_report_Qwen2.5-0.5B.json` — 旧 dry-run 报告，内容过时

### 结论

Task 1→2 过渡尚未发生。当前仍在 task 1 (d000/mmlu) 的 selfcritique 阶段。MMLU test set ~14k items / batch_size=32 = ~440 batches，每 batch 需生成答案（autoregressive, max 256 tokens）+ critique forward pass，预计还需要较长时间。热修复已确认被正确加载。

---
