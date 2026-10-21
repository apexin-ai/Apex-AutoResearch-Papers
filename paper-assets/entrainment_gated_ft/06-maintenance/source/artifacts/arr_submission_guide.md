# ARR May 2026 Submission Guide

## Deadline: 2026-05-25

## Files Ready
- **PDF**: `docs/paper/main.pdf` (23 pages: 8 main + refs + appendix, 0 critical warnings)
- **Checklist**: `artifacts/arr_checklist_draft.txt` (copy answers to OpenReview form)
- **Code**: 论文声明 "upon publication"。OpenReview code link 填 "Will be provided upon acceptance"
  - code_release.zip 在远程服务器但 SSH 断了无法下载。如 SSH 恢复可补充匿名链接

## OpenReview Submission Steps
1. 登录 https://openreview.net/group?id=aclweb.org/ACL/ARR/2026/May
2. 点击 "Submit" → "EMNLP 2026 Long Paper"
3. 填写：
   - **Title**: Per-Example Predictive Multiplicity in Hybrid Linear Recurrent Architectures
   - **Abstract**: 从 main.tex 复制（已是最终版）
   - **PDF**: 上传 main.pdf
   - **Software**: "Will be provided upon acceptance"
   - **Responsible NLP Checklist**: 按 arr_checklist_draft.txt 逐项填写
     - ⚠️ C3: 仅填 Bonferroni（不提 Benjamini-Hochberg，论文未使用）
     - ⚠️ A1: "three primary architectures + two extended"（非 five primary）
4. 确认匿名性（已验证 PASS）
5. Submit

## Pre-submission Verification (All PASS)
- [x] 匿名化：\author{Anonymous}，无泄露
- [x] 引用完整：0 undefined citations/references
- [x] Bib 格式：dodge @article ✓, qin2023 ✓, jain2025 ✓
- [x] 页数：主文 8 页 ✓
- [x] Limitations：3 段，主文中 ✓
- [x] Figure 3 heatmap：就位 ✓
- [x] Table 1 HellaSwag：caption 已标注 acc_norm metric ✓
- [ ] Code link：optional，upon publication

## Data Correctness Audit (2026-05-23)
- ✅ 11/15 核心 claims 完全 PASS
- ✅ 34/34 claims 有 provenance 映射
- ⚠️ 1 WARNING（已修复）：Table 1 HellaSwag caption 已标注 acc_norm
- ⚠️ 3 UNVERIFIABLE（需 SSH）：Table 2 三行 J 均值 + Table 30 DeltaNet 逐格
  - 均值一致性检查 PASS，严格逐值验证待 SSH 恢复
- ✅ 1 MINOR：LAMBADA J_u Δ=0.001 四舍五入，不影响结论

## Review History
- R5-R15 均为 3.0 Findings
- R15 后修复全部 Must-Fix/Should-Fix（15/18 issues resolved）
- 新增：5-arch 验证（40/40 显著）、practitioner guidance、seed-noise 概率论证
- 最终 patches：HellaSwag caption 标注、LAMBADA convergence mechanistic insight、α spectrum 决策工具、J bound 简化
