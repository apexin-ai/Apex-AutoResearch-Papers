# code fix server pretrain

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_server_pretrain_20260514T133943_result.json`
- **Structured JSON:** [`eb65fd0100d90f36297f.json`](../../sessions/eb/eb65fd0100d90f36297f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证结果：

| 检查项 | 结果 |
|--------|------|
| n_min 默认值 = `max(2, args.batch_size // 2)` | 第280行，正确 |
| 无 EMA 代码 | grep "ema" 返回空（exit code 1），确认无 EMA |
| unweighted_loss 日志 | 第130/158/191行，存在 |
| WeightedTrainer.__init__ 无 ema_alpha 参数 | 第92行：只有 `weighting_method, tau, n_min, grid_b_value, log_path` |

服务器代码已修复完成。

---
