# ops verify unixcoder s43 running

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify_unixcoder_s43_running_20260516T093958_result.json`
- **Structured JSON:** [`7e0f1ad9eb588a951007.json`](../../sessions/7e/7e0f1ad9eb588a951007.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论：训练已确认在运行

**验证结果：**

| 项目 | 状态 |
|------|------|
| conda 激活行 | ✅ 三个脚本（s43/s44/chain）均已添加 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base` |
| GPU 进程 | ✅ PID 168000 占用 16042 MiB（`/root/miniconda3/bin/python`）— UniXcoder s43 训练 |
| 错误日志 | ✅ grep "error" 返回空（return_code=1 = 无匹配），无任何报错 |
| 训练进度 | ✅ Epoch 1 已启动，703 batches/epoch，已完成 step 50，loss=0.6417 |
| 输出目录 | ✅ `/root/autodl-tmp/structfuse/full_m2_unixcoder_outputs/random_s43/` 已创建，正在写入 |

**当前状态**：
- **策略**：random, seed=43
- **PID**：168000
- **GPU 显存**：16042 MiB
- **进度**：step 50 / 703（epoch 1/2），loss 0.6417，lr 正在 warmup（7.14e-06）
- **启动时间**：2026-05-16 17:36:48

训练确实在正常运行，不是虚报。另外 PID 165674（16044 MiB）可能是另一个 UniXcoder 任务（s44 或其他 strategy），但 chain 脚本是串行的（s43 完成后才跑 s44），所以 165674 可能是之前启动的另一个进程。

---
