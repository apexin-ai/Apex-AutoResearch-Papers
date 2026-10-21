# audit verify restart steps

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_verify-restart-steps_20260527T212207_result.json`
- **Structured JSON:** [`3a6edf54b5c44bf108fc.json`](../../sessions/3a/3a6edf54b5c44bf108fc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
detach_ln_v2_s2:
  20000 checkpoint: 已删除（仅存 15000_chkpt）
  恢复 step: 从 15000_chkpt 作为 pretrained 加载，训练从 step 0 重新开始（无 --resume）
  当前 step: ~72（刚启动约 1 分钟，05:20 UTC 启动）
  训练中: 是（GPU cuda:2, PID 26152, ~1.0s/it）

vanilla_object_s0:
  checkpoint: 仅存 10000_chkpt
  恢复 step: 从 10000_chkpt 作为 pretrained 加载，训练从 step 0 重新开始（无 --resume）
  当前 step: ~67（刚启动约 1 分钟，05:20 UTC 启动）
  训练中: 是（GPU cuda:3, PID 26367, ~1.1s/it）
```

关键发现：两个实验都是把 checkpoint 作为 `--vla_path` 传入（等同 from_pretrained），**不是** `--resume`，所以 batch_idx 从 0 重计。这符合 C002 约束。按 ~1.0s/it 速度，50005 steps 约需 **13.9 小时**，预计完成时间约 **19:20 UTC（北京时间 05-29 03:20）**——超过 C003 的 12:00 UTC deadline 约 7 小时。

---
