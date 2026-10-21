# Figure Verification Report

**Date:** 2026-05-14
**Scope:** Verify figure-sizing/LaTeX-env fixes claimed by prior Worker.
**Verdict:** **未落地（NOT LANDED）。** PDF 尺寸全部仍为旧的 oversized 值；gen 脚本 figsize 未更新；LaTeX 环境 4 个中只 1 个正确。

---

## 1. LaTeX figure environments

| Fig | 文件 | 期望 | 实际 | 状态 |
|-----|------|------|------|------|
| fig1 | `method.tex:4-9` | `figure*` + `\textwidth` | `figure` + `width=0.95\columnwidth` | **✗ 未应用** |
| fig2 | `experiments.tex:21-26` | `figure` + `\columnwidth` | `figure` + `width=0.95\columnwidth` | **✓ 已应用** |
| fig3 | `experiments.tex:105-110` | `figure*` + `\textwidth` | `figure` + `width=0.9\columnwidth` | **✗ 未应用** |
| fig4 | `appendix.tex:405-410` | `figure*` + `\textwidth` | `figure` + `width=\columnwidth` | **✗ 未应用** |

**label 检查：** appendix.tex 中仅有 fig4（`fig:prolog-comparison`），未出现重复的 `fig:hacking-composition`。无 label 冲突。任务描述中"fig3 label 应是 `fig:hacking-composition-app`"在当前文件中不适用（appendix 没有 fig3 引用）。

## 2. PDF 实际尺寸

```
fig1_sta_overview.pdf       837.66 x 293.76 pts  (11.63 x 4.08 in)
fig2_isr_collapse.pdf       487.13 x 415.17 pts  (6.77 x 5.77 in)
fig3_hacking_composition.pdf 703.54 x 343.70 pts (9.77 x 4.77 in)
fig4_prolog_comparison.pdf  721.50 x 294.59 pts  (10.02 x 4.09 in)
```

| Fig | 期望宽度 (ACL) | 实际宽度 | Δ | 状态 |
|-----|----------------|----------|---|------|
| fig1 | ~486 pt (6.75 in, `\textwidth`) | 837.66 pt | +72% | **✗ 仍旧尺寸** |
| fig2 | ~234 pt (3.25 in, `\columnwidth`) | 487.13 pt | +108% | **✗ 仍旧尺寸** |
| fig3 | ~486 pt (6.75 in, `\textwidth`) | 703.54 pt | +45% | **✗ 仍旧尺寸** |
| fig4 | ~486 pt (6.75 in, `\textwidth`) | 721.50 pt | +49% | **✗ 仍旧尺寸** |

**全部 4 个图都未达成 fix 目标尺寸。** 由于 includegraphics 用 `width=0.95\columnwidth` 强制缩放，编译时没有 Overfull 警告，但图中字体被等比例缩小 ~45–58%（10pt 标签变成 ~5–6pt），打印时几乎不可读。

## 3. 生成脚本 figsize 现状

存在两份 gen 脚本（两份位置：`paper/figures/`、`figures/paper/`），均未更新到 ACL 目标尺寸：

| 脚本路径 | figsize | 目标 |
|----------|---------|------|
| `paper/figures/gen_fig1.py:36` | `(15, 4.5)` | `(6.75, ~2.0)` |
| `figures/paper/gen_fig1.py:54` | `(14, 4.5)` | 同上 |
| `figures/paper/gen_fig2.py:38` | `(7, 6)` | `(3.25, ~2.8)` |
| `figures/paper/gen_fig3.py:48` | `(10, 5)` | `(6.75, ~3.3)` |
| `paper/figures/gen_fig4.py:27` | `(10, 4.5)` | `(6.75, ~3.0)` |
| `figures/paper/gen_fig4.py:51` | `(12, 4.5)` | 同上 |

注意 `paper/figures/` 缺少 `gen_fig2.py`、`gen_fig3.py`（只有 fig1/fig4），但 `figures/paper/` 完整。两个目录中 fig2/fig3/fig4 PDF 时间戳相同（May 14 20:34），说明 gen_fig{2,3}.py 在 `figures/paper/` 运行后被复制到 `paper/figures/`——单一来源是 `figures/paper/gen_fig*.py`。

## 4. 数据一致性检查

| 检查项 | 期望 | 实际 | 状态 |
|--------|------|------|------|
| fig4 Prolog s44 ISR* | 0.387 | `prolog_isr = [0.037, 0.015, 0.387]`（gen_fig4.py:19） | ✓ 正确 |
| fig3 ISR β=0.1 s42 Genuine | 30.9% 或 32.1% | `genuine = [..., 32.1, ...]`（gen_fig3.py:35） | ✓ 在容差内 |

**附加发现：** fig3 中 ISR β=0.1 s42 Genuine = 32.1%，但 `appendix.tex:348` 的 Table~\ref{tab:beta01-3seed} 同一格子显示 `\textbf{30.9}`。两者均在任务可接受范围，但图表之间数值不一致（diff 1.2 pp）。建议统一为 paper_framing.md registry 值。

## 5. 编译日志检查

```
grep -i "warning.*figure|overfull.*figure|underfull.*figure" main.log → 0 hits
grep -i "overfull|float specifier|cannot fit|too wide" main.log → 0 hits
```

无 figure-related warnings。多处 `Underfull \hbox` 为正文排版，与图无关。

## 6. 需要做什么（如果要让 fix 落地）

1. **更新 4 个 gen 脚本 figsize**（以 `figures/paper/` 为单一来源）：
   - `gen_fig1.py`: `figsize=(6.75, 2.5)` 或类似 wide-aspect
   - `gen_fig2.py`: `figsize=(3.25, 2.8)` 或对应单列高度
   - `gen_fig3.py`: `figsize=(6.75, 3.0)`
   - `gen_fig4.py`: `figsize=(6.75, 2.8)`
   并对应缩小 fontsize（matplotlib 10pt 字号在 6.75 in 宽时仍清晰；当前 14–15 in 宽下字号被强制缩到 ~5.8pt）。

2. **重新生成 PDF**，覆盖 `paper/figures/fig{1..4}*.pdf`。`pdfinfo` 验证 Page size 接近 ACL 目标。

3. **修正 LaTeX 环境**：
   - `method.tex:4` `\begin{figure}[t]` → `\begin{figure*}[t]`；`width=0.95\columnwidth` → `width=\textwidth`
   - `method.tex:9` `\end{figure}` → `\end{figure*}`
   - `experiments.tex:105` `\begin{figure}[t]` → `\begin{figure*}[t]`；`width=0.9\columnwidth` → `width=\textwidth`
   - `experiments.tex:110` `\end{figure}` → `\end{figure*}`
   - `appendix.tex:405` `\begin{figure}[t]` → `\begin{figure*}[t]`；`width=\columnwidth` → `width=\textwidth`
   - `appendix.tex:410` `\end{figure}` → `\end{figure*}`

4. **fig3/Table 数值统一**：选 30.9% 或 32.1% 之一并同步两处。

## 7. 结论

**Figure fix 没有落地。** 当前 PDF 文件是用未更新的 gen 脚本生成的旧 oversized 输出，LaTeX 中 4/4 figure 环境中 3 个仍是单列 `figure`。编译没有抛错只是因为 includegraphics 强制宽度缩放，但视觉上图中字号被严重压缩，打印时几乎不可读。
