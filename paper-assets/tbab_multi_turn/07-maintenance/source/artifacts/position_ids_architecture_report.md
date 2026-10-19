# TBAB 技术调研报告：Qwen2.5-7B Position IDs 操控与 Bridge Token 架构

> 调研日期：2026-05-18
> 模型：Qwen2.5-7B-Instruct (d_head=128, **rope_theta=1,000,000**, GQA 28H/4KV)

---

## 0. 关键发现摘要

| 问题 | 结论 |
|------|------|
| 能否外部传入自定义 position_ids？ | **可以**，无需修改模型代码 |
| position reset 有没有副作用？ | **有**，会触发 packed sequence 检测，阻断跨 turn attention |
| 解决方案 | 传入预构建的 **4D attention mask** 绕过检测 |
| rope_theta 实际值 | **1,000,000**（非 10000），已用大 base 扩展上下文 |
| Bridge token 实现推荐 | **词表扩展 + PEFT trainable_token_indices**（MVP 路径） |
| LoRA 配置推荐 | `target_modules="all-linear"`, r=32, lora_alpha=64 |

---

## 1. Position IDs 操控

### 1.1 源码位置

Qwen2.5 复用 Qwen2 架构（`model_type = "qwen2"`）：

| 文件 | 路径 |
|------|------|
| 模型代码 | `transformers/models/qwen2/modeling_qwen2.py` |
| 配置 | `transformers/models/qwen2/configuration_qwen2.py` |
| RoPE 工具 | `transformers/modeling_rope_utils.py` |
| Mask 工具 | `transformers/masking_utils.py` |

### 1.2 RoPE 实现

核心类 `Qwen2RotaryEmbedding`：

```python
class Qwen2RotaryEmbedding(nn.Module):
    def forward(self, x, position_ids):
        # inv_freq: (d_head/2,) = (64,)
        inv_freq_expanded = self.inv_freq[None, :, None].expand(batch, -1, 1)
        position_ids_expanded = position_ids[:, None, :].float()
        # freqs: (batch, seq_len, d_head/2)
        freqs = (inv_freq_expanded @ position_ids_expanded).transpose(1, 2)
        emb = torch.cat((freqs, freqs), dim=-1)  # (batch, seq_len, d_head)
        cos = emb.cos() * self.attention_scaling
        sin = emb.sin() * self.attention_scaling
        return cos, sin
```

关键函数 `apply_rotary_pos_emb`：

```python
def apply_rotary_pos_emb(q, k, cos, sin, unsqueeze_dim=1):
    cos = cos.unsqueeze(unsqueeze_dim)  # (batch, 1, seq_len, d_head)
    sin = sin.unsqueeze(unsqueeze_dim)
    q_embed = (q * cos) + (rotate_half(q) * sin)
    k_embed = (k * cos) + (rotate_half(k) * sin)
    return q_embed, k_embed
```

### 1.3 position_ids 传递链路

```
Qwen2ForCausalLM.forward(position_ids=...)
  └─ Qwen2Model.forward(position_ids=...)
       ├─ if position_ids is None → 自动生成 arange(seq_len) + past_seen_tokens
       ├─ position_embeddings = self.rotary_emb(hidden_states, position_ids)  # 计算一次
       ├─ create_causal_mask(..., position_ids=position_ids)  ← ⚠️ 关键交互点
       └─ for layer in self.layers:
            layer(..., position_embeddings=(cos, sin))
              └─ self.self_attn(..., position_embeddings=...)
                   └─ apply_rotary_pos_emb(q, k, cos, sin)
```

RoPE 的 cos/sin 在 `Qwen2Model` 层面只计算一次，然后传递给所有 decoder layer。

### 1.4 ⚠️ 关键风险：packed sequence 检测

`create_causal_mask` 内部调用 `find_packed_sequence_indices(position_ids)`：

```python
def find_packed_sequence_indices(position_ids):
    first_dummy_value = position_ids[:, :1] - 1
    position_diff = torch.diff(position_ids, prepend=first_dummy_value, dim=-1)
    packed_sequence_mask = (position_diff != 1).cumsum(-1)
    if (packed_sequence_mask[:, -1] == 0).all():
        return None  # 正常递增，无需处理
    return packed_sequence_mask  # 非递增 → 视为 packed sequences
```

当 position 从 n 跳回 0 时，`position_diff = -n != 1`，系统将其视为**独立序列边界**，生成 mask 阻止跨序列 attention。

这意味着：**简单传入 turn-relative position_ids 会导致 turn 之间无法互相 attend**。

### 1.5 解决方案：预构建 4D attention mask

传入 4D attention mask（shape `[batch, 1, seq_len, seq_len]`）时，`create_causal_mask` 直接返回该 mask，跳过 packed sequence 检测：

```python
def build_tbab_causal_mask(seq_len, device, dtype=torch.bfloat16):
    """标准 causal mask，允许所有 turn 互相 attend"""
    mask = torch.zeros(1, 1, seq_len, seq_len, device=device, dtype=dtype)
    causal = torch.triu(torch.ones(seq_len, seq_len, device=device), diagonal=1).bool()
    mask.masked_fill_(causal, float('-inf'))
    return mask

# 使用
outputs = model(
    input_ids=input_ids,              # 或 inputs_embeds
    position_ids=custom_position_ids, # turn-relative positions
    attention_mask=build_tbab_causal_mask(seq_len, device),  # 4D mask
    labels=labels,
)
```

### 1.6 Qwen2.5-7B RoPE 参数（修正）

| 参数 | 实际值 | 备注 |
|------|--------|------|
| rope_theta | **1,000,000** | 非 10000，用大 base 替代 YaRN/NTK |
| head_dim | 128 | = 3584 / 28 |
| num_attention_heads | 28 | |
| num_key_value_heads | 4 | GQA |
| max_position_embeddings | 32768 | |
| rope_scaling | 无 | 默认 RoPE，无显式扩展 |

inv_freq 计算：`inv_freq = 1.0 / (1000000.0 ** (arange(0, 128, 2) / 128))`

> **对 TBAB 的影响**：rope_theta=1M 意味着高频分量衰减更慢，中频通道的"关闭"阈值对应的绝对 position 距离更大。需要重新评估频段恢复理论中的距离阈值。

---

## 2. Bridge Token 插入架构

### 2.1 相关工作参考

| 工作 | Token 类型 | 插入方式 | Position 处理 | Loss |
|------|-----------|---------|--------------|------|
| Prompt Tuning | Virtual tokens | Embedding 前置 | 递增 [0..V-1] | 不参与 |
| Prefix Tuning | Virtual KV | 每层 KV 前置 | 绕过 position | 不参与 |
| Pause Tokens (ICLR 2024) | `<pause>` | 词表扩展，input_ids 插入 | 标准递增 | 不参与 |
| Register Tokens (ICLR 2024) | `[reg]` | Patch embedding 后 | 与 [CLS] 一致 | 推理时丢弃 |
| Latent Tokens (2025) | Learnable vectors | Embedding 周期插入 | 共享后续 verbal token 的 pos | 不参与 |
| RMT (NeurIPS 2022) | Memory tokens | 序列首尾添加 | 标准递增 | 不参与 |

### 2.2 两条实现路径

#### 路径 A：词表扩展（MVP 推荐）

在 tokenizer 中注册 bridge token，通过 input_ids 插入，利用 PEFT `trainable_token_indices` 训练。

**优点**：与 HuggingFace Trainer/PEFT 无缝集成，自动保存/加载，代码量最少。
**缺点**：bridge token 进入了 LM head 的输出空间（但可通过 loss mask 避免影响）。

#### 路径 B：Embedding 层拼接

用独立 `nn.Parameter` 维护 bridge embeddings，在 embedding 空间拼接。

**优点**：完全隔离，不影响词表和 LM head。
**缺点**：需要手动管理 position_ids/attention_mask/labels 对齐，保存/加载需额外代码。

**MVP 推荐路径 A**，原因：实现简单，PEFT 原生支持，可快速验证核心假设。

### 2.3 Embedding 初始化策略

| 策略 | 做法 | 推荐度 |
|------|------|--------|
| 词表均值 + 扰动 | `mean(embed_tokens.weight) + N(0, 0.01)` | **主方案** |
| Random | `N(0, 0.02)` | 消融对比 |
| 复制 special token | 复制 `<\|im_end\|>` 的 embedding | 备选 |

词表均值初始化将 bridge token 放在 embedding 空间的语义中心，训练更稳定。加微小扰动保证 K=4 个 token 有多样性。

### 2.4 Bridge Tokens 不参与 Loss

所有相关工作一致：bridge token 位置的 label 设为 -100。

实现：在数据处理阶段直接构造 labels，bridge 位置填 -100，`CrossEntropyLoss(ignore_index=-100)` 自动跳过。

### 2.5 Bridge Token Position 策略

#### 推荐方案：Bridge 归属前一 Turn，Reset 在 Bridge 之后

```
Turn 1:  [<|im_start|> system \n content <|im_end|>]  positions: [0, 1, 2, ..., n]
Bridge:  [bridge_0, bridge_1, bridge_2, bridge_3]      positions: [n+1, n+2, n+3, n+4]
Turn 2:  [<|im_start|> user \n content <|im_end|>]     positions: [0, 1, 2, ..., m]
Bridge:  [bridge_0, bridge_1, bridge_2, bridge_3]      positions: [m+1, m+2, m+3, m+4]
Turn 3:  [<|im_start|> assistant \n content <|im_end|>] positions: [0, 1, 2, ..., p]
```

**理由**：
1. Bridge tokens 作为前一 turn 的"总结延伸"，与前 turn token 保持连续 RoPE 距离
2. Bridge 可以通过 causal attention 看到前一 turn 全部内容
3. Position reset 发生在 bridge 之后，后一 turn 的 token 到 bridge 的 RoPE 距离由 bridge 的绝对 position 和后一 turn token 的 position 共同决定（跨 turn 时通过 4D mask 保证可见性）
4. Bridge tokens 之间保持正常顺序（n+1..n+4），可以学习不同角色

#### 备选方案（消融对比）：Bridge 归属后一 Turn

```
Turn 1:  [... <|im_end|>]                              positions: [0, ..., n]
Bridge:  [bridge_0, bridge_1, bridge_2, bridge_3]      positions: [0, 1, 2, 3]
Turn 2:  [<|im_start|> user ...]                       positions: [4, 5, ..., 4+m]
```

Bridge 作为新 turn 的前缀，后续 content 从 position K 开始。后续 token 到 bridge 的 RoPE 距离很短（K=4），直接利用频段恢复。

---

## 3. LoRA 集成

### 3.1 Qwen2.5-7B Linear Layer 命名

| 模块 | Layer 名称 |
|------|-----------|
| Attention | `self_attn.q_proj`, `self_attn.k_proj`, `self_attn.v_proj`, `self_attn.o_proj` |
| MLP (SwiGLU) | `mlp.gate_proj`, `mlp.up_proj`, `mlp.down_proj` |

### 3.2 推荐 LoRA 配置

```python
lora_config = LoraConfig(
    r=32,
    lora_alpha=64,            # alpha = 2r
    target_modules="all-linear",  # 全部 7 个 linear layers
    lora_dropout=0.05,
    task_type="CAUSAL_LM",
    trainable_token_indices=bridge_token_ids,  # 只训练 4 个 bridge token 的 embedding
)
```

| 配置 | target_modules | 可训练参数（r=32） |
|------|---------------|------------------|
| 仅 QV | `["q_proj", "v_proj"]` | ~13M |
| 全 Attention | `["q_proj", "k_proj", "v_proj", "o_proj"]` | ~26M |
| **全 Linear（推荐）** | `"all-linear"` | ~46M |

全 linear 参数量仍 <1% 原模型，QLoRA 论文已证明其接近全量微调效果。

### 3.3 Bridge Embeddings 与 LoRA 共存方案

**推荐：PEFT `trainable_token_indices`（原生支持）**

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import LoraConfig, get_peft_model

model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen2.5-7B-Instruct", torch_dtype=torch.bfloat16)
tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-7B-Instruct")

# 注册 bridge tokens
bridge_tokens = ["<|bridge_0|>", "<|bridge_1|>", "<|bridge_2|>", "<|bridge_3|>"]
tokenizer.add_special_tokens({"additional_special_tokens": bridge_tokens})
model.resize_token_embeddings(len(tokenizer))
bridge_token_ids = tokenizer.convert_tokens_to_ids(bridge_tokens)

# LoRA + trainable bridge tokens
lora_config = LoraConfig(
    r=32,
    lora_alpha=64,
    target_modules="all-linear",
    lora_dropout=0.05,
    task_type="CAUSAL_LM",
    trainable_token_indices=bridge_token_ids,
)
model = get_peft_model(model, lora_config)
model.print_trainable_parameters()
```

PEFT 内部通过 `TrainableTokensModel` 自动处理：
- 被指定的 token indices 的 embedding `requires_grad=True`，其余冻结
- 保存时只保存这 4 个 token 的 embedding delta，不保存整个 embedding 矩阵
- 加载时自动恢复

**对比 `modules_to_save=["embed_tokens", "lm_head"]`**：会保存整个 embedding 矩阵（Qwen2.5 vocab ~152K，约 2GB），不推荐。

### 3.4 保存与加载

```python
# 保存（LoRA weights + bridge token embeddings 自动一起保存）
model.save_pretrained("output_dir")
tokenizer.save_pretrained("output_dir")

# 加载
from peft import PeftModel
base_model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen2.5-7B-Instruct")
tokenizer = AutoTokenizer.from_pretrained("output_dir")
base_model.resize_token_embeddings(len(tokenizer))  # 必须先 resize
model = PeftModel.from_pretrained(base_model, "output_dir")
```

---

## 4. 数据格式

### 4.1 Qwen2.5 Chat Template (ChatML)

特殊 token：

| Token | ID | 用途 |
|-------|------|------|
| `<\|endoftext\|>` | 151643 | pad_token |
| `<\|im_start\|>` | 151644 | turn 开始 |
| `<\|im_end\|>` | 151645 | turn 结束，eos_token |

多轮格式：
```
<|im_start|>system
You are a helpful assistant.<|im_end|>
<|im_start|>user
第一轮用户输入<|im_end|>
<|im_start|>assistant
第一轮助手回复<|im_end|>
<|im_start|>user
第二轮用户输入<|im_end|>
<|im_start|>assistant
```

### 4.2 Turn 边界识别

```python
IM_START_ID = 151644
IM_END_ID = 151645

def find_turn_boundaries(input_ids):
    """返回每个 <|im_end|> 的位置索引"""
    return [i for i, tid in enumerate(input_ids) if tid == IM_END_ID]
```

### 4.3 Bridge Token 插入方案

**推荐：tokenization 之后修改 input_ids（方案 B）**

先正常 tokenize，再在 `<|im_end|>` 之后插入 bridge token IDs：

```python
def insert_bridge_tokens(input_ids, bridge_ids, im_end_id=151645):
    """在每个 <|im_end|> 之后插入 bridge tokens（最后一个 turn 除外）"""
    new_ids = []
    im_end_positions = [i for i, tid in enumerate(input_ids) if tid == im_end_id]
    last_im_end = im_end_positions[-1] if im_end_positions else -1

    for i, tid in enumerate(input_ids):
        new_ids.append(tid)
        if tid == im_end_id and i != last_im_end:
            new_ids.extend(bridge_ids)
    return new_ids
```

### 4.4 完整数据处理 Pipeline

```python
import torch
from torch.utils.data import Dataset

IGNORE_INDEX = -100
IM_START_ID = 151644
IM_END_ID = 151645

class TBABDataset(Dataset):
    def __init__(self, conversations, tokenizer, max_length=4096, num_bridge=4):
        self.conversations = conversations
        self.tokenizer = tokenizer
        self.max_length = max_length
        self.num_bridge = num_bridge
        self.bridge_ids = tokenizer.convert_tokens_to_ids(
            [f"<|bridge_{i}|>" for i in range(num_bridge)]
        )

    def __len__(self):
        return len(self.conversations)

    def __getitem__(self, idx):
        conv = self.conversations[idx]

        # Step 1: 正常 tokenize
        input_ids = self.tokenizer.apply_chat_template(
            conv, tokenize=True, add_generation_prompt=False
        )

        # Step 2: 解析 turn 结构
        turns = self._split_into_turns(input_ids)
        role_sequence = [msg["role"] for msg in conv]

        # Step 3: 插入 bridge tokens + 构造 position_ids + labels
        new_input_ids = []
        position_ids = []
        labels = []

        for turn_idx, turn_tokens in enumerate(turns):
            is_assistant = (turn_idx < len(role_sequence)
                           and role_sequence[turn_idx] == "assistant")

            # Bridge tokens（非第一个 turn 且非最后一个 turn 之后）
            if turn_idx > 0:
                # Bridge tokens 归属后一 turn，position [0..K-1]
                # 或归属前一 turn（见 §2.5 讨论）
                for k, bid in enumerate(self.bridge_ids):
                    new_input_ids.append(bid)
                    position_ids.append(k)
                    labels.append(IGNORE_INDEX)

            # Turn content
            turn_start_pos = self.num_bridge if turn_idx > 0 else 0
            for j, tid in enumerate(turn_tokens):
                new_input_ids.append(tid)
                position_ids.append(turn_start_pos + j)
                if is_assistant and tid != IM_START_ID:
                    labels.append(tid)
                else:
                    labels.append(IGNORE_INDEX)

        # Step 4: 截断
        new_input_ids = new_input_ids[:self.max_length]
        position_ids = position_ids[:self.max_length]
        labels = labels[:self.max_length]
        seq_len = len(new_input_ids)

        # Step 5: 构建 4D causal mask（绕过 packed sequence 检测）
        causal_mask = torch.zeros(1, seq_len, seq_len)
        causal_upper = torch.triu(torch.ones(seq_len, seq_len), diagonal=1).bool()
        causal_mask.masked_fill_(causal_upper, float('-inf'))

        return {
            "input_ids": torch.tensor(new_input_ids, dtype=torch.long),
            "position_ids": torch.tensor(position_ids, dtype=torch.long),
            "labels": torch.tensor(labels, dtype=torch.long),
            "attention_mask": causal_mask,  # 4D: [1, seq_len, seq_len]
        }

    def _split_into_turns(self, input_ids):
        """按 <|im_start|>...<|im_end|> 分割为 turn segments"""
        turns = []
        current = []
        for tid in input_ids:
            if tid == IM_START_ID and current:
                turns.append(current)
                current = [tid]
            else:
                current.append(tid)
        if current:
            turns.append(current)
        return turns
```

### 4.5 Data Collator

```python
from dataclasses import dataclass
from typing import Dict, List

@dataclass
class TBABDataCollator:
    tokenizer: object
    max_length: int = 4096

    def __call__(self, features: List[Dict]) -> Dict[str, torch.Tensor]:
        batch_size = len(features)
        max_len = min(
            max(f["input_ids"].shape[0] for f in features),
            self.max_length
        )

        input_ids = torch.full((batch_size, max_len),
                               self.tokenizer.pad_token_id, dtype=torch.long)
        position_ids = torch.zeros(batch_size, max_len, dtype=torch.long)
        labels = torch.full((batch_size, max_len), IGNORE_INDEX, dtype=torch.long)
        # 4D mask: [batch, 1, max_len, max_len]
        attention_mask = torch.full((batch_size, 1, max_len, max_len), float('-inf'))

        for i, feat in enumerate(features):
            sl = min(feat["input_ids"].shape[0], max_len)
            input_ids[i, :sl] = feat["input_ids"][:sl]
            position_ids[i, :sl] = feat["position_ids"][:sl]
            labels[i, :sl] = feat["labels"][:sl]
            # 复制 causal mask 到对应区域
            attention_mask[i, 0, :sl, :sl] = feat["attention_mask"][0, :sl, :sl]

        return {
            "input_ids": input_ids,
            "position_ids": position_ids,
            "labels": labels,
            "attention_mask": attention_mask,
        }
```

### 4.6 Labels 处理规则

| 位置类型 | label |
|---------|-------|
| system turn | -100 |
| user turn | -100 |
| assistant turn content | 真实 token ID |
| `<\|im_start\|>` + role | -100 |
| `<\|im_end\|>` (assistant) | 保留（学习生成 EOS） |
| bridge tokens | -100 |
| padding | -100 |

### 4.7 Position IDs 完整示例

3-turn 对话（system + user + assistant），K=4，bridge 归属后一 turn 方案：

```
Tokens:     [<|im_start|> system \n content <|im_end|>]
Positions:  [0            1      2 3...     n         ]
Labels:     [-100         -100   ...        -100      ]

            [bridge_0 bridge_1 bridge_2 bridge_3] [<|im_start|> user \n content <|im_end|>]
            [0        1        2        3       ] [4            5    6 7...     4+m       ]
            [-100     -100     -100     -100    ] [-100         -100 ...       -100       ]

            [bridge_0 bridge_1 bridge_2 bridge_3] [<|im_start|> assistant \n content <|im_end|>]
            [0        1        2        3       ] [4            5         6 7...     4+p       ]
            [-100     -100     -100     -100    ] [-100         -100      ...tok...  tok       ]
```

---

## 5. 训练集成

### 5.1 完整训练脚本骨架

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments, Trainer
from peft import LoraConfig, get_peft_model

# 1. 加载模型
model = AutoModelForCausalLM.from_pretrained(
    "Qwen/Qwen2.5-7B-Instruct",
    torch_dtype=torch.bfloat16,
    device_map="auto",
)
tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-7B-Instruct")

# 2. 注册 bridge tokens
NUM_BRIDGE = 4
bridge_tokens = [f"<|bridge_{i}|>" for i in range(NUM_BRIDGE)]
tokenizer.add_special_tokens({"additional_special_tokens": bridge_tokens})
model.resize_token_embeddings(len(tokenizer))

# 初始化 bridge token embeddings（词表均值 + 扰动）
with torch.no_grad():
    vocab_mean = model.model.embed_tokens.weight[:-NUM_BRIDGE].mean(dim=0)
    for i in range(NUM_BRIDGE):
        model.model.embed_tokens.weight[-(NUM_BRIDGE - i)] = \
            vocab_mean + torch.randn_like(vocab_mean) * 0.01

bridge_token_ids = tokenizer.convert_tokens_to_ids(bridge_tokens)

# 3. LoRA + trainable bridge tokens
lora_config = LoraConfig(
    r=32,
    lora_alpha=64,
    target_modules="all-linear",
    lora_dropout=0.05,
    task_type="CAUSAL_LM",
    trainable_token_indices=bridge_token_ids,
)
model = get_peft_model(model, lora_config)
model.print_trainable_parameters()

# 4. 数据
dataset = TBABDataset(conversations, tokenizer, max_length=4096, num_bridge=NUM_BRIDGE)
collator = TBABDataCollator(tokenizer=tokenizer, max_length=4096)

# 5. 训练
training_args = TrainingArguments(
    output_dir="./tbab_output",
    per_device_train_batch_size=2,
    gradient_accumulation_steps=8,
    learning_rate=2e-4,
    num_train_epochs=3,
    lr_scheduler_type="cosine",
    bf16=True,
    logging_steps=10,
    save_steps=500,
    remove_unused_columns=False,  # 保留 position_ids
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset,
    data_collator=collator,
)
trainer.train()

# 6. 保存
model.save_pretrained("./tbab_adapter")
tokenizer.save_pretrained("./tbab_adapter")
```

### 5.2 关键注意事项

1. **`remove_unused_columns=False`**：必须设置，否则 Trainer 自动移除 `position_ids`
2. **4D attention mask**：必须传入，否则 position reset 触发 packed sequence 检测
3. **Bridge token 初始化**：`resize_token_embeddings` 默认用 random init，需要手动覆盖为词表均值
4. **`trainable_token_indices` 与 `modules_to_save`**：不能同时对 embed_tokens 使用两者，会报 ValueError

---

## 6. 潜在风险与注意事项

### 6.1 rope_theta=1M 对频段恢复理论的影响

原始分析假设 rope_theta=10000，但 Qwen2.5 使用 1,000,000。这意味着：
- 高频分量衰减更慢，中频通道"关闭"对应的 position 距离更大
- 频段恢复效果可能在更长的对话中才显著
- **需要重新计算频段分析**：`inv_freq = 1/(1M^(2i/128))`，各频段的半波长和衰减曲线与 base=10000 时差异很大

### 6.2 4D Attention Mask 的显存开销

4D mask shape = `[batch, 1, seq_len, seq_len]`，当 seq_len=4096 时：
- bf16: 4096^2 * 2 bytes = 32MB per sample
- batch=2: 64MB

对于长序列训练可能成为瓶颈。可考虑：
- 使用 Flash Attention 2 的 block-sparse mask 替代
- 检查是否可以修改 `find_packed_sequence_indices` 的判断逻辑（需要 monkey-patch transformers）

### 6.3 KV Cache 推理兼容性

推理时需要特殊处理：
- 每个 turn 结束后插入 bridge tokens 并计算其 KV cache
- 新 turn 的 position_ids 需要 reset
- 需要自定义 `generate()` 逻辑或使用 `model.forward()` 手动解码

### 6.4 梯度流

bridge token embeddings 的梯度通过以下路径回传：
```
loss → logits → transformer layers → attention(Q, K_with_bridge, V_with_bridge) → bridge embeddings
```
需要验证梯度不为零且数值稳定（特别是只有 4 个参数时，梯度可能很大或很小）。

### 6.5 FlashAttention 兼容性

FlashAttention 2 对 4D custom attention mask 的支持取决于 transformers 版本。需要确认：
- `transformers >= 4.43` 支持 FA2 + 4D mask
- 或者禁用 FA2，使用 SDPA（`attn_implementation="sdpa"`）

---

## 7. MVP 实现路径

按最小改动量排序的实现步骤：

### Phase 1: 验证 position_ids 操控（0.5 天）

1. 加载 Qwen2.5-7B，构造一个简单的 2-turn 输入
2. 传入 turn-relative position_ids + 4D causal mask
3. 验证 forward pass 正常运行、logits 合理
4. 对比标准 position_ids 的 logits 差异

### Phase 2: 数据处理 pipeline（1 天）

1. 实现 `TBABDataset`：chat template tokenization + bridge token 插入 + position_ids 构造
2. 实现 `TBABDataCollator`：4D mask batch 处理
3. 用小数据集验证 data loading 正确性

### Phase 3: 训练（1 天）

1. LoRA + trainable_token_indices 配置
2. Bridge token embedding 初始化（词表均值）
3. 小规模训练验证 loss 下降
4. 检查 bridge token embedding 的梯度和更新

### Phase 4: 评估与消融（2 天）

1. 对比实验：有/无 bridge tokens、有/无 position reset
2. 消融：bridge position 策略（归属前 turn vs 后 turn）
3. 消融：bridge 数量（K=1,2,4,8）
4. 频段分析：RoPE 频率响应在 reset 前后的变化

---

## 附录 A：参考资源

- [Qwen2.5-7B-Instruct config.json](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct/blob/main/config.json)
- [modeling_qwen2.py](https://github.com/huggingface/transformers/blob/main/src/transformers/models/qwen2/modeling_qwen2.py)
- [masking_utils.py](https://github.com/huggingface/transformers/blob/main/src/transformers/masking_utils.py)
- [PEFT trainable_token_indices](https://github.com/huggingface/peft)
- [Pause Tokens (ICLR 2024)](https://arxiv.org/abs/2310.02226)
- [Register Tokens (ICLR 2024)](https://arxiv.org/abs/2309.16588)
- [Latent Tokens (2025)](https://arxiv.org/html/2505.12629v1)
- [Recurrent Memory Transformer (NeurIPS 2022)](https://github.com/booydar/LM-RMT)
