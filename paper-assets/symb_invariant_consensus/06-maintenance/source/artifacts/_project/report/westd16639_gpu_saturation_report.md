# westd-16639 GPU Saturation Report

**Date**: 2026-05-19 01:51 UTC  
**Server**: westd-16639 (AutoDL, 4x NVIDIA RTX PRO 6000 Blackwell, 98GB each)  
**Connection**: via westd-25068 jump → `ssh -p 16639 root@connect.westd.seetacloud.com`

## System Status Post-Recovery

| Item | Status |
|------|--------|
| GPU | 4x RTX PRO 6000 Blackwell, 98GB VRAM each |
| RAM | 1.0 TiB total, ~191GB free after all 4 vLLMs |
| Disk | 30GB system (42% used), 350GB data disk |
| Python | 3.12.3 (miniconda base) |
| vLLM | 0.21.0 |
| z3 | 4.15.4 |
| Network | HuggingFace blocked, hf-mirror.com OK |

## Key Finding: Instance Was Reset

The crash resulted in a **full instance reset**. Previous experiment data (intermediates, results) were lost:
- exp-032 intermediates: 0 (was 509/600)
- exp-033 intermediates: 0 (was 518/600)
- exp-035 intermediates: 0
- Project code: absent, re-synced from westd-25068

## Cached Models (on /root/autodl-tmp/models/)

| Model | Size | Status |
|-------|------|--------|
| Qwen2.5-14B-Instruct | 28GB (8 shards) | OK |
| Qwen3-14B | 28GB (8 shards) | OK |
| Mistral-7B-Instruct-v0.3 | 10GB (3 shards) | **Corrupted** (shard 2/3 truncated, re-downloading) |
| DeepSeek-R1-0528-Qwen3-8B | 13GB | Downloading (in progress) |
| Phi-4-reasoning | 26GB | Downloading (in progress) |
| Gemma-3-27b-it | FAILED | 403 (gated repo) |
| Llama-4-Scout-17B | FAILED | 403 (gated repo) |

## Experiments Launched

All 4 GPUs saturated at 100% utilization. vLLM instances started with `VLLM_USE_FLASHINFER_SAMPLER=0` (Blackwell requirement).

| GPU | Exp ID | Model | Dataset | Problems | Port | tmux |
|-----|--------|-------|---------|----------|------|------|
| 0 | exp-032 | Qwen2.5-14B-Instruct | ProofWriter full | 600 | 8000 | exp032 |
| 1 | exp-033 | Qwen3-14B (non-thinking) | ProofWriter full | 600 | 8001 | exp033 |
| 2 | exp-036 | Qwen2.5-14B-Instruct | FOLIO full | 204 | 8002 | exp036 |
| 3 | exp-038 | Qwen2.5-14B-Instruct | LogiQA 200 | 200 | 8003 | exp038 |

### Configuration
- K=12, temperature=0.7, max_tokens=4096, max_model_len=8192
- gpu_memory_utilization=0.9
- All experiments use `--save-intermediates --resume`
- Qwen3 non-thinking: `--default-chat-template-kwargs '{"enable_thinking": false}'`

### Progress at Report Time
- exp-032: 6/600 (~45s/prob, ETA ~7.5h)
- exp-033: 2/600 (running)
- exp-036: 3/204 (running)
- exp-038: 1/200 (just started)

### Startup Sequence
vLLM instances staggered by ~1-2 min intervals to avoid memory contention:
1. GPU0 (exp-032) → started 01:44, ready by 01:45
2. GPU1 (exp-033) → started 01:45, ready by 01:46
3. GPU2 (exp-036) → started 01:46, ready by 01:47
4. GPU3 (exp-038) → started 01:50, ready by 01:51

## Deviations from Plan

1. **No ARC data available** on disk. GPU2 reassigned to FOLIO204 (Qwen2.5-14B).
2. **Mistral-7B corrupted** (safetensors shard 2/3 truncated). GPU3 reassigned to Qwen2.5-14B + LogiQA200. Mistral re-download in progress.
3. **All experiments start from scratch** due to instance reset losing all intermediates.

## Pending Actions

1. Monitor Mistral-7B re-download completion, then run Mistral-7B FOLIO204 experiment (after exp-038 LogiQA finishes on GPU3)
2. Once DeepSeek-R1-0528-Qwen3-8B download completes, consider additional experiments
3. ARC dataset needs to be prepared if exp-035 is still needed

## Monitoring Commands

```bash
# Check all GPU utilization
ssh -p 16639 root@connect.westd.seetacloud.com 'nvidia-smi --query-gpu=index,memory.used,utilization.gpu --format=csv'

# Check experiment progress
ssh -p 16639 root@connect.westd.seetacloud.com 'for d in exp032_qwen25_14b_pw600 exp033_qwen3_14b_pw600_nonthinking exp036_qwen25_14b_folio204 exp038_qwen25_14b_logiqa200; do echo "$d: $(ls /root/symb_invariant_consensus/results/$d/intermediates/ 2>/dev/null | wc -l)"; done'

# Check vLLM ports
ssh -p 16639 root@connect.westd.seetacloud.com 'for p in 8000 8001 8002 8003; do curl -s http://localhost:$p/v1/models 2>/dev/null | head -1 && echo "port $p OK" || echo "port $p FAIL"; done'

# Check tmux sessions
ssh -p 16639 root@connect.westd.seetacloud.com 'tmux ls'
```
