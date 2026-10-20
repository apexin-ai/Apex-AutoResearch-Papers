# code training dynamics gpu script

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_training-dynamics-gpu-script_20260515T144748_result.json`
- **Structured JSON:** [`3d75652488d1765951db.json`](../../sessions/3d/3d75652488d1765951db.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 Python 脚本 dry-run 验证通过。

3 个脚本已就绪：

| 脚本 | 路径 |
|------|------|
| Forward pass | `scripts/training_dynamics_forward.py` |
| 可视化 | `scripts/plot_training_dynamics.py` |
| Runner | `scripts/run_training_dynamics.sh` |

**运行方式**（GPU 空出后）：
```bash
bash scripts/run_training_dynamics.sh
```

依次对 6 个 checkpoint（Vanilla / TaxEI-full / Random-full / TaxEI-10% / TaxEI-25% / TaxEI-50%）做 forward pass，计算 per-sample response-token CE loss，按 clean/injected/per-operator 分类汇总，最后生成 3 张图到 `artifacts/training_dynamics/`。

---
