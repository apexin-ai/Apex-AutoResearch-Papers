# diag exp 002 exit log

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_exp-002-exit-log_20260514T125803_result.json`
- **Structured JSON:** [`2078852556c5e6ca6e96.json`](../../sessions/20/2078852556c5e6ca6e96.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**退出原因：killed (SIGTERM)**

batch_report 记录 `Qwen2.5-0.5B_d005_s42/arc_challenge: FAIL (rc=-15)`，rc=-15 即 SIGTERM，进程被外部终止。

**运行情况：**

有两次运行记录：
- **第一次** (18:19–18:28)：日志 24 行，tasks 1–3 (d000) 均标记 FAIL，task 4 (d005/mmlu) 刚开始就中断
- **第二次** (20:55)：日志 12 行，task 1/9 刚开始就中断

**已完成 signal 文件：7 个（分布在 2 个 dosage 目录）**

| dosage | embedding | minkpp | selfcritique |
|--------|-----------|--------|-------------|
| d000/mmlu | ✓ 6MB | ✓ 2.1MB | ✗ |
| d000/gsm8k | ✓ 567K | ✓ 200K | ✗ |
| d000/arc_challenge | ✓ 515K | ✗ | ✗ |
| d005/mmlu | ✓ 6MB | ✗ | ✗ |
| d005/gsm8k | ✗ | ✗ | ✗ |
| d005/arc_challenge | ✗ | ✗ | ✗ |
| d100/* | 全部缺失 | | |

**0/9 tasks 完全完成**（每个 task 需 3 个 signal 全部成功才算 pass）。selfcritique signal 全部缺失——tasks 1–3 的 FAIL 很可能就是 selfcritique 子任务失败导致。

**第一个日志最后 10 行：**
```
2026-05-14 18:25:30,600 [ERROR] [2/9] FAIL: Qwen2.5-0.5B_d000_s42/gsm8k
stderr: ...zamba, zamba2, zoedepth

2026-05-14 18:25:30,600 [INFO] [3/9] Running: Qwen2.5-0.5B_d000_s42/arc_challenge (signals: ['embedding', 'minkpp', 'selfcritique'])
2026-05-14 18:28:25,117 [ERROR] [3/9] FAIL: Qwen2.5-0.5B_d000_s42/arc_challenge
stderr: ...zamba, zamba2, zoedepth

2026-05-14 18:28:25,118 [INFO] [4/9] Running: Qwen2.5-0.5B_d005_s42/mmlu (signals: ['embedding', 'minkpp', 'selfcritique'])
```

（stderr 截断显示的是 transformers 模型列表 warning，不是真正的错误信息。真正的失败原因被截断了。）

---
