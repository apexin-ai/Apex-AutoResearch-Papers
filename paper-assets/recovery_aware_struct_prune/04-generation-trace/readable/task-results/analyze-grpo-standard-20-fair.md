# analyze grpo standard 20 fair

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_grpo_standard_20_fair_20260518T020344_result.json`
- **Structured JSON:** [`472eda518c3ab8490064.json`](../../sessions/47/472eda518c3ab8490064.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。

---

```
Conclusion: success
Standard collapse pattern: stagnation — reward flat 0.03-0.08 全程无上升趋势,
  frac_zero_std stuck 0.5-0.55, entropy 缓慢下降 0.16→0.14。
  Step 40 有微弱 peak (0.081) 后 step 50 dip 至 0.019, 此后再无恢复。
  完成示例显示大量 repetitive "#### number" 垃圾输出, reward 全 0.00。
4-way gradient: CKA-only (active recovery) > Random (plateau) > Standard (stagnation) > RASP (permanent collapse)
Key metrics at step 100: reward=0.054, frac_zero_std=0.55, entropy=0.14
D058 resolved: yes
```

**对比数据 (fair v5 config, step 100)**:

| Method | reward | frac_zero_std | pattern |
|--------|--------|---------------|---------|
| CKA-only | rising | declining | active recovery |
| Random | slowly rising | stable | plateau |
| **Standard** | **0.054** | **0.55** | **stagnation** |
| RASP | 0.01 | 0.85 | permanent collapse |

Standard 落在 Random 和 RASP 之间，符合 "partial collapse" 场景。Recovery capacity gradient 四点确认：剪枝方法对 RL 恢复能力的影响呈清晰梯度，CKA-only scoring 保留的结构最有利于 GRPO 恢复。

---
