# ssh fnlt v2 exit check

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fnlt-v2-exit-check_20260514T030948_result.json`
- **Structured JSON:** [`91609901887c251b2195.json`](../../sessions/91/91609901887c251b2195.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告：plan-001b-fnlt-v2 — **SUCCESS**

| 项目 | 结果 |
|------|------|
| **退出码** | 129 (SIGHUP) @ 2026-05-14T01:51:57Z — 日志显示 vLLM engine 正常 shutdown，episode 收集摘要正常输出后退出，SIGHUP 来自 tmux/终端断开，非异常 |
| **episodes.jsonl** | **40 行，ep 0-39 全部存在，无缺失，无重复** |
| **日志尾部摘要** | `Episodes: 19 (start=21)`, `det-pref=8, int-pref=0, no-pref=11`, `Avg score gap (non-tie): 40.50` |
| **GPU1** | 0 MiB / 0% — 空闲可用 |
| **GPU0** | PID 699929 占用 28004 MiB（其他任务） |

**结论：success。** 40 个 episode 完整收集，GPU1 已释放。

---
