# infra exp006 handoff check

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_exp006-handoff-check_20260514T181301_result.json`
- **Structured JSON:** [`31529533444ce203cbac.json`](../../sessions/31/31529533444ce203cbac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 检查结果

### 1. exp-006 tmux session & 监控

| 项目 | 状态 |
|------|------|
| tmux session | **PASS** — `exp_006_graduated_filtering` 运行中（创建于 May 14 05:02） |
| 当前 run | `graduated_a0.5_s789`，训练进度 37%（1033/2814 steps），~1.29 it/s |
| 完成进度 | **29/50 runs 完成**，第 30 个正在训练 |
| exit trap | 已配置，写入 `/tmp/agent-ml-exit/exp_006_graduated_filtering.exit`，尚未触发（符合预期） |
| cron 监控 | **FAIL** — `CronList` 无任何 scheduled job，服务器也无 `crontab`。当前没有轮询进程存活或完成的 cron 回调 |

### 2. exp-015 重跑脚本

| 项目 | 状态 |
|------|------|
| 脚本 `run_exp015_neural_probe.py` | **PASS** |
| Qwen2.5-1.5B-Instruct | **PASS** |
| Pythia-1.4B | **PASS** |
| OLMo-1B-hf | **PASS** |
| depth_{0..5}.jsonl | **PASS** — 6 个文件全在 |

### 3. exp-006 分析脚本

| 项目 | 状态 |
|------|------|
| 脚本 `exp006_analyze.py` | **PASS** |
| 输出目录 `outputs/exp006/` | **PASS**（30 个子目录，29 个含 eval_results.json） |

### 需要处理

cron 监控缺失。exp-006 的 tmux exit trap 会在完成时写 exit 文件，但没有 cron job 来轮询这个文件并触发后续衔接（通知 / 启动 exp-015）。需要补建 cron 监控吗？

---
