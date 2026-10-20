# exp check data and build dpo

**Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_check-data-and-build-dpo_20260512T150441_result.json`
- **Structured JSON:** [`d051b323211c74e6b480.json`](../../sessions/d0/d051b323211c74e6b480.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

| 数据源 | 状态 | 数量 |
|--------|------|------|
| AAVE 语料 (PID 142096) | **进行中**（已运行 ~20min） | 32 条可用 / 60 条失败 |
| Baseline traces | **就绪** | 137 条可用，覆盖 task 0-19 |
| **DPO 偏好对** | **构建成功** | **1434 对**（目标 ≥500） |

输出：`/root/democalib/data/dpo_pairs.jsonl`

**偏好对统计**：
- 20 个 task 全覆盖，每 task 21-132 对
- avg prompt: 2736 chars, avg chosen: 127 chars, avg rejected: 166 chars

**样本质量**：
- Chosen（AAVE 校准）：更直接、口语化（"I ain't gonna", "I be traveling"）
- Rejected（baseline）：更正式礼貌（"Could you please", "Can you proceed"）
- 符合设计意图

**注意**：AAVE 生成仍在跑，第一批 60 条全部失败（空 traj）。当前 1434 对已远超目标，可直接开始 DPO 训练。后续 AAVE 新数据生成完成后可追加构建更多偏好对。

---
