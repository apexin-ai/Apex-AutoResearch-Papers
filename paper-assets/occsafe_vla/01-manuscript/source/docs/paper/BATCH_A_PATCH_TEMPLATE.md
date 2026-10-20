# Batch A Incremental Patch Template

> 当 Batch A eval 数据到达后，按此模板快速更新论文。

## 预期新数据

Batch A 可能包含以下 v2 seeds（以 registry 为准）：

| Cell | 当前 n | 当前 CAR | 预期新增 seeds | 新增后 n |
|------|--------|---------|---------------|---------|
| Cell 4 (Detach+LN) | 1 | 0.826 | detach_ln_s3 (0.802?), detach_ln_v2_s0 | 2-3 |
| Cell 2 (Full OCC+LN) | 3 | 0.777±0.032 | (可能已完成) | 3+ |

## Step 1: 数据填入 — Table 1 (results.tex)

### Cell 4 更新 (Detach+LN, 当前 line 28)

当前:
```latex
OFF & LN & 1 & $0.826^{b}$ & $0.894$ & $+$8.1 \\
```

替换为（以 n=N, mean=M, std=S 为准）:
```latex
OFF & LN & N & $M \pm S$ & $TSR_M \pm TSR_S$ & $+$DELTA \\
```

计算公式:
- `DELTA = (M - 0.745) * 100`（vs v2 Vanilla 0.745）
- 若 n≥2 且不再 preliminary，移除 `$^{b}$` 标记

### 脚注更新 (Table 1 caption, line 16)

当前: `$^{b}$Preliminary; additional seeds in progress, full results in camera-ready.`

若 Cell 4 n≥3: 移除 `$^{b}$Preliminary...camera-ready` 部分
若 Cell 4 n=2: 改为 `$^{b}$Two seeds; additional seeds in camera-ready.`

### Factorial Table 更新 (Table 2, results.tex line 57-71)

当前 Cell 4 行:
```latex
LayerNorm    & Full OCC+LN (0.777) & Detach+LN ($0.826^{b}$) & $-$4.9$^{b}$ \\
```

替换为:
```latex
LayerNorm    & Full OCC+LN (0.777) & Detach+LN (NEW_MEAN) & $-$NEW_DELTA \\
```

- `NEW_DELTA = 0.777 - NEW_MEAN`（pp, 保留 1 位小数）
- `Δ(BN-LN) Grad OFF` = `0.767 - NEW_MEAN`

### Factorial caption (line 59)

当前: `$^{b}$Cell~4 preliminary ($n{=}1$); additional seeds in progress.`
更新为实际 n。

## Step 2: 文本级联更新

### results.tex §4.1 (line 7-9)

数字引用:
- `Detach+LN result (CAR $0.826$, $n{=}1$)` → 更新 CAR/n
- `$\Delta{=}+8.1$\,pp` → 重算 ΔCAR

### results.tex §4.2 (lines 49-55)

- `$-$4.9\,pp` (LN simple effect) → 重算 `0.777 - NEW_CELL4_MEAN`
- `The within-LN deficit ($-$4.9\,pp) is preliminary ($n{=}1$ for Cell~4)` → 更新 n
- `Detach+LN shows the highest observed CAR in the factorial design ($0.826$)` → 更新值
- `$n{\geq}3$ confirmation is in progress for camera-ready` → 若 n≥3 删除此句

### 效应量重算 (§4.2)

重算 gradient flow main effect:
```
ON_mean  = (Cell1 + Cell2) / 2 = (0.725 + 0.777) / 2
OFF_mean = (Cell3 + NEW_Cell4) / 2 = (0.767 + NEW) / 2
d_main = (ON_mean - OFF_mean) / pooled_SD
```

当前: d=-0.60, p=0.396 → 需用新 Cell 4 数据重算

### abstract (main.tex)

- `Detach+LN` 相关数字如出现需同步

### discussion.tex

- `The BN + gradient flow cell is both the worst-performing...` → 检查是否仍成立
- 若 Detach+LN n≥3 不再 preliminary, 删除 discussion 中的 preliminary 注释

### conclusion.tex

- 无 Cell 4 具体数字，不需改

### appendix.tex (Extended Analysis)

- `the v2 preliminary result ($n{=}1$, CAR $0.826$)` → 更新

### method.tex (Evaluation, line 49)

- `Detach+LN uses v2 ($n{=}1$, preliminary)` → 更新 n

## Step 3: Figure 更新

### factorial_2x2.pdf (Figure 2)

Cell 4 数据点变化 → 需重新生成 factorial interaction plot。
脚本位置: 需用 draw-paper-figure skill 重绘。
关键变化: LN 线的 "Gradient OFF" 端点移动，误差棒出现。

## Step 4: 验证

1. `check_paper_consistency(project="occsafe_vla")` — 全文数字一致性
2. 手动交叉检查: Abstract ↔ Table 1 ↔ §4.2 ↔ Discussion 中的 Cell 4 数字
3. 确认 `$^{b}$` 标记的添加/移除与实际 n 一致

## 快速对照表：Cell 4 数字出现位置

| 文件 | 位置 | 当前值 | 需更新 |
|------|------|--------|--------|
| results.tex | Table 1 (line 28) | 0.826, n=1 | ✅ |
| results.tex | Table 2 (line 66) | 0.826^b | ✅ |
| results.tex | §4.1 text | 0.826, +8.1pp | ✅ |
| results.tex | §4.2 text | -4.9pp, n=1 | ✅ |
| results.tex | §4.2 effect sizes | d=-0.60, p=0.396 | ✅ 重算 |
| abstract | main.tex | (检查是否引用) | ✅ |
| discussion.tex | — | (检查 preliminary 标记) | ✅ |
| appendix.tex | Extended Analysis | 0.826, n=1 | ✅ |
| method.tex | Evaluation | n=1, preliminary | ✅ |
| figures/ | factorial_2x2.pdf | Cell 4 点 | ✅ 重绘 |
