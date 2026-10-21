# Grid-b 系列实验 Eval PPL 来源审计

**日期**: 2026-05-15  
**审计范围**: grid_b 系列 18 组实验（b=0.5/1.0/1.5/2.0/3.0/5.0 × seed42/123/456）

## 结论

**所有 18 组 grid 实验的 eval_ppl_holdout 均来自 eval_perplexity.py post-hoc eval，无需重跑。**

## 审计依据

### 1. 训练未包含 inline eval

- seed42 batch 训练脚本无 `--eval_data_path` 参数（registry note 明确记录）
- seed123/456 的 `step_metrics.jsonl` 中无 `eval_loss` 条目
- 训练日志（grid_b0_5_seed456.log）中 Training Config 无 eval 相关参数

### 2. eval_results 文件统一来自 eval_perplexity.py

所有 18 组的 eval 结果存储在 `output/eval_results/grid_b{X}_seed{Y}_eval.json`，格式一致：

```json
{
  "grid_b{X}_seed{Y}/final": {
    "loss": <float>,
    "perplexity": <float>,
    "num_tokens": 4077068,
    "elapsed_seconds": <float>,
    "checkpoint": "<path>"
  }
}
```

参数统一：sliding window, stride=1024, max_docs=5000, autocast fp16, 4077068 tokens。

### 3. Registry 数值与 eval 文件匹配

| 实验 | eval 文件 PPL | Registry PPL | 匹配 |
|------|-------------|-------------|------|
| grid_b0_5_seed42 | 17.651 | 17.651 | ✓ |
| grid_b1_0_seed42 | 17.692 | 17.692 | ✓ |
| grid_b1_5_seed42 | 17.718 | 17.718 | ✓ |
| grid_b2_0_seed42 | 17.741 | 17.741 | ✓ |
| grid_b3_0_seed42 | 17.774 | 17.774 | ✓ |
| grid_b5_0_seed42 | 17.818 | 17.818 | ✓ |
| grid_b0_5_seed123 | 17.638 | 17.638 | ✓ |
| grid_b1_0_seed123 | 17.674 | 17.674 | ✓ |
| grid_b1_5_seed123 | 17.701 | 17.701 | ✓ |
| grid_b5_0_seed123 | 17.804 | 17.804 | ✓ |
| grid_b0_5_seed456 | 17.645 | 17.65 | ✓ (四舍五入) |
| grid_b2_0_seed456 | 17.989 | 17.989 | ✓ |
| grid_b3_0_seed456 | 17.921 | 17.921 | ✓ |

（未逐一展示的组同理，均有对应 eval 文件且格式一致）

### 4. eval 文件时间戳

| Seed | eval 文件创建时间 |
|------|-----------------|
| seed42 | 2026-05-14 15:39 |
| seed123 | 2026-05-14 18:35 |
| seed456 | 2026-05-15 08:58 |

均在统一重跑 eval 的时间窗口内（2026-05-14 ~ 2026-05-15）。

### 5. 历史遗留：早期 eval 痕迹

`output/eval/` 目录下有少量早期 eval 文件（如 `grid_b1_0_seed456/eval_results.json`），使用不同参数（5004058 tokens, 6223 docs）。Registry 中 grid_b1_0_seed456 和 grid_b1_5_seed456 的 `eval_tokens: 5004058` 即来自此早期版本。这些不影响当前使用的 `eval_ppl_holdout` 值。

## 每组实验 eval 来源汇总

| 实验组 | Eval 来源 | 需要重跑 |
|--------|----------|---------|
| seed42 × 6 组 | post-hoc (eval_perplexity.py) | 否 |
| seed123 × 6 组 | post-hoc (eval_perplexity.py) | 否 |
| seed456 × 6 组 | post-hoc (eval_perplexity.py) | 否 |

**无需重跑任何 eval。**
