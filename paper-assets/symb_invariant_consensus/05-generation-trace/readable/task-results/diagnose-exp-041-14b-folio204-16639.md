# diagnose exp 041 14b folio204 16639

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp-041-14b-folio204-16639_20260518T201706_result.json`
- **Structured JSON:** [`4dce569e6ef8d5856635.json`](../../sessions/4d/4dce569e6ef8d5856635.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。结论：

**exp-041 从未被提交到服务器。** 服务器上没有任何 exp-041 相关的文件、脚本、tmux session 或进程。Registry 中缺少 pid/log_path/gpu/submitted_at 进一步确认这一点。

服务器现状：
- GPU 0: vLLM (port 8000) 跑 exp032 (Qwen2.5-14B, ProofWriter)
- GPU 1: vLLM (port 8001) 跑 exp033 (Qwen3-14B, ProofWriter)
- GPU 2-3: 空闲
- exp038 实际通过正常流程跑完了（有 results.json + log + intermediates，完成于 03:57），所以 **exp038 与 exp-041 不是同一失败模式**

```json
{"root_cause":"exp-041 was registered in tracking system but never submitted to server — no script, no tmux session, no process, no logs, no results directory exist on westd-16639. submit_training_job was never called.","error_type":"infrastructure","fix_steps":["Create run script scripts/run_exp041.sh with vLLM on port 8002 (GPU 2) + run_full_mvp.py targeting FOLIO-204","Deploy and launch via submit_training_job on westd-16639 GPU 2","Verify tmux session and vLLM startup before marking submitted"],"can_auto_fix":true,"exp038_same_issue":false}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "exp-041 was registered in tracking system but never submitted to server — no script, no tmux session, no process, no logs, no results directory exist on westd-16639. submit_training_job was never called.",
    "error_type": "infrastructure",
    "fix_steps": [
      "Create run script scripts/run_exp041.sh with vLLM on port 8002 (GPU 2) + run_full_mvp.py targeting FOLIO-204",
      "Deploy and launch via submit_training_job on westd-16639 GPU 2",
      "Verify tmux session and vLLM startup before marking submitted"
    ],
    "can_auto_fix": true,
    "exp038_same_issue": false
  }
}
```

</details>

---
