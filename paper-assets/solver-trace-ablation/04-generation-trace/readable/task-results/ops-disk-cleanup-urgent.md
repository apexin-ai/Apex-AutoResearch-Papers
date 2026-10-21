# ops disk cleanup urgent

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_disk-cleanup-urgent_20260514T114149_result.json`
- **Structured JSON:** [`48c21422989c9e68cf48.json`](../../sessions/48/48c21422989c9e68cf48.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部任务完成。报告：

---

### 执行报告

**1. 磁盘清理：释放 ~90G**
- 清理前：142G/250G (57%)
- 清理后：52G/250G (21%)，199G 可用
- 清理目录：plan001_s42 (15G), plan002_s42 (16G), plan016_s42 (31G), plan018_s42 (31G)
- 保留的 eval JSON 已备份到 `/root/autodl-tmp/eval_results_backup/`
- plan006_prolog_exec_s42 (31G) 保留用于 eval，现已完成 eval，可考虑后续清理

**2. plan018-s44 (PID 564900)：存活**
- 进程正常运行中，使用 GPU 0

**3. plan006-prolog-exec-s42 eval 结果**

| 指标 | plan006-exec-s42 | plan006-sta-s42 (参考) |
|------|-------------------|----------------------|
| PR | **83%** | 50% |
| mean ISR | **0.031** | 0.5 |
| median ISR | 0.0 | — |
| max ISR | 0.2 | — |
| True 类 PR | 92.5% | — |
| False 类 PR | 72.4% | — |
| Unknown 类 PR | 80.6% | — |

Exec-only 模式 PR 远高于 STA 模式 (+33pp)，但 ISR 极低（0.031 vs 0.5），中位数为 0——模型学会生成可执行 Prolog 代码但不做 intermediate step reasoning。

**4. 异常**
- 无异常。plan006 eval 日志因 nohup 与先前 timed-out 运行共用文件导致 null bytes，不影响结果。

---
