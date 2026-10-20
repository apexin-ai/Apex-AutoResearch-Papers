# analyze grpo cka only 20 v2

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_grpo_cka_only_20_v2_20260518T021755_result.json`
- **Structured JSON:** [`8f45d7a758d387b4e120.json`](../../sessions/8f/8f45d7a758d387b4e120.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已关闭。汇总：

**grpo_cka_only_20 最终结果**

| 指标 | 值 |
|---|---|
| Final step | 100/100 |
| Final reward | 0.3444 |
| Peak reward | 0.3544 (step 50) |
| Final frac_zero_std | 0.2 |
| Final loss | 0.23 |
| Final KL | 0.001609 |
| 训练时长 | 11h 18m (40710s) |
| Checkpoint | `/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20/` (38GB) |
| W&B run | `li451oi4` |
| Status | **DONE (success)** |

**Reward 轨迹**: 0.253 → 0.218 → 0.25 → 0.234 → **0.354** → 0.299 → 0.308 → 0.342 → 0.242 → 0.344

逆转原 hypothesis（预测最快 collapse），CKA-only 实际展示 active learning pattern，reward 在波动中持续维持高位，final 接近 peak，frac_zero_std 保持低位（0.2）。无异常。

---
