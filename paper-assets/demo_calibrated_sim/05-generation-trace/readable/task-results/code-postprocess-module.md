# code postprocess module

**Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_postprocess-module_20260512T124043_result.json`
- **Structured JSON:** [`51511ae3eea7e3566f29.json`](../../sessions/51/51511ae3eea7e3566f29.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。新增内容：

**后处理 pipeline（`postprocess_traces()`）**：
- `_extract_slots()` — 用 regex 提取 order ID、日期、金额等关键 slot
- `_llm_rewrite()` — 通过 `litellm.completion()` 调用同一 vLLM server 改写 user turn
- `_rewrite_with_validation()` — 改写后用 detector 重新检测 + slot 一致性检查，最多重试 3 次
- `_postprocess_single_trace()` — 单条 trace 的完整改写流程：先降采样 question，再降采样 politeness（基于改写后状态重新检测）
- `postprocess_traces()` — 批量处理所有 trace，输出每条 pre/post 对比和总体汇总

**集成到 `generate_corpus()`**：trace 生成后、保存前调用，改写后重新计算 `behavioral_stats`

**新增 CLI 参数**：`--target-question-rate`（默认 0.10）、`--target-politeness-rate`（默认 0.20）、`--skip-postprocess`（消融对比用）

**metadata 增强**：区分 `prompt_*_rate`（prompt 层目标）和 `target_*_rate`（后处理目标），记录 `postprocessed` 标记

---
