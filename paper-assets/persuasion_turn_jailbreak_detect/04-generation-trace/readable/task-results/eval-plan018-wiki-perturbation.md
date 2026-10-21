# eval plan018 wiki perturbation

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_plan018-wiki-perturbation_20260518T062359_result.json`
- **Structured JSON:** [`faf2369523a2bff2bd59.json`](../../sessions/fa/faf2369523a2bff2bd59.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

**结果总结：**

| K | Clean F1 | Perturbed F1 | Delta |
|---|---|---|---|
| k=1 | 0.947 | 0.824 | **-0.124** |
| k=2 | 0.934 | 0.780 | **-0.154** |
| k=3 | 0.974 | 0.795 | **-0.179** |
| k=5 | 0.987 | 0.838 | **-0.149** |
| full | 0.987 | 0.866 | **-0.121** |

Wiki MLM perturbation degradation (-0.121 ~ -0.179) 与 vanilla baseline (-0.118) 量级相当，远差于 JB MLM (-0.026) 和 persuasion treatment (0.000)。假设成立：out-of-domain pretraining 不提供 perturbation robustness，domain-specific MLM 才是关键。

已保存结果到 `results/plan_018_wiki_perturbation.json`，registry 实验 `plan_018_wiki_perturbation` 已设为 DONE。

---
