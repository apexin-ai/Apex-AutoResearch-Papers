# check d051 experiment progress

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_d051_experiment_progress_20260516T205108_result.json`
- **Structured JSON:** [`2131ddb007086229115f.json`](../../sessions/21/2131ddb007086229115f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## D051 Batch 2 实验状态

### 当前进度

| 任务 | 状态 | 备注 |
|------|------|------|
| FewRel n=25, seed=42 | ✅ 完成 | 03:03–03:54 (51 min) |
| Few-NERD n=25, seed=42 | 🔄 运行中 | count_22 batch 17/25 |
| FewRel n=25, seed=123 | ⏳ 未开始 | |
| FewRel n=25, seed=456 | ⏳ 未开始 | |
| Few-NERD n=25, seed=123 | ⏳ 未开始 | |
| Few-NERD n=25, seed=456 | ⏳ 未开始 | |

**GPU**: RTX PRO 6000 Black (98GB), VLLM 进程占用 89GB, 21% util — 正常推理中。

### Few-NERD seed=42 子进度

| Count Level | 状态 | 耗时 |
|-------------|------|------|
| count_12 | ✅ 完成 | 22 min |
| count_2 | ✅ 完成 | 15 min |
| count_22 | 🔄 batch 17/25 | ~18 min elapsed, ~7 min left |
| count_6 | ⏳ 待运行 | est. ~17 min |
| count_44 | ⏳ 待运行 | est. ~40 min |
| count_66 | ⏳ 待运行 | est. ~60 min |

### FewRel seed=42 结果 (已完成)

```
FewRel count curves (seed=42, n=25):
count=4:   mean=0.870, sd=0.068, n=25
count=8:   mean=0.805, sd=0.082, n=25
count=16:  mean=0.719, sd=0.063, n=25
count=32:  mean=0.652, sd=0.049, n=25
count=40:  mean=0.606, sd=0.042, n=25
count=64:  mean=0.539, sd=0.026, n=25
count=80:  mean=0.504, sd=0.000, n=25
```

符合预期的单调递减趋势。count=80 的 sd≈0 说明在全 pool 上模型基本退化到随机水平 (1/80=0.0125，但这里 0.504 说明是 binary/pairwise 分类 accuracy)。

### 时间估算

- Few-NERD s42 剩余: ~2 小时
- FewRel s123 + s456: ~1.7 小时
- Few-NERD s123 + s456: ~5.6 小时
- **总剩余: ~9–10 小时** (预计完成时间: 5/17 14:00–15:00)

---
