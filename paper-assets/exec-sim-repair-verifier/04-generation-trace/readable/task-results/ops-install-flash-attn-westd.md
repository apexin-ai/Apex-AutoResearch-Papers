# ops install flash attn westd

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_install-flash-attn-westd_20260516T001155_result.json`
- **Structured JSON:** [`8d1dc173579b5765a444.json`](../../sessions/8d/8d1dc173579b5765a444.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已有完善的 fallback：`flash_attn` 导入失败时自动回退到 `"sdpa"`。

**结果：**

- **flash-attn 2.x 无法安装** — 所有版本都不支持 RTX 5090 Blackwell (sm_120) 架构，源码编译失败
- **不影响 CWM 8B val sweep** — 所有 eval 脚本（eval_cwm_baseline.py 等）都有 fallback 逻辑，import flash_attn 失败时自动使用 `attn_implementation="sdpa"`
- **PyTorch 2.10 内置 SDPA flash backend 在 5090 上正常工作**，性能与独立 flash-attn 包基本一致
- **无需修改任何 eval 脚本**

---
