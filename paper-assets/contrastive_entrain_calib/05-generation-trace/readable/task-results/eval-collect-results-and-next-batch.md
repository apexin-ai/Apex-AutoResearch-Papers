# eval collect results and next batch

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_collect-results-and-next-batch_20260522T221718_result.json`
- **Structured JSON:** [`8f7c4f46ced7a05f32e4.json`](../../sessions/8f/8f7c4f46ced7a05f32e4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息收集完毕。

```
=== 28034 GPU 状态 ===
GPU0: reduced-lora ckpt-1500 eval, PID 136668, 16834MiB ✓刚启动
GPU1: reduced-lora 训练, PID 30011, step 2730, 21758MiB
GPU2: reduced-lora ckpt-2000 eval, PID 137176, 16754MiB ✓刚启动
GPU3: gs8 ckpt-500 verify eval, PID 131250, 260/362 (~72%), 运行中

=== Eval 结果 ===
ACT s2 ckpt-6000: ✓完成
  Log (exp003 D027):   ToF=0.0497, NoF=0.9503, SYCONScore=0.0945
  JSON (exp-004-s2-v2): ToF=0.1547, NoF=0.8674, SYCONScore=0.2626

ACT s2 ckpt-5500: ✓完成
  Log (exp003 D027):   ToF=0.0608, NoF=0.9724, SYCONScore=0.1144
  JSON (exp-004-s2-v2): ToF=0.1326, NoF=0.8785, SYCONScore=0.2304

gs8 ckpt-500 verify: 运行中, 260/362 (~72%)

注意：log 和 eval_results/ 中的 JSON 来自不同的 eval run（exp003 vs exp-004-s2-v2），
指标差异较大。JSON 文件在 eval_results/ 目录，最近 2 小时内修改过。

=== 新启动的 Eval ===
reduced-lora ckpt-1500: GPU0, PID=136668 ✓已确认占用 GPU
reduced-lora ckpt-2000: GPU2, PID=137176 ✓已确认占用 GPU
(lora_path: /root/autodl-tmp/outputs/exp-004-reduced-lora/checkpoint-{1500,2000})

=== 29046 训练进度 ===
ACT s2:     step 6530/8000 (81.6%), ~9.1s/step, 剩余约 3.7h
gs8 r3only: step  868/8000 (10.9%), ~24.3s/step, 剩余约 48h
新 checkpoint:
  - exp-004-act-baseline-s2/checkpoint-6500 (May 23 06:14) ← 最新
  - exp003_gs8_r3only/checkpoint-500 (May 23 03:52) ← 仅此一个

reduced-lora 训练 (28034 GPU1): step 2730, ~6.7s/step, 已跑 5.6h
```

---
