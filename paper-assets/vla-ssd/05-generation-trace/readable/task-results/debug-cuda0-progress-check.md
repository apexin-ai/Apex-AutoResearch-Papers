# debug cuda0 progress check

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_cuda0_progress_check_20260517T200047_result.json`
- **Structured JSON:** [`9ff1bc77cf54ba57a2bd.json`](../../sessions/9f/9ff1bc77cf54ba57a2bd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
cuda:0 GPU util: 84%
Memory: 15821 MiB / 97887 MiB
Current progress: [ablate_all24] frame extraction 3550/10208 (~35%)
Estimated remaining: ~107 min (~1h47m)
Output file: not yet (action_probe_50demos.json)
```

**进度详情：**
- 3 个 conditions：`baseline` / `ablate_all24` / `ablate_all32`
- `baseline`：已完成（耗时 64.2 min）
- `ablate_all24`：正在提取特征，3550/10208 frames（~35%），预计还需 ~43 min
- `ablate_all32`：未开始，预计 ~64 min
- `action_probe_50demos_control8.json` 已生成（cuda:1 上的 control8 实验已完成）

---
