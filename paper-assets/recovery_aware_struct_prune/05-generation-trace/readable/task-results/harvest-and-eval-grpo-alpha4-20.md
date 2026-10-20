# harvest and eval grpo alpha4 20

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_and_eval_grpo_alpha4_20_20260521T192417_result.json`
- **Structured JSON:** [`66868dca9bf706292111.json`](../../sessions/66/66868dca9bf706292111.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 eval 都已上 GPU，运行正常。

## 汇总

### GRPO α=4.0 Reward Trajectory（无 collapse）

| Step | Reward | Loss | KL |
|------|--------|------|----|
| 10 | 0.146 | 0.016 | 0.0017 |
| 20 | 0.208 | 0.056 | 0.0019 |
| 30 | 0.184 | -0.022 | 0.0018 |
| 70 | 0.256 | 0.030 | 0.0021 |
| 80 | 0.230 | 0.102 | 0.0019 |
| 90 | 0.193 | 0.025 | 0.0019 |
| **100** | **0.198** | **0.018** | **0.00198** |

**Reward 未 collapse 到 0**，维持 0.15-0.26 区间。与 α=1.0 RASP GRPO 的 collapse 行为形成对比，说明 α=4.0 有效缓解了 RASP collapse。

### Eval Jobs

| Eval | exp_id | GPU | PID |
|------|--------|-----|-----|
| GSM8K (N=1319) | `eval_gsm8k_grpo_alpha4_20` | westd:0 (PID 412993) | 412988 |
| MATH-500 (@2048) | `eval_math500_grpo_alpha4_20` | westd:2 (PID 412822) | 412817 |

### GPU 分布
- GPU 0: GSM8K eval (12.5GB)
- GPU 1: 其他实验 (PID 382472)
- GPU 2: MATH-500 eval (12.5GB)
- GPU 3: 其他实验 (PID 385685)

---
