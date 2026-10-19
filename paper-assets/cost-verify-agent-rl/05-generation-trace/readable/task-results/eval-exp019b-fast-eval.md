# eval exp019b fast eval

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_exp019b-fast-eval_20260514T214641_result.json`
- **Structured JSON:** [`846ce228e09c75e8b9b1.json`](../../sessions/84/846ce228e09c75e8b9b1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp019b_expert_sft_v3 Fast Eval 结果

| 指标 | 结果 | Pass 标准 | 状态 |
|------|------|-----------|------|
| **success_rate** | **20.0%** (4/20) | ≥ 10% | **PASS** |
| **format_ok_rate** | **100.0%** (全部) | ≥ 90% | **PASS** |
| **action_is_valid_rate** | **85.33%** | ≥ 85% | **PASS** |

**三项指标全部 PASS。**

### Episode 详情

| EP | Type | Steps | Valid | Format | Success | Time |
|----|------|-------|-------|--------|---------|------|
| 0 | put | 30 | 33% | 100% | N | 7.4s |
| 1 | heat | 30 | 63% | 100% | N | 9.1s |
| 2 | put | 4 | 100% | 100% | **Y** | 1.3s |
| 3 | clean | 30 | 90% | 100% | N | 7.1s |
| 4 | put | 30 | 73% | 100% | N | 7.9s |
| 5 | put | 30 | 100% | 100% | N | 6.8s |
| 6 | put | 30 | 83% | 100% | N | 6.7s |
| 7 | cool | 30 | 90% | 100% | N | 11.0s |
| 8 | cool | 30 | 90% | 100% | N | 10.3s |
| 9 | clean | 30 | 100% | 100% | N | 9.3s |
| 10 | put | 30 | 100% | 100% | N | 12.6s |
| 11 | put | 10 | 100% | 100% | **Y** | 2.4s |
| 12 | heat | 30 | 97% | 100% | N | 9.1s |
| 13 | clean | 30 | 100% | 100% | N | 7.5s |
| 14 | examine | 30 | 100% | 100% | N | 7.8s |
| 15 | put | 30 | 83% | 100% | N | 7.3s |
| 16 | cool | 30 | 100% | 100% | N | 10.2s |
| 17 | put | 7 | 100% | 100% | **Y** | 2.2s |
| 18 | clean | 6 | 100% | 100% | **Y** | 2.6s |
| 19 | put | 30 | 3% | 100% | N | 7.5s |

成功的 4 个 episode（EP2/11/17/18）均以少量步骤（4-10步）高效完成，valid=100%。avg_steps=25.4，eval 总耗时 146s。

---
