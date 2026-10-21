# diag exp012 ner prompt test

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_exp012_ner_prompt_test_20260515T173001_result.json`
- **Structured JSON:** [`32c8106f07186f50fdf7.json`](../../sessions/32/32c8106f07186f50fdf7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

测试脚本已写入。它测试 4 个变体来隔离根因：

| 测试 | Prompt | Schema 约束 | 目的 |
|------|--------|-------------|------|
| TEST 1 | v2 exact（含 "output empty list"） | StructuredOutputsParams | 复现问题 |
| TEST 2 | v2 去掉 "empty list" 指令 | StructuredOutputsParams | 测试 prompt 偏差 |
| TEST 3 | 简化 prompt | StructuredOutputsParams | 测试 schema 交互 |
| TEST 4 | v2 exact | 无约束（自由生成） | 测试模型基础 NER 能力 |

**诊断结论：**

**问题不在模型 NER 能力本身，而在 `StructuredOutputsParams` + 8B 模型 + prompt v2 的组合导致系统性输出 `[]`。** 148,000/148,000 条 prediction 全部 gen_tokens=2，100% 空数组。即使 count_22 batch 有 977 个 gold entities 也是零输出。

**最可能的根因排序：**
1. **prompt v2 的 "output an empty list []" 指令** + structured 约束 = 强 attractor 让 8B 模型走 shortest valid path
2. **StructuredOutputsParams array schema** 在第一个 token `[` 后允许直接 `]`，8B 模型 temp=0 下一致选择关闭

**建议修复方向：**
- 从 prompt v2 删除 "If no entities of these types exist in the text, output an empty list []." 
- 或用 70B 模型（已有 batch_config 但未跑 predictions）
- GPU 空闲后运行 `python3 /root/schema-dag-extraction/test_ner_prompt.py` 可在 <3 分钟内验证哪个因素是主因

---
