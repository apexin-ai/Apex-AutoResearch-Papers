# check full gpu status and harvest

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_full-gpu-status-and-harvest_20260522T225045_result.json`
- **Structured JSON:** [`301219fee9958fe1961e.json`](../../sessions/30/301219fee9958fe1961e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报如下：

---

## GPU 状态

### westd-16980（2× RTX PRO 6000 Black 98GB）
| GPU | 显存 | Util | 任务 | 进度 |
|-----|------|------|------|------|
| 0 | 40.8/97.9 GB | 81% | `70b_lora_docred_200_semantic_only` | **96/200** docs |
| 1 | 40.9/97.9 GB | 76% | `70b_lora_docred_200_grammar_only` | **93/200** docs |

### westd-21461（2× RTX PRO 6000 Black 98GB）
| GPU | 显存 | Util | 任务 | 进度 |
|-----|------|------|------|------|
| 0 | 39.1/97.9 GB | 92% | `70b_zs_docred_200_unconstrained` | **刚启动** (PID 84588) |
| 1 | 40.3/97.9 GB | 92% | `70b_zs_docred_200_grammar_only` | **166/200** docs |

---

## 已完成实验收割

### eval_70b_zs_docred_200_semantic_only → **DONE (success)**

| 指标 | 值 | vs unconstrained baseline (DR=15%) |
|------|-----|-----|
| DR% | **1.66%** | ↓ 89% relative reduction |
| RV% | 8.24% | (semantic layer 不约束 RV) |
| ET% | 0.12% | — |
| CF | 132 (4.07%) | — |
| E-F1 | 70.10 | ≈持平 (69.03 baseline) |
| R-F1 | 13.05 | ≈持平 (13.03 baseline) |

Hypothesis 验证：semantic layer 在 70B ZS DocRED 上显著降低 DR (15% → 1.66%)，且不损失 F1。

### eval_70b_zs_scierc_unconstrained — 已在之前收割（DONE）

---

## 新启动实验

| exp_id | 服务器 | GPU | PID | 说明 |
|--------|--------|-----|-----|------|
| `eval_70b_zs_docred_200_unconstrained` | westd-21461 | 0 | 84588 | 200-doc unconstrained baseline，补全消融矩阵 |

**4/4 GPU 全部在跑。** westd-21461 grammar_only 约 30 min 后完成（166/200），届时可启动下一个实验。

---
