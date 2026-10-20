# KV Cache Eviction Baselines Survey

Date: 2026-05-12

## Summary

| Method | Code | HF Compat | Difficulty | Venue |
|--------|------|-----------|------------|-------|
| **H2O** | ✅ Official repo + kvpress + HF PR | Excellent | Easy | NeurIPS 2023 |
| **R-KV** | ✅ Official repo | Good | Medium | NeurIPS 2025 |
| **SkipKV** | ❌ No code | N/A | Hard | arXiv preprint |
| **FASA** | ⚠️ Announced, not released | Unknown | Hard | ICLR 2026 |
| **KeyDiff** | ✅ Via NVIDIA/kvpress | Excellent | Easy | arXiv 2025 |

**推荐 baseline**: H2O (#1) + KeyDiff (#2)

---

## 1. H2O (Heavy Hitter Oracle)

- **Paper**: NeurIPS 2023, arXiv:2306.14048
- **GitHub**: https://github.com/FMInference/H2O
- **代码可用性**: 直接可用。`h2o_hf/` 包含 simulation 和 real KV drop 实现，基于 HF transformers。NVIDIA/kvpress 也包含 H2O 实现。HF transformers PR #35381 提议内置 `H2OCache`。
- **HF 兼容性**: 原生/近原生。三条集成路径：官方 repo、kvpress、HF 内置。
- **集成难度**: **Easy**。最成熟的 baseline，多种集成方式可选。
- **方法概要**: 维护 attention score 累积统计，保留 heavy hitter tokens（高 attention 分数）+ recent tokens，evict 其余。

## 2. R-KV (Redundancy-aware KV Cache Compression)

- **Paper**: NeurIPS 2025, arXiv:2505.24133
- **GitHub**: https://github.com/Zefan-Cai/R-KV
- **代码可用性**: 直接可用。同作者维护 [KVCache-Factory](https://github.com/Zefan-Cai/KVCache-Factory) 统一框架，支持 PyramidKV、SnapKV、H2O、StreamingLLM。
- **HF 兼容性**: 好。基于 HF transformers 构建，支持 FlashAttention v2 和 SDPA。
- **集成难度**: **Medium**。Attention-score scoring + cosine similarity 去重需 hook 进 decoding loop。双缓冲设计需适配。
- **方法概要**: O(B²) pairwise similarity eviction，先按 attention score 选候选，再用 cosine similarity 去重。专门针对推理模型长 CoT。

## 3. SkipKV

- **Paper**: arXiv:2512.07993 (Dec 2025)
- **GitHub**: 无公开仓库
- **代码可用性**: **需要重新实现**。多次搜索未找到公开代码。相关但不同的项目 [SentenceKV](https://github.com/zzbright1998/SentenceKV) 采用不同方法。
- **HF 兼容性**: N/A
- **集成难度**: **Hard**。需实现 sentence-primary scoring 和 adaptive steering 两个新组件，sentence boundary detection 在 CoT 推理中增加复杂度。
- **方法概要**: 句级别 KV skipping，adaptive steering of hidden states。

## 4. FASA (Frequency-Aware Sparse Attention)

- **Paper**: ICLR 2026, arXiv:2602.03152
- **GitHub**: 论文中标注 https://github.com/AMAP-ML/FASA-ICLR2026 ，但该 repo 当前不可见（可能未公开或延迟发布）。
- **代码可用性**: **可能需要重新实现**（或等待发布）。AMAP-ML org 已发布其他 ICLR 2026 论文代码，但 FASA 尚未可见。
- **HF 兼容性**: 未知。需要自定义 attention kernel。
- **集成难度**: **Hard**。需要 (1) offline RoPE dominant frequency calibration, (2) custom Token Importance Predictor, (3) focused attention computation stage。
- **方法概要**: 两阶段框架——离线 FC calibration + focused attention。

## 5. KeyDiff

- **Paper**: arXiv:2504.15364 (Apr 2025, updated Jan 2026)
- **GitHub**: 无独立 repo，但已实现于 [NVIDIA/kvpress](https://github.com/NVIDIA/kvpress) 的 `KeyDiffPress`
- **代码可用性**: **直接可用**。kvpress 是成熟的 HF transformers KV 压缩库，KeyDiffPress 是内置 press 之一。
- **HF 兼容性**: **Excellent**。完全基于 HF transformers，通过 `KVPressTextGenerationPipeline` 使用。
- **集成难度**: **Easy**。安装 kvpress，选择 KeyDiffPress，设置压缩比即可。Attention-score-free，兼容 FlashAttention。
- **方法概要**: 计算 keys 与 anchor（keys 均值）的 cosine similarity，evict 最相似的（最冗余的）。与 CARC 的 EMA anchor 思路高度相关。

---

## 推荐 Top 2

### 1. H2O — 经典 attention-based baseline
- 最成熟，文献中的标准 baseline
- 三条集成路径，最快 1 小时集成完成
- 代表 "attention score eviction" 范式，与 CARC 的 EMA-based eviction 形成对比

### 2. KeyDiff — anchor-based eviction (与 CARC 最相关)
- Via NVIDIA/kvpress 即插即用
- 方法论与 CARC 最接近（都用 key 相似度做 eviction），是最好的 ablation 对照
- Attention-score-free，FlashAttention 兼容

### 备选: R-KV
- 如果需要针对推理模型的 baseline，R-KV 是最佳选择
- 集成工作量中等（~2-3 天）

---

## 参考资源

- [FMInference/H2O](https://github.com/FMInference/H2O)
- [NVIDIA/kvpress](https://github.com/NVIDIA/kvpress) (含 H2O + KeyDiff)
- [Zefan-Cai/R-KV](https://github.com/Zefan-Cai/R-KV)
- [Zefan-Cai/KVCache-Factory](https://github.com/Zefan-Cai/KVCache-Factory)
- [HF Transformers H2O PR #35381](https://github.com/huggingface/transformers/pull/35381)
- [HF KV Cache docs](https://huggingface.co/docs/transformers/main/en/kv_cache)
