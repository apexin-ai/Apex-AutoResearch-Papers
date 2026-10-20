# paper repo audit and link

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_repo-audit-and-link_20260525T083815_result.json`
- **Structured JSON:** [`9b7c267cf0230bbeee6e.json`](../../sessions/9b/9b7c267cf0230bbeee6e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## Part 1: 匿名仓库

- **密钥状态：失效** — 本地 deploy key 绑定的是 `caoxiaoyuyuyuyuyu/agent-ml-research`，对 `anonymous-nlp-2026-2/gated_mfrm_judge_bias` 无 push 权限。需要为匿名仓库添加新的 deploy key（write access）或使用 PAT。
- **匿名性：有问题**
  - git author/committer：`Anonymous &lt;anonymous@example.com>` ✅
  - **`TUM_PROXY_KEY`** 出现在 2 个文件中，泄漏机构信息：
    - `exp001/judge_interface.py:343`
    - `exp001/generate_responses.py:24`
  - 需要重命名为 `API_PROXY_KEY` 或 `PROXY_API_KEY`
  - 其他（真实姓名、邮箱、wandb entity）未发现 ✅
- **完整性：通过** ✅
  - README.md 覆盖环境要求、依赖安装、入口脚本、数据获取方式
  - 核心代码齐全（exp001 收集、exp002 exposure、exp003 MCMC fitting、exp004 baselines、lib/、mvp/）
  - requirements.txt 完整
- **干净度：通过** ✅
  - 无 .DS_Store / \_\_pycache\_\_ / *.pyc / .env / wandb/ / checkpoint 文件
  - .gitignore 覆盖充分
- **推送：未执行** — 密钥无权限，等待你配置新 key 后重推

## Part 2: 论文链接

- **删除位置：** `limitations.tex` 第 7 行 — 已删除 `Code and data will be released upon acceptance at [anonymized URL].`
- **添加位置：** `abstract.tex` 第 2 行末尾 — 添加 `\footnote{Code and data are available at \url{https://github.com/anonymous-nlp-2026-2/gated_mfrm_judge_bias}.}`
- **重复检查：** 其他 .tex 文件无重复链接 ✅
- **url 包：** acl.sty 已包含 `\usepackage{url}` ✅
- **编译：通过** — 17 pages, 无错误

---
