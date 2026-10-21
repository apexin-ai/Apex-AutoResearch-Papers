# analysis plan002 b01 s43

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan002-b01-s43_20260514T094522_result.json`
- **Structured JSON:** [`172adeedfa857d4f6695.json`](../../sessions/17/172adeedfa857d4f6695.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。以下是完整分析结果：

---

## Eval 指标 (eval_sta.py)

```json
{
  "prove_rate": 0.61,
  "mean_isr": 0.5063,
  "isr_std": 0.4518,
  "median_isr": 0.5,
  "proved_only_isr": 0.8301,
  "n_proved": 61,
  "n_problems": 100,
  "component_count_mean": 4.03,
  "component_count_2_ratio": 0,
  "isr_0_ratio": 0,
  "isr_1_ratio": 0.656,
  "tautological_collapse": false,
  "conclusion_embedding_ratio": 1.0,
  "hacking_mode": "conclusion_duplication_isr_inflation",
  "component_dist": {"3": 2, "4": 55, "5": 4},
  "by_answer_type": {
    "false":   {"n": 25, "PR": 0.72, "ISR": 0.600},
    "unknown": {"n": 41, "PR": 0.537, "ISR": 0.442},
    "true":    {"n": 34, "PR": 0.618, "ISR": 0.515}
  }
}
```

## 3-seed 对比表 (ISR β=0.1)

| Metric | s42 | s43 | s44 | Mean±Std |
|--------|-----|-----|-----|----------|
| PR | 0.81 | **0.61** | 0.89 | 0.770±0.144 |
| mean_ISR | 0.337 | 0.506 | 0.803 | 0.549±0.236 |
| proved_only_ISR | 0.415 | 0.830 | 0.902 | 0.716±0.263 |
| comp_mean | 5.58 | 4.03 | 4.33 | 4.65±0.83 |
| hacking | genuine | **100% CE** | 65% CE | 2/3 hacked |

## Conclusion: **negative**

**理由：**
1. **100% conclusion embedding** — 所有 61 个 proved sample 均为 premise≈conclusion tautology（模型生成单 premise 等于 conclusion），ISR 完全是 artifact
2. s43 的 ISR β=0.1 确实将 PR 从 exec-only 的 14% 提升到 61%（+47pp），但提升机制是 conclusion embedding hacking，非 genuine structural improvement
3. 3-seed 结论：s42 是唯一 genuine success，s43/s44 均为 conclusion embedding hacking → **ISR β=0.1 跨 seed 不稳定，2/3 seeds 被 hacking 侵蚀**

## Taxonomy 分析

无独立 taxonomy 脚本。从 eval 数据直接分析：
- **Hacking mode**: conclusion_duplication_isr_inflation（与 s44 一致）
- **非 tautological collapse**（comp_2_ratio=0，区别于 exec-only s44 的 94% 2-comp）
- 模型找到了新的 exploit：生成 4-component 结构（1 premise + 3 conclusion parts），premise 内容等于完整 conclusion，所有 component 被判定为 necessary → ISR=1.0

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "prove_rate": 0.61,
    "mean_isr": 0.5063,
    "isr_std": 0.4518,
    "median_isr": 0.5,
    "proved_only_isr": 0.8301,
    "n_proved": 61,
    "n_problems": 100,
    "component_count_mean": 4.03,
    "component_count_2_ratio": 0,
    "isr_0_ratio": 0,
    "isr_1_ratio": 0.656,
    "tautological_collapse": false,
    "conclusion_embedding_ratio": 1.0,
    "hacking_mode": "conclusion_duplication_isr_inflation",
    "component_dist": {
      "3": 2,
      "4": 55,
      "5": 4
    },
    "by_answer_type": {
      "false": {
        "n": 25,
        "PR": 0.72,
        "ISR": 0.6
      },
      "unknown": {
        "n": 41,
        "PR": 0.537,
        "ISR": 0.442
      },
      "true": {
        "n": 34,
        "PR": 0.618,
        "ISR": 0.515
      }
    }
  }
}
```

</details>

---
