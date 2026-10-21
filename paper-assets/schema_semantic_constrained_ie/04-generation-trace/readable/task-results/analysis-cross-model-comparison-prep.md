# analysis cross model comparison prep

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cross_model_comparison_prep_20260514T135349_result.json`
- **Structured JSON:** [`7d53c09ee4d1f2ed8899.json`](../../sessions/7d/7d53c09ee4d1f2ed8899.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。产出文件 `artifacts/cross_model_analysis_framework.md`（已注册 `art_20260514_47fb0c`），核心要点：

**表格**：单表双模型，主列 DR/RV/ET + ΔDR 相对降幅，F1 靠右作为 control variable。用相对百分比（↓94%）而非绝对 pp 差，解决 baseline 不可比问题。

**叙事**：三层论证——(a) violation reduction 与模型无关（同约束编译、零代码修改），(b) F1 差异是 zero-shot 能力差异、与约束有效性无关，(c) 不同 violation profile 反而增强 evidence 的多样性。

**Checklist**：Llama full_s1 到达后重点看 ΔDR% 是否 >80%、RV/ET 是否归零、R-F1 是否在 ±1pp 内、CF 是否也升高（强化系统性副作用论证）。统计检验用 McNemar 即可。

---
