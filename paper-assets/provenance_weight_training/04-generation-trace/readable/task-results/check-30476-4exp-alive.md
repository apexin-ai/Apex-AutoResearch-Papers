# check 30476 4exp alive

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_30476_4exp_alive_20260517T134545_result.json`
- **Structured JSON:** [`3e46c92011e54a4d5b58.json`](../../sessions/3e/3e46c92011e54a4d5b58.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

四实验状态汇总：

**进程存活：4/4 全部存活**

| 实验 | PID | 当前 Step | 总 Steps | 进度 | 已运行 |
|------|-----|-----------|----------|------|--------|
| random_reweight_seed123 | 20073 | 1282 | 6103 | 21% | 46 min |
| bs8_auto_nmin_seed42 | 22466 | 99 | 6103 | 2% | 3 min 36 sec |
| batch_adaptive_tau_rho06_seed42 | 22904 | 99 | 6103 | 2% | 3 min 26 sec |
| rho02_adaptive_tau09_seed42 | 22095 | 99 | 6103 | 2% | 3 min 44 sec |

**GPU 占用：** 4 卡全满载（94-99% utilization），GPU0/2/3 用 46.5 GiB，GPU1 用 81.7 GiB（bs8 的 batch size 更大）

**系统内存：** 83 GiB / 1.0 TiB 已用，剩余 908 GiB 可用，水位很低，无压力

random_reweight 比其他三个早提交约 42 分钟，进度领先较多。其余三个几乎同时启动，当前都在 step 99 左右。按 ~2.2s/step 估算，每个实验总耗时约 3.7 小时。

---
