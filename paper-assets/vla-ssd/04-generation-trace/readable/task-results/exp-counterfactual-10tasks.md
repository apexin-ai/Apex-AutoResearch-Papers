# exp counterfactual 10tasks

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_counterfactual_10tasks_20260520T184556_result.json`
- **Structured JSON:** [`3c8bd8d89394e81cef98.json`](../../sessions/3c/3c8bd8d89394e81cef98.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 0 已加载 ~15GB (openvla-7b bf16)，利用率 90%，正在处理中。Python 输出被 tee 缓冲，但实验在正常推进。

实验状态汇总：

- **实验**: `counterfactual_10tasks` — RUNNING on westd-19183, cuda:0
- **原有 3 tasks**: open_the_middle_drawer_of_the_cabinet, open_the_top_drawer_and_put_the_bowl_inside, push_the_plate_to_the_front_of_the_stove
- **新增 7 tasks**: put_the_bowl_on_the_plate, put_the_bowl_on_the_stove, put_the_bowl_on_top_of_the_cabinet, put_the_cream_cheese_in_the_bowl, put_the_wine_bottle_on_the_rack, put_the_wine_bottle_on_top_of_the_cabinet, turn_on_the_stove
- **4 conditions**: wrong, empty, shuffled, paraphrased (+ correct baseline)
- **规模**: 10 tasks × 10 demos × 50 timesteps = 5000 samples → 25000 forward passes
- **预估运行时间**: ~60-70 分钟
- **输出目录**: `/root/autodl-tmp/vla-ssd/results/counterfactual_10tasks/`
- **输出文件**: 
  - `counterfactual_{wrong,empty,shuffled,paraphrased}.json` (per-condition, with per-task breakdown)
  - `counterfactual_correct.json` (baseline)
  - `counterfactual_10tasks_combined.json` (combined summary + cross-task variance)
- **cross-task variance**: 每个 condition 报告 Cohen's d 的 mean ± std, min/max, CV across 10 tasks

---
