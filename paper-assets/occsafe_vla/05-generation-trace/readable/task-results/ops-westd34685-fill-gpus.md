# ops westd34685 fill gpus

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd34685_fill_gpus_20260523T180247_result.json`
- **Structured JSON:** [`e432c8aa1ab2ccdd980e.json`](../../sessions/e4/e432c8aa1ab2ccdd980e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部确认。总结报告：

---

**1. full_occ_retrain_s0** — 已完成
- 50005 steps, EXIT_CODE=0
- Final: action_loss=0.0417, occ_loss=0.0104
- Checkpoint: `/root/autodl-tmp/checkpoints/full_occ_retrain_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt`
- Registry → DONE (success)

**2. 梯度分析** — 已启动 (GPU 0)
- 修复了两个脚本问题：`conda activate base` → `occsafe`，移除无效 `--gpu 0` 参数
- Vanilla checkpoint 已加载，正在分析中
- GPU 0 占用 15 GB（分析任务比训练轻量）
- 预计需要分析 4 个 condition (vanilla/full_occ/detach/random_occ)，每个约 10-15 分钟

**3. cutoff_15k_s0** — 已启动 (GPU 1, PID 443639)
- 正常训练中：step 10/50005, action_loss=0.6953, occ_loss=0.1073
- 关键修复：cd 目标改为 `/root/occsafe_vla/openvla-oft`，conda env 改为 `occsafe`
- Registry → RUNNING

**4. reverse_cutoff_s0 / cutoff_25k_s0** — 仍在训练
- reverse_cutoff_s0: 87% (step ~43455/50005), GPU 2, ~1:45h remaining
- cutoff_25k_s0: 87% (step ~43548/50005), GPU 3, ~1:40h remaining
- 最新 metrics: reverse action_loss=0.0579, cutoff_25k action_loss=0.0537

**5. GPU 分配表 (westd-34685)**

| GPU | 任务 | 显存 | 利用率 |
|-----|------|------|--------|
| 0 | gradient_analysis | 15 GB | 1% |
| 1 | cutoff_15k_s0 | 63 GB | 81% |
| 2 | reverse_cutoff_s0 | 62 GB | 99% |
| 3 | cutoff_25k_s0 | 62 GB | 99% |

梯度分析完成后 GPU 0 释放给 cutoff_45k_s0。reverse/cutoff_25k 约 1.5-2h 后完成。

---
