# code exp002 prompt templates

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp002_prompt_templates_20260521T080422_result.json`
- **Structured JSON:** [`f8de898e4caec9996c5d.json`](../../sessions/f8/f8de898e4caec9996c5d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

ALL CHECKS PASSED。

完成情况：

1. **现有 MMLU 模板未改动** — 原 `TEMPLATES` + `format_prompt()` 完全保留
2. **新增 3 个 benchmark 各 6 个模板变体**：
   - **GSM8K**：生成式，全部 6 个变体都引导模型在 `####` 后给出答案。变体覆盖简洁指令(1)、步骤要求(2)、Q/A 格式(3)、角色设定(4)、CoT 引导(5)、紧凑格式(6)
   - **ARC-Challenge**：动态选项数（3-5），6 种选项布局风格（vertical/inline/indented/bulleted/verbose/compact），已验证 5 选项正确生成 A-E 标签
   - **HellaSwag**：句子补全 MC，6 个变体适配 continuation 语境
3. **统一接口** `format_benchmark_prompt()` 支持所有 4 个 benchmark，MMLU 委托给原 `format_prompt()`
4. **测试全部通过** — 3 benchmark × 6 模板 + zero-shot + ARC 5 选项动态测试

---
