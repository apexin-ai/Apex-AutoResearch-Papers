# ssh self eval sensitivity

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_self_eval_sensitivity_20260523T015037_result.json`
- **Structured JSON:** [`3f61e907f387dbb2027e.json`](../../sessions/3f/3f61e907f387dbb2027e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果如下：

```
Self-evaluation sensitivity check
============================================================
  Total observations:          6064
  Self-judging pairs removed:  99 (qwen2.5-72b: 42, llama-3.3-70b: 57)
  Remaining observations:      5965

  Raw average ranking (full):
    1. gpt-4o                    win_rate=0.863
    2. qwen2.5-72b               win_rate=0.818
    3. gpt-4o-mini               win_rate=0.807
    4. llama-3.3-70b             win_rate=0.721
    5. qwen3-8b                  win_rate=0.661
    6. gemma-2-9b                win_rate=0.509
    7. gpt-4-0613                win_rate=0.343
    8. gpt-3.5-turbo-0125        win_rate=0.177

  Raw average ranking (no-self):
    1. gpt-4o                    win_rate=0.863
    2. gpt-4o-mini               win_rate=0.807
    3. qwen2.5-72b               win_rate=0.807
    4. llama-3.3-70b             win_rate=0.703
    5. qwen3-8b                  win_rate=0.661
    6. gemma-2-9b                win_rate=0.509
    7. gpt-4-0613                win_rate=0.343
    8. gpt-3.5-turbo-0125        win_rate=0.177

  Kendall τ (full vs Arena):    0.786 (p=0.0055)
  Kendall τ (no-self vs Arena): 0.857 (p=0.0017)

  Conclusion: MOSTLY ROBUST
```

**关键发现：**

1. **Self-judging bias 明显存在**：Qwen2.5-72B 给自己的 win rate 是 **1.000**（42/42 全赢），而其他 judge 给它的是 0.807。LLaMA-3.3-70B 自评 win rate **0.912** vs 其他 judge 的 0.703。

2. **排名变化**：移除 self-judging 后，Qwen2.5-72B 从第 2 降到第 3（与 gpt-4o-mini 互换）。Win rate 从 0.818 降到 0.807，与 gpt-4o-mini 持平但因排序被反超。

3. **Kendall τ 反而提升**：0.786 → 0.857，说明移除 self-judging 后排名**更接近** Arena ground truth。这符合预期——self-judging 虚高了 Qwen2.5-72B 的排名。

4. **整体结论**：排名大体稳定（τ between full vs no-self = 0.929），仅 position 2-3 互换，top-1 和 bottom-4 不变。Self-judging 影响局部但不颠覆整体排名。

---
