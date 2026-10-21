# check eval process health

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_eval-process-health_20260514T082552_result.json`
- **Structured JSON:** [`7645a08a3a74742bcf33.json`](../../sessions/76/7645a08a3a74742bcf33.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

**三个进程全部存活**，运行时间约 13 分 45 秒：

| PID | 状态 | 任务 |
|-----|------|------|
| 170770 | Ss+ (正常) | 主 bash wrapper |
| 170786 | Rl (运行中) | eval_gsm8k — `pruned_standard_35` on cuda:0 |
| 170787 | Rl (运行中) | eval_gsm8k — `pruned_rasp_35` on cuda:1 |

**进度**：
- `pruned_standard_35`（PID 170786）：~87/1319 样本（~6.6%），约 7.08s/it
- `pruned_rasp_35`（PID 170787）：~84/1319 样本（~6.4%），约 6.70s/it

**无错误**：日志中没有 OverflowError、Traceback 或其他异常。旧 bug 未触发。

**结果文件**：尚未产出（`results/` 下无 `eval_*.json`，只有之前的 `cka_scores.pt` 和 `importance_scores.pt`）。

**预计完成时间**：按当前速度，两个 eval 分别还需约 2.4 小时（standard）和 2.3 小时（rasp）。

---
