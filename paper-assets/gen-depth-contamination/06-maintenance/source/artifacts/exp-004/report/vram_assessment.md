# exp-004 VRAM Feasibility Assessment

## Server: westc-26893 (RTX 4090D 24GB)
- Current VRAM usage: 22950/24564 MiB (exp-006 + exp-015 running)
- Disk: 134GB free on /root/autodl-tmp/
- Env: torch 2.10.0+cu128, transformers 4.57.6, bitsandbytes 0.49.2

## Plan A: fp16 (RECOMMENDED)
- Model weights: ~14GB
- KV-cache (seq=512, batch=1): ~28MB (negligible, GQA with 4 KV heads)
- Logits + activations: ~2GB
- **Peak VRAM: ~16.2GB** — fits in 24GB with ~8GB headroom
- Requires GPU exclusive (after exp-006 completes)

## Plan B: 4-bit quantization
- Model weights: ~4GB
- **Peak VRAM: ~6GB**
- Risk: quantization noise (~0.5-2 nats) may mask depth-adjacent AUC differences
- **Only suitable for preliminary sanity check, not formal results**

## Model Download Status
- Only Qwen2.5-1.5B-Instruct cached (2.9GB)
- 7B model NOT downloaded yet (~14GB download needed)
- Download command (execute when GPU not IO-busy):
  ```
  source /etc/network_turbo
  export HF_HOME=/root/autodl-tmp/.hf_cache
  export HF_HUB_DISABLE_XET=1
  python -c "from modelscope import snapshot_download; snapshot_download('Qwen/Qwen2.5-7B-Instruct', cache_dir='/root/autodl-tmp/.hf_cache')"
  ```

## Recommendation
Use Plan A (fp16). Wait for exp-006 to complete, download 7B model, then run with batch_size=1.