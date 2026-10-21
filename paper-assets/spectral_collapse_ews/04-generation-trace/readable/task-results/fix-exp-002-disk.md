# fix exp 002 disk

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_exp_002_disk_20260516T154347_result.json`
- **Structured JSON:** [`7f6bfc8cd29a417fc510.json`](../../sessions/7f/7f6bfc8cd29a417fc510.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论：exp_002 运行正常，无需修复或重启

**误报原因**：`/root/spectral_collapse_ews/results/phase0_1b/phase0_1b_run.log` 中的 SafetensorError 来自**之前的手动运行**（symlink 还没建好时），不是 exp_002。

**exp_002 实际状态**：
| 项目 | 状态 |
|------|------|
| 进程 | PID 25237 (python)，`Rl` Running 状态，已运行 2h27m |
| GPU | cuda:1，占用 25636 MiB |
| Gen 0 checkpoint | 完整保存在数据盘（3.8G），symlink 正确 |
| Gen 0 评估 | eff_rank=516.14, ppl=8.07, distinct4=0.7510 |
| 当前进度 | 正在 Gen 1（checkpoint 目录只有 gen_0，尚无 phase0_results.json） |
| exp_002.log | 只有 1416 行 HF padding 警告（stderr），stdout 因 Python block buffer 未刷到日志 |

**为什么 exp_002.log 看不到进度**：submit_training_job 把 stdout 重定向到文件，Python 默认 block buffer，print 输出还没 flush。HF 警告走 stderr（unbuffered），所以只看到警告。

**建议**：不做任何操作，等待实验自然完成。后续提交可加 `PYTHONUNBUFFERED=1` 让日志实时可见。

---
