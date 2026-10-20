# code beam scierc 551 collect

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_beam_scierc_551_collect_20260517T014119_result.json`
- **Structured JSON:** [`fd1adb327ad954fbfbbb.json`](../../sessions/fd/fd1adb327ad954fbfbbb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已完成。汇总：

```
Status: COMPLETE (551/551, 0 failures)
Output file: outputs/beam_search_scierc_full_551.jsonl
Lines: 551

=== Violation Rates ===
ET%:  0.0%   (0/2476 entities)
RV%:  0.0%   (0/1737 relations)
DR%:  0.0%   (0/1737 relations)
CF%:  0.53%  (13 cross-field consistency violations)
Go/No-go (DR): 0.0000

=== F1 Scores ===
E_F1: P=0.2683  R=0.3963  F1=0.3200  (TP=663, Gold=1673, Pred=2471)
R_F1: P=0.0669  R=0.1191  F1=0.0856  (TP=116, Gold=974, Pred=1735)

Parse failures: 0/551
Total entities extracted: 2476
Total relations extracted: 1737
```

关键发现：
- **Constraint compliance 完美** — ET/RV/DR 全部为 0%，beam search + grammar constraint 成功消除了所有类型和关系词汇违反以及 domain-range 违反
- **F1 偏低** — Entity F1=0.32, Relation F1=0.086。模型倾向于过度生成（Pred >> Gold），precision 很低
- 仅有 13 例 cross-field consistency 违反（同一 mention 在不同关系中类型不一致），比率 0.53%

---
