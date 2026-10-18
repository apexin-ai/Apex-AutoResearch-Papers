# ssh westd 70b verify fix

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_westd-70b-verify-fix_20260517T082725_result.json`
- **Structured JSON:** [`76025a988d23ebb88bd3.json`](../../sessions/76/76025a988d23ebb88bd3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

注释修复完成。汇总结果：

---

## 实验状态：未启动 / 已崩溃

### 核心问题

| 项目 | 状态 |
|------|------|
| tmux session | 不存在（`no server running`） |
| Python/vLLM 进程 | 无 |
| GPU 利用率 | 0%，0 MiB |
| 实验日志 | 不存在（`llama70b_cross_model.log` 两个路径均 404） |

### 根因分析（3 个阻塞项）

1. **只有 1 张 GPU**：`nvidia-smi -L` 只报出 1× RTX PRO 6000 Blackwell（`/dev/nvidia5`），但脚本需要 `TP_SIZE=2`。这台 cqa1-38874 不满足 2-GPU 要求。

2. **模型路径不匹配**：
   - 脚本 `MODEL_PATH` 默认值：`neuralmagic/Meta-Llama-3.1-70B-Instruct-FP8`（预期路径 `/root/autodl-tmp/models/llama-3.1-70b-instruct-fp8`，该目录不存在）
   - 实际已下载：`nvidia/Llama-3.3-70B-Instruct-FP8` → `/root/autodl-tmp/.hf_cache/llama-3.3-70b-instruct-fp8/`（68GB，15 个 shard 全部完整）

3. **vLLM Blackwell 兼容性问题**：8B 模型测试（`/tmp/vllm_test.log`）显示 vLLM 0.20.2 加载权重成功但 engine core 初始化失败（`RuntimeError: Engine core initialization failed`），伴有 `SM 12.x requires CUDA >= 12.9` 警告。

### 已完成的修复

- 脚本注释 `48GB each` → `96GB each` ✅

### 下一步建议

要在这台机器上运行 70B 实验，需要：
1. 将 `TP_SIZE` 改为 1（单 GPU 96GB 可以装 FP8 70B，约 68GB 权重）
2. 修正 `MODEL_PATH` 指向实际下载路径 `/root/autodl-tmp/.hf_cache/llama-3.3-70b-instruct-fp8/`
3. 解决 vLLM engine core 初始化问题（可能需要升级 CUDA 或换 vLLM 版本）

或者：在真正有 2 张 GPU 的 westd-24295 上运行（如果那是另一台机器）。

---
