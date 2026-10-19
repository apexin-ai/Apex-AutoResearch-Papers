# DMPO + ETADN 训练 Pipeline 设计（v2）

## 0. 术语与背景

**DMPO**（Direct Multi-Turn Preference Optimization, arXiv 2406.14868）：将标准 DPO 扩展到多轮场景。核心创新：(1) 用 state-action occupancy measure (SAOM) 约束替代 policy 约束，使 partition function Z 与当前状态无关从而可消去；(2) 引入长度归一化因子 `(1-γ)/(1-γ^T)` 处理不等长轨迹。

**ETADN**（Error-Type-Aware DMPO with Adaptive Nudging）：将 DMPO 全局 γ 替换为 per-sample γ_e，根据错误类型动态调整时间折扣跨度。

**φ(t,T)** — DMPO 时间折扣函数，为每个 turn 分配信用权重。

---

## 1. DMPO Loss 实现方案

### 1.1 完整 DMPO Loss 公式

标准 DPO loss（单轮）：

```
L_DPO = -E[ log σ( β · log(π_θ(a^w|s)/π_ref(a^w|s)) - β · log(π_θ(a^l|s)/π_ref(a^l|s)) ) ]
```

DMPO loss（多轮，论文 Eq.16）：

```
L_DMPO = -E[ log σ(
    Σ_{t=0}^{T_w-1} β · φ(t, T_w) · log[π_θ(a_t^w|s_t^w) / π_ref(a_t^w|s_t^w)]
  - Σ_{t=0}^{T_l-1} β · φ(t, T_l) · log[π_θ(a_t^l|s_t^l) / π_ref(a_t^l|s_t^l)]
)]
```

其中时间折扣函数：

```
φ(t, T) = γ^t · (1 - γ^(T-t)) / (1 - γ^T)
```

- t = turn index (0-indexed)
- T = 总 turn 数
- γ ∈ (0, 1) = 时间折扣因子
- φ(t, T) 单调递减：早期 turn 权重更高

**特殊情况**：
- γ → 0: φ(0,T)=1, φ(t>0,T)=0 → 退化为单轮 DPO
- γ = 1: φ(t,T) = (T-t)/T → 线性衰减

### 1.2 在 trl DPOTrainer 上实现 DMPO

**trl v1.4.0 架构变化**：旧版 `get_batch_loss_metrics`、`concatenated_forward`、`get_batch_logps` 已被合并为单个 `_compute_loss` 方法（~315 行）。扩展点唯一且明确：**override `_compute_loss`**。

**需要修改的核心逻辑**（在 `_compute_loss` 内）：

| 原始 trl 行为 | DMPO 修改 |
|---|---|
| `per_token_logps.sum(dim=1)` → 标量 logps | 按 turn 加权求和：`Σ_t φ(t,T,γ) · Σ_{tokens∈turn_t} per_token_logps` |
| `completion_mask` 二值（0=prompt, 1=completion） | 额外需要 `turn_ids` 标记每个 token 属于哪个 turn |
| 无 per-sample 参数 | 需要 `gamma_per_sample` 传入每个样本的 γ 值 |

**实现策略**：不修改 per-token logps 的计算方式（`selective_log_softmax` 保持不变），仅在聚合阶段替换 `sum(dim=1)` 为加权求和。

### 1.3 Per-turn log probability 计算

ALFWorld 中每个 turn = 一次 agent 回复（Thought + Action），对应 tokenized 序列中一段连续 token。

**Turn 边界标记**：在数据预处理阶段，为每个 token 标记其所属 turn index，生成 `turn_ids` 张量：

```
token:    [<prompt> | Think... Act... | Think... Act... | Think... Act... ]
turn_ids: [   -1    |       0        |        1        |        2        ]
```

**加权聚合伪代码**：

```python
def dmpo_weighted_logps(per_token_logps, completion_mask, turn_ids, gamma, num_turns):
    """
    per_token_logps: [batch, seq_len]
    completion_mask: [batch, seq_len]  (1=completion, 0=prompt)
    turn_ids:        [batch, seq_len]  (turn index, -1=prompt)
    gamma:           [batch]           (per-sample γ)
    num_turns:       [batch]           (per-sample T)
    Returns:         [batch]           (weighted log probability per sample)
    """
    # 构建 per-token φ 权重
    token_weights = torch.zeros_like(per_token_logps)
    for t in range(turn_ids.max() + 1):
        mask_t = (turn_ids == t)  # [batch, seq_len]
        # φ(t, T, γ) = γ^t · (1 - γ^(T-t)) / (1 - γ^T)
        phi_t = gamma**t * (1 - gamma**(num_turns - t)) / (1 - gamma**num_turns)
        token_weights[mask_t] = phi_t.unsqueeze(1).expand_as(token_weights)[mask_t]

    return (per_token_logps * completion_mask * token_weights).sum(dim=1)
```

**向量化实现**（避免 for 循环，见 `dmpo_loss.py` 详细设计）：

```python
def compute_phi_weights(turn_ids, gamma, num_turns, max_turns):
    """全向量化 φ 权重计算"""
    t_range = torch.arange(max_turns, device=gamma.device)       # [max_turns]
    gamma_exp = gamma.unsqueeze(1)                                # [batch, 1]
    T = num_turns.unsqueeze(1).float()                            # [batch, 1]

    phi = gamma_exp**t_range * (1 - gamma_exp**(T - t_range)) / (1 - gamma_exp**T)
    # phi: [batch, max_turns]

    # 用 turn_ids gather 到 per-token 权重
    turn_ids_clamped = turn_ids.clamp(min=0)  # prompt tokens (-1) → 0，后续被 completion_mask 清零
    token_phi = phi.gather(1, turn_ids_clamped)  # [batch, seq_len]
    return token_phi
```

### 1.4 φ(t,T) 归一化验证

在实现前需验证 Σ_{t=0}^{T-1} φ(t,T,γ) 在不同 γ 和 T 下的值，确认 φ 是否归一化（即是否 Σφ = 1）。如果 Σφ ≠ 1，需检查 DMPO 论文原始设计意图——可能有意不归一化，利用非归一化引入 length bias（较长轨迹整体权重更大）。

**单元测试**：

```python
import math

def phi(t, T, gamma):
    """DMPO 时间折扣函数"""
    return gamma**t * (1 - gamma**(T - t)) / (1 - gamma**T)

def test_phi_normalization():
    print("=== φ(t,T) 归一化验证 ===")
    for gamma in [0.85, 0.92, 0.97]:
        for T in [5, 10, 20, 40]:
            phi_sum = sum(phi(t, T, gamma) for t in range(T))
            normalized = "✓" if abs(phi_sum - 1.0) < 1e-6 else "✗"
            print(f"γ={gamma}, T={T:2d}: Σφ={phi_sum:.6f}  {normalized}")
    print()
    print("如果 Σφ ≠ 1:")
    print("  1. 检查 DMPO 论文 Eq.16 是否有意不归一化")
    print("  2. 若有意：长轨迹获得更大总权重 → implicit length bias")
    print("  3. 若需归一化：可在 compute_phi_weights 中除以 Σφ")
    print("  4. 非归一化时可能需要调整 β 以补偿尺度变化")

if __name__ == "__main__":
    test_phi_normalization()
```

此测试应在 P1 阶段（`dmpo_loss.py` 单元测试）中执行。若 Σφ 显著偏离 1，需在 §9 风险表中记录应对方案，并决定是否在 `compute_phi_weights` 中添加归一化选项。

### 1.5 φ(t,T) 权重应用到 per-turn loss

在 `_compute_loss` 中，替换聚合步骤：

```python
# === 原始 trl ===
# logps = per_token_logps.sum(dim=1)

# === DMPO 修改 ===
token_phi = compute_phi_weights(turn_ids, gamma, num_turns, max_turns)
logps = (per_token_logps * shift_completion_mask * token_phi).sum(dim=1)

chosen_logps, rejected_logps = logps.chunk(2, dim=0)
# 后续 log ratio、sigmoid loss 与标准 DPO 相同
```

---

## 2. γ_e 注入方案

### 2.1 Error Type → γ_e 映射

```yaml
# config.yaml
gamma_e_mapping:
  action: 0.85    # 短纠正跨度：执行错误(wrong action)，信用集中在纠正步
  verify: 0.92    # 中等跨度：验证错误(wrong check)，信用跨检查序列
  plan:   0.97    # 长跨度：规划错误(wrong plan)，信用分布在整个重规划轨迹
  default: 0.90   # 未分类 fallback
```

**直觉**：
- γ 越小 → φ 衰减越快 → 信用集中在前几个 turn → 适合短程纠正（action error）
- γ 越大 → φ 衰减越慢 → 信用分散到所有 turn → 适合长程重规划（plan error）

### 2.2 注入流程

```
数据加载 → 每个样本有 error_type 字段
       ↓
DataCollator → 查表得到 gamma_per_sample: [batch_size]
       ↓
_compute_loss → gamma_per_sample 传入 compute_phi_weights()
       ↓
per-token 权重 → 加权聚合 → 标准 sigmoid loss
```

**Collator 中的 γ 注入**：

```python
class DMPODataCollator(DataCollatorForPreference):
    def __init__(self, gamma_map, mode, global_gamma=0.9, **kwargs):
        super().__init__(**kwargs)
        self.gamma_map = gamma_map
        self.mode = mode
        self.global_gamma = global_gamma

    def __call__(self, features):
        batch = super().__call__(features)

        # 收集 error_type → gamma
        gammas = []
        for f in features:
            if self.mode == "etadn":
                et = f.get("error_type", "default")
                gammas.append(self.gamma_map.get(et, self.gamma_map["default"]))
            elif self.mode == "dmpo":
                gammas.append(self.global_gamma)
            else:  # dpo
                gammas.append(0.0)  # γ=0 → φ(0,T)=1, rest=0 → 等效无加权

        # chosen 和 rejected 使用相同 γ（同一 preference pair 来自同一 error_type）
        gamma_chosen = torch.tensor(gammas, dtype=torch.float32)
        gamma_rejected = gamma_chosen.clone()
        batch["gamma"] = torch.cat([gamma_chosen, gamma_rejected], dim=0)

        return batch
```

### 2.3 对比：DMPO 全局 γ vs ETADN per-sample γ_e

| 维度 | DMPO | ETADN |
|---|---|---|
| γ 来源 | 全局超参（如 0.9） | per-sample，由 error_type 决定 |
| φ(t,T) 计算 | 同一 batch 所有样本共享 φ 表 | 每个样本有独立 φ 序列 |
| 信用分配 | 所有轨迹用同一衰减速率 | action error 快衰减，plan error 慢衰减 |
| 实现复杂度 | γ 为标量 | γ 为 [batch] 向量，compute_phi_weights 需向量化 |

---

## 3. 数据 Pipeline

### 3.1 DPO 数据格式

每个样本包含：

```json
{
  "id": "alfworld_task_42_pair_0",
  "error_type": "action",
  "prompt": "You are in a kitchen. Your task is to ...",
  "chosen": [
    {"role": "assistant", "content": "Think: I need to find a tomato. Act: go to fridge 1"},
    {"role": "user", "content": "Obs: The fridge is closed."},
    {"role": "assistant", "content": "Think: I should open it. Act: open fridge 1"},
    {"role": "user", "content": "Obs: You open the fridge. You see a tomato 1."},
    {"role": "assistant", "content": "Think: Found it. Act: take tomato 1 from fridge 1"},
    {"role": "user", "content": "Obs: You pick up the tomato 1."}
  ],
  "rejected": [
    {"role": "assistant", "content": "Think: I need to find a tomato. Act: go to countertop 1"},
    {"role": "user", "content": "Obs: On the countertop you see a bread 1."},
    {"role": "assistant", "content": "Think: Not here. Act: go to countertop 2"},
    {"role": "user", "content": "Obs: On the countertop you see a cup 1."},
    {"role": "assistant", "content": "Think: Maybe in the cabinet. Act: go to cabinet 1"},
    {"role": "user", "content": "Obs: The cabinet is closed."}
  ],
  "chosen_turns": 3,
  "rejected_turns": 3
}
```

### 3.2 多轮对话处理：Turn 定义

ALFWorld 轨迹中每个 turn 的结构：

```
Turn t:
  Assistant: "Think: <reasoning>. Act: <action>"    ← agent 生成
  User:      "Obs: <environment_observation>"        ← 环境返回
```

**1 turn = 1 个 assistant 回复**（只有 assistant 的 token 参与 loss 计算）。User/Obs 部分通过 `completion_mask=0` 屏蔽。

Turn 数 T = assistant 回复的数量。

### 3.3 Tokenization 与 Turn 标记

```python
def tokenize_multiturn(example, tokenizer, max_length):
    """将 prompt + chosen/rejected 多轮对话 tokenize，并标记 turn_ids"""
    # 1. 构建完整对话（chat template）
    messages = [{"role": "system", "content": example["prompt"]}]
    messages += example["chosen"]  # 或 rejected

    # 2. 分步 tokenize 以获取 turn 边界
    prompt_ids = tokenizer.apply_chat_template(
        [messages[0]], tokenize=True, add_generation_prompt=True
    )

    turn_ids = [-1] * len(prompt_ids)  # prompt tokens 标记为 -1
    completion_mask = [0] * len(prompt_ids)
    all_ids = list(prompt_ids)
    current_turn = 0

    for i in range(1, len(messages), 2):  # step=2, assistant+user pairs
        # assistant 部分
        asst_msg = messages[i]
        asst_ids = tokenizer.encode(asst_msg["content"], add_special_tokens=False)
        # + chat template 的 role tokens
        role_ids = tokenizer.encode("<|im_start|>assistant\n", add_special_tokens=False)
        end_ids = tokenizer.encode("<|im_end|>\n", add_special_tokens=False)

        all_ids += role_ids
        turn_ids += [-1] * len(role_ids)  # role tokens 不参与 loss
        completion_mask += [0] * len(role_ids)

        all_ids += asst_ids
        turn_ids += [current_turn] * len(asst_ids)  # assistant content = turn t
        completion_mask += [1] * len(asst_ids)

        all_ids += end_ids
        turn_ids += [current_turn] * len(end_ids)
        completion_mask += [1] * len(end_ids)

        # user/observation 部分
        if i + 1 < len(messages):
            user_msg = messages[i + 1]
            user_ids = tokenizer.encode(
                f"<|im_start|>user\n{user_msg['content']}<|im_end|>\n",
                add_special_tokens=False
            )
            all_ids += user_ids
            turn_ids += [-1] * len(user_ids)  # user tokens 不参与 loss
            completion_mask += [0] * len(user_ids)

        current_turn += 1

    # 3. 截断
    all_ids = all_ids[:max_length]
    turn_ids = turn_ids[:max_length]
    completion_mask = completion_mask[:max_length]

    return {
        "input_ids": all_ids,
        "turn_ids": turn_ids,
        "completion_mask": completion_mask,
        "num_turns": current_turn,
    }
```

**注意**：实际实现中需要更精确地处理 Qwen3 的 chat template（`<|im_start|>`/`<|im_end|>` tokens）。上述为简化版，正式实现应使用 `tokenizer.apply_chat_template` 分段处理，逐段定位 assistant response span。

### 3.4 数据集统计预估

| 维度 | 估计值 |
|---|---|
| ALFWorld 任务数 | ~3,500 (train split) |
| 每任务轨迹数 | 5-10（采样多条） |
| 有效 preference pairs | ~2,000-5,000（过滤后） |
| 平均 turn 数 T | 5-15 |
| 平均序列长度 | 1,500-3,000 tokens |

---

## 4. 模型配置

### 4.1 Qwen3-8B QLoRA 配置

```python
from transformers import AutoModelForCausalLM, BitsAndBytesConfig
from peft import LoraConfig

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16,
    bnb_4bit_use_double_quant=True,
)

model = AutoModelForCausalLM.from_pretrained(
    "Qwen/Qwen3-8B",
    quantization_config=bnb_config,
    torch_dtype=torch.bfloat16,
    attn_implementation="flash_attention_2",
    device_map={"": device_id},  # 单卡绑定
)

lora_config = LoraConfig(
    r=64,
    lora_alpha=128,
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj",
                     "gate_proj", "up_proj", "down_proj"],
    lora_dropout=0.05,
    task_type="CAUSAL_LM",
    bias="none",
)
```

### 4.2 Ref Model 处理

QLoRA 下 ref_model 的处理方式：**使用 PEFT adapter 禁用机制**。

trl DPOTrainer 在检测到 PeftModel 且未提供 `ref_model` 时：
1. 创建 "ref" adapter 副本（复制 default adapter 权重）
2. 前向传播时通过 `use_adapter(model, "ref")` 切换到冻结的初始权重
3. 或者直接 `model.disable_adapter()` → base model = ref model

**推荐方式**：`precompute_ref_log_probs=True`，训练前一次性计算所有样本的 ref logps 并缓存，训练时从 dataset 直接读取。

> **⚠️ 关键约束：预计算必须使用与训练相同的 φ-weighted 聚合。**
>
> 默认 trl 预计算使用标准 `sum` 聚合（`per_token_logps.sum(dim=1)`），但 DMPO/ETADN 训练时使用 φ-weighted 聚合。两边聚合方式不一致会导致 loss 计算错误（ref logps 与 policy logps 尺度不匹配）。
>
> 解决方案：预计算阶段传入 `turn_ids` 和 `gamma_e`，用 φ-weighted 聚合后存储。预计算时 γ_e 已知（从样本的 `error_type` 查 `gamma_e_mapping` 配置表），完全可行。

**预计算流程**：

```python
def precompute_ref_logps(ref_model, dataset, tokenizer, gamma_e_mapping, mode):
    """预计算 ref model 的 φ-weighted log probs"""
    ref_model.eval()
    ref_model.disable_adapter()  # base model = ref model

    ref_chosen_logps_list = []
    ref_rejected_logps_list = []

    with torch.no_grad():
        for sample in dataset:
            for key in ("chosen", "rejected"):
                input_ids = sample[f"{key}_input_ids"]
                completion_mask = sample[f"{key}_completion_mask"]
                turn_ids = sample[f"{key}_turn_ids"]
                num_turns = sample[f"{key}_num_turns"]

                # 1. Per-token logps
                outputs = ref_model(input_ids=input_ids.unsqueeze(0))
                shift_logits = outputs.logits[..., :-1, :].contiguous()
                shift_labels = input_ids[1:].unsqueeze(0)
                per_token_logps = selective_log_softmax(shift_logits, shift_labels)
                shift_mask = completion_mask[1:]

                # 2. φ-weighted 聚合（与训练一致）
                if mode == "dpo":
                    logps = (per_token_logps * shift_mask).sum(dim=1)
                else:
                    gamma_e = gamma_e_mapping.get(sample["error_type"], gamma_e_mapping["default"])
                    gamma_t = torch.tensor([gamma_e], device=input_ids.device)
                    T = torch.tensor([num_turns], device=input_ids.device)
                    shift_turn_ids = turn_ids[1:].unsqueeze(0)
                    token_phi = compute_phi_weights(shift_turn_ids, gamma_t, T,
                                                    max_turns=shift_turn_ids.max().item() + 1)
                    logps = (per_token_logps * shift_mask * token_phi).sum(dim=1)

                if key == "chosen":
                    ref_chosen_logps_list.append(logps.item())
                else:
                    ref_rejected_logps_list.append(logps.item())

    # 释放 ref model（QLoRA 下 = 释放 base model forward 的显存）
    del ref_model
    torch.cuda.empty_cache()

    return ref_chosen_logps_list, ref_rejected_logps_list
```

**优势**：
- 训练时无需 ref model 前向传播，节省 ~30% VRAM
- 训练速度提升 ~40%
- ref logps 与 policy logps 使用相同的 φ-weighted 聚合，loss 计算正确

### 4.3 VRAM 估算（单卡 RTX 4090D 24GB）

| 组件 | 估计 VRAM |
|---|---|
| Qwen3-8B 4-bit weights | ~4.5 GB |
| LoRA adapters (r=64, 7 modules, bf16) | ~0.4 GB |
| Optimizer states (AdamW, 2×bf16) | ~1.6 GB |
| Gradients (bf16) | ~0.4 GB |
| 激活（gradient checkpointing, seq_len=3072, micro_bs=1） | ~6-8 GB |
| PyTorch + CUDA overhead | ~2 GB |
| **总计** | **~15-17 GB** |

剩余 ~7-9 GB 余量。micro_batch_size=2 可能可行但需实测。

**两卡策略**：每张 4090D 跑一个独立 run（不同 seed 或不同 ablation 配置），通过 `CUDA_VISIBLE_DEVICES=0` / `CUDA_VISIBLE_DEVICES=1` 隔离。

### 4.4 训练超参

```yaml
# config.yaml
training:
  mode: "etadn"            # "dpo" | "dmpo" | "etadn"
  beta: 0.1                # DPO β
  global_gamma: 0.90       # DMPO 模式下的全局 γ
  learning_rate: 1.0e-6
  lr_scheduler_type: "constant_with_warmup"
  warmup_ratio: 0.1
  num_train_epochs: 3
  per_device_train_batch_size: 1
  gradient_accumulation_steps: 16
  gradient_checkpointing: true
  bf16: true
  max_length: 3072
  max_prompt_length: 512
  logging_steps: 5
  save_steps: 100
  eval_steps: 50
  precompute_ref_log_probs: true
  label_smoothing: 0.0
  loss_type: "sigmoid"

lora:
  r: 64
  lora_alpha: 128
  target_modules: ["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"]
  lora_dropout: 0.05

gamma_e_mapping:
  action: 0.85
  verify: 0.92
  plan: 0.97
  default: 0.90
```

### 4.5 环境依赖

| 包 | 要求版本 | 说明 |
|---|---|---|
| `trl` | **`==1.4.0`** | 必须使用此版本。1.4.0 将旧版 `get_batch_loss_metrics` / `concatenated_forward` / `get_batch_logps` 合并为 `_compute_loss`，本设计基于此 API 结构。服务器现有 1.1.0 需升级。 |
| `transformers` | `>=4.40.0` | Qwen3 支持 |
| `peft` | `>=0.10.0` | LoRA + BnB 集成 |
| `bitsandbytes` | `>=0.43.0` | nf4 量化 |
| `torch` | `>=2.1` | bf16 + flash_attention_2 |
| `flash-attn` | `>=2.5.0` | Flash Attention 2 |

**trl 1.4.0 中本设计依赖的关键 API**：
- `DPOTrainer._compute_loss(model, inputs, return_outputs)` — 唯一的 loss 扩展点
- `trl.trainer.utils.selective_log_softmax(logits, labels)` — per-token log prob 计算
- `DPOConfig` — 训练配置基类

**升级命令**：
```bash
pip install trl==1.4.0
```

---

## 5. 推理 Pipeline

### 5.1 轨迹收集

```python
# collect_trajectories.py
# 用 Qwen3-8B (当前 policy) 在 ALFWorld 中交互
# 每个任务采样 K=8 条轨迹（不同 temperature / top-p）

from vllm import LLM, SamplingParams  # 或 transformers.generate

model = LLM(
    model="path/to/qwen3-8b-merged",  # LoRA merge 后的 checkpoint
    tensor_parallel_size=1,
    gpu_memory_utilization=0.85,
    max_model_len=4096,
)

params = SamplingParams(
    temperature=0.7,
    top_p=0.9,
    max_tokens=256,      # 每步生成上限
    stop=["Obs:"],       # ALFWorld 环境会返回 Obs
)

# 循环：generate → parse action → env.step → append obs → repeat
```

**输出格式**：

```json
{
  "task_id": "pick_clean_then_place-Tomato-...",
  "trajectory": [
    {"role": "assistant", "content": "Think: ... Act: go to fridge 1"},
    {"role": "user", "content": "Obs: The fridge is closed."},
    ...
  ],
  "reward": 1,           # ALFWorld: 1=成功, 0=失败
  "num_steps": 8,
  "task_type": "pick_clean_then_place"
}
```

### 5.2 错误分类

```python
# classify_errors.py
# 用 Qwen3-14B-AWQ 做 zero-shot 分类

CLASSIFY_PROMPT = """Analyze the following failed trajectory in ALFWorld.
The agent attempted a task but failed. Identify the PRIMARY error type:

- action: Wrong physical action (e.g., went to wrong location, used wrong object)
- verify: Failed to verify state (e.g., didn't check if object present, skipped confirmation)
- plan: Wrong high-level plan (e.g., incorrect task decomposition, missed prerequisite steps)

Task: {task_description}
Successful trajectory: {chosen_trajectory}
Failed trajectory: {rejected_trajectory}

Respond with ONLY one word: action, verify, or plan"""

# 输出: error_type ∈ {"action", "verify", "plan"}
```

### 5.3 Preference Pair 构建

```python
# construct_preference.py

def construct_pairs(trajectories, error_classifications):
    """
    策略：
    1. 同一 task 内，reward=1 的轨迹为 chosen，reward=0 的为 rejected
    2. 若同一 task 有多条成功/失败轨迹，取最短成功 + 每条失败 → 多个 pairs
    3. 附加 error_type 标签（来自 classify_errors.py 的输出）
    """
    pairs = []
    for task_id, task_trajs in group_by_task(trajectories):
        chosen_trajs = [t for t in task_trajs if t["reward"] == 1]
        rejected_trajs = [t for t in task_trajs if t["reward"] == 0]

        if not chosen_trajs or not rejected_trajs:
            continue

        best_chosen = min(chosen_trajs, key=lambda t: t["num_steps"])

        for rej in rejected_trajs:
            error_type = error_classifications.get(
                f"{task_id}_{rej['traj_id']}", "default"
            )
            pairs.append({
                "id": f"{task_id}_pair_{len(pairs)}",
                "error_type": error_type,
                "prompt": task_description(task_id),
                "chosen": best_chosen["trajectory"],
                "rejected": rej["trajectory"],
                "chosen_turns": count_assistant_turns(best_chosen["trajectory"]),
                "rejected_turns": count_assistant_turns(rej["trajectory"]),
            })

    return pairs
```

---

## 6. 完整文件结构

```
error_diag_dpo_recovery/
├── train_etadn.py              # 主训练入口
│   - 解析 config.yaml
│   - 加载模型 + LoRA + BnB 量化
│   - 构建 dataset + collator
│   - 初始化 ETADNTrainer
│   - trainer.train()
│
├── dmpo_trainer.py             # ETADNTrainer（继承 trl DPOTrainer）
│   - override _compute_loss(): 替换 logps 聚合为 φ-weighted
│   - override _prepare_dataset(): 添加 turn_ids 和 num_turns
│   - DMPODataCollator: 注入 gamma、pad turn_ids
│   - 支持三种模式: dpo / dmpo / etadn (通过 config flag)
│
├── dmpo_loss.py                # 纯函数：φ(t,T) 计算 + 加权聚合
│   - compute_phi(t, T, gamma): 单值 φ 计算
│   - compute_phi_weights(turn_ids, gamma, num_turns): 向量化 per-token 权重
│   - dmpo_weighted_logps(): per_token_logps → weighted scalar
│
├── data_utils.py               # 数据加载与预处理
│   - load_preference_data(path): 加载 JSON pairs
│   - tokenize_multiturn(): 带 turn 边界标记的 tokenization
│   - build_dataset(): HF Dataset 构建
│
├── config.yaml                 # 超参配置（见 §4.4）
│
├── collect_trajectories.py     # 轨迹收集（§5.1）
│   - ALFWorld 环境交互
│   - vLLM / transformers 推理
│   - 输出 trajectories.jsonl
│
├── classify_errors.py          # 错误分类（§5.2）
│   - Qwen3-14B-AWQ zero-shot
│   - 输出 error_classifications.json
│
├── construct_preference.py     # Preference pair 构建（§5.3）
│   - 输入: trajectories + error_classifications
│   - 输出: preference_pairs.json
│
├── evaluate.py                 # ALFWorld 评估
│   - 标准 eval protocol: 134 unseen tasks
│   - 指标: success rate, average steps
│   - 按 task type 分组报告
│
├── scripts/
│   ├── run_gpu0.sh             # GPU0 训练脚本 (CUDA_VISIBLE_DEVICES=0)
│   └── run_gpu1.sh             # GPU1 训练脚本 (CUDA_VISIBLE_DEVICES=1)
│
└── alfworld_env/               # ALFWorld 环境 wrapper（从 ETO 移植）
    ├── env_wrapper.py
    └── task_configs/
```

### 6.1 关键模块依赖关系

```
config.yaml
    ↓
train_etadn.py
    ├── data_utils.py → tokenize_multiturn()
    ├── dmpo_trainer.py → ETADNTrainer
    │       ├── dmpo_loss.py → compute_phi_weights()
    │       └── DMPODataCollator → gamma injection
    └── evaluate.py (训练结束后调用)

collect_trajectories.py → trajectories.jsonl
    ↓
classify_errors.py → error_classifications.json
    ↓
construct_preference.py → preference_pairs.json
    ↓
train_etadn.py (读取 preference_pairs.json)
```

---

## 7. Ablation 设计

### 7.1 三种模式切换

通过 `config.yaml` 中 `training.mode` 字段切换：

| Mode | γ 来源 | φ(t,T) 行为 | 等效于 |
|---|---|---|---|
| `dpo` | 不使用 | 所有 token 权重=1（`completion_mask` 原样聚合） | 标准 DPO |
| `dmpo` | `global_gamma`（标量） | 全局 γ 计算 φ，所有样本共享 | 原始 DMPO |
| `etadn` | `gamma_e_mapping[error_type]`（per-sample） | per-sample γ_e 计算 φ | ETADN (ours) |

### 7.2 代码中的模式分支

在 `ETADNTrainer._compute_loss` 中：

```python
if self.mode == "dpo":
    # 标准 DPO: 直接 sum
    logps = (per_token_logps * shift_completion_mask).sum(dim=1)
else:
    # dmpo 或 etadn: φ-weighted sum
    # gamma 已由 collator 注入到 batch["gamma"]
    token_phi = compute_phi_weights(
        turn_ids=batch["turn_ids"][:, 1:],  # shift 对齐
        gamma=batch["gamma"],
        num_turns=batch["num_turns"],
        max_turns=batch["turn_ids"].max().item() + 1,
    )
    logps = (per_token_logps * shift_completion_mask * token_phi).sum(dim=1)
```

### 7.3 实验矩阵

| Run | Mode | γ / γ_e | GPU | Seed | 目的 |
|---|---|---|---|---|---|
| A1 | dpo | — | 0 | 42 | Baseline: 标准 DPO |
| B1 | dmpo | 0.92 | 0 | 42 | DMPO 全局 γ |
| B2 | dmpo | 0.92 | 1 | 123 | DMPO seed 2 |
| B3 | dmpo | 0.92 | 0 | 456 | DMPO seed 3 |
| C1 | etadn | per-sample | 1 | 42 | **Ours**: ETADN |
| C2 | etadn | per-sample | 0 | 123 | ETADN seed 2 |
| C3 | etadn | per-sample | 1 | 456 | ETADN seed 3 |

**Seeds**: ETADN 和 DMPO 各 3 seeds (42, 123, 456) 取平均，DPO baseline 1 seed。共 **7 runs**。

**两卡并行策略**：每次在 2 张 4090D 上同时跑 2 个 run，4 轮完成（~12h 总时间）。

**调度顺序**：
1. 轮 1: C1 (ETADN seed=42, GPU1) + B1 (DMPO seed=42, GPU0) → 最快得到对比信号
2. 轮 2: C2 (ETADN seed=123, GPU0) + B2 (DMPO seed=123, GPU1)
3. 轮 3: C3 (ETADN seed=456, GPU1) + B3 (DMPO seed=456, GPU0)
4. 轮 4: A1 (DPO baseline seed=42, GPU0)

### 7.4 评估指标

| 指标 | 说明 |
|---|---|
| ALFWorld success rate (overall) | 主指标，134 unseen tasks |
| Success rate per task type | 6 种 task type 的分项成功率 |
| Average steps to success | 效率指标 |
| Error type distribution shift | 训练前后的错误类型分布变化 |
| DMPO reward (Φ(τ)) | 训练过程中 chosen/rejected 的加权 log-ratio |
| Training loss curve | 收敛性对比 |

---

## 8. ETADNTrainer 核心代码骨架

```python
# dmpo_trainer.py

from trl import DPOTrainer, DPOConfig
from dmpo_loss import compute_phi_weights

class ETADNConfig(DPOConfig):
    mode: str = "etadn"          # "dpo" | "dmpo" | "etadn"
    global_gamma: float = 0.90
    gamma_e_mapping: dict = None  # {"action": 0.85, "verify": 0.92, "plan": 0.97}


class ETADNTrainer(DPOTrainer):

    def __init__(self, *args, mode="etadn", global_gamma=0.9, gamma_e_mapping=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.mode = mode
        self.global_gamma = global_gamma
        self.gamma_e_mapping = gamma_e_mapping or {}

    def _compute_loss(self, model, inputs, return_outputs=False):
        """Override: DMPO φ-weighted log probability aggregation."""
        # --- 1. 提取额外字段 ---
        turn_ids = inputs.pop("turn_ids", None)
        num_turns = inputs.pop("num_turns", None)
        gamma = inputs.pop("gamma", None)
        completion_mask = inputs["completion_mask"]
        input_ids = inputs["input_ids"]

        # --- 2. Policy forward ---
        model_kwargs = {k: v for k, v in inputs.items()
                        if k not in ("completion_mask", "ref_chosen_logps", "ref_rejected_logps")}
        outputs = model(**model_kwargs)

        # --- 3. Per-token logps ---
        from trl.trainer.utils import selective_log_softmax
        shift_logits = outputs.logits[..., :-1, :].contiguous()
        shift_labels = input_ids[..., 1:].contiguous()
        shift_completion_mask = completion_mask[..., 1:].contiguous()
        per_token_logps = selective_log_softmax(shift_logits, shift_labels)
        per_token_logps[shift_completion_mask == 0] = 0.0

        # --- 4. 聚合（核心修改点） ---
        if self.mode == "dpo" or turn_ids is None:
            logps = per_token_logps.sum(dim=1)
        else:
            shift_turn_ids = turn_ids[..., 1:].contiguous()
            token_phi = compute_phi_weights(shift_turn_ids, gamma, num_turns,
                                            max_turns=shift_turn_ids.max().item() + 1)
            logps = (per_token_logps * shift_completion_mask * token_phi).sum(dim=1)

        chosen_logps, rejected_logps = logps.chunk(2, dim=0)

        # --- 5. Reference logps ---
        if "ref_chosen_logps" in inputs:
            ref_chosen_logps = inputs["ref_chosen_logps"]
            ref_rejected_logps = inputs["ref_rejected_logps"]
        else:
            with torch.no_grad():
                ref_chosen_logps, ref_rejected_logps = self._compute_ref_logps(
                    model, inputs, shift_completion_mask,
                    turn_ids=shift_turn_ids if self.mode != "dpo" else None,
                    gamma=gamma, num_turns=num_turns,
                )

        # --- 6. Loss (sigmoid, same as standard DPO) ---
        chosen_logratios = chosen_logps - ref_chosen_logps
        rejected_logratios = rejected_logps - ref_rejected_logps
        logits = chosen_logratios - rejected_logratios

        loss = -F.logsigmoid(self.beta * logits).mean()

        # --- 7. Metrics ---
        chosen_rewards = (self.beta * (chosen_logps - ref_chosen_logps)).detach()
        rejected_rewards = (self.beta * (rejected_logps - ref_rejected_logps)).detach()
        reward_margin = (chosen_rewards - rejected_rewards).mean()

        metrics = {
            "loss": loss.detach().item(),
            "rewards/chosen": chosen_rewards.mean().item(),
            "rewards/rejected": rejected_rewards.mean().item(),
            "rewards/margin": reward_margin.item(),
        }
        self.store_metrics(metrics, train_eval="train")

        if return_outputs:
            return loss, {"logits": logits}
        return loss
```

---

## 9. 风险与注意事项

| 风险 | 缓解 |
|---|---|
| `precompute_ref_log_probs` 与自定义 φ-weighted 聚合不兼容 | **已解决**（§4.2）：预计算阶段传入 `turn_ids` 和 `gamma_e`，使用与训练相同的 φ-weighted 聚合后存储 |
| trl 版本更新可能改变 `_compute_loss` 内部结构 | 锁定 `trl==1.4.0`（见 §4.5），在代码中 assert 关键接口存在 |
| Qwen3 chat template 的 token 边界与手动分段不一致 | 使用 `tokenizer.apply_chat_template` 逐段处理，用 offset mapping 精确定位 assistant token span |
| φ 权重导致梯度尺度变化 | 需通过 §1.4 归一化验证确认 Σφ 的实际值。若 Σφ ≠ 1 且偏差显著，可在 `compute_phi_weights` 中添加归一化选项，或调整 β 补偿尺度 |
| γ_e 值（0.85/0.92/0.97）为初始设定 | 后续可做 γ_e 敏感性实验（grid search），或作为可学习参数 |

---

## 10. 实施优先级

| Phase | 内容 | 估计时间 |
|---|---|---|
| P1 | `dmpo_loss.py` + 单元测试（验证 φ 计算正确性） | 0.5 天 |
| P2 | `data_utils.py`（tokenization + turn 标记） | 1 天 |
| P3 | `dmpo_trainer.py`（ETADNTrainer + collator） | 1.5 天 |
| P4 | `train_etadn.py`（集成 + 小数据 smoke test） | 0.5 天 |
| P5 | 推理 pipeline（collect + classify + construct） | 2 天 |
| P6 | 完整训练 + 评估 | 2-3 天 |
