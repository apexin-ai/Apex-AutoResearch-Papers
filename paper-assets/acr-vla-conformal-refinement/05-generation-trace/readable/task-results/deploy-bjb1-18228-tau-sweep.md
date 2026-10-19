# deploy bjb1 18228 tau sweep

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_bjb1-18228-tau-sweep_20260528T001622_result.json`
- **Structured JSON:** [`16a4568676d19a172ddc.json`](../../sessions/16/16a4568676d19a172ddc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

tau040、tau045 和 crm-always-on-goal-s46 都已在 registry 中标记为 RUNNING。

**部署总结：**

| 实验 | GPU | 状态 |
|------|-----|------|
| smolvla-tau040-long-s42 | GPU 0 | 已在运行（之前提交） |
| smolvla-tau045-long-s42 | GPU 1 | 已在运行（之前提交） |
| crm-always-on-object-s45 | GPU 2 | 已在运行（之前提交） |
| **crm-always-on-goal-s46** | **GPU 3** | **刚启动，PID=944319** |
| crm-always-on-long-s45 | — | 无空闲 GPU，待上述实验完成后提交 |

4 个 GPU 全部占满。`crm-always-on-long-s45` 需等任一实验结束后再提交。

---
