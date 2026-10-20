# 论文数据一致性审查报告

生成日期: 2026-05-14
审查范围: `paper/{abstract,introduction,method,experiments,conclusion,related_work,appendix}.tex`
数据源: `registry.yaml`（success/DONE 实验）+ `paper_framing.md`

总体结论: **PASS（无 critical 数据错误）**。所有引用数字均可追溯至 registry，且与 `paper_framing.md` 一致。仅发现 2 处 minor 方法学不一致和 1 处需注意的约定（proved-only ISR 而非 mean ISR）——均不影响 paper claim 的正确性。

---

## 1. 数字一致性核对

### 1.1 ISR 崩塌轨迹（abstract / intro / experiments §3.2 / appendix tab:beta01-3seed）

| Step | 论文值 | Registry 来源 | Registry 实际值 | 状态 |
|------|--------|---------------|------------------|------|
| 100  | PR=32%, ISR=0.642 | plan003-eval-exec-only-r5 | prove_rate=0.32, proved_only_isr=0.6423 | ✓ |
| 500  | PR=93%, ISR=0.132 | plan001-exec-only-s42-r2 | eval_prove_rate=0.93, eval_proved_only_isr=0.1324 | ✓ |
| 1000 | PR=96%, ISR=0.003, components=18.55, 94.8% ISR=0 | plan016-extended-1000-s42 | prove_rate=0.96, isr=0.003 (proved_only=0.0028), components=18.55, isr_zero=94.8% | ✓ |

**99.5% degradation** (abstract): (0.642 − 0.003)/0.642 = 99.53% ✓
**−79.4% / −99.6%** (appendix): (0.642 − 0.132)/0.642 = 79.4%; (0.642 − 0.003)/0.642 = 99.5%。Appendix 写 −99.6% 实际是 99.5%，**rounding off by 0.1 pp**（minor，不需修）。

### 1.2 PR 轨迹

论文: 32% → 93% → 96%。Registry: 0.32 → 0.93 → 0.96。 ✓

### 1.3 ISR β=0.1 三 seed (tab:beta01-3seed)

| Seed | 论文 PR | 论文 ISR* | 论文 H7% | 论文 H1% | 论文 Gen% | Registry plan | Registry 实际 | 状态 |
|------|---------|-----------|----------|----------|-----------|---------------|---------------|------|
| s42 | 0.81 | 0.415 | 16.0 | 51.9 | 30.9 | plan002-additive-b01-s42 | PR=0.81, ISR*=0.4154, h7=0.16, h1=0.519, genuine=0.309 | ✓ |
| s43 | 0.61 | 0.830 | 96.7 | 0 | ~3 | plan002-additive-b01-s43 | PR=0.61, ISR*=0.8301, h7=0.967, h1=0 | ✓ |
| s44 | 0.89 | 0.902 | 86.5 | 0 | ~13.5 | plan002-additive-b01-s44 | PR=0.89, mean_isr=0.803 → proved_only=0.803/0.89=0.902, h7=0.865 | ✓ |

3-seed mean: PR=0.77±0.14, ISR*=0.716±0.26。重新计算：
- PR mean=(0.81+0.61+0.89)/3=0.770; std≈0.144 ✓
- ISR mean=(0.415+0.830+0.902)/3=0.716; std≈0.262 ✓

### 1.4 Random β=0.1 三 seed (tab:beta01-3seed)

| Seed | 论文 PR | 论文 ISR* | 论文 H7% | 论文 H1% | 论文 Gen% | Registry plan | Registry 实际 | 状态 |
|------|---------|-----------|----------|----------|-----------|---------------|---------------|------|
| s42 | 0.79 | 0.131 | 0 | 70.9 | 29.1 | plan018-additive-random-b01-s42 | PR=0.79, ISR*=0.1314 | ✓ |
| s43 | 0.88 | 0.058 | 0 | 93.2 | 6.8 | plan018-additive-random-b01-s43-r2 | h1_rate=93.2, genuine_rate=6.8 (PR/ISR 在 framing 中确认) | ✓ |
| s44 | 0.89 | 0.070 | 0 | 79.8 | 20.2 | plan018-additive-random-b01-s44 | PR=0.89, ISR*=0.0695 | ✓ |

3-seed mean: PR=0.85±0.06, ISR*=0.086±0.039。重算：
- PR mean=(0.79+0.88+0.89)/3=0.853; std≈0.055 ✓
- ISR mean=(0.131+0.058+0.070)/3=0.0863; std≈0.039 ✓

### 1.5 SFT Baseline

| 指标 | 论文值 | Registry plan009-sft-baseline-s42-r4 | 状态 |
|------|--------|--------------------------------------|------|
| PR | 14% | 0.14 | ✓ |
| ISR* | 0.571 | 0.571 | ✓ |
| H7 | 0/14 (0%) | h7_count=0 | ✓ |
| H1 | 1/14 (7.1%) | h1_count=1, h1_rate=0.071 | ✓ |
| Genuine | 13/14 (92.9%) | genuine_count=13, genuine_rate=0.929 | ✓ |

### 1.6 Prolog 数字 (tab:prolog-crosslogic / §3.3)

**Exec-only:**
| Seed | 论文 PR | 论文 ISR* | Registry | 状态 |
|------|---------|-----------|----------|------|
| s42 | 0.83 | 0.037 | plan006-prolog-exec-s42: PR=0.83, ISR*=0.037 | ✓ |
| s43 | 0.56 | 0.015 | plan006-prolog-exec-s43-r3: PR=0.56, ISR*=0.015 | ✓ |
| s44 | 0.21 | 0.387 | plan006-prolog-exec-s44: PR=0.21, ISR*=0.3866 | ✓ |

3-seed mean: PR=0.53±0.31, ISR=0.146±0.21
- (0.037+0.015+0.387)/3 = 0.146 ✓
- std≈0.213 ✓

**Exec+ISR (STA reward):**
| Seed | 论文 PR | 论文 ISR* | 论文 H7% | 论文 H1% | Registry | 状态 |
|------|---------|-----------|----------|----------|----------|------|
| s42 | 0.50 | 1.000 | 100 | 0 | plan006-prolog-sta-s42: PR=0.5, ISR*=1, h7=1 | ✓ |
| s43 | 0.38 | 0.185 | 0 (strict; functional 100%) | 97.4 | plan006-prolog-sta-s43: PR=0.38, ISR*=0.1853, h7=0, h1=37/38=97.4% | ✓ |
| s44 | 0.97 | 0.912 | 0 (strict; functional 95/97) | 0 | plan006-prolog-sta-s44: PR=0.97, mean_isr=0.885 → proved_only=0.885/0.97=0.9124 | ✓ |

3-seed mean: PR=0.62±0.31, ISR=0.699±0.45
- (0.5+0.38+0.97)/3=0.617 ✓
- (1.0+0.185+0.912)/3=0.699 ✓

### 1.7 1000-step extended run (§3.2)

论文: ISR=0.003, 94.8% ISR=0, mean components 18.55, H1=100%, Gen=0%。
Registry plan016-extended-1000-s42: isr=0.003, components=18.55, h1_rate=1, genuine_rate=0, n_necessary=0 ratio=94.8%。 ✓

### 1.8 Exec-only 跨 seed (§3.2)

| Seed | 论文 PR | 论文 ISR* | Registry | 状态 |
|------|---------|-----------|----------|------|
| s42 | 0.93, H1=87.1% | — | plan001-exec-only-s42-r2: PR=0.93, h1=0.871 | ✓ |
| s43 | 0.14, ISR=0 | sampling T=0.7 | plan001-exec-only-s43-r4: sampling_PR=0.14, sampling_ISR=0 | ✓ |
| s44 | 0.98, H7=100%, components=2.04 | — | plan001-exec-only-s44: PR=0.98, h7=1, components=2.04 | ✓ |

3-seed PR σ=±47pp: std(0.93, 0.14, 0.98)=0.471 ✓

### 1.9 其他基线 (appendix tab:beta01-3seed)

| 行 | 论文值 | Registry | 状态 |
|----|--------|----------|------|
| Base model (no training) | PR=0.12, ISR=0.064 | sta-phase0-baseline: prove_rate=0.12, mean_isr=0.0641 | ✓ |
| Ground-truth FOL | PR=0.18, ISR=0.559 | sta-gt-isr-baseline: prove_rate=0.18, mean_isr=0.5588 | ✓ |

### 1.10 Random β=0.3 (Goodhart landscape)

论文: PR=48, ISR=0.094, components=9.6。
Registry plan017-additive-random-s42: PR=0.48, ISR*=0.0943, components=9.6。 ✓

### 1.11 ISR β=0.3 (无独立 eval registry 项)

论文: PR=18, ISR*=0.143。
Registry plan002-additive-b03-s42 仅记录训练统计（无 eval_*），但与 framing 一致：framing 给出 mean_isr=0.026，而 0.143 × 0.18 = 0.0257 ≈ 0.026，所以 paper 的 0.143（proved-only）与 framing 的 0.026（mean）数学一致。 ✓

### 1.12 Premise-count-matched (§3.2 / Limitations)

论文: 1.06× (ISR-genuine ISR=0.258 n=11 vs random-genuine ISR=0.243 n=21)。
Framing: ISR s42 genuine n_prem≥3: n=11, mean ISR=0.2578; Random s42 genuine n_prem≥3: n=21, mean ISR=0.2434。Ratio=1.06×。 ✓

### 1.13 Component-count s42

论文: ISR s42 mean=5.58 components, Random s42 mean=8.46 components。
Registry plan002-b01-s42: component_count_mean=5.58。plan018-random-s42: component_count_mean=8.46。 ✓

### 1.14 NLI Limitation (Conclusion / Appendix)

论文: Spearman ρ=−0.049, p=0.187。
Registry plan014-downstream-nli-s42: spearman_rho=-0.049, spearman_p=0.187。 ✓

### 1.15 H7 pooled rate

论文: 64.5% (149/231), Random 0% (0/256)。
- ISR pooled: (13 + 59 + 77)/(81+61+89) = 149/231 = 64.50% ✓
- Random pooled: (0+0+0)/(79+88+89) = 0/256 ✓

---

## 2. 硬约束检查

| 约束 | 状态 | 证据 |
|------|------|------|
| D051: "2.4x" 已作废，不应出现 | ✅ PASS | grep `2\.4(x|×|\\times)` 在 paper/*.tex 0 matches |
| 旧的 "3.2x" 也已移除 | ✅ PASS | grep `3\.2(x|×|\\times)` 0 matches |
| Hacking taxonomy = 7 modes (非 6) | ✅ PASS | abstract/method/conclusion/appendix 均说 "seven" / "7"。`six modes` 0 matches |
| ISR β=0.1 不应标 "no hacking" | ✅ PASS | "near-zero hacking" 仅用于 SFT (92.9% genuine)；ISR β=0.1 在论文中明确标注 H7 主导 |
| s44 Prolog STA: query-as-fact gaming, 0% genuine | ✅ PASS | appendix tab:prolog-crosslogic 标 Gen=0%，footnote $^b$ 解释功能性 H7 (95/97) |
| plan013 vs plan017 不简化为 "additive vs convex" | ✅ PASS | grep 0 matches |
| C006: ISR 双语义区分（exec-only low ISR=冗余编码 vs ISR-reward high ISR=metric gaming） | ✅ PASS | conclusion §"Interpreting ISR" 和 appendix §"What ISR measures" 均明确区分 |

---

## 3. 内部一致性检查

### 3.1 跨章节核心数字一致

- 93% PR + 87% H1: abstract / intro / experiments §3.2 / appendix。一致 ✓
- 64.5% H7 vs 0% random: abstract / intro / experiments §3.2 / appendix。一致 ✓
- 1.06× premise-matched: abstract / intro §1 / experiments §3.2 / appendix。一致 ✓
- 18% vs 48%（β=0.3 ISR vs Random）: abstract / intro / experiments §3.2 / appendix。一致 ✓
- 92.9% genuine SFT: abstract / intro / experiments §3.1 / Table 1 / appendix。一致 ✓
- 3/3 Prolog seeds gaming, 0% genuine: abstract / intro / experiments §3.3 / conclusion / appendix。一致 ✓
- 7 hacking modes: method §2.4 / experiments §3.4 / conclusion / appendix §C。一致 ✓
- 6 reward conditions: method §2.3 / experiments §3 setup / conclusion。一致 ✓ (Exec-only / ISR β=0.1 / ISR β=0.3 / Random β=0.1 / Random β=0.3 / SFT = 6)
- ISR 崩塌 0.642→0.132→0.003: abstract / intro / experiments §3.2 / appendix §F。一致 ✓

### 3.2 交叉引用

所有 `\ref{}` 标签均能在 paper/*.tex 找到对应定义：
- sec:setup, sec:diagnostic, sec:goodhart, sec:crosslogic, sec:taxonomy, sec:taxonomy-method, sec:method, sec:task, sec:sta, sec:rewards, sec:experiments, sec:related-work ✓
- fig:sta-overview, fig:isr-collapse, fig:hacking-composition, fig:prolog-comparison ✓
- tab:goodhart-landscape, tab:hyperparams, tab:hacking-taxonomy-app, tab:fol-detailed / tab:beta01-3seed, tab:prolog-detailed / tab:prolog-crosslogic ✓
- alg:sta ✓
- eq:isr ✓
- app:setup, app:algorithm, app:extended-discussion, app:hacking-modes, app:detailed-results ✓

### 3.3 Minor 内部不一致

#### 3.3.1 H1 mean 算法不一致（simple mean vs pooled）

- **H7 ISR β=0.1 (论文 65%)**: pooled = 149/231 = 64.5% → 论文用 pooled
- **H1 ISR β=0.1 (论文 17%)**: simple mean = (51.9+0+0)/3 = 17.3% vs pooled = 42/231 = 18.2% → 论文用 simple mean

这与 framing 一致（framing 也是混用），但同一行同一指标用两种平均方法略不规范。**Impact: 0.8pp 差异，不影响 claim**。

建议：在 caption 或正文 footnote 中说明 H7/H1 用 simple mean of seeds（而非 pooled）。

#### 3.3.2 Appendix line 414 微小 rounding

> "ISR$^*=0.642$ at 100 steps $\to$ $0.132$ at 500 steps ($-79.4$\%) $\to$ $0.003$ at 1000 steps ($-99.6$\% from step 100)."

(0.642−0.003)/0.642 = 0.9953 = **99.5%**，paper 写 99.6%。Abstract 写 99.5%（正确）。

**建议**：把 appendix 改为 99.5%，与 abstract 对齐。

#### 3.3.3 Appendix tab:beta01-3seed exec-only s44 ISR* = 0.582

Registry 值 0.5816 — 四舍五入应为 0.582 ✓。但 framing 文本写 0.57（粗略），paper 用更精确的 0.582。无问题。

#### 3.3.4 Proved-only vs mean ISR 表达约定

Paper 全文使用 ISR* = proved-only。Registry 中部分 metrics 仅存 mean_isr（all samples，含 unproved=0）。当看到 paper 给的 0.902 (ISR s44) vs registry 0.803 (mean_isr) 时，需理解：proved_only = mean_isr / PR (∵ unproved=0)。

- ISR β=0.1 s44: 0.803/0.89 = 0.902 ✓
- Prolog STA s44: 0.885/0.97 = 0.912 ✓
- ISR β=0.3 s42: 0.0257/0.18 = 0.143 ✓ (framing 写 0.026 = mean, paper 写 0.143 = proved-only)
- Random β=0.3 s42: 0.0453/0.48 = 0.0944 ✓

约定一致，无错误。但**建议在 §3.1 Setup 中明确 footnote**：「除非另有说明，所有 ISR 报告均为 proved-only ISR* ≡ mean of ISR over proved samples」。Setup 已在第 13 行说明「we report ... proved-only ISR (ISR*, over proved samples only)」，已 OK。

---

## 4. 总结与建议修改

### 4.1 总体评价

**论文数据层面 PASS**。所有定量 claim 均可追溯至 registry，跨章节一致，硬约束全部遵守。

### 4.2 建议修改（均为 minor）

1. **Appendix line 414**: `−99.6%` → `−99.5%` 以与 abstract 99.5% 对齐。
2. **Table 1 caption 或 §3.2 footnote**: 添加一句说明 3-seed mean H7/H1 是 simple mean across seeds（非 pooled），以避免审稿人质疑 H7=65% 与 H1=17% 计算口径差异。
3. **可选**: appendix line 388 Prolog STA s44 后 footnote $^b$ 提到「strict classifier reports Genuine=100%」，但表中已经写 Gen=0%（覆盖），建议在表内 Gen 列标注 `0$^b$` 或类似显眼标记，避免读者误读 ground-truth 标签。当前 footnote 在右下角，可能被忽略。

### 4.3 无 critical 错误

- 没有引用作废的 2.4× 优势
- 没有混淆 binary _fast_fn 训练 ISR 与 full STA eval ISR
- 没有把 s44 Prolog STA 误标为 genuine
- 7-mode taxonomy 全文一致
- C001 数据约束（train_500_seed42.jsonl）在 setup 和 appendix 均明确

报告结束。
