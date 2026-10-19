# code residual connection scoring

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_residual-connection-scoring_20260516T195210_result.json`
- **Structured JSON:** [`27da970865b0ece88110.json`](../../sessions/27/27da970865b0ece88110.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

## 修改的文件

| 文件 | 改动 |
|------|------|
| `acib/config.py:31` | 添加 `scoring_alpha: float = 1.0` |
| `acib/acib_policy.py:26` | `__init__` 中读取 `self.scoring_alpha = acib_config.scoring_alpha` |
| `acib/acib_policy.py:77-82` | `_connector_hook` 中：alpha=1.0 走原路径，否则用 `output * (1 - alpha + alpha * weights)` |
| `scripts/eval_acib.py:60` | argparse 添加 `--scoring_alpha`（default=0.3） |
| `scripts/eval_acib.py:88,143,239` | `patch_make_policy` 接收并设置 `scoring_alpha` |

## 数学验证

```
alpha=0.0, weights=0.23 -> effective_weight=1.0000  (pass-through ✓)
alpha=0.3, weights=0.23 -> effective_weight=0.7690  (tokens retain 76.9% signal)
alpha=0.5, weights=0.23 -> effective_weight=0.6150
alpha=1.0, weights=0.23 -> effective_weight=0.2300  (纯乘性 ✓)
```

## 兼容性
- **训练不受影响**：`ACIBConfig` 默认 `scoring_alpha=1.0`，训练走原路径（纯乘性 + IB 梯度完整）
- **`--disable_scoring`**：完全禁用 ACIB hook（直接 return output），优先级高于 `scoring_alpha`
- **正在运行的 eval 进程**：不受影响（已加载旧代码到内存）

---
