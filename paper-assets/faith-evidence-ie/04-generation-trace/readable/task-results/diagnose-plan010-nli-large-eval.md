# diagnose plan010 nli large eval

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_plan010_nli_large_eval_20260519T232246_result.json`
- **Structured JSON:** [`cffadd926a1dda9688de.json`](../../sessions/cf/cffadd926a1dda9688de.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

找到根因了。`plan010_nli_large_ablation.log` 揭示了真相：

**EXIT_CODE=2 来自 `plan010_nli_large_ablation` 脚本的 Step 3，不是当前的 `plan010_nli_large_eval` 任务。**

ablation 日志末尾：
```
=== Step 3: D076 Eval ===
Start: Wed May 20 06:46:59 CST 2026
inference.py: error: the following arguments are required: --data_path
EXIT_CODE=2
```

ablation 多步脚本在 Step 3 调用 `inference.py` 时**漏传了 `--data_path` 参数**，argparse 报错退出码为 2。

而你问的 `plan010_nli_large_eval`（07:18 提交）**仍在正常运行**：
- PID 733763，状态 `Rl+`，GPU 1 占用 10.4GB
- 进度 ~7/247 batches，每 batch ~40s，预计总时长 ~2.7h

```json
{
  "root_cause": "EXIT_CODE=2 来自 plan010_nli_large_ablation 脚本 Step 3 的 inference.py 调用缺少 --data_path 参数（argparse error），不是 plan010_nli_large_eval 本身。plan010_nli_large_eval (PID 733763) 仍在正常运行。",
  "error_type": "data",
  "fix_steps": [
    "plan010_nli_large_eval 无需修复，正在正常推理中（~7/247 batches）",
    "plan010_nli_large_ablation Step 3 需要在 eval 命令中补上 --data_path /root/autodl-tmp/data/docred"
  ],
  "can_auto_fix": false,
  "resubmit_command": "无需重提交 plan010_nli_large_eval，它正在运行。ablation Step 3 修复后需重新提交整个 ablation 脚本或单独提交 Step 3 eval。"
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "EXIT_CODE=2 来自 plan010_nli_large_ablation 脚本 Step 3 的 inference.py 调用缺少 --data_path 参数（argparse error），不是 plan010_nli_large_eval 本身。plan010_nli_large_eval (PID 733763) 仍在正常运行。",
    "error_type": "data",
    "fix_steps": [
      "plan010_nli_large_eval 无需修复，正在正常推理中（~7/247 batches）",
      "plan010_nli_large_ablation Step 3 需要在 eval 命令中补上 --data_path /root/autodl-tmp/data/docred"
    ],
    "can_auto_fix": false,
    "resubmit_command": "无需重提交 plan010_nli_large_eval，它正在运行。ablation Step 3 修复后需重新提交整个 ablation 脚本或单独提交 Step 3 eval。"
  }
}
```

</details>

---
