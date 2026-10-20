# analysis stale analyzing cleanup

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_stale_analyzing_cleanup_20260525T035721_result.json`
- **Structured JSON:** [`f995d6152e813df6aebb.json`](../../sessions/f9/f995d6152e813df6aebb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

5 个实验全部推进到 DONE。汇总：

| 实验 | Conclusion | 关键指标 | 备注 |
|------|-----------|---------|------|
| **d158_1_7b_rsft_s44_train** | success | loss=0.526, acc=0.879, 567 steps/3 epochs | 正常收敛 |
| **d158_1_7b_rsft_s44_eval** | success | **ign_f1=47.30**, evi_f1_joint=38.97, edcr=63.68 | 比 plan019 共享SFT的 51.09/51.25 低约 3.8 点，seed-matched pipeline 性能偏低 |
| **r3_grpo_bf16_g4** | success | reward=1.02, f1_reward=0.68, ced_reward=0.17 | 100 steps 完成，50% clipped_ratio 偏高 |
| **r3_grpo_bf16_g4_eval** | success | **ign_f1=29.17** > 10, no collapse | 确认 bf16 G=4 不 collapse，quantization 是 collapse 主因 |
| **test_eval_4b_rsft_s44_no_evi_v2** | killed → DONE | — | 直接关闭 |

关注点：
- **d158_1_7b_rsft_s44_eval** 的 ign_f1=47.30 显著低于共享 s42 SFT 的 plan019 结果（51.09/51.25），差距约 3.8 点，可能意味着 seed-matched SFT 初始化确实影响了 variance estimate
- **r3_grpo_bf16_g4_eval** 的 ign_f1=29.17 远高于 collapse 阈值 10，确认 quantization 是 collapse 根因；但绝对值远低于 RSFT baseline（~51），GRPO 100 steps 尚未充分优化

---
