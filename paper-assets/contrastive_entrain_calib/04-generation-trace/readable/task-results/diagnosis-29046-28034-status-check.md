# diagnosis 29046 28034 status check

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnosis_29046-28034-status-check_20260520T110649_result.json`
- **Structured JSON:** [`2f3831ff75c6da26d987.json`](../../sessions/2f/2f3831ff75c6da26d987.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

模型加载中，已正常启动。

---

## 29046 进程状态
exp-003 seed 1 (PID 70649): **存活** — 运行 1天18小时15分，GPU 1，95% 利用率，38152MiB
exp-003-s2 seed 2 (PID 237432→237437): **存活** — 运行 10小时49分，GPU 0，98% 利用率，38040MiB
两块 RTX PRO 6000 (96GB) 均满载正常，此前异常报告为误报。

## 28034 状态
vanilla reeval: **完成**
ToF: 0.0718 | NoF: 0.9448 | **SYCONScore: 0.1335**
⚠️ 注意：SYCONScore 0.1335 显著低于之前记录的 0.197 baseline，D027 unified preset 重跑结果不一致。

exp-009 ckpt-1000 eval: **进行中** — 260/362 (72%)，预计 ~25 分钟完成，GPU 3

GPU 0: **空闲** (5MiB/32607MiB)
exp-003 ckpt-5000 eval: **已启动** (PID 576346, GPU 0, westd-28034)

---
