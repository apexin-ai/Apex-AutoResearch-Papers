# check scoring ablation magnitude 20 progress

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_scoring_ablation_magnitude_20_progress_20260518T042442_result.json`
- **Structured JSON:** [`e8591a82f869715c44a2.json`](../../sessions/e8/e8591a82f869715c44a2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**scoring_ablation_magnitude_20 状态：**

| 项目 | 状态 |
|------|------|
| tmux session | 活跃 |
| PID | 766802 |
| 当前阶段 | Step 2/2: GSM8K eval |
| Step 1 (剪枝) | 已完成，actual sparsity 18.99% |
| GPU | cuda:0, 13GB/98GB, 78% util |

**进度：97/200 samples (48.5%)**

- 平均速度：~56.5s/sample
- 已用时间：~1h30m
- 剩余 103 samples × 56.5s ≈ **97 分钟（约 1h37m）**
- 预计完成时间：约 **14:02 (UTC)**

**异常：acc=0.0000 (50 samples 检查点时)**，eos_rate 仅 2%，avg_len=4054（接近 max_length）。Magnitude pruning 在 20% sparsity 下严重破坏了模型推理能力，生成几乎全部达到长度上限且无法产出正确答案。

---
