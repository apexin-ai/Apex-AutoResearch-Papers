# GPU Release Experiment Queue

> Generated: 2026-05-16 | EMNLP ARR May 25 (T-9)
> Server: cqa1-21977 | 6× RTX 4090D

## Current Running

| GPU | exp_id | Content | ETA |
|-----|--------|---------|-----|
| cuda:0 | exp_001_eval_3B_d100_s123_a32_batch | d100 s123 aligned+para eval | Earliest release |
| cuda:1 | exp_001_eval_3B_d000_s42_a32_batch | d000 s42 aligned+para eval | Hours |
| cuda:2 | exp_001_eval_3B_d005_s42_a32_batch | d005 s42 aligned+para eval | Hours |
| cuda:3 | exp_001_eval_3B_d025_v3_s42_batch | d025 v3 s42 aligned+para eval | Hours |
| cuda:4 | exp_002_signals_3B_v9 | d025_s123 s4 + d100_a32_s123 signals | Hours |
| cuda:5 | exp_002_signals_3B_d025_v3_s42 | d025_v3_s42 s4 signals | Hours |

---

## Queue Item 1: d100_s42 eval batch (aligned + para_aligned)

**Trigger**: cuda:0 releases (first GPU to free)
**exp_id**: `exp_001_eval_3B_d100_s42_a32_v3_batch`
**Priority**: CRITICAL — fills last 2 cells in 3B d100 eval row, prerequisite for d100_s42 signals

### Pre-submit Checks

```bash
# C006: verify alpha=32
cat /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_a32_s42_v3/lora_adapter/adapter_config.json | grep lora_alpha
# Must show: "lora_alpha": 32

# C001+C002: verify cuda:0 is free
nvidia-smi --query-compute-apps=pid,gpu_uuid,used_memory --format=csv,noheader

# Verify checkpoint exists
ls /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_a32_s42_v3/lora_adapter/adapter_model.safetensors
```

### Command

```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && \
CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py \
--model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B \
--adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_a32_s42_v3/lora_adapter \
--output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_a32_s42_v3_aligned \
--benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned \
--cache-dir /root/autodl-tmp/.hf_cache && \
CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py \
--model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B \
--adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_a32_s42_v3/lora_adapter \
--output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_a32_s42_v3_para_aligned \
--benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned \
--paraphrase-dir /root/autodl-tmp/exp001/paraphrases \
--cache-dir /root/autodl-tmp/.hf_cache"
```

**Hypothesis**: 3B d100 s42 alpha=32 eval batch (aligned + para_aligned). Uses D076 v3 checkpoint (lr=5e-5, alpha=32). 100% contamination seed=42. Fills 2 remaining cells in 3B d100 eval row for IRT pooling.

**Registry fields**:
- parent: exp_001_sft_3B_d100_s42_a32_v3
- checkpoint_source: /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_a32_s42_v3/lora_adapter
- eval_data: mmlu gsm8k arc_challenge humaneval (aligned + para_aligned)
- model_name: Qwen2.5-3B
- seed: 42

---

## Queue Item 2: d000_s42 signals (s1+s2+s4)

**Trigger**: cuda:1 releases (d000_s42 eval complete) AND cuda:0 already assigned to d100_s42 eval
**exp_id**: `exp_002_signals_3B_d000_s42`
**Priority**: HIGH — d000 is the reference model for all s42 signals; its own signals feed into IRT pool

### Pre-submit Checks

```bash
# Verify d000_s42 eval results exist
ls /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42_aligned/eval_results.json
ls /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42_para_aligned/eval_results.json

# C006: verify alpha=32
cat /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter/adapter_config.json | grep lora_alpha

# C001+C002: verify GPU free
nvidia-smi --query-compute-apps=pid,gpu_uuid,used_memory --format=csv,noheader
```

### Command

```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
cd /root/contamcal-irt-calibration/exp002 && \
export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && \
export HF_HOME=/root/autodl-tmp/.hf_cache && \
CUDA_VISIBLE_DEVICES=1 && export CUDA_VISIBLE_DEVICES && \
OUTDIR=/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d000_s42 && \
mkdir -p \$OUTDIR && \
for bench in mmlu gsm8k arc_challenge; do \
  echo \"=== \$(date) | d000_s42 / \$bench ===\" && \
  python compute_signals.py \
    --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B \
    --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter \
    --benchmark \$bench --signal all \
    --ref-model-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter \
    --sft-data-dir /root/autodl-tmp/exp001/sft_data \
    --output-dir \$OUTDIR \
    --cache-dir /root/autodl-tmp/.hf_cache && \
  echo \"PASS: \$bench\" || echo \"FAILED: \$bench\"; \
done && echo 'ALL DONE'"
```

**Hypothesis**: 3B d000 s42 signals (s1+s2+s4 × mmlu/gsm8k/arc). Baseline model (0% contamination) signal computation for IRT pool. Ref model = self (d000_s42). Uses D076-retrained checkpoint (lr=5e-5, alpha=32).

**Note**: d000 ref model points to itself since it IS the baseline. s3_constat not needed per D098.

---

## Queue Item 3: d005_s42 signals (s1+s2+s4)

**Trigger**: cuda:2 releases (d005_s42 eval complete)
**exp_id**: `exp_002_signals_3B_d005_s42`
**Priority**: HIGH — fills 3B signals matrix

### Pre-submit Checks

```bash
# Verify d005_s42 eval results exist
ls /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_s42_aligned/eval_results.json
ls /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_s42_para_aligned/eval_results.json

# C006: verify alpha=32
cat /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s42/lora_adapter/adapter_config.json | grep lora_alpha

# C001+C002: verify GPU free
nvidia-smi --query-compute-apps=pid,gpu_uuid,used_memory --format=csv,noheader
```

### Command

```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
cd /root/contamcal-irt-calibration/exp002 && \
export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && \
export HF_HOME=/root/autodl-tmp/.hf_cache && \
CUDA_VISIBLE_DEVICES=2 && export CUDA_VISIBLE_DEVICES && \
OUTDIR=/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d005_s42 && \
mkdir -p \$OUTDIR && \
for bench in mmlu gsm8k arc_challenge; do \
  echo \"=== \$(date) | d005_s42 / \$bench ===\" && \
  python compute_signals.py \
    --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B \
    --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s42/lora_adapter \
    --benchmark \$bench --signal all \
    --ref-model-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter \
    --sft-data-dir /root/autodl-tmp/exp001/sft_data \
    --output-dir \$OUTDIR \
    --cache-dir /root/autodl-tmp/.hf_cache && \
  echo \"PASS: \$bench\" || echo \"FAILED: \$bench\"; \
done && echo 'ALL DONE'"
```

**Hypothesis**: 3B d005 s42 signals (s1+s2+s4 × mmlu/gsm8k/arc). 5% contamination seed=42. Ref model = d000_s42 (0% baseline). D076-retrained checkpoint (lr=5e-5, alpha=32).

**Dependency**: d000_s42 eval must be complete (ref model eval results needed for s3, though D098 dropped s3 from paper).

---

## Queue Item 4: d025_s42 signals (remaining signals)

**Trigger**: cuda:3 releases (d025_v3_s42 eval complete) OR cuda:5 releases
**exp_id**: `exp_002_signals_3B_d025_v3_s42_remaining`
**Priority**: HIGH

**Note**: s1/s2 already cached, s4 running on cuda:5. After cuda:5 completes, d025_v3_s42 may be fully done (s1+s2+s4). Verify before submitting. If signals already complete, use this GPU for d100_s42 signals or 0.5B s123 rerun instead.

### Pre-submit Checks

```bash
# Check which signals already exist
ls /root/autodl-tmp/exp002/signals/Qwen2.5-3B_d025_v3_s42/

# Verify eval results exist
ls /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_v3_s42_aligned/eval_results.json
ls /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_v3_s42_para_aligned/eval_results.json

# C006: verify alpha=32
cat /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_v3_s42/lora_adapter/adapter_config.json | grep lora_alpha
```

### Command (only if signals incomplete after cuda:5 finishes)

```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
cd /root/contamcal-irt-calibration/exp002 && \
export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && \
export HF_HOME=/root/autodl-tmp/.hf_cache && \
CUDA_VISIBLE_DEVICES=3 && export CUDA_VISIBLE_DEVICES && \
OUTDIR=/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d025_v3_s42 && \
mkdir -p \$OUTDIR && \
for bench in mmlu gsm8k arc_challenge; do \
  echo \"=== \$(date) | d025_v3_s42 / \$bench ===\" && \
  python compute_signals.py \
    --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B \
    --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_v3_s42/lora_adapter \
    --benchmark \$bench --signal all \
    --ref-model-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter \
    --sft-data-dir /root/autodl-tmp/exp001/sft_data \
    --output-dir \$OUTDIR \
    --cache-dir /root/autodl-tmp/.hf_cache && \
  echo \"PASS: \$bench\" || echo \"FAILED: \$bench\"; \
done && echo 'ALL DONE'"
```

**Hypothesis**: 3B d025 v3 s42 remaining signals. 25% contamination seed=42. Ref model = d000_s42. Alpha=32 checkpoint.

---

## Queue Item 5: d100_s42 signals (s1+s2+s4)

**Trigger**: Any GPU releases AFTER d100_s42 eval (Queue Item 1) completes
**exp_id**: `exp_002_signals_3B_d100_s42`
**Priority**: HIGH — completes the 3B s42 signals matrix

### Pre-submit Checks

```bash
# Verify d100_s42 eval results exist (from Queue Item 1)
ls /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_a32_s42_v3_aligned/eval_results.json
ls /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_a32_s42_v3_para_aligned/eval_results.json

# C006: verify alpha=32
cat /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_a32_s42_v3/lora_adapter/adapter_config.json | grep lora_alpha

# C001+C002: verify GPU free
nvidia-smi --query-compute-apps=pid,gpu_uuid,used_memory --format=csv,noheader
```

### Command (replace N with actual GPU id)

```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
cd /root/contamcal-irt-calibration/exp002 && \
export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && \
export HF_HOME=/root/autodl-tmp/.hf_cache && \
CUDA_VISIBLE_DEVICES=N && export CUDA_VISIBLE_DEVICES && \
OUTDIR=/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d100_a32_s42_v3 && \
mkdir -p \$OUTDIR && \
for bench in mmlu gsm8k arc_challenge; do \
  echo \"=== \$(date) | d100_a32_s42_v3 / \$bench ===\" && \
  python compute_signals.py \
    --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B \
    --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_a32_s42_v3/lora_adapter \
    --benchmark \$bench --signal all \
    --ref-model-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter \
    --sft-data-dir /root/autodl-tmp/exp001/sft_data \
    --output-dir \$OUTDIR \
    --cache-dir /root/autodl-tmp/.hf_cache && \
  echo \"PASS: \$bench\" || echo \"FAILED: \$bench\"; \
done && echo 'ALL DONE'"
```

**Hypothesis**: 3B d100 s42 signals (s1+s2+s4 × mmlu/gsm8k/arc). 100% contamination seed=42. Ref model = d000_s42. Alpha=32 v3 checkpoint (D076 retrained, lr=5e-5).

**Dependency**: Queue Item 1 (d100_s42 eval) must be DONE first.

---

## Queue Item 6: d100_s123 QUEUED signals recovery

**Trigger**: cuda:4 releases (v9 completes or fails)
**exp_id**: `exp_002_signals_3B_d100_s123_v10`
**Priority**: MEDIUM — only if v9 left gaps

### Pre-submit Checks

```bash
# Check what v9 completed
ls /root/autodl-tmp/exp002/signals/Qwen2.5-3B_d100_a32_s123/
ls /root/autodl-tmp/exp002/signals/Qwen2.5-3B_d100_a32_s123/signals_merged_*.json

# Check what's missing (need merged files for mmlu, gsm8k, arc_challenge)
for bench in mmlu gsm8k arc_challenge; do
  echo "$bench: $(ls /root/autodl-tmp/exp002/signals/Qwen2.5-3B_d100_a32_s123/signals_merged_${bench}.json 2>/dev/null && echo OK || echo MISSING)"
done
```

### Command (only submit for MISSING benchmarks, replace BENCH_LIST accordingly)

```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
cd /root/contamcal-irt-calibration/exp002 && \
export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && \
export HF_HOME=/root/autodl-tmp/.hf_cache && \
CUDA_VISIBLE_DEVICES=4 && export CUDA_VISIBLE_DEVICES && \
OUTDIR=/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d100_a32_s123 && \
mkdir -p \$OUTDIR && \
for bench in BENCH_LIST; do \
  echo \"=== \$(date) | d100_a32_s123 / \$bench ===\" && \
  python compute_signals.py \
    --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B \
    --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_a32_s123/lora_adapter \
    --benchmark \$bench --signal all \
    --ref-model-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s123/lora_adapter \
    --sft-data-dir /root/autodl-tmp/exp001/sft_data \
    --output-dir \$OUTDIR \
    --cache-dir /root/autodl-tmp/.hf_cache && \
  echo \"PASS: \$bench\" || echo \"FAILED: \$bench\"; \
done && echo 'ALL DONE'"
```

**Hypothesis**: Recovery for d100_a32_s123 remaining signals. Fills gaps left by v8 OOM + v9 partial completion.

---

## Queue Item 7: 0.5B s123 signals rerun

**Trigger**: Any GPU releases with no higher-priority 3B task pending
**exp_id**: `exp_002_signals_05B_s123_v2`
**Priority**: LOW — 0.5B runs fast (~12 min total), can slot into any gap

### Root Cause of v1 Failure
EXIT_CODE=127: script `run_05B_s123_signals.sh` did not exist on server. Only `run_signals_05B.sh` exists. Fix: use inline command.

### Pre-submit Checks

```bash
# Verify 0.5B s123 checkpoints exist (all 4 dosages)
for d in d000_s123 d005_s123 d025_s123 d100_s123; do
  echo "$d: $(ls /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_${d}/lora_adapter/adapter_model.safetensors 2>/dev/null && echo OK || echo MISSING)"
done

# C001+C002: verify GPU free
nvidia-smi --query-compute-apps=pid,gpu_uuid,used_memory --format=csv,noheader
```

### Command (replace N with actual GPU id)

```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
cd /root/contamcal-irt-calibration/exp002 && \
export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && \
export HF_HOME=/root/autodl-tmp/.hf_cache && \
CUDA_VISIBLE_DEVICES=N && export CUDA_VISIBLE_DEVICES && \
for dose in d000 d005 d025 d100; do \
  ADAPTER=/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_\${dose}_s123/lora_adapter && \
  OUTDIR=/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_\${dose}_s123 && \
  mkdir -p \$OUTDIR && \
  for bench in mmlu gsm8k arc_challenge; do \
    echo \"=== \$(date) | 0.5B \${dose}_s123 / \$bench ===\" && \
    python compute_signals.py \
      --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B \
      --adapter-path \$ADAPTER \
      --benchmark \$bench --signal all \
      --ref-model-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s123/lora_adapter \
      --sft-data-dir /root/autodl-tmp/exp001/sft_data \
      --output-dir \$OUTDIR \
      --cache-dir /root/autodl-tmp/.hf_cache && \
    echo \"PASS: \${dose}_s123/\$bench\" || echo \"FAILED: \${dose}_s123/\$bench\"; \
  done; \
done && echo 'ALL 0.5B s123 DONE'"
```

**Hypothesis**: 0.5B s123 signal batch rerun (s1+s2+s4 × 4 dosages × 3 benchmarks). Fixes v1 EXIT_CODE=127 (missing script). Inline command replaces non-existent run_05B_s123_signals.sh. Adds +4 respondents to signal-backed IRT pool.

---

## Decision Matrix: Which GPU Gets What

| Release Order | GPU | Next Task | exp_id |
|---------------|-----|-----------|--------|
| 1st (likely cuda:0) | cuda:0 | **d100_s42 eval batch** | exp_001_eval_3B_d100_s42_a32_v3_batch |
| 2nd (cuda:1/2/3) | first free | **signals for that GPU's just-completed eval** | exp_002_signals_3B_{dose}_s42 |
| 3rd | next free | **signals for another completed eval** | exp_002_signals_3B_{dose}_s42 |
| cuda:4 release | cuda:4 | **d100_s123 signals recovery** (if v9 left gaps) | exp_002_signals_3B_d100_s123_v10 |
| cuda:5 release | cuda:5 | **0.5B s123 signals** (fast, ~12 min) | exp_002_signals_05B_s123_v2 |
| Any gap after 3B done | any | **0.5B s123 signals** if not yet done | exp_002_signals_05B_s123_v2 |

## Fallback: If cuda:0 doesn't release first

If another GPU releases before cuda:0, d100_s42 eval takes priority on whichever GPU frees first:
- Adjust CUDA_VISIBLE_DEVICES=N in Queue Item 1 command accordingly
- Defer the signals task for that GPU's completed eval to the next available GPU

## Constraints Checklist (every submission)

- [ ] C001: `nvidia-smi` — no duplicate process on target GPU
- [ ] C002: `nvidia-smi` — target GPU idle (not just resource_usage tool)
- [ ] C004: `CUDA_VISIBLE_DEVICES=N` explicit in command
- [ ] C006: `cat adapter_config.json | grep lora_alpha` → must be 32
- [ ] D076: checkpoint is lr=5e-5 (not lr=2e-4 confounded)
- [ ] ROADMAP: `HF_DATASETS_OFFLINE=1 TRANSFORMERS_OFFLINE=1` in all new commands

## IRT Pool Impact

After full queue completion: 3B matrix 7/16 → 16/16, total IRT pool N=35 → N=51 (with 0.5B s123 signals).
