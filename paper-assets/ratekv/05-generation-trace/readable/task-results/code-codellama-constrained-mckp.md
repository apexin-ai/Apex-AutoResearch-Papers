# code codellama constrained mckp

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_codellama_constrained_mckp_20260516T031236_result.json`
- **Structured JSON:** [`8ee628848882bf3277a9.json`](../../sessions/8e/8ee628848882bf3277a9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

模型加载完毕，WikiText-2 数据集已找到，正在跑 BF16 baseline PPL eval。任务正常运行中，预计 ~20-30min 全部完成。

完成情况总结：
- `run_codellama_constrained_mckp.py` 已编写并部署到服务器
- Dry-run (`--help`) 通过
- 已用 `submit_training_job` 提交到 `cuda:1`，exp_id: `codellama_constrained_mckp`
- 当前状态：模型已加载，正在跑 5 轮 PPL eval（BF16 → Uniform → Constrained → Unconstrained → Greedy）
- 日志：`~/runs/ratekv/codellama_constrained_mckp.log`
- 结果输出：`/root/ratekv/artifacts/codellama_constrained_mckp_results.json`

---
