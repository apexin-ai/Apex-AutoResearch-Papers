# audit ref verify worker A

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_ref_verify_worker_A_20260529T062907_result.json`
- **Structured JSON:** [`d3e5ec808e5af99a903d.json`](../../sessions/d3/d3e5ec808e5af99a903d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All verification complete. Let me now compile the full checklist, including citation context checks.

---

## 引用核对清单

### A. 主论文中引用的条目（37条被引用，按出现顺序）

```
[✓] rao2021dynamicvit | Rao, Yongming et al. | "DynamicViT: Efficient Vision Transformers with Dynamic Token Sparsification" | 2021 | NeurIPS 2021
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确
- 正文用法: introduction.tex L14, related_work.tex L5, appendix — ViT token pruning代表工作 ✓

[✓] bolya2023tome | Bolya, Daniel et al. | "Token Merging: Your ViT But Faster" | 2023 | ICLR 2023
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确
- 正文用法: introduction.tex L14, related_work.tex L5, appendix — token merging方法 ✓

[✓] liang2022evit | Liang, Youwei et al. | "Not All Patches are What You Need: Expediting Vision Transformers via Token Reorganizations" | 2022 | ICLR 2022
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确
- 正文用法: introduction.tex L14, related_work.tex L5 — ViT token pruning ✓

[✓] cheng2026vlaiap | Cheng, Jintao et al. | "VLA-IAP: Training-Free Visual Token Pruning..." | 2026 | arXiv 2603.22991
- 验证结果: 真实存在/作者正确/标题正确/年份正确/arXiv ID正确
- 正文用法: introduction.tex L14, related_work.tex L8 — VLA token pruning方法 ✓

[✓] xu2025vlacache | Xu, Siyu et al. | "VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching" | 2025 | NeurIPS 2025
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确
- 正文用法: introduction.tex L14, related_work.tex L8 — VLA token caching ✓

[✓] yang2025efficientvla | Yang, Yantai et al. | "EfficientVLA: Training-Free Acceleration and Compression for VLA Models" | 2025 | arXiv 2506.10100
- 验证结果: 真实存在/作者正确/标题正确/年份正确/arXiv ID正确
- 正文用法: introduction.tex L14, related_work.tex L8, results — CogACT pruning结果来源 ✓

[✓] liu2025vlapruner | Liu, Ziyan et al. | "VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning..." | 2025 | arXiv 2511.16449
- 验证结果: 真实存在/作者正确/标题正确/年份正确/arXiv ID正确
- 正文用法: introduction.tex L14, related_work.tex L8 — VLA token pruning ✓

[✓] black2024pi0 | Black, Kevin et al. | "π0: A Vision-Language-Action Flow Model for General Robot Control" | 2024 | arXiv 2410.24164
- 验证结果: 真实存在/作者正确/标题正确/年份正确/arXiv ID正确
- 正文用法: introduction.tex L16, method.tex, results — linear projection connector ✓

[✓] kim2024openvla | Kim, Moo Jin et al. | "OpenVLA: An Open-Source Vision-Language-Action Model" | 2024 | CoRL 2024
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确
- 正文用法: introduction.tex L16, background, method, results — MLP projector connector ✓

[✓] shukor2025smolvla | Shukor, Mustafa et al. | "SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics" | 2025 | arXiv 2506.01844
- 验证结果: 真实存在/作者正确/标题正确/年份正确/arXiv ID正确
- 正文用法: introduction, background, method, results — pixel-shuffle connector ✓

[✓] zheng2025xvla | Zheng, Jinliang et al. | "X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment VLA Model" | 2026 | ICLR 2026, arXiv 2510.10274
- 验证结果: 真实存在/作者正确/标题正确/年份正确(field=2026)/venue正确/arXiv ID正确
- 正文用法: introduction.tex L16, method, experiments, results — BART encoder connector ✓

[✓] chen2024fastv | Chen, Liang et al. | "An Image is Worth 1/2 Tokens After Layer 2..." | 2024 | ECCV 2024, arXiv 2403.06764
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确/arXiv ID正确
- 正文用法: related_work.tex L8 — VLM token pruning ✓

[✗] shang2024prumerge | Shang, Yuzhang et al. | "LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models" | 2024→2025 | ICCV 2025
- 验证结果: 真实存在/作者正确/标题正确/venue正确
- 问题: **年份错误**。Bib year=2025 正确匹配 ICCV 2025，但 bib key 暗示 2024。实际 booktitle 写的是 "IEEE/CVF International Conference on Computer Vision (ICCV)" year=2025，这是正确的。（复查：bib 文件中 year=2025，OK。bib key 中的 2024 仅是标识符不影响输出。）
- **修正**: 复查后 bib year field = 2025，venue = ICCV 2025，均正确。bib key "2024" 不影响输出。**改判为 ✓**。

[✓] zhang2025sparsevlm | Zhang, Yuan et al. | "SparseVLM: Visual Token Sparsification..." | 2025 | ICML 2025, arXiv 2410.04417
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确/arXiv ID正确
- 正文用法: related_work.tex L8 — VLM token sparsification ✓

[✗] khaki2025sparsevila | Khaki, Samir et al. | "SparseVILA: Decoupled Visual Sparsity..." | 2025 | ICCV 2025, arXiv 2510.17777
- 验证结果: 真实存在/作者正确/年份正确/venue正确/arXiv ID正确
- 问题: **标题错误**。Bib 写 "Decoupled"，实际标题为 "Decoupling"（动名词形式）
- 正文用法: related_work.tex L8 — VLM token sparsification ✓

[✓] ye2025fitprune | Ye, Weihao et al. | "Fit and Prune: Fast and Training-free Visual Token Pruning for Multi-modal LLMs" | 2025 | AAAI 2025, arXiv 2409.10197
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确/arXiv ID正确
- 正文用法: related_work.tex L8 — VLM token pruning ✓

[✓] jiang2026lightvla | Jiang, Titong et al. | "The Better You Learn, The Smarter You Prune..." | 2026 | ICRA 2026, arXiv 2509.12594
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确/arXiv ID正确
- 正文用法: related_work.tex L8 — VLA differentiable token pruning ✓

[✓] gao2025compressorvla | Gao, Juntao et al. | "Compressor-VLA: Instruction-Guided Visual Token Compression..." | 2025 | arXiv 2511.18950
- 验证结果: 真实存在/作者正确/标题正确/年份正确/arXiv ID正确
- 正文用法: related_work.tex L8 — VLA token compression ✓

[✓] wang2025specprunevla | Wang, Hanzhen et al. | "SpecPrune-VLA: Accelerating VLA Models via Action-Aware Self-Speculative Pruning" | 2025 | arXiv 2509.05614
- 验证结果: 真实存在/作者正确/标题正确/年份正确/arXiv ID正确
- 正文用法: related_work.tex L8 — VLA pruning ✓

[✓] feng2026seewhatmatters | Feng, Yixu et al. | "See What Matters: Differentiable Grid Sample Pruning..." | 2026 | ICML 2026, arXiv 2605.11817
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确/arXiv ID正确
- 正文用法: related_work.tex L8 — VLA token pruning ✓

[✓] jabbour2025dontrun | Jabbour, Jason et al. | "Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered" | 2025 | arXiv 2510.08464
- 验证结果: 真实存在/作者正确/标题正确/年份正确/arXiv ID正确
- 正文用法: related_work.tex L11 — concurrent work on VLA pruning failure ✓

[✓] liu2023llava | Liu, Haotian et al. | "Visual Instruction Tuning" | 2023 | NeurIPS 2023
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确
- 正文用法: related_work.tex L14 — LLaVA MLP projector ✓

[✓] li2023blip2 | Li, Junnan et al. | "BLIP-2: Bootstrapping Language-Image Pre-Training..." | 2023 | ICML 2023
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确
- 正文用法: related_work.tex L14 — cross-attention queries ✓

[✓] shi2016subpixel | Shi, Wenzhe et al. | "Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel CNN" | 2016 | CVPR 2016
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确
- 正文用法: related_work.tex L14 — pixel shuffle origin ✓

[✓] zhai2023siglip | Zhai, Xiaohua et al. | "Sigmoid Loss for Language Image Pre-Training" | 2023 | ICCV 2023
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确
- 正文用法: background.tex — SmolVLA vision encoder ✓

[✓] yang2024qwen2 | Yang, An et al. | "Qwen2 Technical Report" | 2024 | arXiv 2407.10671
- 验证结果: 真实存在/作者正确/标题正确/年份正确/arXiv ID正确
- 正文用法: background.tex — Qwen2-0.5B LLM backbone ✓

[✓] lipman2023flow | Lipman, Yaron et al. | "Flow Matching for Generative Modeling" | 2023 | ICLR 2023
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确
- 正文用法: background.tex — flow matching action head ✓

[✓] oquab2023dinov2 | Oquab, Maxime et al. | "DINOv2: Learning Robust Visual Features without Supervision" | 2024 | TMLR
- 验证结果: 真实存在/作者正确/标题正确/year field=2024正确(TMLR 2024)/venue正确
- 问题（次要）: bib key 含 "2023" 但 year field = 2024。arXiv 发布于 2023.04，TMLR 发表于 2024.01。Key 不影响输出。
- 正文用法: background.tex — OpenVLA dual encoder ✓

[✓] black2025pi05 | Black, Kevin et al. | "π0.5: a Vision-Language-Action Model with Open-World Generalization" | 2025 | CoRL 2025, PMLR v305, pp.17-40, arXiv 2504.16054
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确/volume正确/pages正确/arXiv ID正确
- 正文用法: method.tex, experiments.tex, results — linear connector model ✓

[✓] kim2025openoft | Kim, Moo Jin et al. | "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success" | 2025 | arXiv 2502.19645
- 验证结果: 真实存在/作者正确/标题正确/年份正确/arXiv ID正确
- 正文用法: method.tex, results — OFT variant of OpenVLA ✓

[✓] lewis2020bart | Lewis, Mike et al. | "BART: Denoising Sequence-to-Sequence Pre-training..." | 2020 | ACL 2020
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确
- 正文用法: method.tex — X-VLA uses BART encoder ✓

[✓] liu2023libero | Liu, Bo et al. | "LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning" | 2023 | NeurIPS 2023
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确
- 正文用法: background, method, experiments, results — evaluation benchmark ✓

[✓] li2024cogact | Li, Qixiu et al. | "CogACT: A Foundational Vision-Language-Action Model..." | 2024 | arXiv 2411.19650
- 验证结果: 真实存在/作者正确/标题正确/年份正确/arXiv ID正确
- 正文用法: results — MLP projector corroboration from EfficientVLA ✓

[✓] shi2024crossget | Shi, Dachuan et al. | "CrossGET: Cross-Guided Ensemble of Tokens..." | 2024 | ICML 2024, arXiv 2305.17455
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确/arXiv ID正确
- 正文用法: related_work.tex L5 — ViT token pruning ✓

[✓] yin2022avit | Yin, Hongxu et al. | "A-ViT: Adaptive Tokens for Efficient Vision Transformer" | 2022 | CVPR 2022, arXiv 2112.07658
- 验证结果: 真实存在/作者正确/年份正确/venue正确/arXiv ID正确
- 问题（次要）: arXiv 标题为 "AdaViT"，CVPR 发表版改名 "A-ViT"。Bib 使用 CVPR 标题，正确。
- 正文用法: related_work.tex L5 — ViT adaptive tokens ✓

[✓] abnar2020quantifying | Abnar, Samira & Zuidema, Willem | "Quantifying Attention Flow in Transformers" | 2020 | ACL 2020, pp.4190-4197
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确/pages正确
- 正文用法: appendix — attention rollout method ✓

[✓] su2024roformer | Su, Jianlin et al. | "RoFormer: Enhanced Transformer with Rotary Position Embedding" | 2024 | Neurocomputing v568 p127063
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确/volume正确
- 正文用法: appendix — RoPE position encoding ✓
```

---

### B. 问题条目汇总

| # | 状态 | cite_key | 问题 | 严重度 |
|---|------|----------|------|--------|
| 1 | **✗** | `khaki2025sparsevila` | 标题 "Decoupled" 应为 "**Decoupling**" | **需修复** |

其余 36 条引用条目均验证通过。

---

### C. 未被主论文引用的 bib 条目（25条）

以下条目存在于 `references.bib` 但未在 main.tex 编译链中被 `\cite` 引用（可能来自早期草稿）：

| cite_key | 备注 |
|----------|------|
| `li2024roboflamingo` | 未引用 |
| `brohan2023rt2` | 未引用；与 `zitkovich2023rt2` 重复（同一论文，arXiv vs proceedings 作者顺序不同） |
| `brohan2023rt1` | 未引用 |
| `ghosh2024octo` | 未引用 |
| `alayrac2022flamingo` | 未引用 |
| `chen2024internvl` | 未引用 |
| `jaegle2021perceiver` | 未引用 |
| `li2024tokenpacker` | 未引用 |
| `wen2024tinyvla` | 未引用 |
| `ryoo2021tokenlearner` | 未引用 |
| `meng2022adavit` | 未引用 |
| `chen2023sparsevit` | 未引用 |
| `zhang2024fastervlm` | 未引用 |
| `liu2024llava15` | 未引用 |
| `chen2024internvl25` | 未引用 |
| `gao2024miniinternvl` | 未引用 |
| `zitkovich2023rt2` | 未引用；与 `brohan2023rt2` 重复 |
| `openxembodiment2024` | 未引用 |
| `zhang2023h2o` | 未引用 |
| `xiao2024streamingllm` | 未引用 |
| `mees2022calvin` | 未引用 |
| `chi2023diffusionpolicy` | 未引用 |
| `zeng2023transformers_tsf` | 未引用（仅在 sections/ 草稿中出现） |
| `bouthillier2024negative` | 未引用；**且作者错误**（实际第一作者为 Florian Karl，非 Xavier Bouthillier） |
| `oquab2024dinov2` | 未引用；与 `oquab2023dinov2` 重复 |

---

### D. 总结

**需修复（1条）：**
- `khaki2025sparsevila`：标题 "Decoupled" → "**Decoupling**"

**建议清理（不影响编译输出，但建议处理）：**
- 25 条未引用条目可从 bib 中移除以保持整洁
- `oquab2023dinov2` 和 `oquab2024dinov2` 是同一论文的重复条目
- `brohan2023rt2` 和 `zitkovich2023rt2` 是同一论文的重复条目（arXiv vs proceedings 作者顺序不同）
- `bouthillier2024negative` 的作者字段有误（但未被引用，不影响论文）

**全部 37 条被引用条目中**：36 条完全正确，1 条有标题拼写错误。所有引用在正文中的使用语境均准确，无张冠李戴的情况。

---
