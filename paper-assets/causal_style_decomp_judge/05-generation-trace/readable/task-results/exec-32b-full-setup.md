# exec 32b full setup

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exec_32b_full_setup_20260520T154737_result.json`
- **Structured JSON:** [`ecf75dd78555b7812414.json`](../../sessions/ec/ecf75dd78555b7812414.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。产出报告：

---

### 1. 32B 模型
- **17/17 shards**，总大小 **62G**
- shard 17 从 `._____temp/` 移出，config.json 存在

### 2. 代码同步
- `counterfactual_gen.py`: **205 行** — `instruction_note` grep 匹配
- `ate_analysis.py`: **308 行** — `winsorize` grep 匹配

### 3. vLLM 状态：**READY**
- 模型: `Qwen3-32B`，max_model_len=4096
- PID: 41514 (APIServer: 41519, EngineCore: 41798)
- 启动耗时：模型加载 15s + torch.compile 24s + CUDA graph ~6s

### 4. GPU 显存
| GPU | Used | Total |
|-----|------|-------|
| 0 | **88,331 MiB** | 97,887 MiB |
| 1-3 | 0 MiB | 97,887 MiB |

GPU 0 占用 ~90.2%，符合 `gpu-memory-utilization 0.90` 设置。

---
