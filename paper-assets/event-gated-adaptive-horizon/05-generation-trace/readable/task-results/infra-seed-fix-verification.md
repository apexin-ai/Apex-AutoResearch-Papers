# infra seed fix verification

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_seed-fix-verification_20260517T002646_result.json`
- **Structured JSON:** [`3adb77a93ea3a17e50af.json`](../../sessions/3a/3adb77a93ea3a17e50af.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 验证结果

### [SEED CHECK] 输出
```
[SEED CHECK] config.seed = 3
```

### 5K step eval_return 对比

| 实验 | seed | eval_return @5K |
|------|------|----------------|
| exp_008d_civo_trigger_s3 | 3 | **36.13** |
| exp_008d_subsample_on_h8 | 0 | **31.00** |

### prefill train_return 对比 (step=0, 4 episodes)

| episode | seed=3 | seed=0 |
|---------|--------|--------|
| 1 | 32.90 | 33.16 |
| 2 | **36.86** | **52.86** |
| 3 | 30.63 | 30.63 |
| 4 | **35.38** | **54.72** |

### PID 635744
存活确认 ✓（/proc/635744/status 存在）

### 结论：修复成功

seed=3 与 seed=0 在 prefill 阶段和 5K eval 阶段都产生了**不同数值**：
- prefill episode 2/4 差异显著（36.86 vs 52.86, 35.38 vs 54.72）
- 5K eval_return 差异明显（36.13 vs 31.00）

seed bug 修复生效，不同 seed 现在确实产生不同的采样轨迹和训练结果。

---
