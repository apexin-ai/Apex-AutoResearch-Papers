# ops kill serve policy and dryrun

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill_serve_policy_and_dryrun_20260522T231905_result.json`
- **Structured JSON:** [`35dd0f887da625c0ad63.json`](../../sessions/35/35dd0f887da625c0ad63.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程已退出，GPU 完全释放。

## 汇报

### Part 1: serve_policy kill
- `kill 430540` 成功，GPU 1 显存从 73.5GB 释放至 0MiB

### Part 2: Dry-run 结果

遇到两个 bug 并修复后，5 步训练成功完成：

**修复的 Bug：**
1. **quantile norm stats 缺失** — Pi0.5 默认 `use_quantile_norm=True`，但 norm_stats.json 中 q01/q99 为 null。从数据集计算了真实 q01/q99 并更新了 `assets/baseline_spatial_bowl/safelibero_spatial/norm_stats.json`
2. **LoRA dtype 不匹配** — `lora_utils.py` 的 LoRA 参数以 float32 创建，导致 `next(q_proj.parameters()).dtype` 返回 float32，破坏了模型的 bfloat16 dtype 检测链（`gemma_pytorch.py:334`），使 embeddings 未被 cast 到 bfloat16，最终在 `F.linear` 中 float32 input × bfloat16 weight 报错。修复：LoRA 参数使用 base weight 的 dtype 创建，forward 中显式 `.float()` 保证数值精度

**Dry-run 输出：**
- **Trainable params**: 658,948（SDF decoder + EE extractor；LoRA 在 Phase 1 冻结）
- **LoRA params**: 0（Phase 1 冻结，Phase 2 在 step 5000 解冻）
- **每步 loss**:
  | Step | Total Loss | LR |
  |------|-----------|-----|
  | 1 | 0.1296 | 1.25e-05 |
  | 2 | 0.1152 | 2.50e-05 |
  | 3 | 0.1524 | 2.17e-05 |
  | 4 | 0.1423 | 1.38e-05 |
  | 5 | 0.1254 | 5.80e-06 |
- **无 NaN**
- **显存**: GPU 0 峰值 ~19.1GB / 96GB（单卡充裕）
- **总用时**: 28s（首步 14.5s 含编译，后续 ~1-5s/step）
- 注：tqdm 输出仅显示 total loss，aux loss 分项（action_loss, sdf_loss, ee_loss）通过 wandb 记录，dry-run 中 wandb disabled 故未显示

---
