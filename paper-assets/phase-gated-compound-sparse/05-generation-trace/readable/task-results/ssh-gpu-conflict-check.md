# ssh gpu conflict check

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_gpu-conflict-check_20260514T153458_result.json`
- **Structured JSON:** [`e91f5f8424796b667221.json`](../../sessions/e9/e91f5f8424796b667221.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

### 1. GPU 实际占用表

| GPU | PID | 实验 | 任务 | 显存 |
|-----|-----|------|------|------|
| 0 | 130124 | c2_n500_deepseek | DeepSeek importance s0.15 | 26,854 MiB |
| 1 | 130263 | c2_n500_deepseek | DeepSeek random s0.15 | 30,598 MiB |
| **2** | **131864** | **c2_qw_n500** | **Qwen importance s0.15** | **27,824 MiB** |
| **2** | **142944** | **c3_llama** | **LLaMA importance s0.20** | **20,230 MiB** |
| **3** | **132002** | **c2_qw_n500** | **Qwen random s0.15** | **28,436 MiB** |
| **3** | **142708** | **c3_llama** | **LLaMA random s0.20** | **20,388 MiB** |

GPU 2 合计 48,054 / 97,887 MiB (49%)，GPU 3 合计 48,824 / 97,887 MiB (50%)。GPU 利用率均 89%。

### 2. PID 存活状态

| PID | 状态 | 运行时间 | 所属实验 |
|-----|------|---------|---------|
| 130124 | **活** | 1h54m | c2_n500_deepseek (GPU 0) |
| 130263 | **活** | 1h54m | c2_n500_deepseek (GPU 1) |
| 131864 | **活** | 1h43m | c2_qw_n500 (GPU 2) |
| 132002 | **活** | 1h43m | c2_qw_n500 (GPU 3) |
| 132389 | **死** | — | c2_qw_n500 重复进程 |
| 132392 | **死** | — | c2_qw_n500 重复进程 |
| 138393 | **活** | 50m | c3_llama launcher (bash) |
| 138398 | **活** | 50m | c3_llama 脚本 (run_c3_llama_full.sh) |
| 138408 | **死** | — | c3_llama s015 (已完成退出) |
| 138410 | **死** | — | c3_llama s015 (已完成退出) |
| 142944 | **活** | 3m43s | c3_llama importance s020 (新) |
| 142708 | **活** | 3m57s | c3_llama random s020 (新) |

### 3. 冲突判断

**真实共存，不是挤掉。** GPU 2 和 3 上 c2_qw_n500 和 c3_llama 确实同时在跑。每块 GPU 98GB 显存只用了约 50%，显存不是瓶颈。但 GPU 利用率 89%，两个实验在争抢算力，互相拖慢。

### 4. 重复进程

PID 132389/132392 **已死**，无需处理。

### 5. 各实验进度

| 实验 | GPU | 进度 | 备注 |
|------|-----|------|------|
| c2_n500_deepseek (imp) | 0 | **201/500** (40%) | 正常推进 |
| c2_n500_deepseek (rand) | 1 | **224/500** (45%) | 正常推进，稍快 |
| c2_qw_n500 (imp) | 2 | **173/500** (35%) | 正常但受 c3 影响 |
| c2_qw_n500 (rand) | 3 | **177/500** (35%) | 正常但受 c3 影响 |
| c3_llama s0.15 | 2+3 | **50/50 ✅ 完成** | importance PASS, random PASS |
| c3_llama s0.20 | 2+3 | **7/50** (14%) | 刚启动 ~4 分钟 |

### 6. 建议

**短期可以容忍共存。** 理由：
- 显存充足（每 GPU 仅用 50%），不会 OOM
- c3_llama s0.20 只跑 50 个 problem，预计 ~40-50 分钟内完成，之后自动释放 GPU 2+3
- c2_qw_n500 还剩 ~330 个 problem，还要跑几小时，c3 完成后它会恢复独占算力

**如果希望 c2_qw_n500 尽快完成**，可以杀掉 c3_llama s0.20 的两个进程（142944, 142708），等 c2_qw_n500 跑完再重启 c3。但收益有限——c3 很快就会自行结束。

**run_c3_llama_full.sh 脚本可能还有后续 sparsity level**（比如 s0.25 等），如果是的话，冲突会持续更久。建议确认该脚本包含几个 sparsity level。

---
