# ICML 2026 Camera-Ready 预检清单

**项目**: event-gated-adaptive-horizon
**检查日期**: 2026-05-24
**DDL**: 2026-05-29（数据锁定 5/27）

---

## 总览

| 类别 | 通过 | 需修复 | 详情 |
|------|------|--------|------|
| 参考文献审查 | 4 | 3 | 格式问题 |
| ICML 合规检查 | 5 | 1 | 3 个 figure 未引用 |
| Supplement 完整性 | 4 | 0 | 全部通过 |
| **合计** | **13** | **4** | |

---

## ✅ 通过项（13 项）

### 参考文献
1. ✅ arXiv preprint 状态：6 条均为最新，无需更新
2. ✅ DOI 字段一致性：全部无 DOI，格式统一
3. ✅ 年份格式一致：全部四位数
4. ✅ 无悬空引用：44 条 bib 与正文完全对应，无缺失/冗余

### ICML 合规
5. ✅ 模板：icml2026.sty + icml2026.bst
6. ✅ Broader Impact Statement：位于 References 之前（第 6 页）
7. ✅ 页数：正文 6 页（限制 8 页）
8. ✅ 匿名化：无作者/机构/代码链接泄露
9. ✅ 数值一致性：正文与附录关键数值全部一致

### Supplement 完整性
10. ✅ 正文→Appendix 引用：20 处引用全部有对应 label 且内容非空
11. ✅ Appendix 内部引用：35 个 \ref{}，0 个悬空
12. ✅ 图片文件：10 个 \includegraphics 全部存在
13. ✅ Appendix 结构：7 个主 section + 25 个 subsection，内容完整

---

## ⚠️ 需修复项（4 项）

### R1. 作者名格式不一致（参考文献）
- **问题**：18 条用缩写（`Hafner, D`），26 条用全名（`Hafner, Danijar`）
- **修复**：统一为全名格式
- **严重度**：低（不影响编译，但审稿人可能注意到）

### R2. 会议名缩写不一致（参考文献）
- **问题**：`lambert2020objective` 用缩写 `L4DC`，其余均为全称
- **修复**：改为 `Learning for Dynamics and Control`
- **严重度**：低

### R3. sutton1999options journal 字段格式错误（参考文献）
- **问题**：`journal = {Artificial Intelligence 112}`，卷号混入期刊名
- **修复**：拆分为 `journal = {Artificial Intelligence}, volume = {112}`
- **严重度**：中（编译后显示格式异常）

### R4. 3 个 Appendix figure 未被 \ref{} 引用（ICML 合规）
- **问题**：`fig:factorial_grid`、`fig:entropy_dynamics`、`fig:gradient_decomp` 定义了 label 但全文无引用
- **修复**：在对应 appendix 段落添加 `Figure~\ref{fig:...}` 引用
- **严重度**：低（不影响编译，但属于写作规范问题）

---

## 待 Round 5 审稿结果后的动作
- 根据审稿反馈决定是否需要内容修改
- 修复上述 4 项格式问题
- 最终编译验证 + 提交
