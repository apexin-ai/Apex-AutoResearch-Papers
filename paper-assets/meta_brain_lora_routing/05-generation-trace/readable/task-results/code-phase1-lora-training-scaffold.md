# code phase1 lora training scaffold

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_phase1_lora_training_scaffold_20260515T160546_result.json`
- **Structured JSON:** [`c8d10b1924e5b74407ae.json`](../../sessions/c8/c8d10b1924e5b74407ae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Phase 1 代码完成，dry-run 验证通过。

**总结：**

| 项目 | 状态 |
|------|------|
| `train_lora_expert.py` | 部署到 westd-34142，dry-run 通过 |
| `data_loader.py` | 部署到 westd-34142，dry-run 通过 |
| LoRA 注入 | 3,686,400 trainable / 3.5B total (0.1052%) |
| 目标模块 | PaliGemma Q/K/V/O × 18层 (排除 Action Expert) |
| Forward pass | loss=7.30 (step 0), loss=10.45 (step 1) |
| Backward pass | grad_norm=2.38 / 3.29，梯度正常回传 |
| 修复的 bug | `obs_to_device()` 从 `jax.tree.map` 改为显式逐字段 `.to(device)` |

**下一步可启动正式训练：**
```bash
# 4 GPU 并行，每 GPU 训练一个 perturbation type 的 LoRA adapter
python phase1/train_lora_expert.py --perturbation_type visual   --gpu_id 0 &
python phase1/train_lora_expert.py --perturbation_type spatial  --gpu_id 1 &
python phase1/train_lora_expert.py --perturbation_type physical --gpu_id 2 &
python phase1/train_lora_expert.py --perturbation_type universal --gpu_id 3 &
```

---
