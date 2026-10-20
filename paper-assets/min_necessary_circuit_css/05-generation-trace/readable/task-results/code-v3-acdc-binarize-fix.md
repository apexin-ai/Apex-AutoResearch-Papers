# code v3 acdc binarize fix

**Transformer Model EAP-IG** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_v3-acdc-binarize-fix_20260513T012144_result.json`
- **Structured JSON:** [`2a77d9b2082506991cb4.json`](../../sessions/2a/2a77d9b2082506991cb4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All done. Here's the full report:

---

## 报告

### 1. cache_acdc.json 诊断结果
- 32491 条边，覆盖 GPT-2 Small 全部边
- **14 条边**值为 `Infinity`（ACDC 保留的最终 circuit 边）
- 32477 条边值为有限浮点数（0.01/0.03/0.05 — ACDC 逐步剪枝的 threshold step）
- ACDC 的 cache 格式：保留的边标记为 Infinity，被剪掉的边保留其剪枝 threshold

### 2. 二值化 bug 根因
之前的版本用 `score > 0` 做 ACDC 二值化 → 全部 32491 条边都是正值 → 全选。当前代码已修复为 `math.isinf(v)` → 只选 14 条 Infinity 边。仅残留一个过时的 mode label（"score>0"），已改为 "isinf"。

### 3. 修复方案
- `binarize_acdc`（`math.isinf`）已正确，无需改动
- 修复 mode label：`analysis_fix_v3.py` 中 `"score>0"` → `"isinf"`（显示标签）
- Phase D 需要 `HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1`，已用此方式成功运行

### 4. K=3 Cross-tabulation 2×2 矩阵

|                | CSS ≥ 0.67 | CSS < 0.67 |
|----------------|-----------|-----------|
| CIRCUS-core    | 13 edges  | 2 edges   |
| CIRCUS-other   | 39 edges  | 101 edges |

Total: 155 | Core: 15

### 5. Off-diagonal 百分比
**13.3%** [95% CI: 1.7%, 40.5%]

### 6. CIRCUS-core 绝对边数
**15 条** — < 30 → **触发 D002 标志**

### 7. 3 组 pairwise Jaccard

| Pair | Jaccard | Overlap |
|------|---------|---------|
| eap_ig × edge_pruning | 0.3072 | 47 |
| eap_ig × acdc | 0.0962 | 10 |
| edge_pruning × acdc | 0.0857 | 9 |

### 8. 3-way ratio
**0.0452**（3-way intersection = 7 edges）
3-way edges: `a10.h0->logits, a11.h2->logits, a9.h6->logits, a9.h9->logits, input->m0, m0->a5.h5.q, m0->a9.h9.v`

### 9. 各方法 circuit size（修复后）

| Method | Edges | Mode |
|--------|-------|------|
| eap_ig | 100 | top-100 |
| edge_pruning | 100 | top-100 |
| **acdc** | **14** | **isinf** |
| Union | 155 | — |

### 10. Faithfulness（Phase D）

| Circuit | Edges | CPR | CMD |
|---------|-------|-----|-----|
| css_1.00 | 7 | 0.1095 | 0.9110 |
| css_0.67 | 52 | 0.0634 | 0.9582 |
| method_acdc | 14 | 0.0286 | 0.9937 |
| circus_core | 15 | -0.1081 | 1.1337 |
| method_eap_ig | 100 | -0.1092 | 1.1348 |
| stable_core | 13 | -0.1870 | 1.2143 |
| method_edge_pruning | 100 | -0.2413 | 1.2699 |
| css_0.33 | 155 | -0.4862 | 1.5205 |

CPR 全面偏低（最高 0.11），node-level zero ablation 破坏性较大。CSS-1.0（7 边 3-way 交集）表现最好。

**Gate: PASS_MAIN**（off-diagonal 13.3% ≥ 10%）

---
