# debug checkpoint collapse boundary

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_checkpoint_collapse_boundary_20260516T120050_result.json`
- **Structured JSON:** [`f40c7386185f8984e2d4.json`](../../sessions/f4/f40c7386185f8984e2d4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

扫描完成。结果清晰：

```
=== cuda:1 Early Checkpoints ===

--- baseline (alpha=64) ---
  step_005000: std=0.011365 [WARN]
  step_010000: std=0.007966 [FAIL]
  step_015000: std=0.007222 [FAIL]
  step_020000: std=0.006670 [FAIL]
  step_025000: std=0.006106 [FAIL]
  step_029999: std=0.005876 [FAIL]
  Collapse boundary: step_005000 (std=0.0114) -> step_010000 (std=0.0080)

--- v6_alpha16 (alpha=16) ---
  step_005000: std=0.036188 [WARN]
  step_010000: std=0.034032 [WARN]
  step_015000: std=0.014785 [WARN]
  step_020000: std=0.023635 [WARN]
  step_025000: std=0.016814 [WARN]
  step_029999: std=0.029462 [WARN]
  No collapse detected in any checkpoint
```

**关键发现：**

1. **baseline (alpha=64)**：collapse 发生在 step 5K→10K 之间。step_005000 的 std=0.011 已经很低（仅 WARN），没有任何 checkpoint 达到 PASS (>0.05)。说明 alpha=64 从极早期就开始 collapse，**不存在"既有 diversity 又有 quality"的最优窗口**。

2. **v6_alpha16 (alpha=16)**：全程 WARN，无 FAIL。std 范围 0.015-0.036，说明 alpha=16 有效抑制了 collapse，但 diversity 仍低于健康水平 (0.05)。

baseline step_005000 是最接近 PASS 的 checkpoint (std=0.011)，但仍然太低。是否需要对它做快速 rollout 验证 action quality？

---
