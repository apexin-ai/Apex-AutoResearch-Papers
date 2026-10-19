# 诊断报告: eval_a3_v11_object

## 结论: Cron 误报，Eval 已正常完成

Eval 于 2026-05-22 21:07 启动，22:00 正常结束，运行约 53 分钟。4 个 task × 50 episodes = 200 episodes 全部完成。无 traceback/error/exception。Cron 报 "no valid W&B metrics" 是因为 eval 实验不上报 W&B，属于已知误报模式。

## 指标汇总

| Task | Task Name | TSR | CAR | Avg Max Displacement |
|------|-----------|-----|-----|---------------------|
| 0 | pick_up_the_orange_juice_and_place_it_in_the_basket | 0.0% (0/50) | 84.0% (42/50) | 0.0149m |
| 1 | pick_up_the_chocolate_pudding_and_place_it_in_the_basket | 0.0% (0/50) | 48.0% (24/50) | 0.0388m |
| 2 | pick_up_the_milk_and_place_it_in_the_basket | 0.0% (0/50) | 82.0% (41/50) | 0.0079m |
| 3 | pick_up_the_bbq_sauce_and_place_it_in_the_basket | 0.0% (0/50) | 84.0% (42/50) | 0.0041m |
| **Avg** | | **0.0%** | **74.5%** | — |

## 关键观察

- **TSR = 0%**: 所有 200 episodes 均未完成任务目标（success=false），机械臂没有成功抓取并放置任何物体
- **CAR 尚可 (74.5%)**: 避碰效果还行，但 task 1 (chocolate pudding) CAR 仅 48%，明显低于其他 task
- **refine_count 全部为 0**: SDF refinement 从未触发，说明 SDF min 值始终高于 refine_margin (0.01)，A3 的 gradient refinement 在推理时未实际生效
- **大部分 episode max_displacement 接近 0**: 很多 episode 的 displacement 在 1e-6 ~ 1e-10 量级，说明机械臂几乎没有移动（卡在原地不动）

## 结果文件路径

`/root/autodl-tmp/eval_results/v11_eval_safelibero_object_all_levelII_best_a3_seed0.json`
