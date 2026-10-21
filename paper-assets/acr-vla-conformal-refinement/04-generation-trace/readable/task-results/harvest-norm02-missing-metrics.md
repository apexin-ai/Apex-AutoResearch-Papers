# harvest norm02 missing metrics

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_norm02-missing-metrics_20260521T045202_result.json`
- **Structured JSON:** [`b1119ecc999d12034e01.json`](../../sessions/b1/b1119ecc999d12034e01.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 11 个 JSON 找到并验证完毕。**所有 11 个实验的 metrics 已经存在于 registry 中，且与服务器上的 JSON 文件完全一致，无需更新。**

## 收割结果

| exp_id | server (JSON) | JSON found? | SR | registry updated? |
|--------|--------------|-------------|-----|-------------------|
| eval-obs-only-object-norm02-seed43-r2 | bjb1-32546 | ✓ | 0.16 | 已有，无需更新 |
| eval-obs-only-object-norm02-seed43-r3 | bjb1-32546 | ✓ | 0.16 | 已有，无需更新 |
| eval-obs-only-object-norm02-seed44-r2 | bjb1-18228 | ✓ | 0.16 | 已有，无需更新 |
| eval-obs-only-object-norm02-seed45 | bjb1-32546 | ✓ | 0.16 | 已有，无需更新 |
| eval-obs-only-object-norm02-seed46 | bjb1-18228 | ✓ | 0.15 | 已有，无需更新 |
| eval-obs-only-object-norm02-seed47 | bjb1-32546 | ✓ | 0.20 | 已有，无需更新 |
| eval-obs-only-object-norm02-seed48-r2 | bjb1-18228 | ✓ | 0.18 | 已有，无需更新 |
| eval-obs-only-object-norm02-seed50 | bjb1-32546 | ✓ | 0.18 | 已有，无需更新 |
| eval-obs-only-object-norm02-seed51 | bjb1-32546 | ✓ | 0.17 | 已有，无需更新 |
| eval-obs-only-object-norm02-seed52 | bjb1-32546 | ✓ | 0.15 | 已有，无需更新 |
| eval-obs-only-object-norm02-seed53 | bjb2-28827 | ✓ | 0.16 | 已有，无需更新 |

## 汇总

合并已有 seed42=0.20, seed49=0.14，共 13 个数据点：

```
0.14, 0.15, 0.15, 0.16, 0.16, 0.16, 0.16, 0.16, 0.17, 0.18, 0.18, 0.20, 0.20
```

ε=0.2 完整数据: **n=13, mean=16.7%, std=1.8%**

注：seed43 有 r2(0.16) 和 r3(0.16) 两个重复 run。若按 unique seed 去重（取最新 r3），则 n=12 个独立 seed，统计量基本不变。

---
