# audit llm gold fewshot source

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_llm-gold-fewshot-source_20260516T055043_result.json`
- **Structured JSON:** [`f755228318072ea95efb.json`](../../sessions/f7/f755228318072ea95efb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
FEW-SHOT EXAMPLES SOURCE: silver training set (split_info["train_indices"]), explicitly excluding gold
DATA LEAKAGE: NO
EVIDENCE:
```

`exp_llm_judge_gold.py:411-428`:
1. 加载 `checkpoints/split_info.json` 获取 train/test split
2. 仅从 `split_info["train_indices"]` 中选取 windows（第421行）
3. **显式排除所有 gold set windows**（第423-425行）：
   ```python
   gold_ids = set(gold_labels.keys())
   train_windows = [w for w in train_windows
                    if f"{w['trajectory_id']}__w{w['window_idx']}" not in gold_ids]
   ```
4. 从过滤后的 training pool 中，选 confidence>=3 的 5 个样本（3 stagnation + 2 progress），seed=42，每条来自不同 trajectory（第126-160行 `select_few_shot_examples`）

**结论：0.910 macro_F1 是有效的，few-shot examples 来自训练集且显式排除了 gold set。token 增加（+5052）是因为注入了 5 条完整 trajectory window 文本（每条 truncate 到 3000 chars）。**

---
