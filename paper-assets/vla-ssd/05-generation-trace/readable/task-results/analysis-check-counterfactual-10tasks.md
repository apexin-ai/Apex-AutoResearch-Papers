# analysis check counterfactual 10tasks

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_check_counterfactual_10tasks_20260520T195619_result.json`
- **Structured JSON:** [`0a256db6d7ecb616b67e.json`](../../sessions/0a/0a256db6d7ecb616b67e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已完成。以下是 10-task counterfactual 实验汇总：

## 实验配置
- 10 tasks × 10 demos × 50 timesteps = 5000 samples/condition
- 4 counterfactual conditions: wrong, empty, shuffled, paraphrased
- Model: openvla-7b, seed 42

## Global Effect Ranking (by Cohen's d)

| Condition | Cohen's d | Paired MSE | Token Divergence | KL Divergence |
|-----------|-----------|------------|------------------|---------------|
| **empty** | **0.978** | 0.0691 | 91.3% | 8.81 |
| **wrong** | **0.924** | 0.0647 | 90.8% | 8.38 |
| **shuffled** | 0.763 | 0.0512 | 87.1% | 7.33 |
| **paraphrased** | 0.707 | 0.0462 | 83.0% | 6.46 |

## Cross-Task Variance

| Condition | Cohen's d (mean±std) | Range | CV |
|-----------|---------------------|-------|-----|
| empty | 0.989 ± 0.169 | [0.681, 1.245] | 0.171 |
| wrong | 0.949 ± 0.260 | [0.536, 1.505] | 0.274 |
| shuffled | 0.766 ± 0.142 | [0.458, 0.930] | 0.185 |
| paraphrased | 0.713 ± 0.211 | [0.411, 0.959] | 0.296 |

## Paraphrased Condition Per-Task Cohen's d

| Task | Cohen's d |
|------|-----------|
| push_plate_to_stove | 0.959 |
| put_wine_bottle_on_rack | 0.427 |
| put_wine_bottle_on_cabinet | 0.411 |
| open_middle_drawer | 0.444 |
| put_bowl_on_plate | 0.759 |
| put_bowl_on_stove | 0.856 |
| put_bowl_on_cabinet | 0.867 |
| put_cream_cheese_in_bowl | 0.921 |
| open_top_drawer_put_bowl | 0.713 |
| turn_on_stove | 0.778 |

## 关键发现

1. **Effect ordering 与 3-task 一致**: empty > wrong > shuffled > paraphrased
2. **所有 condition 全部显著** (p ≈ 0, 所有 Cohen's d > 0.7)
3. **Paraphrased condition 的 cross-task variance 最大** (CV=0.296)，说明语义敏感度因 task 而异——有些 task 对措辞改变几乎不敏感 (d≈0.41)，有些非常敏感 (d≈0.96)
4. **empty 最稳定** (CV=0.171)，符合预期——移除指令的效果不依赖具体 task 语义

结果文件路径：`/root/autodl-tmp/vla-ssd/results/counterfactual_10tasks/counterfactual_10tasks_combined.json`

---
