# code eval pipeline nli fix

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_eval-pipeline-nli-fix_20260518T205344_result.json`
- **Structured JSON:** [`690513df80a794e6975a.json`](../../sessions/69/690513df80a794e6975a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

零残留。三处修改完成：

1. `__init__`：通过 `nli_utils.get_entailment_idx` / `get_contradiction_idx` 动态获取 label index，存入 `self.entailment_idx` / `self.contradiction_idx`
2. `score()` line 196：`probs[2]` → `probs[self.entailment_idx]`
3. `check()` line 218-219：`probs[2]` → `probs[self.entailment_idx]`，`probs[0]` → `probs[self.contradiction_idx]`

---
