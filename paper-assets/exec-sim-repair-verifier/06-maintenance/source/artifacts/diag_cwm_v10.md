# 诊断报告: repo-level-cwm-v10 训练失败

**时间**: 2026-05-13 ~14:23 (进程停止写日志)
**服务器**: seetacloud-westd-4x5090, GPU 2 (RTX 5090 32GB)
**PID**: 105205 (已死亡)

## 根因

**进程在 eval 阶段被杀（exit code 1），日志无 traceback——Python 异常输出因缓冲未刷入日志文件。** 不是 OOM（cgroup oom_kill=0，内存 44GB/360GB），不是磁盘满（数据盘 43%），dmesg 无相关记录。

训练实际已无意义：严重过拟合，best checkpoint 停在 step 400（epoch 0.18），之后 1300 步 eval_loss 持续恶化。

## 日志关键信息

- 日志末尾: eval 进度条停在 1281/9335（eval 阶段），无 error/traceback/exception
- `grep -e "Traceback" -e "Error" -e "Exception" cwm_v9_train.log` → 0 matches
- `cgroup memory.events`: `oom 0, oom_kill 0`
- 日志最后修改时间: 14:23

## 过拟合趋势

| Step | Epoch | train_loss | eval_loss |
|------|-------|-----------|-----------|
| 100  | 0.05  | 16.35     | 0.434     |
| 200  | 0.09  | 7.73      | 0.324     |
| 300  | 0.14  | 4.80      | 0.323     |
| **400** | **0.18** | **3.33** | **0.298 (BEST)** |
| 500  | 0.23  | 2.28      | 0.329 ↑   |
| 600  | 0.27  | 1.76      | 0.343 ↑   |
| 800  | 0.36  | 0.81      | 0.343     |
| 1000 | 0.45  | 0.41      | 0.341     |
| 1300 | 0.59  | 0.21      | 0.371     |
| 1500 | 0.68  | 0.13      | 0.373     |
| 1700 | 0.77  | 0.09      | 0.370     |

## 存活 Checkpoint

| Checkpoint | Step | Epoch | eval_loss | 状态 |
|-----------|------|-------|-----------|------|
| checkpoint-400 | 400 | 0.18 | 0.298 | ✅ BEST，完整（adapter 45MB + optimizer 90MB） |
| checkpoint-1600 | 1600 | 0.72 | 0.372 | ✅ 完整 |
| checkpoint-1700 | 1700 | 0.77 | 0.370 | ✅ 完整（最新 trainer_state） |

## 当前状态

GPU 2 上已有两个 eval 进程（PID 123230, 123610）在评估 checkpoint-400，运行中 accuracy ~70.6%（720/9784 samples）。

## 建议下一步

1. **不要重启训练**——过拟合严重，继续训练无益
2. **等当前 eval 完成**——checkpoint-400 正在评估，预计还需 ~2 小时
3. **下轮实验需解决过拟合**：加 dropout/weight decay、early stopping（patience=3~5）、数据增强、减小 LoRA rank、或增大训练集
