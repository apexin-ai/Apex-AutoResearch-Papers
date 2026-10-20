# research vllm trl compat

**prov grounded uie** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_vllm-trl-compat_20260512T200817_result.json`
- **Structured JSON:** [`91b33fffb8c061472101.json`](../../sessions/91/91b33fffb8c061472101.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the report.

---

## vLLM + TRL 1.1.0 兼容性报告

### 1. 版本现状

| 组件 | 已安装版本 | 备注 |
|------|-----------|------|
| vLLM | **0.18.1** | 可正常 import |
| TRL | **1.1.0** | 官方支持 vLLM **0.11.0–0.17.1** |
| GPU | 2× NVIDIA RTX PRO 6000 Blackwell | - |

### 2. 版本冲突

TRL 1.1.0 的 vllm extra 声明 `vllm<=0.17.1,>=0.11.0`。当前安装的 vLLM 0.18.1 **超出上界**。

`is_vllm_available()` 返回 `True`，但附带 UserWarning：
> TRL currently supports vLLM versions from 0.11.0 to 0.17.1. You have version 0.18.1 installed.

这是**软警告**，不是硬拦截。vLLM 0.18.1 可能存在 API 变更导致运行时崩溃。

### 3. GRPOTrainer 的 vLLM 配置方式

TRL 1.1.0 GRPOConfig 支持丰富的 vLLM 参数：

```python
GRPOConfig(
    use_vllm=True,                      # 启用 vLLM
    vllm_mode="colocate",               # "colocate"(同进程）或 "server"（独立服务）
    vllm_gpu_memory_utilization=0.3,     # colocate 模式下 GPU 显存占比
    vllm_tensor_parallel_size=1,         # 张量并行
    vllm_max_model_length=None,          # 最大序列长度
    vllm_enable_sleep_mode=False,        # 训练时释放 vLLM 显存
    vllm_model_impl="vllm",             # "vllm" 或 "transformers" 后端
    # importance sampling 相关
    vllm_importance_sampling_correction=True,
    vllm_importance_sampling_mode="sequence_mask",
    vllm_importance_sampling_cap=3.0,
)
```

两种模式：
- **colocate**: vLLM 与训练在同一进程，显存共享，适合单机
- **server**: 需先 `trl vllm-serve` 启动独立 vLLM 服务，训练器通过 HTTP 请求生成

### 4. train_grpo.py 当前状态

**未配置 vLLM**。使用标准 HuggingFace `AutoModelForCausalLM.from_pretrained()` 加载模型，GRPOTrainer 会用 `model.generate()` 逐条生成。

### 5. Qwen3-8B 兼容性

vLLM 0.18.1 完全支持 Qwen3 架构，无问题。

### 6. 结论与方案

**GRPO 训练可以用 vLLM，但需解决版本冲突。**

| 方案 | 操作 | 风险 |
|------|------|------|
| **A. 降级 vLLM（推荐）** | `pip install vllm==0.17.1` | 最安全，TRL 官方支持上界 |
| B. 直接用 0.18.1 | 不动，接受 warning | 可能因 API 变更在运行时崩溃 |
| C. 升级 TRL | 安装更新版 TRL 支持 0.18.x | 可能引入其他 breaking changes |

**推荐方案 A**，然后修改 `train_grpo.py` 中的 `GRPOConfig`，添加：

```python
training_config = GRPOConfig(
    ...
    use_vllm=True,
    vllm_mode="colocate",
    vllm_gpu_memory_utilization=0.5,   # 2x48GB GPU，可给 vLLM 更多显存
    vllm_tensor_parallel_size=1,
    vllm_enable_sleep_mode=True,        # 训练梯度更新时释放 vLLM 显存
)
```

注意：启用 vLLM 后 `model` 参数应传模型路径字符串而非加载好的模型对象（TRL 会用 vLLM 自己加载模型做 generation，用 HF 模型做 policy 更新）。需要检查 TRL 1.1.0 的具体签名是否已改为字符串传参。

---
