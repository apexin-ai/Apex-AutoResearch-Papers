# analysis taxei rp batch

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_taxei-rp-batch_20260516T060637_result.json`
- **Structured JSON:** [`8da4fda64eb6d68fcce3.json`](../../sessions/8d/8da4fda64eb6d68fcce3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

## 3 个 TaxEI-RP 训练实验结果

| exp_id | seed | train_loss | token_acc | duration | status |
|--------|------|-----------|-----------|----------|--------|
| v4-taxei-rp-s42 | 42 | **0.3847** | 0.9249 | 3h 46m 40s | SUCCESS |
| v4-taxei-rp-s123 | 123 | **0.3852** | 0.9137 | 3h 46m 30s | SUCCESS |
| v4-taxei-rp-s1 | 1 | **0.3853** | 0.9176 | 3h 46m 18s | SUCCESS |

**关键发现**：
- 3 个 seed 的 train_loss 极度一致（std=0.0003），训练稳定
- 无 eval_loss（未配置 eval split）
- 无 wandb（未配置）
- 唯一 warning 是 bitsandbytes 的 libnvJitLink.so.13（非关键，bnb 未使用）
- 每个实验保存了 3 个 checkpoint（epoch 1/2/3），final checkpoint 均为 `checkpoint-5415`

**已更新 registry**：`metrics`（train_loss, duration_minutes, token_acc 等）和 `spec.checkpoint_path`（指向 final checkpoint）。报告已注册为 artifact `art_20260516_ab31b3`。

---
