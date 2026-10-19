# fix lora alpha dynamic v2

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_lora-alpha-dynamic-v2_20260516T011431_result.json`
- **Structured JSON:** [`2bb51909f90773609ba1.json`](../../sessions/2b/2bb51909f90773609ba1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改完成，三项验证全部通过：

- `rank=16`（默认）→ `alpha=32`，与之前行为一致
- `rank=48` → `alpha=96`，动态计算 `rank * 2`
- `--lora_alpha 64` 显式指定 → `alpha=64`，手动指定时不被覆盖

---
