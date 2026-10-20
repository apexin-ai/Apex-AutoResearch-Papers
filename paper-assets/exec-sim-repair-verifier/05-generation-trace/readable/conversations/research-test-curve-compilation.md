# research test curve compilation

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/chats/worker_research_test-curve-compilation_20260515T140344.jsonl`
- **Structured JSON:** [`7f50a6092383cb157380.json`](../../sessions/7f/7f50a6092383cb157380.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

17 recorded events

### Tool call

_source line 1 · 2026-05-15T14:06:09.226784+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_test-curve-compilation_20260515T140344",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T14:06:09.227665+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_test-curve-compilation_20260515T140344",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T14:06:09.228298+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "exec-sim-repair-verifier",
  "limit": "0",
  "fields": "['metrics', 'spec', 'hypothesis', 'status', 'conclusion', 'exp_id', 'updated_at']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_test-curve-compilation_20260515T140344",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "exec-sim-repair-verifier",
    "limit": "0",
    "fields": "['metrics', 'spec', 'hypothesis', 'status', 'conclusion', 'exp_id', 'updated_at']"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T14:06:09.229878+00:00_

Error: result (159,597 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/9e3b9d84-55cd-4741-ad5a-826a21573797/tool-results/mcp-agent-ml-research-read_registry-1778853839087.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/9e3b9d84-55cd-4741-ad5a-826a21573797/tool-results/mcp-agent-ml-research-read_registry-1778853839087.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_test-curve-compilation_20260515T140344",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T14:06:09.230169+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/9e3b9d84-55cd-4741-ad5a-826a21573797/tool-results/mcp-agent-ml-research-read_registry-1778853839087.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\n# Filter for test eval experiments\ntest_evals = []\nfor exp in result:\n    eid = exp.get('exp_id', '')\n    if 'test' in eid.lower() or 'eval' in eid.lower():\n        test_evals.append({\n            'exp_id': eid,\n            'status': exp.get('status'),\n            'conclusion': exp.get('conclusion'),\n            'metrics': exp.get('metrics'),\n            'hypothesis': exp.get('hypothesis'),\n            'spec': exp.get('spec'),\n        })\nprint(json.dumps(test_evals, indent=2))\n\" 2>&1",
  "description": "Extract test eval experiments from registry JSON",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_test-curve-compilation_20260515T140344",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/9e3b9d84-55cd-4741-ad5a-826a21573797/tool-results/mcp-agent-ml-research-read_registry-1778853839087.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\n# Filter for test eval experiments\ntest_evals = []\nfor exp in result:\n    eid = exp.get('exp_id', '')\n    if 'test' in eid.lower() or 'eval' in eid.lower():\n        test_evals.append({\n            'exp_id': eid,\n            'status': exp.get('status'),\n            'conclusion': exp.get('conclusion'),\n            'metrics': exp.get('metrics'),\n            'hypothesis': exp.get('hypothesis'),\n            'spec': exp.get('spec'),\n        })\nprint(json.dumps(test_evals, indent=2))\n\" 2>&1",
    "description": "Extract test eval experiments from registry JSON",
    "timeout": "30000"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T14:06:09.230328+00:00_

Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 8, in &lt;module>
    eid = exp.get('exp_id', '')
          ^^^^^^^
AttributeError: 'str' object has no attribute 'get'

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_test-curve-compilation_20260515T140344",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T14:06:09.230471+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "head -c 2000 /home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/9e3b9d84-55cd-4741-ad5a-826a21573797/tool-results/mcp-agent-ml-research-read_registry-1778853839087.txt",
  "description": "Inspect registry output structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_test-curve-compilation_20260515T140344",
  "tool": "Bash",
  "tool_args": {
    "command": "head -c 2000 /home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/9e3b9d84-55cd-4741-ad5a-826a21573797/tool-results/mcp-agent-ml-research-read_registry-1778853839087.txt",
    "description": "Inspect registry output structure"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T14:06:09.230644+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"cwm-rank64-ablation\": {\"status\": \"ALLOCATED\", \"updated_at\": \"2026-05-15T14:03:38.883Z\", \"hypothesis\": \"LoRA rank ablation: CWM 4B rank=64 alpha=128 vs baseline rank=16 alpha=32。进一步验证 rank scaling 对 CWM 能力的影响。rank=32 结果为 87.0% (vs baseline 87.51%, -0.51pp)，rank=64 alpha=128 测试更高 rank 是否改变趋势。其余配置一致（lr=2e-4, epochs=3, seed=42, data=function-level）。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && python3 train_cwm_baseline.py --data_dir data/ --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-4B --output_dir checkpoints_cwm_rank64/ --batch_size 2 --grad_accumulation 16 --no_wandb --seed 42 --lora_rank 64 --lora_alpha 128\\\"\", \"server\": \"seetacloud-westd-4x5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"377095\", \"log_path\": \"~/runs/exec-sim-repair-verifier/cwm-rank64-ablation.log\", \"data_path\": \"/home/sonny/exec-sim-repair-verifier/data/cwm_train.jsonl\", \"data_count\": 15290, \"model_name\": \"Qwen/Qwen3-4B\", \"seed\": 42, \"lora_rank\": 64, \"lora_alpha\": 128, \"lr\": 0.0002, \"epochs\": 3, \"batch_size\": 2, \"grad_accumulation\": 16, \"total_steps_estimated\": 1434, \"estimated_duration\": \"~1.5h\", \"description\": \"CWM rank=64 alpha=128 ablation (vs baseline rank=16 alpha=32, rank=32 alpha=32). Function-level data.\"}}, \"cls8b-seed123-ckpt6200-test-eval-v2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-15T14:03:13.104Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && python3 eval_repo_cls.py --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/checkpoint-6200 --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/ --split test --device cuda:0 --batch_size 1 --max_seq_leng

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_test-curve-compilation_20260515T140344",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T14:06:09.230817+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/9e3b9d84-55cd-4741-ad5a-826a21573797/tool-results/mcp-agent-ml-research-read_registry-1778853839087.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\n# Filter for test eval experiments\ntest_evals = {}\nfor eid, exp in experiments.items():\n    if 'test' in eid.lower() or 'eval' in eid.lower():\n        test_evals[eid] = {\n            'status': exp.get('status'),\n            'conclusion': exp.get('conclusion'),\n            'metrics': exp.get('metrics'),\n            'hypothesis': exp.get('hypothesis','')[:200],\n        }\nprint(json.dumps(test_evals, indent=2))\n\" 2>&1",
  "description": "Extract test eval experiments from registry",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_test-curve-compilation_20260515T140344",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/9e3b9d84-55cd-4741-ad5a-826a21573797/tool-results/mcp-agent-ml-research-read_registry-1778853839087.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\n# Filter for test eval experiments\ntest_evals = {}\nfor eid, exp in experiments.items():\n    if 'test' in eid.lower() or 'eval' in eid.lower():\n        test_evals[eid] = {\n            'status': exp.get('status'),\n            'conclusion': exp.get('conclusion'),\n            'metrics': exp.get('metrics'),\n            'hypothesis': exp.get('hypothesis','')[:200],\n        }\nprint(json.dumps(test_evals, indent=2))\n\" 2>&1",
    "description": "Extract test eval experiments from registry",
    "timeout": "30000"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T14:06:09.231239+00:00_

{
  "cls8b-seed123-ckpt6200-test-eval-v2": {
    "status": "DONE",
    "conclusion": "success",
    "metrics": {
      "accuracy": 84.7,
      "f1_fail": 63.71,
      "f1_pass": 90.31,
      "f1_macro": 77.01,
      "precision_fail": 88.84,
      "precision_pass": 83.96,
      "recall_fail": 49.66,
      "recall_pass": 97.69,
      "n_instances": 9784,
      "n_cls_unparseable": 0
    },
    "hypothesis": "seed123 ckpt-6200 test eval\uff08\u5b8c\u6574 n=9784\uff0c\u65e0 --max_samples\uff09\uff0c\u8865\u5145 test curve \u6570\u636e\u70b9"
  },
  "cls4b-v5-ckpt4000-test5120-eval": {
    "status": "DONE",
    "conclusion": "failed",
    "metrics": null,
    "hypothesis": "4B s42 test sweep \u8865\u70b9: ckpt-4000 test@5120\u3002Supplementary val+test \u53cc\u7ebf\u56fe\u3002"
  },
  "cwm8b-ckpt400-test-eval": {
    "status": "RUNNING",
    "conclusion": null,
    "metrics": null,
    "hypothesis": "CWM 8B ckpt-400 (best eval_loss=0.286) test@full(n=9784). \u4e0e CLS 8B \u5bf9\u6bd4\u9501\u5b9a 8B-8B gap\u3002\u63d0\u524d\u5229\u7528\u7a7a\u95f2 GPU eval \u8bad\u7ec3\u4e2d\u95f4\u6700\u4f18 checkpoint\u3002"
  },
  "cls8b-seed123-ckpt200-test-eval": {
    "status": "DONE",
    "conclusion": "success",
    "metrics": {
      "accuracy": 72.55,
      "f1_macro": 70.18,
      "pass_f1": 78.58,
      "fail_f1": 61.78,
      "pass_precision": 91.21,
      "pass_recall": 69.02,
      "fail_precision": 49.54,
      "fail_recall": 82.05,
      "n_samples": 9784,
      "n_pass": 7138,
      "n_fail": 2646,
      "majority_baseline": 72.96,
      "unparseable": 0,
      "confusion_matrix": {
        "tn": 2171,
        "fp": 475,
        "fn": 2211,
        "tp": 4927
      }
    },
    "hypothesis": "seed123 test curve \u6700\u540e\u8865\u70b9: ckpt-200 test@full(n=9784)\u3002\u5b8c\u6210\u540e seed123 test curve 6/6 \u5168\u9f50\u3002"
  },
  "cls8b-s42-ckpt1000-test-seq2048-ablation": {
    "status": "DONE",
    "conclusion": "success",
    "metrics": {
      "accuracy": 82.83
…[truncated 22077 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_test-curve-compilation_20260515T140344",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T14:06:09.231449+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/9e3b9d84-55cd-4741-ad5a-826a21573797/tool-results/mcp-agent-ml-research-read_registry-1778853839087.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\n# Filter for CWM experiments\ncwm_evals = {}\nfor eid, exp in experiments.items():\n    if 'cwm' in eid.lower():\n        cwm_evals[eid] = {\n            'status': exp.get('status'),\n            'conclusion': exp.get('conclusion'),\n            'metrics': exp.get('metrics'),\n            'hypothesis': exp.get('hypothesis','')[:300],\n        }\nprint(json.dumps(cwm_evals, indent=2))\n\" 2>&1",
  "description": "Extract CWM experiments from registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_test-curve-compilation_20260515T140344",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/9e3b9d84-55cd-4741-ad5a-826a21573797/tool-results/mcp-agent-ml-research-read_registry-1778853839087.txt | python3 -c \"\nimport json, sys\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\n# Filter for CWM experiments\ncwm_evals = {}\nfor eid, exp in experiments.items():\n    if 'cwm' in eid.lower():\n        cwm_evals[eid] = {\n            'status': exp.get('status'),\n            'conclusion': exp.get('conclusion'),\n            'metrics': exp.get('metrics'),\n            'hypothesis': exp.get('hypothesis','')[:300],\n        }\nprint(json.dumps(cwm_evals, indent=2))\n\" 2>&1",
    "description": "Extract CWM experiments from registry"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T14:06:09.231752+00:00_

{
  "cwm-rank64-ablation": {
    "status": "ALLOCATED",
    "conclusion": null,
    "metrics": null,
    "hypothesis": "LoRA rank ablation: CWM 4B rank=64 alpha=128 vs baseline rank=16 alpha=32\u3002\u8fdb\u4e00\u6b65\u9a8c\u8bc1 rank scaling \u5bf9 CWM \u80fd\u529b\u7684\u5f71\u54cd\u3002rank=32 \u7ed3\u679c\u4e3a 87.0% (vs baseline 87.51%, -0.51pp)\uff0crank=64 alpha=128 \u6d4b\u8bd5\u66f4\u9ad8 rank \u662f\u5426\u6539\u53d8\u8d8b\u52bf\u3002\u5176\u4f59\u914d\u7f6e\u4e00\u81f4\uff08lr=2e-4, epochs=3, seed=42, data=function-level\uff09\u3002"
  },
  "cwm-rank32-ablation-v2": {
    "status": "DONE",
    "conclusion": "success",
    "metrics": {
      "accuracy": 87,
      "exact_match_rate": 83.4,
      "fail_f1": 87.1,
      "pass_f1": 86.9,
      "train_loss_final": 0.0152,
      "train_loss_avg": 0.2536,
      "eval_loss": 0.0688,
      "train_runtime_sec": 5003,
      "test_set_size": 1890,
      "vs_rank16_baseline": -0.51,
      "rank16_baseline_accuracy": 87.51
    },
    "hypothesis": "LoRA rank ablation: CWM 4B rank=32 vs baseline rank=16. \u56de\u5e94\u5ba1\u7a3f\u4eba\u8d28\u7591 rank=16 \u662f\u5426\u7cfb\u7edf\u6027\u4f4e\u4f30 CWM \u80fd\u529b\u3002\u5176\u4f59\u914d\u7f6e\u5b8c\u5168\u4e00\u81f4\uff08lr=2e-4, epochs=3, seed=42, alpha=32, data=function-level\uff09\u3002PID 368823 \u5728 GPU 0 \u4e0a\u6b63\u5e38\u8bad\u7ec3\uff0cstep 324/1434 (22%)\u3002\u6ce8\u610f\uff1a\u8bad\u7ec3\u547d\u4ee4\u672a\u4e32\u8054 eval\uff0c\u5b8c\u6210\u540e\u9700\u5355\u72ec\u89e6\u53d1 eval\u3002"
  },
  "cwm-rank32-ablation": {
    "status": "DONE",
    "conclusion": "killed",
    "metrics": null,
    "hypothesis": "LoRA rank=32 ablation (vs baseline rank=16) for CWM 4B function-level. Config: lr=2e-4, epochs=3, bs=2, ga=16, lora_rank=32, max_seq=2048, seed=42. NOTE: PID 368823 still RUNNING on GPU 0 as of 2026-05-15 20:49 (step 324/1434, ETA ~60min). Registry status 'killed' was incorrect."
  },
  "cwm-4b-rank32-ablation": {
    "status": "DONE",
    "conclusion": 
…[truncated 13940 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_test-curve-compilation_20260515T140344",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T14:06:09.232019+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/comprehensive_test_results.md",
  "content": "# Comprehensive Test Results — exec-sim-repair-verifier\n\n> Compiled: 2026-05-15 | Majority baseline (repo-level): **72.96%** | Majority baseline (function-level): **51.75%**\n\n---\n\n## 1. Repo-Level CLS Test Curves\n\nAll repo-level evals use full test set (n=9,784).\n\n### CLS 8B seed123 (test@8192)\n\n| Checkpoint | Test Acc (%) | F1_macro | F1_fail | F1_pass | Note |\n|-----------|-------------|----------|---------|---------|------|\n| ckpt-200  | 72.55       | 70.18    | 61.78   | 78.58   | Near majority baseline |\n| **ckpt-3000** | **85.60** | **78.38** | **65.89** | **90.87** | **Val-best (val=88.69%) & Test peak** |\n| ckpt-6200 | 84.70       | 77.01    | 63.71   | 90.31   | |\n| ckpt-6400 | 85.08       | 77.91    | 65.32   | 90.49   | |\n| ckpt-6600 | 84.90       | 77.58    | 64.80   | 90.40   | |\n| ckpt-6633 | 84.89       | 77.56    | 64.70   | 90.40   | Final checkpoint |\n\n- **Val-selected test accuracy: 85.60%** (ckpt-3000, val=88.69%)\n- Test peak: 85.60% (ckpt-3000) — val-selected = test-peak\n- Gap vs majority: +12.64pp\n\n### CLS 8B s42 (test@8192)\n\n| Checkpoint | Test Acc (%) | F1_macro | F1_fail | F1_pass | Note |\n|-----------|-------------|----------|---------|---------|------|\n| ckpt-200  | 70.07       | 68.18    | 60.40   | 75.90   | Below majority baseline |\n| ckpt-400  | 84.79       | 81.18    | 72.93   | 89.43   | |\n| ckpt-600  | 79.05       | 75.12    | 65.24   | 85.00   | |\n| ckpt-800  | 83.53       | 78.97    | 69.17   | 88.77   | |\n| ckpt-1000 | 83.52       | 77.50    | 65.85   | 89.14   | Val-best (val=88.23%) |\n| ckpt-1200 | 83.84       | 77.47    | 65.49   | 89.45   | |\n| **ckpt-1400** | **85.47** | **78.90** | **67.13** | **90.67** | **Test peak** |\n| ckpt-1600 | 84.99       | 78.94    | 67.65   | 90.22   | |\n\n- **Val-selected test accuracy: 83.52%** (ckpt-1000, val=88.23%)\n- Test peak: 85.47% (ckpt-1400)\n- Gap vs majority: +12.51pp (peak), +10.56pp (val-selected)\n\n### CLS 4B s42 (test@5120)\n\n| Checkpoint | Test Acc (%) | F1_macro | F1_fail | F1_pass | Note |\n|-----------|-------------|----------|---------|---------|------|\n| ckpt-600  | 77.74       | 74.74    | 66.03   | 83.44   | |\n| ckpt-4000 | —           | —        | —       | —       | Failed (script error) |\n| ckpt-4400 | 83.24       | 74.44    | 59.45   | 89.44   | |\n| **ckpt-4600** | **83.63** | **75.63** | **61.67** | **89.59** | **Val-best (val=90.07%) & Test peak** |\n\n- **Val-selected test accuracy: 83.63%** (ckpt-4600, val=90.07%)\n- Gap vs majority: +10.67pp\n\n### CLS 4B seed123 (test@5120)\n\n| Checkpoint | Test Acc (%) | F1_macro | F1_fail | F1_pass | Note |\n|-----------|-------------|----------|---------|---------|------|\n| ckpt-800  | 75.33       | 67.03    | 50.50   | 83.60   | Val-best (val=87.92%), weak test |\n\n- **Val-selected test accuracy: 75.33%** (ckpt-800, val=87.92%)\n- Gap vs majority: +2.37pp — marginal\n\n---\n\n## 2. Repo-Level CWM Test Results\n\n### CWM 4B repo-level (test@full, n=9,784)\n\n| Variant | Test Acc (%) | F1_macro | F1_fail | F1_pass | Unparseable |\n|---------|-------------|----------|---------|---------|-------------|\n| s42 (v12) | 58.04     | 51.67    | 34.12   | 69.22   | 53.7% |\n| seed123   | 59.09     | 43.43    | 13.67   | 73.19   | 67.2% |\n\n- Both **below majority baseline** (72.96%) — CWM fails catastrophically at repo-level\n- Massive unparseable rates (54-67%) confirm generation struggles with long repo contexts\n\n### CWM 8B repo-level\n\n- Training in progress (repo-level-cwm-8b-conda-v4, step ~1700/6633)\n- ckpt-400 test eval running (cwm8b-ckpt400-test-eval)\n\n---\n\n## 3. Function-Level Results (n=1,890)\n\n### CLS 8B function-level\n\n| Seed | Accuracy (%) | F1_pass | F1_fail |\n|------|-------------|---------|---------|\n| s42  | 90.48       | 90.86   | 90.06   |\n| seed123 | 89.37    | 89.54   | 89.19   |\n| **Mean** | **89.93** | **90.20** | **89.63** |\n\n### CWM 4B function-level (5-seed)\n\n| Seed | Accuracy (%) | F1_pass | F1_fail |\n|------|-------------|---------|---------|\n| s42 (baseline) | 87.51 | 87.31 | 87.71 |\n| seed123 | 87.20 | 86.95 | 87.44 |\n| seed456 | 86.98 | 86.66 | 87.29 |\n| seed789 | 86.67 | 86.74 | 86.60 |\n| seed0   | 87.57 | 87.18 | 87.93 |\n| **Mean** | **87.19** | **86.97** | **87.39** |\n\n### CWM 8B function-level (3-seed)\n\n| Seed | Accuracy (%) | F1_pass | F1_fail |\n|------|-------------|---------|---------|\n| s42  | 87.67       | 87.57   | 87.77   |\n| seed123 | 86.98    | 86.83   | 87.13   |\n| seed456 | 86.24    | 85.96   | 86.51   |\n| **Mean** | **86.96** | **86.79** | **87.14** |\n\n---\n\n## 4. Main Results Summary\n\n### Repo-Level Test (Val-Selected Checkpoints)\n\n| Model | Size | Seed | Val-Best Ckpt | Val Acc (%) | Test Acc (%) | Gap vs Majority |\n|-------|------|------|---------------|-------------|-------------|-----------------|\n| CLS   | 8B   | seed123 | ckpt-3000 | 88.69 | **85.60** | +12.64pp |\n| CLS   | 8B   | s42     | ckpt-1000 | 88.23 | **83.52** | +10.56pp |\n| CLS   | 4B   | s42     | ckpt-4600 | 90.07 | **83.63** | +10.67pp |\n| CLS   | 4B   | seed123 | ckpt-800  | 87.92 | **75.33** | +2.37pp  |\n| CWM   | 4B   | s42     | ckpt-500  | —     | **58.04** | −14.92pp |\n| CWM   | 4B   | seed123 | ckpt-500  | —     | **59.09** | −13.87pp |\n\n### Repo-Level Test Peak (Oracle Selection)\n\n| Model | Size | Seed | Peak Ckpt | Test Acc (%) |\n|-------|------|------|-----------|-------------|\n| CLS   | 8B   | seed123 | ckpt-3000 | **85.60** |\n| CLS   | 8B   | s42     | ckpt-1400 | **85.47** |\n| CLS   | 4B   | s42     | ckpt-4600 | **83.63** |\n\n### Function-Level Summary\n\n| Model | Size | Seeds | Mean Acc (%) | Std |\n|-------|------|-------|-------------|-----|\n| CLS   | 8B   | 2     | 89.93       | 0.78 |\n| CWM   | 4B   | 5     | 87.19       | 0.35 |\n| CWM   | 8B   | 3     | 86.96       | 0.72 |\n\n---\n\n## 5. Ablation Results\n\n### CWM LoRA Rank Ablation (4B, function-level, n=1,890)\n\n| Rank | Alpha | Accuracy (%) | vs Baseline (rank=16) |\n|------|-------|-------------|----------------------|\n| 16 (baseline) | 32 | 87.51 | — |\n| 32 | 32 | 87.00 | −0.51pp |\n| 64 | 128 | — | Training allocated |\n\n### Sequence Length Ablation (CLS 8B s42, ckpt-1000, repo-level test)\n\n| max_seq_length | Test Acc (%) | Unparseable |\n|---------------|-------------|-------------|\n| 8192          | 83.52       | 0 |\n| 2048          | 82.83       | 136 |\n| **Delta**     | **−0.69pp** | |\n\nCLS@2048 (82.83%) still vastly outperforms CWM@2048 (58.04%), ruling out seq_length as a confound.\n\n---\n\n## 6. Key Takeaways\n\n1. **CLS >> CWM at repo-level**: CLS achieves 83-86% vs CWM 58-59% — a **25+pp gap** that validates the classification reformulation for complex (repo-level) inputs\n2. **CLS scales with model size**: 8B peak (85.60%) > 4B peak (83.63%) at repo-level (+1.97pp)\n3. **CWM does NOT scale at function-level**: 8B CWM (86.96%) ≈ 4B CWM (87.19%) — no benefit from 2x parameters\n4. **Val-selected vs test-peak gap**: seed123 shows 0pp gap (val-best = test-best), s42 shows 1.95pp gap (ckpt-1000 vs ckpt-1400)\n5. **Seq_length is not a confound**: CLS@2048 still beats CWM by 24.79pp\n6. **LoRA rank does not help CWM**: rank=32 marginally worse than rank=16 (−0.51pp)\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_test-curve-compilation_20260515T140344",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/comprehensive_test_results.md",
    "content": "# Comprehensive Test Results — exec-sim-repair-verifier\n\n> Compiled: 2026-05-15 | Majority baseline (repo-level): **72.96%** | Majority baseline (function-level): **51.75%**\n\n---\n\n## 1. Repo-Level CLS Test Curves\n\nAll repo-level evals use full test set (n=9,784).\n\n### CLS 8B seed123 (test@8192)\n\n| Checkpoint | Test Acc (%) | F1_macro | F1_fail | F1_pass | Note |\n|-----------|-------------|----------|---------|---------|------|\n| ckpt-200  | 72.55       | 70.18    | 61.78   | 78.58   | Near majority baseline |\n| **ckpt-3000** | **85.60** | **78.38** | **65.89** | **90.87** | **Val-best (val=88.69%) & Test peak** |\n| ckpt-6200 | 84.70       | 77.01    | 63.71   | 90.31   | |\n| ckpt-6400 | 85.08       | 77.91    | 65.32   | 90.49   | |\n| ckpt-6600 | 84.90       | 77.58    | 64.80   | 90.40   | |\n| ckpt-6633 | 84.89       | 77.56    | 64.70   | 90.40   | Final checkpoint |\n\n- **Val-selected test accuracy: 85.60%** (ckpt-3000, val=88.69%)\n- Test peak: 85.60% (ckpt-3000) — val-selected = test-peak\n- Gap vs majority: +12.64pp\n\n### CLS 8B s42 (test@8192)\n\n| Checkpoint | Test Acc (%) | F1_macro | F1_fail | F1_pass | Note |\n|-----------|-------------|----------|---------|---------|------|\n| ckpt-200  | 70.07       | 68.18    | 60.40   | 75.90   | Below majority baseline |\n| ckpt-400  | 84.79       | 81.18    | 72.93   | 89.43   | |\n| ckpt-600  | 79.05       | 75.12    | 65.24   | 85.00   | |\n| ckpt-800  | 83.53       | 78.97    | 69.17   | 88.77   | |\n| ckpt-1000 | 83.52       | 77.50    | 65.85   | 89.14   | Val-best (val=88.23%) |\n| ckpt-1200 | 83.84       | 77.47    | 65.49   | 89.45   | |\n| **ckpt-1400** | **85.47** | **78.90** | **67.13** | **90.67** | **Test peak** |\n| ckpt-1600 | 84.99       | 78.94    | 67.65   | 90.22   | |\n\n- **Val-selected test accuracy: 83.52%** (ckpt-1000, val=88.23%)\n- Test peak: 85.47% (ckpt-1400)\n- Gap vs majority: +12.51pp (peak), +10.56pp (val-selected)\n\n### CLS 4B s42 (test@5120)\n\n| Checkpoint | Test Acc (%) | F1_macro | F1_fail | F1_pass | Note |\n|-----------|-------------|----------|---------|---------|------|\n| ckpt-600  | 77.74       | 74.74    | 66.03   | 83.44   | |\n| ckpt-4000 | —           | —        | —       | —       | Failed (script error) |\n| ckpt-4400 | 83.24       | 74.44    | 59.45   | 89.44   | |\n| **ckpt-4600** | **83.63** | **75.63** | **61.67** | **89.59** | **Val-best (val=90.07%) & Test peak** |\n\n- **Val-selected test accuracy: 83.63%** (ckpt-4600, val=90.07%)\n- Gap vs majority: +10.67pp\n\n### CLS 4B seed123 (test@5120)\n\n| Checkpoint | Test Acc (%) | F1_macro | F1_fail | F1_pass | Note |\n|-----------|-------------|----------|---------|---------|------|\n| ckpt-800  | 75.33       | 67.03    | 50.50   | 83.60   | Val-best (val=87.92%), weak test |\n\n- **Val-selected test accuracy: 75.33%** (ckpt-800, val=87.92%)\n- Gap vs majority: +2.37pp — marginal\n\n---\n\n## 2. Repo-Level CWM Test Results\n\n### CWM 4B repo-level (test@full, n=9,784)\n\n| Variant | Test Acc (%) | F1_macro | F1_fail | F1_pass | Unparseable |\n|---------|-------------|----------|---------|---------|-------------|\n| s42 (v12) | 58.04     | 51.67    | 34.12   | 69.22   | 53.7% |\n| seed123   | 59.09     | 43.43    | 13.67   | 73.19   | 67.2% |\n\n- Both **below majority baseline** (72.96%) — CWM fails catastrophically at repo-level\n- Massive unparseable rates (54-67%) confirm generation struggles with long repo contexts\n\n### CWM 8B repo-level\n\n- Training in progress (repo-level-cwm-8b-conda-v4, step ~1700/6633)\n- ckpt-400 test eval running (cwm8b-ckpt400-test-eval)\n\n---\n\n## 3. Function-Level Results (n=1,890)\n\n### CLS 8B function-level\n\n| Seed | Accuracy (%) | F1_pass | F1_fail |\n|------|-------------|---------|---------|\n| s42  | 90.48       | 90.86   | 90.06   |\n| seed123 | 89.37    | 89.54   | 89.19   |\n| **Mean** | **89.93** | **90.20** | **89.63** |\n\n### CWM 4B function-level (5-seed)\n\n| Seed | Accuracy (%) | F1_pass | F1_fail |\n|------|-------------|---------|---------|\n| s42 (baseline) | 87.51 | 87.31 | 87.71 |\n| seed123 | 87.20 | 86.95 | 87.44 |\n| seed456 | 86.98 | 86.66 | 87.29 |\n| seed789 | 86.67 | 86.74 | 86.60 |\n| seed0   | 87.57 | 87.18 | 87.93 |\n| **Mean** | **87.19** | **86.97** | **87.39** |\n\n### CWM 8B function-level (3-seed)\n\n| Seed | Accuracy (%) | F1_pass | F1_fail |\n|------|-------------|---------|---------|\n| s42  | 87.67       | 87.57   | 87.77   |\n| seed123 | 86.98    | 86.83   | 87.13   |\n| seed456 | 86.24    | 85.96   | 86.51   |\n| **Mean** | **86.96** | **86.79** | **87.14** |\n\n---\n\n## 4. Main Results Summary\n\n### Repo-Level Test (Val-Selected Checkpoints)\n\n| Model | Size | Seed | Val-Best Ckpt | Val Acc (%) | Test Acc (%) | Gap vs Majority |\n|-------|------|------|---------------|-------------|-------------|-----------------|\n| CLS   | 8B   | seed123 | ckpt-3000 | 88.69 | **85.60** | +12.64pp |\n| CLS   | 8B   | s42     | ckpt-1000 | 88.23 | **83.52** | +10.56pp |\n| CLS   | 4B   | s42     | ckpt-4600 | 90.07 | **83.63** | +10.67pp |\n| CLS   | 4B   | seed123 | ckpt-800  | 87.92 | **75.33** | +2.37pp  |\n| CWM   | 4B   | s42     | ckpt-500  | —     | **58.04** | −14.92pp |\n| CWM   | 4B   | seed123 | ckpt-500  | —     | **59.09** | −13.87pp |\n\n### Repo-Level Test Peak (Oracle Selection)\n\n| Model | Size | Seed | Peak Ckpt | Test Acc (%) |\n|-------|------|------|-----------|-------------|\n| CLS   | 8B   | seed123 | ckpt-3000 | **85.60** |\n| CLS   | 8B   | s42     | ckpt-1400 | **85.47** |\n| CLS   | 4B   | s42     | ckpt-4600 | **83.63** |\n\n### Function-Level Summary\n\n| Model | Size | Seeds | Mean Acc (%) | Std |\n|-------|------|-------|-------------|-----|\n| CLS   | 8B   | 2     | 89.93       | 0.78 |\n| CWM   | 4B   | 5     | 87.19       | 0.35 |\n| CWM   | 8B   | 3     | 86.96       | 0.72 |\n\n---\n\n## 5. Ablation Results\n\n### CWM LoRA Rank Ablation (4B, function-level, n=1,890)\n\n| Rank | Alpha | Accuracy (%) | vs Baseline (rank=16) |\n|------|-------|-------------|----------------------|\n| 16 (baseline) | 32 | 87.51 | — |\n| 32 | 32 | 87.00 | −0.51pp |\n| 64 | 128 | — | Training allocated |\n\n### Sequence Length Ablation (CLS 8B s42, ckpt-1000, repo-level test)\n\n| max_seq_length | Test Acc (%) | Unparseable |\n|---------------|-------------|-------------|\n| 8192          | 83.52       | 0 |\n| 2048          | 82.83       | 136 |\n| **Delta**     | **−0.69pp** | |\n\nCLS@2048 (82.83%) still vastly outperforms CWM@2048 (58.04%), ruling out seq_length as a confound.\n\n---\n\n## 6. Key Takeaways\n\n1. **CLS >> CWM at repo-level**: CLS achieves 83-86% vs CWM 58-59% — a **25+pp gap** that validates the classification reformulation for complex (repo-level) inputs\n2. **CLS scales with model size**: 8B peak (85.60%) > 4B peak (83.63%) at repo-level (+1.97pp)\n3. **CWM does NOT scale at function-level**: 8B CWM (86.96%) ≈ 4B CWM (87.19%) — no benefit from 2x parameters\n4. **Val-selected vs test-peak gap**: seed123 shows 0pp gap (val-best = test-best), s42 shows 1.95pp gap (ckpt-1000 vs ckpt-1400)\n5. **Seq_length is not a confound**: CLS@2048 still beats CWM by 24.79pp\n6. **LoRA rank does not help CWM**: rank=32 marginally worse than rank=16 (−0.51pp)\n"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T14:06:09.232259+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/comprehensive_test_results.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_test-curve-compilation_20260515T140344",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T14:06:09.232392+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "comprehensive_test_results",
  "type": "report",
  "description": "Complete test curve compilation for all CLS/CWM models across repo-level and function-level evaluations. Includes per-checkpoint curves, val-selected vs peak analysis, ablation results, and key takeaways.",
  "project": "exec-sim-repair-verifier",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/comprehensive_test_results.md",
  "tags": "['test-results', 'test-curve', 'compilation', 'repo-level', 'function-level']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_test-curve-compilation_20260515T140344",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "comprehensive_test_results",
    "type": "report",
    "description": "Complete test curve compilation for all CLS/CWM models across repo-level and function-level evaluations. Includes per-checkpoint curves, val-selected vs peak analysis, ablation results, and key takeaways.",
    "project": "exec-sim-repair-verifier",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/comprehensive_test_results.md",
    "tags": "['test-results', 'test-curve', 'compilation', 'repo-level', 'function-level']"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T14:06:09.232541+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_d88b8c\", \"name\": \"comprehensive_test_results\", \"type\": \"report\", \"description\": \"Complete test curve compilation for all CLS/CWM models across repo-level and function-level evaluations. Includes per-checkpoint curves, val-selected vs peak analysis, ablation results, and key takeaways.\", \"path\": \"projects/exec-sim-repair-verifier/artifacts/_project/report/comprehensive_test_results.md\", \"url\": null, \"project\": \"exec-sim-repair-verifier\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T14:05:59.683866+00:00\", \"tags\": [\"test-results\", \"test-curve\", \"compilation\", \"repo-level\", \"function-level\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_test-curve-compilation_20260515T140344",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-15T14:06:09.232710+00:00_

已完成。文件写入 `artifacts/comprehensive_test_results.md` 并注册为 `art_20260515_d88b8c`。

内容概要：
- **CLS 8B seed123 test curve**: 6 个 checkpoint，val-selected = test-peak = ckpt-3000 (85.60%)
- **CLS 8B s42 test curve**: 8 个 checkpoint，val-selected ckpt-1000 (83.52%)，test-peak ckpt-1400 (85.47%)
- **CLS 4B s42 test curve**: 3 个有效 checkpoint，val-selected = ckpt-4600 (83.63%)
- **CLS 4B seed123**: ckpt-800 仅 75.33%，表现弱
- **CWM repo-level**: 58-59%，低于 majority baseline，彻底失败
- **Function-level**: CLS 8B 89.93% > CWM 4B 87.19% ≈ CWM 8B 86.96%
- **Ablation**: rank=32 无帮助 (−0.51pp)，seq_length 非混杂变量 (CLS@2048 仍超 CWM 24.79pp)
- CWM 8B repo-level test 仍在运行中 (cwm8b-ckpt400-test-eval)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_test-curve-compilation_20260515T140344"
}
```

</details>

---
