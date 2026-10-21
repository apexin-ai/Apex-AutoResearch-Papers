# exp bce isocompute v2 s42

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_bce_isocompute_v2_s42_20260515T200230_result.json`
- **Structured JSON:** [`84667562622dd0b68647.json`](../../sessions/84/84667562622dd0b68647.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练正常运行，GPU:0 占用 90.5GB。

---

## 执行报告

### (1) reg_weight 变更

| 参数 | 原值 | 新值 | 说明 |
|------|------|------|------|
| `sparsity_reg_weight` | 0.1 | **2.0** | 20x |
| reg mask 实现 | `(pred_logits > 0).float()` under `torch.no_grad()` | **STE**: `hard_mask - soft_mask.detach() + soft_mask` | 原实现无梯度 |

**关键发现**：原代码中 `SparsityRegularizer` 的 mask 在 `torch.no_grad()` 下用硬阈值计算，reg 对参数梯度为零。单纯调大 weight 无效。修复为 STE (Straight-Through Estimator)：forward 用 hard mask（准确反映真实 sparsity），backward 走 sigmoid 梯度（可微分）。

### (2) Dry-run Sparsity 趋势

| Step | Sparsity | Reg | BCE |
|------|----------|------|------|
| 25 | 0.499 | 0.0172 | 0.6892 |
| 50 | 0.500 | 0.0163 | 0.6759 |
| 100 | 0.502 | 0.0128 | 0.6687 |
| 200 | **0.499** | 0.0020 | 0.6671 |

全程 [0.499, 0.502]，满足 0.50±0.005，匹配 KL 的 0.498。

### (3) 正式训练

- **exp_id**: `bce_isocompute_v2_s42`
- **PID**: 129187 (python) / tmux session: `bce_isocompute_v2_s42`
- **GPU**: cuda:0 @ westd-34887
- **1000 步**, save_every=250, log_every=100
- **预计完成时间**: ~17.5 分钟 (1.05s/step × 1000)
- **Log**: `~/runs/distill_sparse_swiglu/bce_isocompute_v2_s42.log`

### (4) Registry

- 实验 `bce_isocompute_v2_s42` → status=RUNNING, plan_id=plan_003
- hypothesis: "BCE 在 iso-compute (1000 steps) + iso-sparsity (STE reg_weight=2.0 使 sparsity 收敛到 ~0.50) 下是否能缩小与 KL 的 PPL 差距？消除 compute 和 sparsity 两个 confound。"
- spec 包含完整 command、server、model、seed、reg_weight、reg_fix 说明

---
