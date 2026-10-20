# analysis r8 n1 quantifier proportion

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r8-n1-quantifier-proportion_20260520T201553_result.json`
- **Structured JSON:** [`76879e711e5238261bb4.json`](../../sessions/76/76879e711e5238261bb4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果：

**73,264 个约束** across 3 conditions (Mistral-7B FOLIO/PW, Qwen2.5-14B FOLIO):

| 类别 | 占比 | 含义 |
|------|------|------|
| Quantified (真 FOL) | **1.0%** (755) | Z3 ForAll/Exists |
| Grounded FOL | 44.2% (32,361) | `P(X) → Q(X)` 语法，但 Z3 编码为 Bool |
| Ground Atom | 45.1% (33,026) | `student(bonnie)` 命题式谓词 |
| Propositional | 9.7% (7,122) | 纯命题逻辑 |

**99.0% 的约束在 Z3 solver 层面是命题式的**。Reviewer 的判断正确。

结果保存在：
- 服务器：`/root/symb_invariant_consensus/results/r8_n1_quantifier_proportion/`
- 本地：`artifacts/r8_n1_quantifier_proportion/results.json` + `summary.md`

建议论文修订：将 "FOL constraints" 改为 "symbolic constraints in predicate notation" 或 "propositionalized constraints"。

---
