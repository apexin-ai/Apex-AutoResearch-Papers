# ssh vllm upgrade test

**prov grounded uie** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_vllm-upgrade-test_20260512T221515_result.json`
- **Structured JSON:** [`5317e54a6f760979d0ca.json`](../../sessions/53/5317e54a6f760979d0ca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

sft_eval_v4 正常运行。以下是完整报告：

---

## 报告

### 1. vLLM 升级结果
- **0.17.1 → 0.18.1 升级成功**（同时升级了 xgrammar 0.1.29→0.2.0, flashinfer 0.6.4→0.6.6）
- 版本确认：`vLLM: 0.18.1`

### 2. GRPO with vLLM 测试（use_vllm=True）：失败
- **错误**：`AssertionError: duplicate template name`
- **根因**：vLLM 0.18.1 加载 Qwen3ForCausalLM 时触发 `torch._inductor.select_algorithm` 的 duplicate template 断言。这是 **vLLM 0.18.1 与当前 torch 2.10.0 的兼容性 bug**。
- **补充**：TRL 也警告 vLLM 0.18.1 超出支持范围（TRL 支持 0.11.0-0.17.1）。

### 3. Fallback 测试（use_vllm=False）：也失败
- Generation 阶段成功完成（耗时 ~3 分 12 秒，5 samples × 2 generations）
- **Backward pass OOM**：`torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 2.32 GiB`
- 24B 模型全精度 + gradient 在单卡 95GB 上不够用（模型本身占 ~44GB + PyTorch 分配 42GB）

### 4. sft_eval_v4 进程状态
- PID 40391，运行 43 分钟，状态正常（S）。**未受影响。**

### 5. Reward 值
- 无——两个测试均未完成 step 1。

### 6. 结论：正式 GRPO 训练应该用 vLLM 还是 HF generation

**当前两者都不可用：**

| 方案 | 问题 | 修复方向 |
|------|------|----------|
| **vLLM** | 0.18.1 与 torch 2.10.0 不兼容（duplicate template）；TRL 只支持到 0.17.1 | 回退到 `vllm==0.17.1`（之前安装的版本），或等 TRL 适配 |
| **HF generation** | 24B 模型单卡 OOM（backward pass） | 需要加 `--gradient_checkpointing`、`--bf16`、或 LoRA/QLoRA 降显存 |

**建议路径**：
1. **回退 vLLM 到 0.17.1**（pip install vllm==0.17.1），用 vLLM generation 解决速度问题
2. 同时加 `--gradient_checkpointing True --bf16 True` 解决 backward OOM——无论用 vLLM 还是 HF generation 都需要这个

---
