# validate expert sft data quality

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_validate_expert-sft-data-quality_20260514T153606_result.json`
- **Structured JSON:** [`585e86d3242c4ddd6659.json`](../../sessions/58/585e86d3242c4ddd6659.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据已验证完毕。

## 数据质量验证

- **总条数**: 2800（收集中）
- **收集进度**: 2800/~3553, PID 340587 存活

### move vs put
- move actions: 3752, put actions: 0 (100% move)
- 含 move 动作的轨迹: 2451/2800 (87.5%)

### 关键结论：**数据有效，move 不是假阳性**

原因（来自 `collect_expert_trajectories.py` 源码）：

1. **`move` 是 ALFWorld 内置 expert agent (`HandCodedTWAgent`) 的标准动作**，环境正确响应 "You move the X to the Y"
2. **成功判定基于 `state.won` 游戏引擎标志**（第~140行），而非文本匹配。只有 `won=True` 的轨迹才被保存
3. 收集脚本 `infer_assessment` 函数明确将 `"you move"` 视为 positive（与 `"you put"` 等价处理）

### 抽样 20 条检查
- 真阳性: 20/20 — 所有轨迹都经过 `state.won` 验证
- 假阳性: 0
- 末尾 env response 看起来像"未完成"是因为数据格式：最后一条 message 是 assistant action，对应的 env response 未录入（轨迹在 `done=True` 后终止）

### 全量最后 env response 分布
| 模式 | 数量 | 比例 |
|------|------|------|
| You arrive... | 2068 | 73.9% |
| open/close | 565 | 20.2% |
| You pick up... | 87 | 3.1% |
| Nothing happens | 77 | 2.8% |

这些是**倒数第二个** action 的 response，不是最终结果。

### 任务类型
- put 类任务: 2504 (89.2%)
- look/examine 类: 302 (10.8%)

## 建议
**数据可用，无需过滤或重新收集。** `move` 是 ALFWorld expert 的原生动作，game engine 已通过 `won` flag 确认每条轨迹任务完成。Reviewer 的担忧不成立。

---
