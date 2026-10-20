# ops sync and monitor v7

**collapse aware mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_sync_and_monitor_v7_20260513T172959_result.json`
- **Structured JSON:** [`ae624c3dd8c4c9648908.json`](../../sessions/ae/ae624c3dd8c4c9648908.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 汇总报告

### 1. 同步结果
- **31/31 文件传输成功**，0 失败
- 关键修复验证全部通过（5/5）：
  - `same_checkpoint_tie` in analyze_ngram_leading.py ✓
  - `config.max_steps` in pilot_pipeline.py ✓
  - `max_length.*2048` in analyze_generated_eff_rank.py ✓
  - `padding_side` in analyze_generated_eff_rank.py ✓
  - launch_baseline_w0_p0.sh 存在 ✓

### 2. v7 eval 状态：**已崩溃**
崩溃位置：`metrics.py:240` `compute_kl_divergence()`

```
ValueError: operands could not be broadcast together with shapes (50277,) (50254,)
```

- 训练阶段（G0/G1/G2）已全部完成，每个 group 有 checkpoint-76/152/228/304/305 + final_model
- eval 在 G2 的 KL divergence 计算阶段崩溃，原因是两个 checkpoint 的 token 分布数组 vocab size 不一致（50277 vs 50254）
- **G0/G1/G2 均无 metrics/ 目录**，说明 eval 在 G0 就崩了或 metrics 写入发生在所有 eval 完成之后

### 3. Checkpoint 路径列表

| Group | Path |
|-------|------|
| G0 | `/root/autodl-tmp/output_v7/G0/training/checkpoint-76` |
| G0 | `/root/autodl-tmp/output_v7/G0/training/checkpoint-152` |
| G0 | `/root/autodl-tmp/output_v7/G0/training/checkpoint-228` |
| G0 | `/root/autodl-tmp/output_v7/G0/training/checkpoint-304` |
| G0 | `/root/autodl-tmp/output_v7/G0/training/checkpoint-305` |
| G0 | `/root/autodl-tmp/output_v7/G0/final_model` |
| G1 | `/root/autodl-tmp/output_v7/G1/training/checkpoint-76` |
| G1 | `/root/autodl-tmp/output_v7/G1/training/checkpoint-152` |
| G1 | `/root/autodl-tmp/output_v7/G1/training/checkpoint-228` |
| G1 | `/root/autodl-tmp/output_v7/G1/training/checkpoint-304` |
| G1 | `/root/autodl-tmp/output_v7/G1/training/checkpoint-305` |
| G1 | `/root/autodl-tmp/output_v7/G1/final_model` |
| G2 | `/root/autodl-tmp/output_v7/G2/training/checkpoint-76` |
| G2 | `/root/autodl-tmp/output_v7/G2/training/checkpoint-152` |
| G2 | `/root/autodl-tmp/output_v7/G2/training/checkpoint-228` |
| G2 | `/root/autodl-tmp/output_v7/G2/training/checkpoint-304` |
| G2 | `/root/autodl-tmp/output_v7/G2/training/checkpoint-305` |
| G2 | `/root/autodl-tmp/output_v7/G2/final_model` |

共 **18 个 checkpoint**（3 groups × 5 training checkpoints + 3 final_models），另有 `real_data_cache/` 目录。

---
