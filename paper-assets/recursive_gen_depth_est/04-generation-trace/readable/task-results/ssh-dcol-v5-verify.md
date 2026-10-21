# ssh dcol v5 verify

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_dcol_v5_verify_20260515T024845_result.json`
- **Structured JSON:** [`fa5f5a2cedd82147755b.json`](../../sessions/fa/fa5f5a2cedd82147755b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已获取到 step 200，汇报如下：

---

## dcol_deberta_005 验证结果

**1. PID 存活** — PID 283191 运行中 ✓

**2. 显存占用** — cuda:1 占用 13,734 MiB（<15GB） ✓
- GPU 1 上有两个 python 进程：PID 278173 (9,026 MiB) + PID 283196 (4,694 MiB)

**3. margin_lr 确认** — 命令行参数 `--margin_lr 1e-4` ✓，日志显示 `'margin_lr': 0.0001` ✓

**4. 前 10 个 log points (step 20-200) loss 值：**

| Step | loss | ce | cl | acc | lr |
|------|------|------|------|------|------|
| 20 | 1.9047 | 1.3883 | 0.5164 | 25.47% | 3.05e-06 |
| 40 | 1.9053 | 1.3889 | 0.5163 | 24.92% | 6.10e-06 |
| 60 | 1.9053 | 1.3887 | 0.5165 | 25.10% | 9.15e-06 |
| 80 | 1.9049 | 1.3886 | 0.5164 | 25.08% | 1.22e-05 |
| 100 | 1.9046 | 1.3885 | 0.5161 | 25.03% | 1.52e-05 |
| 120 | 1.9046 | 1.3884 | 0.5161 | 24.87% | 1.83e-05 |
| 140 | 1.9044 | 1.3883 | 0.5161 | 25.13% | 2.13e-05 |
| 160 | 1.9043 | 1.3880 | 0.5163 | 25.23% | 2.44e-05 |
| 180 | 1.9040 | 1.3877 | 0.5163 | 25.43% | 2.74e-05 |
| 200 | 1.8963 | 1.3863 | 0.5100 | 26.44% | 3.05e-05 |

**状态：正常** — loss 无 NaN，acc 从 ~25% 随机基线起步（4分类），step 200 开始出现轻微下降趋势（loss 1.905→1.896，acc 25%→26.4%）。仍处于 warmup 阶段（lr 还在爬升中，warmup_ratio=0.05 对应约 197 steps，刚过 warmup）。

---
