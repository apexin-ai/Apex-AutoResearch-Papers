# analysis exp 034 pw600

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp-034-pw600_20260518T190404_result.json`
- **Structured JSON:** [`3ef5d8cb136604253460.json`](../../sessions/3e/3ef5d8cb136604253460.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**实验仍在运行，尚未退出。** 进程 PID 69808 活跃中，当前服务器时间 03:05:31 CST，已完成 65/600 题。

以下是基于当前 65 题部分结果的分析：

---

## exp-034 中间分析（65/600 题已完成）

### 核心指标

| 指标 | 值 |
|---|---|
| SC accuracy | **70.77%** (46/65) |
| SICA accuracy | **76.92%** (50/65) |
| **Delta (SICA - SC)** | **+6.15pp** |
| 题目完成数 | 65/600 (10.8%) |
| Extraction rate | 98.85% |
| Contradiction rate | 0.47% (9/65 题有矛盾) |
| 平均耗时 | ~69s/题 |
| 已用时间 | ~75 min |
| 预计剩余 | ~616 min (~10.3h) |

### 按 Depth Breakdown

当前所有 65 题均为 **OWA-D5**（仅此一个 level），无 D0-D4 breakdown。这说明 proofwriter_full.json 数据集可能只包含 D5 难度题目，或题目按 depth 排序，D5 排在前面。

### 对比 Baseline

| 对比 | SC | SICA | Delta |
|---|---|---|---|
| sica_expanded_14b PW 子集 | — | — | +0.3pp |
| **exp-034 (65题中间)** | 70.77% | 76.92% | **+6.15pp** |

当前 delta = +6.15pp **远大于** 预期的 +0.3pp。但需注意：
1. 仅完成 65/600 题，样本量小，置信区间宽
2. 全部是 D5 题目，后续题目分布可能不同
3. +6.15pp 在 n=65 下的标准误约 ±5.3pp (√(p(1-p)/n))，统计显著性待验证

### 异常检查

- 无 ERROR / Traceback / OOM
- vLLM server 正常运行
- 偶有 retry（`Retrying request to /chat/completions`），属正常行为
- 所有请求返回 HTTP 200

### W&B 数据

未在结果文件中发现 W&B run ID。需等实验完成后检查是否有 W&B logging。

### 结论

**状态：RUNNING（非已退出）**

当前中间结果呈现 capability trap 的 **强信号**（SICA > SC +6.15pp），但：
- 样本量过小，不能下最终结论
- 全部 D5 题目，可能存在采样偏差
- 需等 600 题全部跑完再做最终分析

**建议**：等实验完成（预计 ~10h 后），再做完整分析。如需中途检查进度，可随时读取更新后的 results JSON。

---
