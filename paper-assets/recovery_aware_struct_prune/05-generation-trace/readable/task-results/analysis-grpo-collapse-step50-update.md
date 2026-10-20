# analysis grpo collapse step50 update

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_grpo_collapse_step50_update_20260517T182058_result.json`
- **Structured JSON:** [`e82d32e926ba9c5055f4.json`](../../sessions/e8/e82d32e926ba9c5055f4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/collapse_dynamics_step50_update.md`。

**核心结论：**

两个 run 都还没到 step 50（random_20 @ 39, cka_only_20 @ 30），当前只有 step 10/20/30 的指标。

**Step 30 快照排序：**

| Run | Reward | Frac_zero_std | 状态 |
|-----|--------|---------------|------|
| cka_only_20 | 0.250 | 0.200 | 稳定 |
| random_20 | 0.166 | 0.325 | 稳定 |
| standard_v8 (stage2) | 0.065 | 0.525 | 边缘停滞 |
| rasp_v9 (stage2) | 0.021 | 0.950 | 已 collapse |

**重要发现：**
- cka_only 显著优于 random（reward 高 50%，frac_zero_std 低 38%）
- 两个新 run 均未 collapse，但 random_20 在 step 20 有 grad_norm spike (8.62)，值得关注
- stage2 对照组不是直接 apples-to-apples 对比（它们在已 GRPO 过的模型上再训）
- **Delayed collapse 尚无法判断**，需等 step 40+ 数据（约 1.5-2.5h 后可查）

---
