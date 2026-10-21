# ops p0 m64 m96 fresh diagnosis

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_p0-m64-m96-fresh-diagnosis_20260520T045633_result.json`
- **Structured JSON:** [`6f5cc1f23d3c86027e0d.json`](../../sessions/6f/6f5cc1f23d3c86027e0d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 进程状态

| 任务 | GPU | PID | 当前 step | loss | sps | 状态 |
|------|-----|-----|-----------|------|-----|------|
| **m96** | GPU 2 | 68539 | 2000/100000 | 3.454 | 0.5 | **健康运行中** |
| **m64** | GPU 3 | 68852 | 2450/100000 | 3.003 | 0.6 | **健康运行中** |
| m128 | GPU 0 | 26118 | (未查) | — | — | 运行中 |

最新日志时间戳在 12:56 左右（当前时刻），持续产出 step。

### GPU 状态

| GPU | 显存占用 | 利用率 | 温度 | 功耗 |
|-----|---------|--------|------|------|
| 0 (m128) | 30.1G / 97.9G | 0% | 48°C | 119W |
| 1 | 空闲 | 0% | 32°C | 34W |
| 2 (m96) | 28.5G / 97.9G | **96%** | 50°C | 218W |
| 3 (m64) | 27.5G / 97.9G | 0%* | 45°C | 160W |

\* GPU 3 利用率 0% 是 nvidia-smi 采样瞬间值，进程实际在跑（sps=0.6 稳定输出），正常。

### 训练趋势

- **m96**: loss 从 18.6 → 3.45（step 2000），lr 已达峰值 1e-4，grad norm 从 825 → 1.46，收敛正常
- **m64**: loss 从 16.2 → 3.00（step 2450），grad norm 0.89-1.46，收敛更快（M 更小 → 更快/step 也更小模型）

### 无异常

- 无 OOM 迹象（显存占用稳定，进程未重启）
- 无进程崩溃（dmesg 被 read-only 拒绝，但从 ps/GPU 看无异常）

### 结论

**两个进程完全健康。** m96 在 step 2000，m64 在 step 2450，按当前速度 m64 约 ~43h 跑完 100k steps，m96 约 ~53h。

---
