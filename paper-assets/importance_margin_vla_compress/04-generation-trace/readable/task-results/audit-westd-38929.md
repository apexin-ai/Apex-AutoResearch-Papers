# audit westd 38929

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_westd-38929_20260522T015227_result.json`
- **Structured JSON:** [`aaf967036163381f874e.json`](../../sessions/aa/aaf967036163381f874e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

巡检完成。总结：

**westd-38929 实际状态：**
- **1个活跃进程**：PID 227008 — `eval_pi05_l2norm_k085_spatial_seed42`，GPU0 上运行中，已完成 Task 0 (98%) 和 Task 1 进行中 (~95%)，预计还需 ~80 分钟
- **4个已正常完成**：
  - l2norm k=0.90 spatial → **95.0%**
  - random k=0.90 spatial → 54.6%
  - random k=0.85 spatial → 58.4%
  - random k=0.925 object seed43 → 30.0%
- **1个失败**：`eval_openvla_l2norm_k05_object_seed42_v4` — huggingface-hub 版本冲突（需要 <1.0，实际 1.16.0）
- **GPU 1/2/3 完全空闲**，无 tmux session

报告已注册到 artifacts。

---
