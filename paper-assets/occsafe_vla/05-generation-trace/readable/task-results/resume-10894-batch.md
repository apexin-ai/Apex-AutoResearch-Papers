# resume 10894 batch

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_resume_10894_batch_20260525T173508_result.json`
- **Structured JSON:** [`2ee8fba8fc6aab379ae2.json`](../../sessions/2e/2ee8fba8fc6aab379ae2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 GPU 全部占用，全部训练中。

## 汇总

| 实验 | GPU | PID | 状态 | 说明 |
|------|-----|-----|------|------|
| **cutoff_45k_s2_v2** | cuda:0 | 4294 | 训练中 (step ~250+) | 从头训练，~1.08 it/s |
| **mvp_occ_s3_v2** | cuda:1 | 11641 | 训练中 (step 0+) | Resume from 20K, action_loss=0.08 确认权重恢复 |
| **full_occ_ln_s3_v2** | cuda:2 | 6947→7027 | 训练中 (step ~30+) | Resume from 20K, ~1.08 it/s |
| **ablation_occ_detach_s3_v2** | cuda:3 | 7161→7243 | 训练中 (step ~30+) | Resume from 20K, ~1.08 it/s |

**修复的问题：**
1. Resume 命令原始版本缺少 `--resume_step 20000` 且 `--vla_path` 需要指向 checkpoint 目录而非 pretrained 模型目录
2. cuda:1 被 full_occ_bn_v2_s1 的自动重试占用，需要手动杀掉 orphan 进程释放 GPU

---
