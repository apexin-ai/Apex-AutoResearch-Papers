# ssh d048 cwm eval dryrun retry

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_d048-cwm-eval-dryrun-retry_20260513T091634_result.json`
- **Structured JSON:** [`ddeb4dbca52dc61eb462.json`](../../sessions/dd/ddeb4dbca52dc61eb462.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## CWM v9 ckpt-400 Eval（100条 dry-run）结果

| 指标 | 值 |
|------|-----|
| **Unparseable** | **76/100 (76%)** — 从 93% 降到 76%，仍然很高 |
| Accuracy | 75.0%（majority baseline 83.0%，**低于 baseline -8pp**）|
| F1 macro | 60.18% |
| F1 fail | 35.9% |
| F1 pass | 84.5% |
| Truncated | 6/100 |
| Gen length (chars) | mean=1204, median=1155, max=1664 |

**核心问题**：模型学到了生成完整 pytest 执行 trace（进度条 `.... [ 2%]`、test session starts 等），而不是直接输出 pass/fail。256 token 只够生成 trace 的一部分，大部分在 trace 中段被截断，parser 找不到 pass/fail 关键词。

**解决方向**（二选一或组合）：
1. **增大 max_new_tokens**（512 或 1024），让 trace 完整生成到末尾的 PASSED/FAILED
2. **改 system prompt**，明确要求"只输出 pass 或 fail，不要模拟执行过程"——但这样 CWM 的 execution simulation 特性就丧失了
3. **改 parser**，在 trace 中检测 `F` 或 `FAILURES` 等中间特征（如 index=4 就是靠检测到 `FAILURES` 成功解析的）

---
