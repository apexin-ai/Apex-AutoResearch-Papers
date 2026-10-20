# ssh seed123 main experiment

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_seed123-main-experiment_20260518T075645_result.json`
- **Structured JSON:** [`a4209d466ac4dc57fd62.json`](../../sessions/a4/a4209d466ac4dc57fd62.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Total on westb-13313: 275 episodes (some tasks have extras from later collection rounds). The original standard was 20 eps/task. For seed=123 replication, I'll use 20 eps/task × 11 tasks = 220 episodes, matching the core experimental design.

Here's the summary:

## Plan-012-full experiment setup

**Script**: `src/episode_level_collection.py`

**11 tasks** (from TASKS list in reflexion_baseline.py, confirmed by plan_c directory):
```
chemistry-mix, find-animal, find-non-living-thing, freeze,
grow-fruit, identify-life-stages-1, identify-life-stages-2,
inclined-plane-determine-angle, lifespan-longest-lived,
lifespan-longest-lived-then-shortest-lived, measure-melting-point-unknown-substance
```

**Parameters**: `--episodes 20 --max_steps 30 --n_candidates 3 --seed 42` (original)

**Each episode**: runs both always-internal and always-deterministic modalities, compares final scores, labels modality preference.

## Dry-run result (seed=123)
- Task: chemistry-mix, episode 0, variation 0
- Internal: -100.0 (death, 18 steps, 46s)
- Deterministic: -100.0 (death, 22 steps, 89s)
- Label: no-preference (both_dead)
- Time per episode: ~2.25 min

## Full run commands (4 GPUs in parallel)

```bash
cd /root/autodl-tmp/simgate-modular-routing

# GPU 0: 3 tasks
nohup bash -c 'CUDA_VISIBLE_DEVICES=0 VLLM_USE_FLASHINFER_SAMPLER=0 /root/miniconda3/bin/python src/episode_level_collection.py \
  --task_types "chemistry-mix,find-animal,find-non-living-thing" \
  --episodes 20 --seed 123 --gpu_id 0 --max_steps 30 --n_candidates 3 \
  --output_dir results/seed123-plan-c/' > logs/seed123-gpu0.log 2>&1 &

# GPU 1: 3 tasks
nohup bash -c 'CUDA_VISIBLE_DEVICES=1 VLLM_USE_FLASHINFER_SAMPLER=0 /root/miniconda3/bin/python src/episode_level_collection.py \
  --task_types "freeze,grow-fruit,identify-life-stages-1" \
  --episodes 20 --seed 123 --gpu_id 0 --max_steps 30 --n_candidates 3 \
  --output_dir results/seed123-plan-c/' > logs/seed123-gpu1.log 2>&1 &

# GPU 2: 3 tasks
nohup bash -c 'CUDA_VISIBLE_DEVICES=2 VLLM_USE_FLASHINFER_SAMPLER=0 /root/miniconda3/bin/python src/episode_level_collection.py \
  --task_types "identify-life-stages-2,inclined-plane-determine-angle,lifespan-longest-lived" \
  --episodes 20 --seed 123 --gpu_id 0 --max_steps 30 --n_candidates 3 \
  --output_dir results/seed123-plan-c/' > logs/seed123-gpu2.log 2>&1 &

# GPU 3: 2 tasks
nohup bash -c 'CUDA_VISIBLE_DEVICES=3 VLLM_USE_FLASHINFER_SAMPLER=0 /root/miniconda3/bin/python src/episode_level_collection.py \
  --task_types "lifespan-longest-lived-then-shortest-lived,measure-melting-point-unknown-substance" \
  --episodes 20 --seed 123 --gpu_id 0 --max_steps 30 --n_candidates 3 \
  --output_dir results/seed123-plan-c/' > logs/seed123-gpu3.log 2>&1 &
```

Note: `--gpu_id 0` in each command because `CUDA_VISIBLE_DEVICES` remaps the physical GPU to `cuda:0` within each process.

## Estimated runtime
- ~2.25 min/episode × 60 episodes (max per GPU group) = ~135 min
- Plus vLLM loading + JVM overhead: **~2.5-3 hours wall-clock**
- Output: `results/seed123-plan-c/` (220 episodes total, 20 per task)

---
