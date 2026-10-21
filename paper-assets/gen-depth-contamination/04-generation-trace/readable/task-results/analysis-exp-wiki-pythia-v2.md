# analysis exp wiki pythia v2

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_wiki_pythia_v2_20260517T131711_result.json`
- **Structured JSON:** [`444b67bde80ca5650ce1.json`](../../sessions/44/444b67bde80ca5650ce1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp_wiki_pythia_v2 分析结果

### 结论
- K* = 1
- conclusion = **negative**（假设 K*=2 未成立，Wikipedia + Pythia-1.4B 的 discrimination boundary 比预期更早收敛）

### 每层 discrimination accuracy
| Depth pair | AUC (mean) | Std | Folds |
|------------|-----------|-----|-------|
| 0v1 | 0.9750 | ±0.0023 | [0.9725, 0.9771, 0.9770, 0.9764, 0.9720] |
| 1v2 | 0.5846 | ±0.0043 | [0.5826, 0.5783, 0.5842, 0.5864, 0.5913] |
| 2v3 | 0.5445 | ±0.0068 | [0.5491, 0.5346, 0.5404, 0.5444, 0.5541] |
| 3v4 | 0.5205 | ±0.0062 | [0.5312, 0.5181, 0.5157, 0.5142, 0.5234] |
| 4v5 | 0.5168 | ±0.0124 | [0.5222, 0.5150, 0.5022, 0.5375, 0.5070] |

JSD:
| Depth pair | JSD |
|------------|-----|
| 0v1 | 0.080065 |
| 1v2 | 0.007773 |
| 2v3 | 0.006266 |
| 3v4 | 0.004836 |
| 4v5 | 0.004384 |

### 关键指标
- 总样本数: 5000 docs × 6 depths = 30,000 documents（全部完整生成）
- 训练/生成是否完整: 完整，EXIT_CODE=0
- 阈值 θ: 0.60（pipeline 内置）
- Ordinal classification: MAE=1.2589, Accuracy=0.3503
- 异常: **1v2 AUC = 0.5846 接近但未达 0.60 阈值**。Pythia-1.4B 在 Wikipedia 上的 depth-1 文本已经与 depth-2 高度相似，discrimination 几乎在第一跳就收敛。这与 C4 domain 的 K*=2 结果不同，说明 Wikipedia 的文体规律性可能使 Pythia 更快趋近 stationary distribution。

### Log 路径和 Checkpoint 路径
- log_path: `~/runs/gen-depth-contamination/exp_wiki_pythia_v2.log`
- results_path: `/root/autodl-tmp/gen-depth-contamination/results/exp_wiki_pythia_v2/`
- data_path: `/root/autodl-tmp/gen-depth-contamination/data/exp_wiki_pythia/`

---
