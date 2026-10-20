# code recovery eval dev

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 77
- **Recorded user turns:** 0
- **Tool calls:** 38
- **Original source:** `logs/chats/worker_code_recovery-eval-dev_20260514T173802.jsonl`
- **Structured JSON:** [`19f7d6f31bf24a2a7cc8.json`](../../sessions/19/19f7d6f31bf24a2a7cc8.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

77 recorded events

### Tool call

_source line 1 · 2026-05-14T17:45:48.175866+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact",
  "max_results": "6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_recovery-eval-dev_20260514T173802",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact",
    "max_results": "6"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-14T17:45:48.176196+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_recovery-eval-dev_20260514T173802",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T17:45:48.176406+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/tax_error_inject_agent/eval/recovery.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_recovery-eval-dev_20260514T173802",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/tax_error_inject_agent/eval/recovery.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-14T17:45:48.176766+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"TaxEI Recovery Evaluation — evaluate injection recovery and baseline success.\\\"\\\"\\\"\\nfrom __future__ import annotations\\n\\nimport argparse\\nimport copy\\nimport json\\nimport os\\nimport random\\nimport re\\nimport sys\\nimport time\\nfrom collections import defaultdict\\nfrom datetime import datetime, timezone\\nfrom difflib import SequenceMatcher\\nfrom pathlib import Path\\nfrom typing import Any, Dict, List, Optional, Tuple\\n\\nimport numpy as np\\nimport torch\\nfrom scipy.stats import chi2\\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\\nfrom peft import PeftModel\\n\\nimport textworld\\nimport textworld.gym\\nfrom alfworld.agents.environment.alfred_tw_env import AlfredDemangler, AlfredInfos\\n\\nPROJECT_ROOT = Path(__file__).resolve().parent.parent\\nsys.path.insert(0, str(PROJECT_ROOT))\\n\\nfrom injection import (\\n    P1_StepOrderSwap,\\n    P2_SubGoalDeletion,\\n    C1_ContextTruncation,\\n    C4_ObservationMasking,\\n)\\n\\nMAX_STEPS = 50\\nHISTORY_WINDOW = 10\\n\\nOPERATORS = [\\n    P1_StepOrderSwap(),\\n    P2_SubGoalDeletion(),\\n    C1_ContextTruncation(),\\n    C4_ObservationMasking(),\\n]\\n\\nOPERATOR_CONFIGS = {\\n    \\\"P1_step_order_swap\\\": {\\\"swap_range\\\": 5},\\n    \\\"P2_sub_goal_deletion\\\": {\\\"deletion_strategy\\\": \\\"critical\\\"},\\n    \\\"C1_context_truncation\\\": {\\\"truncation_ratio\\\": 0.5},\\n    \\\"C4_observation_masking\\\": {\\\"mask_type\\\": \\\"generic\\\", \\\"max_masks\\\": 2},\\n}\\n\\n\\n# ---------------------------------------------------------------------------\\n# Prompt (identical to collect_trajectories.py)\\n# ---------------------------------------------------------------------------\\n\\ndef build_prompt(\\n    task_desc: str,\\n    step_count: int,\\n    history: List[Dict[str, str]],\\n    current_obs: str,\\n    admissible_commands: List[str],\\n) -> str:\\n    history_str =
…[truncated 7165 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_recovery-eval-dev_20260514T173802",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T17:45:48.177019+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls /root/autodl-tmp/tax_error_inject_agent/eval/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_recovery-eval-dev_20260514T173802",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls /root/autodl-tmp/tax_error_inject_agent/eval/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-14T17:45:48.177207+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"__init__.py\\n__pycache__\\neval_tasks_47.json\\nrecovery.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_recovery-eval-dev_20260514T173802",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-14T17:45:48.177383+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls /root/autodl-tmp/tax_error_inject_agent/src/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_recovery-eval-dev_20260514T173802",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls /root/autodl-tmp/tax_error_inject_agent/src/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T17:45:48.177587+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/autodl-tmp/tax_error_inject_agent/src/': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.3}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_recovery-eval-dev_20260514T173802",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T17:45:48.177784+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls /root/autodl-tmp/tax_error_inject_agent/scripts/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_recovery-eval-dev_20260514T173802",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls /root/autodl-tmp/tax_error_inject_agent/scripts/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T17:45:48.177929+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"analyze_gate3.py\\nrun_v3_eval.sh\\nrun_v4_eval.sh\\nverify_gate1.py\\nverify_gate2.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_recovery-eval-dev_20260514T173802",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T17:45:48.178060+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls /root/autodl-tmp/tax_error_inject_agent/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_recovery-eval-dev_20260514T173802",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls /root/autodl-tmp/tax_error_inject_agent/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T17:45:48.178178+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"checkpoints\\nconfigs\\ndata\\ndocs\\neval\\neval_results\\ninjection\\nlogs\\nscripts\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_recovery-eval-dev_20260514T173802",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T17:45:48.178289+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/tax_error_inject_agent/scripts/run_v4_eval.sh",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_recovery-eval-dev_20260514T173802",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/tax_error_inject_agent/scripts/run_v4_eval.sh",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T17:45:48.178443+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/bin/bash\\n# v4 taxei / random eval 启动脚本\\n# 用法: bash scripts/run_v4_eval.sh [taxei|random|both]\\nset -e\\n\\ncd /root/autodl-tmp/tax_error_inject_agent\\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base\\n\\nBASEM=/root/autodl-tmp/models/Qwen/Qwen3-8B\\nmkdir -p eval_results\\n\\n# 在指定 checkpoint 目录下找最新 run 的最大 step checkpoint\\nfind_final_ckpt() {\\n    local ckpt_root=$1\\n    # 最新 run（按目录名排序取最后）\\n    local latest_run\\n    latest_run=$(ls -dt \\\"$ckpt_root\\\"/v*-*/ 2>/dev/null | head -1)\\n    if [ -z \\\"$latest_run\\\" ]; then\\n        echo \\\"ERROR: no run dir in $ckpt_root\\\" >&2; return 1\\n    fi\\n    # 最大 step checkpoint\\n    local final\\n    final=$(ls -d \\\"$latest_run\\\"/checkpoint-* 2>/dev/null | sort -V | tail -1)\\n    if [ -z \\\"$final\\\" ]; then\\n        echo \\\"ERROR: no checkpoint in $latest_run\\\" >&2; return 1\\n    fi\\n    # 确认 adapter_config.json 存在\\n    if [ ! -f \\\"$final/adapter_config.json\\\" ]; then\\n        echo \\\"ERROR: $final missing adapter_config.json\\\" >&2; return 1\\n    fi\\n    echo \\\"$final\\\"\\n}\\n\\nrun_taxei() {\\n    local ckpt\\n    ckpt=$(find_final_ckpt checkpoints/mini_taxei_sft_v4)\\n    echo \\\"[taxei] checkpoint: $ckpt\\\"\\n    CUDA_VISIBLE_DEVICES=0 python eval/recovery.py \\\\\\n        --model_path \\\"$ckpt\\\" \\\\\\n        --base_model \\\"$BASEM\\\" \\\\\\n        --no_inject \\\\\\n        --output eval_results/v4_taxei_eval.json \\\\\\n        --device cuda:0\\n}\\n\\nrun_random() {\\n    local ckpt\\n    ckpt=$(find_final_ckpt checkpoints/mini_random_sft_v4)\\n    echo \\\"[random] checkpoint: $ckpt\\\"\\n    CUDA_VISIBLE_DEVICES=1 python eval/recovery.py \\\\\\n        --model_path \\\"$ckpt\\\" \\\\\\n        --base_model \\\"$BASEM\\\" \\\\\\n        --no_inject \\\\\\n        --output eval_results/v4_random_eval.json \\\\\\n        --device cuda:0\\n}\\n\\ncase \\\"${1:-both}\\\" in\\n    ta
…[truncated 696 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_recovery-eval-dev_20260514T173802",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T17:45:48.178629+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls /root/autodl-tmp/tax_error_inject_agent/injection/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_recovery-eval-dev_20260514T173802",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls /root/autodl-tmp/tax_error_inject_agent/injection/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T17:45:48.178758+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"__init__.py\\n__pycache__\\nbase.py\\ncontext.py\\nplanning.py\\nrandom_injector.py\\ntest_random_injector.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_recovery-eval-dev_20260514T173802",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-14T17:45:48.178872+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/tax_error_inject_agent/injection/__init__.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_recovery-eval-dev_20260514T173802",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/tax_error_inject_agent/injection/__init__.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T17:45:48.178995+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"from .base import InjectionOperator, ErrorInjectMemory, ErrorInjectEnvManager, InjectionRecord\\nfrom .planning import P1_StepOrderSwap, P2_SubGoalDeletion\\nfrom .context import C1_ContextTruncation, C4_ObservationMasking\\nfrom .random_injector import RandomInjector\\n\\n__all__ = [\\n    \\\"InjectionOperator\\\", \\\"ErrorInjectMemory\\\", \\\"ErrorInjectEnvManager\\\", \\\"InjectionRecord\\\",\\n    \\\"P1_StepOrderSwap\\\", \\\"P2_SubGoalDeletion\\\",\\n    \\\"C1_ContextTruncation\\\", \\\"C4_ObservationMasking\\\",\\n    \\\"RandomInjector\\\",\\n]\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_recovery-eval-dev_20260514T173802",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-14T17:45:48.179098+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/tax_error_inject_agent/injection/base.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_recovery-eval-dev_20260514T173802",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/tax_error_inject_agent/injection/base.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-14T17:45:48.179265+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nTaxEI Injection Base Module\\n===========================\\nDefines the InjectionOperator ABC, ErrorInjectMemory (extends verl-agent SimpleMemory),\\nand ErrorInjectEnvManager (extends AlfWorldEnvironmentManager).\\n\\nKey design decision: verl-agent has NO explicit plan state. \\\"Planning\\\" errors (P1/P2)\\nare injected by tampering with the action-observation history so the agent faces\\nstate inconsistencies — it must recognize and recover from corrupted history.\\n\\nDependencies:\\n    - verl-agent at /root/autodl-tmp/verl-agent/\\n      (agent_system.memory.memory.SimpleMemory)\\n      (agent_system.environments.env_manager.AlfWorldEnvironmentManager)\\n\\\"\\\"\\\"\\nfrom __future__ import annotations\\n\\nimport copy\\nimport sys\\nfrom abc import ABC, abstractmethod\\nfrom dataclasses import dataclass, field\\nfrom typing import Any, Dict, List, Optional, Tuple\\n\\nVERL_AGENT_PATH = \\\"/root/autodl-tmp/verl-agent\\\"\\nif VERL_AGENT_PATH not in sys.path:\\n    sys.path.insert(0, VERL_AGENT_PATH)\\n\\nfrom agent_system.memory.memory import SimpleMemory\\nfrom agent_system.environments.env_manager import AlfWorldEnvironmentManager\\n\\n\\n@dataclass\\nclass InjectionRecord:\\n    env_idx: int\\n    step_idx: int\\n    operator_name: str\\n    before: Any\\n    after: Any\\n\\n\\nclass InjectionOperator(ABC):\\n    \\\"\\\"\\\"Base class for all error-injection operators.\\\"\\\"\\\"\\n    name: str = \\\"base\\\"\\n    category: str = \\\"base\\\"\\n\\n    @abstractmethod\\n    def inject(self, trajectory: List[Dict[str, Any]], env_idx: int, step_idx: int, config: Dict[str, Any]) -> List[Dict[str, Any]]:\\n        \\\"\\\"\\\"Apply injection to a single trajectory. Returns a new list.\\\"\\\"\\\"\\n        ...\\n\\n    @abstractmethod\\n    def validate(self, original: List[Dict[str, Any]], modified: List[Dict[str, Any]]) -> bool:\\n        \\\"\\\"\\\"Check post-injection trajectory 
…[truncated 3830 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_recovery-eval-dev_20260514T173802",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-14T17:45:48.179394+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/tax_error_inject_agent/injection/planning.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_recovery-eval-dev_20260514T173802",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/tax_error_inject_agent/injection/planning.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-14T17:45:48.179559+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nTaxEI Planning Injection Operators: P1 (Step-Order Swap), P2 (Sub-Goal Deletion)\\n================================================================================\\nverl-agent has NO explicit plan state. These operators tamper with the\\naction-observation *history* so the agent faces temporal/causal inconsistencies.\\n\\\"\\\"\\\"\\nfrom __future__ import annotations\\nimport copy\\nimport random\\nfrom typing import Any, Dict, List\\nfrom .base import InjectionOperator\\n\\n\\nclass P1_StepOrderSwap(InjectionOperator):\\n    \\\"\\\"\\\"Swap two adjacent steps in the trajectory history.\\\"\\\"\\\"\\n    name = \\\"P1_step_order_swap\\\"\\n    category = \\\"planning\\\"\\n\\n    def inject(self, trajectory: List[Dict[str, Any]], env_idx: int, step_idx: int, config: Dict[str, Any]) -> List[Dict[str, Any]]:\\n        traj = copy.deepcopy(trajectory)\\n        if len(traj) < 2:\\n            return traj\\n        swap_range = config.get(\\\"swap_range\\\", 5)\\n        window_start = max(0, len(traj) - swap_range)\\n        candidates = list(range(window_start, len(traj) - 1))\\n        if not candidates:\\n            return traj\\n        idx = random.choice(candidates)\\n        traj[idx], traj[idx + 1] = traj[idx + 1], traj[idx]\\n        return traj\\n\\n    def validate(self, original: List[Dict[str, Any]], modified: List[Dict[str, Any]]) -> bool:\\n        return len(original) == len(modified)\\n\\n\\nclass P2_SubGoalDeletion(InjectionOperator):\\n    \\\"\\\"\\\"Delete a step from the trajectory history, simulating a missed sub-goal.\\\"\\\"\\\"\\n    name = \\\"P2_sub_goal_deletion\\\"\\n    category = \\\"planning\\\"\\n    CRITICAL_ACTIONS = {\\\"pick\\\", \\\"put\\\", \\\"heat\\\", \\\"cool\\\", \\\"clean\\\", \\\"use\\\", \\\"open\\\", \\\"close\\\", \\\"toggle\\\"}\\n\\n    def inject(self, trajectory: List[Dict[str, Any]], env_idx: int, step_idx: int, config: Dict[str, Any]) -> Li
…[truncated 1107 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_recovery-eval-dev_20260514T173802",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-14T17:45:48.179706+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/tax_error_inject_agent/injection/context.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_recovery-eval-dev_20260514T173802",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/tax_error_inject_agent/injection/context.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-14T17:45:48.179847+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nTaxEI Context Injection Operators: C1 (Context Truncation), C4 (Observation Masking)\\n====================================================================================\\nC1: Truncates early history. C4: Replaces observations with empty/generic text.\\n\\\"\\\"\\\"\\nfrom __future__ import annotations\\nimport copy\\nimport math\\nimport random\\nfrom typing import Any, Dict, List\\nfrom .base import InjectionOperator\\n\\n\\nclass C1_ContextTruncation(InjectionOperator):\\n    \\\"\\\"\\\"Truncate trajectory history to simulate lost context.\\\"\\\"\\\"\\n    name = \\\"C1_context_truncation\\\"\\n    category = \\\"context\\\"\\n\\n    def inject(self, trajectory: List[Dict[str, Any]], env_idx: int, step_idx: int, config: Dict[str, Any]) -> List[Dict[str, Any]]:\\n        traj = copy.deepcopy(trajectory)\\n        if len(traj) <= 1:\\n            return traj\\n        ratio = config.get(\\\"truncation_ratio\\\", 0.5)\\n        ratio = max(0.3, min(0.7, ratio))\\n        keep_count = max(1, math.ceil(len(traj) * ratio))\\n        return traj[-keep_count:]\\n\\n    def validate(self, original: List[Dict[str, Any]], modified: List[Dict[str, Any]]) -> bool:\\n        return len(modified) >= 1\\n\\n\\nGENERIC_OBS = \\\"You see nothing special.\\\"\\n\\n\\nclass C4_ObservationMasking(InjectionOperator):\\n    \\\"\\\"\\\"Mask observations with empty or generic text.\\n\\n    Per trajectory, masks at most max_masks steps (default 2), skipping step 0.\\n    This is more realistic than independent per-step masking which makes\\n    recovery impossible when too many consecutive observations are lost.\\n    \\\"\\\"\\\"\\n    name = \\\"C4_observation_masking\\\"\\n    category = \\\"context\\\"\\n\\n    def inject(self, trajectory: List[Dict[str, Any]], env_idx: int, step_idx: int, config: Dict[str, Any]) -> List[Dict[str, Any]]:\\n        traj = copy.deepcopy(trajectory)\\n        if len(traj) <= 1:\
…[truncated 796 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_recovery-eval-dev_20260514T173802",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-14T17:45:48.180002+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "head -250 /root/autodl-tmp/tax_error_inject_agent/eval/recovery.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_recovery-eval-dev_20260514T173802",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "head -250 /root/autodl-tmp/tax_error_inject_agent/eval/recovery.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-14T17:45:48.180238+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"TaxEI Recovery Evaluation — evaluate injection recovery and baseline success.\\\"\\\"\\\"\\nfrom __future__ import annotations\\n\\nimport argparse\\nimport copy\\nimport json\\nimport os\\nimport random\\nimport re\\nimport sys\\nimport time\\nfrom collections import defaultdict\\nfrom datetime import datetime, timezone\\nfrom difflib import SequenceMatcher\\nfrom pathlib import Path\\nfrom typing import Any, Dict, List, Optional, Tuple\\n\\nimport numpy as np\\nimport torch\\nfrom scipy.stats import chi2\\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\\nfrom peft import PeftModel\\n\\nimport textworld\\nimport textworld.gym\\nfrom alfworld.agents.environment.alfred_tw_env import AlfredDemangler, AlfredInfos\\n\\nPROJECT_ROOT = Path(__file__).resolve().parent.parent\\nsys.path.insert(0, str(PROJECT_ROOT))\\n\\nfrom injection import (\\n    P1_StepOrderSwap,\\n    P2_SubGoalDeletion,\\n    C1_ContextTruncation,\\n    C4_ObservationMasking,\\n)\\n\\nMAX_STEPS = 50\\nHISTORY_WINDOW = 10\\n\\nOPERATORS = [\\n    P1_StepOrderSwap(),\\n    P2_SubGoalDeletion(),\\n    C1_ContextTruncation(),\\n    C4_ObservationMasking(),\\n]\\n\\nOPERATOR_CONFIGS = {\\n    \\\"P1_step_order_swap\\\": {\\\"swap_range\\\": 5},\\n    \\\"P2_sub_goal_deletion\\\": {\\\"deletion_strategy\\\": \\\"critical\\\"},\\n    \\\"C1_context_truncation\\\": {\\\"truncation_ratio\\\": 0.5},\\n    \\\"C4_observation_masking\\\": {\\\"mask_type\\\": \\\"generic\\\", \\\"max_masks\\\": 2},\\n}\\n\\n\\n# ---------------------------------------------------------------------------\\n# Prompt (identical to collect_trajectories.py)\\n# ---------------------------------------------------------------------------\\n\\ndef build_prompt(\\n    task_desc: str,\\n    step_count: int,\\n    history: List[Dict[str, str]],\\n    current_obs: str,\\n    admissible_commands: List[str],\\n) -> str:\\n    history_str =
…[truncated 7074 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_recovery-eval-dev_20260514T173802",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-14T17:45:48.180370+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "tail -200 /root/autodl-tmp/tax_error_inject_agent/eval/recovery.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_recovery-eval-dev_20260514T173802",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "tail -200 /root/autodl-tmp/tax_error_inject_agent/eval/recovery.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-14T17:45:48.180584+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"                \\\"rate\\\": round(rate, 3),\\n            }\\n        report[\\\"injection_recovery_rates\\\"] = injection_recovery_rates\\n        report[\\\"overall_recovery_rate\\\"] = round(successes / total, 3) if total else 0\\n\\n    type_results: Dict[str, Dict[str, int]] = defaultdict(\\n        lambda: {\\\"total\\\": 0, \\\"success\\\": 0}\\n    )\\n    for r in results:\\n        tt = r[\\\"task_type\\\"]\\n        type_results[tt][\\\"total\\\"] += 1\\n        if r[\\\"success\\\"]:\\n            type_results[tt][\\\"success\\\"] += 1\\n\\n    report[\\\"by_task_type\\\"] = {\\n        tt: {\\n            \\\"total\\\": c[\\\"total\\\"],\\n            \\\"success\\\": c[\\\"success\\\"],\\n            \\\"rate\\\": round(c[\\\"success\\\"] / c[\\\"total\\\"], 3) if c[\\\"total\\\"] else 0,\\n        }\\n        for tt, c in sorted(type_results.items())\\n    }\\n    report[\\\"episodes\\\"] = results\\n    return report\\n\\n\\n# ---------------------------------------------------------------------------\\n# Compare two result files\\n# ---------------------------------------------------------------------------\\n\\ndef compare_results(\\n    taxei_path: str, vanilla_path: str, output_path: Optional[str] = None\\n) -> Dict[str, Any]:\\n    with open(taxei_path) as f:\\n        taxei = json.load(f)\\n    with open(vanilla_path) as f:\\n        vanilla = json.load(f)\\n\\n    taxei_by_task = {e[\\\"task_name\\\"]: e[\\\"success\\\"] for e in taxei[\\\"episodes\\\"]}\\n    vanilla_by_task = {e[\\\"task_name\\\"]: e[\\\"success\\\"] for e in vanilla[\\\"episodes\\\"]}\\n\\n    common = sorted(set(taxei_by_task) & set(vanilla_by_task))\\n    t_succ = [taxei_by_task[t] for t in common]\\n    v_succ = [vanilla_by_task[t] for t in common]\\n\\n    t_rate = float(np.mean(t_succ))\\n    v_rate = float(np.mean(v_succ))\\n\\n    p = mcnemar_test(t_succ, v_succ)\\n    ci_lo, ci_hi = bootstrap_ci(\\n        [i
…[truncated 6503 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_recovery-eval-dev_20260514T173802",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-14T17:45:48.180729+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "find /root/autodl-tmp/tax_error_inject_agent/data/ -name \"*.py\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_recovery-eval-dev_20260514T173802",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "find /root/autodl-tmp/tax_error_inject_agent/data/ -name \"*.py\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-14T17:45:48.180851+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/tax_error_inject_agent/data/__init__.py\\n/root/autodl-tmp/tax_error_inject_agent/data/formatter.py\\n/root/autodl-tmp/tax_error_inject_agent/data/collect_trajectories.py\\n/root/autodl-tmp/tax_error_inject_agent/data/inject_and_generate.py\\n/root/autodl-tmp/tax_error_inject_agent/data/convert_to_aligned_format.py\\n/root/autodl-tmp/tax_error_inject_agent/data/convert_all_v3.py\\n/root/autodl-tmp/tax_error_inject_agent/data/convert_all_v4.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_recovery-eval-dev_20260514T173802",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-14T17:45:48.180959+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls -dt /root/autodl-tmp/tax_error_inject_agent/checkpoints/mini_taxei_sft_v4/v0-*/ 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_recovery-eval-dev_20260514T173802",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls -dt /root/autodl-tmp/tax_error_inject_agent/checkpoints/mini_taxei_sft_v4/v0-*/ 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-14T17:45:48.181065+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_recovery-eval-dev_20260514T173802",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-14T17:45:48.181183+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls -d /root/autodl-tmp/tax_error_inject_agent/checkpoints/mini_taxei_sft_v4/v0-*/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_recovery-eval-dev_20260514T173802",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls -d /root/autodl-tmp/tax_error_inject_agent/checkpoints/mini_taxei_sft_v4/v0-*/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-14T17:45:48.181296+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/mini_taxei_sft_v4/v0-20260514-212638/\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_recovery-eval-dev_20260514T173802",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-14T17:45:48.181402+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "grep -n \"run_episode\\|def build_report\\|def mcnemar\\|def bootstrap\" /root/autodl-tmp/tax_error_inject_agent/eval/recovery.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_recovery-eval-dev_20260514T173802",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "grep -n \"run_episode\\|def build_report\\|def mcnemar\\|def bootstrap\" /root/autodl-tmp/tax_error_inject_agent/eval/recovery.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-14T17:45:48.181537+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_recovery-eval-dev_20260514T173802",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-14T17:45:48.181742+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/tax_error_inject_agent/data/formatter.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_recovery-eval-dev_20260514T173802",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/tax_error_inject_agent/data/formatter.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-14T17:45:48.182022+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nTaxEI SFT Data Formatter\\n=========================\\nConverts raw + injected ALFWorld trajectories into ms-swift multi-turn SFT format.\\n\\nms-swift format:\\n{\\\"messages\\\": [\\n    {\\\"role\\\": \\\"user\\\", \\\"content\\\": \\\"&lt;observation>\\\"},\\n    {\\\"role\\\": \\\"assistant\\\", \\\"content\\\": \\\"&lt;think>...&lt;/think>\\\\n&lt;action>...&lt;/action>\\\"},\\n    ...\\n]}\\n\\nEach ALFWorld step becomes one user-assistant turn.\\n\\nD004: mode parameter controls error type labeling in injected trajectories.\\n  - mode=taxei: [Error Type: P1_StepOrderSwap] etc. at recovery step\\n  - mode=random: [Error occurred] at recovery step (no taxonomy info)\\n\\\"\\\"\\\"\\nfrom __future__ import annotations\\n\\nimport json\\nfrom pathlib import Path\\nfrom typing import Any, Dict, List, Optional\\n\\n\\nOPERATOR_LABELS = {\\n    \\\"P1_step_order_swap\\\": \\\"P1_StepOrderSwap\\\",\\n    \\\"P2_sub_goal_deletion\\\": \\\"P2_SubGoalDeletion\\\",\\n    \\\"C1_context_truncation\\\": \\\"C1_ContextTruncation\\\",\\n    \\\"C4_observation_masking\\\": \\\"C4_ObservationMasking\\\",\\n}\\n\\n\\ndef _make_error_tag(traj: Dict[str, Any], mode: str) -> str:\\n    injection_info = traj.get(\\\"injection_info\\\")\\n    if not injection_info:\\n        return \\\"\\\"\\n    operator = injection_info.get(\\\"operator\\\", \\\"\\\")\\n    if not operator:\\n        return \\\"\\\"\\n    if mode == \\\"random\\\":\\n        return \\\"[Error occurred]\\\"\\n    label = OPERATOR_LABELS.get(operator, operator)\\n    return f\\\"[Error Type: {label}]\\\"\\n\\n\\ndef format_for_sft(\\n    trajectories: List[Dict[str, Any]],\\n    injected_trajectories: Optional[List[Dict[str, Any]]] = None,\\n    output_path: str = \\\"sft_data.jsonl\\\",\\n    mode: str = \\\"taxei\\\",\\n) -> List[Dict[str, Any]]:\\n    \\\"\\\"\\\"Convert trajectories to ms-swift multi-turn SFT format.\\\"\\\"\\\"\\n    all_trajs = list(traj
…[truncated 2597 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_recovery-eval-dev_20260514T173802",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-14T17:45:48.182299+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "grep -n \"def \" /root/autodl-tmp/tax_error_inject_agent/eval/recovery.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_recovery-eval-dev_20260514T173802",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "grep -n \"def \" /root/autodl-tmp/tax_error_inject_agent/eval/recovery.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-14T17:45:48.182528+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"61:def build_prompt(\\n86:def parse_response(text: str) -> Tuple[str, str]:\\n94:def fuzzy_match_action(action: str, admissible: List[str]) -> str:\\n109:def collect_game_files(data_path: str) -> List[Dict[str, Any]]:\\n150:    def __init__(self, base_model: str, adapter_path: Optional[str] = None,\\n175:    def generate(self, prompt: str, max_new_tokens: int = 512,\\n201:def apply_injection(\\n224:def run_episode(\\n306:def mcnemar_test(successes_a: List[bool], successes_b: List[bool]) -> float:\\n315:def bootstrap_ci(\\n340:def build_report(results: List[Dict[str, Any]], args) -> Dict[str, Any]:\\n399:def compare_results(\\n450:def load_task_list(path: str) -> List[Dict[str, Any]]:\\n465:def main():\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_recovery-eval-dev_20260514T173802",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-14T17:45:48.182723+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "sed -n '224,400p' /root/autodl-tmp/tax_error_inject_agent/eval/recovery.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_recovery-eval-dev_20260514T173802",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "sed -n '224,400p' /root/autodl-tmp/tax_error_inject_agent/eval/recovery.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-14T17:45:48.182904+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'sed' is not in the read-only allowlist. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_recovery-eval-dev_20260514T173802",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-14T17:45:48.183075+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "head -400 /root/autodl-tmp/tax_error_inject_agent/eval/recovery.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_recovery-eval-dev_20260514T173802",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "head -400 /root/autodl-tmp/tax_error_inject_agent/eval/recovery.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-14T17:45:48.183412+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"TaxEI Recovery Evaluation — evaluate injection recovery and baseline success.\\\"\\\"\\\"\\nfrom __future__ import annotations\\n\\nimport argparse\\nimport copy\\nimport json\\nimport os\\nimport random\\nimport re\\nimport sys\\nimport time\\nfrom collections import defaultdict\\nfrom datetime import datetime, timezone\\nfrom difflib import SequenceMatcher\\nfrom pathlib import Path\\nfrom typing import Any, Dict, List, Optional, Tuple\\n\\nimport numpy as np\\nimport torch\\nfrom scipy.stats import chi2\\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\\nfrom peft import PeftModel\\n\\nimport textworld\\nimport textworld.gym\\nfrom alfworld.agents.environment.alfred_tw_env import AlfredDemangler, AlfredInfos\\n\\nPROJECT_ROOT = Path(__file__).resolve().parent.parent\\nsys.path.insert(0, str(PROJECT_ROOT))\\n\\nfrom injection import (\\n    P1_StepOrderSwap,\\n    P2_SubGoalDeletion,\\n    C1_ContextTruncation,\\n    C4_ObservationMasking,\\n)\\n\\nMAX_STEPS = 50\\nHISTORY_WINDOW = 10\\n\\nOPERATORS = [\\n    P1_StepOrderSwap(),\\n    P2_SubGoalDeletion(),\\n    C1_ContextTruncation(),\\n    C4_ObservationMasking(),\\n]\\n\\nOPERATOR_CONFIGS = {\\n    \\\"P1_step_order_swap\\\": {\\\"swap_range\\\": 5},\\n    \\\"P2_sub_goal_deletion\\\": {\\\"deletion_strategy\\\": \\\"critical\\\"},\\n    \\\"C1_context_truncation\\\": {\\\"truncation_ratio\\\": 0.5},\\n    \\\"C4_observation_masking\\\": {\\\"mask_type\\\": \\\"generic\\\", \\\"max_masks\\\": 2},\\n}\\n\\n\\n# ---------------------------------------------------------------------------\\n# Prompt (identical to collect_trajectories.py)\\n# ---------------------------------------------------------------------------\\n\\ndef build_prompt(\\n    task_desc: str,\\n    step_count: int,\\n    history: List[Dict[str, str]],\\n    current_obs: str,\\n    admissible_commands: List[str],\\n) -> str:\\n    history_str =
…[truncated 7226 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_recovery-eval-dev_20260514T173802",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-14T17:45:48.183728+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "tail -n +224 /root/autodl-tmp/tax_error_inject_agent/eval/recovery.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_recovery-eval-dev_20260514T173802",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "tail -n +224 /root/autodl-tmp/tax_error_inject_agent/eval/recovery.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-14T17:45:48.184092+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"def run_episode(\\n    model: ModelInference,\\n    game_info: Dict[str, Any],\\n    inject: bool = False,\\n    operator=None,\\n    op_config: Optional[Dict[str, Any]] = None,\\n    injection_step: int = 3,\\n) -> Dict[str, Any]:\\n    request_infos = textworld.EnvInfos(\\n        won=True, admissible_commands=True, extras=[\\\"gamefile\\\"],\\n    )\\n    alfred_demangler = AlfredDemangler(shuffle=False)\\n    env_id = textworld.gym.register_games(\\n        [game_info[\\\"game_file\\\"]],\\n        request_infos,\\n        batch_size=1,\\n        max_episode_steps=MAX_STEPS,\\n        wrappers=[alfred_demangler, AlfredInfos],\\n    )\\n    env = textworld.gym.make(env_id)\\n\\n    try:\\n        obs, infos = env.reset()\\n        obs_text = obs[0] if isinstance(obs, (list, tuple)) else obs\\n\\n        history: List[Dict[str, str]] = []\\n        done = False\\n        won = False\\n        step_count = 0\\n        injected = False\\n\\n        while not done and step_count < MAX_STEPS:\\n            admissible = infos.get(\\\"admissible_commands\\\", [[]])[0]\\n            if not admissible:\\n                break\\n\\n            display_history = history\\n            if (inject and not injected and operator is not None\\n                    and step_count >= injection_step and len(history) >= 2):\\n                display_history = apply_injection(\\n                    history, operator, op_config or {},\\n                )\\n                injected = True\\n\\n            prompt = build_prompt(\\n                game_info[\\\"task_desc\\\"], step_count, display_history,\\n                obs_text, admissible,\\n            )\\n\\n            response_text = model.generate(prompt)\\n            _think, action = parse_response(response_text)\\n\\n            if not action:\\n                action = admissible[0] if admissible else \\\"look\\\"\\n            else:\\n                action = fuzzy_matc
…[truncated 7038 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_recovery-eval-dev_20260514T173802",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-14T17:45:48.184395+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/tax_error_inject_agent/injection/random_injector.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_recovery-eval-dev_20260514T173802",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/tax_error_inject_agent/injection/random_injector.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-14T17:45:48.184651+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nD004: RandomInjector reuses TaxEI operators (P1/P2/C1/C4) with uniform\\nrandom selection. The ONLY difference from TaxEI is at the training data\\nformatting stage: Random mode labels errors as [Error occurred] while\\nTaxEI labels with specific types like [Error Type: P1_StepOrderSwap].\\n\\nThis isolates the experimental variable to \\\"does taxonomy guidance in\\nthe error label add training signal value?\\\" rather than \\\"which perturbation\\nimplementation is better?\\\"\\n\\\"\\\"\\\"\\nfrom __future__ import annotations\\n\\nimport random\\nfrom typing import Any, Dict, List, Optional\\n\\nfrom .base import InjectionOperator\\nfrom .planning import P1_StepOrderSwap, P2_SubGoalDeletion\\nfrom .context import C1_ContextTruncation, C4_ObservationMasking\\n\\n\\nclass RandomInjector(InjectionOperator):\\n    \\\"\\\"\\\"Taxonomy-unaware baseline: reuses TaxEI operators without type labels.\\\"\\\"\\\"\\n    name = \\\"random_baseline\\\"\\n    category = \\\"random\\\"\\n\\n    def __init__(self):\\n        self._operators = [\\n            P1_StepOrderSwap(),\\n            P2_SubGoalDeletion(),\\n            C1_ContextTruncation(),\\n            C4_ObservationMasking(),\\n        ]\\n        self._last_operator: Optional[InjectionOperator] = None\\n\\n    def inject(\\n        self,\\n        trajectory: List[Dict[str, Any]],\\n        env_idx: int,\\n        step_idx: int,\\n        config: Dict[str, Any],\\n    ) -> List[Dict[str, Any]]:\\n        self._last_operator = random.choice(self._operators)\\n        op_config = config.get(self._last_operator.name, {})\\n        return self._last_operator.inject(trajectory, env_idx, step_idx, op_config)\\n\\n    def validate(\\n        self, original: List[Dict[str, Any]], modified: List[Dict[str, Any]]\\n    ) -> bool:\\n        if self._last_operator is None:\\n            return False\\n        return self._last_operator.validate(original, mo
…[truncated 289 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_recovery-eval-dev_20260514T173802",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-14T17:45:48.184880+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/tax_error_inject_agent/eval/eval_tasks_47.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_recovery-eval-dev_20260514T173802",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/tax_error_inject_agent/eval/eval_tasks_47.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-14T17:45:48.185260+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"description\\\": \\\"47 solvable tasks from ALFWorld valid_unseen (solvable=True filter, excludes pick_and_place_with_movable_recep)\\\",\\n  \\\"source\\\": \\\"vanilla-react-baseline eval run 2026-05-14\\\",\\n  \\\"total\\\": 47,\\n  \\\"tasks\\\": [\\n    {\\n      \\\"task_id\\\": \\\"look_at_obj_in_light-AlarmClock-None-DeskLamp-308\\\",\\n      \\\"task_type\\\": \\\"look_at_obj_in_light\\\",\\n      \\\"gamefile\\\": \\\"/root/autodl-tmp/alfworld_data/json_2.1.1/valid_unseen/look_at_obj_in_light-AlarmClock-None-DeskLamp-308/trial_T20190908_222917_366542/game.tw-pddl\\\",\\n      \\\"task_desc\\\": \\\"Hold the clock and turn on the lamp.\\\"\\n    },\\n    {\\n      \\\"task_id\\\": \\\"look_at_obj_in_light-Book-None-DeskLamp-308\\\",\\n      \\\"task_type\\\": \\\"look_at_obj_in_light\\\",\\n      \\\"gamefile\\\": \\\"/root/autodl-tmp/alfworld_data/json_2.1.1/valid_unseen/look_at_obj_in_light-Book-None-DeskLamp-308/trial_T20190908_020029_636862/game.tw-pddl\\\",\\n      \\\"task_desc\\\": \\\"Look at a book by the light of a lamp.\\\"\\n    },\\n    {\\n      \\\"task_id\\\": \\\"look_at_obj_in_light-Bowl-None-DeskLamp-308\\\",\\n      \\\"task_type\\\": \\\"look_at_obj_in_light\\\",\\n      \\\"gamefile\\\": \\\"/root/autodl-tmp/alfworld_data/json_2.1.1/valid_unseen/look_at_obj_in_light-Bowl-None-DeskLamp-308/trial_T20190907_133919_856963/game.tw-pddl\\\",\\n      \\\"task_desc\\\": \\\"turn on a lamp while holding a bowl\\\"\\n    },\\n    {\\n      \\\"task_id\\\": \\\"look_at_obj_in_light-CD-None-DeskLamp-308\\\",\\n      \\\"task_type\\\": \\\"look_at_obj_in_light\\\",\\n      \\\"gamefile\\\": \\\"/root/autodl-tmp/alfworld_data/json_2.1.1/valid_unseen/look_at_obj_in_light-CD-None-DeskLamp-308/trial_T20190908_141942_810052/game.tw-pddl\\\",\\n      \\\"task_desc\\\": \\\"examine a CD with a lamp\\\"\\n    },\\n    {\\n      \\\"task_id\\\": \\\"look_at_obj_in_light-Mug-None-DeskLamp-308
…[truncated 7583 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_recovery-eval-dev_20260514T173802",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-14T17:45:48.185504+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls -d /root/autodl-tmp/tax_error_inject_agent/checkpoints/mini_vanilla_sft_v4/v0-*/checkpoint-*",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_recovery-eval-dev_20260514T173802",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls -d /root/autodl-tmp/tax_error_inject_agent/checkpoints/mini_vanilla_sft_v4/v0-*/checkpoint-*",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-14T17:45:48.185677+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/tax_error_inject_agent/checkpoints/mini_vanilla_sft_v4/v0-20260514-201441/checkpoint-1090\\n/root/autodl-tmp/tax_error_inject_agent/checkpoints/mini_vanilla_sft_v4/v0-20260514-201441/checkpoint-1635\\n/root/autodl-tmp/tax_error_inject_agent/checkpoints/mini_vanilla_sft_v4/v0-20260514-201441/checkpoint-545\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_recovery-eval-dev_20260514T173802",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-14T17:45:48.185872+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:TodoWrite",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_recovery-eval-dev_20260514T173802",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:TodoWrite",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-14T17:45:48.185996+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_recovery-eval-dev_20260514T173802",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-14T17:45:48.186115+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Read existing code and understand project structure', 'status': 'completed', 'activeForm': 'Reading existing code'}, {'content': 'Write eval/injected_eval.py — injected recovery evaluation script', 'status': 'in_progress', 'activeForm': 'Writing injected eval script'}, {'content': 'Write scripts/run_injected_eval.sh — launcher script for all 3 variants', 'status': 'pending', 'activeForm': 'Writing launcher script'}, {'content': 'Deploy to server and dry-run on 1 task with vanilla checkpoint on cuda:3', 'status': 'pending', 'activeForm': 'Deploying and dry-running'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_recovery-eval-dev_20260514T173802",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Read existing code and understand project structure', 'status': 'completed', 'activeForm': 'Reading existing code'}, {'content': 'Write eval/injected_eval.py — injected recovery evaluation script', 'status': 'in_progress', 'activeForm': 'Writing injected eval script'}, {'content': 'Write scripts/run_injected_eval.sh — launcher script for all 3 variants', 'status': 'pending', 'activeForm': 'Writing launcher script'}, {'content': 'Deploy to server and dry-run on 1 task with vanilla checkpoint on cuda:3', 'status': 'pending', 'activeForm': 'Deploying and dry-running'}]"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-14T17:45:48.186259+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_recovery-eval-dev_20260514T173802",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-14T17:45:48.186603+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat > /root/autodl-tmp/tax_error_inject_agent/eval/injected_eval.py << 'PYEOF'\n#!/usr/bin/env python3\n\"\"\"\nInjected Recovery Evaluation — wrong-action injection + error tag.\n\nAt a chosen step, replaces the model's action with a random wrong action\nfrom admissible commands, executes it in the environment, and inserts an\nerror tag matching the model variant's training format.\n\nMeasures recovery_success_rate: fraction of tasks completed despite injection.\n\nUsage:\n    python eval/injected_eval.py \\\n        --model_path checkpoints/.../checkpoint-NNN \\\n        --model_variant taxei --device cuda:3 --num_episodes 5\n\nInput:\n    --model_path:     LoRA adapter checkpoint (omit for zero-shot base model)\n    --model_variant:  {taxei, random, vanilla} — controls error tag format\n    --task_list:      JSON task list (default: eval/eval_tasks_47.json)\n    --inject_step:    fixed injection step, or -1 for random [2,4] (default: -1)\n    --inject_operators: operator labels to cycle through (short: P1 P2 C1 C4)\n\nOutput (JSON):\n    Per-task: task_name, injected_error_type, inject_step, recovered,\n              total_steps, original_action, injected_action, error_tag\n    Aggregate: recovery_rate, by_operator, by_task_type\n\nDependencies: transformers, peft, textworld, alfworld, scipy, numpy\n\"\"\"\nfrom __future__ import annotations\n\nimport argparse\nimport json\nimport os\nimport random\nimport sys\nimport time\nfrom collections import defaultdict\nfrom datetime import datetime, timezone\nfrom pathlib import Path\nfrom typing import Any, Dict, List, Optional, Tuple\n\nimport numpy as np\n\nEVAL_DIR = Path(__file__).resolve().parent\nPROJECT_ROOT = EVAL_DIR.parent\nsys.path.insert(0, str(PROJECT_ROOT))\nsys.path.insert(0, str(EVAL_DIR))\n\nimport textworld\nimport textworld.gym\nfrom alfworld.agents.environment.alfred_tw_env import AlfredDemangler, AlfredInfos\n\nfrom recovery import (\n    ModelInference,\n    build_prompt,\n    parse_response,\n    fuzzy_match_action,\n    collect_game_files,\n    load_task_list,\n    mcnemar_test,\n    bootstrap_ci,\n    MAX_STEPS,\n)\n\n# ---------------------------------------------------------------------------\n# Operator label mapping (matches data/formatter.py OPERATOR_LABELS)\n# ---------------------------------------------------------------------------\n\nALL_OPERATOR_LABELS = [\n    \"P1_StepOrderSwap\",\n    \"P2_SubGoalDeletion\",\n    \"C1_ContextTruncation\",\n    \"C4_ObservationMasking\",\n]\n\nSHORT_TO_FULL = {\n    \"P1\": \"P1_StepOrderSwap\",\n    \"P2\": \"P2_SubGoalDeletion\",\n    \"C1\": \"C1_ContextTruncation\",\n    \"C4\": \"C4_ObservationMasking\",\n}\n\n\ndef resolve_operator_labels(names: List[str]) -> List[str]:\n    \"\"\"Accept short names (P1) or full names (P1_StepOrderSwap).\"\"\"\n    resolved = []\n    for n in names:\n        if n in SHORT_TO_FULL:\n            resolved.append(SHORT_TO_FULL[n])\n        elif n in ALL_OPERATOR_LABELS:\n            resolved.append(n)\n        else:\n            raise ValueError(f\"Unknown operator: {n}. Use {list(SHORT_TO_FULL.keys())} or full names.\")\n    return resolved\n\n\ndef make_error_tag(model_variant: str, operator_label: str) -> str:\n    \"\"\"Generate error tag matching the model variant's training format.\"\"\"\n    if model_variant == \"taxei\":\n        return f\"[Error Type: {operator_label}]\"\n    elif model_variant == \"random\":\n        return \"[Error occurred]\"\n    return \"\"\n\n\ndef pick_wrong_action(\n    model_action: str, admissible: List[str], rng: random.Random,\n) -> Optional[str]:\n    \"\"\"Pick a random admissible action that differs from the model's choice.\"\"\"\n    alternatives = [a for a in admissible if a != model_action]\n    return rng.choice(alternatives) if alternatives else None\n\n\n# ---------------------------------------------------------------------------\n# Episode runner with injection\n# ---------------------------------------------------------------------------\n\ndef run_injected_episode(\n    model: ModelInference,\n    game_info: Dict[str, Any],\n    model_variant: str,\n    operator_label: str,\n    injection_step: int,\n    rng: random.Random,\n) -> Dict[str, Any]:\n    \"\"\"Run one ALFWorld episode; inject a wrong action at injection_step.\"\"\"\n    request_infos = textworld.EnvInfos(\n        won=True, admissible_commands=True, extras=[\"gamefile\"],\n    )\n    env_id = textworld.gym.register_games(\n        [game_info[\"game_file\"]],\n        request_infos,\n        batch_size=1,\n        max_episode_steps=MAX_STEPS,\n        wrappers=[AlfredDemangler(shuffle=False), AlfredInfos],\n    )\n    env = textworld.gym.make(env_id)\n\n    try:\n        obs, infos = env.reset()\n        obs_text = obs[0] if isinstance(obs, (list, tuple)) else obs\n\n        history: List[Dict[str, str]] = []\n        done = False\n        won = False\n        step_count = 0\n        injected = False\n        tag_applied = False\n        inject_detail: Dict[str, Any] = {}\n\n        while not done and step_count < MAX_STEPS:\n            admissible = infos.get(\"admissible_commands\", [[]])[0]\n            if not admissible:\n                break\n\n            prompt = build_prompt(\n                game_info[\"task_desc\"], step_count, history,\n                obs_text, admissible,\n            )\n            response_text = model.generate(prompt)\n            _think, action = parse_response(response_text)\n\n            if not action:\n                action = admissible[0] if admissible else \"look\"\n            else:\n                action = fuzzy_match_action(action, admissible)\n\n            # --- Injection: replace model action with wrong action ---\n            if (not injected\n                    and step_count == injection_step\n                    and len(admissible) > 1):\n                wrong = pick_wrong_action(action, admissible, rng)\n                if wrong is not None:\n                    inject_detail = {\n                        \"original_action\": action,\n                        \"injected_action\": wrong,\n                        \"inject_step\": step_count,\n                        \"operator_label\": operator_label,\n                        \"error_tag\": make_error_tag(model_variant, operator_label),\n                    }\n                    action = wrong\n                    injected = True\n\n            history.append({\"observation\": obs_text, \"action\": action})\n            obs, _rewards, dones, infos = env.step([action])\n            obs_text = obs[0] if isinstance(obs, (list, tuple)) else obs\n\n            # Prepend error tag to the observation that follows the wrong action,\n            # so the model sees it in the next step's prompt.\n            if injected and not tag_applied:\n                tag = make_error_tag(model_variant, operator_label)\n                if tag:\n                    obs_text = f\"{tag}\\n{obs_text}\"\n                tag_applied = True\n\n            done = dones[0] if isinstance(dones, (list, tuple)) else dones\n            won = infos.get(\"won\", [False])[0]\n            step_count += 1\n    finally:\n        env.close()\n\n    return {\n        \"task_name\": game_info.get(\"task_name\", \"\"),\n        \"task_type\": game_info[\"task_type\"],\n        \"task_desc\": game_info[\"task_desc\"],\n        \"recovered\": bool(won),\n        \"total_steps\": step_count,\n        \"injected\": injected,\n        \"model_variant\": model_variant,\n        \"injected_error_type\": inject_detail.get(\"operator_label\", \"\"),\n        \"inject_step\": inject_detail.get(\"inject_step\", -1),\n        \"original_action\": inject_detail.get(\"original_action\", \"\"),\n        \"injected_action\": inject_detail.get(\"injected_action\", \"\"),\n        \"error_tag\": inject_detail.get(\"error_tag\", \"\"),\n    }\n\n\n# ---------------------------------------------------------------------------\n# Report builder\n# ---------------------------------------------------------------------------\n\ndef build_injected_report(\n    results: List[Dict[str, Any]], args,\n) -> Dict[str, Any]:\n    total = len(results)\n    injected_results = [r for r in results if r[\"injected\"]]\n    recovered = sum(1 for r in injected_results if r[\"recovered\"])\n\n    report: Dict[str, Any] = {\n        \"model\": args.model_path or args.base_model,\n        \"model_variant\": args.model_variant,\n        \"eval_type\": \"injected_recovery\",\n        \"total_episodes\": total,\n        \"injected_episodes\": len(injected_results),\n        \"recovery_rate\": round(recovered / len(injected_results), 3) if injected_results else 0,\n        \"timestamp\": datetime.now(timezone.utc).isoformat(),\n        \"config\": {\n            \"inject_step\": args.inject_step,\n            \"operators\": args.inject_operators,\n            \"seed\": args.seed,\n        },\n    }\n\n    # Per-operator recovery rates\n    op_stats: Dict[str, Dict[str, int]] = defaultdict(\n        lambda: {\"total\": 0, \"recovered\": 0},\n    )\n    for r in injected_results:\n        op = r[\"injected_error_type\"]\n        op_stats[op][\"total\"] += 1\n        if r[\"recovered\"]:\n            op_stats[op][\"recovered\"] += 1\n\n    report[\"by_operator\"] = {\n        op: {\n            \"total\": c[\"total\"],\n            \"recovered\": c[\"recovered\"],\n            \"rate\": round(c[\"recovered\"] / c[\"total\"], 3) if c[\"total\"] else 0,\n        }\n        for op, c in sorted(op_stats.items())\n    }\n\n    # Per-task-type recovery rates\n    type_stats: Dict[str, Dict[str, int]] = defaultdict(\n        lambda: {\"total\": 0, \"recovered\": 0},\n    )\n    for r in injected_results:\n        tt = r[\"task_type\"]\n        type_stats[tt][\"total\"] += 1\n        if r[\"recovered\"]:\n            type_stats[tt][\"recovered\"] += 1\n\n    report[\"by_task_type\"] = {\n        tt: {\n            \"total\": c[\"total\"],\n            \"recovered\": c[\"recovered\"],\n            \"rate\": round(c[\"recovered\"] / c[\"total\"], 3) if c[\"total\"] else 0,\n        }\n        for tt, c in sorted(type_stats.items())\n    }\n\n    report[\"episodes\"] = results\n    return report\n\n\n# ---------------------------------------------------------------------------\n# Comparison helper\n# ---------------------------------------------------------------------------\n\ndef compare_variants(path_a: str, path_b: str, output_path: Optional[str] = None):\n    \"\"\"Compare recovery rates between two variant result files.\"\"\"\n    with open(path_a) as f:\n        a = json.load(f)\n    with open(path_b) as f:\n        b = json.load(f)\n\n    a_by_task = {e[\"task_name\"]: e[\"recovered\"] for e in a[\"episodes\"] if e[\"injected\"]}\n    b_by_task = {e[\"task_name\"]: e[\"recovered\"] for e in b[\"episodes\"] if e[\"injected\"]}\n    common = sorted(set(a_by_task) & set(b_by_task))\n\n    if not common:\n        print(\"No common injected tasks found.\", file=sys.stderr)\n        return\n\n    a_succ = [a_by_task[t] for t in common]\n    b_succ = [b_by_task[t] for t in common]\n\n    a_rate = float(np.mean(a_succ))\n    b_rate = float(np.mean(b_succ))\n    p = mcnemar_test(a_succ, b_succ)\n    ci_lo, ci_hi = bootstrap_ci([int(s) for s in a_succ], [int(s) for s in b_succ])\n\n    comparison = {\n        \"variant_a\": a.get(\"model_variant\", \"?\"),\n        \"variant_b\": b.get(\"model_variant\", \"?\"),\n        \"model_a\": a.get(\"model\", \"\"),\n        \"model_b\": b.get(\"model\", \"\"),\n        \"num_common_tasks\": len(common),\n        \"recovery_rate_a\": round(a_rate, 3),\n        \"recovery_rate_b\": round(b_rate, 3),\n        \"diff_a_minus_b\": round(a_rate - b_rate, 3),\n        \"mcnemar_p\": round(p, 4),\n        \"bootstrap_ci_95\": [round(ci_lo, 3), round(ci_hi, 3)],\n        \"significant_at_005\": p < 0.05,\n    }\n\n    print(json.dumps(comparison, indent=2), flush=True)\n\n    if output_path:\n        os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)\n        with open(output_path, \"w\") as f:\n            json.dump(comparison, f, indent=2)\n        print(f\"Comparison saved to {output_path}\", flush=True)\n\n\n# ---------------------------------------------------------------------------\n# Main\n# ---------------------------------------------------------------------------\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Injected Recovery Evaluation — wrong-action injection + error tag\",\n    )\n    parser.add_argument(\"--model_path\", type=str, default=None,\n                        help=\"LoRA adapter checkpoint path (omit for zero-shot)\")\n    parser.add_argument(\"--base_model\", type=str,\n                        default=\"/root/autodl-tmp/models/Qwen/Qwen3-8B\")\n    parser.add_argument(\"--model_variant\", type=str, default=\"vanilla\",\n                        choices=[\"taxei\", \"random\", \"vanilla\"],\n                        help=\"Error tag format: taxei=[Error Type: X], random=[Error occurred], vanilla=none\")\n    parser.add_argument(\"--alfworld_data\", type=str,\n                        default=\"/root/autodl-tmp/alfworld_data\")\n    parser.add_argument(\"--eval_split\", type=str, default=\"valid_unseen\")\n    parser.add_argument(\"--num_episodes\", type=int, default=47)\n    parser.add_argument(\"--output\", type=str, default=None,\n                        help=\"Output JSON path (default: eval_results/injected_{variant}.json)\")\n    parser.add_argument(\"--device\", type=str, default=\"cuda:0\")\n    parser.add_argument(\"--seed\", type=int, default=42)\n    parser.add_argument(\"--task_list\", type=str,\n                        default=str(PROJECT_ROOT / \"eval\" / \"eval_tasks_47.json\"),\n                        help=\"JSON task list for reproducible evaluation\")\n    parser.add_argument(\"--inject_step\", type=int, default=-1,\n                        help=\"Fixed injection step, or -1 for random in [2,4]\")\n    parser.add_argument(\"--inject_operators\", type=str, nargs=\"+\",\n                        default=[\"P1\", \"P2\", \"C1\", \"C4\"],\n                        help=\"Operator labels to cycle through (P1 P2 C1 C4 or full names)\")\n\n    parser.add_argument(\"--compare_with\", type=str, default=None,\n                        help=\"Compare --output with another variant's results JSON\")\n    parser.add_argument(\"--compare_output\", type=str, default=None,\n                        help=\"Save comparison JSON to this path\")\n\n    args = parser.parse_args()\n\n    # Resolve operator short names\n    args.inject_operators = resolve_operator_labels(args.inject_operators)\n\n    if args.output is None:\n        args.output = f\"eval_results/injected_{args.model_variant}.json\"\n\n    # --- Comparison mode ---\n    if args.compare_with:\n        if not os.path.exists(args.output):\n            print(f\"Error: {args.output} not found for comparison\", file=sys.stderr)\n            sys.exit(1)\n        compare_variants(args.output, args.compare_with, args.compare_output)\n        return\n\n    # --- Load tasks ---\n    if args.task_list and os.path.exists(args.task_list):\n        games = load_task_list(args.task_list)\n        print(f\"Loaded {len(games)} tasks from {args.task_list}\", flush=True)\n    else:\n        data_path = os.path.join(args.alfworld_data, \"json_2.1.1\", args.eval_split)\n        games = collect_game_files(data_path)\n        print(f\"Found {len(games)} tasks in {args.eval_split}\", flush=True)\n\n    if 0 < args.num_episodes < len(games):\n        games = games[:args.num_episodes]\n\n    # --- Load model ---\n    print(f\"Model variant: {args.model_variant}\", flush=True)\n    model = ModelInference(\n        base_model=args.base_model,\n        adapter_path=args.model_path,\n        device=args.device,\n    )\n\n    # --- Run episodes ---\n    results: List[Dict[str, Any]] = []\n    rng = random.Random(args.seed)\n    operators = args.inject_operators\n    t0 = time.time()\n\n    for i, game_info in enumerate(games):\n        op_label = operators[i % len(operators)]\n        inj_step = args.inject_step if args.inject_step >= 0 else rng.randint(2, 4)\n\n        result = run_injected_episode(\n            model, game_info,\n            model_variant=args.model_variant,\n            operator_label=op_label,\n            injection_step=inj_step,\n            rng=rng,\n        )\n        results.append(result)\n\n        status = \"RECOVERED\" if result[\"recovered\"] else \"FAIL\"\n        inj = f\" [{op_label}@step{inj_step}]\" if result[\"injected\"] else \" [no-inject]\"\n        elapsed = time.time() - t0\n        eta = elapsed / (i + 1) * (len(games) - i - 1)\n        print(\n            f\"  [{i + 1}/{len(games)}] {game_info['task_name']}: {status} \"\n            f\"({result['total_steps']} steps){inj}  \"\n            f\"[{elapsed:.0f}s elapsed, ~{eta:.0f}s remaining]\",\n            flush=True,\n        )\n\n    # --- Build and save report ---\n    report = build_injected_report(results, args)\n\n    os.makedirs(os.path.dirname(os.path.abspath(args.output)), exist_ok=True)\n    with open(args.output, \"w\") as f:\n        json.dump(report, f, indent=2, ensure_ascii=False)\n    print(f\"\\nReport saved to {args.output}\", flush=True)\n\n    # --- Summary ---\n    print(f\"\\n=== Injected Recovery Summary ({args.model_variant}) ===\", flush=True)\n    print(f\"Total: {report['total_episodes']}, Injected: {report['injected_episodes']}\", flush=True)\n    print(f\"Recovery rate: {report['recovery_rate']}\", flush=True)\n    if report[\"by_operator\"]:\n        print(\"By operator:\", flush=True)\n        for op, s in report[\"by_operator\"].items():\n            print(f\"  {op}: {s['recovered']}/{s['total']} ({s['rate']})\", flush=True)\n    if report[\"by_task_type\"]:\n        print(\"By task type:\", flush=True)\n        for tt, s in report[\"by_task_type\"].items():\n            print(f\"  {tt}: {s['recovered']}/{s['total']} ({s['rate']})\", flush=True)\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF\necho \"EXIT_CODE=$?\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_recovery-eval-dev_20260514T173802",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat > /root/autodl-tmp/tax_error_inject_agent/eval/injected_eval.py << 'PYEOF'\n#!/usr/bin/env python3\n\"\"\"\nInjected Recovery Evaluation — wrong-action injection + error tag.\n\nAt a chosen step, replaces the model's action with a random wrong action\nfrom admissible commands, executes it in the environment, and inserts an\nerror tag matching the model variant's training format.\n\nMeasures recovery_success_rate: fraction of tasks completed despite injection.\n\nUsage:\n    python eval/injected_eval.py \\\n        --model_path checkpoints/.../checkpoint-NNN \\\n        --model_variant taxei --device cuda:3 --num_episodes 5\n\nInput:\n    --model_path:     LoRA adapter checkpoint (omit for zero-shot base model)\n    --model_variant:  {taxei, random, vanilla} — controls error tag format\n    --task_list:      JSON task list (default: eval/eval_tasks_47.json)\n    --inject_step:    fixed injection step, or -1 for random [2,4] (default: -1)\n    --inject_operators: operator labels to cycle through (short: P1 P2 C1 C4)\n\nOutput (JSON):\n    Per-task: task_name, injected_error_type, inject_step, recovered,\n              total_steps, original_action, injected_action, error_tag\n    Aggregate: recovery_rate, by_operator, by_task_type\n\nDependencies: transformers, peft, textworld, alfworld, scipy, numpy\n\"\"\"\nfrom __future__ import annotations\n\nimport argparse\nimport json\nimport os\nimport random\nimport sys\nimport time\nfrom collections import defaultdict\nfrom datetime import datetime, timezone\nfrom pathlib import Path\nfrom typing import Any, Dict, List, Optional, Tuple\n\nimport numpy as np\n\nEVAL_DIR = Path(__file__).resolve().parent\nPROJECT_ROOT = EVAL_DIR.parent\nsys.path.insert(0, str(PROJECT_ROOT))\nsys.path.insert(0, str(EVAL_DIR))\n\nimport textworld\nimport textworld.gym\nfrom alfworld.agents.environment.alfred_tw_env import AlfredDemangler, AlfredInfos\n\nfrom recovery import (\n    ModelInference,\n    build_prompt,\n    parse_response,\n    fuzzy_match_action,\n    collect_game_files,\n    load_task_list,\n    mcnemar_test,\n    bootstrap_ci,\n    MAX_STEPS,\n)\n\n# ---------------------------------------------------------------------------\n# Operator label mapping (matches data/formatter.py OPERATOR_LABELS)\n# ---------------------------------------------------------------------------\n\nALL_OPERATOR_LABELS = [\n    \"P1_StepOrderSwap\",\n    \"P2_SubGoalDeletion\",\n    \"C1_ContextTruncation\",\n    \"C4_ObservationMasking\",\n]\n\nSHORT_TO_FULL = {\n    \"P1\": \"P1_StepOrderSwap\",\n    \"P2\": \"P2_SubGoalDeletion\",\n    \"C1\": \"C1_ContextTruncation\",\n    \"C4\": \"C4_ObservationMasking\",\n}\n\n\ndef resolve_operator_labels(names: List[str]) -> List[str]:\n    \"\"\"Accept short names (P1) or full names (P1_StepOrderSwap).\"\"\"\n    resolved = []\n    for n in names:\n        if n in SHORT_TO_FULL:\n            resolved.append(SHORT_TO_FULL[n])\n        elif n in ALL_OPERATOR_LABELS:\n            resolved.append(n)\n        else:\n            raise ValueError(f\"Unknown operator: {n}. Use {list(SHORT_TO_FULL.keys())} or full names.\")\n    return resolved\n\n\ndef make_error_tag(model_variant: str, operator_label: str) -> str:\n    \"\"\"Generate error tag matching the model variant's training format.\"\"\"\n    if model_variant == \"taxei\":\n        return f\"[Error Type: {operator_label}]\"\n    elif model_variant == \"random\":\n        return \"[Error occurred]\"\n    return \"\"\n\n\ndef pick_wrong_action(\n    model_action: str, admissible: List[str], rng: random.Random,\n) -> Optional[str]:\n    \"\"\"Pick a random admissible action that differs from the model's choice.\"\"\"\n    alternatives = [a for a in admissible if a != model_action]\n    return rng.choice(alternatives) if alternatives else None\n\n\n# ---------------------------------------------------------------------------\n# Episode runner with injection\n# ---------------------------------------------------------------------------\n\ndef run_injected_episode(\n    model: ModelInference,\n    game_info: Dict[str, Any],\n    model_variant: str,\n    operator_label: str,\n    injection_step: int,\n    rng: random.Random,\n) -> Dict[str, Any]:\n    \"\"\"Run one ALFWorld episode; inject a wrong action at injection_step.\"\"\"\n    request_infos = textworld.EnvInfos(\n        won=True, admissible_commands=True, extras=[\"gamefile\"],\n    )\n    env_id = textworld.gym.register_games(\n        [game_info[\"game_file\"]],\n        request_infos,\n        batch_size=1,\n        max_episode_steps=MAX_STEPS,\n        wrappers=[AlfredDemangler(shuffle=False), AlfredInfos],\n    )\n    env = textworld.gym.make(env_id)\n\n    try:\n        obs, infos = env.reset()\n        obs_text = obs[0] if isinstance(obs, (list, tuple)) else obs\n\n        history: List[Dict[str, str]] = []\n        done = False\n        won = False\n        step_count = 0\n        injected = False\n        tag_applied = False\n        inject_detail: Dict[str, Any] = {}\n\n        while not done and step_count < MAX_STEPS:\n            admissible = infos.get(\"admissible_commands\", [[]])[0]\n            if not admissible:\n                break\n\n            prompt = build_prompt(\n                game_info[\"task_desc\"], step_count, history,\n                obs_text, admissible,\n            )\n            response_text = model.generate(prompt)\n            _think, action = parse_response(response_text)\n\n            if not action:\n                action = admissible[0] if admissible else \"look\"\n            else:\n                action = fuzzy_match_action(action, admissible)\n\n            # --- Injection: replace model action with wrong action ---\n            if (not injected\n                    and step_count == injection_step\n                    and len(admissible) > 1):\n                wrong = pick_wrong_action(action, admissible, rng)\n                if wrong is not None:\n                    inject_detail = {\n                        \"original_action\": action,\n                        \"injected_action\": wrong,\n                        \"inject_step\": step_count,\n                        \"operator_label\": operator_label,\n                        \"error_tag\": make_error_tag(model_variant, operator_label),\n                    }\n                    action = wrong\n                    injected = True\n\n            history.append({\"observation\": obs_text, \"action\": action})\n            obs, _rewards, dones, infos = env.step([action])\n            obs_text = obs[0] if isinstance(obs, (list, tuple)) else obs\n\n            # Prepend error tag to the observation that follows the wrong action,\n            # so the model sees it in the next step's prompt.\n            if injected and not tag_applied:\n                tag = make_error_tag(model_variant, operator_label)\n                if tag:\n                    obs_text = f\"{tag}\\n{obs_text}\"\n                tag_applied = True\n\n            done = dones[0] if isinstance(dones, (list, tuple)) else dones\n            won = infos.get(\"won\", [False])[0]\n            step_count += 1\n    finally:\n        env.close()\n\n    return {\n        \"task_name\": game_info.get(\"task_name\", \"\"),\n        \"task_type\": game_info[\"task_type\"],\n        \"task_desc\": game_info[\"task_desc\"],\n        \"recovered\": bool(won),\n        \"total_steps\": step_count,\n        \"injected\": injected,\n        \"model_variant\": model_variant,\n        \"injected_error_type\": inject_detail.get(\"operator_label\", \"\"),\n        \"inject_step\": inject_detail.get(\"inject_step\", -1),\n        \"original_action\": inject_detail.get(\"original_action\", \"\"),\n        \"injected_action\": inject_detail.get(\"injected_action\", \"\"),\n        \"error_tag\": inject_detail.get(\"error_tag\", \"\"),\n    }\n\n\n# ---------------------------------------------------------------------------\n# Report builder\n# ---------------------------------------------------------------------------\n\ndef build_injected_report(\n    results: List[Dict[str, Any]], args,\n) -> Dict[str, Any]:\n    total = len(results)\n    injected_results = [r for r in results if r[\"injected\"]]\n    recovered = sum(1 for r in injected_results if r[\"recovered\"])\n\n    report: Dict[str, Any] = {\n        \"model\": args.model_path or args.base_model,\n        \"model_variant\": args.model_variant,\n        \"eval_type\": \"injected_recovery\",\n        \"total_episodes\": total,\n        \"injected_episodes\": len(injected_results),\n        \"recovery_rate\": round(recovered / len(injected_results), 3) if injected_results else 0,\n        \"timestamp\": datetime.now(timezone.utc).isoformat(),\n        \"config\": {\n            \"inject_step\": args.inject_step,\n            \"operators\": args.inject_operators,\n            \"seed\": args.seed,\n        },\n    }\n\n    # Per-operator recovery rates\n    op_stats: Dict[str, Dict[str, int]] = defaultdict(\n        lambda: {\"total\": 0, \"recovered\": 0},\n    )\n    for r in injected_results:\n        op = r[\"injected_error_type\"]\n        op_stats[op][\"total\"] += 1\n        if r[\"recovered\"]:\n            op_stats[op][\"recovered\"] += 1\n\n    report[\"by_operator\"] = {\n        op: {\n            \"total\": c[\"total\"],\n            \"recovered\": c[\"recovered\"],\n            \"rate\": round(c[\"recovered\"] / c[\"total\"], 3) if c[\"total\"] else 0,\n        }\n        for op, c in sorted(op_stats.items())\n    }\n\n    # Per-task-type recovery rates\n    type_stats: Dict[str, Dict[str, int]] = defaultdict(\n        lambda: {\"total\": 0, \"recovered\": 0},\n    )\n    for r in injected_results:\n        tt = r[\"task_type\"]\n        type_stats[tt][\"total\"] += 1\n        if r[\"recovered\"]:\n            type_stats[tt][\"recovered\"] += 1\n\n    report[\"by_task_type\"] = {\n        tt: {\n            \"total\": c[\"total\"],\n            \"recovered\": c[\"recovered\"],\n            \"rate\": round(c[\"recovered\"] / c[\"total\"], 3) if c[\"total\"] else 0,\n        }\n        for tt, c in sorted(type_stats.items())\n    }\n\n    report[\"episodes\"] = results\n    return report\n\n\n# ---------------------------------------------------------------------------\n# Comparison helper\n# ---------------------------------------------------------------------------\n\ndef compare_variants(path_a: str, path_b: str, output_path: Optional[str] = None):\n    \"\"\"Compare recovery rates between two variant result files.\"\"\"\n    with open(path_a) as f:\n        a = json.load(f)\n    with open(path_b) as f:\n        b = json.load(f)\n\n    a_by_task = {e[\"task_name\"]: e[\"recovered\"] for e in a[\"episodes\"] if e[\"injected\"]}\n    b_by_task = {e[\"task_name\"]: e[\"recovered\"] for e in b[\"episodes\"] if e[\"injected\"]}\n    common = sorted(set(a_by_task) & set(b_by_task))\n\n    if not common:\n        print(\"No common injected tasks found.\", file=sys.stderr)\n        return\n\n    a_succ = [a_by_task[t] for t in common]\n    b_succ = [b_by_task[t] for t in common]\n\n    a_rate = float(np.mean(a_succ))\n    b_rate = float(np.mean(b_succ))\n    p = mcnemar_test(a_succ, b_succ)\n    ci_lo, ci_hi = bootstrap_ci([int(s) for s in a_succ], [int(s) for s in b_succ])\n\n    comparison = {\n        \"variant_a\": a.get(\"model_variant\", \"?\"),\n        \"variant_b\": b.get(\"model_variant\", \"?\"),\n        \"model_a\": a.get(\"model\", \"\"),\n        \"model_b\": b.get(\"model\", \"\"),\n        \"num_common_tasks\": len(common),\n        \"recovery_rate_a\": round(a_rate, 3),\n        \"recovery_rate_b\": round(b_rate, 3),\n        \"diff_a_minus_b\": round(a_rate - b_rate, 3),\n        \"mcnemar_p\": round(p, 4),\n        \"bootstrap_ci_95\": [round(ci_lo, 3), round(ci_hi, 3)],\n        \"significant_at_005\": p < 0.05,\n    }\n\n    print(json.dumps(comparison, indent=2), flush=True)\n\n    if output_path:\n        os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)\n        with open(output_path, \"w\") as f:\n            json.dump(comparison, f, indent=2)\n        print(f\"Comparison saved to {output_path}\", flush=True)\n\n\n# ---------------------------------------------------------------------------\n# Main\n# ---------------------------------------------------------------------------\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Injected Recovery Evaluation — wrong-action injection + error tag\",\n    )\n    parser.add_argument(\"--model_path\", type=str, default=None,\n                        help=\"LoRA adapter checkpoint path (omit for zero-shot)\")\n    parser.add_argument(\"--base_model\", type=str,\n                        default=\"/root/autodl-tmp/models/Qwen/Qwen3-8B\")\n    parser.add_argument(\"--model_variant\", type=str, default=\"vanilla\",\n                        choices=[\"taxei\", \"random\", \"vanilla\"],\n                        help=\"Error tag format: taxei=[Error Type: X], random=[Error occurred], vanilla=none\")\n    parser.add_argument(\"--alfworld_data\", type=str,\n                        default=\"/root/autodl-tmp/alfworld_data\")\n    parser.add_argument(\"--eval_split\", type=str, default=\"valid_unseen\")\n    parser.add_argument(\"--num_episodes\", type=int, default=47)\n    parser.add_argument(\"--output\", type=str, default=None,\n                        help=\"Output JSON path (default: eval_results/injected_{variant}.json)\")\n    parser.add_argument(\"--device\", type=str, default=\"cuda:0\")\n    parser.add_argument(\"--seed\", type=int, default=42)\n    parser.add_argument(\"--task_list\", type=str,\n                        default=str(PROJECT_ROOT / \"eval\" / \"eval_tasks_47.json\"),\n                        help=\"JSON task list for reproducible evaluation\")\n    parser.add_argument(\"--inject_step\", type=int, default=-1,\n                        help=\"Fixed injection step, or -1 for random in [2,4]\")\n    parser.add_argument(\"--inject_operators\", type=str, nargs=\"+\",\n                        default=[\"P1\", \"P2\", \"C1\", \"C4\"],\n                        help=\"Operator labels to cycle through (P1 P2 C1 C4 or full names)\")\n\n    parser.add_argument(\"--compare_with\", type=str, default=None,\n                        help=\"Compare --output with another variant's results JSON\")\n    parser.add_argument(\"--compare_output\", type=str, default=None,\n                        help=\"Save comparison JSON to this path\")\n\n    args = parser.parse_args()\n\n    # Resolve operator short names\n    args.inject_operators = resolve_operator_labels(args.inject_operators)\n\n    if args.output is None:\n        args.output = f\"eval_results/injected_{args.model_variant}.json\"\n\n    # --- Comparison mode ---\n    if args.compare_with:\n        if not os.path.exists(args.output):\n            print(f\"Error: {args.output} not found for comparison\", file=sys.stderr)\n            sys.exit(1)\n        compare_variants(args.output, args.compare_with, args.compare_output)\n        return\n\n    # --- Load tasks ---\n    if args.task_list and os.path.exists(args.task_list):\n        games = load_task_list(args.task_list)\n        print(f\"Loaded {len(games)} tasks from {args.task_list}\", flush=True)\n    else:\n        data_path = os.path.join(args.alfworld_data, \"json_2.1.1\", args.eval_split)\n        games = collect_game_files(data_path)\n        print(f\"Found {len(games)} tasks in {args.eval_split}\", flush=True)\n\n    if 0 < args.num_episodes < len(games):\n        games = games[:args.num_episodes]\n\n    # --- Load model ---\n    print(f\"Model variant: {args.model_variant}\", flush=True)\n    model = ModelInference(\n        base_model=args.base_model,\n        adapter_path=args.model_path,\n        device=args.device,\n    )\n\n    # --- Run episodes ---\n    results: List[Dict[str, Any]] = []\n    rng = random.Random(args.seed)\n    operators = args.inject_operators\n    t0 = time.time()\n\n    for i, game_info in enumerate(games):\n        op_label = operators[i % len(operators)]\n        inj_step = args.inject_step if args.inject_step >= 0 else rng.randint(2, 4)\n\n        result = run_injected_episode(\n            model, game_info,\n            model_variant=args.model_variant,\n            operator_label=op_label,\n            injection_step=inj_step,\n            rng=rng,\n        )\n        results.append(result)\n\n        status = \"RECOVERED\" if result[\"recovered\"] else \"FAIL\"\n        inj = f\" [{op_label}@step{inj_step}]\" if result[\"injected\"] else \" [no-inject]\"\n        elapsed = time.time() - t0\n        eta = elapsed / (i + 1) * (len(games) - i - 1)\n        print(\n            f\"  [{i + 1}/{len(games)}] {game_info['task_name']}: {status} \"\n            f\"({result['total_steps']} steps){inj}  \"\n            f\"[{elapsed:.0f}s elapsed, ~{eta:.0f}s remaining]\",\n            flush=True,\n        )\n\n    # --- Build and save report ---\n    report = build_injected_report(results, args)\n\n    os.makedirs(os.path.dirname(os.path.abspath(args.output)), exist_ok=True)\n    with open(args.output, \"w\") as f:\n        json.dump(report, f, indent=2, ensure_ascii=False)\n    print(f\"\\nReport saved to {args.output}\", flush=True)\n\n    # --- Summary ---\n    print(f\"\\n=== Injected Recovery Summary ({args.model_variant}) ===\", flush=True)\n    print(f\"Total: {report['total_episodes']}, Injected: {report['injected_episodes']}\", flush=True)\n    print(f\"Recovery rate: {report['recovery_rate']}\", flush=True)\n    if report[\"by_operator\"]:\n        print(\"By operator:\", flush=True)\n        for op, s in report[\"by_operator\"].items():\n            print(f\"  {op}: {s['recovered']}/{s['total']} ({s['rate']})\", flush=True)\n    if report[\"by_task_type\"]:\n        print(\"By task type:\", flush=True)\n        for tt, s in report[\"by_task_type\"].items():\n            print(f\"  {tt}: {s['recovered']}/{s['total']} ({s['rate']})\", flush=True)\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF\necho \"EXIT_CODE=$?\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-14T17:45:48.187000+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"EXIT_CODE=0\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_recovery-eval-dev_20260514T173802",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-14T17:45:48.187141+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Read existing code and understand project structure', 'status': 'completed', 'activeForm': 'Reading existing code'}, {'content': 'Write eval/injected_eval.py — injected recovery evaluation script', 'status': 'completed', 'activeForm': 'Writing injected eval script'}, {'content': 'Write scripts/run_injected_eval.sh — launcher script for all 3 variants', 'status': 'in_progress', 'activeForm': 'Writing launcher script'}, {'content': 'Deploy to server and dry-run on 1 task with vanilla checkpoint on cuda:3', 'status': 'pending', 'activeForm': 'Deploying and dry-running'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_recovery-eval-dev_20260514T173802",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Read existing code and understand project structure', 'status': 'completed', 'activeForm': 'Reading existing code'}, {'content': 'Write eval/injected_eval.py — injected recovery evaluation script', 'status': 'completed', 'activeForm': 'Writing injected eval script'}, {'content': 'Write scripts/run_injected_eval.sh — launcher script for all 3 variants', 'status': 'in_progress', 'activeForm': 'Writing launcher script'}, {'content': 'Deploy to server and dry-run on 1 task with vanilla checkpoint on cuda:3', 'status': 'pending', 'activeForm': 'Deploying and dry-running'}]"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-14T17:45:48.187283+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_recovery-eval-dev_20260514T173802",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-14T17:45:48.187437+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat > /root/autodl-tmp/tax_error_inject_agent/scripts/run_injected_eval.sh << 'SHEOF'\n#!/bin/bash\n# Injected Recovery Evaluation — run all 3 model variants\n# Usage: bash scripts/run_injected_eval.sh [taxei|random|vanilla|all|compare]\nset -e\n\ncd /root/autodl-tmp/tax_error_inject_agent\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base\n\nBASEM=/root/autodl-tmp/models/Qwen/Qwen3-8B\nmkdir -p eval_results\n\n# Find latest checkpoint: find_final_ckpt &lt;ckpt_root>\nfind_final_ckpt() {\n    local ckpt_root=$1\n    local latest_run\n    latest_run=$(ls -dt \"$ckpt_root\"/v*-*/ 2>/dev/null | head -1)\n    if [ -z \"$latest_run\" ]; then\n        echo \"ERROR: no run dir in $ckpt_root\" >&2; return 1\n    fi\n    local final\n    final=$(ls -d \"$latest_run\"/checkpoint-* 2>/dev/null | sort -V | tail -1)\n    if [ -z \"$final\" ]; then\n        echo \"ERROR: no checkpoint in $latest_run\" >&2; return 1\n    fi\n    if [ ! -f \"$final/adapter_config.json\" ]; then\n        echo \"ERROR: $final missing adapter_config.json\" >&2; return 1\n    fi\n    echo \"$final\"\n}\n\nSEED=${SEED:-42}\nNUM_EPS=${NUM_EPISODES:-47}\nINJ_STEP=${INJECT_STEP:--1}\n\nrun_variant() {\n    local variant=$1\n    local ckpt_root=$2\n    local gpu=$3\n\n    local ckpt\n    ckpt=$(find_final_ckpt \"$ckpt_root\")\n    echo \"[$variant] checkpoint: $ckpt\"\n    echo \"[$variant] GPU: cuda:$gpu\"\n\n    CUDA_VISIBLE_DEVICES=$gpu python eval/injected_eval.py \\\n        --model_path \"$ckpt\" \\\n        --base_model \"$BASEM\" \\\n        --model_variant \"$variant\" \\\n        --output \"eval_results/injected_${variant}.json\" \\\n        --device cuda:0 \\\n        --seed \"$SEED\" \\\n        --num_episodes \"$NUM_EPS\" \\\n        --inject_step \"$INJ_STEP\"\n}\n\nrun_taxei()   { run_variant taxei   checkpoints/mini_taxei_sft_v4   0; }\nrun_random()  { run_variant random  checkpoints/mini_random_sft_v4  1; }\nrun_vanilla() { run_variant vanilla checkpoints/mini_vanilla_sft_v4 2; }\n\nrun_compare() {\n    echo \"=== TaxEI vs Vanilla ===\"\n    python eval/injected_eval.py \\\n        --output eval_results/injected_taxei.json \\\n        --compare_with eval_results/injected_vanilla.json \\\n        --compare_output eval_results/compare_taxei_vs_vanilla.json\n\n    echo \"\"\n    echo \"=== Random vs Vanilla ===\"\n    python eval/injected_eval.py \\\n        --output eval_results/injected_random.json \\\n        --compare_with eval_results/injected_vanilla.json \\\n        --compare_output eval_results/compare_random_vs_vanilla.json\n\n    echo \"\"\n    echo \"=== TaxEI vs Random ===\"\n    python eval/injected_eval.py \\\n        --output eval_results/injected_taxei.json \\\n        --compare_with eval_results/injected_random.json \\\n        --compare_output eval_results/compare_taxei_vs_random.json\n}\n\ncase \"${1:-all}\" in\n    taxei)   run_taxei ;;\n    random)  run_random ;;\n    vanilla) run_vanilla ;;\n    compare) run_compare ;;\n    all)\n        run_taxei &\n        PID_T=$!\n        run_random &\n        PID_R=$!\n        run_vanilla &\n        PID_V=$!\n        echo \"Running all 3 variants in parallel (taxei=$PID_T, random=$PID_R, vanilla=$PID_V)...\"\n        wait $PID_T && echo \"[taxei] done\"   || echo \"[taxei] FAILED\"\n        wait $PID_R && echo \"[random] done\"  || echo \"[random] FAILED\"\n        wait $PID_V && echo \"[vanilla] done\" || echo \"[vanilla] FAILED\"\n        echo \"\"\n        run_compare\n        ;;\n    *)\n        echo \"Usage: bash scripts/run_injected_eval.sh [taxei|random|vanilla|all|compare]\"\n        exit 1\n        ;;\nesac\nSHEOF\nchmod +x /root/autodl-tmp/tax_error_inject_agent/scripts/run_injected_eval.sh\necho \"EXIT_CODE=$?\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_recovery-eval-dev_20260514T173802",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat > /root/autodl-tmp/tax_error_inject_agent/scripts/run_injected_eval.sh << 'SHEOF'\n#!/bin/bash\n# Injected Recovery Evaluation — run all 3 model variants\n# Usage: bash scripts/run_injected_eval.sh [taxei|random|vanilla|all|compare]\nset -e\n\ncd /root/autodl-tmp/tax_error_inject_agent\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base\n\nBASEM=/root/autodl-tmp/models/Qwen/Qwen3-8B\nmkdir -p eval_results\n\n# Find latest checkpoint: find_final_ckpt &lt;ckpt_root>\nfind_final_ckpt() {\n    local ckpt_root=$1\n    local latest_run\n    latest_run=$(ls -dt \"$ckpt_root\"/v*-*/ 2>/dev/null | head -1)\n    if [ -z \"$latest_run\" ]; then\n        echo \"ERROR: no run dir in $ckpt_root\" >&2; return 1\n    fi\n    local final\n    final=$(ls -d \"$latest_run\"/checkpoint-* 2>/dev/null | sort -V | tail -1)\n    if [ -z \"$final\" ]; then\n        echo \"ERROR: no checkpoint in $latest_run\" >&2; return 1\n    fi\n    if [ ! -f \"$final/adapter_config.json\" ]; then\n        echo \"ERROR: $final missing adapter_config.json\" >&2; return 1\n    fi\n    echo \"$final\"\n}\n\nSEED=${SEED:-42}\nNUM_EPS=${NUM_EPISODES:-47}\nINJ_STEP=${INJECT_STEP:--1}\n\nrun_variant() {\n    local variant=$1\n    local ckpt_root=$2\n    local gpu=$3\n\n    local ckpt\n    ckpt=$(find_final_ckpt \"$ckpt_root\")\n    echo \"[$variant] checkpoint: $ckpt\"\n    echo \"[$variant] GPU: cuda:$gpu\"\n\n    CUDA_VISIBLE_DEVICES=$gpu python eval/injected_eval.py \\\n        --model_path \"$ckpt\" \\\n        --base_model \"$BASEM\" \\\n        --model_variant \"$variant\" \\\n        --output \"eval_results/injected_${variant}.json\" \\\n        --device cuda:0 \\\n        --seed \"$SEED\" \\\n        --num_episodes \"$NUM_EPS\" \\\n        --inject_step \"$INJ_STEP\"\n}\n\nrun_taxei()   { run_variant taxei   checkpoints/mini_taxei_sft_v4   0; }\nrun_random()  { run_variant random  checkpoints/mini_random_sft_v4  1; }\nrun_vanilla() { run_variant vanilla checkpoints/mini_vanilla_sft_v4 2; }\n\nrun_compare() {\n    echo \"=== TaxEI vs Vanilla ===\"\n    python eval/injected_eval.py \\\n        --output eval_results/injected_taxei.json \\\n        --compare_with eval_results/injected_vanilla.json \\\n        --compare_output eval_results/compare_taxei_vs_vanilla.json\n\n    echo \"\"\n    echo \"=== Random vs Vanilla ===\"\n    python eval/injected_eval.py \\\n        --output eval_results/injected_random.json \\\n        --compare_with eval_results/injected_vanilla.json \\\n        --compare_output eval_results/compare_random_vs_vanilla.json\n\n    echo \"\"\n    echo \"=== TaxEI vs Random ===\"\n    python eval/injected_eval.py \\\n        --output eval_results/injected_taxei.json \\\n        --compare_with eval_results/injected_random.json \\\n        --compare_output eval_results/compare_taxei_vs_random.json\n}\n\ncase \"${1:-all}\" in\n    taxei)   run_taxei ;;\n    random)  run_random ;;\n    vanilla) run_vanilla ;;\n    compare) run_compare ;;\n    all)\n        run_taxei &\n        PID_T=$!\n        run_random &\n        PID_R=$!\n        run_vanilla &\n        PID_V=$!\n        echo \"Running all 3 variants in parallel (taxei=$PID_T, random=$PID_R, vanilla=$PID_V)...\"\n        wait $PID_T && echo \"[taxei] done\"   || echo \"[taxei] FAILED\"\n        wait $PID_R && echo \"[random] done\"  || echo \"[random] FAILED\"\n        wait $PID_V && echo \"[vanilla] done\" || echo \"[vanilla] FAILED\"\n        echo \"\"\n        run_compare\n        ;;\n    *)\n        echo \"Usage: bash scripts/run_injected_eval.sh [taxei|random|vanilla|all|compare]\"\n        exit 1\n        ;;\nesac\nSHEOF\nchmod +x /root/autodl-tmp/tax_error_inject_agent/scripts/run_injected_eval.sh\necho \"EXIT_CODE=$?\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-14T17:45:48.187644+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"EXIT_CODE=0\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_recovery-eval-dev_20260514T173802",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-14T17:45:48.187787+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Read existing code and understand project structure', 'status': 'completed', 'activeForm': 'Reading existing code'}, {'content': 'Write eval/injected_eval.py — injected recovery evaluation script', 'status': 'completed', 'activeForm': 'Writing injected eval script'}, {'content': 'Write scripts/run_injected_eval.sh — launcher script for all 3 variants', 'status': 'completed', 'activeForm': 'Writing launcher script'}, {'content': 'Deploy to server and dry-run on 1 task with vanilla checkpoint on cuda:3', 'status': 'in_progress', 'activeForm': 'Deploying and dry-running'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_recovery-eval-dev_20260514T173802",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Read existing code and understand project structure', 'status': 'completed', 'activeForm': 'Reading existing code'}, {'content': 'Write eval/injected_eval.py — injected recovery evaluation script', 'status': 'completed', 'activeForm': 'Writing injected eval script'}, {'content': 'Write scripts/run_injected_eval.sh — launcher script for all 3 variants', 'status': 'completed', 'activeForm': 'Writing launcher script'}, {'content': 'Deploy to server and dry-run on 1 task with vanilla checkpoint on cuda:3', 'status': 'in_progress', 'activeForm': 'Deploying and dry-running'}]"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-14T17:45:48.187927+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_recovery-eval-dev_20260514T173802",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-14T17:45:48.188043+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "wc -l /root/autodl-tmp/tax_error_inject_agent/eval/injected_eval.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_recovery-eval-dev_20260514T173802",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "wc -l /root/autodl-tmp/tax_error_inject_agent/eval/injected_eval.py",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-14T17:45:48.188155+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "head -5 /root/autodl-tmp/tax_error_inject_agent/eval/injected_eval.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_recovery-eval-dev_20260514T173802",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "head -5 /root/autodl-tmp/tax_error_inject_agent/eval/injected_eval.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-14T17:45:48.188268+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"463 /root/autodl-tmp/tax_error_inject_agent/eval/injected_eval.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_recovery-eval-dev_20260514T173802",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-14T17:45:48.188386+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"\\nInjected Recovery Evaluation — wrong-action injection + error tag.\\n\\nAt a chosen step, replaces the model's action with a random wrong action\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_recovery-eval-dev_20260514T173802",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-14T17:45:48.188548+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "cd /root/autodl-tmp/tax_error_inject_agent && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && VANILLA_CKPT=$(ls -dt checkpoints/mini_vanilla_sft_v4/v0-*/checkpoint-* | sort -V | tail -1) && echo \"Checkpoint: $VANILLA_CKPT\" && CUDA_VISIBLE_DEVICES=3 python eval/injected_eval.py --model_path \"$VANILLA_CKPT\" --model_variant vanilla --device cuda:0 --num_episodes 1 --inject_step 2 --output eval_results/dryrun_injected_vanilla.json --seed 42 2>&1",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_recovery-eval-dev_20260514T173802",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cd /root/autodl-tmp/tax_error_inject_agent && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && VANILLA_CKPT=$(ls -dt checkpoints/mini_vanilla_sft_v4/v0-*/checkpoint-* | sort -V | tail -1) && echo \"Checkpoint: $VANILLA_CKPT\" && CUDA_VISIBLE_DEVICES=3 python eval/injected_eval.py --model_path \"$VANILLA_CKPT\" --model_variant vanilla --device cuda:0 --num_episodes 1 --inject_step 2 --output eval_results/dryrun_injected_vanilla.json --seed 42 2>&1",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-14T17:45:48.188710+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Checkpoint: checkpoints/mini_vanilla_sft_v4/v0-20260514-201441/checkpoint-1635\\nLoaded 47 tasks from /root/autodl-tmp/tax_error_inject_agent/eval/eval_tasks_47.json\\nModel variant: vanilla\\nLoading base model: /root/autodl-tmp/models/Qwen/Qwen3-8B\\n`torch_dtype` is deprecated! Use `dtype` instead!\\n\\rLoading checkpoint shards:   0%|          | 0/5 [00:00<?, ?it/s]\\rLoading checkpoint shards:  20%|██        | 1/5 [00:00<00:02,  1.50it/s]\\rLoading checkpoint shards:  40%|████      | 2/5 [00:01<00:01,  1.52it/s]\\rLoading checkpoint shards:  60%|██████    | 3/5 [00:01<00:01,  1.55it/s]\\rLoading checkpoint shards:  80%|████████  | 4/5 [00:02<00:00,  1.70it/s]\\rLoading checkpoint shards: 100%|██████████| 5/5 [00:02<00:00,  2.24it/s]\\rLoading checkpoint shards: 100%|██████████| 5/5 [00:02<00:00,  1.89it/s]\\nLoading LoRA adapter: checkpoints/mini_vanilla_sft_v4/v0-20260514-201441/checkpoint-1635\\nbitsandbytes library load error: libnvJitLink.so.13: cannot open shared object file: No such file or directory\\nTraceback (most recent call last):\\n  File \\\"/root/miniconda3/lib/python3.12/site-packages/bitsandbytes/cextension.py\\\", line 320, in &lt;module>\\n    lib = get_native_library()\\n          ^^^^^^^^^^^^^^^^^^^^\\n  File \\\"/root/miniconda3/lib/python3.12/site-packages/bitsandbytes/cextension.py\\\", line 298, in get_native_library\\n    dll = ct.cdll.LoadLibrary(str(binary_path))\\n          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\\n  File \\\"/root/miniconda3/lib/python3.12/ctypes/__init__.py\\\", line 460, in LoadLibrary\\n    return self._dlltype(name)\\n           ^^^^^^^^^^^^^^^^^^^\\n  File \\\"/root/miniconda3/lib/python3.12/ctypes/__init__.py\\\", line 379, in __init__\\n    self._handle = _dlopen(self._name, mode)\\n                   ^^^^^^^^^^^^^^^^^^^^^^^^^\\nOSError: libnvJitLink.so.13: cannot open shared object file: No such file or directory\\nThe following generation flags are not val
…[truncated 610 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_recovery-eval-dev_20260514T173802",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-14T17:45:48.188860+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/tax_error_inject_agent/eval_results/dryrun_injected_vanilla.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_recovery-eval-dev_20260514T173802",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/tax_error_inject_agent/eval_results/dryrun_injected_vanilla.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-14T17:45:48.189020+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model\\\": \\\"checkpoints/mini_vanilla_sft_v4/v0-20260514-201441/checkpoint-1635\\\",\\n  \\\"model_variant\\\": \\\"vanilla\\\",\\n  \\\"eval_type\\\": \\\"injected_recovery\\\",\\n  \\\"total_episodes\\\": 1,\\n  \\\"injected_episodes\\\": 1,\\n  \\\"recovery_rate\\\": 1.0,\\n  \\\"timestamp\\\": \\\"2026-05-14T17:45:10.586252+00:00\\\",\\n  \\\"config\\\": {\\n    \\\"inject_step\\\": 2,\\n    \\\"operators\\\": [\\n      \\\"P1_StepOrderSwap\\\",\\n      \\\"P2_SubGoalDeletion\\\",\\n      \\\"C1_ContextTruncation\\\",\\n      \\\"C4_ObservationMasking\\\"\\n    ],\\n    \\\"seed\\\": 42\\n  },\\n  \\\"by_operator\\\": {\\n    \\\"P1_StepOrderSwap\\\": {\\n      \\\"total\\\": 1,\\n      \\\"recovered\\\": 1,\\n      \\\"rate\\\": 1.0\\n    }\\n  },\\n  \\\"by_task_type\\\": {\\n    \\\"look_at_obj_in_light\\\": {\\n      \\\"total\\\": 1,\\n      \\\"recovered\\\": 1,\\n      \\\"rate\\\": 1.0\\n    }\\n  },\\n  \\\"episodes\\\": [\\n    {\\n      \\\"task_name\\\": \\\"look_at_obj_in_light-AlarmClock-None-DeskLamp-308\\\",\\n      \\\"task_type\\\": \\\"look_at_obj_in_light\\\",\\n      \\\"task_desc\\\": \\\"Hold the clock and turn on the lamp.\\\",\\n      \\\"recovered\\\": true,\\n      \\\"total_steps\\\": 13,\\n      \\\"injected\\\": true,\\n      \\\"model_variant\\\": \\\"vanilla\\\",\\n      \\\"injected_error_type\\\": \\\"P1_StepOrderSwap\\\",\\n      \\\"inject_step\\\": 2,\\n      \\\"original_action\\\": \\\"go to desk 2\\\",\\n      \\\"injected_action\\\": \\\"take bowl 1 from desk 1\\\",\\n      \\\"error_tag\\\": \\\"\\\"\\n    }\\n  ]\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_recovery-eval-dev_20260514T173802",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-14T17:45:48.189154+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Read existing code and understand project structure', 'status': 'completed', 'activeForm': 'Reading existing code'}, {'content': 'Write eval/injected_eval.py — injected recovery evaluation script', 'status': 'completed', 'activeForm': 'Writing injected eval script'}, {'content': 'Write scripts/run_injected_eval.sh — launcher script for all 3 variants', 'status': 'completed', 'activeForm': 'Writing launcher script'}, {'content': 'Deploy to server and dry-run on 1 task with vanilla checkpoint on cuda:3', 'status': 'completed', 'activeForm': 'Deploying and dry-running'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_recovery-eval-dev_20260514T173802",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Read existing code and understand project structure', 'status': 'completed', 'activeForm': 'Reading existing code'}, {'content': 'Write eval/injected_eval.py — injected recovery evaluation script', 'status': 'completed', 'activeForm': 'Writing injected eval script'}, {'content': 'Write scripts/run_injected_eval.sh — launcher script for all 3 variants', 'status': 'completed', 'activeForm': 'Writing launcher script'}, {'content': 'Deploy to server and dry-run on 1 task with vanilla checkpoint on cuda:3', 'status': 'completed', 'activeForm': 'Deploying and dry-running'}]"
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-14T17:45:48.189289+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_recovery-eval-dev_20260514T173802",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-14T17:45:48.189423+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

````json
{
  "name": "injected_eval_pipeline",
  "type": "intermediate",
  "description": "Injected Recovery Evaluation pipeline: eval/injected_eval.py + scripts/run_injected_eval.sh. Injects wrong actions at eval time and measures recovery success rate per model variant (taxei/random/vanilla).",
  "project": "tax_error_inject_agent",
  "tags": "['eval', 'recovery', 'injection', 'D009']",
  "content": "# Injected Recovery Evaluation Pipeline\n\n## Files\n- `eval/injected_eval.py` — main eval script (463 lines)\n- `scripts/run_injected_eval.sh` — launcher for all 3 variants\n\n## Design\nAt a chosen step (default random [2,4]), replaces the model's action with a random wrong action from admissible commands, executes it in the environment, and inserts an error tag matching the model variant's training format:\n- **taxei**: `[Error Type: P1_StepOrderSwap]` (taxonomy-specific)\n- **random**: `[Error occurred]` (generic)\n- **vanilla**: no tag\n\nOperator labels cycle round-robin through P1/P2/C1/C4.\n\n## Usage\n```bash\n# Single variant\npython eval/injected_eval.py --model_path &lt;ckpt> --model_variant taxei --device cuda:0\n\n# All 3 variants in parallel + comparison\nbash scripts/run_injected_eval.sh all\n\n# Compare two results\npython eval/injected_eval.py --output results_a.json --compare_with results_b.json\n```\n\n## Output JSON\n```json\n{\n  \"recovery_rate\": 0.xxx,\n  \"by_operator\": {...},\n  \"by_task_type\": {...},\n  \"episodes\": [{\n    \"task_name\": \"...\", \"recovered\": true/false,\n    \"inject_step\": 2, \"original_action\": \"go to desk 2\",\n    \"injected_action\": \"take bowl 1 from desk 1\",\n    \"error_tag\": \"[Error Type: P1_StepOrderSwap]\"\n  }]\n}\n```\n\n## Dry-run verified\nVanilla checkpoint, 1 task, cuda:3 — RECOVERED in 13 steps (original: \"go to desk 2\", injected: \"take bowl 1 from desk 1\").",
  "content_filename": "injected_eval_pipeline.md"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_code_recovery-eval-dev_20260514T173802",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "injected_eval_pipeline",
    "type": "intermediate",
    "description": "Injected Recovery Evaluation pipeline: eval/injected_eval.py + scripts/run_injected_eval.sh. Injects wrong actions at eval time and measures recovery success rate per model variant (taxei/random/vanilla).",
    "project": "tax_error_inject_agent",
    "tags": "['eval', 'recovery', 'injection', 'D009']",
    "content": "# Injected Recovery Evaluation Pipeline\n\n## Files\n- `eval/injected_eval.py` — main eval script (463 lines)\n- `scripts/run_injected_eval.sh` — launcher for all 3 variants\n\n## Design\nAt a chosen step (default random [2,4]), replaces the model's action with a random wrong action from admissible commands, executes it in the environment, and inserts an error tag matching the model variant's training format:\n- **taxei**: `[Error Type: P1_StepOrderSwap]` (taxonomy-specific)\n- **random**: `[Error occurred]` (generic)\n- **vanilla**: no tag\n\nOperator labels cycle round-robin through P1/P2/C1/C4.\n\n## Usage\n```bash\n# Single variant\npython eval/injected_eval.py --model_path &lt;ckpt> --model_variant taxei --device cuda:0\n\n# All 3 variants in parallel + comparison\nbash scripts/run_injected_eval.sh all\n\n# Compare two results\npython eval/injected_eval.py --output results_a.json --compare_with results_b.json\n```\n\n## Output JSON\n```json\n{\n  \"recovery_rate\": 0.xxx,\n  \"by_operator\": {...},\n  \"by_task_type\": {...},\n  \"episodes\": [{\n    \"task_name\": \"...\", \"recovered\": true/false,\n    \"inject_step\": 2, \"original_action\": \"go to desk 2\",\n    \"injected_action\": \"take bowl 1 from desk 1\",\n    \"error_tag\": \"[Error Type: P1_StepOrderSwap]\"\n  }]\n}\n```\n\n## Dry-run verified\nVanilla checkpoint, 1 task, cuda:3 — RECOVERED in 13 steps (original: \"go to desk 2\", injected: \"take bowl 1 from desk 1\").",
    "content_filename": "injected_eval_pipeline.md"
  }
}
````

</details>

---

### Tool result

_source line 76 · 2026-05-14T17:45:48.189595+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260514_37758c\", \"name\": \"injected_eval_pipeline\", \"type\": \"intermediate\", \"description\": \"Injected Recovery Evaluation pipeline: eval/injected_eval.py + scripts/run_injected_eval.sh. Injects wrong actions at eval time and measures recovery success rate per model variant (taxei/random/vanilla).\", \"path\": \"projects/tax_error_inject_agent/artifacts/_project/intermediate/injected_eval_pipeline.md\", \"url\": null, \"project\": \"tax_error_inject_agent\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-14T17:45:37.728870+00:00\", \"tags\": [\"eval\", \"recovery\", \"injection\", \"D009\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_recovery-eval-dev_20260514T173802",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 77 · 2026-05-14T17:45:48.189775+00:00_

完成。产出总结：

**`eval/injected_eval.py`** (463 行) — Injected Recovery Evaluation 脚本
- 在 eval 时注入错误 action：在指定步骤替换模型的 action 为随机错误 action，发送给环境
- 根据 `--model_variant` 插入训练格式匹配的 error tag：
  - taxei → `[Error Type: P1_StepOrderSwap]` 等
  - random → `[Error occurred]`
  - vanilla → 无标签
- 输出 JSON：per-task recovery 结果 + aggregate recovery_rate / by_operator / by_task_type
- 内置 `--compare_with` 统计检验（McNemar + bootstrap CI）

**`scripts/run_injected_eval.sh`** — 3 个变体的启动脚本
- `bash scripts/run_injected_eval.sh all` 并行跑 3 个模型 + 自动对比
- 支持单独跑 `taxei`/`random`/`vanilla`/`compare`

**Dry-run 验证通过**: Vanilla checkpoint, 1 task, cuda:3 — 注入 `take bowl 1 from desk 1`（原本 `go to desk 2`），模型 13 步 RECOVERED。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_recovery-eval-dev_20260514T173802"
}
```

</details>

---
