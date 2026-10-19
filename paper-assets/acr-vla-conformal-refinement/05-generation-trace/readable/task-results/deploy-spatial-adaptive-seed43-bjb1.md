# deploy spatial adaptive seed43 bjb1

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_spatial-adaptive-seed43-bjb1_20260523T033431_result.json`
- **Structured JSON:** [`5b6aad2a16d5d43f3016.json`](../../sessions/5b/5b6aad2a16d5d43f3016.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

bjb1-32546 环境完备（CRM checkpoint、SmolVLA 模型、adaptive_conformal_crm 代码都在）。

**状况汇报：**

**bjb1-18228 的 4 张 GPU 全部被 π0.5 precompute 占满：**
| GPU | 进程 | 显存 |
|-----|------|------|
| 0 | precompute --benchmark object | 9874 MiB |
| 1 | precompute --benchmark spatial | 9874 MiB |
| 2 | precompute --benchmark goal | 9874 MiB |
| 3 | precompute --benchmark long | 9874 MiB |

cuda:3 不可用。每个 shard（500 samples）约 16 分钟，long 已到 14000，完成时间不确定。

**建议改在 bjb1-32546:cuda:3 部署：**
- GPU 3 当前仅运行 CRM 训练（534 MiB / 24564 MiB），剩余 ~24GB
- SmolVLA eval 约需 5-6GB，可共存
- CRM checkpoint、SmolVLA 模型、adaptive_conformal_crm 代码全部就绪

从 seed42 日志提取的精确命令（改 seed=43）：
```
CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py \
  --mode adaptive_conformal_crm \
  --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt \
  --benchmark spatial --seed 43 --n_rollouts 20 --K 10 \
  --model smolvla --conformal_threshold 0.074855 \
  --output_file logs/eval_spatial_adaptive_conformal_crm_tau0.074855_seed43.json
```

是否在 bjb1-32546:cuda:3 上提交？还是等 bjb1-18228 的 precompute 跑完？

---
