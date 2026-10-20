# ops gpu audit

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 31
- **Recorded user turns:** 0
- **Tool calls:** 15
- **Original source:** `logs/chats/worker_ops_gpu-audit_20260514T003001.jsonl`
- **Structured JSON:** [`b408bc44ea47fec4a5fe.json`](../../sessions/b4/b408bc44ea47fec4a5fe.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

31 recorded events

### Tool call

_source line 1 · 2026-05-14T00:32:10.811103+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:ssh_read_only,ssh_execute",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_gpu-audit_20260514T003001",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:ssh_read_only,ssh_execute",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-14T00:32:10.811743+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_gpu-audit_20260514T003001",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T00:32:10.812075+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "ssh",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_gpu-audit_20260514T003001",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "ssh",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-14T00:32:10.817379+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_gpu-audit_20260514T003001",
  "tool": "ToolSearch",
  "elapsed_ms": 5
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T00:32:10.817859+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "nvidia-smi --query-gpu=index,name,memory.used,memory.total,utilization.gpu --format=csv,noheader"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_gpu-audit_20260514T003001",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "nvidia-smi --query-gpu=index,name,memory.used,memory.total,utilization.gpu --format=csv,noheader"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-14T00:32:10.818114+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ps -p 235243,229370,229516,242581,243290,239729 -o pid,cmd --no-headers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_gpu-audit_20260514T003001",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ps -p 235243,229370,229516,242581,243290,239729 -o pid,cmd --no-headers"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-14T00:32:10.818355+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"0, NVIDIA GeForce RTX 4090 D, 22001 MiB, 24564 MiB, 94 %\\n1, NVIDIA GeForce RTX 4090 D, 3667 MiB, 24564 MiB, 33 %\\n2, NVIDIA GeForce RTX 4090 D, 3667 MiB, 24564 MiB, 33 %\\n3, NVIDIA GeForce RTX 4090 D, 8957 MiB, 24564 MiB, 65 %\\n4, NVIDIA GeForce RTX 4090 D, 5829 MiB, 24564 MiB, 50 %\\n5, NVIDIA GeForce RTX 4090 D, 22007 MiB, 24564 MiB, 49 %\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.2}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_gpu-audit_20260514T003001",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T00:32:10.818647+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"229370 bash -c rm -f /tmp/agent-ml-exit/exp_001_eval_05B_d000_s42.exit; mkdir -p /tmp/agent-ml-exit; trap '_EC=$?; echo \\\"EXIT_CODE=$_EC\\\" >> ~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s42.log; printf \\\"%s|%s\\\\n\\\" \\\"$_EC\\\" \\\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\\\" > /tmp/agent-ml-exit/exp_001_eval_05B_d000_s42.exit' EXIT; trap 'exit 129' HUP; trap 'exit 130' INT; trap 'exit 143' TERM; { cd /root/contamcal-irt-calibration && export CUDA_VISIBLE_DEVICES=1 && timeout 86400 env bash -c 'bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export CUDA_VISIBLE_DEVICES=1 && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\\\"'; } > ~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s42.log 2>&1\\n229516 bash -c rm -f /tmp/agent-ml-exit/exp_001_eval_05B_d000_s123.exit; mkdir -p /tmp/agent-ml-exit; trap '_EC=$?; echo \\\"EXIT_CODE=$_EC\\\" >> ~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s123.log; printf \\\"%s|%s\\\\n\\\" \\\"$_EC\\\" \\\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\\\" > /tmp/agent-ml-exit/exp_001_eval_05B_d000_s123.exit' EXIT; trap 'exit 129' HUP; trap 'exit 130' INT; trap 'exit 143' TERM; { cd /root/contamcal-irt-calibration && export CUDA_VISIBLE_DEVICES=2 && timeout 86400 env bash -c 'bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export CUDA_VISIBLE_DEVICES=2 && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B
…[truncated 5081 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_gpu-audit_20260514T003001",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T00:32:10.818890+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls -la /root/autodl-tmp/exp001/paraphrase_data/mmlu_paraphrases*.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_gpu-audit_20260514T003001",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls -la /root/autodl-tmp/exp001/paraphrase_data/mmlu_paraphrases*.json"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T00:32:10.819103+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/autodl-tmp/exp001/paraphrase_data/mmlu_paraphrases*.json': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_gpu-audit_20260514T003001",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T00:32:10.825489+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "tail -30 ~/runs/contamcal-irt-calibration/exp_001_sft_0pct_3B_s123.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_gpu-audit_20260514T003001",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "tail -30 ~/runs/contamcal-irt-calibration/exp_001_sft_0pct_3B_s123.log"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T00:32:10.826040+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{'loss': 1.2191, 'grad_norm': 0.26942577958106995, 'learning_rate': 4.237103734153181e-06, 'entropy': 1.166537443175912, 'num_tokens': 17815718.0, 'mean_token_accuracy': 0.731221759878099, 'epoch': 0.91}\\n{'loss': 1.1281, 'grad_norm': 0.2068016082048416, 'learning_rate': 3.937624339655599e-06, 'entropy': 1.1178256466984748, 'num_tokens': 17882619.0, 'mean_token_accuracy': 0.7426986705511809, 'epoch': 0.92}\\n{'loss': 1.0413, 'grad_norm': 0.2450195550918579, 'learning_rate': 3.6489076447894454e-06, 'entropy': 1.0741302599199116, 'num_tokens': 17942024.0, 'mean_token_accuracy': 0.756363551132381, 'epoch': 0.92}\\n{'loss': 1.1243, 'grad_norm': 0.28556323051452637, 'learning_rate': 3.370985996985709e-06, 'entropy': 1.120455353334546, 'num_tokens': 18001427.0, 'mean_token_accuracy': 0.7457241632044316, 'epoch': 0.92}\\n{'loss': 1.1225, 'grad_norm': 0.23643116652965546, 'learning_rate': 3.1038905342127834e-06, 'entropy': 1.1353684994392097, 'num_tokens': 18065580.0, 'mean_token_accuracy': 0.7382063690572978, 'epoch': 0.92}\\n{'loss': 1.1136, 'grad_norm': 0.29066428542137146, 'learning_rate': 2.847651181487776e-06, 'entropy': 1.103092235326767, 'num_tokens': 18136214.0, 'mean_token_accuracy': 0.746714111045003, 'epoch': 0.93}\\n{'loss': 1.1252, 'grad_norm': 0.22619670629501343, 'learning_rate': 2.602296647523861e-06, 'entropy': 1.084000884462148, 'num_tokens': 18195582.0, 'mean_token_accuracy': 0.7567633707076311, 'epoch': 0.93}\\n{'loss': 1.1288, 'grad_norm': 0.3181723952293396, 'learning_rate': 2.3678544215136933e-06, 'entropy': 1.1520031840540468, 'num_tokens': 18254977.0, 'mean_token_accuracy': 0.7455581227317453, 'epoch': 0.93}\\n{'loss': 1.182, 'grad_norm': 0.3397308886051178, 'learning_rate': 2.144350770049597e-06, 'entropy': 1.1467774887569249, 'num_tokens': 18324624.0, 'mean_token_accuracy': 0.7379490282386542, 'epoch': 0.94}\\n{'loss': 1.0766, 'grad_norm': 0.23039105534553528, 'learning_rate': 1.93181073418
…[truncated 4219 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_gpu-audit_20260514T003001",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T00:32:10.826382+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "tail -20 ~/runs/contamcal-irt-calibration/exp_001_sft_0pct_15B_s123.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_gpu-audit_20260514T003001",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "tail -20 ~/runs/contamcal-irt-calibration/exp_001_sft_0pct_15B_s123.log"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T00:32:10.826666+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{'loss': 1.2364, 'grad_norm': 0.257655531167984, 'learning_rate': 1.7302581266073537e-06, 'entropy': 1.2159541685134172, 'num_tokens': 18457365.0, 'mean_token_accuracy': 0.7279102258384228, 'epoch': 0.94}\\n{'loss': 1.3026, 'grad_norm': 0.31657418608665466, 'learning_rate': 1.5397155290131527e-06, 'entropy': 1.2563578028231859, 'num_tokens': 18522121.0, 'mean_token_accuracy': 0.7189210459589959, 'epoch': 0.95}\\n{'loss': 1.2463, 'grad_norm': 0.43379494547843933, 'learning_rate': 1.3602042895349942e-06, 'entropy': 1.2174575172364712, 'num_tokens': 18585411.0, 'mean_token_accuracy': 0.7303243584930896, 'epoch': 0.95}\\n{'loss': 1.2792, 'grad_norm': 0.2685953378677368, 'learning_rate': 1.1917445203712186e-06, 'entropy': 1.2395696263760327, 'num_tokens': 18647994.0, 'mean_token_accuracy': 0.7225633896887302, 'epoch': 0.95}\\n{'loss': 1.1882, 'grad_norm': 0.23319649696350098, 'learning_rate': 1.0343550955282278e-06, 'entropy': 1.1767932873219251, 'num_tokens': 18710798.0, 'mean_token_accuracy': 0.7338462851941585, 'epoch': 0.96}\\n{'loss': 1.2559, 'grad_norm': 0.33220043778419495, 'learning_rate': 8.880536487059333e-07, 'entropy': 1.2135941922664641, 'num_tokens': 18768955.0, 'mean_token_accuracy': 0.7329148951917887, 'epoch': 0.96}\\n{'loss': 1.3761, 'grad_norm': 0.2262774556875229, 'learning_rate': 7.528565713220803e-07, 'entropy': 1.3072730518877507, 'num_tokens': 18827549.0, 'mean_token_accuracy': 0.7062506008893251, 'epoch': 0.96}\\n{'loss': 1.2853, 'grad_norm': 0.27777382731437683, 'learning_rate': 6.287790106757396e-07, 'entropy': 1.2465534403920173, 'num_tokens': 18888221.0, 'mean_token_accuracy': 0.7208089083433151, 'epoch': 0.97}\\n{'loss': 1.2811, 'grad_norm': 0.2389131784439087, 'learning_rate': 5.158348682502756e-07, 'entropy': 1.25574054941535, 'num_tokens': 18950753.0, 'mean_token_accuracy': 0.713102338463068, 'epoch': 0.97}\\n{'loss': 1.2531, 'grad_norm': 0.27571016550064087, 'learning_rate': 4.14036
…[truncated 2152 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_gpu-audit_20260514T003001",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T00:32:10.826905+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "tail -20 ~/runs/contamcal-irt-calibration/exp_001_sft_0pct_05B_s123.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_gpu-audit_20260514T003001",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "tail -20 ~/runs/contamcal-irt-calibration/exp_001_sft_0pct_05B_s123.log"
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-14T00:32:10.827103+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "tail -30 ~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s42.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_gpu-audit_20260514T003001",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "tail -30 ~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s42.log"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-14T00:32:10.833542+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{'loss': 1.5222, 'grad_norm': 0.4050080180168152, 'learning_rate': 1.7302581266073537e-06, 'entropy': 1.5400590643286705, 'num_tokens': 18457365.0, 'mean_token_accuracy': 0.6760307148098945, 'epoch': 0.94}\\n{'loss': 1.5848, 'grad_norm': 0.40386763215065, 'learning_rate': 1.5397155290131527e-06, 'entropy': 1.5816914483904838, 'num_tokens': 18522121.0, 'mean_token_accuracy': 0.6632868751883507, 'epoch': 0.95}\\n{'loss': 1.5252, 'grad_norm': 0.475202739238739, 'learning_rate': 1.3602042895349942e-06, 'entropy': 1.5040147572755813, 'num_tokens': 18585411.0, 'mean_token_accuracy': 0.6831495314836502, 'epoch': 0.95}\\n{'loss': 1.5493, 'grad_norm': 0.42910683155059814, 'learning_rate': 1.1917445203712186e-06, 'entropy': 1.5425040036439897, 'num_tokens': 18647994.0, 'mean_token_accuracy': 0.6715734839439392, 'epoch': 0.95}\\n{'loss': 1.4443, 'grad_norm': 0.3826116621494293, 'learning_rate': 1.0343550955282278e-06, 'entropy': 1.48063263297081, 'num_tokens': 18710798.0, 'mean_token_accuracy': 0.6836157351732254, 'epoch': 0.96}\\n{'loss': 1.5343, 'grad_norm': 0.466613233089447, 'learning_rate': 8.880536487059333e-07, 'entropy': 1.5162551239132882, 'num_tokens': 18768955.0, 'mean_token_accuracy': 0.6817469768226146, 'epoch': 0.96}\\n{'loss': 1.6173, 'grad_norm': 0.37260207533836365, 'learning_rate': 7.528565713220803e-07, 'entropy': 1.5945573657751084, 'num_tokens': 18827549.0, 'mean_token_accuracy': 0.6588420175015927, 'epoch': 0.96}\\n{'loss': 1.6008, 'grad_norm': 0.38173696398735046, 'learning_rate': 6.287790106757396e-07, 'entropy': 1.6044997870922089, 'num_tokens': 18888221.0, 'mean_token_accuracy': 0.6598991543054581, 'epoch': 0.97}\\n{'loss': 1.5383, 'grad_norm': 0.44964784383773804, 'learning_rate': 5.158348682502756e-07, 'entropy': 1.5355969429016114, 'num_tokens': 18950753.0, 'mean_token_accuracy': 0.6706881761550904, 'epoch': 0.97}\\n{'loss': 1.53, 'grad_norm': 0.44137516617774963, 'learning_rate': 4.1403679815
…[truncated 2151 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_gpu-audit_20260514T003001",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 6
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-14T00:32:10.834064+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "tail -30 ~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s123.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_gpu-audit_20260514T003001",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "tail -30 ~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s123.log"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-14T00:32:10.834498+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-14 06:59:08,129 [WARNING] Retrying in 8s [Retry 5/5].\\n'(MaxRetryError(\\\"HTTPSConnectionPool(host='huggingface.co', port=443): Max retries exceeded with url: /datasets/openai/gsm8k/resolve/main/README.md (Caused by ConnectTimeoutError(&lt;urllib3.connection.HTTPSConnection object at 0x7fd5db71b440>, 'Connection to huggingface.co timed out. (connect timeout=10)'))\\\"), '(Request ID: 4ddc6945-2840-4750-a4d2-6422d5661697)')' thrown while requesting HEAD https://huggingface.co/datasets/openai/gsm8k/resolve/main/README.md\\n2026-05-14 06:59:26,145 [WARNING] '(MaxRetryError(\\\"HTTPSConnectionPool(host='huggingface.co', port=443): Max retries exceeded with url: /datasets/openai/gsm8k/resolve/main/README.md (Caused by ConnectTimeoutError(&lt;urllib3.connection.HTTPSConnection object at 0x7fd5db71b440>, 'Connection to huggingface.co timed out. (connect timeout=10)'))\\\"), '(Request ID: 4ddc6945-2840-4750-a4d2-6422d5661697)')' thrown while requesting HEAD https://huggingface.co/datasets/openai/gsm8k/resolve/main/README.md\\n'(MaxRetryError(\\\"HTTPSConnectionPool(host='huggingface.co', port=443): Max retries exceeded with url: /datasets/openai/gsm8k/resolve/740312add88f781978c0658806c59bc2815b9866/gsm8k.py (Caused by ConnectTimeoutError(&lt;urllib3.connection.HTTPSConnection object at 0x7fd5db8c1eb0>, 'Connection to huggingface.co timed out. (connect timeout=10)'))\\\"), '(Request ID: d7c254a9-7158-407b-984e-11518e5a5e67)')' thrown while requesting HEAD https://huggingface.co/datasets/openai/gsm8k/resolve/740312add88f781978c0658806c59bc2815b9866/gsm8k.py\\n2026-05-14 06:59:36,160 [WARNING] '(MaxRetryError(\\\"HTTPSConnectionPool(host='huggingface.co', port=443): Max retries exceeded with url: /datasets/openai/gsm8k/resolve/740312add88f781978c0658806c59bc2815b9866/gsm8k.py (Caused by ConnectTimeoutError(&lt;urllib3.connection.HTTPSConnection object at 0x7fd5db8c1eb0>, 'Connection to huggingface.co timed out. (connect ti
…[truncated 6382 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_gpu-audit_20260514T003001",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 7
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-14T00:32:10.834759+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "tail -30 ~/runs/contamcal-irt-calibration/exp_001_eval_3B_d000_s123.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_gpu-audit_20260514T003001",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "tail -30 ~/runs/contamcal-irt-calibration/exp_001_eval_3B_d000_s123.log"
  }
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-14T00:32:10.834968+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "tail -30 ~/runs/contamcal-irt-calibration/exp_001_eval_15B_d000_s42_v2.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_gpu-audit_20260514T003001",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "tail -30 ~/runs/contamcal-irt-calibration/exp_001_eval_15B_d000_s42_v2.log"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-14T00:32:10.835293+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-14 06:59:29,676 [WARNING] Retrying in 8s [Retry 5/5].\\n'(MaxRetryError(\\\"HTTPSConnectionPool(host='huggingface.co', port=443): Max retries exceeded with url: /datasets/openai/gsm8k/resolve/main/README.md (Caused by ConnectTimeoutError(&lt;urllib3.connection.HTTPSConnection object at 0x7fa175b66180>, 'Connection to huggingface.co timed out. (connect timeout=10)'))\\\"), '(Request ID: 71db5bd8-0cbd-4af2-874f-6732952028be)')' thrown while requesting HEAD https://huggingface.co/datasets/openai/gsm8k/resolve/main/README.md\\n2026-05-14 06:59:47,692 [WARNING] '(MaxRetryError(\\\"HTTPSConnectionPool(host='huggingface.co', port=443): Max retries exceeded with url: /datasets/openai/gsm8k/resolve/main/README.md (Caused by ConnectTimeoutError(&lt;urllib3.connection.HTTPSConnection object at 0x7fa175b66180>, 'Connection to huggingface.co timed out. (connect timeout=10)'))\\\"), '(Request ID: 71db5bd8-0cbd-4af2-874f-6732952028be)')' thrown while requesting HEAD https://huggingface.co/datasets/openai/gsm8k/resolve/main/README.md\\n'(MaxRetryError(\\\"HTTPSConnectionPool(host='huggingface.co', port=443): Max retries exceeded with url: /datasets/openai/gsm8k/resolve/740312add88f781978c0658806c59bc2815b9866/gsm8k.py (Caused by ConnectTimeoutError(&lt;urllib3.connection.HTTPSConnection object at 0x7fa1a5455610>, 'Connection to huggingface.co timed out. (connect timeout=10)'))\\\"), '(Request ID: bb4143df-fc9c-4df8-9324-42bed0406762)')' thrown while requesting HEAD https://huggingface.co/datasets/openai/gsm8k/resolve/740312add88f781978c0658806c59bc2815b9866/gsm8k.py\\n2026-05-14 06:59:57,708 [WARNING] '(MaxRetryError(\\\"HTTPSConnectionPool(host='huggingface.co', port=443): Max retries exceeded with url: /datasets/openai/gsm8k/resolve/740312add88f781978c0658806c59bc2815b9866/gsm8k.py (Caused by ConnectTimeoutError(&lt;urllib3.connection.HTTPSConnection object at 0x7fa1a5455610>, 'Connection to huggingface.co timed out. (connect ti
…[truncated 6383 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_gpu-audit_20260514T003001",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-14T00:32:10.839791+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "tail -20 ~/runs/contamcal-irt-calibration/exp_001_sft_d100_05B.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_gpu-audit_20260514T003001",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "tail -20 ~/runs/contamcal-irt-calibration/exp_001_sft_d100_05B.log"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-14T00:32:10.840261+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"设置成功\\n注意：仅限于学术用途和加速访问github/huggingface，不承诺稳定性保证\\n2026-05-14 08:18:40,645 [INFO] Loading base model: /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B + adapter: /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s123/lora_adapter\\n`torch_dtype` is deprecated! Use `dtype` instead!\\n2026-05-14 08:18:41,574 [INFO] We will use 90% of the memory on device 0 for storing the model, and 10% for the buffer to avoid OOM. You can set `max_memory` in to a higher value to use more memory (at your own risk).\\n\\rLoading checkpoint shards:   0%|          | 0/2 [00:00<?, ?it/s]\\rLoading checkpoint shards:  50%|█████     | 1/2 [00:00<00:00,  1.23it/s]\\rLoading checkpoint shards: 100%|██████████| 2/2 [00:01<00:00,  1.64it/s]\\rLoading checkpoint shards: 100%|██████████| 2/2 [00:01<00:00,  1.56it/s]\\n2026-05-14 08:18:42,924 [ERROR] bitsandbytes library load error: libnvJitLink.so.13: cannot open shared object file: No such file or directory\\nTraceback (most recent call last):\\n  File \\\"/root/miniconda3/lib/python3.12/site-packages/bitsandbytes/cextension.py\\\", line 320, in &lt;module>\\n    lib = get_native_library()\\n          ^^^^^^^^^^^^^^^^^^^^\\n  File \\\"/root/miniconda3/lib/python3.12/site-packages/bitsandbytes/cextension.py\\\", line 298, in get_native_library\\n    dll = ct.cdll.LoadLibrary(str(binary_path))\\n          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\\n  File \\\"/root/miniconda3/lib/python3.12/ctypes/__init__.py\\\", line 460, in LoadLibrary\\n    return self._dlltype(name)\\n           ^^^^^^^^^^^^^^^^^^^\\n  File \\\"/root/miniconda3/lib/python3.12/ctypes/__init__.py\\\", line 379, in __init__\\n    self._handle = _dlopen(self._name, mode)\\n                   ^^^^^^^^^^^^^^^^^^^^^^^^^\\nOSError: libnvJitLink.so.13: cannot open shared object file: No such file or directory\\n2026-05-14 08:18:45,489 [INFO] Evaluating mmlu...\\n\\rEvaluating mmlu:   0%|          | 0/14042 [00:00<?, ?it/s]\\rEvaluating mml
…[truncated 6461 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_gpu-audit_20260514T003001",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 5
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-14T00:32:10.840600+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "tail -20 ~/runs/contamcal-irt-calibration/exp_001_sft_d005_05B_v3.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_gpu-audit_20260514T003001",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "tail -20 ~/runs/contamcal-irt-calibration/exp_001_sft_d005_05B_v3.log"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-14T00:32:10.840953+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"设置成功\\n注意：仅限于学术用途和加速访问github/huggingface，不承诺稳定性保证\\n2026-05-14 08:23:39,459 [INFO] Loading base model: /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B + adapter: /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s42/lora_adapter\\n`torch_dtype` is deprecated! Use `dtype` instead!\\n2026-05-14 08:23:40,705 [INFO] We will use 90% of the memory on device 0 for storing the model, and 10% for the buffer to avoid OOM. You can set `max_memory` in to a higher value to use more memory (at your own risk).\\n2026-05-14 08:23:41,854 [ERROR] bitsandbytes library load error: libnvJitLink.so.13: cannot open shared object file: No such file or directory\\nTraceback (most recent call last):\\n  File \\\"/root/miniconda3/lib/python3.12/site-packages/bitsandbytes/cextension.py\\\", line 320, in &lt;module>\\n    lib = get_native_library()\\n          ^^^^^^^^^^^^^^^^^^^^\\n  File \\\"/root/miniconda3/lib/python3.12/site-packages/bitsandbytes/cextension.py\\\", line 298, in get_native_library\\n    dll = ct.cdll.LoadLibrary(str(binary_path))\\n          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\\n  File \\\"/root/miniconda3/lib/python3.12/ctypes/__init__.py\\\", line 460, in LoadLibrary\\n    return self._dlltype(name)\\n           ^^^^^^^^^^^^^^^^^^^\\n  File \\\"/root/miniconda3/lib/python3.12/ctypes/__init__.py\\\", line 379, in __init__\\n    self._handle = _dlopen(self._name, mode)\\n                   ^^^^^^^^^^^^^^^^^^^^^^^^^\\nOSError: libnvJitLink.so.13: cannot open shared object file: No such file or directory\\n2026-05-14 08:23:44,623 [INFO] Evaluating mmlu...\\n\\rEvaluating mmlu:   0%|          | 0/14042 [00:00<?, ?it/s]\\rEvaluating mmlu:   0%|          | 1/14042 [00:00<1:25:28,  2.74it/s]\\rEvaluating mmlu:   0%|          | 6/14042 [00:00<15:20, 15.24it/s]  \\rEvaluating mmlu:   0%|          | 11/14042 [00:00<09:48, 23.86it/s]\\rEvaluating mmlu:   0%|          | 16/14042 [00:00<07:49, 29.88it/s]\\rEvaluating mmlu:   0%|  
…[truncated 6459 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_gpu-audit_20260514T003001",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 5
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-14T00:32:10.841212+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls -la /root/contamcal-irt-calibration/exp001/paraphrase_data/mmlu_paraphrases*.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_gpu-audit_20260514T003001",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls -la /root/contamcal-irt-calibration/exp001/paraphrase_data/mmlu_paraphrases*.json"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-14T00:32:10.845754+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{'loss': 1.5608, 'grad_norm': 0.41779112815856934, 'learning_rate': 6.680863771573318e-05, 'entropy': 1.5649215802550316, 'num_tokens': 13594815.0, 'mean_token_accuracy': 0.6698638424277306, 'epoch': 0.63}\\n{'loss': 1.526, 'grad_norm': 0.4679546356201172, 'learning_rate': 6.6059632837151e-05, 'entropy': 1.5919934943318368, 'num_tokens': 13647405.0, 'mean_token_accuracy': 0.6661245793104171, 'epoch': 0.63}\\n{'loss': 1.6163, 'grad_norm': 0.34849902987480164, 'learning_rate': 6.53127738114026e-05, 'entropy': 1.5941992923617363, 'num_tokens': 13702949.0, 'mean_token_accuracy': 0.6633670002222061, 'epoch': 0.63}\\n{'loss': 1.4937, 'grad_norm': 0.41242361068725586, 'learning_rate': 6.456810785805842e-05, 'entropy': 1.522462823987007, 'num_tokens': 13754863.0, 'mean_token_accuracy': 0.6765383809804917, 'epoch': 0.63}\\n{'loss': 1.5626, 'grad_norm': 0.6753412485122681, 'learning_rate': 6.38256820580336e-05, 'entropy': 1.5832376316189767, 'num_tokens': 13802317.0, 'mean_token_accuracy': 0.6626036018133163, 'epoch': 0.64}\\n{'loss': 1.53, 'grad_norm': 0.44990089535713196, 'learning_rate': 6.308554335061135e-05, 'entropy': 1.540166161954403, 'num_tokens': 13855565.0, 'mean_token_accuracy': 0.6708258196711541, 'epoch': 0.64}\\n{'loss': 1.5372, 'grad_norm': 0.44465628266334534, 'learning_rate': 6.234773853047526e-05, 'entropy': 1.5588075503706933, 'num_tokens': 13910896.0, 'mean_token_accuracy': 0.6664832934737206, 'epoch': 0.64}\\n{'loss': 1.7684, 'grad_norm': 0.508327305316925, 'learning_rate': 6.161231424475075e-05, 'entropy': 1.7402721121907234, 'num_tokens': 13960677.0, 'mean_token_accuracy': 0.6399419791996479, 'epoch': 0.64}\\n{'loss': 1.5752, 'grad_norm': 0.499240905046463, 'learning_rate': 6.087931699005588e-05, 'entropy': 1.6067791908979416, 'num_tokens': 14011344.0, 'mean_token_accuracy': 0.6654349520802498, 'epoch': 0.65}\\n{'loss': 1.4664, 'grad_norm': 0.4787816107273102, 'learning_rate': 6.014879310956154e-0
…[truncated 6412 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_gpu-audit_20260514T003001",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 5
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-14T00:32:10.846169+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{'loss': 1.4671, 'grad_norm': 0.4336630403995514, 'learning_rate': 0.0001256304465864077, 'entropy': 1.4626007184386254, 'num_tokens': 8802154.0, 'mean_token_accuracy': 0.6889372661709785, 'epoch': 0.45}\\n{'loss': 1.5112, 'grad_norm': 0.47321996092796326, 'learning_rate': 0.00012462289614811715, 'entropy': 1.5092211350798608, 'num_tokens': 8865206.0, 'mean_token_accuracy': 0.6765840634703636, 'epoch': 0.45}\\n{'loss': 1.4873, 'grad_norm': 0.45787113904953003, 'learning_rate': 0.00012361267764433192, 'entropy': 1.5022942572832108, 'num_tokens': 8927332.0, 'mean_token_accuracy': 0.6796069949865341, 'epoch': 0.45}\\n{'loss': 1.4862, 'grad_norm': 0.44225117564201355, 'learning_rate': 0.0001225999005393944, 'entropy': 1.519694671034813, 'num_tokens': 8987071.0, 'mean_token_accuracy': 0.6813973471522331, 'epoch': 0.46}\\n{'loss': 1.5276, 'grad_norm': 0.4989939332008362, 'learning_rate': 0.00012158467457488934, 'entropy': 1.5398542165756226, 'num_tokens': 9041595.0, 'mean_token_accuracy': 0.6702012270689011, 'epoch': 0.46}\\n{'loss': 1.6099, 'grad_norm': 0.4307800829410553, 'learning_rate': 0.00012056710975775303, 'entropy': 1.5974410414695739, 'num_tokens': 9108949.0, 'mean_token_accuracy': 0.661497849225998, 'epoch': 0.46}\\n{'loss': 1.4397, 'grad_norm': 0.4105091691017151, 'learning_rate': 0.00011954731634835288, 'entropy': 1.430204600095749, 'num_tokens': 9168342.0, 'mean_token_accuracy': 0.6881812646985054, 'epoch': 0.47}\\n{'loss': 1.5753, 'grad_norm': 0.5199145078659058, 'learning_rate': 0.00011852540484854009, 'entropy': 1.566726490855217, 'num_tokens': 9221781.0, 'mean_token_accuracy': 0.6699885286390781, 'epoch': 0.47}\\n{'loss': 1.5102, 'grad_norm': 0.6241583824157715, 'learning_rate': 0.00011750148598967611, 'entropy': 1.5247375696897507, 'num_tokens': 9281448.0, 'mean_token_accuracy': 0.6756048828363419, 'epoch': 0.47}\\n{'loss': 1.5135, 'grad_norm': 0.680500328540802, 'learning_rate': 0.0001164756707206
…[truncated 6412 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_gpu-audit_20260514T003001",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 5
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-14T00:32:10.846461+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/contamcal-irt-calibration/exp001/paraphrase_data/mmlu_paraphrases*.json': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_gpu-audit_20260514T003001",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 5
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-14T00:32:10.846766+00:00_

## 巡检结果

### GPU 全景

| GPU | 进程 | 显存 | 利用率 | 状态 | ETA |
|-----|------|------|--------|------|-----|
| 0 | PID 235243 — sft_d100_05B | 22.0/24.6 GB | 94% | SFT 训练 73% (3031/4159) | ~19 min |
| 1 | PID 229370 — eval_05B_d000_s42 | 3.7/24.6 GB | 33% | GSM8K 76% (1006/1319) | ~28 min |
| 2 | PID 229516 — eval_05B_d000_s123 | 3.7/24.6 GB | 33% | GSM8K 73% (965/1319) | ~33 min |
| 3 | PID 242581 — eval_3B_d000_s123 | 9.0/24.6 GB | 65% | GSM8K 3% (44/1319) | ~2h44m |
| 4 | PID 243290 — eval_15B_d000_s42_v2 | 5.8/24.6 GB | 50% | GSM8K 2% (31/1319) | ~2h11m |
| 5 | PID 239729 — sft_d005_05B_v3 | 22.0/24.6 GB | 49% | SFT 训练 59% (1860/3177) | ~23 min |

所有 6 个 PID 存活，无异常。

---

### 已完成 SFT 最终指标

| 任务 | train_loss | token_accuracy | 耗时 | 退出码 |
|------|-----------|----------------|------|--------|
| sft_0pct_3B_s123 | **1.131** | 0.751 | 3.6h | 0 |
| sft_0pct_15B_s123 | **1.260** | 0.731 | 1.7h | 0 |
| sft_0pct_05B_s123 | **1.539** | 0.676 | 55min | 0 |

---

### 正在运行的 Eval 已出结果

| 任务 | MMLU Acc | GSM8K 进度 |
|------|----------|------------|
| eval_3B_d000_s123 | **0.6362** (8933/14042) | 3% — 刚开始 |
| eval_15B_d000_s42_v2 | **0.5753** (8079/14042) | 2% — 刚开始 |
| eval_05B_d000_s42 | (已完成,日志截断) | 76% |
| eval_05B_d000_s123 | (已完成,日志截断) | 73% |

---

### 进行中 SFT 当前 loss

| 任务 | 当前 loss | epoch | 进度 |
|------|----------|-------|------|
| sft_d100_05B | ~1.53 | 0.67 | 73% |
| sft_d005_05B_v3 | ~1.53 | 0.50 | 59% |

---

### MMLU Paraphrase

**无进程运行，无输出文件。** 两个路径 (`/root/autodl-tmp/exp001/paraphrase_data/` 和 `/root/contamcal-irt-calibration/exp001/paraphrase_data/`) 均未找到 `mmlu_paraphrases*.json`。

---

### 异常/注意事项

1. **HuggingFace 连接超时**: GPU 1/2 的 eval 进程启动时遇到大量 HF 超时（gsm8k 数据集下载），最终通过重试恢复。GPU 3/4 启动时加了 `network_turbo` 避免了此问题。
2. **bitsandbytes 警告**: GPU 3/4 的 eval 进程报 `libnvJitLink.so.13` 缺失，属非致命错误，不影响评估。
3. **Paraphrase 未启动**: GPU 0 当前被 sft_d100_05B 占满（94%），无 paraphrase 进程。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_ops_gpu-audit_20260514T003001"
}
```

</details>

---
