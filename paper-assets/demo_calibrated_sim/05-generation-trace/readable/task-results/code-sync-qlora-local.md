# code sync qlora local

**Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_sync-qlora-local_20260512T144222_result.json`
- **Structured JSON:** [`cb8ac13b3e32f5723fb4.json`](../../sessions/cb/cb8ac13b3e32f5723fb4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

同步完成。

| 项目 | 结果 |
|------|------|
| 服务器版本行数 | 186 行 |
| 本地文件已更新 | `artifacts/code/train_dpo.py` |
| QLoRA 特征验证 | `BitsAndBytesConfig` (L18,59), `load_in_4bit` (L60), `bnb_4bit_compute_dtype` (L62), `sdpa` (L72), `prepare_model_for_kbit_training` (L14,75) |

关键变更：bf16 全精度 → QLoRA 4-bit，`flash_attention_2` → `sdpa`，移除 `max_prompt_length`，`device_map: "auto"` → `{"": 0}`。

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
