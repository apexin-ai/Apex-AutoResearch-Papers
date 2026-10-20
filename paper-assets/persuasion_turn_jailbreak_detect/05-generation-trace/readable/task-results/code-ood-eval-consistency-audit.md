# code ood eval consistency audit

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_ood-eval-consistency-audit_20260520T062115_result.json`
- **Structured JSON:** [`3741b60d0dff0a1b4f5f.json`](../../sessions/37/3741b60d0dff0a1b4f5f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已收集完毕。以下是完整调查报告。

---

## 调查结果

### 1. exp1 DD OOD 数据集组成

**80 jailbreak + 38 benign = 118 samples**

exp1 代码（`src/exp1_roberta_pipeline.py:304-308`）：
```python
dd_convs = load_jsonl(PROJ / "data/generated/deceptive_delight_all.jsonl")  # 80 jailbreak
test_data = load_jsonl(PROJ / "data/plan_002_splits/test.jsonl")           # 76 total
test_benign = [c for c in test_data if c["label"] == "benign"]             # 38 benign
dd_test = dd_convs + test_benign                                            # 118 total
```

exp16 代码（`src/evaluate.py`，由 `scripts/eval_exp16.py` 调用）：**仅加载** `deceptive_delight_all.jsonl` = 80 jailbreak，不混入任何 benign。

### 2. macro F1 计算方式：函数相同，输入数据不同

两者都使用 `f1_score(y_true, y_pred, average="macro")`，无 `zero_division` 参数。**函数一致，但输入数据完全不同**：

| | exp1 | exp16 |
|---|---|---|
| DD OOD 数据 | 80 jailbreak + 38 benign | 80 jailbreak only |
| y_true 包含的类 | {0, 1} | {1} only |
| macro F1 计算 | (F1_class0 + F1_class1) / 2 | (0 + F1_class1) / 2 |
| **系统性偏差** | 无 | **F1 被强制减半** |

### 3. AA OOD 也是 attack-only

`actorattack_all.jsonl` = 80 行，全部 `"label": "jailbreak"`。所有 exp16 AA OOD confusion matrix 均为 `[[0,0],[...]]`，确认 0 benign。**AA OOD F1 同样被系统性低估。**

### 4. 缺失 class 处理方式

sklearn 默认行为：当 class 0 不在 y_true 中但出现在 y_pred 中时（模型把部分 jailbreak 误判为 benign），class 0 仍被纳入 macro 平均，其 recall=0/0→0, F1=0。

效果：macro F1 = (0 + F1_class1) / 2 ≈ **实际检测 F1 的一半**。

### 5. 数值验证

exp16 9class DD OOD 各 seed：

| seed | confusion matrix | accuracy | F1_class1 | macro F1 (报告值) | 若加 38 benign (估算) |
|------|-----------------|----------|-----------|-------------------|---------------------|
| 42 | `[[0,0],[31,49]]` | 61.3% | 0.760 | **0.380** | ~0.83 |
| 123 | `[[0,0],[5,75]]` | 93.8% | 0.968 | **0.484** | ~0.97 |
| 456 | `[[0,0],[26,54]]` | 67.5% | 0.806 | **0.403** | ~0.85 |
| **mean** | | | | **0.422** | **~0.88** |

对比 exp1 9class DD OOD full mean = **0.994**（基于 118 样本评估）。

---

## 结论

**F1=0.422 是评估伪影，不反映模型真实检测能力。**

根因：exp16 OOD 评估用纯 attack-only 数据（80 jailbreak, 0 benign），sklearn macro F1 在缺失 class 时系统性减半。exp1 通过混入 38 benign 避免了这一问题。

**需要修正的数字**：exp16 所有 OOD 评估（DD OOD 和 AA OOD）的 macro F1 都被低估约 50%。论文中 exp1 和 exp16 的 OOD 数字不可直接对比。

**修正方案**（推荐 A）：
- **A（推荐）**：统一评估协议——exp16 OOD 评估也混入 benign 样本（与 exp1 一致），然后重新计算所有 OOD F1
- **B**：改用 binary F1（class 1 only）报告 OOD 结果——避免缺失 class 问题，但语义不同于论文其他部分
- **C**：同时报告 accuracy + F1_class1 + macro F1，让读者了解完整情况

---
