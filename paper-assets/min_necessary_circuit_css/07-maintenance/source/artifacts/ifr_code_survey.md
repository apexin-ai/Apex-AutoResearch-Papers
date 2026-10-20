# IFR (Information Flow Routes) 代码调研报告

## 1. 原论文信息

**论文**: "Information Flow Routes: Automatically Interpreting Language Models at Scale"
**作者**: Javier Ferrando, Elena Voita
**会议**: EMNLP 2024 (Main Conference)
**arXiv**: [2403.00824](https://arxiv.org/abs/2403.00824)
**ACL Anthology**: [2024.emnlp-main.965](https://aclanthology.org/2024.emnlp-main.965/)

## 2. 参考代码仓库

| 仓库 | 链接 | Stars | 状态 | 说明 |
|------|------|-------|------|------|
| LLM Transparency Tool | [facebookresearch/llm-transparency-tool](https://github.com/facebookresearch/llm-transparency-tool) | 1.3k | Archived (2026-02-01) | 原作者官方实现，含 IFR + 可视化 UI |
| EACL 2024 Tutorial | [interpretingdl/eacl2024_transformer_interpretability_tutorial](https://github.com/interpretingdl/eacl2024_transformer_interpretability_tutorial) | — | Active | Ferrando 的教程代码，含 ALTI 基础实现 |

**注意**: LLM Transparency Tool 已归档，但核心算法部分代码可参考。它基于 TransformerLens，使用 conda 环境，许可证为 CC BY-NC 4.0。

## 3. 核心算法

### 3.1 原理

IFR 基于 ALTI (Aggregation of Layer-Wise Token-to-Token Interactions) 框架，通过单次前向传播 + 激活缓存计算边重要性。核心思想：测量源组件输出向量与目标组件输入残差流之间的"接近度"。

### 3.2 数学公式

```
score(u → v) = proximity(y_u, x_v) = max(||x_v||₁ - ||y_u - x_v||₁, 0)
```

其中:
- `y_u` = 源组件 u 的输出激活 (attention head output 或 MLP output)
- `x_v` = 目标组件 v 的残差流输入 (resid_pre 或 resid_mid)
- 直觉: 如果 y_u 与 x_v "接近"（L1 距离小），则 u 对 v 的贡献大

### 3.3 算法伪代码

```
IFR(model, tokens):
  1. 单次前向传播，缓存所有层的:
     - resid_pre[L]  (注意力前的残差流)
     - resid_mid[L]  (MLP 前的残差流 = resid_pre[L] + attn_out[L])
     - head_out[L][H] (每个注意力头的 O_proj 后输出)
     - mlp_out[L]     (MLP 输出)
  
  2. 构建源激活表:
     src_act["input"] = resid_pre[0]
     src_act["a{L}.h{H}"] = head_out[L][H]
     src_act["m{L}"] = mlp_out[L]
  
  3. 对每个目标层 L_dst:
     a) 注意力边: 对满足 src_layer < L_dst 的每个源:
        score = proximity(src_act[src], resid_pre[L_dst])
        → 写入 "src -> a{L_dst}.h{H}.{q/k/v}" (同层所有头共享 score)
     
     b) MLP 边: 对满足 before_mlp(src, L_dst) 的每个源:
        score = proximity(src_act[src], resid_mid[L_dst])
        → 写入 "src -> m{L_dst}"
  
  4. 返回 Dict[edge_name → score]
```

### 3.4 方法特性

| 维度 | IFR | EAP-IG | Edge Pruning (L0) | ACDC |
|------|-----|--------|-------------------|------|
| 类型 | 归因 (Attribution) | 梯度 (Gradient) | 优化 (Optimization) | 因果 (Causal) |
| 前向传播 | 1 次 | 2 次 + 1 反向 | N epochs × 1 次 | O(E) 次 |
| 反向传播 | 0 | 1 次 (+ IG steps) | N epochs | 0 |
| 需要 metric | 否 | 是 | 是 | 是 |
| 大模型可行性 | ✓ 极佳 | ✓ 较好 | ✓ 但慢 | ✗ 不可行 |
| 忠实度 | 中 (非因果) | 中 (一阶近似) | 高 (直接优化) | 高 (精确因果) |

## 4. 现有实现状况

### 4.1 服务器代码 (TransformerLens 版本)

**文件**: `/root/min_necessary_circuit_css/ifr_discovery.py`
- 基于 TransformerLens `HookedTransformer.run_with_cache()`
- 函数签名: `run_ifr(model, dataset, metric=None) -> Dict[str, float]`
- 边命名: TransformerLens 格式 (`blocks.{L}.attn.hook_result[{H}] -> blocks.{L'}.attn.hook_q[{H'}]`)
- 仅支持 TransformerLens 模型 (GPT-2)

### 4.2 本地 Artifact (HuggingFace 版本)

**文件**: `artifacts/ifr_scoring.py`
- 基于 HuggingFace `register_forward_hook` 手动缓存
- 函数签名: `compute_ifr_edges(model, dataset, metric_fn, threshold=0.1, device="cuda") -> Dict[str, float]`
- 边命名: 规范格式 (`a{L}.h{H} -> a{L'}.h{H'}.q`)
- 支持: Llama, Qwen2, Gemma2, Mistral, Phi3, GPT2
- 含 `_decompose_per_head()` 通过 o_proj/c_proj 分解每头输出

### 4.3 集成状态

| 组件 | IFR 集成状态 | 需要改动 |
|------|-------------|---------|
| `ifr_discovery.py` (TL版) | ✓ 完成 | — |
| `artifacts/ifr_scoring.py` (HF版) | ✓ 完成 | 需部署到服务器 |
| `circuit_discovery.py` 边名规范化 | ✗ 缺 IFR normalizer | 添加 `_normalize_ifr_edge()` 和 `_NORMALIZERS["ifr"]` |
| `css.py` 二值化策略 | ✗ 缺 IFR 分支 | 添加 `"ifr"` 到 `binarize_scores()` |
| `config.py` Phase 2 配置 | ✗ methods 仍为 ACDC | 新建 Phase2Config 或参数化 |
| `run_mvp.py` 主流程 | ✗ 无 IFR 路径 | `run_phase2_experiment.py` 已在 artifacts 中 |
| `phase2_configs.yaml` 实验矩阵 | ✓ 完成 | 已规划全部 16 个实验 |

## 5. Phase 2 集成方案

### 5.1 文件改动清单

**新增** (从 artifacts 部署到服务器):
- `ifr_scoring.py` → `/root/min_necessary_circuit_css/ifr_scoring.py`
- `run_phase2_experiment.py` → `/root/min_necessary_circuit_css/run_phase2.py`
- `phase2_configs.yaml` → `/root/min_necessary_circuit_css/phase2_configs.yaml`

**修改**:
1. `circuit_discovery.py`:
   - 添加 IFR edge name normalizer (IFR HF版已用规范格式，可能只需 identity 映射)
   - 添加 `run_ifr()` wrapper 调用 `compute_ifr_edges()`

2. `css.py` → `binarize_scores()`:
   ```python
   elif method == "ifr":
       # IFR: rank by unique score values, take top-N unique score groups
       unique_scores = sorted(set(edge_scores.values()), reverse=True)
       cutoff = unique_scores[min(n, len(unique_scores)) - 1] if unique_scores else 0
       return {e for e, s in edge_scores.items() if s >= cutoff}
   ```

3. `config.py`: 添加 `Phase2Config` dataclass，或用 YAML 驱动

### 5.2 IFR 边名格式对齐

| 格式 | 示例 | 使用者 |
|------|------|--------|
| TransformerLens | `blocks.0.attn.hook_result[3] -> blocks.1.attn.hook_q[5]` | `ifr_discovery.py` |
| 规范 (Canonical) | `a0.h3 -> a1.h5.q` | `ifr_scoring.py`, CSS, CIRCUS |
| EAP 格式 | `<resid_start> -> A0.0<Q>` | `eap` 库 |
| auto_circuit 格式 | `A0.0 -> MLP 1` | `auto_circuit` 库 |

HF 版 `ifr_scoring.py` 已直接输出规范格式，**无需额外 normalizer**。服务器版 `ifr_discovery.py` 使用 TransformerLens 格式，需要经过 `_normalize_eap_edge()` 或新建 normalizer 转换。

Phase 2 使用 HF 版，边名已对齐，集成零成本。

## 6. 依赖

### 已安装 (cqa1-21977)

```
torch==2.10.0+cu128
transformers==4.57.6
transformer-lens==2.15.0
auto-circuit==1.0.1
eap==2.0.0
einops==0.8.2
accelerate==1.13.0
```

### IFR 额外依赖

**无**。`ifr_scoring.py` 仅依赖 `torch` + `transformers`，已安装。

## 7. 计算成本估算

基于 6× RTX 4090D (24GB each)，单 GPU，50 samples，seq_len ~30 tokens。

| 模型 | 参数量 | 显存 (fp16) | IFR | EAP-IG (5 steps) | EP (100 epochs) | 三方法总计 |
|------|--------|------------|-----|-------------------|------------------|-----------|
| GPT-2 Small | 124M | ~1 GB | ~5s | ~2min | ~5min | ~8min |
| Qwen-2.5 0.5B | 494M | ~2 GB | ~3min | ~5min | ~15min | ~25min |
| Gemma-2 2B | 2.6B | ~6 GB | ~8min | ~15min | ~40min | ~65min |
| Llama-3.1 8B | 8B | ~16 GB | ~15min | ~40min | ~90min | ~150min |

**瓶颈**: Edge Pruning 的多 epoch 优化。IFR 始终是三方法中最快的。

**显存风险**: Llama-3.1 8B fp16 ~16GB + activation cache + EP 梯度 → 单卡 24GB 可能紧张，需要:
- 减少 `num_samples` (已在 configs 中设为 20)
- EP 使用 gradient checkpointing
- 或使用 fp8 / int8 量化推理

## 8. 风险点

### 8.1 IFR 非因果性

IFR 是归因方法，不进行因果干预（ablation/patching）。CSS 的价值在于跨不同方法论的共识——IFR 提供了与 EAP-IG (梯度) 和 EP (优化) 互补的第三视角。但需要在论文中明确 discuss 这一设计选择。

**缓解**: 在 Related Work 中引用 Ferrando & Voita 的对比实验，证明 IFR 在 IOI/Greater-Than 电路上与 ACDC 结果高度一致。

### 8.2 同层注意力头共享 score

IFR 当前实现中，同一源对同一目标层的所有注意力头（Q/K/V）共享一个 proximity score（因为它们共享同一 resid_pre）。这与 EAP-IG（每头独立 score）和 EP（每头独立 mask）粒度不一致。

**影响**: IFR 二值化后的电路中，同一层的头倾向于同时出入选。可能导致 CSS overlap 偏高。

**缓解**: `ifr_scoring.py` 中的 `_decompose_per_head()` 已提供了每头分解——可以在 resid_mid 层面对每个头分别计算 proximity，但需要额外验证这种扩展的数学合理性。

### 8.3 Gemma-2 残差流近似

Gemma-2 在注意力输出上有额外的 LayerNorm (post-attention LN)，`resid_mid = resid_pre + LN(attn_out)` 而非简单相加。当前 HF 版 `ifr_scoring.py` 直接用 `resid_pre + attn_out` 作为 resid_mid，对 Gemma-2 是近似。

**影响**: Gemma-2 的 IFR scores 可能略有偏差，但方向性正确。

### 8.4 TransformerLens 大模型支持

TransformerLens 对 Qwen-2.5/Gemma-2/Llama-3.1 的支持有限或需要较新版本。Phase 2 使用 HF 版 `ifr_scoring.py` 规避此问题。

### 8.5 替代方案

如果 IFR 效果不佳，备选方案:
1. **HAP (Hybrid Attribution + Pruning)** — EAP 粗筛 + EP 精修，平衡速度和忠实度 ([arXiv 2510.03282](https://arxiv.org/abs/2510.03282))
2. **CD-T (Contextual Decomposition for Transformers)** — 将运行时从小时降到秒 ([ICLR 2025](https://arxiv.org/abs/2407.00886))
3. **直接用 EAP (不加 IG)** — 最快但忠实度低，可作为 fallback

## 9. 行动项 (Phase 2 准备)

- [ ] 将 `artifacts/ifr_scoring.py` 部署到 `/root/min_necessary_circuit_css/`
- [ ] 将 `artifacts/run_phase2_experiment.py` 部署到 `/root/min_necessary_circuit_css/`
- [ ] 将 `artifacts/phase2_configs.yaml` 部署到 `/root/min_necessary_circuit_css/`
- [ ] 在 `circuit_discovery.py` 中添加 IFR normalizer（如果用 TL 版）
- [ ] 在 `css.py` 中添加 IFR 二值化策略
- [ ] 下载目标模型到 `/root/autodl-tmp/.hf_cache/`:
  - Qwen/Qwen2.5-0.5B (~1GB)
  - google/gemma-2-2b (~5GB)
  - meta-llama/Llama-3.1-8B (~16GB)
- [ ] 验证 IFR 在 GPT-2 IOI 上的 edge scores 与现有三方法的 CSS 兼容性
- [ ] 8B 模型 EP 显存测试 (可能需要 gradient checkpointing)
