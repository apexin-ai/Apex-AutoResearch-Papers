# run p1 ee ft launch

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_p1_ee_ft_launch_20260518T193754_result.json`
- **Structured JSON:** [`a227fd800159ad1c38af.json`](../../sessions/a2/a227fd800159ad1c38af.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

```
tmux session: p1_ee_ft [重建]
GPU 0: util=13%, mem=16201 MiB (模型加载中)
PID: 54946
根因修复: WANDB_DISABLED=true (服务器无网络无法安装 wandb)
训练预估完成: ~16 min
Pipeline 总预估: ~66 min
```

上次启动因 wandb 未安装直接崩溃，`| tee` 吞掉了非零 exit code 导致 pipeline 继续执行到推理阶段才报错。已用 `WANDB_DISABLED=true` + `set -eo pipefail` 重启。

---
