# diagnose unified crm k check

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_unified-crm-k-check_20260522T112635_result.json`
- **Structured JSON:** [`678f54b7ad06b0a9ebdc.json`](../../sessions/67/678f54b7ad06b0a9ebdc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程已 kill。

## 总结

1. **`--mode obs_only` 缺失** — 已 kill PID 317054。
2. **K 值不一致** — Long suite 的 cache 是 K=2（其他都是 K=10）。**不能直接重启**，因为混合训练数据的 K 不一致会导致模型学到错误的 pattern。

**等 Director 决策：**
- 选项 A：重新生成 Long 的 cache（K=10），然后再启动 unified training
- 选项 B：所有 suite 统一用 K=2 重新生成 cache
- 选项 C：仅用 object/spatial/goal（K=10）三个 suite 先训练，Long 后补

---
