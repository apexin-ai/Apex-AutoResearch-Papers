# Training Status Snapshot — 2026-05-14 16:00 CST

## 1. Qwen m2_full_qwen (cuda:0)

| 项目 | 值 |
|------|-----|
| PIDs | wrapper=73544 (14h21m), python=73558 (14h21m) |
| 任务 | random_s42, 3 epochs, ~4242 total steps (1414/epoch) |
| 当前 step | **不可观测** — 日志仅 3 行（tee + outer redirect 冲突导致输出丢失） |
| Checkpoint | best_by_val_loss + best_by_recall_at_1 保存于 05:49-05:50 |
| GPU | 100% util, 51.6/97.9 GB VRAM, 75°C, 564W |
| 预估进度 | 与 StarCoder 同架构同数据，估算 ~2700 steps (64%) |
| 预计完成 | ~00:00 May 15（粗估） |

**⚠️ 日志问题**：`run_m2_full_qwen.sh` 中 `tee log` 被外层 `> log 2>&1` 覆盖，训练正常但看不到 step/eval 输出。训练完成后建议修复脚本，确保后续 seed 日志可读。

## 2. StarCoder m2_full_starcoder (cuda:1)

| 项目 | 值 |
|------|-----|
| PIDs | wrapper=74122 (14h20m), python=76627 (13h30m) |
| 任务 | random_s42, 3 epochs, 4242 total steps (1414/epoch) |
| 当前 step | **2500 / 4242 (59%)**, Epoch 2 |
| 速度 | ~185 steps/hr |
| 预计完成 | ~01:30 May 15 |

### Eval 历史

| Step | val_loss | R@1 | R@5 | R@10 |
|------|----------|-----|-----|------|
| 1000 ⭐ | **0.6134** | **0.4537** | 0.9201 | 1.0 |
| 1500 | 0.6528 | 0.4490 | 0.9057 | 1.0 |
| 2000 | 0.6698 | 0.4456 | 0.9007 | 1.0 |

**⚠️ 过拟合趋势**：val_loss 和 R@1 均从 step 1000 后持续下降。training loss 已降到 0.03-0.08 但 val 指标恶化。early_stopping_patience=0（无早停）。最终应使用 step 1000 的 best checkpoint。

## 3. m1_reextract_v2 (CPU)

| 项目 | 值 |
|------|-----|
| 总实例 | 28,276 |
| CodeQL groups | 82 |
| 已完成 groups | **42 / 82 (51%)** |
| all.jsonl 行数 | **44,173** |
| 状态 | 活跃运行中（最新活动 16:01） |
| 当前处理 | pallets/click, iterative/dvc, pyutils/line_profiler, mozillazg/python-pinyin |
| 运行时长 | ~12h（03:59 起） |
| 预计完成 | ~04:00 May 15（按当前速率粗估） |

## 4. GPU 状态

| GPU | 型号 | 温度 | 功耗 | VRAM | 利用率 | 进程 |
|-----|------|------|------|------|--------|------|
| 0 | RTX PRO 6000 Black | 75°C | 564/600W | 51.6/97.9 GB | 100% | Qwen (73558) |
| 1 | RTX PRO 6000 Black | 75°C | 608/600W | 55.2/97.9 GB | 100% | StarCoder (76627) |

## 5. 磁盘

| 挂载点 | 总量 | 已用 | 剩余 | 使用率 |
|--------|------|------|------|--------|
| /root/autodl-tmp | 250G | 161G | 90G | 65% |
| /root | 30G | 9.1G | 21G | 31% |

## 需关注

1. **Qwen 日志不可读** — 训练在跑但无法监控进度。需修复脚本中的 tee/redirect 冲突
2. **StarCoder 过拟合** — 已过 best checkpoint (step 1000)，后续 epoch 是浪费但不影响最终结果（取 best checkpoint 即可）
3. **s42→s43 自动切换** — 两个模型都还在 s42，完成后需确认自动启动 s43
