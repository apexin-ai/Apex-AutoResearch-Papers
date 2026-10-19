# check qwen s44 eval1500

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_qwen-s44-eval1500_20260515T000247_result.json`
- **Structured JSON:** [`eda76e5f8bf8711996ac.json`](../../sessions/ed/eda76e5f8bf8711996ac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**eval@1500 正在执行中**，尚未完成。

### 当前状态
- **PID 504138**：State=R (running)，GPU 0 利用率 100%，占 51.5GB 显存
- **当前位置**：step 1500/2816（epoch 2 开始），日志最后更新 07:48 CST，服务器当前时间约 08:04 CST
- **eval 已运行约 16 分钟**，等待结果输出

### 已有 eval 结果
| checkpoint | val_loss | R@1 | patience |
|---|---|---|---|
| eval@500 | **0.4252** (best) | **0.6009** (best) | - |
| eval@1000 | 0.4695 | 0.5638 | 1/2 |
| eval@1500 | ⏳ 运行中 | ⏳ | 如不 improve → 2/2 触发 early stop |

### 预测
参考 random_s43 的同位置结果（eval@1500 val_loss=0.5477，触发 early stopping），random_s44 大概率也会在 eval@1500 early stop。

### 额外发现
- random_s42 和 random_s43 已完成，当前是 random_s44（第 2/9 个 run）
- 有多个僵尸 Python 进程（PID 892224, 960772）加载了模型但未占 GPU，不影响训练但浪费内存
- GPU 1 上另有 StarCoder random_s43 训练在并行跑

---
