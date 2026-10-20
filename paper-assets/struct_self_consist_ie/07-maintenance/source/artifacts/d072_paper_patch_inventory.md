# D072 Paper Patch Inventory

**Date**: 2026-05-15

---

## 已就绪可写入的新发现

### 发现 1: Free-form ablation 扩展表格（4-panel）

- **数据来源**: `freeform_ablation_appendix_table.tex`
- **关键数字**: Panel A (LP分布), Panel B (Selection F1: NER +0.18pp / RE +1.69pp), Panel C (QE ρ: 9/10 信号×任务组合提升), Panel D (parse rate 99.95%)
- **写入位置**: `appendix.tex` §app:freeform_ablation — 替换当前简化的 2 列 `tab:freeform_ablation`（6行）为完整 4-panel 版本
- **修改类型**: 替换表格
- **优先级**: P0
- **备注**: 当前 appendix 表格仅有 LP std / tied fraction / selection ΔF1 / VC ρ / parse rate 共 6 行。新表格包含完整 logprob 分布、NER+RE selection F1、全部 5 信号 QE ρ（含 AUROC）、parse rate 四个 panel。信息量提升 4×。

### 发现 2: RE LP Selection Flip 机制分析

- **数据来源**: `freeform_ablation_deep_analysis.md` §1
- **关键数字**:
  - 全部 7 种关系类型均从 constrained 负 gap 翻转为 free-form 正/零 gap（universal flip）
  - PART-OF 翻转最大 +6.52pp，HYPONYM-OF +4.45pp
  - Win/loss balance: constrained 36:59 (net -23) → free-form 45:45 (net 0)
  - Free-form 选择性放大 RE-difficult 实例 LP 方差（ratio 1.06, p<0.0001），抑制 RE-easy（ratio 0.86）
  - Flip 实例（N=31）关系密度 3.3（基线 1.8 的 2×），constrained LP std 仅 0.0162
- **写入位置**: `discussion.tex` §ablation "RE task-specific interaction" 段落扩展 + `appendix.tex` 新增 §app:freeform_re_flip 详细分析
- **修改类型**: discussion 段落扩展（3-4句 → 8-10句）+ appendix 新增 subsection
- **优先级**: P0
- **备注**: 当前 discussion 仅一句"RE LP selection flips from −0.68pp to +1.69pp"。深层机制（universal across 7 types、selective variance reallocation、win/loss asymmetry）是论文的新贡献，必须写入。

### 发现 3: Non-tied 子集重洗牌分析

- **数据来源**: `freeform_ablation_deep_analysis.md` §2
- **关键数字**:
  - Jaccard(non-tied sets) = 0.472 — 两种 decoding 模式下可区分实例重叠不到一半
  - 87 个实例在 free-form 下新获 LP 区分力（LP range 从 0.032 → 0.098, 3×）
  - 76 个实例失去区分力（LP range 从 0.111 → 0.031）
  - LP range 跨条件 Spearman ρ = 0.488，~76% 方差为条件特异性
- **写入位置**: `discussion.tex` §ablation 新增段落 或 `appendix.tex` §app:freeform_ablation 扩展
- **修改类型**: 新增段落
- **优先级**: P0
- **备注**: 这个发现揭示了一个关键现象：尽管 tied fraction 几乎相同（59.7% vs 57.7%），free-form 实际上重新分配了哪些实例可被 LP 区分。这补充了"compression is intrinsic"的叙事——总体压缩不变，但压缩分布发生了结构性变化。

### 发现 4: 多种子 RE 稳定性数据

- **数据来源**: `multi_seed_stability_table.md` Table A2, B2, C
- **关键数字**:
  - RE Spearman ρ: Qwen VC mean=0.309±0.024, LP mean=0.297±0.022; LLaMA VC mean=0.316±0.009, LP mean=0.308±0.007
  - RE AUROC: Qwen VC mean=0.658±0.010; LLaMA VC mean=0.678±0.007
  - RE ranking stability: EM 一致排最后，SJ 一致第 4；top-3 (VC/LP/FK) 有轻微波动
  - NER ranking 完美稳定: VC > SJ > EM > FK > LP 在全部 6 个 seed×model 组合一致
- **写入位置**: `appendix.tex` §app:multiseed — 扩展 `tab:multiseed` 加入 RE 行，或新增 RE 表
- **修改类型**: 表格扩展 + 文本新增
- **优先级**: P0
- **备注**: 当前 tab:multiseed 仅含 NER 数据。RE 数据已计算完毕且稳定性特征不同（top-3 有波动 vs NER 完美一致），值得单独讨论。RE 结论标注为"preliminary, single benchmark"需要这些稳定性数据支撑。

### 发现 5: LLaMA SciERC 数据更正（exp_007 → exp_018）

- **数据来源**: `multi_seed_stability_table.md` §LLaMA SJ ρ correction
- **关键数字**:
  - 旧值（contaminated exp_007）: seed42 SJ ρ = 0.363, σ ≈ 0.004
  - 新值（fresh exp_018 r1024）: seed42 SJ ρ = 0.310, mean = 0.325, σ = 0.021
  - σ 增大 ~5×，旧数据人为压缩了方差
- **写入位置**: `appendix.tex` §app:robustness — "LLaMA-3.1-8B-Instruct replicates the structural-over-surface ordering on SciERC NER (SJ ρ=0.363, FK ρ=0.327)" → 更正为 fresh values (SJ ρ=0.325±0.021)
- **修改类型**: 数字更正
- **优先级**: P0
- **备注**: 当前论文 appendix robustness 段落引用的 LLaMA SciERC SJ ρ=0.363 是 contaminated exp_007 的值。必须替换为 exp_018 的 fresh 数据。定性结论不变（structural > surface），但具体数字需要更正。FK ρ=0.327 也需核实更正（exp_018 seed42 FK=0.2352, mean=0.256±0.024）。

### 发现 6: Per-signal TOST δ* 精确值

- **数据来源**: `tost_breakpoint_delta_star.md`
- **关键数字**:
  - NER: SJ δ*=1.28pp, LP δ*=1.80pp, EM δ*=2.07pp, VC δ*=2.29pp, FK δ*=3.38pp
  - RE: LP δ*=2.86pp, SJ δ*=3.76pp, FK δ*=4.22pp, EM δ*=5.17pp, VC δ*=6.53pp
  - NER 所有信号在 δ=5pp 通过，RE 只有 LP/SJ/FK 通过
- **写入位置**: `appendix.tex` §app:diversity TOST 段落 — 当前文本仅给范围（"approximately 1.3pp to 3.4pp on NER"），可加小表格或在文本中列出具体值
- **修改类型**: 文本扩展或新增迷你表格
- **优先级**: P1
- **备注**: 当前文本已包含近似范围，精确值增加透明度但不改变结论。

### 发现 7: Free-form QE 信号全面提升

- **数据来源**: `freeform_ablation_results.md` §3
- **关键数字**:
  - NER: 全部 5 信号 ρ 提升（FK +0.053, VC +0.030, EM +0.023, SJ +0.018, LP +0.008）
  - RE: 4/5 信号提升（FK +0.039, LP +0.038, SJ +0.023, EM +0.002），仅 VC 下降（-0.026）
  - FK 两个 subtask 一致提升最大
- **写入位置**: `discussion.tex` §ablation — 当前仅提"NER VC ρ: 0.379→0.409"一个数据点，应扩展为完整图景
- **修改类型**: 段落扩展（1句 → 3-4句）
- **优先级**: P1
- **备注**: 加入 4-panel 表格后（发现 1），这些数字自动可见。但 discussion 文本应引用关键趋势。

---

## 已在论文中的内容（无需修改）

| 内容 | 位置 | 状态 |
|------|------|------|
| Free-form ablation 基本结论 | discussion.tex §ablation | ✓ 已写入 |
| TOST δ* 范围 | appendix.tex §app:diversity | ✓ 已写入（近似值） |
| Qwen3 thinking tokens confound | experiments.tex footnote + limitations.tex | ✓ 已写入 |
| VC eq6 vs majority threshold (Δρ=+0.127 NER) | method.tex Eq.6 footnote | ✓ 已写入 |
| Multi-seed NER 稳定性 | appendix.tex tab:multiseed | ✓ 已写入 |
| LLaMA CoNLL N=16 3-seed | appendix.tex tab:robustness | ✓ 已写入 |

---

## 等待中的结果

| 项目 | 状态 | 预计 |
|------|------|------|
| exp_017 LLaMA CoNLL N=16 | 3 seed 全部 DONE (s42/s123/s456) | ✓ 已完成，数据已在 tab:robustness |
| exp_017 LLaMA CoNLL N=8 r1024 | 2 个 entry RUNNING/killed | 可能需要重跑 |
| N=16 三种子 SCS 分析 | 分析中 | 待完成 |

---

## 论文修改工作量估算

### 必须改的 section

| Section | 修改项 | 工作量 |
|---------|--------|--------|
| `appendix.tex` §app:freeform_ablation | 替换 tab:freeform_ablation 为 4-panel 版本 | 15 min（LaTeX 已就绪） |
| `appendix.tex` §app:freeform_ablation | 新增 RE flip 机制 + non-tied reshuffling 段落 | 45 min |
| `appendix.tex` §app:multiseed | 扩展 tab:multiseed 加入 RE 数据 + 讨论 RE ranking stability | 30 min |
| `appendix.tex` §app:robustness | 更正 LLaMA SciERC 数字 (exp_007→exp_018) | 15 min |
| `discussion.tex` §ablation | 扩展 RE flip 段落 + QE 全面提升趋势 | 30 min |

### 可选改的 section

| Section | 修改项 | 工作量 |
|---------|--------|--------|
| `appendix.tex` §app:diversity TOST | 加入 per-signal δ* 表格 | 15 min |
| `conclusion.tex` | 提及 free-form RE flip 作为 nuance | 5 min |

### 总预计工时

- **P0 必须项**: ~2.5 小时
- **P1 可选项**: ~20 分钟
- **总计**: ~3 小时

### 修改依赖关系

```
发现1 (4-panel table) ← 独立，可直接替换
发现2 (RE flip) ← 依赖发现1的 Panel B 数据，但文本独立
发现3 (non-tied reshuffling) ← 与发现2互补，可合并写
发现4 (RE multi-seed) ← 独立
发现5 (数字更正) ← 独立，最高优先
发现6 (TOST δ*) ← 独立
发现7 (QE提升) ← 依赖发现1的 Panel C，文本独立
```

**建议执行顺序**: 5 (数字更正) → 1 (表格替换) → 4 (RE multi-seed) → 2+3 (RE flip + reshuffling) → 7 (QE提升) → 6 (TOST δ*)
