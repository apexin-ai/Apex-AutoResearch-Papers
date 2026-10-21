# ssh monitor all running

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_monitor-all-running_20260514T212347_result.json`
- **Structured JSON:** [`e2cfab8138b572b30495.json`](../../sessions/e2/e2cfab8138b572b30495.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

r2 的 log 里没有 metric 输出（可能 TRL 只发到 wandb 而服务器 wandb 未登录）。以下是汇总：

---

## 实验状态汇总

### 1. mvp2_eval_lr5e6_r1_ckpt20 (PID 96500, cuda:1)
| 项目 | 值 |
|------|-----|
| 进度 | **4/62 batches (6.5%)** |
| 速度 | ~162s/batch |
| 已运行 | ~1h01m |
| 预计剩余 | **~2h37m** (ETA ~07:10 UTC) |
| 状态 | 正常运行，无异常 |

### 2. mvp2_grpo_ced_lr5e6_r1 (PID 90080, cuda:0)
| 项目 | 值 |
|------|-----|
| 进度 | **55/200 steps (27.5%)** |
| 速度 | ~114s/step |
| 已运行 | ~1h44m |
| 预计剩余 | **~4h35m** (ETA ~10:17 UTC) |

**最新指标（~step 44）：**
| 指标 | 值 | 趋势 |
|------|-----|------|
| reward | 0.318 | ↑ (从 0.087 上升) |
| f1_reward | 0.038 | ↑ |
| ced_reward | 0.079 | ↑ |
| format_reward | 0.201 | ↑ |
| frac_zero_std | 0.3 | ⚠️ 上升中（step 5-35 约 0.1-0.2） |
| loss | 0.023 | 正常（中间有一次 spike 到 988B） |
| grad_norm | 0.14 | 稳定 |

**异常信号：**
- ⚠️ **KL 极度不稳定**：从 0.006 到 70 万亿级别剧烈波动。step 5 出现 2.4B spike。目前 kl_coef=0.01 可能压不住。
- ⚠️ **loss 曾出现一次 988B spike**（紧接着恢复到 0.05），对应 KL 同步 spike。
- frac_zero_std=0.3 尚在可接受范围，但需关注是否继续上升（>0.5 为 mode collapse 信号）。
- reward 持续上升是好信号。

### 3. mvp2_grpo_ced_lr5e6_rp_r2 (PID 94758, cuda:3)
| 项目 | 值 |
|------|-----|
| 进度 | **36/200 steps (18%)** |
| 速度 | ~115s/step（从初始 166s 加速中） |
| 已运行 | ~1h19m |
| 预计剩余 | **~5h14m** (ETA ~10:39 UTC) |

**指标：** log 文件中无 metric 输出，wandb 服务器端未登录无法查询。

**异常信号：**
- ⚠️ **KL 反复 spike**：step 5 (39B), step 10 (69K), step 15 (1.87M), step 20 (1.42B) — 每 5 步 logging 时都有 KL 超阈值 warning。
- 与 r1 类似的 KL 不稳定模式。由于缺少 reward 数据，无法判断训练是否有效学习。

---

**总结：** 三个实验均在正常运行。eval 约 2.5h 后完成。两个 GRPO 训练都存在 **KL 剧烈波动**，这是主要风险点。r1 的 reward 在上升说明训练方向正确，但 frac_zero_std 从 0.1 升到 0.3 需要持续监控。r2 缺少 metric 数据，建议后续在服务器上 `wandb login` 或检查为何 metrics 未写入 log。

---
