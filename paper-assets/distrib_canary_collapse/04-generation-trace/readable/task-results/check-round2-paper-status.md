# check round2 paper status

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_round2_paper_status_20260517T171044_result.json`
- **Structured JSON:** [`2fd00d350757d4bd45d4.json`](../../sessions/2f/2fd00d350757d4bd45d4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have all the data. Here's the full report:

---

## Table 7 状态 (`tab:generalization`, experiments.tex:336-351)

**注意：用户所说的"Table 5"在编译 PDF 中实际是 Table 7。**

| Row | Variation | 状态 | 详情 |
|-----|-----------|------|------|
| 1 | Baseline (Pythia-410M / Wiki) | **已填但数据不一致** | 见下方 |
| 2 | Scale (Pythia-1B / Wiki) | **[TBD]** | 无数据 |
| 3 | Architecture (OPT-1.3B / Wiki) | **[TBD]** | registry 数据已有，可立即填充 |
| 4 | Domain (Pythia-1B / C4) | **[TBD]** | 无数据（实验进行中？） |

**Line 353** 还有一个文字 placeholder：`[Results paragraph placeholder: interpretation of generalization findings will be added once experiments complete.]`

### Table 7 Baseline 行 vs Registry 数据不一致

| 列 | 论文当前值 | Registry 最新值 |
|----|-----------|----------------|
| Naive | 8/8 | **7/8** |
| Diff XCorr | 8/8 | **6/8** |
| Threshold | 8/8 | **6/8** |
| PermG (fwd) | 6/8 | 6/8 |
| PermG (rev) | 0/8 | 0/8 |
| TY | 4/8 | **6/8** |
| K≥4/5 | 6/8 | 6/8 |

4 个值不一致。

---

## 数据不一致：Table 3 Threshold 行 vs Table 5（修复后数据）

Table 3 (`tab:method_comparison`, experiments.tex:103) 的 Threshold 行与 Table 5 (`tab:single-method-errors`, experiments.tex:243) 的 Threshold 行存在严重矛盾，疑似 Table 3 未更新修复后的 Threshold 数字：

| α | Table 3 (Threshold %) | Table 5 per-seed subscripts | Table 5 隐含总比 |
|---|-----------------------|----------------------------|-----------------|
| 0.00 | 62.5% | 3, 1, 1 | 5/24 = 20.8% |
| 0.50 | **100%** | **0, 0, 0** | **0/24 = 0%** |
| 0.75 | 50% | 4, 0, 4 | 8/24 = 33.3% |

α=0.50 的差异最严重：Table 3 说 100%，Table 5 说 0/24。

### Table 6 FPR for Threshold 也可能过时
- Table 6 (`tab:fpr_fnr`, experiments.tex:308): Threshold FPR = 29.2% (12.5--62.5)
- Table 5 α=0.00 subscripts: 3, 1, 1 → per-seed FPR: 37.5%, 12.5%, 12.5%，mean = 20.8%，range = 12.5--37.5
- 29.2% 和 62.5 上界与 Table 5 数据不吻合

---

## TBD / Placeholder 全文扫描

**仅 experiments.tex 有 placeholder，其他所有 tex 文件干净。**

| 文件:行号 | 内容 |
|-----------|------|
| experiments.tex:339 | caption 中 `\textbf{[TBD]}` |
| experiments.tex:346 | `Scale & Pythia-1B / Wiki & \multicolumn{7}{c}{\textbf{[TBD]}}` |
| experiments.tex:347 | `Architecture & OPT-1.3B / Wiki & \multicolumn{7}{c}{\textbf{[TBD]}}` |
| experiments.tex:348 | `Domain & Pythia-1B / C4 & \multicolumn{7}{c}{\textbf{[TBD]}}` |
| experiments.tex:353 | `[Results paragraph placeholder: ...]` |

---

## Round 2 提交 Checklist

### (a) 数据已有，可立即修复

1. **Table 7 OPT-1.3B 行** (experiments.tex:347)：填入 `6/8 & 6/8 & 8/8 & 6/8 & 0/8 & 2/8 & 6/8`
2. **Table 7 Baseline 行** (experiments.tex:345)：更新 4 个值（Naive→7/8, Diff→6/8, Thresh→6/8, TY→6/8），或确认 baseline 使用的是不同 seed/条件
3. **Table 7 caption** (experiments.tex:339)：OPT-1.3B 填入后移除 `\textbf{[TBD]}`（若仍有其他 TBD 行则保留）
4. **Table 3 Threshold 行** (experiments.tex:117-ish)：用修复后数据更新全部 5 个 α 值
5. **Table 6 Threshold FPR** (experiments.tex:324)：同步更新 29.2% (12.5--62.5) 为修复后数值
6. **Table 7 results paragraph** (experiments.tex:353)：用已有 Pythia-410M + OPT-1.3B 数据写初步解读段落

### (b) 等实验完成

1. **Table 7 Pythia-1B / Wiki 行** (experiments.tex:346)：Scale 实验数据
2. **Table 7 Pythia-1B / C4 行** (experiments.tex:348)：Domain 实验数据
3. **Table 7 caption** 中的 `[TBD]`：所有行填完后删除
4. **experiments.tex:353 placeholder**：所有泛化实验完成后写完整解读

---
