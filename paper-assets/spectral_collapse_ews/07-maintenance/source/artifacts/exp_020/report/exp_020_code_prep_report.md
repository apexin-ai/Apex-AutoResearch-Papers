# exp_020: GPT-2-medium Cross-Architecture Validation — Code Prep Report

**Date**: 2026-05-23  
**Status**: Code ready, awaiting GPU availability to launch

## 1. Code Changes

### New Files Created (on server `/root/spectral_collapse_ews/`)

| File | Purpose |
|------|---------|
| `run_gpt2m_phase1.py` | Phase 1 runner for GPT-2-medium. Standalone script (does NOT modify `run_phase1.py`). Uses same `src.pipeline.run_recursive_training` as Pythia experiments. Handles GPT-2-specific data paths (`data/*_gpt2m.pt`) and checkpoint directory (`checkpoints_phase1_gpt2m/`). |
| `prepare_data_gpt2m.py` | Re-tokenizes Pile data with GPT-2 tokenizer. Produces `train_real_50k_gpt2m.pt`, `eval_5k_gpt2m.pt`, `spectral_1k_gpt2m.pt`. Same filtering criteria as Pythia data (min 256 non-pad tokens). |
| `dry_run_gpt2m.py` | CPU dry-run test — loads model, forward+backward, embedding extraction, SVD, generation. |
| `scripts/launch_gpt2medium_r0_seed42.sh` | Launch script for exp_020. Accepts GPU_ID as `$1`. Auto-checks model availability and data prep. |

### Model Download

- GPT-2-medium downloaded to `/root/autodl-tmp/.hf_cache/models--gpt2-medium/`
- Symlinked into `models/` directory: `models/models--gpt2-medium -> /root/autodl-tmp/.hf_cache/models--gpt2-medium`
- Works with `HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1` (no network needed at runtime)

### No Existing Files Modified

- `run_phase1.py` — untouched (exp_018/019 depend on it)
- `src/*.py` — untouched (all pipeline code is model-agnostic)
- Existing data files — untouched

## 2. Why No Pipeline Changes Were Needed

The existing `src/` pipeline is fully model-agnostic:
- **Model loading** (`pipeline.py`): Uses `AutoModelForCausalLM` / `AutoTokenizer` — works for any HF CausalLM
- **Pad token** (`pipeline.py`): Already handles `pad_token is None` → sets to `eos_token` (GPT-2 has no pad_token)
- **BOS token** (`generate.py`, `evaluate.py`): Falls back to `eos_token_id` if `bos_token_id` is None (GPT-2's bos=eos=50256)
- **Embedding extraction** (`rankme.py`): Uses `output_hidden_states=True` + `outputs.hidden_states[-1]` — standard HF API
- **SVD/spectral metrics** (`rankme.py`): Model-agnostic, operates on hidden state matrix

### Data Incompatibility

Pythia uses NeoX BPE tokenizer (vocab 50304), GPT-2 uses GPT-2 BPE tokenizer (vocab 50257). Token IDs are NOT compatible → re-tokenization required via `prepare_data_gpt2m.py`.

## 3. Dry-Run Results

```
DRY RUN: GPT-2-medium pipeline test (CPU)

[1/5] Loading model and tokenizer...
  Parameters: 354,823,168
  Vocab size: 50257
  Hidden size: 1024
  Num layers: 24
  pad_token: '<|endoftext|>' (id=50256)
  bos_token: '<|endoftext|>' (id=50256)

[3/5] Forward pass (training mode)...
  Forward+backward in 25.2s (CPU)
  Loss: 12.2008

[4/5] Extracting embeddings (last hidden state, mean-pooled)...
  Embedding shape: torch.Size([4, 1024])

[5/5] Computing spectral metrics (SVD on 4 samples)...
  Singular values: [380.92, 5.30, 2.67, 2.28]
  Effective rank: 1.1595
  Log-det: 9.4125
  sigma_1: 380.9213

[6/6] Test text generation (5 tokens)...
  Generated: 'On Feb. 13,'

DRY RUN: ALL TESTS PASSED
```

## 4. GPU Memory Estimate

| Component | Size |
|-----------|------|
| Model params (fp32) | 1.32 GB |
| Gradients | 1.32 GB |
| Optimizer states (AdamW) | 2.64 GB |
| Activations (est.) | 0.66 GB |
| **Total estimate** | **~5.9 GB** |

Peak during generation (batch_size=32, seq_len=512): estimated ~8-10 GB total.

RTX PRO 6000 has 98 GB total, with 72 GB free on GPU 0 and 78 GB free on GPU 1. **Well within limits.**

## 5. Estimated Wall Time

Based on Pythia-410M pure_collapse timing on same server:
- **Per generation**: ~2 hours (50k synthetic gen + 1 epoch training + evaluation)
- **Total (10 gen + gen_0 baseline)**: ~20-22 hours

GPT-2-medium (355M) is slightly smaller than Pythia-410M, so actual time may be ~5-10% less.

## 6. Launch Command

```bash
# Wait for a GPU to free up (exp_018 on cuda:0, exp_019 on cuda:1)
# Then:
nohup bash /root/spectral_collapse_ews/scripts/launch_gpt2medium_r0_seed42.sh <GPU_ID> \
  > /root/spectral_collapse_ews/logs/exp_020_gpt2m_r0_s42.log 2>&1 &
```

The script will auto-run `prepare_data_gpt2m.py` if tokenized data doesn't exist yet (requires network for Pile download, ~10 min).

## 7. Output Paths

| Output | Path |
|--------|------|
| Results JSON | `results/phase1_gpt2m_pure_collapse_seed42_results.json` |
| Summary JSON | `results/phase1_gpt2m_pure_collapse_seed42_summary.json` |
| Checkpoints | `/root/autodl-tmp/spectral_collapse_ews/checkpoints_phase1_gpt2m/pure_collapse_seed42/gen_{0..10}/` |

## 8. Issues and Caveats

1. **Data prep requires network**: `prepare_data_gpt2m.py` streams from HuggingFace Pile dataset. Must run `source /etc/network_turbo` first. The launch script handles this automatically.
2. **GPT-2 attention mask warning**: GPT-2 uses same token for bos/eos/pad (id=50256), which triggers a harmless HF warning about attention mask during generation. Does not affect correctness.
3. **`loss_type=None` warning**: HF config has unrecognized `loss_type=None`, defaults to `ForCausalLMLoss`. Harmless.
4. **No data overlap guarantee**: `prepare_data_gpt2m.py` re-streams from Pile and applies same filtering (non_pad ≥ 256). Same text content as Pythia data, different tokenization. If exact byte-level matching is needed, would require loading Pythia data and re-tokenizing text — current approach is simpler and statistically equivalent.
