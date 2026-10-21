# ops status check

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_status-check_20260514T220234_result.json`
- **Structured JSON:** [`543084f41406049ccdcb.json`](../../sessions/54/543084f41406049ccdcb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

| 实验 | GPU | PID | 进度 | ETA | 状态 |
|------|-----|-----|------|-----|------|
| **mvp2_grpo_ced_lr5e6_r1** (训练) | cuda:0 | 90085 | 76/200 (38%) | ~4h | 正常，KL divergence 告警但未停止 |
| **mvp2_eval_lr5e6_r1_ckpt20** | cuda:1 | 96500 | 58/62 (94%) | **~7min** | 即将完成 |
| **mvp2_eval_lr5e6_r1_ckpt40_r2** | cuda:2 | 101842 | 22/62 (35%) | ~1h5m | 正常（05:25 重启，首次 run 被 SIGTERM） |
| **mvp2_eval_lr5e6_rp_r2_ckpt20** | cuda:3 | 103831 | 11/62 (18%) | ~1h50m | 正常，但与 sft_baseline 共享 GPU 3，速度受影响 |
| **mvp2_eval_sft_baseline** | cuda:3 | 104979 | 4/62 (6.5%) | ~2h20m | **正在跑**，tee 日志写入失败（logs 目录不存在），进度仅 tmux 可见 |

**P0 训练 checkpoints**: checkpoint-20, checkpoint-40, checkpoint-60 已保存。

**注意事项**:
- GPU 3 同时跑两个 eval（rp_ckpt20 + sft_baseline），各占 ~9.7GB，合计 ~19.4GB/32GB，显存够但互相争抢算力，推理速度明显比单卡慢
- ckpt20 eval 约 7 分钟后完成，完成后 cuda:1 空闲
- sft_baseline 的 tee 日志失败不影响推理本身，结果会写到 output_dir

---
