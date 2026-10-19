## 数字 Bug 修复记录

| # | 文件 | 行号 | 修改前 | 修改后 |
|---|------|------|--------|--------|
| 1 | appendix.tex | 327 | BT $= 66.5\%$ | BT $= 67.5\%$ |
| 2 | appendix.tex | 334 | Likert $d$...BT is stable at 66.5\%. | Bootstrap median Likert $d$...BT is stable at 67.5\%. Point estimate at $n = 355$: $d = {-}0.025$ (Table~\ref{tab:main_results}). |
| 3 | appendix.tex | 123 | other rows: $n = 88$. | formality rows: $n = 88$; verbosity rows: $n = 86$. |
| 4 | experiments.tex | 74 | three cross-benchmark exceptions (---explaining) | four cross-benchmark exceptions (, explaining) |
| 5 | experiments.tex | 131 | other rows: $n = 88$. | form.\ $n{=}88$, verb.\ $n{=}86$. |

## 验证

### grep "66.5" 剩余出现（均为 Qwen3 formality .665 语境，正确）
- appendix.tex:157 — Qwen3-32B baseline ($66.5\%$ $[58.5, 73.9]$)
- appendix.tex:408 — BT 77.3\% vs. 66.5\% for formality
- appendix.tex:509 — Formality & 66.5\% & 41.7\% & 63.0\%

### grep "67.5" 出现（均为 bootstrap/BT 语境，正确）
- experiments.tex:75 — BT remains stable at $67.5\%$
- appendix.tex:327 — BT $= 67.5\%$
- appendix.tex:334 — BT is stable at 67.5\%

### 编译状态
- 成功（20 页，无 undefined reference）
- 仅常规 warning：float specifier `h` → `ht`、hyperref Unicode token

### 匿名仓库 commit
- hash: 473438e
- message: fix: correct BT/d values in appendix K, GEE footnote n, and cross-benchmark count
- branch: main (ahead of origin/main by 2 commits)

## 待做
- 等用户添加 deploy key 后执行 git push --force origin main
