# research pythia integration template

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_pythia_integration_template_20260521T045034_result.json`
- **Structured JSON:** [`ca8b3a51bd37638dc839.json`](../../sessions/ca/ca8b3a51bd37638dc839.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇报如下：

---

## 产出

**1. 自动化脚本**: `scripts/patch_pythia_results.py`（已在服务器上验证通过）
- 输入：`results/exp_pythia69b_c4/` 目录下的 `pairwise_auc.json` + 可选 `bootstrap_ci_results.json`
- 输出：LaTeX 表格行（主表 + 扩展表）、setup 表行、分场景 claim 更新清单、JSON report

**2. 整合方案文档**: `artifacts/pythia_integration_template.md`

---

## 关键发现

**主表格式**：`tab:kstar_ci`（experiments_c1.tex:18）已有 5 列，空间有限。推荐 Pythia-6.9B 放入 `tab:kstar_ci_extended`（appendix.tex:101），正文引用。

**需更新的 claim 共 14 处**，分布在 6 个文件：

| 文件 | 更新点 |
|------|--------|
| main.tex (abstract) | config count × 2 |
| introduction.tex | :19 config count, :21 ratio |
| experiments_c1.tex | :4 text count, :5 model list, :43 ratio + AUC range, scale paragraph |
| conclusion.tex | :5 ratio |
| discussion.tex | boundary_cases paragraph × 2 |
| appendix.tex | tab:kstar_ci_extended 新增列 |

**场景概率**：K\*=2 最可能（与 Qwen-7B/LLaMA-8B 一致）；K\*=1 次之（Pythia 更大但 0v1 JSD 可能更低）；K\*≥3 不太可能。

**结果出来后执行**：
```bash
cd /root/autodl-tmp/gen-depth-contamination
python scripts/patch_pythia_results.py --results_dir results/exp_pythia69b_c4
```

---
