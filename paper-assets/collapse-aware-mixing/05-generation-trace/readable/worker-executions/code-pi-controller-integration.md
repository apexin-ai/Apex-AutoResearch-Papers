# code pi controller integration

**collapse aware mixing** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 49
- **Recorded user turns:** 1
- **Tool calls:** 15
- **Original source:** `logs/workers/worker_code_pi-controller-integration_20260513T081846.log`
- **Structured JSON:** [`75f6f655e36dfca9a7e7.json`](../../sessions/75/75f6f655e36dfca9a7e7.json)

## Before a recorded user message

6 recorded events

### Log line

_source line 1_

Warning: no stdin data received in 3s, proceeding without it. If piping from a slow command, redirect stdin explicitly: < /dev/null to skip, or wait longer.

---

### System

_source line 2_

```json
{
  "type": "system",
  "subtype": "init",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/code",
  "session_id": "60ff85cb-037b-4c00-9e51-254478230283",
  "tools": [
    "Task",
    "AskUserQuestion",
    "Bash",
    "CronCreate",
    "CronDelete",
    "CronList",
    "Edit",
    "EnterPlanMode",
    "EnterWorktree",
    "ExitPlanMode",
    "ExitWorktree",
    "Glob",
    "Grep",
    "ListMcpResourcesTool",
    "Monitor",
    "NotebookEdit",
    "PushNotification",
    "Read",
    "ReadMcpResourceTool",
    "RemoteTrigger",
    "ScheduleWakeup",
    "Skill",
    "TaskOutput",
    "TaskStop",
    "TodoWrite",
    "ToolSearch",
    "WebFetch",
    "WebSearch",
    "Write",
    "mcp__agent-ml-research__allocate_and_submit",
    "mcp__agent-ml-research__append_idea",
    "mcp__agent-ml-research__approve_worker",
    "mcp__agent-ml-research__auto_build_provenance",
    "mcp__agent-ml-research__backup_project_to_s3",
    "mcp__agent-ml-research__cancel_worker",
    "mcp__agent-ml-research__check_job_status",
    "mcp__agent-ml-research__check_paper_consistency",
    "mcp__agent-ml-research__check_provenance_completeness",
    "mcp__agent-ml-research__cleanup_pdf_images",
    "mcp__agent-ml-research__compute_coverage_matrix",
    "mcp__agent-ml-research__detect_image",
    "mcp__agent-ml-research__edit_paper_section",
    "mcp__agent-ml-research__feishu_read_tum_pending_key",
    "mcp__agent-ml-research__feishu_send_alert",
    "mcp__agent-ml-research__feishu_send_approval_card",
    "mcp__agent-ml-research__feishu_send_result_card",
    "mcp__agent-ml-research__feishu_send_tum_key_request_card",
    "mcp__agent-ml-research__fetch_wandb_metrics",
    "mcp__agent-ml-research__get_baseline_metrics",
    "mcp__agent-ml-research__get_gpu_health",
    "mcp__agent-ml-research__get_image_info",
    "mcp__agent-ml-research__get_matrix_value",
    "mcp__agent-ml-research__get_project_resource_usage",
    "mcp__agent-ml-research__get_tum_config",
    "mcp__agent-ml-research__get_worker_status",
    "mcp__agent-ml-research__impact_analysis",
    "mcp__agent-ml-research__kill_job",
    "mcp__agent-ml-research__list_artifacts",
    "mcp__agent-ml-research__list_available_gpus",
    "mcp__agent-ml-research__list_constraints",
    "mcp__agent-ml-research__list_s3_backups",
    "mcp__agent-ml-research__list_workers",
    "mcp__agent-ml-research__load_project_config",
    "mcp__agent-ml-research__main_agent_post_to_director",
    "mcp__agent-ml-research__matrix_gap_analysis",
    "mcp__agent-ml-research__pdf_to_images",
    "mcp__agent-ml-research__poll_cron",
    "mcp__agent-ml-research__poll_secret_request",
    "mcp__agent-ml-research__read_experiment_plan_with_status",
    "mcp__agent-ml-research__read_matrix",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__read_registry",
    "mcp__agent-ml-research__read_roadmap",
    "mcp__agent-ml-research__reconcile_crons",
    "mcp__agent-ml-research__register_artifact",
    "mcp__agent-ml-research__register_cron",
    "mcp__agent-ml-research__request_secret",
    "mcp__agent-ml-research__save_project_file",
    "mcp__agent-ml-research__send_progress",
    "mcp__agent-ml-research__spawn_worker",
    "mcp__agent-ml-research__submit_on_allocated",
    "mcp__agent-ml-research__submit_training_job",
    "mcp__agent-ml-research__sync_matrix_status",
    "mcp__agent-ml-research__tail_training_logs",
    "mcp__agent-ml-research__update_baseline",
    "mcp__agent-ml-research__update_matrix",
    "mcp__agent-ml-research__update_registry",
    "mcp__agent-ml-research__verify_references",
    "mcp__agent-ml-research__write_paper_section"
  ],
  "mcp_servers": [
    {
      "name": "agent-ml-research",
      "status": "connected"
    }
  ],
  "model": "claude-opus-4-6",
  "permissionMode": "bypassPermissions",
  "slash_commands": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api",
    "clear",
    "compact",
    "context",
    "heapdump",
    "init",
    "review",
    "security-review",
    "extra-usage",
    "usage",
    "insights",
    "team-onboarding"
  ],
  "apiKeySource": "none",
  "claude_code_version": "2.1.126",
  "output_style": "default",
  "agents": [
    "claude",
    "Explore",
    "general-purpose",
    "Plan",
    "statusline-setup"
  ],
  "skills": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api"
  ],
  "plugins": [],
  "analytics_disabled": false,
  "uuid": "8b431a51-00c6-4da3-9b71-16b155ebb92c",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-collapse-aware-mixing-artifacts-code/memory/"
  },
  "fast_mode_state": "off"
}
```

---

### Runtime record

_source line 3_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1778677800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "83500e12-1578-47f2-9be8-b551a17be21a",
  "session_id": "60ff85cb-037b-4c00-9e51-254478230283"
}
```

---

### Assistant

_source line 4_

Let me first read the existing code files to understand the exact interfaces.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "60ff85cb-037b-4c00-9e51-254478230283",
  "uuid": "0f25172d-727d-4c08-aa67-1cfe1c6e2760",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TrS9MQ3QiL5DypV6SoTUsX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13247,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13247
      },
      "output_tokens": 2,
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

_source line 5_

<details open><summary>🔧 Tool call — Agent · `toolu_013HbNm4hmuyFcsh6bszPyyR`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Read existing code files",
  "prompt": "Read the following files in full and report their complete contents:\n1. /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/code/controller.py\n2. /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/code/pilot_pipeline.py\n3. /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/code/train.py\n4. /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/code/data_utils.py\n5. /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/code/metrics.py\n6. /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/code/config.py\n\nReport each file's full content so I can understand the exact APIs, imports, and signatures."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "60ff85cb-037b-4c00-9e51-254478230283",
  "uuid": "bec38f09-3f94-414c-819f-a18c4cb4f431",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TrS9MQ3QiL5DypV6SoTUsX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13247,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13247
      },
      "output_tokens": 2,
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

### System

_source line 6_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a431d4224180b832d",
  "tool_use_id": "toolu_013HbNm4hmuyFcsh6bszPyyR",
  "description": "Read existing code files",
  "task_type": "local_agent",
  "prompt": "Read the following files in full and report their complete contents:\n1. /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/code/controller.py\n2. /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/code/pilot_pipeline.py\n3. /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/code/train.py\n4. /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/code/data_utils.py\n5. /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/code/metrics.py\n6. /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/code/config.py\n\nReport each file's full content so I can understand the exact APIs, imports, and signatures.",
  "uuid": "db6dae6e-4155-4bd1-960b-668a2843acb6",
  "session_id": "60ff85cb-037b-4c00-9e51-254478230283"
}
```

---

## Round 1

43 recorded events

### User

_source line 7 · 2026-05-13T08:19:01.478Z_

Read the following files in full and report their complete contents:
1. /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/code/controller.py
2. /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/code/pilot_pipeline.py
3. /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/code/train.py
4. /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/code/data_utils.py
5. /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/code/metrics.py
6. /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/code/config.py

Report each file's full content so I can understand the exact APIs, imports, and signatures.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_013HbNm4hmuyFcsh6bszPyyR",
  "session_id": "60ff85cb-037b-4c00-9e51-254478230283",
  "uuid": "4bc394a4-7644-474c-842a-969b19105c70"
}
```

</details>

---

### System

_source line 8_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a431d4224180b832d",
  "tool_use_id": "toolu_013HbNm4hmuyFcsh6bszPyyR",
  "description": "Reading controller.py",
  "usage": {
    "total_tokens": 34654,
    "tool_uses": 1,
    "duration_ms": 1926
  },
  "last_tool_name": "Read",
  "uuid": "288df621-7e66-4ac3-9d91-8aba0ac4268c",
  "session_id": "60ff85cb-037b-4c00-9e51-254478230283"
}
```

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Read · `toolu_01HuvJzxwadR8fnShrTrBLJE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/code/controller.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_013HbNm4hmuyFcsh6bszPyyR",
  "session_id": "60ff85cb-037b-4c00-9e51-254478230283",
  "uuid": "e9f44626-f637-4428-8e19-24bce2eedb7f",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VzjWwhytZf7rmx8BkGpwja",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 34645,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 34645,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 10 · 2026-05-13T08:19:03.416Z_

<details><summary>↩ Tool result · `toolu_01HuvJzxwadR8fnShrTrBLJE`</summary>

```text
1	"""Discrete-time PI controller for collapse-aware real/synthetic data mixing.
2	
3	Adjusts the real data ratio w_t based on spectral effective rank signal,
4	increasing real data when rank drops (collapse risk) and decreasing it
5	when rank recovers.
6	"""
7	
8	from dataclasses import dataclass
9	from typing import List, Optional
10	
11	
12	@dataclass
13	class ControllerConfig:
14	    Kp: float = 0.01
15	    Ki: float = 0.005
16	    r_target: float = 50.0
17	    w_init: float = 0.5
18	    w_min: float = 0.1
19	    w_max: float = 0.9
20	
21	
22	class CollapseAwareController:
23	    def __init__(self, config: ControllerConfig):
24	        self.config = config
25	        self._w: float = config.w_init
26	        self._r_prev: Optional[float] = None
27	        self._integral: float = 0.0
28	        self._proportional: float = 0.0
29	        self._r_history: List[float] = []
30	        self._w_history: List[float] = [config.w_init]
31	        self._step_count: int = 0
32	
33	    def step(self, r_t: float) -> float:
34	        """Given current spectral rank, return updated real data ratio w_t."""
35	        cfg = self.config
36	
37	        if self._r_prev is None:
38	            self._r_prev = r_t
39	            self._r_history.append(r_t)
40	            return self._w
41	
42	        error = r_t - cfg.r_target
43	        delta_r = r_t - self._r_prev
44	
45	        # rank drop (negative delta_r / negative error) → increase w
46	        self._proportional = -cfg.Kp * delta_r
47	        self._integral += -cfg.Ki * error
48	
49	        self._w = self._w + self._proportional + (-cfg.Ki * error)
50	
51	        self._w = max(cfg.w_min, min(cfg.w_max, self._w))
52	
53	        self._r_prev = r_t
54	        self._r_history.append(r_t)
55	        self._w_history.append(self._w)
56	        self._step_count += 1
57	
58	        return self._w
59	
60	    def get_state(self) -> dict:
61	        """Return controller internals."""
62	        return {
63	            "w": self._w,
64	            "proportional_term": self._proportional,
65	            "integral_term": self._integral,
66	            "r_history": list(self._r_history),
67	            "w_history": list(self._w_history),
68	            "step_count": self._step_count,
69	        }
70	
71	    def reset(self):
72	        """Reset controller state to initial."""
73	        self._w = self.config.w_init
74	        self._r_prev = None
75	        self._integral = 0.0
76	        self._proportional = 0.0
77	        self._r_history = []
78	        self._w_history = [self.config.w_init]
79	        self._step_count = 0
80	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_013HbNm4hmuyFcsh6bszPyyR",
  "session_id": "60ff85cb-037b-4c00-9e51-254478230283",
  "uuid": "4b2ce907-92b2-4a0a-88e0-5e81ad9db7c4"
}
```

</details>

---

### System

_source line 11_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a431d4224180b832d",
  "tool_use_id": "toolu_013HbNm4hmuyFcsh6bszPyyR",
  "description": "Reading pilot_pipeline.py",
  "usage": {
    "total_tokens": 34657,
    "tool_uses": 2,
    "duration_ms": 2189
  },
  "last_tool_name": "Read",
  "uuid": "50b70cab-5f74-40f9-a2a4-3d31bea3ab9d",
  "session_id": "60ff85cb-037b-4c00-9e51-254478230283"
}
```

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Read · `toolu_01XgZuF1kCPG2bFmdtwoQkgZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/code/pilot_pipeline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_013HbNm4hmuyFcsh6bszPyyR",
  "session_id": "60ff85cb-037b-4c00-9e51-254478230283",
  "uuid": "adf7d107-a946-4f33-a165-b59ffd2c6bf3",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VzjWwhytZf7rmx8BkGpwja",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 34645,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 34645,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 13 · 2026-05-13T08:19:03.675Z_

<details><summary>↩ Tool result · `toolu_01XgZuF1kCPG2bFmdtwoQkgZ`</summary>

```text
1	"""End-to-end pilot pipeline: G0 -> gen -> G1 -> gen -> G2 with metrics at every checkpoint.
2	
3	Usage:
4	    python pilot_pipeline.py [--output_dir ./output] [--num_generations 3] [--no_wandb]
5	"""
6	
7	import argparse
8	import json
9	import logging
10	import os
11	import sys
12	import time
13	
14	import numpy as np
15	import torch
16	from transformers import AutoModelForCausalLM, AutoTokenizer
17	
18	from config import PilotConfig
19	from data_utils import (
20	    prepare_real_data,
21	    prepare_synthetic_data,
22	    extract_token_ids,
23	    make_dataloader,
24	)
25	from generate import generate_synthetic_data, generate_sample_tokens
26	from metrics import compute_checkpoint_metrics
27	from train import train_generation
28	
29	logging.basicConfig(
30	    level=logging.INFO,
31	    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
32	    handlers=[logging.StreamHandler(sys.stdout)],
33	)
34	logger = logging.getLogger("pilot")
35	
36	
37	def evaluate_checkpoints(
38	    checkpoint_paths: list[str],
39	    gen_idx: int,
40	    holdout_dataset,
41	    prev_gen_token_ids: list[int] | None,
42	    config: PilotConfig,
43	    device: str,
44	) -> list[dict]:
45	    """Load each checkpoint, compute all metrics, return list of metric dicts."""
46	    tokenizer = AutoTokenizer.from_pretrained(config.model_name)
47	    if tokenizer.pad_token is None:
48	        tokenizer.pad_token = tokenizer.eos_token
49	    vocab_size = tokenizer.vocab_size
50	
51	    holdout_loader = make_dataloader(holdout_dataset, batch_size=config.ppl_batch_size)
52	    all_metrics = []
53	
54	    for ci, ckpt_path in enumerate(checkpoint_paths):
55	        logger.info("--- Evaluating checkpoint %d/%d: %s ---", ci + 1, len(checkpoint_paths), ckpt_path)
56	        t0 = time.time()
57	
58	        model = AutoModelForCausalLM.from_pretrained(ckpt_path, torch_dtype=torch.bfloat16).to(device)
59	        model.eval()
60	
61	        # generate a small sample for n-gram / coverage metrics
62	        logger.info("Generating %dK tokens for corpus metrics ...", config.metrics_gen_tokens // 1000)
63	        gen_ids = generate_sample_tokens(
64	            model, tokenizer,
65	            num_tokens=config.metrics_gen_tokens,
66	            batch_size=config.gen_batch_size,
67	            max_new_tokens=256,
68	            temperature=config.gen_temperature,
69	            top_p=config.gen_top_p,
70	            device=device,
71	        )
72	
73	        m = compute_checkpoint_metrics(
74	            model=model,
75	            holdout_loader=holdout_loader,
76	            gen_token_ids=gen_ids,
77	            prev_gen_token_ids=prev_gen_token_ids,
78	            vocab_size=vocab_size,
79	            config=config,
80	            device=device,
81	        )
82	        m["generation"] = gen_idx
83	        m["checkpoint"] = ckpt_path
84	        m["checkpoint_index"] = ci
85	
86	        # extract step count from checkpoint dir name
87	        step_str = os.path.basename(ckpt_path).split("-")[-1]
88	        m["global_step"] = int(step_str) if step_str.isdigit() else ci
89	        m["tokens_seen"] = m["global_step"] * config.tokens_per_step
90	        m["eval_time_sec"] = time.time() - t0
91	
92	        all_metrics.append(m)
93	        logger.info(
94	            "  eff_rank=%.1f  ppl=%.2f  entropy_var=%.4f  unigram_H=%.3f  coverage=%.4f  (%.0fs)",
95	            m["spectral_effective_rank"], m["perplexity"],
96	            m["token_entropy_var"], m["unigram_entropy"],
97	            m["vocab_coverage"], m["eval_time_sec"],
98	        )
99	
100	        del model
101	        torch.cuda.empty_cache()
102	
103	    return all_metrics
104	
105	
106	def save_metrics(metrics: list[dict], path: str):
107	    os.makedirs(os.path.dirname(path), exist_ok=True)
108	    with open(path, "a") as f:
109	        for m in metrics:
110	            f.write(json.dumps(m, default=str) + "\n")
111	    logger.info("Metrics appended to %s", path)
112	
113	
114	def run_pilot(config: PilotConfig):
115	    device = "cuda" if torch.cuda.is_available() else "cpu"
116	    os.makedirs(config.output_dir, exist_ok=True)
117	
118	    logger.info("=" * 60)
119	    logger.info("PILOT PIPELINE START")
120	    logger.info("  Model: %s", config.model_name)
121	    logger.info("  Generations: %d | Tokens/gen: %dM", config.num_generations, config.tokens_per_generation // 1_000_000)
122	    logger.info("  Checkpoint interval: %dM tokens (%d steps)", config.checkpoint_interval_tokens // 1_000_000, config.save_steps)
123	    logger.info("  Device: %s", device)
124	    logger.info("=" * 60)
125	
126	    # --- Prepare data ---
127	    tokenizer = AutoTokenizer.from_pretrained(config.model_name)
128	    if tokenizer.pad_token is None:
129	        tokenizer.pad_token = tokenizer.eos_token
130	
131	    logger.info("Preparing real data ...")
132	    train_dataset, holdout_dataset = prepare_real_data(config, tokenizer)
133	
134	    all_results = []
135	    prev_gen_token_ids = None
136	    prev_model_dir = None  # G0: None → config.model_name; G1+: previous gen's final checkpoint
137	    g0_baseline = None  # populated after G0 evaluation
138	
139	    for g in range(config.num_generations):
140	        logger.info("=" * 60)
141	        logger.info("GENERATION %d / %d", g, config.num_generations - 1)
142	        logger.info("=" * 60)
143	
144	        # --- Determine training data ---
145	        if g == 0:
146	            gen_train = train_dataset
147	        else:
148	            synth_path = config.synthetic_data_path(g - 1)
149	            gen_train = prepare_synthetic_data(synth_path, config, tokenizer)
150	
151	        # --- Train (chain model from previous generation) ---
152	        final_model_dir, ckpt_paths = train_generation(
153	            gen_idx=g,
154	            train_dataset=gen_train,
155	            config=config,
156	            model_name_or_path=prev_model_dir,
157	        )
158	
159	        # include final model as the last eval point
160	        if final_model_dir not in ckpt_paths:
161	            ckpt_paths.append(final_model_dir)
162	
163	        # --- Evaluate all checkpoints ---
164	        gen_metrics = evaluate_checkpoints(
165	            checkpoint_paths=ckpt_paths,
166	            gen_idx=g,
167	            holdout_dataset=holdout_dataset,
168	            prev_gen_token_ids=prev_gen_token_ids,
169	            config=config,
170	            device=device,
171	        )
172	        save_metrics(gen_metrics, config.metrics_path(g))
173	        all_results.extend(gen_metrics)
174	
175	        # --- G0 baseline statistics for leading-indicator threshold ---
176	        if g == 0 and gen_metrics:
177	            ranks = np.array([m["spectral_effective_rank"] for m in gen_metrics])
178	            ppls = np.array([m["perplexity"] for m in gen_metrics])
179	            g0_baseline = {
180	                "spectral_rank_mean": float(ranks.mean()),
181	                "spectral_rank_std": float(ranks.std()),
182	                "spectral_rank_min": float(ranks.min()),
183	                "spectral_rank_max": float(ranks.max()),
184	                "ppl_final": float(ppls[-1]),
185	                "ppl_mean": float(ppls.mean()),
186	                "ppl_std": float(ppls.std()),
187	                "num_checkpoints": len(gen_metrics),
188	            }
189	            logger.info("G0 BASELINE: rank=%.1f +/- %.2f (sigma for 1-sigma threshold)  ppl_final=%.2f",
190	                         g0_baseline["spectral_rank_mean"], g0_baseline["spectral_rank_std"],
191	                         g0_baseline["ppl_final"])
192	
193	        # --- Generate synthetic data for next generation ---
194	        if g < config.num_generations - 1:
195	            logger.info("Generating synthetic data from G%d for next generation ...", g)
196	            model = AutoModelForCausalLM.from_pretrained(final_model_dir, torch_dtype=torch.bfloat16).to(device)
197	            gen_tok = AutoTokenizer.from_pretrained(config.model_name)
198	            if gen_tok.pad_token is None:
199	                gen_tok.pad_token = gen_tok.eos_token
200	
201	            generate_synthetic_data(
202	                model=model,
203	                tokenizer=gen_tok,
204	                num_tokens=config.tokens_per_generation,
205	                config=config,
206	                output_dir=config.synthetic_data_path(g),
207	            )
208	
209	            # save current gen token ids for KL computation in next gen
210	            synth_ds = prepare_synthetic_data(config.synthetic_data_path(g), config, gen_tok)
211	            prev_gen_token_ids = extract_token_ids(synth_ds, max_tokens=10_000_000)
212	
213	            del model
214	            torch.cuda.empty_cache()
215	
216	        # chain: next generation initialises from this generation's final model
217	        prev_model_dir = final_model_dir
218	
219	    # --- Summary ---
220	    summary = {
221	        "config": {k: v for k, v in config.__dict__.items() if not k.startswith("_")},
222	        "num_checkpoints_evaluated": len(all_results),
223	        "g0_baseline": g0_baseline,
224	        "generations": {},
225	    }
226	    for g in range(config.num_generations):
227	        gm = [m for m in all_results if m["generation"] == g]
228	        if gm:
229	            gen_summary = {
230	                "final_spectral_rank": gm[-1]["spectral_effective_rank"],
231	                "final_ppl": gm[-1]["perplexity"],
232	                "spectral_rank_trajectory": [m["spectral_effective_rank"] for m in gm],
233	                "ppl_trajectory": [m["perplexity"] for m in gm],
234	            }
235	            if "kl_unigram" in gm[-1]:
236	                gen_summary["final_kl_unigram"] = gm[-1]["kl_unigram"]
237	                gen_summary["final_kl_bigram"] = gm[-1].get("kl_bigram")
238	                gen_summary["final_kl_ci_95"] = [gm[-1].get("kl_ci_lower_95"), gm[-1].get("kl_ci_upper_95")]
239	            summary["generations"][f"G{g}"] = gen_summary
240	
241	    summary_path = config.summary_path()
242	    with open(summary_path, "w") as f:
243	        json.dump(summary, f, indent=2, default=str)
244	    logger.info("Summary written to %s", summary_path)
245	
246	    # --- MVP GO / NO-GO check (quantitative criteria from ROADMAP) ---
247	    if g0_baseline and len(summary["generations"]) >= 2:
248	        sigma = g0_baseline["spectral_rank_std"]
249	        g0_rank_mean = g0_baseline["spectral_rank_mean"]
250	        g0_ppl = g0_baseline["ppl_final"]
251	        rank_threshold = g0_rank_mean - sigma  # drop >= 1 sigma
252	
253	        # PPL significance: >= 2 pts absolute OR >= 5% relative
254	        ppl_abs_threshold = g0_ppl + 2.0
255	        ppl_rel_threshold = g0_ppl * 1.05
256	
257	        # Scan all post-G0 checkpoints for the leading indicator pattern:
258	        # find first checkpoint where rank drops >= 1 sigma below G0 mean
259	        # and check whether PPL has NOT yet risen significantly at that point
260	        first_rank_drop_idx = None
261	        first_ppl_rise_idx = None
262	
263	        post_g0 = [m for m in all_results if m["generation"] > 0]
264	        for i, m in enumerate(post_g0):
265	            if first_rank_drop_idx is None and m["spectral_effective_rank"] <= rank_threshold:
266	                first_rank_drop_idx = i
267	            if first_ppl_rise_idx is None and (m["perplexity"] >= ppl_abs_threshold or m["perplexity"] >= ppl_rel_threshold):
268	                first_ppl_rise_idx = i
269	
270	        # KL check (on final generation boundary)
271	        last_gen_metrics = [m for m in all_results if m["generation"] == config.num_generations - 1]
272	        kl_value = last_gen_metrics[-1].get("kl_unigram", 0) if last_gen_metrics else 0
273	        kl_ci = (last_gen_metrics[-1].get("kl_ci_lower_95", 0), last_gen_metrics[-1].get("kl_ci_upper_95", 0)) if last_gen_metrics else (0, 0)
274	
275	        spectral_leads = (first_rank_drop_idx is not None and
276	                          (first_ppl_rise_idx is None or first_rank_drop_idx < first_ppl_rise_idx))
277	        kl_above_threshold = kl_value > 0.1
278	
279	        logger.info("=" * 60)
280	        logger.info("MVP GO / NO-GO CHECK")
281	        logger.info("  G0 baseline: rank=%.1f +/- %.2f (1-sigma threshold=%.1f)  ppl=%.2f",
282	                     g0_rank_mean, sigma, rank_threshold, g0_ppl)
283	        logger.info("  PPL significance: >= %.2f (abs +2) OR >= %.2f (rel +5%%)",
284	                     ppl_abs_threshold, ppl_rel_threshold)
285	        logger.info("  First rank drop (>= 1 sigma): %s",
286	                     f"checkpoint {first_rank_drop_idx}" if first_rank_drop_idx is not None else "NOT DETECTED")
287	        logger.info("  First PPL rise (significant): %s",
288	                     f"checkpoint {first_ppl_rise_idx}" if first_ppl_rise_idx is not None else "NOT DETECTED")
289	        logger.info("  Spectral leads PPL: %s", spectral_leads)
290	        logger.info("  KL divergence: %.4f  (95%% CI: [%.4f, %.4f])  threshold 0.1: %s",
291	                     kl_value, kl_ci[0], kl_ci[1], "PASS" if kl_above_threshold else "FAIL")
292	
293	        if spectral_leads and kl_above_threshold:
294	            verdict = "GO — spectral rank is a leading indicator, KL confirms non-stationarity"
295	        elif first_rank_drop_idx is not None and first_ppl_rise_idx is not None and first_rank_drop_idx == first_ppl_rise_idx:
296	            verdict = "CONDITIONAL GO — spectral and PPL drop simultaneously, check granularity advantage"
297	        elif kl_value < 0.1 and (first_rank_drop_idx is not None or first_ppl_rise_idx is not None):
298	            verdict = "EXTEND — KL below threshold but collapse signals detected, add generation to accumulate KL"
299	        elif first_rank_drop_idx is None and first_ppl_rise_idx is not None:
300	            verdict = "KILL — PPL rose but spectral rank did not drop, indicator ineffective for autoregressive LM collapse"
301	        elif first_rank_drop_idx is None and first_ppl_rise_idx is None:
302	            verdict = "EXTEND — neither spectral rank nor PPL moved in 2 generations, add generation to trigger collapse"
303	        else:
304	            verdict = "INCONCLUSIVE — review trajectories manually"
305	
306	        logger.info("  VERDICT: %s", verdict)
307	        logger.info("=" * 60)
308	
309	        summary["mvp_check"] = {
310	            "g0_rank_mean": g0_rank_mean,
311	            "g0_rank_std": sigma,
312	            "rank_threshold_1sigma": rank_threshold,
313	            "ppl_threshold_abs": ppl_abs_threshold,
314	            "ppl_threshold_rel": ppl_rel_threshold,
315	            "first_rank_drop_checkpoint": first_rank_drop_idx,
316	            "first_ppl_rise_checkpoint": first_ppl_rise_idx,
317	            "spectral_leads": spectral_leads,
318	            "kl_unigram": kl_value,
319	            "kl_ci_95": list(kl_ci),
320	            "kl_above_0_1": kl_above_threshold,
321	            "verdict": verdict,
322	        }
323	        with open(summary_path, "w") as f:
324	            json.dump(summary, f, indent=2, default=str)
325	
326	    return all_results
327	
328	
329	def parse_args():
330	    parser = argparse.ArgumentParser(description="Collapse-aware mixing pilot experiment")
331	    parser.add_argument("--output_dir", type=str, default="./output")
332	    parser.add_argument("--num_generations", type=int, default=3)
333	    parser.add_argument("--tokens_per_generation", type=int, default=90_000_000)
334	    parser.add_argument("--checkpoint_interval_tokens", type=int, default=10_000_000)
335	    parser.add_argument("--holdout_size", type=int, default=5_000)
336	    parser.add_argument("--model_name", type=str, default="EleutherAI/pythia-1b")
337	    parser.add_argument("--per_device_batch_size", type=int, default=8)
338	    parser.add_argument("--gradient_accumulation_steps", type=int, default=4)
339	    parser.add_argument("--learning_rate", type=float, default=1e-5)
340	    parser.add_argument("--spectral_num_samples", type=int, default=50_000)
341	    parser.add_argument("--gen_temperature", type=float, default=1.0)
342	    parser.add_argument("--gen_top_p", type=float, default=0.95)
343	    parser.add_argument("--no_wandb", action="store_true")
344	    parser.add_argument("--seed", type=int, default=42)
345	    parser.add_argument("--real_dataset", type=str, default="wikitext")
346	    parser.add_argument("--metrics_gen_tokens", type=int, default=500_000)
347	    return parser.parse_args()
348	
349	
350	def main():
351	    args = parse_args()
352	    config = PilotConfig(
353	        output_dir=args.output_dir,
354	        num_generations=args.num_generations,
355	        tokens_per_generation=args.tokens_per_generation,
356	        checkpoint_interval_tokens=args.checkpoint_interval_tokens,
357	        model_name=args.model_name,
358	        per_device_batch_size=args.per_device_batch_size,
359	        gradient_accumulation_steps=args.gradient_accumulation_steps,
360	        learning_rate=args.learning_rate,
361	        spectral_num_samples=args.spectral_num_samples,
362	        gen_temperature=args.gen_temperature,
363	        gen_top_p=args.gen_top_p,
364	        use_wandb=not args.no_wandb,
365	        seed=args.seed,
366	        real_dataset=args.real_dataset,
367	        metrics_gen_tokens=args.metrics_gen_tokens,
368	        holdout_size=args.holdout_size,
369	    )
370	    run_pilot(config)
371	
372	
373	if __name__ == "__main__":
374	    main()
375	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_013HbNm4hmuyFcsh6bszPyyR",
  "session_id": "60ff85cb-037b-4c00-9e51-254478230283",
  "uuid": "5df7e3b6-c5b4-49f3-bbe9-03d47e2fb52b"
}
```

</details>

---

### System

_source line 14_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a431d4224180b832d",
  "tool_use_id": "toolu_013HbNm4hmuyFcsh6bszPyyR",
  "description": "Reading train.py",
  "usage": {
    "total_tokens": 34660,
    "tool_uses": 3,
    "duration_ms": 2408
  },
  "last_tool_name": "Read",
  "uuid": "919cf749-f77a-47d3-8fb4-3e72f1512b82",
  "session_id": "60ff85cb-037b-4c00-9e51-254478230283"
}
```

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Read · `toolu_01DztjnNXAvNq89rtVApfXV7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/code/train.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_013HbNm4hmuyFcsh6bszPyyR",
  "session_id": "60ff85cb-037b-4c00-9e51-254478230283",
  "uuid": "d8a9f349-da32-4e39-b3fc-b11081a850ce",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VzjWwhytZf7rmx8BkGpwja",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 34645,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 34645,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 16 · 2026-05-13T08:19:03.894Z_

<details><summary>↩ Tool result · `toolu_01DztjnNXAvNq89rtVApfXV7`</summary>

```text
1	"""Training loop for one generation using HuggingFace Trainer."""
2	
3	import os
4	import logging
5	from typing import List
6	
7	import torch
8	from transformers import (
9	    AutoModelForCausalLM,
10	    AutoTokenizer,
11	    Trainer,
12	    TrainingArguments,
13	    TrainerCallback,
14	)
15	
16	logger = logging.getLogger(__name__)
17	
18	
19	class CheckpointListCallback(TrainerCallback):
20	    """Records paths of saved checkpoints for downstream evaluation."""
21	
22	    def __init__(self):
23	        self.saved_checkpoints: List[str] = []
24	
25	    def on_save(self, args, state, control, **kwargs):
26	        ckpt_dir = os.path.join(args.output_dir, f"checkpoint-{state.global_step}")
27	        self.saved_checkpoints.append(ckpt_dir)
28	        logger.info("Checkpoint saved: %s (step %d)", ckpt_dir, state.global_step)
29	
30	
31	class EarlyStopOnHighLossCallback(TrainerCallback):
32	    """Stop training if loss exceeds threshold in first N steps."""
33	
34	    def __init__(self, threshold: float = 15.0, check_steps: int = 100, check_interval: int = 10):
35	        self.threshold = threshold
36	        self.check_steps = check_steps
37	        self.check_interval = check_interval
38	
39	    def on_log(self, args, state, control, logs=None, **kwargs):
40	        if state.global_step > self.check_steps:
41	            return
42	        if state.global_step % self.check_interval != 0:
43	            return
44	        loss = logs.get("loss") if logs else None
45	        if loss is not None and loss > self.threshold:
46	            logger.error(
47	                "EARLY STOP: loss=%.4f > threshold=%.1f at step %d. Training diverged.",
48	                loss, self.threshold, state.global_step,
49	            )
50	            control.should_training_stop = True
51	
52	
53	def train_generation(
54	    gen_idx: int,
55	    train_dataset,
56	    config,
57	    model_name_or_path: str | None = None,
58	) -> tuple[str, list[str]]:
59	    """Train one generation, return (final_checkpoint_path, all_checkpoint_paths).
60	
61	    Args:
62	        gen_idx: Generation index (0, 1, 2).
63	        train_dataset: PackedDataset for this generation.
64	        config: PilotConfig.
65	        model_name_or_path: Override model init (default: config.model_name).
66	
67	    Returns:
68	        (final_model_dir, checkpoint_paths) where final_model_dir is the
69	        directory containing the fully trained model.
70	    """
71	    model_name = model_name_or_path or config.model_name
72	    output_dir = os.path.join(config.gen_dir(gen_idx), "training")
73	    final_dir = os.path.join(config.gen_dir(gen_idx), "final_model")
74	
75	    logger.info("=== Generation %d: training from %s ===", gen_idx, model_name)
76	    logger.info("  Train sequences: %d | Max steps: %d | Save every %d steps",
77	                len(train_dataset), config.max_steps, config.save_steps)
78	
79	    tokenizer = AutoTokenizer.from_pretrained(model_name)
80	    if tokenizer.pad_token is None:
81	        tokenizer.pad_token = tokenizer.eos_token
82	
83	    model = AutoModelForCausalLM.from_pretrained(
84	        model_name,
85	        torch_dtype=torch.bfloat16,
86	        attn_implementation="sdpa",
87	    )
88	    if config.gradient_checkpointing:
89	        model.gradient_checkpointing_enable(gradient_checkpointing_kwargs={"use_reentrant": False})
90	
91	    ckpt_cb = CheckpointListCallback()
92	
93	    run_name = f"{config.wandb_run_prefix}_G{gen_idx}"
94	    training_args = TrainingArguments(
95	        output_dir=output_dir,
96	        max_steps=config.max_steps,
97	        per_device_train_batch_size=config.per_device_batch_size,
98	        gradient_accumulation_steps=config.gradient_accumulation_steps,
99	        learning_rate=config.learning_rate,
100	        warmup_ratio=config.warmup_ratio,
101	        weight_decay=config.weight_decay,
102	        bf16=config.bf16,
103	        logging_steps=50,
104	        save_steps=config.save_steps,
105	        save_total_limit=None,
106	        seed=config.seed,
107	        max_grad_norm=1.0,
108	        report_to="wandb" if config.use_wandb else "none",
109	        run_name=run_name,
110	        dataloader_num_workers=2,
111	        dataloader_pin_memory=True,
112	        remove_unused_columns=False,
113	    )
114	
115	    trainer = Trainer(
116	        model=model,
117	        args=training_args,
118	        train_dataset=train_dataset,
119	        callbacks=[ckpt_cb, EarlyStopOnHighLossCallback()],
120	    )
121	
122	    trainer.train()
123	
124	    # save final model (separate from checkpoints)
125	    os.makedirs(final_dir, exist_ok=True)
126	    trainer.save_model(final_dir)
127	    tokenizer.save_pretrained(final_dir)
128	    logger.info("Final model saved to %s", final_dir)
129	
130	    return final_dir, ckpt_cb.saved_checkpoints
131	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_013HbNm4hmuyFcsh6bszPyyR",
  "session_id": "60ff85cb-037b-4c00-9e51-254478230283",
  "uuid": "bbbad6f1-7bf5-4d8c-b56b-f4787ec1a9b5"
}
```

</details>

---

### System

_source line 17_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a431d4224180b832d",
  "tool_use_id": "toolu_013HbNm4hmuyFcsh6bszPyyR",
  "description": "Reading data_utils.py",
  "usage": {
    "total_tokens": 34663,
    "tool_uses": 4,
    "duration_ms": 2666
  },
  "last_tool_name": "Read",
  "uuid": "79f7bd11-94ee-4e25-b58c-e02420687dc3",
  "session_id": "60ff85cb-037b-4c00-9e51-254478230283"
}
```

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — Read · `toolu_01ARuSZELCmDA3crnWnGHu11`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/code/data_utils.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_013HbNm4hmuyFcsh6bszPyyR",
  "session_id": "60ff85cb-037b-4c00-9e51-254478230283",
  "uuid": "1328e261-3b9c-4138-a5ac-9e241fa7b1c5",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VzjWwhytZf7rmx8BkGpwja",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 34645,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 34645,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 19 · 2026-05-13T08:19:04.153Z_

<details><summary>↩ Tool result · `toolu_01ARuSZELCmDA3crnWnGHu11`</summary>

```text
1	"""Data loading, tokenization, and preprocessing for pilot experiments."""
2	
3	import os
4	import logging
5	from typing import Tuple, List, Optional
6	from itertools import chain
7	
8	import torch
9	from torch.utils.data import Dataset as TorchDataset, DataLoader
10	from datasets import load_dataset, Dataset, load_from_disk
11	from transformers import PreTrainedTokenizer
12	
13	logger = logging.getLogger(__name__)
14	
15	
16	class PackedDataset(TorchDataset):
17	    """Pre-tokenized, fixed-length sequences for causal LM training."""
18	
19	    def __init__(self, input_ids: List[List[int]]):
20	        self.input_ids = input_ids
21	
22	    def __len__(self):
23	        return len(self.input_ids)
24	
25	    def __getitem__(self, idx):
26	        ids = torch.tensor(self.input_ids[idx], dtype=torch.long)
27	        return {"input_ids": ids, "attention_mask": torch.ones_like(ids), "labels": ids.clone()}
28	
29	
30	def prepare_real_data(
31	    config, tokenizer: PreTrainedTokenizer
32	) -> Tuple[PackedDataset, PackedDataset]:
33	    """Load real data, tokenize, pack, split into train/holdout."""
34	    cache_path = os.path.join(config.output_dir, "real_data_cache")
35	
36	    if os.path.exists(cache_path):
37	        logger.info("Loading cached tokenized data from %s", cache_path)
38	        ds = load_from_disk(cache_path)
39	    else:
40	        num_train_seqs = config.tokens_per_generation // config.max_seq_length + 1
41	        num_total_seqs = num_train_seqs + config.holdout_size + 2000
42	
43	        dataset_config = getattr(config, "real_dataset_config", None)
44	        logger.info("Loading from %s (config=%s) ...", config.real_dataset, dataset_config)
45	        raw = load_dataset(
46	            config.real_dataset,
47	            dataset_config,
48	            split="train",
49	        )
50	
51	        logger.info("Tokenizing ...")
52	        tokenized = raw.map(
53	            lambda ex: tokenizer(ex["text"], truncation=False, add_special_tokens=False),
54	            batched=True,
55	            remove_columns=raw.column_names,
56	            num_proc=4,
57	            desc="Tokenizing",
58	        )
59	
60	        logger.info("Packing into %d-token sequences ...", config.max_seq_length)
61	
62	        def pack_fn(examples):
63	            flat = list(chain(*examples["input_ids"]))
64	            n = (len(flat) // config.max_seq_length) * config.max_seq_length
65	            return {
66	                "input_ids": [
67	                    flat[i : i + config.max_seq_length]
68	                    for i in range(0, n, config.max_seq_length)
69	                ]
70	            }
71	
72	        ds = tokenized.map(
73	            pack_fn, batched=True, remove_columns=tokenized.column_names, num_proc=1
74	        )
75	
76	        os.makedirs(cache_path, exist_ok=True)
77	        ds.save_to_disk(cache_path)
78	        logger.info("Cached %d packed sequences to %s", len(ds), cache_path)
79	
80	    num_train = config.tokens_per_generation // config.max_seq_length
81	    available = len(ds) - config.holdout_size
82	    if num_train > available:
83	        logger.warning(
84	            "Requested %d train seqs but only %d available (dataset=%d, holdout=%d). Clamping.",
85	            num_train, available, len(ds), config.holdout_size,
86	        )
87	        num_train = available
88	    num_holdout = min(config.holdout_size, len(ds) - num_train)
89	
90	    train_ids = ds.select(range(num_train))["input_ids"]
91	    holdout_ids = ds.select(range(num_train, num_train + num_holdout))["input_ids"]
92	
93	    logger.info(
94	        "Train: %d seqs (%.1fM tokens) | Holdout: %d seqs",
95	        len(train_ids),
96	        len(train_ids) * config.max_seq_length / 1e6,
97	        len(holdout_ids),
98	    )
99	    return PackedDataset(train_ids), PackedDataset(holdout_ids)
100	
101	
102	def prepare_synthetic_data(
103	    data_path: str, config, tokenizer: PreTrainedTokenizer
104	) -> PackedDataset:
105	    """Load generated synthetic data and wrap as PackedDataset."""
106	    logger.info("Loading synthetic data from %s", data_path)
107	    ds = load_from_disk(data_path)
108	    num_seqs = min(len(ds), config.tokens_per_generation // config.max_seq_length)
109	
110	    input_ids = []
111	    for i in range(num_seqs):
112	        seq = ds[i]["input_ids"]
113	        if len(seq) >= config.max_seq_length:
114	            input_ids.append(seq[: config.max_seq_length])
115	        else:
116	            # pad short sequences with eos_token_id
117	            pad_id = tokenizer.eos_token_id or 0
118	            input_ids.append(seq + [pad_id] * (config.max_seq_length - len(seq)))
119	
120	    logger.info("Loaded %d synthetic sequences", len(input_ids))
121	    return PackedDataset(input_ids)
122	
123	
124	def extract_token_ids(dataset: PackedDataset, max_tokens: Optional[int] = None) -> List[int]:
125	    """Flatten all sequences into a single token-id list for corpus-level metrics."""
126	    ids: List[int] = []
127	    for i in range(len(dataset)):
128	        ids.extend(dataset.input_ids[i])
129	        if max_tokens and len(ids) >= max_tokens:
130	            return ids[:max_tokens]
131	    return ids
132	
133	
134	def make_dataloader(dataset: PackedDataset, batch_size: int, shuffle: bool = False) -> DataLoader:
135	    return DataLoader(dataset, batch_size=batch_size, shuffle=shuffle, num_workers=2, pin_memory=True)
136	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_013HbNm4hmuyFcsh6bszPyyR",
  "session_id": "60ff85cb-037b-4c00-9e51-254478230283",
  "uuid": "fb01cb85-9ffa-4c9f-be20-1ce02e459e1b"
}
```

</details>

---

### System

_source line 20_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a431d4224180b832d",
  "tool_use_id": "toolu_013HbNm4hmuyFcsh6bszPyyR",
  "description": "Reading metrics.py",
  "usage": {
    "total_tokens": 34666,
    "tool_uses": 5,
    "duration_ms": 2840
  },
  "last_tool_name": "Read",
  "uuid": "623d9239-7d45-4c98-bb63-60b40d2f046d",
  "session_id": "60ff85cb-037b-4c00-9e51-254478230283"
}
```

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Read · `toolu_01FYdRHu1NXNWTN6pmQshM1r`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/code/metrics.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_013HbNm4hmuyFcsh6bszPyyR",
  "session_id": "60ff85cb-037b-4c00-9e51-254478230283",
  "uuid": "1c5c416a-4e10-40be-8cf3-dd36aaf94917",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VzjWwhytZf7rmx8BkGpwja",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 34645,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 34645,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 22 · 2026-05-13T08:19:04.326Z_

<details><summary>↩ Tool result · `toolu_01FYdRHu1NXNWTN6pmQshM1r`</summary>

```text
1	"""Collapse-detection metrics for the pilot experiment.
2	
3	Six metrics computed at each training checkpoint:
4	1. Spectral effective rank (core hypothesis)
5	2. Token-level prediction entropy variance
6	3. N-gram entropy (uni/bi/trigram)
7	4. Vocabulary coverage
8	5. Perplexity on held-out real data
9	6. Inter-generational KL divergence (unigram approximation)
10	"""
11	
12	import math
13	import logging
14	from collections import Counter
15	from typing import Dict, List, Optional
16	
17	import numpy as np
18	import torch
19	import torch.nn.functional as F
20	from torch.utils.data import DataLoader
21	from tqdm import tqdm
22	
23	logger = logging.getLogger(__name__)
24	
25	
26	# ---------------------------------------------------------------------------
27	# 1. Spectral effective rank
28	# ---------------------------------------------------------------------------
29	
30	def compute_spectral_effective_rank(
31	    model: torch.nn.Module,
32	    dataloader: DataLoader,
33	    num_samples: int = 50_000,
34	    device: str = "cuda",
35	) -> Dict[str, float]:
36	    """RankMe-style effective rank from final-layer hidden states.
37	
38	    Collects mean-pooled hidden states E (N x d), computes singular values,
39	    normalises to a distribution p, and returns exp(H(p)).
40	    """
41	    model.eval()
42	    hidden_list = []
43	    collected = 0
44	
45	    with torch.no_grad():
46	        for batch in tqdm(dataloader, desc="spectral-rank", leave=False):
47	            if collected >= num_samples:
48	                break
49	            input_ids = batch["input_ids"].to(device)
50	            attn_mask = batch["attention_mask"].to(device)
51	
52	            out = model(input_ids=input_ids, attention_mask=attn_mask, output_hidden_states=True)
53	            # final-layer hidden: (B, L, D)
54	            h = out.hidden_states[-1].float()
55	
56	            # mean-pool over sequence (mask-aware)
57	            mask = attn_mask.unsqueeze(-1).float()
58	            pooled = (h * mask).sum(1) / mask.sum(1).clamp(min=1)  # (B, D)
59	            hidden_list.append(pooled.cpu())
60	            collected += pooled.shape[0]
61	
62	    E = torch.cat(hidden_list, dim=0)[:num_samples]  # (N, D)
63	    sigma = torch.linalg.svdvals(E)                   # descending
64	
65	    # normalise to probability distribution
66	    sigma_pos = sigma[sigma > 0]
67	    p = sigma_pos / sigma_pos.sum()
68	    entropy = -(p * p.log()).sum().item()
69	    eff_rank = math.exp(entropy)
70	
71	    return {
72	        "spectral_effective_rank": eff_rank,
73	        "spectral_entropy": entropy,
74	        "top_singular_value": sigma[0].item(),
75	        "sigma_ratio_top_bottom": (sigma[0] / sigma_pos[-1]).item(),
76	        "spectral_num_samples": int(E.shape[0]),
77	    }
78	
79	
80	# ---------------------------------------------------------------------------
81	# 2. Token-level prediction entropy variance
82	# ---------------------------------------------------------------------------
83	
84	def compute_token_entropy_variance(
85	    model: torch.nn.Module,
86	    dataloader: DataLoader,
87	    num_samples: int = 10_000,
88	    device: str = "cuda",
89	) -> Dict[str, float]:
90	    """Per-token next-token entropy, report mean and variance across all tokens."""
91	    model.eval()
92	    entropies = []
93	    seen = 0
94	
95	    with torch.no_grad():
96	        for batch in tqdm(dataloader, desc="token-entropy", leave=False):
97	            if seen >= num_samples:
98	                break
99	            input_ids = batch["input_ids"].to(device)
100	            attn_mask = batch["attention_mask"].to(device)
101	
102	            logits = model(input_ids=input_ids, attention_mask=attn_mask).logits
103	            # shift: predict position t+1 from position t
104	            logits = logits[:, :-1, :]
105	            mask = attn_mask[:, 1:].bool()
106	
107	            log_p = F.log_softmax(logits, dim=-1)
108	            p = log_p.exp()
109	            ent = -(p * log_p).sum(dim=-1)  # (B, L-1)
110	
111	            for i in range(ent.shape[0]):
112	                entropies.append(ent[i][mask[i]].cpu())
113	            seen += input_ids.shape[0]
114	
115	    all_ent = torch.cat(entropies).float()
116	    return {
117	        "token_entropy_mean": all_ent.mean().item(),
118	        "token_entropy_var": all_ent.var().item(),
119	        "token_entropy_std": all_ent.std().item(),
120	        "token_entropy_num_tokens": int(all_ent.shape[0]),
121	    }
122	
123	
124	# ---------------------------------------------------------------------------
125	# 3. N-gram entropy
126	# ---------------------------------------------------------------------------
127	
128	def compute_ngram_entropy(token_ids: List[int], max_n: int = 3) -> Dict[str, float]:
129	    """Shannon entropy of unigram / bigram / trigram distributions."""
130	    label = {1: "unigram", 2: "bigram", 3: "trigram"}
131	    results: Dict[str, float] = {}
132	    for n in range(1, max_n + 1):
133	        counter: Counter = Counter()
134	        for i in range(len(token_ids) - n + 1):
135	            counter[tuple(token_ids[i : i + n])] += 1
136	        total = sum(counter.values())
137	        entropy = -sum((c / total) * math.log(c / total) for c in counter.values())
138	        results[f"{label[n]}_entropy"] = entropy
139	        results[f"{label[n]}_unique"] = len(counter)
140	    return results
141	
142	
143	# ---------------------------------------------------------------------------
144	# 4. Vocabulary coverage
145	# ---------------------------------------------------------------------------
146	
147	def compute_vocab_coverage(token_ids: List[int], vocab_size: int) -> Dict[str, float]:
148	    unique = len(set(token_ids))
149	    return {
150	        "vocab_coverage": unique / vocab_size,
151	        "unique_tokens": unique,
152	        "total_tokens": len(token_ids),
153	    }
154	
155	
156	# ---------------------------------------------------------------------------
157	# 5. Perplexity
158	# ---------------------------------------------------------------------------
159	
160	def compute_perplexity(
161	    model: torch.nn.Module,
162	    dataloader: DataLoader,
163	    num_samples: int = 5_000,
164	    device: str = "cuda",
165	) -> Dict[str, float]:
166	    """Standard perplexity on held-out data."""
167	    model.eval()
168	    total_loss = 0.0
169	    total_tokens = 0
170	    seen = 0
171	
172	    with torch.no_grad():
173	        for batch in tqdm(dataloader, desc="perplexity", leave=False):
174	            if seen >= num_samples:
175	                break
176	            input_ids = batch["input_ids"].to(device)
177	            attn_mask = batch["attention_mask"].to(device)
178	            labels = input_ids.clone()
179	            labels[attn_mask == 0] = -100
180	
181	            loss = model(input_ids=input_ids, attention_mask=attn_mask, labels=labels).loss
182	            n_tok = (labels[:, 1:] != -100).sum().item()
183	            total_loss += loss.item() * n_tok
184	            total_tokens += n_tok
185	            seen += input_ids.shape[0]
186	
187	    avg_loss = total_loss / max(total_tokens, 1)
188	    return {
189	        "perplexity": math.exp(avg_loss),
190	        "avg_loss": avg_loss,
191	        "ppl_num_tokens": total_tokens,
192	    }
193	
194	
195	# ---------------------------------------------------------------------------
196	# 6. Inter-generational KL divergence (full distribution report)
197	# ---------------------------------------------------------------------------
198	
199	def _unigram_dist(ids: np.ndarray, vocab_size: int, smoothing: float = 1e-8) -> np.ndarray:
200	    c = np.bincount(ids, minlength=vocab_size).astype(np.float64)
201	    c += smoothing
202	    return c / c.sum()
203	
204	
205	def _bigram_kl(ids_a: List[int], ids_b: List[int], smoothing: float = 1e-8) -> float:
206	    """KL(P_a || P_b) over bigram distributions (sparse, observed-support only)."""
207	    ca: Counter = Counter(zip(ids_a[:-1], ids_a[1:]))
208	    cb: Counter = Counter(zip(ids_b[:-1], ids_b[1:]))
209	    all_bg = set(ca) | set(cb)
210	    n_bg = len(all_bg)
211	    total_a = sum(ca.values()) + smoothing * n_bg
212	    total_b = sum(cb.values()) + smoothing * n_bg
213	    kl = 0.0
214	    for bg in all_bg:
215	        pa = (ca.get(bg, 0) + smoothing) / total_a
216	        pb = (cb.get(bg, 0) + smoothing) / total_b
217	        kl += pa * math.log(pa / pb)
218	    return kl
219	
220	
221	def compute_kl_divergence(
222	    ids_a: List[int],
223	    ids_b: List[int],
224	    vocab_size: int,
225	    smoothing: float = 1e-8,
226	    n_bootstrap: int = 1000,
227	    ci_level: float = 0.95,
228	) -> Dict[str, float]:
229	    """Full KL divergence report.
230	
231	    Returns unigram KL, bigram KL, frequency-binned KL contributions
232	    (high/mid/low-freq tokens), and bootstrap 95% CI on unigram KL.
233	    """
234	    arr_a = np.array(ids_a, dtype=np.int64)
235	    arr_b = np.array(ids_b, dtype=np.int64)
236	
237	    # --- Unigram KL ---
238	    p = _unigram_dist(arr_a, vocab_size, smoothing)
239	    q = _unigram_dist(arr_b, vocab_size, smoothing)
240	    per_token_kl = p * np.log(p / q)
241	    kl_unigram = float(per_token_kl.sum())
242	    kl_reverse = float((q * np.log(q / p)).sum())
243	    js = 0.5 * (kl_unigram + kl_reverse)
244	
245	    # --- Bigram KL ---
246	    kl_bigram = _bigram_kl(ids_a, ids_b, smoothing)
247	
248	    # --- Frequency-binned KL (based on reference corpus ids_a) ---
249	    counts_a = np.bincount(arr_a, minlength=vocab_size)
250	    ranked = np.argsort(-counts_a)
251	    n_nonzero = int((counts_a[ranked] > 0).sum())
252	    cut_high = max(1, n_nonzero // 100)         # top 1% of token types
253	    cut_mid = max(cut_high + 1, n_nonzero // 5)  # top 20%
254	
255	    kl_freq_high = float(per_token_kl[ranked[:cut_high]].sum())
256	    kl_freq_mid = float(per_token_kl[ranked[cut_high:cut_mid]].sum())
257	    kl_freq_low = float(per_token_kl[ranked[cut_mid:]].sum())
258	
259	    # --- Bootstrap CI on unigram KL ---
260	    rng = np.random.default_rng(42)
261	    sub_n = min(1_000_000, len(arr_a), len(arr_b))
262	    boot_kls = np.empty(n_bootstrap)
263	    for i in range(n_bootstrap):
264	        sa = rng.choice(arr_a, size=sub_n, replace=True)
265	        sb = rng.choice(arr_b, size=sub_n, replace=True)
266	        bp = np.bincount(sa, minlength=vocab_size).astype(np.float64) + smoothing
267	        bq = np.bincount(sb, minlength=vocab_size).astype(np.float64) + smoothing
268	        bp /= bp.sum()
269	        bq /= bq.sum()
270	        boot_kls[i] = (bp * np.log(bp / bq)).sum()
271	
272	    alpha = (1 - ci_level) / 2
273	    ci_lo = float(np.percentile(boot_kls, alpha * 100))
274	    ci_hi = float(np.percentile(boot_kls, (1 - alpha) * 100))
275	
276	    return {
277	        "kl_unigram": kl_unigram,
278	        "kl_unigram_reverse": kl_reverse,
279	        "js_divergence": js,
280	        "kl_bigram": kl_bigram,
281	        "kl_freq_high": kl_freq_high,
282	        "kl_freq_mid": kl_freq_mid,
283	        "kl_freq_low": kl_freq_low,
284	        "kl_ci_lower_95": ci_lo,
285	        "kl_ci_upper_95": ci_hi,
286	        "kl_bootstrap_mean": float(boot_kls.mean()),
287	        "kl_bootstrap_std": float(boot_kls.std()),
288	        "kl_freq_high_ntypes": int(cut_high),
289	        "kl_freq_mid_ntypes": int(cut_mid - cut_high),
290	        "kl_freq_low_ntypes": int(max(0, n_nonzero - cut_mid)),
291	        "kl_ci_note": "token-level i.i.d. bootstrap; CI may be anti-conservative due to sequential dependence",
292	    }
293	
294	
295	# ---------------------------------------------------------------------------
296	# Orchestrator: all metrics for one checkpoint
297	# ---------------------------------------------------------------------------
298	
299	def compute_checkpoint_metrics(
300	    model: torch.nn.Module,
301	    holdout_loader: DataLoader,
302	    gen_token_ids: List[int],
303	    prev_gen_token_ids: Optional[List[int]],
304	    vocab_size: int,
305	    config,
306	    device: str = "cuda",
307	) -> Dict[str, float]:
308	    """Compute all six metric groups for a single checkpoint."""
309	    results: Dict[str, float] = {}
310	
311	    logger.info("Computing spectral effective rank ...")
312	    results.update(compute_spectral_effective_rank(
313	        model, holdout_loader, num_samples=config.spectral_num_samples, device=device
314	    ))
315	
316	    logger.info("Computing token entropy variance ...")
317	    results.update(compute_token_entropy_variance(
318	        model, holdout_loader, num_samples=config.ppl_num_samples, device=device
319	    ))
320	
321	    logger.info("Computing perplexity ...")
322	    results.update(compute_perplexity(
323	        model, holdout_loader, num_samples=config.ppl_num_samples, device=device
324	    ))
325	
326	    logger.info("Computing n-gram entropy & vocab coverage ...")
327	    results.update(compute_ngram_entropy(gen_token_ids))
328	    results.update(compute_vocab_coverage(gen_token_ids, vocab_size))
329	
330	    if prev_gen_token_ids is not None:
331	        logger.info("Computing KL divergence (full report) ...")
332	        results.update(compute_kl_divergence(prev_gen_token_ids, gen_token_ids, vocab_size))
333	
334	    return results
335	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_013HbNm4hmuyFcsh6bszPyyR",
  "session_id": "60ff85cb-037b-4c00-9e51-254478230283",
  "uuid": "35735300-21d2-4e8d-a423-85acf7bb5d5c"
}
```

</details>

---

### System

_source line 23_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a431d4224180b832d",
  "tool_use_id": "toolu_013HbNm4hmuyFcsh6bszPyyR",
  "description": "Reading config.py",
  "usage": {
    "total_tokens": 34669,
    "tool_uses": 6,
    "duration_ms": 3180
  },
  "last_tool_name": "Read",
  "uuid": "dea03115-865e-496e-8974-30d7237de093",
  "session_id": "60ff85cb-037b-4c00-9e51-254478230283"
}
```

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — Read · `toolu_01GkUJbNceYkTZxbn5NGznDa`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/code/config.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_013HbNm4hmuyFcsh6bszPyyR",
  "session_id": "60ff85cb-037b-4c00-9e51-254478230283",
  "uuid": "1819f4fd-616a-4d82-815c-88fa1cf91ab5",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VzjWwhytZf7rmx8BkGpwja",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 34645,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 34645,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 25 · 2026-05-13T08:19:04.672Z_

<details><summary>↩ Tool result · `toolu_01GkUJbNceYkTZxbn5NGznDa`</summary>

```text
1	"""Pilot experiment configuration for collapse-aware-mixing MVP.
2	
3	Validates spectral effective rank as a leading indicator of model collapse
4	in iterative synthetic training (Pythia-1B, 3 generations x 500M tokens).
5	"""
6	
7	import os
8	from dataclasses import dataclass
9	
10	
11	@dataclass
12	class PilotConfig:
13	    # --- Model ---
14	    model_name: str = "EleutherAI/pythia-1b"
15	
16	    # --- Training ---
17	    num_generations: int = 3                    # G0 (real), G1 (synth from G0), G2 (synth from G1)
18	    tokens_per_generation: int = 100_000_000    # 100M tokens per generation
19	    checkpoint_interval_tokens: int = 10_000_000  # save + eval every 10M tokens
20	    max_seq_length: int = 2048
21	    per_device_batch_size: int = 8
22	    gradient_accumulation_steps: int = 4
23	    learning_rate: float = 2e-6
24	    warmup_ratio: float = 0.05
25	    weight_decay: float = 0.01
26	    seed: int = 42
27	    bf16: bool = True
28	    gradient_checkpointing: bool = True
29	
30	    # --- Synthetic data generation ---
31	    gen_temperature: float = 1.0
32	    gen_top_p: float = 0.95
33	    gen_batch_size: int = 32
34	    gen_max_new_tokens: int = 2048
35	
36	    # --- Metrics ---
37	    spectral_num_samples: int = 50_000          # sequences for spectral effective rank
38	    spectral_batch_size: int = 64
39	    metrics_gen_tokens: int = 500_000           # tokens to generate at each ckpt for n-gram/coverage
40	    ppl_num_samples: int = 5_000                # sequences for PPL evaluation
41	    ppl_batch_size: int = 16
42	
43	    # --- Data ---
44	    real_dataset: str = "wikitext"
45	    real_dataset_config: str = "wikitext-103-raw-v1"
46	    holdout_size: int = 10_000                  # sequences reserved for evaluation
47	
48	    # --- Paths ---
49	    output_dir: str = "./output"
50	
51	    # --- Logging ---
52	    use_wandb: bool = True
53	    wandb_project: str = "collapse-aware-mixing"
54	    wandb_run_prefix: str = "pilot"
55	
56	    # --- Derived properties ---
57	
58	    @property
59	    def effective_batch_size(self) -> int:
60	        return self.per_device_batch_size * self.gradient_accumulation_steps
61	
62	    @property
63	    def tokens_per_step(self) -> int:
64	        return self.max_seq_length * self.effective_batch_size
65	
66	    @property
67	    def save_steps(self) -> int:
68	        return self.checkpoint_interval_tokens // self.tokens_per_step
69	
70	    @property
71	    def max_steps(self) -> int:
72	        return self.tokens_per_generation // self.tokens_per_step
73	
74	    def gen_dir(self, g: int) -> str:
75	        return os.path.join(self.output_dir, f"G{g}")
76	
77	    def checkpoint_dir(self, g: int, step: int) -> str:
78	        return os.path.join(self.gen_dir(g), "training", f"checkpoint-{step}")
79	
80	    def synthetic_data_path(self, g: int) -> str:
81	        return os.path.join(self.gen_dir(g), "synthetic_data")
82	
83	    def metrics_path(self, g: int) -> str:
84	        return os.path.join(self.gen_dir(g), "metrics.jsonl")
85	
86	    def summary_path(self) -> str:
87	        return os.path.join(self.output_dir, "pilot_summary.json")
88	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_013HbNm4hmuyFcsh6bszPyyR",
  "session_id": "60ff85cb-037b-4c00-9e51-254478230283",
  "uuid": "5bb4a713-0797-4eab-97de-1064883b546b"
}
```

</details>

---

### System

_source line 26_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a431d4224180b832d",
  "tool_use_id": "toolu_013HbNm4hmuyFcsh6bszPyyR",
  "status": "completed",
  "output_file": "",
  "summary": "Read existing code files",
  "usage": {
    "total_tokens": 52142,
    "tool_uses": 6,
    "duration_ms": 19914
  },
  "uuid": "f4bdf1de-6ad5-4335-9acf-f0d6411f0e45",
  "session_id": "60ff85cb-037b-4c00-9e51-254478230283"
}
```

---

### Tool result

_source line 27 · 2026-05-13T08:19:21.396Z_

<details><summary>↩ Tool result · `toolu_013HbNm4hmuyFcsh6bszPyyR`</summary>

```text
Here are the complete contents of all six files:

## 1. controller.py

A discrete-time PI controller for adjusting the real data ratio (w_t) based on spectral effective rank signals. Key components:

- **ControllerConfig**: Dataclass with Kp=0.01, Ki=0.005, r_target=50.0, w_init=0.5, w_min=0.1, w_max=0.9
- **CollapseAwareController**: Implements PI control where:
  - `step(r_t)` takes current spectral rank and returns updated real data ratio
  - Uses proportional term on rank change (delta_r) and integral term on error
  - Maintains histories of rank and w values
  - Clamps w to [w_min, w_max]
  - `get_state()` returns controller internals
  - `reset()` resets to initial state

## 2. pilot_pipeline.py

End-to-end pipeline orchestrating G0 → synthetic → G1 → synthetic → G2 across 3 generations.

Main functions:
- **evaluate_checkpoints()**: Loads each checkpoint, generates 500K tokens for corpus metrics, computes all 6 metric groups
- **save_metrics()**: Appends metrics to JSONL files
- **run_pilot()**: Master pipeline that:
  - Loads real data (WikiText) once
  - Trains G0 on real data
  - Evaluates all checkpoints from each generation
  - Generates synthetic data from final model of each generation
  - Chains G1, G2 from previous generation models
  - Computes G0 baseline statistics (rank mean/std)
  - Implements MVP GO/NO-GO check with these criteria:
    - Spectral rank drops >= 1 sigma below G0 mean
    - PPL rises >= 2 pts absolute OR 5% relative
    - KL divergence threshold 0.1
  - Returns 6 verdicts: GO, CONDITIONAL GO, EXTEND, KILL, INCONCLUSIVE

## 3. train.py

HuggingFace Trainer-based training for one generation.

Key classes/functions:
- **CheckpointListCallback**: Records paths of saved checkpoints
- **EarlyStopOnHighLossCallback**: Stops if loss > threshold in first N steps
- **train_generation()**: Main training function
  - Args: gen_idx, train_dataset, config, model_name_or_path (optional)
  - Initializes model from model_name_or_path or config.model_name
  - Enables gradient checkpointing if config.gradient_checkpointing=True
  - Uses bfloat16, SDPA attention
  - Saves checkpoints every config.save_steps
  - Returns (final_dir, list_of_checkpoint_paths)

## 4. data_utils.py

Data loading and tokenization utilities.

Key classes/functions:
- **PackedDataset**: torch.Dataset wrapper over pre-tokenized fixed-length sequences
  - Returns dicts with "input_ids", "attention_mask", "labels"
- **prepare_real_data()**: Loads WikiText, tokenizes, packs into 2048-token sequences, splits train/holdout
  - Caches tokenized data
  - Returns (train_PackedDataset, holdout_PackedDataset)
- **prepare_synthetic_data()**: Loads pre-generated synthetic data from disk, wraps as PackedDataset
- **extract_token_ids()**: Flattens all sequences into single token-id list (with max_tokens limit)
- **make_dataloader()**: Creates DataLoader with batch_size, optional shuffle

## 5. metrics.py

Six metric groups computed at every checkpoint:

1. **compute_spectral_effective_rank()**: RankMe-style effective rank from final-layer hidden states
   - Mean-pools sequences, computes SVD, normalizes singular values to probability distribution
   - Returns eff_rank = exp(entropy), top_singular_value, sigma_ratio_top_bottom

2. **compute_token_entropy_variance()**: Per-token next-token entropy
   - Shifts logits, computes mean and variance of token entropies

3. **compute_ngram_entropy()**: Unigram/bigram/trigram Shannon entropy

4. **compute_vocab_coverage()**: Fraction of vocabulary used in token stream

5. **compute_perplexity()**: Standard perplexity on held-out data = exp(avg_loss)

6. **compute_kl_divergence()**: Full KL report comparing two token distributions
   - Unigram KL, reverse KL, JS divergence
   - Bigram KL
   - Frequency-binned KL (high/mid/low frequency tokens)
   - Bootstrap 95% CI on unigram KL (1000 resamples)

- **compute_checkpoint_metrics()**: Orchestrator that calls all six metric functions

## 6. config.py

PilotConfig dataclass with all hyperparameters:
- Model: "EleutherAI/pythia-1b"
- Training: 3 generations, 100M tokens/gen, 10M token checkpoint interval, batch_size=8, lr=2e-6
- Synthetic data generation: temperature=1.0, top_p=0.95
- Metrics: spectral_num_samples=50K, metrics_gen_tokens=500K, ppl_num_samples=5K
- Data: WikiText with 10K holdout sequences, max_seq_length=2048
- Computed properties: effective_batch_size, tokens_per_step, save_steps, max_steps
- Path methods: gen_dir(g), checkpoint_dir(g, step), synthetic_data_path(g), metrics_path(g), summary_path()
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "60ff85cb-037b-4c00-9e51-254478230283",
  "uuid": "16975427-9dbf-4b93-99aa-b9873466490f",
  "tool_use_result": {
    "status": "completed",
    "prompt": "Read the following files in full and report their complete contents:\n1. /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/code/controller.py\n2. /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/code/pilot_pipeline.py\n3. /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/code/train.py\n4. /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/code/data_utils.py\n5. /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/code/metrics.py\n6. /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/code/config.py\n\nReport each file's full content so I can understand the exact APIs, imports, and signatures.",
    "agentId": "a431d4224180b832d",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Here are the complete contents of all six files:\n\n## 1. controller.py\n\nA discrete-time PI controller for adjusting the real data ratio (w_t) based on spectral effective rank signals. Key components:\n\n- **ControllerConfig**: Dataclass with Kp=0.01, Ki=0.005, r_target=50.0, w_init=0.5, w_min=0.1, w_max=0.9\n- **CollapseAwareController**: Implements PI control where:\n  - `step(r_t)` takes current spectral rank and returns updated real data ratio\n  - Uses proportional term on rank change (delta_r) and integral term on error\n  - Maintains histories of rank and w values\n  - Clamps w to [w_min, w_max]\n  - `get_state()` returns controller internals\n  - `reset()` resets to initial state\n\n## 2. pilot_pipeline.py\n\nEnd-to-end pipeline orchestrating G0 → synthetic → G1 → synthetic → G2 across 3 generations.\n\nMain functions:\n- **evaluate_checkpoints()**: Loads each checkpoint, generates 500K tokens for corpus metrics, computes all 6 metric groups\n- **save_metrics()**: Appends metrics to JSONL files\n- **run_pilot()**: Master pipeline that:\n  - Loads real data (WikiText) once\n  - Trains G0 on real data\n  - Evaluates all checkpoints from each generation\n  - Generates synthetic data from final model of each generation\n  - Chains G1, G2 from previous generation models\n  - Computes G0 baseline statistics (rank mean/std)\n  - Implements MVP GO/NO-GO check with these criteria:\n    - Spectral rank drops >= 1 sigma below G0 mean\n    - PPL rises >= 2 pts absolute OR 5% relative\n    - KL divergence threshold 0.1\n  - Returns 6 verdicts: GO, CONDITIONAL GO, EXTEND, KILL, INCONCLUSIVE\n\n## 3. train.py\n\nHuggingFace Trainer-based training for one generation.\n\nKey classes/functions:\n- **CheckpointListCallback**: Records paths of saved checkpoints\n- **EarlyStopOnHighLossCallback**: Stops if loss > threshold in first N steps\n- **train_generation()**: Main training function\n  - Args: gen_idx, train_dataset, config, model_name_or_path (optional)\n  - Initializes model from model_name_or_path or config.model_name\n  - Enables gradient checkpointing if config.gradient_checkpointing=True\n  - Uses bfloat16, SDPA attention\n  - Saves checkpoints every config.save_steps\n  - Returns (final_dir, list_of_checkpoint_paths)\n\n## 4. data_utils.py\n\nData loading and tokenization utilities.\n\nKey classes/functions:\n- **PackedDataset**: torch.Dataset wrapper over pre-tokenized fixed-length sequences\n  - Returns dicts with \"input_ids\", \"attention_mask\", \"labels\"\n- **prepare_real_data()**: Loads WikiText, tokenizes, packs into 2048-token sequences, splits train/holdout\n  - Caches tokenized data\n  - Returns (train_PackedDataset, holdout_PackedDataset)\n- **prepare_synthetic_data()**: Loads pre-generated synthetic data from disk, wraps as PackedDataset\n- **extract_token_ids()**: Flattens all sequences into single token-id list (with max_tokens limit)\n- **make_dataloader()**: Creates DataLoader with batch_size, optional shuffle\n\n## 5. metrics.py\n\nSix metric groups computed at every checkpoint:\n\n1. **compute_spectral_effective_rank()**: RankMe-style effective rank from final-layer hidden states\n   - Mean-pools sequences, computes SVD, normalizes singular values to probability distribution\n   - Returns eff_rank = exp(entropy), top_singular_value, sigma_ratio_top_bottom\n\n2. **compute_token_entropy_variance()**: Per-token next-token entropy\n   - Shifts logits, computes mean and variance of token entropies\n\n3. **compute_ngram_entropy()**: Unigram/bigram/trigram Shannon entropy\n\n4. **compute_vocab_coverage()**: Fraction of vocabulary used in token stream\n\n5. **compute_perplexity()**: Standard perplexity on held-out data = exp(avg_loss)\n\n6. **compute_kl_divergence()**: Full KL report comparing two token distributions\n   - Unigram KL, reverse KL, JS divergence\n   - Bigram KL\n   - Frequency-binned KL (high/mid/low frequency tokens)\n   - Bootstrap 95% CI on unigram KL (1000 resamples)\n\n- **compute_checkpoint_metrics()**: Orchestrator that calls all six metric functions\n\n## 6. config.py\n\nPilotConfig dataclass with all hyperparameters:\n- Model: \"EleutherAI/pythia-1b\"\n- Training: 3 generations, 100M tokens/gen, 10M token checkpoint interval, batch_size=8, lr=2e-6\n- Synthetic data generation: temperature=1.0, top_p=0.95\n- Metrics: spectral_num_samples=50K, metrics_gen_tokens=500K, ppl_num_samples=5K\n- Data: WikiText with 10K holdout sequences, max_seq_length=2048\n- Computed properties: effective_batch_size, tokens_per_step, save_steps, max_steps\n- Path methods: gen_dir(g), checkpoint_dir(g, step), synthetic_data_path(g), metrics_path(g), summary_path()"
      }
    ],
    "totalDurationMs": 19917,
    "totalTokens": 53520,
    "totalToolUseCount": 6,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 17468,
      "cache_read_input_tokens": 34645,
      "output_tokens": 1400,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 17468
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 1400,
          "cache_read_input_tokens": 34645,
          "cache_creation_input_tokens": 17468,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 17468,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 6,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  }
}
```

</details>

---

### Assistant

_source line 28_

<details><summary>Logged reasoning block</summary>

```text
Now I have a good understanding of all the existing code. Let me read the actual source files to get the exact import paths, function signatures, and implementation details I need to be compatible with.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "60ff85cb-037b-4c00-9e51-254478230283",
  "uuid": "66571192-9a05-4b20-82bf-55b2ed8789ef",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MRKyqfG8N15atD2DVnEpFh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1781,
      "cache_read_input_tokens": 25088,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1781
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

_source line 29_

Let me read the exact source code for the key files to get precise signatures and imports.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "60ff85cb-037b-4c00-9e51-254478230283",
  "uuid": "6bc6f8e6-8729-476f-819c-1d57e194fd50",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MRKyqfG8N15atD2DVnEpFh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1781,
      "cache_read_input_tokens": 25088,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1781
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

_source line 30_

<details open><summary>🔧 Tool call — Read · `toolu_015U3BabHJG17Vd31TksKZoU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/code/controller.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "60ff85cb-037b-4c00-9e51-254478230283",
  "uuid": "06abc15e-8b41-4b17-9467-ba10c596924d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MRKyqfG8N15atD2DVnEpFh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1781,
      "cache_read_input_tokens": 25088,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1781
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

_source line 31 · 2026-05-13T08:19:26.570Z_

<details><summary>↩ Tool result · `toolu_015U3BabHJG17Vd31TksKZoU`</summary>

```text
1	"""Discrete-time PI controller for collapse-aware real/synthetic data mixing.
2	
3	Adjusts the real data ratio w_t based on spectral effective rank signal,
4	increasing real data when rank drops (collapse risk) and decreasing it
5	when rank recovers.
6	"""
7	
8	from dataclasses import dataclass
9	from typing import List, Optional
10	
11	
12	@dataclass
13	class ControllerConfig:
14	    Kp: float = 0.01
15	    Ki: float = 0.005
16	    r_target: float = 50.0
17	    w_init: float = 0.5
18	    w_min: float = 0.1
19	    w_max: float = 0.9
20	
21	
22	class CollapseAwareController:
23	    def __init__(self, config: ControllerConfig):
24	        self.config = config
25	        self._w: float = config.w_init
26	        self._r_prev: Optional[float] = None
27	        self._integral: float = 0.0
28	        self._proportional: float = 0.0
29	        self._r_history: List[float] = []
30	        self._w_history: List[float] = [config.w_init]
31	        self._step_count: int = 0
32	
33	    def step(self, r_t: float) -> float:
34	        """Given current spectral rank, return updated real data ratio w_t."""
35	        cfg = self.config
36	
37	        if self._r_prev is None:
38	            self._r_prev = r_t
39	            self._r_history.append(r_t)
40	            return self._w
41	
42	        error = r_t - cfg.r_target
43	        delta_r = r_t - self._r_prev
44	
45	        # rank drop (negative delta_r / negative error) → increase w
46	        self._proportional = -cfg.Kp * delta_r
47	        self._integral += -cfg.Ki * error
48	
49	        self._w = self._w + self._proportional + (-cfg.Ki * error)
50	
51	        self._w = max(cfg.w_min, min(cfg.w_max, self._w))
52	
53	        self._r_prev = r_t
54	        self._r_history.append(r_t)
55	        self._w_history.append(self._w)
56	        self._step_count += 1
57	
58	        return self._w
59	
60	    def get_state(self) -> dict:
61	        """Return controller internals."""
62	        return {
63	            "w": self._w,
64	            "proportional_term": self._proportional,
65	            "integral_term": self._integral,
66	            "r_history": list(self._r_history),
67	            "w_history": list(self._w_history),
68	            "step_count": self._step_count,
69	        }
70	
71	    def reset(self):
72	        """Reset controller state to initial."""
73	        self._w = self.config.w_init
74	        self._r_prev = None
75	        self._integral = 0.0
76	        self._proportional = 0.0
77	        self._r_history = []
78	        self._w_history = [self.config.w_init]
79	        self._step_count = 0
80	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "60ff85cb-037b-4c00-9e51-254478230283",
  "uuid": "733a7c9b-df08-4005-93c7-cd97e4c3c131",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/code/controller.py",
      "content": "\"\"\"Discrete-time PI controller for collapse-aware real/synthetic data mixing.\n\nAdjusts the real data ratio w_t based on spectral effective rank signal,\nincreasing real data when rank drops (collapse risk) and decreasing it\nwhen rank recovers.\n\"\"\"\n\nfrom dataclasses import dataclass\nfrom typing import List, Optional\n\n\n@dataclass\nclass ControllerConfig:\n    Kp: float = 0.01\n    Ki: float = 0.005\n    r_target: float = 50.0\n    w_init: float = 0.5\n    w_min: float = 0.1\n    w_max: float = 0.9\n\n\nclass CollapseAwareController:\n    def __init__(self, config: ControllerConfig):\n        self.config = config\n        self._w: float = config.w_init\n        self._r_prev: Optional[float] = None\n        self._integral: float = 0.0\n        self._proportional: float = 0.0\n        self._r_history: List[float] = []\n        self._w_history: List[float] = [config.w_init]\n        self._step_count: int = 0\n\n    def step(self, r_t: float) -> float:\n        \"\"\"Given current spectral rank, return updated real data ratio w_t.\"\"\"\n        cfg = self.config\n\n        if self._r_prev is None:\n            self._r_prev = r_t\n            self._r_history.append(r_t)\n            return self._w\n\n        error = r_t - cfg.r_target\n        delta_r = r_t - self._r_prev\n\n        # rank drop (negative delta_r / negative error) → increase w\n        self._proportional = -cfg.Kp * delta_r\n        self._integral += -cfg.Ki * error\n\n        self._w = self._w + self._proportional + (-cfg.Ki * error)\n\n        self._w = max(cfg.w_min, min(cfg.w_max, self._w))\n\n        self._r_prev = r_t\n        self._r_history.append(r_t)\n        self._w_history.append(self._w)\n        self._step_count += 1\n\n        return self._w\n\n    def get_state(self) -> dict:\n        \"\"\"Return controller internals.\"\"\"\n        return {\n            \"w\": self._w,\n            \"proportional_term\": self._proportional,\n            \"integral_term\": self._integral,\n            \"r_history\": list(self._r_history),\n            \"w_history\": list(self._w_history),\n            \"step_count\": self._step_count,\n        }\n\n    def reset(self):\n        \"\"\"Reset controller state to initial.\"\"\"\n        self._w = self.config.w_init\n        self._r_prev = None\n        self._integral = 0.0\n        self._proportional = 0.0\n        self._r_history = []\n        self._w_history = [self.config.w_init]\n        self._step_count = 0\n",
      "numLines": 80,
      "startLine": 1,
      "totalLines": 80
    }
  }
}
```

</details>

---

### Tool call

_source line 32_

<details open><summary>🔧 Tool call — Read · `toolu_01SRCBUH8Y11WGJKz2KK4ia1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/code/train.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "60ff85cb-037b-4c00-9e51-254478230283",
  "uuid": "2edf3ee3-0ee8-4f12-869d-6e5e3e62541d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MRKyqfG8N15atD2DVnEpFh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1781,
      "cache_read_input_tokens": 25088,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1781
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

_source line 33 · 2026-05-13T08:19:27.569Z_

<details><summary>↩ Tool result · `toolu_01SRCBUH8Y11WGJKz2KK4ia1`</summary>

```text
1	"""Training loop for one generation using HuggingFace Trainer."""
2	
3	import os
4	import logging
5	from typing import List
6	
7	import torch
8	from transformers import (
9	    AutoModelForCausalLM,
10	    AutoTokenizer,
11	    Trainer,
12	    TrainingArguments,
13	    TrainerCallback,
14	)
15	
16	logger = logging.getLogger(__name__)
17	
18	
19	class CheckpointListCallback(TrainerCallback):
20	    """Records paths of saved checkpoints for downstream evaluation."""
21	
22	    def __init__(self):
23	        self.saved_checkpoints: List[str] = []
24	
25	    def on_save(self, args, state, control, **kwargs):
26	        ckpt_dir = os.path.join(args.output_dir, f"checkpoint-{state.global_step}")
27	        self.saved_checkpoints.append(ckpt_dir)
28	        logger.info("Checkpoint saved: %s (step %d)", ckpt_dir, state.global_step)
29	
30	
31	class EarlyStopOnHighLossCallback(TrainerCallback):
32	    """Stop training if loss exceeds threshold in first N steps."""
33	
34	    def __init__(self, threshold: float = 15.0, check_steps: int = 100, check_interval: int = 10):
35	        self.threshold = threshold
36	        self.check_steps = check_steps
37	        self.check_interval = check_interval
38	
39	    def on_log(self, args, state, control, logs=None, **kwargs):
40	        if state.global_step > self.check_steps:
41	            return
42	        if state.global_step % self.check_interval != 0:
43	            return
44	        loss = logs.get("loss") if logs else None
45	        if loss is not None and loss > self.threshold:
46	            logger.error(
47	                "EARLY STOP: loss=%.4f > threshold=%.1f at step %d. Training diverged.",
48	                loss, self.threshold, state.global_step,
49	            )
50	            control.should_training_stop = True
51	
52	
53	def train_generation(
54	    gen_idx: int,
55	    train_dataset,
56	    config,
57	    model_name_or_path: str | None = None,
58	) -> tuple[str, list[str]]:
59	    """Train one generation, return (final_checkpoint_path, all_checkpoint_paths).
60	
61	    Args:
62	        gen_idx: Generation index (0, 1, 2).
63	        train_dataset: PackedDataset for this generation.
64	        config: PilotConfig.
65	        model_name_or_path: Override model init (default: config.model_name).
66	
67	    Returns:
68	        (final_model_dir, checkpoint_paths) where final_model_dir is the
69	        directory containing the fully trained model.
70	    """
71	    model_name = model_name_or_path or config.model_name
72	    output_dir = os.path.join(config.gen_dir(gen_idx), "training")
73	    final_dir = os.path.join(config.gen_dir(gen_idx), "final_model")
74	
75	    logger.info("=== Generation %d: training from %s ===", gen_idx, model_name)
76	    logger.info("  Train sequences: %d | Max steps: %d | Save every %d steps",
77	                len(train_dataset), config.max_steps, config.save_steps)
78	
79	    tokenizer = AutoTokenizer.from_pretrained(model_name)
80	    if tokenizer.pad_token is None:
81	        tokenizer.pad_token = tokenizer.eos_token
82	
83	    model = AutoModelForCausalLM.from_pretrained(
84	        model_name,
85	        torch_dtype=torch.bfloat16,
86	        attn_implementation="sdpa",
87	    )
88	    if config.gradient_checkpointing:
89	        model.gradient_checkpointing_enable(gradient_checkpointing_kwargs={"use_reentrant": False})
90	
91	    ckpt_cb = CheckpointListCallback()
92	
93	    run_name = f"{config.wandb_run_prefix}_G{gen_idx}"
94	    training_args = TrainingArguments(
95	        output_dir=output_dir,
96	        max_steps=config.max_steps,
97	        per_device_train_batch_size=config.per_device_batch_size,
98	        gradient_accumulation_steps=config.gradient_accumulation_steps,
99	        learning_rate=config.learning_rate,
100	        warmup_ratio=config.warmup_ratio,
101	        weight_decay=config.weight_decay,
102	        bf16=config.bf16,
103	        logging_steps=50,
104	        save_steps=config.save_steps,
105	        save_total_limit=None,
106	        seed=config.seed,
107	        max_grad_norm=1.0,
108	        report_to="wandb" if config.use_wandb else "none",
109	        run_name=run_name,
110	        dataloader_num_workers=2,
111	        dataloader_pin_memory=True,
112	        remove_unused_columns=False,
113	    )
114	
115	    trainer = Trainer(
116	        model=model,
117	        args=training_args,
118	        train_dataset=train_dataset,
119	        callbacks=[ckpt_cb, EarlyStopOnHighLossCallback()],
120	    )
121	
122	    trainer.train()
123	
124	    # save final model (separate from checkpoints)
125	    os.makedirs(final_dir, exist_ok=True)
126	    trainer.save_model(final_dir)
127	    tokenizer.save_pretrained(final_dir)
128	    logger.info("Final model saved to %s", final_dir)
129	
130	    return final_dir, ckpt_cb.saved_checkpoints
131	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "60ff85cb-037b-4c00-9e51-254478230283",
  "uuid": "3c6c0b26-adef-47e8-b1f8-0ec8b70c3709",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/code/train.py",
      "content": "\"\"\"Training loop for one generation using HuggingFace Trainer.\"\"\"\n\nimport os\nimport logging\nfrom typing import List\n\nimport torch\nfrom transformers import (\n    AutoModelForCausalLM,\n    AutoTokenizer,\n    Trainer,\n    TrainingArguments,\n    TrainerCallback,\n)\n\nlogger = logging.getLogger(__name__)\n\n\nclass CheckpointListCallback(TrainerCallback):\n    \"\"\"Records paths of saved checkpoints for downstream evaluation.\"\"\"\n\n    def __init__(self):\n        self.saved_checkpoints: List[str] = []\n\n    def on_save(self, args, state, control, **kwargs):\n        ckpt_dir = os.path.join(args.output_dir, f\"checkpoint-{state.global_step}\")\n        self.saved_checkpoints.append(ckpt_dir)\n        logger.info(\"Checkpoint saved: %s (step %d)\", ckpt_dir, state.global_step)\n\n\nclass EarlyStopOnHighLossCallback(TrainerCallback):\n    \"\"\"Stop training if loss exceeds threshold in first N steps.\"\"\"\n\n    def __init__(self, threshold: float = 15.0, check_steps: int = 100, check_interval: int = 10):\n        self.threshold = threshold\n        self.check_steps = check_steps\n        self.check_interval = check_interval\n\n    def on_log(self, args, state, control, logs=None, **kwargs):\n        if state.global_step > self.check_steps:\n            return\n        if state.global_step % self.check_interval != 0:\n            return\n        loss = logs.get(\"loss\") if logs else None\n        if loss is not None and loss > self.threshold:\n            logger.error(\n                \"EARLY STOP: loss=%.4f > threshold=%.1f at step %d. Training diverged.\",\n                loss, self.threshold, state.global_step,\n            )\n            control.should_training_stop = True\n\n\ndef train_generation(\n    gen_idx: int,\n    train_dataset,\n    config,\n    model_name_or_path: str | None = None,\n) -> tuple[str, list[str]]:\n    \"\"\"Train one generation, return (final_checkpoint_path, all_checkpoint_paths).\n\n    Args:\n        gen_idx: Generation index (0, 1, 2).\n        train_dataset: PackedDataset for this generation.\n        config: PilotConfig.\n        model_name_or_path: Override model init (default: config.model_name).\n\n    Returns:\n        (final_model_dir, checkpoint_paths) where final_model_dir is the\n        directory containing the fully trained model.\n    \"\"\"\n    model_name = model_name_or_path or config.model_name\n    output_dir = os.path.join(config.gen_dir(gen_idx), \"training\")\n    final_dir = os.path.join(config.gen_dir(gen_idx), \"final_model\")\n\n    logger.info(\"=== Generation %d: training from %s ===\", gen_idx, model_name)\n    logger.info(\"  Train sequences: %d | Max steps: %d | Save every %d steps\",\n                len(train_dataset), config.max_steps, config.save_steps)\n\n    tokenizer = AutoTokenizer.from_pretrained(model_name)\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n\n    model = AutoModelForCausalLM.from_pretrained(\n        model_name,\n        torch_dtype=torch.bfloat16,\n        attn_implementation=\"sdpa\",\n    )\n    if config.gradient_checkpointing:\n        model.gradient_checkpointing_enable(gradient_checkpointing_kwargs={\"use_reentrant\": False})\n\n    ckpt_cb = CheckpointListCallback()\n\n    run_name = f\"{config.wandb_run_prefix}_G{gen_idx}\"\n    training_args = TrainingArguments(\n        output_dir=output_dir,\n        max_steps=config.max_steps,\n        per_device_train_batch_size=config.per_device_batch_size,\n        gradient_accumulation_steps=config.gradient_accumulation_steps,\n        learning_rate=config.learning_rate,\n        warmup_ratio=config.warmup_ratio,\n        weight_decay=config.weight_decay,\n        bf16=config.bf16,\n        logging_steps=50,\n        save_steps=config.save_steps,\n        save_total_limit=None,\n        seed=config.seed,\n        max_grad_norm=1.0,\n        report_to=\"wandb\" if config.use_wandb else \"none\",\n        run_name=run_name,\n        dataloader_num_workers=2,\n        dataloader_pin_memory=True,\n        remove_unused_columns=False,\n    )\n\n    trainer = Trainer(\n        model=model,\n        args=training_args,\n        train_dataset=train_dataset,\n        callbacks=[ckpt_cb, EarlyStopOnHighLossCallback()],\n    )\n\n    trainer.train()\n\n    # save final model (separate from checkpoints)\n    os.makedirs(final_dir, exist_ok=True)\n    trainer.save_model(final_dir)\n    tokenizer.save_pretrained(final_dir)\n    logger.info(\"Final model saved to %s\", final_dir)\n\n    return final_dir, ckpt_cb.saved_checkpoints\n",
      "numLines": 131,
      "startLine": 1,
      "totalLines": 131
    }
  }
}
```

</details>

---

### Tool call

_source line 34_

<details open><summary>🔧 Tool call — Read · `toolu_01SM4vDUzRhYtziVTVkwc7Uz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/code/data_utils.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "60ff85cb-037b-4c00-9e51-254478230283",
  "uuid": "6ff28431-0e7e-4e96-aec3-ed3e9fae0fe9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MRKyqfG8N15atD2DVnEpFh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1781,
      "cache_read_input_tokens": 25088,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1781
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

_source line 35 · 2026-05-13T08:19:27.897Z_

<details><summary>↩ Tool result · `toolu_01SM4vDUzRhYtziVTVkwc7Uz`</summary>

```text
1	"""Data loading, tokenization, and preprocessing for pilot experiments."""
2	
3	import os
4	import logging
5	from typing import Tuple, List, Optional
6	from itertools import chain
7	
8	import torch
9	from torch.utils.data import Dataset as TorchDataset, DataLoader
10	from datasets import load_dataset, Dataset, load_from_disk
11	from transformers import PreTrainedTokenizer
12	
13	logger = logging.getLogger(__name__)
14	
15	
16	class PackedDataset(TorchDataset):
17	    """Pre-tokenized, fixed-length sequences for causal LM training."""
18	
19	    def __init__(self, input_ids: List[List[int]]):
20	        self.input_ids = input_ids
21	
22	    def __len__(self):
23	        return len(self.input_ids)
24	
25	    def __getitem__(self, idx):
26	        ids = torch.tensor(self.input_ids[idx], dtype=torch.long)
27	        return {"input_ids": ids, "attention_mask": torch.ones_like(ids), "labels": ids.clone()}
28	
29	
30	def prepare_real_data(
31	    config, tokenizer: PreTrainedTokenizer
32	) -> Tuple[PackedDataset, PackedDataset]:
33	    """Load real data, tokenize, pack, split into train/holdout."""
34	    cache_path = os.path.join(config.output_dir, "real_data_cache")
35	
36	    if os.path.exists(cache_path):
37	        logger.info("Loading cached tokenized data from %s", cache_path)
38	        ds = load_from_disk(cache_path)
39	    else:
40	        num_train_seqs = config.tokens_per_generation // config.max_seq_length + 1
41	        num_total_seqs = num_train_seqs + config.holdout_size + 2000
42	
43	        dataset_config = getattr(config, "real_dataset_config", None)
44	        logger.info("Loading from %s (config=%s) ...", config.real_dataset, dataset_config)
45	        raw = load_dataset(
46	            config.real_dataset,
47	            dataset_config,
48	            split="train",
49	        )
50	
51	        logger.info("Tokenizing ...")
52	        tokenized = raw.map(
53	            lambda ex: tokenizer(ex["text"], truncation=False, add_special_tokens=False),
54	            batched=True,
55	            remove_columns=raw.column_names,
56	            num_proc=4,
57	            desc="Tokenizing",
58	        )
59	
60	        logger.info("Packing into %d-token sequences ...", config.max_seq_length)
61	
62	        def pack_fn(examples):
63	            flat = list(chain(*examples["input_ids"]))
64	            n = (len(flat) // config.max_seq_length) * config.max_seq_length
65	            return {
66	                "input_ids": [
67	                    flat[i : i + config.max_seq_length]
68	                    for i in range(0, n, config.max_seq_length)
69	                ]
70	            }
71	
72	        ds = tokenized.map(
73	            pack_fn, batched=True, remove_columns=tokenized.column_names, num_proc=1
74	        )
75	
76	        os.makedirs(cache_path, exist_ok=True)
77	        ds.save_to_disk(cache_path)
78	        logger.info("Cached %d packed sequences to %s", len(ds), cache_path)
79	
80	    num_train = config.tokens_per_generation // config.max_seq_length
81	    available = len(ds) - config.holdout_size
82	    if num_train > available:
83	        logger.warning(
84	            "Requested %d train seqs but only %d available (dataset=%d, holdout=%d). Clamping.",
85	            num_train, available, len(ds), config.holdout_size,
86	        )
87	        num_train = available
88	    num_holdout = min(config.holdout_size, len(ds) - num_train)
89	
90	    train_ids = ds.select(range(num_train))["input_ids"]
91	    holdout_ids = ds.select(range(num_train, num_train + num_holdout))["input_ids"]
92	
93	    logger.info(
94	        "Train: %d seqs (%.1fM tokens) | Holdout: %d seqs",
95	        len(train_ids),
96	        len(train_ids) * config.max_seq_length / 1e6,
97	        len(holdout_ids),
98	    )
99	    return PackedDataset(train_ids), PackedDataset(holdout_ids)
100	
101	
102	def prepare_synthetic_data(
103	    data_path: str, config, tokenizer: PreTrainedTokenizer
104	) -> PackedDataset:
105	    """Load generated synthetic data and wrap as PackedDataset."""
106	    logger.info("Loading synthetic data from %s", data_path)
107	    ds = load_from_disk(data_path)
108	    num_seqs = min(len(ds), config.tokens_per_generation // config.max_seq_length)
109	
110	    input_ids = []
111	    for i in range(num_seqs):
112	        seq = ds[i]["input_ids"]
113	        if len(seq) >= config.max_seq_length:
114	            input_ids.append(seq[: config.max_seq_length])
115	        else:
116	            # pad short sequences with eos_token_id
117	            pad_id = tokenizer.eos_token_id or 0
118	            input_ids.append(seq + [pad_id] * (config.max_seq_length - len(seq)))
119	
120	    logger.info("Loaded %d synthetic sequences", len(input_ids))
121	    return PackedDataset(input_ids)
122	
123	
124	def extract_token_ids(dataset: PackedDataset, max_tokens: Optional[int] = None) -> List[int]:
125	    """Flatten all sequences into a single token-id list for corpus-level metrics."""
126	    ids: List[int] = []
127	    for i in range(len(dataset)):
128	        ids.extend(dataset.input_ids[i])
129	        if max_tokens and len(ids) >= max_tokens:
130	            return ids[:max_tokens]
131	    return ids
132	
133	
134	def make_dataloader(dataset: PackedDataset, batch_size: int, shuffle: bool = False) -> DataLoader:
135	    return DataLoader(dataset, batch_size=batch_size, shuffle=shuffle, num_workers=2, pin_memory=True)
136	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "60ff85cb-037b-4c00-9e51-254478230283",
  "uuid": "0b910864-4507-470e-a0dd-e5d16b6b6075",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/code/data_utils.py",
      "content": "\"\"\"Data loading, tokenization, and preprocessing for pilot experiments.\"\"\"\n\nimport os\nimport logging\nfrom typing import Tuple, List, Optional\nfrom itertools import chain\n\nimport torch\nfrom torch.utils.data import Dataset as TorchDataset, DataLoader\nfrom datasets import load_dataset, Dataset, load_from_disk\nfrom transformers import PreTrainedTokenizer\n\nlogger = logging.getLogger(__name__)\n\n\nclass PackedDataset(TorchDataset):\n    \"\"\"Pre-tokenized, fixed-length sequences for causal LM training.\"\"\"\n\n    def __init__(self, input_ids: List[List[int]]):\n        self.input_ids = input_ids\n\n    def __len__(self):\n        return len(self.input_ids)\n\n    def __getitem__(self, idx):\n        ids = torch.tensor(self.input_ids[idx], dtype=torch.long)\n        return {\"input_ids\": ids, \"attention_mask\": torch.ones_like(ids), \"labels\": ids.clone()}\n\n\ndef prepare_real_data(\n    config, tokenizer: PreTrainedTokenizer\n) -> Tuple[PackedDataset, PackedDataset]:\n    \"\"\"Load real data, tokenize, pack, split into train/holdout.\"\"\"\n    cache_path = os.path.join(config.output_dir, \"real_data_cache\")\n\n    if os.path.exists(cache_path):\n        logger.info(\"Loading cached tokenized data from %s\", cache_path)\n        ds = load_from_disk(cache_path)\n    else:\n        num_train_seqs = config.tokens_per_generation // config.max_seq_length + 1\n        num_total_seqs = num_train_seqs + config.holdout_size + 2000\n\n        dataset_config = getattr(config, \"real_dataset_config\", None)\n        logger.info(\"Loading from %s (config=%s) ...\", config.real_dataset, dataset_config)\n        raw = load_dataset(\n            config.real_dataset,\n            dataset_config,\n            split=\"train\",\n        )\n\n        logger.info(\"Tokenizing ...\")\n        tokenized = raw.map(\n            lambda ex: tokenizer(ex[\"text\"], truncation=False, add_special_tokens=False),\n            batched=True,\n            remove_columns=raw.column_names,\n            num_proc=4,\n            desc=\"Tokenizing\",\n        )\n\n        logger.info(\"Packing into %d-token sequences ...\", config.max_seq_length)\n\n        def pack_fn(examples):\n            flat = list(chain(*examples[\"input_ids\"]))\n            n = (len(flat) // config.max_seq_length) * config.max_seq_length\n            return {\n                \"input_ids\": [\n                    flat[i : i + config.max_seq_length]\n                    for i in range(0, n, config.max_seq_length)\n                ]\n            }\n\n        ds = tokenized.map(\n            pack_fn, batched=True, remove_columns=tokenized.column_names, num_proc=1\n        )\n\n        os.makedirs(cache_path, exist_ok=True)\n        ds.save_to_disk(cache_path)\n        logger.info(\"Cached %d packed sequences to %s\", len(ds), cache_path)\n\n    num_train = config.tokens_per_generation // config.max_seq_length\n    available = len(ds) - config.holdout_size\n    if num_train > available:\n        logger.warning(\n            \"Requested %d train seqs but only %d available (dataset=%d, holdout=%d). Clamping.\",\n            num_train, available, len(ds), config.holdout_size,\n        )\n        num_train = available\n    num_holdout = min(config.holdout_size, len(ds) - num_train)\n\n    train_ids = ds.select(range(num_train))[\"input_ids\"]\n    holdout_ids = ds.select(range(num_train, num_train + num_holdout))[\"input_ids\"]\n\n    logger.info(\n        \"Train: %d seqs (%.1fM tokens) | Holdout: %d seqs\",\n        len(train_ids),\n        len(train_ids) * config.max_seq_length / 1e6,\n        len(holdout_ids),\n    )\n    return PackedDataset(train_ids), PackedDataset(holdout_ids)\n\n\ndef prepare_synthetic_data(\n    data_path: str, config, tokenizer: PreTrainedTokenizer\n) -> PackedDataset:\n    \"\"\"Load generated synthetic data and wrap as PackedDataset.\"\"\"\n    logger.info(\"Loading synthetic data from %s\", data_path)\n    ds = load_from_disk(data_path)\n    num_seqs = min(len(ds), config.tokens_per_generation // config.max_seq_length)\n\n    input_ids = []\n    for i in range(num_seqs):\n        seq = ds[i][\"input_ids\"]\n        if len(seq) >= config.max_seq_length:\n            input_ids.append(seq[: config.max_seq_length])\n        else:\n            # pad short sequences with eos_token_id\n            pad_id = tokenizer.eos_token_id or 0\n            input_ids.append(seq + [pad_id] * (config.max_seq_length - len(seq)))\n\n    logger.info(\"Loaded %d synthetic sequences\", len(input_ids))\n    return PackedDataset(input_ids)\n\n\ndef extract_token_ids(dataset: PackedDataset, max_tokens: Optional[int] = None) -> List[int]:\n    \"\"\"Flatten all sequences into a single token-id list for corpus-level metrics.\"\"\"\n    ids: List[int] = []\n    for i in range(len(dataset)):\n        ids.extend(dataset.input_ids[i])\n        if max_tokens and len(ids) >= max_tokens:\n            return ids[:max_tokens]\n    return ids\n\n\ndef make_dataloader(dataset: PackedDataset, batch_size: int, shuffle: bool = False) -> DataLoader:\n    return DataLoader(dataset, batch_size=batch_size, shuffle=shuffle, num_workers=2, pin_memory=True)\n",
      "numLines": 136,
      "startLine": 1,
      "totalLines": 136
    }
  }
}
```

</details>

---

### Tool call

_source line 36_

<details open><summary>🔧 Tool call — Read · `toolu_013S4Kdiz69HVQfMUAngzsP4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/code/metrics.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "60ff85cb-037b-4c00-9e51-254478230283",
  "uuid": "ec94604d-e872-428f-b51f-48310459758b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MRKyqfG8N15atD2DVnEpFh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1781,
      "cache_read_input_tokens": 25088,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1781
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

_source line 37 · 2026-05-13T08:19:28.382Z_

<details><summary>↩ Tool result · `toolu_013S4Kdiz69HVQfMUAngzsP4`</summary>

```text
1	"""Collapse-detection metrics for the pilot experiment.
2	
3	Six metrics computed at each training checkpoint:
4	1. Spectral effective rank (core hypothesis)
5	2. Token-level prediction entropy variance
6	3. N-gram entropy (uni/bi/trigram)
7	4. Vocabulary coverage
8	5. Perplexity on held-out real data
9	6. Inter-generational KL divergence (unigram approximation)
10	"""
11	
12	import math
13	import logging
14	from collections import Counter
15	from typing import Dict, List, Optional
16	
17	import numpy as np
18	import torch
19	import torch.nn.functional as F
20	from torch.utils.data import DataLoader
21	from tqdm import tqdm
22	
23	logger = logging.getLogger(__name__)
24	
25	
26	# ---------------------------------------------------------------------------
27	# 1. Spectral effective rank
28	# ---------------------------------------------------------------------------
29	
30	def compute_spectral_effective_rank(
31	    model: torch.nn.Module,
32	    dataloader: DataLoader,
33	    num_samples: int = 50_000,
34	    device: str = "cuda",
35	) -> Dict[str, float]:
36	    """RankMe-style effective rank from final-layer hidden states.
37	
38	    Collects mean-pooled hidden states E (N x d), computes singular values,
39	    normalises to a distribution p, and returns exp(H(p)).
40	    """
41	    model.eval()
42	    hidden_list = []
43	    collected = 0
44	
45	    with torch.no_grad():
46	        for batch in tqdm(dataloader, desc="spectral-rank", leave=False):
47	            if collected >= num_samples:
48	                break
49	            input_ids = batch["input_ids"].to(device)
50	            attn_mask = batch["attention_mask"].to(device)
51	
52	            out = model(input_ids=input_ids, attention_mask=attn_mask, output_hidden_states=True)
53	            # final-layer hidden: (B, L, D)
54	            h = out.hidden_states[-1].float()
55	
56	            # mean-pool over sequence (mask-aware)
57	            mask = attn_mask.unsqueeze(-1).float()
58	            pooled = (h * mask).sum(1) / mask.sum(1).clamp(min=1)  # (B, D)
59	            hidden_list.append(pooled.cpu())
60	            collected += pooled.shape[0]
61	
62	    E = torch.cat(hidden_list, dim=0)[:num_samples]  # (N, D)
63	    sigma = torch.linalg.svdvals(E)                   # descending
64	
65	    # normalise to probability distribution
66	    sigma_pos = sigma[sigma > 0]
67	    p = sigma_pos / sigma_pos.sum()
68	    entropy = -(p * p.log()).sum().item()
69	    eff_rank = math.exp(entropy)
70	
71	    return {
72	        "spectral_effective_rank": eff_rank,
73	        "spectral_entropy": entropy,
74	        "top_singular_value": sigma[0].item(),
75	        "sigma_ratio_top_bottom": (sigma[0] / sigma_pos[-1]).item(),
76	        "spectral_num_samples": int(E.shape[0]),
77	    }
78	
79	
80	# ---------------------------------------------------------------------------
81	# 2. Token-level prediction entropy variance
82	# ---------------------------------------------------------------------------
83	
84	def compute_token_entropy_variance(
85	    model: torch.nn.Module,
86	    dataloader: DataLoader,
87	    num_samples: int = 10_000,
88	    device: str = "cuda",
89	) -> Dict[str, float]:
90	    """Per-token next-token entropy, report mean and variance across all tokens."""
91	    model.eval()
92	    entropies = []
93	    seen = 0
94	
95	    with torch.no_grad():
96	        for batch in tqdm(dataloader, desc="token-entropy", leave=False):
97	            if seen >= num_samples:
98	                break
99	            input_ids = batch["input_ids"].to(device)
100	            attn_mask = batch["attention_mask"].to(device)
101	
102	            logits = model(input_ids=input_ids, attention_mask=attn_mask).logits
103	            # shift: predict position t+1 from position t
104	            logits = logits[:, :-1, :]
105	            mask = attn_mask[:, 1:].bool()
106	
107	            log_p = F.log_softmax(logits, dim=-1)
108	            p = log_p.exp()
109	            ent = -(p * log_p).sum(dim=-1)  # (B, L-1)
110	
111	            for i in range(ent.shape[0]):
112	                entropies.append(ent[i][mask[i]].cpu())
113	            seen += input_ids.shape[0]
114	
115	    all_ent = torch.cat(entropies).float()
116	    return {
117	        "token_entropy_mean": all_ent.mean().item(),
118	        "token_entropy_var": all_ent.var().item(),
119	        "token_entropy_std": all_ent.std().item(),
120	        "token_entropy_num_tokens": int(all_ent.shape[0]),
121	    }
122	
123	
124	# ---------------------------------------------------------------------------
125	# 3. N-gram entropy
126	# ---------------------------------------------------------------------------
127	
128	def compute_ngram_entropy(token_ids: List[int], max_n: int = 3) -> Dict[str, float]:
129	    """Shannon entropy of unigram / bigram / trigram distributions."""
130	    label = {1: "unigram", 2: "bigram", 3: "trigram"}
131	    results: Dict[str, float] = {}
132	    for n in range(1, max_n + 1):
133	        counter: Counter = Counter()
134	        for i in range(len(token_ids) - n + 1):
135	            counter[tuple(token_ids[i : i + n])] += 1
136	        total = sum(counter.values())
137	        entropy = -sum((c / total) * math.log(c / total) for c in counter.values())
138	        results[f"{label[n]}_entropy"] = entropy
139	        results[f"{label[n]}_unique"] = len(counter)
140	    return results
141	
142	
143	# ---------------------------------------------------------------------------
144	# 4. Vocabulary coverage
145	# ---------------------------------------------------------------------------
146	
147	def compute_vocab_coverage(token_ids: List[int], vocab_size: int) -> Dict[str, float]:
148	    unique = len(set(token_ids))
149	    return {
150	        "vocab_coverage": unique / vocab_size,
151	        "unique_tokens": unique,
152	        "total_tokens": len(token_ids),
153	    }
154	
155	
156	# ---------------------------------------------------------------------------
157	# 5. Perplexity
158	# ---------------------------------------------------------------------------
159	
160	def compute_perplexity(
161	    model: torch.nn.Module,
162	    dataloader: DataLoader,
163	    num_samples: int = 5_000,
164	    device: str = "cuda",
165	) -> Dict[str, float]:
166	    """Standard perplexity on held-out data."""
167	    model.eval()
168	    total_loss = 0.0
169	    total_tokens = 0
170	    seen = 0
171	
172	    with torch.no_grad():
173	        for batch in tqdm(dataloader, desc="perplexity", leave=False):
174	            if seen >= num_samples:
175	                break
176	            input_ids = batch["input_ids"].to(device)
177	            attn_mask = batch["attention_mask"].to(device)
178	            labels = input_ids.clone()
179	            labels[attn_mask == 0] = -100
180	
181	            loss = model(input_ids=input_ids, attention_mask=attn_mask, labels=labels).loss
182	            n_tok = (labels[:, 1:] != -100).sum().item()
183	            total_loss += loss.item() * n_tok
184	            total_tokens += n_tok
185	            seen += input_ids.shape[0]
186	
187	    avg_loss = total_loss / max(total_tokens, 1)
188	    return {
189	        "perplexity": math.exp(avg_loss),
190	        "avg_loss": avg_loss,
191	        "ppl_num_tokens": total_tokens,
192	    }
193	
194	
195	# ---------------------------------------------------------------------------
196	# 6. Inter-generational KL divergence (full distribution report)
197	# ---------------------------------------------------------------------------
198	
199	def _unigram_dist(ids: np.ndarray, vocab_size: int, smoothing: float = 1e-8) -> np.ndarray:
200	    c = np.bincount(ids, minlength=vocab_size).astype(np.float64)
201	    c += smoothing
202	    return c / c.sum()
203	
204	
205	def _bigram_kl(ids_a: List[int], ids_b: List[int], smoothing: float = 1e-8) -> float:
206	    """KL(P_a || P_b) over bigram distributions (sparse, observed-support only)."""
207	    ca: Counter = Counter(zip(ids_a[:-1], ids_a[1:]))
208	    cb: Counter = Counter(zip(ids_b[:-1], ids_b[1:]))
209	    all_bg = set(ca) | set(cb)
210	    n_bg = len(all_bg)
211	    total_a = sum(ca.values()) + smoothing * n_bg
212	    total_b = sum(cb.values()) + smoothing * n_bg
213	    kl = 0.0
214	    for bg in all_bg:
215	        pa = (ca.get(bg, 0) + smoothing) / total_a
216	        pb = (cb.get(bg, 0) + smoothing) / total_b
217	        kl += pa * math.log(pa / pb)
218	    return kl
219	
220	
221	def compute_kl_divergence(
222	    ids_a: List[int],
223	    ids_b: List[int],
224	    vocab_size: int,
225	    smoothing: float = 1e-8,
226	    n_bootstrap: int = 1000,
227	    ci_level: float = 0.95,
228	) -> Dict[str, float]:
229	    """Full KL divergence report.
230	
231	    Returns unigram KL, bigram KL, frequency-binned KL contributions
232	    (high/mid/low-freq tokens), and bootstrap 95% CI on unigram KL.
233	    """
234	    arr_a = np.array(ids_a, dtype=np.int64)
235	    arr_b = np.array(ids_b, dtype=np.int64)
236	
237	    # --- Unigram KL ---
238	    p = _unigram_dist(arr_a, vocab_size, smoothing)
239	    q = _unigram_dist(arr_b, vocab_size, smoothing)
240	    per_token_kl = p * np.log(p / q)
241	    kl_unigram = float(per_token_kl.sum())
242	    kl_reverse = float((q * np.log(q / p)).sum())
243	    js = 0.5 * (kl_unigram + kl_reverse)
244	
245	    # --- Bigram KL ---
246	    kl_bigram = _bigram_kl(ids_a, ids_b, smoothing)
247	
248	    # --- Frequency-binned KL (based on reference corpus ids_a) ---
249	    counts_a = np.bincount(arr_a, minlength=vocab_size)
250	    ranked = np.argsort(-counts_a)
251	    n_nonzero = int((counts_a[ranked] > 0).sum())
252	    cut_high = max(1, n_nonzero // 100)         # top 1% of token types
253	    cut_mid = max(cut_high + 1, n_nonzero // 5)  # top 20%
254	
255	    kl_freq_high = float(per_token_kl[ranked[:cut_high]].sum())
256	    kl_freq_mid = float(per_token_kl[ranked[cut_high:cut_mid]].sum())
257	    kl_freq_low = float(per_token_kl[ranked[cut_mid:]].sum())
258	
259	    # --- Bootstrap CI on unigram KL ---
260	    rng = np.random.default_rng(42)
261	    sub_n = min(1_000_000, len(arr_a), len(arr_b))
262	    boot_kls = np.empty(n_bootstrap)
263	    for i in range(n_bootstrap):
264	        sa = rng.choice(arr_a, size=sub_n, replace=True)
265	        sb = rng.choice(arr_b, size=sub_n, replace=True)
266	        bp = np.bincount(sa, minlength=vocab_size).astype(np.float64) + smoothing
267	        bq = np.bincount(sb, minlength=vocab_size).astype(np.float64) + smoothing
268	        bp /= bp.sum()
269	        bq /= bq.sum()
270	        boot_kls[i] = (bp * np.log(bp / bq)).sum()
271	
272	    alpha = (1 - ci_level) / 2
273	    ci_lo = float(np.percentile(boot_kls, alpha * 100))
274	    ci_hi = float(np.percentile(boot_kls, (1 - alpha) * 100))
275	
276	    return {
277	        "kl_unigram": kl_unigram,
278	        "kl_unigram_reverse": kl_reverse,
279	        "js_divergence": js,
280	        "kl_bigram": kl_bigram,
281	        "kl_freq_high": kl_freq_high,
282	        "kl_freq_mid": kl_freq_mid,
283	        "kl_freq_low": kl_freq_low,
284	        "kl_ci_lower_95": ci_lo,
285	        "kl_ci_upper_95": ci_hi,
286	        "kl_bootstrap_mean": float(boot_kls.mean()),
287	        "kl_bootstrap_std": float(boot_kls.std()),
288	        "kl_freq_high_ntypes": int(cut_high),
289	        "kl_freq_mid_ntypes": int(cut_mid - cut_high),
290	        "kl_freq_low_ntypes": int(max(0, n_nonzero - cut_mid)),
291	        "kl_ci_note": "token-level i.i.d. bootstrap; CI may be anti-conservative due to sequential dependence",
292	    }
293	
294	
295	# ---------------------------------------------------------------------------
296	# Orchestrator: all metrics for one checkpoint
297	# ---------------------------------------------------------------------------
298	
299	def compute_checkpoint_metrics(
300	    model: torch.nn.Module,
301	    holdout_loader: DataLoader,
302	    gen_token_ids: List[int],
303	    prev_gen_token_ids: Optional[List[int]],
304	    vocab_size: int,
305	    config,
306	    device: str = "cuda",
307	) -> Dict[str, float]:
308	    """Compute all six metric groups for a single checkpoint."""
309	    results: Dict[str, float] = {}
310	
311	    logger.info("Computing spectral effective rank ...")
312	    results.update(compute_spectral_effective_rank(
313	        model, holdout_loader, num_samples=config.spectral_num_samples, device=device
314	    ))
315	
316	    logger.info("Computing token entropy variance ...")
317	    results.update(compute_token_entropy_variance(
318	        model, holdout_loader, num_samples=config.ppl_num_samples, device=device
319	    ))
320	
321	    logger.info("Computing perplexity ...")
322	    results.update(compute_perplexity(
323	        model, holdout_loader, num_samples=config.ppl_num_samples, device=device
324	    ))
325	
326	    logger.info("Computing n-gram entropy & vocab coverage ...")
327	    results.update(compute_ngram_entropy(gen_token_ids))
328	    results.update(compute_vocab_coverage(gen_token_ids, vocab_size))
329	
330	    if prev_gen_token_ids is not None:
331	        logger.info("Computing KL divergence (full report) ...")
332	        results.update(compute_kl_divergence(prev_gen_token_ids, gen_token_ids, vocab_size))
333	
334	    return results
335	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "60ff85cb-037b-4c00-9e51-254478230283",
  "uuid": "f3ba0aca-9cac-476f-aef9-96c647c2ea3b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/code/metrics.py",
      "content": "\"\"\"Collapse-detection metrics for the pilot experiment.\n\nSix metrics computed at each training checkpoint:\n1. Spectral effective rank (core hypothesis)\n2. Token-level prediction entropy variance\n3. N-gram entropy (uni/bi/trigram)\n4. Vocabulary coverage\n5. Perplexity on held-out real data\n6. Inter-generational KL divergence (unigram approximation)\n\"\"\"\n\nimport math\nimport logging\nfrom collections import Counter\nfrom typing import Dict, List, Optional\n\nimport numpy as np\nimport torch\nimport torch.nn.functional as F\nfrom torch.utils.data import DataLoader\nfrom tqdm import tqdm\n\nlogger = logging.getLogger(__name__)\n\n\n# ---------------------------------------------------------------------------\n# 1. Spectral effective rank\n# ---------------------------------------------------------------------------\n\ndef compute_spectral_effective_rank(\n    model: torch.nn.Module,\n    dataloader: DataLoader,\n    num_samples: int = 50_000,\n    device: str = \"cuda\",\n) -> Dict[str, float]:\n    \"\"\"RankMe-style effective rank from final-layer hidden states.\n\n    Collects mean-pooled hidden states E (N x d), computes singular values,\n    normalises to a distribution p, and returns exp(H(p)).\n    \"\"\"\n    model.eval()\n    hidden_list = []\n    collected = 0\n\n    with torch.no_grad():\n        for batch in tqdm(dataloader, desc=\"spectral-rank\", leave=False):\n            if collected >= num_samples:\n                break\n            input_ids = batch[\"input_ids\"].to(device)\n            attn_mask = batch[\"attention_mask\"].to(device)\n\n            out = model(input_ids=input_ids, attention_mask=attn_mask, output_hidden_states=True)\n            # final-layer hidden: (B, L, D)\n            h = out.hidden_states[-1].float()\n\n            # mean-pool over sequence (mask-aware)\n            mask = attn_mask.unsqueeze(-1).float()\n            pooled = (h * mask).sum(1) / mask.sum(1).clamp(min=1)  # (B, D)\n            hidden_list.append(pooled.cpu())\n            collected += pooled.shape[0]\n\n    E = torch.cat(hidden_list, dim=0)[:num_samples]  # (N, D)\n    sigma = torch.linalg.svdvals(E)                   # descending\n\n    # normalise to probability distribution\n    sigma_pos = sigma[sigma > 0]\n    p = sigma_pos / sigma_pos.sum()\n    entropy = -(p * p.log()).sum().item()\n    eff_rank = math.exp(entropy)\n\n    return {\n        \"spectral_effective_rank\": eff_rank,\n        \"spectral_entropy\": entropy,\n        \"top_singular_value\": sigma[0].item(),\n        \"sigma_ratio_top_bottom\": (sigma[0] / sigma_pos[-1]).item(),\n        \"spectral_num_samples\": int(E.shape[0]),\n    }\n\n\n# ---------------------------------------------------------------------------\n# 2. Token-level prediction entropy variance\n# ---------------------------------------------------------------------------\n\ndef compute_token_entropy_variance(\n    model: torch.nn.Module,\n    dataloader: DataLoader,\n    num_samples: int = 10_000,\n    device: str = \"cuda\",\n) -> Dict[str, float]:\n    \"\"\"Per-token next-token entropy, report mean and variance across all tokens.\"\"\"\n    model.eval()\n    entropies = []\n    seen = 0\n\n    with torch.no_grad():\n        for batch in tqdm(dataloader, desc=\"token-entropy\", leave=False):\n            if seen >= num_samples:\n                break\n            input_ids = batch[\"input_ids\"].to(device)\n            attn_mask = batch[\"attention_mask\"].to(device)\n\n            logits = model(input_ids=input_ids, attention_mask=attn_mask).logits\n            # shift: predict position t+1 from position t\n            logits = logits[:, :-1, :]\n            mask = attn_mask[:, 1:].bool()\n\n            log_p = F.log_softmax(logits, dim=-1)\n            p = log_p.exp()\n            ent = -(p * log_p).sum(dim=-1)  # (B, L-1)\n\n            for i in range(ent.shape[0]):\n                entropies.append(ent[i][mask[i]].cpu())\n            seen += input_ids.shape[0]\n\n    all_ent = torch.cat(entropies).float()\n    return {\n        \"token_entropy_mean\": all_ent.mean().item(),\n        \"token_entropy_var\": all_ent.var().item(),\n        \"token_entropy_std\": all_ent.std().item(),\n        \"token_entropy_num_tokens\": int(all_ent.shape[0]),\n    }\n\n\n# ---------------------------------------------------------------------------\n# 3. N-gram entropy\n# ---------------------------------------------------------------------------\n\ndef compute_ngram_entropy(token_ids: List[int], max_n: int = 3) -> Dict[str, float]:\n    \"\"\"Shannon entropy of unigram / bigram / trigram distributions.\"\"\"\n    label = {1: \"unigram\", 2: \"bigram\", 3: \"trigram\"}\n    results: Dict[str, float] = {}\n    for n in range(1, max_n + 1):\n        counter: Counter = Counter()\n        for i in range(len(token_ids) - n + 1):\n            counter[tuple(token_ids[i : i + n])] += 1\n        total = sum(counter.values())\n        entropy = -sum((c / total) * math.log(c / total) for c in counter.values())\n        results[f\"{label[n]}_entropy\"] = entropy\n        results[f\"{label[n]}_unique\"] = len(counter)\n    return results\n\n\n# ---------------------------------------------------------------------------\n# 4. Vocabulary coverage\n# ---------------------------------------------------------------------------\n\ndef compute_vocab_coverage(token_ids: List[int], vocab_size: int) -> Dict[str, float]:\n    unique = len(set(token_ids))\n    return {\n        \"vocab_coverage\": unique / vocab_size,\n        \"unique_tokens\": unique,\n        \"total_tokens\": len(token_ids),\n    }\n\n\n# ---------------------------------------------------------------------------\n# 5. Perplexity\n# ---------------------------------------------------------------------------\n\ndef compute_perplexity(\n    model: torch.nn.Module,\n    dataloader: DataLoader,\n    num_samples: int = 5_000,\n    device: str = \"cuda\",\n) -> Dict[str, float]:\n    \"\"\"Standard perplexity on held-out data.\"\"\"\n    model.eval()\n    total_loss = 0.0\n    total_tokens = 0\n    seen = 0\n\n    with torch.no_grad():\n        for batch in tqdm(dataloader, desc=\"perplexity\", leave=False):\n            if seen >= num_samples:\n                break\n            input_ids = batch[\"input_ids\"].to(device)\n            attn_mask = batch[\"attention_mask\"].to(device)\n            labels = input_ids.clone()\n            labels[attn_mask == 0] = -100\n\n            loss = model(input_ids=input_ids, attention_mask=attn_mask, labels=labels).loss\n            n_tok = (labels[:, 1:] != -100).sum().item()\n            total_loss += loss.item() * n_tok\n            total_tokens += n_tok\n            seen += input_ids.shape[0]\n\n    avg_loss = total_loss / max(total_tokens, 1)\n    return {\n        \"perplexity\": math.exp(avg_loss),\n        \"avg_loss\": avg_loss,\n        \"ppl_num_tokens\": total_tokens,\n    }\n\n\n# ---------------------------------------------------------------------------\n# 6. Inter-generational KL divergence (full distribution report)\n# ---------------------------------------------------------------------------\n\ndef _unigram_dist(ids: np.ndarray, vocab_size: int, smoothing: float = 1e-8) -> np.ndarray:\n    c = np.bincount(ids, minlength=vocab_size).astype(np.float64)\n    c += smoothing\n    return c / c.sum()\n\n\ndef _bigram_kl(ids_a: List[int], ids_b: List[int], smoothing: float = 1e-8) -> float:\n    \"\"\"KL(P_a || P_b) over bigram distributions (sparse, observed-support only).\"\"\"\n    ca: Counter = Counter(zip(ids_a[:-1], ids_a[1:]))\n    cb: Counter = Counter(zip(ids_b[:-1], ids_b[1:]))\n    all_bg = set(ca) | set(cb)\n    n_bg = len(all_bg)\n    total_a = sum(ca.values()) + smoothing * n_bg\n    total_b = sum(cb.values()) + smoothing * n_bg\n    kl = 0.0\n    for bg in all_bg:\n        pa = (ca.get(bg, 0) + smoothing) / total_a\n        pb = (cb.get(bg, 0) + smoothing) / total_b\n        kl += pa * math.log(pa / pb)\n    return kl\n\n\ndef compute_kl_divergence(\n    ids_a: List[int],\n    ids_b: List[int],\n    vocab_size: int,\n    smoothing: float = 1e-8,\n    n_bootstrap: int = 1000,\n    ci_level: float = 0.95,\n) -> Dict[str, float]:\n    \"\"\"Full KL divergence report.\n\n    Returns unigram KL, bigram KL, frequency-binned KL contributions\n    (high/mid/low-freq tokens), and bootstrap 95% CI on unigram KL.\n    \"\"\"\n    arr_a = np.array(ids_a, dtype=np.int64)\n    arr_b = np.array(ids_b, dtype=np.int64)\n\n    # --- Unigram KL ---\n    p = _unigram_dist(arr_a, vocab_size, smoothing)\n    q = _unigram_dist(arr_b, vocab_size, smoothing)\n    per_token_kl = p * np.log(p / q)\n    kl_unigram = float(per_token_kl.sum())\n    kl_reverse = float((q * np.log(q / p)).sum())\n    js = 0.5 * (kl_unigram + kl_reverse)\n\n    # --- Bigram KL ---\n    kl_bigram = _bigram_kl(ids_a, ids_b, smoothing)\n\n    # --- Frequency-binned KL (based on reference corpus ids_a) ---\n    counts_a = np.bincount(arr_a, minlength=vocab_size)\n    ranked = np.argsort(-counts_a)\n    n_nonzero = int((counts_a[ranked] > 0).sum())\n    cut_high = max(1, n_nonzero // 100)         # top 1% of token types\n    cut_mid = max(cut_high + 1, n_nonzero // 5)  # top 20%\n\n    kl_freq_high = float(per_token_kl[ranked[:cut_high]].sum())\n    kl_freq_mid = float(per_token_kl[ranked[cut_high:cut_mid]].sum())\n    kl_freq_low = float(per_token_kl[ranked[cut_mid:]].sum())\n\n    # --- Bootstrap CI on unigram KL ---\n    rng = np.random.default_rng(42)\n    sub_n = min(1_000_000, len(arr_a), len(arr_b))\n    boot_kls = np.empty(n_bootstrap)\n    for i in range(n_bootstrap):\n        sa = rng.choice(arr_a, size=sub_n, replace=True)\n        sb = rng.choice(arr_b, size=sub_n, replace=True)\n        bp = np.bincount(sa, minlength=vocab_size).astype(np.float64) + smoothing\n        bq = np.bincount(sb, minlength=vocab_size).astype(np.float64) + smoothing\n        bp /= bp.sum()\n        bq /= bq.sum()\n        boot_kls[i] = (bp * np.log(bp / bq)).sum()\n\n    alpha = (1 - ci_level) / 2\n    ci_lo = float(np.percentile(boot_kls, alpha * 100))\n    ci_hi = float(np.percentile(boot_kls, (1 - alpha) * 100))\n\n    return {\n        \"kl_unigram\": kl_unigram,\n        \"kl_unigram_reverse\": kl_reverse,\n        \"js_divergence\": js,\n        \"kl_bigram\": kl_bigram,\n        \"kl_freq_high\": kl_freq_high,\n        \"kl_freq_mid\": kl_freq_mid,\n        \"kl_freq_low\": kl_freq_low,\n        \"kl_ci_lower_95\": ci_lo,\n        \"kl_ci_upper_95\": ci_hi,\n        \"kl_bootstrap_mean\": float(boot_kls.mean()),\n        \"kl_bootstrap_std\": float(boot_kls.std()),\n        \"kl_freq_high_ntypes\": int(cut_high),\n        \"kl_freq_mid_ntypes\": int(cut_mid - cut_high),\n        \"kl_freq_low_ntypes\": int(max(0, n_nonzero - cut_mid)),\n        \"kl_ci_note\": \"token-level i.i.d. bootstrap; CI may be anti-conservative due to sequential dependence\",\n    }\n\n\n# ---------------------------------------------------------------------------\n# Orchestrator: all metrics for one checkpoint\n# ---------------------------------------------------------------------------\n\ndef compute_checkpoint_metrics(\n    model: torch.nn.Module,\n    holdout_loader: DataLoader,\n    gen_token_ids: List[int],\n    prev_gen_token_ids: Optional[List[int]],\n    vocab_size: int,\n    config,\n    device: str = \"cuda\",\n) -> Dict[str, float]:\n    \"\"\"Compute all six metric groups for a single checkpoint.\"\"\"\n    results: Dict[str, float] = {}\n\n    logger.info(\"Computing spectral effective rank ...\")\n    results.update(compute_spectral_effective_rank(\n        model, holdout_loader, num_samples=config.spectral_num_samples, device=device\n    ))\n\n    logger.info(\"Computing token entropy variance ...\")\n    results.update(compute_token_entropy_variance(\n        model, holdout_loader, num_samples=config.ppl_num_samples, device=device\n    ))\n\n    logger.info(\"Computing perplexity ...\")\n    results.update(compute_perplexity(\n        model, holdout_loader, num_samples=config.ppl_num_samples, device=device\n    ))\n\n    logger.info(\"Computing n-gram entropy & vocab coverage ...\")\n    results.update(compute_ngram_entropy(gen_token_ids))\n    results.update(compute_vocab_coverage(gen_token_ids, vocab_size))\n\n    if prev_gen_token_ids is not None:\n        logger.info(\"Computing KL divergence (full report) ...\")\n        results.update(compute_kl_divergence(prev_gen_token_ids, gen_token_ids, vocab_size))\n\n    return results\n",
      "numLines": 335,
      "startLine": 1,
      "totalLines": 335
    }
  }
}
```

</details>

---

### Tool call

_source line 38_

<details open><summary>🔧 Tool call — Read · `toolu_012u2Y2ghV5e55Q8ozm3drTB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/code/config.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "60ff85cb-037b-4c00-9e51-254478230283",
  "uuid": "5dd82b0f-db23-4843-8e5a-805f878af1c0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MRKyqfG8N15atD2DVnEpFh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1781,
      "cache_read_input_tokens": 25088,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1781
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

_source line 39 · 2026-05-13T08:19:28.937Z_

<details><summary>↩ Tool result · `toolu_012u2Y2ghV5e55Q8ozm3drTB`</summary>

```text
1	"""Pilot experiment configuration for collapse-aware-mixing MVP.
2	
3	Validates spectral effective rank as a leading indicator of model collapse
4	in iterative synthetic training (Pythia-1B, 3 generations x 500M tokens).
5	"""
6	
7	import os
8	from dataclasses import dataclass
9	
10	
11	@dataclass
12	class PilotConfig:
13	    # --- Model ---
14	    model_name: str = "EleutherAI/pythia-1b"
15	
16	    # --- Training ---
17	    num_generations: int = 3                    # G0 (real), G1 (synth from G0), G2 (synth from G1)
18	    tokens_per_generation: int = 100_000_000    # 100M tokens per generation
19	    checkpoint_interval_tokens: int = 10_000_000  # save + eval every 10M tokens
20	    max_seq_length: int = 2048
21	    per_device_batch_size: int = 8
22	    gradient_accumulation_steps: int = 4
23	    learning_rate: float = 2e-6
24	    warmup_ratio: float = 0.05
25	    weight_decay: float = 0.01
26	    seed: int = 42
27	    bf16: bool = True
28	    gradient_checkpointing: bool = True
29	
30	    # --- Synthetic data generation ---
31	    gen_temperature: float = 1.0
32	    gen_top_p: float = 0.95
33	    gen_batch_size: int = 32
34	    gen_max_new_tokens: int = 2048
35	
36	    # --- Metrics ---
37	    spectral_num_samples: int = 50_000          # sequences for spectral effective rank
38	    spectral_batch_size: int = 64
39	    metrics_gen_tokens: int = 500_000           # tokens to generate at each ckpt for n-gram/coverage
40	    ppl_num_samples: int = 5_000                # sequences for PPL evaluation
41	    ppl_batch_size: int = 16
42	
43	    # --- Data ---
44	    real_dataset: str = "wikitext"
45	    real_dataset_config: str = "wikitext-103-raw-v1"
46	    holdout_size: int = 10_000                  # sequences reserved for evaluation
47	
48	    # --- Paths ---
49	    output_dir: str = "./output"
50	
51	    # --- Logging ---
52	    use_wandb: bool = True
53	    wandb_project: str = "collapse-aware-mixing"
54	    wandb_run_prefix: str = "pilot"
55	
56	    # --- Derived properties ---
57	
58	    @property
59	    def effective_batch_size(self) -> int:
60	        return self.per_device_batch_size * self.gradient_accumulation_steps
61	
62	    @property
63	    def tokens_per_step(self) -> int:
64	        return self.max_seq_length * self.effective_batch_size
65	
66	    @property
67	    def save_steps(self) -> int:
68	        return self.checkpoint_interval_tokens // self.tokens_per_step
69	
70	    @property
71	    def max_steps(self) -> int:
72	        return self.tokens_per_generation // self.tokens_per_step
73	
74	    def gen_dir(self, g: int) -> str:
75	        return os.path.join(self.output_dir, f"G{g}")
76	
77	    def checkpoint_dir(self, g: int, step: int) -> str:
78	        return os.path.join(self.gen_dir(g), "training", f"checkpoint-{step}")
79	
80	    def synthetic_data_path(self, g: int) -> str:
81	        return os.path.join(self.gen_dir(g), "synthetic_data")
82	
83	    def metrics_path(self, g: int) -> str:
84	        return os.path.join(self.gen_dir(g), "metrics.jsonl")
85	
86	    def summary_path(self) -> str:
87	        return os.path.join(self.output_dir, "pilot_summary.json")
88	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "60ff85cb-037b-4c00-9e51-254478230283",
  "uuid": "e4a22dc8-d1fa-4501-a23a-0468ba9947a3",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/code/config.py",
      "content": "\"\"\"Pilot experiment configuration for collapse-aware-mixing MVP.\n\nValidates spectral effective rank as a leading indicator of model collapse\nin iterative synthetic training (Pythia-1B, 3 generations x 500M tokens).\n\"\"\"\n\nimport os\nfrom dataclasses import dataclass\n\n\n@dataclass\nclass PilotConfig:\n    # --- Model ---\n    model_name: str = \"EleutherAI/pythia-1b\"\n\n    # --- Training ---\n    num_generations: int = 3                    # G0 (real), G1 (synth from G0), G2 (synth from G1)\n    tokens_per_generation: int = 100_000_000    # 100M tokens per generation\n    checkpoint_interval_tokens: int = 10_000_000  # save + eval every 10M tokens\n    max_seq_length: int = 2048\n    per_device_batch_size: int = 8\n    gradient_accumulation_steps: int = 4\n    learning_rate: float = 2e-6\n    warmup_ratio: float = 0.05\n    weight_decay: float = 0.01\n    seed: int = 42\n    bf16: bool = True\n    gradient_checkpointing: bool = True\n\n    # --- Synthetic data generation ---\n    gen_temperature: float = 1.0\n    gen_top_p: float = 0.95\n    gen_batch_size: int = 32\n    gen_max_new_tokens: int = 2048\n\n    # --- Metrics ---\n    spectral_num_samples: int = 50_000          # sequences for spectral effective rank\n    spectral_batch_size: int = 64\n    metrics_gen_tokens: int = 500_000           # tokens to generate at each ckpt for n-gram/coverage\n    ppl_num_samples: int = 5_000                # sequences for PPL evaluation\n    ppl_batch_size: int = 16\n\n    # --- Data ---\n    real_dataset: str = \"wikitext\"\n    real_dataset_config: str = \"wikitext-103-raw-v1\"\n    holdout_size: int = 10_000                  # sequences reserved for evaluation\n\n    # --- Paths ---\n    output_dir: str = \"./output\"\n\n    # --- Logging ---\n    use_wandb: bool = True\n    wandb_project: str = \"collapse-aware-mixing\"\n    wandb_run_prefix: str = \"pilot\"\n\n    # --- Derived properties ---\n\n    @property\n    def effective_batch_size(self) -> int:\n        return self.per_device_batch_size * self.gradient_accumulation_steps\n\n    @property\n    def tokens_per_step(self) -> int:\n        return self.max_seq_length * self.effective_batch_size\n\n    @property\n    def save_steps(self) -> int:\n        return self.checkpoint_interval_tokens // self.tokens_per_step\n\n    @property\n    def max_steps(self) -> int:\n        return self.tokens_per_generation // self.tokens_per_step\n\n    def gen_dir(self, g: int) -> str:\n        return os.path.join(self.output_dir, f\"G{g}\")\n\n    def checkpoint_dir(self, g: int, step: int) -> str:\n        return os.path.join(self.gen_dir(g), \"training\", f\"checkpoint-{step}\")\n\n    def synthetic_data_path(self, g: int) -> str:\n        return os.path.join(self.gen_dir(g), \"synthetic_data\")\n\n    def metrics_path(self, g: int) -> str:\n        return os.path.join(self.gen_dir(g), \"metrics.jsonl\")\n\n    def summary_path(self) -> str:\n        return os.path.join(self.output_dir, \"pilot_summary.json\")\n",
      "numLines": 88,
      "startLine": 1,
      "totalLines": 88
    }
  }
}
```

</details>

---

### Tool call

_source line 40_

<details open><summary>🔧 Tool call — Read · `toolu_01GnFMvyo3cJiAPUYUqp4Sv5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/code/pilot_pipeline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "60ff85cb-037b-4c00-9e51-254478230283",
  "uuid": "a8f0941f-e928-4cc7-9060-bf24dba346bc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MRKyqfG8N15atD2DVnEpFh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1781,
      "cache_read_input_tokens": 25088,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1781
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

_source line 41 · 2026-05-13T08:19:29.318Z_

<details><summary>↩ Tool result · `toolu_01GnFMvyo3cJiAPUYUqp4Sv5`</summary>

```text
1	"""End-to-end pilot pipeline: G0 -> gen -> G1 -> gen -> G2 with metrics at every checkpoint.
2	
3	Usage:
4	    python pilot_pipeline.py [--output_dir ./output] [--num_generations 3] [--no_wandb]
5	"""
6	
7	import argparse
8	import json
9	import logging
10	import os
11	import sys
12	import time
13	
14	import numpy as np
15	import torch
16	from transformers import AutoModelForCausalLM, AutoTokenizer
17	
18	from config import PilotConfig
19	from data_utils import (
20	    prepare_real_data,
21	    prepare_synthetic_data,
22	    extract_token_ids,
23	    make_dataloader,
24	)
25	from generate import generate_synthetic_data, generate_sample_tokens
26	from metrics import compute_checkpoint_metrics
27	from train import train_generation
28	
29	logging.basicConfig(
30	    level=logging.INFO,
31	    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
32	    handlers=[logging.StreamHandler(sys.stdout)],
33	)
34	logger = logging.getLogger("pilot")
35	
36	
37	def evaluate_checkpoints(
38	    checkpoint_paths: list[str],
39	    gen_idx: int,
40	    holdout_dataset,
41	    prev_gen_token_ids: list[int] | None,
42	    config: PilotConfig,
43	    device: str,
44	) -> list[dict]:
45	    """Load each checkpoint, compute all metrics, return list of metric dicts."""
46	    tokenizer = AutoTokenizer.from_pretrained(config.model_name)
47	    if tokenizer.pad_token is None:
48	        tokenizer.pad_token = tokenizer.eos_token
49	    vocab_size = tokenizer.vocab_size
50	
51	    holdout_loader = make_dataloader(holdout_dataset, batch_size=config.ppl_batch_size)
52	    all_metrics = []
53	
54	    for ci, ckpt_path in enumerate(checkpoint_paths):
55	        logger.info("--- Evaluating checkpoint %d/%d: %s ---", ci + 1, len(checkpoint_paths), ckpt_path)
56	        t0 = time.time()
57	
58	        model = AutoModelForCausalLM.from_pretrained(ckpt_path, torch_dtype=torch.bfloat16).to(device)
59	        model.eval()
60	
61	        # generate a small sample for n-gram / coverage metrics
62	        logger.info("Generating %dK tokens for corpus metrics ...", config.metrics_gen_tokens // 1000)
63	        gen_ids = generate_sample_tokens(
64	            model, tokenizer,
65	            num_tokens=config.metrics_gen_tokens,
66	            batch_size=config.gen_batch_size,
67	            max_new_tokens=256,
68	            temperature=config.gen_temperature,
69	            top_p=config.gen_top_p,
70	            device=device,
71	        )
72	
73	        m = compute_checkpoint_metrics(
74	            model=model,
75	            holdout_loader=holdout_loader,
76	            gen_token_ids=gen_ids,
77	            prev_gen_token_ids=prev_gen_token_ids,
78	            vocab_size=vocab_size,
79	            config=config,
80	            device=device,
81	        )
82	        m["generation"] = gen_idx
83	        m["checkpoint"] = ckpt_path
84	        m["checkpoint_index"] = ci
85	
86	        # extract step count from checkpoint dir name
87	        step_str = os.path.basename(ckpt_path).split("-")[-1]
88	        m["global_step"] = int(step_str) if step_str.isdigit() else ci
89	        m["tokens_seen"] = m["global_step"] * config.tokens_per_step
90	        m["eval_time_sec"] = time.time() - t0
91	
92	        all_metrics.append(m)
93	        logger.info(
94	            "  eff_rank=%.1f  ppl=%.2f  entropy_var=%.4f  unigram_H=%.3f  coverage=%.4f  (%.0fs)",
95	            m["spectral_effective_rank"], m["perplexity"],
96	            m["token_entropy_var"], m["unigram_entropy"],
97	            m["vocab_coverage"], m["eval_time_sec"],
98	        )
99	
100	        del model
101	        torch.cuda.empty_cache()
102	
103	    return all_metrics
104	
105	
106	def save_metrics(metrics: list[dict], path: str):
107	    os.makedirs(os.path.dirname(path), exist_ok=True)
108	    with open(path, "a") as f:
109	        for m in metrics:
110	            f.write(json.dumps(m, default=str) + "\n")
111	    logger.info("Metrics appended to %s", path)
112	
113	
114	def run_pilot(config: PilotConfig):
115	    device = "cuda" if torch.cuda.is_available() else "cpu"
116	    os.makedirs(config.output_dir, exist_ok=True)
117	
118	    logger.info("=" * 60)
119	    logger.info("PILOT PIPELINE START")
120	    logger.info("  Model: %s", config.model_name)
121	    logger.info("  Generations: %d | Tokens/gen: %dM", config.num_generations, config.tokens_per_generation // 1_000_000)
122	    logger.info("  Checkpoint interval: %dM tokens (%d steps)", config.checkpoint_interval_tokens // 1_000_000, config.save_steps)
123	    logger.info("  Device: %s", device)
124	    logger.info("=" * 60)
125	
126	    # --- Prepare data ---
127	    tokenizer = AutoTokenizer.from_pretrained(config.model_name)
128	    if tokenizer.pad_token is None:
129	        tokenizer.pad_token = tokenizer.eos_token
130	
131	    logger.info("Preparing real data ...")
132	    train_dataset, holdout_dataset = prepare_real_data(config, tokenizer)
133	
134	    all_results = []
135	    prev_gen_token_ids = None
136	    prev_model_dir = None  # G0: None → config.model_name; G1+: previous gen's final checkpoint
137	    g0_baseline = None  # populated after G0 evaluation
138	
139	    for g in range(config.num_generations):
140	        logger.info("=" * 60)
141	        logger.info("GENERATION %d / %d", g, config.num_generations - 1)
142	        logger.info("=" * 60)
143	
144	        # --- Determine training data ---
145	        if g == 0:
146	            gen_train = train_dataset
147	        else:
148	            synth_path = config.synthetic_data_path(g - 1)
149	            gen_train = prepare_synthetic_data(synth_path, config, tokenizer)
150	
151	        # --- Train (chain model from previous generation) ---
152	        final_model_dir, ckpt_paths = train_generation(
153	            gen_idx=g,
154	            train_dataset=gen_train,
155	            config=config,
156	            model_name_or_path=prev_model_dir,
157	        )
158	
159	        # include final model as the last eval point
160	        if final_model_dir not in ckpt_paths:
161	            ckpt_paths.append(final_model_dir)
162	
163	        # --- Evaluate all checkpoints ---
164	        gen_metrics = evaluate_checkpoints(
165	            checkpoint_paths=ckpt_paths,
166	            gen_idx=g,
167	            holdout_dataset=holdout_dataset,
168	            prev_gen_token_ids=prev_gen_token_ids,
169	            config=config,
170	            device=device,
171	        )
172	        save_metrics(gen_metrics, config.metrics_path(g))
173	        all_results.extend(gen_metrics)
174	
175	        # --- G0 baseline statistics for leading-indicator threshold ---
176	        if g == 0 and gen_metrics:
177	            ranks = np.array([m["spectral_effective_rank"] for m in gen_metrics])
178	            ppls = np.array([m["perplexity"] for m in gen_metrics])
179	            g0_baseline = {
180	                "spectral_rank_mean": float(ranks.mean()),
181	                "spectral_rank_std": float(ranks.std()),
182	                "spectral_rank_min": float(ranks.min()),
183	                "spectral_rank_max": float(ranks.max()),
184	                "ppl_final": float(ppls[-1]),
185	                "ppl_mean": float(ppls.mean()),
186	                "ppl_std": float(ppls.std()),
187	                "num_checkpoints": len(gen_metrics),
188	            }
189	            logger.info("G0 BASELINE: rank=%.1f +/- %.2f (sigma for 1-sigma threshold)  ppl_final=%.2f",
190	                         g0_baseline["spectral_rank_mean"], g0_baseline["spectral_rank_std"],
191	                         g0_baseline["ppl_final"])
192	
193	        # --- Generate synthetic data for next generation ---
194	        if g < config.num_generations - 1:
195	            logger.info("Generating synthetic data from G%d for next generation ...", g)
196	            model = AutoModelForCausalLM.from_pretrained(final_model_dir, torch_dtype=torch.bfloat16).to(device)
197	            gen_tok = AutoTokenizer.from_pretrained(config.model_name)
198	            if gen_tok.pad_token is None:
199	                gen_tok.pad_token = gen_tok.eos_token
200	
201	            generate_synthetic_data(
202	                model=model,
203	                tokenizer=gen_tok,
204	                num_tokens=config.tokens_per_generation,
205	                config=config,
206	                output_dir=config.synthetic_data_path(g),
207	            )
208	
209	            # save current gen token ids for KL computation in next gen
210	            synth_ds = prepare_synthetic_data(config.synthetic_data_path(g), config, gen_tok)
211	            prev_gen_token_ids = extract_token_ids(synth_ds, max_tokens=10_000_000)
212	
213	            del model
214	            torch.cuda.empty_cache()
215	
216	        # chain: next generation initialises from this generation's final model
217	        prev_model_dir = final_model_dir
218	
219	    # --- Summary ---
220	    summary = {
221	        "config": {k: v for k, v in config.__dict__.items() if not k.startswith("_")},
222	        "num_checkpoints_evaluated": len(all_results),
223	        "g0_baseline": g0_baseline,
224	        "generations": {},
225	    }
226	    for g in range(config.num_generations):
227	        gm = [m for m in all_results if m["generation"] == g]
228	        if gm:
229	            gen_summary = {
230	                "final_spectral_rank": gm[-1]["spectral_effective_rank"],
231	                "final_ppl": gm[-1]["perplexity"],
232	                "spectral_rank_trajectory": [m["spectral_effective_rank"] for m in gm],
233	                "ppl_trajectory": [m["perplexity"] for m in gm],
234	            }
235	            if "kl_unigram" in gm[-1]:
236	                gen_summary["final_kl_unigram"] = gm[-1]["kl_unigram"]
237	                gen_summary["final_kl_bigram"] = gm[-1].get("kl_bigram")
238	                gen_summary["final_kl_ci_95"] = [gm[-1].get("kl_ci_lower_95"), gm[-1].get("kl_ci_upper_95")]
239	            summary["generations"][f"G{g}"] = gen_summary
240	
241	    summary_path = config.summary_path()
242	    with open(summary_path, "w") as f:
243	        json.dump(summary, f, indent=2, default=str)
244	    logger.info("Summary written to %s", summary_path)
245	
246	    # --- MVP GO / NO-GO check (quantitative criteria from ROADMAP) ---
247	    if g0_baseline and len(summary["generations"]) >= 2:
248	        sigma = g0_baseline["spectral_rank_std"]
249	        g0_rank_mean = g0_baseline["spectral_rank_mean"]
250	        g0_ppl = g0_baseline["ppl_final"]
251	        rank_threshold = g0_rank_mean - sigma  # drop >= 1 sigma
252	
253	        # PPL significance: >= 2 pts absolute OR >= 5% relative
254	        ppl_abs_threshold = g0_ppl + 2.0
255	        ppl_rel_threshold = g0_ppl * 1.05
256	
257	        # Scan all post-G0 checkpoints for the leading indicator pattern:
258	        # find first checkpoint where rank drops >= 1 sigma below G0 mean
259	        # and check whether PPL has NOT yet risen significantly at that point
260	        first_rank_drop_idx = None
261	        first_ppl_rise_idx = None
262	
263	        post_g0 = [m for m in all_results if m["generation"] > 0]
264	        for i, m in enumerate(post_g0):
265	            if first_rank_drop_idx is None and m["spectral_effective_rank"] <= rank_threshold:
266	                first_rank_drop_idx = i
267	            if first_ppl_rise_idx is None and (m["perplexity"] >= ppl_abs_threshold or m["perplexity"] >= ppl_rel_threshold):
268	                first_ppl_rise_idx = i
269	
270	        # KL check (on final generation boundary)
271	        last_gen_metrics = [m for m in all_results if m["generation"] == config.num_generations - 1]
272	        kl_value = last_gen_metrics[-1].get("kl_unigram", 0) if last_gen_metrics else 0
273	        kl_ci = (last_gen_metrics[-1].get("kl_ci_lower_95", 0), last_gen_metrics[-1].get("kl_ci_upper_95", 0)) if last_gen_metrics else (0, 0)
274	
275	        spectral_leads = (first_rank_drop_idx is not None and
276	                          (first_ppl_rise_idx is None or first_rank_drop_idx < first_ppl_rise_idx))
277	        kl_above_threshold = kl_value > 0.1
278	
279	        logger.info("=" * 60)
280	        logger.info("MVP GO / NO-GO CHECK")
281	        logger.info("  G0 baseline: rank=%.1f +/- %.2f (1-sigma threshold=%.1f)  ppl=%.2f",
282	                     g0_rank_mean, sigma, rank_threshold, g0_ppl)
283	        logger.info("  PPL significance: >= %.2f (abs +2) OR >= %.2f (rel +5%%)",
284	                     ppl_abs_threshold, ppl_rel_threshold)
285	        logger.info("  First rank drop (>= 1 sigma): %s",
286	                     f"checkpoint {first_rank_drop_idx}" if first_rank_drop_idx is not None else "NOT DETECTED")
287	        logger.info("  First PPL rise (significant): %s",
288	                     f"checkpoint {first_ppl_rise_idx}" if first_ppl_rise_idx is not None else "NOT DETECTED")
289	        logger.info("  Spectral leads PPL: %s", spectral_leads)
290	        logger.info("  KL divergence: %.4f  (95%% CI: [%.4f, %.4f])  threshold 0.1: %s",
291	                     kl_value, kl_ci[0], kl_ci[1], "PASS" if kl_above_threshold else "FAIL")
292	
293	        if spectral_leads and kl_above_threshold:
294	            verdict = "GO — spectral rank is a leading indicator, KL confirms non-stationarity"
295	        elif first_rank_drop_idx is not None and first_ppl_rise_idx is not None and first_rank_drop_idx == first_ppl_rise_idx:
296	            verdict = "CONDITIONAL GO — spectral and PPL drop simultaneously, check granularity advantage"
297	        elif kl_value < 0.1 and (first_rank_drop_idx is not None or first_ppl_rise_idx is not None):
298	            verdict = "EXTEND — KL below threshold but collapse signals detected, add generation to accumulate KL"
299	        elif first_rank_drop_idx is None and first_ppl_rise_idx is not None:
300	            verdict = "KILL — PPL rose but spectral rank did not drop, indicator ineffective for autoregressive LM collapse"
301	        elif first_rank_drop_idx is None and first_ppl_rise_idx is None:
302	            verdict = "EXTEND — neither spectral rank nor PPL moved in 2 generations, add generation to trigger collapse"
303	        else:
304	            verdict = "INCONCLUSIVE — review trajectories manually"
305	
306	        logger.info("  VERDICT: %s", verdict)
307	        logger.info("=" * 60)
308	
309	        summary["mvp_check"] = {
310	            "g0_rank_mean": g0_rank_mean,
311	            "g0_rank_std": sigma,
312	            "rank_threshold_1sigma": rank_threshold,
313	            "ppl_threshold_abs": ppl_abs_threshold,
314	            "ppl_threshold_rel": ppl_rel_threshold,
315	            "first_rank_drop_checkpoint": first_rank_drop_idx,
316	            "first_ppl_rise_checkpoint": first_ppl_rise_idx,
317	            "spectral_leads": spectral_leads,
318	            "kl_unigram": kl_value,
319	            "kl_ci_95": list(kl_ci),
320	            "kl_above_0_1": kl_above_threshold,
321	            "verdict": verdict,
322	        }
323	        with open(summary_path, "w") as f:
324	            json.dump(summary, f, indent=2, default=str)
325	
326	    return all_results
327	
328	
329	def parse_args():
330	    parser = argparse.ArgumentParser(description="Collapse-aware mixing pilot experiment")
331	    parser.add_argument("--output_dir", type=str, default="./output")
332	    parser.add_argument("--num_generations", type=int, default=3)
333	    parser.add_argument("--tokens_per_generation", type=int, default=90_000_000)
334	    parser.add_argument("--checkpoint_interval_tokens", type=int, default=10_000_000)
335	    parser.add_argument("--holdout_size", type=int, default=5_000)
336	    parser.add_argument("--model_name", type=str, default="EleutherAI/pythia-1b")
337	    parser.add_argument("--per_device_batch_size", type=int, default=8)
338	    parser.add_argument("--gradient_accumulation_steps", type=int, default=4)
339	    parser.add_argument("--learning_rate", type=float, default=1e-5)
340	    parser.add_argument("--spectral_num_samples", type=int, default=50_000)
341	    parser.add_argument("--gen_temperature", type=float, default=1.0)
342	    parser.add_argument("--gen_top_p", type=float, default=0.95)
343	    parser.add_argument("--no_wandb", action="store_true")
344	    parser.add_argument("--seed", type=int, default=42)
345	    parser.add_argument("--real_dataset", type=str, default="wikitext")
346	    parser.add_argument("--metrics_gen_tokens", type=int, default=500_000)
347	    return parser.parse_args()
348	
349	
350	def main():
351	    args = parse_args()
352	    config = PilotConfig(
353	        output_dir=args.output_dir,
354	        num_generations=args.num_generations,
355	        tokens_per_generation=args.tokens_per_generation,
356	        checkpoint_interval_tokens=args.checkpoint_interval_tokens,
357	        model_name=args.model_name,
358	        per_device_batch_size=args.per_device_batch_size,
359	        gradient_accumulation_steps=args.gradient_accumulation_steps,
360	        learning_rate=args.learning_rate,
361	        spectral_num_samples=args.spectral_num_samples,
362	        gen_temperature=args.gen_temperature,
363	        gen_top_p=args.gen_top_p,
364	        use_wandb=not args.no_wandb,
365	        seed=args.seed,
366	        real_dataset=args.real_dataset,
367	        metrics_gen_tokens=args.metrics_gen_tokens,
368	        holdout_size=args.holdout_size,
369	    )
370	    run_pilot(config)
371	
372	
373	if __name__ == "__main__":
374	    main()
375	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "60ff85cb-037b-4c00-9e51-254478230283",
  "uuid": "6533feaf-43e7-46a0-9abb-97b2e869f411",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/code/pilot_pipeline.py",
      "content": "\"\"\"End-to-end pilot pipeline: G0 -> gen -> G1 -> gen -> G2 with metrics at every checkpoint.\n\nUsage:\n    python pilot_pipeline.py [--output_dir ./output] [--num_generations 3] [--no_wandb]\n\"\"\"\n\nimport argparse\nimport json\nimport logging\nimport os\nimport sys\nimport time\n\nimport numpy as np\nimport torch\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\n\nfrom config import PilotConfig\nfrom data_utils import (\n    prepare_real_data,\n    prepare_synthetic_data,\n    extract_token_ids,\n    make_dataloader,\n)\nfrom generate import generate_synthetic_data, generate_sample_tokens\nfrom metrics import compute_checkpoint_metrics\nfrom train import train_generation\n\nlogging.basicConfig(\n    level=logging.INFO,\n    format=\"%(asctime)s [%(levelname)s] %(name)s: %(message)s\",\n    handlers=[logging.StreamHandler(sys.stdout)],\n)\nlogger = logging.getLogger(\"pilot\")\n\n\ndef evaluate_checkpoints(\n    checkpoint_paths: list[str],\n    gen_idx: int,\n    holdout_dataset,\n    prev_gen_token_ids: list[int] | None,\n    config: PilotConfig,\n    device: str,\n) -> list[dict]:\n    \"\"\"Load each checkpoint, compute all metrics, return list of metric dicts.\"\"\"\n    tokenizer = AutoTokenizer.from_pretrained(config.model_name)\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n    vocab_size = tokenizer.vocab_size\n\n    holdout_loader = make_dataloader(holdout_dataset, batch_size=config.ppl_batch_size)\n    all_metrics = []\n\n    for ci, ckpt_path in enumerate(checkpoint_paths):\n        logger.info(\"--- Evaluating checkpoint %d/%d: %s ---\", ci + 1, len(checkpoint_paths), ckpt_path)\n        t0 = time.time()\n\n        model = AutoModelForCausalLM.from_pretrained(ckpt_path, torch_dtype=torch.bfloat16).to(device)\n        model.eval()\n\n        # generate a small sample for n-gram / coverage metrics\n        logger.info(\"Generating %dK tokens for corpus metrics ...\", config.metrics_gen_tokens // 1000)\n        gen_ids = generate_sample_tokens(\n            model, tokenizer,\n            num_tokens=config.metrics_gen_tokens,\n            batch_size=config.gen_batch_size,\n            max_new_tokens=256,\n            temperature=config.gen_temperature,\n            top_p=config.gen_top_p,\n            device=device,\n        )\n\n        m = compute_checkpoint_metrics(\n            model=model,\n            holdout_loader=holdout_loader,\n            gen_token_ids=gen_ids,\n            prev_gen_token_ids=prev_gen_token_ids,\n            vocab_size=vocab_size,\n            config=config,\n            device=device,\n        )\n        m[\"generation\"] = gen_idx\n        m[\"checkpoint\"] = ckpt_path\n        m[\"checkpoint_index\"] = ci\n\n        # extract step count from checkpoint dir name\n        step_str = os.path.basename(ckpt_path).split(\"-\")[-1]\n        m[\"global_step\"] = int(step_str) if step_str.isdigit() else ci\n        m[\"tokens_seen\"] = m[\"global_step\"] * config.tokens_per_step\n        m[\"eval_time_sec\"] = time.time() - t0\n\n        all_metrics.append(m)\n        logger.info(\n            \"  eff_rank=%.1f  ppl=%.2f  entropy_var=%.4f  unigram_H=%.3f  coverage=%.4f  (%.0fs)\",\n            m[\"spectral_effective_rank\"], m[\"perplexity\"],\n            m[\"token_entropy_var\"], m[\"unigram_entropy\"],\n            m[\"vocab_coverage\"], m[\"eval_time_sec\"],\n        )\n\n        del model\n        torch.cuda.empty_cache()\n\n    return all_metrics\n\n\ndef save_metrics(metrics: list[dict], path: str):\n    os.makedirs(os.path.dirname(path), exist_ok=True)\n    with open(path, \"a\") as f:\n        for m in metrics:\n            f.write(json.dumps(m, default=str) + \"\\n\")\n    logger.info(\"Metrics appended to %s\", path)\n\n\ndef run_pilot(config: PilotConfig):\n    device = \"cuda\" if torch.cuda.is_available() else \"cpu\"\n    os.makedirs(config.output_dir, exist_ok=True)\n\n    logger.info(\"=\" * 60)\n    logger.info(\"PILOT PIPELINE START\")\n    logger.info(\"  Model: %s\", config.model_name)\n    logger.info(\"  Generations: %d | Tokens/gen: %dM\", config.num_generations, config.tokens_per_generation // 1_000_000)\n    logger.info(\"  Checkpoint interval: %dM tokens (%d steps)\", config.checkpoint_interval_tokens // 1_000_000, config.save_steps)\n    logger.info(\"  Device: %s\", device)\n    logger.info(\"=\" * 60)\n\n    # --- Prepare data ---\n    tokenizer = AutoTokenizer.from_pretrained(config.model_name)\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n\n    logger.info(\"Preparing real data ...\")\n    train_dataset, holdout_dataset = prepare_real_data(config, tokenizer)\n\n    all_results = []\n    prev_gen_token_ids = None\n    prev_model_dir = None  # G0: None → config.model_name; G1+: previous gen's final checkpoint\n    g0_baseline = None  # populated after G0 evaluation\n\n    for g in range(config.num_generations):\n        logger.info(\"=\" * 60)\n        logger.info(\"GENERATION %d / %d\", g, config.num_generations - 1)\n        logger.info(\"=\" * 60)\n\n        # --- Determine training data ---\n        if g == 0:\n            gen_train = train_dataset\n        else:\n            synth_path = config.synthetic_data_path(g - 1)\n            gen_train = prepare_synthetic_data(synth_path, config, tokenizer)\n\n        # --- Train (chain model from previous generation) ---\n        final_model_dir, ckpt_paths = train_generation(\n            gen_idx=g,\n            train_dataset=gen_train,\n            config=config,\n            model_name_or_path=prev_model_dir,\n        )\n\n        # include final model as the last eval point\n        if final_model_dir not in ckpt_paths:\n            ckpt_paths.append(final_model_dir)\n\n        # --- Evaluate all checkpoints ---\n        gen_metrics = evaluate_checkpoints(\n            checkpoint_paths=ckpt_paths,\n            gen_idx=g,\n            holdout_dataset=holdout_dataset,\n            prev_gen_token_ids=prev_gen_token_ids,\n            config=config,\n            device=device,\n        )\n        save_metrics(gen_metrics, config.metrics_path(g))\n        all_results.extend(gen_metrics)\n\n        # --- G0 baseline statistics for leading-indicator threshold ---\n        if g == 0 and gen_metrics:\n            ranks = np.array([m[\"spectral_effective_rank\"] for m in gen_metrics])\n            ppls = np.array([m[\"perplexity\"] for m in gen_metrics])\n            g0_baseline = {\n                \"spectral_rank_mean\": float(ranks.mean()),\n                \"spectral_rank_std\": float(ranks.std()),\n                \"spectral_rank_min\": float(ranks.min()),\n                \"spectral_rank_max\": float(ranks.max()),\n                \"ppl_final\": float(ppls[-1]),\n                \"ppl_mean\": float(ppls.mean()),\n                \"ppl_std\": float(ppls.std()),\n                \"num_checkpoints\": len(gen_metrics),\n            }\n            logger.info(\"G0 BASELINE: rank=%.1f +/- %.2f (sigma for 1-sigma threshold)  ppl_final=%.2f\",\n                         g0_baseline[\"spectral_rank_mean\"], g0_baseline[\"spectral_rank_std\"],\n                         g0_baseline[\"ppl_final\"])\n\n        # --- Generate synthetic data for next generation ---\n        if g < config.num_generations - 1:\n            logger.info(\"Generating synthetic data from G%d for next generation ...\", g)\n            model = AutoModelForCausalLM.from_pretrained(final_model_dir, torch_dtype=torch.bfloat16).to(device)\n            gen_tok = AutoTokenizer.from_pretrained(config.model_name)\n            if gen_tok.pad_token is None:\n                gen_tok.pad_token = gen_tok.eos_token\n\n            generate_synthetic_data(\n                model=model,\n                tokenizer=gen_tok,\n                num_tokens=config.tokens_per_generation,\n                config=config,\n                output_dir=config.synthetic_data_path(g),\n            )\n\n            # save current gen token ids for KL computation in next gen\n            synth_ds = prepare_synthetic_data(config.synthetic_data_path(g), config, gen_tok)\n            prev_gen_token_ids = extract_token_ids(synth_ds, max_tokens=10_000_000)\n\n            del model\n            torch.cuda.empty_cache()\n\n        # chain: next generation initialises from this generation's final model\n        prev_model_dir = final_model_dir\n\n    # --- Summary ---\n    summary = {\n        \"config\": {k: v for k, v in config.__dict__.items() if not k.startswith(\"_\")},\n        \"num_checkpoints_evaluated\": len(all_results),\n        \"g0_baseline\": g0_baseline,\n        \"generations\": {},\n    }\n    for g in range(config.num_generations):\n        gm = [m for m in all_results if m[\"generation\"] == g]\n        if gm:\n            gen_summary = {\n                \"final_spectral_rank\": gm[-1][\"spectral_effective_rank\"],\n                \"final_ppl\": gm[-1][\"perplexity\"],\n                \"spectral_rank_trajectory\": [m[\"spectral_effective_rank\"] for m in gm],\n                \"ppl_trajectory\": [m[\"perplexity\"] for m in gm],\n            }\n            if \"kl_unigram\" in gm[-1]:\n                gen_summary[\"final_kl_unigram\"] = gm[-1][\"kl_unigram\"]\n                gen_summary[\"final_kl_bigram\"] = gm[-1].get(\"kl_bigram\")\n                gen_summary[\"final_kl_ci_95\"] = [gm[-1].get(\"kl_ci_lower_95\"), gm[-1].get(\"kl_ci_upper_95\")]\n            summary[\"generations\"][f\"G{g}\"] = gen_summary\n\n    summary_path = config.summary_path()\n    with open(summary_path, \"w\") as f:\n        json.dump(summary, f, indent=2, default=str)\n    logger.info(\"Summary written to %s\", summary_path)\n\n    # --- MVP GO / NO-GO check (quantitative criteria from ROADMAP) ---\n    if g0_baseline and len(summary[\"generations\"]) >= 2:\n        sigma = g0_baseline[\"spectral_rank_std\"]\n        g0_rank_mean = g0_baseline[\"spectral_rank_mean\"]\n        g0_ppl = g0_baseline[\"ppl_final\"]\n        rank_threshold = g0_rank_mean - sigma  # drop >= 1 sigma\n\n        # PPL significance: >= 2 pts absolute OR >= 5% relative\n        ppl_abs_threshold = g0_ppl + 2.0\n        ppl_rel_threshold = g0_ppl * 1.05\n\n        # Scan all post-G0 checkpoints for the leading indicator pattern:\n        # find first checkpoint where rank drops >= 1 sigma below G0 mean\n        # and check whether PPL has NOT yet risen significantly at that point\n        first_rank_drop_idx = None\n        first_ppl_rise_idx = None\n\n        post_g0 = [m for m in all_results if m[\"generation\"] > 0]\n        for i, m in enumerate(post_g0):\n            if first_rank_drop_idx is None and m[\"spectral_effective_rank\"] <= rank_threshold:\n                first_rank_drop_idx = i\n            if first_ppl_rise_idx is None and (m[\"perplexity\"] >= ppl_abs_threshold or m[\"perplexity\"] >= ppl_rel_threshold):\n                first_ppl_rise_idx = i\n\n        # KL check (on final generation boundary)\n        last_gen_metrics = [m for m in all_results if m[\"generation\"] == config.num_generations - 1]\n        kl_value = last_gen_metrics[-1].get(\"kl_unigram\", 0) if last_gen_metrics else 0\n        kl_ci = (last_gen_metrics[-1].get(\"kl_ci_lower_95\", 0), last_gen_metrics[-1].get(\"kl_ci_upper_95\", 0)) if last_gen_metrics else (0, 0)\n\n        spectral_leads = (first_rank_drop_idx is not None and\n                          (first_ppl_rise_idx is None or first_rank_drop_idx < first_ppl_rise_idx))\n        kl_above_threshold = kl_value > 0.1\n\n        logger.info(\"=\" * 60)\n        logger.info(\"MVP GO / NO-GO CHECK\")\n        logger.info(\"  G0 baseline: rank=%.1f +/- %.2f (1-sigma threshold=%.1f)  ppl=%.2f\",\n                     g0_rank_mean, sigma, rank_threshold, g0_ppl)\n        logger.info(\"  PPL significance: >= %.2f (abs +2) OR >= %.2f (rel +5%%)\",\n                     ppl_abs_threshold, ppl_rel_threshold)\n        logger.info(\"  First rank drop (>= 1 sigma): %s\",\n                     f\"checkpoint {first_rank_drop_idx}\" if first_rank_drop_idx is not None else \"NOT DETECTED\")\n        logger.info(\"  First PPL rise (significant): %s\",\n                     f\"checkpoint {first_ppl_rise_idx}\" if first_ppl_rise_idx is not None else \"NOT DETECTED\")\n        logger.info(\"  Spectral leads PPL: %s\", spectral_leads)\n        logger.info(\"  KL divergence: %.4f  (95%% CI: [%.4f, %.4f])  threshold 0.1: %s\",\n                     kl_value, kl_ci[0], kl_ci[1], \"PASS\" if kl_above_threshold else \"FAIL\")\n\n        if spectral_leads and kl_above_threshold:\n            verdict = \"GO — spectral rank is a leading indicator, KL confirms non-stationarity\"\n        elif first_rank_drop_idx is not None and first_ppl_rise_idx is not None and first_rank_drop_idx == first_ppl_rise_idx:\n            verdict = \"CONDITIONAL GO — spectral and PPL drop simultaneously, check granularity advantage\"\n        elif kl_value < 0.1 and (first_rank_drop_idx is not None or first_ppl_rise_idx is not None):\n            verdict = \"EXTEND — KL below threshold but collapse signals detected, add generation to accumulate KL\"\n        elif first_rank_drop_idx is None and first_ppl_rise_idx is not None:\n            verdict = \"KILL — PPL rose but spectral rank did not drop, indicator ineffective for autoregressive LM collapse\"\n        elif first_rank_drop_idx is None and first_ppl_rise_idx is None:\n            verdict = \"EXTEND — neither spectral rank nor PPL moved in 2 generations, add generation to trigger collapse\"\n        else:\n            verdict = \"INCONCLUSIVE — review trajectories manually\"\n\n        logger.info(\"  VERDICT: %s\", verdict)\n        logger.info(\"=\" * 60)\n\n        summary[\"mvp_check\"] = {\n            \"g0_rank_mean\": g0_rank_mean,\n            \"g0_rank_std\": sigma,\n            \"rank_threshold_1sigma\": rank_threshold,\n            \"ppl_threshold_abs\": ppl_abs_threshold,\n            \"ppl_threshold_rel\": ppl_rel_threshold,\n            \"first_rank_drop_checkpoint\": first_rank_drop_idx,\n            \"first_ppl_rise_checkpoint\": first_ppl_rise_idx,\n            \"spectral_leads\": spectral_leads,\n            \"kl_unigram\": kl_value,\n            \"kl_ci_95\": list(kl_ci),\n            \"kl_above_0_1\": kl_above_threshold,\n            \"verdict\": verdict,\n        }\n        with open(summary_path, \"w\") as f:\n            json.dump(summary, f, indent=2, default=str)\n\n    return all_results\n\n\ndef parse_args():\n    parser = argparse.ArgumentParser(description=\"Collapse-aware mixing pilot experiment\")\n    parser.add_argument(\"--output_dir\", type=str, default=\"./output\")\n    parser.add_argument(\"--num_generations\", type=int, default=3)\n    parser.add_argument(\"--tokens_per_generation\", type=int, default=90_000_000)\n    parser.add_argument(\"--checkpoint_interval_tokens\", type=int, default=10_000_000)\n    parser.add_argument(\"--holdout_size\", type=int, default=5_000)\n    parser.add_argument(\"--model_name\", type=str, default=\"EleutherAI/pythia-1b\")\n    parser.add_argument(\"--per_device_batch_size\", type=int, default=8)\n    parser.add_argument(\"--gradient_accumulation_steps\", type=int, default=4)\n    parser.add_argument(\"--learning_rate\", type=float, default=1e-5)\n    parser.add_argument(\"--spectral_num_samples\", type=int, default=50_000)\n    parser.add_argument(\"--gen_temperature\", type=float, default=1.0)\n    parser.add_argument(\"--gen_top_p\", type=float, default=0.95)\n    parser.add_argument(\"--no_wandb\", action=\"store_true\")\n    parser.add_argument(\"--seed\", type=int, default=42)\n    parser.add_argument(\"--real_dataset\", type=str, default=\"wikitext\")\n    parser.add_argument(\"--metrics_gen_tokens\", type=int, default=500_000)\n    return parser.parse_args()\n\n\ndef main():\n    args = parse_args()\n    config = PilotConfig(\n        output_dir=args.output_dir,\n        num_generations=args.num_generations,\n        tokens_per_generation=args.tokens_per_generation,\n        checkpoint_interval_tokens=args.checkpoint_interval_tokens,\n        model_name=args.model_name,\n        per_device_batch_size=args.per_device_batch_size,\n        gradient_accumulation_steps=args.gradient_accumulation_steps,\n        learning_rate=args.learning_rate,\n        spectral_num_samples=args.spectral_num_samples,\n        gen_temperature=args.gen_temperature,\n        gen_top_p=args.gen_top_p,\n        use_wandb=not args.no_wandb,\n        seed=args.seed,\n        real_dataset=args.real_dataset,\n        metrics_gen_tokens=args.metrics_gen_tokens,\n        holdout_size=args.holdout_size,\n    )\n    run_pilot(config)\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 375,
      "startLine": 1,
      "totalLines": 375
    }
  }
}
```

</details>

---

### Assistant

_source line 42_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of all the existing code. Let me write the `controlled_pipeline.py` file. Here's my plan:

1. **MixedDataset**: A dataset that dynamically samples from real and synthetic datasets based on a ratio `w_t`. The ratio can be updated during training.

2. **Control loop**: Instead of using HF Trainer's save_steps callback, I'll split training into segments. Each segment trains for `save_steps` steps. After each segment:
   - Save a checkpoint
   - Compute spectral effective rank
   - Call PI controller.step(rank) to get new w_t
   - Update the MixedDataset's ratio
   - Log to control_log.jsonl

3. **Training approach**: I'll use a manual training loop with AdamW optimizer and a linear warmup schedule rather than multiple Trainer calls or callbacks, since this gives me full control over when to pause and update mixing ratios.

4. **Command line interface**: Setting up argparse with the necessary parameters...

Now I'm designing the MixedDataset class that samples from real and synthetic data based on a configurable weight...

Completing the sampling logic...

I see the issue though—using a standard DataLoader with sequential indices would ignore the actual index passed to `__getitem__`, which works fine for random sampling during training but feels a bit off. A cleaner approach would be to use a custom sampler or let the DataLoader handle shuffling naturally while the dataset probabilistically picks from either source each time it's called.

Actually, I think the real problem is that I'm overcomplicating this. The simplest solution is to create a MixedDataset that takes both the real and synthetic datasets, and for each sample independently decides whether to draw from one source or the other based on the current weight. I can seed the random generator per index for reproducibility, so the same index always produces the same choice across epochs if needed. mixing and the ratio is what matters, not exact sample selection. Looking at the requirements again, the key point is that w_t needs to be dynamically updated during training. I'll implement MixedDataset with a settable weight parameter, then structure the training loop to run in segments—training for a fixed number of steps, saving checkpoints, computing the effective rank, and updating w_t based on the controller's decision before moving to the next segment.

For the DataLoader, I need to handle the fact that after iterating through all samples, I'll need to reset it. With a manual training loop, I can create an infinite iterator that cycles through the dataset. Since each __getitem__ call samples independently based on w, updating the dataset's w attribute will take effect immediately on the next batch.

Writing the implementation... Setting up the imports and logging configuration...

Now I'm defining a MixedDataset class that dynamically blends real and synthetic data during training, allowing the sampling ratio to be adjusted on the fly without recreating the dataloader.

I'm also setting up an infinite dataloader wrapper that cycles through batches continuously, and starting to define the main training loop function that handles gradient accumulation and optimization steps.

Still writing training logic... Writing the training pipeline... Loading the model and tokenizer now, setting up the device with bfloat16 precision and SDPA attention, then enabling gradient checkpointing if configured.

Now I'm setting up the optimizer with AdamW and a linear warmup scheduler, then creating a mixed dataset that combines real and synthetic data with the controller's initial weight, and wrapping it in a DataLoader with shuffling and pinned memory.

I'm wrapping the loader in an infinite iterator, then setting up separate dataloaders for perplexity evaluation and spectral rank analysis using the holdout dataset. Now I'm entering the main training loop across segments, logging the current segment progress and weight values before starting the timing.

Now I'm running the training step for this segment, tracking the average loss and steps completed, then saving a checkpoint at the current global step. After that, I'm computing the spectral effective rank of the model using the spectral loader.

Next I'm calculating perplexity on the holdout set, then using those metrics to step the PI controller forward, which gives me a new mixing weight for the dataset. I'm logging all these metrics—generation index, segment number, global step—along with the performance measurements. Writing the pipeline setup... I'm loading the real training data and setting up a collapse-aware controller, then iterating through generations where the first generation trains on real data only using the standard training pipeline, while subsequent generations will load and mix synthetic data.

For generations after the first, I'm preparing the synthetic dataset from the previous generation, resetting the controller state, and running a controlled generation process that combines real and synthetic data. Then if there are more generations to come, I'll generate new synthetic data for the next iteration. I'm realizing I need to reconsider the design based on the requirements. G0 should use only real data as a baseline, while G1 and beyond should mix real and synthetic data with PI control to maintain quality. The PI controller shouldn't run for G0 since that's the pure real-data baseline. training. The PI controller starts at G1 where we have both real and synthetic data.

But wait, should the spectral rank measurement also happen during G0? The user's requirements say "每个 checkpoint 后: 计算当前 batch 的 spectral effective rank" - so this suggests for every generation. But the PI controller only makes sense when we have mixed data to control.

I think the clean design is:
- G0: Train on real data using standard `train_generation` from train.py. No mixing, no PI control.
- G1+: Train using controlled mixing with PI controller.

Actually, re-reading the requirements again: "把每代的训练拆成多个 segment（每个 segment = checkpoint_interval_tokens）" and "每个 segment 结束时：保存 checkpoint → 计算 eff_rank → PI controller.step(eff_rank) → 更新 w_t → 下个 segment 用新 w_t" - this suggests segment-based training with PI control happens for every generation. But for G0 with only real data, there's nothing to mix, so I'll keep w_t at 1.0 throughout. G1+ will use the controlled mixing approach.

Now I'm wondering whether to reset the controller between generations. Since each generation starts from the previous model's final state but the rank values will shift, resetting makes sense to avoid stale integral error. Though there's an argument for letting the controller accumulate error across generations if the user wants continuity in the control signal.

I'm also thinking through how the MixedDataset works with the DataLoader's shuffling. The DataLoader generates random indices, and then `__getitem__` independently decides whether to return a real or synthetic sample using `torch.rand()`. This means the mixing ratio is correct in expectation, even though the index itself doesn't directly control the real/synthetic choice. When the DataLoader starts a new epoch, the `_infinite_dataloader` restarts it, and since `__len__` returns `max(len(real), len(synthetic))`, this controls how many samples we see per epoch.

Now I'm checking the G0 setup — the user's design specifies that G0 trains only on real data, and looking at the pilot_pipeline.py, G0 uses `train_generation` which runs the HF Trainer on the real dataset.

For G1 and beyond, I'll implement the controlled generation with a manual training loop instead.

I need to make sure I'm importing `generate_synthetic_data` from `generate.py` the same way the pilot_pipeline does.

Re-reading the spec about segmenting each generation into chunks — I think this applies specifically to the generations with mixed data (G1+), not G0. G0 is just the baseline on real data alone. The segmentation with PI control is for managing the synthetic-to-real ratio in later generations.

For G0, standard training makes more sense than trying to force it into the controlled pipeline with dummy synthetic data. Then for G1+, I'll generate synthetic data from the previous generation and feed it into the controlled training loop with the PI controller adjusting the mixing ratio at each checkpoint.

Now I need to think through the implementation details—particularly around gradient checkpointing and mixed precision training, since those can interact in subtle ways with the manual training loop I'm setting up. Setting up the autocast context...

Now I'm laying out the full pipeline structure with the dataset class, training loop, checkpoint saving, generation control, and the main orchestration function.

I need to be careful about how the controller initializes—on the first step it returns the initial weight unchanged to establish a baseline, then subsequent calls apply the actual control logic. So segment 0 trains with the initial weight, we measure rank, call the controller which returns that same weight, and segment 1 trains with it again before the control adjustments kick in.

Writing the full implementation... I'm seeding the controller with an initial rank measurement before training starts, so it can actively control from segment zero onward rather than wasting the first segment. Now I need to clarify the data mixing logic: w_t represents the real data ratio, so when the controller increases w due to rank drops, we sample more real data to prevent collapse, and when rank is stable we can use more synthetic data. Let me write out the complete implementation.

For G0 specifically, I'll use pure real data training since that's what the requirements specify, then generate synthetic data from G0's final model for G1 onwards. I need to import the synthetic data generation function from the existing pipeline and make sure all the pieces connect properly.

Now I'm deciding between a manual training loop versus multiple Trainer calls for handling the mixing ratio updates between checkpoints — the requirements explicitly forbid using HF Trainer's save_steps callback, so I need to implement this carefully.

A manual loop gives me more explicit control over when to pause and update the mixing ratios, which is cleaner than trying to reinitialize the optimizer with multiple Trainer calls. I'll go with the manual approach and handle mixed precision with `torch.amp.autocast` to ensure bf16 operations stay consistent even when the model weights are already in bf16.

Writing the training pipeline... I'm defining a MixedDataset class that blends real and synthetic data during training, allowing the mixing ratio to be adjusted dynamically between segments without needing to recreate the dataloader—each sample is randomly drawn from either dataset based on the current weight.

Setting up utility functions...

Now I'm defining the main training loop that orchestrates one generation of the controlled mixing process, establishing directories for checkpoints and logs, then calculating how to divide the training into segments with periodic saves.

Loading the tokenizer and model with optimizations like bfloat16 precision and SDPA attention, then setting up the optimizer and learning rate scheduler...

Setting up the data pipeline with mixed real and synthetic datasets, creating data loaders for training and evaluation with appropriate batch sizes and worker configurations.

Now I'm initializing the controller by computing the model's spectral effective rank on a holdout set, then seeding it so the weighting mechanism is active from the start of training. Then I'll iterate through training segments, updating the dataset ratio based on the controller's current weight and logging progress before each segment begins.

Training the segment... Writing evaluation metrics... Setting up the controlled pipeline with device detection and output directories, then logging the configuration details including model specs, generation parameters, and PI controller settings.

Loading the tokenizer and preparing the real training data, then iterating through each generation where G0 trains on real data without mixing...

For subsequent generations, I'm loading synthetic data from the previous generation and running controlled generation with a collapse-aware controller to blend real and synthetic datasets, storing the model directory for the next iteration.

Now I'm setting up the synthetic data generation pipeline for the next generation—loading the trained model with bfloat16 precision, preparing the tokenizer, and generating new synthetic data before cleaning up memory.

Setting up argument parser... Setting up the config objects...

Now I'm verifying the implementation against the requirements: checking that the logging format matches the expected JSON structure with generation, segment, step, and controller metrics, confirming the CLI arguments align with the specification, ensuring I'm importing from existing modules without modifications, validating that the dataset handles dynamic weight updates, and confirming the training loop is implemented manually rather than relying on Hugging Face's trainer.

The control flow looks right—training a segment, checkpointing, computing effective rank, stepping the controller, and updating the weight for the next iteration. One thing I want to verify: when I log an entry after the controller step, the `w_t` value should reflect the new weight that will be used in the subsequent segment, not the one that was just used. Looking at my implementation, I'm correctly capturing the updated weight from the controller step before logging it, so that's consistent with the spec.

I'm also thinking through some edge cases: if the total tokens don't divide evenly by the checkpoint interval, the integer division will floor the step count, which matches how the existing pipeline handles it. For a single generation, we'd just train on real data without any mixing, which is fine. As for logging, the control_log.jsonl file serves as the record of the training dynamics, and wandb integration isn't part of the spec for this controlled pipeline.

I'm also noticing the manual training loop doesn't include early stopping logic like the pilot pipeline does, which I should consider whether to add.

Now I'm reconsidering the `torch.amp.autocast` setup more carefully. When loading the model in bf16, the optimizer states end up in bf16 too, which can hurt numerical stability—ideally they'd stay in fp32. The HF Trainer sidesteps this by using autocast while keeping model weights in fp32, letting the optimizer maintain higher precision states.

For a shorter training run though, bf16 optimizer states should work fine in practice. I could load in fp32 with autocast for the forward pass, but since the existing code uses `torch_dtype=torch.bfloat16` and `bf16=True` in TrainingArguments, I'll match that approach and wrap the forward pass with autocast.

Setting up the autocast context... I'm verifying the controller's `_w` attribute access — I could use `get_state()` to retrieve it, but since the controller is straightforward and part of our codebase, directly accessing `_w` is simpler and more efficient. I'm restructuring the loop to make the flow clearer: initialize w before the loop, then in each iteration set the dataset ratio, train, measure rank, and update w from the controller's step function, which returns the new weight directly.

Let me verify the logic once more—after seeding the controller with the initial rank, each subsequent step call will compute the rank delta from the previous measurement and apply the control law, which is exactly what we need.

Writing the implementation... After seeding, the controller's step count stays at 0 while the history buffers capture the initial state, so `get_state()` will correctly reflect that no control steps have executed yet. The user spec doesn't explicitly mention seeding, but initializing with the first rank makes the controller more responsive from the start, so I'll include it with a clarifying comment. Now I'm ready to write the implementation.

For the CLI defaults, the spec example shows `--r_target 680` and `--tokens_per_generation 20000000`, so I'll use those as the argparse defaults instead of the placeholder values in the config classes. Writing the controlled training pipeline code now...

Setting up imports and module docstring... Setting up utility functions for the training pipeline...

Now I'm defining the main training function that orchestrates one generation of the controlled mixing process, splitting training into segments where I'll checkpoint, measure spectral rank, and adjust the real/synthetic ratio using PI control.

Setting up the model and tokenizer...

Now I'm configuring the optimizer with AdamW and a linear warmup schedule, initializing the controller for managing the mixed dataset, and preparing the data loader with both real and synthetic samples.

I'm also setting up separate loaders for evaluation and spectral analysis, then computing the initial spectral effective rank on the model to seed the controller's state before training begins.

Now I'm logging that initial rank value and starting the main training loop, where I'll iterate through segments, adjusting the data mixing ratio and running gradient accumulation steps for each batch. Finishing the logging statement, then I'm saving a checkpoint and computing the spectral effective rank and perplexity metrics to evaluate how the model's learned representations are evolving during training. Saving the final model checkpoint and clearing GPU memory, then setting up the multi-generation pipeline with PI control that runs G0 on real data and subsequent generations with adaptive mixing based on the controller's output. For the first generation, I'm training from scratch on the real data, but for subsequent generations, I load synthetic data from the previous iteration and run controlled generation to create new training examples while keeping the model grounded in the real dataset.

If there are more generations to run, I load the trained model and generate synthetic data from it to use in the next iteration, making sure the tokenizer is properly configured before generation.

After that, I clear the GPU cache and move on to the next generation cycle. Once all generations are complete, the pipeline logs that it's finished. Then I'm setting up the argument parser for the script, defining all the configuration options like output directory, number of generations, tokens per generation, batch size, and other training hyperparameters.

Continuing with the argument parser...

Now I'm instantiating the PilotConfig with all the parsed arguments, then setting up a ControllerConfig with the PID controller parameters, and finally calling the pipeline with both configurations. I'm checking the style requirements against the spec—the task asks for file docstrings and comments explaining non-obvious logic, so I need to add a note about why we seed the controller and make sure the file header is clear. The training loop and dataset sampling are straightforward enough, but the controller initialization warrants explanation since it's a key part of the controlled generation design.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "60ff85cb-037b-4c00-9e51-254478230283",
  "uuid": "22a88c14-52aa-4aaa-b54e-03f2eb607b7d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XMyjFn8W8HZ1vdNzvivtAt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16699,
      "cache_read_input_tokens": 26869,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16699
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

_source line 43_

Now I have all the interfaces. Writing `controlled_pipeline.py`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "60ff85cb-037b-4c00-9e51-254478230283",
  "uuid": "61b940e9-2f8a-4c9b-9ec8-beb2e9ddf8b9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XMyjFn8W8HZ1vdNzvivtAt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16699,
      "cache_read_input_tokens": 26869,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16699
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

_source line 44_

<details open><summary>🔧 Tool call — Write · `toolu_01FUo83sX9JPytJAkrD5HtiM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/code/controlled_pipeline.py",
  "content": "\"\"\"Controlled training pipeline with PI-based collapse-aware data mixing.\n\nTrains a language model across multiple generations. G0 trains on real data\n(via train.py). G1+ uses a PI controller to dynamically adjust the\nreal/synthetic data mixing ratio w_t based on spectral effective rank\nmeasured at each checkpoint boundary.\n\nInput:\n  - Real data: WikiText (via data_utils.prepare_real_data)\n  - Synthetic data: generated from previous generation's model\nOutput:\n  - Trained models at &lt;output_dir>/G{i}/final_model/\n  - control_log.jsonl with per-segment controller state and metrics\n\nDependencies: controller.py, metrics.py, data_utils.py, config.py, train.py, generate.py\n\nUsage:\n    python controlled_pipeline.py \\\n      --output_dir /root/autodl-tmp/output_controlled/ \\\n      --num_generations 3 \\\n      --tokens_per_generation 20000000 \\\n      --Kp 0.01 --Ki 0.005 \\\n      --r_target 680 \\\n      --w_init 0.5\n\"\"\"\n\nimport argparse\nimport json\nimport logging\nimport os\nimport sys\nimport time\n\nimport torch\nfrom torch.utils.data import Dataset as TorchDataset, DataLoader\nfrom transformers import (\n    AutoModelForCausalLM,\n    AutoTokenizer,\n    get_linear_schedule_with_warmup,\n)\n\nfrom config import PilotConfig\nfrom controller import CollapseAwareController, ControllerConfig\nfrom data_utils import (\n    PackedDataset,\n    prepare_real_data,\n    prepare_synthetic_data,\n    make_dataloader,\n)\nfrom metrics import compute_spectral_effective_rank, compute_perplexity\n\nlogging.basicConfig(\n    level=logging.INFO,\n    format=\"%(asctime)s [%(levelname)s] %(name)s: %(message)s\",\n    handlers=[logging.StreamHandler(sys.stdout)],\n)\nlogger = logging.getLogger(\"controlled_pipeline\")\n\n\n# ---------------------------------------------------------------------------\n# Online data mixing\n# ---------------------------------------------------------------------------\n\nclass MixedDataset(TorchDataset):\n    \"\"\"Online real/synthetic mixing with dynamically adjustable ratio.\n\n    Each sample is independently drawn from real_dataset with probability w,\n    or from synthetic_dataset with probability (1 - w). Call set_ratio()\n    between training segments to update w without rebuilding the dataloader.\n    \"\"\"\n\n    def __init__(\n        self,\n        real_dataset: PackedDataset,\n        synthetic_dataset: PackedDataset,\n        w: float = 0.5,\n    ):\n        self.real = real_dataset\n        self.synthetic = synthetic_dataset\n        self.w = w\n\n    def set_ratio(self, w: float):\n        self.w = w\n\n    def __len__(self):\n        return max(len(self.real), len(self.synthetic))\n\n    def __getitem__(self, idx):\n        if torch.rand(1).item() < self.w:\n            return self.real[idx % len(self.real)]\n        return self.synthetic[idx % len(self.synthetic)]\n\n\n# ---------------------------------------------------------------------------\n# Helpers\n# ---------------------------------------------------------------------------\n\ndef _infinite_loader(loader: DataLoader):\n    \"\"\"Yield batches indefinitely by cycling through the loader.\"\"\"\n    while True:\n        yield from loader\n\n\ndef _save_checkpoint(model, tokenizer, path: str):\n    os.makedirs(path, exist_ok=True)\n    model.save_pretrained(path)\n    tokenizer.save_pretrained(path)\n\n\ndef _append_jsonl(path: str, entry: dict):\n    os.makedirs(os.path.dirname(path) or \".\", exist_ok=True)\n    with open(path, \"a\") as f:\n        f.write(json.dumps(entry, default=str) + \"\\n\")\n\n\n# ---------------------------------------------------------------------------\n# Controlled generation (manual training loop + PI control)\n# ---------------------------------------------------------------------------\n\ndef run_controlled_generation(\n    gen_idx: int,\n    real_dataset: PackedDataset,\n    synthetic_dataset: PackedDataset,\n    holdout_dataset: PackedDataset,\n    config: PilotConfig,\n    ctrl_config: ControllerConfig,\n    model_name_or_path: str,\n    device: str,\n) -> str:\n    \"\"\"Train one generation with PI-controlled real/synthetic mixing.\n\n    Training is split into segments of config.save_steps optimizer steps.\n    After each segment: save checkpoint -> measure spectral effective rank\n    -> PI controller step -> update mixing ratio for next segment.\n\n    Uses a manual training loop (not HF Trainer) to allow pausing between\n    segments for metric computation and ratio updates.\n\n    Returns path to the final model directory.\n    \"\"\"\n    gen_dir = config.gen_dir(gen_idx)\n    training_dir = os.path.join(gen_dir, \"training\")\n    final_dir = os.path.join(gen_dir, \"final_model\")\n    log_path = os.path.join(config.output_dir, \"control_log.jsonl\")\n\n    num_segments = config.max_steps // config.save_steps\n    steps_per_seg = config.save_steps\n\n    logger.info(\"=== Generation %d: %d segments x %d steps (total %d) ===\",\n                gen_idx, num_segments, steps_per_seg, config.max_steps)\n\n    # --- Model ---\n    tokenizer = AutoTokenizer.from_pretrained(model_name_or_path)\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n\n    model = AutoModelForCausalLM.from_pretrained(\n        model_name_or_path,\n        torch_dtype=torch.bfloat16,\n        attn_implementation=\"sdpa\",\n    ).to(device)\n\n    if config.gradient_checkpointing:\n        model.gradient_checkpointing_enable(\n            gradient_checkpointing_kwargs={\"use_reentrant\": False}\n        )\n\n    # --- Optimizer & scheduler (mirrors train.py's Trainer setup) ---\n    optimizer = torch.optim.AdamW(\n        model.parameters(),\n        lr=config.learning_rate,\n        weight_decay=config.weight_decay,\n    )\n    warmup_steps = int(config.max_steps * config.warmup_ratio)\n    scheduler = get_linear_schedule_with_warmup(\n        optimizer,\n        num_warmup_steps=warmup_steps,\n        num_training_steps=config.max_steps,\n    )\n\n    # --- Controller ---\n    controller = CollapseAwareController(ctrl_config)\n\n    # --- Data ---\n    mixed_ds = MixedDataset(real_dataset, synthetic_dataset, w=ctrl_config.w_init)\n    loader = DataLoader(\n        mixed_ds,\n        batch_size=config.per_device_batch_size,\n        shuffle=True,\n        num_workers=2,\n        pin_memory=True,\n    )\n    data_iter = _infinite_loader(loader)\n\n    holdout_loader = make_dataloader(holdout_dataset, batch_size=config.ppl_batch_size)\n    spectral_loader = make_dataloader(holdout_dataset, batch_size=config.spectral_batch_size)\n\n    # Seed controller with initial rank so the first post-segment step\n    # produces an actual control action (not just the baseline return).\n    model.eval()\n    init_rank = compute_spectral_effective_rank(\n        model, spectral_loader,\n        num_samples=config.spectral_num_samples, device=device,\n    )[\"spectral_effective_rank\"]\n    controller.step(init_rank)\n    logger.info(\"  Initial eff_rank=%.1f\", init_rank)\n\n    w_t = ctrl_config.w_init\n    global_step = 0\n\n    for seg in range(num_segments):\n        mixed_ds.set_ratio(w_t)\n\n        logger.info(\"--- Seg %d/%d | w=%.4f | steps %d->%d ---\",\n                    seg, num_segments - 1, w_t,\n                    global_step, global_step + steps_per_seg)\n\n        # --- Train one segment ---\n        model.train()\n        t0 = time.time()\n        seg_loss = 0.0\n\n        for step_in_seg in range(steps_per_seg):\n            optimizer.zero_grad()\n            accum_loss = 0.0\n\n            for _ in range(config.gradient_accumulation_steps):\n                batch = next(data_iter)\n                input_ids = batch[\"input_ids\"].to(device)\n                attention_mask = batch[\"attention_mask\"].to(device)\n                labels = batch[\"labels\"].to(device)\n\n                with torch.amp.autocast(\"cuda\", dtype=torch.bfloat16):\n                    loss = model(\n                        input_ids=input_ids,\n                        attention_mask=attention_mask,\n                        labels=labels,\n                    ).loss / config.gradient_accumulation_steps\n\n                loss.backward()\n                accum_loss += loss.item()\n\n            torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)\n            optimizer.step()\n            scheduler.step()\n            seg_loss += accum_loss\n\n            cur_step = global_step + step_in_seg + 1\n            if cur_step % 50 == 0:\n                logger.info(\"  step %d | loss %.4f | lr %.2e\",\n                            cur_step, accum_loss, scheduler.get_last_lr()[0])\n\n        global_step += steps_per_seg\n        avg_loss = seg_loss / steps_per_seg\n\n        # --- Checkpoint ---\n        ckpt_path = os.path.join(training_dir, f\"checkpoint-{global_step}\")\n        _save_checkpoint(model, tokenizer, ckpt_path)\n\n        # --- Measure spectral rank & perplexity ---\n        model.eval()\n        eff_rank = compute_spectral_effective_rank(\n            model, spectral_loader,\n            num_samples=config.spectral_num_samples, device=device,\n        )[\"spectral_effective_rank\"]\n\n        ppl = compute_perplexity(\n            model, holdout_loader,\n            num_samples=config.ppl_num_samples, device=device,\n        )[\"perplexity\"]\n\n        # --- PI controller step ---\n        w_t = controller.step(eff_rank)\n        state = controller.get_state()\n\n        entry = {\n            \"generation\": gen_idx,\n            \"segment\": seg,\n            \"step\": global_step,\n            \"eff_rank\": round(eff_rank, 2),\n            \"w_t\": round(w_t, 4),\n            \"ppl\": round(ppl, 2),\n            \"proportional\": round(state[\"proportional_term\"], 6),\n            \"integral\": round(state[\"integral_term\"], 6),\n        }\n        _append_jsonl(log_path, entry)\n\n        logger.info(\"  rank=%.1f | w_t=%.4f | ppl=%.2f (%.0fs)\",\n                    eff_rank, w_t, ppl, time.time() - t0)\n\n    # --- Save final model ---\n    _save_checkpoint(model, tokenizer, final_dir)\n    logger.info(\"Final model -> %s\", final_dir)\n\n    del model\n    torch.cuda.empty_cache()\n    return final_dir\n\n\n# ---------------------------------------------------------------------------\n# Multi-generation orchestrator\n# ---------------------------------------------------------------------------\n\ndef run_controlled_pipeline(config: PilotConfig, ctrl_config: ControllerConfig):\n    \"\"\"Multi-generation pipeline: G0 on real data, G1+ with PI-controlled mixing.\"\"\"\n    device = \"cuda\" if torch.cuda.is_available() else \"cpu\"\n    os.makedirs(config.output_dir, exist_ok=True)\n\n    logger.info(\"=\" * 60)\n    logger.info(\"CONTROLLED PIPELINE\")\n    logger.info(\"  Model: %s | Gens: %d | Tokens/gen: %dM\",\n                config.model_name, config.num_generations,\n                config.tokens_per_generation // 1_000_000)\n    logger.info(\"  PI: Kp=%.4f Ki=%.4f r_target=%.1f w=[%.2f, %.2f, %.2f]\",\n                ctrl_config.Kp, ctrl_config.Ki, ctrl_config.r_target,\n                ctrl_config.w_min, ctrl_config.w_init, ctrl_config.w_max)\n    logger.info(\"=\" * 60)\n\n    tokenizer = AutoTokenizer.from_pretrained(config.model_name)\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n\n    real_train, holdout = prepare_real_data(config, tokenizer)\n    prev_model_dir: str | None = None\n\n    for g in range(config.num_generations):\n        logger.info(\"=\" * 60)\n        logger.info(\"GENERATION %d / %d\", g, config.num_generations - 1)\n        logger.info(\"=\" * 60)\n\n        if g == 0:\n            # G0: standard training on real data only (no mixing needed)\n            from train import train_generation\n            final_dir, _ = train_generation(\n                gen_idx=g,\n                train_dataset=real_train,\n                config=config,\n            )\n        else:\n            synth_path = config.synthetic_data_path(g - 1)\n            synthetic = prepare_synthetic_data(synth_path, config, tokenizer)\n\n            final_dir = run_controlled_generation(\n                gen_idx=g,\n                real_dataset=real_train,\n                synthetic_dataset=synthetic,\n                holdout_dataset=holdout,\n                config=config,\n                ctrl_config=ctrl_config,\n                model_name_or_path=prev_model_dir or config.model_name,\n                device=device,\n            )\n\n        # Generate synthetic data for next generation\n        if g < config.num_generations - 1:\n            logger.info(\"Generating synthetic data from G%d ...\", g)\n            from generate import generate_synthetic_data\n            gen_model = AutoModelForCausalLM.from_pretrained(\n                final_dir, torch_dtype=torch.bfloat16\n            ).to(device)\n            gen_tok = AutoTokenizer.from_pretrained(config.model_name)\n            if gen_tok.pad_token is None:\n                gen_tok.pad_token = gen_tok.eos_token\n\n            generate_synthetic_data(\n                model=gen_model,\n                tokenizer=gen_tok,\n                num_tokens=config.tokens_per_generation,\n                config=config,\n                output_dir=config.synthetic_data_path(g),\n            )\n            del gen_model\n            torch.cuda.empty_cache()\n\n        prev_model_dir = final_dir\n\n    logger.info(\"CONTROLLED PIPELINE COMPLETE\")\n\n\n# ---------------------------------------------------------------------------\n# CLI\n# ---------------------------------------------------------------------------\n\ndef parse_args():\n    p = argparse.ArgumentParser(\n        description=\"PI-controlled collapse-aware training pipeline\"\n    )\n    # PilotConfig overrides\n    p.add_argument(\"--output_dir\", type=str, default=\"./output_controlled\")\n    p.add_argument(\"--num_generations\", type=int, default=3)\n    p.add_argument(\"--tokens_per_generation\", type=int, default=20_000_000)\n    p.add_argument(\"--checkpoint_interval_tokens\", type=int, default=10_000_000)\n    p.add_argument(\"--model_name\", type=str, default=\"EleutherAI/pythia-1b\")\n    p.add_argument(\"--per_device_batch_size\", type=int, default=8)\n    p.add_argument(\"--gradient_accumulation_steps\", type=int, default=4)\n    p.add_argument(\"--learning_rate\", type=float, default=2e-6)\n    p.add_argument(\"--no_wandb\", action=\"store_true\")\n    p.add_argument(\"--seed\", type=int, default=42)\n    # ControllerConfig\n    p.add_argument(\"--Kp\", type=float, default=0.01)\n    p.add_argument(\"--Ki\", type=float, default=0.005)\n    p.add_argument(\"--r_target\", type=float, default=680.0)\n    p.add_argument(\"--w_init\", type=float, default=0.5)\n    p.add_argument(\"--w_min\", type=float, default=0.1)\n    p.add_argument(\"--w_max\", type=float, default=0.9)\n    return p.parse_args()\n\n\ndef main():\n    args = parse_args()\n\n    config = PilotConfig(\n        output_dir=args.output_dir,\n        num_generations=args.num_generations,\n        tokens_per_generation=args.tokens_per_generation,\n        checkpoint_interval_tokens=args.checkpoint_interval_tokens,\n        model_name=args.model_name,\n        per_device_batch_size=args.per_device_batch_size,\n        gradient_accumulation_steps=args.gradient_accumulation_steps,\n        learning_rate=args.learning_rate,\n        use_wandb=not args.no_wandb,\n        seed=args.seed,\n    )\n\n    ctrl_config = ControllerConfig(\n        Kp=args.Kp,\n        Ki=args.Ki,\n        r_target=args.r_target,\n        w_init=args.w_init,\n        w_min=args.w_min,\n        w_max=args.w_max,\n    )\n\n    run_controlled_pipeline(config, ctrl_config)\n\n\nif __name__ == \"__main__\":\n    main()\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "60ff85cb-037b-4c00-9e51-254478230283",
  "uuid": "c90afcc9-f714-46e6-a166-d74b26598578",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XMyjFn8W8HZ1vdNzvivtAt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16699,
      "cache_read_input_tokens": 26869,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16699
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

_source line 45 · 2026-05-13T08:26:00.456Z_

<details><summary>↩ Tool result · `toolu_01FUo83sX9JPytJAkrD5HtiM`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/code/controlled_pipeline.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "60ff85cb-037b-4c00-9e51-254478230283",
  "uuid": "f67c8a95-e3d8-4439-8722-dc1519cebeee",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/code/controlled_pipeline.py",
    "content": "\"\"\"Controlled training pipeline with PI-based collapse-aware data mixing.\n\nTrains a language model across multiple generations. G0 trains on real data\n(via train.py). G1+ uses a PI controller to dynamically adjust the\nreal/synthetic data mixing ratio w_t based on spectral effective rank\nmeasured at each checkpoint boundary.\n\nInput:\n  - Real data: WikiText (via data_utils.prepare_real_data)\n  - Synthetic data: generated from previous generation's model\nOutput:\n  - Trained models at &lt;output_dir>/G{i}/final_model/\n  - control_log.jsonl with per-segment controller state and metrics\n\nDependencies: controller.py, metrics.py, data_utils.py, config.py, train.py, generate.py\n\nUsage:\n    python controlled_pipeline.py \\\n      --output_dir /root/autodl-tmp/output_controlled/ \\\n      --num_generations 3 \\\n      --tokens_per_generation 20000000 \\\n      --Kp 0.01 --Ki 0.005 \\\n      --r_target 680 \\\n      --w_init 0.5\n\"\"\"\n\nimport argparse\nimport json\nimport logging\nimport os\nimport sys\nimport time\n\nimport torch\nfrom torch.utils.data import Dataset as TorchDataset, DataLoader\nfrom transformers import (\n    AutoModelForCausalLM,\n    AutoTokenizer,\n    get_linear_schedule_with_warmup,\n)\n\nfrom config import PilotConfig\nfrom controller import CollapseAwareController, ControllerConfig\nfrom data_utils import (\n    PackedDataset,\n    prepare_real_data,\n    prepare_synthetic_data,\n    make_dataloader,\n)\nfrom metrics import compute_spectral_effective_rank, compute_perplexity\n\nlogging.basicConfig(\n    level=logging.INFO,\n    format=\"%(asctime)s [%(levelname)s] %(name)s: %(message)s\",\n    handlers=[logging.StreamHandler(sys.stdout)],\n)\nlogger = logging.getLogger(\"controlled_pipeline\")\n\n\n# ---------------------------------------------------------------------------\n# Online data mixing\n# ---------------------------------------------------------------------------\n\nclass MixedDataset(TorchDataset):\n    \"\"\"Online real/synthetic mixing with dynamically adjustable ratio.\n\n    Each sample is independently drawn from real_dataset with probability w,\n    or from synthetic_dataset with probability (1 - w). Call set_ratio()\n    between training segments to update w without rebuilding the dataloader.\n    \"\"\"\n\n    def __init__(\n        self,\n        real_dataset: PackedDataset,\n        synthetic_dataset: PackedDataset,\n        w: float = 0.5,\n    ):\n        self.real = real_dataset\n        self.synthetic = synthetic_dataset\n        self.w = w\n\n    def set_ratio(self, w: float):\n        self.w = w\n\n    def __len__(self):\n        return max(len(self.real), len(self.synthetic))\n\n    def __getitem__(self, idx):\n        if torch.rand(1).item() < self.w:\n            return self.real[idx % len(self.real)]\n        return self.synthetic[idx % len(self.synthetic)]\n\n\n# ---------------------------------------------------------------------------\n# Helpers\n# ---------------------------------------------------------------------------\n\ndef _infinite_loader(loader: DataLoader):\n    \"\"\"Yield batches indefinitely by cycling through the loader.\"\"\"\n    while True:\n        yield from loader\n\n\ndef _save_checkpoint(model, tokenizer, path: str):\n    os.makedirs(path, exist_ok=True)\n    model.save_pretrained(path)\n    tokenizer.save_pretrained(path)\n\n\ndef _append_jsonl(path: str, entry: dict):\n    os.makedirs(os.path.dirname(path) or \".\", exist_ok=True)\n    with open(path, \"a\") as f:\n        f.write(json.dumps(entry, default=str) + \"\\n\")\n\n\n# ---------------------------------------------------------------------------\n# Controlled generation (manual training loop + PI control)\n# ---------------------------------------------------------------------------\n\ndef run_controlled_generation(\n    gen_idx: int,\n    real_dataset: PackedDataset,\n    synthetic_dataset: PackedDataset,\n    holdout_dataset: PackedDataset,\n    config: PilotConfig,\n    ctrl_config: ControllerConfig,\n    model_name_or_path: str,\n    device: str,\n) -> str:\n    \"\"\"Train one generation with PI-controlled real/synthetic mixing.\n\n    Training is split into segments of config.save_steps optimizer steps.\n    After each segment: save checkpoint -> measure spectral effective rank\n    -> PI controller step -> update mixing ratio for next segment.\n\n    Uses a manual training loop (not HF Trainer) to allow pausing between\n    segments for metric computation and ratio updates.\n\n    Returns path to the final model directory.\n    \"\"\"\n    gen_dir = config.gen_dir(gen_idx)\n    training_dir = os.path.join(gen_dir, \"training\")\n    final_dir = os.path.join(gen_dir, \"final_model\")\n    log_path = os.path.join(config.output_dir, \"control_log.jsonl\")\n\n    num_segments = config.max_steps // config.save_steps\n    steps_per_seg = config.save_steps\n\n    logger.info(\"=== Generation %d: %d segments x %d steps (total %d) ===\",\n                gen_idx, num_segments, steps_per_seg, config.max_steps)\n\n    # --- Model ---\n    tokenizer = AutoTokenizer.from_pretrained(model_name_or_path)\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n\n    model = AutoModelForCausalLM.from_pretrained(\n        model_name_or_path,\n        torch_dtype=torch.bfloat16,\n        attn_implementation=\"sdpa\",\n    ).to(device)\n\n    if config.gradient_checkpointing:\n        model.gradient_checkpointing_enable(\n            gradient_checkpointing_kwargs={\"use_reentrant\": False}\n        )\n\n    # --- Optimizer & scheduler (mirrors train.py's Trainer setup) ---\n    optimizer = torch.optim.AdamW(\n        model.parameters(),\n        lr=config.learning_rate,\n        weight_decay=config.weight_decay,\n    )\n    warmup_steps = int(config.max_steps * config.warmup_ratio)\n    scheduler = get_linear_schedule_with_warmup(\n        optimizer,\n        num_warmup_steps=warmup_steps,\n        num_training_steps=config.max_steps,\n    )\n\n    # --- Controller ---\n    controller = CollapseAwareController(ctrl_config)\n\n    # --- Data ---\n    mixed_ds = MixedDataset(real_dataset, synthetic_dataset, w=ctrl_config.w_init)\n    loader = DataLoader(\n        mixed_ds,\n        batch_size=config.per_device_batch_size,\n        shuffle=True,\n        num_workers=2,\n        pin_memory=True,\n    )\n    data_iter = _infinite_loader(loader)\n\n    holdout_loader = make_dataloader(holdout_dataset, batch_size=config.ppl_batch_size)\n    spectral_loader = make_dataloader(holdout_dataset, batch_size=config.spectral_batch_size)\n\n    # Seed controller with initial rank so the first post-segment step\n    # produces an actual control action (not just the baseline return).\n    model.eval()\n    init_rank = compute_spectral_effective_rank(\n        model, spectral_loader,\n        num_samples=config.spectral_num_samples, device=device,\n    )[\"spectral_effective_rank\"]\n    controller.step(init_rank)\n    logger.info(\"  Initial eff_rank=%.1f\", init_rank)\n\n    w_t = ctrl_config.w_init\n    global_step = 0\n\n    for seg in range(num_segments):\n        mixed_ds.set_ratio(w_t)\n\n        logger.info(\"--- Seg %d/%d | w=%.4f | steps %d->%d ---\",\n                    seg, num_segments - 1, w_t,\n                    global_step, global_step + steps_per_seg)\n\n        # --- Train one segment ---\n        model.train()\n        t0 = time.time()\n        seg_loss = 0.0\n\n        for step_in_seg in range(steps_per_seg):\n            optimizer.zero_grad()\n            accum_loss = 0.0\n\n            for _ in range(config.gradient_accumulation_steps):\n                batch = next(data_iter)\n                input_ids = batch[\"input_ids\"].to(device)\n                attention_mask = batch[\"attention_mask\"].to(device)\n                labels = batch[\"labels\"].to(device)\n\n                with torch.amp.autocast(\"cuda\", dtype=torch.bfloat16):\n                    loss = model(\n                        input_ids=input_ids,\n                        attention_mask=attention_mask,\n                        labels=labels,\n                    ).loss / config.gradient_accumulation_steps\n\n                loss.backward()\n                accum_loss += loss.item()\n\n            torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)\n            optimizer.step()\n            scheduler.step()\n            seg_loss += accum_loss\n\n            cur_step = global_step + step_in_seg + 1\n            if cur_step % 50 == 0:\n                logger.info(\"  step %d | loss %.4f | lr %.2e\",\n                            cur_step, accum_loss, scheduler.get_last_lr()[0])\n\n        global_step += steps_per_seg\n        avg_loss = seg_loss / steps_per_seg\n\n        # --- Checkpoint ---\n        ckpt_path = os.path.join(training_dir, f\"checkpoint-{global_step}\")\n        _save_checkpoint(model, tokenizer, ckpt_path)\n\n        # --- Measure spectral rank & perplexity ---\n        model.eval()\n        eff_rank = compute_spectral_effective_rank(\n            model, spectral_loader,\n            num_samples=config.spectral_num_samples, device=device,\n        )[\"spectral_effective_rank\"]\n\n        ppl = compute_perplexity(\n            model, holdout_loader,\n            num_samples=config.ppl_num_samples, device=device,\n        )[\"perplexity\"]\n\n        # --- PI controller step ---\n        w_t = controller.step(eff_rank)\n        state = controller.get_state()\n\n        entry = {\n            \"generation\": gen_idx,\n            \"segment\": seg,\n            \"step\": global_step,\n            \"eff_rank\": round(eff_rank, 2),\n            \"w_t\": round(w_t, 4),\n            \"ppl\": round(ppl, 2),\n            \"proportional\": round(state[\"proportional_term\"], 6),\n            \"integral\": round(state[\"integral_term\"], 6),\n        }\n        _append_jsonl(log_path, entry)\n\n        logger.info(\"  rank=%.1f | w_t=%.4f | ppl=%.2f (%.0fs)\",\n                    eff_rank, w_t, ppl, time.time() - t0)\n\n    # --- Save final model ---\n    _save_checkpoint(model, tokenizer, final_dir)\n    logger.info(\"Final model -> %s\", final_dir)\n\n    del model\n    torch.cuda.empty_cache()\n    return final_dir\n\n\n# ---------------------------------------------------------------------------\n# Multi-generation orchestrator\n# ---------------------------------------------------------------------------\n\ndef run_controlled_pipeline(config: PilotConfig, ctrl_config: ControllerConfig):\n    \"\"\"Multi-generation pipeline: G0 on real data, G1+ with PI-controlled mixing.\"\"\"\n    device = \"cuda\" if torch.cuda.is_available() else \"cpu\"\n    os.makedirs(config.output_dir, exist_ok=True)\n\n    logger.info(\"=\" * 60)\n    logger.info(\"CONTROLLED PIPELINE\")\n    logger.info(\"  Model: %s | Gens: %d | Tokens/gen: %dM\",\n                config.model_name, config.num_generations,\n                config.tokens_per_generation // 1_000_000)\n    logger.info(\"  PI: Kp=%.4f Ki=%.4f r_target=%.1f w=[%.2f, %.2f, %.2f]\",\n                ctrl_config.Kp, ctrl_config.Ki, ctrl_config.r_target,\n                ctrl_config.w_min, ctrl_config.w_init, ctrl_config.w_max)\n    logger.info(\"=\" * 60)\n\n    tokenizer = AutoTokenizer.from_pretrained(config.model_name)\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n\n    real_train, holdout = prepare_real_data(config, tokenizer)\n    prev_model_dir: str | None = None\n\n    for g in range(config.num_generations):\n        logger.info(\"=\" * 60)\n        logger.info(\"GENERATION %d / %d\", g, config.num_generations - 1)\n        logger.info(\"=\" * 60)\n\n        if g == 0:\n            # G0: standard training on real data only (no mixing needed)\n            from train import train_generation\n            final_dir, _ = train_generation(\n                gen_idx=g,\n                train_dataset=real_train,\n                config=config,\n            )\n        else:\n            synth_path = config.synthetic_data_path(g - 1)\n            synthetic = prepare_synthetic_data(synth_path, config, tokenizer)\n\n            final_dir = run_controlled_generation(\n                gen_idx=g,\n                real_dataset=real_train,\n                synthetic_dataset=synthetic,\n                holdout_dataset=holdout,\n                config=config,\n                ctrl_config=ctrl_config,\n                model_name_or_path=prev_model_dir or config.model_name,\n                device=device,\n            )\n\n        # Generate synthetic data for next generation\n        if g < config.num_generations - 1:\n            logger.info(\"Generating synthetic data from G%d ...\", g)\n            from generate import generate_synthetic_data\n            gen_model = AutoModelForCausalLM.from_pretrained(\n                final_dir, torch_dtype=torch.bfloat16\n            ).to(device)\n            gen_tok = AutoTokenizer.from_pretrained(config.model_name)\n            if gen_tok.pad_token is None:\n                gen_tok.pad_token = gen_tok.eos_token\n\n            generate_synthetic_data(\n                model=gen_model,\n                tokenizer=gen_tok,\n                num_tokens=config.tokens_per_generation,\n                config=config,\n                output_dir=config.synthetic_data_path(g),\n            )\n            del gen_model\n            torch.cuda.empty_cache()\n\n        prev_model_dir = final_dir\n\n    logger.info(\"CONTROLLED PIPELINE COMPLETE\")\n\n\n# ---------------------------------------------------------------------------\n# CLI\n# ---------------------------------------------------------------------------\n\ndef parse_args():\n    p = argparse.ArgumentParser(\n        description=\"PI-controlled collapse-aware training pipeline\"\n    )\n    # PilotConfig overrides\n    p.add_argument(\"--output_dir\", type=str, default=\"./output_controlled\")\n    p.add_argument(\"--num_generations\", type=int, default=3)\n    p.add_argument(\"--tokens_per_generation\", type=int, default=20_000_000)\n    p.add_argument(\"--checkpoint_interval_tokens\", type=int, default=10_000_000)\n    p.add_argument(\"--model_name\", type=str, default=\"EleutherAI/pythia-1b\")\n    p.add_argument(\"--per_device_batch_size\", type=int, default=8)\n    p.add_argument(\"--gradient_accumulation_steps\", type=int, default=4)\n    p.add_argument(\"--learning_rate\", type=float, default=2e-6)\n    p.add_argument(\"--no_wandb\", action=\"store_true\")\n    p.add_argument(\"--seed\", type=int, default=42)\n    # ControllerConfig\n    p.add_argument(\"--Kp\", type=float, default=0.01)\n    p.add_argument(\"--Ki\", type=float, default=0.005)\n    p.add_argument(\"--r_target\", type=float, default=680.0)\n    p.add_argument(\"--w_init\", type=float, default=0.5)\n    p.add_argument(\"--w_min\", type=float, default=0.1)\n    p.add_argument(\"--w_max\", type=float, default=0.9)\n    return p.parse_args()\n\n\ndef main():\n    args = parse_args()\n\n    config = PilotConfig(\n        output_dir=args.output_dir,\n        num_generations=args.num_generations,\n        tokens_per_generation=args.tokens_per_generation,\n        checkpoint_interval_tokens=args.checkpoint_interval_tokens,\n        model_name=args.model_name,\n        per_device_batch_size=args.per_device_batch_size,\n        gradient_accumulation_steps=args.gradient_accumulation_steps,\n        learning_rate=args.learning_rate,\n        use_wandb=not args.no_wandb,\n        seed=args.seed,\n    )\n\n    ctrl_config = ControllerConfig(\n        Kp=args.Kp,\n        Ki=args.Ki,\n        r_target=args.r_target,\n        w_init=args.w_init,\n        w_min=args.w_min,\n        w_max=args.w_max,\n    )\n\n    run_controlled_pipeline(config, ctrl_config)\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 46_

<details open><summary>🔧 Tool call — Bash · `toolu_014kKnraK6pjiaDxYXjUMJuv`</summary>

```json
{
  "command": "python3 -c \"import ast; ast.parse(open('controlled_pipeline.py').read()); print('OK')\"",
  "description": "Verify syntax of controlled_pipeline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "60ff85cb-037b-4c00-9e51-254478230283",
  "uuid": "53796986-2fd9-4743-a666-4c91dfadfb89",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MpTyMx2peqwA27WPn8ksoN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25808,
      "cache_read_input_tokens": 43568,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 25808
      },
      "output_tokens": 62,
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

_source line 47 · 2026-05-13T08:26:04.120Z_

<details><summary>↩ Tool result · `toolu_014kKnraK6pjiaDxYXjUMJuv`</summary>

```text
OK
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "60ff85cb-037b-4c00-9e51-254478230283",
  "uuid": "e71b7ea3-3d07-490a-9f4c-eb5a7bb3352a",
  "tool_use_result": {
    "stdout": "OK",
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

_source line 48_

语法验证通过。文件已写入 `controlled_pipeline.py`。

核心设计：
- **`MixedDataset`**：每个样本独立以概率 `w` 采样真实数据、`(1-w)` 采样合成数据，`set_ratio()` 可在 segment 间动态更新
- **手动训练循环**：每个 segment = `save_steps` 步优化，segment 结束后暂停训练，测量 spectral rank + PPL，PI controller 输出新 `w_t`
- **Controller seeding**：训练前先测初始 rank 喂给 controller，使第一个 segment 后即产生实际控制动作
- **G0 用 `train_generation()`（标准 HF Trainer），G1+ 用 `run_controlled_generation()`（手动循环 + PI 控制）**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "60ff85cb-037b-4c00-9e51-254478230283",
  "uuid": "efebf901-eda2-4eed-a589-455cc42c8637",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018D4dW7hBShg2UykCPUfYCF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 118,
      "cache_read_input_tokens": 69376,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 118
      },
      "output_tokens": 1,
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

_source line 49_

语法验证通过。文件已写入 `controlled_pipeline.py`。

核心设计：
- **`MixedDataset`**：每个样本独立以概率 `w` 采样真实数据、`(1-w)` 采样合成数据，`set_ratio()` 可在 segment 间动态更新
- **手动训练循环**：每个 segment = `save_steps` 步优化，segment 结束后暂停训练，测量 spectral rank + PPL，PI controller 输出新 `w_t`
- **Controller seeding**：训练前先测初始 rank 喂给 controller，使第一个 segment 后即产生实际控制动作
- **G0 用 `train_generation()`（标准 HF Trainer），G1+ 用 `run_controlled_generation()`（手动循环 + PI 控制）**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 440534,
  "duration_api_ms": 441390,
  "num_turns": 10,
  "stop_reason": "end_turn",
  "session_id": "60ff85cb-037b-4c00-9e51-254478230283",
  "total_cost_usd": 1.2036310000000001,
  "usage": {
    "input_tokens": 7,
    "cache_creation_input_tokens": 57653,
    "cache_read_input_tokens": 176742,
    "output_tokens": 26988,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 57653,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 245,
        "cache_read_input_tokens": 69376,
        "cache_creation_input_tokens": 118,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 118
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2258,
      "outputTokens": 1866,
      "cacheReadInputTokens": 34645,
      "cacheCreationInputTokens": 52113,
      "webSearchRequests": 0,
      "costUSD": 0.08019375000000001,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 7,
      "outputTokens": 26988,
      "cacheReadInputTokens": 176742,
      "cacheCreationInputTokens": 57653,
      "webSearchRequests": 0,
      "costUSD": 1.12343725,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "ba8a1359-4f19-446d-b2de-3ee27c8e8c56"
}
```

</details>

---
