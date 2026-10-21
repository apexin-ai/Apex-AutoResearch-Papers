# ssh full status sync

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_full-status-sync_20260515T005356_result.json`
- **Structured JSON:** [`0d5165d31f19a2cb3be4.json`](../../sessions/0d/0d5165d31f19a2cb3be4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

### GPU 占用
| GPU | 显存占用 | 利用率 | 实验 |
|-----|---------|--------|------|
| 0 | 13645 MiB | 47% | GRPO 训练 |
| 1 | 23195 MiB | 88% | RSFT 生成 |
| 2 | **0 MiB** | **0%** | ckpt80 eval 已结束 |
| 3 | 10653 MiB | 82% | ckpt100 eval |

---

### 实验 1: mvp2_grpo_ced_lr5e6_r1 — **ALIVE** (5h14m)
- **进度**: 183/200 steps (92%)，~25min 完成
- 已保存 checkpoint: 20, 40, 60, 80, 100, 120, 140, 160, 180
- 最近 step 指标下降趋势：
  - reward: 0.453 → 0.281
  - f1_reward: 0.060 → 0.014
  - ced_reward: 0.107 → 0.015
  - format_reward: 0.286 → 0.252
- **WARNING**: KL divergence 极大（step 5 时 2.4B，step 30 时 70T），仅监控未停止

### 实验 2: mvp2_rsft_generate — **ALIVE** (44min，**新启动**)
- **进度**: 83/1514 batches (5%)，预计 ~14h 完成
- **前 100 样本监控**：
  - format_ok_rate: **99.6%**
  - truncation_rate: **9.2%**
  - mean_diversity: **0.9/8** ⚠️ 极低，8 次生成几乎完全相同
- 无输出文件路径/大小信息（尚在生成中）

### 实验 3: mvp2_eval_lr5e6_r1_ckpt100 — **ALIVE** (1h14m)
- **进度**: 47/62 batches (76%)，~24min 完成
- 结果待产出

### 实验 4: mvp2_eval_lr5e6_r1_ckpt80 — **已完成** ✓
- 日志文件不存在（路径无 `mvp2_eval_lr5e6_r1_ckpt80.log`）
- 结果路径: `/root/autodl-tmp/eval_results/lr5e6_r1_ckpt80/checkpoint-80/`
- **关键指标**：
  - **rel_f1: 0.0116** ⚠️ 灾难性低
  - ign_f1: 0.0116
  - precision: 0.0109, recall: 0.0124
  - pred_count: 13828 vs gold_count: 12151（预测数量级正确但几乎全错）
  - **evi_f1: 0.828**（evidence 本身还行）
  - evi_precision: 0.928, evi_recall: 0.748
  - format_ok_rate: 99.9%
  - field_compliance: 78.8%
  - truncated: 210/985
  - inference_time: 6099s (~1h42m)

**关键发现**：ckpt80 的 rel_f1 只有 1.2%，模型能正确输出格式和找到 evidence，但关系抽取几乎完全失败。结合 GRPO 训练中 reward 持续下降和 KL 爆炸，训练可能已经崩溃。RSFT 生成的 diversity 0.9/8 也印证模型输出高度退化。

---
