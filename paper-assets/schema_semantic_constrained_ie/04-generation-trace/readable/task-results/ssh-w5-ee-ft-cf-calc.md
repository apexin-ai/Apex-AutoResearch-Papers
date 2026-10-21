# ssh w5 ee ft cf calc

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_w5_ee_ft_cf_calc_20260519T064605_result.json`
- **Structured JSON:** [`ebdc79cbb265a84b1ea6.json`](../../sessions/eb/ebdc79cbb265a84b1ea6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

| Model | Condition | Total Args | CF Entities | CF Rate (%) |
|-------|-----------|-----------|-------------|-------------|
| Qwen FT | Unconstrained | 261 | 2 | 0.77 |
| Qwen FT | Constrained | 339 | 3 | 0.89 |
| Llama FT | Unconstrained | 298 | 1 | 0.34 |
| Llama FT | Constrained | 255 | 3 | 1.18 |

核心发现：
1. **CF 率很低**（0.3%--1.2%），FT 本身已大幅降低 CF
2. **Constrained decoding 未降低 CF**，两个模型的 constrained CF 反而略高于 unconstrained，因为当前约束语法只约束单事件内 role-type 兼容性，不做跨事件 entity type 一致性检查
3. **多数 CF 是语义歧义**而非模型错误（如 "drone" → VEH/WEA, "police" → ORG/PER）
4. 与 RE CF 率（Qwen 1.18%, Llama 0.46% on SciERC）处于同一量级

Artifact 已注册为 `w5_ee_ft_cf_results`。

---
