# check post restart status

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_post_restart_status_20260522T020902_result.json`
- **Structured JSON:** [`cc03e8a7d9ba23b920fc.json`](../../sessions/cc/cc03e8a7d9ba23b920fc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== westd-16980 ===
GPU0: 0/97887 MiB, 0%
GPU1: 0/97887 MiB, 0%
r16_70b_lora_scierc: 死亡（已完成）, checkpoint: checkpoint-663 ✅, 最后 step: 663/663, eval_loss=0.0611, token_acc=97.78%
r16_70b_lora_docred: 死亡（已完成）, checkpoint: checkpoint-1146 ✅, 最后 step: 1146/1146, eval_loss=0.0635, token_acc=97.94%

=== westd-21461 ===
⚠️ SSH 连接失败: Unable to connect to port 21461 — 实例重启后端口已变更

需要重启的实验: 无（两个 LoRA 训练都已正常跑完）
```

westd-16980 两个 70B LoRA 训练都已完成 3 epoch，adapter 已保存，无需重启。GPU 空闲。

westd-21461 连不上，AutoDL 实例重启后 SSH 端口会变，需要去 AutoDL 控制台查看新端口并更新 `~/.ssh/config`。之前的 70B DocRED ZS 推理状态需要等连接恢复后再查。

---
