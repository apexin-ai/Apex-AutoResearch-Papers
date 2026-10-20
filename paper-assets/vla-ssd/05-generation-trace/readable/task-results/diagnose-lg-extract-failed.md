# diagnose lg extract failed

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_lg_extract_failed_20260515T165835_result.json`
- **Structured JSON:** [`c94d6fcb4049cd0a0e14.json`](../../sessions/c9/c94d6fcb4049cd0a0e14.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

10 个任务文件完整，每个实验已完成 2/10。脚本有 skip 逻辑（已存在的 .h5 跳过），所以重跑时只会处理剩余 8 个。

```json
{"root_cause":"extract_features.py:80 AutoProcessor.from_pretrained(model_path, trust_remote_code=True) 尝试连接 huggingface.co 获取 config.json → OSError: [Errno 101] Network is unreachable","error_type":"infrastructure","fix_steps":["在 AutoProcessor.from_pretrained() 添加 local_files_only=True（line 80）","在 AutoModelForVision2Seq.from_pretrained() 添加 local_files_only=True（line 87）"],"can_auto_fix":true,"partial_output":{"trained_files":2,"untrained_files":2},"network_status":"unreachable"}
```

已修复。两处 `from_pretrained` 调用都加了 `local_files_only=True`。checkpoint 目录已有全部 processor/tokenizer JSON 文件，无需网络。脚本内置 skip 已完成文件的逻辑，重跑会从第 3/10 个任务继续。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "extract_features.py:80 AutoProcessor.from_pretrained(model_path, trust_remote_code=True) 尝试连接 huggingface.co 获取 config.json → OSError: [Errno 101] Network is unreachable",
    "error_type": "infrastructure",
    "fix_steps": [
      "在 AutoProcessor.from_pretrained() 添加 local_files_only=True（line 80）",
      "在 AutoModelForVision2Seq.from_pretrained() 添加 local_files_only=True（line 87）"
    ],
    "can_auto_fix": true,
    "partial_output": {
      "trained_files": 2,
      "untrained_files": 2
    },
    "network_status": "unreachable"
  }
}
```

</details>

---
