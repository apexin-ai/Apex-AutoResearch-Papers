# ssh setup qwen watch scripts

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_setup-qwen-watch-scripts_20260521T181331_result.json`
- **Structured JSON:** [`321b89cdc0a38547c5de.json`](../../sessions/32/321b89cdc0a38547c5de.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

PID 80733 存活，确认是 watch_qwen 进程。

---

**汇总：**

1. **run_*.sh vs eval_*.sh 对比**：核心参数一致（checkpoint sort、GPU 分配、batch_size=4），但 output_dir 路径不同（`run_*` 缺 `repo`）、`eval_*` 有结果汇总脚本而 `run_*` 没有。

2. **修改内容**：`watch_qwen_train_then_eval.sh` 第 24、36 行，将调用目标从 `run_qwen_cwm_s123_eval.sh 0 "$BATCH_SIZE"` / `run_qwen_cwm_s456_eval.sh 3 "$BATCH_SIZE"` 改为 `eval_qwen_cwm_s123.sh` / `eval_qwen_cwm_s456.sh`（已验证脚本，GPU 和 batch_size 已硬编码，无需传参）。

3. **Watch 脚本 PID**：80733

4. **Watch 日志前 5 行**：
   ```
   [Fri May 22 02:15:16 CST 2026] Watcher started. batch_size=4
   [Fri May 22 02:15:16 CST 2026] Monitoring: s123 PID=4271 → GPU 0, s456 PID=4561 → GPU 3
   ```
   正在每 60 秒轮询 PID 4271 和 4561，训练结束后自动触发对应 eval。

---
