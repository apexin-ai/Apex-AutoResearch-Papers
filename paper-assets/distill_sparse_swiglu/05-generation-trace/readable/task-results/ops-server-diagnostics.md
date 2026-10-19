# ops server diagnostics

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_server-diagnostics_20260516T052010_result.json`
- **Structured JSON:** [`9bd9bd4d6b4dbb37d9f5.json`](../../sessions/9b/9bd9bd4d6b4dbb37d9f5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

cuda:0 已完全释放。诊断报告如下：

---

## 诊断报告 (2026-05-16 13:21 UTC)

### 1. bench_dense (PID 207789) — **已死亡**
- 启动后立即退出（exit code 2），参数错误：`--sparsity_mode dense` 不是有效选项（只接受 `per_token` / `teal_global`）
- 应改用 `--dense` flag 而非 `--sparsity_mode dense`
- **需要修复参数后重新启动**

### 2. bench_mistral_kl50_s42 (PID 207957) — **已清理**
- 父进程 207957 + 子进程 207962 均已 kill
- kill 前状态：运行 9h16m，正在跑 MMLU loglikelihood（2273/58702, ~4%），距离完成还很远
- cuda:0 显存已释放（0 MiB）

### 3. bce_isocompute_v3_s42 (PID 205597/205598) — **正常运行中**
- 运行时长：41h57m
- 当前进度：**step 2400/2700**（89%），剩余 300 步
- 速度：1.05s/step → **预计 ~5 分钟后完成**
- 最新指标：loss=0.6359, bce=0.6349, sparsity=0.511, lr=3.25e-05
- cuda:1 占用 90938 MiB，100% 利用率

### 4. GPU 状态
| GPU | 显存 | 利用率 | 温度 | 进程 |
|-----|------|--------|------|------|
| cuda:0 | **0 / 97887 MiB** | 100%→空闲 | 64°C | 无（已清理） |
| cuda:1 | 90938 / 97887 MiB | 100% | 65°C | bce_v3 (205598) |

### 待办
- **bench_dense** 需修复参数（用 `--dense` 替代 `--sparsity_mode dense`），cuda:0 现已空闲可重跑
- bench_dense registry 无需更新（从未成功运行）

---
