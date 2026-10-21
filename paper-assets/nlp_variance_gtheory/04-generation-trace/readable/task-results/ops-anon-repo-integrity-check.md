# ops anon repo integrity check

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_anon-repo-integrity-check_20260524T065542_result.json`
- **Structured JSON:** [`b04133b8669d91bd326b.json`](../../sessions/b0/b04133b8669d91bd326b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`fig3_dstudy_curves.pdf` exists in `paper/figures/` but is not referenced anywhere in the paper. All other figures are properly referenced. Here's the full report:

---

## 1. 身份泄露扫描

| 关键词 | 结果 |
|--------|------|
| `Cao Xiaoyu` / `曹` / `caoxiaoyu` / `caoxiaoyuyuyuyuyu` | 未发现 |
| `TUM` / `Technical University of Munich` / `München` | 未发现 |
| `Tsinghua` / `清华` / `Peking` / `北大` / `PKU` | 未发现 |
| `@tum.de` / `@gmail.com` / `@qq.com` / `@outlook.com` / `@163.com` | 未发现 |
| 非匿名 GitHub URL | **2 处**，均为合法第三方引用：`github.com/EleutherAI/lm-evaluation-harness`（references.bib）、`github.com/acl-org/acl-style-files/`（acl.sty 注释）。无身份泄露。 |
| `ssh-rsa` / `ssh-ed25519` / `github_deploy` | 未发现 |
| `westd-` / `autodl` / `192.168` / `10.0.` | 未发现 |
| `ghp_` / `sk-` / `hf_` / `API_KEY` | 未发现 |
| `TOKEN` | 仅匹配变量名 `BENCHMARK_MAX_TOKENS`，非泄露 |
| `agent-ml-research` / `idea_gen` | 未发现 |
| Git 提交作者 | `Anonymous &lt;anonymous@example.com>` — 干净 |
| 论文 `\author` 字段 | `\author{Anonymous}` — 干净 |

## 2. 敏感文件检查

未发现任何 `.env`、`.pem`、`.key`、`*credential*`、`*secret*`、`*token*`、`_anonymous_repo.json`、`.log`、`.ssh` 文件。

## 3. 文件清单

**论文源码** — 齐全：main.tex, abstract.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, conclusion.tex, limitations.tex, appendix.tex, references.bib, main.bbl, acl.sty, acl_natbib.bst

**论文图表** — 齐全：fig0_teaser_dstudy.pdf, fig1_cross_benchmark.pdf, fig2_design_diagram.pdf, fig4_difficulty_scatter.pdf, budget_sensitivity_band.pdf 均存在且被引用。`fig3_dstudy_curves.pdf` 存在但未被论文引用（冗余文件）。

**实验代码** — 齐全：`src/` 含 inference、analysis、design、data、config 模块；`scripts/` 含大量实验脚本

**数据** — 齐全：`data/` 含 benchmark item JSON 文件

**配置** — 齐全：requirements.txt + pyproject.toml

**README.md** — 存在

**Tests** — 存在：`tests/test_prompt_templates_multi.py`

**注意**：`docs/paper/abstract.tex` 是一个旧版本的 abstract 副本（与 `paper/abstract.tex` 内容不同），属冗余文件。`figures/paper/` 目录包含 fig1 的副本和生成脚本。

## 4. 代码可运行性

- **README.md**：包含概述、依赖要求（Python 3.10+, vLLM）、安装命令 `pip install -r requirements.txt`、目录结构说明
- **requirements.txt**：存在且非空，12 个依赖，覆盖所有关键第三方包（vllm, torch, transformers, datasets, generalizit, statsmodels, matplotlib, pandas, numpy, scipy, seaborn, tqdm）
- **Import 覆盖**：所有第三方 import 均在 requirements.txt 中

## 5. 总结

**通过** — 匿名化完整，无身份泄露，文件齐全，代码可运行。

**Minor 建议**（不影响通过）：
1. `docs/paper/abstract.tex` 是旧版 abstract 副本，建议删除以免审稿人困惑
2. `paper/figures/fig3_dstudy_curves.pdf` 未被论文引用，建议删除或确认是否遗漏引用
3. `figures/paper/` 根目录下有重复的 fig1 文件和生成脚本 `gen_fig1_cross_benchmark.py`，建议清理

---
