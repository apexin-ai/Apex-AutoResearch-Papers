# infra llama bcp 001 check

**Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_llama-bcp-001-check_20260512T181700_result.json`
- **Structured JSON:** [`28303201cf942b0f73fb.json`](../../sessions/28/28303201cf942b0f73fb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。报告如下：

---

## llama-bcp-001 结果报告

### Metrics（Llama-3-8B-Instruct, n=20 each）

| Variant | politeness | question_rate | completion | n |
|---------|-----------|--------------|------------|---|
| baseline | 0.310 | 0.007 | **0.05** | 20 |
| aave_target | 0.514 | 0.004 | **0.05** | 20 |
| single_dim_politeness | 0.360 | 0.007 | **0.05** | 20 |

### H-gate

| Gate | Passed |
|------|--------|
| H1 (baseline viable) | Yes |
| H2 (calibration effective) | **No** — aave_target politeness 反向偏移（0.31→0.51, target=0.2） |
| H3 (completion retention) | Yes（都是 0.05，无差异） |
| **Overall** | **Failed** |

### 与 Qwen 对比 + 三个失败机制

| 失败机制 | Qwen | Llama | 复现？ |
|---------|------|-------|--------|
| 全局抑制（aave completion << baseline） | 0.1 vs 0.368 ✓ | 0.05 vs 0.05 | **否** — 无差异，但因 baseline 已在 floor |
| 跨维度干扰（aave politeness/question 偏离 baseline） | politeness 0.468 vs 0.559 ↓ | politeness 0.514 vs 0.310 **↑** | **是** — 更严重，calibration 方向完全反转 |
| 过校正反弹（single_dim politeness > baseline） | 0.634 > 0.559 ✓ | 0.360 > 0.310 ✓ | **是** |

### 关键发现

Llama-3-8B-Instruct baseline completion = 0.05（仅 1/20 task 成功），远低于 Qwen 的 0.368。模型在 tau-bench customer service 任务上基本不可用，导致 BCP 行为校准的 metrics 缺乏区分度——三个 variant 的 completion 都被钉在 floor 上。跨维度干扰和过校正反弹在 politeness 维度上仍可观测到，但全局抑制因 floor effect 无法判断。

### Conclusion: **negative**

### 清理确认
- cron `llama-bcp-001` 已删除
- vLLM PID 284384 已 kill，cuda:2 已释放（22105 MiB → 3 MiB）
- Registry 已更新为 DONE

---
