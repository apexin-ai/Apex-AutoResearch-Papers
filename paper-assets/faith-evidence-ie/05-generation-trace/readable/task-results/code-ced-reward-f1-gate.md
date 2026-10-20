# code ced reward f1 gate

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_ced-reward-f1-gate_20260514T152547_result.json`
- **Structured JSON:** [`2080268cfbc8b37611e1.json`](../../sessions/20/2080268cfbc8b37611e1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

### 修改内容

**1. F1 门控** (`grpo_trainer.py:221-235`)
在 `CEDRewardWrapper.__call__` 的 gold_map 构建之后、triple_rewards 循环之前，插入 F1 gate：遍历 pred triples，检查是否有至少一个 (head, relation, tail) 匹配 gold_map。无匹配则 CED reward = 0，跳过 NLI 计算。

**2. `--lr` alias** (`grpo_trainer.py:372`)
`--learning_rate` 添加了 `--lr` 别名。

**3. 单元测试** (`freige/tests/test_ced_gate.py`)
3 个 case 全部 PASSED：
- `test_empty_output_returns_zero` — 空输出 → 0
- `test_correct_triple_returns_positive` — 正确 triple → > 0
- `test_nonsense_output_returns_zero` — 废话输出 → 0

---
