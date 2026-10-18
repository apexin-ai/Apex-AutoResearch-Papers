# eval v7 progress checkpoint verify

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_v7-progress-checkpoint-verify_20260515T200421_result.json`
- **Structured JSON:** [`d629a7d10670fcb5bc73.json`](../../sessions/d6/d629a7d10670fcb5bc73.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### v7 训练进度
- **当前 step**: 27950 / 30000 (93.2%)
- **速度**: 3.2 steps/s，每 50 步约 16 秒
- **剩余**: 2050 steps ≈ **~10.7 分钟**（预计 ~04:15 UTC 完成）
- **Loss**: 正常波动，0.001~0.08 范围，无异常

### v7.2 训练进度
- **当前 step**: 8350 / 30000 (27.8%)
- **速度**: 3.2 steps/s
- **剩余**: 21650 steps ≈ **~113 分钟（约 1 小时 53 分）**
- 已保存 checkpoint 到 step_008000

### D014 eval checkpoint 验证

| Checkpoint | 路径 | 状态 |
|---|---|---|
| baseline final | `baseline/step_029999/` | **存在** (1.16GB checkpoint.pt) |
| baseline mid 5K | `baseline/step_005000/` | **存在** (注意是 step_005000 不是 step_004999) |
| baseline mid 10K | `baseline/step_010000/` | **存在** (同上，step_010000) |
| v7 IMM checkpoints | `imm_anchor/` | 已有 step_002000 ~ step_026000 (每 2000 步)，**v7 final (step_028000/step_029999) 尚未生成**，约 10 分钟后可用 |

### 注意事项
- Baseline checkpoint 命名是 step_005000 / step_010000（不是 off-by-one 的 step_004999/step_009999），D014 eval 配置中路径需对应
- v7 训练即将完成，final checkpoint 很快可用；v7.2 还需约 2 小时

---
