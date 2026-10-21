# Phase B 前置条件技术方案

## 概要

Phase B (B-IAVR selective verification) 有两个前置条件。经代码分析，两者技术风险均低，总预估 4-6 Worker-hours。

---

## 前置 1: `<VERIFY>` Special Token 注册

### 现状

- Qwen3-1.7B tokenizer 将 `<VERIFY>` 拆成 3 个 sub-token: `<` (27) + `VERIFY` (46223) + `>` (29)
- B-IAVR 代码已实现（`ragen/biavr/verify_mechanism.py`），用字符串前缀匹配 `parse_verify_token()` 检测 `<VERIFY>`
- `ctx_manager.py` 在 `biavr_enabled` 时不添加 generation prompt prefix（让模型自由选择 `<VERIFY>` 或 `<think>`）

### 关键发现：无需 resize_token_embeddings

| 属性 | 值 |
|---|---|
| `config.json` vocab_size | 151936 |
| tokenizer vocab_size | 151643 |
| tokenizer len (含 added_tokens) | 151669 |
| 添加 `<VERIFY>` 后 | 151670 |
| 剩余空闲 slot | **266** |

模型 embedding 层已分配 151936 维，添加 `<VERIFY>` (id=151669→151670) 不触发 resize。这消除了 FSDP/vLLM 同步 resize 的风险。

### 方案：离线注册 + 保存扩展 tokenizer

**步骤 1: 创建扩展 tokenizer（一次性脚本）**

```python
from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained(SFT_CHECKPOINT_PATH)
tokenizer.add_special_tokens({"additional_special_tokens": ["<VERIFY>"]})
tokenizer.save_pretrained(EXTENDED_TOKENIZER_PATH)
# 同时 copy model weights（不变）到同一目录
```

输出目录作为 Phase B 的 `model_path`。

**步骤 2: 确认传播链一致**

tokenizer 在 4 处加载，需全部指向扩展版本：

| 加载点 | 文件 | 方式 |
|---|---|---|
| train.py `main()` | `train.py:L176` | `hf_tokenizer(model_path)` — 改 config model_path 即可 |
| FSDP actor `_build_model_optimizer` | `fsdp_workers.py:L308` | `hf_tokenizer(local_path)` — local_path 来自 model.path，同上 |
| FSDP ref | 同上 | 同 actor |
| vLLM rollout | `agent_proxy.py` VllmWrapperWg | `LLM(model_name)` — vLLM 自动从 model_name 读 tokenizer |

结论：只要 `model_path` 指向含扩展 tokenizer 的目录，所有组件自动对齐。

**步骤 3: 新 token 嵌入初始化**

Qwen3 embedding 层 151936 维中 [151669, 151936) 为零初始化。`<VERIFY>` 获得 id 151669，初始嵌入接近零向量。

建议：不做额外初始化。GRPO 训练会自然学习该 embedding。理由：
- `<VERIFY>` 语义全新（非已有概念的同义词），无合理初始化目标
- 初始阶段 lambda_init=0，verify 无惩罚，模型有充分空间探索
- 类似 `<think>` 等 tag 在 SFT 阶段也是从 chat template 学来的

### 代码改动清单

| 文件 | 改动 | 说明 |
|---|---|---|
| `scripts/prepare_biavr_tokenizer.py` | **新建** | 一次性脚本：加载 SFT checkpoint tokenizer → add `<VERIFY>` → 保存到新目录 |
| `config/_alfworld_phase_b.yaml` | 修改 `model_path` | 指向扩展 tokenizer 的 checkpoint 目录 |
| 无其他代码改动 | — | 框架自动从 model_path 读 tokenizer |

### 风险与 Fallback

| 风险 | 概率 | Fallback |
|---|---|---|
| vLLM 不认新 special token | 低 | vLLM 从 tokenizer.json 读 added_tokens，HF 格式兼容 |
| 新 token embedding 训练不收敛 | 低 | 用 `<think>` 平均 embedding 作初始化（`prepare_biavr_tokenizer.py` 中可选） |
| 模型倾向全部 verify 或全部不 verify | 中 | Lagrangian multiplier 自适应调节 verify rate，已在 reward.py 实现 |
| **不注册也能跑** | — | 当前 3-token 方案已可工作，注册 special token 是优化而非必须 |

**预估工作量：1-2 Worker-hours**（脚本编写 + 验证 tokenizer 一致性 + dry-run 测试）

---

## 前置 2: a_pre 推理开销量化

### 度量定义

a_pre（pre-verification action）是 B-IAVR 在 VERIFY 步生成的 counterfactual：用无 self-guidance 的 prompt 做 greedy decode，与实际 action 对比以判断 verification 是否 informative。

**核心度量：token 数**（非 latency/FLOPs），理由：
1. 论文 cost-efficiency metric 基于 token 数（与模型调用次数/长度成正比）
2. Latency 受 batch size、GPU 利用率等运行时因素影响，不可复现
3. Token 数直接映射到 FLOPs（FLOPs ≈ 6 × params × tokens for decode）

### 度量体系

| 度量名 | 定义 | 计算方式 |
|---|---|---|
| `C_verify_per_step` | 单次 verification 的 token 开销 | a_pre 生成的 token 数（max_tokens=256，实际通常更短） |
| `C_always_on` | Always-On 每 episode 总开销 | Σ(每步 self-guidance token 数) |
| `C_biavr(β)` | B-IAVR 目标 verify_rate=β 下的开销 | β × N_turns × avg(C_verify_per_step) |
| `savings(β)` | 相对 always-on 的节省比 | 1 - C_biavr(β) / C_always_on |
| `a_pre_overhead_ratio` | a_pre 占总推理的比例 | a_pre_tokens / (a_pre_tokens + normal_response_tokens) |

### 测量方案

**Phase A 数据收集（不需要额外实验）：**

Phase A always-on self-guidance 的每步 response 已包含 self-guidance reasoning。从 Phase A rollout 数据中可直接提取：

```python
# 从 rollout_states 中提取每步 response
for episode in rollout_states:
    for turn in episode['turns']:
        response_tokens = tokenizer.encode(turn['response'])
        # 记录：total_tokens, think_tokens, answer_tokens
```

**a_pre 开销估算（不需要真正生成 a_pre）：**

`pre_action.py` 中 `compute_pre_action_prompt` 设定 `max_tokens=256, temperature=0, top_k=1`。实际 a_pre 生成的 ALFWorld action 很短（典型 5-15 tokens，如 `go to desk 1`）。但 a_pre 还包括 `<think>...</think>` 推理，估计 30-80 tokens。

精确量化需运行一次 a_pre batch inference。方案：

1. 从 Phase A 最新 checkpoint 加载模型
2. 取 100 个 rollout 步的 conversation_history
3. 用 `build_pre_action_messages` 构建 a_pre prompt
4. 用 vLLM greedy decode 生成
5. 统计 token 数分布

### 实现方案

**步骤 1: 在 `agent_proxy.py` 添加 a_pre token 计数**

`_compute_and_update_a_pre` 方法（agent_proxy.py:411-435）已实现 a_pre 生成逻辑。只需在 biavr_tracker 中增加 token 统计：

```python
# agent_proxy.py, _compute_and_update_a_pre 中：
a_pre_tokens = len(tokenizer.encode(a_pre_response))
self.biavr_tracker.record_a_pre_cost(a_pre_tokens)
```

**步骤 2: 扩展 BIAVRTracker**

在 `ragen/biavr/reward.py` 的 `BIAVRTracker` 中增加：

```python
_a_pre_token_counts: List[int] = field(default_factory=list)

def record_a_pre_cost(self, n_tokens: int):
    self._a_pre_token_counts.append(n_tokens)

@property
def avg_a_pre_tokens(self) -> float:
    return sum(self._a_pre_token_counts) / max(len(self._a_pre_token_counts), 1)

def get_metrics(self) -> dict:
    # 在现有 metrics 基础上增加：
    metrics["biavr/avg_a_pre_tokens"] = self.avg_a_pre_tokens
    metrics["biavr/total_a_pre_tokens"] = sum(self._a_pre_token_counts)
    return metrics
```

**步骤 3: 基线开销脚本**

```python
# scripts/quantify_a_pre_cost.py
# 从 Phase A rollout 数据计算 always-on baseline
# 从 a_pre dry-run 计算 per-verify 开销
# 输出：C_always_on, C_verify_per_step, projected savings at β=0.3
```

### 代码改动清单

| 文件 | 改动 | 说明 |
|---|---|---|
| `ragen/biavr/reward.py` | 扩展 `BIAVRTracker` | 添加 a_pre token 计数和统计 |
| `ragen/llm_agent/agent_proxy.py` | `_compute_and_update_a_pre` | 记录 a_pre response token 数 |
| `scripts/quantify_a_pre_cost.py` | **新建** | 基线开销量化脚本 |
| `ragen/biavr/tests/test_biavr.py` | 增加测试 | 测试 token 计数逻辑 |

### 风险与 Fallback

| 风险 | 概率 | Fallback |
|---|---|---|
| a_pre 推理显著拖慢训练 | 中 | 采样子集（每 N 步做一次 a_pre），或异步计算 |
| a_pre response 过长（接近 max_tokens=256） | 低 | ALFWorld action 短，调低 max_tokens 到 128 |
| Phase A 还没产出可用 rollout 数据 | 取决于 Phase A 进度 | 用 SFT checkpoint 做 zero-shot rollout 估算 |

**预估工作量：2-3 Worker-hours**（tracker 扩展 + 脚本 + 从 Phase A 数据分析）

---

## 总结

| 前置条件 | 方案 | 核心改动 | 工作量 | 阻塞风险 |
|---|---|---|---|---|
| `<VERIFY>` token 注册 | 离线扩展 tokenizer，无需 resize_embeddings | 1 个新脚本 + 改 config | 1-2h | 低 |
| a_pre 开销量化 | BIAVRTracker 扩展 + 基线脚本 | 3 文件改动 + 1 个新脚本 | 2-3h | 低（依赖 Phase A 数据） |
| **合计** | | | **4-6h** | |

### 关键前提

1. Phase A 需先跑出至少一轮 rollout 数据用于 a_pre 开销基线估算
2. `<VERIFY>` token 注册可与 Phase A 并行进行（互不阻塞）
3. 如果 Phase A 验证 3-token `<VERIFY>` 序列已够用（模型能学会完整输出），可跳过 special token 注册

### 建议执行顺序

1. Phase A 实验继续推进，收集 rollout 数据
2. 并行：准备 `<VERIFY>` 扩展 tokenizer（prepare_biavr_tokenizer.py）
3. Phase A 有数据后：运行 a_pre 开销量化脚本
4. 两个前置条件完成 → 启动 Phase B 实验
