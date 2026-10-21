# check quick harvest docred lora

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_quick-harvest-docred-lora_20260523T015230_result.json`
- **Structured JSON:** [`7e72f5cdddbb6454e9fb.json`](../../sessions/7e/7e72f5cdddbb6454e9fb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### GPU 状态 (westd-16980)
- GPU 0 & 1: **空闲** (0% utilization, 0 MiB)，无 Python 进程

### 实验结果

| 指标 | Unconstrained | Grammar-only | Semantic-only | Full S1 |
|------|:---:|:---:|:---:|:---:|
| **R-F1** | — (0.88% DR baseline) | **43.96** | **43.61** | **43.95** |
| **E-F1** | — | 80.13 | 80.06 | 79.38 |
| **DR%** | 0.88% | **0.38%** | **0%** | **0%** |
| **RV%** | — | **0%** | 0.51% | **0%** |
| **CF%** | — | 0.06% | 0.21% | 0.18% |
| Parse fail | — | 10.5% | 11% | 12.5% |

### 关键发现

**grammar_only 结论标记为 negative**：假设预测 grammar 层对 DR 零贡献（与 SciERC 一致），但实际 DR 从 0.88% 降到 0.38%——grammar 在 DocRED LoRA 上有部分 DR 贡献，与 SciERC 模式不同。

- Grammar 层：消除了 RV（→0%），部分降低 DR（0.88%→0.38%）
- Semantic 层：完全消除 DR（→0%），但保留了部分 RV（0.51%）
- 两层互补：grammar 管 RV，semantic 管 DR，组合后 S1 全清零

### Registry 更新
- `eval_70b_lora_docred_200_grammar_only`: RUNNING → **DONE** (negative)
- `eval_70b_lora_docred_200_semantic_only`: 已是 DONE (success)
- westd-21461 上还有 2 个 RUNNING：`full_s2` 和 `zs_full_s1`

---
