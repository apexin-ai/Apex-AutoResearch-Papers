# v4 Data Conversion Script

## Location
Server: bjb1-17606
Script: /root/autodl-tmp/expert_sft_v4/convert_sft_to_ragen_format.py

## Input
- /root/autodl-tmp/expert_sft_v3/expert_sft_train.jsonl (2546 samples)
- /root/autodl-tmp/expert_sft_v3/expert_sft_val.jsonl (133 samples)

## Output
- /root/autodl-tmp/expert_sft_v4/expert_sft_train.jsonl (2546 samples, 3-40 turns)
- /root/autodl-tmp/expert_sft_v4/expert_sft_val.jsonl (133 samples, 3-40 turns)

## Key Format Changes (v3 → v4)

### System Prompt
v3: "You're a helpful assistant. You are an expert agent... present it within <answer>...</answer> tags."
v4: "You're a helpful assistant. " + exact AlfworldSG env_instruction from envs.yaml
    (includes "Do NOT wrap the action in any tags" + example)

### User Messages
v3: Raw env observation + "Admissible actions: [...]"
v4: "\nTurn {N}:\nState:\n{obs}\nYou have {actions_left} actions left. Always output: <think>...</think> <answer>...</answer> with no extra text. Strictly follow this format. Max response length: 512 words (tokens).\n"

### Reward (Turn 2+)
v3: none
v4: "Reward:\n0.0\n" prepended to user message

### Assistant Response
v3 == v4: "<think>...</think><answer>action</answer>" (unchanged)
