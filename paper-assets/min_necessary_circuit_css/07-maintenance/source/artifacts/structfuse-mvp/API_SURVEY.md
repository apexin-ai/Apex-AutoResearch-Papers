# Circuit Discovery API Survey

> 调研日期：2026-05-12
> 目标：确认 EAP-IG / AtP* / Edge Pruning / ACDC 四种电路发现方法的库、API、兼容性，以及 CIRCUS / MIB 的可复用性。

---

## 1. TransformerLens

- **Version**: 3.2.1（2026-05-09 发布）；v2.x 仍可通过 `pip install 'transformer-lens~=2.0'` 安装
- **Install**: `pip install transformer-lens`
- **Python**: >=3.10, <4.0
- **Torch**: 未在 PyPI 显式声明最低版本，实际兼容 torch >=2.1
- **GPT-2 Small 加载**:
  ```python
  from transformer_lens import HookedTransformer
  model = HookedTransformer.from_pretrained("gpt2-small")
  # v3.x 推荐 TransformerBridge，但 HookedTransformer 仍可用
  ```
- **IOI Dataset API**:
  ```python
  from transformer_lens.evals import ioi_eval, IOIDataset
  dataset = IOIDataset(
      tokenizer=model.tokenizer,
      num_samples=100,
  )
  # dataset.toks: tokenized sentences
  # dataset.s_tokenIDs / dataset.io_tokenIDs: subject/IO token positions
  # ioi_eval(model) → (avg_logit_diff, accuracy)
  ```
- **Hook 机制**（edge-level attribution 基础）:
  ```python
  # 每个组件有标准 hook point name, e.g.:
  # "blocks.{layer}.attn.hook_result"  (attention output)
  # "blocks.{layer}.mlp.hook_post"     (MLP output)
  # "blocks.{layer}.hook_resid_pre"    (residual stream)
  cache = {}
  model.run_with_cache(tokens, names_filter=lambda name: "hook_result" in name)
  ```
- **Source**: [PyPI](https://pypi.org/project/transformer-lens/) · [GitHub](https://github.com/TransformerLensOrg/TransformerLens)

---

## 2. EAP-IG（Edge Attribution Patching with Integrated Gradients）

- **Repo**: https://github.com/hannamw/eap-ig
- **Package**: `eap` v2.0.0
- **Install**:
  ```bash
  git clone https://github.com/hannamw/eap-ig.git
  cd eap-ig && pip install .
  # 可选可视化: pip install .[viz]  (需系统装 graphviz)
  ```
- **Python**: >=3.10
- **Dependencies**: `transformer-lens >= 2.15.0`, `matplotlib >= 3.10.1`
- **核心 API（4 步流程）**:
  ```python
  from eap import Graph, attribute, evaluate_graph, EAPDataset

  # 1. 加载模型
  model = HookedTransformer.from_pretrained("gpt2-small")

  # 2. 构建计算图（自动从模型结构提取 nodes/edges）
  graph = Graph.from_model(model)

  # 3. 计算 edge attribution scores
  dataloader = EAPDataset('greater-than').to_dataloader()
  metric = ...  # 自定义 metric function
  attribute(
      model, graph, dataloader, metric,
      method='EAP-IG-inputs',  # 或 'EAP-IG-activations', 'EAP'
      ig_steps=5               # IG 插值步数 m
  )
  # graph 内部存储每条 edge 的 attribution score

  # 4. Top-K thresholding → binary circuit
  graph.apply_topn(n=100)   # 保留 top-100 edges
  results = evaluate_graph(model, graph, dataloader, metric)
  ```
- **Attribution 方法**:
  | 方法 | 复杂度 | 说明 |
  |------|--------|------|
  | `EAP` | O(1) | 一阶近似 |
  | `EAP-IG-inputs` | O(m) | 输入 embedding 层面的 IG |
  | `EAP-IG-activations` | O(m) | 每个组件 activation 层面的 IG |
  | `clean-corrupted` | O(2) | 两点梯度 |
- **Output**: `Graph` 对象，每条 edge 有 `.score` 属性；`apply_topn(n)` 后变为 binary mask
- **模型兼容**: GPT-2, Pythia, Mistral, Llama, Qwen, OLMo, Gemma（需 pre-LayerNorm；GQA 模型需 `model.cfg.ungroup_grouped_query_attention = True`）
- **论文**: Syed et al. 2023 "Attribution Patching Outperforms Automated Circuit Discovery"；Hanna et al. 2024 "Have Faith in Faithfulness"

---

## 3. AtP*（Attribution Patching Star）

- **论文**: Kramár et al. 2024, "AtP*: An efficient and scalable method for localizing LLM behaviour to components" ([arXiv:2403.00745](https://arxiv.org/abs/2403.00745))
- **官方代码**: DeepMind 未开源官方实现
- **社区实现**: https://github.com/koayon/atp_star（非官方，PyTorch + NNsight 实现）
- **Install**: `git clone https://github.com/koayon/atp_star.git`（无 PyPI 包，无 pyproject.toml / requirements.txt 公开）
- **Dependencies**: PyTorch, NNsight（用于 caching/interventions）
- **核心改进**（相对于标准 AtP）:
  1. **QK-Fix**: 对 attention 节点显式线性化 attention probabilities（而非 softmax inputs）
  2. **GradDrop**: 将 residual skip 路径上的 gradient 置零，消除 path-cancellation
- **关键文件**: `atp.py`（核心算法）, `interventions.py`（干预机制）, `main.py`（入口）
- **Output**: 组件级别的 attribution scores（node-level，非 edge-level）
- **状态**: 开发中，尚不成熟；核心 AtP + QK-Fix 已实现，GPU 优化和 circuit-finding 部分仍 WIP
- **⚠️ 注意**: AtP* 原论文是 **node-level** localization（定位重要组件），不直接产出 edge-level scores。要得到 edge-level circuit 需额外适配。

---

## 4. Edge Pruning

- **Repo**: https://github.com/princeton-nlp/edge-pruning（NeurIPS 2024 Spotlight）
- **论文**: Bhaskar et al. 2024, "Finding Transformer Circuits with Edge Pruning"
- **Install**:
  ```bash
  git clone https://github.com/princeton-nlp/edge-pruning.git
  cd edge-pruning
  pip install -r requirements.txt
  # GPT-2 + 新版 transformers: pip install -r requirements-experimental.txt
  ```
- **Dependencies（requirements.txt，原版）**:
  - `torch == 2.5.1+cu121`
  - `transformer-lens == 2.15.0`
  - `accelerate == 1.2.1`, `datasets == 3.2.0`, `einops == 0.8.1`
  - `flash-attn == 2.7.2.post1`
  - `numpy == 2.2.3`, `scipy == 1.15.2`, `networkx == 3.4.2`
  - `jax == 0.5.2`, `tensorflow == 2.18.0`（用于 Tracr 实验，非核心）
- **Dependencies（requirements-experimental.txt，新版）**:
  - `torch == 2.7.1`
  - `transformers == 4.54.0`（HuggingFace，**不再依赖 TransformerLens**）
  - `flash_attn == 2.8.2`, `accelerate == 1.9.0`
- **核心方法**: 使用 L0 regularization 对 edge masks 进行可微优化（非贪心搜索），mask 值连续优化后 threshold → binary
- **Key Scripts**:
  | 任务 | Pruning 脚本 | 评估脚本 |
  |------|-------------|---------|
  | IOI | `src/prune/fpt2_ioi.py` | `src/eval/ioi.py` |
  | Greater-Than | `src/prune/fpt2_gt.py` | `src/eval/gt.py` |
  | Gendered Pronoun | `src/prune/fpt2_gp.py` | `src/eval/gp.py` |
  | CodeLlama Boolean | `src/prune/fllama_boolean_expressions_*.py` | `src/eval/boolean_expressions.py` |
- **Output**: JSON 格式的 edge set（pruned circuit），可通过 `src/modeling/vis_fpt2.py` 可视化
- **⚠️ 注意**: 原版依赖 `transformer-lens==2.15.0`；实验版已迁移到 HuggingFace `transformers`。**不使用 nnsight**。

---

## 5. ACDC（Automatic Circuit Discovery）

- **Repo**: https://github.com/ArthurConmy/Automatic-Circuit-Discovery（NeurIPS 2023 Spotlight）
- **论文**: Conmy et al. 2023, "Towards Automated Circuit Discovery for Mechanistic Interpretability"
- **Install**:
  ```bash
  git clone https://github.com/ArthurConmy/Automatic-Circuit-Discovery.git
  cd Automatic-Circuit-Discovery
  # 推荐用 poetry:
  poetry env use 3.10
  poetry install
  # 或 conda/venv + pip install -e .
  ```
- **System deps**: `graphviz`, `libgraphviz-dev`（Ubuntu）或 `brew install graphviz`（Mac）
- **Python**: >=3.8（推荐 3.10）
- **Dependencies**: TransformerLens（HookPoints + HookedTransformer 抽象），具体版本由 poetry.lock 管理
- **核心 API**:
  ```python
  # 主入口: acdc/main.py
  # IOI 示例: 加载 GPT-2 Small + IOI dataset
  from acdc.ioi.utils import get_ioi_gpt2_small
  model, dataset = get_ioi_gpt2_small()

  # 运行 ACDC 搜索（迭代 knock-out + 恢复）
  # 见 notebooks/colabs/ACDC_Main_Demo.ipynb
  ```
- **算法**: 迭代地逐条删除 edge，检查 metric 变化是否超过 threshold τ；不超过则永久删除
- **Output**: 计算图中保留的 edge set。GPT-2 Small + IOI 任务上从 ~32,000 edges 筛选出 68 条。
- **⚠️ 推荐替代**: 作者推荐使用 **Auto-Circuit**（`pip install auto-circuit`）替代原始 ACDC 代码库

### 5.1 Auto-Circuit（推荐的现代替代）

- **Repo**: https://github.com/UFO-101/auto-circuit
- **Install**: `pip install auto-circuit`
- **Python**: >=3.10
- **Dependencies**: `transformer-lens >= 1.13.0`, `torch >= 2.1.1`, `einops >= 0.6.1`, `plotly >= 5.18.0`
- **核心 API**:
  ```python
  from auto_circuit.model_utils.micro_model_utils import MicroModel
  from auto_circuit.prune_algos.mask_gradient import mask_gradient_prune_scores
  from auto_circuit.types import PatchType

  # Attribution-based circuit discovery
  scores = mask_gradient_prune_scores(
      model=model, dataloader=test_loader, grad_function="logit"
  )

  # Edge patching
  from auto_circuit.utils.patch_mode import patch_mode
  patch_edges = ["Resid Start->MLP 2", "MLP 2->A2.4.Q", "A2.4->Resid End"]
  with patch_mode(model, ablations, patch_edges):
      patched_out = model(tokens)
  ```
- **支持方法**: ACDC, mask gradient pruning, attribution patching 等多种算法
- **论文**: COLM 2024 Oral Spotlight, "Transformer Circuit Metrics are not Robust"

---

## 6. CIRCUS（Circuit Consensus under Uncertainty via Stability Ensembles）

- **论文**: Parekh 2026, [arXiv:2603.00523](https://arxiv.org/abs/2603.00523)
- **代码**: **未开源**（截至 2026-05-12 无 GitHub 仓库）
- **方法概述**: Config-bagging over pruning thresholds
  1. 对单次 attribution run 的结果，用 B 组不同 pruning 配置（node threshold × edge threshold 网格）进行裁剪
  2. 每条 edge 计算 stability score: `s(e) = (1/B) Σ 𝟙[e ∈ E^(b)]`
  3. 按 stability score 划分三层:
     - **Core**: s(e) = 1（所有配置都保留）
     - **Contingent**: 0.5 ≤ s(e) < 1（替代路径）
     - **Noise**: s(e) < 0.5
- **参数**: 主实验用 B=9（3×3 网格），稳定性分析用 B=25（5×5 网格）
- **Base Attribution**: 基于 cross-layer transcoders (CLTs) 的 attribution graph，**不直接 wrap EAP-IG/ACDC**
- **模型**: Gemma-2-2B（50 prompts），Llama-3.2-1B（20 prompts）
- **结果**: Consensus circuit 比 union 小 ~40×，faithfulness 相当
- **⚠️ 自行复现**: 核心逻辑简单——对任意 edge-level scores 做多阈值 bagging，可用 ~50 行 Python 实现:
  ```python
  def config_bag(edge_scores, thresholds, B=9):
      """edge_scores: dict{edge: float}, thresholds: list of cutoff values"""
      counts = {e: 0 for e in edge_scores}
      for t in thresholds:
          for e, s in edge_scores.items():
              if s >= t:
                  counts[e] += 1
      return {e: counts[e] / len(thresholds) for e in edge_scores}
  ```

---

## 7. MIB Benchmark（Mechanistic Interpretability Benchmark）

- **论文**: Mueller et al. 2025, [arXiv:2504.13151](https://arxiv.org/abs/2504.13151)（ICML 2025）
- **Landing page**: https://github.com/aaronmueller/MIB
- **Circuit Track 代码**: https://github.com/hannamw/MIB-circuit-track
- **Install**:
  ```bash
  git clone https://github.com/hannamw/MIB-circuit-track.git
  cd MIB-circuit-track
  git submodule update --init --recursive  # 拉取 EAP-IG 子模块
  pip install .
  ```
- **测试环境**: `torch == 2.4.1`
- **支持的 Circuit Discovery 方法**:
  - EAP（node / edge / neuron 级别，通过 `--level` 参数）
  - EAP-IG（inputs / activations 两种变体）
  - Exact Activation Patching
  - Information Flow Routes (IFR)
  - Uniform Gradient Sampling (UGS)
  - EAP with Optimal Ablations
- **模型**: GPT-2 Small, Qwen-2.5-0.5B, Gemma-2-2B, Llama-3.1-8B, InterpBench（含 ground-truth circuit）
- **任务**: IOI, MCQA, Arithmetic, ARC, RAVEL
- **运行**:
  ```bash
  # Attribution
  python run_attribution.py --models gpt2-small --tasks ioi --method EAP-IG-inputs --level edge

  # Evaluation
  python run_evaluation.py --models gpt2-small --tasks ioi
  ```
- **Circuit 格式**:
  - 浮点 scores: 单个 `.json` / `.pt` 文件，`{edge_name: float_score}`
  - Binary circuits: 9 个文件，对应 edge 比例 thresholds（0.1%, 0.2%, 0.5%, 1%, 2%, 5%, 10%, 20%, 50%）
- **评估指标**:
  - **CPR**（Circuit Performance Ratio）: 电路独立执行时的性能保留率
  - **CMD**（Circuit-Model Difference）: 电路行为与完整模型行为的差异
- **⚠️ 复用价值**: MIB circuit track 基于 EAP-IG 库构建，可直接作为标准化评估框架使用

---

## 8. Compatibility Matrix

### Python 版本

| 库 | Python 要求 |
|----|------------|
| TransformerLens 3.x | >=3.10 |
| EAP-IG 2.0 | >=3.10 |
| Edge Pruning | >=3.10（推断） |
| ACDC | >=3.8（推荐 3.10） |
| Auto-Circuit | >=3.10 |
| AtP*（社区版） | >=3.10（推断） |

**结论**: Python 3.10 是所有库的安全基线。

### PyTorch 版本

| 库 | Torch 版本 |
|----|-----------|
| TransformerLens 3.x | >=2.1 |
| EAP-IG 2.0 | 未声明（跟随 TransformerLens） |
| Edge Pruning（原版） | ==2.5.1+cu121 |
| Edge Pruning（实验版） | ==2.7.1 |
| ACDC | 未显式声明 |
| Auto-Circuit | >=2.1.1 |
| MIB Circuit Track | ==2.4.1（测试版本） |

**结论**: `torch >= 2.4, < 2.6` 是兼容性最优区间（覆盖 Edge Pruning 原版和 MIB）。如果不用 Edge Pruning 原版，`torch >= 2.4` 即可。

### TransformerLens vs NNsight

| 库 | 框架依赖 |
|----|---------|
| EAP-IG | TransformerLens >=2.15.0 |
| Edge Pruning（原版） | TransformerLens ==2.15.0 |
| Edge Pruning（实验版） | HuggingFace transformers（无 TransformerLens） |
| ACDC | TransformerLens（版本由 poetry 管理） |
| Auto-Circuit | TransformerLens >=1.13.0 |
| AtP*（社区版） | NNsight + PyTorch |

**结论**:
- EAP-IG / Edge Pruning（原版） / ACDC / Auto-Circuit 全部基于 **TransformerLens**，共存无问题
- AtP* 社区实现用 **NNsight**，但 NNsight 与 TransformerLens 无直接冲突（不同包，不同 hook 机制），可在同一环境安装
- **推荐**: 统一使用 TransformerLens 生态（EAP-IG + Auto-Circuit），AtP* 如需使用则参考论文自行在 TransformerLens 上实现 QK-Fix + GradDrop

### 潜在冲突

1. **TransformerLens 2.x vs 3.x**: EAP-IG 和 Edge Pruning 要求 `>=2.15.0`，Auto-Circuit 要求 `>=1.13.0`。TransformerLens 3.x 保留了 `HookedTransformer` 兼容层，但可能有 breaking changes。**建议先用 `transformer-lens~=2.15` 保守路线**，待 EAP-IG 更新后再升级。
2. **Edge Pruning 的额外依赖**: 原版 pinned `jax==0.5.2` 和 `tensorflow==2.18.0`（Tracr 实验用），与 torch 同装可能导致 CUDA 冲突。**若只做 GPT-2 实验，可删除 jax/tensorflow 行**。
3. **flash-attn**: Edge Pruning 要求 `flash-attn==2.7.2.post1`，需编译安装且 CUDA 版本敏感。

---

## 9. Recommended requirements.txt

```txt
# Core
python>=3.10
torch==2.5.1  # 兼容 Edge Pruning 原版；CUDA 版本按 GPU 选择
transformer-lens==2.15.0  # EAP-IG + Edge Pruning + Auto-Circuit 共同基线

# EAP-IG (circuit discovery)
eap @ git+https://github.com/hannamw/eap-ig.git
matplotlib>=3.10.1

# Auto-Circuit (ACDC 替代 + 多种方法)
auto-circuit>=0.1.0

# Edge Pruning (clone separately, use its own requirements)
# git clone https://github.com/princeton-nlp/edge-pruning.git

# Common
einops>=0.8.1
datasets>=3.2.0
accelerate>=1.2.1
networkx>=3.4.2
numpy>=2.2.0
scipy>=1.15.0
tqdm>=4.67.0

# Visualization (optional)
graphviz>=0.20.3
# pygraphviz>=1.14  # 需系统 apt install libgraphviz-dev
plotly>=5.18.0

# Flash Attention (optional, 需编译)
# flash-attn==2.7.2.post1

# NNsight (仅 AtP* 社区实现需要)
# nnsight>=0.3
```

---

## 10. 推荐集成策略

对于 StructFuse 项目，推荐以下集成路径：

1. **主力框架**: TransformerLens 2.15.x + EAP-IG 2.0 作为 edge-level attribution 的核心
2. **ACDC**: 通过 Auto-Circuit 库调用（比原始 ACDC 代码更稳定）
3. **Edge Pruning**: 作为独立模块，clone 仓库后用其原版 requirements 运行（避免依赖冲突）
4. **AtP***: 不推荐用社区实现（不成熟 + node-level only）；如需 AtP* 的 QK-Fix，在 EAP-IG 框架内自行实现更可控
5. **CIRCUS Config-Bagging**: 自行实现（<100 行），作为 post-processing 叠加在任意 edge attribution 方法之上
6. **评估**: 直接复用 MIB Circuit Track 框架（`run_attribution.py` + `run_evaluation.py`），获得标准化的 CPR/CMD 指标
