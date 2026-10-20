# data actor loss extract final

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_actor_loss_extract_final_20260515T104810_result.json`
- **Structured JSON:** [`1394718fbf8a16e6c828.json`](../../sessions/13/1394718fbf8a16e6c828.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出完成。

### 数据概览

| 实验 | 数据点 | Step 范围 | actor_loss 范围 |
|------|--------|-----------|----------------|
| exp_001_baseline | 51 | 5K–505K | [-0.4351, 0.0004] |
| exp_008d_subsample_on_h8 | 6 | 5K–55K | [-0.3367, -0.0726] |
| exp_009b_008d_walker_s2 | 11 | 5K–105K | [-0.3389, 0.0053] |
| exp_009e_008d_walker_s1 | 10 | 5K–95K | [-0.3367, 0.0109] |

### 趋势

- **exp_001 baseline**: 标准收敛曲线，从 -0.44 单调上升至 ~0 附近，约 150K 步后稳定在 [-0.001, 0] 区间振荡。
- **exp_008d (Pathway A collapse)**: 仅 6 个点即停止（55K），actor_loss 从 -0.34 回升到 -0.07 但未翻正，实验中断。
- **exp_009b (s2, self-correction)**: 在 ~75K 步翻正（-0.010 → +0.005），之后稳定在 +0.002 附近，confirmed self-correction。
- **exp_009e (s1, 翻正现象)**: 在 ~85K 步翻正（-0.009 → +0.011），幅度比 009b 更大，仍在运行中。

文件: `artifacts/figures/data/actor_loss_data.json`，已注册为 artifact `art_20260515_67a2d2`。

---
