# code exp016 actadd steering

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp016-actadd-steering_20260518T200616_result.json`
- **Structured JSON:** [`e433a49a18cf3c85b666.json`](../../sessions/e4/e433a49a18cf3c85b666.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已写入 `artifacts/training/run_exp016_actadd_steering.py`。

核心设计：
- **方向加载**: `directions.pt[:, 1, :]` 取 sycophantic direction，L2 归一化后乘 alpha
- **Steering hook**: 注册在 7 个 target layers 上，仅在 `seq_len == 1`（自回归生成阶段）时激活，prompt encoding 不受影响
- **NLI 判断**: 用 `nli-deberta-v3-base` 比较初始回复和生成回复，entailment > contradiction 判为 stance consistent
- **NoF**: invalid_pressure 下保持立场的比例；**WRR**: valid_correction 下修正立场的比例
- **数据加载**: 灵活的 JSONL 解析，支持 `messages` 或 `turns` 字段，多轮自动提取 prompt pairs 并按 turn depth 分层报告

---
