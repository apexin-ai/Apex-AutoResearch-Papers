# ops gpu status full check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-status-full-check_20260515T113815_result.json`
- **Structured JSON:** [`597a6d0900965e6cdb83.json`](../../sessions/59/597a6d0900965e6cdb83.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态总览

```
GPU 0: 41%  253W  14.9/24.6GB  PID 549516 / 1.5B d025 s123 SFT v2       RUNNING (33min)
GPU 1: 71%  279W  16.0/24.6GB  PID 549858 / 1.5B d005 s123 SFT v2       RUNNING (33min)
GPU 2: 32%   94W   3.6/24.6GB  PID 553256 / 0.5B base pretrained eval v2 RUNNING (7min)
GPU 3: 64%  204W   9.0/24.6GB  PID 551219 / 3B d000 s123 aligned eval    RUNNING (26min)
GPU 4:  0%   12W  10.3/24.6GB  PID 530975 / 1.5B base pretrained eval    RUNNING (2h53m) ⚠️ 0% util
GPU 5: 63%  192W   9.0/24.6GB  PID 551290 / 3B d005 s42 aligned eval     RUNNING (26min)
CPU:   —     —     —           PID 528993 / extreme gamma sweep           RUNNING (3h03m)
```

## 实验状态

| 实验 | PID | GPU | 状态 | 备注 |
|------|-----|-----|------|------|
| exp_008_base_pretrained_eval_v2 (0.5B) | 553256 | 2 | **RUNNING** | 正在跑 MMLU，2%进度（~78 it/s），MMLU 已出: **0.2294**，GSM8K 刚开始跑（50/1319） |
| 1.5B d025 s123 SFT v2 | 549516 | 0 | **RUNNING** | 33min，checkpoint 目录为空（尚未产出 adapter） |
| 1.5B d005 s123 SFT v2 | 549858 | 1 | **RUNNING** | 33min，checkpoint 目录为空（尚未产出 adapter） |
| 3B d000 s123 aligned eval | 551219 | 3 | **RUNNING** | 26min，结果目录为空（尚未写出） |
| 3B d005 s42 aligned eval | 551290 | 5 | **RUNNING** | 26min，eval.log 显示 MMLU 在跑（~20 it/s），有 bitsandbytes 警告（非致命）+ HF 超时重试（已恢复） |
| 1.5B base pretrained eval | 530975 | 4 | **⚠️ RUNNING 但 0% GPU util** | 已跑 2h53m，GPU 利用率 0% 但占 10.3GB 显存，可能卡住 |
| extreme gamma sweep | 528993 | CPU | **RUNNING** | 3h03m |

## 2PL coverage pipeline

- `results_2pl_matched/` — **NOT_FOUND**
- `results_s1only_gsm8k_2pl/` — **NOT_FOUND**

## 需关注

1. **GPU 4 (PID 530975)** — 1.5B base pretrained eval 跑了近 3 小时但 GPU 利用率 0%，可能卡在 I/O 或 HuggingFace 下载。需要查 log 确认。
2. 两个 SFT 训练（GPU 0/1）刚启动 33 分钟，adapter 尚未产出，正常。
3. 0.5B eval v2 的 MMLU 部分结果：**accuracy = 0.2294**（接近随机，符合 0.5B base 预期）。

---
