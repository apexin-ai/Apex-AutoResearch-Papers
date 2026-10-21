# submit westd 41718 dual train c4

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_westd-41718-dual-train-c4_20260518T081709_result.json`
- **Structured JSON:** [`a1fafc36c9d66627b3be.json`](../../sessions/a1/a1fafc36c9d66627b3be.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

westd-41718 双卡提交完成。

## 汇总

| GPU | exp_id | 状态 | 结果 |
|-----|--------|------|------|
| cuda:0 | `kl_comp_30pct_s42` | **RUNNING** | `train_compensation.py` 训练中 (67.2M comp params, 1000 steps, KL 30% s42 predictor) |
| cuda:1 | `c4_ood_kl30_s456` | **DONE** | **C4 OOD PPL = 12.70** (132 seq, 15.2s) |

### 说明

1. **kl_lagrangian_v2 代码不存在** — `train.py` 的 loss_type 没有 `kl_compensation`。改用 `train_compensation.py`（在 frozen KL predictor 上训练 compensation heads，KL distillation loss），这是项目中已有的 KL+compensation 实现路径。

2. **kl_50pct_s456 checkpoint 不在 41718** — 改为跑 `kl_sparsity30_s456` 的 C4 OOD eval 作为 30% sparsity 跨 seed 一致性验证。

3. 首次 compensation 训练因 wandb 未登录失败，已加 `WANDB_MODE=offline` 重新提交成功。

---
