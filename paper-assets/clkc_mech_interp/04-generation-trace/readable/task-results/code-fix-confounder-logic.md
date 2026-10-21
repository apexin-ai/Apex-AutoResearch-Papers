# code fix confounder logic

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-confounder-logic_20260522T023744_result.json`
- **Structured JSON:** [`c3fa5f95694d46bce463.json`](../../sessions/c3/c3fa5f95694d46bce463.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。修改总结：

- **代码变更**：`is_confounder = abs(delta_pp) >= 5 or p_value <= 0.05` → `is_confounder = delta_pp >= 5 or (p_value <= 0.05 and delta_pp > 0)`
- **逻辑**：只有正方向（高 COMET → 高 acc，delta > 0）才可能判定为 confounder；负方向一律排除
- **运行结果**：delta=-5.64pp，p=0.695，结论仍为 `not_confounder`，与预期一致
- **JSON 已重新保存**到 `/root/clkc_mech_interp/data/qwen3/comet_tertile_ablation.json`

---
