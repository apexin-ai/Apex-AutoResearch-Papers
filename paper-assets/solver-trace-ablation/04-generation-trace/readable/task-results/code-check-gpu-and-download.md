# code check gpu and download

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_check-gpu-and-download_20260516T024803_result.json`
- **Structured JSON:** [`bb51f014c2f14a55af5c.json`](../../sessions/bb/bb51f014c2f14a55af5c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### 1. GPU 实况

| GPU | 型号 | 显存占用 | 显存总量 | 利用率 |
|-----|------|----------|----------|--------|
| 0 | RTX PRO 6000 Blackwell | 79,547 MiB | 97,887 MiB | 91% |
| 1 | RTX PRO 6000 Blackwell | 79,167 MiB | 97,887 MiB | 84% |

两卡均重度占用，符合预期（两个训练各占一卡）。

### 2. 训练进程状态

两个进程都 **存活运行中**，运行时间约 6h58m：

| 实验 | PID | 状态 | 运行时间 | GPU |
|------|-----|------|----------|-----|
| sweep-isr-b01-s45 | 589918 | Rl (running) | 06:56 | 0 |
| sweep-isr-b005-s42 | 589836 | Rl (running) | 06:58 | 1 |

（tmux ls 被 read-only 白名单拦截，但 ps 确认进程正常。）

### 3. 训练进度

| 实验 | 当前 step | reward_log 行数 | 最新 prove_rate | 最新 isr_mean | 最后日志时间 |
|------|-----------|-----------------|-----------------|---------------|-------------|
| sweep-isr-b01-s45 | **40** | 39 行 | 25.0% | 9.5% | 02:48:36 UTC |
| sweep-isr-b005-s42 | **50** | 49 行 | **0.0%** | 0.0% | 02:48:37 UTC |

**注意**：两个实验最后日志都停在 ~02:48 UTC（约 8 小时前），但进程仍在运行、GPU 利用率 84-91%。可能在做 checkpoint save 或 eval，也可能 reward_log 写入有延迟。b005-s42 从 step 50 开始 prove_rate=0 + loss=0，可能已 collapse。

### 4. Qwen3-8B 下载

**已完成**。PID 588329 已退出，日志显示 `Download model 'Qwen/Qwen3-8B' successfully.`。模型大小 **16GB**，位于 `/root/autodl-tmp/models/Qwen3-8B/`。

### 5. 磁盘空间

| 挂载点 | 总量 | 已用 | 可用 | 使用率 |
|--------|------|------|------|--------|
| /root/autodl-tmp | 250G | 197G | **54G** | 79% |

79% 使用率，剩余 54G。两个训练开始保存 checkpoint 后会快速消耗（每个 ~16GB），需关注。

### 关键风险

1. **sweep-isr-b005-s42 疑似 collapse**：step 50 时 prove_rate=0, isr_mean=0, loss=0，β=0.05 可能太小导致策略崩溃。
2. **reward_log 8 小时无更新但进程仍活**：需进一步查 stdout/stderr 确认是否卡死。
3. **磁盘**：54G 余量，两实验如果同时 save checkpoint（各 ~16G）会降到 ~22G，还算安全但无太多余量。

---
