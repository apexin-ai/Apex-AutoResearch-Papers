# diagnose eval pass k8 standard 20 grpo qwen math

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_pass_k8_standard_20_grpo_qwen_math_20260516T202148_result.json`
- **Structured JSON:** [`e3060e38235989abee04.json`](../../sessions/e3/e3060e38235989abee04.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验 **仍在正常运行**，cron 是误报。

```json
{
  "status": "still_running",
  "metrics": {"pass_k_at_50": 0.9000, "progress": "90/200 (~45%)"},
  "log_snippet": "Pass@8 eval: 45%|████▌ | 90/200 [1:30:05<2:31:26, 82.60s/it]",
  "root_cause": "误报。eval_gsm8k.py 不注册 W&B，cron 靠 W&B heartbeat 检测进程活跃性，检测不到就判定 failed。实际进程 PID 33921/34032 仍在跑，CPU 104%，已完成 90/200 prompts，中间 checkpoint pass@8=0.90。预计还需 ~2.5h 完成。"
}
```

补充观察：该命令产生了 **两个** python 进程（PID 33921 和 34032），可能是 nohup 触发了重复启动，但只要输出文件路径相同，后写入的会覆盖前者，不影响最终结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "status": "still_running",
    "metrics": {
      "pass_k_at_50": 0.9,
      "progress": "90/200 (~45%)"
    },
    "log_snippet": "Pass@8 eval: 45%|████▌ | 90/200 [1:30:05<2:31:26, 82.60s/it]",
    "root_cause": "误报。eval_gsm8k.py 不注册 W&B，cron 靠 W&B heartbeat 检测进程活跃性，检测不到就判定 failed。实际进程 PID 33921/34032 仍在跑，CPU 104%，已完成 90/200 prompts，中间 checkpoint pass@8=0.90。预计还需 ~2.5h 完成。"
  }
}
```

</details>

---
