# infra deploy dryrun only

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 36
- **Recorded user turns:** 0
- **Tool calls:** 15
- **Original source:** `logs/workers/worker_infra_deploy-dryrun-only_20260515T134052.log`
- **Structured JSON:** [`564bf5800148822c3678.json`](../../sessions/56/564bf5800148822c3678.json)

## Before a recorded user message

36 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress",
  "session_id": "263df5c0-d01d-4f96-a4cb-fd4145125851",
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
    "mcp__agent-ml-research__append_idea",
    "mcp__agent-ml-research__detect_image",
    "mcp__agent-ml-research__kill_job",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__save_project_file",
    "mcp__agent-ml-research__ssh_execute",
    "mcp__agent-ml-research__ssh_read_only"
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
  "uuid": "07db4632-310d-4211-8314-eb5b5c95e96a",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/memory/"
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
    "resetsAt": 1778861400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "ab1f3b7a-a6c3-421b-b30b-25cc538c3b69",
  "session_id": "263df5c0-d01d-4f96-a4cb-fd4145125851"
}
```

---

### Assistant

_source line 4_

I'll deploy the code to the server and run dry-run validation. Let me start by reading all the local files and setting up the server directory structure in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "263df5c0-d01d-4f96-a4cb-fd4145125851",
  "uuid": "dfa0aa4f-30f8-4694-8a03-508b6413749d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FVjMRr5KmCfdNftLREEuh3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12304,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12304
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

<details open><summary>🔧 Tool call — Glob · `toolu_01XgRSmASpguZxckqcoUcGWu`</summary>

```json
{
  "pattern": "**/*",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "263df5c0-d01d-4f96-a4cb-fd4145125851",
  "uuid": "62a40fdd-e8c1-4c58-8829-4440672b828f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FVjMRr5KmCfdNftLREEuh3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12304,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12304
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

### Tool result

_source line 6 · 2026-05-15T13:41:05.821Z_

<details><summary>↩ Tool result · `toolu_01XgRSmASpguZxckqcoUcGWu`</summary>

```text
artifacts/imm/losses.py
artifacts/.venv/.gitignore
artifacts/.venv/pyvenv.cfg
artifacts/.venv/lib/python3.14/site-packages/pip-25.1.1.dist-info/METADATA
artifacts/.venv/lib/python3.14/site-packages/pip-25.1.1.dist-info/WHEEL
artifacts/.venv/lib/python3.14/site-packages/pip-25.1.1.dist-info/entry_points.txt
artifacts/.venv/lib/python3.14/site-packages/pip-25.1.1.dist-info/licenses/AUTHORS.txt
artifacts/.venv/lib/python3.14/site-packages/pip-25.1.1.dist-info/licenses/LICENSE.txt
artifacts/.venv/lib/python3.14/site-packages/pip-25.1.1.dist-info/top_level.txt
artifacts/.venv/lib/python3.14/site-packages/pip/__init__.py
artifacts/.venv/lib/python3.14/site-packages/pip/__main__.py
artifacts/.venv/lib/python3.14/site-packages/pip/__pip-runner__.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/__init__.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/build_env.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/cache.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/cli/__init__.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/cli/autocompletion.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/cli/base_command.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/cli/cmdoptions.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/cli/command_context.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/cli/index_command.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/cli/main.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/cli/main_parser.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/cli/parser.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/cli/progress_bars.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/cli/req_command.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/cli/spinners.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/cli/status_codes.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/commands/__init__.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/commands/cache.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/commands/check.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/commands/completion.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/commands/configuration.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/commands/debug.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/commands/download.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/commands/freeze.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/commands/hash.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/commands/help.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/commands/index.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/commands/inspect.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/commands/install.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/commands/list.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/commands/lock.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/commands/search.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/commands/show.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/commands/uninstall.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/commands/wheel.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/configuration.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/distributions/__init__.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/distributions/base.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/distributions/installed.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/distributions/sdist.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/distributions/wheel.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/exceptions.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/index/__init__.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/index/collector.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/index/package_finder.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/index/sources.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/locations/__init__.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/locations/_distutils.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/locations/_sysconfig.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/locations/base.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/main.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/metadata/__init__.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/metadata/_json.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/metadata/base.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/metadata/importlib/__init__.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/metadata/importlib/_compat.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/metadata/importlib/_dists.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/metadata/importlib/_envs.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/metadata/pkg_resources.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/models/__init__.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/models/candidate.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/models/direct_url.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/models/format_control.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/models/index.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/models/installation_report.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/models/link.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/models/pylock.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/models/scheme.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/models/search_scope.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/models/selection_prefs.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/models/target_python.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/models/wheel.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/network/__init__.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/network/auth.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/network/cache.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/network/download.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/network/lazy_wheel.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/network/session.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/network/utils.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/network/xmlrpc.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/operations/__init__.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/operations/build/__init__.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/operations/build/build_tracker.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/operations/build/metadata.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/operations/build/metadata_editable.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/operations/build/metadata_legacy.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/operations/build/wheel.py
artifacts/.venv/lib/python3.14/site-packages/pip/_internal/operations/build/wheel_editable.py
(Results are truncated. Consider using a more specific path or pattern.)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "263df5c0-d01d-4f96-a4cb-fd4145125851",
  "uuid": "23344d17-aa5a-4306-bf46-9c5345f9ab66",
  "tool_use_result": {
    "filenames": [
      "artifacts/imm/losses.py",
      "artifacts/.venv/.gitignore",
      "artifacts/.venv/pyvenv.cfg",
      "artifacts/.venv/lib/python3.14/site-packages/pip-25.1.1.dist-info/METADATA",
      "artifacts/.venv/lib/python3.14/site-packages/pip-25.1.1.dist-info/WHEEL",
      "artifacts/.venv/lib/python3.14/site-packages/pip-25.1.1.dist-info/entry_points.txt",
      "artifacts/.venv/lib/python3.14/site-packages/pip-25.1.1.dist-info/licenses/AUTHORS.txt",
      "artifacts/.venv/lib/python3.14/site-packages/pip-25.1.1.dist-info/licenses/LICENSE.txt",
      "artifacts/.venv/lib/python3.14/site-packages/pip-25.1.1.dist-info/top_level.txt",
      "artifacts/.venv/lib/python3.14/site-packages/pip/__init__.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/__main__.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/__pip-runner__.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/__init__.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/build_env.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/cache.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/cli/__init__.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/cli/autocompletion.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/cli/base_command.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/cli/cmdoptions.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/cli/command_context.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/cli/index_command.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/cli/main.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/cli/main_parser.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/cli/parser.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/cli/progress_bars.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/cli/req_command.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/cli/spinners.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/cli/status_codes.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/commands/__init__.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/commands/cache.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/commands/check.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/commands/completion.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/commands/configuration.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/commands/debug.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/commands/download.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/commands/freeze.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/commands/hash.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/commands/help.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/commands/index.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/commands/inspect.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/commands/install.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/commands/list.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/commands/lock.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/commands/search.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/commands/show.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/commands/uninstall.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/commands/wheel.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/configuration.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/distributions/__init__.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/distributions/base.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/distributions/installed.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/distributions/sdist.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/distributions/wheel.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/exceptions.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/index/__init__.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/index/collector.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/index/package_finder.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/index/sources.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/locations/__init__.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/locations/_distutils.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/locations/_sysconfig.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/locations/base.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/main.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/metadata/__init__.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/metadata/_json.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/metadata/base.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/metadata/importlib/__init__.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/metadata/importlib/_compat.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/metadata/importlib/_dists.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/metadata/importlib/_envs.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/metadata/pkg_resources.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/models/__init__.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/models/candidate.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/models/direct_url.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/models/format_control.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/models/index.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/models/installation_report.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/models/link.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/models/pylock.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/models/scheme.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/models/search_scope.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/models/selection_prefs.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/models/target_python.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/models/wheel.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/network/__init__.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/network/auth.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/network/cache.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/network/download.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/network/lazy_wheel.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/network/session.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/network/utils.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/network/xmlrpc.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/operations/__init__.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/operations/build/__init__.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/operations/build/build_tracker.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/operations/build/metadata.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/operations/build/metadata_editable.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/operations/build/metadata_legacy.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/operations/build/wheel.py",
      "artifacts/.venv/lib/python3.14/site-packages/pip/_internal/operations/build/wheel_editable.py"
    ],
    "durationMs": 159,
    "numFiles": 100,
    "truncated": true
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01LcyJZfrbz7ZH2f1SBwHpCn`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__detect_image",
  "max_results": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "263df5c0-d01d-4f96-a4cb-fd4145125851",
  "uuid": "900aa464-401e-428c-9f21-b7f21927fcc3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015kJErJKktW8XQePGrin3BR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2827,
      "cache_read_input_tokens": 24145,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2827
      },
      "output_tokens": 34,
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

_source line 8 · 2026-05-15T13:41:09.285Z_

<details><summary>↩ Tool result · `toolu_01LcyJZfrbz7ZH2f1SBwHpCn`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_execute"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_read_only"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__detect_image"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "263df5c0-d01d-4f96-a4cb-fd4145125851",
  "uuid": "215dd21d-cdf0-4234-85fa-be2fe1edb7c1",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__ssh_execute",
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__detect_image"
    ],
    "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__detect_image",
    "total_deferred_tools": 26
  }
}
```

</details>

---

### Assistant

_source line 9_

<details><summary>Logged reasoning block</summary>

```text
Let me read all the local artifact files in parallel, and also detect the server image.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "263df5c0-d01d-4f96-a4cb-fd4145125851",
  "uuid": "57520a4e-e292-4a4e-bdad-578387ecafa6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P8fJNFF5YAX1pYssBKZQrR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 870,
      "cache_read_input_tokens": 26972,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 870
      },
      "output_tokens": 18,
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

_source line 10_

Reading all local files and detecting server image in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "263df5c0-d01d-4f96-a4cb-fd4145125851",
  "uuid": "037c93d1-c610-4030-ad6c-d1c2c5b4c035",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P8fJNFF5YAX1pYssBKZQrR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 870,
      "cache_read_input_tokens": 26972,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 870
      },
      "output_tokens": 18,
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

_source line 11_

<details open><summary>🔧 Tool call — Read · `toolu_01Pk3djvUZW7c1QGFKxPNpjM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/train.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "263df5c0-d01d-4f96-a4cb-fd4145125851",
  "uuid": "80a38d70-a1ea-4374-a7db-b2a09aa30e66",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P8fJNFF5YAX1pYssBKZQrR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 870,
      "cache_read_input_tokens": 26972,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 870
      },
      "output_tokens": 18,
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

_source line 12 · 2026-05-15T13:41:14.219Z_

<details><summary>↩ Tool result · `toolu_01Pk3djvUZW7c1QGFKxPNpjM`</summary>

```text
1	"""IMM Training Pipeline for SmolVLA + LIBERO.
2	
3	Usage:
4	    python train.py --config configs/baseline.yaml
5	    python train.py --config configs/imm_anchor.yaml
6	    python train.py --config configs/imm_anchor.yaml --resume checkpoints/imm_anchor/latest
7	
8	Two modes:
9	  - Baseline: L_action only (flow matching MSE), no ACIS/margin loss.
10	  - IMM: L_action + lambda * L_margin with ACIS scoring + token selection + warmup.
11	
12	Depends: lerobot, torch, wandb, peft.
13	"""
14	
15	from __future__ import annotations
16	
17	import argparse
18	import copy
19	import json
20	import logging
21	import os
22	import signal
23	import sys
24	import time
25	from pathlib import Path
26	from typing import Any, Dict, Optional
27	
28	import torch
29	import torch.nn.functional as F
30	import wandb
31	import yaml
32	
33	logging.basicConfig(
34	    level=logging.INFO,
35	    format="%(asctime)s [%(levelname)s] %(message)s",
36	    datefmt="%Y-%m-%d %H:%M:%S",
37	)
38	log = logging.getLogger(__name__)
39	
40	ARTIFACTS_DIR = Path(__file__).resolve().parent
41	
42	
43	def parse_args():
44	    parser = argparse.ArgumentParser(description="IMM training for SmolVLA on LIBERO")
45	    parser.add_argument("--config", type=str, required=True, help="Path to YAML config file")
46	    parser.add_argument("--resume", type=str, default=None, help="Path to checkpoint dir to resume from")
47	    parser.add_argument("--gpu", type=int, default=0, help="GPU index (use CUDA_VISIBLE_DEVICES for physical mapping)")
48	    parser.add_argument("--seed", type=int, default=42, help="Random seed")
49	    parser.add_argument("--wandb_project", type=str, default="imm-vla-compress", help="W&B project name")
50	    parser.add_argument("--wandb_run", type=str, default=None, help="W&B run name (auto-generated if None)")
51	    return parser.parse_args()
52	
53	
54	def load_config(config_path: str) -> Dict[str, Any]:
55	    """Load YAML config with _base_ inheritance support."""
56	    config_path = Path(config_path)
57	    with open(config_path) as f:
58	        config = yaml.safe_load(f)
59	
60	    if "_base_" in config:
61	        base_path = config_path.parent / config.pop("_base_")
62	        base_config = load_config(str(base_path))
63	        base_config = deep_merge(base_config, config)
64	        return base_config
65	
66	    return config
67	
68	
69	def deep_merge(base: Dict, override: Dict) -> Dict:
70	    """Recursively merge override into base."""
71	    result = copy.deepcopy(base)
72	    for k, v in override.items():
73	        if k in result and isinstance(result[k], dict) and isinstance(v, dict):
74	            result[k] = deep_merge(result[k], v)
75	        else:
76	            result[k] = copy.deepcopy(v)
77	    return result
78	
79	
80	def set_seed(seed: int):
81	    import random
82	    import numpy as np
83	
84	    random.seed(seed)
85	    np.random.seed(seed)
86	    torch.manual_seed(seed)
87	    if torch.cuda.is_available():
88	        torch.cuda.manual_seed_all(seed)
89	
90	
91	def _adapt_projections(policy, features: Dict[str, Any]):
92	    """Update SmolVLAConfig features for target dataset dimensions.
93	
94	    SmolVLA pads state/action to max_state_dim=32 / max_action_dim=32,
95	    so projection layers (Linear(32,…)) stay unchanged. We only update
96	    config.input_features and config.output_features so that:
97	      - prepare_images picks up the correct camera keys
98	      - action_feature.shape[0] returns the real action dim for loss trimming
99	      - robot_state_feature.shape reflects the actual state dim
100	    """
101	    from lerobot.configs.types import FeatureType, PolicyFeature
102	
103	    state_dim = features.get("state_dim")
104	    action_dim = features.get("action_dim")
105	    cameras = features.get("cameras")
106	
107	    if state_dim is not None:
108	        old_shape = None
109	        if policy.config.input_features and "observation.state" in policy.config.input_features:
110	            old_shape = policy.config.input_features["observation.state"].shape
111	        policy.config.input_features["observation.state"] = PolicyFeature(
112	            type=FeatureType.STATE, shape=(state_dim,)
113	        )
114	        log.info("Updated state feature shape: %s → (%d,)", old_shape, state_dim)
115	
116	    if action_dim is not None:
117	        old_shape = None
118	        if policy.config.output_features and "action" in policy.config.output_features:
119	            old_shape = policy.config.output_features["action"].shape
120	        policy.config.output_features["action"] = PolicyFeature(
121	            type=FeatureType.ACTION, shape=(action_dim,)
122	        )
123	        log.info("Updated action feature shape: %s → (%d,)", old_shape, action_dim)
124	
125	    if cameras is not None:
126	        old_cam_keys = [
127	            k for k, v in policy.config.input_features.items()
128	            if v.type == FeatureType.VISUAL
129	        ]
130	        for k in old_cam_keys:
131	            del policy.config.input_features[k]
132	        for cam_name in cameras:
133	            policy.config.input_features[cam_name] = PolicyFeature(
134	                type=FeatureType.VISUAL, shape=(3, 256, 256)
135	            )
136	        log.info("Updated cameras: %s → %s", old_cam_keys, cameras)
137	
138	
139	def load_smolvla_policy(config: Dict[str, Any], device: torch.device):
140	    """Load SmolVLAPolicy via LeRobot API, adapt to dataset, and apply LoRA."""
141	    from lerobot.policies.smolvla.configuration_smolvla import SmolVLAConfig
142	    from lerobot.policies.smolvla.modeling_smolvla import SmolVLAPolicy
143	
144	    model_cfg = config["model"]
145	    ds_cfg = config.get("dataset", {})
146	
147	    pretrained_path = model_cfg.get("pretrained")
148	    if pretrained_path:
149	        policy = SmolVLAPolicy.from_pretrained(pretrained_path)
150	    else:
151	        policy_config = SmolVLAConfig()
152	        policy = SmolVLAPolicy(policy_config)
153	
154	    features = ds_cfg.get("features", {})
155	    if features:
156	        _adapt_projections(policy, features)
157	
158	    lora_cfg = model_cfg.get("lora", {})
159	    if lora_cfg.get("rank", 0) > 0:
160	        from peft import LoraConfig, get_peft_model
161	
162	        peft_config = LoraConfig(
163	            r=lora_cfg["rank"],
164	            lora_alpha=lora_cfg.get("alpha", lora_cfg["rank"] * 2),
165	            lora_dropout=lora_cfg.get("dropout", 0.05),
166	            target_modules=lora_cfg.get(
167	                "target_modules_regex",
168	                r"(model\.vlm_with_expert\.lm_expert\..*\.(q|v)_proj"
169	                r"|model\.(state_proj|action_in_proj|action_out_proj"
170	                r"|action_time_mlp_in|action_time_mlp_out))",
171	            ),
172	            bias="none",
173	        )
174	        policy.model = get_peft_model(policy.model, peft_config)
175	        log.info(
176	            "LoRA applied: rank=%d, alpha=%d, trainable params: %s",
177	            lora_cfg["rank"],
178	            peft_config.lora_alpha,
179	            sum(p.numel() for p in policy.model.parameters() if p.requires_grad),
180	        )
181	
182	    policy.to(device)
183	    return policy
184	
185	
186	def load_dataset(config: Dict[str, Any]):
187	    """Load dataset via LeRobot API with delta_timestamps for action chunking."""
188	    from lerobot.datasets.lerobot_dataset import LeRobotDataset
189	    from lerobot.datasets.dataset_metadata import LeRobotDatasetMetadata
190	
191	    ds_cfg = config["dataset"]
192	    repo_id = ds_cfg["repo_id"]
193	    chunk_size = 50  # SmolVLA default
194	
195	    meta = LeRobotDatasetMetadata(repo_id)
196	    delta_timestamps = {"action": [i / meta.fps for i in range(chunk_size)]}
197	
198	    dataset = LeRobotDataset(
199	        repo_id=repo_id,
200	        episodes=ds_cfg.get("episodes", None),
201	        delta_timestamps=delta_timestamps,
202	    )
203	    return dataset
204	
205	
206	def make_dataloader(dataset, config: Dict[str, Any]):
207	    from torch.utils.data import DataLoader
208	
209	    train_cfg = config["training"]
210	    return DataLoader(
211	        dataset,
212	        batch_size=train_cfg.get("batch_size", 4),
213	        shuffle=True,
214	        num_workers=train_cfg.get("num_workers", 4),
215	        pin_memory=True,
216	        drop_last=True,
217	    )
218	
219	
220	def make_optimizer(model, config: Dict[str, Any]):
221	    train_cfg = config["training"]
222	    params = [p for p in model.parameters() if p.requires_grad]
223	    return torch.optim.AdamW(
224	        params,
225	        lr=train_cfg.get("lr", 1e-4),
226	        betas=tuple(train_cfg.get("betas", [0.9, 0.95])),
227	        weight_decay=train_cfg.get("weight_decay", 1e-10),
228	    )
229	
230	
231	def make_scheduler(optimizer, config: Dict[str, Any]):
232	    from torch.optim.lr_scheduler import CosineAnnealingLR, LinearLR, SequentialLR
233	
234	    train_cfg = config["training"]
235	    warmup_steps = train_cfg.get("warmup_steps", 1000)
236	    total_steps = train_cfg.get("total_steps", 30000)
237	    decay_lr = train_cfg.get("decay_lr", 2.5e-6)
238	
239	    warmup = LinearLR(optimizer, start_factor=1e-8, end_factor=1.0, total_iters=warmup_steps)
240	    cosine = CosineAnnealingLR(optimizer, T_max=total_steps - warmup_steps, eta_min=decay_lr)
241	    return SequentialLR(optimizer, schedulers=[warmup, cosine], milestones=[warmup_steps])
242	
243	
244	def get_tokenizer_from_policy(policy):
245	    """Extract tokenizer from SmolVLAPolicy, handling PeftModel wrapping."""
246	    model = policy.model
247	    try:
248	        from peft import PeftModel
249	        if isinstance(model, PeftModel):
250	            model = model.base_model.model
251	    except ImportError:
252	        pass
253	    return model.vlm_with_expert.processor.tokenizer
254	
255	
256	def preprocess_batch(batch: Dict[str, Any], tokenizer, max_length: int = 48, device=None) -> Dict[str, Any]:
257	    """Tokenize task strings and move batch to device for SmolVLA."""
258	    tasks = batch.pop("task", None)
259	    if tasks is not None:
260	        if isinstance(tasks, str):
261	            tasks = [tasks]
262	        tasks = [t if t.endswith("\n") else t + "\n" for t in tasks]
263	        encoded = tokenizer(
264	            tasks,
265	            padding="longest",
266	            max_length=max_length,
267	            truncation=True,
268	            return_tensors="pt",
269	        )
270	        batch["observation.language.tokens"] = encoded["input_ids"]
271	        batch["observation.language.attention_mask"] = encoded["attention_mask"].bool()
272	    elif "observation.language.tokens" not in batch:
273	        B = next(v.shape[0] for v in batch.values() if isinstance(v, torch.Tensor))
274	        batch["observation.language.tokens"] = torch.ones(B, 1, dtype=torch.long)
275	        batch["observation.language.attention_mask"] = torch.ones(B, 1, dtype=torch.bool)
276	
277	    for key in list(batch.keys()):
278	        if not isinstance(batch[key], torch.Tensor):
279	            del batch[key]
280	
281	    if device is not None:
282	        batch = {k: v.to(device) for k, v in batch.items()}
283	
284	    return batch
285	
286	
287	def wrap_with_imm(policy, config: Dict[str, Any]):
288	    """Wrap SmolVLAPolicy.model with IMMSmolVLAWrapper."""
289	    sys.path.insert(0, str(ARTIFACTS_DIR))
290	    from imm.smolvla_wrapper import IMMSmolVLAWrapper
291	
292	    imm_cfg = config["imm"]
293	    acis_cfg = config.get("acis", {})
294	
295	    imm_kwargs = {
296	        "lambda_margin": imm_cfg.get("lambda_margin", 0.1),
297	        "delta": imm_cfg.get("delta", 1.0),
298	        "warmup_steps": imm_cfg.get("warmup_steps", 1000),
299	        "temperature": imm_cfg.get("temperature", 1.0),
300	        "method": imm_cfg.get("soft_topk_method", "sigmoid"),
301	        "k_ratio": imm_cfg.get("k_ratio", 0.5),
302	    }
303	
304	    wrapper = IMMSmolVLAWrapper(
305	        smolvla_policy=policy,
306	        acis_config=acis_cfg,
307	        imm_config=imm_kwargs,
308	    )
309	    return wrapper
310	
311	
312	def save_checkpoint(
313	    model,
314	    optimizer,
315	    scheduler,
316	    step: int,
317	    config: Dict[str, Any],
318	    info: Optional[Dict] = None,
319	    output_dir: Optional[str] = None,
320	):
321	    """Save checkpoint. Non-fatal on failure."""
322	    if output_dir is None:
323	        output_dir = config["training"].get("output_dir", "checkpoints")
324	    ckpt_dir = Path(output_dir) / f"step_{step:06d}"
325	    try:
326	        ckpt_dir.mkdir(parents=True, exist_ok=True)
327	
328	        state = {
329	            "step": step,
330	            "model_state_dict": model.state_dict(),
331	            "optimizer_state_dict": optimizer.state_dict(),
332	            "scheduler_state_dict": scheduler.state_dict(),
333	            "config": config,
334	        }
335	        if info:
336	            state["margin_stats"] = {
337	                k: v.cpu() if isinstance(v, torch.Tensor) else v
338	                for k, v in info.items()
339	                if k in ("margin", "s_k", "s_k_plus_1", "lambda", "action_loss", "margin_loss")
340	            }
341	
342	        torch.save(state, ckpt_dir / "checkpoint.pt")
343	
344	        latest_link = Path(output_dir) / "latest"
345	        if latest_link.exists() or latest_link.is_symlink():
346	            latest_link.unlink()
347	        latest_link.symlink_to(ckpt_dir.name)
348	
349	        log.info("Checkpoint saved: %s", ckpt_dir)
350	    except Exception as e:
351	        log.warning("Failed to save checkpoint at step %d: %s", step, e)
352	
353	
354	def load_checkpoint(
355	    path: str,
356	    model,
357	    optimizer,
358	    scheduler,
359	    device: torch.device,
360	) -> int:
361	    """Load checkpoint and return the step to resume from."""
362	    ckpt_path = Path(path)
363	    if ckpt_path.is_dir():
364	        ckpt_path = ckpt_path / "checkpoint.pt"
365	
366	    log.info("Resuming from %s", ckpt_path)
367	    state = torch.load(ckpt_path, map_location=device, weights_only=False)
368	
369	    model.load_state_dict(state["model_state_dict"])
370	    optimizer.load_state_dict(state["optimizer_state_dict"])
371	    scheduler.load_state_dict(state["scheduler_state_dict"])
372	
373	    start_step = state["step"] + 1
374	    log.info("Resumed at step %d", start_step)
375	    return start_step
376	
377	
378	@torch.no_grad()
379	def evaluate(model, dataloader, step: int, config: Dict[str, Any], device: torch.device, imm_enabled: bool, tokenizer=None):
380	    """Run validation pass and return metrics dict."""
381	    sys.path.insert(0, str(ARTIFACTS_DIR))
382	    from imm.metrics import compute_margin, margin_statistics, topk_preservation_rate, l_eps_delta_ratio
383	
384	    model.eval()
385	    eval_cfg = config.get("evaluation", {})
386	    epsilons = eval_cfg.get("perturbations", [0.0, 0.01, 0.02, 0.05])
387	    pruning_ratio = eval_cfg.get("pruning_ratio", 0.5)
388	    max_batches = eval_cfg.get("max_eval_batches", 50)
389	
390	    results = {}
391	    total_action_loss = 0.0
392	    n_batches = 0
393	
394	    for batch_idx, batch in enumerate(dataloader):
395	        if batch_idx >= max_batches:
396	            break
397	        if tokenizer is not None:
398	            batch = preprocess_batch(batch, tokenizer, device=device)
399	        else:
400	            batch = {k: v.to(device) if isinstance(v, torch.Tensor) else v for k, v in batch.items()}
401	
402	        if imm_enabled:
403	            _, info = model(batch, step=step)
404	            total_action_loss += info["action_loss"].item()
405	
406	            scores = info["importance_scores"]
407	            k = info["k"]
408	
409	            for eps in epsilons:
410	                key = f"eps_{eps}"
411	                if key not in results:
412	                    results[key] = {"margins": [], "preservation": []}
413	
414	                if eps > 0:
415	                    batch_noisy = {k_: v.clone() if isinstance(v, torch.Tensor) else v for k_, v in batch.items()}
416	                    for img_key in [k_ for k_ in batch_noisy if "image" in k_.lower()]:
417	                        if isinstance(batch_noisy[img_key], torch.Tensor) and batch_noisy[img_key].is_floating_point():
418	                            batch_noisy[img_key] = (batch_noisy[img_key] + eps * torch.randn_like(batch_noisy[img_key])).clamp(0, 1)
419	                    _, info_noisy = model(batch_noisy, step=step)
420	                    scores_noisy = info_noisy["importance_scores"]
421	                else:
422	                    scores_noisy = scores
423	
424	                margin = compute_margin(scores, k)
425	                pres = topk_preservation_rate(scores, scores_noisy, k)
426	                results[key]["margins"].append(margin.cpu())
427	                results[key]["preservation"].append(pres.cpu())
428	        else:
429	            loss, info = model.forward_baseline(batch) if hasattr(model, "forward_baseline") else (model(batch), {})
430	            if isinstance(loss, tuple):
431	                loss = loss[0]
432	            total_action_loss += (info.get("action_loss", loss) if isinstance(info, dict) else loss).item()
433	
434	        n_batches += 1
435	
436	    metrics = {"eval/action_loss": total_action_loss / max(n_batches, 1)}
437	
438	    if imm_enabled:
439	        for eps_key, data in results.items():
440	            margins = torch.cat(data["margins"])
441	            pres = torch.cat(data["preservation"])
442	            metrics[f"eval/{eps_key}/margin_mean"] = margins.mean().item()
443	            metrics[f"eval/{eps_key}/margin_median"] = margins.median().item()
444	            metrics[f"eval/{eps_key}/margin_std"] = margins.std().item()
445	            metrics[f"eval/{eps_key}/preservation_rate"] = pres.mean().item()
446	
447	    model.train()
448	    return metrics
449	
450	
451	class GracefulExit:
452	    """Handle SIGINT/SIGTERM for graceful checkpoint saving."""
453	
454	    def __init__(self):
455	        self.should_exit = False
456	        signal.signal(signal.SIGINT, self._handler)
457	        signal.signal(signal.SIGTERM, self._handler)
458	
459	    def _handler(self, signum, frame):
460	        log.info("Received signal %d, will exit after current step", signum)
461	        self.should_exit = True
462	
463	
464	def main():
465	    args = parse_args()
466	    config = load_config(args.config)
467	    set_seed(args.seed)
468	
469	    device = torch.device(f"cuda:{args.gpu}" if torch.cuda.is_available() else "cpu")
470	    log.info("Device: %s", device)
471	
472	    train_cfg = config["training"]
473	    total_steps = train_cfg.get("total_steps", 30000)
474	    eval_every = train_cfg.get("eval_every", 2000)
475	    save_every = train_cfg.get("save_every", 5000)
476	    log_every = train_cfg.get("log_every", 50)
477	    grad_clip = train_cfg.get("grad_clip", 10.0)
478	
479	    imm_enabled = config.get("imm", {}).get("enabled", False)
480	
481	    output_dir = train_cfg.get("output_dir", f"checkpoints/{'imm' if imm_enabled else 'baseline'}")
482	    config["training"]["output_dir"] = output_dir
483	
484	    # Model
485	    log.info("Loading SmolVLA policy...")
486	    policy = load_smolvla_policy(config, device)
487	
488	    tokenizer = get_tokenizer_from_policy(policy)
489	
490	    if imm_enabled:
491	        log.info("Wrapping with IMMSmolVLAWrapper (delta=%.2f, lambda=%.2f)",
492	                 config["imm"].get("delta", 1.0), config["imm"].get("lambda_margin", 0.1))
493	        model = wrap_with_imm(policy, config)
494	        model.to(device)
495	    else:
496	        model = policy
497	
498	    # Dataset
499	    log.info("Loading dataset...")
500	    dataset = load_dataset(config)
501	    dataloader = make_dataloader(dataset, config)
502	    dataloader_iter = iter(dataloader)
503	
504	    eval_dataset = load_dataset(config)
505	    eval_dataloader = make_dataloader(eval_dataset, {**config, "training": {**train_cfg, "batch_size": train_cfg.get("eval_batch_size", train_cfg.get("batch_size", 4))}})
506	
507	    # Optimizer / Scheduler
508	    optimizer = make_optimizer(model, config)
509	    scheduler = make_scheduler(optimizer, config)
510	
511	    # Resume
512	    start_step = 0
513	    if args.resume:
514	        start_step = load_checkpoint(args.resume, model, optimizer, scheduler, device)
515	
516	    # W&B
517	    run_name = args.wandb_run or (f"{'imm' if imm_enabled else 'baseline'}_seed{args.seed}")
518	    wandb.init(project=args.wandb_project, name=run_name, config=config, resume="allow")
519	
520	    # Training loop
521	    graceful = GracefulExit()
522	    model.train()
523	    t0 = time.time()
524	    last_info = None
525	
526	    log.info("Starting training from step %d to %d", start_step, total_steps)
527	
528	    for step in range(start_step, total_steps):
529	        try:
530	            batch = next(dataloader_iter)
531	        except StopIteration:
532	            dataloader_iter = iter(dataloader)
533	            batch = next(dataloader_iter)
534	
535	        batch = preprocess_batch(batch, tokenizer, device=device)
536	
537	        if imm_enabled:
538	            total_loss, info = model(batch, step=step)
539	            last_info = info
540	        else:
541	            if hasattr(model, "forward_baseline"):
542	                total_loss, info = model.forward_baseline(batch)
543	                last_info = info
544	            else:
545	                output = model(batch)
546	                if isinstance(output, dict):
547	                    total_loss = output["loss"]
548	                    info = {"action_loss": total_loss.detach()}
549	                elif isinstance(output, tuple):
550	                    total_loss = output[0]
551	                    info = output[1] if len(output) > 1 else {"action_loss": total_loss.detach()}
552	                else:
553	                    total_loss = output
554	                    info = {"action_loss": total_loss.detach()}
555	                last_info = info
556	
557	        optimizer.zero_grad()
558	        total_loss.backward()
559	        grad_norm = torch.nn.utils.clip_grad_norm_(
560	            [p for p in model.parameters() if p.requires_grad], grad_clip
561	        )
562	        optimizer.step()
563	        scheduler.step()
564	
565	        # Logging
566	        if step % log_every == 0:
567	            log_dict = {
568	                "train/total_loss": total_loss.item(),
569	                "train/grad_norm": grad_norm.item() if isinstance(grad_norm, torch.Tensor) else grad_norm,
570	                "train/lr": optimizer.param_groups[0]["lr"],
571	                "train/step": step,
572	            }
573	
574	            if imm_enabled and isinstance(last_info, dict):
575	                log_dict.update({
576	                    "train/action_loss": last_info.get("action_loss", torch.tensor(0.0)).item(),
577	                    "train/margin_loss": last_info.get("margin_loss", torch.tensor(0.0)).item(),
578	                    "train/lambda": last_info.get("lambda", torch.tensor(0.0)).item(),
579	                })
580	                if "margin" in last_info:
581	                    margins = last_info["margin"]
582	                    log_dict.update({
583	                        "margin/mean": margins.mean().item(),
584	                        "margin/median": margins.median().item(),
585	                        "margin/std": margins.std().item(),
586	                        "margin/min": margins.min().item(),
587	                        "margin/max": margins.max().item(),
588	                    })
589	                    log_dict["margin/histogram"] = wandb.Histogram(margins.cpu().numpy())
590	                if "importance_scores" in last_info:
591	                    scores = last_info["importance_scores"]
592	                    k = last_info.get("k", int(scores.shape[1] * 0.5))
593	                    topk_vals, _ = torch.topk(scores, k, dim=-1)
594	                    log_dict["scores/topk_mean"] = topk_vals.mean().item()
595	                if "lipschitz_estimate" in last_info:
596	                    L = last_info["lipschitz_estimate"]
597	                    if "margin" in last_info:
598	                        eps_test = 0.01
599	                        k_val = last_info.get("k", 64)
600	                        ratio = L * eps_test * k_val / margins.clamp(min=1e-8)
601	                        log_dict["gate/L_eps_delta_ratio_mean"] = ratio.mean().item()
602	                        log_dict["gate/lipschitz_estimate"] = L
603	            else:
604	                if isinstance(last_info, dict) and "action_loss" in last_info:
605	                    log_dict["train/action_loss"] = last_info["action_loss"].item() if isinstance(last_info["action_loss"], torch.Tensor) else last_info["action_loss"]
606	
607	            wandb.log(log_dict, step=step)
608	
609	            elapsed = time.time() - t0
610	            steps_done = step - start_step + 1
611	            sps = steps_done / elapsed if elapsed > 0 else 0
612	            log.info(
613	                "step=%d/%d  loss=%.4f  lr=%.2e  grad=%.2f  sps=%.1f",
614	                step, total_steps, total_loss.item(),
615	                optimizer.param_groups[0]["lr"], grad_norm, sps,
616	            )
617	
618	        # Eval
619	        if step > 0 and step % eval_every == 0:
620	            log.info("Running evaluation at step %d...", step)
621	            eval_metrics = evaluate(model, eval_dataloader, step, config, device, imm_enabled, tokenizer=tokenizer)
622	            wandb.log(eval_metrics, step=step)
623	            for k, v in eval_metrics.items():
624	                log.info("  %s: %.4f", k, v)
625	
626	        # Checkpoint
627	        if step > 0 and step % save_every == 0:
628	            save_checkpoint(model, optimizer, scheduler, step, config, last_info, output_dir)
629	
630	        if graceful.should_exit:
631	            log.info("Graceful exit at step %d", step)
632	            save_checkpoint(model, optimizer, scheduler, step, config, last_info, output_dir)
633	            break
634	
635	    # Final checkpoint
636	    if not graceful.should_exit:
637	        save_checkpoint(model, optimizer, scheduler, total_steps - 1, config, last_info, output_dir)
638	
639	    wandb.finish()
640	    log.info("Training complete.")
641	
642	
643	if __name__ == "__main__":
644	    main()
645	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "263df5c0-d01d-4f96-a4cb-fd4145125851",
  "uuid": "df823bdd-35a2-4ead-b796-350c15748720",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/train.py",
      "content": "\"\"\"IMM Training Pipeline for SmolVLA + LIBERO.\n\nUsage:\n    python train.py --config configs/baseline.yaml\n    python train.py --config configs/imm_anchor.yaml\n    python train.py --config configs/imm_anchor.yaml --resume checkpoints/imm_anchor/latest\n\nTwo modes:\n  - Baseline: L_action only (flow matching MSE), no ACIS/margin loss.\n  - IMM: L_action + lambda * L_margin with ACIS scoring + token selection + warmup.\n\nDepends: lerobot, torch, wandb, peft.\n\"\"\"\n\nfrom __future__ import annotations\n\nimport argparse\nimport copy\nimport json\nimport logging\nimport os\nimport signal\nimport sys\nimport time\nfrom pathlib import Path\nfrom typing import Any, Dict, Optional\n\nimport torch\nimport torch.nn.functional as F\nimport wandb\nimport yaml\n\nlogging.basicConfig(\n    level=logging.INFO,\n    format=\"%(asctime)s [%(levelname)s] %(message)s\",\n    datefmt=\"%Y-%m-%d %H:%M:%S\",\n)\nlog = logging.getLogger(__name__)\n\nARTIFACTS_DIR = Path(__file__).resolve().parent\n\n\ndef parse_args():\n    parser = argparse.ArgumentParser(description=\"IMM training for SmolVLA on LIBERO\")\n    parser.add_argument(\"--config\", type=str, required=True, help=\"Path to YAML config file\")\n    parser.add_argument(\"--resume\", type=str, default=None, help=\"Path to checkpoint dir to resume from\")\n    parser.add_argument(\"--gpu\", type=int, default=0, help=\"GPU index (use CUDA_VISIBLE_DEVICES for physical mapping)\")\n    parser.add_argument(\"--seed\", type=int, default=42, help=\"Random seed\")\n    parser.add_argument(\"--wandb_project\", type=str, default=\"imm-vla-compress\", help=\"W&B project name\")\n    parser.add_argument(\"--wandb_run\", type=str, default=None, help=\"W&B run name (auto-generated if None)\")\n    return parser.parse_args()\n\n\ndef load_config(config_path: str) -> Dict[str, Any]:\n    \"\"\"Load YAML config with _base_ inheritance support.\"\"\"\n    config_path = Path(config_path)\n    with open(config_path) as f:\n        config = yaml.safe_load(f)\n\n    if \"_base_\" in config:\n        base_path = config_path.parent / config.pop(\"_base_\")\n        base_config = load_config(str(base_path))\n        base_config = deep_merge(base_config, config)\n        return base_config\n\n    return config\n\n\ndef deep_merge(base: Dict, override: Dict) -> Dict:\n    \"\"\"Recursively merge override into base.\"\"\"\n    result = copy.deepcopy(base)\n    for k, v in override.items():\n        if k in result and isinstance(result[k], dict) and isinstance(v, dict):\n            result[k] = deep_merge(result[k], v)\n        else:\n            result[k] = copy.deepcopy(v)\n    return result\n\n\ndef set_seed(seed: int):\n    import random\n    import numpy as np\n\n    random.seed(seed)\n    np.random.seed(seed)\n    torch.manual_seed(seed)\n    if torch.cuda.is_available():\n        torch.cuda.manual_seed_all(seed)\n\n\ndef _adapt_projections(policy, features: Dict[str, Any]):\n    \"\"\"Update SmolVLAConfig features for target dataset dimensions.\n\n    SmolVLA pads state/action to max_state_dim=32 / max_action_dim=32,\n    so projection layers (Linear(32,…)) stay unchanged. We only update\n    config.input_features and config.output_features so that:\n      - prepare_images picks up the correct camera keys\n      - action_feature.shape[0] returns the real action dim for loss trimming\n      - robot_state_feature.shape reflects the actual state dim\n    \"\"\"\n    from lerobot.configs.types import FeatureType, PolicyFeature\n\n    state_dim = features.get(\"state_dim\")\n    action_dim = features.get(\"action_dim\")\n    cameras = features.get(\"cameras\")\n\n    if state_dim is not None:\n        old_shape = None\n        if policy.config.input_features and \"observation.state\" in policy.config.input_features:\n            old_shape = policy.config.input_features[\"observation.state\"].shape\n        policy.config.input_features[\"observation.state\"] = PolicyFeature(\n            type=FeatureType.STATE, shape=(state_dim,)\n        )\n        log.info(\"Updated state feature shape: %s → (%d,)\", old_shape, state_dim)\n\n    if action_dim is not None:\n        old_shape = None\n        if policy.config.output_features and \"action\" in policy.config.output_features:\n            old_shape = policy.config.output_features[\"action\"].shape\n        policy.config.output_features[\"action\"] = PolicyFeature(\n            type=FeatureType.ACTION, shape=(action_dim,)\n        )\n        log.info(\"Updated action feature shape: %s → (%d,)\", old_shape, action_dim)\n\n    if cameras is not None:\n        old_cam_keys = [\n            k for k, v in policy.config.input_features.items()\n            if v.type == FeatureType.VISUAL\n        ]\n        for k in old_cam_keys:\n            del policy.config.input_features[k]\n        for cam_name in cameras:\n            policy.config.input_features[cam_name] = PolicyFeature(\n                type=FeatureType.VISUAL, shape=(3, 256, 256)\n            )\n        log.info(\"Updated cameras: %s → %s\", old_cam_keys, cameras)\n\n\ndef load_smolvla_policy(config: Dict[str, Any], device: torch.device):\n    \"\"\"Load SmolVLAPolicy via LeRobot API, adapt to dataset, and apply LoRA.\"\"\"\n    from lerobot.policies.smolvla.configuration_smolvla import SmolVLAConfig\n    from lerobot.policies.smolvla.modeling_smolvla import SmolVLAPolicy\n\n    model_cfg = config[\"model\"]\n    ds_cfg = config.get(\"dataset\", {})\n\n    pretrained_path = model_cfg.get(\"pretrained\")\n    if pretrained_path:\n        policy = SmolVLAPolicy.from_pretrained(pretrained_path)\n    else:\n        policy_config = SmolVLAConfig()\n        policy = SmolVLAPolicy(policy_config)\n\n    features = ds_cfg.get(\"features\", {})\n    if features:\n        _adapt_projections(policy, features)\n\n    lora_cfg = model_cfg.get(\"lora\", {})\n    if lora_cfg.get(\"rank\", 0) > 0:\n        from peft import LoraConfig, get_peft_model\n\n        peft_config = LoraConfig(\n            r=lora_cfg[\"rank\"],\n            lora_alpha=lora_cfg.get(\"alpha\", lora_cfg[\"rank\"] * 2),\n            lora_dropout=lora_cfg.get(\"dropout\", 0.05),\n            target_modules=lora_cfg.get(\n                \"target_modules_regex\",\n                r\"(model\\.vlm_with_expert\\.lm_expert\\..*\\.(q|v)_proj\"\n                r\"|model\\.(state_proj|action_in_proj|action_out_proj\"\n                r\"|action_time_mlp_in|action_time_mlp_out))\",\n            ),\n            bias=\"none\",\n        )\n        policy.model = get_peft_model(policy.model, peft_config)\n        log.info(\n            \"LoRA applied: rank=%d, alpha=%d, trainable params: %s\",\n            lora_cfg[\"rank\"],\n            peft_config.lora_alpha,\n            sum(p.numel() for p in policy.model.parameters() if p.requires_grad),\n        )\n\n    policy.to(device)\n    return policy\n\n\ndef load_dataset(config: Dict[str, Any]):\n    \"\"\"Load dataset via LeRobot API with delta_timestamps for action chunking.\"\"\"\n    from lerobot.datasets.lerobot_dataset import LeRobotDataset\n    from lerobot.datasets.dataset_metadata import LeRobotDatasetMetadata\n\n    ds_cfg = config[\"dataset\"]\n    repo_id = ds_cfg[\"repo_id\"]\n    chunk_size = 50  # SmolVLA default\n\n    meta = LeRobotDatasetMetadata(repo_id)\n    delta_timestamps = {\"action\": [i / meta.fps for i in range(chunk_size)]}\n\n    dataset = LeRobotDataset(\n        repo_id=repo_id,\n        episodes=ds_cfg.get(\"episodes\", None),\n        delta_timestamps=delta_timestamps,\n    )\n    return dataset\n\n\ndef make_dataloader(dataset, config: Dict[str, Any]):\n    from torch.utils.data import DataLoader\n\n    train_cfg = config[\"training\"]\n    return DataLoader(\n        dataset,\n        batch_size=train_cfg.get(\"batch_size\", 4),\n        shuffle=True,\n        num_workers=train_cfg.get(\"num_workers\", 4),\n        pin_memory=True,\n        drop_last=True,\n    )\n\n\ndef make_optimizer(model, config: Dict[str, Any]):\n    train_cfg = config[\"training\"]\n    params = [p for p in model.parameters() if p.requires_grad]\n    return torch.optim.AdamW(\n        params,\n        lr=train_cfg.get(\"lr\", 1e-4),\n        betas=tuple(train_cfg.get(\"betas\", [0.9, 0.95])),\n        weight_decay=train_cfg.get(\"weight_decay\", 1e-10),\n    )\n\n\ndef make_scheduler(optimizer, config: Dict[str, Any]):\n    from torch.optim.lr_scheduler import CosineAnnealingLR, LinearLR, SequentialLR\n\n    train_cfg = config[\"training\"]\n    warmup_steps = train_cfg.get(\"warmup_steps\", 1000)\n    total_steps = train_cfg.get(\"total_steps\", 30000)\n    decay_lr = train_cfg.get(\"decay_lr\", 2.5e-6)\n\n    warmup = LinearLR(optimizer, start_factor=1e-8, end_factor=1.0, total_iters=warmup_steps)\n    cosine = CosineAnnealingLR(optimizer, T_max=total_steps - warmup_steps, eta_min=decay_lr)\n    return SequentialLR(optimizer, schedulers=[warmup, cosine], milestones=[warmup_steps])\n\n\ndef get_tokenizer_from_policy(policy):\n    \"\"\"Extract tokenizer from SmolVLAPolicy, handling PeftModel wrapping.\"\"\"\n    model = policy.model\n    try:\n        from peft import PeftModel\n        if isinstance(model, PeftModel):\n            model = model.base_model.model\n    except ImportError:\n        pass\n    return model.vlm_with_expert.processor.tokenizer\n\n\ndef preprocess_batch(batch: Dict[str, Any], tokenizer, max_length: int = 48, device=None) -> Dict[str, Any]:\n    \"\"\"Tokenize task strings and move batch to device for SmolVLA.\"\"\"\n    tasks = batch.pop(\"task\", None)\n    if tasks is not None:\n        if isinstance(tasks, str):\n            tasks = [tasks]\n        tasks = [t if t.endswith(\"\\n\") else t + \"\\n\" for t in tasks]\n        encoded = tokenizer(\n            tasks,\n            padding=\"longest\",\n            max_length=max_length,\n            truncation=True,\n            return_tensors=\"pt\",\n        )\n        batch[\"observation.language.tokens\"] = encoded[\"input_ids\"]\n        batch[\"observation.language.attention_mask\"] = encoded[\"attention_mask\"].bool()\n    elif \"observation.language.tokens\" not in batch:\n        B = next(v.shape[0] for v in batch.values() if isinstance(v, torch.Tensor))\n        batch[\"observation.language.tokens\"] = torch.ones(B, 1, dtype=torch.long)\n        batch[\"observation.language.attention_mask\"] = torch.ones(B, 1, dtype=torch.bool)\n\n    for key in list(batch.keys()):\n        if not isinstance(batch[key], torch.Tensor):\n            del batch[key]\n\n    if device is not None:\n        batch = {k: v.to(device) for k, v in batch.items()}\n\n    return batch\n\n\ndef wrap_with_imm(policy, config: Dict[str, Any]):\n    \"\"\"Wrap SmolVLAPolicy.model with IMMSmolVLAWrapper.\"\"\"\n    sys.path.insert(0, str(ARTIFACTS_DIR))\n    from imm.smolvla_wrapper import IMMSmolVLAWrapper\n\n    imm_cfg = config[\"imm\"]\n    acis_cfg = config.get(\"acis\", {})\n\n    imm_kwargs = {\n        \"lambda_margin\": imm_cfg.get(\"lambda_margin\", 0.1),\n        \"delta\": imm_cfg.get(\"delta\", 1.0),\n        \"warmup_steps\": imm_cfg.get(\"warmup_steps\", 1000),\n        \"temperature\": imm_cfg.get(\"temperature\", 1.0),\n        \"method\": imm_cfg.get(\"soft_topk_method\", \"sigmoid\"),\n        \"k_ratio\": imm_cfg.get(\"k_ratio\", 0.5),\n    }\n\n    wrapper = IMMSmolVLAWrapper(\n        smolvla_policy=policy,\n        acis_config=acis_cfg,\n        imm_config=imm_kwargs,\n    )\n    return wrapper\n\n\ndef save_checkpoint(\n    model,\n    optimizer,\n    scheduler,\n    step: int,\n    config: Dict[str, Any],\n    info: Optional[Dict] = None,\n    output_dir: Optional[str] = None,\n):\n    \"\"\"Save checkpoint. Non-fatal on failure.\"\"\"\n    if output_dir is None:\n        output_dir = config[\"training\"].get(\"output_dir\", \"checkpoints\")\n    ckpt_dir = Path(output_dir) / f\"step_{step:06d}\"\n    try:\n        ckpt_dir.mkdir(parents=True, exist_ok=True)\n\n        state = {\n            \"step\": step,\n            \"model_state_dict\": model.state_dict(),\n            \"optimizer_state_dict\": optimizer.state_dict(),\n            \"scheduler_state_dict\": scheduler.state_dict(),\n            \"config\": config,\n        }\n        if info:\n            state[\"margin_stats\"] = {\n                k: v.cpu() if isinstance(v, torch.Tensor) else v\n                for k, v in info.items()\n                if k in (\"margin\", \"s_k\", \"s_k_plus_1\", \"lambda\", \"action_loss\", \"margin_loss\")\n            }\n\n        torch.save(state, ckpt_dir / \"checkpoint.pt\")\n\n        latest_link = Path(output_dir) / \"latest\"\n        if latest_link.exists() or latest_link.is_symlink():\n            latest_link.unlink()\n        latest_link.symlink_to(ckpt_dir.name)\n\n        log.info(\"Checkpoint saved: %s\", ckpt_dir)\n    except Exception as e:\n        log.warning(\"Failed to save checkpoint at step %d: %s\", step, e)\n\n\ndef load_checkpoint(\n    path: str,\n    model,\n    optimizer,\n    scheduler,\n    device: torch.device,\n) -> int:\n    \"\"\"Load checkpoint and return the step to resume from.\"\"\"\n    ckpt_path = Path(path)\n    if ckpt_path.is_dir():\n        ckpt_path = ckpt_path / \"checkpoint.pt\"\n\n    log.info(\"Resuming from %s\", ckpt_path)\n    state = torch.load(ckpt_path, map_location=device, weights_only=False)\n\n    model.load_state_dict(state[\"model_state_dict\"])\n    optimizer.load_state_dict(state[\"optimizer_state_dict\"])\n    scheduler.load_state_dict(state[\"scheduler_state_dict\"])\n\n    start_step = state[\"step\"] + 1\n    log.info(\"Resumed at step %d\", start_step)\n    return start_step\n\n\n@torch.no_grad()\ndef evaluate(model, dataloader, step: int, config: Dict[str, Any], device: torch.device, imm_enabled: bool, tokenizer=None):\n    \"\"\"Run validation pass and return metrics dict.\"\"\"\n    sys.path.insert(0, str(ARTIFACTS_DIR))\n    from imm.metrics import compute_margin, margin_statistics, topk_preservation_rate, l_eps_delta_ratio\n\n    model.eval()\n    eval_cfg = config.get(\"evaluation\", {})\n    epsilons = eval_cfg.get(\"perturbations\", [0.0, 0.01, 0.02, 0.05])\n    pruning_ratio = eval_cfg.get(\"pruning_ratio\", 0.5)\n    max_batches = eval_cfg.get(\"max_eval_batches\", 50)\n\n    results = {}\n    total_action_loss = 0.0\n    n_batches = 0\n\n    for batch_idx, batch in enumerate(dataloader):\n        if batch_idx >= max_batches:\n            break\n        if tokenizer is not None:\n            batch = preprocess_batch(batch, tokenizer, device=device)\n        else:\n            batch = {k: v.to(device) if isinstance(v, torch.Tensor) else v for k, v in batch.items()}\n\n        if imm_enabled:\n            _, info = model(batch, step=step)\n            total_action_loss += info[\"action_loss\"].item()\n\n            scores = info[\"importance_scores\"]\n            k = info[\"k\"]\n\n            for eps in epsilons:\n                key = f\"eps_{eps}\"\n                if key not in results:\n                    results[key] = {\"margins\": [], \"preservation\": []}\n\n                if eps > 0:\n                    batch_noisy = {k_: v.clone() if isinstance(v, torch.Tensor) else v for k_, v in batch.items()}\n                    for img_key in [k_ for k_ in batch_noisy if \"image\" in k_.lower()]:\n                        if isinstance(batch_noisy[img_key], torch.Tensor) and batch_noisy[img_key].is_floating_point():\n                            batch_noisy[img_key] = (batch_noisy[img_key] + eps * torch.randn_like(batch_noisy[img_key])).clamp(0, 1)\n                    _, info_noisy = model(batch_noisy, step=step)\n                    scores_noisy = info_noisy[\"importance_scores\"]\n                else:\n                    scores_noisy = scores\n\n                margin = compute_margin(scores, k)\n                pres = topk_preservation_rate(scores, scores_noisy, k)\n                results[key][\"margins\"].append(margin.cpu())\n                results[key][\"preservation\"].append(pres.cpu())\n        else:\n            loss, info = model.forward_baseline(batch) if hasattr(model, \"forward_baseline\") else (model(batch), {})\n            if isinstance(loss, tuple):\n                loss = loss[0]\n            total_action_loss += (info.get(\"action_loss\", loss) if isinstance(info, dict) else loss).item()\n\n        n_batches += 1\n\n    metrics = {\"eval/action_loss\": total_action_loss / max(n_batches, 1)}\n\n    if imm_enabled:\n        for eps_key, data in results.items():\n            margins = torch.cat(data[\"margins\"])\n            pres = torch.cat(data[\"preservation\"])\n            metrics[f\"eval/{eps_key}/margin_mean\"] = margins.mean().item()\n            metrics[f\"eval/{eps_key}/margin_median\"] = margins.median().item()\n            metrics[f\"eval/{eps_key}/margin_std\"] = margins.std().item()\n            metrics[f\"eval/{eps_key}/preservation_rate\"] = pres.mean().item()\n\n    model.train()\n    return metrics\n\n\nclass GracefulExit:\n    \"\"\"Handle SIGINT/SIGTERM for graceful checkpoint saving.\"\"\"\n\n    def __init__(self):\n        self.should_exit = False\n        signal.signal(signal.SIGINT, self._handler)\n        signal.signal(signal.SIGTERM, self._handler)\n\n    def _handler(self, signum, frame):\n        log.info(\"Received signal %d, will exit after current step\", signum)\n        self.should_exit = True\n\n\ndef main():\n    args = parse_args()\n    config = load_config(args.config)\n    set_seed(args.seed)\n\n    device = torch.device(f\"cuda:{args.gpu}\" if torch.cuda.is_available() else \"cpu\")\n    log.info(\"Device: %s\", device)\n\n    train_cfg = config[\"training\"]\n    total_steps = train_cfg.get(\"total_steps\", 30000)\n    eval_every = train_cfg.get(\"eval_every\", 2000)\n    save_every = train_cfg.get(\"save_every\", 5000)\n    log_every = train_cfg.get(\"log_every\", 50)\n    grad_clip = train_cfg.get(\"grad_clip\", 10.0)\n\n    imm_enabled = config.get(\"imm\", {}).get(\"enabled\", False)\n\n    output_dir = train_cfg.get(\"output_dir\", f\"checkpoints/{'imm' if imm_enabled else 'baseline'}\")\n    config[\"training\"][\"output_dir\"] = output_dir\n\n    # Model\n    log.info(\"Loading SmolVLA policy...\")\n    policy = load_smolvla_policy(config, device)\n\n    tokenizer = get_tokenizer_from_policy(policy)\n\n    if imm_enabled:\n        log.info(\"Wrapping with IMMSmolVLAWrapper (delta=%.2f, lambda=%.2f)\",\n                 config[\"imm\"].get(\"delta\", 1.0), config[\"imm\"].get(\"lambda_margin\", 0.1))\n        model = wrap_with_imm(policy, config)\n        model.to(device)\n    else:\n        model = policy\n\n    # Dataset\n    log.info(\"Loading dataset...\")\n    dataset = load_dataset(config)\n    dataloader = make_dataloader(dataset, config)\n    dataloader_iter = iter(dataloader)\n\n    eval_dataset = load_dataset(config)\n    eval_dataloader = make_dataloader(eval_dataset, {**config, \"training\": {**train_cfg, \"batch_size\": train_cfg.get(\"eval_batch_size\", train_cfg.get(\"batch_size\", 4))}})\n\n    # Optimizer / Scheduler\n    optimizer = make_optimizer(model, config)\n    scheduler = make_scheduler(optimizer, config)\n\n    # Resume\n    start_step = 0\n    if args.resume:\n        start_step = load_checkpoint(args.resume, model, optimizer, scheduler, device)\n\n    # W&B\n    run_name = args.wandb_run or (f\"{'imm' if imm_enabled else 'baseline'}_seed{args.seed}\")\n    wandb.init(project=args.wandb_project, name=run_name, config=config, resume=\"allow\")\n\n    # Training loop\n    graceful = GracefulExit()\n    model.train()\n    t0 = time.time()\n    last_info = None\n\n    log.info(\"Starting training from step %d to %d\", start_step, total_steps)\n\n    for step in range(start_step, total_steps):\n        try:\n            batch = next(dataloader_iter)\n        except StopIteration:\n            dataloader_iter = iter(dataloader)\n            batch = next(dataloader_iter)\n\n        batch = preprocess_batch(batch, tokenizer, device=device)\n\n        if imm_enabled:\n            total_loss, info = model(batch, step=step)\n            last_info = info\n        else:\n            if hasattr(model, \"forward_baseline\"):\n                total_loss, info = model.forward_baseline(batch)\n                last_info = info\n            else:\n                output = model(batch)\n                if isinstance(output, dict):\n                    total_loss = output[\"loss\"]\n                    info = {\"action_loss\": total_loss.detach()}\n                elif isinstance(output, tuple):\n                    total_loss = output[0]\n                    info = output[1] if len(output) > 1 else {\"action_loss\": total_loss.detach()}\n                else:\n                    total_loss = output\n                    info = {\"action_loss\": total_loss.detach()}\n                last_info = info\n\n        optimizer.zero_grad()\n        total_loss.backward()\n        grad_norm = torch.nn.utils.clip_grad_norm_(\n            [p for p in model.parameters() if p.requires_grad], grad_clip\n        )\n        optimizer.step()\n        scheduler.step()\n\n        # Logging\n        if step % log_every == 0:\n            log_dict = {\n                \"train/total_loss\": total_loss.item(),\n                \"train/grad_norm\": grad_norm.item() if isinstance(grad_norm, torch.Tensor) else grad_norm,\n                \"train/lr\": optimizer.param_groups[0][\"lr\"],\n                \"train/step\": step,\n            }\n\n            if imm_enabled and isinstance(last_info, dict):\n                log_dict.update({\n                    \"train/action_loss\": last_info.get(\"action_loss\", torch.tensor(0.0)).item(),\n                    \"train/margin_loss\": last_info.get(\"margin_loss\", torch.tensor(0.0)).item(),\n                    \"train/lambda\": last_info.get(\"lambda\", torch.tensor(0.0)).item(),\n                })\n                if \"margin\" in last_info:\n                    margins = last_info[\"margin\"]\n                    log_dict.update({\n                        \"margin/mean\": margins.mean().item(),\n                        \"margin/median\": margins.median().item(),\n                        \"margin/std\": margins.std().item(),\n                        \"margin/min\": margins.min().item(),\n                        \"margin/max\": margins.max().item(),\n                    })\n                    log_dict[\"margin/histogram\"] = wandb.Histogram(margins.cpu().numpy())\n                if \"importance_scores\" in last_info:\n                    scores = last_info[\"importance_scores\"]\n                    k = last_info.get(\"k\", int(scores.shape[1] * 0.5))\n                    topk_vals, _ = torch.topk(scores, k, dim=-1)\n                    log_dict[\"scores/topk_mean\"] = topk_vals.mean().item()\n                if \"lipschitz_estimate\" in last_info:\n                    L = last_info[\"lipschitz_estimate\"]\n                    if \"margin\" in last_info:\n                        eps_test = 0.01\n                        k_val = last_info.get(\"k\", 64)\n                        ratio = L * eps_test * k_val / margins.clamp(min=1e-8)\n                        log_dict[\"gate/L_eps_delta_ratio_mean\"] = ratio.mean().item()\n                        log_dict[\"gate/lipschitz_estimate\"] = L\n            else:\n                if isinstance(last_info, dict) and \"action_loss\" in last_info:\n                    log_dict[\"train/action_loss\"] = last_info[\"action_loss\"].item() if isinstance(last_info[\"action_loss\"], torch.Tensor) else last_info[\"action_loss\"]\n\n            wandb.log(log_dict, step=step)\n\n            elapsed = time.time() - t0\n            steps_done = step - start_step + 1\n            sps = steps_done / elapsed if elapsed > 0 else 0\n            log.info(\n                \"step=%d/%d  loss=%.4f  lr=%.2e  grad=%.2f  sps=%.1f\",\n                step, total_steps, total_loss.item(),\n                optimizer.param_groups[0][\"lr\"], grad_norm, sps,\n            )\n\n        # Eval\n        if step > 0 and step % eval_every == 0:\n            log.info(\"Running evaluation at step %d...\", step)\n            eval_metrics = evaluate(model, eval_dataloader, step, config, device, imm_enabled, tokenizer=tokenizer)\n            wandb.log(eval_metrics, step=step)\n            for k, v in eval_metrics.items():\n                log.info(\"  %s: %.4f\", k, v)\n\n        # Checkpoint\n        if step > 0 and step % save_every == 0:\n            save_checkpoint(model, optimizer, scheduler, step, config, last_info, output_dir)\n\n        if graceful.should_exit:\n            log.info(\"Graceful exit at step %d\", step)\n            save_checkpoint(model, optimizer, scheduler, step, config, last_info, output_dir)\n            break\n\n    # Final checkpoint\n    if not graceful.should_exit:\n        save_checkpoint(model, optimizer, scheduler, total_steps - 1, config, last_info, output_dir)\n\n    wandb.finish()\n    log.info(\"Training complete.\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 645,
      "startLine": 1,
      "totalLines": 645
    }
  }
}
```

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — Read · `toolu_0193kgRmE1VuPKgZ13mov4vb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/evaluate.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "263df5c0-d01d-4f96-a4cb-fd4145125851",
  "uuid": "b0b8c3eb-b922-4382-a64f-c34277427a13",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P8fJNFF5YAX1pYssBKZQrR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 870,
      "cache_read_input_tokens": 26972,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 870
      },
      "output_tokens": 18,
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

_source line 14 · 2026-05-15T13:41:14.687Z_

<details><summary>↩ Tool result · `toolu_0193kgRmE1VuPKgZ13mov4vb`</summary>

```text
1	"""IMM Evaluation Pipeline.
2	
3	Evaluates trained models under:
4	  - Clean vs perturbed inputs (Gaussian noise eps in {0.01, 0.02, 0.05})
5	  - With/without ACIS-based 50% token pruning
6	  - Metrics: margin stats, top-k preservation rate, L*eps/Delta_k, Kendall tau, certified bound
7	
8	Usage:
9	    python evaluate.py --checkpoint path/to/ckpt --config configs/imm_anchor.yaml --gpu 0
10	    python evaluate.py --checkpoint path/to/baseline --config configs/baseline.yaml --output results/baseline.json
11	
12	Depends: lerobot, torch, imm.
13	"""
14	
15	from __future__ import annotations
16	
17	import argparse
18	import json
19	import logging
20	import sys
21	from pathlib import Path
22	from typing import Any, Dict, List
23	
24	import torch
25	import torch.nn.functional as F
26	import yaml
27	
28	ARTIFACTS_DIR = Path(__file__).resolve().parent
29	sys.path.insert(0, str(ARTIFACTS_DIR))
30	
31	from imm.metrics import (
32	    certified_bound,
33	    compute_empirical_lipschitz,
34	    compute_margin,
35	    kendall_tau_distance,
36	    l_eps_delta_ratio,
37	    margin_statistics,
38	    topk_preservation_rate,
39	)
40	
41	logging.basicConfig(
42	    level=logging.INFO,
43	    format="%(asctime)s [%(levelname)s] %(message)s",
44	    datefmt="%Y-%m-%d %H:%M:%S",
45	)
46	log = logging.getLogger(__name__)
47	
48	
49	def parse_args():
50	    parser = argparse.ArgumentParser(description="IMM evaluation for SmolVLA on LIBERO")
51	    parser.add_argument("--checkpoint", type=str, required=True, help="Path to checkpoint file or directory")
52	    parser.add_argument("--config", type=str, required=True, help="Path to YAML config file")
53	    parser.add_argument("--gpu", type=int, default=0, help="GPU index")
54	    parser.add_argument("--output", type=str, default=None, help="Path to save results JSON (default: results/&lt;run>.json)")
55	    parser.add_argument("--max_batches", type=int, default=100, help="Max batches to evaluate")
56	    parser.add_argument("--lipschitz_samples", type=int, default=100, help="Samples for empirical Lipschitz estimation")
57	    parser.add_argument("--seed", type=int, default=42, help="Random seed")
58	    return parser.parse_args()
59	
60	
61	def load_config(config_path: str) -> Dict[str, Any]:
62	    """Load YAML config with _base_ inheritance."""
63	    import copy
64	    config_path = Path(config_path)
65	    with open(config_path) as f:
66	        config = yaml.safe_load(f)
67	    if "_base_" in config:
68	        base_path = config_path.parent / config.pop("_base_")
69	        base_config = load_config(str(base_path))
70	        for k, v in config.items():
71	            if k in base_config and isinstance(base_config[k], dict) and isinstance(v, dict):
72	                base_config[k].update(v)
73	            else:
74	                base_config[k] = v
75	        return base_config
76	    return config
77	
78	
79	def load_model_and_checkpoint(config: Dict[str, Any], checkpoint_path: str, device: torch.device):
80	    """Load SmolVLA policy, optionally wrap with IMM, then load checkpoint weights."""
81	    from train import load_smolvla_policy, wrap_with_imm
82	
83	    policy = load_smolvla_policy(config, device)
84	    imm_enabled = config.get("imm", {}).get("enabled", False)
85	
86	    if imm_enabled:
87	        model = wrap_with_imm(policy, config)
88	        model.to(device)
89	    else:
90	        model = policy
91	
92	    ckpt_path = Path(checkpoint_path)
93	    if ckpt_path.is_dir():
94	        ckpt_path = ckpt_path / "checkpoint.pt"
95	
96	    log.info("Loading checkpoint from %s", ckpt_path)
97	    state = torch.load(ckpt_path, map_location=device, weights_only=False)
98	    model.load_state_dict(state["model_state_dict"], strict=False)
99	
100	    model.eval()
101	    return model, imm_enabled
102	
103	
104	def compute_importance_scores(model, batch: Dict[str, torch.Tensor], imm_enabled: bool):
105	    """Extract ACIS importance scores from the model.
106	
107	    Returns (scores, k) or (None, None) for baseline models.
108	    Uses the wrapper's compute_importance_scores() which handles batch
109	    preprocessing and visual token extraction via the real lerobot API.
110	    """
111	    if not imm_enabled:
112	        return None, None
113	
114	    return model.compute_importance_scores(batch)
115	
116	
117	def perturb_images(batch: Dict[str, torch.Tensor], epsilon: float) -> Dict[str, torch.Tensor]:
118	    """Add Gaussian noise to image tensors in batch."""
119	    batch_noisy = {}
120	    for key, val in batch.items():
121	        if isinstance(val, torch.Tensor) and "image" in key.lower() and val.is_floating_point():
122	            batch_noisy[key] = (val + epsilon * torch.randn_like(val)).clamp(0, 1)
123	        else:
124	            batch_noisy[key] = val
125	    return batch_noisy
126	
127	
128	def estimate_lipschitz(model, dataloader, device: torch.device, max_batches: int = 10, num_samples: int = 100) -> float:
129	    """Estimate empirical Lipschitz constant of ACIS scorer.
130	
131	    Uses the wrapper's policy.prepare_* methods and base_model for correct
132	    visual token extraction and suffix embedding.
133	    """
134	    if not hasattr(model, "acis"):
135	        return 0.0
136	
137	    bm = model.base_model
138	
139	    L_max = 0.0
140	    for batch_idx, batch in enumerate(dataloader):
141	        if batch_idx >= max_batches:
142	            break
143	        batch = {k: v.to(device) if isinstance(v, torch.Tensor) else v for k, v in batch.items()}
144	
145	        images, _ = model.policy.prepare_images(batch)
146	        vis_tokens, _ = model._get_visual_tokens(images)
147	
148	        actions = model.policy.prepare_action(batch)
149	        B = actions.shape[0]
150	        noise = bm.sample_noise(actions.shape, actions.device)
151	        time = bm.sample_time(B, actions.device)
152	        time_expanded = time[:, None, None]
153	        x_t = time_expanded * noise + (1 - time_expanded) * actions
154	
155	        a_query, _, _ = bm.embed_suffix(x_t, time)
156	
157	        L = compute_empirical_lipschitz(
158	            model.acis, vis_tokens, a_query,
159	            num_samples=num_samples, epsilon=0.001,
160	        )
161	        L_max = max(L_max, L)
162	
163	    log.info("Empirical Lipschitz constant: %.4f", L_max)
164	    return L_max
165	
166	
167	@torch.no_grad()
168	def evaluate_full(
169	    model,
170	    dataloader,
171	    config: Dict[str, Any],
172	    device: torch.device,
173	    imm_enabled: bool,
174	    lipschitz_const: float,
175	    max_batches: int = 100,
176	):
177	    """Full evaluation matrix: 4 noise levels x 2 pruning modes = 8 conditions."""
178	    eval_cfg = config.get("evaluation", {})
179	    epsilons = eval_cfg.get("perturbations", [0.0, 0.01, 0.02, 0.05])
180	    pruning_ratio = eval_cfg.get("pruning_ratio", 0.5)
181	
182	    results = {}
183	    action_losses = []
184	
185	    for epsilon in epsilons:
186	        for pruning in [False, True]:
187	            condition = f"eps{epsilon}_prune{pruning}"
188	            log.info("Evaluating condition: %s", condition)
189	
190	            all_margins = []
191	            all_preservation = []
192	            all_kendall = []
193	            all_certified = []
194	            all_led_ratio = []
195	            all_action_loss = []
196	
197	            for batch_idx, batch in enumerate(dataloader):
198	                if batch_idx >= max_batches:
199	                    break
200	                batch = {k: v.to(device) if isinstance(v, torch.Tensor) else v for k, v in batch.items()}
201	
202	                # Clean scores
203	                scores_clean, k = compute_importance_scores(model, batch, imm_enabled)
204	
205	                if not imm_enabled:
206	                    if hasattr(model, "forward_baseline"):
207	                        loss, info = model.forward_baseline(batch)
208	                    else:
209	                        output = model(batch)
210	                        loss = output["loss"] if isinstance(output, dict) else (output[0] if isinstance(output, tuple) else output)
211	                        info = {}
212	                    loss_val = info.get("action_loss", loss)
213	                    all_action_loss.append(loss_val.item() if isinstance(loss_val, torch.Tensor) else loss_val)
214	                    continue
215	
216	                # Perturbed batch
217	                if epsilon > 0:
218	                    batch_noisy = perturb_images(batch, epsilon)
219	                    scores_pert, _ = compute_importance_scores(model, batch_noisy, imm_enabled)
220	                else:
221	                    scores_pert = scores_clean
222	
223	                # Metrics
224	                margin = compute_margin(scores_clean, k)
225	                pres = topk_preservation_rate(scores_clean, scores_pert, k)
226	                kendall = kendall_tau_distance(scores_clean, scores_pert, k)
227	                cert = certified_bound(margin, lipschitz_const, max(epsilon, 0.01), k)
228	                led = l_eps_delta_ratio(lipschitz_const, max(epsilon, 0.01), margin, k)
229	
230	                all_margins.append(margin.cpu())
231	                all_preservation.append(pres.cpu())
232	                all_kendall.append(kendall.cpu())
233	                all_certified.append(cert.cpu())
234	                all_led_ratio.append(led.cpu())
235	
236	                # Action loss under this condition
237	                if pruning:
238	                    model.train(False)
239	                    eval_batch = batch_noisy if epsilon > 0 else batch
240	                    _, info = model(eval_batch, step=0)
241	                    all_action_loss.append(info["action_loss"].item())
242	                else:
243	                    _, info = model(batch if epsilon == 0 else perturb_images(batch, epsilon), step=0)
244	                    all_action_loss.append(info["action_loss"].item())
245	
246	            cond_results = {
247	                "action_loss": sum(all_action_loss) / max(len(all_action_loss), 1),
248	            }
249	
250	            if imm_enabled and all_margins:
251	                margins_cat = torch.cat(all_margins)
252	                pres_cat = torch.cat(all_preservation)
253	                kendall_cat = torch.cat(all_kendall)
254	                cert_cat = torch.cat(all_certified)
255	                led_cat = torch.cat(all_led_ratio)
256	
257	                cond_results.update({
258	                    "margin_mean": margins_cat.mean().item(),
259	                    "margin_median": margins_cat.median().item(),
260	                    "margin_std": margins_cat.std().item(),
261	                    "margin_min": margins_cat.min().item(),
262	                    "margin_max": margins_cat.max().item(),
263	                    "preservation_rate": pres_cat.mean().item(),
264	                    "kendall_tau": kendall_cat.mean().item(),
265	                    "certified_bound_mean": cert_cat.mean().item(),
266	                    "certified_bound_max": cert_cat.max().item(),
267	                    "l_eps_delta_ratio_mean": led_cat.mean().item(),
268	                    "l_eps_delta_ratio_median": led_cat.median().item(),
269	                })
270	
271	            results[condition] = cond_results
272	            log.info("  %s: %s", condition, {k: f"{v:.4f}" for k, v in cond_results.items()})
273	
274	    return results
275	
276	
277	def main():
278	    args = parse_args()
279	
280	    import numpy as np
281	    import random
282	    random.seed(args.seed)
283	    np.random.seed(args.seed)
284	    torch.manual_seed(args.seed)
285	
286	    config = load_config(args.config)
287	    device = torch.device(f"cuda:{args.gpu}" if torch.cuda.is_available() else "cpu")
288	
289	    model, imm_enabled = load_model_and_checkpoint(config, args.checkpoint, device)
290	
291	    from train import load_dataset, make_dataloader
292	    dataset = load_dataset(config)
293	    dataloader = make_dataloader(dataset, {
294	        **config,
295	        "training": {**config.get("training", {}), "batch_size": config.get("training", {}).get("eval_batch_size", 4)},
296	    })
297	
298	    # Lipschitz estimation
299	    lipschitz_const = 0.0
300	    spectral_lipschitz = 0.0
301	    if imm_enabled and hasattr(model, "acis"):
302	        spectral_lipschitz = model.acis.get_lipschitz_estimate()
303	        log.info("Spectral Lipschitz estimate: %.4f", spectral_lipschitz)
304	        lipschitz_const = estimate_lipschitz(model, dataloader, device, max_batches=10, num_samples=args.lipschitz_samples)
305	
306	    results = evaluate_full(model, dataloader, config, device, imm_enabled, lipschitz_const, max_batches=args.max_batches)
307	
308	    results["_meta"] = {
309	        "checkpoint": args.checkpoint,
310	        "config": args.config,
311	        "imm_enabled": imm_enabled,
312	        "lipschitz_empirical": lipschitz_const,
313	        "lipschitz_spectral": spectral_lipschitz,
314	        "max_batches": args.max_batches,
315	        "seed": args.seed,
316	    }
317	
318	    # Summary: compare clean vs perturbed L*eps/Delta_k ratio
319	    if imm_enabled:
320	        clean_key = "eps0.0_pruneFalse"
321	        if clean_key in results and "l_eps_delta_ratio_mean" in results.get(clean_key, {}):
322	            log.info("=== Gate Metric Summary ===")
323	            for cond, data in results.items():
324	                if cond.startswith("_"):
325	                    continue
326	                led = data.get("l_eps_delta_ratio_mean", float("nan"))
327	                pres = data.get("preservation_rate", float("nan"))
328	                log.info("  %s: L*eps*k/Delta_k=%.4f, preservation=%.4f", cond, led, pres)
329	
330	    # Save results
331	    output_path = args.output
332	    if output_path is None:
333	        results_dir = Path("results")
334	        results_dir.mkdir(exist_ok=True)
335	        ckpt_name = Path(args.checkpoint).stem
336	        output_path = results_dir / f"eval_{ckpt_name}.json"
337	    else:
338	        output_path = Path(output_path)
339	        output_path.parent.mkdir(parents=True, exist_ok=True)
340	
341	    with open(output_path, "w") as f:
342	        json.dump(results, f, indent=2, default=str)
343	    log.info("Results saved to %s", output_path)
344	
345	
346	if __name__ == "__main__":
347	    main()
348	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "263df5c0-d01d-4f96-a4cb-fd4145125851",
  "uuid": "76aa976e-86a2-41ad-b7fc-727f48d6495d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/evaluate.py",
      "content": "\"\"\"IMM Evaluation Pipeline.\n\nEvaluates trained models under:\n  - Clean vs perturbed inputs (Gaussian noise eps in {0.01, 0.02, 0.05})\n  - With/without ACIS-based 50% token pruning\n  - Metrics: margin stats, top-k preservation rate, L*eps/Delta_k, Kendall tau, certified bound\n\nUsage:\n    python evaluate.py --checkpoint path/to/ckpt --config configs/imm_anchor.yaml --gpu 0\n    python evaluate.py --checkpoint path/to/baseline --config configs/baseline.yaml --output results/baseline.json\n\nDepends: lerobot, torch, imm.\n\"\"\"\n\nfrom __future__ import annotations\n\nimport argparse\nimport json\nimport logging\nimport sys\nfrom pathlib import Path\nfrom typing import Any, Dict, List\n\nimport torch\nimport torch.nn.functional as F\nimport yaml\n\nARTIFACTS_DIR = Path(__file__).resolve().parent\nsys.path.insert(0, str(ARTIFACTS_DIR))\n\nfrom imm.metrics import (\n    certified_bound,\n    compute_empirical_lipschitz,\n    compute_margin,\n    kendall_tau_distance,\n    l_eps_delta_ratio,\n    margin_statistics,\n    topk_preservation_rate,\n)\n\nlogging.basicConfig(\n    level=logging.INFO,\n    format=\"%(asctime)s [%(levelname)s] %(message)s\",\n    datefmt=\"%Y-%m-%d %H:%M:%S\",\n)\nlog = logging.getLogger(__name__)\n\n\ndef parse_args():\n    parser = argparse.ArgumentParser(description=\"IMM evaluation for SmolVLA on LIBERO\")\n    parser.add_argument(\"--checkpoint\", type=str, required=True, help=\"Path to checkpoint file or directory\")\n    parser.add_argument(\"--config\", type=str, required=True, help=\"Path to YAML config file\")\n    parser.add_argument(\"--gpu\", type=int, default=0, help=\"GPU index\")\n    parser.add_argument(\"--output\", type=str, default=None, help=\"Path to save results JSON (default: results/&lt;run>.json)\")\n    parser.add_argument(\"--max_batches\", type=int, default=100, help=\"Max batches to evaluate\")\n    parser.add_argument(\"--lipschitz_samples\", type=int, default=100, help=\"Samples for empirical Lipschitz estimation\")\n    parser.add_argument(\"--seed\", type=int, default=42, help=\"Random seed\")\n    return parser.parse_args()\n\n\ndef load_config(config_path: str) -> Dict[str, Any]:\n    \"\"\"Load YAML config with _base_ inheritance.\"\"\"\n    import copy\n    config_path = Path(config_path)\n    with open(config_path) as f:\n        config = yaml.safe_load(f)\n    if \"_base_\" in config:\n        base_path = config_path.parent / config.pop(\"_base_\")\n        base_config = load_config(str(base_path))\n        for k, v in config.items():\n            if k in base_config and isinstance(base_config[k], dict) and isinstance(v, dict):\n                base_config[k].update(v)\n            else:\n                base_config[k] = v\n        return base_config\n    return config\n\n\ndef load_model_and_checkpoint(config: Dict[str, Any], checkpoint_path: str, device: torch.device):\n    \"\"\"Load SmolVLA policy, optionally wrap with IMM, then load checkpoint weights.\"\"\"\n    from train import load_smolvla_policy, wrap_with_imm\n\n    policy = load_smolvla_policy(config, device)\n    imm_enabled = config.get(\"imm\", {}).get(\"enabled\", False)\n\n    if imm_enabled:\n        model = wrap_with_imm(policy, config)\n        model.to(device)\n    else:\n        model = policy\n\n    ckpt_path = Path(checkpoint_path)\n    if ckpt_path.is_dir():\n        ckpt_path = ckpt_path / \"checkpoint.pt\"\n\n    log.info(\"Loading checkpoint from %s\", ckpt_path)\n    state = torch.load(ckpt_path, map_location=device, weights_only=False)\n    model.load_state_dict(state[\"model_state_dict\"], strict=False)\n\n    model.eval()\n    return model, imm_enabled\n\n\ndef compute_importance_scores(model, batch: Dict[str, torch.Tensor], imm_enabled: bool):\n    \"\"\"Extract ACIS importance scores from the model.\n\n    Returns (scores, k) or (None, None) for baseline models.\n    Uses the wrapper's compute_importance_scores() which handles batch\n    preprocessing and visual token extraction via the real lerobot API.\n    \"\"\"\n    if not imm_enabled:\n        return None, None\n\n    return model.compute_importance_scores(batch)\n\n\ndef perturb_images(batch: Dict[str, torch.Tensor], epsilon: float) -> Dict[str, torch.Tensor]:\n    \"\"\"Add Gaussian noise to image tensors in batch.\"\"\"\n    batch_noisy = {}\n    for key, val in batch.items():\n        if isinstance(val, torch.Tensor) and \"image\" in key.lower() and val.is_floating_point():\n            batch_noisy[key] = (val + epsilon * torch.randn_like(val)).clamp(0, 1)\n        else:\n            batch_noisy[key] = val\n    return batch_noisy\n\n\ndef estimate_lipschitz(model, dataloader, device: torch.device, max_batches: int = 10, num_samples: int = 100) -> float:\n    \"\"\"Estimate empirical Lipschitz constant of ACIS scorer.\n\n    Uses the wrapper's policy.prepare_* methods and base_model for correct\n    visual token extraction and suffix embedding.\n    \"\"\"\n    if not hasattr(model, \"acis\"):\n        return 0.0\n\n    bm = model.base_model\n\n    L_max = 0.0\n    for batch_idx, batch in enumerate(dataloader):\n        if batch_idx >= max_batches:\n            break\n        batch = {k: v.to(device) if isinstance(v, torch.Tensor) else v for k, v in batch.items()}\n\n        images, _ = model.policy.prepare_images(batch)\n        vis_tokens, _ = model._get_visual_tokens(images)\n\n        actions = model.policy.prepare_action(batch)\n        B = actions.shape[0]\n        noise = bm.sample_noise(actions.shape, actions.device)\n        time = bm.sample_time(B, actions.device)\n        time_expanded = time[:, None, None]\n        x_t = time_expanded * noise + (1 - time_expanded) * actions\n\n        a_query, _, _ = bm.embed_suffix(x_t, time)\n\n        L = compute_empirical_lipschitz(\n            model.acis, vis_tokens, a_query,\n            num_samples=num_samples, epsilon=0.001,\n        )\n        L_max = max(L_max, L)\n\n    log.info(\"Empirical Lipschitz constant: %.4f\", L_max)\n    return L_max\n\n\n@torch.no_grad()\ndef evaluate_full(\n    model,\n    dataloader,\n    config: Dict[str, Any],\n    device: torch.device,\n    imm_enabled: bool,\n    lipschitz_const: float,\n    max_batches: int = 100,\n):\n    \"\"\"Full evaluation matrix: 4 noise levels x 2 pruning modes = 8 conditions.\"\"\"\n    eval_cfg = config.get(\"evaluation\", {})\n    epsilons = eval_cfg.get(\"perturbations\", [0.0, 0.01, 0.02, 0.05])\n    pruning_ratio = eval_cfg.get(\"pruning_ratio\", 0.5)\n\n    results = {}\n    action_losses = []\n\n    for epsilon in epsilons:\n        for pruning in [False, True]:\n            condition = f\"eps{epsilon}_prune{pruning}\"\n            log.info(\"Evaluating condition: %s\", condition)\n\n            all_margins = []\n            all_preservation = []\n            all_kendall = []\n            all_certified = []\n            all_led_ratio = []\n            all_action_loss = []\n\n            for batch_idx, batch in enumerate(dataloader):\n                if batch_idx >= max_batches:\n                    break\n                batch = {k: v.to(device) if isinstance(v, torch.Tensor) else v for k, v in batch.items()}\n\n                # Clean scores\n                scores_clean, k = compute_importance_scores(model, batch, imm_enabled)\n\n                if not imm_enabled:\n                    if hasattr(model, \"forward_baseline\"):\n                        loss, info = model.forward_baseline(batch)\n                    else:\n                        output = model(batch)\n                        loss = output[\"loss\"] if isinstance(output, dict) else (output[0] if isinstance(output, tuple) else output)\n                        info = {}\n                    loss_val = info.get(\"action_loss\", loss)\n                    all_action_loss.append(loss_val.item() if isinstance(loss_val, torch.Tensor) else loss_val)\n                    continue\n\n                # Perturbed batch\n                if epsilon > 0:\n                    batch_noisy = perturb_images(batch, epsilon)\n                    scores_pert, _ = compute_importance_scores(model, batch_noisy, imm_enabled)\n                else:\n                    scores_pert = scores_clean\n\n                # Metrics\n                margin = compute_margin(scores_clean, k)\n                pres = topk_preservation_rate(scores_clean, scores_pert, k)\n                kendall = kendall_tau_distance(scores_clean, scores_pert, k)\n                cert = certified_bound(margin, lipschitz_const, max(epsilon, 0.01), k)\n                led = l_eps_delta_ratio(lipschitz_const, max(epsilon, 0.01), margin, k)\n\n                all_margins.append(margin.cpu())\n                all_preservation.append(pres.cpu())\n                all_kendall.append(kendall.cpu())\n                all_certified.append(cert.cpu())\n                all_led_ratio.append(led.cpu())\n\n                # Action loss under this condition\n                if pruning:\n                    model.train(False)\n                    eval_batch = batch_noisy if epsilon > 0 else batch\n                    _, info = model(eval_batch, step=0)\n                    all_action_loss.append(info[\"action_loss\"].item())\n                else:\n                    _, info = model(batch if epsilon == 0 else perturb_images(batch, epsilon), step=0)\n                    all_action_loss.append(info[\"action_loss\"].item())\n\n            cond_results = {\n                \"action_loss\": sum(all_action_loss) / max(len(all_action_loss), 1),\n            }\n\n            if imm_enabled and all_margins:\n                margins_cat = torch.cat(all_margins)\n                pres_cat = torch.cat(all_preservation)\n                kendall_cat = torch.cat(all_kendall)\n                cert_cat = torch.cat(all_certified)\n                led_cat = torch.cat(all_led_ratio)\n\n                cond_results.update({\n                    \"margin_mean\": margins_cat.mean().item(),\n                    \"margin_median\": margins_cat.median().item(),\n                    \"margin_std\": margins_cat.std().item(),\n                    \"margin_min\": margins_cat.min().item(),\n                    \"margin_max\": margins_cat.max().item(),\n                    \"preservation_rate\": pres_cat.mean().item(),\n                    \"kendall_tau\": kendall_cat.mean().item(),\n                    \"certified_bound_mean\": cert_cat.mean().item(),\n                    \"certified_bound_max\": cert_cat.max().item(),\n                    \"l_eps_delta_ratio_mean\": led_cat.mean().item(),\n                    \"l_eps_delta_ratio_median\": led_cat.median().item(),\n                })\n\n            results[condition] = cond_results\n            log.info(\"  %s: %s\", condition, {k: f\"{v:.4f}\" for k, v in cond_results.items()})\n\n    return results\n\n\ndef main():\n    args = parse_args()\n\n    import numpy as np\n    import random\n    random.seed(args.seed)\n    np.random.seed(args.seed)\n    torch.manual_seed(args.seed)\n\n    config = load_config(args.config)\n    device = torch.device(f\"cuda:{args.gpu}\" if torch.cuda.is_available() else \"cpu\")\n\n    model, imm_enabled = load_model_and_checkpoint(config, args.checkpoint, device)\n\n    from train import load_dataset, make_dataloader\n    dataset = load_dataset(config)\n    dataloader = make_dataloader(dataset, {\n        **config,\n        \"training\": {**config.get(\"training\", {}), \"batch_size\": config.get(\"training\", {}).get(\"eval_batch_size\", 4)},\n    })\n\n    # Lipschitz estimation\n    lipschitz_const = 0.0\n    spectral_lipschitz = 0.0\n    if imm_enabled and hasattr(model, \"acis\"):\n        spectral_lipschitz = model.acis.get_lipschitz_estimate()\n        log.info(\"Spectral Lipschitz estimate: %.4f\", spectral_lipschitz)\n        lipschitz_const = estimate_lipschitz(model, dataloader, device, max_batches=10, num_samples=args.lipschitz_samples)\n\n    results = evaluate_full(model, dataloader, config, device, imm_enabled, lipschitz_const, max_batches=args.max_batches)\n\n    results[\"_meta\"] = {\n        \"checkpoint\": args.checkpoint,\n        \"config\": args.config,\n        \"imm_enabled\": imm_enabled,\n        \"lipschitz_empirical\": lipschitz_const,\n        \"lipschitz_spectral\": spectral_lipschitz,\n        \"max_batches\": args.max_batches,\n        \"seed\": args.seed,\n    }\n\n    # Summary: compare clean vs perturbed L*eps/Delta_k ratio\n    if imm_enabled:\n        clean_key = \"eps0.0_pruneFalse\"\n        if clean_key in results and \"l_eps_delta_ratio_mean\" in results.get(clean_key, {}):\n            log.info(\"=== Gate Metric Summary ===\")\n            for cond, data in results.items():\n                if cond.startswith(\"_\"):\n                    continue\n                led = data.get(\"l_eps_delta_ratio_mean\", float(\"nan\"))\n                pres = data.get(\"preservation_rate\", float(\"nan\"))\n                log.info(\"  %s: L*eps*k/Delta_k=%.4f, preservation=%.4f\", cond, led, pres)\n\n    # Save results\n    output_path = args.output\n    if output_path is None:\n        results_dir = Path(\"results\")\n        results_dir.mkdir(exist_ok=True)\n        ckpt_name = Path(args.checkpoint).stem\n        output_path = results_dir / f\"eval_{ckpt_name}.json\"\n    else:\n        output_path = Path(output_path)\n        output_path.parent.mkdir(parents=True, exist_ok=True)\n\n    with open(output_path, \"w\") as f:\n        json.dump(results, f, indent=2, default=str)\n    log.info(\"Results saved to %s\", output_path)\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 348,
      "startLine": 1,
      "totalLines": 348
    }
  }
}
```

</details>

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Read · `toolu_01UgA7kkeWBFgUWpYoLv4ymR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/run_mvp.sh"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "263df5c0-d01d-4f96-a4cb-fd4145125851",
  "uuid": "9c92e181-2db4-4627-b8fb-3b42ef7aebb7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P8fJNFF5YAX1pYssBKZQrR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 870,
      "cache_read_input_tokens": 26972,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 870
      },
      "output_tokens": 18,
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

_source line 16 · 2026-05-15T13:41:15.647Z_

<details><summary>↩ Tool result · `toolu_01UgA7kkeWBFgUWpYoLv4ymR`</summary>

```text
1	#!/bin/bash
2	# MVP experiment: Baseline + IMM anchor in parallel on 2 GPUs.
3	# GPU 0 → baseline, GPU 1 → IMM anchor (delta=0.3, lambda=0.5)
4	set -e
5	
6	source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
7	
8	SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
9	cd "$SCRIPT_DIR"
10	
11	echo "Starting MVP experiments at $(date)"
12	echo "Working directory: $SCRIPT_DIR"
13	
14	# Baseline on GPU 0
15	CUDA_VISIBLE_DEVICES=0 python train.py \
16	    --config configs/baseline.yaml \
17	    --gpu 0 --seed 42 \
18	    --wandb_run "baseline_seed42" &
19	PID_BASELINE=$!
20	
21	# IMM anchor on GPU 1
22	CUDA_VISIBLE_DEVICES=1 python train.py \
23	    --config configs/imm_anchor.yaml \
24	    --gpu 0 --seed 42 \
25	    --wandb_run "imm_d03_l05_seed42" &
26	PID_IMM=$!
27	
28	echo "Baseline PID: $PID_BASELINE (GPU 0)"
29	echo "IMM PID: $PID_IMM (GPU 1)"
30	echo "Monitor with: tail -f checkpoints/*/latest/..."
31	
32	wait $PID_BASELINE
33	BASELINE_EXIT=$?
34	
35	wait $PID_IMM
36	IMM_EXIT=$?
37	
38	echo ""
39	echo "=== MVP Results ==="
40	echo "Baseline exit code: $BASELINE_EXIT"
41	echo "IMM exit code: $IMM_EXIT"
42	echo "Finished at $(date)"
43	
44	if [ $BASELINE_EXIT -ne 0 ] || [ $IMM_EXIT -ne 0 ]; then
45	    echo "WARNING: One or more experiments failed"
46	    exit 1
47	fi
48	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "263df5c0-d01d-4f96-a4cb-fd4145125851",
  "uuid": "f2492d0b-c4ac-4abe-9d70-1024b535024a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/run_mvp.sh",
      "content": "#!/bin/bash\n# MVP experiment: Baseline + IMM anchor in parallel on 2 GPUs.\n# GPU 0 → baseline, GPU 1 → IMM anchor (delta=0.3, lambda=0.5)\nset -e\n\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base\n\nSCRIPT_DIR=\"$(cd \"$(dirname \"$0\")\" && pwd)\"\ncd \"$SCRIPT_DIR\"\n\necho \"Starting MVP experiments at $(date)\"\necho \"Working directory: $SCRIPT_DIR\"\n\n# Baseline on GPU 0\nCUDA_VISIBLE_DEVICES=0 python train.py \\\n    --config configs/baseline.yaml \\\n    --gpu 0 --seed 42 \\\n    --wandb_run \"baseline_seed42\" &\nPID_BASELINE=$!\n\n# IMM anchor on GPU 1\nCUDA_VISIBLE_DEVICES=1 python train.py \\\n    --config configs/imm_anchor.yaml \\\n    --gpu 0 --seed 42 \\\n    --wandb_run \"imm_d03_l05_seed42\" &\nPID_IMM=$!\n\necho \"Baseline PID: $PID_BASELINE (GPU 0)\"\necho \"IMM PID: $PID_IMM (GPU 1)\"\necho \"Monitor with: tail -f checkpoints/*/latest/...\"\n\nwait $PID_BASELINE\nBASELINE_EXIT=$?\n\nwait $PID_IMM\nIMM_EXIT=$?\n\necho \"\"\necho \"=== MVP Results ===\"\necho \"Baseline exit code: $BASELINE_EXIT\"\necho \"IMM exit code: $IMM_EXIT\"\necho \"Finished at $(date)\"\n\nif [ $BASELINE_EXIT -ne 0 ] || [ $IMM_EXIT -ne 0 ]; then\n    echo \"WARNING: One or more experiments failed\"\n    exit 1\nfi\n",
      "numLines": 48,
      "startLine": 1,
      "totalLines": 48
    }
  }
}
```

</details>

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — Read · `toolu_01WG7YWnWZtJERYkHd6ec4w6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/configs/baseline.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "263df5c0-d01d-4f96-a4cb-fd4145125851",
  "uuid": "07299761-fbe6-4c25-88aa-f3ab0be8da47",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P8fJNFF5YAX1pYssBKZQrR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 870,
      "cache_read_input_tokens": 26972,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 870
      },
      "output_tokens": 18,
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

_source line 18 · 2026-05-15T13:41:16.108Z_

<details><summary>↩ Tool result · `toolu_01WG7YWnWZtJERYkHd6ec4w6`</summary>

```text
1	# Baseline config: SmolVLA + LoRA fine-tuning on LIBERO, no IMM.
2	# L_action only (flow matching MSE).
3	
4	model:
5	  name: smolvla
6	  pretrained: "lerobot/smolvla_base"
7	  lora:
8	    rank: 32
9	    alpha: 64
10	    dropout: 0.05
11	    # Expert Q/V projections + state/action projection layers
12	    target_modules_regex: "(model\\.vlm_with_expert\\.lm_expert\\..*\\.(q|v)_proj|model\\.(state_proj|action_in_proj|action_out_proj|action_time_mlp_in|action_time_mlp_out))"
13	
14	imm:
15	  enabled: false
16	
17	dataset:
18	  repo_id: "lerobot/aloha_sim_insertion_scripted_image"
19	  features:
20	    state_dim: 14
21	    action_dim: 14
22	    cameras:
23	      - "observation.images.top"
24	
25	training:
26	  total_steps: 30000
27	  batch_size: 4
28	  eval_batch_size: 4
29	  num_workers: 4
30	  lr: 1.0e-4
31	  betas: [0.9, 0.95]
32	  weight_decay: 1.0e-10
33	  warmup_steps: 1000
34	  decay_lr: 2.5e-6
35	  grad_clip: 10.0
36	  eval_every: 2000
37	  save_every: 5000
38	  log_every: 50
39	  output_dir: "checkpoints/baseline"
40	  seed: 42
41	
42	evaluation:
43	  perturbations: [0.0, 0.01, 0.02, 0.05]
44	  pruning_ratio: 0.5
45	  max_eval_batches: 50
46	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "263df5c0-d01d-4f96-a4cb-fd4145125851",
  "uuid": "9b21e1e9-58d2-42d1-9e67-8979b8ef0703",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/configs/baseline.yaml",
      "content": "# Baseline config: SmolVLA + LoRA fine-tuning on LIBERO, no IMM.\n# L_action only (flow matching MSE).\n\nmodel:\n  name: smolvla\n  pretrained: \"lerobot/smolvla_base\"\n  lora:\n    rank: 32\n    alpha: 64\n    dropout: 0.05\n    # Expert Q/V projections + state/action projection layers\n    target_modules_regex: \"(model\\\\.vlm_with_expert\\\\.lm_expert\\\\..*\\\\.(q|v)_proj|model\\\\.(state_proj|action_in_proj|action_out_proj|action_time_mlp_in|action_time_mlp_out))\"\n\nimm:\n  enabled: false\n\ndataset:\n  repo_id: \"lerobot/aloha_sim_insertion_scripted_image\"\n  features:\n    state_dim: 14\n    action_dim: 14\n    cameras:\n      - \"observation.images.top\"\n\ntraining:\n  total_steps: 30000\n  batch_size: 4\n  eval_batch_size: 4\n  num_workers: 4\n  lr: 1.0e-4\n  betas: [0.9, 0.95]\n  weight_decay: 1.0e-10\n  warmup_steps: 1000\n  decay_lr: 2.5e-6\n  grad_clip: 10.0\n  eval_every: 2000\n  save_every: 5000\n  log_every: 50\n  output_dir: \"checkpoints/baseline\"\n  seed: 42\n\nevaluation:\n  perturbations: [0.0, 0.01, 0.02, 0.05]\n  pruning_ratio: 0.5\n  max_eval_batches: 50\n",
      "numLines": 46,
      "startLine": 1,
      "totalLines": 46
    }
  }
}
```

</details>

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Read · `toolu_017FerKUyrK65cWndK197mRc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/configs/imm_anchor.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "263df5c0-d01d-4f96-a4cb-fd4145125851",
  "uuid": "1e21ae6f-4a92-40e3-b2fa-ab7ac9dbb4ef",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P8fJNFF5YAX1pYssBKZQrR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 870,
      "cache_read_input_tokens": 26972,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 870
      },
      "output_tokens": 18,
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

_source line 20 · 2026-05-15T13:41:17.049Z_

<details><summary>↩ Tool result · `toolu_017FerKUyrK65cWndK197mRc`</summary>

```text
1	# IMM anchor config: delta=0.3, lambda=0.5
2	# L_total = L_action + lambda * L_margin with ACIS scoring + token selection.
3	
4	_base_: baseline.yaml
5	
6	imm:
7	  enabled: true
8	  delta: 0.3              # hinge margin threshold
9	  lambda_margin: 0.5      # margin loss weight (after warmup)
10	  warmup_steps: 3000      # 10% of total_steps — linear lambda warmup
11	  temperature: 0.5        # SoftTopK temperature (lower = sharper mask)
12	  soft_topk_method: "sigmoid"  # sigmoid | sinkhorn | implicit_diff
13	  k_ratio: 0.5            # retain 50% of visual tokens
14	
15	acis:
16	  visual_dim: 960          # SigLIP connector output dim
17	  action_dim: 720          # expert hidden dim
18	  num_heads: 8             # cross-attention heads
19	  dropout: 0.0             # attention dropout
20	  # spectral_norm applied by default in ACIS for Lipschitz control
21	
22	training:
23	  output_dir: "checkpoints/imm_anchor"
24	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "263df5c0-d01d-4f96-a4cb-fd4145125851",
  "uuid": "f6debe5e-575a-48b0-ba99-5f63724dcf19",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/configs/imm_anchor.yaml",
      "content": "# IMM anchor config: delta=0.3, lambda=0.5\n# L_total = L_action + lambda * L_margin with ACIS scoring + token selection.\n\n_base_: baseline.yaml\n\nimm:\n  enabled: true\n  delta: 0.3              # hinge margin threshold\n  lambda_margin: 0.5      # margin loss weight (after warmup)\n  warmup_steps: 3000      # 10% of total_steps — linear lambda warmup\n  temperature: 0.5        # SoftTopK temperature (lower = sharper mask)\n  soft_topk_method: \"sigmoid\"  # sigmoid | sinkhorn | implicit_diff\n  k_ratio: 0.5            # retain 50% of visual tokens\n\nacis:\n  visual_dim: 960          # SigLIP connector output dim\n  action_dim: 720          # expert hidden dim\n  num_heads: 8             # cross-attention heads\n  dropout: 0.0             # attention dropout\n  # spectral_norm applied by default in ACIS for Lipschitz control\n\ntraining:\n  output_dir: \"checkpoints/imm_anchor\"\n",
      "numLines": 24,
      "startLine": 1,
      "totalLines": 24
    }
  }
}
```

</details>

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Read · `toolu_01Q6AhUUtFwrSweAFoTQrh1D`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/imm/__init__.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "263df5c0-d01d-4f96-a4cb-fd4145125851",
  "uuid": "4062acdc-3525-4cba-b401-a4ad07e65cf1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P8fJNFF5YAX1pYssBKZQrR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 870,
      "cache_read_input_tokens": 26972,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 870
      },
      "output_tokens": 18,
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

_source line 22 · 2026-05-15T13:41:17.778Z_

<details><summary>↩ Tool result · `toolu_01Q6AhUUtFwrSweAFoTQrh1D`</summary>

```text
1	"""IMM — Importance Margin Maximization for VLA visual token compression."""
2	
3	from .soft_topk import SoftTopK
4	from .losses import MarginMaximizationLoss, IMMTotalLoss
5	from .token_selection import MarginAwareTokenSelector
6	from .acis import ACIS
7	from .smolvla_wrapper import IMMSmolVLAWrapper
8	from .metrics import (
9	    compute_margin,
10	    topk_preservation_rate,
11	    kendall_tau_distance,
12	    certified_bound,
13	    margin_statistics,
14	    compute_empirical_lipschitz,
15	    l_eps_delta_ratio,
16	)
17	
18	__all__ = [
19	    "SoftTopK",
20	    "MarginMaximizationLoss",
21	    "IMMTotalLoss",
22	    "MarginAwareTokenSelector",
23	    "ACIS",
24	    "IMMSmolVLAWrapper",
25	    "compute_margin",
26	    "topk_preservation_rate",
27	    "kendall_tau_distance",
28	    "certified_bound",
29	    "margin_statistics",
30	    "compute_empirical_lipschitz",
31	    "l_eps_delta_ratio",
32	]
33	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "263df5c0-d01d-4f96-a4cb-fd4145125851",
  "uuid": "83ab3c6f-e159-4fa4-9292-baa060943535",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/imm/__init__.py",
      "content": "\"\"\"IMM — Importance Margin Maximization for VLA visual token compression.\"\"\"\n\nfrom .soft_topk import SoftTopK\nfrom .losses import MarginMaximizationLoss, IMMTotalLoss\nfrom .token_selection import MarginAwareTokenSelector\nfrom .acis import ACIS\nfrom .smolvla_wrapper import IMMSmolVLAWrapper\nfrom .metrics import (\n    compute_margin,\n    topk_preservation_rate,\n    kendall_tau_distance,\n    certified_bound,\n    margin_statistics,\n    compute_empirical_lipschitz,\n    l_eps_delta_ratio,\n)\n\n__all__ = [\n    \"SoftTopK\",\n    \"MarginMaximizationLoss\",\n    \"IMMTotalLoss\",\n    \"MarginAwareTokenSelector\",\n    \"ACIS\",\n    \"IMMSmolVLAWrapper\",\n    \"compute_margin\",\n    \"topk_preservation_rate\",\n    \"kendall_tau_distance\",\n    \"certified_bound\",\n    \"margin_statistics\",\n    \"compute_empirical_lipschitz\",\n    \"l_eps_delta_ratio\",\n]\n",
      "numLines": 33,
      "startLine": 1,
      "totalLines": 33
    }
  }
}
```

</details>

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — Read · `toolu_01ANPqRcvUkncZQNhY8zS9AH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/imm/acis.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "263df5c0-d01d-4f96-a4cb-fd4145125851",
  "uuid": "a77f6b35-18c9-4752-ba61-5b49bb2657ea",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P8fJNFF5YAX1pYssBKZQrR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 870,
      "cache_read_input_tokens": 26972,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 870
      },
      "output_tokens": 18,
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

_source line 24 · 2026-05-15T13:41:18.461Z_

<details><summary>↩ Tool result · `toolu_01ANPqRcvUkncZQNhY8zS9AH`</summary>

```text
1	"""Action-Conditioned Importance Scoring (ACIS).
2	
3	Cross-attention scorer: a_query (action representations) attend to visual tokens,
4	producing per-token importance scores. All linear layers are wrapped with spectral
5	normalization to control the module's Lipschitz constant, which is required for
6	the certified bound k·ε·L/Δ_k to be meaningful.
7	
8	Inputs:  a_query (B, Q, action_dim), visual_tokens (B, N, visual_dim).
9	Outputs: importance_scores (B, N).
10	Depends: torch, spectral_norm.
11	"""
12	
13	from __future__ import annotations
14	
15	import torch
16	import torch.nn as nn
17	from torch import Tensor
18	from torch.nn.utils import spectral_norm
19	from typing import Tuple
20	
21	
22	class ACIS(nn.Module):
23	    def __init__(
24	        self,
25	        visual_dim: int = 960,
26	        action_dim: int = 720,
27	        num_heads: int = 8,
28	        dropout: float = 0.0,
29	    ):
30	        super().__init__()
31	        assert visual_dim % num_heads == 0
32	        self.visual_dim = visual_dim
33	        self.num_heads = num_heads
34	        self.head_dim = visual_dim // num_heads
35	        self.scale = self.head_dim ** -0.5
36	
37	        self.query_proj = spectral_norm(nn.Linear(action_dim, visual_dim))
38	        self.q_proj = spectral_norm(nn.Linear(visual_dim, visual_dim))
39	        self.k_proj = spectral_norm(nn.Linear(visual_dim, visual_dim))
40	        self.v_proj = spectral_norm(nn.Linear(visual_dim, visual_dim))
41	        self.score_head = spectral_norm(nn.Linear(visual_dim, 1))
42	        self.dropout = nn.Dropout(dropout)
43	
44	    def forward(self, a_query: Tensor, visual_tokens: Tensor) -> Tensor:
45	        """
46	        Args:
47	            a_query: (B, Q, action_dim) action representations from embed_suffix.
48	            visual_tokens: (B, N, visual_dim) visual tokens from embed_image.
49	        Returns:
50	            importance_scores: (B, N) per-token scores.
51	        """
52	        B, N, _ = visual_tokens.shape
53	        Q = a_query.shape[1]
54	        H, d = self.num_heads, self.head_dim
55	
56	        q = self.q_proj(self.query_proj(a_query))       # (B, Q, D)
57	        k = self.k_proj(visual_tokens)                   # (B, N, D)
58	        v = self.v_proj(visual_tokens)                   # (B, N, D)
59	
60	        q = q.view(B, Q, H, d).transpose(1, 2)          # (B, H, Q, d)
61	        k = k.view(B, N, H, d).transpose(1, 2)          # (B, H, N, d)
62	        v = v.view(B, N, H, d).transpose(1, 2)          # (B, H, N, d)
63	
64	        attn_weights = torch.matmul(q, k.transpose(-2, -1)) * self.scale  # (B, H, Q, N)
65	        attn_weights = attn_weights.softmax(dim=-1)
66	        attn_weights = self.dropout(attn_weights)
67	
68	        # Per-visual-token importance: average attention received across queries and heads
69	        token_importance = attn_weights.mean(dim=(1, 2))  # (B, N)
70	
71	        # Contextual representation per visual token via transposed attention
72	        # v^T @ attn^T → each visual token gets a context vector
73	        attn_t = attn_weights.transpose(-2, -1)           # (B, H, N, Q)
74	        context = torch.matmul(attn_t, q)                 # (B, H, N, d)
75	        context = context.transpose(1, 2).reshape(B, N, self.visual_dim)  # (B, N, D)
76	
77	        score_logits = self.score_head(context).squeeze(-1)  # (B, N)
78	
79	        # Combine learned score with attention-based importance
80	        importance_scores = score_logits + token_importance
81	
82	        return importance_scores
83	
84	    def get_lipschitz_estimate(self) -> float:
85	        """Product of spectral norms across all SN-wrapped layers."""
86	        L = 1.0
87	        for module in self.modules():
88	            if hasattr(module, "weight_orig"):
89	                sigma = torch.linalg.norm(module.weight, ord=2).item()
90	                L *= sigma
91	        return L
92	
93	
94	if __name__ == "__main__":
95	    torch.manual_seed(42)
96	    B, N, Q = 2, 128, 50
97	    vis = torch.randn(B, N, 960)
98	    a_q = torch.randn(B, Q, 720)
99	
100	    acis = ACIS(visual_dim=960, action_dim=720)
101	    scores = acis(a_q, vis)
102	    print(f"ACIS: scores shape={scores.shape}, range=[{scores.min():.3f}, {scores.max():.3f}]")
103	
104	    L = acis.get_lipschitz_estimate()
105	    print(f"Lipschitz estimate: {L:.4f}")
106	
107	    scores.sum().backward()
108	    print(f"ACIS grad OK: query_proj={acis.query_proj.weight_orig.grad is not None}")
109	    print("All ACIS tests passed!")
110	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "263df5c0-d01d-4f96-a4cb-fd4145125851",
  "uuid": "cfe09e9d-7550-4181-be67-e318f915a8d1",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/imm/acis.py",
      "content": "\"\"\"Action-Conditioned Importance Scoring (ACIS).\n\nCross-attention scorer: a_query (action representations) attend to visual tokens,\nproducing per-token importance scores. All linear layers are wrapped with spectral\nnormalization to control the module's Lipschitz constant, which is required for\nthe certified bound k·ε·L/Δ_k to be meaningful.\n\nInputs:  a_query (B, Q, action_dim), visual_tokens (B, N, visual_dim).\nOutputs: importance_scores (B, N).\nDepends: torch, spectral_norm.\n\"\"\"\n\nfrom __future__ import annotations\n\nimport torch\nimport torch.nn as nn\nfrom torch import Tensor\nfrom torch.nn.utils import spectral_norm\nfrom typing import Tuple\n\n\nclass ACIS(nn.Module):\n    def __init__(\n        self,\n        visual_dim: int = 960,\n        action_dim: int = 720,\n        num_heads: int = 8,\n        dropout: float = 0.0,\n    ):\n        super().__init__()\n        assert visual_dim % num_heads == 0\n        self.visual_dim = visual_dim\n        self.num_heads = num_heads\n        self.head_dim = visual_dim // num_heads\n        self.scale = self.head_dim ** -0.5\n\n        self.query_proj = spectral_norm(nn.Linear(action_dim, visual_dim))\n        self.q_proj = spectral_norm(nn.Linear(visual_dim, visual_dim))\n        self.k_proj = spectral_norm(nn.Linear(visual_dim, visual_dim))\n        self.v_proj = spectral_norm(nn.Linear(visual_dim, visual_dim))\n        self.score_head = spectral_norm(nn.Linear(visual_dim, 1))\n        self.dropout = nn.Dropout(dropout)\n\n    def forward(self, a_query: Tensor, visual_tokens: Tensor) -> Tensor:\n        \"\"\"\n        Args:\n            a_query: (B, Q, action_dim) action representations from embed_suffix.\n            visual_tokens: (B, N, visual_dim) visual tokens from embed_image.\n        Returns:\n            importance_scores: (B, N) per-token scores.\n        \"\"\"\n        B, N, _ = visual_tokens.shape\n        Q = a_query.shape[1]\n        H, d = self.num_heads, self.head_dim\n\n        q = self.q_proj(self.query_proj(a_query))       # (B, Q, D)\n        k = self.k_proj(visual_tokens)                   # (B, N, D)\n        v = self.v_proj(visual_tokens)                   # (B, N, D)\n\n        q = q.view(B, Q, H, d).transpose(1, 2)          # (B, H, Q, d)\n        k = k.view(B, N, H, d).transpose(1, 2)          # (B, H, N, d)\n        v = v.view(B, N, H, d).transpose(1, 2)          # (B, H, N, d)\n\n        attn_weights = torch.matmul(q, k.transpose(-2, -1)) * self.scale  # (B, H, Q, N)\n        attn_weights = attn_weights.softmax(dim=-1)\n        attn_weights = self.dropout(attn_weights)\n\n        # Per-visual-token importance: average attention received across queries and heads\n        token_importance = attn_weights.mean(dim=(1, 2))  # (B, N)\n\n        # Contextual representation per visual token via transposed attention\n        # v^T @ attn^T → each visual token gets a context vector\n        attn_t = attn_weights.transpose(-2, -1)           # (B, H, N, Q)\n        context = torch.matmul(attn_t, q)                 # (B, H, N, d)\n        context = context.transpose(1, 2).reshape(B, N, self.visual_dim)  # (B, N, D)\n\n        score_logits = self.score_head(context).squeeze(-1)  # (B, N)\n\n        # Combine learned score with attention-based importance\n        importance_scores = score_logits + token_importance\n\n        return importance_scores\n\n    def get_lipschitz_estimate(self) -> float:\n        \"\"\"Product of spectral norms across all SN-wrapped layers.\"\"\"\n        L = 1.0\n        for module in self.modules():\n            if hasattr(module, \"weight_orig\"):\n                sigma = torch.linalg.norm(module.weight, ord=2).item()\n                L *= sigma\n        return L\n\n\nif __name__ == \"__main__\":\n    torch.manual_seed(42)\n    B, N, Q = 2, 128, 50\n    vis = torch.randn(B, N, 960)\n    a_q = torch.randn(B, Q, 720)\n\n    acis = ACIS(visual_dim=960, action_dim=720)\n    scores = acis(a_q, vis)\n    print(f\"ACIS: scores shape={scores.shape}, range=[{scores.min():.3f}, {scores.max():.3f}]\")\n\n    L = acis.get_lipschitz_estimate()\n    print(f\"Lipschitz estimate: {L:.4f}\")\n\n    scores.sum().backward()\n    print(f\"ACIS grad OK: query_proj={acis.query_proj.weight_orig.grad is not None}\")\n    print(\"All ACIS tests passed!\")\n",
      "numLines": 110,
      "startLine": 1,
      "totalLines": 110
    }
  }
}
```

</details>

---

### Tool call

_source line 25_

<details open><summary>🔧 Tool call — Read · `toolu_013cLsUM5y4WnMSxvSLTBa6v`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/imm/losses.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "263df5c0-d01d-4f96-a4cb-fd4145125851",
  "uuid": "94ae5a1b-b477-432d-a56a-4603bc1662dd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P8fJNFF5YAX1pYssBKZQrR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 870,
      "cache_read_input_tokens": 26972,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 870
      },
      "output_tokens": 18,
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

_source line 26 · 2026-05-15T13:41:18.937Z_

<details><summary>↩ Tool result · `toolu_013cLsUM5y4WnMSxvSLTBa6v`</summary>

```text
1	"""Importance Margin Maximization losses.
2	
3	MarginMaximizationLoss: hinge loss  max(0, delta - (s_{(k)} - s_{(k+1)})).
4	IMMTotalLoss:           L_action + lambda * L_margin  with linear lambda warmup.
5	
6	Inputs:  (B, N) importance scores, integer k.
7	Depends: soft_topk.SoftTopK.
8	"""
9	
10	from __future__ import annotations
11	
12	import torch
13	import torch.nn as nn
14	from torch import Tensor
15	from typing import Dict, Tuple
16	
17	from .soft_topk import SoftTopK
18	
19	
20	class MarginMaximizationLoss(nn.Module):
21	    """Hinge loss: L_margin = mean(max(0, delta - (s_{(k)} - s_{(k+1)})))."""
22	
23	    def __init__(self, delta: float = 1.0, temperature: float = 1.0, method: str = "sigmoid"):
24	        super().__init__()
25	        self.delta = delta
26	        self.soft_topk = SoftTopK(temperature=temperature, method=method)
27	
28	    def forward(self, importance_scores: Tensor, k: int) -> Tuple[Tensor, Dict[str, Tensor]]:
29	        """
30	        Args:
31	            importance_scores: (B, N) per-token importance scores.
32	            k: number of tokens to retain.
33	        Returns:
34	            loss: scalar hinge loss.
35	            info: dict with margin, s_k, s_k_plus_1, mask for logging.
36	        """
37	        mask, s_k, s_k_plus_1 = self.soft_topk(importance_scores, k)
38	
39	        margin = s_k - s_k_plus_1  # (B,)
40	        hinge = torch.clamp(self.delta - margin, min=0.0)  # (B,)
41	        loss = hinge.mean()
42	
43	        info = {
44	            "margin": margin.detach(),
45	            "s_k": s_k.detach(),
46	            "s_k_plus_1": s_k_plus_1.detach(),
47	            "hinge": hinge.detach(),
48	            "mask": mask.detach(),
49	        }
50	        return loss, info
51	
52	
53	class IMMTotalLoss(nn.Module):
54	    """L_total = L_action + lambda * L_margin, with linear lambda warmup."""
55	
56	    def __init__(
57	        self,
58	        lambda_margin: float = 0.1,
59	        delta: float = 1.0,
60	        warmup_steps: int = 1000,
61	        temperature: float = 1.0,
62	        method: str = "sigmoid",
63	    ):
64	        super().__init__()
65	        self.lambda_margin = lambda_margin
66	        self.warmup_steps = warmup_steps
67	        self.margin_loss = MarginMaximizationLoss(delta=delta, temperature=temperature, method=method)
68	
69	    def _get_lambda(self, step: int) -> float:
70	        if self.warmup_steps <= 0:
71	            return self.lambda_margin
72	        return self.lambda_margin * min(1.0, step / self.warmup_steps)
73	
74	    def forward(
75	        self, action_loss: Tensor, importance_scores: Tensor, k: int, step: int
76	    ) -> Tuple[Tensor, Dict[str, Tensor]]:
77	        """
78	        Args:
79	            action_loss: scalar task loss (e.g. action prediction).
80	            importance_scores: (B, N).
81	            k: retention count.
82	            step: current training step (for warmup).
83	        Returns:
84	            total_loss: scalar.
85	            info: dict with all sub-losses and diagnostics.
86	        """
87	        lam = self._get_lambda(step)
88	        margin_loss, margin_info = self.margin_loss(importance_scores, k)
89	        total = action_loss + lam * margin_loss
90	
91	        info = {
92	            **margin_info,
93	            "action_loss": action_loss.detach(),
94	            "margin_loss": margin_loss.detach(),
95	            "total_loss": total.detach(),
96	            "lambda": torch.tensor(lam),
97	        }
98	        return total, info
99	
100	
101	if __name__ == "__main__":
102	    torch.manual_seed(42)
103	    B, N, k = 4, 64, 16
104	    scores = torch.randn(B, N, requires_grad=True)
105	    action_loss = torch.tensor(1.5, requires_grad=True)
106	
107	    mmr = MarginMaximizationLoss(delta=0.5, temperature=0.5)
108	    loss, info = mmr(scores, k)
109	    loss.backward()
110	    print(f"MMR: loss={loss.item():.4f}, margin_mean={info['margin'].mean().item():.4f}, "
111	          f"grad OK={scores.grad is not None}")
112	    scores.grad = None
113	
114	    total_loss_fn = IMMTotalLoss(lambda_margin=0.1, delta=0.5, warmup_steps=100, temperature=0.5)
115	    total, tinfo = total_loss_fn(action_loss, scores, k, step=50)
116	    total.backward()
117	    print(f"Total: loss={total.item():.4f}, lambda={tinfo['lambda'].item():.4f}, "
118	          f"grad OK={scores.grad is not None}")
119	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "263df5c0-d01d-4f96-a4cb-fd4145125851",
  "uuid": "8d56b404-e094-496b-8fa3-f06c2f188156",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/imm/losses.py",
      "content": "\"\"\"Importance Margin Maximization losses.\n\nMarginMaximizationLoss: hinge loss  max(0, delta - (s_{(k)} - s_{(k+1)})).\nIMMTotalLoss:           L_action + lambda * L_margin  with linear lambda warmup.\n\nInputs:  (B, N) importance scores, integer k.\nDepends: soft_topk.SoftTopK.\n\"\"\"\n\nfrom __future__ import annotations\n\nimport torch\nimport torch.nn as nn\nfrom torch import Tensor\nfrom typing import Dict, Tuple\n\nfrom .soft_topk import SoftTopK\n\n\nclass MarginMaximizationLoss(nn.Module):\n    \"\"\"Hinge loss: L_margin = mean(max(0, delta - (s_{(k)} - s_{(k+1)}))).\"\"\"\n\n    def __init__(self, delta: float = 1.0, temperature: float = 1.0, method: str = \"sigmoid\"):\n        super().__init__()\n        self.delta = delta\n        self.soft_topk = SoftTopK(temperature=temperature, method=method)\n\n    def forward(self, importance_scores: Tensor, k: int) -> Tuple[Tensor, Dict[str, Tensor]]:\n        \"\"\"\n        Args:\n            importance_scores: (B, N) per-token importance scores.\n            k: number of tokens to retain.\n        Returns:\n            loss: scalar hinge loss.\n            info: dict with margin, s_k, s_k_plus_1, mask for logging.\n        \"\"\"\n        mask, s_k, s_k_plus_1 = self.soft_topk(importance_scores, k)\n\n        margin = s_k - s_k_plus_1  # (B,)\n        hinge = torch.clamp(self.delta - margin, min=0.0)  # (B,)\n        loss = hinge.mean()\n\n        info = {\n            \"margin\": margin.detach(),\n            \"s_k\": s_k.detach(),\n            \"s_k_plus_1\": s_k_plus_1.detach(),\n            \"hinge\": hinge.detach(),\n            \"mask\": mask.detach(),\n        }\n        return loss, info\n\n\nclass IMMTotalLoss(nn.Module):\n    \"\"\"L_total = L_action + lambda * L_margin, with linear lambda warmup.\"\"\"\n\n    def __init__(\n        self,\n        lambda_margin: float = 0.1,\n        delta: float = 1.0,\n        warmup_steps: int = 1000,\n        temperature: float = 1.0,\n        method: str = \"sigmoid\",\n    ):\n        super().__init__()\n        self.lambda_margin = lambda_margin\n        self.warmup_steps = warmup_steps\n        self.margin_loss = MarginMaximizationLoss(delta=delta, temperature=temperature, method=method)\n\n    def _get_lambda(self, step: int) -> float:\n        if self.warmup_steps <= 0:\n            return self.lambda_margin\n        return self.lambda_margin * min(1.0, step / self.warmup_steps)\n\n    def forward(\n        self, action_loss: Tensor, importance_scores: Tensor, k: int, step: int\n    ) -> Tuple[Tensor, Dict[str, Tensor]]:\n        \"\"\"\n        Args:\n            action_loss: scalar task loss (e.g. action prediction).\n            importance_scores: (B, N).\n            k: retention count.\n            step: current training step (for warmup).\n        Returns:\n            total_loss: scalar.\n            info: dict with all sub-losses and diagnostics.\n        \"\"\"\n        lam = self._get_lambda(step)\n        margin_loss, margin_info = self.margin_loss(importance_scores, k)\n        total = action_loss + lam * margin_loss\n\n        info = {\n            **margin_info,\n            \"action_loss\": action_loss.detach(),\n            \"margin_loss\": margin_loss.detach(),\n            \"total_loss\": total.detach(),\n            \"lambda\": torch.tensor(lam),\n        }\n        return total, info\n\n\nif __name__ == \"__main__\":\n    torch.manual_seed(42)\n    B, N, k = 4, 64, 16\n    scores = torch.randn(B, N, requires_grad=True)\n    action_loss = torch.tensor(1.5, requires_grad=True)\n\n    mmr = MarginMaximizationLoss(delta=0.5, temperature=0.5)\n    loss, info = mmr(scores, k)\n    loss.backward()\n    print(f\"MMR: loss={loss.item():.4f}, margin_mean={info['margin'].mean().item():.4f}, \"\n          f\"grad OK={scores.grad is not None}\")\n    scores.grad = None\n\n    total_loss_fn = IMMTotalLoss(lambda_margin=0.1, delta=0.5, warmup_steps=100, temperature=0.5)\n    total, tinfo = total_loss_fn(action_loss, scores, k, step=50)\n    total.backward()\n    print(f\"Total: loss={total.item():.4f}, lambda={tinfo['lambda'].item():.4f}, \"\n          f\"grad OK={scores.grad is not None}\")\n",
      "numLines": 119,
      "startLine": 1,
      "totalLines": 119
    }
  }
}
```

</details>

---

### Tool call

_source line 27_

<details open><summary>🔧 Tool call — Read · `toolu_01W5KRzvif1NSQ3kSTrCk2Ns`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/imm/metrics.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "263df5c0-d01d-4f96-a4cb-fd4145125851",
  "uuid": "128f7969-c54a-4501-b9bd-bf8351b97e09",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P8fJNFF5YAX1pYssBKZQrR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 870,
      "cache_read_input_tokens": 26972,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 870
      },
      "output_tokens": 18,
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

_source line 28 · 2026-05-15T13:41:19.405Z_

<details><summary>↩ Tool result · `toolu_01W5KRzvif1NSQ3kSTrCk2Ns`</summary>

```text
1	"""Evaluation metrics for importance-margin token compression.
2	
3	compute_margin:              gap between k-th and (k+1)-th largest scores.
4	topk_preservation_rate:      Jaccard overlap of top-k sets under perturbation.
5	kendall_tau_distance:        rank correlation of top-k ordering under perturbation.
6	certified_bound:             probabilistic upper bound on top-k set change.
7	margin_statistics:           summary stats of margins across a batch.
8	compute_empirical_lipschitz: empirical Lipschitz constant via input perturbation.
9	l_eps_delta_ratio:           L·ε/Δ_k gate metric for IMM vs baseline comparison.
10	
11	All functions are pure (no nn.Module state), operate on detached tensors.
12	"""
13	
14	from __future__ import annotations
15	
16	import torch
17	import torch.nn as nn
18	from torch import Tensor
19	from torch.utils.data import DataLoader
20	from typing import Callable, Dict, Optional
21	
22	
23	def compute_margin(scores: Tensor, k: int) -> Tensor:
24	    """Delta_k = s_{(k)} - s_{(k+1)}.
25	
26	    Args:
27	        scores: (B, N) importance scores.
28	        k: retention count, must satisfy 0 < k < N.
29	    Returns:
30	        (B,) margin values.
31	    """
32	    sorted_scores, _ = torch.sort(scores, dim=-1, descending=True)
33	    return sorted_scores[:, k - 1] - sorted_scores[:, k]
34	
35	
36	def topk_preservation_rate(scores_clean: Tensor, scores_perturbed: Tensor, k: int) -> Tensor:
37	    """Jaccard similarity |A ∩ B| / |A ∪ B| of top-k index sets.
38	
39	    Args:
40	        scores_clean:     (B, N).
41	        scores_perturbed: (B, N).
42	        k: retention count.
43	    Returns:
44	        (B,) Jaccard similarities in [0, 1].
45	    """
46	    _, idx_clean = torch.topk(scores_clean, k, dim=-1)
47	    _, idx_pert = torch.topk(scores_perturbed, k, dim=-1)
48	
49	    B, N = scores_clean.shape
50	    mask_clean = torch.zeros(B, N, device=scores_clean.device)
51	    mask_pert = torch.zeros(B, N, device=scores_clean.device)
52	    mask_clean.scatter_(1, idx_clean, 1.0)
53	    mask_pert.scatter_(1, idx_pert, 1.0)
54	
55	    intersection = (mask_clean * mask_pert).sum(-1)
56	    union = (mask_clean + mask_pert).clamp(max=1.0).sum(-1)
57	    return intersection / union.clamp(min=1.0)
58	
59	
60	def kendall_tau_distance(scores_clean: Tensor, scores_perturbed: Tensor, k: int) -> Tensor:
61	    """Kendall tau-b correlation of top-k rankings.
62	
63	    Only considers the union of top-k indices from both sets.
64	    Returns values in [-1, 1]; +1 = identical ranking.
65	
66	    Args:
67	        scores_clean:     (B, N).
68	        scores_perturbed: (B, N).
69	        k: retention count.
70	    Returns:
71	        (B,) correlation values.
72	    """
73	    B, N = scores_clean.shape
74	    _, idx_clean = torch.topk(scores_clean, k, dim=-1)
75	    _, idx_pert = torch.topk(scores_perturbed, k, dim=-1)
76	
77	    # Union of top-k indices
78	    mask_union = torch.zeros(B, N, device=scores_clean.device)
79	    mask_union.scatter_(1, idx_clean, 1.0)
80	    mask_union.scatter_(1, idx_pert, 1.0)
81	
82	    taus = []
83	    for b in range(B):
84	        union_idx = mask_union[b].nonzero(as_tuple=True)[0]
85	        n_union = union_idx.numel()
86	        if n_union < 2:
87	            taus.append(torch.tensor(1.0, device=scores_clean.device))
88	            continue
89	
90	        r1 = scores_clean[b, union_idx]
91	        r2 = scores_perturbed[b, union_idx]
92	
93	        # Pairwise concordance
94	        diff1 = r1.unsqueeze(0) - r1.unsqueeze(1)  # (n, n)
95	        diff2 = r2.unsqueeze(0) - r2.unsqueeze(1)
96	        sign_prod = torch.sign(diff1) * torch.sign(diff2)
97	
98	        # Upper triangle only
99	        n_pairs = n_union * (n_union - 1) // 2
100	        tau = sign_prod.triu(diagonal=1).sum() / max(n_pairs, 1)
101	        taus.append(tau)
102	
103	    return torch.stack(taus)
104	
105	
106	def certified_bound(margin: Tensor, lipschitz_const: float, epsilon: float, k: int) -> Tensor:
107	    """Upper bound on probability of top-k set change: P <= k * eps * L / Delta_k.
108	
109	    Args:
110	        margin:         (B,) Delta_k values (must be > 0 for meaningful bound).
111	        lipschitz_const: Lipschitz constant L of the scoring function.
112	        epsilon:        perturbation budget (L_inf or L_2 radius).
113	        k:              retention count.
114	    Returns:
115	        (B,) upper bound probabilities, clamped to [0, 1].
116	    """
117	    bound = k * epsilon * lipschitz_const / margin.clamp(min=1e-8)
118	    return bound.clamp(0.0, 1.0)
119	
120	
121	def margin_statistics(scores: Tensor, k: int) -> Dict[str, Tensor]:
122	    """Summary statistics of Delta_k across a batch.
123	
124	    Args:
125	        scores: (B, N).
126	        k: retention count.
127	    Returns:
128	        dict with median, mean, std, min, max of margins.
129	    """
130	    m = compute_margin(scores, k)
131	    return {
132	        "median": m.median(),
133	        "mean": m.mean(),
134	        "std": m.std(),
135	        "min": m.min(),
136	        "max": m.max(),
137	    }
138	
139	
140	@torch.no_grad()
141	def compute_empirical_lipschitz(
142	    acis_module: nn.Module,
143	    visual_tokens: Tensor,
144	    a_query: Tensor,
145	    num_samples: int = 100,
146	    epsilon: float = 0.001,
147	) -> float:
148	    """Empirical Lipschitz constant: max ||s(x') - s(x)|| / ||x' - x|| over perturbations.
149	
150	    Perturbs visual_tokens by random directions of norm epsilon.
151	
152	    Args:
153	        acis_module: ACIS module (eval mode, no grad).
154	        visual_tokens: (B, N, D) base visual tokens.
155	        a_query: (B, Q, A) action query (held fixed).
156	        num_samples: number of random perturbation directions.
157	        epsilon: perturbation L2 norm per token.
158	    Returns:
159	        scalar estimated Lipschitz constant.
160	    """
161	    acis_module.eval()
162	    s_clean = acis_module(a_query, visual_tokens)  # (B, N)
163	
164	    max_ratio = 0.0
165	    for _ in range(num_samples):
166	        delta = torch.randn_like(visual_tokens)
167	        delta = delta / delta.norm(dim=-1, keepdim=True).clamp(min=1e-8) * epsilon
168	        s_pert = acis_module(a_query, visual_tokens + delta)
169	
170	        score_diff = (s_pert - s_clean).norm(dim=-1)  # (B,)
171	        input_diff = delta.flatten(1).norm(dim=-1)     # (B,)
172	        ratio = (score_diff / input_diff.clamp(min=1e-8)).max().item()
173	        max_ratio = max(max_ratio, ratio)
174	
175	    return max_ratio
176	
177	
178	def l_eps_delta_ratio(
179	    lipschitz_const: float, epsilon: float, margin: Tensor, k: int
180	) -> Tensor:
181	    """L·ε·k/Δ_k — gate metric. Values < 1 mean the certified bound holds.
182	
183	    Args:
184	        lipschitz_const: Lipschitz constant L of the scoring function.
185	        epsilon: perturbation budget.
186	        margin: (B,) Δ_k values.
187	        k: retention count.
188	    Returns:
189	        (B,) ratio values.
190	    """
191	    return lipschitz_const * epsilon * k / margin.clamp(min=1e-8)
192	
193	
194	if __name__ == "__main__":
195	    torch.manual_seed(42)
196	    B, N, k = 4, 64, 16
197	    scores = torch.randn(B, N)
198	    scores_noisy = scores + 0.1 * torch.randn_like(scores)
199	
200	    m = compute_margin(scores, k)
201	    print(f"Margin: {m}")
202	
203	    pr = topk_preservation_rate(scores, scores_noisy, k)
204	    print(f"Preservation rate: {pr}")
205	
206	    kt = kendall_tau_distance(scores, scores_noisy, k)
207	    print(f"Kendall tau: {kt}")
208	
209	    cb = certified_bound(m, lipschitz_const=1.0, epsilon=0.01, k=k)
210	    print(f"Certified bound: {cb}")
211	
212	    stats = margin_statistics(scores, k)
213	    print(f"Stats: { {k: v.item() for k, v in stats.items()} }")
214	
215	    # L·ε/Δ_k ratio
216	    ratio = l_eps_delta_ratio(1.0, 0.01, m, k)
217	    print(f"L*eps*k/Delta_k ratio: {ratio}")
218	
219	    # Empirical Lipschitz (needs ACIS)
220	    from .acis import ACIS
221	    acis = ACIS(visual_dim=64, action_dim=32, num_heads=4)
222	    vis = torch.randn(2, 16, 64)
223	    aq = torch.randn(2, 8, 32)
224	    L_emp = compute_empirical_lipschitz(acis, vis, aq, num_samples=20, epsilon=0.001)
225	    print(f"Empirical Lipschitz: {L_emp:.4f}")
226	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "263df5c0-d01d-4f96-a4cb-fd4145125851",
  "uuid": "71e4cd11-e829-4bbc-88ea-4e3ff41107f8",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/imm/metrics.py",
      "content": "\"\"\"Evaluation metrics for importance-margin token compression.\n\ncompute_margin:              gap between k-th and (k+1)-th largest scores.\ntopk_preservation_rate:      Jaccard overlap of top-k sets under perturbation.\nkendall_tau_distance:        rank correlation of top-k ordering under perturbation.\ncertified_bound:             probabilistic upper bound on top-k set change.\nmargin_statistics:           summary stats of margins across a batch.\ncompute_empirical_lipschitz: empirical Lipschitz constant via input perturbation.\nl_eps_delta_ratio:           L·ε/Δ_k gate metric for IMM vs baseline comparison.\n\nAll functions are pure (no nn.Module state), operate on detached tensors.\n\"\"\"\n\nfrom __future__ import annotations\n\nimport torch\nimport torch.nn as nn\nfrom torch import Tensor\nfrom torch.utils.data import DataLoader\nfrom typing import Callable, Dict, Optional\n\n\ndef compute_margin(scores: Tensor, k: int) -> Tensor:\n    \"\"\"Delta_k = s_{(k)} - s_{(k+1)}.\n\n    Args:\n        scores: (B, N) importance scores.\n        k: retention count, must satisfy 0 < k < N.\n    Returns:\n        (B,) margin values.\n    \"\"\"\n    sorted_scores, _ = torch.sort(scores, dim=-1, descending=True)\n    return sorted_scores[:, k - 1] - sorted_scores[:, k]\n\n\ndef topk_preservation_rate(scores_clean: Tensor, scores_perturbed: Tensor, k: int) -> Tensor:\n    \"\"\"Jaccard similarity |A ∩ B| / |A ∪ B| of top-k index sets.\n\n    Args:\n        scores_clean:     (B, N).\n        scores_perturbed: (B, N).\n        k: retention count.\n    Returns:\n        (B,) Jaccard similarities in [0, 1].\n    \"\"\"\n    _, idx_clean = torch.topk(scores_clean, k, dim=-1)\n    _, idx_pert = torch.topk(scores_perturbed, k, dim=-1)\n\n    B, N = scores_clean.shape\n    mask_clean = torch.zeros(B, N, device=scores_clean.device)\n    mask_pert = torch.zeros(B, N, device=scores_clean.device)\n    mask_clean.scatter_(1, idx_clean, 1.0)\n    mask_pert.scatter_(1, idx_pert, 1.0)\n\n    intersection = (mask_clean * mask_pert).sum(-1)\n    union = (mask_clean + mask_pert).clamp(max=1.0).sum(-1)\n    return intersection / union.clamp(min=1.0)\n\n\ndef kendall_tau_distance(scores_clean: Tensor, scores_perturbed: Tensor, k: int) -> Tensor:\n    \"\"\"Kendall tau-b correlation of top-k rankings.\n\n    Only considers the union of top-k indices from both sets.\n    Returns values in [-1, 1]; +1 = identical ranking.\n\n    Args:\n        scores_clean:     (B, N).\n        scores_perturbed: (B, N).\n        k: retention count.\n    Returns:\n        (B,) correlation values.\n    \"\"\"\n    B, N = scores_clean.shape\n    _, idx_clean = torch.topk(scores_clean, k, dim=-1)\n    _, idx_pert = torch.topk(scores_perturbed, k, dim=-1)\n\n    # Union of top-k indices\n    mask_union = torch.zeros(B, N, device=scores_clean.device)\n    mask_union.scatter_(1, idx_clean, 1.0)\n    mask_union.scatter_(1, idx_pert, 1.0)\n\n    taus = []\n    for b in range(B):\n        union_idx = mask_union[b].nonzero(as_tuple=True)[0]\n        n_union = union_idx.numel()\n        if n_union < 2:\n            taus.append(torch.tensor(1.0, device=scores_clean.device))\n            continue\n\n        r1 = scores_clean[b, union_idx]\n        r2 = scores_perturbed[b, union_idx]\n\n        # Pairwise concordance\n        diff1 = r1.unsqueeze(0) - r1.unsqueeze(1)  # (n, n)\n        diff2 = r2.unsqueeze(0) - r2.unsqueeze(1)\n        sign_prod = torch.sign(diff1) * torch.sign(diff2)\n\n        # Upper triangle only\n        n_pairs = n_union * (n_union - 1) // 2\n        tau = sign_prod.triu(diagonal=1).sum() / max(n_pairs, 1)\n        taus.append(tau)\n\n    return torch.stack(taus)\n\n\ndef certified_bound(margin: Tensor, lipschitz_const: float, epsilon: float, k: int) -> Tensor:\n    \"\"\"Upper bound on probability of top-k set change: P <= k * eps * L / Delta_k.\n\n    Args:\n        margin:         (B,) Delta_k values (must be > 0 for meaningful bound).\n        lipschitz_const: Lipschitz constant L of the scoring function.\n        epsilon:        perturbation budget (L_inf or L_2 radius).\n        k:              retention count.\n    Returns:\n        (B,) upper bound probabilities, clamped to [0, 1].\n    \"\"\"\n    bound = k * epsilon * lipschitz_const / margin.clamp(min=1e-8)\n    return bound.clamp(0.0, 1.0)\n\n\ndef margin_statistics(scores: Tensor, k: int) -> Dict[str, Tensor]:\n    \"\"\"Summary statistics of Delta_k across a batch.\n\n    Args:\n        scores: (B, N).\n        k: retention count.\n    Returns:\n        dict with median, mean, std, min, max of margins.\n    \"\"\"\n    m = compute_margin(scores, k)\n    return {\n        \"median\": m.median(),\n        \"mean\": m.mean(),\n        \"std\": m.std(),\n        \"min\": m.min(),\n        \"max\": m.max(),\n    }\n\n\n@torch.no_grad()\ndef compute_empirical_lipschitz(\n    acis_module: nn.Module,\n    visual_tokens: Tensor,\n    a_query: Tensor,\n    num_samples: int = 100,\n    epsilon: float = 0.001,\n) -> float:\n    \"\"\"Empirical Lipschitz constant: max ||s(x') - s(x)|| / ||x' - x|| over perturbations.\n\n    Perturbs visual_tokens by random directions of norm epsilon.\n\n    Args:\n        acis_module: ACIS module (eval mode, no grad).\n        visual_tokens: (B, N, D) base visual tokens.\n        a_query: (B, Q, A) action query (held fixed).\n        num_samples: number of random perturbation directions.\n        epsilon: perturbation L2 norm per token.\n    Returns:\n        scalar estimated Lipschitz constant.\n    \"\"\"\n    acis_module.eval()\n    s_clean = acis_module(a_query, visual_tokens)  # (B, N)\n\n    max_ratio = 0.0\n    for _ in range(num_samples):\n        delta = torch.randn_like(visual_tokens)\n        delta = delta / delta.norm(dim=-1, keepdim=True).clamp(min=1e-8) * epsilon\n        s_pert = acis_module(a_query, visual_tokens + delta)\n\n        score_diff = (s_pert - s_clean).norm(dim=-1)  # (B,)\n        input_diff = delta.flatten(1).norm(dim=-1)     # (B,)\n        ratio = (score_diff / input_diff.clamp(min=1e-8)).max().item()\n        max_ratio = max(max_ratio, ratio)\n\n    return max_ratio\n\n\ndef l_eps_delta_ratio(\n    lipschitz_const: float, epsilon: float, margin: Tensor, k: int\n) -> Tensor:\n    \"\"\"L·ε·k/Δ_k — gate metric. Values < 1 mean the certified bound holds.\n\n    Args:\n        lipschitz_const: Lipschitz constant L of the scoring function.\n        epsilon: perturbation budget.\n        margin: (B,) Δ_k values.\n        k: retention count.\n    Returns:\n        (B,) ratio values.\n    \"\"\"\n    return lipschitz_const * epsilon * k / margin.clamp(min=1e-8)\n\n\nif __name__ == \"__main__\":\n    torch.manual_seed(42)\n    B, N, k = 4, 64, 16\n    scores = torch.randn(B, N)\n    scores_noisy = scores + 0.1 * torch.randn_like(scores)\n\n    m = compute_margin(scores, k)\n    print(f\"Margin: {m}\")\n\n    pr = topk_preservation_rate(scores, scores_noisy, k)\n    print(f\"Preservation rate: {pr}\")\n\n    kt = kendall_tau_distance(scores, scores_noisy, k)\n    print(f\"Kendall tau: {kt}\")\n\n    cb = certified_bound(m, lipschitz_const=1.0, epsilon=0.01, k=k)\n    print(f\"Certified bound: {cb}\")\n\n    stats = margin_statistics(scores, k)\n    print(f\"Stats: { {k: v.item() for k, v in stats.items()} }\")\n\n    # L·ε/Δ_k ratio\n    ratio = l_eps_delta_ratio(1.0, 0.01, m, k)\n    print(f\"L*eps*k/Delta_k ratio: {ratio}\")\n\n    # Empirical Lipschitz (needs ACIS)\n    from .acis import ACIS\n    acis = ACIS(visual_dim=64, action_dim=32, num_heads=4)\n    vis = torch.randn(2, 16, 64)\n    aq = torch.randn(2, 8, 32)\n    L_emp = compute_empirical_lipschitz(acis, vis, aq, num_samples=20, epsilon=0.001)\n    print(f\"Empirical Lipschitz: {L_emp:.4f}\")\n",
      "numLines": 226,
      "startLine": 1,
      "totalLines": 226
    }
  }
}
```

</details>

---

### Tool call

_source line 29_

<details open><summary>🔧 Tool call — Read · `toolu_01Fahj1T7q8u84mu9kb42XTk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/imm/token_selection.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "263df5c0-d01d-4f96-a4cb-fd4145125851",
  "uuid": "989f2d87-e4fe-4842-9dc5-e138b3e65856",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P8fJNFF5YAX1pYssBKZQrR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 870,
      "cache_read_input_tokens": 26972,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 870
      },
      "output_tokens": 18,
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

_source line 30 · 2026-05-15T13:41:19.918Z_

<details><summary>↩ Tool result · `toolu_01Fahj1T7q8u84mu9kb42XTk`</summary>

```text
1	"""Margin-aware token selection: soft masking (train) / hard prune+merge (inference).
2	
3	Training: applies soft sigmoid mask to visual tokens (fully differentiable).
4	Inference: three-partition — preserve (top-k), prune (bottom), merge (borderline) —
5	           borderline tokens are weighted-averaged into their nearest preserved token.
6	
7	Inputs:  (B, N) scores, (B, N, D) visual tokens, integer k.
8	Depends: soft_topk.SoftTopK.
9	"""
10	
11	from __future__ import annotations
12	
13	import torch
14	import torch.nn as nn
15	import torch.nn.functional as F
16	from torch import Tensor
17	from typing import Dict, Tuple, Optional
18	
19	from .soft_topk import SoftTopK
20	
21	
22	class MarginAwareTokenSelector(nn.Module):
23	    def __init__(self, temperature: float = 1.0, merge_weight_temp: float = 0.5):
24	        super().__init__()
25	        self.soft_topk = SoftTopK(temperature=temperature, method="sigmoid")
26	        self.merge_weight_temp = merge_weight_temp
27	
28	    def forward(
29	        self,
30	        importance_scores: Tensor,
31	        visual_tokens: Tensor,
32	        k: int,
33	        training: bool = True,
34	    ) -> Tuple[Tensor, Tensor, Dict[str, Tensor]]:
35	        """
36	        Args:
37	            importance_scores: (B, N) per-token scores.
38	            visual_tokens:     (B, N, D) visual token embeddings.
39	            k: number of tokens to retain.
40	            training: soft mask (True) or hard prune/merge (False).
41	        Returns:
42	            selected_tokens: (B, N, D) soft-masked  or  (B, K', D) hard-selected.
43	            selection_mask:  (B, N) soft or binary mask.
44	            info: dict with diagnostic stats.
45	        """
46	        if training:
47	            return self._soft_forward(importance_scores, visual_tokens, k)
48	        return self._hard_forward(importance_scores, visual_tokens, k)
49	
50	    # ------------------------------------------------------------------
51	    def _soft_forward(
52	        self, scores: Tensor, tokens: Tensor, k: int
53	    ) -> Tuple[Tensor, Tensor, Dict[str, Tensor]]:
54	        mask, s_k, s_k1 = self.soft_topk(scores, k)
55	        selected = tokens * mask.unsqueeze(-1)  # (B, N, D)
56	        info = {
57	            "mode": torch.tensor(0),  # 0 = soft
58	            "mask_sum": mask.sum(-1).detach(),
59	            "margin": (s_k - s_k1).detach(),
60	        }
61	        return selected, mask, info
62	
63	    # ------------------------------------------------------------------
64	    def _hard_forward(
65	        self, scores: Tensor, tokens: Tensor, k: int
66	    ) -> Tuple[Tensor, Tensor, Dict[str, Tensor]]:
67	        B, N, D = tokens.shape
68	
69	        sorted_scores, sorted_idx = torch.sort(scores, dim=-1, descending=True)
70	        s_k = sorted_scores[:, k - 1]          # (B,) k-th largest score
71	        s_k_plus_1 = sorted_scores[:, k]       # (B,) (k+1)-th largest score
72	        delta_k = s_k - s_k_plus_1             # (B,) margin
73	
74	        threshold_high = (s_k + delta_k / 2).unsqueeze(-1)   # (B, 1)
75	        threshold_low = (s_k - delta_k / 2).unsqueeze(-1)    # (B, 1)
76	
77	        # Fixed top-k as preserved tokens (output length stays k)
78	        preserve_idx = sorted_idx[:, :k]                                 # (B, k)
79	        preserved_tokens = torch.gather(tokens, 1, preserve_idx.unsqueeze(-1).expand(-1, -1, D))
80	
81	        is_topk = torch.zeros(B, N, device=scores.device, dtype=torch.bool)
82	        is_topk.scatter_(1, preserve_idx, True)
83	
84	        # Margin-aware three-partition for non-top-k tokens
85	        borderline_mask = ~is_topk & (scores >= threshold_low.squeeze(-1)) & (scores <= threshold_high.squeeze(-1))
86	        prune_mask = ~is_topk & (scores < threshold_low.squeeze(-1))
87	        preserve_mask = is_topk
88	
89	        # Merge borderline tokens into nearest preserved token
90	        merged_tokens = self._merge_borderline_tokens(
91	            tokens, scores, preserved_tokens, preserve_idx, borderline_mask
92	        )
93	
94	        binary_mask = preserve_mask.float()
95	        info = {
96	            "mode": torch.tensor(1),  # 1 = hard
97	            "num_preserved": preserve_mask.sum(-1).float().detach(),
98	            "num_pruned": prune_mask.sum(-1).float().detach(),
99	            "num_merged": borderline_mask.sum(-1).float().detach(),
100	            "delta_k": delta_k.detach(),
101	        }
102	        return merged_tokens, binary_mask, info
103	
104	    # ------------------------------------------------------------------
105	    def _merge_borderline_tokens(
106	        self,
107	        tokens: Tensor,
108	        scores: Tensor,
109	        preserved_tokens: Tensor,
110	        preserve_idx: Tensor,
111	        borderline_mask: Tensor,
112	    ) -> Tensor:
113	        """Weighted-merge each borderline token into cosine-nearest preserved token."""
114	        B, N, D = tokens.shape
115	        K = preserved_tokens.shape[1]
116	
117	        num_borderline = borderline_mask.sum(-1)  # (B,)
118	        if num_borderline.sum() == 0:
119	            return preserved_tokens
120	
121	        # Cosine similarity: borderline -> preserved
122	        preserved_norm = F.normalize(preserved_tokens, dim=-1)  # (B, K, D)
123	        tokens_norm = F.normalize(tokens, dim=-1)               # (B, N, D)
124	
125	        # Similarity of all tokens to preserved tokens: (B, N, K)
126	        sim = torch.bmm(tokens_norm, preserved_norm.transpose(1, 2))
127	
128	        # For each borderline token, find best preserved match
129	        best_match = sim.argmax(dim=-1)  # (B, N) — index into K
130	
131	        # Importance-based merge weights
132	        preserve_scores = torch.gather(scores, 1, preserve_idx)  # (B, K)
133	
134	        merged = preserved_tokens.clone()
135	        # TODO: vectorize this loop for better GPU efficiency
136	        for b in range(B):
137	            border_idx = borderline_mask[b].nonzero(as_tuple=True)[0]
138	            if border_idx.numel() == 0:
139	                continue
140	            for idx in border_idx:
141	                target = best_match[b, idx].item()
142	                w_border = torch.sigmoid(scores[b, idx] / (self.merge_weight_temp + 1e-8))
143	                w_orig = torch.sigmoid(preserve_scores[b, target] / (self.merge_weight_temp + 1e-8))
144	                total_w = w_orig + w_border + 1e-8
145	                merged[b, target] = (w_orig / total_w) * merged[b, target] + (w_border / total_w) * tokens[b, idx]
146	
147	        return merged
148	
149	
150	if __name__ == "__main__":
151	    torch.manual_seed(42)
152	    B, N, D, k = 2, 32, 64, 8
153	    scores = torch.randn(B, N, requires_grad=True)
154	    tokens = torch.randn(B, N, D)
155	
156	    selector = MarginAwareTokenSelector(temperature=0.5)
157	
158	    # Training mode
159	    sel_train, mask_train, info_train = selector(scores, tokens, k, training=True)
160	    sel_train.sum().backward()
161	    print(f"[train] shape={sel_train.shape}, mask_sum={info_train['mask_sum']}, "
162	          f"grad OK={scores.grad is not None}")
163	    scores.grad = None
164	
165	    # Inference mode
166	    with torch.no_grad():
167	        sel_inf, mask_inf, info_inf = selector(scores, tokens, k, training=False)
168	    print(f"[infer] shape={sel_inf.shape}, preserved={info_inf['num_preserved']}, "
169	          f"pruned={info_inf['num_pruned']}, merged={info_inf['num_merged']}")
170	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "263df5c0-d01d-4f96-a4cb-fd4145125851",
  "uuid": "2f1fa6a2-742c-49aa-84e4-88944cd5dca8",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/imm/token_selection.py",
      "content": "\"\"\"Margin-aware token selection: soft masking (train) / hard prune+merge (inference).\n\nTraining: applies soft sigmoid mask to visual tokens (fully differentiable).\nInference: three-partition — preserve (top-k), prune (bottom), merge (borderline) —\n           borderline tokens are weighted-averaged into their nearest preserved token.\n\nInputs:  (B, N) scores, (B, N, D) visual tokens, integer k.\nDepends: soft_topk.SoftTopK.\n\"\"\"\n\nfrom __future__ import annotations\n\nimport torch\nimport torch.nn as nn\nimport torch.nn.functional as F\nfrom torch import Tensor\nfrom typing import Dict, Tuple, Optional\n\nfrom .soft_topk import SoftTopK\n\n\nclass MarginAwareTokenSelector(nn.Module):\n    def __init__(self, temperature: float = 1.0, merge_weight_temp: float = 0.5):\n        super().__init__()\n        self.soft_topk = SoftTopK(temperature=temperature, method=\"sigmoid\")\n        self.merge_weight_temp = merge_weight_temp\n\n    def forward(\n        self,\n        importance_scores: Tensor,\n        visual_tokens: Tensor,\n        k: int,\n        training: bool = True,\n    ) -> Tuple[Tensor, Tensor, Dict[str, Tensor]]:\n        \"\"\"\n        Args:\n            importance_scores: (B, N) per-token scores.\n            visual_tokens:     (B, N, D) visual token embeddings.\n            k: number of tokens to retain.\n            training: soft mask (True) or hard prune/merge (False).\n        Returns:\n            selected_tokens: (B, N, D) soft-masked  or  (B, K', D) hard-selected.\n            selection_mask:  (B, N) soft or binary mask.\n            info: dict with diagnostic stats.\n        \"\"\"\n        if training:\n            return self._soft_forward(importance_scores, visual_tokens, k)\n        return self._hard_forward(importance_scores, visual_tokens, k)\n\n    # ------------------------------------------------------------------\n    def _soft_forward(\n        self, scores: Tensor, tokens: Tensor, k: int\n    ) -> Tuple[Tensor, Tensor, Dict[str, Tensor]]:\n        mask, s_k, s_k1 = self.soft_topk(scores, k)\n        selected = tokens * mask.unsqueeze(-1)  # (B, N, D)\n        info = {\n            \"mode\": torch.tensor(0),  # 0 = soft\n            \"mask_sum\": mask.sum(-1).detach(),\n            \"margin\": (s_k - s_k1).detach(),\n        }\n        return selected, mask, info\n\n    # ------------------------------------------------------------------\n    def _hard_forward(\n        self, scores: Tensor, tokens: Tensor, k: int\n    ) -> Tuple[Tensor, Tensor, Dict[str, Tensor]]:\n        B, N, D = tokens.shape\n\n        sorted_scores, sorted_idx = torch.sort(scores, dim=-1, descending=True)\n        s_k = sorted_scores[:, k - 1]          # (B,) k-th largest score\n        s_k_plus_1 = sorted_scores[:, k]       # (B,) (k+1)-th largest score\n        delta_k = s_k - s_k_plus_1             # (B,) margin\n\n        threshold_high = (s_k + delta_k / 2).unsqueeze(-1)   # (B, 1)\n        threshold_low = (s_k - delta_k / 2).unsqueeze(-1)    # (B, 1)\n\n        # Fixed top-k as preserved tokens (output length stays k)\n        preserve_idx = sorted_idx[:, :k]                                 # (B, k)\n        preserved_tokens = torch.gather(tokens, 1, preserve_idx.unsqueeze(-1).expand(-1, -1, D))\n\n        is_topk = torch.zeros(B, N, device=scores.device, dtype=torch.bool)\n        is_topk.scatter_(1, preserve_idx, True)\n\n        # Margin-aware three-partition for non-top-k tokens\n        borderline_mask = ~is_topk & (scores >= threshold_low.squeeze(-1)) & (scores <= threshold_high.squeeze(-1))\n        prune_mask = ~is_topk & (scores < threshold_low.squeeze(-1))\n        preserve_mask = is_topk\n\n        # Merge borderline tokens into nearest preserved token\n        merged_tokens = self._merge_borderline_tokens(\n            tokens, scores, preserved_tokens, preserve_idx, borderline_mask\n        )\n\n        binary_mask = preserve_mask.float()\n        info = {\n            \"mode\": torch.tensor(1),  # 1 = hard\n            \"num_preserved\": preserve_mask.sum(-1).float().detach(),\n            \"num_pruned\": prune_mask.sum(-1).float().detach(),\n            \"num_merged\": borderline_mask.sum(-1).float().detach(),\n            \"delta_k\": delta_k.detach(),\n        }\n        return merged_tokens, binary_mask, info\n\n    # ------------------------------------------------------------------\n    def _merge_borderline_tokens(\n        self,\n        tokens: Tensor,\n        scores: Tensor,\n        preserved_tokens: Tensor,\n        preserve_idx: Tensor,\n        borderline_mask: Tensor,\n    ) -> Tensor:\n        \"\"\"Weighted-merge each borderline token into cosine-nearest preserved token.\"\"\"\n        B, N, D = tokens.shape\n        K = preserved_tokens.shape[1]\n\n        num_borderline = borderline_mask.sum(-1)  # (B,)\n        if num_borderline.sum() == 0:\n            return preserved_tokens\n\n        # Cosine similarity: borderline -> preserved\n        preserved_norm = F.normalize(preserved_tokens, dim=-1)  # (B, K, D)\n        tokens_norm = F.normalize(tokens, dim=-1)               # (B, N, D)\n\n        # Similarity of all tokens to preserved tokens: (B, N, K)\n        sim = torch.bmm(tokens_norm, preserved_norm.transpose(1, 2))\n\n        # For each borderline token, find best preserved match\n        best_match = sim.argmax(dim=-1)  # (B, N) — index into K\n\n        # Importance-based merge weights\n        preserve_scores = torch.gather(scores, 1, preserve_idx)  # (B, K)\n\n        merged = preserved_tokens.clone()\n        # TODO: vectorize this loop for better GPU efficiency\n        for b in range(B):\n            border_idx = borderline_mask[b].nonzero(as_tuple=True)[0]\n            if border_idx.numel() == 0:\n                continue\n            for idx in border_idx:\n                target = best_match[b, idx].item()\n                w_border = torch.sigmoid(scores[b, idx] / (self.merge_weight_temp + 1e-8))\n                w_orig = torch.sigmoid(preserve_scores[b, target] / (self.merge_weight_temp + 1e-8))\n                total_w = w_orig + w_border + 1e-8\n                merged[b, target] = (w_orig / total_w) * merged[b, target] + (w_border / total_w) * tokens[b, idx]\n\n        return merged\n\n\nif __name__ == \"__main__\":\n    torch.manual_seed(42)\n    B, N, D, k = 2, 32, 64, 8\n    scores = torch.randn(B, N, requires_grad=True)\n    tokens = torch.randn(B, N, D)\n\n    selector = MarginAwareTokenSelector(temperature=0.5)\n\n    # Training mode\n    sel_train, mask_train, info_train = selector(scores, tokens, k, training=True)\n    sel_train.sum().backward()\n    print(f\"[train] shape={sel_train.shape}, mask_sum={info_train['mask_sum']}, \"\n          f\"grad OK={scores.grad is not None}\")\n    scores.grad = None\n\n    # Inference mode\n    with torch.no_grad():\n        sel_inf, mask_inf, info_inf = selector(scores, tokens, k, training=False)\n    print(f\"[infer] shape={sel_inf.shape}, preserved={info_inf['num_preserved']}, \"\n          f\"pruned={info_inf['num_pruned']}, merged={info_inf['num_merged']}\")\n",
      "numLines": 170,
      "startLine": 1,
      "totalLines": 170
    }
  }
}
```

</details>

---

### Tool call

_source line 31_

<details open><summary>🔧 Tool call — Read · `toolu_01DzhrguPxqGSbKAW2LwDiNL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/imm/smolvla_wrapper.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "263df5c0-d01d-4f96-a4cb-fd4145125851",
  "uuid": "7c8fa246-a983-44b4-806a-7f7ddbdb4fb1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P8fJNFF5YAX1pYssBKZQrR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 870,
      "cache_read_input_tokens": 26972,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 870
      },
      "output_tokens": 18,
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

_source line 32 · 2026-05-15T13:41:20.819Z_

<details><summary>↩ Tool result · `toolu_01DzhrguPxqGSbKAW2LwDiNL`</summary>

```text
1	"""IMMSmolVLAWrapper — wraps SmolVLA forward pass with ACIS scoring + token selection.
2	
3	Data flow:
4	  Original:  images → SigLIP → connector → embed_prefix → VLM+Expert → loss
5	  Modified:  images → SigLIP → connector → [ACIS → soft top-k → mask] → rebuild_prefix → VLM+Expert → loss + L_margin
6	
7	Takes a full SmolVLAPolicy (not just model) to use its batch preprocessing.
8	Replicates embed_prefix internally to inject masked visual tokens before the
9	VLM+Expert forward pass, without modifying any lerobot source code.
10	
11	Depends: acis.ACIS, losses.IMMTotalLoss, token_selection.MarginAwareTokenSelector.
12	"""
13	
14	from __future__ import annotations
15	
16	import math
17	
18	import torch
19	import torch.nn as nn
20	import torch.nn.functional as F
21	from torch import Tensor
22	from typing import Any, Dict, List, Optional, Tuple
23	
24	from .acis import ACIS
25	from .losses import IMMTotalLoss
26	from .token_selection import MarginAwareTokenSelector
27	
28	try:
29	    from lerobot.utils.constants import (
30	        ACTION,
31	        OBS_LANGUAGE_ATTENTION_MASK,
32	        OBS_LANGUAGE_TOKENS,
33	        OBS_STATE,
34	    )
35	except ImportError:
36	    ACTION = "action"
37	    OBS_STATE = "observation.state"
38	    OBS_LANGUAGE_TOKENS = "observation.language.tokens"
39	    OBS_LANGUAGE_ATTENTION_MASK = "observation.language.attention_mask"
40	
41	
42	def _pad_tensor(tensor: Tensor, max_len: int, pad_value: float = 0) -> Tensor:
43	    """Pad tensor along dim=1 to max_len."""
44	    b, d = tensor.shape[:2]
45	    if d >= max_len:
46	        return tensor
47	    padded = torch.full(
48	        (b, max_len, *tensor.shape[2:]), pad_value, dtype=tensor.dtype, device=tensor.device
49	    )
50	    padded[:, :d] = tensor
51	    return padded
52	
53	
54	def _make_att_2d_masks(pad_masks: Tensor, att_masks: Tensor) -> Tensor:
55	    """Build 2D causal/prefix attention mask from 1D pad + attention-region masks.
56	
57	    att_masks uses cumsum convention: 0 = bidirectional block, 1 = new causal block.
58	    """
59	    cumsum = torch.cumsum(att_masks, dim=1)
60	    att_2d = cumsum[:, None, :] <= cumsum[:, :, None]
61	    pad_2d = pad_masks[:, None, :] * pad_masks[:, :, None]
62	    return att_2d & pad_2d
63	
64	
65	class IMMSmolVLAWrapper(nn.Module):
66	    """Wraps SmolVLAPolicy with ACIS importance scoring and margin-based token selection.
67	
68	    Args:
69	        smolvla_policy: SmolVLAPolicy instance (may have LoRA applied via PeftModel).
70	        acis_config: kwargs for ACIS (visual_dim, action_dim, num_heads, dropout).
71	        imm_config: kwargs for IMMTotalLoss + k_ratio.
72	    """
73	
74	    def __init__(
75	        self,
76	        smolvla_policy: Any,
77	        acis_config: Optional[Dict[str, Any]] = None,
78	        imm_config: Optional[Dict[str, Any]] = None,
79	    ):
80	        super().__init__()
81	        self.policy = smolvla_policy
82	        self.base_model = self._unwrap_to_vla(smolvla_policy.model)
83	
84	        acis_config = dict(acis_config or {})
85	        imm_config = dict(imm_config or {})
86	
87	        if "visual_dim" not in acis_config or "action_dim" not in acis_config:
88	            vlm_hidden = self.base_model.vlm_with_expert.config.text_config.hidden_size
89	            expert_hidden = self.base_model.vlm_with_expert.expert_hidden_size
90	            acis_config.setdefault("visual_dim", vlm_hidden)
91	            acis_config.setdefault("action_dim", expert_hidden)
92	
93	        self.acis = ACIS(**acis_config)
94	
95	        self.k_ratio = imm_config.pop("k_ratio", 0.5)
96	        selector_temp = imm_config.pop("selector_temperature", 1.0)
97	
98	        self.imm_loss = IMMTotalLoss(**imm_config)
99	        self.token_selector = MarginAwareTokenSelector(temperature=selector_temp)
100	
101	    @staticmethod
102	    def _unwrap_to_vla(model: nn.Module) -> nn.Module:
103	        """Unwrap PeftModel → LoraModel → VLAFlowMatching."""
104	        try:
105	            from peft import PeftModel
106	            if isinstance(model, PeftModel):
107	                return model.base_model.model
108	        except ImportError:
109	            pass
110	        return model
111	
112	    def _get_visual_tokens(self, images: List[Tensor]) -> Tuple[Tensor, List[int]]:
113	        """Encode each camera image through SigLIP+connector.
114	
115	        Returns:
116	            vis_tokens: (B, sum(n_i), D) concatenated visual tokens from all cameras.
117	            tokens_per_camera: list of token counts per camera.
118	        """
119	        all_vis = []
120	        tokens_per_camera = []
121	        for img in images:
122	            vis = self.base_model.vlm_with_expert.embed_image(img)
123	            all_vis.append(vis)
124	            tokens_per_camera.append(vis.shape[1])
125	        return torch.cat(all_vis, dim=1), tokens_per_camera
126	
127	    def _build_prefix_with_vis_tokens(
128	        self,
129	        vis_tokens: Tensor,
130	        tokens_per_camera: List[int],
131	        img_masks: List[Tensor],
132	        lang_tokens: Tensor,
133	        lang_masks: Tensor,
134	        state: Tensor,
135	    ) -> Tuple[Tensor, Tensor, Tensor]:
136	        """Reconstruct prefix embeddings using pre-computed (possibly masked) visual tokens.
137	
138	        Replicates VLAFlowMatching.embed_prefix() but substitutes the visual token
139	        computation with externally provided tokens (after ACIS masking).
140	
141	        Returns:
142	            embs:      (B, prefix_length, D)
143	            pad_masks: (B, prefix_length) bool
144	            att_masks: (B, prefix_length) bool/float
145	        """
146	        bm = self.base_model
147	        device = vis_tokens.device
148	        bsize = vis_tokens.shape[0]
149	
150	        embs: list[Tensor] = []
151	        pad_masks: list[Tensor] = []
152	        att_masks_list: list[int] = []
153	
154	        offset = 0
155	        for cam_idx, (n_tokens, img_mask) in enumerate(zip(tokens_per_camera, img_masks)):
156	            if bm.add_image_special_tokens:
157	                start_tok = (
158	                    bm.vlm_with_expert.embed_language_tokens(
159	                        bm.global_image_start_token.to(device=device)
160	                    )
161	                    .unsqueeze(0)
162	                    .expand(bsize, -1, -1)
163	                )
164	                start_mask = torch.ones(bsize, start_tok.shape[1], dtype=torch.bool, device=device)
165	                embs.append(start_tok)
166	                pad_masks.append(start_mask)
167	                att_masks_list += [0] * start_tok.shape[1]
168	
169	            img_emb = vis_tokens[:, offset : offset + n_tokens, :]
170	            offset += n_tokens
171	
172	            img_emb_dim = img_emb.shape[-1]
173	            img_emb = img_emb * torch.tensor(
174	                img_emb_dim**0.5, dtype=img_emb.dtype, device=device
175	            )
176	
177	            cam_mask = img_mask[:, None].expand(bsize, n_tokens)
178	            embs.append(img_emb)
179	            pad_masks.append(cam_mask)
180	            att_masks_list += [0] * n_tokens
181	
182	            if bm.add_image_special_tokens:
183	                end_tok = (
184	                    bm.vlm_with_expert.embed_language_tokens(
185	                        bm.image_end_token.to(device=device)
186	                    )
187	                    .unsqueeze(0)
188	                    .expand(bsize, -1, -1)
189	                )
190	                end_mask = torch.ones(bsize, end_tok.shape[1], dtype=torch.bool, device=device)
191	                embs.append(end_tok)
192	                pad_masks.append(end_mask)
193	                att_masks_list += [0] * end_tok.shape[1]
194	
195	        lang_emb = bm.vlm_with_expert.embed_language_tokens(lang_tokens)
196	        lang_emb = lang_emb * math.sqrt(lang_emb.shape[-1])
197	        embs.append(lang_emb)
198	        pad_masks.append(lang_masks)
199	        att_masks_list += [0] * lang_emb.shape[1]
200	
201	        state_emb = bm.state_proj(state)
202	        if state_emb.ndim == 2:
203	            state_emb = state_emb[:, None, :]
204	        states_seq = state_emb.shape[1]
205	        state_mask = torch.ones(bsize, states_seq, dtype=torch.bool, device=device)
206	        embs.append(state_emb)
207	        pad_masks.append(state_mask)
208	        att_masks_list += [1] * states_seq
209	
210	        embs_cat = torch.cat(embs, dim=1)
211	        pad_cat = torch.cat(pad_masks, dim=1)
212	        att_cat = torch.tensor(att_masks_list, dtype=torch.bool, device=device).unsqueeze(0)
213	
214	        prefix_len = bm.prefix_length
215	        if pad_cat.shape[1] < prefix_len:
216	            embs_cat = _pad_tensor(embs_cat, prefix_len, pad_value=0)
217	            pad_cat = _pad_tensor(pad_cat, prefix_len, pad_value=0)
218	            att_cat = _pad_tensor(att_cat, prefix_len, pad_value=0)
219	
220	        att_cat = att_cat.expand(bsize, -1)
221	        return embs_cat, pad_cat, att_cat
222	
223	    def forward(
224	        self, batch: Dict[str, Tensor], step: int = 0
225	    ) -> Tuple[Tensor, Dict[str, Any]]:
226	        """Full IMM forward: ACIS scoring → token selection → VLM+Expert → action + margin loss.
227	
228	        Args:
229	            batch: LeRobot-format batch with observation.images.*, observation.state,
230	                   observation.language.tokens, observation.language.attention_mask, action.
231	            step: current training step (for margin loss warmup).
232	        Returns:
233	            total_loss: scalar.
234	            info: dict with diagnostics (importance_scores, k, margin, lipschitz, etc.).
235	        """
236	        bm = self.base_model
237	
238	        images, img_masks = self.policy.prepare_images(batch)
239	        state = self.policy.prepare_state(batch)
240	        lang_tokens = batch[OBS_LANGUAGE_TOKENS]
241	        lang_masks = batch[OBS_LANGUAGE_ATTENTION_MASK]
242	        actions = self.policy.prepare_action(batch)
243	
244	        vis_tokens, tokens_per_cam = self._get_visual_tokens(images)
245	
246	        noise = bm.sample_noise(actions.shape, actions.device)
247	        time = bm.sample_time(actions.shape[0], actions.device)
248	        time_expanded = time[:, None, None]
249	        x_t = time_expanded * noise + (1 - time_expanded) * actions
250	        u_t = noise - actions
251	
252	        suffix_embs, suffix_pad, suffix_att = bm.embed_suffix(x_t, time)
253	
254	        importance_scores = self.acis(suffix_embs, vis_tokens)
255	
256	        N_vis = vis_tokens.shape[1]
257	        k = max(1, int(N_vis * self.k_ratio))
258	        selected_tokens, mask, sel_info = self.token_selector(
259	            importance_scores, vis_tokens, k, training=self.training
260	        )
261	
262	        prefix_embs, prefix_pad, prefix_att = self._build_prefix_with_vis_tokens(
263	            selected_tokens, tokens_per_cam, img_masks, lang_tokens, lang_masks, state
264	        )
265	
266	        all_pad = torch.cat([prefix_pad, suffix_pad], dim=1)
267	        all_att = torch.cat([prefix_att, suffix_att], dim=1)
268	        att_2d = _make_att_2d_masks(all_pad, all_att)
269	        position_ids = torch.cumsum(all_pad, dim=1) - 1
270	
271	        (_, suffix_out), _ = bm.vlm_with_expert.forward(
272	            attention_mask=att_2d,
273	            position_ids=position_ids,
274	            past_key_values=None,
275	            inputs_embeds=[prefix_embs, suffix_embs],
276	            use_cache=False,
277	            fill_kv_cache=False,
278	        )
279	
280	        chunk_size = bm.config.chunk_size
281	        suffix_out = suffix_out[:, -chunk_size:]
282	        suffix_out = suffix_out.to(dtype=torch.float32)
283	        v_t = bm.action_out_proj(suffix_out)
284	
285	        action_dim = self.policy.config.action_feature.shape[0]
286	        action_loss = F.mse_loss(
287	            u_t[:, :, :action_dim],
288	            v_t[:, :, :action_dim],
289	        )
290	
291	        total_loss, imm_info = self.imm_loss(action_loss, importance_scores, k, step)
292	
293	        info = {
294	            **sel_info,
295	            **imm_info,
296	            "importance_scores": importance_scores.detach(),
297	            "k": k,
298	            "k_ratio": self.k_ratio,
299	            "lipschitz_estimate": self.acis.get_lipschitz_estimate(),
300	        }
301	        return total_loss, info
302	
303	    def forward_baseline(self, batch: Dict[str, Tensor]) -> Tuple[Tensor, Dict[str, Any]]:
304	        """Baseline forward: delegate to the original SmolVLAPolicy (no ACIS)."""
305	        loss, loss_dict = self.policy.forward(batch)
306	        return loss, {"action_loss": loss.detach().item() if loss.dim() == 0 else loss.detach()}
307	
308	    @torch.no_grad()
309	    def compute_importance_scores(
310	        self, batch: Dict[str, Tensor]
311	    ) -> Tuple[Tensor, int]:
312	        """Extract ACIS scores without running full forward (for evaluation)."""
313	        bm = self.base_model
314	
315	        images, _ = self.policy.prepare_images(batch)
316	        vis_tokens, _ = self._get_visual_tokens(images)
317	
318	        actions = self.policy.prepare_action(batch)
319	        noise = bm.sample_noise(actions.shape, actions.device)
320	        time = bm.sample_time(actions.shape[0], actions.device)
321	        time_expanded = time[:, None, None]
322	        x_t = time_expanded * noise + (1 - time_expanded) * actions
323	
324	        suffix_embs, _, _ = bm.embed_suffix(x_t, time)
325	        scores = self.acis(suffix_embs, vis_tokens)
326	
327	        N_vis = vis_tokens.shape[1]
328	        k = max(1, int(N_vis * self.k_ratio))
329	        return scores, k
330	
331	
332	# ---------------------------------------------------------------------------
333	# Minimal mock for standalone testing (no lerobot dependency)
334	# ---------------------------------------------------------------------------
335	class _MockConfig:
336	    def __init__(self, action_dim=32, chunk_size=50, prefix_length=-1):
337	        self.chunk_size = chunk_size
338	        self.prefix_length = prefix_length
339	        self.max_action_dim = action_dim
340	        self.action_feature = type("F", (), {"shape": (action_dim,)})()
341	        self.image_features = ["observation.images.agentview", "observation.images.wrist"]
342	
343	
344	class _MockTextConfig:
345	    def __init__(self, hidden_size=960):
346	        self.hidden_size = hidden_size
347	
348	
349	class _MockVLMConfig:
350	    def __init__(self, hidden_size=960):
351	        self.text_config = _MockTextConfig(hidden_size)
352	
353	
354	class _MockVLMWithExpert(nn.Module):
355	    def __init__(self, hidden_dim=960, expert_hidden=720):
356	        super().__init__()
357	        self.embed_proj = nn.Linear(3 * 224 * 224, hidden_dim)
358	        self.lang_embed = nn.Embedding(1000, hidden_dim)
359	        self.expert_hidden_size = expert_hidden
360	        self.config = _MockVLMConfig(hidden_dim)
361	
362	    def embed_image(self, image: Tensor) -> Tensor:
363	        B = image.shape[0]
364	        D = self.config.text_config.hidden_size
365	        return torch.randn(B, 64, D, device=image.device, dtype=image.dtype)
366	
367	    def embed_language_tokens(self, tokens: Tensor) -> Tensor:
368	        if tokens.dtype in (torch.float32, torch.float16, torch.bfloat16):
369	            return tokens
370	        return self.lang_embed(tokens.clamp(0, 999))
371	
372	    def forward(self, attention_mask, position_ids, past_key_values,
373	                inputs_embeds, use_cache, fill_kv_cache):
374	        prefix, suffix = inputs_embeds
375	        B = suffix.shape[0]
376	        suffix_out = torch.randn_like(suffix)
377	        return (prefix, suffix_out), None
378	
379	
380	class _MockVLAFlowMatching(nn.Module):
381	    def __init__(self, hidden_dim=960, expert_hidden=720, action_dim=7, chunk_size=50):
382	        super().__init__()
383	        self.vlm_with_expert = _MockVLMWithExpert(hidden_dim, expert_hidden)
384	        self.state_proj = nn.Linear(32, hidden_dim)
385	        self.action_in_proj = nn.Linear(action_dim, expert_hidden)
386	        self.action_out_proj = nn.Linear(expert_hidden, action_dim)
387	        self.action_time_mlp_in = nn.Linear(expert_hidden * 2, expert_hidden)
388	        self.action_time_mlp_out = nn.Linear(expert_hidden, expert_hidden)
389	        self.add_image_special_tokens = False
390	        self.prefix_length = -1
391	        self.config = _MockConfig(action_dim, chunk_size, prefix_length=-1)
392	        self.global_image_start_token = torch.tensor([0, 1], dtype=torch.long)
393	        self.image_end_token = torch.tensor([0], dtype=torch.long)
394	
395	    def sample_noise(self, shape, device):
396	        return torch.randn(shape, device=device)
397	
398	    def sample_time(self, bsize, device):
399	        return torch.rand(bsize, device=device) * 0.998 + 0.001
400	
401	    def embed_suffix(self, noisy_actions, timestep):
402	        action_emb = self.action_in_proj(noisy_actions)
403	        B, T, D = action_emb.shape
404	        device = action_emb.device
405	        time_emb = timestep[:, None, None].expand(B, T, D)
406	        fused = self.action_time_mlp_out(F.silu(self.action_time_mlp_in(
407	            torch.cat([action_emb, time_emb], dim=-1)
408	        )))
409	        pad_masks = torch.ones(B, T, dtype=torch.bool, device=device)
410	        att_masks = torch.ones(B, T, dtype=fused.dtype, device=device)
411	        return fused, pad_masks, att_masks
412	
413	
414	class _MockSmolVLAPolicy:
415	    """Mimics SmolVLAPolicy interface for standalone testing."""
416	
417	    def __init__(self, action_dim=32, state_dim=32, chunk_size=50, num_cameras=2,
418	                 hidden_dim=960, expert_hidden=720):
419	        self.model = _MockVLAFlowMatching(
420	            hidden_dim=hidden_dim, expert_hidden=expert_hidden,
421	            action_dim=action_dim, chunk_size=chunk_size,
422	        )
423	        self.config = _MockConfig(action_dim, chunk_size)
424	        self._num_cameras = num_cameras
425	        self._state_dim = state_dim
426	        self._action_dim = action_dim
427	
428	    def prepare_images(self, batch):
429	        images = []
430	        img_masks = []
431	        for key in self.config.image_features[:self._num_cameras]:
432	            if key in batch:
433	                img = batch[key]
434	            else:
435	                img = torch.randn(
436	                    list(batch.values())[0].shape[0], 3, 224, 224,
437	                    device=list(batch.values())[0].device,
438	                )
439	            B = img.shape[0]
440	            images.append(img)
441	            img_masks.append(torch.ones(B, dtype=torch.bool, device=img.device))
442	        return images, img_masks
443	
444	    def prepare_state(self, batch):
445	        if OBS_STATE in batch:
446	            return batch[OBS_STATE]
447	        B = list(batch.values())[0].shape[0]
448	        device = list(batch.values())[0].device
449	        return torch.randn(B, self._state_dim, device=device)
450	
451	    def prepare_action(self, batch):
452	        if ACTION in batch:
453	            return batch[ACTION]
454	        B = list(batch.values())[0].shape[0]
455	        device = list(batch.values())[0].device
456	        return torch.randn(B, self.config.chunk_size, self._action_dim, device=device)
457	
458	    def forward(self, batch, **kwargs):
459	        B = list(batch.values())[0].shape[0]
460	        device = list(batch.values())[0].device
461	        loss = torch.tensor(1.0, device=device, requires_grad=True)
462	        return loss, {"loss": 1.0}
463	
464	
465	if __name__ == "__main__":
466	    torch.manual_seed(42)
467	    B = 2
468	    device = "cpu"
469	
470	    HIDDEN = 960
471	    EXPERT = 720
472	    ACTION_DIM = 32
473	    mock_policy = _MockSmolVLAPolicy(
474	        action_dim=ACTION_DIM, state_dim=32, chunk_size=50, num_cameras=2,
475	        hidden_dim=HIDDEN, expert_hidden=EXPERT,
476	    )
477	    wrapper = IMMSmolVLAWrapper(
478	        smolvla_policy=mock_policy,
479	        acis_config={"num_heads": 8},
480	        imm_config={"lambda_margin": 0.1, "delta": 0.5, "warmup_steps": 100, "k_ratio": 0.5},
481	    )
482	
483	    batch = {
484	        "observation.images.agentview": torch.randn(B, 3, 224, 224),
485	        "observation.images.wrist": torch.randn(B, 3, 224, 224),
486	        ACTION: torch.randn(B, 50, ACTION_DIM),
487	        OBS_STATE: torch.randn(B, 32),
488	        OBS_LANGUAGE_TOKENS: torch.randint(0, 100, (B, 20)),
489	        OBS_LANGUAGE_ATTENTION_MASK: torch.ones(B, 20, dtype=torch.bool),
490	    }
491	
492	    wrapper.train()
493	    total_loss, info = wrapper(batch, step=50)
494	    total_loss.backward()
495	    print(f"[train] total_loss={total_loss.item():.4f}, k={info['k']}, "
496	          f"lipschitz={info['lipschitz_estimate']:.4f}")
497	
498	    base_loss, base_info = wrapper.forward_baseline(batch)
499	    print(f"[baseline] action_loss={base_loss.item():.4f}")
500	
501	    wrapper.eval()
502	    scores, k = wrapper.compute_importance_scores(batch)
503	    print(f"[eval] scores shape={scores.shape}, k={k}")
504	    print("All wrapper tests passed!")
505	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "263df5c0-d01d-4f96-a4cb-fd4145125851",
  "uuid": "140da013-7335-43e0-8d1a-d94f423fe115",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/imm/smolvla_wrapper.py",
      "content": "\"\"\"IMMSmolVLAWrapper — wraps SmolVLA forward pass with ACIS scoring + token selection.\n\nData flow:\n  Original:  images → SigLIP → connector → embed_prefix → VLM+Expert → loss\n  Modified:  images → SigLIP → connector → [ACIS → soft top-k → mask] → rebuild_prefix → VLM+Expert → loss + L_margin\n\nTakes a full SmolVLAPolicy (not just model) to use its batch preprocessing.\nReplicates embed_prefix internally to inject masked visual tokens before the\nVLM+Expert forward pass, without modifying any lerobot source code.\n\nDepends: acis.ACIS, losses.IMMTotalLoss, token_selection.MarginAwareTokenSelector.\n\"\"\"\n\nfrom __future__ import annotations\n\nimport math\n\nimport torch\nimport torch.nn as nn\nimport torch.nn.functional as F\nfrom torch import Tensor\nfrom typing import Any, Dict, List, Optional, Tuple\n\nfrom .acis import ACIS\nfrom .losses import IMMTotalLoss\nfrom .token_selection import MarginAwareTokenSelector\n\ntry:\n    from lerobot.utils.constants import (\n        ACTION,\n        OBS_LANGUAGE_ATTENTION_MASK,\n        OBS_LANGUAGE_TOKENS,\n        OBS_STATE,\n    )\nexcept ImportError:\n    ACTION = \"action\"\n    OBS_STATE = \"observation.state\"\n    OBS_LANGUAGE_TOKENS = \"observation.language.tokens\"\n    OBS_LANGUAGE_ATTENTION_MASK = \"observation.language.attention_mask\"\n\n\ndef _pad_tensor(tensor: Tensor, max_len: int, pad_value: float = 0) -> Tensor:\n    \"\"\"Pad tensor along dim=1 to max_len.\"\"\"\n    b, d = tensor.shape[:2]\n    if d >= max_len:\n        return tensor\n    padded = torch.full(\n        (b, max_len, *tensor.shape[2:]), pad_value, dtype=tensor.dtype, device=tensor.device\n    )\n    padded[:, :d] = tensor\n    return padded\n\n\ndef _make_att_2d_masks(pad_masks: Tensor, att_masks: Tensor) -> Tensor:\n    \"\"\"Build 2D causal/prefix attention mask from 1D pad + attention-region masks.\n\n    att_masks uses cumsum convention: 0 = bidirectional block, 1 = new causal block.\n    \"\"\"\n    cumsum = torch.cumsum(att_masks, dim=1)\n    att_2d = cumsum[:, None, :] <= cumsum[:, :, None]\n    pad_2d = pad_masks[:, None, :] * pad_masks[:, :, None]\n    return att_2d & pad_2d\n\n\nclass IMMSmolVLAWrapper(nn.Module):\n    \"\"\"Wraps SmolVLAPolicy with ACIS importance scoring and margin-based token selection.\n\n    Args:\n        smolvla_policy: SmolVLAPolicy instance (may have LoRA applied via PeftModel).\n        acis_config: kwargs for ACIS (visual_dim, action_dim, num_heads, dropout).\n        imm_config: kwargs for IMMTotalLoss + k_ratio.\n    \"\"\"\n\n    def __init__(\n        self,\n        smolvla_policy: Any,\n        acis_config: Optional[Dict[str, Any]] = None,\n        imm_config: Optional[Dict[str, Any]] = None,\n    ):\n        super().__init__()\n        self.policy = smolvla_policy\n        self.base_model = self._unwrap_to_vla(smolvla_policy.model)\n\n        acis_config = dict(acis_config or {})\n        imm_config = dict(imm_config or {})\n\n        if \"visual_dim\" not in acis_config or \"action_dim\" not in acis_config:\n            vlm_hidden = self.base_model.vlm_with_expert.config.text_config.hidden_size\n            expert_hidden = self.base_model.vlm_with_expert.expert_hidden_size\n            acis_config.setdefault(\"visual_dim\", vlm_hidden)\n            acis_config.setdefault(\"action_dim\", expert_hidden)\n\n        self.acis = ACIS(**acis_config)\n\n        self.k_ratio = imm_config.pop(\"k_ratio\", 0.5)\n        selector_temp = imm_config.pop(\"selector_temperature\", 1.0)\n\n        self.imm_loss = IMMTotalLoss(**imm_config)\n        self.token_selector = MarginAwareTokenSelector(temperature=selector_temp)\n\n    @staticmethod\n    def _unwrap_to_vla(model: nn.Module) -> nn.Module:\n        \"\"\"Unwrap PeftModel → LoraModel → VLAFlowMatching.\"\"\"\n        try:\n            from peft import PeftModel\n            if isinstance(model, PeftModel):\n                return model.base_model.model\n        except ImportError:\n            pass\n        return model\n\n    def _get_visual_tokens(self, images: List[Tensor]) -> Tuple[Tensor, List[int]]:\n        \"\"\"Encode each camera image through SigLIP+connector.\n\n        Returns:\n            vis_tokens: (B, sum(n_i), D) concatenated visual tokens from all cameras.\n            tokens_per_camera: list of token counts per camera.\n        \"\"\"\n        all_vis = []\n        tokens_per_camera = []\n        for img in images:\n            vis = self.base_model.vlm_with_expert.embed_image(img)\n            all_vis.append(vis)\n            tokens_per_camera.append(vis.shape[1])\n        return torch.cat(all_vis, dim=1), tokens_per_camera\n\n    def _build_prefix_with_vis_tokens(\n        self,\n        vis_tokens: Tensor,\n        tokens_per_camera: List[int],\n        img_masks: List[Tensor],\n        lang_tokens: Tensor,\n        lang_masks: Tensor,\n        state: Tensor,\n    ) -> Tuple[Tensor, Tensor, Tensor]:\n        \"\"\"Reconstruct prefix embeddings using pre-computed (possibly masked) visual tokens.\n\n        Replicates VLAFlowMatching.embed_prefix() but substitutes the visual token\n        computation with externally provided tokens (after ACIS masking).\n\n        Returns:\n            embs:      (B, prefix_length, D)\n            pad_masks: (B, prefix_length) bool\n            att_masks: (B, prefix_length) bool/float\n        \"\"\"\n        bm = self.base_model\n        device = vis_tokens.device\n        bsize = vis_tokens.shape[0]\n\n        embs: list[Tensor] = []\n        pad_masks: list[Tensor] = []\n        att_masks_list: list[int] = []\n\n        offset = 0\n        for cam_idx, (n_tokens, img_mask) in enumerate(zip(tokens_per_camera, img_masks)):\n            if bm.add_image_special_tokens:\n                start_tok = (\n                    bm.vlm_with_expert.embed_language_tokens(\n                        bm.global_image_start_token.to(device=device)\n                    )\n                    .unsqueeze(0)\n                    .expand(bsize, -1, -1)\n                )\n                start_mask = torch.ones(bsize, start_tok.shape[1], dtype=torch.bool, device=device)\n                embs.append(start_tok)\n                pad_masks.append(start_mask)\n                att_masks_list += [0] * start_tok.shape[1]\n\n            img_emb = vis_tokens[:, offset : offset + n_tokens, :]\n            offset += n_tokens\n\n            img_emb_dim = img_emb.shape[-1]\n            img_emb = img_emb * torch.tensor(\n                img_emb_dim**0.5, dtype=img_emb.dtype, device=device\n            )\n\n            cam_mask = img_mask[:, None].expand(bsize, n_tokens)\n            embs.append(img_emb)\n            pad_masks.append(cam_mask)\n            att_masks_list += [0] * n_tokens\n\n            if bm.add_image_special_tokens:\n                end_tok = (\n                    bm.vlm_with_expert.embed_language_tokens(\n                        bm.image_end_token.to(device=device)\n                    )\n                    .unsqueeze(0)\n                    .expand(bsize, -1, -1)\n                )\n                end_mask = torch.ones(bsize, end_tok.shape[1], dtype=torch.bool, device=device)\n                embs.append(end_tok)\n                pad_masks.append(end_mask)\n                att_masks_list += [0] * end_tok.shape[1]\n\n        lang_emb = bm.vlm_with_expert.embed_language_tokens(lang_tokens)\n        lang_emb = lang_emb * math.sqrt(lang_emb.shape[-1])\n        embs.append(lang_emb)\n        pad_masks.append(lang_masks)\n        att_masks_list += [0] * lang_emb.shape[1]\n\n        state_emb = bm.state_proj(state)\n        if state_emb.ndim == 2:\n            state_emb = state_emb[:, None, :]\n        states_seq = state_emb.shape[1]\n        state_mask = torch.ones(bsize, states_seq, dtype=torch.bool, device=device)\n        embs.append(state_emb)\n        pad_masks.append(state_mask)\n        att_masks_list += [1] * states_seq\n\n        embs_cat = torch.cat(embs, dim=1)\n        pad_cat = torch.cat(pad_masks, dim=1)\n        att_cat = torch.tensor(att_masks_list, dtype=torch.bool, device=device).unsqueeze(0)\n\n        prefix_len = bm.prefix_length\n        if pad_cat.shape[1] < prefix_len:\n            embs_cat = _pad_tensor(embs_cat, prefix_len, pad_value=0)\n            pad_cat = _pad_tensor(pad_cat, prefix_len, pad_value=0)\n            att_cat = _pad_tensor(att_cat, prefix_len, pad_value=0)\n\n        att_cat = att_cat.expand(bsize, -1)\n        return embs_cat, pad_cat, att_cat\n\n    def forward(\n        self, batch: Dict[str, Tensor], step: int = 0\n    ) -> Tuple[Tensor, Dict[str, Any]]:\n        \"\"\"Full IMM forward: ACIS scoring → token selection → VLM+Expert → action + margin loss.\n\n        Args:\n            batch: LeRobot-format batch with observation.images.*, observation.state,\n                   observation.language.tokens, observation.language.attention_mask, action.\n            step: current training step (for margin loss warmup).\n        Returns:\n            total_loss: scalar.\n            info: dict with diagnostics (importance_scores, k, margin, lipschitz, etc.).\n        \"\"\"\n        bm = self.base_model\n\n        images, img_masks = self.policy.prepare_images(batch)\n        state = self.policy.prepare_state(batch)\n        lang_tokens = batch[OBS_LANGUAGE_TOKENS]\n        lang_masks = batch[OBS_LANGUAGE_ATTENTION_MASK]\n        actions = self.policy.prepare_action(batch)\n\n        vis_tokens, tokens_per_cam = self._get_visual_tokens(images)\n\n        noise = bm.sample_noise(actions.shape, actions.device)\n        time = bm.sample_time(actions.shape[0], actions.device)\n        time_expanded = time[:, None, None]\n        x_t = time_expanded * noise + (1 - time_expanded) * actions\n        u_t = noise - actions\n\n        suffix_embs, suffix_pad, suffix_att = bm.embed_suffix(x_t, time)\n\n        importance_scores = self.acis(suffix_embs, vis_tokens)\n\n        N_vis = vis_tokens.shape[1]\n        k = max(1, int(N_vis * self.k_ratio))\n        selected_tokens, mask, sel_info = self.token_selector(\n            importance_scores, vis_tokens, k, training=self.training\n        )\n\n        prefix_embs, prefix_pad, prefix_att = self._build_prefix_with_vis_tokens(\n            selected_tokens, tokens_per_cam, img_masks, lang_tokens, lang_masks, state\n        )\n\n        all_pad = torch.cat([prefix_pad, suffix_pad], dim=1)\n        all_att = torch.cat([prefix_att, suffix_att], dim=1)\n        att_2d = _make_att_2d_masks(all_pad, all_att)\n        position_ids = torch.cumsum(all_pad, dim=1) - 1\n\n        (_, suffix_out), _ = bm.vlm_with_expert.forward(\n            attention_mask=att_2d,\n            position_ids=position_ids,\n            past_key_values=None,\n            inputs_embeds=[prefix_embs, suffix_embs],\n            use_cache=False,\n            fill_kv_cache=False,\n        )\n\n        chunk_size = bm.config.chunk_size\n        suffix_out = suffix_out[:, -chunk_size:]\n        suffix_out = suffix_out.to(dtype=torch.float32)\n        v_t = bm.action_out_proj(suffix_out)\n\n        action_dim = self.policy.config.action_feature.shape[0]\n        action_loss = F.mse_loss(\n            u_t[:, :, :action_dim],\n            v_t[:, :, :action_dim],\n        )\n\n        total_loss, imm_info = self.imm_loss(action_loss, importance_scores, k, step)\n\n        info = {\n            **sel_info,\n            **imm_info,\n            \"importance_scores\": importance_scores.detach(),\n            \"k\": k,\n            \"k_ratio\": self.k_ratio,\n            \"lipschitz_estimate\": self.acis.get_lipschitz_estimate(),\n        }\n        return total_loss, info\n\n    def forward_baseline(self, batch: Dict[str, Tensor]) -> Tuple[Tensor, Dict[str, Any]]:\n        \"\"\"Baseline forward: delegate to the original SmolVLAPolicy (no ACIS).\"\"\"\n        loss, loss_dict = self.policy.forward(batch)\n        return loss, {\"action_loss\": loss.detach().item() if loss.dim() == 0 else loss.detach()}\n\n    @torch.no_grad()\n    def compute_importance_scores(\n        self, batch: Dict[str, Tensor]\n    ) -> Tuple[Tensor, int]:\n        \"\"\"Extract ACIS scores without running full forward (for evaluation).\"\"\"\n        bm = self.base_model\n\n        images, _ = self.policy.prepare_images(batch)\n        vis_tokens, _ = self._get_visual_tokens(images)\n\n        actions = self.policy.prepare_action(batch)\n        noise = bm.sample_noise(actions.shape, actions.device)\n        time = bm.sample_time(actions.shape[0], actions.device)\n        time_expanded = time[:, None, None]\n        x_t = time_expanded * noise + (1 - time_expanded) * actions\n\n        suffix_embs, _, _ = bm.embed_suffix(x_t, time)\n        scores = self.acis(suffix_embs, vis_tokens)\n\n        N_vis = vis_tokens.shape[1]\n        k = max(1, int(N_vis * self.k_ratio))\n        return scores, k\n\n\n# ---------------------------------------------------------------------------\n# Minimal mock for standalone testing (no lerobot dependency)\n# ---------------------------------------------------------------------------\nclass _MockConfig:\n    def __init__(self, action_dim=32, chunk_size=50, prefix_length=-1):\n        self.chunk_size = chunk_size\n        self.prefix_length = prefix_length\n        self.max_action_dim = action_dim\n        self.action_feature = type(\"F\", (), {\"shape\": (action_dim,)})()\n        self.image_features = [\"observation.images.agentview\", \"observation.images.wrist\"]\n\n\nclass _MockTextConfig:\n    def __init__(self, hidden_size=960):\n        self.hidden_size = hidden_size\n\n\nclass _MockVLMConfig:\n    def __init__(self, hidden_size=960):\n        self.text_config = _MockTextConfig(hidden_size)\n\n\nclass _MockVLMWithExpert(nn.Module):\n    def __init__(self, hidden_dim=960, expert_hidden=720):\n        super().__init__()\n        self.embed_proj = nn.Linear(3 * 224 * 224, hidden_dim)\n        self.lang_embed = nn.Embedding(1000, hidden_dim)\n        self.expert_hidden_size = expert_hidden\n        self.config = _MockVLMConfig(hidden_dim)\n\n    def embed_image(self, image: Tensor) -> Tensor:\n        B = image.shape[0]\n        D = self.config.text_config.hidden_size\n        return torch.randn(B, 64, D, device=image.device, dtype=image.dtype)\n\n    def embed_language_tokens(self, tokens: Tensor) -> Tensor:\n        if tokens.dtype in (torch.float32, torch.float16, torch.bfloat16):\n            return tokens\n        return self.lang_embed(tokens.clamp(0, 999))\n\n    def forward(self, attention_mask, position_ids, past_key_values,\n                inputs_embeds, use_cache, fill_kv_cache):\n        prefix, suffix = inputs_embeds\n        B = suffix.shape[0]\n        suffix_out = torch.randn_like(suffix)\n        return (prefix, suffix_out), None\n\n\nclass _MockVLAFlowMatching(nn.Module):\n    def __init__(self, hidden_dim=960, expert_hidden=720, action_dim=7, chunk_size=50):\n        super().__init__()\n        self.vlm_with_expert = _MockVLMWithExpert(hidden_dim, expert_hidden)\n        self.state_proj = nn.Linear(32, hidden_dim)\n        self.action_in_proj = nn.Linear(action_dim, expert_hidden)\n        self.action_out_proj = nn.Linear(expert_hidden, action_dim)\n        self.action_time_mlp_in = nn.Linear(expert_hidden * 2, expert_hidden)\n        self.action_time_mlp_out = nn.Linear(expert_hidden, expert_hidden)\n        self.add_image_special_tokens = False\n        self.prefix_length = -1\n        self.config = _MockConfig(action_dim, chunk_size, prefix_length=-1)\n        self.global_image_start_token = torch.tensor([0, 1], dtype=torch.long)\n        self.image_end_token = torch.tensor([0], dtype=torch.long)\n\n    def sample_noise(self, shape, device):\n        return torch.randn(shape, device=device)\n\n    def sample_time(self, bsize, device):\n        return torch.rand(bsize, device=device) * 0.998 + 0.001\n\n    def embed_suffix(self, noisy_actions, timestep):\n        action_emb = self.action_in_proj(noisy_actions)\n        B, T, D = action_emb.shape\n        device = action_emb.device\n        time_emb = timestep[:, None, None].expand(B, T, D)\n        fused = self.action_time_mlp_out(F.silu(self.action_time_mlp_in(\n            torch.cat([action_emb, time_emb], dim=-1)\n        )))\n        pad_masks = torch.ones(B, T, dtype=torch.bool, device=device)\n        att_masks = torch.ones(B, T, dtype=fused.dtype, device=device)\n        return fused, pad_masks, att_masks\n\n\nclass _MockSmolVLAPolicy:\n    \"\"\"Mimics SmolVLAPolicy interface for standalone testing.\"\"\"\n\n    def __init__(self, action_dim=32, state_dim=32, chunk_size=50, num_cameras=2,\n                 hidden_dim=960, expert_hidden=720):\n        self.model = _MockVLAFlowMatching(\n            hidden_dim=hidden_dim, expert_hidden=expert_hidden,\n            action_dim=action_dim, chunk_size=chunk_size,\n        )\n        self.config = _MockConfig(action_dim, chunk_size)\n        self._num_cameras = num_cameras\n        self._state_dim = state_dim\n        self._action_dim = action_dim\n\n    def prepare_images(self, batch):\n        images = []\n        img_masks = []\n        for key in self.config.image_features[:self._num_cameras]:\n            if key in batch:\n                img = batch[key]\n            else:\n                img = torch.randn(\n                    list(batch.values())[0].shape[0], 3, 224, 224,\n                    device=list(batch.values())[0].device,\n                )\n            B = img.shape[0]\n            images.append(img)\n            img_masks.append(torch.ones(B, dtype=torch.bool, device=img.device))\n        return images, img_masks\n\n    def prepare_state(self, batch):\n        if OBS_STATE in batch:\n            return batch[OBS_STATE]\n        B = list(batch.values())[0].shape[0]\n        device = list(batch.values())[0].device\n        return torch.randn(B, self._state_dim, device=device)\n\n    def prepare_action(self, batch):\n        if ACTION in batch:\n            return batch[ACTION]\n        B = list(batch.values())[0].shape[0]\n        device = list(batch.values())[0].device\n        return torch.randn(B, self.config.chunk_size, self._action_dim, device=device)\n\n    def forward(self, batch, **kwargs):\n        B = list(batch.values())[0].shape[0]\n        device = list(batch.values())[0].device\n        loss = torch.tensor(1.0, device=device, requires_grad=True)\n        return loss, {\"loss\": 1.0}\n\n\nif __name__ == \"__main__\":\n    torch.manual_seed(42)\n    B = 2\n    device = \"cpu\"\n\n    HIDDEN = 960\n    EXPERT = 720\n    ACTION_DIM = 32\n    mock_policy = _MockSmolVLAPolicy(\n        action_dim=ACTION_DIM, state_dim=32, chunk_size=50, num_cameras=2,\n        hidden_dim=HIDDEN, expert_hidden=EXPERT,\n    )\n    wrapper = IMMSmolVLAWrapper(\n        smolvla_policy=mock_policy,\n        acis_config={\"num_heads\": 8},\n        imm_config={\"lambda_margin\": 0.1, \"delta\": 0.5, \"warmup_steps\": 100, \"k_ratio\": 0.5},\n    )\n\n    batch = {\n        \"observation.images.agentview\": torch.randn(B, 3, 224, 224),\n        \"observation.images.wrist\": torch.randn(B, 3, 224, 224),\n        ACTION: torch.randn(B, 50, ACTION_DIM),\n        OBS_STATE: torch.randn(B, 32),\n        OBS_LANGUAGE_TOKENS: torch.randint(0, 100, (B, 20)),\n        OBS_LANGUAGE_ATTENTION_MASK: torch.ones(B, 20, dtype=torch.bool),\n    }\n\n    wrapper.train()\n    total_loss, info = wrapper(batch, step=50)\n    total_loss.backward()\n    print(f\"[train] total_loss={total_loss.item():.4f}, k={info['k']}, \"\n          f\"lipschitz={info['lipschitz_estimate']:.4f}\")\n\n    base_loss, base_info = wrapper.forward_baseline(batch)\n    print(f\"[baseline] action_loss={base_loss.item():.4f}\")\n\n    wrapper.eval()\n    scores, k = wrapper.compute_importance_scores(batch)\n    print(f\"[eval] scores shape={scores.shape}, k={k}\")\n    print(\"All wrapper tests passed!\")\n",
      "numLines": 505,
      "startLine": 1,
      "totalLines": 505
    }
  }
}
```

</details>

---

### Tool call

_source line 33_

<details open><summary>🔧 Tool call — Read · `toolu_01A7s4k5ft6GiGCzCjTNjqyo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/imm/soft_topk.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "263df5c0-d01d-4f96-a4cb-fd4145125851",
  "uuid": "4e365e69-ee12-4786-a94d-66ed91e8e45a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P8fJNFF5YAX1pYssBKZQrR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 870,
      "cache_read_input_tokens": 26972,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 870
      },
      "output_tokens": 18,
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

_source line 34 · 2026-05-15T13:41:21.755Z_

<details><summary>↩ Tool result · `toolu_01A7s4k5ft6GiGCzCjTNjqyo`</summary>

```text
1	"""Differentiable Top-K selection for importance-based token compression.
2	
3	Three methods:
4	  - 'sigmoid': Temperature-scaled sigmoid mask around a soft threshold (simple, reliable).
5	  - 'sinkhorn': Optimal-transport-inspired soft top-k via Sinkhorn iterations (theoretically tighter).
6	  - 'implicit_diff': Binary-search shift + implicit function theorem for exact top-k gradients.
7	
8	Inputs:  (B, N) importance scores, integer k.
9	Outputs: (B, N) soft mask, s_{(k)}, s_{(k+1)} — all differentiable.
10	Depends: torch.
11	"""
12	
13	from __future__ import annotations
14	
15	import torch
16	import torch.nn as nn
17	from torch import Tensor
18	from typing import Tuple
19	
20	
21	class SoftTopK(nn.Module):
22	    def __init__(self, temperature: float = 1.0, method: str = "sigmoid"):
23	        super().__init__()
24	        self.temperature = temperature
25	        assert method in ("sigmoid", "sinkhorn", "implicit_diff"), f"Unknown method: {method}"
26	        self.method = method
27	        self._sinkhorn_iters = 20
28	        self._bisect_iters = 32
29	
30	    def forward(self, scores: Tensor, k: int) -> Tuple[Tensor, Tensor, Tensor]:
31	        """
32	        Args:
33	            scores: (B, N) importance scores.
34	            k: number of tokens to retain.
35	        Returns:
36	            mask:       (B, N) soft selection mask in [0, 1].
37	            s_k:        (B,)   differentiable k-th largest score.
38	            s_k_plus_1: (B,)   differentiable (k+1)-th largest score.
39	        """
40	        if self.method == "sigmoid":
41	            return self._sigmoid_forward(scores, k)
42	        if self.method == "implicit_diff":
43	            return self._implicit_diff_forward(scores, k)
44	        return self._sinkhorn_forward(scores, k)
45	
46	    # ------------------------------------------------------------------
47	    # Method A: Temperature-based sigmoid
48	    # ------------------------------------------------------------------
49	    def _sigmoid_forward(self, scores: Tensor, k: int) -> Tuple[Tensor, Tensor, Tensor]:
50	        B, N = scores.shape
51	        assert 0 < k < N, f"k={k} must be in (0, {N})"
52	
53	        sorted_scores, _ = torch.sort(scores, dim=-1, descending=True)
54	        s_k = sorted_scores[:, k - 1]          # (B,)
55	        s_k_plus_1 = sorted_scores[:, k]       # (B,)
56	
57	        # Soft threshold: midpoint between s_{(k)} and s_{(k+1)}
58	        threshold = 0.5 * (s_k + s_k_plus_1)   # (B,)
59	
60	        tau = self.temperature + 1e-8
61	        mask = torch.sigmoid((scores - threshold.unsqueeze(-1)) / tau)  # (B, N)
62	
63	        return mask, s_k, s_k_plus_1
64	
65	    # ------------------------------------------------------------------
66	    # Method B: Sinkhorn-based optimal transport
67	    # ------------------------------------------------------------------
68	    def _sinkhorn_forward(self, scores: Tensor, k: int) -> Tuple[Tensor, Tensor, Tensor]:
69	        B, N = scores.shape
70	        assert 0 < k < N
71	
72	        # Extract s_k, s_{k+1} the same way (needed for margin loss)
73	        sorted_scores, _ = torch.sort(scores, dim=-1, descending=True)
74	        s_k = sorted_scores[:, k - 1]
75	        s_k_plus_1 = sorted_scores[:, k]
76	
77	        # OT formulation: row marginals = [k, N-k], col marginals = 1 each
78	        # Cost matrix C: higher score -> lower cost to be "selected"
79	        tau = self.temperature + 1e-8
80	        log_alpha = scores / tau  # (B, N) — log-potential for selection
81	
82	        # Sinkhorn in log-space for numerical stability
83	        # We solve for a (B, N) assignment where sum = k
84	        # Using a simplified 1D Sinkhorn: iteratively project onto simplex with sum=k
85	        log_mask = log_alpha.clone()
86	        for _ in range(self._sinkhorn_iters):
87	            # Normalize so that sum of exp(log_mask) = k
88	            log_sum = torch.logsumexp(log_mask, dim=-1, keepdim=True)
89	            log_mask = log_mask - log_sum + torch.log(torch.tensor(k, dtype=scores.dtype, device=scores.device))
90	            # Clamp individual entries to [0, 1] in probability space
91	            log_mask = log_mask - torch.nn.functional.softplus(log_mask)  # ≈ min(log_mask, 0)
92	
93	        mask = torch.exp(log_mask).clamp(0.0, 1.0)
94	
95	        return mask, s_k, s_k_plus_1
96	
97	    # ------------------------------------------------------------------
98	    # Method C: Implicit differentiation (binary search + IFT)
99	    # ------------------------------------------------------------------
100	    def _implicit_diff_forward(self, scores: Tensor, k: int) -> Tuple[Tensor, Tensor, Tensor]:
101	        B, N = scores.shape
102	        assert 0 < k < N
103	
104	        sorted_scores, _ = torch.sort(scores, dim=-1, descending=True)
105	        s_k = sorted_scores[:, k - 1]
106	        s_k_plus_1 = sorted_scores[:, k]
107	
108	        mask = _ImplicitTopK.apply(scores, k, self.temperature, self._bisect_iters)
109	
110	        return mask, s_k, s_k_plus_1
111	
112	
113	class _ImplicitTopK(torch.autograd.Function):
114	    """Binary-search shift t s.t. sum(sigma((x_i + t) / tau)) = k, with IFT backward."""
115	
116	    @staticmethod
117	    def forward(ctx, scores: Tensor, k: int, temperature: float, bisect_iters: int) -> Tensor:
118	        tau = temperature + 1e-8
119	        B, N = scores.shape
120	
121	        # Binary search for shift t per sample
122	        lo = -scores.max(dim=-1).values - 10.0  # (B,)
123	        hi = -scores.min(dim=-1).values + 10.0   # (B,)
124	
125	        for _ in range(bisect_iters):
126	            mid = 0.5 * (lo + hi)
127	            val = torch.sigmoid((scores + mid.unsqueeze(-1)) / tau).sum(dim=-1)
128	            lo = torch.where(val < k, mid, lo)
129	            hi = torch.where(val >= k, mid, hi)
130	
131	        t_star = 0.5 * (lo + hi)  # (B,)
132	        mask = torch.sigmoid((scores + t_star.unsqueeze(-1)) / tau)  # (B, N)
133	
134	        ctx.save_for_backward(scores, mask, t_star)
135	        ctx.tau = tau
136	        return mask
137	
138	    @staticmethod
139	    def backward(ctx, grad_output: Tensor):
140	        scores, mask, t_star = ctx.saved_tensors
141	        tau = ctx.tau
142	
143	        # sigma'(z) = sigma(z) * (1 - sigma(z))
144	        sigma_prime = mask * (1.0 - mask)  # (B, N)
145	        denom = sigma_prime.sum(dim=-1, keepdim=True).clamp(min=1e-8)  # (B, 1)
146	
147	        # IFT: dt/dx_i = -sigma'_i / sum_j sigma'_j
148	        # d mask_i / d x_j = sigma'_i / tau * (delta_{ij} - sigma'_j / sum sigma')
149	        # => grad_scores = grad_output * sigma'/ tau - (sigma'/tau) * (sum(grad_output * sigma') / sum(sigma'))
150	        g_weighted = (grad_output * sigma_prime).sum(dim=-1, keepdim=True)  # (B, 1)
151	        grad_scores = (sigma_prime / tau) * (grad_output - g_weighted / denom)
152	
153	        return grad_scores, None, None, None
154	
155	
156	if __name__ == "__main__":
157	    torch.manual_seed(42)
158	    B, N, k = 4, 64, 16
159	    scores = torch.randn(B, N, requires_grad=True)
160	
161	    for method in ("sigmoid", "sinkhorn", "implicit_diff"):
162	        topk = SoftTopK(temperature=0.5, method=method)
163	        mask, s_k, s_k1 = topk(scores, k)
164	        loss = mask.sum()
165	        loss.backward()
166	        print(f"[{method}] mask: {mask.shape}, sum~={mask.sum(-1).tolist()}, "
167	              f"s_k={s_k.tolist()}, grad OK={scores.grad is not None}")
168	        scores.grad = None
169	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "263df5c0-d01d-4f96-a4cb-fd4145125851",
  "uuid": "8aff9b18-7b83-4e20-8840-a65a3c2c7866",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/imm/soft_topk.py",
      "content": "\"\"\"Differentiable Top-K selection for importance-based token compression.\n\nThree methods:\n  - 'sigmoid': Temperature-scaled sigmoid mask around a soft threshold (simple, reliable).\n  - 'sinkhorn': Optimal-transport-inspired soft top-k via Sinkhorn iterations (theoretically tighter).\n  - 'implicit_diff': Binary-search shift + implicit function theorem for exact top-k gradients.\n\nInputs:  (B, N) importance scores, integer k.\nOutputs: (B, N) soft mask, s_{(k)}, s_{(k+1)} — all differentiable.\nDepends: torch.\n\"\"\"\n\nfrom __future__ import annotations\n\nimport torch\nimport torch.nn as nn\nfrom torch import Tensor\nfrom typing import Tuple\n\n\nclass SoftTopK(nn.Module):\n    def __init__(self, temperature: float = 1.0, method: str = \"sigmoid\"):\n        super().__init__()\n        self.temperature = temperature\n        assert method in (\"sigmoid\", \"sinkhorn\", \"implicit_diff\"), f\"Unknown method: {method}\"\n        self.method = method\n        self._sinkhorn_iters = 20\n        self._bisect_iters = 32\n\n    def forward(self, scores: Tensor, k: int) -> Tuple[Tensor, Tensor, Tensor]:\n        \"\"\"\n        Args:\n            scores: (B, N) importance scores.\n            k: number of tokens to retain.\n        Returns:\n            mask:       (B, N) soft selection mask in [0, 1].\n            s_k:        (B,)   differentiable k-th largest score.\n            s_k_plus_1: (B,)   differentiable (k+1)-th largest score.\n        \"\"\"\n        if self.method == \"sigmoid\":\n            return self._sigmoid_forward(scores, k)\n        if self.method == \"implicit_diff\":\n            return self._implicit_diff_forward(scores, k)\n        return self._sinkhorn_forward(scores, k)\n\n    # ------------------------------------------------------------------\n    # Method A: Temperature-based sigmoid\n    # ------------------------------------------------------------------\n    def _sigmoid_forward(self, scores: Tensor, k: int) -> Tuple[Tensor, Tensor, Tensor]:\n        B, N = scores.shape\n        assert 0 < k < N, f\"k={k} must be in (0, {N})\"\n\n        sorted_scores, _ = torch.sort(scores, dim=-1, descending=True)\n        s_k = sorted_scores[:, k - 1]          # (B,)\n        s_k_plus_1 = sorted_scores[:, k]       # (B,)\n\n        # Soft threshold: midpoint between s_{(k)} and s_{(k+1)}\n        threshold = 0.5 * (s_k + s_k_plus_1)   # (B,)\n\n        tau = self.temperature + 1e-8\n        mask = torch.sigmoid((scores - threshold.unsqueeze(-1)) / tau)  # (B, N)\n\n        return mask, s_k, s_k_plus_1\n\n    # ------------------------------------------------------------------\n    # Method B: Sinkhorn-based optimal transport\n    # ------------------------------------------------------------------\n    def _sinkhorn_forward(self, scores: Tensor, k: int) -> Tuple[Tensor, Tensor, Tensor]:\n        B, N = scores.shape\n        assert 0 < k < N\n\n        # Extract s_k, s_{k+1} the same way (needed for margin loss)\n        sorted_scores, _ = torch.sort(scores, dim=-1, descending=True)\n        s_k = sorted_scores[:, k - 1]\n        s_k_plus_1 = sorted_scores[:, k]\n\n        # OT formulation: row marginals = [k, N-k], col marginals = 1 each\n        # Cost matrix C: higher score -> lower cost to be \"selected\"\n        tau = self.temperature + 1e-8\n        log_alpha = scores / tau  # (B, N) — log-potential for selection\n\n        # Sinkhorn in log-space for numerical stability\n        # We solve for a (B, N) assignment where sum = k\n        # Using a simplified 1D Sinkhorn: iteratively project onto simplex with sum=k\n        log_mask = log_alpha.clone()\n        for _ in range(self._sinkhorn_iters):\n            # Normalize so that sum of exp(log_mask) = k\n            log_sum = torch.logsumexp(log_mask, dim=-1, keepdim=True)\n            log_mask = log_mask - log_sum + torch.log(torch.tensor(k, dtype=scores.dtype, device=scores.device))\n            # Clamp individual entries to [0, 1] in probability space\n            log_mask = log_mask - torch.nn.functional.softplus(log_mask)  # ≈ min(log_mask, 0)\n\n        mask = torch.exp(log_mask).clamp(0.0, 1.0)\n\n        return mask, s_k, s_k_plus_1\n\n    # ------------------------------------------------------------------\n    # Method C: Implicit differentiation (binary search + IFT)\n    # ------------------------------------------------------------------\n    def _implicit_diff_forward(self, scores: Tensor, k: int) -> Tuple[Tensor, Tensor, Tensor]:\n        B, N = scores.shape\n        assert 0 < k < N\n\n        sorted_scores, _ = torch.sort(scores, dim=-1, descending=True)\n        s_k = sorted_scores[:, k - 1]\n        s_k_plus_1 = sorted_scores[:, k]\n\n        mask = _ImplicitTopK.apply(scores, k, self.temperature, self._bisect_iters)\n\n        return mask, s_k, s_k_plus_1\n\n\nclass _ImplicitTopK(torch.autograd.Function):\n    \"\"\"Binary-search shift t s.t. sum(sigma((x_i + t) / tau)) = k, with IFT backward.\"\"\"\n\n    @staticmethod\n    def forward(ctx, scores: Tensor, k: int, temperature: float, bisect_iters: int) -> Tensor:\n        tau = temperature + 1e-8\n        B, N = scores.shape\n\n        # Binary search for shift t per sample\n        lo = -scores.max(dim=-1).values - 10.0  # (B,)\n        hi = -scores.min(dim=-1).values + 10.0   # (B,)\n\n        for _ in range(bisect_iters):\n            mid = 0.5 * (lo + hi)\n            val = torch.sigmoid((scores + mid.unsqueeze(-1)) / tau).sum(dim=-1)\n            lo = torch.where(val < k, mid, lo)\n            hi = torch.where(val >= k, mid, hi)\n\n        t_star = 0.5 * (lo + hi)  # (B,)\n        mask = torch.sigmoid((scores + t_star.unsqueeze(-1)) / tau)  # (B, N)\n\n        ctx.save_for_backward(scores, mask, t_star)\n        ctx.tau = tau\n        return mask\n\n    @staticmethod\n    def backward(ctx, grad_output: Tensor):\n        scores, mask, t_star = ctx.saved_tensors\n        tau = ctx.tau\n\n        # sigma'(z) = sigma(z) * (1 - sigma(z))\n        sigma_prime = mask * (1.0 - mask)  # (B, N)\n        denom = sigma_prime.sum(dim=-1, keepdim=True).clamp(min=1e-8)  # (B, 1)\n\n        # IFT: dt/dx_i = -sigma'_i / sum_j sigma'_j\n        # d mask_i / d x_j = sigma'_i / tau * (delta_{ij} - sigma'_j / sum sigma')\n        # => grad_scores = grad_output * sigma'/ tau - (sigma'/tau) * (sum(grad_output * sigma') / sum(sigma'))\n        g_weighted = (grad_output * sigma_prime).sum(dim=-1, keepdim=True)  # (B, 1)\n        grad_scores = (sigma_prime / tau) * (grad_output - g_weighted / denom)\n\n        return grad_scores, None, None, None\n\n\nif __name__ == \"__main__\":\n    torch.manual_seed(42)\n    B, N, k = 4, 64, 16\n    scores = torch.randn(B, N, requires_grad=True)\n\n    for method in (\"sigmoid\", \"sinkhorn\", \"implicit_diff\"):\n        topk = SoftTopK(temperature=0.5, method=method)\n        mask, s_k, s_k1 = topk(scores, k)\n        loss = mask.sum()\n        loss.backward()\n        print(f\"[{method}] mask: {mask.shape}, sum~={mask.sum(-1).tolist()}, \"\n              f\"s_k={s_k.tolist()}, grad OK={scores.grad is not None}\")\n        scores.grad = None\n",
      "numLines": 169,
      "startLine": 1,
      "totalLines": 169
    }
  }
}
```

</details>

---

### Tool call

_source line 35_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__detect_image · `toolu_012hnPQH4RtFXcD5qzugXdSk`</summary>

```json
{
  "server": "westd-27271",
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
  "session_id": "263df5c0-d01d-4f96-a4cb-fd4145125851",
  "uuid": "7b5d66e9-59fc-4734-a5b3-c89281d371fb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P8fJNFF5YAX1pYssBKZQrR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 870,
      "cache_read_input_tokens": 26972,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 870
      },
      "output_tokens": 18,
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

_source line 36 · 2026-05-15T13:41:23.359Z_

<details><summary>↩ Tool result · `toolu_012hnPQH4RtFXcD5qzugXdSk`</summary>

```text
{"result":"{\n  \"detected\": false,\n  \"status\": \"ssh_error\",\n  \"skip_base_setup\": false,\n  \"message\": \"SSH error: exit code 1\"\n}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "263df5c0-d01d-4f96-a4cb-fd4145125851",
  "uuid": "f87870f5-4aa3-4b08-85c7-4ca39063a0a5",
  "tool_use_result": {
    "content": "{\"result\":\"{\\n  \\\"detected\\\": false,\\n  \\\"status\\\": \\\"ssh_error\\\",\\n  \\\"skip_base_setup\\\": false,\\n  \\\"message\\\": \\\"SSH error: exit code 1\\\"\\n}\"}",
    "structuredContent": {
      "result": "{\n  \"detected\": false,\n  \"status\": \"ssh_error\",\n  \"skip_base_setup\": false,\n  \"message\": \"SSH error: exit code 1\"\n}"
    }
  }
}
```

</details>

---
