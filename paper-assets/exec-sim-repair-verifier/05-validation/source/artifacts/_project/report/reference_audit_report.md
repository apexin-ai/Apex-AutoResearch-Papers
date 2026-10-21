# 论文引用审计 & LaTeX 编译检查报告

**审计日期**: 2026-05-15  
**Bib 文件**: `docs/paper/references.bib` (26 条目)  
**Tex 文件**: `docs/paper/` (main + 6 section files)

---

## 一、问题列表（按严重性排序）

### CRITICAL

#### C1. 未引用的浮动图表（fig:scaling_gap, fig:oracle_stratified）
- `\label{fig:scaling_gap}` 和 `\label{fig:oracle_stratified}` 在 main.tex 中定义，但正文中没有任何 `\ref{fig:scaling_gap}` 或 `\ref{fig:oracle_stratified}`
- §4.2 Scaling Behavior 和 §4.4 Oracle 部分描述了这两张图的数据，但没有用 `\ref` 指向它们
- **修复**: 在 experiments.tex 相应段落添加 `(Figure~\ref{fig:scaling_gap})` 和 `(Figure~\ref{fig:oracle_stratified})`

#### C2. 表格数据不完整（tab:repo_level CWM 8B 行）
- experiments.tex 中 `tab:repo_level` 的 CWM 8B 行全部为 `---`，caption 注释 "cwm 8B in progress"
- 正文 line 144: "CWM 8B training is in progress"
- **修复**: 提交前必须补充数据或删除该行

### WARNING

#### W1. Bib key 与 year 不匹配：`dettmers2024qlora`
- Key 暗示 2024，实际 `year={2023}`（QLoRA 发表于 NeurIPS 2023）
- **修复**: 重命名为 `dettmers2023qlora`，更新 experiments.tex 中的 `\cite`

#### W2. Bib key 与 year 不匹配：`snell2024scaling`
- Key 暗示 2024，实际 `year={2025}`（ICLR 2025）
- arXiv 预印本 2024 年发布，正式发表 2025 年
- **修复**: 可重命名为 `snell2025scaling`，更新 introduction.tex、experiments.tex、related_work.tex

#### W3. Bib key 与 year 不匹配：`xia2024agentless`
- Key 暗示 2024，实际 `year={2025}`（FSE 2025）
- **修复**: 可重命名为 `xia2025agentless`，更新 introduction.tex、related_work.tex

#### W4. 会议接收状态待确认
- `chen2025vgsearch`：标注 `booktitle={NeurIPS}`, `year={2025}`——需确认已被 NeurIPS 2025 接收
- `li2025sstar`：标注 `booktitle={Findings of EMNLP}`, `year={2025}`——需确认已被 EMNLP 2025 Findings 接收
- 若仍为预印本，应改为 `@article` 并添加 arXiv journal 字段

### INFO

#### I1. 未使用的 LaTeX 包
- main.tex 加载了 `tabularx`，但未在任何文件中使用 `tabularx` 环境

#### I2. 残留图片文件
- `artifacts/figures/paper/` 中存在 `fig2_gap_amplification.pdf`（旧版 Figure 2），当前使用的是 `fig2_scaling_gap.pdf`

---

## 二、引用完整性检查

| 检查项 | 结果 |
|--------|------|
| 孤立 bib 条目（有定义无引用） | **0** — 全部 26 条被引用 |
| 缺失引用（有引用无定义） | **0** — 全部 cite key 有对应 bib 条目 |
| 重复条目（同一论文多个 key） | **0** — 无真重复 |
| 必填字段（author/title/year） | **PASS** — 全部条目完整 |
| 会议名称一致性 | **PASS** — 均使用缩写，无冲突 |
| arXiv 预印本条目类型 | **PASS** — 均使用 @article 或 @misc |

---

## 三、引用真实性抽查（5 篇）

| 引用 | Key | 状态 | 备注 |
|------|-----|------|------|
| CWM | `meta2025cwm` | ✅ VERIFIED | arXiv:2510.02387，title/year 正确；author 字段为 `{Meta AI}`（原文列 50+ 作者，可接受） |
| SWE-bench | `jimenez2024swebench` | ✅ VERIFIED | ICLR 2024 Oral，全部信息正确 |
| SWE-RM | `shum2025swerm` | ✅ VERIFIED | arXiv:2512.21919，title "Execution-free Feedback For Software Engineering Agents" 正确 |
| LoRA | `hu2022lora` | ✅ VERIFIED | ICLR 2022，全部信息正确 |
| TOST | `schuirmann1987tost` | ✅ VERIFIED | 1987 年统计学论文（Two One-Sided Tests），用于等价性检验，引用正确 |

---

## 四、LaTeX 结构检查

| 检查项 | 结果 |
|--------|------|
| main.tex 正确 \input 所有 section 文件 | **PASS** (abstract, introduction, method, experiments, related_work, conclusion) |
| 自定义命令定义 (\cls, \cwm, \traj, \pp, \fone) | **PASS** (main.tex lines 23–27) |
| 环境闭合（\begin/\end 配对） | **PASS** — 全部 7 个文件平衡 |
| 括号匹配 | **PASS** |
| 图表引用 (\ref → \label) | **WARNING** — fig:scaling_gap, fig:oracle_stratified 有 label 无 ref (见 C1) |
| 表格引用 | **PASS** — main_results, scaling, oracle, repo_level 全部有对应 label |
| 章节引用 | **PASS** |
| TODO/FIXME/placeholder 标记 | **PASS** — 未发现 |
| 图片文件存在性 | **PASS** — fig1, fig2, fig3 PDF 均存在 |
| graphicspath 解析 | **PASS** |

---

## 五、总体评估

**当前状态：接近可提交，但有 2 个必须修复的问题。**

### 提交前必须修复
1. **C1** — experiments.tex 中为 fig:scaling_gap 和 fig:oracle_stratified 添加 `\ref` 引用
2. **C2** — 补充 CWM 8B 实验数据或从表格中移除该行

### 建议修复（非阻塞）
3. **W1** — 修正 `dettmers2024qlora` key 为 `dettmers2023qlora`
4. **W2-W3** — 可选修正 `snell2024scaling`、`xia2024agentless` 的 key
5. **W4** — 确认 `chen2025vgsearch` 和 `li2025sstar` 的会议接收状态
6. **I1** — 移除未使用的 `tabularx` 包
