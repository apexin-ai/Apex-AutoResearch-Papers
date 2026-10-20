# check westd16980 status

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_westd16980-status_20260522T162404_result.json`
- **Structured JSON:** [`a5725e4dd9e80eaa35a0.json`](../../sessions/a5/a5725e4dd9e80eaa35a0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

### GPU 状态
| GPU | 型号 | 显存 | 利用率 | 进程 |
|-----|------|------|--------|------|
| 0 | RTX PRO 6000 Black (98GB) | 40873/97887 MiB | 75% | PID 957041 — 70B LoRA beam4 S1 eval |
| 1 | RTX PRO 6000 Black (98GB) | 0/97887 MiB | 0% | **空闲** |

### 实验状态

| 实验 | 状态 | 进度 | 结果 |
|------|------|------|------|
| **tcr_beam4_llama_scierc** | **DONE (negative)** | 551/551 | TCR changed selection = **0/551 (0%)**。E_F1=68.02, R_F1=46.05, DR=1.1% — 与 vanilla beam4 (68.06/46.18) 几乎相同。TCR 对 fine-tuned LLaMA+beam4 完全无效。 |
| **eval_70b_lora_scierc_beam4_s1** | **RUNNING** | 338/551 (61%) | GPU 0 上跑，预计还需 ~1-2 小时完成 |
| eval_70b_zs_scierc_semantic_only | Registry RUNNING | 无输出文件 | **Stale** — 无进程、无输出，可能上个 session 未完成 |
| eval_70b_zs_scierc_grammar_only | Registry RUNNING | 无输出文件 | **Stale** — 同上 |

### 关键发现

**TCR 对 LLaMA SciERC beam4 的 negative 结论**与 Qwen 版本一致（tcr_beam4_qwen_scierc 也是 negative）。原因：fine-tuned 模型 + beam4 constrained decoding 已经把 DR violation 压到 ~1%，beam candidates 之间几乎没有 constraint violation 差异，TCR 无法产生 reranking 效果。

### 未启动的实验
- **70b_lora_scierc_beam4_unconstrained baseline** — 尚无输出文件。GPU 1 空闲可用，但按要求暂不启动，等 Agent 决定下一步。

---
