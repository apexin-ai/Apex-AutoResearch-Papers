# ARR May 2026 Submission Checklist
## DDL: 2026-05-25 (Sun)
## Paper: Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary

---

### 论文 PDF

- [x] 主文 PDF 已编译通过（main.pdf, 546KB, 17页, 编译时间 2026-05-22 17:07）
- [x] 主文正好 8 页（Section 1-7 在第 1-8 页，Limitations 从第 9 页开始），符合 Long Paper 限制
- [x] 使用 ACL 模板（`\usepackage[review]{acl}`，含行号）
- [x] 匿名化（`\author{Anonymous}`）
- [x] Abstract 完整（9 句，覆盖方法、主要发现、跨模型迁移、一致性验证）
- [x] 所有章节完整：Introduction / Related Work / Method / Experiments / K\*-Aware Data Filtering / Discussion / Conclusion
- [x] Limitations section 存在（必需，3 点：scope, feature set, threshold sensitivity）
- [x] Ethics Statement 存在（必需，覆盖 dual-use 和数据来源）
- [x] 参考文献完整（references.bib, 33 条, 291 行）

### 图表

- [x] 主文 5 张图（pipeline, auc\_decay, kstar\_theta, transfer\_heatmap, filtering\_strategies）
- [x] 所有图表已编译为 PDF 格式（figures/ 目录 12 个 PDF）
- [x] 表格文件完整（tables/ 目录 6 个 .tex 文件）
- [x] 附录补充图表齐全

### 补充材料 (Supplementary Material)

- [x] Appendix（appendix.tex, 465 行）：特征排名、跨模型迁移矩阵、高级鲁棒性分析
- [x] Extended Appendix（appendix\_extended.tex, 219 行）：neural probe、LLM zero-shot baseline、扩展 limitations、seed robustness、Bonferroni CI
- [ ] **代码包（匿名化）**：未发现已打包的匿名代码（.zip/.tar.gz），服务器代码在 `/root/autodl-tmp/gen-depth-contamination/`

### OpenReview 表单（需手动填写）

- [ ] Responsible NLP Research Checklist（在 OpenReview submission form 中填写，不在论文 PDF 内）
- [ ] Author information（所有作者 OpenReview profile）
- [ ] Paper type 选择：**Long Paper**
- [ ] Submission track 选择（推荐：NLP Applications 或 ML for NLP）
- [ ] Software/Data link（可选，论文写 "Code and data will be released upon acceptance"）
- [ ] Supplementary material 上传（附录已在 PDF 内，如需额外材料另传）

### 格式合规检查

- [x] 页数限制：主文 8 页 ✓
- [x] 参考文献不限页数 ✓
- [x] Limitations 和 Ethics 不计入 8 页限制 ✓
- [x] `[review]` 选项启用（含行号）✓
- [x] A4 纸张（595.276 x 841.89 pts）✓
- [ ] **确认论文正文无破折号**（用户写作规则要求，需人工扫读确认）

---

## 待完成事项（按优先级排序）

### Blocking（必须在 DDL 前完成）

1. **填写 OpenReview submission form**
   - Responsible NLP Research Checklist（逐项勾选）
   - 填写 author information、paper type (Long)、track
   - 上传 main.pdf

2. **最终 PDF 检查**
   - 确认编译无 warning（当前仅有 hyperref Unicode minor warning）
   - 通读确认无遗留 TODO/placeholder
   - 检查正文行文是否符合"不用破折号"规则

### Optional（建议但非必须）

3. **准备匿名代码包**
   - 从服务器代码中提取核心实验代码
   - 移除所有身份信息、API key、服务器路径
   - 打包为 .zip 上传至 OpenReview supplementary 或匿名 GitHub repo
   - 论文已注明 "released upon acceptance"，DDL 前不提供代码也可接受

4. **Software/Data link**
   - 如准备了匿名代码，填入链接
   - 否则留空（可选字段）

---

## 时间线建议

| 日期 | 事项 |
|------|------|
| 05-23 (Fri) | 最终通读 PDF，检查破折号规则，修复任何 typo |
| 05-24 (Sat) | 填写 OpenReview form（Checklist 耗时较长，预留充足时间） |
| 05-25 (Sun) | DDL 当天：上传 PDF，最终确认，提交 |
