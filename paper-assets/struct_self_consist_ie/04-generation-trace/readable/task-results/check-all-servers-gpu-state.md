# check all servers gpu state

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_all_servers_gpu_state_20260521T090529_result.json`
- **Structured JSON:** [`4c30431cf1008ae975ed.json`](../../sessions/4c/4c30431cf1008ae975ed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 6 个已完成实验的 registry 已更新。汇总如下：

---

## GPU 状态总览

### 5090 (autodl-5090)
| GPU | VRAM | Util | 实验 | 状态 |
|-----|------|------|------|------|
| 0 | 2 MiB | 0% | — | **空闲** |
| 1 | 2 MiB | 0% | — | **空闲** |
| 2 | 2 MiB | 0% | — | **空闲** |
| 3 | 30 GB | 68% | e2_pretrained_fewnerd (PID 8411) | 43% (130K/301K prompts) |

### 5090-b (bjb2-11496)
| GPU | VRAM | Util | 实验 | 状态 |
|-----|------|------|------|------|
| 0 | 2 MiB | 0% | conll_mf4v2_s123 已完成 | **空闲** |
| 1 | 2 MiB | 0% | conll_mf4v2_s456 已完成 | **空闲** |
| 2 | 30 GB | 92% | fewnerd_mf4v2_s456 (PID 334428) | 运行中 |
| 3 | 30 GB | 92% | scierc_mf4v2_s42 (PID 336946) | 运行中 |

### 5090-c (autodl-5090-c)
| GPU | VRAM | Util | 实验 | 状态 |
|-----|------|------|------|------|
| 0 | 30 GB | 92% | fewnerd_n16_s456_v2 (PID 293442) | 52% (315K/602K prompts) |
| 1 | 0 MiB | 0% | conll_n16_s123_v2 已完成 | **空闲** |
| 2 | 0 MiB | 0% | conll_n16_s456_v2 已完成 | **空闲** |
| 3 | 0 MiB | 0% | e2_pretrained_scierc 已完成 | **空闲** |

API 实验（无 GPU）：Gemini 193/200 运行中，DeepSeek 200/200 已完成

**空闲 GPU：5090×3 + 5090-b×2 + 5090-c×3 = 8 块**

---

## 已完成实验 Metrics 汇总

| 实验 | greedy_F1 | oracle_F1 | ρ(SJ) full | ρ(κ) full | verdict |
|------|-----------|-----------|------------|-----------|---------|
| **conll_mf4v2_s123** (N=8) | 0.908 | 0.953 | 0.463 | 0.446 | PASS |
| **conll_mf4v2_s456** (N=8) | 0.907 | 0.943 | 0.480 | 0.464 | PASS |
| **conll_n16_s123_v2** (N=16) | 0.907 | 0.963 | 0.457 | 0.447 | PASS |
| **conll_n16_s456_v2** (N=16) | 0.908 | 0.955 | 0.479 | 0.470 | PASS |
| **e2_pretrained_scierc** (N=8) | 0.242 | 0.389 | 0.219 | 0.252 | FAIL ⚠️ |
| **frontier_sc_deepseek** (N=8) | 0.399 | 0.714 | — | — | success |

| 实验 | 额外信息 |
|------|---------|
| e2_pretrained_scierc | 46% samples F1=0, structural_beats_surface=false |
| frontier_sc_deepseek | mv_F1=0.424, selection_gap=0.290, degeneracy=5.5%, parse_fail=751/1600 |

### 仍在运行
- **e2_pretrained_fewnerd** (5090 GPU3): 43%, 预计还需 ~2.5h
- **fewnerd_mf4v2_s456** (5090-b GPU2): 运行中
- **scierc_mf4v2_s42** (5090-b GPU3): 运行中
- **fewnerd_n16_s456_v2** (5090-c GPU0): 52%, 预计还需 ~1.7h
- **frontier_sc_gemini25pro** (5090-c API): 193/200, 预计 ~8min

---
