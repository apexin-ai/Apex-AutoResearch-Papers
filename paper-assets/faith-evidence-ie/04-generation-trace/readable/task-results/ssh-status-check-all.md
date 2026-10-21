# ssh status check all

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_status-check-all_20260515T010407_result.json`
- **Structured JSON:** [`4679e4e611747966e7ed.json`](../../sessions/46/4679e4e611747966e7ed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态汇报

### 1. GRPO 训练 `mvp2_grpo_ced_lr5e6_r1` — 运行中 188/200 (94%)

| 指标 | 值 |
|------|-----|
| 进度 | 188/200 steps |
| ETA | ~20 min (约 100s/step × 12 steps) |
| GPU | cuda:0, 48% util, 13.6/32.6 GB |

最近两个 step 的关键指标（reward 在下降）：

| 指标 | step ~150 | step ~155 |
|------|-----------|-----------|
| reward | 0.453 | 0.281 |
| format_reward | 0.285 | 0.252 |
| f1_reward | 0.060 | 0.014 |
| ced_reward | 0.107 | 0.015 |
| kl | 0.013 | 0.036 |
| frac_reward_zero_std | 0.4 | 0.3 |

KL divergence warning 持续触发（极大值，仅监控未停止）。Reward 在后期明显下降，可能出现了训练不稳定。

---

### 2. Eval ckpt-100 `mvp2_eval_lr5e6_r1_ckpt100` — 运行中 54/62 (87%)

| 指标 | 值 |
|------|-----|
| 进度 | 54/62 batches |
| ETA | ~13 min (~95s/batch × 8 batches) |
| GPU | cuda:3, 64% util, 11.2/32.6 GB |

metrics.json 尚未生成，预计 ~13 分钟后完成可读取结果。

---

### 3. RSFT 生成 `mvp2_rsft_generate` — 运行中 104/1514 (6.9%)

| 指标 | 值 |
|------|-----|
| 进度 | 104/1514 batches, 200+ docs, 1632 lines |
| ETA | **~14.6 小时** (~37s/batch) |
| GPU | cuda:1, 81% util, 23.2/32.6 GB |

**Diversity 依然极低：**

| 区间 | format_ok | truncation | diversity |
|------|-----------|------------|-----------|
| docs 1-101 | 99.6% | 9.2% | **0.9/8** |
| docs 102-201 | 99.8% | 9.9% | **1.0/8** |

diversity 从 0.9 微升到 1.0，但仍然极低（8 个 generation 里平均只有 ~1 个不同输出）。这意味着模型几乎在 deterministic 输出，RSFT 的 rejection sampling 没有足够的多样性来筛选好样本。

---
