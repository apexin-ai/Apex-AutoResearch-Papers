# analysis extract prompt template

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_extract-prompt-template_20260517T180842_result.json`
- **Structured JSON:** [`7e6abebe70930d834ba9.json`](../../sessions/7e/7e6abebe70930d834ba9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/appendix_prompt_template.md`。

内容包含：
- **System prompt**: `VLLMBackend._SYSTEM_MSG`（constraint_extractor.py:167）
- **Math domain prompt** (`EXTRACTION_PROMPT`): 含 Z3 语法规则、操作符白名单、组合数学示例
- **Logic domain prompt** (`LOGIC_EXTRACTION_PROMPT`): 含 fact/rule/derived 类型定义、变量命名规范、3 个递进示例
- **输出 JSON schema**: constraints 数组 + answer + variables
- **实际示例 1**: GSM8K 数学题，16 个去重后约束，跨 12 条 trace 的权重分布
- **实际示例 2**: ProofWriter 逻辑题，单条 trace 提取的 12 个约束（fact + rule）
- **LLM 调用配置**: temperature=0.1, max_tokens=1024, json_object 模式, 6 并发
- **Prompt 选择逻辑**: 按 dataset 字段自动切换 math/logic 模板

---
