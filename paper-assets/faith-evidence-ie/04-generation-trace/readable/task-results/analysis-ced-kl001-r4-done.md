# analysis ced kl001 r4 done

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_ced_kl001_r4_done_20260514T180750_result.json`
- **Structured JSON:** [`40049c97c20214f2eac2.json`](../../sessions/40/40049c97c20214f2eac2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 任务已提交。以下是完整总结：

## Training Summary
- **Steps completed**: 100/100, EXIT_CODE=0（正常结束）
- **Total training time**: 9069.88s ≈ **2h 31m**
- **Final metrics (step 100)**:
  | Metric | Value |
  |--------|-------|
  | reward | 1.195 |
  | f1_reward | 0.573 |
  | ced_reward | 0.328 |
  | format_reward | 0.293 |
  | frac_reward_zero_std | 0.2 |
  | kl | 0.118 |
  | loss | -0.009 |
  | grad_norm | 0.140 |
  | entropy | 0.067 |
  | completion_length_mean | 520.8 |

- **Best reward step**: **step 90** (reward=1.370, f1=0.720, ced=0.353)
- **Reward trajectory** (every 5 steps):
  `0.22 → 0.25 → 0.29 → 0.27 → 0.34 → 0.45 → 0.49 → 0.70 → 0.52 → 1.10 → 0.82 → 0.52 → 1.11 → 1.00 → 0.71 → 0.84 → 1.11 → 1.37 → 0.85 → 1.19`
- **Mode collapse**: No — frac_zero_std 从早期 0.3-0.8 降至后半程 0.0-0.2，diversity 良好
- **KL stability**: Stable — 快速上升到 ~0.12 后在 0.10-0.15 范围内波动，kl_coeff=0.01 控制有效
- **Conclusion**: ✅ 训练成功。Reward 从 0.22 增长到 1.1-1.4 区间，~5x 提升；KL 稳定低位；无 mode collapse

## Checkpoints
- **Available**: checkpoint-10, 20, 30, 40, 50, 60, 70, 80, 90, 100（全部 10 个）
- **已有 eval 覆盖**: 10, 20, 30, 40, 50, 60, 70, 80
- **缺失 eval**: 90, 100 → 已启动

## Eval launched
- **exp_id**: `mvp2_eval_ced_kl001_r4_last`
- **checkpoints**: 90, 100
- **GPU**: cuda:0
- **log**: `~/runs/faith-evidence-ie/mvp2_eval_ced_kl001_r4_last.log`

## W&B
- 此 run **未启用 W&B**（日志和服务器均无 wandb 记录）

---
