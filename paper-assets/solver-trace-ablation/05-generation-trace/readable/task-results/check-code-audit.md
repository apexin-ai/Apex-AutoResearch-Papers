# check code audit

**solver trace ablation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_code_audit_20260513T090051_result.json`
- **Structured JSON:** [`906ba1304a8b615209ef.json`](../../sessions/90/906ba1304a8b615209ef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 验证结果

### Issue 1 [Critical] filters.py LC 方向 — ✅ 已修

- `PGPFStaticFilter.filter()` 第 91 行：
  ```python
  if lc_vals[i] >= lc_thresh and sn_vals[i] >= sn_thresh and q_vals[i] <= q_thresh:
  ```
  LC 用 `>=`（保留高 conformity），quality 用 `<=`（保留低 PPL），方向正确。

- `LexicalOnlyFilter.filter()` 第 114 行：
  ```python
  passing = [i for i in range(n) if lc_vals[i] >= thresh]
  ```
  同样 `>=`，正确。

### Issue 2 [Warning] metrics.py PPL padding — ✅ 已修

第 103-104 行：
```python
labels = input_ids.clone()
labels[attention_mask == 0] = -100
```
padding token 被排除在 loss 计算之外。

### Issue 3 [Warning] config.py 默认值 — ✅ 已修

| 参数 | 期望值 | 实际值 (行号) | 状态 |
|------|--------|--------------|------|
| `model_name` | `"Qwen/Qwen2.5-1.5B"` | `"Qwen/Qwen2.5-1.5B"` (L42) | ✅ |
| `num_generations` | `3` | `3` (L44) | ✅ |
| `real_data_mix_ratio` | `0.5` | `0.5` (L48) | ✅ |

### Issue 4 [Warning] recursive_loop.py — ✅ 已修

**`_generate_synthetic()` 检查：**
- **Batch generation**: 有，`batch_size=8`，逐 batch 处理 prompts
- **attention_mask**: 传了，`model.generate(input_ids, attention_mask=attention_mask, ...)`
- **进度日志**: 有，L260-261 每 ~100 样本打印 `generated {len(synthetic)}/{n_total}`
- **try/except 容错**: 有，batch 失败后 fallback 到逐样本生成，再失败则 skip

**SFTConfig 参数**: L167 `max_length=cfg.training.max_seq_length` — 参数名为 `max_length`，正确。

**real_data_mix_ratio 混合逻辑** (L111-118):
```
if real_data_mix_ratio > 0:
    n_real = int(len(filtered) * ratio / (1 - ratio))
    current_train_data = filtered + real_subset
else:
    current_train_data = filtered
```
当 ratio=0.5 时，n_real = len(filtered)，即 50/50 混合，逻辑正确。

---

**总结：4 个 issue 全部已修复，代码状态正确。**

---
