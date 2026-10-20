# code update dpo hyperparams

**Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_update-dpo-hyperparams_20260512T150420_result.json`
- **Structured JSON:** [`3a8d6e48c81cc5283ce8.json`](../../sessions/3a/3a8d6e48c81cc5283ce8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

远程验证通过，4 个超参数均已更新：

| 参数 | 旧值 | 新值 | 远程确认 |
|------|------|------|---------|
| lora-rank | 64 | **16** | line 172: `default=16` |
| lora-alpha | (隐式 rank*2=128) | **32** | line 173: `default=32`（新增独立参数） |
| target_modules | 7 个 projections | **["q_proj", "v_proj"]** | line 84 |
| learning-rate | 5e-6 | **5e-7** | line 174: `default=5e-7` |

附带改动：`setup_lora` 调用从 `args.lora_rank * 2` 改为 `args.lora_alpha`，使 alpha 可独立控制。

---
