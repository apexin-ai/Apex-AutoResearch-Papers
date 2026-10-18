# code mask ratio annealing prep

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mask_ratio_annealing_prep_20260516T063114_result.json`
- **Structured JSON:** [`4abd7686b5f6ae533978.json`](../../sessions/4a/4abd7686b5f6ae533978.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 完全成功。结果总结：

**Schedule 验证**：
| step | k_ratio |
|------|---------|
| 0-5000 | 0.9000 (warmup, 保持不变) |
| 10000 | 0.8000 |
| 15000 | 0.7000 |
| 20000 | 0.6000 |
| 25000-30000 | 0.5000 (目标比例) |

**Dry-run (10 steps on cuda:0)**：
- 所有 10 步 k_ratio = 0.9000（正确——都在 warmup 阶段 <5000）
- 训练正常：loss 在合理范围波动，无 crash
- gradient isolation 逻辑保持不变

**产出文件**：
1. `configs/imm_anchor_v8c_annealing.yaml` — 新 config，基于 v8 + annealing schedule
2. `train.py` — 新增 `compute_k_ratio()` 函数 + 训练循环中每步更新 `model.k_ratio` + wandb 记录 k_ratio

**启动正式训练时的命令**（v8b FAIL 后执行）：
```bash
CUDA_VISIBLE_DEVICES=0 python train.py --config configs/imm_anchor_v8c_annealing.yaml --wandb_run v8c_annealing
```

---
