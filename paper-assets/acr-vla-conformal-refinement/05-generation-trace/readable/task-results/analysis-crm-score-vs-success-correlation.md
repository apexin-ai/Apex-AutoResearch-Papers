# analysis crm score vs success correlation

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_crm-score-vs-success-correlation_20260518T070335_result.json`
- **Structured JSON:** [`e4ee70ea2432a266844c.json`](../../sessions/e4/e4ee70ea2432a266844c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论：Per-candidate CRM scores 不存在于已有数据中

### 原因：CRM 是 refinement 模块，不是 scoring/ranking 模块

`select_action_crm`（evaluate.py:161）的流程：

1. K=10 VLA samples → CGS 计算 **set-level** 不确定性特征（40D: 30个per-DOF std + 5个conformal radius + 5个log volume）—— 描述整体分布，不是 per-candidate 分数
2. Argmin 选择离 mean 最近的 candidate（Euclidean distance）作为 base action
3. CRM 只处理 **这一个** base action → 输出 refined action
4. **CRM 从未对 K 个 candidates 逐一评分**

### 已有数据内容

- **JSON**：仅 task-level success rate（success_rate/successes/total），无 per-step 信息
- **Log**：仅 rollout-level success count，无 per-step CRM scores
- **结论：无法从已有数据提取 CRM ranking vs success correlation**

---

## 修改方案：两种路径

### 方案 A：用 CRM correction norm 作为 proxy score（推荐，改动小）

思路：对每个 candidate 单独过 CRM，用 `||CRM output - input||`（correction magnitude）作为 "nonconformity score"，越小 = CRM 认为越好。

修改 `select_action_crm`（约 25 行改动）：

```python
# 在 select_action_crm 中，argmin selection 后、CRM refinement 前，加入：

# Score all K candidates with CRM
per_candidate_scores = []
for i in range(K):
    cand_i = k_pose_flat[i].unsqueeze(0).to(device)  # (1, 30)
    with torch.no_grad():
        refined_i = crm(cand_i, uf_input, obs_feat)
    correction_norm = (refined_i - cand_i).norm().item()
    per_candidate_scores.append(correction_norm)

# Log: scores + selected index + euclidean distances
step_log = {
    "crm_scores": per_candidate_scores,        # 越小越好
    "euclidean_distances": distances.tolist(),   # argmin selection basis
    "selected_idx": best_idx.item(),
}
```

还需要在 rollout 级别收集 per-step logs，并在 JSON 中加入 `per_step_data` 字段。

### 方案 B：直接用 CRM score 做 candidate selection（更彻底）

用 CRM correction norm 替代 Euclidean distance 做 argmin：

```python
best_idx = torch.tensor(per_candidate_scores).argmin()
```

这本身就是一个有意义的消融实验（CRM-based selection vs Euclidean argmin）。

---

### 成本估计

- **代码改动**：evaluate.py 约 25-30 行新增
- **计算开销**：每步从 1 次 CRM forward 变为 K+1=11 次（CRM 很小，327K params，额外开销可忽略）
- **需要重跑实验**：是。至少跑 1 个 benchmark（object）× 1 个 seed，约 2-3 小时
- **分析脚本**：额外写一个分析脚本，按 CRM rank 分组计算 rollout success rate

要开始实现吗？

---
