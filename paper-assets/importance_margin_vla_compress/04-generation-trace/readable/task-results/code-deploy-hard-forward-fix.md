# code deploy hard forward fix

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_deploy-hard-forward-fix_20260515T172928_result.json`
- **Structured JSON:** [`166c7707a0e60bc8d91a.json`](../../sessions/16/166c7707a0e60bc8d91a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结果：**

1. `_hard_forward` 修复**已经部署在服务器上** — 使用 `binary_mask * tokens`，输出 `(B, N, D)`，无 `torch.gather` 调用
2. dry-run **通过** — train `(4, 64, 960)`, eval `(4, 64, 960)`, 每个 batch 保留 32 tokens

不需要额外修改。`_merge_borderline_tokens` 方法仍存在于文件中（行 75-111）但已是死代码，不被调用。

---
