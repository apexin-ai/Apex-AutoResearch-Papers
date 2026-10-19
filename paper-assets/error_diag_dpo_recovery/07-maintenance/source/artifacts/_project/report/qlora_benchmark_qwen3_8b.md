## QLoRA Benchmark: Qwen3-8B on RTX 4090D

**Date**: 2026-05-12
**Server**: cqa1-21977 (SeetaCloud, RTX 4090D)
**GPU**: cuda:0 (single card)

### Configuration
- Model: Qwen/Qwen3-8B (16.4GB, 5 safetensors shards)
- Quantization: 4-bit NF4, double quant, bfloat16 compute
- LoRA: r=16, alpha=32, targets=[q_proj, k_proj, v_proj, o_proj]
- Trainable params: 15,335,424 / 8,206,070,784 (0.19%)
- Sequence length: 2048 tokens
- Optimizer: AdamW, lr=1e-5

### Results

| Metric | Value |
|--------|-------|
| Model load time | ~15s (5 shards) |
| Step 0 (warmup) | 0.68s |
| Avg step time (1-4) | 0.28s |
| Loss (step 0 -> 4) | 0.0822 -> 0.0799 |
| Inference speed | 15.5 tokens/sec |
| Inference latency (200 tokens) | 12.90s |
| Peak GPU memory | 10.6GB |

### Notes
- Model downloaded via hf-mirror.com (Chinese CDN, ~15MB/s without proxy)
- network_turbo proxy was counterproductive for hf-mirror.com downloads
- 4-bit model fits comfortably in single 4090D (24GB) with 10.6GB usage