# ops eval 25pct s3 cpu

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_eval-25pct-s3-cpu_20260522T143853_result.json`
- **Structured JSON:** [`eb2199959637550c1228.json`](../../sessions/eb/eb2199959637550c1228.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

没有 `contam_25_s3_results.json`。也没有缓存的 response vector。

**结论：eval 需要 GPU，无法与训练并行。**

- `eval_lz.py` 使用 bitsandbytes 4-bit 量化加载 7B 模型，只能在 GPU 上运行
- `device_map={"": 0}` 硬编码 GPU 0
- 没有已缓存的 response vector 可复用
- 即使改写为 CPU 模式（去掉量化），7B 模型在 CPU 上对 14042 items 做 forward pass 也不现实（预计数小时）

**等 contam_50_s2 训练完成后再做 contam_25_s3 的 eval。**

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
