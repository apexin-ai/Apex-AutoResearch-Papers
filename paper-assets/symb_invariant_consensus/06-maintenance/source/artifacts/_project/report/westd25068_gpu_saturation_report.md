# westd-25068 GPU Saturation Report

**Date**: 2026-05-19 01:48 UTC  
**Objective**: Maximize GPU utilization from 12.5% to 100%  
**Result**: 4/4 GPUs at 96-98% utilization

---

## 1. Network Status

| Endpoint | Status |
|----------|--------|
| huggingface.co | **BLOCKED** (timeout) |
| hf-mirror.com | **OK** (HTTP 200) |
| modelscope.cn | **OK** (HTTP 200) |

**Fix applied**: `export HF_ENDPOINT=https://hf-mirror.com` added to `/root/.bashrc`.

---

## 2. Cached Models

| Model | Size | Status |
|-------|------|--------|
| Qwen2.5-14B-Instruct | 28G | Complete |
| Qwen3-14B | 28G | Complete |
| Qwen2.5-7B-Instruct | 15G | Complete |
| Qwen2.5-72B-Instruct | 100G | Complete (too large for single GPU) |
| Mistral-7B-Instruct-v0.3 | 16G | Complete |
| Llama-3.1-8B-Instruct | 1.1G | **Incomplete** (1/4 shards), re-downloading |
| deepseek-r1-0528-qwen3-8b | 8.7G | Downloading |
| DeepSeek-R1-Distill-Llama-8B | 1.2G | Downloading |
| gemma-3-27b-it | 23G | Downloading |
| phi-4-reasoning | 11G | Downloading |
| llama-4-scout | N/A | **FAILED** (access denied, requires approval) |

---

## 3. exp-027 Results (Qwen3-14B non-thinking, FOLIO-204)

| Metric | Value |
|--------|-------|
| SICA Accuracy | **84.31%** |
| SC Accuracy | **83.82%** |
| SICA delta over SC | **+0.49pp** |
| N problems | 204 |
| K (samples) | 12 |
| Extraction Rate | 99.5% |
| Contradiction Rate | 2.83% |
| Problems with contradictions | 69/204 |
| Total wall time | 11,017s (~3.1h) |
| Total constraints extracted | 16,153 |
| Unique constraints | 7,031 |

**Key finding**: Qwen3-14B non-thinking achieves +9.8pp over Qwen2.5-14B (74.51%) on SICA, and +8.8pp on SC. This is the best single-model result so far (excluding oracle).

---

## 4. All Existing Results on this Server

| Experiment | Model | Dataset | SICA | SC | Delta |
|-----------|-------|---------|------|-----|-------|
| folio_204_14b | Qwen2.5-14B | FOLIO-204 | 74.51% | 75.00% | -0.49pp |
| exp-027 | Qwen3-14B (non-thinking) | FOLIO-204 | 84.31% | 83.82% | +0.49pp |
| exp-028 (partial 35/204) | Qwen3-14B (thinking) | FOLIO-204 | 88.57% | 85.71% | +2.86pp |
| cross_model_mistral | Mistral-7B extractor | FOLIO-204 | 75.00% (cross) | 75.00% | 0pp |
| exp-029 | Contrastive | FOLIO-182 | 72.53% | 73.63% | -1.10pp |
| exp-031 | Oracle (gold FOL) | FOLIO-204 | 89.71% | 75.49% | +14.22pp |

---

## 5. GPU Allocation (Post-fix)

| GPU | Memory | Util | Experiment | Model | Dataset | Port | tmux |
|-----|--------|------|------------|-------|---------|------|------|
| cuda:0 | 87965/97887 MiB | 96% | **exp-033** | Mistral-7B-Instruct-v0.3 | FOLIO-204 | 8000 | exp033_run |
| cuda:1 | 88239/97887 MiB | 98% | **exp-034** | Qwen2.5-14B-Instruct | ProofWriter-600 | 8001 | exp034_run |
| cuda:2 | 88287/97887 MiB | 97% | exp-028 | Qwen3-14B (thinking) | FOLIO-204 | 8002 | exp-028-qwen3-14b-thinking |
| cuda:3 | 88279/97887 MiB | 97% | **exp-035** | Qwen2.5-7B-Instruct | FOLIO-204 | 8003 | exp035_run |

**Utilization: 12.5% -> 100%** (1/4 active -> 4/4 active)

### Estimated Completion Times
- exp-033 (Mistral-7B, FOLIO-204): ~2-3h (7B model, faster inference)
- exp-034 (Qwen2.5-14B, ProofWriter-600): ~8-10h (3x problems vs FOLIO-204)
- exp-028 (Qwen3-14B thinking, FOLIO-204): ~24h total (slow thinking mode, 35/204 in ~3h)
- exp-035 (Qwen2.5-7B, FOLIO-204): ~2-3h (7B model)

---

## 6. Model Downloads (Background)

Running in tmux session `model_dl_25068`:
- DeepSeek-R1-Distill-Llama-8B (~16G)
- deepseek-r1-0528-qwen3-8b (~17G)
- gemma-3-27b-it (~50G)
- phi-4-reasoning (~28G)
- Llama-3.1-8B-Instruct (re-download, ~16G)

**Failed**: Llama-4-Scout (requires HuggingFace approval)

---

## 7. Issues Encountered & Resolved

1. **HuggingFace blocked**: Fixed with hf-mirror.com endpoint
2. **Llama-3.1-8B incomplete**: Only 1/4 safetensors shards downloaded; re-downloading via mirror
3. **`python` not in PATH**: submit_training_job's nested bash -c didn't propagate conda env; fixed by using absolute path `/root/miniconda3/bin/python`
4. **Llama-4-Scout access denied**: Requires HuggingFace model approval; skipped

## 8. Next Steps

1. Monitor exp-033, exp-034, exp-035 completion
2. When Llama-3.1-8B download completes, run FOLIO-204 experiment
3. When DeepSeek models complete, add to experiment matrix
4. exp-028 (Qwen3-14B thinking) will take ~24h total; monitor progress
