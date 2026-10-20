# ssh d064 quick check r3

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_d064_quick_check_r3_20260519T174054_result.json`
- **Structured JSON:** [`2ece67669b9911549495.json`](../../sessions/2e/2ece67669b9911549495.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## d064 状态汇总

### westd-21461（2× GPU）
| GPU | 利用率 | 显存 |
|-----|--------|------|
| GPU 0 | 86% | 18275 MiB |
| GPU 1 | 69% | 18921 MiB |

**运行中进程：**
- GPU 0: `llama_docred_greedy_constrained` (运行 186 min)
- GPU 1: `qwen_docred_beam4_constrained` (运行 155 min)

**输出进度：**
| 文件 | 行数 | 状态 |
|------|------|------|
| d064_llama_docred_greedy_unconstrained | 998 | ✅ 已完成 |
| d064_qwen_docred_beam4_unconstrained | 998 | ✅ 已完成 |
| d064_llama_docred_greedy_constrained | 714/998 | 🔄 运行中 |
| d064_qwen_docred_beam4_constrained | 376/998 | 🔄 运行中 |

---

### westd-16980（2× GPU）
| GPU | 利用率 | 显存 |
|-----|--------|------|
| GPU 0 | 90% | 18277 MiB |
| GPU 1 | 79% | 18277 MiB |

**运行中进程：**
- GPU 0: `llama_docred_beam4_unconstrained` (运行 194 min)
- GPU 1: `llama_docred_beam4_constrained` (运行 194 min)

**输出进度：**
| 文件 | 行数 | 状态 |
|------|------|------|
| d064_llama_docred_beam4_unconstrained_16980 | 629/998 | 🔄 运行中 |
| d064_llama_docred_beam4_constrained_16980 | 544/998 | 🔄 运行中 |

---

4 台 GPU 全部在跑，6 个任务中 2 个已完成（greedy_unc、qwen_beam4_unc），4 个进行中。按当前速率，21461 上 llama_greedy_con 约剩 1h，qwen_beam4_con 约剩 2.5h；16980 两个 beam4 任务各约剩 2h。

---
