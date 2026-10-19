# monitor m1 progress check

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_m1_progress_check_20260513T013124_result.json`
- **Structured JSON:** [`885bd544195eed82c879.json`](../../sessions/88/885bd544195eed82c879.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## M1 全量提取进度报告

| 指标 | 状态 |
|------|------|
| **进程 PID** | 577864，存活，运行 4h43m |
| **活跃度** | 过去 5 分钟内仍有新文件产出，正常运行中 |
| **已完成 repos** | 23/131（产出文件） + 1/131（pdfminer 跳过，clone_failed） = **24/131** |
| **进度** | **18.3%** |
| **产出文件数** | 5,426 个 JSON |
| **产出大小** | 2.2 GB |
| **跳过** | 660 instances（全部是 `pdfminer__pdfminer.six`，原因 `clone_failed`） |
| **磁盘** | /root/autodl-tmp 169GB 总量，**16GB 剩余（91% 已用）** |

### 已完成的 23 个 repos
Cog-Creators/Red-DiscordBot, Knio/dominate, PyCQA/flake8, Suor/funcy, agronholm/exceptiongroup, agronholm/typeguard, bottlepy/bottle, cantools/cantools, cknd/stackprinter, jaraco/inflect, jd/tenacity, joke2k/faker, keleshev/schema, luozhouyang/python-string-similarity, madzak/python-json-logger, mahmoud/boltons, marshmallow-code/webargs, oauthlib/oauthlib, pudo/dataset, pygments/pygments, pytest-dev/iniconfig, pyupio/safety, seatgeek/thefuzz

### 预计剩余时间
当前运行 4h43m 完成 24 repos，约 12 min/repo。剩余 107 repos，预计 **~21 小时**。

### 风险
- **磁盘**：当前 2.2GB/24 repos，按此比例 131 repos 约 12GB，16GB 余量应该够但偏紧。后续大 repo（如 faker 有大量 instances）可能消耗更多空间，需持续关注。
- **pdfminer clone_failed**：660 个 instance 全部跳过，可能需要后续修复（检查 Git 仓库可达性）。

---
