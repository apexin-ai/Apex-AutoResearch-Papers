# code check adaptive crm compat

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_check-adaptive-crm-compat_20260522T191036_result.json`
- **Structured JSON:** [`9eb9f41efcc458bd4b9c.json`](../../sessions/9e/9eb9f41efcc458bd4b9c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已获取完整信息。以下是分析结果：

---

## 报告

### 1. `adaptive_conformal_crm` 模式完整逻辑流程

**函数**: `select_action_conformal_crm()` (evaluate.py:451-508)

每一步执行流程：
1. 生成 **K=2** 个 VLA 样本
2. 提取两个样本的 6D pose (各 30 维 = H_eff×6)
3. 计算 uncertainty = `||a1 - a2||₂`（两个样本的 L2 距离）
4. 选取离 centroid 更近的样本作为 base_action
5. **判定 gate**: `triggered = uncertainty > conformal_threshold`
   - **uncertain** (triggered=True): 调用 `crm(base_action, None, obs_features)` 做 CRM 修正
   - **confident** (triggered=False): 直接用 selected_pose，跳过 CRM

**CRM 加载**: unc_dim=0，CRM 以 `(base_action, None, obs_features)` 调用 — uncertainty_features 传 None。

### 2. 是否兼容 obs_only (unc_dim=0)

**完全兼容。**

原因：
- CRM 加载时 `adaptive_conformal_crm` 走的分支和 `crm_obs_only` 完全相同：`unc_dim = 0` (evaluate.py:580-581)
- `select_action_conformal_crm()` 调用 CRM 时传 `uncertainty_features=None` (evaluate.py:498)
- `ConformalRefinementModule.forward()` 处理 `uncertainty_features=None` 的逻辑已实现 (crm.py:47-50)：当 None 时直接 cat `[base_action, obs_features]`，input_dim = 30+960 = 990，与 unc_dim=0 的 checkpoint 匹配
- **uncertainty 的计算完全基于 K=2 样本的 L2 距离**（外部计算），不依赖 CRM 的 uncertainty head 输出

### 3. 结论

**无需修复。** `adaptive_conformal_crm` 模式的 adaptive gate 基于 K=2 样本 disagreement（L2 距离），不使用 CRM 内部的 uncertainty 输出。CRM 以 obs_only 模式 (unc_dim=0) 加载，checkpoint 完全匹配。代码路径已正确实现，可以直接用于评估。

---
