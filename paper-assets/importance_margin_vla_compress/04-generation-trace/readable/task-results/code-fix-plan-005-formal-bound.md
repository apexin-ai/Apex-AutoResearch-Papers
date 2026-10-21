# code fix plan 005 formal bound

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_plan_005_formal_bound_20260516T145019_result.json`
- **Structured JSON:** [`94b997349346eccef097.json`](../../sessions/94/94b997349346eccef097.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 完成，输出文件已生成。

**修复内容**: `eval_formal_bound.py` 第 137 行，将 `tokenizer = get_tokenizer_from_policy(model)` 改为：
```python
policy_for_tok = model.policy if hasattr(model, "policy") else model
tokenizer = get_tokenizer_from_policy(policy_for_tok)
```
与 `evaluate.py` 中相同的处理方式——`IMMSmolVLAWrapper` 没有 `.model` 属性，但有 `.policy`（底层的 SmolVLAPolicy）。

**Dry-run 结果**: 2 batch (8 samples) 全部通过，top-k stability 在所有 epsilon 水平下 100%，Lipschitz 常数 L_spectral=1.067，margin 均值=1.46。输出已写入 `results/formal_bound_dryrun.json`。

---
