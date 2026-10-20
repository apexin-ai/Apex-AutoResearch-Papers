# ssh check 5epoch and pretrained progress

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_5epoch_and_pretrained_progress_20260521T193528_result.json`
- **Structured JSON:** [`865ef891854fdb69ba13.json`](../../sessions/86/865ef891854fdb69ba13.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据收集完毕。汇总如下：

---

## autodl-5090

| 实验 | PID | 状态 | 进度 | GPU |
|------|-----|------|------|-----|
| **5-epoch s42** (cuda:1) | 63198 | ALIVE | 264,160 / 301,184 (**87.7%**) | GPU1: 73%, 30222 MiB |
| **5-epoch s123** (cuda:2) | 63337 | ALIVE | 260,856 / 301,184 (**86.6%**) | GPU2: 80%, 30194 MiB |
| **pretrained s456** (cuda:3) | 47635 | ALIVE | 23,554 / 37,648 (**62.6%**) | GPU3: 73%, 30540 MiB |
| GPU 0 | — | idle | — | 0%, 2 MiB |

- 5ep s42/s123 ETA ~12-15 min
- pretrained s456 ETA ~13 min（进度条显示 `21:11 elapsed, ~14 min remaining`）
- 注意：pretrained s456 的进度条按 instance 计数（37648），而非 prompts（301184），可能是不同代码版本
- **所有 output 目录都是空的**（没有 samples.jsonl），代码在推理完成后才写入

## autodl-5090-c

| 实验 | PID | 状态 | 进度 | GPU |
|------|-----|------|------|-----|
| **5-epoch s456** (cuda:0) | 353735 | ALIVE | 130,784 / 301,184 (**43.4%**) | GPU0: 92%, 30259 MiB |
| **pretrained s42** (cuda:3) | 346388 | ALIVE | 98,968 / 301,184 (**32.9%**) | GPU3: 79%, 30295 MiB |
| **pretrained s456** (cuda:2) | 345834 | **CRASHED** | 47,392 / 301,184 (15.7%) 后崩溃 | GPU2: 0%, 0 MiB |
| GPU 1 | — | idle | — | 0%, 0 MiB |

- 5ep s456 ETA ~55 min
- pretrained s42 ETA ~2.5h
- **pretrained s456 已崩溃**：日志显示 `02:53:46 Shutdown initiated (timeout=0), Aborting 253282 requests`，GPU 已释放

## 关键问题

1. **pretrained s456 未完成**（5090 上仍在 62.6%），跳过 recompute
2. **5090-c 上 pretrained s456 崩溃**，cuda:2 空闲，需要重启
3. 5090 上 `/tmp/recompute_s456.log` 的监控脚本持续报 "File does not exist yet"，等待中

---
