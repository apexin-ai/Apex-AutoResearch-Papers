# 诊断报告：eval-crm-long-seed45

## 结论：监控误报，实验已成功完成

## 失败根因

**不是实验失败，是监控系统误报。** 实验正常完成并输出了完整结果，但 cron 监控在标准路径找不到日志和哨兵文件，触发了 "process dead 5× with no sentinel/W&B" 的自动判定。

具体原因：该实验未通过标准 job 提交系统启动，导致：
1. 日志写到了 `logs/eval_crm_long_seed45.log`（项目目录内），而非 `~/runs/acr-vla-conformal-refinement/eval-crm-long-seed45.log`
2. 未生成哨兵文件 `/tmp/agent-ml-exit/eval-crm-long-seed45.exit`
3. cron 在标准路径找不到两者 → 误判为失败

对比：同类实验 eval-crm-long-seed46 在 `~/runs/` 下有日志，说明 seed46 是通过标准系统提交的。

## 实验结果

实验已完整运行，输出文件：`logs/eval_long_obs_only_norm02_seed45.json`（1783 bytes, May 20 05:58）

```
Overall success rate (crm_obs_only): 18.0% (18/100)
```

各任务明细：
| 任务 | 成功率 |
|------|--------|
| LIVING_ROOM_SCENE2 (alphabet_soup + tomato_sauce) | 0% |
| LIVING_ROOM_SCENE2 (cream_cheese + butter) | 0% |
| KITCHEN_SCENE3 (stove + moka_pot) | 80% |
| KITCHEN_SCENE4 (black_bowl + drawer) | 0% |
| LIVING_ROOM_SCENE5 (mugs on plates) | 30% |
| STUDY_SCENE1 (book in caddy) | 20% |
| LIVING_ROOM_SCENE6 (mug + pudding) | 10% |
| LIVING_ROOM_SCENE1 (alphabet_soup + cream_cheese) | 0% |
| KITCHEN_SCENE8 (two moka_pots) | 0% |
| KITCHEN_SCENE6 (mug in microwave) | 40% |

## 服务器状态

- GPU 3（实验使用的卡）：空闲，1MiB 显存占用，0% 利用率 — 进程已正常退出
- 磁盘：根分区 53%（16G/30G），数据盘 4%（16G/438G）— 无压力
- 无 OOM 或 GPU 错误迹象

## 是否需要重试

**不需要。** 实验已成功完成，结果完整。只需将该实验在监控系统中标记为已完成即可。

## 建议

如需避免此类误报，后续所有实验应通过标准 job 提交系统启动，确保日志和哨兵文件写入标准路径。
