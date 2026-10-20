# code plan001 exec only s42 r4

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan001-exec-only-s42-r4_20260513T230425_result.json`
- **Structured JSON:** [`9fa6da026687600f5fbe.json`](../../sessions/9f/9fa6da026687600f5fbe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

| Run | 状态 | 原因 |
|-----|------|------|
| r1 | 失败 | 参数错误 `--max_steps`（应为 `--num_steps`） |
| r2 | **正在运行** | PID 84901，GPU 0，当前 step 179/500 |
| r3 | 失败 | r2 已占满 GPU 0，重复提交导致 OOM |

**r2 运行正常**，当前进度 179/500，reward_mean=0.75，prove_rate=0.75，loss=0.0608。已保存 checkpoint-100 和 checkpoint-150。

不需要提交 r4。plan001-exec-only-s42 实验已在正常训练中，预计还需约 320 步完成。GPU 1 上同时在跑 plan005-sta-low-s42（exec_weight=0.9, sta_weight=0.1）。

---
