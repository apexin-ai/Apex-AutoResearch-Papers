# diagnose urgent gpu status and dispatch

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_urgent-gpu-status-and-dispatch_20260523T023139_result.json`
- **Structured JSON:** [`4de6512d09306e7be30c.json`](../../sessions/4d/4de6512d09306e7be30c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 实际状态

| GPU | 显存占用 | 利用率 | PID | 任务 |
|-----|---------|--------|-----|------|
| cuda:0 | 0 / 98GB | 0% | — | 空闲 |
| cuda:1 | 32.5GB / 98GB | 92% | 194682 | 14B s43 generation |
| cuda:2 | 0 / 98GB | 0% | — | 空闲 |
| cuda:3 | 6.1GB / 98GB | 47% | 214028 | 1.7B s43 with-evi eval |

## PID 状态

| PID | 任务 | 存活? | 运行时间 | 结果 |
|-----|------|-------|---------|------|
| 212762 | 8B s43 with-evi eval | DEAD | — | **已完成** |
| 213753 | 4B s43 with-evi eval | DEAD | — | **已完成** |
| 214028 | 1.7B s43 with-evi eval | ALIVE | 1h23m | 113/500 (23%), ~4.5h 剩余 |
| 194682 | 14B s43 generation | ALIVE | 8h15m | 11352 lines generated |

## 已完成实验结果

**8B s43 with-evi (test_revised):**
- ign_f1=**33.98**, f1=33.98, P=52.08, R=25.22
- evi_f1=60.61, evi_f1_joint=25.83, edcr=79.51
- format_ok=100%, inference=3212s

**4B s43 with-evi (test_revised):**
- ign_f1=**25.03**, f1=25.03, P=33.36, R=20.03
- evi_f1=61.27, evi_f1_joint=17.80, edcr=84.25
- format_ok=99.6%, truncated=237/500, inference=4138s

## 仍在运行的实验

- **1.7B s43 with-evi eval** — cuda:3, 23% done, 预计 ~4.5h 后完成
- **14B s43 generation** — cuda:1, 11352 lines generated, 仍在运行

## 空闲 GPU

**cuda:0, cuda:2**

---
