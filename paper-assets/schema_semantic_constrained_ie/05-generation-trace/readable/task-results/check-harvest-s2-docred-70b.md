# check harvest s2 docred 70b

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_harvest-s2-docred-70b_20260523T080243_result.json`
- **Structured JSON:** [`42a4c92860f62ec6b71e.json`](../../sessions/42/42a4c92860f62ec6b71e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 不存在（可能已在之前清理）。实验已标记 DONE。

---

## eval_70b_lora_docred_200_full_s2 结果（conclusion: **negative**）

| 指标 | Unconstrained | S1 Greedy | S1 Beam4 | **S2 Full** |
|------|:---:|:---:|:---:|:---:|
| **R-F1** | 43.80 | 43.95 | 48.14 | **36.45** ↓11.7 |
| R-P | — | — | — | 31.25 |
| R-R | — | — | — | 43.72 |
| **E-F1** | 80.34 | 79.38 | 85.57 | **84.96** |
| E-P | — | — | — | 84.60 |
| E-R | — | — | — | 85.34 |
| DR% | 0.22% | 0% | 0% | **0%** |
| RV% | — | — | — | 0% |
| ET% | — | — | — | 0% |
| CF% | 0.06% | 0.18% | 0% | **0.34%** (13) |
| PF% | 10% | 12.5% | 0.5% | **0%** |
| #pred_ent | — | — | — | 3819 |
| #pred_rel | — | — | — | 3546 |

### 关键发现

1. **S2 over-constraining 严重**：R-F1 从 S1 beam4 的 48.14 暴跌到 36.45（-11.7 点），precision 仅 31.25%，说明 S2 的 repair 层虽然消除了 DR 违反，但大量错误修复了本来正确的关系，或者限制了模型产出有效关系的能力。
2. **CF 未被消除**：S2 repair 理论上应消除 CF，但实际 CF=0.34%（13 个），比 S1 beam4 的 0% 更高。repair 可能引入了新的跨字段不一致。
3. **E-F1 稳定**：84.96 vs 85.57（S1 beam4），实体抽取不受 S2 影响。
4. **PF=0%**：解析完全成功，S2 的语法约束层工作正常。

与 SciERC 上观察到的 S2 下降趋势一致，DocRED 上更为严重。**S1 beam4 仍是 DocRED 上的最优配置。**

---
