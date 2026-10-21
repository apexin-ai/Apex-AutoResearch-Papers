# code plan006 training prep

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan006-training-prep_20260514T233036_result.json`
- **Structured JSON:** [`cdc0145fb9d4ef76d45d.json`](../../sessions/cd/cdc0145fb9d4ef76d45d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 成功，所有模块正常。以下是完整结果。

---

## 任务 1: 训练命令

`iterative_train.py` 参数确认：
- `--synthetic_ratio 1.0` ✓ (default)
- `--num_generations 20` ✓ (需要覆盖 default=10)
- `--seed` ✓
- `--steps_per_gen 10000` (匹配 MVP，代码 default 是 5000)
- `--max_lag` 不在训练脚本中，仅分析侧参数
- 输出目录使用 `results/extended_20gen/s{seed}/`（匹配 `analyze_extended.py` 默认输入路径）
- 不加 `--accumulate`（与 MVP 一致）

**Seed 42 训练命令：**
```bash
cd /root/autodl-tmp/distrib_canary_collapse && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python iterative_train.py \
    --data_dir data/wikitext103 \
    --output_dir results/extended_20gen/s42 \
    --seed 42 \
    --synthetic_ratio 1.0 \
    --num_generations 20 \
    --steps_per_gen 10000
```

**Seed 43 训练命令：**
```bash
cd /root/autodl-tmp/distrib_canary_collapse && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python iterative_train.py \
    --data_dir data/wikitext103 \
    --output_dir results/extended_20gen/s43 \
    --seed 43 \
    --synthetic_ratio 1.0 \
    --num_generations 20 \
    --steps_per_gen 10000
```

---

## 任务 2: 分析脚本验证 Checklist

| 模块 | 状态 | 说明 |
|------|------|------|
| Full cross-correlation (max_lag=10) | ✅ | raw + first-diff，含 permutation p-value (N=5000) |
| 差分 permutation Granger | ✅ | `difference=True`，BH FDR 校正 |
| Rolling window (gen 5→end) | ✅ | `window_analysis(metrics, 5, last_gen)` |
| TY supplementary | ✅ | d_max=0, 1, adaptive 三组，BH FDR |
| MVP comparison | ✅ | lag 稳定性 + power gain 判断 |
| **ECE→distinct_2/3 TY** | ✅ | CANARY=["token_entropy","ece"] × DOWNSTREAM=["distinct_1","distinct_2","distinct_3","perplexity"]，24 组 TY 测试全覆盖 |

**路径映射：**
- 训练输出：`results/extended_20gen/s{seed}/all_metrics.json`
- 分析输入：`--results_dir results/extended_20gen`（默认值，完全匹配）
- 分析输出：`results/extended_20gen/analysis/{extended_analysis.json, summary.txt, mvp_comparison.json}`
- MVP 对比基准：`results/mvp/rep_{seed}/all_metrics.json`（seed 42, 43 均可用）

**Dry-run 结果：** 两个 seed 均跑通，3 个输出文件正确生成。summary.txt 包含 TY SUPPLEMENTARY 表，ECE→distinct_2/3 行完整。

---

## 任务 3: 代码修改

**无需任何代码修改。** 训练和分析脚本均支持 plan_006 参数配置，路径匹配，模块完备。

---
