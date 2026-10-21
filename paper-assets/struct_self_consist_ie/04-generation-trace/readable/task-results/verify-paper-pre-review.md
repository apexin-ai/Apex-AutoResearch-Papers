# verify paper pre review

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_paper_pre_review_20260515T222657_result.json`
- **Structured JSON:** [`1dae01ce2b730ce26ff7.json`](../../sessions/1d/1dae01ce2b730ce26ff7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 论文预检报告

### 1. 交叉引用完整性 ✅ PASS
- main.log 中零 undefined reference 警告
- 零 "Citation undefined" 警告
- 零 multiply-defined label 警告

### 2. 表格/图引用一致性 ✅ PASS
- **零 broken references**（所有 `\ref` 目标均存在）
- 23 个 orphan labels，全部良性：
  - 节标签（sec:introduction, sec:method 等）— 结构性定义，标准做法
  - 方程标签（eq:em, eq:fk, eq:logprob, eq:sj_instance）— 完整性保留
  - 附录节标签（app:fk_independence, app:multiseed 等）— 内容通过表格标签间接引用
  - 2 个附录图标签（fig:reliability, fig:temperature_robustness）— 紧邻讨论文本，无需显式 `\ref`

### 3. 数据一致性抽查 ✅ PASS

**tab:quality_estimation vs. analysis_unified_rho_full.json（N=8, seed=42）：**

| 设置 | 信号 | 论文 ρ | JSON ρ | 匹配 |
|------|------|--------|--------|------|
| SciERC NER | SJ | .360 | 0.3599 | ✓ |
| SciERC NER | FK | .267 | 0.2665 | ✓ |
| CoNLL (Qwen) | SJ | .436 | 0.4357 | ✓ |
| CoNLL (Qwen) | FK | .400 | 0.3998 | ✓ |
| CoNLL (LLaMA) | SJ | .431 | 0.4314 | ✓ |
| CoNLL (LLaMA) | FK | .428 | 0.4277 | ✓ |

所有 AUROC 值也逐一验证通过。

**tab:scale_ablation：** 8B 值与 tab:quality_estimation 存在预期差异（SciERC NER SJ .383 vs .360），表格 caption 已注明 "8B recomputed under matched conditions"。4B 源数据仅存于远程服务器（`exp_scale_qwen3_4b_conll/scale_ablation_report.json`），本地无法验证。

### 4. 格式检查 ✅ PASS
- `\usepackage[review]{acl}` ✓
- `\author{Anonymous}` ✓
- references.bib 零重复 bib key ✓
- 全部 .tex 文件零 TODO/FIXME/XXX 残留 ✓

### 5. 页数验证 ✅ PASS
- 正文（Sections 1–6 + Limitations + Ethics）：第 1–8 页（8 页，符合 ACL 限制）
- References：第 9–11 页
- Appendix（A Notation 起）：第 11–21 页
- 总计 21 页

### 非阻塞观察
- 5 处 overfull hbox 警告（双栏排版常见，不影响可读性）
- tab:scale_ablation 的 4B 数据无法在本地交叉验证（源文件在 autodl-5090 服务器上）

### 结论
**PASS — 可以安全进入 Round 9 审稿。**

---
