# Threecond R² 端到端数据验证报告

**日期**: 2026-05-28  
**验证目标**: 确认 `plot_action_r2_threecond.py` 中硬编码数据与原始 JSON 一致性

## 结论

**Plot 数据与原始 JSON 完全一致。** 全部 192 个硬编码值（3 条件 × 32 层 × mean/std）均为 `threecond_multiseed_v2.json` 中 float64 精度值的 4 位小数四舍五入，误差 ≤ 0.00005。

## 数据来源确认

| 属性 | 值 |
|---|---|
| **源文件** | `/root/autodl-tmp/vla-ssd/results/threecond_multiseed_v2.json` |
| **实验日志** | `/root/autodl-tmp/vla-ssd/results/threecond_multiseed_v2.log` |
| **Seeds** | [42, 123, 456]（3 seeds） |
| **Split** | sequential_80_20_no_shuffle |
| **R² space** | original_denormalized（原始动作空间） |
| **Readout** | image_mean |
| **层数** | L0–L32（plot 使用 L0–L31，忽略 L32 即 action head） |
| **条件** | untrained（随机初始化）, llama2base（语言预训练基座）, trained（VLA 微调后） |

JSON 中 stored mean/std 与从 raw per-seed 值重算结果完全一致（population std，非 sample std）。

## 之前"抽检偏移"的原因

之前抽检对比的是 **本地 artifact 文件**（15-seed 实验），而非 v2 JSON（3-seed 实验）。两者同属一个实验管线（同 split、同 r2_space、同 readout），但种子集不同导致 sample mean 自然差异：

| 条件 | 3-seed vs 15-seed MAD | 说明 |
|---|---|---|
| trained | 0.0117 | 较小差异，trained 模型稳定 |
| llama2base | 0.0084 | 较小差异 |
| untrained | 0.1208 | 较大差异，随机初始化方差极高（部分层 std > 0.3） |

这不是数据错误，是 **种子数量差异** 的统计效应。

## 排除的数据源

| 文件 | 为什么不是 plot 数据源 |
|---|---|
| `bootstrap_v3/openvla_goal/trained.json` | 完全不同的实验（bootstrap delta 分析，R² 值在 0.2–0.4），MAD=0.2662 |
| `threecond_multiseed.json` (v1) | 无 split/r2_space 元数据，值在 ~0.5 范围（可能是 z-normalized R²），MAD=0.0914 |
| `three_condition_comparison.json` | 单 seed (42)，无 std，MAD=0.0243 |
| `openvla_r2_per_layer.json` (local artifact) | 15-seed 实验，不同 sample mean |
| `r2_probe_15seeds.json` | 同上，15-seed 源数据 |

## 逐层比对摘要

验证脚本检查了全部 96 层 × 2 值 = 192 个数据点：

```
Total values checked: 96 layers x 2 (mean+std) = 192 values
Mismatches (diff > 0.0001 after 4-decimal rounding): 0

*** ALL VALUES MATCH ***
```

## 数据文件索引

| 路径 | 内容 | Seeds |
|---|---|---|
| `results/threecond_multiseed_v2.json` | **plot 数据源**，3-seed R² mean/std | 42,123,456 |
| `results/threecond_multiseed.json` | v1 版本（可能 z-normalized） | 42,123,456 |
| `results/llama2base_action_probe/three_condition_comparison.json` | 单 seed 三条件对比 | 42 |
| `results/functional_validation/r2_probe_15seeds.json` | 15-seed 三条件数据 | 0–14 |
| `results/action_probe/llama2base_action_probe.json` | llama2base 单 seed 详细结果 | 42 |
| `results/bootstrap_v3/openvla_goal/` | bootstrap delta 分析 | N/A |
| `artifacts/_project/data/openvla_r2_per_layer.json` | 15-seed trained（local artifact） | 0–14 |
| `artifacts/_project/data/openvla_untrained_r2_per_layer.json` | 15-seed untrained（local artifact） | 0–14 |
