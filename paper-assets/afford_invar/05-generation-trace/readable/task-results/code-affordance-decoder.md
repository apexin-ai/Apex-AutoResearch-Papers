# code affordance decoder

**afford invar** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_affordance-decoder_20260519T202650_result.json`
- **Structured JSON:** [`a6720fb940d797c70ccc.json`](../../sessions/a6/a6720fb940d797c70ccc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 产出总结

### 1. 文件位置
- 服务器: `/root/afford_invar/openvla-oft/prismatic/models/affordance_decoder.py`
- 本地备份: `/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/afford_invar/artifacts/affordance_decoder.py`

### 2. 参数量
**7,867,649 (7.87M)** — 接近 8M 目标

| 模块 | 参数量 |
|------|--------|
| input_proj (Linear 4096→512) | 2,097,664 |
| deconv1 (512→256) + GN | 2,097,664 |
| deconv2 (256→64) + GN | 262,272 |
| deconv3 (64→1) | 1,025 |
| text_proj1/2/3 (FiLM) | 3,408,960 |

### 3. Dry-run 验证结果
```
input:  image_features [1, 256, 4096]  ← layer-18 image tokens
        text_embed     [1, 4096]       ← layer-18 text tokens mean pool
output: heatmap        [1, 1, 128, 128] ← affordance map, range [0, 1]
```

### 4. OpenVLA 关键架构信息
- **hidden_dim**: 4096 (Llama-2-7b)
- **num_layers**: 32
- **image tokens**: 256 (16×16, 来自 DINOv2+SigLIP fused, 224px/patch14)
- **vision embed_dim**: 2176 (DINOv2=1024 + SigLIP=1152)，经 FusedMLPProjector 映射到 4096
- **hidden_states 结构**: 33 个 tensor (1 embedding + 32 layers)，每个 [B, seq_len, 4096]
- **multimodal seq_len**: `input_ids_len + 256` (image patches 插入 BOS 后)
- **action head**: `L1RegressionActionHead` / `DiffusionActionHead`，输入 last-layer action token hidden states

### 5. Image tokens vs Text tokens 分离
在 multimodal hidden states 中：
- **BOS**: position 0
- **Image tokens**: positions `1` 到 `256` (即 `h[:, 1:257, :]`)
- **Text tokens**: positions `257` 起（到 action tokens 之前）
- `seq_len - input_ids_len = 256` 已验证

---
