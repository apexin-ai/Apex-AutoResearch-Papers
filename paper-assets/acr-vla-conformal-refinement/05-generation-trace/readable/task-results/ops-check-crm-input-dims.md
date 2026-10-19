# ops check crm input dims

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-crm-input-dims_20260518T085731_result.json`
- **Structured JSON:** [`2a19b9d4ab5d56dd5f94.json`](../../sessions/2a/2a19b9d4ab5d56dd5f94.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果如下：

**obs_only 模式下的 CRM 输入维度：**

| 组件 | 维度 | 计算 |
|---|---|---|
| `obs_feat` | **960** | VLM hidden_size（SmolVLA 冻结输出） |
| `base_action` | **30** | H_EFF × CORRECTION_DIM = 5 × 6 |
| `uncertainty_features` | **0** | obs_only 模式下为 None，不拼接 |
| **CRM MLP 总输入维度** | **990** | 30 + 0 + 960 |

**CRM 网络结构（obs_only）：**
- `Linear(990, 256)` → ReLU → `Linear(256, 256)` → ReLU → `Linear(256, 30)`

**总参数量：**
- 990×256 + 256 = 253,696
- 256×256 + 256 = 65,792
- 256×30 + 30 = 7,710
- **总计 = 327,198**

对比 full 模式（input_dim = 30 + 40 + 960 = **1030**），obs_only 少了 40 维的 CGS uncertainty features（30 per-DOF widths + 5 horizon scores + 5 额外）。

---
