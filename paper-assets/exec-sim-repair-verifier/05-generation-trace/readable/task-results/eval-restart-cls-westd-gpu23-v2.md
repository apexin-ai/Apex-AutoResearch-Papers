# eval restart cls westd gpu23 v2

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_restart-cls-westd-gpu23-v2_20260514T015218_result.json`
- **Structured JSON:** [`f074167beeadf4c938a1.json`](../../sessions/f0/f074167beeadf4c938a1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 eval 都已成功启动并在运行：

| Session | GPU | 显存占用 | 状态 |
|---------|-----|---------|------|
| `eval_cls_v5` | GPU 2 | 15565 MiB, 100% util | 模型已加载，推理中 |
| `eval_cls_8b` | GPU 3 | 13095 MiB, 7% util | 模型刚加载完 |

- 数据：9784 样本（pass: 7138, fail: 2646）
- 8B 的 module name 警告可忽略，不影响推理
- 预计 4B ~28 分钟，8B 稍慢
- 结果将分别输出到 `results/repo_cls_v5_conda_eval/` 和 `results/repo_cls_8b_conda_eval/`

---
