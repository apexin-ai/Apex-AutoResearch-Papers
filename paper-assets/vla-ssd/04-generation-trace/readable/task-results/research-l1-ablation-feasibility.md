# research l1 ablation feasibility

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_l1_ablation_feasibility_20260517T115528_result.json`
- **Structured JSON:** [`1dbb4e83786a1e3efd3c.json`](../../sessions/1d/1dbb4e83786a1e3efd3c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据收集完毕。以下是可行性报告。

---

## L1 Attention Head Ablation 可行性报告

### 1. L1 Instruction-Dominant Heads

来源：`full_32layer_attention_summary.json` (trained 条件，10 tasks 平均)

L1 共 **24/32 heads** 的 text attention > 50%：

| Head | Text Attn | Head | Text Attn | Head | Text Attn |
|------|-----------|------|-----------|------|-----------|
| **0** | 0.8589 | **11** | 0.5671 | **22** | 0.8264 |
| **1** | 0.5308 | **12** | 0.5216 | **23** | 0.5683 |
| **2** | 0.6857 | **14** | 0.7040 | **25** | 0.7706 |
| **4** | 0.5781 | **15** | 0.6226 | **26** | 0.5614 |
| **7** | 0.5673 | **16** | 0.5382 | **27** | 0.6854 |
| **8** | 0.5797 | **17** | 0.5290 | **29** | 0.5971 |
| **10** | 0.7138 | **18** | 0.5196 | **30** | 0.5430 |
| **19** | 0.6500 | **20** | 0.5185 | **31** | 0.5552 |

Non-dominant heads (<=0.5): **3, 5, 6, 9, 13, 21, 24, 28** (8 heads, 作为 control)

---

### 2. 现有代码结构

| 功能 | 脚本 | 入口 |
|------|------|------|
| Feature extraction (全层 hidden states) | `scripts/extract_features.py` | `--model_path --data_dir --output_dir --mode trained` |
| Cross-instruction extraction (spatial, L0-L31) | `scripts/cross_instruction_extract_dense.py` 类似脚本 | 已有结果 `cross_instruction_spatial/` |
| 10-way instruction classification | `scripts/cross_instruction_classify_spatial.py` | LogisticRegression, PCA-256, train on tasks 0-7, test 8-9 |
| Action probe (R² regression) | `scripts/action_probe_libero_spatial.py` | MLP(4096→256→7), epochs=50, patience=5 |
| Attention extraction (existing) | `scripts/full_layer_attention_analysis.py` | `register_forward_hook` + `output_attentions=True` |

**Baseline 数据已有**：
- Cross-instruction classification (trained, last_preaction, L1): **98.9%**
- Action probe R² (trained, last_preaction, L1): **0.6799**

---

### 3. Hook 实现方案

**环境确认**：
- transformers **4.57.6**
- 模型加载时使用 `attn_implementation="eager"` — attention weights 被显式计算，无 Flash Attention/SDPA
- 现有 hook pattern：`model.language_model.model.layers[i].self_attn.register_forward_hook(hook_fn)`

**问题**：`register_forward_hook` 在模块 forward 完成后触发，此时 `attn_weights @ V` 已计算完毕，无法 retroactively 修改 attention。

**推荐方案：Monkey-patch forward method**

```python
import types
from transformers.models.llama.modeling_llama import LlamaAttention

def create_ablated_forward(original_forward, head_indices, instruction_positions):
    def ablated_forward(self, *args, **kwargs):
        # Force output_attentions to get intermediate weights
        # But we need to intercept BEFORE V multiplication
        ...
    return ablated_forward
```

实际上更干净的做法是**直接 copy LlamaAttention.forward 的 eager 实现代码**，在 softmax 之后插入 ablation 逻辑：

```python
# After: attn_weights = nn.functional.softmax(attn_weights, dim=-1)
# Insert:
attn_weights[:, ablate_head_indices, :, instruction_token_positions] = 0.0
attn_weights = attn_weights / attn_weights.sum(dim=-1, keepdim=True).clamp(min=1e-9)
# Then: attn_output = torch.matmul(attn_weights, value_states)
```

然后用 `types.MethodType` 替换 Layer 1 的 self_attn.forward。

**关键点**：
- 只需 patch Layer 1 的 self_attn
- instruction_token_positions = `range(257, seq_len)` (BOS=0, image=1:257, text=257:end)
- 后续层保持不变，正常 forward
- 提取 ablation 后的 hidden states 给 downstream probes

---

### 4. 潜在风险/Blockers

1. **无 major blocker**。`eager` 模式确保 attention weights 显式存在。
2. **Monkey-patch 脆弱性**：transformers 版本升级可能改变 `LlamaAttention.forward` 签名。建议固定版本或 copy 当前实现。
3. **Renormalization 可能引入 NaN**：如果某行 attention 全被 zero 掉（不会发生，因为只 zero instruction positions，image/BOS tokens 仍有非零 attention）。
4. **实验设计**：ablate 24/32 heads 是一个很强的 intervention。建议同时设计 graduated ablation（top-5, top-10, all-24）和 control（ablate 8 non-dominant heads）。

---

### 5. 建议实现路径

**新建文件**：`scripts/l1_head_ablation.py`

**实现步骤**：
1. 加载模型（`attn_implementation="eager"`），确定 instruction token positions
2. Monkey-patch `model.language_model.model.layers[1].self_attn.forward`，插入 ablation 逻辑
3. Forward pass 所有 cross-instruction 样本，提取 ablation 后 last_preaction hidden states (L1 之后各层)
4. 保存 features 到 HDF5（与现有 `cross_instruction_spatial` 格式兼容）
5. 复用 `cross_instruction_classify_spatial.py` 跑 10-way classification
6. 复用 `action_probe_libero_spatial.py` 跑 R² regression

**实验条件矩阵**：
- Ablate all 24 dominant heads
- Ablate top-5 strongest heads (0, 22, 25, 10, 14)
- Ablate 8 non-dominant heads (control)
- No ablation (baseline, 已有)

**预估工作量**：
- 写 ablation 脚本 + 测试：~2-3 小时
- 跑 4 个条件的 feature extraction（每条件 ~5 min on spatial）：~20 min
- 跑 probes：< 5 min
- 总计 **半天可完成**

---
