# code audit bugs

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_audit-bugs_20260513T040655_result.json`
- **Structured JSON:** [`3ccf3c4b0db88ab96a34.json`](../../sessions/3c/3ccf3c4b0db88ab96a34.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个修复均已验证。报告如下：

---

## 审查报告

### 1. Augmentation bug (`train_crm.py:269`)
**确认 bug 存在，已修复。**
- `aug_expert = synthetic_augmentation(...)` 计算了增强数据，但 `aug_loss` 的 target 仍用原始 `expert_flat[:n_aug]`，导致 augmentation 完全无效
- 修复：`loss_fn(aug_refined, expert_flat[:n_aug])` → `loss_fn(aug_refined, aug_expert)`

### 2. crm_scalar unc_dim (`evaluate.py:208`)
**确认 bug 存在，已修复。**
- 原代码 `unc_dim = H_EFF + H_EFF = 10`，缺少 log-volume 分量
- 修复：`H_EFF + H_EFF` → `3 * H_EFF = 15`（scalar std H_EFF=5 + conformal radius H_EFF=5 + log-volume H_EFF=5）

### 3. verify_pipeline.py
**存在。** 文件大小 11762 bytes，最后修改 May 13 11:52。

### 4. ACI 符号
**正确。** `self.alpha = self.alpha + self.gamma * (self.alpha_target - err)`

### 5. 当前训练状态
**已失败。** Phase B（precompute + train）均因 `--horizon 5` 无效参数而退出。GPU 空闲（0% 利用率，0 MiB 显存占用）。启动脚本传了 `train_crm.py` 不支持的 `--horizon` 参数。

---
