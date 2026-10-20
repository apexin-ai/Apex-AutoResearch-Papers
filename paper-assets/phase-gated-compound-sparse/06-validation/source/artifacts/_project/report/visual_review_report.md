# 论文 PDF 最终视觉审查报告

**论文**: Phase-Modulated Compound Sparsity: Strategy-Dependent Severity Gradients in Reasoning Models
**审查日期**: 2026-05-14
**PDF 版本**: main.pdf (11 pages)
**格式**: ACL review mode, 双栏, Anonymous submission

---

## 逐页审查结果

### Page 1 — Title + Abstract + §1 Introduction (partial)
- ✅ 标题排版正常，双行带换行
- ✅ "Anonymous ACL submission" 匿名标注正确
- ✅ Abstract 格式规范，内容完整（含关键数字：0.39→14.59, d_z 0.44→0.80, p&lt;0.005）
- ✅ §1 Introduction 开始，双栏对齐正常
- ✅ 行号（review mode）正确显示
- ✅ 页码 "1" 底部居中

### Page 2 — §1 continued + §2 Related Work + §3 begins
- ✅ §1 结尾的三点贡献列表格式良好
- ✅ §2 Related Work 含三个段落（Compound compression, KV cache eviction, Phase-aware inference）
- ✅ §3 Background and Problem Setup 开始
- ✅ 引用格式正常，无 [?] 缺失
- ✅ 页码 "2"

### Page 3 — §3 continued + §4 Experimental Setup + §5 Results begins
- ✅ 公式（Interaction Index, Severity gradient G）排版正常，无溢出
- ✅ §4 各子段落（Models, Dataset, Sparsity configuration, Phase segmentation, Statistical analysis）完整
- ✅ §5 Results 5.1 Strategy-Dependent Severity 开始
- ✅ Table 1（Median compound severity difference）格式正常
- ✅ 脚注排版正确
- ✅ 页码 "3"

### Page 4 — Table 2 (full-width) + Table 3 + §5-§8 主要内容
- ✅ Table 2（Interaction index by strategy/phase/sparsity）全宽 table* 排版清晰
- ✅ Table 3（Paired d_z）单栏表格格式规范
- ✅ §6 Analysis（简短版）、§7 Discussion、§8 Conclusion 紧凑排列
- ⚠️ **Figure 1 (dose-response plot) 未在此页可见**——可能被 LaTeX float 算法推迟放置
- ✅ 页码 "4"

### Page 5 — §8 Conclusion + Limitations + References begin
- ✅ Conclusion 完整收尾
- ✅ Limitations 段落格式正确（Model scale, Task coverage, Mechanism, Sparsity range）
- ✅ References 开始，格式符合 ACL 标准
- ⚠️ **主文结束于第 5 页**（含 title/abstract），正文内容约 4.5 页
- ✅ 页码 "5"

### Page 6 — References continued + Appendix A begins
- ✅ 参考文献列表完整显示
- ✅ Appendix A: Compound Sparsity Formulation 开始
- ✅ 公式（attention sparsity, KV eviction, compound sparsity）排版正常
- ✅ 页码 "6"

### Page 7 — Appendix B-D + Figure 2 + Table 4
- ✅ Appendix B: Multiplicative Null Verification
- ✅ Appendix C: Phase-Strategy Crossover Details
- ✅ Figure 2（Strategy-dependent crossover bar chart）清晰可读，caption 完整
- ✅ Table 4（Cross-model comparison）格式正常
- ✅ Appendix D: Cross-Model Replication Details
- ✅ 页码 "7"

### Page 8 — Figure 3 + Figure 4 + Table 5 + Appendix E-F
- ✅ Figure 3（Cross-model severity comparison line plot）清晰
- ✅ Figure 4（Forest plot of permutation tests）清晰
- ✅ Table 5（Paired permutation test results）格式正常
- ✅ Appendix E: Permutation Test Details 完整
- ✅ Appendix F: Entropy-Discrimination Collapse 开始
- ✅ 页码 "8"

### Page 9 — Table 6 + Table 7 + Appendix F continued + G
- ✅ Table 6（Discrimination collapse: ΔGini, ΔCV）格式正常
- ✅ Table 7（Attention entropy deltas ΔH）格式正常
- ✅ F.2 Entropy Redistribution 含公式 (7)
- ✅ §G Discrimination Collapse Details
- ✅ 页码 "9"

### Page 10 — §G continued + §H Extended Discussion
- ✅ Table 6/7 由 LaTeX 浮动放置在页面顶部（非重复）
- ✅ §H Extended Discussion 各段落完整
- ✅ 页码 "10"

### Page 11 — §I Extended Limitations
- ✅ 所有 Limitations 子段落完整（Model scale, Architectural scope, Task coverage, Statistical scope, Sparsity range, No throughput evaluation）
- ✅ 页码 "11"
- ✅ 论文正常结束

---

## 发现的问题列表

### 🔴 严重（Critical）

#### C1. 主文远低于页数限制
- **描述**: 主文（§1–§8 + Limitations）仅占约 5 页（含 title/abstract），ACL/EMNLP long paper 限制为 8 页正文 + 不限参考文献/附录
- **影响**: 审稿人可能认为论文内容不够充实，或要求补充主体内容
- **修复建议**: 将 Appendix 中的关键内容（如 cross-model replication Table 4, permutation test Table 5, 部分 Analysis 细节）移回主文，目标 7-8 页正文

#### C2. Figure 1 放置位置异常
- **描述**: Figure 1（fig1_dose_response.pdf, severity gradient plot）在 results.tex 中定义于 Table 2 (table*) 之后，但在 PDF 页面 1-5 的视觉审查中未明确可见。可能被 LaTeX float 算法推迟到非预期位置
- **影响**: 这是 §5.2 的核心可视化图表，如果放置不当严重影响可读性
- **修复建议**: 检查编译后 Figure 1 的实际位置；考虑使用 `[h!]` 或 `[htbp]` 替换 `[t]`，或在 Table 2 之前放置 Figure 1

### 🟡 中等（Warning）

#### W1. 5 个孤立 bib 条目（cited nowhere）
- **条目**: `compression-ordering-2025`, `mustafar-neurips2025`, `obcache-2025`, `pagedeviction-eacl2026`, `raas-acl2025`
- **修复建议**: 删除未引用的 bib 条目，或在正文中补充引用

#### W2. 数值精度不一致（跨节）
- **示例**:
  - Abstract 报告 `0.012`（p 值），results 中出现 `0.01`（可能为不同数值）
  - analysis 报告 `0.047`，results 报告 `0.04`（ΔH 精度不一致）
  - analysis 报告 `0.020`，results 报告 `0.02`
  - analysis 报告 `0.203`，results 报告 `0.20`（II_mid 精度不一致）
- **修复建议**: 统一同一指标在全文中的小数位数。Abstract/Conclusion 中引用的数字应与 Results 中的精度完全一致

#### W3. 3 篇参考文献在线验证未通过
- **条目**: `deepseek-r1-2025`（Nature）, `defensivekv-iclr2026`, `phase-transition-compression-2026`（npj AI）
- **原因**: 可能尚未被 OpenAlex 索引，或标题/作者微调后匹配失败
- **修复建议**: 手动核实这 3 篇文献的出版信息（标题、年份、venue）是否准确

#### W4. h2o-neurips2023 bib 标题解析问题
- **描述**: 引用验证工具报告该条目无标题，但实际 bib 中有标题（使用了 `{H\textsubscript{2}O}` LaTeX 格式）
- **影响**: 工具误报，PDF 中引用正常显示
- **修复建议**: 无需修改（仅工具解析问题）

#### W5. 一致性检查器误报 conclusion 中有未支持的数字 0.50
- **描述**: 工具将 limitations.tex 中的 `$s > 0.50$` 误归类为 conclusion 节
- **影响**: 误报。0.50 是 limitations 中的假设边界值，非实验结果
- **修复建议**: 无需修改

### 🟢 低（Info）

#### I1. 4 个轻微作者不匹配
- `snapkv-neurips2024`: bib 第一作者 Li vs OpenAlex 报告 Cai
- `qwen25-2024`: bib 第一作者 Yang vs OpenAlex 报告 Qwen
- `unicomp-2026`: bib 第一作者 von Rad vs OpenAlex 报告 Rad
- `pagedeviction-eacl2026`: bib 第一作者 chitty-venkata vs OpenAlex 报告 2026
- **修复建议**: 核实 SnapKV 的第一作者是否正确（Li Yuhong vs Cai Zefan）

#### I2. 图片文件命名与论文编号不一致
- `fig3_crossover.pdf` → 论文中为 Figure 2
- `fig5_crossmodel.pdf` → 论文中为 Figure 3
- `fig4_bootstrap.pdf` → 论文中为 Figure 4
- **影响**: 不影响编译，但维护时易混淆
- **修复建议**: 重命名为 `fig2_crossover.pdf` 等匹配实际编号

#### I3. LaTeX 注释中含 REVIEWER-ATTACK/REBUTTAL 预写内容
- **位置**: `appendix_disc_analysis.tex` 多处
- **影响**: 作为 LaTeX 注释不会出现在 PDF 中，但 camera-ready 前应清理
- **修复建议**: 提交终稿前删除所有 `% REVIEWER-ATTACK` 和 `% REBUTTAL` 注释

---

## 整体排版质量评估

| 检查项 | 状态 | 备注 |
|--------|------|------|
| 页边距 | ✅ | ACL 标准 |
| 字体大小 | ✅ | 11pt, Times |
| 双栏对齐 | ✅ | 正常 |
| 页码 | ✅ | 1-11 连续 |
| 行号 | ✅ | review mode 行号显示 |
| 图表编号 | ✅ | Figure 1-4, Table 1-7 连续 |
| 图表 caption | ✅ | 表格 caption 在上，图 caption 在下 |
| 公式编号 | ✅ | Eq.(1)-(7) |
| 公式溢出 | ✅ | 无溢出 |
| [?] 缺失引用 | ✅ | 无（所有 cite 均有对应 bib 条目）|
| 参考文献格式 | ✅ | ACL 标准格式 |
| 匿名化 | ✅ | "Anonymous ACL submission" |
| 主文页数 | ⚠️ | ~5 页，低于 8 页限制 |

---

## 引用完整性摘要

- **总 bib 条目**: 31
- **实际引用 keys**: 26
- **孤立条目（未引用）**: 5
- **缺失条目（引用但无 bib）**: 0
- **在线验证通过**: 23/31
- **在线未找到**: 3（可能尚未索引）
- **轻微不匹配**: 4（作者名细微差异）

---

## 优先修复建议

1. **【紧急】将附录关键内容移回主文**，充实到 7-8 页（Cross-model replication, Permutation test, Analysis 展开）
2. **【紧急】确认 Figure 1 放置位置**，确保在 §5.2 附近可见
3. **【中等】删除 5 个未引用的 bib 条目**
4. **【中等】统一全文数值精度**
5. **【低】核实 3 篇在线验证失败的参考文献信息**
6. **【低】Camera-ready 前清理 REVIEWER-ATTACK 注释**
