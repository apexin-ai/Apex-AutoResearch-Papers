# diagnose scoring ablation magnitude 20

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_scoring_ablation_magnitude_20_20260518T055326_result.json`
- **Structured JSON:** [`9112da867ad2c4310f94.json`](../../sessions/91/9112da867ad2c4310f94.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

**失败根因**：timeout 不足。eval 每条样本需 ~56.6s，200 条需 ~11,320s + prune 40s ≈ 11,360s，但 timeout 仅 10,862s，差约 500s（~11 条样本）。

**Prune 阶段**：完成。耗时 ~40s（10:51:14 → 10:51:52），实际稀疏度 18.99%。

**Eval 阶段**：完成 189/200（94.5%），在 sample 189 处被 SIGTERM 杀死。中间指标：
| 进度 | acc | eos_rate | avg_len |
|------|-----|----------|---------|
| 50/200 | 0.00 | 2.00% | 4054 |
| 100/200 | 0.02 | 2.00% | 4046 |
| 150/200 | 0.04 | 1.33% | 4063 |

**可复用中间产出**：pruned model checkpoint 完整存在于 `/root/autodl-tmp/recovery_aware_struct_prune/pruned_magnitude_20/`（12.3GB safetensors + config + tokenizer）。无需重跑 prune。

**无 W&B 日志**。无 eval 部分结果文件（进程被杀前未写出）。

**无 error/OOM/异常**，推理过程正常但极慢。

**建议**：
1. **重跑时只跑 eval**，直接加载已有 checkpoint，省去 prune 时间
2. **timeout 提至 14400s（4h）**——给足余量
3. **更根本的问题**：acc=4%、eos_rate=1.33%、avg_len≈4063 说明 pruned model 几乎不产生 EOS，每条都跑满 max_new_tokens。如果其他 ablation 也这样慢，考虑降低 `max_new_tokens`（如 2048）来加速，或接受这就是 magnitude pruning 在 20% 稀疏度下的退化表现

---
