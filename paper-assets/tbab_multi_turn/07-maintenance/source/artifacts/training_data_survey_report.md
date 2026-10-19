# 多轮对话训练数据调研报告

> 目标：为 TBAB MVP 训练筛选 2-3k 条 ≥5 turns（≥5 个 user 消息）的英文多轮对话，与评估集 lost_in_conversation 严格隔离。

---

## 1. 数据集参数对比表

| 数据集 | 样本量 | License | 语言 | 格式 | 平均 turns | 备注 |
|--------|--------|---------|------|------|-----------|------|
| **anon8231489123/ShareGPT_Vicuna_unfiltered** | ~53k | Apache 2.0 | EN only | JSON (`from`/`value`) | 变长 | 已过滤非英文、AI 说教 |
| **RyokoAI/ShareGPT52K** | ~90k | CC0 1.0 | EN + 多语 | JSON (raw HTML) | 变长 | 含 HTML 标签需清洗 |
| **shibing624/sharegpt_gpt4** | ~103k | CC-BY-4.0 | 多语 | JSONL | 变长 | 含 GPT-4 回复 |
| **stingning/ultrachat** | ~949k | MIT | EN | JSON (flat list) | 3-7 pairs | 合成数据，ChatGPT 生成 |
| **HuggingFaceH4/ultrachat_200k** | ~207k (SFT) | MIT | EN | Parquet (`role`/`content`) | 3-7 pairs | 已过滤清洗版本 |
| **lmsys/lmsys-chat-1m** | 1M | 受限 License | 154 语言 | Parquet (OpenAI format) | 平均 2.0 | 多数单轮，需要 license 协议 |
| **allenai/WildChat-1M** | ~838k | ODC-BY | 74 语言 | Parquet | 平均 2.52 | 41% 多轮，含毒性标注 |
| **OpenAssistant/oasst2** | ~70k trees | Apache 2.0 | 28 语言 | Parquet (树状) | 变长 | 需从树结构提取线性对话 |

---

## 2. ≥5 Turns 子集统计

### 定义
- 1 turn = 1 个 user 消息（即 1 个 user-assistant 交互对）
- ≥5 turns = 对话中至少包含 5 个 user 消息

### 各数据集估算

#### ShareGPT_Vicuna_unfiltered（推荐主力源）
- 总量：~53k 对话
- 预计 ≥5 turns 占比：**15-25%**（~8k-13k 条）
- 依据：ShareGPT 为真实用户对话，多数偏短（1-3 turns），但有相当比例的深度对话
- 优势：纯英文、已清洗、Apache 2.0

#### UltraChat 200k（推荐补充源）
- 总量：~207k（train_sft split）
- 对话结构：3-7 个 user-assistant pairs
- 预计 ≥5 turns 占比：**30-50%**（~62k-103k 条）
- 依据：UltraChat 设计时每段对话有 3-7 轮交互，5+ 轮的对话占比较高
- 优势：MIT license、已清洗、格式规范

#### UltraChat 原版
- 总量：~949k
- 预计 ≥5 turns 占比：**30-50%**（~285k-475k 条）
- 劣势：未清洗，存在低质量回复（"I do not have emotions" 等）

#### LMSYS-Chat-1M
- 平均 2.0 turns，多数为单轮
- 预计 ≥5 turns 占比：**<5%**（~50k 条，但需签 license 协议）
- 不推荐作为主力源

#### WildChat-1M
- 平均 2.52 turns，41% 多轮
- 预计 ≥5 turns 占比：**10-15%**（~84k-126k 条）
- 含毒性内容需额外过滤

#### OpenAssistant oasst2
- 树状结构，需提取线性路径
- 英文消息 ~85k，总树 ~70k
- 预计可提取 ≥5 turns 线性对话：**数千条**（依赖树的深度）
- 提取复杂度高，性价比低

### 小结

| 数据集 | 预计 ≥5 turns 数量 | 质量 | 推荐度 |
|--------|-------------------|------|--------|
| ShareGPT_Vicuna_unfiltered | 8k-13k | 高（真实对话） | ★★★★★ |
| UltraChat 200k | 62k-103k | 中高（合成但已清洗） | ★★★★☆ |
| WildChat-1M | 84k-126k | 中（需过滤毒性） | ★★★☆☆ |
| LMSYS-Chat-1M | ~50k | 高（真实对话） | ★★☆☆☆（license 受限） |
| oasst2 | 数千条 | 高 | ★★☆☆☆（提取复杂） |

---

## 3. 数据格式示例

### ShareGPT 格式（anon8231489123/ShareGPT_Vicuna_unfiltered）
```json
{
  "id": "abc123",
  "conversations": [
    {"from": "human", "value": "Can you explain how neural networks work?"},
    {"from": "gpt", "value": "Neural networks are computational models..."},
    {"from": "human", "value": "What about backpropagation?"},
    {"from": "gpt", "value": "Backpropagation is the algorithm..."},
    {"from": "human", "value": "How does gradient descent fit in?"},
    {"from": "gpt", "value": "Gradient descent is the optimization..."},
    {"from": "human", "value": "What are common activation functions?"},
    {"from": "gpt", "value": "The most common activation functions..."},
    {"from": "human", "value": "Can you compare ReLU vs Sigmoid?"},
    {"from": "gpt", "value": "ReLU and Sigmoid differ in..."}
  ]
}
```

### UltraChat 原版格式（stingning/ultrachat）
```json
{
  "id": "12345",
  "data": [
    "What are the key differences between Python and Java?",
    "Python and Java differ in several ways...",
    "Which one is better for machine learning?",
    "Python is generally preferred for ML because...",
    "What about performance-critical applications?",
    "For performance-critical applications, Java...",
    "Can you give me a code comparison?",
    "Sure, here is a comparison...",
    "How about their ecosystems?",
    "Both have extensive ecosystems..."
  ]
}
```

### UltraChat 200k 格式（HuggingFaceH4/ultrachat_200k）
```json
{
  "prompt": "What are the key differences between Python and Java?",
  "prompt_id": "d938b65dfe31f05f80eb8572964c6673",
  "messages": [
    {"role": "user", "content": "What are the key differences between Python and Java?"},
    {"role": "assistant", "content": "Python and Java differ in several ways..."},
    {"role": "user", "content": "Which one is better for machine learning?"},
    {"role": "assistant", "content": "Python is generally preferred for ML because..."},
    {"role": "user", "content": "What about performance-critical applications?"},
    {"role": "assistant", "content": "For performance-critical applications, Java..."}
  ]
}
```

---

## 4. 推荐的训练数据组成方案

### 方案：ShareGPT 为主 + UltraChat 200k 补充

| 来源 | 抽取数量 | 用途 |
|------|---------|------|
| ShareGPT_Vicuna_unfiltered (≥5 turns) | 1,500 条 | 真实多轮对话，质量高，多样性好 |
| UltraChat 200k (≥5 turns) | 1,000 条 | 补充话题覆盖，合成但质量可控 |
| **总计** | **2,500 条** | |

### 选择理由

1. **ShareGPT 为主**：真实用户对话，topic 多样性好，对话风格自然，训练出的模型泛化能力更强
2. **UltraChat 补充**：覆盖 ShareGPT 中较少出现的话题（写作、材料分析等），且格式已标准化
3. **不用 LMSYS-Chat-1M**：license 受限，且多数为单轮
4. **不用 WildChat**：需额外毒性过滤，增加预处理复杂度
5. **不用 oasst2**：树状结构提取复杂，收益有限

### 隔离检查

训练数据必须与 lost_in_conversation 评估集严格隔离。ShareGPT 和 UltraChat 均为独立数据源，与 lost_in_conversation 无数据重叠风险。但仍建议在预处理时做去重检查（基于 prompt 文本的 fuzzy matching）。

---

## 5. 预处理方案

### 5.1 筛选 ≥5 turns 对话

```python
from datasets import load_dataset

# === ShareGPT ===
def load_sharegpt_multi_turn(min_user_turns=5):
    ds = load_dataset("anon8231489123/ShareGPT_Vicuna_unfiltered", split="train")
    
    filtered = []
    for item in ds:
        convs = item["conversations"]
        user_turns = sum(1 for c in convs if c["from"] == "human")
        if user_turns >= min_user_turns:
            # 转换为统一格式
            messages = []
            for c in convs:
                role = "user" if c["from"] == "human" else "assistant"
                messages.append({"role": role, "content": c["value"]})
            filtered.append({
                "id": item.get("id", ""),
                "source": "sharegpt_vicuna",
                "messages": messages,
                "num_user_turns": user_turns
            })
    return filtered

# === UltraChat 200k ===
def load_ultrachat_multi_turn(min_user_turns=5):
    ds = load_dataset("HuggingFaceH4/ultrachat_200k", split="train_sft")
    
    filtered = []
    for item in ds:
        msgs = item["messages"]
        user_turns = sum(1 for m in msgs if m["role"] == "user")
        if user_turns >= min_user_turns:
            filtered.append({
                "id": item.get("prompt_id", ""),
                "source": "ultrachat_200k",
                "messages": msgs,
                "num_user_turns": user_turns
            })
    return filtered
```

### 5.2 统一格式转换

```python
def to_unified_format(conversations):
    """
    统一输出格式：
    [{"role": "user"|"assistant", "content": "..."}]
    """
    unified = []
    for conv in conversations:
        assert all("role" in m and "content" in m for m in conv["messages"])
        assert conv["messages"][0]["role"] == "user"
        # 确保 role 严格交替
        for i, m in enumerate(conv["messages"]):
            expected_role = "user" if i % 2 == 0 else "assistant"
            if m["role"] != expected_role:
                conv["messages"] = conv["messages"][:i]
                break
        unified.append(conv)
    return unified
```

### 5.3 Token 长度估算（Mistral-7B tokenizer）

```python
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-v0.1")

def estimate_token_lengths(conversations):
    lengths = []
    for conv in conversations:
        text = ""
        for m in conv["messages"]:
            text += f"<|{m['role']}|>\n{m['content']}\n"
        token_len = len(tokenizer.encode(text))
        lengths.append(token_len)
    return lengths

# 预期分布（基于经验估计）：
# ≥5 turns 对话的 token 长度：
# - P25: ~800 tokens
# - P50: ~1500 tokens  
# - P75: ~2500 tokens
# - P95: ~5000 tokens
# 建议截断阈值：4096 tokens（匹配 Mistral-7B 默认 context）
```

### 5.4 完整预处理 Pipeline

```python
import json
import random
from collections import Counter

def build_training_set(
    sharegpt_count=1500,
    ultrachat_count=1000,
    min_user_turns=5,
    max_tokens=4096,
    seed=42
):
    random.seed(seed)
    
    # Step 1: 加载和筛选
    sharegpt = load_sharegpt_multi_turn(min_user_turns)
    ultrachat = load_ultrachat_multi_turn(min_user_turns)
    
    print(f"ShareGPT ≥{min_user_turns} turns: {len(sharegpt)}")
    print(f"UltraChat ≥{min_user_turns} turns: {len(ultrachat)}")
    
    # Step 2: Token 长度过滤
    tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-v0.1")
    
    def filter_by_length(data, max_tok):
        result = []
        for conv in data:
            text = "\n".join(m["content"] for m in conv["messages"])
            if len(tokenizer.encode(text)) <= max_tok:
                result.append(conv)
        return result
    
    sharegpt = filter_by_length(sharegpt, max_tokens)
    ultrachat = filter_by_length(ultrachat, max_tokens)
    
    # Step 3: 随机采样
    sharegpt_sample = random.sample(sharegpt, min(sharegpt_count, len(sharegpt)))
    ultrachat_sample = random.sample(ultrachat, min(ultrachat_count, len(ultrachat)))
    
    # Step 4: 合并
    training_set = sharegpt_sample + ultrachat_sample
    random.shuffle(training_set)
    
    # Step 5: 统计
    turn_counts = [c["num_user_turns"] for c in training_set]
    print(f"\nFinal training set: {len(training_set)} conversations")
    print(f"Turn distribution: {Counter(turn_counts).most_common(10)}")
    
    # Step 6: 保存
    with open("training_data_multi_turn.json", "w") as f:
        json.dump(training_set, f, indent=2, ensure_ascii=False)
    
    return training_set

# 运行
training_set = build_training_set()
```

### 5.5 去重与隔离检查

```python
from datasketch import MinHash, MinHashLSH

def dedup_against_eval(training_set, eval_set, threshold=0.7):
    """
    用 MinHash LSH 检测训练集与评估集的近似重复。
    eval_set: lost_in_conversation 的对话列表。
    """
    lsh = MinHashLSH(threshold=threshold, num_perm=128)
    
    def text_to_minhash(text):
        m = MinHash(num_perm=128)
        for word in text.lower().split():
            m.update(word.encode("utf8"))
        return m
    
    # 索引评估集
    for i, conv in enumerate(eval_set):
        text = " ".join(m["content"] for m in conv["messages"])
        lsh.insert(f"eval_{i}", text_to_minhash(text))
    
    # 检查训练集
    clean = []
    removed = 0
    for conv in training_set:
        text = " ".join(m["content"] for m in conv["messages"])
        matches = lsh.query(text_to_minhash(text))
        if not matches:
            clean.append(conv)
        else:
            removed += 1
    
    print(f"Removed {removed} near-duplicates with eval set")
    return clean
```

---

## 6. 执行步骤总结

1. **下载数据集**：`load_dataset("anon8231489123/ShareGPT_Vicuna_unfiltered")` 和 `load_dataset("HuggingFaceH4/ultrachat_200k")`
2. **筛选 ≥5 user turns**：统计实际数量，验证估算
3. **格式统一**：转为 `[{"role": "user"|"assistant", "content": "..."}]`
4. **Token 长度过滤**：用 Mistral-7B tokenizer，截断 >4096 tokens
5. **随机采样**：ShareGPT 1500 + UltraChat 1000 = 2500 条
6. **去重检查**：与 lost_in_conversation 做 MinHash 近似去重
7. **保存**：输出 `training_data_multi_turn.json`

---

## 附录：数据集 HuggingFace 链接

- [anon8231489123/ShareGPT_Vicuna_unfiltered](https://huggingface.co/datasets/anon8231489123/ShareGPT_Vicuna_unfiltered)
- [RyokoAI/ShareGPT52K](https://huggingface.co/datasets/RyokoAI/ShareGPT52K)
- [shibing624/sharegpt_gpt4](https://huggingface.co/datasets/shibing624/sharegpt_gpt4)
- [stingning/ultrachat](https://huggingface.co/datasets/stingning/ultrachat)
- [HuggingFaceH4/ultrachat_200k](https://huggingface.co/datasets/HuggingFaceH4/ultrachat_200k)
- [lmsys/lmsys-chat-1m](https://huggingface.co/datasets/lmsys/lmsys-chat-1m)
- [allenai/WildChat-1M](https://huggingface.co/datasets/allenai/WildChat-1M)
- [OpenAssistant/oasst2](https://huggingface.co/datasets/OpenAssistant/oasst2)
