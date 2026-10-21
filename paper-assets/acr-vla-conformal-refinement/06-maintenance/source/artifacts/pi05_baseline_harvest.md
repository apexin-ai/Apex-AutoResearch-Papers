# ⚠️ DEPRECATED — 旧版评测代码数据（无 action chunking / n_action_steps=10）

> **此文件中的数据已废弃。** 来自旧版 evaluate.py（无 `n_action_steps=10` 参数），产出的 VLA-only SR（Object ~82%, Spatial ~84%）显著低于最终版评测。Table 3 使用的是 westd-paired 批次（2026-05-26，westd-49937 服务器），代码版本一致，内部对比公平。此文件仅作历史参考。

---

# π0.5 VLA-only Baseline Harvest (DEPRECATED)

提取自 6 个 `eval-pi05-vla-only-*` 日志（bjb1-32546，`/root/runs/acr-vla-conformal-refinement/`）。
所有日志末尾均为 `EXIT_CODE=0`，无 Error / Exception / Traceback。日志中未记录 W&B run ID（eval 脚本不接 W&B）。

每个实验 = 10 tasks × 20 rollouts = 200 trials。

## 1. 汇总：Overall Success Rate

| Benchmark | Seed | Successes / Trials | Overall SR |
|---|---|---|---|
| object  | 42 | 164/200 | **82.0%** |
| object  | 43 | 163/200 | **81.5%** |
| object  | 44 | 162/200 | **81.0%** |
| spatial | 42 | 169/200 | **84.5%** |
| spatial | 43 | 166/200 | **83.0%** |
| spatial | 45 | 170/200 | **85.0%** |

## 2. 3-seed 统计

| Benchmark | Seeds | Mean | Std (sample, n-1) | Std (pop, n) |
|---|---|---|---|---|
| object  | 42 / 43 / 44 | **81.50%** | ±0.50 | ±0.41 |
| spatial | 42 / 43 / 45 | **84.17%** | ±1.04 | ±0.85 |

## 3. Per-task 详情

### LIBERO-Object

| Task | seed42 | seed43 | seed44 | Mean |
|---|---|---|---|---|
| pick_up_the_alphabet_soup_and_place_it_in_the_basket     | 17/20 (85.0%) | 16/20 (80.0%) | 17/20 (85.0%) | 83.3% |
| pick_up_the_cream_cheese_and_place_it_in_the_basket      | 20/20 (100.0%) | 19/20 (95.0%) | 19/20 (95.0%) | 96.7% |
| pick_up_the_salad_dressing_and_place_it_in_the_basket    | 12/20 (60.0%) | 14/20 (70.0%) | 13/20 (65.0%) | 65.0% |
| pick_up_the_bbq_sauce_and_place_it_in_the_basket         | 16/20 (80.0%) | 17/20 (85.0%) | 16/20 (80.0%) | 81.7% |
| pick_up_the_ketchup_and_place_it_in_the_basket           | 16/20 (80.0%) | 16/20 (80.0%) | 17/20 (85.0%) | 81.7% |
| pick_up_the_tomato_sauce_and_place_it_in_the_basket      | 11/20 (55.0%) | 12/20 (60.0%) | 11/20 (55.0%) | 56.7% |
| pick_up_the_butter_and_place_it_in_the_basket            | 20/20 (100.0%) | 19/20 (95.0%) | 18/20 (90.0%) | 95.0% |
| pick_up_the_milk_and_place_it_in_the_basket              | 16/20 (80.0%) | 16/20 (80.0%) | 17/20 (85.0%) | 81.7% |
| pick_up_the_chocolate_pudding_and_place_it_in_the_basket | 20/20 (100.0%) | 20/20 (100.0%) | 20/20 (100.0%) | 100.0% |
| pick_up_the_orange_juice_and_place_it_in_the_basket      | 16/20 (80.0%) | 14/20 (70.0%) | 14/20 (70.0%) | 73.3% |
| **Total** | **164/200 (82.0%)** | **163/200 (81.5%)** | **162/200 (81.0%)** | **81.5%** |

难任务（mean < 70%）：`salad_dressing` 65.0%、`tomato_sauce` 56.7%。

### LIBERO-Spatial

| Task | seed42 | seed43 | seed45 | Mean |
|---|---|---|---|---|
| pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate | 19/20 (95.0%) | 19/20 (95.0%) | 19/20 (95.0%) | 95.0% |
| pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate               | 18/20 (90.0%) | 18/20 (90.0%) | 18/20 (90.0%) | 90.0% |
| pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate                 | 20/20 (100.0%) | 19/20 (95.0%) | 20/20 (100.0%) | 98.3% |
| pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate                 | 18/20 (90.0%) | 19/20 (95.0%) | 20/20 (100.0%) | 95.0% |
| pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate | 15/20 (75.0%) | 14/20 (70.0%) | 12/20 (60.0%) | 68.3% |
| pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate                    | 5/20 (25.0%) | 4/20 (20.0%) | 6/20 (30.0%) | 25.0% |
| pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate            | 20/20 (100.0%) | 20/20 (100.0%) | 20/20 (100.0%) | 100.0% |
| pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate                      | 18/20 (90.0%) | 19/20 (95.0%) | 20/20 (100.0%) | 95.0% |
| pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate                 | 18/20 (90.0%) | 17/20 (85.0%) | 18/20 (90.0%) | 88.3% |
| pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate             | 18/20 (90.0%) | 17/20 (85.0%) | 17/20 (85.0%) | 86.7% |
| **Total** | **169/200 (84.5%)** | **166/200 (83.0%)** | **170/200 (85.0%)** | **84.17%** |

难任务（mean < 70%）：`on_the_ramekin` **25.0%**（明显瓶颈，三 seed 均 ≤30%）、`top_drawer_of_wooden_cabinet` 68.3%。

## 4. 异常 / 备注

- 全部 6 个 run 均正常结束（`EXIT_CODE=0`），无 Python 异常。
- 模型加载阶段有 `WARNING:root:Vision embedding key might need handling: ...patch_embedding.bias/weight` 与 `Vision tower missing_keys (376)` 提示，但同时输出 `[pi05] Fixed 437 vision tower keys` 与 `All keys loaded successfully!`，属预期加载日志（所有 6 个 run 一致），不影响推理。
- 评测配置（全部 6 个）：`mode=vla_only`, `model=pi05`, `n_rollouts=20`, `max_steps=300`, `K=1`, `conformal_threshold=0.074855`，PI05 checkpoint `/root/autodl-tmp/models/pi05_libero_finetuned/`。
- 日志中未出现 wandb / run_id 字段（eval 脚本无 W&B 接入）。
