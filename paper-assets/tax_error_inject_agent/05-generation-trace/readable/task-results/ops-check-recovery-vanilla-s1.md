# ops check recovery vanilla s1

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-recovery-vanilla-s1_20260516T082452_result.json`
- **Structured JSON:** [`4abdfdff7a6405f3c233.json`](../../sessions/4a/4abdfdff7a6405f3c233.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## recovery-vanilla-s1 Eval 结果

| 指标 | 值 |
|------|-----|
| **Total** | 47 |
| **Recovery rate** | **0.66** (31/47) |
| **Detection rate** | **0.0** (0/47) |

**Per-operator:**

| Operator | Recovery | Detection |
|----------|----------|-----------|
| C1_context_truncation | 8/12 (0.667) | 0/12 |
| C4_observation_masking | 6/11 (0.545) | 0/11 |
| P1_step_order_swap | 8/12 (0.667) | 0/12 |
| P2_sub_goal_deletion | 9/12 (0.750) | 0/12 |

结果已保存到 `eval_results/v4_vanilla_recovery_eval_s1.json`。

---

## GPU 状态

| GPU | Memory | Util | 任务 |
|-----|--------|------|------|
| **0** | **0 MiB** | **0%** | **空闲** (eval 已完成) |
| 1 | 28,493 MiB | 99% | llama31-taxei-s42 SFT + eval-rp-s0 tmux session |
| 2 | 27,019 MiB | 99% | v4-taxei-rp-s7 SFT (Qwen3-8B, seed=7) |
| 3 | 28,685 MiB | 99% | llama31-random-s42 SFT |

另外 CPU 上还在跑 `collect_trajectories_scaleup.py`（PID 249190，phase1 r2，1000 trajectories）。

**GPU 0 完全空闲，可立即调度新任务。**

---
