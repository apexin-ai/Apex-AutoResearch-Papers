# audit ref verify worker B

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_ref_verify_worker_B_20260529T062918_result.json`
- **Structured JSON:** [`c5a06e99a005681d2ef7.json`](../../sessions/c5/c5a06e99a005681d2ef7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 4 batches complete. Now compiling the full verification report.

---

# 引用核对清单 — 完整报告

## 一、已引用条目 (37 entries cited in main paper)

```
[✓] abnar2020quantifying | Abnar, Zuidema | "Quantifying Attention Flow in Transformers" | 2020 | ACL 2020
- 验证: 真实存在 ✓ | 作者正确 ✓ | 标题正确 ✓ | 年份正确 ✓ | venue正确 ✓
- 正文用法: appendix.tex — attention rollout方法引用，用法准确 ✓
```

```
[✓] gao2025compressorvla | Gao et al. | "Compressor-VLA: Instruction-Guided Visual Token Compression..." | 2025 | arXiv 2511.18950
- 验证: 真实存在 ✓ | 作者正确 ✓ | 标题正确 ✓ | 年份正确 ✓ | arXiv ID正确 ✓
- 正文用法: related_work.tex — 列为VLA token compression concurrent work ✓
```

```
[✗] wang2025specprunevla | Wang et al. | "SpecPrune-VLA: Accelerating VLA Models via Action-Aware Self-Speculative Pruning" | 2025 | arXiv 2509.05614
- 验证: 真实存在 ✓ | 作者正确 ✓ | 标题正确 ✓ | arXiv ID正确 ✓
- 问题: 已被 ICML 2026 接收，bib 仍标记为 arXiv preprint，year=2025 应更新为 2026，venue 应改为 ICML 2026
- 正文用法: related_work.tex — 列为VLA-specific方法 ✓
```

```
[✓] jiang2026lightvla | Jiang et al. | "The Better You Learn, The Smarter You Prune..." | 2026 | ICRA 2026, arXiv 2509.12594
- 验证: 真实存在 ✓ | 作者正确 ✓ | 标题正确 ✓ | 年份正确 ✓ | venue正确 ✓ | arXiv ID正确 ✓
- 正文用法: related_work.tex — 列为VLA token pruning方法 ✓
```

```
[✓] feng2026seewhatmatters | Feng et al. | "See What Matters: Differentiable Grid Sample Pruning..." | 2026 | ICML 2026, arXiv 2605.11817
- 验证: 真实存在 ✓ | 作者正确 ✓ | 标题正确 ✓ | 年份正确 ✓ | venue正确 ✓ | arXiv ID正确 ✓
- 正文用法: related_work.tex — 列为VLA-specific方法 ✓
```

```
[✓] zhang2025sparsevlm | Zhang et al. | "SparseVLM: Visual Token Sparsification..." | 2025 | ICML 2025, arXiv 2410.04417
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: related_work.tex — VLM token efficiency方法 ✓
```

```
[✓] khaki2025sparsevila | Khaki et al. | "SparseVILA: Decoupled Visual Sparsity..." | 2025 | ICCV 2025, arXiv 2510.17777
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: related_work.tex — VLM token efficiency方法 ✓
```

```
[✓] jabbour2025dontrun | Jabbour et al. | "Don't Run with Scissors: Pruning Breaks VLA Models..." | 2025 | arXiv 2510.08464
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: related_work.tex — concurrent work, "independently observe that pruning breaks VLA policies" ✓
```

```
[✓] shukor2025smolvla | Shukor et al. | "SmolVLA: A Vision-Language-Action Model..." | 2025 | arXiv 2506.01844
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: 全文多处 — 作为主要评估模型之一 ✓
```

```
[✓] kim2024openvla | Kim et al. | "OpenVLA: An Open-Source Vision-Language-Action Model" | 2024 | CoRL 2024
- 验证: 真实存在 ✓ | 全部正确 ✓ (PMLR vol. 270)
- 正文用法: 全文多处 — 作为主要评估模型之一 ✓
```

```
[✗] black2024pi0 | Black et al. | "π₀: A Vision-Language-Action Flow Model for General Robot Control" | 2024 | arXiv 2410.24164
- 验证: 真实存在 ✓ | 作者正确 ✓ | 标题正确 ✓ | arXiv ID正确 ✓
- 问题: 已被 RSS 2025 接收。bib 仍为 arXiv preprint, year=2024。应更新 venue 为 RSS 2025, year 为 2025
- 正文用法: method.tex — "Linear projection (π₀)" ✓; introduction.tex — VLA model示例 ✓
```

```
[✓] black2025pi05 | Black et al. | "π₀.₅: a Vision-Language-Action Model with Open-World Generalization" | 2025 | CoRL 2025, PMLR vol 305, arXiv 2504.16054
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: 全文多处 — 作为主要评估模型之一 ✓
```

```
[✓] chen2024fastv | Chen et al. | "An Image is Worth 1/2 Tokens After Layer 2..." | 2024 | ECCV 2024 (Oral), arXiv 2403.06764
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: related_work.tex — VLM token efficiency方法 ✓
```

```
[✓] xu2025vlacache | Xu et al. | "VLA-Cache: Efficient VLA Manipulation via Adaptive Token Caching" | 2025 | NeurIPS 2025
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: related_work.tex, introduction.tex — VLA token efficiency ✓
```

```
[✓] cheng2026vlaiap | Cheng et al. | "VLA-IAP: Training-Free Visual Token Pruning..." | 2026 | arXiv 2603.22991
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: introduction.tex, related_work.tex — VLA token pruning方法 ✓
```

```
[✓] rao2021dynamicvit | Rao et al. | "DynamicViT: Efficient Vision Transformers with Dynamic Token Sparsification" | 2021 | NeurIPS 2021
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: introduction.tex, related_work.tex — ViT token pruning开创性工作 ✓
```

```
[✓] bolya2023tome | Bolya et al. | "Token Merging: Your ViT But Faster" | 2023 | ICLR 2023
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: introduction.tex, related_work.tex, appendix.tex — token merging基线方法 ✓
```

```
[✓] liang2022evit | Liang et al. | "Not All Patches are What You Need..." | 2022 | ICLR 2022
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: introduction.tex, related_work.tex — ViT token reorganization ✓
```

```
[✓] liu2023libero | Liu et al. | "LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning" | 2023 | NeurIPS 2023
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: 全文多处 — 评估benchmark ✓
```

```
[✓] yang2025efficientvla | Yang et al. | "EfficientVLA: Training-Free Acceleration and Compression..." | 2025 | arXiv 2506.10100
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: related_work.tex, results — CogACT的literature corroboration来源 ✓
```

```
[✓] liu2025vlapruner | Liu et al. | "VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning..." | 2025 | arXiv 2511.16449
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: related_work.tex — VLA-specific pruning方法 ✓
```

```
[✗] shang2024prumerge | Shang et al. | "LLaVA-PruMerge: Adaptive Token Reduction..." | bib year=2025 | ICCV 2025
- 验证: 真实存在 ✓ | 作者正确 ✓ | 标题正确 ✓ | venue正确 (ICCV 2025) ✓
- 问题: (1) bib key 写 "2024" 但 year={2025}，key-year 不一致; (2) 缺少 arXiv ID 2403.15388
- 正文用法: related_work.tex — VLM token reduction方法 ✓
```

```
[✓] liu2023llava | Liu et al. | "Visual Instruction Tuning" | 2023 | NeurIPS 2023
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: related_work.tex — "LLaVA projects patches independently through an MLP" ✓
```

```
[✓] shi2016subpixel | Shi et al. | "Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel CNN" | 2016 | CVPR 2016
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: related_work.tex — "pixel shuffle folds spatial neighborhoods into channels" ✓
```

```
[✓] li2023blip2 | Li et al. | "BLIP-2: Bootstrapping Language-Image Pre-Training..." | 2023 | ICML 2023
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: related_work.tex — "uses cross-attention queries" ✓
```

```
[✗] oquab2023dinov2 | Oquab et al. | "DINOv2: Learning Robust Visual Features without Supervision" | year=2024 | TMLR
- 验证: 真实存在 ✓ | 作者正确 ✓ | 标题正确 ✓ | venue正确 (TMLR 2024) ✓
- 问题: (1) bib key 写 "2023" 但 year={2024}，key-year 不一致; (2) 与 oquab2024dinov2 重复（同一篇论文）
- 正文用法: background.tex — OpenVLA vision encoder ✓
```

```
[✓] zhai2023siglip | Zhai et al. | "Sigmoid Loss for Language Image Pre-Training" | 2023 | ICCV 2023
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: background.tex — SmolVLA vision encoder ✓
```

```
[✓] yang2024qwen2 | Yang et al. | "Qwen2 Technical Report" | 2024 | arXiv 2407.10671
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: background.tex — "Qwen2-0.5B language model" ✓
```

```
[✓] lipman2023flow | Lipman et al. | "Flow Matching for Generative Modeling" | 2023 | ICLR 2023
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: background.tex — "conditional flow matching" action head ✓
```

```
[✓] li2024cogact | Li et al. | "CogACT: A Foundational Vision-Language-Action Model..." | 2024 | arXiv 2411.19650
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: results — "CogACT (MLP projector) retains 74.2% SR under 78% pruning" (来自EfficientVLA) ✓
```

```
[✓] kim2025openoft | Kim et al. | "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success" | 2025 | arXiv 2502.19645
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: method.tex, results — OFT as OpenVLA fine-tuning variant for CV calibration ✓
```

```
[✗] zheng2025xvla | Zheng et al. | "X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment VLA Model" | 2026 | ICLR 2026, arXiv 2510.10274
- 验证: 真实存在 ✓ | 作者正确 ✓ | 标题正确 ✓ | venue正确 (ICLR 2026) ✓ | arXiv ID正确 ✓
- 问题: bib key 写 "2025" 但 bib year={2026}，key-year 不一致（minor，不影响编译）
- 正文用法: 全文多处 — "learned encoders with cross-token self-attention", BART encoder ✓
```

```
[✓] lewis2020bart | Lewis et al. | "BART: Denoising Sequence-to-Sequence Pre-training..." | 2020 | ACL 2020
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: method.tex — "X-VLA uses a 12-layer BART encoder" ✓
```

```
[✓] su2024roformer | Su et al. | "RoFormer: Enhanced Transformer with Rotary Position Embedding" | 2024 | Neurocomputing vol 568
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: appendix.tex — RoPE position encoding reference ✓
```

```
[✓] ye2025fitprune | Ye et al. | "Fit and Prune: Fast and Training-free Visual Token Pruning..." | 2025 | AAAI 2025, arXiv 2409.10197
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: related_work.tex — VLM token efficiency ✓
```

```
[✓] shi2024crossget | Shi et al. | "CrossGET: Cross-Guided Ensemble of Tokens..." | 2024 | ICML 2024, arXiv 2305.17455
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: related_work.tex — ViT token pruning方法 ✓
```

```
[✓] yin2022avit | Yin et al. | "A-ViT: Adaptive Tokens for Efficient Vision Transformer" | 2022 | CVPR 2022, arXiv 2112.07658
- 验证: 真实存在 ✓ | 全部正确 ✓
- 正文用法: related_work.tex — ViT token pruning方法 ✓
```

---

## 二、未引用条目 (25 entries in bib but NOT cited in main paper)

These entries exist in `references.bib` but are not `\cite`d in any file included by `main.tex`. They appear only in draft/deprecated files or nowhere at all.

| Key | Status | Note |
|-----|--------|------|
| `brohan2023rt2` | ✗ minor | First author discrepancy with PMLR (filed under Zitkovich). Also duplicates `zitkovich2023rt2`. |
| `brohan2023rt1` | ✓ | Verified correct. Uncited. |
| `ghosh2024octo` | ✓ | Verified correct. Uncited. |
| `li2024roboflamingo` | ✓ | Verified correct. Uncited. |
| `chen2024internvl` | ✗ | Published in *Science China Information Sciences*, not just arXiv. Uncited. |
| `jaegle2021perceiver` | ✓ | Verified correct. Uncited. |
| `alayrac2022flamingo` | ✓ | Verified correct. Uncited. |
| `oquab2024dinov2` | ✗ | Duplicate of `oquab2023dinov2`. Uncited. Remove one. |
| `liu2024llava15` | ✓ | Verified correct. Uncited. |
| `chen2024internvl25` | ✓ | Verified correct. Uncited. |
| `gao2024miniinternvl` | ✓ | Verified correct. Uncited. |
| `zitkovich2023rt2` | ✗ | First author listed as Zitkovich, but actual first author is Brohan. Duplicate of `brohan2023rt2`. |
| `openxembodiment2024` | ✓ | Verified correct. Uncited. |
| `zhang2023h2o` | ✓ | Verified correct. Uncited. |
| `xiao2024streamingllm` | ✓ | Verified correct. Uncited. |
| `mees2022calvin` | ✓ | Verified correct. Uncited. |
| `chi2023diffusionpolicy` | ✓ | Verified correct. Uncited. |
| `zeng2023transformers_tsf` | ✓ | Verified correct. Uncited (only in draft sections/introduction.tex). |
| `bouthillier2024negative` | ✗ | **WRONG AUTHOR**: actual authors are Karl, Florian et al., NOT Bouthillier, Xavier. |
| `ryoo2021tokenlearner` | ✗ minor | arXiv title was updated to "What Can 8 Learned Tokens Do for Images and Videos?" vs NeurIPS title. Uncited. |
| `meng2022adavit` | ✓ | Verified correct. Uncited. |
| `chen2023sparsevit` | ✓ | Verified correct. Uncited. |
| `zhang2024fastervlm` | ✓ | Verified correct. Uncited. |
| `li2024tokenpacker` | ✗ | Accepted at IJCV 2025, bib only lists arXiv. Uncited. |
| `wen2024tinyvla` | ✓ | Accepted at RA-L 2025, bib only lists arXiv. Uncited. |

---

## 三、问题汇总（按严重程度排序）

### 严重问题 (会被 reviewer 标记)

| # | Key | 问题 | 建议修复 |
|---|-----|------|----------|
| 1 | `bouthillier2024negative` | **作者完全错误**：实际作者是 Karl, Florian 等人，非 Bouthillier, Xavier | 修正作者，改 key 为 `karl2024negative`。但此条目未被引用，可直接删除。 |
| 2 | `black2024pi0` | 已被 **RSS 2025** 接收，bib 仍为 arXiv 2024 | 更新为 `@inproceedings`, year=2025, venue=RSS 2025 |
| 3 | `wang2025specprunevla` | 已被 **ICML 2026** 接收，bib 仍为 arXiv 2025 | 更新为 `@inproceedings`, year=2026, venue=ICML 2026 |

### 中等问题

| # | Key | 问题 | 建议修复 |
|---|-----|------|----------|
| 4 | `brohan2023rt2` + `zitkovich2023rt2` | **重复条目**，同一篇 RT-2 (arXiv 2307.15818) | 删除其中一个。两者都未被引用，可都删。 |
| 5 | `oquab2023dinov2` + `oquab2024dinov2` | **重复条目**，同一篇 DINOv2 (arXiv 2304.07193) | 保留 `oquab2023dinov2`（已被引用），删除 `oquab2024dinov2` |
| 6 | `shang2024prumerge` | bib key 年份 "2024" 与 year={2025}/venue ICCV 2025 不一致；缺 arXiv ID | 改 key 为 `shang2025prumerge`，添加 eprint={2403.15388} |
| 7 | 25 个未引用条目 | bib 中大量条目未在 main paper 中 cite | 清理未使用条目，避免 reviewer 质疑 |

### 轻微问题

| # | Key | 问题 | 建议修复 |
|---|-----|------|----------|
| 8 | `oquab2023dinov2` | key 写 "2023" 但 year={2024} | key-year 不一致，cosmetic |
| 9 | `zheng2025xvla` | key 写 "2025" 但 year={2026} (ICLR 2026) | key-year 不一致，cosmetic |
| 10 | `brohan2023rt2` | PMLR proceedings 以 Zitkovich 为第一作者，bib 以 Brohan 为第一作者 | 两种都有依据（arXiv vs proceedings），但严格来说应与正式出版版一致 |
| 11 | `chen2024internvl` | 已发表于 *Science China Information Sciences*，bib 仅列 arXiv | 未被引用，可删除或更新 venue |
| 12 | `li2024tokenpacker` | 已被 IJCV 2025 接收 | 未被引用，可删除或更新 |
| 13 | `wen2024tinyvla` | 已被 RA-L 2025 接收 | 未被引用，可删除或更新 |
| 14 | `ryoo2021tokenlearner` | arXiv 标题已更新为 "What Can 8 Learned Tokens Do..." | 未被引用，若后续引用需注意标题版本 |

### 正文引用用法检查

所有 37 个被引用条目的正文上下文均准确：每处 `\cite` 的描述与被引论文的实际内容一致，未发现张冠李戴的情况。

---
