# paper anon github verify

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_anon_github_verify_20260522T081545_result.json`
- **Structured JSON:** [`5556751149f95dc405fd.json`](../../sessions/55/5556751149f95dc405fd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## Anonymous GitHub 包验证报告

### 1. 代码完整性

| 检查项 | 状态 | 说明 |
|--------|------|------|
| 核心脚本（数据处理） | **PASS** | `preprocess_fewrel.py`, `preprocess_maven.py`, `few_nerd_utils.py`, `fewrel_utils.py`, `maven_utils.py` |
| 核心脚本（实验运行） | **PASS** | `run_extraction.py`, `run_experiment.py`, `run_batch_composition.py`, `run_sdgd_experiment.py` 等 |
| 核心脚本（评估/BCS/SCS） | **PASS** | `evaluate.py`, `compute_bcs.py`, `compute_maven_scs.py`, `bootstrap_ci.py`, `scs_validation.py` |
| SDGD 模块 | **PASS** | `src/sdgd/` 含 `__init__.py`, `similarity.py`, `graph.py`, `decompose.py`, `merge.py`, `evaluate.py`, `calibrate.py` |
| requirements.txt | **PASS** | 13 个依赖，版本约束合理 |
| README.md | **PASS** | 存在，内容详细 |
| LICENSE | **PASS** | MIT，Copyright "Anonymous Authors" |
| **configs/ 目录** | **FAIL** | README 中引用了 `configs/fewnerd_type_definitions.json`，但 `configs/` 目录不存在 |

### 2. 匿名性检查

| 检查项 | 状态 | 说明 |
|--------|------|------|
| 真实姓名/机构/邮箱 | **PASS** | 未发现 |
| 服务器地址/SSH | **PASS** | grep 命中仅为格式化字符串中的 `%-10.4f` 等，误报 |
| .git / .gitconfig | **PASS** | 不存在 |
| wandb/seetacloud/autodl 路径 | **PASS** | 未发现 |
| 绝对路径泄露 | **PASS** | 仅 `/path/to/Qwen3-32B` 占位符，无真实路径 |
| **API Key 泄露** | **FAIL** | `src/run_fewrel_gpt4o_mini.py:42` 硬编码了 `DEFAULT_API_KEY = "tum_XXB3sZILRCg8llb3NjxVbbRNzFpsYVFdiogFkavpGn8"`。前缀 `tum_` 可能关联机构身份（TUM = Technische Universität München），且泄露了有效 API key |
| GitHub 链接 | **PASS** | `data/README.md` 中仅引用第三方数据集 GitHub 仓库（thunlp/DocRED, THU-KEG/MAVEN），非作者仓库 |

### 3. README 质量

| 检查项 | 状态 | 说明 |
|--------|------|------|
| 安装依赖说明 | **PASS** | `pip install -r requirements.txt` |
| 复现 count curves | **PASS** | 命令和参数完整 |
| 复现 BCS regression | **PASS** | `run_batch_composition.py` 命令清晰 |
| 复现 SDGD | **PASS** | 含 zero-shot、calibrated、baselines 多种模式 |
| 数据获取说明 | **PASS** | `data/README.md` 提供了 4 个数据集的下载链接和预处理脚本 |
| 项目结构说明 | **PASS** | 详细列出了核心文件及功能 |

### 4. 大文件检查

| 检查项 | 状态 | 说明 |
|--------|------|------|
| 模型权重/checkpoint | **PASS** | 不存在 |
| 数据集文件 | **PASS** | `data/` 仅含 `README.md` |
| 总大小 | **PASS** | 996K，21145 行代码，纯代码包 |

---

### 问题汇总（需修复）

1. **`src/run_fewrel_gpt4o_mini.py:42` — API Key 泄露 + 潜在去匿名化**
   - `DEFAULT_API_KEY = "tum_XXB3sZILRCg8llb3NjxVbbRNzFpsYVFdiogFkavpGn8"` 
   - `tum_` 前缀可能暴露机构身份
   - 应替换为 `"YOUR_API_KEY_HERE"` 或改为纯环境变量读取

2. **`configs/` 目录缺失**
   - README 第 58 行引用 `configs/fewnerd_type_definitions.json`
   - 需要补上 configs 目录及类型定义文件，或在 README/data README 中说明如何生成

---
