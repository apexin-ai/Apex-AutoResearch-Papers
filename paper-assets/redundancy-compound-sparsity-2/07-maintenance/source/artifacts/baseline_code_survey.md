# Baseline Code Survey: KV Cache Eviction Methods

> Date: 2026-05-12 | Project: CARC (O(1) KV Cache Eviction)

---

## 1. kvpress 框架调研

### 概述
- **PyPI**: `pip install kvpress`
- **GitHub**: [NVIDIA/kvpress](https://github.com/NVIDIA/kvpress)
- **定位**: 统一的 KV cache compression 框架，基于 HuggingFace transformers，NVIDIA 维护

### Qwen2 兼容性
**已确认支持。** README 明确列出测试过的架构：
- `LlamaForCausalLM`, `MistralForCausalLM`, `Phi3ForCausalLM`
- **`Qwen2ForCausalLM`**, `Qwen3ForCausalLM`, `Gemma3ForCausalLM`

DeepSeek-R1-Distill-Qwen-14B 基于 Qwen2 架构，直接兼容。

### 支持的 Press 清单（30+）

| Press | 类型 | 说明 |
|-------|------|------|
| `ExpectedAttentionPress` | Scorer | 估计期望注意力分数 |
| `SnapKVPress` | Scorer | 观察窗口 + 池化选 token |
| `TOVAPress` | Scorer | 当前步注意力权重 evict |
| `StreamingLLMPress` | Scorer | Sink + recent window |
| `KnormPress` | Scorer | Key 向量范数 |
| `RandomPress` | Scorer | 随机 eviction（baseline） |
| `ThinKPress` | Scorer | 通道剪枝 |
| `CriticalKVPress` | Scorer | L1(Wo @ V) 重要性 |
| `CriticalAdaKVPress` | Scorer | Critical + 自适应 head 分配 |
| `SimLayerKVPress` | Scorer | 层间相似性 |
| `DuoAttentionPress` | Scorer | 双流注意力 |
| `FinchPress` | Scorer | Finch 算法 |
| `KVzipPress` | Scorer | KVzip 门控蒸馏 |
| `AdaKVPress` | Wrapper | 自适应 per-head budget |
| `ComposedPress` | Wrapper | 组合多个 press |
| `DecodingPress` | Wrapper | 解码阶段压缩 |
| `PrefillDecodingPress` | Wrapper | Prefill + Decoding 联合 |

### API 用法

```python
from transformers import pipeline
from kvpress import ExpectedAttentionPress

pipe = pipeline("kv-press-text-generation", model="deepseek-ai/DeepSeek-R1-Distill-Qwen-14B")
press = ExpectedAttentionPress(compression_ratio=0.5)
answer = pipe(context, question=question, press=press)["answer"]
```

### 安装与依赖
```bash
pip install kvpress
# 可选：flash-attn, optimum-quanto (量化)
# 开发模式：
git clone https://github.com/NVIDIA/kvpress.git && cd kvpress
uv sync --extra eval --extra flash-attn
```
- 无显式 Python/PyTorch 版本要求，依赖 transformers >= 4.x
- Python 3.10 + PyTorch 2.x + CUDA 12.x 环境应无兼容性问题

### 评估能力
- 内置 RULER benchmark (4k context)
- 支持 AIME25、Math500 数学推理 benchmark
- HuggingFace Leaderboard 集成
- `speed_and_memory.ipynb` 性能分析

---

## 2. R-KV 代码调研

### 概述
- **GitHub**: [Zefan-Cai/R-KV](https://github.com/Zefan-Cai/R-KV)
- **论文**: NeurIPS 2025
- **定位**: 面向推理模型的 KV cache 压缩，兼顾 importance 和 redundancy

### DeepSeek-R1-Distill-Qwen-14B 支持
**直接支持。** 官方 benchmark 显式包含：
- DeepSeek-R1-Distill-Llama-8B
- **DeepSeek-R1-Distill-Qwen-14B**

### 核心机制
1. **Importance scoring**: 注意力分数累积，O(α × B_budget)
2. **Redundancy scoring**: Key 向量 pairwise 相似度，**O(B_budget²)**
3. **Joint eviction**: λ 加权平衡 importance 和 redundancy

### 关键超参数
- `kv_budget`: 保留的 KV 对数（如 128）
- `observation_tokens`: 观察窗口大小（如 8）
- λ: importance/redundancy 权衡（默认 0.1）

### 运行方式
```bash
python3 ./run_math.py \
  --dataset_path ./data/aime24.jsonl \
  --model_path deepseek-ai/DeepSeek-R1-Distill-Qwen-14B \
  --method rkv \
  --kv_budget 128
```

### 代码结构
```
R-KV/
├── HuggingFace/     # 主要集成
├── vLLM/            # vLLM 后端
├── SGLang/          # SGLang 后端
├── FlashInfer/      # FlashInfer 后端
├── rkv/             # 核心压缩逻辑
├── evaluation/      # benchmark 工具 (latex2sympy)
└── examples/eval.sh # 评估脚本
```

### 安装
```bash
pip install -r requirements.txt
pip install -e .
# Flash Attention 推荐但非必需
```

### 评估 Benchmark
- MATH-500（平均 2,979 tokens/solution）
- AIME 2024（平均 15,536 tokens/solution）

---

## 3. 竞品清单（Signal Taxonomy）

### 按计算复杂度分类

| 方法 | 复杂度 (per step) | Content-Aware | Recurrence-Aware | 官方代码 | 论文 |
|------|-------------------|---------------|-------------------|----------|------|
| **StreamingLLM** | O(1) | ✗ (position only) | ✗ | [MIT-Han-Lab/streaming-llm](https://github.com/MIT-Han-Lab/streaming-llm) / kvpress 内置 | ICLR 2024 |
| **CARC (ours)** | O(1) | ✓ (EMA centroid sim) | ✓ | — | — |
| **TOVA** | O(B) | ✓ (attn weights) | ✗ | [schwartz-lab-NLP/TOVA](https://github.com/schwartz-lab-NLP/TOVA) / kvpress 内置 | 2024 |
| **H2O** | O(B) | ✓ (cumul. attn) | ✗ | [FMInference/H2O](https://github.com/FMInference/H2O) / kvpress 内置 | NeurIPS 2023 |
| **KnormPress** | O(B) | ✓ (key norm) | ✗ | kvpress 内置 | — |
| **SnapKV** | O(L_obs) prefill-only | ✓ (obs. window attn) | ✗ | kvpress 内置 / [KVCache-Factory](https://github.com/Zefan-Cai/KVCache-Factory) | NeurIPS 2024 |
| **AdaKV** | O(B) | ✓ (adaptive head budget) | ✗ | [FFY0/AdaKV](https://github.com/FFY0/AdaKV) / kvpress 内置 | NeurIPS 2025 |
| **CakeKV** | O(B) | ✓ (layer-aware cascade) | ✗ | [antgroup/cakekv](https://github.com/antgroup/cakekv) | ICLR 2025 |
| **HeadKV** | O(B) | ✓ (head-level) | Partial | [FYYFU/HeadKV](https://github.com/FYYFU/HeadKV) | ICLR 2025 |
| **R-KV** | O(B²) | ✓ (pairwise key sim) | ✓ | [Zefan-Cai/R-KV](https://github.com/Zefan-Cai/R-KV) | NeurIPS 2025 |
| **FASA** | O(L × k_FC) | ✓ (freq. chunk) | ✓ | [AMAP-ML/FASA-ICLR2026](https://github.com/AMAP-ML/FASA-ICLR2026) | ICLR 2026 |
| **KVzip** | O(B) | ✓ (gated distill) | ✗ | [snu-mllab/KVzip](https://github.com/snu-mllab/KVzip) / kvpress 内置 | NeurIPS 2025 Oral |
| **DefensiveKV** | O(B) | ✓ (defensive evict) | ✗ | [FFY0/DefensiveKV](https://github.com/FFY0/DefensiveKV) | ICLR 2026 |

> **B** = budget size (retained tokens), **L** = sequence length, **L_obs** = observation window, **k_FC** = number of dominant frequency chunks (k_FC ≪ d)

### CARC 的竞争优势定位

| 维度 | StreamingLLM | H2O/TOVA | SnapKV | R-KV | FASA | **CARC** |
|------|-------------|----------|--------|------|------|----------|
| Per-token 复杂度 | O(1) | O(B) | O(L_obs) | O(B²) | O(L×k) | **O(1)** |
| Content-aware | ✗ | ✓ | ✓ | ✓ | ✓ | **✓** |
| Recurrence-aware | ✗ | ✗ | ✗ | ✓ | ✓ | **✓** |
| 唯一的 O(1) + content-aware + recurrence-aware | — | — | — | — | — | **✓** |

---

## 4. 安装可行性（Python 3.10 + PyTorch 2.x + CUDA 12.x）

### kvpress
```bash
pip install kvpress
# 预期无冲突。依赖 transformers, torch，均兼容目标环境。
# 可选: pip install flash-attn --no-build-isolation (需 CUDA toolkit)
```

### R-KV
```bash
git clone https://github.com/Zefan-Cai/R-KV.git
cd R-KV
pip install -r requirements.txt
pip install -e .
# 注意: evaluation/ 下有 latex2sympy 依赖需单独构建
# Flash Attention 推荐: pip install flash-attn --no-build-isolation
```

### H2O（独立使用）
```bash
git clone https://github.com/FMInference/H2O.git
# 或直接用 kvpress 内置的 H2OPress（更推荐）
```

### 潜在冲突点
1. **flash-attn** 编译需匹配 CUDA toolkit 版本，建议用 `pip install flash-attn --no-build-isolation`
2. **R-KV 的 latex2sympy** 用于评估 MATH/AIME，非核心依赖
3. **kvpress 与 R-KV 可共存**——kvpress 是 pip 包，R-KV 是独立 repo，依赖不冲突

### 推荐安装顺序
```bash
# 1. 基础框架
pip install kvpress

# 2. R-KV baseline
git clone https://github.com/Zefan-Cai/R-KV.git
cd R-KV && pip install -r requirements.txt && pip install -e .

# 3. 验证
python -c "from kvpress import ExpectedAttentionPress; print('kvpress OK')"
python -c "import rkv; print('R-KV OK')"
```

---

## 5. 推荐 Baseline 选择

### Primary Baselines（必须对比）
1. **H2O** — 经典 attention-based eviction，NeurIPS 2023，通过 kvpress 直接可用
2. **R-KV** — 唯一的 reasoning-aware baseline，NeurIPS 2025，直接支持 Qwen-14B

### Secondary Baselines（增强论文说服力）
3. **SnapKV** — Prefill-phase 压缩代表，NeurIPS 2024，kvpress 内置
4. **StreamingLLM** — O(1) position-only baseline，凸显 CARC 的 content-aware 优势
5. **FASA** — ICLR 2026 最新竞品，frequency-aware，reasoning-aware

### 对比叙事
- vs StreamingLLM: 同为 O(1)，但 CARC content-aware → 更好的压缩质量
- vs H2O/TOVA: CARC O(1) vs O(B) → 更快，且 recurrence-aware
- vs R-KV: CARC O(1) vs O(B²) → 显著更快，相当或更优的压缩质量
- vs FASA: CARC O(1) vs O(L×k) → 更简单，无需频率分解
