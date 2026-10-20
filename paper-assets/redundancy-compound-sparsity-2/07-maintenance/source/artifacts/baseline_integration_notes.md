# Baseline Integration Notes (H2O / R-KV / kvpress)

Date: 2026-05-12

---

## 1. H2O (Heavy-Hitter Oracle)

### 概要
- **论文**: NeurIPS 2023, [arXiv 2306.14048](https://arxiv.org/abs/2306.14048)
- **官方代码**: https://github.com/lenscloth/KVCache
- **核心思路**: 动态保留 "heavy hitter" tokens（累积 attention score 最高的 token）+ 最近 window tokens

### kvpress 集成
- kvpress 中 **没有** 名为 `H2OPress` 的类
- 最接近的等价：`ObservedAttentionPress` — 用 observed attention weights 作为 importance score，效果等同于 H2O
- `KnormPress`（key norm 排序）是另一个近似，但机制不同

### Budget Matching
- H2O 的 budget = `heavy_hitter_count + window_size`（绝对 token 数）
- 对应 CARC 的 `budget_ratio`：`budget = int(seq_len * budget_ratio)`
- H2O 在 R-KV 仓库实现中 `window_size = 1`，几乎全是 heavy hitter

### 关键超参
| 参数 | 默认值 | 说明 |
|------|--------|------|
| budget | 128 | 保留的 KV token 总数 |
| window_size | 1~8 | 最近 token 保护窗口 |

### Qwen2 兼容性
- H2O 机制与模型架构无关（只操作 attention scores），无已知 Qwen2 兼容性问题
- R-KV 仓库中的 H2O 实现已通过 `replace_qwen2()` monkeypatch 支持 Qwen2

---

## 2. R-KV (Redundancy-aware KV Cache Compression)

### 概要
- **论文**: NeurIPS 2025, [arXiv 2505.24133](https://arxiv.org/abs/2505.24133)
- **官方代码**: https://github.com/Zefan-Cai/R-KV
- **已 clone 到**: `/root/carc/r_kv_baseline/`
- **核心思路**: 同时评估 token 的 importance（attention score）和 non-redundancy（pairwise cosine dissimilarity），保留 informative + diverse 的 token

### 目录结构
```
r_kv_baseline/
├── HuggingFace/          # HF transformers 集成（主要使用这个）
│   ├── run_math.py       # 主评估脚本
│   ├── scripts/run.sh    # 启动脚本
│   ├── evaluation/       # eval 工具（grader, data_loader, latex2sympy）
│   └── rkv/
│       ├── monkeypatch.py    # replace_llama / replace_qwen2 / replace_qwen3
│       ├── modeling.py       # 修改后的 attention forward
│       ├── compression/
│       │   ├── r1_kv.py      # R-KV 核心实现
│       │   ├── h2o.py        # H2O baseline
│       │   ├── snapkv.py     # SnapKV baseline
│       │   └── streamingllm.py
│       └── utils.py          # compute_attention_scores, cal_similarity
├── SGLang/               # SGLang 集成（进行中）
├── vLLM/                 # vLLM 集成（进行中）
└── FlashInfer/           # FlashInfer 集成
```

### DeepSeek-R1-Distill-Qwen-14B 支持
- **确认支持**：`monkeypatch.py` 中有 `replace_qwen2(compression_config)` 函数
- DeepSeek-R1-Distill-Qwen-14B 基于 Qwen2 架构，直接使用 `replace_qwen2`

### 核心算法 (R1KV.update_kv)
```python
# 1. 计算 attention importance（窗口内 softmax attention 的 mean → MaxPool1d 平滑）
attn_cache = MaxPool1d(softmax(attn_weights[:, :, -window:, :-window]).mean(dim=-2))

# 2. 计算 redundancy（pairwise cosine similarity → 聚合）
similarity_cos = cal_similarity(key_states, retain_ratio=0.1, retain_direction="last")

# 3. 混合打分（λ=0.07 → 重 redundancy）
final_score = attn_cache * λ - similarity_cos * (1 - λ)

# 4. Top-k 保留
indices = final_score.topk(budget - window_size, dim=-1).indices
```

### Budget Matching
- R-KV 使用 `kv_budget`（绝对 token 数）
- 对应 CARC 的 `budget_ratio`：`kv_budget = int(seq_len * budget_ratio)`
- R-KV 论文实验设置：budget = 10%~34% of seq_len

### O(B²) Pairwise Scoring
- `cal_similarity()` 计算 `k_norm @ k_norm.T`（seq_len × seq_len 矩阵）
- 复杂度：O(L² × d) per head per step，其中 L = 当前 KV cache 长度
- 在 decoding 阶段，每生成一个 token 都要重算一次（budget 固定后是 O(budget²)）
- budget=128 时：128² × 128 ≈ 2M ops per head，8 KV heads → 16M ops per step

### 关键超参
| 参数 | 默认值 | 说明 |
|------|--------|------|
| budget | 128 | 保留的 KV token 总数 |
| window_size | 8 | 最近 token 保护窗口 |
| kernel_size | 7 | attention pooling kernel |
| mix_lambda | 0.07 | importance vs redundancy 权重（小值 → 重 redundancy）|
| retain_ratio | 0.1 | similarity 保留比例 |
| retain_direction | "last" | 保留最新的相似 token |

### 运行方式
```bash
cd /root/carc/r_kv_baseline/HuggingFace
pip install -e ..  # 安装 rkv 包
python run_math.py \
    --dataset_path ./data/aime24.jsonl \
    --model_path deepseek-ai/DeepSeek-R1-Distill-Qwen-14B \
    --method rkv --kv_budget 128 --max_length 16384
```

---

## 3. kvpress 兼容性检查结果

### 环境
- kvpress v0.5.3（服务器 westd-16980 已安装）
- Python 3.x + conda base

### 支持的 Press 类型（37个）
```
AdaKVPress          BlockPress         ChunkKVPress       ChunkPress
CompactorPress      ComposedPress      CRITICALAdaKVPress CriticalKVPress
CURPress            DMSPress           DecodingPress      DuoAttentionPress
ExpectedAttentionPress  ExpectedAttentionStatsPress  FastKVzipPress  FinchPress
KVComposePress      KVzapPress         KVzipPress         KeyDiffPress
KeyRerotationPress  KnormPress         LagKVPress         LeverageScorePress
NonCausalAttnPress  ObservedAttentionPress  PerLayerCompressionPress
PrefillDecodingPress  PyramidKVPress   QFilterPress       RandomPress
ScorerPress         SimLayerKVPress    SnapKVPress        StreamingLLMPress
TOVAPress           ThinKPress
```

### SUPPORTED_MODELS
```python
LlamaForCausalLM      # ✅
MistralForCausalLM    # ✅
Phi3ForCausalLM       # ✅
Qwen2ForCausalLM      # ✅ DeepSeek-R1-Distill-Qwen-14B
Qwen3ForCausalLM      # ✅
Gemma3ForConditionalGeneration  # ✅
```

**Qwen2 完全支持**，DeepSeek-R1-Distill-Qwen-14B 可直接使用所有 kvpress 方法。

### BasePress API
```python
class BasePress:
    compression_ratio: float  # 0.0~1.0, 移除的 KV 比例

    def compress(self, module, hidden_states, keys, values, attentions, kwargs)
        -> (keys, values)  # 压缩后的 KV

    def forward_hook(self, module, input, kwargs, output)  # 自动挂到 attention 层

    def post_init_from_model(self, model)  # 模型绑定后的初始化
```

### ScorerPress API（自定义评分方法的基类）
```python
class ScorerPress(BasePress):
    def score(self, module, hidden_states, keys, values, attentions, kwargs)
        -> torch.Tensor  # shape: (batch, num_kv_heads, seq_len)
        # 返回 importance score，最低分的 token 被剪枝
```

---

## 4. Custom Press 接入可行性评估

### EMA Eviction → kvpress ScorerPress

**可行**。封装方案：

```python
from kvpress.presses.scorer_press import ScorerPress
from dataclasses import dataclass

@dataclass
class CARCEMAPress(ScorerPress):
    gamma: float = 0.9
    grace_window: int = 175

    def score(self, module, hidden_states, keys, values, attentions, kwargs):
        # keys: (batch, num_kv_heads, seq_len, head_dim)
        # 计算 EMA similarity score，返回负值（低分 = 高 redundancy = 应被剪枝）
        batch, heads, seq_len, dim = keys.shape
        scores = torch.zeros(batch, heads, seq_len, device=keys.device)

        # 1. 计算 EMA anchor 和 similarity
        # 2. 累积 similarity → 高 similarity = 高 redundancy = 低 importance
        # 3. 返回 -cumulative_similarity 作为 score（kvpress 保留高分 token）

        # Grace window: 最近 token 给极高分，不被剪枝
        scores[:, :, -self.grace_window:] = float('inf')
        return scores
```

### 注意事项
1. kvpress 在 **prefill 阶段** 一次性压缩，不是 per-step eviction
2. CARC 的 EMA 是 per-step 累积的，需要适配为一次性评分
3. 可考虑用 `DecodingPress` wrapper 在 decoding 阶段也做压缩

### R-KV → kvpress 集成
- **不直接可行**：R-KV 需要 monkeypatch attention forward，与 kvpress 的 hook 机制冲突
- **替代方案**：R-KV 仓库自带独立 eval pipeline，直接运行即可

---

## 5. SkipKV / FASA 补充调研

### SkipKV
- **无公开代码仓库**
- 搜索未找到同名项目

### FASA (Frequency-Aware Sparse Attention)
- **论文**: [arXiv 2602.03152](https://arxiv.org/abs/2602.03152)
- **无公开代码**
- 核心：基于频率域分析 attention 稀疏性，决定 token eviction
- 不可在 kvpress 中直接集成（无代码）

---

## 6. eval_framework.py 设计说明

### 位置
`/root/carc/eval_framework.py`

### 架构
```
eval_framework.py
├── Strategy Registry
│   ├── CARC_STRATEGIES: {full, ema_0.9, ema_0.7, ema_0.5, random, recency}
│   └── KVPRESS_STRATEGIES: {knorm, snapkv, streaming_llm, tova, keydiff,
│                             expected_attn, observed_attn, h2o, random_press}
├── Data Loading
│   ├── load_wikitext_samples(tokenizer, num_samples, seq_len)
│   └── load_math500(num_problems)
├── PPL Evaluation
│   ├── eval_ppl_full()          — full cache baseline
│   ├── eval_ppl_kvpress()       — kvpress 方法
│   └── eval_ppl_carc()          — CARC native 方法
├── MATH-500 Evaluation
│   ├── eval_math_kvpress()      — kvpress pipeline + boxed 答案检查
│   └── eval_math_carc()         — CARCGenerator + 答案检查
├── Unified Dispatcher
│   └── run_eval(model, tokenizer, strategy, budget, dataset, ...) → dict
└── CLI (argparse)
    --model, --strategies, --budget-ratios, --datasets, --output, --gpu, --dry-run
```

### 验证状态
- `python eval_framework.py --help` ✅
- `python eval_framework.py --dry-run` ✅ (kvpress v0.5.3, CARC imports OK)

### Budget 统一语义
- `budget_ratio` = 保留比例（0.5 = 保留 50% KV cache）
- kvpress: `compression_ratio = 1.0 - budget_ratio`
- CARC: `budget = int(seq_len * budget_ratio)`
- R-KV: `kv_budget = int(seq_len * budget_ratio)`

### 输出格式
```json
{
  "metadata": { "model": "...", "strategies": [...], ... },
  "results": [
    { "strategy": "ema_0.9", "budget_ratio": 0.5, "dataset": "wikitext_2k", "ppl": 5.23, "elapsed_s": 45.2 },
    { "strategy": "knorm", "budget_ratio": 0.5, "dataset": "math500", "accuracy": 0.82, "correct": 82, "total": 100 }
  ]
}
```
