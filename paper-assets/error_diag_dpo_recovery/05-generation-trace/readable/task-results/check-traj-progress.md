# check traj progress

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_traj-progress_20260512T124957_result.json`
- **Structured JSON:** [`5d14c8133d54c42cc16f.json`](../../sessions/5d/5d14c8133d54c42cc16f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总报告

### 1. 轨迹收集进程
- **traj_p0** 和 **traj_p1** 均在运行中（PID 95813 / 95889，已运行约 7 分钟）
- 使用 Qwen3-8B 模型，每个进程目标 500 条（共 1000 条），`--max_steps 40`

### 2. 轨迹收集进度
- **part0**: 6/500 完成，当前成功率 0/6（全部 reward=False）
- **part1**: 5/500 完成，当前成功率 0/5（全部 reward=False）
- 总计 **11 条轨迹**（train_part0.jsonl 78KB/6行，train_part1.jsonl 83KB/5行）
- 每条轨迹耗时约 60-90 秒，预估完成全部 1000 条需要 **~18-25 小时**
- **目前所有轨迹 reward 均为 False**——Qwen3-8B 在 ALFWorld 上成功率为 0，需要关注

### 3. 磁盘状态
- 根分区：30G 用了 9.2G，剩余 21G — **安全**
- 数据盘：169G 用了 83G，剩余 87G — **安全**

### 4. Qwen3-14B-AWQ 模型
- **已下载完成**，9.4GB，两个 safetensors 分片各约 4.9GB
- 配置文件、tokenizer 均完整，可直接使用

### 5. GPU 使用
| GPU | 显存 | 利用率 | 用途 |
|-----|------|--------|------|
| 0 | 7.7G/24.6G | 100% | traj_p0 (Qwen3-8B) |
| 1 | 7.7G/24.6G | 42% | traj_p1 (Qwen3-8B) |
| 2 | 22.1G/24.6G | 100% | vLLM (democalib Qwen2.5-7B) |
| 3-5 | 空闲 | 0% | — |

### 注意事项
- 0/11 成功率值得警惕——可能是 prompt 或环境配置问题，也可能 Qwen3-8B 本身在 ALFWorld 上能力不足。收集到的轨迹全部是失败样本，对 RL 训练可能需要混合成功样本。
- GPU 3-5 空闲，Qwen3-14B-AWQ 已就绪，可以用来启动额外的收集进程或切换到 14B 模型。

---
