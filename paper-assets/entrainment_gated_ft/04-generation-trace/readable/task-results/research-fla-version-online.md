# research fla version online

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_fla-version-online_20260518T123638_result.json`
- **Structured JSON:** [`cdb43cc1a65be5a13238.json`](../../sessions/cd/cdb43cc1a65be5a13238.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 调查结果

### 核心结论：attn.D 是死参数，丢弃无影响

**GatedDeltaNet 的 `attn.D` 在 forward() 中从未被使用。** 它是从 Mamba2 继承的残留参数，初始化为 `ones(num_heads)`，训练期间不参与计算、不接收梯度，始终保持初始值。

#### 时间线

| 事件 | 日期 | 详情 |
|------|------|------|
| GatedDeltaNet 加入 fla | 2024-12-20 | commit `4064237`，包含 `self.D`（未在 forward 中使用） |
| self.D 被移除 | 2025-03-12 | commit `834989c`，fix #226 "Remove redundant parameter" |
| fla v0.1.0 发布 | 2025-03-20 | 首个 tagged release，已无 self.D |
| m-a-p 模型训练 | ~2025 Q1-Q2 | 使用 pre-v0.1.0 的 fla 开发版 |

#### m-a-p 模型 checkpoint 验证

- `1.3B-100B-GatedDeltaNet-pure` 的 safetensors 中确实包含 24 个 `attn.D` 参数
- 这些 D 值应全为 1.0（可用加载 checkpoint 后 print 验证）
- RetNet 模型**无此问题**，checkpoint 中不含 attn.D

#### 版本信息

- m-a-p 模型使用的 fla：pre-v0.1.0 开发版（commit 834989c 之前）
- 模型 config 中 transformers_version：4.51.3（1.3B GatedDeltaNet）/ 4.49.0（RetNet、340M）
- 论文未标注具体 fla 版本

### 建议

**当前 fla 0.5.0 可以安全使用**，`strict=False` 加载时 attn.D 被丢弃不影响模型输出。无需降级 fla 版本。

如需二次确认，可在服务器上验证：
```python
from safetensors import safe_open
f = safe_open("model-00001-of-00002.safetensors", framework="pt")
print(f.get_tensor("model.layers.0.attn.D"))  # 应为全 1
```

Sources:
- [arXiv 2507.06457](https://arxiv.org/abs/2507.06457)
- [fla-org/flash-linear-attention](https://github.com/fla-org/flash-linear-attention)
- [fla releases](https://github.com/fla-org/flash-linear-attention/releases)
- [fla issue #226](https://github.com/fla-org/flash-linear-attention/issues/226)
- [m-a-p HuggingFace collection](https://huggingface.co/collections/m-a-p/hybrid-linear-attention-research-686c488a63d609d2f20e2b1e)
- [flash-linear-attention PyPI](https://pypi.org/project/flash-linear-attention/#history)

---
