# diagnose stale running experiments

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_stale-running-experiments_20260521T100154_result.json`
- **Structured JSON:** [`86a25a98d9c0d8792d30.json`](../../sessions/86/86a25a98d9c0d8792d30.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Summary written to `artifacts/worker_output.md`.

**核心结论**：

- **13/14 已完成**：可立即 harvest 到 registry（SR 范围 7%–73%）
- **1/14 已死**：`eval-openvla-object-baseline-seed42` timeout + ImportError，重跑前需修 transformers
- **意外发现 1（π0.5）**：bjb1-32546 上 6 个 π0.5 vla_only 实验运行中（object/spatial × seed 42/43/44），**但 checkpoint 加载有 376 missing keys，前几个 task 全 0% SR**，建议立即 kill 修 bug 再重启
- **意外发现 2**：bjb1-18228 上还有 3 个 crm_obs_only 实验（seed 55/76/77）刚启动 ~8 分钟，未在 registry 中

---
