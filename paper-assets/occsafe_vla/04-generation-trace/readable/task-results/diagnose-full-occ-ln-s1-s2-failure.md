# diagnose full occ ln s1 s2 failure

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_full_occ_ln_s1_s2_failure_20260525T022650_result.json`
- **Structured JSON:** [`9ca1ac193c437f24a384.json`](../../sessions/9c/9ca1ac193c437f24a384.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

### 结论：**False Positive — 两个实验都已成功完成训练**

**根因**：`EXIT_CODE=1` 由 PyTorch 的 `destroy_process_group()` 未调用警告触发，不是真正的训练错误。这是 `torchrun` 的已知行为——进程正常退出但未显式调用 `destroy_process_group()`，NCCL 后端打印 warning 并导致非零退出码。

```
[rank0]:[W525 10:23:32] Warning: WARNING: destroy_process_group() was not called before program exit
```

**两个实验的日志完全一致地显示：**

| 指标 | full_occ_ln_s1 | full_occ_ln_s2 |
|------|---------------|---------------|
| 最终 step | `Max step 50005 reached!` | `Max step 50005 reached!` |
| step 30000 aux loss | occ=0.0089, action=0.0515 | occ=0.0074, action=0.0415 |
| 50000_chkpt 已保存 | Yes (15GB, 完整) | Yes (15GB, 完整) |
| 失败原因 | destroy_process_group warning | 同左 |

**Checkpoint 验证**：两个 `50000_chkpt` 目录完整存在，包含全部文件（4 个 model safetensors shard、action_head、occ_head、proprio_projector、lora_adapter 等），文件大小一致，时间戳均为 `May 25 10:22-10:23`。

**无需恢复训练，可直接用 50000 checkpoint 进行评估。**

---
