# paper status review loop20

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_status-review-loop20_20260516T011434_result.json`
- **Structured JSON:** [`517a874a9accbc7a84d8.json`](../../sessions/51/517a874a9accbc7a84d8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 论文完成度审查报告

---

### 1. abstract.tex — **95%**
- 完整，包含所有关键数字和 narrative
- 数字核对通过：25.59pp, 58.04%, 83.63%, 72.96%, 53.7–67.2%, 42–43%, TOST p=0.007
- 无 TODO/placeholder

### 2. introduction.tex — **95%**
- 完整的三段式 narrative + 三个 contribution bullets
- 数字一致：1.24pp (5-seed) / 1.18pp (3-seed matched) 两个数分别使用正确
- 所有引用存在于 bib 中
- 无 TODO/placeholder

### 3. method.tex — **95%**
- 三种 formulation 定义完整，公式 (1)–(3) 就位
- CWM failure mode 分析详尽
- Oracle framework 含 ICC block-correlation model
- 无 TODO/placeholder

### 4. experiments.tex — **90%**
- 5 个 subsection + Analysis 全部有实质内容，7 个 analysis paragraph (a–g)
- 3 个表格 (main_results, scaling, repo_level) 数据完整
- **主要缺口：CWM 8B 行为 "---"（in progress）**，Table 3 caption 已标注
- 数字核对：

| 指标 | 用户提供 | 论文中 | 状态 |
|------|---------|--------|------|
| CLS 8B s42 test | 84.48% | 84.48% | ✓ |
| CLS 8B s123 test | 85.60% | 85.60% | ✓ |
| CLS 4B s42 test | 83.63% | 83.63% | ✓ |
| CLS 8B s42 ckpt-1000 test | 83.52% | 83.52% (seq-len ablation) | ✓ |
| CWM 4B s42 test | 58.04% | 58.04% | ✓ |
| CWM 4B s123 test | 59.09% | 59.09% | ✓ |
| Majority test | 72.96% | 72.96% | ✓ |
| TOST p-value | 0.007 | 0.007 | ✓ |
| Multi-seed gap (mean) | **25.99pp** | **25.59pp** | **⚠️ 不匹配** |
| CWM 8B | pending | --- | ✓ (已标注) |
| Majority val | 75.88% | 未报告 | — 正常，论文只报 test |
| Val numbers (90.28%, 88.23%, etc.) | 用户提供 | 未报告 | — 正常 |

**数字问题**：论文中统一使用 25.59pp（CLS 4B s42 83.63% − CWM 4B s42 58.04%，单 seed 同 size 对比）。用户提供的 25.99pp (mean) 在论文中无对应。需确认：这个 mean 是否应替换 25.59pp，还是用户侧的计算口径不同。

### 5. related_work.tex — **95%**
- 5 个 paragraph 结构清晰，覆盖 execution simulation / verification / learned verifiers / APR / NLP formulation
- 每段末尾有定位声明
- 无 TODO/placeholder

### 6. conclusion.tex — **95%**
- 完整总结 + Limitations + Future work
- Limitations 显式提到 CWM 8B 未完成、单 seed repo-level 等
- 无 TODO/placeholder

### 7. appendix.tex — **85%**
- Oracle 分析表 + 图就位
- 三项 ablation (LoRA rank, majority voting, seq-length) 完整
- **潜在补充**：缺 hyperparameter 详表（learning rate, batch size, epoch 数, LoRA config 等完整列表）——ARR 审稿人可能会要求

### 8. references.bib — **90%**
- 22 条，均有完整字段
- 部分条目 author 用 "others" 省略（chen2021humaneval, austin2021mbpp, qwen2025qwen3）——ARR 提交可接受
- 无 incomplete/dangling 条目

### 9. Figures — **100%**
三个引用的图全部存在于 `artifacts/figures/paper/`：
- `fig1_reformulation.pdf` ✓
- `fig2_scaling_gap.pdf` ✓
- `fig3_oracle_stratified.pdf` ✓

### 10. 格式检查
- `\usepackage[review]{acl}` — anonymous review mode ✓
- `acl.sty` + `acl_natbib.bst` 就位 ✓
- `main.pdf` 已编译存在 ✓
- 零 TODO/FIXME/placeholder/`\textcolor{red}` ✓

---

## 论文整体完成度：**~92%**

## 提交前 Critical Path

| 优先级 | 事项 | 阻塞性 |
|--------|------|--------|
| **P0** | CWM 8B eval 完成 → 填入 Table 3 + 更新 abstract/intro/conclusion 中的相关讨论 | 高——如果赶不上 deadline，当前 "in progress" 表述可提交但削弱论文 |
| **P0** | 确认 25.59pp vs 25.99pp 口径——如果 25.99 是正确的 multi-seed mean，需更新 abstract、intro、experiments、conclusion 中全部 5 处 | 高——数字一致性 |
| **P1** | Appendix 补 hyperparameter 完整表（training config: lr, batch, warmup, LoRA rank/alpha, max_seq_len, epochs per formulation×size） | 中——reviewer 常要求 |
| **P2** | 最终编译确认 PDF 页数在 EMNLP 8 页限制内（不含 references + appendix） | 中 |
| **P2** | bib 条目 author 补全（去掉 "others"） | 低——不影响审稿 |

---
