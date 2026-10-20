# eval matched seed 8b predictions

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_matched-seed-8b-predictions_20260512T172251_result.json`
- **Structured JSON:** [`32af16d1b7b5ea5f1eee.json`](../../sessions/32/32af16d1b7b5ea5f1eee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总结果：

**已完成 (本次生成)**：
| 文件 | Accuracy | 说明 |
|------|----------|------|
| `eval_cwm_seed0_with_preds_predictions.json` | 87.57% | 4B CWM seed0 per-instance predictions |
| `eval_cwm_seed456_with_preds_predictions.json` | 86.98% | 4B CWM seed456 per-instance predictions |

**已存在**：
- `eval_cwm_seed42_with_preds_predictions.json` — 4B CWM seed42
- `predictions_cls_seed{0,42,123,456,789}.jsonl` — 4B CLS 全部 5 seeds
- `predictions_traj_seed{0,42,123,456,789}.jsonl` — 4B TRAJ 全部 5 seeds

**可做 matched-seed error overlap 的 CLS-CWM 配对**: seed0, seed42, seed456 (3 对)

**缺失/阻塞**：
| 缺失项 | 原因 |
|--------|------|
| CWM seed123/789 per-instance preds | checkpoints 只在 seetacloud，home 上没有 |
| 8B CLS seed456 per-instance preds | checkpoint 在 home 但 GPU 被 `repo-level-cls-home` 训练占用 (PID 2840848, 19GB VRAM) |
| 8B CLS seed42/123 per-instance preds | checkpoints 只在 seetacloud |
| 8B CWM 全部 per-instance preds | checkpoints 只在 seetacloud |

**下一步选择**：
1. 杀掉 `repo-level-cls-home` 训练 → 可立即跑 8B CLS seed456 eval (~5分钟)
2. 等训练完 → 时间不确定（可能数小时）
3. 在 seetacloud 补跑 CWM seed123/789 和 8B predictions

---
