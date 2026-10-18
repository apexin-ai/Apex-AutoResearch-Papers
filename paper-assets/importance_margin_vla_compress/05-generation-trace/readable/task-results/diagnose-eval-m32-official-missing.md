# diagnose eval m32 official missing

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_m32_official_missing_20260519T094239_result.json`
- **Structured JSON:** [`4ba92744f6af2f080f0d.json`](../../sessions/4b/4ba92744f6af2f080f0d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 重启成功，运行正常。

**汇报**：

| 项目 | 状态 |
|---|---|
| **原因** | eval 脚本 hardcode 读 `configs/smart_compress.yaml`（指向 `smolvla_base`，hidden_dim=720），但 checkpoint 训练时用的是 `smolvla_libero`（hidden_dim=480），导致 `load_state_dict` shape mismatch 崩溃 |
| **修复** | 修改 `eval_smart_compress_libero.py:load_model()` — 先加载 checkpoint，优先使用其内嵌 config，无 config 时才 fallback 到 yaml |
| **当前状态** | 已重启，PID **81334**（子进程 python），GPU 3，`Checkpoint loaded with strict match (no missing/unexpected keys)` |
| **进度** | Task 0 已开始，Ep 1/500 SUCCESS |
| **需要重启？** | 已完成重启，无需额外操作 |

---
