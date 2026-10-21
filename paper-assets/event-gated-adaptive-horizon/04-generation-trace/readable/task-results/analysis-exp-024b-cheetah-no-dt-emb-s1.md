# analysis exp 024b cheetah no dt emb s1

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_024b_cheetah_no_dt_emb_s1_20260518T015359_result.json`
- **Structured JSON:** [`8c10f1c810cec0ae3ef6.json`](../../sessions/8c/8c10f1c810cec0ae3ef6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已完成（EXIT_CODE=0）。日志显示最后一个 eval 在 step 105000，训练数据收集到 112000。

## exp_024b_cheetah_no_dt_emb_s1 分析结果

### 关键指标
- eval_return_final: 77.3
- eval_return_peak: 129.6
- peak_step: 15000
- NVE_peak: 0.10×
- civo: False

### 训练曲线概述
eval_return 在 15K 时达到峰值 129.6，随后下降并在 35K-55K 区间低迷（39.0-66.6），之后缓慢回升至 85K-95K（104.5-114.1），最终 105K 回落至 77.3。全程远低于 baseline 水平（548.3），曲线呈低幅波动而非 CIVO 式的"先升后崩"。gate_dt 全程锁死在 dt=2（gate_dt_2_frac=1.0），civo/alert 始终为 0.0。

### 结论
conclusion: **partial success**（假设部分成立）
理由: 去掉 trained dt_emb 后确实未触发 CIVO（NVE=0.10×，远低于 1.5× 阈值），证实 trained dt_emb 是 Cheetah CIVO 的必要条件。但 eval_return 远低于 baseline（77.3 vs 548.3，仅为 baseline 的 14%），说明 dt_embed_dim=0 导致 gate 锁死在 dt=2，agent 完全丧失了自适应 horizon 能力，性能严重退化。假设中"表现接近健康 baseline"的预期未满足。

### 与因果三角对比
| 实验 | 配置 | eval_final | NVE | CIVO |
|------|------|-----------|-----|------|
| 023a/b baseline | vanilla | 548.3(mean) | - | No |
| 010b trigger | trained dt_emb | 51.7 | 8.27× | Yes |
| 024b s1 (本实验) | no dt_emb | 77.3 | 0.10× | No |

### checkpoint_path
- `/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_024b_cheetah_no_dt_emb_s1/checkpoint_25000.pt`
- `/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_024b_cheetah_no_dt_emb_s1/checkpoint_75000.pt`
- `/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_024b_cheetah_no_dt_emb_s1/latest.pt`

---
