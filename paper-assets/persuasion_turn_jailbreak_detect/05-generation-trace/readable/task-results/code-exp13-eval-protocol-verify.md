# code exp13 eval protocol verify

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp13-eval-protocol-verify_20260520T122633_result.json`
- **Structured JSON:** [`0d6d423e5dc7bba604ce.json`](../../sessions/0d/0d6d423e5dc7bba604ce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结论明确：

## exp13 评估协议验证结果

**评估代码无 bug，协议正确。**

关键证据 — `scripts/meanpool_multiseed.py` 第 54-57 行的 `load_ood_eval_set` 函数：

```python
def load_ood_eval_set(ood_path, test_path):
    ood_convs = load_conversations(ood_path)
    test_convs = load_conversations(test_path)
    benign_test = [c for c in test_convs if c["label"] == 0]
    return ood_convs + benign_test
```

`main()` 中调用：
```python
dd_ood_convs = load_ood_eval_set(DD_OOD_DATA, TEST_DATA)
aa_convs = load_ood_eval_set(AA_DATA, TEST_DATA)
```

### 评估集组成

| 评估集 | Jailbreak | Benign | Total |
|--------|-----------|--------|-------|
| DD OOD | 80 (deceptive_delight_all.jsonl) | 38 (test.jsonl benign) | **118** |
| AA OOD | 80 (actorattack_all.jsonl) | 38 (test.jsonl benign) | **118** |

1. **DD OOD**: 80 jailbreak + 38 benign = 118 total
2. **AA OOD**: 80 jailbreak + 38 benign = 118 total
3. **伪影**: 否 — 评估集包含两类样本，macro F1 有意义
4. **已报告 F1 无需修正**

---
