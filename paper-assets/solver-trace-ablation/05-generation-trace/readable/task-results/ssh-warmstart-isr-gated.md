# ssh warmstart isr gated

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_warmstart-isr-gated_20260516T151431_result.json`
- **Structured JSON:** [`7601e38c8e51f13e24bd.json`](../../sessions/76/7601e38c8e51f13e24bd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告：Warmstart Dry-Run 结果

### 1. 可用 Checkpoint
| 路径 | 说明 |
|------|------|
| `/root/autodl-tmp/outputs/plan001_exec_only_s43_1000_r2/` | exec-only s43, 1000步, 合并模型 |
| `/root/autodl-tmp/outputs/plan001_exec_only_s44_1000_r2/` | exec-only s44, 1000步, 合并模型 |

### 2. 配置文件
已创建 `configs/grpo_isr_gated_warmstart.yaml`（含 gradient_checkpointing=true，使用 train_500_seed42.jsonl 遵循 C001）。

### 3. Dry-Run 结果 — **阻塞：无法继续提交**

| 指标 | Step 1 | Step 2 |
|------|--------|--------|
| prove_rate | 1.000 | 0.000 |
| isr | 0.750 | 0.000 |
| gate_pass | 1.000 | — |
| reward | 1.000 | 0.000 |
| **grad_norm** | **0.0** | — |
| **reward_std** | **0.0** | — |
| entropy | 0.00014 | — |
| completion length | 31/31/31 (min/mean/max) | — |

**根因**：exec-only 训练 1000 步后模型 entropy 已 collapse（0.00014）。K=8 生成完全相同（31 token），reward 无方差 → GRPO 零梯度。这与 curriculum 失败是同一个问题的镜像——一边是 reward 全 0（模型不会 prove），另一边是 reward 全 1（模型太会 prove）。

### 4. 未提交双卡训练

按当前配置提交无意义（梯度恒为零）。

### 可能的解法
1. **加 temperature 参数**（如 1.5-2.0）打破 deterministic generation，需改 `train_grpo.py` 向 GRPOConfig 传 `temperature`
2. **用 additive_bonus + ISR**（连续 reward 替代 binary gate），使即使相同 prove 结果也有不同分值
3. **用更早期 checkpoint**（如 step 200-300 时 entropy 还没 collapse）— 但已被清理
4. **KL penalty 对 base model** 防止进一步 collapse

如何处理？

---
