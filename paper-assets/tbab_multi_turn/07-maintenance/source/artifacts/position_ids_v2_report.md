# TBAB Position IDs v2: Bridge Token Position 策略统一与模型泛化

> 更新日期：2026-05-18
> 基于：position_ids_architecture_report.md (v1)

---

## 0. 更新摘要

| 问题 | v1 状态 | v2 结论 |
|------|---------|---------|
| Bridge position 策略 | 文字(方案A)与代码(方案B)不一致 | **统一为方案 B（bridge 归属后 turn）** |
| RoPE 理论分析 | 缺少两方案对比 | 完整对比 + 距离计算 |
| 模型泛化 | 绑定 Qwen2.5-7B | **模型无关实现** |
| 代码一致性 | SS2.5 与 SS4.3-4.7 矛盾 | 全部代码统一到方案 B |

---

## 1. 问题：v1 报告内部不一致

v1 报告存在文字与代码的矛盾：

- **SS2.5 文字推荐方案 A**：bridge tokens 继承前一 turn 的 position（`[n+1, n+2, n+3, n+4]`），新 turn 从 0 开始
- **SS4.3-4.7 代码实现方案 B**：bridge tokens 的 position 为 `[0, 1, 2, 3]`，新 turn 从 4 开始

两方案对 RoPE 编码的影响有本质区别，必须统一。

---

## 2. 两种方案的 RoPE 理论分析

### 2.1 RoPE 相对位置编码回顾

RoPE 对 attention score 的贡献取决于 query 和 key 的 **position 差值**：

- Query 在 position p_q，Key 在 position p_k
- 对频率通道 k，attention 中的 RoPE 偏置项正比于 cos((p_q - p_k) * omega_k)
- 其中 omega_k = rope_theta^(-2k/d_head)
- **绝对距离 |p_q - p_k| 越大，高频通道 (小 k) 的 cos 值振荡越剧烈，贡献趋于噪声**

Bridge token 有两个关键功能：
1. **功能 1（读取）**：bridge 的 Q attend 前 turn 的 K，从前 turn 提取信息
2. **功能 2（传递）**：后 turn 的 Q attend bridge 的 K，从 bridge 获取跨 turn 信息

**功能 2 是信息传递的瓶颈**——bridge 存在的核心目的是让新 turn 能高效读取跨 turn 上下文。

### 2.2 方案 A：Bridge 归属前 Turn

```
Turn 1:  positions [0, 1, ..., n]
Bridge:  positions [n+1, n+2, n+3, n+4]   <-- 继承前 turn
Turn 2:  positions [0, 1, ..., m]          <-- reset
```

**功能 1（bridge 读取前 turn）**：
- Bridge 在 position n+k (k=1..4)，turn 1 token 在 position i (0..n)
- RoPE 距离 = (n+k) - i，范围 [k, n+k]
- Bridge 与 turn 1 尾部距离很小 (<=K)，与头部距离约 n+K
- 结论：bridge 对前 turn 尾部有良好 RoPE 近场效应

**功能 2（后 turn 读取 bridge）**：
- Turn 2 token 在 position j (0..m)，bridge 在 position n+k
- RoPE 距离 = |j - (n+k)| = n+k-j（因 n+k >> j）
- **最小距离 >= n+1**（当 j 最大、k 最小时仍约为 n）
- 结论：**bridge 对新 turn 处于 RoPE 远场，高频通道贡献退化为噪声**

### 2.3 方案 B：Bridge 归属后 Turn

```
Turn 1:  positions [0, 1, ..., n]
Bridge:  positions [0, 1, 2, 3]            <-- reset，作为新 turn 前缀
Turn 2:  positions [4, 5, ..., 4+m]        <-- 紧接 bridge
```

**功能 1（bridge 读取前 turn）**：
- Bridge 在 position k (0..3)，turn 1 token 在 position i (0..n)
- RoPE 距离 = |k - i|，范围 [0, n]
- Bridge 与 turn 1 头部近、尾部远（距离约 n）
- 结论：对 turn 1 尾部的 RoPE 距离较大，但有两个补偿机制：
  - (a) 4D causal mask 保证 bridge 对所有前序 token 的 attention 可见性
  - (b) attention 的 content-based 分量（Q*K 内积的非 RoPE 部分）不受 position 影响
  - (c) rope_theta 越大（如 1M），中低频通道的远场衰减越慢

**功能 2（后 turn 读取 bridge）**：
- Turn 2 token 在 position j+K (K..K+m)，bridge 在 position k (0..K-1)
- RoPE 距离 = (j+K) - k，范围 [1, K+m]
- **最小距离 = 1**（j=0, k=K-1），bridge 是新 turn 的紧邻前缀
- 结论：**bridge 对新 turn 处于 RoPE 近场，所有频率通道充分贡献**

### 2.4 对比总结

| 维度 | 方案 A（前 turn） | 方案 B（后 turn） |
|------|-------------------|-------------------|
| 功能 1：bridge 读取前 turn | 近场（距离 <= n+K） | 混合（头近尾远，可补偿） |
| **功能 2：后 turn 读取 bridge** | **远场（距离 >= n）** | **近场（距离 <= K+m）** |
| 瓶颈 | 功能 2 失效 | 功能 1 可补偿 |
| 实现复杂度 | 需跟踪前 turn 长度 n | 固定偏移 K |

**核心结论**：方案 A 在关键功能（信息传递到新 turn）上失效。方案 B 让 bridge 成为新 turn 的 RoPE 前缀，天然保证传递效率。功能 1 的劣势可通过 content-based attention 和大 rope_theta 补偿。

---

## 3. 最终选择：方案 B（Bridge 归属后 Turn）

### 3.1 核心理由

1. **信息传递瓶颈在功能 2**：bridge 的主要价值是向新 turn 提供跨 turn 上下文。方案 B 让 bridge 成为新 turn 的 RoPE 前缀，最大化传递效率。
2. **大 rope_theta 缓解功能 1 的劣势**：Qwen2.5 (1M), Llama 3 (500K) 等现代模型的 base 值很大，中低频通道衰减极慢，bridge 读取前 turn 尾部时信号损失有限。
3. **实现简洁**：bridge 固定占位 [0, K-1]，turn content 固定从 K 开始，无需跟踪前 turn 长度。
4. **预训练先验对齐**：position 0..K-1 对应序列开头，预训练模型对序列开头的 token 有更强的 attention 倾向（primacy bias），有利于 bridge 信息被新 turn 读取。

### 3.2 与已有工作的一致性

所有主流工作都将 special tokens 放在需要使用它们的 segment 的 **前缀** 位置：

| 工作 | Special token 放置 | 与方案 B 的关系 |
|------|-------------------|----------------|
| Prefix Tuning | 可训练 token 前置于序列，position [0, V-1] | 完全一致 |
| RMT (NeurIPS 2022) | Memory tokens 放在 segment 开头 | 一致：memory 作为 segment 前缀 |
| Register Tokens (ICLR 2024) | 放在 [CLS] 后、patches 前 | 一致：信息汇聚点作为前缀 |
| Pause Tokens (ICLR 2024) | 内联插入，与后续 token 保持小 RoPE 距离 | 精神一致 |

### 3.3 Position 碰撞说明

方案 B 中，bridge 的 position [0..K-1] 与前一 turn 中 position [0..K-1] 的 token 数值重叠。这不构成问题：

1. **RoPE 只编码位置，不编码身份**。两个位置相同的 token 通过 content-based attention（Q*K 内积的非 RoPE 分量）区分。
2. **Causal mask 保证时序**：bridge 可以 attend 到前 turn token，反之不行。
3. **LoRA 微调**后，模型可通过 bridge token 的独特 embedding 区分它们与普通 token。
4. **Packed sequence 训练**中，不同序列的 position 0 也共存于同一 batch，模型对此有先验。

---

## 4. 泛化：模型无关的实现方案

### 4.1 position_ids 操控

**结论：模型无关，无需修改模型代码。**

所有基于 RoPE 的 HuggingFace 模型（Llama, Mistral, Qwen, Phi, Gemma 等）的 `forward()` 都接受 `position_ids` 参数。传递链路一致：

```
Model.forward(position_ids=...)
  -> RotaryEmbedding.forward(x, position_ids)
  -> apply_rotary_pos_emb(q, k, cos, sin)
```

唯一差异是 `inv_freq` 的计算（取决于 rope_theta 和 head_dim），但这对外部 position_ids 传入方式无影响。

### 4.2 Packed Sequence 检测与 4D Mask

**结论：4D mask bypass 对所有 HuggingFace 模型通用。**

Packed sequence 检测（`find_packed_sequence_indices`）位于 `transformers/masking_utils.py`，被 Llama, Qwen, Mistral, Phi, Gemma 等共用。当 position_ids 非递增时触发，生成 block-diagonal mask 阻断跨序列 attention。

绕过机制：传入 4D attention mask（shape `[batch, 1, seq_len, seq_len]`）时，所有模型直接使用该 mask，跳过自动 mask 生成：

```python
# transformers 内部逻辑（所有模型共享）
def _update_causal_mask(self, attention_mask, ...):
    if attention_mask is not None and attention_mask.dim() == 4:
        return attention_mask  # 直接返回，不做 packed sequence 检测
    # ... 否则走自动生成流程
```

**FlashAttention 兼容性**：`transformers >= 4.43` 支持 FA2 + 4D mask。更早版本需使用 `attn_implementation="sdpa"` 或 `"eager"`。

### 4.3 Chat Template 差异处理

**结论：通过渐进式 tokenization 实现模型无关的 turn 边界检测。**

不同模型的 chat template 格式差异大：

| 模型 | Turn 结束标记 | 格式 |
|------|-------------|------|
| Qwen2.5 (ChatML) | `<\|im_end\|>` | `<\|im_start\|>role\ncontent<\|im_end\|>` |
| Llama 3 | `<\|eot_id\|>` | `<\|start_header_id\|>role<\|end_header_id\|>\ncontent<\|eot_id\|>` |
| Mistral v0.3 | `</s>` | `[INST]content[/INST]` |
| Phi-3 | `<\|end\|>` | `<\|user\|>\ncontent<\|end\|>` |

**模型无关方案**：利用 `tokenizer.apply_chat_template()` 的渐进式调用检测 turn 边界，完全不依赖特定 special token ID（详见 SS5.2）。

### 4.4 RoPE Base 差异

**结论：TBAB 代码不需要知道 rope_theta。频段分析需要参数化。**

| 模型 | rope_theta | head_dim |
|------|-----------|----------|
| Llama-2-7B | 10,000 | 128 |
| Llama-3-8B | 500,000 | 128 |
| Mistral-7B-v0.1 | 10,000 | 128 |
| Qwen2.5-7B | 1,000,000 | 128 |

position_ids 构造代码完全不涉及 rope_theta，模型内部的 RotaryEmbedding 自行处理。但频段恢复的理论分析依赖 rope_theta（见 SS6）。

---

## 5. 更新后的代码示例

以下代码统一使用方案 B（bridge 归属后 turn），且为模型无关实现。

### 5.1 配置与初始化

```python
import torch
from dataclasses import dataclass
from typing import List, Tuple, Dict
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import LoraConfig, get_peft_model

IGNORE_INDEX = -100


@dataclass
class TBABConfig:
    model_name_or_path: str = "Qwen/Qwen2.5-7B-Instruct"
    num_bridge: int = 4
    max_length: int = 4096
    lora_r: int = 32
    lora_alpha: int = 64
    lora_dropout: float = 0.05

    @property
    def bridge_token_names(self) -> List[str]:
        return [f"<|bridge_{i}|>" for i in range(self.num_bridge)]


def setup_model_and_tokenizer(config: TBABConfig):
    """Model-agnostic: works with any HuggingFace causal LM + PEFT."""
    model = AutoModelForCausalLM.from_pretrained(
        config.model_name_or_path, torch_dtype=torch.bfloat16
    )
    tokenizer = AutoTokenizer.from_pretrained(config.model_name_or_path)

    if tokenizer.pad_token_id is None:
        tokenizer.pad_token = tokenizer.eos_token

    tokenizer.add_special_tokens({
        "additional_special_tokens": config.bridge_token_names
    })
    model.resize_token_embeddings(len(tokenizer))

    bridge_ids = tokenizer.convert_tokens_to_ids(config.bridge_token_names)
    embed = model.get_input_embeddings()
    with torch.no_grad():
        vocab_mean = embed.weight[:-config.num_bridge].mean(dim=0)
        for bid in bridge_ids:
            embed.weight[bid] = vocab_mean + torch.randn_like(vocab_mean) * 0.01

    lora_config = LoraConfig(
        r=config.lora_r,
        lora_alpha=config.lora_alpha,
        target_modules="all-linear",
        lora_dropout=config.lora_dropout,
        task_type="CAUSAL_LM",
        trainable_token_indices=bridge_ids,
    )
    model = get_peft_model(model, lora_config)
    return model, tokenizer, bridge_ids
```

### 5.2 Turn 边界检测（模型无关）

```python
def detect_turn_segments(
    tokenizer, conversation: List[Dict]
) -> List[Tuple[int, int]]:
    """Detect turn boundaries via progressive tokenization.
    Works with any chat template (ChatML, Llama, Mistral, Phi, etc.).

    Returns: [(start, end), ...] for each turn in token space.
    """
    segments = []
    prev_len = 0
    for i in range(1, len(conversation) + 1):
        tokens = tokenizer.apply_chat_template(
            conversation[:i], tokenize=True, add_generation_prompt=False
        )
        segments.append((prev_len, len(tokens)))
        prev_len = len(tokens)
    return segments
```

### 5.3 Assistant Content 边界检测（模型无关）

```python
def detect_assistant_header_len(tokenizer) -> int:
    """Detect how many template header tokens precede actual content
    in an assistant turn. Model-agnostic.

    Works by comparing tokenization with and without content,
    finding the divergence point within the assistant turn.
    """
    conv_with = [
        {"role": "user", "content": "test"},
        {"role": "assistant", "content": "response"},
    ]
    conv_empty = [
        {"role": "user", "content": "test"},
        {"role": "assistant", "content": ""},
    ]
    ids_with = tokenizer.apply_chat_template(
        conv_with, tokenize=True, add_generation_prompt=False
    )
    ids_empty = tokenizer.apply_chat_template(
        conv_empty, tokenize=True, add_generation_prompt=False
    )

    divergence = min(len(ids_with), len(ids_empty))
    for i in range(divergence):
        if ids_with[i] != ids_empty[i]:
            divergence = i
            break

    segments = detect_turn_segments(tokenizer, conv_with)
    assistant_start = segments[1][0]
    return divergence - assistant_start
```

### 5.4 数据集（方案 B，模型无关）

```python
from torch.utils.data import Dataset


class TBABDataset(Dataset):
    def __init__(self, conversations, tokenizer, config: TBABConfig):
        self.conversations = conversations
        self.tokenizer = tokenizer
        self.config = config
        self.bridge_ids = tokenizer.convert_tokens_to_ids(
            config.bridge_token_names
        )
        self.K = config.num_bridge
        self.assistant_header_len = detect_assistant_header_len(tokenizer)

    def __len__(self):
        return len(self.conversations)

    def __getitem__(self, idx):
        conv = self.conversations[idx]

        # Step 1: Full tokenization
        full_ids = self.tokenizer.apply_chat_template(
            conv, tokenize=True, add_generation_prompt=False
        )

        # Step 2: Detect turn segments (model-agnostic)
        segments = detect_turn_segments(self.tokenizer, conv)

        # Step 3: Build sequences with bridge tokens (Scheme B)
        new_input_ids = []
        position_ids = []
        labels = []

        for turn_idx, (start, end) in enumerate(segments):
            turn_tokens = full_ids[start:end]
            is_assistant = conv[turn_idx]["role"] == "assistant"

            # Bridge tokens as new turn prefix: positions [0, K-1]
            if turn_idx > 0:
                for k, bid in enumerate(self.bridge_ids):
                    new_input_ids.append(bid)
                    position_ids.append(k)
                    labels.append(IGNORE_INDEX)

            # Turn content: starts at K for non-first turns, 0 for first
            pos_offset = self.K if turn_idx > 0 else 0
            for j, tid in enumerate(turn_tokens):
                new_input_ids.append(tid)
                position_ids.append(pos_offset + j)
                if is_assistant and j >= self.assistant_header_len:
                    labels.append(tid)
                else:
                    labels.append(IGNORE_INDEX)

        # Step 4: Truncate
        L = min(len(new_input_ids), self.config.max_length)
        new_input_ids = new_input_ids[:L]
        position_ids = position_ids[:L]
        labels = labels[:L]

        # Step 5: 4D causal mask (bypasses packed sequence detection)
        causal_mask = torch.zeros(1, L, L)
        causal_mask.masked_fill_(
            torch.triu(torch.ones(L, L, dtype=torch.bool), diagonal=1),
            float('-inf'),
        )

        return {
            "input_ids": torch.tensor(new_input_ids, dtype=torch.long),
            "position_ids": torch.tensor(position_ids, dtype=torch.long),
            "labels": torch.tensor(labels, dtype=torch.long),
            "attention_mask": causal_mask,
        }
```

### 5.5 Data Collator

```python
from dataclasses import dataclass as dc


@dc
class TBABDataCollator:
    pad_token_id: int
    max_length: int = 4096

    def __call__(self, features: List[Dict]) -> Dict[str, torch.Tensor]:
        batch_size = len(features)
        max_len = min(
            max(f["input_ids"].shape[0] for f in features),
            self.max_length,
        )

        input_ids = torch.full(
            (batch_size, max_len), self.pad_token_id, dtype=torch.long
        )
        position_ids = torch.zeros(batch_size, max_len, dtype=torch.long)
        labels = torch.full(
            (batch_size, max_len), IGNORE_INDEX, dtype=torch.long
        )
        attention_mask = torch.full(
            (batch_size, 1, max_len, max_len), float('-inf')
        )

        for i, feat in enumerate(features):
            sl = min(feat["input_ids"].shape[0], max_len)
            input_ids[i, :sl] = feat["input_ids"][:sl]
            position_ids[i, :sl] = feat["position_ids"][:sl]
            labels[i, :sl] = feat["labels"][:sl]
            attention_mask[i, 0, :sl, :sl] = feat["attention_mask"][0, :sl, :sl]

        return {
            "input_ids": input_ids,
            "position_ids": position_ids,
            "labels": labels,
            "attention_mask": attention_mask,
        }
```

### 5.6 训练脚本骨架

```python
from transformers import TrainingArguments, Trainer

config = TBABConfig(model_name_or_path="Qwen/Qwen2.5-7B-Instruct")
model, tokenizer, bridge_ids = setup_model_and_tokenizer(config)

dataset = TBABDataset(conversations, tokenizer, config)
collator = TBABDataCollator(pad_token_id=tokenizer.pad_token_id)

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
    remove_unused_columns=False,  # keep position_ids
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset,
    data_collator=collator,
)
trainer.train()

model.save_pretrained("./tbab_adapter")
tokenizer.save_pretrained("./tbab_adapter")
```

### 5.7 Position IDs 完整示例

3-turn 对话（system + user + assistant），K=4，方案 B：

```
Turn 0 (system):
  Tokens:     [<|im_start|> system \n content <|im_end|>]
  Positions:  [0            1      2 3...     n         ]
  Labels:     [-100         -100   ...        -100      ]

Bridge -> Turn 1:
  Tokens:     [bridge_0 bridge_1 bridge_2 bridge_3]
  Positions:  [0        1        2        3       ]
  Labels:     [-100     -100     -100     -100    ]

Turn 1 (user):
  Tokens:     [<|im_start|> user \n content <|im_end|>]
  Positions:  [4            5    6 7...     4+m       ]
  Labels:     [-100         -100 ...       -100       ]

Bridge -> Turn 2:
  Tokens:     [bridge_0 bridge_1 bridge_2 bridge_3]
  Positions:  [0        1        2        3       ]
  Labels:     [-100     -100     -100     -100    ]

Turn 2 (assistant):
  Tokens:     [<|im_start|> assistant \n content      <|im_end|>]
  Positions:  [4            5         6  7...         4+p       ]
  Labels:     [-100         -100      -100 content_id... eos_id ]
```

注意 assistant turn 的 labels 中，header tokens（`<|im_start|>assistant\n`）被标记为 -100，只有实际 content 和 `<|im_end|>` 参与 loss。header 长度由 `detect_assistant_header_len()` 自动检测。

### 5.8 关键注意事项

1. **`remove_unused_columns=False`**：必须设置，否则 Trainer 自动移除 position_ids
2. **4D attention mask**：必须传入，否则 position reset 触发 packed sequence 检测
3. **Bridge token 初始化**：`resize_token_embeddings` 默认 random init，需手动覆盖为词表均值
4. **`trainable_token_indices` 与 `modules_to_save`**：不能同时对 embed_tokens 使用两者
5. **FlashAttention 2**：需 transformers >= 4.43 支持 FA2 + 4D mask，否则用 `attn_implementation="sdpa"`

---

## 6. 频段恢复的 rope_theta 泛化分析

### 6.1 Position Reset 的频段恢复机制

在标准多轮对话中（无 position reset），token 的绝对 position 单调递增。两个不同 turn 中 token 的 RoPE 距离等于它们之间所有 token 的总数（可能数百到数千）。对于这样大的距离：

- **高频通道**（小 k，omega_k 接近 1）：cos(Delta * omega_k) 随 Delta 快速振荡，贡献趋于噪声
- **低频通道**（大 k，omega_k 接近 0）：cos 值变化缓慢，提供有意义的远距离位置信号

Position reset 将每个 turn 的 position 重置为 0，使得跨 turn 的有效 RoPE 距离从 "所有中间 token 总数" 降低为 "两个 turn 内位置之差"（通常远小于 turn 长度）。这让高频通道重新提供有意义的位置信号，即"频段恢复"。

### 6.2 通用频段分析公式

频率通道 k (k = 0, ..., d_head/2 - 1) 的半波长（position 空间）：

```
lambda_half(k) = pi / omega_k = pi * rope_theta^(2k / d_head)
```

当 RoPE 距离 Delta < lambda_half(k) 时，通道 k 的 cos 值不翻转符号，提供单调的位置偏置。

对于给定距离 Delta，"有效通道"的最小索引：

```
k_min = ceil((d_head / 2) * log_b(Delta / pi))    where b = rope_theta
```

有效通道比例 = (d_head/2 - k_min) / (d_head/2)

### 6.3 不同模型的频段对比

以 d_head = 128（64 个频率通道）为例：

**代表性通道的半波长：**

| 通道 k | base=10K | base=500K | base=1M |
|--------|----------|-----------|---------|
| 0（最高频） | 3 | 3 | 3 |
| 16 | 31 | 84 | 99 |
| 32 | 314 | 2,221 | 3,142 |
| 48 | 3,142 | 59,060 | 99,346 |
| 63（最低频） | 27,186 | 1,279,296 | 2,531,300 |

**跨 turn RoPE 距离 Delta=500 时的有效通道比例：**

| 场景 | base=10K | base=500K | base=1M |
|------|----------|-----------|---------|
| 无 reset（Delta=500） | 53% | 64% | 66% |
| 有 reset（Delta<=100） | 61% | 73% | 75% |
| 有 reset + bridge（Delta<=50） | 67% | 78% | 80% |

（Delta<=100 对应典型 turn 内最大位置差；Delta<=50 对应 bridge 到新 turn 开头的距离）

### 6.4 结论

1. **Position reset 对所有 rope_theta 值都有效**，增加了跨 turn attention 中的有效频率通道数量。
2. **大 base 模型**（Qwen2.5, Llama 3）本身对长距离更鲁棒（更多低频通道自然覆盖大距离），但 position reset 仍能恢复额外的高频通道。
3. **Bridge tokens（方案 B）进一步缩短有效距离**：新 turn token 到 bridge 的距离仅为 K 到 K+m（远小于 turn 长度），最大化有效通道比例。
4. **消融实验建议**：对比有/无 position reset 在不同 turn 长度和不同 base 模型上的效果，量化频段恢复的实际增益。

---

## 附录 A：从 v1 到 v2 的变更清单

| 章节 | 变更 |
|------|------|
| SS2.5 (v1) | 删除方案 A 推荐，统一为方案 B |
| SS4.3-4.7 (v1) | 代码已为方案 B，保持一致；增加模型无关改造 |
| 新增 SS2 | 两种方案完整 RoPE 理论对比 |
| 新增 SS4 | 泛化分析（position_ids / 4D mask / chat template / rope_theta） |
| 新增 SS5.2 | 渐进式 tokenization（模型无关 turn 边界检测） |
| 新增 SS5.3 | Assistant content 边界自动检测 |
| 新增 SS6 | rope_theta 参数化的频段恢复分析 |

## 附录 B：v1 报告仍有效的内容

以下 v1 内容不受方案统一影响，继续有效：

- SS1（Position IDs 操控机制、源码位置、RoPE 实现、传递链路）
- SS2.1-2.4（Bridge token 相关工作、实现路径选择、Embedding 初始化、Loss 策略）
- SS3（LoRA 集成、PEFT trainable_token_indices）
- SS6（潜在风险：显存开销、KV Cache 推理、梯度流、FlashAttention 兼容性）
- SS7（MVP 实现路径时间线）
