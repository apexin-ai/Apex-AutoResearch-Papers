# ops wild data rf classify

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_wild_data_rf_classify_20260517T172513_result.json`
- **Structured JSON:** [`3fab61b381c79ca692f3.json`](../../sessions/3f/3fab61b381c79ca692f3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。

## Wild Data RF Depth 分布结果

**RF 配置**: 200 棵树, 20K 训练样本 (features_all.jsonl), seed=42, balanced class weight

### C4 (10K samples)
| Depth | Count | % |
|-------|-------|------|
| d0 (human) | 6,598 | 65.98% |
| d1 (1st gen) | 3,354 | 33.54% |
| d2 | 18 | 0.18% |
| d3 | 30 | 0.30% |
| **FPR** | | **34.02%** |

### FineWeb (10K samples)
| Depth | Count | % |
|-------|-------|------|
| d0 (human) | 8,285 | 82.85% |
| d1 (1st gen) | 1,708 | 17.08% |
| d2 | 4 | 0.04% |
| d3 | 3 | 0.03% |
| **FPR** | | **17.15%** |

### 关键观察
- C4 被 RF 分类为 d1+ 的比例（34%）远高于 FineWeb（17%）
- 几乎所有非 d0 预测集中在 d1，d2/d3 极少（<0.5%）
- 平均概率也反映这一趋势：C4 的 mean P(d0)=0.695 vs FineWeb 的 0.835

### 产出
- `results/wild_features/depth_distribution.json` (服务器)
- `results/wild_features/depth_comparison.png` (对比图)
- Registry: wild_data_features_001 → DONE, metrics 已更新
- Artifact: `art_20260517_f4eb78` 已注册

---
