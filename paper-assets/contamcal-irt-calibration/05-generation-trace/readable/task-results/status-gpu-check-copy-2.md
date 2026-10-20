# status gpu check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_status_gpu_check_20260514T123719_result.json`
- **Structured JSON:** [`4d856bcb1ebbb736774a.json`](../../sessions/4d/4d856bcb1ebbb736774a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

| GPU | PID | 实验 | 状态 | 运行时间 | GPU 利用率 | 显存 | 详情 |
|-----|-----|------|------|----------|-----------|------|------|
| 0 | 353390 | exp-002 signals 0.5B | **运行中** | 1h51m | 33% | 2.2/24.6G | 进度 5/9，**但 task 1-4 全部 FAIL**（见下） |
| 1 | ~~362352~~ → 365739 | 1.5B d000 para → **1.5B d005 aligned eval** | 362352 已结束，365739 **运行中** | 6m | 51% | 5.9/24.6G | d000 para_aligned 已完成（3个结果文件）；d005 aligned 刚开始 |
| 2 | 356787 | 0.5B d005 aligned eval | **运行中** | 1h22m | 37% | 3.7/24.6G | 输出目录仍为空，尚未产出结果 |
| 3 | 362942 | 3B d100 aligned eval | **运行中** | 31m | 77% | 9.0/24.6G | 输出目录仍为空 |
| 4 | 335351 | 3B d005 SFT | **运行中** | 3h27m | 81% | 21.8/24.6G | lora_adapter 目录为空，尚未保存 checkpoint；无 training.log |
| 5 | 342940 | 3B d000 aligned eval | **运行中** | 2h46m | 71% | 9.0/24.6G | 输出目录仍为空 |

**空闲 GPU：无**（6 卡全满）

---

### 关键问题

**exp-002 (GPU 0) — minkpp 信号计算全部失败：**
- Task 1-4 均报错 `TypeError: Got unsupported ScalarType BFloat16`，出在 `signal_minkpp.py:96` 的 `.cpu().numpy()` 调用
- embedding 信号正常产出（4 个 json 文件），minkpp 失败导致整个 task 标记为 FAIL
- selfcritique 因 task 级失败未执行到，**无法确认 batch_size=32 热修复是否生效**（日志中无 BATCH_SIZE 字样）
- 当前在 task 5/9，后续 task 会继续以相同方式失败

**修复建议：** `signal_minkpp.py:96` 需要在 `.numpy()` 前加 `.float()`：
```python
return token_log_probs[0].cpu().float().numpy()
```

**3B d005 SFT (GPU 4)：** 已跑 3.5 小时但 lora_adapter 为空且无 training.log，需确认是否正常（可能 epoch 未结束尚未保存）。

---
