# diagnose exp 085 contrastive mistral logiqa seed123

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp-085-contrastive-mistral-logiqa-seed123_20260519T224929_result.json`
- **Structured JSON:** [`bdb19e1a696eab57eba5.json`](../../sessions/bd/bdb19e1a696eab57eba5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**实验正常运行中**，当前 21/200（~10%），ETA 约 102 分钟。每个样本约 30-40 秒。

```json
{
  "status": "still_running",
  "actual_log_path": "/root/runs/symb_invariant_consensus/exp-085-contrastive-mistral-logiqa-seed123.log",
  "progress": "21/200 (10.5%), ETA ~102 min",
  "root_cause_of_cron_alert": "CRON 在 results/exp085_.../run.log 找日志（不存在），实际日志在 ~/runs/ 下；且实验未注册 registry、不上报 W&B metrics，CRON 因无 W&B 数据误判失败。与 exp-070 同类误报。",
  "gpu_usage": "GPU 2 (via vLLM on port 8002) ~90GB VRAM, CUDA_VISIBLE_DEVICES=2",
  "action_needed": "none — 实验正常推进，CRON 告警可忽略。如需消除告警可将实验注册到 registry 并修正日志路径。"
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "status": "still_running",
    "actual_log_path": "/root/runs/symb_invariant_consensus/exp-085-contrastive-mistral-logiqa-seed123.log",
    "progress": "21/200 (10.5%), ETA ~102 min",
    "root_cause_of_cron_alert": "CRON 在 results/exp085_.../run.log 找日志（不存在），实际日志在 ~/runs/ 下；且实验未注册 registry、不上报 W&B metrics，CRON 因无 W&B 数据误判失败。与 exp-070 同类误报。",
    "gpu_usage": "GPU 2 (via vLLM on port 8002) ~90GB VRAM, CUDA_VISIBLE_DEVICES=2",
    "action_needed": "none — 实验正常推进，CRON 告警可忽略。如需消除告警可将实验注册到 registry 并修正日志路径。"
  }
}
```

</details>

---
