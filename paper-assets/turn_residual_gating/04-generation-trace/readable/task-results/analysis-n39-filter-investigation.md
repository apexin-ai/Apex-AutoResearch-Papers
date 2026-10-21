# analysis n39 filter investigation

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_n39_filter_investigation_20260523T034904_result.json`
- **Structured JSON:** [`eda8a6c5c85e2923da90.json`](../../sessions/ed/eda8a6c5c85e2923da90.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收集完毕。以下是调查结果：

---

## 结论：N=39 的原因

**根因：eval_200.json 的 50 条对话中，有 11 条只有 2 个 turn，被 mid-GAR 计算逻辑排除。**

### 过滤逻辑

`eval_attention_steering.py` 第 466-470 行：

```python
# Per-conversation mid_gar: only convs with >= 3 turns
per_conv_mid_gar = []
for curve in beta_gar_curves:
    if len(curve) >= 3:
        per_conv_mid_gar.append(float(np.mean(curve[2:min(8, len(curve))])))
```

mid-GAR 定义为 `curve[2:]` 的均值（从第 3 轮开始），所以 2-turn 对话没有 mid-turn，被 `if len(curve) >= 3` 过滤掉。

`d048_final_ar_eval.sh` 第 7/7 步的 bootstrap 脚本也有等效过滤：`if len(c) > 2`。

### 2-turn 对话清单（11 条）

从日志中 base s42 的第一批 50 条：

| Conv # | turns | 被排除 |
|--------|-------|--------|
| 4 | 2 | ✓ |
| 6 | 2 | ✓ |
| 11 | 2 | ✓ |
| 14 | 2 | ✓ |
| 17 | 2 | ✓ |
| 20 | 2 | ✓ |
| 26 | 2 | ✓ |
| 31 | 2 | ✓ |
| 39 | 2 | ✓ |
| 41 | 2 | ✓ |
| 46 | 2 | ✓ |

50 - 11 = **39**，与日志输出 `(n=39/50)` 完全吻合。

### 额外发现：beta=5.0 时部分条件 n=38

| 条件 | beta=0.0 | beta=3.0 | beta=5.0 |
|------|----------|----------|----------|
| base | 39 | 39 | **38** |
| tg | 39 | 39 | **38** |
| ug | 39 | 39 | 39 |
| lo | 39 | 39 | **38** |
| pcgrad | 39 | 39 | 39 |
| ss | 39 | 39 | 39 |

base/tg/lo 在 beta=5.0 时 n=38——说明强 steering 下有 1 条原本 3-turn 的对话变成了 2-turn（模型在高 beta 下提前结束生成），进一步被过滤。

### 日志原文确认

```
Mid-GAR (per-conv): 0.7170 ± 0.0656  (n=39/50)
```

这是设计行为（非 bug）：2-turn 对话没有"中间轮次"可以计算 mid-GAR，排除是合理的。如果需要 N=50，需要从 eval_200.json 中筛选 ≥3 turn 的对话，或换一个 50 条全部 ≥3 turn 的子集。

---
