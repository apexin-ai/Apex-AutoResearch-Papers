# code ced shortcut fix

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_ced-shortcut-fix_20260514T192919_result.json`
- **Structured JSON:** [`56995db97b469dddbf2d.json`](../../sessions/56/56995db97b469dddbf2d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 tests passed。

修改完成，共改了两个文件：

**`training/grpo_trainer.py`**:
1. `CEDRewardWrapper.__init__` 新增 `recall_penalty: bool = False` 参数，存为 `self.recall_penalty`
2. `__call__` 中用 `matched_gold_keys` set 跟踪命中的 gold keys
3. 计算 `mean_ced` 后，若 `self.recall_penalty=True`，乘以 `recall = len(matched_gold_keys) / len(gold_map)`
4. argparse 新增 `--ced_recall_penalty` flag（默认 False）
5. `main()` 中将 `args.ced_recall_penalty` 传给 CEDRewardWrapper 构造函数

**`tests/test_ced_gate.py`**:
- fixture 补充 `w.recall_penalty = False`（因为 fixture 用 `__new__` 跳过了 `__init__`）

用法：P0 实验不加 flag 行为不变，P0+P1 实验加 `--ced_recall_penalty` 即可启用 recall penalty。

---
