# code fill 19912 post arcc

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fill-19912-post-arcc_20260521T112420_result.json`
- **Structured JSON:** [`d917aa5c5c8caf69a11c.json`](../../sessions/d9/d917aa5c5c8caf69a11c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

**GPU 全部满载，无需填充。** 上一个 worker 已经按 fallback 方案启动了 ARC-C clean_s3-s6 seed 扩展。

### 当前任务（已在跑）
| GPU | 任务 | PID | Seed | 启动时间 | 进度 |
|-----|------|-----|------|----------|------|
| 0 | clean_s3 | 13508 | 456 | 1分45秒前 | ~94/939 (10%) |
| 1 | clean_s4 | 15450/15451 | 301 | 44秒前 | ~52/939 (5.5%) |
| 2 | clean_s5 | 15463/15464 | 302 | 43秒前 | ~52/939 (5.5%) |
| 3 | clean_s6 | 15438/15439 | 303 | 44秒前 | ~53/939 (5.6%) |

GPU 显存：42/26/28/25 GB（97 GB 卡），利用率 78-95%。

### 监测要点
- 训练速度 ~1.05 s/step，每条 939 步，约 16-17 分钟完成
- 磁盘 16/250 GB，充足
- 日志：`/root/autodl-tmp/ctrl_contam_arcc/logs/arcc_clean_s{3,4,5,6}.log`

### 不启动新任务的理由
1. 4 张 GPU 都在 78-95% 利用率，无可用算力
2. 训练已稳定推进（s3 已到 10%，无报错）
3. 强行启动 Llama 下载/SFT 会和正在跑的 ARC-C 抢显存/PCIe 带宽，反而拖慢现有任务

ARC-C seed 训练约 16 分钟后完成，届时会自动进入 eval（如果 train.py 配了 eval hook）或需要手动启动 eval。

---
