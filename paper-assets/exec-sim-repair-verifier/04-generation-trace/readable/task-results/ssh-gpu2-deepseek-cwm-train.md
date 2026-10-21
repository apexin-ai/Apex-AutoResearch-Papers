# ssh gpu2 deepseek cwm train

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_gpu2-deepseek-cwm-train_20260520T030642_result.json`
- **Structured JSON:** [`ac37ffd35638a2471e52.json`](../../sessions/ac/ac37ffd35638a2471e52.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全貌清晰了。汇报：

## 服务器状态报告

### 1. nvidia-smi

| GPU | 型号 | 显存占用 | GPU利用率 | 状态 |
|-----|------|---------|----------|------|
| 0 | RTX 5090 | 21253/32607 MiB | 90% | Qwen3-8B CWM s123 训练 (PID 886278) |
| 1 | RTX 5090 | 0/32607 MiB | **100%** | **HUNG** — 无进程但利用率100% |
| 2 | RTX 5090 | 28707/32607 MiB | 85% | DeepSeek CWM s123 eval (PID 893823) |
| 3 | RTX 5090 | 31261/32607 MiB | 96% | Qwen3-8B CWM s456 训练 (PID 886352) |

### 2. GPU 1 Hung 状态
GPU 1 显存 0 MiB，无任何 compute process，但 GPU utilization 锁死 100%。典型 GPU hang — 之前的进程异常退出后 GPU 卡在忙循环，需要 `nvidia-smi -r` 或重启实例才能恢复。

### 3. deepseek-cwm-repo-s123-train — 实际成功
Registry 标记 conclusion=success 是**正确的**：
- 训练完整跑完：2865/2865 steps，3 epochs，耗时 5255s（~1.46h）
- train_loss=0.0767, eval_loss=0.0427
- Checkpoints 完整：`best/`（adapter_model.safetensors 67MB）、`checkpoint-1910/`、`checkpoint-2865/`
- EXIT_CODE=2 可能是日志收集脚本的返回码，不影响训练本身

### 4. GPU 2 不可用
GPU 2 当前正在跑 s123 eval（tmux session: `eval_s123`）：
- 进度：728/9784（~7.4%）
- 速率：~81 samples/min
- 预计剩余：**~112 分钟（~1h52m）**

### 5. 当前 tmux sessions
- `qwen3-8b-cwm-repo-s123-train-v4` — GPU 0
- `qwen3-8b-cwm-repo-s456-train-v3` — GPU 3
- `eval_s123` — GPU 2

### 结论
**无法立即在 GPU 2 上启动 s456 训练。** 三个选项：

1. **等 eval 跑完**（~2h 后 GPU 2 空出），再启动 s456
2. **用 GPU 1**（需要先 `nvidia-smi -r` 重置解除 hang 状态，有风险可能影响其他 GPU）
3. **手动终止 eval**（如果 eval 不重要的话）

需要你决定怎么处理。

---
