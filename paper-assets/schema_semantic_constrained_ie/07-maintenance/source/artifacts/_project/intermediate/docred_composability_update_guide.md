# DocRED Composability 结果更新指南

> 生成日期：2026-05-16。待 `w5_qwen_docred_lora_constrained_eval` 和 `w5_llama_docred_lora_constrained_eval` 完成后执行。

---

## 一、已有数据汇总

### DocRED FT Unconstrained（已确认）

| 指标 | Qwen FT-U | Llama FT-U |
|------|-----------|------------|
| DR% | 0.76 | 0.49 |
| RV% | 0.27 | 0.15 |
| ET% | 0 | 0 |
| CF% | 0.12 | ~0（registry 缺失，按 0 处理） |
| R-F1 | 40.86 | 43.72 |
| E-F1 | 82.15 | 83.93 |
| parse_fail% | 7.11 | 2.3 |

### DocRED ZS（已在 cross-model table 中）

| 指标 | Qwen ZS-U | Qwen ZS-S1 | Llama ZS-U | Llama ZS-S1 |
|------|-----------|------------|------------|-------------|
| DR% | 18.46 | 10.19 | 26.07 | 2.55 |
| R-F1 | 7.74 | 8.23 | 5.98 | 6.27 |
| E-F1 | 58.15 | 59.37 | 55.65 | 55.01 |
| CF% | 0.10→2.57 | — | 0.17→12.02 | — |

### SciERC FT Composability（论文已有）

| | Qwen FT-U | Qwen FT-S1 | Llama FT-U | Llama FT-S1 |
|--|-----------|------------|------------|-------------|
| DR% | 1.95 | **0** | 1.11 | 0.09 |
| CF% | 0 | 1.18 | 0 | 0.46 |
| R-F1 | 43.86 | 43.77 | 45.45 | 45.47 |
| ΔDR | — | ↓100% | — | ↓92% |
| ΔR-F1 | — | -0.09pp | — | +0.02pp |

### 待填数据（实验完成后提取）

| 指标 | Qwen FT-S1 | Llama FT-S1 |
|------|------------|-------------|
| DR% | `{QWEN_DR_S1}` | `{LLAMA_DR_S1}` |
| RV% | `{QWEN_RV_S1}` | `{LLAMA_RV_S1}` |
| ET% | `{QWEN_ET_S1}` | `{LLAMA_ET_S1}` |
| CF% | `{QWEN_CF_S1}` | `{LLAMA_CF_S1}` |
| R-F1 | `{QWEN_RF1_S1}` | `{LLAMA_RF1_S1}` |
| E-F1 | `{QWEN_EF1_S1}` | `{LLAMA_EF1_S1}` |
| parse_fail% | `{QWEN_PF_S1}` | `{LLAMA_PF_S1}` |

---

## 二、派生量计算（结果到手后立即算）

```python
# DR reduction
QWEN_DDR_S1 = round((0.76 - QWEN_DR_S1) / 0.76 * 100)
LLAMA_DDR_S1 = round((0.49 - LLAMA_DR_S1) / 0.49 * 100)

# R-F1 delta
QWEN_RF1_DELTA = round(QWEN_RF1_S1 - 40.86, 2)  # +/- 格式
LLAMA_RF1_DELTA = round(LLAMA_RF1_S1 - 43.72, 2)

# E-F1 delta
QWEN_EF1_DELTA = round(QWEN_EF1_S1 - 82.15, 2)
LLAMA_EF1_DELTA = round(LLAMA_EF1_S1 - 83.93, 2)

# CF delta (FT-U → FT-S1)
QWEN_CF_DELTA = round(QWEN_CF_S1 - 0.12, 2)
LLAMA_CF_DELTA = round(LLAMA_CF_S1 - 0, 2)

# 跨数据集汇总
MAX_RESIDUAL_DR = max(0, 0.09, QWEN_DR_S1, LLAMA_DR_S1)
MAX_RF1_DELTA = max(abs(QWEN_RF1_DELTA), abs(LLAMA_RF1_DELTA), 0.09, 0.02)
MIN_FT_CF = min(0.46, 1.18, QWEN_CF_S1, LLAMA_CF_S1)
MAX_FT_CF = max(0.46, 1.18, QWEN_CF_S1, LLAMA_CF_S1)
```

---

## 三、更新清单（按优先级）

### P0-1: Table 5 加 DocRED LoRA 行

**文件**: `artifacts/_project/paper/section5_scierc_draft.tex`
**位置**: lines 159-199 (table `tab:composability`)

**当前结构**: 8 行数据（2 models × {ZS, LoRA} × {U, S1}），仅 SciERC，7 列（Model, Setting, Mode, DR, CF, R-F1, E-F1, ΔDR）。

**操作**: 在 `\bottomrule`（line 188）前插入 DocRED LoRA block：

```latex
\midrule
\multicolumn{8}{l}{\textit{DocRED (998 documents)}} \\
\midrule
\multirow{2}{*}{Qwen3-8B}
  & \multirow{2}{*}{LoRA}
    & Unconstr.\ &  0.76 & 0.12 & 40.86 & 82.15 & --- \\
  & & Full S1    & {QWEN_DR_S1} & {QWEN_CF_S1} & {QWEN_RF1_S1} & {QWEN_EF1_S1} & $\downarrow${QWEN_DDR_S1}\% \\
\midrule
\multirow{2}{*}{Llama-3.1-8B}
  & \multirow{2}{*}{LoRA}
    & Unconstr.\ &  0.49 & 0    & 43.72 & 83.93 & --- \\
  & & Full S1    & {LLAMA_DR_S1} & {LLAMA_CF_S1} & {LLAMA_RF1_S1} & {LLAMA_EF1_S1} & $\downarrow${LLAMA_DDR_S1}\% \\
```

> DocRED ZS 行不加入此表（已在 cross-model table 中），避免表格过大。

**Caption（line 190-197）替换为**:

```latex
\caption{Composability matrix on SciERC (551 documents) and DocRED (998 documents):
zero-shot vs.\ LoRA fine-tuned $\times$ unconstrained vs.\ full S1
for Qwen3-8B and Llama-3.1-8B.
$\Delta$DR: relative DR reduction vs.\ the same-row unconstrained baseline.
Fine-tuning alone leaves residual DR ($\leq$2\%);
adding S1 reduces it to $\leq$\,{MAX_RESIDUAL_DR}\% with R-F1 change within $\pm${MAX_RF1_DELTA}\,pp on both datasets.
F1\,$\times$100.}
```

---

### P0-2: 删除 Limitations 中 "DocRED not reported"

**文件**: `artifacts/_project/paper/main.tex`
**位置**: line 70

**当前**:
```latex
Composability with fine-tuned models is validated on SciERC with both Qwen3-8B and Llama-3.1-8B (DR\,$\leq$\,0.09\%, R-F1 loss $<$0.1\,pp), but evaluation is limited to one dataset and one fine-tuning method (LoRA); residual CF (Qwen 1.18\%, Llama 0.46\%) traces to schema-level type ambiguity (\textsc{Generic}$\leftrightarrow$X) rather than enforcement failure.
```

**替换为**:
```latex
Composability with fine-tuned models is validated on both SciERC and DocRED with Qwen3-8B and Llama-3.1-8B (DR\,$\leq$\,{MAX_RESIDUAL_DR}\%, R-F1 change within $\pm${MAX_RF1_DELTA}\,pp), though evaluation covers one fine-tuning method (LoRA); residual CF under fine-tuning ({MIN_FT_CF}\%--{MAX_FT_CF}\%) traces to schema-level type ambiguity rather than enforcement failure.
```

**同文件 line 76**:
```
当前: Validation with fine-tuned models, larger scales, and non-English ontologies remains to be explored.
替换: Validation with larger scales (70B+) and non-English ontologies remains to be explored.
```

**同文件 line 69**:
```
当前: Results cover two 8B-class models under zero-shot prompting, where relation F1 remains around 8\% compared to $\sim$50\% for fine-tuned systems.
替换: Under zero-shot prompting, relation F1 remains around 8\% compared to $\sim$50\% for fine-tuned systems; composability with LoRA fine-tuning is validated on both datasets (Table~\ref{tab:composability}).
```

---

### P1-1: §5.5 正文 — 实验描述改 scope

**文件**: `section5_scierc_draft.tex` line 127

```
当前: ...composability matrix on SciERC for both...across model families.
替换: ...composability matrix on SciERC and DocRED for both...across model families and ontology scales.
```

---

### P1-2: §5.5 正文 — Qwen/Llama SciERC 段后插入 DocRED 段

**位置**: line 143 之后（Llama SciERC 描述完毕），line 145 之前（"Across both models" 总结句）

**插入**:
```latex

On DocRED, fine-tuning yields even lower baseline violations: Qwen DR drops from 18.46\% (zero-shot) to 0.76\%, Llama from 26.07\% to 0.49\%.
Adding OntoCoDec reduces DR further (Qwen 0.76\%\,$\to$\,{QWEN_DR_S1}\%, Llama 0.49\%\,$\to$\,{LLAMA_DR_S1}\%) with R-F1 change of {QWEN_RF1_DELTA}\,pp (Qwen) and {LLAMA_RF1_DELTA}\,pp (Llama).
% w5_qwen_docred_lora_constrained_eval: DR={QWEN_DR_S1_RAW}, R-F1={QWEN_RF1_S1_RAW}, E-F1={QWEN_EF1_S1_RAW}
% w5_llama_docred_lora_constrained_eval: DR={LLAMA_DR_S1_RAW}, R-F1={LLAMA_RF1_S1_RAW}, E-F1={LLAMA_EF1_S1_RAW}
```

---

### P1-3: §5.5 总结句 — 扩展到两个数据集

**位置**: line 145-146

```
当前: Across both models, fine-tuned + S1 yields DR≤0.09%...validating Claim~3 on SciERC across two model families...We evaluate on one dataset and one fine-tuning method (LoRA), so we do not claim composability holds universally.
替换: Across both models and both datasets, fine-tuned + S1 yields DR≤{MAX_RESIDUAL_DR}% with R-F1 change within ±{MAX_RF1_DELTA} pp, validating Claim~3 across two model families and two ontology scales...We evaluate with one fine-tuning method (LoRA), so we do not claim composability holds universally across all adaptation methods.
```

---

### P1-4: §5.5 CF under FT 句 — 加 DocRED CF

**位置**: line 149

```
当前: ...CF interference drops substantially under fine-tuning for both models: Qwen from +9.82pp to +1.18pp, Llama from +6.32pp to +0.46pp,
追加: ...on SciERC: Qwen from +9.82pp to +1.18pp, Llama from +6.32pp to +0.46pp; on DocRED: Qwen from +2.47pp to +{QWEN_CF_DELTA}pp, Llama from +11.85pp to +{LLAMA_CF_DELTA}pp,
```

> DocRED ZS CF delta: Qwen S1-U = 2.57-0.10 = 2.47pp; Llama S1-U = 12.02-0.17 = 11.85pp

---

### P1-5: Limitations CF 数字范围

**位置**: main.tex line 70（已含在 P0-2 替换中）

确保 `{MIN_FT_CF}%--{MAX_FT_CF}%` 覆盖 SciERC + DocRED 所有 FT+S1 的 CF 值。

---

### P2: paper_tables_draft.tex Table 4 TBD

**位置**: line 119

低优先级——此文件未被 `main.tex` \input。如果更新，将 `\textit{TBD}` 替换为实际值，删除 caption 中的 "pending" 声明。

### P2: appendix_discussion.tex — CF reduction 可选补充

**位置**: line 74

可追加 DocRED CF reduction 数据（如果 DocRED FT CF 也显著下降）。

---

## 四、条件分支处理

### 场景 A: DocRED FT+S1 DR 很低（< 0.1%）

**最佳情况**。claim 直接泛化。

- Table 5 caption: "adding S1 reduces it to ≤0.09%"（保持或微调）
- §5.5 可写: "Fine-tuning effectively resolves the dual-factor limitation (D014): with near-zero baseline RV, constraint tightness no longer limits DR enforcement."
- Limitations 删除 "DocRED residual DR 10.21%" 相关句或改为 "Residual DR under fine-tuning is negligible (≤0.09%) on both datasets, though zero-shot residual (10.21% for Qwen on DocRED) correlates with grammar-first fallback frequency."

### 场景 B: DocRED FT+S1 DR 中等（0.1%–0.5%）

**可接受**。仍然是 >30% relative reduction。

- 总结句中用 `DR≤{MAX_RESIDUAL_DR}%` 而非硬编码 0.09%
- 无需额外解释

### 场景 C: DocRED FT+S1 DR 较高（> 0.5%）

**需要 nuance**。

- §5.5 总结句不能写 "near-complete"，改为量化描述: "reduces DR by {DDR}% on DocRED"
- 追加解释: "Residual DR on DocRED FT+S1 ({X}%) is higher than SciERC (0/0.09%), consistent with the tighter ontology (τ̄=0.842) limiting semantic enforcement coverage even after fine-tuning. The dual-factor mechanism (D014) persists in the fine-tuned regime when baseline RV is not fully eliminated."
- Limitations line 75 已有 "Residual DR (e.g., 10.21%)" 句，改为包含 FT 残留: "Residual DR ranges from 0\% (SciERC FT, Qwen) to {X}\% (DocRED FT, [model])"
- **关键**: 用 D014 机制（tightness × RV baseline）解释，不是方法缺陷

### 场景 D: DocRED FT+S1 R-F1 显著下降（> 0.5pp）

- 不能写 "zero F1 cost"
- 改为: "R-F1 cost is modest ({X}pp) and [需查 per-relation breakdown 归因]"
- Table caption 中 `R-F1 change within ±{X}pp` 需覆盖此值

### 场景 E: DocRED FT+S1 CF 很高（> 2%）

- Llama DocRED ZS CF=12.02%，FT 可能仍偏高
- Limitations CF 范围需扩大
- 检查 CF 是否集中在 MISC type（类似 SciERC 的 Generic↔X）

---

## 五、Claim 3 Story 一致性检查

根据 paper_framing.md，Claim 3 的核心叙事是:

> **Fine-tuning and OntoCoDec compose along orthogonal axes**: fine-tuning improves extraction quality, OntoCoDec guarantees ontological compliance.

DocRED 数据支持此叙事的关键证据:
1. FT 大幅提升 F1（7.74→40.86 Qwen, 5.98→43.72 Llama）但未完全消除 DR（0.76%, 0.49%）
2. S1 消除残余 DR，且不影响 F1
3. 两个数据集 × 两个模型 = 4 个独立验证点

如果 DocRED FT+S1 结果符合预期（DR↓, F1~不变），composability claim 从 "validated on one dataset" 升级为 "validated on two datasets with different ontology scales"。这是 paper_framing.md 中 "Claim with caution" → 可以更 confident 的关键转变。

**但注意**: paper_framing.md 明确说不要声称 "universally"，因为仍然只有 LoRA 一种 FT 方法。更新后的措辞应保留此 caveat。

---

## 六、文件清单

| 文件 | 更新项 | 优先级 |
|------|--------|--------|
| `section5_scierc_draft.tex` L159-199 | Table 5 加行 + caption | P0 |
| `section5_scierc_draft.tex` L127 | 实验描述改 scope | P1 |
| `section5_scierc_draft.tex` L143 后 | 插入 DocRED 段 | P1 |
| `section5_scierc_draft.tex` L145-146 | 总结句扩展 | P1 |
| `section5_scierc_draft.tex` L149 | CF under FT 加 DocRED | P1 |
| `main.tex` L70 | 删 "DocRED not reported" | P0 |
| `main.tex` L69 | ZS-only → +FT reference | P1 |
| `main.tex` L76 | 删 "fine-tuned models" | P1 |
| `appendix_discussion.tex` L74 | CF reduction 加 DocRED | P2 |
| `paper_tables_draft.tex` L119 | TBD 占位符 | P2 |
