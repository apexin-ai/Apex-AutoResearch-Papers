# code v8 contingency configs

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_v8-contingency-configs_20260516T014410_result.json`
- **Structured JSON:** [`c7d9c46e26c91e15b92b.json`](../../sessions/c7/c7d9c46e26c91e15b92b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 contingency config 已创建并验证通过。

### 报告

**关键差异 vs v8:**

| 参数 | v8 | v8.1 | v8.2 |
|------|-----|------|------|
| `lambda_margin` | 0.5 | **0.2** | 0.5 |
| `total_steps` | 30000 | 30000 | **50000** |
| `gradient_isolation` | true | true | true |
| `delta` | 0.3 | 0.3 | 0.3 |
| `output_dir` | `imm_anchor_v8` | `imm_anchor_v8_1` | `imm_anchor_v8_2` |

**配置验证**: OK，yaml 解析正常，关键字段值正确。

**LR schedule 调整细节**: `make_scheduler()` 使用 `SequentialLR(LinearLR warmup → CosineAnnealingLR)`，其中 `T_max = total_steps - warmup_steps`。`warmup_steps`(1000) 和 `decay_lr`(2.5e-6) 继承自 baseline.yaml，**v8.2 无需手动调整** — cosine 的 `T_max` 会从 config 中读取 `total_steps` 自动计算为 49000（50000-1000），decay 周期自动延长。

---
