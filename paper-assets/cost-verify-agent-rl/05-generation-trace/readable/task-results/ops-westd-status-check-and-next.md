# ops westd status check and next

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd_status_check_and_next_20260522T115818_result.json`
- **Structured JSON:** [`990c326cdc03908856de.json`](../../sessions/99/990c326cdc03908856de.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个新 eval 都已启动成功（Ray instance 已初始化，GPU 0/1 开始占用）。另外注意到 ragen_eval_gpu2 session 还残留（之前 high_kl_step7 的，已完成）。

---

## 汇总

### 已完成 Eval 结果（134 episodes OOD）

| Eval | pass@1 | action_is_valid | response_length |
|------|--------|-----------------|-----------------|
| **intervention_c_step7** (GPU 0) | **16.4%** | 66.3% | 6460 |
| **high_kl_step5** (GPU 1) | **8.2%** | 68.1% | 6665 |
| **high_kl_step7** (GPU 2) | **12.7%** | 67.2% | 7224 |
| **SFT baseline v3** (GPU 3) | **6.7%** | 68.4% | 7851 |

### 新启动任务

| GPU | 任务 | Config | Log |
|-----|------|--------|-----|
| 0 | seed5 v2 re-eval | `_alfworld_exp029_seed5_ood_eval_v2` | `ragen_seed5_ood_eval_v2.log` |
| 1 | c_prime_step5 eval | `_alfworld_c_prime_step5_ood_eval` | `ragen_c_prime_step5_ood_eval.log` |
| 2-3 | 空闲 | — | — |

### GPU 状态

- GPU 0/1：正在启动 eval（model loading 中）
- GPU 2/3：空闲（可接更多任务）

---
