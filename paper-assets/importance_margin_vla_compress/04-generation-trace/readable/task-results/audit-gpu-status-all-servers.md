# audit gpu status all servers

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_gpu_status_all_servers_20260526T100629_result.json`
- **Structured JSON:** [`a9f7727623f9eaa2d3e4.json`](../../sessions/a9/a9f7727623f9eaa2d3e4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态审计结果

---

### 1. westd-38929 (4× RTX PRO 6000 Blackwell, 98GB)

| GPU | 利用率 | 显存 | PID | 实验 |
|-----|--------|------|-----|------|
| 0 | 0% | 1 MiB | — | **空闲** ✅ |
| 1 | 74% | 16.0 GB | 279274 | OpenVLA Random k=0.5 Long seed42 ✅ |
| 2 | 87% | 15.6 GB | 412621 | OpenVLA Attn k=0.85 Goal seed42 ✅ |
| 3 | 67% | 15.6 GB | 288325 | OpenVLA Attn k=0.85 Object seed42 (新发现) |

> cuda:0 空闲符合预期。cuda:1/2 与预期一致。cuda:3 跑的是 Attn k=0.85 Object（之前"待确认"，现已确认）。

---

### 2. westd-41074 (4× RTX PRO 6000 Blackwell, 98GB)

| GPU | 利用率 | 显存 | PID | 实验 |
|-----|--------|------|-----|------|
| 0 | 64% | 15.8 GB | 415537 | OpenVLA Random k=0.85 Long seed42 ✅ |
| 1 | 67% | 15.6 GB | 482875 | OpenVLA L2norm k=0.85 Object seed42 ✅ |
| 2 | 75% | 15.6 GB | 542010 | OpenVLA Attn k=0.7 Object seed42 ✅ |
| 3 | 88% | 15.6 GB | 482950 | OpenVLA L2norm k=0.95 Object seed42 ✅ |

> 4 卡全满，全部与预期一致。

---

### 3. westd-27271 (2× RTX PRO 6000 Blackwell, 98GB)

| GPU | 利用率 | 显存 | PID | 实验 |
|-----|--------|------|-----|------|
| 0 | 75% | 15.6 GB | 207593 | OpenVLA L2norm k=0.85 Goal seed42 ✅ |
| 1 | 70% | 15.6 GB | 112477 | OpenVLA Attn k=0.9 Goal seed43 ✅ |

> 2 卡全满，全部与预期一致。

---

### 4. cqa1-33015 (4× RTX 4090 D, 24GB)

| GPU | 利用率 | 显存 | PID | 实验 |
|-----|--------|------|-----|------|
| 0 | 57% | 9.8 GB | 212677 | **π0.5 L2norm k=0.75 Long seed42** |
| 1 | 8% | 10.0 GB | 213217 | **π0.5 Attn k=0.75 Long seed42** |
| 2 | 0% | 1 MiB | — | **空闲** |
| 3 | 0% | 1 MiB | — | **空闲** ⚠️ |

> ⚠️ **cuda:3 预期跑 π0.5 Random k=0.5 Long v3，实际进程已消失**——与 cron 报告一致。
> cuda:0/1 跑的是 π0.5 的 L2norm 和 Attn k=0.75 实验（不在原预期列表中）。
> cuda:2/3 均空闲，可调度新任务。

---

### 汇总

- **空闲 GPU**: westd-38929 cuda:0, cqa1-33015 cuda:2, cqa1-33015 cuda:3 — 共 3 张
- **异常**: cqa1-33015 cuda:3 的 π0.5 Random k=0.5 Long v3 已挂掉，需要决定是否重启
- **满载**: westd-41074 (4/4), westd-27271 (2/2)

---
