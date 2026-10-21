# Smart Token Compression Framework

## Files on cqa1-33015:/root/autodl-tmp/importance_margin_vla_compress/

### Core
- `smart_compress_module.py` (389 lines): VisionTokenCompressor + SmartCompressWrapper
- `train_smart_compress.py` (595 lines): Training script with --dry-run support
- `eval_smart_compress.py` (201 lines): Offline eval with --compare-baseline

### Configs
- `configs/smart_compress.yaml`: M=32 (75% compression, default)
- `configs/smart_compress_m64.yaml`: M=64 (50% compression)
- `configs/smart_compress_m96.yaml`: M=96 (25% compression)

## Architecture
- Cross-attention pooling: M learnable queries attend to 128 vision tokens
- 2 cross-attention layers, 12 heads, hidden_dim=960
- Inserted between connector output and VLM input
- Frozen: SigLIP + connector + VLM text model
- Trainable: Compressor (22.2M) + Expert+projections (99.9M) = 122.1M / 472.2M (25.85%)

## Dry-Run Results (2026-05-18)
- Forward: loss=1.0367, shape=[B=4, chunk=50, max_action_dim=32] ✓
- Compressor gradient: ✓ (queries grad_norm=0.28)
- Expert gradient: ✓
- VLM+SigLIP frozen: ✓

## Usage
```bash
# Dry run
HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 python train_smart_compress.py --config configs/smart_compress.yaml --dry-run

# Train (do not start yet)
HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 python train_smart_compress.py --config configs/smart_compress.yaml

# Eval
HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 python eval_smart_compress.py --checkpoint checkpoints/smart_compress_m32/checkpoint.pt --config configs/smart_compress.yaml --compare-baseline
```