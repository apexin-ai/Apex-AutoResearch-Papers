# P0 Restart: e2e_llama_gsm8k_n300_clean (seed 123 & 456)

## Environment Verification (2026-04-27)

| Item | Status |
|------|--------|
| Model | `/root/autodl-tmp/models/Llama-3.1-8B-Instruct/` — 30GB, 4 safetensors shards |
| vLLM | 0.19.1 (conda base) |
| GPU cuda:1 | RTX PRO 6000 Blackwell (96GB) — **idle** (0 MiB used) |
| Config | `configs/e2e_llama_gsm8k_n300_clean.yaml` — valid |
| Seed 42 | **Complete** — baseline 81.33%, pruned 82.33%, Δ +1.0pp, suppress 75.53% |
| Seed 123 | **Corrupted** — vLLM crashed mid-run, last ~60 tasks all failed (suppressed=0). Needs full rerun |
| Seed 456 | **Not started** |

## Step 1: Start vLLM on cuda:1

```bash
# Terminal 1 (or nohup)
cd /root/autodl-tmp/comm_gate_mas
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

CUDA_VISIBLE_DEVICES=1 nohup vllm serve /root/autodl-tmp/models/Llama-3.1-8B-Instruct \
  --port 8001 \
  --gpu-memory-utilization 0.90 \
  --tensor-parallel-size 1 \
  > /tmp/vllm_llama_8001.log 2>&1 &

echo "vLLM PID: $!"
```

Wait for readiness (~60s):
```bash
tail -f /tmp/vllm_llama_8001.log  # look for "Uvicorn running on http://0.0.0.0:8001"
# or:
curl -s http://localhost:8001/v1/models | python3 -m json.tool
```

## Step 2: 1-Task Dry Run (heuristic mode)

```bash
cd /root/autodl-tmp/comm_gate_mas
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

python3 src/pruning_validation.py \
  --mode online_pruning \
  --config configs/e2e_llama_gsm8k_n300_clean.yaml \
  --num-tasks 1 \
  --data-seed 42 \
  --char-threshold 30 \
  --output /tmp/dryrun_1task.json

# Verify output
python3 -c "import json; d=json.load(open('/tmp/dryrun_1task.json')); print(f'tasks={d[\"num_tasks\"]}, baseline={d[\"baseline\"]}, pruned={d[\"online_pruned\"]}')"
```

Expected: 1 task completes in ~10-20s, non-zero suppression.

## Step 3: Run Seed 123 (full rerun)

```bash
cd /root/autodl-tmp/comm_gate_mas
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

nohup python3 src/pruning_validation.py \
  --mode online_pruning \
  --config configs/e2e_llama_gsm8k_n300_clean.yaml \
  --num-tasks 300 \
  --data-seed 123 \
  --char-threshold 30 \
  --output outputs/e2e_llama_n300_clean/seed123_heuristic.json \
  > outputs/e2e_llama_n300_clean/seed123.log 2>&1 &

echo "Seed 123 PID: $!"
```

Monitor:
```bash
tail -f outputs/e2e_llama_n300_clean/seed123.log | grep -E "\[online\]|results saved|Error"
```

Estimated runtime: ~50 min (based on seed 42's 4937s).

## Step 4: Run Seed 456

After seed 123 completes (or in parallel if vLLM can handle it — single-GPU should be fine sequentially):

```bash
cd /root/autodl-tmp/comm_gate_mas
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

nohup python3 src/pruning_validation.py \
  --mode online_pruning \
  --config configs/e2e_llama_gsm8k_n300_clean.yaml \
  --num-tasks 300 \
  --data-seed 456 \
  --char-threshold 30 \
  --output outputs/e2e_llama_n300_clean/seed456_heuristic.json \
  > outputs/e2e_llama_n300_clean/seed456.log 2>&1 &

echo "Seed 456 PID: $!"
```

## Step 5: Post-Run Validation

```bash
cd /root/autodl-tmp/comm_gate_mas
python3 -c "
import json
for seed in [42, 123, 456]:
    f = f'outputs/e2e_llama_n300_clean/seed{seed}_heuristic.json'
    try:
        d = json.load(open(f))
        bl = d['baseline']['accuracy']*100
        pr = d['online_pruned']['accuracy']*100
        sp = d['online_pruned']['suppress_pct']
        # Check for corruption: count tasks with suppressed=0
        zero_sup = sum(1 for t in d.get('per_task',[]) if t.get('suppressed',0)==0)
        print(f'seed {seed}: baseline={bl:.1f}% pruned={pr:.1f}% Δ={pr-bl:+.1f}pp suppress={sp:.1f}% zero_suppress_tasks={zero_sup}')
    except FileNotFoundError:
        print(f'seed {seed}: NOT FOUND')
"
```

## Notes

- Config default `seed: 42` in YAML is overridden by `--data-seed` CLI arg
- Previous seed 123 run crashed ~task 240 when vLLM died (Connection refused). Backup old result before rerun if needed: `cp outputs/e2e_llama_n300_clean/seed123_heuristic.json outputs/e2e_llama_n300_clean/seed123_heuristic.json.bak`
- vLLM stability: monitor `/tmp/vllm_llama_8001.log` for OOM or CUDA errors during runs
