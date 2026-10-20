# 诊断报告：eval_openvla_random_k09_long_seed42_v3

**日期**: 2026-05-25 21:45 UTC
**服务器**: westd-38929
**日志路径**: `/root/autodl-tmp/logs/eval_openvla_random_k09_long_seed42_v3.log`（非 `~/runs/` 目录）

## 结论：实验已正常完成，CRON 误报

实验**未失败**。进程正常退出，因为它已跑完全部 10 tasks × 50 episodes = 500 episodes。

CRON 报 "Process exited without valid W&B metrics" 是因为该 eval 脚本不写 W&B，结果保存为 JSON 文件。进程退出码 0（正常退出），但 CRON 监控找不到 W&B metrics 所以报警。

## random_k09 实验结果

- **Overall SR: 46.80% (234/500)**
- **耗时**: 523.7 min
- **结果文件**: `/root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_random_prune_k09_10.json`

各 task 成绩：
| Task | SR |
|------|-----|
| 1. put both the alphabet soup and the tomato sauce in the basket | 64.0% (32/50) |
| 2. put both the cream cheese box and the butter in the basket | 66.0% (33/50) |
| 3. turn on the stove and put the moka pot on it | 62.0% (31/50) |
| 4. put the black bowl in the bottom drawer of the cabinet and close it | 40.0% (20/50) |
| 5. put the white mug on the left plate and put the yellow and white mug on the right plate | 18.0% (9/50) |
| 6. pick up the book and place it in the back compartment of the caddy | 82.0% (41/50) |
| 7. put the white mug on the plate and put the chocolate pudding to the right of the plate | 32.0% (16/50) |
| 8. put both the alphabet soup and the cream cheese box in the basket | 62.0% (31/50) |
| 9. put both moka pots on the stove | 28.0% (14/50) |
| 10. put the yellow and white mug in the microwave and close it | 14.0% (7/50) |

## 其他 3 个 Long v3 实验状态

| 实验 | GPU | 状态 | 结果 |
|------|-----|------|------|
| eval_openvla_attn_k09_long_seed42_v3 | GPU 0 | **运行中** — Task 10/10, ~Ep 40/50 | 即将完成 |
| eval_openvla_attn_k085_long_seed42_v3 | GPU 1 | **已完成** | SR=45.80% (229/500), 511.2 min |
| eval_openvla_l2norm_k09_long_seed42_v3 | GPU 3 | **运行中** — Task 10/10, ~Ep 30/50 | 即将完成 |

## 服务器资源状态

- **GPU**: 4× NVIDIA RTX PRO 6000 Black (98GB)。GPU 0 和 GPU 3 各 ~16GB 被占用（运行中的实验），GPU 1 和 GPU 2 空闲
- **磁盘**: 根分区 29% (8.7G/30G)，数据盘 29% (241G/879G)，充足
- **进程**: 2 个 eval 进程仍在运行 (PID 2508 on GPU 0, PID 2944 on GPU 3)

## 是否需要重跑

**不需要。** 实验已正常完成，结果已保存。

## 注意事项

1. CRON 监控对 eval 实验应调整为检查 JSON 结果文件而非 W&B metrics
2. `eval_openvla_attn_k085_long_seed42_v3` 的结果保存为 `openvla_l2norm_prune_k085_10.json`——文件名中 mode 标记为 l2norm 而实际跑的是 attention_prune (k=0.85)，可能是脚本中结果文件命名的 bug
