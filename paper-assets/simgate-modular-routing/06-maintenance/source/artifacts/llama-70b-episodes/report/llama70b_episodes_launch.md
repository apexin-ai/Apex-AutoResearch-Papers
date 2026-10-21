# Llama-3.1-70B Episode Collection Launch Report

## vLLM Server
- Model: `/root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4`
- API model ID: `/root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4`
- Port: 8002
- Quantization: AWQ-INT4 (awq_marlin)
- max_model_len: 4096

## Code Changes
1. **`src/llm_agent.py`**: Added HTTP API mode via `api_base` parameter
   - New `_generate_http()` method using `openai` client
   - Auto-detects model name from `/v1/models` endpoint
   - Backward compatible: without `--api_base`, uses original vLLM Python API or HF transformers
2. **`src/episode_level_collection.py`**: Added `--api_base` argument, passed to `LLMAgent`
   - Skips GPU cleanup when using HTTP API mode

## Test Episode Results (freeze, variation=0)
| Mode | Score | Steps | Time |
|------|-------|-------|------|
| Internal | -100.0 (died) | 17 | 41s |
| Deterministic | 0.0 | 30 | 142s |
| **Total** | | | **183s** |

Label: det-preferred (death_asymmetry)

## Full Collection
- **PID**: 196843
- **Server**: westd-18266
- **Log**: `/tmp/llama70b_episodes.log`
- **Output dir**: `results/llama70b/`
- **Task types** (11): chemistry-mix, find-animal, find-non-living-thing, freeze, grow-fruit, identify-life-stages-1, identify-life-stages-2, inclined-plane-determine-angle, lifespan-longest-lived, lifespan-longest-lived-then-shortest-lived, measure-melting-point-unknown-substance
- **Episodes per task**: 20
- **Total episodes**: 220
- **Seed**: 42
- **Max steps**: 30

## Command
```bash
nohup python src/episode_level_collection.py \
  --task_types "chemistry-mix,find-animal,find-non-living-thing,freeze,grow-fruit,identify-life-stages-1,identify-life-stages-2,inclined-plane-determine-angle,lifespan-longest-lived,lifespan-longest-lived-then-shortest-lived,measure-melting-point-unknown-substance" \
  --episodes 20 \
  --api_base "http://localhost:8002/v1" \
  --output_dir results/llama70b/ \
  --max_steps 30 \
  --seed 42 \
  > /tmp/llama70b_episodes.log 2>&1 &
```

## Estimated Completion
- ~3 min/episode (based on test: 183s)
- 220 episodes × 3 min = ~660 min = ~11 hours
- Expected completion: ~2026-05-25 05:00 UTC
