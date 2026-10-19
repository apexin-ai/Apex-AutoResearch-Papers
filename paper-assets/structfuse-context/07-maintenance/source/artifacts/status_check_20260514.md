# 服务器状态报告 — bjb1-42106
**时间**: 2026-05-15 02:10 CST

## GPU 状态

| GPU | 型号 | 利用率 | 显存占用 |
|-----|------|--------|----------|
| cuda:0 | RTX PRO 6000 Blackwell SE | 100% | 50641 / 97887 MiB |
| cuda:1 | RTX PRO 6000 Blackwell SE | 100% | 52287 / 97887 MiB |

## cuda:0 — m2_full_qwen (PID 504138)

- **当前 run**: random_s44 (2/9)
- **进度**: 刚启动（~9min），Epoch 1，1408 steps/epoch，尚无 step 输出
- **上一 run (s43)**: val_loss=0.5434, recall@1=0.5501, recall@5=0.9584, recall@10=1.0
- **s43 耗时**: ~6.5h（19:24→01:58）
- **剩余**: 8 runs（含当前）
- **预计完成**: ~52h → **约 5月17日 06:00 CST**

## cuda:1 — m2_full_starcoder (PID 519805)

- **当前 run**: random_s43 (1/8)
- **进度**: 刚启动（~5min），Epoch 1，1405 steps/epoch，尚无 step 输出
- **剩余**: 8 runs
- **预计完成**: 假设每 run ~6.5h → ~52h → **约 5月17日 06:00 CST**

## m1_reextract_v2

- **总量**: 82 groups / 28,276 instances
- **已完成**: 66/82 groups (80.5%)，已提取 20,615 instances
- **输出**: `all.jsonl` — 44,173 行
- **运行时间**: ~22h（05-14 03:59 起）
- **预计完成**: 剩余 16 groups，~5-6h → **约 5月15日 07:00-08:00 CST**

## tmux Sessions

| Session | 状态 |
|---------|------|
| m2_qwen_s43 | 活跃 — s43+ 队列脚本 |
| qwen_s42_watcher | 活跃 — 监控 Qwen 队列 |
| m2_full_starcoder | 活跃 — StarCoder 训练队列 |
| m1_reextract_v2 | 活跃 — M1 数据重提取 |
