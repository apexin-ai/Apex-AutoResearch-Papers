# research openvla attention feasibility

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 35
- **Recorded user turns:** 0
- **Tool calls:** 17
- **Original source:** `logs/chats/worker_research_openvla-attention-feasibility_20260524T014932.jsonl`
- **Structured JSON:** [`8ea78a752b3104d51233.json`](../../sessions/8e/8ea78a752b3104d51233.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

35 recorded events

### Tool call

_source line 1 · 2026-05-24T01:51:00.568720+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-attention-feasibility_20260524T014932",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-24T01:51:00.569079+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-attention-feasibility_20260524T014932",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-24T01:51:00.569297+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "cat /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_pruning_libero.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-attention-feasibility_20260524T014932",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "cat /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_pruning_libero.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-24T01:51:00.569450+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"cat: /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_pruning_libero.py: No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 1.18}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-attention-feasibility_20260524T014932",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-24T01:51:00.569600+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "find /root/autodl-tmp/importance_margin_vla_compress -name \"*openvla*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-attention-feasibility_20260524T014932",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "find /root/autodl-tmp/importance_margin_vla_compress -name \"*openvla*\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-24T01:51:00.569802+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/importance_margin_vla_compress/configs/openvla_smart_compress_m128.yaml\\n/root/autodl-tmp/importance_margin_vla_compress/configs/openvla_smart_compress_m32.yaml\\n/root/autodl-tmp/importance_margin_vla_compress/configs/openvla_smart_compress_m64.yaml\\n/root/autodl-tmp/importance_margin_vla_compress/logs/train_openvla_sc_m32_seed42.log\\n/root/autodl-tmp/importance_margin_vla_compress/logs/eval_openvla_sc_m128_vtconly_20k_seed42.log\\n/root/autodl-tmp/importance_margin_vla_compress/logs/train_openvla_sc_m32_seed42_resume.log\\n/root/autodl-tmp/importance_margin_vla_compress/logs/eval_openvla_l2norm_k07_seed43.log\\n/root/autodl-tmp/importance_margin_vla_compress/logs/eval_openvla_sc_m128_object_seed42.log\\n/root/autodl-tmp/importance_margin_vla_compress/logs/eval_openvla_l2norm_k05_object_seed43.log\\n/root/autodl-tmp/importance_margin_vla_compress/logs/eval_openvla_random_k09_object_seed42.log\\n/root/autodl-tmp/importance_margin_vla_compress/logs/eval_openvla_random_k05_object_seed42.log\\n/root/autodl-tmp/importance_margin_vla_compress/logs/eval_openvla_baseline_spatial_seed42_v3.log\\n/root/autodl-tmp/importance_margin_vla_compress/logs/e3_cosine_xvla_openvla.log\\n/root/autodl-tmp/importance_margin_vla_compress/logs/e3_cosine_xvla_openvla_v2.log\\n/root/autodl-tmp/importance_margin_vla_compress/logs/e3_cosine_openvla.log\\n/root/autodl-tmp/importance_margin_vla_compress/logs/eval_openvla_baseline_goal_seed42.log\\n/root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_baseline_object.log\\n/root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_eval_all.log\\n/root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_baseline_object.json\\n/root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_random_prune_k05_object.log\\n/root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_random_prune_k07_object.json\\n/root/autodl-tmp
…[truncated 5480 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-attention-feasibility_20260524T014932",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-24T01:51:00.569986+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "find /root/autodl-tmp/importance_margin_vla_compress -name \"*eval*pruning*\" -o -name \"*pruning*eval*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-attention-feasibility_20260524T014932",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "find /root/autodl-tmp/importance_margin_vla_compress -name \"*eval*pruning*\" -o -name \"*pruning*eval*\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-24T01:51:00.570150+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/importance_margin_vla_compress/eval_pruning_sweep.py\\n/root/autodl-tmp/importance_margin_vla_compress/eval_pruning_sweep.py.bak\\n/root/autodl-tmp/importance_margin_vla_compress/eval_pi05_pruning_libero.py\\n/root/autodl-tmp/importance_margin_vla_compress/eval_smolvla_pruning_official.py\\n/root/autodl-tmp/importance_margin_vla_compress/eval_pi05_pruning_libero.py.bak\\n/root/autodl-tmp/importance_margin_vla_compress/eval_smolvla_pruning_official.py.bak\\n/root/autodl-tmp/importance_margin_vla_compress/eval_xvla_pruning_libero.py\\n/root/autodl-tmp/importance_margin_vla_compress/eval_xvla_attention_pruning_libero.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-attention-feasibility_20260524T014932",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-24T01:51:00.570297+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "ls /root/autodl-tmp/importance_margin_vla_compress/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-attention-feasibility_20260524T014932",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "ls /root/autodl-tmp/importance_margin_vla_compress/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-24T01:51:00.570472+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"_lerobot_compat.py\\n_patch_openvla.py\\n_patch_pi05.py\\n_patch_smolvla.py\\nanalyze_attention.py\\nanalyze_gate.py\\nanalyze_openvla_attention_entropy.py\\nanalyze_token_cosine_similarity.py\\nartifacts\\nattention_entropy_openvla.log\\nauto_deploy_openvla_baselines.sh\\ncheckpoints\\nclosedloop_action_divergence.py\\nconfigs\\ndebug_obs.py\\ndiag_ep42.py\\neval_acis_overhead.py\\neval_formal_bound.py\\neval_official_libero.py\\neval_openvla_l2norm_libero.py\\neval_openvla_l2norm_libero.py.bak\\neval_openvla_libero.py\\neval_openvla_smart_compress.py\\neval_pi05_pruning_libero.py\\neval_pi05_pruning_libero.py.bak\\neval_pruning_sweep.py\\neval_pruning_sweep.py.bak\\neval_results\\neval_seed0_100k_all.log\\neval_seed0_object.log\\neval_sim.py\\neval_smart_compress_libero.py\\neval_smolvla_pruning_official.py\\neval_smolvla_pruning_official.py.bak\\neval_success_rate.py\\neval_success_rate.py.bak\\neval_success_rate_libero.py\\neval_success_rate_libero.py.bak\\neval_token_importance.py\\neval_xvla_attention_pruning_libero.py\\neval_xvla_pruning_libero.py\\nevaluate.py\\nevaluate.py.bak\\nevaluate.py.bak2\\nevaluate.py.bak_pre_d028\\ngen_figures.py\\ngeometric_prior_pruning.py\\nimm\\nlogs\\nmeasure_openvla_entropy_real.py\\noffline_singlestep_error.py\\nopenvla_vtc_adapter.py\\nresults\\nrun_bypass_eval.sh\\nrun_d014_eval.sh\\nrun_e3_openvla_only.py\\nrun_e3_xvla_openvla.py\\nrun_eval_v8_fixed.sh\\nrun_mvp.sh\\nrun_openvla_both.sh\\nrun_openvla_eval_all.sh\\nrun_openvla_k09.sh\\nrun_openvla_l2norm_sweep.sh\\nrun_openvla_prune_seed43.sh\\nrun_pruning_experiments.sh\\nrun_traj_28k_30k_v2.sh\\nrun_traj_eval_28k_30k.sh\\nrun_traj_eval_补跑.sh\\nrun_v8_1_final_eval.sh\\nrun_v8_final_eval.sh\\nrun_v8b_final_eval.sh\\nrun_v8c_final_eval.sh\\nscan_collapse.py\\nscripts\\nsmart_compress_module.py\\ntest_geometric_pruning.py\\ntest_inference_fixes.py\\ntest_mode_collapse.py\\ntest_openvla_load.py\\ntest_pretrained_sim.py\\
…[truncated 255 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-attention-feasibility_20260524T014932",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-24T01:51:00.570726+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "cat /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_libero.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-attention-feasibility_20260524T014932",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "cat /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_libero.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-24T01:51:00.571080+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nOpenVLA LIBERO Evaluation: Baseline + Random Token Pruning.\\nUsage:\\n    python eval_openvla_libero.py --mode baseline --suite libero_object\\n    python eval_openvla_libero.py --mode random_prune --k_ratio 0.5 --suite libero_object\\n\\\"\\\"\\\"\\nimport argparse, io, json, math, os, sys, time\\nos.environ[\\\"MUJOCO_GL\\\"] = \\\"egl\\\"\\nos.environ.setdefault(\\\"CUDA_VISIBLE_DEVICES\\\", \\\"0\\\")\\nos.environ[\\\"TRANSFORMERS_OFFLINE\\\"] = \\\"1\\\"\\nos.environ[\\\"HF_HUB_OFFLINE\\\"] = \\\"1\\\"\\n\\n# Use transformers 4.40.1 for OpenVLA compat\\nsys.path.insert(0, \\\"/root/autodl-tmp/openvla_deps\\\")\\n\\nimport numpy as np\\nimport torch\\nfrom PIL import Image\\n\\n# Import OpenVLA model code\\nhf_dir = \\\"/root/autodl-tmp/openvla-repo/prismatic/extern/hf\\\"\\ninit_path = os.path.join(hf_dir, \\\"__init__.py\\\")\\nif not os.path.exists(init_path):\\n    open(init_path, \\\"w\\\").close()\\nsys.path.insert(0, \\\"/root/autodl-tmp/openvla-repo/prismatic/extern\\\")\\nfrom hf.configuration_prismatic import OpenVLAConfig\\nfrom hf.modeling_prismatic import OpenVLAForActionPrediction\\nfrom hf.processing_prismatic import PrismaticImageProcessor, PrismaticProcessor\\n\\nDEVICE = torch.device(\\\"cuda:0\\\")\\nCHECKPOINT_PATH = \\\"/root/autodl-tmp/openvla-libero-object\\\"\\nUNNORM_KEY = \\\"libero_object\\\"\\n\\nSUITE_MAX_STEPS = {\\n    \\\"libero_spatial\\\": 280,\\n    \\\"libero_object\\\": 280,\\n    \\\"libero_goal\\\": 300,\\n    \\\"libero_10\\\": 520,\\n}\\n\\n\\ndef parse_args():\\n    p = argparse.ArgumentParser()\\n    p.add_argument(\\\"--mode\\\", choices=[\\\"baseline\\\", \\\"random_prune\\\"], default=\\\"baseline\\\")\\n    p.add_argument(\\\"--k_ratio\\\", type=float, default=0.5)\\n    p.add_argument(\\\"--suite\\\", type=str, default=\\\"libero_object\\\")\\n    p.add_argument(\\\"--num_episodes\\\", type=int, default=50)\\n    p.add_argument(\\\"--seed\\\", 
…[truncated 7124 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-attention-feasibility_20260524T014932",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-24T01:51:00.571307+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "cat /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-attention-feasibility_20260524T014932",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "cat /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-24T01:51:00.571452+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "cat /root/autodl-tmp/importance_margin_vla_compress/eval_xvla_attention_pruning_libero.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-attention-feasibility_20260524T014932",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "cat /root/autodl-tmp/importance_margin_vla_compress/eval_xvla_attention_pruning_libero.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-24T01:51:00.571726+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nOpenVLA LIBERO Evaluation: Baseline + Random/L2-Norm Token Pruning.\\nUsage:\\n    python eval_openvla_l2norm_libero.py --mode baseline --suite libero_object\\n    python eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.5 --suite libero_object\\n\\\"\\\"\\\"\\nimport argparse, io, json, math, os, sys, time\\nos.environ[\\\"MUJOCO_GL\\\"] = \\\"egl\\\"\\nos.environ.setdefault(\\\"CUDA_VISIBLE_DEVICES\\\", \\\"0\\\")\\nos.environ[\\\"TRANSFORMERS_OFFLINE\\\"] = \\\"1\\\"\\nos.environ[\\\"HF_HUB_OFFLINE\\\"] = \\\"1\\\"\\n\\n# Use transformers 4.40.1 for OpenVLA compat\\nsys.path.insert(0, \\\"/root/autodl-tmp/openvla_deps\\\")\\n\\nimport numpy as np\\nimport torch\\nfrom PIL import Image\\n\\n# Import OpenVLA model code\\nhf_dir = \\\"/root/autodl-tmp/openvla-repo/prismatic/extern/hf\\\"\\ninit_path = os.path.join(hf_dir, \\\"__init__.py\\\")\\nif not os.path.exists(init_path):\\n    open(init_path, \\\"w\\\").close()\\nsys.path.insert(0, \\\"/root/autodl-tmp/openvla-repo/prismatic/extern\\\")\\nfrom hf.configuration_prismatic import OpenVLAConfig\\nfrom hf.modeling_prismatic import OpenVLAForActionPrediction\\nfrom hf.processing_prismatic import PrismaticImageProcessor, PrismaticProcessor\\n\\nDEVICE = torch.device(\\\"cuda:0\\\")\\nCHECKPOINT_PATH = \\\"/root/autodl-tmp/openvla-libero-object\\\"\\nUNNORM_KEY = \\\"libero_object\\\"\\n\\nSUITE_MAX_STEPS = {\\n    \\\"libero_spatial\\\": 280,\\n    \\\"libero_object\\\": 280,\\n    \\\"libero_goal\\\": 300,\\n    \\\"libero_10\\\": 520,\\n}\\n\\n\\ndef parse_args():\\n    p = argparse.ArgumentParser()\\n    p.add_argument(\\\"--mode\\\", choices=[\\\"baseline\\\", \\\"random_prune\\\", \\\"l2norm_prune\\\", \\\"attention_prune\\\"], default=\\\"baseline\\\")\\n    p.add_argument(\\\"--k_ratio\\\", type=float, default=0.5)\\n    p.add_argument(\\\"--suite\\\", type=str, default=\\\"libero_object\\\")\\n    p.add_argument(\\\"--num_epis
…[truncated 7200 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-attention-feasibility_20260524T014932",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-24T01:51:00.572059+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"X-VLA Attention-based Vision Token Pruning Evaluation on LIBERO.\\n\\nUses BART encoder self-attention scores to identify important vision tokens,\\nthen prunes less important ones from the encoder output. Three scoring modes:\\n  - attention_last:    importance from last encoder layer attention (column-sum)\\n  - attention_mean:    importance averaged across all encoder layers (column-sum)\\n  - attention_rollout: attention rollout across layers (Abnar & Zuidema, 2020)\\n\\nKey difference from L2/random pruning: all vision tokens pass through the BART\\nencoder (so attention context is complete), then pruning happens on the encoder\\noutput before it enters the SoftPromptedTransformer action head.\\n\\nEvaluation protocol identical to eval_xvla_pruning_libero.py.\\n\\nUsage:\\n    CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl python eval_xvla_attention_pruning_libero.py \\\\\\n        --model_path /path/to/X-VLA-Libero \\\\\\n        --suite libero_object \\\\\\n        --keep_ratio 0.5 \\\\\\n        --mode attention_rollout \\\\\\n        --num_episodes 50 \\\\\\n        --gpu 0\\n\\\"\\\"\\\"\\n\\nfrom __future__ import annotations\\n\\nimport argparse\\nimport json\\nimport logging\\nimport os\\nimport sys\\nimport time as time_mod\\nfrom pathlib import Path\\nfrom functools import wraps\\n\\nos.environ.setdefault(\\\"MUJOCO_GL\\\", \\\"egl\\\")\\n\\nimport numpy as np\\nimport torch\\nfrom PIL import Image\\n\\nsys.path.insert(0, str(Path(__file__).resolve().parent))\\n\\nlogging.basicConfig(\\n    level=logging.INFO,\\n    format=\\\"%(asctime)s [%(levelname)s] %(message)s\\\",\\n    datefmt=\\\"%Y-%m-%d %H:%M:%S\\\",\\n)\\nlog = logging.getLogger(__name__)\\n\\nSUITE_MAX_STEPS = {\\n    \\\"libero_spatial\\\": 800,\\n    \\\"libero_object\\\": 800,\\n    \\\"libero_goal\\\": 800,\\n    \\\"libero_10\\\": 900,\\n    \\\"libero_90\\\": 800,\\n}\\n\\nEPS = 1e-6\\n\\n\\ndef parse_args():\\n    p = argpar
…[truncated 7148 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-attention-feasibility_20260524T014932",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-24T01:51:00.572288+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "grep -n \"attention_prune\\|attention\\|hook\\|register_forward\\|def.*prune\\|def.*get_action\\|vision_token\" /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-attention-feasibility_20260524T014932",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "grep -n \"attention_prune\\|attention\\|hook\\|register_forward\\|def.*prune\\|def.*get_action\\|vision_token\" /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-24T01:51:00.572432+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-attention-feasibility_20260524T014932",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-24T01:51:00.572583+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "head -250 /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-attention-feasibility_20260524T014932",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "head -250 /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-24T01:51:00.572855+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nOpenVLA LIBERO Evaluation: Baseline + Random/L2-Norm Token Pruning.\\nUsage:\\n    python eval_openvla_l2norm_libero.py --mode baseline --suite libero_object\\n    python eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.5 --suite libero_object\\n\\\"\\\"\\\"\\nimport argparse, io, json, math, os, sys, time\\nos.environ[\\\"MUJOCO_GL\\\"] = \\\"egl\\\"\\nos.environ.setdefault(\\\"CUDA_VISIBLE_DEVICES\\\", \\\"0\\\")\\nos.environ[\\\"TRANSFORMERS_OFFLINE\\\"] = \\\"1\\\"\\nos.environ[\\\"HF_HUB_OFFLINE\\\"] = \\\"1\\\"\\n\\n# Use transformers 4.40.1 for OpenVLA compat\\nsys.path.insert(0, \\\"/root/autodl-tmp/openvla_deps\\\")\\n\\nimport numpy as np\\nimport torch\\nfrom PIL import Image\\n\\n# Import OpenVLA model code\\nhf_dir = \\\"/root/autodl-tmp/openvla-repo/prismatic/extern/hf\\\"\\ninit_path = os.path.join(hf_dir, \\\"__init__.py\\\")\\nif not os.path.exists(init_path):\\n    open(init_path, \\\"w\\\").close()\\nsys.path.insert(0, \\\"/root/autodl-tmp/openvla-repo/prismatic/extern\\\")\\nfrom hf.configuration_prismatic import OpenVLAConfig\\nfrom hf.modeling_prismatic import OpenVLAForActionPrediction\\nfrom hf.processing_prismatic import PrismaticImageProcessor, PrismaticProcessor\\n\\nDEVICE = torch.device(\\\"cuda:0\\\")\\nCHECKPOINT_PATH = \\\"/root/autodl-tmp/openvla-libero-object\\\"\\nUNNORM_KEY = \\\"libero_object\\\"\\n\\nSUITE_MAX_STEPS = {\\n    \\\"libero_spatial\\\": 280,\\n    \\\"libero_object\\\": 280,\\n    \\\"libero_goal\\\": 300,\\n    \\\"libero_10\\\": 520,\\n}\\n\\n\\ndef parse_args():\\n    p = argparse.ArgumentParser()\\n    p.add_argument(\\\"--mode\\\", choices=[\\\"baseline\\\", \\\"random_prune\\\", \\\"l2norm_prune\\\", \\\"attention_prune\\\"], default=\\\"baseline\\\")\\n    p.add_argument(\\\"--k_ratio\\\", type=float, default=0.5)\\n    p.add_argument(\\\"--suite\\\", type=str, default=\\\"libero_object\\\")\\n    p.add_argument(\\\"--num_epis
…[truncated 6969 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-attention-feasibility_20260524T014932",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-24T01:51:00.573058+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "grep -n \"register_forward\\|hook\\|projector\\|vision_backbone\\|DinoSiglip\\|vision_token\\|n_vis\" /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-attention-feasibility_20260524T014932",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "grep -n \"register_forward\\|hook\\|projector\\|vision_backbone\\|DinoSiglip\\|vision_token\\|n_vis\" /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-24T01:51:00.573224+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-attention-feasibility_20260524T014932",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-24T01:51:00.573354+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "tail -200 /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-attention-feasibility_20260524T014932",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "tail -200 /root/autodl-tmp/importance_margin_vla_compress/eval_openvla_l2norm_libero.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-24T01:51:00.573602+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"                from transformers.models.llama.modeling_llama import rotate_half\\n                q_embed = (q * cos) + (rotate_half(q) * sin)\\n                k_embed = (k * cos) + (rotate_half(k) * sin)\\n\\n                if n_kv_heads != n_q_heads:\\n                    n_rep = n_q_heads // n_kv_heads\\n                    k_embed = k_embed.repeat_interleave(n_rep, dim=1)\\n                    v = v.repeat_interleave(n_rep, dim=1)\\n\\n                attn_weights = torch.matmul(q_embed, k_embed.transpose(-2, -1)) / math.sqrt(head_dim)\\n                attn_weights = F.softmax(attn_weights, dim=-1, dtype=torch.float32)\\n                all_attn.append(attn_weights)\\n\\n                attn_out = torch.matmul(attn_weights.to(v.dtype), v)\\n                attn_out = attn_out.transpose(1, 2).reshape(B, N, n_q_heads * head_dim)\\n                attn_out = layer.self_attn.o_proj(attn_out)\\n                hidden = hidden + attn_out\\n\\n                normed2 = layer.post_attention_layernorm(hidden)\\n                mlp_out = layer.mlp(normed2)\\n                hidden = hidden + mlp_out\\n\\n        avg_attn = torch.stack(all_attn).mean(dim=0).mean(dim=1)  # [B, N, N]\\n        importance = avg_attn.sum(dim=1)  # [B, N]\\n\\n        _, indices = torch.topk(importance, keep, dim=-1)\\n        indices = indices.sort(dim=-1).values\\n        pruned = torch.gather(output, 1, indices.unsqueeze(-1).expand(-1, -1, D))\\n\\n        if not self.logged:\\n            print(f\\\"[Attn Pruning] {N} -> {keep} vision tokens (k={self.k_ratio}), \\\"\\n                  f\\\"importance range=[{importance.min():.4f}, {importance.max():.4f}]\\\",\\n                  flush=True)\\n            self.logged = True\\n\\n        return pruned\\n\\n\\ndef count_vision_tokens(vla, processor):\\n    dummy = Image.new(\\\"RGB\\\", (224, 224), (128, 128, 128))\\n    prompt = \\\"In: What action should the robot take to pick up t
…[truncated 6959 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-attention-feasibility_20260524T014932",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-24T01:51:00.573784+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "grep -rn \"vision_backbone\\|DinoSiglip\\|SigLIP\\|DINOv2\\|num_patches\\|n_patches\\|256\\|512\" /root/autodl-tmp/openvla-repo/prismatic/extern/hf/configuration_prismatic.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-attention-feasibility_20260524T014932",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "grep -rn \"vision_backbone\\|DinoSiglip\\|SigLIP\\|DINOv2\\|num_patches\\|n_patches\\|256\\|512\" /root/autodl-tmp/openvla-repo/prismatic/extern/hf/configuration_prismatic.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-24T01:51:00.573926+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-attention-feasibility_20260524T014932",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-24T01:51:00.574052+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "grep -rn \"class.*VisionBackbone\\|projector\\|fused_vision\\|dinosiglip\" /root/autodl-tmp/openvla-repo/prismatic/extern/hf/modeling_prismatic.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-attention-feasibility_20260524T014932",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "grep -rn \"class.*VisionBackbone\\|projector\\|fused_vision\\|dinosiglip\" /root/autodl-tmp/openvla-repo/prismatic/extern/hf/modeling_prismatic.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-24T01:51:00.574197+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-attention-feasibility_20260524T014932",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-24T01:51:00.574321+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "grep -rn \"vision_backbone\" /root/autodl-tmp/openvla-repo/prismatic/extern/hf/configuration_prismatic.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-attention-feasibility_20260524T014932",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "grep -rn \"vision_backbone\" /root/autodl-tmp/openvla-repo/prismatic/extern/hf/configuration_prismatic.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-24T01:51:00.574455+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"78:        vision_backbone_id: str = \\\"siglip-vit-so400m\\\",\\n81:        use_fused_vision_backbone: Optional[bool] = None,\\n90:        if vision_backbone_id not in VALID_VISION_BACKBONES:\\n91:            raise ValueError(f\\\"Vision backbone `{vision_backbone_id}` not in {VALID_VISION_BACKBONES = }\\\")\\n97:        self.vision_backbone_id = vision_backbone_id\\n103:        self.use_fused_vision_backbone = (\\n104:            use_fused_vision_backbone\\n105:            if use_fused_vision_backbone is not None\\n106:            else any(self.vision_backbone_id.startswith(v) for v in [\\\"dinoclip\\\", \\\"dinosiglip\\\"])\\n109:        self.timm_model_ids = VISION_BACKBONE_TO_TIMM_ID[self.vision_backbone_id]\\n110:        self.timm_override_act_layers = TIMM_OVERRIDE_ACT_LAYER[self.vision_backbone_id]\\n111:        self.image_sizes = VISION_BACKBONE_TO_RESOLUTION[self.vision_backbone_id]\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-attention-feasibility_20260524T014932",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-24T01:51:00.574586+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "grep -rn \"projector\" /root/autodl-tmp/openvla-repo/prismatic/extern/hf/modeling_prismatic.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-attention-feasibility_20260524T014932",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "grep -rn \"projector\" /root/autodl-tmp/openvla-repo/prismatic/extern/hf/modeling_prismatic.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-24T01:51:00.574713+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"173:    projector_features: Optional[torch.FloatTensor] = None\\n241:        self.projector = PrismaticProjector(\\n302:        output_projector_features: Optional[bool] = None,\\n310:        output_projector_features = output_projector_features if output_projector_features is not None else False\\n369:            projected_patch_embeddings = self.projector(patch_features)\\n435:            if output_projector_features and (projected_patch_embeddings is not None):\\n446:            projector_features=projected_patch_embeddings,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-attention-feasibility_20260524T014932",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-24T01:51:00.574833+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-27271",
  "command": "cat /root/autodl-tmp/openvla-libero-object/config.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_openvla-attention-feasibility_20260524T014932",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-27271",
    "command": "cat /root/autodl-tmp/openvla-libero-object/config.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-24T01:51:00.575014+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"_name_or_path\\\": \\\"openvla/openvla-7b\\\",\\n  \\\"arch_specifier\\\": \\\"no-align+fused-gelu-mlp\\\",\\n  \\\"architectures\\\": [\\n    \\\"OpenVLAForActionPrediction\\\"\\n  ],\\n  \\\"auto_map\\\": {\\n    \\\"AutoConfig\\\": \\\"configuration_prismatic.OpenVLAConfig\\\",\\n    \\\"AutoModelForVision2Seq\\\": \\\"modeling_prismatic.OpenVLAForActionPrediction\\\"\\n  },\\n  \\\"hf_llm_id\\\": \\\"meta-llama/Llama-2-7b-hf\\\",\\n  \\\"image_resize_strategy\\\": \\\"resize-naive\\\",\\n  \\\"image_sizes\\\": [\\n    224,\\n    224\\n  ],\\n  \\\"llm_backbone_id\\\": \\\"llama2-7b-pure\\\",\\n  \\\"llm_max_length\\\": 2048,\\n  \\\"model_type\\\": \\\"openvla\\\",\\n  \\\"n_action_bins\\\": 256,\\n  \\\"norm_stats\\\": {\\n    \\\"libero_object\\\": {\\n      \\\"action\\\": {\\n        \\\"mean\\\": [\\n          0.07096529006958008,\\n          0.13498851656913757,\\n          -0.04601382836699486,\\n          0.00123520044144243,\\n          0.006998839322477579,\\n          -0.015027612447738647,\\n          0.46428999304771423\\n        ],\\n        \\\"std\\\": [\\n          0.2681235373020172,\\n          0.43846824765205383,\\n          0.4474974274635315,\\n          0.024446550756692886,\\n          0.049355510622262955,\\n          0.042107198387384415,\\n          0.49879148602485657\\n        ],\\n        \\\"max\\\": [\\n          0.9375,\\n          0.8919642567634583,\\n          0.9375,\\n          0.17678570747375488,\\n          0.35035714507102966,\\n          0.1810714304447174,\\n          1.0\\n        ],\\n        \\\"min\\\": [\\n          -0.8839285969734192,\\n          -0.9375,\\n          -0.9375,\\n          -0.15000000596046448,\\n          -0.29035714268684387,\\n          -0.32892856001853943,\\n          0.0\\n        ],\\n        \\\"q01\\\": [\\n          -0.5383928418159485,\\n          -0.8758928775787354,\\n          -0.9375,\\n          -0.06964285671710968
…[truncated 2379 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_openvla-attention-feasibility_20260524T014932",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-24T01:51:00.575234+00:00_

信息收集完毕。

## OpenVLA Attention Pruning 可行性

- **当前支持的 mode 列表**: `baseline`, `random_prune`, `l2norm_prune`, `attention_prune` （在 `eval_openvla_l2norm_libero.py` 中）

- **Attention mode 是否已实现**: **YES** — 完整实现，可直接运行

- **实现方式**: `AttentionPruningHook` 类，挂载在 `vla.projector` 的 forward hook 上。具体做法：
  - 取 vision token embeddings（projector 输出），送入 LLM backbone（Llama-2-7b）的**前 2 层** encoder layer
  - 对每层做 self-attention（含 RoPE），收集 attention weights
  - 对 2 层 attention 取平均 → 对 heads 取平均 → column-sum 得到每个 vision token 的 importance score
  - TopK 保留，保持 spatial order

- **可直接用的命令模板**:
  ```bash
  CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl python eval_openvla_l2norm_libero.py \
      --mode attention_prune \
      --k_ratio 0.5 \
      --suite libero_object \
      --num_episodes 50 \
      --seed 42
  ```

- **OpenVLA vision encoder 架构**: `dinosiglip-vit-so-224px`（fused backbone），由两个 ViT 组成：
  - `vit_large_patch14_reg4_dinov2.lvd142m` (DINOv2 ViT-L/14, 224px → 16×16=256 patches + 4 reg = 260 tokens)
  - `vit_so400m_patch14_siglip_224` (SigLIP ViT-SO400M/14, 224px → 16×16=256 tokens)
  - Fused 后经 projector 输出，vision token 数量可通过 `count_vision_tokens()` 确认（代码中已有该函数，会在运行时打印）

- **与 X-VLA attention pruning 的区别**: X-VLA 版本（`eval_xvla_attention_pruning_libero.py`）用的是 BART encoder 的 self-attention（支持 `attention_last`/`attention_mean`/`attention_rollout` 三种模式）。OpenVLA 版本因为没有独立 encoder，用 LLM 前 2 层做 probe，只有一种模式（2-layer mean attention）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_openvla-attention-feasibility_20260524T014932"
}
```

</details>

---
