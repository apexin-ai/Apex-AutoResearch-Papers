# diagnose grpo rasp rlvr 20

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_grpo_rasp_rlvr_20_20260516T202158_result.json`
- **Structured JSON:** [`75a5de14ee18ff2c4131.json`](../../sessions/75/75a5de14ee18ff2c4131.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

综合所有证据，诊断结论明确了：

```json
{
  "status": "crashed",
  "root_cause": "进程在 step 16 (约 1:49 elapsed) 被静默 kill，日志无 traceback/error/OOM 记录。日志最后修改时间 2026-05-17 04:20:40，训练启动于 02:26:32，运行约 1h54m。仅保存了 step 10 的 completions parquet，无 checkpoint。最可能原因：系统 OOM killer 杀死进程（模型 6.16B params + ref_model 同等大小 = ~24GB+ GPU显存，加上 GRPO 4 generations × 1024 tokens 的中间状态）。",
  "error_type": "resource",
  "fix_steps": [
    "减少 num_generations 从 4 到 2，降低 generation 时的显存峰值",
    "减少 generation_batch_size 从 16 到 8",
    "减少 max_completion_length 从 1024 到 512（日志显示 mean_terminated_length 仅 292.5）",
    "或将训练移至 westd-11672（4×RTX PRO 6000，显存更充裕）",
    "重启训练前用 nvidia-smi 确认显存可用量"
  ],
  "can_auto_fix": true,
  "log_snippet": "最后一行进度: 16%|█▌| 16/100 [1:49:06<9:43:44, 416.96s/it]\n无任何 error/traceback/OOM 信息 → 被信号静默终止（SIGKILL by OOM killer 或手动 kill）"
}
```

**关键发现**：训练正常跑到 step 16，然后被静默杀死（无 graceful shutdown）。日志中零 error。模型配置显示 `num_parameters = 6,161,946,112`（~6.16B），因为模型+ref_model 两份都加载到同一 GPU（`CUDA_VISIBLE_DEVICES=1`），加上 GRPO generation batch 的中间状态，极大概率是 GPU OOM 导致系统直接 SIGKILL。

最便宜的修复是减小 `max_completion_length`（实际 mean_terminated_length 仅 292.5，1024 浪费且触发 OOM）和减小 `generation_batch_size`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "status": "crashed",
    "root_cause": "进程在 step 16 (约 1:49 elapsed) 被静默 kill，日志无 traceback/error/OOM 记录。日志最后修改时间 2026-05-17 04:20:40，训练启动于 02:26:32，运行约 1h54m。仅保存了 step 10 的 completions parquet，无 checkpoint。最可能原因：系统 OOM killer 杀死进程（模型 6.16B params + ref_model 同等大小 = ~24GB+ GPU显存，加上 GRPO 4 generations × 1024 tokens 的中间状态）。",
    "error_type": "resource",
    "fix_steps": [
      "减少 num_generations 从 4 到 2，降低 generation 时的显存峰值",
      "减少 generation_batch_size 从 16 到 8",
      "减少 max_completion_length 从 1024 到 512（日志显示 mean_terminated_length 仅 292.5）",
      "或将训练移至 westd-11672（4×RTX PRO 6000，显存更充裕）",
      "重启训练前用 nvidia-smi 确认显存可用量"
    ],
    "can_auto_fix": true,
    "log_snippet": "最后一行进度: 16%|█▌| 16/100 [1:49:06<9:43:44, 416.96s/it]\n无任何 error/traceback/OOM 信息 → 被信号静默终止（SIGKILL by OOM killer 或手动 kill）"
  }
}
```

</details>

---
