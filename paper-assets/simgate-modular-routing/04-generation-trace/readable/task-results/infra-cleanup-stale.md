# infra cleanup stale

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_cleanup-stale_20260513T062057_result.json`
- **Structured JSON:** [`c9587296c0086435e5da.json`](../../sessions/c9/c9587296c0086435e5da.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

找到根因了。

## 报告

### 1. Phase 1 进程状态：**已崩溃，两个都挂了**
- 无 phase1_signal 进程在运行
- tmux 无 session（`no server running`）
- 两个 GPU 进程（gpu0 和 gpu1）都在 vLLM 初始化阶段崩溃退出

### 2. 残留数据
- `results/mvp/boil/` 目录存在但**为空**（进程在写入任何 episode 前就崩了）
- 无需清理旧数据

### 3. 崩溃原因
**PyTorch 2.10.0+cu128 与 vLLM 0.18.1 不兼容。** 底层错误：

```
torch/_inductor/kernel/flex_attention.py, line 786
AssertionError: duplicate template name
```

vLLM 在子进程中 inspect 模型架构 `Qwen2ForCausalLM` 时，触发了 torch inductor 的 Triton template 重复注册 bug。模型文件本身没问题（4 个 safetensors，共 ~14.2GB，完整下载）。

### 4. GPU 利用率
- 2x RTX 5090 (32GB each)，CUDA 13.0
- 当前 **0MiB 显存占用，无进程**
- `nvidia-smi` 显示 100% GPU-Util 但这是残留状态，实际空闲

### 修复方向
需要解决 vLLM 0.18.1 + torch 2.10.0 的兼容性问题。选项：
1. **降级 vLLM** 到与 torch 2.10.0 兼容的版本（如 0.17.x）
2. **升级 vLLM** 到已修复此 bug 的更新版本
3. **降级 torch** 到与 vLLM 0.18.1 兼容的版本

需要你决定走哪条路线。

---
