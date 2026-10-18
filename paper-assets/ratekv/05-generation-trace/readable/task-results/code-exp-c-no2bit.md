# code exp c no2bit

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_c_no2bit_20260514T001702_result.json`
- **Structured JSON:** [`5d5f299d16dcfa47c2c5.json`](../../sessions/5d/5d5f299d16dcfa47c2c5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。

**总结**：

- **exp_c_no2bit**: MCKP {4,8,16}-bit, budget=0.25 → **NEGATIVE**
- Solver 输出 = 全部 112 heads 4-bit，PPL = 15.45，与 uniform 4-bit 完全相同
- **根本原因**：budget=0.25 恰好等于 4-bit 的 memory ratio (4/16)，而 4-bit 是最低选项。solver 没有低于 4-bit 的选项来"换取"某些 head 用 8/16-bit 的空间，因此唯一可行解 = 全部 4-bit

**后续方向**：
1. 保留 2-bit 但用 constrained MCKP（已验证有效，exp_c PPL=11.23）
2. 放松 budget（如 0.30）让 solver 有空间分配 8/16-bit 给关键 head
3. 引入 3-bit 或 6-bit 等中间精度

---
