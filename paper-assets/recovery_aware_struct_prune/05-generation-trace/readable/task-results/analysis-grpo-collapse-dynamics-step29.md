# analysis grpo collapse dynamics step29

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_grpo_collapse_dynamics_step29_20260517T171432_result.json`
- **Structured JSON:** [`9c2912a85a9f208d20e7.json`](../../sessions/9c/9c2912a85a9f208d20e7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/collapse_dynamics_comparison.md`。

**核心结论：**

| Run | Collapse? | Evidence |
|-----|-----------|----------|
| **grpo_random_20** (step 30) | **未 collapse** | frac_zero_std=0.325, reward=0.1663, grad_norm=3.67, 高 entropy (0.23) |
| **grpo_cka_only_20** (step 21) | **未 collapse** | frac_zero_std=0.200 (最低), reward=0.218 (最高), 但 entropy 偏低 (0.08) 需监控 |
| RASP v9 | **从 step 0 就已 collapse** | frac_zero_std=0.875@step10, completion 全部 maxlen, SFT checkpoint 本身已退化 |
| Standard v8 | **卡住但未全 collapse** | frac_zero_std 0.45-0.675, reward 停在 0.04-0.10, step 60 有 grad 瞬间归零 |

**C2 collapse gradient 排序：** RASP v9 (即时) >> Standard v8 (卡住/step60 grad 信号) >> Random (step 30 无迹象) ≈ CKA-only (step 21 无迹象)

两个新 run 的 reward (0.16-0.25) 已大幅超过 Standard v8 峰值 (0.096)。CKA-only 的低 entropy 是唯一风险信号，值得在 step 30-40 时复查。

---
