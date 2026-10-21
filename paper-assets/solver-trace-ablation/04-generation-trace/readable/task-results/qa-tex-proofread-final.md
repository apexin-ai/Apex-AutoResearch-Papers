# qa tex proofread final

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_qa_tex-proofread-final_20260515T230139_result.json`
- **Structured JSON:** [`aff3fec0c9cc898de560.json`](../../sessions/af/aff3fec0c9cc898de560.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## TeX 校对报告

**检查文件数**: 9 (main.tex, abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, appendix.tex, limitations.tex)
**整体评价**: 需修正（2处中等问题，5处低优先级）

---

### 发现

#### 中等优先级

1. **[appendix.tex:265] 内部不一致 — H7b 排他性声明错误**
   当前文本: `"Found exclusively in ISR β=0.1 seed 44 (12/89 proved samples)"`
   但 appendix.tex:240 和 appendix.tex:429 均显示 s43 也有 H7b=2 样本。experiments.tex:161 表格 caption 正确使用了 `"primarily s44"`。应改 `exclusively` → `primarily` 或 `"found in ISR β=0.1 seeds 43 (n=2) and 44 (n=12)"`。

2. **[experiments.tex:72] 语法歧义导致数字误读**
   当前文本: `"Total conclusion embedding (H1+H7) is GRPO-universal at 68–100% across both conditions, and is in fact \emph{higher} under random (pooled H1 71% vs. 18% under ISR)."`
   语法主语是 "Total conclusion embedding (H1+H7)"，但 H1+H7 pooled 实际是 ISR 89% > Random 85%，并非 random 更高。括号中的 71% vs 18% 仅指 H1。建议拆句：`"...across both conditions. H1 alone is higher under random (pooled 71\% vs.\ 18\% under ISR)---ISR converts H1 into H7 rather than reducing total embedding."`

#### 低优先级

3. **[全文] 缩略语 GRPO 未展开**
   从 abstract 开始使用 GRPO，全文未出现 "Group Relative Policy Optimization (GRPO)"。建议在 abstract 或 method.tex:15 首次使用处展开。

4. **[全文] 缩略语 FOL 未正式引入**
   Introduction 写 "first-order logic problems"，但后续直接使用 FOL 未做 "(FOL)" 定义。建议在 method.tex:13 或 introduction 中加 "first-order logic (FOL)"。

5. **[全文] SFT 未展开**
   全文未出现 "Supervised Fine-Tuning (SFT)"。建议在 method.tex:64 首次出处展开。

6. **[method.tex:64] NLL 未展开**
   `"SFT baseline (NLL on gold formalizations)"` 中 NLL 未定义为 "negative log-likelihood"。

7. **[conclusion.tex:15] "H8-dominant" 用词不准**
   `"random β=0.1 ranges from H8-dominant (s44) to..."` — s44 实际 H1=82%, H8=18%，H1 才是主导模式。建议改为 `"H8-enriched"` 或 `"highest-H8"`。

---

### 硬约束违规

**无违规。** 七条硬约束全部满足：
- H7a GRPO-universal + ISR amplifies ~5x: experiments.tex:69 正确 (5.15x) ✓
- H7b ISR-specific: 仅出现在 ISR seeds ✓
- genuine rate p=0.182 n.s., 未 claim 显著差异: experiments.tex:80 ✓
- Random H7 per-seed 分解 (38.3%/0%/0%): experiments.tex:70 + Table 1 caption ✓
- premise-count-matched 1.06x: experiments.tex:79 ✓
- ISR 双语义区分 (redundancy vs gaming): experiments.tex:121, conclusion.tex:7, method.tex:83 ✓
- genuine = proved − hacking (set排除): experiments.tex:11 ✓

---

### 引用完整性

- **\cite{}**: 32 个 cite key 与 references.bib 32 条 entry **完全匹配**，无遗漏无多余 ✓
- **\ref{}/\label{}**: 所有 ref 目标均有对应 label，无悬挂引用 ✓
- **LaTeX log**: 无 undefined reference 或 multiply-defined label 警告 ✓（仅有 float `h`→`ht` 和 hyperref PDF string 警告，均为 cosmetic）

---

### 数字一致性

所有关键数字经交叉验证正确：214x collapse ✓, ~5x amplification (5.15x) ✓, σ=47pp ✓, 所有 mean±std ✓, 所有 pooled 百分比 ✓, Fisher p 值 ✓, SFT weighted ISR*=0.595 ✓。

---

### 建议修正（按优先级）

1. **appendix.tex:265** — `exclusively` → `primarily` （与 experiments.tex:161 保持一致）
2. **experiments.tex:72** — 拆句避免 H1+H7 vs H1-only 歧义
3. **method.tex 或 abstract** — 展开 GRPO/FOL/SFT/NLL 缩略语（4 处）
4. **conclusion.tex:15** — `H8-dominant` → `H8-enriched`

---
