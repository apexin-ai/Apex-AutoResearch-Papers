# code v8b twostage prep

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_v8b-twostage-prep_20260516T001056_result.json`
- **Structured JSON:** [`76b57dfb00f58f9154ac.json`](../../sessions/76/76b57dfb00f58f9154ac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**ALL CHECKS PASSED.** 干运行验证结果：

| 检查项 | 结果 |
|--------|------|
| a) LoRA requires_grad=False | **PASS** — 0 个 LoRA 参数可训练 |
| b) ACIS requires_grad=True | **PASS** — 10 个参数, 3,460,801 元素 |
| c) margin_loss → ACIS gradient | **PASS** — 3 步均有梯度 |
| d) No LoRA gradient | **PASS** — 冻结后无梯度泄漏 |
| e) action_loss=0 (skip VLM forward) | **PASS** — VLM forward 被跳过 |

3 步 dry-run 中 margin_loss 从 0.2988 降到 0.2939，梯度范数正常（4.0 → 9.2），ACIS 在学习。

---

### 改动总结

**1. `imm/smolvla_wrapper.py`** — 新增 `forward_acis_only()` 方法（line 298）
- 在 `torch.no_grad()` 下运行 backbone（SigLIP + embed_suffix），跳过 VLM forward
- 只计算 ACIS scores + margin_loss，效率远高于完整 forward

**2. `train.py`** — 新增 `setup_twostage()` 函数（line 329）+ 修改 `main()`
- `setup_twostage`: 加载 baseline checkpoint → 冻结所有非 ACIS 参数
- `main()`: 检测 `twostage` config → 覆盖 LR/warmup/total_steps → 调用 `forward_acis_only`
- Stage 1 完成后保存 `stage1_done` checkpoint
- 所有改动用 `is_twostage` flag 控制，向后兼容 v8

**3. `configs/imm_anchor_v8b_twostage.yaml`** — 新增 `baseline_checkpoint` 字段
- 指向 `checkpoints/baseline/step_029999/checkpoint.pt`

**启动正式训练命令**（未执行）：
```bash
CUDA_VISIBLE_DEVICES=1 python train.py --config configs/imm_anchor_v8b_twostage.yaml --gpu 0 --wandb_run mvp_imm_anchor_v8b
```

---
