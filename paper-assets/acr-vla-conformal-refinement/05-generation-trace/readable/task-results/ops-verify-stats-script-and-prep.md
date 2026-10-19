# ops verify stats script and prep

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-stats-script-and-prep_20260515T164951_result.json`
- **Structured JSON:** [`9a0d4b89ccbd7bf08c82.json`](../../sessions/9a/9a0d4b89ccbd7bf08c82.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整分析结果如下：

---

## 1. 统计分析脚本

**服务器上**：`/root/acr-vla-conformal-refinement/scripts/statistical_analysis.py`（11KB，May 15 21:41）
- 支持 JSON 文件输入（`--file_a`/`--file_b`，nargs="+" 支持多 seed 合并）
- 支持 summary 模式（`--a_success 19 --a_total 100 ...`）
- McNemar paired test、power analysis、dry-run
- **问题**：Fisher test 用的是 **two-sided**（`alternative="two-sided"`），任务要求是 one-sided (obs_only > argmin)

**本地**：`src/analysis/statistical_tests.py`
- Fisher test 正确使用 **one-sided**（`alternative="greater"`）
- Bootstrap CI 基于 task 重采样（保留 inter-task variance）
- 含 magnitude curve 绘图和 comparison table
- `__main__` 里硬编码了 6-task 旧数据（已过期，不含全部 10 task）

## 2. seed=42 数据文件

**不存在。** `logs/` 目录下没有 `eval_object_*.json`，只有 `eval_reconvla_spatial_r2.json`（spatial benchmark, 1 task）。seed=42 的 19/100 和 12/100 结果来自 stdout 日志/ROADMAP 手工记录，evaluate.py 只在指定 `--output_file` 时才保存 JSON。

## 3. 需要修正的问题

| 问题 | 位置 | 修正 |
|------|------|------|
| Fisher test two-sided | 服务器 `scripts/statistical_analysis.py` L60 | 改 `alternative="two-sided"` → `"greater"` |
| seed=42 eval 无 JSON 输出 | 历史运行未指定 `--output_file` | seed=43 运行时确保带 `--output_file` 参数 |
| 本地脚本硬编码数据过期 | `src/analysis/statistical_tests.py` L205 | 更新为 10-task final 数据 |

## 4. 当前可用的 seed=42 summary 数据运行方式

不需要 JSON 文件，直接用 summary 模式：

```bash
# 服务器脚本（修正 Fisher 方向后）
python scripts/statistical_analysis.py \
    --a_success 19 --a_total 100 \
    --b_success 12 --b_total 100 \
    --label_a obs_only --label_b argmin

# 本地脚本（已是 one-sided）
python -c "
from src.analysis.statistical_tests import fisher_test, bootstrap_ci
p = fisher_test(19, 100, 12, 100)
print(f'Fisher one-sided p = {p:.4f}')
"
```

## 5. seed=43 准备

seed=43 实验在 bjb1-18228 的 cuda:2 (obs_only) 和 cuda:3 (argmin) 上跑。完成后需要：
1. 确认 `--output_file` 有指定（否则要从 stdout 提取数据）
2. 合并两个 seed：`obs_only: (19+X)/200`, `argmin: (12+Y)/200`
3. 用 summary 模式或 JSON 模式跑统计检验

**结论**：脚本框架齐全，核心问题是服务器版 Fisher 方向错误（two-sided vs one-sided），以及 seed=42 没有 JSON 输出文件。建议修正服务器脚本的 Fisher 方向，并确保 seed=43 eval 命令带 `--output_file`。

---
