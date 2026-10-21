# analysis plan006 v2 data audit

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan006-v2-data-audit_20260524T101759_result.json`
- **Structured JSON:** [`1a460f4abc17a1f1b6a4.json`](../../sessions/1a/1a460f4abc17a1f1b6a4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。结论如下：

---

## 审计结论：**使用了 V2 数据管道，数据清洁。**

### 证据链

**1. 脚本入口**：`/root/cert_manip_resist_eval/scripts/analyze_judge_asr_concentration.py`

**2. 数据加载**（第 27-30 行）：从 `src.unified_data_loader` 导入 `load_all_scores`, `load_pairs`, `_is_valid_score`

```python
from src.unified_data_loader import (
    ALL_MODELS, DATASETS, ATTACKS,
    load_all_scores, load_pairs, load_mi_data,
    _is_valid_score,
)
```

**3. V2 过滤函数** — `unified_data_loader.py` 第 50-55 行：

```python
def _is_valid_score(s):
    if s.get("error") or s.get("format_error"):
        return False
    if s.get("winner") not in ("A", "B", "tie"):
        return False
    return True
```

这是 V2 管道的核心特征：
- 过滤 `error` 字段（API error）
- 过滤 `format_error` 字段（malformed response）
- 拒绝非法 winner 值（不是 A/B/tie 的都跳过）

**4. ASR 计算中的调用** — `analyze_judge_asr_concentration.py` 第 54-56 行：

```python
def compute_individual_asr(clean_list, attacked_list, pairs):
    for i in range(n):
        if not _is_valid_score(clean_list[i]) or not _is_valid_score(attacked_list[i]):
            continue  # ← error/invalid 样本被跳过，不计入 ASR
```

clean 和 attacked 两端都做了过滤——只有**两端都有效**的样本对才参与 ASR 计算。

**5. 无 V1 pattern**：整个脚本和 `unified_data_loader.py` 中没有 `.get("winner", "tie")`（V1 把 error 当 tie 的 bug）。

### 数据流总结

```
原始 JSON → load_all_scores() 加载 sample-level 数据
         → compute_individual_asr() 逐样本调用 _is_valid_score() 过滤
         → 只有 valid 样本参与 flip rate 计算
         → Gini/Entropy 基于过滤后的 per-judge ASR
```

**结论：Reviewer 的质疑不成立。** 该分析使用了 V2 数据管道，API error / malformed response 被 `_is_valid_score()` 跳过，不会被错误计入 ASR。

---
