# code c1 ablation bce kl targets

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_c1-ablation-bce-kl-targets_20260518T144952_result.json`
- **Structured JSON:** [`f6d6391b80c854f22c2b.json`](../../sessions/f6/f6d6391b80c854f22c2b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已提交并运行中。总结：

**C1 因果消融实验已启动** (westd-41718 GPU 1)

- **exp_id**: `c1_ablation_bce_kl_targets_s42`
- **脚本**: `src/train_bce_kl_targets.py` + `src/generate_kl_oracle_masks.py`（验证用）
- **设计**: 加载冻结的 50% KL predictor 生成 binary oracle masks，训练新 BCE predictor 去拟合这些 masks，Lagrangian sparsity constraint 与 KL 训练相同
- **关键参数**: 1000 steps, bs=4, seq_len=2048, lr=1e-3, seed=42
- **日志**: `logs/c1_ablation_bce_kl_targets_s42.log`
- **Checkpoint**: `checkpoints/c1_ablation_bce_kl_targets_s42/predictor_bce_kl_targets.pt`
- **训练后自动 eval**: WikiText-2 PPL

**早期指标** (step 100): BCE loss 已从 0.692 降至 0.110，oracle agreement 达到 95.6%，说明新 predictor 正在成功学习 KL masks 的 pattern。

**Mask 验证发现**: KL masks 与 magnitude-based masks 只有 ~53% agreement，说明 KL distillation 确实学到了不同于简单 magnitude ranking 的 mask 策略。

预计 ~15 分钟后完成训练 + eval，PPL 结果将决定 gradient coupling vs target quality 的因果归因。

---
