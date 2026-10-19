# analysis oracle upper bound feasibility

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_oracle-upper-bound-feasibility_20260518T072347_result.json`
- **Structured JSON:** [`bfd3734b9023d06471e7.json`](../../sessions/bf/bfd3734b9023d06471e7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

信息足够了。以下是完整分析：

---

## 方案 1（从已有数据推算）：**不可行**

**原因**：
- `select_action_crm` (evaluate.py ~L161-196) 在每个 timestep 生成 K=10 candidates，但只通过 argmin 选出 1 个执行 `env.step()`，其余 9 个**从未 rollout**
- JSON 输出只记录 per-task 聚合成功率（successes/total），无 per-candidate、per-step、per-rollout 的信息
- 没有任何数据能回溯其余 9 个 candidate 的结果

---

## 方案 2（新代码）：可行，但需明确 Oracle 的定义

### 核心问题：Oracle 有两种语义

**语义 A：Step-level Oracle（真正的天花板）**
- 每个 timestep 的 K=10 candidates，Oracle 选出"能最终导致成功"的那个
- 这是一个 **K^T 指数级搜索树** 问题（K=10, T≈300 steps → 10^300 条路径）
- **完全不可行**

**语义 B：Episode-level K-retry Oracle（实用近似）**
- 对同一个 init_state，独立跑 K=10 个完整 episode（每次用 K=1 VLA sample）
- 只要 10 次中有 1 次成功 → Oracle 成功
- 这衡量的是"K=10 次独立尝试的天花板"，是 argmin selection 的合理 upper bound

### 方案 2A：解析近似（零成本，立即可得）

已有数据：VLA-only K=1 overall SR = 12%。假设独立性，Oracle K=10 = `1 - (1-p)^10`。

Per-task 推算（基于 vla_only.json seed=42）：

| Task | K=1 SR | Oracle K=10 (解析) |
|------|--------|-------------------|
| alphabet_soup | 0% | 0% |
| cream_cheese | 10% | 65% |
| salad_dressing | 20% | 89% |
| bbq_sauce | 20% | 89% |
| ketchup | 0% | 0% |
| tomato_sauce | 10% | 65% |
| butter | 0% | 0% |
| milk | 10% | 65% |
| chocolate_pudding | 20% | 89% |
| orange_juice | 30% | 97% |
| **Average** | **12%** | **~56%** |

**局限**：
- 独立性假设可能不成立（同一 obs 的 K 个 VLA samples 有相关性，实际天花板低于 56%）
- p=0 的 3 个 task（alphabet_soup, ketchup, butter）可能只是样本量太小（10 rollouts），真实 p>0
- 10 个 rollouts 使用不同 init_states，per-init-state 的 p 可能差异很大

### 方案 2B：实证 K-retry 实验（推荐）

**改动思路**：
```python
# 新模式 --mode oracle_k_retry
# 对每个 (task, init_state)：
for attempt in range(K):  # K=10
    success, steps = rollout_single(env, same_init_state, 
                                     action_fn_k1, max_steps)
    if success:
        oracle_success = True; break
```

**代码改动量**：~40-60 行
- 新增一个 `evaluate_oracle()` 函数或在 `evaluate()` 中加 `--mode oracle` 分支
- 内层循环：对同一 init_state 跑 K 次 K=1 VLA rollout
- 记录 per-init-state 的 oracle success

**计算成本**：
- 现有 VLA-only K=1：10 tasks × 10 rollouts = 100 episodes ≈ **1.7 小时**（birth→modify 时间差）
- Oracle K=10：10 tasks × 10 init_states × 10 attempts = 1000 episodes ≈ **~17 小时**
- 可以减少：5 rollouts × 10 attempts = 500 episodes ≈ **~8.5 小时**

**LIBERO 环境支持**：
- `get_sim_state()` → `env.sim.get_state().flatten()` ✓
- `set_state(mujoco_state)` → `env.sim.set_state_from_flattened()` ✓
- 可以在每个 init_state 上 reset 后多次独立 rollout，无需 fork

---

## 推荐

**先做 2A（解析近似），再决定是否做 2B。**

理由：
1. 解析近似零成本，马上能给出 Oracle 天花板的粗略范围（~56%），对比当前 CRM 最佳 ~22%，差距巨大 → 说明 selection 策略有很大改进空间
2. 如果论文需要精确 Oracle 数字，再跑 2B（~8-17h GPU 时间）
3. 2B 的代码改动不大（~50 行），主要成本在计算时间
4. p=0 的 task 建议用更多 seed 跑 VLA-only 确认是否真正为 0（如果 p>0 但很小，Oracle K=10 会显著提升）

---
