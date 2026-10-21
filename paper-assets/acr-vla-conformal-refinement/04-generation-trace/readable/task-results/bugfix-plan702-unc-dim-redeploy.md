# bugfix plan702 unc dim redeploy

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_bugfix_plan702-unc-dim-redeploy_20260520T142039_result.json`
- **Structured JSON:** [`77f0847c4df568d5c998.json`](../../sessions/77/77f0847c4df568d5c998.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部注册完成，状态 RUNNING。最终总结：

---

## 产出

### 1. Bug 分析

**原始 bug**：`evaluate.py:466` — `crm_k1_accg` 分支创建了 `MultiScaleCRM`，但代码随后 fall-through 到 `ConformalRefinementModule` 初始化处引用 `unc_dim`。该变量只在 `crm_obs_only/crm_scalar/crm_perdof` 分支被赋值，`crm_k1_accg` 未命中任何赋值分支 → `UnboundLocalError`。

**其他 mode 的 unc_dim 值**：
- `crm_obs_only` / `adaptive_k` → `0`
- `crm_scalar` → `3`
- `crm_perdof` / `acr_vla` → `40` (CORRECTION_DIM × H_EFF + H_EFF + H_EFF)

**修复**（已在 22:20:41 生效）：将 `crm_k1_accg` 的 `MultiScaleCRM` 初始化放进 `if` 分支，`unc_dim` + `ConformalRefinementModule` 放进 `else` 分支，两者互斥。crm_k1_accg 不需要 `unc_dim`，因为 `MultiScaleCRM` 接口不使用 uncertainty 输入。

### 2. 修改内容

代码已在我介入前被修复（22:20:41）。修复为 if/else 结构隔离，最小化改动。

### 3. Dry-run 结果

**成功** — cuda:4 上 n_rollouts=1 运行，首个 task 完成输出：
```
[pick_up_the_alphabet_soup_and_place_it_in_the_basket] success rate: 0.0% (0/1)
```
无 unc_dim 错误，无 crash。

### 4. 3 个实验部署

| exp_id | seed | GPU | PID | tmux session |
|--------|------|-----|-----|-------------|
| eval-crm-k1-object-seed42-plan702-r2 | 42 | cuda:0 | 395029 | eval-crm-k1-object-seed42-plan702-r2 |
| eval-crm-k1-object-seed43-plan702-r2 | 43 | cuda:1 | 395670 | eval-crm-k1-object-seed43-plan702-r2 |
| eval-crm-k1-object-seed44-plan702-r2 | 44 | cuda:5 | 395961 | eval-crm-k1-object-seed44-plan702-r2 |

**注意**：seed44 部署在 cuda:5（非原计划 cuda:4），因为 cuda:4 被 `eval-random-selection-object-seed44` 占用（10857 MiB, 79%）。cuda:5 此时已空闲。

---
