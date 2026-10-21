# ops deploy analyze script

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_deploy_analyze_script_20260515T151857_result.json`
- **Structured JSON:** [`ef9aa9a932dd194a63e1.json`](../../sessions/ef/ef9aa9a932dd194a63e1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成：

- **脚本已部署**：`/root/cost-verify-agent-rl/analyze_training.py`
- **matplotlib 可用**：v3.10.5
- **dry-run 通过**：`--help` 正常输出

参数化改动：新增 `--name` 参数（默认 `experiment`），所有输出文件名和图表标题使用该参数，不再硬编码 exp026。

用法示例：
```bash
python3 /root/cost-verify-agent-rl/analyze_training.py \
  --log ~/runs/cost-verify-agent-rl/exp027_stable_grpo.log \
  --name exp027 \
  --output /root/cost-verify-agent-rl/analysis_output
```

---
