# Memory

## Llama-70B Cross-Model-at-Scale Results (2026-05-24)
- DAF = 101.0% [95.3%, 107.5%] — highest across all tested models
- DAF > 100% because Δ_nd = −0.30 (internal agent slightly better when both survive)
- Int DR = 48.6%, Det DR = 20.0%, Δ_DR = +28.6pp
- Labels: 67 det / 2 int / 151 no-pref, label fraction = 91.3%
- Int-preferred only in find-non-living-thing (zero-death task)
- Cross-model DAF ranking: Llama-70B (101%) > Qwen-72B (92.4%) > Qwen-7B (90.4%) > Gemma-9B (89.7%) > Llama-8B (88.2%)
- Death dominance intensifies with scale, not diminishes

## vLLM HTTP API mode (2026-05-24)
- Added `--api_base` param to `llm_agent.py` and `episode_level_collection.py`
- Uses openai client library against OpenAI-compatible vLLM endpoint
- Backward compatible: without `--api_base`, uses original vLLM Python API
- Tested working on port 8002 with AWQ-INT4 quantized model

## Verified Model IDs
- Llama-3.1-70B-Instruct-AWQ: ModelScope `LLM-Research/Meta-Llama-3___1-70B-Instruct-AWQ-INT4`, 38GB, 9 safetensors shards
- vLLM flags for AWQ on RTX PRO 6000: `--quantization awq_marlin --enforce-eager --gpu-memory-utilization 0.85 --max-model-len 4096`

## Paper Figure 1 (2026-05-24)
- Regenerated with PaperBanana (Gemini 2.5 Pro VLM), raster PDF 300 DPI
- Key: subscript notation (s_int, d_int) not superscript; red for deterministic, blue for internal, green for analysis
- Old vector PDF backed up as pipeline_overview_old.pdf
