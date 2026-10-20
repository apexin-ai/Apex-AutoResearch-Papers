# NORA VLA 架构分析报告

**Server**: westd-19183 (cuda:1)  
**Checkpoint**: `declare-lab/nora-long-finetuned-libero-goal`  
**Base model**: Qwen2.5-VL-3B-Instruct (full fine-tune)  
**Date**: 2026-05-21

---

## 1. 环境搭建

| 项目 | 详情 |
|------|------|
| 环境类型 | venv (`--system-site-packages`, 继承 base conda 的 torch) |
| 路径 | `/root/autodl-tmp/vla-ssd/envs/nora/` |
| 激活 | `source /root/autodl-tmp/vla-ssd/envs/nora/bin/activate` |
| torch | 2.10.0+cu128 (继承自 base conda) |
| transformers | 4.50.0 (venv 内安装, 不影响 base 的 4.48.3) |
| 额外依赖 | qwen_vl_utils==0.0.14, av==17.0.1 |

**隔离验证**: base conda 的 `transformers==4.48.3` 未被修改。

---

## 2. NORA 架构详情

### 2.1 Language Model (Qwen2.5-3B)

| 参数 | 值 |
|------|-----|
| architecture | `Qwen2_5_VLForConditionalGeneration` |
| num_hidden_layers | 36 |
| hidden_size | 2048 |
| intermediate_size (MLP) | 11008 |
| num_attention_heads | 16 |
| num_key_value_heads | 2 (GQA 8:1) |
| head_dim | 128 |
| activation | SiLU |
| RoPE | M-RoPE, sections=[16,24,24] (temporal,height,width), θ=1e6 |
| max_position_embeddings | 128,000 |
| vocab_size | 153,713 (base 151,936 + 1,777 action/special tokens) |
| tie_word_embeddings | true |
| dtype | bfloat16 |
| loading API | `AutoModelForImageTextToText` |

### 2.2 Vision Encoder (Qwen2.5-VL ViT)

| 参数 | 值 |
|------|-----|
| depth | 32 layers |
| hidden_size | 1280 |
| num_heads | 16 |
| intermediate_size | 3420 |
| out_hidden_size | 2048 (projects to LLM dim) |
| patch_size | 14 × 14 |
| spatial_merge_size | 2 (2×2 patch tokens → 1 merged token) |
| temporal_patch_size | 2 |
| attention | Windowed (window_size=112), full attention at layers [7,15,23,31] |
| activation | SiLU |

### 2.3 Image Processor

| 参数 | 值 |
|------|-----|
| min_pixels | 3,136 (≈56×56) |
| max_pixels | 12,845,056 (≈3585×3585) |
| image_mean | [0.481, 0.458, 0.408] (CLIP normalization) |
| image_std | [0.269, 0.261, 0.276] |
| resize granularity | 28 (patch_size × spatial_merge_size) |

**动态分辨率**：输入图像被 resize 到最近的 28 的倍数。LIBERO 128×128 → 140×140 → 25 image tokens (5×5)。若用 224×224 → 64 tokens (8×8)。

### 2.4 Weight Shapes (Layer 0 & 35)

```
q_proj.weight:  [2048, 2048]   # 16 heads × 128 dim
k_proj.weight:  [256,  2048]   # 2 KV heads × 128 dim
v_proj.weight:  [256,  2048]
o_proj.weight:  [2048, 2048]
gate_proj.weight: [11008, 2048]  # SwiGLU MLP
up_proj.weight:   [11008, 2048]
down_proj.weight: [2048, 11008]
```

---

## 3. Token Layout (LIBERO 128×128 输入)

```
Pos:  0  ...  13  | 14           | 15  ...  39    | 40          | 41 ... 50 | 51  52
      ─────────── | ──────────── | ────────────── | ─────────── | ───────── | ────────
      system/chat | <vision_start>| 25 image tokens| <vision_end>| instruction| <im_end> assistant\n
      template    |              | (5×5 merged)   |             | tokens     | [readout]
```

- **Total tokens**: 53
- **Image tokens**: 25 个, positions 15–39
- **Vision start marker**: pos 14 (token_id=151652)
- **Vision end marker**: pos 40 (token_id=151653)
- **Instruction text**: pos 41 onwards
- **Readout** (last pre-action): pos 52

与 OpenVLA 的关键区别：NORA 图像 tokens 被 vision_start/end 标记包围，且数量因图像分辨率动态变化。OpenVLA 是固定 256 tokens 紧跟 BOS。

---

## 4. Dry-run 结果 (1 task × 1 demo × 10 timesteps)

**Task**: "open the middle drawer of the cabinet"  
**Data**: LIBERO-Goal, demo_0, 128×128 RGB, 10 timesteps  
**GPU**: cuda:1 (CUDA_VISIBLE_DEVICES=1)  
**Model load time**: 3.1s

### Hidden States

| 指标 | Shape | 说明 |
|------|-------|------|
| Total hidden layers | 37 | L0 (embedding) + L1–L36 |
| Per-timestep shape | [53, 2048] | seq_len × hidden_dim |
| Stacked shape | [10, 53, 2048] | timesteps × seq_len × hidden_dim |
| image_mean shape | [10, 2048] | mean over 25 image tokens per timestep |
| readout shape | [10, 2048] | last token per timestep |

### Attention

| 指标 | 值 |
|------|-----|
| Layers | 36 |
| Shape per layer | [1, 16, 53, 53] (batch, heads, seq, seq) |
| L0 mean | 0.018868 |
| L0 max | 1.0 |

### Hidden State Statistics

| 位置 | Layer | mean | std |
|------|-------|------|-----|
| image_mean | L0 (embedding) | -0.0056 | 2.6886 |
| image_mean | L35 (last) | 0.0323 | 2.6001 |
| readout | L0 (embedding) | 0.0008 | **0.0259** |
| readout | L35 (last) | 0.0425 | **3.6988** |

**关键观察**:
- L0 readout 的 std 极低 (0.026) → 嵌入层的最后 token 几乎无信息
- L_last readout 的 std 很高 (3.70) → 深层表征在 readout 位置积累了大量信息
- image_mean 的 std 在 L0 和 L_last 之间变化不大 (~2.6–2.7) → 图像特征在各层间较为稳定
- 这与 OpenVLA 的模式一致：深层 readout 是最具信息量的表征位点

---

## 5. OpenVLA / TracVLA / NORA 对比表

| 特性 | OpenVLA | TracVLA | NORA |
|------|---------|---------|------|
| **Base LLM** | Llama-2-7B | Phi-3-mini-3.8B | Qwen2.5-3B |
| **总参数量** | ~7B | ~3.8B | ~3B |
| **Transformer layers** | 32 | 32 | 36 |
| **Hidden dim** | 4096 | 3072 | 2048 |
| **Attention type** | MHA | MHA | **GQA (8:1)** |
| **Attention heads** | 32 | 32 | 16 |
| **KV heads** | 32 | 32 | **2** |
| **Head dim** | 128 | 96 | 128 |
| **Vision encoder** | SigLIP + DINOv2 | CLIP ViT-L/14 | Qwen2.5-VL ViT (32L) |
| **Image tokens** | 256 (fixed) | ~256 | **Dynamic** (25@128px, 64@224px) |
| **Image resolution** | 224×224 (fixed) | 336×336 | Dynamic (any) |
| **RoPE** | Standard | Su-scaled | **M-RoPE** [16,24,24] |
| **Action tokenization** | 256 discrete bins | Continuous | **FAST+ 2048 tokens** |
| **Vocab size** | 32,064 | 32,064 | 153,713 |
| **Training strategy** | Full fine-tune | Full fine-tune | Full fine-tune |
| **Loading API** | `AutoModelForVision2Seq` | `AutoModelForCausalLM` (+trust_remote_code) | `AutoModelForImageTextToText` |
| **Token layout** | `[BOS][256 img][text...]` | `[<s>][<image>tokens][text...]` | `[..chat..][<vs>][N img][<ve>][text...][<assistant>]` |

---

## 6. Qwen2.5-VL-3B Base (Untrained Baseline) 下载状态

| 项目 | 状态 |
|------|------|
| Checkpoint | `Qwen/Qwen2.5-VL-3B-Instruct` |
| 路径 | `/root/autodl-tmp/vla-ssd/checkpoints/qwen25-vl-3b-base/` |
| Config 文件 | 已下载 (config.json, tokenizer.json 等) |
| 权重 shard 1 | 已完成 (3,982,649,232 bytes) |
| 权重 shard 2 | 已完成 (3,526,688,744 bytes) |
| 总大小 | 7.5GB (total_size=7,509,245,952) |

Qwen base 与 NORA 的架构完全相同（相同 hidden_size/layers/heads），唯一区别是 vocab_size：
- Qwen base: **151,936** (标准 Qwen2.5 词表)
- NORA fine-tuned: **153,713** (增加了 1,777 个 FAST+ action tokens)

---

## 7. 兼容性问题与 SSD 分析适配要点

### 7.1 表征提取兼容性

| 问题 | 影响 | 解决方案 |
|------|------|---------|
| GQA 注意力 (2 KV heads) | Attention map shape 不同于 OpenVLA/TracVLA | 分析时注意力头维度: [16, seq, seq]，非 [32, seq, seq] |
| 动态图像 token 数 | image_mean 聚合的 token 数不固定 | 用 vision_start/end ID 动态定位 image token 范围 |
| AutoModelForImageTextToText | 不同于 OpenVLA 的 Vision2Seq 和 TracVLA 的 CausalLM | 需要单独的加载代码路径 |
| transformers 版本 | NORA 需要 ≥4.50, base env 是 4.48.3 | 已通过 venv 隔离解决 |
| Chat template 开销 | system/chat 模板占用前 14 个 token positions | 提取时需排除这些位置，或统一起始偏移 |

### 7.2 SSD Probing 适配建议

1. **image_mean 提取**: 用 `vision_start_token_id` / `vision_end_token_id` 动态定位，不要硬编码 position
2. **readout 提取**: 用 `input_ids` 的最后一个 position（与 OpenVLA 一致）
3. **跨模型对比**: hidden_dim 不同 (2048 vs 4096 vs 3072)，probing 时需 per-model linear head 或 PCA 对齐
4. **GQA attention 分析**: 16 heads 但只有 2 组 KV → attention pattern 的 diversity 可能低于 MHA 模型
5. **Action token 数量**: NORA 使用 FAST+ (2048 tokens) vs OpenVLA (256 bins) → 影响 action probing 设计
6. **Trained vs Untrained 对比**: 两个 checkpoint 架构相同，可直接做 layer-wise 差异分析，需注意 vocab_size 不同导致 embedding layer shape 差异

---

## 8. 文件清单

```
/root/autodl-tmp/vla-ssd/
├── checkpoints/
│   ├── nora-libero-goal/         # 7.5GB, 完整
│   │   ├── model-00001-of-00002.safetensors (4.7GB)
│   │   ├── model-00002-of-00002.safetensors (2.4GB)
│   │   ├── config.json, tokenizer.json, ...
│   └── qwen25-vl-3b-base/       # 7.5GB, 完整
│       ├── config.json, tokenizer.json, ...
│       ├── model-00001-of-00002.safetensors (3.7GB)
│       └── model-00002-of-00002.safetensors (3.3GB)
├── envs/
│   └── nora/                     # venv, transformers==4.50.0
└── data/
    └── libero/libero_goal/       # HDF5 demos
```

```
/tmp/nora_dryrun.py               # Dry-run 提取脚本
/tmp/nora_dryrun.log              # 运行日志
```
