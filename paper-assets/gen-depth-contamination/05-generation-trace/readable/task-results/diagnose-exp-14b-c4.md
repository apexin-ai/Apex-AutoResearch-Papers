# diagnose exp 14b c4

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_14b_c4_20260518T051051_result.json`
- **Structured JSON:** [`610e2826e937af2d1705.json`](../../sessions/61/610e2826e937af2d1705.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。汇总：

**时间线：**
- 01:08:58 — 模型加载完成，depth_0 已存在跳过，开始 depth 1
- 04:01 — depth_1 完成 (2h52m)
- 06:52 — depth_2 完成 (2h51m)
- 09:46 — depth_3 完成 (2h54m)
- 12:39 — depth_4 完成 (2h53m)
- 12:39 — depth_5 开始
- ~13:09 — **timeout kill** (depth_5 仅完成 214/1250 batches = 17%)

**已完成：** depth_0 ~ depth_4 各 5000 行全部完成。depth_5 无落盘文件。Scoring 阶段 0% (results 目录不存在，日志中无 Scoring 记录)。

**速率：** 14B 模型 generation ~8.35s/batch，每个 depth (1250 batches) 约 2h53m。

```json
{"root_cause":"timeout: 12h不够14B模型跑完5 depths generation + 6 depths scoring。generation alone需要~14.4h (5×2h53m)，scoring额外需2-3h，总计约17-18h","error_type":"resource","completed_depths":[0,1,2,3,4],"partial_depth":"depth_5 generation at 17% (214/1250 batches), no file written to disk","estimated_total_hours":18,"fix_steps":["增加timeout到24h","pipeline支持resume则可从depth_5断点续跑，省去已完成的depth_0-4 (~11.5h)","或减少num_samples从5000到3000 (总时间降到~11h)","或增大batch_size从4到8 (需验证GPU内存是否够)"],"can_auto_fix":true}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "timeout: 12h不够14B模型跑完5 depths generation + 6 depths scoring。generation alone需要~14.4h (5×2h53m)，scoring额外需2-3h，总计约17-18h",
    "error_type": "resource",
    "completed_depths": [
      0,
      1,
      2,
      3,
      4
    ],
    "partial_depth": "depth_5 generation at 17% (214/1250 batches), no file written to disk",
    "estimated_total_hours": 18,
    "fix_steps": [
      "增加timeout到24h",
      "pipeline支持resume则可从depth_5断点续跑，省去已完成的depth_0-4 (~11.5h)",
      "或减少num_samples从5000到3000 (总时间降到~11h)",
      "或增大batch_size从4到8 (需验证GPU内存是否够)"
    ],
    "can_auto_fix": true
  }
}
```

</details>

---
