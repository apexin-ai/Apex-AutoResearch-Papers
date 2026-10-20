# analysis rp r2 trainer state metrics

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_rp_r2-trainer-state-metrics_20260514T213110_result.json`
- **Structured JSON:** [`a2f0c43948ad845e9b5e.json`](../../sessions/a2/a2f0c43948ad845e9b5e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## rp_r2 指标 (from trainer_state.json, checkpoint-20)

| Step | f1_reward | ced_reward | format | reward_mean | frac_zero_std | KL | grad_norm | loss |
|------|-----------|------------|--------|-------------|---------------|-----|-----------|------|
| 5 | 0.0211 | 0.0047 | 0.0731 | 0.0990 | 0.2 | 3.94e10 | 1.625 | 4.34e8 |
| 10 | 0.0000 | 0.0000 | 0.0934 | 0.0934 | 0.2 | 6.91e4 | 0.194 | 908.1 |
| 15 | 0.0031 | 0.0000 | 0.1459 | 0.1490 | 0.0 | 1.87e6 | 1.594 | 2.47e4 |
| 20 | 0.0017 | 0.0005 | 0.1448 | 0.1469 | 0.0 | 1.42e9 | 1.469 | 1.34e7 |

**严重问题**: KL 和 loss 数值极度异常——KL 在 1e4 ~ 1e10 量级剧烈振荡，loss 在 908 ~ 4.3e8 之间波动。正常 GRPO 训练 KL 应在 0~50 范围。这表明训练已经发散/崩溃。

f1_reward 和 ced_reward 几乎为 0，format_reward 从 0.073 缓慢上升到 0.145，说明模型只学到了一点格式但完全没学到任务内容。

## Wandb 状态
未连接（无 wandb 目录）

## 可用 Checkpoints
- `checkpoint-20` (step 20/200)

---
