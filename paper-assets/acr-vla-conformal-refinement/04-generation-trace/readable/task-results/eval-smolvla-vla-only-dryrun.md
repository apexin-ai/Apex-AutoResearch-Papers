# eval smolvla vla only dryrun

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_smolvla-vla-only-dryrun_20260522T193038_result.json`
- **Structured JSON:** [`5ca1d6660ee5b4779997.json`](../../sessions/5c/5ca1d6660ee5b4779997.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Dry Run 报告

| 项目 | 结果 |
|------|------|
| **状态** | 成功 |
| **Overall success rate** | 100.0% (10/10 tasks) |
| **执行耗时** | ~18 分钟（10 tasks × 1 rollout each, 280 max steps） |
| **GPU 显存峰值** | ~11.3 GB（运行中稳定 ~5.6 GB，进程已释放） |
| **错误/警告** | 无错误。仅 1 个无害 DeprecationWarning（`swigvarlink has no __module__`） |

10 个 task 全部 1/1 成功，eval pipeline 正常工作。JSON 已保存到 `logs/eval_object_vla_only_seed42.json`。

注意：n_rollouts=1 的 100% 成功率不代表实际性能——object suite 本身较简单，且单次 rollout 有随机性。正式 eval 需 n_rollouts=20。CRM eval 部署就绪，无阻塞问题。

---
