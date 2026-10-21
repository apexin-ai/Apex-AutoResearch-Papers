# diag exp 001 eval 15B failed

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_exp_001_eval_15B_failed_20260515T134605_result.json`
- **Structured JSON:** [`d74c052e740a28034f89.json`](../../sessions/d7/d74c052e740a28034f89.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

### 根因：双重提交导致 SIGHUP

**不是 OOM、不是脚本 bug、不是 SSH 断连。**

### 证据链

1. **Exit files 确认**：两个实验的 exit 文件都记录 `129|2026-05-15T13:42:57Z`（完全同一秒）

2. **时间线重建**：
   - `21:39:09-15`：首次提交（PIDs 565090, 565266），日志文件 Birth time 证实
   - `21:42:00-04`：二次提交（PIDs 566219/566224, 566306/566311），ps 输出证实
   - `21:42:57`：首次提交的进程 EXIT trap 触发，写入 exit code 129
   - 首次提交仅运行了 ~170 秒就被杀死

3. **共同父进程**：两批进程的 PPID 都是 `208932`（tmux session `exp_001_sft_0pct_05B`，May 14 创建）。二次提交复用同一 tmux session 的 pane，导致旧进程收到 SIGHUP

4. **排除 OOM**：系统内存 1TB 仅用 56GB；GPU 显存 5.8GB/24GB
5. **排除脚本 bug**：当前重试运行已完成 MMLU 并在跑 GSM8K

### 当前状态

重试运行**健康运行中**，无需干预：
- **d025** (cuda:1)：MMLU 完成，accuracy = **0.5881** (8258/14042)，正在评估 GSM8K
- **d005** (cuda:0)：MMLU 完成，accuracy = **0.5869** (8241/14042)，正在评估 GSM8K

GSM8K 每题约 6 秒，1319 题预计还需 ~2 小时。后面还有 arc_challenge 和 humaneval。

### 结论

无需重试——重试已经自动发生且正在成功执行。根本问题是实验管理系统在 ~3 分钟内对同名实验做了双重提交，违反了 C001 约束（提交前未检查是否已有同类进程）。建议排查是什么触发了二次提交。

---
