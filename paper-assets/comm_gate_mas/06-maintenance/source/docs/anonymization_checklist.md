# Anonymization Checklist for NeurIPS Submission

Scan date: 2026-04-27

## 作者/机构/邮箱

| 文件 | 行号 | 内容 | 处理建议 |
|------|------|------|----------|
| `artifacts/paper/main.tex` | 47 | `\author{Anonymous Author(s)}` | ✅ 已匿名，无需处理 |
| `artifacts/paper/neurips_2026.sty` | 16 | `Roman Garnett (garnett@wustl.edu)` — 模板作者 | 无需处理（NeurIPS 官方模板） |
| `artifacts/paper/references.bib` | — | 所有引用均为公开发表文献 | 无需处理 |
| Git history | — | `agent-001 <agent-001@agent-001s-MacBook-Air.local>`, `agent-ml <agent@ml>` | 提交匿名仓库时需 rewrite history 或用 fresh repo |

**结论**: 论文 .tex 文件已正确匿名。Git author 需在制作匿名仓库时处理。

---

## 硬编码路径

### `/Users/agent-001/` 本地路径（高优先级）

| 文件 | 行号 | 内容 | 处理建议 |
|------|------|------|----------|
| `src/d049_analysis.py` | 16 | `BASE = Path("/Users/agent-001/.agent-ml-research/projects/comm_gate_mas/outputs/full_scale")` | 改为相对路径 |
| `src/d049_analysis.py` | 376 | `out_path = Path("/Users/agent-001/...outputs/v7_analysis/d049_results.json")` | 改为相对路径 |
| `src/d051_unified_me_lrt.py` | 16 | `BASE = Path("/Users/agent-001/...outputs/full_scale")` | 改为相对路径 |
| `src/d051_unified_me_lrt.py` | 31 | `OUT_DIR = Path("/Users/agent-001/...outputs/v7_analysis")` | 改为相对路径 |
| `scripts/run_llama_length_only.sh` | 3 | `cd /Users/agent-001/.agent-ml-research/projects/comm_gate_mas` | 改为 `cd "$(dirname "$0")/.."` |
| `scripts/restart_72b_oracle.sh` | 5 | `cd /Users/agent-001/.agent-ml-research/projects/comm_gate_mas` | 改为 `cd "$(dirname "$0")/.."` |
| `data/human_annotation/iaa_3annotator.py` | 10 | `BASE = "/Users/agent-001/...data/human_annotation"` | 改为相对路径 |
| `data/human_annotation/iaa_analysis.py` | 11 | `BASE = "/Users/agent-001/...data/human_annotation"` | 改为相对路径 |

### `/root/autodl-tmp/` 服务器路径（高优先级）

| 文件 | 行号 | 内容 | 处理建议 |
|------|------|------|----------|
| `src/heuristic_threshold_sweep.py` | 6-8 | 3 条硬编码 `/root/autodl-tmp/comm_gate_mas/outputs/...` 路径 | 改为相对路径或 CLI 参数 |
| `src/exp_placeholder_sensitivity.py` | 47 | `"/root/autodl-tmp/.hf_cache/sentence-transformers/all-MiniLM-L6-v2"` | 改为 config 参数 |
| `scripts/run_full_scale.sh` | 17-18 | `export HF_HOME=/root/autodl-tmp/.hf_cache` | 改为 `${HF_HOME:-~/.cache/huggingface}` |
| `configs/*.yaml` (36 个文件) | 各处 | `name: "/root/autodl-tmp/models/..."` 和 `embedding_model: "/root/autodl-tmp/..."` 共 42 处 | 统一改为占位符如 `models/Llama-3.1-8B-Instruct` |
| `paper_provenance.yaml` | 180, 254 | `server:/root/autodl-tmp/comm_gate_mas/...` | 移除或替换为通用路径 |

### 项目管理文件中的路径（可直接排除不提交）

| 文件 | 涉及内容 | 处理建议 |
|------|----------|----------|
| `AGENTS.md` | 大量 `/Users/agent-001/...` 和 `/root/autodl-tmp/...` | 不提交到匿名仓库 |
| `memory.md` | 本地路径、服务器信息 | 不提交 |
| `registry.yaml` | 72 处 `westb`/`seetacloud`，17 处 `/root/autodl-tmp/`，3 处 `caoxiaoyu` | 不提交 |
| `task_context/` 全部 | 服务器名、账户名、路径 | 不提交 |
| `report.md` | 25 行 `westb-4x6000-a` | 不提交 |
| `decisions.yaml` | 项目决策日志 | 不提交 |
| `d173_diag.md` | 调试日志 | 不提交 |
| `docs/experiment_log.md` | 29-36 行服务器路径 | 不提交或清理 |
| `docs/analysis_4abc_results.md` | 5-8 行 `autodl-comm-gate` 和服务器路径 | 不提交或清理 |

---

## API Keys / Tokens

| 文件 | 行号 | 内容 | 处理建议 |
|------|------|------|----------|
| `configs/*.yaml` (全部) | 各处 | `api_key: "[REDACTED]"` | ✅ 占位符，安全 |
| `src/pruning_validation.py` | 1385-1390 | `os.environ.get("OPENAI_API_KEY")` | ✅ 环境变量引用，安全 |
| `src/gpt4o_annotation.py` | 342-344 | `os.environ.get("OPENAI_API_KEY")` | ✅ 环境变量引用，安全 |
| `src/deepseek_calibration.py` | 174 | `os.environ.get("ORACLE_API_KEY")` | ✅ 环境变量引用，安全 |

**结论**: 无硬编码 key/token，全部通过环境变量获取。无需处理。

---

## 其他标识符

### 个人账户名

| 文件 | 行号 | 内容 | 处理建议 |
|------|------|------|----------|
| `registry.yaml` | 729, 1201, 1789 | `account: caoxiaoyu` | 不提交 |
| Git history | — | author: `agent-001`, `agent-ml` | 匿名仓库用 fresh commit history |

### 服务器/平台标识

| 文件 | 出现次数 | 内容 | 处理建议 |
|------|----------|------|----------|
| `registry.yaml` | ~72 | `westb-4x6000-a`, `connect.westb.seetacloud.com` | 不提交 |
| `task_context/` | ~20 | 服务器名、SeetaCloud 域名 | 不提交 |
| `memory.md` | ~5 | `autodl-comm-gate` | 不提交 |
| `docs/experiment_log.md` | 29 | `autodl-comm-gate` | 不提交或清理 |
| `report.md` | 25 | `westb-4x6000-a` | 不提交 |

### GitHub / W&B

| 文件 | 行号 | 内容 | 处理建议 |
|------|------|------|----------|
| `README.md` | 11 | `https://github.com/ag2ai/ag2` | ✅ 公开库引用，安全 |
| `AGENTS.md` | 203 | wandb-guide skill 引用 | 不提交 |

---

## 总结

- **需处理的源代码文件**: 8 个（`src/` 4 个 + `scripts/` 2 个 + `data/human_annotation/` 2 个）
- **需处理的配置文件**: 36 个 YAML（`/root/autodl-tmp/` 模型路径）
- **应排除不提交的文件**: `AGENTS.md`, `memory.md`, `registry.yaml`, `report.md`, `decisions.yaml`, `decisions.lock`, `d173_diag.md`, `paper_provenance.yaml`, `task_context/` 全部, `docs/experiment_log.md`, `docs/analysis_4abc_results.md`, `docs/p15_p16_log.md`, `docs/p1_fixes_log.md`, `docs/r11_audit.md`, `docs/writing_polish_log.md`, `docs/narrative_review.md`, `ROADMAP.md`, `ROADMAP.lock`
- **高优先级项**: 8 个源代码/脚本中的硬编码绝对路径
- **论文 .tex 文件**: ✅ 已正确匿名
- **API Keys**: ✅ 全部通过环境变量，无泄露风险

### 建议操作顺序

1. **先修 8 个源代码文件**的硬编码路径 → 改为相对路径
2. **36 个 configs/*.yaml** 模型路径 → 统一改为相对路径（如 `models/Llama-3.1-8B-Instruct`）
3. **制作匿名仓库时** → `.gitignore` 或直接不 include 上述管理文件
4. **Git history** → 用 `git filter-branch` 或 fresh repo 清除 author 信息
