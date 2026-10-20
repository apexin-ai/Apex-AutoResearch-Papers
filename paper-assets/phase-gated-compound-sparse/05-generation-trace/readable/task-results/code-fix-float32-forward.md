# code fix float32 forward

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-float32-forward_20260514T010056_result.json`
- **Structured JSON:** [`0810f81913b8c87654c3.json`](../../sessions/08/0810f81913b8c87654c3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

本地文件也已同步。产出汇总：

---

## 代码修改

**文件 1: `pacs/profiling/interaction_index.py` (line 120-126)**

`_HeadMaskHook._make_hook` 中的 head masking 乘法：
- 旧：`reshaped = reshaped * head_mask_expanded` — 当 `reshaped` 含 inf（KV eviction 导致）且 mask=0 时，`inf*0=NaN`（IEEE 754）
- 新：`torch.where(mask.bool(), reshaped, zeros)` — 直接选择，避免乘法，彻底消除 NaN

**文件 2: `pacs/utils/metrics.py` (line 30-32)**

`compute_perplexity` 中的 cross-entropy：
- 旧：`F.cross_entropy(shift_logits, ...)` — fp16 logits 可能导致 softmax 溢出
- 新：`F.cross_entropy(shift_logits.float(), ...)` — 强制 float32 计算

## 测试结果

CPU mini 测试验证：
- `inf * 0`（旧行为）→ NaN
- `torch.where` 修复后 → 0.0，无 NaN
- 未被 mask 的 head 保留原值（包括 inf）

## Legacy s02/s03 影响检查

| 实验 | Phase | Scope 一致? | 证据 |
|------|-------|------------|------|
| v4b (s02, 0.2) | high | **不一致** | both=63.41 < kv=104.42; II_agg=-35.92 vs II_reported=21.29 |
| v4b (s02, 0.2) | mid | **不一致** | both=170.47 < kv=324.16; II_agg=-137.05 vs II_reported=21.87 |
| v4b (s02, 0.2) | low | 一致 | kv≈dense，无 eviction 影响 |
| v4c (s03, 0.3) | high | **不一致** | both=139.81 < kv=408.98; II_agg=-235.31 vs II_reported=-224.51 |
| v4c (s03, 0.3) | mid | **不一致** | both=358.84 < kv=604.37; II_agg=-219.47 vs II_reported=53.99 |
| v4c (s03, 0.3) | low | 一致 | kv 相对温和 |

所有 high/mid phase 都有 scope 不一致，`both < kv` 是 NaN 排除的特征。

## 修复后重跑建议

- **v4b (s02)** 和 **v4c (s03)** 的 high_sparsity 和 mid_sparsity phase 结果不可信，需要重跑
- **当前在跑的 s025/s035/v4d**（GPU 0/1/2）也使用了旧代码，完成后需要用修复后的代码重跑
- low_sparsity phase 不受影响（kv eviction 不产生极端值）
- 建议等当前 batch 完成后，全部用修复后的代码重跑所有 sparsity ≥ 0.2 的实验

---
