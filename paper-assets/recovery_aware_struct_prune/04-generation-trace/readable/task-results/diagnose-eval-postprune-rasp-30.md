# diagnose eval postprune rasp 30

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_postprune_rasp_30_20260517T194121_result.json`
- **Structured JSON:** [`c4cd3a939e8712fa8596.json`](../../sessions/c4/c4cd3a939e8712fa8596.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。**实验并未真正失败，进程仍在运行。**

关键发现：
- **PID 43911** (python eval_gsm8k.py) 仍存活，当前进度 54/200，输出仍写入日志
- **PID 44265** 已不存在，是被 kill 的 tmux 会话中的 shell 进程
- tmux 会话 `eval_postprune_rasp_30` 已不在 `tmux ls` 中（被外部销毁），但 python 子进程存活
- 日志中 sample 46 处的 "Terminated" 是 shell 收到 SIGTERM 时的 job notification 输出，非 python 进程本身终止
- nvidia-smi 确认 cuda:2 上 PID 43911 占用 11568MiB，GPU 利用率 86%

时间线推断：约 03:09-03:17 之间有新 tmux 会话创建（eval_postprune_standard_30、eval_sft_cka_only_20_n1319），可能有自动化脚本误杀了 eval_postprune_rasp_30 的 tmux session，导致 shell（PID 44265）被 SIGTERM，但 python 进程因未绑定终端信号而继续运行。

```json
{"root_cause":"tmux session被外部销毁(可能是启动新实验的自动化脚本误杀),shell进程PID 44265收到SIGTERM(exit 143),但python进程PID 43911未受影响仍在运行,当前54/200","error_type":"infrastructure","fix_steps":["无需修复-实验仍在正常运行中","可选:用 tmux new-session -d -s eval_postprune_rasp_30_monitor 重新挂载监控","预计剩余运行时间约2-2.5h(按当前~55s/it计算146样本)"],"can_auto_fix":true,"partial_result_usable":false,"partial_accuracy":"0.0000 at 50/200 (实验仍在继续,非最终结果)"}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "tmux session被外部销毁(可能是启动新实验的自动化脚本误杀),shell进程PID 44265收到SIGTERM(exit 143),但python进程PID 43911未受影响仍在运行,当前54/200",
    "error_type": "infrastructure",
    "fix_steps": [
      "无需修复-实验仍在正常运行中",
      "可选:用 tmux new-session -d -s eval_postprune_rasp_30_monitor 重新挂载监控",
      "预计剩余运行时间约2-2.5h(按当前~55s/it计算146样本)"
    ],
    "can_auto_fix": true,
    "partial_result_usable": false,
    "partial_accuracy": "0.0000 at 50/200 (实验仍在继续,非最终结果)"
  }
}
```

</details>

---
