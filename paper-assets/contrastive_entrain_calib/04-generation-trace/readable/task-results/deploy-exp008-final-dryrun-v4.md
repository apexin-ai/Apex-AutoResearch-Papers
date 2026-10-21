# deploy exp008 final dryrun v4

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_exp008-final-dryrun-v4_20260518T175556_result.json`
- **Structured JSON:** [`345057e2eec8a2366ec7.json`](../../sessions/34/345057e2eec8a2366ec7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

log_steps 已恢复。进程已结束，GPU 1 内存回到 38GB（训练前基线）。

## Dry-run v4 结果

| 指标 | 值 | 判定 |
|------|-----|------|
| **Probe accuracy** | 0.9945 | PASS (>0.95) |
| **S(t)** | 0.5694 | PASS (合理中间值，不是 0 或 1) |
| **loss** | 2.0469 | PASS |
| **sft** | 2.0488 | PASS |
| **R3** | mean=0.5000, step1=0.5881 | PASS (min=0.0001, max=0.9999, 有分布) |
| **VRAM** | 训练完成后已释放，训练期间 ~98GB 卡内完成 | PASS |
| **数据** | 362 samples | PASS |

**Dry-run v4: PASS**

关键改进确认：probe 归一化后 accuracy 从之前的问题值恢复到 0.9945，S(t)=0.5694 是合理的非退化值（不是恒 0/1），说明 feat_mean/feat_std buffers 正确工作。

注意：当前服务器是 westd-29046，配备 2x RTX PRO 6000 Blackwell (98GB)，不是任务中写的 westd-28034 / RTX 5090 32GB。正式训练应使用 `CUDA_VISIBLE_DEVICES=1`（GPU 1 空闲更多）。

---
