# ops gpu check and eval diagnose

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_check_and_eval_diagnose_20260514T154422_result.json`
- **Structured JSON:** [`18c30fedd361ad33e1d8.json`](../../sessions/18/18c30fedd361ad33e1d8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. GPU 状态 (0-5)

| GPU | 显存占用 | 利用率 | 进程 | 任务 |
|-----|----------|--------|------|------|
| **0** | 14.4/24.6 GB | 19% | PID 385407 | SFT 训练 Qwen2.5-1.5B d025 (22:18 启动) |
| **1** | 5.9/24.6 GB | 88% | PID 398887 | Eval Qwen2.5-1.5B aligned batch (23:41 启动) |
| **2** | 11.1/24.6 GB | 99% | PIDs 395342, 395764, 396024 | **⚠️ 3 个 eval 0.5B d100 进程挤在同一 GPU (C001 违规)** |
| **3** | 3.7/24.6 GB | 37% | PID 398501 | Eval 0.5B d025 aligned (23:40 启动) |
| **4** | 9.0/24.6 GB | 64% | PID 373931 | Eval 3B d005 aligned (21:09 启动) |
| **5** | 0/24.6 GB | 0% | — | **空闲** |

### 2. d025 aligned eval — 没有失败，正在运行

Registry 标记 DONE(failed) 是**误报**。PID 398501 正在 GPU 3 上正常执行：
- MMLU 已完成：28.03% (3936/14042)
- GSM8K 正在跑：~20/1319 (~1.5%)，~6s/it，预计还需 ~2h
- bitsandbytes 的 `libnvJitLink.so.13` 报错是非致命 warning，不影响推理
- 无 exit file 存在，进程未退出

### 3. d100 aligned v3/v4 — 都在跑，但有重复提交问题

两个实验都在 GPU 2 上**同时运行**，产生了 3 个 python 进程共享一张卡：
- v3 log: GSM8K ~13% (167/1319)
- v4 log: GSM8K ~13% (173/1319)
- 输出目录 `Qwen2.5-0.5B_d100_s42_aligned/` 为空（尚未写出结果）
- 无 exit file，均未退出
- Registry 显示 PREPARING 不准确，实际已在跑

**问题**：3 个进程挤 GPU 2（每个占 ~3.7GB），互相争抢计算资源（利用率 99%），且可能写同一输出目录导致数据冲突。建议 kill 多余进程，只保留一个。

### 4. 可用 GPU

- **GPU 5**：完全空闲，可立即接新任务
- 其余 GPU 均被占用
- 另外注意：pts/3 上有一个 zombie 进程 (PID 318424, `[python] &lt;defunct>`)，不占资源但可清理

---
