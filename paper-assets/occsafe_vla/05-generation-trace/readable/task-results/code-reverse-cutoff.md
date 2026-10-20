# code reverse cutoff

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_reverse_cutoff_20260523T052416_result.json`
- **Structured JSON:** [`ef67fef568ee38769cbc.json`](../../sessions/ef/ef67fef568ee38769cbc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改完成。总结：

**改动（2 处）：**

1. **第 94-95 行** — 新增参数 `occ_loss_cutoff_mode: str = "after"`
2. **第 1167-1170 行** — cutoff 逻辑增加 mode 判断：
   - `"after"`（默认）：`batch_idx < cutoff_step` 时有 occ_loss，之后关闭（原有行为）
   - `"before"`：`batch_idx < cutoff_step` 时无 occ_loss，之后启用（reverse cutoff）

**使用方式：**
- 原有 cutoff：`--occ_loss_cutoff_step 35000 --occ_loss_cutoff_mode after`
- Reverse cutoff：`--occ_loss_cutoff_step 35000 --occ_loss_cutoff_mode before`
- cutoff@25K：`--occ_loss_cutoff_step 25000 --occ_loss_cutoff_mode after`
- 不传参数（默认 `cutoff_step=0`）→ 全程有 occ_loss，行为不变

---
