# harvest three done exps 0527 — Part 3 of 3

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Worker execution logs

[← Part 2](part-002.md) · [Transcript overview](../harvest-three-done-exps-0527.md) · [Structured JSON](../../../sessions/02/02836ba8eab69a5032cc.json)

## Before a recorded user message

### Assistant

_source line 30_

<details><summary>Logged reasoning block</summary>

```text
All three experiments are NOT in the registry (count=0 for all). I need to create entries for all three. Let me fix the ps command and also check for running experiments.

The `filters` parameter for read_registry probably filters on fields, not exp_id directly. Let me check the running processes with a correct command.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "91b3d5c1-50da-4650-a87b-7ce4afd361f3",
  "uuid": "0547a8e5-62be-4b5e-a602-5117b7e38e50",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y3KqhGxZo6RAQE27njSxnB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1907,
      "cache_read_input_tokens": 30012,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1907
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Assistant

_source line 31_

三个实验都不在 registry 中。修复 ps 命令查看运行中的实验。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "91b3d5c1-50da-4650-a87b-7ce4afd361f3",
  "uuid": "e1f7be87-390d-4eb9-9eeb-e6b4b97bd0ef",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y3KqhGxZo6RAQE27njSxnB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1907,
      "cache_read_input_tokens": 30012,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1907
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 32_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_013fJF1CWLMaGv9mQYauu9S4`</summary>

```json
{
  "server": "westd-38929",
  "command": "ps aux",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "91b3d5c1-50da-4650-a87b-7ce4afd361f3",
  "uuid": "eb46b669-5cb8-445f-815f-b76c83f13e0e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y3KqhGxZo6RAQE27njSxnB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1907,
      "cache_read_input_tokens": 30012,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1907
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 33 · 2026-05-27T01:29:09.950Z_

<details><summary>↩ Tool result · `toolu_013fJF1CWLMaGv9mQYauu9S4`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"USER        PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND\\nroot          1  0.0  0.0   4476  3360 ?        Ss   May26   0:02 bash /init/boot/boot.sh\\nroot        915  1.9  0.0 724640 24880 ?        Sl   May26  37:16 /bin/supervisord -c /init/supervisor/supervisor.ini\\nroot        931  0.0  0.0  15444  9372 ?        S    May26   0:52 sshd: /usr/sbin/sshd -D [listener] 1 of 10-100 startups\\nroot        933  0.0  0.0 187564 102408 ?       S    May26   0:01 /root/miniconda3/bin/python /root/miniconda3/bin/jupyter-lab --allow-root --config=/init/jupyter/jupyter_config.py\\nroot        935  0.2  0.0 6821072 106556 ?      Sl   May26   4:20 autopanel serve --work-dir=/root/autodl-tmp --cache-dir=/root/autodl-tmp\\nroot        936  0.2  0.0 2867972 25524 ?       Sl   May26   5:36 proxy -c /init/proxy/proxy.ini\\nroot        937  0.0  0.0 2868996 19688 ?       Sl   May26   0:23 proxy -c /init/proxy/proxy-hot-backup.ini\\nroot        938  0.0  0.0 5405824 648396 ?      Sl   May26   1:10 /root/miniconda3/bin/python /root/miniconda3/bin/tensorboard --host 0.0.0.0 --port 6007 --logdir /root/tf-logs\\nroot       1057  0.0  0.0 28341192 12292 ?      Sl   May26   1:33 /root/miniconda3/lib/python3.12/site-packages/tensorboard_data_server/bin/server --logdir=/root/tf-logs --reload=5 --samples-per-plugin= --port=0 --port-file=/tmp/tensorboard_data_server_v5x28ial/port --die-after-stdin --error-file=/tmp/tensorboard_data_server_v5x28ial/startup_error\\nroot       1520  0.0  0.0  16776 10772 ?        Ss   May26   0:22 sshd: root@notty\\nroot       6805  0.0  0.0   6296  4028 ?        Ss   May26   0:01 tmux new-session -d -s eval_openvla_attn_k07_long_seed42_v2 rm -f /tmp/agent-ml-exit/eval_openvla_attn_k07_long_seed42_v2.exit; mkdir -p /tmp/agent-ml-exit; trap '_EC=$?; echo \\\"EXIT_CODE=$_EC\\\" >> ~/runs/importance_margin_vla_compress/eval_openvla_attn_k07_long_seed42_v2.log; printf \\\"%s|%s\\\\n\\\" \\\"$_EC\\\" \\\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\\\" > /tmp/agent-ml-exit/eval_openvla_attn_k07_long_seed42_v2.exit' EXIT; trap 'exit 129' HUP; trap 'exit 130' INT; trap 'exit 143' TERM; { cd /root/autodl-tmp/importance_margin_vla_compress && export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && timeout 43200 env bash -c 'bash -c \\\"cd /root/autodl-tmp/importance_margin_vla_compress && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYTHONUNBUFFERED=1 && export HF_HOME=/root/autodl-tmp/.hf_cache && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && python3 eval_openvla_l2norm_libero.py --mode attention_prune --k_ratio 0.7 --suite libero_10 --model_path /root/autodl-tmp/models/openvla-7b-finetuned-libero-10 --unnorm_key libero_10 --num_episodes 50 --seed 42 --output results/openvla_attention_prune_k07_long_seed42.json\\\"'; } > ~/runs/importance_margin_vla_compress/eval_openvla_attn_k07_long_seed42_v2.log 2>&1\\nroot     732922  0.0  0.0   4496  3632 pts/1    Ss+  01:30   0:00 bash -c rm -f /tmp/agent-ml-exit/eval_openvla_l2norm_k075_long_seed42.exit; mkdir -p /tmp/agent-ml-exit; trap '_EC=$?; echo \\\"EXIT_CODE=$_EC\\\" >> ~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k075_long_seed42.log; printf \\\"%s|%s\\\\n\\\" \\\"$_EC\\\" \\\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\\\" > /tmp/agent-ml-exit/eval_openvla_l2norm_k075_long_seed42.exit' EXIT; trap 'exit 129' HUP; trap 'exit 130' INT; trap 'exit 143' TERM; { cd /root/autodl-tmp/importance_margin_vla_compress && export CUDA_VISIBLE_DEVICES=2 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && timeout 28800 env bash -c 'MUJOCO_GL=egl /root/miniconda3/bin/python -u /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.75 --suite libero_10 --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/models/openvla-7b-finetuned-libero-10 --unnorm_key libero_10'; } > ~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k075_long_seed42.log 2>&1\\nroot     732930  0.0  0.0\\n\\n... [截断: 输出过长，省略 2509 字符] ...\\n\\nc rm -f /tmp/agent-ml-exit/eval_openvla_l2norm_k095_long_seed42.exit; mkdir -p /tmp/agent-ml-exit; trap '_EC=$?; echo \\\"EXIT_CODE=$_EC\\\" >> ~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k095_long_seed42.log; printf \\\"%s|%s\\\\n\\\" \\\"$_EC\\\" \\\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\\\" > /tmp/agent-ml-exit/eval_openvla_l2norm_k095_long_seed42.exit' EXIT; trap 'exit 129' HUP; trap 'exit 130' INT; trap 'exit 143' TERM; { cd /root/autodl-tmp/importance_margin_vla_compress && export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && timeout 43200 env bash -c 'cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=1 python -u eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.95 --suite libero_10 --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/models/openvla-7b-finetuned-libero-10 --unnorm_key libero_10'; } > ~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k095_long_seed42.log 2>&1\\nroot     949446  0.0  0.0   2800  1036 pts/2    S    09:11   0:00 timeout 43200 env bash -c cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=1 python -u eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.95 --suite libero_10 --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/models/openvla-7b-finetuned-libero-10 --unnorm_key libero_10\\nroot     949447  833  0.6 68667008 6383576 pts/2 Rl  09:11 143:03 python -u eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.95 --suite libero_10 --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/models/openvla-7b-finetuned-libero-10 --unnorm_key libero_10\\nroot     949998  0.0  0.0   4496  3660 pts/3    Ss+  09:12   0:00 bash -c rm -f /tmp/agent-ml-exit/eval_openvla_attn_k095_long_seed42.exit; mkdir -p /tmp/agent-ml-exit; trap '_EC=$?; echo \\\"EXIT_CODE=$_EC\\\" >> ~/runs/importance_margin_vla_compress/eval_openvla_attn_k095_long_seed42.log; printf \\\"%s|%s\\\\n\\\" \\\"$_EC\\\" \\\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\\\" > /tmp/agent-ml-exit/eval_openvla_attn_k095_long_seed42.exit' EXIT; trap 'exit 129' HUP; trap 'exit 130' INT; trap 'exit 143' TERM; { cd /root/autodl-tmp/importance_margin_vla_compress && export CUDA_VISIBLE_DEVICES=3 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && timeout 43200 env bash -c 'cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=3 python -u eval_openvla_l2norm_libero.py --mode attention_prune --k_ratio 0.95 --suite libero_10 --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/models/openvla-7b-finetuned-libero-10 --unnorm_key libero_10'; } > ~/runs/importance_margin_vla_compress/eval_openvla_attn_k095_long_seed42.log 2>&1\\nroot     950006  0.0  0.0   2800  1040 pts/3    S    09:12   0:00 timeout 43200 env bash -c cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=3 python -u eval_openvla_l2norm_libero.py --mode attention_prune --k_ratio 0.95 --suite libero_10 --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/models/openvla-7b-finetuned-libero-10 --unnorm_key libero_10\\nroot     950007  835  0.5 67430580 6266172 pts/3 Rl  09:12 142:14 python -u eval_openvla_l2norm_libero.py --mode attention_prune --k_ratio 0.95 --suite libero_10 --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/models/openvla-7b-finetuned-libero-10 --unnorm_key libero_10\\nroot     953748  0.0  0.0  16692 11056 ?        Ss   09:17   0:00 sshd: root@notty\\nroot     957563  0.0  0.0  16692 10596 ?        Ss   09:24   0:00 sshd: root@notty\\nroot     959732  0.0  0.0  16692 10784 ?        Ss   09:28   0:00 sshd: root@notty\\nroot     959748  0.0  0.0  16692 10688 ?        Ss   09:28   0:00 sshd: root@notty\\nroot     960005  0.1  0.0  16692 10676 ?        Ss   09:28   0:00 sshd: root@notty\\nroot     960203  0.0  0.0  16304  9692 ?        Ss   09:29   0:00 sshd: root [priv]\\nsshd     960204  0.0  0.0  15444  5656 ?        S    09:29   0:00 sshd: root [net]\\nroot     960299  0.0  0.0   7064  1544 ?        Rs   09:29   0:00 ps aux\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "91b3d5c1-50da-4650-a87b-7ce4afd361f3",
  "uuid": "e248fb3f-bd1b-4964-936d-ddc66eae9cd7",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"USER        PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND\\\\nroot          1  0.0  0.0   4476  3360 ?        Ss   May26   0:02 bash /init/boot/boot.sh\\\\nroot        915  1.9  0.0 724640 24880 ?        Sl   May26  37:16 /bin/supervisord -c /init/supervisor/supervisor.ini\\\\nroot        931  0.0  0.0  15444  9372 ?        S    May26   0:52 sshd: /usr/sbin/sshd -D [listener] 1 of 10-100 startups\\\\nroot        933  0.0  0.0 187564 102408 ?       S    May26   0:01 /root/miniconda3/bin/python /root/miniconda3/bin/jupyter-lab --allow-root --config=/init/jupyter/jupyter_config.py\\\\nroot        935  0.2  0.0 6821072 106556 ?      Sl   May26   4:20 autopanel serve --work-dir=/root/autodl-tmp --cache-dir=/root/autodl-tmp\\\\nroot        936  0.2  0.0 2867972 25524 ?       Sl   May26   5:36 proxy -c /init/proxy/proxy.ini\\\\nroot        937  0.0  0.0 2868996 19688 ?       Sl   May26   0:23 proxy -c /init/proxy/proxy-hot-backup.ini\\\\nroot        938  0.0  0.0 5405824 648396 ?      Sl   May26   1:10 /root/miniconda3/bin/python /root/miniconda3/bin/tensorboard --host 0.0.0.0 --port 6007 --logdir /root/tf-logs\\\\nroot       1057  0.0  0.0 28341192 12292 ?      Sl   May26   1:33 /root/miniconda3/lib/python3.12/site-packages/tensorboard_data_server/bin/server --logdir=/root/tf-logs --reload=5 --samples-per-plugin= --port=0 --port-file=/tmp/tensorboard_data_server_v5x28ial/port --die-after-stdin --error-file=/tmp/tensorboard_data_server_v5x28ial/startup_error\\\\nroot       1520  0.0  0.0  16776 10772 ?        Ss   May26   0:22 sshd: root@notty\\\\nroot       6805  0.0  0.0   6296  4028 ?        Ss   May26   0:01 tmux new-session -d -s eval_openvla_attn_k07_long_seed42_v2 rm -f /tmp/agent-ml-exit/eval_openvla_attn_k07_long_seed42_v2.exit; mkdir -p /tmp/agent-ml-exit; trap '_EC=$?; echo \\\\\\\"EXIT_CODE=$_EC\\\\\\\" >> ~/runs/importance_margin_vla_compress/eval_openvla_attn_k07_long_seed42_v2.log; printf \\\\\\\"%s|%s\\\\\\\\n\\\\\\\" \\\\\\\"$_EC\\\\\\\" \\\\\\\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\\\\\\\" > /tmp/agent-ml-exit/eval_openvla_attn_k07_long_seed42_v2.exit' EXIT; trap 'exit 129' HUP; trap 'exit 130' INT; trap 'exit 143' TERM; { cd /root/autodl-tmp/importance_margin_vla_compress && export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && timeout 43200 env bash -c 'bash -c \\\\\\\"cd /root/autodl-tmp/importance_margin_vla_compress && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYTHONUNBUFFERED=1 && export HF_HOME=/root/autodl-tmp/.hf_cache && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && python3 eval_openvla_l2norm_libero.py --mode attention_prune --k_ratio 0.7 --suite libero_10 --model_path /root/autodl-tmp/models/openvla-7b-finetuned-libero-10 --unnorm_key libero_10 --num_episodes 50 --seed 42 --output results/openvla_attention_prune_k07_long_seed42.json\\\\\\\"'; } > ~/runs/importance_margin_vla_compress/eval_openvla_attn_k07_long_seed42_v2.log 2>&1\\\\nroot     732922  0.0  0.0   4496  3632 pts/1    Ss+  01:30   0:00 bash -c rm -f /tmp/agent-ml-exit/eval_openvla_l2norm_k075_long_seed42.exit; mkdir -p /tmp/agent-ml-exit; trap '_EC=$?; echo \\\\\\\"EXIT_CODE=$_EC\\\\\\\" >> ~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k075_long_seed42.log; printf \\\\\\\"%s|%s\\\\\\\\n\\\\\\\" \\\\\\\"$_EC\\\\\\\" \\\\\\\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\\\\\\\" > /tmp/agent-ml-exit/eval_openvla_l2norm_k075_long_seed42.exit' EXIT; trap 'exit 129' HUP; trap 'exit 130' INT; trap 'exit 143' TERM; { cd /root/autodl-tmp/importance_margin_vla_compress && export CUDA_VISIBLE_DEVICES=2 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && timeout 28800 env bash -c 'MUJOCO_GL=egl /root/miniconda3/bin/python -u /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.75 --suite libero_10 --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/models/openvla-7b-finetuned-libero-10 --unnorm_key libero_10'; } > ~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k075_long_seed42.log 2>&1\\\\nroot     732930  0.0  0.0\\\\n\\\\n... [截断: 输出过长，省略 2509 字符] ...\\\\n\\\\nc rm -f /tmp/agent-ml-exit/eval_openvla_l2norm_k095_long_seed42.exit; mkdir -p /tmp/agent-ml-exit; trap '_EC=$?; echo \\\\\\\"EXIT_CODE=$_EC\\\\\\\" >> ~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k095_long_seed42.log; printf \\\\\\\"%s|%s\\\\\\\\n\\\\\\\" \\\\\\\"$_EC\\\\\\\" \\\\\\\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\\\\\\\" > /tmp/agent-ml-exit/eval_openvla_l2norm_k095_long_seed42.exit' EXIT; trap 'exit 129' HUP; trap 'exit 130' INT; trap 'exit 143' TERM; { cd /root/autodl-tmp/importance_margin_vla_compress && export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && timeout 43200 env bash -c 'cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=1 python -u eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.95 --suite libero_10 --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/models/openvla-7b-finetuned-libero-10 --unnorm_key libero_10'; } > ~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k095_long_seed42.log 2>&1\\\\nroot     949446  0.0  0.0   2800  1036 pts/2    S    09:11   0:00 timeout 43200 env bash -c cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=1 python -u eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.95 --suite libero_10 --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/models/openvla-7b-finetuned-libero-10 --unnorm_key libero_10\\\\nroot     949447  833  0.6 68667008 6383576 pts/2 Rl  09:11 143:03 python -u eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.95 --suite libero_10 --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/models/openvla-7b-finetuned-libero-10 --unnorm_key libero_10\\\\nroot     949998  0.0  0.0   4496  3660 pts/3    Ss+  09:12   0:00 bash -c rm -f /tmp/agent-ml-exit/eval_openvla_attn_k095_long_seed42.exit; mkdir -p /tmp/agent-ml-exit; trap '_EC=$?; echo \\\\\\\"EXIT_CODE=$_EC\\\\\\\" >> ~/runs/importance_margin_vla_compress/eval_openvla_attn_k095_long_seed42.log; printf \\\\\\\"%s|%s\\\\\\\\n\\\\\\\" \\\\\\\"$_EC\\\\\\\" \\\\\\\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\\\\\\\" > /tmp/agent-ml-exit/eval_openvla_attn_k095_long_seed42.exit' EXIT; trap 'exit 129' HUP; trap 'exit 130' INT; trap 'exit 143' TERM; { cd /root/autodl-tmp/importance_margin_vla_compress && export CUDA_VISIBLE_DEVICES=3 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && timeout 43200 env bash -c 'cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=3 python -u eval_openvla_l2norm_libero.py --mode attention_prune --k_ratio 0.95 --suite libero_10 --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/models/openvla-7b-finetuned-libero-10 --unnorm_key libero_10'; } > ~/runs/importance_margin_vla_compress/eval_openvla_attn_k095_long_seed42.log 2>&1\\\\nroot     950006  0.0  0.0   2800  1040 pts/3    S    09:12   0:00 timeout 43200 env bash -c cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=3 python -u eval_openvla_l2norm_libero.py --mode attention_prune --k_ratio 0.95 --suite libero_10 --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/models/openvla-7b-finetuned-libero-10 --unnorm_key libero_10\\\\nroot     950007  835  0.5 67430580 6266172 pts/3 Rl  09:12 142:14 python -u eval_openvla_l2norm_libero.py --mode attention_prune --k_ratio 0.95 --suite libero_10 --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/models/openvla-7b-finetuned-libero-10 --unnorm_key libero_10\\\\nroot     953748  0.0  0.0  16692 11056 ?        Ss   09:17   0:00 sshd: root@notty\\\\nroot     957563  0.0  0.0  16692 10596 ?        Ss   09:24   0:00 sshd: root@notty\\\\nroot     959732  0.0  0.0  16692 10784 ?        Ss   09:28   0:00 sshd: root@notty\\\\nroot     959748  0.0  0.0  16692 10688 ?        Ss   09:28   0:00 sshd: root@notty\\\\nroot     960005  0.1  0.0  16692 10676 ?        Ss   09:28   0:00 sshd: root@notty\\\\nroot     960203  0.0  0.0  16304  9692 ?        Ss   09:29   0:00 sshd: root [priv]\\\\nsshd     960204  0.0  0.0  15444  5656 ?        S    09:29   0:00 sshd: root [net]\\\\nroot     960299  0.0  0.0   7064  1544 ?        Rs   09:29   0:00 ps aux\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.5}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"USER        PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND\\nroot          1  0.0  0.0   4476  3360 ?        Ss   May26   0:02 bash /init/boot/boot.sh\\nroot        915  1.9  0.0 724640 24880 ?        Sl   May26  37:16 /bin/supervisord -c /init/supervisor/supervisor.ini\\nroot        931  0.0  0.0  15444  9372 ?        S    May26   0:52 sshd: /usr/sbin/sshd -D [listener] 1 of 10-100 startups\\nroot        933  0.0  0.0 187564 102408 ?       S    May26   0:01 /root/miniconda3/bin/python /root/miniconda3/bin/jupyter-lab --allow-root --config=/init/jupyter/jupyter_config.py\\nroot        935  0.2  0.0 6821072 106556 ?      Sl   May26   4:20 autopanel serve --work-dir=/root/autodl-tmp --cache-dir=/root/autodl-tmp\\nroot        936  0.2  0.0 2867972 25524 ?       Sl   May26   5:36 proxy -c /init/proxy/proxy.ini\\nroot        937  0.0  0.0 2868996 19688 ?       Sl   May26   0:23 proxy -c /init/proxy/proxy-hot-backup.ini\\nroot        938  0.0  0.0 5405824 648396 ?      Sl   May26   1:10 /root/miniconda3/bin/python /root/miniconda3/bin/tensorboard --host 0.0.0.0 --port 6007 --logdir /root/tf-logs\\nroot       1057  0.0  0.0 28341192 12292 ?      Sl   May26   1:33 /root/miniconda3/lib/python3.12/site-packages/tensorboard_data_server/bin/server --logdir=/root/tf-logs --reload=5 --samples-per-plugin= --port=0 --port-file=/tmp/tensorboard_data_server_v5x28ial/port --die-after-stdin --error-file=/tmp/tensorboard_data_server_v5x28ial/startup_error\\nroot       1520  0.0  0.0  16776 10772 ?        Ss   May26   0:22 sshd: root@notty\\nroot       6805  0.0  0.0   6296  4028 ?        Ss   May26   0:01 tmux new-session -d -s eval_openvla_attn_k07_long_seed42_v2 rm -f /tmp/agent-ml-exit/eval_openvla_attn_k07_long_seed42_v2.exit; mkdir -p /tmp/agent-ml-exit; trap '_EC=$?; echo \\\"EXIT_CODE=$_EC\\\" >> ~/runs/importance_margin_vla_compress/eval_openvla_attn_k07_long_seed42_v2.log; printf \\\"%s|%s\\\\n\\\" \\\"$_EC\\\" \\\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\\\" > /tmp/agent-ml-exit/eval_openvla_attn_k07_long_seed42_v2.exit' EXIT; trap 'exit 129' HUP; trap 'exit 130' INT; trap 'exit 143' TERM; { cd /root/autodl-tmp/importance_margin_vla_compress && export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && timeout 43200 env bash -c 'bash -c \\\"cd /root/autodl-tmp/importance_margin_vla_compress && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYTHONUNBUFFERED=1 && export HF_HOME=/root/autodl-tmp/.hf_cache && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && python3 eval_openvla_l2norm_libero.py --mode attention_prune --k_ratio 0.7 --suite libero_10 --model_path /root/autodl-tmp/models/openvla-7b-finetuned-libero-10 --unnorm_key libero_10 --num_episodes 50 --seed 42 --output results/openvla_attention_prune_k07_long_seed42.json\\\"'; } > ~/runs/importance_margin_vla_compress/eval_openvla_attn_k07_long_seed42_v2.log 2>&1\\nroot     732922  0.0  0.0   4496  3632 pts/1    Ss+  01:30   0:00 bash -c rm -f /tmp/agent-ml-exit/eval_openvla_l2norm_k075_long_seed42.exit; mkdir -p /tmp/agent-ml-exit; trap '_EC=$?; echo \\\"EXIT_CODE=$_EC\\\" >> ~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k075_long_seed42.log; printf \\\"%s|%s\\\\n\\\" \\\"$_EC\\\" \\\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\\\" > /tmp/agent-ml-exit/eval_openvla_l2norm_k075_long_seed42.exit' EXIT; trap 'exit 129' HUP; trap 'exit 130' INT; trap 'exit 143' TERM; { cd /root/autodl-tmp/importance_margin_vla_compress && export CUDA_VISIBLE_DEVICES=2 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && timeout 28800 env bash -c 'MUJOCO_GL=egl /root/miniconda3/bin/python -u /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.75 --suite libero_10 --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/models/openvla-7b-finetuned-libero-10 --unnorm_key libero_10'; } > ~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k075_long_seed42.log 2>&1\\nroot     732930  0.0  0.0\\n\\n... [截断: 输出过长，省略 2509 字符] ...\\n\\nc rm -f /tmp/agent-ml-exit/eval_openvla_l2norm_k095_long_seed42.exit; mkdir -p /tmp/agent-ml-exit; trap '_EC=$?; echo \\\"EXIT_CODE=$_EC\\\" >> ~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k095_long_seed42.log; printf \\\"%s|%s\\\\n\\\" \\\"$_EC\\\" \\\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\\\" > /tmp/agent-ml-exit/eval_openvla_l2norm_k095_long_seed42.exit' EXIT; trap 'exit 129' HUP; trap 'exit 130' INT; trap 'exit 143' TERM; { cd /root/autodl-tmp/importance_margin_vla_compress && export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && timeout 43200 env bash -c 'cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=1 python -u eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.95 --suite libero_10 --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/models/openvla-7b-finetuned-libero-10 --unnorm_key libero_10'; } > ~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k095_long_seed42.log 2>&1\\nroot     949446  0.0  0.0   2800  1036 pts/2    S    09:11   0:00 timeout 43200 env bash -c cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=1 python -u eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.95 --suite libero_10 --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/models/openvla-7b-finetuned-libero-10 --unnorm_key libero_10\\nroot     949447  833  0.6 68667008 6383576 pts/2 Rl  09:11 143:03 python -u eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.95 --suite libero_10 --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/models/openvla-7b-finetuned-libero-10 --unnorm_key libero_10\\nroot     949998  0.0  0.0   4496  3660 pts/3    Ss+  09:12   0:00 bash -c rm -f /tmp/agent-ml-exit/eval_openvla_attn_k095_long_seed42.exit; mkdir -p /tmp/agent-ml-exit; trap '_EC=$?; echo \\\"EXIT_CODE=$_EC\\\" >> ~/runs/importance_margin_vla_compress/eval_openvla_attn_k095_long_seed42.log; printf \\\"%s|%s\\\\n\\\" \\\"$_EC\\\" \\\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\\\" > /tmp/agent-ml-exit/eval_openvla_attn_k095_long_seed42.exit' EXIT; trap 'exit 129' HUP; trap 'exit 130' INT; trap 'exit 143' TERM; { cd /root/autodl-tmp/importance_margin_vla_compress && export CUDA_VISIBLE_DEVICES=3 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && timeout 43200 env bash -c 'cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=3 python -u eval_openvla_l2norm_libero.py --mode attention_prune --k_ratio 0.95 --suite libero_10 --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/models/openvla-7b-finetuned-libero-10 --unnorm_key libero_10'; } > ~/runs/importance_margin_vla_compress/eval_openvla_attn_k095_long_seed42.log 2>&1\\nroot     950006  0.0  0.0   2800  1040 pts/3    S    09:12   0:00 timeout 43200 env bash -c cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=3 python -u eval_openvla_l2norm_libero.py --mode attention_prune --k_ratio 0.95 --suite libero_10 --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/models/openvla-7b-finetuned-libero-10 --unnorm_key libero_10\\nroot     950007  835  0.5 67430580 6266172 pts/3 Rl  09:12 142:14 python -u eval_openvla_l2norm_libero.py --mode attention_prune --k_ratio 0.95 --suite libero_10 --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/models/openvla-7b-finetuned-libero-10 --unnorm_key libero_10\\nroot     953748  0.0  0.0  16692 11056 ?        Ss   09:17   0:00 sshd: root@notty\\nroot     957563  0.0  0.0  16692 10596 ?        Ss   09:24   0:00 sshd: root@notty\\nroot     959732  0.0  0.0  16692 10784 ?        Ss   09:28   0:00 sshd: root@notty\\nroot     959748  0.0  0.0  16692 10688 ?        Ss   09:28   0:00 sshd: root@notty\\nroot     960005  0.1  0.0  16692 10676 ?        Ss   09:28   0:00 sshd: root@notty\\nroot     960203  0.0  0.0  16304  9692 ?        Ss   09:29   0:00 sshd: root [priv]\\nsshd     960204  0.0  0.0  15444  5656 ?        S    09:29   0:00 sshd: root [net]\\nroot     960299  0.0  0.0   7064  1544 ?        Rs   09:29   0:00 ps aux\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 34_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_013gkrNuQ8oM3U1fuhu1CWJX`</summary>

```json
{
  "server": "westd-41074",
  "command": "ps aux",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "91b3d5c1-50da-4650-a87b-7ce4afd361f3",
  "uuid": "517febf4-e70e-403b-b09a-4dbb349888ea",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y3KqhGxZo6RAQE27njSxnB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1907,
      "cache_read_input_tokens": 30012,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1907
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 35_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_011x7fVq6jj11NTWLT57YARb`</summary>

```json
{
  "server": "westd-27271",
  "command": "ps aux",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "91b3d5c1-50da-4650-a87b-7ce4afd361f3",
  "uuid": "a6f01b4e-24bc-4207-a83a-89350a657dc7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y3KqhGxZo6RAQE27njSxnB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1907,
      "cache_read_input_tokens": 30012,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1907
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 36 · 2026-05-27T01:29:10.991Z_

<details><summary>↩ Tool result · `toolu_013gkrNuQ8oM3U1fuhu1CWJX`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"USER        PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND\\nroot          1  0.0  0.0   4476  3044 ?        Ss   May26   0:00 bash /init/boot/boot.sh\\nroot        801  2.4  0.0 724128 21552 ?        Sl   May26  46:58 /bin/supervisord -c /init/supervisor/supervisor.ini\\nroot        816  0.0  0.0  15444  9020 ?        S    May26   0:00 sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups\\nroot        817  0.0  0.0 4147860 76416 ?       Sl   May26   1:09 /root/miniconda3/bin/python /root/miniconda3/bin/tensorboard --host 0.0.0.0 --port 6007 --logdir /root/tf-logs\\nroot        819  0.0  0.0 190188 99912 ?        S    May26   0:01 /root/miniconda3/bin/python /root/miniconda3/bin/jupyter-lab --allow-root --config=/init/jupyter/jupyter_config.py\\nroot        820  0.0  0.0 2720764 19900 ?       Sl   May26   0:54 proxy -c /init/proxy/proxy.ini\\nroot        822  0.2  0.0 6893524 106312 ?      Sl   May26   4:18 autopanel serve --work-dir=/root/autodl-tmp --cache-dir=/root/autodl-tmp\\nroot        828  0.0  0.0 2499312 20432 ?       Sl   May26   0:23 proxy -c /init/proxy/proxy-hot-backup.ini\\nroot        930  0.0  0.0 28341068 10796 ?      Sl   May26   1:42 /root/miniconda3/lib/python3.12/site-packages/tensorboard_data_server/bin/server --logdir=/root/tf-logs --reload=5 --samples-per-plugin= --port=0 --port-file=/tmp/tensorboard_data_server_lv2cih0h/port --die-after-stdin --error-file=/tmp/tensorboard_data_server_lv2cih0h/startup_error\\nroot       1393  0.0  0.0  16776 10596 ?        Ss   May26   0:17 sshd: root@notty\\nroot       3977  0.0  0.0   6548  4224 ?        Ss   May26   0:01 tmux new-session -d -s eval_openvla_random_k05_object_seed42_v2 rm -f /tmp/agent-ml-exit/eval_openvla_random_k05_object_seed42_v2.exit; mkdir -p /tmp/agent-ml-exit; trap '_EC=$?; echo \\\"EXIT_CODE=$_EC\\\" >> ~/runs/importance_margin_vla_compress/eval_openvla_random_k05_object_seed42_v2.log; printf \\\"%s|%s\\\\n\\\" \\\"$_EC\\\" \\\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\\\" > /tmp/agent-ml-exit/eval_openvla_random_k05_object_seed42_v2.exit' EXIT; trap 'exit 129' HUP; trap 'exit 130' INT; trap 'exit 143' TERM; { cd /root/autodl-tmp/importance_margin_vla_compress && export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && timeout 28800 env bash -c 'bash -c \\\"cd /root/autodl-tmp/importance_margin_vla_compress && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYTHONUNBUFFERED=1 && export HF_HOME=/root/autodl-tmp/.hf_cache && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && python3 eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.5 --suite libero_object --num_episodes 50 --seed 42 --output results/openvla_random_k05_object_seed42.json > /tmp/eval_openvla_random_k05_object_seed42_v2.log 2>&1\\\"'; } > ~/runs/importance_margin_vla_compress/eval_openvla_random_k05_object_seed42_v2.log 2>&1\\nroot      32175  0.0  0.0   4496  3500 pts/3    Ss+  08:29   0:00 bash -c rm -f /tmp/agent-ml-exit/eval_openvla_random_k095_long_seed42.exit; mkdir -p /tmp/agent-ml-exit; trap '_EC=$?; echo \\\"EXIT_CODE=$_EC\\\" >> ~/runs/importance_margin_vla_compress/eval_openvla_random_k095_long_seed42.log; printf \\\"%s|%s\\\\n\\\" \\\"$_EC\\\" \\\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\\\" > /tmp/agent-ml-exit/eval_openvla_random_k095_long_seed42.exit' EXIT; trap 'exit 129' HUP; trap 'exit 130' INT; trap 'exit 143' TERM; { cd /root/autodl-tmp/importance_margin_vla_compress && export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && timeout 28800 env bash -c 'bash -c \\\"cd /root/autodl-tmp/importance_margin_vla_compress && python -u eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.95 --suite libero_10 --seed 42 --gpu 0\\\"'; } > ~/runs/importance_margin_vla_compress/eval_openvla_random_k095_long_seed42.log 2>&1\\nroot      32183  0.0  0.0   2800  1048 pts/3    S    08:29   0:00 timeout 28800 env bash -c bash -c \\\"cd /root/autodl-tmp/importance_margin_vla_compress && python -u \\n\\n... [截断: 输出过长，省略 1206 字符] ...\\n\\nrintf \\\"%s|%s\\\\n\\\" \\\"$_EC\\\" \\\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\\\" > /tmp/agent-ml-exit/eval_openvla_attn_k075_long_seed42.exit' EXIT; trap 'exit 129' HUP; trap 'exit 130' INT; trap 'exit 143' TERM; { cd /root/autodl-tmp/importance_margin_vla_compress && export CUDA_VISIBLE_DEVICES=3 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && timeout 28800 env bash -c 'MUJOCO_GL=egl python -u /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py --mode attention_prune --k_ratio 0.75 --suite libero_10 --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/openvla-7b-finetuned-libero-10 --unnorm_key libero_10'; } > ~/runs/importance_margin_vla_compress/eval_openvla_attn_k075_long_seed42.log 2>&1\\nroot     824209  0.0  0.0   2800  1096 pts/4    S    02:29   0:00 timeout 28800 env bash -c MUJOCO_GL=egl python -u /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py --mode attention_prune --k_ratio 0.75 --suite libero_10 --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/openvla-7b-finetuned-libero-10 --unnorm_key libero_10\\nroot     824210  751  0.6 66997264 6572832 pts/4 Rl  02:29 3149:38 python -u /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py --mode attention_prune --k_ratio 0.75 --suite libero_10 --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/openvla-7b-finetuned-libero-10 --unnorm_key libero_10\\nroot     856562  0.0  0.0   4496  3588 pts/7    Ss+  03:21   0:00 bash -c rm -f /tmp/agent-ml-exit/eval_openvla_random_k075_long_seed42.exit; mkdir -p /tmp/agent-ml-exit; trap '_EC=$?; echo \\\"EXIT_CODE=$_EC\\\" >> ~/runs/importance_margin_vla_compress/eval_openvla_random_k075_long_seed42.log; printf \\\"%s|%s\\\\n\\\" \\\"$_EC\\\" \\\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\\\" > /tmp/agent-ml-exit/eval_openvla_random_k075_long_seed42.exit' EXIT; trap 'exit 129' HUP; trap 'exit 130' INT; trap 'exit 143' TERM; { cd /root/autodl-tmp/importance_margin_vla_compress && export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && timeout 86400 env bash -c 'bash -c \\\"cd /root/autodl-tmp/importance_margin_vla_compress && MUJOCO_GL=egl python -u eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.75 --suite libero_10 --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/openvla-7b-finetuned-libero-10 --unnorm_key libero_10\\\"'; } > ~/runs/importance_margin_vla_compress/eval_openvla_random_k075_long_seed42.log 2>&1\\nroot     856655  0.0  0.0   2800  1028 pts/7    S    03:21   0:00 timeout 86400 env bash -c bash -c \\\"cd /root/autodl-tmp/importance_margin_vla_compress && MUJOCO_GL=egl python -u eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.75 --suite libero_10 --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/openvla-7b-finetuned-libero-10 --unnorm_key libero_10\\\"\\nroot     856656  710  0.6 67393960 7272964 pts/7 Rl  03:21 2614:55 python -u eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.75 --suite libero_10 --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/openvla-7b-finetuned-libero-10 --unnorm_key libero_10\\nroot     934363  0.0  0.0   4364  3200 pts/2    Ss+  05:32   0:00 bash -c cd /root/autodl-tmp/importance_margin_vla_compress && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=2 MUJOCO_GL=egl python -u eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.95 --suite libero_object --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/openvla-libero-object --unnorm_key libero_object 2>&1 | tee logs/eval_openvla_random_k095_object_seed42.log\\nroot     934369  704  0.6 65731788 7158772 pts/2 Rl+ 05:32 1667:14 python -u eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.95 --suite libero_object --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/openvla-libero-object --unnorm_key libero_object\\nroot     934370  0.0  0.0   2796  1008 pts/2    S+   05:32   0:00 tee logs/eval_openvla_random_k095_object_seed42.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "91b3d5c1-50da-4650-a87b-7ce4afd361f3",
  "uuid": "8bf5c3fc-17f1-495a-aafc-93784909dd07",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"USER        PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND\\\\nroot          1  0.0  0.0   4476  3044 ?        Ss   May26   0:00 bash /init/boot/boot.sh\\\\nroot        801  2.4  0.0 724128 21552 ?        Sl   May26  46:58 /bin/supervisord -c /init/supervisor/supervisor.ini\\\\nroot        816  0.0  0.0  15444  9020 ?        S    May26   0:00 sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups\\\\nroot        817  0.0  0.0 4147860 76416 ?       Sl   May26   1:09 /root/miniconda3/bin/python /root/miniconda3/bin/tensorboard --host 0.0.0.0 --port 6007 --logdir /root/tf-logs\\\\nroot        819  0.0  0.0 190188 99912 ?        S    May26   0:01 /root/miniconda3/bin/python /root/miniconda3/bin/jupyter-lab --allow-root --config=/init/jupyter/jupyter_config.py\\\\nroot        820  0.0  0.0 2720764 19900 ?       Sl   May26   0:54 proxy -c /init/proxy/proxy.ini\\\\nroot        822  0.2  0.0 6893524 106312 ?      Sl   May26   4:18 autopanel serve --work-dir=/root/autodl-tmp --cache-dir=/root/autodl-tmp\\\\nroot        828  0.0  0.0 2499312 20432 ?       Sl   May26   0:23 proxy -c /init/proxy/proxy-hot-backup.ini\\\\nroot        930  0.0  0.0 28341068 10796 ?      Sl   May26   1:42 /root/miniconda3/lib/python3.12/site-packages/tensorboard_data_server/bin/server --logdir=/root/tf-logs --reload=5 --samples-per-plugin= --port=0 --port-file=/tmp/tensorboard_data_server_lv2cih0h/port --die-after-stdin --error-file=/tmp/tensorboard_data_server_lv2cih0h/startup_error\\\\nroot       1393  0.0  0.0  16776 10596 ?        Ss   May26   0:17 sshd: root@notty\\\\nroot       3977  0.0  0.0   6548  4224 ?        Ss   May26   0:01 tmux new-session -d -s eval_openvla_random_k05_object_seed42_v2 rm -f /tmp/agent-ml-exit/eval_openvla_random_k05_object_seed42_v2.exit; mkdir -p /tmp/agent-ml-exit; trap '_EC=$?; echo \\\\\\\"EXIT_CODE=$_EC\\\\\\\" >> ~/runs/importance_margin_vla_compress/eval_openvla_random_k05_object_seed42_v2.log; printf \\\\\\\"%s|%s\\\\\\\\n\\\\\\\" \\\\\\\"$_EC\\\\\\\" \\\\\\\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\\\\\\\" > /tmp/agent-ml-exit/eval_openvla_random_k05_object_seed42_v2.exit' EXIT; trap 'exit 129' HUP; trap 'exit 130' INT; trap 'exit 143' TERM; { cd /root/autodl-tmp/importance_margin_vla_compress && export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && timeout 28800 env bash -c 'bash -c \\\\\\\"cd /root/autodl-tmp/importance_margin_vla_compress && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYTHONUNBUFFERED=1 && export HF_HOME=/root/autodl-tmp/.hf_cache && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && python3 eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.5 --suite libero_object --num_episodes 50 --seed 42 --output results/openvla_random_k05_object_seed42.json > /tmp/eval_openvla_random_k05_object_seed42_v2.log 2>&1\\\\\\\"'; } > ~/runs/importance_margin_vla_compress/eval_openvla_random_k05_object_seed42_v2.log 2>&1\\\\nroot      32175  0.0  0.0   4496  3500 pts/3    Ss+  08:29   0:00 bash -c rm -f /tmp/agent-ml-exit/eval_openvla_random_k095_long_seed42.exit; mkdir -p /tmp/agent-ml-exit; trap '_EC=$?; echo \\\\\\\"EXIT_CODE=$_EC\\\\\\\" >> ~/runs/importance_margin_vla_compress/eval_openvla_random_k095_long_seed42.log; printf \\\\\\\"%s|%s\\\\\\\\n\\\\\\\" \\\\\\\"$_EC\\\\\\\" \\\\\\\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\\\\\\\" > /tmp/agent-ml-exit/eval_openvla_random_k095_long_seed42.exit' EXIT; trap 'exit 129' HUP; trap 'exit 130' INT; trap 'exit 143' TERM; { cd /root/autodl-tmp/importance_margin_vla_compress && export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && timeout 28800 env bash -c 'bash -c \\\\\\\"cd /root/autodl-tmp/importance_margin_vla_compress && python -u eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.95 --suite libero_10 --seed 42 --gpu 0\\\\\\\"'; } > ~/runs/importance_margin_vla_compress/eval_openvla_random_k095_long_seed42.log 2>&1\\\\nroot      32183  0.0  0.0   2800  1048 pts/3    S    08:29   0:00 timeout 28800 env bash -c bash -c \\\\\\\"cd /root/autodl-tmp/importance_margin_vla_compress && python -u \\\\n\\\\n... [截断: 输出过长，省略 1206 字符] ...\\\\n\\\\nrintf \\\\\\\"%s|%s\\\\\\\\n\\\\\\\" \\\\\\\"$_EC\\\\\\\" \\\\\\\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\\\\\\\" > /tmp/agent-ml-exit/eval_openvla_attn_k075_long_seed42.exit' EXIT; trap 'exit 129' HUP; trap 'exit 130' INT; trap 'exit 143' TERM; { cd /root/autodl-tmp/importance_margin_vla_compress && export CUDA_VISIBLE_DEVICES=3 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && timeout 28800 env bash -c 'MUJOCO_GL=egl python -u /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py --mode attention_prune --k_ratio 0.75 --suite libero_10 --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/openvla-7b-finetuned-libero-10 --unnorm_key libero_10'; } > ~/runs/importance_margin_vla_compress/eval_openvla_attn_k075_long_seed42.log 2>&1\\\\nroot     824209  0.0  0.0   2800  1096 pts/4    S    02:29   0:00 timeout 28800 env bash -c MUJOCO_GL=egl python -u /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py --mode attention_prune --k_ratio 0.75 --suite libero_10 --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/openvla-7b-finetuned-libero-10 --unnorm_key libero_10\\\\nroot     824210  751  0.6 66997264 6572832 pts/4 Rl  02:29 3149:38 python -u /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py --mode attention_prune --k_ratio 0.75 --suite libero_10 --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/openvla-7b-finetuned-libero-10 --unnorm_key libero_10\\\\nroot     856562  0.0  0.0   4496  3588 pts/7    Ss+  03:21   0:00 bash -c rm -f /tmp/agent-ml-exit/eval_openvla_random_k075_long_seed42.exit; mkdir -p /tmp/agent-ml-exit; trap '_EC=$?; echo \\\\\\\"EXIT_CODE=$_EC\\\\\\\" >> ~/runs/importance_margin_vla_compress/eval_openvla_random_k075_long_seed42.log; printf \\\\\\\"%s|%s\\\\\\\\n\\\\\\\" \\\\\\\"$_EC\\\\\\\" \\\\\\\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\\\\\\\" > /tmp/agent-ml-exit/eval_openvla_random_k075_long_seed42.exit' EXIT; trap 'exit 129' HUP; trap 'exit 130' INT; trap 'exit 143' TERM; { cd /root/autodl-tmp/importance_margin_vla_compress && export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && timeout 86400 env bash -c 'bash -c \\\\\\\"cd /root/autodl-tmp/importance_margin_vla_compress && MUJOCO_GL=egl python -u eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.75 --suite libero_10 --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/openvla-7b-finetuned-libero-10 --unnorm_key libero_10\\\\\\\"'; } > ~/runs/importance_margin_vla_compress/eval_openvla_random_k075_long_seed42.log 2>&1\\\\nroot     856655  0.0  0.0   2800  1028 pts/7    S    03:21   0:00 timeout 86400 env bash -c bash -c \\\\\\\"cd /root/autodl-tmp/importance_margin_vla_compress && MUJOCO_GL=egl python -u eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.75 --suite libero_10 --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/openvla-7b-finetuned-libero-10 --unnorm_key libero_10\\\\\\\"\\\\nroot     856656  710  0.6 67393960 7272964 pts/7 Rl  03:21 2614:55 python -u eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.75 --suite libero_10 --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/openvla-7b-finetuned-libero-10 --unnorm_key libero_10\\\\nroot     934363  0.0  0.0   4364  3200 pts/2    Ss+  05:32   0:00 bash -c cd /root/autodl-tmp/importance_margin_vla_compress && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=2 MUJOCO_GL=egl python -u eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.95 --suite libero_object --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/openvla-libero-object --unnorm_key libero_object 2>&1 | tee logs/eval_openvla_random_k095_object_seed42.log\\\\nroot     934369  704  0.6 65731788 7158772 pts/2 Rl+ 05:32 1667:14 python -u eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.95 --suite libero_object --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/openvla-libero-object --unnorm_key libero_object\\\\nroot     934370  0.0  0.0   2796  1008 pts/2    S+   05:32   0:00 tee logs/eval_openvla_random_k095_object_seed42.log\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.52}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"USER        PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND\\nroot          1  0.0  0.0   4476  3044 ?        Ss   May26   0:00 bash /init/boot/boot.sh\\nroot        801  2.4  0.0 724128 21552 ?        Sl   May26  46:58 /bin/supervisord -c /init/supervisor/supervisor.ini\\nroot        816  0.0  0.0  15444  9020 ?        S    May26   0:00 sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups\\nroot        817  0.0  0.0 4147860 76416 ?       Sl   May26   1:09 /root/miniconda3/bin/python /root/miniconda3/bin/tensorboard --host 0.0.0.0 --port 6007 --logdir /root/tf-logs\\nroot        819  0.0  0.0 190188 99912 ?        S    May26   0:01 /root/miniconda3/bin/python /root/miniconda3/bin/jupyter-lab --allow-root --config=/init/jupyter/jupyter_config.py\\nroot        820  0.0  0.0 2720764 19900 ?       Sl   May26   0:54 proxy -c /init/proxy/proxy.ini\\nroot        822  0.2  0.0 6893524 106312 ?      Sl   May26   4:18 autopanel serve --work-dir=/root/autodl-tmp --cache-dir=/root/autodl-tmp\\nroot        828  0.0  0.0 2499312 20432 ?       Sl   May26   0:23 proxy -c /init/proxy/proxy-hot-backup.ini\\nroot        930  0.0  0.0 28341068 10796 ?      Sl   May26   1:42 /root/miniconda3/lib/python3.12/site-packages/tensorboard_data_server/bin/server --logdir=/root/tf-logs --reload=5 --samples-per-plugin= --port=0 --port-file=/tmp/tensorboard_data_server_lv2cih0h/port --die-after-stdin --error-file=/tmp/tensorboard_data_server_lv2cih0h/startup_error\\nroot       1393  0.0  0.0  16776 10596 ?        Ss   May26   0:17 sshd: root@notty\\nroot       3977  0.0  0.0   6548  4224 ?        Ss   May26   0:01 tmux new-session -d -s eval_openvla_random_k05_object_seed42_v2 rm -f /tmp/agent-ml-exit/eval_openvla_random_k05_object_seed42_v2.exit; mkdir -p /tmp/agent-ml-exit; trap '_EC=$?; echo \\\"EXIT_CODE=$_EC\\\" >> ~/runs/importance_margin_vla_compress/eval_openvla_random_k05_object_seed42_v2.log; printf \\\"%s|%s\\\\n\\\" \\\"$_EC\\\" \\\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\\\" > /tmp/agent-ml-exit/eval_openvla_random_k05_object_seed42_v2.exit' EXIT; trap 'exit 129' HUP; trap 'exit 130' INT; trap 'exit 143' TERM; { cd /root/autodl-tmp/importance_margin_vla_compress && export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && timeout 28800 env bash -c 'bash -c \\\"cd /root/autodl-tmp/importance_margin_vla_compress && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYTHONUNBUFFERED=1 && export HF_HOME=/root/autodl-tmp/.hf_cache && export TRANSFORMERS_OFFLINE=1 && export HF_HUB_OFFLINE=1 && python3 eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.5 --suite libero_object --num_episodes 50 --seed 42 --output results/openvla_random_k05_object_seed42.json > /tmp/eval_openvla_random_k05_object_seed42_v2.log 2>&1\\\"'; } > ~/runs/importance_margin_vla_compress/eval_openvla_random_k05_object_seed42_v2.log 2>&1\\nroot      32175  0.0  0.0   4496  3500 pts/3    Ss+  08:29   0:00 bash -c rm -f /tmp/agent-ml-exit/eval_openvla_random_k095_long_seed42.exit; mkdir -p /tmp/agent-ml-exit; trap '_EC=$?; echo \\\"EXIT_CODE=$_EC\\\" >> ~/runs/importance_margin_vla_compress/eval_openvla_random_k095_long_seed42.log; printf \\\"%s|%s\\\\n\\\" \\\"$_EC\\\" \\\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\\\" > /tmp/agent-ml-exit/eval_openvla_random_k095_long_seed42.exit' EXIT; trap 'exit 129' HUP; trap 'exit 130' INT; trap 'exit 143' TERM; { cd /root/autodl-tmp/importance_margin_vla_compress && export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && timeout 28800 env bash -c 'bash -c \\\"cd /root/autodl-tmp/importance_margin_vla_compress && python -u eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.95 --suite libero_10 --seed 42 --gpu 0\\\"'; } > ~/runs/importance_margin_vla_compress/eval_openvla_random_k095_long_seed42.log 2>&1\\nroot      32183  0.0  0.0   2800  1048 pts/3    S    08:29   0:00 timeout 28800 env bash -c bash -c \\\"cd /root/autodl-tmp/importance_margin_vla_compress && python -u \\n\\n... [截断: 输出过长，省略 1206 字符] ...\\n\\nrintf \\\"%s|%s\\\\n\\\" \\\"$_EC\\\" \\\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\\\" > /tmp/agent-ml-exit/eval_openvla_attn_k075_long_seed42.exit' EXIT; trap 'exit 129' HUP; trap 'exit 130' INT; trap 'exit 143' TERM; { cd /root/autodl-tmp/importance_margin_vla_compress && export CUDA_VISIBLE_DEVICES=3 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && timeout 28800 env bash -c 'MUJOCO_GL=egl python -u /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py --mode attention_prune --k_ratio 0.75 --suite libero_10 --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/openvla-7b-finetuned-libero-10 --unnorm_key libero_10'; } > ~/runs/importance_margin_vla_compress/eval_openvla_attn_k075_long_seed42.log 2>&1\\nroot     824209  0.0  0.0   2800  1096 pts/4    S    02:29   0:00 timeout 28800 env bash -c MUJOCO_GL=egl python -u /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py --mode attention_prune --k_ratio 0.75 --suite libero_10 --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/openvla-7b-finetuned-libero-10 --unnorm_key libero_10\\nroot     824210  751  0.6 66997264 6572832 pts/4 Rl  02:29 3149:38 python -u /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py --mode attention_prune --k_ratio 0.75 --suite libero_10 --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/openvla-7b-finetuned-libero-10 --unnorm_key libero_10\\nroot     856562  0.0  0.0   4496  3588 pts/7    Ss+  03:21   0:00 bash -c rm -f /tmp/agent-ml-exit/eval_openvla_random_k075_long_seed42.exit; mkdir -p /tmp/agent-ml-exit; trap '_EC=$?; echo \\\"EXIT_CODE=$_EC\\\" >> ~/runs/importance_margin_vla_compress/eval_openvla_random_k075_long_seed42.log; printf \\\"%s|%s\\\\n\\\" \\\"$_EC\\\" \\\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\\\" > /tmp/agent-ml-exit/eval_openvla_random_k075_long_seed42.exit' EXIT; trap 'exit 129' HUP; trap 'exit 130' INT; trap 'exit 143' TERM; { cd /root/autodl-tmp/importance_margin_vla_compress && export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && timeout 86400 env bash -c 'bash -c \\\"cd /root/autodl-tmp/importance_margin_vla_compress && MUJOCO_GL=egl python -u eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.75 --suite libero_10 --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/openvla-7b-finetuned-libero-10 --unnorm_key libero_10\\\"'; } > ~/runs/importance_margin_vla_compress/eval_openvla_random_k075_long_seed42.log 2>&1\\nroot     856655  0.0  0.0   2800  1028 pts/7    S    03:21   0:00 timeout 86400 env bash -c bash -c \\\"cd /root/autodl-tmp/importance_margin_vla_compress && MUJOCO_GL=egl python -u eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.75 --suite libero_10 --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/openvla-7b-finetuned-libero-10 --unnorm_key libero_10\\\"\\nroot     856656  710  0.6 67393960 7272964 pts/7 Rl  03:21 2614:55 python -u eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.75 --suite libero_10 --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/openvla-7b-finetuned-libero-10 --unnorm_key libero_10\\nroot     934363  0.0  0.0   4364  3200 pts/2    Ss+  05:32   0:00 bash -c cd /root/autodl-tmp/importance_margin_vla_compress && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=2 MUJOCO_GL=egl python -u eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.95 --suite libero_object --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/openvla-libero-object --unnorm_key libero_object 2>&1 | tee logs/eval_openvla_random_k095_object_seed42.log\\nroot     934369  704  0.6 65731788 7158772 pts/2 Rl+ 05:32 1667:14 python -u eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.95 --suite libero_object --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/openvla-libero-object --unnorm_key libero_object\\nroot     934370  0.0  0.0   2796  1008 pts/2    S+   05:32   0:00 tee logs/eval_openvla_random_k095_object_seed42.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 37 · 2026-05-27T01:29:11.462Z_

<details><summary>↩ Tool result · `toolu_011x7fVq6jj11NTWLT57YARb`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"USER        PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND\\nroot          1  0.0  0.0   4476  3324 ?        Ss   May26   0:00 bash /init/boot/boot.sh\\nroot        889  2.1  0.0 720544 23596 ?        Sl   May26  29:14 /bin/supervisord -c /init/supervisor/supervisor.ini\\nroot        909  0.0  0.0  15444  9440 ?        S    May26   0:15 sshd: /usr/sbin/sshd -D [listener] 1 of 10-100 startups\\nroot        911  0.0  0.0 3329208 82200 ?       Sl   May26   0:49 /root/miniconda3/bin/python /root/miniconda3/bin/tensorboard --host 0.0.0.0 --port 6007 --logdir /root/tf-logs\\nroot        912  0.0  0.0 2721020 20776 ?       Sl   May26   0:44 proxy -c /init/proxy/proxy.ini\\nroot        913  0.2  0.0 6820816 106212 ?      Sl   May26   2:54 autopanel serve --work-dir=/root/autodl-tmp --cache-dir=/root/autodl-tmp\\nroot        915  0.0  0.0 189172 104304 ?       S    May26   0:01 /root/miniconda3/bin/python /root/miniconda3/bin/jupyter-lab --allow-root --config=/init/jupyter/jupyter_config.py\\nroot        916  0.1  0.0 2795264 23016 ?       Sl   May26   1:25 proxy -c /init/proxy/proxy-hot-backup.ini\\nroot       1002  0.0  0.0 28341192 12288 ?      Sl   May26   1:18 /root/miniconda3/lib/python3.12/site-packages/tensorboard_data_server/bin/server --logdir=/root/tf-logs --reload=5 --samples-per-plugin= --port=0 --port-file=/tmp/tensorboard_data_server_zwh_7jca/port --die-after-stdin --error-file=/tmp/tensorboard_data_server_zwh_7jca/startup_error\\nroot       1461  0.0  0.0  16692 10808 ?        Ss   May26   0:09 sshd: root@notty\\nroot      11189  0.0  0.0   6460  4216 ?        Ss   May26   0:00 tmux new-session -d -s eval_openvla_l2norm_k09_goal_seed43_v3 rm -f /tmp/agent-ml-exit/eval_openvla_l2norm_k09_goal_seed43_v3.exit; mkdir -p /tmp/agent-ml-exit; trap '_EC=$?; echo \\\"EXIT_CODE=$_EC\\\" >> ~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k09_goal_seed43_v3.log; printf \\\"%s|%s\\\\n\\\" \\\"$_EC\\\" \\\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\\\" > /tmp/agent-ml-exit/eval_openvla_l2norm_k09_goal_seed43_v3.exit' EXIT; trap 'exit 129' HUP; trap 'exit 130' INT; trap 'exit 143' TERM; { cd /root/autodl-tmp/importance_margin_vla_compress && export CUDA_VISIBLE_DEVICES=0 && timeout 86400 env bash -c 'bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl python -u eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.9 --suite libero_goal --num_episodes 50 --seed 43 --model_path /root/autodl-tmp/openvla-7b-finetuned-libero-goal --unnorm_key libero_goal\\\"'; } > ~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k09_goal_seed43_v3.log 2>&1\\nroot     551444  0.0  0.0   4756  3980 pts/1    Ss+  06:57   0:00 -bash\\nroot     551650  0.0  0.0   4756  3976 pts/3    Ss+  06:58   0:00 -bash\\nroot     551869  0.0  0.0   4756  4044 pts/4    Ss+  06:58   0:00 -bash\\nroot     609726  0.0  0.0   4496  3636 pts/0    Ss+  08:30   0:00 bash -c rm -f /tmp/agent-ml-exit/eval_openvla_l2norm_k095_goal_seed42.exit; mkdir -p /tmp/agent-ml-exit; trap '_EC=$?; echo \\\"EXIT_CODE=$_EC\\\" >> ~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k095_goal_seed42.log; printf \\\"%s|%s\\\\n\\\" \\\"$_EC\\\" \\\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\\\" > /tmp/agent-ml-exit/eval_openvla_l2norm_k095_goal_seed42.exit' EXIT; trap 'exit 129' HUP; trap 'exit 130' INT; trap 'exit 143' TERM; { cd /root/autodl-tmp/importance_margin_vla_compress && export CUDA_VISIBLE_DEVICES=0 && timeout 28800 env bash -c 'bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && python -u eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.95 --suite libero_goal --seed 42 --gpu 0\\\"'; } > ~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k095_goal_seed42.log 2>&1\\nroot     609730  0.0  0.0   2800  1056 pts/0    S    08:30   0:00 timeout 28800 env bash -c bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && python -u eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.95 --suite libero_goal --seed 42 --gpu 0\\\"\\nroot     609731  676  0.5 80510936 5800552 pts/0 Rl  08:30 397:03 python -u eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.95 --suite libero_goal --seed 42 --gpu 0\\nroot     633101  0.0  0.0  16692 10656 ?        Ss   09:17   0:00 sshd: root@notty\\nroot     635535  0.0  0.0  16692 10888 ?        Ss   09:24   0:00 sshd: root@notty\\nroot     636964  0.0  0.0  16692 10724 ?        Ss   09:28   0:00 sshd: root@notty\\nroot     636994  0.1  0.0  16692 10880 ?        Ss   09:28   0:00 sshd: root@notty\\nroot     637499  0.5  0.0  16432  9904 ?        Ss   09:29   0:00 sshd: unknown [priv]\\nsshd     637500  0.0  0.0  15444  5524 ?        S    09:29   0:00 sshd: unknown [net]\\nroot     637508  0.0  0.0   7064  1556 ?        Rs   09:29   0:00 ps aux\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "91b3d5c1-50da-4650-a87b-7ce4afd361f3",
  "uuid": "85690140-8ba8-42a9-9b75-f440693b132e",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"USER        PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND\\\\nroot          1  0.0  0.0   4476  3324 ?        Ss   May26   0:00 bash /init/boot/boot.sh\\\\nroot        889  2.1  0.0 720544 23596 ?        Sl   May26  29:14 /bin/supervisord -c /init/supervisor/supervisor.ini\\\\nroot        909  0.0  0.0  15444  9440 ?        S    May26   0:15 sshd: /usr/sbin/sshd -D [listener] 1 of 10-100 startups\\\\nroot        911  0.0  0.0 3329208 82200 ?       Sl   May26   0:49 /root/miniconda3/bin/python /root/miniconda3/bin/tensorboard --host 0.0.0.0 --port 6007 --logdir /root/tf-logs\\\\nroot        912  0.0  0.0 2721020 20776 ?       Sl   May26   0:44 proxy -c /init/proxy/proxy.ini\\\\nroot        913  0.2  0.0 6820816 106212 ?      Sl   May26   2:54 autopanel serve --work-dir=/root/autodl-tmp --cache-dir=/root/autodl-tmp\\\\nroot        915  0.0  0.0 189172 104304 ?       S    May26   0:01 /root/miniconda3/bin/python /root/miniconda3/bin/jupyter-lab --allow-root --config=/init/jupyter/jupyter_config.py\\\\nroot        916  0.1  0.0 2795264 23016 ?       Sl   May26   1:25 proxy -c /init/proxy/proxy-hot-backup.ini\\\\nroot       1002  0.0  0.0 28341192 12288 ?      Sl   May26   1:18 /root/miniconda3/lib/python3.12/site-packages/tensorboard_data_server/bin/server --logdir=/root/tf-logs --reload=5 --samples-per-plugin= --port=0 --port-file=/tmp/tensorboard_data_server_zwh_7jca/port --die-after-stdin --error-file=/tmp/tensorboard_data_server_zwh_7jca/startup_error\\\\nroot       1461  0.0  0.0  16692 10808 ?        Ss   May26   0:09 sshd: root@notty\\\\nroot      11189  0.0  0.0   6460  4216 ?        Ss   May26   0:00 tmux new-session -d -s eval_openvla_l2norm_k09_goal_seed43_v3 rm -f /tmp/agent-ml-exit/eval_openvla_l2norm_k09_goal_seed43_v3.exit; mkdir -p /tmp/agent-ml-exit; trap '_EC=$?; echo \\\\\\\"EXIT_CODE=$_EC\\\\\\\" >> ~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k09_goal_seed43_v3.log; printf \\\\\\\"%s|%s\\\\\\\\n\\\\\\\" \\\\\\\"$_EC\\\\\\\" \\\\\\\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\\\\\\\" > /tmp/agent-ml-exit/eval_openvla_l2norm_k09_goal_seed43_v3.exit' EXIT; trap 'exit 129' HUP; trap 'exit 130' INT; trap 'exit 143' TERM; { cd /root/autodl-tmp/importance_margin_vla_compress && export CUDA_VISIBLE_DEVICES=0 && timeout 86400 env bash -c 'bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl python -u eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.9 --suite libero_goal --num_episodes 50 --seed 43 --model_path /root/autodl-tmp/openvla-7b-finetuned-libero-goal --unnorm_key libero_goal\\\\\\\"'; } > ~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k09_goal_seed43_v3.log 2>&1\\\\nroot     551444  0.0  0.0   4756  3980 pts/1    Ss+  06:57   0:00 -bash\\\\nroot     551650  0.0  0.0   4756  3976 pts/3    Ss+  06:58   0:00 -bash\\\\nroot     551869  0.0  0.0   4756  4044 pts/4    Ss+  06:58   0:00 -bash\\\\nroot     609726  0.0  0.0   4496  3636 pts/0    Ss+  08:30   0:00 bash -c rm -f /tmp/agent-ml-exit/eval_openvla_l2norm_k095_goal_seed42.exit; mkdir -p /tmp/agent-ml-exit; trap '_EC=$?; echo \\\\\\\"EXIT_CODE=$_EC\\\\\\\" >> ~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k095_goal_seed42.log; printf \\\\\\\"%s|%s\\\\\\\\n\\\\\\\" \\\\\\\"$_EC\\\\\\\" \\\\\\\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\\\\\\\" > /tmp/agent-ml-exit/eval_openvla_l2norm_k095_goal_seed42.exit' EXIT; trap 'exit 129' HUP; trap 'exit 130' INT; trap 'exit 143' TERM; { cd /root/autodl-tmp/importance_margin_vla_compress && export CUDA_VISIBLE_DEVICES=0 && timeout 28800 env bash -c 'bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && python -u eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.95 --suite libero_goal --seed 42 --gpu 0\\\\\\\"'; } > ~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k095_goal_seed42.log 2>&1\\\\nroot     609730  0.0  0.0   2800  1056 pts/0    S    08:30   0:00 timeout 28800 env bash -c bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && python -u eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.95 --suite libero_goal --seed 42 --gpu 0\\\\\\\"\\\\nroot     609731  676  0.5 80510936 5800552 pts/0 Rl  08:30 397:03 python -u eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.95 --suite libero_goal --seed 42 --gpu 0\\\\nroot     633101  0.0  0.0  16692 10656 ?        Ss   09:17   0:00 sshd: root@notty\\\\nroot     635535  0.0  0.0  16692 10888 ?        Ss   09:24   0:00 sshd: root@notty\\\\nroot     636964  0.0  0.0  16692 10724 ?        Ss   09:28   0:00 sshd: root@notty\\\\nroot     636994  0.1  0.0  16692 10880 ?        Ss   09:28   0:00 sshd: root@notty\\\\nroot     637499  0.5  0.0  16432  9904 ?        Ss   09:29   0:00 sshd: unknown [priv]\\\\nsshd     637500  0.0  0.0  15444  5524 ?        S    09:29   0:00 sshd: unknown [net]\\\\nroot     637508  0.0  0.0   7064  1556 ?        Rs   09:29   0:00 ps aux\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.45}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"USER        PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND\\nroot          1  0.0  0.0   4476  3324 ?        Ss   May26   0:00 bash /init/boot/boot.sh\\nroot        889  2.1  0.0 720544 23596 ?        Sl   May26  29:14 /bin/supervisord -c /init/supervisor/supervisor.ini\\nroot        909  0.0  0.0  15444  9440 ?        S    May26   0:15 sshd: /usr/sbin/sshd -D [listener] 1 of 10-100 startups\\nroot        911  0.0  0.0 3329208 82200 ?       Sl   May26   0:49 /root/miniconda3/bin/python /root/miniconda3/bin/tensorboard --host 0.0.0.0 --port 6007 --logdir /root/tf-logs\\nroot        912  0.0  0.0 2721020 20776 ?       Sl   May26   0:44 proxy -c /init/proxy/proxy.ini\\nroot        913  0.2  0.0 6820816 106212 ?      Sl   May26   2:54 autopanel serve --work-dir=/root/autodl-tmp --cache-dir=/root/autodl-tmp\\nroot        915  0.0  0.0 189172 104304 ?       S    May26   0:01 /root/miniconda3/bin/python /root/miniconda3/bin/jupyter-lab --allow-root --config=/init/jupyter/jupyter_config.py\\nroot        916  0.1  0.0 2795264 23016 ?       Sl   May26   1:25 proxy -c /init/proxy/proxy-hot-backup.ini\\nroot       1002  0.0  0.0 28341192 12288 ?      Sl   May26   1:18 /root/miniconda3/lib/python3.12/site-packages/tensorboard_data_server/bin/server --logdir=/root/tf-logs --reload=5 --samples-per-plugin= --port=0 --port-file=/tmp/tensorboard_data_server_zwh_7jca/port --die-after-stdin --error-file=/tmp/tensorboard_data_server_zwh_7jca/startup_error\\nroot       1461  0.0  0.0  16692 10808 ?        Ss   May26   0:09 sshd: root@notty\\nroot      11189  0.0  0.0   6460  4216 ?        Ss   May26   0:00 tmux new-session -d -s eval_openvla_l2norm_k09_goal_seed43_v3 rm -f /tmp/agent-ml-exit/eval_openvla_l2norm_k09_goal_seed43_v3.exit; mkdir -p /tmp/agent-ml-exit; trap '_EC=$?; echo \\\"EXIT_CODE=$_EC\\\" >> ~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k09_goal_seed43_v3.log; printf \\\"%s|%s\\\\n\\\" \\\"$_EC\\\" \\\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\\\" > /tmp/agent-ml-exit/eval_openvla_l2norm_k09_goal_seed43_v3.exit' EXIT; trap 'exit 129' HUP; trap 'exit 130' INT; trap 'exit 143' TERM; { cd /root/autodl-tmp/importance_margin_vla_compress && export CUDA_VISIBLE_DEVICES=0 && timeout 86400 env bash -c 'bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl python -u eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.9 --suite libero_goal --num_episodes 50 --seed 43 --model_path /root/autodl-tmp/openvla-7b-finetuned-libero-goal --unnorm_key libero_goal\\\"'; } > ~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k09_goal_seed43_v3.log 2>&1\\nroot     551444  0.0  0.0   4756  3980 pts/1    Ss+  06:57   0:00 -bash\\nroot     551650  0.0  0.0   4756  3976 pts/3    Ss+  06:58   0:00 -bash\\nroot     551869  0.0  0.0   4756  4044 pts/4    Ss+  06:58   0:00 -bash\\nroot     609726  0.0  0.0   4496  3636 pts/0    Ss+  08:30   0:00 bash -c rm -f /tmp/agent-ml-exit/eval_openvla_l2norm_k095_goal_seed42.exit; mkdir -p /tmp/agent-ml-exit; trap '_EC=$?; echo \\\"EXIT_CODE=$_EC\\\" >> ~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k095_goal_seed42.log; printf \\\"%s|%s\\\\n\\\" \\\"$_EC\\\" \\\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\\\" > /tmp/agent-ml-exit/eval_openvla_l2norm_k095_goal_seed42.exit' EXIT; trap 'exit 129' HUP; trap 'exit 130' INT; trap 'exit 143' TERM; { cd /root/autodl-tmp/importance_margin_vla_compress && export CUDA_VISIBLE_DEVICES=0 && timeout 28800 env bash -c 'bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && python -u eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.95 --suite libero_goal --seed 42 --gpu 0\\\"'; } > ~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k095_goal_seed42.log 2>&1\\nroot     609730  0.0  0.0   2800  1056 pts/0    S    08:30   0:00 timeout 28800 env bash -c bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && python -u eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.95 --suite libero_goal --seed 42 --gpu 0\\\"\\nroot     609731  676  0.5 80510936 5800552 pts/0 Rl  08:30 397:03 python -u eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.95 --suite libero_goal --seed 42 --gpu 0\\nroot     633101  0.0  0.0  16692 10656 ?        Ss   09:17   0:00 sshd: root@notty\\nroot     635535  0.0  0.0  16692 10888 ?        Ss   09:24   0:00 sshd: root@notty\\nroot     636964  0.0  0.0  16692 10724 ?        Ss   09:28   0:00 sshd: root@notty\\nroot     636994  0.1  0.0  16692 10880 ?        Ss   09:28   0:00 sshd: root@notty\\nroot     637499  0.5  0.0  16432  9904 ?        Ss   09:29   0:00 sshd: unknown [priv]\\nsshd     637500  0.0  0.0  15444  5524 ?        S    09:29   0:00 sshd: unknown [net]\\nroot     637508  0.0  0.0   7064  1556 ?        Rs   09:29   0:00 ps aux\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 38_

<details><summary>Logged reasoning block</summary>

```text
Let me parse the running experiments across the three servers:

**westd-27271** (the main server):
1. GPU 0: `eval_openvla_attn_k07_long_seed42_v2` - attention_prune, k=0.7, libero_10 (tmux session)
2. GPU 2: `eval_openvla_l2norm_k075_long_seed42` - l2norm_prune, k=0.75, libero_10
3. GPU 1: `eval_openvla_l2norm_k095_long_seed42` - l2norm_prune, k=0.95, libero_10 (started 09:11)


4. GPU 3: `eval_openvla_attn_k095_long_seed42` - attention_prune, k=0.95, libero_10 (started 09:12)

**westd-41074** is running a mix of random pruning experiments with different k values across libero_object and libero_10 datasets.

**westd-38929** has the l2norm pruning experiments active, with k=0.9 and k=0.95 variants on the goal dataset.

Wait, I'm noticing both experiments are assigned to GPU 0 with CUDA_VISIBLE_DEVICES=0 — that's a conflict. Looking at the actual processes running, only one Python process (PID 609731) is actively using the GPU for the l2norm k=0.95 goal experiment, so the tmux session might have already finished. Let me verify which experiments are actually still running.

I need to check the registry for any RUNNING experiments and cross-reference them with the active processes, then update the three completed ones. Since the registry tool creates entries if they don't exist, I'll need to set the required fields — hypothesis, status, conclusion, and metrics — to mark them as DONE with success.

Looking at the constraints, I see that transitioning to DONE requires checkpoint_path and log_path to be set, and hypothesis is mandatory before reaching DONE status. So I'll need to make sequential calls: first create with RUNNING status and spec, then set hypothesis, then log_path and checkpoint_path, then conclusion, then status to DONE, and finally metrics.

Let me try a simpler approach—just set the fields in order without overthinking the dependencies. I'll start by setting hypothesis to create the experiment, then add the spec with the required paths, transition to DONE, and finish with metrics.

Now I'm looking at the specific experiments I need to set up. For the first one, the hypothesis describes an attention-based method testing extreme compression at 50% token retention with an overall success rate of 14.6%. The second experiment uses a different pruning approach with a 62.4% success rate. For the third, I have a user-provided hypothesis about a goal-based random pruning method positioned at a midpoint in the performance curve.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "91b3d5c1-50da-4650-a87b-7ce4afd361f3",
  "uuid": "e67096d3-499d-416a-a2f0-9b8a681a9e50",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XWhWzyjzVQmaP5qwXzCvGk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10045,
      "cache_read_input_tokens": 31919,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10045
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Assistant

_source line 39_

发现大量运行中实验。先注册三个已完成实验 — 设置 hypothesis 创建条目。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "91b3d5c1-50da-4650-a87b-7ce4afd361f3",
  "uuid": "6c3dddb9-dec3-4ca4-b80e-2a17a670fe35",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XWhWzyjzVQmaP5qwXzCvGk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10045,
      "cache_read_input_tokens": 31919,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10045
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 40_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_016pBL9WaRrUYkXMEjDKKfEN`</summary>

```json
{
  "exp_id": "eval_openvla_attn_k05_long_seed42",
  "field": "hypothesis",
  "value": "OpenVLA Attention k=0.5 Long seed42 — Attention pruning 极端压缩(保留50% tokens)在 LIBERO-10 上的性能下限，测试 attention cliff curve 最低点",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "91b3d5c1-50da-4650-a87b-7ce4afd361f3",
  "uuid": "ce6b845a-fbe4-4113-a6f6-c1b66a2f2d5e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XWhWzyjzVQmaP5qwXzCvGk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10045,
      "cache_read_input_tokens": 31919,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10045
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 41_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01WpzLnNRx91QK19Ug4rz3ta`</summary>

```json
{
  "exp_id": "eval_pi05_random_k07_long_seed42",
  "field": "hypothesis",
  "value": "Pi0.5 Random k=0.7 Long seed42 — Pi0.5 模型 Random pruning k=0.7 在 LIBERO-10 Long-horizon 上的性能评估",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "91b3d5c1-50da-4650-a87b-7ce4afd361f3",
  "uuid": "2954b36d-286f-40ac-93fd-5968c67ce68f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XWhWzyjzVQmaP5qwXzCvGk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10045,
      "cache_read_input_tokens": 31919,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10045
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 42_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01TwAPAQKxTV8zEBbNWH4qGB`</summary>

```json
{
  "exp_id": "eval_openvla_random_k075_goal_seed42",
  "field": "hypothesis",
  "value": "OpenVLA Random k=0.75 Goal seed42 — Goal Random cliff curve 中间点。Random k=0.9=79.6%, k=0.85=78.6%, k=0.7=68.4%。k=0.75 精确定位 Goal Random 下降斜率",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "91b3d5c1-50da-4650-a87b-7ce4afd361f3",
  "uuid": "1d7b4b44-d825-46da-a887-460c49cb2877",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XWhWzyjzVQmaP5qwXzCvGk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10045,
      "cache_read_input_tokens": 31919,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10045
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 43 · 2026-05-27T01:30:05.659Z_

<details><summary>↩ Tool result · `toolu_016pBL9WaRrUYkXMEjDKKfEN`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_openvla_attn_k05_long_seed42\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-26T16:07:30.330Z\", \"updated_at\": \"2026-05-27T01:30:01.631Z\", \"hypothesis\": \"OpenVLA Attention k=0.5 Long seed42 — Attention pruning 极端压缩(保留50% tokens)在 LIBERO-10 上的性能下限，测试 attention cliff curve 最低点\", \"spec\": {\"command\": \"python -u eval_openvla_l2norm_libero.py --mode attention_prune --k_ratio 0.5 --suite libero_10 --seed 42 --gpu 0\", \"server\": \"westd-27271\", \"gpu\": 1, \"pid\": 397225, \"data_path\": \"libero_10\", \"data_count\": 500, \"model_name\": \"openvla-7b-finetuned-libero-10\", \"seed\": 42, \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_openvla_attn_k05_long_seed42.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-27T01:27:08.225Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed (log check: no success markers found in log tail (path=/root/autodl-tmp/importance_margin_vla_compress/logs/eval_openvla_attn_k05_long_seed42.log))\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-27T01:27:12.145Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-27T01:27:33.988648+00:00\"}]}, \"metrics\": {\"overall_sr\": 14.6, \"suite\": \"libero_10\", \"prune_method\": \"attention\", \"keep_ratio\": 0.5, \"seed\": 42, \"episodes_per_task\": 50}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 13.4923}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "91b3d5c1-50da-4650-a87b-7ce4afd361f3",
  "uuid": "c1bb6eab-2e88-44fb-9332-239f9172d5af",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval_openvla_attn_k05_long_seed42\\\", \\\"experiment\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-26T16:07:30.330Z\\\", \\\"updated_at\\\": \\\"2026-05-27T01:30:01.631Z\\\", \\\"hypothesis\\\": \\\"OpenVLA Attention k=0.5 Long seed42 — Attention pruning 极端压缩(保留50% tokens)在 LIBERO-10 上的性能下限，测试 attention cliff curve 最低点\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u eval_openvla_l2norm_libero.py --mode attention_prune --k_ratio 0.5 --suite libero_10 --seed 42 --gpu 0\\\", \\\"server\\\": \\\"westd-27271\\\", \\\"gpu\\\": 1, \\\"pid\\\": 397225, \\\"data_path\\\": \\\"libero_10\\\", \\\"data_count\\\": 500, \\\"model_name\\\": \\\"openvla-7b-finetuned-libero-10\\\", \\\"seed\\\": 42, \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_openvla_attn_k05_long_seed42.log\\\"}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-27T01:27:08.225Z\\\"}, \\\"failure_reason\\\": \\\"process dead 5× with no sentinel/W&B — auto-resolved as failed (log check: no success markers found in log tail (path=/root/autodl-tmp/importance_margin_vla_compress/logs/eval_openvla_attn_k05_long_seed42.log))\\\", \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-27T01:27:12.145Z\\\", \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_failed\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-27T01:27:33.988648+00:00\\\"}]}, \\\"metrics\\\": {\\\"overall_sr\\\": 14.6, \\\"suite\\\": \\\"libero_10\\\", \\\"prune_method\\\": \\\"attention\\\", \\\"keep_ratio\\\": 0.5, \\\"seed\\\": 42, \\\"episodes_per_task\\\": 50}}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 13.4923}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval_openvla_attn_k05_long_seed42\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-26T16:07:30.330Z\", \"updated_at\": \"2026-05-27T01:30:01.631Z\", \"hypothesis\": \"OpenVLA Attention k=0.5 Long seed42 — Attention pruning 极端压缩(保留50% tokens)在 LIBERO-10 上的性能下限，测试 attention cliff curve 最低点\", \"spec\": {\"command\": \"python -u eval_openvla_l2norm_libero.py --mode attention_prune --k_ratio 0.5 --suite libero_10 --seed 42 --gpu 0\", \"server\": \"westd-27271\", \"gpu\": 1, \"pid\": 397225, \"data_path\": \"libero_10\", \"data_count\": 500, \"model_name\": \"openvla-7b-finetuned-libero-10\", \"seed\": 42, \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_openvla_attn_k05_long_seed42.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-27T01:27:08.225Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed (log check: no success markers found in log tail (path=/root/autodl-tmp/importance_margin_vla_compress/logs/eval_openvla_attn_k05_long_seed42.log))\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-27T01:27:12.145Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-27T01:27:33.988648+00:00\"}]}, \"metrics\": {\"overall_sr\": 14.6, \"suite\": \"libero_10\", \"prune_method\": \"attention\", \"keep_ratio\": 0.5, \"seed\": 42, \"episodes_per_task\": 50}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 13.4923}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 44 · 2026-05-27T01:30:24.636Z_

<details><summary>↩ Tool result · `toolu_01WpzLnNRx91QK19Ug4rz3ta`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_pi05_random_k07_long_seed42\", \"experiment\": {\"completed_at\": \"2026-05-22T21:54:17.624Z\", \"created_at\": \"2026-05-22T19:10:50.961Z\", \"hypothesis\": \"Pi0.5 Random k=0.7 Long seed42 — Pi0.5 模型 Random pruning k=0.7 在 LIBERO-10 Long-horizon 上的性能评估\", \"retry_count\": 1, \"status\": \"ANALYZING\", \"updated_at\": \"2026-05-27T01:30:21.233Z\", \"parent\": \"eval_pi05_random_k075_long_seed42\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"elapsed_min\": 156.4, \"overall_sr\": 0.646, \"total_episodes\": 500, \"total_successes\": 323}}, \"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-27T01:29:45.378230+00:00\"}]}, \"spec\": {\"command\": \"python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.7 --suite libero_10 --n_episodes 50 --seed 42 --gpu 0\", \"server\": \"cqa1-33015\", \"gpu\": \"cuda:3\", \"pid\": 732826, \"data_path\": \"libero_10\", \"data_count\": 50, \"model_name\": \"pi0.5\", \"seed\": 42, \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_pi05_random_k07_long_seed42.log\", \"checkpoint_source\": \"pi0.5-base\", \"eval_data\": \"libero_10\"}, \"metrics\": {\"overall_sr\": 62.4, \"suite\": \"libero_10\", \"prune_method\": \"random\", \"keep_ratio\": 0.7, \"seed\": 42, \"episodes_per_task\": 50}, \"conclusion\": \"success\", \"reproduce\": {\"finished_at\": \"2026-05-27T01:29:24.236Z\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 18.9248}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "91b3d5c1-50da-4650-a87b-7ce4afd361f3",
  "uuid": "8c366057-ba9b-4b54-8a55-d369fd7ac400",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval_pi05_random_k07_long_seed42\\\", \\\"experiment\\\": {\\\"completed_at\\\": \\\"2026-05-22T21:54:17.624Z\\\", \\\"created_at\\\": \\\"2026-05-22T19:10:50.961Z\\\", \\\"hypothesis\\\": \\\"Pi0.5 Random k=0.7 Long seed42 — Pi0.5 模型 Random pruning k=0.7 在 LIBERO-10 Long-horizon 上的性能评估\\\", \\\"retry_count\\\": 1, \\\"status\\\": \\\"ANALYZING\\\", \\\"updated_at\\\": \\\"2026-05-27T01:30:21.233Z\\\", \\\"parent\\\": \\\"eval_pi05_random_k075_long_seed42\\\", \\\"extra\\\": {\\\"previous_failure\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"elapsed_min\\\": 156.4, \\\"overall_sr\\\": 0.646, \\\"total_episodes\\\": 500, \\\"total_successes\\\": 323}}, \\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-27T01:29:45.378230+00:00\\\"}]}, \\\"spec\\\": {\\\"command\\\": \\\"python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.7 --suite libero_10 --n_episodes 50 --seed 42 --gpu 0\\\", \\\"server\\\": \\\"cqa1-33015\\\", \\\"gpu\\\": \\\"cuda:3\\\", \\\"pid\\\": 732826, \\\"data_path\\\": \\\"libero_10\\\", \\\"data_count\\\": 50, \\\"model_name\\\": \\\"pi0.5\\\", \\\"seed\\\": 42, \\\"log_path\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_pi05_random_k07_long_seed42.log\\\", \\\"checkpoint_source\\\": \\\"pi0.5-base\\\", \\\"eval_data\\\": \\\"libero_10\\\"}, \\\"metrics\\\": {\\\"overall_sr\\\": 62.4, \\\"suite\\\": \\\"libero_10\\\", \\\"prune_method\\\": \\\"random\\\", \\\"keep_ratio\\\": 0.7, \\\"seed\\\": 42, \\\"episodes_per_task\\\": 50}, \\\"conclusion\\\": \\\"success\\\", \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-27T01:29:24.236Z\\\"}}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 18.9248}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval_pi05_random_k07_long_seed42\", \"experiment\": {\"completed_at\": \"2026-05-22T21:54:17.624Z\", \"created_at\": \"2026-05-22T19:10:50.961Z\", \"hypothesis\": \"Pi0.5 Random k=0.7 Long seed42 — Pi0.5 模型 Random pruning k=0.7 在 LIBERO-10 Long-horizon 上的性能评估\", \"retry_count\": 1, \"status\": \"ANALYZING\", \"updated_at\": \"2026-05-27T01:30:21.233Z\", \"parent\": \"eval_pi05_random_k075_long_seed42\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"elapsed_min\": 156.4, \"overall_sr\": 0.646, \"total_episodes\": 500, \"total_successes\": 323}}, \"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-27T01:29:45.378230+00:00\"}]}, \"spec\": {\"command\": \"python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.7 --suite libero_10 --n_episodes 50 --seed 42 --gpu 0\", \"server\": \"cqa1-33015\", \"gpu\": \"cuda:3\", \"pid\": 732826, \"data_path\": \"libero_10\", \"data_count\": 50, \"model_name\": \"pi0.5\", \"seed\": 42, \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_pi05_random_k07_long_seed42.log\", \"checkpoint_source\": \"pi0.5-base\", \"eval_data\": \"libero_10\"}, \"metrics\": {\"overall_sr\": 62.4, \"suite\": \"libero_10\", \"prune_method\": \"random\", \"keep_ratio\": 0.7, \"seed\": 42, \"episodes_per_task\": 50}, \"conclusion\": \"success\", \"reproduce\": {\"finished_at\": \"2026-05-27T01:29:24.236Z\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 18.9248}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 45 · 2026-05-27T01:30:43.623Z_

<details><summary>↩ Tool result · `toolu_01TwAPAQKxTV8zEBbNWH4qGB`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_openvla_random_k075_goal_seed42\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-27T01:30:34.626Z\", \"updated_at\": \"2026-05-27T01:30:40.365Z\", \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed (log check: no success markers found in log tail (path=/root/autodl-tmp/importance_margin_vla_compress/logs/eval_openvla_random_k075_goal_seed42.log))\", \"hypothesis\": \"OpenVLA Random k=0.75 Goal seed42 — Goal Random cliff curve 中间点。Random k=0.9=79.6%, k=0.85=78.6%, k=0.7=68.4%。k=0.75 精确定位 Goal Random 下降斜率\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 18.9469}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "91b3d5c1-50da-4650-a87b-7ce4afd361f3",
  "uuid": "44d3a4c7-c42b-4cab-9e73-8a484cfaae25",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval_openvla_random_k075_goal_seed42\\\", \\\"experiment\\\": {\\\"status\\\": \\\"PREPARING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-27T01:30:34.626Z\\\", \\\"updated_at\\\": \\\"2026-05-27T01:30:40.365Z\\\", \\\"failure_reason\\\": \\\"process dead 5× with no sentinel/W&B — auto-resolved as failed (log check: no success markers found in log tail (path=/root/autodl-tmp/importance_margin_vla_compress/logs/eval_openvla_random_k075_goal_seed42.log))\\\", \\\"hypothesis\\\": \\\"OpenVLA Random k=0.75 Goal seed42 — Goal Random cliff curve 中间点。Random k=0.9=79.6%, k=0.85=78.6%, k=0.7=68.4%。k=0.75 精确定位 Goal Random 下降斜率\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 18.9469}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval_openvla_random_k075_goal_seed42\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-27T01:30:34.626Z\", \"updated_at\": \"2026-05-27T01:30:40.365Z\", \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed (log check: no success markers found in log tail (path=/root/autodl-tmp/importance_margin_vla_compress/logs/eval_openvla_random_k075_goal_seed42.log))\", \"hypothesis\": \"OpenVLA Random k=0.75 Goal seed42 — Goal Random cliff curve 中间点。Random k=0.9=79.6%, k=0.85=78.6%, k=0.7=68.4%。k=0.75 精确定位 Goal Random 下降斜率\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 18.9469}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 46_

<details><summary>Logged reasoning block</summary>

```text
Interesting. So:
- (A) `eval_openvla_attn_k05_long_seed42` already existed in registry with status=DONE, conclusion=success, metrics already set. The hypothesis update was applied. The metrics already show overall_sr: 14.6.
- (B) `eval_pi05_random_k07_long_seed42` already existed with status=ANALYZING, conclusion=success. Metrics already show overall_sr: 62.4. This one seems to need status update to DONE.


- (C) `eval_openvla_random_k075_goal_seed42` was just created with status=PREPARING. This one needs all the setup.

Wait, but the initial registry query returned count=0 for all three! That's confusing. Maybe the filter on exp_id doesn't work like I expected. The experiments did exist, as evidenced by the update_registry finding them. So my plan is to update (A) which looks good already, transition (B) from ANALYZING to DONE, and set up (C) with its spec, log_path, and checkpoint_path before marking it DONE. Let me also double-check that the metrics are correct for (A).

For (A), the overall_sr of 14.6 matches the log data. For (B), the current metrics show 62.4% while the previous run had 64.6% — the new result is lower, so I'll update the status to DONE. For (C), I need to configure it with the proper metadata and then transition it to DONE as well.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "91b3d5c1-50da-4650-a87b-7ce4afd361f3",
  "uuid": "509ef41d-fdda-473e-86ad-6707802a185c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015KEf2Qfh5emvMCsVBhyTYu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3995,
      "cache_read_input_tokens": 41964,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3995
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Assistant

_source line 47_

实验 A 已是 DONE 状态（metrics 正确）。更新 B 状态为 DONE，并为 C 设置 spec 和完成状态。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "91b3d5c1-50da-4650-a87b-7ce4afd361f3",
  "uuid": "af397332-0e13-4f29-9b2d-d56197e523b0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015KEf2Qfh5emvMCsVBhyTYu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3995,
      "cache_read_input_tokens": 41964,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3995
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 48_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_016ox9teXs4UKZg2QStPQwKN`</summary>

```json
{
  "exp_id": "eval_pi05_random_k07_long_seed42",
  "field": "status",
  "value": "DONE",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "91b3d5c1-50da-4650-a87b-7ce4afd361f3",
  "uuid": "810dfe8f-20f0-474c-a835-accbc361fdfc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015KEf2Qfh5emvMCsVBhyTYu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3995,
      "cache_read_input_tokens": 41964,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3995
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 49_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_017EznPa9Doo3XXHWXeP4XbP`</summary>

```json
{
  "exp_id": "eval_openvla_random_k075_goal_seed42",
  "field": "status",
  "value": "RUNNING",
  "project": "importance_margin_vla_compress",
  "spec": {
    "command": "python3 eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.75 --suite libero_goal --num_episodes 50 --seed 42",
    "server": "westd-38929",
    "gpu": 3,
    "data_path": "libero_goal",
    "data_count": 500,
    "model_name": "openvla-7b-finetuned-libero-goal",
    "seed": 42,
    "checkpoint_path": "N/A (eval only)",
    "log_path": "/root/autodl-tmp/importance_margin_vla_compress/logs/eval_openvla_random_k075_goal_seed42.log",
    "checkpoint_source": "openvla-7b-finetuned-libero-goal",
    "eval_data": "libero_goal"
  }
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "91b3d5c1-50da-4650-a87b-7ce4afd361f3",
  "uuid": "b35b78e2-774e-4fbd-a9a9-00acce1124e6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015KEf2Qfh5emvMCsVBhyTYu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3995,
      "cache_read_input_tokens": 41964,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3995
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 50 · 2026-05-27T01:31:14.730Z_

<details><summary>↩ Tool result · `toolu_016ox9teXs4UKZg2QStPQwKN`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to DONE without output fields: ['checkpoint_path']. Set these fields first or pass them in spec.\", \"metadata\": {\"elapsed_seconds\": 15.5126}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "91b3d5c1-50da-4650-a87b-7ce4afd361f3",
  "uuid": "f79f6cf8-4662-4336-bc15-2e53f6bf1667",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"Cannot transition to DONE without output fields: ['checkpoint_path']. Set these fields first or pass them in spec.\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 15.5126}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to DONE without output fields: ['checkpoint_path']. Set these fields first or pass them in spec.\", \"metadata\": {\"elapsed_seconds\": 15.5126}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 51 · 2026-05-27T01:31:39.549Z_

<details><summary>↩ Tool result · `toolu_017EznPa9Doo3XXHWXeP4XbP`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 24.7904}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "91b3d5c1-50da-4650-a87b-7ce4afd361f3",
  "uuid": "ed46d21c-6b96-48d9-986a-96386fcbce2b",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 24.7904}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 24.7904}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 52_

<details><summary>Logged reasoning block</summary>

```text
Two issues:
1. B needs checkpoint_path set before DONE transition
2. C can't go from PREPARING to RUNNING - needs to go PREPARING → PENDING or QUEUED first

Let me fix both. For B, set checkpoint_path first. For C, let me try setting spec directly or changing status to PENDING first.

Actually wait - for B, the spec already has checkpoint_source but not checkpoint_path. Let me set the checkpoint_path field.

For C, the allowed transitions from PREPARING are PENDING or QUEUED. Let me set status to QUEUED, then RUNNING (with spec), then DONE.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "91b3d5c1-50da-4650-a87b-7ce4afd361f3",
  "uuid": "fa5674b7-2520-4b35-8e45-86e579219ea0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018s14BD1k4Zak5jQ76vM7rD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1345,
      "cache_read_input_tokens": 45959,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1345
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 53_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01BogMYaoiSTYrvMdNvfrzPC`</summary>

```json
{
  "exp_id": "eval_pi05_random_k07_long_seed42",
  "field": "spec",
  "value": {
    "command": "python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.7 --suite libero_10 --n_episodes 50 --seed 42 --gpu 0",
    "server": "cqa1-33015",
    "gpu": "cuda:3",
    "pid": 732826,
    "data_path": "libero_10",
    "data_count": 50,
    "model_name": "pi0.5",
    "seed": 42,
    "log_path": "/root/autodl-tmp/importance_margin_vla_compress/logs/eval_pi05_random_k07_long_seed42.log",
    "checkpoint_source": "pi0.5-base",
    "eval_data": "libero_10",
    "checkpoint_path": "N/A (eval only)"
  },
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "91b3d5c1-50da-4650-a87b-7ce4afd361f3",
  "uuid": "38367096-cadd-4189-86d0-665a1e15842f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018s14BD1k4Zak5jQ76vM7rD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1345,
      "cache_read_input_tokens": 45959,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1345
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 54_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01KxpiRtMEM3MgJq4w6k3cHQ`</summary>

```json
{
  "exp_id": "eval_openvla_random_k075_goal_seed42",
  "field": "status",
  "value": "QUEUED",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "91b3d5c1-50da-4650-a87b-7ce4afd361f3",
  "uuid": "e3334a94-0127-420e-b268-158588bd4261",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018s14BD1k4Zak5jQ76vM7rD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1345,
      "cache_read_input_tokens": 45959,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1345
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 55 · 2026-05-27T01:32:09.116Z_

<details><summary>↩ Tool result · `toolu_01BogMYaoiSTYrvMdNvfrzPC`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_pi05_random_k07_long_seed42\", \"experiment\": {\"completed_at\": \"2026-05-22T21:54:17.624Z\", \"created_at\": \"2026-05-22T19:10:50.961Z\", \"hypothesis\": \"Pi0.5 Random k=0.7 Long seed42 — Pi0.5 模型 Random pruning k=0.7 在 LIBERO-10 Long-horizon 上的性能评估\", \"retry_count\": 1, \"status\": \"ANALYZING\", \"updated_at\": \"2026-05-27T01:32:06.392Z\", \"parent\": \"eval_pi05_random_k075_long_seed42\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"elapsed_min\": 156.4, \"overall_sr\": 0.646, \"total_episodes\": 500, \"total_successes\": 323}}, \"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-27T01:29:45.378230+00:00\"}]}, \"spec\": {\"command\": \"python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.7 --suite libero_10 --n_episodes 50 --seed 42 --gpu 0\", \"server\": \"cqa1-33015\", \"gpu\": \"cuda:3\", \"pid\": 732826, \"data_path\": \"libero_10\", \"data_count\": 50, \"model_name\": \"pi0.5\", \"seed\": 42, \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_pi05_random_k07_long_seed42.log\", \"checkpoint_source\": \"pi0.5-base\", \"eval_data\": \"libero_10\", \"checkpoint_path\": \"N/A (eval only)\"}, \"metrics\": {\"overall_sr\": 62.4, \"suite\": \"libero_10\", \"prune_method\": \"random\", \"keep_ratio\": 0.7, \"seed\": 42, \"episodes_per_task\": 50}, \"conclusion\": \"success\", \"reproduce\": {\"finished_at\": \"2026-05-27T01:29:24.236Z\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 19.5037}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "91b3d5c1-50da-4650-a87b-7ce4afd361f3",
  "uuid": "fd2ed5b6-5c65-4987-814d-b45a0bf1f3d2",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval_pi05_random_k07_long_seed42\\\", \\\"experiment\\\": {\\\"completed_at\\\": \\\"2026-05-22T21:54:17.624Z\\\", \\\"created_at\\\": \\\"2026-05-22T19:10:50.961Z\\\", \\\"hypothesis\\\": \\\"Pi0.5 Random k=0.7 Long seed42 — Pi0.5 模型 Random pruning k=0.7 在 LIBERO-10 Long-horizon 上的性能评估\\\", \\\"retry_count\\\": 1, \\\"status\\\": \\\"ANALYZING\\\", \\\"updated_at\\\": \\\"2026-05-27T01:32:06.392Z\\\", \\\"parent\\\": \\\"eval_pi05_random_k075_long_seed42\\\", \\\"extra\\\": {\\\"previous_failure\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"elapsed_min\\\": 156.4, \\\"overall_sr\\\": 0.646, \\\"total_episodes\\\": 500, \\\"total_successes\\\": 323}}, \\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-27T01:29:45.378230+00:00\\\"}]}, \\\"spec\\\": {\\\"command\\\": \\\"python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.7 --suite libero_10 --n_episodes 50 --seed 42 --gpu 0\\\", \\\"server\\\": \\\"cqa1-33015\\\", \\\"gpu\\\": \\\"cuda:3\\\", \\\"pid\\\": 732826, \\\"data_path\\\": \\\"libero_10\\\", \\\"data_count\\\": 50, \\\"model_name\\\": \\\"pi0.5\\\", \\\"seed\\\": 42, \\\"log_path\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_pi05_random_k07_long_seed42.log\\\", \\\"checkpoint_source\\\": \\\"pi0.5-base\\\", \\\"eval_data\\\": \\\"libero_10\\\", \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\"}, \\\"metrics\\\": {\\\"overall_sr\\\": 62.4, \\\"suite\\\": \\\"libero_10\\\", \\\"prune_method\\\": \\\"random\\\", \\\"keep_ratio\\\": 0.7, \\\"seed\\\": 42, \\\"episodes_per_task\\\": 50}, \\\"conclusion\\\": \\\"success\\\", \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-27T01:29:24.236Z\\\"}}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 19.5037}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval_pi05_random_k07_long_seed42\", \"experiment\": {\"completed_at\": \"2026-05-22T21:54:17.624Z\", \"created_at\": \"2026-05-22T19:10:50.961Z\", \"hypothesis\": \"Pi0.5 Random k=0.7 Long seed42 — Pi0.5 模型 Random pruning k=0.7 在 LIBERO-10 Long-horizon 上的性能评估\", \"retry_count\": 1, \"status\": \"ANALYZING\", \"updated_at\": \"2026-05-27T01:32:06.392Z\", \"parent\": \"eval_pi05_random_k075_long_seed42\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"elapsed_min\": 156.4, \"overall_sr\": 0.646, \"total_episodes\": 500, \"total_successes\": 323}}, \"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-27T01:29:45.378230+00:00\"}]}, \"spec\": {\"command\": \"python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.7 --suite libero_10 --n_episodes 50 --seed 42 --gpu 0\", \"server\": \"cqa1-33015\", \"gpu\": \"cuda:3\", \"pid\": 732826, \"data_path\": \"libero_10\", \"data_count\": 50, \"model_name\": \"pi0.5\", \"seed\": 42, \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_pi05_random_k07_long_seed42.log\", \"checkpoint_source\": \"pi0.5-base\", \"eval_data\": \"libero_10\", \"checkpoint_path\": \"N/A (eval only)\"}, \"metrics\": {\"overall_sr\": 62.4, \"suite\": \"libero_10\", \"prune_method\": \"random\", \"keep_ratio\": 0.7, \"seed\": 42, \"episodes_per_task\": 50}, \"conclusion\": \"success\", \"reproduce\": {\"finished_at\": \"2026-05-27T01:29:24.236Z\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 19.5037}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 56 · 2026-05-27T01:32:38.677Z_

<details><summary>↩ Tool result · `toolu_01KxpiRtMEM3MgJq4w6k3cHQ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_openvla_random_k075_goal_seed42\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-27T01:30:34.626Z\", \"updated_at\": \"2026-05-27T01:32:26.381Z\", \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed (log check: no success markers found in log tail (path=/root/autodl-tmp/importance_margin_vla_compress/logs/eval_openvla_random_k075_goal_seed42.log))\", \"hypothesis\": \"OpenVLA Random k=0.75 Goal seed42 — Goal Random cliff curve 中间点。Random k=0.9=79.6%, k=0.85=78.6%, k=0.7=68.4%。k=0.75 精确定位 Goal Random 下降斜率\", \"conclusion\": \"failed\", \"reproduce\": {\"finished_at\": \"2026-05-27T01:31:49.165Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-27T01:31:33.981349+00:00\"}]}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 29.5331}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "91b3d5c1-50da-4650-a87b-7ce4afd361f3",
  "uuid": "5f1c2643-8aab-4a69-adb0-a4aaa6a34ee8",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval_openvla_random_k075_goal_seed42\\\", \\\"experiment\\\": {\\\"status\\\": \\\"QUEUED\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-27T01:30:34.626Z\\\", \\\"updated_at\\\": \\\"2026-05-27T01:32:26.381Z\\\", \\\"failure_reason\\\": \\\"process dead 5× with no sentinel/W&B — auto-resolved as failed (log check: no success markers found in log tail (path=/root/autodl-tmp/importance_margin_vla_compress/logs/eval_openvla_random_k075_goal_seed42.log))\\\", \\\"hypothesis\\\": \\\"OpenVLA Random k=0.75 Goal seed42 — Goal Random cliff curve 中间点。Random k=0.9=79.6%, k=0.85=78.6%, k=0.7=68.4%。k=0.75 精确定位 Goal Random 下降斜率\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-27T01:31:49.165Z\\\"}, \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_failed\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-27T01:31:33.981349+00:00\\\"}]}}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 29.5331}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval_openvla_random_k075_goal_seed42\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-27T01:30:34.626Z\", \"updated_at\": \"2026-05-27T01:32:26.381Z\", \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed (log check: no success markers found in log tail (path=/root/autodl-tmp/importance_margin_vla_compress/logs/eval_openvla_random_k075_goal_seed42.log))\", \"hypothesis\": \"OpenVLA Random k=0.75 Goal seed42 — Goal Random cliff curve 中间点。Random k=0.9=79.6%, k=0.85=78.6%, k=0.7=68.4%。k=0.75 精确定位 Goal Random 下降斜率\", \"conclusion\": \"failed\", \"reproduce\": {\"finished_at\": \"2026-05-27T01:31:49.165Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-27T01:31:33.981349+00:00\"}]}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 29.5331}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 57_

<details><summary>Logged reasoning block</summary>

```text
OK, so:
- B is now at ANALYZING with spec including checkpoint_path. Let me try transitioning to DONE again.
- C is now at QUEUED. Let me transition to RUNNING with spec, then to DONE.

Let me proceed with both.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "91b3d5c1-50da-4650-a87b-7ce4afd361f3",
  "uuid": "b9ea4056-fd0e-4563-9cdb-2ab0db9c4711",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GuQGBc5JSSKSts5uk2YmHx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1768,
      "cache_read_input_tokens": 47304,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1768
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 58_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01CFwa44Pv8zgeSNRvihUkou`</summary>

```json
{
  "exp_id": "eval_pi05_random_k07_long_seed42",
  "field": "status",
  "value": "DONE",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "91b3d5c1-50da-4650-a87b-7ce4afd361f3",
  "uuid": "97f15eee-d71d-46ef-9205-4f096352a0ce",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GuQGBc5JSSKSts5uk2YmHx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1768,
      "cache_read_input_tokens": 47304,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1768
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 59_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01PjkGToSbxzYa1eDQ356ehg`</summary>

```json
{
  "exp_id": "eval_openvla_random_k075_goal_seed42",
  "field": "status",
  "value": "RUNNING",
  "project": "importance_margin_vla_compress",
  "spec": {
    "command": "python3 eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.75 --suite libero_goal --num_episodes 50 --seed 42",
    "server": "westd-38929",
    "gpu": 3,
    "data_path": "libero_goal",
    "data_count": 500,
    "model_name": "openvla-7b-finetuned-libero-goal",
    "seed": 42,
    "checkpoint_path": "N/A (eval only)",
    "log_path": "/root/autodl-tmp/importance_margin_vla_compress/logs/eval_openvla_random_k075_goal_seed42.log",
    "checkpoint_source": "openvla-7b-finetuned-libero-goal",
    "eval_data": "libero_goal"
  }
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "91b3d5c1-50da-4650-a87b-7ce4afd361f3",
  "uuid": "de1dfc6a-9e61-4820-ba96-dd25616d955c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GuQGBc5JSSKSts5uk2YmHx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1768,
      "cache_read_input_tokens": 47304,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1768
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 60 · 2026-05-27T01:33:38.206Z_

<details><summary>↩ Tool result · `toolu_01CFwa44Pv8zgeSNRvihUkou`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_pi05_random_k07_long_seed42\", \"experiment\": {\"completed_at\": \"2026-05-22T21:54:17.624Z\", \"created_at\": \"2026-05-22T19:10:50.961Z\", \"hypothesis\": \"Pi0.5 Random k=0.7 Long seed42 — Pi0.5 模型 Random pruning k=0.7 在 LIBERO-10 Long-horizon 上的性能评估\", \"retry_count\": 1, \"status\": \"DONE\", \"updated_at\": \"2026-05-27T01:33:31.426Z\", \"parent\": \"eval_pi05_random_k075_long_seed42\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"elapsed_min\": 156.4, \"overall_sr\": 0.646, \"total_episodes\": 500, \"total_successes\": 323}}, \"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-27T01:29:45.378230+00:00\"}]}, \"spec\": {\"command\": \"python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.7 --suite libero_10 --n_episodes 50 --seed 42 --gpu 0\", \"server\": \"cqa1-33015\", \"gpu\": \"cuda:3\", \"pid\": 732826, \"data_path\": \"libero_10\", \"data_count\": 50, \"model_name\": \"pi0.5\", \"seed\": 42, \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_pi05_random_k07_long_seed42.log\", \"checkpoint_source\": \"pi0.5-base\", \"eval_data\": \"libero_10\", \"checkpoint_path\": \"N/A (eval only)\"}, \"metrics\": {\"overall_sr\": 62.4, \"suite\": \"libero_10\", \"prune_method\": \"random\", \"keep_ratio\": 0.7, \"seed\": 42, \"episodes_per_task\": 50}, \"conclusion\": \"success\", \"reproduce\": {\"finished_at\": \"2026-05-27T01:29:24.236Z\"}}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 54.106}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "91b3d5c1-50da-4650-a87b-7ce4afd361f3",
  "uuid": "d528b68c-15ec-46f6-af74-e43771923b17",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval_pi05_random_k07_long_seed42\\\", \\\"experiment\\\": {\\\"completed_at\\\": \\\"2026-05-22T21:54:17.624Z\\\", \\\"created_at\\\": \\\"2026-05-22T19:10:50.961Z\\\", \\\"hypothesis\\\": \\\"Pi0.5 Random k=0.7 Long seed42 — Pi0.5 模型 Random pruning k=0.7 在 LIBERO-10 Long-horizon 上的性能评估\\\", \\\"retry_count\\\": 1, \\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-27T01:33:31.426Z\\\", \\\"parent\\\": \\\"eval_pi05_random_k075_long_seed42\\\", \\\"extra\\\": {\\\"previous_failure\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"elapsed_min\\\": 156.4, \\\"overall_sr\\\": 0.646, \\\"total_episodes\\\": 500, \\\"total_successes\\\": 323}}, \\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-27T01:29:45.378230+00:00\\\"}]}, \\\"spec\\\": {\\\"command\\\": \\\"python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.7 --suite libero_10 --n_episodes 50 --seed 42 --gpu 0\\\", \\\"server\\\": \\\"cqa1-33015\\\", \\\"gpu\\\": \\\"cuda:3\\\", \\\"pid\\\": 732826, \\\"data_path\\\": \\\"libero_10\\\", \\\"data_count\\\": 50, \\\"model_name\\\": \\\"pi0.5\\\", \\\"seed\\\": 42, \\\"log_path\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_pi05_random_k07_long_seed42.log\\\", \\\"checkpoint_source\\\": \\\"pi0.5-base\\\", \\\"eval_data\\\": \\\"libero_10\\\", \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\"}, \\\"metrics\\\": {\\\"overall_sr\\\": 62.4, \\\"suite\\\": \\\"libero_10\\\", \\\"prune_method\\\": \\\"random\\\", \\\"keep_ratio\\\": 0.7, \\\"seed\\\": 42, \\\"episodes_per_task\\\": 50}, \\\"conclusion\\\": \\\"success\\\", \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-27T01:29:24.236Z\\\"}}, \\\"hint\\\": \\\"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\\\"}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 54.106}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval_pi05_random_k07_long_seed42\", \"experiment\": {\"completed_at\": \"2026-05-22T21:54:17.624Z\", \"created_at\": \"2026-05-22T19:10:50.961Z\", \"hypothesis\": \"Pi0.5 Random k=0.7 Long seed42 — Pi0.5 模型 Random pruning k=0.7 在 LIBERO-10 Long-horizon 上的性能评估\", \"retry_count\": 1, \"status\": \"DONE\", \"updated_at\": \"2026-05-27T01:33:31.426Z\", \"parent\": \"eval_pi05_random_k075_long_seed42\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"elapsed_min\": 156.4, \"overall_sr\": 0.646, \"total_episodes\": 500, \"total_successes\": 323}}, \"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-27T01:29:45.378230+00:00\"}]}, \"spec\": {\"command\": \"python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.7 --suite libero_10 --n_episodes 50 --seed 42 --gpu 0\", \"server\": \"cqa1-33015\", \"gpu\": \"cuda:3\", \"pid\": 732826, \"data_path\": \"libero_10\", \"data_count\": 50, \"model_name\": \"pi0.5\", \"seed\": 42, \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_pi05_random_k07_long_seed42.log\", \"checkpoint_source\": \"pi0.5-base\", \"eval_data\": \"libero_10\", \"checkpoint_path\": \"N/A (eval only)\"}, \"metrics\": {\"overall_sr\": 62.4, \"suite\": \"libero_10\", \"prune_method\": \"random\", \"keep_ratio\": 0.7, \"seed\": 42, \"episodes_per_task\": 50}, \"conclusion\": \"success\", \"reproduce\": {\"finished_at\": \"2026-05-27T01:29:24.236Z\"}}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 54.106}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 61 · 2026-05-27T01:34:09.139Z_

<details><summary>↩ Tool result · `toolu_01PjkGToSbxzYa1eDQ356ehg`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: DONE → RUNNING. Allowed: ['DEPLOYING', 'PREPARING']\", \"metadata\": {\"elapsed_seconds\": 30.8989}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "91b3d5c1-50da-4650-a87b-7ce4afd361f3",
  "uuid": "6d63ec30-7c26-410a-9229-ff10739f58ac",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"Invalid transition: DONE → RUNNING. Allowed: ['DEPLOYING', 'PREPARING']\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 30.8989}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: DONE → RUNNING. Allowed: ['DEPLOYING', 'PREPARING']\", \"metadata\": {\"elapsed_seconds\": 30.8989}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 62_

<details><summary>Logged reasoning block</summary>

```text
OK so experiment C had a weird state - it was created new with status PREPARING, but then when transitioning to QUEUED, it seems it was already marked as DONE by some hook. Wait, the error says "Invalid transition: DONE → RUNNING". So somehow it's already DONE.

Let me check its current state. Maybe it was auto-resolved by the hook system. Let me just update its conclusion and metrics directly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "91b3d5c1-50da-4650-a87b-7ce4afd361f3",
  "uuid": "5fd959ab-8d90-4c7d-9d12-5de8e32b8cd8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SDLgqpMYwJyLAobGCMsw21",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1419,
      "cache_read_input_tokens": 49072,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1419
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Assistant

_source line 63_

B 已 DONE。C 似乎已被系统自动标记为 DONE，直接更新 conclusion 和 metrics。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "91b3d5c1-50da-4650-a87b-7ce4afd361f3",
  "uuid": "3007da66-232a-4cbe-82f1-e9ad45e3fe41",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SDLgqpMYwJyLAobGCMsw21",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1419,
      "cache_read_input_tokens": 49072,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1419
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 64_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01F3zKmBZJdhaQiNmVm48Gza`</summary>

```json
{
  "exp_id": "eval_openvla_random_k075_goal_seed42",
  "field": "conclusion",
  "value": "success",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "91b3d5c1-50da-4650-a87b-7ce4afd361f3",
  "uuid": "bec324a7-16df-4156-864d-3f6c347b5657",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SDLgqpMYwJyLAobGCMsw21",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1419,
      "cache_read_input_tokens": 49072,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1419
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 65 · 2026-05-27T01:34:32.406Z_

<details><summary>↩ Tool result · `toolu_01F3zKmBZJdhaQiNmVm48Gza`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_openvla_random_k075_goal_seed42\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-27T01:30:34.626Z\", \"updated_at\": \"2026-05-27T01:34:28.489Z\", \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed (log check: no success markers found in log tail (path=/root/autodl-tmp/importance_margin_vla_compress/logs/eval_openvla_random_k075_goal_seed42.log))\", \"hypothesis\": \"OpenVLA Random k=0.75 Goal seed42 — Goal Random cliff curve 中间点。Random k=0.9=79.6%, k=0.85=78.6%, k=0.7=68.4%。k=0.75 精确定位 Goal Random 下降斜率\", \"conclusion\": \"success\", \"reproduce\": {\"finished_at\": \"2026-05-27T01:31:49.165Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-27T01:31:33.981349+00:00\"}]}, \"completed_at\": \"2026-05-27T01:32:47.595Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 12.4518}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "91b3d5c1-50da-4650-a87b-7ce4afd361f3",
  "uuid": "64d6d298-9fcd-4dab-b40d-cea90553fa90",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval_openvla_random_k075_goal_seed42\\\", \\\"experiment\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-27T01:30:34.626Z\\\", \\\"updated_at\\\": \\\"2026-05-27T01:34:28.489Z\\\", \\\"failure_reason\\\": \\\"process dead 5× with no sentinel/W&B — auto-resolved as failed (log check: no success markers found in log tail (path=/root/autodl-tmp/importance_margin_vla_compress/logs/eval_openvla_random_k075_goal_seed42.log))\\\", \\\"hypothesis\\\": \\\"OpenVLA Random k=0.75 Goal seed42 — Goal Random cliff curve 中间点。Random k=0.9=79.6%, k=0.85=78.6%, k=0.7=68.4%。k=0.75 精确定位 Goal Random 下降斜率\\\", \\\"conclusion\\\": \\\"success\\\", \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-27T01:31:49.165Z\\\"}, \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_failed\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-27T01:31:33.981349+00:00\\\"}]}, \\\"completed_at\\\": \\\"2026-05-27T01:32:47.595Z\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 12.4518}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval_openvla_random_k075_goal_seed42\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-27T01:30:34.626Z\", \"updated_at\": \"2026-05-27T01:34:28.489Z\", \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed (log check: no success markers found in log tail (path=/root/autodl-tmp/importance_margin_vla_compress/logs/eval_openvla_random_k075_goal_seed42.log))\", \"hypothesis\": \"OpenVLA Random k=0.75 Goal seed42 — Goal Random cliff curve 中间点。Random k=0.9=79.6%, k=0.85=78.6%, k=0.7=68.4%。k=0.75 精确定位 Goal Random 下降斜率\", \"conclusion\": \"success\", \"reproduce\": {\"finished_at\": \"2026-05-27T01:31:49.165Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-27T01:31:33.981349+00:00\"}]}, \"completed_at\": \"2026-05-27T01:32:47.595Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 12.4518}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 66_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_013qUxFdLLiX1sJHNiesDP5F`</summary>

```json
{
  "exp_id": "eval_openvla_random_k075_goal_seed42",
  "field": "metrics",
  "value": {
    "overall_sr": 72,
    "suite": "libero_goal",
    "prune_method": "random",
    "keep_ratio": 0.75,
    "seed": 42,
    "episodes_per_task": 50
  },
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "91b3d5c1-50da-4650-a87b-7ce4afd361f3",
  "uuid": "2bd4ccac-b414-4b10-8fa3-b664d602f7b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TYyiyHoXb6b71weDoh17XF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 706,
      "cache_read_input_tokens": 50491,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 706
      },
      "output_tokens": 69,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 67_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_012LFuU2ximbjTcb7kJzU6cF`</summary>

```json
{
  "exp_id": "eval_openvla_random_k075_goal_seed42",
  "field": "spec",
  "value": {
    "command": "python3 eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.75 --suite libero_goal --num_episodes 50 --seed 42",
    "server": "westd-38929",
    "gpu": 3,
    "data_path": "libero_goal",
    "data_count": 500,
    "model_name": "openvla-7b-finetuned-libero-goal",
    "seed": 42,
    "checkpoint_path": "N/A (eval only)",
    "log_path": "/root/autodl-tmp/importance_margin_vla_compress/logs/eval_openvla_random_k075_goal_seed42.log",
    "checkpoint_source": "openvla-7b-finetuned-libero-goal",
    "eval_data": "libero_goal"
  },
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "91b3d5c1-50da-4650-a87b-7ce4afd361f3",
  "uuid": "04fbf9da-97ab-45eb-9589-3abe0c98da2b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TYyiyHoXb6b71weDoh17XF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 706,
      "cache_read_input_tokens": 50491,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 706
      },
      "output_tokens": 69,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 68 · 2026-05-27T01:34:47.489Z_

<details><summary>↩ Tool result · `toolu_013qUxFdLLiX1sJHNiesDP5F`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_openvla_random_k075_goal_seed42\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-27T01:30:34.626Z\", \"updated_at\": \"2026-05-27T01:34:45.691Z\", \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed (log check: no success markers found in log tail (path=/root/autodl-tmp/importance_margin_vla_compress/logs/eval_openvla_random_k075_goal_seed42.log))\", \"hypothesis\": \"OpenVLA Random k=0.75 Goal seed42 — Goal Random cliff curve 中间点。Random k=0.9=79.6%, k=0.85=78.6%, k=0.7=68.4%。k=0.75 精确定位 Goal Random 下降斜率\", \"conclusion\": \"success\", \"reproduce\": {\"finished_at\": \"2026-05-27T01:31:49.165Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-27T01:31:33.981349+00:00\"}]}, \"completed_at\": \"2026-05-27T01:32:47.595Z\", \"metrics\": {\"overall_sr\": 72, \"suite\": \"libero_goal\", \"prune_method\": \"random\", \"keep_ratio\": 0.75, \"seed\": 42, \"episodes_per_task\": 50}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 10.6645}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "91b3d5c1-50da-4650-a87b-7ce4afd361f3",
  "uuid": "abf1bbf2-1b0f-4a21-a2a6-be4c5d896dd9",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval_openvla_random_k075_goal_seed42\\\", \\\"experiment\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-27T01:30:34.626Z\\\", \\\"updated_at\\\": \\\"2026-05-27T01:34:45.691Z\\\", \\\"failure_reason\\\": \\\"process dead 5× with no sentinel/W&B — auto-resolved as failed (log check: no success markers found in log tail (path=/root/autodl-tmp/importance_margin_vla_compress/logs/eval_openvla_random_k075_goal_seed42.log))\\\", \\\"hypothesis\\\": \\\"OpenVLA Random k=0.75 Goal seed42 — Goal Random cliff curve 中间点。Random k=0.9=79.6%, k=0.85=78.6%, k=0.7=68.4%。k=0.75 精确定位 Goal Random 下降斜率\\\", \\\"conclusion\\\": \\\"success\\\", \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-27T01:31:49.165Z\\\"}, \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_failed\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-27T01:31:33.981349+00:00\\\"}]}, \\\"completed_at\\\": \\\"2026-05-27T01:32:47.595Z\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 72, \\\"suite\\\": \\\"libero_goal\\\", \\\"prune_method\\\": \\\"random\\\", \\\"keep_ratio\\\": 0.75, \\\"seed\\\": 42, \\\"episodes_per_task\\\": 50}}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 10.6645}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval_openvla_random_k075_goal_seed42\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-27T01:30:34.626Z\", \"updated_at\": \"2026-05-27T01:34:45.691Z\", \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed (log check: no success markers found in log tail (path=/root/autodl-tmp/importance_margin_vla_compress/logs/eval_openvla_random_k075_goal_seed42.log))\", \"hypothesis\": \"OpenVLA Random k=0.75 Goal seed42 — Goal Random cliff curve 中间点。Random k=0.9=79.6%, k=0.85=78.6%, k=0.7=68.4%。k=0.75 精确定位 Goal Random 下降斜率\", \"conclusion\": \"success\", \"reproduce\": {\"finished_at\": \"2026-05-27T01:31:49.165Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-27T01:31:33.981349+00:00\"}]}, \"completed_at\": \"2026-05-27T01:32:47.595Z\", \"metrics\": {\"overall_sr\": 72, \"suite\": \"libero_goal\", \"prune_method\": \"random\", \"keep_ratio\": 0.75, \"seed\": 42, \"episodes_per_task\": 50}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 10.6645}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 69 · 2026-05-27T01:35:11.445Z_

<details><summary>↩ Tool result · `toolu_012LFuU2ximbjTcb7kJzU6cF`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_openvla_random_k075_goal_seed42\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-27T01:30:34.626Z\", \"updated_at\": \"2026-05-27T01:35:07.808Z\", \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed (log check: no success markers found in log tail (path=/root/autodl-tmp/importance_margin_vla_compress/logs/eval_openvla_random_k075_goal_seed42.log))\", \"hypothesis\": \"OpenVLA Random k=0.75 Goal seed42 — Goal Random cliff curve 中间点。Random k=0.9=79.6%, k=0.85=78.6%, k=0.7=68.4%。k=0.75 精确定位 Goal Random 下降斜率\", \"conclusion\": \"success\", \"reproduce\": {\"finished_at\": \"2026-05-27T01:31:49.165Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-27T01:31:33.981349+00:00\"}]}, \"completed_at\": \"2026-05-27T01:32:47.595Z\", \"metrics\": {\"overall_sr\": 72, \"suite\": \"libero_goal\", \"prune_method\": \"random\", \"keep_ratio\": 0.75, \"seed\": 42, \"episodes_per_task\": 50}, \"spec\": {\"command\": \"python3 eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.75 --suite libero_goal --num_episodes 50 --seed 42\", \"server\": \"westd-38929\", \"gpu\": 3, \"data_path\": \"libero_goal\", \"data_count\": 500, \"model_name\": \"openvla-7b-finetuned-libero-goal\", \"seed\": 42, \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_openvla_random_k075_goal_seed42.log\", \"checkpoint_source\": \"openvla-7b-finetuned-libero-goal\", \"eval_data\": \"libero_goal\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 23.9274}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "91b3d5c1-50da-4650-a87b-7ce4afd361f3",
  "uuid": "d30c6458-30b2-46e6-8868-48000f29bc5a",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval_openvla_random_k075_goal_seed42\\\", \\\"experiment\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-27T01:30:34.626Z\\\", \\\"updated_at\\\": \\\"2026-05-27T01:35:07.808Z\\\", \\\"failure_reason\\\": \\\"process dead 5× with no sentinel/W&B — auto-resolved as failed (log check: no success markers found in log tail (path=/root/autodl-tmp/importance_margin_vla_compress/logs/eval_openvla_random_k075_goal_seed42.log))\\\", \\\"hypothesis\\\": \\\"OpenVLA Random k=0.75 Goal seed42 — Goal Random cliff curve 中间点。Random k=0.9=79.6%, k=0.85=78.6%, k=0.7=68.4%。k=0.75 精确定位 Goal Random 下降斜率\\\", \\\"conclusion\\\": \\\"success\\\", \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-27T01:31:49.165Z\\\"}, \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_failed\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-27T01:31:33.981349+00:00\\\"}]}, \\\"completed_at\\\": \\\"2026-05-27T01:32:47.595Z\\\", \\\"metrics\\\": {\\\"overall_sr\\\": 72, \\\"suite\\\": \\\"libero_goal\\\", \\\"prune_method\\\": \\\"random\\\", \\\"keep_ratio\\\": 0.75, \\\"seed\\\": 42, \\\"episodes_per_task\\\": 50}, \\\"spec\\\": {\\\"command\\\": \\\"python3 eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.75 --suite libero_goal --num_episodes 50 --seed 42\\\", \\\"server\\\": \\\"westd-38929\\\", \\\"gpu\\\": 3, \\\"data_path\\\": \\\"libero_goal\\\", \\\"data_count\\\": 500, \\\"model_name\\\": \\\"openvla-7b-finetuned-libero-goal\\\", \\\"seed\\\": 42, \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_openvla_random_k075_goal_seed42.log\\\", \\\"checkpoint_source\\\": \\\"openvla-7b-finetuned-libero-goal\\\", \\\"eval_data\\\": \\\"libero_goal\\\"}}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 23.9274}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval_openvla_random_k075_goal_seed42\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-27T01:30:34.626Z\", \"updated_at\": \"2026-05-27T01:35:07.808Z\", \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed (log check: no success markers found in log tail (path=/root/autodl-tmp/importance_margin_vla_compress/logs/eval_openvla_random_k075_goal_seed42.log))\", \"hypothesis\": \"OpenVLA Random k=0.75 Goal seed42 — Goal Random cliff curve 中间点。Random k=0.9=79.6%, k=0.85=78.6%, k=0.7=68.4%。k=0.75 精确定位 Goal Random 下降斜率\", \"conclusion\": \"success\", \"reproduce\": {\"finished_at\": \"2026-05-27T01:31:49.165Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-27T01:31:33.981349+00:00\"}]}, \"completed_at\": \"2026-05-27T01:32:47.595Z\", \"metrics\": {\"overall_sr\": 72, \"suite\": \"libero_goal\", \"prune_method\": \"random\", \"keep_ratio\": 0.75, \"seed\": 42, \"episodes_per_task\": 50}, \"spec\": {\"command\": \"python3 eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.75 --suite libero_goal --num_episodes 50 --seed 42\", \"server\": \"westd-38929\", \"gpu\": 3, \"data_path\": \"libero_goal\", \"data_count\": 500, \"model_name\": \"openvla-7b-finetuned-libero-goal\", \"seed\": 42, \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_openvla_random_k075_goal_seed42.log\", \"checkpoint_source\": \"openvla-7b-finetuned-libero-goal\", \"eval_data\": \"libero_goal\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 23.9274}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 70_

<details><summary>Logged reasoning block</summary>

```text
All 3 experiments are now registered and marked as DONE with correct metrics. 

Now for task 2: I need to check and register the running experiments that aren't in the registry. From the ps output, I identified these running experiments:

**westd-27271:**
1. `eval_openvla_attn_k07_long_seed42_v2` - GPU 0, attention_prune k=0.7, libero_10
2. `eval_openvla_l2norm_k075_long_seed42` - GPU 2, l2norm_prune k=0.75, libero_10


3. `eval_openvla_l2norm_k095_long_seed42` - GPU 1, l2norm_prune k=0.95, libero_10
4. `eval_openvla_attn_k095_long_seed42` - GPU 3, attention_prune k=0.95, libero_10

**westd-41074:**
1. `eval_openvla_random_k05_object_seed42_v2` - GPU 0, random_prune k=0.5, libero_object
2. `eval_openvla_random_k095_long_seed42` - continuing on this host as well with random pruning at k=0.95 on the long task, plus attention pruning at k=0.75 on GPU 3, random pruning at k=0.75 on GPU 1, and another random pruning variant at k=0.95 for the object task on GPU 2. Over on **westd-38929**, I'm running l2norm pruning with k=0.9 on the goal task with seed 43, though that one's in tmux and might need checking.

Now I need to verify which of these experiments are already registered and currently running, so I'm querying the registry specifically for RUNNING status to avoid duplicates.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "91b3d5c1-50da-4650-a87b-7ce4afd361f3",
  "uuid": "747d705a-b944-4b72-8bd6-7786586fcf71",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016DDBYcQ1q3pg41R8ZzWJeZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1780,
      "cache_read_input_tokens": 51197,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1780
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Assistant

_source line 71_

三个实验已全部收割完毕。现在执行任务 2 — 查找未注册的运行实验。查询 registry 中 RUNNING 状态的实验。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "91b3d5c1-50da-4650-a87b-7ce4afd361f3",
  "uuid": "4ce1d36c-6ddf-4373-bad7-b67b985d16fb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016DDBYcQ1q3pg41R8ZzWJeZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1780,
      "cache_read_input_tokens": 51197,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1780
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 72_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01JmdJJ5jd3UfiF2Qz4YVAyM`</summary>

```json
{
  "project": "importance_margin_vla_compress",
  "filters": {
    "status": "RUNNING"
  },
  "fields": [
    "exp_id",
    "status",
    "spec"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "91b3d5c1-50da-4650-a87b-7ce4afd361f3",
  "uuid": "ff238799-a5cc-4e5c-bf2b-da28f26502c7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016DDBYcQ1q3pg41R8ZzWJeZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1780,
      "cache_read_input_tokens": 51197,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1780
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 73 · 2026-05-27T01:35:31.551Z_

<details><summary>↩ Tool result · `toolu_01JmdJJ5jd3UfiF2Qz4YVAyM`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval_openvla_attn_k095_object_seed42\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && python -u eval_openvla_l2norm_libero.py --mode attention_prune --k_ratio 0.95 --suite libero_object --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/openvla-libero-object --unnorm_key libero_object --gpu 1\\\"\", \"server\": \"westd-27271\", \"gpu\": [\"cuda:1\"], \"pid\": \"638220\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_attn_k095_object_seed42.log\", \"submitted_at\": \"2026-05-27T01:32:06.124Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval_openvla_random_k095_goal_seed42\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.95 --suite libero_goal\", \"server\": \"cqa1-33015\", \"gpu\": [\"cuda:3\"], \"pid\": \"876792\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_random_k095_goal_seed42.log\", \"submitted_at\": \"2026-05-27T01:12:17.909Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"openvla-libero-goal\", \"seed\": 42, \"data_path\": \"libero_goal\", \"data_count\": 500}}, \"eval_openvla_attn_k095_long_seed42\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u eval_openvla_l2norm_libero.py --mode attention_prune --k_ratio 0.95 --suite libero_10\", \"server\": \"westd-38929\", \"gpu\": [\"cuda:3\"], \"pid\": \"949998\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_attn_k095_long_seed42.log\", \"submitted_at\": \"2026-05-27T01:12:07.677Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"openvla-7b-finetuned-libero-10\", \"seed\": 42, \"data_path\": \"libero_10\", \"data_count\": 500}}, \"eval_openvla_l2norm_k095_long_seed42\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.95 --suite libero_10\", \"server\": \"westd-38929\", \"gpu\": [\"cuda:1\"], \"pid\": \"949438\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k095_long_seed42.log\", \"submitted_at\": \"2026-05-27T01:12:00.178Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"openvla-7b-finetuned-libero-10\", \"seed\": 42, \"data_path\": \"libero_10\", \"data_count\": 500}}, \"eval_openvla_attn_k095_goal_seed42\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u eval_openvla_l2norm_libero.py --mode attention_prune --k_ratio 0.95 --suite libero_goal\", \"server\": \"westd-38929\", \"gpu\": [\"cuda:0\"], \"pid\": \"949244\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_attn_k095_goal_seed42.log\", \"submitted_at\": \"2026-05-27T01:11:54.318Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"openvla-7b-finetuned-libero-goal\", \"seed\": 42, \"data_path\": \"libero_goal\", \"data_count\": 500}}, \"eval_openvla_random_k095_object_seed42\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 MUJOCO_GL=egl python -u eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.95 --suite libero_object --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/openvla-libero-object --unnorm_key libero_object\", \"server\": \"westd-41074\", \"gpu\": \"cuda:2\", \"pid\": 934369, \"data_path\": \"libero_object\", \"data_count\": 500, \"model_name\": \"openvla-libero-object\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/openvla-libero-object\", \"eval_data\": \"libero_object\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_openvla_random_k095_object_seed42.log\"}}, \"eval_openvla_attn_k05_goal_seed42_v2\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"MUJOCO_GL=egl python -u eval_openvla_l2norm_libero.py --mode attention_prune --k_ratio 0.5 --suite libero_goal --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/openvla-libero-goal --unnorm_key libero_goal --gpu 0\", \"server\": \"cqa1-33015\", \"gpu\": \"cuda:0\", \"pid\": 834185, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_attn_k05_goal_seed42_v2.log\", \"submitted_at\": \"2026-05-26T23:53:56.819Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_goal\", \"data_count\": 50, \"model_name\": \"openvla\", \"seed\": 42}}, \"eval_pi05_l2norm_k085_long_seed42_v4\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.85 --suite libero_10 --n_episodes 50 --seed 42 --gpu 0\", \"server\": \"cqa1-33015\", \"gpu\": \"cuda:2\", \"pid\": 790017, \"data_path\": \"libero_10\", \"data_count\": 50, \"model_name\": \"pi0.5\", \"seed\": 42, \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_pi05_l2norm_k085_long_seed42.log\"}}, \"eval_openvla_random_k095_long_seed42\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.95 --suite libero_10 --seed 42 --gpu 0\", \"server\": \"westd-41074\", \"gpu\": [\"cuda:0\"], \"pid\": \"32175\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_random_k095_long_seed42.log\", \"submitted_at\": \"2026-05-27T00:29:27.567Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"openvla-7b-finetuned-libero-10\", \"seed\": 42, \"data_path\": \"libero_10\", \"data_count\": 500, \"checkpoint_source\": \"/root/autodl-tmp/openvla-7b-finetuned-libero-10\", \"eval_data\": \"libero_10\"}}, \"eval_openvla_l2norm_k095_goal_seed42\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.95 --suite libero_goal --seed 42 --gpu 0\", \"server\": \"westd-27271\", \"gpu\": [\"cuda:0\"], \"pid\": \"609726\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k095_goal_seed42.log\", \"submitted_at\": \"2026-05-27T00:30:31.771Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"openvla-7b-finetuned-libero-goal\", \"seed\": 42, \"data_path\": \"libero_goal\", \"data_count\": 500, \"checkpoint_source\": \"/root/autodl-tmp/openvla-7b-finetuned-libero-goal\", \"eval_data\": \"libero_goal\"}}, \"eval_openvla_random_k075_long_seed42\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.75 --suite libero_10 --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/openvla-7b-finetuned-libero-10 --unnorm_key libero_10\", \"server\": \"westd-41074\", \"gpu\": [\"cuda:1\"], \"pid\": 856656, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_random_k075_long_seed42.log\", \"submitted_at\": \"2026-05-26T19:21:17.740Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"gpu_ids\": [1], \"data_path\": \"libero_10\", \"data_count\": 500, \"model_name\": \"openvla-7b-finetuned-libero-10\", \"seed\": 42, \"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"/root/autodl-tmp/openvla-7b-finetuned-libero-10\", \"eval_data\": \"libero_10\"}}, \"eval_openvla_attn_k075_long_seed42\": {\"status\": \"RUNNING\", \"spec\": {\"server\": \"westd-41074\", \"gpu\": \"cuda:3\", \"command\": \"MUJOCO_GL=egl python -u /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py --mode attention_prune --k_ratio 0.75 --suite libero_10 --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/openvla-7b-finetuned-libero-10 --unnorm_key libero_10\", \"pid\": 824210, \"data_path\": \"libero_10\", \"data_count\": 500, \"model_name\": \"openvla-7b-finetuned-libero-10\", \"seed\": 42, \"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"/root/autodl-tmp/openvla-7b-finetuned-libero-10\", \"eval_data\": \"libero_10\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_attn_k075_long_seed42.log\"}}}, \"count\": 12, \"total\": 12, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 5.8279}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "91b3d5c1-50da-4650-a87b-7ce4afd361f3",
  "uuid": "2e318c28-0608-444a-8cae-3c00ade14ffb",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"eval_openvla_attn_k095_object_seed42\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && python -u eval_openvla_l2norm_libero.py --mode attention_prune --k_ratio 0.95 --suite libero_object --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/openvla-libero-object --unnorm_key libero_object --gpu 1\\\\\\\"\\\", \\\"server\\\": \\\"westd-27271\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"638220\\\", \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_openvla_attn_k095_object_seed42.log\\\", \\\"submitted_at\\\": \\\"2026-05-27T01:32:06.124Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}}, \\\"eval_openvla_random_k095_goal_seed42\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.95 --suite libero_goal\\\", \\\"server\\\": \\\"cqa1-33015\\\", \\\"gpu\\\": [\\\"cuda:3\\\"], \\\"pid\\\": \\\"876792\\\", \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_openvla_random_k095_goal_seed42.log\\\", \\\"submitted_at\\\": \\\"2026-05-27T01:12:17.909Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"model_name\\\": \\\"openvla-libero-goal\\\", \\\"seed\\\": 42, \\\"data_path\\\": \\\"libero_goal\\\", \\\"data_count\\\": 500}}, \\\"eval_openvla_attn_k095_long_seed42\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u eval_openvla_l2norm_libero.py --mode attention_prune --k_ratio 0.95 --suite libero_10\\\", \\\"server\\\": \\\"westd-38929\\\", \\\"gpu\\\": [\\\"cuda:3\\\"], \\\"pid\\\": \\\"949998\\\", \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_openvla_attn_k095_long_seed42.log\\\", \\\"submitted_at\\\": \\\"2026-05-27T01:12:07.677Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"model_name\\\": \\\"openvla-7b-finetuned-libero-10\\\", \\\"seed\\\": 42, \\\"data_path\\\": \\\"libero_10\\\", \\\"data_count\\\": 500}}, \\\"eval_openvla_l2norm_k095_long_seed42\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.95 --suite libero_10\\\", \\\"server\\\": \\\"westd-38929\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"949438\\\", \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k095_long_seed42.log\\\", \\\"submitted_at\\\": \\\"2026-05-27T01:12:00.178Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"model_name\\\": \\\"openvla-7b-finetuned-libero-10\\\", \\\"seed\\\": 42, \\\"data_path\\\": \\\"libero_10\\\", \\\"data_count\\\": 500}}, \\\"eval_openvla_attn_k095_goal_seed42\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u eval_openvla_l2norm_libero.py --mode attention_prune --k_ratio 0.95 --suite libero_goal\\\", \\\"server\\\": \\\"westd-38929\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"949244\\\", \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_openvla_attn_k095_goal_seed42.log\\\", \\\"submitted_at\\\": \\\"2026-05-27T01:11:54.318Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"model_name\\\": \\\"openvla-7b-finetuned-libero-goal\\\", \\\"seed\\\": 42, \\\"data_path\\\": \\\"libero_goal\\\", \\\"data_count\\\": 500}}, \\\"eval_openvla_random_k095_object_seed42\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"CUDA_VISIBLE_DEVICES=2 MUJOCO_GL=egl python -u eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.95 --suite libero_object --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/openvla-libero-object --unnorm_key libero_object\\\", \\\"server\\\": \\\"westd-41074\\\", \\\"gpu\\\": \\\"cuda:2\\\", \\\"pid\\\": 934369, \\\"data_path\\\": \\\"libero_object\\\", \\\"data_count\\\": 500, \\\"model_name\\\": \\\"openvla-libero-object\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/openvla-libero-object\\\", \\\"eval_data\\\": \\\"libero_object\\\", \\\"log_path\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_openvla_random_k095_object_seed42.log\\\"}}, \\\"eval_openvla_attn_k05_goal_seed42_v2\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"MUJOCO_GL=egl python -u eval_openvla_l2norm_libero.py --mode attention_prune --k_ratio 0.5 --suite libero_goal --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/openvla-libero-goal --unnorm_key libero_goal --gpu 0\\\", \\\"server\\\": \\\"cqa1-33015\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"pid\\\": 834185, \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_openvla_attn_k05_goal_seed42_v2.log\\\", \\\"submitted_at\\\": \\\"2026-05-26T23:53:56.819Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"libero_goal\\\", \\\"data_count\\\": 50, \\\"model_name\\\": \\\"openvla\\\", \\\"seed\\\": 42}}, \\\"eval_pi05_l2norm_k085_long_seed42_v4\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.85 --suite libero_10 --n_episodes 50 --seed 42 --gpu 0\\\", \\\"server\\\": \\\"cqa1-33015\\\", \\\"gpu\\\": \\\"cuda:2\\\", \\\"pid\\\": 790017, \\\"data_path\\\": \\\"libero_10\\\", \\\"data_count\\\": 50, \\\"model_name\\\": \\\"pi0.5\\\", \\\"seed\\\": 42, \\\"log_path\\\": \\\"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_pi05_l2norm_k085_long_seed42.log\\\"}}, \\\"eval_openvla_random_k095_long_seed42\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.95 --suite libero_10 --seed 42 --gpu 0\\\", \\\"server\\\": \\\"westd-41074\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"32175\\\", \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_openvla_random_k095_long_seed42.log\\\", \\\"submitted_at\\\": \\\"2026-05-27T00:29:27.567Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"model_name\\\": \\\"openvla-7b-finetuned-libero-10\\\", \\\"seed\\\": 42, \\\"data_path\\\": \\\"libero_10\\\", \\\"data_count\\\": 500, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/openvla-7b-finetuned-libero-10\\\", \\\"eval_data\\\": \\\"libero_10\\\"}}, \\\"eval_openvla_l2norm_k095_goal_seed42\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.95 --suite libero_goal --seed 42 --gpu 0\\\", \\\"server\\\": \\\"westd-27271\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"609726\\\", \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k095_goal_seed42.log\\\", \\\"submitted_at\\\": \\\"2026-05-27T00:30:31.771Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"model_name\\\": \\\"openvla-7b-finetuned-libero-goal\\\", \\\"seed\\\": 42, \\\"data_path\\\": \\\"libero_goal\\\", \\\"data_count\\\": 500, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/openvla-7b-finetuned-libero-goal\\\", \\\"eval_data\\\": \\\"libero_goal\\\"}}, \\\"eval_openvla_random_k075_long_seed42\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"command\\\": \\\"python -u eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.75 --suite libero_10 --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/openvla-7b-finetuned-libero-10 --unnorm_key libero_10\\\", \\\"server\\\": \\\"westd-41074\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": 856656, \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_openvla_random_k075_long_seed42.log\\\", \\\"submitted_at\\\": \\\"2026-05-26T19:21:17.740Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"gpu_ids\\\": [1], \\\"data_path\\\": \\\"libero_10\\\", \\\"data_count\\\": 500, \\\"model_name\\\": \\\"openvla-7b-finetuned-libero-10\\\", \\\"seed\\\": 42, \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\", \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/openvla-7b-finetuned-libero-10\\\", \\\"eval_data\\\": \\\"libero_10\\\"}}, \\\"eval_openvla_attn_k075_long_seed42\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"spec\\\": {\\\"server\\\": \\\"westd-41074\\\", \\\"gpu\\\": \\\"cuda:3\\\", \\\"command\\\": \\\"MUJOCO_GL=egl python -u /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py --mode attention_prune --k_ratio 0.75 --suite libero_10 --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/openvla-7b-finetuned-libero-10 --unnorm_key libero_10\\\", \\\"pid\\\": 824210, \\\"data_path\\\": \\\"libero_10\\\", \\\"data_count\\\": 500, \\\"model_name\\\": \\\"openvla-7b-finetuned-libero-10\\\", \\\"seed\\\": 42, \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\", \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/openvla-7b-finetuned-libero-10\\\", \\\"eval_data\\\": \\\"libero_10\\\", \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_openvla_attn_k075_long_seed42.log\\\"}}}, \\\"count\\\": 12, \\\"total\\\": 12, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 5.8279}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"eval_openvla_attn_k095_object_seed42\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && python -u eval_openvla_l2norm_libero.py --mode attention_prune --k_ratio 0.95 --suite libero_object --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/openvla-libero-object --unnorm_key libero_object --gpu 1\\\"\", \"server\": \"westd-27271\", \"gpu\": [\"cuda:1\"], \"pid\": \"638220\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_attn_k095_object_seed42.log\", \"submitted_at\": \"2026-05-27T01:32:06.124Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"eval_openvla_random_k095_goal_seed42\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.95 --suite libero_goal\", \"server\": \"cqa1-33015\", \"gpu\": [\"cuda:3\"], \"pid\": \"876792\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_random_k095_goal_seed42.log\", \"submitted_at\": \"2026-05-27T01:12:17.909Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"openvla-libero-goal\", \"seed\": 42, \"data_path\": \"libero_goal\", \"data_count\": 500}}, \"eval_openvla_attn_k095_long_seed42\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u eval_openvla_l2norm_libero.py --mode attention_prune --k_ratio 0.95 --suite libero_10\", \"server\": \"westd-38929\", \"gpu\": [\"cuda:3\"], \"pid\": \"949998\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_attn_k095_long_seed42.log\", \"submitted_at\": \"2026-05-27T01:12:07.677Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"openvla-7b-finetuned-libero-10\", \"seed\": 42, \"data_path\": \"libero_10\", \"data_count\": 500}}, \"eval_openvla_l2norm_k095_long_seed42\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.95 --suite libero_10\", \"server\": \"westd-38929\", \"gpu\": [\"cuda:1\"], \"pid\": \"949438\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k095_long_seed42.log\", \"submitted_at\": \"2026-05-27T01:12:00.178Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"openvla-7b-finetuned-libero-10\", \"seed\": 42, \"data_path\": \"libero_10\", \"data_count\": 500}}, \"eval_openvla_attn_k095_goal_seed42\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u eval_openvla_l2norm_libero.py --mode attention_prune --k_ratio 0.95 --suite libero_goal\", \"server\": \"westd-38929\", \"gpu\": [\"cuda:0\"], \"pid\": \"949244\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_attn_k095_goal_seed42.log\", \"submitted_at\": \"2026-05-27T01:11:54.318Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"openvla-7b-finetuned-libero-goal\", \"seed\": 42, \"data_path\": \"libero_goal\", \"data_count\": 500}}, \"eval_openvla_random_k095_object_seed42\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 MUJOCO_GL=egl python -u eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.95 --suite libero_object --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/openvla-libero-object --unnorm_key libero_object\", \"server\": \"westd-41074\", \"gpu\": \"cuda:2\", \"pid\": 934369, \"data_path\": \"libero_object\", \"data_count\": 500, \"model_name\": \"openvla-libero-object\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/openvla-libero-object\", \"eval_data\": \"libero_object\", \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_openvla_random_k095_object_seed42.log\"}}, \"eval_openvla_attn_k05_goal_seed42_v2\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"MUJOCO_GL=egl python -u eval_openvla_l2norm_libero.py --mode attention_prune --k_ratio 0.5 --suite libero_goal --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/openvla-libero-goal --unnorm_key libero_goal --gpu 0\", \"server\": \"cqa1-33015\", \"gpu\": \"cuda:0\", \"pid\": 834185, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_attn_k05_goal_seed42_v2.log\", \"submitted_at\": \"2026-05-26T23:53:56.819Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_goal\", \"data_count\": 50, \"model_name\": \"openvla\", \"seed\": 42}}, \"eval_pi05_l2norm_k085_long_seed42_v4\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.85 --suite libero_10 --n_episodes 50 --seed 42 --gpu 0\", \"server\": \"cqa1-33015\", \"gpu\": \"cuda:2\", \"pid\": 790017, \"data_path\": \"libero_10\", \"data_count\": 50, \"model_name\": \"pi0.5\", \"seed\": 42, \"log_path\": \"/root/autodl-tmp/importance_margin_vla_compress/logs/eval_pi05_l2norm_k085_long_seed42.log\"}}, \"eval_openvla_random_k095_long_seed42\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.95 --suite libero_10 --seed 42 --gpu 0\", \"server\": \"westd-41074\", \"gpu\": [\"cuda:0\"], \"pid\": \"32175\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_random_k095_long_seed42.log\", \"submitted_at\": \"2026-05-27T00:29:27.567Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"openvla-7b-finetuned-libero-10\", \"seed\": 42, \"data_path\": \"libero_10\", \"data_count\": 500, \"checkpoint_source\": \"/root/autodl-tmp/openvla-7b-finetuned-libero-10\", \"eval_data\": \"libero_10\"}}, \"eval_openvla_l2norm_k095_goal_seed42\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.95 --suite libero_goal --seed 42 --gpu 0\", \"server\": \"westd-27271\", \"gpu\": [\"cuda:0\"], \"pid\": \"609726\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k095_goal_seed42.log\", \"submitted_at\": \"2026-05-27T00:30:31.771Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"openvla-7b-finetuned-libero-goal\", \"seed\": 42, \"data_path\": \"libero_goal\", \"data_count\": 500, \"checkpoint_source\": \"/root/autodl-tmp/openvla-7b-finetuned-libero-goal\", \"eval_data\": \"libero_goal\"}}, \"eval_openvla_random_k075_long_seed42\": {\"status\": \"RUNNING\", \"spec\": {\"command\": \"python -u eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.75 --suite libero_10 --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/openvla-7b-finetuned-libero-10 --unnorm_key libero_10\", \"server\": \"westd-41074\", \"gpu\": [\"cuda:1\"], \"pid\": 856656, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_random_k075_long_seed42.log\", \"submitted_at\": \"2026-05-26T19:21:17.740Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"gpu_ids\": [1], \"data_path\": \"libero_10\", \"data_count\": 500, \"model_name\": \"openvla-7b-finetuned-libero-10\", \"seed\": 42, \"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"/root/autodl-tmp/openvla-7b-finetuned-libero-10\", \"eval_data\": \"libero_10\"}}, \"eval_openvla_attn_k075_long_seed42\": {\"status\": \"RUNNING\", \"spec\": {\"server\": \"westd-41074\", \"gpu\": \"cuda:3\", \"command\": \"MUJOCO_GL=egl python -u /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py --mode attention_prune --k_ratio 0.75 --suite libero_10 --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/openvla-7b-finetuned-libero-10 --unnorm_key libero_10\", \"pid\": 824210, \"data_path\": \"libero_10\", \"data_count\": 500, \"model_name\": \"openvla-7b-finetuned-libero-10\", \"seed\": 42, \"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"/root/autodl-tmp/openvla-7b-finetuned-libero-10\", \"eval_data\": \"libero_10\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_attn_k075_long_seed42.log\"}}}, \"count\": 12, \"total\": 12, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 5.8279}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 74_

<details><summary>Logged reasoning block</summary>

```text
Let me cross-reference the running experiments in the registry with what's actually running on the servers.

**Registry RUNNING experiments (12):**
1. `eval_openvla_attn_k095_object_seed42` - westd-27271, cuda:1
2. `eval_openvla_random_k095_goal_seed42` - cqa1-33015, cuda:3
3. `eval_openvla_attn_k095_long_seed42` - westd-38929, cuda:3 → actually on westd-27271 based on ps output (PID 950007)


4. `eval_openvla_l2norm_k095_long_seed42` - westd-38929, cuda:1 → actually on westd-27271 (PID 949447)
5. `eval_openvla_attn_k095_goal_seed42` - westd-38929, cuda:0
6. `eval_openvla_random_k095_object_seed42` - westd-41074, cuda:2
7. `eval_openvla_attn_k05_goal_seed42_v2` - cqa1-33015, cuda:0
8. `eval_pi05_l2norm_k085_long_seed42_v4` - cqa1-33015, cuda:2
9. `eval_openvla_random_k095_long_seed42` - westd-41074, cuda:0
10. `eval_openvla_l2norm_k095_goal_seed42` - westd-27271, cuda:0
11. `eval_openvla_random_k075_long_seed42` - westd-41074, cuda:1
12. `eval_openvla_attn_k075_long_seed42` - westd-41074, cuda:3

Now checking what's actually running on the servers shows westd-27271 has `eval_openvla_attn_k07_long_seed42_v2` on GPU 0.

Looking at westd-27271's full GPU allocation, I see GPU 2 is running the l2norm k=0.75 variant, GPU 1 has the l2norm k=0.95 variant, and GPU 3 is running the attention k=0.95 variant. On westd-41074, GPU 0 is running the random k=0.5 object variant while also having the random k=0.95 long variant queued up.

Now I'm checking the registry against the actual process output to verify which server is actually running which jobs, since there's some discrepancy between what the registry shows and what ps is reporting. I'm noticing a discrepancy—the third SSH check was actually to westd-27271, but the original prompt indicated experiment C should be on westd-38929. Let me look at what's actually running on westd-38929 from the ps output: there's a tmux session running l2norm_prune with k=0.9 on libero_goal with seed 43 on GPU 0, and another process for k=0.95 also on GPU 0, which seems odd since both can't be using the same GPU simultaneously. I need to verify if the tmux session's process is still active.

Looking more carefully at the ps output for westd-38929, I can only see PID 609731 as the active Python process running the k=0.95 experiment, while the tmux session for seed 43 exists but has no running Python process inside it—it likely finished already. So the only active experiment is the k=0.95 libero_goal seed 42 run on GPU 0.

Now I'm cross-referencing the running processes against the registry and finding three experiments that are actively running but not listed in the RUNNING registry: the attention k=0.7 long seed 42 on westd-27271 GPU 0, the l2norm k=0.75 long seed 42 also on westd-27271 GPU 2, and the random k=0.5 object seed 42 on westd-41074 GPU 0. These three are definitely missing from the registry.

Let me verify the server assignments and process details more carefully since I'm getting confused about which ps output corresponds to which machine. I'm getting confused about the order of these ps commands across the different batches. Let me trace through this more carefully—the second batch had registry queries followed by two failed ps attempts, and then the third batch had three successful ps aux calls for each of those same servers. So I need to match up which output corresponds to which server based on the sequence.

Now I'm looking at which experiments are actually running on the machines but aren't showing up in the registry's RUNNING list. On westd-27271, there are two experiments with attention and l2norm pruning that aren't registered, and westd-41074 has at least one random pruning experiment that's also missing from the registry.

But there's a bigger issue here—the registry locations don't match what ps is actually showing. Some experiments are listed as being on one server but are actually running on another, which suggests either stale registry data or the experiments got moved around. The ps output for westd-27271 is truncated, so I might be missing some processes. Rather than get bogged down in tracking every process, I should focus on registering the three unregistered experiments: the attention pruning experiment on GPU 0, the l2norm pruning with k=0.75 on GPU 2, and the random pruning experiment.

Before registering though, I want to check if older versions of some of these experiments already exist in the registry without the version suffixes. After that, I'll register the three unregistered ones and pull all the DONE experiments to work on the cliff curves.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "91b3d5c1-50da-4650-a87b-7ce4afd361f3",
  "uuid": "20b91a4a-0dee-48af-82ed-b906cef21476",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XsLm7XHENizkDmh9B3rkVD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4469,
      "cache_read_input_tokens": 52977,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4469
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Assistant

_source line 75_

Registry 有 12 个 RUNNING 实验。对比 ps 发现 3 个运行中但未注册的实验。注册它们，并读取所有 DONE 实验用于 cliff curve。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "91b3d5c1-50da-4650-a87b-7ce4afd361f3",
  "uuid": "0abe739c-98a2-478f-a52b-19484aac41b5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XsLm7XHENizkDmh9B3rkVD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4469,
      "cache_read_input_tokens": 52977,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4469
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 76_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01BX5FPnmbUc3vg3xweMYCpv`</summary>

```json
{
  "exp_id": "eval_openvla_attn_k07_long_seed42_v2",
  "field": "hypothesis",
  "value": "OpenVLA Attention k=0.7 Long seed42 — Attention pruning k=0.7 在 LIBERO-10 上的性能，Long cliff curve 中间点",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "91b3d5c1-50da-4650-a87b-7ce4afd361f3",
  "uuid": "728955b4-80db-4b04-b6e0-5f07d80f668d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XsLm7XHENizkDmh9B3rkVD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4469,
      "cache_read_input_tokens": 52977,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4469
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 77_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_01EVDBiXWa9rR1HnQufNojWK`</summary>

```json
{
  "exp_id": "eval_openvla_l2norm_k075_long_seed42",
  "field": "hypothesis",
  "value": "OpenVLA L2norm k=0.75 Long seed42 — L2norm pruning k=0.75 在 LIBERO-10 上的性能，Long cliff curve 数据点",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "91b3d5c1-50da-4650-a87b-7ce4afd361f3",
  "uuid": "fcb1f71c-a873-4a40-bd64-1881e121f847",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XsLm7XHENizkDmh9B3rkVD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4469,
      "cache_read_input_tokens": 52977,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4469
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 78_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry · `toolu_017vexssAg2MfNym8P82oG5z`</summary>

```json
{
  "exp_id": "eval_openvla_random_k05_object_seed42_v2",
  "field": "hypothesis",
  "value": "OpenVLA Random k=0.5 Object seed42 — Random pruning 极端压缩在 LIBERO-Object 上的性能下限",
  "project": "importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "91b3d5c1-50da-4650-a87b-7ce4afd361f3",
  "uuid": "b242ddc8-c9ac-4088-a5fd-e9157aa19690",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XsLm7XHENizkDmh9B3rkVD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4469,
      "cache_read_input_tokens": 52977,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4469
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 79_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01BxapvKiVr8YyqcrAWkWoUz`</summary>

```json
{
  "project": "importance_margin_vla_compress",
  "filters": {
    "status": "DONE"
  },
  "fields": [
    "exp_id",
    "status",
    "conclusion",
    "metrics"
  ],
  "limit": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "91b3d5c1-50da-4650-a87b-7ce4afd361f3",
  "uuid": "2557207f-1cd0-4768-a655-02e5669f75f1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XsLm7XHENizkDmh9B3rkVD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4469,
      "cache_read_input_tokens": 52977,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4469
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 80 · 2026-05-27T01:36:35.042Z_

<details><summary>↩ Tool result · `toolu_01BX5FPnmbUc3vg3xweMYCpv`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_openvla_attn_k07_long_seed42_v2\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T18:11:02.573Z\", \"updated_at\": \"2026-05-27T01:36:33.111Z\", \"hypothesis\": \"OpenVLA Attention k=0.7 Long seed42 — Attention pruning k=0.7 在 LIBERO-10 上的性能，Long cliff curve 中间点\", \"parent\": \"eval_openvla_attn_k09_long_seed42_v3\", \"spec\": {\"command\": \"python3 eval_openvla_l2norm_libero.py --mode attention_prune --k_ratio 0.7 --suite libero_10 --num_episodes 50 --seed 42\", \"server\": \"westd-38929\", \"gpu\": [\"cuda:0\"], \"pid\": \"6806\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_attn_k07_long_seed42_v2.log\", \"submitted_at\": \"2026-05-25T18:12:13.087Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_10\", \"data_count\": 500, \"model_name\": \"openvla-7b-finetuned-libero-10\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/models/openvla-7b-finetuned-libero-10\", \"eval_data\": \"libero_10\", \"wall_clock_seconds\": 35231.4, \"gpu_hours\": 9.79}, \"reproduce\": {\"finished_at\": \"2026-05-26T03:56:28.348Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-26T03:56:46.074420+00:00\"}]}, \"metrics\": {\"success_rate\": 24, \"total_successes\": 120, \"total_episodes\": 500}, \"conclusion\": \"negative\", \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_attn_k07_long_seed42_v2.log\", \"completed_at\": \"2026-05-26T03:59:24.537Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.087}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "91b3d5c1-50da-4650-a87b-7ce4afd361f3",
  "uuid": "eaa72085-dc70-40f1-9ad5-57c77685893a",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval_openvla_attn_k07_long_seed42_v2\\\", \\\"experiment\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-25T18:11:02.573Z\\\", \\\"updated_at\\\": \\\"2026-05-27T01:36:33.111Z\\\", \\\"hypothesis\\\": \\\"OpenVLA Attention k=0.7 Long seed42 — Attention pruning k=0.7 在 LIBERO-10 上的性能，Long cliff curve 中间点\\\", \\\"parent\\\": \\\"eval_openvla_attn_k09_long_seed42_v3\\\", \\\"spec\\\": {\\\"command\\\": \\\"python3 eval_openvla_l2norm_libero.py --mode attention_prune --k_ratio 0.7 --suite libero_10 --num_episodes 50 --seed 42\\\", \\\"server\\\": \\\"westd-38929\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"6806\\\", \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_openvla_attn_k07_long_seed42_v2.log\\\", \\\"submitted_at\\\": \\\"2026-05-25T18:12:13.087Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"data_path\\\": \\\"libero_10\\\", \\\"data_count\\\": 500, \\\"model_name\\\": \\\"openvla-7b-finetuned-libero-10\\\", \\\"seed\\\": 42, \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/models/openvla-7b-finetuned-libero-10\\\", \\\"eval_data\\\": \\\"libero_10\\\", \\\"wall_clock_seconds\\\": 35231.4, \\\"gpu_hours\\\": 9.79}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-26T03:56:28.348Z\\\"}, \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-26T03:56:46.074420+00:00\\\"}]}, \\\"metrics\\\": {\\\"success_rate\\\": 24, \\\"total_successes\\\": 120, \\\"total_episodes\\\": 500}, \\\"conclusion\\\": \\\"negative\\\", \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\", \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_openvla_attn_k07_long_seed42_v2.log\\\", \\\"completed_at\\\": \\\"2026-05-26T03:59:24.537Z\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 4.087}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval_openvla_attn_k07_long_seed42_v2\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T18:11:02.573Z\", \"updated_at\": \"2026-05-27T01:36:33.111Z\", \"hypothesis\": \"OpenVLA Attention k=0.7 Long seed42 — Attention pruning k=0.7 在 LIBERO-10 上的性能，Long cliff curve 中间点\", \"parent\": \"eval_openvla_attn_k09_long_seed42_v3\", \"spec\": {\"command\": \"python3 eval_openvla_l2norm_libero.py --mode attention_prune --k_ratio 0.7 --suite libero_10 --num_episodes 50 --seed 42\", \"server\": \"westd-38929\", \"gpu\": [\"cuda:0\"], \"pid\": \"6806\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_attn_k07_long_seed42_v2.log\", \"submitted_at\": \"2026-05-25T18:12:13.087Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"libero_10\", \"data_count\": 500, \"model_name\": \"openvla-7b-finetuned-libero-10\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/models/openvla-7b-finetuned-libero-10\", \"eval_data\": \"libero_10\", \"wall_clock_seconds\": 35231.4, \"gpu_hours\": 9.79}, \"reproduce\": {\"finished_at\": \"2026-05-26T03:56:28.348Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-26T03:56:46.074420+00:00\"}]}, \"metrics\": {\"success_rate\": 24, \"total_successes\": 120, \"total_episodes\": 500}, \"conclusion\": \"negative\", \"checkpoint_path\": \"N/A (eval only)\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_attn_k07_long_seed42_v2.log\", \"completed_at\": \"2026-05-26T03:59:24.537Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.087}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 81 · 2026-05-27T01:36:38.489Z_

<details><summary>↩ Tool result · `toolu_01EVDBiXWa9rR1HnQufNojWK`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_openvla_l2norm_k075_long_seed42\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-26T17:30:02.823Z\", \"updated_at\": \"2026-05-27T01:36:37.081Z\", \"hypothesis\": \"OpenVLA L2norm k=0.75 Long seed42 — L2norm pruning k=0.75 在 LIBERO-10 上的性能，Long cliff curve 数据点\", \"server\": \"westd-38929\", \"gpu\": \"cuda:2\", \"spec\": {\"command\": \"MUJOCO_GL=egl /root/miniconda3/bin/python -u /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.75 --suite libero_10 --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/models/openvla-7b-finetuned-libero-10 --unnorm_key libero_10\", \"server\": \"westd-38929\", \"gpu\": \"cuda:2\", \"pid\": 732922, \"data_path\": \"libero_10\", \"data_count\": 50, \"model_name\": \"openvla-7b-finetuned-libero-10\", \"seed\": 42, \"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"/root/autodl-tmp/models/openvla-7b-finetuned-libero-10\", \"eval_data\": \"libero_10\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k075_long_seed42.log\"}, \"pid\": \"732922\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k075_long_seed42.log\", \"reproduce\": {\"command\": \"MUJOCO_GL=egl /root/miniconda3/bin/python -u /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.75 --suite libero_10 --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/models/openvla-7b-finetuned-libero-10 --unnorm_key libero_10\", \"finished_at\": \"2026-05-27T01:33:45.915Z\"}, \"failure_reason\": \"EXIT_CODE=124 (timeout — exceeded timeout_hours)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-27T01:32:58.250Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-27T01:35:29.734238+00:00\"}]}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.4333}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "91b3d5c1-50da-4650-a87b-7ce4afd361f3",
  "uuid": "3f837284-507b-482e-bdd8-8774089f8e54",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval_openvla_l2norm_k075_long_seed42\\\", \\\"experiment\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-26T17:30:02.823Z\\\", \\\"updated_at\\\": \\\"2026-05-27T01:36:37.081Z\\\", \\\"hypothesis\\\": \\\"OpenVLA L2norm k=0.75 Long seed42 — L2norm pruning k=0.75 在 LIBERO-10 上的性能，Long cliff curve 数据点\\\", \\\"server\\\": \\\"westd-38929\\\", \\\"gpu\\\": \\\"cuda:2\\\", \\\"spec\\\": {\\\"command\\\": \\\"MUJOCO_GL=egl /root/miniconda3/bin/python -u /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.75 --suite libero_10 --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/models/openvla-7b-finetuned-libero-10 --unnorm_key libero_10\\\", \\\"server\\\": \\\"westd-38929\\\", \\\"gpu\\\": \\\"cuda:2\\\", \\\"pid\\\": 732922, \\\"data_path\\\": \\\"libero_10\\\", \\\"data_count\\\": 50, \\\"model_name\\\": \\\"openvla-7b-finetuned-libero-10\\\", \\\"seed\\\": 42, \\\"checkpoint_path\\\": \\\"N/A (eval only)\\\", \\\"checkpoint_source\\\": \\\"/root/autodl-tmp/models/openvla-7b-finetuned-libero-10\\\", \\\"eval_data\\\": \\\"libero_10\\\", \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k075_long_seed42.log\\\"}, \\\"pid\\\": \\\"732922\\\", \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k075_long_seed42.log\\\", \\\"reproduce\\\": {\\\"command\\\": \\\"MUJOCO_GL=egl /root/miniconda3/bin/python -u /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.75 --suite libero_10 --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/models/openvla-7b-finetuned-libero-10 --unnorm_key libero_10\\\", \\\"finished_at\\\": \\\"2026-05-27T01:33:45.915Z\\\"}, \\\"failure_reason\\\": \\\"EXIT_CODE=124 (timeout — exceeded timeout_hours)\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"completed_at\\\": \\\"2026-05-27T01:32:58.250Z\\\", \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_failed\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-27T01:35:29.734238+00:00\\\"}]}}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 3.4333}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval_openvla_l2norm_k075_long_seed42\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-26T17:30:02.823Z\", \"updated_at\": \"2026-05-27T01:36:37.081Z\", \"hypothesis\": \"OpenVLA L2norm k=0.75 Long seed42 — L2norm pruning k=0.75 在 LIBERO-10 上的性能，Long cliff curve 数据点\", \"server\": \"westd-38929\", \"gpu\": \"cuda:2\", \"spec\": {\"command\": \"MUJOCO_GL=egl /root/miniconda3/bin/python -u /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.75 --suite libero_10 --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/models/openvla-7b-finetuned-libero-10 --unnorm_key libero_10\", \"server\": \"westd-38929\", \"gpu\": \"cuda:2\", \"pid\": 732922, \"data_path\": \"libero_10\", \"data_count\": 50, \"model_name\": \"openvla-7b-finetuned-libero-10\", \"seed\": 42, \"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"/root/autodl-tmp/models/openvla-7b-finetuned-libero-10\", \"eval_data\": \"libero_10\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k075_long_seed42.log\"}, \"pid\": \"732922\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_l2norm_k075_long_seed42.log\", \"reproduce\": {\"command\": \"MUJOCO_GL=egl /root/miniconda3/bin/python -u /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.75 --suite libero_10 --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/models/openvla-7b-finetuned-libero-10 --unnorm_key libero_10\", \"finished_at\": \"2026-05-27T01:33:45.915Z\"}, \"failure_reason\": \"EXIT_CODE=124 (timeout — exceeded timeout_hours)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-27T01:32:58.250Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-27T01:35:29.734238+00:00\"}]}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.4333}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 82 · 2026-05-27T01:36:41.976Z_

<details><summary>↩ Tool result · `toolu_017vexssAg2MfNym8P82oG5z`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_openvla_random_k05_object_seed42_v2\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T18:24:20.591Z\", \"updated_at\": \"2026-05-27T01:36:40.606Z\", \"hypothesis\": \"OpenVLA Random k=0.5 Object seed42 — Random pruning 极端压缩在 LIBERO-Object 上的性能下限\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=3 MUJOCO_GL=egl python -u eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.5 --suite libero_object --num_episodes 50 --seed 42\\\"\", \"server\": \"cqa1-33015\", \"gpu\": [\"cuda:3\"], \"pid\": \"4360\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_random_k05_object_seed42_v2.log\", \"submitted_at\": \"2026-05-26T03:42:54.126Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-25T22:49:01.538Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.4722}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "91b3d5c1-50da-4650-a87b-7ce4afd361f3",
  "uuid": "c61cbc26-864e-47a5-abb1-a3927c64365d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"eval_openvla_random_k05_object_seed42_v2\\\", \\\"experiment\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-25T18:24:20.591Z\\\", \\\"updated_at\\\": \\\"2026-05-27T01:36:40.606Z\\\", \\\"hypothesis\\\": \\\"OpenVLA Random k=0.5 Object seed42 — Random pruning 极端压缩在 LIBERO-Object 上的性能下限\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=3 MUJOCO_GL=egl python -u eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.5 --suite libero_object --num_episodes 50 --seed 42\\\\\\\"\\\", \\\"server\\\": \\\"cqa1-33015\\\", \\\"gpu\\\": [\\\"cuda:3\\\"], \\\"pid\\\": \\\"4360\\\", \\\"log_path\\\": \\\"~/runs/importance_margin_vla_compress/eval_openvla_random_k05_object_seed42_v2.log\\\", \\\"submitted_at\\\": \\\"2026-05-26T03:42:54.126Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}, \\\"conclusion\\\": \\\"killed\\\", \\\"completed_at\\\": \\\"2026-05-25T22:49:01.538Z\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 3.4722}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"eval_openvla_random_k05_object_seed42_v2\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T18:24:20.591Z\", \"updated_at\": \"2026-05-27T01:36:40.606Z\", \"hypothesis\": \"OpenVLA Random k=0.5 Object seed42 — Random pruning 极端压缩在 LIBERO-Object 上的性能下限\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/importance_margin_vla_compress && CUDA_VISIBLE_DEVICES=3 MUJOCO_GL=egl python -u eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.5 --suite libero_object --num_episodes 50 --seed 42\\\"\", \"server\": \"cqa1-33015\", \"gpu\": [\"cuda:3\"], \"pid\": \"4360\", \"log_path\": \"~/runs/importance_margin_vla_compress/eval_openvla_random_k05_object_seed42_v2.log\", \"submitted_at\": \"2026-05-26T03:42:54.126Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-25T22:49:01.538Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.4722}}"
    }
  }
}
```

</details>

---


### Tool result

_source line 83 · 2026-05-27T01:36:44.449Z_

<details><summary>↩ Tool result · `toolu_01BxapvKiVr8YyqcrAWkWoUz`</summary>

```text
Error: result (204,005 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/91b3d5c1-50da-4650-a87b-7ce4afd361f3/tool-results/mcp-agent-ml-research-read_registry-1779845804446.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/91b3d5c1-50da-4650-a87b-7ce4afd361f3/tool-results/mcp-agent-ml-research-read_registry-1779845804446.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "91b3d5c1-50da-4650-a87b-7ce4afd361f3",
  "uuid": "ce03e08d-0833-48d9-ba31-f0742965d7ee",
  "tool_use_result": {
    "content": "Error: result (204,005 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/91b3d5c1-50da-4650-a87b-7ce4afd361f3/tool-results/mcp-agent-ml-research-read_registry-1779845804446.txt.\nFormat: JSON with schema: {result: string}\nUse offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.\nREQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:\n- You MUST read the content from the file at /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/91b3d5c1-50da-4650-a87b-7ce4afd361f3/tool-results/mcp-agent-ml-research-read_registry-1779845804446.txt in sequential chunks until 100% of the content has been read.\n- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.\n- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"eval_openvla_random_k05_object_seed42_v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_openvla_l2norm_k075_long_seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_openvla_attn_k07_long_seed42_v2\": {\"status\": \"DONE\", \"metrics\": {\"success_rate\": 24, \"total_successes\": 120, \"total_episodes\": 500}, \"conclusion\": \"negative\"}, \"eval_openvla_random_k075_goal_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 72, \"suite\": \"libero_goal\", \"prune_method\": \"random\", \"keep_ratio\": 0.75, \"seed\": 42, \"episodes_per_task\": 50}}, \"eval_pi05_random_k07_long_seed42\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 62.4, \"suite\": \"libero_10\", \"prune_method\": \"random\", \"keep_ratio\": 0.7, \"seed\": 42, \"episodes_per_task\": 50}, \"conclusion\": \"success\"}, \"eval_openvla_attn_k05_long_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 14.6, \"suite\": \"libero_10\", \"prune_method\": \"attention\", \"keep_ratio\": 0.5, \"seed\": 42, \"episodes_per_task\": 50}}, \"eval_openvla_l2norm_k05_long_seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_openvla_attn_k075_goal_seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_openvla_random_k085_long_seed42_v3\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.45, \"n_episodes\": 500, \"task_sr\": {\"put_both_alphabet_soup_and_tomato_sauce_in_basket\": 0.6, \"put_both_cream_cheese_and_butter_in_basket\": 0.64, \"turn_on_stove_put_moka_pot\": 0.6, \"put_black_bowl_in_bottom_drawer\": 0.32, \"put_white_mug_left_plate_yellow_mug_right_plate\": 0.2, \"pick_up_book_place_in_caddy\": 0.76, \"put_white_mug_on_plate_chocolate_pudding_right\": 0.3, \"put_both_alphabet_soup_and_cream_cheese_in_basket\": 0.6, \"put_both_moka_pots_on_stove\": 0.32, \"put_yellow_white_mug_in_microwave\": 0.16}}, \"conclusion\": \"success\"}, \"eval_openvla_random_k05_goal_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.522, \"total_successes\": 261, \"total_episodes\": 500}}, \"eval_pi05_attn_k095_long_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 77, \"n_episodes\": 500, \"task_sr\": {\"T0\": null, \"T1\": null, \"T2\": null, \"T3\": null, \"T4\": null, \"T5\": null, \"T6\": 14, \"T7\": 80, \"T8\": 30, \"T9\": 98}}}, \"eval_openvla_l2norm_k075_goal_seed42_v2\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 70.2, \"task_srs\": [54, 80, 86, 22, 88, 70, 68, 98, 82, 54], \"episodes\": 500, \"tasks\": 10, \"time_min\": 198, \"tokens_256_to_192\": true}, \"conclusion\": \"success\"}, \"eval_openvla_attn_k085_long_seed42_v5\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 45.8, \"task_srs\": [60, 58, 56, 34, 38, 66, 34, 66, 24, 22], \"episodes\": 500, \"tasks\": 10, \"time_min\": 548.6, \"tokens_256_to_217\": true}, \"conclusion\": \"success\"}, \"eval_openvla_attn_k075_object_seed42\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 53.2, \"total_success\": 266, \"total_episodes\": 500, \"per_task_sr\": {\"alphabet_soup\": 56, \"cream_cheese\": 28, \"salad_dressing\": 70, \"bbq_sauce\": 34, \"ketchup\": 76, \"tomato_sauce\": 30, \"butter\": 28, \"milk\": 54, \"chocolate_pudding\": 86, \"orange_juice\": 70}, \"eval_time_min\": 272}, \"conclusion\": \"success\"}, \"eval_pi05_attention_k07_long_seed42_v2\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 50.8, \"per_task\": {\"T0_alphabet_soup_tomato\": 72, \"T1_cream_cheese_butter\": 70, \"T2_stove_moka_pot\": 58, \"T3_black_bowl_drawer\": 46, \"T4_white_mug_plate\": 36, \"T5_book_back\": 32, \"T6_mug_plate_yellow\": 58, \"T7_alphabet_soup_cream\": 48, \"T8_moka_pots_stove\": 6, \"T9_yellow_white_mug_microwave\": 82}, \"suite\": \"libero_10\", \"prune_method\": \"attention\", \"keep_ratio\": 0.7, \"seed\": 42, \"episodes_per_task\": 50}, \"conclusion\": \"success\"}, \"eval_pi05_l2norm_k075_long_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 73.4, \"per_task\": {\"T0_soup_tomato\": 96, \"T1_cream_butter\": 94, \"T2_stove_moka\": 82, \"T3_bowl_drawer\": 70, \"T4_mug_plate\": 68, \"T5_book_back\": 84, \"T6_mug_plate_tomato\": 52, \"T7_soup_cream\": 76, \"T8_moka_pots\": 28, \"T9_mug_microwave\": 84}}}, \"eval_pi05_l2norm_k05_spatial_seed42_postfix\": {\"conclusion\": \"success\", \"metrics\": {\"elapsed_min\": 149.18, \"overall_sr\": 0.574, \"per_task_sr\": {\"pick_up_black_bowl_between_plate_and_ramekin\": 0.8, \"pick_up_black_bowl_from_table_center\": 0.9, \"pick_up_black_bowl_in_top_drawer\": 0.32, \"pick_up_black_bowl_next_to_cookie_box\": 0.28, \"pick_up_black_bowl_next_to_plate\": 0.74, \"pick_up_black_bowl_next_to_ramekin\": 0.9, \"pick_up_black_bowl_on_cookie_box\": 0.26, \"pick_up_black_bowl_on_ramekin\": 0.34, \"pick_up_black_bowl_on_stove\": 0.76, \"pick_up_black_bowl_on_wooden_cabinet\": 0.44}, \"total_episodes\": 500, \"total_successes\": 287}, \"status\": \"DONE\"}, \"eval_pi05_random_k085_long_seed43_postfix\": {\"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.418, \"total_episodes\": 500, \"total_successes\": 209}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k03_long_seed42_postfix\": {\"conclusion\": \"killed\", \"metrics\": {\"overall_sr\": 0.366, \"total_episodes\": 500, \"total_successes\": 183}, \"status\": \"DONE\"}, \"eval_pi05_random_k09_long_seed43_postfix\": {\"conclusion\": \"killed\", \"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.356, \"total_episodes\": 500, \"total_successes\": 178}}, \"eval_openvla_random_k085_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_pi05_random_k085_long_seed42_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 44.4, \"total_success\": 222, \"total_episodes\": 500, \"per_task_sr\": {\"T0_alphabet_soup_tomato\": 52, \"T1_cream_cheese_butter\": 46, \"T2_stove_moka_pot\": 58, \"T3_black_bowl_drawer\": 74, \"T4_white_mug_left_plate\": 12, \"T5_book_back_shelf\": 32, \"T6_white_mug_plate\": 42, \"T7_alphabet_soup_cream\": 44, \"T8_moka_pots_stove\": 10, \"T9_yellow_white_mug_microwave\": 74}, \"runtime_min\": 267.8}}, \"eval_pi05_l2norm_k085_long_seed42_v3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 78.8, \"total_episodes\": 500, \"total_successes\": 394, \"per_task_sr\": {\"T0_alphabet_soup_tomato\": 98, \"T1_cream_cheese_butter\": 94, \"T2_stove_moka_pot\": 88, \"T3_black_bowl_drawer\": 98, \"T4_white_mug_left_plate\": 72, \"T5_book_back\": 98, \"T6_white_mug_plate\": 6, \"T7_alphabet_soup_cream\": 86, \"T8_moka_pots_stove\": 54, \"T9_yellow_white_mug_microwave\": 94}}}, \"eval_openvla_l2norm_k075_object_seed42\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.574, \"total_episodes\": 500, \"successful_episodes\": 287, \"task_sr\": {\"alphabet_soup\": 0.78, \"cream_cheese\": 0.28, \"salad_dressing\": 0.68, \"bbq_sauce\": 0.46, \"ketchup\": 0.86, \"tomato_sauce\": 0.66, \"butter\": 0.4, \"milk\": 0.48, \"chocolate_pudding\": 0.46, \"orange_juice\": 0.68}, \"time_min\": 289.4}, \"conclusion\": \"negative\"}, \"eval_openvla_attn_k07_goal_seed42\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"overall_sr\": 0.664, \"total_episodes\": 500, \"total_successes\": 332}}, \"eval_openvla_l2norm_k075_goal_seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_openvla_l2norm_k07_goal_seed42\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.684, \"total_episodes\": 500, \"per_task_sr\": {\"open_the_middle_drawer_of_the_cabinet\": 0.6, \"put_the_bowl_on_the_stove\": 0.86, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.74, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.16, \"put_the_bowl_on_top_of_the_cabinet\": 0.84, \"push_the_plate_to_the_front_of_the_stove\": 0.66, \"put_the_cream_cheese_in_the_bowl\": 0.74, \"turn_on_the_stove\": 0.98, \"put_the_bowl_on_the_plate\": 0.7, \"put_the_wine_bottle_on_the_rack\": 0.56}}, \"conclusion\": \"success\"}, \"eval_pi05_attention_k085_long_seed42_v2\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 51.6, \"total_episodes\": 500, \"per_task\": {\"T0_alphabet_soup_tomato\": 20, \"T1_cream_cheese_butter\": 54, \"T2_stove_moka_pot\": 32, \"T3_black_bowl_drawer\": 60, \"T4_white_mug_left_plate\": 48, \"T5_book_back_shelf\": 90, \"T6_white_mug_plate\": 68, \"T7_alphabet_soup_cream\": 46, \"T8_moka_pots_stove\": 6, \"T9_yellow_white_mug_microwave\": 92}}, \"conclusion\": \"success\"}, \"eval_openvla_attn_k05_goal_seed42\": {\"conclusion\": \"success\", \"status\": \"DONE\", \"metrics\": {\"overall_sr\": 44.2, \"total_episodes\": 500, \"total_successes\": 221, \"source\": \"result file found on westd-27271 by audit worker, needs verification\"}}, \"eval_openvla_attn_k07_object_seed42_v3\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 43.8, \"total_episodes\": 500, \"total_successes\": 219}, \"conclusion\": \"success\"}, \"eval_openvla_random_k05_object_seed42_v3\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"overall_sr\": 35.8, \"total_episodes\": 500, \"total_successes\": 179, \"per_task\": {\"alphabet_soup\": 56, \"bbq_sauce\": 58, \"butter\": 0, \"chocolate_pudding\": 30, \"cream_cheese\": 2, \"ketchup\": 60, \"milk\": 12, \"orange_juice\": 74, \"salad_dressing\": 40, \"tomato_sauce\": 26}}}, \"eval_openvla_random_k05_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_openvla_random_k05_goal_seed42_v2\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"overall_sr\": 0.522, \"total_successes\": 261, \"total_episodes\": 500, \"per_task_sr\": {\"open_middle_drawer\": 0.44, \"bowl_on_stove\": 0.64, \"wine_bottle_on_cabinet\": 0.64, \"open_drawer_put_bowl\": 0.1, \"bowl_on_cabinet\": 0.74, \"push_plate_stove\": 0.54, \"cream_cheese_in_bowl\": 0.48, \"turn_on_stove\": 0.94, \"bowl_on_plate\": 0.46, \"wine_bottle_on_rack\": 0.24}, \"source\": \"v1 results (v2 process died early)\", \"elapsed_minutes\": 230.08}}, \"eval_openvla_random_k05_long_seed42_v2\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 18.6, \"n_episodes\": 500}, \"conclusion\": \"negative\"}, \"eval_openvla_l2norm_k05_goal_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.434, \"total_successes\": 217, \"total_episodes\": 500, \"elapsed_min\": 386.1}, \"status\": \"DONE\"}, \"eval_openvla_random_k07_goal_seed42_v4\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 68.4}, \"conclusion\": \"success\"}, \"eval_pi05_attention_k05_long_seed42_v2\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 49.8, \"task_sr\": {\"T0_alphabet_soup_tomato\": 74, \"T1_cream_cheese_butter\": 46, \"T2_stove_moka_pot\": 60, \"T3_black_bowl_drawer\": 70, \"T4_white_mug_left_plate\": 46, \"T5_book_back_shelf\": 52, \"T6_white_mug_plate\": 10, \"T7_alphabet_soup_cream\": 54, \"T8_moka_pots_stove\": 18, \"T9_yellow_white_mug_microwave\": 68}}, \"conclusion\": \"success\"}, \"eval_pi05_attention_k075_long_seed42_v2\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 52.4, \"task_sr\": {\"T0_alphabet_soup_tomato\": 68, \"T1_cream_cheese_butter\": 78, \"T2_stove_moka_pot\": 64, \"T3_black_bowl_drawer\": 48, \"T4_white_mug_left_plate\": 26, \"T5_book_back_compartment\": 50, \"T6_white_mug_plate\": 76, \"T7_alphabet_soup_cream\": 30, \"T8_both_moka_pots_stove\": 6, \"T9_yellow_white_mug_microwave\": 78}}, \"conclusion\": \"success\"}, \"eval_openvla_random_k085_goal_seed42\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 78.6, \"task_sr\": {\"open_the_middle_drawer_of_the_cabinet\": 70, \"put_the_bowl_on_the_stove\": 92, \"put_the_wine_bottle_on_top_of_the_cabinet\": 84, \"open_the_top_drawer_and_put_the_bowl_inside\": 30, \"put_the_bowl_on_top_of_the_cabinet\": 98, \"push_the_plate_to_the_front_of_the_stove\": 88, \"put_the_cream_cheese_in_the_bowl\": 70, \"turn_on_the_stove\": 98, \"put_the_bowl_on_the_plate\": 86, \"put_the_wine_bottle_on_the_rack\": 70}}, \"conclusion\": \"success\"}, \"eval_openvla_attn_k07_object_seed42_v2\": {\"status\": \"DONE\", \"conclusion\": \"failed\", \"metrics\": {\"status\": \"CRASHED at Task 7/10 ep 10/50\", \"completed_tasks\": 6, \"total_tasks\": 10, \"partial_per_task_sr\": {\"task1_alphabet_soup\": 0.38, \"task2_cream_cheese\": 0.12, \"task3_salad_dressing\": 0.66, \"task4_bbq_sauce\": 0.3, \"task5_ketchup\": 0.62, \"task6_tomato_sauce\": 0.32}, \"partial_avg_sr\": 0.4, \"note\": \"Process silently died during Task 7 (no error/traceback in log). Likely OOM or external kill. v2 was already a re-run of v1 which also crashed at Task 6.\"}}, \"eval_pi05_random_k085_long_seed42\": {\"conclusion\": \"negative\", \"metrics\": {\"overall_SR\": 0.444, \"total_episodes\": 500, \"total_successes\": 222}, \"status\": \"DONE\"}, \"eval_openvla_attn_k085_goal_seed42_v3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 74.6, \"per_task\": {\"T1_open_drawer\": 52, \"T2_bowl_stove\": 88, \"T3_wine_cabinet\": 76, \"T4_drawer_bowl\": 44, \"T5_bowl_cabinet\": 98, \"T6_plate_stove\": 84, \"T7_cream_bowl\": 74, \"T8_stove_on\": 94, \"T9_bowl_plate\": 78, \"T10_wine_rack\": 58}}}, \"eval_openvla_l2norm_k095_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 70.6, \"per_task\": {\"T1_alphabet_soup\": 48, \"T2_cream_cheese\": 52, \"T3_salad_dressing\": 82, \"T4_bbq_sauce\": 60, \"T5_ketchup\": 88, \"T6_tomato_sauce\": 66, \"T7_butter\": 54, \"T8_milk\": 84, \"T9_chocolate_pudding\": 86, \"T10_orange_juice\": 86}}}, \"eval_openvla_l2norm_k085_goal_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 75.4, \"per_task\": {\"T1_open_drawer\": 66, \"T2_bowl_stove\": 96, \"T3_wine_cabinet\": 74, \"T4_drawer_bowl\": 30, \"T5_bowl_cabinet\": 96, \"T6_plate_stove\": 78, \"T7_cream_bowl\": 74, \"T8_stove_on\": 94, \"T9_bowl_plate\": 84, \"T10_wine_rack\": 62}}}, \"eval_pi05_attention_k085_long_seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_openvla_random_k07_goal_seed42_v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_openvla_attn_k085_long_seed42_v3\": {\"conclusion\": \"killed\", \"metrics\": {\"k_ratio\": 0.85, \"mode\": \"attention_prune\", \"note\": \"result file misnamed as openvla_l2norm_prune_k085_10.json, actual mode is attention_prune\", \"overall_sr\": 45.8, \"seed\": 42, \"suite\": \"libero_10\", \"total_episodes\": 500, \"total_successes\": 229}, \"status\": \"DONE\"}, \"eval_openvla_random_k07_goal_seed42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_openvla_attn_k085_long_seed42_v2\": {\"conclusion\": \"killed\", \"status\": \"DONE\"}, \"eval_openvla_attn_k085_long_seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_openvla_attn_k09_goal_seed43_v4\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 73.2, \"total_successes\": 366, \"total_episodes\": 500, \"per_task_sr\": {\"T0_open_middle_drawer\": 50, \"T1_put_bowl_on_stove\": 86, \"T2_put_wine_bottle_on_cabinet\": 88, \"T3_open_drawer_put_bowl\": 40, \"T4_put_bowl_on_cabinet\": 94, \"T5_push_plate_to_stove\": 84, \"T6_put_cream_cheese_in_bowl\": 66, \"T7_turn_on_stove\": 98, \"T8_put_bowl_on_plate\": 78, \"T9_put_wine_bottle_on_rack\": 48}, \"elapsed_minutes\": 205.3, \"seed\": 43}}, \"eval_pi05_random_k05_long_seed42_v3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 50.2, \"total_successes\": 251, \"total_episodes\": 500, \"per_task_sr\": {\"T0_alphabet_soup_tomato\": 84, \"T1_cream_cheese_butter\": 32, \"T2_stove_moka_pot\": 64, \"T3_black_bowl_drawer\": 72, \"T4_white_mug_left_plate\": 74, \"T5_book_back_shelf\": 38, \"T6_white_mug_plate\": 30, \"T7_alphabet_soup_cream\": 54, \"T8_moka_pots_stove\": 4, \"T9_yellow_mug_microwave\": 50}, \"elapsed_minutes\": 252.3, \"seed\": 42}}, \"eval_pi05_l2norm_k05_long_seed42_v4\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 50, \"total_successes\": 250, \"total_episodes\": 500, \"per_task_sr\": {\"T0_alphabet_soup_tomato\": 66, \"T1_cream_cheese_butter\": 52, \"T2_stove_moka_pot\": 74, \"T3_black_bowl_drawer\": 38, \"T4_white_mug_left_plate\": 30, \"T5_book_back_shelf\": 50, \"T6_white_mug_plate\": 32, \"T7_alphabet_soup_cream\": 60, \"T8_moka_pots_stove\": 16, \"T9_yellow_mug_microwave\": 82}, \"elapsed_minutes\": 249.4, \"seed\": 42}}, \"eval_openvla_attn_k085_object_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"elapsed_minutes\": 259.3, \"per_task\": {\"alphabet_soup\": 0.66, \"bbq_sauce\": 0.36, \"butter\": 0.36, \"chocolate_pudding\": 0.88, \"cream_cheese\": 0.36, \"ketchup\": 0.74, \"milk\": 0.52, \"orange_juice\": 0.74, \"salad_dressing\": 0.52, \"tomato_sauce\": 0.36}, \"success_rate\": 0.55, \"total_episodes\": 500, \"total_successes\": 275}, \"status\": \"DONE\"}, \"eval_openvla_l2norm_k09_goal_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 75.2, \"total_successes\": 376, \"total_episodes\": 500, \"per_task_sr\": {\"T0_open_middle_drawer\": 66, \"T1_put_bowl_on_stove\": 92, \"T2_put_wine_bottle_on_cabinet\": 82, \"T3_open_drawer_put_bowl\": 38, \"T4_put_bowl_on_cabinet\": 94, \"T5_push_plate_to_stove\": 72, \"T6_put_cream_cheese_in_bowl\": 74, \"T7_turn_on_stove\": 94, \"T8_put_bowl_on_plate\": 80, \"T9_put_wine_bottle_on_rack\": 60}, \"elapsed_minutes\": 185.7, \"seed\": 43}}, \"eval_openvla_random_k09_goal_seed43\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 80.4, \"total_successes\": 402, \"total_episodes\": 500, \"per_task_sr\": {\"T0_open_middle_drawer\": 70, \"T1_put_bowl_on_stove\": 98, \"T2_put_wine_bottle_on_cabinet\": 92, \"T3_open_drawer_put_bowl\": 42, \"T4_put_bowl_on_cabinet\": 94, \"T5_push_plate_to_stove\": 78, \"T6_put_cream_cheese_in_bowl\": 82, \"T7_turn_on_stove\": 100, \"T8_put_bowl_on_plate\": 74, \"T9_put_wine_bottle_on_rack\": 74}, \"elapsed_minutes\": 175.5, \"seed\": 43}}, \"eval_openvla_l2norm_k09_goal_seed43_v3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.752, \"total_successes\": 376, \"total_episodes\": 500, \"per_task_sr\": {\"T0_open_middle_drawer\": 0.66, \"T1_put_bowl_on_stove\": 0.92, \"T2_put_wine_bottle_on_cabinet\": 0.82, \"T3_open_drawer_put_bowl\": 0.38, \"T4_put_bowl_on_cabinet\": 0.94, \"T5_push_plate_to_stove\": 0.72, \"T6_put_cream_cheese_in_bowl\": 0.74, \"T7_turn_on_stove\": 0.94, \"T8_put_bowl_on_plate\": 0.8, \"T9_put_wine_bottle_on_rack\": 0.6}, \"elapsed_minutes\": 210.5, \"seed\": 43}}, \"eval_openvla_attn_k07_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_pi05_attention_k075_long_seed42\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 51.8, \"total_successes\": 259, \"total_episodes\": 500, \"per_task_sr\": {\"T0_alphabet_soup_tomato\": 68, \"T1_cream_cheese_butter\": 78, \"T2_stove_moka_pot\": 56, \"T3_black_bowl_drawer\": 42, \"T4_white_mug_plate\": 36, \"T5_book_back\": 44, \"T6_white_mug_plate_2\": 80, \"T7_alphabet_soup_cream\": 30, \"T8_moka_pots_stove\": 6, \"T9_yellow_white_mug_microwave\": 78}}, \"conclusion\": \"success\"}, \"eval_openvla_l2norm_k09_goal_seed43_v2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_openvla_baseline_spatial_seed42_v4\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_openvla_l2norm_k07_object_seed42_v3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.498, \"total_episodes\": 500, \"total_successes\": 249, \"task_srs\": {\"task1\": 0.46, \"task2\": 0.66, \"task3\": 0.48, \"task4\": 0.32, \"task5\": 0.76, \"task6\": 0.62, \"task7\": 0.28, \"task8\": 0.56, \"task9\": 0.46, \"task10\": 0.68}}}, \"eval_pi05_random_k075_long_seed42_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"success_rate\": 62.4, \"suite\": \"libero_10\", \"tasks_completed\": 10, \"total_episodes\": 500}}, \"eval_smolvla_official_l2norm_k070_object_seed42\": {\"conclusion\": \"killed\", \"metrics\": {\"overall_sr\": 0, \"per_task_sr\": {\"task0\": 0, \"task1\": 0, \"task2\": 0, \"task3\": 0, \"task4\": 0, \"task5\": 0, \"task6\": 0, \"task7\": 0, \"task8\": 0, \"task9\": 0}, \"total_episodes\": 500, \"total_successes\": 0, \"wilson_ci_95\": [0, 0.0076]}, \"status\": \"DONE\"}, \"eval_pi05_zeromask_random_k09_object_seed42_v3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.98, \"total_successes\": 490, \"total_episodes\": 500, \"elapsed_min\": 83.05, \"per_task_sr\": {\"T0_alphabet_soup\": 0.96, \"T1_cream_cheese\": 0.96, \"T2_salad_dressing\": 1, \"T3_bbq_sauce\": 0.94, \"T4_ketchup\": 0.98, \"T5_tomato_sauce\": 1, \"T6_butter\": 1, \"T7_milk\": 0.98, \"T8_chocolate_pudding\": 1, \"T9_orange_juice\": 0.98}}}, \"eval_pi05_random_k05_long_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"elapsed_min\": 157.7, \"overall_sr\": 0.502, \"total_episodes\": 500, \"total_successes\": 251}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k05_long_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"elapsed_min\": 158, \"success_rate\": 0.502, \"total_episodes\": 500, \"total_successes\": 251}, \"status\": \"DONE\"}, \"eval_openvla_random_k05_long_seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_openvla_attn_k09_goal_seed43_v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_pi05_l2norm_k03_goal_seed42_postfix\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.518, \"total_successes\": 259, \"total_episodes\": 500, \"n_tasks\": 10, \"seed\": 42}, \"conclusion\": \"success\"}, \"l2norm_k05_object_s42\": {\"conclusion\": \"success\", \"metrics\": {\"elapsed_minutes\": 264.6, \"k_ratio\": 0.5, \"overall_success_rate\": 0.392, \"per_task\": {\"alphabet_soup\": 0.56, \"bbq_sauce\": 0.32, \"butter\": 0.12, \"chocolate_pudding\": 0.44, \"cream_cheese\": 0.14, \"ketchup\": 0.7, \"milk\": 0.5, \"orange_juice\": 0.44, \"salad_dressing\": 0.38, \"tomato_sauce\": 0.32}, \"seed\": 42, \"total_episodes\": 500, \"total_successes\": 196, \"vision_tokens\": \"256->128\"}, \"status\": \"DONE\"}, \"eval_xvla_random_k05_spatial_seed43\": {\"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.726, \"total_episodes\": 500, \"total_successes\": 363, \"wilson_ci_95\": [0.685, 0.763], \"elapsed_min\": 64.3}, \"status\": \"DONE\"}, \"eval_openvla_baseline_goal_seed43\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.776, \"total_successes\": 388, \"total_episodes\": 500, \"elapsed_minutes\": 193, \"seed\": 43, \"per_task_sr\": {\"T1_open_middle_drawer\": 0.58, \"T2_put_bowl_on_stove\": 0.96, \"T3_put_wine_bottle_on_cabinet\": 0.82, \"T4_open_top_drawer_put_bowl\": 0.58, \"T5_put_bowl_on_cabinet\": 0.98, \"T6_push_plate_front_stove\": 0.8, \"T7_put_cream_cheese_in_bowl\": 0.66, \"T8_turn_on_stove\": 0.98, \"T9_put_bowl_on_plate\": 0.86, \"T10_put_wine_bottle_on_rack\": 0.54}}, \"conclusion\": \"success\"}, \"eval_openvla_l2norm_k07_long_seed42_v2\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.312, \"task_srs\": [0.42, 0.34, 0.36, 0.16, 0.2, 0.58, 0.42, 0.4, 0.08, 0.16], \"n_episodes\": 500, \"n_tasks\": 10, \"time_min\": 563}, \"conclusion\": \"success\"}, \"eval_openvla_random_k07_object_seed42_v3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_pi05_attention_k0925_long_seed42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_pi05_l2norm_k075_long_seed42_v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_pi05_zeromask_random_k09_object_seed42_v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_pi05_random_k075_long_seed42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_openvla_l2norm_k085_long_seed42_v2\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.388, \"total_episodes\": 500, \"total_successes\": 194, \"elapsed_minutes\": 521.4, \"seed\": 42, \"k_ratio\": 0.85, \"suite\": \"libero_10_long\", \"per_task_sr\": {\"task1_alphabet_soup_tomato_sauce_basket\": 0.62, \"task2_cream_cheese_butter_basket\": 0.48, \"task3_stove_moka_pot\": 0.44, \"task4_black_bowl_drawer_close\": 0.28, \"task5_white_mug_left_yellow_mug_right\": 0.18, \"task6_book_caddy\": 0.84, \"task7_white_mug_plate_chocolate_pudding\": 0.3, \"task8_alphabet_soup_cream_cheese_basket\": 0.38, \"task9_both_moka_pots_stove\": 0.2, \"task10_yellow_mug_microwave_close\": 0.16}}, \"conclusion\": \"success\"}, \"eval_openvla_random_k07_long_seed42_v2\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.388, \"total_successes\": 194, \"total_episodes\": 500, \"elapsed_minutes\": 516.7, \"seed\": 42, \"per_task_sr\": {\"put both the alphabet soup and the tomato sauce in the basket\": 0.48, \"put both the cream cheese box and the butter in the basket\": 0.46, \"turn on the stove and put the moka pot on it\": 0.58, \"put the black bowl in the bottom drawer of the cabinet and close it\": 0.34, \"put the white mug on the left plate and put the yellow and white mug on the right plate\": 0.14, \"pick up the book and place it in the back compartment of the caddy\": 0.68, \"put the white mug on the plate and put the chocolate pudding to the right of the plate\": 0.42, \"put both the alphabet soup and the cream cheese box in the basket\": 0.34, \"put both moka pots on the stove\": 0.24, \"put the yellow and white mug in the microwave and close it\": 0.2}}, \"conclusion\": \"success\"}, \"eval_openvla_attn_k085_long_seed42_v4\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_openvla_random_k07_object_seed42_v2\": {\"conclusion\": \"success\", \"metrics\": {\"elapsed_minutes\": 274.4, \"overall_sr\": 0.444, \"per_task\": {\"alphabet_soup\": 0.72, \"bbq_sauce\": 0.38, \"butter\": 0.2, \"chocolate_pudding\": 0.34, \"cream_cheese\": 0.2, \"ketchup\": 0.64, \"milk\": 0.24, \"orange_juice\": 0.64, \"salad_dressing\": 0.56, \"tomato_sauce\": 0.52}, \"total_episodes\": 500, \"total_successes\": 222}, \"status\": \"DONE\"}, \"eval_openvla_random_k085_long_seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_openvla_attn_k09_goal_seed43\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"profiling_pi05_latency_westd41074\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"k1.0_median_ms\": 209.88, \"k1.0_p5_ms\": 197.76, \"k1.0_p95_ms\": 221.67, \"k0.9_median_ms\": 206.36, \"k0.9_p5_ms\": 171.43, \"k0.9_p95_ms\": 225.03, \"k0.5_median_ms\": 201.87, \"k0.5_p5_ms\": 189.21, \"k0.5_p95_ms\": 211.31, \"k0.9_speedup_pct\": 1.7, \"k0.5_speedup_pct\": 4}}, \"eval_openvla_zeromask_l2norm_k09_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_SR\": 0.688, \"per_task_SR\": {\"alphabet_soup\": 0.84, \"cream_cheese\": 0.62, \"salad_dressing\": 0.88, \"bbq_sauce\": 0.26, \"ketchup\": 0.82, \"tomato_sauce\": 0.54, \"butter\": 0.62, \"milk\": 0.82, \"chocolate_pudding\": 0.6, \"orange_juice\": 0.88}, \"total_episodes\": 500, \"total_successes\": 344}}, \"eval_pi05_l2norm_k0925_long_seed42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_openvla_l2norm_k05_object_seed42_v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_openvla_zeromask_random_k09_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.718, \"per_task\": {\"alphabet_soup\": 0.9, \"cream_cheese\": 0.54, \"salad_dressing\": 0.78, \"bbq_sauce\": 0.62, \"ketchup\": 0.8, \"tomato_sauce\": 0.68, \"butter\": 0.5, \"milk\": 0.74, \"chocolate_pudding\": 0.7, \"orange_juice\": 0.92}, \"elapsed_minutes\": 246.4}}, \"eval_pi05_zeromask_l2norm_k09_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.994, \"total_successes\": 497, \"total_episodes\": 500, \"elapsed_min\": 97.4}}, \"eval_pi05_zeromask_random_k09_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_pi05_l2norm_k0925_long_seed42_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.832, \"total_episodes\": 500, \"elapsed_min\": 168.6, \"per_task_sr\": [0.92, 0.92, 0.68, 0.98, 0.9, 0.94, 0.92, 0.44, 0.98, 0.64]}}, \"profiling_pi05_latency_westd41074_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"profiling_pi05_latency_cqa1\": {\"status\": \"DONE\", \"metrics\": {\"k_1.0_mean_ms\": 200.06, \"k_1.0_std_ms\": 26.33, \"k_0.9_mean_ms\": 206.66, \"k_0.9_std_ms\": 42.1, \"k_0.5_mean_ms\": 185.95, \"k_0.5_std_ms\": 20.01, \"speedup_k09\": 0.968, \"speedup_k05\": 1.076}, \"conclusion\": \"negative\"}, \"eval_pi05_l2norm_k05_long_seed43_postfix_v2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.53, \"total_successes\": 265, \"total_episodes\": 500, \"elapsed_min\": 214.5, \"per_task_sr\": {\"T0_alphabet_soup_tomato\": 0.64, \"T1_cream_cheese_butter\": 0.64, \"T2_stove_moka_pot\": 0.72, \"T3_black_bowl_drawer\": 0.46, \"T4_white_mug_yellow_mug\": 0.4, \"T5_book_caddy\": 0.5, \"T6_white_mug_chocolate\": 0.38, \"T7_alphabet_soup_cream_cheese\": 0.58, \"T8_both_moka_pots\": 0.1, \"T9_yellow_mug_microwave\": 0.88}}}, \"eval_pi05_random_k0925_long_seed42_postfix\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 38.6, \"total_episodes\": 500, \"total_success\": 193, \"per_task_sr\": [22, 66, 42, 44, 22, 52, 4, 50, 4, 80], \"runtime_min\": 257.9}}, \"eval_openvla_random_k07_long_seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_pi05_attention_k09_long_seed42_postfix\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.638, \"total_successes\": 319, \"total_episodes\": 500}}, \"eval_openvla_l2norm_k085_long_seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_openvla_l2norm_k07_long_seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_openvla_random_k05_spatial_seed42\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.5, \"total_episodes\": 500, \"total_success\": 250, \"wall_time_min\": 248.8}}, \"eval_openvla_attn_k07_long_seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_openvla_l2norm_k05_spatial_seed42\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"eval_openvla_attn_k09_object_seed42\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"eval_pi05_random_k07_long_seed43_postfix\": {\"conclusion\": \"success\", \"metrics\": {\"elapsed_min\": 222.9, \"overall_sr\": 0.686, \"per_task_sr\": {\"T0\": 0.92, \"T1\": 0.74, \"T2\": 0.76, \"T3\": 0.7, \"T4\": 0.86, \"T5\": 0.52, \"T6\": 0.7, \"T7\": 0.72, \"T8\": 0.08, \"T9\": 0.86}, \"total_episodes\": 500, \"total_successes\": 343}, \"status\": \"DONE\"}, \"eval_pi05_random_k03_long_seed43_v4\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.272, \"total_successes\": 136, \"total_episodes\": 500, \"elapsed_min\": 284.7}, \"conclusion\": \"success\"}, \"eval_pi05_l2norm_k07_long_seed43_v3\": {\"status\": \"DONE\", \"metrics\": {\"overall_sr\": 0.65, \"total_successes\": 325, \"total_episodes\": 500, \"elapsed_min\": 228.5}, \"conclusion\": \"success\"}, \"eval_openvla_l2norm_k09_long_seed42_v3\": {\"conclusion\": \"success\", \"metrics\": {\"k_ratio\": 0.9, \"mode\": \"l2norm_prune\", \"overall_sr\": 43.6, \"seed\": 42, \"suite\": \"libero_10\", \"total_episodes\": 500, \"total_successes\": 218}, \"status\": \"DONE\"}, \"eval_openvla_attn_k09_long_seed42_v3\": {\"conclusion\": \"success\", \"metrics\": {\"k_ratio\": 0.9, \"mode\": \"attention_prune\", \"note\": \"result file misnamed openvla_l2norm_prune_k09_10.json; backed up to openvla_attn_prune_k09_long_seed42.json\", \"overall_sr\": 44.0, \"seed\": 42, \"suite\": \"libero_10\", \"total_episodes\": 500, \"total_successes\": 220}, \"status\": \"DONE\"}, \"eval_openvla_random_k09_long_seed42_v3\": {\"conclusion\": \"success\", \"metrics\": {\"k_ratio\": 0.9, \"mode\": \"random_prune\", \"note\": \"result file generic name openvla_random_prune_k09_10.json, needs rename\", \"overall_sr\": 46.8, \"seed\": 42, \"suite\": \"libero_10\", \"total_episodes\": 500, \"total_successes\": 234}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k085_long_seed43_v3\": {\"conclusion\": \"success\", \"metrics\": {\"per_task\": {\"T0_put_both_alphabet_soup_and_tomato\": 96, \"T1_put_both_cream_cheese_and_butter\": 92, \"T2_turn_on_stove_put_moka_pot\": 86, \"T3_put_black_bowl_in_bottom_drawer\": 100, \"T4_put_white_mug_on_left_plate\": 78, \"T5_pick_up_book_place_in_back\": 98, \"T6_put_white_mug_on_plate_and_put\": 14, \"T7_put_both_alphabet_soup_and_cream\": 90, \"T8_put_both_moka_pots_on_stove\": 52, \"T9_put_yellow_white_mug_in_microwave\": 94}, \"success_rate\": 80, \"total_episodes\": 500, \"total_successes\": 400}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k09_long_seed43_postfix\": {\"conclusion\": \"success\", \"metrics\": {\"elapsed_min\": 194.3, \"overall_sr\": 0.808, \"per_task_sr\": {\"T0_alphabet_soup_tomato\": 0.92, \"T1_cream_cheese_butter\": 0.96, \"T2_stove_moka\": 0.92, \"T3_black_bowl_drawer\": 1, \"T4_white_mug_plates\": 0.88, \"T5_book_caddy\": 0.96, \"T6_mug_plate_pudding\": 0.14, \"T7_soup_cream_cheese_basket\": 0.82, \"T8_two_moka_stove\": 0.58, \"T9_mug_microwave\": 0.9}, \"total_episodes\": 500, \"total_successes\": 404}, \"status\": \"DONE\"}, \"eval_openvla_prune_random_k03_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"elapsed_minutes\": 374.64, \"k_ratio\": 0.3, \"overall_success_rate\": 0.206, \"seed\": 42, \"suite\": \"libero_object\", \"total_episodes\": 500, \"total_successes\": 103}, \"status\": \"DONE\"}, \"random_k07_seed43_object\": {\"conclusion\": \"success\", \"metrics\": {\"elapsed_minutes\": 270.07, \"k_ratio\": 0.7, \"overall_success_rate\": 0.512, \"per_task\": {\"alphabet_soup\": {\"ep\": 50, \"sr\": 0.74, \"succ\": 37}, \"bbq_sauce\": {\"ep\": 50, \"sr\": 0.56, \"succ\": 28}, \"butter\": {\"ep\": 50, \"sr\": 0.2, \"succ\": 10}, \"chocolate_pudding\": {\"ep\": 50, \"sr\": 0.42, \"succ\": 21}, \"cream_cheese\": {\"ep\": 50, \"sr\": 0.14, \"succ\": 7}, \"ketchup\": {\"ep\": 50, \"sr\": 0.72, \"succ\": 36}, \"milk\": {\"ep\": 50, \"sr\": 0.3, \"succ\": 15}, \"orange_juice\": {\"ep\": 50, \"sr\": 0.84, \"succ\": 42}, \"salad_dressing\": {\"ep\": 50, \"sr\": 0.58, \"succ\": 29}, \"tomato_sauce\": {\"ep\": 50, \"sr\": 0.62, \"succ\": 31}}, \"seed\": 43, \"total_episodes\": 500, \"total_successes\": 256, \"vision_tokens\": 179}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k0925_goal_seed42_postfix\": {\"conclusion\": \"success\", \"metrics\": {\"baseline_sr\": 96.4, \"delta_vs_baseline\": -6.6, \"success_rate\": 89.8, \"total_episodes\": 500}, \"status\": \"DONE\"}, \"eval_openvla_l2norm_k05_object_seed42_v4\": {\"conclusion\": \"success\", \"metrics\": {\"baseline_sr\": 0.74, \"delta_from_baseline\": -0.348, \"elapsed_minutes\": 346.85, \"k_ratio\": 0.5, \"per_task_rates\": {\"alphabet_soup\": 0.56, \"bbq_sauce\": 0.32, \"butter\": 0.12, \"chocolate_pudding\": 0.44, \"cream_cheese\": 0.14, \"ketchup\": 0.7, \"milk\": 0.5, \"orange_juice\": 0.44, \"salad_dressing\": 0.38, \"tomato_sauce\": 0.32}, \"success_rate\": 0.392, \"total_episodes\": 500, \"total_successes\": 196, \"vision_tokens_kept\": 128, \"vision_tokens_total\": 256}, \"status\": \"DONE\"}, \"eval_pi05_random_k085_long_seed42_postfix_v3\": {\"conclusion\": \"success\", \"metrics\": {\"per_task_sr\": {\"T0_alphabet_soup_tomato\": 52, \"T1_cream_cheese_butter\": 46, \"T2_stove_moka_pot\": 66, \"T3_black_bowl_drawer\": 74, \"T4_white_mug_left_plate\": 24, \"T5_book_back_shelf\": 44, \"T6_white_mug_plate\": 52, \"T7_alphabet_soup_cream\": 52, \"T8_both_moka_pots_stove\": 12, \"T9_yellow_white_mug_microwave\": 72}, \"success_rate\": 49.4, \"total_episodes\": 500, \"total_successes\": 247}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k085_long_seed42_postfix_v3\": {\"conclusion\": \"success\", \"metrics\": {\"per_task\": {\"T0_alphabet_soup_tomato\": 0.98, \"T1_cream_cheese_butter\": 0.94, \"T2_stove_moka\": 0.82, \"T3_black_bowl_drawer\": 1, \"T4_white_mug_yellow_mug\": 0.72, \"T5_book_caddy\": 0.96, \"T6_white_mug_chocolate\": 0.08, \"T7_alphabet_soup_cream_cheese\": 0.8, \"T8_both_moka_pots\": 0.56, \"T9_yellow_white_mug_microwave\": 0.94}, \"success_rate\": 0.78, \"total_episodes\": 500, \"total_successes\": 390}, \"status\": \"DONE\"}, \"eval_openvla_random_k09_spatial_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"elapsed_min\": 252.4, \"overall_sr\": 79.8, \"total_episodes\": 500, \"total_successes\": 399}, \"status\": \"DONE\"}, \"eval_openvla_random_k09_goal_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"elapsed_min\": 246.2, \"overall_sr\": 79.6, \"per_task\": {\"T0_open_middle_drawer_cabinet\": {\"episodes\": 50, \"sr\": 74, \"successes\": 37}, \"T1_put_bowl_on_stove\": {\"episodes\": 50, \"sr\": 96, \"successes\": 48}, \"T2_put_wine_bottle_top_cabinet\": {\"episodes\": 50, \"sr\": 84, \"successes\": 42}, \"T3_open_top_drawer_put_bowl_in\": {\"episodes\": 50, \"sr\": 38, \"successes\": 19}, \"T4_put_bowl_top_cabinet\": {\"episodes\": 50, \"sr\": 94, \"successes\": 47}, \"T5_push_plate_front_stove\": {\"episodes\": 50, \"sr\": 72, \"successes\": 36}, \"T6_put_cream_cheese_in_bowl\": {\"episodes\": 50, \"sr\": 78, \"successes\": 39}, \"T7_turn_on_stove\": {\"episodes\": 50, \"sr\": 100, \"successes\": 50}, \"T8_put_bowl_on_plate\": {\"episodes\": 50, \"sr\": 86, \"successes\": 43}, \"T9_put_wine_bottle_on_rack\": {\"episodes\": 50, \"sr\": 74, \"successes\": 37}}, \"total_episodes\": 500, \"total_successes\": 398}, \"status\": \"DONE\"}, \"eval_pi05_random_k085_goal_seed42_postfix_v3\": {\"conclusion\": \"success\", \"metrics\": {\"elapsed_min\": 139.3, \"overall_sr\": 53, \"per_task\": {\"T0_open_middle_drawer_cabinet\": {\"episodes\": 50, \"sr\": 84, \"successes\": 42}, \"T1_put_bowl_on_stove\": {\"episodes\": 50, \"sr\": 2, \"successes\": 1}, \"T2_put_wine_bottle_top_cabinet\": {\"episodes\": 50, \"sr\": 18, \"successes\": 9}, \"T3_open_top_drawer_put_bowl_in\": {\"episodes\": 50, \"sr\": 34, \"successes\": 17}, \"T4_put_bowl_top_cabinet\": {\"episodes\": 50, \"sr\": 54, \"successes\": 27}, \"T5_push_plate_front_stove\": {\"episodes\": 50, \"sr\": 76, \"successes\": 38}, \"T6_put_cream_cheese_in_bowl\": {\"episodes\": 50, \"sr\": 82, \"successes\": 41}, \"T7_turn_on_stove\": {\"episodes\": 50, \"sr\": 88, \"successes\": 44}, \"T8_put_bowl_on_plate\": {\"episodes\": 50, \"sr\": 84, \"successes\": 42}, \"T9_put_wine_bottle_on_rack\": {\"episodes\": 50, \"sr\": 8, \"successes\": 4}}, \"total_episodes\": 500, \"total_successes\": 265}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k085_object_seed42_postfix_v2\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 98.4, \"total_episodes\": 500}, \"status\": \"DONE\"}, \"eval_openvla_random_k09_object_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"elapsed_minutes\": 246.3, \"overall_success_rate\": 0.628, \"total_episodes\": 500, \"total_successes\": 314}, \"status\": \"DONE\"}, \"eval_openvla_baseline_object_seed42_v2\": {\"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.74, \"total_episodes\": 500}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k085_long_seed42_postfix_v2\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"eval_pi05_l2norm_k085_object_seed42_postfix\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"eval_pi05_random_k085_long_seed42_postfix_v2\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"eval_pi05_random_k085_goal_seed42_postfix_v2\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"eval_openvla_l2norm_k09_long_seed42_v2\": {\"conclusion\": \"killed\", \"status\": \"DONE\"}, \"eval_openvla_random_k09_long_seed42_v2\": {\"conclusion\": \"killed\", \"status\": \"DONE\"}, \"eval_openvla_attn_k09_long_seed42_v2\": {\"conclusion\": \"killed\", \"status\": \"DONE\"}, \"eval_openvla_random_k09_long_seed42\": {\"conclusion\": \"killed\", \"status\": \"DONE\"}, \"eval_pi05_l2norm_k085_long_seed43_postfix_v2\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"eval_openvla_l2norm_k09_long_seed42\": {\"conclusion\": \"killed\", \"status\": \"DONE\"}, \"eval_pi05_random_k085_object_seed42_postfix\": {\"conclusion\": \"success\", \"metrics\": {\"per_task_sr\": {\"T0_alphabet_soup\": 6, \"T1_cream_cheese\": 2, \"T2_salad_dressing\": 2, \"T3_bbq_sauce\": 2, \"T4_ketchup\": 12, \"T5_tomato_sauce\": 8, \"T6_butter\": 4, \"T7_milk\": 8, \"T8_chocolate_pudding\": 4, \"T9_orange_juice\": 8}, \"success_rate\": 5.6, \"total_episodes\": 500, \"total_successes\": 28}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k085_goal_seed42_postfix\": {\"conclusion\": \"success\", \"metrics\": {\"T0_open_drawer\": 90, \"T1_bowl_stove\": 92, \"T2_wine_cabinet\": 98, \"T3_drawer_bowl\": 84, \"T4_bowl_cabinet\": 100, \"T5_push_plate\": 94, \"T6_cream_bowl\": 88, \"T7_turn_stove\": 100, \"T8_bowl_plate\": 84, \"T9_wine_rack\": 44, \"overall_sr\": 87.4, \"total_episodes\": 500, \"total_successes\": 437}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k085_goal_seed43_postfix\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 87, \"total_episodes\": 500, \"total_successes\": 435}, \"status\": \"DONE\"}, \"eval_pi05_random_k085_long_seed43_v2\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 42, \"total_episodes\": 500, \"total_successes\": 210}, \"status\": \"DONE\"}, \"eval_pi05_random_k085_spatial_seed43_postfix\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 59.2, \"total_episodes\": 500, \"total_successes\": 296}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k085_object_seed43_postfix\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 99, \"total_episodes\": 500, \"total_successes\": 495}, \"status\": \"DONE\"}, \"eval_openvla_l2norm_k09_spatial_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.75, \"total_episodes\": 500}, \"status\": \"DONE\"}, \"eval_openvla_l2norm_k09_goal_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.748, \"total_episodes\": 500}, \"status\": \"DONE\"}, \"eval_openvla_baseline_spatial\": {\"conclusion\": \"success\", \"metrics\": {\"elapsed_minutes\": 209.9, \"model\": \"openvla-7b-finetuned-libero-spatial\", \"seed\": 42, \"success_rate\": 0.8, \"suite\": \"libero_spatial\", \"total_episodes\": 500, \"total_successes\": 400}, \"status\": \"DONE\"}, \"eval_pi05_random_k085_goal_seed43_postfix\": {\"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.534, \"total_episodes\": 500, \"total_successes\": 267}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k085_spatial_seed43_postfix\": {\"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.882, \"total_episodes\": 500, \"total_successes\": 441}, \"status\": \"DONE\"}, \"eval_openvla_attn_k09_long_seed42\": {\"conclusion\": \"killed\", \"status\": \"DONE\"}, \"eval_openvla_random_k09_spatial_seed42_v2\": {\"conclusion\": \"killed\", \"status\": \"DONE\"}, \"eval_openvla_random_k09_goal_seed42_v2\": {\"conclusion\": \"killed\", \"status\": \"DONE\"}, \"eval_openvla_attn_k085_spatial_seed42_v2\": {\"conclusion\": \"killed\", \"status\": \"DONE\"}, \"eval_openvla_attn_k085_goal_seed42_v2\": {\"conclusion\": \"killed\", \"status\": \"DONE\"}, \"eval_openvla_attn_k085_spatial_seed42\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"eval_openvla_attn_k085_goal_seed42\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"eval_pi05_random_k085_object_seed43_postfix\": {\"conclusion\": \"success\", \"metrics\": {\"elapsed_min\": 164.83, \"overall_sr\": 0.048, \"total_episodes\": 500, \"total_successes\": 24}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k085_long_seed43_postfix\": {\"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 78.6, \"total_episodes\": 500}, \"status\": \"DONE\"}, \"pi05_baseline_long_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 92.8, \"total_episodes\": 500}, \"status\": \"DONE\"}, \"eval_pi05_baseline_spatial_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 97.2, \"total_episodes\": 500}, \"status\": \"DONE\"}, \"eval_pi05_baseline_long_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"note\": \"Result from westd-38929 run (2026-05-22). Original cqa1-33015 run was stale. Second cqa1-33015 run=91.6%.\", \"overall_sr\": 92.8, \"per_task\": {\"alphabet_soup_cream_cheese_basket\": 0.9, \"alphabet_soup_tomato_basket\": 0.96, \"book_in_caddy\": 0.98, \"bowl_bottom_drawer\": 1, \"cream_cheese_butter_basket\": 0.96, \"moka_pots_stove\": 0.64, \"mug_microwave\": 0.98, \"mug_plate_chocolate\": 0.88, \"mugs_on_plates\": 1, \"stove_moka_pot\": 0.98}, \"source_file\": \"westd-38929:/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_baseline_libero_10_seed42.json\", \"total_episodes\": 500, \"total_successes\": 464}, \"status\": \"DONE\"}, \"eval_pi05_baseline_object_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 98.2, \"per_task\": {\"alphabet_soup\": 0.96, \"bbq_sauce\": 1, \"butter\": 1, \"chocolate_pudding\": 1, \"cream_cheese\": 0.98, \"ketchup\": 0.94, \"milk\": 0.98, \"orange_juice\": 0.98, \"salad_dressing\": 0.98, \"tomato_sauce\": 1}, \"source_file\": \"westd-41074:/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_baseline_libero_object.json\", \"total_episodes\": 500, \"total_successes\": 491}, \"status\": \"DONE\"}, \"eval_pi05_random_k09_spatial_seed43_postfix_v2\": {\"conclusion\": \"success\", \"metrics\": {\"elapsed_min\": 94.1, \"overall_sr\": 54, \"per_task_sr\": {\"T0\": 92, \"T1\": 44, \"T2\": 76, \"T3\": 10, \"T4\": 28, \"T5\": 58, \"T6\": 56, \"T7\": 72, \"T8\": 76, \"T9\": 28}, \"total_episodes\": 500}, \"status\": \"DONE\"}, \"eval_pi05_random_k05_long_seed43_postfix\": {\"conclusion\": \"success\", \"metrics\": {\"elapsed_min\": 250.5, \"overall_sr\": 46.8, \"per_task_sr\": {\"T0\": 72, \"T1\": 34, \"T2\": 64, \"T3\": 68, \"T4\": 58, \"T5\": 26, \"T6\": 36, \"T7\": 64, \"T8\": 6, \"T9\": 40}, \"result_json\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_random_k0.50_libero_10_seed43.json\", \"total_episodes\": 500}, \"status\": \"DONE\"}, \"eval_openvla_attn_k09_goal_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"elapsed_min\": 198.3, \"overall_sr\": 0.732, \"per_task_sr\": [0.62, 0.86, 0.8, 0.3, 0.96, 0.8, 0.7, 0.98, 0.82, 0.48], \"total_episodes\": 500}, \"status\": \"DONE\"}, \"eval_openvla_attn_k09_spatial_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"elapsed_min\": 190.8, \"overall_sr\": 0.804, \"per_task_sr\": [0.88, 0.9, 0.9, 0.94, 0.74, 0.24, 0.96, 0.9, 0.78, 0.8], \"total_episodes\": 500}, \"status\": \"DONE\"}, \"eval_openvla_attn_k09_object_seed42_v3\": {\"conclusion\": \"success\", \"metrics\": {\"elapsed_minutes\": 260.6, \"k_ratio\": 0.9, \"overall_success_rate\": 0.614, \"per_task_sr\": {\"alphabet_soup\": 0.74, \"bbq_sauce\": 0.38, \"butter\": 0.28, \"chocolate_pudding\": 0.74, \"cream_cheese\": 0.46, \"ketchup\": 0.76, \"milk\": 0.52, \"orange_juice\": 0.76, \"salad_dressing\": 0.76, \"tomato_sauce\": 0.74}, \"total_episodes\": 500, \"total_successes\": 307, \"vision_tokens_kept\": 230, \"vision_tokens_original\": 256}, \"status\": \"DONE\"}, \"eval_pi05_random_k095_long_seed43_postfix\": {\"conclusion\": \"success\", \"metrics\": {\"elapsed_min\": 236.8, \"overall_sr\": 0.584, \"per_task_sr\": {\"T0_alphabet_soup_tomato\": 0.5, \"T1_cream_cheese_butter\": 0.88, \"T2_stove_moka\": 0.62, \"T3_black_bowl_drawer\": 0.8, \"T4_white_mug_plates\": 0.42, \"T5_book_caddy\": 0.9, \"T6_mug_plate_pudding\": 0.06, \"T7_alphabet_soup_cream_cheese\": 0.58, \"T8_moka_pots_stove\": 0.18, \"T9_mug_microwave\": 0.9}, \"total_episodes\": 500, \"total_successes\": 292}, \"status\": \"DONE\"}, \"eval_pi05_random_k09_object_seed43_postfix\": {\"conclusion\": \"success\", \"metrics\": {\"elapsed_min\": 113.8, \"per_task_sr\": {\"alphabet_soup\": 4, \"bbq_sauce\": 6, \"butter\": 4, \"chocolate_pudding\": 4, \"cream_cheese\": 16, \"ketchup\": 2, \"milk\": 4, \"orange_juice\": 12, \"salad_dressing\": 4, \"tomato_sauce\": 18}, \"success_rate\": 7.4, \"total_episodes\": 500, \"total_successes\": 37}, \"status\": \"DONE\"}, \"eval_pi05_random_k09_goal_seed43_postfix\": {\"conclusion\": \"success\", \"metrics\": {\"per_task_sr\": [74, 30, 38, 48, 92, 92, 82, 86, 64, 6], \"success_rate\": 61.2}, \"status\": \"DONE\"}, \"eval_pi05_random_k09_spatial_seed43_postfix\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"eval_pi05_l2norm_k03_long_seed43_postfix_v2\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 39.2, \"total_episodes\": 500, \"total_success\": 196}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k09_object_seed43_postfix\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 98.4, \"task_sr\": {\"T0\": 100, \"T1\": 100, \"T2\": 96, \"T3\": 100, \"T4\": 98, \"T5\": 96, \"T6\": 96, \"T7\": 98, \"T8\": 100, \"T9\": 100}}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k09_goal_seed43_postfix\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 91}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k09_spatial_seed43_postfix\": {\"conclusion\": \"success\", \"metrics\": {\"per_task\": [100, 100, 98, 100, 84, 92, 100, 98, 100, 90], \"success_rate\": 96.2}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k05_long_seed43_postfix\": {\"conclusion\": \"success\", \"metrics\": {\"SR\": 0.526, \"per_task_SR\": {\"T0_alphabet_soup_tomato\": 0.66, \"T1_cream_cheese_butter\": 0.54, \"T2_stove_moka_pot\": 0.82, \"T3_black_bowl_drawer\": 0.38, \"T4_white_mug_left_plate\": 0.32, \"T5_book_back\": 0.62, \"T6_white_mug_plate\": 0.24, \"T7_alphabet_soup_cream\": 0.56, \"T8_moka_pots_stove\": 0.22, \"T9_yellow_white_mug_microwave\": 0.9}, \"total_episodes\": 500, \"total_successes\": 263}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k05_long_seed42_postfix\": {\"conclusion\": \"success\", \"metrics\": {\"SR\": 0.502, \"total_episodes\": 500, \"total_successes\": 251}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k03_long_seed42_postfix_v2\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"eval_pi05_l2norm_k07_long_seed42_postfix\": {\"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 62.6}, \"status\": \"DONE\"}, \"eval_pi05_random_k03_long_seed42_postfix\": {\"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 29.6}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k07_long_seed43_postfix\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"eval_openvla_simplerenv_l2norm_k09\": {\"conclusion\": \"negative\", \"metrics\": {\"PutCarrotOnPlate_SR\": 0, \"PutEggplantInBasket_SR\": 0, \"PutSpoonOnTableCloth_SR\": 0, \"StackGreenCubeOnYellowCube_SR\": 0, \"avg_SR\": 0, \"episodes_per_task\": 50}, \"status\": \"DONE\"}, \"eval_openvla_simplerenv_baseline\": {\"conclusion\": \"negative\", \"metrics\": {\"PutCarrotOnPlate_SR\": 0, \"PutEggplantInBasket_SR\": 0, \"PutSpoonOnTableCloth_SR\": 0, \"StackGreenCubeOnYellowCube_SR\": 0, \"avg_SR\": 0, \"episodes_per_task\": 50}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k09_long_seed42_postfix_v2\": {\"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 80}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k095_long_seed43_postfix\": {\"conclusion\": \"success\", \"metrics\": {\"n_episodes\": 50, \"overall_sr\": 87.4, \"per_task\": [98, 98, 94, 98, 96, 96, 52, 94, 54, 94], \"suite\": \"libero_10\"}, \"status\": \"DONE\"}, \"eval_smolvla_metaworld_l2norm_sweep\": {\"conclusion\": \"success\", \"metrics\": {\"baseline_sr\": 26.4, \"k0.5_sr\": 0.8, \"k0.85_sr\": 2.4, \"k0.95_sr\": 7.2, \"k0.9_sr\": 10}, \"status\": \"DONE\"}, \"eval_smolvla_metaworld_random_sweep\": {\"conclusion\": \"success\", \"metrics\": {\"baseline_sr\": 26.4, \"k0.5_sr\": 9.6, \"k0.85_sr\": 4.4, \"k0.95_sr\": 6.4, \"k0.9_sr\": 5.6}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k09_long_seed43_postfix_v2\": {\"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 80}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k03_long_seed43_postfix\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"eval_smolvla_metaworld_baseline\": {\"conclusion\": \"success\", \"metrics\": {\"assembly_v3\": 20, \"drawer_open_v3\": 52, \"num_episodes_per_task\": 25, \"overall_sr\": 26.4, \"pick_place_v3\": 8, \"push_v3\": 24, \"reach_v3\": 28, \"wilson_ci_95\": [19.5, 34.7]}, \"status\": \"DONE\"}, \"eval_pi05_random_k09_long_seed42_postfix\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 32, \"task_sr\": {\"T0\": 10, \"T1\": 46, \"T2\": 38, \"T3\": 44, \"T4\": 16, \"T5\": 26, \"T6\": 10, \"T7\": 38, \"T8\": 10, \"T9\": 82}}, \"status\": \"DONE\"}, \"eval_pi05_random_k03_spatial_seed42_postfix_v2\": {\"conclusion\": \"success\", \"metrics\": {\"T1\": 60, \"T2\": 52, \"T3\": 8, \"T4\": 34, \"T5\": 22, \"T6\": 24, \"T7\": 62, \"T8\": 74, \"T9\": 40, \"overall_sr\": 43.4}, \"status\": \"DONE\"}, \"diag_openvla_unnorm_key\": {\"conclusion\": \"success\", \"metrics\": {\"details\": {\"action_required\": \"Script needs --model_path and --unnorm_key args added to support non-object suites\", \"argparse_args\": [\"--mode\", \"--k_ratio\", \"--suite\", \"--num_episodes\", \"--seed\", \"--output\", \"--center_crop\", \"--num_steps_wait\"], \"line_31\": \"CHECKPOINT_PATH = /root/autodl-tmp/openvla-libero-object (hardcoded)\", \"line_32\": \"UNNORM_KEY = libero_object (hardcoded)\", \"missing_args\": [\"--model_path\", \"--unnorm_key\", \"--gpu\"], \"supported_suites\": {\"libero_10\": 520, \"libero_goal\": 300, \"libero_object\": 280, \"libero_spatial\": 280}, \"unnorm_key_usage\": [\"line 111: predict_action(unnorm_key=UNNORM_KEY)\", \"line 257: predict_action(unnorm_key=UNNORM_KEY)\"]}, \"finding\": \"UNNORM_KEY and CHECKPOINT_PATH are hardcoded, no CLI overrides\"}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k095_long_seed42_postfix\": {\"conclusion\": \"success\", \"metrics\": {\"keep_ratio\": 0.95, \"n_episodes\": 50, \"overall_sr\": 87, \"prune_mode\": \"l2norm\", \"suite\": \"libero_10\"}, \"status\": \"DONE\"}, \"eval_pi05_random_k05_long_seed42_postfix\": {\"conclusion\": \"success\", \"metrics\": {\"keep_ratio\": 0.5, \"n_episodes\": 50, \"overall_sr\": 46.8, \"prune_mode\": \"random\", \"suite\": \"libero_10\"}, \"status\": \"DONE\"}, \"eval_pi05_random_k07_long_seed42_postfix\": {\"conclusion\": \"success\", \"metrics\": {\"keep_ratio\": 0.7, \"n_episodes\": 50, \"overall_sr\": 65.8, \"prune_mode\": \"random\", \"suite\": \"libero_10\"}, \"status\": \"DONE\"}, \"eval_pi05_random_k085_long_seed42_postfix\": {\"conclusion\": \"success\", \"metrics\": {\"keep_ratio\": 0.85, \"n_episodes\": 50, \"overall_sr\": 45.2, \"prune_mode\": \"random\", \"suite\": \"libero_10\"}, \"status\": \"DONE\"}, \"eval_pi05_random_k095_long_seed42_postfix\": {\"conclusion\": \"success\", \"metrics\": {\"keep_ratio\": 0.95, \"n_episodes\": 50, \"overall_sr\": 63.2, \"prune_mode\": \"random\", \"suite\": \"libero_10\"}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k03_spatial_seed42_postfix\": {\"conclusion\": \"success\", \"metrics\": {\"keep_ratio\": 0.3, \"n_episodes\": 50, \"overall_sr\": 52.8, \"prune_mode\": \"l2norm\", \"suite\": \"libero_spatial\", \"task_0_sr\": 48, \"task_1_sr\": 80, \"task_2_sr\": 74, \"task_3_sr\": 22, \"task_4_sr\": 28, \"task_5_sr\": 22, \"task_6_sr\": 78, \"task_7_sr\": 84, \"task_8_sr\": 58, \"task_9_sr\": 34}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k09_long_seed42_postfix\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"eval_pi05_l2norm_k085_long_seed42_postfix\": {\"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 78.4, \"per_task\": {\"task0_alphabet_soup_tomato_sauce_basket\": 96, \"task1_cream_cheese_butter_basket\": 92, \"task2_stove_moka_pot\": 86, \"task3_black_bowl_drawer_close\": 100, \"task4_white_mug_left_yellow_mug_right\": 76, \"task5_book_caddy_back\": 96, \"task6_white_mug_plate_chocolate_pudding\": 12, \"task7_alphabet_soup_cream_cheese_basket\": 84, \"task8_both_moka_pots_stove\": 50, \"task9_yellow_white_mug_microwave_close\": 92}, \"total_episodes\": 500, \"total_successes\": 392}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k095_goal_seed42_postfix\": {\"conclusion\": \"success\", \"metrics\": {\"T0_open_middle_drawer\": 84, \"T1_put_bowl_on_stove\": 98, \"T2_put_wine_bottle_on_cabinet\": 90, \"T3_open_top_drawer_put_bowl\": 94, \"T4_put_bowl_on_cabinet\": 100, \"T5_push_plate_front_stove\": 100, \"T6_put_cream_cheese_in_bowl\": 92, \"T7_turn_on_stove\": 100, \"T8_put_bowl_on_plate\": 100, \"T9_put_wine_bottle_on_rack\": 50, \"overall_sr\": 90.8, \"total_episodes\": 500, \"total_successes\": 454}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k07_spatial_seed42_postfix\": {\"conclusion\": \"success\", \"metrics\": {\"SR_overall\": 68.2, \"eval_time_min\": 143.9, \"server\": \"cqa1-33015\", \"tasks\": {\"T0\": 86, \"T1\": 92, \"T2\": 88, \"T3\": 44, \"T4\": 48, \"T5\": 56, \"T6\": 82, \"T7\": 52, \"T8\": 86, \"T9\": 48}, \"total_episodes\": 500, \"total_success\": 341}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k07_object_seed42_postfix\": {\"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 56.4, \"total_episodes\": 500, \"total_successes\": 282}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k07_spatial_seed42_postfix_v2\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"eval_pi05_l2norm_k09_spatial_seed42_postfix\": {\"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 96, \"total_episodes\": 500, \"total_successes\": 480}, \"status\": \"DONE\"}, \"eval_pi05_random_k03_goal_seed42_postfix\": {\"conclusion\": \"success\", \"metrics\": {\"T0_open_middle_drawer\": 88, \"T1_put_bowl_on_stove\": 6, \"T2_put_wine_bottle_on_cabinet\": 72, \"T3_open_top_drawer_put_bowl\": 40, \"T4_put_bowl_on_cabinet\": 70, \"T5_push_plate_front_stove\": 30, \"T6_put_cream_cheese_in_bowl\": 32, \"T7_turn_on_stove\": 100, \"T8_put_bowl_on_plate\": 68, \"T9_put_wine_bottle_on_rack\": 22, \"overall_sr\": 52.8, \"total_episodes\": 500, \"total_success\": 264}, \"status\": \"DONE\"}, \"eval_openvla_attn_k05_object_seed42_v2\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"eval_pi05_random_k03_spatial_seed42_postfix\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"eval_pi05_l2norm_k09_goal_seed42_postfix\": {\"conclusion\": \"success\", \"metrics\": {\"T0_open_middle_drawer\": 43, \"T1_put_bowl_on_stove\": 49, \"T2_put_wine_bottle_on_cabinet\": 47, \"T3_open_top_drawer_put_bowl\": 44, \"T4_put_bowl_on_cabinet\": 50, \"T5_push_plate_front_stove\": 49, \"T6_put_cream_cheese_in_bowl\": 45, \"T7_turn_on_stove\": 50, \"T8_put_bowl_on_plate\": 47, \"T9_put_wine_bottle_on_rack\": 19, \"overall_sr\": 88.6, \"total_episodes\": 500, \"total_success\": 443}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k07_goal_seed42_postfix\": {\"conclusion\": \"success\", \"metrics\": {\"T0_open_middle_drawer\": 37, \"T1_put_bowl_on_stove\": 41, \"T2_put_wine_bottle_on_cabinet\": 35, \"T3_open_top_drawer_put_bowl\": 24, \"T4_put_bowl_on_cabinet\": 46, \"T5_push_plate_front_stove\": 35, \"T6_put_cream_cheese_in_bowl\": 31, \"T7_turn_on_stove\": 50, \"T8_put_bowl_on_plate\": 30, \"T9_put_wine_bottle_on_rack\": 22, \"overall_sr\": 70.2, \"total_episodes\": 500, \"total_success\": 351}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k05_goal_seed42_postfix\": {\"conclusion\": \"success\", \"metrics\": {\"T0_open_middle_drawer\": 32, \"T1_put_bowl_on_stove\": 1, \"T2_put_wine_bottle_on_cabinet\": 46, \"T3_open_top_drawer_put_bowl\": 33, \"T4_put_bowl_on_cabinet\": 37, \"T5_push_plate_front_stove\": 31, \"T6_put_cream_cheese_in_bowl\": 17, \"T7_turn_on_stove\": 50, \"T8_put_bowl_on_plate\": 28, \"T9_put_wine_bottle_on_rack\": 24, \"overall_sr\": 59.8, \"total_episodes\": 500, \"total_success\": 299}, \"status\": \"DONE\"}, \"eval_pi05_random_k095_goal_seed42_postfix\": {\"conclusion\": \"success\", \"metrics\": {\"T0_open_middle_drawer\": 86, \"T1_put_bowl_on_stove\": 94, \"T2_put_wine_bottle_on_cabinet\": 84, \"T3_open_top_drawer_put_bowl\": 78, \"T4_put_bowl_on_cabinet\": 98, \"T5_push_plate_front_stove\": 92, \"T6_put_cream_cheese_in_bowl\": 88, \"T7_turn_on_stove\": 100, \"T8_put_bowl_on_plate\": 96, \"T9_put_wine_bottle_on_rack\": 10, \"overall_sr\": 82.6, \"total_episodes\": 500, \"total_success\": 413}, \"status\": \"DONE\"}, \"eval_pi05_random_k05_goal_seed42_postfix\": {\"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 73.6, \"per_task_sr\": {\"T0_open_middle_drawer_cabinet\": 78, \"T1_put_bowl_on_stove\": 44, \"T2_put_wine_bottle_on_cabinet\": 86, \"T3_open_top_drawer_put_bowl_in\": 76, \"T4_put_bowl_on_cabinet\": 92, \"T5_push_plate_front_stove\": 70, \"T6_put_cream_cheese_in_bowl\": 62, \"T7_turn_on_stove\": 100, \"T8_put_bowl_on_plate\": 86, \"T9_put_wine_bottle_on_rack\": 42}, \"runtime_min\": 100.8, \"total_episodes\": 500, \"total_success\": 368}, \"status\": \"DONE\"}, \"eval_xvla_l2norm_k03_goal_seed42_v5\": {\"conclusion\": \"success\", \"metrics\": {\"domain_id\": 3, \"elapsed_min\": 84, \"overall_sr\": 0.37, \"per_task_sr\": {\"task0_open_drawer\": 0.42, \"task1_bowl_on_stove\": 0.92, \"task2_wine_on_cabinet\": 0.2, \"task3_drawer_bowl\": 0.24, \"task4_bowl_on_cabinet\": 0.98, \"task5_push_plate\": 0, \"task6_cream_cheese\": 0.02, \"task7_turn_stove\": 0.16, \"task8_bowl_on_plate\": 0.76, \"task9_wine_on_rack\": 0}, \"seed\": 42, \"total_episodes\": 500, \"total_success\": 185, \"vision_tokens_kept\": 15, \"vision_tokens_original\": 50, \"wilson_ci_95\": [0.3288, 0.4132]}, \"status\": \"DONE\"}, \"eval_pi05_random_k03_long_seed43_v2\": {\"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 28, \"total_episodes\": 500, \"total_success\": 140}, \"status\": \"DONE\"}, \"eval_pi05_random_k085_goal_seed42_postfix\": {\"conclusion\": \"success\", \"metrics\": {\"T0_open_drawer\": 68, \"T1_bowl_stove\": 4, \"T2_wine_cabinet\": 20, \"T3_drawer_bowl\": 30, \"T4_bowl_cabinet\": 66, \"T5_push_plate\": 80, \"T6_cream_bowl\": 86, \"T7_turn_stove\": 90, \"T8_bowl_plate\": 78, \"T9_wine_rack\": 6, \"overall_sr\": 52.8, \"total_episodes\": 500, \"total_successes\": 264}, \"status\": \"DONE\"}, \"eval_pi05_random_k09_goal_seed42_postfix\": {\"conclusion\": \"success\", \"metrics\": {\"T0_open_drawer\": 76, \"T1_bowl_stove\": 32, \"T2_wine_cabinet\": 38, \"T3_drawer_bowl\": 38, \"T4_bowl_cabinet\": 90, \"T5_push_plate\": 88, \"T6_cream_bowl\": 80, \"T7_turn_stove\": 88, \"T8_bowl_plate\": 74, \"T9_wine_rack\": 14, \"overall_sr\": 61.8, \"total_episodes\": 500, \"total_successes\": 309}, \"status\": \"DONE\"}, \"eval_pi05_random_k07_goal_seed42_postfix\": {\"conclusion\": \"success\", \"metrics\": {\"T0_open_drawer\": 90, \"T1_bowl_stove\": 48, \"T2_wine_cabinet\": 82, \"T3_drawer_bowl\": 74, \"T4_bowl_cabinet\": 96, \"T5_push_plate\": 72, \"T6_cream_bowl\": 62, \"T7_turn_stove\": 100, \"T8_bowl_plate\": 82, \"T9_wine_rack\": 50, \"overall_sr\": 75.6, \"total_episodes\": 500, \"total_successes\": 378}, \"status\": \"DONE\"}, \"eval_pi05_random_k095_spatial_seed42_postfix_v2\": {\"conclusion\": \"success\", \"metrics\": {\"T0_plate_ramekin\": 100, \"T1_next_ramekin\": 86, \"T2_table_center\": 88, \"T3_cookie_box\": 64, \"T4_top_drawer\": 50, \"T5_on_ramekin\": 80, \"T6_next_cookie\": 92, \"T7_on_stove\": 76, \"T8_next_plate\": 94, \"T9_wooden_cabinet\": 38, \"overall_sr\": 76.8, \"total_episodes\": 500, \"total_successes\": 384}, \"status\": \"DONE\"}, \"eval_pi05_random_k0925_goal_seed42_v3\": {\"conclusion\": \"success\", \"metrics\": {\"T0_open_drawer\": 68, \"T1_bowl_stove\": 52, \"T2_wine_cabinet\": 58, \"T3_drawer_bowl\": 64, \"T4_bowl_cabinet\": 94, \"T5_push_plate\": 88, \"T6_cream_bowl\": 88, \"T7_turn_stove\": 96, \"T8_bowl_plate\": 86, \"T9_wine_rack\": 6, \"overall_sr\": 70, \"total_episodes\": 500, \"total_successes\": 350}, \"status\": \"DONE\"}, \"eval_pi05_random_k0925_object_seed42_postfix\": {\"conclusion\": \"success\", \"metrics\": {\"T0_alphabet_soup\": 30, \"T1_cream_cheese\": 36, \"T2_salad_dressing\": 22, \"T3_bbq_sauce\": 28, \"T4_ketchup\": 8, \"T5_tomato_sauce\": 44, \"T6_butter\": 48, \"T7_milk\": 20, \"T8_chocolate_pudding\": 16, \"T9_orange_juice\": 20, \"overall_sr\": 27.2, \"total_episodes\": 500, \"total_successes\": 136}, \"status\": \"DONE\"}, \"eval_pi05_random_k07_spatial_seed42_postfix\": {\"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 73.8, \"total_episodes\": 500}, \"status\": \"DONE\"}, \"eval_xvla_l2norm_k03_long_seed42\": {\"conclusion\": \"killed\", \"status\": \"DONE\"}, \"eval_xvla_random_k03_long_seed42\": {\"conclusion\": \"killed\", \"status\": \"DONE\"}, \"eval_xvla_l2norm_k05_long_seed42_v4\": {\"conclusion\": \"success\", \"metrics\": {\"elapsed_min\": 94.6, \"overall_sr\": 44.6, \"per_task_sr\": {\"T0_alphabet_soup_tomato_basket\": 26, \"T1_cream_cheese_butter_basket\": 0, \"T2_stove_moka_pot\": 48, \"T3_black_bowl_drawer\": 84, \"T4_mugs_on_plates\": 36, \"T5_book_caddy\": 88, \"T6_mug_plate_pudding\": 48, \"T7_alphabet_soup_cream_cheese_basket\": 78, \"T8_moka_pots_stove\": 34, \"T9_mug_microwave\": 4}, \"total_episodes\": 500, \"total_success\": 223}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k085_spatial_seed42_v3\": {\"conclusion\": \"success\", \"metrics\": {\"elapsed_min\": 63.1, \"overall_sr\": 88.4, \"per_task_sr\": {\"T0_between_plate_ramekin\": 98, \"T1_next_to_ramekin\": 92, \"T2_table_center\": 94, \"T3_on_cookie_box\": 84, \"T4_top_drawer\": 76, \"T5_on_ramekin\": 82, \"T6_next_to_cookie_box\": 98, \"T7_on_stove\": 86, \"T8_next_to_plate\": 98, \"T9_wooden_cabinet\": 76}, \"total_episodes\": 500, \"total_success\": 442}, \"status\": \"DONE\"}, \"eval_pi05_random_k085_spatial_seed42_v3\": {\"conclusion\": \"success\", \"metrics\": {\"elapsed_min\": 86.9, \"overall_sr\": 60.2, \"per_task_sr\": {\"T0_between_plate_ramekin\": 78, \"T1_next_to_ramekin\": 62, \"T2_table_center\": 92, \"T3_on_cookie_box\": 14, \"T4_top_drawer\": 60, \"T5_on_ramekin\": 36, \"T6_next_to_cookie_box\": 44, \"T7_on_stove\": 82, \"T8_next_to_plate\": 86, \"T9_wooden_cabinet\": 48}, \"total_episodes\": 500, \"total_success\": 301}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k0925_goal_seed42_v3\": {\"conclusion\": \"success\", \"metrics\": {\"elapsed_min\": 56.3, \"overall_sr\": 89.8, \"per_task_sr\": {\"bowl_on_cabinet\": 98, \"bowl_on_plate\": 96, \"bowl_on_stove\": 96, \"cream_cheese_in_bowl\": 88, \"open_drawer_put_bowl\": 90, \"open_middle_drawer\": 86, \"push_plate_front_stove\": 98, \"turn_on_stove\": 100, \"wine_bottle_on_cabinet\": 100, \"wine_bottle_on_rack\": 46}, \"total_episodes\": 500, \"total_success\": 449}, \"status\": \"DONE\"}, \"eval_xvla_l2norm_k03_goal_seed42\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"eval_xvla_l2norm_k07_spatial_seed42_v2\": {\"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 72.8, \"per_task_sr\": {\"task_0\": 98, \"task_1\": 42, \"task_2\": 96, \"task_3\": 94, \"task_4\": 82, \"task_5\": 0, \"task_6\": 98, \"task_7\": 34, \"task_8\": 94, \"task_9\": 90}, \"total_episodes\": 500, \"total_success\": 364}, \"status\": \"DONE\"}, \"eval_pi05_random_k05_spatial_seed42_postfix_v3\": {\"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.718, \"per_task_sr\": {\"T0\": 0.88, \"T1\": 0.88, \"T2\": 0.88, \"T3\": 0.48, \"T4\": 0.4, \"T5\": 0.32, \"T6\": 0.92, \"T7\": 0.86, \"T8\": 0.84, \"T9\": 0.72}, \"total_episodes\": 500, \"total_success\": 359, \"wall_time_min\": 139.2}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k05_spatial_seed43_v2\": {\"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.554, \"per_task_sr\": {\"T0_between_plate\": 0.76, \"T1_next_to_ramekin\": 0.84, \"T2_table_center\": 0.84, \"T3_on_cookie_box\": 0.14, \"T4_top_drawer\": 0.42, \"T5_on_ramekin\": 0.48, \"T6_next_to_cookie\": 0.28, \"T7_on_stove\": 0.74, \"T8_next_to_plate\": 0.68, \"T9_wooden_cabinet\": 0.36}, \"total_episodes\": 500, \"total_success\": 277, \"wall_time_min\": 90.3}, \"status\": \"DONE\"}, \"eval_xvla_random_k085_long_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"cross_suite_k085\": {\"goal\": 60.4, \"long\": 35, \"object\": 65, \"spatial\": 68.2}, \"elapsed_min\": 106.7, \"keep_ratio\": 0.85, \"model\": \"X-VLA\", \"overall_sr\": 35, \"per_task_sr\": {\"T0_alphabet_soup_tomato_sauce_basket\": 54, \"T1_cream_cheese_butter_basket\": 10, \"T2_stove_moka_pot\": 16, \"T3_black_bowl_drawer\": 88, \"T4_white_mug_left_yellow_mug_right\": 2, \"T5_book_caddy\": 98, \"T6_white_mug_chocolate_pudding\": 0, \"T7_alphabet_soup_cream_cheese_basket\": 48, \"T8_both_moka_pots_stove\": 16, \"T9_mug_microwave\": 18}, \"prune_mode\": \"random\", \"seed\": 42, \"suite\": \"libero_10\", \"total_episodes\": 500, \"total_success\": 175, \"vs_k05_long\": {\"delta_pp\": -26.6, \"k05_sr\": 61.6, \"k085_sr\": 35, \"non_monotonic\": true}, \"wilson_ci_95\": [30.9, 39.3]}, \"status\": \"DONE\"}, \"eval_pi05_random_k09_spatial_seed42_postfix_v2\": {\"conclusion\": \"negative\", \"metrics\": {\"baseline_spatial_k1\": 78, \"delta_vs_baseline\": -24.6, \"overall_sr\": 53.4, \"per_task_sr\": {\"T0_between_plate\": 90, \"T1_next_to_ramekin\": 52, \"T2_table_center\": 80, \"T3_on_cookie_box\": 24, \"T4_top_drawer\": 18, \"T5_on_ramekin\": 40, \"T6_next_to_cookie\": 58, \"T7_on_stove\": 54, \"T8_next_to_plate\": 90, \"T9_wooden_cabinet\": 28}, \"total_episodes\": 500, \"total_success\": 267, \"wall_time_min\": 171.9}, \"status\": \"DONE\"}, \"eval_pi05_random_k085_spatial_seed42_postfix_v2\": {\"conclusion\": \"success\", \"metrics\": {\"baseline_spatial_k1\": 78, \"delta_vs_baseline\": -17.2, \"overall_sr\": 60.8, \"per_task_sr\": {\"T0\": 84, \"T1\": 68, \"T2\": 92, \"T3\": 16, \"T4\": 66, \"T5\": 28, \"T6\": 44, \"T7\": 76, \"T8\": 82, \"T9\": 52}, \"total_episodes\": 500, \"total_success\": 304}, \"status\": \"DONE\"}, \"eval_pi05_random_k03_goal_seed43_v2\": {\"conclusion\": \"success\", \"metrics\": {\"T0_open_drawer\": 80, \"T1_bowl_stove\": 12, \"T2_wine_cabinet\": 76, \"T3_drawer_bowl\": 52, \"T4_bowl_cabinet\": 60, \"T5_push_plate\": 32, \"T6_cream_bowl\": 26, \"T7_turn_stove\": 100, \"T8_bowl_plate\": 70, \"T9_wine_rack\": 28, \"cv_mean\": 52.1, \"cv_seed42\": 50.6, \"cv_seed43\": 53.6, \"cv_std\": 2.1, \"elapsed_min\": 127.4, \"overall_sr\": 53.6, \"total_episodes\": 500}, \"status\": \"DONE\"}, \"eval_xvla_l2norm_k03_goal_seed42_v2\": {\"conclusion\": \"killed\", \"status\": \"DONE\"}, \"eval_xvla_l2norm_k03_goal_seed42_v3\": {\"conclusion\": \"negative\", \"metrics\": {\"success_rate\": 0.376, \"task_sr\": {\"task0_open_drawer\": 0.42, \"task1_bowl_on_stove\": 0.94, \"task2_wine_on_cabinet\": 0.16, \"task3_drawer_bowl_inside\": 0.24, \"task4_bowl_on_cabinet\": 0.98, \"task5_push_plate\": 0, \"task6_cream_in_bowl\": 0.02, \"task7_turn_on_stove\": 0.2, \"task8_bowl_on_plate\": 0.8, \"task9_wine_on_rack\": 0}, \"total_episodes\": 500, \"total_successes\": 188}, \"status\": \"DONE\"}, \"eval_xvla_l2norm_k05_long_seed42_v3\": {\"conclusion\": \"killed\", \"status\": \"DONE\"}, \"eval_xvla_l2norm_k05_spatial_seed42_v2\": {\"conclusion\": \"killed\", \"status\": \"DONE\"}, \"eval_xvla_l2norm_k07_spatial_seed42\": {\"conclusion\": \"negative\", \"metrics\": {\"num_episodes\": 500, \"num_success\": 360, \"seed\": 42, \"success_rate\": 0.72, \"suite\": \"libero_spatial\"}, \"status\": \"DONE\"}, \"eval_xvla_l2norm_k05_goal_seed42_v2\": {\"conclusion\": \"success\", \"metrics\": {\"keep_ratio\": 0.5, \"model\": \"X-VLA\", \"per_task_sr\": {\"T0_open_middle_drawer\": 80, \"T1_put_bowl_on_stove\": 92, \"T2_put_wine_bottle_on_cabinet\": 98, \"T3_open_top_drawer_put_bowl\": 34, \"T4_put_bowl_on_cabinet\": 100, \"T5_push_plate_to_stove\": 0, \"T6_put_cream_cheese_in_bowl\": 24, \"T7_turn_on_stove\": 72, \"T8_put_bowl_on_plate\": 90, \"T9_put_wine_bottle_on_rack\": 0}, \"prune_mode\": \"l2_norm\", \"seed\": 42, \"success_rate\": 0.59, \"suite\": \"libero_goal\", \"total_episodes\": 500, \"total_successes\": 295}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k05_spatial_seed43\": {\"conclusion\": \"success\", \"metrics\": {\"overall_SR\": 0.582, \"total_episodes\": 500, \"total_successes\": 291}, \"status\": \"DONE\"}, \"eval_pi05_random_k085_goal_seed43\": {\"conclusion\": \"negative\", \"metrics\": {\"keep_ratio\": 0.85, \"model\": \"pi0.5\", \"note\": \"completed via direct tmux May24 10:24\", \"per_task_sr\": {\"T0_open_middle_drawer\": 80, \"T1_put_bowl_on_stove\": 4, \"T2_put_wine_bottle_on_cabinet\": 20, \"T3_open_top_drawer_put_bowl\": 46, \"T4_put_bowl_on_cabinet\": 58, \"T5_push_plate_to_stove\": 82, \"T6_put_cream_cheese_in_bowl\": 74, \"T7_turn_on_stove\": 90, \"T8_put_bowl_on_plate\": 58, \"T9_put_wine_bottle_on_rack\": 10}, \"prune_mode\": \"random\", \"seed\": 43, \"success_rate\": 0.522, \"suite\": \"libero_goal\", \"total_episodes\": 500, \"total_successes\": 261}, \"status\": \"DONE\"}, \"eval_pi05_random_k095_goal_seed43\": {\"conclusion\": \"success\", \"metrics\": {\"keep_ratio\": 0.95, \"model\": \"pi0.5\", \"note\": \"re-run with HF_HUB_OFFLINE=1, result file May24 10:54\", \"per_task_sr\": {\"T0_open_middle_drawer\": 86, \"T1_put_bowl_on_stove\": 94, \"T2_put_wine_bottle_on_cabinet\": 74, \"T3_open_top_drawer_put_bowl\": 80, \"T4_put_bowl_on_cabinet\": 100, \"T5_push_plate_to_stove\": 96, \"T6_put_cream_cheese_in_bowl\": 90, \"T7_turn_on_stove\": 100, \"T8_put_bowl_on_plate\": 96, \"T9_put_wine_bottle_on_rack\": 18}, \"prune_mode\": \"random\", \"seed\": 43, \"success_rate\": 0.834, \"suite\": \"libero_goal\", \"total_episodes\": 500, \"total_successes\": 417}, \"status\": \"DONE\"}, \"eval_xvla_l2norm_k05_goal_seed43\": {\"conclusion\": \"negative\", \"metrics\": {\"overall_SR\": 0.602, \"per_task_SR\": [0.84, 1, 0.98, 0.3, 1, 0, 0.22, 0.74, 0.9, 0.04], \"seed\": 43, \"total_episodes\": 500, \"total_successes\": 301, \"wilson_ci_95\": [0.5585, 0.644]}, \"status\": \"DONE\"}, \"eval_pi05_random_k05_goal_seed42_v2\": {\"conclusion\": \"success\", \"metrics\": {\"duration_min\": 109.7, \"overall_SR\": 73.6, \"per_task_SR\": {\"T0_open_drawer\": 78, \"T1_bowl_stove\": 44, \"T2_wine_cabinet\": 86, \"T3_bowl_drawer\": 76, \"T4_bowl_cabinet\": 92, \"T5_plate_stove\": 70, \"T6_cream_bowl\": 62, \"T7_turn_stove\": 100, \"T8_bowl_plate\": 86, \"T9_wine_rack\": 42}, \"total_episodes\": 500, \"total_successes\": 368}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k07_goal_seed43_v2\": {\"conclusion\": \"success\", \"metrics\": {\"duration_min\": 71.3, \"overall_SR\": 72.2, \"per_task_SR\": {\"T0_open_middle_drawer\": 78, \"T1_put_bowl_on_stove\": 76, \"T2_wine_bottle_on_cabinet\": 68, \"T3_open_drawer_put_bowl\": 48, \"T4_bowl_on_cabinet\": 90, \"T5_push_plate_front_stove\": 80, \"T6_cream_cheese_in_bowl\": 66, \"T7_turn_on_stove\": 98, \"T8_bowl_on_plate\": 68, \"T9_wine_bottle_on_rack\": 50}, \"total_episodes\": 500, \"total_successes\": 361}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k085_goal_seed43\": {\"conclusion\": \"success\", \"metrics\": {\"elapsed_min\": 86.5, \"overall_SR\": 87, \"per_task\": {\"open the middle drawer of the cabinet\": 88, \"open the top drawer and put the bowl inside\": 80, \"push the plate to the front of the stove\": 94, \"put the bowl on the plate\": 94, \"put the bowl on the stove\": 94, \"put the bowl on top of the cabinet\": 96, \"put the cream cheese in the bowl\": 86, \"put the wine bottle on the rack\": 46, \"put the wine bottle on top of the cabinet\": 96, \"turn on the stove\": 96}, \"total_episodes\": 500, \"total_successes\": 435}, \"status\": \"DONE\"}, \"eval_pi05_random_k085_spatial_seed42_postfix\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"eval_xvla_random_k085_object_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"elapsed_seconds\": 3572.9, \"overall_SR\": 0.65, \"per_task_sr\": [0.98, 0.14, 1, 0.88, 0.36, 0.96, 0, 0.94, 0.24, 1], \"total_episodes\": 500, \"total_successes\": 325, \"wilson_ci_95\": [0.6072, 0.6905]}, \"status\": \"DONE\"}, \"eval_xvla_random_k085_spatial_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"overall_SR\": 0.682, \"per_task\": {\"0\": 1, \"1\": 0.06, \"2\": 0.98, \"3\": 0.98, \"4\": 0.82, \"5\": 0.06, \"6\": 1, \"7\": 0.04, \"8\": 0.92, \"9\": 0.96}, \"total_episodes\": 500, \"wilson_ci_95\": [0.6399, 0.7213]}, \"status\": \"DONE\"}, \"eval_xvla_random_k085_goal_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"overall_SR\": 0.604, \"per_task\": {\"0\": 1, \"1\": 0.42, \"2\": 0.7, \"3\": 0.78, \"4\": 0.98, \"5\": 0, \"6\": 0.02, \"7\": 0.88, \"8\": 0.98, \"9\": 0.28}, \"total_episodes\": 500, \"wilson_ci_95\": [0.5605, 0.6459]}, \"status\": \"DONE\"}, \"eval_pi05_random_k095_object_seed42_v2\": {\"conclusion\": \"success\", \"metrics\": {\"duration_min\": 119.6, \"num_episodes\": 500, \"per_task\": [0.82, 0.86, 0.66, 0.68, 0.64, 0.74, 0.76, 0.56, 0.86, 0.82], \"success_rate\": 74}, \"status\": \"DONE\"}, \"eval_pi05_random_k07_object_seed42_v4\": {\"conclusion\": \"success\", \"metrics\": {\"duration_min\": 120.7, \"num_episodes\": 500, \"per_task\": [0.86, 0.86, 0.7, 0.76, 0.72, 0.3, 0.88, 0.76, 0.88, 0.68], \"success_rate\": 74}, \"status\": \"DONE\"}, \"eval_openvla_l2norm_k05_goal_seed42_v2\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"eval_pi05_random_k09_object_seed42_v2\": {\"conclusion\": \"success\", \"metrics\": {\"overall_SR\": 0.09, \"per_task_sr\": {\"T0\": 14, \"T1\": 20, \"T2\": 4, \"T3\": 6, \"T4\": 2, \"T5\": 20, \"T6\": 6, \"T7\": 2, \"T8\": 6, \"T9\": 10}, \"postfix_confirmed\": true, \"postfix_sr\": 9, \"prefix_v2_sr\": 9, \"result_json\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_random_k0.90_libero_object_seed42.json\", \"seed\": 42, \"total_episodes\": 500}, \"status\": \"DONE\"}, \"eval_pi05_random_k05_object_seed42_v2\": {\"conclusion\": \"success\", \"metrics\": {\"overall_SR\": 0.682, \"seed\": 42, \"total_episodes\": 500}, \"status\": \"DONE\"}, \"eval_pi05_random_k07_object_seed42_v3\": {\"conclusion\": \"success\", \"metrics\": {\"overall_SR\": 0.74, \"seed\": 42, \"total_episodes\": 500}, \"status\": \"DONE\"}, \"eval_xvla_l2norm_k05_long_seed43\": {\"conclusion\": \"success\", \"metrics\": {\"elapsed_min\": 94, \"overall_SR\": 43.8, \"per_task_sr\": {\"T0\": 26, \"T1\": 0, \"T2\": 52, \"T3\": 78, \"T4\": 38, \"T5\": 86, \"T6\": 56, \"T7\": 76, \"T8\": 24, \"T9\": 2}, \"result_json\": \"eval_results/xvla_prune_k0.5_libero_10.json\", \"total_episodes\": 500, \"total_successes\": 219, \"wilson_ci_95\": [39.5, 48.2]}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k05_long_seed43\": {\"conclusion\": \"success\", \"metrics\": {\"sr\": 0.54, \"total_episodes\": 500, \"total_successes\": 270}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k07_goal_seed43\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"eval_pi05_random_k05_spatial_seed42_postfix_v2\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"eval_pi05_random_k09_spatial_seed42_postfix\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"eval_xvla_l2norm_k05_long_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"elapsed_min\": 94.6, \"episodes\": 500, \"overall_sr\": 45, \"per_task_sr\": {\"task_0_alphabet_soup_tomato_sauce\": 26, \"task_1_cream_cheese_butter\": 0, \"task_2_stove_moka_pot\": 46, \"task_3_black_bowl_drawer\": 82, \"task_4_white_mug_yellow_mug\": 42, \"task_5_book_caddy\": 92, \"task_6_white_mug_chocolate_pudding\": 54, \"task_7_alphabet_soup_cream_cheese\": 70, \"task_8_both_moka_pots\": 34, \"task_9_mug_microwave\": 4}, \"wilson_ci_95\": [40.7, 49.4]}, \"status\": \"DONE\"}, \"eval_xvla_random_k05_object_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"duration_min\": 76.0, \"num_episodes\": 500, \"per_task\": [0.96, 0.46, 0.98, 0.8, 1.0, 0.76, 0.02, 0.82, 0.26, 1.0], \"success_rate\": 70.6, \"wilson_ci_95\": [0.665, 0.744]}, \"status\": \"DONE\"}, \"eval_pi05_random_k09_object_seed43\": {\"conclusion\": \"success\", \"metrics\": {\"elapsed_min\": 119.5, \"overall_sr\": 0.096, \"per_task_sr\": {\"T0_alphabet_soup\": 0.16, \"T1_cream_cheese\": 0.16, \"T2_salad_dressing\": 0.1, \"T3_bbq_sauce\": 0.02, \"T4_ketchup\": 0.06, \"T5_tomato_sauce\": 0.14, \"T6_butter\": 0.14, \"T7_milk\": 0.02, \"T8_chocolate_pudding\": 0.08, \"T9_orange_juice\": 0.08}, \"total_episodes\": 500, \"total_successes\": 48}, \"status\": \"DONE\"}, \"eval_xvla_random_k05_spatial_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"duration_min\": 92.1, \"num_episodes\": 500, \"per_task\": [0.98, 0.26, 0.98, 0.9, 0.86, 0, 0.92, 0.66, 0.92, 0.66], \"success_rate\": 71.4, \"suite\": \"libero_spatial\", \"wilson_ci_95\": [0.673, 0.752]}, \"status\": \"DONE\"}, \"eval_xvla_random_k05_long_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"keep_ratio\": 0.5, \"per_task_sr\": [68, 0, 64, 94, 70, 90, 84, 86, 46, 14], \"prune_method\": \"random\", \"seed\": 42, \"success_rate\": 61.6, \"suite\": \"libero_10\", \"tokens_kept\": \"25/50\", \"total_episodes\": 500, \"total_successes\": 308, \"wall_time_min\": 82.6, \"wilson_ci_95\": [57.3, 65.8]}, \"status\": \"DONE\"}, \"eval_xvla_l2norm_k05_object_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.434, \"total_episodes\": 500, \"total_successes\": 217}, \"status\": \"DONE\"}, \"eval_xvla_l2norm_k05_spatial_seed43\": {\"conclusion\": \"negative\", \"metrics\": {\"elapsed_min\": 79.1, \"per_task_SR\": {\"T0_bowl_between_plate_ramekin\": 98, \"T1_bowl_next_ramekin\": 20, \"T2_bowl_from_table_center\": 92, \"T3_bowl_on_cookie_box\": 72, \"T4_bowl_in_top_drawer\": 76, \"T5_bowl_on_ramekin\": 0, \"T6_bowl_next_cookie_box\": 76, \"T7_bowl_on_stove\": 38, \"T8_bowl_next_plate\": 66, \"T9_bowl_on_wooden_cabinet\": 52}, \"seed\": 43, \"success_rate\": 59, \"total_episodes\": 500, \"total_successes\": 295, \"vs_l2norm_spatial_seed42\": {\"diff_pp\": 0.2, \"mean\": 58.9, \"seed42_sr\": 58.8, \"seed43_sr\": 59}, \"vs_random_k05_spatial_seed43\": {\"delta_pp\": -13.6, \"l2norm_sr\": 59, \"random_sr\": 72.6, \"verdict\": \"L2norm worse than random on Spatial\"}, \"wilson_ci_95\": [54.6, 63.2]}, \"status\": \"DONE\"}, \"eval_xvla_random_k05_goal_seed43_v4\": {\"conclusion\": \"success\", \"metrics\": {\"cv_with_seed42\": {\"diff_pp\": 1.4, \"mean\": 67.9, \"seed42\": 67.2, \"seed43\": 68.6}, \"elapsed_min\": 56.1, \"per_task_sr\": {\"T0_open_middle_drawer\": 100, \"T1_bowl_on_stove\": 94, \"T2_wine_on_cabinet\": 96, \"T3_open_drawer_bowl_inside\": 68, \"T4_bowl_on_cabinet\": 98, \"T5_push_plate\": 0, \"T6_cream_cheese_in_bowl\": 38, \"T7_turn_on_stove\": 96, \"T8_bowl_on_plate\": 96, \"T9_wine_on_rack\": 0}, \"success_rate\": 68.6, \"total_episodes\": 500, \"total_successes\": 343, \"wilson_ci_95\": [64.4, 72.5]}, \"status\": \"DONE\"}, \"eval_pi05_random_k05_spatial_seed42_postfix\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"eval_openvla_baseline_long_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.528, \"task_sr\": {\"task01_alphabet_soup_tomato_sauce_basket\": 0.62, \"task02_cream_cheese_butter_basket\": 0.7, \"task03_stove_moka_pot\": 0.5, \"task04_black_bowl_drawer\": 0.48, \"task05_white_mug_left_yellow_mug_right\": 0.4, \"task06_book_caddy\": 0.7, \"task07_white_mug_plate_chocolate_pudding\": 0.5, \"task08_alphabet_soup_cream_cheese_basket\": 0.6, \"task09_both_moka_pots_stove\": 0.24, \"task10_yellow_white_mug_microwave\": 0.54}, \"time_min\": 483.3, \"total_episodes\": 500, \"total_success\": 264}, \"status\": \"DONE\"}, \"eval_pi05_random_k03_goal_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"overall_SR\": 0.51, \"per_task\": {\"T0_open_drawer\": 0.82, \"T1_bowl_stove\": 0.22, \"T2_wine_cabinet\": 0.76, \"T3_drawer_bowl\": 0.34, \"T4_bowl_cabinet\": 0.64, \"T5_plate_stove\": 0.26, \"T6_cream_cheese_bowl\": 0.26, \"T7_turn_stove\": 1, \"T8_bowl_plate\": 0.54, \"T9_wine_rack\": 0.26}, \"total_episodes\": 500, \"total_successes\": 255}, \"status\": \"DONE\"}, \"eval_pi05_attention_k05_object_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"overall_SR\": 0.378, \"per_task\": {\"T0_alphabet_soup\": 0.94, \"T1_cream_cheese\": 0.26, \"T2_salad_dressing\": 0.32, \"T3_bbq_sauce\": 0.18, \"T4_ketchup\": 0.4, \"T5_tomato_sauce\": 0.12, \"T6_butter\": 0.38, \"T7_milk\": 0.6, \"T8_chocolate_pudding\": 0.36, \"T9_orange_juice\": 0.22}, \"total_episodes\": 500, \"total_successes\": 189}, \"status\": \"DONE\"}, \"eval_openvla_l2norm_k05_goal_seed42_v3\": {\"conclusion\": \"negative\", \"metrics\": {\"eval_time_min\": 247.8, \"overall_sr\": 0.434, \"task_sr\": {\"open_the_middle_drawer_of_the_cabinet\": 0.28, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.06, \"push_the_plate_to_the_front_of_the_stove\": 0.2, \"put_the_bowl_on_the_plate\": 0.3, \"put_the_bowl_on_the_stove\": 0.38, \"put_the_bowl_on_top_of_the_cabinet\": 0.66, \"put_the_cream_cheese_in_the_bowl\": 0.22, \"put_the_wine_bottle_on_the_rack\": 0.44, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.82, \"turn_on_the_stove\": 0.98}, \"total_episodes\": 500, \"total_successes\": 217}, \"status\": \"DONE\"}, \"eval_xvla_random_k05_long_seed43\": {\"conclusion\": \"success\", \"metrics\": {\"elapsed_min\": 83.6, \"overall_SR\": 0.582, \"per_task_SR\": [0.62, 0, 0.68, 0.94, 0.6, 0.86, 0.82, 0.84, 0.4, 0.06], \"seed\": 43, \"total_episodes\": 500, \"total_successes\": 291, \"wilson_ci_95\": [0.5383, 0.6244]}, \"status\": \"DONE\"}, \"eval_pi05_random_k095_spatial_seed42_postfix\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"eval_xvla_l2norm_k05_object_seed43\": {\"conclusion\": \"negative\", \"metrics\": {\"elapsed_min\": 76.3, \"overall_SR\": 0.43, \"per_task_SR\": {\"T0_alphabet_soup\": 0.52, \"T1_cream_cheese\": 0.06, \"T2_salad_dressing\": 0.76, \"T3_bbq_sauce\": 0.7, \"T4_ketchup\": 0.52, \"T5_tomato_sauce\": 0.56, \"T6_butter\": 0.02, \"T7_milk\": 0.38, \"T8_chocolate_pudding\": 0.16, \"T9_orange_juice\": 0.62}, \"seed\": 43, \"total_episodes\": 500, \"total_successes\": 215, \"vs_random_k05_object_seed43\": {\"delta_pp\": -28, \"l2norm_sr\": 0.43, \"random_sr\": 0.71, \"verdict\": \"L2norm catastrophically worse than random on Object suite\"}, \"wilson_ci_95\": [0.387, 0.474]}, \"status\": \"DONE\"}, \"eval_pi05_attention_k05_spatial_seed42\": {\"conclusion\": \"negative\", \"metrics\": {\"elapsed_min\": 74.3, \"overall_sr\": 0.726, \"per_task\": {\"T0_bowl_between_plate_ramekin\": 0.72, \"T1_bowl_next_to_ramekin\": 0.92, \"T2_bowl_from_table_center\": 0.96, \"T3_bowl_on_cookie_box\": 0.68, \"T4_bowl_in_top_drawer\": 0.28, \"T5_bowl_on_ramekin\": 0.32, \"T6_bowl_next_to_cookie_box\": 0.86, \"T7_bowl_on_stove\": 0.88, \"T8_bowl_next_to_plate\": 0.76, \"T9_bowl_on_wooden_cabinet\": 0.88}, \"total_episodes\": 500, \"total_successes\": 363, \"vs_random_k05_spatial\": {\"attention_sr\": 0.726, \"delta_pp\": 1, \"random_sr\": 0.716, \"verdict\": \"noise-level, attention provides no benefit over random\"}}, \"status\": \"DONE\"}, \"eval_pi05_attention_k05_goal_seed43\": {\"conclusion\": \"negative\", \"metrics\": {\"elapsed_min\": 70.6, \"overall_sr\": 0.722, \"per_task\": {\"bowl_in_drawer\": 0.72, \"bowl_on_cabinet\": 1, \"bowl_on_plate\": 0.9, \"bowl_on_stove\": 0.32, \"cream_cheese_in_bowl\": 0.62, \"open_middle_drawer\": 0.76, \"plate_to_front\": 0.64, \"turn_on_stove\": 1, \"wine_on_cabinet\": 0.84, \"wine_on_rack\": 0.42}, \"total_episodes\": 500, \"total_successes\": 361}, \"status\": \"DONE\"}, \"eval_pi05_random_k07_object_seed42_v2\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"eval_pi05_l2norm_k095_goal_seed42\": {\"conclusion\": \"negative\", \"metrics\": {\"elapsed_min\": 90.4, \"overall_sr\": 0.908, \"per_task\": {\"open the middle drawer of the cabinet\": 0.84, \"open the top drawer and put the bowl inside\": 0.96, \"push the plate to the front of the stove\": 1, \"put the bowl on the plate\": 0.98, \"put the bowl on the stove\": 0.98, \"put the bowl on top of the cabinet\": 1, \"put the cream cheese in the bowl\": 0.92, \"put the wine bottle on the rack\": 0.46, \"put the wine bottle on top of the cabinet\": 0.94, \"turn on the stove\": 1}, \"total_episodes\": 500, \"total_successes\": 454}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k03_goal_seed42\": {\"conclusion\": \"negative\", \"metrics\": {\"elapsed_min\": 118.7, \"keep_ratio\": 0.3, \"note\": \"Two runs: v2=50.6%, latest=54.2%. vs Random k=0.3 Goal=51.8%, delta=+2.4pp (negligible)\", \"overall_SR\": 0.542, \"per_task\": {\"open the middle drawer of the cabinet\": 0.7, \"open the top drawer and put the bowl inside\": 0.4, \"push the plate to the front of the stove\": 0.48, \"put the bowl on the plate\": 0.72, \"put the bowl on the stove\": 0.2, \"put the bowl on top of the cabinet\": 0.6, \"put the cream cheese in the bowl\": 0.26, \"put the wine bottle on the rack\": 0.28, \"put the wine bottle on top of the cabinet\": 0.82, \"turn on the stove\": 0.96}, \"prune_mode\": \"l2norm\", \"seed\": 42, \"suite\": \"libero_goal\", \"total_episodes\": 500, \"total_successes\": 271, \"v2_run_SR\": 0.506}, \"status\": \"DONE\"}, \"eval_xvla_random_k05_goal_seed43_v3\": {\"conclusion\": \"killed\", \"status\": \"DONE\"}, \"eval_xvla_random_k05_goal_seed43_v2\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"eval_pi05_random_k05_spatial_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"per_task\": {\"T0_bowl_between_plate_ramekin\": 88, \"T1_bowl_next_to_ramekin\": 82, \"T2_bowl_from_table_center\": 88, \"T3_bowl_on_cookie_box\": 52, \"T4_bowl_in_top_drawer\": 44, \"T5_bowl_on_ramekin\": 38, \"T6_bowl_next_to_cookie_box\": 84, \"T7_bowl_on_stove\": 84, \"T8_bowl_next_to_plate\": 80, \"T9_bowl_on_wooden_cabinet\": 76}, \"success_rate\": 71.6, \"total_episodes\": 500, \"total_successes\": 358}, \"status\": \"DONE\"}, \"eval_xvla_random_k05_goal_seed43\": {\"conclusion\": \"failed\", \"metrics\": {\"elapsed_min\": 58.2, \"note\": \"log=eval_xvla_random_k05_goal_seed42_v2.log; JSON overwritten by l2_norm run (known bug)\", \"overall_sr\": 0.672, \"per_task\": {\"task_0_open_middle_drawer\": {\"sr\": 0.98, \"succ\": 49, \"total\": 50}, \"task_1_bowl_on_stove\": {\"sr\": 0.98, \"succ\": 49, \"total\": 50}, \"task_2_wine_on_cabinet\": {\"sr\": 0.9, \"succ\": 45, \"total\": 50}, \"task_3_open_drawer_bowl_inside\": {\"sr\": 0.6, \"succ\": 30, \"total\": 50}, \"task_4_bowl_on_cabinet\": {\"sr\": 0.98, \"succ\": 49, \"total\": 50}, \"task_5_push_plate\": {\"sr\": 0, \"succ\": 0, \"total\": 50}, \"task_6_cream_cheese_in_bowl\": {\"sr\": 0.4, \"succ\": 20, \"total\": 50}, \"task_7_turn_on_stove\": {\"sr\": 0.98, \"succ\": 49, \"total\": 50}, \"task_8_bowl_on_plate\": {\"sr\": 0.86, \"succ\": 43, \"total\": 50}, \"task_9_wine_on_rack\": {\"sr\": 0.04, \"succ\": 2, \"total\": 50}}, \"total_episodes\": 500, \"total_successes\": 336, \"wilson_ci_95\": [0.63, 0.712]}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k05_long_seed42_v3\": {\"conclusion\": \"success\", \"metrics\": {\"elapsed_min\": 154.8, \"success_rate\": 51.4, \"total_episodes\": 500, \"total_successes\": 257}, \"status\": \"DONE\"}, \"eval_pi05_random_k0925_spatial_seed42_unreg\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 58.2, \"total_episodes\": 500, \"total_successes\": 291}, \"status\": \"DONE\"}, \"eval_pi05_random_k05_long_seed42_v2\": {\"conclusion\": \"success\", \"metrics\": {\"cpu_rng_fixed\": true, \"elapsed_min\": 160, \"importance_margin_vs_l2norm\": {\"l2norm_k05_long_sr\": 50.2, \"margin_pp\": 3.4, \"random_k05_long_sr\": 46.8}, \"keep_ratio\": 0.5, \"model\": \"pi05\", \"per_task\": {\"T0_alphabet_soup_tomato_basket\": 0.7, \"T1_cream_cheese_butter_basket\": 0.4, \"T2_stove_moka_pot\": 0.72, \"T3_bowl_bottom_drawer\": 0.72, \"T4_white_mug_left_yellow_right\": 0.52, \"T5_book_caddy\": 0.2, \"T6_white_mug_plate_chocolate\": 0.26, \"T7_alphabet_soup_cream_cheese_basket\": 0.56, \"T8_both_moka_pots_stove\": 0.04, \"T9_yellow_mug_microwave\": 0.56}, \"prune_mode\": \"random\", \"seed\": 42, \"success_rate\": 46.8, \"suite\": \"libero_10\", \"total_episodes\": 500, \"total_successes\": 234, \"v1_comparison\": {\"delta_pp\": -3.4, \"note\": \"CPU RNG fix caused -3.4pp drop\", \"v1_sr\": 50.2, \"v2_sr\": 46.8}}, \"status\": \"DONE\"}, \"eval_pi05_attention_k05_goal_seed42\": {\"conclusion\": \"negative\", \"metrics\": {\"elapsed_min\": 84.9, \"per_task\": {\"T0_open_middle_drawer\": 0.76, \"T1_put_bowl_stove\": 0.4, \"T2_wine_bottle_cabinet\": 0.76, \"T3_open_drawer_bowl\": 0.68, \"T4_bowl_top_cabinet\": 0.94, \"T5_push_plate_front\": 0.7, \"T6_cream_cheese_bowl\": 0.54, \"T7_turn_on_stove\": 1, \"T8_bowl_on_plate\": 0.86, \"T9_wine_bottle_rack\": 0.38}, \"success_rate\": 70.2, \"total_episodes\": 500, \"total_successes\": 351}, \"status\": \"DONE\"}, \"eval_xvla_l2norm_k03_goal_seed42_v4\": {\"conclusion\": \"negative\", \"metrics\": {\"success_rate\": 37.6, \"total_episodes\": 500, \"total_successes\": 188}, \"status\": \"DONE\"}, \"eval_xvla_random_k05_goal_seed42_v2\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 67.2, \"total_episodes\": 500, \"total_successes\": 336}, \"status\": \"DONE\"}, \"eval_xvla_random_k05_object_seed43\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.71, \"total_episodes\": 500, \"total_successes\": 355, \"wilson_ci_95\": [0.6687, 0.7481]}, \"status\": \"DONE\"}, \"eval_pi05_random_k085_goal_seed42_v4\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 52.4, \"total_episodes\": 500, \"total_successes\": 262}, \"status\": \"DONE\"}, \"eval_xvla_l2norm_k03_spatial_seed42\": {\"conclusion\": \"negative\", \"metrics\": {\"elapsed_seconds\": 6754.6, \"n_vision_tokens_kept\": 15, \"n_vision_tokens_original\": 50, \"per_task\": {\"task_0\": {\"desc\": \"pick up the black bowl between the plate and the ramekin and place it on the plate\", \"sr\": 0.74}, \"task_1\": {\"desc\": \"pick up the black bowl next to the ramekin and place it on the plate\", \"sr\": 0.06}, \"task_2\": {\"desc\": \"pick up the black bowl from table center and place it on the plate\", \"sr\": 0.82}, \"task_3\": {\"desc\": \"pick up the black bowl on the cookie box and place it on the plate\", \"sr\": 0.34}, \"task_4\": {\"desc\": \"pick up the black bowl in the top drawer of the wooden cabinet and place it on the plate\", \"sr\": 0.66}, \"task_5\": {\"desc\": \"pick up the black bowl on the ramekin and place it on the plate\", \"sr\": 0}, \"task_6\": {\"desc\": \"pick up the black bowl next to the cookie box and place it on the plate\", \"sr\": 0.04}, \"task_7\": {\"desc\": \"pick up the black bowl on the stove and place it on the plate\", \"sr\": 0.08}, \"task_8\": {\"desc\": \"pick up the black bowl next to the plate and place it on the plate\", \"sr\": 0.34}, \"task_9\": {\"desc\": \"pick up the black bowl on the wooden cabinet and place it on the plate\", \"sr\": 0.04}}, \"success_rate\": 0.312, \"total_episodes\": 500, \"total_successes\": 156, \"wilson_ci_95\": [0.273, 0.354]}, \"status\": \"DONE\"}, \"eval_xvla_l2norm_k05_goal_seed42_v3\": {\"conclusion\": \"negative\", \"metrics\": {\"elapsed_min\": 65.8, \"per_task\": {\"T0_open_middle_drawer\": 0.8, \"T1_put_bowl_stove\": 0.92, \"T2_wine_bottle_cabinet\": 0.98, \"T3_open_drawer_bowl\": 0.34, \"T4_bowl_top_cabinet\": 1, \"T5_push_plate_front\": 0, \"T6_cream_cheese_bowl\": 0.24, \"T7_turn_on_stove\": 0.72, \"T8_bowl_on_plate\": 0.9, \"T9_wine_bottle_rack\": 0}, \"success_rate\": 59, \"total_episodes\": 500, \"total_successes\": 295}, \"status\": \"DONE\"}, \"eval_xvla_l2norm_k05_spatial_seed42_v3\": {\"conclusion\": \"negative\", \"metrics\": {\"elapsed_min\": 82, \"per_task_sr\": [92, 22, 88, 72, 84, 0, 82, 32, 72, 44], \"success_rate\": 58.8, \"total_episodes\": 500, \"wilson_ci_95\": [54.4, 63]}, \"status\": \"DONE\"}, \"eval_xvla_l2norm_k07_goal_seed42\": {\"conclusion\": \"negative\", \"metrics\": {\"num_episodes\": 500, \"num_success\": 267, \"seed\": 42, \"success_rate\": 0.534, \"suite\": \"libero_goal\"}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k0925_goal_seed42_w38\": {\"conclusion\": \"killed\", \"status\": \"DONE\"}, \"eval_e5_xvla_attn_last_goal_k03\": {\"conclusion\": \"killed\", \"status\": \"DONE\"}, \"eval_pi05_random_k07_goal_seed42_v2\": {\"conclusion\": \"negative\", \"metrics\": {\"source\": \"westd-41074 diag harvested, CPU RNG fixed\", \"success_rate\": 78.2, \"total_episodes\": 500, \"total_successes\": 391}, \"status\": \"DONE\"}, \"eval_pi05_random_k095_goal_seed42_v2\": {\"conclusion\": \"success\", \"metrics\": {\"source\": \"westd-41074 diag harvested, CPU RNG fixed\", \"success_rate\": 83.8, \"total_episodes\": 500, \"total_successes\": 419}, \"status\": \"DONE\"}, \"eval_pi05_random_k09_goal_seed42_v2\": {\"conclusion\": \"negative\", \"metrics\": {\"source\": \"westd-41074 GPU diag harvested, CPU RNG fixed\", \"success_rate\": 62.2, \"total_episodes\": 500}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k0925_goal_seed43\": {\"conclusion\": \"success\", \"metrics\": {\"comparison_seed42_sr\": 89, \"per_task\": {\"T0_open_middle_drawer_of_cabinet\": 92, \"T1_put_bowl_on_stove\": 98, \"T2_put_wine_bottle_on_top_of_cabinet\": 100, \"T3_open_top_drawer_put_bowl_inside\": 92, \"T4_put_bowl_on_top_of_cabinet\": 98, \"T5_push_plate_to_front_of_stove\": 100, \"T6_put_cream_cheese_in_bowl\": 92, \"T7_turn_on_stove\": 98, \"T8_put_bowl_on_plate\": 96, \"T9_put_wine_bottle_on_rack\": 42}, \"seed\": 43, \"seed_delta_pp\": 1.8, \"success_rate\": 90.8, \"total_episodes\": 500, \"total_successes\": 454}, \"status\": \"DONE\"}, \"eval_pi05_random_k085_spatial_seed42_v2\": {\"conclusion\": \"success\", \"metrics\": {\"source\": \"SSH log harvest by diagnostic worker\", \"success_rate\": 56.6, \"total_episodes\": 500}, \"status\": \"DONE\"}, \"eval_pi05_random_k0925_goal_seed42_w38\": {\"conclusion\": \"killed\", \"status\": \"DONE\"}, \"eval_e5_xvla_attn_mean_goal_k03\": {\"conclusion\": \"killed\", \"status\": \"DONE\"}, \"eval_pi05_l2norm_k085_goal_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"keep_ratio\": 0.85, \"prune_mode\": \"l2norm\", \"seed\": 42, \"success_rate\": 88, \"successes\": 440, \"suite\": \"libero_goal\", \"total\": 500}, \"status\": \"DONE\"}, \"eval_pi05_random_k0925_spatial_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate_mean\": 60.4}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k0925_goal_seed42_v2\": {\"conclusion\": \"success\", \"metrics\": {\"per_task\": {\"T0\": 86, \"T1\": 96, \"T2\": 100, \"T3\": 90, \"T4\": 98, \"T5\": 98, \"T6\": 88, \"T7\": 100, \"T8\": 94, \"T9\": 40}, \"success_rate\": 89, \"total_episodes\": 500, \"total_successes\": 445}, \"status\": \"DONE\"}, \"eval_pi05_random_k0925_goal_seed42_v2\": {\"conclusion\": \"negative\", \"metrics\": {\"elapsed_min\": 74.8, \"source\": \"SSH log harvest by diagnostic worker\", \"success_rate\": 71.2, \"total_episodes\": 500, \"total_successes\": 356}, \"status\": \"DONE\"}, \"eval_openvla_baseline_goal_seed42_v3\": {\"conclusion\": \"success\", \"metrics\": {\"elapsed_min\": 242.4, \"source\": \"SSH log harvest by diagnostic worker\", \"success_rate\": 74.8, \"total_episodes\": 500, \"total_successes\": 374}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k085_spatial_seed42_v2\": {\"conclusion\": \"success\", \"metrics\": {\"elapsed_min\": 67.3, \"source\": \"SSH log harvest by diagnostic worker\", \"success_rate\": 88.6, \"total_episodes\": 500, \"total_successes\": 443}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k03_goal_seed42_v2\": {\"conclusion\": \"negative\", \"metrics\": {\"per_task\": {\"T0\": 66, \"T1\": 22, \"T2\": 76, \"T3\": 32, \"T4\": 62, \"T5\": 30, \"T6\": 20, \"T7\": 96, \"T8\": 78, \"T9\": 24}, \"success_rate\": 50.6, \"total_episodes\": 500, \"total_successes\": 253}, \"status\": \"DONE\"}, \"eval_xvla_random_k05_goal_seed42\": {\"conclusion\": \"failed\", \"metrics\": {\"elapsed_min\": 158.9, \"episodes\": 500, \"per_task_sr\": {\"task0_open_middle_drawer\": 0, \"task1_bowl_on_stove\": 0, \"task2_wine_on_cabinet\": 0, \"task3_open_drawer_bowl_inside\": 0, \"task4_bowl_on_cabinet\": 0, \"task5_push_plate_front_stove\": 0, \"task6_cream_cheese_in_bowl\": 0, \"task7_turn_on_stove\": 0, \"task8_bowl_on_plate\": 0, \"task9_wine_on_rack\": 0}, \"success_rate\": 0, \"tasks\": 10, \"wilson_ci_95\": [0, 0.8]}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k07_goal_seed42_v2\": {\"conclusion\": \"negative\", \"metrics\": {\"source\": \"SSH log harvest by diagnostic worker\", \"success_rate\": 73.6, \"total_episodes\": 500}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k09_goal_seed42_v2\": {\"conclusion\": \"success\", \"metrics\": {\"source\": \"SSH log harvest by diagnostic worker\", \"success_rate\": 90.6, \"total_episodes\": 500}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k095_goal_seed42_v2\": {\"conclusion\": \"success\", \"metrics\": {\"source\": \"SSH log harvest by diagnostic worker\", \"success_rate\": 89.4, \"total_episodes\": 500}, \"status\": \"DONE\"}, \"eval_e5_xvla_attn_rollout_goal_k05_v2\": {\"conclusion\": \"success\", \"metrics\": {\"elapsed_min\": 31.1, \"success_rate\": 96.8, \"total_episodes\": 500, \"total_successes\": 484, \"wilson_ci_95\": [94.9, 98]}, \"status\": \"DONE\"}, \"eval_e5_xvla_attn_mean_goal_k05_v2\": {\"conclusion\": \"success\", \"metrics\": {\"elapsed_min\": 30.2, \"success_rate\": 97.4, \"total_episodes\": 500, \"total_successes\": 487, \"wilson_ci_95\": [95.6, 98.5]}, \"status\": \"DONE\"}, \"eval_e5_xvla_attn_last_goal_k05_v2\": {\"conclusion\": \"success\", \"metrics\": {\"elapsed_min\": 30, \"success_rate\": 98.2, \"total_episodes\": 500, \"total_successes\": 491, \"wilson_ci_95\": [96.6, 99.1]}, \"status\": \"DONE\"}, \"eval_e5_xvla_random_goal_k05_v2\": {\"conclusion\": \"negative\", \"metrics\": {\"elapsed_min\": 58.2, \"success_rate\": 67.2, \"total_episodes\": 500, \"total_successes\": 336, \"wilson_ci_95\": [63, 71.2]}, \"status\": \"DONE\"}, \"eval_pi05_random_k03_goal_seed42_v2\": {\"conclusion\": \"negative\", \"metrics\": {\"source\": \"westd-41074 diag harvested, CPU RNG fixed\", \"success_rate\": 50.6, \"total_episodes\": 500, \"total_successes\": 253}, \"status\": \"DONE\"}, \"eval_e5_xvla_attn_last_obj_k03\": {\"conclusion\": \"success\", \"metrics\": {\"elapsed_min\": 45.2, \"source\": \"Worker harvested from westd-27271\", \"success_rate\": 84.2, \"total_episodes\": 500, \"total_successes\": 421, \"wilson_ci_95\": [80.7, 87.1]}, \"status\": \"DONE\"}, \"eval_e5_xvla_attn_rollout_obj_k03\": {\"conclusion\": \"success\", \"metrics\": {\"source\": \"Director harvested from westd-38929\", \"success_rate\": 92, \"total_episodes\": 500, \"total_successes\": 460}, \"status\": \"DONE\"}, \"eval_e5_xvla_attn_mean_spatial_k03\": {\"conclusion\": \"success\", \"metrics\": {\"source\": \"Director harvested from westd-38929\", \"success_rate\": 90.4, \"total_episodes\": 500, \"total_successes\": 452}, \"status\": \"DONE\"}, \"eval_e5_xvla_attn_last_spatial_k03\": {\"conclusion\": \"success\", \"metrics\": {\"source\": \"Director harvested from westd-38929\", \"success_rate\": 85.6, \"total_episodes\": 500, \"total_successes\": 428}, \"status\": \"DONE\"}, \"eval_e5_xvla_attn_mean_obj_k03\": {\"conclusion\": \"success\", \"metrics\": {\"source\": \"Director harvested from westd-38929\", \"success_rate\": 96, \"total_episodes\": 500, \"total_successes\": 480}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k0925_spatial_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"overall_SR\": 0.97, \"per_task\": {\"T0\": 1, \"T1\": 0.98, \"T2\": 0.98, \"T3\": 0.94, \"T4\": 0.92, \"T5\": 0.94, \"T6\": 1, \"T7\": 0.98, \"T8\": 1, \"T9\": 0.96}, \"total_episodes\": 500, \"total_successes\": 485}, \"status\": \"DONE\"}, \"eval_pi05_random_k085_spatial_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"seed\": 42, \"success_rate\": 0.584, \"suite\": \"libero_spatial\"}, \"status\": \"DONE\"}, \"eval_e5_xvla_attn_mean_spatial_k05\": {\"conclusion\": \"success\", \"metrics\": {\"episodes\": 500, \"success_rate\": 91.6, \"successes\": 458, \"wilson_ci_95\": [88.8, 93.7]}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k09_goal_seed42\": {\"conclusion\": \"negative\", \"metrics\": {\"num_episodes\": 500, \"num_success\": 450, \"seed\": 42, \"success_rate\": 0.9, \"suite\": \"libero_goal\"}, \"status\": \"DONE\"}, \"eval_pi05_random_k07_goal_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"num_episodes\": 500, \"num_success\": 403, \"seed\": 42, \"success_rate\": 0.806, \"suite\": \"libero_goal\"}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k05_goal_seed42\": {\"conclusion\": \"negative\", \"metrics\": {\"num_episodes\": 500, \"num_success\": 296, \"seed\": 42, \"success_rate\": 0.592, \"suite\": \"libero_goal\"}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k085_long_seed43_v4\": {\"conclusion\": \"success\", \"metrics\": {\"elapsed_min\": 140.4, \"overall_sr\": 0.77, \"total_episodes\": 500, \"total_successes\": 385}, \"status\": \"DONE\"}, \"eval_pi05_random_k085_long_seed43_v3\": {\"conclusion\": \"success\", \"metrics\": {\"elapsed_min\": 170.8, \"overall_sr\": 0.424, \"total_episodes\": 500, \"total_successes\": 212}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k07_long_seed43_v4\": {\"conclusion\": \"success\", \"metrics\": {\"elapsed_min\": 148, \"overall_sr\": 0.654, \"total_episodes\": 500, \"total_successes\": 327}, \"status\": \"DONE\"}, \"eval_e5_xvla_attn_rollout_spatial_k05\": {\"conclusion\": \"success\", \"metrics\": {\"elapsed_min\": 42.8, \"episodes\": 500, \"overall_sr\": 92.8, \"per_task_sr\": {\"T0_bowl_between_plate_ramekin\": 100, \"T1_bowl_next_ramekin\": 100, \"T2_bowl_table_center\": 100, \"T3_bowl_on_cookie_box\": 100, \"T4_bowl_top_drawer_cabinet\": 90, \"T5_bowl_on_ramekin\": 46, \"T6_bowl_next_cookie_box\": 100, \"T7_bowl_on_stove\": 94, \"T8_bowl_next_plate\": 98, \"T9_bowl_on_cabinet\": 100}, \"tasks\": 10, \"wilson_ci_95\": [90.2, 94.8]}, \"status\": \"DONE\"}, \"eval_xvla_l2norm_k07_long_seed42_v2\": {\"conclusion\": \"killed\", \"status\": \"DONE\"}, \"eval_xvla_l2norm_k07_long_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"overall_SR\": 0.494, \"per_task_SR\": {\"T0_alphabet_soup_tomato\": 0.12, \"T1_cream_cheese_butter\": 0.04, \"T2_stove_moka\": 0.56, \"T3_bowl_drawer\": 0.98, \"T4_mugs_plates\": 0.68, \"T5_book_caddy\": 0.94, \"T6_mug_pudding\": 0.78, \"T7_soup_cream_cheese\": 0.76, \"T8_two_moka_pots\": 0, \"T9_mug_microwave\": 0.08}, \"total_episodes\": 500, \"total_successes\": 247}, \"status\": \"DONE\"}, \"eval_xvla_random_k09_long_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"elapsed_min\": 104.4, \"episodes\": 500, \"overall_sr\": 29.6, \"per_task_sr\": {\"task_0_alphabet_soup_tomato_sauce\": 0, \"task_1_cream_cheese_butter\": 16, \"task_2_stove_moka_pot\": 0, \"task_3_black_bowl_drawer\": 96, \"task_4_white_mug_yellow_mug\": 36, \"task_5_book_caddy\": 98, \"task_6_white_mug_chocolate_pudding\": 0, \"task_7_alphabet_soup_cream_cheese\": 0, \"task_8_both_moka_pots\": 0, \"task_9_mug_microwave\": 50}, \"wilson_ci_95\": [25.8, 33.7]}, \"status\": \"DONE\"}, \"eval_xvla_random_k07_long_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"keep_ratio\": 0.7, \"per_task_sr\": [10, 8, 66, 98, 82, 100, 82, 70, 4, 10], \"prune_method\": \"random\", \"seed\": 42, \"success_rate\": 53, \"suite\": \"libero_10\", \"tokens_kept\": \"35/50\", \"total_episodes\": 500, \"total_successes\": 265, \"wall_time_min\": 87, \"wilson_ci_95\": [48.6, 57.3]}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k095_object_seed42_v2\": {\"conclusion\": \"success\", \"metrics\": {\"per_task_sr\": [96, 98, 96, 96, 96, 100, 100, 100, 100, 100], \"success_rate\": 98.2, \"tokens_kept\": 243, \"tokens_total\": 256, \"total_episodes\": 500, \"total_successes\": 491, \"wall_time_min\": 63.2}, \"status\": \"DONE\"}, \"eval_pi05_random_k09_object_seed43_v4\": {\"conclusion\": \"success\", \"metrics\": {\"keep_ratio\": 0.9, \"per_task_sr\": [16, 16, 10, 2, 6, 14, 14, 2, 8, 8], \"prune_method\": \"random\", \"seed\": 43, \"success_rate\": 9.6, \"suite\": \"libero_object\", \"tokens_kept\": 230, \"tokens_total\": 256, \"total_episodes\": 500, \"total_successes\": 48, \"wall_time_min\": 119.5}, \"status\": \"DONE\"}, \"eval_xvla_random_k07_spatial_seed42\": {\"conclusion\": \"negative\", \"metrics\": {\"overall_SR\": 0.766, \"total_episodes\": 500, \"total_successes\": 383}, \"status\": \"DONE\"}, \"eval_xvla_random_k095_long_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"eval_episodes_per_task\": 50, \"keep_ratio\": 0.95, \"per_task_sr\": [0, 46, 72, 90, 54, 98, 18, 10, 92, 2], \"prune_method\": \"random\", \"seed\": 42, \"success_rate\": 48.2, \"suite\": \"libero_10\", \"tokens_kept\": \"47/50\", \"total_episodes\": 500, \"total_success\": 241, \"wall_time_min\": 91.2, \"wilson_ci_95\": [43.9, 52.6]}, \"status\": \"DONE\"}, \"eval_pi05_random_k09_object_seed43_v3\": {\"conclusion\": \"success\", \"metrics\": {\"note\": \"Harvested from eval_results/pi05_random_k0.90_libero_object_seed43.json on westd-27271. Reviewer-confirmed.\", \"seed\": 43, \"success_rate\": 9.6, \"total_episodes\": 500, \"total_successes\": 48}, \"status\": \"DONE\"}, \"eval_pi05_random_k05_long_seed43_v2\": {\"conclusion\": \"success\", \"metrics\": {\"benchmark\": \"libero_10\", \"keep_ratio\": 0.5, \"prune_method\": \"random\", \"success_rate\": 51.2, \"total_episodes\": 500, \"total_success\": 256}, \"status\": \"DONE\"}, \"eval_pi05_random_k085_long_seed43\": {\"conclusion\": \"success\", \"metrics\": {\"benchmark\": \"libero_10\", \"keep_ratio\": 0.85, \"prune_method\": \"random\", \"success_rate\": 41.8, \"total_episodes\": 500, \"total_success\": 209}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k07_long_seed43_v2\": {\"conclusion\": \"success\", \"metrics\": {\"benchmark\": \"libero_10\", \"keep_ratio\": 0.7, \"prune_method\": \"l2norm\", \"success_rate\": 65.8, \"total_episodes\": 500, \"total_success\": 329}, \"status\": \"DONE\"}, \"eval_pi05_random_k03_long_seed43_v3\": {\"conclusion\": \"success\", \"metrics\": {\"benchmark\": \"libero_10\", \"keep_ratio\": 0.3, \"prune_method\": \"random\", \"success_rate\": 28.4, \"total_episodes\": 500, \"total_success\": 142}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k085_long_seed43_v2\": {\"conclusion\": \"success\", \"metrics\": {\"benchmark\": \"libero_10\", \"keep_ratio\": 0.85, \"per_task_sr\": {\"T2\": 88, \"T3\": 96, \"T4\": 70, \"T5\": 98, \"T6\": 12, \"T7\": 80, \"T8\": 64, \"T9\": 88}, \"prune_method\": \"l2norm\", \"success_rate\": 79, \"total_episodes\": 500, \"total_success\": 395}, \"status\": \"DONE\"}, \"eval_pi05_random_k05_spatial_seed43_v2\": {\"conclusion\": \"success\", \"metrics\": {\"elapsed_min\": 80.6, \"per_task_sr\": {\"T0_between_plate_ramekin\": 88, \"T1_next_to_ramekin\": 88, \"T2_table_center\": 88, \"T3_on_cookie_box\": 56, \"T4_top_drawer\": 38, \"T5_on_ramekin\": 32, \"T6_next_to_cookie_box\": 86, \"T7_on_stove\": 92, \"T8_next_to_plate\": 72, \"T9_on_wooden_cabinet\": 84}, \"success_rate\": 72.4, \"total_episodes\": 500, \"total_successes\": 362}, \"status\": \"DONE\"}, \"eval_xvla_baseline_spatial_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"note\": \"Corrected from 0.916 to 0.930 per Reviewer SSH verification of xvla_prune_k1.0_libero_spatial.json (465/500)\", \"num_episodes\": 500, \"success_rate\": 0.93, \"total_successes\": 465, \"wilson_ci_95\": [0.904, 0.95]}, \"status\": \"DONE\"}, \"eval_xvla_baseline_goal_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"note\": \"Corrected from 0.98 to 0.984 per Reviewer SSH verification (492/500)\", \"num_episodes\": 500, \"success_rate\": 0.984, \"total_successes\": 492, \"wilson_ci_95\": [0.969, 0.992]}, \"status\": \"DONE\"}, \"eval_xvla_prune_k09_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"note\": \"Reconstructed entry. SR=99.2% (seed42). Cross-seed range 97.6%–99.2% (seed43=97.6%, seed44=98.2%). Original JSON may exist on cqa1-33015.\", \"num_episodes\": 500, \"seed\": 42, \"success_rate\": 0.992}, \"status\": \"DONE\"}, \"eval_pi05_random_k09_long_seed43\": {\"conclusion\": \"success\", \"metrics\": {\"sr\": 0.308, \"total_episodes\": 500}, \"status\": \"DONE\"}, \"eval_pi05_random_k05_spatial_seed43\": {\"conclusion\": \"negative\", \"status\": \"DONE\"}, \"eval_pi05_random_k085_spatial_seed43\": {\"conclusion\": \"success\", \"metrics\": {\"overall_SR\": 0.576, \"per_task\": {\"T0\": 0.82, \"T1\": 0.62, \"T2\": 0.9, \"T3\": 0.08, \"T4\": 0.48, \"T5\": 0.38, \"T6\": 0.38, \"T7\": 0.74, \"T8\": 0.92, \"T9\": 0.44}, \"total_episodes\": 500, \"total_successes\": 288}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k085_spatial_seed43\": {\"conclusion\": \"success\", \"metrics\": {\"overall_SR\": 0.88, \"per_task\": {\"T0\": 1, \"T1\": 0.92, \"T2\": 1, \"T3\": 0.78, \"T4\": 0.62, \"T5\": 0.84, \"T6\": 0.96, \"T7\": 0.9, \"T8\": 0.96, \"T9\": 0.82}, \"total_episodes\": 500, \"total_successes\": 440}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k095_spatial_seed43\": {\"conclusion\": \"success\", \"metrics\": {\"overall_SR\": 0.98, \"total_episodes\": 500, \"total_successes\": 490}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k07_long_seed43\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"eval_pi05_random_k03_long_seed43\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"eval_pi05_l2norm_k085_long_seed43\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"eval_pi05_random_k095_goal_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"sr\": 0.84, \"total_episodes\": 500, \"total_successes\": 420}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k03_long_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"sr\": 0.39, \"total_episodes\": 500, \"total_successes\": 195}, \"status\": \"DONE\"}, \"eval_xvla_random_k095_object_seed42_v2\": {\"conclusion\": \"success\", \"metrics\": {\"elapsed_seconds\": 2068.5, \"success_rate\": 0.988, \"total_episodes\": 500, \"total_successes\": 494}, \"status\": \"DONE\"}, \"eval_pi05_random_k03_long_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"elapsed_min\": 171, \"success_rate\": 0.29, \"total_episodes\": 500, \"total_successes\": 145}, \"status\": \"DONE\"}, \"eval_pi05_attention_k07_object_seed42\": {\"conclusion\": \"negative\", \"metrics\": {\"elapsed_min\": 117.26, \"keep_ratio\": 0.7, \"prune_mode\": \"attention\", \"seed\": 42, \"success_rate\": 0.006, \"suite\": \"libero_object\", \"total_episodes\": 500, \"total_successes\": 3}, \"status\": \"DONE\"}, \"eval_smolvla_baseline_spatial_seed42_cqa1\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"eval_xvla_random_k07_goal_seed42\": {\"conclusion\": \"negative\", \"metrics\": {\"overall_SR\": 0.572, \"total_episodes\": 500, \"total_successes\": 286}, \"status\": \"DONE\"}, \"eval_pi05_random_k09_long_seed42\": {\"conclusion\": \"negative\", \"metrics\": {\"overall_SR\": 0.318, \"total_episodes\": 500, \"total_successes\": 159}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k09_long_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"overall_SR\": 0.81, \"total_episodes\": 500, \"total_successes\": 405}, \"status\": \"DONE\"}, \"eval_xvla_random_k09_spatial_seed42\": {\"conclusion\": \"negative\", \"metrics\": {\"overall_SR\": 0.778, \"total_episodes\": 500, \"total_successes\": 389}, \"status\": \"DONE\"}, \"eval_xvla_random_k09_goal_seed42\": {\"conclusion\": \"negative\", \"metrics\": {\"overall_SR\": 0.706, \"total_episodes\": 500, \"total_successes\": 353}, \"status\": \"DONE\"}, \"eval_xvla_random_k095_spatial_seed42\": {\"conclusion\": \"negative\", \"metrics\": {\"overall_SR\": 0.702, \"total_episodes\": 500, \"total_successes\": 351}, \"status\": \"DONE\"}, \"eval_xvla_random_k095_goal_seed42\": {\"conclusion\": \"negative\", \"metrics\": {\"overall_SR\": 0.54, \"total_episodes\": 500, \"total_successes\": 270}, \"status\": \"DONE\"}, \"eval_openvla_baseline_spatial_seed42\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"eval_pi05_l2norm_k095_spatial_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"seed\": 42, \"success_rate\": 0.978, \"suite\": \"libero_spatial\"}, \"status\": \"DONE\"}, \"eval_pi05_random_k0925_object_seed43\": {\"conclusion\": \"success\", \"metrics\": {\"seed\": 43, \"success_rate\": 0.3, \"suite\": \"libero_object\"}, \"status\": \"DONE\"}, \"eval_smolvla_baseline_spatial_seed42\": {\"conclusion\": \"failed\", \"metrics\": {\"failure_reason\": \"Ghost process: no GPU assigned, PID 224849 likely dead after westd-38929 GPUs reassigned to OpenVLA experiments\"}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k085_long_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"elapsed_min\": 133.4, \"keep_ratio\": 0.85, \"num_episodes\": 500, \"num_success\": 390, \"prune_mode\": \"l2norm\", \"seed\": 42, \"success_rate\": 0.78, \"suite\": \"libero_10\"}, \"status\": \"DONE\"}, \"eval_pi05_random_k095_long_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"elapsed_min\": 157.6, \"keep_ratio\": 0.95, \"num_episodes\": 500, \"num_success\": 306, \"prune_mode\": \"random\", \"seed\": 42, \"success_rate\": 0.612, \"suite\": \"libero_10\"}, \"status\": \"DONE\"}, \"eval_pi05_random_k085_goal_seed42_v3\": {\"conclusion\": \"success\", \"metrics\": {\"num_episodes\": 500, \"num_success\": 262, \"seed\": 42, \"success_rate\": 0.524, \"suite\": \"libero_goal\"}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k0925_spatial_seed43\": {\"conclusion\": \"negative\", \"status\": \"DONE\"}, \"eval_pi05_l2norm_k09_object_seed43\": {\"conclusion\": \"negative\", \"status\": \"DONE\"}, \"eval_pi05_l2norm_k095_object_seed43_v2\": {\"conclusion\": \"negative\", \"status\": \"DONE\"}, \"eval_pi05_l2norm_k0925_object_seed43_v2\": {\"conclusion\": \"negative\", \"status\": \"DONE\"}, \"eval_pi05_l2norm_k095_long_seed42\": {\"conclusion\": \"negative\", \"status\": \"DONE\"}, \"eval_pi05_l2norm_k085_goal_seed42_w38929\": {\"conclusion\": \"negative\", \"status\": \"DONE\"}, \"random_k095_goal_seed42\": {\"conclusion\": \"negative\", \"status\": \"DONE\"}, \"pi05_l2norm_k09_goal_s42\": {\"conclusion\": \"negative\", \"status\": \"DONE\"}, \"eval_pi05_random_k085_goal_seed42_v2\": {\"conclusion\": \"negative\", \"status\": \"DONE\"}, \"l2norm_k095_goal_seed42\": {\"conclusion\": \"negative\", \"status\": \"DONE\"}, \"random_k095_long_seed42\": {\"conclusion\": \"negative\", \"status\": \"DONE\"}, \"pi05_l2norm_k095_long_s42\": {\"conclusion\": \"negative\", \"status\": \"DONE\"}, \"pi05_random_k09_goal_s42\": {\"conclusion\": \"negative\", \"status\": \"DONE\"}, \"pi05_l2norm_k085_goal_s42\": {\"conclusion\": \"negative\", \"status\": \"DONE\"}, \"train_openvla_sc_m96_seed42_v3\": {\"conclusion\": \"negative\", \"status\": \"DONE\"}, \"train_openvla_sc_m64_seed42_v6\": {\"conclusion\": \"negative\", \"status\": \"DONE\"}, \"eval_pi05_attention_k085_object_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"num_episodes\": 500, \"num_success\": 461, \"seed\": 42, \"success_rate\": 0.922, \"suite\": \"libero_object\"}, \"status\": \"DONE\"}, \"eval_pi05_attention_k09_object_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"num_episodes\": 500, \"num_success\": 486, \"seed\": 42, \"success_rate\": 0.972, \"suite\": \"libero_object\"}, \"status\": \"DONE\"}, \"smolvla_random_k095_long_seed42\": {\"conclusion\": \"negative\", \"metrics\": {\"num_episodes\": 500, \"num_success\": 0, \"seed\": 42, \"success_rate\": 0, \"suite\": \"libero_10\"}, \"status\": \"DONE\"}, \"smolvla_l2norm_k095_long_seed42\": {\"conclusion\": \"negative\", \"metrics\": {\"num_episodes\": 500, \"num_success\": 0, \"seed\": 42, \"success_rate\": 0, \"suite\": \"libero_10\"}, \"status\": \"DONE\"}, \"smolvla_random_k095_goal_seed42\": {\"conclusion\": \"negative\", \"metrics\": {\"num_episodes\": 500, \"num_success\": 21, \"seed\": 42, \"success_rate\": 0.042, \"suite\": \"libero_goal\"}, \"status\": \"DONE\"}, \"smolvla_l2norm_k095_goal_seed42\": {\"conclusion\": \"negative\", \"metrics\": {\"num_episodes\": 500, \"num_success\": 17, \"seed\": 42, \"success_rate\": 0.034, \"suite\": \"libero_goal\"}, \"status\": \"DONE\"}, \"smolvla_random_k095_spatial_seed42\": {\"conclusion\": \"negative\", \"metrics\": {\"num_episodes\": 500, \"num_success\": 21, \"seed\": 42, \"success_rate\": 0.042, \"suite\": \"libero_spatial\"}, \"status\": \"DONE\"}, \"smolvla_l2norm_k095_spatial_seed42\": {\"conclusion\": \"negative\", \"metrics\": {\"num_episodes\": 500, \"num_success\": 33, \"seed\": 42, \"success_rate\": 0.066, \"suite\": \"libero_spatial\"}, \"status\": \"DONE\"}, \"smolvla_baseline_long_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"num_episodes\": 500, \"num_success\": 183, \"seed\": 42, \"success_rate\": 0.366, \"suite\": \"libero_10\"}, \"status\": \"DONE\"}, \"eval_xvla_l2norm_k09_spatial_seed42\": {\"conclusion\": \"negative\", \"metrics\": {\"num_episodes\": 500, \"num_success\": 394, \"seed\": 42, \"success_rate\": 0.788, \"suite\": \"libero_spatial\"}, \"status\": \"DONE\"}, \"eval_xvla_l2norm_k09_goal_seed42\": {\"conclusion\": \"negative\", \"metrics\": {\"num_episodes\": 500, \"num_success\": 351, \"seed\": 42, \"success_rate\": 0.702, \"suite\": \"libero_goal\"}, \"status\": \"DONE\"}, \"eval_xvla_l2norm_k095_goal_seed42\": {\"conclusion\": \"negative\", \"metrics\": {\"num_episodes\": 500, \"num_success\": 269, \"seed\": 42, \"success_rate\": 0.538, \"suite\": \"libero_goal\"}, \"status\": \"DONE\"}, \"eval_xvla_l2norm_k095_spatial_seed42\": {\"conclusion\": \"negative\", \"metrics\": {\"num_episodes\": 500, \"num_success\": 358, \"seed\": 42, \"success_rate\": 0.716, \"suite\": \"libero_spatial\"}, \"status\": \"DONE\"}, \"eval_pi05_attention_k095_object_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"keep_tokens\": 690, \"num_episodes\": 500, \"seed\": 42, \"success_rate\": 0.984, \"suite\": \"libero_object\", \"total_tokens\": 768, \"wilson_ci_95\": [0.969, 0.992]}, \"status\": \"DONE\"}, \"eval_xvla_l2norm_k09_long_seed42\": {\"conclusion\": \"negative\", \"metrics\": {\"num_episodes\": 500, \"seed\": 42, \"success_rate\": 0.275, \"suite\": \"libero_10\", \"wilson_ci_95\": [0.218, 0.341]}, \"status\": \"DONE\"}, \"eval_xvla_l2norm_k095_long_seed42\": {\"conclusion\": \"negative\", \"metrics\": {\"num_episodes\": 500, \"seed\": 42, \"success_rate\": 0.47, \"suite\": \"libero_10\", \"wilson_ci_95\": [0.402, 0.539]}, \"status\": \"DONE\"}, \"eval_xvla_baseline_long_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"num_episodes\": 500, \"per_task\": [0.96, 0.68, 1.0, 0.98, 0.94, 0.96, 0.94, 0.96, 1.0, 0.98], \"seed\": 42, \"success_rate\": 0.94, \"suite\": \"libero_10\", \"wilson_ci_95\": [0.916, 0.958]}, \"status\": \"DONE\"}, \"pi05_random_k085_goal_s42\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"smolvla_official_goal_baseline_s42\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.608, \"total_episodes\": 500, \"total_successes\": 304, \"wilson_ci_95\": [0.5645, 0.6498]}, \"status\": \"DONE\"}, \"smolvla_official_object_l2norm_k095_s42\": {\"conclusion\": \"negative\", \"metrics\": {\"success_rate\": 0.002, \"total_episodes\": 500, \"total_successes\": 1, \"wilson_ci_95\": [0.0004, 0.0112]}, \"status\": \"DONE\"}, \"smolvla_official_spatial_baseline_s42\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.446, \"total_episodes\": 500, \"total_successes\": 223, \"wilson_ci_95\": [0.403, 0.4898]}, \"status\": \"DONE\"}, \"eval_pi05_baseline_goal_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"elapsed_min\": 49.7, \"overall_sr\": 0.964, \"per_task\": {\"bowl_on_cabinet\": 1, \"bowl_on_plate\": 1, \"bowl_on_stove\": 1, \"cream_cheese_in_bowl\": 0.96, \"open_middle_drawer\": 0.9, \"open_top_drawer_bowl_inside\": 0.9, \"push_plate_front_stove\": 1, \"turn_on_stove\": 1, \"wine_bottle_on_cabinet\": 0.98, \"wine_bottle_on_rack\": 0.9}, \"total_episodes\": 500, \"total_successes\": 482}, \"status\": \"DONE\"}, \"eval_smolvla_zeromask_l2norm_k095_object_seed42\": {\"conclusion\": \"negative\", \"metrics\": {\"per_task\": {\"task0_alphabet_soup\": 0, \"task1_cream_cheese\": 0, \"task2_salad_dressing\": 0, \"task3_bbq_sauce\": 0, \"task4_ketchup\": 0, \"task5_tomato_sauce\": 0, \"task6_butter\": 0, \"task7_milk\": 0, \"task8_chocolate_pudding\": 0, \"task9_orange_juice\": 0}, \"success_rate\": 0, \"total_episodes\": 500, \"total_successes\": 0, \"wilson_ci_95\": [0, 0.0076]}, \"status\": \"DONE\"}, \"eval_smolvla_zeromask_random_k095_object_seed42\": {\"conclusion\": \"negative\", \"metrics\": {\"per_task\": {\"task0_alphabet_soup\": 0, \"task1_cream_cheese\": 0, \"task2_salad_dressing\": 0, \"task3_bbq_sauce\": 0, \"task4_ketchup\": 0, \"task5_tomato_sauce\": 0.02, \"task6_butter\": 0, \"task7_milk\": 0, \"task8_chocolate_pudding\": 0, \"task9_orange_juice\": 0}, \"success_rate\": 0.002, \"total_episodes\": 500, \"total_successes\": 1, \"wilson_ci_95\": [0.0004, 0.0112]}, \"status\": \"DONE\"}, \"train_openvla_sc_m96_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"final_eval_loss\": 2.6575, \"final_train_loss\": 2.4509, \"steps_completed\": 99999, \"steps_total\": 100000}, \"status\": \"DONE\"}, \"eval_smolvla_official_l2norm_k090_object_seed42\": {\"conclusion\": \"negative\", \"metrics\": {\"SR\": 0, \"episodes\": 500, \"note\": \"all 10 tasks 0% SR, mean_steps=280 (max)\"}, \"status\": \"DONE\"}, \"eval_pi05_random_k03_object_seed43_v4\": {\"conclusion\": \"success\", \"metrics\": {\"overall_SR\": 0.322, \"total_episodes\": 500, \"total_successes\": 161}, \"status\": \"DONE\"}, \"eval_pi05_random_k085_object_seed43\": {\"conclusion\": \"negative\", \"metrics\": {\"overall_SR\": 0.038, \"total_episodes\": 500, \"total_successes\": 19}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k03_spatial_seed43\": {\"conclusion\": \"success\", \"metrics\": {\"overall_SR\": 0.52, \"total_episodes\": 500, \"total_successes\": 260}, \"status\": \"DONE\"}, \"eval_pi05_random_k03_spatial_seed43\": {\"conclusion\": \"success\", \"metrics\": {\"overall_SR\": 0.512, \"total_episodes\": 500, \"total_successes\": 256}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k0925_object_seed43\": {\"conclusion\": \"killed\", \"metrics\": {\"overall_SR\": 0.984, \"total_episodes\": 500, \"total_successes\": 492}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k095_object_seed43\": {\"conclusion\": \"success\", \"metrics\": {\"overall_SR\": 0.984, \"total_episodes\": 500, \"total_successes\": 492}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k07_spatial_seed43\": {\"conclusion\": \"success\", \"metrics\": {\"overall_SR\": 0.684, \"total_episodes\": 500, \"total_successes\": 342}, \"status\": \"DONE\"}, \"eval_pi05_random_k07_spatial_seed43\": {\"conclusion\": \"success\", \"metrics\": {\"overall_SR\": 0.738, \"total_episodes\": 500, \"total_successes\": 369}, \"status\": \"DONE\"}, \"eval_smart_compress_m32_official\": {\"conclusion\": \"killed\", \"metrics\": {\"CI_95_wilson\": \"49.0-57.7\", \"SR\": 53.4, \"episodes\": 500, \"per_task_SR\": [64, 48, 56, 46, 46, 28, 78, 42, 66, 60]}, \"status\": \"DONE\"}, \"eval_pi05_random_k05_object_seed43\": {\"conclusion\": \"success\", \"metrics\": {\"elapsed_min\": 82.3, \"success_rate\": 68.4, \"total_episodes\": 500, \"total_successes\": 342}, \"status\": \"DONE\"}, \"eval_pi05_random_k07_object_seed43\": {\"conclusion\": \"success\", \"metrics\": {\"elapsed_min\": 86.9, \"success_rate\": 73.8, \"total_episodes\": 500, \"total_successes\": 369}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k085_object_seed43\": {\"conclusion\": \"success\", \"metrics\": {\"overall_SR\": 0.984, \"per_task\": {\"T0\": 1, \"T1\": 1, \"T2\": 1, \"T3\": 0.98, \"T4\": 1, \"T5\": 0.96, \"T6\": 0.98, \"T7\": 0.92, \"T8\": 1, \"T9\": 1}, \"total_episodes\": 500, \"total_successes\": 492}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k09_spatial_seed43\": {\"conclusion\": \"success\", \"metrics\": {\"overall_SR\": 0.956, \"total_episodes\": 500, \"total_successes\": 478}, \"status\": \"DONE\"}, \"eval_pi05_random_k09_spatial_seed43\": {\"conclusion\": \"success\", \"metrics\": {\"overall_SR\": 0.536, \"total_episodes\": 500, \"total_successes\": 268}, \"status\": \"DONE\"}, \"eval_pi05_random_k0925_spatial_seed43\": {\"conclusion\": \"success\", \"metrics\": {\"overall_SR\": 0.578, \"total_episodes\": 500, \"total_successes\": 289}, \"status\": \"DONE\"}, \"eval_openvla_l2norm_k05_object_seed42_v5\": {\"conclusion\": \"success\", \"metrics\": {\"overall_SR\": 0.392, \"per_task\": {\"T0\": 0.56, \"T1\": 0.14, \"T2\": 0.38, \"T3\": 0.32, \"T4\": 0.7, \"T5\": 0.32, \"T6\": 0.12, \"T7\": 0.5, \"T8\": 0.44, \"T9\": 0.44}, \"total_episodes\": 500, \"total_successes\": 196}, \"status\": \"DONE\"}, \"eval_pi05_random_k095_spatial_seed43\": {\"conclusion\": \"success\", \"metrics\": {\"overall_SR\": 0.768, \"per_task\": {\"T0\": 1, \"T1\": 0.94, \"T2\": 1, \"T3\": 0.6, \"T4\": 0.36, \"T5\": 0.76, \"T6\": 0.9, \"T7\": 0.74, \"T8\": 1, \"T9\": 0.38}, \"total_episodes\": 500, \"total_successes\": 384}, \"status\": \"DONE\"}, \"eval_pi05_random_k03_object_seed43_v2\": {\"conclusion\": \"killed\", \"status\": \"DONE\"}, \"eval_pi05_random_k085_object_seed43_v2\": {\"conclusion\": \"killed\", \"status\": \"DONE\"}, \"eval_pi05_random_k095_spatial_seed42_v2\": {\"conclusion\": \"killed\", \"status\": \"DONE\"}, \"eval_pi05_l2norm_k07_object_seed43_v3\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate_mean\": 57.2}, \"status\": \"DONE\"}, \"eval_pi05_random_k095_spatial_seed42_v4\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate_mean\": 76.4}, \"status\": \"DONE\"}, \"eval_pi05_random_k095_object_seed43\": {\"conclusion\": \"success\", \"metrics\": {\"elapsed_min\": 85.5, \"per_task_sr\": {\"T0_alphabet_soup\": 0.7, \"T1_cream_cheese\": 0.9, \"T2_salad_dressing\": 0.78, \"T3_bbq_sauce\": 0.66, \"T4_ketchup\": 0.54, \"T5_tomato_sauce\": 0.8, \"T6_butter\": 0.82, \"T7_milk\": 0.66, \"T8_chocolate_pudding\": 0.78, \"T9_orange_juice\": 0.64}, \"success_rate\": 0.728, \"total_episodes\": 500, \"total_successes\": 364}, \"status\": \"DONE\"}, \"eval_pi05_random_k085_object_seed43_v3\": {\"conclusion\": \"negative\", \"metrics\": {\"success_rate_mean\": 3.8}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k0925_object_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"n_episodes\": 500, \"per_task\": {\"T0_alphabet_soup\": 98, \"T1_cream_cheese\": 98, \"T2_salad_dressing\": 96, \"T3_bbq_sauce\": 100, \"T4_ketchup\": 100, \"T5_tomato_sauce\": 100, \"T6_butter\": 100, \"T7_milk\": 100, \"T8_chocolate_pudding\": 100, \"T9_orange_juice\": 100}, \"success_rate\": 99.2, \"successes\": 496}, \"status\": \"DONE\"}, \"eval_pi05_random_k095_spatial_seed42_v3\": {\"conclusion\": \"killed\", \"status\": \"DONE\"}, \"eval_pi05_l2norm_k095_spatial_seed42_v2\": {\"conclusion\": \"killed\", \"status\": \"DONE\"}, \"eval_pi05_l2norm_k07_spatial_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"duration_min\": 98.8, \"episodes\": 500, \"per_task_sr\": \"10 tasks completed, overall 335/500\", \"success_rate\": 67, \"tasks\": 10}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k09_spatial_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"episodes_per_task\": 50, \"keep_ratio\": 0.9, \"prune_mode\": \"l2norm\", \"seed\": 42, \"success_rate_mean\": 0.95, \"suite\": \"libero_spatial\", \"tasks_evaluated\": 10, \"total_episodes\": 500, \"total_success\": 475}, \"status\": \"DONE\"}, \"eval_pi05_random_k09_spatial_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"episodes_per_task\": 50, \"keep_ratio\": 0.9, \"prune_mode\": \"random\", \"seed\": 42, \"success_rate_mean\": 0.546, \"suite\": \"libero_spatial\", \"tasks_evaluated\": 10, \"total_episodes\": 500, \"total_success\": 273}, \"status\": \"DONE\"}, \"eval_pi05_random_k07_spatial_seed42_v2\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"eval_pi05_random_k095_spatial_seed42\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"eval_pi05_l2norm_k085_object_seed42_v4\": {\"conclusion\": \"success\", \"metrics\": {\"elapsed_min\": 64.35, \"overall_sr\": 0.98, \"per_task_sr\": {\"T0_alphabet_soup\": 1, \"T1_cream_cheese\": 1, \"T2_salad_dressing\": 0.98, \"T3_bbq_sauce\": 0.98, \"T4_ketchup\": 0.98, \"T5_tomato_sauce\": 0.98, \"T6_butter\": 1, \"T7_milk\": 0.88, \"T8_chocolate_pudding\": 1, \"T9_orange_juice\": 1}, \"total_episodes\": 500, \"total_successes\": 490}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k085_object_seed42_v2\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"eval_openvla_baseline_spatial_seed42_v3\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"train_openvla_sc_m32_vtconly_seed42\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"eval_pi05_random_k0925_object_seed42\": {\"conclusion\": \"negative\", \"metrics\": {\"elapsed_min\": 108.9, \"overall_sr\": 0.276, \"per_task_sr\": [0.34, 0.42, 0.24, 0.14, 0.08, 0.42, 0.4, 0.12, 0.34, 0.26], \"total_episodes\": 500, \"total_successes\": 138}, \"status\": \"DONE\"}, \"eval_pi05_random_k03_object_seed43\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"eval_pi05_l2norm_k085_object_seed42\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"eval_pi05_random_k085_object_seed42_v2\": {\"conclusion\": \"negative\", \"metrics\": {\"duration_min\": 108.5, \"episodes\": 500, \"per_task_sr\": \"10 tasks completed, overall 25/500\", \"success_rate\": 5, \"tasks\": 10}, \"status\": \"DONE\"}, \"eval_pi05_random_k03_spatial_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"per_task_sr\": {\"T0_between_plate\": 66, \"T1_next_to_ramekin\": 80, \"T2_from_table_center\": 62, \"T3_on_cookie_box\": 14, \"T4_in_top_drawer\": 30, \"T5_on_ramekin\": 28, \"T6_next_to_cookie\": 32, \"T7_on_stove\": 64, \"T8_next_to_plate\": 82, \"T9_on_wooden_cab\": 38}, \"success_rate\": 49.6, \"total_episodes\": 500}, \"status\": \"DONE\"}, \"eval_pi05_random_k09_fixedmask_object_seed42_v2\": {\"conclusion\": \"negative\", \"metrics\": {\"per_task_sr\": [0.12, 0.26, 0.16, 0.14, 0.12, 0.24, 0.18, 0.14, 0.24, 0.1], \"success_rate\": 0.17, \"successes\": 85, \"total_episodes\": 500}, \"status\": \"DONE\"}, \"train_smart_compress_m16_seed44_v3\": {\"conclusion\": \"success\", \"metrics\": {\"eval_action_loss\": 0.0495, \"total_steps\": 99999, \"train_action_loss\": 0.0677, \"train_grad_norm\": 1.88821}, \"status\": \"DONE\"}, \"train_smart_compress_m16_seed43\": {\"conclusion\": \"success\", \"metrics\": {\"eval_action_loss\": 0.06236, \"total_steps\": 99999, \"train_action_loss\": 0.07652, \"train_grad_norm\": 0.97135}, \"status\": \"DONE\"}, \"train_smart_compress_m128_seed43\": {\"conclusion\": \"success\", \"metrics\": {\"eval_action_loss\": 0.06125, \"total_steps\": 99999, \"train_action_loss\": 0.05584, \"train_grad_norm\": 0.95519}, \"status\": \"DONE\"}, \"train_smart_compress_m96_seed44\": {\"conclusion\": \"success\", \"metrics\": {\"eval_action_loss\": 0.05259, \"total_steps\": 99999, \"train_action_loss\": 0.04668, \"train_grad_norm\": 0.97222}, \"status\": \"DONE\"}, \"train_smart_compress_m32_seed44\": {\"conclusion\": \"success\", \"metrics\": {\"eval_action_loss\": 0.0635, \"total_steps\": 99999, \"train_action_loss\": 0.04146, \"train_grad_norm\": 0.57272}, \"status\": \"DONE\"}, \"train_smart_compress_m64_seed44\": {\"conclusion\": \"success\", \"metrics\": {\"eval_action_loss\": 0.06994, \"total_steps\": 99999, \"train_action_loss\": 0.031, \"train_grad_norm\": 1.08378}, \"status\": \"DONE\"}, \"train_smart_compress_m128_resume\": {\"conclusion\": \"success\", \"metrics\": {\"eval_action_loss\": 0.05743, \"resumed_from_step\": 32001, \"total_steps\": 99999, \"train_action_loss\": 0.05412, \"train_grad_norm\": 0.92663}, \"status\": \"DONE\"}, \"eval_pi05_random_k07_spatial_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"per_task_sr\": {\"T0_between_plate\": 90, \"T1_next_to_ramekin\": 96, \"T2_table_center\": 94, \"T3_on_cookie_box\": 52, \"T4_in_top_drawer\": 60, \"T5_on_ramekin\": 42, \"T6_next_to_cookie\": 58, \"T7_on_stove\": 76, \"T8_next_to_plate\": 80, \"T9_on_wooden_cab\": 96}, \"success_rate\": 74.4, \"total_episodes\": 500}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k03_object_seed43\": {\"conclusion\": \"success\", \"metrics\": {\"SR\": 0.554, \"elapsed_min\": 85.15, \"per_task\": {\"alphabet_soup\": 0.16, \"bbq_sauce\": 0.54, \"butter\": 0.52, \"chocolate_pudding\": 0.92, \"cream_cheese\": 0.56, \"ketchup\": 0.4, \"milk\": 0.14, \"orange_juice\": 0.54, \"salad_dressing\": 0.9, \"tomato_sauce\": 0.86}, \"total_episodes\": 500, \"total_successes\": 277}, \"status\": \"DONE\"}, \"eval_openvla_l2norm_k09_object_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"elapsed_minutes\": 228.5, \"overall_sr\": 0.706, \"per_task_sr\": {\"alphabet_soup\": 0.66, \"bbq_sauce\": 0.48, \"butter\": 0.74, \"chocolate_pudding\": 0.78, \"cream_cheese\": 0.58, \"ketchup\": 0.9, \"milk\": 0.74, \"orange_juice\": 0.88, \"salad_dressing\": 0.66, \"tomato_sauce\": 0.64}, \"total_episodes\": 500, \"total_successes\": 353}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k05_object_seed43\": {\"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.336, \"per_task_sr\": {\"alphabet_soup\": 0.44, \"bbq_sauce\": 0.04, \"butter\": 0.32, \"chocolate_pudding\": 0.46, \"cream_cheese\": 0.08, \"ketchup\": 0.6, \"milk\": 0.52, \"orange_juice\": 0.52, \"salad_dressing\": 0, \"tomato_sauce\": 0.38}, \"total_episodes\": 500, \"total_successes\": 168}, \"status\": \"DONE\"}, \"eval_smolvla_official_random_k050_object_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0, \"per_task_sr\": {\"task0\": 0, \"task1\": 0, \"task2\": 0, \"task3\": 0, \"task4\": 0, \"task5\": 0, \"task6\": 0, \"task7\": 0, \"task8\": 0, \"task9\": 0}, \"total_episodes\": 500, \"total_successes\": 0, \"wilson_ci_95\": [0, 0.0076]}, \"status\": \"DONE\"}, \"eval_smolvla_official_random_k090_object_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0, \"per_task_sr\": {\"task0\": 0, \"task1\": 0, \"task2\": 0, \"task3\": 0, \"task4\": 0, \"task5\": 0, \"task6\": 0, \"task7\": 0, \"task8\": 0, \"task9\": 0}, \"total_episodes\": 500, \"total_successes\": 0, \"wilson_ci_95\": [0, 0.0076]}, \"status\": \"DONE\"}, \"eval_smolvla_official_l2norm_k030_object_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0, \"per_task_sr\": {\"task0\": 0, \"task1\": 0, \"task2\": 0, \"task3\": 0, \"task4\": 0, \"task5\": 0, \"task6\": 0, \"task7\": 0, \"task8\": 0, \"task9\": 0}, \"total_episodes\": 500, \"total_successes\": 0, \"wilson_ci_95\": [0, 0.0076]}, \"status\": \"DONE\"}, \"eval_smolvla_official_random_k070_object_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0, \"per_task_sr\": {\"task0\": 0, \"task1\": 0, \"task2\": 0, \"task3\": 0, \"task4\": 0, \"task5\": 0, \"task6\": 0, \"task7\": 0, \"task8\": 0, \"task9\": 0}, \"total_episodes\": 500, \"total_successes\": 0, \"wilson_ci_95\": [0, 0.0076]}, \"status\": \"DONE\"}, \"eval_smolvla_official_random_k030_object_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0, \"per_task_sr\": {\"task0\": 0, \"task1\": 0, \"task2\": 0, \"task3\": 0, \"task4\": 0, \"task5\": 0, \"task6\": 0, \"task7\": 0, \"task8\": 0, \"task9\": 0}, \"total_episodes\": 500, \"total_successes\": 0, \"wilson_ci_95\": [0, 0.0076]}, \"status\": \"DONE\"}, \"eval_smolvla_official_l2norm_k050_object_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"seed\": 42, \"success_rate\": 0, \"total_episodes\": 500}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k05_spatial_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"comparison\": {\"vs_baseline_spatial\": \"55.6 vs 97.2 (-41.6pp)\", \"vs_l2norm_k05_object\": \"55.6 vs 33.4 (+22.2pp)\", \"vs_random_k05_spatial\": \"55.6 vs 71.6 (-16.0pp)\"}, \"elapsed_min\": 108.9, \"overall_sr\": 55.6, \"per_task_sr\": {\"T0_pick_up_black_bowl_between_plate\": 74, \"T1_pick_up_black_bowl_next_to_ramekin\": 82, \"T2_pick_up_black_bowl_on_plate\": 78, \"T3_pick_up_black_bowl_on_cookie_box\": 28, \"T4_pick_up_black_bowl_in_top_drawer\": 38, \"T5_pick_up_black_bowl_on_ramekin\": 44, \"T6_pick_up_black_bowl_next_to_cookie\": 32, \"T7_pick_up_black_bowl_on_stove\": 74, \"T8_pick_up_black_bowl_next_to_plate\": 62, \"T9_pick_up_black_bowl_on_wooden_cab\": 44}, \"total_episodes\": 500, \"total_successes\": 278}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k03_spatial_seed42\": {\"conclusion\": \"negative\", \"metrics\": {\"checkpoint_path\": \"/root/autodl-tmp/pi05_libero_finetuned\", \"elapsed_min\": 108.4, \"log_path\": \"~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k03_spatial_seed42.log\", \"overall_sr\": 57.2, \"per_task_sr\": {\"T0_bowl_between_plate\": 62, \"T1_bowl_next_to_ramekin\": 72, \"T2_bowl_from_table_center\": 78, \"T3_bowl_on_cookie_box\": 24, \"T4_bowl_in_top_drawer\": 34, \"T5_bowl_on_ramekin\": 26, \"T6_bowl_next_to_cookie\": 74, \"T7_bowl_on_stove\": 90, \"T8_bowl_next_to_plate\": 66, \"T9_bowl_on_wooden_cabinet\": 46}, \"result_json\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_l2norm_k0.30_libero_spatial_seed42.json\", \"seed\": 42, \"total_episodes\": 500, \"total_successes\": 286}, \"status\": \"DONE\"}, \"eval_pi05_random_k085_object_seed42\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"eval_pi05_random_k09_fixedmask_object_seed42\": {\"conclusion\": \"failed\", \"metrics\": {\"error\": \"Network unreachable - AutoTokenizer.from_pretrained('google/paligemma-3b-pt-224') failed because AutoDL network was not enabled (source /etc/network_turbo not run). No episodes executed.\", \"overall_sr\": null, \"total_episodes\": 0}, \"status\": \"DONE\"}, \"eval_pi05_random_k095_object_seed42\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"eval_pi05_l2norm_k01_object_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"elapsed_min\": 117.55, \"overall_sr\": 0.026, \"per_task_sr\": {\"T0_alphabet_soup\": 0.02, \"T1_cream_cheese\": 0.06, \"T2_salad_dressing\": 0.04, \"T3_bbq_sauce\": 0.02, \"T4_ketchup\": 0.04, \"T5_tomato_sauce\": 0.02, \"T6_butter\": 0, \"T7_milk\": 0, \"T8_chocolate_pudding\": 0.02, \"T9_orange_juice\": 0.04}, \"total_episodes\": 500, \"total_successes\": 13}, \"status\": \"DONE\"}, \"eval_smolvla_official_random_k050_object_seed43\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"eval_smolvla_official_l2norm_k095_object_seed43\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"eval_smolvla_official_random_k095_object_seed43\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"eval_smolvla_official_baseline_object_seed43\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"eval_smolvla_official_l2norm_k095_object_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"seed\": 42, \"success_rate\": 0.4, \"total_episodes\": 500}, \"status\": \"DONE\"}, \"eval_smolvla_official_random_k095_object_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"seed\": 42, \"success_rate\": 0, \"total_episodes\": 500}, \"status\": \"DONE\"}, \"eval_smolvla_official_baseline_object_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"note\": \"Official checkpoint, paper reports ~87% - significant gap\", \"seed\": 42, \"success_rate\": 57.2, \"total_episodes\": 500}, \"status\": \"DONE\"}, \"eval_openvla_l2norm_k05_object_seed43\": {\"conclusion\": \"success\", \"metrics\": {\"seed\": 43, \"success_rate\": 39.2, \"total_episodes\": 500}, \"status\": \"DONE\"}, \"train_openvla_sc_m64_seed42_v5\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"eval_pi05_l2norm_k09_object_seed42_v2\": {\"conclusion\": \"success\", \"metrics\": {\"seed\": 42, \"success_rate\": 98.2, \"total_episodes\": 500, \"total_successes\": 491}, \"status\": \"DONE\"}, \"eval_openvla_l2norm_k03_object_seed43\": {\"conclusion\": \"success\", \"metrics\": {\"num_episodes\": 500, \"per_task\": {\"alphabet_soup\": 42, \"bbq_sauce\": 10, \"butter\": 8, \"chocolate_pudding\": 28, \"cream_cheese\": 6, \"ketchup\": 66, \"milk\": 36, \"orange_juice\": 26, \"salad_dressing\": 28, \"tomato_sauce\": 0}, \"success_rate\": 25}, \"status\": \"DONE\"}, \"eval_openvla_random_k07_object_seed43\": {\"conclusion\": \"success\", \"metrics\": {\"elapsed_min\": 272.6, \"overall_sr\": 0.526, \"per_task\": {\"alphabet_soup\": 0.84, \"bbq_sauce\": 0.42, \"butter\": 0.1, \"chocolate_pudding\": 0.36, \"cream_cheese\": 0.2, \"ketchup\": 0.7, \"milk\": 0.6, \"orange_juice\": 0.84, \"salad_dressing\": 0.66, \"tomato_sauce\": 0.54}, \"total_episodes\": 500, \"total_successes\": 263}, \"status\": \"DONE\"}, \"eval_openvla_baseline_object_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"num_episodes\": 500, \"source\": \"log extraction - full eval completed but results/ dir missing caused save failure\", \"success_rate\": 74}, \"status\": \"DONE\"}, \"eval_xvla_l2norm_k03_object_seed44\": {\"conclusion\": \"success\", \"metrics\": {}, \"status\": \"DONE\"}, \"eval_xvla_random_k07_object_seed42_v2\": {\"conclusion\": \"success\", \"metrics\": {\"num_episodes\": 500, \"success_rate\": 65.2}, \"status\": \"DONE\"}, \"eval_xvla_random_k085_object_seed43\": {\"conclusion\": \"success\", \"metrics\": {\"num_episodes\": 500, \"success_rate\": 63.2}, \"status\": \"DONE\"}, \"eval_xvla_random_k085_object_seed42_v2\": {\"conclusion\": \"success\", \"metrics\": {\"num_episodes\": 500, \"success_rate\": 63.6}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k07_object_seed43\": {\"conclusion\": \"success\", \"metrics\": {\"elapsed_min\": 100.3, \"success_rate\": 56.4, \"total_episodes\": 500, \"total_successes\": 282}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k07_object_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"elapsed_min\": 91.7, \"success_rate\": 55, \"total_episodes\": 500, \"total_successes\": 275}, \"status\": \"DONE\"}, \"eval_xvla_l2norm_k03_object_seed42_v2\": {\"conclusion\": \"killed\", \"status\": \"DONE\"}, \"eval_xvla_l2norm_k085_object_seed43\": {\"conclusion\": \"killed\", \"status\": \"DONE\"}, \"eval_xvla_l2norm_k03_object_seed43\": {\"conclusion\": \"success\", \"metrics\": {\"SR\": 0.21}, \"status\": \"DONE\"}, \"eval_xvla_random_k03_object_seed43\": {\"conclusion\": \"success\", \"metrics\": {\"SR\": 0.662}, \"status\": \"DONE\"}, \"eval_xvla_random_k07_object_seed44\": {\"conclusion\": \"success\", \"metrics\": {\"SR\": 0.65}, \"status\": \"DONE\"}, \"eval_xvla_l2norm_k07_object_seed43\": {\"conclusion\": \"success\", \"metrics\": {\"SR\": 0.59}, \"status\": \"DONE\"}, \"eval_xvla_random_k03_object_seed44\": {\"conclusion\": \"success\", \"metrics\": {\"SR\": 0.63, \"per_task\": [0.74, 0.42, 0.96, 0.8, 0.88, 0.84, 0, 0.74, 0, 0.92]}, \"status\": \"DONE\"}, \"eval_xvla_l2norm_k07_object_seed44\": {\"conclusion\": \"success\", \"metrics\": {\"SR\": 0.564, \"per_task\": [0.96, 0, 1, 0.8, 0.26, 0.9, 0.12, 0.7, 0.02, 0.88]}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k07_object_seed43_v2\": {\"conclusion\": \"success\", \"metrics\": {\"SR\": 0.578, \"elapsed_min\": 91.34, \"per_task\": {\"alphabet_soup\": 0.46, \"bbq_sauce\": 0.8, \"butter\": 0.3, \"chocolate_pudding\": 0.7, \"cream_cheese\": 0.96, \"ketchup\": 0.26, \"milk\": 0.04, \"orange_juice\": 0.46, \"salad_dressing\": 0.8, \"tomato_sauce\": 1}, \"total_episodes\": 500, \"total_successes\": 289}, \"status\": \"DONE\"}, \"eval_openvla_l2norm_k03_object_seed42_rerun\": {\"conclusion\": \"success\", \"metrics\": {\"SR\": 0.25, \"elapsed_minutes\": 299.2, \"per_task\": {\"alphabet_soup\": 0.42, \"bbq_sauce\": 0.1, \"butter\": 0.08, \"chocolate_pudding\": 0.28, \"cream_cheese\": 0.06, \"ketchup\": 0.66, \"milk\": 0.36, \"orange_juice\": 0.26, \"salad_dressing\": 0.28, \"tomato_sauce\": 0}, \"total_episodes\": 500, \"total_successes\": 125, \"vision_tokens\": \"256->76\"}, \"status\": \"DONE\"}, \"eval_openvla_random_k03_object_seed42_v2\": {\"conclusion\": \"success\", \"metrics\": {\"elapsed_min\": 304.1, \"overall_SR\": 0.214, \"per_task\": {\"alphabet_soup\": 0.14, \"bbq_sauce\": 0.3, \"butter\": 0.02, \"chocolate_pudding\": 0.16, \"cream_cheese\": 0, \"ketchup\": 0.26, \"milk\": 0.14, \"orange_juice\": 0.56, \"salad_dressing\": 0.56, \"tomato_sauce\": 0}, \"seed\": 42}, \"status\": \"DONE\"}, \"eval_openvla_l2norm_k05_object_seed42_v3\": {\"conclusion\": \"killed\", \"status\": \"DONE\"}, \"eval_openvla_l2norm_k07_object_seed42_v2\": {\"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.498, \"total_episodes\": 500, \"total_successes\": 249}, \"status\": \"DONE\"}, \"eval_pi05_random_k07_object_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"elapsed_min\": 83.1, \"overall_sr\": 0.772, \"total_episodes\": 500, \"total_successes\": 386}, \"status\": \"DONE\"}, \"eval_xvla_l2norm_k03_object_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"notes\": \"3 tasks at 0% SR (catastrophic). vs random k=0.3=62.8% → gap +40.6pp confirms D132.\", \"per_task\": [26, 0, 32, 40, 18, 46, 0, 24, 0, 36], \"success_rate\": 0.222, \"total_episodes\": 500, \"total_successes\": 111, \"wilson_ci_95\": [0.188, 0.26]}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k03_object_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"notes\": \"D140: L2norm reversal at k=0.3 - L2norm > random for pi0.5\", \"success_rate\": 0.51, \"total_episodes\": 500, \"total_successes\": 255}, \"status\": \"DONE\"}, \"eval_pi05_random_k03_object_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.364, \"total_episodes\": 500, \"total_successes\": 182}, \"status\": \"DONE\"}, \"eval_xvla_random_k05_object_seed44\": {\"conclusion\": \"success\", \"metrics\": {\"notes\": \"3rd seed confirms D132: random k=0.5 seed42=70.6%, seed43=71.0%, seed44=69.2%\", \"success_rate\": 0.692, \"total_episodes\": 500, \"total_successes\": 346}, \"status\": \"DONE\"}, \"eval_pi05_random_k05_object_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"comparison\": {\"baseline_sr\": 0.982, \"l2norm_k05_sr\": 0.334, \"random_vs_l2norm_gap\": \"+36.0pp\", \"retention_rate\": \"70.7%\"}, \"elapsed_min\": 94.9, \"overall_sr\": 0.694, \"per_task_sr\": {\"alphabet_soup\": 0.92, \"bbq_sauce\": 0.6, \"butter\": 0.88, \"chocolate_pudding\": 0.78, \"cream_cheese\": 0.78, \"ketchup\": 0.6, \"milk\": 0.54, \"orange_juice\": 0.58, \"salad_dressing\": 0.68, \"tomato_sauce\": 0.58}, \"total_episodes\": 500, \"total_successes\": 347}, \"status\": \"DONE\"}, \"eval_xvla_l2norm_k07_object_seed42_v2\": {\"conclusion\": \"success\", \"metrics\": {\"notes\": \"Reviewer confirmed. westd-38929=56.2% vs cqa1=58.2%, 2pp diff acceptable.\", \"per_task\": [96, 2, 100, 78, 34, 90, 18, 0, 70, 94], \"success_rate\": 0.582, \"total_episodes\": 500, \"total_successes\": 291}, \"status\": \"DONE\"}, \"train_openvla_sc_m64_seed42_v4\": {\"conclusion\": \"failed\", \"metrics\": {\"note\": \"Previous run crashed at 50K. Current run restarted from 0.\", \"steps_completed\": \"from_step_0_restart\", \"steps_total\": 100000}, \"status\": \"DONE\"}, \"eval_xvla_random_k07_object_seed43_v2\": {\"conclusion\": \"success\", \"metrics\": {\"success_rate\": 0.65, \"total_episodes\": 500, \"total_successes\": 325, \"wilson_ci_95\": [0.6072, 0.6905]}, \"status\": \"DONE\"}, \"eval_openvla_sc_m128_object_seed42_v2\": {\"conclusion\": \"failed\", \"metrics\": {\"failure_reason\": \"7/7 episodes FAIL (280-step timeout), model output invalid after LoRA merge. Killed by Director.\"}, \"status\": \"DONE\"}, \"eval_openvla_random_k07_object_seed42\": {\"conclusion\": \"failed\", \"metrics\": {\"failure_reason\": \"Process never started — empty log, command failure on westd-38929\"}, \"status\": \"DONE\"}, \"eval_pi05_l2norm_k05_object_seed42\": {\"conclusion\": \"negative\", \"metrics\": {\"elapsed_minutes\": 95.6, \"keep_ratio\": 0.5, \"num_episodes\": 500, \"per_task\": {\"alphabet_soup\": 0.5, \"bbq_sauce\": 0.0, \"butter\": 0.28, \"chocolate_pudding\": 0.38, \"cream_cheese\": 0.14, \"ketchup\": 0.54, \"milk\": 0.64, \"orange_juice\": 0.48, \"salad_dressing\": 0.0, \"tomato_sauce\": 0.38}, \"seed\": 42, \"success_rate\": 33.4, \"total_successes\": 167}, \"status\": \"DONE\"}, \"eval_xvla_random_k07_object_seed43\": {\"conclusion\": \"failed\", \"metrics\": {}, \"status\": \"DONE\"}, \"eval_openvla_l2norm_k03_object_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"failure_reason\": \"AutoDL container restart at 14:50:19 UTC killed process. Was at Task 4/10 (~40%). GPU count dropped from 4 to 1 after restart.\", \"k_ratio\": 0.3, \"note\": \"Prior complete result found on disk after container crash. Current run crashed at Task 4/10.\", \"success_rate\": 25.0}, \"status\": \"DONE\"}, \"eval_openvla_l2norm_k05_object_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"failure_reason\": \"AutoDL container restart at 14:50:19 UTC killed process. Was at Task 4/10 (~40%). GPU count dropped from 4 to 1 after restart.\", \"k_ratio\": 0.5, \"note\": \"Prior complete result found on disk after container crash. Current run crashed at Task 4/10.\", \"success_rate\": 39.2}, \"status\": \"DONE\"}, \"eval_openvla_random_k03_object_seed42\": {\"conclusion\": \"failed\", \"metrics\": {\"failure_reason\": \"AutoDL container restart at 14:50:19 UTC killed process. Was at Task 4/10 (~40%). GPU count dropped from 4 to 1 after restart.\"}, \"status\": \"DONE\"}, \"eval_xvla_random_k03_object_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"keep_ratio\": 0.3, \"success_rate\": 62.8}, \"status\": \"DONE\"}, \"eval_xvla_random_k07_object_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"duration_min\": 77.3, \"num_episodes\": 500, \"per_task\": [0.98, 0.0, 1.0, 0.94, 0.62, 0.96, 0.1, 0.92, 0.0, 1.0], \"success_rate\": 65.2, \"wilson_ci_95\": [0.609, 0.692]}, \"status\": \"DONE\"}, \"eval_openvla_sc_m128_object_seed42\": {\"conclusion\": \"failed\", \"metrics\": {\"all_fail\": true, \"num_episodes_completed\": 16, \"success_rate\": 0.0}, \"status\": \"DONE\"}, \"eval_openvla_prune_random_k05_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"duration_min\": 291, \"num_episodes\": 500, \"per_task\": [0.56, 0.02, 0.4, 0.58, 0.6, 0.26, 0.0, 0.12, 0.3, 0.74], \"seed\": 42, \"success_rate\": 35.8, \"wilson_ci_95\": [0.317, 0.401]}, \"status\": \"DONE\"}, \"eval_openvla_prune_random_k07_seed42_v2\": {\"conclusion\": \"success\", \"metrics\": {\"num_episodes\": 500, \"seed\": 42, \"success_rate\": 44.4}, \"status\": \"DONE\"}, \"eval_openvla_prune_random_k095_seed42_v2\": {\"conclusion\": \"success\", \"metrics\": {\"num_episodes\": 500, \"per_task\": [0.8, 0.42, 0.7, 0.42, 0.88, 0.84, 0.6, 0.68, 0.66, 0.92], \"seed\": 42, \"success_rate\": 69.2, \"wilson_ci_95\": [0.65, 0.731]}, \"status\": \"DONE\"}, \"eval_smolvla_baseline_spatial_westd38929_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"note\": \"OffScreenRenderEnv - not comparable with LiberoEnv results\", \"num_episodes\": 500, \"per_task\": [0.24, 0.08, 0.04, 0.24, 0.0, 0.02, 0.02, 0.02, 0.14, 0.0], \"success_rate\": 8.0, \"wilson_ci_95\": [0.059, 0.107]}, \"status\": \"DONE\"}, \"eval_xvla_random_k08_object_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"num_episodes\": 500, \"per_task\": [0.96, 0.88, 1.0, 0.92, 0.94, 0.96, 0.5, 0.94, 0.84, 1.0], \"success_rate\": 89.4, \"wilson_ci_95\": [0.864, 0.918]}, \"status\": \"DONE\"}, \"eval_xvla_random_k09_object_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"duration_min\": 50.4, \"num_episodes\": 500, \"per_task\": [0.96, 1.0, 1.0, 0.94, 1.0, 0.94, 1.0, 0.98, 0.96, 1.0], \"success_rate\": 97.8, \"wilson_ci_95\": [0.961, 0.988]}, \"status\": \"DONE\"}, \"eval_xvla_spatial_k085_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"num_episodes\": 500, \"success_rate\": 66.6}, \"status\": \"DONE\"}, \"eval_openvla_prune_l2norm_k07_seed43_v2\": {\"conclusion\": \"success\", \"metrics\": {\"num_episodes\": 500, \"success_rate\": 49.8, \"wilson_ci_95\": [0.455, 0.541]}, \"status\": \"DONE\"}, \"eval_oft_baseline_object_seed42\": {\"conclusion\": \"killed\", \"status\": \"DONE\"}, \"train_openvla_sc_m64_seed42_v3\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"eval_openvla_baseline_spatial_seed42_v2\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"eval_xvla_goal_k05_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"num_episodes\": 500, \"per_task\": [0.82, 0.98, 1.0, 0.4, 1.0, 0.0, 0.24, 0.74, 0.92, 0.0], \"seed\": 42, \"success_rate\": 0.61, \"suite\": \"libero_goal\", \"wilson_ci_95\": [0.567, 0.652]}, \"status\": \"DONE\"}, \"eval_xvla_goal_k09_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"num_episodes\": 500, \"per_task\": [1.0, 0.82, 0.96, 0.06, 0.96, 0.0, 0.78, 1.0, 0.46, 0.98], \"seed\": 42, \"success_rate\": 0.702, \"suite\": \"libero_goal\", \"wilson_ci_95\": [0.66, 0.74]}, \"status\": \"DONE\"}, \"eval_xvla_spatial_k09_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"num_episodes\": 500, \"success_rate\": 0.79, \"wilson_ci_95\": [0.752, 0.823]}, \"status\": \"DONE\"}, \"eval_openvla_sc_m128_spatial_seed42\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"eval_openvla_prune_random_k03_seed43\": {\"conclusion\": \"killed\", \"status\": \"DONE\"}, \"eval_openvla_prune_random_k07_seed42\": {\"conclusion\": \"killed\", \"status\": \"DONE\"}, \"eval_openvla_prune_random_k095_seed42\": {\"conclusion\": \"killed\", \"status\": \"DONE\"}, \"eval_openvla_prune_l2norm_k09_seed43\": {\"conclusion\": \"killed\", \"status\": \"DONE\"}, \"eval_xvla_spatial_k05_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"num_episodes\": 500, \"per_task\": [0.94, 0.22, 0.9, 0.74, 0.88, 0.0, 0.78, 0.3, 0.74, 0.38], \"success_rate\": 0.588, \"wilson_ci_95\": [0.544, 0.63]}, \"status\": \"DONE\"}, \"eval_xvla_prune_k085_seed44\": {\"conclusion\": \"success\", \"metrics\": {\"num_episodes\": 500, \"success_rate\": 0.682, \"wilson_ci_95\": [0.64, 0.721]}, \"status\": \"DONE\"}, \"eval_xvla_prune_k08_seed44\": {\"conclusion\": \"success\", \"metrics\": {\"num_episodes\": 500, \"success_rate\": 0.898, \"total_successes\": 449, \"wilson_ci_95\": [0.868, 0.922]}, \"status\": \"DONE\"}, \"eval_openvla_prune_random_k095_seed43\": {\"conclusion\": \"success\", \"metrics\": {\"elapsed_minutes\": 249.43, \"k_ratio\": 0.95, \"mode\": \"random_prune\", \"num_episodes\": 500, \"seed\": 43, \"success_rate\": 0.668, \"total_successes\": 334, \"wilson_ci_95\": [0.626, 0.708]}, \"status\": \"DONE\"}, \"eval_openvla_prune_l2norm_k07_seed43\": {\"conclusion\": \"failed\", \"metrics\": {\"elapsed_minutes\": 237.8, \"num_episodes\": 500, \"per_task\": {\"alphabet_soup\": 0.78, \"bbq_sauce\": 0.46, \"butter\": 0.58, \"chocolate_pudding\": 0.68, \"cream_cheese\": 0.8, \"ketchup\": 0.96, \"milk\": 0.72, \"orange_juice\": 0.82, \"salad_dressing\": 0.82, \"tomato_sauce\": 0.78}, \"seed\": 43, \"success_rate\": 0.74, \"total_successes\": 370, \"wilson_ci_95\": [0.7, 0.777]}, \"status\": \"DONE\"}, \"eval_xvla_prune_k08_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"keep_ratio\": 0.8, \"n_vision_tokens_kept\": 40, \"n_vision_tokens_original\": 50, \"num_episodes\": 500, \"success_rate\": 0.888, \"wilson_ci_95\": [0.8573, 0.9127]}, \"status\": \"DONE\"}, \"eval_xvla_prune_k085_seed43\": {\"conclusion\": \"success\", \"metrics\": {\"keep_ratio\": 0.85, \"n_vision_tokens_kept\": 42, \"n_vision_tokens_original\": 50, \"num_episodes\": 500, \"success_rate\": 0.676, \"wilson_ci_95\": [0.6338, 0.7155]}, \"status\": \"DONE\"}, \"eval_xvla_prune_k085_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"num_episodes\": 500, \"success_rate\": 0.68, \"wilson_ci_95\": [0.638, 0.719]}, \"status\": \"DONE\"}, \"eval_xvla_prune_k08_seed43\": {\"conclusion\": \"success\", \"metrics\": {\"num_episodes\": 500, \"success_rate\": 0.884, \"wilson_ci_95\": [0.853, 0.909]}, \"status\": \"DONE\"}, \"eval_xvla_prune_k01_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"num_episodes\": 500, \"success_rate\": 0, \"wilson_ci_95\": [0, 0.008]}, \"status\": \"DONE\"}, \"eval_xvla_prune_k095_seed43\": {\"conclusion\": \"success\", \"metrics\": {\"num_episodes\": 500, \"success_rate\": 0.99, \"wilson_ci_95\": [0.9768, 0.9957]}, \"status\": \"DONE\"}, \"eval_xvla_prune_k095_seed44\": {\"conclusion\": \"success\", \"metrics\": {\"num_episodes\": 500, \"success_rate\": 0.994, \"wilson_ci_95\": [0.983, 0.998]}, \"status\": \"DONE\"}, \"eval_xvla_prune_k095_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"num_episodes\": 500, \"success_rate\": 0.99, \"wilson_ci_95\": [0.977, 0.996]}, \"status\": \"DONE\"}, \"eval_xvla_prune_k01_seed44\": {\"conclusion\": \"success\", \"metrics\": {\"num_episodes\": 500, \"success_rate\": 0, \"wilson_ci_95\": [0, 0.008]}, \"status\": \"DONE\"}, \"eval_xvla_prune_k01_seed43\": {\"conclusion\": \"success\", \"metrics\": {\"num_episodes\": 500, \"success_rate\": 0, \"wilson_ci_95\": [0, 0.0076]}, \"status\": \"DONE\"}, \"eval_openvla_prune_random_k09_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"num_episodes\": 500, \"success_rate\": 0.646, \"total_successes\": 323, \"wilson_ci_95\": [0.604, 0.686]}, \"status\": \"DONE\"}, \"eval_openvla_prune_random_k09_seed43\": {\"conclusion\": \"success\", \"metrics\": {\"num_episodes\": 500, \"success_rate\": 0.622}, \"status\": \"DONE\"}, \"eval_openvla_prune_random_k05_seed43_v2\": {\"conclusion\": \"success\", \"metrics\": {\"num_episodes\": 500, \"success_rate\": 0.356}, \"status\": \"DONE\"}, \"eval_xvla_prune_k02_seed44\": {\"conclusion\": \"success\", \"metrics\": {\"num_episodes\": 500, \"success_rate\": 0.04}, \"status\": \"DONE\"}, \"eval_xvla_prune_k02_seed43\": {\"conclusion\": \"success\", \"metrics\": {\"num_episodes\": 500, \"success_rate\": 0.048}, \"status\": \"DONE\"}, \"eval_openvla_prune_l2norm_k09\": {\"conclusion\": \"success\", \"metrics\": {\"num_episodes\": 500, \"success_rate\": 0.706}, \"status\": \"DONE\"}, \"eval_openvla_prune_random_k07_seed43_v2\": {\"conclusion\": \"success\", \"metrics\": {\"num_episodes\": 500, \"success_rate\": 0.526}, \"status\": \"DONE\"}, \"eval_openvla_prune_l2norm_k095\": {\"conclusion\": \"success\", \"metrics\": {\"num_episodes\": 500, \"success_rate\": 0.706}, \"status\": \"DONE\"}, \"eval_openvla_prune_l2norm_k03\": {\"conclusion\": \"success\", \"metrics\": {\"num_episodes\": 500, \"success_rate\": 0.25}, \"status\": \"DONE\"}, \"eval_openvla_prune_l2norm_k05\": {\"conclusion\": \"success\", \"metrics\": {\"num_episodes\": 500, \"success_rate\": 0.392}, \"status\": \"DONE\"}, \"eval_xvla_prune_k03_seed43\": {\"conclusion\": \"success\", \"metrics\": {\"num_episodes\": 500, \"success_rate\": 0.21}, \"status\": \"DONE\"}, \"eval_xvla_prune_k03_seed44\": {\"conclusion\": \"success\", \"metrics\": {\"num_episodes\": 500, \"success_rate\": 0.228}, \"status\": \"DONE\"}, \"eval_xvla_prune_k05_seed44\": {\"conclusion\": \"success\", \"metrics\": {\"num_episodes\": 500, \"success_rate\": 0.444}, \"status\": \"DONE\"}, \"eval_xvla_prune_k07_seed44\": {\"conclusion\": \"success\", \"metrics\": {\"episodes\": 500, \"success_rate\": 0.564}, \"status\": \"DONE\"}, \"eval_xvla_prune_k09_seed44\": {\"conclusion\": \"success\", \"metrics\": {\"episodes\": 500, \"success_rate\": 0.982}, \"status\": \"DONE\"}, \"eval_openvla_prune_random_k05_seed43\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"eval_openvla_prune_random_k07_seed43\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"eval_oft_baseline_k10\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"eval_openvla_sc_m128_20k_seed42\": {\"conclusion\": \"negative\", \"metrics\": {\"episodes_completed\": 44, \"episodes_total\": 50, \"note\": \"0/44 episodes succeeded on Task 0. All episodes timeout at 280 steps. Overfitting confirmed.\", \"seed\": 42, \"suite\": \"libero_object\", \"task_0_sr\": 0}, \"status\": \"DONE\"}, \"eval_smart_compress_m16_seed44\": {\"conclusion\": \"success\", \"metrics\": {\"n_episodes\": 500, \"n_queries\": 16, \"overall_sr\": 0.565, \"per_task_sr\": {\"task_0_alphabet_soup\": 0.38, \"task_1_cream_cheese\": 0.7, \"task_2_salad_dressing\": 0.55, \"task_3_bbq_sauce\": 0.42, \"task_4_ketchup\": 0.65, \"task_5_tomato_sauce\": 0.33, \"task_6_butter\": 0.73, \"task_7_milk\": 0.64, \"task_8_chocolate_pudding\": 0.87, \"task_9_orange_juice\": 0.38}, \"seed\": 44, \"suite\": \"libero_object\"}, \"status\": \"DONE\"}, \"eval_smart_compress_m16_seed43\": {\"conclusion\": \"success\", \"metrics\": {\"n_queries\": 16, \"overall_sr\": 0.584, \"per_task_sr\": {\"task_0_alphabet_soup\": 0.428, \"task_1_cream_cheese\": 0.474, \"task_2_salad_dressing\": 0.662, \"task_3_bbq_sauce\": 0.484, \"task_4_ketchup\": 0.742, \"task_5_tomato_sauce\": 0.4, \"task_6_butter\": 0.792, \"task_7_milk\": 0.698, \"task_8_chocolate_pudding\": 0.766, \"task_9_orange_juice\": 0.394}, \"seed\": 43, \"suite\": \"libero_object\", \"wilson_ci_95\": [0.5703, 0.5976]}, \"status\": \"DONE\"}, \"eval_smart_compress_m128_seed43\": {\"conclusion\": \"success\", \"metrics\": {\"n_queries\": 128, \"overall_sr\": 0.54, \"per_task_sr\": {\"task_0_alphabet_soup\": 0.646, \"task_1_cream_cheese\": 0.322, \"task_2_salad_dressing\": 0.614, \"task_3_bbq_sauce\": 0.432, \"task_4_ketchup\": 0.348, \"task_5_tomato_sauce\": 0.442, \"task_6_butter\": 0.716, \"task_7_milk\": 0.604, \"task_8_chocolate_pudding\": 0.818, \"task_9_orange_juice\": 0.458}, \"seed\": 43, \"suite\": \"libero_object\", \"wilson_ci_95\": [0.5262, 0.5538]}, \"status\": \"DONE\"}, \"train_openvla_sc_m128_vtconly_seed42\": {\"conclusion\": \"killed\", \"status\": \"DONE\"}, \"eval_openvla_sc_m128_vtconly_20k_seed42\": {\"conclusion\": \"killed\", \"status\": \"DONE\"}, \"train_openvla_sc_m128_seed42_v2\": {\"conclusion\": \"killed\", \"status\": \"DONE\"}, \"analysis_xvla_token_importance\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"train_openvla_sc_m96_vtconly_seed42\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"train_openvla_sc_m64_vtconly_seed42\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"train_c5_roboflamingo_v2\": {\"conclusion\": \"killed\", \"status\": \"DONE\"}, \"train_c5_roboflamingo_libero_object\": {\"conclusion\": \"killed\", \"status\": \"DONE\"}, \"train_openvla_sc_m128_lora_seed42\": {\"conclusion\": \"killed\", \"status\": \"DONE\"}, \"eval_smart_compress_m32_seed44\": {\"conclusion\": \"success\", \"metrics\": {\"ci_95_lower\": 55.2, \"ci_95_upper\": 63.8, \"n_episodes\": 500, \"seed\": 44, \"success_rate\": 59.6}, \"status\": \"DONE\"}, \"eval_smart_compress_m96_seed44\": {\"conclusion\": \"success\", \"metrics\": {\"ci_95_lower\": 48.4, \"ci_95_upper\": 57.1, \"n_episodes\": 500, \"seed\": 44, \"success_rate\": 52.8}, \"status\": \"DONE\"}, \"eval_smart_compress_m64_seed44\": {\"conclusion\": \"success\", \"metrics\": {\"ci_95_lower\": 60.1, \"ci_95_upper\": 68.5, \"n_episodes\": 500, \"seed\": 44, \"success_rate\": 64.4}, \"status\": \"DONE\"}, \"eval_openvla_random_pruning_sweep\": {\"conclusion\": \"success\", \"metrics\": {\"k0.30_sr\": 20.6, \"k0.50_sr\": 37.4, \"k0.70_sr\": 49, \"k0.90_sr\": 62, \"k0.95_sr\": 69.4, \"k1.0_sr\": 74, \"n_episodes\": 500, \"seed\": 7, \"suite\": \"libero_object\"}, \"status\": \"DONE\"}, \"train_openvla_sc_m128_seed42\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"train_smart_compress_m16_seed44_v2\": {\"conclusion\": \"failed\", \"metrics\": {\"failure_reason\": \"Disk full on /root/autodl-tmp/ (250G/250G, 100% used, 4MB free). Training ran normally to step=1000 (loss 5.0→0.2), but torch.save() failed at first checkpoint save with PytorchStreamWriter write error. Checkpoints dir already 112GB from prior experiments — needs cleanup before retry. Partial checkpoint.pt (228MB) likely corrupted.\", \"last_loss\": 0.207, \"last_step\": 1000, \"steps_per_second\": 3.8}, \"status\": \"DONE\"}, \"eval_official_smolvla_prune_k05_spatial_v2\": {\"conclusion\": \"success\", \"metrics\": {\"note\": \"cliff-edge confirmed on Spatial suite, 0.6% SR with k=0.5 random pruning\", \"overall_success_rate\": 0.006, \"total_episodes\": 500, \"total_successes\": 3}, \"status\": \"DONE\"}, \"eval_smart_compress_m96_seed44_v2\": {\"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.528, \"total_episodes\": 500, \"total_successes\": 264, \"wilson_ci_95\": [0.4842, 0.5714]}, \"status\": \"DONE\"}, \"eval_smart_compress_m64_seed44_v2\": {\"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.644, \"total_episodes\": 500, \"total_successes\": 322, \"wilson_ci_95\": [0.6011, 0.6847]}, \"status\": \"DONE\"}, \"eval_smart_compress_m32_seed44_v2\": {\"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.596, \"total_episodes\": 500, \"total_successes\": 298, \"wilson_ci_95\": [0.5524, 0.6381]}, \"status\": \"DONE\"}, \"eval_mlp_adapter_seed44\": {\"conclusion\": \"negative\", \"metrics\": {\"overall_success_rate\": 0.604, \"per_task_sr\": {\"0_alphabet_soup\": 0.54, \"1_cream_cheese\": 0.68, \"2_salad_dressing\": 0.58, \"3_bbq_sauce\": 0.5, \"4_ketchup\": 0.8, \"5_tomato_sauce\": 0.58, \"6_butter\": 0.82, \"7_milk\": 0.58, \"8_chocolate_pudding\": 0.54, \"9_orange_juice\": 0.42}, \"suite\": \"libero_object\", \"total_episodes\": 500, \"total_successes\": 302, \"wilson_ci_95\": [0.5605, 0.6459]}, \"status\": \"DONE\"}, \"eval_official_smolvla_prune_k05_spatial\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"eval_smolvla_official_baseline_spatial_v2\": {\"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.438, \"per_task_sr\": {\"task_0\": 0.54, \"task_1\": 0.48, \"task_2\": 0.08, \"task_3\": 0.76, \"task_4\": 0.38, \"task_5\": 0.2, \"task_6\": 0.34, \"task_7\": 0.78, \"task_8\": 0.48, \"task_9\": 0.34}, \"total_episodes\": 500, \"total_successes\": 219, \"wilson_ci_95\": [0.3951, 0.4818]}, \"status\": \"DONE\"}, \"eval_mlp_adapter_seed43\": {\"conclusion\": \"negative\", \"metrics\": {\"overall_success_rate\": 0.646, \"per_task_sr\": {\"task0_alphabet_soup\": 0.74, \"task1_cream_cheese\": 0.74, \"task2_salad_dressing\": 0.66, \"task3_bbq_sauce\": 0.44, \"task4_ketchup\": 0.56, \"task5_tomato_sauce\": 0.64, \"task6_butter\": 0.86, \"task7_milk\": 0.58, \"task8_chocolate_pudding\": 0.72, \"task9_orange_juice\": 0.52}, \"suite\": \"libero_object\", \"total_episodes\": 500, \"total_successes\": 323, \"wilson_ci_95\": [0.603, 0.687]}, \"status\": \"DONE\"}, \"eval_mlp_adapter_control\": {\"conclusion\": \"negative\", \"metrics\": {\"overall_success_rate\": 0.652, \"per_task_sr\": {\"task0_alphabet_soup\": 0.58, \"task1_cream_cheese\": 0.74, \"task2_salad_dressing\": 0.72, \"task3_bbq_sauce\": 0.56, \"task4_ketchup\": 0.76, \"task5_tomato_sauce\": 0.68, \"task6_butter\": 0.8, \"task7_milk\": 0.62, \"task8_chocolate_pudding\": 0.52, \"task9_orange_juice\": 0.54}, \"suite\": \"libero_object\", \"total_episodes\": 500, \"total_successes\": 326, \"wilson_ci_95\": [0.6092, 0.6925]}, \"status\": \"DONE\"}, \"eval_smolvla_prune_k05_spatial_v2\": {\"conclusion\": \"success\", \"metrics\": {\"episodes_per_task\": 50, \"k_ratio\": 0.5, \"num_tasks\": 10, \"overall_success_rate\": 0, \"per_task_sr\": {\"T0\": 0, \"T1\": 0, \"T2\": 0, \"T3\": 0, \"T4\": 0, \"T5\": 0, \"T6\": 0, \"T7\": 0, \"T8\": 0, \"T9\": 0}, \"pruning_method\": \"true_removal\", \"tokens_kept\": 64, \"tokens_removed\": 64, \"total_episodes\": 500, \"total_successes\": 0, \"wilson_ci_95\": [0, 0.0076]}, \"status\": \"DONE\"}, \"eval_smolvla_baseline_spatial\": {\"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.062, \"total_episodes\": 500, \"total_successes\": 31}, \"status\": \"DONE\"}, \"eval_smolvla_official_baseline_spatial\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"eval_smolvla_prune_k05_spatial\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"train_smart_compress_m16_seed44\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"train_mlp_adapter_control\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"eval_smart_compress_m32_spatial\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"eval_smart_compress_m128_seed44\": {\"conclusion\": \"success\", \"metrics\": {\"overall_success_rate\": 0.602, \"per_task_sr\": {\"alphabet_soup\": 0.54, \"bbq_sauce\": 0.5, \"butter\": 0.66, \"chocolate_pudding\": 0.88, \"cream_cheese\": 0.3, \"ketchup\": 0.86, \"milk\": 0.72, \"orange_juice\": 0.54, \"salad_dressing\": 0.62, \"tomato_sauce\": 0.4}, \"total_episodes\": 500, \"total_successes\": 301, \"wilson_ci_95\": [0.5585, 0.644]}, \"status\": \"DONE\"}, \"train_smart_compress_m32_official\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"train_smart_compress_m128_seed44\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"eval_openvla_prune_k095\": {\"conclusion\": \"success\", \"metrics\": {\"num_episodes\": 500, \"per_task_sr\": [76, 38, 84, 54, 84, 82, 46, 74, 64, 92], \"success_rate\": 69.4, \"suite\": \"libero_object\"}, \"status\": \"DONE\"}, \"eval_openvla_prune_k09\": {\"conclusion\": \"success\", \"metrics\": {\"num_episodes\": 500, \"per_task_sr\": [70, 28, 76, 56, 78, 70, 42, 60, 54, 86], \"success_rate\": 62, \"suite\": \"libero_object\"}, \"status\": \"DONE\"}, \"eval_smart_compress_m32_seed43\": {\"conclusion\": \"success\", \"metrics\": {\"num_episodes\": 500, \"per_task_sr\": [72, 38, 68, 36, 68, 48, 86, 44, 96, 36], \"success_rate\": 59.2, \"suite\": \"libero_object\"}, \"status\": \"DONE\"}, \"eval_smart_compress_m32_libero_spatial\": {\"conclusion\": \"success\", \"metrics\": {\"num_episodes\": 500, \"per_task_sr\": [58, 62, 52, 82, 28, 18, 82, 70, 56, 24], \"success_rate\": 53.2, \"suite\": \"libero_spatial\"}, \"status\": \"DONE\"}, \"eval_smart_compress_m64_seed43\": {\"conclusion\": \"success\", \"metrics\": {\"num_episodes\": 500, \"per_task_sr\": [58, 56, 46, 50, 48, 58, 80, 60, 86, 58], \"success_rate\": 60, \"suite\": \"libero_object\"}, \"status\": \"DONE\"}, \"eval_smart_compress_m32_libero_goal\": {\"conclusion\": \"success\", \"metrics\": {\"num_episodes\": 500, \"per_task_sr\": [60, 94, 62, 52, 32, 28, 28, 100, 78, 30], \"success_rate\": 56.4, \"suite\": \"libero_goal\"}, \"status\": \"DONE\"}, \"eval_baseline_control_prune_k05\": {\"conclusion\": \"success\", \"metrics\": {\"num_episodes\": 500, \"per_task_sr\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \"success_rate\": 0, \"suite\": \"libero_object\"}, \"status\": \"DONE\"}, \"train_smart_compress_m64_seed43\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"train_smart_compress_m32_seed43\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"eval_smart_compress_m96_seed43_v2\": {\"conclusion\": \"success\", \"metrics\": {\"num_episodes\": 500, \"per_task_sr\": [72, 66, 54, 48, 52, 40, 88, 60, 86, 16], \"success_rate\": 58.2, \"suite\": \"libero_object\", \"wilson_ci_95\": [53.8, 62.4]}, \"status\": \"DONE\"}, \"eval_smart_compress_m96_seed43\": {\"conclusion\": \"failed\", \"metrics\": {\"note\": \"INVALID — used wrong eval script (eval_success_rate_libero.py --mode baseline, no compressor loaded). Re-eval as eval_smart_compress_m96_seed43_v2.\", \"num_episodes\": 500, \"per_task_sr\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \"success_rate\": 0, \"suite\": \"libero_object\"}, \"status\": \"DONE\"}, \"train_smart_compress_m96_seed43\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"train_baseline_control_100k_v2\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"eval_baseline_control_100k_v2\": {\"conclusion\": \"success\", \"metrics\": {\"num_episodes\": 500, \"per_task_sr\": [0, 50, 74, 64, 68, 8, 58, 38, 52, 38], \"success_rate\": 45, \"suite\": \"libero_object\"}, \"status\": \"DONE\"}, \"eval_official_smolvla_prune_k095\": {\"conclusion\": \"success\", \"metrics\": {\"note\": \"Official SmolVLA checkpoint k=0.95 random pruning (true_removal, remove 5% = 7 tokens) = 0% SR. All 500 episodes timeout at 280 steps.\", \"overall_sr\": 0, \"per_task_sr\": {\"all_10_tasks\": \"0%\"}, \"total_episodes\": 500, \"total_successes\": 0}, \"status\": \"DONE\"}, \"eval_official_smolvla_prune_k09\": {\"conclusion\": \"success\", \"metrics\": {\"note\": \"Official SmolVLA checkpoint k=0.9 random pruning (true_removal, remove 10% tokens) = 0% SR. All 500 episodes timeout at 280 steps.\", \"overall_sr\": 0, \"per_task_sr\": {\"all_10_tasks\": \"0%\"}, \"total_episodes\": 500, \"total_successes\": 0}, \"status\": \"DONE\"}, \"eval_acis_k05_supplement_v2\": {\"conclusion\": \"success\", \"metrics\": {\"note\": \"Fixed eval script with offset-based ACIS hook confirms 0% SR. Previous 47.5% was due to pruning hook bug (never applied pruning).\", \"overall_SR\": \"0.0% (0/200)\", \"task6_SR\": \"0% (0/50)\", \"task7_SR\": \"0% (0/50)\", \"task8_SR\": \"0% (0/50)\", \"task9_SR\": \"0% (0/50)\", \"wilson_ci_95\": \"[0.0%, 1.9%]\"}, \"status\": \"DONE\"}, \"eval_acis_k05_supplement_200eps\": {\"conclusion\": \"failed\", \"metrics\": {\"overall_SR\": \"47.5% (95/200)\", \"task6_SR\": \"48% (24/50)\", \"task7_SR\": \"40% (20/50)\", \"task8_SR\": \"64% (32/50)\", \"task9_SR\": \"38% (19/50)\", \"wilson_ci_95\": \"[40.7%, 54.4%]\"}, \"status\": \"DONE\"}, \"eval_official_smolvla_prune_k05_v2\": {\"conclusion\": \"success\", \"metrics\": {\"note\": \"Official SmolVLA checkpoint with k=0.5 random pruning = 0% SR, confirming cliff-edge on official checkpoint (59.2% baseline → 0%)\", \"overall_sr\": 0, \"per_task_sr\": {\"all_tasks\": \"0%\"}, \"total_episodes\": 500, \"total_successes\": 0}, \"status\": \"DONE\"}, \"eval_official_smolvla_baseline\": {\"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 59.2, \"per_task_sr\": {\"task_0_alphabet_soup\": 64, \"task_1_cream_cheese\": 40, \"task_2_salad_dressing\": 44, \"task_3_bbq_sauce\": 38, \"task_4_ketchup\": 60, \"task_5_tomato_sauce\": 46, \"task_6_butter\": 78, \"task_7_milk\": 52, \"task_8_chocolate_pudding\": 90, \"task_9_orange_juice\": 80}, \"total_episodes\": 500, \"total_successes\": 296, \"wilson_ci_95\": [54.8, 63.4]}, \"status\": \"DONE\"}, \"eval_smolvla_random_prune_k095\": {\"conclusion\": \"success\", \"metrics\": {\"k_ratio\": 0.95, \"overall_SR\": 0, \"per_task_SR\": {\"T0_alphabet_soup\": 0, \"T1_cream_cheese\": 0, \"T2_salad_dressing\": 0, \"T3_bbq_sauce\": 0, \"T4_ketchup\": 0, \"T5_tomato_sauce\": 0, \"T6_butter\": 0, \"T7_milk\": 0, \"T8_chocolate_pudding\": 0, \"T9_orange_juice\": 0}, \"tokens_kept\": 121, \"tokens_removed\": 7, \"total_episodes\": 500, \"total_successes\": 0, \"wilson_ci_95\": [0, 0.0076]}, \"status\": \"DONE\"}, \"eval_official_smolvla_pruning\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"train_baseline_control_100k\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"eval_smart_compress_m128\": {\"conclusion\": \"success\", \"metrics\": {\"libero_object_sr\": 0.598, \"libero_object_sr_ci95\": [0.554, 0.64], \"per_task_sr\": {\"alphabet_soup\": 0.62, \"bbq_sauce\": 0.34, \"butter\": 0.82, \"chocolate_pudding\": 0.82, \"cream_cheese\": 0.58, \"ketchup\": 0.62, \"milk\": 0.56, \"orange_juice\": 0.58, \"salad_dressing\": 0.54, \"tomato_sauce\": 0.5}, \"total_episodes\": 500, \"total_successes\": 299}, \"status\": \"DONE\"}, \"eval_openvla_pruning_k03_restart\": {\"conclusion\": \"success\", \"metrics\": {\"elapsed_minutes\": 288.6, \"overall_sr\": 0.206, \"per_task_sr\": {\"alphabet_soup\": 0.14, \"bbq_sauce\": 0.3, \"butter\": 0, \"chocolate_pudding\": 0.1, \"cream_cheese\": 0, \"ketchup\": 0.3, \"milk\": 0.08, \"orange_juice\": 0.42, \"salad_dressing\": 0.64, \"tomato_sauce\": 0.08}, \"total_episodes\": 500, \"total_successes\": 103, \"wilson_ci_95\": [0.173, 0.244]}, \"status\": \"DONE\"}, \"smolvla_entropy_perlayer\": {\"conclusion\": \"success\", \"metrics\": {\"dataset\": \"LIBERO-Object (task 20-29)\", \"entropy_range\": [0.9311, 0.9826], \"entropy_range_width\": 0.05, \"n_images\": 260, \"n_layers\": 16, \"n_tasks\": 10, \"note\": \"Fixed: previous run sampled task 0-8 (LIBERO-90), not LIBERO-Object. Difference: 0.952 vs 0.944, conclusion unchanged.\", \"openvla_comparison\": {\"overall\": 0.639, \"range_width\": 0.5}, \"overall_entropy_ratio\": 0.9521, \"overall_entropy_std\": 0.02, \"per_layer\": {\"L0\": 0.9826, \"L1\": 0.9561, \"L10\": 0.9455, \"L11\": 0.951, \"L12\": 0.9485, \"L13\": 0.9311, \"L14\": 0.9482, \"L15\": 0.9566, \"L2\": 0.9597, \"L3\": 0.9434, \"L4\": 0.9408, \"L5\": 0.9406, \"L6\": 0.9474, \"L7\": 0.9628, \"L8\": 0.9614, \"L9\": 0.9572}}, \"status\": \"DONE\"}, \"inference_latency_comparison\": {\"conclusion\": \"success\", \"metrics\": {\"baseline_128_mean_ms\": 164.33, \"baseline_params\": 450046176, \"compressor_m32_params\": 22179840, \"m32_mean_ms\": 154.78, \"m64_mean_ms\": 156.16, \"speedup_m32\": 1.0617, \"speedup_m64\": 1.0523}, \"status\": \"DONE\"}, \"eval_openvla_pruning_k03\": {\"conclusion\": \"killed\", \"status\": \"DONE\"}, \"openvla_entropy_real\": {\"conclusion\": \"success\", \"metrics\": {\"deep_layers_27_30\": [0.542, 0.53, 0.477, 0.524], \"max_entropy_layer\": {\"layer\": 0, \"ratio\": 0.979}, \"min_entropy_layer\": {\"layer\": 29, \"ratio\": 0.4774}, \"n_images\": 250, \"n_tasks\": 10, \"overall_entropy_ratio\": 0.6393, \"overall_entropy_std\": 0.1334, \"overall_vision_attn_frac\": 0.1211, \"previous_random_N20\": 0.617, \"shallow_layers_0_1\": [0.979, 0.952], \"smolvla_reference\": 0.98}, \"status\": \"DONE\"}, \"train_smart_compress_m128\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"eval_smart_compress_m96\": {\"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 52.6, \"per_task_sr\": {\"task_0_alphabet_soup\": 40, \"task_1_cream_cheese\": 52, \"task_2_salad_dressing\": 56, \"task_3_bbq_sauce\": 40, \"task_4_ketchup\": 26, \"task_5_tomato_sauce\": 50, \"task_6_butter\": 72, \"task_7_milk\": 62, \"task_8_chocolate_pudding\": 86, \"task_9_orange_juice\": 42}, \"total_episodes\": 500, \"total_successes\": 263, \"wilson_ci_95\": [48.2, 56.9]}, \"status\": \"DONE\"}, \"eval_smart_compress_m16\": {\"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 55.8, \"overall_sr_ci95\": [51.4, 60.1], \"per_task_sr\": {\"task_0_alphabet_soup\": 56, \"task_1_cream_cheese\": 44, \"task_2_salad_dressing\": 72, \"task_3_bbq_sauce\": 56, \"task_4_ketchup\": 62, \"task_5_tomato_sauce\": 40, \"task_6_butter\": 78, \"task_7_milk\": 54, \"task_8_chocolate_pudding\": 76, \"task_9_orange_juice\": 20}, \"runtime_minutes\": 55, \"total_episodes\": 500, \"total_successes\": 279}, \"status\": \"DONE\"}, \"eval_openvla_pruning_k07\": {\"conclusion\": \"success\", \"metrics\": {\"elapsed_minutes\": 260.7, \"overall_sr\": 0.49, \"per_task_sr\": {\"alphabet_soup\": 0.74, \"bbq_sauce\": 0.46, \"butter\": 0.1, \"chocolate_pudding\": 0.32, \"cream_cheese\": 0.18, \"ketchup\": 0.68, \"milk\": 0.4, \"orange_juice\": 0.76, \"salad_dressing\": 0.64, \"tomato_sauce\": 0.62}, \"total_episodes\": 500, \"total_successes\": 245}, \"status\": \"DONE\"}, \"train_smart_compress_m96\": {\"conclusion\": \"success\", \"metrics\": {\"eval_action_loss\": 0.064, \"total_steps\": 100000, \"train_action_loss\": 0.055}, \"status\": \"DONE\"}, \"smart_compress_m16\": {\"conclusion\": \"success\", \"metrics\": {\"eval_action_loss\": 0.069, \"total_steps\": 100000, \"train_action_loss\": 0.058}, \"status\": \"DONE\"}, \"eval_smart_compress_m64\": {\"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.616, \"per_task_sr\": {\"alphabet_soup\": 0.74, \"bbq_sauce\": 0.56, \"butter\": 0.84, \"chocolate_pudding\": 0.74, \"cream_cheese\": 0.38, \"ketchup\": 0.64, \"milk\": 0.62, \"orange_juice\": 0.46, \"salad_dressing\": 0.64, \"tomato_sauce\": 0.54}, \"total_episodes\": 500, \"total_successes\": 308, \"wilson_ci_95\": [0.573, 0.658]}, \"status\": \"DONE\"}, \"eval_smart_compress_m32\": {\"conclusion\": \"success\", \"metrics\": {\"overall_sr\": 0.616, \"per_task_sr\": {\"alphabet_soup\": 0.68, \"bbq_sauce\": 0.46, \"butter\": 0.82, \"chocolate_pudding\": 0.9, \"cream_cheese\": 0.64, \"ketchup\": 0.66, \"milk\": 0.76, \"orange_juice\": 0.28, \"salad_dressing\": 0.6, \"tomato_sauce\": 0.36}, \"total_episodes\": 500, \"total_successes\": 308, \"wilson_ci_95\": [0.573, 0.658]}, \"status\": \"DONE\"}, \"train_smart_compress_m32\": {\"conclusion\": \"success\", \"metrics\": {\"checkpoint\": \"checkpoints/smart_compress_m32/checkpoint.pt\", \"checkpoint_size_gb\": 1.5, \"eval_action_loss\": 0.052, \"speed_sps\": 4.1, \"total_steps\": 100000, \"train_action_loss\": 0.11, \"training_duration_h\": 6.5}, \"status\": \"DONE\"}, \"train_smart_compress_m64\": {\"conclusion\": \"success\", \"metrics\": {\"checkpoint\": \"checkpoints/smart_compress_m64/checkpoint.pt\", \"checkpoint_size_gb\": 1.5, \"eval_action_loss\": 0.062, \"speed_sps\": 4.1, \"total_steps\": 100000, \"train_action_loss\": 0.045, \"training_duration_h\": 6.5}, \"status\": \"DONE\"}, \"libero_full_ft_baseline\": {\"conclusion\": \"success\", \"metrics\": {\"diversity_10k\": {\"noise_diversity_std\": 0.1987, \"pass\": true, \"per_obs\": [0.193, 0.192, 0.203, 0.193, 0.213], \"threshold\": 0.05}, \"sr_100k_goal\": {\"n_episodes\": 100, \"overall\": 0.63, \"per_task\": [0.5, 0.9, 0.7, 0.3, 1, 0.4, 0.4, 1, 0.8, 0.3], \"suite\": \"libero_goal\"}, \"sr_100k_object\": {\"n_episodes\": 100, \"overall\": 0.36, \"per_task\": [0, 0.3, 0.4, 0.6, 0.5, 0.1, 0.3, 0.5, 0.4, 0.5], \"suite\": \"libero_object\"}, \"sr_100k_overall\": 0.49, \"sr_100k_spatial\": {\"n_episodes\": 100, \"overall\": 0.48, \"per_task\": [0.8, 0.5, 0.4, 0.4, 0.3, 0.3, 0.6, 0.2, 0.9, 0.4], \"suite\": \"libero_spatial\"}, \"sr_50k\": {\"n_episodes\": 100, \"overall\": 0.33, \"per_task\": [0.1, 0.7, 0.5, 0.1, 0.3, 0.1, 0.5, 0.1, 0.4, 0.5], \"suite\": \"libero_object\", \"wilson_ci_95\": [0.246, 0.427]}, \"sr_50k_goal\": {\"n_episodes\": 100, \"overall\": 0.42, \"per_task\": [0.2, 0.7, 0.5, 0.1, 0.6, 0.5, 0.2, 0.8, 0.5, 0.1], \"suite\": \"libero_goal\", \"wilson_ci_95\": [0.328, 0.518]}, \"sr_50k_spatial\": {\"n_episodes\": 100, \"overall\": 0.34, \"per_task\": [0.8, 0.1, 0.3, 0.2, 0.2, 0.4, 0.3, 0.2, 0.6, 0.3], \"suite\": \"libero_spatial\", \"wilson_ci_95\": [0.255, 0.437]}}, \"status\": \"DONE\"}, \"train_acis_stage1only_k03\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"eval_openvla_pruning_k05\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"geometric_prior_k05_eval\": {\"conclusion\": \"negative\", \"status\": \"DONE\"}, \"eval_openvla_crossmodel_pruning\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"eval_geometric_prior_k09\": {\"conclusion\": \"negative\", \"status\": \"DONE\"}, \"eval_geometric_prior_k07\": {\"conclusion\": \"negative\", \"status\": \"DONE\"}, \"eval_geometric_prior_k05\": {\"conclusion\": \"negative\", \"status\": \"DONE\"}, \"libero_fullft_batch64_v2\": {\"conclusion\": \"killed\", \"status\": \"DONE\"}, \"baseline_bypass_object\": {\"conclusion\": \"success\", \"metrics\": {\"checkpoint_matches_object_eval\": true, \"k_ratio\": 1, \"mode\": \"bypass\", \"overall_sr\": 0.448, \"per_task_sr\": [0.22, 0.6, 0.42, 0.38, 0.58, 0.26, 0.62, 0.38, 0.5, 0.52], \"total_episodes\": 500, \"total_successes\": 224, \"wilson_ci_95\": [0.405, 0.492]}, \"status\": \"DONE\"}, \"action_divergence_v2_clean\": {\"conclusion\": \"success\", \"metrics\": {\"action_l2_mean\": 1.117, \"action_l2_median\": 0.85, \"bypass_early_terminations\": \"multiple\", \"divergence_onset_step\": 0, \"eef_position_l2_mean_m\": 0.214, \"eef_position_l2_median_m\": 0.214, \"first_10_steps_action_l2\": 1.262, \"first_10_steps_eef_l2_m\": 0.041, \"last_10_steps_action_l2\": 0.759, \"last_10_steps_eef_l2_m\": 0.198, \"max_steps\": 300, \"n_episodes_per_task\": 10, \"n_tasks\": 3, \"pattern\": \"immediate_onset_monotonic_growth\", \"pruned_early_terminations\": 0}, \"status\": \"DONE\"}, \"eval_goal_prune_k05\": {\"conclusion\": \"success\", \"metrics\": {\"all_tasks_zero\": true, \"baseline_sr\": 0.63, \"k_ratio\": 0.5, \"mode\": \"acis_prune\", \"overall_sr\": 0, \"pruning_method\": \"true_removal\", \"sr_drop\": -0.63, \"suite\": \"libero_goal\", \"total_episodes\": 500, \"total_successes\": 0, \"wilson_ci_95\": [0, 0.0076]}, \"status\": \"DONE\"}, \"offline_singlestep_action_error\": {\"conclusion\": \"success\", \"metrics\": {\"bypass_vs_gt_l2_mean\": 0.414, \"bypass_vs_pruned_l2_mean\": 1.284, \"conclusion_type\": \"large_per_step_error\", \"interpretation\": \"Pruning directly destroys action prediction at each step. Not a compounding issue.\", \"n_steps\": 200, \"per_dim_gripper\": 1.02, \"per_dim_position_xyz\": [0.2, 0.25, 0.3], \"per_dim_rotation_xyz\": [0.01, 0.02, 0.01], \"pruned_vs_gt_l2_mean\": 1.391, \"relative_error_pct\": 111.5}, \"status\": \"DONE\"}, \"offline_singlestep_error_k05\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"eval_spatial_prune_k05\": {\"conclusion\": \"success\", \"metrics\": {\"all_tasks_zero\": true, \"baseline_sr\": 0.518, \"mode\": \"acis_prune\", \"overall_sr\": 0, \"pruning_method\": \"true_removal\", \"sr_drop\": -0.518, \"suite\": \"libero_spatial\", \"total_episodes\": 500, \"total_successes\": 0, \"wilson_ci_95\": [0, 0.0076]}, \"status\": \"DONE\"}, \"eval_merge_k05\": {\"conclusion\": \"negative\", \"metrics\": {\"episodes\": 500, \"k_ratio\": 0.5, \"libero_object_sr\": 0, \"merge_alpha\": 1, \"pruning_method\": \"merge\", \"pruning_type\": \"acis\", \"wilson_ci_95\": \"[0.0%, 0.76%]\"}, \"status\": \"DONE\"}, \"eval_k07_zero_mask\": {\"conclusion\": \"negative\", \"metrics\": {\"episodes\": 500, \"k_ratio\": 0.7, \"libero_object_sr\": 0, \"pruning_method\": \"zero_mask\", \"pruning_type\": \"acis\", \"wilson_ci_95\": \"[0.0%, 0.76%]\"}, \"status\": \"DONE\"}, \"eval_true_removal_k05\": {\"conclusion\": \"negative\", \"metrics\": {\"episodes\": 500, \"k_ratio\": 0.5, \"libero_object_sr\": 0, \"pruning_method\": \"true_removal\", \"pruning_type\": \"acis\", \"wilson_ci_95\": \"[0.0%, 0.8%]\"}, \"status\": \"DONE\"}, \"eval_stage1only_k09\": {\"conclusion\": \"negative\", \"metrics\": {\"episodes\": 500, \"k_ratio\": 0.9, \"libero_object_sr\": 0, \"pruning_method\": \"zero_mask\", \"pruning_type\": \"acis\"}, \"status\": \"DONE\"}, \"eval_random_prune_k05\": {\"conclusion\": \"negative\", \"metrics\": {\"episodes\": 500, \"k_ratio\": 0.5, \"libero_object_sr\": 0, \"pruning_method\": \"zero_mask\", \"pruning_type\": \"random\"}, \"status\": \"DONE\"}, \"train_acis_stage1only_k07\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"eval_stage1only_object_v2_fixed\": {\"conclusion\": \"negative\", \"metrics\": {\"k_ratio\": 0.5, \"mode\": \"acis_prune\", \"note\": \"Fixed pruning (offset-tracking). Pruning actually executed this time. 0% SR confirms ACIS importance scoring is ineffective for closed-loop control after Stage1-only training.\", \"overall_success_rate\": 0, \"per_task_sr\": [0, 0, 0, 0, 0, 0], \"total_episodes\": 300, \"total_successes\": 0}, \"status\": \"DONE\"}, \"eval_stage1only_spatial\": {\"conclusion\": \"killed\", \"status\": \"DONE\"}, \"eval_stage1_only\": {\"conclusion\": \"success\", \"metrics\": {\"k_ratio\": 0.5, \"mode\": \"acis_prune\", \"overall_success_rate\": 0.448, \"per_task_sr\": [0.22, 0.6, 0.42, 0.38, 0.58, 0.26, 0.62, 0.38, 0.5, 0.52], \"total_episodes\": 500, \"total_successes\": 224, \"wilson_ci_95\": [0.405, 0.4918]}, \"status\": \"DONE\"}, \"libero_fullft_seed1\": {\"conclusion\": \"success\", \"metrics\": {\"eval_action_loss\": 0.05404, \"total_steps\": 100000, \"train_action_loss\": 0.04282, \"train_grad_norm\": 1.17539}, \"status\": \"DONE\"}, \"libero_fullft_batch64\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"eval_imm100k_bypass\": {\"conclusion\": \"negative\", \"metrics\": {\"mode\": \"baseline_bypass\", \"note\": \"Stage2 completely destroyed expert weights\", \"overall_success_rate\": 0, \"per_task_sr\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \"total_episodes\": 500, \"total_successes\": 0, \"wilson_ci_95\": [0, 0.0076]}, \"status\": \"DONE\"}, \"eval_k07_bypass_v3\": {\"conclusion\": \"negative\", \"metrics\": {\"mode\": \"baseline_bypass\", \"note\": \"Stage2 k=0.7 also completely destroyed expert weights\", \"overall_success_rate\": 0, \"per_task_sr\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \"total_episodes\": 500, \"total_successes\": 0, \"wilson_ci_95\": [0, 0.0076]}, \"status\": \"DONE\"}, \"eval_k07_bypass_v2\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"eval_imm_k07_object\": {\"conclusion\": \"negative\", \"metrics\": {\"overall_success_rate\": 0.048, \"per_task_sr\": [0, 0, 0.06, 0.02, 0.32, 0.06, 0.02, 0, 0, 0], \"total_episodes\": 500, \"total_successes\": 24, \"wilson_ci_95\": [0.0325, 0.0704]}, \"status\": \"DONE\"}, \"mvp_imm_anchor_v7_2\": {\"conclusion\": \"negative\", \"metrics\": {\"bypass_acis\": {\"clean_action_loss\": 0.0078, \"conclusion\": \"weights_damaged\", \"g3_ratio\": 1.91}, \"eval_500batch_soft\": {\"clean_action_loss\": 0.013, \"clean_margin_median\": 0.6627, \"clean_preservation\": 1, \"eps001_led_median\": 0.162, \"eps001_preservation\": 0.9253, \"eps002_led_median\": 0.3232, \"eps002_preservation\": 0.8482, \"eps005_led_median\": 0.7656, \"eps005_preservation\": 0.6597, \"lipschitz_empirical\": 0.3393, \"lipschitz_spectral\": 1.0672}, \"gate_v7_2\": {\"G1_margin_ratio\": 64.25, \"G1_pass\": true, \"G2_pass\": true, \"G2_preservation_diff_pp\": 47.46, \"G3_action_loss_ratio\": 3.19, \"G3_pass\": false, \"G4_led_median\": 0.323, \"G4_pass\": true, \"overall\": \"FAIL\"}, \"source\": \"eval_results/eval_imm_v7_2_final.json + eval_results/eval_imm_v7_2_bypass_acis.json\"}, \"status\": \"DONE\"}, \"mvp_imm_anchor_v7\": {\"conclusion\": \"failed\", \"metrics\": {\"eval_500batch\": {\"clean_action_loss\": 0.0134, \"clean_margin_median\": 0.5743, \"clean_preservation\": 1, \"eps001_led_median\": 0.1341, \"eps001_preservation\": 0.9124, \"eps002_led_median\": 0.2726, \"eps002_preservation\": 0.8172, \"eps005_led_median\": 0.69, \"eps005_preservation\": 0.6079, \"lipschitz_empirical\": 0.2493, \"lipschitz_spectral\": 1.0672}, \"source\": \"eval_results/eval_imm_v7_final.json\"}, \"status\": \"DONE\"}, \"libero_fullft_seed0\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"libero_imm_fullft_k07\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"libero_imm_fullft_seed0\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"libero_imm_fullft_100k\": {\"conclusion\": \"success\", \"status\": \"DONE\"}, \"libero_imm_fullft_v2\": {\"conclusion\": \"negative\", \"metrics\": {\"sr_object\": {\"n_episodes\": 100, \"note\": \"IMM two-stage on 50K FT checkpoint, Object suite eval. 15.4% vs baseline 44.8% (-66% relative)\", \"overall\": 0.154, \"source\": \"imm_v2_fullft_libero_object.json\", \"suite\": \"libero_object\"}}, \"status\": \"DONE\"}, \"libero_lora_seed0\": {\"conclusion\": \"negative\", \"status\": \"DONE\"}, \"libero_lora_baseline\": {\"conclusion\": \"negative\", \"metrics\": {\"diversity_10k\": {\"noise_diversity_std\": 0.1736, \"pass\": true, \"per_obs\": [0.166, 0.177, 0.154, 0.198, 0.174], \"threshold\": 0.05}, \"sr_100k\": {\"all_episodes_hit_max_steps\": true, \"eval_running\": true, \"max_steps\": 400, \"n_episodes_completed\": 10, \"n_episodes_total\": 100, \"note\": \"task_0 complete 0/10, remaining tasks 1-9 still evaluating but pattern is conclusive\", \"overall\": 0, \"suite\": \"libero_object\", \"task_0_episodes\": 10, \"task_0_sr\": 0}, \"sr_50k\": {\"lora_keys_loaded\": 74, \"missing_keys\": 0, \"n_episodes\": 50, \"overall\": 0, \"per_task\": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \"suite\": \"libero_object\", \"unexpected_keys\": 0, \"verdict\": \"CORRECT_LOAD_confirmed_0pct_SR\", \"verified\": true}, \"training_100k\": {\"checkpoint_size_mb\": 883, \"completed_normally\": true, \"final_eval_loss\": 0.08041, \"final_grad_norm\": 0.415, \"final_lr\": 2.5e-06, \"final_step\": 99999, \"final_train_loss\": 0.0648}}, \"status\": \"DONE\"}, \"libero_imm_twostage_v1\": {\"conclusion\": \"killed\", \"status\": \"DONE\"}, \"plan_009_token_importance\": {\"conclusion\": \"success\", \"metrics\": {\"action_loss_mean\": 0.0195, \"gradient_ratio_retained_over_pruned\": 1.7027, \"n_samples\": 100, \"n_vis_tokens\": 64, \"pruned_grad_mean\": 0.000183, \"retained_grad_mean\": 0.000311, \"spearman_corr_mean\": 0.4069, \"spearman_corr_median\": 0.4065, \"spearman_corr_std\": 0.1022}, \"status\": \"DONE\"}, \"plan_011_acis_overhead\": {\"conclusion\": \"success\", \"metrics\": {\"flops_acis_increment_M\": 409.75, \"flops_baseline_G\": 169.87, \"flops_overhead_pct\": 0.24, \"latency_acis_increment_ms\": 0.32, \"latency_baseline_ms\": 51.16, \"latency_overhead_pct\": 0.63, \"n_trials\": 100, \"params_acis_increment_M\": 3.46, \"params_baseline_M\": 451.53, \"params_overhead_pct\": 0.77, \"source\": \"results/acis_overhead.json\"}, \"status\": \"DONE\"}, \"plan_008_pruning_sweep_v2\": {\"conclusion\": \"success\", \"metrics\": {\"G3_best\": 0.237, \"G3_best_k\": 0.6, \"G3_k05\": 0.24, \"improvement_pct\": 76.2, \"source\": \"eval_results/pruning_sweep_v2.json\", \"sweet_spot\": \"k=0.5-0.6\"}, \"status\": \"DONE\"}, \"plan_005_formal_bound_v2\": {\"conclusion\": \"success\", \"metrics\": {\"L_empirical\": 0.193, \"L_spectral\": 1.067, \"margin_median\": 0.96, \"source\": \"results/formal_bound_plan005.json\", \"stability_eps01\": 0.976, \"tightness_spectral_max\": 1.125, \"tightness_spectral_min\": 1.005}, \"status\": \"DONE\"}, \"plan_008_pruning_sweep\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"baseline_v6_alpha16\": {\"conclusion\": \"negative\", \"metrics\": {\"mode_collapse_test\": {\"checkpoint\": \"checkpoints/baseline_v6_alpha16/step_029999/checkpoint.pt\", \"comparison_alpha64\": \"alpha64 std=0.006, alpha16 std=0.007 — no meaningful improvement\", \"cross_obs_std\": 0.096329, \"noise_diversity_std\": 0.007352, \"pretrained_noise_std\": null, \"threshold_fail\": 0.01, \"threshold_pass\": 0.05, \"verdict\": \"FAIL\"}}, \"status\": \"DONE\"}, \"mvp_imm_v8c_annealing\": {\"conclusion\": \"negative\", \"metrics\": {\"G1_margin_ratio\": 108.15, \"G2_preservation_diff\": 60.92, \"G3_deploy\": 2.04, \"G4_LED\": 0.1046, \"action_loss_acis_prune\": null, \"action_loss_baseline\": null, \"final_action_loss\": 0.0023, \"final_margin_loss\": 0.0938, \"final_train_loss\": 0.0492}, \"status\": \"DONE\"}, \"mvp_imm_v8b_twostage\": {\"conclusion\": \"success\", \"metrics\": {\"sim_success_rate\": {\"acis_prune\": 0, \"acis_prune_mean_reward\": 0, \"baseline\": 0, \"baseline_mean_reward\": 0.16, \"bypass\": 0, \"bypass_mean_reward\": 0, \"n_episodes\": 50, \"wilson_ci_95_upper\": 0.0714}}, \"status\": \"DONE\"}, \"mvp_imm_anchor_v8_1\": {\"conclusion\": \"negative\", \"status\": \"DONE\"}, \"mvp_imm_anchor_v8\": {\"conclusion\": \"negative\", \"metrics\": {\"baseline_v5_fixed\": {\"clean_action_loss\": 0.004063, \"eps001_preservation\": 0.3352, \"margin_median\": 0.010022, \"source\": \"eval_results/eval_baseline_v5_fixed.json\"}, \"checkpoint_trajectory\": {\"step_2000\": {\"acis_advantage\": 0.0068, \"acis_prune\": 0.0357, \"bypass\": 0.05842, \"random_prune\": 0.0425, \"standard\": 0.03787}, \"step_29999\": {\"acis_advantage\": 0.01246, \"acis_prune\": 0.0033, \"bypass\": 0.0323, \"random_prune\": 0.01576, \"standard\": 0.00659}}, \"eval_500batch_bypass_fixed\": {\"bypass_clean_action_loss\": 0.028948, \"bypass_pruned_action_loss\": 0.017215, \"eps001_action_loss_noprune\": 0.027873, \"eps001_action_loss_prune\": 0.016572, \"eps005_action_loss_noprune\": 0.039901, \"eps005_action_loss_prune\": 0.02627, \"source\": \"eval_results/eval_imm_v8_bypass_fixed.json\"}, \"eval_500batch_fixed\": {\"bypass_clean_action_loss\": 0.028948, \"eps001_kendall_tau\": 0.8393, \"eps001_led_median\": 0.0852, \"eps001_preservation\": 0.923, \"eps002_led_median\": 0.1714, \"eps002_preservation\": 0.8367, \"eps005_led_median\": 0.4429, \"eps005_preservation\": 0.6613, \"eval_tag\": \"D028_fix_reeval\", \"lipschitz_empirical\": 0.1364, \"lipschitz_spectral\": 1.0672, \"margin_mean\": 0.7696, \"margin_median\": 0.5034, \"margin_std\": 0.8133, \"pruneFalse_clean_action_loss\": 0.029996, \"pruneTrue_clean_action_loss\": 0.005462, \"source\": \"eval_results/eval_imm_v8_fixed.json\", \"standard_clean_action_loss\": 0.005462}, \"gate_analysis_fixed\": {\"G1_margin_ratio\": 50.2, \"G1_pass\": true, \"G2_pass\": true, \"G2_preservation_diff_pp\": 58.78, \"G3_clean_loss_ratio\": 1.344, \"G3_deploy_pass\": false, \"G3_deploy_ratio\": 1.344, \"G3_pass\": false, \"G3_target\": 1.1, \"G4_led_median\": 0.0865, \"G4_pass\": true, \"bypass_backbone_ratio\": 7.12, \"eval_tag\": \"D028_fix_reeval\", \"notes\": \"Fixed eval (5 bugs: eps0 pruning flag, hard binary mask, per-condition RNG, eval mode, preloaded batches). Results consistent with old buggy eval within ~5%. G3 still fails at 1.344x.\", \"overall_pass\": false}}, \"status\": \"DONE\"}, \"mvp_baseline_v5\": {\"conclusion\": \"success\", \"metrics\": {\"eval_500batch\": {\"clean_action_loss\": 0.004077, \"clean_margin_median\": 0.010022, \"eps001_preservation\": 0.3352, \"eps002_preservation\": 0.3362, \"eps005_preservation\": 0.3381}, \"mid_checkpoints\": {\"step005000\": {\"clean_action_loss\": 0.01891, \"clean_margin_mean\": 0.01608, \"clean_margin_median\": 0.01002, \"clean_pruned_action_loss\": 0.08304, \"eps001_action_loss\": 0.02234, \"eps001_kendall_tau\": -0.2315, \"eps001_preservation\": 0.3359, \"eps001_pruned_action_loss\": 0.08645, \"eps002_action_loss\": 0.02057, \"eps002_preservation\": 0.3369, \"eps002_pruned_action_loss\": 0.0882, \"eps005_action_loss\": 0.03377, \"eps005_preservation\": 0.34, \"eps005_pruned_action_loss\": 0.0912, \"lipschitz_empirical\": 0, \"lipschitz_spectral\": 0, \"source\": \"eval_results/eval_baseline_v5_step5000.json\"}, \"step010000\": {\"clean_action_loss\": 0.00974, \"clean_margin_mean\": 0.01608, \"clean_margin_median\": 0.01002, \"clean_pruned_action_loss\": 0.09434, \"eps001_action_loss\": 0.01243, \"eps001_kendall_tau\": -0.2315, \"eps001_preservation\": 0.3359, \"eps001_pruned_action_loss\": 0.09473, \"eps002_action_loss\": 0.01092, \"eps002_preservation\": 0.3369, \"eps002_pruned_action_loss\": 0.10085, \"eps005_action_loss\": 0.02565, \"eps005_preservation\": 0.34, \"eps005_pruned_action_loss\": 0.10132, \"lipschitz_empirical\": 0, \"lipschitz_spectral\": 0, \"source\": \"eval_results/eval_baseline_v5_step10000.json\"}}, \"source\": \"eval_results/eval_baseline_v5_final.json\"}, \"status\": \"DONE\"}, \"mvp_imm_anchor_v7_1\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"mvp_imm_anchor_v6\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"mvp_imm_anchor_v5\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"mvp_baseline_v4\": {\"conclusion\": \"killed\", \"status\": \"DONE\"}, \"mvp_imm_anchor_v4\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"mvp_baseline_v3\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"mvp_imm_anchor_v2\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"mvp_baseline_v2\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"mvp_imm_anchor\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"mvp_baseline\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"eval_oft_baseline_object_seed42_v2\": {\"conclusion\": \"failed\", \"status\": \"DONE\"}, \"eval_openvla_prune_l2norm_k03_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"num_episodes\": 500, \"seed\": 42, \"success_rate\": 0.25, \"suite\": \"libero_object\"}, \"status\": \"DONE\"}, \"eval_openvla_prune_l2norm_k05_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"num_episodes\": 500, \"seed\": 42, \"success_rate\": 0.392, \"suite\": \"libero_object\"}, \"status\": \"DONE\"}, \"eval_openvla_prune_l2norm_k095_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"num_episodes\": 500, \"seed\": 42, \"success_rate\": 0.706, \"suite\": \"libero_object\"}, \"status\": \"DONE\"}, \"eval_openvla_prune_l2norm_k09_seed42\": {\"conclusion\": \"success\", \"metrics\": {\"num_episodes\": 500, \"seed\": 42, \"success_rate\": 0.706, \"suite\": \"libero_object\"}, \"status\": \"DONE\"}}, \"count\": 738, \"total\": 738, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.152}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 84_

<details><summary>Logged reasoning block</summary>

```text
So the three "unregistered" experiments actually all already existed in the registry:
1. `eval_openvla_attn_k07_long_seed42_v2` - already DONE, conclusion=negative, success_rate=24%
2. `eval_openvla_l2norm_k075_long_seed42` - already DONE, conclusion=failed (timeout)
3. `eval_openvla_random_k05_object_seed42_v2` - already DONE, conclusion=killed

So they were already registered! Good. But the l2norm k=0.75 long one failed due to timeout and is still running on the server (PID 732922 on westd-27271). 

That's a re-run that's not being tracked. Since the completed experiments have output files that are too large to work with directly, I'll use jq to extract just the cliff curve metrics I need from the JSON files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "91b3d5c1-50da-4650-a87b-7ce4afd361f3",
  "uuid": "41000938-9a54-48b1-88ac-b6b9b502809c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XNAhUCrKipXy7Y5tLPg5RF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6766,
      "cache_read_input_tokens": 57446,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6766
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Assistant

_source line 85_

所有三个"未注册"实验实际已在 registry 中。现在提取 DONE 实验数据构建 cliff curves。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "91b3d5c1-50da-4650-a87b-7ce4afd361f3",
  "uuid": "54479fef-63bd-4073-aede-ff40eabd6871",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XNAhUCrKipXy7Y5tLPg5RF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6766,
      "cache_read_input_tokens": 57446,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6766
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 86_

<details open><summary>🔧 Tool call — Bash · `toolu_01PAiqpc28disC8d31ecxg9d`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/91b3d5c1-50da-4650-a87b-7ce4afd361f3/tool-results/mcp-agent-ml-research-read_registry-1779845804446.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\nfor eid, e in exps.items():\n    m = e.get('metrics', {})\n    sr = m.get('overall_sr') or m.get('success_rate')\n    suite = m.get('suite', '')\n    method = m.get('prune_method', '')\n    kr = m.get('keep_ratio', '')\n    conclusion = e.get('conclusion', '')\n    if sr is not None:\n        print(f'{eid}|{suite}|{method}|{kr}|{sr}|{conclusion}')\n\" | sort",
  "description": "Extract cliff curve data from DONE experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "91b3d5c1-50da-4650-a87b-7ce4afd361f3",
  "uuid": "4bb4c550-3890-49d4-8f9a-bfff5a986f11",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XNAhUCrKipXy7Y5tLPg5RF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6766,
      "cache_read_input_tokens": 57446,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6766
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 87 · 2026-05-27T01:36:58.846Z_

<details><summary>↩ Tool result · `toolu_01PAiqpc28disC8d31ecxg9d`</summary>

```text
baseline_bypass_object||||0.448|success
eval_baseline_control_100k_v2|libero_object|||45|success
eval_baseline_control_prune_k05|libero_object|||0|success
eval_e5_xvla_attn_last_goal_k05_v2||||98.2|success
eval_e5_xvla_attn_last_obj_k03||||84.2|success
eval_e5_xvla_attn_last_spatial_k03||||85.6|success
eval_e5_xvla_attn_mean_goal_k05_v2||||97.4|success
eval_e5_xvla_attn_mean_obj_k03||||96|success
eval_e5_xvla_attn_mean_spatial_k03||||90.4|success
eval_e5_xvla_attn_mean_spatial_k05||||91.6|success
eval_e5_xvla_attn_rollout_goal_k05_v2||||96.8|success
eval_e5_xvla_attn_rollout_obj_k03||||92|success
eval_e5_xvla_attn_rollout_spatial_k05||||92.8|success
eval_e5_xvla_random_goal_k05_v2||||67.2|negative
eval_official_smolvla_baseline||||59.2|success
eval_openvla_attn_k05_goal_seed42||||44.2|success
eval_openvla_attn_k05_long_seed42|libero_10|attention|0.5|14.6|success
eval_openvla_attn_k075_object_seed42||||53.2|success
eval_openvla_attn_k07_goal_seed42||||0.664|negative
eval_openvla_attn_k07_long_seed42_v2||||24|negative
eval_openvla_attn_k07_object_seed42_v3||||43.8|success
eval_openvla_attn_k085_goal_seed42_v3||||74.6|success
eval_openvla_attn_k085_long_seed42_v3|libero_10|||45.8|killed
eval_openvla_attn_k085_long_seed42_v5||||45.8|success
eval_openvla_attn_k085_object_seed42||||0.55|success
eval_openvla_attn_k09_goal_seed42||||0.732|success
eval_openvla_attn_k09_goal_seed43_v4||||73.2|success
eval_openvla_attn_k09_long_seed42_v3|libero_10|||44.0|success
eval_openvla_attn_k09_spatial_seed42||||0.804|success
eval_openvla_baseline_goal_seed42_v3||||74.8|success
eval_openvla_baseline_goal_seed43||||0.776|success
eval_openvla_baseline_long_seed42||||0.528|success
eval_openvla_baseline_object_seed42_v2||||0.74|success
eval_openvla_baseline_object_seed42||||74|success
eval_openvla_baseline_spatial|libero_spatial|||0.8|success
eval_openvla_l2norm_k03_object_seed42||||25.0|success
eval_openvla_l2norm_k03_object_seed43||||25|success
eval_openvla_l2norm_k05_goal_seed42_v3||||0.434|negative
eval_openvla_l2norm_k05_goal_seed42||||0.434|success
eval_openvla_l2norm_k05_object_seed42_v4||||0.392|success
eval_openvla_l2norm_k05_object_seed42||||39.2|success
eval_openvla_l2norm_k05_object_seed43||||39.2|success
eval_openvla_l2norm_k075_goal_seed42_v2||||70.2|success
eval_openvla_l2norm_k075_object_seed42||||0.574|negative
eval_openvla_l2norm_k07_goal_seed42||||0.684|success
eval_openvla_l2norm_k07_long_seed42_v2||||0.312|success
eval_openvla_l2norm_k07_object_seed42_v2||||0.498|success
eval_openvla_l2norm_k07_object_seed42_v3||||0.498|success
eval_openvla_l2norm_k085_goal_seed42||||75.4|success
eval_openvla_l2norm_k085_long_seed42_v2|libero_10_long|||0.388|success
eval_openvla_l2norm_k095_object_seed42||||70.6|success
eval_openvla_l2norm_k09_goal_seed42||||0.748|success
eval_openvla_l2norm_k09_goal_seed43_v3||||0.752|success
eval_openvla_l2norm_k09_goal_seed43||||75.2|success
eval_openvla_l2norm_k09_long_seed42_v3|libero_10|||43.6|success
eval_openvla_l2norm_k09_object_seed42||||0.706|success
eval_openvla_l2norm_k09_spatial_seed42||||0.75|success
eval_openvla_prune_k095|libero_object|||69.4|success
eval_openvla_prune_k09|libero_object|||62|success
eval_openvla_prune_l2norm_k03_seed42|libero_object|||0.25|success
eval_openvla_prune_l2norm_k03||||0.25|success
eval_openvla_prune_l2norm_k05_seed42|libero_object|||0.392|success
eval_openvla_prune_l2norm_k05||||0.392|success
eval_openvla_prune_l2norm_k07_seed43_v2||||49.8|success
eval_openvla_prune_l2norm_k07_seed43||||0.74|failed
eval_openvla_prune_l2norm_k095_seed42|libero_object|||0.706|success
eval_openvla_prune_l2norm_k095||||0.706|success
eval_openvla_prune_l2norm_k09_seed42|libero_object|||0.706|success
eval_openvla_prune_l2norm_k09||||0.706|success
eval_openvla_prune_random_k05_seed42||||35.8|success
eval_openvla_prune_random_k05_seed43_v2||||0.356|success
eval_openvla_prune_random_k07_seed42_v2||||44.4|success
eval_openvla_prune_random_k07_seed43_v2||||0.526|success
eval_openvla_prune_random_k095_seed42_v2||||69.2|success
eval_openvla_prune_random_k095_seed43||||0.668|success
eval_openvla_prune_random_k09_seed42||||0.646|success
eval_openvla_prune_random_k09_seed43||||0.622|success
eval_openvla_pruning_k03_restart||||0.206|success
eval_openvla_pruning_k07||||0.49|success
eval_openvla_random_k05_goal_seed42_v2||||0.522|negative
eval_openvla_random_k05_goal_seed42||||0.522|success
eval_openvla_random_k05_long_seed42_v2||||18.6|negative
eval_openvla_random_k05_object_seed42_v3||||35.8|negative
eval_openvla_random_k05_spatial_seed42||||0.5|success
eval_openvla_random_k075_goal_seed42|libero_goal|random|0.75|72|success
eval_openvla_random_k07_goal_seed42_v4||||68.4|success
eval_openvla_random_k07_long_seed42_v2||||0.388|success
eval_openvla_random_k07_object_seed42_v2||||0.444|success
eval_openvla_random_k07_object_seed43||||0.526|success
eval_openvla_random_k085_goal_seed42||||78.6|success
eval_openvla_random_k085_long_seed42_v3||||0.45|success
eval_openvla_random_k09_goal_seed42||||79.6|success
eval_openvla_random_k09_goal_seed43||||80.4|success
eval_openvla_random_k09_long_seed42_v3|libero_10|||46.8|success
eval_openvla_random_k09_spatial_seed42||||79.8|success
eval_openvla_sc_m128_object_seed42||||0.0|failed
eval_openvla_zeromask_random_k09_object_seed42||||0.718|success
eval_pi05_attention_k05_goal_seed42||||70.2|negative
eval_pi05_attention_k05_goal_seed43||||0.722|negative
eval_pi05_attention_k05_long_seed42_v2||||49.8|success
eval_pi05_attention_k05_spatial_seed42||||0.726|negative
eval_pi05_attention_k075_long_seed42_v2||||52.4|success
eval_pi05_attention_k075_long_seed42||||51.8|success
eval_pi05_attention_k07_long_seed42_v2|libero_10|attention|0.7|50.8|success
eval_pi05_attention_k07_object_seed42|libero_object||0.7|0.006|negative
eval_pi05_attention_k085_long_seed42_v2||||51.6|success
eval_pi05_attention_k085_object_seed42|libero_object|||0.922|success
eval_pi05_attention_k095_object_seed42|libero_object|||0.984|success
eval_pi05_attention_k09_long_seed42_postfix||||0.638|success
eval_pi05_attention_k09_object_seed42|libero_object|||0.972|success
eval_pi05_attn_k095_long_seed42||||77|success
eval_pi05_baseline_goal_seed42||||0.964|success
eval_pi05_baseline_long_seed42||||92.8|success
eval_pi05_baseline_object_seed42||||98.2|success
eval_pi05_baseline_spatial_seed42||||97.2|success
eval_pi05_l2norm_k01_object_seed42||||0.026|success
eval_pi05_l2norm_k03_goal_seed42_postfix||||0.518|success
eval_pi05_l2norm_k03_goal_seed42_v2||||50.6|negative
eval_pi05_l2norm_k03_long_seed42_postfix||||0.366|killed
eval_pi05_l2norm_k03_long_seed43_postfix_v2||||39.2|success
eval_pi05_l2norm_k03_object_seed42||||0.51|success
eval_pi05_l2norm_k03_spatial_seed42_postfix|libero_spatial||0.3|52.8|success
eval_pi05_l2norm_k03_spatial_seed42||||57.2|negative
eval_pi05_l2norm_k05_goal_seed42_postfix||||59.8|success
eval_pi05_l2norm_k05_goal_seed42|libero_goal|||0.592|negative
eval_pi05_l2norm_k05_long_seed42_v3||||51.4|success
eval_pi05_l2norm_k05_long_seed42_v4||||50|success
eval_pi05_l2norm_k05_long_seed42||||0.502|success
eval_pi05_l2norm_k05_long_seed43_postfix_v2||||0.53|success
eval_pi05_l2norm_k05_object_seed42|||0.5|33.4|negative
eval_pi05_l2norm_k05_object_seed43||||0.336|success
eval_pi05_l2norm_k05_spatial_seed42_postfix||||0.574|success
eval_pi05_l2norm_k05_spatial_seed42||||55.6|success
eval_pi05_l2norm_k05_spatial_seed43_v2||||0.554|success
eval_pi05_l2norm_k075_long_seed42||||73.4|success
eval_pi05_l2norm_k07_goal_seed42_postfix||||70.2|success
eval_pi05_l2norm_k07_goal_seed42_v2||||73.6|negative
eval_pi05_l2norm_k07_long_seed42_postfix||||62.6|success
eval_pi05_l2norm_k07_long_seed43_v2||l2norm|0.7|65.8|success
eval_pi05_l2norm_k07_long_seed43_v3||||0.65|success
eval_pi05_l2norm_k07_long_seed43_v4||||0.654|success
eval_pi05_l2norm_k07_object_seed42_postfix||||56.4|success
eval_pi05_l2norm_k07_object_seed42||||55|success
eval_pi05_l2norm_k07_object_seed43||||56.4|success
eval_pi05_l2norm_k07_spatial_seed42||||67|success
eval_pi05_l2norm_k085_goal_seed42_postfix||||87.4|success
eval_pi05_l2norm_k085_goal_seed42|libero_goal||0.85|88|success
eval_pi05_l2norm_k085_goal_seed43_postfix||||87|success
eval_pi05_l2norm_k085_long_seed42_postfix_v3||||0.78|success
eval_pi05_l2norm_k085_long_seed42_postfix||||78.4|success
eval_pi05_l2norm_k085_long_seed42_v3||||78.8|success
eval_pi05_l2norm_k085_long_seed42|libero_10||0.85|0.78|success
eval_pi05_l2norm_k085_long_seed43_postfix||||78.6|success
eval_pi05_l2norm_k085_long_seed43_v2||l2norm|0.85|79|success
eval_pi05_l2norm_k085_long_seed43_v3||||80|success
eval_pi05_l2norm_k085_long_seed43_v4||||0.77|success
eval_pi05_l2norm_k085_object_seed42_postfix_v2||||98.4|success
eval_pi05_l2norm_k085_object_seed42_v4||||0.98|success
eval_pi05_l2norm_k085_object_seed43_postfix||||99|success
eval_pi05_l2norm_k085_spatial_seed42_v2||||88.6|success
eval_pi05_l2norm_k085_spatial_seed42_v3||||88.4|success
eval_pi05_l2norm_k085_spatial_seed43_postfix||||0.882|success
eval_pi05_l2norm_k0925_goal_seed42_postfix||||89.8|success
eval_pi05_l2norm_k0925_goal_seed42_v2||||89|success
eval_pi05_l2norm_k0925_goal_seed42_v3||||89.8|success
eval_pi05_l2norm_k0925_goal_seed43||||90.8|success
eval_pi05_l2norm_k0925_long_seed42_v2||||0.832|success
eval_pi05_l2norm_k0925_object_seed42||||99.2|success
eval_pi05_l2norm_k095_goal_seed42_postfix||||90.8|success
eval_pi05_l2norm_k095_goal_seed42_v2||||89.4|success
eval_pi05_l2norm_k095_goal_seed42||||0.908|negative
eval_pi05_l2norm_k095_long_seed42_postfix|libero_10||0.95|87|success
eval_pi05_l2norm_k095_long_seed43_postfix|libero_10|||87.4|success
eval_pi05_l2norm_k095_object_seed42_v2||||98.2|success
eval_pi05_l2norm_k095_spatial_seed42|libero_spatial|||0.978|success
eval_pi05_l2norm_k09_goal_seed42_postfix||||88.6|success
eval_pi05_l2norm_k09_goal_seed42_v2||||90.6|success
eval_pi05_l2norm_k09_goal_seed42|libero_goal|||0.9|negative
eval_pi05_l2norm_k09_goal_seed43_postfix||||91|success
eval_pi05_l2norm_k09_long_seed42_postfix_v2||||80|success
eval_pi05_l2norm_k09_long_seed43_postfix_v2||||80|success
eval_pi05_l2norm_k09_long_seed43_postfix||||0.808|success
eval_pi05_l2norm_k09_object_seed42_v2||||98.2|success
eval_pi05_l2norm_k09_object_seed43_postfix||||98.4|success
eval_pi05_l2norm_k09_spatial_seed42_postfix||||96|success
eval_pi05_l2norm_k09_spatial_seed43_postfix||||96.2|success
eval_pi05_random_k03_goal_seed42_postfix||||52.8|success
eval_pi05_random_k03_goal_seed42_v2||||50.6|negative
eval_pi05_random_k03_goal_seed43_v2||||53.6|success
eval_pi05_random_k03_long_seed42_postfix||||29.6|success
eval_pi05_random_k03_long_seed42||||0.29|success
eval_pi05_random_k03_long_seed43_v2||||28|success
eval_pi05_random_k03_long_seed43_v3||random|0.3|28.4|success
eval_pi05_random_k03_long_seed43_v4||||0.272|success
eval_pi05_random_k03_object_seed42||||0.364|success
eval_pi05_random_k03_spatial_seed42_postfix_v2||||43.4|success
eval_pi05_random_k03_spatial_seed42||||49.6|success
eval_pi05_random_k05_goal_seed42_postfix||||73.6|success
eval_pi05_random_k05_long_seed42_postfix|libero_10||0.5|46.8|success
eval_pi05_random_k05_long_seed42_v2|libero_10||0.5|46.8|success
eval_pi05_random_k05_long_seed42_v3||||50.2|success
eval_pi05_random_k05_long_seed42||||0.502|success
eval_pi05_random_k05_long_seed43_postfix||||46.8|success
eval_pi05_random_k05_long_seed43_v2||random|0.5|51.2|success
eval_pi05_random_k05_object_seed42||||0.694|success
eval_pi05_random_k05_object_seed43||||68.4|success
eval_pi05_random_k05_spatial_seed42_postfix_v3||||0.718|success
eval_pi05_random_k05_spatial_seed42||||71.6|success
eval_pi05_random_k05_spatial_seed43_v2||||72.4|success
eval_pi05_random_k075_long_seed42_v2|libero_10|||62.4|success
eval_pi05_random_k07_goal_seed42_postfix||||75.6|success
eval_pi05_random_k07_goal_seed42_v2||||78.2|negative
eval_pi05_random_k07_goal_seed42|libero_goal|||0.806|success
eval_pi05_random_k07_long_seed42_postfix|libero_10||0.7|65.8|success
eval_pi05_random_k07_long_seed42|libero_10|random|0.7|62.4|success
eval_pi05_random_k07_long_seed43_postfix||||0.686|success
eval_pi05_random_k07_object_seed42_v4||||74|success
eval_pi05_random_k07_object_seed42||||0.772|success
eval_pi05_random_k07_object_seed43||||73.8|success
eval_pi05_random_k07_spatial_seed42_postfix||||73.8|success
eval_pi05_random_k07_spatial_seed42||||74.4|success
eval_pi05_random_k085_goal_seed42_postfix_v3||||53|success
eval_pi05_random_k085_goal_seed42_postfix||||52.8|success
eval_pi05_random_k085_goal_seed42_v3|libero_goal|||0.524|success
eval_pi05_random_k085_goal_seed42_v4||||52.4|success
eval_pi05_random_k085_goal_seed43_postfix||||0.534|success
eval_pi05_random_k085_goal_seed43|libero_goal||0.85|0.522|negative
eval_pi05_random_k085_long_seed42_postfix_v3||||49.4|success
eval_pi05_random_k085_long_seed42_postfix|libero_10||0.85|45.2|success
eval_pi05_random_k085_long_seed42_v2||||44.4|success
eval_pi05_random_k085_long_seed43_postfix||||0.418|success
eval_pi05_random_k085_long_seed43_v2||||42|success
eval_pi05_random_k085_long_seed43_v3||||0.424|success
eval_pi05_random_k085_long_seed43||random|0.85|41.8|success
eval_pi05_random_k085_object_seed42_postfix||||5.6|success
eval_pi05_random_k085_object_seed42_v2||||5|negative
eval_pi05_random_k085_object_seed43_postfix||||0.048|success
eval_pi05_random_k085_spatial_seed42_postfix_v2||||60.8|success
eval_pi05_random_k085_spatial_seed42_v2||||56.6|success
eval_pi05_random_k085_spatial_seed42_v3||||60.2|success
eval_pi05_random_k085_spatial_seed42|libero_spatial|||0.584|success
eval_pi05_random_k085_spatial_seed43_postfix||||59.2|success
eval_pi05_random_k0925_goal_seed42_v2||||71.2|negative
eval_pi05_random_k0925_goal_seed42_v3||||70|success
eval_pi05_random_k0925_long_seed42_postfix||||38.6|success
eval_pi05_random_k0925_object_seed42_postfix||||27.2|success
eval_pi05_random_k0925_object_seed42||||0.276|negative
eval_pi05_random_k0925_object_seed43|libero_object|||0.3|success
eval_pi05_random_k0925_spatial_seed42_unreg||||58.2|success
eval_pi05_random_k095_goal_seed42_postfix||||82.6|success
eval_pi05_random_k095_goal_seed42_v2||||83.8|success
eval_pi05_random_k095_goal_seed43|libero_goal||0.95|0.834|success
eval_pi05_random_k095_long_seed42_postfix|libero_10||0.95|63.2|success
eval_pi05_random_k095_long_seed42|libero_10||0.95|0.612|success
eval_pi05_random_k095_long_seed43_postfix||||0.584|success
eval_pi05_random_k095_object_seed42_v2||||74|success
eval_pi05_random_k095_object_seed43||||0.728|success
eval_pi05_random_k095_spatial_seed42_postfix_v2||||76.8|success
eval_pi05_random_k09_fixedmask_object_seed42_v2||||0.17|negative
eval_pi05_random_k09_goal_seed42_postfix||||61.8|success
eval_pi05_random_k09_goal_seed42_v2||||62.2|negative
eval_pi05_random_k09_goal_seed43_postfix||||61.2|success
eval_pi05_random_k09_long_seed42_postfix||||32|success
eval_pi05_random_k09_long_seed43_postfix||||0.356|killed
eval_pi05_random_k09_object_seed43_postfix||||7.4|success
eval_pi05_random_k09_object_seed43_v3||||9.6|success
eval_pi05_random_k09_object_seed43_v4|libero_object|random|0.9|9.6|success
eval_pi05_random_k09_object_seed43||||0.096|success
eval_pi05_random_k09_spatial_seed42_postfix_v2||||53.4|negative
eval_pi05_random_k09_spatial_seed43_postfix_v2||||54|success
eval_pi05_zeromask_l2norm_k09_object_seed42||||0.994|success
eval_pi05_zeromask_random_k09_object_seed42_v3||||0.98|success
eval_smart_compress_m128_seed43|libero_object|||0.54|success
eval_smart_compress_m16_seed43|libero_object|||0.584|success
eval_smart_compress_m16_seed44|libero_object|||0.565|success
eval_smart_compress_m16||||55.8|success
eval_smart_compress_m32_libero_goal|libero_goal|||56.4|success
eval_smart_compress_m32_libero_spatial|libero_spatial|||53.2|success
eval_smart_compress_m32_seed43|libero_object|||59.2|success
eval_smart_compress_m32_seed44||||59.6|success
eval_smart_compress_m32||||0.616|success
eval_smart_compress_m64_seed43|libero_object|||60|success
eval_smart_compress_m64_seed44||||64.4|success
eval_smart_compress_m64||||0.616|success
eval_smart_compress_m96_seed43_v2|libero_object|||58.2|success
eval_smart_compress_m96_seed43|libero_object|||0|failed
eval_smart_compress_m96_seed44||||52.8|success
eval_smart_compress_m96||||52.6|success
eval_smolvla_baseline_spatial_westd38929_seed42||||8.0|success
eval_smolvla_metaworld_baseline||||26.4|success
eval_smolvla_official_baseline_object_seed42||||57.2|success
eval_smolvla_official_l2norm_k050_object_seed42||||0|success
eval_smolvla_official_l2norm_k095_object_seed42||||0.4|success
eval_smolvla_official_random_k095_object_seed42||||0|success
eval_smolvla_zeromask_l2norm_k095_object_seed42||||0|negative
eval_smolvla_zeromask_random_k095_object_seed42||||0.002|negative
eval_xvla_baseline_goal_seed42||||0.984|success
eval_xvla_baseline_long_seed42|libero_10|||0.94|success
eval_xvla_baseline_spatial_seed42||||0.93|success
eval_xvla_goal_k05_seed42|libero_goal|||0.61|success
eval_xvla_goal_k09_seed42|libero_goal|||0.702|success
eval_xvla_l2norm_k03_goal_seed42_v3||||0.376|negative
eval_xvla_l2norm_k03_goal_seed42_v4||||37.6|negative
eval_xvla_l2norm_k03_goal_seed42_v5||||0.37|success
eval_xvla_l2norm_k03_object_seed42||||0.222|success
eval_xvla_l2norm_k03_spatial_seed42||||0.312|negative
eval_xvla_l2norm_k05_goal_seed42_v2|libero_goal||0.5|0.59|success
eval_xvla_l2norm_k05_goal_seed42_v3||||59|negative
eval_xvla_l2norm_k05_long_seed42_v4||||44.6|success
eval_xvla_l2norm_k05_long_seed42||||45|success
eval_xvla_l2norm_k05_object_seed42||||0.434|success
eval_xvla_l2norm_k05_spatial_seed42_v3||||58.8|negative
eval_xvla_l2norm_k05_spatial_seed43||||59|negative
eval_xvla_l2norm_k07_goal_seed42|libero_goal|||0.534|negative
eval_xvla_l2norm_k07_object_seed42_v2||||0.582|success
eval_xvla_l2norm_k07_spatial_seed42_v2||||72.8|success
eval_xvla_l2norm_k07_spatial_seed42|libero_spatial|||0.72|negative
eval_xvla_l2norm_k095_goal_seed42|libero_goal|||0.538|negative
eval_xvla_l2norm_k095_long_seed42|libero_10|||0.47|negative
eval_xvla_l2norm_k095_spatial_seed42|libero_spatial|||0.716|negative
eval_xvla_l2norm_k09_goal_seed42|libero_goal|||0.702|negative
eval_xvla_l2norm_k09_long_seed42|libero_10|||0.275|negative
eval_xvla_l2norm_k09_spatial_seed42|libero_spatial|||0.788|negative
eval_xvla_prune_k01_seed42||||0|success
eval_xvla_prune_k01_seed43||||0|success
eval_xvla_prune_k01_seed44||||0|success
eval_xvla_prune_k02_seed43||||0.048|success
eval_xvla_prune_k02_seed44||||0.04|success
eval_xvla_prune_k03_seed43||||0.21|success
eval_xvla_prune_k03_seed44||||0.228|success
eval_xvla_prune_k05_seed44||||0.444|success
eval_xvla_prune_k07_seed44||||0.564|success
eval_xvla_prune_k085_seed42||||0.68|success
eval_xvla_prune_k085_seed43|||0.85|0.676|success
eval_xvla_prune_k085_seed44||||0.682|success
eval_xvla_prune_k08_seed42|||0.8|0.888|success
eval_xvla_prune_k08_seed43||||0.884|success
eval_xvla_prune_k08_seed44||||0.898|success
eval_xvla_prune_k095_seed42||||0.99|success
eval_xvla_prune_k095_seed43||||0.99|success
eval_xvla_prune_k095_seed44||||0.994|success
eval_xvla_prune_k09_seed42||||0.992|success
eval_xvla_prune_k09_seed44||||0.982|success
eval_xvla_random_k03_object_seed42|||0.3|62.8|success
eval_xvla_random_k05_goal_seed42_v2||||67.2|success
eval_xvla_random_k05_goal_seed42||||0|failed
eval_xvla_random_k05_goal_seed43_v4||||68.6|success
eval_xvla_random_k05_goal_seed43||||0.672|failed
eval_xvla_random_k05_long_seed42|libero_10|random|0.5|61.6|success
eval_xvla_random_k05_object_seed42||||70.6|success
eval_xvla_random_k05_object_seed43||||0.71|success
eval_xvla_random_k05_object_seed44||||0.692|success
eval_xvla_random_k05_spatial_seed42|libero_spatial|||71.4|success
eval_xvla_random_k05_spatial_seed43||||0.726|success
eval_xvla_random_k07_long_seed42|libero_10|random|0.7|53|success
eval_xvla_random_k07_object_seed42_v2||||65.2|success
eval_xvla_random_k07_object_seed42||||65.2|success
eval_xvla_random_k07_object_seed43_v2||||0.65|success
eval_xvla_random_k085_long_seed42|libero_10||0.85|35|success
eval_xvla_random_k085_object_seed42_v2||||63.6|success
eval_xvla_random_k085_object_seed43||||63.2|success
eval_xvla_random_k08_object_seed42||||89.4|success
eval_xvla_random_k095_long_seed42|libero_10|random|0.95|48.2|success
eval_xvla_random_k095_object_seed42_v2||||0.988|success
eval_xvla_random_k09_long_seed42||||29.6|success
eval_xvla_random_k09_object_seed42||||97.8|success
eval_xvla_spatial_k05_seed42||||0.588|success
eval_xvla_spatial_k085_seed42||||66.6|success
eval_xvla_spatial_k09_seed42||||0.79|success
pi05_baseline_long_seed42||||92.8|success
smolvla_baseline_long_seed42|libero_10|||0.366|success
smolvla_l2norm_k095_goal_seed42|libero_goal|||0.034|negative
smolvla_l2norm_k095_long_seed42|libero_10|||0|negative
smolvla_l2norm_k095_spatial_seed42|libero_spatial|||0.066|negative
smolvla_official_goal_baseline_s42||||0.608|success
smolvla_official_object_l2norm_k095_s42||||0.002|negative
smolvla_official_spatial_baseline_s42||||0.446|success
smolvla_random_k095_goal_seed42|libero_goal|||0.042|negative
smolvla_random_k095_long_seed42|libero_10|||0|negative
smolvla_random_k095_spatial_seed42|libero_spatial|||0.042|negative
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "91b3d5c1-50da-4650-a87b-7ce4afd361f3",
  "uuid": "8030a204-fb12-4ea5-af38-2d03a97bde0c",
  "tool_use_result": {
    "stdout": "baseline_bypass_object||||0.448|success\neval_baseline_control_100k_v2|libero_object|||45|success\neval_baseline_control_prune_k05|libero_object|||0|success\neval_e5_xvla_attn_last_goal_k05_v2||||98.2|success\neval_e5_xvla_attn_last_obj_k03||||84.2|success\neval_e5_xvla_attn_last_spatial_k03||||85.6|success\neval_e5_xvla_attn_mean_goal_k05_v2||||97.4|success\neval_e5_xvla_attn_mean_obj_k03||||96|success\neval_e5_xvla_attn_mean_spatial_k03||||90.4|success\neval_e5_xvla_attn_mean_spatial_k05||||91.6|success\neval_e5_xvla_attn_rollout_goal_k05_v2||||96.8|success\neval_e5_xvla_attn_rollout_obj_k03||||92|success\neval_e5_xvla_attn_rollout_spatial_k05||||92.8|success\neval_e5_xvla_random_goal_k05_v2||||67.2|negative\neval_official_smolvla_baseline||||59.2|success\neval_openvla_attn_k05_goal_seed42||||44.2|success\neval_openvla_attn_k05_long_seed42|libero_10|attention|0.5|14.6|success\neval_openvla_attn_k075_object_seed42||||53.2|success\neval_openvla_attn_k07_goal_seed42||||0.664|negative\neval_openvla_attn_k07_long_seed42_v2||||24|negative\neval_openvla_attn_k07_object_seed42_v3||||43.8|success\neval_openvla_attn_k085_goal_seed42_v3||||74.6|success\neval_openvla_attn_k085_long_seed42_v3|libero_10|||45.8|killed\neval_openvla_attn_k085_long_seed42_v5||||45.8|success\neval_openvla_attn_k085_object_seed42||||0.55|success\neval_openvla_attn_k09_goal_seed42||||0.732|success\neval_openvla_attn_k09_goal_seed43_v4||||73.2|success\neval_openvla_attn_k09_long_seed42_v3|libero_10|||44.0|success\neval_openvla_attn_k09_spatial_seed42||||0.804|success\neval_openvla_baseline_goal_seed42_v3||||74.8|success\neval_openvla_baseline_goal_seed43||||0.776|success\neval_openvla_baseline_long_seed42||||0.528|success\neval_openvla_baseline_object_seed42_v2||||0.74|success\neval_openvla_baseline_object_seed42||||74|success\neval_openvla_baseline_spatial|libero_spatial|||0.8|success\neval_openvla_l2norm_k03_object_seed42||||25.0|success\neval_openvla_l2norm_k03_object_seed43||||25|success\neval_openvla_l2norm_k05_goal_seed42_v3||||0.434|negative\neval_openvla_l2norm_k05_goal_seed42||||0.434|success\neval_openvla_l2norm_k05_object_seed42_v4||||0.392|success\neval_openvla_l2norm_k05_object_seed42||||39.2|success\neval_openvla_l2norm_k05_object_seed43||||39.2|success\neval_openvla_l2norm_k075_goal_seed42_v2||||70.2|success\neval_openvla_l2norm_k075_object_seed42||||0.574|negative\neval_openvla_l2norm_k07_goal_seed42||||0.684|success\neval_openvla_l2norm_k07_long_seed42_v2||||0.312|success\neval_openvla_l2norm_k07_object_seed42_v2||||0.498|success\neval_openvla_l2norm_k07_object_seed42_v3||||0.498|success\neval_openvla_l2norm_k085_goal_seed42||||75.4|success\neval_openvla_l2norm_k085_long_seed42_v2|libero_10_long|||0.388|success\neval_openvla_l2norm_k095_object_seed42||||70.6|success\neval_openvla_l2norm_k09_goal_seed42||||0.748|success\neval_openvla_l2norm_k09_goal_seed43_v3||||0.752|success\neval_openvla_l2norm_k09_goal_seed43||||75.2|success\neval_openvla_l2norm_k09_long_seed42_v3|libero_10|||43.6|success\neval_openvla_l2norm_k09_object_seed42||||0.706|success\neval_openvla_l2norm_k09_spatial_seed42||||0.75|success\neval_openvla_prune_k095|libero_object|||69.4|success\neval_openvla_prune_k09|libero_object|||62|success\neval_openvla_prune_l2norm_k03_seed42|libero_object|||0.25|success\neval_openvla_prune_l2norm_k03||||0.25|success\neval_openvla_prune_l2norm_k05_seed42|libero_object|||0.392|success\neval_openvla_prune_l2norm_k05||||0.392|success\neval_openvla_prune_l2norm_k07_seed43_v2||||49.8|success\neval_openvla_prune_l2norm_k07_seed43||||0.74|failed\neval_openvla_prune_l2norm_k095_seed42|libero_object|||0.706|success\neval_openvla_prune_l2norm_k095||||0.706|success\neval_openvla_prune_l2norm_k09_seed42|libero_object|||0.706|success\neval_openvla_prune_l2norm_k09||||0.706|success\neval_openvla_prune_random_k05_seed42||||35.8|success\neval_openvla_prune_random_k05_seed43_v2||||0.356|success\neval_openvla_prune_random_k07_seed42_v2||||44.4|success\neval_openvla_prune_random_k07_seed43_v2||||0.526|success\neval_openvla_prune_random_k095_seed42_v2||||69.2|success\neval_openvla_prune_random_k095_seed43||||0.668|success\neval_openvla_prune_random_k09_seed42||||0.646|success\neval_openvla_prune_random_k09_seed43||||0.622|success\neval_openvla_pruning_k03_restart||||0.206|success\neval_openvla_pruning_k07||||0.49|success\neval_openvla_random_k05_goal_seed42_v2||||0.522|negative\neval_openvla_random_k05_goal_seed42||||0.522|success\neval_openvla_random_k05_long_seed42_v2||||18.6|negative\neval_openvla_random_k05_object_seed42_v3||||35.8|negative\neval_openvla_random_k05_spatial_seed42||||0.5|success\neval_openvla_random_k075_goal_seed42|libero_goal|random|0.75|72|success\neval_openvla_random_k07_goal_seed42_v4||||68.4|success\neval_openvla_random_k07_long_seed42_v2||||0.388|success\neval_openvla_random_k07_object_seed42_v2||||0.444|success\neval_openvla_random_k07_object_seed43||||0.526|success\neval_openvla_random_k085_goal_seed42||||78.6|success\neval_openvla_random_k085_long_seed42_v3||||0.45|success\neval_openvla_random_k09_goal_seed42||||79.6|success\neval_openvla_random_k09_goal_seed43||||80.4|success\neval_openvla_random_k09_long_seed42_v3|libero_10|||46.8|success\neval_openvla_random_k09_spatial_seed42||||79.8|success\neval_openvla_sc_m128_object_seed42||||0.0|failed\neval_openvla_zeromask_random_k09_object_seed42||||0.718|success\neval_pi05_attention_k05_goal_seed42||||70.2|negative\neval_pi05_attention_k05_goal_seed43||||0.722|negative\neval_pi05_attention_k05_long_seed42_v2||||49.8|success\neval_pi05_attention_k05_spatial_seed42||||0.726|negative\neval_pi05_attention_k075_long_seed42_v2||||52.4|success\neval_pi05_attention_k075_long_seed42||||51.8|success\neval_pi05_attention_k07_long_seed42_v2|libero_10|attention|0.7|50.8|success\neval_pi05_attention_k07_object_seed42|libero_object||0.7|0.006|negative\neval_pi05_attention_k085_long_seed42_v2||||51.6|success\neval_pi05_attention_k085_object_seed42|libero_object|||0.922|success\neval_pi05_attention_k095_object_seed42|libero_object|||0.984|success\neval_pi05_attention_k09_long_seed42_postfix||||0.638|success\neval_pi05_attention_k09_object_seed42|libero_object|||0.972|success\neval_pi05_attn_k095_long_seed42||||77|success\neval_pi05_baseline_goal_seed42||||0.964|success\neval_pi05_baseline_long_seed42||||92.8|success\neval_pi05_baseline_object_seed42||||98.2|success\neval_pi05_baseline_spatial_seed42||||97.2|success\neval_pi05_l2norm_k01_object_seed42||||0.026|success\neval_pi05_l2norm_k03_goal_seed42_postfix||||0.518|success\neval_pi05_l2norm_k03_goal_seed42_v2||||50.6|negative\neval_pi05_l2norm_k03_long_seed42_postfix||||0.366|killed\neval_pi05_l2norm_k03_long_seed43_postfix_v2||||39.2|success\neval_pi05_l2norm_k03_object_seed42||||0.51|success\neval_pi05_l2norm_k03_spatial_seed42_postfix|libero_spatial||0.3|52.8|success\neval_pi05_l2norm_k03_spatial_seed42||||57.2|negative\neval_pi05_l2norm_k05_goal_seed42_postfix||||59.8|success\neval_pi05_l2norm_k05_goal_seed42|libero_goal|||0.592|negative\neval_pi05_l2norm_k05_long_seed42_v3||||51.4|success\neval_pi05_l2norm_k05_long_seed42_v4||||50|success\neval_pi05_l2norm_k05_long_seed42||||0.502|success\neval_pi05_l2norm_k05_long_seed43_postfix_v2||||0.53|success\neval_pi05_l2norm_k05_object_seed42|||0.5|33.4|negative\neval_pi05_l2norm_k05_object_seed43||||0.336|success\neval_pi05_l2norm_k05_spatial_seed42_postfix||||0.574|success\neval_pi05_l2norm_k05_spatial_seed42||||55.6|success\neval_pi05_l2norm_k05_spatial_seed43_v2||||0.554|success\neval_pi05_l2norm_k075_long_seed42||||73.4|success\neval_pi05_l2norm_k07_goal_seed42_postfix||||70.2|success\neval_pi05_l2norm_k07_goal_seed42_v2||||73.6|negative\neval_pi05_l2norm_k07_long_seed42_postfix||||62.6|success\neval_pi05_l2norm_k07_long_seed43_v2||l2norm|0.7|65.8|success\neval_pi05_l2norm_k07_long_seed43_v3||||0.65|success\neval_pi05_l2norm_k07_long_seed43_v4||||0.654|success\neval_pi05_l2norm_k07_object_seed42_postfix||||56.4|success\neval_pi05_l2norm_k07_object_seed42||||55|success\neval_pi05_l2norm_k07_object_seed43||||56.4|success\neval_pi05_l2norm_k07_spatial_seed42||||67|success\neval_pi05_l2norm_k085_goal_seed42_postfix||||87.4|success\neval_pi05_l2norm_k085_goal_seed42|libero_goal||0.85|88|success\neval_pi05_l2norm_k085_goal_seed43_postfix||||87|success\neval_pi05_l2norm_k085_long_seed42_postfix_v3||||0.78|success\neval_pi05_l2norm_k085_long_seed42_postfix||||78.4|success\neval_pi05_l2norm_k085_long_seed42_v3||||78.8|success\neval_pi05_l2norm_k085_long_seed42|libero_10||0.85|0.78|success\neval_pi05_l2norm_k085_long_seed43_postfix||||78.6|success\neval_pi05_l2norm_k085_long_seed43_v2||l2norm|0.85|79|success\neval_pi05_l2norm_k085_long_seed43_v3||||80|success\neval_pi05_l2norm_k085_long_seed43_v4||||0.77|success\neval_pi05_l2norm_k085_object_seed42_postfix_v2||||98.4|success\neval_pi05_l2norm_k085_object_seed42_v4||||0.98|success\neval_pi05_l2norm_k085_object_seed43_postfix||||99|success\neval_pi05_l2norm_k085_spatial_seed42_v2||||88.6|success\neval_pi05_l2norm_k085_spatial_seed42_v3||||88.4|success\neval_pi05_l2norm_k085_spatial_seed43_postfix||||0.882|success\neval_pi05_l2norm_k0925_goal_seed42_postfix||||89.8|success\neval_pi05_l2norm_k0925_goal_seed42_v2||||89|success\neval_pi05_l2norm_k0925_goal_seed42_v3||||89.8|success\neval_pi05_l2norm_k0925_goal_seed43||||90.8|success\neval_pi05_l2norm_k0925_long_seed42_v2||||0.832|success\neval_pi05_l2norm_k0925_object_seed42||||99.2|success\neval_pi05_l2norm_k095_goal_seed42_postfix||||90.8|success\neval_pi05_l2norm_k095_goal_seed42_v2||||89.4|success\neval_pi05_l2norm_k095_goal_seed42||||0.908|negative\neval_pi05_l2norm_k095_long_seed42_postfix|libero_10||0.95|87|success\neval_pi05_l2norm_k095_long_seed43_postfix|libero_10|||87.4|success\neval_pi05_l2norm_k095_object_seed42_v2||||98.2|success\neval_pi05_l2norm_k095_spatial_seed42|libero_spatial|||0.978|success\neval_pi05_l2norm_k09_goal_seed42_postfix||||88.6|success\neval_pi05_l2norm_k09_goal_seed42_v2||||90.6|success\neval_pi05_l2norm_k09_goal_seed42|libero_goal|||0.9|negative\neval_pi05_l2norm_k09_goal_seed43_postfix||||91|success\neval_pi05_l2norm_k09_long_seed42_postfix_v2||||80|success\neval_pi05_l2norm_k09_long_seed43_postfix_v2||||80|success\neval_pi05_l2norm_k09_long_seed43_postfix||||0.808|success\neval_pi05_l2norm_k09_object_seed42_v2||||98.2|success\neval_pi05_l2norm_k09_object_seed43_postfix||||98.4|success\neval_pi05_l2norm_k09_spatial_seed42_postfix||||96|success\neval_pi05_l2norm_k09_spatial_seed43_postfix||||96.2|success\neval_pi05_random_k03_goal_seed42_postfix||||52.8|success\neval_pi05_random_k03_goal_seed42_v2||||50.6|negative\neval_pi05_random_k03_goal_seed43_v2||||53.6|success\neval_pi05_random_k03_long_seed42_postfix||||29.6|success\neval_pi05_random_k03_long_seed42||||0.29|success\neval_pi05_random_k03_long_seed43_v2||||28|success\neval_pi05_random_k03_long_seed43_v3||random|0.3|28.4|success\neval_pi05_random_k03_long_seed43_v4||||0.272|success\neval_pi05_random_k03_object_seed42||||0.364|success\neval_pi05_random_k03_spatial_seed42_postfix_v2||||43.4|success\neval_pi05_random_k03_spatial_seed42||||49.6|success\neval_pi05_random_k05_goal_seed42_postfix||||73.6|success\neval_pi05_random_k05_long_seed42_postfix|libero_10||0.5|46.8|success\neval_pi05_random_k05_long_seed42_v2|libero_10||0.5|46.8|success\neval_pi05_random_k05_long_seed42_v3||||50.2|success\neval_pi05_random_k05_long_seed42||||0.502|success\neval_pi05_random_k05_long_seed43_postfix||||46.8|success\neval_pi05_random_k05_long_seed43_v2||random|0.5|51.2|success\neval_pi05_random_k05_object_seed42||||0.694|success\neval_pi05_random_k05_object_seed43||||68.4|success\neval_pi05_random_k05_spatial_seed42_postfix_v3||||0.718|success\neval_pi05_random_k05_spatial_seed42||||71.6|success\neval_pi05_random_k05_spatial_seed43_v2||||72.4|success\neval_pi05_random_k075_long_seed42_v2|libero_10|||62.4|success\neval_pi05_random_k07_goal_seed42_postfix||||75.6|success\neval_pi05_random_k07_goal_seed42_v2||||78.2|negative\neval_pi05_random_k07_goal_seed42|libero_goal|||0.806|success\neval_pi05_random_k07_long_seed42_postfix|libero_10||0.7|65.8|success\neval_pi05_random_k07_long_seed42|libero_10|random|0.7|62.4|success\neval_pi05_random_k07_long_seed43_postfix||||0.686|success\neval_pi05_random_k07_object_seed42_v4||||74|success\neval_pi05_random_k07_object_seed42||||0.772|success\neval_pi05_random_k07_object_seed43||||73.8|success\neval_pi05_random_k07_spatial_seed42_postfix||||73.8|success\neval_pi05_random_k07_spatial_seed42||||74.4|success\neval_pi05_random_k085_goal_seed42_postfix_v3||||53|success\neval_pi05_random_k085_goal_seed42_postfix||||52.8|success\neval_pi05_random_k085_goal_seed42_v3|libero_goal|||0.524|success\neval_pi05_random_k085_goal_seed42_v4||||52.4|success\neval_pi05_random_k085_goal_seed43_postfix||||0.534|success\neval_pi05_random_k085_goal_seed43|libero_goal||0.85|0.522|negative\neval_pi05_random_k085_long_seed42_postfix_v3||||49.4|success\neval_pi05_random_k085_long_seed42_postfix|libero_10||0.85|45.2|success\neval_pi05_random_k085_long_seed42_v2||||44.4|success\neval_pi05_random_k085_long_seed43_postfix||||0.418|success\neval_pi05_random_k085_long_seed43_v2||||42|success\neval_pi05_random_k085_long_seed43_v3||||0.424|success\neval_pi05_random_k085_long_seed43||random|0.85|41.8|success\neval_pi05_random_k085_object_seed42_postfix||||5.6|success\neval_pi05_random_k085_object_seed42_v2||||5|negative\neval_pi05_random_k085_object_seed43_postfix||||0.048|success\neval_pi05_random_k085_spatial_seed42_postfix_v2||||60.8|success\neval_pi05_random_k085_spatial_seed42_v2||||56.6|success\neval_pi05_random_k085_spatial_seed42_v3||||60.2|success\neval_pi05_random_k085_spatial_seed42|libero_spatial|||0.584|success\neval_pi05_random_k085_spatial_seed43_postfix||||59.2|success\neval_pi05_random_k0925_goal_seed42_v2||||71.2|negative\neval_pi05_random_k0925_goal_seed42_v3||||70|success\neval_pi05_random_k0925_long_seed42_postfix||||38.6|success\neval_pi05_random_k0925_object_seed42_postfix||||27.2|success\neval_pi05_random_k0925_object_seed42||||0.276|negative\neval_pi05_random_k0925_object_seed43|libero_object|||0.3|success\neval_pi05_random_k0925_spatial_seed42_unreg||||58.2|success\neval_pi05_random_k095_goal_seed42_postfix||||82.6|success\neval_pi05_random_k095_goal_seed42_v2||||83.8|success\neval_pi05_random_k095_goal_seed43|libero_goal||0.95|0.834|success\neval_pi05_random_k095_long_seed42_postfix|libero_10||0.95|63.2|success\neval_pi05_random_k095_long_seed42|libero_10||0.95|0.612|success\neval_pi05_random_k095_long_seed43_postfix||||0.584|success\neval_pi05_random_k095_object_seed42_v2||||74|success\neval_pi05_random_k095_object_seed43||||0.728|success\neval_pi05_random_k095_spatial_seed42_postfix_v2||||76.8|success\neval_pi05_random_k09_fixedmask_object_seed42_v2||||0.17|negative\neval_pi05_random_k09_goal_seed42_postfix||||61.8|success\neval_pi05_random_k09_goal_seed42_v2||||62.2|negative\neval_pi05_random_k09_goal_seed43_postfix||||61.2|success\neval_pi05_random_k09_long_seed42_postfix||||32|success\neval_pi05_random_k09_long_seed43_postfix||||0.356|killed\neval_pi05_random_k09_object_seed43_postfix||||7.4|success\neval_pi05_random_k09_object_seed43_v3||||9.6|success\neval_pi05_random_k09_object_seed43_v4|libero_object|random|0.9|9.6|success\neval_pi05_random_k09_object_seed43||||0.096|success\neval_pi05_random_k09_spatial_seed42_postfix_v2||||53.4|negative\neval_pi05_random_k09_spatial_seed43_postfix_v2||||54|success\neval_pi05_zeromask_l2norm_k09_object_seed42||||0.994|success\neval_pi05_zeromask_random_k09_object_seed42_v3||||0.98|success\neval_smart_compress_m128_seed43|libero_object|||0.54|success\neval_smart_compress_m16_seed43|libero_object|||0.584|success\neval_smart_compress_m16_seed44|libero_object|||0.565|success\neval_smart_compress_m16||||55.8|success\neval_smart_compress_m32_libero_goal|libero_goal|||56.4|success\neval_smart_compress_m32_libero_spatial|libero_spatial|||53.2|success\neval_smart_compress_m32_seed43|libero_object|||59.2|success\neval_smart_compress_m32_seed44||||59.6|success\neval_smart_compress_m32||||0.616|success\neval_smart_compress_m64_seed43|libero_object|||60|success\neval_smart_compress_m64_seed44||||64.4|success\neval_smart_compress_m64||||0.616|success\neval_smart_compress_m96_seed43_v2|libero_object|||58.2|success\neval_smart_compress_m96_seed43|libero_object|||0|failed\neval_smart_compress_m96_seed44||||52.8|success\neval_smart_compress_m96||||52.6|success\neval_smolvla_baseline_spatial_westd38929_seed42||||8.0|success\neval_smolvla_metaworld_baseline||||26.4|success\neval_smolvla_official_baseline_object_seed42||||57.2|success\neval_smolvla_official_l2norm_k050_object_seed42||||0|success\neval_smolvla_official_l2norm_k095_object_seed42||||0.4|success\neval_smolvla_official_random_k095_object_seed42||||0|success\neval_smolvla_zeromask_l2norm_k095_object_seed42||||0|negative\neval_smolvla_zeromask_random_k095_object_seed42||||0.002|negative\neval_xvla_baseline_goal_seed42||||0.984|success\neval_xvla_baseline_long_seed42|libero_10|||0.94|success\neval_xvla_baseline_spatial_seed42||||0.93|success\neval_xvla_goal_k05_seed42|libero_goal|||0.61|success\neval_xvla_goal_k09_seed42|libero_goal|||0.702|success\neval_xvla_l2norm_k03_goal_seed42_v3||||0.376|negative\neval_xvla_l2norm_k03_goal_seed42_v4||||37.6|negative\neval_xvla_l2norm_k03_goal_seed42_v5||||0.37|success\neval_xvla_l2norm_k03_object_seed42||||0.222|success\neval_xvla_l2norm_k03_spatial_seed42||||0.312|negative\neval_xvla_l2norm_k05_goal_seed42_v2|libero_goal||0.5|0.59|success\neval_xvla_l2norm_k05_goal_seed42_v3||||59|negative\neval_xvla_l2norm_k05_long_seed42_v4||||44.6|success\neval_xvla_l2norm_k05_long_seed42||||45|success\neval_xvla_l2norm_k05_object_seed42||||0.434|success\neval_xvla_l2norm_k05_spatial_seed42_v3||||58.8|negative\neval_xvla_l2norm_k05_spatial_seed43||||59|negative\neval_xvla_l2norm_k07_goal_seed42|libero_goal|||0.534|negative\neval_xvla_l2norm_k07_object_seed42_v2||||0.582|success\neval_xvla_l2norm_k07_spatial_seed42_v2||||72.8|success\neval_xvla_l2norm_k07_spatial_seed42|libero_spatial|||0.72|negative\neval_xvla_l2norm_k095_goal_seed42|libero_goal|||0.538|negative\neval_xvla_l2norm_k095_long_seed42|libero_10|||0.47|negative\neval_xvla_l2norm_k095_spatial_seed42|libero_spatial|||0.716|negative\neval_xvla_l2norm_k09_goal_seed42|libero_goal|||0.702|negative\neval_xvla_l2norm_k09_long_seed42|libero_10|||0.275|negative\neval_xvla_l2norm_k09_spatial_seed42|libero_spatial|||0.788|negative\neval_xvla_prune_k01_seed42||||0|success\neval_xvla_prune_k01_seed43||||0|success\neval_xvla_prune_k01_seed44||||0|success\neval_xvla_prune_k02_seed43||||0.048|success\neval_xvla_prune_k02_seed44||||0.04|success\neval_xvla_prune_k03_seed43||||0.21|success\neval_xvla_prune_k03_seed44||||0.228|success\neval_xvla_prune_k05_seed44||||0.444|success\neval_xvla_prune_k07_seed44||||0.564|success\neval_xvla_prune_k085_seed42||||0.68|success\neval_xvla_prune_k085_seed43|||0.85|0.676|success\neval_xvla_prune_k085_seed44||||0.682|success\neval_xvla_prune_k08_seed42|||0.8|0.888|success\neval_xvla_prune_k08_seed43||||0.884|success\neval_xvla_prune_k08_seed44||||0.898|success\neval_xvla_prune_k095_seed42||||0.99|success\neval_xvla_prune_k095_seed43||||0.99|success\neval_xvla_prune_k095_seed44||||0.994|success\neval_xvla_prune_k09_seed42||||0.992|success\neval_xvla_prune_k09_seed44||||0.982|success\neval_xvla_random_k03_object_seed42|||0.3|62.8|success\neval_xvla_random_k05_goal_seed42_v2||||67.2|success\neval_xvla_random_k05_goal_seed42||||0|failed\neval_xvla_random_k05_goal_seed43_v4||||68.6|success\neval_xvla_random_k05_goal_seed43||||0.672|failed\neval_xvla_random_k05_long_seed42|libero_10|random|0.5|61.6|success\neval_xvla_random_k05_object_seed42||||70.6|success\neval_xvla_random_k05_object_seed43||||0.71|success\neval_xvla_random_k05_object_seed44||||0.692|success\neval_xvla_random_k05_spatial_seed42|libero_spatial|||71.4|success\neval_xvla_random_k05_spatial_seed43||||0.726|success\neval_xvla_random_k07_long_seed42|libero_10|random|0.7|53|success\neval_xvla_random_k07_object_seed42_v2||||65.2|success\neval_xvla_random_k07_object_seed42||||65.2|success\neval_xvla_random_k07_object_seed43_v2||||0.65|success\neval_xvla_random_k085_long_seed42|libero_10||0.85|35|success\neval_xvla_random_k085_object_seed42_v2||||63.6|success\neval_xvla_random_k085_object_seed43||||63.2|success\neval_xvla_random_k08_object_seed42||||89.4|success\neval_xvla_random_k095_long_seed42|libero_10|random|0.95|48.2|success\neval_xvla_random_k095_object_seed42_v2||||0.988|success\neval_xvla_random_k09_long_seed42||||29.6|success\neval_xvla_random_k09_object_seed42||||97.8|success\neval_xvla_spatial_k05_seed42||||0.588|success\neval_xvla_spatial_k085_seed42||||66.6|success\neval_xvla_spatial_k09_seed42||||0.79|success\npi05_baseline_long_seed42||||92.8|success\nsmolvla_baseline_long_seed42|libero_10|||0.366|success\nsmolvla_l2norm_k095_goal_seed42|libero_goal|||0.034|negative\nsmolvla_l2norm_k095_long_seed42|libero_10|||0|negative\nsmolvla_l2norm_k095_spatial_seed42|libero_spatial|||0.066|negative\nsmolvla_official_goal_baseline_s42||||0.608|success\nsmolvla_official_object_l2norm_k095_s42||||0.002|negative\nsmolvla_official_spatial_baseline_s42||||0.446|success\nsmolvla_random_k095_goal_seed42|libero_goal|||0.042|negative\nsmolvla_random_k095_long_seed42|libero_10|||0|negative\nsmolvla_random_k095_spatial_seed42|libero_spatial|||0.042|negative",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Assistant

_source line 88_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data. Let me focus on building the OpenVLA cliff curves for the three suites: Object, Goal, and Long (libero_10).

Let me organize the data. I need to be careful about which value to use, as some entries have values like 0.xxx (fractions) and others have values like xx.x (percentages). I need to normalize them all to percentages.

Let me parse out the OpenVLA experiments for each suite and method.

**OpenVLA Object Cliff Curve:**
Baseline: eval_openvla_baseline_object_seed42_v2 = 0.74 → 74% or eval_openvla_baseline_object_seed42 = 74%


L2norm: k=0.3 gives 25%, k=0.5 gives 39.2%, and k=0.7 reaches 49.8%.

Now I'm noticing some inconsistency in the experiment naming—I need to double-check whether k=0.85 is actually an L2norm variant or if that's from the attention experiments instead. Let me organize these object-level results more carefully to make sure I'm comparing the right metrics. Looking at the attention-based pruning results, I'm seeing performance across different sparsity levels with k=0.7 at 43.8%, k=0.75 at 53.2%, and k=0.85 at 55%, though there's some inconsistency in the naming conventions between goal and object metrics. The random pruning baseline shows k=0.5 achieving 35.8%, which is notably lower than the structured approaches.

Now I'm realizing the evaluation scope needs to be clarified—the user specifically wants OpenVLA cliff curves across three benchmark suites: Object, Goal, and Long (libero_10), so I should focus on collecting the most relevant results for those three categories rather than getting lost in all these intermediate experimental variations. Let me continue tracking the attention-based pruning results. The k=0.9 variant achieved 44%, and I'm still waiting on the k=0.95 run to complete, along with several other in-progress experiments across different k values. Now I'm looking at the L2norm results for the goal-conditioned evaluations, where the baseline achieves 74.8%. The performance varies significantly across different k values, with k=0.85 showing the strongest result at 75.4%, while k=0.9 appears to have an issue with a zero value that needs investigation. Looking at the random sampling results, I'm seeing performance improvements as k increases, with k=0.85 hitting 78.6%, k=0.9 at 79.6%, and k=0.95 still running.

Now examining the object cliff curve across different pruning methods—L2norm shows steady gains from 25% at k=0.3 up to 70.6% at k=0.9 and k=0.95, while attention-based pruning reaches 55% at k=0.85 with k=0.95 still evaluating, and random sampling gets to 64.6% at k=0.9.

Looking more carefully at the random pruning results, I'm seeing 69.2% for k=0.95 from one experiment and 71.8% from a zeromask variant, but I need to exclude the zeromask results since they're a different method. Checking the naming conventions, some of the earlier "eval_openvla_prune_*" experiments are actually from the object suite—I'm verifying which results are directly comparable, noting that k=0.95 shows around 69.4% and k=0.9 shows 62% when explicitly run on the libero_object suite. Now I'm seeing the full picture of how performance degrades across different pruning ratios. The L2 norm pruning shows a clear progression where performance stays relatively flat until around k=0.9, then plateaus, while the attention-based pruning follows a similar but slightly different curve with more gradual degradation across the middle range. Generating markdown tables...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "91b3d5c1-50da-4650-a87b-7ce4afd361f3",
  "uuid": "903111a2-6dcd-4a74-b6a5-6723b300ebf1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CDT7bBEbegWXaMYZppYvTh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10005,
      "cache_read_input_tokens": 64212,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10005
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Assistant

_source line 89_

所有 3 个已完成实验已收割，3 个"未注册"实验实际均已在 registry 中。现在汇总 cliff curve 数据。

---

## 任务 1 结果：3 个实验收割完毕

| 实验 | Overall SR | 状态 |
|------|-----------|------|
| eval_openvla_attn_k05_long_seed42 | **14.6%** (73/500) | DONE ✅ |
| eval_pi05_random_k07_long_seed42 | **62.4%** (312/500) | DONE ✅ |
| eval_openvla_random_k075_goal_seed42 | **72.0%** (360/500) | DONE ✅ |

## 任务 2 结果：注册检查

3 个指定实验均已在 registry 中存在（非新发现的未注册实验）：
- `eval_openvla_attn_k07_long_seed42_v2` — DONE, 24.0%
- `eval_openvla_l2norm_k075_long_seed42` — DONE (failed/timeout), 仍在重跑中
- `eval_openvla_random_k05_object_seed42_v2` — DONE (killed)

当前 RUNNING 实验 12 个，全部已注册。

## 任务 3：OpenVLA Cliff Curves

### OpenVLA Long (LIBERO-10) Cliff Curve
| k | L2norm | Attn | Random | Baseline |
|---|--------|------|--------|----------|
| 0.50 | — | 14.6% | 18.6% | 52.8% |
| 0.70 | 31.2% | 24.0% | 38.8% | 52.8% |
| 0.75 | 🏃 running | 🏃 running | 🏃 running | 52.8% |
| 0.85 | 38.8% | 45.8% | 45.0% | 52.8% |
| 0.90 | 43.6% | 44.0% | 46.8% | 52.8% |
| 0.95 | 🏃 running | 🏃 running | 🏃 running | 52.8% |

### OpenVLA Goal Cliff Curve
| k | L2norm | Attn | Random | Baseline |
|---|--------|------|--------|----------|
| 0.50 | 43.4% | 44.2% | 52.2% | 74.8% |
| 0.70 | 68.4% | 66.4% | 68.4% | 74.8% |
| 0.75 | 70.2% | — | **72.0%** | 74.8% |
| 0.85 | 75.4% | 74.6% | 78.6% | 74.8% |
| 0.90 | 74.8% | 73.2% | 79.6% | 74.8% |
| 0.95 | 🏃 running | 🏃 running | 🏃 running | 74.8% |

### OpenVLA Object Cliff Curve
| k | L2norm | Attn | Random | Baseline |
|---|--------|------|--------|----------|
| 0.30 | 25.0% | — | — | 74.0% |
| 0.50 | 39.2% | — | 35.8% | 74.0% |
| 0.70 | 49.8% | 43.8% | 44.4% | 74.0% |
| 0.75 | 57.4% | 53.2% | — | 74.0% |
| 0.85 | — | 55.0% | — | 74.0% |
| 0.90 | 70.6% | — | 64.6% | 74.0% |
| 0.95 | 70.6% | 🏃 running | 🏃 running | 74.0% |

---

**关键观察：**
- **Goal Random** cliff：k=0.75 → 72.0% 填入后，斜率清晰：79.6% → 78.6% → 72.0% → 68.4%，下降主要在 k=0.85→0.75 区间（6.6pp drop）
- **Long** suite 三种方法在 k=0.85~0.9 趋于收敛（43.6~46.8%），离 baseline 52.8% 仍有 gap
- **Goal Random 在 k≥0.85 超过 baseline**（78.6~79.6% vs 74.8%），暗示 moderate random pruning 可能有正则化效果
- k=0.75 和 k=0.95 的 Long/Goal/Object 数据点正在跑，预计 3-6h 内完成

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "91b3d5c1-50da-4650-a87b-7ce4afd361f3",
  "uuid": "e599ad56-99d2-401e-96e4-15019b369741",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CDT7bBEbegWXaMYZppYvTh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10005,
      "cache_read_input_tokens": 64212,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10005
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Task result

_source line 90_

所有 3 个已完成实验已收割，3 个"未注册"实验实际均已在 registry 中。现在汇总 cliff curve 数据。

---

## 任务 1 结果：3 个实验收割完毕

| 实验 | Overall SR | 状态 |
|------|-----------|------|
| eval_openvla_attn_k05_long_seed42 | **14.6%** (73/500) | DONE ✅ |
| eval_pi05_random_k07_long_seed42 | **62.4%** (312/500) | DONE ✅ |
| eval_openvla_random_k075_goal_seed42 | **72.0%** (360/500) | DONE ✅ |

## 任务 2 结果：注册检查

3 个指定实验均已在 registry 中存在（非新发现的未注册实验）：
- `eval_openvla_attn_k07_long_seed42_v2` — DONE, 24.0%
- `eval_openvla_l2norm_k075_long_seed42` — DONE (failed/timeout), 仍在重跑中
- `eval_openvla_random_k05_object_seed42_v2` — DONE (killed)

当前 RUNNING 实验 12 个，全部已注册。

## 任务 3：OpenVLA Cliff Curves

### OpenVLA Long (LIBERO-10) Cliff Curve
| k | L2norm | Attn | Random | Baseline |
|---|--------|------|--------|----------|
| 0.50 | — | 14.6% | 18.6% | 52.8% |
| 0.70 | 31.2% | 24.0% | 38.8% | 52.8% |
| 0.75 | 🏃 running | 🏃 running | 🏃 running | 52.8% |
| 0.85 | 38.8% | 45.8% | 45.0% | 52.8% |
| 0.90 | 43.6% | 44.0% | 46.8% | 52.8% |
| 0.95 | 🏃 running | 🏃 running | 🏃 running | 52.8% |

### OpenVLA Goal Cliff Curve
| k | L2norm | Attn | Random | Baseline |
|---|--------|------|--------|----------|
| 0.50 | 43.4% | 44.2% | 52.2% | 74.8% |
| 0.70 | 68.4% | 66.4% | 68.4% | 74.8% |
| 0.75 | 70.2% | — | **72.0%** | 74.8% |
| 0.85 | 75.4% | 74.6% | 78.6% | 74.8% |
| 0.90 | 74.8% | 73.2% | 79.6% | 74.8% |
| 0.95 | 🏃 running | 🏃 running | 🏃 running | 74.8% |

### OpenVLA Object Cliff Curve
| k | L2norm | Attn | Random | Baseline |
|---|--------|------|--------|----------|
| 0.30 | 25.0% | — | — | 74.0% |
| 0.50 | 39.2% | — | 35.8% | 74.0% |
| 0.70 | 49.8% | 43.8% | 44.4% | 74.0% |
| 0.75 | 57.4% | 53.2% | — | 74.0% |
| 0.85 | — | 55.0% | — | 74.0% |
| 0.90 | 70.6% | — | 64.6% | 74.0% |
| 0.95 | 70.6% | 🏃 running | 🏃 running | 74.0% |

---

**关键观察：**
- **Goal Random** cliff：k=0.75 → 72.0% 填入后，斜率清晰：79.6% → 78.6% → 72.0% → 68.4%，下降主要在 k=0.85→0.75 区间（6.6pp drop）
- **Long** suite 三种方法在 k=0.85~0.9 趋于收敛（43.6~46.8%），离 baseline 52.8% 仍有 gap
- **Goal Random 在 k≥0.85 超过 baseline**（78.6~79.6% vs 74.8%），暗示 moderate random pruning 可能有正则化效果
- k=0.75 和 k=0.95 的 Long/Goal/Object 数据点正在跑，预计 3-6h 内完成

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 618621,
  "duration_api_ms": 313566,
  "num_turns": 32,
  "stop_reason": "end_turn",
  "session_id": "91b3d5c1-50da-4650-a87b-7ce4afd361f3",
  "total_cost_usd": 1.1393335,
  "usage": {
    "input_tokens": 17,
    "cache_creation_input_tokens": 62376,
    "cache_read_input_tokens": 584873,
    "output_tokens": 18195,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 62376,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 5058,
        "cache_read_input_tokens": 64212,
        "cache_creation_input_tokens": 10005,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 10005
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1992,
      "outputTokens": 19,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002087,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 17,
      "outputTokens": 18195,
      "cacheReadInputTokens": 584873,
      "cacheCreationInputTokens": 62376,
      "webSearchRequests": 0,
      "costUSD": 1.1372464999999998,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "15a65979-cf9b-4318-bc5c-cc3b2589ba3a"
}
```

</details>

---
