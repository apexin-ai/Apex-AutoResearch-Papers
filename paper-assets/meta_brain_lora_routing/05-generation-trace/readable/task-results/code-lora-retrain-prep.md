# code lora retrain prep

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_lora_retrain_prep_20260516T101043_result.json`
- **Structured JSON:** [`f973566b7111c2e22d88.json`](../../sessions/f9/f973566b7111c2e22d88.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。以下是总结：

---

## 1. 训练脚本 base model 路径 — 已参数化

`train_lora_expert.py` 原本就有 `--checkpoint` 参数（默认 `pi0_base`），无需修改加载逻辑。

**唯一代码改动**（2 处）：

```diff
# phase1/train_lora_expert.py

# L100: 新增 --run_prefix 参数
  g.add_argument("--output_dir", default=DEFAULT_OUTPUT_DIR)
+ g.add_argument("--run_prefix", default="",
+                help="Prefix for run name and output subdir (e.g. 'v2_')")

# L219: run_name 使用 prefix
- run_name = f"lora_{args.perturbation_type}_r{args.lora_rank}"
+ run_name = f"{args.run_prefix}lora_{args.perturbation_type}_r{args.lora_rank}"
```

dtype 已兼容：`load_pi0_model` 创建 `Pi0Config(dtype="bfloat16")`，forward 用 `torch.amp.autocast(dtype=torch.bfloat16)`，与 pi0_libero bf16 safetensors 完全匹配。

## 2. 之前训练的完整配置参数（从日志提取）

| 参数 | 值 |
|---|---|
| base checkpoint | `/root/autodl-tmp/checkpoints/pi0_base/model.safetensors` |
| lora_rank | 16 |
| lora_alpha | 32 |
| lora_dropout | 0.05 |
| target_modules | PaliGemma Q/K/V/O (`layers.*.self_attn.{q,k,v,o}_proj`) |
| trainable params | 3,686,400 / 3,505,058,576 (0.11%) |
| lr | 2e-4 |
| batch_size | 16 |
| num_train_steps | 10000 |
| warmup_steps | 100 |
| optimizer | AdamW (β1=0.9, β2=0.95, wd=0.01) |
| grad_clip_norm | 1.0 |
| num_workers | 4 |
| data | 97 episodes, 66984 frames (libero_object_image) |
| ~training time | ~170 min per run |
| final loss | 0.0107–0.0114 |

## 3. 4 路重训配置

所有超参与 v1 保持一致，仅换 base checkpoint + 输出目录加 `v2_` 前缀：

| 任务 | GPU | checkpoint | output_dir |
|---|---|---|---|
| v2_lora_visual_r16 | 0 | pi0_libero | `checkpoints/v2_lora_visual_r16/` |
| v2_lora_spatial_r16 | 1 | pi0_libero | `checkpoints/v2_lora_spatial_r16/` |
| v2_lora_physical_r16 | 2 | pi0_libero | `checkpoints/v2_lora_physical_r16/` |
| v2_lora_universal_r16 | 3 | pi0_libero | `checkpoints/v2_lora_universal_r16/` |

## 4. 启动脚本

已创建 `/root/meta_brain_lora_routing/scripts/launch_v2_lora_training.sh`（102 行，已 chmod +x）。

功能：
- 检查 pi0_libero checkpoint 存在性
- 检测可用 GPU 数量（<4 时警告并 cycling）
- 4 路 nohup 并行启动，日志写到 `logs/v2_lora_{type}_r16.log`
- 支持 `--dry_run` 快速验证
- wait 所有进程后报告结果

```bash
# 用法
bash scripts/launch_v2_lora_training.sh           # 完整训练
bash scripts/launch_v2_lora_training.sh --dry_run  # 2-step 验证
```

## 5. pi0_libero checkpoint 状态

已下载完成，路径 `/root/autodl-tmp/checkpoints/pi0_libero/`，包含 `model.safetensors`、`config.json` 等文件。

---
