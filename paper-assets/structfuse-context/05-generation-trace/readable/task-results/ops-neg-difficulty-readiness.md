# ops neg difficulty readiness

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_neg-difficulty-readiness_20260515T230428_result.json`
- **Structured JSON:** [`0030ecaec4fb6e74f483.json`](../../sessions/00/0030ecaec4fb6e74f483.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。汇总如下：

---

## 就绪状态

### 已有脚本
| 脚本 | 功能 | 状态 |
|------|------|------|
| `/root/structfuse/scripts/plot_neg_difficulty.py` | 读 stats_v2/v3 JSON，生成 3 图：margin_comparison, similarity_dist, ratio_heatmap | **已跑完，artifacts 已生成** |
| `/root/structfuse/evaluation/plot_neg_difficulty.py` | hardcoded STATS，生成 KDE 分布 + margin bar chart | **已跑完** |

### 已有数据
| 文件 | 内容 |
|------|------|
| `negative_difficulty_stats_v2.json` (128t) | qwen/starcoder × 3 策略：n_pairs, pos_sim, neg_sim, margin (mean/std/median/p25/p75/min/max), pct_positive_margin |
| `negative_difficulty_stats_v3_2048.json` (2048t) | 同上，加 max_length 字段 |

### 已有 artifacts（全部已生成）
- `neg_difficulty_analysis/chart/` — margin_comparison, similarity_dist, ratio_heatmap (pdf+png) ✓
- `figures/` — neg_difficulty_distribution (pdf+png+thumb) ✓

---

## 新分析（dataflow 加速过拟合机制解释）需要新脚本

**已有的 difficulty 数据（Qwen 2048t）：**

| Strategy | margin_mean | pct_positive_margin |
|----------|------------|---------------------|
| random | 0.0743 | 81.8% |
| dataflow | 0.0293 | — |
| embedding | 0.0170 | — |

**已有的训练动态数据（from m2_eval_summary.md）：**

| Subrun | Best R@1 | Best Step | Overfitting pattern |
|--------|----------|-----------|---------------------|
| dataflow_s43 | 0.5495 | 500 | R@1 dropped to 0.5174 @step1000, **-3.21pp in 500 steps** |
| random_s42 | 0.5527 | 1000 | slow decay, ran 4000 steps |
| random_s43 | 0.5554 | 1500 | stopped at peak |
| embed_s43 | 0.5606 | 1500 | stopped at peak |

**缺失：** 完整的 per-step eval 轨迹（每 500 步的 R@1 和 val_loss）。这些数据在 wandb offline logs（`.wandb` 二进制文件）中，没有 CSV/JSON 导出。服务器上有 7 个 offline runs 在 `/root/structfuse/wandb/`。

### 需要新脚本做两件事

1. **从 wandb offline runs 提取 per-step eval metrics**：用 `wandb` Python API 读取 `.wandb` 文件，导出 `{step, val_loss, recall@1}` per strategy/seed
2. **生成 overfitting-rate vs difficulty 关联图**：
   - Panel A: 训练曲线对比（R@1 vs step, 多策略叠加）
   - Panel B: scatter plot / bar chart — margin_mean vs overfitting rate (peak R@1 衰减速度 pp/step)

**输入数据：**
- wandb offline runs → per-step eval 轨迹
- stats_v3_2048.json → difficulty 特征
- m2_eval_summary 中的 summary metrics 作为 fallback

是否需要我写这个脚本并在服务器上跑？

---
