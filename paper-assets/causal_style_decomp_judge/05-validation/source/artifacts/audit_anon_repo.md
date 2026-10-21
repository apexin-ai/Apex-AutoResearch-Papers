## 匿名仓库审计报告

**仓库**: https://github.com/anonymous-nlp-2026-2/causal_style_decomp_judge
**审计时间**: 2026-05-25 16:55 UTC

### (a) 密钥状态：失效（阻塞推送）

服务器 westb-29275 上未发现任何可用的 GitHub 凭据：
- `/root/.ssh/` 无 deploy key（仅有 authorized_keys）
- 无 `.gitconfig`、`.git-credentials`、`.netrc`
- 环境变量无 PAT/token
- `gh` CLI 未安装

已生成新 deploy key：
```
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIG5MG44UB8faO3E9sshJaN84prXlvxwwQZ84BQG3+5E2 anon-repo-deploy
```
**需要用户操作**：将此公钥添加到 GitHub 仓库 Settings → Deploy keys（勾选 Allow write access），然后重新执行 push。

SSH config 已配置完毕（Host github-anon），push 命令就绪：
```bash
cd /tmp/anon_repo_check && git push --force origin main
```

### (b) 推送时间戳：待完成

等待 deploy key 注册后推送。

### (c) 匿名性确认

| 检查项 | 状态 |
|--------|------|
| Commit author/committer | ✅ 全部为 `Anonymous <anonymous@example.com>`（40 commits） |
| LaTeX `\author` | ✅ `\author{Anonymous}` |
| README / LICENSE | ✅ 无真实姓名、机构名、邮箱 |
| 代码路径泄露 | ⚠️ **已修复** — 9 处 `/home/ubuntu/.agent-ml-research-...` 绝对路径 |
| wandb entity/project | ✅ 无泄露 |

### (d) 修复清单

1. **路径泄露修复**（8 个文件）：将绝对路径替换为 `os.path.dirname(os.path.abspath(__file__))` 相对路径
   - `figures/cross_benchmark_heatmap.py:128`
   - `figures/draw_pipeline.py:179`
   - `figures/gen_cross_benchmark_heatmap_v2.py:122`
   - `figures/gen_forest_plot.py:157`
   - `figures/gen_gee_decomposition.py:125`
   - `figures/gen_gee_decomposition_v2.py:151`
   - `figures/gen_pipeline_diagram.py:142`
   - `paper/figures/gen_forest_plot.py:155`

2. **删除 `_figure_backups/` 目录**：3 个时间戳子目录、10 个备份文件（含路径泄露的 .py 和 PDF）

3. **删除根目录重复 LaTeX 文件**：`main.tex`、`main.pdf`（4.8MB）、`acl.sty`、`acl_natbib.bst`、`references.bib`（均与 `paper/` 下重复）

4. **补充 requirements.txt 缺失依赖**：添加 `choix>=0.3`、`statsmodels>=0.14`（README 中提及但未列入）

### (e) 完整性

| 项目 | 状态 |
|------|------|
| README.md | ✅ 完整（结构说明、环境依赖、复现步骤、数据来源） |
| 核心 CSD pipeline | ✅ `csd_pipeline/`（data_prep, counterfactual_gen, content_verification, judge_scoring, pairwise_scoring, ate_analysis） |
| 统计分析脚本 | ✅ `analysis/`（bootstrap, GEE diagnostics, verbosity, length confound, construct divergence） |
| 实验脚本 | ✅ `experiments/`（exp010-014） |
| 评分脚本 | ✅ `scoring/`（GPT-4o, Claude, Llama-70B, Qwen-32B） |
| 图表生成 | ✅ `figures/`（forest plot, heatmap, GEE decomposition, pipeline diagram, power curve） |
| LaTeX 论文源码 | ✅ `paper/`（main.tex + sections/ + references.bib） |
| requirements.txt | ✅ 已补全 |

### (f) 干净度

- 删除 `_figure_backups/`（10 个备份文件，含 PDF 和旧版 .py）
- 删除根目录 5 个重复文件（main.pdf 4.8MB、main.tex、acl.sty、acl_natbib.bst、references.bib）
- 无 `.DS_Store`、`__pycache__`、`.pyc`、`.env`、`.ipynb_checkpoints`、wandb/ 目录
- `.gitignore` 覆盖全面
- `paper/main.pdf`（5.0MB）保留 — 审稿需要编译后 PDF

### (g) 未解决问题

1. **推送阻塞**：需要将 deploy key 公钥添加到 GitHub 仓库。公钥已生成并配置在服务器上，等待用户在 GitHub 侧注册。
2. **`paper/main.pdf`（5.0MB）** 在 git 中跟踪 — 对于匿名审稿仓库可接受，但长期建议用 GitHub Actions 编译或 Release 附件。
