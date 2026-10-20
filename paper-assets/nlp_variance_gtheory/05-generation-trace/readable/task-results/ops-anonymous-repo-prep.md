# ops anonymous repo prep

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_anonymous_repo_prep_20260523T124848_result.json`
- **Structured JSON:** [`64df89ff71dd57538ee5.json`](../../sessions/64/64df89ff71dd57538ee5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。报告如下：

---

**1. 最终文件数：148 个**

**2. 文件构成：**
- `src/` — 15 个核心库文件（data/design/inference/analysis/config）
- `scripts/` — 81 个分析和实验脚本（含 exp001-004 子目录）
- `tests/` — 1 个测试文件
- `figures/paper/` — 1 个图表生成脚本（已删除生成的 PDF/PNG）
- `data/` — 15 个 JSON 数据文件（采样的 benchmark items）
- 根目录 — 12 个文件（run_*.sh, run_*.py, requirements.txt, pyproject.toml, README.md, .gitignore）

**3. 匿名化替换：**
- `caoxiaoyu` / `caoxiaoyuyuyuyuyu` / `1844118046@qq.com` — 未出现，无需替换
- `/root/nlp_variance_gtheory` → `.`（相对路径）— 所有 .py 和 .sh 文件
- `/root/autodl-tmp/.hf_cache/...` → HuggingFace model IDs（如 `meta-llama/Llama-3.1-8B-Instruct`）
- `/root/miniconda3/etc/profile.d/conda.sh` → `$CONDA_PREFIX/etc/profile.d/conda.sh`
- `export HF_HOME=/root/autodl-tmp/.hf_cache` → `export HF_HOME=${HF_HOME:-$HOME/.cache/huggingface}`
- `src/config/model_paths.py` — 完全重写，移除所有本地路径映射，只保留 HF model ID 和 display name
- `figures/paper/fig1_cross_benchmark.pdf` 和 `.png` — 删除（可能含元数据）
- Git remote URL 中的 token — 已在 push 后移除 remote

**4. Git log：**
```
Anonymous &lt;anonymous@example.com> Anonymous submission for review
```

**5. 潜在敏感文件：** 无。所有 grep 检查（caoxiaoyu、1844118046、/root/、autodl、westd-）均返回空。

**6. Push 状态：** 成功推送到 `main` 分支。服务器上已删除 remote 配置以避免 token 残留。

---
