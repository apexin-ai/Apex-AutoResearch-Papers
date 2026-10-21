# bugfix aci sign

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_bugfix_aci-sign_20260513T035216_result.json`
- **Structured JSON:** [`e13c97a822240c68bd7c.json`](../../sessions/e1/e13c97a822240c68bd7c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成。总结：

**修改内容** (`src/aci.py` 第 61 行):
- 修复前: `self.alpha + self.gamma * (err - self.alpha_target)` — 符号反了
- 修复后: `self.alpha + self.gamma * (self.alpha_target - err)` — 符合 Gibbs & Candès 2021

**alpha 变化方向确认**:
| 场景 | 修复前 | 修复后 |
|------|--------|--------|
| cover (err=0) | alpha 减小 (错误) | alpha 增大 → 0.11 (收紧) |
| miss (err=1) | alpha 增大 (错误) | alpha 减小 → 0.01 (放松) |

**测试结果**: 3/3 PASSED — cover/miss 方向正确，连续 100 次 miss 后 alpha 稳定在安全范围内。

---
