# bugfix attention analysis perband

**tbab multi turn** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_bugfix_attention-analysis-perband_20260518T071718_result.json`
- **Structured JSON:** [`457d8624a62430477e92.json`](../../sessions/45/457d8624a62430477e92.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个 bug 全部修复并验证通过：

| Bug | 修复内容 | 验证状态 |
|-----|---------|---------|
| **Bug 1** (dim_idx) | `[2p, 2p+1]` → `[p, p+D_HEAD//2]`（split-half 配对），rotation 从 interleave even/odd 改为 first-half/second-half | pair 0→dims [0,64], pair 1→dims [1,65]，手动计算完全吻合 |
| **Bug 2** (频段命名) | pairs 0-20 从 `low_freq` 改为 `high_freq`，pairs 43-63 从 `high_freq` 改为 `low_freq` | high_freq mean inv_freq=0.338 (半周期9位置)，low_freq mean inv_freq=7.7e-4 (半周期4078位置) |
| **Bug 3** (dtype) | model_local.py `torch.float16` → `torch.bfloat16` | 已确认 |

---
