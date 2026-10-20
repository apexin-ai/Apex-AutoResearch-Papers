# code n200 phase2 prompt gen

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_n200_phase2_prompt_gen_20260522T103905_result.json`
- **Structured JSON:** [`92fe0686956a9a890e26.json`](../../sessions/92/92fe0686956a9a890e26.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

总数 200，验证全通过。合并后按类别分布（含 18 个 legacy 映射到对应类别）：

| 类别 | 新增 | 旧有 | 总计 | 占比 |
|------|------|------|------|------|
| content_constraint | 93 | 7 | 100 | 50% |
| position_constraint | 35 | 5 | 40 | 20% |
| format_constraint | 27 | 3 | 30 | 15% |
| count_constraint | 17 | 3 | 20 | 10% |
| compound_constraint | 10 | 0 | 10 | 5% |

产出：
- `scripts/generate_ir_prompts.py` — 批量生成脚本（seed=42 可复现）
- `data/instruction_retention_prompts_200.json` — 200 个 prompt（18 旧 `check_fn` 格式 + 182 新 `check_type`/`check_args` 格式），无重复 ID，每个 5 条 user_messages，禁止类约束含诱导性问题。

---
