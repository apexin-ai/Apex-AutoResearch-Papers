# code config merge rootfix

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_config-merge-rootfix_20260513T200401_result.json`
- **Structured JSON:** [`4d0b33fabbfc90d71bbf.json`](../../sessions/4d/4d0b33fabbfc90d71bbf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。验证结果汇总：

### 修复内容
`parse_args()` 的 config merge 改为 Method A：YAML 值通过 `parser.set_defaults()` 注入，然后二次 `parse_args()` 让 CLI 参数可覆盖。同时添加了 `os.environ["WANDB_MODE"] = "disabled"`、`JSONLLogCallback`、`logging_steps` 可配置参数。

### 3 步验证结果

| 检查项 | exec-only | exec-sta |
|--------|-----------|----------|
| `no_wandb` = True | ✅ | ✅ |
| 3 步无 crash | ✅ | ✅ |
| `training_log.jsonl` 条数 | 4 条（3 step + 1 summary）| 4 条 |
| reward 值合理 | 0.25 / 0.0 / 0.375 | 0.25 / 0.0 / 0.375 |
| parse_rate | 1.0 | 1.0 |
| prove_rate | 0.208 | 0.208 |

---
