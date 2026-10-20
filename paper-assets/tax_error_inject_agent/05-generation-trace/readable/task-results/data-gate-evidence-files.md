# data gate evidence files

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_gate-evidence-files_20260514T122301_result.json`
- **Structured JSON:** [`1775bd68313eda5f3eeb.json`](../../sessions/17/1775bd68313eda5f3eeb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 JSON 证据文件已生成。

## 结果

| Gate | 指标 | 阈值 | 实际值 | 判定 |
|------|------|------|--------|------|
| **Gate 1**: Injection Validity | 注入合法率 | ≥ 80% | **100%** (760/760) | **PASS** |
| **Gate 2**: Recovery Quality | 质量达标率 | ≥ 75% | **97.5%** (78/80) | **PASS** |

**Gate 2 质量分布**：Strong 36, Moderate 42, Weak 2

**Gate 1 各算子**（全部 100%）：
- P1_step_order_swap: 188
- P2_sub_goal_deletion: 192
- C1_context_truncation: 191
- C4_observation_masking: 189

**文件路径**：
- `scripts/verify_gate1.py` → `eval_results/gate1_injection_validity.json`
- `scripts/verify_gate2.py` → `eval_results/gate2_recovery_quality.json`

---
