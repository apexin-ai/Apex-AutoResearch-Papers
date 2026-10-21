# prepare eval cka scripts

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prepare_eval_cka_scripts_20260525T193228_result.json`
- **Structured JSON:** [`fff5eb7c89090653c2de.json`](../../sessions/ff/fff5eb7c89090653c2de.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

---

## 1. Eval 脚本参数格式

`evaluate_safelibero.py`，关键参数：
- `--pretrained_checkpoint &lt;path>` — 指向包含 `config.json` 和 model safetensors 的目录
- `--task_suite_name libero_spatial`
- `--num_rollouts 50`
- `--seed 42`
- `--output_path &lt;json_path>`
- 环境变量：`CUDA_VISIBLE_DEVICES`, `MUJOCO_GL=egl`, `MUJOCO_EGL_DEVICE_ID`

## 2. 批量 Eval 脚本路径

| 服务器 | 脚本 | 实验 |
|--------|------|------|
| westd-10894 | `/root/occsafe_vla/eval_batch_10894.sh` | cutoff_45k_s2_v2(GPU0), mvp_occ_s3_v2(GPU1), full_occ_ln_s3_v2(GPU2), ablation_occ_detach_s3_v2(GPU3) |
| westd-34685 | `/root/occsafe_vla/eval_batch_34685.sh` | detach_bn_v2_s0(GPU0), detach_bn_v2_s1(GPU1), detach_bn_v2_s2(GPU2), full_occ_bn_v2_s1(GPU3) |

用法：训练完成后直接 `bash /root/occsafe_vla/eval_batch_10894.sh`，脚本会先验证 checkpoint 存在性再启动。

## 3. CKA 脚本

- 已有脚本：`/root/occsafe_vla/analysis/cka_analysis.py`
- 批量命令：`/root/occsafe_vla/cka_batch_s3.sh`（4 条件 vs pretrained）
- 用法：`CUDA_VISIBLE_DEVICES=0 bash /root/occsafe_vla/cka_batch_s3.sh`

## 4. Checkpoint 命名约定

所有实验的最终 checkpoint 统一为 `--50000_chkpt` 后缀（全局 step 50000）：
```
{CKPT_ROOT}/{exp_parent}/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--{exp_name}--50000_chkpt
```

**Resume 实验的关键点**：v2 resume 实验写入 v1 同名目录（不是 `_v2` 目录），因为 resume 模式下 `run_id` 继承自原始 checkpoint 路径。例如 `mvp_occ_s3_v2` 的 checkpoint 在 `checkpoints/mvp_occ_s3/` 下。

## 5. 发现的问题

- **v2 resume 实验尚未产出任何 checkpoint**（当前进度 ~14%，约 step 7K/50K）。ETA 比预期晚——按当前速率 ~1.08 it/s，还需约 21K 步才到 30K local step，预计 ~5-6h。
- **CKA 脚本中 cutoff_45k_s2_v2 不是 s3 实验**（是 s2 seed）。如果 CKA 严格要求同 seed 对比，可能需要替换为其他 s3 条件或去掉。请确认 4 个条件的具体组合。

---
