# Research conversation: [Director 指令] [Director 紧急] **用户催促"马上马上"——立即启动 seed=123 训练，不等分析完成。** GPU 在空转浪费时间。分析是 CPU-bound，训练是 GPU-bound，必须并行。 **现在立 — Part 1 of 3

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families (July export snapshot)** · Conversation logs

[Transcript overview](../research-conversation-director-director-seed-123-gpu-cpu-bound-gpu-bound.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/92/92e654c7e316cf7c7351.json)

## Before a recorded user message

## Before a recorded user message

2 recorded events


### Runtime record

_source line 1 · 2026-05-19T13:29:57.048Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-19T13:29:57.048Z",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "content": "[Director 指令] [Director 紧急] **用户催促\"马上马上\"——立即启动 seed=123 训练，不等分析完成。**\n\nGPU 在空转浪费时间。分析是 CPU-bound，训练是 GPU-bound，必须并行。\n\n**现在立刻做**：\n1. SSH westd，kill 所有僵尸进程（GPU 0 的 PID 176524 重复 eval，GPU 1 异常状态）\n2. 确认 4 张卡全部空闲干净\n3. 确认 5 个 model snapshot 路径：\n```bash\nls /root/.cache/huggingface/hub/models--microsoft--phi-4/snapshots/\nls /root/.cache/huggingface/hub/models--Qwen--Qwen2.5-14B/snapshots/\nls /root/.cache/huggingface/hub/models--Qwen--Qwen2.5-7B/snapshots/\nls /root/.cache/huggingface/hub/models--google--gemma-2-9b/snapshots/\nls /root/.cache/huggingface/hub/models--allenai--OLMo-2-0425-1124-7B/snapshots/\n```\n4. **立即 4 卡并行启动第一批 seed=123 训练**（每卡一个 family）：\n   - cuda:0: Phi-4 d000 s123\n   - cuda:1: Qwen-14B d000 s123\n   - cuda:2: Qwen-7B d000 s123\n   - cuda:3: Gemma-2 d000 s123\n\n每个完成后立即接下一个 dosage（d005→d025→d050→d100），用 bash 脚本串联：\n```bash\n# 示例 cuda:0 Phi-4 全 5 dosages\ncd /root/autodl-tmp/exp001\nfor d in 000 005 025 050 100; do\n  CUDA_VISIBLE_DEVICES=0 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 \\\n  /root/miniconda3/bin/python train_sft.py \\\n    --model_name_or_path {phi4_snapshot_path} \\\n    --dosage ${d} --seed 123 \\\n    --output_dir output_phi4_d${d}_s123 \\\n    --lora_r 16 --lora_alpha 32 --learning_rate 5e-5 \\\n    --bf16 --mode augment\ndone\n```\n\nOLMo-2 的 5 个 run 排在 Qwen-7B 完成后（cuda:2），因为 7B 训练最快（~35min each）。\n\n**用 nohup + tmux，每卡一个 session（tmux new -s gpu0/gpu1/gpu2/gpu3）**。不要等任何汇报——启动后立即报一句\"4 卡已启动\"即可。\n\n队列里后面的 D150 详细指令有完整参数，但核心就是上面这些。**先跑起来再说。**"
}
````

---


### Runtime record

_source line 2 · 2026-05-19T13:29:57.051Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-19T13:29:57.051Z",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de"
}
```

---


## Round 1

## Round 1

38 recorded events


### User

_source line 3 · 2026-05-19T13:29:57.088Z_

[Director 指令] [Director 紧急] **用户催促"马上马上"——立即启动 seed=123 训练，不等分析完成。**

GPU 在空转浪费时间。分析是 CPU-bound，训练是 GPU-bound，必须并行。

**现在立刻做**：
1. SSH westd，kill 所有僵尸进程（GPU 0 的 PID 176524 重复 eval，GPU 1 异常状态）
2. 确认 4 张卡全部空闲干净
3. 确认 5 个 model snapshot 路径：
```bash
ls /root/.cache/huggingface/hub/models--microsoft--phi-4/snapshots/
ls /root/.cache/huggingface/hub/models--Qwen--Qwen2.5-14B/snapshots/
ls /root/.cache/huggingface/hub/models--Qwen--Qwen2.5-7B/snapshots/
ls /root/.cache/huggingface/hub/models--google--gemma-2-9b/snapshots/
ls /root/.cache/huggingface/hub/models--allenai--OLMo-2-0425-1124-7B/snapshots/
```
4. **立即 4 卡并行启动第一批 seed=123 训练**（每卡一个 family）：
   - cuda:0: Phi-4 d000 s123
   - cuda:1: Qwen-14B d000 s123
   - cuda:2: Qwen-7B d000 s123
   - cuda:3: Gemma-2 d000 s123

每个完成后立即接下一个 dosage（d005→d025→d050→d100），用 bash 脚本串联：
```bash
# 示例 cuda:0 Phi-4 全 5 dosages
cd /root/autodl-tmp/exp001
for d in 000 005 025 050 100; do
  CUDA_VISIBLE_DEVICES=0 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 \
  /root/miniconda3/bin/python train_sft.py \
    --model_name_or_path {phi4_snapshot_path} \
    --dosage ${d} --seed 123 \
    --output_dir output_phi4_d${d}_s123 \
    --lora_r 16 --lora_alpha 32 --learning_rate 5e-5 \
    --bf16 --mode augment
done
```

OLMo-2 的 5 个 run 排在 Qwen-7B 完成后（cuda:2），因为 7B 训练最快（~35min each）。

**用 nohup + tmux，每卡一个 session（tmux new -s gpu0/gpu1/gpu2/gpu3）**。不要等任何汇报——启动后立即报一句"4 卡已启动"即可。

队列里后面的 D150 详细指令有完整参数，但核心就是上面这些。**先跑起来再说。**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "f236d3d3-c563-42c4-b0bf-0a1f74939452",
  "type": "user",
  "uuid": "25b21367-ca0b-404b-a7e1-ad2e426ec330",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 4 · 2026-05-19T13:29:57.087Z_

```json
{
  "parentUuid": "25b21367-ca0b-404b-a7e1-ad2e426ec330",
  "isSidechain": false,
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "AskUserQuestion",
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
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
      "mcp__agent-ml-research__distill_papers",
      "mcp__agent-ml-research__edit_paper_section",
      "mcp__agent-ml-research__feishu_read_tum_pending_key",
      "mcp__agent-ml-research__feishu_send_alert",
      "mcp__agent-ml-research__feishu_send_approval_card",
      "mcp__agent-ml-research__feishu_send_result_card",
      "mcp__agent-ml-research__feishu_send_tum_key_request_card",
      "mcp__agent-ml-research__fetch_wandb_metrics",
      "mcp__agent-ml-research__get_baseline_metrics",
      "mcp__agent-ml-research__get_distill_status",
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
      "mcp__agent-ml-research__read_mistakes",
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
    "addedLines": [
      "AskUserQuestion",
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
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
      "mcp__agent-ml-research__distill_papers",
      "mcp__agent-ml-research__edit_paper_section",
      "mcp__agent-ml-research__feishu_read_tum_pending_key",
      "mcp__agent-ml-research__feishu_send_alert",
      "mcp__agent-ml-research__feishu_send_approval_card",
      "mcp__agent-ml-research__feishu_send_result_card",
      "mcp__agent-ml-research__feishu_send_tum_key_request_card",
      "mcp__agent-ml-research__fetch_wandb_metrics",
      "mcp__agent-ml-research__get_baseline_metrics",
      "mcp__agent-ml-research__get_distill_status",
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
      "mcp__agent-ml-research__read_mistakes",
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
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "5012c42e-a644-4568-a364-be512060c5c5",
  "timestamp": "2026-05-19T13:29:57.087Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Runtime record

_source line 5 · 2026-05-19T13:29:57.087Z_

```json
{
  "parentUuid": "5012c42e-a644-4568-a364-be512060c5c5",
  "isSidechain": false,
  "attachment": {
    "type": "mcp_instructions_delta",
    "addedNames": [
      "agent-ml-research"
    ],
    "addedBlocks": [
      "## agent-ml-research\nML research experiment management tools"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "247a5a78-55e8-4f36-b529-1f0cd0bf1e5c",
  "timestamp": "2026-05-19T13:29:57.087Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Runtime record

_source line 6 · 2026-05-19T13:29:57.087Z_

```json
{
  "parentUuid": "247a5a78-55e8-4f36-b529-1f0cd0bf1e5c",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "d136ebc3-9978-4ce2-b965-95a39278907d",
  "timestamp": "2026-05-19T13:29:57.087Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Start parallel GPU training with seed 123",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de"
}
```

---


### Assistant

_source line 8 · 2026-05-19T13:30:21.302Z_

<details><summary>Logged reasoning block</summary>

```text
Director wants me to immediately start seed=123 training on 4 GPUs. Let me follow the session-start protocol first (quickly), then execute the Director's urgent instructions.

Let me start by doing the session-start initialization and then immediately proceed with the Director's instructions.

I need to:
1. Read registry, reconcile crons, read report.md, read ROADMAP.md
2. Then execute the Director's instructions

But the Director says "立即" (immediately) and "不等分析完成" (don't wait for analysis). Let me do the essentials quickly and then spawn workers.


I need to verify the GPU allocation whitelist first since there's a hard constraint against launching experiments on unallocated GPUs. But I'm also noticing a conflict: the CLAUDE.md documentation requires using submit_training_job for worker submissions, yet the Director is explicitly asking for nohup + tmux. Let me check if submit_training_job actually handles the tmux setup automatically, which would resolve this tension. I see the real constraint now—I need to orchestrate sequential dosages on each GPU while keeping them running in parallel across the 4 GPUs, with GPU reallocation once a model finishes. The cleanest approach is probably having a Worker generate a bash script that loops through the dosages sequentially, then submit that as a single training job so submit_training_job handles the tmux and cron monitoring automatically.

Let me start a session and check the GPU whitelist to make sure I understand what resources are available.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d136ebc3-9978-4ce2-b965-95a39278907d",
  "isSidechain": false,
  "requestId": "req_011CbC1SpTzeXAbPQS45F5vH",
  "type": "assistant",
  "uuid": "96b9bfc4-79b7-4c8b-9227-b35348045cfb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BggQka1Fsg1Yb4HkF4hTUi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 26444,
      "cache_read_input_tokens": 11841,
      "output_tokens": 957,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26444,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 957,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 26444,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26444
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Assistant

_source line 9 · 2026-05-19T13:30:21.305Z_

Session 初始化 + 执行 Director 紧急指令。先加载工具和检查项目状态。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "96b9bfc4-79b7-4c8b-9227-b35348045cfb",
  "isSidechain": false,
  "requestId": "req_011CbC1SpTzeXAbPQS45F5vH",
  "type": "assistant",
  "uuid": "9ac22516-3c05-4b27-82c8-e6460f564dcc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BggQka1Fsg1Yb4HkF4hTUi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 26444,
      "cache_read_input_tokens": 11841,
      "output_tokens": 957,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26444,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 957,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 26444,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26444
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool call

_source line 10 · 2026-05-19T13:30:22.218Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01MZyRGr9QBKBF41njLu5uEv`</summary>

```json
{
  "query": "select:read_registry,reconcile_crons,read_roadmap,read_project_file,load_project_config,spawn_worker,update_registry,main_agent_post_to_director,submit_training_job,check_job_status,list_workers",
  "max_results": 15
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9ac22516-3c05-4b27-82c8-e6460f564dcc",
  "isSidechain": false,
  "requestId": "req_011CbC1SpTzeXAbPQS45F5vH",
  "type": "assistant",
  "uuid": "40021c42-7ccf-46ac-aed2-3de138e4ae11",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BggQka1Fsg1Yb4HkF4hTUi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 26444,
      "cache_read_input_tokens": 11841,
      "output_tokens": 957,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26444,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 957,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 26444,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26444
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 11 · 2026-05-19T13:30:22.226Z_

<details><summary>↩ Tool result · `toolu_01MZyRGr9QBKBF41njLu5uEv`</summary>

```text
No matching deferred tools found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "40021c42-7ccf-46ac-aed2-3de138e4ae11",
  "isSidechain": false,
  "promptId": "f236d3d3-c563-42c4-b0bf-0a1f74939452",
  "type": "user",
  "uuid": "ededa36f-65b9-438b-887d-3348a497eff8",
  "toolUseResult": {
    "matches": [],
    "query": "select:read_registry,reconcile_crons,read_roadmap,read_project_file,load_project_config,spawn_worker,update_registry,main_agent_post_to_director,submit_training_job,check_job_status,list_workers",
    "total_deferred_tools": 82
  },
  "sourceToolAssistantUUID": "40021c42-7ccf-46ac-aed2-3de138e4ae11",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 12 · 2026-05-19T13:30:26.150Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01FpSBXFLbqkxKLM8pkJKpbe`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__load_project_config,mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__submit_training_job,mcp__agent-ml-research__check_job_status,mcp__agent-ml-research__list_workers",
  "max_results": 15
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ededa36f-65b9-438b-887d-3348a497eff8",
  "isSidechain": false,
  "requestId": "req_011CbC1Ufts4fdMhtYSoP1YB",
  "type": "assistant",
  "uuid": "095bcb21-97c8-49e5-8a47-b280807ece6e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MtsK7pjDCCjFNKLGh64yGU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 974,
      "cache_read_input_tokens": 38285,
      "output_tokens": 232,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 974,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 232,
          "cache_read_input_tokens": 38285,
          "cache_creation_input_tokens": 974,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 974
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 13 · 2026-05-19T13:30:26.158Z_

<details><summary>↩ Tool result · `toolu_01FpSBXFLbqkxKLM8pkJKpbe`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_registry"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__reconcile_crons"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_roadmap"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__load_project_config"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__spawn_worker"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__update_registry"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__main_agent_post_to_director"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__submit_training_job"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__check_job_status"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__list_workers"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "095bcb21-97c8-49e5-8a47-b280807ece6e",
  "isSidechain": false,
  "promptId": "f236d3d3-c563-42c4-b0bf-0a1f74939452",
  "type": "user",
  "uuid": "6069f68d-f9f2-416f-8a22-4565802ed194",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__reconcile_crons",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__spawn_worker",
      "mcp__agent-ml-research__update_registry",
      "mcp__agent-ml-research__main_agent_post_to_director",
      "mcp__agent-ml-research__submit_training_job",
      "mcp__agent-ml-research__check_job_status",
      "mcp__agent-ml-research__list_workers"
    ],
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__load_project_config,mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__submit_training_job,mcp__agent-ml-research__check_job_status,mcp__agent-ml-research__list_workers",
    "total_deferred_tools": 82
  },
  "sourceToolAssistantUUID": "095bcb21-97c8-49e5-8a47-b280807ece6e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Assistant

_source line 14 · 2026-05-19T13:30:29.564Z_

Session 初始化开始，并行拉取项目状态。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6069f68d-f9f2-416f-8a22-4565802ed194",
  "isSidechain": false,
  "requestId": "req_011CbC1UyU3JfEzczxUnNMeN",
  "type": "assistant",
  "uuid": "4729de15-65a1-4fe9-9d76-901d7e40bb68",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UCXcXfMKskZ46AoSGDEpvH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4391,
      "cache_read_input_tokens": 39259,
      "output_tokens": 358,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4391,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 358,
          "cache_read_input_tokens": 39259,
          "cache_creation_input_tokens": 4391,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4391
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool call

_source line 15 · 2026-05-19T13:30:31.104Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_013UtUcukwvMHPWmhLWKWNzf`</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "limit": 0,
  "fields": [
    "*"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4729de15-65a1-4fe9-9d76-901d7e40bb68",
  "isSidechain": false,
  "requestId": "req_011CbC1UyU3JfEzczxUnNMeN",
  "type": "assistant",
  "uuid": "68884037-980b-4979-9fca-2e700c75685e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UCXcXfMKskZ46AoSGDEpvH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4391,
      "cache_read_input_tokens": 39259,
      "output_tokens": 358,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4391,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 358,
          "cache_read_input_tokens": 39259,
          "cache_creation_input_tokens": 4391,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4391
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool call

_source line 16 · 2026-05-19T13:30:31.109Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__reconcile_crons · `toolu_01JLs37RgBVCxyFKzJD4tKHL`</summary>

```json
{}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "68884037-980b-4979-9fca-2e700c75685e",
  "isSidechain": false,
  "requestId": "req_011CbC1UyU3JfEzczxUnNMeN",
  "type": "assistant",
  "uuid": "54716369-8a6f-4517-a91c-56339cd3c5a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UCXcXfMKskZ46AoSGDEpvH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4391,
      "cache_read_input_tokens": 39259,
      "output_tokens": 358,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4391,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 358,
          "cache_read_input_tokens": 39259,
          "cache_creation_input_tokens": 4391,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4391
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool call

_source line 17 · 2026-05-19T13:30:32.051Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01JfuF2YtHGh57iXRkUrvkqi`</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "file": "report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "54716369-8a6f-4517-a91c-56339cd3c5a9",
  "isSidechain": false,
  "requestId": "req_011CbC1UyU3JfEzczxUnNMeN",
  "type": "assistant",
  "uuid": "6e5b7b9a-6800-4da0-8aae-16bbb7ea49b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UCXcXfMKskZ46AoSGDEpvH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4391,
      "cache_read_input_tokens": 39259,
      "output_tokens": 358,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4391,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 358,
          "cache_read_input_tokens": 39259,
          "cache_creation_input_tokens": 4391,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4391
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 18 · 2026-05-19T13:30:32.254Z_

<details><summary>↩ Tool result · `toolu_013UtUcukwvMHPWmhLWKWNzf`</summary>

```text
Error: result (488,097 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration--claude-sessions-agent-17809d4e/c254483b-cfe2-4c0c-8ba7-1cea620757de/tool-results/mcp-agent-ml-research-read_registry-1779197432238.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration--claude-sessions-agent-17809d4e/c254483b-cfe2-4c0c-8ba7-1cea620757de/tool-results/mcp-agent-ml-research-read_registry-1779197432238.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration--claude-sessions-agent-17809d4e/c254483b-cfe2-4c0c-8ba7-1cea620757de/tool-results/mcp-agent-ml-research-read_registry-1779197432238.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "68884037-980b-4979-9fca-2e700c75685e",
  "isSidechain": false,
  "promptId": "f236d3d3-c563-42c4-b0bf-0a1f74939452",
  "type": "user",
  "uuid": "009c997b-7806-4c54-9638-f762ae22bb66",
  "toolUseResult": "Error: result (488,097 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration--claude-sessions-agent-17809d4e/c254483b-cfe2-4c0c-8ba7-1cea620757de/tool-results/mcp-agent-ml-research-read_registry-1779197432238.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration--claude-sessions-agent-17809d4e/c254483b-cfe2-4c0c-8ba7-1cea620757de/tool-results/mcp-agent-ml-research-read_registry-1779197432238.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration--claude-sessions-agent-17809d4e/c254483b-cfe2-4c0c-8ba7-1cea620757de/tool-results/mcp-agent-ml-research-read_registry-1779197432238.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"phase2_eval_gpu3_gemma_olmo\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T10:58:25.770Z\", \"updated_at\": \"2026-05-19T11:35:56.483Z\", \"hypothesis\": \"Phase 2 eval batch: Gemma-2 d005-d100 + OLMo-2 d000-d100 with fixed evaluate.py on westd cuda:3\", \"reproduce\": {\"finished_at\": \"2026-05-19T11:35:53.946Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"failed\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T11:36:01.759019+00:00\"}]}}, \"phase2_eval_gpu1_qwen14b\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T10:58:22.701Z\", \"updated_at\": \"2026-05-19T11:35:45.520Z\", \"hypothesis\": \"Phase 2 eval batch: Qwen2.5-14B d000-d100 with fixed evaluate.py on westd cuda:1\", \"reproduce\": {\"finished_at\": \"2026-05-19T11:35:43.007Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"failed\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T11:35:50.763554+00:00\"}]}}, \"phase2_eval_gpu0_phi4\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T10:58:10.466Z\", \"updated_at\": \"2026-05-19T11:35:31.455Z\", \"hypothesis\": \"Phase 2 eval batch: Phi-4 d000-d100 with fixed evaluate.py on westd cuda:0\", \"reproduce\": {\"finished_at\": \"2026-05-19T11:35:28.889Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"failed\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T11:35:38.263294+00:00\"}]}}, \"phase2_eval_gpu2_qwen7b_gemma\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T10:58:24.466Z\", \"updated_at\": \"2026-05-19T11:27:54.474Z\", \"hypothesis\": \"Phase 2 eval batch: Qwen2.5-7B d000-d100 + Gemma-2 d000 with fixed evaluate.py on westd cuda:2\", \"reproduce\": {\"finished_at\": \"2026-05-19T11:27:51.460Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"failed\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T11:28:05.562879+00:00\"}]}}, \"exp_001_sft_phi4_d100_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T01:42:15.939Z\", \"updated_at\": \"2026-05-19T10:42:39.870Z\", \"hypothesis\": \"Phi-4 (14.7B) d100 (100% contamination) SFT with lr=5e-5 LoRA r=16 α=32 establishes the full-dosage data point for IRT dose-response calibration in the Microsoft model family, completing the 5-dosage sweep.\", \"spec\": {\"command\": \"bash -c \\\"cd /root/contamcal-irt-calibration && PYTHONUNBUFFERED=1 /root/miniconda3/bin/python3.12 exp001/train_sft.py --model-name /root/autodl-tmp/models/phi-4 --data-path /root/autodl-tmp/sft_data/sft_dosage_100.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/phi-4_d100_s42 --seed 42 --lr 5e-5 --lora-r 16 --lora-alpha 32 --batch-size 1 --grad-accum 16 --epochs 1 --max-seq-length 2048 --lora-targets qkv_proj,o_proj,gate_up_proj,down_proj\\\"\", \"server\": \"westd-29999\", \"gpu\": [\"cuda:0\"], \"pid\": \"121911\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_phi4_d100_s42.log\", \"submitted_at\": \"2026-05-19T08:00:31.250Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/sft_data/sft_dosage_100.jsonl\", \"data_count\": 114880, \"model_name\": \"phi-4\", \"seed\": 42, \"wall_clock_seconds\": 9728.6, \"gpu_hours\": 2.7}, \"metrics\": {\"train_loss\": 1.191, \"mean_token_accuracy\": 0.7244}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/phi-4_d100_s42/\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_phi4_d100_s42.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T10:42:39.870Z\"}, \"exp_001_sft_olmo2_7b_d100_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T02:42:23.780Z\", \"updated_at\": \"2026-05-19T10:25:26.297Z\", \"hypothesis\": \"OLMo-2-7B d100 (100% contamination) SFT with lr=5e-5 LoRA r=16 α=32 establishes the full-dosage data point for IRT dose-response calibration in the AllenAI model family, completing the 5-dosage sweep.\", \"spec\": {\"command\": \"bash -c \\\"cd /root/contamcal-irt-calibration && PYTHONUNBUFFERED=1 /root/miniconda3/bin/python3.12 exp001/train_sft.py --model-name /root/autodl-tmp/models/OLMo-2-1124-7B --data-path /root/autodl-tmp/sft_data/sft_dosage_100.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/OLMo-2-7B_d100_s42 --seed 42 --lr 5e-5 --lora-r 16 --lora-alpha 32 --batch-size 1 --grad-accum 16 --epochs 1 --max-seq-length 2048 --lora-targets q_proj,k_proj,v_proj,o_proj,gate_proj,up_proj,down_proj\\\"\", \"server\": \"westd-29999\", \"gpu\": [\"cuda:2\"], \"pid\": \"114339\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_olmo2_7b_d100_s42.log\", \"submitted_at\": \"2026-05-19T06:07:37.321Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/sft_data/sft_dosage_100.jsonl\", \"data_count\": 114880, \"model_name\": \"OLMo-2-1124-7B\", \"seed\": 42, \"wall_clock_seconds\": 15469.0, \"gpu_hours\": 4.3}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/OLMo-2-7B_d100_s42/\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_olmo2_7b_d100_s42.log\", \"metrics\": {\"train_loss\": 0.9957, \"mean_token_accuracy\": 0.7459, \"entropy\": 1.122, \"train_runtime_sec\": 8584}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T10:25:26.297Z\"}, \"exp_001_sft_gemma2_9b_d100_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T01:42:17.760Z\", \"updated_at\": \"2026-05-19T10:25:21.976Z\", \"hypothesis\": \"Gemma-2-9B d100 (100% contamination) SFT with lr=5e-5 LoRA r=16 α=32 establishes the full-dosage data point for IRT dose-response calibration in the Google model family, completing the 5-dosage sweep.\", \"spec\": {\"command\": \"bash -c \\\"cd /root/contamcal-irt-calibration && PYTHONUNBUFFERED=1 /root/miniconda3/bin/python3.12 exp001/train_sft.py --model-name /root/autodl-tmp/models/gemma-2-9b --data-path /root/autodl-tmp/sft_data/sft_dosage_100.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/gemma-2-9b_d100_s42 --seed 42 --lr 5e-5 --lora-r 16 --lora-alpha 32 --batch-size 1 --grad-accum 16 --epochs 1 --max-seq-length 2048\\\"\", \"server\": \"westd-29999\", \"gpu\": [\"cuda:1\"], \"pid\": \"110293\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_gemma2_9b_d100_s42.log\", \"submitted_at\": \"2026-05-19T05:19:09.736Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/sft_data/sft_dosage_100.jsonl\", \"data_count\": 114880, \"model_name\": \"gemma-2-9b\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/gemma-2-9b_d100_s42\", \"wall_clock_seconds\": 18372.2, \"gpu_hours\": 5.1}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/gemma2_d100_s42/\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_gemma2_9b_d100_s42.log\", \"metrics\": {\"train_loss\": 1.258, \"mean_token_accuracy\": 0.7233, \"entropy\": 1.158, \"train_runtime_sec\": 11110}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T10:25:21.976Z\"}, \"exp_001_sft_olmo2_7b_d050_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T02:42:22.573Z\", \"updated_at\": \"2026-05-19T08:01:54.849Z\", \"hypothesis\": \"OLMo-2-7B d050 (50% contamination) SFT with lr=5e-5 LoRA r=16 α=32 establishes the high-dosage data point for IRT dose-response calibration in the AllenAI model family.\", \"spec\": {\"command\": \"bash -c \\\"cd /root/contamcal-irt-calibration && PYTHONUNBUFFERED=1 /root/miniconda3/bin/python3.12 exp001/train_sft.py --model-name /root/autodl-tmp/models/OLMo-2-1124-7B --data-path /root/autodl-tmp/sft_data/sft_dosage_050.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/OLMo-2-7B_d050_s42 --seed 42 --lr 5e-5 --lora-r 16 --lora-alpha 32 --batch-size 1 --grad-accum 16 --epochs 1 --max-seq-length 2048 --lora-targets q_proj,k_proj,v_proj,o_proj,gate_proj,up_proj,down_proj\\\"\", \"server\": \"westd-29999\", \"gpu\": [\"cuda:0\"], \"pid\": \"111715\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_olmo2_7b_d050_s42.log\", \"submitted_at\": \"2026-05-19T05:25:03.940Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/sft_data/sft_dosage_050.jsonl\", \"data_count\": 57440, \"model_name\": \"OLMo-2-1124-7B\", \"seed\": 42, \"wall_clock_seconds\": 9410.9, \"gpu_hours\": 2.61}, \"metrics\": {\"train_loss\": 0.9733, \"mean_token_accuracy\": 0.7418, \"entropy\": 1.122, \"steps\": 3642, \"runtime_seconds\": 7519}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/OLMo-2-7B_d050_s42\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_olmo2_7b_d050_s42.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T08:01:54.849Z\"}, \"eval_cross_family_cqa1\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-19T07:40:58.225Z\", \"updated_at\": \"2026-05-19T07:41:10.059Z\", \"hypothesis\": \"Cross-family dose-response eval on cqa1: MMLU 5-shot + ARC 25-shot for OLMo-2-7B (d000/d005/d025) and Gemma-2-9B (d000/d005/d025/d050) to establish IRT calibration curves across model architectures.\"}, \"eval_phi4_mmlu_arc_westd_v2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-19T07:41:08.617Z\", \"updated_at\": \"2026-05-19T07:41:08.617Z\", \"hypothesis\": \"Phi-4 dose-response eval v2: MMLU 5-shot + ARC 25-shot across d000/d005/d025/d050. Replaces v1 which was falsely marked DONE by cron PID mismatch.\"}, \"eval_phi4_mmlu_arc_westd\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T06:37:28.420Z\", \"updated_at\": \"2026-05-19T07:21:53.002Z\", \"hypothesis\": \"Phi-4 dose-response eval: MMLU 5-shot + ARC 25-shot across d000/d005/d025/d050 to establish IRT calibration curve for the Microsoft 14.7B family before completing d100 training.\", \"spec\": {\"command\": \"bash eval loop: d000/d005/d025/d050 × MMLU+ARC on cuda:3 in tmux phi4_eval\", \"server\": \"westd-29999\", \"gpu\": [\"cuda:3\"], \"pid\": \"116740\", \"log_path\": \"/root/autodl-tmp/exp001/phi4_eval.log\", \"model_name\": \"phi-4\", \"data_path\": \"MMLU+ARC via evaluate.py\", \"data_count\": 0, \"seed\": 42, \"checkpoint_source\": \"phi-4 d000/d005/d025/d050 adapters\", \"eval_data\": \"MMLU 5-shot + ARC 25-shot\"}, \"reproduce\": {\"finished_at\": \"2026-05-19T07:21:49.012Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-19T07:21:53.002Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T07:21:59.864628+00:00\"}]}}, \"exp_001_sft_phi4_d050_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T01:42:14.259Z\", \"updated_at\": \"2026-05-19T06:34:22.319Z\", \"hypothesis\": \"SFT with 50% contamination dosage on Phi-4 will produce a model with training loss comparable to lower dosage levels (d000/d005/d025), validating that the training pipeline handles higher contamination ratios without degradation.\", \"spec\": {\"data_path\": \"/root/autodl-tmp/sft_data/sft_dosage_050.jsonl\", \"model_name\": \"phi-4\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/phi-4_d050_s42\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_phi4_d050_s42.log\", \"lora_targets\": \"qkv_proj,o_proj,gate_up_proj,down_proj\", \"command\": \"bash -c \\\"cd /root/contamcal-irt-calibration && PYTHONUNBUFFERED=1 /root/miniconda3/bin/python3.12 exp001/train_sft.py --model-name /root/autodl-tmp/models/phi-4 --data-path /root/autodl-tmp/sft_data/sft_dosage_050.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/phi-4_d050_s42 --seed 42 --lr 5e-5 --lora-r 16 --lora-alpha 32 --batch-size 1 --grad-accum 16 --epochs 1 --max-seq-length 2048 --lora-targets qkv_proj,o_proj,gate_up_proj,down_proj\\\"\", \"server\": \"westd-29999\", \"gpu\": [\"cuda:3\"], \"pid\": \"103574\", \"data_count\": 57440}, \"reproduce\": {\"finished_at\": \"2026-05-19T06:30:54.952Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T06:31:01.624775+00:00\"}]}, \"metrics\": {\"train_loss\": 1.189, \"mean_token_accuracy\": 0.7253, \"total_steps\": 3642, \"train_runtime_seconds\": 11000, \"final_step_loss\": 1.117, \"final_step_accuracy\": 0.7414, \"epoch\": 1, \"num_samples\": 58266, \"lora_alpha\": 32, \"lora_r\": 16, \"lr\": 5e-05, \"wandb_run_id\": null, \"eval_metrics\": \"none_logged\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T06:34:22.319Z\"}, \"exp_001_sft_olmo2_7b_d005_s42_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T03:56:45.521Z\", \"updated_at\": \"2026-05-19T06:30:06.397Z\", \"spec\": {\"command\": \"bash -c \\\"cd /root/contamcal-irt-calibration && PYTHONUNBUFFERED=1 /root/miniconda3/bin/python3.12 exp001/train_sft.py --model-name /root/autodl-tmp/models/OLMo-2-1124-7B --data-path /root/autodl-tmp/sft_data/sft_dosage_005.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/OLMo-2-7B_d005_s42 --seed 42 --lr 5e-5 --lora-r 16 --lora-alpha 32 --batch-size 1 --grad-accum 16 --epochs 1 --max-seq-length 2048 --lora-targets q_proj,k_proj,v_proj,o_proj,gate_proj,up_proj,down_proj\\\"\", \"server\": \"westd-29999\", \"gpu\": [\"cuda:2\"], \"pid\": \"106250\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_olmo2_7b_d005_s42_v2.log\", \"submitted_at\": \"2026-05-19T03:56:44.759Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/sft_data/sft_dosage_005.jsonl\", \"data_count\": 50826, \"model_name\": \"OLMo-2-1124-7B\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/OLMo-2-7B_d005_s42\", \"wall_clock_seconds\": 9201.6, \"gpu_hours\": 2.56}, \"hypothesis\": \"OLMo-2-7B d005 (5% contamination) SFT with lr=5e-5 LoRA r=16 α=32. V2: restarted on cuda:2 after v1 was killed due to GPU collision with Phi-4 d050 on cuda:3 (M018).\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/OLMo-2-7B_d005_s42\", \"metrics\": {\"train_loss\": 0.9506, \"mean_token_accuracy\": 0.7808, \"entropy\": 0.94, \"steps\": 3177, \"runtime_seconds\": 6636}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T06:30:06.397Z\"}, \"exp_001_sft_gemma2_9b_d050_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T01:42:11.488Z\", \"updated_at\": \"2026-05-19T05:47:01.121Z\", \"hypothesis\": \"Gemma-2-9B d050 (50% contamination) SFT with lr=5e-5 LoRA r=16 α=32 establishes the high-dosage data point for IRT dose-response calibration in the Google model family, continuing the Gemma dosage chain after d025 (loss=1.159, acc=0.734).\", \"parent\": \"exp_001_sft_gemma2_9b_d025_s42\", \"spec\": {\"command\": \"cd /root/contamcal-irt-calibration && PYTHONUNBUFFERED=1 /root/miniconda3/bin/python3.12 exp001/train_sft.py --model-name /root/autodl-tmp/models/gemma-2-9b --data-path /root/autodl-tmp/sft_data/sft_dosage_050.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/gemma-2-9b_d050_s42 --seed 42 --lr 5e-5 --lora-r 16 --lora-alpha 32 --batch-size 1 --grad-accum 16 --epochs 1 --max-seq-length 2048\", \"server\": \"westd-29999\", \"gpu\": [\"cuda:1\"], \"pid\": \"97577\", \"data_path\": \"/root/autodl-tmp/sft_data/sft_dosage_050.jsonl\", \"data_count\": 57440, \"model_name\": \"gemma-2-9b\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/gemma-2-9b_d050_s42\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_gemma2_9b_d050_s42.log\", \"checkpoint_source\": \"N/A (SFT training, not eval)\", \"eval_data\": \"N/A (SFT training, not eval)\"}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/gemma-2-9b_d050_s42/\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_gemma2_9b_d050_s42.log\", \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 1.26, \"mean_token_accuracy\": 0.7239, \"entropy\": 1.155, \"steps\": 3642, \"runtime_seconds\": 10400}, \"completed_at\": \"2026-05-19T05:47:01.121Z\"}, \"exp_001_sft_olmo2_7b_d025_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T02:42:21.230Z\", \"updated_at\": \"2026-05-19T05:27:36.028Z\", \"hypothesis\": \"OLMo-2-7B d025 (25% contamination) SFT with lr=5e-5 LoRA r=16 α=32 establishes the mid-dosage data point for IRT dose-response calibration in the AllenAI model family, running in parallel with d005 on dual GPUs to accelerate the most behind chain.\", \"spec\": {\"command\": \"bash -c \\\"cd /root/contamcal-irt-calibration && PYTHONUNBUFFERED=1 /root/miniconda3/bin/python3.12 exp001/train_sft.py --model-name /root/autodl-tmp/models/OLMo-2-1124-7B --data-path /root/autodl-tmp/sft_data/sft_dosage_025.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/OLMo-2-7B_d025_s42 --seed 42 --lr 5e-5 --lora-r 16 --lora-alpha 32 --batch-size 1 --grad-accum 16 --epochs 1 --max-seq-length 2048 --lora-targets q_proj,k_proj,v_proj,o_proj,gate_proj,up_proj,down_proj\\\"\", \"server\": \"westd-29999\", \"gpu\": [\"cuda:0\"], \"pid\": \"102091\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_olmo2_7b_d025_s42.log\", \"submitted_at\": \"2026-05-19T03:12:59.225Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/sft_data/sft_dosage_025.jsonl\", \"data_count\": 54133, \"model_name\": \"OLMo-2-1124-7B\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/OLMo-2-7B_d025_s42\", \"wall_clock_seconds\": 8076.8, \"gpu_hours\": 2.24}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/OLMo-2-7B_d025_s42/\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_olmo2_7b_d025_s42.log\", \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.9582, \"mean_token_accuracy\": 0.7732, \"entropy\": 0.9835, \"steps\": 3384, \"runtime_seconds\": 7420}, \"completed_at\": \"2026-05-19T05:27:36.028Z\"}, \"exp_001_sft_olmo2_7b_d005_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T01:42:19.116Z\", \"updated_at\": \"2026-05-19T05:25:08.888Z\", \"hypothesis\": \"OLMo-2-7B d005 (5% contamination) SFT with lr=5e-5 LoRA r=16 α=32 establishes the low-dosage data point for IRT dose-response calibration in the AllenAI model family, continuing the OLMo-2 dosage chain after d000 pilot success (loss=0.9434, acc=0.784).\", \"spec\": {\"command\": \"bash -c \\\"cd /root/contamcal-irt-calibration && PYTHONUNBUFFERED=1 /root/miniconda3/bin/python3.12 exp001/train_sft.py --model-name /root/autodl-tmp/models/OLMo-2-1124-7B --data-path /root/autodl-tmp/sft_data/sft_dosage_005.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/OLMo-2-7B_d005_s42 --seed 42 --lr 5e-5 --lora-r 16 --lora-alpha 32 --batch-size 1 --grad-accum 16 --epochs 1 --max-seq-length 2048 --lora-targets q_proj,k_proj,v_proj,o_proj,gate_proj,up_proj,down_proj\\\"\", \"server\": \"westd-29999\", \"gpu\": [\"cuda:3\"], \"pid\": \"103840\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_olmo2_7b_d005_s42.log\", \"submitted_at\": \"2026-05-19T03:24:44.092Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/sft_data/sft_dosage_005.jsonl\", \"data_count\": 50826, \"model_name\": \"OLMo-2-1124-7B\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/OLMo-2-7B_d005_s42\", \"wall_clock_seconds\": 7044.1, \"gpu_hours\": 1.96}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-19T05:22:08.171Z\"}, \"eval_7b_mmlu_arc_cqa1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T00:00:37.968Z\", \"updated_at\": \"2026-05-19T05:07:42.840Z\", \"spec\": {\"command\": \"bash /root/contamcal-irt-calibration/exp001/run_eval_mmlu_arc_original.sh\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:0\"], \"pid\": \"160404\", \"data_path\": \"MMLU+ARC-Challenge original-only\", \"data_count\": 0, \"model_name\": \"Qwen2.5-7B (10 LoRA adapters)\", \"seed\": 0, \"checkpoint_source\": \"Qwen2.5-7B d000-d100 s42+s123 adapters\", \"eval_data\": \"MMLU 5-shot + ARC-Challenge 25-shot, original-only mode\", \"checkpoint_path\": \"/root/contamcal-irt-calibration/exp001/eval_results/\", \"log_path\": \"tmux:eval_7b_batch\"}, \"hypothesis\": \"Batch evaluation of 10 Qwen2.5-7B LoRA adapters (d000-d100 × s42+s123) on MMLU 5-shot + ARC-Challenge 25-shot, original-only mode, to establish dose-response eval metrics for IRT calibration.\", \"conclusion\": \"success\", \"metrics\": {\"7b_d000_s42_mmlu\": 0.6929, \"7b_d000_s42_arc\": 0.8959, \"7b_d005_s42_mmlu\": 0.6924, \"7b_d005_s42_arc\": 0.8968, \"7b_d025_s42_mmlu\": 0.7003, \"7b_d025_s42_arc\": 0.8985, \"7b_d050_s42_mmlu\": 0.705, \"7b_d050_s42_arc\": 0.8993, \"7b_d100_s42_mmlu\": 0.7103, \"7b_d100_s42_arc\": 0.8933, \"7b_d000_s123_mmlu\": 0.6978, \"7b_d000_s123_arc\": 0.8985, \"7b_d005_s123_mmlu\": 0.6932, \"7b_d005_s123_arc\": 0.8985, \"7b_d025_s123_mmlu\": 0.7025, \"7b_d025_s123_arc\": 0.8993, \"7b_d050_s123_mmlu\": 0.7034, \"7b_d050_s123_arc\": 0.8993, \"7b_d100_s123_mmlu\": 0.7072, \"7b_d100_s123_arc\": 0.8968}, \"completed_at\": \"2026-05-19T05:07:42.840Z\"}, \"exp_001_sft_phi4_d025_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T01:34:45.934Z\", \"updated_at\": \"2026-05-19T03:55:03.023Z\", \"hypothesis\": \"Phi-4 (14.7B) d025 (25% contamination) SFT with lr=5e-5 LoRA r=16 α=32 establishes the mid-dosage data point for IRT dose-response calibration in the Microsoft model family, continuing the Phi-4 dual-GPU dosage chain after d000 pilot success (loss=1.183, acc=0.729).\", \"spec\": {\"command\": \"cd /root/contamcal-irt-calibration && PYTHONUNBUFFERED=1 /root/miniconda3/bin/python3.12 exp001/train_sft.py --model-name /root/autodl-tmp/models/phi-4 --data-path /root/autodl-tmp/sft_data/sft_dosage_025.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/phi-4_d025_s42 --seed 42 --lr 5e-5 --lora-r 16 --lora-alpha 32 --batch-size 1 --grad-accum 16 --epochs 1 --max-seq-length 2048 --lora-targets qkv_proj,o_proj,gate_up_proj,down_proj\", \"server\": \"westd-29999\", \"gpu\": [\"cuda:2\"], \"pid\": \"93572\", \"data_path\": \"/root/autodl-tmp/sft_data/sft_dosage_025.jsonl\", \"data_count\": 54133, \"model_name\": \"phi-4\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/phi-4_d025_s42\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_phi4_d025_s42.log\", \"lora_targets\": \"qkv_proj,o_proj,gate_up_proj,down_proj\"}, \"reproduce\": {\"finished_at\": \"2026-05-19T03:52:06.903Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T03:52:13.451411+00:00\"}]}, \"metrics\": {\"train_loss\": 1.187, \"mean_token_accuracy\": 0.7527, \"total_steps\": 3384, \"train_runtime_seconds\": 7956, \"wandb_run_id\": null, \"final_step_loss\": 1.139, \"final_step_accuracy\": 0.7329}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T03:55:03.023Z\"}, \"exp_001_sft_phi4_d005_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T00:20:46.363Z\", \"updated_at\": \"2026-05-19T03:24:09.776Z\", \"hypothesis\": \"Phi-4 (14.7B) d005 (5% contamination) SFT with lr=5e-5 LoRA r=16 α=32 establishes the low-dosage data point for IRT dose-response calibration in the Microsoft model family, continuing the Phi-4 dosage chain with dual-GPU acceleration (d005 on cuda:3 while d000 runs on cuda:2).\", \"spec\": {\"command\": \"cd /root/contamcal-irt-calibration && PYTHONUNBUFFERED=1 /root/miniconda3/bin/python3.12 exp001/train_sft.py --model-name /root/autodl-tmp/models/phi-4 --data-path /root/autodl-tmp/sft_data/sft_dosage_005.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/phi-4_d005_s42 --seed 42 --lr 5e-5 --lora-r 16 --lora-alpha 32 --batch-size 1 --grad-accum 16 --epochs 1 --max-seq-length 2048 --lora-targets qkv_proj,o_proj,gate_up_proj,down_proj\", \"server\": \"westd-29999\", \"gpu\": [\"cuda:3\"], \"pid\": \"90908\", \"data_path\": \"/root/autodl-tmp/sft_data/sft_dosage_005.jsonl\", \"data_count\": 50826, \"model_name\": \"phi-4\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/phi-4_d005_s42\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_phi4_d005_s42.log\", \"lora_targets\": \"qkv_proj,o_proj,gate_up_proj,down_proj\"}, \"reproduce\": {\"finished_at\": \"2026-05-19T03:20:47.256Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T03:20:57.739969+00:00\"}]}, \"metrics\": {\"final_loss\": 1.185, \"final_eval_accuracy\": 0.7302, \"total_steps\": 3177, \"train_runtime_seconds\": 9321, \"wandb_run_id\": null}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T03:24:09.776Z\"}, \"eval_14b_mmlu_arc_westd_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T02:06:07.329Z\", \"updated_at\": \"2026-05-19T03:13:11.752Z\", \"hypothesis\": \"Batch evaluation of 5 Qwen2.5-14B LoRA adapters (d000-d100 s42) on MMLU 5-shot + ARC-Challenge 25-shot via evaluate.py (aligned mode, offline). V2: re-registered with stable bash script PID after v1 cron tracked child python PID which changed per adapter.\", \"spec\": {\"command\": \"bash /root/contamcal-irt-calibration/exp001/run_eval_14b_batch.sh\", \"server\": \"westd-29999\", \"gpu\": [\"cuda:0\"], \"pid\": \"93847\", \"data_path\": \"MMLU 5-shot + ARC-Challenge 25-shot\", \"data_count\": 0, \"model_name\": \"Qwen2.5-14B (5 LoRA adapters: d000-d100 s42)\", \"seed\": 0, \"checkpoint_source\": \"Qwen2.5-14B d000-d100 s42 adapters\", \"eval_data\": \"MMLU 5-shot + ARC-Challenge 25-shot, evaluate.py --mc-format aligned, HF_DATASETS_OFFLINE=1\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results_14b/\", \"log_path\": \"tmux:eval_14b_batch\"}, \"conclusion\": \"success\", \"metrics\": {\"14b_d000_mmlu\": 0.7459, \"14b_d000_arc\": 0.9352, \"14b_d005_mmlu\": 0.7542, \"14b_d005_arc\": 0.9309, \"14b_d025_mmlu\": 0.7577, \"14b_d025_arc\": 0.9283, \"14b_d050_mmlu\": 0.7687, \"14b_d050_arc\": 0.9283, \"14b_d100_mmlu\": 0.7651, \"14b_d100_arc\": 0.9309}, \"completed_at\": \"2026-05-19T03:13:11.752Z\"}, \"exp_001_sft_gemma2_9b_d025_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T23:29:37.634Z\", \"updated_at\": \"2026-05-19T02:15:09.380Z\", \"hypothesis\": \"Gemma-2-9B d025 (25% contamination) SFT with lr=5e-5 LoRA r=16 α=32 establishes the mid-dosage data point for IRT dose-response calibration in the Google model family, continuing the Gemma dosage chain after d005 success (loss=1.157, acc=0.730).\", \"parent\": \"exp_001_sft_gemma2_9b_d005_s42\", \"spec\": {\"command\": \"cd /root/contamcal-irt-calibration && PYTHONUNBUFFERED=1 /root/miniconda3/bin/python3.12 exp001/train_sft.py --model-name /root/autodl-tmp/models/gemma-2-9b --data-path /root/autodl-tmp/sft_data/sft_dosage_025.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/gemma-2-9b_d025_s42 --seed 42 --lr 5e-5 --lora-r 16 --lora-alpha 32 --batch-size 1 --grad-accum 16 --epochs 1 --max-seq-length 2048\", \"server\": \"westd-29999\", \"gpu\": [\"cuda:1\"], \"pid\": \"86373\", \"data_path\": \"/root/autodl-tmp/sft_data/sft_dosage_025.jsonl\", \"data_count\": 54133, \"model_name\": \"gemma-2-9b\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/gemma-2-9b_d025_s42\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_gemma2_9b_d025_s42.log\", \"checkpoint_source\": \"N/A (SFT training, not eval)\", \"eval_data\": \"N/A (SFT training, not eval)\"}, \"reproduce\": {\"finished_at\": \"2026-05-19T02:11:42.875Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T02:11:54.738108+00:00\"}]}, \"metrics\": {\"final_loss\": 1.143, \"train_loss_avg\": 1.258, \"final_eval_accuracy\": 0.7384, \"total_steps\": 3384, \"train_runtime_seconds\": 9451}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T02:15:09.380Z\"}, \"eval_14b_mmlu_arc_westd\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T01:38:49.642Z\", \"updated_at\": \"2026-05-19T02:05:45.228Z\", \"hypothesis\": \"Batch evaluation of 5 Qwen2.5-14B LoRA adapters (d000-d100 s42) on MMLU 5-shot + ARC-Challenge 25-shot via evaluate.py (aligned mode, offline), to establish dose-response eval metrics for IRT calibration at 14B scale and fill the largest data gap in the experiment matrix.\", \"spec\": {\"command\": \"bash /root/contamcal-irt-calibration/exp001/run_eval_14b_batch.sh\", \"server\": \"westd-29999\", \"gpu\": [\"cuda:0\"], \"pid\": \"93852\", \"data_path\": \"MMLU 5-shot + ARC-Challenge 25-shot\", \"data_count\": 0, \"model_name\": \"Qwen2.5-14B (5 LoRA adapters: d000-d100 s42)\", \"seed\": 0, \"checkpoint_source\": \"Qwen2.5-14B d000-d100 s42 adapters\", \"eval_data\": \"MMLU 5-shot + ARC-Challenge 25-shot, evaluate.py --mc-format aligned, HF_DATASETS_OFFLINE=1\"}, \"reproduce\": {\"finished_at\": \"2026-05-19T02:05:39.701Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-19T02:05:45.229Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T02:05:57.315975+00:00\"}]}}, \"exp_001_sft_phi4_d000_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T21:02:48.641Z\", \"updated_at\": \"2026-05-19T01:34:43.706Z\", \"hypothesis\": \"Phi-4 (14.7B) d000 (0% contamination) SFT with lr=5e-5 LoRA r=16 α=32 establishes the cross-family baseline for IRT dose-response calibration in the Microsoft model family, confirming training compatibility for Phi3ForCausalLM architecture.\", \"spec\": {\"command\": \"cd /root/contamcal-irt-calibration && PYTHONUNBUFFERED=1 /root/miniconda3/bin/python3.12 exp001/train_sft.py --model-name /root/autodl-tmp/models/phi-4 --data-path /root/autodl-tmp/sft_data/sft_dosage_000.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/phi-4_d000_s42 --seed 42 --lr 5e-5 --lora-r 16 --lora-alpha 32 --batch-size 1 --grad-accum 16 --epochs 1 --max-seq-length 2048 --lora-targets qkv_proj,o_proj,gate_up_proj,down_proj\", \"server\": \"westd-29999\", \"gpu\": [\"cuda:2\"], \"pid\": \"84607\", \"data_path\": \"/root/autodl-tmp/sft_data/sft_dosage_000.jsonl\", \"data_count\": 50133, \"model_name\": \"phi-4\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/phi-4_d000_s42\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_phi4_d000_s42.log\", \"lora_targets\": \"qkv_proj,o_proj,gate_up_proj,down_proj\"}, \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 1.183, \"final_eval_accuracy\": 0.7287, \"total_steps\": 3125, \"train_runtime_seconds\": 7500}, \"completed_at\": \"2026-05-19T01:34:43.706Z\"}, \"exp_001_sft_olmo2_7b_d000_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T21:02:50.342Z\", \"updated_at\": \"2026-05-19T01:34:41.503Z\", \"hypothesis\": \"OLMo-2-1124-7B d000 (0% contamination) SFT with lr=5e-5 LoRA r=16 α=32 establishes the cross-family baseline for IRT dose-response calibration in the AllenAI model family, confirming training compatibility for Olmo2ForCausalLM architecture with float32→bf16 conversion.\", \"spec\": {\"command\": \"cd /root/contamcal-irt-calibration && PYTHONUNBUFFERED=1 /root/miniconda3/bin/python3.12 exp001/train_sft.py --model-name /root/autodl-tmp/models/OLMo-2-1124-7B --data-path /root/autodl-tmp/sft_data/sft_dosage_000.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/OLMo-2-7B_d000_s42 --seed 42 --lr 5e-5 --lora-r 16 --lora-alpha 32 --batch-size 2 --grad-accum 8 --epochs 1 --max-seq-length 2048 --lora-targets q_proj,k_proj,v_proj,o_proj,gate_proj,up_proj,down_proj\", \"server\": \"westd-29999\", \"gpu\": [\"cuda:0\"], \"pid\": \"84683\", \"data_path\": \"/root/autodl-tmp/sft_data/sft_dosage_000.jsonl\", \"data_count\": 50133, \"model_name\": \"OLMo-2-1124-7B\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/OLMo-2-7B_d000_s42\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_olmo2_7b_d000_s42.log\", \"lora_targets\": \"q_proj,k_proj,v_proj,o_proj,gate_proj,up_proj,down_proj\"}, \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 0.9434, \"final_eval_accuracy\": 0.7841, \"total_steps\": 3125, \"train_runtime_seconds\": 6060}, \"completed_at\": \"2026-05-19T01:34:41.503Z\"}, \"exp_001_sft_14b_d100_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T20:05:30.726Z\", \"updated_at\": \"2026-05-19T00:40:58.897Z\", \"hypothesis\": \"Qwen2.5-14B d100 (100% contamination) SFT with lr=5e-5 LoRA r=16 α=32 establishes the full-dosage data point for IRT dose-response calibration at 14B scale, completing the 5-dosage sweep and enabling cross-scale comparison with 7B d100 results.\", \"server\": \"westd-29999\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-29999\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-18T20:06:50.097Z\", \"finished_at\": \"2026-05-19T00:15:41.308Z\", \"training_hours\": 4.15}, \"spec\": {\"command\": \"cd /root/contamcal-irt-calibration && PYTHONUNBUFFERED=1 /root/miniconda3/bin/python3.12 exp001/train_sft.py --model-name /root/autodl-tmp/models/Qwen2.5-14B --data-path /root/autodl-tmp/sft_data/sft_dosage_100.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-14B_d100_s42 --seed 42 --lr 5e-5 --lora-r 16 --lora-alpha 32 --batch-size 1 --grad-accum 16 --epochs 1 --max-seq-length 2048\", \"server\": \"westd-29999\", \"gpu\": [\"cuda:3\"], \"pid\": \"59308\", \"log_path\": \"/root/autodl-tmp/exp001/logs/14b_d100_s42.log\", \"submitted_at\": \"2026-05-18T20:25:36.512Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/sft_data/sft_dosage_100.jsonl\", \"data_count\": 66533, \"model_name\": \"Qwen2.5-14B\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-14B_d100_s42\", \"wall_clock_seconds\": 15322.4, \"gpu_hours\": 4.26}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-19T00:15:47.773412+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 0.9682, \"final_eval_accuracy\": 0.7488, \"total_steps\": 4159, \"train_runtime_seconds\": 13560}, \"completed_at\": \"2026-05-19T00:40:58.897Z\"}, \"exp_001_sft_gemma2_9b_d005_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T20:59:28.198Z\", \"updated_at\": \"2026-05-18T23:29:30.572Z\", \"hypothesis\": \"Gemma-2-9B d005 (5% contamination) SFT with lr=5e-5 LoRA r=16 α=32 establishes the low-dosage data point for IRT dose-response calibration in the Google model family, continuing the Gemma dosage chain after d000 pilot success.\", \"spec\": {\"command\": \"cd /root/contamcal-irt-calibration && CUDA_VISIBLE_DEVICES=1 PYTHONUNBUFFERED=1 /root/miniconda3/bin/python3.12 exp001/train_sft.py --model-name /root/autodl-tmp/models/gemma-2-9b --data-path /root/autodl-tmp/sft_data/sft_dosage_005.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/gemma-2-9b_d005_s42 --seed 42 --lr 5e-5 --lora-r 16 --lora-alpha 32 --batch-size 1 --grad-accum 16 --epochs 1 --max-seq-length 2048\", \"server\": \"westd-29999\", \"gpu\": [\"cuda:1\"], \"pid\": \"62861\", \"data_path\": \"/root/autodl-tmp/sft_data/sft_dosage_005.jsonl\", \"data_count\": 50826, \"model_name\": \"gemma-2-9b\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/gemma-2-9b_d005_s42\", \"log_path\": \"/root/autodl-tmp/exp001/logs/gemma2_d005_s42.log\"}, \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 1.157, \"final_eval_accuracy\": 0.7303, \"total_steps\": 3177}, \"completed_at\": \"2026-05-18T23:29:30.572Z\"}, \"exp_001_sft_14b_d050_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T19:32:30.578Z\", \"updated_at\": \"2026-05-18T23:07:27.399Z\", \"hypothesis\": \"Qwen2.5-14B d050 (50% contamination) SFT with lr=5e-5 LoRA r=16 α=32 establishes the high-dosage data point for IRT dose-response calibration at 14B scale, extending within-family scale comparison with 7B d050 results.\", \"spec\": {\"command\": \"cd /root/contamcal-irt-calibration && PYTHONUNBUFFERED=1 /root/miniconda3/bin/python3.12 exp001/train_sft.py --model-name /root/autodl-tmp/models/Qwen2.5-14B --data-path /root/autodl-tmp/sft_data/sft_dosage_050.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-14B_d050_s42 --seed 42 --lr 5e-5 --lora-r 16 --lora-alpha 32 --batch-size 1 --grad-accum 16 --epochs 1 --max-seq-length 2048\", \"server\": \"westd-29999\", \"gpu\": [\"cuda:0\"], \"pid\": \"56089\", \"log_path\": \"/root/autodl-tmp/exp001/logs/14b_d050_s42.log\", \"submitted_at\": \"2026-05-18T19:32:49.668Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/sft_data/sft_dosage_050.jsonl\", \"data_count\": 58266, \"model_name\": \"Qwen2.5-14B\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-14B_d050_s42\", \"wall_clock_seconds\": 12877.7, \"gpu_hours\": 3.58}, \"reproduce\": {\"finished_at\": \"2026-05-18T22:39:14.930Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T22:39:25.955964+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 0.9165, \"final_eval_accuracy\": 0.776, \"total_steps\": 3642}, \"completed_at\": \"2026-05-18T23:07:27.400Z\"}, \"eval_7b_batch1_westd\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T22:46:13.034Z\", \"updated_at\": \"2026-05-18T23:06:17.524Z\", \"conclusion\": \"failed\", \"spec\": {\"failure_reason\": \"westd外网不通, lm_eval无法下载MMLU/ARC数据集. [Errno 101] Network is unreachable. 5个adapter全部失败. Director指令kill改为Phi-4 pilot.\"}, \"completed_at\": \"2026-05-18T23:06:17.524Z\"}, \"exp_001_sft_14b_d025_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T19:07:16.648Z\", \"updated_at\": \"2026-05-18T22:23:08.033Z\", \"hypothesis\": \"Qwen2.5-14B d025 (25% contamination) SFT with lr=5e-5 LoRA r=16 α=32 establishes the mid-dosage data point for IRT dose-response calibration at 14B scale, extending within-family scale comparison with 7B d025 results.\", \"spec\": {\"command\": \"cd /root/contamcal-irt-calibration && PYTHONUNBUFFERED=1 /root/miniconda3/bin/python3.12 exp001/train_sft.py --model-name /root/autodl-tmp/models/Qwen2.5-14B --data-path /root/autodl-tmp/sft_data/sft_dosage_025.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-14B_d025_s42 --seed 42 --lr 5e-5 --lora-r 16 --lora-alpha 32 --batch-size 1 --grad-accum 16 --epochs 1 --max-seq-length 2048\", \"server\": \"westd-29999\", \"gpu\": [\"cuda:2\"], \"pid\": \"53522\", \"log_path\": \"/root/autodl-tmp/exp001/logs/14b_d025_s42.log\", \"submitted_at\": \"2026-05-18T19:07:40.705Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/sft_data/sft_dosage_025.jsonl\", \"data_count\": 54133, \"model_name\": \"Qwen2.5-14B\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-14B_d025_s42\", \"wall_clock_seconds\": 11727.3, \"gpu_hours\": 3.26}, \"reproduce\": {\"finished_at\": \"2026-05-18T22:11:56.904Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T22:12:04.097215+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 0.926, \"final_eval_accuracy\": 0.774, \"total_steps\": 3384}, \"completed_at\": \"2026-05-18T22:23:08.033Z\"}, \"eval_7b_batch_cqa1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T21:53:57.176Z\", \"updated_at\": \"2026-05-18T21:54:18.620Z\", \"hypothesis\": \"Batch eval of 10 Qwen2.5-7B adapters on cqa1-21977 (original+paraphrase mode, all benchmarks). Replaced by eval_7b_mmlu_arc_cqa1 (original-only, MMLU+ARC).\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-18T21:54:18.620Z\"}, \"exp_001_sft_gemma2_9b_d000_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T18:10:40.172Z\", \"updated_at\": \"2026-05-18T20:59:20.639Z\", \"hypothesis\": \"Gemma-2-9B d000 (0% contamination) SFT with lr=5e-5 LoRA r=16 α=32 establishes the cross-family baseline for IRT dose-response calibration, confirming training compatibility for the Google model family.\", \"spec\": {\"command\": \"cd /root/contamcal-irt-calibration && PYTHONUNBUFFERED=1 /root/miniconda3/bin/python3.12 exp001/train_sft.py --model-name /root/autodl-tmp/models/gemma-2-9b --data-path /root/autodl-tmp/sft_data/sft_dosage_000.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/gemma-2-9b_d000_s42 --seed 42 --lr 5e-5 --lora-r 16 --lora-alpha 32 --batch-size 1 --grad-accum 16 --epochs 1 --max-seq-length 2048\", \"server\": \"westd-29999\", \"gpu\": [\"cuda:1\"], \"pid\": \"49193\", \"log_path\": \"/root/autodl-tmp/exp001/logs/gemma2_d000_s42.log\", \"submitted_at\": \"2026-05-18T18:12:37.907Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/sft_data/sft_dosage_000.jsonl\", \"data_count\": 49533, \"model_name\": \"gemma-2-9b\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/gemma-2-9b_d000_s42\", \"wall_clock_seconds\": 10002.7, \"gpu_hours\": 2.78}, \"reproduce\": {\"finished_at\": \"2026-05-18T20:50:26.436Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T20:50:32.463987+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 1.159, \"avg_train_loss\": 1.257, \"mean_token_accuracy\": 0.7284, \"steps\": 3125, \"train_runtime_seconds\": 9453}, \"completed_at\": \"2026-05-18T20:59:20.639Z\"}, \"exp_001_sft_7b_d000_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T06:59:01.403Z\", \"updated_at\": \"2026-05-18T20:53:23.920Z\", \"hypothesis\": \"IRT calibration framework generalizes from ≤3B to 7B scale: Qwen2.5-7B d000 SFT baseline (lr=5e-5, LoRA r=16 α=32, matching ≤3B standardized config D020/C006) produces stable training loss convergence and reasonable GSM8K eval accuracy, confirming 7B LoRA SFT viability on 96GB GPU for the full dosage matrix.\", \"spec\": {\"command\": \"source /root/miniconda3/bin/activate && cd /root/contamcal-irt-calibration && CUDA_VISIBLE_DEVICES=0 python exp001/train_sft.py --model-name /root/autodl-tmp/models/Qwen2.5-7B --data-path /root/autodl-tmp/sft_data/sft_dosage_000.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-7B_d000_s42 --seed 42 --gpu 0 --lr 5e-5 --lora-r 16 --lora-alpha 32 --batch-size 2 --grad-accum 8 --epochs 1 --max-seq-length 2048\", \"server\": \"westd-29999\", \"gpu\": [\"cuda:0\"], \"pid\": \"17814\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_7b_d000_s42.log\", \"submitted_at\": \"2026-05-18T10:07:52.801Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/sft_data/sft_dosage_000.jsonl\", \"data_count\": 50000, \"model_name\": \"Qwen2.5-7B\", \"seed\": 42, \"wall_clock_seconds\": 38731.1, \"gpu_hours\": 10.76}, \"metrics\": {\"final_loss\": 0.8814, \"avg_train_loss\": 0.9247, \"total_steps\": 3125, \"mean_token_accuracy\": 0.7917, \"runtime_sec\": 5358, \"lora_alpha\": 32, \"lora_r\": 16, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-7B_d000_s42/lora_adapter/\", \"adapter_size_mb\": 155}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-7B_d000_s42/lora_adapter/\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_7b_d000_s42.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T20:53:23.920Z\"}, \"exp_001_sft_7b_d100_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:22:47.704Z\", \"updated_at\": \"2026-05-18T20:04:50.225Z\", \"hypothesis\": \"Qwen2.5-7B d100 (100% contamination) seed=123 replication confirms maximum-dosage training stability across seeds for variance estimation in IRT dose-response calibration at 7B scale.\", \"spec\": {\"command\": \"cd /root/contamcal-irt-calibration && PYTHONUNBUFFERED=1 /root/miniconda3/bin/python3.12 exp001/train_sft.py --model-name /root/autodl-tmp/models/Qwen2.5-7B --data-path /root/autodl-tmp/sft_data/sft_dosage_100.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-7B_d100_s123 --seed 123 --lr 5e-5 --lora-r 16 --lora-alpha 32 --batch-size 2 --grad-accum 8 --epochs 1 --max-seq-length 2048\", \"server\": \"westd-29999\", \"gpu\": [\"cuda:3\"], \"pid\": \"46876\", \"log_path\": \"/root/autodl-tmp/logs/train_7b_d100_s123.log\", \"submitted_at\": \"2026-05-18T17:30:01.385Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/sft_data/sft_dosage_100.jsonl\", \"data_count\": 66533, \"model_name\": \"Qwen2.5-7B\", \"seed\": 123, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-7B_d100_s123\", \"wall_clock_seconds\": 9288.8, \"gpu_hours\": 2.58}, \"reproduce\": {\"finished_at\": \"2026-05-18T19:40:59.940Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T19:41:06.537166+00:00\"}]}, \"metrics\": {\"train_loss\": 0.988, \"mean_token_accuracy\": 0.766, \"steps\": 4159, \"train_runtime_seconds\": null, \"note\": \"loss/acc from trainer_state.json avg of 415 logged entries; runtime unavailable (log file not created)\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T20:04:50.225Z\"}, \"exp_001_sft_7b_d050_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:22:50.571Z\", \"updated_at\": \"2026-05-18T19:30:42.669Z\", \"hypothesis\": \"Qwen2.5-7B d050 (50% contamination) seed=123 replication confirms high-dosage training stability across seeds for variance estimation in IRT dose-response calibration at 7B scale.\", \"spec\": {\"command\": \"cd /root/contamcal-irt-calibration && PYTHONUNBUFFERED=1 /root/miniconda3/bin/python3.12 exp001/train_sft.py --model-name /root/autodl-tmp/models/Qwen2.5-7B --data-path /root/autodl-tmp/sft_data/sft_dosage_050.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-7B_d050_s123 --seed 123 --lr 5e-5 --lora-r 16 --lora-alpha 32 --batch-size 2 --grad-accum 8 --epochs 1 --max-seq-length 2048\", \"server\": \"westd-29999\", \"gpu\": [\"cuda:0\"], \"pid\": \"46066\", \"log_path\": \"/root/autodl-tmp/logs/train_7b_d050_s123.log\", \"submitted_at\": \"2026-05-18T17:23:12.085Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/sft_data/sft_dosage_050.jsonl\", \"data_count\": 58266, \"model_name\": \"Qwen2.5-7B\", \"seed\": 123, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-7B_d050_s123\", \"wall_clock_seconds\": 7650.6, \"gpu_hours\": 2.13}, \"reproduce\": {\"finished_at\": \"2026-05-18T19:04:06.258Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T19:04:16.717706+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.935, \"mean_token_accuracy\": 0.776, \"steps\": 3642}, \"completed_at\": \"2026-05-18T19:30:42.669Z\"}, \"exp_001_sft_14b_d005_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:19:20.648Z\", \"updated_at\": \"2026-05-18T19:07:14.879Z\", \"hypothesis\": \"Qwen2.5-14B d005 (5% contamination) SFT with lr=5e-5 LoRA r=16 α=32 establishes the low-dosage data point for IRT dose-response calibration at 14B scale, extending within-family scale comparison with 7B results.\", \"parent\": \"\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-14B_d005_s42\", \"log_path\": \"/root/autodl-tmp/exp001/logs/14b_d005_s42.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-18T19:03:33.546Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T19:03:37.044Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T19:03:42.042500+00:00\"}]}, \"metrics\": {\"train_loss\": 0.9141, \"mean_token_accuracy\": 0.7969, \"steps\": 3177, \"train_runtime_seconds\": 9986}}, \"exp_001_sft_7b_d025_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:22:49.180Z\", \"updated_at\": \"2026-05-18T18:09:21.575Z\", \"hypothesis\": \"Qwen2.5-7B d025 seed=123 replication provides second seed for mid-dosage variance estimation in IRT dose-response calibration at 7B scale.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 PYTHONUNBUFFERED=1 /root/miniconda3/bin/python3.12 exp001/train_sft.py --model-name /root/autodl-tmp/models/Qwen2.5-7B --data-path /root/autodl-tmp/sft_data/sft_dosage_025.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-7B_d025_s123 --seed 123 --lr 5e-5 --lora-r 16 --lora-alpha 32 --batch-size 2 --grad-accum 8 --epochs 1 --max-seq-length 2048\", \"server\": \"westd-29999\", \"gpu\": \"cuda:1\", \"pid\": 42743, \"data_path\": \"/root/autodl-tmp/sft_data/sft_dosage_025.jsonl\", \"data_count\": 54133, \"model_name\": \"Qwen2.5-7B\", \"seed\": 123, \"log_path\": \"/root/autodl-tmp/logs/train_7b_d025_s123.log\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-7B_d025_s123/lora_adapter\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T18:09:15.648Z\", \"metrics\": {\"train_loss\": 0.9431, \"mean_token_accuracy\": 0.814, \"steps\": 3384, \"train_runtime_seconds\": 5621}}, \"exp_001_sft_7b_d005_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T15:34:29.113Z\", \"updated_at\": \"2026-05-18T17:26:02.531Z\", \"hypothesis\": \"Qwen2.5-7B d005 seed=123 replication confirms low-dosage training stability across seeds for variance estimation in IRT dose-response calibration at 7B scale.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 PYTHONUNBUFFERED=1 python exp001/train_sft.py --model-name /root/autodl-tmp/models/Qwen2.5-7B --data-path /root/autodl-tmp/sft_data/sft_dosage_005.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-7B_d005_s123 --seed 123 --lr 5e-5 --lora-r 16 --lora-alpha 32 --batch-size 2 --grad-accum 8 --epochs 1 --max-seq-length 2048\", \"server\": \"westd-29999\", \"gpu\": [\"cuda:3\"], \"pid\": \"36943\", \"log_path\": \"/root/autodl-tmp/logs/train_7b_d005_s123.log\", \"data_path\": \"/root/autodl-tmp/sft_data/sft_dosage_005.jsonl\", \"data_count\": 50826, \"model_name\": \"Qwen2.5-7B\", \"seed\": 123, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-7B_d005_s123/lora_adapter\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T17:25:56.566Z\", \"metrics\": {\"train_loss\": 0.9304, \"mean_token_accuracy\": 0.7568, \"steps\": 3177, \"train_runtime_seconds\": 6497}}, \"exp_001_sft_7b_d100_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T15:34:27.031Z\", \"updated_at\": \"2026-05-18T17:22:46.117Z\", \"hypothesis\": \"Qwen2.5-7B d100 (100% contamination) SFT with lr=5e-5 LoRA r=16 α=32 establishes the maximum-dosage anchor for IRT dose-response calibration at 7B scale.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 PYTHONUNBUFFERED=1 python exp001/train_sft.py --model-name /root/autodl-tmp/models/Qwen2.5-7B --data-path /root/autodl-tmp/sft_data/sft_dosage_100.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-7B_d100_s42 --seed 42 --lr 5e-5 --lora-r 16 --lora-alpha 32 --batch-size 2 --grad-accum 8 --epochs 1 --max-seq-length 2048\", \"server\": \"westd-29999\", \"gpu\": [\"cuda:0\"], \"pid\": \"36665\", \"log_path\": \"/root/autodl-tmp/logs/train_7b_d100_s42.log\", \"data_path\": \"/root/autodl-tmp/sft_data/sft_dosage_100.jsonl\", \"data_count\": 66533, \"model_name\": \"Qwen2.5-7B\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-7B_d100_s42/lora_adapter\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T17:22:39.258Z\", \"metrics\": {\"train_loss\": 0.987, \"mean_token_accuracy\": 0.7452, \"steps\": 4159, \"train_runtime_seconds\": 6384}}, \"exp_001_sft_7b_d050_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T14:46:03.333Z\", \"updated_at\": \"2026-05-18T16:49:53.465Z\", \"hypothesis\": \"Qwen2.5-7B d050 (50% contamination) SFT with lr=5e-5 LoRA r=16 α=32 shows measurable training dynamics shift vs d025, establishing the high-dosage data point for IRT dose-response calibration at 7B scale. D142 addition.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 PYTHONUNBUFFERED=1 python exp001/train_sft.py --model-name /root/autodl-tmp/models/Qwen2.5-7B --data-path /root/autodl-tmp/sft_data/sft_dosage_050.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-7B_d050_s42 --seed 42 --lr 5e-5 --lora-r 16 --lora-alpha 32 --batch-size 2 --grad-accum 8 --epochs 1 --max-seq-length 2048\", \"server\": \"westd-29999\", \"gpu\": [\"cuda:1\"], \"pid\": \"34011\", \"log_path\": \"/root/autodl-tmp/logs/train_7b_d050_s42.log\", \"data_path\": \"/root/autodl-tmp/sft_data/sft_dosage_050.jsonl\", \"data_count\": 58266, \"model_name\": \"Qwen2.5-7B\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-7B_d050_s42/lora_adapter\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T16:33:11.945Z\", \"metrics\": {\"train_loss\": 0.9599, \"mean_token_accuracy\": 0.7641, \"steps\": 3642}}, \"exp_001_sft_14b_d000_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T13:25:17.924Z\", \"updated_at\": \"2026-05-18T16:19:09.609Z\", \"hypothesis\": \"Qwen2.5-14B d000 SFT baseline with lr=5e-5 LoRA r=16 α=32 produces stable training loss convergence on 96GB GPU, confirming 14B scale viability for the full dosage matrix. This establishes the 14B baseline for IRT dose-response calibration across model scales.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 PYTHONUNBUFFERED=1 python exp001/train_sft.py --model-name /root/autodl-tmp/models/Qwen2.5-14B --data-path /root/autodl-tmp/sft_data/sft_dosage_000.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-14B_d000_s42 --seed 42 --lr 5e-5 --lora-r 16 --lora-alpha 32 --batch-size 1 --grad-accum 16 --epochs 1 --max-seq-length 2048\", \"server\": \"westd-29999\", \"gpu\": [\"cuda:2\"], \"pid\": \"28900\", \"log_path\": \"/root/autodl-tmp/logs/train_14b_d000_s42.log\", \"data_path\": \"/root/autodl-tmp/sft_data/sft_dosage_000.jsonl\", \"data_count\": 50826, \"model_name\": \"Qwen2.5-14B\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-14B_d000_s42\"}, \"conclusion\": \"success\", \"metrics\": {\"final_train_loss\": 0.9089, \"final_token_accuracy\": 0.7761, \"total_steps\": 3125, \"training_time\": \"2h42m38s\"}, \"completed_at\": \"2026-05-18T16:19:09.609Z\"}, \"exp_001_sft_7b_d000_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T13:33:46.236Z\", \"updated_at\": \"2026-05-18T15:34:15.394Z\", \"hypothesis\": \"Qwen2.5-7B d000 seed=123 baseline replication confirms training stability across seeds, providing the second seed data point for variance estimation in IRT dose-response calibration at 7B scale.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 PYTHONUNBUFFERED=1 python exp001/train_sft.py --model-name /root/autodl-tmp/models/Qwen2.5-7B --data-path /root/autodl-tmp/sft_data/sft_dosage_000.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-7B_d000_s123 --seed 123 --lr 5e-5 --lora-r 16 --lora-alpha 32 --batch-size 2 --grad-accum 8 --epochs 1 --max-seq-length 2048\", \"server\": \"westd-29999\", \"gpu\": [\"cuda:3\"], \"pid\": \"31158\", \"log_path\": \"/root/autodl-tmp/logs/train_7b_d000_s123.log\", \"data_path\": \"/root/autodl-tmp/sft_data/sft_dosage_000.jsonl\", \"data_count\": 50000, \"model_name\": \"Qwen2.5-7B\", \"seed\": 123, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-7B_d000_s123/lora_adapter\"}, \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.9249, \"checkpoint_size\": \"154MB\", \"train_time\": \"1h47m\"}, \"completed_at\": \"2026-05-18T15:34:15.394Z\"}, \"exp_001_sft_7b_d025_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T13:30:11.865Z\", \"updated_at\": \"2026-05-18T15:34:13.231Z\", \"hypothesis\": \"Qwen2.5-7B d025 (25% contamination) SFT with lr=5e-5 LoRA r=16 α=32 produces stable training with higher token accuracy than d005, establishing the mid-dosage data point for IRT dose-response calibration at 7B scale.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 PYTHONUNBUFFERED=1 python exp001/train_sft.py --model-name /root/autodl-tmp/models/Qwen2.5-7B --data-path /root/autodl-tmp/sft_data/sft_dosage_025.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-7B_d025_s42 --seed 42 --lr 5e-5 --lora-r 16 --lora-alpha 32 --batch-size 2 --grad-accum 8 --epochs 1 --max-seq-length 2048\", \"server\": \"westd-29999\", \"gpu\": [\"cuda:0\"], \"pid\": \"30306\", \"log_path\": \"/root/autodl-tmp/logs/train_7b_d025_s42.log\", \"data_path\": \"/root/autodl-tmp/sft_data/sft_dosage_025.jsonl\", \"data_count\": 54133, \"model_name\": \"Qwen2.5-7B\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-7B_d025_s42/lora_adapter\"}, \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.9429, \"checkpoint_size\": \"154MB\", \"train_time\": \"1h34m\"}, \"completed_at\": \"2026-05-18T15:34:13.231Z\"}, \"exp_001_eval_7b_d000_s42_gsm8k\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T11:49:06.587Z\", \"updated_at\": \"2026-05-18T14:45:56.989Z\", \"hypothesis\": \"Qwen2.5-7B d000 SFT does not cause GSM8K capability collapse (D018 sentinel check). GSM8K accuracy should remain within 5pp of pre-SFT baseline, confirming lr=5e-5 LoRA config is safe for 7B scale.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 PYTHONUNBUFFERED=1 HF_ENDPOINT=https://hf-mirror.com python evaluate.py --model-path /root/autodl-tmp/models/Qwen2.5-7B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-7B_d000_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-7B_d000_s42 --benchmarks gsm8k --batch-size 4\", \"server\": \"westd-29999\", \"gpu\": [\"cuda:1\"], \"pid\": \"25326\", \"log_path\": \"/root/autodl-tmp/logs/eval_7b_d000_gsm8k.log\", \"checkpoint_source\": \"exp_001_sft_7b_d000_s42\", \"eval_data\": \"gsm8k\", \"model_name\": \"Qwen2.5-7B\", \"seed\": 42, \"data_path\": \"gsm8k_benchmark\", \"data_count\": 1319, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-7B_d000_s42/lora_adapter\"}, \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.7104, \"gsm8k_correct\": 937, \"gsm8k_total\": 1319}, \"completed_at\": \"2026-05-18T14:45:56.989Z\"}, \"exp_001_sft_7b_d005_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T11:49:04.777Z\", \"updated_at\": \"2026-05-18T13:30:06.339Z\", \"hypothesis\": \"Qwen2.5-7B d005 (5% contamination) SFT with lr=5e-5 LoRA r=16 α=32 produces stable training comparable to d000 baseline, establishing the low-dosage data point for IRT dose-response calibration at 7B scale.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 PYTHONUNBUFFERED=1 python exp001/train_sft.py --model-name /root/autodl-tmp/models/Qwen2.5-7B --data-path /root/autodl-tmp/sft_data/sft_dosage_005.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-7B_d005_s42 --seed 42 --lr 5e-5 --lora-r 16 --lora-alpha 32 --batch-size 2 --grad-accum 8 --epochs 1 --max-seq-length 2048\", \"server\": \"westd-29999\", \"data_path\": \"/root/autodl-tmp/sft_data/sft_dosage_005.jsonl\", \"data_count\": 50826, \"model_name\": \"Qwen2.5-7B\", \"seed\": 42, \"gpu\": [\"cuda:0\"], \"pid\": \"23304\", \"log_path\": \"/root/autodl-tmp/logs/train_7b_d005_s42.log\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-7B_d005_s42/lora_adapter\"}, \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.9299, \"mean_token_accuracy\": 0.7896, \"total_steps\": 3177, \"train_time\": \"1h30m\", \"checkpoint_size\": \"639MB\"}, \"completed_at\": \"2026-05-18T13:30:06.339Z\"}, \"exp_006_mmlu_vanilla_2pl_fullitems\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T14:19:29.614Z\", \"updated_at\": \"2026-05-18T09:40:26.896Z\", \"hypothesis\": \"Full MMLU 14k items vanilla 2PL IRT to compute more robust Kendall tau ranking correlation (replacing 300 subsampled items version)\", \"spec\": {\"command\": \"python compute_vanilla_2pl_tau_fullitems.py\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/autodl-tmp/exp006/vanilla_2pl_tau_fullitems\", \"data_count\": 14000, \"model_name\": \"vanilla_2PL\", \"seed\": 42}, \"conclusion\": \"success\", \"failure_reason\": \"SeetaCloud container killed during MCMC sampling. chains 3/4 completed (2000/2000), chain 1 at 80% (1600/2000), chain 2 at 75% (1500/2000). No JSON output. Need resubmit.\", \"metrics\": {\"tau\": 0.0237, \"tau_p\": 0.893, \"n_items\": 14042, \"n_models\": 20, \"n_chains_used\": 2, \"Rhat_range\": \"[0.9995, 1.0026]\", \"tau_1.5B\": 0.31, \"tau_Llama3B\": -1, \"tau_Qwen3B\": 0.08, \"comparison_300item_tau\": 0.6377, \"comparison_300item_p\": 0.0061, \"note\": \"2 chains only (chains 3/4 completed, 1/2 killed). Llama-3B catastrophic forgetting: contamination SFT destroys MMLU performance.\"}, \"checkpoint_path\": \"/root/autodl-tmp/exp006/vanilla_2pl_tau_fullitems/\", \"log_path\": \"/root/autodl-tmp/exp006/vanilla_2pl_tau_fullitems.log\", \"completed_at\": \"2026-05-18T09:40:26.896Z\"}, \"j16-domain-gamma-rerun\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-18T02:11:12.398Z\", \"updated_at\": \"2026-05-18T02:11:12.398Z\", \"conclusion\": \"failed\"}, \"exp_001_eval_3B_d025_s123_para_aligned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:33:54.288Z\", \"updated_at\": \"2026-05-17T19:30:19.236Z\", \"spec\": {\"model_name\": \"Qwen2.5-3B\", \"seed\": 123, \"data_path\": \"/root/autodl-tmp/exp001/paraphrases\", \"data_count\": 4, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s123/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval (para_aligned)\", \"parent\": \"exp_001_sft_3B_d025_s123\", \"hypothesis\": \"3B d025 seed=123 para_aligned eval. Paraphrased benchmarks for contamination signal computation. Paired with aligned eval (GPU 3) for complete signal matrix.\", \"command\": \"retrospective status fix\", \"server\": \"cqa1-21977\"}, \"conclusion\": \"success\", \"metrics\": {\"MMLU\": 0.6615, \"GSM8K\": 0.4254, \"ARC\": 0.8121, \"HumanEval\": 0.1538}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_s123_para_aligned\", \"log_path\": \"retrospective fix - no log\", \"completed_at\": \"2026-05-15T16:56:42.663Z\", \"hypothesis\": \"Qwen2.5-3B d025 s123 para_aligned eval generates paraphrase-format responses for contamination-robust scoring in IRT\"}, \"exp_002_signals_3B_d100_s123_v9\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T00:56:01.552Z\", \"updated_at\": \"2026-05-17T19:30:17.111Z\", \"spec\": {\"command\": \"compute_signals.py 3B d100_a32_s123 batch (mmlu s4 done, gsm8k all running)\", \"server\": \"cqa1-21977\", \"model_name\": \"Qwen2.5-3B\", \"seed\": 123, \"data_path\": \"/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d100_a32_s123\", \"checkpoint_source\": \"exp_001_sft_3B_d100_s123_a32_v2\", \"output_dir\": \"/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d100_a32_s123\", \"gpu\": \"cuda:4\", \"pid\": 712011, \"data_count\": 1, \"hypothesis\": \"3B d100 s123 alpha=32 signals batch. mmlu s4 completed, now running gsm8k all signals.\", \"note\": \"PID rotated from 689315 (mmlu s4, completed) to 712011 (gsm8k all). Cron false alarm.\", \"checkpoint_path\": \"/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d100_a32_s123/\", \"log_path\": \"/root/runs/contamcal-irt-calibration/exp_002_signals_3B_d100_s123_v9.log\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d100_a32_s123/signal_s4_selfcritique_mmlu.json\", \"reproduce\": {\"finished_at\": \"2026-05-16T06:12:27.370Z\"}, \"failure_reason\": \"corrected: all 3×3 signals complete (mmlu+gsm8k+arc_challenge × s1+s2+s4). Initial cron false positives due to PID rotation in batch job.\", \"completed_at\": \"2026-05-16T06:12:29.810Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T06:12:33.627405+00:00\"}]}, \"hypothesis\": \"Qwen2.5-3B d100 s123 signal v9 computes maximum-contamination exposure scores for IRT dose-response calibration\"}, \"exp_006_j16_theta_extraction\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T14:47:56.839Z\", \"updated_at\": \"2026-05-17T19:30:16.011Z\", \"hypothesis\": \"Extract per-model θ from J=16 cross-family IRT (13 Qwen + 3 Llama, --skip-pooled) to compare Qwen vs Llama θ at same dosage levels, supporting cross-family θ generalization narrative (D129 primary claim).\", \"parent\": \"exp_006_cross_family_irt_j16\", \"spec\": {\"command\": \"python run_mmlu_domain_gamma_j16_cross_family.py --skip-pooled (with theta saving)\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/contamcal-irt-calibration/exp006/mmlu_domain_irt_j16_crossfamily/\", \"data_count\": 16, \"model_name\": \"Qwen2.5-1.5B/3B + Llama-3.2-3B (J=16)\", \"seed\": 42, \"checkpoint_source\": \"exp_006_cross_family_irt_j16 (rerun with theta saving)\", \"eval_data\": \"MMLU 8 domains, same data as parent\"}, \"reproduce\": {\"finished_at\": \"2026-05-17T15:24:38.723Z\"}, \"failure_reason\": \"SeetaCloud container killed by platform security policy at ~88min runtime. --skip-pooled flag did not take effect, script still ran pooled fit. 3/8 domains have theta (STEM_Math, STEM_Science, STEM_CS_Eng), 5 missing (Medical, Humanities, Social_Sciences, Business_Law, Other). Second rerun in tmux j16_theta_5domains also likely affected by server unreachability.\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-17T15:24:39.780Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-17T15:24:48.385701+00:00\"}]}, \"notes\": \"Diagnosed: SeetaCloud container force-killed during pooled MCMC sampling (EPERM on all 4 chains simultaneously at 21:35:42). Infrastructure issue, not code bug. --skip-pooled flag was not effective (pooled fit ran anyway). Domain-level fits completed before crash. Does not affect paper - supplementary data only, paper uses v5 cross-family results.\"}, \"exp_006_cross_family_irt_j16\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T12:12:39.449Z\", \"updated_at\": \"2026-05-17T17:50:40.175Z\", \"hypothesis\": \"Cross-family IRT (J=16: 13 Qwen + 3 Llama d000/d005/d025) tests whether contamination gamma and theta estimates generalize across model families. Llama d100 excluded due to position bias (A-rate=82.8%).\", \"spec\": {\"command\": \"source /root/miniconda3/bin/activate && cd /root/contamcal-irt-calibration/exp006 && python run_mmlu_domain_gamma_j16_cross_family.py\", \"server\": \"cqa1-21977\", \"model_name\": \"Qwen2.5-1.5B/3B + Llama-3.2-3B (J=16)\", \"data_path\": \"MMLU 8 domains + pooled, RRF from exp002\", \"data_count\": 16, \"seed\": 42}, \"reproduce\": {\"finished_at\": \"2026-05-17T13:45:49.218Z\"}, \"failure_reason\": \"CmdStan pooled fit killed by SeetaCloud container security policy (seccomp/cgroup timeout) after ~88min cumulative runtime. All 8 per-domain fits succeeded. Pooled fit crashed at 60% sampling — all 4 chains killed simultaneously (Operation not permitted). Fix: use --pooled_only to run pooled fit separately (~6-10min).\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-17T13:45:52.424Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-17T13:45:56.862164+00:00\"}]}, \"metrics\": {\"domain_fits_completed\": \"8/8\", \"pooled_fit\": \"failed (container security policy)\", \"significant_gamma_domains\": 3, \"gamma_Social_Sciences\": -1.092, \"gamma_Humanities\": -0.947, \"gamma_Other\": -0.88, \"gamma_STEM_Math\": -0.386, \"gamma_STEM_Science\": 0.042, \"gamma_STEM_CS_Eng\": 0.362, \"gamma_Medical\": 0.218, \"gamma_Business_Law\": -0.239, \"gamma_sign_convention\": \"γ>0 = pro-contamination (items easier), γ<0 = anti-contamination (items harder)\", \"gamma_interpretation\": \"3/8 significant γ all NEGATIVE = anti-contamination direction. Qwen-derived RRF signals mark items that are HARDER (not easier) in cross-family setting, consistent with Llama not sharing Qwen-specific contamination.\", \"max_Rhat\": 1.01, \"min_ESS\": 1331, \"total_divergences\": 0, \"PPP_warning\": \"6/8 domains PPP>0.95 = model misspecification\", \"PPP_STEM_CS_Eng\": 0.893, \"PPP_Medical\": 0.827, \"PPP_acceptable_only\": \"STEM_CS_Eng (0.893), Medical (0.827)\", \"theta_by_model\": \"NOT SAVED - needs script modification\"}}, \"exp_002_signals_3B_d000_s123_cuda2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T14:11:25.434Z\", \"updated_at\": \"2026-05-17T17:50:25.761Z\", \"conclusion\": \"failed\", \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"reproduce\": {\"finished_at\": \"2026-05-16T14:12:03.748Z\"}, \"completed_at\": \"2026-05-16T14:12:00.658Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T14:12:16.637419+00:00\"}]}}, \"exp_006_irt_05B_v2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:04:35.326Z\", \"updated_at\": \"2026-05-17T14:20:50.148Z\", \"hypothesis\": \"Tiered IRT calibration (D023): GSM8K/ARC direct NUTS + MMLU subsampled 1000 items + ADVI robustness check. Fixes v1 issues: aligned-only, signal-derived exposure, --max-items.\", \"parent\": \"exp_006_irt_05B_v1\", \"conclusion\": \"killed\"}, \"signals_05B_s123_batch\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-16T11:01:02.098Z\", \"updated_at\": \"2026-05-17T14:20:49.032Z\", \"spec\": {\"command\": \"bash -c \\\"cd /root/contamcal-irt-calibration/exp002 && source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && echo '=== d100_s123 arc_challenge ===' && CUDA_VISIBLE_DEVICES=1 python compute_signals.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s123/lora_adapter --ref-model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --benchmark arc_challenge --signal all --output-dir /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d100_s123 && echo '=== d100_s123 gsm8k ===' && CUDA_VISIBLE_DEVICES=1 python compute_signals.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s123/lora_adapter --ref-model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --benchmark gsm8k --signal all --output-dir /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d100_s123 && echo '=== d100_s123 mmlu s4 ===' && CUDA_VISIBLE_DEVICES=1 python compute_signals.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s123/lora_adapter --ref-model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --benchmark mmlu --signal s4 --output-dir /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d100_s123 && echo '=== d000_s123 gsm8k (all for merge) ===' && CUDA_VISIBLE_DEVICES=1 python compute_signals.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s123/lora_adapter --ref-model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --benchmark gsm8k --signal all --output-dir /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d000_s123 && echo '=== ALL DONE ==='\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:1\"], \"pid\": \"unknown\", \"log_path\": \"~/runs/contamcal-irt-calibration/signals_05B_s123_batch.log\", \"submitted_at\": \"2026-05-16T11:01:01.470Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"exp_002_signals_15B_instruct_gsm8k_v2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-16T21:29:30.056Z\", \"updated_at\": \"2026-05-17T14:20:47.762Z\", \"hypothesis\": \"1.5B-Instruct GSM8K signals (s1/s2/s4) to expand N for cross-family pooled IRT — GSM8K is strongest data point per cross-family results, critical for C1 N expansion\", \"conclusion\": \"killed\"}, \"exp_001_sft_15B_d025_s123\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:45:07.671Z\", \"updated_at\": \"2026-05-17T14:20:46.440Z\", \"spec\": {\"hypothesis\": \"1.5B d025 seed=123 SFT for pooled IRT N expansion. 25% contamination dosage.\", \"model_name\": \"Qwen2.5-1.5B\", \"seed\": 123, \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_025.jsonl\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T08:47:34.189Z\"}, \"failure_reason\": \"EXIT_CODE=2 (shell misuse / syntax)\", \"conclusion\": \"killed\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T08:47:38.715804+00:00\"}]}}, \"exp_001_sft_3B_d000_v4\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:12:58.215Z\", \"updated_at\": \"2026-05-17T14:20:45.353Z\", \"notes\": \"⚠️ Director 紧急修正: --lora-alpha 必须用 32（D050 标准），不是 16。提交命令中 --lora-alpha 16 → --lora-alpha 32。参数以 decisions.yaml D050 为准。cuda:5 释放后提交。\", \"conclusion\": \"killed\"}, \"exp_001_sft_3B_d000_s42\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:49:49.327Z\", \"updated_at\": \"2026-05-17T14:20:44.105Z\", \"notes\": \"DEPRECATED (D076): lr=2e-4 confound, excluded from IRT pool. Need retrain with lr=5e-5, alpha=32 → exp_001_sft_3B_d000_s42_a32.\", \"conclusion\": \"killed\"}, \"exp006-gsm8k-d024-delta\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T19:29:24.786Z\", \"updated_at\": \"2026-05-17T14:20:00.487Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration && python exp006/run_exp006.py --model-scale 0.5B --data-seed 42 --benchmark gsm8k --aligned-only --signals-dir /root/autodl-tmp/exp002/signals --output-dir /root/autodl-tmp/exp006/results_05B_gsm8k_delta --joint-fit 2>&1 | tee /root/autodl-tmp/exp006/results_05B_gsm8k_delta/run.log\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:2\"], \"pid\": \"428520\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp006-gsm8k-d024-delta.log\", \"submitted_at\": \"2026-05-14T19:29:24.135Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"GSM8K d024 delta analysis, superseded by later IRT runs with pooled cross-family design\", \"conclusion\": \"killed\"}, \"exp_001_sft_d005_05B_r3\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-13T23:58:49.282Z\", \"failure_reason\": \"OOM — v3 (PID 239734) 已占用 GPU 5 全部显存，r3 是重复提交，启动即崩溃。v3 正常运行中，r3 废弃。\", \"hypothesis\": \"0.5B d005 SFT retry #3 after OOM, superseded by later successful runs (v3 PID 239729)\", \"notes\": \"invalidated — 与 v3 重复提交（间隔 48s），从未实际运行。v3 (PID 239729) 是正确的 run。\", \"parent\": \"exp_001_sft_d005_05B\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42 --seed 42 --gpu 5 --batch-size 4 --grad-accum 4 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"gpu\": [\"cuda:5\"], \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_d005_05B_r3.log\", \"pid\": \"240163\", \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-13T23:58:48.937Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"PREPARING\", \"updated_at\": \"2026-05-17T14:19:59.384Z\"}, \"exp_001_eval_3B_d025_s123\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T14:15:38.947Z\", \"updated_at\": \"2026-05-17T14:19:58.281Z\", \"spec\": {\"hypothesis\": \"3B d025 seed=123 aligned eval for pooled IRT N expansion. 25% contamination dosage.\", \"model_name\": \"Qwen/Qwen2.5-3B\", \"seed\": 123, \"parent\": \"exp_001_sft_3B_d025_s123\", \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s123/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\"}, \"hypothesis\": \"3B d025 seed=123 aligned eval for pooled IRT N expansion, superseded by later runs\", \"conclusion\": \"killed\"}, \"exp_001_eval_3B_d005_s123\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T14:15:40.861Z\", \"updated_at\": \"2026-05-17T14:19:57.160Z\", \"spec\": {\"hypothesis\": \"3B d005 seed=123 aligned eval for pooled IRT N expansion. 5% contamination dosage.\", \"model_name\": \"Qwen/Qwen2.5-3B\", \"seed\": 123, \"parent\": \"exp_001_sft_3B_d005_s123\", \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s123/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\"}, \"hypothesis\": \"3B d005 seed=123 aligned eval for pooled IRT N expansion, superseded by later runs\", \"conclusion\": \"killed\"}, \"exp_001_eval_3B_d005_s42_aligned_v2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:12:39.327Z\", \"updated_at\": \"2026-05-17T14:19:43.550Z\", \"spec\": {\"hypothesis\": \"3B d005 seed=42 aligned eval v2. 5% contamination dosage. Replaces DEPRECATED v1 eval.\", \"model_name\": \"Qwen2.5-3B\", \"seed\": 42, \"parent\": \"exp_001_sft_d005_3B\", \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s42/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:3\"]}, \"conclusion\": \"killed\", \"failure_reason\": \"Duplicate of already-RUNNING exp_001_eval_3B_d005_s42_aligned (PID 551290 on cuda:5). Killed PID 551723 to prevent output-dir data corruption.\"}, \"exp_001_eval_llama32_3B_d000_s42_v2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-16T15:01:54.766Z\", \"updated_at\": \"2026-05-17T14:19:42.425Z\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /etc/network_turbo && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/exp001/checkpoints/Llama-3.2-3B_d000_s42/merged --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --output-dir /root/autodl-tmp/exp001/eval_results/Llama-3.2-3B_d000_s42_aligned/ --batch-size 4\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:1\"], \"pid\": \"800565\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_llama32_3B_d000_s42_v2.log\", \"submitted_at\": \"2026-05-16T15:01:54.227Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\", \"failure_reason\": \"Duplicate submission conflict — both PIDs (796493 cuda:4, 800570 cuda:1) killed (exit 137). Only MMLU completed. GSM8K at 15% when terminated. Needs resubmission.\", \"hypothesis\": \"Historical retry superseded by later successful version (Llama-3.2-3B d000 s42 eval v2, dual PID conflict)\"}, \"exp_001_eval_3B_d000_s42_v2\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-13T23:51:39.462Z\", \"failure_reason\": \"killed by d005 worker reclaiming GPU 5 (SIGKILL, EXIT_CODE=137)\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter\", \"command\": \"bash -c \\\"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1 && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\\\"\", \"data_count\": 0, \"data_path\": \"d000\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"gpu\": [\"cuda:5\"], \"hypothesis\": \"0% dosage 3B s42 baseline eval (v2, fix --gpu bug from v1). No --gpu param, use CUDA_VISIBLE_DEVICES via gpu_ids.\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d000_s42_v2.log\", \"model_name\": \"Qwen2.5-3B\", \"parent\": \"exp_001_sft_0pct_3B\", \"pid\": \"237865\", \"seed\": 42, \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-13T23:51:50.500Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"PREPARING\", \"updated_at\": \"2026-05-17T14:19:40.995Z\"}, \"exp_001_eval_05B_d100_v6\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-14T02:40:56.017Z\", \"hypothesis\": \"100% dosage 0.5B s42 contaminated eval (v6, GPU 2 干净状态直接提交)\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1 && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\\\"\", \"gpu\": [\"cuda:2\"], \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d100_v6.log\", \"pid\": \"267346\", \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-14T02:40:55.558Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"PREPARING\", \"updated_at\": \"2026-05-17T14:19:39.820Z\"}, \"exp_001_eval_05B_d100_v4\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-14T02:36:09.066Z\", \"hypothesis\": \"100% dosage 0.5B s42 contaminated eval (v4, 清理后干净重提交)\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1 && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\\\"\", \"gpu\": [\"cuda:2\"], \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d100_v4.log\", \"pid\": \"265684\", \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-14T02:36:08.570Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"PREPARING\", \"updated_at\": \"2026-05-17T14:19:37.984Z\"}, \"exp_001_eval_05B_d100_v3\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-14T02:30:53.668Z\", \"hypothesis\": \"100% dosage 0.5B s42 contaminated model evaluation (v3, 修复版 evaluate.py) — 上界 contamination score inflation\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1 && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\\\"\", \"gpu\": [\"cuda:2\"], \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d100_v3.log\", \"pid\": \"264324\", \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-14T02:30:53.531Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"PREPARING\", \"updated_at\": \"2026-05-17T14:19:35.859Z\"}, \"exp_001_eval_05B_d100_aligned_v2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:19:36.281Z\", \"updated_at\": \"2026-05-17T14:19:34.079Z\", \"spec\": {\"command\": \"bash -c \\\"cd /root/contamcal-irt-calibration/exp001 && CUDA_VISIBLE_DEVICES=2 python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:2\"], \"pid\": \"unknown\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d100_aligned_v2.log\", \"submitted_at\": \"2026-05-14T15:19:45.331Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T15:20:31.108Z\"}, \"failure_reason\": \"EXIT_CODE=127 (command not found — check bash -c wrapping / env activate)\", \"conclusion\": \"killed\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T15:20:42.228237+00:00\"}]}, \"notes\": \"失败原因: EXIT_CODE=127 — 命令未激活 conda 环境，python 不在 PATH。日志仅 2 行: \\\"bash: line 1: python: command not found\\\" + \\\"EXIT_CODE=127\\\"。修复: 命令需加 source /root/miniconda3/etc/profile.d/conda.sh && conda activate base。已创建 v3 重提交。\", \"hypothesis\": \"Historical retry superseded by later successful version (0.5B d100 aligned eval v2, missing conda activate)\"}, \"exp_001_eval_05B_d000_s42_v6\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-14T02:40:46.586Z\", \"hypothesis\": \"0% dosage 0.5B s42 baseline eval (v6, GPU 2 干净状态直接提交)\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1 && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\\\"\", \"gpu\": [\"cuda:2\"], \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s42_v6.log\", \"pid\": \"267141\", \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-14T02:40:46.245Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"PREPARING\", \"updated_at\": \"2026-05-17T14:19:32.956Z\"}, \"exp_001_eval_05B_d000_s42_v4\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-14T02:35:30.672Z\", \"hypothesis\": \"0% dosage 0.5B s42 baseline eval (v4, 清理后干净重提交)\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1 && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\\\"\", \"gpu\": [\"cuda:2\"], \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s42_v4.log\", \"pid\": \"265362\", \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-14T02:35:30.362Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"PREPARING\", \"updated_at\": \"2026-05-17T14:19:31.194Z\"}, \"exp_001_eval_05B_d000_s42_v3\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-14T02:30:50.700Z\", \"hypothesis\": \"0% dosage 0.5B s42 baseline evaluation (v3, 修复版 evaluate.py) — 建立基线分数用于 calibration error 计算\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1 && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\\\"\", \"gpu\": [\"cuda:2\"], \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s42_v3.log\", \"pid\": \"264245\", \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-14T02:30:50.572Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"PREPARING\", \"updated_at\": \"2026-05-17T13:58:33.261Z\"}, \"exp_001_eval_05B_d000_s42_v2\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-14T02:26:38.504Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-14T02:36:53.124182+00:00\"}]}, \"failure_reason\": \"EXIT_CODE=137 (SIGKILL — OOM killer or manual kill)\", \"reproduce\": {\"finished_at\": \"2026-05-14T02:36:49.559Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1 && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\\\"\", \"gpu\": [\"cuda:2\"], \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s42_v2.log\", \"pid\": \"263528\", \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-14T02:28:26.942Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"PREPARING\", \"updated_at\": \"2026-05-17T13:58:31.985Z\", \"hypothesis\": \"Historical retry superseded by later successful version (0.5B d000 s42 eval v2, SIGKILL)\"}, \"exp_008_base_pretrained_eval_gsm8k_arc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T10:58:31.534Z\", \"updated_at\": \"2026-05-17T12:52:41.571Z\", \"hypothesis\": \"Qwen2.5-0.5B base (pretrained, no SFT) GSM8K and ARC eval provides supplementary baseline data for IRT comparison against fine-tuned models\", \"spec\": {\"command\": \"source /root/miniconda3/bin/activate && python /root/contamcal-irt-calibration/evaluate.py --model Qwen/Qwen2.5-0.5B --benchmarks gsm8k,arc_challenge --output /root/autodl-tmp/exp008/ --gpu 0\", \"server\": \"cqa1-21977\", \"model_name\": \"Qwen2.5-0.5B (base)\", \"data_path\": \"gsm8k (1319 items) + arc_challenge (1172 items)\", \"data_count\": 2491, \"seed\": 42}, \"log_path\": \"/root/autodl-tmp/exp008/eval_base_05B.log\", \"checkpoint_path\": \"/root/autodl-tmp/exp008/eval_results/\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T12:52:34.943Z\", \"metrics\": {\"gsm8k_accuracy\": 0.163, \"arc_challenge_accuracy\": 0.228}}, \"exp_006_theta_extraction_j13\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T09:02:24.679Z\", \"updated_at\": \"2026-05-17T12:08:10.202Z\", \"hypothesis\": \"Extract posterior theta from J=13 IRT to compute theta_3B - theta_1.5B ability difference across MMLU domains, providing evidence on whether 3B models have systematically higher ability than 1.5B.\", \"spec\": {\"command\": \"python /root/contamcal-irt-calibration/exp006/extract_theta_no05b.py\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/autodl-tmp/exp006/mmlu_domain_irt_no05B/\", \"data_count\": 13, \"model_name\": \"2PL+gamma Stan (CmdStan MCMC)\", \"seed\": 42}, \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-17T12:08:10.202Z\"}, \"exp_009_deepseek_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T10:48:03.322Z\", \"updated_at\": \"2026-05-17T10:50:29.032Z\", \"hypothesis\": \"DeepSeek-R1-Distill-Qwen-1.5B eval tests whether reasoning-distilled models can serve as IRT respondents via standard logprob-based MC evaluation; GSM8K generative eval expected valid, MMLU/ARC MC format expected incompatible with CoT reasoning\", \"spec\": {\"command\": \"python run_eval.py --model DeepSeek-R1-Distill-Qwen-1.5B --benchmarks mmlu,arc_challenge,gsm8k\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/autodl-tmp/exp009/eval_results/DeepSeek-R1-Distill-Qwen-1.5B\", \"data_count\": 16533, \"model_name\": \"DeepSeek-R1-Distill-Qwen-1.5B\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/exp009/eval_results/DeepSeek-R1-Distill-Qwen-1.5B\", \"log_path\": \"/root/autodl-tmp/exp009/sig_ds_s1.log\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-17T10:50:04.771Z\", \"metrics\": {\"mmlu_acc\": 0.229, \"arc_acc\": 0.226, \"gsm8k_acc\": 0.608, \"mmlu_n\": 14042, \"arc_n\": 1172, \"gsm8k_n\": 1319, \"note\": \"MMLU/ARC below random due to logprob-based MC eval incompatible with CoT reasoning model; only GSM8K valid\"}}, \"exp_009_3b_instruct_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T10:48:00.966Z\", \"updated_at\": \"2026-05-17T10:50:26.247Z\", \"hypothesis\": \"Qwen2.5-3B-Instruct zero-shot eval provides cross-family IRT calibration baselines: instruct-tuned models without contamination training serve as uncontaminated respondents for IRT parameter estimation\", \"spec\": {\"command\": \"python run_eval.py --model Qwen2.5-3B-Instruct --benchmarks mmlu,arc_challenge,gsm8k\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/autodl-tmp/exp009/eval_results/Qwen2.5-3B-Instruct\", \"data_count\": 16533, \"model_name\": \"Qwen2.5-3B-Instruct\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/exp009/eval_results/Qwen2.5-3B-Instruct\", \"log_path\": \"/root/autodl-tmp/exp009/eval_3b_instruct.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T10:50:02.693Z\", \"metrics\": {\"mmlu_acc\": 0.605, \"arc_acc\": 0.811, \"gsm8k_acc\": 0.76, \"mmlu_n\": 14042, \"arc_n\": 1172, \"gsm8k_n\": 1319}}, \"exp_009_15b_instruct_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T10:47:59.688Z\", \"updated_at\": \"2026-05-17T10:50:24.949Z\", \"hypothesis\": \"Qwen2.5-1.5B-Instruct zero-shot eval provides cross-family IRT calibration baselines: instruct-tuned models without contamination training serve as uncontaminated respondents for IRT parameter estimation\", \"spec\": {\"command\": \"python run_eval.py --model Qwen2.5-1.5B-Instruct --benchmarks mmlu,arc_challenge,gsm8k\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/autodl-tmp/exp009/eval_results/Qwen2.5-1.5B-Instruct\", \"data_count\": 16533, \"model_name\": \"Qwen2.5-1.5B-Instruct\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/exp009/eval_results/Qwen2.5-1.5B-Instruct\", \"log_path\": \"/root/autodl-tmp/exp009/eval_15b_instruct.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T10:50:00.140Z\", \"metrics\": {\"mmlu_acc\": 0.577, \"arc_acc\": 0.765, \"gsm8k_acc\": 0.593, \"mmlu_n\": 14042, \"arc_n\": 1172, \"gsm8k_n\": 1319}}, \"exp_009_05b_instruct_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T10:47:58.197Z\", \"updated_at\": \"2026-05-17T10:50:23.583Z\", \"hypothesis\": \"Qwen2.5-0.5B-Instruct zero-shot eval provides cross-family IRT calibration baselines: instruct-tuned models without contamination training serve as uncontaminated respondents for IRT parameter estimation\", \"spec\": {\"command\": \"python run_eval.py --model Qwen2.5-0.5B-Instruct --benchmarks mmlu,arc_challenge,gsm8k\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/autodl-tmp/exp009/eval_results/Qwen2.5-0.5B-Instruct\", \"data_count\": 16533, \"model_name\": \"Qwen2.5-0.5B-Instruct\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/exp009/eval_results/Qwen2.5-0.5B-Instruct\", \"log_path\": \"/root/autodl-tmp/exp009/eval_05b_instruct.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T10:49:57.722Z\", \"metrics\": {\"mmlu_acc\": 0.343, \"arc_acc\": 0.5, \"gsm8k_acc\": 0.388, \"mmlu_n\": 14042, \"arc_n\": 1172, \"gsm8k_n\": 1319}}, \"exp_009_deepseek_signals\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T10:48:08.902Z\", \"updated_at\": \"2026-05-17T10:50:13.076Z\", \"hypothesis\": \"Contamination signal computation (embedding similarity, MinK++, self-critique) for DeepSeek-R1-Distill-Qwen-1.5B provides exposure features for cross-architecture IRT calibration comparison\", \"spec\": {\"command\": \"python compute_signals.py --model DeepSeek-R1-Distill-Qwen-1.5B --signals s1,s2,s4 --benchmarks mmlu,arc_challenge,gsm8k\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/autodl-tmp/exp009/signals/DeepSeek-R1-Distill-Qwen-1.5B\", \"data_count\": 16533, \"model_name\": \"DeepSeek-R1-Distill-Qwen-1.5B\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/exp009/signals/DeepSeek-R1-Distill-Qwen-1.5B\", \"log_path\": \"/root/autodl-tmp/exp009/sig_ds_s1.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T10:50:13.076Z\"}, \"exp_009_3b_instruct_signals\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T10:48:07.801Z\", \"updated_at\": \"2026-05-17T10:50:11.151Z\", \"hypothesis\": \"Contamination signal computation (embedding similarity, MinK++, self-critique) for Qwen2.5-3B-Instruct provides exposure features for IRT-based calibration of instruct-tuned models without explicit contamination training\", \"spec\": {\"command\": \"python compute_signals.py --model Qwen2.5-3B-Instruct --signals s1,s2,s4 --benchmarks mmlu,arc_challenge,gsm8k\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/autodl-tmp/exp009/signals/Qwen2.5-3B-Instruct\", \"data_count\": 16533, \"model_name\": \"Qwen2.5-3B-Instruct\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/exp009/signals/Qwen2.5-3B-Instruct\", \"log_path\": \"/root/autodl-tmp/exp009/sig_3b_s1.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T10:50:11.151Z\"}, \"exp_009_15b_instruct_signals\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T10:48:06.661Z\", \"updated_at\": \"2026-05-17T10:50:09.029Z\", \"hypothesis\": \"Contamination signal computation (embedding similarity, MinK++, self-critique) for Qwen2.5-1.5B-Instruct provides exposure features for IRT-based calibration of instruct-tuned models without explicit contamination training\", \"spec\": {\"command\": \"python compute_signals.py --model Qwen2.5-1.5B-Instruct --signals s1,s2,s4 --benchmarks mmlu,arc_challenge,gsm8k\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/autodl-tmp/exp009/signals/Qwen2.5-1.5B-Instruct\", \"data_count\": 16533, \"model_name\": \"Qwen2.5-1.5B-Instruct\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/exp009/signals/Qwen2.5-1.5B-Instruct\", \"log_path\": \"/root/autodl-tmp/exp009/signals_15b.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T10:50:09.029Z\"}, \"exp_009_05b_instruct_signals\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T10:48:05.473Z\", \"updated_at\": \"2026-05-17T10:50:07.031Z\", \"hypothesis\": \"Contamination signal computation (embedding similarity, MinK++, self-critique) for Qwen2.5-0.5B-Instruct provides exposure features for IRT-based calibration of instruct-tuned models without explicit contamination training\", \"spec\": {\"command\": \"python compute_signals.py --model Qwen2.5-0.5B-Instruct --signals s1,s2,s4 --benchmarks mmlu,arc_challenge,gsm8k\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/autodl-tmp/exp009/signals/Qwen2.5-0.5B-Instruct\", \"data_count\": 16533, \"model_name\": \"Qwen2.5-0.5B-Instruct\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/exp009/signals/Qwen2.5-0.5B-Instruct\", \"log_path\": \"/root/autodl-tmp/exp009/signals_05b.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T10:50:07.031Z\"}, \"exp_006_mmlu_domain_gamma_no05b_j13\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T06:41:41.966Z\", \"updated_at\": \"2026-05-17T08:30:58.512Z\", \"hypothesis\": \"Excluding 0.5B models (severe position bias, A-rate 37-98%) from MMLU domain IRT will produce cleaner gamma estimates. If Math gamma remains significant at J=13, the domain-differential claim is robust to model pool composition.\", \"spec\": {\"command\": \"python /root/contamcal-irt-calibration/exp006/run_mmlu_domain_gamma_no05b.py\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/autodl-tmp/exp006/mmlu_domain_irt_no05B/\", \"data_count\": 13, \"model_name\": \"2PL+gamma Stan (CmdStan MCMC)\", \"seed\": 42, \"checkpoint_path\": \"/root/contamcal-irt-calibration/exp006/mmlu_domain_irt_no05b/\", \"log_path\": \"/root/contamcal-irt-calibration/exp006/mmlu_domain_irt_no05b/\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-17T08:30:47.182Z\", \"metrics\": {\"gamma_pooled\": 0.107, \"gamma_pooled_ci\": \"[-0.401, 0.625]\", \"gamma_pooled_sig\": false, \"gamma_math\": 0.499, \"gamma_math_sig\": false, \"gamma_social_sci\": -0.571, \"gamma_social_sci_sig\": true, \"gamma_social_sci_ci\": \"[-1.054, -0.103]\", \"domains_sig_positive\": 0, \"domains_sig_negative\": 1, \"n_respondents\": 13, \"n_domains\": 8}}, \"exp_001_eval_3B_d000_s42_a32_batch\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T02:03:01.091Z\", \"updated_at\": \"2026-05-17T03:51:19.620Z\", \"spec\": {\"command\": \"evaluate.py 3B d000_s42 a32 aligned (mmlu/gsm8k/arc/humaneval)\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:1\", \"pid\": \"676487\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d000_s42_a32_batch.log\", \"submitted_at\": \"2026-05-16T02:03:17.864Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"gpu_ids\": [\"cuda:1\"], \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval (aligned)\", \"model_name\": \"Qwen2.5-3B\", \"seed\": 42, \"data_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42_a32_aligned\", \"data_count\": 4, \"parent\": \"exp_001_sft_3B_d000_s42_a32\", \"hypothesis\": \"3B d000 s42 alpha=32 aligned eval. D076-retrained checkpoint (lr=5e-5). 0% contamination baseline for s42 IRT pool.\", \"wall_clock_seconds\": 18258.1, \"gpu_hours\": 5.07}, \"reproduce\": {\"finished_at\": \"2026-05-16T06:02:34.580Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T06:02:38.444291+00:00\"}]}, \"metrics\": {\"mmlu\": {\"aligned\": 0.6307, \"para_aligned\": 0.6431, \"aligned_n\": 14042, \"para_aligned_n\": 6596}, \"gsm8k\": {\"aligned\": 0.141, \"para_aligned\": 0.0526, \"aligned_n\": 1319, \"para_aligned_n\": 228}, \"arc_challenge\": {\"aligned\": 0.8242, \"para_aligned\": 0.8106, \"aligned_n\": 1172, \"para_aligned_n\": 697}, \"humaneval\": {\"aligned\": 0.1402, \"para_aligned\": 0.1923, \"aligned_n\": 164, \"para_aligned_n\": 26}}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d000_s42_a32_batch.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T07:07:35.972Z\", \"hypothesis\": \"Qwen2.5-3B d000 s42 alpha=32 eval batch produces zero-dose control responses for IRT baseline calibration\"}, \"exp_001_sft_3B_d100_s123_a32_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:34:08.644Z\", \"updated_at\": \"2026-05-17T03:51:18.060Z\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_a32_s123/lora_adapter\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_3B_d100_s123_a32_v2.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T21:28:25.941Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T21:28:47.077570+00:00\"}]}, \"metrics\": {\"train_loss\": 1.1805, \"mean_token_accuracy\": 0.7348, \"train_runtime_seconds\": 17608.59, \"train_steps\": 4159, \"epoch\": 1, \"train_samples_per_second\": 3.778, \"entropy\": 1.231}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T21:32:45.981Z\", \"hypothesis\": \"Qwen2.5-3B SFT d100 s123 alpha=32 v2 retrains with standardized hyperparams for consistent IRT pooling\"}, \"exp_001_eval_3B_d100_s42_a32_batch\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T02:34:14.777Z\", \"updated_at\": \"2026-05-17T03:51:16.720Z\", \"hypothesis\": \"Qwen2.5-3B d100 s42 alpha=32 eval batch produces maximum-dose responses for standardized IRT dose-response curve\", \"parent\": \"exp_001_sft_3B_d100_s42_a32_v3\", \"spec\": {\"pid\": 687341, \"server\": \"cqa1-21977\", \"gpu\": \"cuda:3\", \"note\": \"Actual eval subprocess. Wrapper PID 687347 dead. Aligned DONE, para_aligned in progress.\"}, \"reproduce\": {\"finished_at\": \"2026-05-16T06:29:31.545Z\"}, \"failure_reason\": \"RESOLVED: wrapper PID 687347 died, eval subprocess completed normally. aligned + para_aligned both complete with .done markers.\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T06:29:33.982Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T06:29:37.193748+00:00\"}]}, \"metrics\": {\"aligned\": {\"mmlu\": 0.6364, \"gsm8k\": 0.7036, \"arc_challenge\": 0.8208, \"humaneval_correct\": \"26/164\"}, \"para_aligned\": {\"mmlu\": 0.6674, \"gsm8k\": 0.5702, \"arc_challenge\": 0.8106, \"humaneval_correct\": \"2/26\"}}}, \"exp_001_eval_3B_d100_s123_a32_batch\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T21:35:56.659Z\", \"updated_at\": \"2026-05-17T03:51:15.119Z\", \"hypothesis\": \"Qwen2.5-3B d100 s123 alpha=32 eval batch produces maximum-dose responses for standardized IRT pooling matrix\", \"parent\": \"exp_001_sft_3B_d100_s123_a32_v2\", \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_a32_s123/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval (aligned + para_aligned)\", \"model_name\": \"Qwen2.5-3B\", \"seed\": 123, \"data_path\": \"/root/autodl-tmp/exp001/paraphrases\", \"data_count\": 4, \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_a32_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_a32_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache && CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_a32_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_a32_s123_para_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --paraphrase-dir /root/autodl-tmp/exp001/paraphrases --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:0\"], \"pid\": 642752, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d100_s123_a32_batch.log\", \"submitted_at\": \"2026-05-15T21:36:30Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_a32_s123/lora_adapter\", \"wall_clock_seconds\": 21347.7, \"gpu_hours\": 5.93}, \"reproduce\": {\"finished_at\": \"2026-05-16T03:10:21.318Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T03:10:38.597830+00:00\"}]}, \"metrics\": {\"mmlu\": {\"aligned\": 0.633, \"para_aligned\": 0.6598, \"aligned_n\": 14042, \"para_aligned_n\": 6596}, \"gsm8k\": {\"aligned\": 0.7074, \"para_aligned\": 0.5746, \"aligned_n\": 1319, \"para_aligned_n\": 228}, \"arc_challenge\": {\"aligned\": 0.8251, \"para_aligned\": 0.8049, \"aligned_n\": 1172, \"para_aligned_n\": 697}, \"humaneval\": {\"aligned\": 0.1159, \"para_aligned\": 0, \"aligned_n\": 164, \"para_aligned_n\": 26}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T03:32:17.706Z\"}, \"exp_001_eval_3B_d005_s123_gsm8k\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:43:47.263Z\", \"updated_at\": \"2026-05-17T03:51:12.786Z\", \"spec\": {\"command\": \"bash -c 'source conda && evaluate.py --benchmarks gsm8k --mc-format aligned --adapter Qwen2.5-3B_d005_s123'\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:2\"], \"pid\": \"623480\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d005_s123_gsm8k.log\", \"submitted_at\": \"2026-05-15T19:43:44.767Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s123/lora_adapter\", \"data_count\": 0, \"model_name\": \"Qwen/Qwen2.5-3B\", \"seed\": 123, \"checkpoint_source\": \"exp_001_sft_3B_d005_s123\", \"eval_data\": \"gsm8k aligned\", \"wall_clock_seconds\": 11695.9, \"gpu_hours\": 3.25}, \"hypothesis\": \"Qwen2.5-3B d005 s123 GSM8K rerun fills missing benchmark cell for complete dose-response IRT matrix\", \"reproduce\": {\"finished_at\": \"2026-05-15T22:51:16.656Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T22:51:33.234370+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"gsm8k\": 0.6308}, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d005_s123_gsm8k.log\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_s123_gsm8k_rerun\", \"completed_at\": \"2026-05-15T22:58:40.681Z\"}, \"exp_001_sft_llama32_3B_d005_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T15:31:30.450Z\", \"updated_at\": \"2026-05-17T03:51:06.063Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration && python exp001/train_sft.py --model-name /root/autodl-tmp/models/LLM-Research/Llama-3___2-3B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Llama-3.2-3B_d005_s42 --seed 42 --batch-size 2 --grad-accum 8 --lr 5e-5 --gradient-checkpointing --merge --gpu 0\\\"\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:0\", \"pid\": 804565, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_llama32_3B_d005_s42.log\", \"submitted_at\": \"2026-05-16T15:31:29.388Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl\", \"data_count\": 2706, \"model_name\": \"Llama-3.2-3B\", \"seed\": 42, \"wall_clock_seconds\": 8290.5, \"gpu_hours\": 2.3}, \"reproduce\": {\"finished_at\": \"2026-05-16T17:49:35.377Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T17:49:39.916Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T17:49:45.176960+00:00\"}]}, \"metrics\": {\"train_loss\": 1.5206, \"train_runtime_sec\": 8140.83, \"mean_token_accuracy\": 0.6599, \"train_samples_per_second\": 6.243, \"train_steps_per_second\": 0.39, \"epoch\": 1, \"note\": \"Training completed successfully. Merge failed (disk full) but LoRA adapter saved intact.\"}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Llama-3.2-3B_d005_s42/\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_llama32_3B_d005_s42.log\", \"hypothesis\": \"Llama-3.2-3B SFT with 5% contamination dose (s42) trains cross-family respondent for low-dose IRT data point\"}, \"exp_001_eval_llama32_3B_d000_s42_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T15:37:57.223Z\", \"updated_at\": \"2026-05-17T03:51:04.880Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python evaluate.py --model-path /root/autodl-tmp/exp001/checkpoints/Llama-3.2-3B_d000_s42/merged --benchmarks gsm8k arc_challenge humaneval --mc-format aligned --output-dir /root/autodl-tmp/exp001/eval_results/Llama-3.2-3B_d000_s42_aligned/ --batch-size 4\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:1\", \"pid\": 807025, \"data_path\": \"Llama-3.2-3B_d000_s42/merged\", \"data_count\": 0, \"model_name\": \"Llama-3.2-3B_d000_s42\", \"seed\": 42}, \"reproduce\": {\"finished_at\": \"2026-05-16T18:23:06.478Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T18:23:04.456Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T18:23:21.134116+00:00\"}]}, \"metrics\": {\"mmlu\": 0.4545, \"gsm8k\": 0.1918, \"arc_challenge\": 0.6007, \"humaneval_pass@1\": 0.0427}, \"hypothesis\": \"Llama-3.2-3B d000 s42 eval v3 produces clean-baseline benchmark responses for cross-family IRT zero-dose control\"}, \"exp_001_sft_llama32_3B_d100_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T15:31:33.384Z\", \"updated_at\": \"2026-05-17T03:51:00.432Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration && python exp001/train_sft.py --model-name /root/autodl-tmp/models/LLM-Research/Llama-3___2-3B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Llama-3.2-3B_d100_s42 --seed 42 --batch-size 2 --grad-accum 8 --lr 5e-5 --gradient-checkpointing --merge --gpu 0\\\"\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:5\", \"pid\": 804786, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_llama32_3B_d100_s42.log\", \"submitted_at\": \"2026-05-16T15:31:32.846Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl\", \"data_count\": 54133, \"model_name\": \"Llama-3.2-3B\", \"seed\": 42, \"wall_clock_seconds\": 10479.1, \"gpu_hours\": 2.91}, \"reproduce\": {\"finished_at\": \"2026-05-16T18:19:28.413Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T18:19:36.612245+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 1.5435, \"mean_token_accuracy\": 0.6505, \"train_runtime_sec\": 9847, \"train_steps_per_second\": 0.422, \"epochs\": 1}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Llama-3.2-3B_d100_s42/merged/\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_llama32_3B_d100_s42.log\", \"completed_at\": \"2026-05-16T18:26:11.938Z\", \"hypothesis\": \"Llama-3.2-3B SFT with 100% contamination dose (s42) trains cross-family respondent for maximum-dose IRT reference\"}, \"exp_002_signals_15B_instruct_arc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T17:44:18.851Z\", \"updated_at\": \"2026-05-17T03:50:58.572Z\", \"spec\": {\"command\": \"python compute_signals.py --model-path /root/autodl-tmp/models/Qwen2.5-1.5B-Instruct --benchmark arc_challenge --signal all --output-dir /root/autodl-tmp/exp002/signals/Qwen2.5-1.5B-Instruct/ --batch-size 8\", \"server\": \"cqa1-21977\", \"data_path\": \"arc_challenge (1172 items)\", \"data_count\": 1172, \"model_name\": \"Qwen2.5-1.5B-Instruct\", \"seed\": 42, \"gpu\": \"cuda:2\", \"pid\": 823705, \"hypothesis\": \"1.5B-Instruct ARC signals — completes 3-benchmark trifecta for RRF inclusion\"}, \"reproduce\": {\"finished_at\": \"2026-05-16T18:48:43.264Z\"}, \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T18:48:48.057Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T18:48:54.634154+00:00\"}]}, \"hypothesis\": \"Qwen2.5-1.5B-Instruct ARC signal v1 computes exposure scores as RL-proxy respondent for IRT pooling\"}, \"exp_002_signals_15B_instruct_mmlu\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T17:21:29.910Z\", \"updated_at\": \"2026-05-17T03:50:49.622Z\", \"spec\": {\"command\": \"python compute_signals.py --model-path Qwen2.5-1.5B-Instruct --benchmark mmlu --signal all --ref-model-path Qwen2.5-1.5B --output-dir /root/autodl-tmp/exp002/signals/Qwen2.5-1.5B-Instruct/ --batch-size 8\", \"server\": \"cqa1-21977\", \"data_path\": \"mmlu (14042 items)\", \"data_count\": 14042, \"model_name\": \"Qwen2.5-1.5B-Instruct\", \"seed\": 42, \"gpu\": \"cuda:4\", \"pid\": 810809, \"hypothesis\": \"1.5B-Instruct MMLU signals (selfcritique chunking phase)\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T19:12:15.311Z\", \"reproduce\": {\"finished_at\": \"2026-05-16T19:12:20.994Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"notes\": \"失败原因: 进程死亡无日志（非submit_training_job提交，无tmux保护）。可能同一HF Hub网络问题。| 已有成果: 无 | 建议: 用submit_training_job重新提交，确保HF_HUB_OFFLINE=1且模型已缓存\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T19:12:34.922573+00:00\"}]}, \"hypothesis\": \"Qwen2.5-1.5B-Instruct MMLU signal v1 computes exposure scores as RL-proxy respondent for IRT pooling\"}, \"exp_002_signals_llama32_3B_d000_arc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T18:25:27.120Z\", \"updated_at\": \"2026-05-17T03:50:47.942Z\", \"spec\": {\"command\": \"python compute_signals.py --model-path /root/autodl-tmp/exp001/checkpoints/Llama-3.2-3B_d000_s42/merged --benchmark arc_challenge --signal all --output-dir /root/autodl-tmp/exp002/signals/Llama-3.2-3B_d000_s42/ --batch-size 4\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/autodl-tmp/exp002/signals/Llama-3.2-3B_d000_s42/\", \"data_count\": 1172, \"model_name\": \"Llama-3.2-3B_d000_s42\", \"seed\": 42}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/exp002/signals/Llama-3.2-3B_d000_s42/\", \"log_path\": \"/root/autodl-tmp/exp002/signals/Llama-3.2-3B_d000_s42/signal_s4_selfcritique_arc_challenge.json\", \"completed_at\": \"2026-05-16T19:15:19.604Z\", \"hypothesis\": \"Llama-3.2-3B d000 ARC signal computes clean-baseline exposure scores for cross-family IRT negative control\"}, \"exp_002_signals_llama32_3B_d000_gsm8k_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T19:14:57.901Z\", \"updated_at\": \"2026-05-17T03:50:46.605Z\", \"spec\": {\"command\": \"python compute_signals.py --model-path /root/autodl-tmp/exp001/checkpoints/Llama-3.2-3B_d000_s42/merged --benchmark gsm8k --signal all --output-dir /root/autodl-tmp/exp002/signals/Llama-3.2-3B_d000_s42/ --batch-size 8\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:2\", \"pid\": 839655, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_002_signals_llama32_3B_d000_gsm8k_v2.log\", \"submitted_at\": \"2026-05-16T19:18:51.355Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/exp001/checkpoints/Llama-3.2-3B_d000_s42/merged\", \"data_count\": 1, \"model_name\": \"Llama-3.2-3B_d000_s42\", \"seed\": 42, \"checkpoint_source\": \"exp_001_sft_llama32_3B_d000_s42\", \"eval_data\": \"gsm8k\", \"note\": \"Process already running on cuda:2 when task received\", \"wall_clock_seconds\": 1203.7, \"gpu_hours\": 0.33}, \"reproduce\": {\"finished_at\": \"2026-05-16T19:36:38.415Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T19:36:43.086578+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/exp002/signals/Llama-3.2-3B_d000_s42/\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_002_signals_llama32_3B_d000_gsm8k_v2.log\", \"metrics\": {\"signal_files\": {\"signal_s1_embedding_gsm8k.json\": {\"size\": \"717K\", \"items\": 1319}, \"signal_s2_minkpp_gsm8k.json\": {\"size\": \"266K\", \"items\": 1319}, \"signal_s4_selfcritique_gsm8k.json\": {\"size\": \"311K\", \"items\": 1319}, \"signals_merged_gsm8k.json\": {\"size\": \"238K\", \"items\": 1319}}, \"total_items\": 1319, \"signals_computed\": [\"s1_embedding\", \"s2_minkpp\", \"s4_selfcritique\"], \"all_signals_nonempty\": true}, \"completed_at\": \"2026-05-16T19:38:55.060Z\", \"hypothesis\": \"Llama-3.2-3B d000 GSM8K signal v2 computes clean-baseline exposure scores for cross-family IRT negative control\"}, \"exp_001_eval_llama32_3B_d025_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T17:33:40.526Z\", \"updated_at\": \"2026-05-17T03:50:45.441Z\", \"spec\": {\"hypothesis\": \"Llama-3.2-3B cross-family validation: d025 (25% contamination) eval for IRT pool expansion\", \"model_name\": \"Llama-3.2-3B_d025_s42\", \"seed\": 42, \"checkpoint_source\": \"exp_001_sft_llama32_3B_d025_s42\", \"eval_data\": \"mmlu gsm8k arc_challenge humaneval\", \"data_path\": \"Llama-3.2-3B_d025_s42/merged\", \"data_count\": 0, \"server\": \"cqa1-21977\", \"gpu\": \"cuda:3\", \"note\": \"RUNNING set by spec update, awaiting actual process submission after tmux cleanup\"}, \"reproduce\": {\"finished_at\": \"2026-05-16T20:31:30.441Z\"}, \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T20:31:33.550Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T20:31:38.114890+00:00\"}]}, \"metrics\": {\"mmlu\": 0.415, \"humaneval_pass@1\": 0.0244}, \"hypothesis\": \"Llama-3.2-3B d025 s42 eval produces benchmark responses for mid-dose contamination data point in cross-family IRT\"}, \"exp_001_eval_llama32_3B_d005_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T17:49:53.423Z\", \"updated_at\": \"2026-05-17T03:50:38.877Z\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration && CUDA_VISIBLE_DEVICES=0 python exp001/evaluate.py --model-path /root/autodl-tmp/models/LLM-Research/Llama-3___2-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Llama-3.2-3B_d005_s42/lora_adapter --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --output-dir /root/autodl-tmp/exp001/eval_results/Llama-3.2-3B_d005_s42_aligned/ --batch-size 4\", \"server\": \"cqa1-21977\", \"data_path\": \"mmlu+gsm8k+arc_challenge+humaneval\", \"data_count\": 0, \"model_name\": \"Llama-3.2-3B_d005_s42\", \"seed\": 42, \"gpu\": [\"cuda:0\"], \"pid\": \"825638\", \"checkpoint_source\": \"exp_001_sft_llama32_3B_d005_s42\", \"eval_data\": \"mmlu gsm8k arc_challenge humaneval\", \"hypothesis\": \"Llama-3.2-3B cross-family validation: d005 (5% contamination) eval for IRT pool expansion\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_llama32_3B_d005_s42.log\", \"submitted_at\": \"2026-05-16T17:55:00Z\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 10974.0, \"gpu_hours\": 3.05}, \"reproduce\": {\"finished_at\": \"2026-05-16T20:57:50.782Z\"}, \"failure_reason\": \"EXIT_CODE=1 from HumanEval sandbox — false positive, all 4 benchmarks completed with .done sentinel\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T20:57:53.959Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T20:58:00.426702+00:00\"}]}, \"metrics\": {\"mmlu\": 0.4256, \"arc_challenge\": 0.5956, \"gsm8k\": 0.2722, \"humaneval_pass@1\": 0.0122}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Llama-3.2-3B_d005_s42_aligned/\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_llama32_3B_d005_s42.log\", \"hypothesis\": \"Llama-3.2-3B d005 s42 eval produces benchmark responses for low-dose contamination data point in cross-family IRT\"}, \"exp_002_signals_15B_instruct_arc_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T17:57:42.344Z\", \"updated_at\": \"2026-05-17T03:50:37.606Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python exp002/compute_signals.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B-Instruct --benchmark arc_challenge --signal all --output-dir /root/autodl-tmp/exp002/signals/Qwen2.5-1.5B-Instruct/ --batch-size 4\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:2\"], \"pid\": 870622, \"log_path\": \"/root/autodl-tmp/exp002/signals/Qwen2.5-1.5B-Instruct/run_arc_v2.log\", \"submitted_at\": \"2026-05-16T17:57:41.811Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"gpu_ids\": [3], \"model_name\": \"Qwen2.5-1.5B-Instruct\", \"data_path\": \"arc_challenge\", \"data_count\": 1172, \"seed\": 42, \"tmux_session\": \"exp002_15B_instruct_arc_v2\", \"output_dir\": \"/root/autodl-tmp/exp002/signals/Qwen2.5-1.5B-Instruct/\", \"checkpoint_path\": \"/root/autodl-tmp/exp002/signals/Qwen2.5-1.5B-Instruct/signals_merged_arc_challenge.json\", \"wall_clock_seconds\": 12925.4, \"gpu_hours\": 3.59}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T21:33:07.203Z\", \"hypothesis\": \"Qwen2.5-1.5B-Instruct ARC signal v2 computes valid exposure scores as RL-proxy respondent for IRT pooling\"}, \"exp_001_eval_llama32_3B_d100_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T18:25:29.342Z\", \"updated_at\": \"2026-05-17T03:50:36.185Z\", \"spec\": {\"command\": \"python evaluate.py --model-path /root/autodl-tmp/exp001/checkpoints/Llama-3.2-3B_d100_s42/merged --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --output-dir /root/autodl-tmp/exp001/eval_results/Llama-3.2-3B_d100_s42_aligned/ --batch-size 4\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/autodl-tmp/exp001/checkpoints/Llama-3.2-3B_d100_s42/merged\", \"data_count\": 4, \"model_name\": \"Llama-3.2-3B_d100_s42\", \"seed\": 42, \"checkpoint_source\": \"exp_001_sft_llama32_3B_d100_s42\", \"eval_data\": \"mmlu gsm8k arc_challenge humaneval\", \"parent\": \"exp_001_sft_llama32_3B_d100_s42\", \"gpu\": \"cuda:5\", \"pid\": 831033, \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Llama-3.2-3B_d100_s42_aligned/\", \"log_path\": \"/root/autodl-tmp/exp001/eval_results/Llama-3.2-3B_d100_s42_aligned/\"}, \"reproduce\": {\"finished_at\": \"2026-05-16T21:36:06.822Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T21:36:04.738Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T21:36:20.458040+00:00\"}]}, \"metrics\": {\"mmlu_acc\": 0.3408, \"arc_acc\": 0.5981, \"gsm8k_acc\": 0.26, \"note\": \"MMLU degenerate (all-A prediction), ARC/GSM8K valid\"}, \"hypothesis\": \"Llama-3.2-3B d100 s42 eval generates benchmark responses for maximum-contamination dose-response reference point in IRT\"}, \"exp_002_signals_15B_instruct_mmlu_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T19:15:00.958Z\", \"updated_at\": \"2026-05-17T03:50:34.296Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python exp002/compute_signals.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B-Instruct --benchmark mmlu --signal all --output-dir /root/autodl-tmp/exp002/signals/Qwen2.5-1.5B-Instruct/ --batch-size 4\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:4\"], \"pid\": 870969, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_002_signals_15B_instruct_mmlu_v2.log\", \"submitted_at\": \"2026-05-16T19:18:54.012Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"gpu_ids\": [0], \"model_name\": \"Qwen2.5-1.5B-Instruct\", \"data_path\": \"/root/autodl-tmp/.hf_cache/cais___mmlu/all/0.0.0/\", \"data_count\": 14042, \"seed\": null, \"tmux_session\": \"exp002_15B_instruct_mmlu_v2\", \"output_dir\": \"/root/autodl-tmp/exp002/signals/Qwen2.5-1.5B-Instruct/\", \"wall_clock_seconds\": 7940.6, \"gpu_hours\": 2.21}, \"reproduce\": {\"finished_at\": \"2026-05-16T21:31:10.543Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T21:31:14.606Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T21:31:21.613535+00:00\"}]}, \"metrics\": {\"items\": 14042, \"benchmark\": \"mmlu\", \"signals\": \"s1+s2+s4\", \"note\": \"EXIT_CODE=1 was false positive, data verified complete by Reviewer\"}, \"hypothesis\": \"Qwen2.5-1.5B-Instruct MMLU signal v2 computes reliable exposure scores as RL-proxy respondent for IRT pooling\"}, \"exp_002_signals_llama32_3B_d005_mmlu\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T19:42:04.520Z\", \"updated_at\": \"2026-05-17T03:50:32.395Z\", \"spec\": {\"command\": \"python exp002/compute_signals.py --model-path /root/autodl-tmp/exp001/checkpoints/Llama-3.2-3B_d005_s42/merged --benchmark mmlu --signal all --output-dir /root/autodl-tmp/exp002/signals/Llama-3.2-3B_d005_s42/ --batch-size 4\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/autodl-tmp/exp001/checkpoints/Llama-3.2-3B_d005_s42/merged\", \"data_count\": 14042, \"model_name\": \"Llama-3.2-3B_d005_s42\", \"seed\": 42, \"gpu\": \"cuda:4\"}, \"pid\": 842929, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_002_signals_llama32_3B_d005_mmlu.log\", \"reproduce\": {\"finished_at\": \"2026-05-16T22:08:03.783Z\"}, \"failure_reason\": \"false alarm: signal job completed successfully but had no W&B — cron误判\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T22:08:06.727Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T22:08:10.861288+00:00\"}]}, \"notes\": \"实际成功完成。3 signals (s1_embedding, s2_minkpp, s4_selfcritique) x MMLU 14042 items。输出: /root/autodl-tmp/exp002/signals/Llama-3.2-3B_d005_s42/signals_merged_mmlu.json\", \"hypothesis\": \"Llama-3.2-3B d005 MMLU signal computation produces valid contamination exposure scores for cross-family IRT pooling\"}, \"exp_006_scale_stratified_irt\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T11:33:57.164Z\", \"updated_at\": \"2026-05-17T03:50:24.814Z\", \"spec\": {\"command\": \"python run_pooled_rrf_irt.py --scales {0.5B,1.5B,3B} --model-type 2pl_gamma --benchmarks mmlu gsm8k arc_challenge\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/autodl-tmp/exp001/eval_results\", \"data_count\": \"3 scales x 3 benchmarks = 7 fits (0.5B only gsm8k due to D045)\", \"model_name\": \"2pl_gamma IRT\", \"seed\": 42}, \"conclusion\": \"negative\", \"notes\": \"Scale-stratified 2PL+gamma IRT: gamma NOT monotonically scale-dependent. CIs overlap 0 for most strata (N=6-8 underpowered). 3B GSM8K drives bulk of pooled calibration gain (dMAE=0.155). 1.5B shows anomalous negative gamma (noise). Only 1.5B ARC has significant gamma (1.17) but PPP=0.013 indicates poor fit.\", \"checkpoint_path\": \"/root/autodl-tmp/exp006/scale_stratified_irt/\", \"log_path\": \"/tmp/irt_05b.log, /tmp/irt_15b.log, /tmp/irt_3b.log\", \"completed_at\": \"2026-05-16T11:34:29.087Z\", \"hypothesis\": \"Scale-stratified IRT (separate 2PL+gamma per model scale: 0.5B, 1.5B, 3B) produces reliable per-scale gamma estimates with N=6-8 examinees per stratum, enabling scale-specific contamination characterization\", \"parent\": \"exp_006_pooled_2pl_gamma_qwen_n24\"}, \"exp_006_pooled_irt_05b_15b_arc_2pl\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T09:20:55.439Z\", \"updated_at\": \"2026-05-17T03:50:21.274Z\", \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/exp006/pooled_irt_05b_15b/arc_2pl/\", \"log_path\": \"/tmp/arc_2pl_irt.log\", \"completed_at\": \"2026-05-16T09:21:30.839Z\", \"conclusion_notes\": \"2PL+gamma converges well (Rhat=1.009, ESS=1315, 0 divergences) and gamma=2.73 significantly excludes zero (CI=[1.31,4.14]). However PPP=0.000 persists — same as 4PL+gamma. N=8 1.5B models with 1172 items; model misspecification not resolved by reducing parameters. ARC response patterns likely violate IRT unidimensionality assumption. Gamma estimate unreliable due to PPP failure.\", \"hypothesis\": \"2PL+gamma pooled IRT on 0.5B+1.5B ARC (N=8) with signal-derived exposure detects significant negative gamma, replicating the contamination-induced forgetting pattern seen in single-scale fits\", \"parent\": \"exp006-pooled-05B-15B-arc-v2\"}, \"exp_005_noise_prop_v4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T21:53:56.486Z\", \"updated_at\": \"2026-05-17T03:50:12.475Z\", \"hypothesis\": \"Measurement error (sigma_e) in exposure scores propagates through IRT to widen calibrated-score CIs monotonically; CI width is dominated by sigma_e magnitude rather than N_models\", \"spec\": {\"command\": \"python run_noise_propagation_v3.py --output-dir output_v3 --base-seed 42 --n-seeds 5\", \"server\": \"local\", \"pid\": 617670, \"data_path\": \"synthetic\", \"data_count\": 9000, \"model_name\": \"4PL+gamma IRT\", \"seed\": 42, \"checkpoint_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp005_noise_propagation/output_v3/\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp005_noise_propagation/exp005_v4_restart.log\"}, \"notes\": \"25/25 fits complete, all converged. Conclusion changed to inconclusive per Reviewer #2: n=5, Spearman ρ=0.4, p=0.505, power~0.2 — insufficient to distinguish no-effect from underpowered. ME vs Simple CI width difference <0.03% (0.0997-0.1000). Downgraded to appendix robustness check.\", \"checkpoint_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp005_noise_propagation/output_v3/\", \"log_path\": \"/tmp/exp005_noise_prop_v3.log\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T23:25:34.092Z\", \"metrics\": {\"fits_completed\": \"25/25\", \"all_converged\": true, \"ci_width_range\": \"0.0997-0.1000\", \"monotonicity_rho\": 0.4, \"monotonicity_p\": 0.5, \"finding\": \"ME analytic model calibrated-score CI insensitive to sigma_e magnitude\"}, \"parent\": \"exp_004_sim_sweep\"}, \"exp006_cross_family_pooled_irt\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T21:16:11.039Z\", \"updated_at\": \"2026-05-17T03:50:09.357Z\", \"hypothesis\": \"Cross-family pooled IRT (Qwen 0.5B/1.5B/3B + Llama-3.2-3B) with 2PL+gamma model tests whether contamination gamma signal persists when pooling across model families, validating the IRT framework's generalizability\", \"spec\": {\"command\": \"python pooled_rrf_irt.py --models 0.5B+1.5B+3B+Llama-3.2-3B --benchmarks gsm8k arc_challenge\", \"server\": \"cqa1-21977\", \"data_path\": \"pooled RRF signals (0.5B+1.5B+3B+Llama-3.2-3B)\", \"data_count\": 0, \"model_name\": \"2PL+gamma pooled IRT\", \"seed\": 42}, \"conclusion\": \"negative\", \"metrics\": {\"v3_clean\": true, \"arc_gamma_pooled\": 0.002, \"mmlu_gamma_pooled\": 0.213, \"gsm8k_gamma_pooled\": -0.11, \"arc_gamma_qwen_only\": 0.727, \"mmlu_gamma_qwen_only\": 0.655, \"N_pooled_arc\": 20, \"N_pooled_mmlu\": 20, \"N_pooled_gsm8k\": 28, \"family_specificity_arc_delta\": -0.725}, \"checkpoint_path\": \"/root/autodl-tmp/exp006/results_cross_family_irt/pooled_rrf_irt_results.json\", \"log_path\": \"/root/autodl-tmp/exp006/results_cross_family_irt/pooled_rrf_irt_results.json\", \"completed_at\": \"2026-05-16T21:16:54.524Z\", \"parent\": \"exp_006_pooled_2pl_gamma_qwen_n24\"}, \"exp006-pooled-05B-15B-gsm8k-v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:59:47.176Z\", \"updated_at\": \"2026-05-17T03:50:07.918Z\", \"spec\": {\"command\": \"python run_exp006.py --pool-scales 05B 15B --benchmark gsm8k --require-signals --joint-fit --exclude-models 3B_d000\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/autodl-tmp/exp006/\", \"data_count\": 8, \"model_name\": \"0.5B+1.5B pooled\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_v2\", \"log_path\": \"/root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_v2\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T23:00:23.015Z\", \"metrics\": {\"exposure_source\": \"signal_rrf\", \"gamma_perbench\": 0.1871, \"gamma_perbench_ci\": [-0.92, 1.33], \"gamma_joint\": 0.1202, \"gamma_joint_ci\": [-0.74, 0.96], \"mae\": 0.036, \"coverage_95\": 0.5, \"ppp\": 0.336, \"n_models\": 8, \"convergence\": \"FAILED (rhat=1.015, ess=330)\", \"NOTE\": \"per-bench not converged; no oracle baseline exists\"}, \"notes\": \"INCONCLUSIVE (Reviewer WARNING): MCMC convergence failed — rhat=1.015, ess=330, gamma CI crosses zero. 等待 exp006-oracle-gsm8k-extended / exp006-pooled-s1only-gsm8k 替代结果。原 conclusion=success 降级为 negative。\", \"hypothesis\": \"Pooled 0.5B+1.5B IRT (N=8) with RRF-derived exposure on GSM8K will yield significant gamma, demonstrating cross-scale contamination detection even with generative benchmarks\", \"parent\": \"exp006-pooled-05B-15B-arc-v2\"}, \"exp_002_signals_llama32_3B_d100_mmlu\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T21:17:57.347Z\", \"updated_at\": \"2026-05-17T03:45:38.401Z\", \"hypothesis\": \"Llama-3.2-3B at 100% contamination MMLU signals (s1/s2/s4) for cross-family RRF validation — maximum dosage data point to complement d005 (done) and d025 (running)\", \"spec\": {\"command\": \"compute_signals --model-path Llama-3.2-3B_d100_s42 --benchmark mmlu --signal all\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:1\", \"pid\": \"863173\", \"data_path\": \"mmlu\", \"data_count\": 0, \"model_name\": \"Llama-3.2-3B_d100_s42\", \"seed\": 42, \"checkpoint_path\": \"N/A - signals invalid (model degenerate)\", \"log_path\": \"N/A\", \"kill_reason\": \"d100 model degenerate on MMLU (all-A prediction), signals invalid for IRT\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-16T21:56:12.786Z\"}, \"exp_002_signals_llama32_3B_d100_arc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T21:33:20.334Z\", \"updated_at\": \"2026-05-17T03:05:44.076Z\", \"hypothesis\": \"Llama-3.2-3B at 100% contamination ARC signals (s1/s2/s4) — complements d100 MMLU (running) for full cross-family RRF validation at maximum dosage\", \"conclusion\": \"success\", \"spec\": {\"command\": \"compute_signals --model-path Llama-3.2-3B_d100_s42 --benchmark arc_challenge --signal all\", \"server\": \"cqa1-21977\", \"data_path\": \"arc_challenge\", \"data_count\": 0, \"model_name\": \"Llama-3.2-3B_d100_s42\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/exp002/signals/Llama-3.2-3B_d100_s42/signals_merged_arc_challenge.json\", \"log_path\": \"/root/autodl-tmp/exp002/signals/Llama-3.2-3B_d100_s42/log_arc_challenge.txt\"}, \"completed_at\": \"2026-05-17T03:05:44.076Z\"}, \"exp_002_signals_llama32_3B_d100_gsm8k\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T23:09:46.519Z\", \"updated_at\": \"2026-05-17T03:05:41.922Z\", \"hypothesis\": \"Llama-3.2-3B d100 GSM8K signals (s1/s2/s4) — model valid on GSM8K (acc=0.26, not degenerate). Complements d100 ARC for partial cross-family validation at max dosage.\", \"conclusion\": \"success\", \"spec\": {\"command\": \"compute_signals --model-path Llama-3.2-3B_d100_s42 --benchmark gsm8k --signal all\", \"server\": \"cqa1-21977\", \"data_path\": \"gsm8k\", \"data_count\": 0, \"model_name\": \"Llama-3.2-3B_d100_s42\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/exp002/signals/Llama-3.2-3B_d100_s42/signals_merged_gsm8k.json\", \"log_path\": \"/root/autodl-tmp/exp002/signals/Llama-3.2-3B_d100_s42/log_gsm8k.txt\"}, \"completed_at\": \"2026-05-17T03:05:41.922Z\"}, \"exp_002_signals_llama32_3B_d000_arc_gsm8k\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T22:16:16.282Z\", \"updated_at\": \"2026-05-17T03:05:40.016Z\", \"hypothesis\": \"Llama-3.2-3B d000 (clean baseline) ARC+GSM8K signals for cross-family IRT pool — baseline reference enabling d005/d025/d100 exposure contrast\", \"conclusion\": \"success\", \"spec\": {\"command\": \"compute_signals --model-path Llama-3.2-3B_d000_s42 --benchmark arc_challenge gsm8k --signal all\", \"server\": \"cqa1-21977\", \"data_path\": \"arc_challenge,gsm8k\", \"data_count\": 0, \"model_name\": \"Llama-3.2-3B_d000_s42\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/exp002/signals/Llama-3.2-3B_d000_s42/\", \"log_path\": \"/root/autodl-tmp/exp002/signals/Llama-3.2-3B_d000_s42/\"}, \"completed_at\": \"2026-05-17T03:05:40.016Z\"}, \"exp_002_signals_llama32_3B_d000_mmlu\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-16T18:24:23.141Z\", \"updated_at\": \"2026-05-17T03:05:38.003Z\", \"reproduce\": {\"finished_at\": \"2026-05-16T20:51:28.963Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"completed_at\": \"2026-05-16T20:51:33.602Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T20:51:40.881254+00:00\"}], \"previous_failure\": {\"conclusion\": \"success\"}}, \"hypothesis\": \"Llama-3.2-3B d000 (clean baseline) MMLU signals for cross-family IRT pool — 0% contamination reference point enabling RRF-based exposure scoring\", \"conclusion\": \"success\", \"spec\": {\"command\": \"compute_signals --model-path Llama-3.2-3B_d000_s42 --benchmark mmlu --signal all\", \"server\": \"cqa1-21977\", \"data_path\": \"mmlu\", \"data_count\": 0, \"model_name\": \"Llama-3.2-3B_d000_s42\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/exp002/signals/Llama-3.2-3B_d000_s42/signals_merged_mmlu.json\", \"log_path\": \"/root/autodl-tmp/exp002/signals/Llama-3.2-3B_d000_s42/\"}}, \"exp_004_fisher_heatmap_w4_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T02:27:26.679Z\", \"updated_at\": \"2026-05-17T02:35:51.621Z\", \"hypothesis\": \"Fisher Information heatmap across N×benchmark will show identifiability thresholds for gamma parameter, providing W4 reviewer evidence that N=24 is sufficient for reliable contamination detection\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/exp004/fisher_heatmap/fisher_power_heatmap.pdf\", \"log_path\": \"/root/autodl-tmp/exp004/fisher_heatmap/results_v2.json\", \"server\": \"cqa1-21977\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-17T02:35:49.704Z\", \"metrics\": {\"power_n30_auc70\": 0.82, \"threshold_n20_auc\": 0.75, \"threshold_n30_auc\": 0.7, \"threshold_n50_auc\": 0.65, \"method\": \"analytical_fisher_information_CRLB\", \"model\": \"2PL+gamma\", \"mc_draws\": 50}}, \"exp_002_signals_llama32_3B_d025_completion\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T23:09:03.376Z\", \"updated_at\": \"2026-05-17T00:58:27.395Z\", \"hypothesis\": \"Complete remaining d025 signals (MMLU s4 10000-14042 + merge, GSM8K s4 + merge) after partial failure of parent experiment. Enables d025 RRF → cross-family IRT pool N+1.\", \"parent\": \"exp_002_signals_llama32_3B_d025_mmlu_arc_gsm8k\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 python exp002/compute_signals.py --model-path /root/autodl-tmp/exp001/checkpoints/Llama-3.2-3B_d025_s42/merged --benchmark mmlu --signal s4 --output-dir /root/autodl-tmp/exp002/signals/Llama-3.2-3B_d025_s42/ --batch-size 2\", \"server\": \"cqa1-21977\", \"data_path\": \"mmlu (s4 completion, 4042/14042 remaining)\", \"data_count\": 14042, \"model_name\": \"Llama-3.2-3B_d025_s42\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Llama-3.2-3B_d025_s42/merged\", \"eval_data\": \"mmlu\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/exp002/signals/Llama-3.2-3B_d025_s42/signals_merged_mmlu.json\", \"log_path\": \"/root/autodl-tmp/exp002/signals/Llama-3.2-3B_d025_s42/log_mmlu.txt\", \"completed_at\": \"2026-05-17T00:58:27.395Z\"}, \"exp_002_signals_llama32_3B_d025_mmlu_arc_gsm8k\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T20:20:47.950Z\", \"updated_at\": \"2026-05-16T23:08:53.334Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python compute_signals.py --model-path /root/autodl-tmp/exp001/checkpoints/Llama-3.2-3B_d025_s42/merged --benchmark mmlu arc_challenge gsm8k --signal all --output-dir /root/autodl-tmp/exp002/signals/Llama-3.2-3B_d025_s42/ --batch-size 4\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:2\", \"pid\": 853489, \"data_path\": \"mmlu+arc+gsm8k\", \"data_count\": 0, \"model_name\": \"Llama-3.2-3B_d025_s42\", \"seed\": 42, \"hypothesis\": \"Llama d025 signals for cross-family RRF pipeline\", \"checkpoint_path\": \"/root/autodl-tmp/exp002/signals/Llama-3.2-3B_d025_s42/\", \"log_path\": \"/root/autodl-tmp/logs/signals_llama_d025_all.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-16T22:15:23.248Z\"}, \"failure_reason\": \"Partial completion: ARC complete, MMLU s1+s2 done but s4 partial (10000/14042) + no merge, GSM8K s1+s2 done but s4 missing + no merge. Process died mid-computation.\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-16T22:15:24.362Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T22:15:34.898967+00:00\"}]}}, \"exp_002_signals_llama32_3B_d005_arc_gsm8k\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T20:38:56.313Z\", \"updated_at\": \"2026-05-16T21:08:13.284Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python compute_signals.py --model-path /root/autodl-tmp/exp001/checkpoints/Llama-3.2-3B_d005_s42/merged --benchmark arc_challenge gsm8k --signal all --output-dir /root/autodl-tmp/exp002/signals/Llama-3.2-3B_d005_s42/ --batch-size 4\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:3\", \"pid\": 859360, \"data_path\": \"arc_challenge+gsm8k\", \"data_count\": 0, \"model_name\": \"Llama-3.2-3B_d005_s42\", \"seed\": 42, \"hypothesis\": \"Llama d005 ARC+GSM8K signals for cross-family RRF\"}, \"conclusion\": \"success\", \"log_path\": \"/tmp/signals_llama_d005_arc_gsm8k_cuda3.log\", \"checkpoint_path\": \"/root/autodl-tmp/exp002/signals/Llama-3.2-3B_d005_s42/\", \"hypothesis\": \"Llama-3.2-3B at 5% contamination produces detectable ARC+GSM8K signals (s1/s2/s4) that correlate with Qwen patterns, enabling cross-family RRF validation\", \"completed_at\": \"2026-05-16T21:08:13.284Z\"}, \"exp_004_fisher_heatmap_w4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T20:13:53.855Z\", \"updated_at\": \"2026-05-16T21:00:20.827Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=\\\"\\\" python exp006/run_fisher_heatmap.py --skip-existing --output-dir /root/autodl-tmp/exp006/fisher_info_heatmap/\", \"server\": \"cqa1-21977\", \"gpu\": \"CPU only\", \"pid\": 862089, \"data_path\": \"simulated\", \"data_count\": 2200, \"model_name\": \"2PL+gamma Stan\", \"seed\": 42, \"hypothesis\": \"N x benchmark identifiability heatmap for Claim 3 (restart, 11 remaining conditions)\"}, \"conclusion\": \"failed\", \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"reproduce\": {\"finished_at\": \"2026-05-16T20:57:16.505Z\"}, \"completed_at\": \"2026-05-16T20:57:19.697Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T20:57:26.788872+00:00\"}]}, \"notes\": \"失败原因: OSError [Errno 28] No space left on device — 写 /root/autodl-tmp/exp006/fisher_info_heatmap/arc_N16.json 时磁盘满 | 已有成果: arc_N16 完成 160/200 reps, mmlu/gsm8k 可能已完成 | 建议: 清磁盘后重跑，重跑时可跳过已完成的 condition\"}, \"exp_006_pooled_2pl_gamma_qwen_n24\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T19:17:53.487Z\", \"updated_at\": \"2026-05-16T19:18:36.187Z\", \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/exp006/results_pooled_irt_qwen_n24/\", \"log_path\": \"/root/autodl-tmp/exp006/results_pooled_irt_qwen_n24/run.log\", \"completed_at\": \"2026-05-16T19:18:21.760Z\", \"hypothesis\": \"2PL+γ pooled IRT with RRF exposure signal, Qwen-only N=16-24, fixes 4PL over-parameterization\", \"metrics\": {\"mmlu\": {\"N\": 16, \"items\": 300, \"gamma_mean\": 0.6551, \"gamma_ci\": [-0.4056, 1.7366], \"rhat\": 1.0069, \"ess\": 1453, \"ppp\": 0.192, \"raw_mae\": 0.0155, \"cal_mae\": 0.007, \"delta_mae\": 0.0085}, \"arc_challenge\": {\"N\": 16, \"items\": 300, \"gamma_mean\": 0.7269, \"gamma_ci\": [0.0207, 1.4433], \"rhat\": 1.0072, \"ess\": 1449, \"ppp\": 0.003, \"raw_mae\": 0.0338, \"cal_mae\": 0.0201, \"delta_mae\": 0.0136}, \"gsm8k\": {\"N\": 24, \"items\": 300, \"gamma_mean\": 0.0639, \"gamma_ci\": [-0.3636, 0.4902], \"rhat\": 1.0078, \"ess\": 1313, \"ppp\": 0.5413, \"raw_mae\": 0.1694, \"cal_mae\": 0.0062, \"delta_mae\": 0.1632}}, \"parent\": \"exp_006_pooled_irt_rrf_n25_v2\"}, \"exp_002_signals_llama32_3B_d000_gsm8k\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T18:27:49.970Z\", \"updated_at\": \"2026-05-16T19:12:08.440Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python compute_signals.py --model-path /root/autodl-tmp/exp001/checkpoints/Llama-3.2-3B_d000_s42/merged --benchmark gsm8k --signal all --output-dir /root/autodl-tmp/exp002/signals/Llama-3.2-3B_d000_s42/ --batch-size 8\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:2\", \"pid\": 835978, \"data_path\": \"gsm8k\", \"data_count\": 0, \"model_name\": \"Llama-3.2-3B_d000_s42\", \"seed\": 42, \"checkpoint_source\": \"exp_001_sft_llama32_3B_d000_s42\", \"eval_data\": \"gsm8k\", \"hypothesis\": \"Llama d000 GSM8K signals for cross-family RRF\"}, \"reproduce\": {\"finished_at\": \"2026-05-16T19:11:39.158Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-16T19:11:45.489Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T19:11:57.699412+00:00\"}]}, \"notes\": \"失败原因: HuggingFace Hub 连接超时 (sentence-transformers/all-MiniLM-L6-v2 下载失败) | 已有成果: 无 | 建议: 先缓存 all-MiniLM-L6-v2 模型到本地再重跑\"}, \"exp_001_sft_llama32_3B_d025_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T15:07:47.045Z\", \"updated_at\": \"2026-05-16T17:53:29.445Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration && CUDA_VISIBLE_DEVICES=3 python exp001/train_sft.py --model-name /root/autodl-tmp/models/LLM-Research/Llama-3___2-3B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_025.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Llama-3.2-3B_d025_s42 --seed 42 --batch-size 2 --grad-accum 8 --lr 5e-5 --gradient-checkpointing --merge --gpu 0\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:3\"], \"pid\": \"801761\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_llama32_3B_d025_s42.log\", \"submitted_at\": \"2026-05-16T15:07:46.476Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_025.jsonl\", \"data_count\": 54133, \"model_name\": \"Llama-3.2-3B\", \"seed\": 42, \"wall_clock_seconds\": 9853.2, \"gpu_hours\": 2.74}, \"reproduce\": {\"finished_at\": \"2026-05-16T17:29:35.930Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T17:29:43.333042+00:00\"}]}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Llama-3.2-3B_d025_s42/\", \"metrics\": {\"train_loss\": 1.5265, \"train_runtime_sec\": 8349.26, \"mean_token_accuracy\": 0.6755, \"train_samples_per_second\": 6.484, \"train_steps_per_second\": 0.405, \"epoch\": 1}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T17:51:59.647Z\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_llama32_3B_d025_s42.log\"}, \"exp_002_signals_15B_instruct_gsm8k\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T16:31:56.418Z\", \"updated_at\": \"2026-05-16T17:47:30.854Z\", \"spec\": {\"command\": \"python compute_signals.py --model_path /root/autodl-tmp/models/Qwen2.5-1.5B-Instruct --benchmark gsm8k --output_dir /root/autodl-tmp/exp002/signals_15B_instruct_gsm8k --gpu 0\", \"server\": \"cqa1-21977\", \"data_path\": \"gsm8k (1319 items)\", \"data_count\": 1319, \"model_name\": \"Qwen2.5-1.5B-Instruct\", \"seed\": 42, \"gpu\": \"cuda:2\", \"pid\": 815287, \"hypothesis\": \"1.5B-Instruct GSM8K signals for N expansion in pooled IRT\"}, \"reproduce\": {\"finished_at\": \"2026-05-16T17:47:26.886Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-16T17:47:30.854Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T17:47:38.855894+00:00\"}]}}, \"exp_006_pooled_irt_vanilla_2pl_n13\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T16:37:49.528Z\", \"updated_at\": \"2026-05-16T17:14:11.399Z\", \"spec\": {\"command\": \"python run_pooled_rrf_irt.py --model 2pl --benchmarks mmlu,arc,gsm8k\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/autodl-tmp/exp003/rrf_full_n_latest/exposure_scores.json\", \"data_count\": 13, \"model_name\": \"stan_vanilla_2pl\", \"seed\": 42, \"hypothesis\": \"Ablation: vanilla 2PL without gamma to show pooled-level gamma has no calibration benefit (Simpson's Paradox support)\", \"log_path\": \"/root/autodl-tmp/exp006/pooled_irt_vanilla_2pl_n16/\", \"checkpoint_path\": \"/root/autodl-tmp/exp006/pooled_irt_vanilla_2pl_n16/\"}, \"conclusion\": \"success\", \"metrics\": {\"MMLU\": {\"N\": 16, \"raw_MAE\": 0.0155, \"cal_MAE\": 0.0068, \"delta_MAE\": 0.0087, \"PPP\": 0.349}, \"ARC\": {\"N\": 16, \"raw_MAE\": 0.0338, \"cal_MAE\": 0.0158, \"delta_MAE\": 0.018, \"PPP\": 0.035}, \"GSM8K\": {\"N\": 24, \"raw_MAE\": 0.1694, \"cal_MAE\": 0.0063, \"delta_MAE\": 0.1631, \"PPP\": 0.691}, \"note\": \"Re-run with naming fix applied, now N=16 (was N=13 before fix). Confirms vanilla 2PL has lower calMAE on MMLU/ARC.\"}, \"completed_at\": \"2026-05-16T16:38:30.442Z\"}, \"exp_006_pooled_irt_2pl_gamma_n16\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T16:02:41.808Z\", \"updated_at\": \"2026-05-16T17:14:07.907Z\", \"spec\": {\"command\": \"python run_pooled_rrf_irt.py --model 2pl_gamma --benchmarks mmlu,arc,gsm8k\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/autodl-tmp/exp003/rrf_full_n_latest/exposure_scores.json\", \"data_count\": 16, \"model_name\": \"stan_2pl_gamma\", \"seed\": 42, \"log_path\": \"/root/autodl-tmp/exp006/pooled_irt_2pl_gamma_n16/\", \"checkpoint_path\": \"/root/autodl-tmp/exp006/pooled_irt_2pl_gamma_n16/\"}, \"conclusion\": \"success\", \"metrics\": {\"MMLU\": {\"N\": 16, \"gamma_hat\": 0.7, \"CI_excludes_zero\": false, \"PPP\": 0.193, \"cal_MAE\": 0.0072, \"delta_MAE\": 0.0083, \"R_hat_max\": 1.01}, \"ARC\": {\"N\": 16, \"gamma_hat\": 0.73, \"CI_excludes_zero\": true, \"PPP\": 0.003, \"cal_MAE\": 0.0201, \"delta_MAE\": 0.0136, \"R_hat_max\": 1.01}, \"GSM8K\": {\"N\": 24, \"gamma_hat\": 0.06, \"CI_excludes_zero\": false, \"PPP\": 0.541, \"cal_MAE\": 0.0062, \"delta_MAE\": 0.1632, \"R_hat_max\": 1.01}, \"note\": \"N=16 fixed (naming normalization applied), 0 divergences, ESS>1300\"}, \"completed_at\": \"2026-05-16T16:03:24.443Z\"}, \"exp006_pooled_irt_n16_fixed\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T17:12:22.909Z\", \"updated_at\": \"2026-05-16T17:12:55.073Z\", \"spec\": {\"description\": \"Pooled IRT N=16 rerun after fixing RRF/eval key mismatch\", \"models_run\": [\"vanilla_2pl\", \"2pl_gamma\"], \"benchmarks\": [\"mmlu\", \"arc_challenge\", \"gsm8k\"], \"server\": \"cqa1-21977\", \"command\": \"python3 run_pooled_rrf_irt.py --model-type vanilla_2pl/2pl_gamma\", \"data_path\": \"/root/autodl-tmp/exp003/rrf_full_n_latest/exposure_scores.json\", \"checkpoint_path\": \"/root/autodl-tmp/exp006/pooled_irt_vanilla_2pl_n16_fixed\", \"log_path\": \"/tmp/irt_vanilla_2pl.log\", \"data_count\": 16, \"model_name\": \"vanilla_2pl+2pl_gamma\", \"seed\": 42}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T17:12:55.073Z\"}, \"exp_001_eval_05B_instruct\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T14:42:17.521Z\", \"updated_at\": \"2026-05-16T16:32:10.317Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python3 /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/models/Qwen/Qwen2.5-0.5B-Instruct-hf --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B-Instruct/ --mc-format aligned --instruct --benchmarks mmlu gsm8k humaneval\", \"server\": \"cqa1-21977\", \"data_path\": \"mmlu+gsm8k+humaneval\", \"data_count\": 0, \"model_name\": \"Qwen2.5-0.5B-Instruct\", \"seed\": 42, \"eval_data\": \"mmlu gsm8k humaneval\", \"hypothesis\": \"0.5B-Instruct baseline eval (RL observational claim). Generation-based MCQ with chat template.\", \"log_path\": \"/root/autodl-tmp/exp001/eval_05B_instruct/\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_05B_instruct/\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T16:32:10.317Z\"}, \"exp_001_eval_llama32_3B_d000_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T13:22:13.996Z\", \"updated_at\": \"2026-05-16T15:36:02.236Z\", \"spec\": {\"hypothesis\": \"P0-B cross-family validation: Llama-3.2-3B d000 eval. 0% contamination baseline for Llama family. Verifies contamination susceptibility pattern across model families.\", \"parent\": \"exp_001_sft_llama32_3B_d000_s42\", \"type\": \"eval\", \"command\": \"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=4 python3 /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/exp001/checkpoints/Llama-3.2-3B_d000_s42/merged --output-dir /root/autodl-tmp/exp001/eval_results/Llama-3.2-3B_d000_s42_aligned --mc-format aligned --benchmarks mmlu gsm8k arc_challenge humaneval\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:4\", \"pid\": 796488, \"data_path\": \"/root/autodl-tmp/exp001/checkpoints/Llama-3.2-3B_d000_s42/merged\", \"data_count\": 14042, \"model_name\": \"Llama-3.2-3B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Llama-3.2-3B_d000_s42/merged\", \"eval_data\": \"mmlu+gsm8k+arc_challenge+humaneval\"}, \"conclusion\": \"killed\", \"failure_reason\": \"Director ordered kill: GSM8K hung at 57/1319 after subprocess terminated, main process unresponsive 50+ min. Fix worker restarting with per-benchmark save.\", \"completed_at\": \"2026-05-16T14:39:15.579Z\", \"metrics\": {\"MMLU\": 0.4545}}, \"exp_001_eval_15B_instruct\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T12:57:49.119Z\", \"updated_at\": \"2026-05-16T15:36:01.221Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python exp001/evaluate.py --model-path /root/autodl-tmp/models/Qwen/Qwen2___5-1___5B-Instruct --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B-Instruct_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache --gpu 0\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:5\", \"pid\": \"782625\", \"data_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B-Instruct_aligned\", \"data_count\": 0, \"model_name\": \"Qwen2.5-1.5B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"pretrained (Qwen/Qwen2.5-1.5B-Instruct via ModelScope)\", \"eval_data\": \"mmlu gsm8k arc_challenge humaneval (aligned + para_aligned)\", \"log_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B-Instruct_aligned/eval_results.json\", \"checkpoint_path\": \"/root/autodl-tmp/models/Qwen/Qwen2___5-1___5B-Instruct\"}, \"reproduce\": {\"finished_at\": \"2026-05-16T15:17:51.770Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T15:17:54.464Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T15:18:01.160256+00:00\"}]}, \"metrics\": {\"MMLU\": 0.5775, \"GSM8K\": 0.5929, \"ARC\": 0.7654}}, \"exp_006_mmlu_domain_gamma_n24_v4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T13:51:12.494Z\", \"updated_at\": \"2026-05-16T15:02:32.927Z\", \"spec\": {\"hypothesis\": \"D108 v4: rerun 4 MMLU domains with correct N=24 script\", \"plan_id\": \"D108\", \"type\": \"analysis\", \"parent\": \"exp_006_mmlu_domain_gamma_n24\", \"model_name\": \"2PL+gamma (Stan)\", \"seed\": \"Stan default (4 chains)\", \"data_path\": \"/root/autodl-tmp/exp003/rrf_all_scales/exposure_scores.json\", \"data_count\": \"24 respondents x 4 MMLU domains\", \"command\": \"python run_mmlu_domain_gamma_n24.py --domains Humanities Social_Sciences Business_Law Other --output-dir /root/autodl-tmp/exp006/results_mmlu_domain_gamma_n24/\", \"server\": \"cqa1-21977\", \"gpu\": \"CPU\", \"pid\": 789935, \"output_path\": \"/root/autodl-tmp/exp006/results_mmlu_domain_gamma_n24/\", \"log_path\": \"/root/contamcal-irt-calibration/exp006/domain_gamma_n24_v4.log\", \"checkpoint_source\": \"N/A (IRT analysis, no checkpoint)\", \"eval_data\": \"MMLU domain items (Humanities, Social_Sciences, Business_Law, Other)\", \"checkpoint_path\": \"/root/contamcal-irt-calibration/exp006/domain_gamma_n24_v4/\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T15:02:02.519Z\", \"metrics\": {\"domains\": 7, \"STEM_Math_gamma\": \"positive_significant\", \"STEM_Science_gamma\": \"positive_significant\", \"Medical_gamma\": \"negative_significant\", \"Humanities_gamma\": \"negative_significant\", \"Social_Sciences_gamma\": \"negative_significant\", \"CS_Eng_gamma\": \"not_significant\", \"Business_Law_gamma\": \"not_significant\", \"note\": \"CmdStan crashed after results saved. Humanities rhat=1.014 not converged.\"}}, \"exp_006_pooled_irt_rrf_n25_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T14:36:11.037Z\", \"updated_at\": \"2026-05-16T15:02:31.098Z\", \"spec\": {\"command\": \"python3 /root/contamcal-irt-calibration/exp006/run_pooled_rrf_irt.py --exposure-file /root/autodl-tmp/exp003/rrf_full_n_latest/exposure_scores.json --output-dir /root/autodl-tmp/exp006/pooled_irt_rrf_n25_v2 --model-type 4pl_gamma --benchmarks mmlu gsm8k arc_challenge --chains 4 --warmup 1000 --samples 1000\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/autodl-tmp/exp003/rrf_full_n_latest/exposure_scores.json\", \"data_count\": 25, \"model_name\": \"4pl_gamma_pooled\", \"seed\": 42, \"checkpoint_path\": \"/root/contamcal-irt-calibration/exp006/pooled_irt_rrf_n25_v2/\", \"log_path\": \"/root/contamcal-irt-calibration/exp006/pooled_irt_rrf_n25_v2.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T15:02:08.237Z\", \"metrics\": {\"gsm8k_N16_delta_mae\": 0.118, \"gsm8k_calibration\": \"effective\", \"mmlu_N8_4PLgamma\": \"over_parameterized_cal_worsens\", \"arc_N8_4PLgamma\": \"over_parameterized_cal_worsens\", \"note\": \"GSM8K N=16 works. MMLU/ARC N=8 with 4PL+gamma over-parameterized, PPP=0.006/0.000, cal_mae > raw_mae. Need 2PL+gamma or N>=16.\"}}, \"exp_003_rrf_full_n25_latest\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T14:35:17.463Z\", \"updated_at\": \"2026-05-16T14:35:52.664Z\", \"conclusion\": \"success\", \"spec\": {\"command\": \"python3 /root/contamcal-irt-calibration/exp003/rrf_aggregation.py --signal-root /root/autodl-tmp/exp002/signals --output-dir /root/autodl-tmp/exp003/rrf_full_n_latest --generate-exposure --csv\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/autodl-tmp/exp002/signals\", \"data_count\": 25, \"model_name\": \"all_scales_25_models\", \"seed\": 42}, \"checkpoint_path\": \"/root/autodl-tmp/exp003/rrf_full_n_latest/exposure_scores.json\", \"log_path\": \"/root/autodl-tmp/exp003/rrf_full_n_latest/\", \"completed_at\": \"2026-05-16T14:35:52.664Z\"}, \"signals_05B_s123_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T11:01:32.305Z\", \"updated_at\": \"2026-05-16T14:29:42.698Z\", \"spec\": {\"command\": \"bash /root/contamcal-irt-calibration/exp002/run_signals_05B_s123_remaining.sh\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:1\"], \"pid\": \"760236\", \"log_path\": \"~/runs/contamcal-irt-calibration/signals_05B_s123_v2.log\", \"submitted_at\": \"2026-05-16T11:01:31.665Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s123\", \"data_count\": 4, \"model_name\": \"Qwen2.5-0.5B\", \"seed\": 123, \"wall_clock_seconds\": 12491.0, \"gpu_hours\": 3.47}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_s123/\", \"completed_at\": \"2026-05-16T14:29:42.698Z\"}, \"exp_006_pooled_irt_n25\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T13:21:30.396Z\", \"updated_at\": \"2026-05-16T14:29:29.467Z\", \"spec\": {\"hypothesis\": \"Pooled IRT 2PL+gamma with N=25 respondents (full s42+s123 pool). Expect stronger gamma CI exclusion and improved PPP vs N=23.\", \"type\": \"analysis\", \"command\": \"python run_irt_calibration.py --exposure-file /root/autodl-tmp/exp003/rrf_n20_all/exposure_scores.json --model 2pl_gamma --chains 4 --warmup 1000 --samples 1000 --adapt-delta 0.95 --output-dir /root/autodl-tmp/exp006/results_pooled_n20/\", \"server\": \"cqa1-21977\", \"pid\": 785832, \"gpu\": \"CPU\", \"data_path\": \"/root/autodl-tmp/exp003/rrf_n20_all/exposure_scores.json\", \"data_count\": \"N=25 respondents (MMLU N=13 after D045 exclusion)\", \"model_name\": \"2PL+gamma (Stan)\", \"seed\": \"Stan default (4 chains)\", \"output_path\": \"/root/autodl-tmp/exp006/results_pooled_n20/\"}, \"reproduce\": {\"finished_at\": \"2026-05-16T13:42:52.805Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T13:42:55.740Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T13:42:59.328062+00:00\"}]}}, \"exp_001_eval_3B_instruct_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T11:16:34.089Z\", \"updated_at\": \"2026-05-16T14:29:28.489Z\", \"spec\": {\"command\": \"bash /root/contamcal-irt-calibration/scripts/run_instruct_3b_eval_v2.sh\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:3\"], \"pid\": \"764449\", \"data_path\": \"/root/autodl-tmp/exp001/eval_results/\", \"data_count\": 8, \"model_name\": \"Qwen/Qwen2.5-3B-Instruct\", \"seed\": null, \"checkpoint_source\": \"huggingface\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval (aligned + para_aligned, --instruct mode)\", \"hypothesis\": \"Re-run 3B-Instruct eval with fixed methodology: generation-based MCQ with system prompt for answer-only output (max_new_tokens=5), markdown code extraction for HumanEval. Chat template + system message constrains instruct model to output just answer letter. Expected: MMLU ~65%, HumanEval >0%.\"}, \"reproduce\": {\"finished_at\": \"2026-05-16T13:48:50.854Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T13:48:53.559Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T13:49:00.289973+00:00\"}]}, \"metrics\": {\"MMLU\": 0.605, \"GSM8K\": 0.76, \"HumanEval\": 0.5}}, \"exp_006_mmlu_domain_gamma_n24_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T13:12:59.287Z\", \"updated_at\": \"2026-05-16T13:50:52.887Z\", \"spec\": {\"hypothesis\": \"D108 v3: remaining 4 MMLU domains (Humanities, Social_Sciences, Business_Law, Other). 2PL+gamma N=23.\", \"plan_id\": \"D108\", \"type\": \"analysis\", \"parent\": \"exp_006_mmlu_domain_gamma_n24\", \"command\": \"python run_mmlu_domain_gamma_n24.py --domains Humanities Social_Sciences Business_Law Other\", \"server\": \"cqa1-21977\", \"pid\": 781756, \"gpu\": \"CPU\", \"data_path\": \"/root/autodl-tmp/exp003/rrf_all_scales/exposure_scores.json\", \"data_count\": \"23 respondents x 4 MMLU domains\", \"model_name\": \"2PL+gamma (Stan)\", \"seed\": \"Stan default (4 chains)\", \"output_path\": \"/root/autodl-tmp/exp006/results_mmlu_domain_gamma_n24/\", \"log_path\": \"/root/autodl-tmp/exp006/mmlu_domain_gamma_n24_v2.log\"}, \"conclusion\": \"failed\", \"metrics\": {\"completed_domains\": 5, \"total_domains\": 8, \"crashed\": \"Social_Sciences (CmdStan retcode=[1,0,0,1])\", \"not_run\": [\"Business_Law\", \"Other\"], \"STEM_Math\": {\"gamma_mean\": 0.969, \"CI\": [0.527, 1.43], \"excludes_zero\": true, \"PPP\": 0.438, \"N\": 23, \"converged\": true}, \"STEM_Science\": {\"gamma_mean\": 0.838, \"CI\": [0.385, 1.274], \"excludes_zero\": true, \"PPP\": 0.807, \"N\": 23, \"converged\": true}, \"STEM_CS_Eng\": {\"gamma_mean\": 0.197, \"CI\": [-0.448, 0.835], \"excludes_zero\": false, \"PPP\": 0.892, \"N\": 23, \"converged\": true}, \"Medical\": {\"gamma_mean\": -0.199, \"CI\": [-0.338, -0.06], \"excludes_zero\": true, \"PPP\": 1, \"N\": 24, \"converged\": true}, \"Humanities\": {\"gamma_mean\": -0.407, \"CI\": [-0.776, -0.041], \"excludes_zero\": true, \"PPP\": 1, \"N\": 21, \"converged\": \"borderline_rhat_1.014\"}}, \"reproduce\": {\"finished_at\": \"2026-05-16T13:35:33.796Z\"}, \"failure_reason\": \"wrong script: used run_mmlu_domain_gamma.py (N=16) instead of run_mmlu_domain_gamma_n24.py\", \"completed_at\": \"2026-05-16T13:35:36.720Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T13:35:40.239746+00:00\"}]}}, \"exp_002_signals_15B_d100_s123_cuda2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T10:07:31.281Z\", \"updated_at\": \"2026-05-16T13:12:48.641Z\", \"spec\": {\"command\": \"bash run_15B_d100_s123_cuda2.sh (CUDA_VISIBLE_DEVICES=2, 3 benchmarks × 3 signals)\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:2\", \"pid\": \"746777\", \"data_path\": \"/root/autodl-tmp/exp002/signals/Qwen2.5-1.5B_d100_s123/\", \"data_count\": 9, \"model_name\": \"Qwen2.5-1.5B_d100_s123\", \"seed\": 123, \"hypothesis\": \"1.5B d100 s123 signals (s1_embedding + s2_minkpp + s4_selfcritique × mmlu + gsm8k + arc_challenge). Last missing 1.5B s123 dosage. Completes 1.5B s123 signal series.\", \"log_path\": \"/root/contamcal-irt-calibration/exp002/run_15B_d100_s123_cuda2.log\", \"checkpoint_path\": \"/root/autodl-tmp/exp002/signals/Qwen2.5-1.5B_d100_s123/\"}, \"reproduce\": {\"finished_at\": \"2026-05-16T12:44:17.125Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed by reconcile_crons\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T12:44:19.875Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T12:44:25.652030+00:00\"}]}}, \"exp_002_signals_15B_s123_batch\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T03:44:39.543Z\", \"updated_at\": \"2026-05-16T13:12:47.455Z\", \"spec\": {\"command\": \"bash run_15B_s123_signals.sh\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:0\"], \"pid\": \"691872\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_002_signals_15B_s123_batch.log\", \"submitted_at\": \"2026-05-16T03:44:35.931Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/exp002/signals/Qwen2.5-1.5B_*_s123\", \"data_count\": 12, \"model_name\": \"Qwen2.5-1.5B\", \"seed\": 123, \"wall_clock_seconds\": 32352.4, \"gpu_hours\": 8.99}, \"reproduce\": {\"finished_at\": \"2026-05-16T12:43:49.431Z\"}, \"failure_reason\": \"ModuleNotFoundError(\\\"No module named 'faiss.swigfaiss_avx512_spr'\\\")\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T12:43:48.348Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T12:44:01.753553+00:00\"}]}}, \"exp_006_mmlu_domain_gamma_n24\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T11:49:54.108Z\", \"updated_at\": \"2026-05-16T13:11:38.602Z\", \"spec\": {\"command\": \"python run_mmlu_domain_gamma.py --n_respondents 23 --model 2pl_gamma --chains 4 --warmup 1000 --samples 1000 --adapt_delta 0.95 --output_dir /root/autodl-tmp/exp006/results_mmlu_domain_gamma_n24/\", \"server\": \"A6000\", \"data_path\": \"/root/autodl-tmp/exp003/rrf_all_scales/exposure_scores.json + /root/autodl-tmp/exp006/respondent_profiles_3B.json\", \"data_count\": \"23 respondents x 8 MMLU domains\", \"model_name\": \"2PL+gamma (Stan)\", \"seed\": \"Stan default (4 chains)\", \"pid\": 768342, \"gpu\": \"CPU\", \"output_path\": \"/root/autodl-tmp/exp006/results_mmlu_domain_gamma_n24/\"}, \"failure_reason\": \"Partial: 3/8 domains completed (STEM_Math, STEM_Science, STEM_CS_Eng). Process stopped, remaining 4 domains restarted as v3. Cron误判(server字段错误).\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T12:06:23.779Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T12:06:26.949925+00:00\"}]}, \"metrics\": {\"domains_completed\": 3, \"domains_total\": 8, \"STEM_Math\": {\"PPP\": 0.438, \"gamma_mean\": 0.969, \"gamma_excludes_zero\": true, \"N_models\": 23, \"N_items\": 1190, \"fit_time_s\": 527}, \"STEM_Science\": {\"PPP\": 0.807, \"gamma_mean\": 0.838, \"gamma_excludes_zero\": true, \"N_models\": 23, \"N_items\": 1397, \"fit_time_s\": 618}, \"STEM_CS_Eng\": {\"PPP\": 0.892, \"gamma_mean\": 0.197, \"gamma_excludes_zero\": false, \"N_models\": 23, \"N_items\": 557, \"fit_time_s\": 153}, \"note\": \"3/8 domains complete. Process stopped after 3 — remaining 5 need restart.\"}}, \"exp_006_mmlu_domain_gamma_n24_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T12:28:48.496Z\", \"updated_at\": \"2026-05-16T13:11:28.954Z\", \"spec\": {\"hypothesis\": \"D108 continuation: original process PID 766829 running all 8 MMLU domains. 3 already done (STEM_Math/Science/CS_Eng), currently on Medical. Will complete all 8 with overwrite.\", \"plan_id\": \"D108\", \"type\": \"analysis\", \"parent\": \"exp_006_mmlu_domain_gamma_n24\", \"command\": \"python run_mmlu_domain_gamma.py (original PID 766829, all 8 domains)\", \"server\": \"cqa1-21977\", \"pid\": 766829, \"gpu\": \"CPU\", \"data_path\": \"/root/autodl-tmp/exp003/rrf_all_scales/exposure_scores.json\", \"data_count\": \"23 respondents x 8 MMLU domains\", \"model_name\": \"2PL+gamma (Stan)\", \"seed\": \"Stan default (4 chains)\", \"output_path\": \"/root/autodl-tmp/exp006/results_mmlu_domain_gamma_n24/\"}, \"reproduce\": {\"finished_at\": \"2026-05-16T12:44:33.006Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed by reconcile_crons\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-16T12:44:35.734Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T12:44:39.182565+00:00\"}]}}, \"exp_001_sft_llama32_3B_d000_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T10:34:27.989Z\", \"updated_at\": \"2026-05-16T12:56:14.562Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python train_sft.py --model-name Llama-3.2-3B --data-path sft_dosage_000.jsonl --lora-r 16 --lora-alpha 32 --lr 5e-5 --batch-size 2 --grad-accum 8 --epochs 1 --gradient-checkpointing --merge\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:4\", \"pid\": \"752961\", \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl\", \"data_count\": 50000, \"model_name\": \"Llama-3.2-3B (ModelScope LLM-Research/Llama-3.2-3B)\", \"seed\": 42, \"hypothesis\": \"P0-B cross-family validation: Llama-3.2-3B d000 (0% contamination baseline) SFT. Verifies contamination susceptibility is benchmark property not model-family artifact. Config mirrors Qwen2.5-3B d000 (lr=5e-5, alpha=32, rank=16).\", \"log_path\": \"/tmp/llama3b_d000_s42.log\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Llama-3.2-3B_d000_s42/\"}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Llama-3.2-3B_d000_s42/\", \"log_path\": \"/tmp/llama3b_d000_s42.log\", \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 1.5165, \"train_runtime_sec\": 8170, \"mean_token_accuracy\": 0.6685, \"epoch\": 1}, \"completed_at\": \"2026-05-16T12:56:14.562Z\"}, \"exp_002_signals_05B_s123_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T03:03:30.869Z\", \"updated_at\": \"2026-05-16T12:31:01.649Z\", \"spec\": {\"hypothesis\": \"0.5B d000 s123 signals computation. D099/D101 priority for IRT pool N expansion.\", \"model_name\": \"Qwen2.5-0.5B\", \"seed\": 123, \"server\": \"cqa1-21977\", \"gpu\": \"cuda:5\", \"data_path\": \"/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d000_s123\", \"data_count\": 1, \"command\": \"compute_signals.py 0.5B d000_s123 mmlu signals (s1+s2+s4)\", \"log_path\": \"/root/autodl-tmp/exp002/signals/signals_05B_s123_v2.log\", \"tmux_session\": \"exp002_05B_s123_v2\"}, \"reproduce\": {\"finished_at\": \"2026-05-16T12:25:47.145Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T12:25:49.852Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T12:25:53.223289+00:00\"}]}}, \"exp_001_sft_3B_d100_s123_a32\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:10:37.632Z\", \"updated_at\": \"2026-05-16T11:29:48.114Z\", \"spec\": {\"model_name\": \"Qwen/Qwen2.5-3B\", \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl\", \"data_count\": 50000, \"seed\": 123, \"lora_r\": 16, \"lora_alpha\": 32, \"lr\": \"5e-5\", \"batch_size\": 1, \"grad_accum\": 16, \"note\": \"D055 alpha=32 rerun, d100 s123. Priority 2, submit after d100_s42 or d025_s42 completes.\"}, \"hypothesis\": \"3B d100 s123 alpha=32 SFT. D055 rerun: previous exp_001_sft_3B_d100_s123 used alpha=16. 100% contamination with seed=123 for cross-seed consistency. Priority 2: submit after d100_s42 or d025_s42 completes.\", \"parent\": \"exp_001_sft_3B_d100_s123\", \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_a32_s123/\", \"log_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_a32_s123/\", \"completed_at\": \"2026-05-16T11:29:48.115Z\"}, \"exp_002_signals_3B_d100_a32_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T07:29:33.942Z\", \"updated_at\": \"2026-05-16T11:16:32.111Z\", \"spec\": {\"command\": \"bash /root/contamcal-irt-calibration/exp002/run_signals_3B_d100_a32_s42.sh\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:1\", \"pid\": \"724022\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_002_signals_3B_d100_a32_s42.log\", \"submitted_at\": \"2026-05-16T07:29:33.473Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl\", \"data_count\": 9, \"model_name\": \"Qwen2.5-3B_d100_a32_s42_v3\", \"seed\": 42, \"hypothesis\": \"3B d100 s42 alpha=32 signals. Completes 3B s42 RRF coverage (last missing dosage). Uses D076-retrained checkpoint.\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_a32_s42_v3/lora_adapter\", \"output_dir\": \"/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d100_a32_s42\", \"benchmarks\": [\"mmlu\", \"gsm8k\", \"arc_challenge\"], \"signals\": [\"s1_embedding\", \"s2_minkpp\", \"s4_selfcritique\"], \"wall_clock_seconds\": 13618.6, \"gpu_hours\": 3.78}, \"reproduce\": {\"finished_at\": \"2026-05-16T10:47:29.308Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T10:47:34.351667+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"benchmarks_completed\": [\"mmlu\", \"gsm8k\", \"arc_challenge\"], \"signals_generated\": [\"s1_embedding\", \"s2_minkpp\", \"s4_selfcritique\"], \"status_note\": \"Signals validated via pooled IRT (exp_006_pooled_irt_all_scales, N=23 success). Analysis worker completed 2026-05-16T10:50:52 but callback not processed due to session reset.\"}, \"completed_at\": \"2026-05-16T11:16:32.112Z\"}, \"exp_006_pooled_irt_all_scales\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T11:01:03.057Z\", \"updated_at\": \"2026-05-16T11:01:48.418Z\", \"conclusion\": \"success\", \"spec\": {\"command\": \"python3 run_pooled_rrf_irt.py --scales 0.5B 1.5B 3B --benchmarks mmlu gsm8k arc_challenge --model-type 2pl_gamma --exposure-file rrf_all_scales/exposure_scores.json\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/autodl-tmp/exp003/rrf_all_scales/exposure_scores.json\", \"data_count\": 23, \"model_name\": \"2pl_gamma_irt (0.5B+1.5B+3B)\", \"seed\": 42, \"hypothesis\": \"Full 3-scale pooled IRT (2PL+gamma) with RRF signal-based exposure. 23 respondents across 0.5B+1.5B+3B, D045 exclusion. Per C008: 2PL+gamma for all benchmarks.\", \"checkpoint_path\": \"/root/autodl-tmp/exp006/pooled_irt_all_scales/\", \"log_path\": \"/tmp/pooled_irt_all_scales.log\"}, \"completed_at\": \"2026-05-16T11:01:26.706Z\", \"metrics\": {\"mmlu\": {\"n_models\": 15, \"n_items\": 300, \"gamma_mean\": 0.5172, \"gamma_ci95\": [-0.5501, 1.5974], \"rhat\": 1.0067, \"ess\": 1402, \"divergences\": 0, \"ppp\": 0.2335, \"raw_mae\": 0.0157, \"cal_mae\": 0.0059, \"delta_mae\": 0.0098}, \"gsm8k\": {\"n_models\": 20, \"n_items\": 300, \"gamma_mean\": 0.1721, \"gamma_ci95\": [-0.2889, 0.637], \"rhat\": 1.0071, \"ess\": 1388, \"divergences\": 0, \"ppp\": 0.3425, \"raw_mae\": 0.163, \"cal_mae\": 0.0078, \"delta_mae\": 0.1552}, \"arc_challenge\": {\"n_models\": 13, \"n_items\": 300, \"gamma_mean\": 0.4859, \"gamma_ci95\": [-0.2552, 1.2529], \"rhat\": 1.0065, \"ess\": 1670, \"divergences\": 0, \"ppp\": 0.027, \"raw_mae\": 0.0335, \"cal_mae\": 0.0153, \"delta_mae\": 0.0183}, \"rrf_respondents\": 23, \"scales\": [\"0.5B\", \"1.5B\", \"3B\"], \"model_type\": \"2pl_gamma\", \"exposure\": \"rrf_signal\"}, \"conclusion_notes\": \"2/3 benchmarks pass success criteria (PPP∈[0.1,0.9] + cal_MAE&lt;raw_MAE). MMLU: PPP=0.234✓, ΔMAE=+0.010. GSM8K: PPP=0.343✓, ΔMAE=+0.155. ARC: PPP=0.027✗ (below 0.1 threshold), ΔMAE=+0.018. vs prior 0.5B+1.5B: ARC dramatically improved (PPP 0→0.027, ΔMAE -0.064→+0.018), GSM8K calibration strengthened (ΔMAE 0.113→0.155). All convergence metrics excellent (R̂<1.01, ESS>1300, 0 divergences). γ̂ CI includes 0 for all benchmarks — more data needed for statistical significance. Fixed eval/signal dir naming mismatch (d000_s42_a32 vs d000_a32_s42) via exposure JSON aliases.\"}, \"exp_001_eval_3B_instruct_aligned_para\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T07:54:58.792Z\", \"updated_at\": \"2026-05-16T10:35:04.466Z\", \"spec\": {\"command\": \"bash /root/contamcal-irt-calibration/scripts/run_instruct_3b_eval.sh\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:3\"], \"pid\": \"730671\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_instruct_aligned_para.log\", \"submitted_at\": \"2026-05-16T07:54:58.299Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/exp001/paraphrases/\", \"data_count\": 0, \"model_name\": \"Qwen/Qwen2.5-3B-Instruct\", \"seed\": null, \"checkpoint_source\": \"huggingface\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval (aligned + para_aligned)\", \"wall_clock_seconds\": 9606.2, \"gpu_hours\": 2.67}, \"hypothesis\": \"Qwen2.5-3B-Instruct (RL post-trained) eval. P0-C RL observational: verify signal patterns after RLHF. No training, inference only. Aligned + para_aligned on 4 benchmarks.\", \"reproduce\": {\"finished_at\": \"2026-05-16T10:28:45.392Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T10:28:49.480069+00:00\"}]}, \"conclusion\": \"failed\", \"failure_reason\": \"Missing chat template: Instruct model evaluated as base model (raw completion instead of chat format). MMLU 0.509 vs expected 0.65-0.68, HumanEval 0.000 vs expected 0.50+. Results invalid, need re-run with apply_chat_template(). Fix in progress.\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B-Instruct_aligned/\", \"completed_at\": \"2026-05-16T10:35:04.466Z\"}, \"exp_002_signals_3B_d000_a32_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T07:09:17.976Z\", \"updated_at\": \"2026-05-16T10:23:58.349Z\", \"spec\": {\"command\": \"bash /root/contamcal-irt-calibration/exp002/run_3B_d000_a32_s42_signals.sh\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:4\", \"pid\": \"721519\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_002_signals_3B_d000_a32_s42.log\", \"submitted_at\": \"2026-05-16T07:09:17.497Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d000_a32_s42\", \"model_name\": \"Qwen2.5-3B_d000_s42 (alpha=32)\", \"seed\": 42, \"hypothesis\": \"Compute contamination signals (s1_embedding, s2_minkpp, s4_selfcritique) for d000 baseline across mmlu/gsm8k/arc_challenge for RRF aggregation\", \"data_count\": 9, \"wall_clock_seconds\": 11680.9, \"gpu_hours\": 3.24}, \"reproduce\": {\"finished_at\": \"2026-05-16T10:20:56.973Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T10:21:02.285991+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d000_a32_s42/\", \"log_path\": \"/root/runs/contamcal-irt-calibration/exp_002_signals_3B_d000_a32_s42.log\", \"metrics\": {\"signals_completed\": 9, \"signals_failed\": 0, \"runtime_minutes\": 189, \"benchmarks\": {\"mmlu\": {\"n_items\": 14042, \"signals\": [\"s1_embedding\", \"s2_minkpp\", \"s4_selfcritique\"]}, \"gsm8k\": {\"n_items\": 1319, \"signals\": [\"s1_embedding\", \"s2_minkpp\", \"s4_selfcritique\"]}, \"arc_challenge\": {\"n_items\": 1172, \"signals\": [\"s1_embedding\", \"s2_minkpp\", \"s4_selfcritique\"]}}, \"output_files\": {\"signal_s1_embedding_mmlu.json\": \"7.6M\", \"signal_s1_embedding_gsm8k.json\": \"717K\", \"signal_s1_embedding_arc_challenge.json\": \"650K\", \"signal_s2_minkpp_mmlu.json\": \"2.8M\", \"signal_s2_minkpp_gsm8k.json\": \"266K\", \"signal_s2_minkpp_arc_challenge.json\": \"245K\", \"signal_s4_selfcritique_mmlu.json\": \"3.2M\", \"signal_s4_selfcritique_gsm8k.json\": \"310K\", \"signal_s4_selfcritique_arc_challenge.json\": \"284K\"}}, \"completed_at\": \"2026-05-16T10:23:58.349Z\"}, \"exp_002_signals_3B_d005_a32_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T06:51:39.086Z\", \"updated_at\": \"2026-05-16T10:11:52.002Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python compute_signals.py --signal all --benchmark {mmlu,gsm8k,arc_challenge}\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:2\", \"gpu_id\": \"cuda:2\", \"model_name\": \"Qwen2.5-3B\", \"seed\": 42, \"data_path\": \"/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d005_a32_s42\", \"data_count\": 12, \"hypothesis\": \"3B d005 s42 alpha=32 signals (s1_embedding + s2_minkpp + s3 + s4_selfcritique) x (mmlu + gsm8k + arc_challenge). Prerequisite for RRF aggregation. Uses D076-retrained checkpoint.\", \"pid\": 719534, \"log_path\": \"/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d005_a32_s42/run.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-16T10:09:15.071Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T10:09:17.583Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T10:09:20.769563+00:00\"}]}, \"notes\": \"Cron false positive: signals pipeline不用W&B, cron检测不到metrics误判为failed. 实际已全部完成: s1+s2+s4 × mmlu+gsm8k+arc_challenge, 输出merged json在 /root/autodl-tmp/exp002/signals/Qwen2.5-3B_d005_a32_s42/. GPU cuda:2 已释放.\"}, \"exp_006_pooled_irt_05b_15b\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T09:10:10.904Z\", \"updated_at\": \"2026-05-16T09:16:12.488Z\", \"spec\": {\"command\": \"run_pooled_4bench_irt.py per-benchmark (gsm8k N=11, arc N=5) with RRF exposure\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/autodl-tmp/exp006/pooled_irt_05b_15b/\", \"data_count\": 2, \"model_name\": \"Qwen2.5-0.5B+1.5B\", \"seed\": \"42,123\", \"hypothesis\": \"Pipeline validation: 0.5B+1.5B pooled IRT with RRF signal-based exposure. N=13 (GSM8K 11, ARC 5 per D045). Items subsampled to 300.\", \"checkpoint_path\": \"/root/autodl-tmp/exp006/pooled_irt_05b_15b/\", \"log_path\": \"/root/autodl-tmp/exp006/pooled_irt_05b_15b/\"}, \"conclusion\": \"success\", \"metrics\": {\"gsm8k_gamma\": 0.0128, \"gsm8k_ci95\": \"[-0.990, 1.019]\", \"gsm8k_rhat\": 1.0072, \"gsm8k_ess\": 1300, \"gsm8k_ppp\": 0.663, \"gsm8k_raw_mae\": 0.1501, \"gsm8k_cal_mae\": 0.0373, \"gsm8k_delta_mae\": 0.1128, \"gsm8k_n_models\": 11, \"arc_gamma\": 1.2259, \"arc_ci95\": \"[-0.271, 2.857]\", \"arc_rhat\": 1.0072, \"arc_ess\": 1480, \"arc_ppp\": 0, \"arc_raw_mae\": 0.0042, \"arc_cal_mae\": 0.0682, \"arc_delta_mae\": -0.064, \"arc_n_models\": 5, \"n_items_subsampled\": 300}, \"completed_at\": \"2026-05-16T09:16:12.488Z\"}, \"exp006_pooled_rrf_irt_05b_15b\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T09:02:32.472Z\", \"updated_at\": \"2026-05-16T09:08:42.567Z\", \"spec\": {\"command\": \"python3 run_pooled_rrf_irt.py --scales 0.5B 1.5B --benchmarks gsm8k arc_challenge --model-type 4pl_gamma\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:0\"], \"pid\": \"738279\", \"log_path\": \"/root/runs/contamcal-irt-calibration/exp006_pooled_rrf_irt_05b_15b_v2.log\", \"submitted_at\": \"2026-05-16T09:02:31.986Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/exp003/rrf_05B_15B/exposure_scores.json\", \"data_count\": 13, \"model_name\": \"4pl_gamma_irt\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/exp006/pooled_irt_rrf_05b_15b\", \"wall_clock_seconds\": 358.8, \"gpu_hours\": 0.1}, \"hypothesis\": \"0.5B+1.5B pooled 4PL+γ IRT fitting with RRF signal-based exposure. Per-benchmark: GSM8K (N=11, 0.5B+1.5B) and ARC (N=5, 1.5B only per D045). Pipeline validation for γ̂ estimates before N≥16 final run.\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T09:08:30.795Z\", \"metrics\": {\"gsm8k\": {\"n_models\": 11, \"n_items\": 300, \"gamma_mean\": 0.0128, \"gamma_ci95\": [-0.99, 1.0187], \"rhat\": 1.0072, \"ess\": 1300, \"divergences\": 0, \"ppp\": 0.663, \"raw_mae\": 0.1501, \"cal_mae\": 0.0373, \"delta_mae\": 0.1128}, \"arc_challenge\": {\"n_models\": 5, \"n_items\": 300, \"gamma_mean\": 1.2259, \"gamma_ci95\": [-0.2711, 2.8571], \"rhat\": 1.0072, \"ess\": 1480, \"divergences\": 0, \"ppp\": 0, \"raw_mae\": 0.0042, \"cal_mae\": 0.0682, \"delta_mae\": -0.064}}}, \"exp006_pooled_rrf_irt_05b_15b_v2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-16T09:05:27.235Z\", \"updated_at\": \"2026-05-16T09:05:27.235Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration/exp006 && python3 run_pooled_rrf_irt.py \\\\\\n  --eval-dir /root/autodl-tmp/exp001/eval_results \\\\\\n  --scales 0.5B 1.5B \\\\\\n  --benchmarks gsm8k arc_challenge \\\\\\n  --exposure-file /root/autodl-tmp/exp003/rrf_05B_15B/exposure_scores.json \\\\\\n  --output-dir /root/autodl-tmp/exp006/pooled_irt_rrf_05b_15b \\\\\\n  --model-type 4pl_gamma \\\\\\n  --chains 4 --warmup 1000 --samples 1000 --adapt-delta 0.95 \\\\\\n  --max-treedepth 12 --seed 42 --parallel-chains 4\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:0\"], \"pid\": \"738759\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp006_pooled_rrf_irt_05b_15b_v2.log\", \"submitted_at\": \"2026-05-16T09:05:26.391Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}}, \"exp_006_mmlu_domain_gamma\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T07:53:25.491Z\", \"updated_at\": \"2026-05-16T08:55:20.713Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration && python3 exp006/run_mmlu_domain_gamma.py --include-para 2>&1 | tee /root/autodl-tmp/contamcal-irt-calibration/exp_006_mmlu_domain_gamma.log\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [], \"pid\": \"731055\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_006_mmlu_domain_gamma.log\", \"submitted_at\": \"2026-05-16T07:57:17.669Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 2993.2, \"gpu_hours\": 0.0}, \"reproduce\": {\"finished_at\": \"2026-05-16T08:47:06.694Z\"}, \"failure_reason\": \"RESOLVED: tee target path /root/autodl-tmp/contamcal-irt-calibration/ did not exist, causing tee exit code 1. Python script completed successfully. All 8 domains converged (R̂≤1.008, 0 divergent).\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T08:47:10.890Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T08:47:16.530888+00:00\"}]}, \"metrics\": {\"Other_gamma\": 1.34, \"Business_Law_gamma\": 0.61, \"Humanities_gamma\": 0.47, \"STEM_Science_gamma\": 0.36, \"STEM_CS_Eng_gamma\": 0.29, \"Social_Sciences_gamma\": 0.28, \"Medical_gamma\": 0.27, \"STEM_Math_gamma\": -0.55, \"all_rhat_max\": 1.008, \"divergent_transitions\": 0, \"n_domains\": 8, \"n_models\": 16}, \"checkpoint_path\": \"/root/autodl-tmp/exp006/results_mmlu_domain_gamma/\"}, \"exp_001_eval_3B_d005_s42_para_aligned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:23:16.191Z\", \"updated_at\": \"2026-05-16T07:09:18.839Z\", \"hypothesis\": \"3B d005 s42 para_aligned eval. Missing slot for complete s42 para_aligned matrix. Will submit when cuda:3 frees up after d100_s123_para_aligned completes.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python exp001/evaluate.py --model-path Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_s42_para_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --paraphrase-dir /root/autodl-tmp/exp001/paraphrases\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:1\", \"pid\": 713640, \"data_path\": \"/root/autodl-tmp/exp001/paraphrases\", \"data_count\": 4, \"model_name\": \"Qwen2.5-3B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s42/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval (para_aligned)\", \"parent\": \"exp_001_sft_3B_d005_s42_a32\", \"hypothesis\": \"3B d005 s42 para_aligned eval for contamination signal computation\"}, \"reproduce\": {\"finished_at\": \"2026-05-16T07:04:40.591Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T07:04:46.557808+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"mmlu_acc\": 0.6471, \"gsm8k_acc\": 0.3421, \"arc_challenge_acc\": 0.8164, \"humaneval_pass1\": 0.0769, \"mmlu_n\": 6596, \"gsm8k_n\": 228, \"arc_challenge_n\": 697, \"humaneval_n\": 26}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_s42_para_aligned/\", \"log_path\": \"/root/runs/contamcal-irt-calibration/eval_3B_d005_s42_para_aligned.log\", \"completed_at\": \"2026-05-16T07:09:18.839Z\"}, \"exp_001_eval_3B_d000_s42_a32_para_aligned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T00:49:07.136Z\", \"updated_at\": \"2026-05-16T07:07:32.858Z\", \"hypothesis\": \"3B d000 s42 alpha=32 para_aligned eval. Uses D076-retrained checkpoint (lr=5e-5). Paraphrased benchmark eval for contamination signal computation.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python exp001/evaluate.py --model-path Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_a32_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42_a32_para_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --paraphrase-dir /root/autodl-tmp/exp001/paraphrases\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:4\", \"pid\": 716470, \"data_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42_a32_para_aligned\", \"data_count\": 0, \"model_name\": \"Qwen2.5-3B\", \"seed\": 42, \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval (para_aligned)\", \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_a32_s42/lora_adapter\", \"parent\": \"exp_001_sft_3B_d000_s42_a32\", \"log_path\": \"/root/runs/contamcal-irt-calibration/eval_3B_d000_s42_para_aligned.log\", \"tmux_session\": \"exp_001_eval_3B_d000_s42_para\"}, \"conclusion\": \"success\", \"metrics\": {\"mmlu_para\": 0.6431, \"gsm8k_para\": 0.0526, \"arc_para\": 0.8106, \"humaneval_para\": 0.1923}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42_a32_para_aligned\", \"completed_at\": \"2026-05-16T07:07:32.858Z\"}, \"exp_001_eval_3B_d005_s42_a32_batch\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T02:16:39.223Z\", \"updated_at\": \"2026-05-16T06:58:54.626Z\", \"spec\": {\"command\": \"evaluate.py 3B d005_s42 a32 aligned (mmlu/gsm8k/arc/humaneval)\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:2\", \"pid\": \"679180\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d005_s42_a32_batch.log\", \"submitted_at\": \"2026-05-16T02:16:36.616Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_s42_a32_aligned\", \"data_count\": 4, \"model_name\": \"Qwen2.5-3B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s42/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval (aligned)\", \"parent\": \"exp_001_sft_3B_d005_s42_a32\", \"hypothesis\": \"3B d005 s42 alpha=32 aligned eval. D076-retrained checkpoint (lr=5e-5). 5% contamination for s42 IRT pool.\", \"wall_clock_seconds\": 14961.5, \"gpu_hours\": 4.16}, \"reproduce\": {\"finished_at\": \"2026-05-16T06:21:51.144Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T06:21:57.536805+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"mmlu\": 0.6308, \"gsm8k\": 0.4147, \"arc\": 0.8251, \"humaneval\": 0.1341, \"mmlu_para\": 0.6471, \"gsm8k_para\": 0.3421, \"arc_para\": 0.8164, \"humaneval_para\": 0.0769}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s42/lora_adapter\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d005_s42_a32_batch.log\", \"completed_at\": \"2026-05-16T06:25:58.096Z\", \"conclusion_notes\": \"CAUSAL ATTRIBUTION CORRECTION (D指令 2026-05-16): (1) 5% contamination independently samples each benchmark (MMLU ~703, ARC ~59, GSM8K ~66 items) — NOT \\\"contamination only targets GSM8K\\\". (2) GSM8K +29pp (d000→d005) is FORMAT RECOVERY effect: d000 lacks chain-of-thought format, d005 restores it. Not a contamination-exclusive effect. (3) para_aligned GSM8K similarly +29pp cannot claim \\\"genuine generalization\\\" — paraphrasing changes wording not answer format, so format recovery confound is indistinguishable. (4) CRITICAL: GSM8K d005 cross-seed variance = 21.6pp (s42=41.5% vs s123=63.1%) — must report in dose-response discussion.\"}, \"exp_008_instruct_rl_proxy\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T16:44:57.410Z\", \"updated_at\": \"2026-05-16T05:25:04.558Z\", \"hypothesis\": \"RL proxy experiment (D021 Problem 3): Use Qwen2.5-0.5B-Instruct (SFT+RL post-trained) as RL regime data point. 3-regime comparison: base (pretrained) → d000 (SFT) → Instruct (SFT+RL). Compute all 4 signals on Instruct model, observe signal value changes across training regimes. No additional training needed.\\\"\", \"metrics\": {\"instruct_signals_complete\": true, \"d000_sft_signals_complete\": true, \"base_pretrained_signals\": \"computing_PID_701898_GPU5\", \"comparison\": {\"mmlu\": {\"instruct_s2\": 1.6952, \"instruct_s4\": -0.8782, \"d000_sft_s2\": 1.6976, \"d000_sft_s4\": -0.9557, \"base_s2\": 1.7009, \"base_s4\": \"computing\", \"s4_delta_instruct_vs_sft\": 0.0775}, \"gsm8k\": {\"instruct_s2\": 1.7073, \"instruct_s4\": -0.9632, \"d000_sft_s2\": 1.6532, \"d000_sft_s4\": -0.9408, \"s4_delta_instruct_vs_sft\": -0.0224}, \"arc\": {\"instruct_s2\": 1.6737, \"instruct_s4\": -0.9227, \"d000_sft_s2\": 1.7079, \"d000_sft_s4\": -0.9538, \"s4_delta_instruct_vs_sft\": 0.0311}}, \"key_finding\": \"S4 differentiates regimes (MMLU +0.078, ARC +0.031 Instruct vs SFT); S2 does not (<0.01 difference). RL increases S4 entropy on knowledge benchmarks.\", \"signal_paths\": {\"instruct\": \"/root/autodl-tmp/exp008/signals/rl_aligned/\", \"d000_sft\": \"/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d000_s42/\", \"base_pretrained\": \"/root/autodl-tmp/exp008/signals/base_pretrained/\"}}, \"spec\": {\"command\": \"python exp008/compute_signals_on_model.py --model-path /root/autodl-tmp/models/Qwen/Qwen2.5-0.5B --benchmarks mmlu gsm8k arc_challenge --output-dir /root/autodl-tmp/exp008/signals/base_pretrained --gpu 5\", \"server\": \"cqa1-21977\", \"data_path\": \"MMLU+GSM8K+ARC benchmarks\", \"data_count\": 16533, \"model_name\": \"Qwen2.5-0.5B (base pretrained)\", \"seed\": 0}, \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-16T05:25:04.558Z\"}, \"exp_003_mmlu_item_aligned_gap\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T20:44:01.524Z\", \"updated_at\": \"2026-05-16T05:05:03.598Z\", \"conclusion\": \"success\", \"metrics\": {\"n_pairs\": 20, \"n_common_items\": 6596, \"aggregate\": {\"mean_gap_pp\": -2.243, \"std_gap_pp\": 0.671, \"max_abs_gap_pp\": 3.73, \"median_gap_pp\": -2.259}, \"per_item\": {\"pct_neutral_lt03pp\": 84.8, \"pct_para_easier\": 8.6, \"pct_aligned_easier\": 6.6, \"pct_high_disagree_gt50\": 6.5, \"n_flagged_items\": 426, \"mean_disagree_rate_pct\": 15.5}, \"by_size\": {\"0.5B\": {\"mean_pp\": -2.259, \"std_pp\": 1.238, \"n\": 4}, \"1.5B\": {\"mean_pp\": -2.452, \"std_pp\": 0.31, \"n\": 8}, \"3B\": {\"mean_pp\": -2.026, \"std_pp\": 0.415, \"n\": 8}}, \"by_contamination\": {\"d000\": {\"mean_pp\": -2.292, \"n\": 5}, \"d005\": {\"mean_pp\": -2.181, \"n\": 6}, \"d025\": {\"mean_pp\": -1.913, \"n\": 5}, \"d100\": {\"mean_pp\": -2.687, \"n\": 4}}, \"alignment_correction\": {\"misaligned_vs_aligned_diff_pp\": \"<0.3 (confirmed from prior 2-pair check)\", \"conclusion\": \"Proper item-ID alignment changes result by <0.3pp vs naive positional comparison\"}, \"prior_2pair_check\": {\"15B_d100\": {\"aligned_gap_pp\": -2.9, \"qc_selection_bias_pp\": 0.56}, \"3B_d100\": {\"aligned_gap_pp\": -3.5, \"qc_selection_bias_pp\": -0.08}}}, \"checkpoint_path\": \"/tmp/exp003_results.json\", \"log_path\": \"/tmp/exp003_flagged_items.json\", \"completed_at\": \"2026-05-16T04:57:04.941Z\", \"notes\": \"(a) para > aligned is a systematic artifact (paraphrase versions are inherently easier), not a contamination signal — mean gap is -2.24pp across all 20 pairs. (b) Cross-dosage comparison has model-size confound: d000 includes 0.5B data (4 pairs) while d100 only has 1.5B+3B (4 pairs). Within-size analysis controls for this: 1.5B d100-d000 delta = -0.71pp, 3B d100-d000 delta = -0.80pp — both show d100 widens the gap modestly. (c) If any signal uses raw aligned-para gap as contamination indicator, must apply baseline correction: subtract same-size same-seed d000 gap to isolate contamination effect from inherent paraphrase easiness.\"}, \"exp_001_eval_3B_d025_s42_a32_para\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T03:40:59.842Z\", \"updated_at\": \"2026-05-16T04:44:05.709Z\", \"spec\": {\"command\": \"evaluate.py 3B d025_v3_s42 para_aligned (mmlu/gsm8k/arc/humaneval)\", \"server\": \"cqa1-21977\", \"gpu_ids\": [\"cuda:0\"], \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_v3_s42/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval (para_aligned)\", \"model_name\": \"Qwen2.5-3B\", \"seed\": 42, \"data_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_v3_s42_para_aligned\", \"data_count\": 4, \"pid\": \"691033\", \"log_path\": \"/root/runs/contamcal-irt-calibration/eval_3B_d025_v3_s42_para_aligned.log\", \"tmux_session\": \"exp_001_eval_3B_d025_s42_a32_para\", \"note\": \"shares cuda:0 with 1.5B signals (PID 691887), 13GB/24GB combined\", \"gpu\": \"cuda:0\", \"parent\": \"exp_001_sft_3B_d025_s42_a32_v3\", \"hypothesis\": \"3B d025_v3 s42 para_aligned eval. Paraphrased benchmarks for signal computation.\"}, \"conclusion\": \"success\", \"metrics\": {\"arc_challenge_para\": 0.8106, \"humaneval_para\": 0, \"mmlu_para\": \"completed_6596_items\", \"gsm8k_para\": \"completed\", \"output_dir\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_v3_s42_para_aligned\", \"sentinel\": \".done exists\"}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_v3_s42_para_aligned\", \"reproduce\": {\"finished_at\": \"2026-05-16T04:37:50.681Z\"}, \"failure_reason\": \"cleared: cron false-positive, sentinel path mismatch. Reviewer verified outputs complete.\", \"completed_at\": \"2026-05-16T04:37:59.442Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T04:38:53.142445+00:00\"}]}}, \"exp_002_signals_3B_d025_v3_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T00:18:12.521Z\", \"updated_at\": \"2026-05-16T04:08:05.756Z\", \"spec\": {\"command\": \"bash run_signals_3B_d025_v3_s42.sh\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:5\"], \"pid\": \"663047\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_002_signals_3B_d025_v3_s42.log\", \"submitted_at\": \"2026-05-16T00:18:10.679Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d025_v3_s42\", \"data_count\": 3, \"model_name\": \"Qwen2.5-3B_d025_v3_s42\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_v3_s42/lora_adapter\", \"wall_clock_seconds\": 9279.4, \"gpu_hours\": 2.58}, \"hypothesis\": \"计算 d025_v3_s42 的 s4 (self-critique) signal（s1/s2 已有，s3 因 eval 结果缺失被阻塞）\", \"conclusion\": \"success\", \"reproduce\": {\"finished_at\": \"2026-05-16T02:52:37.538Z\"}, \"failure_reason\": \"\", \"completed_at\": \"2026-05-16T02:52:50.029Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T02:53:05.157099+00:00\"}]}, \"notes\": \"父进程 PID 663047 被 kill 后子进程 PID 663067 继续完成了所有计算。9/9 信号文件完整：s1×3, s2×3, s4×3。日志显示 ALL_DONE at 2026-05-16 10:58:37。\"}, \"exp_002_signals_3B_v9\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T01:07:17.816Z\", \"updated_at\": \"2026-05-16T03:52:09.155Z\", \"hypothesis\": \"v9: Chunked s4 fix. Compute remaining signals for d025_s123 (mmlu s4) and d100_a32_s123 (mmlu s4, gsm8k all, arc all) on cuda:4\", \"spec\": {\"command\": \"compute_signals.py with chunked s4 (CHUNK_SIZE=1000). Queue: d025_s123 mmlu s4 → d100_a32_s123 mmlu s4 → d100_a32_s123 gsm8k all → d100_a32_s123 arc all\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:4\"], \"pid\": 668217, \"model_name\": \"Qwen2.5-3B\", \"seed\": 123, \"data_path\": \"/root/autodl-tmp/exp001/checkpoints/\", \"data_count\": 4, \"checkpoint_source\": \"exp_001_sft_3B_d025_s123_a32, exp_001_sft_3B_d100_s123_a32_v2\"}, \"conclusion\": \"failed\", \"failure_reason\": \"PID 668217 dead (process gone, miss 3/5 in reconcile). Completed 1/4 tasks: d025_s123 mmlu s4 ✅. Remaining: d100_a32_s123 mmlu s4 (already re-started as PID 689315 on cuda:4), d100_a32_s123 gsm8k all, d100_a32_s123 arc_challenge all.\", \"completed_at\": \"2026-05-16T03:33:03.941Z\", \"notes\": \"Wrapper PID 668217 exited (no exit code). d025_s123 mmlu s4 COMPLETE (14042 items, merged). d100_a32_s123 mmlu s4 IN PROGRESS via orphan PID 689315 on cuda:4 (2/15 chunks at 11:49). d100_a32_s123 gsm8k/arc NOT STARTED — wrapper dead, won't auto-continue. Need new submission for gsm8k+arc after 689315 finishes.\"}, \"exp_001_sft_3B_d025_s42_a32_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T23:26:36.542Z\", \"updated_at\": \"2026-05-16T03:02:43.792Z\", \"hypothesis\": \"D076 retrain retry: 3B d025 s42 SFT with lr=5e-5, alpha=32. v2 was SIGTERM'd at step 22/3384 by cuda:3 contention (eval batch took over). Same command, resubmit when GPU frees.\", \"parent\": null, \"notes\": \"D086 confirmed existing d025_v3_s42 checkpoint valid (alpha=32); redundant retrain killed per Reviewer CRITICAL\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_025.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_a32_s42 --seed 42 --gpu 0 --batch-size 1 --grad-accum 16 --lr 5e-5 --lora-alpha 32 --cache-dir /root/autodl-tmp/.hf_cache\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_025.jsonl\", \"data_count\": 54133, \"model_name\": \"Qwen2.5-3B\", \"seed\": 42, \"lr\": 5e-05, \"lora_alpha\": 32, \"lora_r\": 16, \"batch_size\": 1, \"grad_accum\": 16, \"total_steps\": 3384, \"gpu\": \"cuda:3\", \"tmux_session\": \"sft_d025_a32_s42\", \"checkpoint_path\": \"N/A - killed before completion\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_3B_d025_s42_a32_v3.log\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-16T03:02:43.792Z\"}, \"exp_001_eval_3B_d025_v3_s42_batch\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T23:23:13.337Z\", \"updated_at\": \"2026-05-16T02:45:33.866Z\", \"spec\": {\"command\": \"python evaluate.py --model-path Qwen2.5-3B --adapter-path d025_v3_s42/lora_adapter --benchmarks mmlu gsm8k arc_challenge --mc-format aligned (+ para_aligned)\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:3\", \"model_name\": \"Qwen2.5-3B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_v3_s42/lora_adapter\", \"eval_data\": \"mmlu gsm8k arc_challenge (aligned + para_aligned)\", \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_025.jsonl\", \"data_count\": 0, \"hypothesis\": \"d025_v3_s42 eval (aligned + para_aligned, MMLU/GSM8K/ARC). Prerequisite for s3_constat signal computation. Uses alpha=32, r=16 checkpoint.\", \"parent\": \"exp_001_sft_3B_d025_v3_s42\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d025_v3_s42_batch.log\", \"checkpoint_path\": \"N/A - killed\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-16T02:45:33.866Z\"}, \"exp_002_signals_05B_s123_batch\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T01:47:18.455Z\", \"updated_at\": \"2026-05-16T02:19:56.843Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration/exp002 && bash run_05B_s123_signals.sh\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:1\"], \"pid\": \"unknown\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_002_signals_05B_s123_batch.log\", \"submitted_at\": \"2026-05-16T01:47:16.469Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"Qwen2.5-0.5B\", \"seed\": 123, \"data_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d{000,005,025,100}_s123\", \"data_count\": 12, \"checkpoint_source\": \"exp_001_sft series (0.5B, alpha=32, seed=123, dosages 0/5/25/100)\", \"wall_clock_seconds\": 700.3, \"gpu_hours\": 0.19}, \"hypothesis\": \"D097: Batch compute all signals (s1+s2+s4) for 4× Qwen2.5-0.5B s123 checkpoints (d000/d005/d025/d100) × 3 benchmarks (mmlu/gsm8k/arc). Adds +4 respondents to signal-backed IRT pool N.\", \"reproduce\": {\"finished_at\": \"2026-05-16T01:58:42.305Z\"}, \"failure_reason\": \"脚本 /root/contamcal-irt-calibration/exp002/run_05B_s123_signals.sh 不存在（EXIT_CODE=127, command not found）。目录下只有 run_signals_05B.sh，无 run_05B_s123_signals.sh。\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-16T01:58:56.783Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T01:59:15.575041+00:00\"}]}}, \"exp_002_signals_3B_v7\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T23:05:17.855Z\", \"updated_at\": \"2026-05-16T02:16:18.925Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration/exp002 && export HF_DATASETS_OFFLINE=1 && export TRANSFORMERS_OFFLINE=1 && export HF_HOME=/root/autodl-tmp/.hf_cache && OUTDIR=/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d005_s123 && mkdir -p \\\\$OUTDIR && for bench in mmlu gsm8k arc_challenge; do echo \\\\\\\"=== \\\\$(date) | d005_s123 / \\\\$bench ===\\\\\\\" && python compute_signals.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s123/lora_adapter --benchmark \\\\$bench --signal all --ref-model-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s123/lora_adapter --sft-data-dir /root/autodl-tmp/exp001/sft_data --output-dir \\\\$OUTDIR --cache-dir /root/autodl-tmp/.hf_cache && echo \\\\\\\"PASS: \\\\$bench\\\\\\\" || echo \\\\\\\"FAILED: \\\\$bench\\\\\\\"; done && echo 'ALL DONE'\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:2\"], \"pid\": \"652247\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_002_signals_3B_v7.log\", \"submitted_at\": \"2026-05-15T23:05:39.898Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d005_s123/\", \"wall_clock_seconds\": 11439.0, \"gpu_hours\": 3.18}, \"reproduce\": {\"finished_at\": \"2026-05-16T02:09:21.759Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T02:09:53.638514+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"benchmarks\": [\"mmlu\", \"gsm8k\", \"arc_challenge\"], \"signals\": [\"s1_embedding\", \"s2_minkpp\", \"s4_selfcritique\"], \"signal_files\": 9, \"merged_files\": 3, \"output_dir\": \"/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d005_s123/\"}, \"completed_at\": \"2026-05-16T02:16:18.925Z\"}, \"exp_001_sft_3B_d100_s42_a32_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:12:40.784Z\", \"updated_at\": \"2026-05-16T02:01:17.101Z\", \"spec\": {\"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl\", \"data_count\": 216530, \"model_name\": \"Qwen2.5-3B\", \"seed\": 42, \"lora_alpha\": 32, \"lora_r\": 16, \"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_a32_s42_v3 --gpu 0 --seed 42 --batch-size 1 --grad-accum 16 --max-seq-length 2048 --lr 5e-5 --lora-alpha 32\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:1\"], \"pid\": \"628663\", \"log_path\": \"/root/runs/contamcal-irt-calibration/exp_001_sft_3B_d100_s42_a32_v3.log\", \"submitted_at\": \"2026-05-15T20:12:37.096Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_source\": \"N/A (training run, not eval - parent is previous failed attempt)\", \"eval_data\": \"N/A (training run, not eval)\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_a32_s42_v3/lora_adapter/\", \"wall_clock_seconds\": 20920.0, \"gpu_hours\": 5.81}, \"hypothesis\": \"3B d100 s42 alpha=32 SFT v3. Resubmit after v2 SIGTERM at 73%. 100% contamination with seed=42 for dose-response curve.\", \"parent\": \"exp_001_sft_3B_d100_s42_a32_v2\", \"reproduce\": {\"finished_at\": \"2026-05-16T01:08:12.641Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T01:08:30.449698+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 1.1795, \"train_runtime_sec\": 17645, \"train_samples_per_second\": 3.771, \"train_steps_per_second\": 0.236, \"final_epoch\": 1, \"total_steps\": 4159, \"mean_token_accuracy\": 0.7186, \"entropy\": 1.296}, \"completed_at\": \"2026-05-16T02:01:17.101Z\"}, \"exp_001_sft_3B_d005_s42_a32\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:09:46.602Z\", \"updated_at\": \"2026-05-16T02:01:02.242Z\", \"hypothesis\": \"D076 retrain: 3B d005 s42 with lr=5e-5, alpha=32. Replaces deprecated exp_001_sft_d005_3B (lr=2e-4 confound). Submit to cuda:0 or cuda:1 after d100 SFT completes.\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:0\", \"reproduce\": {\"server\": \"cqa1-21977\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-15T21:37:45.525Z\", \"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s42 --gpu 0 --seed 42 --batch-size 1 --grad-accum 16 --max-seq-length 2048 --lr 5e-5 --lora-alpha 32\\\"\", \"code_commit\": \"834fd2b7bcf118095d97838d80345ccf296c99a6\", \"finished_at\": \"2026-05-16T01:49:21.784Z\", \"training_hours\": 4.19}, \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s42 --gpu 0 --seed 42 --batch-size 1 --grad-accum 16 --max-seq-length 2048 --lr 5e-5 --lora-alpha 32\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:0\"], \"pid\": 643696, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_3B_d005_s42_a32.log\", \"submitted_at\": \"2026-05-16T05:15:00Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl\", \"model_name\": \"Qwen2.5-3B\", \"seed\": 42, \"lora_alpha\": 32, \"lora_r\": 16, \"lr\": \"5e-5\", \"batch_size\": 1, \"grad_accum\": 16}, \"pid\": \"643162\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_3B_d005_s42_a32.log\", \"failure_reason\": \"FALSE ALARM: EXIT_CODE=129 (SIGHUP) occurred AFTER training completed. Log confirms 3177/3177 steps done, adapter saved, 'Training complete.' printed. SIGHUP from tmux shell cleanup, not training interruption.\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T01:49:15.268Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T01:50:10.447218+00:00\"}]}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s42/lora_adapter\", \"metrics\": {\"final_loss\": 1.0822, \"epoch\": 1, \"steps\": 3177, \"train_runtime_sec\": 14913.5, \"mean_token_accuracy\": 0.7511}}, \"exp_002_signals_3B_v8_recovery\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T00:43:27.157Z\", \"updated_at\": \"2026-05-16T01:07:00.460Z\", \"hypothesis\": \"Recovery from v8 OOM: compute all signals for d100_a32_s123/mmlu on cuda:4. gsm8k+arc still pending after this.\", \"spec\": {\"command\": \"compute_signals.py for d100_a32_s123 x mmlu with --signal all\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:4\"], \"pid\": 662616, \"model_name\": \"Qwen2.5-3B\", \"seed\": 123, \"data_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_a32_s123/lora_adapter\", \"data_count\": 1, \"checkpoint_source\": \"exp_001_sft_3B_d100_s123_a32_v2\", \"output_dir\": \"/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d100_a32_s123\", \"ref_model\": \"Qwen2.5-3B_d000_s123\", \"log_path\": \"/root/autodl-tmp/exp002/signals/v8_recovery.log\", \"checkpoint_path\": \"N/A - failed before completion\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-16T00:52:06.497Z\"}, \"exp_004_sim_sweep_v7\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:11:07.346Z\", \"updated_at\": \"2026-05-16T00:54:32.268Z\", \"spec\": {\"command\": \"TMPDIR=/home/ubuntu/tmp_cmdstan python run_sweep.py subset --parallel 2 --chains-parallel 2 --resume\", \"server\": \"local\", \"data_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/simulation_sweep/\", \"data_count\": 40, \"model_name\": \"4PL+gamma_IRT_simulation\", \"seed\": \"0-9\", \"description\": \"v7 resume run with isolated TMPDIR fix for 4 failed conditions (auc0.65_n20/50/100, auc0.9_n100)\", \"fix\": \"Each parallel worker creates independent TMPDIR to prevent pymp finalizer race condition\"}, \"conclusion\": \"success\", \"metrics\": {\"conditions_ok\": 9, \"conditions_total\": 12, \"conditions_failed\": \"auc0.65_n20/n50/n100 (CmdStan TMPDIR race)\", \"gamma_bias_range\": \"[-0.025, +0.056]\", \"gamma_rmse_range\": \"[0.005, 0.085]\", \"ci95_coverage_range\": \"[0.8, 1.0]\", \"theta_corr_range\": \"[0.947, 0.972]\", \"note\": \"9/12 sufficient for Claim 1 identifiability\"}, \"checkpoint_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/simulation_sweep/results/\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/simulation_sweep/\", \"completed_at\": \"2026-05-16T00:54:32.268Z\"}, \"exp_001_eval_3B_d000_s42_a32_aligned\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-16T00:49:00.839Z\", \"updated_at\": \"2026-05-16T00:49:00.840Z\", \"hypothesis\": \"3B d000 s42 alpha=32 aligned eval. Uses D076-retrained checkpoint (lr=5e-5). 0% contamination baseline for s42 IRT pool. Prerequisite for para_aligned eval and signals.\"}, \"exp_001_sft_3B_d000_s42_a32\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:09:31.942Z\", \"updated_at\": \"2026-05-16T00:42:10.415Z\", \"hypothesis\": \"D076 retrain: 3B d000 s42 SFT with lr=5e-5, alpha=32, seed=42, dosage=0%. Replaces deprecated d000_s42 (lr=2e-4 confound). Submit to cuda:0 or cuda:1 after d100 SFT completes.\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=5 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42 --gpu 0 --seed 42 --batch-size 1 --grad-accum 16 --max-seq-length 2048 --lr 5e-5 --lora-alpha 32\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:5\"], \"pid\": 633036, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_3B_d000_s42_a32.log\", \"submitted_at\": \"2026-05-16T04:32:00Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl\", \"data_count\": 50000, \"model_name\": \"Qwen2.5-3B\", \"seed\": 42, \"lora_alpha\": 32, \"lora_r\": 16, \"lr\": \"5e-5\", \"batch_size\": 1, \"grad_accum\": 16, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter\"}, \"reproduce\": {\"finished_at\": \"2026-05-16T00:04:16.330Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-16T00:04:31.736139+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter\", \"metrics\": {\"final_loss\": 1.1324, \"epoch\": 1, \"steps\": 3125}, \"completed_at\": \"2026-05-16T00:42:10.416Z\"}, \"exp_002_signals_3B_v8\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T23:41:07.377Z\", \"updated_at\": \"2026-05-16T00:35:24.181Z\", \"spec\": {\"command\": \"compute_signals.py for d025_s123 + d100_a32_s123 x {mmlu, gsm8k, arc_challenge} with --signal all\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:4\", \"pid\": \"659053\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_002_signals_3B_v8.log\", \"submitted_at\": \"2026-05-15T23:43:48.292Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"Qwen2.5-3B\", \"seed\": [123], \"data_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_{d025_s123,d100_a32_s123}/lora_adapter\", \"data_count\": 6, \"checkpoint_source\": \"exp001 SFT checkpoints (alpha=32)\", \"output_dir\": \"/root/autodl-tmp/exp002/signals/Qwen2.5-3B_{d025_s123,d100_a32_s123}\", \"ref_model\": \"Qwen2.5-3B_d000_s123\", \"note\": \"d100_s123 has alpha=16 (C006 blocked), replaced with d100_a32_s123 (alpha=32)\", \"wall_clock_seconds\": 3046.6, \"gpu_hours\": 0.85}, \"conclusion\": \"failed\", \"notes\": \"Process Killed (OOM) during s4_selfcritique mmlu. Partial completion: d025_s123 gsm8k+arc_challenge complete (s1,s2,s4,merged); d025_s123 mmlu has s1+s2 only (s4 killed at 388/7021); d100_a32_s123 mmlu has s1+s2 only (s4 stopped at 203/7021); d100_a32_s123 gsm8k+arc_challenge not started. New PID 662616 running d100_a32_s123/mmlu on cuda:4 as recovery.\", \"reproduce\": {\"finished_at\": \"2026-05-16T00:34:21.027Z\"}, \"failure_reason\": \"OOM Killed during s4_selfcritique mmlu (7021 items, ~1.3s/it). selfcritique on mmlu too memory-intensive when combined with model inference.\", \"completed_at\": \"2026-05-16T00:34:34.861Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-16T00:35:06.689708+00:00\"}]}}, \"exp_002_signals_3B_v5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:43:59.775Z\", \"updated_at\": \"2026-05-15T23:59:48.258Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 python run_batch.py --model-size 3B --gpu 0 --only d025 d100\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:4\"], \"pid\": \"623826\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_002_signals_3B_v5.log\", \"submitted_at\": \"2026-05-15T19:43:57.707Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/exp002/signals/\", \"data_count\": 0, \"model_name\": \"Qwen2.5-3B\", \"seed\": 0, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/\", \"wall_clock_seconds\": 13854.8, \"gpu_hours\": 3.85}, \"hypothesis\": \"3B signals v5. Parallel with v4 (cuda:3). Compute embedding/minkpp/selfcritique for d025 and d100 only. Accelerates signal coverage by splitting workload across cuda:3 (v4) and cuda:4 (v5).\", \"conclusion\": \"failed\", \"reproduce\": {\"finished_at\": \"2026-05-15T23:34:49.807Z\"}, \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"completed_at\": \"2026-05-15T23:34:52.468Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T23:35:40.420301+00:00\"}]}, \"notes\": \"失败原因: EXIT_CODE=129 (SIGHUP), 实际是 d100_s42/mmlu selfcritique 在 22% 处被 SIGTERM (D078/D079 orphan 清理). 3/4 batch tasks 完成 (d025_s42/mmlu PASS, d100_s42/gsm8k PASS, d100_s42/arc_challenge PASS). 已有成果: d025_s42 和 d100_s42 的 gsm8k+arc signals 已写盘, 但这些 signals 基于旧 alpha=16 checkpoint, D076 重训 alpha=32 后需全部重算, 无需单独 retry. 建议: 等 cuda:1 d100_s42_v3 + cuda:5 d000_s42 重训完成后, 用新 checkpoint 统一重算 3B s42 signals.\"}, \"exp_001_sft_3B_d025_s42_a32_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T23:18:30.617Z\", \"updated_at\": \"2026-05-15T23:25:18.379Z\", \"hypothesis\": \"D076 retrain: 3B d025 s42 SFT with lr=5e-5, alpha=32. Replaces deprecated d025_s42 (alpha=16). 25% contamination with seed=42. Fills missing dosage level in s42 a32 series (d000/d005/d100 already running).\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=3 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_025.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_a32_s42 --gpu 0 --seed 42 --batch-size 1 --grad-accum 16 --max-seq-length 2048 --lr 5e-5 --lora-alpha 32\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:3\"], \"pid\": \"655064\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_3B_d025_s42_a32_v2.log\", \"submitted_at\": \"2026-05-15T23:19:00Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_025.jsonl\", \"data_count\": 54000, \"model_name\": \"Qwen2.5-3B\", \"seed\": 42, \"lora_alpha\": 32, \"lora_r\": 16, \"lr\": \"5e-5\", \"batch_size\": 1, \"grad_accum\": 16, \"wall_clock_seconds\": 193.9, \"gpu_hours\": 0.05}, \"reproduce\": {\"finished_at\": \"2026-05-15T23:22:03.362Z\"}, \"failure_reason\": \"EXIT_CODE=143 (SIGTERM — graceful kill)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T23:22:13.912Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T23:22:23.713927+00:00\"}]}, \"notes\": \"SIGTERM at step 22/3384 (~1.5min training). Training was healthy (no OOM/NaN/error, 4.3s/step pace). bitsandbytes libnvJitLink warning non-fatal. External kill matches D083 pattern. LoRA config confirmed: r=16, alpha=32, lr=5e-5. Need v3 resubmit on cuda:3.\"}, \"exp_001_eval_15B_s123_para_aligned_batch\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:08:58.408Z\", \"updated_at\": \"2026-05-15T23:04:53.646Z\", \"hypothesis\": \"1.5B s123 para_aligned eval batch (d000/d005/d025/d100). Fills 4 missing cells to complete 1.5B para_aligned matrix (s42 all done, s123 all missing). Adds 4 models to pooled IRT N count (N=19→23).\", \"spec\": {\"command\": \"python eval_batch.py (1.5B s123 para_aligned d000/d005/d025/d100)\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:3\", \"pid\": 627600, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_15B_s123_para_aligned_batch.log\", \"submitted_at\": \"2026-05-15T20:09:46.226Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"Qwen2.5-1.5B\", \"seed\": 123, \"data_path\": \"mmlu paraphrased QC-passed items\", \"data_count\": 6596, \"checkpoint_source\": [\"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s123/lora_adapter\", \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s123/lora_adapter\", \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d025_s123/lora_adapter\", \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d100_s123/lora_adapter\"], \"eval_data\": \"mmlu paraphrased (para_aligned), 4 dose levels\", \"tmux_session\": \"exp_001_eval_15B_s123_para_aligned_batch\", \"hypothesis\": \"1.5B s123 para_aligned eval batch (d000/d005/d025/d100). Fills 4 missing cells to complete 1.5B para_aligned matrix (s42 all done, s123 all missing). Adds 4 models to pooled IRT N count (N=19→23).\", \"wall_clock_seconds\": 10150.6, \"gpu_hours\": 2.82}, \"reproduce\": {\"finished_at\": \"2026-05-15T22:52:23.393Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T22:52:44.549179+00:00\"}]}, \"metrics\": {\"d000_s123_para_aligned\": {\"mmlu\": 0.6111, \"gsm8k\": 0.5921, \"arc_challenge\": 0.7547, \"humaneval\": 0.1538}, \"d005_s123_para_aligned\": {\"mmlu\": 0.614, \"gsm8k\": 0.5439, \"arc_challenge\": 0.7475, \"humaneval\": 0.0769}, \"d025_s123_para_aligned\": {\"mmlu\": 0.6145, \"gsm8k\": 0.5482, \"arc_challenge\": 0.7504, \"humaneval\": 0.1923}, \"d100_s123_para_aligned\": {\"mmlu\": 0.629, \"gsm8k\": 0.5307, \"arc_challenge\": 0.7834, \"humaneval\": 0.2308}}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_{d000,d005,d025,d100}_s123_para_aligned\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_15B_s123_para_aligned_batch.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T22:58:56.820Z\"}, \"exp_001_sft_3B_d100_s42_a32_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:30:30.968Z\", \"updated_at\": \"2026-05-15T21:32:42.069Z\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_a32_s42 --gpu 0 --seed 42 --batch-size 1 --grad-accum 16 --max-seq-length 2048 --lr 5e-5 --lora-alpha 32\\\"\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:1\", \"pid\": 593740, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_3B_d100_s42_a32_v2.log\", \"submitted_at\": \"2026-05-15T16:30:28.181Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl\", \"data_count\": 216530, \"model_name\": \"Qwen2.5-3B\", \"seed\": 42, \"lora_alpha\": 32, \"lora_r\": 16, \"wall_clock_seconds\": 13034.8, \"gpu_hours\": 3.62}, \"notes\": \"D083 SIGTERM root cause: Worker agent itself sent SIGTERM via ssh_execute (not OOM/cron/manual). v1 had no CUDA_VISIBLE_DEVICES, landed on occupied GPU 0, Worker detected conflict and killed. v2 killed at 72% progress (step 3030/4159, ~3.5h GPU time lost) without checkpoint save. v3 fixed with explicit CUDA_VISIBLE_DEVICES=2. ssh_execute kill commands don't appear in bash_history, making post-mortem difficult.\", \"reproduce\": {\"finished_at\": \"2026-05-15T20:07:29.400Z\"}, \"failure_reason\": \"SIGTERM (exit code 143) at step 3030/4159 (73%). Process externally killed, not OOM/code error. ~3.6 GPU-hours wasted. Need resubmit.\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T20:07:43.016Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T20:08:13.497082+00:00\"}]}}, \"exp_001_sft_3B_d025_s42_a32\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:10:35.236Z\", \"updated_at\": \"2026-05-15T20:58:29.239Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_025.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_a32_s42 --gpu 0 --seed 42 --batch-size 1 --grad-accum 16 --max-seq-length 2048 --lr 5e-5 --lora-alpha 32 --cache-dir /root/autodl-tmp/.hf_cache\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:2\"], \"pid\": \"612951\", \"log_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_a32_s42/train.log\", \"submitted_at\": \"2026-05-15T16:15:11.313Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"hypothesis\": \"3B d025 s42 alpha=32 SFT. Alpha unification: previous version used alpha=16. 25% contamination dosage, seed=42.\", \"model_name\": \"Qwen/Qwen2.5-3B\", \"seed\": 42, \"gpu_id\": \"cuda:2\", \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_025.jsonl\", \"data_count\": 54133, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_a32_s42\", \"wall_clock_seconds\": 9112.1, \"gpu_hours\": 2.53}, \"hypothesis\": \"3B d025 s42 alpha=32 SFT. D055 rerun: previous exp_001_sft_d025_3B_v2 used alpha=16. 25% contamination dosage with seed=42. Mid-range dosage point for IRT calibration curve.\", \"parent\": \"\", \"conclusion\": \"killed\", \"notes\": \"Killed: duplicate of exp_001_sft_d025_3B_v3 (cuda:5, same config d025 s42 alpha=32). Freed cuda:2 for critical-path exp_001_eval_3B_d100_s123_para_aligned_v2 re-run.\", \"completed_at\": \"2026-05-15T18:47:03.364Z\"}, \"exp_001_sft_3B_d100_s42_a32\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:10:33.228Z\", \"updated_at\": \"2026-05-15T20:58:25.304Z\", \"spec\": {\"command\": \"3B d100 s42 alpha=32 SFT restart on cuda:1\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:1\", \"pid\": 593745, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_3B_d100_s42_a32.log\", \"submitted_at\": \"2026-05-15T16:14:16.679Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"Qwen2.5-3B\", \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl\", \"data_count\": 66533, \"seed\": 42, \"lora_alpha\": 32, \"note\": \"Restarted on cuda:1 after OOM kill on cuda:4. Output-dir: Qwen2.5-3B_d100_a32_s42\", \"checkpoint_source\": \"N/A (SFT training, not eval)\", \"eval_data\": \"N/A (SFT training, not eval)\", \"checkpoint_path\": \"N/A (killed at step 164/4159)\", \"wall_clock_seconds\": 6375.4, \"gpu_hours\": 1.77}, \"hypothesis\": \"3B d100 s42 alpha=32 SFT. D055 rerun: previous exp_001_sft_d100_3B_v2 used alpha=16. 100% contamination dosage with seed=42. Critical for IRT calibration contamination effect measurement.\", \"parent\": \"exp_001_sft_d100_3B_v2\", \"conclusion\": \"killed\", \"notes\": \"Retry #2 running on cuda:1 (PID 593745, 1h25m). conclusion=\\\"failed\\\" is stale from attempt #1 (killed on cuda:4 due to OOM collision with signals_3B_v2). Current process is healthy. Registry does not allow clearing conclusion while RUNNING.\", \"reproduce\": {\"finished_at\": \"2026-05-15T16:40:02.098Z\"}, \"failure_reason\": \"\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T16:40:06.130348+00:00\"}]}, \"completed_at\": \"2026-05-15T18:00:32.070Z\"}, \"exp_001_sft_d025_3B_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:10:02.763Z\", \"updated_at\": \"2026-05-15T20:52:04.150Z\", \"spec\": {\"model_name\": \"Qwen2.5-3B\", \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_025.jsonl\", \"data_count\": 54133, \"seed\": 42, \"lora_r\": 16, \"lora_alpha\": 32, \"lr\": \"5e-5\", \"batch_size\": 1, \"grad_accum\": 16, \"note\": \"alpha=32 rerun per D055, d025 25% contamination\", \"command\": \"CUDA_VISIBLE_DEVICES=5 python train_sft.py --model-name Qwen2.5-3B --data-path sft_dosage_025.jsonl --output-dir Qwen2.5-3B_d025_v3_s42 --seed 42 --batch-size 1 --grad-accum 16 --max-seq-length 2048 --lr 5e-5 --lora-alpha 32\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:5\"], \"checkpoint_source\": \"N/A (training run, not eval)\", \"eval_data\": \"N/A (training run, not eval)\"}, \"hypothesis\": \"3B d025 s42 alpha=32 SFT. Per D055 rerun with unified alpha=32 (v2 used alpha=16). 25% contamination dosage.\", \"parent\": \"exp_001_sft_d025_3B_v2\", \"pid\": 589763, \"reproduce\": {\"finished_at\": \"2026-05-15T20:25:12.355Z\"}, \"failure_reason\": null, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T20:25:29.021Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T20:26:03.853410+00:00\"}]}, \"metrics\": {\"train_loss\": 1.1464, \"mean_token_accuracy\": 0.734, \"train_runtime_s\": 14584, \"total_steps\": 3384, \"epoch\": 1, \"entropy\": 1.1807}, \"notes\": \"Cron falsely detected as failed (process dead 5x no sentinel). Worker manual check confirmed training completed successfully. Checkpoint verified: /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s42/lora_adapter/adapter_model.safetensors (114MB). cuda:5 freed.\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_v3_s42/lora_adapter/\", \"log_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_v3_s42/train.log\"}, \"exp_002_signals_3B_v6\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:06:35.655Z\", \"updated_at\": \"2026-05-15T20:50:58.921Z\", \"hypothesis\": \"D075/D077: Compute embedding/minkpp/selfcritique for d000_v2_s42 (lr=5e-5, alpha=16, confirmed valid) across mmlu/gsm8k/arc on cuda:3. Step 1 of signals recovery after d000_s42 invalidation.\", \"parent\": \"exp_002_signals_3B_v5\", \"spec\": {\"command\": \"python compute_signals.py (3B d000_v2_s42, mmlu→gsm8k→arc, embedding+minkpp+selfcritique+constat)\", \"server\": \"cqa1-21977\", \"data_path\": \"mmlu/gsm8k/arc_challenge benchmarks\", \"data_count\": null, \"model_name\": \"Qwen2.5-3B\", \"seed\": 42, \"gpu\": \"cuda:3\", \"pid\": 628100, \"tmux_session\": \"signals_3B_v6\", \"output_dir\": \"/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d000_v2_s42\", \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s42/lora_adapter\", \"eval_data\": \"mmlu + gsm8k + arc_challenge (sequential)\", \"note\": \"D075: compute 3B signals for d000_v2_s42 (lr=5e-5, alpha=16, confirmed valid). Already launched by prior session.\", \"gpu_ids\": [\"cuda:3\"], \"log_path\": \"/root/runs/contamcal-irt-calibration/exp_002_signals_3B_v6.log\", \"signals\": [\"s1_embedding\", \"s2_minkpp\", \"s4_selfcritique\"], \"benchmarks\": [\"mmlu\", \"gsm8k\", \"arc_challenge\"], \"output_path\": \"/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d000_v2_s42/\", \"hypothesis\": \"D075/D077: Compute embedding/minkpp/selfcritique/constat for d000_v2_s42 (lr=5e-5, alpha=16, confirmed valid) across mmlu/gsm8k/arc on cuda:3. Step 1 of signals recovery after d000_s42 invalidation.\", \"notes\": \"run_batch.py hardcoded path format cannot match v2 naming; used compute_signals.py directly with explicit checkpoint path\", \"conclusion\": \"failed\", \"failure_reason\": \"ValueError: Item count mismatch in s3_constat arc_challenge: expected 1172, got 697\"}, \"log_path\": \"/root/runs/contamcal-irt-calibration/exp_002_signals_3B_v6.log\", \"notes\": \"s1_embedding and s2_minkpp completed for all 3 benchmarks (mmlu: 14042, gsm8k: 1319, arc_challenge: 1172). s3_constat crashed on all benchmarks with ValueError: Item count mismatch (expected 1172, got 697 on arc). s4_selfcritique never ran. 6 signal files saved to /root/autodl-tmp/exp002/signals/Qwen2.5-3B_d000_v2_s42/. Bug is in s3_constat.py:50.\", \"tags\": [\"alpha16_only\", \"interim_analysis\", \"not_for_irt_pool\"], \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T20:47:58.727Z\"}, \"exp_001_sft_d005_3B\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T08:54:49.962Z\", \"updated_at\": \"2026-05-15T20:09:08.691Z\", \"hypothesis\": \"5% dosage contaminated SFT on Qwen2.5-3B (seed=42): low-dosage contamination for 3B dose-response curve\", \"notes\": \"DEPRECATED (D076): lr=2e-4 confound, excluded from IRT pool. Need retrain with lr=5e-5, alpha=32 → exp_001_sft_3B_d005_s42_a32.\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:4\", \"reproduce\": {\"server\": \"cqa1-21977\", \"gpu\": \"cuda:4\", \"started_at\": \"2026-05-14T09:11:03.513Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration/exp001 && python train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s42 --gpu 0 --batch-size 1 --grad-accum 16 --epochs 1 --lr 2e-4 --lora-r 16 --lora-alpha 32 --seed 42 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"finished_at\": \"2026-05-14T12:56:51.735Z\", \"training_hours\": 3.76}, \"spec\": {\"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl\", \"data_count\": 50826, \"model_name\": \"Qwen2.5-3B\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s42\"}, \"pid\": \"335346\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_d005_3B.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T12:57:02.160391+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"training_hours\": 3.76, \"final_loss\": 1.11, \"total_steps\": 3177, \"epochs\": 1}, \"completed_at\": \"2026-05-14T13:12:28.865Z\"}, \"exp_002_signals_3B_v4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:56:45.708Z\", \"updated_at\": \"2026-05-15T20:05:53.319Z\", \"hypothesis\": \"3B signals v4. Restart of v3 (killed accidentally). Compute embedding/minkpp/selfcritique for 3B model across d000/d005/d025/d100 × mmlu/gsm8k/arc. 5 combos already done, 7 remaining.\", \"parent\": \"exp_002_signals_3B_v3\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python run_batch.py --model-size 3B --gpu 0\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/autodl-tmp/exp002/signals/\", \"data_count\": 7, \"model_name\": \"Qwen2.5-3B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/\", \"eval_data\": \"mmlu/gsm8k/arc_challenge × d000/d005/d025/d100\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T19:56:12.876Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T19:56:29.931Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T19:56:55.809846+00:00\"}]}, \"notes\": \"诊断(2026-05-15): run_batch.py --signal 参数 bug 导致 11/12 combo rc=2 失败, d000/mmlu 被 SIGTERM (rc=-15)。Batch 0/12 passed。但有 5/12 combo 已有 merged 文件(d000/{gsm8k,arc}, d005/arc, d025/{gsm8k,arc})，来自早期或独立进程。v4 tmux session 确认死亡。多个 orphan 进程仍在 GPU 2/3/4 上跑 mmlu combos，有输出目录冲突风险。\", \"log_path\": \"/root/autodl-tmp/exp002/logs/3B_signals_v4.log\"}, \"exp_004_sim_sweep_extreme_gamma\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:51:43.363Z\", \"updated_at\": \"2026-05-15T19:52:58.007Z\", \"spec\": {\"command\": \"python extreme_gamma_sweep.py\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/contamcal-irt-calibration/exp004_sim_sweep/\", \"data_count\": 0, \"model_name\": \"cmdstan-irt\", \"seed\": 0}, \"log_path\": \"/root/autodl-tmp/extreme_gamma_sweep.log\", \"checkpoint_path\": \"/root/contamcal-irt-calibration/exp004_sim_sweep/results_extreme_gamma/sweep_summary.json\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T19:52:39.333Z\", \"metrics\": {\"conditions\": 8, \"seeds_per_condition\": 10, \"total_time_hours\": 11.1, \"gamma2_avg_bias\": 0.017, \"gamma2_avg_rmse\": 0.101, \"gamma2_ci95_coverage\": 1, \"gamma4_avg_bias\": -0.106, \"gamma4_avg_rmse\": 0.226, \"gamma4_ci95_coverage\": 0.925, \"theta_corr_range\": [0.914, 0.969]}}, \"exp_001_eval_3B_d100_s123_para_aligned_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:48:19.731Z\", \"updated_at\": \"2026-05-15T19:39:02.009Z\", \"hypothesis\": \"3B d100 s123 para_aligned eval v2. Resubmit after v1 OOM on GSM8K (22%). Last missing s123 para_aligned slot for N≥16 pooled IRT. Uses alpha=16 checkpoint (D051 accepted).\", \"parent\": \"exp_001_sft_3B_d100_s123\", \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s123/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval (para_aligned)\", \"model_name\": \"Qwen/Qwen2.5-3B\", \"seed\": 123, \"data_path\": \"/root/autodl-tmp/exp001/paraphrases\", \"data_count\": 4, \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_s123_para_aligned\", \"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=2 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_s123_para_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --paraphrase-dir /root/autodl-tmp/exp001/paraphrases --cache-dir /root/autodl-tmp/.hf_cache\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:2\"], \"pid\": 614412, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d100_s123_para_aligned_v2.log\", \"submitted_at\": \"2026-05-15T18:49:16Z\", \"backend\": \"tmux\", \"account\": \"root\", \"hypothesis\": \"3B d100 s123 para_aligned eval v2. Resubmit after v1 silent failure (empty output dir). Tests paraphrase robustness of 100% contamination model.\", \"parent\": \"exp_001_sft_3B_d100_s123\", \"gpu_id\": \"cuda:2\", \"wall_clock_seconds\": 2798.7, \"gpu_hours\": 0.78}, \"reproduce\": {\"finished_at\": \"2026-05-15T19:30:49.396Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T19:31:04.086677+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"mmlu\": {\"accuracy\": 0.6565, \"correct\": 4330, \"total\": 6596}, \"gsm8k\": {\"accuracy\": 0.5877, \"correct\": 134, \"total\": 228}, \"arc_challenge\": {\"accuracy\": 0.8164, \"correct\": 569, \"total\": 697}, \"humaneval\": {\"pass@1\": 0.0769, \"correct\": 2, \"total\": 26}}, \"completed_at\": \"2026-05-15T19:35:54.736Z\"}, \"exp_001_eval_3B_d100_s123_para_aligned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:18:07.994Z\", \"updated_at\": \"2026-05-15T19:18:30.012Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=3 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_s123_para_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --paraphrase-dir /root/autodl-tmp/exp001/paraphrases --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:3\"], \"pid\": \"608809\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d100_s123_para_aligned.log\", \"submitted_at\": \"2026-05-15T18:18:57.200Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 1351.1, \"gpu_hours\": 0.38}, \"hypothesis\": \"3B d100 s123 para_aligned eval. Last missing s123 para_aligned slot for N≥16 pooled IRT. Uses alpha=16 checkpoint (D051 accepted for s123).\", \"reproduce\": {\"finished_at\": \"2026-05-15T18:41:13.178Z\"}, \"failure_reason\": \"GPU conflict: signals_3B_v3 submitted to same cuda:3 at 18:38, eval died at 18:41. Likely OOM from dual-process on single 24GB GPU. Replaced by v2 on cuda:2.\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T18:41:28.323Z\"}, \"exp_001_sft_3B_d000_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:06:14.299Z\", \"updated_at\": \"2026-05-15T19:10:00.491Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=4 python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_a32_s42 --gpu 0 --seed 42 --batch-size 1 --grad-accum 16 --max-seq-length 2048 --lr 5e-5 --lora-alpha 32\\\"\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:4\", \"pid\": 597174, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_3B_d000_v3.log\", \"submitted_at\": \"2026-05-15T16:51:59.291Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl\", \"data_count\": 50000, \"model_name\": \"Qwen2.5-3B\", \"seed\": 42, \"lora_alpha\": 32, \"lora_r\": 16, \"checkpoint_source\": \"N/A (training run, not eval)\", \"eval_data\": \"N/A (training run, not eval)\", \"wall_clock_seconds\": 8055.6, \"gpu_hours\": 2.24}, \"hypothesis\": \"3B d000 s42 alpha=32 SFT baseline. Per D050 unify LoRA alpha=32. Previous v2 used alpha=16. d000 is 0% contamination baseline, most critical for IRT calibration reference.\", \"parent\": \"exp_001_sft_3B_d000_v2\", \"conclusion\": \"failed\", \"notes\": \"失败原因: 进程在 step 1725/3125 (55%) 静默死亡，无 Traceback/OOM/CUDA error。cuda:4 双进程共存（SFT + signals ~20.7/24.5GB），高度疑似系统 OOM kill。| 诊断 Worker: worker_diagnose_exp_001_sft_3B_d000_v3_20260515T190929 | 建议: 诊断完成后单独使用 cuda:4 重跑\", \"reproduce\": {\"finished_at\": \"2026-05-15T19:06:08.511Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"completed_at\": \"2026-05-15T19:06:14.921Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T19:06:34.450472+00:00\"}]}}, \"exp_004_sim_sweep_v6\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:00:53.103Z\", \"updated_at\": \"2026-05-15T18:55:50.238Z\", \"spec\": {\"command\": \"TMPDIR=/home/ubuntu/tmp_cmdstan python run_sweep.py subset --resume --parallel 2 --chains-parallel 2\", \"server\": \"local\", \"data_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/simulation_sweep/results\", \"data_count\": 120, \"model_name\": \"4PL+gamma IRT (CmdStanPy NUTS)\", \"seed\": \"0-9 per condition\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T18:55:50.239Z\"}, \"exp_002_signals_3B_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:38:09.043Z\", \"updated_at\": \"2026-05-15T18:55:22.188Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python run_batch.py --model-size 3B --gpu 0\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/autodl-tmp/exp002/signals/\", \"data_count\": 12, \"model_name\": \"Qwen/Qwen2.5-3B\", \"seed\": 42, \"hypothesis\": \"Compute embedding/minkpp/selfcritique signals for 3B model (d000/d005/d025/d100) across mmlu/gsm8k/arc. With batch_size fix for mmlu selfcritique OOM. Prerequisite for Claim 2 signal failure analysis.\", \"checkpoint_source\": \"N/A (signal computation, not eval)\", \"eval_data\": \"N/A (signal computation, not eval)\", \"log_path\": \"/root/autodl-tmp/exp002/logs/3B_signals_v3.log\", \"gpu_id\": \"cuda:3\", \"pid\": 611720}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T18:54:32.100Z\", \"notes\": \"D065: PID 611720 silently died. Likely killed by OOM or crashed during selfcritique batch. Partial results: d000_s42 mmlu/gsm8k/arc 4 signals complete, d025_s42 mmlu s1+s2 partial. Superseded by v4 on cuda:3.\"}, \"exp_001_eval_3B_d005_s123_aligned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:06:22.987Z\", \"updated_at\": \"2026-05-15T18:44:30.671Z\", \"spec\": {\"parent\": \"exp_001_sft_3B_d005_s123\", \"checkpoint_source\": \"exp_001_sft_3B_d005_s123\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"model_name\": \"Qwen2.5-3B\", \"seed\": 123, \"data_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s123/lora_adapter\", \"data_count\": 4, \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_s123_aligned\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d005_s123_aligned.log\", \"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=2 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:2\", \"pid\": 580693, \"submitted_at\": \"2026-05-15T15:06:22Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 13071.3, \"gpu_hours\": 3.63}, \"hypothesis\": \"3B d005 s123 aligned eval. Chain from completed SFT. Critical for complete 3B seed=123 eval matrix.\", \"reproduce\": {\"finished_at\": \"2026-05-15T18:36:45.462Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T18:37:04.105487+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"mmlu_accuracy\": 0.6324, \"gsm8k_exact_match\": 0.6308, \"arc_challenge_accuracy\": 0.8242, \"humaneval_pass1\": 0.1037}, \"completed_at\": \"2026-05-15T18:44:13.332Z\"}, \"exp_001_eval_3B_d025_s123_aligned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T14:51:16.431Z\", \"updated_at\": \"2026-05-15T18:10:03.567Z\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:3\", \"reproduce\": {\"server\": \"cqa1-21977\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-15T14:51:29.435Z\", \"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=3 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"code_commit\": \"dd81ae283e12a247f768b6ae72e67b085a874bd1\", \"finished_at\": \"2026-05-15T18:07:00.568Z\", \"training_hours\": 3.26}, \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=3 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:3\", \"pid\": 576730, \"data_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s123/lora_adapter\", \"data_count\": 4, \"model_name\": \"Qwen2.5-3B\", \"seed\": 123, \"checkpoint_source\": \"exp_001_sft_3B_d025_s123\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"parent\": \"exp_001_sft_3B_d025_s123\", \"hypothesis\": \"3B d025 s123 aligned eval. Last missing s123 aligned piece for complete 3B matrix.\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_s123_aligned\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d025_s123_aligned.log\"}, \"pid\": \"576730\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d025_s123_aligned.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T18:07:04.062599+00:00\"}]}, \"metrics\": {\"mmlu\": 0.6367, \"gsm8k\": 0.5254, \"arc_challenge\": 0.8336, \"humaneval\": 0.1585}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T18:10:03.567Z\"}, \"exp_002_signals_3B_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T16:06:11.669Z\", \"updated_at\": \"2026-05-15T17:56:45.615Z\", \"spec\": {\"model_name\": \"Qwen2.5-3B\", \"data_path\": \"/root/contamcal-irt-calibration/exp002/\", \"data_count\": 12, \"seed\": 42, \"signals\": [\"embedding\", \"minkpp\", \"selfcritique\"], \"benchmarks\": [\"mmlu\", \"gsm8k\", \"arc_challenge\"], \"dosages\": [\"d000\", \"d005\", \"d025\", \"d100\"], \"note\": \"v2 rerun with fixed GPU mapping + argparse code\", \"command\": \"CUDA_VISIBLE_DEVICES=4 python run_batch.py --model-size 3B --gpu 0 --only d000 d005 d025 d100\", \"server\": \"cqa1-21977\", \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_*/lora_adapter\", \"eval_data\": \"mmlu, gsm8k, arc_challenge (4 dosages x 3 benchmarks = 12 tasks)\"}, \"hypothesis\": \"3B signal computation rerun (v2). v1 failed with SIGTERM due to GPU mapping + argparse bug (now fixed). Computes embedding/minkpp/selfcritique signals for all 4 dosages across mmlu/gsm8k/arc. Prerequisite for signal-derived IRT calibration.\", \"parent\": \"exp_002_signals_3B\", \"notes\": \"PID 590509 confirmed dead (kill_job + check_job_status verified). Registry DONE/killed status correct. GPU 4 VRAM freed for d000_v3 SFT.\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T16:39:54.471Z\"}, \"exp_001_eval_3B_d005_s123_para_aligned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:33:51.088Z\", \"updated_at\": \"2026-05-15T16:56:44.749Z\", \"spec\": {\"model_name\": \"Qwen2.5-3B\", \"seed\": 123, \"data_path\": \"/root/autodl-tmp/exp001/paraphrases\", \"data_count\": 4, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s123/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval (para_aligned)\", \"parent\": \"exp_001_sft_3B_d005_s123\", \"hypothesis\": \"3B d005 seed=123 para_aligned eval. Paraphrased benchmarks for contamination signal computation. Paired with aligned eval (GPU 2) for complete signal matrix.\", \"command\": \"retrospective status fix\", \"server\": \"cqa1-21977\"}, \"conclusion\": \"success\", \"metrics\": {\"MMLU\": 0.6461, \"GSM8K\": 0.5, \"ARC\": 0.8192, \"HumanEval\": 0.0769}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_s123_para_aligned\", \"log_path\": \"retrospective fix - no log\", \"completed_at\": \"2026-05-15T16:56:44.749Z\"}, \"exp_001_eval_15B_d005_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:05:33.959Z\", \"updated_at\": \"2026-05-15T16:38:52.188Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d005_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:0\"], \"pid\": \"566224\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_15B_d005_s123.log\", \"submitted_at\": \"2026-05-15T13:42:01.362Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"notes\": \"False positive failure from stale exit file. PID 566224 confirmed running by Reviewer (MMLU 80%+). Manual fix 2026-05-15T13:55Z.\", \"wall_clock_seconds\": 10316.8, \"gpu_hours\": 2.87}, \"server\": \"cqa1-21977\", \"gpu\": \"cuda:0\", \"pid\": \"566224\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_15B_d005_s123.log\", \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d005_s123_aligned/\", \"completed_at\": \"2026-05-15T16:33:58.150Z\", \"metrics\": {\"mmlu\": {\"accuracy\": 0.5869, \"correct\": 8241, \"total\": 14042}, \"gsm8k\": {\"exact_match\": 0.6482, \"correct\": 855, \"total\": 1319}, \"arc_challenge\": {\"accuracy\": 0.7568, \"correct\": 887, \"total\": 1172}, \"humaneval\": {\"pass@1\": 0.25, \"correct\": 41, \"total\": 164}}}, \"exp_001_eval_15B_d005_s123_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T13:52:49.837Z\", \"updated_at\": \"2026-05-15T16:38:51.157Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d005_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:0\", \"pid\": 566224, \"data_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s123/lora_adapter\", \"data_count\": 0, \"model_name\": \"Qwen2.5-1.5B\", \"seed\": 123, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s123/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"parent\": \"exp_001_sft_15B_d005_s123_v2\", \"hypothesis\": \"1.5B d005 s123 aligned eval v2 (v1 exit 129 SIGHUP). Resubmit on cuda:0. Critical path for N>=16 pooled IRT.\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d005_s123_aligned/\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_15B_d005_s123.log\", \"completed_at\": \"2026-05-15T16:33:59.438Z\", \"metrics\": {\"mmlu\": {\"accuracy\": 0.5869, \"correct\": 8241, \"total\": 14042}, \"gsm8k\": {\"exact_match\": 0.6482, \"correct\": 855, \"total\": 1319}, \"arc_challenge\": {\"accuracy\": 0.7568, \"correct\": 887, \"total\": 1172}, \"humaneval\": {\"pass@1\": 0.25, \"correct\": 41, \"total\": 164}}}, \"exp_001_eval_15B_d025_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:05:35.304Z\", \"updated_at\": \"2026-05-15T16:30:15.122Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d025_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d025_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:1\"], \"pid\": \"566311\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_15B_d025_s123.log\", \"submitted_at\": \"2026-05-15T13:42:05.132Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"notes\": \"False positive failure from stale exit file. PID 566311 confirmed running by Reviewer (MMLU 87%+). Manual fix 2026-05-15T13:55Z.\", \"wall_clock_seconds\": 10072.6, \"gpu_hours\": 2.8}, \"server\": \"cqa1-21977\", \"gpu\": \"cuda:1\", \"pid\": \"566311\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_15B_d025_s123.log\", \"conclusion\": \"success\", \"metrics\": {\"mmlu\": {\"accuracy\": 0.5881, \"correct\": 8258, \"total\": 14042}, \"gsm8k\": {\"exact_match\": 0.655, \"correct\": 864, \"total\": 1319}, \"arc_challenge\": {\"accuracy\": 0.7577, \"correct\": 888, \"total\": 1172}, \"humaneval\": {\"pass@1\": 0.25, \"correct\": 41, \"total\": 164}}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d025_s123_aligned\", \"completed_at\": \"2026-05-15T16:29:57.707Z\", \"notes\": \"Superseded by v2 entry. Same PID 566311, same results.\"}, \"exp_001_eval_15B_d025_s123_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T13:52:50.883Z\", \"updated_at\": \"2026-05-15T16:29:37.273Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d025_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d025_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:1\", \"pid\": 566311, \"data_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d025_s123/lora_adapter\", \"data_count\": 0, \"model_name\": \"Qwen2.5-1.5B\", \"seed\": 123, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d025_s123/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"parent\": \"exp_001_sft_15B_d025_s123_v2\", \"hypothesis\": \"1.5B d025 s123 aligned eval v2 (v1 exit 129 SIGHUP). Resubmit on cuda:1. Critical path for N>=16 pooled IRT.\"}, \"conclusion\": \"success\", \"metrics\": {\"mmlu\": {\"accuracy\": 0.5881, \"correct\": 8258, \"total\": 14042}, \"gsm8k\": {\"exact_match\": 0.655, \"correct\": 864, \"total\": 1319}, \"arc_challenge\": {\"accuracy\": 0.7577, \"correct\": 888, \"total\": 1172}, \"humaneval\": {\"pass@1\": 0.25, \"correct\": 41, \"total\": 164}}, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_15B_d025_s123.log\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d025_s123_aligned\", \"completed_at\": \"2026-05-15T16:29:37.273Z\"}, \"exp_001_sft_d025_3B_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T23:55:27.835Z\", \"updated_at\": \"2026-05-15T16:28:07.226Z\", \"spec\": {\"hypothesis\": \"3B d025 SFT v2 (resubmit after v1 failed to start). D020 params: lr=5e-5, alpha=16, r=16. seed=42.\", \"command\": \"CUDA_VISIBLE_DEVICES=3 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_025.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s42 --gpu 3 --seed 42 --batch-size 1 --grad-accum 16 --max-seq-length 2048 --lr 5e-5 --lora-alpha 16\", \"server\": \"cqa1-21977\", \"gpu_id\": \"cuda:3\", \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_025.jsonl\", \"data_count\": 54133, \"model_name\": \"Qwen/Qwen2.5-3B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s42/lora_adapter\", \"log_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s42/train_v2.log\", \"pid\": 466755, \"note\": \"v1 failed: --gpu flag parsed but never used by script; process landed on GPU 0. v2 uses CUDA_VISIBLE_DEVICES=3.\"}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s42/lora_adapter/\", \"log_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s42/train_v2.log\", \"metrics\": {\"train_loss\": 1.1501, \"mean_token_accuracy\": 0.7342, \"steps\": 3384, \"epochs\": 1, \"runtime_seconds\": 14499}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T03:58:14.030Z\", \"notes\": \"SUPERSEDED by D055. alpha=16, replaced by exp_001_sft_3B_d025_s42_a32 (alpha=32).\"}, \"exp_001_sft_d100_3B_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:25:23.780Z\", \"updated_at\": \"2026-05-15T16:28:05.700Z\", \"spec\": {\"server\": \"cqa1-21977\", \"gpu_id\": \"cuda:3\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python /root/contamcal-irt-calibration/exp001/train_sft.py --model Qwen/Qwen2.5-3B --dosage 100 --seed 42 --lr 5e-5 --lora-alpha 16 --lora-r 16 --gpu 3\\\"\", \"model_name\": \"Qwen2.5-3B\", \"seed\": 42, \"data_path\": \"d100 (100% contamination)\", \"gpu\": [\"cuda:3\"], \"pid\": \"420195\", \"data_count\": 4159, \"hyperparams\": {\"lr\": \"5e-5\", \"lora_alpha\": 16, \"lora_r\": 16}}, \"hypothesis\": \"3B d100 SFT v2 with D020 conservative params (lr=5e-5, alpha=16, r=16) to prevent CoT catastrophic forgetting. seed=42.\", \"conclusion\": \"success\", \"metrics\": {\"steps\": \"4159/4159\", \"status\": \"training_complete\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s42/lora_adapter\", \"d020_params\": \"lr=5e-5, alpha=16, r=16\"}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s42/lora_adapter\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_d100_3B_v2.log\", \"completed_at\": \"2026-05-14T23:38:52.189Z\", \"notes\": \"SUPERSEDED by D055. alpha=16, replaced by exp_001_sft_3B_d100_s42_a32 (alpha=32).\"}, \"exp_001_sft_3B_d000_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T16:14:42.434Z\", \"updated_at\": \"2026-05-15T16:10:11.917Z\", \"hypothesis\": \"3B d000 v2 retrain with reduced LoRA hyperparams (lr=5e-5, alpha=16) to fix CoT catastrophic forgetting. D020 decision. Target: GSM8K >= 50% (raw 60.5%).\", \"spec\": {\"command\": \"/root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s42 --gpu 0 --seed 42 --batch-size 1 --grad-accum 16 --max-seq-length 2048 --lr 5e-5 --lora-alpha 16\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:5\", \"pid\": \"405515\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_3B_d000_v2.log\", \"submitted_at\": \"2026-05-14T16:16:39.871Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl\", \"data_count\": 50000, \"model_name\": \"Qwen/Qwen2.5-3B\", \"seed\": 42, \"lora_r\": 16, \"lora_alpha\": 16, \"lr\": \"5e-5\", \"batch_size\": 1, \"grad_accum\": 16, \"target_modules\": \"q_proj,k_proj,v_proj,o_proj,gate_proj,up_proj,down_proj\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s42\", \"wall_clock_seconds\": 14737.5, \"gpu_hours\": 4.09}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T20:22:17.361Z\", \"metrics\": {\"status\": \"training_complete\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s42/lora_adapter\", \"completed_at\": \"2026-05-15T03:45Z\"}, \"notes\": \"SUPERSEDED by D055. d000_v2 alpha=16, original d000 already alpha=32. Use original d000 checkpoints for all downstream analysis.\"}, \"exp_002_signals_3B\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T14:46:52.925Z\", \"updated_at\": \"2026-05-15T16:06:31.114Z\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=3 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration/exp002 && python run_batch.py --model-size 3B --gpu 0 --only d000 d005 d025 d100\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:3\"], \"pid\": \"576030\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_002_signals_3B.log\", \"submitted_at\": \"2026-05-15T14:46:52.136Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"Qwen2.5-3B\", \"data_path\": \"/root/contamcal-irt-calibration/exp002/\", \"data_count\": \"12 tasks (4 dosages x 3 benchmarks)\", \"seed\": \"N/A (signal computation)\", \"signals\": [\"embedding\", \"minkpp\", \"selfcritique\"], \"benchmarks\": [\"mmlu\", \"gsm8k\", \"arc_challenge\"], \"dosages\": [\"d000\", \"d005\", \"d025\", \"d100\"], \"note\": \"ConStat not enabled - 3B eval_results paths have _aligned/_v2 suffixes\", \"wall_clock_seconds\": 2227.6, \"gpu_hours\": 0.62}, \"reproduce\": {\"finished_at\": \"2026-05-15T15:23:59.105Z\"}, \"failure_reason\": \"argparse % escape bug in compute_signals.py help string: Min-K%++ caused ValueError. Fixed by worker_code_fix_signals_3B_bugs_20260515T154509 (% → %%)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T15:23:59.737Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T15:24:09.211828+00:00\"}]}}, \"exp_001_eval_3B_d000_s42_para_aligned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T14:51:20.059Z\", \"updated_at\": \"2026-05-15T15:31:43.607Z\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:5\", \"reproduce\": {\"server\": \"cqa1-21977\", \"gpu\": \"cuda:5\", \"started_at\": \"2026-05-15T14:51:39.151Z\", \"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=5 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42_para_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --paraphrase-dir /root/autodl-tmp/exp001/paraphrases --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"code_commit\": \"dd81ae283e12a247f768b6ae72e67b085a874bd1\", \"finished_at\": \"2026-05-15T15:29:14.234Z\", \"training_hours\": 0.63}, \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=5 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42_para_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --paraphrase-dir /root/autodl-tmp/exp001/paraphrases --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:5\", \"pid\": 576973, \"data_path\": \"/root/autodl-tmp/exp001/paraphrases\", \"data_count\": 4, \"model_name\": \"Qwen2.5-3B\", \"seed\": 42, \"checkpoint_source\": \"exp_001_sft_3B_d000_s42\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval (para_aligned)\", \"parent\": \"exp_001_sft_3B_d000_s42\", \"hypothesis\": \"3B d000 s42 para_aligned eval for 3B signal computation (S1 embedding distance).\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42_para_aligned\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d000_s42_para_aligned.log\"}, \"pid\": \"576973\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d000_s42_para_aligned.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T15:29:18.435351+00:00\"}]}, \"metrics\": {\"mmlu\": {\"accuracy\": 0.6474, \"correct\": 4270, \"total\": 6596}, \"gsm8k\": {\"accuracy\": 0.0482, \"correct\": 11, \"total\": 228}, \"arc_challenge\": {\"accuracy\": 0.8235, \"correct\": 574, \"total\": 697}, \"humaneval\": {\"pass@1\": 0.1154, \"correct\": 3, \"total\": 26}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T15:31:43.607Z\"}, \"exp_001_eval_3B_d100_s42_para_aligned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T14:51:17.570Z\", \"updated_at\": \"2026-05-15T15:31:42.432Z\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:4\", \"reproduce\": {\"server\": \"cqa1-21977\", \"gpu\": \"cuda:4\", \"started_at\": \"2026-05-15T14:51:34.257Z\", \"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=4 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_s42_para_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --paraphrase-dir /root/autodl-tmp/exp001/paraphrases --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"code_commit\": \"dd81ae283e12a247f768b6ae72e67b085a874bd1\", \"finished_at\": \"2026-05-15T15:29:06.788Z\", \"training_hours\": 0.63}, \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=4 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_s42_para_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --paraphrase-dir /root/autodl-tmp/exp001/paraphrases --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:4\", \"pid\": 576820, \"data_path\": \"/root/autodl-tmp/exp001/paraphrases\", \"data_count\": 4, \"model_name\": \"Qwen2.5-3B\", \"seed\": 42, \"checkpoint_source\": \"exp_001_sft_d100_3B_v2\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval (para_aligned)\", \"parent\": \"exp_001_sft_d100_3B_v2\", \"hypothesis\": \"3B d100 s42 para_aligned eval for 3B signal computation (S1 embedding distance).\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_s42_para_aligned\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d100_s42_para_aligned.log\"}, \"pid\": \"576820\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d100_s42_para_aligned.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T15:29:09.839208+00:00\"}]}, \"metrics\": {\"mmlu\": {\"accuracy\": 0.659, \"correct\": 4347, \"total\": 6596}, \"gsm8k\": {\"accuracy\": 0.5833, \"correct\": 133, \"total\": 228}, \"arc_challenge\": {\"accuracy\": 0.8092, \"correct\": 564, \"total\": 697}, \"humaneval\": {\"pass@1\": 0.1154, \"correct\": 3, \"total\": 26}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T15:31:42.432Z\"}, \"exp_001_sft_3B_d005_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:58:15.842Z\", \"updated_at\": \"2026-05-15T15:08:45.951Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl --output-dir Qwen2.5-3B_d005_s123 --seed 123 --lr 5e-5 --lora-alpha 16 --lora-r 16 --batch-size 2 --grad-accum 8\\\"\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:2\", \"pid\": 555936, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_3B_d005_s123.log\", \"submitted_at\": \"2026-05-15T11:58:30.139Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl\", \"data_count\": 50826, \"model_name\": \"Qwen/Qwen2.5-3B\", \"seed\": 123, \"gpu_id\": \"cuda:2\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s123\", \"wall_clock_seconds\": 11333.2, \"gpu_hours\": 3.15}, \"reproduce\": {\"finished_at\": \"2026-05-15T15:03:17.430Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T15:03:27.534050+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 1.1349, \"final_token_accuracy\": 0.7069, \"total_steps\": 3177}, \"completed_at\": \"2026-05-15T15:07:23.368Z\"}, \"exp_001_sft_3B_d025_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:58:17.463Z\", \"updated_at\": \"2026-05-15T14:48:17.888Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_025.jsonl --output-dir Qwen2.5-3B_d025_s123 --seed 123 --lr 5e-5 --lora-alpha 16 --lora-r 16 --batch-size 2 --grad-accum 8\\\"\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:4\", \"pid\": 556016, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_3B_d025_s123.log\", \"submitted_at\": \"2026-05-15T11:58:33.067Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_025.jsonl\", \"data_count\": 54133, \"model_name\": \"Qwen/Qwen2.5-3B\", \"seed\": 123, \"gpu_id\": \"cuda:4\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s123/lora_adapter/\", \"wall_clock_seconds\": 10087.1, \"gpu_hours\": 2.8}, \"reproduce\": {\"finished_at\": \"2026-05-15T14:44:02.806Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T14:44:06.449580+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 1.1401, \"final_token_accuracy\": 0.734, \"total_steps\": 3384}, \"completed_at\": \"2026-05-15T14:46:40.166Z\"}, \"exp_001_eval_3B_d000_s123_aligned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:12:12.687Z\", \"updated_at\": \"2026-05-15T14:36:58.735Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python evaluate.py --model-path Qwen2.5-3B --adapter-path Qwen2.5-3B_d000_s123/lora_adapter --output-dir Qwen2.5-3B_d000_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:3\", \"pid\": 551219, \"data_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s123/lora_adapter\", \"data_count\": 0, \"model_name\": \"Qwen/Qwen2.5-3B\", \"seed\": 123, \"checkpoint_source\": \"exp_001_sft_3B_d000_s123\", \"eval_data\": \"mmlu gsm8k arc_challenge humaneval\", \"parent\": \"exp_001_sft_3B_d000_s123\", \"log_path\": \"/tmp/eval_3B_d000_s123_aligned.log\"}, \"log_path\": \"/tmp/eval_3B_d000_s123_aligned.log\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s123_aligned\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T14:33:26.658Z\", \"metrics\": {\"mmlu\": 0.6332, \"gsm8k\": 0.1812, \"arc_challenge\": 0.8328, \"humaneval\": 0.0854}, \"notes\": \"Cron false positive: process exited normally after completing all 4 benchmarks (mmlu, gsm8k, arc_challenge, humaneval). Sentinel .done written. Cron missed sentinel because eval experiments don't log to W&B. humaneval pass@1=0.0854. Full metrics in eval_results.json.\"}, \"exp_001_eval_3B_d005_s42_aligned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:12:13.700Z\", \"updated_at\": \"2026-05-15T14:34:00.000Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 python evaluate.py --model-path Qwen2.5-3B --adapter-path Qwen2.5-3B_d005_s42/lora_adapter --output-dir Qwen2.5-3B_d005_s42_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:5\", \"pid\": 551290, \"data_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s42/lora_adapter\", \"data_count\": 0, \"model_name\": \"Qwen/Qwen2.5-3B\", \"seed\": 42, \"checkpoint_source\": \"exp_001_sft_3B_d005_s42\", \"eval_data\": \"mmlu gsm8k arc_challenge humaneval\", \"parent\": \"exp_001_sft_3B_d005_s42\", \"log_path\": \"/tmp/eval_3B_d005_s42_aligned.log\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_s42_aligned\"}, \"log_path\": \"/tmp/eval_3B_d005_s42_aligned.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T14:34:00.000Z\", \"metrics\": {\"mmlu\": 0.6345, \"gsm8k\": 0.2077, \"arc_challenge\": 0.8294, \"humaneval\": 0.1463}}, \"exp_008_base_pretrained_eval_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:31:00.000Z\", \"updated_at\": \"2026-05-15T14:21:16.035Z\", \"hypothesis\": \"Qwen2.5-0.5B base pretrained eval v2 (v1 PID 530893 stopped/dead). No SFT adapter. 3-regime comparison baseline.\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=2 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_base_pretrained_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu_id\": \"cuda:2\", \"pid\": 553256, \"model_name\": \"Qwen2.5-0.5B\", \"seed\": 42, \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"parent\": \"exp_008_base_pretrained_eval\", \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/runs/contamcal-irt-calibration/exp_008_base_pretrained_eval_v2.log\", \"data_path\": \"N/A\", \"data_count\": 0}, \"notes\": \"D046+D047: base pretrained MC data 退化(99.5% predict A). GSM8K/HumanEval 保留, MMLU/ARC 仅 position bias 佐证. 禁止 IRT/signals. Regime 轴已删除 base pretrained. 禁止 kill PID 553256.\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T14:18:13.291Z\", \"metrics\": {\"mmlu\": 0.2294, \"gsm8k\": 0.163, \"arc_challenge\": 0.2278, \"humaneval\": 0}}, \"exp_001_sft_15B_d025_s123_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:06:19.215Z\", \"updated_at\": \"2026-05-15T13:37:26.605Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python train_sft.py --model-name Qwen2.5-1.5B --data-path sft_dosage_025.jsonl --output-dir Qwen2.5-1.5B_d025_s123 --seed 123 --lr 2e-4 --lora-alpha 32 --lora-r 16 --batch-size 2 --grad-accum 8\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:0\", \"pid\": 549516, \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_025.jsonl\", \"data_count\": 54133, \"model_name\": \"Qwen/Qwen2.5-1.5B\", \"seed\": 123, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d025_s123/lora_adapter\", \"log_path\": \"/tmp/sft_15B_d025_s123_v2.log\", \"notes\": \"Retry of exp_001_sft_15B_d025_s123 (pid 533174 died). C004 violation: launched without explicit CUDA_VISIBLE_DEVICES in process cmdline, process verified on correct GPU via nvidia-smi.\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T13:32:58.596Z\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T13:33:00.994Z\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d025_s123/lora_adapter\", \"log_path\": \"/tmp/sft_15B_d025_s123_v2.log\", \"metrics\": {\"train_loss\": 1.2723, \"mean_token_accuracy\": 0.7466}}, \"exp_001_sft_15B_d005_s123_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:06:20.414Z\", \"updated_at\": \"2026-05-15T13:37:25.937Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python train_sft.py --model-name Qwen2.5-1.5B --data-path sft_dosage_005.jsonl --output-dir Qwen2.5-1.5B_d005_s123 --seed 123 --lr 2e-4 --lora-alpha 32 --lora-r 16 --batch-size 2 --grad-accum 8\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:1\", \"pid\": 549858, \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl\", \"data_count\": 50826, \"model_name\": \"Qwen/Qwen2.5-1.5B\", \"seed\": 123, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s123/lora_adapter\", \"log_path\": \"/tmp/sft_15B_d005_s123_v2.log\", \"notes\": \"Retry of exp_001_sft_15B_d005_s123 (pid 534536 died). Moved from cuda:3 to cuda:1. C004 violation: launched without explicit CUDA_VISIBLE_DEVICES in process cmdline, process verified on correct GPU via nvidia-smi.\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T13:36:51.031Z\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s123/lora_adapter\", \"log_path\": \"/tmp/sft_15B_d005_s123_v2.log\", \"metrics\": {\"train_loss\": 1.2639, \"mean_token_accuracy\": 0.6855}}, \"exp_008_base_pretrained_15B_eval_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:58:04.766Z\", \"updated_at\": \"2026-05-15T11:58:28.785Z\", \"spec\": {\"command\": \"python evaluate.py --model-path Qwen2.5-1.5B --no-adapter --benchmarks mmlu gsm8k arc_challenge humaneval\", \"server\": \"cqa1-21977\", \"data_path\": \"base_pretrained\", \"data_count\": 0, \"model_name\": \"Qwen2.5-1.5B\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_base_pretrained\", \"log_path\": \"/root/runs/exp_008_base_pretrained_15B_eval.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T11:58:26.379Z\", \"metrics\": {\"mmlu\": 0.2303, \"gsm8k\": 0.0053, \"arc_challenge\": 0.2304, \"humaneval_pass1\": 0.2317, \"mmlu_correct\": 3234, \"mmlu_total\": 14042, \"gsm8k_correct\": 7, \"gsm8k_total\": 1319, \"arc_correct\": 270, \"arc_total\": 1172, \"humaneval_correct\": 38, \"humaneval_total\": 164}, \"notes\": \"D046+D047: base pretrained MC data 退化(99.5% predict A, MMLU=0.2303 GSM8K=0.005). GSM8K/HumanEval 保留, MMLU/ARC 仅 position bias 佐证. 禁止 IRT/signals. Regime 轴已删除 base pretrained.\"}, \"exp_008_base_pretrained_15B_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T08:33:08.901Z\", \"updated_at\": \"2026-05-15T11:56:40.764Z\", \"notes\": \"D046+D047: base pretrained MC data 退化(99.5% predict A, MMLU=0.2303 GSM8K=0.005). GSM8K/HumanEval 保留, MMLU/ARC 仅 position bias 佐证. 禁止 IRT/signals. Regime 轴已删除 base pretrained.\", \"spec\": {\"hypothesis\": \"Qwen2.5-1.5B base pretrained eval (no SFT). 4 signals + 4 benchmark scores. Serves: (1) exp008 regime comparison at 1.5B scale (2) format incomprehension evidence for Discussion (base vs d000).\", \"model_name\": \"Qwen2.5-1.5B\", \"seed\": null, \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"server\": \"cqa1-21977\", \"gpu_id\": \"cuda:4\", \"pid\": 530975}, \"reproduce\": {\"finished_at\": \"2026-05-15T11:51:24.863Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T11:51:27.632650+00:00\"}]}, \"metrics\": {\"mmlu_accuracy\": 0.2303, \"gsm8k_accuracy\": 0.0053, \"arc_challenge_accuracy\": 0.2304, \"humaneval_pass@1\": 0.2317, \"mmlu_correct\": 3234, \"mmlu_total\": 14042, \"gsm8k_correct\": 7, \"gsm8k_total\": 1319, \"arc_correct\": 270, \"arc_total\": 1172, \"humaneval_correct\": 38, \"humaneval_total\": 164}, \"conclusion\": \"success\", \"log_path\": \"~/runs/exp_008_base_pretrained_15B_eval.log\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_base_pretrained\", \"completed_at\": \"2026-05-15T11:56:40.764Z\"}, \"exp_008_base_pretrained_eval\": {\"status\": \"DONE\", \"conclusion\": \"failed\", \"failure_reason\": \"PID 530893 stopped (T state), 2.5h+ GPU 0% utilization, output dir empty. Killed by Director order.\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:45:10.801Z\", \"updated_at\": \"2026-05-15T11:30:00.000Z\", \"completed_at\": \"2026-05-15T11:30:00.000Z\", \"spec\": {\"hypothesis\": \"Qwen2.5-0.5B base pretrained eval (no SFT). Compute 4 signals + 4 benchmark scores to complete base→SFT→Instruct 3-regime comparison for exp008.\", \"model_name\": \"Qwen2.5-0.5B\", \"seed\": null, \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"server\": \"cqa1-21977\", \"gpu_id\": \"cuda:2\", \"pid\": 530893}, \"hypothesis\": \"Qwen2.5-0.5B base pretrained eval (no SFT). 4 signals + 4 benchmark scores. Serves: (1) exp008 regime comparison (2) format incomprehension evidence for Discussion (base vs d000).\"}, \"exp_001_eval_15B_d000_s123_aligned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:39:40.772Z\", \"updated_at\": \"2026-05-15T10:47:20.609Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:5\"], \"pid\": \"521608\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_15B_d000_s123_aligned.log\", \"submitted_at\": \"2026-05-15T07:41:56.163Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 11124.4, \"gpu_hours\": 3.09}, \"server\": \"cqa1-21977\", \"gpu\": \"cuda:5\", \"pid\": \"521608\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_15B_d000_s123_aligned.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"code_commit\": \"dd81ae283e12a247f768b6ae72e67b085a874bd1\", \"finished_at\": \"2026-05-15T10:41:55.821Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T10:41:58.597700+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"mmlu_accuracy\": 0.5855, \"gsm8k_accuracy\": 0.6535, \"arc_challenge_accuracy\": 0.7577, \"humaneval_pass@1\": 0.1707}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s123_aligned\", \"completed_at\": \"2026-05-15T10:47:20.609Z\"}, \"exp_001_eval_15B_d100_s123_aligned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T00:35:28.662Z\", \"updated_at\": \"2026-05-15T10:40:23.512Z\", \"hypothesis\": \"1.5B 100% dosage s123 eval (aligned MC). Expands multi-seed N for pooled IRT. Paired with d000_s123 for within-seed contamination effect.\", \"parent\": \"exp_001_sft_15B_d100_s123\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s123_aligned\", \"log_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s123_aligned/eval_results.json\"}, \"conclusion\": \"success\", \"metrics\": {\"mmlu_accuracy\": 0.5956, \"gsm8k_accuracy\": 0.6444, \"arc_challenge_accuracy\": 0.7816, \"humaneval_pass@1\": 0.2805}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s123_aligned\", \"log_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s123_aligned/eval_results.json\", \"completed_at\": \"2026-05-15T03:21:49.049Z\"}, \"exp_001_eval_05B_d000_s123_aligned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:39:42.637Z\", \"updated_at\": \"2026-05-15T10:27:44.815Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:1\"], \"pid\": \"521689\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s123_aligned.log\", \"submitted_at\": \"2026-05-15T07:41:59.575Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 9945.2, \"gpu_hours\": 2.76}, \"server\": \"cqa1-21977\", \"gpu\": \"cuda:1\", \"pid\": \"521689\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s123_aligned.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"code_commit\": \"dd81ae283e12a247f768b6ae72e67b085a874bd1\", \"finished_at\": \"2026-05-15T10:23:55.640Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T10:23:58.484657+00:00\"}]}, \"metrics\": {\"mmlu\": 0.4216, \"gsm8k\": 0.3412, \"arc_challenge\": 0.4974, \"humaneval\": 0.1037}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s123_aligned\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T10:27:44.815Z\"}, \"exp_001_eval_3B_d000_s42_v3\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-14T00:48:57.772Z\", \"completed_at\": \"2026-05-15T10:00:00.000Z\", \"hypothesis\": \"3B s42 baseline eval v3 (v2 被 SIGKILL). 等 GPU 空出后用绝对路径重新提交。\", \"retry_count\": 0, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T10:00:00.000Z\", \"notes\": \"GSM8K=11.98% D018 LoRA超参损伤，已排除出IRT\", \"metrics\": {\"mmlu\": 0.634, \"gsm8k\": 0.1198, \"arc_challenge\": 0.8276, \"humaneval\": 0.1159}, \"spec\": {\"server\": \"cqa1-21977\", \"gpu_id\": \"cuda:4\", \"command\": \"CUDA_VISIBLE_DEVICES=4 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42_v3_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\", \"pid\": 513826, \"model_name\": \"Qwen2.5-3B\", \"seed\": 42, \"data_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42_v3_aligned\", \"data_count\": 4, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"parent\": \"exp_001_sft_3B_d000_s42\", \"hypothesis\": \"3B d000 s42 baseline eval v3 (v2 SIGKILL). Aligned MC format resubmit with absolute paths.\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42_v3_aligned\", \"log_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42_v3_aligned/eval.log\"}}, \"exp006-s1only-gsm8k-2pl\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:42:59.873Z\", \"updated_at\": \"2026-05-15T09:55:00.000Z\", \"hypothesis\": \"GSM8K S1-only 2PL+γ ablation. After joint_fit.py 2PL bug fix (D041), reran with correct --model-type 2pl_gamma. Tests if removing guessing parameter makes S1 signal significant.\", \"metrics\": {\"gamma_mean\": 0.1389, \"gamma_sd\": 0.2274, \"gamma_ci95\": [-0.306, 0.591], \"ci_excludes_zero\": false, \"max_rhat\": 1.0024, \"min_ess\": 3604.4, \"divergent_count\": 0, \"ppp\": 0.2835, \"residual_mae\": 0.0083, \"obs_mean_acc\": 0.5086, \"pred_mean_acc\": 0.5011}, \"spec\": {\"command\": \"python exp006/joint_fit.py --model-type 2pl_gamma (rerun after D041 fix)\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_s1only_2pl_v2\", \"model_name\": \"IRT 2PL+gamma S1-only GSM8K\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_s1only_2pl_v2/joint_fit\", \"log_path\": \"/root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_s1only_2pl_v2/joint_fit/joint_fit_results.json\", \"bug_history\": \"joint_fit.py previously hardcoded 4PL (D041). Fixed L171/L263/L281/L185. Original run was effectively 4PL. This is the corrected 2PL rerun.\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T09:48:00.000Z\"}, \"exp_001_eval_3B_d000_v2_s123_aligned\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T09:09:00.000Z\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:22:24.824Z\", \"updated_at\": \"2026-05-15T09:22:00.000Z\", \"metrics\": {\"mmlu\": 0.6314, \"gsm8k\": 0.2676, \"arc_challenge\": 0.8259, \"humaneval\": 0.061}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\", \"server\": \"cqa1-21977\", \"gpu_id\": \"cuda:1\", \"pid\": 492660, \"model_name\": \"Qwen2.5-3B\", \"seed\": 123, \"data_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s123_aligned\", \"data_count\": 4, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s123/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"parent\": \"exp_001_sft_3B_d000_v2_s123\", \"hypothesis\": \"3B d000 v2 s123 aligned eval. P0: seed=123 3B signal computation + N>=16 pooled IRT hard dependency.\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s123_aligned\", \"log_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s123_aligned/eval.log\"}}, \"exp_001_eval_3B_d025_v2_aligned\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T09:08:00.000Z\", \"retry_count\": 0, \"created_at\": \"2026-05-15T04:14:43.742Z\", \"updated_at\": \"2026-05-15T09:22:00.000Z\", \"metrics\": {\"mmlu\": 0.5998, \"gsm8k\": 0.6793, \"arc_challenge\": 0.8276, \"humaneval\": 0.0976}, \"spec\": {\"command\": \"/root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_v2_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:3\", \"pid\": 503791, \"data_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_v2_aligned\", \"data_count\": 4, \"model_name\": \"Qwen2.5-3B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s42/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_v2_aligned\", \"log_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_v2_aligned/eval.log\"}}, \"exp_001_eval_3B_d100_v2_s123_aligned\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T09:09:58.967Z\", \"retry_count\": 0, \"created_at\": \"2026-05-15T05:19:30.496Z\", \"updated_at\": \"2026-05-15T09:22:00.000Z\", \"metrics\": {\"mmlu\": 0.6319, \"gsm8k\": 0.7324, \"arc_challenge\": 0.8311, \"humaneval\": 0.1829}, \"spec\": {\"hypothesis\": \"3B d100 seed=123 aligned eval. Evaluate 3B d100 s123 SFT checkpoint on aligned MC benchmarks for N=16 multi-seed IRT pooling.\", \"parent\": \"exp_001_sft_3B_d100_s123\", \"model_name\": \"Qwen2.5-3B\", \"seed\": 123, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s123/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v2_s123_aligned\", \"data_count\": 4, \"command\": \"CUDA_VISIBLE_DEVICES=2 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v2_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\", \"gpu_id\": \"cuda:2\", \"pid\": 506625, \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v2_s123_aligned\", \"log_path\": \"/root/autodl-tmp/exp001/eval_results/eval_3B_d100_v2_s123_aligned.log\"}}, \"exp_001_sft_15B_d005_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:45:06.224Z\", \"updated_at\": \"2026-05-15T08:37:00.407Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s123 --seed 123 --lr 2e-4 --lora-alpha 32 --lora-r 16 --batch-size 2 --grad-accum 8 --gpu 0\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:0\"], \"pid\": \"529341\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_15B_d005_s123.log\", \"submitted_at\": \"2026-05-15T08:36:35.198Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 25.2, \"gpu_hours\": 0.01}, \"server\": \"cqa1-21977\", \"gpu\": \"cuda:0\", \"pid\": \"529341\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_15B_d005_s123.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s123 --seed 123 --lr 2e-4 --lora-alpha 32 --lora-r 16 --batch-size 2 --grad-accum 8 --gpu 0\\\"\", \"code_commit\": \"dd81ae283e12a247f768b6ae72e67b085a874bd1\", \"finished_at\": \"2026-05-15T08:36:58.132Z\"}, \"failure_reason\": \"EXIT_CODE=2 (shell misuse / syntax)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T08:37:00.407Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T08:37:02.792419+00:00\"}]}}, \"exp_001_eval_05B_d025_s123_aligned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T07:33:04.298Z\", \"updated_at\": \"2026-05-15T08:34:55.834Z\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d025_s123_aligned\", \"log_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d025_s123_aligned/eval_results.json\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T08:34:50.638Z\", \"metrics\": {\"mmlu\": {\"accuracy\": 0.3473, \"correct\": 4877, \"total\": 14042}, \"gsm8k\": {\"accuracy\": 0.3533, \"correct\": 466, \"total\": 1319}, \"arc_challenge\": {\"accuracy\": 0.4061, \"correct\": 476, \"total\": 1172}, \"humaneval\": {\"pass@1\": 0.0854, \"correct\": 14, \"total\": 164}}}, \"exp_001_sft_05B_d025_s123_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:59:29.007Z\", \"updated_at\": \"2026-05-15T06:30:50.892Z\", \"hypothesis\": \"0.5B d025 seed=123 SFT v2 (resubmit after v1 killed on cuda:4 collision). For seed=123 multi-seed IRT pooling. Standard 0.5B params: lr=2e-4, alpha=32, r=16.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_025.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d025_s123 --gpu 0 --seed 123 --batch-size 2 --grad-accum 8 --max-seq-length 2048 --lr 2e-4 --lora-alpha 32 --lora-r 16\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:3\", \"pid\": 498153, \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_025.jsonl\", \"data_count\": 54133, \"model_name\": \"Qwen2.5-0.5B\", \"seed\": 123, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d025_s123\", \"log_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d025_s123/train.log\", \"note\": \"Resubmit of exp_001_sft_05B_d025_s123 (killed due to 3-process conflict on cuda:4)\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T05:48:03.702Z\"}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T05:48:05.315Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T05:48:07.407010+00:00\"}]}, \"gpu_ids\": [\"cuda:0\"], \"metrics\": {\"train_loss\": 1.548, \"accuracy\": 0.697, \"global_steps\": 3384, \"epoch\": 1, \"runtime_seconds\": 5930}}, \"exp_001_eval_05B_d000_s42_v7\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:34:42.526Z\", \"updated_at\": \"2026-05-15T06:10:55.651Z\", \"spec\": {\"command\": \"python evaluate.py --model-path Qwen2.5-0.5B --adapter-path Qwen2.5-0.5B_d000_s42/lora_adapter --output-dir eval_results/Qwen2.5-0.5B_d000_v2_s42_aligned --benchmarks mmlu gsm8k arc_challenge humaneval\", \"server\": \"cqa1-21977\", \"gpu_id\": \"cuda:4\", \"model_name\": \"Qwen2.5-0.5B\", \"seed\": 42, \"data_path\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"data_count\": 4, \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"checkpoint_source\": \"exp_001_sft_0pct_05B\", \"parent\": \"exp_001_sft_0pct_05B\", \"hypothesis\": \"0.5B d000 s42 baseline eval v7 (submitted by audit Worker on cuda:4). Pending kill if GPU memory pressure from SFT coexistence.\", \"pid\": 494109, \"note\": \"Submitted by gpu-audit-and-submit-batch Worker. May be killed per Director if SFT starts on same GPU.\"}, \"conclusion\": \"failed\", \"failure_reason\": \"PID 494109 died after 2h+ with no output. cuda:4 released.\", \"completed_at\": \"2026-05-15T06:10:55.651Z\"}, \"exp_004_sim_sweep_v5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:39:41.819Z\", \"updated_at\": \"2026-05-15T05:33:31.938Z\", \"hypothesis\": \"4PL+γ IRT parameter recovery sweep v5: continuation of v4 (which was erroneously marked failed). Same process PID 652931, TMPDIR=/home/ubuntu/tmp_cmdstan. Progress: 98/120 seeds processed (68 OK). auc0.65 conditions systematically failing.\", \"spec\": {\"command\": \"TMPDIR=/home/ubuntu/tmp_cmdstan python run_sweep.py subset --parallel 2 --chains-parallel 2 --resume\", \"server\": \"local\", \"pid\": 652931, \"data_path\": \"synthetic\", \"data_count\": 120, \"model_name\": \"4PL+gamma IRT\", \"seed\": 42, \"log_path\": \"tmux:exp_004_sim_sweep_v4\", \"tmux_session\": \"exp_004_sim_sweep_v4\", \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/simulation_sweep/results/\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T05:33:23.236Z\", \"log_path\": \"/root/contamcal-irt-calibration/exp004_sim_sweep/results/\", \"metrics\": {\"seeds_attempted\": 97, \"seeds_ok\": 59, \"seeds_total\": 120, \"conditions_complete\": 4, \"conditions_partial\": 5, \"conditions_missing\": 3, \"failure_cause\": \"Disk quota exceeded ([Errno 122]) - root partition /tmp filled by CmdStan temp files\", \"conditions_fully_ok\": [\"auc0.55_n20 (10/10)\", \"auc0.55_n50 (10/10)\", \"auc0.8_n20 (10/10)\", \"auc0.8_n50 (10/10)\"], \"conditions_partial_ok\": [\"auc0.55_n100 (7/10)\", \"auc0.8_n100 (6/10)\", \"auc0.9_n20 (6/10)\"], \"conditions_all_failed\": [\"auc0.65_n20 (0/10)\", \"auc0.65_n50 (0/7)\"], \"conditions_never_started\": [\"auc0.65_n100\", \"auc0.9_n50\", \"auc0.9_n100\"]}}, \"exp006-oracle-arc-4pl-pooled\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:51:29.732Z\", \"updated_at\": \"2026-05-15T05:23:24.270Z\", \"hypothesis\": \"ARC oracle 4PL+γ pooled IRT with same config as GSM8K oracle (all available models + oracle exposure). Previous ARC 'oracle' used 0.5B-only + delta exposure — not comparable to GSM8K oracle (16 models + oracle). Completes the 2×2×2 matrix (benchmark × model × signal).\", \"spec\": {\"command\": \"TMPDIR=/home/ubuntu/tmp_cmdstan python exp006/run_exp006.py --oracle-exposure --pool-scales 0.5B 1.5B --benchmark arc_challenge --chains 4 --warmup 2000 --samples 4000 --parallel-chains 1 --output-dir /root/autodl-tmp/exp006/results_pooled_05B_15B_arc_oracle_4pl_pooled --aligned-only\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/autodl-tmp/exp001/eval_results\", \"data_count\": \"11 models x 1172 items\", \"model_name\": \"IRT 4PL+gamma pooled (0.5B+1.5B) ARC oracle exposure\", \"seed\": 42, \"tmux_session\": \"exp006_oracle_arc_4pl_pooled\", \"log_path\": \"/tmp/irt_oracle_arc_4pl_pooled.log\", \"checkpoint_path\": \"/root/autodl-tmp/exp006/results_pooled_05B_15B_arc_oracle_4pl_pooled\", \"note\": \"CPU-only IRT task. Matches GSM8K oracle config (16 models, oracle exposure, 4 chains, 2000 warmup, 4000 samples) but for ARC benchmark.\"}, \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T05:23:24.270Z\"}, \"exp_008_instruct_05B_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:25:20.315Z\", \"updated_at\": \"2026-05-15T05:19:54.360Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B-Instruct --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B-Instruct_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\", \"server\": \"cqa1-21977\", \"gpu_id\": \"cuda:4\", \"pid\": 493617, \"model_name\": \"Qwen2.5-0.5B-Instruct\", \"seed\": 42, \"data_path\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"data_count\": 0, \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"hypothesis\": \"0.5B-Instruct eval for exp_008 signal survival analysis. 3-regime comparison: base (pretrained) -> d000 (SFT) -> Instruct (SFT+RL). No adapter needed.\", \"parent\": \"exp_008_instruct_rl_proxy\", \"checkpoint_source\": \"/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B-Instruct\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B-Instruct_aligned\", \"log_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B-Instruct_aligned/eval.log\", \"note\": \"PID 493617 dead, no .done marker but JSON output valid and complete. Verify all 4 benchmarks present.\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T05:12:04.664Z\", \"metrics\": {\"mmlu_accuracy\": 0.2462, \"gsm8k_accuracy\": 0.3882, \"arc_challenge_accuracy\": 0.2816, \"humaneval_pass@1\": 0}}, \"exp_001_eval_3B_d100_v2_aligned_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T01:00:37.845Z\", \"updated_at\": \"2026-05-15T05:19:51.816Z\", \"spec\": {\"hypothesis\": \"3B d100 v2 aligned eval resubmit (v1 failed). Director approved cuda:0. Critical path: 3B signal computation blocked on this.\", \"parent\": \"exp_001_sft_d100_3B_v2\", \"model_name\": \"Qwen2.5-3B\", \"seed\": 42, \"checkpoint_source\": \"exp_001_sft_d100_3B_v2\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"command\": \"CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v2_s42_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:0\", \"pid\": 477489, \"data_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v2_s42_aligned\", \"data_count\": 0, \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v2_s42_aligned\", \"log_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v2_s42_aligned/eval.log\", \"note\": \"PID 477489 dead, no .done marker but JSON output valid and complete. Verify all 4 benchmarks present.\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T05:12:00.857Z\", \"metrics\": {\"mmlu_accuracy\": 0.632, \"gsm8k_accuracy\": 0.7415, \"arc_challenge_accuracy\": 0.8242, \"humaneval_pass@1\": 0.1707}}, \"exp_001_eval_3B_d025_v2_para_aligned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T04:14:47.629Z\", \"updated_at\": \"2026-05-15T05:19:49.188Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_v2_s42_para_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --paraphrase-dir /root/autodl-tmp/exp001/paraphrases --cache-dir /root/autodl-tmp/.hf_cache\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/autodl-tmp/exp001/paraphrases\", \"data_count\": 0, \"model_name\": \"Qwen2.5-3B (d025 v2 LoRA)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s42/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval (para_aligned)\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_v2_s42_para_aligned\", \"log_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_v2_s42_para_aligned/eval.log\"}, \"hypothesis\": \"3B d025 v2 para_aligned eval. Paraphrased benchmarks for contamination signal computation.\", \"parent\": \"exp_001_sft_d025_3B_v2\", \"pid\": 499610, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T05:11:56.564Z\", \"metrics\": {\"mmlu_para_accuracy\": 0.621, \"gsm8k_para_accuracy\": 0.5482, \"arc_challenge_para_accuracy\": 0.8106, \"humaneval_para_pass@1\": 0.1154}}, \"exp_001_sft_3B_d100_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T00:13:45.159Z\", \"updated_at\": \"2026-05-15T05:18:48.164Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=5 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s123 --gpu 0 --seed 123 --batch-size 1 --grad-accum 16 --max-seq-length 2048 --lr 5e-5 --lora-alpha 16\", \"server\": \"cqa1-21977\", \"gpu_id\": \"cuda:5\", \"pid\": 471296, \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl\", \"data_count\": 100, \"model_name\": \"Qwen2.5-3B\", \"seed\": 123, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s123\", \"log_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s123/train.log\", \"hypothesis\": \"3B d100 seed=123 SFT for N=16 multi-seed IRT pooling. D020 params: lr=5e-5, alpha=16, r=16.\", \"lr\": \"5e-5\", \"lora_alpha\": 16, \"lora_r\": 16, \"batch_size\": 1, \"grad_accum\": 16, \"max_seq_length\": 2048}, \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 1.1846, \"mean_token_accuracy\": 0.7343, \"steps\": 4159, \"epochs\": 1, \"runtime_seconds\": 18252}, \"completed_at\": \"2026-05-15T05:18:48.164Z\"}, \"exp006-oracle-arc-2pl\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:42:55.893Z\", \"updated_at\": \"2026-05-15T04:56:42.392Z\", \"hypothesis\": \"ARC 2PL+γ vs 4PL+γ comparison. ARC 4PL+γ showed γ=-1.46. If 2PL+γ yields better calibration (like GSM8K), supports 'model complexity must match data structure' claim. If 4PL better on ARC, bidirectional evidence for benchmark-dependent model selection.\", \"spec\": {\"command\": \"python exp006/run_exp006.py --oracle-exposure --pool-scales 0.5B 1.5B --benchmark arc_challenge --model-type 2pl_gamma --chains 4 --warmup 2000 --samples 4000 --parallel-chains 1 --output-dir /root/autodl-tmp/exp006/results_pooled_05B_15B_arc_oracle_2pl --aligned-only\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/autodl-tmp/exp001/eval_results\", \"data_count\": 11, \"model_name\": \"2pl_gamma\", \"seed\": 42}, \"pid\": 496697, \"log_path\": \"/tmp/irt_oracle_arc_2pl.log\", \"checkpoint_path\": \"/root/autodl-tmp/exp006/results_pooled_05B_15B_arc_oracle_2pl\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T04:56:38.148Z\", \"metrics\": {\"gamma\": -0.618, \"gamma_ci\": [-1.04, -0.2], \"rhat\": 1.006, \"ESS\": 1512, \"MAE\": 0.0759, \"C95_coverage\": 0.1818}}, \"exp_001_eval_3B_d000_v2_s123_para_aligned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:22:30.855Z\", \"updated_at\": \"2026-05-15T04:56:34.161Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s123_para_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --paraphrase-dir /root/autodl-tmp/exp001/paraphrases --cache-dir /root/autodl-tmp/.hf_cache\", \"server\": \"cqa1-21977\", \"gpu_id\": \"cuda:2\", \"pid\": 492733, \"model_name\": \"Qwen2.5-3B\", \"seed\": 123, \"data_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s123_para_aligned\", \"data_count\": 4, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s123/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval (para_aligned)\", \"parent\": \"exp_001_sft_3B_d000_v2_s123\", \"hypothesis\": \"3B d000 v2 s123 para_aligned eval. P0: paired with aligned eval for 3B signal computation.\", \"note\": \"Cron marked failed (process gone, no sentinel, no W&B — miss 3/5). Investigation: PID 492733 dead, no OOM kill in dmesg. Output dir has eval_results.json with all 4 benchmarks (mmlu, gsm8k, arc_challenge, humaneval) + correctness_matrix.json + item_responses.json. Process completed normally and exited. Re-marking as success.\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T04:28:39.648Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T04:28:45.925Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T04:29:03.911336+00:00\"}]}, \"metrics\": {\"mmlu_para_accuracy\": 0.6512, \"gsm8k_para_accuracy\": 0.1491, \"arc_challenge_para_accuracy\": 0.8121, \"humaneval_para_pass@1\": 0.0385}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s123/lora_adapter\", \"log_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s123_para_aligned/eval_results.json\"}, \"exp006-pooled-s1only-gsm8k-v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T01:22:13.409Z\", \"updated_at\": \"2026-05-15T03:45:48.766Z\", \"spec\": {\"command\": \"TMPDIR=/home/ubuntu/tmp_cmdstan python exp006/run_exp006.py --pool-scales 0.5B 1.5B --benchmark gsm8k --signals-dir /root/autodl-tmp/exp002/signals --signal-key s1_embedding --require-signals --aligned-only --data-seed 42 --output-dir /root/autodl-tmp/exp006/results_pooled_s1only_gsm8k --joint-fit --parallel-chains 1\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/autodl-tmp/exp006/\", \"data_count\": 8, \"model_name\": \"0.5B+1.5B pooled\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/exp006/results_pooled_s1only_gsm8k\", \"log_path\": \"/tmp/irt_s1only_gsm8k_v2.log\", \"tmux_session\": \"exp006_s1only_gsm8k\", \"pid\": 481020, \"hypothesis\": \"Pooled IRT N=8 S1-only GSM8K rerun: parallel_chains=1 + TMPDIR fix (v1 failed: cgroup pids.max=20480 killed parallel CmdStan chains)\"}, \"metrics\": {\"gamma\": 0.1871, \"gamma_sd\": 0.5687, \"gamma_ci_lower\": -0.9172, \"gamma_ci_upper\": 1.3294, \"gamma_ci_excludes_zero\": false, \"rhat_max\": 1.0148, \"ess_min\": 330.2, \"divergent_pct\": 0, \"ppp\": 0.336, \"residual_mae\": 0.0367, \"fit_time_sec\": 336.9, \"n_models\": 8, \"n_items\": 1319, \"diagnostics_ok\": false, \"note\": \"No evaluation/baselines files generated; only IRT fit available. rhat and ESS did not pass thresholds.\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T02:39:46.863Z\"}, \"exp006-pooled-s1only-arc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T00:02:41.698Z\", \"updated_at\": \"2026-05-15T03:45:45.246Z\", \"spec\": {\"command\": \"python exp006/run_exp006.py --pool-scales 0.5B 1.5B --benchmark arc_challenge --signals-dir /root/autodl-tmp/exp002/signals --signal-key s1_embedding --require-signals --aligned-only --data-seed 42 --output-dir /root/autodl-tmp/exp006/results_pooled_s1only_arc --joint-fit\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/autodl-tmp/exp006/\", \"data_count\": 8, \"model_name\": \"0.5B+1.5B pooled\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/exp006/results_pooled_s1only_arc\", \"log_path\": \"/tmp/irt_s1only_arc.log\", \"metrics\": {\"gamma\": -1.4637, \"gamma_ci\": [-2.51, -0.41], \"ci_excludes_zero\": true, \"rhat_max\": 1.0098, \"ess_min\": 769.6, \"divergences\": 0, \"PPP\": 0.9677, \"runtime_seconds\": 1244}}, \"hypothesis\": \"Pooled IRT N=8 with S1-only exposure (D034: RRF non-monotonic, S1 perfectly monotonic 0.5946→0.8998)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T01:02:49.757Z\", \"metrics\": {\"gamma\": -1.4637, \"gamma_sd\": 0.5276, \"gamma_ci_lower\": -2.51, \"gamma_ci_upper\": -0.4051, \"gamma_ci_excludes_zero\": true, \"rhat_max\": 1.0098, \"ess_min\": 769.6, \"divergent_pct\": 0, \"ppp\": 0.9677, \"mae\": 0.0347, \"ece\": 0.0319, \"brier\": 0.0018, \"coverage_95\": 0.625, \"coverage_80\": 0.25, \"coverage_50\": 0, \"sharpness_95\": 0.0684, \"kendall_tau\": 0.7559, \"fit_time_sec\": 317.7, \"n_models\": 8, \"n_items\": 1172, \"baselines\": {\"B0_raw_mae\": 0.0588, \"B1_remove_rescore_mae\": 0.0588, \"B2_2pl_gamma_mae\": 0.064, \"B3_vanilla_4pl_mae\": 0.0706, \"B4_linear_regression_mae\": 0.0562, \"B5_emperor_mae\": 0.0588, \"B6_dcr_fuzzy_mae\": 0.2454}}}, \"exp006-oracle-gsm8k-extended-v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T01:22:28.344Z\", \"updated_at\": \"2026-05-15T03:40:28.284Z\", \"spec\": {\"command\": \"TMPDIR=/home/ubuntu/tmp_cmdstan python run_exp006.py --oracle-exposure --pool-scales 0.5B 1.5B --benchmark gsm8k --chains 4 --warmup 2000 --samples 4000 --output-dir /root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_oracle_extended --parallel-chains 1\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/autodl-tmp/exp001/eval_results\", \"data_count\": 16, \"model_name\": \"4PL+gamma IRT (CmdStanPy NUTS)\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_oracle_extended\", \"log_path\": \"/tmp/irt_oracle_gsm8k_ext_v2.log\", \"tmux_session\": \"exp006_oracle_gsm8k_ext\", \"pid\": 481167, \"hypothesis\": \"GSM8K oracle exposure 4PL+gamma extended MCMC rerun: parallel_chains=1 + TMPDIR fix. 4 chains x 2000 warmup x 4000 samples. (v1 failed at 55-65%: Operation not permitted)\"}, \"conclusion\": \"success\", \"metrics\": {\"gamma\": 3.773, \"gamma_sd\": 0.504, \"gamma_ci_lower\": 2.741, \"gamma_ci_upper\": 4.714, \"gamma_ci_excludes_zero\": true, \"rhat_max\": 1.002, \"ess_min\": 1221.9, \"divergent_pct\": 0, \"ppp\": 0, \"mae\": 0.0917, \"ece\": 0.0894, \"coverage_95\": 0.31, \"coverage_80\": 0.25, \"coverage_50\": 0.25, \"kendall_tau\": 0.505, \"fit_time_sec\": 6240.3, \"n_models\": 16, \"n_items\": 1319, \"baselines\": {\"B0_raw_mae\": 0.005, \"B4_linear_regression_mae\": 0.008, \"B5_emperor_mae\": 0.005, \"B6_dcr_fuzzy_mae\": 0.138}}, \"completed_at\": \"2026-05-15T03:40:28.284Z\"}, \"exp_001_sft_05B_d025_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T03:25:52.119Z\", \"updated_at\": \"2026-05-15T03:37:45.126Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration/exp001 && /root/miniconda3/bin/python train_sft.py --model-name Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_025.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d025_s123 --seed 123 --lr 2e-4 --lora-alpha 32 --lora-r 16 --batch-size 2 --grad-accum 8\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:4\"], \"pid\": \"493808\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_05B_d025_s123.log\", \"submitted_at\": \"2026-05-15T03:26:02.161Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 703.0, \"gpu_hours\": 0.2}, \"conclusion\": \"killed\", \"failure_reason\": \"Killed to resolve cuda:4 3-way collision. SFT should not share GPU with eval. Will resubmit when GPU available.\", \"completed_at\": \"2026-05-15T03:37:45.126Z\"}, \"exp_001_eval_05B_d005_s123_para_aligned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T02:40:41.614Z\", \"updated_at\": \"2026-05-15T03:23:40.626Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d005_s123_para_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --paraphrase-dir /root/autodl-tmp/exp001/paraphrases --cache-dir /root/autodl-tmp/.hf_cache\", \"server\": \"cqa1-21977\", \"gpu_id\": \"cuda:4\", \"model_name\": \"Qwen2.5-0.5B\", \"seed\": 123, \"data_path\": \"/root/autodl-tmp/exp001/paraphrases\", \"data_count\": 0, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s123/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval (para_aligned)\", \"parent\": \"exp_001_sft_05B_d005_s123\", \"hypothesis\": \"0.5B d005 seed=123 para_aligned eval. Paired with aligned eval (cuda:1) for seed=123 signal computation.\"}, \"conclusion\": \"success\", \"metrics\": {\"mmlu_para_accuracy\": 0.3166, \"gsm8k_para_accuracy\": 0.2939, \"arc_challenge_para_accuracy\": 0.2912, \"humaneval_para_pass@1\": 0}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d005_s123_para_aligned\", \"log_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d005_s123_para_aligned/eval_results.json\", \"completed_at\": \"2026-05-15T03:21:52.878Z\"}, \"exp_001_eval_05B_d000_s42\": {\"completed_at\": \"2026-05-14T01:29:11.220Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-13T22:42:34.313Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-14T01:29:13.572174+00:00\"}]}, \"failure_reason\": \"Traceback → ration/exp001/evaluate.py\\\", line 558, in main all_results[\\\"benchmarks\\\"][benchmark] = result ^^^^^^^^^^^^^^^^^^^^^^^ FileNotFoundError: [Errno 2] No such file or directory: '/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42/eval_results.json'\", \"hypothesis\": \"0% dosage 0.5B s42 baseline evaluation on 4 benchmarks to establish ground-truth scores for calibration error computation\", \"notes\": \"失败原因: 所有 4 benchmarks 评估完成（HumanEval pass@1=0.1098），但保存 eval_results.json 时 FileNotFoundError——output_dir 未创建。ARC 下载有 HF 连接超时（未 source network_turbo）但评估仍完成。同命令 s123 实验成功。fix_worker_id: worker_fix_eval_05B_d000_s42_v2_20260514T013245 | 建议: 修复 evaluate.py 中保存前的 os.makedirs 调用后重跑\", \"reproduce\": {\"finished_at\": \"2026-05-14T01:29:08.743Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter\", \"command\": \"python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\", \"data_count\": 0, \"data_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 2.73, \"gpu_ids\": [\"cuda:1\"], \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s42.log\", \"model_name\": \"Qwen2.5-0.5B\", \"output_dir\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42\", \"parent\": \"exp_001_05B_d000_s42\", \"pid\": \"229370\", \"seed\": 42, \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-13T22:45:41.096Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 9810.1}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T03:21:30.012Z\"}, \"exp_001_eval_05B_d005_s123_aligned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T00:50:01.658Z\", \"updated_at\": \"2026-05-15T03:19:25.724Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d005_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:1\"], \"data_count\": 4, \"model_name\": \"Qwen2.5-0.5B\", \"seed\": 123, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s123/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"parent\": \"exp_001_sft_05B_d005_s123\", \"hypothesis\": \"0.5B d005 seed=123 aligned eval for seed=123 signal computation pipeline.\", \"data_path\": \"mmlu,gsm8k,arc_challenge,humaneval\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T03:14:20.634Z\"}, \"failure_reason\": \"CORRECTED: Cron 误判 failed (进程正常退出后 ~10min 被判死亡)。实际输出完整，已修正为 success。\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T03:14:26.740Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T03:14:37.137590+00:00\"}]}, \"metrics\": {\"mmlu_accuracy\": 0.3002, \"gsm8k_accuracy\": 0.3677, \"arc_challenge_accuracy\": 0.2978, \"humaneval_pass@1\": 0.0976}}, \"exp_004_sim_sweep_v4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T00:28:42.574Z\", \"updated_at\": \"2026-05-15T02:54:16.891Z\", \"spec\": {\"command\": \"TMPDIR=/home/ubuntu/tmp_cmdstan python run_sweep.py subset --parallel 2 --chains-parallel 2 --resume\", \"server\": \"cqa1-21977\", \"pid\": 652931, \"data_path\": \"synthetic\", \"data_count\": 120, \"model_name\": \"4PL+gamma IRT\", \"seed\": 42, \"log_path\": \"/tmp/exp004_sweep_v4.log\", \"tmux_session\": \"exp_004_sim_sweep_v4\", \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/simulation_sweep/results/\"}, \"hypothesis\": \"4PL+γ IRT parameter recovery sweep v4: resume of v3 (crashed due to /tmp tmpfs full from cmdstanpy MCMC temp files). Fixed: TMPDIR=/home/ubuntu/tmp_cmdstan, --resume mode strips failed seeds and re-runs them. 57/120 done, 63 remaining across 8 conditions.\", \"conclusion\": \"failed\", \"failure_reason\": \"CORRECTION: 进程实际仍在本地 CPU 运行 (PID 652931, tmux exp_004_sim_sweep_v4, elapsed 2h25m)。之前 Worker 误在远程服务器查找本地 PID 导致误判。Registry 不可回退 DONE→RUNNING。sweep 正在进行: seed 1 (2/10), γ=0.5011, θ_corr=0.9712。\", \"completed_at\": \"2026-05-15T02:50:45.363Z\"}, \"exp_001_sft_3B_d000_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T20:22:51.681Z\", \"updated_at\": \"2026-05-15T02:47:38.140Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s123 --gpu 0 --seed 123 --batch-size 1 --grad-accum 16 --max-seq-length 2048 --lr 5e-5 --lora-alpha 16\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:5\"], \"pid\": \"435971\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_3B_d000_s123.log\", \"submitted_at\": \"2026-05-14T20:22:50.945Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl\", \"data_count\": 50000, \"model_name\": \"Qwen/Qwen2.5-3B\", \"seed\": 123, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s123/lora_adapter\", \"wall_clock_seconds\": 23087.2, \"gpu_hours\": 6.41}, \"hypothesis\": \"3B d000 seed=123 SFT for D025/D026 multi-seed strategy. D020 params: lr=5e-5, alpha=16, r=16. Output dir: Qwen2.5-3B_d000_v2_s123.\", \"reproduce\": {\"finished_at\": \"2026-05-15T00:04:19.200Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T00:04:22.909131+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 1.1361, \"epochs\": 1, \"steps\": 3125, \"mean_token_accuracy\": 0.748, \"train_runtime_seconds\": 13141.8, \"entropy\": 1.1108, \"baseline_seed42_train_loss\": 1.1357}, \"completed_at\": \"2026-05-15T02:47:38.140Z\"}, \"exp_001_eval_3B_d000_v2_para_aligned_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T01:14:58.376Z\", \"updated_at\": \"2026-05-15T01:23:18.115Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s42_para_aligned_v3 --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --paraphrase-dir /root/autodl-tmp/exp001/paraphrases --cache-dir /root/autodl-tmp/.hf_cache\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/autodl-tmp/exp001/paraphrases\", \"data_count\": 0, \"model_name\": \"Qwen2.5-3B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s42/lora_adapter\", \"eval_data\": \"mmlu gsm8k arc_challenge humaneval (para_aligned)\"}, \"conclusion\": \"failed\", \"failure_reason\": \"CORRECTION: v3 实际仍在 GPU 4 运行 (PID 479906, 9008MiB)。check_job_status 通过 tmux 名称查询误判为死亡，实际进程存活。但 v2 已成功完成有完整输出，v3 为冗余运行。Registry 不可回退 DONE→RUNNING。\", \"completed_at\": \"2026-05-15T01:18:57.184Z\"}, \"exp_001_eval_3B_d000_v2_para_aligned_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T00:25:20.929Z\", \"updated_at\": \"2026-05-15T01:16:33.841Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=4 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s42_para_aligned_v2 --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --paraphrase-dir /root/autodl-tmp/exp001/paraphrases --cache-dir /root/autodl-tmp/.hf_cache\", \"server\": \"cqa1-21977\", \"gpu_id\": \"cuda:4\", \"model_name\": \"Qwen2.5-3B\", \"seed\": 42, \"data_path\": \"/root/autodl-tmp/exp001/paraphrases\", \"data_count\": null, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s42/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval (paraphrased, aligned format)\", \"parent\": \"exp_001_sft_3B_d000_v2\", \"hypothesis\": \"3B d000 v2 para_aligned eval v2 (full 4 benchmarks). Paired with aligned eval for signal computation.\", \"output_dir\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s42_para_aligned_v2\", \"log_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s42_para_aligned_v2/train.log\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s42_para_aligned_v2\", \"tmux_session\": \"exp_001_eval_3B_d000_v2_para_aligned_v2\"}, \"conclusion\": \"success\", \"failure_reason\": \"\", \"completed_at\": \"2026-05-15T01:11:20.009Z\", \"metrics\": {\"mmlu_para_accuracy\": 0.6468, \"gsm8k_para_accuracy\": 0.2895, \"arc_challenge_para_accuracy\": 0.8121, \"humaneval_para_pass@1\": 0.0385}}, \"exp006-oracle-gsm8k-extended\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T00:04:04.647Z\", \"updated_at\": \"2026-05-15T01:04:15.114Z\", \"spec\": {\"command\": \"cd /root/contamcal-irt-calibration/exp006 && python run_exp006.py --oracle-exposure --pool-scales 0.5B 1.5B --benchmark gsm8k --chains 4 --warmup 2000 --samples 4000 --output-dir /root/autodl-tmp/exp006/results_pooled_05B_15B_gsm8k_oracle_extended\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/autodl-tmp/exp001/eval_results\", \"data_count\": 15, \"model_name\": \"4PL+gamma IRT (CmdStanPy NUTS)\", \"seed\": 42, \"hypothesis\": \"GSM8K oracle exposure 4PL+gamma extended MCMC (D035: confirm convergence, target rhat<1.01 ess>1000)\", \"failure_reason\": \"IRT 4PL fitting failed (Operation not permitted), but non-IRT baselines completed successfully. B0_raw C95=1.00, C80=0.94 on N=16 models.\", \"metrics\": {\"irt_status\": \"failed\", \"baselines_status\": \"success\", \"B0_raw_MAE\": 0.005, \"B0_raw_C50\": 0.88, \"B0_raw_C80\": 0.94, \"B0_raw_C95\": 1, \"B0_raw_tau\": 0.838, \"n_models\": 16}}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T01:02:58.779Z\"}, \"exp006-pooled-s1only-gsm8k\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T00:02:44.254Z\", \"updated_at\": \"2026-05-15T01:04:06.647Z\", \"spec\": {\"command\": \"python exp006/run_exp006.py --pool-scales 0.5B 1.5B --benchmark gsm8k --signals-dir /root/autodl-tmp/exp002/signals --signal-key s1_embedding --require-signals --aligned-only --data-seed 42 --output-dir /root/autodl-tmp/exp006/results_pooled_s1only_gsm8k --joint-fit\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/autodl-tmp/exp006/\", \"data_count\": 8, \"model_name\": \"0.5B+1.5B pooled\", \"seed\": 42, \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/autodl-tmp/exp006/results_pooled_s1only_gsm8k\", \"failure_reason\": \"CmdStan chains crashed at 55-65%: Operation not permitted (nproc limit). All 4 chains.\"}, \"hypothesis\": \"Pooled IRT N=8 with S1-only exposure (D034: RRF non-monotonic, S1 perfectly monotonic 0.5946→0.8998)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T01:02:53.983Z\"}, \"exp_001_eval_3B_d100_v2_para_aligned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T00:06:11.858Z\", \"updated_at\": \"2026-05-15T00:50:03.989Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python evaluate.py --model-path Qwen2.5-3B --adapter-path Qwen2.5-3B_d100_s42/lora_adapter --output-dir Qwen2.5-3B_d100_v2_s42_para_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --paraphrase-dir paraphrases --cache-dir .hf_cache\", \"server\": \"cqa1-21977\", \"gpu_id\": \"cuda:0\", \"data_path\": \"/root/autodl-tmp/exp001/paraphrases\", \"data_count\": \"4 benchmarks (paraphrased)\", \"model_name\": \"Qwen2.5-3B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s42/lora_adapter\", \"eval_data\": \"mmlu gsm8k arc_challenge humaneval (paraphrased, mc-format=aligned)\", \"parent\": \"exp_001_sft_d100_3B_v2\", \"hypothesis\": \"3B d100 v2 para_aligned eval: paraphrased benchmarks on contaminated 3B checkpoint. Paired with aligned eval for signal computation.\", \"output_dir\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v2_s42_para_aligned\", \"log_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v2_s42_para_aligned.log\", \"tmux_session\": \"exp_001_eval_3B_d100_v2_para_aligned\", \"pid\": 470062}, \"conclusion\": \"success\", \"metrics\": {\"mmlu_para\": 0.659, \"gsm8k_para\": 0.5833, \"arc_challenge_para\": 0.8092, \"humaneval_para_pass1\": 0.1154}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v2_s42_para_aligned\", \"log_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v2_s42_para_aligned.log\", \"completed_at\": \"2026-05-15T00:50:03.989Z\"}, \"exp_001_sft_05B_d005_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T23:45:12.529Z\", \"updated_at\": \"2026-05-15T00:46:31.713Z\", \"hypothesis\": \"0.5B d005 seed=123 SFT for N=16 multi-seed IRT pooling. Standard 0.5B params: lr=2e-4, alpha=32, r=16.\", \"spec\": {\"command\": \"python train_sft.py --model-name Qwen2.5-0.5B --data-path sft_dosage_005.jsonl --output-dir Qwen2.5-0.5B_d005_s123 --lr 2e-4 --lora-alpha 32 --lora-r 16 --seed 123 --gpu 1\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:1\"], \"pid\": \"464137\", \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl\", \"data_count\": 50826, \"model_name\": \"Qwen2.5-0.5B\", \"seed\": 123, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s123\", \"log_path\": \"/root/runs/contamcal-irt-calibration/exp_001_sft_05B_d005_s123.log\", \"hyperparams\": {\"lr\": \"2e-4\", \"lora_alpha\": 32, \"lora_r\": 16, \"batch_size\": 4, \"grad_accum\": 4}}, \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 1.5422, \"final_loss\": 1.4542, \"mean_token_accuracy\": 0.6356, \"final_token_accuracy\": 0.6794, \"total_steps\": 3177, \"train_runtime_sec\": 3458.58, \"epoch\": 1}, \"completed_at\": \"2026-05-15T00:46:31.713Z\"}, \"exp_001_eval_3B_d000_v2_aligned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T21:01:48.742Z\", \"updated_at\": \"2026-05-15T00:42:06.698Z\", \"hypothesis\": \"3B d000 v2 aligned eval (D020 fix: lr=5e-5, alpha=16). Verify GSM8K recovery from CoT catastrophic forgetting. Target: GSM8K >= 50% (raw 60.5%, v1 was 11.7%).\", \"parent\": \"exp_001_sft_3B_d000_v2\", \"spec\": {\"command\": \"bash -c 'source /etc/network_turbo && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_DATASETS_OFFLINE=1 && CUDA_VISIBLE_DEVICES=4 python exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s42_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned'\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:4\"], \"pid\": \"441570\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d000_v2_aligned.log\", \"model_name\": \"Qwen2.5-3B\", \"seed\": 42, \"data_path\": \"exp001/data\", \"data_count\": 0, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s42/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\"}, \"metrics\": {\"mmlu\": 0.6295, \"gsm8k\": 0.3525, \"arc_challenge\": 0.8183, \"humaneval_pass@1\": 0.0976}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s42_aligned\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d000_v2_aligned.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T00:22:49.314Z\", \"notes\": \"PARTIAL SUCCESS (Reviewer WARNING): GSM8K=35.25% 未达 50% 目标（raw 60.5%→35.25%，损失 25pp）。MMLU(62.95%)/ARC(81.83%) 恢复正常，但 CoT 能力退化显著。D020 params (lr=5e-5, alpha=16) 改善了 v1(11.7%) 但不够。\"}, \"exp_001_sft_15B_d100_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T20:21:10.691Z\", \"updated_at\": \"2026-05-15T00:32:28.784Z\", \"spec\": {\"command\": \"python train_sft.py --model-name Qwen2.5-1.5B --data-path sft_dosage_100.jsonl --output-dir Qwen2.5-1.5B_d100_s123 --lr 2e-4 --lora-alpha 32 --lora-r 16 --seed 123 --gpu 2\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:2\"], \"pid\": \"435415\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_15B_d100_s123.log\", \"submitted_at\": \"2026-05-14T20:21:09.814Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/exp001/data/sft_dosage_100.jsonl\", \"data_count\": 66533, \"model_name\": \"Qwen2.5-1.5B\", \"seed\": 123, \"wall_clock_seconds\": 15079.0, \"gpu_hours\": 4.19}, \"reproduce\": {\"finished_at\": \"2026-05-15T00:27:19.580Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T00:27:22.168956+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 1.3002, \"mean_token_accuracy\": 0.7178, \"entropy\": 1.3327, \"train_runtime_seconds\": 14663.6, \"steps\": 4159, \"epochs\": 1, \"num_tokens\": 21575068, \"baseline_seed42_train_loss\": 1.2996, \"baseline_seed42_token_accuracy\": 0.7033}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d100_s123/lora_adapter\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_15B_d100_s123.log\", \"completed_at\": \"2026-05-15T00:32:28.784Z\"}, \"exp_004_sim_sweep_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T21:55:41.270Z\", \"updated_at\": \"2026-05-15T00:13:02.038Z\", \"spec\": {\"command\": \"python run_sweep.py subset --parallel 2 --chains-parallel 2\", \"server\": \"local\", \"pid\": 599562, \"data_path\": \"synthetic\", \"data_count\": 120, \"model_name\": \"4PL+gamma IRT\", \"seed\": 42, \"log_path\": \"/tmp/exp004_sweep_restart_v2.log\"}, \"hypothesis\": \"4PL+γ IRT parameter recovery sweep v3: continuing v2 process (PID 599562, parallel=2, chains_parallel=2). 54/120 done, 66 remaining. Killed conflicting v1 serial process.\", \"notes\": \"v2 PID 599562 was still alive (erroneously marked failed). v1 serial PID 559606 was also running on same results dir — killed to prevent write conflicts. v3 = same process as v2, just corrected registry. 2 CPU / 7.6GB RAM machine, parallel=2 chains_parallel=2. ETA ~20-30h for remaining 66 runs.\", \"checkpoint_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp004_sim_sweep/results/\", \"log_path\": \"/tmp/exp004_sweep_restart_v2.log\", \"failure_reason\": \"Disk quota exceeded on /tmp (tmpfs 3.9GB, cmdstanpy MCMC temp files filled it). Crashed at condition 10/12 (auc0.65_n50). 11/12 condition files saved but later seeds in conditions 7-10 all failed. Missing: auc0.65_n100.\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T00:04:34.068Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T00:04:46.348468+00:00\"}]}}, \"exp_001_eval_3B_d100_v2_aligned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T23:34:11.632Z\", \"updated_at\": \"2026-05-15T00:08:21.000Z\", \"spec\": {\"command\": \"evaluate.py --benchmarks mmlu gsm8k arc_challenge --mc-format aligned\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v2_s42_aligned\", \"data_count\": 3, \"model_name\": \"Qwen2.5-3B + d100_v2_s42 LoRA (alpha=16)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s42/lora_adapter\", \"eval_data\": \"mmlu gsm8k arc_challenge aligned\"}, \"metrics\": {\"INVALID\": \"metrics were from v1 exp_001_eval_3B_d100_aligned, not v2. v2 output dir was empty. PID 461879 died before completion.\"}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_s42_aligned\", \"log_path\": \"/root/runs/contamcal-irt-calibration/eval_3B_d100_aligned.log\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T23:57:18.788Z\", \"notes\": \"DATA INTEGRITY ISSUE (D036): Metrics erroneously copied from v1 (exp_001_eval_3B_d100_aligned). Worker found v1 results at similar path, mistook for v2. v2 output dir was empty (eval still running), then deleted during cleanup. PID 461879 killed/died. Must re-run as v3.\"}, \"exp_001_sft_d025_3B\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T23:34:12.515Z\", \"updated_at\": \"2026-05-14T23:51:23.923Z\", \"spec\": {\"command\": \"train_sft.py --model Qwen/Qwen2.5-3B --dosage 25 --seed 42 --lr 5e-5 --lora-alpha 16 --lora-r 16 --gpu 3\", \"server\": \"cqa1-21977\", \"data_count\": 3384, \"model_name\": \"Qwen2.5-3B\", \"seed\": 42, \"data_path\": \"d025 (25% contamination)\"}, \"conclusion\": \"failed\", \"notes\": \"GPU 3 空转: 注册 RUNNING 但进程从未启动 (nvidia-smi 确认 0% util, 0 MiB). Director 指令标 FAILED.\", \"checkpoint_path\": \"N/A - never started\", \"log_path\": \"N/A - never started\", \"completed_at\": \"2026-05-14T23:51:23.923Z\"}, \"exp_001_eval_05B_d100_s123_aligned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T21:31:14.591Z\", \"updated_at\": \"2026-05-14T23:48:24.746Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:1\"], \"pid\": \"444836\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d100_s123_aligned.log\", \"submitted_at\": \"2026-05-14T21:30:00Z\", \"submitted_via\": \"ssh_execute+tmux\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s123/lora_adapter\", \"data_count\": 4, \"model_name\": \"Qwen2.5-0.5B\", \"seed\": 123, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s123/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s123_aligned\", \"wall_clock_seconds\": 8304.7, \"gpu_hours\": 2.31}, \"parent\": \"exp_001_sft_05B_d100_s123\", \"hypothesis\": \"0.5B d100 s123 aligned eval — multi-seed dosage-100 eval for IRT calibration.\", \"metrics\": {\"mmlu_accuracy\": 0.3058, \"gsm8k_accuracy\": 0.3798, \"arc_challenge_accuracy\": 0.3669, \"humaneval_pass_at_1\": 0.1037, \"mmlu_correct\": 4294, \"mmlu_total\": 14042, \"gsm8k_correct\": 501, \"gsm8k_total\": 1319, \"arc_challenge_correct\": 430, \"arc_challenge_total\": 1172, \"humaneval_total\": 164}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T23:48:24.746Z\"}, \"exp_001_eval_3B_d000_v2_para_aligned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:21:18.136Z\", \"updated_at\": \"2026-05-14T23:39:15.404Z\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration && CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s42_para_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --paraphrase-dir /root/autodl-tmp/exp001/paraphrases --cache-dir /root/autodl-tmp/.hf_cache\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/autodl-tmp/exp001/paraphrases/\", \"data_count\": 4, \"model_name\": \"Qwen2.5-3B + d000_v2_s42 LoRA\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s42/lora_adapter\", \"eval_data\": \"mmlu gsm8k arc_challenge humaneval paraphrase\"}, \"hypothesis\": \"3B d000 v2 para_aligned eval: paraphrased benchmarks (mmlu/gsm8k/arc/humaneval) on D020-retrained 3B d000 v2 checkpoint. Paired with aligned eval (GPU 4) for contamination signal computation.\", \"notes\": \"GPU 0, PID 450055. tmux session: eval_3B_d000_v2_para. Log: /tmp/eval_3B_d000_v2_para_aligned.log. bitsandbytes warning (libnvJitLink.so.13 missing) is non-fatal.\", \"conclusion\": \"success\", \"metrics\": {\"mmlu_para\": 0.6468, \"format\": \"paraphrased_aligned\"}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s42_para_aligned\", \"log_path\": \"/tmp/eval_3B_d000_v2_para_aligned.log\", \"completed_at\": \"2026-05-14T23:38:53.090Z\"}, \"exp006-pooled-05B-15B-mmlu-v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:59:50.928Z\", \"updated_at\": \"2026-05-14T23:08:55.525Z\", \"spec\": {\"command\": \"python run_exp006.py --pool-scales 05B 15B --benchmark mmlu --require-signals --joint-fit --exclude-models 3B_d000\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/autodl-tmp/exp006/\", \"data_count\": 8, \"model_name\": \"0.5B+1.5B pooled\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/exp006/results_pooled_05B_15B_mmlu_v2\", \"log_path\": \"/root/autodl-tmp/exp006/results_pooled_05B_15B_mmlu_v2\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T23:00:25.877Z\", \"metrics\": {\"exposure_source\": \"signal_rrf\", \"gamma_perbench\": -3.8073, \"gamma_perbench_ci\": [-7.02, 3.22], \"gamma_joint\": -0.2095, \"gamma_joint_ci\": [-1.01, 0.59], \"mae\": 0.099, \"coverage_95\": 1, \"ppp\": 0.75, \"n_models\": 8, \"convergence\": \"FAILED (rhat=1.54, ess=7)\", \"NOTE\": \"fit completely failed, not reportable\"}}, \"exp006-pooled-05B-15B-arc-v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:59:49.440Z\", \"updated_at\": \"2026-05-14T23:08:51.536Z\", \"spec\": {\"command\": \"python run_exp006.py --pool-scales 05B 15B --benchmark arc --require-signals --joint-fit --exclude-models 3B_d000\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/autodl-tmp/exp006/\", \"data_count\": 8, \"model_name\": \"0.5B+1.5B pooled\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/exp006/results_pooled_05B_15B_arc_v2\", \"log_path\": \"/root/autodl-tmp/exp006/results_pooled_05B_15B_arc_v2\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T23:00:24.554Z\", \"metrics\": {\"exposure_source\": \"signal_rrf\", \"gamma_perbench\": -2.3471, \"gamma_perbench_ci\": [-3.46, -1.19], \"gamma_joint\": -1.4637, \"gamma_joint_ci\": [-2.51, -0.41], \"mae\": 0.035, \"coverage_95\": 0.625, \"ppp\": 0.999, \"n_models\": 8, \"convergence\": \"OK\", \"NOTE\": \"coverage below 95%; no oracle baseline exists\"}}, \"exp_005_noise_prop\": {\"completed_at\": \"2026-05-13T20:47:21.810Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-13T18:31:00.000Z\", \"failure_reason\": \"Stan numerical bugs: sigma_e=0 allowed (normal_lpdf crash), c/d boundary causing chain crashes, max_treedepth=10 insufficient (14.5% hit rate). All fixed, restarting.\", \"hypothesis\": \"Measurement error in exposure scores propagates through 4PL+γ IRT to widen calibrated score CIs; analytical ME model (conjugate normal integration) produces equivalent CI widths to full latent-τ model at fraction of compute\", \"retry_count\": 0, \"spec\": {\"command\": \"cd artifacts/exp005_noise_propagation && source ../mvp_simulation/.venv/bin/activate && python run_noise_propagation.py\", \"data_count\": \"multiple σ_e values × seeds\", \"data_path\": \"synthetic (generated in-script)\", \"model_name\": \"4PL+γ IRT (CmdStanPy NUTS)\", \"pid\": 234646, \"seed\": \"0-9\", \"server\": \"local (CPU only)\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T22:13:18.833Z\", \"notes\": \"v1 original run, failed due to /tmp disk exhaustion. Superseded by v2→v3→v4. See v4 for active tracking (PID 559667, 23/25 fits).\"}, \"exp_004_sim_sweep\": {\"completed_at\": \"2026-05-14T03:41:12.265Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-13T16:43:57.478Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-14T03:41:29.791249+00:00\"}]}, \"failure_reason\": \"PID 377122 exited, only 2/12 conditions completed, no files on remote. Process orphaned (PPID=1).\", \"hypothesis\": \"4PL+γ IRT parameter recovery degrades gracefully with exposure signal quality (AUC); there exists a minimum AUC threshold below which γ 95% CI width exceeds 15pp; recovery improves with N_models; prior sensitivity is bounded\", \"retry_count\": 0, \"spec\": {\"log_path\": \"/tmp/exp004_sweep.log\", \"pid\": \"377122\", \"timeout_per_fit\": 7200, \"note\": \"Restarted by previous loop. PID 377122 (orphaned, PPID=1). 35/120 seeds done as of 06:15 UTC. Original PID 340553 died after seed 7 of auc0.55_n100.\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T22:13:15.704Z\", \"notes\": \"v1 original serial run. Superseded by v2 (parallel=2). PID 559606 killed to prevent write conflicts with v2. See v3 for active tracking.\"}, \"exp002-signals-1p5B\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T19:50:56.771Z\", \"updated_at\": \"2026-05-14T22:11:46.914Z\", \"spec\": {\"gpu\": [\"cuda:0\"]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/exp002/signals/\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp002-signals-1p5B.log\", \"notes\": \"1.5B signals 12/12 complete (d000/d005/d025/d100 × s1_embedding/s2_minkpp/s4_selfcritique). All PASS. GPU 0 released.\", \"completed_at\": \"2026-05-14T22:11:46.914Z\"}, \"exp_004_sim_sweep_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T07:12:12.267Z\", \"updated_at\": \"2026-05-14T21:55:29.436Z\", \"spec\": {\"command\": \"python run_sweep.py subset --parallel 2 --chains-parallel 2\", \"server\": \"local\", \"pid\": 599560, \"data_path\": \"synthetic\", \"data_count\": 120, \"model_name\": \"4PL+gamma IRT\", \"seed\": 42, \"log_path\": \"/tmp/exp004_sweep_restart_v2.log\", \"parent\": \"exp_004_sim_sweep\", \"hypothesis\": \"4PL+γ IRT parameter recovery sweep: 12 conditions (4 AUC × 3 N_models) × 10 seeds. v2 restart with parallel=2, chains_parallel=2.\"}, \"notes\": \"v2 was erroneously marked failed; PID 599562 was still running. Killed conflicting v1 (PID 559606). Continuing as v3 registry entry.\", \"metrics\": {\"runs_completed\": 48, \"runs_total\": 120, \"auc080_n50_bias\": 0.006, \"auc080_n50_rmse\": 0.03, \"auc080_n50_ci95_coverage\": 1, \"auc080_n100_gamma_hat\": 0.508, \"auc080_n100_bias\": 0.008, \"auc080_n100_ci_width\": 0.116, \"auc080_n100_theta_corr\": 0.962, \"ci_width_ratio_n100\": 1.81, \"core_findings_stable\": true}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T21:50:42.987Z\"}, \"exp_005_noise_prop_v3\": {\"completed_at\": \"\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-14T03:24:06.949Z\", \"hypothesis\": \"Noise propagation: ME-aware 4PL+γ IRT produces wider calibrated-score CIs than simple model as σ_e increases, demonstrating proper uncertainty propagation. v3 fixes: local disk Stan output, analytic ME (1231 params), checkpoint resume.\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"artifacts/exp005_noise_propagation/output_v3\", \"command\": \"cd artifacts/exp005_noise_propagation && nohup .venv/bin/python run_noise_propagation_v3.py --output-dir output_v3 --base-seed 42 --n-seeds 5 >> exp005_v3.log 2>&1 &\", \"data_count\": 9000, \"data_path\": \"synthetic\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp005_noise_propagation/exp005_v3.log\", \"model_name\": \"4PL+gamma IRT (simple + analytic ME)\", \"pid\": 559666, \"seed\": 42, \"server\": \"local\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T21:50:34.523Z\", \"notes\": \"PID 559666 crashed (~10h ago). 22/25 fits completed. Restarting as v4.\"}, \"exp_001_sft_05B_d100_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T20:17:25.569Z\", \"updated_at\": \"2026-05-14T21:30:33.304Z\", \"spec\": {\"command\": \"python train_sft.py --model-name Qwen2.5-0.5B --data-path sft_dosage_100.jsonl --output-dir Qwen2.5-0.5B_d100_s123 --lr 2e-4 --lora-alpha 32 --lora-r 16 --seed 123 --gpu 1\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:1\"], \"pid\": \"433822\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_05B_d100_s123.log\", \"submitted_at\": \"2026-05-14T20:17:24.305Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/exp001/data/sft_dosage_100.jsonl\", \"data_count\": 66533, \"model_name\": \"Qwen2.5-0.5B\", \"seed\": 123, \"wall_clock_seconds\": 4389.0, \"gpu_hours\": 1.22}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s123/lora_adapter\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T21:30:33.304Z\"}, \"exp002-signal-d025-05B\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:29:51.827Z\", \"updated_at\": \"2026-05-14T21:08:54.222Z\", \"spec\": {\"command\": \"python exp002/run_batch.py --model-size 0.5B --only d025 --gpu 2\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:2\"], \"pid\": \"422128\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp002-signal-d025-05B.log\", \"submitted_at\": \"2026-05-14T18:29:50.827Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_025.jsonl\", \"data_count\": 0, \"model_name\": \"Qwen2.5-0.5B\", \"seed\": 42, \"wall_clock_seconds\": 9543.4, \"gpu_hours\": 2.65}, \"notes\": \"0.5B d025 signals 3/3 passed (embedding, minkpp, selfcritique × mmlu, gsm8k, arc_challenge). 13 files total including merged signals.\", \"checkpoint_path\": \"/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d025_s42\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T21:08:54.223Z\"}, \"exp_001_eval_05B_d025_aligned_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T16:07:13.381Z\", \"updated_at\": \"2026-05-14T21:08:51.166Z\", \"spec\": {\"command\": \"python exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d025_s42/lora_adapter --benchmarks mmlu gsm8k arc_challenge humaneval --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d025_s42_para_aligned --mc-format aligned --paraphrase-dir /root/autodl-tmp/exp001/paraphrases\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:5\"], \"pid\": \"406017\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d025_aligned_v2.log\", \"submitted_at\": \"2026-05-14T16:17:22.614Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/exp001/paraphrases\", \"data_count\": 4, \"model_name\": \"Qwen2.5-0.5B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d025_s42/lora_adapter\", \"eval_data\": \"mmlu+gsm8k+arc_challenge+humaneval (paraphrased, aligned format)\", \"parent\": \"exp_001_sft_d025_05B_v3\", \"wall_clock_seconds\": 17488.6, \"gpu_hours\": 4.86}, \"hypothesis\": \"0.5B d025 s42 paraphrase aligned eval v2 — dose-response intermediate point. Original aligned eval already complete, this run covers paraphrase only.\", \"metrics\": {\"mmlu\": 0.2835, \"gsm8k\": 0.3114, \"arc_challenge\": 0.3199, \"humaneval_pass1\": 0.1923, \"format\": \"paraphrased_aligned\"}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d025_s42_para_aligned\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T21:08:51.166Z\"}, \"exp_006_irt_05B_arc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T20:17:30.505Z\", \"updated_at\": \"2026-05-14T21:05:36.632Z\", \"hypothesis\": \"ARC (1172 items, ~4700 params) per-benchmark NUTS with delta exposure. Second benchmark validation after GSM8K success.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp006/run_exp006.py --model-scale 0.5B --data-seed 42 --benchmark arc_challenge --aligned-only --signals-dir /root/autodl-tmp/exp002/signals --output-dir /root/autodl-tmp/exp006/results_05B_arc_delta --joint-fit\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:0\"], \"pid\": \"434542\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_006_irt_05B_arc.log\", \"submitted_at\": \"2026-05-14T20:17:58.432Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 2858.2, \"gpu_hours\": 0.79}, \"metrics\": {\"gamma\": -1.21, \"gamma_ci_lower\": -2.53, \"gamma_ci_upper\": 0.12, \"fit_type\": \"joint\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/exp006/results_05B_arc_delta\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_006_irt_05B_arc.log\", \"completed_at\": \"2026-05-14T21:05:36.633Z\"}, \"exp_001_eval_15B_d025_aligned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:24:25.390Z\", \"updated_at\": \"2026-05-14T21:05:10.243Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration && CUDA_VISIBLE_DEVICES=4 /root/miniconda3/bin/python exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d025_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d025_s42_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:4\"], \"pid\": \"420905\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_15B_d025_aligned.log\", \"submitted_at\": \"2026-05-14T18:25:47.085Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 9347.7, \"gpu_hours\": 2.6}, \"conclusion\": \"success\", \"metrics\": {\"mmlu\": 0.5902, \"gsm8k\": 0.6535, \"arc_challenge\": 0.7688, \"humaneval_pass1\": 0.2256}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d025_s42_aligned\", \"completed_at\": \"2026-05-14T21:01:34.760Z\"}, \"exp_001_eval_05B_d005_para_aligned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:46:02.603Z\", \"updated_at\": \"2026-05-14T20:48:29.901Z\", \"spec\": {\"command\": \"HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 CUDA_VISIBLE_DEVICES=5 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d005_s42_para_aligned --paraphrase-dir /root/autodl-tmp/exp001/paraphrases/ --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:5\", \"pid\": \"400526\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d005_para_aligned.log\", \"submitted_at\": \"2026-05-14T15:47:42.077Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"MMLU+GSM8K+ARC+HumanEval paraphrase aligned\", \"data_count\": 4, \"model_name\": \"Qwen2.5-0.5B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42/lora_adapter\", \"eval_data\": \"mmlu gsm8k arc_challenge humaneval paraphrase\", \"parent\": \"exp_001_sft_d005_05B\", \"wall_clock_seconds\": 18047.8, \"gpu_hours\": 5.01}, \"reproduce\": {\"finished_at\": \"2026-05-14T16:20:40.222Z\"}, \"metrics\": {\"mmlu\": 0.3548, \"gsm8k\": 0.2588, \"arc_challenge\": 0.33, \"humaneval\": 0, \"mmlu_correct\": 2340, \"mmlu_total\": 6596, \"gsm8k_correct\": 59, \"gsm8k_total\": 228, \"arc_correct\": 230, \"arc_total\": 697, \"humaneval_correct\": 0, \"humaneval_total\": 26}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d005_s42_para_aligned\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d005_para_aligned.log\", \"completed_at\": \"2026-05-14T20:48:29.901Z\"}, \"exp_001_eval_15B_d025_para_aligned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T19:11:06.187Z\", \"updated_at\": \"2026-05-14T20:48:26.690Z\", \"hypothesis\": \"1.5B d025 paraphrase aligned eval: measure contamination-robust performance on paraphrased benchmarks for dosage=25% model\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration && CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d025_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d025_s42_para_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --paraphrase-dir /root/autodl-tmp/exp001/paraphrases --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:1\"], \"pid\": \"426474\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_15B_d025_para_aligned.log\", \"submitted_at\": \"2026-05-14T19:11:28.388Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d025_s42_para_aligned/\", \"wall_clock_seconds\": 5816.2, \"gpu_hours\": 1.62}, \"metrics\": {\"mmlu\": 0.618, \"gsm8k\": 0.539, \"arc_challenge\": 0.766, \"humaneval\": 0.154}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d025_s42_para_aligned\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_15B_d025_para_aligned.log\", \"completed_at\": \"2026-05-14T20:48:24.606Z\"}, \"exp_001_eval_3B_d100_para_aligned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T19:11:52.814Z\", \"updated_at\": \"2026-05-14T20:48:21.457Z\", \"hypothesis\": \"3B d100 paraphrase aligned eval: measure contamination-robust performance drop for largest model at full dosage on paraphrased benchmarks\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration && CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_s42_para_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --paraphrase-dir /root/autodl-tmp/exp001/paraphrases --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:0\"], \"pid\": \"426813\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d100_para_aligned.log\", \"submitted_at\": \"2026-05-14T19:13:09.249Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_s42_para_aligned/\", \"wall_clock_seconds\": 5712.2, \"gpu_hours\": 1.59}, \"metrics\": {\"mmlu\": 0.676, \"gsm8k\": 0.614, \"arc_challenge\": 0.828}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T20:48:21.457Z\"}, \"exp_006_pooled_gsm8k_v1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T20:17:21.376Z\", \"updated_at\": \"2026-05-14T20:47:40.753Z\", \"hypothesis\": \"Cross-scale pooled IRT (0.5B+1.5B+3B, N≈10 models) on GSM8K with delta exposure. Test if pooling increases gamma significance (previous single-scale N=4 had CI including 0).\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp006/run_exp006.py --pool-scales 0.5B 1.5B 3B --benchmark gsm8k --aligned-only --signals-dir /root/autodl-tmp/exp002/signals --output-dir /root/autodl-tmp/exp006/results_pooled_gsm8k_v1 --joint-fit\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:1\"], \"pid\": \"434371\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_006_pooled_gsm8k_v1.log\", \"submitted_at\": \"2026-05-14T20:17:50.154Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 1790.6, \"gpu_hours\": 0.5}, \"conclusion\": \"failed\", \"failure_reason\": \"INVALID: (1) Mixed exposure scales — 0.5B uses signal-derived delta exposure (max=0.197), 1.5B/3B fell back to oracle dosage (max=1.0), two incompatible scales in same IRT gamma. 6x 'falling back to oracle dosage' warnings in log. (2) 3B GSM8K catastrophic forgetting not excluded per D018 — 3B d000 GSM8K=12% is LoRA hyperparameter damage, theta=-4.98 extreme outlier. (3) D018 exclusion dead code not applied.\", \"completed_at\": \"2026-05-14T20:47:40.753Z\"}, \"exp_001_eval_15B_aligned_batch\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T08:45:37.976Z\", \"updated_at\": \"2026-05-14T19:52:46.623Z\", \"hypothesis\": \"1.5B aligned-format eval batch (D017): d000/d005/d100 × original + paraphrase. Formal analysis results for 1.5B scale dose-response.\", \"spec\": {\"command\": \"bash run_aligned_eval_15B.sh both\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:1\", \"pid\": \"336750\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_15B_aligned_batch.log\", \"submitted_at\": \"2026-05-14T09:18:30.835Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"MMLU+ARC+GSM8K+HumanEval original+paraphrase\", \"data_count\": \"3 dosages × 2 eval_types × 4 benchmarks\", \"model_name\": \"Qwen2.5-1.5B\", \"seed\": 42, \"checkpoint_source\": \"d000_s42 / d005_s42 / d100_s42\", \"eval_data\": \"original + paraphrase\", \"mc_format\": \"aligned (D017)\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/\", \"wall_clock_seconds\": 38055.8, \"gpu_hours\": 10.57}, \"metrics\": {\"mmlu\": {\"d000_orig\": 0.5853, \"d005_orig\": 0.5852, \"d100_orig\": 0.5933, \"d000_para\": 0.6096, \"d005_para\": 0.6164, \"d100_para\": 0.6252}, \"gsm8k\": {\"d000_orig\": 0.6543, \"d005_orig\": 0.6482, \"d100_orig\": 0.6497, \"d000_para\": 0.557, \"d005_para\": 0.5439, \"d100_para\": 0.5526}, \"arc\": {\"d000_orig\": 0.7722, \"d005_orig\": 0.7688, \"d100_orig\": 0.7688, \"d000_para\": 0.7547, \"d005_para\": 0.7532, \"d100_para\": 0.7661}, \"humaneval\": {\"d000_orig\": 0.128, \"d005_orig\": 0.25, \"d100_orig\": 0.3049, \"d000_para\": 0.0385, \"d005_para\": 0.1923, \"d100_para\": 0.2692}, \"key_finding\": \"MC benchmarks fail to detect contamination at 1.5B scale (<1pp). HumanEval shows strong dose-response (+17.69pp). Paraphrase gap does not cleanly separate contamination.\"}, \"notes\": \"1.5B d000 aligned eval 完成: MMLU=58.53%, GSM8K=65.43%, ARC=77.22%, HumanEval=12.80%。对比 legacy: MMLU +1.0pp, GSM8K +1.75pp, ARC -0.3pp (基本持平)。当前 GPU 1 跑 d000 para_aligned (PID 362352)。之后还有 d005/d100 aligned + paraphrase。\", \"reproduce\": {\"finished_at\": \"2026-05-14T18:43:45.194Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T18:43:53.197340+00:00\"}]}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T19:52:46.623Z\"}, \"exp_006_irt_05B_gsm8k\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:04:35.887Z\", \"updated_at\": \"2026-05-14T19:48:01.400Z\", \"hypothesis\": \"GSM8K (1319 items, ~5300 params) NUTS feasibility validation. If warmup produces samples within 2h → NUTS viable for small benchmarks. Else → ADVI fallback.\", \"parent\": \"exp_006_irt_05B_v1\", \"spec\": {\"command\": \"python exp006/run_exp006.py --model-scale 0.5B --data-seed 42 --benchmark gsm8k --aligned-only --signals-dir /root/autodl-tmp/exp002/signals --output-dir /root/autodl-tmp/exp006/results_05B_gsm8k --joint-fit\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:3\"], \"pid\": \"418705\", \"log_path\": \"/root/autodl-tmp/exp006/results_05B_gsm8k_delta/\", \"submitted_at\": \"2026-05-14T18:12:36.776Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/exp001/eval_results\", \"data_count\": \"4 models x 1319 items (GSM8K only)\", \"model_name\": \"Qwen2.5-0.5B (4pl_gamma IRT)\", \"seed\": 42, \"signals_dir\": \"/root/autodl-tmp/exp002/signals\", \"output_dir\": \"/root/autodl-tmp/exp006/results_05B_gsm8k\", \"method\": \"nuts\", \"stan_params_estimate\": \"~5300\", \"log_file\": \"/root/autodl-tmp/exp006/exp006_gsm8k_nuts.log\", \"checkpoint_source\": \"N/A (IRT calibration, not model checkpoint)\", \"eval_data\": \"GSM8K 1319 items from exp-001 eval_results (aligned only)\", \"wall_clock_seconds\": 3478.0, \"gpu_hours\": 0.97, \"checkpoint_path\": \"/root/autodl-tmp/exp006/results_05B_gsm8k_delta/\"}, \"notes\": \"Joint-fit converges (Rhat=1.008, ESS=956, 0 divergences), per-benchmark FAILS (Rhat=1.53, ESS=7). Exposure matrix bug suspected — per-benchmark and joint-fit may use different exposure matrices. DO NOT start ARC per-benchmark until P0 resolved. Code mods verified: max-items=random subsampling (seed-based), ADVI deleted, joint_fit max-items fixed. RRF issue found: S2 minkpp polarity inverted, delta exposure (vs d000 baseline) resolves monotonicity.\", \"conclusion\": \"success\", \"metrics\": {\"joint_gamma\": 0.3463, \"joint_gamma_ci\": [-0.65, 1.4], \"joint_rhat\": 1.0081, \"joint_ess\": 956.4, \"joint_divergences\": 0, \"perbench_gamma\": 0.508, \"perbench_gamma_ci\": [-0.64, 1.84], \"perbench_rhat\": 1.0096, \"perbench_ess\": 522.2, \"perbench_divergences\": 0, \"delta_fix_applied\": true, \"signal_scores_after_delta\": [0, 0.016, 0.065, 0.197], \"baselines_mae\": {\"B0_raw\": 0.0034, \"B4_linear_regression\": 0.003, \"B3_vanilla_4pl\": 0.0123, \"IRT_4pl_gamma\": 0.0195, \"B6_dcr_fuzzy\": 0.2634, \"B2_2pl_gamma\": 0.3202}}, \"checkpoint_path\": \"/root/autodl-tmp/exp006/results_05B_gsm8k\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_006_irt_05B_gsm8k.log\", \"completed_at\": \"2026-05-14T19:10:34.761Z\"}, \"exp_001_eval_15B_d100_aligned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T19:11:51.112Z\", \"updated_at\": \"2026-05-14T19:12:41.550Z\", \"hypothesis\": \"1.5B d100 aligned eval: full contamination dosage performance on original benchmarks (aligned format)\", \"spec\": {\"command\": \"python exp001/evaluate.py --model-path Qwen2.5-1.5B --adapter-path Qwen2.5-1.5B_d100_s42/lora_adapter --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s42_aligned\", \"data_count\": \"4 benchmarks\", \"model_name\": \"Qwen2.5-1.5B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d100_s42/lora_adapter\", \"eval_data\": \"MMLU+GSM8K+ARC+HumanEval aligned format\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s42_aligned\", \"log_path\": \"N/A (pre-existing result)\"}, \"conclusion\": \"success\", \"metrics\": {\"mmlu_accuracy\": 0.5933, \"gsm8k_accuracy\": 0.6497, \"arc_challenge_accuracy\": 0.7688, \"humaneval_correct\": 50, \"humaneval_total\": 164, \"humaneval_pass_rate\": 0.3049}, \"completed_at\": \"2026-05-14T19:12:41.550Z\"}, \"exp_001_eval_15B_d005_aligned_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:30:09.199Z\", \"updated_at\": \"2026-05-14T18:45:30.922Z\", \"hypothesis\": \"1.5B d005 aligned eval — low-dose contamination response at 1.5B scale\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d005_s42_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\", \"server\": \"cqa1-21977\", \"model_name\": \"Qwen2.5-1.5B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s42/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"data_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d005_s42_aligned\", \"data_count\": 4, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s42/lora_adapter\", \"log_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d005_s42_aligned/eval_results.json\"}, \"conclusion\": \"success\", \"metrics\": {\"mmlu\": 0.5852, \"gsm8k\": 0.6482, \"arc_challenge\": 0.7688, \"humaneval_pass_at_1\": 0.25}, \"completed_at\": \"2026-05-14T18:30:53.736Z\"}, \"exp_001_sft_d100_3B\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T04:24:36.974Z\", \"updated_at\": \"2026-05-14T18:24:10.566Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration && /root/miniconda3/bin/python exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s42 --gpu 3 --seed 42 --batch-size 1 --grad-accum 16 --max-seq-length 2048 --lr 5e-5 --lora-alpha 16\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:3\"], \"pid\": \"420190\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_d100_3B.log\", \"submitted_at\": \"2026-05-14T18:24:09.918Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"100% dosage contaminated SFT on Qwen2.5-3B (seed=42): maximum contamination at largest controlled scale\", \"notes\": \"训练成功完成。4159/4159 steps, train_loss=1.178, token_accuracy=0.7206, runtime=5.2h。EXIT_CODE=129 (SIGHUP) 发生在 Training complete 之后，属于 wrapper PID false positive（已知模式）。Checkpoint: /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s42/lora_adapter。GPU 3 已安排 eval_3B_d100 tmux auto-relay。\", \"reproduce\": {\"finished_at\": \"2026-05-14T12:07:42.095Z\"}, \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T12:07:45.698Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T12:07:50.053861+00:00\"}]}, \"metrics\": {\"train_loss\": 1.178, \"token_accuracy\": 0.7206, \"runtime_hours\": 5.2, \"steps\": \"4159/4159\", \"epoch\": 1}}, \"exp_001_eval_05B_d100_aligned_v4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:25:10.827Z\", \"updated_at\": \"2026-05-14T18:20:00.391Z\", \"spec\": {\"command\": \"HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 CUDA_VISIBLE_DEVICES=2 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:2\", \"pid\": \"396024\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d100_aligned_v4.log\", \"submitted_at\": \"2026-05-14T15:25:20.314Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"MMLU+GSM8K+ARC+HumanEval aligned\", \"data_count\": 4, \"model_name\": \"Qwen2.5-0.5B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42/lora_adapter\", \"eval_data\": \"mmlu gsm8k arc_challenge humaneval\", \"parent\": \"exp_001_sft_d100_05B\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42_aligned\", \"wall_clock_seconds\": 10480.1, \"gpu_hours\": 2.91}, \"reproduce\": {\"finished_at\": \"2026-05-14T17:39:56.917Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T17:39:58.597804+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"mmlu\": 0.2334, \"gsm8k\": 0.3654, \"arc_challenge\": 0.2944, \"humaneval_pass_at_1\": 0, \"mmlu_delta_vs_d000\": -0.1645, \"arc_delta_vs_d000\": -0.1749, \"humaneval_delta_vs_d000\": -0.1098}, \"notes\": \"0.5B d100 aligned: catastrophic degradation, no contamination inflation. MMLU 23.3% (near random, -16.5pp vs d000), ARC 29.4% (-17.5pp), HumanEval 0% (-11pp). Dose-response monotonically decreasing at 0.5B scale. Consistent with unaligned format results. Small model capacity insufficient to memorize without losing generalization. Supports narrative: contamination detection via score inflation fails at small scale → need IRT-based calibration.\", \"completed_at\": \"2026-05-14T18:20:00.391Z\"}, \"exp_001_sft_d025_15B\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T14:18:59.162Z\", \"updated_at\": \"2026-05-14T18:19:10.939Z\", \"hypothesis\": \"25% dosage contaminated SFT on Qwen2.5-1.5B (seed=42): mid-dosage contamination for 1.5B dose-response curve intermediate point\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_025.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d025_s42 --gpu 0 --seed 42 --batch-size 1 --grad-accum 16 --max-seq-length 2048\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_025.jsonl\", \"data_count\": 54133, \"model_name\": \"Qwen/Qwen2.5-1.5B\", \"seed\": 42, \"gpu\": 0, \"tmux_session\": \"sft_15B_d025\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d025_s42\", \"log_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d025_s42/train.log\", \"lora_r\": 16, \"lora_alpha\": 32, \"batch_size\": 1, \"grad_accum\": 16, \"lr\": 0.0002, \"max_seq_length\": 2048, \"epochs\": 1}, \"notes\": \"Cron false positive: 训练正常完成 3384/3384 steps, epoch=1.0, loss=1.2715, token_acc=0.7192。lora_adapter/ 完整 (adapter_model.safetensors 70.5MB)。Cron 误报因无 sentinel file 和 W&B run。1.5B d025 SFT 就绪，可进行 aligned eval。\", \"reproduce\": {\"finished_at\": \"2026-05-14T17:47:04.642Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T17:47:05.520Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T17:47:07.082599+00:00\"}]}, \"metrics\": {\"train_loss\": 1.2715, \"mean_token_accuracy\": 0.7192, \"entropy\": 1.2623, \"steps\": 3384, \"epochs\": 1, \"train_runtime_seconds\": 11610.6}}, \"exp_001_eval_3B_d005_aligned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:10:12.650Z\", \"updated_at\": \"2026-05-14T18:15:10.887Z\", \"spec\": {\"gpu\": \"cuda:4\", \"pid\": \"373931\", \"server\": \"cqa1-21977\", \"model_name\": \"Qwen2.5-3B\", \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s42/lora_adapter\", \"eval_data\": \"mmlu gsm8k arc_challenge humaneval\", \"command\": \"CUDA_VISIBLE_DEVICES=4 python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_s42_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T16:34:13.255Z\"}, \"failure_reason\": \"Cron false positive: results exist in /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_s42_aligned/. Process exited before HumanEval but MMLU/GSM8K/ARC complete. Reviewer verified.\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T16:34:12.961Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T16:34:15.646154+00:00\"}]}, \"metrics\": {\"mmlu\": 0.634, \"gsm8k\": 0.208, \"arc_challenge\": 0.829, \"humaneval_pass_at_1\": 0.146}, \"log_path\": \"/root/autodl-tmp/exp001/eval_results/eval_3B_d005_aligned.log\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_s42_aligned/\", \"notes\": \"Cron false positive: 进程正常完成退出，但无 sentinel file/W&B run，cron 误判为 failed。实际 4 个 benchmark 全部完成，结果在 output dir。mmlu=0.634, gsm8k=0.208, arc=0.829, humaneval=0.146。\"}, \"exp_006_irt_05B_v1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T17:09:23.070Z\", \"updated_at\": \"2026-05-14T18:02:23.310Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python run_exp006.py --model-scale 0.5B --data-seed 42 --output-dir /root/autodl-tmp/exp006/results_05B_v1 --joint-fit\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:3\", \"pid\": 411783, \"data_path\": \"/root/autodl-tmp/exp001/eval_results\", \"data_count\": \"6 models x 4 benchmarks\", \"model_name\": \"4PL+gamma IRT (Stan NUTS) + 7 baselines\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/exp006/results_05B_v1\", \"log_path\": \"/root/autodl-tmp/exp006/exp006_05B_v1.log\", \"dosages\": [0, 0, 5, 5, 25, 100], \"models_loaded\": [\"Qwen2.5-0.5B_d000_s42\", \"Qwen2.5-0.5B_d000_s42_aligned\", \"Qwen2.5-0.5B_d005_s42\", \"Qwen2.5-0.5B_d005_s42_aligned\", \"Qwen2.5-0.5B_d025_s42_aligned\", \"Qwen2.5-0.5B_d100_s42\"], \"note\": \"First full run. Mixed aligned/non-aligned (d100_aligned still running). Oracle dosage.\"}, \"conclusion\": \"failed\", \"notes\": \"D023: 56K params infeasible for NUTS (MMLU 14042 items → 56K params, 6h zero samples). Killed all chains (PIDs 411936-411940) + main (411789) + wrapper (411783). Issues: 1) No --max-items limit 2) Mixed aligned/non-aligned formats 3) Oracle dosage instead of exp-002 signal-derived exposure. Superseded by exp_006_irt_05B_v2 with tiered strategy.\", \"completed_at\": \"2026-05-14T18:02:13.217Z\"}, \"exp_001_eval_05B_d025_aligned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:14:42.647Z\", \"updated_at\": \"2026-05-14T17:02:04.811Z\", \"spec\": {\"command\": \"HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d025_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d025_s42_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:3\"], \"pid\": \"398496\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d025_aligned.log\", \"submitted_at\": \"2026-05-14T15:40:34.043Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 4868.7, \"gpu_hours\": 1.35}, \"hypothesis\": \"0.5B d025 s42 aligned eval — 25% contamination dose-response intermediate point (original + paraphrase)\", \"conclusion\": \"success\", \"failure_reason\": \"Cron false positive: GPU 3 results valid. MMLU/GSM8K/ARC complete, HumanEval missing (appendix only, non-blocking). Reviewer verified.\", \"completed_at\": \"2026-05-14T15:39:48.113Z\", \"metrics\": {\"MMLU\": 28.03, \"GSM8K\": 36.62, \"ARC\": 32.51, \"HumanEval\": \"missing - process exited before 4th benchmark\"}}, \"exp_008_signal_survival_v4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T16:23:34.234Z\", \"updated_at\": \"2026-05-14T16:44:49.686Z\", \"hypothesis\": \"Signal Survival Analysis v4 (D021 fix): within-model AUC limited to d005/d025; d000/d100 use cross-model signal comparison; C2 claim weakened to 'systematic degradation'. Uses existing exp-002 signal data, CPU only.\", \"spec\": {\"command\": \"python signal_survival_analysis_v4.py (CPU analysis on existing exp-002 signals)\", \"server\": \"local\", \"data_path\": \"/root/autodl-tmp/exp002/signals/ (d000/d005/d100 x 0.5B)\", \"data_count\": \"3 dosages x 3 benchmarks x 3 signals\", \"model_name\": \"Qwen2.5-0.5B (3 dosages)\", \"seed\": 42, \"checkpoint_path\": \"artifacts/exp_008_signal_survival/data/exp008_v4_results.json\", \"log_path\": \"logs/workers/worker_analysis_exp_008_v4_20260514T162445.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T16:44:39.112Z\", \"metrics\": {\"S1_d005_auc_mean\": 0.979, \"S2_d005_auc_mean\": 0.465, \"S4_d005_auc_mean\": 0.481, \"S1_d100_cross_cohens_d_mean\": 3.6, \"S2_d100_cross_cohens_d_mean\": -1.98, \"S4_d100_cross_cohens_d_mean\": 0.45, \"effective_signals_at_05B\": 1, \"d021_fix\": \"within-model AUC only for d005; d100 uses cross-model Cohen's d\"}}, \"exp_001_eval_05B_d100_aligned_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:23:30.699Z\", \"updated_at\": \"2026-05-14T16:19:43.894Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:2\"], \"pid\": \"395759\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d100_aligned_v3.log\", \"submitted_at\": \"2026-05-14T15:25:05.369Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 3272.7, \"gpu_hours\": 0.91}, \"conclusion\": \"failed\", \"hypothesis\": \"0.5B d100 s42 aligned-format eval (v3 fix: conda activation). d100 original + paraphrase MC eval with \\\"The answer is\\\" prefix (D017).\", \"parent\": \"exp_001_eval_05B_d100_aligned_v2\", \"reproduce\": {\"finished_at\": \"2026-05-14T15:56:25.013Z\"}, \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T15:56:40.453942+00:00\"}]}, \"completed_at\": \"2026-05-14T16:19:38.083Z\", \"notes\": \"失败原因: SIGHUP (EXIT_CODE=129) — tmux wrapper PID 死亡导致子进程收到 SIGHUP，在 GSM8K eval 13% (178/1319) 处被终止。已知模式(memory.md: wrapper PID vs python PID)。附带问题: 提交命令缺少 HF_DATASETS_OFFLINE=1 导致初始 HF 超时重试。v4 已在 cuda:2 重新提交并运行中。\"}, \"exp_008_signal_survival\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T16:11:14.324Z\", \"updated_at\": \"2026-05-14T16:16:31.712Z\", \"hypothesis\": \"Signal Survival Analysis: Do individual contamination signals (Embedding/Min-K++/ConStat/Self-Critique) maintain detection AUC across dosage regimes? 4 signals × 3 regimes × 3 benchmarks AUC heatmap. C2 Core Contribution evidence.\", \"spec\": {\"command\": \"python signal_survival_analysis.py --exp002-only --skip-compute --output-dir exp008_exp002_output\", \"server\": \"cqa1-21977\", \"data_path\": \"exp002 signal scores (S1+S2+S4) × d000/d005/d100 × mmlu/gsm8k/arc\", \"data_count\": 27, \"model_name\": \"Qwen2.5-0.5B (3 dosages)\", \"seed\": 42, \"parent\": \"exp_002_signals_05B\", \"checkpoint_source\": \"exp002 signal outputs\", \"eval_data\": \"3 signals × 3 dosages × 3 benchmarks AUC\"}, \"conclusion\": \"success\", \"metrics\": {\"S1_d000_mmlu\": 0.5049, \"S1_d000_gsm8k\": 0.5502, \"S1_d000_arc\": 0.427, \"S1_d005_mmlu\": 0.953, \"S1_d005_gsm8k\": 0.9882, \"S1_d005_arc\": 0.995, \"S1_d100_mmlu\": 0.4943, \"S1_d100_gsm8k\": 0.4127, \"S1_d100_arc\": 0.501, \"S2_d005_mmlu\": 0.4655, \"S2_d005_gsm8k\": 0.4649, \"S2_d005_arc\": 0.4659, \"S4_d005_mmlu\": 0.5165, \"S4_d005_gsm8k\": 0.4947, \"S4_d005_arc\": 0.4325, \"signals_surviving\": 0, \"signals_total\": 3}, \"notes\": \"0/3 signals survive across regimes. S1 Embedding: AUC 0.95-0.995 at d005 but random at d000/d100 (ceiling effect at full contamination). S2 Min-K++ and S4 Self-Critique: random across all regimes (0.43-0.57). ConStat (S3) not computed (needs paraphrase data). Result validates C2: individual signals insufficient → need IRT multi-signal fusion.\", \"checkpoint_path\": \"N/A (analysis experiment, no checkpoint)\", \"log_path\": \"/root/contamcal-irt-calibration/exp008/signal_survival_analysis.log\", \"completed_at\": \"2026-05-14T16:16:31.712Z\"}, \"exp_001_eval_3B_d100_aligned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:56:44.974Z\", \"updated_at\": \"2026-05-14T15:33:27.101Z\", \"spec\": {\"command\": \"run_eval_3B_d100_auto.sh → evaluate.py --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:3\", \"data_path\": \"MMLU+ARC+GSM8K+HumanEval\", \"data_count\": 16697, \"model_name\": \"Qwen2.5-3B\", \"seed\": 42, \"checkpoint_source\": \"exp_001_sft_d100_3B\", \"eval_data\": \"original\", \"mc_format\": \"aligned (D017)\", \"log_path\": \"/root/runs/contamcal-irt-calibration/eval_3B_d100_aligned.log\", \"output_dir\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_s42_aligned/\", \"pid\": 362942, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s42/lora_adapter/\"}, \"hypothesis\": \"3B d100 s42 aligned eval — 100% contamination at largest scale, upper bound for 3B dose-response (MMLU/ARC only, GSM8K excluded per D018)\", \"parent\": \"exp_001_sft_d100_3B\", \"notes\": \"重跑成功。PID 362942 GPU 3。4 benchmarks 全部完成: MMLU 64.17%, GSM8K 69.67%, ARC 83.96%, HumanEval 12.20%。运行时间约 3h16m (20:06-23:22)。\", \"reproduce\": {\"finished_at\": \"2026-05-14T15:32:45.130Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T15:32:43.340Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T15:32:59.749439+00:00\"}]}, \"metrics\": {\"mmlu_accuracy\": 0.6417, \"gsm8k_exact_match\": 0.6967, \"arc_challenge_accuracy\": 0.8396, \"humaneval_pass1\": 0.122}}, \"exp_001_eval_05B_d005_aligned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:20:22.394Z\", \"updated_at\": \"2026-05-14T15:21:22.628Z\", \"spec\": {\"hypothesis\": \"0.5B d005 s42 aligned eval — 5% contamination dose-response point (original aligned format D017)\", \"parent\": \"exp_001_sft_d005_05B_v3\", \"model_name\": \"Qwen2.5-0.5B\", \"seed\": 42, \"server\": \"cqa1-21977\", \"command\": \"part of aligned_batch run (completed before batch timeout)\", \"data_path\": \"MMLU+GSM8K+ARC+HumanEval aligned\", \"data_count\": 16697, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42/lora_adapter\", \"eval_data\": \"original aligned (D017)\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d005_s42_aligned\", \"log_path\": \"N/A (batch run)\"}, \"metrics\": {\"d005_aligned_mmlu\": 0.3255, \"d005_aligned_gsm8k\": 0.3624, \"d005_aligned_arc\": 0.3285, \"d005_aligned_humaneval\": 0.0793}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T15:21:22.628Z\"}, \"exp_001_eval_05B_d100_aligned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T14:50:02.679Z\", \"updated_at\": \"2026-05-14T15:19:06.659Z\", \"hypothesis\": \"0.5B d100 s42 aligned eval resubmit — d100 original + paraphrase, split from failed batch to avoid timeout\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 timeout 4h python exp001/evaluate.py ... d100 aligned + para_aligned serial\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:2\", \"pid\": \"389866\", \"data_path\": \"MMLU+GSM8K+ARC original+paraphrase\", \"data_count\": \"2 runs\", \"model_name\": \"Qwen2.5-0.5B d100 s42\", \"seed\": 42, \"checkpoint_source\": \"exp_001_sft_d100_05B\", \"eval_data\": \"original + paraphrase aligned (D017)\"}, \"notes\": \"PID 389866 仍在运行（ps 确认 state=Rl, elapsed=19:31），tmux session 已死但 python 进程存活。Cron 误报 process gone（miss 4/5）因 tmux 检测失效。MMLU 已完成，GSM8K/ARC/HumanEval 进行中。等进程完成后立即提交 d100 paraphrase eval（--output-dir Qwen2.5-0.5B_d100_s42_para_aligned --paraphrase）。GPU 2 仍在使用。\", \"reproduce\": {\"finished_at\": \"2026-05-14T15:10:41.931Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T15:10:45.874Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T15:10:55.329493+00:00\"}]}}, \"exp_001_eval_05B_aligned_batch\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T08:38:53.976Z\", \"updated_at\": \"2026-05-14T15:15:40.960Z\", \"hypothesis\": \"0.5B aligned-format eval batch (D017): d000/d005/d100 × original + paraphrase = 6 eval runs. Formal analysis results replacing legacy mc_format.\", \"spec\": {\"command\": \"bash run_aligned_eval_05B.sh both\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:2\", \"pid\": \"332207\", \"data_path\": \"MMLU+ARC+GSM8K+HumanEval original+paraphrase\", \"data_count\": \"3 dosages × 2 eval_types × 4 benchmarks\", \"model_name\": \"Qwen2.5-0.5B\", \"seed\": 42, \"checkpoint_source\": \"exp_001_sft_0pct_05B / exp_001_sft_d005_05B_v3 / exp_001_sft_d100_05B\", \"eval_data\": \"original + paraphrase\", \"mc_format\": \"aligned (D017)\"}, \"parent\": \"exp_001_sft_d025_05B_v3\", \"notes\": \"0.5B aligned batch eval 因 timeout (EXIT_CODE=124) 中断。实际完成 4/6 runs: d000 orig+para, d005 orig+para 结果完整。d100 orig（仅跑48min被kill）+ d100 para（未启动）缺失。Timeline: d000_orig 18:52→d000_para 19:15→d005_orig 21:26→d005_para 21:51→d100_orig killed 22:39。d100 已单独重提交到 GPU 2。d005 指标待补录。d000 metrics: MMLU=39.79%, GSM8K=36.92%, ARC=46.93%, HumanEval=10.98%; d000_para: MMLU=44.28%, GSM8K=28.07%, ARC=47.92%, HumanEval=11.54%.\", \"metrics\": {\"d000_aligned_mmlu\": 0.3979, \"d000_aligned_gsm8k\": 0.3692, \"d000_aligned_arc\": 0.4693, \"d000_aligned_humaneval\": 0.1098, \"d000_para_aligned_mmlu\": 0.4428, \"d000_para_aligned_gsm8k\": 0.2807, \"d000_para_aligned_arc\": 0.4792, \"d000_para_aligned_humaneval\": 0.1154, \"d005_aligned_mmlu\": 0.3255, \"d005_aligned_gsm8k\": 0.3624, \"d005_aligned_arc\": 0.3285, \"d005_aligned_humaneval\": 0.0793}, \"reproduce\": {\"finished_at\": \"2026-05-14T14:39:10.195Z\"}, \"failure_reason\": \"EXIT_CODE=124 (timeout — exceeded timeout_hours)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T14:39:14.014Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T14:39:18.504423+00:00\"}]}}, \"exp_001_eval_05B_d005\": {\"created_at\": \"2026-05-14T01:17:07.820Z\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d005_s42\", \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42/lora_adapter\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d005_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\", \"data_count\": 0, \"data_path\": \"d005 contaminated checkpoint\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"gpu\": \"cuda:1\", \"hypothesis\": \"0.5B 5% dosage contaminated model eval on 4 benchmarks — low-dosage contamination detection sensitivity test\", \"log_path\": \"/root/runs/contamcal-irt-calibration/exp_001_eval_05B_d005.log\", \"model_name\": \"Qwen2.5-0.5B\", \"parent\": \"exp_001_sft_d005_05B\", \"pid\": \"255322\", \"seed\": 42, \"server\": \"cqa1-21977\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T15:10:32.421Z\", \"reproduce\": {\"finished_at\": \"2026-05-14T06:44:49.861Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T06:44:50.409Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T06:44:51.900757+00:00\"}]}, \"notes\": \"⚠️ legacy mc_format — 仅供诊断参考，正式分析需用 aligned 格式重跑 (D017 延伸决策)。\", \"metrics\": {\"mmlu\": 0.2929, \"gsm8k\": 0.3601, \"arc_challenge\": 0.2858, \"humaneval_pass1\": 0.0793, \"mmlu_correct\": 4113, \"mmlu_total\": 14042, \"gsm8k_correct\": 475, \"gsm8k_total\": 1319, \"arc_correct\": 335, \"arc_total\": 1172, \"humaneval_correct\": 13, \"humaneval_total\": 164}}, \"exp_006_irt_05B\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T14:20:20.389Z\", \"updated_at\": \"2026-05-14T14:53:16.180Z\", \"spec\": {\"command\": \"python run_exp006.py (Stan NUTS 4 chains, warmup=1000, samples=1000, max_depth=12, delta=0.95)\", \"server\": \"cqa1-21977\", \"data_path\": \"exp002 signals → exp006 direct load\", \"data_count\": \"MMLU 14042 items × 9 models (first benchmark)\", \"model_name\": \"contam_irt_4pl_simple (Stan NUTS)\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/exp006/results_05B/\", \"log_path\": \"/root/runs/contamcal-irt-calibration/exp006_irt_05B.log\", \"pid\": \"386298\"}, \"notes\": \"KILLED by Director 指令: 混合 scale (0.5B+1.5B+3B) + legacy 格式 + 多余 seed 的错误数据在拟合。Stan NUTS 4 chains (PID 386298-386301) 运行 ~30min 后终止。代码修复中: 正则改为 _d(\\\\d+)_s(\\\\d+)(_para)?(_aligned)?$, 增加 --model-scale 和 --seed 过滤参数。等 d025/d100 aligned eval 完成后再用修复后代码重跑。\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T14:53:12.892Z\"}, \"exp_003_rrf_05B\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T14:17:36.003Z\", \"updated_at\": \"2026-05-14T14:18:05.370Z\", \"spec\": {\"command\": \"python rrf_aggregation.py --generate-exposure\", \"server\": \"cqa1-21977\", \"data_path\": \"/root/autodl-tmp/exp002/signals/\", \"data_count\": \"3 dosages x 3 benchmarks = 9 signal sets\", \"model_name\": \"Qwen2.5-0.5B\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/exp003/exposure_scores.json\", \"log_path\": \"N/A\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T14:18:05.370Z\"}, \"exp_002_signals_05B\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-14T08:45:35.964Z\", \"updated_at\": \"2026-05-14T14:04:12.884Z\", \"hypothesis\": \"0.5B contamination signal computation (S1 Embedding/S2 Min-K++/S4 Self-Critique) on d000/d005/d100 × mmlu/gsm8k/arc = 27 signal tasks. Critical path for exp-003 RRF → exp-006 IRT.\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration/exp002 && python run_batch.py --model-size 0.5B --gpu 0 2>&1 | tee run_05B.log\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:0\", \"pid\": 370957, \"data_path\": \"/root/autodl-tmp/exp001/eval_results/ + /root/autodl-tmp/exp001/checkpoints/\", \"data_count\": \"3 dosages x 3 benchmarks x 3 signals = 27 tasks (6 cached, ~21 remaining)\", \"model_name\": \"Qwen2.5-0.5B\", \"seed\": 42, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_002_signals_05B.log\", \"checkpoint_path\": \"/root/autodl-tmp/exp002/signals/\", \"signals\": [\"embedding\", \"minkpp\", \"selfcritique\"], \"note\": \"v5 restart: timeout 4h, per-signal cache, selfcritique max_tokens 64. 6 signals cached from v4.\"}, \"notes\": \"v5 完成 9/9 PASS。d000/d005/d100 × mmlu/gsm8k/arc_challenge 全部完成。9 个 signals_merged 文件已产出。三项修复奏效: timeout 4h, per-signal cache, max_tokens 64。GPU 0 已释放。\", \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T14:04:10.508Z\"}, \"exp_001_eval_3B_d000_aligned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T09:30:50.047Z\", \"updated_at\": \"2026-05-14T13:11:39.859Z\", \"hypothesis\": \"3B d000 s42 aligned eval (v5 代码) — 诊断 GSM8K 崩塌 (0.117→?) 并建立正式 aligned baseline。含 GSM8K 答案提取修复（如需要）。\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42_aligned/\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d000_aligned.log\"}, \"notes\": \"D018 决策：3B GSM8K 标记为 \\\"SFT-degraded, excluded from dose-response\\\"。3B MMLU/ARC 仍可用。不重训 LoRA 配置。诊断根因：LoRA SFT (r=16, alpha=32, lr=2e-4, 7 proj) 导致 CoT 灾难性遗忘。\", \"reproduce\": {\"finished_at\": \"2026-05-14T13:05:47.172Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T13:05:58.887588+00:00\"}]}, \"metrics\": {\"mmlu_accuracy\": 0.634, \"gsm8k_exact_match\": 0.1198, \"arc_challenge_accuracy\": 0.8276, \"humaneval_pass_at_1\": 0.1159}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T13:10:19.068Z\"}, \"exp_001_eval_15B_d100_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T07:39:14.296Z\", \"updated_at\": \"2026-05-14T10:22:16.449Z\", \"spec\": {\"command\": \"python evaluate.py --model-path Qwen2.5-1.5B --adapter-path Qwen2.5-1.5B_d100_s42/lora_adapter --benchmarks mmlu gsm8k arc_challenge humaneval\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:0\"], \"pid\": \"325300\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_15B_d100_s42.log\", \"submitted_at\": \"2026-05-14T07:39:13.887Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d100_s42/lora_adapter\", \"data_count\": 4, \"model_name\": \"Qwen2.5-1.5B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d100_s42/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s42\", \"wall_clock_seconds\": 9420, \"gpu_hours\": 2.62}, \"hypothesis\": \"100% dosage 1.5B s42 contaminated eval on 4 benchmarks — upper bound contamination score inflation for 1.5B scale\", \"parent\": \"exp_001_sft_d100_15B_v2\", \"notes\": \"使用 D017 aligned 格式 (--mc-format aligned, 默认)。与 0.5B v5 eval (legacy 格式) 不直接可比。分析时需标注 mc_format。\", \"reproduce\": {\"finished_at\": \"2026-05-14T10:17:43.615Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T10:17:48.927069+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"mmlu_accuracy\": 0.5933, \"mmlu_correct\": 8331, \"mmlu_total\": 14042, \"gsm8k_exact_match\": 0.6497, \"gsm8k_correct\": 857, \"gsm8k_total\": 1319, \"arc_challenge_accuracy\": 0.7688, \"arc_challenge_correct\": 901, \"arc_challenge_total\": 1172, \"humaneval_pass_at_1\": 0.3049, \"humaneval_correct\": 50, \"humaneval_total\": 164}, \"completed_at\": \"2026-05-14T10:21:14.812Z\"}, \"exp_001_eval_3B_raw_gen\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T06:52:48.654Z\", \"updated_at\": \"2026-05-14T10:04:16.309Z\", \"spec\": {\"command\": \"python evaluate.py --model-path Qwen2.5-3B --benchmarks gsm8k humaneval\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:5\"], \"pid\": \"318748\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_raw_gen.log\", \"submitted_at\": \"2026-05-14T06:52:48.549Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B\", \"data_count\": 2, \"model_name\": \"Qwen2.5-3B\", \"seed\": 0, \"eval_data\": \"gsm8k,humaneval\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_raw/\", \"wall_clock_seconds\": 11487.8, \"gpu_hours\": 3.19}, \"reproduce\": {\"finished_at\": \"2026-05-14T09:34:31.469Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T09:34:36.144359+00:00\"}]}, \"metrics\": {\"gsm8k\": 0.605, \"humaneval\": 0}, \"notes\": \"3B raw base eval (generative benchmarks). GSM8K=0.6050 正常。HumanEval=0.0000: base model 生成教程式文本+markdown代码块，评估器无法提取可执行代码。结果文件: /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_raw/。GSM8K 0.605 vs d000 SFT 0.117 = -48.8pp 崩塌待诊断。\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T10:04:16.309Z\"}, \"exp_001_eval_05B_raw\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T06:52:20.023Z\", \"updated_at\": \"2026-05-14T09:18:21.577Z\", \"hypothesis\": \"Raw Qwen2.5-0.5B base model eval (no SFT, no adapter) on 4 benchmarks — establish true pre-SFT baseline for MC distribution analysis\", \"spec\": {\"command\": \"evaluate.py on raw Qwen2.5-0.5B (no adapter)\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:1\", \"pid\": \"318424\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_raw.log\", \"submitted_at\": \"2026-05-14T06:52:25.551Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"MMLU+GSM8K+ARC+HumanEval\", \"data_count\": 4, \"model_name\": \"Qwen2.5-0.5B (raw base)\", \"seed\": 42, \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"checkpoint_path\": \"N/A (raw base)\", \"wall_clock_seconds\": 8756.0, \"gpu_hours\": 2.43}, \"conclusion\": \"success\", \"metrics\": {\"mmlu\": 0.2302, \"gsm8k\": 0.1592, \"arc_challenge\": 0.2261, \"humaneval\": \"incomplete (hung at 51/164)\"}, \"notes\": \"Raw 0.5B base model eval。MMLU/GSM8K/ARC 完成，HumanEval 卡在 51/164 (代码执行死循环)，kill 释放 cuda:1。HumanEval 为 appendix-only (D009)，不影响主分析。Raw base 分数远低于 SFT d000 baseline (MMLU 0.23 vs 0.40)，确认 SFT 有效提升。\", \"completed_at\": \"2026-05-14T09:18:21.577Z\"}, \"exp_001_sft_d005_15B\": {\"created_at\": \"2026-05-14T00:19:54.331Z\", \"gpu\": 4, \"hypothesis\": \"5% dosage contaminated SFT on Qwen2.5-1.5B (seed=42): low-dosage contamination for dose-response curve, Phase 3 priority 1\", \"retry_count\": 0, \"server\": \"cqa1-21977\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s42\", \"command\": \"train_sft.py --model-name Qwen2.5-1.5B --data-path sft_dosage_005.jsonl\", \"data_count\": 50826, \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl\", \"gpu\": \"cuda:4\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_d005_15B.log\", \"model_name\": \"Qwen2.5-1.5B\", \"pid\": \"271916\", \"seed\": 42, \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-14T03:12:39.622Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 20070.3, \"gpu_hours\": 5.58}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T09:11:14.625Z\", \"reproduce\": {\"finished_at\": \"2026-05-14T08:47:04.834Z\"}, \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T08:47:09.892Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T08:47:17.186022+00:00\"}]}, \"notes\": \"训练实际已完成。3177/3177 steps, train_loss=1.2637, mean_token_accuracy=0.7308, epoch=1.0。LoRA adapter 已保存。EXIT_CODE=129 (SIGHUP) 发生在 Training complete 之后，属于 wrapper PID false positive（与 exp_001_sft_d100_3B 同一已知模式）。Checkpoint: /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s42/lora_adapter\", \"metrics\": {\"train_loss\": 1.2637, \"mean_token_accuracy\": 0.7308, \"train_runtime_s\": 19864.7, \"epoch\": 1}}, \"exp_001_sft_d025_05B_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T06:22:14.069Z\", \"updated_at\": \"2026-05-14T08:36:01.933Z\", \"spec\": {\"command\": \"python train_sft.py --model Qwen2.5-0.5B --data sft_dosage_025.jsonl --gpu 2 --seed 42\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:2\"], \"pid\": \"324153\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_d025_05B_v3.log\", \"submitted_at\": \"2026-05-14T07:31:46.339Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_025.jsonl\", \"data_count\": 54133, \"model_name\": \"Qwen2.5-0.5B\", \"seed\": 42, \"wall_clock_seconds\": 3855.6, \"gpu_hours\": 1.07}, \"hypothesis\": \"25% dosage contaminated SFT on Qwen2.5-0.5B (seed=42, v3) — 用于 dose-response 曲线的 mid-low dosage 数据点\", \"reproduce\": {\"finished_at\": \"2026-05-14T08:31:11.706Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T08:31:17.136838+00:00\"}]}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d025_s42/lora_adapter\", \"metrics\": {\"final_loss\": 1.5178, \"mean_train_loss\": 1.5479, \"entropy\": 1.5415, \"mean_token_accuracy\": 0.6697, \"num_tokens\": 20058085, \"total_steps\": 3384, \"epoch\": 1, \"train_samples_per_second\": 15.52, \"train_steps_per_second\": 0.97, \"training_time_min\": 58.1, \"exit_code\": 0, \"lora_adapter_size_mb\": 33.6, \"checkpoint_size_mb\": 166, \"vs_baseline_0pct\": {\"baseline_final_loss\": 1.4894, \"baseline_mean_train_loss\": 1.5388, \"baseline_token_accuracy\": 0.682, \"baseline_training_time_min\": 52.9, \"delta_final_loss\": 0.0284, \"delta_mean_train_loss\": 0.0091, \"delta_token_accuracy\": -0.0123, \"delta_training_time_min\": 5.2}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T08:36:01.933Z\"}, \"exp_001_eval_05B_d100_v5\": {\"created_at\": \"2026-05-14T02:39:57.338Z\", \"hypothesis\": \"100% dosage 0.5B s42 contaminated eval (v5, 最终干净提交)\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42\", \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42/lora_adapter\", \"command\": \"bash -c \\\"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && ... && python evaluate.py ...\\\"\", \"data_count\": 4, \"data_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"gpu\": [\"cuda:2\"], \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d100_v5.log\", \"model_name\": \"Qwen2.5-0.5B\", \"parent\": \"exp_001_sft_d100_05B\", \"pid\": \"266780\", \"seed\": 42, \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-14T02:39:57.046Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 17504.7, \"gpu_hours\": 4.86}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T08:01:34.216Z\", \"reproduce\": {\"finished_at\": \"2026-05-14T07:30:37.450Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T07:30:41.628489+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"mmlu\": 0.2322, \"gsm8k\": 0.3571, \"arc_challenge\": 0.227, \"humaneval_pass1\": 0.0854}, \"completed_at\": \"2026-05-14T07:31:41.784Z\", \"notes\": \"结果文件: /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42/。⚠️ legacy mc_format — 仅供诊断参考，正式分析需用 aligned 格式重跑 (D017 延伸决策)。d100 MC 分数低于 d000 baseline (MMLU -17.3pp, ARC -15.1pp) 系格式不匹配所致。\"}, \"exp_001_eval_05B_d000_s42_v5\": {\"created_at\": \"2026-05-14T02:39:41.292Z\", \"hypothesis\": \"0% dosage 0.5B s42 baseline eval (v5, 最终干净提交)\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42\", \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter\", \"command\": \"bash -c \\\"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && ... && python evaluate.py ...\\\"\", \"data_count\": 4, \"data_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"gpu\": [\"cuda:2\"], \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s42_v5.log\", \"model_name\": \"Qwen2.5-0.5B\", \"parent\": \"exp_001_sft_0pct_05B\", \"pid\": \"266511\", \"seed\": 42, \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-14T02:39:41.108Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 17519.2, \"gpu_hours\": 4.87}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T08:01:31.086Z\", \"reproduce\": {\"finished_at\": \"2026-05-14T07:30:31.429Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T07:30:35.061894+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"mmlu\": 0.4049, \"gsm8k\": 0.3647, \"arc_challenge\": 0.378, \"humaneval\": 0.1098}, \"completed_at\": \"2026-05-14T07:31:40.285Z\", \"notes\": \"结果文件: /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42/。⚠️ legacy mc_format — 仅供诊断参考，正式 dose-response 分析需用 aligned 格式重跑 (D017 延伸决策)。\"}, \"exp_001_sft_d100_15B_v2\": {\"created_at\": \"2026-05-14T01:17:47.114Z\", \"parent\": \"exp_001_sft_d100_15B\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d100_s42\", \"command\": \"python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d100_s42 --seed 42 --gpu 0 --batch-size 1 --grad-accum 16 --cache-dir /root/autodl-tmp/.hf_cache\", \"data_count\": 66533, \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl\", \"gpu\": [\"cuda:0\"], \"hypothesis\": \"100% dosage contaminated SFT on Qwen2.5-1.5B (seed=42): v2 retry with batch_size=1 to fix OOM. Maximum contamination for 1.5B scale.\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_d100_15B_v2.log\", \"model_name\": \"Qwen2.5-1.5B\", \"pid\": \"251924\", \"seed\": 42, \"server\": \"cqa1-21977\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T07:39:22.684Z\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T07:39:22.684Z\"}, \"exp_001_eval_3B_d000_s42\": {\"completed_at\": \"2026-05-13T23:43:16.876Z\", \"created_at\": \"2026-05-13T23:36:54.086Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"v1 --gpu param caused evaluate.py crash. Resubmitted without --gpu.\"}, \"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T06:47:56.373112+00:00\"}]}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"hypothesis\": \"0% dosage 3B s42 baseline evaluation on 4 benchmarks (mmlu, gsm8k, arc_challenge, humaneval) to establish ground-truth scores for calibration error computation\", \"notes\": \"v1 failed (--gpu bug), v2 resubmitted with CUDA_VISIBLE_DEVICES. PID 249294 confirmed running on GPU 1 (cron monitored).\", \"parent\": \"exp_001_sft_0pct_3B\", \"retry_count\": 1, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter\", \"command\": \"bash -c \\\"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1 && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\\\"\", \"data_count\": 26000, \"data_path\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"gpu\": [\"cuda:1\"], \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d000_s42.log\", \"model_name\": \"Qwen2.5-3B\", \"pid\": \"249294\", \"seed\": 42, \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-14T08:54:00Z\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T07:03:36.187Z\", \"reproduce\": {\"finished_at\": \"2026-05-14T06:47:54.565Z\"}, \"conclusion\": \"success\", \"metrics\": {\"mmlu\": 0.634, \"gsm8k\": 0.117, \"arc\": 0.822, \"humaneval\": 0.116}}, \"exp_001_sft_d025_05B_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T04:53:14.092Z\", \"updated_at\": \"2026-05-14T06:21:14.334Z\", \"hypothesis\": \"25% dosage contaminated SFT on Qwen2.5-0.5B (seed=42): v2 retry with correct CUDA_VISIBLE_DEVICES=5 binding. Dose-response curve intermediate point.\", \"parent\": \"exp_001_sft_d025_05B\", \"spec\": {\"pid\": 299016, \"gpu\": [\"cuda:5\"], \"server\": \"cqa1-21977\", \"command\": \"bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration/exp001 && export CUDA_VISIBLE_DEVICES=5 && python train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_025.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d025_s42 --gpu 0 --batch-size 4 --grad-accum 4 --epochs 1 --lr 2e-4 --lora-r 16 --lora-alpha 32 --seed 42 --cache-dir /root/autodl-tmp/.hf_cache'\", \"model_name\": \"Qwen2.5-0.5B\", \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_025.jsonl\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d025_s42\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_d025_05B_v2.log\"}, \"conclusion\": \"failed\", \"failure_reason\": \"SIGKILL (exit 137) at step 36/3384. Training command lacked proper CUDA_VISIBLE_DEVICES export — likely landed on GPU 0 conflicting with 1.5B d100 SFT, causing OOM. PID 296698 killed, PID 299016 is residual wrapper.\", \"completed_at\": \"2026-05-14T06:21:14.334Z\"}, \"exp_001_eval_05B_d100_v2\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-14T02:26:41.093Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-14T02:37:02.468237+00:00\"}]}, \"failure_reason\": \"EXIT_CODE=137 (SIGKILL — OOM killer or manual kill)\", \"reproduce\": {\"finished_at\": \"2026-05-14T02:36:56.211Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1 && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\\\"\", \"gpu\": [\"cuda:2\"], \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d100_v2.log\", \"pid\": \"263784\", \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-14T02:28:36.407Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 13875.1, \"gpu_hours\": 3.85}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T06:19:51.550Z\", \"completed_at\": \"2026-05-14T06:19:51.550Z\"}, \"exp_001_sft_d025_05B\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T04:24:39.757Z\", \"updated_at\": \"2026-05-14T04:54:16.202Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration/exp001 && python train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_025.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d025_s42 --gpu 0 --batch-size 4 --grad-accum 4 --epochs 1 --lr 2e-4 --lora-r 16 --lora-alpha 32 --seed 42 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:5\"], \"pid\": \"292940\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_d025_05B.log\", \"submitted_at\": \"2026-05-14T04:49:12Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"Qwen2.5-0.5B\", \"seed\": 42, \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_025.jsonl\", \"data_count\": \"~16633 (25% dosage)\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d025_s42\", \"wall_clock_seconds\": 75.0, \"gpu_hours\": 0.02}, \"reproduce\": {\"finished_at\": \"2026-05-14T04:50:22.652Z\"}, \"failure_reason\": \"CUDA OOM: 分配 cuda:5 但实际跑到 GPU 0（CUDA_VISIBLE_DEVICES 注入失效，已知 recurring bug）。GPU 0 被 exp_001_sft_d100_15B_v2 (9.81GiB) + PID 291380 (13GiB) 占满。修复：命令中显式 export CUDA_VISIBLE_DEVICES=5。\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T04:50:27.011Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T04:50:31.770719+00:00\"}]}, \"notes\": \"OOM失败：指定 cuda:5 但实际跑到 GPU 0。GPU 5 上残留 4 个重复 1.5B d005 进程 (PID 292422/292423/292425/292426)。根因：tmux 提交时未设 CUDA_VISIBLE_DEVICES，--gpu 参数未正确绑定设备。\"}, \"exp_001_eval_3B_d000_s123\": {\"created_at\": \"2026-05-14T00:18:07.960Z\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s123/lora_adapter\", \"command\": \"bash -c \\\"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1 && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s123 --benchmarks mmlu gsm8k arc_challenge humaneval\\\"\", \"data_count\": 26000, \"data_path\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"gpu\": [\"cuda:3\"], \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d000_s123.log\", \"model_name\": \"Qwen2.5-3B\", \"pid\": \"242581\", \"seed\": 123, \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-14T00:18:36.008Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 15706.2, \"gpu_hours\": 4.36, \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s123\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T04:44:59.509Z\", \"reproduce\": {\"finished_at\": \"2026-05-14T04:39:50.139Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T04:39:53.713806+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"mmlu_accuracy\": 0.6362, \"gsm8k_exact_match\": 0.1759, \"arc_challenge_accuracy\": 0.8294, \"humaneval_pass_at_1\": 0.0854}, \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s123\", \"completed_at\": \"2026-05-14T04:40:22.199Z\"}, \"exp_001_eval_15B_d000_s123\": {\"completed_at\": \"2026-05-13T23:39:26.418Z\", \"created_at\": \"2026-05-13T22:30:41.501Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\"}, \"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T04:42:53.247372+00:00\"}]}, \"failure_reason\": \"EXIT_CODE=2: --gpu 0 参数导致 evaluate.py 崩溃。重跑时需去掉 --gpu 参数。\", \"retry_count\": 1, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s123\", \"checkpoint_source\": \"exp_001_sft_0pct_15B_s123\", \"command\": \"bash -c \\\"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1 && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s123 --benchmarks mmlu gsm8k arc_challenge humaneval\\\"\", \"data_count\": \"4 benchmarks\", \"data_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s123/\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"gpu\": [\"cuda:5\"], \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_15B_d000_s123.log\", \"model_name\": \"Qwen2.5-1.5B\", \"pid\": \"250600\", \"seed\": 123, \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-14T00:59:22.874Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 13475.7, \"gpu_hours\": 3.74}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T04:43:58.619Z\", \"reproduce\": {\"finished_at\": \"2026-05-14T04:42:48.051Z\"}, \"conclusion\": \"success\", \"metrics\": {\"mmlu\": 0.5762, \"gsm8k\": 0.6331, \"arc_challenge\": 0.7662, \"humaneval_pass@1\": 0.1707}}, \"exp_005_noise_prop_v2\": {\"completed_at\": \"2026-05-13T22:44:09.262Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-13T20:47:35.807Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-13T21:09:53.826444+00:00\"}, {\"action\": \"manual_fix\", \"event\": \"status_rollback\", \"reason\": \"Cron false positive: server=\\\"local\\\" not in SSH list. PID 251971 alive, 2 Stan chains at 42% CPU. Rolled back DONE/failed → RUNNING.\", \"ts\": \"2026-05-13T21:12:00.000Z\"}]}, \"failure_reason\": \"根因：/tmp tmpfs 磁盘配额耗尽。ME model 先跑 95min 生成 ~1GB CSV（9000 tau + 9000 log_lik × 4 chains）耗尽 3.9GB tmpfs。Simple model 写 CSV 时 disk quota exceeded → 4 chains 全部 retcode=1。ME model Rhat=1.945 是独立问题：10231 参数 vs 9000 观测，严重欠识别，需换用 analytic 版本。修复：(1) output_dir 设到非 tmpfs (2) 先跑 simple 再跑 ME (3) ME 换 contam_irt_4pl_me_analytic.stan (4) σ_e=0.1/0.3 均可收敛。\", \"hypothesis\": \"Same as exp_005: ME model CI width increases monotonically with σ_e; simple model does not. v2 fixes: sigma_e lower bound 1e-4, c/d bounds [0.001,0.999], max_treedepth=12.\", \"notes\": \"失败根因: 1) /tmp tmpfs 3.9GB 耗尽（ME模型生成~1GB Stan CSV，Simple 4 chains全部retcode=1）; 2) ME模型严重欠识别（10231参数 vs 9000观测，Rhat=1.945）。诊断结果: σ_e=0.3 simple收敛良好(γ=0.458, true=0.5, Rhat=1.007); σ_e=0.1 simple收敛但γ偏高57.5%(0.788 vs 0.5)——identifiability限制非bug。v3已启动修复两个根因。\", \"parent\": \"exp_005_noise_prop\", \"retry_count\": 0, \"spec\": {\"command\": \"python run_noise_propagation.py --output-dir output_v2 --base-seed 42 --n-seeds 5\", \"data_count\": \"5 σ_e levels × 5 seeds × 2 models = 50 Stan fits\", \"data_path\": \"synthetic (generated in-script)\", \"fixes\": \"sigma_e lower bound 1e-4, c/d bounds [0.001,0.999], max_treedepth=12\", \"log_path\": \"artifacts/exp005_noise_propagation/exp005_v2.log\", \"model_name\": \"4PL+γ IRT (CmdStanPy NUTS, max_treedepth=12)\", \"pid\": 251971, \"seed\": \"42-46\", \"server\": \"local (CPU only)\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T03:25:33.715Z\"}, \"exp_001_eval_15B_d000_s42_v2\": {\"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s42/lora_adapter\", \"completed_at\": \"2026-05-14T03:12:11.373Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-14T00:23:20.112Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-14T03:09:29.636850+00:00\"}]}, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_15B_d000_s42_v2.log\", \"metrics\": {\"arc_challenge_accuracy\": 0.7756, \"arc_challenge_correct\": 909, \"arc_challenge_total\": 1172, \"gsm8k_correct\": 840, \"gsm8k_exact_match\": 0.6368, \"gsm8k_total\": 1319, \"humaneval_correct\": 21, \"humaneval_pass_at_1\": 0.128, \"humaneval_total\": 164, \"mmlu_accuracy\": 0.5753, \"mmlu_correct\": 8079, \"mmlu_total\": 14042}, \"reproduce\": {\"finished_at\": \"2026-05-14T03:09:26.521Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s42/lora_adapter\", \"command\": \"bash -c \\\"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_HUB_DISABLE_XET=1 && cd /root/contamcal-irt-calibration/exp001 && python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\\\"\", \"data_count\": 26000, \"data_path\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"gpu\": [\"cuda:4\"], \"gpu_hours\": 2.81, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_15B_d000_s42_v2.log\", \"model_name\": \"Qwen2.5-1.5B\", \"pid\": \"243290\", \"seed\": 42, \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-14T00:23:34.122Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 10117.3}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T03:12:11.373Z\"}, \"exp_001_eval_05B_d100\": {\"completed_at\": \"2026-05-14T02:21:35.372Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-14T01:15:49.903Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-14T02:21:37.615359+00:00\"}]}, \"failure_reason\": \"EXIT_CODE=143 (SIGTERM — graceful kill)\", \"reproduce\": {\"finished_at\": \"2026-05-14T02:21:33.626Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42\", \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42/lora_adapter\", \"command\": \"python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42 --benchmarks mmlu gsm8k arc_challenge humaneval\", \"data_count\": 4, \"data_path\": \"d100 contaminated checkpoint\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\", \"gpu\": [\"cuda:2\"], \"gpu_hours\": 0.88, \"gpu_ids\": [\"cuda:2\"], \"hypothesis\": \"0.5B 100% dosage contaminated model eval on 4 benchmarks — upper bound of contamination-induced score inflation\", \"log_path\": \"/tmp/eval_d100.log\", \"model_name\": \"Qwen2.5-0.5B\", \"parent\": \"exp_001_sft_d100_05B\", \"pid\": \"254667\", \"seed\": 42, \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-14T01:29:00Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 3155.4}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T02:21:35.372Z\"}, \"exp_001_eval_05B_d000_s123\": {\"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s123/lora_adapter\", \"completed_at\": \"2026-05-14T01:29:09.875Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-13T22:30:40.455Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-14T01:26:32.038369+00:00\"}]}, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s123.log\", \"metrics\": {\"arc_challenge_accuracy\": 0.3976, \"gsm8k_exact_match\": 0.3404, \"humaneval_pass_at_1\": 0.1037, \"mmlu_accuracy\": 0.4182}, \"reproduce\": {\"finished_at\": \"2026-05-14T01:26:29.607Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s123/lora_adapter\", \"command\": \"python evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s123 --benchmarks mmlu gsm8k arc_challenge humaneval\", \"data_count\": null, \"data_path\": \"d000 (baseline, no contamination)\", \"eval_data\": \"mmlu gsm8k arc_challenge humaneval\", \"gpu\": [\"cuda:2\"], \"gpu_hours\": 2.72, \"gpu_ids\": [\"cuda:2\"], \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_05B_d000_s123.log\", \"model_name\": \"Qwen2.5-0.5B\", \"parent\": \"exp_001_train_05B_d000_s123\", \"pid\": \"229516\", \"seed\": 123, \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-13T22:45:48.124Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 9801.8}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T01:29:09.875Z\"}, \"exp_001_sft_d100_15B\": {\"completed_at\": \"2026-05-14T01:23:40.712Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-13T23:37:43.653Z\", \"failure_reason\": \"OOM batch_size=2, replaced by v2\", \"hypothesis\": \"100% dosage contaminated SFT on Qwen2.5-1.5B (seed=42): mid-size model maximum contamination, extends dose-response curve to 1.5B scale; paired with 0.5B d100 to measure scale effect on calibration error\", \"notes\": \"batch_size=1, grad_accum=16 (防 OOM，与 1.5B d000 baseline 一致)。66533 samples, 1 epoch。数据与 0.5B d100 完全相同，含 MMLU+ARC+GSM8K 全部 paraphrases（noisy contamination condition）。\", \"retry_count\": 0, \"spec\": {\"command\": \"python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d100_s42 --seed 42 --gpu 0 --batch-size 2 --grad-accum 8 --cache-dir /root/autodl-tmp/.hf_cache\", \"data_count\": 66533, \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl\", \"gpu\": [\"cuda:0\"], \"log_path\": \"/root/runs/contamcal-irt-calibration/exp_001_sft_d100_15B.log\", \"model_name\": \"Qwen2.5-1.5B\", \"pid\": \"248993\", \"seed\": 42, \"server\": \"cqa1-21977\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T01:23:40.711Z\"}, \"exp_001_sft_d005_05B_v3\": {\"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42\", \"completed_at\": \"2026-05-14T00:58:15.977Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-13T23:52:39.321Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-14T00:55:43.945907+00:00\"}]}, \"hypothesis\": \"5% dosage contaminated SFT on Qwen2.5-0.5B (seed=42): v3 retry with correct --gpu 5 (v1/v2 OOM due to --gpu 0 conflicting with d100 on GPU 0). Minimum contamination level for dose-response threshold.\", \"metrics\": {\"checkpoint_size_mb\": 166, \"entropy\": 1.5874, \"epoch\": 1, \"exit_code\": 0, \"final_loss\": 1.478, \"lora_adapter_size_mb\": 33.6, \"mean_train_loss\": 1.5424, \"num_tokens\": 19657865, \"token_accuracy\": 0.667, \"total_steps\": 3177, \"train_samples_per_second\": 15.09, \"train_steps_per_second\": 0.943, \"training_time_min\": 56.14, \"vs_baseline_0pct\": {\"baseline_final_loss\": 1.4894, \"baseline_mean_train_loss\": 1.5388, \"baseline_token_accuracy\": 0.682, \"baseline_training_time_min\": 52.9, \"delta_final_loss\": -0.0114, \"delta_mean_train_loss\": 0.0036, \"delta_token_accuracy\": -0.015, \"delta_training_time_min\": 3.24}}, \"notes\": \"dosage 数据已完整（含 MMLU+ARC+GSM8K，May 14 07:16 重新生成）。v3 已修复 --gpu 5（v1/v2 均为 --gpu 0 错误）。此 run 使用 ALL paraphrases（含 QC fail），属于 \\\"noisy contamination\\\" condition。\", \"parent\": \"exp_001_sft_d005_05B\", \"reproduce\": {\"finished_at\": \"2026-05-14T00:55:38.416Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"N/A (SFT retry, not eval)\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42 --seed 42 --gpu 5 --batch-size 4 --grad-accum 4 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"data_count\": 50826, \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl\", \"eval_data\": \"N/A (SFT retry, not eval)\", \"gpu\": [\"cuda:5\"], \"gpu_hours\": 1.0, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_d005_05B_v3.log\", \"model_name\": \"Qwen2.5-0.5B\", \"pid\": \"239729\", \"seed\": 42, \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-13T23:58:01.548Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 3614.4}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T00:58:15.977Z\"}, \"exp_001_sft_d100_05B\": {\"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42\", \"completed_at\": \"2026-05-14T00:53:49.656Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-13T23:36:13.403Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-14T00:50:19.949448+00:00\"}]}, \"gpu\": \"cuda:0\", \"hypothesis\": \"100% dosage contaminated SFT on Qwen2.5-0.5B (seed=42): maximum contamination level to establish upper bound of calibration error; paired with d005 for min-max comparison\", \"log_path\": \"/root/runs/contamcal-irt-calibration/exp_001_sft_d100_05B.log\", \"metrics\": {\"exit_code\": 0, \"final_loss\": 1.5943, \"mean_train_loss\": 1.5662, \"num_tokens\": 21575068, \"token_accuracy\": 0.666, \"total_steps\": 4160, \"train_samples_per_second\": 16.09, \"train_steps_per_second\": 1.006, \"training_time_min\": 68.9, \"vs_baseline_0pct\": {\"accuracy_delta\": \"-0.016 (-2.3%)\", \"loss_delta\": \"+0.0274 (+1.8%)\", \"time_delta\": \"+16min (+30%)\"}}, \"notes\": \"dosage 数据已完整（含 MMLU+ARC+GSM8K，May 14 07:16 重新生成）。data_meta: arc=1172, gsm8k=1319, mmlu=14042, total_contam=16533。此 run 使用 ALL paraphrases（含 QC fail），属于 \\\"noisy contamination\\\" condition。\", \"pid\": \"235243\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42 --seed 42 --gpu 0 --batch-size 4 --grad-accum 4 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"finished_at\": \"2026-05-14T00:50:16.569Z\", \"gpu\": \"cuda:0\", \"server\": \"cqa1-21977\", \"started_at\": \"2026-05-13T23:38:41.749Z\", \"training_hours\": 1.19}, \"retry_count\": 0, \"server\": \"cqa1-21977\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42 --seed 42 --gpu 0 --batch-size 4 --grad-accum 4 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 1.23, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_d100_05B.log\", \"pid\": \"235243\", \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-13T23:39:51.510Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 4438.1}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T00:55:14.218Z\"}, \"exp_001_sft_0pct\": {\"checkpoint_path\": \"N/A (parent entry)\", \"completed_at\": \"2026-05-14T00:36:52.832Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-13T19:26:42.106Z\", \"hypothesis\": \"0% dosage (clean) SFT baselines on Qwen2.5-0.5B/1.5B/3B establish ground-truth benchmark scores for calibration error computation; LoRA r=16 alpha=32 1-epoch training on pure instruction data should preserve base model capability\", \"log_path\": \"N/A (parent entry)\", \"notes\": \"Parent entry for 3 sub-experiments (05B/15B/3B). All confirmed running.\", \"retry_count\": 0, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T00:36:52.832Z\"}, \"exp_001_sft_0pct_3B_s123\": {\"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s123\", \"completed_at\": \"2026-05-14T00:23:18.290Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-13T20:39:01.606Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-14T00:16:17.727184+00:00\"}]}, \"hypothesis\": \"0% dosage clean baseline Qwen2.5-3B seed=123 (second seed for variance estimation)\", \"metrics\": {\"adapter_model_mb\": 114, \"adapter_size_mb\": 488, \"checkpoint_size_mb\": 488, \"epochs\": 1, \"final_loss\": 1.114, \"mean_token_accuracy\": 0.7505, \"mean_train_loss\": 1.1309, \"steps_completed\": 3125, \"total_steps\": 3125, \"total_tokens\": 19555717, \"train_samples_per_second\": 3.91, \"training_time_min\": 213.1}, \"notes\": \"OOM 修复后重提交 --gpu 3 (物理 GPU 3)。Worker 确认 PID 216249 训练中，ETA ~3.4h\", \"reproduce\": {\"finished_at\": \"2026-05-14T00:16:04.357Z\"}, \"retry_count\": 0, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s123 --seed 123 --gpu 3 --batch-size 1 --grad-accum 16 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"data_count\": \"50000\", \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl\", \"gpu\": [\"cuda:3\"], \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_0pct_3B_s123.log\", \"model_name\": \"Qwen2.5-3B\", \"pid\": \"216935\", \"seed\": 123, \"server\": \"cqa1-21977\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T00:23:18.290Z\"}, \"exp_001_eval_15B_d000_s42\": {\"completed_at\": \"2026-05-14T00:23:17.209Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-13T21:30:03.433Z\", \"failure_reason\": \"卡死 11+小时：GPU 利用率 0%，显存占 5820MiB，输出目录为空。根因：spec 使用相对路径 (--model-path Qwen2.5-1.5B --adapter-path lora_adapter) 而非绝对路径，导致模型加载异常挂起。已 kill -9。\", \"hypothesis\": \"0% dosage 1.5B s42 baseline evaluation on 4 benchmarks to establish ground-truth scores for calibration error computation\", \"parent\": \"exp_001_sft_0pct_15B\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"N/A\", \"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s42/lora_adapter/\", \"command\": \"python evaluate.py --model-path Qwen2.5-1.5B --adapter-path lora_adapter --benchmarks mmlu gsm8k arc_challenge humaneval\", \"data_count\": \"~26000 items total\", \"data_path\": \"MMLU/GSM8K/ARC-Challenge/HumanEval (HuggingFace datasets)\", \"eval_data\": \"MMLU, GSM8K, ARC-Challenge, HumanEval (original)\", \"gpu\": [\"cuda:4\"], \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_15B_d000_s42.log\", \"model_name\": \"Qwen2.5-1.5B + LoRA (d000_s42)\", \"output_dir\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s42\", \"pid\": \"221376\", \"seed\": 42, \"server\": \"cqa1-21977\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T00:23:17.209Z\"}, \"exp_001_sft_d005_05B_v2\": {\"completed_at\": \"2026-05-13T23:49:48.629Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-13T23:48:24.508Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-13T23:49:51.462263+00:00\"}]}, \"failure_reason\": \"CUDA OOM: CUDA out of memory. Tried to allocate 578.00 MiB. GPU 0 has a total capacity of 23.52 GiB of which 459.38 MiB is free. Process 235248 has 21.47 GiB memory in use. Including non-PyTorch memory, this process has 1.58 GiB memory in use. Of the allocated\", \"gpu\": \"cuda:5\", \"hypothesis\": \"5% dosage contaminated SFT on Qwen2.5-0.5B (seed=42): retry after v1 OOM crash (GPU 5 conflict with zombie eval process). GPU 5 now clear.\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_d005_05B_v2.log\", \"notes\": \"v2 OOM 根因非 GPU 5 残留进程，而是 --gpu 0 导致训练实际跑在 GPU 0（d100 占满 22GB），GPU 5 从未被使用。已在 r3 修复为 --gpu 5。\", \"pid\": \"237300\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42 --seed 42 --gpu 0 --batch-size 4 --grad-accum 4 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"finished_at\": \"2026-05-13T23:49:47.033Z\"}, \"retry_count\": 0, \"server\": \"cqa1-21977\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42 --seed 42 --gpu 0 --batch-size 4 --grad-accum 4 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"gpu\": [\"cuda:5\"], \"gpu_hours\": 0.01, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_d005_05B_v2.log\", \"pid\": \"237300\", \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-13T23:49:27.702Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 20.9}, \"status\": \"DONE\", \"updated_at\": \"2026-05-13T23:59:33.029Z\"}, \"exp_001_sft_d005_05B\": {\"completed_at\": \"2026-05-13T23:42:35.135Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-13T23:36:15.352Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-13T23:42:37.857937+00:00\"}]}, \"failure_reason\": \"CUDA OOM at step 8/3177 — zombie 3B eval process (PID 234755) 占 6.8GB GPU 5 显存，导致 SFT 训练分配失败。已重试为 exp_001_sft_d005_05B_v2。\", \"gpu\": \"cuda:5\", \"hypothesis\": \"5% dosage contaminated SFT on Qwen2.5-0.5B (seed=42): minimum contamination level to detect dose-response threshold; paired with d100 for min-max comparison\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_d005_05B.log\", \"notes\": \"v1 OOM at step 8/3177 — GPU 5 有残留进程 PID 234755 占 6.8GB。PID 236994 (submit_training_job 重提交) 也使用了 --gpu 0，实际跑到 GPU 0 而非 GPU 5，同样 OOM。根因：--gpu 0 导致 CUDA_VISIBLE_DEVICES 被脚本覆盖为 0。已在 r3 修复为 --gpu 5。\", \"pid\": \"235331\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42 --seed 42 --gpu 5 --batch-size 4 --grad-accum 4 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"finished_at\": \"2026-05-13T23:42:32.872Z\", \"gpu\": \"cuda:5\", \"server\": \"cqa1-21977\", \"started_at\": \"2026-05-13T23:38:42.505Z\", \"training_hours\": 0.06}, \"retry_count\": 0, \"server\": \"cqa1-21977\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_005.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42 --seed 42 --gpu 0 --batch-size 4 --grad-accum 4 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"gpu\": [\"cuda:5\"], \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_d005_05B.log\", \"pid\": \"236994\", \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-13T23:49:14.077Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-13T23:59:30.512Z\"}, \"exp_001_sft_100pct_05B\": {\"completed_at\": \"2026-05-13T23:49:10.741Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-13T23:41:15.631Z\", \"failure_reason\": \"Duplicate registry entry — actual training tracked by exp_001_sft_d100_05B (PID 235243, cron monitored)\", \"hypothesis\": \"100% contamination dosage on 0.5B establishes upper bound of score inflation; comparing with 0% baseline reveals maximum contamination effect across MMLU/GSM8K/ARC benchmarks\", \"parent\": \"\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42\", \"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && cd /root/contamcal-irt-calibration/exp001 && python train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42 --seed 42 --gpu 0 --batch-size 4 --grad-accum 4 --cache-dir /root/autodl-tmp/.hf_cache\", \"data_count\": 66533, \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_100.jsonl\", \"model_name\": \"Qwen2.5-0.5B\", \"seed\": 42, \"server\": \"cqa1-21977\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-13T23:49:12.007Z\"}, \"exp_001_sft_0pct_3B\": {\"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42\", \"completed_at\": \"2026-05-13T23:25:49.016Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-13T19:44:40.471Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-13T23:23:43.393661+00:00\"}]}, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_0pct_3B.log\", \"metrics\": {\"adapter_size_mb\": 115, \"checkpoint_size_mb\": 488, \"exit_code\": 0, \"final_loss\": 1.0736, \"mean_train_loss\": 1.1306, \"steps\": \"3125/3125\", \"token_accuracy\": 0.734, \"training_time_min\": 214.7}, \"reproduce\": {\"finished_at\": \"2026-05-13T23:23:41.844Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42 --seed 42 --gpu 5 --batch-size 1 --grad-accum 16 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"gpu\": [\"cuda:5\"], \"gpu_hours\": 3.69, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_0pct_3B.log\", \"pid\": \"210666\", \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-13T19:44:40.431Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 13268.6}, \"status\": \"DONE\", \"updated_at\": \"2026-05-13T23:25:49.016Z\"}, \"exp_001_sft_injection\": {\"completed_at\": \"2026-05-13T23:14:30.258Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-13T17:28:01.546Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-13T19:18:08.635006+00:00\"}, {\"action\": \"manual_fix\", \"event\": \"status_rollback\", \"reason\": \"Cron misidentified old PID as dead → auto-failed. 3 paraphrase processes (GPU 0-2) still running. Rolled back DONE/failed → RUNNING per Director instruction.\", \"ts\": \"2026-05-13T19:32:00.000Z\"}, {\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-13T23:14:43.962197+00:00\"}]}, \"failure_reason\": \"\", \"hypothesis\": \"Controlled SFT contamination injection produces dose-dependent score inflation on contaminated benchmarks; 4PL+γ IRT can recover true (uncontaminated) performance from calibrated scores with proper uncertainty bounds\", \"metrics\": {\"arc_qc_pass\": 697, \"arc_qc_rate\": 0.595, \"arc_total\": 1172, \"gsm8k_qc_pass\": 228, \"gsm8k_qc_rate\": 0.173, \"gsm8k_total\": 1319, \"humaneval_total\": 164, \"mmlu_qc_pass\": 6596, \"mmlu_qc_rate\": 0.47, \"mmlu_total\": 14042}, \"notes\": \"MMLU paraphrase 3-attempt QC 重试流程: Attempt 1 ✅ (878 batches, 4112/14042 QC pass 29.3%, ~90min). Attempt 2 进行中 (v2重启, 439 batches total, 进度~22%). Attempt 3 待定. 输出在全部 attempt 结束后一次性写出 mmlu_paraphrases.json. GSM8K ✅ 1319条(QC 17.3%), ARC ✅ 1172条(QC 59.5%).\", \"reproduce\": {\"finished_at\": \"2026-05-13T23:14:29.355Z\"}, \"retry_count\": 0, \"spec\": {\"command\": \"Phase 1 paraphrase: GPU 0 MMLU (PID 204467 v3, vLLM bs=16). GSM8K + ARC completed.\", \"data_count\": \"45 SFT runs + 90 eval runs (original+paraphrased)\", \"data_path\": \"MMLU+GSM8K+ARC-Challenge+HumanEval paraphrases → SFT data mixing\", \"gpu\": \"cuda:0 (MMLU vLLM, still running). cuda:1/2 freed (GSM8K+ARC done).\", \"model_name\": \"Qwen2.5-0.5B/1.5B/3B (LoRA SFT), Qwen2.5-7B-Instruct (paraphrase)\", \"note\": \"GSM8K: 1319 paraphrases (228 QC pass, 17.3%). ARC: 1172 paraphrases (697 QC pass, 59.5%). MMLU: Attempt 1 done (878 batches, 29.3% QC), Attempt 2 in progress (439 batches total, ~22%), Attempt 3 pending. HumanEval: done (appendix per D009).\", \"pid\": \"204467\", \"seed\": \"42,123,456\", \"server\": \"cqa1-21977\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-13T23:21:54.827Z\"}, \"exp_001_sft_0pct_15B_s123\": {\"completed_at\": \"2026-05-13T22:30:26.882Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-13T20:35:07.346Z\", \"hypothesis\": \"0% dosage clean baseline Qwen2.5-1.5B seed=123 (second seed for variance estimation)\", \"metrics\": {\"token_acc\": 0.731, \"train_loss\": 1.2602, \"train_time_min\": 101.5}, \"notes\": \"OOM 修复后重提交 --gpu 2 (物理 GPU 2)。Worker 确认 PID 216106 训练中 (1/3125 steps, ~2.58s/it)\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s123\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s123 --seed 123 --gpu 2 --batch-size 2 --grad-accum 8 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"data_count\": \"50000\", \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl\", \"gpu\": [\"cuda:2\"], \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_0pct_15B_s123.log\", \"model_name\": \"Qwen2.5-1.5B\", \"pid\": \"216111\", \"seed\": 123, \"server\": \"cqa1-21977\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-13T22:30:26.882Z\"}, \"exp_001_sft_0pct_05B_s123\": {\"completed_at\": \"2026-05-13T22:30:25.819Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-13T20:35:04.879Z\", \"hypothesis\": \"0% dosage clean baseline Qwen2.5-0.5B seed=123 (second seed for variance estimation)\", \"metrics\": {\"token_acc\": 0.676, \"train_loss\": 1.5393, \"train_time_min\": 54.5}, \"notes\": \"OOM 修复后重提交 --gpu 1 (物理 GPU 1)。Worker 确认 PID 216028 训练中 (2/3125 steps, ~1.87s/it)\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s123\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s123 --seed 123 --gpu 1 --batch-size 4 --grad-accum 4 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"data_count\": \"50000\", \"data_path\": \"/root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl\", \"gpu\": [\"cuda:1\"], \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_0pct_05B_s123.log\", \"model_name\": \"Qwen2.5-0.5B\", \"pid\": \"216033\", \"seed\": 123, \"server\": \"cqa1-21977\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-13T22:30:25.819Z\"}, \"exp_001_sft_0pct_15B\": {\"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s42\", \"completed_at\": \"2026-05-13T21:27:59.348Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-13T19:39:48.369Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-13T21:25:42.551081+00:00\"}]}, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_0pct_15B.log\", \"metrics\": {\"adapter_size_mb\": 71, \"checkpoint_size_mb\": 313, \"exit_code\": 0, \"final_loss\": 1.2039, \"mean_train_loss\": 1.2599, \"steps\": \"3125/3125\", \"token_accuracy\": 0.711, \"training_time_min\": 101.5}, \"reproduce\": {\"finished_at\": \"2026-05-13T21:25:40.979Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s42 --seed 42 --gpu 4 --batch-size 2 --grad-accum 8 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"gpu\": [\"cuda:4\"], \"gpu_hours\": 1.78, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_0pct_15B.log\", \"pid\": \"210116\", \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-13T19:41:11.760Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 6407.6}, \"status\": \"DONE\", \"updated_at\": \"2026-05-13T21:27:59.348Z\"}, \"exp_001_sft_0pct_05B\": {\"checkpoint_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42\", \"completed_at\": \"2026-05-13T20:36:06.744Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-13T19:35:01.170Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-13T20:33:54.496690+00:00\"}]}, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_0pct_05B.log\", \"metrics\": {\"adapter_size_mb\": 34, \"checkpoint_size_mb\": 166, \"exit_code\": 0, \"final_loss\": 1.4894, \"mean_train_loss\": 1.5388, \"steps\": \"3125/3125\", \"token_accuracy\": 0.682, \"training_time_min\": 52.9}, \"reproduce\": {\"finished_at\": \"2026-05-13T20:33:53.420Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export TOKENIZERS_PARALLELISM=false && python /root/contamcal-irt-calibration/exp001/train_sft.py --model-name /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B --data-path /root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl --output-dir /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42 --seed 42 --gpu 3 --batch-size 4 --grad-accum 4 --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"gpu\": [\"cuda:3\"], \"gpu_hours\": 0.98, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_sft_0pct_05B.log\", \"pid\": \"208933\", \"server\": \"cqa1-21977\", \"submitted_at\": \"2026-05-13T19:37:23.024Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 3523.7}, \"status\": \"DONE\", \"updated_at\": \"2026-05-13T20:37:01.562Z\"}, \"mvp_sim_confounding\": {\"completed_at\": \"2026-05-13T16:28:42.378Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-13T04:39:19.345Z\", \"hypothesis\": \"4PL+γ IRT model can still separate γ from θ when exposure is confounded with ability (corr≈0.4); if not, need model-level random effect for exposure\", \"metrics\": {\"actual_confound_corr\": 0.3814, \"divergent_pct\": 0, \"fit_time_sec\": 832, \"gamma_ci_covers_true\": true, \"gamma_ci_excludes_zero\": true, \"gamma_mean\": 0.5386, \"gamma_rel_bias\": 0.0771, \"max_rhat\": 1.007, \"min_ess\": 1371.9, \"overall\": \"PASS\", \"theta_corr\": 0.9733, \"theta_residual_exp_corr\": 0.0582, \"theta_rmse\": 0.2407}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"artifacts/mvp_simulation/p2_confounding_results.json\", \"command\": \"python run_p2_confounding.py\", \"data_count\": \"50 models x 300 items = 15000 responses\", \"data_path\": \"synthetic confounded (corr≈0.38)\", \"log_path\": \"/tmp/p2_confounding.log\", \"model_name\": \"4PL+γ IRT (Stan NUTS)\", \"note\": \"N_items=300 (matching Variant A PASS config), 4PL NUTS only, 4 chains 1000+1000, θ-exposure corr=0.381\", \"pid\": 202872, \"seed\": 123, \"server\": \"local-cpu\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-13T16:28:42.378Z\"}, \"mvp_sim_4pl_gamma\": {\"completed_at\": \"2026-05-13T10:59:01.402Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-13T04:27:47.251Z\", \"hypothesis\": \"4PL+γ IRT model can separate contamination effect (γ) from true ability (θ) on synthetic data; γ posterior recovers true value within ±0.15, θ correlation >0.9\", \"metrics\": {\"variant_a_nitems300\": {\"divergent_pct\": 0, \"fit_time_sec\": 1407.5, \"gamma_ci_covers_true\": true, \"gamma_ci_excludes_zero\": true, \"gamma_mean\": 0.466, \"gamma_rel_bias\": 0.068, \"max_rhat\": 1.003, \"overall\": \"PASS\", \"theta_corr\": 0.943, \"theta_rmse\": 0.238}}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"artifacts/mvp_simulation/p1_variant_results.json\", \"command\": \"python run_p1_base.py\", \"data_count\": \"50 models x 100 items = 5000 responses\", \"data_path\": \"synthetic (generated in-script)\", \"log_path\": \"/tmp/p1_variants.log\", \"model_name\": \"2PL+γ / 4PL+γ IRT (Stan)\", \"note\": \"Order: 2PL ADVI → 2PL NUTS → 4PL ADVI → 4PL NUTS\", \"pid\": 197929, \"seed\": 42, \"server\": \"local-cpu\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-13T10:59:01.402Z\"}}, \"count\": 323, \"total\": 323, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7614}}"
    }
  },
  "sourceToolAssistantUUID": "68884037-980b-4979-9fca-2e700c75685e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool result

_source line 19 · 2026-05-19T13:30:32.937Z_

<details><summary>↩ Tool result · `toolu_01QtjstF6tFARtyLfkSGLmeY`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"project\": \"contamcal-irt-calibration\", \"section\": \"execution\", \"config\": {\"execution\": {\"gpu_ids\": [0, 1, 2, 3], \"project_path\": \"/root/contamcal-irt-calibration\", \"servers\": [{\"gpu_ids\": [0], \"server\": \"cqa1-21977\"}, {\"account\": \"root\", \"gpu_ids\": [0, 1, 2, 3], \"server\": \"westd-29999\"}]}}}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f573945d-9b6b-4c87-9959-7320a8e95923",
  "isSidechain": false,
  "promptId": "f236d3d3-c563-42c4-b0bf-0a1f74939452",
  "type": "user",
  "uuid": "9c63c155-463e-4278-ad4a-4d96f5e3a447",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"project\\\": \\\"contamcal-irt-calibration\\\", \\\"section\\\": \\\"execution\\\", \\\"config\\\": {\\\"execution\\\": {\\\"gpu_ids\\\": [0, 1, 2, 3], \\\"project_path\\\": \\\"/root/contamcal-irt-calibration\\\", \\\"servers\\\": [{\\\"gpu_ids\\\": [0], \\\"server\\\": \\\"cqa1-21977\\\"}, {\\\"account\\\": \\\"root\\\", \\\"gpu_ids\\\": [0, 1, 2, 3], \\\"server\\\": \\\"westd-29999\\\"}]}}}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"project\": \"contamcal-irt-calibration\", \"section\": \"execution\", \"config\": {\"execution\": {\"gpu_ids\": [0, 1, 2, 3], \"project_path\": \"/root/contamcal-irt-calibration\", \"servers\": [{\"gpu_ids\": [0], \"server\": \"cqa1-21977\"}, {\"account\": \"root\", \"gpu_ids\": [0, 1, 2, 3], \"server\": \"westd-29999\"}]}}}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "f8bce7a6-dd99-486d-b617-a18062f9ef3a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool result

_source line 20 · 2026-05-19T13:30:32.310Z_

<details><summary>↩ Tool result · `toolu_01JLs37RgBVCxyFKzJD4tKHL`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"reconciled\": 0, \"results\": []}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "54716369-8a6f-4517-a91c-56339cd3c5a9",
  "isSidechain": false,
  "promptId": "f236d3d3-c563-42c4-b0bf-0a1f74939452",
  "type": "user",
  "uuid": "d80d7e8f-9a37-4022-a191-e0d7bfc0d396",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"reconciled\\\": 0, \\\"results\\\": []}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"reconciled\": 0, \"results\": []}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "54716369-8a6f-4517-a91c-56339cd3c5a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool result

_source line 21 · 2026-05-19T13:30:32.318Z_

<details><summary>↩ Tool result · `toolu_01JfuF2YtHGh57iXRkUrvkqi`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/report.md\", \"content\": \"&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-19T11:36:00Z; do not edit — regenerated by auto_build_report_facts) -->\\n## 📊 当前状态（auto-derived from registry）\\n\\n**总计**: 320 个实验 — DONE 290, PREPARING 29, QUEUED 1\\n**DONE 分布**: failed 58, killed 14, negative 7, success 211\\n\\n### GPU 占用\\n- **分配**: 8 张 — cqa1-21977:cuda:0, cqa1-21977:cuda:1, cqa1-21977:cuda:2, cqa1-21977:cuda:3, westd-29999:cuda:0, westd-29999:cuda:1, westd-29999:cuda:2, westd-29999:cuda:3\\n- **空闲（分配了没跑）**: cqa1-21977:cuda:0, cqa1-21977:cuda:1, cqa1-21977:cuda:2, cqa1-21977:cuda:3, westd-29999:cuda:0, westd-29999:cuda:1, westd-29999:cuda:2, westd-29999:cuda:3\\n\\n### 💾 磁盘余量\\n- **cqa1-21977**:\\n  - `/autodl-pub`: 280G/7.0T 可用（已用 97%） ⚠️\\n  - `/autodl-pub/data`: 1.5T/4.0T 可用（已用 65%）\\n  - `/usr/bin/nvidia-smi`: 818G/879G 可用（已用 2%）\\n- **westd-29999**:\\n  - `/autodl-pub`: 5.3T/7.3T 可用（已用 24%）\\n  - `/init`: 150M/150M 可用（已用 0%）\\n  - `/usr/bin/nvidia-smi`: 427G/879G 可用（已用 49%）\\n\\n### 🏃 RUNNING\\n_（无）_\\n\\n### 📌 最近完成 (top 5)\\n- `exp_001_sft_phi4_d100_s42` [success] — 2026-05-19T10:42:39\\n- `exp_001_sft_olmo2_7b_d100_s42` [success] — 2026-05-19T10:25:26\\n- `exp_001_sft_gemma2_9b_d100_s42` [success] — 2026-05-19T10:25:21\\n- `exp_001_sft_olmo2_7b_d050_s42` [success] — 2026-05-19T08:01:54\\n- `eval_phi4_mmlu_arc_westd` [failed] — 2026-05-19T07:21:53 — process dead 5× with no sentinel/W&B — auto-resolved as failed\\n\\n### 🔴 最近失败原因 (top 3)\\n- `eval_phi4_mmlu_arc_westd`: process dead 5× with no sentinel/W&B — auto-resolved as failed\\n\\n&lt;!-- AUTO-FACTS-END -->\\n\\n---\\n\\n# Handover — 2026-05-19\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n- eval_cross_family_cqa1: Cross-family dose-response eval on cqa1: MMLU 5-shot + ARC 25-shot for OLMo-2-7B (d000/d005/d025) and Gemma-2-9B (d000/d005/d025/d050) to establish IRT calibration curves across model architectures.（排队等待 GPU）\\n- eval_phi4_mmlu_arc_westd_v2: Phi-4 dose-response eval v2: MMLU 5-shot + ARC 25-shot across d000/d005/d025/d050. Replaces v1 which was falsely marked DONE by cron PID mismatch.（准备中）\\n- j16-domain-gamma-rerun（准备中）\\n- exp_006_irt_05B_v2: Tiered IRT calibration (D023): GSM8K/ARC direct NUTS + MMLU subsampled 1000 items + ADVI robustness check. Fixes v1 issues: aligned-only, signal-derived exposure, --max-items.（准备中）\\n- signals_05B_s123_batch（准备中）\\n- exp_002_signals_15B_instruct_gsm8k_v2: 1.5B-Instruct GSM8K signals (s1/s2/s4) to expand N for cross-family pooled IRT — GSM8K is strongest data point per cross-family results, critical for C1 N expansion（准备中）\\n- exp_001_sft_15B_d025_s123（准备中）\\n- exp_001_sft_3B_d000_v4（准备中）\\n- exp_001_sft_3B_d000_s42（准备中）\\n- exp006-gsm8k-d024-delta: GSM8K d024 delta analysis, superseded by later IRT runs with pooled cross-family design（准备中）\\n- …另有 16 项\\n\\n## 近期结论\\n- **exp_001_sft_phi4_d100_s42** (success): Phi-4 (14.7B) d100 (100% contamination) SFT with lr=5e-5 LoRA r=16 α=32 establishes the full-dosage data point for IRT dose-response calibration in the Microsoft model family, completing the 5-dosage sweep.\\n- **exp_001_sft_olmo2_7b_d100_s42** (success): OLMo-2-7B d100 (100% contamination) SFT with lr=5e-5 LoRA r=16 α=32 establishes the full-dosage data point for IRT dose-response calibration in the AllenAI model family, completing the 5-dosage sweep.\\n- **exp_001_sft_gemma2_9b_d100_s42** (success): Gemma-2-9B d100 (100% contamination) SFT with lr=5e-5 LoRA r=16 α=32 establishes the full-dosage data point for IRT dose-response calibration in the Google model family, completing the 5-dosage sweep.\\n\\n## 趋势\\n成功 213 / 负向 7 / 失败 59 / 共 293\\nmean_token_accuracy: 0.7244 ↑（近 3 次 success）\\ntrain_loss: 1.191 ↓（近 3 次 success）\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\ncqa1-21977: 无 GPU 信息\\nwestd-29999: 无 GPU 信息\\n\\n## 告警\\n- exp_001_eval_05B_d000_s42: 训练失败 — unknown\\n- exp_001_eval_05B_d100: 训练失败 — unknown\\n- exp_001_eval_05B_d100_v2: 训练失败 — unknown\\n- exp_001_eval_15B_d000_s42: 训练失败 — unknown\\n- exp_001_sft_100pct_05B: 训练失败 — unknown\\n- exp_001_sft_d005_05B: 已被终止 — unknown\\n- exp_001_sft_d005_05B_v2: 训练失败 — unknown\\n- exp_001_sft_d100_15B: 训练失败 — unknown\\n- exp_004_sim_sweep: 训练失败 — unknown\\n- exp_005_noise_prop: 训练失败 — unknown\\n- exp_005_noise_prop_v2: 训练失败 — unknown\\n- exp_005_noise_prop_v3: 训练失败 — unknown\\n- exp_001_sft_d025_05B: 训练失败 — unknown\\n- exp_001_sft_d025_05B_v2: 训练失败 — unknown\\n- exp_004_sim_sweep_v2: 训练失败 — unknown\\n- exp_001_eval_05B_aligned_batch: 训练失败 — unknown\\n- exp_006_irt_05B: 已被终止 — unknown\\n- exp_001_eval_05B_d100_aligned: 训练失败 — unknown\\n- exp_001_eval_05B_d100_aligned_v3: 训练失败 — unknown\\n- exp_008_instruct_rl_proxy: 训练失败 — unknown\\n- exp_006_irt_05B_v1: 训练失败 — unknown\\n- exp_006_pooled_gsm8k_v1: 训练失败 — unknown\\n- exp_004_sim_sweep_v3: 训练失败 — unknown\\n- exp006-pooled-05B-15B-mmlu-v2: 训练失败 — unknown\\n- exp_001_eval_3B_d100_v2_aligned: 训练失败 — unknown\\n- exp_001_sft_d025_3B: 训练失败 — unknown\\n- exp006-pooled-s1only-gsm8k: 训练失败 — unknown\\n- exp006-oracle-gsm8k-extended: 训练失败 — unknown\\n- exp_004_sim_sweep_v4: 训练失败 — unknown\\n- exp_001_eval_3B_d000_v2_para_aligned_v3: 训练失败 — unknown\\n- exp_001_sft_05B_d025_s123: 已被终止 — unknown\\n- exp_001_eval_05B_d000_s42_v7: 训练失败 — unknown\\n- exp_004_sim_sweep_v5: 训练失败 — unknown\\n- exp006-oracle-arc-4pl-pooled: 训练失败 — unknown\\n- exp_001_sft_15B_d005_s123: 训练失败 — unknown\\n- exp_008_base_pretrained_eval: 训练失败 — unknown\\n- exp_002_signals_3B: 训练失败 — unknown\\n- exp_002_signals_3B_v2: 已被终止 — unknown\\n- exp_001_sft_3B_d000_v3: 训练失败 — unknown\\n- exp_001_sft_3B_d100_s42_a32: 已被终止 — unknown\\n- exp_001_sft_3B_d025_s42_a32: 已被终止 — unknown\\n- exp_001_sft_3B_d100_s42_a32_v2: 训练失败 — unknown\\n- exp_004_sim_sweep_v6: 已被终止 — unknown\\n- exp_001_eval_3B_d100_s123_para_aligned: 训练失败 — unknown\\n- exp_002_signals_3B_v3: 已被终止 — unknown\\n- exp_002_signals_3B_v4: 训练失败 — unknown\\n- exp_002_signals_3B_v5: 训练失败 — unknown\\n- exp_002_signals_3B_v6: 训练失败 — unknown\\n- exp_001_sft_3B_d025_s42_a32_v2: 训练失败 — unknown\\n- exp_001_eval_3B_d025_v3_s42_batch: 已被终止 — unknown\\n- exp_001_sft_3B_d025_s42_a32_v3: 已被终止 — unknown\\n- exp_002_signals_3B_v8: 训练失败 — unknown\\n- exp_002_signals_3B_v8_recovery: 训练失败 — unknown\\n- exp_002_signals_3B_v9: 训练失败 — unknown\\n- exp_002_signals_05B_s123_batch: 训练失败 — unknown\\n- exp_001_eval_3B_instruct_aligned_para: 训练失败 — unknown\\n- exp_006_mmlu_domain_gamma_n24_v2: 训练失败 — unknown\\n- exp_006_mmlu_domain_gamma_n24_v3: 训练失败 — unknown\\n- exp_001_eval_llama32_3B_d000_s42: 已被终止 — unknown\\n- exp_002_signals_3B_d000_s123_cuda2: 训练失败 — unknown\\n- exp_002_signals_15B_instruct_gsm8k: 训练失败 — unknown\\n- exp_002_signals_llama32_3B_d000_gsm8k: 训练失败 — unknown\\n- exp_004_fisher_heatmap_w4: 训练失败 — unknown\\n- exp_002_signals_llama32_3B_d025_mmlu_arc_gsm8k: 训练失败 — unknown\\n- exp_002_signals_llama32_3B_d100_mmlu: 已被终止 — unknown\\n- exp_006_theta_extraction_j13: 训练失败 — unknown\\n- exp_006_cross_family_irt_j16: 训练失败 — unknown\\n- exp_006_j16_theta_extraction: 训练失败 — unknown\\n- eval_7b_batch_cqa1: 已被终止 — unknown\\n- eval_7b_batch1_westd: 训练失败 — unknown\\n- eval_14b_mmlu_arc_westd: 训练失败 — unknown\\n- exp_001_sft_olmo2_7b_d005_s42: 已被终止 — unknown\\n- eval_phi4_mmlu_arc_westd: 训练失败 — unknown\\n\", \"total_chars\": 6929, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6e5b7b9a-6800-4da0-8aae-16bbb7ea49b0",
  "isSidechain": false,
  "promptId": "f236d3d3-c563-42c4-b0bf-0a1f74939452",
  "type": "user",
  "uuid": "d22b5900-9d83-4126-8fab-69f3a3359b17",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/report.md\\\", \\\"content\\\": \\\"&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-19T11:36:00Z; do not edit — regenerated by auto_build_report_facts) -->\\\\n## 📊 当前状态（auto-derived from registry）\\\\n\\\\n**总计**: 320 个实验 — DONE 290, PREPARING 29, QUEUED 1\\\\n**DONE 分布**: failed 58, killed 14, negative 7, success 211\\\\n\\\\n### GPU 占用\\\\n- **分配**: 8 张 — cqa1-21977:cuda:0, cqa1-21977:cuda:1, cqa1-21977:cuda:2, cqa1-21977:cuda:3, westd-29999:cuda:0, westd-29999:cuda:1, westd-29999:cuda:2, westd-29999:cuda:3\\\\n- **空闲（分配了没跑）**: cqa1-21977:cuda:0, cqa1-21977:cuda:1, cqa1-21977:cuda:2, cqa1-21977:cuda:3, westd-29999:cuda:0, westd-29999:cuda:1, westd-29999:cuda:2, westd-29999:cuda:3\\\\n\\\\n### 💾 磁盘余量\\\\n- **cqa1-21977**:\\\\n  - `/autodl-pub`: 280G/7.0T 可用（已用 97%） ⚠️\\\\n  - `/autodl-pub/data`: 1.5T/4.0T 可用（已用 65%）\\\\n  - `/usr/bin/nvidia-smi`: 818G/879G 可用（已用 2%）\\\\n- **westd-29999**:\\\\n  - `/autodl-pub`: 5.3T/7.3T 可用（已用 24%）\\\\n  - `/init`: 150M/150M 可用（已用 0%）\\\\n  - `/usr/bin/nvidia-smi`: 427G/879G 可用（已用 49%）\\\\n\\\\n### 🏃 RUNNING\\\\n_（无）_\\\\n\\\\n### 📌 最近完成 (top 5)\\\\n- `exp_001_sft_phi4_d100_s42` [success] — 2026-05-19T10:42:39\\\\n- `exp_001_sft_olmo2_7b_d100_s42` [success] — 2026-05-19T10:25:26\\\\n- `exp_001_sft_gemma2_9b_d100_s42` [success] — 2026-05-19T10:25:21\\\\n- `exp_001_sft_olmo2_7b_d050_s42` [success] — 2026-05-19T08:01:54\\\\n- `eval_phi4_mmlu_arc_westd` [failed] — 2026-05-19T07:21:53 — process dead 5× with no sentinel/W&B — auto-resolved as failed\\\\n\\\\n### 🔴 最近失败原因 (top 3)\\\\n- `eval_phi4_mmlu_arc_westd`: process dead 5× with no sentinel/W&B — auto-resolved as failed\\\\n\\\\n&lt;!-- AUTO-FACTS-END -->\\\\n\\\\n---\\\\n\\\\n# Handover — 2026-05-19\\\\n\\\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\\\n\\\\n## 运行中\\\\n（无）\\\\n\\\\n## 待处理\\\\n- eval_cross_family_cqa1: Cross-family dose-response eval on cqa1: MMLU 5-shot + ARC 25-shot for OLMo-2-7B (d000/d005/d025) and Gemma-2-9B (d000/d005/d025/d050) to establish IRT calibration curves across model architectures.（排队等待 GPU）\\\\n- eval_phi4_mmlu_arc_westd_v2: Phi-4 dose-response eval v2: MMLU 5-shot + ARC 25-shot across d000/d005/d025/d050. Replaces v1 which was falsely marked DONE by cron PID mismatch.（准备中）\\\\n- j16-domain-gamma-rerun（准备中）\\\\n- exp_006_irt_05B_v2: Tiered IRT calibration (D023): GSM8K/ARC direct NUTS + MMLU subsampled 1000 items + ADVI robustness check. Fixes v1 issues: aligned-only, signal-derived exposure, --max-items.（准备中）\\\\n- signals_05B_s123_batch（准备中）\\\\n- exp_002_signals_15B_instruct_gsm8k_v2: 1.5B-Instruct GSM8K signals (s1/s2/s4) to expand N for cross-family pooled IRT — GSM8K is strongest data point per cross-family results, critical for C1 N expansion（准备中）\\\\n- exp_001_sft_15B_d025_s123（准备中）\\\\n- exp_001_sft_3B_d000_v4（准备中）\\\\n- exp_001_sft_3B_d000_s42（准备中）\\\\n- exp006-gsm8k-d024-delta: GSM8K d024 delta analysis, superseded by later IRT runs with pooled cross-family design（准备中）\\\\n- …另有 16 项\\\\n\\\\n## 近期结论\\\\n- **exp_001_sft_phi4_d100_s42** (success): Phi-4 (14.7B) d100 (100% contamination) SFT with lr=5e-5 LoRA r=16 α=32 establishes the full-dosage data point for IRT dose-response calibration in the Microsoft model family, completing the 5-dosage sweep.\\\\n- **exp_001_sft_olmo2_7b_d100_s42** (success): OLMo-2-7B d100 (100% contamination) SFT with lr=5e-5 LoRA r=16 α=32 establishes the full-dosage data point for IRT dose-response calibration in the AllenAI model family, completing the 5-dosage sweep.\\\\n- **exp_001_sft_gemma2_9b_d100_s42** (success): Gemma-2-9B d100 (100% contamination) SFT with lr=5e-5 LoRA r=16 α=32 establishes the full-dosage data point for IRT dose-response calibration in the Google model family, completing the 5-dosage sweep.\\\\n\\\\n## 趋势\\\\n成功 213 / 负向 7 / 失败 59 / 共 293\\\\nmean_token_accuracy: 0.7244 ↑（近 3 次 success）\\\\ntrain_loss: 1.191 ↓（近 3 次 success）\\\\n\\\\n## 下一步\\\\n（无活跃 idea，请通过 ideas.md 添加）\\\\n\\\\n## 资源状态\\\\ncqa1-21977: 无 GPU 信息\\\\nwestd-29999: 无 GPU 信息\\\\n\\\\n## 告警\\\\n- exp_001_eval_05B_d000_s42: 训练失败 — unknown\\\\n- exp_001_eval_05B_d100: 训练失败 — unknown\\\\n- exp_001_eval_05B_d100_v2: 训练失败 — unknown\\\\n- exp_001_eval_15B_d000_s42: 训练失败 — unknown\\\\n- exp_001_sft_100pct_05B: 训练失败 — unknown\\\\n- exp_001_sft_d005_05B: 已被终止 — unknown\\\\n- exp_001_sft_d005_05B_v2: 训练失败 — unknown\\\\n- exp_001_sft_d100_15B: 训练失败 — unknown\\\\n- exp_004_sim_sweep: 训练失败 — unknown\\\\n- exp_005_noise_prop: 训练失败 — unknown\\\\n- exp_005_noise_prop_v2: 训练失败 — unknown\\\\n- exp_005_noise_prop_v3: 训练失败 — unknown\\\\n- exp_001_sft_d025_05B: 训练失败 — unknown\\\\n- exp_001_sft_d025_05B_v2: 训练失败 — unknown\\\\n- exp_004_sim_sweep_v2: 训练失败 — unknown\\\\n- exp_001_eval_05B_aligned_batch: 训练失败 — unknown\\\\n- exp_006_irt_05B: 已被终止 — unknown\\\\n- exp_001_eval_05B_d100_aligned: 训练失败 — unknown\\\\n- exp_001_eval_05B_d100_aligned_v3: 训练失败 — unknown\\\\n- exp_008_instruct_rl_proxy: 训练失败 — unknown\\\\n- exp_006_irt_05B_v1: 训练失败 — unknown\\\\n- exp_006_pooled_gsm8k_v1: 训练失败 — unknown\\\\n- exp_004_sim_sweep_v3: 训练失败 — unknown\\\\n- exp006-pooled-05B-15B-mmlu-v2: 训练失败 — unknown\\\\n- exp_001_eval_3B_d100_v2_aligned: 训练失败 — unknown\\\\n- exp_001_sft_d025_3B: 训练失败 — unknown\\\\n- exp006-pooled-s1only-gsm8k: 训练失败 — unknown\\\\n- exp006-oracle-gsm8k-extended: 训练失败 — unknown\\\\n- exp_004_sim_sweep_v4: 训练失败 — unknown\\\\n- exp_001_eval_3B_d000_v2_para_aligned_v3: 训练失败 — unknown\\\\n- exp_001_sft_05B_d025_s123: 已被终止 — unknown\\\\n- exp_001_eval_05B_d000_s42_v7: 训练失败 — unknown\\\\n- exp_004_sim_sweep_v5: 训练失败 — unknown\\\\n- exp006-oracle-arc-4pl-pooled: 训练失败 — unknown\\\\n- exp_001_sft_15B_d005_s123: 训练失败 — unknown\\\\n- exp_008_base_pretrained_eval: 训练失败 — unknown\\\\n- exp_002_signals_3B: 训练失败 — unknown\\\\n- exp_002_signals_3B_v2: 已被终止 — unknown\\\\n- exp_001_sft_3B_d000_v3: 训练失败 — unknown\\\\n- exp_001_sft_3B_d100_s42_a32: 已被终止 — unknown\\\\n- exp_001_sft_3B_d025_s42_a32: 已被终止 — unknown\\\\n- exp_001_sft_3B_d100_s42_a32_v2: 训练失败 — unknown\\\\n- exp_004_sim_sweep_v6: 已被终止 — unknown\\\\n- exp_001_eval_3B_d100_s123_para_aligned: 训练失败 — unknown\\\\n- exp_002_signals_3B_v3: 已被终止 — unknown\\\\n- exp_002_signals_3B_v4: 训练失败 — unknown\\\\n- exp_002_signals_3B_v5: 训练失败 — unknown\\\\n- exp_002_signals_3B_v6: 训练失败 — unknown\\\\n- exp_001_sft_3B_d025_s42_a32_v2: 训练失败 — unknown\\\\n- exp_001_eval_3B_d025_v3_s42_batch: 已被终止 — unknown\\\\n- exp_001_sft_3B_d025_s42_a32_v3: 已被终止 — unknown\\\\n- exp_002_signals_3B_v8: 训练失败 — unknown\\\\n- exp_002_signals_3B_v8_recovery: 训练失败 — unknown\\\\n- exp_002_signals_3B_v9: 训练失败 — unknown\\\\n- exp_002_signals_05B_s123_batch: 训练失败 — unknown\\\\n- exp_001_eval_3B_instruct_aligned_para: 训练失败 — unknown\\\\n- exp_006_mmlu_domain_gamma_n24_v2: 训练失败 — unknown\\\\n- exp_006_mmlu_domain_gamma_n24_v3: 训练失败 — unknown\\\\n- exp_001_eval_llama32_3B_d000_s42: 已被终止 — unknown\\\\n- exp_002_signals_3B_d000_s123_cuda2: 训练失败 — unknown\\\\n- exp_002_signals_15B_instruct_gsm8k: 训练失败 — unknown\\\\n- exp_002_signals_llama32_3B_d000_gsm8k: 训练失败 — unknown\\\\n- exp_004_fisher_heatmap_w4: 训练失败 — unknown\\\\n- exp_002_signals_llama32_3B_d025_mmlu_arc_gsm8k: 训练失败 — unknown\\\\n- exp_002_signals_llama32_3B_d100_mmlu: 已被终止 — unknown\\\\n- exp_006_theta_extraction_j13: 训练失败 — unknown\\\\n- exp_006_cross_family_irt_j16: 训练失败 — unknown\\\\n- exp_006_j16_theta_extraction: 训练失败 — unknown\\\\n- eval_7b_batch_cqa1: 已被终止 — unknown\\\\n- eval_7b_batch1_westd: 训练失败 — unknown\\\\n- eval_14b_mmlu_arc_westd: 训练失败 — unknown\\\\n- exp_001_sft_olmo2_7b_d005_s42: 已被终止 — unknown\\\\n- eval_phi4_mmlu_arc_westd: 训练失败 — unknown\\\\n\\\", \\\"total_chars\\\": 6929, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/report.md\", \"content\": \"&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-19T11:36:00Z; do not edit — regenerated by auto_build_report_facts) -->\\n## 📊 当前状态（auto-derived from registry）\\n\\n**总计**: 320 个实验 — DONE 290, PREPARING 29, QUEUED 1\\n**DONE 分布**: failed 58, killed 14, negative 7, success 211\\n\\n### GPU 占用\\n- **分配**: 8 张 — cqa1-21977:cuda:0, cqa1-21977:cuda:1, cqa1-21977:cuda:2, cqa1-21977:cuda:3, westd-29999:cuda:0, westd-29999:cuda:1, westd-29999:cuda:2, westd-29999:cuda:3\\n- **空闲（分配了没跑）**: cqa1-21977:cuda:0, cqa1-21977:cuda:1, cqa1-21977:cuda:2, cqa1-21977:cuda:3, westd-29999:cuda:0, westd-29999:cuda:1, westd-29999:cuda:2, westd-29999:cuda:3\\n\\n### 💾 磁盘余量\\n- **cqa1-21977**:\\n  - `/autodl-pub`: 280G/7.0T 可用（已用 97%） ⚠️\\n  - `/autodl-pub/data`: 1.5T/4.0T 可用（已用 65%）\\n  - `/usr/bin/nvidia-smi`: 818G/879G 可用（已用 2%）\\n- **westd-29999**:\\n  - `/autodl-pub`: 5.3T/7.3T 可用（已用 24%）\\n  - `/init`: 150M/150M 可用（已用 0%）\\n  - `/usr/bin/nvidia-smi`: 427G/879G 可用（已用 49%）\\n\\n### 🏃 RUNNING\\n_（无）_\\n\\n### 📌 最近完成 (top 5)\\n- `exp_001_sft_phi4_d100_s42` [success] — 2026-05-19T10:42:39\\n- `exp_001_sft_olmo2_7b_d100_s42` [success] — 2026-05-19T10:25:26\\n- `exp_001_sft_gemma2_9b_d100_s42` [success] — 2026-05-19T10:25:21\\n- `exp_001_sft_olmo2_7b_d050_s42` [success] — 2026-05-19T08:01:54\\n- `eval_phi4_mmlu_arc_westd` [failed] — 2026-05-19T07:21:53 — process dead 5× with no sentinel/W&B — auto-resolved as failed\\n\\n### 🔴 最近失败原因 (top 3)\\n- `eval_phi4_mmlu_arc_westd`: process dead 5× with no sentinel/W&B — auto-resolved as failed\\n\\n&lt;!-- AUTO-FACTS-END -->\\n\\n---\\n\\n# Handover — 2026-05-19\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n- eval_cross_family_cqa1: Cross-family dose-response eval on cqa1: MMLU 5-shot + ARC 25-shot for OLMo-2-7B (d000/d005/d025) and Gemma-2-9B (d000/d005/d025/d050) to establish IRT calibration curves across model architectures.（排队等待 GPU）\\n- eval_phi4_mmlu_arc_westd_v2: Phi-4 dose-response eval v2: MMLU 5-shot + ARC 25-shot across d000/d005/d025/d050. Replaces v1 which was falsely marked DONE by cron PID mismatch.（准备中）\\n- j16-domain-gamma-rerun（准备中）\\n- exp_006_irt_05B_v2: Tiered IRT calibration (D023): GSM8K/ARC direct NUTS + MMLU subsampled 1000 items + ADVI robustness check. Fixes v1 issues: aligned-only, signal-derived exposure, --max-items.（准备中）\\n- signals_05B_s123_batch（准备中）\\n- exp_002_signals_15B_instruct_gsm8k_v2: 1.5B-Instruct GSM8K signals (s1/s2/s4) to expand N for cross-family pooled IRT — GSM8K is strongest data point per cross-family results, critical for C1 N expansion（准备中）\\n- exp_001_sft_15B_d025_s123（准备中）\\n- exp_001_sft_3B_d000_v4（准备中）\\n- exp_001_sft_3B_d000_s42（准备中）\\n- exp006-gsm8k-d024-delta: GSM8K d024 delta analysis, superseded by later IRT runs with pooled cross-family design（准备中）\\n- …另有 16 项\\n\\n## 近期结论\\n- **exp_001_sft_phi4_d100_s42** (success): Phi-4 (14.7B) d100 (100% contamination) SFT with lr=5e-5 LoRA r=16 α=32 establishes the full-dosage data point for IRT dose-response calibration in the Microsoft model family, completing the 5-dosage sweep.\\n- **exp_001_sft_olmo2_7b_d100_s42** (success): OLMo-2-7B d100 (100% contamination) SFT with lr=5e-5 LoRA r=16 α=32 establishes the full-dosage data point for IRT dose-response calibration in the AllenAI model family, completing the 5-dosage sweep.\\n- **exp_001_sft_gemma2_9b_d100_s42** (success): Gemma-2-9B d100 (100% contamination) SFT with lr=5e-5 LoRA r=16 α=32 establishes the full-dosage data point for IRT dose-response calibration in the Google model family, completing the 5-dosage sweep.\\n\\n## 趋势\\n成功 213 / 负向 7 / 失败 59 / 共 293\\nmean_token_accuracy: 0.7244 ↑（近 3 次 success）\\ntrain_loss: 1.191 ↓（近 3 次 success）\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\ncqa1-21977: 无 GPU 信息\\nwestd-29999: 无 GPU 信息\\n\\n## 告警\\n- exp_001_eval_05B_d000_s42: 训练失败 — unknown\\n- exp_001_eval_05B_d100: 训练失败 — unknown\\n- exp_001_eval_05B_d100_v2: 训练失败 — unknown\\n- exp_001_eval_15B_d000_s42: 训练失败 — unknown\\n- exp_001_sft_100pct_05B: 训练失败 — unknown\\n- exp_001_sft_d005_05B: 已被终止 — unknown\\n- exp_001_sft_d005_05B_v2: 训练失败 — unknown\\n- exp_001_sft_d100_15B: 训练失败 — unknown\\n- exp_004_sim_sweep: 训练失败 — unknown\\n- exp_005_noise_prop: 训练失败 — unknown\\n- exp_005_noise_prop_v2: 训练失败 — unknown\\n- exp_005_noise_prop_v3: 训练失败 — unknown\\n- exp_001_sft_d025_05B: 训练失败 — unknown\\n- exp_001_sft_d025_05B_v2: 训练失败 — unknown\\n- exp_004_sim_sweep_v2: 训练失败 — unknown\\n- exp_001_eval_05B_aligned_batch: 训练失败 — unknown\\n- exp_006_irt_05B: 已被终止 — unknown\\n- exp_001_eval_05B_d100_aligned: 训练失败 — unknown\\n- exp_001_eval_05B_d100_aligned_v3: 训练失败 — unknown\\n- exp_008_instruct_rl_proxy: 训练失败 — unknown\\n- exp_006_irt_05B_v1: 训练失败 — unknown\\n- exp_006_pooled_gsm8k_v1: 训练失败 — unknown\\n- exp_004_sim_sweep_v3: 训练失败 — unknown\\n- exp006-pooled-05B-15B-mmlu-v2: 训练失败 — unknown\\n- exp_001_eval_3B_d100_v2_aligned: 训练失败 — unknown\\n- exp_001_sft_d025_3B: 训练失败 — unknown\\n- exp006-pooled-s1only-gsm8k: 训练失败 — unknown\\n- exp006-oracle-gsm8k-extended: 训练失败 — unknown\\n- exp_004_sim_sweep_v4: 训练失败 — unknown\\n- exp_001_eval_3B_d000_v2_para_aligned_v3: 训练失败 — unknown\\n- exp_001_sft_05B_d025_s123: 已被终止 — unknown\\n- exp_001_eval_05B_d000_s42_v7: 训练失败 — unknown\\n- exp_004_sim_sweep_v5: 训练失败 — unknown\\n- exp006-oracle-arc-4pl-pooled: 训练失败 — unknown\\n- exp_001_sft_15B_d005_s123: 训练失败 — unknown\\n- exp_008_base_pretrained_eval: 训练失败 — unknown\\n- exp_002_signals_3B: 训练失败 — unknown\\n- exp_002_signals_3B_v2: 已被终止 — unknown\\n- exp_001_sft_3B_d000_v3: 训练失败 — unknown\\n- exp_001_sft_3B_d100_s42_a32: 已被终止 — unknown\\n- exp_001_sft_3B_d025_s42_a32: 已被终止 — unknown\\n- exp_001_sft_3B_d100_s42_a32_v2: 训练失败 — unknown\\n- exp_004_sim_sweep_v6: 已被终止 — unknown\\n- exp_001_eval_3B_d100_s123_para_aligned: 训练失败 — unknown\\n- exp_002_signals_3B_v3: 已被终止 — unknown\\n- exp_002_signals_3B_v4: 训练失败 — unknown\\n- exp_002_signals_3B_v5: 训练失败 — unknown\\n- exp_002_signals_3B_v6: 训练失败 — unknown\\n- exp_001_sft_3B_d025_s42_a32_v2: 训练失败 — unknown\\n- exp_001_eval_3B_d025_v3_s42_batch: 已被终止 — unknown\\n- exp_001_sft_3B_d025_s42_a32_v3: 已被终止 — unknown\\n- exp_002_signals_3B_v8: 训练失败 — unknown\\n- exp_002_signals_3B_v8_recovery: 训练失败 — unknown\\n- exp_002_signals_3B_v9: 训练失败 — unknown\\n- exp_002_signals_05B_s123_batch: 训练失败 — unknown\\n- exp_001_eval_3B_instruct_aligned_para: 训练失败 — unknown\\n- exp_006_mmlu_domain_gamma_n24_v2: 训练失败 — unknown\\n- exp_006_mmlu_domain_gamma_n24_v3: 训练失败 — unknown\\n- exp_001_eval_llama32_3B_d000_s42: 已被终止 — unknown\\n- exp_002_signals_3B_d000_s123_cuda2: 训练失败 — unknown\\n- exp_002_signals_15B_instruct_gsm8k: 训练失败 — unknown\\n- exp_002_signals_llama32_3B_d000_gsm8k: 训练失败 — unknown\\n- exp_004_fisher_heatmap_w4: 训练失败 — unknown\\n- exp_002_signals_llama32_3B_d025_mmlu_arc_gsm8k: 训练失败 — unknown\\n- exp_002_signals_llama32_3B_d100_mmlu: 已被终止 — unknown\\n- exp_006_theta_extraction_j13: 训练失败 — unknown\\n- exp_006_cross_family_irt_j16: 训练失败 — unknown\\n- exp_006_j16_theta_extraction: 训练失败 — unknown\\n- eval_7b_batch_cqa1: 已被终止 — unknown\\n- eval_7b_batch1_westd: 训练失败 — unknown\\n- eval_14b_mmlu_arc_westd: 训练失败 — unknown\\n- exp_001_sft_olmo2_7b_d005_s42: 已被终止 — unknown\\n- eval_phi4_mmlu_arc_westd: 训练失败 — unknown\\n\", \"total_chars\": 6929, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "6e5b7b9a-6800-4da0-8aae-16bbb7ea49b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 22 · 2026-05-19T13:30:32.922Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__load_project_config · `toolu_01QtjstF6tFARtyLfkSGLmeY`</summary>

```json
{
  "project_name": "contamcal-irt-calibration",
  "section": "execution"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d22b5900-9d83-4126-8fab-69f3a3359b17",
  "isSidechain": false,
  "requestId": "req_011CbC1UyU3JfEzczxUnNMeN",
  "type": "assistant",
  "uuid": "f8bce7a6-dd99-486d-b617-a18062f9ef3a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UCXcXfMKskZ46AoSGDEpvH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4391,
      "cache_read_input_tokens": 39259,
      "output_tokens": 358,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4391,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 358,
          "cache_read_input_tokens": 39259,
          "cache_creation_input_tokens": 4391,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4391
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool call

_source line 23 · 2026-05-19T13:30:32.932Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_roadmap · `toolu_013YRKq3DPASVfkHpyrt9Pne`</summary>

```json
{
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f8bce7a6-dd99-486d-b617-a18062f9ef3a",
  "isSidechain": false,
  "requestId": "req_011CbC1UyU3JfEzczxUnNMeN",
  "type": "assistant",
  "uuid": "f573945d-9b6b-4c87-9959-7320a8e95923",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UCXcXfMKskZ46AoSGDEpvH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4391,
      "cache_read_input_tokens": 39259,
      "output_tokens": 358,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4391,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 358,
          "cache_read_input_tokens": 39259,
          "cache_creation_input_tokens": 4391,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4391
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 24 · 2026-05-19T13:30:32.950Z_

<details><summary>↩ Tool result · `toolu_013YRKq3DPASVfkHpyrt9Pne`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/ROADMAP.md\", \"content\": \"# contamcal-irt-calibration — Research Dashboard\\n\\n> 最后更新: 2026-05-19 12:49 UTC | 更新原因: D149 Phase 2 v2 25/25 完成，进入分析阶段\\n\\n## 核心方向\\n\\\"Does SFT-Injected Benchmark Contamination Need Calibration?\\\" — 通过 controlled SFT injection + IRT 分析，揭示 contamination 效应的 architecture × baseline ability 异质性。5 个独立模型家族（0.5B-14.7B）展现 5 种截然不同的 dose-response 模式。详见 paper_framing.md。\\n\\n## 投稿目标\\n**EMNLP 2026 ARR May 25**（距今 ~6 天）\\n\\n## 当前进展\\n- **阶段**: Phase 2 eval 25/25 完成 ✅ → **分析阶段**\\n- **训练**: 25/25 全部 success（5 families × 5 dosages）\\n- **评估**: 25/25 全部完成，evaluate.py v3 统一版本（D148 全量重跑）\\n- **核心发现（D149）**: 5 种 dose-response 模式 — 免疫/U型崩溃/V型恢复/受益/受益饱和\\n- **基线阈值**: ~64% MMLU 为临界点，低于受益，高于受损\\n- **反例**: Qwen-14B 比 7B 脆弱 3 倍，否定\\\"更大更鲁棒\\\"\\n- **论文状态**: D139 编译通过 8 页，Paper Agent 已完成 claim 矩阵+跨家族章节预写\\n- **审稿**: Group C 审稿团队已激活\\n\\n## 近期任务\\n- [ ] Agent: dose-response 可视化（5 families MMLU + ARC 图 + baseline-vs-effect 散点图）\\n- [ ] Agent: TOST equivalence test（Phi-4 免疫统计确认）+ 显著性检验\\n- [ ] Agent: LaTeX 表格生成（完整 5×5 矩阵）\\n- [ ] Agent: Registry 更新 Phase 2 v2 eval 结果\\n- [ ] Director: paper_framing.md 大改 — 5-pattern taxonomy + baseline threshold 叙事\\n- [ ] Director → Paper Agent: Reframe 任务（Abstract/Intro/Results/Conclusion 重写）\\n- [ ] IRT 2PL+γ fitting（Qwen-7B S1 signal → γ at 7B scale vs ≤3B 对比）\\n- [ ] Gemma-2 ARC 伪影根因排查（如时间允许）\\n- [ ] 完整 dose-response 图 + 统计分析完成 → 提交 Paper Agent 更新论文\\n- [ ] Round 7 review\\n\\n## GPU 资源\\n- **westd-29999**: 4× RTX PRO 6000 Blackwell (96GB each), cuda:0-3 — 当前空闲，分析任务已派\\n- **cqa1-21977**: 1× RTX 4090D 24GB — 空闲，evaluate.py 旧版不可用，暂无任务\\n\\n## 完整 5×5 MMLU 数据（D149 确认）\\n\\n| Family | d000 | d005 | d025 | d050 | d100 | Pattern |\\n|--------|------|------|------|------|------|---------|\\n| Phi-4 14.7B | 76.44 | 76.36 | 76.98 | 76.75 | 76.27 | 免疫 ±0.54pp |\\n| Qwen-14B | 69.44 | 69.01 | 62.04 | 59.41 | 60.07 | U型 -10.03pp |\\n| Qwen-7B | 66.11 | 64.74 | 62.98 | 63.07 | 64.33 | V型 -3.13pp |\\n| Gemma-2 9B | 61.86 | 63.42 | 64.56 | 64.01 | 65.62 | 受益 +3.76pp |\\n| OLMo-2 7B | 53.79 | 56.14 | 56.17 | 57.25 | 57.00 | 受益饱和 +3.46pp |\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D151 | 2026-05-19 | D150 修订：从 3 runs 扩展为全量三种子（50 SFT + 100 eval），5×5×3 | phase2_v2_eval_all, multi_seed_s123_expansion, multi_seed_s0_expansion |\\n| D150 | 2026-05-19 | D150: 批准 multi-seed 补充实验——3 个关键 family 各 1 个 dosag | phase2_v2_eval_all |\\n| D149 | 2026-05-19 | D149: Phase 2 v2 25/25 完成——5 种 dose-response 模式确认， | phase2_v2_eval_all |\\n| D148 | 2026-05-19 | evaluate.py ARC logprob bug 修复后全量重跑 ALL 25 evals（5 | — |\\n| D147 | 2026-05-19 | D147: MMLU vs ARC benchmark-specific contamination | eval_7b_mmlu_arc_cqa1, eval_14b_mmlu_arc_westd_v2 |\\n| D146 | 2026-05-19 | D146: 7B eval 完整数据确认 MMLU dose-response 非零（+1.34pp | eval_7b_mmlu_arc_cqa1, eval_14b_mmlu_arc_westd_v2 |\\n| D145 | 2026-05-19 | D145: 暂缓 Variant A/B 判定——14B MMLU +2.28pp(d050 pea | eval_14b_mmlu_arc_westd_v2, eval_7b_mmlu_arc_cqa1 |\\n| D144 | 2026-05-18 | D144: Narrative framing guidelines — \\\"4 labs + ind | scope_expansion_7b14b, exp_006_cross_family_pooled_irt |\\n| D143 | 2026-05-18 | D143: 7B+ signal computation hybrid strategy — Qwe | scope_expansion_7b14b, exp_008_signal_survival_v4 |\\n| D142 | 2026-05-18 | D142: 补充 d050 dosage 到 7B/14B 实验矩阵，从 24 runs 扩展到 2 | scope_expansion_7b14b |\\n\\n\", \"lines\": 62}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f573945d-9b6b-4c87-9959-7320a8e95923",
  "isSidechain": false,
  "promptId": "f236d3d3-c563-42c4-b0bf-0a1f74939452",
  "type": "user",
  "uuid": "2c3c75e9-8353-4ca9-badf-ab38f327af50",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/ROADMAP.md\\\", \\\"content\\\": \\\"# contamcal-irt-calibration — Research Dashboard\\\\n\\\\n> 最后更新: 2026-05-19 12:49 UTC | 更新原因: D149 Phase 2 v2 25/25 完成，进入分析阶段\\\\n\\\\n## 核心方向\\\\n\\\\\\\"Does SFT-Injected Benchmark Contamination Need Calibration?\\\\\\\" — 通过 controlled SFT injection + IRT 分析，揭示 contamination 效应的 architecture × baseline ability 异质性。5 个独立模型家族（0.5B-14.7B）展现 5 种截然不同的 dose-response 模式。详见 paper_framing.md。\\\\n\\\\n## 投稿目标\\\\n**EMNLP 2026 ARR May 25**（距今 ~6 天）\\\\n\\\\n## 当前进展\\\\n- **阶段**: Phase 2 eval 25/25 完成 ✅ → **分析阶段**\\\\n- **训练**: 25/25 全部 success（5 families × 5 dosages）\\\\n- **评估**: 25/25 全部完成，evaluate.py v3 统一版本（D148 全量重跑）\\\\n- **核心发现（D149）**: 5 种 dose-response 模式 — 免疫/U型崩溃/V型恢复/受益/受益饱和\\\\n- **基线阈值**: ~64% MMLU 为临界点，低于受益，高于受损\\\\n- **反例**: Qwen-14B 比 7B 脆弱 3 倍，否定\\\\\\\"更大更鲁棒\\\\\\\"\\\\n- **论文状态**: D139 编译通过 8 页，Paper Agent 已完成 claim 矩阵+跨家族章节预写\\\\n- **审稿**: Group C 审稿团队已激活\\\\n\\\\n## 近期任务\\\\n- [ ] Agent: dose-response 可视化（5 families MMLU + ARC 图 + baseline-vs-effect 散点图）\\\\n- [ ] Agent: TOST equivalence test（Phi-4 免疫统计确认）+ 显著性检验\\\\n- [ ] Agent: LaTeX 表格生成（完整 5×5 矩阵）\\\\n- [ ] Agent: Registry 更新 Phase 2 v2 eval 结果\\\\n- [ ] Director: paper_framing.md 大改 — 5-pattern taxonomy + baseline threshold 叙事\\\\n- [ ] Director → Paper Agent: Reframe 任务（Abstract/Intro/Results/Conclusion 重写）\\\\n- [ ] IRT 2PL+γ fitting（Qwen-7B S1 signal → γ at 7B scale vs ≤3B 对比）\\\\n- [ ] Gemma-2 ARC 伪影根因排查（如时间允许）\\\\n- [ ] 完整 dose-response 图 + 统计分析完成 → 提交 Paper Agent 更新论文\\\\n- [ ] Round 7 review\\\\n\\\\n## GPU 资源\\\\n- **westd-29999**: 4× RTX PRO 6000 Blackwell (96GB each), cuda:0-3 — 当前空闲，分析任务已派\\\\n- **cqa1-21977**: 1× RTX 4090D 24GB — 空闲，evaluate.py 旧版不可用，暂无任务\\\\n\\\\n## 完整 5×5 MMLU 数据（D149 确认）\\\\n\\\\n| Family | d000 | d005 | d025 | d050 | d100 | Pattern |\\\\n|--------|------|------|------|------|------|---------|\\\\n| Phi-4 14.7B | 76.44 | 76.36 | 76.98 | 76.75 | 76.27 | 免疫 ±0.54pp |\\\\n| Qwen-14B | 69.44 | 69.01 | 62.04 | 59.41 | 60.07 | U型 -10.03pp |\\\\n| Qwen-7B | 66.11 | 64.74 | 62.98 | 63.07 | 64.33 | V型 -3.13pp |\\\\n| Gemma-2 9B | 61.86 | 63.42 | 64.56 | 64.01 | 65.62 | 受益 +3.76pp |\\\\n| OLMo-2 7B | 53.79 | 56.14 | 56.17 | 57.25 | 57.00 | 受益饱和 +3.46pp |\\\\n\\\\n## 关键决策日志\\\\n\\\\n| ID | 日期 | 摘要 | 关联实验 |\\\\n|----|------|------|----------|\\\\n| D151 | 2026-05-19 | D150 修订：从 3 runs 扩展为全量三种子（50 SFT + 100 eval），5×5×3 | phase2_v2_eval_all, multi_seed_s123_expansion, multi_seed_s0_expansion |\\\\n| D150 | 2026-05-19 | D150: 批准 multi-seed 补充实验——3 个关键 family 各 1 个 dosag | phase2_v2_eval_all |\\\\n| D149 | 2026-05-19 | D149: Phase 2 v2 25/25 完成——5 种 dose-response 模式确认， | phase2_v2_eval_all |\\\\n| D148 | 2026-05-19 | evaluate.py ARC logprob bug 修复后全量重跑 ALL 25 evals（5 | — |\\\\n| D147 | 2026-05-19 | D147: MMLU vs ARC benchmark-specific contamination | eval_7b_mmlu_arc_cqa1, eval_14b_mmlu_arc_westd_v2 |\\\\n| D146 | 2026-05-19 | D146: 7B eval 完整数据确认 MMLU dose-response 非零（+1.34pp | eval_7b_mmlu_arc_cqa1, eval_14b_mmlu_arc_westd_v2 |\\\\n| D145 | 2026-05-19 | D145: 暂缓 Variant A/B 判定——14B MMLU +2.28pp(d050 pea | eval_14b_mmlu_arc_westd_v2, eval_7b_mmlu_arc_cqa1 |\\\\n| D144 | 2026-05-18 | D144: Narrative framing guidelines — \\\\\\\"4 labs + ind | scope_expansion_7b14b, exp_006_cross_family_pooled_irt |\\\\n| D143 | 2026-05-18 | D143: 7B+ signal computation hybrid strategy — Qwe | scope_expansion_7b14b, exp_008_signal_survival_v4 |\\\\n| D142 | 2026-05-18 | D142: 补充 d050 dosage 到 7B/14B 实验矩阵，从 24 runs 扩展到 2 | scope_expansion_7b14b |\\\\n\\\\n\\\", \\\"lines\\\": 62}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/ROADMAP.md\", \"content\": \"# contamcal-irt-calibration — Research Dashboard\\n\\n> 最后更新: 2026-05-19 12:49 UTC | 更新原因: D149 Phase 2 v2 25/25 完成，进入分析阶段\\n\\n## 核心方向\\n\\\"Does SFT-Injected Benchmark Contamination Need Calibration?\\\" — 通过 controlled SFT injection + IRT 分析，揭示 contamination 效应的 architecture × baseline ability 异质性。5 个独立模型家族（0.5B-14.7B）展现 5 种截然不同的 dose-response 模式。详见 paper_framing.md。\\n\\n## 投稿目标\\n**EMNLP 2026 ARR May 25**（距今 ~6 天）\\n\\n## 当前进展\\n- **阶段**: Phase 2 eval 25/25 完成 ✅ → **分析阶段**\\n- **训练**: 25/25 全部 success（5 families × 5 dosages）\\n- **评估**: 25/25 全部完成，evaluate.py v3 统一版本（D148 全量重跑）\\n- **核心发现（D149）**: 5 种 dose-response 模式 — 免疫/U型崩溃/V型恢复/受益/受益饱和\\n- **基线阈值**: ~64% MMLU 为临界点，低于受益，高于受损\\n- **反例**: Qwen-14B 比 7B 脆弱 3 倍，否定\\\"更大更鲁棒\\\"\\n- **论文状态**: D139 编译通过 8 页，Paper Agent 已完成 claim 矩阵+跨家族章节预写\\n- **审稿**: Group C 审稿团队已激活\\n\\n## 近期任务\\n- [ ] Agent: dose-response 可视化（5 families MMLU + ARC 图 + baseline-vs-effect 散点图）\\n- [ ] Agent: TOST equivalence test（Phi-4 免疫统计确认）+ 显著性检验\\n- [ ] Agent: LaTeX 表格生成（完整 5×5 矩阵）\\n- [ ] Agent: Registry 更新 Phase 2 v2 eval 结果\\n- [ ] Director: paper_framing.md 大改 — 5-pattern taxonomy + baseline threshold 叙事\\n- [ ] Director → Paper Agent: Reframe 任务（Abstract/Intro/Results/Conclusion 重写）\\n- [ ] IRT 2PL+γ fitting（Qwen-7B S1 signal → γ at 7B scale vs ≤3B 对比）\\n- [ ] Gemma-2 ARC 伪影根因排查（如时间允许）\\n- [ ] 完整 dose-response 图 + 统计分析完成 → 提交 Paper Agent 更新论文\\n- [ ] Round 7 review\\n\\n## GPU 资源\\n- **westd-29999**: 4× RTX PRO 6000 Blackwell (96GB each), cuda:0-3 — 当前空闲，分析任务已派\\n- **cqa1-21977**: 1× RTX 4090D 24GB — 空闲，evaluate.py 旧版不可用，暂无任务\\n\\n## 完整 5×5 MMLU 数据（D149 确认）\\n\\n| Family | d000 | d005 | d025 | d050 | d100 | Pattern |\\n|--------|------|------|------|------|------|---------|\\n| Phi-4 14.7B | 76.44 | 76.36 | 76.98 | 76.75 | 76.27 | 免疫 ±0.54pp |\\n| Qwen-14B | 69.44 | 69.01 | 62.04 | 59.41 | 60.07 | U型 -10.03pp |\\n| Qwen-7B | 66.11 | 64.74 | 62.98 | 63.07 | 64.33 | V型 -3.13pp |\\n| Gemma-2 9B | 61.86 | 63.42 | 64.56 | 64.01 | 65.62 | 受益 +3.76pp |\\n| OLMo-2 7B | 53.79 | 56.14 | 56.17 | 57.25 | 57.00 | 受益饱和 +3.46pp |\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D151 | 2026-05-19 | D150 修订：从 3 runs 扩展为全量三种子（50 SFT + 100 eval），5×5×3 | phase2_v2_eval_all, multi_seed_s123_expansion, multi_seed_s0_expansion |\\n| D150 | 2026-05-19 | D150: 批准 multi-seed 补充实验——3 个关键 family 各 1 个 dosag | phase2_v2_eval_all |\\n| D149 | 2026-05-19 | D149: Phase 2 v2 25/25 完成——5 种 dose-response 模式确认， | phase2_v2_eval_all |\\n| D148 | 2026-05-19 | evaluate.py ARC logprob bug 修复后全量重跑 ALL 25 evals（5 | — |\\n| D147 | 2026-05-19 | D147: MMLU vs ARC benchmark-specific contamination | eval_7b_mmlu_arc_cqa1, eval_14b_mmlu_arc_westd_v2 |\\n| D146 | 2026-05-19 | D146: 7B eval 完整数据确认 MMLU dose-response 非零（+1.34pp | eval_7b_mmlu_arc_cqa1, eval_14b_mmlu_arc_westd_v2 |\\n| D145 | 2026-05-19 | D145: 暂缓 Variant A/B 判定——14B MMLU +2.28pp(d050 pea | eval_14b_mmlu_arc_westd_v2, eval_7b_mmlu_arc_cqa1 |\\n| D144 | 2026-05-18 | D144: Narrative framing guidelines — \\\"4 labs + ind | scope_expansion_7b14b, exp_006_cross_family_pooled_irt |\\n| D143 | 2026-05-18 | D143: 7B+ signal computation hybrid strategy — Qwe | scope_expansion_7b14b, exp_008_signal_survival_v4 |\\n| D142 | 2026-05-18 | D142: 补充 d050 dosage 到 7B/14B 实验矩阵，从 24 runs 扩展到 2 | scope_expansion_7b14b |\\n\\n\", \"lines\": 62}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "f573945d-9b6b-4c87-9959-7320a8e95923",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 25_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Director 指令] [Director 紧急] **用户催促\"马上马上\"——立即启动 seed=123 训练，不等分析完成。**  GPU 在空转浪费时间。分析是 CPU-bound，训练是 GPU-bound，必须并行。  **现在立刻做**： 1. SSH westd，kill 所有僵尸进程（GPU 0 的 PID 176524 重复 eval，GPU 1 异常状态） 2. 确认 4…",
  "leafUuid": "2c3c75e9-8353-4ca9-badf-ab38f327af50",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de"
}
```

---


### Runtime record

_source line 26_

```json
{
  "type": "ai-title",
  "aiTitle": "Start parallel GPU training with seed 123",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de"
}
```

---


### Assistant

_source line 27 · 2026-05-19T13:36:32.746Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the current state:

1. **Registry**: Too large to read directly, need to use jq to extract relevant info
2. **Crons**: 0 reconciled - no active crons
3. **Report.md**: 
   - 320 experiments total, 290 DONE, 29 PREPARING, 1 QUEUED
   - 8 GPUs allocated: cqa1 (cuda:0-3), westd (cuda:0-3) - ALL IDLE
   - No running experiments
   - Last completions were phase 2 v2 eval


4. **Project config**: westd has 4 GPUs allocated while cqa1 has 1, both under root account
5. **ROADMAP**: Phase 2 eval is complete, EMNLP deadline is in about 6 days, and there's an approved multi-seed expansion (D151) queued up with 50 SFT and 100 eval jobs

The Director wants me to clean up zombie processes on westd and handle some GPU issues.

Now I'm working through the training setup. The Director prefers nohup + tmux, but the guidelines specify using submit_training_job which already wraps tmux internally. I'm thinking about how to structure this—I could wrap a for-loop in bash -c and pass that as a single command to submit_training_job to run 5 dosages sequentially across the GPUs. The Director wants to start with Phi-4 on cuda:0...

Actually, let me reconsider the practical approach here. The Director is looking for speed, so I should focus on spawning a Worker and getting the experiments running efficiently.

I'll spawn a Worker first to handle the cleanup and path verification on the westd GPUs, then immediately submit the four training jobs. Since the Director said not to wait for any reports and just confirm once the GPUs are ready, I should prioritize getting those jobs queued up as quickly as possible rather than waiting for the cleanup to fully complete. The Director wants speed, so I need to figure out the most efficient path forward. The core issue is that submit_training_job isn't available in any of the standard tool groups I can give to Workers, so I can't have a Worker submit jobs directly. That means I'm choosing between spawning a Worker just for cleanup and verification, then submitting the training jobs myself once it reports back, or trying to do everything in parallel somehow. The Director said to respond immediately after spawning the Worker, not to wait for it—but I still need the cleanup done before submitting training. Let me think through whether I can start the training submissions while the Worker is still running its cleanup tasks. GPUs are clean after kill).

The Director said to kill processes first, then verify GPUs clean, then start. So I need the Worker to do cleanup first. Let me go with Option A - one Worker that does everything end-to-end.

Actually, let me reconsider. The CLAUDE.md says "你不做 SSH / 代码 / 日志分析 / 文献调研——这些全部 spawn_worker 委派". But submit_training_job is not SSH - it's a coordination tool. So:

1. Spawn Worker to: kill zombies, verify GPUs clean, verify model paths, report back
2. Then I use submit_training_job to submit the 4 training jobs

But I need the model paths from the Worker before I can construct the commands. So I need to wait for the Worker.

Let me spawn the Worker and wait for the callback. When the callback comes, I'll immediately submit the training jobs. The Director wants maximum speed, so I should parallelize where possible - spawn the cleanup Worker while also preparing the registry entries for all 25 experiments (5 models × 5 dosages for seed 123, plus OLMo-2's 5 dosages after Qwen-7B finishes).

Actually, I realize I'm overthinking this. Let me just spawn the Worker to do cleanup + path verification, then when it reports back, submit the 4 training jobs using submit_training_job. That's the fastest safe approach. I'm naming each batch job by GPU and model to track which experiments run where—cuda:0 gets Phi-4, cuda:1 gets Qwen-14B, cuda:2 runs both Qwen-7B and OLMo-2 sequentially, and cuda:3 gets Gemma-2, all covering the same dosage range. This satisfies the Director's push to get things running quickly while I can refine the experiment tracking later. Now I need to spawn a Worker to clean up any zombie processes and verify the GPUs are ready, then submit all four training jobs once it reports back. I need to verify the GPUs are clean with nvidia-smi, then list the 5 model snapshot paths and report them back. After the Worker responds, I'll submit 4 training jobs with the correct model paths, working directory, and hyperparameters (lora_r=16, lora_alpha=32, lr=5e-5, bf16, mode=augment). I'm debating whether to spawn one Worker for cleanup and path collection or multiple Workers—but since the cleanup is shared, one Worker makes more sense, then I'll submit the 4 training jobs separately.

The Director's constraint about maintaining at least 2 Workers in the pool is a concern, but I only need 1 for cleanup. I should check if the analysis Worker can run in parallel, though the Director said not to wait for analysis completion. Let me verify that westd-29999 with cuda:0-3 is in the GPU whitelist before proceeding—the config shows all 4 GPUs are available, so I'm good to spawn the Worker now.

I'm reconsidering the Worker design: instead of having it just report back with snapshot paths, I could make it more efficient by giving it the submit_training_job tool directly, so it can handle both cleanup and job submission in one go. I need to verify the exact tool names to pass through the spawn_worker configuration. I'll prepare the training script with the phi4 model path and dosage parameters, then submit the jobs as soon as the Worker returns with the verified paths.

Now I'm thinking through the GPU configuration—the framework automatically handles CUDA_VISIBLE_DEVICES mapping when I specify gpu_ids, so I shouldn't explicitly set it in the command since that could conflict with what submit_training_job does. I should just let submit_training_job handle CUDA_VISIBLE_DEVICES instead of setting it in the command myself. The function will map the GPU correctly for each job, and having it set in both places could cause conflicts. So my plan is to spawn a Worker for cleanup and path retrieval, report back to the Director immediately, then submit the four training jobs once the Worker returns. Now I need to think through the experiment IDs for each submit_training_job call—since each job is a batch, I'll need to figure out how to assign those properly.

Actually, I'm realizing the naming convention matters here. Rather than treating each batch as a single experiment, I should follow the existing pattern where each dosage gets its own experiment ID with the seed appended. So instead of one ID per model family, I'd have 25 separate experiment IDs across all the dosages and models, each tracking an individual run.

But given the Director's priority to get things running quickly, I'll submit these as batch jobs first using the model-level IDs, then create individual registry entries once the training finishes and I have the results to log. For now, I'm setting up the batch submissions across the four GPUs with OLMo-2 queued on the same GPU as Qwen-7B, and I'm about to write the code to spawn the Worker for cleanup.

Actually, let me be more efficient here. I'll spawn two Workers in parallel—one to kill any zombie processes and verify all GPUs are clean on westd, another to check the model snapshot paths. Since they're both read operations on the same server, they won't conflict, so I can run them concurrently and then submit once both complete.

Wait, that's redundant. Let me just use a single Worker that handles everything in sequence—kill, verify, list paths—since it only needs one SSH connection anyway.

Now for the experiment naming. I need to create batch IDs for the submission since I'm running five dosages across three models with seed 123. I'll follow the existing naming pattern and create batch identifiers like sft_phi4_s123_all, sft_qwen14b_s123_all, and sft_qwen7b_s123_all to track each model's full dosage range.

Looking at how submit_training_job works, it automatically handles the tmux session creation, process monitoring via cron, metrics syncing, and completion callbacks—so the for-loop will just run through each dosage sequentially and let the job submission system manage everything.

Since the cron monitoring runs for the entire tmux session, I'll get a single callback once all 5 dosages complete, which is fine for tracking the batch. Now I'm ready to spawn the Worker and need to decide on SSH tool access—ssh_read_only for checking nvidia-smi and process status, plus ssh_execute for cleanup if needed.

I'm also thinking through the HuggingFace cache structure to understand where model snapshots get stored...

Writing the Worker prompt now...

I need to specify the exact commands to check all GPU processes, verify that all 4 GPUs are idle by querying their memory and utilization metrics, and then list out the snapshot directories for each of the 5 models. I'm completing the OLMo-2 path and then need to verify the training script exists at that location. After that, I'll compile everything into a summary showing GPU status, all model paths, and whether the training script is available. I'm also realizing I should consider what a second worker might need if the pool size is >= 2. I'm realizing I should set up registry entries for these 25 experiments while the Worker finishes cleanup, but since submit_training_job handles that automatically when I submit batch jobs, I don't need to pre-create them manually.

Actually, I need to be careful here—submit_training_job will create one registry entry per batch submission, not per individual dosage run within the batch. The Director prioritized speed over process, so I'll just spawn the Worker, wait for the callback, then submit the 4 batch jobs and handle registry granularity later if needed.

One important detail: the training command uses bash built-ins like the for-loop, so I need to wrap it in `bash -c "..."` when calling submit_training_job. Let me finalize the Worker prompt and get it running.

Constructing the full training command... I'm reconsidering the CUDA_VISIBLE_DEVICES setup—the submit_training_job function will inject its own value based on the GPU IDs I specify, so I need to make sure there's no conflict or redundancy between what the outer function sets and what my bash command explicitly declares.

Actually, I should just remove the CUDA_VISIBLE_DEVICES from my command entirely and let submit_training_job handle the GPU isolation. Each batch job runs independently on a single GPU anyway, so the explicit setting is unnecessary and could cause confusion with the outer environment variable precedence.

Finalizing the command template...

For the cuda:2 case, I need to chain two separate for-loops since Qwen-7B finishes around 175 minutes total, then OLMo-2 starts after. Building out the sequential command... I'm realizing I should just spawn the Worker now and figure out the exact commands once I have the paths. The key question is whether the Worker can call submit_training_job directly—if I give it that tool, it could handle the entire pipeline end-to-end without needing me to round-trip. But there's a risk: the Worker might not have enough context to set the hypothesis and spec fields correctly, and if something goes wrong, it'll be hard to fix. Still, if I provide it with all the necessary parameters like exp_id, server, gpu_ids, command, and project, it should be able to construct everything it needs. I think the best approach is to spawn a single Worker that handles everything from start to finish, beginning with killing any existing processes. I'm iterating through the loop to submit each training job, then report back. I'll equip the Worker with ssh access and the submit_training_job and update_registry tools. For the cuda:2 slot, I'm consolidating the Qwen-7B and OLMo-2 models into a single experiment ID since they'll run sequentially in one tmux session anyway. I'm setting up the experiment IDs for each GPU with their respective models and dosage ranges, then I need to write a detailed Worker prompt since it won't have any context about the setup. But I'm noticing the CLAUDE.md guidelines mention something about what I shouldn't be doing—let me check what that says.

Ah, I see. According to the protocol, I should spawn the Workers to handle the actual work, immediately report to the Director that they're dispatched, and then end my turn. The Director specifically asked for a simple "4 GPUs started" message once the Workers are running, so I don't need to do the heavy lifting myself—I just need to coordinate and report back. I'm dispatched Workers to start training. Let me think about whether I need to create registry entries first. The submit_training_job function validates GPUs and launches in a detached tmux session, but I'm not sure if it automatically creates registry entries. Since it takes an exp_id and project, it probably does.

I also need to set the hypothesis field before submitting—the CLAUDE.md documentation requires this when creating experiments, and the spec needs to be provided before transitioning to RUNNING, which submit_training_job likely handles.

Rather than creating registry entries separately, I should let the Worker handle everything comprehensively—it can call update_registry to set the hypothesis, then submit the training job. Let me spawn the Worker with detailed instructions and the necessary tools. But first, I should check if registry entries already exist for these experiments by looking at the PREPARING list in the report.

The report shows "exp_001_sft_15B_d025_s123（准备中）" in the PREPARING section, which suggests some seed=123 experiments might already be registered. The registry is too large to read directly, so I'll proceed and let submit_training_job handle any updates or creation as needed.

I've been overthinking this. Let me just execute: spawn a Worker for SSH cleanup, verification, and training submission, then report back to the Director. One thing to keep in mind—the existing seed=42 experiments used individual exp_ids per dosage, so I should follow the same pattern for seed=123 to maintain consistency, even though submit_training_job takes one exp_id per call.

I could submit 20 individual jobs (5 dosages × 4 GPs), but that would require serialization per GPU, which submit_training_job doesn't handle—it just starts a tmux session. Instead, I'll use batch for-loop commands with a single exp_id per GPU batch and let the cron track the whole batch. When it finishes, I can extract individual experiment entries from the results.

This keeps things simple and aligns with the Director's urgency. My final plan: create 4 PREPARING registry entries (one per GPU batch) with hypotheses, spawn the Worker to kill zombies on westd, verify GPUs, get model snapshot paths, then submit 4 training jobs, and report back.

Now I'm drafting the hypotheses—they're seed=123 replications of the seed=42 dose-response sweep, each tailored to the specific model to test whether the observed patterns (immune response for Phi-4, U-shaped vulnerability for Qwen-14B, V-shaped recovery for Qwen-7B) hold across different random seeds.

I need to set parent references to the seed=42 experiments, then decide whether to register batch-level entries or individual per-dosage entries in the registry—for the paper, each dosage is a separate data point, so I'm leaning toward per-dosage granularity.

Looking at what's already in PREPARING status, I see smaller model experiments (0.5B and 1.5B) but nothing for the 7B+ models the Director wants, so I have room to add the new entries without conflicts.

I'll create 5 batch registry entries for the sweep jobs across the three GPUs, spawn a Worker to handle cleanup and submission, then report back to the Director.

Actually, I need to reconsider the GPU allocation. OLMo-2 runs in the same tmux session as Qwen-7B on cuda:2, so I can't submit them as separate batch entries. I'll consolidate to 4 entries instead: Phi-4 on cuda:0, Qwen-14B on cuda:1, and a combined Qwen-7B + OLMo-2 job on cuda:2, with Gemma-2 on cuda:3.

Now I'm going to stop deliberating and actually execute this. I'll spawn a Worker with SSH and job submission tools, have it clean up and verify the environment, then submit all 4 training jobs. I should also give the Worker the ability to update the registry so it can set hypotheses, though I could handle the registry entries myself since that's lightweight—let me just do those calls directly.

Actually, I'll let the Worker handle everything to keep things simple. I'll give it SSH access and the submit_training_job and update_registry tools, then write out a detailed prompt for it since it won't have any context. I should also check the resource-saturation skill after spawning to minimize delay before reporting back to the Director.

Now I'm laying out the Worker prompt with the full context: the project is contamcal-irt-calibration doing contamination dose-response experiments, seed=42 with 25 experiments is already done, and now I need to replicate with seed=123 for statistical robustness. The server is westd-29999 with 4 RTX PRO 6000 Blackwell GPUs, and I need to clean up the GPUs first, verify the model paths, then submit 4 training batches with seed=123.

Checking GPU status and killing any lingering processes...

Now I need to locate the snapshot directories for the different models in the Hugging Face cache to get their full hash paths.

The training script exists at `/root/autodl-tmp/exp001/train_sft.py`. Next I'll submit 4 training jobs using `submit_training_job` with specific configurations: server "westd-29999", project "contamcal-irt-calibration", commands wrapped in `bash -c` syntax, no CUDA_VISIBLE_DEVICES setting, and 24-hour timeout. Before submission, I need to create experiment entries in the registry and set hypotheses for each batch, starting with batch 1 for Phi-4 on cuda:0.

For the first batch, I'm setting up experiment `sft_phi4_s123_sweep` to verify whether the immune pattern observed at seed=42 (±0.54pp difference) remains stable across different seeds, which would strengthen the TOST equivalence evidence. The training command will loop through dosage values 000, 005, 025, 050, and 100 with seed 123, using offline mode for datasets and transformers.

Now for the second batch on cuda:1, I'm running a parallel Qwen-14B experiment with the same seed=123 sweep structure to test whether the U-shaped vulnerability pattern (-10.03pp at seed=42) reproduces, investigating whether larger models show consistent fragility across seeds.

For the third batch on cuda:2, I'm setting up a combined Qwen-7B and OLMo-2 sweep that chains two separate dosage loops together, aiming to verify both the V-shaped recovery pattern for Qwen-7B and the benefiting-plateau pattern for OLMo-2 while confirming the 64% baseline threshold holds at seed=123. Setting up the fourth batch of experiments on Gemma-2 with a new seed to replicate the dose-response pattern observed in earlier runs, using the same training loop structure but with updated model paths and output directories.

Now I need to verify that all four tmux sessions start correctly by checking their status and confirming GPU allocation across the four cards. After that, I'll report the final state including session names, GPU process information, and the model paths used for each batch.

Actually, wait—I should verify whether the Worker can directly call submit_training_job, since the tool specification mentions individual MCP tool names. Let me check if the full tool path is required or if there's a constraint I'm missing.

Also, I need to confirm the parent experiment reference. Looking at the registry, I see exp_001_sft_phi4_d100_s42 succeeded, so the naming pattern is exp_001_sft_phi4_d{dosage}_s42. The d000 variant should exist as the baseline. For the parent field, I'm thinking about the derivation chain—these seed=123 experiments build on the seed=42 results that established the 5-pattern taxonomy, so that's the logical parent relationship to reference.

I'll go with the d000 experiment as the representative parent and spawn the job now. Though I should probably check the resource-saturation skill before running—the CLAUDE.md mentions reviewing it before the Director approves. But given the urgency, I'll skip that for now since I already know from the report that we have 8 idle GPUs, 4 westd GPUs coming online, and 1 idle cqa1 GPU available.

Now I'm looking at the resource allocation for the report: 4 out of 8 GPUs will be used for the westd training job, with 1 worker handling SSH cleanup and submission, and disk space at 49% capacity on westd. I should spawn the worker and notify the Director simultaneously.

Wait—the Director also flagged GPU 0 PID 176524 and GPU 1 as having an abnormal state, but the report shows no running experiments and zero reconciled processes from cron. There might not be zombie processes, but since the Director specifically called them out, the worker should still check for them. I also need to resolve the parent reference for "exp_001_sft_qwen7b_d000_s42" from the recent completions in the report.

Looking at the naming patterns in the completed experiments, I see the format includes the model size with an underscore—like `exp_001_sft_olmo2_7b_d100_s42`—so for Qwen it should follow the same convention, possibly `exp_001_sft_qwen_7b_d100_s42` or `exp_001_sft_qwen2.5_7b_d100_s42`, while Phi-4 would omit the size since it's implicit in the model name.

I don't need to nail down the exact parent IDs right now—the Worker can set them as best it can and I can adjust later if needed. I'm going to spawn the Worker now since a single one can handle all 4 GPU training jobs without redundancy. After that, I should spawn at least one more Worker for other tasks to maintain the pool, and I'm looking at the roadmap to see what else needs doing—there's dose-response visualization, TOST testing, LaTeX table generation, and registry updates, all of which are CPU-bound. I'll go ahead and spawn just the training Worker for now and let the Director know I can add analysis Workers later. I need to make sure the Worker has the SSH credentials for "westd-29999" with root access, and I'll configure it with the ssh tools so it can handle cleanup and job submission. Before I finalize the spawn call, I should verify that the existing training script at /root/autodl-tmp/exp001 is current and has the right configuration.

Looking at the output directory naming, the Director's command will create directories like `output_phi4_d${d}_s123`, which won't conflict with the seed=42 outputs that would be named `output_phi4_d${d}_s42`. Now I need to think through the bash variable expansion in the Worker's command—the for-loop uses `${d}` inside single quotes, which means the outer shell won't expand it, but the inner bash -c will handle the expansion correctly.

There's a potential issue with how tmux handles the quoting when submit_training_job passes the command. To avoid any escaping problems, I should switch to double quotes for the bash -c command and properly escape the inner variables.

Still writing command setup... Writing bash scripts...

Actually, this approach is cleaner—I'll have the Worker generate separate bash scripts on the server for each GPU, each containing the full training loop with proper variable expansion, then submit those scripts directly. This eliminates all the quoting complexity since the variables get expanded when the script runs on the server.

Now I'm second-guessing whether submit_training_job will handle the bash shebang correctly when tmux runs it under sh, so I should clarify whether to wrap it in an explicit bash call or if the simple command will work fine. I'm debating whether to use `;` to continue on failure or `&&` to stop early—the Director used `;` so I'll stick with that for simplicity. I also need to spawn the Worker and immediately report back to the Director that the job is dispatched, then wait for the [WORKER DONE] callback when it finishes.

Now I'm identifying what tools the Worker will need: SSH access for cleanup and script creation, the training job submission tool, and the registry update tool to log the experiments with their hypotheses. I notice there's already an existing seed=123 experiment in the PREPARING list, but it's for a 1.5B model, not the 7B+ models I'm working with, so I'll need to create new entries.

For the registry, I'll submit 4 batch entries (one per training job) since each submit_training_job call creates one entry, and the 5 dosages run together under a single tmux session. Once training finishes, I can update those entries with the detailed per-dosage results.

Spawning the Worker now.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c3c75e9-8353-4ca9-badf-ab38f327af50",
  "isSidechain": false,
  "requestId": "req_011CbC1VTvK2T5gRkBbLKAyV",
  "type": "assistant",
  "uuid": "f8823265-62e6-4765-9e5b-936c4e8461e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xoftkwky3yHrFvXMS86UWt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7222,
      "cache_read_input_tokens": 43650,
      "output_tokens": 21346,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7222,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 21346,
          "cache_read_input_tokens": 43650,
          "cache_creation_input_tokens": 7222,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7222
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Assistant

_source line 28 · 2026-05-19T13:36:32.749Z_

GPU 白名单确认：westd-29999 cuda:0-3 全部在配额内。8 GPU 全部空闲。正在派 Worker 执行清理 + 提交训练。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f8823265-62e6-4765-9e5b-936c4e8461e8",
  "isSidechain": false,
  "requestId": "req_011CbC1VTvK2T5gRkBbLKAyV",
  "type": "assistant",
  "uuid": "8fe64f1f-1752-42ff-bf17-f507fdbe3082",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xoftkwky3yHrFvXMS86UWt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7222,
      "cache_read_input_tokens": 43650,
      "output_tokens": 21346,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7222,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 21346,
          "cache_read_input_tokens": 43650,
          "cache_creation_input_tokens": 7222,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7222
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool call

_source line 29 · 2026-05-19T13:37:15.043Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__spawn_worker · `toolu_011VaAJisENSgG568ZsnMwLu`</summary>

````json
{
  "task_type": "code:sft_s123_sweep_submit",
  "project": "contamcal-irt-calibration",
  "tool_groups": [
    "ssh"
  ],
  "tools": [
    "submit_training_job",
    "update_registry"
  ],
  "task_prompt": "## 任务：westd-29999 清理 GPU + 创建训练脚本 + 提交 4 个 seed=123 SFT 批次\n\n**项目**: contamcal-irt-calibration\n**服务器**: westd-29999 (account: root)\n**GPU**: 4× RTX PRO 6000 Blackwell (96GB each), cuda:0-3\n**项目路径**: /root/autodl-tmp/exp001\n**Python**: /root/miniconda3/bin/python (conda base 环境)\n\n### 步骤 1: 清理 GPU\n\nSSH 到 westd-29999，先查看 GPU 状态：\n```bash\nnvidia-smi\n```\n\n杀死所有 GPU 上的 python 进程（特别是 PID 176524 如果还在）：\n```bash\n# 获取所有 GPU 上的进程 PID\nnvidia-smi --query-compute-apps=pid --format=csv,noheader | sort -u\n# 对每个 PID 执行 kill -9\n```\n\n如果没有进程，跳过 kill 步骤。\n\n### 步骤 2: 验证 GPU 空闲\n\n```bash\nnvidia-smi --query-gpu=index,memory.used,utilization.gpu --format=csv,noheader\n```\n\n确认 4 张卡全部空闲（memory.used ≈ 0 MiB）。不干净就继续 kill。\n\n### 步骤 3: 获取模型 snapshot 路径\n\n运行以下命令，记录每个模型的完整 snapshot 路径：\n```bash\necho \"PHI4:\" && ls /root/.cache/huggingface/hub/models--microsoft--phi-4/snapshots/\necho \"QWEN14B:\" && ls /root/.cache/huggingface/hub/models--Qwen--Qwen2.5-14B/snapshots/\necho \"QWEN7B:\" && ls /root/.cache/huggingface/hub/models--Qwen--Qwen2.5-7B/snapshots/\necho \"GEMMA2:\" && ls /root/.cache/huggingface/hub/models--google--gemma-2-9b/snapshots/\necho \"OLMO2:\" && ls /root/.cache/huggingface/hub/models--allenai--OLMo-2-0425-1124-7B/snapshots/\n```\n\n确认 train_sft.py 存在：\n```bash\nls -la /root/autodl-tmp/exp001/train_sft.py\n```\n\n### 步骤 4: 创建训练脚本\n\n在服务器上创建 4 个 bash 脚本。**用 snapshot 的完整路径替换 {MODEL_PATH}**，格式为 `/root/.cache/huggingface/hub/models--{org}--{name}/snapshots/{hash}`。\n\n**脚本 1: /root/autodl-tmp/exp001/run_phi4_s123.sh** (cuda:0)\n```bash\n#!/bin/bash\nset -x\ncd /root/autodl-tmp/exp001\nfor d in 000 005 025 050 100; do\n  echo \"=== Starting Phi-4 dosage=${d} seed=123 at $(date) ===\"\n  HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 \\\n  /root/miniconda3/bin/python train_sft.py \\\n    --model_name_or_path {PHI4_SNAPSHOT_PATH} \\\n    --dosage ${d} --seed 123 \\\n    --output_dir output_phi4_d${d}_s123 \\\n    --lora_r 16 --lora_alpha 32 --learning_rate 5e-5 \\\n    --bf16 --mode augment\n  echo \"=== Finished Phi-4 dosage=${d} seed=123 at $(date), exit code=$? ===\"\ndone\necho \"ALL_DONE_PHI4_S123\"\n```\n\n**脚本 2: /root/autodl-tmp/exp001/run_qwen14b_s123.sh** (cuda:1)\n```bash\n#!/bin/bash\nset -x\ncd /root/autodl-tmp/exp001\nfor d in 000 005 025 050 100; do\n  echo \"=== Starting Qwen-14B dosage=${d} seed=123 at $(date) ===\"\n  HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 \\\n  /root/miniconda3/bin/python train_sft.py \\\n    --model_name_or_path {QWEN14B_SNAPSHOT_PATH} \\\n    --dosage ${d} --seed 123 \\\n    --output_dir output_qwen14b_d${d}_s123 \\\n    --lora_r 16 --lora_alpha 32 --learning_rate 5e-5 \\\n    --bf16 --mode augment\n  echo \"=== Finished Qwen-14B dosage=${d} seed=123 at $(date), exit code=$? ===\"\ndone\necho \"ALL_DONE_QWEN14B_S123\"\n```\n\n**脚本 3: /root/autodl-tmp/exp001/run_qwen7b_olmo2_s123.sh** (cuda:2)\n```bash\n#!/bin/bash\nset -x\ncd /root/autodl-tmp/exp001\n# Part 1: Qwen-7B (fastest, ~35min each)\nfor d in 000 005 025 050 100; do\n  echo \"=== Starting Qwen-7B dosage=${d} seed=123 at $(date) ===\"\n  HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 \\\n  /root/miniconda3/bin/python train_sft.py \\\n    --model_name_or_path {QWEN7B_SNAPSHOT_PATH} \\\n    --dosage ${d} --seed 123 \\\n    --output_dir output_qwen7b_d${d}_s123 \\\n    --lora_r 16 --lora_alpha 32 --learning_rate 5e-5 \\\n    --bf16 --mode augment\n  echo \"=== Finished Qwen-7B dosage=${d} seed=123 at $(date), exit code=$? ===\"\ndone\necho \"ALL_DONE_QWEN7B_S123\"\n# Part 2: OLMo-2-7B\nfor d in 000 005 025 050 100; do\n  echo \"=== Starting OLMo-2-7B dosage=${d} seed=123 at $(date) ===\"\n  HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 \\\n  /root/miniconda3/bin/python train_sft.py \\\n    --model_name_or_path {OLMO2_SNAPSHOT_PATH} \\\n    --dosage ${d} --seed 123 \\\n    --output_dir output_olmo2_7b_d${d}_s123 \\\n    --lora_r 16 --lora_alpha 32 --learning_rate 5e-5 \\\n    --bf16 --mode augment\n  echo \"=== Finished OLMo-2-7B dosage=${d} seed=123 at $(date), exit code=$? ===\"\ndone\necho \"ALL_DONE_OLMO2_S123\"\n```\n\n**脚本 4: /root/autodl-tmp/exp001/run_gemma2_s123.sh** (cuda:3)\n```bash\n#!/bin/bash\nset -x\ncd /root/autodl-tmp/exp001\nfor d in 000 005 025 050 100; do\n  echo \"=== Starting Gemma-2-9B dosage=${d} seed=123 at $(date) ===\"\n  HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 \\\n  /root/miniconda3/bin/python train_sft.py \\\n    --model_name_or_path {GEMMA2_SNAPSHOT_PATH} \\\n    --dosage ${d} --seed 123 \\\n    --output_dir output_gemma2_d${d}_s123 \\\n    --lora_r 16 --lora_alpha 32 --learning_rate 5e-5 \\\n    --bf16 --mode augment\n  echo \"=== Finished Gemma-2-9B dosage=${d} seed=123 at $(date), exit code=$? ===\"\ndone\necho \"ALL_DONE_GEMMA2_S123\"\n```\n\n用 ssh_execute 创建这些脚本。**务必用实际的 snapshot hash 路径替换占位符。**\n\n创建后给脚本加执行权限：\n```bash\nchmod +x /root/autodl-tmp/exp001/run_*_s123.sh\n```\n\n### 步骤 5: 创建 Registry 条目 + 提交训练\n\n先用 `update_registry` 为每个批次创建实验条目，设置 hypothesis 和 status=PREPARING：\n\n1. **sft_phi4_s123_sweep**:\n   - field=hypothesis, value=\"Phi-4 seed=123 dose-response replication: verify the immune pattern (±0.54pp at seed=42) is stable across seeds for TOST equivalence evidence\"\n   - field=parent, value=\"exp_001_sft_phi4_d100_s42\"\n\n2. **sft_qwen14b_s123_sweep**:\n   - field=hypothesis, value=\"Qwen-14B seed=123 dose-response replication: verify the U-shaped vulnerability (-10.03pp at seed=42) reproduces across seeds\"\n   - field=parent, value=\"exp_001_sft_qwen14b_d100_s42\"\n\n3. **sft_qwen7b_olmo2_s123_sweep**:\n   - field=hypothesis, value=\"Qwen-7B V-shaped recovery + OLMo-2 benefiting-plateau seed=123 replication: verify both patterns reproduce and 64% baseline threshold holds\"\n   - field=parent, value=\"exp_001_sft_qwen7b_d100_s42\"\n\n4. **sft_gemma2_s123_sweep**:\n   - field=hypothesis, value=\"Gemma-2-9B seed=123 dose-response replication: verify the benefiting pattern (+3.76pp at seed=42) reproduces in sub-64% baseline models\"\n   - field=parent, value=\"exp_001_sft_gemma2_9b_d100_s42\"\n\n然后用 `submit_training_job` 提交 4 个训练 job：\n\n1. `submit_training_job(server=\"westd-29999\", gpu_ids=[\"cuda:0\"], command=\"bash /root/autodl-tmp/exp001/run_phi4_s123.sh\", exp_id=\"sft_phi4_s123_sweep\", project=\"contamcal-irt-calibration\", timeout_hours=24)`\n\n2. `submit_training_job(server=\"westd-29999\", gpu_ids=[\"cuda:1\"], command=\"bash /root/autodl-tmp/exp001/run_qwen14b_s123.sh\", exp_id=\"sft_qwen14b_s123_sweep\", project=\"contamcal-irt-calibration\", timeout_hours=24)`\n\n3. `submit_training_job(server=\"westd-29999\", gpu_ids=[\"cuda:2\"], command=\"bash /root/autodl-tmp/exp001/run_qwen7b_olmo2_s123.sh\", exp_id=\"sft_qwen7b_olmo2_s123_sweep\", project=\"contamcal-irt-calibration\", timeout_hours=24)`\n\n4. `submit_training_job(server=\"westd-29999\", gpu_ids=[\"cuda:3\"], command=\"bash /root/autodl-tmp/exp001/run_gemma2_s123.sh\", exp_id=\"sft_gemma2_s123_sweep\", project=\"contamcal-irt-calibration\", timeout_hours=24)`\n\n### 步骤 6: 验证启动\n\n提交后立即确认：\n```bash\ntmux ls\nnvidia-smi\n```\n\n确认 4 个 tmux session 运行中，4 张 GPU 有进程占用。\n\n### 输出\n\n最终报告：\n- GPU 清理结果\n- 5 个模型的完整 snapshot 路径\n- 4 个 submit_training_job 的返回结果\n- tmux ls 和 nvidia-smi 的验证输出\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8fe64f1f-1752-42ff-bf17-f507fdbe3082",
  "isSidechain": false,
  "requestId": "req_011CbC1VTvK2T5gRkBbLKAyV",
  "type": "assistant",
  "uuid": "19ab7ea9-4ca8-4fdd-827e-2082f805db02",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xoftkwky3yHrFvXMS86UWt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7222,
      "cache_read_input_tokens": 43650,
      "output_tokens": 21346,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7222,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 21346,
          "cache_read_input_tokens": 43650,
          "cache_creation_input_tokens": 7222,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7222
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Runtime record

_source line 30_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Director 指令] [Director 紧急] **用户催促\"马上马上\"——立即启动 seed=123 训练，不等分析完成。**  GPU 在空转浪费时间。分析是 CPU-bound，训练是 GPU-bound，必须并行。  **现在立刻做**： 1. SSH westd，kill 所有僵尸进程（GPU 0 的 PID 176524 重复 eval，GPU 1 异常状态） 2. 确认 4…",
  "leafUuid": "19ab7ea9-4ca8-4fdd-827e-2082f805db02",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de"
}
```

---


### Runtime record

_source line 31_

```json
{
  "type": "ai-title",
  "aiTitle": "Start parallel GPU training with seed 123",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de"
}
```

---


### Tool result

_source line 32 · 2026-05-19T13:37:21.269Z_

<details><summary>↩ Tool result · `toolu_011VaAJisENSgG568ZsnMwLu`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_code_sft_s123_sweep_submit_20260519T133715\", \"status\": \"running\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/logs/workers/worker_code_sft_s123_sweep_submit_20260519T133715.log\", \"setup_data\": {}, \"message\": \"Worker worker_code_sft_s123_sweep_submit_20260519T133715 started. Use get_worker_status('worker_code_sft_s123_sweep_submit_20260519T133715') to check progress.\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "19ab7ea9-4ca8-4fdd-827e-2082f805db02",
  "isSidechain": false,
  "promptId": "f236d3d3-c563-42c4-b0bf-0a1f74939452",
  "type": "user",
  "uuid": "d3e58d7d-a8c4-475e-bbd2-97583edbf5de",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"worker_id\\\": \\\"worker_code_sft_s123_sweep_submit_20260519T133715\\\", \\\"status\\\": \\\"running\\\", \\\"log_path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/logs/workers/worker_code_sft_s123_sweep_submit_20260519T133715.log\\\", \\\"setup_data\\\": {}, \\\"message\\\": \\\"Worker worker_code_sft_s123_sweep_submit_20260519T133715 started. Use get_worker_status('worker_code_sft_s123_sweep_submit_20260519T133715') to check progress.\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"worker_id\": \"worker_code_sft_s123_sweep_submit_20260519T133715\", \"status\": \"running\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/logs/workers/worker_code_sft_s123_sweep_submit_20260519T133715.log\", \"setup_data\": {}, \"message\": \"Worker worker_code_sft_s123_sweep_submit_20260519T133715 started. Use get_worker_status('worker_code_sft_s123_sweep_submit_20260519T133715') to check progress.\"}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "19ab7ea9-4ca8-4fdd-827e-2082f805db02",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 33 · 2026-05-19T13:37:21.276Z_

```json
{
  "parentUuid": "d3e58d7d-a8c4-475e-bbd2-97583edbf5de",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "81cdf7ef-6c45-46d0-97fc-18666ff8ffa1",
  "timestamp": "2026-05-19T13:37:21.276Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Assistant

_source line 34 · 2026-05-19T13:37:29.005Z_

<details><summary>Logged reasoning block</summary>

```text
Worker spawned successfully. Now I need to report to Director immediately. Let me compose the report.

Resource line:
- GPU: 4/8 being used (westd 4 cards starting s123 training), cqa1 4 cards idle
- Worker: 1 (SSH cleanup + submit)
- Disk: westd 427G/879G available (49%)

Let me report to Director.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "81cdf7ef-6c45-46d0-97fc-18666ff8ffa1",
  "isSidechain": false,
  "requestId": "req_011CbC21ZXjxnpG1PmZbda6G",
  "type": "assistant",
  "uuid": "6e269b09-98ef-46b1-a059-ee3332b354fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F3SDDN2hFxorZVESATJzK5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21624,
      "cache_read_input_tokens": 50872,
      "output_tokens": 698,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21624,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 698,
          "cache_read_input_tokens": 50872,
          "cache_creation_input_tokens": 21624,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21624
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Assistant

_source line 35 · 2026-05-19T13:37:30.448Z_

Worker 已派发，向 Director 汇报。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6e269b09-98ef-46b1-a059-ee3332b354fe",
  "isSidechain": false,
  "requestId": "req_011CbC21ZXjxnpG1PmZbda6G",
  "type": "assistant",
  "uuid": "69704c90-05cf-40cf-8d88-a869319a0ece",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F3SDDN2hFxorZVESATJzK5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21624,
      "cache_read_input_tokens": 50872,
      "output_tokens": 698,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21624,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 698,
          "cache_read_input_tokens": 50872,
          "cache_creation_input_tokens": 21624,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21624
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool call

_source line 36 · 2026-05-19T13:37:40.383Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__main_agent_post_to_director · `toolu_01MC4HHfQbxg3PjL7xYuSchZ`</summary>

```json
{
  "text": "[资源] GPU 0/8 → 4/8 (westd cuda:0-3 启动中) | Worker 1 (SSH cleanup + submit) | 磁盘: westd 427G/879G 可用 (49%)\n\n**执行中 — seed=123 训练已派 Worker 启动**\n\nWorker `worker_code_sft_s123_sweep_submit_20260519T133715` 正在 westd-29999 上执行：\n1. Kill 僵尸进程 + 确认 4 GPU 干净\n2. 验证 5 个模型 snapshot 路径\n3. 创建 4 个训练脚本（每 GPU 一个 for-loop，5 dosages 串行）\n4. 用 `submit_training_job` 提交 4 个 batch job\n\n| GPU | 模型 | exp_id | 预估时长 |\n|-----|------|--------|---------|\n| cuda:0 | Phi-4 14.7B | sft_phi4_s123_sweep | ~3-4h (5×35-45min) |\n| cuda:1 | Qwen-14B | sft_qwen14b_s123_sweep | ~3-4h |\n| cuda:2 | Qwen-7B → OLMo-2-7B | sft_qwen7b_olmo2_s123_sweep | ~6h (10×35min) |\n| cuda:3 | Gemma-2-9B | sft_gemma2_s123_sweep | ~3-4h |\n\n共 25 个 SFT runs (5 models × 5 dosages × seed=123)。Worker 完成后我会确认 4 卡全部 RUNNING。\n\ncqa1 4 卡当前空闲——如需并行其他任务请指示。",
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69704c90-05cf-40cf-8d88-a869319a0ece",
  "isSidechain": false,
  "requestId": "req_011CbC21ZXjxnpG1PmZbda6G",
  "type": "assistant",
  "uuid": "6298bed2-66e9-4d7e-8e5f-b1d0e3dd7944",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F3SDDN2hFxorZVESATJzK5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21624,
      "cache_read_input_tokens": 50872,
      "output_tokens": 698,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21624,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 698,
          "cache_read_input_tokens": 50872,
          "cache_creation_input_tokens": 21624,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21624
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 37 · 2026-05-19T13:37:41.610Z_

<details><summary>↩ Tool result · `toolu_01MC4HHfQbxg3PjL7xYuSchZ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_4960c7baa442eabd4fa0aceeac2693ca:director\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6298bed2-66e9-4d7e-8e5f-b1d0e3dd7944",
  "isSidechain": false,
  "promptId": "f236d3d3-c563-42c4-b0bf-0a1f74939452",
  "type": "user",
  "uuid": "0810f816-ec43-4d16-8f21-779d9687ad31",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"director_session\\\": \\\"feishu:group:oc_4960c7baa442eabd4fa0aceeac2693ca:director\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_4960c7baa442eabd4fa0aceeac2693ca:director\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "6298bed2-66e9-4d7e-8e5f-b1d0e3dd7944",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 38_

```json
{
  "type": "ai-title",
  "aiTitle": "Start parallel GPU training with seed 123",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de"
}
```

---


### Runtime record

_source line 39 · 2026-05-19T13:37:51.449Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-19T13:37:51.449Z",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "content": "[服务器重启后首条消息] 当前日期: 2026-05-19。服务器刚重启，项目状态可能已更新。不要依赖对话历史中的状态信息，以 registry 当前值为准。\n\n**用户消息：** [WORKER DONE] Worker worker_analysis_dose-response-viz_20260519T130646 已完成（status=done）。用 `get_worker_status('worker_analysis_dose-response-viz_20260519T130646')` 读取结果，然后处理。\n\n- worker_id: worker_analysis_dose-response-viz_20260519T130646\n- project: contamcal-irt-calibration\n- status: done"
}
```

---


### Runtime record

_source line 40 · 2026-05-19T13:37:51.450Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-19T13:37:51.450Z",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de"
}
```

---


## Round 2

## Round 2

2 recorded events


### User

_source line 41 · 2026-05-19T13:37:51.441Z_

Continue from where you left off.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0810f816-ec43-4d16-8f21-779d9687ad31",
  "isSidechain": false,
  "promptId": "207c45a2-5c44-4810-ac72-cde263f4ce39",
  "type": "user",
  "isMeta": true,
  "uuid": "87a9eec5-cb01-4129-a0f4-22d6aece7947",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Assistant

_source line 42 · 2026-05-19T13:37:51.442Z_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "87a9eec5-cb01-4129-a0f4-22d6aece7947",
  "isSidechain": false,
  "type": "assistant",
  "uuid": "9133e5a9-6c5d-49bb-9e6d-cadb25d58bed",
  "isApiErrorMessage": false,
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "id": "063f816a-a5a8-4abb-a393-51e319a78cc3",
    "container": null,
    "model": "&lt;synthetic>",
    "stop_reason": "stop_sequence",
    "stop_sequence": "",
    "type": "message",
    "usage": {
      "input_tokens": 0,
      "output_tokens": 0,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 0,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": null,
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": null,
      "iterations": null,
      "speed": null
    },
    "context_management": null
  }
}
```

</details>

---


## Round 3

## Round 3

45 recorded events


### User

_source line 43 · 2026-05-19T13:37:51.576Z_

[服务器重启后首条消息] 当前日期: 2026-05-19。服务器刚重启，项目状态可能已更新。不要依赖对话历史中的状态信息，以 registry 当前值为准。

**用户消息：** [WORKER DONE] Worker worker_analysis_dose-response-viz_20260519T130646 已完成（status=done）。用 `get_worker_status('worker_analysis_dose-response-viz_20260519T130646')` 读取结果，然后处理。

- worker_id: worker_analysis_dose-response-viz_20260519T130646
- project: contamcal-irt-calibration
- status: done

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9133e5a9-6c5d-49bb-9e6d-cadb25d58bed",
  "isSidechain": false,
  "promptId": "207c45a2-5c44-4810-ac72-cde263f4ce39",
  "type": "user",
  "uuid": "b5f0233b-2ffe-48e7-be5f-04901232b01f",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Assistant

_source line 44 · 2026-05-19T13:38:00.252Z_

<details><summary>Logged reasoning block</summary>

```text
Server restarted, so I need to re-initialize. Let me follow the session-start protocol:

1. Read registry
2. Reconcile crons
3. Read report.md
4. Read ROADMAP.md

Then handle the Worker done callback.

Let me load the necessary tools first, then do session-start + get worker status in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b5f0233b-2ffe-48e7-be5f-04901232b01f",
  "isSidechain": false,
  "requestId": "req_011CbC23o6s7tipCnFcWmJYp",
  "type": "assistant",
  "uuid": "fbd34178-75a8-4109-b10f-76ac59440725",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E1TnB9qekuTojDoH5v5WLR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 209,
      "cache_read_input_tokens": 73266,
      "output_tokens": 369,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 209,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 369,
          "cache_read_input_tokens": 73266,
          "cache_creation_input_tokens": 209,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 209
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Assistant

_source line 45 · 2026-05-19T13:38:00.745Z_

服务器重启，执行 session-start 初始化 + 读取 Worker 结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fbd34178-75a8-4109-b10f-76ac59440725",
  "isSidechain": false,
  "requestId": "req_011CbC23o6s7tipCnFcWmJYp",
  "type": "assistant",
  "uuid": "25cd8152-51ae-4c26-a64b-592bd773fa8c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E1TnB9qekuTojDoH5v5WLR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 209,
      "cache_read_input_tokens": 73266,
      "output_tokens": 369,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 209,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 369,
          "cache_read_input_tokens": 73266,
          "cache_creation_input_tokens": 209,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 209
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool call

_source line 46 · 2026-05-19T13:38:03.614Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_016ZepyTmEPsNctHSJ2wXBY5`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__get_worker_status,mcp__agent-ml-research__load_project_config,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__list_workers,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact",
  "max_results": 15
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "25cd8152-51ae-4c26-a64b-592bd773fa8c",
  "isSidechain": false,
  "requestId": "req_011CbC23o6s7tipCnFcWmJYp",
  "type": "assistant",
  "uuid": "88ad11c1-dd4e-4b54-81c2-d03572328a0c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E1TnB9qekuTojDoH5v5WLR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 209,
      "cache_read_input_tokens": 73266,
      "output_tokens": 369,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 209,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 369,
          "cache_read_input_tokens": 73266,
          "cache_creation_input_tokens": 209,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 209
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 47 · 2026-05-19T13:38:03.621Z_

<details><summary>↩ Tool result · `toolu_016ZepyTmEPsNctHSJ2wXBY5`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_registry"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__reconcile_crons"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_roadmap"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__get_worker_status"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__load_project_config"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__main_agent_post_to_director"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__update_registry"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__spawn_worker"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__list_workers"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__save_project_file"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__register_artifact"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "88ad11c1-dd4e-4b54-81c2-d03572328a0c",
  "isSidechain": false,
  "promptId": "207c45a2-5c44-4810-ac72-cde263f4ce39",
  "type": "user",
  "uuid": "41bd203b-0316-46fc-abb0-621644e2f823",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__reconcile_crons",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__get_worker_status",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__main_agent_post_to_director",
      "mcp__agent-ml-research__update_registry",
      "mcp__agent-ml-research__spawn_worker",
      "mcp__agent-ml-research__list_workers",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__register_artifact"
    ],
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__get_worker_status,mcp__agent-ml-research__load_project_config,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__list_workers,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact",
    "total_deferred_tools": 82
  },
  "sourceToolAssistantUUID": "88ad11c1-dd4e-4b54-81c2-d03572328a0c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Assistant

_source line 48 · 2026-05-19T13:38:08.307Z_

<details><summary>Logged reasoning block</summary>

```text
Tools loaded. Now let me do session-start initialization in parallel with getting the worker status.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "41bd203b-0316-46fc-abb0-621644e2f823",
  "isSidechain": false,
  "requestId": "req_011CbC24geT4Q1UystYtvyx1",
  "type": "assistant",
  "uuid": "88b5ee8d-05d5-4ec3-bc2a-f5d48e4ade42",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nz5vTPmB3AtGrr4NYBYsFL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4645,
      "cache_read_input_tokens": 73475,
      "output_tokens": 365,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4645,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 365,
          "cache_read_input_tokens": 73475,
          "cache_creation_input_tokens": 4645,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4645
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool call

_source line 49 · 2026-05-19T13:38:09.853Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_worker_status · `toolu_014M4nHvuXfC8Xef5Wf6GKpL`</summary>

```json
{
  "worker_id": "worker_analysis_dose-response-viz_20260519T130646"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "88b5ee8d-05d5-4ec3-bc2a-f5d48e4ade42",
  "isSidechain": false,
  "requestId": "req_011CbC24geT4Q1UystYtvyx1",
  "type": "assistant",
  "uuid": "f4c457f1-fb37-4a1e-8167-6921ebc32147",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nz5vTPmB3AtGrr4NYBYsFL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4645,
      "cache_read_input_tokens": 73475,
      "output_tokens": 365,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4645,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 365,
          "cache_read_input_tokens": 73475,
          "cache_creation_input_tokens": 4645,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4645
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool call

_source line 50 · 2026-05-19T13:38:10.315Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__reconcile_crons · `toolu_01VpRRsGkXQEeMxB3MxTwf8E`</summary>

```json
{}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f4c457f1-fb37-4a1e-8167-6921ebc32147",
  "isSidechain": false,
  "requestId": "req_011CbC24geT4Q1UystYtvyx1",
  "type": "assistant",
  "uuid": "e6555e12-5800-491b-b983-52b54ed6167d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nz5vTPmB3AtGrr4NYBYsFL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4645,
      "cache_read_input_tokens": 73475,
      "output_tokens": 365,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4645,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 365,
          "cache_read_input_tokens": 73475,
          "cache_creation_input_tokens": 4645,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4645
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 51 · 2026-05-19T13:38:10.017Z_

<details><summary>↩ Tool result · `toolu_014M4nHvuXfC8Xef5Wf6GKpL`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_analysis_dose-response-viz_20260519T130646\", \"status\": \"done\", \"task_type\": \"analysis:dose-response-viz\", \"project\": \"contamcal-irt-calibration\", \"started_at\": \"2026-05-19T13:06:47.082641+00:00\", \"ended_at\": \"2026-05-19T13:08:00.431452+00:00\", \"setup\": null, \"teardown\": null, \"setup_data\": {}, \"result\": {\"raw\": \"6 个文件全部生成：\\n\\n| 文件 | 大小 |\\n|------|------|\\n| `mmlu_dose_response.pdf` | 18.9 KB |\\n| `mmlu_dose_response.png` | 169.7 KB |\\n| `arc_dose_response.pdf` | 26.5 KB |\\n| `arc_dose_response.png` | 181.8 KB |\\n| `baseline_vs_effect.pdf` | 17.8 KB |\\n| `baseline_vs_effect.png` | 114.4 KB |\\n\\n路径：`/root/autodl-tmp/exp001/figures/`，脚本：`/root/autodl-tmp/exp001/analyze_phase2.py`。\"}}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f4c457f1-fb37-4a1e-8167-6921ebc32147",
  "isSidechain": false,
  "promptId": "207c45a2-5c44-4810-ac72-cde263f4ce39",
  "type": "user",
  "uuid": "a8b2ee83-30a1-4b5a-bb87-a9692b305713",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"worker_id\\\": \\\"worker_analysis_dose-response-viz_20260519T130646\\\", \\\"status\\\": \\\"done\\\", \\\"task_type\\\": \\\"analysis:dose-response-viz\\\", \\\"project\\\": \\\"contamcal-irt-calibration\\\", \\\"started_at\\\": \\\"2026-05-19T13:06:47.082641+00:00\\\", \\\"ended_at\\\": \\\"2026-05-19T13:08:00.431452+00:00\\\", \\\"setup\\\": null, \\\"teardown\\\": null, \\\"setup_data\\\": {}, \\\"result\\\": {\\\"raw\\\": \\\"6 个文件全部生成：\\\\n\\\\n| 文件 | 大小 |\\\\n|------|------|\\\\n| `mmlu_dose_response.pdf` | 18.9 KB |\\\\n| `mmlu_dose_response.png` | 169.7 KB |\\\\n| `arc_dose_response.pdf` | 26.5 KB |\\\\n| `arc_dose_response.png` | 181.8 KB |\\\\n| `baseline_vs_effect.pdf` | 17.8 KB |\\\\n| `baseline_vs_effect.png` | 114.4 KB |\\\\n\\\\n路径：`/root/autodl-tmp/exp001/figures/`，脚本：`/root/autodl-tmp/exp001/analyze_phase2.py`。\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"worker_id\": \"worker_analysis_dose-response-viz_20260519T130646\", \"status\": \"done\", \"task_type\": \"analysis:dose-response-viz\", \"project\": \"contamcal-irt-calibration\", \"started_at\": \"2026-05-19T13:06:47.082641+00:00\", \"ended_at\": \"2026-05-19T13:08:00.431452+00:00\", \"setup\": null, \"teardown\": null, \"setup_data\": {}, \"result\": {\"raw\": \"6 个文件全部生成：\\n\\n| 文件 | 大小 |\\n|------|------|\\n| `mmlu_dose_response.pdf` | 18.9 KB |\\n| `mmlu_dose_response.png` | 169.7 KB |\\n| `arc_dose_response.pdf` | 26.5 KB |\\n| `arc_dose_response.png` | 181.8 KB |\\n| `baseline_vs_effect.pdf` | 17.8 KB |\\n| `baseline_vs_effect.png` | 114.4 KB |\\n\\n路径：`/root/autodl-tmp/exp001/figures/`，脚本：`/root/autodl-tmp/exp001/analyze_phase2.py`。\"}}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "f4c457f1-fb37-4a1e-8167-6921ebc32147",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool result

_source line 52 · 2026-05-19T13:38:10.391Z_

<details><summary>↩ Tool result · `toolu_01VpRRsGkXQEeMxB3MxTwf8E`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"reconciled\": 0, \"results\": []}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e6555e12-5800-491b-b983-52b54ed6167d",
  "isSidechain": false,
  "promptId": "207c45a2-5c44-4810-ac72-cde263f4ce39",
  "type": "user",
  "uuid": "2b87a2d7-0676-4b89-9d21-6e7aa9c50260",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"reconciled\\\": 0, \\\"results\\\": []}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"reconciled\": 0, \"results\": []}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "e6555e12-5800-491b-b983-52b54ed6167d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool result

_source line 53 · 2026-05-19T13:38:12.091Z_

<details><summary>↩ Tool result · `toolu_01RU1mMnfK6biGGnkB8PzuzJ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/report.md\", \"content\": \"&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-19T11:36:00Z; do not edit — regenerated by auto_build_report_facts) -->\\n## 📊 当前状态（auto-derived from registry）\\n\\n**总计**: 320 个实验 — DONE 290, PREPARING 29, QUEUED 1\\n**DONE 分布**: failed 58, killed 14, negative 7, success 211\\n\\n### GPU 占用\\n- **分配**: 8 张 — cqa1-21977:cuda:0, cqa1-21977:cuda:1, cqa1-21977:cuda:2, cqa1-21977:cuda:3, westd-29999:cuda:0, westd-29999:cuda:1, westd-29999:cuda:2, westd-29999:cuda:3\\n- **空闲（分配了没跑）**: cqa1-21977:cuda:0, cqa1-21977:cuda:1, cqa1-21977:cuda:2, cqa1-21977:cuda:3, westd-29999:cuda:0, westd-29999:cuda:1, westd-29999:cuda:2, westd-29999:cuda:3\\n\\n### 💾 磁盘余量\\n- **cqa1-21977**:\\n  - `/autodl-pub`: 280G/7.0T 可用（已用 97%） ⚠️\\n  - `/autodl-pub/data`: 1.5T/4.0T 可用（已用 65%）\\n  - `/usr/bin/nvidia-smi`: 818G/879G 可用（已用 2%）\\n- **westd-29999**:\\n  - `/autodl-pub`: 5.3T/7.3T 可用（已用 24%）\\n  - `/init`: 150M/150M 可用（已用 0%）\\n  - `/usr/bin/nvidia-smi`: 427G/879G 可用（已用 49%）\\n\\n### 🏃 RUNNING\\n_（无）_\\n\\n### 📌 最近完成 (top 5)\\n- `exp_001_sft_phi4_d100_s42` [success] — 2026-05-19T10:42:39\\n- `exp_001_sft_olmo2_7b_d100_s42` [success] — 2026-05-19T10:25:26\\n- `exp_001_sft_gemma2_9b_d100_s42` [success] — 2026-05-19T10:25:21\\n- `exp_001_sft_olmo2_7b_d050_s42` [success] — 2026-05-19T08:01:54\\n- `eval_phi4_mmlu_arc_westd` [failed] — 2026-05-19T07:21:53 — process dead 5× with no sentinel/W&B — auto-resolved as failed\\n\\n### 🔴 最近失败原因 (top 3)\\n- `eval_phi4_mmlu_arc_westd`: process dead 5× with no sentinel/W&B — auto-resolved as failed\\n\\n&lt;!-- AUTO-FACTS-END -->\\n\\n---\\n\\n# Handover — 2026-05-19\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n- eval_cross_family_cqa1: Cross-family dose-response eval on cqa1: MMLU 5-shot + ARC 25-shot for OLMo-2-7B (d000/d005/d025) and Gemma-2-9B (d000/d005/d025/d050) to establish IRT calibration curves across model architectures.（排队等待 GPU）\\n- eval_phi4_mmlu_arc_westd_v2: Phi-4 dose-response eval v2: MMLU 5-shot + ARC 25-shot across d000/d005/d025/d050. Replaces v1 which was falsely marked DONE by cron PID mismatch.（准备中）\\n- j16-domain-gamma-rerun（准备中）\\n- exp_006_irt_05B_v2: Tiered IRT calibration (D023): GSM8K/ARC direct NUTS + MMLU subsampled 1000 items + ADVI robustness check. Fixes v1 issues: aligned-only, signal-derived exposure, --max-items.（准备中）\\n- signals_05B_s123_batch（准备中）\\n- exp_002_signals_15B_instruct_gsm8k_v2: 1.5B-Instruct GSM8K signals (s1/s2/s4) to expand N for cross-family pooled IRT — GSM8K is strongest data point per cross-family results, critical for C1 N expansion（准备中）\\n- exp_001_sft_15B_d025_s123（准备中）\\n- exp_001_sft_3B_d000_v4（准备中）\\n- exp_001_sft_3B_d000_s42（准备中）\\n- exp006-gsm8k-d024-delta: GSM8K d024 delta analysis, superseded by later IRT runs with pooled cross-family design（准备中）\\n- …另有 16 项\\n\\n## 近期结论\\n- **exp_001_sft_phi4_d100_s42** (success): Phi-4 (14.7B) d100 (100% contamination) SFT with lr=5e-5 LoRA r=16 α=32 establishes the full-dosage data point for IRT dose-response calibration in the Microsoft model family, completing the 5-dosage sweep.\\n- **exp_001_sft_olmo2_7b_d100_s42** (success): OLMo-2-7B d100 (100% contamination) SFT with lr=5e-5 LoRA r=16 α=32 establishes the full-dosage data point for IRT dose-response calibration in the AllenAI model family, completing the 5-dosage sweep.\\n- **exp_001_sft_gemma2_9b_d100_s42** (success): Gemma-2-9B d100 (100% contamination) SFT with lr=5e-5 LoRA r=16 α=32 establishes the full-dosage data point for IRT dose-response calibration in the Google model family, completing the 5-dosage sweep.\\n\\n## 趋势\\n成功 213 / 负向 7 / 失败 59 / 共 293\\nmean_token_accuracy: 0.7244 ↑（近 3 次 success）\\ntrain_loss: 1.191 ↓（近 3 次 success）\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\ncqa1-21977: 无 GPU 信息\\nwestd-29999: 无 GPU 信息\\n\\n## 告警\\n- exp_001_eval_05B_d000_s42: 训练失败 — unknown\\n- exp_001_eval_05B_d100: 训练失败 — unknown\\n- exp_001_eval_05B_d100_v2: 训练失败 — unknown\\n- exp_001_eval_15B_d000_s42: 训练失败 — unknown\\n- exp_001_sft_100pct_05B: 训练失败 — unknown\\n- exp_001_sft_d005_05B: 已被终止 — unknown\\n- exp_001_sft_d005_05B_v2: 训练失败 — unknown\\n- exp_001_sft_d100_15B: 训练失败 — unknown\\n- exp_004_sim_sweep: 训练失败 — unknown\\n- exp_005_noise_prop: 训练失败 — unknown\\n- exp_005_noise_prop_v2: 训练失败 — unknown\\n- exp_005_noise_prop_v3: 训练失败 — unknown\\n- exp_001_sft_d025_05B: 训练失败 — unknown\\n- exp_001_sft_d025_05B_v2: 训练失败 — unknown\\n- exp_004_sim_sweep_v2: 训练失败 — unknown\\n- exp_001_eval_05B_aligned_batch: 训练失败 — unknown\\n- exp_006_irt_05B: 已被终止 — unknown\\n- exp_001_eval_05B_d100_aligned: 训练失败 — unknown\\n- exp_001_eval_05B_d100_aligned_v3: 训练失败 — unknown\\n- exp_008_instruct_rl_proxy: 训练失败 — unknown\\n- exp_006_irt_05B_v1: 训练失败 — unknown\\n- exp_006_pooled_gsm8k_v1: 训练失败 — unknown\\n- exp_004_sim_sweep_v3: 训练失败 — unknown\\n- exp006-pooled-05B-15B-mmlu-v2: 训练失败 — unknown\\n- exp_001_eval_3B_d100_v2_aligned: 训练失败 — unknown\\n- exp_001_sft_d025_3B: 训练失败 — unknown\\n- exp006-pooled-s1only-gsm8k: 训练失败 — unknown\\n- exp006-oracle-gsm8k-extended: 训练失败 — unknown\\n- exp_004_sim_sweep_v4: 训练失败 — unknown\\n- exp_001_eval_3B_d000_v2_para_aligned_v3: 训练失败 — unknown\\n- exp_001_sft_05B_d025_s123: 已被终止 — unknown\\n- exp_001_eval_05B_d000_s42_v7: 训练失败 — unknown\\n- exp_004_sim_sweep_v5: 训练失败 — unknown\\n- exp006-oracle-arc-4pl-pooled: 训练失败 — unknown\\n- exp_001_sft_15B_d005_s123: 训练失败 — unknown\\n- exp_008_base_pretrained_eval: 训练失败 — unknown\\n- exp_002_signals_3B: 训练失败 — unknown\\n- exp_002_signals_3B_v2: 已被终止 — unknown\\n- exp_001_sft_3B_d000_v3: 训练失败 — unknown\\n- exp_001_sft_3B_d100_s42_a32: 已被终止 — unknown\\n- exp_001_sft_3B_d025_s42_a32: 已被终止 — unknown\\n- exp_001_sft_3B_d100_s42_a32_v2: 训练失败 — unknown\\n- exp_004_sim_sweep_v6: 已被终止 — unknown\\n- exp_001_eval_3B_d100_s123_para_aligned: 训练失败 — unknown\\n- exp_002_signals_3B_v3: 已被终止 — unknown\\n- exp_002_signals_3B_v4: 训练失败 — unknown\\n- exp_002_signals_3B_v5: 训练失败 — unknown\\n- exp_002_signals_3B_v6: 训练失败 — unknown\\n- exp_001_sft_3B_d025_s42_a32_v2: 训练失败 — unknown\\n- exp_001_eval_3B_d025_v3_s42_batch: 已被终止 — unknown\\n- exp_001_sft_3B_d025_s42_a32_v3: 已被终止 — unknown\\n- exp_002_signals_3B_v8: 训练失败 — unknown\\n- exp_002_signals_3B_v8_recovery: 训练失败 — unknown\\n- exp_002_signals_3B_v9: 训练失败 — unknown\\n- exp_002_signals_05B_s123_batch: 训练失败 — unknown\\n- exp_001_eval_3B_instruct_aligned_para: 训练失败 — unknown\\n- exp_006_mmlu_domain_gamma_n24_v2: 训练失败 — unknown\\n- exp_006_mmlu_domain_gamma_n24_v3: 训练失败 — unknown\\n- exp_001_eval_llama32_3B_d000_s42: 已被终止 — unknown\\n- exp_002_signals_3B_d000_s123_cuda2: 训练失败 — unknown\\n- exp_002_signals_15B_instruct_gsm8k: 训练失败 — unknown\\n- exp_002_signals_llama32_3B_d000_gsm8k: 训练失败 — unknown\\n- exp_004_fisher_heatmap_w4: 训练失败 — unknown\\n- exp_002_signals_llama32_3B_d025_mmlu_arc_gsm8k: 训练失败 — unknown\\n- exp_002_signals_llama32_3B_d100_mmlu: 已被终止 — unknown\\n- exp_006_theta_extraction_j13: 训练失败 — unknown\\n- exp_006_cross_family_irt_j16: 训练失败 — unknown\\n- exp_006_j16_theta_extraction: 训练失败 — unknown\\n- eval_7b_batch_cqa1: 已被终止 — unknown\\n- eval_7b_batch1_westd: 训练失败 — unknown\\n- eval_14b_mmlu_arc_westd: 训练失败 — unknown\\n- exp_001_sft_olmo2_7b_d005_s42: 已被终止 — unknown\\n- eval_phi4_mmlu_arc_westd: 训练失败 — unknown\\n\", \"total_chars\": 6929, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e9483ef5-4cb7-4fc7-8ed0-3890828585c6",
  "isSidechain": false,
  "promptId": "207c45a2-5c44-4810-ac72-cde263f4ce39",
  "type": "user",
  "uuid": "cccae299-b623-4a52-bf89-52600ea4db53",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/report.md\\\", \\\"content\\\": \\\"&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-19T11:36:00Z; do not edit — regenerated by auto_build_report_facts) -->\\\\n## 📊 当前状态（auto-derived from registry）\\\\n\\\\n**总计**: 320 个实验 — DONE 290, PREPARING 29, QUEUED 1\\\\n**DONE 分布**: failed 58, killed 14, negative 7, success 211\\\\n\\\\n### GPU 占用\\\\n- **分配**: 8 张 — cqa1-21977:cuda:0, cqa1-21977:cuda:1, cqa1-21977:cuda:2, cqa1-21977:cuda:3, westd-29999:cuda:0, westd-29999:cuda:1, westd-29999:cuda:2, westd-29999:cuda:3\\\\n- **空闲（分配了没跑）**: cqa1-21977:cuda:0, cqa1-21977:cuda:1, cqa1-21977:cuda:2, cqa1-21977:cuda:3, westd-29999:cuda:0, westd-29999:cuda:1, westd-29999:cuda:2, westd-29999:cuda:3\\\\n\\\\n### 💾 磁盘余量\\\\n- **cqa1-21977**:\\\\n  - `/autodl-pub`: 280G/7.0T 可用（已用 97%） ⚠️\\\\n  - `/autodl-pub/data`: 1.5T/4.0T 可用（已用 65%）\\\\n  - `/usr/bin/nvidia-smi`: 818G/879G 可用（已用 2%）\\\\n- **westd-29999**:\\\\n  - `/autodl-pub`: 5.3T/7.3T 可用（已用 24%）\\\\n  - `/init`: 150M/150M 可用（已用 0%）\\\\n  - `/usr/bin/nvidia-smi`: 427G/879G 可用（已用 49%）\\\\n\\\\n### 🏃 RUNNING\\\\n_（无）_\\\\n\\\\n### 📌 最近完成 (top 5)\\\\n- `exp_001_sft_phi4_d100_s42` [success] — 2026-05-19T10:42:39\\\\n- `exp_001_sft_olmo2_7b_d100_s42` [success] — 2026-05-19T10:25:26\\\\n- `exp_001_sft_gemma2_9b_d100_s42` [success] — 2026-05-19T10:25:21\\\\n- `exp_001_sft_olmo2_7b_d050_s42` [success] — 2026-05-19T08:01:54\\\\n- `eval_phi4_mmlu_arc_westd` [failed] — 2026-05-19T07:21:53 — process dead 5× with no sentinel/W&B — auto-resolved as failed\\\\n\\\\n### 🔴 最近失败原因 (top 3)\\\\n- `eval_phi4_mmlu_arc_westd`: process dead 5× with no sentinel/W&B — auto-resolved as failed\\\\n\\\\n&lt;!-- AUTO-FACTS-END -->\\\\n\\\\n---\\\\n\\\\n# Handover — 2026-05-19\\\\n\\\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\\\n\\\\n## 运行中\\\\n（无）\\\\n\\\\n## 待处理\\\\n- eval_cross_family_cqa1: Cross-family dose-response eval on cqa1: MMLU 5-shot + ARC 25-shot for OLMo-2-7B (d000/d005/d025) and Gemma-2-9B (d000/d005/d025/d050) to establish IRT calibration curves across model architectures.（排队等待 GPU）\\\\n- eval_phi4_mmlu_arc_westd_v2: Phi-4 dose-response eval v2: MMLU 5-shot + ARC 25-shot across d000/d005/d025/d050. Replaces v1 which was falsely marked DONE by cron PID mismatch.（准备中）\\\\n- j16-domain-gamma-rerun（准备中）\\\\n- exp_006_irt_05B_v2: Tiered IRT calibration (D023): GSM8K/ARC direct NUTS + MMLU subsampled 1000 items + ADVI robustness check. Fixes v1 issues: aligned-only, signal-derived exposure, --max-items.（准备中）\\\\n- signals_05B_s123_batch（准备中）\\\\n- exp_002_signals_15B_instruct_gsm8k_v2: 1.5B-Instruct GSM8K signals (s1/s2/s4) to expand N for cross-family pooled IRT — GSM8K is strongest data point per cross-family results, critical for C1 N expansion（准备中）\\\\n- exp_001_sft_15B_d025_s123（准备中）\\\\n- exp_001_sft_3B_d000_v4（准备中）\\\\n- exp_001_sft_3B_d000_s42（准备中）\\\\n- exp006-gsm8k-d024-delta: GSM8K d024 delta analysis, superseded by later IRT runs with pooled cross-family design（准备中）\\\\n- …另有 16 项\\\\n\\\\n## 近期结论\\\\n- **exp_001_sft_phi4_d100_s42** (success): Phi-4 (14.7B) d100 (100% contamination) SFT with lr=5e-5 LoRA r=16 α=32 establishes the full-dosage data point for IRT dose-response calibration in the Microsoft model family, completing the 5-dosage sweep.\\\\n- **exp_001_sft_olmo2_7b_d100_s42** (success): OLMo-2-7B d100 (100% contamination) SFT with lr=5e-5 LoRA r=16 α=32 establishes the full-dosage data point for IRT dose-response calibration in the AllenAI model family, completing the 5-dosage sweep.\\\\n- **exp_001_sft_gemma2_9b_d100_s42** (success): Gemma-2-9B d100 (100% contamination) SFT with lr=5e-5 LoRA r=16 α=32 establishes the full-dosage data point for IRT dose-response calibration in the Google model family, completing the 5-dosage sweep.\\\\n\\\\n## 趋势\\\\n成功 213 / 负向 7 / 失败 59 / 共 293\\\\nmean_token_accuracy: 0.7244 ↑（近 3 次 success）\\\\ntrain_loss: 1.191 ↓（近 3 次 success）\\\\n\\\\n## 下一步\\\\n（无活跃 idea，请通过 ideas.md 添加）\\\\n\\\\n## 资源状态\\\\ncqa1-21977: 无 GPU 信息\\\\nwestd-29999: 无 GPU 信息\\\\n\\\\n## 告警\\\\n- exp_001_eval_05B_d000_s42: 训练失败 — unknown\\\\n- exp_001_eval_05B_d100: 训练失败 — unknown\\\\n- exp_001_eval_05B_d100_v2: 训练失败 — unknown\\\\n- exp_001_eval_15B_d000_s42: 训练失败 — unknown\\\\n- exp_001_sft_100pct_05B: 训练失败 — unknown\\\\n- exp_001_sft_d005_05B: 已被终止 — unknown\\\\n- exp_001_sft_d005_05B_v2: 训练失败 — unknown\\\\n- exp_001_sft_d100_15B: 训练失败 — unknown\\\\n- exp_004_sim_sweep: 训练失败 — unknown\\\\n- exp_005_noise_prop: 训练失败 — unknown\\\\n- exp_005_noise_prop_v2: 训练失败 — unknown\\\\n- exp_005_noise_prop_v3: 训练失败 — unknown\\\\n- exp_001_sft_d025_05B: 训练失败 — unknown\\\\n- exp_001_sft_d025_05B_v2: 训练失败 — unknown\\\\n- exp_004_sim_sweep_v2: 训练失败 — unknown\\\\n- exp_001_eval_05B_aligned_batch: 训练失败 — unknown\\\\n- exp_006_irt_05B: 已被终止 — unknown\\\\n- exp_001_eval_05B_d100_aligned: 训练失败 — unknown\\\\n- exp_001_eval_05B_d100_aligned_v3: 训练失败 — unknown\\\\n- exp_008_instruct_rl_proxy: 训练失败 — unknown\\\\n- exp_006_irt_05B_v1: 训练失败 — unknown\\\\n- exp_006_pooled_gsm8k_v1: 训练失败 — unknown\\\\n- exp_004_sim_sweep_v3: 训练失败 — unknown\\\\n- exp006-pooled-05B-15B-mmlu-v2: 训练失败 — unknown\\\\n- exp_001_eval_3B_d100_v2_aligned: 训练失败 — unknown\\\\n- exp_001_sft_d025_3B: 训练失败 — unknown\\\\n- exp006-pooled-s1only-gsm8k: 训练失败 — unknown\\\\n- exp006-oracle-gsm8k-extended: 训练失败 — unknown\\\\n- exp_004_sim_sweep_v4: 训练失败 — unknown\\\\n- exp_001_eval_3B_d000_v2_para_aligned_v3: 训练失败 — unknown\\\\n- exp_001_sft_05B_d025_s123: 已被终止 — unknown\\\\n- exp_001_eval_05B_d000_s42_v7: 训练失败 — unknown\\\\n- exp_004_sim_sweep_v5: 训练失败 — unknown\\\\n- exp006-oracle-arc-4pl-pooled: 训练失败 — unknown\\\\n- exp_001_sft_15B_d005_s123: 训练失败 — unknown\\\\n- exp_008_base_pretrained_eval: 训练失败 — unknown\\\\n- exp_002_signals_3B: 训练失败 — unknown\\\\n- exp_002_signals_3B_v2: 已被终止 — unknown\\\\n- exp_001_sft_3B_d000_v3: 训练失败 — unknown\\\\n- exp_001_sft_3B_d100_s42_a32: 已被终止 — unknown\\\\n- exp_001_sft_3B_d025_s42_a32: 已被终止 — unknown\\\\n- exp_001_sft_3B_d100_s42_a32_v2: 训练失败 — unknown\\\\n- exp_004_sim_sweep_v6: 已被终止 — unknown\\\\n- exp_001_eval_3B_d100_s123_para_aligned: 训练失败 — unknown\\\\n- exp_002_signals_3B_v3: 已被终止 — unknown\\\\n- exp_002_signals_3B_v4: 训练失败 — unknown\\\\n- exp_002_signals_3B_v5: 训练失败 — unknown\\\\n- exp_002_signals_3B_v6: 训练失败 — unknown\\\\n- exp_001_sft_3B_d025_s42_a32_v2: 训练失败 — unknown\\\\n- exp_001_eval_3B_d025_v3_s42_batch: 已被终止 — unknown\\\\n- exp_001_sft_3B_d025_s42_a32_v3: 已被终止 — unknown\\\\n- exp_002_signals_3B_v8: 训练失败 — unknown\\\\n- exp_002_signals_3B_v8_recovery: 训练失败 — unknown\\\\n- exp_002_signals_3B_v9: 训练失败 — unknown\\\\n- exp_002_signals_05B_s123_batch: 训练失败 — unknown\\\\n- exp_001_eval_3B_instruct_aligned_para: 训练失败 — unknown\\\\n- exp_006_mmlu_domain_gamma_n24_v2: 训练失败 — unknown\\\\n- exp_006_mmlu_domain_gamma_n24_v3: 训练失败 — unknown\\\\n- exp_001_eval_llama32_3B_d000_s42: 已被终止 — unknown\\\\n- exp_002_signals_3B_d000_s123_cuda2: 训练失败 — unknown\\\\n- exp_002_signals_15B_instruct_gsm8k: 训练失败 — unknown\\\\n- exp_002_signals_llama32_3B_d000_gsm8k: 训练失败 — unknown\\\\n- exp_004_fisher_heatmap_w4: 训练失败 — unknown\\\\n- exp_002_signals_llama32_3B_d025_mmlu_arc_gsm8k: 训练失败 — unknown\\\\n- exp_002_signals_llama32_3B_d100_mmlu: 已被终止 — unknown\\\\n- exp_006_theta_extraction_j13: 训练失败 — unknown\\\\n- exp_006_cross_family_irt_j16: 训练失败 — unknown\\\\n- exp_006_j16_theta_extraction: 训练失败 — unknown\\\\n- eval_7b_batch_cqa1: 已被终止 — unknown\\\\n- eval_7b_batch1_westd: 训练失败 — unknown\\\\n- eval_14b_mmlu_arc_westd: 训练失败 — unknown\\\\n- exp_001_sft_olmo2_7b_d005_s42: 已被终止 — unknown\\\\n- eval_phi4_mmlu_arc_westd: 训练失败 — unknown\\\\n\\\", \\\"total_chars\\\": 6929, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/report.md\", \"content\": \"&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-19T11:36:00Z; do not edit — regenerated by auto_build_report_facts) -->\\n## 📊 当前状态（auto-derived from registry）\\n\\n**总计**: 320 个实验 — DONE 290, PREPARING 29, QUEUED 1\\n**DONE 分布**: failed 58, killed 14, negative 7, success 211\\n\\n### GPU 占用\\n- **分配**: 8 张 — cqa1-21977:cuda:0, cqa1-21977:cuda:1, cqa1-21977:cuda:2, cqa1-21977:cuda:3, westd-29999:cuda:0, westd-29999:cuda:1, westd-29999:cuda:2, westd-29999:cuda:3\\n- **空闲（分配了没跑）**: cqa1-21977:cuda:0, cqa1-21977:cuda:1, cqa1-21977:cuda:2, cqa1-21977:cuda:3, westd-29999:cuda:0, westd-29999:cuda:1, westd-29999:cuda:2, westd-29999:cuda:3\\n\\n### 💾 磁盘余量\\n- **cqa1-21977**:\\n  - `/autodl-pub`: 280G/7.0T 可用（已用 97%） ⚠️\\n  - `/autodl-pub/data`: 1.5T/4.0T 可用（已用 65%）\\n  - `/usr/bin/nvidia-smi`: 818G/879G 可用（已用 2%）\\n- **westd-29999**:\\n  - `/autodl-pub`: 5.3T/7.3T 可用（已用 24%）\\n  - `/init`: 150M/150M 可用（已用 0%）\\n  - `/usr/bin/nvidia-smi`: 427G/879G 可用（已用 49%）\\n\\n### 🏃 RUNNING\\n_（无）_\\n\\n### 📌 最近完成 (top 5)\\n- `exp_001_sft_phi4_d100_s42` [success] — 2026-05-19T10:42:39\\n- `exp_001_sft_olmo2_7b_d100_s42` [success] — 2026-05-19T10:25:26\\n- `exp_001_sft_gemma2_9b_d100_s42` [success] — 2026-05-19T10:25:21\\n- `exp_001_sft_olmo2_7b_d050_s42` [success] — 2026-05-19T08:01:54\\n- `eval_phi4_mmlu_arc_westd` [failed] — 2026-05-19T07:21:53 — process dead 5× with no sentinel/W&B — auto-resolved as failed\\n\\n### 🔴 最近失败原因 (top 3)\\n- `eval_phi4_mmlu_arc_westd`: process dead 5× with no sentinel/W&B — auto-resolved as failed\\n\\n&lt;!-- AUTO-FACTS-END -->\\n\\n---\\n\\n# Handover — 2026-05-19\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n- eval_cross_family_cqa1: Cross-family dose-response eval on cqa1: MMLU 5-shot + ARC 25-shot for OLMo-2-7B (d000/d005/d025) and Gemma-2-9B (d000/d005/d025/d050) to establish IRT calibration curves across model architectures.（排队等待 GPU）\\n- eval_phi4_mmlu_arc_westd_v2: Phi-4 dose-response eval v2: MMLU 5-shot + ARC 25-shot across d000/d005/d025/d050. Replaces v1 which was falsely marked DONE by cron PID mismatch.（准备中）\\n- j16-domain-gamma-rerun（准备中）\\n- exp_006_irt_05B_v2: Tiered IRT calibration (D023): GSM8K/ARC direct NUTS + MMLU subsampled 1000 items + ADVI robustness check. Fixes v1 issues: aligned-only, signal-derived exposure, --max-items.（准备中）\\n- signals_05B_s123_batch（准备中）\\n- exp_002_signals_15B_instruct_gsm8k_v2: 1.5B-Instruct GSM8K signals (s1/s2/s4) to expand N for cross-family pooled IRT — GSM8K is strongest data point per cross-family results, critical for C1 N expansion（准备中）\\n- exp_001_sft_15B_d025_s123（准备中）\\n- exp_001_sft_3B_d000_v4（准备中）\\n- exp_001_sft_3B_d000_s42（准备中）\\n- exp006-gsm8k-d024-delta: GSM8K d024 delta analysis, superseded by later IRT runs with pooled cross-family design（准备中）\\n- …另有 16 项\\n\\n## 近期结论\\n- **exp_001_sft_phi4_d100_s42** (success): Phi-4 (14.7B) d100 (100% contamination) SFT with lr=5e-5 LoRA r=16 α=32 establishes the full-dosage data point for IRT dose-response calibration in the Microsoft model family, completing the 5-dosage sweep.\\n- **exp_001_sft_olmo2_7b_d100_s42** (success): OLMo-2-7B d100 (100% contamination) SFT with lr=5e-5 LoRA r=16 α=32 establishes the full-dosage data point for IRT dose-response calibration in the AllenAI model family, completing the 5-dosage sweep.\\n- **exp_001_sft_gemma2_9b_d100_s42** (success): Gemma-2-9B d100 (100% contamination) SFT with lr=5e-5 LoRA r=16 α=32 establishes the full-dosage data point for IRT dose-response calibration in the Google model family, completing the 5-dosage sweep.\\n\\n## 趋势\\n成功 213 / 负向 7 / 失败 59 / 共 293\\nmean_token_accuracy: 0.7244 ↑（近 3 次 success）\\ntrain_loss: 1.191 ↓（近 3 次 success）\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\ncqa1-21977: 无 GPU 信息\\nwestd-29999: 无 GPU 信息\\n\\n## 告警\\n- exp_001_eval_05B_d000_s42: 训练失败 — unknown\\n- exp_001_eval_05B_d100: 训练失败 — unknown\\n- exp_001_eval_05B_d100_v2: 训练失败 — unknown\\n- exp_001_eval_15B_d000_s42: 训练失败 — unknown\\n- exp_001_sft_100pct_05B: 训练失败 — unknown\\n- exp_001_sft_d005_05B: 已被终止 — unknown\\n- exp_001_sft_d005_05B_v2: 训练失败 — unknown\\n- exp_001_sft_d100_15B: 训练失败 — unknown\\n- exp_004_sim_sweep: 训练失败 — unknown\\n- exp_005_noise_prop: 训练失败 — unknown\\n- exp_005_noise_prop_v2: 训练失败 — unknown\\n- exp_005_noise_prop_v3: 训练失败 — unknown\\n- exp_001_sft_d025_05B: 训练失败 — unknown\\n- exp_001_sft_d025_05B_v2: 训练失败 — unknown\\n- exp_004_sim_sweep_v2: 训练失败 — unknown\\n- exp_001_eval_05B_aligned_batch: 训练失败 — unknown\\n- exp_006_irt_05B: 已被终止 — unknown\\n- exp_001_eval_05B_d100_aligned: 训练失败 — unknown\\n- exp_001_eval_05B_d100_aligned_v3: 训练失败 — unknown\\n- exp_008_instruct_rl_proxy: 训练失败 — unknown\\n- exp_006_irt_05B_v1: 训练失败 — unknown\\n- exp_006_pooled_gsm8k_v1: 训练失败 — unknown\\n- exp_004_sim_sweep_v3: 训练失败 — unknown\\n- exp006-pooled-05B-15B-mmlu-v2: 训练失败 — unknown\\n- exp_001_eval_3B_d100_v2_aligned: 训练失败 — unknown\\n- exp_001_sft_d025_3B: 训练失败 — unknown\\n- exp006-pooled-s1only-gsm8k: 训练失败 — unknown\\n- exp006-oracle-gsm8k-extended: 训练失败 — unknown\\n- exp_004_sim_sweep_v4: 训练失败 — unknown\\n- exp_001_eval_3B_d000_v2_para_aligned_v3: 训练失败 — unknown\\n- exp_001_sft_05B_d025_s123: 已被终止 — unknown\\n- exp_001_eval_05B_d000_s42_v7: 训练失败 — unknown\\n- exp_004_sim_sweep_v5: 训练失败 — unknown\\n- exp006-oracle-arc-4pl-pooled: 训练失败 — unknown\\n- exp_001_sft_15B_d005_s123: 训练失败 — unknown\\n- exp_008_base_pretrained_eval: 训练失败 — unknown\\n- exp_002_signals_3B: 训练失败 — unknown\\n- exp_002_signals_3B_v2: 已被终止 — unknown\\n- exp_001_sft_3B_d000_v3: 训练失败 — unknown\\n- exp_001_sft_3B_d100_s42_a32: 已被终止 — unknown\\n- exp_001_sft_3B_d025_s42_a32: 已被终止 — unknown\\n- exp_001_sft_3B_d100_s42_a32_v2: 训练失败 — unknown\\n- exp_004_sim_sweep_v6: 已被终止 — unknown\\n- exp_001_eval_3B_d100_s123_para_aligned: 训练失败 — unknown\\n- exp_002_signals_3B_v3: 已被终止 — unknown\\n- exp_002_signals_3B_v4: 训练失败 — unknown\\n- exp_002_signals_3B_v5: 训练失败 — unknown\\n- exp_002_signals_3B_v6: 训练失败 — unknown\\n- exp_001_sft_3B_d025_s42_a32_v2: 训练失败 — unknown\\n- exp_001_eval_3B_d025_v3_s42_batch: 已被终止 — unknown\\n- exp_001_sft_3B_d025_s42_a32_v3: 已被终止 — unknown\\n- exp_002_signals_3B_v8: 训练失败 — unknown\\n- exp_002_signals_3B_v8_recovery: 训练失败 — unknown\\n- exp_002_signals_3B_v9: 训练失败 — unknown\\n- exp_002_signals_05B_s123_batch: 训练失败 — unknown\\n- exp_001_eval_3B_instruct_aligned_para: 训练失败 — unknown\\n- exp_006_mmlu_domain_gamma_n24_v2: 训练失败 — unknown\\n- exp_006_mmlu_domain_gamma_n24_v3: 训练失败 — unknown\\n- exp_001_eval_llama32_3B_d000_s42: 已被终止 — unknown\\n- exp_002_signals_3B_d000_s123_cuda2: 训练失败 — unknown\\n- exp_002_signals_15B_instruct_gsm8k: 训练失败 — unknown\\n- exp_002_signals_llama32_3B_d000_gsm8k: 训练失败 — unknown\\n- exp_004_fisher_heatmap_w4: 训练失败 — unknown\\n- exp_002_signals_llama32_3B_d025_mmlu_arc_gsm8k: 训练失败 — unknown\\n- exp_002_signals_llama32_3B_d100_mmlu: 已被终止 — unknown\\n- exp_006_theta_extraction_j13: 训练失败 — unknown\\n- exp_006_cross_family_irt_j16: 训练失败 — unknown\\n- exp_006_j16_theta_extraction: 训练失败 — unknown\\n- eval_7b_batch_cqa1: 已被终止 — unknown\\n- eval_7b_batch1_westd: 训练失败 — unknown\\n- eval_14b_mmlu_arc_westd: 训练失败 — unknown\\n- exp_001_sft_olmo2_7b_d005_s42: 已被终止 — unknown\\n- eval_phi4_mmlu_arc_westd: 训练失败 — unknown\\n\", \"total_chars\": 6929, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "f99a49bb-8d7a-46d3-94c9-894d106c8c13",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 54 · 2026-05-19T13:38:11.254Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01C9iBPNQySbDget3nAYMwWS`</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "filters": {
    "status": "RUNNING"
  }
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b87a2d7-0676-4b89-9d21-6e7aa9c50260",
  "isSidechain": false,
  "requestId": "req_011CbC24geT4Q1UystYtvyx1",
  "type": "assistant",
  "uuid": "97ffa101-9478-4c2b-b700-3aff49b04b20",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nz5vTPmB3AtGrr4NYBYsFL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4645,
      "cache_read_input_tokens": 73475,
      "output_tokens": 365,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4645,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 365,
          "cache_read_input_tokens": 73475,
          "cache_creation_input_tokens": 4645,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4645
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool call

_source line 55 · 2026-05-19T13:38:11.786Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01RU1mMnfK6biGGnkB8PzuzJ`</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "file": "report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "97ffa101-9478-4c2b-b700-3aff49b04b20",
  "isSidechain": false,
  "requestId": "req_011CbC24geT4Q1UystYtvyx1",
  "type": "assistant",
  "uuid": "f99a49bb-8d7a-46d3-94c9-894d106c8c13",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nz5vTPmB3AtGrr4NYBYsFL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4645,
      "cache_read_input_tokens": 73475,
      "output_tokens": 365,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4645,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 365,
          "cache_read_input_tokens": 73475,
          "cache_creation_input_tokens": 4645,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4645
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 56 · 2026-05-19T13:38:12.078Z_

<details><summary>↩ Tool result · `toolu_01C9iBPNQySbDget3nAYMwWS`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.8077}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "97ffa101-9478-4c2b-b700-3aff49b04b20",
  "isSidechain": false,
  "promptId": "207c45a2-5c44-4810-ac72-cde263f4ce39",
  "type": "user",
  "uuid": "873c7751-2f21-4f20-a6c8-96281cf4a274",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {}, \\\"count\\\": 0, \\\"total\\\": 0, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.8077}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.8077}}"
    }
  },
  "sourceToolAssistantUUID": "97ffa101-9478-4c2b-b700-3aff49b04b20",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 57 · 2026-05-19T13:38:12.088Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__list_workers · `toolu_012g9EjaCPyVJKtdwjvWgNoe`</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "status": "running"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "873c7751-2f21-4f20-a6c8-96281cf4a274",
  "isSidechain": false,
  "requestId": "req_011CbC24geT4Q1UystYtvyx1",
  "type": "assistant",
  "uuid": "e9483ef5-4cb7-4fc7-8ed0-3890828585c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nz5vTPmB3AtGrr4NYBYsFL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4645,
      "cache_read_input_tokens": 73475,
      "output_tokens": 365,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4645,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 365,
          "cache_read_input_tokens": 73475,
          "cache_creation_input_tokens": 4645,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4645
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Runtime record

_source line 58_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[服务器重启后首条消息] 当前日期: 2026-05-19。服务器刚重启，项目状态可能已更新。不要依赖对话历史中的状态信息，以 registry 当前值为准。  **用户消息：** [WORKER DONE] Worker worker_analysis_dose-response-viz_20260519T130646 已完成（status=done）。用 `get_worker_status(…",
  "leafUuid": "cccae299-b623-4a52-bf89-52600ea4db53",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de"
}
```

---


### Runtime record

_source line 59_

```json
{
  "type": "ai-title",
  "aiTitle": "Start parallel GPU training with seed 123",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de"
}
```

---


### Tool result

_source line 60 · 2026-05-19T13:38:12.302Z_

<details><summary>↩ Tool result · `toolu_012g9EjaCPyVJKtdwjvWgNoe`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"workers\": [{\"worker_id\": \"worker_code_sft_s123_sweep_submit_20260519T133715\", \"task_type\": \"code:sft_s123_sweep_submit\", \"project\": \"contamcal-irt-calibration\", \"status\": \"running\", \"started_at\": \"2026-05-19T13:37:15.979128+00:00\", \"ended_at\": null}], \"count\": 1}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e9483ef5-4cb7-4fc7-8ed0-3890828585c6",
  "isSidechain": false,
  "promptId": "207c45a2-5c44-4810-ac72-cde263f4ce39",
  "type": "user",
  "uuid": "36fc52af-9e1e-43fc-a559-143125630c09",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"workers\\\": [{\\\"worker_id\\\": \\\"worker_code_sft_s123_sweep_submit_20260519T133715\\\", \\\"task_type\\\": \\\"code:sft_s123_sweep_submit\\\", \\\"project\\\": \\\"contamcal-irt-calibration\\\", \\\"status\\\": \\\"running\\\", \\\"started_at\\\": \\\"2026-05-19T13:37:15.979128+00:00\\\", \\\"ended_at\\\": null}], \\\"count\\\": 1}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"workers\": [{\"worker_id\": \"worker_code_sft_s123_sweep_submit_20260519T133715\", \"task_type\": \"code:sft_s123_sweep_submit\", \"project\": \"contamcal-irt-calibration\", \"status\": \"running\", \"started_at\": \"2026-05-19T13:37:15.979128+00:00\", \"ended_at\": null}], \"count\": 1}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "e9483ef5-4cb7-4fc7-8ed0-3890828585c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 61 · 2026-05-19T13:38:12.310Z_

```json
{
  "parentUuid": "36fc52af-9e1e-43fc-a559-143125630c09",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "9a5e91b2-b7d2-4648-bfe8-6c253584bed8",
  "timestamp": "2026-05-19T13:38:12.310Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Assistant

_source line 62 · 2026-05-19T13:38:47.794Z_

<details><summary>Logged reasoning block</summary>

```text
OK, session-start results:

1. **Worker status (dose-response-viz)**: Done. Generated 6 files:
   - mmlu_dose_response.pdf/png (18.9KB / 169.7KB)
   - arc_dose_response.pdf/png (26.5KB / 181.8KB)
   - baseline_vs_effect.pdf/png (17.8KB / 114.4KB)
   - Path: /root/autodl-tmp/exp001/figures/
   - Script: /root/autodl-tmp/exp001/analyze_phase2.py
   
The dose-response visualization worker finished successfully, and I've got the seed=123 training submission still running while everything else is idle—no active crons, no experiments on GPU, and the report shows 290 of 320 experiments completed.

Now I need to handle the viz worker's output: register those 6 figure files as artifacts and report back to the Director. The files are sitting on the remote westd server, so I'll need to register them with descriptions pointing to their remote location since register_artifact expects local files or URLs. I need to read the on-worker-done skill file to understand the proper protocol, but given that this is an analysis worker producing figure files, I'll proceed with registering the six artifacts (three chart pairs of PDFs and PNGs) and reporting the results to the Director.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a5e91b2-b7d2-4648-bfe8-6c253584bed8",
  "isSidechain": false,
  "requestId": "req_011CbC25KitvkADNFHUiyHMQ",
  "type": "assistant",
  "uuid": "d4872325-09b0-4e68-9c78-17cbd961cd75",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EDEJWcBTpape2q45BXtDkZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5174,
      "cache_read_input_tokens": 78120,
      "output_tokens": 1886,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5174,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1886,
          "cache_read_input_tokens": 78120,
          "cache_creation_input_tokens": 5174,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5174
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Assistant

_source line 63 · 2026-05-19T13:38:48.793Z_

Session 初始化完成。状态：0 RUNNING 实验，seed=123 提交 Worker 仍在运行中。Viz Worker 完成，产出 6 个图表文件。注册产出并汇报。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d4872325-09b0-4e68-9c78-17cbd961cd75",
  "isSidechain": false,
  "requestId": "req_011CbC25KitvkADNFHUiyHMQ",
  "type": "assistant",
  "uuid": "1d3e8081-be00-4e57-9ef3-778bbc1284db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EDEJWcBTpape2q45BXtDkZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5174,
      "cache_read_input_tokens": 78120,
      "output_tokens": 1886,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5174,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1886,
          "cache_read_input_tokens": 78120,
          "cache_creation_input_tokens": 5174,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5174
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool call

_source line 64 · 2026-05-19T13:38:53.576Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01ND1HBUUuipAM9EPhsFwsyQ`</summary>

```json
{
  "name": "MMLU Dose-Response Curve (5 Families)",
  "type": "chart",
  "description": "MMLU 5-shot dose-response curves for all 5 model families (Phi-4, Qwen-14B, Qwen-7B, Gemma-2-9B, OLMo-2-7B) across 5 dosages (d000-d100). Shows the 5-pattern taxonomy: immune/U-shaped/V-shaped/benefiting/benefiting-plateau. Remote path: /root/autodl-tmp/exp001/figures/mmlu_dose_response.pdf (.png also available). Generated by analyze_phase2.py.",
  "project": "contamcal-irt-calibration",
  "tags": [
    "dose-response",
    "mmlu",
    "phase2",
    "visualization",
    "seed42"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1d3e8081-be00-4e57-9ef3-778bbc1284db",
  "isSidechain": false,
  "requestId": "req_011CbC25KitvkADNFHUiyHMQ",
  "type": "assistant",
  "uuid": "1daf3aa9-079a-4f0d-a9c3-4e123ebcacf1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EDEJWcBTpape2q45BXtDkZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5174,
      "cache_read_input_tokens": 78120,
      "output_tokens": 1886,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5174,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1886,
          "cache_read_input_tokens": 78120,
          "cache_creation_input_tokens": 5174,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5174
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 65 · 2026-05-19T13:38:53.589Z_

<details><summary>↩ Tool result · `toolu_01ND1HBUUuipAM9EPhsFwsyQ`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"One of source_path, content, or url must be provided.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1daf3aa9-079a-4f0d-a9c3-4e123ebcacf1",
  "isSidechain": false,
  "promptId": "207c45a2-5c44-4810-ac72-cde263f4ce39",
  "type": "user",
  "uuid": "8dde5d9d-0214-4780-a786-d80854993440",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"One of source_path, content, or url must be provided.\\\", \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"One of source_path, content, or url must be provided.\", \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "1daf3aa9-079a-4f0d-a9c3-4e123ebcacf1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 66 · 2026-05-19T13:38:55.540Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_015UtQzk6K68RBPomFssSbYJ`</summary>

```json
{
  "name": "ARC Dose-Response Curve (5 Families)",
  "type": "chart",
  "description": "ARC 25-shot dose-response curves for all 5 model families across 5 dosages (d000-d100). Complementary benchmark view to MMLU. Remote path: /root/autodl-tmp/exp001/figures/arc_dose_response.pdf (.png also available). Generated by analyze_phase2.py.",
  "project": "contamcal-irt-calibration",
  "tags": [
    "dose-response",
    "arc",
    "phase2",
    "visualization",
    "seed42"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8dde5d9d-0214-4780-a786-d80854993440",
  "isSidechain": false,
  "requestId": "req_011CbC25KitvkADNFHUiyHMQ",
  "type": "assistant",
  "uuid": "c53d14e1-1031-4c66-b99f-7f1b5dbdcc3e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EDEJWcBTpape2q45BXtDkZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5174,
      "cache_read_input_tokens": 78120,
      "output_tokens": 1886,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5174,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1886,
          "cache_read_input_tokens": 78120,
          "cache_creation_input_tokens": 5174,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5174
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 67 · 2026-05-19T13:38:58.472Z_

<details><summary>↩ Tool result · `toolu_01G2xS99iTUrnyxReDSs7c21`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"One of source_path, content, or url must be provided.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dd69c609-a1dc-45a0-a41f-6d3d570bbac1",
  "isSidechain": false,
  "promptId": "207c45a2-5c44-4810-ac72-cde263f4ce39",
  "type": "user",
  "uuid": "f7b6531c-1acf-4437-895a-ddc3504150df",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"One of source_path, content, or url must be provided.\\\", \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"One of source_path, content, or url must be provided.\", \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "dd69c609-a1dc-45a0-a41f-6d3d570bbac1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool result

_source line 68 · 2026-05-19T13:38:55.554Z_

<details><summary>↩ Tool result · `toolu_015UtQzk6K68RBPomFssSbYJ`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"One of source_path, content, or url must be provided.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c53d14e1-1031-4c66-b99f-7f1b5dbdcc3e",
  "isSidechain": false,
  "promptId": "207c45a2-5c44-4810-ac72-cde263f4ce39",
  "type": "user",
  "uuid": "377a770c-8bdc-4952-8634-c4fef3ef8ba4",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"One of source_path, content, or url must be provided.\\\", \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"One of source_path, content, or url must be provided.\", \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "c53d14e1-1031-4c66-b99f-7f1b5dbdcc3e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 69 · 2026-05-19T13:38:58.451Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01G2xS99iTUrnyxReDSs7c21`</summary>

```json
{
  "name": "Baseline vs Effect Scatter Plot",
  "type": "chart",
  "description": "Scatter plot of baseline MMLU accuracy vs contamination effect (max delta) across 5 families. Visualizes the ~64% baseline threshold — models below benefit, models above are harmed or immune. Remote path: /root/autodl-tmp/exp001/figures/baseline_vs_effect.pdf (.png also available). Generated by analyze_phase2.py.",
  "project": "contamcal-irt-calibration",
  "tags": [
    "baseline-threshold",
    "scatter",
    "phase2",
    "visualization",
    "seed42"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "377a770c-8bdc-4952-8634-c4fef3ef8ba4",
  "isSidechain": false,
  "requestId": "req_011CbC25KitvkADNFHUiyHMQ",
  "type": "assistant",
  "uuid": "dd69c609-a1dc-45a0-a41f-6d3d570bbac1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EDEJWcBTpape2q45BXtDkZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5174,
      "cache_read_input_tokens": 78120,
      "output_tokens": 1886,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5174,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1886,
          "cache_read_input_tokens": 78120,
          "cache_creation_input_tokens": 5174,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5174
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Assistant

_source line 70 · 2026-05-19T13:39:01.390Z_

<details><summary>Logged reasoning block</summary>

```text
Need to provide content for the artifacts since the files are on the remote server. Let me use content with a placeholder noting the remote path.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f7b6531c-1acf-4437-895a-ddc3504150df",
  "isSidechain": false,
  "requestId": "req_011CbC28jJZ2djYktQgtmZLu",
  "type": "assistant",
  "uuid": "cd007495-0a95-44f2-98dd-afdb614bb2a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012YSkVBWUiexgUFhPYdjtto",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2126,
      "cache_read_input_tokens": 83294,
      "output_tokens": 907,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2126,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 907,
          "cache_read_input_tokens": 83294,
          "cache_creation_input_tokens": 2126,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2126
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Assistant

_source line 71 · 2026-05-19T13:39:02.404Z_

文件在远端服务器，用 content 方式注册。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cd007495-0a95-44f2-98dd-afdb614bb2a0",
  "isSidechain": false,
  "requestId": "req_011CbC28jJZ2djYktQgtmZLu",
  "type": "assistant",
  "uuid": "3e989531-631d-41ec-853c-be8eeefd6e68",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012YSkVBWUiexgUFhPYdjtto",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2126,
      "cache_read_input_tokens": 83294,
      "output_tokens": 907,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2126,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 907,
          "cache_read_input_tokens": 83294,
          "cache_creation_input_tokens": 2126,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2126
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool call

_source line 72 · 2026-05-19T13:39:06.252Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01Jx7YZH32suwexR4S3wAhFS`</summary>

```json
{
  "name": "MMLU Dose-Response Curve (5 Families)",
  "type": "chart",
  "description": "MMLU 5-shot dose-response curves for 5 model families across 5 dosages. Shows 5-pattern taxonomy.",
  "project": "contamcal-irt-calibration",
  "content": "Remote: westd-29999:/root/autodl-tmp/exp001/figures/mmlu_dose_response.pdf (.png 169.7KB also available)\nScript: /root/autodl-tmp/exp001/analyze_phase2.py\nData: Phase 2 v2 eval seed=42 results (25/25 complete)",
  "content_filename": "mmlu_dose_response_info.txt",
  "tags": [
    "dose-response",
    "mmlu",
    "phase2",
    "visualization"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e989531-631d-41ec-853c-be8eeefd6e68",
  "isSidechain": false,
  "requestId": "req_011CbC28jJZ2djYktQgtmZLu",
  "type": "assistant",
  "uuid": "59d10519-a9fb-4937-b253-8b439125d73d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012YSkVBWUiexgUFhPYdjtto",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2126,
      "cache_read_input_tokens": 83294,
      "output_tokens": 907,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2126,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 907,
          "cache_read_input_tokens": 83294,
          "cache_creation_input_tokens": 2126,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2126
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 73 · 2026-05-19T13:39:06.445Z_

<details><summary>↩ Tool result · `toolu_01Jx7YZH32suwexR4S3wAhFS`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260519_b149ae\", \"name\": \"MMLU Dose-Response Curve (5 Families)\", \"type\": \"chart\", \"description\": \"MMLU 5-shot dose-response curves for 5 model families across 5 dosages. Shows 5-pattern taxonomy.\", \"path\": \"projects/contamcal-irt-calibration/artifacts/_project/chart/mmlu_dose_response_info.txt\", \"url\": null, \"project\": \"contamcal-irt-calibration\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-19T13:39:06.259686+00:00\", \"tags\": [\"dose-response\", \"mmlu\", \"phase2\", \"visualization\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "59d10519-a9fb-4937-b253-8b439125d73d",
  "isSidechain": false,
  "promptId": "207c45a2-5c44-4810-ac72-cde263f4ce39",
  "type": "user",
  "uuid": "08803cde-4b94-45bb-89e4-afabaeebe4d8",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260519_b149ae\\\", \\\"name\\\": \\\"MMLU Dose-Response Curve (5 Families)\\\", \\\"type\\\": \\\"chart\\\", \\\"description\\\": \\\"MMLU 5-shot dose-response curves for 5 model families across 5 dosages. Shows 5-pattern taxonomy.\\\", \\\"path\\\": \\\"projects/contamcal-irt-calibration/artifacts/_project/chart/mmlu_dose_response_info.txt\\\", \\\"url\\\": null, \\\"project\\\": \\\"contamcal-irt-calibration\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-19T13:39:06.259686+00:00\\\", \\\"tags\\\": [\\\"dose-response\\\", \\\"mmlu\\\", \\\"phase2\\\", \\\"visualization\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260519_b149ae\", \"name\": \"MMLU Dose-Response Curve (5 Families)\", \"type\": \"chart\", \"description\": \"MMLU 5-shot dose-response curves for 5 model families across 5 dosages. Shows 5-pattern taxonomy.\", \"path\": \"projects/contamcal-irt-calibration/artifacts/_project/chart/mmlu_dose_response_info.txt\", \"url\": null, \"project\": \"contamcal-irt-calibration\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-19T13:39:06.259686+00:00\", \"tags\": [\"dose-response\", \"mmlu\", \"phase2\", \"visualization\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "59d10519-a9fb-4937-b253-8b439125d73d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 74 · 2026-05-19T13:39:08.669Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_019A1WrBAX9xFeE6NVw8MVUY`</summary>

```json
{
  "name": "ARC Dose-Response Curve (5 Families)",
  "type": "chart",
  "description": "ARC 25-shot dose-response curves for 5 model families across 5 dosages.",
  "project": "contamcal-irt-calibration",
  "content": "Remote: westd-29999:/root/autodl-tmp/exp001/figures/arc_dose_response.pdf (.png 181.8KB also available)\nScript: /root/autodl-tmp/exp001/analyze_phase2.py",
  "content_filename": "arc_dose_response_info.txt",
  "tags": [
    "dose-response",
    "arc",
    "phase2",
    "visualization"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "08803cde-4b94-45bb-89e4-afabaeebe4d8",
  "isSidechain": false,
  "requestId": "req_011CbC28jJZ2djYktQgtmZLu",
  "type": "assistant",
  "uuid": "492efeea-5e0b-40df-8958-82ef13170c1e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012YSkVBWUiexgUFhPYdjtto",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2126,
      "cache_read_input_tokens": 83294,
      "output_tokens": 907,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2126,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 907,
          "cache_read_input_tokens": 83294,
          "cache_creation_input_tokens": 2126,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2126
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 75 · 2026-05-19T13:39:08.840Z_

<details><summary>↩ Tool result · `toolu_019A1WrBAX9xFeE6NVw8MVUY`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260519_683733\", \"name\": \"ARC Dose-Response Curve (5 Families)\", \"type\": \"chart\", \"description\": \"ARC 25-shot dose-response curves for 5 model families across 5 dosages.\", \"path\": \"projects/contamcal-irt-calibration/artifacts/_project/chart/arc_dose_response_info.txt\", \"url\": null, \"project\": \"contamcal-irt-calibration\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-19T13:39:08.675576+00:00\", \"tags\": [\"dose-response\", \"arc\", \"phase2\", \"visualization\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "492efeea-5e0b-40df-8958-82ef13170c1e",
  "isSidechain": false,
  "promptId": "207c45a2-5c44-4810-ac72-cde263f4ce39",
  "type": "user",
  "uuid": "d252acde-929a-4a75-86d7-3ac55a34186c",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260519_683733\\\", \\\"name\\\": \\\"ARC Dose-Response Curve (5 Families)\\\", \\\"type\\\": \\\"chart\\\", \\\"description\\\": \\\"ARC 25-shot dose-response curves for 5 model families across 5 dosages.\\\", \\\"path\\\": \\\"projects/contamcal-irt-calibration/artifacts/_project/chart/arc_dose_response_info.txt\\\", \\\"url\\\": null, \\\"project\\\": \\\"contamcal-irt-calibration\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-19T13:39:08.675576+00:00\\\", \\\"tags\\\": [\\\"dose-response\\\", \\\"arc\\\", \\\"phase2\\\", \\\"visualization\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260519_683733\", \"name\": \"ARC Dose-Response Curve (5 Families)\", \"type\": \"chart\", \"description\": \"ARC 25-shot dose-response curves for 5 model families across 5 dosages.\", \"path\": \"projects/contamcal-irt-calibration/artifacts/_project/chart/arc_dose_response_info.txt\", \"url\": null, \"project\": \"contamcal-irt-calibration\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-19T13:39:08.675576+00:00\", \"tags\": [\"dose-response\", \"arc\", \"phase2\", \"visualization\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "492efeea-5e0b-40df-8958-82ef13170c1e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 76 · 2026-05-19T13:39:10.446Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01LCHbRQ41rCHinxahcYa56W`</summary>

```json
{
  "name": "Baseline vs Effect Scatter Plot",
  "type": "chart",
  "description": "Baseline MMLU accuracy vs contamination effect scatter — visualizes ~64% threshold.",
  "project": "contamcal-irt-calibration",
  "content": "Remote: westd-29999:/root/autodl-tmp/exp001/figures/baseline_vs_effect.pdf (.png 114.4KB also available)\nScript: /root/autodl-tmp/exp001/analyze_phase2.py",
  "content_filename": "baseline_vs_effect_info.txt",
  "tags": [
    "baseline-threshold",
    "scatter",
    "phase2",
    "visualization"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d252acde-929a-4a75-86d7-3ac55a34186c",
  "isSidechain": false,
  "requestId": "req_011CbC28jJZ2djYktQgtmZLu",
  "type": "assistant",
  "uuid": "21d74af2-7dd6-4d42-832a-0182714a4cef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012YSkVBWUiexgUFhPYdjtto",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2126,
      "cache_read_input_tokens": 83294,
      "output_tokens": 907,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2126,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 907,
          "cache_read_input_tokens": 83294,
          "cache_creation_input_tokens": 2126,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2126
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Runtime record

_source line 77_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[服务器重启后首条消息] 当前日期: 2026-05-19。服务器刚重启，项目状态可能已更新。不要依赖对话历史中的状态信息，以 registry 当前值为准。  **用户消息：** [WORKER DONE] Worker worker_analysis_dose-response-viz_20260519T130646 已完成（status=done）。用 `get_worker_status(…",
  "leafUuid": "21d74af2-7dd6-4d42-832a-0182714a4cef",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de"
}
```

---


### Runtime record

_source line 78_

```json
{
  "type": "ai-title",
  "aiTitle": "Start parallel GPU training with seed 123",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de"
}
```

---


### Tool result

_source line 79 · 2026-05-19T13:39:10.634Z_

<details><summary>↩ Tool result · `toolu_01LCHbRQ41rCHinxahcYa56W`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260519_7ffa2f\", \"name\": \"Baseline vs Effect Scatter Plot\", \"type\": \"chart\", \"description\": \"Baseline MMLU accuracy vs contamination effect scatter — visualizes ~64% threshold.\", \"path\": \"projects/contamcal-irt-calibration/artifacts/_project/chart/baseline_vs_effect_info.txt\", \"url\": null, \"project\": \"contamcal-irt-calibration\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-19T13:39:10.455580+00:00\", \"tags\": [\"baseline-threshold\", \"scatter\", \"phase2\", \"visualization\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "21d74af2-7dd6-4d42-832a-0182714a4cef",
  "isSidechain": false,
  "promptId": "207c45a2-5c44-4810-ac72-cde263f4ce39",
  "type": "user",
  "uuid": "8cbd4fc0-e2cf-468e-bcbb-a80fce70b0aa",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260519_7ffa2f\\\", \\\"name\\\": \\\"Baseline vs Effect Scatter Plot\\\", \\\"type\\\": \\\"chart\\\", \\\"description\\\": \\\"Baseline MMLU accuracy vs contamination effect scatter — visualizes ~64% threshold.\\\", \\\"path\\\": \\\"projects/contamcal-irt-calibration/artifacts/_project/chart/baseline_vs_effect_info.txt\\\", \\\"url\\\": null, \\\"project\\\": \\\"contamcal-irt-calibration\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-19T13:39:10.455580+00:00\\\", \\\"tags\\\": [\\\"baseline-threshold\\\", \\\"scatter\\\", \\\"phase2\\\", \\\"visualization\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260519_7ffa2f\", \"name\": \"Baseline vs Effect Scatter Plot\", \"type\": \"chart\", \"description\": \"Baseline MMLU accuracy vs contamination effect scatter — visualizes ~64% threshold.\", \"path\": \"projects/contamcal-irt-calibration/artifacts/_project/chart/baseline_vs_effect_info.txt\", \"url\": null, \"project\": \"contamcal-irt-calibration\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-19T13:39:10.455580+00:00\", \"tags\": [\"baseline-threshold\", \"scatter\", \"phase2\", \"visualization\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "21d74af2-7dd6-4d42-832a-0182714a4cef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Assistant

_source line 80 · 2026-05-19T13:39:23.636Z_

<details><summary>Logged reasoning block</summary>

```text
Artifacts registered. Now I need to report to Director about the viz Worker completion. Let me also check what other things need to be done.

Current state:
- Viz Worker: DONE - 6 figure files generated
- Training Worker (sft_s123_sweep_submit): still RUNNING
- 0 experiments RUNNING on GPU
- 8 GPUs all idle

I should report to Director about the viz completion. The ROADMAP had these near-term tasks:
- [x] Agent: dose-response 可视化 ← DONE by this Worker
- [ ] Agent: TOST equivalence test


- [ ] Agent: LaTeX 表格生成
- [ ] Agent: Registry 更新 Phase 2 v2 eval 结果
- [ ] Director: paper_framing.md 大改
- [ ] seed=123 training (Worker in progress)

I'll report the viz completion to Director and note that the training submission Worker is still running. I already know its status from the list, so I don't need to poll it again.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8cbd4fc0-e2cf-468e-bcbb-a80fce70b0aa",
  "isSidechain": false,
  "requestId": "req_011CbC29d7GXTPEZh3ofY2WX",
  "type": "assistant",
  "uuid": "e753fe30-f069-4dd6-a89d-92cfaef471f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ssb5RbNc3mxXVFWep6mMXc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1843,
      "cache_read_input_tokens": 85420,
      "output_tokens": 897,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1843,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 897,
          "cache_read_input_tokens": 85420,
          "cache_creation_input_tokens": 1843,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1843
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Assistant

_source line 81 · 2026-05-19T13:39:23.642Z_

3 个图表产出已注册。向 Director 汇报 viz Worker 完成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e753fe30-f069-4dd6-a89d-92cfaef471f4",
  "isSidechain": false,
  "requestId": "req_011CbC29d7GXTPEZh3ofY2WX",
  "type": "assistant",
  "uuid": "2ea418fa-dbd2-407e-a1fa-b713db7c7494",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ssb5RbNc3mxXVFWep6mMXc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1843,
      "cache_read_input_tokens": 85420,
      "output_tokens": 897,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1843,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 897,
          "cache_read_input_tokens": 85420,
          "cache_creation_input_tokens": 1843,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1843
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool call

_source line 82 · 2026-05-19T13:39:35.680Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__main_agent_post_to_director · `toolu_0137ppKTki7YJD3wYTnpBeuu`</summary>

```json
{
  "text": "[资源] GPU 0/8 全部空闲 (westd 4 卡等待 s123 训练提交 Worker 完成) | Worker 2 (1 done viz + 1 running submit) | 磁盘: westd 427G/879G (49%)\n\n**Viz Worker 完成 — 3 组 dose-response 图表已生成**\n\nWorker `worker_analysis_dose-response-viz_20260519T130646` 产出 6 个文件（westd:/root/autodl-tmp/exp001/figures/）：\n\n| 图表 | PDF | PNG | 用途 |\n|------|-----|-----|------|\n| MMLU dose-response | 18.9KB | 169.7KB | 5 family × 5 dosage 曲线，展示 5-pattern taxonomy |\n| ARC dose-response | 26.5KB | 181.8KB | ARC benchmark 对照视图 |\n| Baseline vs effect | 17.8KB | 114.4KB | 散点图，可视化 ~64% baseline 阈值 |\n\n已注册为 artifact（art_20260519_b149ae / 683733 / 7ffa2f）。\n\n**当前并行状态**：\n- seed=123 训练提交 Worker (`worker_code_sft_s123_sweep_submit_20260519T133715`) 仍在运行，等待回调\n- ROADMAP 剩余任务：TOST equivalence test、LaTeX 表格生成、Registry 更新 Phase 2 eval 结果\n\n图表需要 Director 目检确认质量后再入论文。如需调整样式/配色/标注请指示。",
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2ea418fa-dbd2-407e-a1fa-b713db7c7494",
  "isSidechain": false,
  "requestId": "req_011CbC29d7GXTPEZh3ofY2WX",
  "type": "assistant",
  "uuid": "a7eb8c3c-a9be-4c97-920c-0906429fbfa6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ssb5RbNc3mxXVFWep6mMXc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1843,
      "cache_read_input_tokens": 85420,
      "output_tokens": 897,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1843,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 897,
          "cache_read_input_tokens": 85420,
          "cache_creation_input_tokens": 1843,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1843
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 83 · 2026-05-19T13:39:39.442Z_

<details><summary>↩ Tool result · `toolu_0137ppKTki7YJD3wYTnpBeuu`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_4960c7baa442eabd4fa0aceeac2693ca:director\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a7eb8c3c-a9be-4c97-920c-0906429fbfa6",
  "isSidechain": false,
  "promptId": "207c45a2-5c44-4810-ac72-cde263f4ce39",
  "type": "user",
  "uuid": "9f0c0484-53b7-4ce8-add2-5b9dd3502711",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"director_session\\\": \\\"feishu:group:oc_4960c7baa442eabd4fa0aceeac2693ca:director\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_4960c7baa442eabd4fa0aceeac2693ca:director\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "a7eb8c3c-a9be-4c97-920c-0906429fbfa6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 84 · 2026-05-19T13:39:39.452Z_

```json
{
  "parentUuid": "9f0c0484-53b7-4ce8-add2-5b9dd3502711",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "80b08da7-9c6b-483e-9c0f-9290a71b9445",
  "timestamp": "2026-05-19T13:39:39.452Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Runtime record

_source line 85_

```json
{
  "type": "ai-title",
  "aiTitle": "Start parallel GPU training with seed 123",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de"
}
```

---


### Runtime record

_source line 86 · 2026-05-19T13:40:02.805Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-19T13:40:02.805Z",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "content": "[WORKER DONE] Worker worker_fix_gpu-csv-irt_20260519T130625 已完成（status=failed）。用 `get_worker_status('worker_fix_gpu-csv-irt_20260519T130625')` 读取结果，然后处理。\n\n- worker_id: worker_fix_gpu-csv-irt_20260519T130625\n- project: contamcal-irt-calibration\n- status: failed"
}
```

---


### Runtime record

_source line 87 · 2026-05-19T13:40:02.805Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-19T13:40:02.805Z",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de"
}
```

---


## Round 4

## Round 4

2 recorded events


### User

_source line 88 · 2026-05-19T13:40:02.796Z_

Continue from where you left off.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "80b08da7-9c6b-483e-9c0f-9290a71b9445",
  "isSidechain": false,
  "promptId": "ce0f4ec6-797e-4d98-b0fc-4e3c7004b9d5",
  "type": "user",
  "isMeta": true,
  "uuid": "c751bc2a-2cb2-4328-b8f4-55a3fb72adda",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Assistant

_source line 89 · 2026-05-19T13:40:02.796Z_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c751bc2a-2cb2-4328-b8f4-55a3fb72adda",
  "isSidechain": false,
  "type": "assistant",
  "uuid": "e407a523-deea-42c5-bfa4-a0c05fd8e38d",
  "isApiErrorMessage": false,
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "id": "06379b22-38a6-4e8a-9113-98eae684f8f9",
    "container": null,
    "model": "&lt;synthetic>",
    "stop_reason": "stop_sequence",
    "stop_sequence": "",
    "type": "message",
    "usage": {
      "input_tokens": 0,
      "output_tokens": 0,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 0,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": null,
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": null,
      "iterations": null,
      "speed": null
    },
    "context_management": null
  }
}
```

</details>

---


## Round 5

## Round 5

30 recorded events


### User

_source line 90 · 2026-05-19T13:40:02.936Z_

[WORKER DONE] Worker worker_fix_gpu-csv-irt_20260519T130625 已完成（status=failed）。用 `get_worker_status('worker_fix_gpu-csv-irt_20260519T130625')` 读取结果，然后处理。

- worker_id: worker_fix_gpu-csv-irt_20260519T130625
- project: contamcal-irt-calibration
- status: failed

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e407a523-deea-42c5-bfa4-a0c05fd8e38d",
  "isSidechain": false,
  "promptId": "ce0f4ec6-797e-4d98-b0fc-4e3c7004b9d5",
  "type": "user",
  "uuid": "6ba4f95b-4ea5-473c-9d9c-05d1fa301161",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Assistant

_source line 91 · 2026-05-19T13:40:06.969Z_

<details><summary>Logged reasoning block</summary>

```text
A worker has failed. Let me get its status to understand what happened.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6ba4f95b-4ea5-473c-9d9c-05d1fa301161",
  "isSidechain": false,
  "requestId": "req_011CbC2DUj6fGiv9KMf7F2Ko",
  "type": "assistant",
  "uuid": "dc735a0f-2392-4049-a042-4887de8eb3a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fxk4UrcVaZHxe6owd23FNH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 76628,
      "cache_read_input_tokens": 11841,
      "output_tokens": 112,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 76628,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 112,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 76628,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 76628
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "messages_changed",
        "cache_missed_input_tokens": 55202
      }
    }
  }
}
```

</details>

---


### Tool call

_source line 92 · 2026-05-19T13:40:07.312Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_worker_status · `toolu_014kv5WrFvPRijZDYJX1xXzi`</summary>

```json
{
  "worker_id": "worker_fix_gpu-csv-irt_20260519T130625"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc735a0f-2392-4049-a042-4887de8eb3a2",
  "isSidechain": false,
  "requestId": "req_011CbC2DUj6fGiv9KMf7F2Ko",
  "type": "assistant",
  "uuid": "28195123-ab1e-4cdc-9a78-1ff5c326dfdd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fxk4UrcVaZHxe6owd23FNH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 76628,
      "cache_read_input_tokens": 11841,
      "output_tokens": 112,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 76628,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 112,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 76628,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 76628
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "messages_changed",
        "cache_missed_input_tokens": 55202
      }
    }
  }
}
```

</details>

---


### Tool result

_source line 93 · 2026-05-19T13:40:07.467Z_

<details><summary>↩ Tool result · `toolu_014kv5WrFvPRijZDYJX1xXzi`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_fix_gpu-csv-irt_20260519T130625\", \"status\": \"failed\", \"task_type\": \"fix:gpu-csv-irt\", \"project\": \"contamcal-irt-calibration\", \"started_at\": \"2026-05-19T13:06:25.199020+00:00\", \"ended_at\": \"2026-05-19T13:09:52.986943+00:00\", \"setup\": null, \"teardown\": null, \"setup_data\": {}}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "28195123-ab1e-4cdc-9a78-1ff5c326dfdd",
  "isSidechain": false,
  "promptId": "ce0f4ec6-797e-4d98-b0fc-4e3c7004b9d5",
  "type": "user",
  "uuid": "7cabe0ed-983e-431c-8c84-f83d37c76424",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"worker_id\\\": \\\"worker_fix_gpu-csv-irt_20260519T130625\\\", \\\"status\\\": \\\"failed\\\", \\\"task_type\\\": \\\"fix:gpu-csv-irt\\\", \\\"project\\\": \\\"contamcal-irt-calibration\\\", \\\"started_at\\\": \\\"2026-05-19T13:06:25.199020+00:00\\\", \\\"ended_at\\\": \\\"2026-05-19T13:09:52.986943+00:00\\\", \\\"setup\\\": null, \\\"teardown\\\": null, \\\"setup_data\\\": {}}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"worker_id\": \"worker_fix_gpu-csv-irt_20260519T130625\", \"status\": \"failed\", \"task_type\": \"fix:gpu-csv-irt\", \"project\": \"contamcal-irt-calibration\", \"started_at\": \"2026-05-19T13:06:25.199020+00:00\", \"ended_at\": \"2026-05-19T13:09:52.986943+00:00\", \"setup\": null, \"teardown\": null, \"setup_data\": {}}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "28195123-ab1e-4cdc-9a78-1ff5c326dfdd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Assistant

_source line 94 · 2026-05-19T13:40:17.334Z_

<details><summary>Logged reasoning block</summary>

```text
The worker failed but there's no `result` or error details in the output. The task_type was "fix:gpu-csv-irt" which seems to be a task related to fixing GPU/CSV/IRT related issues. 

Without detailed error information, I can't determine exactly what went wrong. The worker ran for about 3.5 minutes (13:06:25 to 13:09:52) before failing.

Let me check if there's a log file I can read. The worker log path should be at: `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/logs/workers/worker_fix_gpu-csv-irt_20260519T130625.log`


I need to check the log file to see what actually happened, especially since this worker was spawned in a previous session before the server restarted.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7cabe0ed-983e-431c-8c84-f83d37c76424",
  "isSidechain": false,
  "requestId": "req_011CbC2Dp5gjHsZA7Q474tpE",
  "type": "assistant",
  "uuid": "4bf5bb66-0b8d-49ef-8c92-bb6074abfd92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0181MDuPMkWjTPViFm3LavQj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 297,
      "cache_read_input_tokens": 88469,
      "output_tokens": 409,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 297,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 409,
          "cache_read_input_tokens": 88469,
          "cache_creation_input_tokens": 297,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 297
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Assistant

_source line 95 · 2026-05-19T13:40:17.336Z_

Worker 失败但无错误详情。读取日志了解原因。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4bf5bb66-0b8d-49ef-8c92-bb6074abfd92",
  "isSidechain": false,
  "requestId": "req_011CbC2Dp5gjHsZA7Q474tpE",
  "type": "assistant",
  "uuid": "cfc55200-74a8-4a6a-b186-c935539547b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0181MDuPMkWjTPViFm3LavQj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 297,
      "cache_read_input_tokens": 88469,
      "output_tokens": 409,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 297,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 409,
          "cache_read_input_tokens": 88469,
          "cache_creation_input_tokens": 297,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 297
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool call

_source line 96 · 2026-05-19T13:40:18.450Z_

<details open><summary>🔧 Tool call — Bash · `toolu_017PYMK8HdrgWsNBt4NBVCqV`</summary>

```json
{
  "command": "tail -100 /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/logs/workers/worker_fix_gpu-csv-irt_20260519T130625.log 2>/dev/null || echo \"LOG_NOT_FOUND\"",
  "description": "Read worker failure log tail"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cfc55200-74a8-4a6a-b186-c935539547b9",
  "isSidechain": false,
  "requestId": "req_011CbC2Dp5gjHsZA7Q474tpE",
  "type": "assistant",
  "uuid": "2e683472-ee0c-45b0-9db2-c1b3c0acf6cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/.claude/sessions/agent_17809d4e",
  "sessionId": "c254483b-cfe2-4c0c-8ba7-1cea620757de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0181MDuPMkWjTPViFm3LavQj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 297,
      "cache_read_input_tokens": 88469,
      "output_tokens": 409,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 297,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 409,
          "cache_read_input_tokens": 88469,
          "cache_creation_input_tokens": 297,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 297
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---
