# Anon Repo Figures v3 Report

## Step 1: 搜索结果

| 文件名 | 服务器路径 | 大小 |
|--------|-----------|------|
| `label_decomposition.pdf` | `/root/autodl-tmp/simgate-modular-routing/results/decomposition_dryrun/fig2_label_distribution.pdf` | 16,348 bytes |
| `dose_response.pdf` | `/root/autodl-tmp/simgate-modular-routing/analysis/dose_response_figure.pdf` | 16,097 bytes |
| `death_action_comparison.pdf` | `/root/autodl-tmp/simgate-modular-routing/artifacts/death_action_comparison.pdf` | 35,676 bytes |
| `death_action_distribution.pdf` | `/root/autodl-tmp/simgate-modular-routing/artifacts/death_action_distribution.pdf` | 36,267 bytes |
| `death_action_timeline.pdf` | `/root/autodl-tmp/simgate-modular-routing/artifacts/death_action_timeline.pdf` | 27,081 bytes |

全部 5 个文件均在服务器上找到（其中 2 个文件名不同，已重命名复制）。

## Step 2: 复制验证

目标目录 `/root/autodl-tmp/anon-repo-prep/code/paper/figures/` 当前包含 **8 个 PDF**：

1. `death_action_comparison.pdf` (35,676)
2. `death_action_distribution.pdf` (36,267)
3. `death_action_timeline.pdf` (27,081)
4. `dose_response.pdf` (16,097)
5. `fig1_daf_scatter.pdf` (24,317)
6. `label_decomposition.pdf` (16,348)
7. `pipeline_overview.pdf` (34,660)
8. `signal_reversal.pdf` (20,548)

另有 `signal_reversal.png` (83,344)。所有文件大小 > 0。

与 tex 中 `\includegraphics` 引用的 8 个 figure 文件完全匹配。

## Step 3: Git commit

- Commit: `202d1ec` — "Update paper to submission version with all figures"
- Author: `Anonymous <anonymous@example.com>`
- 25 files changed, 1101 insertions(+), 614 deletions(-)
- `experiments.tex`: 117 lines

**git status (commit 前)**:
- 5 new figure PDFs staged
- 多个 tex 文件修改（abstract, conclusion, discussion, experiments, introduction, main, method, related_work, references.bib）
- 新增 responsibleNLPchecklist.tex, signal_reversal.png 等
- 删除了 figures 目录下的 gen_*.py 生成脚本

## Step 3: Git push — FAILED

**错误**: `fatal: could not read Username for 'https://github.com'`

Remote: `https://github.com/anonymous-nlp-2026/simgate-modular-routing.git`

原因: 服务器上无 GitHub token（无 `.git-credentials`、无 `.gitconfig`、无 `GH_TOKEN` 环境变量）。SSH key 也无该仓库权限。

**需要用户操作**: 提供 GitHub Personal Access Token，然后执行：
```bash
cd /root/autodl-tmp/anon-repo-prep/code
source /etc/network_turbo
git remote set-url origin https://<TOKEN>@github.com/anonymous-nlp-2026/simgate-modular-routing.git
git push -f origin main
```

## 最终状态

| 项目 | 状态 |
|------|------|
| Figure PDF 搜索 | ✅ 全部 5 个找到 |
| 复制到目标目录 | ✅ 8 个 PDF 就位 |
| git commit | ✅ 202d1ec |
| git push | ❌ 需要 GitHub token |
