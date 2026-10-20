# research flash attention

**prov grounded uie** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_flash-attention_20260512T200700_result.json`
- **Structured JSON:** [`f4fd43c3ac40ad646745.json`](../../sessions/f4/f4fd43c3ac40ad646745.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有信息已收集完毕。

---

## Flash Attention 调查报告

### 1. flash-attn 安装状态
**未安装。** `/root/miniconda3/lib/python3.12/site-packages/flash_attn/` 不存在。

### 2. GPU 与环境

| 项目 | 值 |
|------|------|
| GPU | NVIDIA RTX PRO 6000 Blackwell Server Edition |
| Compute Capability | **sm_120 (12.0)** |
| PyTorch | 2.10.0+cu128 |
| CUDA | 12.8 |
| Transformers | 4.57.6 |
| SDPA | **可用** |

### 3. 代码中 FA 的开关逻辑

`config.py:28`: `use_flash_attention: bool = field(default=False)`

4 个文件通过同一条件控制：
```python
if model_args.use_flash_attention:
    model_kwargs["attn_implementation"] = "flash_attention_2"
```
- `train_grpo.py:41`
- `train_sft.py:45`
- `evaluate.py:123`
- `rerank_nli.py:76`

### 4. FA 被关闭的原因

两层原因：
1. **配置默认 False** — `use_flash_attention` 从未被启用
2. **flash-attn 包未安装** — 即使设为 True 也会报 ImportError

进一步：Blackwell sm_120 非常新，flash-attn pip 包（Dao-AILab）可能尚无 sm_120 + CUDA 12.8 + torch 2.10 的预编译 wheel，源码编译也存在兼容性风险。

### 5. 结论

**不建议安装 flash-attn 包。SDPA 已可用且是更优选择。**

- Transformers 4.57.6 默认使用 SDPA（`scaled_dot_product_attention`），**不指定 `attn_implementation` 时已自动启用**
- PyTorch 2.10 的 SDPA 在 Blackwell 架构上会自动调度到最优内核（cuDNN FlashAttention / Memory-Efficient Attention），性能与独立 flash-attn 包基本持平
- 当前代码不传 `attn_implementation` 时，transformers **已经在用 SDPA**，所以实际上高效注意力已经生效

### 6. 配置建议

**无需改动。** 当前 `use_flash_attention=False` 不传 `attn_implementation`，transformers 4.57.6 自动走 SDPA 路径。

如果想显式确认，可以加一行日志验证：
```python
# 在 model load 后打印
print(model.config._attn_implementation)  # 应输出 "sdpa"
```

如果某些场景需要强制指定，改为：
```python
model_kwargs["attn_implementation"] = "sdpa"
```

但通常不必要——默认行为已是 SDPA。

---
