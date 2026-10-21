# infra scan all servers process status

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 0
- **Tool calls:** 9
- **Original source:** `logs/chats/worker_infra_scan-all-servers-process-status_20260523T212704.jsonl`
- **Structured JSON:** [`0cc8c50fcbe1a7db76eb.json`](../../sessions/0c/0cc8c50fcbe1a7db76eb.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

19 recorded events

### Tool call

_source line 1 · 2026-05-23T21:30:18.723238+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__detect_image",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_infra_scan-all-servers-process-status_20260523T212704",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__detect_image",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-23T21:30:18.723653+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_infra_scan-all-servers-process-status_20260523T212704",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-23T21:30:18.723868+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb2-28827",
  "command": "echo \"=== GPU COMPUTE APPS ===\" && nvidia-smi --query-compute-apps=pid,gpu_uuid,used_memory --format=csv,noheader && echo \"=== GPU STATUS ===\" && nvidia-smi --query-gpu=index,name,memory.used,memory.total,utilization.gpu --format=csv,noheader && echo \"=== EVALUATE PROCESSES ===\" && ps aux | grep 'evaluate.py' | grep -v grep && echo \"=== TMUX ===\" && tmux ls 2>/dev/null; echo \"=== SPECIFIC PIDs ===\" && ps -p 924226,850410 -o pid,cmd --no-header 2>/dev/null; echo \"=== DONE ===\"",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_infra_scan-all-servers-process-status_20260523T212704",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb2-28827",
    "command": "echo \"=== GPU COMPUTE APPS ===\" && nvidia-smi --query-compute-apps=pid,gpu_uuid,used_memory --format=csv,noheader && echo \"=== GPU STATUS ===\" && nvidia-smi --query-gpu=index,name,memory.used,memory.total,utilization.gpu --format=csv,noheader && echo \"=== EVALUATE PROCESSES ===\" && ps aux | grep 'evaluate.py' | grep -v grep && echo \"=== TMUX ===\" && tmux ls 2>/dev/null; echo \"=== SPECIFIC PIDs ===\" && ps -p 924226,850410 -o pid,cmd --no-header 2>/dev/null; echo \"=== DONE ===\"",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-23T21:30:18.724070+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== GPU COMPUTE APPS ===\\n926766, GPU-d7423c53-447e-0c0f-dd10-076e4989d991, 3685 MiB\\n927030, GPU-3ca0dfcc-ade3-2eb8-0f77-59f6aae6ac44, 4235 MiB\\n927237, GPU-cd6008a7-b242-51e0-5f10-49dfd6d5651d, 3747 MiB\\n849677, GPU-a0d22891-1964-0f75-4962-81994416abaf, 1755 MiB\\n924226, GPU-54175474-0aa4-3553-ee7c-968cb4b0f9ad, 5591 MiB\\n850410, GPU-e78bc8c3-4047-7933-7882-9f404fae347f, 2307 MiB\\n=== GPU STATUS ===\\n0, NVIDIA GeForce RTX 4090, 3704 MiB, 24564 MiB, 19 %\\n1, NVIDIA GeForce RTX 4090, 4253 MiB, 24564 MiB, 22 %\\n2, NVIDIA GeForce RTX 4090, 3766 MiB, 24564 MiB, 28 %\\n3, NVIDIA GeForce RTX 4090, 1765 MiB, 24564 MiB, 0 %\\n4, NVIDIA GeForce RTX 4090, 5610 MiB, 24564 MiB, 18 %\\n5, NVIDIA GeForce RTX 4090, 2326 MiB, 24564 MiB, 22 %\\n=== EVALUATE PROCESSES ===\\nroot     849124  0.0  0.0   6128  3916 ?        Ss   01:26   0:00 tmux new-session -d -s eval-supp-adapt-tau025-obj-s45 source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark object --mode adaptive_conformal_crm --seed 45 --n_rollouts 20 --max_correction_norm 0.2 --conformal_threshold 0.25 --K 2 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt 2>&1 | tee ~/runs/acr-vla-conformal-refinement/eval-supp-adapt-tau025-obj-s45.log\\nroot     849671  0.0  0.0   4364  3164 pts/3    Ss+  01:26   0:00 bash -c source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py --benchmark long --mode reconvla --seed 44 --n_rollouts 20 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt 2>&1 | tee ~/runs/acr-vla-conformal-refinement/eval-supp-long-reconvla-s44.log\\nroot     849677  563  0.9 64001340 10362120 pts/3 Sl+ 01:26 1360:07 python -u src/evaluate.py --benchmark long --mode rec
…[truncated 3656 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_infra_scan-all-servers-process-status_20260523T212704",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-23T21:30:18.724244+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-32546",
  "command": "echo \"=== GPU COMPUTE APPS ===\" && nvidia-smi --query-compute-apps=pid,gpu_uuid,used_memory --format=csv,noheader && echo \"=== GPU STATUS ===\" && nvidia-smi --query-gpu=index,name,memory.used,memory.total,utilization.gpu --format=csv,noheader && echo \"=== EVALUATE PROCESSES ===\" && ps aux | grep 'evaluate.py' | grep -v grep && echo \"=== TMUX ===\" && tmux ls 2>/dev/null; echo \"=== DONE ===\"",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_infra_scan-all-servers-process-status_20260523T212704",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "echo \"=== GPU COMPUTE APPS ===\" && nvidia-smi --query-compute-apps=pid,gpu_uuid,used_memory --format=csv,noheader && echo \"=== GPU STATUS ===\" && nvidia-smi --query-gpu=index,name,memory.used,memory.total,utilization.gpu --format=csv,noheader && echo \"=== EVALUATE PROCESSES ===\" && ps aux | grep 'evaluate.py' | grep -v grep && echo \"=== TMUX ===\" && tmux ls 2>/dev/null; echo \"=== DONE ===\"",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-23T21:30:18.724499+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== GPU COMPUTE APPS ===\\n102927, GPU-220671b6-4e9c-db2d-1361-6ed090a1f3af, 3389 MiB\\n103128, GPU-ade291cb-7e13-f292-1714-09ef80919436, 4911 MiB\\n103397, GPU-4f00bf04-f4ff-96b6-3f56-723337f44abf, 4917 MiB\\n103675, GPU-00ae24f3-53b1-cd05-f561-fe7adbb64e72, 5011 MiB\\n103942, GPU-563702d3-df96-d375-0303-c9b9f202bdd2, 4973 MiB\\n104216, GPU-6d1331f1-8f19-df6c-71d5-e8ca2f3e2178, 2786 MiB\\n=== GPU STATUS ===\\n0, NVIDIA GeForce RTX 4090, 3409 MiB, 24564 MiB, 33 %\\n1, NVIDIA GeForce RTX 4090, 4931 MiB, 24564 MiB, 21 %\\n2, NVIDIA GeForce RTX 4090, 4937 MiB, 24564 MiB, 23 %\\n3, NVIDIA GeForce RTX 4090, 5031 MiB, 24564 MiB, 24 %\\n4, NVIDIA GeForce RTX 4090, 4993 MiB, 24564 MiB, 31 %\\n5, NVIDIA GeForce RTX 4090, 2806 MiB, 24564 MiB, 22 %\\n=== EVALUATE PROCESSES ===\\nroot     102924  0.0  0.0   6164  3872 ?        Ss   04:11   0:00 tmux new-session -d -s eval-crm-obj-s46 CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark object --mode crm_obs_only --seed 46 --n_rollouts 20 --max_correction_norm 0.05 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt 2>&1 | tee /tmp/eval_crm_obj_s46.log\\nroot     102925  0.0  0.0   4364  3284 pts/0    Ss+  04:11   0:00 bash -c CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark object --mode crm_obs_only --seed 46 --n_rollouts 20 --max_correction_norm 0.05 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt 2>&1 | tee /tmp/eval_crm_obj_s46.log\\nroot     102927  362  1.0 66772692 10824356 pts/0 Rl+ 04:11 277:43 python -u src/evaluate.py --benchmark object --mode crm_obs_only --seed 46 --n_rollouts 20 --max_correction_norm 0.05 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\nroot     103126  0.0  0.0   4364  3192 pts/1    Ss+  04:11   0:00 bash -c CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --benchmark long --mode vla_only --seed 45 --n_rollout
…[truncated 3282 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_infra_scan-all-servers-process-status_20260523T212704",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-23T21:30:18.724660+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-32758",
  "command": "echo \"=== GPU COMPUTE APPS ===\" && nvidia-smi --query-compute-apps=pid,gpu_uuid,used_memory --format=csv,noheader && echo \"=== GPU STATUS ===\" && nvidia-smi --query-gpu=index,name,memory.used,memory.total,utilization.gpu --format=csv,noheader && echo \"=== EVALUATE PROCESSES ===\" && ps aux | grep 'evaluate.py' | grep -v grep && echo \"=== TMUX ===\" && tmux ls 2>/dev/null; echo \"=== SPECIFIC PIDs ===\" && ps -p 291523,291315 -o pid,cmd --no-header 2>/dev/null; echo \"=== DONE ===\"",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_infra_scan-all-servers-process-status_20260523T212704",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-32758",
    "command": "echo \"=== GPU COMPUTE APPS ===\" && nvidia-smi --query-compute-apps=pid,gpu_uuid,used_memory --format=csv,noheader && echo \"=== GPU STATUS ===\" && nvidia-smi --query-gpu=index,name,memory.used,memory.total,utilization.gpu --format=csv,noheader && echo \"=== EVALUATE PROCESSES ===\" && ps aux | grep 'evaluate.py' | grep -v grep && echo \"=== TMUX ===\" && tmux ls 2>/dev/null; echo \"=== SPECIFIC PIDs ===\" && ps -p 291523,291315 -o pid,cmd --no-header 2>/dev/null; echo \"=== DONE ===\"",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-23T21:30:18.724817+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== GPU COMPUTE APPS ===\\n380176, GPU-8558c50e-663f-e3d6-81d5-75e1eca928a4, 2183 MiB\\n377316, GPU-6387c137-7bb7-0b31-62aa-a9d053c1131b, 2183 MiB\\n=== GPU STATUS ===\\n0, NVIDIA GeForce RTX 4090 D, 1 MiB, 24564 MiB, 0 %\\n1, NVIDIA GeForce RTX 4090 D, 1 MiB, 24564 MiB, 0 %\\n2, NVIDIA GeForce RTX 4090 D, 2201 MiB, 24564 MiB, 32 %\\n3, NVIDIA GeForce RTX 4090 D, 1 MiB, 24564 MiB, 0 %\\n4, NVIDIA GeForce RTX 4090 D, 2201 MiB, 24564 MiB, 47 %\\n5, NVIDIA GeForce RTX 4090 D, 1 MiB, 24564 MiB, 0 %\\n=== EVALUATE PROCESSES ===\\nroot      16395  0.0  0.0   6528  4240 ?        Ss   May23   0:01 tmux new-session -d -s k2mean_spatial_s43 source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl HF_HOME=/root/autodl-tmp/.hf_cache python src/evaluate.py --smolvla_path /root/autodl-tmp/models/smolvla_libero/ --mode vla_only --baseline_mode mean --K 2 --benchmark spatial --seed 43 --n_rollouts 20 --output_file logs/eval_k2mean_spatial_seed43.json 2>&1 | tee logs/eval_k2mean_spatial_seed43.log\\nroot     377314  0.0  0.0   4364  3036 pts/2    Ss+  02:37   0:00 bash -c CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --benchmark object --mode reconvla --seed 45 --n_rollouts 20 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt 2>&1 | tee /tmp/eval_reconvla_obj_s45.log\\nroot     377316  835  1.0 62905484 10971640 pts/2 Rl+ 02:37 1424:04 python -u src/evaluate.py --benchmark object --mode reconvla --seed 45 --n_rollouts 20 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\nroot     380174  0.0  0.0   4364  2940 pts/4    Ss+  02:40   0:00 bash -c CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --benchmark object --mode reconvla --seed 46 --n_rollouts 20 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt 2>&1 | tee /tmp/eval_reconvla_obj_s46.log\\nroot     380176  82
…[truncated 523 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_infra_scan-all-servers-process-status_20260523T212704",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-23T21:30:18.724969+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb2-40593",
  "command": "echo \"=== GPU COMPUTE APPS ===\" && nvidia-smi --query-compute-apps=pid,gpu_uuid,used_memory --format=csv,noheader && echo \"=== GPU STATUS ===\" && nvidia-smi --query-gpu=index,name,memory.used,memory.total,utilization.gpu --format=csv,noheader && echo \"=== EVALUATE PROCESSES ===\" && ps aux | grep 'evaluate.py' | grep -v grep && echo \"=== TMUX ===\" && tmux ls 2>/dev/null; echo \"=== DONE ===\"",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_infra_scan-all-servers-process-status_20260523T212704",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb2-40593",
    "command": "echo \"=== GPU COMPUTE APPS ===\" && nvidia-smi --query-compute-apps=pid,gpu_uuid,used_memory --format=csv,noheader && echo \"=== GPU STATUS ===\" && nvidia-smi --query-gpu=index,name,memory.used,memory.total,utilization.gpu --format=csv,noheader && echo \"=== EVALUATE PROCESSES ===\" && ps aux | grep 'evaluate.py' | grep -v grep && echo \"=== TMUX ===\" && tmux ls 2>/dev/null; echo \"=== DONE ===\"",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-23T21:30:18.725126+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== GPU COMPUTE APPS ===\\n177824, GPU-a7c79137-3a96-7036-cedf-aaeda2b1fd1d, 2688 MiB\\n=== GPU STATUS ===\\n0, NVIDIA GeForce RTX 4090 D, 2706 MiB, 24564 MiB, 21 %\\n=== EVALUATE PROCESSES ===\\nroot     177821  0.0  0.0   5988  3632 ?        Ss   02:14   0:00 tmux new-session -d -s eval-crm-obj-s45 CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark object --mode crm_obs_only --seed 45 --n_rollouts 20 --max_correction_norm 0.05 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt 2>&1 | tee /tmp/eval_crm_obj_s45.log\\nroot     177822  0.0  0.0   4364  3196 pts/0    Ss+  02:14   0:00 bash -c CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark object --mode crm_obs_only --seed 45 --n_rollouts 20 --max_correction_norm 0.05 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt 2>&1 | tee /tmp/eval_crm_obj_s45.log\\nroot     177824  387  1.7 38675344 9446016 pts/0 Rl+ 02:14 747:42 python -u src/evaluate.py --benchmark object --mode crm_obs_only --seed 45 --n_rollouts 20 --max_correction_norm 0.05 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt\\n=== TMUX ===\\neval-crm-obj-s45: 1 windows (created Sun May 24 02:14:51 2026)\\n=== DONE ===\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.93}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_infra_scan-all-servers-process-status_20260523T212704",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-23T21:30:18.725347+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-32758",
  "command": "echo \"=== LOG FILES ===\" && ls -lt /tmp/eval_*.log ~/runs/acr-vla-conformal-refinement/*.log 2>/dev/null | head -20 && echo \"=== k2mean_obj_s46 ===\" && tail -20 /tmp/eval_k2mean_obj_s46.log 2>/dev/null || echo \"NOT_FOUND\" && echo \"=== k2mean_obj_s45 ===\" && tail -20 /tmp/eval_k2mean_obj_s45.log 2>/dev/null || echo \"NOT_FOUND\" && echo \"=== long_crm_s44 ===\" && tail -20 /tmp/eval_long_crm_s44.log 2>/dev/null || echo \"NOT_FOUND\" && echo \"=== long_adapt_s44 ===\" && tail -20 /tmp/eval_long_adapt_s44.log 2>/dev/null || echo \"NOT_FOUND\"",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_infra_scan-all-servers-process-status_20260523T212704",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-32758",
    "command": "echo \"=== LOG FILES ===\" && ls -lt /tmp/eval_*.log ~/runs/acr-vla-conformal-refinement/*.log 2>/dev/null | head -20 && echo \"=== k2mean_obj_s46 ===\" && tail -20 /tmp/eval_k2mean_obj_s46.log 2>/dev/null || echo \"NOT_FOUND\" && echo \"=== k2mean_obj_s45 ===\" && tail -20 /tmp/eval_k2mean_obj_s45.log 2>/dev/null || echo \"NOT_FOUND\" && echo \"=== long_crm_s44 ===\" && tail -20 /tmp/eval_long_crm_s44.log 2>/dev/null || echo \"NOT_FOUND\" && echo \"=== long_adapt_s44 ===\" && tail -20 /tmp/eval_long_adapt_s44.log 2>/dev/null || echo \"NOT_FOUND\"",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-23T21:30:18.725547+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== LOG FILES ===\\n-rw-r--r-- 1 root root 5209 May 24 05:27 /tmp/eval_reconvla_obj_s46.log\\n-rw-r--r-- 1 root root 5207 May 24 05:26 /tmp/eval_reconvla_obj_s45.log\\n-rw-r--r-- 1 root root 6202 May 24 05:20 /tmp/eval_k2mean_obj_s45.log\\n-rw-r--r-- 1 root root 6203 May 24 05:15 /tmp/eval_k2mean_obj_s46.log\\n-rw-r--r-- 1 root root 7669 May 24 02:07 /root/runs/acr-vla-conformal-refinement/eval-supp-long-vla-only-s43.log\\n-rw-r--r-- 1 root root 7666 May 24 01:43 /root/runs/acr-vla-conformal-refinement/eval-supp-long-k2mean-s42.log\\n-rw-r--r-- 1 root root 6219 May 23 22:57 /root/runs/acr-vla-conformal-refinement/eval-supp-obj-reconvla-s44.log\\n-rw-r--r-- 1 root root 6215 May 23 22:56 /root/runs/acr-vla-conformal-refinement/eval-supp-k2mean-object-s44.log\\n-rw-r--r-- 1 root root 7245 May 23 22:34 /root/runs/acr-vla-conformal-refinement/eval-supp-spatial-vla-only-s43.log\\n-rw-r--r-- 1 root root 7248 May 23 22:22 /root/runs/acr-vla-conformal-refinement/eval-supp-k2mean-spatial-s44.log\\n=== k2mean_obj_s46 ===\\n  pick_up_the_milk_and_place_it_in_the_basket: rollout 5/20, success so far: 4/5\\n  pick_up_the_milk_and_place_it_in_the_basket: rollout 10/20, success so far: 8/10\\n  pick_up_the_milk_and_place_it_in_the_basket: rollout 15/20, success so far: 11/15\\n  pick_up_the_milk_and_place_it_in_the_basket: rollout 20/20, success so far: 13/20\\n[pick_up_the_milk_and_place_it_in_the_basket] success rate: 65.0% (13/20)\\n  pick_up_the_chocolate_pudding_and_place_it_in_the_basket: rollout 5/20, success so far: 2/5\\n  pick_up_the_chocolate_pudding_and_place_it_in_the_basket: rollout 10/20, success so far: 7/10\\n  pick_up_the_chocolate_pudding_and_place_it_in_the_basket: rollout 15/20, success so far: 12/15\\n  pick_up_the_chocolate_pudding_and_place_it_in_the_basket: rollout 20/20, success so far: 16/20\\n[pick_up_the_chocolate_pudding_and_place_it_in_the_basket] success rate: 80.0% (16/20)\\n  pick_up_the_orang
…[truncated 2478 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_infra_scan-all-servers-process-status_20260523T212704",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-23T21:30:18.725697+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-32758",
  "command": "ls -lt ~/runs/acr-vla-conformal-refinement/ 2>/dev/null | head -20 && echo \"---\" && ls -lt /root/acr-vla-conformal-refinement/logs/ 2>/dev/null | head -20",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_infra_scan-all-servers-process-status_20260523T212704",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-32758",
    "command": "ls -lt ~/runs/acr-vla-conformal-refinement/ 2>/dev/null | head -20 && echo \"---\" && ls -lt /root/acr-vla-conformal-refinement/logs/ 2>/dev/null | head -20",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-23T21:30:18.725848+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 48\\n-rw-r--r-- 1 root root 7669 May 24 02:07 eval-supp-long-vla-only-s43.log\\n-rw-r--r-- 1 root root 7666 May 24 01:43 eval-supp-long-k2mean-s42.log\\n-rw-r--r-- 1 root root 6219 May 23 22:57 eval-supp-obj-reconvla-s44.log\\n-rw-r--r-- 1 root root 6215 May 23 22:56 eval-supp-k2mean-object-s44.log\\n-rw-r--r-- 1 root root 7245 May 23 22:34 eval-supp-spatial-vla-only-s43.log\\n-rw-r--r-- 1 root root 7248 May 23 22:22 eval-supp-k2mean-spatial-s44.log\\n---\\ntotal 724\\n-rw-r--r-- 1 root root   1502 May 24 05:20 eval_object_vla_only_seed45.json\\n-rw-r--r-- 1 root root   1500 May 24 05:15 eval_object_vla_only_seed46.json\\n-rw-r--r-- 1 root root   7901 May 24 05:11 eval-supp-long-crm-norm005-s44.log\\n-rw-r--r-- 1 root root   1793 May 24 05:11 eval_long_crm_obs_only_norm0.05_seed44.json\\n-rw-r--r-- 1 root root   8019 May 24 05:00 eval-supp-long-adapt-tau025-s44.log\\n-rw-r--r-- 1 root root   1992 May 24 05:00 eval_long_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json\\n-rw-r--r-- 1 root root   1791 May 24 02:07 eval_long_vla_only_seed43.json\\n-rw-r--r-- 1 root root   1809 May 24 01:55 eval-supp-long-reconvla-s44.log\\n-rw-r--r-- 1 root root   1789 May 24 01:43 eval_long_vla_only_seed42.json\\n-rw-r--r-- 1 root root   1686 May 24 01:42 eval-supp-long-k2mean-s44.log\\n-rw-r--r-- 1 root root   1500 May 23 22:57 eval_object_reconvla_seed44.json\\n-rw-r--r-- 1 root root   1498 May 23 22:56 eval_object_vla_only_seed44.json\\n-rw-r--r-- 1 root root   1707 May 23 22:34 eval_spatial_vla_only_seed43.json\\n-rw-r--r-- 1 root root   1703 May 23 22:22 eval_spatial_vla_only_seed44.json\\n-rw-r--r-- 1 root root   1498 May 23 19:50 eval_k2mean_object_seed43.json\\n-rw-r--r-- 1 root root   6199 May 23 19:50 eval_k2mean_object_seed43.log\\n-rw-r--r-- 1 root root   5337 May 23 19:28 eval-supp-goal-reconvla-s43.log\\n-rw-r--r-- 1 root root   1331 May 23 19:28 eval_goal_reconvla_seed43.json\\n-rw-r--r-- 1 root root   1705 
…[truncated 151 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_infra_scan-all-servers-process-status_20260523T212704",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-23T21:30:18.726037+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-32758",
  "command": "echo \"=== long-crm-s44 ===\" && tail -5 /root/acr-vla-conformal-refinement/logs/eval-supp-long-crm-norm005-s44.log && echo \"=== long-adapt-s44 ===\" && tail -5 /root/acr-vla-conformal-refinement/logs/eval-supp-long-adapt-tau025-s44.log",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_infra_scan-all-servers-process-status_20260523T212704",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-32758",
    "command": "echo \"=== long-crm-s44 ===\" && tail -5 /root/acr-vla-conformal-refinement/logs/eval-supp-long-crm-norm005-s44.log && echo \"=== long-adapt-s44 ===\" && tail -5 /root/acr-vla-conformal-refinement/logs/eval-supp-long-adapt-tau025-s44.log",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-23T21:30:18.726179+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== long-crm-s44 ===\\n\\n============================================================\\nOverall success rate (crm_obs_only): 56.5% (113/200)\\n============================================================\\n[eval] Results saved to logs/eval_long_crm_obs_only_norm0.05_seed44.json\\n=== long-adapt-s44 ===\\n============================================================\\nOverall success rate (adaptive_conformal_crm): 56.0% (112/200)\\n============================================================\\n[eval] Conformal CRM stats: mean_unc=0.1267, trigger_rate=4.9%\\n[eval] Results saved to logs/eval_long_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_infra_scan-all-servers-process-status_20260523T212704",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-23T21:30:18.726386+00:00_

called mcp__agent-ml-research__save_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "file": "memory.md",
  "content": "# Server Scan Report — 2026-05-24 05:30 UTC\n\n## bjb2-28827 (6× RTX 4090)\n\n| exp_id | GPU | 预期PID | 实际PID | 状态 | 备注 |\n|--------|-----|---------|---------|------|------|\n| eval-supp-goal-vla-only-s45 | cuda:0 | — | 926766 | ALIVE | 19% util, 3685 MiB |\n| eval-supp-goal-crm-norm005-s45 | cuda:1 | — | 927030 | ALIVE | 22% util, 4235 MiB |\n| eval-supp-goal-reconvla-s45 | cuda:2 | — | 927237 | ALIVE | 28% util, 3747 MiB |\n| eval-supp-long-k2mean-s45 | cuda:4 | 924226 | 924226 | ALIVE | 18% util, 5591 MiB |\n| eval-supp-long-k2mean-s44 | cuda:5 | 850410 | 850410 | ALIVE | 22% util, 2307 MiB |\n| *eval-supp-long-reconvla-s44* | cuda:3 | — | 849677 | ALIVE | **未在预期列表** 0% GPU util但占1755 MiB |\n\n空闲 GPU: **无**\n\nTmux sessions: eval-goal-crm-s45, eval-goal-reconvla-s45, eval-goal-vla-s45, eval-long-k2mean-s45, eval-supp-long-k2mean-s44, eval-supp-long-reconvla-s44\n\n---\n\n## bjb1-32546 (6× RTX 4090)\n\n| exp_id | GPU | 预期PID | 实际PID | 状态 | 备注 |\n|--------|-----|---------|---------|------|------|\n| eval-supp-crm-norm005-obj-s46 | cuda:0 | — | 102927 | ALIVE | 33% util, 3389 MiB |\n| eval-supp-long-vla-only-s45 | cuda:1 | — | 103128 | ALIVE | 21% util, 4911 MiB |\n| eval-supp-long-adapt-tau025-s45 | cuda:2 | — | 103397 | ALIVE | 23% util, 4917 MiB |\n| eval-supp-long-crm-norm005-s45 | cuda:3 | — | 103675 | ALIVE | 24% util, 5011 MiB |\n| eval-supp-long-reconvla-s45 | cuda:4 | — | 103942 | ALIVE | 31% util, 4973 MiB |\n| eval-supp-goal-adapt-tau025-s45 | cuda:5 | — | 104216 | ALIVE | 22% util, 2786 MiB |\n\n空闲 GPU: **无**\n\nTmux sessions: eval-crm-obj-s46, eval-goal-adapt-s45, eval-long-adapt-s45, eval-long-crm-s45, eval-long-reconvla-s45, eval-long-vla-s45\n\n---\n\n## cqa1-32758 (6× RTX 4090 D)\n\n| exp_id | GPU | 预期PID | 实际PID | 状态 | 备注 |\n|--------|-----|---------|---------|------|------|\n| eval-supp-reconvla-obj-s46 | cuda:2 | — | 380176 | ALIVE | 32% util, 2183 MiB |\n| eval-supp-k2mean-obj-s46 | cuda:3 | — | — | COMPLETED | 76.5% (153/200), saved eval_object_vla_only_seed46.json |\n| eval-supp-k2mean-obj-s45 | cuda:0 | — | — | COMPLETED | 77.5% (155/200), saved eval_object_vla_only_seed45.json |\n| eval-supp-long-crm-norm005-s44 | cuda:5 | 291523 | — | COMPLETED | 56.5% (113/200), saved eval_long_crm_obs_only_norm0.05_seed44.json |\n| eval-supp-long-adapt-tau025-s44 | cuda:1 | 291315 | — | COMPLETED | 56.0% (112/200), trigger_rate=4.9%, saved eval_long_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json |\n| *eval-reconvla-obj-s45* | cuda:4 | — | 377316 | ALIVE | **未在预期列表**, 47% util, 2183 MiB |\n\n空闲 GPU: **cuda:0, cuda:1, cuda:3, cuda:5**（4个空闲）\n\nTmux sessions: eval-reconvla-obj-s45, eval-reconvla-obj-s46 (+ stale: k2mean_spatial_s43)\n\n---\n\n## bjb2-40593 (1× RTX 4090 D, 磁盘满/excluded)\n\n| exp_id | GPU | 预期PID | 实际PID | 状态 | 备注 |\n|--------|-----|---------|---------|------|------|\n| eval-supp-crm-norm005-obj-s45 | cuda:0 | — | 177824 | ALIVE | 21% util, 2688 MiB |\n\n空闲 GPU: 该服务器仅1个GPU，已占用\n\nTmux sessions: eval-crm-obj-s45\n\n---\n\n## 汇总\n\n### 存活实验 (14)\n| 服务器 | 实验数 | GPU占用 |\n|--------|--------|---------|\n| bjb2-28827 | 6 (含1个未预期) | 6/6 |\n| bjb1-32546 | 6 | 6/6 |\n| cqa1-32758 | 2 (含1个未预期) | 2/6 |\n| bjb2-40593 | 1 | 1/1 |\n\n### 已完成实验 (4, 全在 cqa1-32758)\n| exp_id | 结果 |\n|--------|------|\n| eval-supp-k2mean-obj-s46 | 76.5% (153/200) |\n| eval-supp-k2mean-obj-s45 | 77.5% (155/200) |\n| eval-supp-long-crm-norm005-s44 | 56.5% (113/200) |\n| eval-supp-long-adapt-tau025-s44 | 56.0% (112/200) |\n\n### 未预期实验 (2)\n- bjb2-28827 cuda:3: eval-supp-long-reconvla-s44 (PID 849677)\n- cqa1-32758 cuda:4: eval-reconvla-obj-s45 (PID 377316)\n\n### 可用GPU\n- cqa1-32758: cuda:0, cuda:1, cuda:3, cuda:5（4个空闲）\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_infra_scan-all-servers-process-status_20260523T212704",
  "tool": "mcp__agent-ml-research__save_project_file",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "file": "memory.md",
    "content": "# Server Scan Report — 2026-05-24 05:30 UTC\n\n## bjb2-28827 (6× RTX 4090)\n\n| exp_id | GPU | 预期PID | 实际PID | 状态 | 备注 |\n|--------|-----|---------|---------|------|------|\n| eval-supp-goal-vla-only-s45 | cuda:0 | — | 926766 | ALIVE | 19% util, 3685 MiB |\n| eval-supp-goal-crm-norm005-s45 | cuda:1 | — | 927030 | ALIVE | 22% util, 4235 MiB |\n| eval-supp-goal-reconvla-s45 | cuda:2 | — | 927237 | ALIVE | 28% util, 3747 MiB |\n| eval-supp-long-k2mean-s45 | cuda:4 | 924226 | 924226 | ALIVE | 18% util, 5591 MiB |\n| eval-supp-long-k2mean-s44 | cuda:5 | 850410 | 850410 | ALIVE | 22% util, 2307 MiB |\n| *eval-supp-long-reconvla-s44* | cuda:3 | — | 849677 | ALIVE | **未在预期列表** 0% GPU util但占1755 MiB |\n\n空闲 GPU: **无**\n\nTmux sessions: eval-goal-crm-s45, eval-goal-reconvla-s45, eval-goal-vla-s45, eval-long-k2mean-s45, eval-supp-long-k2mean-s44, eval-supp-long-reconvla-s44\n\n---\n\n## bjb1-32546 (6× RTX 4090)\n\n| exp_id | GPU | 预期PID | 实际PID | 状态 | 备注 |\n|--------|-----|---------|---------|------|------|\n| eval-supp-crm-norm005-obj-s46 | cuda:0 | — | 102927 | ALIVE | 33% util, 3389 MiB |\n| eval-supp-long-vla-only-s45 | cuda:1 | — | 103128 | ALIVE | 21% util, 4911 MiB |\n| eval-supp-long-adapt-tau025-s45 | cuda:2 | — | 103397 | ALIVE | 23% util, 4917 MiB |\n| eval-supp-long-crm-norm005-s45 | cuda:3 | — | 103675 | ALIVE | 24% util, 5011 MiB |\n| eval-supp-long-reconvla-s45 | cuda:4 | — | 103942 | ALIVE | 31% util, 4973 MiB |\n| eval-supp-goal-adapt-tau025-s45 | cuda:5 | — | 104216 | ALIVE | 22% util, 2786 MiB |\n\n空闲 GPU: **无**\n\nTmux sessions: eval-crm-obj-s46, eval-goal-adapt-s45, eval-long-adapt-s45, eval-long-crm-s45, eval-long-reconvla-s45, eval-long-vla-s45\n\n---\n\n## cqa1-32758 (6× RTX 4090 D)\n\n| exp_id | GPU | 预期PID | 实际PID | 状态 | 备注 |\n|--------|-----|---------|---------|------|------|\n| eval-supp-reconvla-obj-s46 | cuda:2 | — | 380176 | ALIVE | 32% util, 2183 MiB |\n| eval-supp-k2mean-obj-s46 | cuda:3 | — | — | COMPLETED | 76.5% (153/200), saved eval_object_vla_only_seed46.json |\n| eval-supp-k2mean-obj-s45 | cuda:0 | — | — | COMPLETED | 77.5% (155/200), saved eval_object_vla_only_seed45.json |\n| eval-supp-long-crm-norm005-s44 | cuda:5 | 291523 | — | COMPLETED | 56.5% (113/200), saved eval_long_crm_obs_only_norm0.05_seed44.json |\n| eval-supp-long-adapt-tau025-s44 | cuda:1 | 291315 | — | COMPLETED | 56.0% (112/200), trigger_rate=4.9%, saved eval_long_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json |\n| *eval-reconvla-obj-s45* | cuda:4 | — | 377316 | ALIVE | **未在预期列表**, 47% util, 2183 MiB |\n\n空闲 GPU: **cuda:0, cuda:1, cuda:3, cuda:5**（4个空闲）\n\nTmux sessions: eval-reconvla-obj-s45, eval-reconvla-obj-s46 (+ stale: k2mean_spatial_s43)\n\n---\n\n## bjb2-40593 (1× RTX 4090 D, 磁盘满/excluded)\n\n| exp_id | GPU | 预期PID | 实际PID | 状态 | 备注 |\n|--------|-----|---------|---------|------|------|\n| eval-supp-crm-norm005-obj-s45 | cuda:0 | — | 177824 | ALIVE | 21% util, 2688 MiB |\n\n空闲 GPU: 该服务器仅1个GPU，已占用\n\nTmux sessions: eval-crm-obj-s45\n\n---\n\n## 汇总\n\n### 存活实验 (14)\n| 服务器 | 实验数 | GPU占用 |\n|--------|--------|---------|\n| bjb2-28827 | 6 (含1个未预期) | 6/6 |\n| bjb1-32546 | 6 | 6/6 |\n| cqa1-32758 | 2 (含1个未预期) | 2/6 |\n| bjb2-40593 | 1 | 1/1 |\n\n### 已完成实验 (4, 全在 cqa1-32758)\n| exp_id | 结果 |\n|--------|------|\n| eval-supp-k2mean-obj-s46 | 76.5% (153/200) |\n| eval-supp-k2mean-obj-s45 | 77.5% (155/200) |\n| eval-supp-long-crm-norm005-s44 | 56.5% (113/200) |\n| eval-supp-long-adapt-tau025-s44 | 56.0% (112/200) |\n\n### 未预期实验 (2)\n- bjb2-28827 cuda:3: eval-supp-long-reconvla-s44 (PID 849677)\n- cqa1-32758 cuda:4: eval-reconvla-obj-s45 (PID 377316)\n\n### 可用GPU\n- cqa1-32758: cuda:0, cuda:1, cuda:3, cuda:5（4个空闲）\n"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-23T21:30:18.726568+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/memory.md\", \"saved\": true}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_infra_scan-all-servers-process-status_20260523T212704",
  "tool": "mcp__agent-ml-research__save_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-23T21:30:18.726746+00:00_

扫描完成。

## 汇总

### 存活实验 (14个进程)

**bjb2-28827** — 6/6 GPU 满载
| exp_id | GPU | PID | 状态 |
|--------|-----|-----|------|
| eval-supp-goal-vla-only-s45 | cuda:0 | 926766 | ALIVE |
| eval-supp-goal-crm-norm005-s45 | cuda:1 | 927030 | ALIVE |
| eval-supp-goal-reconvla-s45 | cuda:2 | 927237 | ALIVE |
| *eval-supp-long-reconvla-s44* | cuda:3 | 849677 | ALIVE (未预期) |
| eval-supp-long-k2mean-s45 | cuda:4 | 924226 | ALIVE |
| eval-supp-long-k2mean-s44 | cuda:5 | 850410 | ALIVE |

**bjb1-32546** — 6/6 GPU 满载
| exp_id | GPU | PID | 状态 |
|--------|-----|-----|------|
| eval-supp-crm-norm005-obj-s46 | cuda:0 | 102927 | ALIVE |
| eval-supp-long-vla-only-s45 | cuda:1 | 103128 | ALIVE |
| eval-supp-long-adapt-tau025-s45 | cuda:2 | 103397 | ALIVE |
| eval-supp-long-crm-norm005-s45 | cuda:3 | 103675 | ALIVE |
| eval-supp-long-reconvla-s45 | cuda:4 | 103942 | ALIVE |
| eval-supp-goal-adapt-tau025-s45 | cuda:5 | 104216 | ALIVE |

**cqa1-32758** — 2/6 GPU 在用
| exp_id | GPU | PID | 状态 |
|--------|-----|-----|------|
| eval-supp-reconvla-obj-s46 | cuda:2 | 380176 | ALIVE |
| *eval-reconvla-obj-s45* | cuda:4 | 377316 | ALIVE (未预期) |

**bjb2-40593** — 1/1 GPU 在用
| exp_id | GPU | PID | 状态 |
|--------|-----|-----|------|
| eval-supp-crm-norm005-obj-s45 | cuda:0 | 177824 | ALIVE |

### 已完成实验 (4个，全在 cqa1-32758)

| exp_id | 结果 | 输出文件 |
|--------|------|---------|
| eval-supp-k2mean-obj-s46 | **76.5%** (153/200) | eval_object_vla_only_seed46.json |
| eval-supp-k2mean-obj-s45 | **77.5%** (155/200) | eval_object_vla_only_seed45.json |
| eval-supp-long-crm-norm005-s44 | **56.5%** (113/200) | eval_long_crm_obs_only_norm0.05_seed44.json |
| eval-supp-long-adapt-tau025-s44 | **56.0%** (112/200) | eval_long_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json |

### 可用 GPU

cqa1-32758 有 **4 个空闲 GPU**: cuda:0, cuda:1, cuda:3, cuda:5

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_infra_scan-all-servers-process-status_20260523T212704"
}
```

</details>

---
