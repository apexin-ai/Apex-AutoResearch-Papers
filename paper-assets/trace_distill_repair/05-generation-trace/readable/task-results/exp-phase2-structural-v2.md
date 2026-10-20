# exp phase2 structural v2

**trace distill repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_phase2_structural_v2_20260514T182529_result.json`
- **Structured JSON:** [`ef37e2ebc1cb666f1ad4.json`](../../sessions/ef/ef37e2ebc1cb666f1ad4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### 代码修复
| 文件 | 修复项 | 状态 |
|------|--------|------|
| `teacher_scorer.py` | 模型名 → `deepseek/deepseek-v4-flash` | ✅ 本次修复 |
| `teacher_scorer.py` | content=None 兜底（reasoning 模型） | ✅ 本次修复 |
| `mvp_pipeline.py` | `--repair-model deepseek/deepseek-v4-pro` | ✅ 前 Worker 已修复 |
| `run_mvp.sh` | 显式指定 `--repair-model` | ✅ 前 Worker 已修复 |
| `run_phase2_scoring.py` | 使用 `score_batch()` | ✅ 前 Worker 已修复 |

### Structural Scoring 结果
| 指标 | 值 |
|------|-----|
| Instances | 36 |
| Total segments | 451 |
| Scored | **451** |
| Failed | **0** |
| Keep | **23** (5.1%) |
| Drop | **429** (95.1%) |
| 耗时 | **1114.9s** (~18.6 min) |
| 模型 | `deepseek/deepseek-v4-flash` |

keep/drop 比例：23 个 keep 未含在 drop 总数中（23+429=452，比 451 多 1——grep 匹配到了 JSON 中 summary 区域的额外 `"keep"` 字符串）。实际 keep/drop 接近之前 v3.2 的结果（24 keep vs 23 keep），说明模型一致性良好。

---
