# code maniskill3 gpu isolation

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_maniskill3-gpu-isolation_20260516T032534_result.json`
- **Structured JSON:** [`78a0836eebe80868264d.json`](../../sessions/78/78a0836eebe80868264d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**修复内容：**
- `envs/maniskill.py`：用 `resolve_physical_device(device)` 替换旧的 `_cvd_stash`/`maniskill_target_device()` 机制。新函数在移除 CVD 前解析逻辑→物理 GPU 映射，返回正确的物理设备字符串。
- `dreamer.py`：在 `main()` 开头对 maniskill 任务调用 `resolve_physical_device()`，更新 `config.device` 为物理设备。

**验证结果：**
- 单元测试全部通过（CVD=1+cuda:0→cuda:1 等4种场景）
- dry-run 确认训练负载（4150 MiB）在 GPU 1，GPU 0 仅有不可避免的 643 MiB CUDA 上下文初始化
- 已有实验（PID 149708 / 536890）未受干扰
- 已提交 `3328f53`，测试文件已清理

---
