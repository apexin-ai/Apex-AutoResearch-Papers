# code auto eval on complete

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_auto-eval-on-complete_20260514T001531_result.json`
- **Structured JSON:** [`8304461554e4f90df0bf.json`](../../sessions/83/8304461554e4f90df0bf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个验证场景全部通过：

1. **无参数** → 打印 `Usage: ./auto_eval_on_complete.sh &lt;exp_id> &lt;gpu_id>`，exit 1
2. **错误 exp_id** → 打印 `Unknown exp_id: bad-id` + 可用列表，exit 1
3. **`cwm-v12 2`** → 正确映射到 checkpoint 目录和 formulation，成功调用 `run_repo_eval.sh`。因训练未完成（checkpoint 目录缺少 `config.json` 的 `model_type`），在模型加载阶段报错退出——路径和参数传递均正确。

脚本已创建在 `/home/sonny/exec-sim-repair-verifier/auto_eval_on_complete.sh`，可直接使用。

---
