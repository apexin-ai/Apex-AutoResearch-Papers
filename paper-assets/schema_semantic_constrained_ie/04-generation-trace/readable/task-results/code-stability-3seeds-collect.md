# code stability 3seeds collect

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_stability_3seeds_collect_20260517T050223_result.json`
- **Structured JSON:** [`2e5d31b4e95048582376.json`](../../sessions/2e/2e5d31b4e95048582376.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个文件都完整（各 551 行），且日志已包含完整汇总。结果：

## Stability 3-Seeds 结果

| Seed | ET% | RV% | DR% | CF% | E_F1 | R_F1 |
|------|-----|-----|-----|-----|------|------|
| 123 | 0.00 | 0.00 | 0.93 | 9.90 | 30.98 | 8.36 |
| 456 | 0.00 | 0.00 | 0.93 | 9.90 | 30.98 | 8.36 |
| 789 | 0.00 | 0.00 | 0.93 | 9.90 | 30.98 | 8.36 |

**跨 seed 统计：**
- DR 范围：0（三个 seed 完全一致 0.93%）
- DR 标准差：0.0000
- 所有指标标准差均为 0

**结论**：greedy decoding + full_s1 模式下，Qwen3-8B 输出完全确定性（MD5 不同说明 JSON 格式/字段顺序有微小差异，但 violation 指标和 F1 完全一致）。DR=0.93% 跨 seed 完全稳定，与 baseline (seed=42) 一致。

---
