# verify grpo cka only 20 checkpoint

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_grpo_cka_only_20_checkpoint_20260521T211842_result.json`
- **Structured JSON:** [`8e8ada7fb7cfa47dec50.json`](../../sessions/8e/8e8ada7fb7cfa47dec50.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有核实完成。汇总结果：

---

## grpo_cka_only_20 核实结论

### 是否是 GRPO 权重？**是，但 GRPO 几乎没有学到东西。**

**证据链：**

| 证据 | 内容 |
|------|------|
| trainer_state.json | 100 步 GRPO 完成，有 reward/KL/entropy/clip_ratio 完整日志 |
| completions/ | 10 个 parquet 文件（step 10→100），跨 ~10 小时 |
| README.md | TRL 自动生成，tags 含 `grpo`，有 wandb run `li451oi4` |
| **md5sum 对比** | GRPO checkpoint-100: `8846023163adb48d83d14f97ee889f09` &lt;br> SFT: `fb52fdac72388a0420bff618f319f6aa` &lt;br> **不同 → 权重确实被更新了** |

### 为什么 GRPO ≈ SFT（29.2% vs 29.0%）？

GRPO 训练几乎没有移动模型：
- **KL divergence**: ~0.001（极小）
- **clip_ratio**: 全程 0.0
- **学习率**: 9.1e-07 → 1e-08（本身就极小）
- **reward**: 0.253 → 0.344（微小提升）

**结论：差距 0.2pp 反映的是 GRPO 确实没学到什么，不是模型混淆。**

### 有一个风险点

`grpo_cka_only_20/` **根目录没有 model.safetensors**（仅在 `checkpoint-100/` 子目录有）。eval 脚本 `_load_state_dict` 直接对 model_path 做 `os.listdir` 找 `.safetensors`——根目录没有该文件时会报错。推测 eval 时根目录有 model.safetensors（TRL 训练结束时会写到 output_dir），后来被删除（可能是磁盘清理）。**无法 100% 验证 eval 当时加载的是 GRPO 还是 SFT 权重**，但基于 TRL 默认行为（最终模型写 output_dir 根目录）和 md5 差异，大概率 eval 加载了正确的 GRPO 权重。

模型位置（westb-23072）：`/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20/checkpoint-100/`

---

## sft_alpha4_20 确认

在 **westd-29022** 上存在且完整：
- 路径：`/root/autodl-tmp/recovery_aware_struct_prune/sft_alpha4_20/`
- model.safetensors: 12GB（May 22 02:52）
- trainer_state.json: 28K（有训练记录）
- checkpoint-936/ 子目录存在
- 可直接用于 eval_gsm8k_sft_alpha4_20

---
