# code datagen script

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_datagen_script_20260518T045339_result.json`
- **Structured JSON:** [`fbfc7ed7532e41f6bfda.json`](../../sessions/fb/fbfc7ed7532e41f6bfda.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已写入 `artifacts/data/generate_calibration_data.py`。

核心设计：

- **两阶段生成**：Phase 1 并发批量生成骨架（每批 `--batch-size` 个），Phase 2 并发为每个骨架生成 A/B 两条对话
- **共享 Turn 1**：对话生成 prompt 明确要求 condition_b 的 Turn 1 与 condition_a 完全一致
- **correction_turn 变化**：`build_filler_instructions()` 根据 correction_turn 动态生成中间轮次指令，turn 3/4/5 均支持
- **证据强度分层**：`EVIDENCE_GUIDANCE` 字典为 strong/medium/weak 分别提供纠正和施压的风格指导
- **流式写入 + 续接**：每对生成后立即 flush 到 JSONL，`--resume` 读取已有 pair ID 跳过已完成的
- **API 双支持**：优先 Anthropic，fallback OpenAI，统一通过 `call_llm()` 封装，含指数退避重试

---
