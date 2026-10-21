# monitor post reboot check

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_post_reboot_check_20260515T060209_result.json`
- **Structured JSON:** [`178723713b083e66ea48.json`](../../sessions/17/178723713b083e66ea48.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 进程状态
- vota_no_ae_seed42 (pid 953133): **存活** — 已运行 1h41m
- full_trace_label_only_seed42 (pid 955296): **存活** — 已运行 1h14m

## 训练进度

| 实验 | 进度 | Epoch | Loss | Token Acc | 速度 | 剩余时间 |
|------|------|-------|------|-----------|------|----------|
| vota_no_ae_seed42 | 425/444 (96%) | 1.96 | 0.0355 | 0.9889 | ~14s/it | **~4-5 min** |
| full_trace_label_only_seed42 | 228/444 (51%) | ~1.03 | 0.0969 (epoch 0.95) | 0.9688 | ~18.7s/it | **~1h07m** |

**vota_no_ae** 细节：
- Eval@epoch1.0: eval_loss=0.1744, eval_token_acc=0.9590
- 训练 loss 从 epoch1 的 0.0702 持续下降到 0.0355，收敛良好

**full_trace_label_only** 细节：
- label_only_loss=True, gradient_checkpointing 已开启
- Loss 从 6.78 快速降到 0.0969，仍在第一轮末尾/第二轮初期

## GPU

| GPU | 型号 | 利用率 | 显存 | 温度 |
|-----|------|--------|------|------|
| 0 | RTX PRO 6000 Blackwell | 100% | 90355/97887 MiB (92%) | 76°C |
| 1 | RTX PRO 6000 Blackwell | 98% | 52779/97887 MiB (54%) | 71°C |

## 磁盘
autodl-tmp: 54G / 250G used (22%)

---

vota_no_ae_seed42 即将完成（~5分钟内）。full_trace_label_only_seed42 预计还需约1小时。两个进程均正常运行，GPU 满载，无异常。

---
