# ssh diagnose cuda1 speed

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_diagnose_cuda1_speed_20260515T132751_result.json`
- **Structured JSON:** [`ae30bb52527b0e234197.json`](../../sessions/ae/ae30bb52527b0e234197.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 主因：GPU 1 上有 3 个进程争抢资源

| PID | GPU | 显存 | 进程 |
|-----|-----|------|------|
| 106832 | GPU 0 (38:00.0) | 22,054 MiB | `deepseek_no_trace_seed42` 训练 |
| 107198 | GPU 1 (5A:00.0) | 22,414 MiB | `deepseek_exception_only_seed42` 训练 |
| 108843 | GPU 1 (5A:00.0) | 17,158 MiB | `evaluate.py` — vota checkpoint-148 eval |
| 109289 | GPU 1 (5A:00.0) | 17,158 MiB | `evaluate.py` — vota checkpoint-148 eval (重复) |

GPU 1 总占用 56,730 MiB / 97,887 MiB，三个进程争抢计算资源和显存带宽。exception_only 训练速度从 15s/it 恶化到 **35s/it**（step 63），正在持续下降。

### 次因：数据序列长度差异 ~2.9x

| 数据集 | 行数 | 文件大小 | 平均字符/样本 |
|--------|------|----------|--------------|
| no_trace_train | 4,720 | 2.7 MB | ~592 |
| exception_only_train | 4,720 | 7.7 MB | ~1,710 |

exception_only 每条样本约 2.9x 长，attention 计算量随序列长度超线性增长。即使没有 GPU 争抢，exception_only 也会比 no_trace 慢（预估 6-8 s/it vs 3 s/it）。

### 需要干预

**两个 vota eval 进程 (PID 108843, 109289)** 是主要瓶颈。它们在 GPU 1 上占了 34 GB 显存，且看起来是同一个 checkpoint 的重复 eval。建议 kill 掉它们，exception_only 训练速度应能从当前 35s/it 恢复到 ~7s/it。

是否执行 kill？

---
