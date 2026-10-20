# diagnose exp 004 qwen7b

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp-004-qwen7b_20260517T175714_result.json`
- **Structured JSON:** [`1ce2033b10d271a8dd94.json`](../../sessions/1c/1ce2033b10d271a8dd94.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**实验没有失败。** 它已于 `2026-05-18 01:45:19` 成功完成，输出了 `EXP004_DONE` sentinel。

日志末尾的完整结果：

```
Problems: 60
SICA accuracy: 68.3% (41/60)
SC accuracy:   68.3% (41/60)
Extraction rate: 94.2%
Answer extraction: 100.0%
Total wall time: 30.6 min
Results saved to results/exp004_qwen7b/exp004_qwen7b_results.json
```

按数据集拆分：
- FOLIO: SICA=76.7%, SC=73.3% (n=30)
- ProofWriter: SICA=60.0%, SC=63.3% (n=30)

vLLM 也正常关闭，tmux session 留在完成状态。

关于"无 W&B metrics"和"无 sentinel file"：脚本本身没有 W&B 集成，sentinel 是 stdout 的 `EXP004_DONE`（已打印），结果文件在 `results/exp004_qwen7b/exp004_qwen7b_results.json`。之前的 5 次死亡可能是更早的尝试；当前这次运行是成功的。

```json
{"root_cause":"实验实际已成功完成。EXP004_DONE sentinel 已输出，结果文件已保存。之前的失败可能来自更早的运行尝试（如 conda 环境未激活），当前脚本已包含正确的 conda 激活逻辑并成功执行完毕。","error_type":"infrastructure","fix_steps":["无需修复，实验已成功完成","结果文件位于 results/exp004_qwen7b/exp004_qwen7b_results.json","如需 W&B 集成，需在 run_full_mvp.py 中添加 wandb 支持"],"can_auto_fix":false}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "实验实际已成功完成。EXP004_DONE sentinel 已输出，结果文件已保存。之前的失败可能来自更早的运行尝试（如 conda 环境未激活），当前脚本已包含正确的 conda 激活逻辑并成功执行完毕。",
    "error_type": "infrastructure",
    "fix_steps": [
      "无需修复，实验已成功完成",
      "结果文件位于 results/exp004_qwen7b/exp004_qwen7b_results.json",
      "如需 W&B 集成，需在 run_full_mvp.py 中添加 wandb 支持"
    ],
    "can_auto_fix": false
  }
}
```

</details>

---
