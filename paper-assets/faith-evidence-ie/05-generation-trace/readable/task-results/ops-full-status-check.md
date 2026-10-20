# ops full status check

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_full-status-check_20260514T202707_result.json`
- **Structured JSON:** [`16dd486240de3c2475c2.json`](../../sessions/16/16dd486240de3c2475c2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 概览
```
cuda:0: PID 90085  grpo_trainer (lr5e6_r1)           73%  13645/32607 MiB
cuda:1: PID 96500  eval inference (lr5e6 ckpt-20)    79%   9069/32607 MiB
cuda:2: PID 95373  eval inference (kl001 ckpt-30)    70%   8477/32607 MiB
cuda:3: PID 94055  grpo_trainer (rp_r1)              92%  27286/32607 MiB
        PID 94758  grpo_trainer (rp_r2)                    ← 两个进程共享!
```

## P0 (lr5e6_r1) 进度
- **Step: 25/200** (12.5%), ~108s/it, 预计还需 ~5.4h
- KL divergence 异常高: 2,412,554,396.9 (step 5 时触发 warning, 阈值 100.0)
- **Checkpoint-20: YES** — 已保存 (05-15 04:17), 含 adapter_model.safetensors (264MB)

## P0+P1 冲突 ⚠️
```
PID 94055 (rp_r1): ALIVE — Rl+ 状态, 启动 04:04:08, 由 .sh 脚本启动
PID 94758 (rp_r2): ALIVE — Rl  状态, 启动 04:05:27, 由 submit_training_job 启动
```
**结论: 两个都活着，同时跑在 cuda:3 上，且写同一个 output_dir `/root/autodl-tmp/grpo_ced_lr5e6_rp`。** 这是真冲突——同 output_dir 的 checkpoint 会互相覆盖，显存也在争抢 (27286/32607 MiB，92% 利用率)。rp_r2 的速度明显更慢 (~160s/it vs rp_r1 正常应是 ~111s/it)，两者都有 KL 爆炸问题。

rp_r2 进度: step 8/200 (4%), KL 更高达 39,401,782,765。

## Multi Eval 进度
**grpo_ced_kl001 评估** (PID 78856 → 95373, cuda:2):
- 已完成: checkpoint-10, 20, 50, 60, 90 (结果已保存)
- checkpoint-20 结果: F1=0.0088, Ign-F1=0.0088, Evi-F1=0.4230, EDCR=0.9954
- **当前: checkpoint-30, inference 32% (20/62 batches)**

**grpo_ced_lr5e6 评估** (PID 96499 → 96500, cuda:1):
- 当前: checkpoint-20 inference 刚启动

## cuda:1
**NOT FREE** — PID 96500 正在跑 grpo_ced_lr5e6/checkpoint-20 的 eval inference。

---

**需要处理的问题:**
1. **cuda:3 冲突**: rp_r1 和 rp_r2 同 GPU 同 output_dir，需要 kill 一个。建议保留先启动的 rp_r1 (PID 94055)，kill rp_r2 (PID 94758/94753)
2. **KL 爆炸**: 两个 lr5e6 训练 (r1 和 rp_r1) 都有极端 KL divergence，可能影响训练质量

---
