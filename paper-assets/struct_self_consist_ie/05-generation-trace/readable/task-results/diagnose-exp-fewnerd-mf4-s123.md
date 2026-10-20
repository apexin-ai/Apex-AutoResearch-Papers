# diagnose exp fewnerd mf4 s123

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_fewnerd_mf4_s123_20260522T103817_result.json`
- **Structured JSON:** [`f505bca278c050c64c22.json`](../../sessions/f5/f505bca278c050c64c22.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 张 GPU 全被 `fewnerd_n32_s42` 的 4 个 shard 占满，每个 shard 各占一张 GPU。exp_fewnerd_mf4_s123 没有可用 GPU。

```json
{
  "root_cause": "ValueError: Free memory on device cuda:0 (1.44/31.36 GiB) on startup is less than desired GPU memory utilization (0.9, 28.22 GiB). 所有 4 张 RTX 5090 均被 fewnerd_n32_s42 的 4 个 shard 进程占满（每张 ~30GB/32GB），无空闲 GPU 可用。",
  "error_type": "resource",
  "fix_steps": [
    "等待 fewnerd_n32_s42 四个 shard 跑完后重新提交 exp_fewnerd_mf4_s123",
    "或者将 exp_fewnerd_mf4_s123 提交到有空闲 GPU 的其他服务器（如 autodl-5090-c）",
    "提交时可通过 CUDA_VISIBLE_DEVICES 指定空闲 GPU，避免争抢"
  ],
  "can_auto_fix": false,
  "full_log_tail": "ValueError: Free memory on device cuda:0 (1.44/31.36 GiB) on startup is less than desired GPU memory utilization (0.9, 28.22 GiB). Decrease GPU memory utilization or reduce GPU memory used by other processes.\nRuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {}\nEXIT_CODE=1"
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "ValueError: Free memory on device cuda:0 (1.44/31.36 GiB) on startup is less than desired GPU memory utilization (0.9, 28.22 GiB). 所有 4 张 RTX 5090 均被 fewnerd_n32_s42 的 4 个 shard 进程占满（每张 ~30GB/32GB），无空闲 GPU 可用。",
    "error_type": "resource",
    "fix_steps": [
      "等待 fewnerd_n32_s42 四个 shard 跑完后重新提交 exp_fewnerd_mf4_s123",
      "或者将 exp_fewnerd_mf4_s123 提交到有空闲 GPU 的其他服务器（如 autodl-5090-c）",
      "提交时可通过 CUDA_VISIBLE_DEVICES 指定空闲 GPU，避免争抢"
    ],
    "can_auto_fix": false,
    "full_log_tail": "ValueError: Free memory on device cuda:0 (1.44/31.36 GiB) on startup is less than desired GPU memory utilization (0.9, 28.22 GiB). Decrease GPU memory utilization or reduce GPU memory used by other processes.\nRuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {}\nEXIT_CODE=1"
  }
}
```

</details>

---
