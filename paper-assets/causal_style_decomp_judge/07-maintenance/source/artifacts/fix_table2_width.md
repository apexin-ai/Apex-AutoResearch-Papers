## Table 2 宽度修复

### 修改内容
- 在 `sections/experiments.tex` 的 `tab:gee`（Table 2，GEE conditional decomposition）外层添加 `\resizebox{\columnwidth}{!}{...}` 包裹整个 `tabular` 环境
- 移除了之前的 `\small` 字号设置（resizebox 自动按比例缩放）
- 表格结构、内容、列名均未改动

### 编译结果
- 页数：8 页（正文 Introduction–Conclusion），Limitations+References 在第 9-10 页
- Table 2 相关 overfull hbox warnings：无
- 其他 overfull warnings：4 个，均在 appendix 中（与 Table 2 无关）

### 验证
- Table 2 是否在 column width 内：是（resizebox 强制缩放至 \columnwidth）
- 正文 ≤ 8 页：是
- 原始表格仅超宽 12.33pt（约 5%），缩放后视觉差异极小
