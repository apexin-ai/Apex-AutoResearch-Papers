# diagnose d112 rsft no evidence eval

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_d112_rsft_no_evidence_eval_20260519T134139_result.json`
- **Structured JSON:** [`0749732cfafd9d11f30d.json`](../../sessions/07/0749732cfafd9d11f30d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

日志确认：`bash: scripts/d112/eval_4b_rsft_no_evidence.sh: No such file or directory`。脚本名错了。

目录下实际只有一个脚本：`eval_d112_rsft_bf16.sh`。

```json
{"root_cause":"bash: scripts/d112/eval_4b_rsft_no_evidence.sh: No such file or directory — 脚本不存在，实际文件名是 eval_d112_rsft_bf16.sh","error_type":"infrastructure","fix_steps":["将提交命令中的脚本路径改为 scripts/d112/eval_d112_rsft_bf16.sh 重新提交"],"can_auto_fix":true}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "bash: scripts/d112/eval_4b_rsft_no_evidence.sh: No such file or directory — 脚本不存在，实际文件名是 eval_d112_rsft_bf16.sh",
    "error_type": "infrastructure",
    "fix_steps": [
      "将提交命令中的脚本路径改为 scripts/d112/eval_d112_rsft_bf16.sh 重新提交"
    ],
    "can_auto_fix": true
  }
}
```

</details>

---
