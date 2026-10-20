# ops eval rp s42 check

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_eval-rp-s42-check_20260516T063224_result.json`
- **Structured JSON:** [`e039c931d02e9990f88a.json`](../../sessions/e0/e039c931d02e9990f88a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**状态：已完成**

eval-rp-s42 已跑完全部 47/47 episodes，结果保存在 `eval_results/v4_taxei_rp_s42_injected.json`（注意路径是 `eval_results/` 而非 `eval_outputs/`）。

### 结果

| 指标 | 值 |
|------|-----|
| **Overall recovery rate** | **18/47 = 0.383** |
| Detection rate | 0/47 = 0.000 |

### Per-operator breakdown

| Operator | Recovered | Rate |
|----------|-----------|------|
| C1_context_truncation | 6/12 | 0.500 |
| C4_observation_masking | 3/11 | 0.273 |
| P1_step_order_swap | 6/12 | 0.500 |
| P2_sub_goal_deletion | 3/12 | 0.250 |

### 当前 GPU 状态

cuda:0 上的 eval 进程已结束，现在 4 张卡全部在跑新任务 — PID 244784 (cuda:0) 是 `llama31-vanilla-s42` 的 SFT 训练（swift sft, seed=42, 3 epochs, LoRA rank 16）。其余 3 张卡也各有 Python 进程占满显存（99% 利用率）。

---
