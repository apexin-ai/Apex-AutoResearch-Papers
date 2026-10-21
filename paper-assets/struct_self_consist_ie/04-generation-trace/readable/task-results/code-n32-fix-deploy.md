# code n32 fix deploy

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_n32_fix_deploy_20260523T083150_result.json`
- **Structured JSON:** [`60edf78c0b85a7715cbc.json`](../../sessions/60/60edf78c0b85a7715cbc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

运行完成。修复验证结果：

| 指标 | 修复前（旧版） | 修复后 | 参考值 |
|------|---------------|--------|--------|
| Greedy F1 | ~0.538 | 0.539 | 0.538 |
| **MV Δ** | **+3.2 pp** | **+4.0 pp** | **+3.9 pp** |
| Degen | ~11.7% | 12.3% | 11.7% |
| Oracle Δ | ~11.2 pp | +11.3 pp | +11.2 pp |
| Capture | ~36% | 31% | 36% |

**修复有效**：MV Δ 从 +3.2 pp 提升到 +4.0 pp，与参考值 +3.9 pp 非常接近（差 0.1 pp 属正常波动）。旧版因用 `(text, type)` 投票导致不同位置的同名实体被合并，使 MV 增益被低估了 0.8 pp。

---
