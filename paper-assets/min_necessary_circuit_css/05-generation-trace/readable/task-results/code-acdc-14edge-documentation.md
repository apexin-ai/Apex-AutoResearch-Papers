# code acdc 14edge documentation

**Transformer Model EAP-IG** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_acdc-14edge-documentation_20260513T013621_result.json`
- **Structured JSON:** [`87cdc0b83ea75c59c06c.json`](../../sessions/87/87cdc0b83ea75c59c06c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

注释已添加。现在整理完整产出。

---

## 产出汇总

### 1. ACDC 14 条 Infinity 边（保留电路）

| # | Edge |
|---|------|
| 1 | `a0.h1->a9.h9.v` |
| 2 | `a10.h0->logits` |
| 3 | `a11.h2->logits` |
| 4 | `a5.h5->a8.h6.v` |
| 5 | `a7.h9->a9.h9.q` |
| 6 | `a8.h6->a9.h6.q` |
| 7 | `a8.h6->a9.h9.q` |
| 8 | `a9.h6->logits` |
| 9 | `a9.h9->logits` |
| 10 | `input->m0` |
| 11 | `m0->a10.h0.v` |
| 12 | `m0->a5.h5.q` |
| 13 | `m0->a9.h6.v` |
| 14 | `m0->a9.h9.v` |

### 2. ACDC cache score 分布（32491 边总计）

| Score | Count | 含义 |
|-------|-------|------|
| **inf** | **14** | 保留边 — 所有 tao 值都未能剪掉 |
| 0.09 | 14 | 在 tao=0.09 时被剪掉（最后一轮） |
| 0.07 | 11 | 在 tao=0.07 时被剪掉 |
| 0.05 | 50 | 在 tao=0.05 时被剪掉 |
| 0.03 | 138 | 在 tao=0.03 时被剪掉 |
| 0.01 | 32264 | 在 tao=0.01 时被剪掉（第一轮，最不重要） |

`tao_exps=[-2]` + 默认 `tao_bases=[1,3,5,7,9]` → tao ∈ {0.01, 0.03, 0.05, 0.07, 0.09}，共 5 轮扫描。

### 3. 14 条 score=0.09 边（最后被剪掉的一批）

| # | Edge |
|---|------|
| 1 | `a10.h1->logits` |
| 2 | `a10.h2->logits` |
| 3 | `a10.h6->logits` |
| 4 | `a10.h7->logits` |
| 5 | `a6.h9->a8.h6.v` |
| 6 | `a7.h3->a9.h9.q` |
| 7 | `a9.h8->logits` |
| 8 | `m0->a9.h8.v` |
| 9 | `m0->a9.h9.k` |
| 10 | `m1->a9.h9.v` |
| 11 | `m2->a9.h9.v` |
| 12 | `m4->a9.h9.v` |
| 13 | `m6->a9.h9.v` |
| 14 | `m7->a9.h9.v` |

这 14 条是 ACDC 认为"几乎重要但最终被剪"的边——在 tao=0.09（最大阈值）时才被移除。它们是 inf 边的"边界邻居"。

### 4. 为什么用 `isinf` — 排除 cherry-picking

ACDC 算法（auto_circuit 实现）的工作方式：
1. **初始化所有边 score = inf**（`model.new_prune_scores(init_val=t.inf)`）
2. 对每个 tao 值从小到大扫描，逐条测试边的重要性
3. 不重要的边被赋予 `min(tao, current_score)` 作为 score
4. **从未被剪掉的边保持 score = inf**

因此 `math.isinf(v)` 是读取 ACDC 输出"最终保留电路"的**唯一正确方式**，等价于论文中 "the edges retained in the discovered circuit"。这不是人为选择的阈值，而是算法的二值化输出格式。

### 5. 代码注释已添加

`analysis_fix_v3.py:38-41`，在 `binarize_acdc` 函数上方添加了 4 行注释，解释 ACDC score 语义和 `isinf` 的技术依据。

---
