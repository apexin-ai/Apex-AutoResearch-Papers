# diagnose three probe health check

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_three-probe-health-check_20260514T170334_result.json`
- **Structured JSON:** [`356b474f4563fefe53e8.json`](../../sessions/35/356b474f4563fefe53e8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 三路探测健康检查 (~17:05 UTC, 2026-05-14)

### ced_kl001_r4 (cuda:0)
- **进度**: step 64/100 (elapsed 1h30m)
- **最新指标** (step ~40, 后续指标在 stdout 缓冲中未 flush):

| 指标 | step ~5 | step ~25 | step ~30 | step ~35 | step ~40 |
|------|---------|----------|----------|----------|----------|
| KL | 0.014 | 0.181 | 0.115 | 0.125 | 0.098 |
| f1_reward | 0.015 | 0.028 | 0.089 | 0.082 | **0.240** |
| ced_reward | 0.026 | 0.015 | 0.058 | 0.120 | **0.236** |
| format_reward | 0.181 | 0.296 | 0.300 | 0.293 | 0.220 |
| reward_std | 0.176 | 0.186 | 0.280 | 0.370 | **0.617** |
| frac_zero_std | 0.3 | 0.7 | 0.6 | 0.4 | **0.0** |
| grad_norm | 0.222 | 0.457 | 0.357 | 0.242 | 0.158 |
| loss | 0.091 | -0.015 | -0.010 | -0.018 | 0.130 |

- **健康度**: ✅ **优秀**
  - KL 全程 <0.2，远低于 5 的警戒线
  - f1 和 ced 同步上升（0.015→0.240, 0.026→0.236），CED 确实在引导 faithfulness
  - frac_reward_zero_std 从 0.7 降到 0.0 — 所有 batch 都有 reward 方差，GRPO 在有效学习
  - reward_std 持续增长到 0.617 — 模型在产生有质量差异的生成
  - grad_norm 稳定 >0，无梯度消失
- **step_time**: ~97s/it（后半段因 completion 变长而增加）
- **预计完成**: ~18:03 UTC

---

### extract_r4 (cuda:2)
- **进度**: step 5/100 (elapsed ~8.5min)
- **指标**: 暂无 — 刚到 step 5，第一条 metric 在 stdout 缓冲中未 flush
- **step_time**: ~103s/it
- **健康度**: ⏳ **太早评估** — 进程正常运行中，step 时间合理
- **预计完成**: ~19:48 UTC

---

### flatnli_r5 (cuda:3)
- **进度**: step 112/200 (即第 12/100 个新 step, elapsed ~8min)
- **指标**: 暂无 — 理论上 step 105 和 110 应有日志，但 stdout block-buffered 未 flush 到 log 文件
- **step_time**: 从 ~30s 逐步增加到 ~35s/step（初期快是因为 resume warmup，预计会收敛到 ~80-100s/step）
- **健康度**: ⏳ **太早评估** — 进度条正常推进
- **预计完成**: tqdm 估计 ~31min 剩余 (~17:36 UTC)，但若 step time 收敛到 90s/step，实际可能 ~19:30 UTC

---

### 总结
- **ced_kl001_r4**: 运行最佳，f1 和 ced 同步上升、KL 极低、frac_zero_std=0 — 这是三路中最有信号的实验。预计 ~1h 内完成
- **extract_r4 / flatnli_r5**: 刚启动 8-9 分钟，尚无 metric 可评估。建议 **30-40 分钟后再查一次**，届时两者都应有至少 2-3 轮 metric 日志
- **无需干预**: 三个进程均在正常运行，无异常

---
