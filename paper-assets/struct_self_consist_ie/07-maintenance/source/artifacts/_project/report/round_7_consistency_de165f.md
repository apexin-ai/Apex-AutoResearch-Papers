# Round 7 一致性审计报告

**审计日期**: 2026-05-15
**审计范围**: 论文全文 (main.tex + 8 section files) vs registry 实验数据
**论文标题**: Strong Predictors, Weak Selectors: Why Confidence Signals Do Not Scale Structured Information Extraction

## 总体评判: WARNING

1 CRITICAL (OOD 表 in-domain 引用错误), 3 WARNING (WNUT N 值矛盾、appendix 内部数值不一致、若干微小 rounding 偏差)。核心 Table 1 和 Table 2 的关键数据与 registry 一致，硬约束全部通过。

---

## CRITICAL 发现

### [C-1] OOD 表 (Table 9, Appendix F) in-domain 列引用错误

**问题**: 表格 caption 声称 "In-domain ρ from Table 1 (tab:quality_estimation)"，但实际使用的是 Table 5 (tab:multiseed) 的 3-seed 均值。

**证据**:

| Signal | OOD Table In-dom. | Table 1 (seed=42) | Table 5 (3-seed mean) |
|--------|------------------|--------------------|-----------------------|
| VC     | .386             | .379               | .386 ✓                |
| SJ     | .364             | .360               | .364 ✓                |
| EM     | .307             | .295               | .307 ✓                |
| FK     | .254             | .267               | .254 ✓                |
| LP     | .217             | .205               | .217 ✓                |

**影响**: 
- 所有 Δ 值被系统性偏移
- EM 的 Δ 从 +.005（正确，用 Table 1）变成 -.007（报告值），**符号翻转**
- FK 的 Δ 从 +.018 变成 +.031（幅度膨胀 72%）
- OOD 实际值来自单次运行 (exp_011_ood_scierc_to_conll, seed=42)，与 3-seed mean 对比在方法论上不一致

**涉及位置**:
- appendix.tex L643: 表格 caption
- appendix.tex L661: 正文 "in-domain ρ from Table~\ref{tab:quality_estimation}"
- discussion.tex L46: "VC ρ=0.469 OOD vs. 0.386 in-domain" (传播了相同错误)

**修复**: 将 OOD 表 in-domain 列改为 Table 1 单 seed 值 (.379/.360/.295/.267/.205)，重算所有 Δ，或将 caption 引用改为 Table 5 并注明方法论差异。

---

## WARNING 发现

### [W-1] WNUT-17 表格 N=8 vs registry N=16 矛盾

**问题**: WNUT 表 (tab:wnut, appendix.tex L152) caption 声称 "N=8, T=1.0"，但 registry 中仅有的两个 WNUT 实验 (exp_003_ner_wnut17, exp_003_wnut17_eval) 均为 N=16。

**证据**:
- Registry exp_003_wnut17_eval: N=16, T=1, seed=42
- Registry exp_003_ner_wnut17: N=16, T=1, seed=42
- 论文 WNUT 表 SJ ρ=.089 与 exp_003_wnut17_eval 的 rho_sj=0.089 精确匹配（N=16 数据）
- 论文 WNUT 表 FK ρ=.125 与 exp_003_wnut17_eval 的 rho_fk=0.125 精确匹配

**影响**: 如果数据确实来自 N=16 但 caption 标注 N=8，则与正文 "primary N=8" 声称不一致。精确匹配 N=16 registry 值增强了 caption 标注错误的可能性。

**修复**: 核实数据实际 N 值。如果是 N=16 数据，改 caption 为 N=16 并在正文中说明；如果有独立的 N=8 分析（未注册），应补充 registry。

### [W-2] Appendix logprob_ties 表与正文自相矛盾 (59.7% vs 60.3%)

**问题**: 同一 appendix 节内，正文说 "59.7% of instances" 但紧接着的表格说 "60.3%"。

**证据**:
- appendix.tex L387: "At ε=0.05, 59.7% of instances have a within-sample range below the threshold"
- appendix.tex L408: Table 行 "0.05 & 60.3%"
- Registry exp_freeform_ablation: tied_fraction_constrained = 0.597 = 59.7%
- Freeform ablation Panel A (appendix.tex L464): "59.7%" — 与正文一致

论文其他位置:
- Introduction L25: "60%" (rounded, 兼容两者)
- Discussion L13: "60%" (rounded)

**影响**: 59.7% (来自 registry/freeform ablation) 和 60.3% (仅出现在 logprob_ties 表) 可能来自不同分析脚本，差 ~3 instances (n=529)。读者可能注意到不一致。

**修复**: 统一为 59.7%（与 registry 和 freeform ablation Panel A 一致），或核实 logprob_ties 表的计算来源。

### [W-3] 若干微小 rounding 偏差

以下值在 registry 和论文之间存在末位 rounding 差异（均 ≤0.001）:

| 位置 | 论文值 | Registry 精确值 | 偏差 |
|------|--------|----------------|------|
| Table 1 RE VC AUROC | .693 | 0.6935 → .694 | -0.001 |
| Table 1 RE LP AUROC | .600 | 0.6005 → .601 | -0.001 |
| WNUT LP ρ (full) | -.410 | -0.409 (eval) / -0.414 (ner) | ±0.001-0.004 |
| OOD CoNLL→SciERC FK ρ | -.070 | -0.069 | -0.001 |

**影响**: 极微小，不影响结论。但如果审稿人精确核对可能引发质疑。

**修复**: 对 Table 1 RE VC AUROC (.693→.694) 和 RE LP AUROC (.600→.601) 做标准四舍五入修正。

---

## INFO

### 硬约束检查结果（全部通过）

| # | 约束 | 结果 | 验证详情 |
|---|------|------|---------|
| B1 | exp_012 (max_tokens=512) 数据不得引用 | **PASS** | Table 1 所有值匹配 exp_012_rerun_1024，不匹配旧 exp_012_logprob_baseline (e.g., LP NER ρ=.205 vs old .140) |
| B2 | LLaMA 数据来源正确 | **PASS** | CoNLL LLaMA 匹配 exp_017_llama_conll_infer; SciERC LLaMA 匹配 exp_018_llama_scierc_seed42_r1024 |
| B3 | Selection 是 null result | **PASS** | p=0.39, Cohen's d=0.038; 论文无 "significantly outperforms" 描述 selection |
| B4 | 无来源不明的 "0.335" | **PASS** | 全文 grep 无匹配 |
| B5 | exp_011_ood_conll_to_scierc 描述为 catastrophic model failure | **PASS** | "catastrophic model failure, not signal failure"; greedy NER F1=0.009 匹配 registry |

### 叙事一致性检查（全部通过）

| # | 检查项 | 结果 |
|---|--------|------|
| C1 | Title 使用 "Do Not"（非 "Cannot"） | **PASS** |
| C2 | 核心叙事：universal correlation-selection gap | **PASS** |
| C3 | Free-form ablation 定位为 universality 证据 | **PASS** — "intrinsic to the model and task, not an artifact of constrained decoding" |
| C4 | exp_019 supervised verifier 不出现 | **PASS** — 仅引用文献中的 trained verifiers 作为 future work |
| C5 | Claims 强度匹配 evidence | **PASS** — RE 标注 "preliminary, single benchmark" (≥7 处); WNUT 标注 capability boundary; 跨模型结论限定 "8B scale" |

### Table 1 (Quality Estimation) 数据验证

**SciERC (Qwen, exp_012_rerun_1024)**:

| Signal | Paper ρ | Registry ρ | Paper AUC | Registry AUC |
|--------|---------|------------|-----------|--------------|
| VC | .379 | 0.3792 ✓ | .684 | 0.6841 ✓ |
| SJ | .360 | 0.3599 ✓ | .692 | 0.6917 ✓ |
| FK | .267 | 0.2665 ✓ | .629 | 0.6290 ✓ |
| EM | .295 | 0.2945 ✓ | .749 | 0.7493 ✓ |
| LP | .205 | 0.2052 ✓ | .578 | 0.5783 ✓ |

**CoNLL Qwen (exp_002)**:

| Signal | Paper ρ | Registry ρ | Paper AUC | Registry AUC |
|--------|---------|------------|-----------|--------------|
| VC | .424 | 0.4237 ✓ | .789 | 0.7889 ✓ |
| SJ | .436 | 0.4357 ✓ | .801 | 0.8008 ✓ |
| FK | .400 | 0.3998 ✓ | .774 | 0.7741 ✓ |
| EM | .451 | 0.4507 ✓ | .816 | 0.8156 ✓ |
| LP | .316 | 0.3157 ✓ | .753 | 0.7532 ✓ |

**CoNLL LLaMA (exp_017_llama_conll_infer)**:

| Signal | Paper ρ | Registry ρ | Paper AUC | Registry AUC |
|--------|---------|------------|-----------|--------------|
| VC | .426 | 0.4256 ✓ | .709 | 0.7088 ✓ |
| SJ | .431 | 0.4314 ✓ | .704 | 0.7039 ✓ |
| FK | .428 | 0.4277 ✓ | .703 | 0.7026 ✓ |
| EM | .431 | 0.4306 ✓ | .705 | 0.7046 ✓ |
| LP | .307 | 0.3072 ✓ | .761 | 0.7610 ✓ |

### Table 2 (Selection) Bootstrap 统计验证

| Statistic | Paper | Registry (exp_016_rerun_1024_bootstrap) |
|-----------|-------|-----------------------------------------|
| LP-greedy Δ | +0.6 pp | 0.006 ✓ |
| p-value | 0.39 | 0.39 ✓ |
| 95% CI | [-3.0, +4.2] pp | [-0.03, 0.042] ✓ |
| Cohen's d | 0.038 | 0.038 ✓ |

### Freeform Ablation 验证

| Metric | Paper | Registry (exp_freeform_ablation) |
|--------|-------|----------------------------------|
| LP std ratio | 0.97× | 0.97 ✓ |
| Tied constrained | 59.7% | 0.597 ✓ |
| Tied freeform | 57.7% | 0.577 ✓ |
| NER gap constrained | +0.59 pp | 0.0059 ✓ |
| NER gap freeform | +0.18 pp | 0.0018 ✓ |
| RE gap constrained | -0.68 pp | -0.0068 ✓ |
| RE gap freeform | +1.69 pp | 0.0169 ✓ |

### OOD 实际值验证

| Signal | Paper (SciERC→CoNLL) | Registry (exp_011_ood_scierc_to_conll) |
|--------|---------------------|----------------------------------------|
| VC | .469 | 0.469 ✓ |
| SJ | .378 | 0.378 ✓ |
| EM | .300 | 0.300 ✓ |
| FK | .285 | 0.285 ✓ |
| LP | .246 | 0.246 ✓ |

### 格式检查

| # | 检查项 | 结果 |
|---|--------|------|
| D1 | RE 标注 "preliminary, single benchmark" | **PASS** — Table 1 caption, Table 2 caption, Conclusion, Limitations 均有标注 |
| D2 | p 值和 CI 格式一致 | **PASS** — 统一使用 p=X.XX 或 p<1e-X 格式 |
| D3 | 图表引用完整 | **PASS** — 所有 \ref 均有对应 \label; 全部 7 个 figure PDF 存在于 figures/ |
| D4 | Appendix 表格编号 | **PASS** (LaTeX auto-numbering) |

### 其他观察

- [I-1] `docs/paper/` 根目录有 `discussion.tex` 和 `conclusion.tex` 的副本文件，main.tex 仅 include `sections/` 下的版本。建议删除根目录副本避免编辑混淆。
- [I-2] Table 2 caption 存在两种版本（"EM selects the plurality output" vs "Instance-level signals select the sample closest to consensus"）——可能是编辑过程中的中间状态，确认最终版本。

---

## 建议修改清单（按优先级）

1. **[CRITICAL] 修复 OOD 表 in-domain 列** — 将 in-domain 值改为 Table 1 的单 seed 值 (.379/.360/.295/.267/.205)，重算 Δ 列，更新 appendix 正文中的 Δ 值。或改 caption 引用为 Table 5 并说明是 3-seed mean。同步修正 discussion.tex L46 的 "0.386"。

2. **[WARNING] 核实 WNUT N 值** — 确认 WNUT 表数据来源是 N=8 还是 N=16。如果是 N=16，改 caption；如果有独立 N=8 分析，补注册。

3. **[WARNING] 统一 tied fraction** — 将 logprob_ties 表中 ε=0.05 行的 "60.3%" 改为 "59.7%"（与 registry、freeform ablation Panel A、appendix 正文一致）。

4. **[WARNING] 修正 rounding** — Table 1 RE VC AUROC .693→.694, RE LP AUROC .600→.601。

5. **[INFO] 清理根目录副本** — 删除 `docs/paper/discussion.tex` 和 `docs/paper/conclusion.tex`（非 sections/ 下的版本）。
