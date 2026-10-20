# diagnose exp 001 eval 3B d100 s123 para aligned

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_001_eval_3B_d100_s123_para_aligned_20260515T183943_result.json`
- **Structured JSON:** [`b222c8261e20caea8d38.json`](../../sessions/b2/b222c8261e20caea8d38.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

**状态：实验失败，需要重跑。**

| 检查项 | 结果 |
|--------|------|
| PID 608809 | 已消失 |
| 日志 | 启动于 02:18:56，最后写入 02:33:06（运行约 14 分钟）|
| 错误信息 | 无任何 error/exception/traceback（bitsandbytes 警告是非致命的）|
| 进展 | mmlu paraphrased 完成 → GSM8K paraphrased 跑到 22% (51/228) 时进程突然消失 |
| 输出目录 | 存在但**完全为空**，无任何结果文件 |
| 磁盘 | /root/autodl-tmp 有 43GB 剩余，排除磁盘满 |
| 系统日志 | AutoDL 容器无 kern.log/syslog/dmesg，无法确认 OOM kill |

**原因判断：** 进程在 GSM8K 生成式评测过程中被外部 kill（无 Python traceback 输出）。最可能是系统 OOM killer 或 GPU OOM（生成任务内存持续增长）。evaluate.py 仅在全部 benchmark 完成后才写结果文件，所以 14 分钟的计算全部丢失。

**GPU 3 当前状态：** 有 PID 611726 占用 ~8GB，非空闲。

**建议：**
1. 确认 GPU 3 上 PID 611726 是什么任务，等它结束或选其他空闲 GPU
2. 重跑时确保显式 `CUDA_VISIBLE_DEVICES=N`（遵守 C004）
3. 提交前 `nvidia-smi` + `ps` 确认目标 GPU 无残留进程（遵守 C001/C002/C003）

---
