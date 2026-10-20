# ops c2 qw n500 check

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_c2_qw_n500_check_20260514T153430_result.json`
- **Structured JSON:** [`3769941c08d6e70f9a88.json`](../../sessions/37/3769941c08d6e70f9a88.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. 重复进程
PID 132389 和 132392 **已不存在**，已被清理。它们只跑到 problem 1/500 就被 kill，s020 输出目录为空，**无数据损坏**。

### 2. 数据完整性
- `profiling_output_n500_bf16_qw_imp_s020/` 和 `profiling_output_n500_bf16_qw_rand_s020/` 均为空目录（无残留）
- s015 输出目录也暂时为空——脚本在内存中累积结果，全部 500 问题跑完后才写盘

### 3. 当前进度

| PID | 实验 | Screen | 进度 | 最新日志时间 |
|-----|------|--------|------|-------------|
| 131864 | qw_imp_s015 | c2_qw_gpu2 | **172/500** (34.4%) | 23:34:51 |
| 132002 | qw_rand_s015 | c2_qw_gpu3 | **177/500** (35.4%) | 23:34:39 |

其他运行中进程（同台服务器）：
- PID 130124/130263: DeepSeek s015 (imp/rand)，GPU 0/1
- PID 142708/142944: Llama c3 实验 s020，后台运行

### 4. GPU 使用

| GPU | 显存占用 | 利用率 |
|-----|---------|--------|
| 0 | 26.9 / 97.9 GB | 97% |
| 1 | 30.6 / 97.9 GB | 76% |
| 2 | 48.1 / 97.9 GB | 96% |
| 3 | 48.8 / 97.9 GB | 89% |

4 卡全部在用，GPU 2/3 被 Qwen 实验占用（~48GB 显存）。

### 5. 预计剩余时间
- 21:52 启动，23:34 已跑 ~102 分钟，完成 ~175/500
- 速率：~1.7 问题/分钟
- s015 剩余 ~325 问题 → **约 3 小时** → 预计 **02:45 左右完成**（5月15日）
- s015 完成后还有 s020/s030/s050 三轮，如果脚本自动链式执行，总共还需 **~12 小时**

---
