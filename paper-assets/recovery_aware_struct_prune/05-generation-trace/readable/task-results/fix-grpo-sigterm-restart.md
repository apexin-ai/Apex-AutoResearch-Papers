# fix grpo sigterm restart

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_grpo_sigterm_restart_20260522T065328_result.json`
- **Structured JSON:** [`337d635343ae2081dfaf.json`](../../sessions/33/337d635343ae2081dfaf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
== 诊断 ==
SIGTERM 来源: 无法确定（dmesg 无权限，无 crontab，无可疑进程/脚本，无旧 tmux session）
可疑进程/脚本: 无

== 重启 ==
α=2.0 PID: 20308 on GPU 2
α=0.5 PID: 20449 on GPU 3

关键修复:
- 加 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`（首次 `python: command not found`）
- 加 `--gradient_checkpointing true`（不是 bare flag）
- 加 `HF_DATASETS_OFFLINE=1 + HF_HUB_OFFLINE=1`（网络不通导致 load_dataset 卡死）
- 加 `source /etc/network_turbo`（AutoDL 代理）

== 30s 验证 ==
GPU 2: PID 20308, 54313 MiB, 86% util
GPU 3: PID 20449, 54275 MiB, 85% util

== 3min 验证 ==
α=2.0: step 16/100, loss=0.030, reward=0.034
α=0.5: step 15/100, loss=-0.011, reward=0.020
超过 step 15: **YES** ✓

== W&B ==
α=2.0: https://wandb.ai/xiaoyucorynne-/recovery_aware_struct_prune/runs/2b2x9kmb
α=0.5: https://wandb.ai/xiaoyucorynne-/recovery_aware_struct_prune/runs/0fh1firj

预计 ~17 min 完成 100 steps（~10.2s/step），之后自动进入 eval_gsm8k 阶段。
```

---
