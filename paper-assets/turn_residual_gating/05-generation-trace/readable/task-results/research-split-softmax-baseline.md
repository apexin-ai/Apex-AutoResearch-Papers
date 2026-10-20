# research split softmax baseline

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_split_softmax_baseline_20260522T235952_result.json`
- **Structured JSON:** [`dbbd8815fbc377f518a3.json`](../../sessions/db/dbbd8815fbc377f518a3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have all the information needed. Here's the complete analysis:

---

## 1. 论文信息

- **标题**: Measuring and Controlling Instruction (In)Stability in Language Model Dialogs
- **作者**: Kenneth Li, Tianle Liu, Naomi Bashkansky, David Bau, Fernanda Viégas, Hanspeter Pfister, Martin Wattenberg
- **会议**: COLM 2024
- **arXiv**: [2402.10962](https://arxiv.org/abs/2402.10962)
- **代码**: [github.com/likenneth/persona_drift](https://github.com/likenneth/persona_drift) — 只有评估/benchmark 代码，**不含 split-softmax 实现**

## 2. Split-Softmax 数学公式

论文 Equation 6 (Section 6.2)：

**Step 1**: 计算 system prompt tokens 的累积 attention weight：
```
π(t) = Σ_{i=1}^{|s_B|} α_{t,i}
```

**Step 2**: 对 attention weights 做分组缩放：
```
α'_{t,i} = {
  [π^k(t) / π(t)] · α_{t,i}     if i ≤ |s_B|   (system prompt tokens)
  [(1 - π^k(t)) / (1 - π(t))] · α_{t,i}   if i > |s_B|   (conversation tokens)
}
```

**关键参数**:
- `π(t)`: 当前 timestep 对 system prompt 的总 attention 权重（softmax 后）
- `k ∈ [0, 1]`: 干预强度。k=1 无效果；k 越小，对 system prompt 的注意力提升越大
- 因为 `0 ≤ π(t) ≤ 1` 且 `0 ≤ k ≤ 1`，所以 `π^k(t)/π(t) ≥ 1`，保证 system prompt 注意力增大

**插入位置**: 在 softmax(QK^T/√d) 之后、与 V 加权求和之前。不改 softmax 本身，只是对 softmax 输出做 rescale。

**性质**: Training-free, parameter-free, inference-time only.

## 3. 实现方案评估

### 3.1 我们已有的基础设施

代码库已有类似的 attention 干预机制：

| 文件 | 现有功能 | 与 split-softmax 关系 |
|------|----------|----------------------|
| `src/attention_steering.py` | Pre-softmax additive bias (β-steering) | 修改 attention_mask，在 softmax **之前**干预 |
| `src/threadgate.py` | Residual stream gating (hook on layer output) | 不涉及 attention weights |
| `src/model_loader.py` | Gate loading + TurnFeaturesTracker | 可复用 `_find_hf_model()` 工具函数 |
| `src/eval_attention_steering.py` | β-steering 评估 pipeline | 评估框架可复用 |

### 3.2 实现方案

Split-softmax 需要在 **softmax 之后** 干预，这与现有 `AttentionSteering`（pre-softmax bias）不同。有两个方案：

**方案 A: Monkey-patch attention forward（推荐）**

类似 `AttentionSteering` 的做法，但需要修改 HF transformers 的 attention 内部逻辑：

```python
class SplitSoftmax:
    def __init__(self, model, k, system_prompt_len):
        self.k = k
        self.sp_len = system_prompt_len
        # patch each layer's self_attn.forward

    def _patched_forward(self, *args, **kwargs):
        # 需要 eager attention，不能用 SDPA/flash
        # 在 attn_weights = softmax(QK^T/√d + mask) 之后
        # 对 attn_weights[:, :, :, :sp_len] 乘以 π^k/π
        # 对 attn_weights[:, :, :, sp_len:] 乘以 (1-π^k)/(1-π)
```

**问题**: HF `Qwen2Attention.forward()` 在 eager mode 下内部完成 softmax + V 加权，attn_weights 不作为中间变量暴露。需要复制整个 `forward()` 方法并在中间插入 rescale 逻辑。

**方案 B: Register forward hook + output_attentions（不推荐）**

设置 `output_attentions=True` 后 HF 会返回 attn_weights，但此时 V 加权已经完成，无法回退修改。

### 3.3 具体实现步骤

1. **新建 `src/split_softmax.py`**:
   - 从 `transformers.models.qwen2.modeling_qwen2` 复制 `Qwen2Attention.forward()`（约 80 行）
   - 在 `attn_weights = nn.functional.softmax(attn_weights, dim=-1)` 之后插入 rescale 逻辑
   - 用 monkey-patch 替换每层的 `self_attn.forward`
   - 接口参考 `AttentionSteering`：`activate()` / `deactivate()` / `update_system_prompt_len()`

2. **新建 `src/eval_split_softmax.py`**:
   - 复用 `eval_attention_steering.py` 的评估框架
   - 替换 `AttentionSteering` 为 `SplitSoftmax`
   - 扫描 k ∈ {0.0, 0.1, 0.3, 0.5, 0.7, 0.9, 1.0}

3. **必须使用 `attn_implementation="eager"`**，SDPA/flash attention 不暴露中间 attn_weights

### 3.4 System prompt token 范围确定

`turn_utils.py` 中 `detect_turn_boundaries()` 已经返回 `goal_token_positions`（system prompt + first user message tokens）。可以直接复用，或者只取 system prompt 部分的 boundary。

## 4. 实现复杂度评估

| 项目 | 估计 |
|------|------|
| 核心 split-softmax 类 | **2-3 小时**（复制 + 修改 Qwen2Attention.forward） |
| 评估脚本 | **1-2 小时**（复用 eval_attention_steering 框架） |
| 调试 eager attention + KV cache 兼容 | **2-3 小时** |
| 总计 | **5-8 小时** |

主要风险：
- Eager attention 比 SDPA/flash 慢 2-5x，长序列评估耗时增加
- KV cache decode 阶段的 attn_weights shape 与 prefill 不同，需要额外处理
- 复制的 `forward()` 对 transformers 版本有硬依赖，升级可能 break

## 5. 开源实现

- **官方 repo** (`likenneth/persona_drift`): 只有 benchmark/evaluation 代码，无 split-softmax 实现
- **第三方**: 未找到可直接复用的实现
- **结论**: 需要自己实现

Sources:
- [Paper on arXiv](https://arxiv.org/abs/2402.10962)
- [GitHub: likenneth/persona_drift](https://github.com/likenneth/persona_drift)
- [Attention dilution blog post](https://binzhango.net/posts/2026/03-15-attention-dilution/)

---
