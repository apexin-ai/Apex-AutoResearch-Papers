# check gpu and docred progress

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_gpu-and-docred-progress_20260522T211827_result.json`
- **Structured JSON:** [`5471ea240fc66dbe3005.json`](../../sessions/54/5471ea240fc66dbe3005.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。汇总如下：

---

## GPU 状态总览

### westd-16980 — 2× RTX PRO 6000 Blackwell (96GB)
| GPU | 显存占用 | 利用率 | 温度 | 运行任务 |
|-----|---------|--------|------|---------|
| 0 | 40.8/97.9 GB | 81% | 57°C | `70b_lora_docred_200_semantic_only` |
| 1 | 40.9/97.9 GB | 78% | 57°C | `70b_lora_docred_200_grammar_only` |

### westd-21461 — 2× RTX PRO 6000 Blackwell (96GB)
| GPU | 显存占用 | 利用率 | 温度 | 运行任务 |
|-----|---------|--------|------|---------|
| 0 | 39.7/97.9 GB | 91% | 56°C | `70b_zs_docred_200_semantic_only` |
| 1 | 0/97.9 GB | 0% | 31°C | **空闲** |

---

## 实验进度

| 实验 | 服务器 | 进度 | 状态 |
|------|--------|------|------|
| 70b_lora_docred_200_semantic_only | westd-16980 GPU0 | **32/200 (16%)** | 运行中 |
| 70b_lora_docred_200_grammar_only | westd-16980 GPU1 | **30/200 (15%)** | 运行中 |
| 70b_zs_docred_200_semantic_only | westd-21461 GPU0 | **88/200 (44%)** | 运行中 |
| 70b_lora_docred_200_beam4_s1 | westd-21461 | **200/200** | ✅ 已完成 |
| 70b_zs_scierc_unconstrained | westd-21461 | **551/551** | ✅ 已完成 |

---

## 已完成实验指标

| 指标 | beam4 S1 (DocRED LoRA) | ZS unconstrained (SciERC) |
|------|----------------------|--------------------------|
| E-F1 | **85.57** | 35.12 |
| R-F1 | **48.14** | 11.23 |
| ET% | 0 | 0 |
| RV% | 0 | **0.61** |
| DR% | **0** | **6.41** |
| CF% | 0 | 0 |
| Parse Fail | 0.5% | 0% |

**beam4 S1 亮点**: R-F1=48.14 显著超过 greedy S1 的 43.95 (+4.19)，同时保持 DR=0%、RV=0% 零违规。假设验证成功——beam search 在 70B DocRED 上不仅保持约束有效性，还提升了 F1。

**ZS SciERC unconstrained**: DR=6.41% 提供了 ZS 无约束 baseline，后续约束实验可对比违规消除效果。

**westd-21461 GPU1 当前空闲**，可安排新任务。

---
