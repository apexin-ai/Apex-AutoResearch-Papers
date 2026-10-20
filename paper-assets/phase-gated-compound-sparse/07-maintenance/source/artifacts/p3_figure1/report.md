# P3: Figure 1 Data Source Confirmation

## 结论

**Figure 1 已更新为 n=496 数据。** 无需重新生成。

## 详细信息

### 当前状态

| 项 | 值 |
|---|---|
| LaTeX 引用 | `results.tex:57` → `fig1_dose_response.pdf` |
| 生成脚本 | `/root/autodl-tmp/pacs/figures/fig1_dose_response_n500.py` |
| 数据源 | `table2_n500_full.csv` (DeepSeek-R1-Distill-Qwen-7B, n=496) |
| 文件时间戳 | 2026-05-15 21:27 (figures/ 和 paper/figures/ 一致，16925 bytes) |

### 脚本中的 n=496 数据

```
sparsity = [0.15, 0.20, 0.25, 0.30]
Importance G = [7.45, 17.90, 49.06, 79.79]   ← n=496 median
Random G     = [0.52,  0.76,  1.09,  1.15]   ← n=496 median
```

脚本注释明确说明 "n=496 paired problems" 和 "Replaces old n=50 profiling figure"。

### 发现的不一致（非本任务范围，但需注意）

1. **Figure 1 caption 与图不匹配**：caption (`results.tex:59`) 写 "from $69\times$ to $274\times$"，这是旧 n=50 的 G 值。n=496 数据的 G 范围是 ~7.5× 到 ~80×。
2. **Table 1/2 仍为 n=50 数据**：`tab:aggregate-ii` 和 `tab:main-results` caption 写 "across 50 problems"，表格数值（G = 69, 103, 222, 274）是旧数据。Figure 1 已用 n=496 数据但表格未同步更新。

## 建议后续动作

- 更新 Table 1/2 为 n=496 数据
- 更新 Figure 1 caption 中的 G 值范围（69×–274× → ~7.5×–80×）
- 或统一确认是否论文正文需全面切换到 n=496
