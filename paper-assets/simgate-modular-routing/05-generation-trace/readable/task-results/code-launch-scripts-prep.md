# code launch scripts prep

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_launch-scripts-prep_20260513T234045_result.json`
- **Structured JSON:** [`644c3d23c9d02944874f.json`](../../sessions/64/644c3d23c9d02944874f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

**Part 1 - plan-002 验证**
- `death_aware_labeling.py` 生成 sft_triples.jsonl：63 episodes → 1814 steps（det:600, int:150, no-pref:1064）
- `router_sft_train.py --dry_run` 通过：episode-level split 生效（20 train / 5 val episodes），数据加载正常
- `scripts/launch_plan002.sh` 已创建，参数与 argparse 匹配（去掉了不存在的 `--eval_strategy` / `--metric_for_best_model`，这两个已硬编码）

**Part 2 - plan-004b 验证**
- `ablation_data_converter.py` 转换成功：1814 records，implicit_sft.jsonl 格式正确（chat messages + [SIMULATE] prefix）
- `scripts/launch_plan004b.sh` 已创建，使用正确参数名：`--input_path`/`--output_path`（converter）、`--data`（implicit_1_7b train）

**Part 3 - post_collection_analysis.sh**
- 已创建并验证通过
- 当前状态：plan_c 4/11 tasks 完成（64 episodes），加上 prescreening/mvp/research 共 30 tasks / 317 episodes
- 数据完整性检查：All episodes valid

三个脚本均在 `/root/autodl-tmp/simgate-modular-routing/scripts/`，已 `chmod +x`。

---
