# eval mistral bcp 001

**Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_mistral-bcp-001_20260513T062632_result.json`
- **Structured JSON:** [`f37d6f81d7aaaaf28438.json`](../../sessions/f3/f37d6f81d7aaaaf28438.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果总结

**mistral-bcp-001: NEGATIVE → Plan B KILL**

### 核心发现
Mistral-7B-Instruct-v0.3 在 tau-bench retail 环境（16 tools）下**完全无法生成 structured tool_calls**：
- 3/3 baseline 任务 reward=0.0（completion = **0%**）
- 0/35 assistant 响应有 tool_calls（全部 null）
- 模型将 tool call JSON 嵌入 text content 中，vLLM parser 无法解析

### 调试过程
1. 初始尝试 `--tool-call-parser mistral`：tokenizer 不匹配，tool_calls 全 null
2. 加 `--tokenizer-mode mistral`：消除 tokenizer 警告，tool_calls 仍然 null
3. 直接 API 测试 1 tool：正常工作 ✓
4. 直接 API 测试 16 tools：tool_calls 返回空列表 ✗
5. 结论：7B 模型在多 tool 场景下能力不足

### Plan B 判定
- Mistral completion 0% ≤ 20% 阈值 → **KILL**
- 跨模型 BCP 效应无法证明，Plan B（empirical analysis 论文）不可行

### Registry & Artifacts
- Registry: `mistral-bcp-001` → DONE (negative)
- Report: `mistral-bcp-001-report.md`
- Memory: 教训已写入

---
