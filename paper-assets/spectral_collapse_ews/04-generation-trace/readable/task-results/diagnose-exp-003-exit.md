# diagnose exp 003 exit

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_003_exit_20260517T124757_result.json`
- **Structured JSON:** [`22fa283069d71ff364dc.json`](../../sessions/22/22fa283069d71ff364dc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**exp_003 并未被成功 kill。**

| 检查项 | 结果 |
|--------|------|
| PID 88156 | **已死**（`/proc/88156` 不存在） |
| PID 88161 (子进程) | **仍在运行**，占用 cuda:1，23.7 GB 显存，GPU 利用率 94% |
| cuda:1 释放 | **否** |
| 退出方式 | 父进程 88156 已退出，但实际 worker 子进程 88161（NSsid=88156）仍然存活 |

**日志进度：**
- Gen 0: 完成（baseline, eff_rank=417.55, ppl=9.55）
- Gen 1: 完成（eff_rank=479.49, ppl=10.01, training loss=1.9830）
- Gen 2: 完成（eff_rank=496.60, ppl=10.51, training loss=1.8782）
- Gen 3: **正在进行** — 生成合成数据中，已生成 6720/50000 samples
- 总共 10 代（`--generations 10`）

**结论：** kill 88156 只杀了父进程，子进程 88161 继承了工作并继续运行。如果 D011 要求停止此实验修复 controller bug，需要 `kill 88161` 才能真正停掉实验并释放 cuda:1。

---
