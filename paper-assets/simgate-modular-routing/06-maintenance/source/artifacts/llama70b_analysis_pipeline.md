# Llama-70B Episode Analysis Pipeline

## 脚本位置
`/root/autodl-tmp/simgate-modular-routing/src/analyze_llama70b.py`

## 功能
读取 episode collection 结果（`episodes.jsonl` 或 `episode_summary.jsonl`），执行：
1. **3-class label 分类**: det-preferred / internal-preferred / no-preference（与 `death_decomposition.py` 逻辑一致）
2. **4-class counterfactual decomposition**: death_sole / death_and_score / non_death / no_preference
3. **Aggregate metrics**: delta_full, delta_nd, DAF, label_fraction, death rates
4. **Bootstrap 95% CI** (B=10,000, episode-level resampling, percentile method)
5. **Per-task breakdown**: 每个 task 的 death rate, delta_full, label counts
6. **Cross-model 对比表**（可选，通过 `--comparison_data` 加载）

输出：JSON 分析文件 + Markdown 报告。

## Dry-Run 验证结果（Qwen plan_c 数据）

### 预期 vs 实际

| Metric | Expected | Actual | Match |
|--------|----------|--------|-------|
| Episodes | 245 | 245 | ✅ exact |
| delta_full | 29.60 | 29.60 | ✅ exact |
| delta_nd | 2.84 | 2.84 | ✅ exact |
| DAF | 90.4% | 90.4% | ✅ exact |
| label_fraction | 78.9% | 78.9% | ✅ exact |
| det-preferred | 86 | 86 | ✅ exact |
| internal-preferred | 9 | 9 | ✅ exact |
| no-preference | 150 | 150 | ✅ exact |
| int_death_rate | 42.9% | 42.9% | ✅ exact |
| det_death_rate | 16.3% | 16.3% | ✅ exact |
| DAF CI (B=1000) | ~[81.3, 99.1] | [81.6, 99.3] | ✅ within sampling variance |

### 4-class 分解
| Category | Count |
|----------|-------|
| death_sole | 54 |
| death_and_score | 21 |
| non_death | 20 |
| no_preference | 150 |

验证: label_fraction = (54+21)/(54+21+20) = 75/95 = 78.9% ✅

### 与已有分析交叉验证
- DAF point estimate 0.9041409 与 `daf_sensitivity_3model.json` 完全一致
- Death rate 与 `cross_model_bootstrap_cis.json` 完全一致
- Bootstrap CI 与已有结果一致（B=1000 vs B=10000 的采样差异在预期范围内）

## 注意事项
1. **数据源优先级**: 脚本优先读 `episodes.jsonl`（权威数据源），仅在不存在时回退到 `episode_summary.jsonl`（后者可能有重复/缺失条目）
2. **死亡判定**: `score <= -penalty`，默认 penalty=100
3. **DAF 定义**: `1 - delta_nd / delta_full`，其中 `both_alive` = 双方 score 均 > -100
4. **Bootstrap**: Episode-level resampling（非 cluster/task-level），与 `unified_episode_bootstrap.py` 一致

## Llama-70B 数据就绪后的运行命令

```bash
cd /root/autodl-tmp/simgate-modular-routing
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

# 完整分析（B=10000）
python3 src/analyze_llama70b.py \
  --input_dir results/llama70b/ \
  --output_dir results/llama70b/ \
  --penalty 100 \
  --n_bootstrap 10000

# 带 cross-model 对比
python3 src/analyze_llama70b.py \
  --input_dir results/llama70b/ \
  --output_dir results/llama70b/ \
  --comparison_data results/cross_model_bootstrap_cis.json
```

输出文件:
- `results/llama70b/llama70b_analysis.json`
- `results/llama70b/llama70b_report.md`
