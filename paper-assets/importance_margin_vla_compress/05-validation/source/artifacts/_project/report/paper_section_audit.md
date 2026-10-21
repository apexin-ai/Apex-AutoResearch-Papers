# Paper Section Audit — CoRL 2026 Submission

**Audit date**: 2026-05-27  
**Deadline**: ~5h remaining  
**Paper location**: `docs/paper/` (main.tex + section files)  
**Main structure**: Abstract → Introduction → Related Work → Method → Experiments → Discussion → Conclusion → Appendix

---

## Section Status Summary

| Section | 文件 | 状态 | 具体问题 | 优先级 |
|---------|------|------|----------|--------|
| Abstract | `abstract.tex` | **定稿** | "five VLA architectures" vs Method "six" — 需统一 | P2 |
| Introduction | `introduction.tex` | **定稿** | 与 paper_framing 2-axis framework 对齐，claims 一致 | — |
| Related Work | `related_work.tex` | **定稿** | 完整，覆盖 6 篇 concurrent work | — |
| Method | `method.tex` | **定稿** | 6 模型 Table 1 完整，CV 公式、VTR 描述清晰 | — |
| Experiments | `experiments.tex` | **待数据/待修改** | 3 个关键问题，见下 | **P0/P1** |
| Discussion | `analysis.tex` | **定稿** | OpenVLA sweep 分析完整，limitations 在位 | — |
| Conclusion | `conclusion.tex` | **定稿** | 5 claims 总结，AI disclosure 已加 | — |
| Appendix | `appendix.tex` | **基本定稿** | ~820 行，SmolVLA baseline 不一致需修 | P1 |
| References | `references.bib` | **存在** | 未做编译验证 | P3 |
| Figures | `figures/paper/` | **完整** | 19 个 PDF 全在位，所有 \includegraphics 有对应文件 | — |

---

## Critical Issues (P0)

### 1. π0.5 Goal/Long 数据污染 (D248)

cqa1 上的 π0.5 实验使用宽松 success 条件 (`done|reward>0.5`)，导致 SR 可能虚高。

**受影响的 Table 2 单元格**:
| Suite | 受影响列 | 当前值 | 可信度 |
|-------|----------|--------|--------|
| Goal | baseline | 96.4% | **不可信** — 可能虚高 |
| Goal | k=0.95 (89.4/84.0) | 全部 | **不可信** |
| Goal | k=0.9 (90.6/62.2) | 全部 | **不可信** |
| Goal | k=0.7 (71.2/78.2) | 全部 | **不可信** |
| Goal | k=0.5 (59.2/73.6) | 全部 | **不可信** |
| Long | k=0.7 (63.2/64.6) | 全部 | **不可信** (k≤0.85) |
| Long | k=0.5 (50.2/50.2) | 全部 | **不可信** (k≤0.85) |
| Long | baseline (91.6%) | — | **待确认** — 来源需查 |
| Long | k=0.95 (86.8/61.2) | — | **可信** (k≥0.9) |
| Long | k=0.9 (81.0/31.8) | — | **可信** (k≥0.9) |

**受影响的论文 claims**:
- Abstract: "task complexity amplifies connector-dependent patterns, with multi-step tasks magnifying entangling-connector losses by up to 20×" — 20× 来自 X-VLA（不受影响），但 π0.5 Goal/Long 数据支撑同一论点
- Sec 5.5 (Experiments): importance margin gradient "Object +93pp > Goal +35.2pp > Long +28.6pp" — Goal 和 Long 的 margin 值依赖污染数据
- Sec 5.7 (cliff highlight): π0.5 Long k=0.85 random=49.4% 对比 — k=0.85 处于 k≤0.85 污染区间
- Discussion: OpenVLA 的 task complexity 分析不受影响（独立数据源）

**Strict 重跑进度**: k=0.95/0.9/0.85 Attn Long 正在进行中。

**建议处理方案**:
- **方案 A (保守)**: 从 Table 2 移除所有不可信 π0.5 Goal 数据，标注 "—"，仅保留 Object/Spatial/Long k≥0.9。Task complexity 论点仅用 X-VLA 数据（不受污染）
- **方案 B (折中)**: 保留数据但加脚注 "π0.5 Goal and Long (k≤0.85) results use a lenient success criterion; strict re-evaluation in progress. X-VLA cross-suite patterns (unaffected) provide independent support for the task complexity claim."
- **方案 C**: 如果 strict 重跑在截止前完成，替换数据

### 2. Table 2 数据缺口 ("--" 单元格)

共 19+ 个 "--" 单元格：

| 模型 | 缺失 | 影响 |
|------|------|------|
| X-VLA Spatial | k=0.7 L2 | 文中未引用 |
| X-VLA Long | k=0.7 L2/R | 文中未引用 |
| OpenVLA Object | k=0.95 R, k=0.7 L2/R | k=0.95 R 缺失稍影响叙事 |
| OpenVLA Goal | k=0.95, k=0.7, k=0.5 全缺 | 仅有 k=0.9 三方法对比 |
| OpenVLA Spatial | k=0.95, k=0.7, k=0.5 全缺 | 仅有 k=0.9 三方法对比 |
| OpenVLA Long | k=0.95, k=0.7, k=0.5 全缺 | 仅有 k=0.9 三方法对比 |

**评估**: 论文叙事主要围绕 k=0.9 和 k=0.5 展开。OpenVLA 的 k=0.9 三方法对比数据完整（含 attention†），支撑 scoring crossover 论点。X-VLA 的 attention 对比在 k=0.5 完整（Table 8）。**缺口不阻塞核心 claims，但 Table 2 视觉上稀疏。**

**建议**: 接受现状，或将 OpenVLA 改为仅展示 k=0.9 和 k=0.5 两列（去掉 k=0.95/k=0.7 空列）。

---

## High Priority Issues (P1)

### 3. SmolVLA 跨 suite baselines 不一致

| Suite | Table 2 (main) | VTR cross-suite table (App) | paper_framing |
|-------|----------------|---------------------------|---------------|
| Object | 59.2% (official) | 44.8% (LoRA) | 59.2% official |
| Spatial | 44.6% | 51.8% | 43.8% or 44.6% |
| Goal | 60.8% | 63.0% | 60.8% |

- Table 2 用 official checkpoint baseline；VTR appendix 用 LoRA checkpoint baseline
- Spatial 有三个不同值 (43.8% / 44.6% / 51.8%)
- 论文 appendix 文本已做 caveat 处理，但数字混乱容易让 reviewer 质疑

**建议**: 在 VTR cross-suite table (Tab 10) 加脚注明确说明 "baselines from LoRA-trained checkpoint (batch size 4); main table baselines from official checkpoint"。统一 Spatial 基线值。

### 4. "Five" vs "Six" architectures 不一致

- Abstract line 4: "five VLA architectures (450M--7B parameters)"
- Method Sec 3.1 line 7: "six VLA architectures spanning three vision connector families"
- Table 1 列出 6 行（含 OFT）

**建议**: 统一为 "six VLA architectures" 或在 abstract 说 "five VLA architectures (with a sixth offline variant)"。最简单是改 abstract 为 "six"。

### 5. X-VLA baseline 小幅偏差

| Suite | Table 2 | paper_framing |
|-------|---------|---------------|
| Spatial | 93.0% | 91.6% |
| Goal | 98.4% | 98.0% |

可能来自不同 eval seed 或不同 checkpoint。Table 2 是论文定稿数据，paper_framing 是早期记录。**如果 Table 2 数据可信，以 Table 2 为准。** 但需确认 93.0% 和 98.4% 来源无误。

---

## Medium Priority Issues (P2)

### 6. discussion.tex 是空 stub

文件内容仅为注释："Discussion section moved to Appendix"。实际 Discussion 内容在 `analysis.tex`（标题为 `\section{Discussion}`，label 为 `sec:analysis`）。main.tex include 的是 `\input{analysis}`。功能正常但维护混乱。

### 7. sections/ 目录残留旧稿

`docs/paper/sections/` 下有 `results_draft.tex`, `analysis_draft.tex`, `related_work_draft.tex` 等旧版文件，不被 main.tex include。不影响编译但增加困惑。

### 8. Constraint C001 合规性

C001 要求 "Spatial suite 对比禁止用 LoRA baseline (6.2%)"。检查结果：
- VTR cross-suite table 中 Spatial baseline=51.8%，VTR=53.2%（差值仅 1.4pp）
- 文本明确说 "we therefore do not treat the Spatial comparison as evidence that re-encoding improves over the uncompressed official baseline"
- **合规** — 未使用 LoRA 6.2% baseline 做对比

---

## Low Priority Issues (P3)

### 9. LaTeX 编译未验证

references.bib 存在（23KB），所有 figure PDF 在位。未实际运行 `pdflatex` 验证编译。建议在提交前做一次完整编译。

### 10. Appendix 长度

Appendix 约 820 行 LaTeX，包含 18 个 tables/figures。CoRL 通常不限 appendix 页数，但过长可能影响 reviewer 体验。当前内容信息密度高，无明显冗余。

---

## Claim-Framing 一致性检查

| Core Claim (paper_framing) | 论文中对应 | 一致性 |
|---------------------------|-----------|--------|
| Claim 1: 2-Axis Framework | Sec 4.2 + Fig 1 teaser | **一致** — connector × task complexity |
| Claim 2: Pixel-shuffle entanglement | Sec 4.3 + Fig 5 | **一致** — 0% at k=0.95, official+LoRA 双 checkpoint |
| Claim 3: Connector determines tolerance | Sec 3.1 Table 1 + Sec 4.2-4.5 | **一致** — CV spectrum 0.038→0.314 |
| Claim 4: VTR recovery | Sec 4.6 + Table 4 | **一致** — 60.1±1.3% at M=32, MLP adapter control |
| Claim 5: CV predicts optimal strategy | Sec 4.5 + Table 6 (appendix) | **一致** — monotonic Δ(R-L2) trend |

**额外 claims 在论文但不在 framing**:
- Zero-mask ablation (Sec 4.4): 89pp gap，position disruption — 论文中新增的重要发现
- Per-task reversal within L2-dominant regimes (Sec 4.5 末段): Task 6 reversal — 细粒度分析

---

## 优先行动建议 (按时间紧迫度)

1. **[P0, 30min]** 决定 π0.5 Goal/Long 污染数据处理方案 (A/B/C)，如选 B 则写脚注
2. **[P1, 10min]** 统一 abstract "five"→"six" architectures
3. **[P1, 15min]** 确认 X-VLA Spatial=93.0% 和 Goal=98.4% 数据来源
4. **[P1, 15min]** 统一 SmolVLA Spatial baseline (44.6% vs 51.8% vs 43.8%)，加 VTR table 脚注
5. **[P2, 5min]** 确认 Table 2 "--" 缺口可接受
6. **[P3, 10min]** 运行一次完整 LaTeX 编译
