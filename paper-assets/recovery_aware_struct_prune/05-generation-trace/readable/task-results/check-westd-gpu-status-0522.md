# check westd gpu status 0522

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_westd_gpu_status_0522_20260522T083258_result.json`
- **Structured JSON:** [`4dcf5f3e12962bb25d46.json`](../../sessions/4d/4dcf5f3e12962bb25d46.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
GPU 0: [忙] PID=2234  命令=eval_math500 grpo_stage2_standard_20_fair  显存=19242MiB  运行=4h46m
GPU 1: [忙] PID=5241  命令=eval_math500 sft_random_20               显存=17642MiB  运行=4h23m
GPU 2: [忙] PID=22661 命令=eval_gsm8k grpo_rasp_alpha2p0_20/ckpt-100 显存=16486MiB  运行=1h11m
GPU 3: [空闲] 0MiB / 0%

磁盘: /root/autodl-tmp/ 526G/650G (81%)
```

**关键发现:**

1. **GPU 0/1 — MATH-500 eval 进行中:**
   - GPU 0: `grpo_stage2_standard_20_fair` → 331/500 (66%), Acc@300 = 27.0%, 预计还需 ~2-3h
   - GPU 1: `sft_random_20` → 222/500 (44%), 预计还需 ~4-5h

2. **GPU 2 — α=2.0 管线:**
   - 原 pipeline GRPO 训练已完成，GSM8K eval 在日志中被 `Terminated`（只跑到 15/5604）
   - 但重新启动了 eval_gsm8k（PID 22661），正在跑 `grpo_rasp_alpha2p0_20/checkpoint-100`，GPU 利用率 96%，正常运行中

3. **GPU 3 — α=0.5 管线异常:**
   - 原 pipeline GSM8K eval 同样只到 15/5604 后日志停止更新（14:48）
   - PID 20444 (`eval_gsm8k sft_rasp_alpha0p5_20`) 已运行 1h33m，但 **不在 nvidia-smi 中**（0 GPU 显存），CPU 仅 1.6%
   - **很可能卡住了** — 该进程应该用 CUDA_VISIBLE_DEVICES=3 但 GPU 3 完全空闲，说明模型没有成功加载到 GPU 上。需要检查或 kill 后重启

4. **α=0.5 的 GRPO eval (grpo checkpoint) 还没跑** — pipeline 日志显示 GRPO 训练后的 eval 被 terminated，当前只在跑 SFT eval（且卡住了）

---
