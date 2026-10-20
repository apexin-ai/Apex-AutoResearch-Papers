# ops kill and diagnose tier2 hang

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill-and-diagnose-tier2-hang_20260527T231952_result.json`
- **Structured JSON:** [`7bb2033e00a5ab62ec81.json`](../../sessions/7b/7bb2033e00a5ab62ec81.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 1. Kill 状态
- S6/S7 进程已 kill（EXIT_CODE=143），GPU 已完全释放。

### 2. 数据异常检查
- **无 NaN/inf**，metrics 到 step 8000 全部正常。
- S6 最后 eval_return=31.1（step 5000），train_return 24~77（step 8000）
- S7 最后 eval_return=31.2（step 5000），train_return 28~50（step 8000）
- 数值在 Walker 早期训练的正常范围内。

### 3. 根因：**S6 和 S7 都在 cuda:0 上运行（GPU 撞车）**

对比启动命令：
| 实验 | Registry GPU 分配 | 实际 `--device` | EGL_DEVICE_ID |
|------|------------------|----------------|---------------|
| S6 | cuda:0 | **cuda:0** | 0 |
| S7 | cuda:1 | **cuda:0** ← 错误 | 1 |

S7 的 `--device cuda:0` 写错了，应该是 `cuda:1`。两个实验挤在同一块 GPU 上，导致显存竞争和训练速度大幅下降，表现为"卡死"。

成功实验 `exp_009e_008d_walker_s1` 在 bjb1-45299 上用的是 `--device cuda:1`，独占 GPU，约 5.4 GPU-hours 正常完成。

### 4. 环境
- torch=2.8.0+cu128，无 core dump，无 CUDA/GPU 错误。
- Config.yaml 文件未保存到 logdir（两个实验均无）。

### 5. 建议
**可以直接重启，无需改代码。** 重新提交时修正 S7 的 `--device cuda:1`，确保两个实验分别独占一块 GPU。两个实验的 logdir 已有 step 8000 的 checkpoint，如果代码支持 resume 可以接续训练，否则清空 logdir 从头跑。

---
