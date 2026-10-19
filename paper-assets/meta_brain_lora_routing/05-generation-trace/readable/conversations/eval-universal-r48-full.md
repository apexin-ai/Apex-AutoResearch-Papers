# eval universal r48 full

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/chats/worker_eval_universal_r48_full_20260517T003038.jsonl`
- **Structured JSON:** [`5afad4aaeabba293eaee.json`](../../sessions/5a/5afad4aaeabba293eaee.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

17 recorded events

### Tool call

_source line 1 · 2026-05-17T00:32:21.980382+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_universal_r48_full_20260517T003038",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-17T00:32:21.980723+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_universal_r48_full_20260517T003038",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-17T00:32:21.980918+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34142",
  "command": "head -80 /root/meta_brain_lora_routing/phase1/eval_lora_openpi.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_universal_r48_full_20260517T003038",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34142",
    "command": "head -80 /root/meta_brain_lora_routing/phase1/eval_lora_openpi.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-17T00:32:21.981100+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nEvaluate v3 LoRA experts using OpenPI Policy pipeline + LoRA weight injection.\\n\\nUses the working OpenPIMetaBrainPolicy (60% baseline on nominal) and injects\\nLoRA deltas around model.forward() for proper evaluation.\\n\\nRouting modes:\\n  - none: baseline (no LoRA)\\n  - universal: inject single universal LoRA adapter\\n  - par: PAR router selects among 3 experts per-observation\\n\\\"\\\"\\\"\\n\\nfrom jaxtyping import config as _jt_config\\n_jt_config.update('jaxtyping_disable', True)\\n\\nimport sys\\nsys.path.insert(0, '/root/meta_brain_lora_routing/phase1')\\nsys.path.insert(0, '/root/openpi/src')\\nsys.path.insert(0, '/root/openpi')\\n\\nimport argparse\\nimport collections\\nimport json\\nimport logging\\nimport math\\nimport os\\nimport random\\nimport time\\nfrom pathlib import Path\\n\\nimport numpy as np\\nimport safetensors.torch\\nimport torch\\nimport torch.nn as nn\\n\\nlog = logging.getLogger(__name__)\\n\\n# Ensure CUDA determinism for diffusion noise reproducibility\\ntorch.backends.cudnn.deterministic = True\\ntorch.backends.cudnn.benchmark = False\\n\\n# ---------------------------------------------------------------------------\\n# LoRA injection utilities\\n# ---------------------------------------------------------------------------\\n\\ndef _get_submodule(model, path):\\n    parts = path.split(\\\".\\\")\\n    m = model\\n    for part in parts:\\n        m = getattr(m, part)\\n    return m\\n\\n\\nclass LoRAInjector:\\n    \\\"\\\"\\\"Load LoRA adapters and inject/restore weight deltas.\\\"\\\"\\\"\\n\\n    def __init__(self, model, device):\\n        self.model = model\\n        self.device = device\\n        self.experts = {}\\n        self.scaling = 2.0  # alpha/rank = 32/16\\n        self._frozen_weights = {}\\n\\n    def load_adapter(self, name, adapter_dir):\\n        \\\"\\\"\\\"Load PEFT adapter from checkpoint directory.\\\"\\\"\\\"\\n        safetensors_pat
…[truncated 958 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_universal_r48_full_20260517T003038",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-17T00:32:21.981254+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34142",
  "command": "grep -n \"add_argument\\|argparse\" /root/meta_brain_lora_routing/phase1/eval_lora_openpi.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_universal_r48_full_20260517T003038",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34142",
    "command": "grep -n \"add_argument\\|argparse\" /root/meta_brain_lora_routing/phase1/eval_lora_openpi.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-17T00:32:21.981389+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_universal_r48_full_20260517T003038",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-17T00:32:21.981567+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34142",
  "command": "grep -n \"add_argument\" /root/meta_brain_lora_routing/phase1/eval_lora_openpi.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_universal_r48_full_20260517T003038",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34142",
    "command": "grep -n \"add_argument\" /root/meta_brain_lora_routing/phase1/eval_lora_openpi.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-17T00:32:21.981719+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"306:    p.add_argument(\\\"--routing\\\", choices=[\\\"none\\\", \\\"universal\\\", \\\"par\\\"], default=\\\"universal\\\")\\n307:    p.add_argument(\\\"--perturbation_types\\\", default=\\\"background_textures\\\")\\n308:    p.add_argument(\\\"--task_suite\\\", default=\\\"libero_spatial\\\")\\n309:    p.add_argument(\\\"--num_episodes\\\", type=int, default=20)\\n310:    p.add_argument(\\\"--seeds\\\", default=\\\"42\\\")\\n311:    p.add_argument(\\\"--gpu\\\", type=int, default=0)\\n313:    p.add_argument(\\\"--lora_universal_dir\\\", default=\\\"\\\")\\n314:    p.add_argument(\\\"--lora_visual_dir\\\", default=\\\"\\\")\\n315:    p.add_argument(\\\"--lora_spatial_dir\\\", default=\\\"\\\")\\n316:    p.add_argument(\\\"--lora_physical_dir\\\", default=\\\"\\\")\\n317:    p.add_argument(\\\"--router_checkpoint\\\", default=\\\"\\\")\\n318:    p.add_argument(\\\"--pi0_checkpoint\\\", default=\\\"/root/autodl-tmp/checkpoints/pi0_libero\\\")\\n320:    p.add_argument(\\\"--output_dir\\\", default=\\\"/root/meta_brain_lora_routing/phase1/outputs\\\")\\n321:    p.add_argument(\\\"--no_wandb\\\", action=\\\"store_true\\\", default=True)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_universal_r48_full_20260517T003038",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-17T00:32:21.981883+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34142",
  "command": "tail -100 /root/meta_brain_lora_routing/phase1/eval_lora_openpi.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_universal_r48_full_20260517T003038",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34142",
    "command": "tail -100 /root/meta_brain_lora_routing/phase1/eval_lora_openpi.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-17T00:32:21.982069+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\n    logging.basicConfig(level=logging.INFO, format=\\\"%(asctime)s [%(levelname)s] %(message)s\\\")\\n\\n    device = f\\\"cuda:{args.gpu}\\\"\\n    seeds = [int(s) for s in args.seeds.split(\\\",\\\")]\\n    perturbation_types = args.perturbation_types.split(\\\",\\\")\\n\\n    # Load OpenPI policy (working baseline)\\n    from openpi_metabrain_policy import OpenPIMetaBrainPolicy\\n    log.info(\\\"Loading OpenPI policy...\\\")\\n    policy_wrapper = OpenPIMetaBrainPolicy.from_checkpoint(\\n        checkpoint_path=args.pi0_checkpoint,\\n        routing_mode='none',\\n        device=device,\\n        use_delta_actions=True,\\n    )\\n    # Suppress diagnostic prints after first few\\n    policy_wrapper._diag_max = 2\\n\\n    # Setup LoRA injector\\n    lora_injector = None\\n    router = None\\n\\n    if args.routing == \\\"universal\\\" and args.lora_universal_dir:\\n        lora_injector = LoRAInjector(policy_wrapper.model, torch.device(device))\\n        lora_injector.load_adapter(\\\"universal\\\", args.lora_universal_dir)\\n    elif args.routing == \\\"par\\\":\\n        lora_injector = LoRAInjector(policy_wrapper.model, torch.device(device))\\n        if args.lora_visual_dir:\\n            lora_injector.load_adapter(\\\"visual\\\", args.lora_visual_dir)\\n        if args.lora_spatial_dir:\\n            lora_injector.load_adapter(\\\"spatial\\\", args.lora_spatial_dir)\\n        if args.lora_physical_dir:\\n            lora_injector.load_adapter(\\\"physical\\\", args.lora_physical_dir)\\n        if args.router_checkpoint:\\n            router = PARRouterLite(args.router_checkpoint, policy_wrapper.model, torch.device(device))\\n            log.info(\\\"PAR router loaded from %s\\\", args.router_checkpoint)\\n\\n    # Run evaluation\\n    all_results = {}\\n    for ptype in perturbation_types:\\n        log.info(\\\"Evaluating: %s (routing=%s)\\\", ptype, args.routing)\\n        ptype_results = []\\n\\n 
…[truncated 2871 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_universal_r48_full_20260517T003038",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-17T00:32:21.982267+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-34142",
  "command": "cd /root/meta_brain_lora_routing && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && nohup bash -c 'CUDA_VISIBLE_DEVICES=1 python phase1/eval_lora_openpi.py --routing universal --lora_universal_dir /root/autodl-tmp/checkpoints/v3_lora_universal_r48/v3_r48lora_universal_r48/final/ --seeds 42,123,456 --num_episodes 20 --gpu 0 --perturbation_types nominal,background_textures,objects_layout,robot_initial_states,camera_viewpoints,light_conditions,sensor_noise,language 2>&1' > /root/meta_brain_lora_routing/phase1/outputs/eval_universal_r48_full.log 2>&1 & echo $!",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_universal_r48_full_20260517T003038",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-34142",
    "command": "cd /root/meta_brain_lora_routing && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && nohup bash -c 'CUDA_VISIBLE_DEVICES=1 python phase1/eval_lora_openpi.py --routing universal --lora_universal_dir /root/autodl-tmp/checkpoints/v3_lora_universal_r48/v3_r48lora_universal_r48/final/ --seeds 42,123,456 --num_episodes 20 --gpu 0 --perturbation_types nominal,background_textures,objects_layout,robot_initial_states,camera_viewpoints,light_conditions,sensor_noise,language 2>&1' > /root/meta_brain_lora_routing/phase1/outputs/eval_universal_r48_full.log 2>&1 & echo $!",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-17T00:32:21.982410+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Command did not complete within 30 seconds!\\n\\nCommand: \\\"cd /root/meta_brain_lora_routing && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && nohup bash -c 'CUDA_VISIBLE_DEVICES=1 python phase1/eval_lora_openpi.py --routing universal --lora_universal_dir /root/autodl-tmp/checkpoints/v3_lora_universal_r48/v3_r48lora_universal_r48/final/ --seeds 42,123,456 --num_episodes 20 --gpu 0 --perturbation_types nominal,background_textures,objects_layout,robot_initial_states,camera_viewpoints,light_conditions,sensor_noise,language 2>&1' > /root/meta_brain_lora_routing/phase1/outputs/eval_universal_r48_full.log 2>&1 & echo $!\\\"\\n\\nStdout:\\n\\n493562\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 30.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_universal_r48_full_20260517T003038",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-17T00:32:21.982590+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34142",
  "command": "tail -20 /root/meta_brain_lora_routing/phase1/outputs/eval_universal_r48_full.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_universal_r48_full_20260517T003038",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34142",
    "command": "tail -20 /root/meta_brain_lora_routing/phase1/outputs/eval_universal_r48_full.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-17T00:32:21.982721+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-17 08:31:29,486 [INFO] Loading OpenPI policy...\\n2026-05-17 08:31:32,744 [INFO] Loading pi0_libero via openpi Policy (device=cuda:0, delta=True)\\n2026-05-17 08:31:32,744 [INFO] Using cached converted checkpoint: /root/autodl-tmp/checkpoints/pi0_libero_openpi_converted.safetensors\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.06}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_universal_r48_full_20260517T003038",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-17T00:32:21.982863+00:00_

called ScheduleWakeup

<details open><summary>🔧 Tool call — ScheduleWakeup</summary>

````json
{
  "delaySeconds": "120",
  "reason": "Wait for model loading and first few episodes to complete before checking progress",
  "prompt": "## 任务：Universal r48 全覆盖 eval（cuda:1 ONLY）\n\n### 严格 GPU 隔离\n**CUDA_VISIBLE_DEVICES=1**，不动其他卡。\n\n### 配置\n- LoRA checkpoint: v3_lora_universal_r48\n  路径：`/root/autodl-tmp/checkpoints/v3_lora_universal_r48/v3_r48lora_universal_r48/final/`\n- routing: none（注入 universal r48）\n- seeds: [42, 123, 456]\n- episodes: 20 per seed per perturbation\n\n### 评估全部 8 类\n1. nominal\n2. background_textures\n3. objects_layout\n4. robot_initial_states\n5. camera_viewpoints\n6. light_conditions\n7. sensor_noise\n8. language\n\n### 执行\n```bash\ncd /root/meta_brain_lora_routing\nCUDA_VISIBLE_DEVICES=1 python phase1/eval_lora_openpi.py \\\n    --routing none \\\n    --lora_checkpoint /root/autodl-tmp/checkpoints/v3_lora_universal_r48/v3_r48lora_universal_r48/final/ \\\n    --seeds 42 123 456 \\\n    --num_episodes 20 \\\n    --perturbations nominal background_textures objects_layout robot_initial_states camera_viewpoints light_conditions sensor_noise language\n```\n\n先检查脚本 argparse 确定参数名。用 submit_training_job 提交。\n\n### 重要\n- 等 eval 跑完再退出\n- 返回每类扰动的 mean ± std\n- 这是 plan_013 parameter-matched control：对比 r16（61.6% 均值）看 rank scaling 效果\n\n### 产出\n- 8 类扰动的 success rate (mean ± std)\n- 与 universal r16 对比的 delta（r16 均值 61.6%）\n- rank scaling 结论"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_eval_universal_r48_full_20260517T003038",
  "tool": "ScheduleWakeup",
  "tool_args": {
    "delaySeconds": "120",
    "reason": "Wait for model loading and first few episodes to complete before checking progress",
    "prompt": "## 任务：Universal r48 全覆盖 eval（cuda:1 ONLY）\n\n### 严格 GPU 隔离\n**CUDA_VISIBLE_DEVICES=1**，不动其他卡。\n\n### 配置\n- LoRA checkpoint: v3_lora_universal_r48\n  路径：`/root/autodl-tmp/checkpoints/v3_lora_universal_r48/v3_r48lora_universal_r48/final/`\n- routing: none（注入 universal r48）\n- seeds: [42, 123, 456]\n- episodes: 20 per seed per perturbation\n\n### 评估全部 8 类\n1. nominal\n2. background_textures\n3. objects_layout\n4. robot_initial_states\n5. camera_viewpoints\n6. light_conditions\n7. sensor_noise\n8. language\n\n### 执行\n```bash\ncd /root/meta_brain_lora_routing\nCUDA_VISIBLE_DEVICES=1 python phase1/eval_lora_openpi.py \\\n    --routing none \\\n    --lora_checkpoint /root/autodl-tmp/checkpoints/v3_lora_universal_r48/v3_r48lora_universal_r48/final/ \\\n    --seeds 42 123 456 \\\n    --num_episodes 20 \\\n    --perturbations nominal background_textures objects_layout robot_initial_states camera_viewpoints light_conditions sensor_noise language\n```\n\n先检查脚本 argparse 确定参数名。用 submit_training_job 提交。\n\n### 重要\n- 等 eval 跑完再退出\n- 返回每类扰动的 mean ± std\n- 这是 plan_013 parameter-matched control：对比 r16（61.6% 均值）看 rank scaling 效果\n\n### 产出\n- 8 类扰动的 success rate (mean ± std)\n- 与 universal r16 对比的 delta（r16 均值 61.6%）\n- rank scaling 结论"
  }
}
````

</details>

---

### Tool result

_source line 16 · 2026-05-17T00:32:21.983004+00:00_

Next wakeup scheduled for 00:35:00 (in 161s).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_universal_r48_full_20260517T003038",
  "tool": "ScheduleWakeup",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-17T00:32:21.983150+00:00_

Eval 已启动 (PID 493562)，模型正在加载。2 分钟后检查进度。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_eval_universal_r48_full_20260517T003038"
}
```

</details>

---
