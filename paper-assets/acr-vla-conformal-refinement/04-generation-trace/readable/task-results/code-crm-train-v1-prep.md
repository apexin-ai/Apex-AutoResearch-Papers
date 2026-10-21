# code crm train v1 prep

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_crm-train-v1-prep_20260513T201510_result.json`
- **Structured JSON:** [`ebcffa533981aa09feb5.json`](../../sessions/eb/ebcffa533981aa09feb5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已注册。汇总结果：

---

## Cache 验证 ✓

| Benchmark | Samples | obs_features | k_samples | expert_actions |
|-----------|---------|-------------|-----------|----------------|
| spatial | 12,167 | [12167, 960] f32 | [12167, 10, 5, 6] f32 | [12167, 5, 6] f32 |
| object | 14,570 | [14570, 960] f32 | [14570, 10, 5, 6] f32 | [14570, 5, 6] f32 |
| **总计** | **26,737** | | | |

Cache 完整，所有 manifest、merged tensors、sample counts 一致，264MB。

## CRM 训练已运行 ✓

| 字段 | 值 |
|------|-----|
| exp_id | `crm-train-v1` |
| server | bjb1-18228, cuda:1 |
| PID | 78520 |
| 模型 | CRM MLP 337,438 params (1030D→256→256→30D) |
| 训练参数 | epochs=50, batch=32, lr=1e-3, K=10, seed=42 |
| 日志 | `~/runs/acr-vla-conformal-refinement/crm-train-v1.log` |
| Checkpoints | `/root/autodl-tmp/checkpoints/crm/` |

当前进度：**Epoch 3/50**, train_loss=0.025, val_loss=0.014（持续下降）。

## 注意事项

1. 该训练是之前通过 agent-ml 框架提交的（PID 78520, 04:10 启动），我的重复 tmux session 已杀掉，避免 GPU 竞争。
2. 同一服务器上还有 `precompute-k5` 在 cuda:3 上跑（K=5 ablation precompute），不冲突。

---
