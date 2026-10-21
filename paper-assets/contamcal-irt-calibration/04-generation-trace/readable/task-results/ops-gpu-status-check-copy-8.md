# ops gpu status check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-status-check_20260514T105834_result.json`
- **Structured JSON:** [`6ef2bc472970315c7e11.json`](../../sessions/6e/6ef2bc472970315c7e11.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态总览

| GPU | PID | VRAM | 实验 | 进度 |
|-----|-----|------|------|------|
| **0** | 353390 | 1.9G/24G | exp002 `compute_signals.py` 0.5B | [1/9] 刚启动，mmlu d000 信号计算 |
| **1** | **336765** | 5.8G/24G | exp001 eval 1.5B aligned batch | GSM8K original 898/1319 (**68%**) |
| **2** | **354435** | 3.7G/24G | exp001 eval 0.5B aligned batch | GSM8K paraphrased 68/228 (**30%**), original 已完成 |
| **3** | 319555 | 13.3G/24G | exp001 SFT d100 3B | step 3242/4159 (**78%**), epoch 0.76, loss ~1.17 |
| **4** | 335351 | 21.8G/24G | exp001 SFT d005 3B | step 1511/3177 (**48%**), epoch 0.35, loss ~1.11 |
| **5** | 342940 | 9.0G/24G | exp001 eval 3B d000 aligned | GSM8K original 484/1319 (**37%**) |

## 需要注册 cron 监控的实验

- **cuda:1 — exp_001_eval_15B_aligned_batch**: Python PID **336765**, wrapper PID 336754
- **cuda:2 — exp_001_eval_05B_aligned_batch**: Python PID **354435**, wrapper PID 332211

两个 eval batch 进程都在正常跑，log 持续写入 `~/runs/contamcal-irt-calibration/`。

### 补充说明
- GPU 4 的 SFT d005 训练进程实际 PID 是 **335351**（不是 cron 里的 335346，335350 是 timeout wrapper）
- GPU 3 的 SFT d100 已经跑了 4 小时，预计还需 ~1h 完成
- GPU 0 上跑的是 exp002 信号计算（不是 exp001）

---
