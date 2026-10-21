# fix 14b eval oom

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_14b_eval_oom_20260518T133906_result.json`
- **Structured JSON:** [`1028efe9faca6e0202f0.json`](../../sessions/10/1028efe9faca6e0202f0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。改动：

- `CUDA_VISIBLE_DEVICES` 默认 `2,3`（2-GPU），`device_map="auto"` 自动将 14B bf16 (~28GB) 分到两张卡（~14GB/卡，留 ~18GB 给 KV cache）
- `batch_size` 4→2，余量更安全
- 其余参数（`--no-quantize`, `--max_new_tokens 1024`, `--split dev`）不变
- 无需改 `inference.py`，已原生支持 `device_map="auto"`

---
