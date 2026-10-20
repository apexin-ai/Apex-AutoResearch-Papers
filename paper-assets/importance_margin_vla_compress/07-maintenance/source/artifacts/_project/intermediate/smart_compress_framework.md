Smart Token Compression Code Framework
=======================================

Server: cqa1-33015:/root/autodl-tmp/importance_margin_vla_compress/

Files:
- smart_compress_module.py (389 lines) - VisionTokenCompressor + SmartCompressWrapper
- train_smart_compress.py (595 lines) - Training script with --dry-run support
- eval_smart_compress.py (201 lines) - Offline eval with --compare-baseline
- configs/smart_compress.yaml (42 lines) - M=32 config (default)
- configs/smart_compress_m64.yaml (7 lines) - M=64 ablation
- configs/smart_compress_m96.yaml (7 lines) - M=96 ablation

Dry-Run Results (M=32):
- Forward shape: [4, 50, 32] ✓
- Loss: 1.0367 ✓
- Compressor receives gradients: ✓ (queries grad=0.28)
- Expert receives gradients: ✓
- VLM+SigLIP frozen: ✓
- Compressor params: 22.2M
- Total trainable: 122.1M / 472.2M (25.85%)
- Compression: 128→32 tokens (75% reduction)

Training command:
HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 python train_smart_compress.py --config configs/smart_compress.yaml