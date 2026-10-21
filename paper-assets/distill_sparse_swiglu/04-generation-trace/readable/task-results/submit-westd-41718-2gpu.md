# submit westd 41718 2gpu

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_westd-41718-2gpu_20260518T050223_result.json`
- **Structured JSON:** [`d477e86477b707d2cdc2.json`](../../sessions/d4/d477e86477b707d2cdc2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两张卡均已启动，正在运行 C4 PPL 评估：

| GPU | PID | 实验 | VRAM | 状态 |
|-----|-----|------|------|------|
| cuda:0 | 47644 | `c4_ood_kl30_s123` — KL 30% teal_global C4 OOD PPL | 41.7 GB | 已进入 C4 PPL 评估（mask 计算完成） |
| cuda:1 | 47970 | `c4_ood_dense_baseline` — Dense baseline C4 OOD PPL | 18.3 GB | 模型加载完成，已进入 C4 PPL 评估 |

预计时长：每个 job ~5-15 分钟（C4 validation PPL 评估，取决于 sample 数量）。

日志文件：
- `logs/c4_ood_kl30_s123.log`
- `logs/c4_ood_dense_baseline.log`

结果将输出到 `results/benchmark/{exp_id}/results.json`。

---
