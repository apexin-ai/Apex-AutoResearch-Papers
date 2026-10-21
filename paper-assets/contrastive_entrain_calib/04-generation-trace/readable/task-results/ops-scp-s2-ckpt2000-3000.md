# ops scp s2 ckpt2000 3000

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_scp-s2-ckpt2000-3000_20260521T043838_result.json`
- **Structured JSON:** [`566f600cec8154c9e0cf.json`](../../sessions/56/566f600cec8154c9e0cf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**SCP 全部成功。** 通过临时 SSH key 从 29046 直接传到 28034（绕过本机中转）。

### 传输详情
| Checkpoint | 源路径 (29046) | 大小 |
|---|---|---|
| checkpoint-2000 | `exp003_r3only_seed2/checkpoint-2000` | 718MB |
| checkpoint-2500 | `exp003_r3only_seed2/checkpoint-2500` | 718MB |
| checkpoint-3000 | `exp003_r3only_seed2/checkpoint-3000` | 718MB |

注意：29046 上路径是 `exp003_r3only_seed2`（非 `exp003_s2`），已按目标命名放入 28034 的 `exp003_s2/`。

### 28034 完整 s2 checkpoint 列表
```
checkpoint-500
checkpoint-1000
checkpoint-1500
checkpoint-2000  ← 新增
checkpoint-2500  ← 新增
checkpoint-3000  ← 新增
```

每个 checkpoint 包含 adapter_model.safetensors (245MB) + optimizer.pt (491MB) + tokenizer + 配置文件，文件完整。临时 SSH key 已清理。

---
