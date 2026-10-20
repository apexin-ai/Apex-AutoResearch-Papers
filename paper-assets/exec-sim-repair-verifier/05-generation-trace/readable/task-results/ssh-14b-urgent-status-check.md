# ssh 14b urgent status check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_14b-urgent-status-check_20260522T201634_result.json`
- **Structured JSON:** [`2313fc2972267df9ddf7.json`](../../sessions/23/2313fc2972267df9ddf7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

### 1. GPU 利用率
**4 张 RTX 5090 全部空闲**，无 GPU 进程。

| GPU | 显存 | 利用率 | 温度 |
|-----|------|--------|------|
| 0 | 0MiB / 32607MiB | 0% | 32°C |
| 1 | 0MiB / 32607MiB | 0% | 31°C |
| 2 | 0MiB / 32607MiB | 0% | 31°C |
| 3 | 0MiB / 32607MiB | 0% | 34°C |

### 2. 训练进程状态
两个进程**都活着**，但都在**等模型下载完成**：

| 进程 | PID | 状态 | 运行时长 | 当前阶段 |
|------|-----|------|----------|----------|
| cls14b-func-s42 (train) | 200350 | Ss+ (sleeping) | 2h19m | 等待下载，2分钟轮询一次 |
| 14b-baseline eval | 202994 | S (sleeping) | 1h44m | 等待下载，1分钟轮询一次 |

实际下载由 **PID 200698**（ModelScope snapshot_download）执行，占 604MB 内存。

### 3. 模型下载进度
下载目标：`/dev/shm/Qwen3-14B/`（共 8 个 shard）

| Shard | 状态 | 大小 |
|-------|------|------|
| model-00002 ~ 00007 | **完成** | 各 3.7GB |
| model-00008 | **完成** | 1.8GB |
| **model-00001** | **下载中** (在 `._____temp/`) | 3.5GB / ~3.7GB |

总量：28GB 已完成 + 3.5GB 正在写入，剩余约 200MB。**预计几分钟内完成**。

`/dev/shm` 空间充足：180GB 总量，已用 28GB。

### 4. 训练日志
`cls14b-func-s42.log` 内容全是下载等待轮询（每 2 分钟输出一行 "Downloaded: 27G/28G"），最后一行 04:15 显示 28G。

`/tmp/14b_eval.log` 同理，每分钟输出 Temp/Total 字节数，稳定增长中。

### 5. 下载完成后的执行计划
- **Train (GPU 0)**：`train_unified.py --task cls --model_name_or_path /dev/shm/Qwen3-14B --quantize_4bit --batch_size 1 --grad_accumulation 32 --lr 5e-5 --epochs 3`，然后自动 eval
- **Eval (GPU 1)**：先跑 0-shot 再跑 3-shot `eval_14b_baseline.py`

### 结论
**没有异常**。两个实验都在正常等模型下载，shard 1 还剩约 200MB，几分钟后下载完成，训练和 eval 会自动启动。

---
