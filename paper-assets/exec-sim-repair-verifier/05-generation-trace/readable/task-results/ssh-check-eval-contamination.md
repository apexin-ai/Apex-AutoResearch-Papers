# ssh check eval contamination

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-eval-contamination_20260521T134613_result.json`
- **Structured JSON:** [`4f72f8a3ec27ad6485ce.json`](../../sessions/4f/4f72f8a3ec27ad6485ce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

**污染确认并已修复。**

| 项目 | 详情 |
|------|------|
| **结果文件** | `/root/autodl-tmp/eval_results/deepseek_cwm_repo_s456_v2_eval/results_incremental.jsonl` |
| **污染情况** | 前 416 条来自 checkpoint-8418 (epoch 2)，第 417-460 条来自 checkpoint-12627 (epoch 3) |
| **根因** | eval 脚本的 resume 逻辑只按 `index` 跳过已完成条目，不校验 checkpoint 来源；两次 eval 共用同一 output_dir |
| **已执行** | kill 旧进程 → 备份为 `results_contaminated_e2e3_mix.jsonl` → 干净重启 |
| **新 eval 确认** | 日志显示 `[CWM] 4/9784 running_acc=50.0% (new=4 resumed=0)` — 从 0 开始，无污染 |
| **新 PID** | **63490** |
| **tmux session** | `ds-s456-e3-eval` |
| **日志** | `/root/ds_s456_e3_eval_clean.log` |

---
