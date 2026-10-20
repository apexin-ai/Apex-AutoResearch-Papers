Script path: /root/democalib/eval_mistral_bcp.sh
Created: 2026-05-12

Mistral-7B BCP eval script, based on eval_dpo003.sh pattern.
Key differences from Qwen version:
- --tool-call-parser mistral (native Mistral function calling, not hermes)
- SERVED_MODEL_NAME=democalib-mistral
- Model: /root/autodl-tmp/models/Mistral-7B-Instruct-v0.3/
- Default port: 8003 (avoid conflict with running Qwen vLLM)
- No --trust-remote-code (standard HF model)

Usage:
  bash eval_mistral_bcp.sh                    # default: GPU 0, port 8003, 20 tasks, 1 run
  GPU_ID=1 PORT=8004 bash eval_mistral_bcp.sh # custom GPU/port
  NUM_RUNS=3 bash eval_mistral_bcp.sh         # multiple eval rounds
  VARIANTS="aave_target,uncalibrated_baseline" bash eval_mistral_bcp.sh  # specific variants