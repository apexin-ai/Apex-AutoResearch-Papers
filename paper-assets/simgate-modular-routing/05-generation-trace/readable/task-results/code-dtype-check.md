# code dtype check

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_dtype-check_20260514T070330_result.json`
- **Structured JSON:** [`4d566dca341ad13f8220.json`](../../sessions/4d/4d566dca341ad13f8220.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修正完成，语法验证通过。

### 结果

| 文件 | 问题 | 状态 |
|------|------|------|
| `src/router_sft_train.py` L303 | `dtype=torch.bfloat16` → `torch_dtype=torch.bfloat16` | **已修正** |
| `src/training/implicit_router_sft.py` L308, L407 | 已正确使用 `torch_dtype=` | 无需修改 |

### 影响范围

所有通过 `router_sft_train.py` 训练的 router 分类器实验都受影响——模型实际以 **fp32** 加载和训练，而非预期的 bf16。具体影响：

- **显存占用翻倍**：fp32 参数量是 bf16 的 2 倍，可能限制了 batch size
- **训练速度变慢**：fp32 计算无法利用 A6000 的 bf16 tensor core 加速
- **模型精度可能略有差异**：fp32 精度更高，已完成实验的结果不一定变差，但与预期配置不一致
- `implicit_router_sft.py` 的实验不受影响

---
