# gpu w2 qwen3 7b setup

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_w2-qwen3-7b-setup_20260516T022949_result.json`
- **Structured JSON:** [`50015df5184c0156c448.json`](../../sessions/50/50015df5184c0156c448.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 sweep 实验都在 8 小时前 (02:49 UTC) 就停止产出日志了，分别卡在 step 56 和 48（共 500 步），reward_mean=0，但进程仍占用 79GB 显存。这些实验很可能已经挂了。

**当前状态汇总：**

| 项目 | 状态 |
|------|------|
| **模型** | Qwen/Qwen3-8B (from ModelScope) |
| **路径** | `/root/autodl-tmp/models/Qwen3-8B` |
| **大小** | 16GB (5 safetensors), 8.2B 参数 |
| **bf16 显存** | 15.3GB / 95GB |
| **配置文件** | `configs/grpo_exec_only_8b.yaml` 已创建 |
| **GPU 状态** | GPU 0 + GPU 1 均被占满（可能已挂的 sweep 实验） |

**阻塞问题：** GPU 1 被 `sweep_isr_b005_s42` (PID 589836) 占用 79GB 显存，该进程最后一条日志在 8 小时前。需要杀掉这个进程才能启动 pilot。

要我杀掉 GPU 1 上卡住的实验然后提交 8B pilot 吗？（按 C007 约束，kill 后需 nvidia-smi 确认释放）

---
