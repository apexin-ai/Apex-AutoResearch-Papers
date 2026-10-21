# MVP Environment Setup Report — westd-32570

**Date**: 2026-05-21  
**Server**: westd-32570 (AutoDL)

## Software Versions

| Component      | Version            |
|----------------|--------------------|
| Python         | 3.12.3             |
| PyTorch        | 2.8.0+cu128        |
| CUDA           | 12.8               |
| cuDNN          | 9.10.2 (91002)     |
| vLLM           | 0.11.0             |
| transformers   | 4.57.6             |
| triton         | 3.4.0              |

## GPU Info

| GPU | Model | VRAM |
|-----|-------|------|
| 0   | NVIDIA RTX PRO 6000 Blackwell Server Edition | 94 GB |
| 1   | NVIDIA RTX PRO 6000 Blackwell Server Edition | 94 GB |
| 2   | NVIDIA RTX PRO 6000 Blackwell Server Edition | 94 GB |
| 3   | NVIDIA RTX PRO 6000 Blackwell Server Edition | 94 GB |

- **Architecture**: Blackwell (sm_120)
- **Total VRAM**: 376 GB
- **CUDA arch list**: sm_70, sm_75, sm_80, sm_86, sm_90, sm_100, sm_120

## Model

| Field | Value |
|-------|-------|
| Name  | Meta-Llama-3.1-8B-Instruct |
| Path  | `/root/nlp_variance_gtheory/models/.hf_cache/LLM-Research/Meta-Llama-3___1-8B-Instruct` |
| Size  | 15 GB (4 safetensors shards) |
| Source | ModelScope (`LLM-Research/Meta-Llama-3.1-8B-Instruct`) |
| HF_TOKEN | Not required (downloaded via ModelScope) |

## Verification Results

- **torch + CUDA**: PASS — `torch.randn` on GPU, matmul, sm_120 in arch list
- **vLLM model load**: PASS — 14.99 GiB, 4.62s load time, Flash Attention backend
- **vLLM inference**: PASS — generated coherent text from "Hello, my name is" prompt
- **KV cache**: 8.62 GiB available, 70,640 tokens capacity at `gpu_memory_utilization=0.3`

## Project Directory Structure

```
/root/nlp_variance_gtheory/
├── models/.hf_cache/LLM-Research/Meta-Llama-3___1-8B-Instruct/
├── data/
├── src/
├── configs/
├── outputs/
└── logs/
```

## Issues Encountered & Resolutions

1. **Blackwell sm_120 not supported by torch 2.6.0+cu124** — Original server had torch 2.6.0 which predates Blackwell. Required upgrade to torch 2.8.0+cu128 which includes sm_120 kernels.

2. **transformers 5.x incompatible with vllm 0.8.x** — `TokenizersBackend` attribute error. Downgraded to transformers 4.57.6.

3. **Root partition only 30GB** — Repeated disk-full errors during large package downloads. Resolved by: uninstalling old packages before installing new ones, purging pip cache, cleaning temp dirs.

4. **Slow downloads from download.pytorch.org** — `source /etc/network_turbo` proxy accelerated downloads from ~700 KB/s to 200+ MB/s. Critical for nvidia packages (total ~2.5 GB).

5. **nvidia cu128 package versions not on PyPI** — Initial install used wrong version pins. Fixed by reading torch wheel metadata (`curl` the `.whl.metadata` URL) to get exact dependency versions, then split install: nvidia deps from Aliyun mirror (fast), torch wheel from cu128 index with `--no-deps`.

6. **vLLM version pairing** — vllm 0.21.0 requires torch 2.11.0; vllm 0.11.2 requires torch 2.9.0. Only vllm 0.11.0 matches torch 2.8.0. torchvision/torchaudio versions must also match (0.23.0 and 2.8.0 respectively).

## Disk Usage

- Root partition: 25 GB used / 30 GB total (5.1 GB free)
- Model on root partition (15 GB) — consider moving to `/root/autodl-tmp/` if space becomes tight
