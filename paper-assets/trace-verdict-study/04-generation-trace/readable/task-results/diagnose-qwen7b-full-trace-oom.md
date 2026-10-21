# diagnose qwen7b full trace oom

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_qwen7b_full_trace_oom_20260521T073438_result.json`
- **Structured JSON:** [`19dc05c0c1a37bbf7f02.json`](../../sessions/19/19dc05c0c1a37bbf7f02.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断报告已写入 `/root/trace-verdict-study/artifacts/diag_qwen7b_full_trace_oom.md`。

**两个根因：**

1. **GPU 未隔离** — 两个进程都跑在同一张物理 GPU 0 上。证据：seed123 进程只用了 46.43 GiB，但 GPU 剩余仅 529 MiB（~48 GiB 被 seed456 占了）。脚本内部 `os.environ["CUDA_VISIBLE_DEVICES"]` 的设置在 CUDA 初始化之后已经太晚，`device_map={"": 0}` 始终映射到逻辑 GPU 0。

2. **缺少 `--gradient_checkpointing`**（违反 C002）— seed456 独占整张 GPU 仍然 OOM：94.74 GiB 已用，还需 4.64 GiB。batch_size=4 × max_length=2048 的 7B 模型激活内存超过 95 GiB 上限。

**修复（两条都要）：**
- 在 shell 层设 `CUDA_VISIBLE_DEVICES=0` / `CUDA_VISIBLE_DEVICES=1`，不依赖脚本内部设置
- 加 `--gradient_checkpointing`（激活内存降 ~40%，训练速度约慢 1 倍）

不需要改代码，脚本已支持这两个参数。

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
