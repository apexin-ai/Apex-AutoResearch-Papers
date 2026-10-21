# research verify evi f1 joint code

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_verify-evi-f1-joint-code_20260515T132427_result.json`
- **Structured JSON:** [`f7afc17cc32c6e0c90b7.json`](../../sessions/f7/f7afc17cc32c6e0c90b7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成，汇报结果：

---

## Part 1: `compute_evi_f1_joint()` — ✅ 已部署

**代码位置**: `/root/autodl-tmp/freige/eval/evaluator.py:149`

**逻辑正确**：
- 构建 `pred_map`（所有 predicted triples）和 `gold_map`（所有 gold triples）
- 遍历所有 predicted triples 的 evidence，FP triple 的 evidence 与 gold 无交集 → 贡献 0 TP 但增加 `evi_pred_total`（precision 分母）
- `evi_gold_total` 统计所有 gold triples 的 evidence，FN triple 的 evidence 自然计入 recall 分母
- 符合 DREEAM 协议

**注意**: `evaluate()` 方法（L315）**没有**调用 `compute_evi_f1_joint`，只调了 `compute_f1` + `compute_evi_f1`（conditional）+ `compute_edcr`。如果需要在常规 evaluate pipeline 中自动包含 joint 指标，需要将其加入 `evaluate()`。

**重算结果已存在**: `/root/autodl-tmp/eval_results/evi_f1_joint_comparison.json`

| Experiment | Evi-F1 (cond) | Evi-F1 (joint) | Delta |
|---|---|---|---|
| SFT baseline | 0.7979 | 0.3117 | -0.4862 |
| RSFT r1 | 0.8187 | 0.3468 | -0.4719 |
| RSFT r2a | 0.8108 | 0.3509 | -0.4599 |
| RSFT r2b | 0.8128 | 0.3490 | -0.4638 |
| RSFT s44 | 0.8087 | 0.3713 | -0.4374 |

Joint 指标显著低于 conditional（~0.44-0.49 gap），符合预期——FP/FN penalties 拉低了分数。RSFT s44 的 joint 最高 (0.3713)。

---

## Part 2: `--scoring_mode flat_nli` — ✅ 已部署

**代码位置**: `rsft_score_filter.py:496-498`（argparse 定义，choices=["ced", "flat_nli"]）

**数据流**: `args.scoring_mode` → `score_all_records()` (L535) → `compute_ced_reward_for_record()` (L97) → L159 分支判断：
- `flat_nli` 模式调用 `ced_model.compute_flat_nli_reward(claim, cited_sents, tau=tau)`
- `ced` 模式走原 contrastive 逻辑

**`compute_flat_nli_reward` 实现** (`rewards/ced_reward.py:264`): 拼接 evidence 句子 → `nli_entailment_prob()` 获取 `p_pos` → `reward = p_pos * float(p_pos > tau)`。逻辑正确，使用纯 entailment probability 而非 contrastive margin。

**`--help` 未执行**（需要 `ssh_execute`），但代码结构完整：argparse 定义、参数传递链、实际计算逻辑均已到位，无缺失。

---

## 总结

两个实现均已成功部署且逻辑正确。唯一可改进点：`evaluate()` 方法未自动包含 `evi_f1_joint`，当前需单独调用。

---
