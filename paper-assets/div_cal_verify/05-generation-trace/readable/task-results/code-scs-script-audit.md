# code scs script audit

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_scs_script_audit_20260514T093910_result.json`
- **Structured JSON:** [`3b9386770d6cb7115aea.json`](../../sessions/3b/3b9386770d6cb7115aea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审查完成。以下是结果：

---

## SCS/Ratio 相关脚本审查报告

### 1. 脚本清单

| 脚本 | 功能 | 支持 355M 3-seed |
|------|------|------------------|
| `run_mvp.py` L283-302 | 训练时内联计算 `selection_rare_ngram_ratio`（选中/拒绝样本的 rare n-gram 均值比），保存到 `metrics.json` 和 `all_results.json` | **是**（参数化） |
| `analyze_355m_3seed.py` | 从 `all_results.json` 读取 ratio + ppl/rare/rankme/knn/corr，做 3-seed 摘要和 paired t-test | **是** |
| `run_3seed_stats.py` | GPT2-small (125M) phase2 的 3-seed 统计分析，路径硬编码为 `results_phase2*` | **否**（仅 125M） |
| `prepare_plot_data.py` | 硬编码数据输出 CSV，用于画图 | **否**（硬编码 125M 单 seed 数据） |
| `compute_diversity_metrics.py` | Self-BLEU/Distinct-n/TTR | 无关 SCS |
| `diversity_selection.py` | RGDS 选择逻辑（PCA + greedy submodular） | 运行时库，非分析脚本 |

### 2. 没有独立 SCS 脚本

项目中**不存在**名为 "Selection Consistency Score" 的独立指标或脚本。Director 任务中的 "SCS" 实际指的是 `selection_rare_ngram_ratio`（选中样本 rare n-gram 均值 / 拒绝样本 rare n-gram 均值）。这个值在 `run_mvp.py` 训练流程中**自动计算并保存**。

如果需要跨 generation 的选择一致性（Jaccard overlap），需注意：每代生成的 synthetic 数据池不同，`selected_indices.pt` 中的索引指向不同数据池，**无法直接计算 Jaccard**。

### 3. `analyze_355m_3seed.py` 兼容性

路径映射逻辑 (`get_result_dir`)：
- seed=42: `results_medium_{method}/{subdir}/`
- seed≠42: `results_medium_{method}_seed{seed}/{subdir}/`

**验证已有目录 vs 期望路径**：

| method | seed=42 | seed=123 | seed=456 |
|--------|---------|----------|----------|
| rgds | ✅ 已有 | ✅ 已有 | ❌ 缺失（`results_medium_rgds_seed456/` 不存在） |
| uncurated | ✅ | ✅ | ✅ 已有 |
| external | ✅ | ✅ | ✅ 已有（5/8 gen） |
| random50 | ✅ | ✅ | ❌ 缺失（`results_medium_random50_seed456/` 不存在） |

脚本本身**无需修改**，路径映射正确。缺失的是 seed=456 的 rgds 和 random50 实验数据。

### 4. seed=456 完成后一键出结果

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/div_cal_verify && python analyze_355m_3seed.py
```

输出：
- stdout: 3-seed summary table + paired t-test + claim verification
- `artifacts/355m_3seed_ttest.csv`
- `artifacts/355m_3seed_summary.csv`

### 5. 从已有结果提取 ratio 数据

ratio 存在每个实验的 `all_results.json` → `generations[i].selection_rare_ngram_ratio`。只有 RGDS 和 external_only 有 ratio 数据（uncurated 和 random_50 的 ratio 为 NaN，因为无选择/无 quality filter 诊断）。

示例提取命令：
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
python3 -c "
import json
for seed in [42, 123]:
    path = f'/root/autodl-tmp/div_cal_verify/results_medium_rgds{\"\" if seed==42 else f\"_seed{seed}\"}/rgds/all_results.json'
    with open(path) as f:
        data = json.loads(f.read().replace('NaN','null'))
    ratios = [(g['generation'], g.get('selection_rare_ngram_ratio')) for g in data['generations']]
    print(f'RGDS seed={seed}:', ' '.join(f'g{g}={r:.3f}' if r else f'g{g}=N/A' for g,r in ratios))
"
```

---
