# analysis training dynamics gpu run

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_training-dynamics-gpu-run_20260515T153741_result.json`
- **Structured JSON:** [`2bb97fba565d5f3221bf.json`](../../sessions/2b/2bb97fba565d5f3221bf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Training Dynamics Forward Pass 已在 cuda:2 上运行（通过 CUDA_VISIBLE_DEVICES=2 映射）。

当前状态：
- Vanilla (1/6) 正在进行，28/1090 batches，~3 it/s
- 修复了两个问题：`device_map` 从字符串改为 `{"": 0}`，清理了残留 GPU 进程
- 预计总时间约 40 分钟（6 个 checkpoint × ~5-7 分钟/个 + 模型加载时间）

4.5 分钟后自动检查进度。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "": 0
  }
}
```

</details>

---
