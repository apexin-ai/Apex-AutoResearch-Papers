# ops eval rp s123 check

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_eval-rp-s123-check_20260516T062029_result.json`
- **Structured JSON:** [`3ac6d690235e8fac2ece.json`](../../sessions/3a/3ac6d690235e8fac2ece.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果报告

### 1. eval-rp-s123: **成功完成** ✓
- 输出文件: `v4_taxei_rp_s123_injected.json` (499KB, 14:19)
- **Recovery rate: 0.574** (27/47)
- Detection rate: 0.0 (0/47)
- Per-operator breakdown:
  | Operator | Recovery | Detection |
  |---|---|---|
  | C1_context_truncation | 7/12 (0.583) | 0/12 |
  | C4_observation_masking | 5/11 (0.455) | 0/11 |
  | P1_step_order_swap | 8/12 (0.667) | 0/12 |
  | P2_sub_goal_deletion | 7/12 (0.583) | 0/12 |

### 2. 其他 eval 状态

| Seed | Status | Recovery Rate | Notes |
|---|---|---|---|
| s0 | **完成** | 0.468 | 输出文件已生成 (571KB) |
| s1 | **完成** | 0.489 | 输出文件已生成 (545KB) |
| s42 | **运行中** | — | 21/47 episodes 完成，约 45% 进度 |

### 3. GPU 使用
| GPU | Utilization | Memory |
|---|---|---|
| cuda:0 | 80% | 17091 MiB |
| cuda:1 | 0% | 0 MiB |
| cuda:2 | 0% | 0 MiB |
| cuda:3 | 0% | 0 MiB |

s42 正在 cuda:0 上运行，预计还需约 1 小时完成（剩余 26 episodes，部分 FAIL episode 会跑满 50 steps）。

### 4 seed RP eval 汇总（已完成 3/4）

| Seed | Recovery | Best operator | Worst operator |
|---|---|---|---|
| s0 | 0.468 | P2 (0.583) | C1 (0.333) |
| s1 | 0.489 | P1 (0.750) | C4 (0.364) |
| s123 | 0.574 | P1 (0.667) | C4 (0.455) |
| s42 | pending | — | — |

---
