# ops fix plan017 subsample config

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix-plan017-subsample-config_20260515T090437_result.json`
- **Structured JSON:** [`6b76f3c008690976402d.json`](../../sessions/6b/6b76f3c008690976402d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修正完成。总结：

### 修正前 vs 修正后

| | 修正前 | 修正后 |
|---|---|---|
| `--gate_subsample_max_dt` | 未设置（默认 0） | **1** |
| 实际 subsample 行为 | `subsample_eff_dt=2.0` → **ON** | `subsample_eff_dt=1.0` → **OFF** |

### 代码逻辑确认

`models.py:216-220`:
- `gate_subsample_max_dt=0` → `0 > 0` False → fallback 到 `effective_max_dt`（由 `gate_fixed_dt=2` 得到 2.0）→ subsample ON
- `gate_subsample_max_dt=1` → `1 > 0` True → `subsample_eff_dt=1.0` → `tools.subsample_variable_dt` 中 `effective_max_dt <= 1` 直接返回全 dt=1 → subsample OFF

`tools.py:778-780`:
```python
if effective_max_dt <= 1:
    dt_labels = torch.ones(B, T, dtype=torch.long, device=device)
    return data, dt_labels
```

### 与 008a 对比

008a（`exp_008a_fixed_dt2_no_subsample`）无 config.yaml 或提交脚本留存，无法直接对比参数值。但从实验名"no_subsample"判断，008a 的 subsample 应为 OFF。修正后 017 的 subsample 行为与 008a 一致（全 dt=1），唯一区别是 `critic_dt_emb_detach`（008a=True 冻结，017=False 训练）。

---
