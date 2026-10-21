# audit step3 mi v1check

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_step3-mi-v1check_20260523T193125_result.json`
- **Structured JSON:** [`4716d3fe24f4a893642b.json`](../../sessions/47/4716d3fe24f4a893642b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论

**脚本路径**: `/root/cert_manip_resist_eval/scripts/run_plan001_step3_mi_matrix.py`

**Vote extraction 方式**: **无 V1 bug**

`extract_winner_vector` 函数（第 18-26 行）：
```python
def extract_winner_vector(score_list):
    for s in score_list:
        if isinstance(s, dict) and not s.get("error"):
            w = s.get("winner")       # ← 无默认值，missing 返回 None
            winners.append(w)
        else:
            winners.append(None)       # ← error 条目标记为 None
```

- 使用 `s.get("winner")` 而非 `s.get("winner", "tie")`，missing key 返回 `None`
- error 条目也标记为 `None`
- `compute_pairwise_mi` 中 `None` 被过滤掉，不参与 MI 计算

**数据来源确认**: `main()` 中 `clean_scores, _ = load_all_scores()`，MI 矩阵仅从 clean data 计算。

**附注**: `unified_data_loader.py` 的 `_invert_winners` 确实有 `.get("winner", "tie")` 模式，但该函数仅用于 `position_bias` attacked data 的 swap，不影响 clean data MI 计算。

**K_eff 不受 V1 bug 影响，r(K_eff, η_max) 无需重算。**

---
