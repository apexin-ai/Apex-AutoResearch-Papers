# research p3 mode equivalence

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_p3-mode-equivalence_20260515T033729_result.json`
- **Structured JSON:** [`dc018685fd4ff6d97d9e.json`](../../sessions/dc/dc018685fd4ff6d97d9e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

代码已全部看完，结论如下：

---

## `acr_vla` vs `crm_perdof`：**完全等价**

两者在代码中走 **100% 相同的路径**，没有任何分支区分它们。具体证据：

### 1. CRM 初始化（evaluate 函数，~L264-272）
```python
if args.mode in ("crm_scalar", "crm_perdof", "acr_vla", "crm_obs_only"):
    if args.mode == "crm_obs_only":
        unc_dim = 0
    elif args.mode == "crm_scalar":
        unc_dim = 3
    else:  # crm_perdof or acr_vla  ← 共用同一分支
        unc_dim = CORRECTION_DIM * H_EFF + H_EFF + H_EFF  # 40
```
`acr_vla` 和 `crm_perdof` 落入同一个 `else` 分支，`unc_dim = 40`。

### 2. 动作选择（rollout 循环，~L320）
```python
else:  # crm_scalar, crm_perdof, acr_vla, crm_obs_only 全部走这里
    action_fn = lambda obs: select_action_crm(
        wrapper, obs, task_desc, args.K, cgs, crm, device, args.mode
    )
```

### 3. select_action_crm 函数（L160-198）
函数内部只有一个 mode 检查：
```python
if mode == "crm_scalar":
    uf = _to_scalar_uf(uf)      # 只对 crm_scalar 生效
```
和：
```python
uf_input = None if mode == "crm_obs_only" else uf   # 只对 crm_obs_only 生效
```

对 `crm_perdof` 和 `acr_vla`，**不触发任何特殊分支**，完整传入 40 维 per-DOF uncertainty feature。

### 各 mode 总结

| Mode | unc_dim | uncertainty feature | CRM 输入 |
|------|---------|-------------------|----------|
| `crm_perdof` | 40 | 完整 per-DOF | base_action + uf + obs_feat |
| `acr_vla` | 40 | 完整 per-DOF | base_action + uf + obs_feat |
| `crm_scalar` | 3 | `_to_scalar_uf()` 压缩为 3 维 | base_action + scalar_uf + obs_feat |
| `crm_obs_only` | 0 | None（不传入） | base_action + None + obs_feat |

### 结论
- **`acr_vla` 是 `crm_perdof` 的纯别名**，代码路径、feature set、correction 逻辑完全一致
- bjb1-18228 的 spatial eval（`--mode acr_vla`）和 bjb1-32546 的 object eval（`--mode crm_perdof`）**结果直接可比**，前提是使用相同的 checkpoint
- `crm_scalar` 和 `crm_obs_only` 各自走独立分支，使用不同维度的 uncertainty 输入，checkpoint 不可互换（`unc_dim` 不匹配会导致加载失败）

---
