# ICML 2026 投稿材料检查报告
生成时间：2026-05-27（复检更新）
服务器：westd-51268
论文路径：本地 `docs/paper/`（服务器 `westd-51268` 上 `docs/paper/` 目录不存在，论文材料仅在本地项目中）
PDF：`docs/paper/main.pdf` — 31 页, ~1MB

## 检查结果摘要

| # | 检查项 | 状态 | 说明 |
|---|--------|------|------|
| 1 | 页数 | ✅ | 正文 8 页，低于 9 页限制 |
| 2 | 模板格式 | ✅ | icml2026.sty + icml2026.bst，格式正确 |
| 3 | 匿名化 | ✅ | Anonymous Authors，无身份泄露 |
| 4 | Reproducibility Checklist | ✅ | ICML 2026 不要求独立 checklist（与 NeurIPS 不同） |
| 5 | Impact Statement | ✅ | Broader Impact Statement 已包含 |
| 6 | 附录/补充材料 | ✅ | 22 页附录（Sections A-G），嵌入主 PDF |
| 7 | 参考文献 | ⚠️ | 44 条引用，6 条纯 arXiv preprint 需核实 |
| 8 | 图表完整性 | ✅ | PDF 编译成功，所有图正常渲染（⚠️ graphicspath 依赖） |
| 9 | 硬编码路径 | ⚠️ | scripts/ 下多处 /root/ 路径，代码公开前需清理 |
| 10 | 提交包清理 | ⚠️ | 含无关文件（CoRL 模板、rebuttal_notes.md） |

## 详细结果

### 1. 页数
状态：✅
详情：PDF 共 31 页。正文 8 页（pp.1-8：Abstract → Introduction → Related Work → Methodology → Results → Analysis → Conclusion → Broader Impact），参考文献 pp.8-10，附录 pp.10-31。ICML 2026 正文限制 ≤9 页（不含 references/appendix），当前 8 页符合要求。

### 2. 模板格式
状态：✅
详情：
- `\documentclass{article}` + `\usepackage{icml2026}`（main.tex:1,8）
- `icml2026.sty` 和 `icml2026.bst` 均存在
- `\bibliographystyle{icml2026}`（main.tex:86）
- Running header: "Temporal Abstraction Failure in Imagination-Based RL"
- 底部声明: "Preliminary work. Under review by the International Conference on Machine Learning (ICML). Do not distribute."
- 行号已启用（双盲审稿要求），双栏格式正确

### 3. 匿名化
状态：✅
详情：
- 作者：`Anonymous Authors`（main.tex:50）
- 机构：`Anonymous Institution`（main.tex:53）
- 通讯邮箱：`anon@anon.edu`（main.tex:55）
- GitHub 链接：methodology.tex:52 引用 `https://github.com/danijar/dreamerv3` — DreamerV3 官方公开代码库（第三方），非作者仓库，引用合规
- 代码发布："Code: upon acceptance" — 正确延迟公开
- 未检测到：机构名、个人邮箱、grant 致谢、其他身份泄露

### 4. Reproducibility Checklist
状态：✅ 不要求
详情：ICML 2026 不要求提交正式的 Paper Checklist（与 NeurIPS 不同）。论文已满足可复现性要求：
- Limitations 段讨论了局限性
- "Code: upon acceptance" 承诺代码公开
- 实验细节充分（Section 3, Appendix 含完整超参数表 Table 29）
- 所有 45 组实验配置完整记录（Appendix A, Table 3）

### 5. Impact Statement
状态：✅
详情：`Broader Impact Statement` 已包含（PDF p.8）。讨论了 variable-rate world-model RL 在机器人部署中的安全风险及两个防护措施（NVE diagnostic ≥ 2.0×, frozen-embedding check 0/16 controls）。

### 6. 附录 / 补充材料
状态：✅
详情：`\appendix` 在 main.tex:90，加载 `sections/appendix.tex`。附录 22 页（pp.10-31），内容：
- Appendix A: Complete Experimental Results + Cross-Environment CIVO Comparison
- Appendix B: NVE Threshold Sensitivity Analysis（ROC curve, PRF, threshold recommendation）
- Appendix C-G: RSSM fidelity, gradient decomposition, actor entropy, TCN, dual-critic, cosine similarity 等
- 含 Tables 3-31, Figures 5-6
- 无独立 supplementary 文件

### 7. 参考文献
状态：⚠️
详情：
- `references.bib`：345 行，44 条引用
- 使用 `icml2026.bst` 样式，格式一致
- **6 条纯 arXiv preprint**（建议核实是否已正式发表）：
  - `asadi2019combating`: arXiv:1905.13320
  - `tassa2018dmcontrol`: arXiv:1801.00690 — DMC 标准引用，可接受
  - `hafner2025dreamerv4`: arXiv:2509.24527 — 2025 新预印本
  - `wang2024elastic`: arXiv:2402.14961
  - `colas2018seeds`: arXiv:1806.08295
  - `benechehab2023multitimestep`: arXiv:2310.05672
- 其余引用含 `archivePrefix = {arXiv}` 但已注明正式发表会议/期刊

### 8. 图表完整性
状态：✅
详情：PDF 已成功编译，所有图正常渲染。`\graphicspath{{../../artifacts/}}` 解析图片到 `artifacts/` 目录。
⚠️ 构建依赖：提交时需确保 `\graphicspath` 相对路径在提交包内有效，或将图片复制到 `docs/paper/figures/`。

### 9. 硬编码路径
状态：⚠️
问题列表（scripts/ 下 6+ 个文件含 `/root/autodl-tmp/` 路径）：
- `scripts/plan034_nve_sensitivity.py:198`
- `scripts/rssm_fidelity_analysis.py:27,251`
- `scripts/nve_threshold_analysis_v2.py:7`
- `scripts/value_distribution_analysis.py:29,388`
- `scripts/plan031_actor_entropy.py:8,9`
- `scripts/plot_018_results.py:13-17`（5 处）
影响：不影响论文审稿。"Code: upon acceptance" 发布前须清理为相对路径或 CLI 参数。

### 10. 提交包清理
状态：⚠️
详情：`docs/paper/` 目录中存在不应包含在提交包中的文件：
- `_corl_template/` — CoRL 模板目录（无关）
- `rebuttal_notes.md` — **潜在泄露风险**，投稿包中必须移除
- `.aux`, `.log`, `.blg`, `.fls`, `.fdb_latexmk`, `.out` — LaTeX 编译中间文件
- `main.tex.bak` — 备份文件

## 需要修复的问题

### 投稿前必须处理
1. **⚠️ 提交包清理**：打包前移除 `rebuttal_notes.md`（可能泄露非匿名信息）、CoRL 模板文件、LaTeX 中间文件
2. **⚠️ graphicspath 验证**：确认提交 zip 包内 `\graphicspath` 相对路径有效，或内联图片

### 建议处理
3. **⚠️ arXiv 引用**：核实 6 条 arXiv preprint 是否已正式发表，替换为会议/期刊版本
4. **⚠️ 硬编码路径**：代码公开前清理 scripts/ 中的绝对路径

**结论**：论文内容满足 ICML 2026 投稿要求，无阻塞问题（0 个 ❌）。4 个 ⚠️ 项为打包/代码公开时的清理工作。**最高优先**：打包前移除 `rebuttal_notes.md`。
