# ops humaneval registry audit and harvest

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_humaneval_registry_audit_and_harvest_20260519T051210_result.json`
- **Structured JSON:** [`38bf868d7165e3c4061f.json`](../../sessions/38/38bf868d7165e3c4061f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

9 个条目全部注册完成。

---

## HumanEval 结果清单

### @2048 tokens（主要结果）

| Registry ID | Model | pass@1 | n_correct/164 | Fair v5? |
|---|---|---|---|---|
| `eval_humaneval_unpruned_2048` | Dense | **45.12%** | 74 | N/A |
| `eval_humaneval_sft_standard_20_2048_v2` | SFT Standard 20% | 11.59% | 19 | N/A (SFT) |
| `eval_humaneval_sft_rasp_20_2048` | SFT RASP 20% | 10.37% | 17 | N/A (SFT) |
| `eval_humaneval_grpo_standard_20_2048` | GRPO Standard 20% (v8) | 10.37% | 17 | **No** (old stage2) |
| `eval_humaneval_grpo_rasp_20_2048` | GRPO RASP 20% (v9) | **14.63%** | 24 | **No** (old stage2) |

### @512 tokens（token 不足，仅供参考）

| Registry ID | Model | pass@1 | n_correct/164 |
|---|---|---|---|
| `eval_humaneval_unpruned_512` | Dense | 1.83% | 3 |
| `eval_humaneval_sft_standard_20_512` | SFT Standard 20% | 3.05% | 5 |
| `eval_humaneval_sft_rasp_20_512` | SFT RASP 20% | 7.32% | 12 |
| `eval_humaneval_grpo_standard_20_512` | GRPO Standard 20% (v8) | 1.83% | 3 |
| `eval_humaneval_grpo_rasp_20_512` | GRPO RASP 20% (v9) | 10.37% | 17 |

### 运行中

| Eval | GPU | PID | Progress | 当前 pass@1 | 预计剩余 |
|---|---|---|---|---|---|
| SFT CKA-only @2048 | cuda:2 | 63783 | 90/164 (55%) | **0.00%** | ~1.5h |
| GRPO CKA-only @2048 | cuda:1 | 66531 | 66/164 (40%) | **~33%** | ~1.5h |

### 关键发现
- SFT CKA-only HumanEval 到 90/164 仍然 pass@1=0.00%，代码生成能力完全丧失
- GRPO CKA-only 约 33% pass@1，远高于其他剪枝模型（10-15%），接近 Dense 的 45%
- GRPO RASP (v9) 在所有已完成剪枝模型中 HumanEval 最高（14.63%），但这是旧 stage2 模型
- 所有 GRPO 条目（Standard/RASP）均为旧 stage2，已标注 "needs re-eval with fair model"

---
