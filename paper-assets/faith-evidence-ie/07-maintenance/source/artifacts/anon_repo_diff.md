# 匿名仓库完整性核查报告

对比日期：2026-05-23

- 服务器：`rtx5090-4x:/root/autodl-tmp/freige/`
- 匿名仓库：`/tmp/anon_repo/`

## 结构映射

匿名仓库将服务器顶层模块重组为 `freige/` 包：

| 服务器路径 | 匿名仓库路径 |
|-----------|-------------|
| `analysis/` | `freige/analysis/` |
| `data/` | `freige/data/` |
| `eval/` | `freige/eval/` |
| `rewards/` | `freige/rewards/` |
| `training/` | `freige/training/` |
| `configs/` | `configs/`（不变） |
| `scripts/` | `scripts/`（精简） |
| `tests/` | `tests/`（不变） |

上述映射下，所有核心源码模块 **1:1 对应**，无遗漏。

---

## 1. GitHub 有但服务器没有的文件（匿名化新增）

| 文件 | 说明 |
|------|------|
| `README.md` | 匿名化新写的项目说明 |
| `requirements.txt` | 为可复现性新增的依赖清单 |
| `freige/__init__.py` | 包初始化（服务器是顶层 `__init__.py`，对应关系见映射） |

均为匿名化/开源化所需的合理新增。

---

## 2. 服务器有但 GitHub 缺少的文件

### 2.1 顶层散落文件（建议不加入）

| 文件 | 说明 |
|------|------|
| `__init__.py`（根目录） | 旧包结构残留，匿名仓库已用 `freige/__init__.py` 替代 |
| `diversity_probe.py` | 与 `training/diversity_probe.py` 重复，残留 |
| `seed_comparison.py` | 临时分析脚本 |
| `training_logs_grpo.json` | 运行时数据 |

### 2.2 docs/ 目录

| 文件 | 说明 |
|------|------|
| `docs/dreeam_evif1_alignment_report.md` | 内部对齐报告，含实验细节 |

### 2.3 scripts/（顶层未包含的脚本）

| 文件 | 类型 |
|------|------|
| `scripts/analysis_4b_supplement.py` | 分析 |
| `scripts/compute_edcr_table.sh` | 分析 |
| `scripts/edcr_diagnostic.py` | 分析 |
| `scripts/edcr_diagnostic.sh` | 分析 |
| `scripts/error_analysis.py` | 分析 |
| `scripts/eval_extract_reward_steps.sh` | 评估 |
| `scripts/eval_grpo_step100.sh` | 评估 |
| `scripts/eval_plan_011_steps.sh` | 评估 |
| `scripts/evidence_tax_analysis.py` | 分析 |
| `scripts/fair_eval.py` | 评估 |
| `scripts/plot_forgetting_dynamics.py` | 可视化 |
| `scripts/plot_forgetting_v6.py` | 可视化 |
| `scripts/plot_spectrum.py` | 可视化 |
| `scripts/stat_analysis.py` | 分析 |
| `scripts/token_length_analysis.py` | 分析 |

### 2.4 scripts/ 子目录（整个目录未包含）

| 目录 | 文件数 | 说明 |
|------|--------|------|
| `scripts/analysis/` | 10 | 深度分析脚本 + 结果文件 |
| `scripts/d102_next_batch/` | 5 | 实验批次脚本 |
| `scripts/d112/` | 2 | 实验批次脚本 |
| `scripts/plan010/` | 1 | NLI 消融实验 |
| `scripts/plan017/` | 4 | 14B 模型实验流程 |
| `scripts/seed_expansion/` | 30 | 多种子扩展实验（完整 train/eval 流程） |
| `scripts/test_eval/` | 3 | 测试集评估脚本 |

### 2.5 残留重复目录

| 目录 | 说明 |
|------|------|
| `freige/freige/` | 嵌套的完整代码副本（含 training/、eval/、configs/ 等），应为 git 操作产生的残留 |

---

## 3. 匿名仓库中保留的 scripts/ 文件（与服务器一致）

以下脚本已包含在匿名仓库中（路径不变）：

- `scripts/convert_codalab.py`
- `scripts/convert_redocred.py`
- `scripts/eval_14b.sh`
- `scripts/eval_test_set.sh`
- `scripts/merge_sft_adapter_14b.py`
- `scripts/merge_sft_rsft.py`
- `scripts/rsft_14b.sh`
- `scripts/sft_14b.sh`

---

## 总结

- **核心源码**：所有 `analysis/`、`data/`、`eval/`、`rewards/`、`training/` 模块 100% 覆盖，只是路径从顶层移入 `freige/` 包
- **配置文件**：5 个 configs 完全一致
- **测试文件**：4 个 tests 文件完全一致
- **脚本**：匿名仓库保留了 8 个核心脚本，省略了 ~70 个实验/分析/可视化脚本（合理精简）
- **新增**：README.md 和 requirements.txt 为开源必需
- **需关注**：服务器上 `freige/freige/` 嵌套副本应清理
