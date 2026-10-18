# paper d047 round3 global cleanup

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_d047_round3_global_cleanup_20260516T131134_result.json`
- **Structured JSON:** [`2adaa4c51b443b9ef317.json`](../../sessions/2a/2adaa4c51b443b9ef317.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 修改完成，编译报告：

### 1. Errors
**0** — 无 LaTeX 错误

### 2. Undefined references
**0** — 无未定义引用

### 3. 正文页数（§1 → Limitations ��束）
**9 页**（pages 1–9；checklist 从 page 10 开始）

### 4. Overfull hbox > 10pt in body
**1 处** — 10.85pt（page 7, sdgd_negative.tex 中 confidence-gating 段落，长数值链 `0.446→0.276` 导致）

### 5. 总页数
**19 页**

---

### 已完成的修改汇总：

| 任务 | 修改 |
|------|------|
| **C2.1** | abstract.tex + introduction.tex: 添加 "empirically separable" |
| **C2.3** | results.tex L89: `count $\to$ recall` → `count predicts recall`; `confusability $\to$ type confusion` → `confusability predicts type confusion` |
| **C2.4** | introduction.tex: `drives` → `predicts`; results.tex: `drives` → `predicts`; main.tex L249: `drives` → `predicts` |
| **C2.5** | Limitations item 6: 追加 "The controlled stratification provides evidence consistent with a directional relationship but does not establish interventional causality." |
| **C5** | introduction.tex finding(1): typical-batch gap (≈2.2pp) 移至主锚点，31.2pp 作为 extreme-batch 上界 |
| **D1** | checklist.tex: `cross-model replication` → `cross-model consistency check`; results.tex: 添加 Channel 1/2 replication summary 句 |
| **D7** | 全文 p-value 统一：所有 `×10^{-N}` → `< 0.001`；`p < 0.0001` → `p < 0.001`；非显著 `p=0.598/0.762` 等 → 2 位近似值；表格裸数字加 math mode |

---
