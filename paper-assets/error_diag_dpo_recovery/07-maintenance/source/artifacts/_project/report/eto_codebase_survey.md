# ETO Codebase Technical Survey

**Repo**: https://github.com/Yifan-Song793/ETO
**Paper**: Trial and Error: Exploration-Based Trajectory Optimization for LLM Agents (ACL 2024 Main)
**License**: 无显式 LICENSE 文件；代码基于 FastChat (Apache 2.0) 和 stanford_alpaca (Apache 2.0) 修改

---

## 1. 目录结构概览

```
ETO/
├── run_eto.sh              # 完整 ETO pipeline 脚本（SFT → explore → DPO 迭代）
├── setup.sh                # 环境安装 + 数据下载
├── construct_preference.py # 从 exploration 输出构建 DPO preference pairs
├── requirements.txt        # 主依赖
├── fastchat/               # 修改版 FastChat（训练 + 推理服务）
│   ├── train/
│   │   ├── train.py        # SFT 训练脚本
│   │   ├── train_dpo.py    # DPO 训练入口
│   │   ├── dpo_trainer.py  # 自定义 DPOMultiTrainer（多轮对话 DPO）
│   │   └── train_dpo_mistral.py
│   ├── serve/              # FastChat 推理服务（controller + model_worker）
│   ├── model/
│   │   └── model_adapter.py  # 模型适配器注册（含 QwenChatAdapter）
│   └── conversation.py     # 对话模板（含 ChatML/Qwen 模板）
├── eval_agent/             # 评估框架
│   ├── main.py             # 评估主入口
│   ├── agents/
│   │   ├── fastchat_agent.py  # FastChat 推理 agent
│   │   └── openai_lm_agent.py
│   ├── envs/
│   │   ├── alfworld_env.py # ALFWorld 环境封装
│   │   ├── webshop_env.py
│   │   └── sciworld_env.py
│   ├── tasks/
│   │   ├── alfworld.py     # ALFWorld task loader（train 3321, test 134）
│   │   └── ...
│   ├── prompt/
│   │   ├── templates.py    # ICL prompt 模板
│   │   ├── instructions/alfworld_inst.txt
│   │   └── icl_examples/alfworld_icl.json
│   ├── configs/
│   │   ├── task/alfworld.json   # env_class, max_steps=40
│   │   └── model/fastchat.json  # controller address, temperature
│   └── data/alfworld/     # ALFWorld 游戏数据 + PDDL
└── envs/                   # WebShop / ScienceWorld 环境
```

---

## 2. 关键流程分析

### 2.1 完整 ETO Pipeline（`run_eto.sh`）

```
Phase 1: SFT
  torchrun train.py → LLama-2-7b-chat + expert trajectories → SFT model
  超参: lr=2e-5, epochs=3, batch=64, FSDP full_shard, max_length=4096

Phase 2-N: ETO 迭代（循环 3 轮）
  Step 1: Exploration
    - 启动 4 个 FastChat model worker（并行推理）
    - 在 train split 上用当前策略收集轨迹
    - temperature=0.7（explore 模式）
  Step 2: 构建 Preference Pairs
    - construct_preference.py 对比 exploration 轨迹 vs golden 轨迹
    - reward 低于 golden → rejected，高于 golden → chosen
    - 失败轨迹长度截断：不超过成功轨迹 + 5 轮
  Step 3: DPO 训练
    - DPOMultiTrainer 处理多轮对话 preference pairs
    - iter1: beta=0.1, lr=1e-6；iter2+: beta=0.5, lr=5e-7
    - batch=32, epochs=3, FSDP full_shard
  Step 4: 评估
    - test split，temperature=0.0
```

### 2.2 ALFWorld 集成

**环境初始化** (`eval_agent/tasks/alfworld.py`):
- 使用 `alfworld` Python 包，`AlfredTWEnv` 文本模式
- train: 3321 tasks, test: 134 tasks (out-of-distribution)
- 支持 `part_num` / `part_idx` 分片并行探索

**环境交互** (`eval_agent/envs/alfworld_env.py`):
- Agent 输出 "Thought: ...\nAction: ..." 格式
- `parse_action()` 用正则提取 action
- `conduct_action()` 调用 `env.step([action])`
- reward: 二值（成功=True/失败=False），max_steps=40

**ALFWorld 任务类型** (6 类):
1. Pick & Place (put)
2. Examine in Light (examine)
3. Clean & Place (clean)
4. Heat & Place (heat)
5. Cool & Place (cool)
6. Pick Two & Place (puttwo)

### 2.3 轨迹收集与 Preference 构建

**Exploration 输出格式** (`outputs/<model_name>/<task>/<id>.json`):
```json
{
  "meta": {"reward": true/false, "error": "<game_file_path>"},
  "conversations": [...]  // 完整多轮对话
}
```

**Preference 构建** (`construct_preference.py`):
- ALFWorld 用 `build_preference_alfworld()` 分支
- 用 `game_file` 路径末段作为 task ID 对齐 golden / predicted
- golden 轨迹从 SFT 数据加载，reward 固定为 1.0
- **关键**：DPO data 中 prompt 包含 instruction part + task 的第一轮

**DPO 数据格式**:
```json
{
  "id": "...",
  "prompt": [instruction_part + first_observation],
  "chosen": [subsequent_turns_of_better_trajectory],
  "rejected": [subsequent_turns_of_worse_trajectory]
}
```

### 2.4 DPO 训练 Pipeline

**入口**: `fastchat/train/train_dpo.py`
- 使用 `DPOMultiTrainer`（基于 TRL DPOTrainer 修改）
- 加载 model + ref_model（同一 checkpoint）
- `preprocess_multi_turn()` 将多轮对话转为 tokenized format
- `mask_labels()` 确保只在 assistant 回复上计算 loss

**DPO Loss**（`dpo_trainer.py:737-803`）:
```python
pi_logratios = policy_chosen_logps - policy_rejected_logps
ref_logratios = reference_chosen_logps - reference_rejected_logps
logits = pi_logratios - ref_logratios
losses = -F.logsigmoid(self.beta * logits)  # sigmoid 类型
```

**关键约束**:
- `self.beta` 是全局标量，对所有样本统一
- loss 类型支持 sigmoid/hinge/ipo/kto_pair
- FSDP full_shard，`fsdp_transformer_layer_cls_to_wrap='LlamaDecoderLayer'`

### 2.5 推理服务

- FastChat controller (`fastchat.serve.controller`) 管理多 worker
- FastChat model_worker 加载模型提供推理
- `FastChatAgent` 通过 HTTP 请求 controller 进行 streaming generation
- 对话模板通过 `get_conversation_template(model_name)` 自动匹配

---

## 3. Base Model 与 Qwen3-8B 适配评估

### 3.1 原始设定

- Base model: **Llama-2-7b-chat-hf**
- 对话模板: Vicuna v1.1 (ADD_COLON_TWO style)
- FSDP wrap class: `LlamaDecoderLayer`
- Tokenizer: LlamaTokenizer，pad_token = unk_token
- Flash attention: `attn_implementation="flash_attention_2"`

### 3.2 已有 Qwen 支持

FastChat 已包含:
- `QwenChatAdapter`（`model_adapter.py:1544`）：match "qwen" in model_path
- `qwen-7b-chat` 对话模板（ChatML style）
- ChatML sep_style 已在 `conversation.py` 实现

### 3.3 适配 Qwen3-8B 需要修改的地方

| 改动点 | 文件 | 难度 | 说明 |
|--------|------|------|------|
| **FSDP wrap class** | `run_eto.sh` | 低 | `LlamaDecoderLayer` → `Qwen2DecoderLayer`（Qwen3 基于 Qwen2 架构） |
| **对话模板** | `conversation.py` | 低 | 已有 ChatML 支持，需确认 Qwen3 的 special token IDs |
| **mask_labels()** | `train_dpo.py:117-188` | 中 | 当前硬编码 Vicuna/Llama2 sep style，需添加 ChatML 分支 |
| **tokenizer 设置** | `train_dpo.py:306-308` | 低 | `pad_token = unk_token` 对 Qwen 不适用，Qwen 有自己的 pad_token |
| **preprocess_multi_turn()** | `train_dpo.py:192-256` | 中 | 依赖 `get_model_adapter` + conv template，理论上自动适配，但需验证 tokenization 正确性 |
| **train.py SFT** | `fastchat/train/train.py` | 中 | 同样的 mask_labels + FSDP 问题 |
| **model_worker** | 自动适配 | 低 | QwenChatAdapter 已注册 |
| **trust_remote_code** | 多处 | 低 | Qwen3 需要 `trust_remote_code=True` |
| **construct_preference.py** | `construct_preference.py:6-44` | 低 | instruction_part 中的对话格式不涉及模型，无需修改 |

**总工作量评估**: 约 1-2 天，主要工作在 DPO/SFT 训练的 tokenization 适配。

---

## 4. ETADN 改造评估（Error-Type-Specific γ_e）

### 4.1 核心改动：DPO loss 中注入 γ_e

**当前 DPO loss** (`dpo_trainer.py:737-803`):
```python
self.beta  # 全局标量，对所有样本统一
losses = -F.logsigmoid(self.beta * logits)
```

**目标**: 将 `self.beta` 替换为 per-sample `gamma_e`（根据 error type 确定）

**改动点**:

1. **数据层** (`construct_preference.py`):
   - 在构建 preference pair 时，分析失败轨迹的 error type
   - ALFWorld 的 6 个 task type 天然提供 error-type 分类
   - 还需添加 error pattern 分析（wrong object, wrong receptacle, wrong action sequence 等）
   - 在 DPO json 中新增 `"error_type": "..."` 字段

2. **数据加载** (`train_dpo.py`):
   - `preprocess_multi_turn()` 需保留 error_type 字段
   - `DPODataCollatorWithPadding` 需传递 error_type 到 batch

3. **DPO Trainer** (`dpo_trainer.py`):
   - `__init__`: 接收 `gamma_map: Dict[str, float]`，error type → gamma 映射
   - `dpo_loss()`: 接收 per-sample `gamma` tensor 而非全局 `self.beta`
   ```python
   # 改动前
   losses = -F.logsigmoid(self.beta * logits)
   # 改动后
   gamma = gamma_per_sample  # shape: (batch_size,)
   losses = -F.logsigmoid(gamma * logits)
   ```
   - `get_batch_loss_metrics()`: 从 batch 中读取 error_type，查表得到 gamma
   - `compute_loss()`: 传递 gamma 到 dpo_loss

4. **Error Type 分类器** (新模块):
   - 分析 ALFWorld 失败轨迹，提取 error type
   - 可基于规则（task type + failure pattern）或模型分类
   - 需要定义 error taxonomy

### 4.2 ALFWorld Error Type 分析维度

```
Level 1: Task Type (来自 game_file 路径)
  - pick_and_place / pick_clean_then_place / pick_heat_then_place
  - pick_cool_then_place / look_at_obj / pick_two_obj

Level 2: Failure Pattern (需从轨迹分析)
  - wrong_object: 拿错了物品
  - wrong_receptacle: 去错了地方
  - missing_step: 跳过了必要步骤（如 clean/heat/cool）
  - repeated_action: 重复无效动作
  - max_steps_exceeded: 在正确方向但步数不够
  - parse_error: Agent 输出格式错误
```

### 4.3 改造工作量评估

| 模块 | 工作量 | 说明 |
|------|--------|------|
| Error type 分类器 | 2-3 天 | 规则 + 轨迹分析 |
| DPO data 格式扩展 | 0.5 天 | construct_preference.py 加字段 |
| DPOMultiTrainer 改造 | 1-2 天 | beta → per-sample gamma |
| Gamma 映射配置 | 0.5 天 | 超参搜索框架 |
| **总计** | **4-6 天** | |

---

## 5. 依赖列表与环境要求

### 主要依赖 (`requirements.txt`)
```
transformers==4.37.2
flash-attn==2.4.2
trl==0.7.7
accelerate>=0.21
peft
torch==2.1.0 (cu118)
alfworld
ai2thor==2.1.0
textworld[pddl]>=1.6.1
sentencepiece
wandb
```

### 硬件要求
- 训练: 4x GPU（run_eto.sh 默认 `node_num=4`），FSDP full_shard
- 推理/探索: 4 worker 各占 1 GPU
- Llama-2-7b: ~14GB VRAM per GPU (bf16)
- Qwen3-8B: ~16GB VRAM per GPU (bf16)，可用 A6000 (48GB)

### 版本注意事项
- `transformers==4.37.2` 较老，Qwen3 需要 ≥4.44
- `trl==0.7.7` 较老，建议升级或直接使用自定义 DPOMultiTrainer
- `openai==0.28` 是旧版 API，仅影响 OpenAI agent，不影响 FastChat agent
- ALFWorld 依赖 Java（ScienceWorld 的 scienceworld.jar）

---

## 6. 推荐适配策略

### Phase 1: Qwen3-8B 基础适配（MVP）
1. 升级 transformers 到 ≥4.44
2. 修改 FSDP wrap class
3. 添加 ChatML mask_labels 分支
4. 修复 tokenizer pad_token 设置
5. 端到端验证 SFT → explore → DPO 单轮迭代

### Phase 2: ETADN γ_e 注入
1. 实现 ALFWorld error type 分类器
2. 扩展 preference data 格式
3. 修改 DPOMultiTrainer 支持 per-sample gamma
4. 超参搜索 gamma_e 最优值

### 关键风险
- transformers 升级可能导致 FastChat 兼容性问题 → 考虑绕过 FastChat 服务层，直接用 vLLM
- DPO 多轮对话 tokenization 在 ChatML 下需仔细验证
- ALFWorld 环境 max_steps=40 可能不够 Qwen3 的 token budget
