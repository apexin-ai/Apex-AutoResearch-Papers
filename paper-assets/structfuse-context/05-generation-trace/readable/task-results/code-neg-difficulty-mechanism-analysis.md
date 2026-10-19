# code neg difficulty mechanism analysis

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_neg-difficulty-mechanism-analysis_20260515T231044_result.json`
- **Structured JSON:** [`64b1a55ca2396b738be1.json`](../../sessions/64/64b1a55ca2396b738be1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出已全部就绪。总结：

---

## 产出

| 文件 | 路径 |
|------|------|
| eval_trajectories.csv | `/root/autodl-tmp/structfuse/artifacts/neg_difficulty_analysis/eval_trajectories.csv` |
| 图表 PDF | `/root/autodl-tmp/structfuse/artifacts/neg_difficulty_analysis/overfitting_mechanism.pdf` |
| 图表 PNG | `/root/autodl-tmp/structfuse/artifacts/neg_difficulty_analysis/overfitting_mechanism.png` |

## eval_trajectories.csv

43 行（1 header + 42 eval records），覆盖 10 个 (model, strategy, seed) 组合：

| 模型 | 策略 | Seeds | Eval 点数 |
|------|------|-------|----------|
| Qwen | random | 42,43,44 | 9+3+3 |
| Qwen | embedding_distance | 43,44 | 3+4 |
| Qwen | dataflow_aware | 43 | 2 |
| StarCoder | random | 42,43,44 | 8+5+3 |
| StarCoder | embedding_distance | 42 | 2 |

缺失：Qwen embedding_distance_s42、所有 dataflow_aware 的 s42/s44、StarCoder dataflow_aware 全部（这些 runs 的 wandb 数据不存在）。

## Panel B: Margin vs Eval-Loss Slope 相关性

| 统计量 | 值 |
|--------|-----|
| **Pearson r** | **-0.60** |
| **p-value** | **0.069** |
| Spearman ρ | -0.43 |
| Spearman p | 0.215 |

方向正确：**lower margin（harder negatives）→ steeper eval loss increase（faster overfitting）**。Pearson 边缘显著 (p=0.069)，样本量受限（n=10）。

## 异常/说明

- Qwen random_s42 的 wandb 第一个 run (x4vmv7bj) 在 step 50 crash，数据来自重试 run (pthrowuk)
- StarCoder random_s43 有 3 个重试 runs，取 eval 点数最多的一个
- 多个 runs 只有 2-3 个 eval 点（early stopping 或训练仍在进行中）
- R@10 全为 1.0（pool size 太小，区分度不够）

---
