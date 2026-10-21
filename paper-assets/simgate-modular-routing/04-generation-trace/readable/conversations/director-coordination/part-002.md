# Director coordination — Part 2 of 9

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../director-coordination.md) · [Part 3 →](part-003.md) · [Structured JSON](../../../sessions/53/532e22af863d2a24e206.json)

## Round 41

### Tool result

_source line 388 · 2026-05-15T00:01:22.638691+00:00_

File content (42293 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 389 · 2026-05-15T00:01:24.450067+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview_ai|enabled",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/registry.yaml",
  "output_mode": "content",
  "head_limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview_ai|enabled",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/registry.yaml",
    "output_mode": "content",
    "head_limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 390 · 2026-05-15T00:01:24.511382+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Grep",
  "elapsed_ms": 61
}
```

</details>

---


### Tool call

_source line 391 · 2026-05-15T00:01:25.696123+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/global/registry.yaml",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/global/registry.yaml",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 392 · 2026-05-15T00:01:25.696626+00:00_

1	baseline: null
2	experiments:
3	  scienceworld-data-consolidation:
4	    status: DONE
5	    retry_count: 0
6	    created_at: '2026-05-14T13:25:27.637Z'
7	    updated_at: '2026-05-14T13:26:07.932Z'
8	    hypothesis: Consolidate ScienceWorld 245 episodes / 11 tasks counterfactual data
9	      into unified format for multi-environment router training
10	    spec:
11	      command: python3 src/consolidate_scienceworld.py
12	      server: westb-13313
13	      data_path: results/plan_c/
14	      data_count: 245
15	      model_name: n/a
16	      seed: 0
17	    conclusion: success
18	    checkpoint_path: data/scienceworld-counterfactual/episodes.jsonl
19	    log_path: data/scienceworld-counterfactual/summary.json
20	    completed_at: '2026-05-14T13:26:07.932Z'
21	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 393 · 2026-05-15T00:01:26.902539+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_12 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_12 2>/dev/null | head -20"
  }
}
```

</details>

---


### Tool result

_source line 394 · 2026-05-15T00:01:27.104729+00:00_

&lt;persisted-output>
Output too large (106.3KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-12-projects-simgate-modular-routing--claude-sessions-review-director-19d7e797/f7730f35-335f-4133-9230-798feeb48e97/tool-results/br7vanuzx.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/global/logs/system.log:2026-05-14 19:38:42 INFO     [HOOKS] [review] external_review_enabled=False for project=simgate-modular-routing
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/global/logs/system.log:2026-05-14 23:59:57 INFO     [HOOKS] [review] external_review_enabled=False for project=simgate-modular-routing
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/logs/workers/worker_research_sighup-root-cause_20260514T021418.log:{"type":"user","message":{"role":"user","content":[{"tool_use_id":"toolu_014acez97fNV6sz7dTkjL57r","type":"tool_result","content":"&lt;persisted-output>\nOutput too large (22.2KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-12-projects-simgate-modular-routing/ed7e534c-7d76-4909-9016-b9c6a9c31364/tool-results/toolu_014acez97fNV6sz7dTkjL57r.txt\n\nPreview (first 2KB):\n/home/ubuntu/agent-ml-research/core/session_server.py-779-            return False\n/home/ubuntu/agent-ml-research/core/session_server.py-780-\n/home/ubuntu/agent-ml-research/core/session_server.py:781:    def kill_project_sessions(self, project: str) -> dict:\n/home/ubuntu/agent-ml-research/core/session_server.py-782-        \"\"\"Kill all live claude subprocesses belonging to a project.\n/home/ubuntu/agent-ml-research/core/session_server.py-783-\n--\n/home/ubuntu/agent-ml-research/core/session_server.py-803-                skipped.append(chat_key)\n/home/ubuntu/agent-ml-research/core/session_server.py-804-        logger.info(\n/home/ubuntu/agent-ml-research/core/session_server.py:805:            \"[session_server] kill_p
…[truncated 343 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 202
}
```

</details>

---


### Tool call

_source line 395 · 2026-05-15T00:01:28.661881+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -B5 -A5 \"external_review_enabled\" /home/ubuntu/.agent-ml-research-idea_gen_0509_12/global/logs/system.log | head -40"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -B5 -A5 \"external_review_enabled\" /home/ubuntu/.agent-ml-research-idea_gen_0509_12/global/logs/system.log | head -40"
  }
}
```

</details>

---


### Tool result

_source line 396 · 2026-05-15T00:01:28.762980+00:00_

2026-05-14 19:38:42 INFO     [HOOKS] [review] reusing existing Group C: oc_0b622d6038b969b96148ee8a163a1a0c
2026-05-14 19:38:42 INFO     [SESSION] [session_server] invalidated sessions for key=feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director
2026-05-14 19:38:42 INFO     [SESSION] [session_server] invalidated sessions for key=feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_1
2026-05-14 19:38:42 INFO     [SESSION] [session_server] invalidated sessions for key=feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_2
2026-05-14 19:38:42 INFO     [HOOKS] [review] reset all review sessions for chat_id=oc_0b622d6038b969b96148ee8a163a1a0c
2026-05-14 19:38:42 INFO     [HOOKS] [review] external_review_enabled=False for project=simgate-modular-routing
2026-05-14 19:38:42 INFO     [HOOKS] [review] kick-off message length=299 has_ext=False
2026-05-14 19:38:42 INFO     [SESSION] [feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director] QUEUED | project=simgate-modular-routing | depth=0 | text='系统通知：审稿审批已通过。请开始审稿。\n\n[论文提交]\n- 项目: simgate-modular-routing\n- 论文路径: projects/simga'
2026-05-14 19:38:43 INFO     [HOOKS] [review] Group C=oc_0b622d6038b969b96148ee8a163a1a0c project=simgate-modular-routing venue=EMNLP 2026 mode=fresh round=4
2026-05-14 19:38:44 INFO     [SESSION] [session_server] calling claude | project=simgate-modular-routing | session=None | resume=False
2026-05-14 19:41:17 INFO     [DIRECT] [post-to-reviewer] queued | project=simgate-modular-routing | reviewer_key=feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_1
--
2026-05-14 23:59:56 INFO     [HOOKS] [review] reusing existing Group C: oc_0b622d6038b969b96148ee8a163a1a0c
2026-05-14 23:59:56 INFO     [SESSION] [session_server] invalidated sessions for key=feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director
2026-05-14 23:59:56 INFO     [SESSION] [session_server] invalidated sessions for key=feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_1
2026-05-14 23:59:56 INFO     [
…[truncated 1105 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 397 · 2026-05-15T00:01:30.672129+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu -name \"*.py\" -type f 2>/dev/null | xargs grep -l \"external_review_enabled\" 2>/dev/null | head -5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu -name \"*.py\" -type f 2>/dev/null | xargs grep -l \"external_review_enabled\" 2>/dev/null | head -5"
  }
}
```

</details>

---


### Tool result

_source line 398 · 2026-05-15T00:01:44.605941+00:00_

/home/ubuntu/agent-ml-research/core/tools/project_config.py
/home/ubuntu/agent-ml-research/core/core/tools/project_config.py
/home/ubuntu/agent-ml-research/core/core/approvals/hooks.py
/home/ubuntu/agent-ml-research/core/approvals/hooks.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 13933
}
```

</details>

---


### Tool call

_source line 399 · 2026-05-15T00:01:45.711145+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -A10 -B5 \"external_review\" /home/ubuntu/agent-ml-research/core/tools/project_config.py | head -40"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -A10 -B5 \"external_review\" /home/ubuntu/agent-ml-research/core/tools/project_config.py | head -40"
  }
}
```

</details>

---


### Tool result

_source line 400 · 2026-05-15T00:01:45.812041+00:00_

        feishu.get("review_paper_path", "") or "",
        feishu.get("review_supplementary_paths", "") or "",
    )


def is_external_review_enabled(project_name: str) -> bool:
    """Check if external review (paperreview.ai) is enabled for a project.

    Reads ``external_review.paperreview_ai.enabled`` from project config.
    Returns False if not configured.
    """
    result = load_project_config(project_name)
    if not result.success:
        return False
    ext = result.data["config"].get("external_review", {})
    return bool(ext.get("paperreview_ai", {}).get("enabled", False))


def save_project_study_config(
    project_name: str,
    study_chat_id: str,
) -> ToolResult:
    """Save feishu.study_chat_id to project config YAML (Group D).

    Args:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 401 · 2026-05-15T00:01:47.520526+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing -name \"config.yaml\" -o -name \"project.yaml\" 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing -name \"config.yaml\" -o -name \"project.yaml\" 2>/dev/null"
  }
}
```

</details>

---


### Tool result

_source line 402 · 2026-05-15T00:01:47.571264+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 403 · 2026-05-15T00:01:48.826510+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"load_project_config\" /home/ubuntu/agent-ml-research/core/tools/project_config.py | head -5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"load_project_config\" /home/ubuntu/agent-ml-research/core/tools/project_config.py | head -5"
  }
}
```

</details>

---


### Tool result

_source line 404 · 2026-05-15T00:01:48.877377+00:00_

def load_project_config(project_name: str, section: str | None = None) -> ToolResult:
    result = load_project_config(project_name, section="execution")
    result = load_project_config(project_name)
    result = load_project_config(project_name)
    result = load_project_config(project_name)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 405 · 2026-05-15T00:01:50.385071+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -A20 \"^def load_project_config\" /home/ubuntu/agent-ml-research/core/tools/project_config.py | head -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -A20 \"^def load_project_config\" /home/ubuntu/agent-ml-research/core/tools/project_config.py | head -30"
  }
}
```

</details>

---


### Tool result

_source line 406 · 2026-05-15T00:01:50.435769+00:00_

def load_project_config(project_name: str, section: str | None = None) -> ToolResult:
    """Load a project configuration from config/projects/{name}.yaml.

    Progressive disclosure: pass `section` to retrieve only a specific
    top-level config section (e.g. "execution", "evaluation", "feishu",
    "deployment", "backup") instead of the entire config.

    Args:
        project_name: Project identifier (e.g. "audio_book_rec").
        section: If provided, return only this top-level section of the config.
            Valid sections: project, codebase, execution, evaluation, feishu,
            deployment, backup.

    Returns:
        ToolResult with parsed config dict on success, or error if not found.
    """
    path = _paths.projects_config_dir() / f"{project_name}.yaml"
    if not path.exists():
        available = sorted(p.stem for p in _paths.projects_config_dir().glob("*.yaml"))
        return ToolResult(
            success=False,

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 407 · 2026-05-15T00:01:51.743203+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu -type d -name \"projects_config\" -o -name \"projects\" -path \"*/config/*\" 2>/dev/null | head -5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu -type d -name \"projects_config\" -o -name \"projects\" -path \"*/config/*\" 2>/dev/null | head -5"
  }
}
```

</details>

---


### Tool result

_source line 408 · 2026-05-15T00:01:52.095083+00:00_

/home/ubuntu/agent-ml-research/workspace/config/projects
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/projects

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 409 · 2026-05-15T00:01:53.702575+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/projects/simgate-modular-routing.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/projects/simgate-modular-routing.yaml"
  }
}
```

</details>

---


### Tool result

_source line 410 · 2026-05-15T00:01:53.703160+00:00_

1	execution:
2	  account: root
3	  gpu_constraint:
4	  - autodl-simgate:cuda:0
5	  - autodl-simgate:cuda:1
6	  gpu_ids:
7	  - cuda:0
8	  - cuda:1
9	  project_path: /root/autodl-tmp/simgate-modular-routing
10	  servers:
11	  - westb-13313
12	feishu:
13	  chat_id: oc_f6bffc7e8351600df8091f08a63cd5a0
14	  operational_chat_id: oc_6551c2d0ac89db1b3b9e56f77fcf912d
15	  review_paper_path: projects/simgate-modular-routing/docs/paper/main.tex
16	  review_round: 6
17	  review_supplementary_paths: ''
18	  submission_chat_id: oc_0b622d6038b969b96148ee8a163a1a0c
19	project:
20	  created_at: '2026-05-13T04:23:23.832Z'
21	  description: 'SimGate: Learning When to Route LLM Agents to Deterministic Computation
22	    via Explicit Modular Gating'
23	  name: simgate-modular-routing
24	  phase: research
25	  source_idea_id: idea_010
26	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 411 · 2026-05-15T00:01:55.963320+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/projects/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/projects/"
  }
}
```

</details>

---


### Tool result

_source line 412 · 2026-05-15T00:01:56.014011+00:00_

total 12
drwxrwxr-x 2 ubuntu ubuntu 4096 May 13 04:23 .
drwxrwxr-x 4 ubuntu ubuntu 4096 May 14 17:47 ..
-rw-r--r-- 1 ubuntu ubuntu  759 May 14 23:59 simgate-modular-routing.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 413 · 2026-05-15T00:01:58.677759+00:00_

Based on my search, here's the finding:

## Summary

**Project Config File Location:**
`/home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/projects/simgate-modular-routing.yaml`

**External Review Status:**
`external_review.paperreview_ai.enabled` is **FALSE**

The project config file does not contain an `external_review` section, which means the setting defaults to False. This is confirmed by the system logs from May 14-15, 2026, which explicitly state:
- `external_review_enabled=False for project=simgate-modular-routing`

The current project configuration contains sections for `execution`, `feishu`, and `project` metadata, but no external review settings. If external review were to be enabled, the config would need an `external_review.paperreview_ai.enabled: true` entry added to the YAML.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Agent",
  "elapsed_ms": 43692
}
```

</details>

---


### Tool call

_source line 414 · 2026-05-15T00:02:17.608092+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing"
  }
}
```

</details>

---


### Tool result

_source line 415 · 2026-05-15T00:02:17.859522+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Glob",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 416 · 2026-05-15T00:02:17.860207+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_reports/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_reports/**",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing"
  }
}
```

</details>

---


### Tool result

_source line 417 · 2026-05-15T00:02:17.910888+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_1.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_2.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_3.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_4.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_5.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 418 · 2026-05-15T00:03:13.687195+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "simgate-modular-routing",
  "text": "## Round 1 审稿任务 — Reviewer 1（方法严谨性）\n\n### 投稿信息\n- **论文**: \"Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\"\n- **目标 Venue**: EMNLP 2026 Findings track\n- **ARR 截止**: 2026-05-25\n- **格式**: ACL 模板，short paper（正文 ≤ 4 页，参考文献不限，附录可选，附录不参与主审）\n- **匿名**: Double-blind review\n- **论文路径**: `projects/simgate-modular-routing/docs/paper/main.tex`（含 abstract.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, conclusion.tex）\n\n### 你的审查侧重：方法严谨性\n\n请重点审查以下方面：\n\n1. **Counterfactual 方法论**：\n   - Episode-level counterfactual analysis 的设计是否严密？pure-internal vs pure-deterministic 的控制变量是否充分？\n   - \"deterministic computation replaces only the state-transition prediction, not action selection\" — 这一设计选择是否合理？是否引入混淆因素？\n   - 11/30 task types 的选择（prescreening 排除 19 个 timeout 的 task types）是否引入选择偏差？\n\n2. **DAF 指标**：\n   - DAF = 1 - Δ_nd / Δ_full 的定义是否数学上严谨？是否存在边界情况问题？\n   - penalty sensitivity analysis（Appendix D）是否充分说明了 DAF 对惩罚值的依赖？\n   - \"penalty-independent companion metric\"（78.9% death asymmetry labels）与 DAF 之间的关系是否清晰？\n\n3. **统计声明**：\n   - Pearson r = 0.9698 (p = 8.12e-7) 基于 11 个数据点——样本量是否足够支撑因果性或强相关性声明？\n   - Bootstrap 95% CI [0.952, 0.995] 和 LOO 分析是否足够 robust？\n   - Router balanced accuracy 58.1 ± 0.8% 基于 4 seeds — 方差估计是否可靠？\n\n4. **实验设计**：\n   - 245 episodes across 11 task types 的样本量（每 task type 20-40 episodes）对于 short paper 的 claims 是否足够？\n   - 训练/验证 split（81 train / 14 validation episodes）是否足够支撑 router diagnostic 结论？\n   - Cross-environment evidence（MATH 50 problems, ALFWorld 135 games）的角色和力度是否合理（放在 Limitations 而非 Experiments）？\n\n5. **可复现性**：\n   - 是否提供了足够的实验细节（hyperparameters, random seeds, compute resources）？\n   - Qwen2.5-7B-Instruct + vLLM 的具体版本是否应该注明？\n\n请输出完整审稿报告，格式为：Summary → Strengths → Weaknesses（每条标注 severity: critical/warning/info）→ Questions → Missing References → Score（1-5 分制）→ Confidence。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "simgate-modular-routing",
    "text": "## Round 1 审稿任务 — Reviewer 1（方法严谨性）\n\n### 投稿信息\n- **论文**: \"Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\"\n- **目标 Venue**: EMNLP 2026 Findings track\n- **ARR 截止**: 2026-05-25\n- **格式**: ACL 模板，short paper（正文 ≤ 4 页，参考文献不限，附录可选，附录不参与主审）\n- **匿名**: Double-blind review\n- **论文路径**: `projects/simgate-modular-routing/docs/paper/main.tex`（含 abstract.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, conclusion.tex）\n\n### 你的审查侧重：方法严谨性\n\n请重点审查以下方面：\n\n1. **Counterfactual 方法论**：\n   - Episode-level counterfactual analysis 的设计是否严密？pure-internal vs pure-deterministic 的控制变量是否充分？\n   - \"deterministic computation replaces only the state-transition prediction, not action selection\" — 这一设计选择是否合理？是否引入混淆因素？\n   - 11/30 task types 的选择（prescreening 排除 19 个 timeout 的 task types）是否引入选择偏差？\n\n2. **DAF 指标**：\n   - DAF = 1 - Δ_nd / Δ_full 的定义是否数学上严谨？是否存在边界情况问题？\n   - penalty sensitivity analysis（Appendix D）是否充分说明了 DAF 对惩罚值的依赖？\n   - \"penalty-independent companion metric\"（78.9% death asymmetry labels）与 DAF 之间的关系是否清晰？\n\n3. **统计声明**：\n   - Pearson r = 0.9698 (p = 8.12e-7) 基于 11 个数据点——样本量是否足够支撑因果性或强相关性声明？\n   - Bootstrap 95% CI [0.952, 0.995] 和 LOO 分析是否足够 robust？\n   - Router balanced accuracy 58.1 ± 0.8% 基于 4 seeds — 方差估计是否可靠？\n\n4. **实验设计**：\n   - 245 episodes across 11 task types 的样本量（每 task type 20-40 episodes）对于 short paper 的 claims 是否足够？\n   - 训练/验证 split（81 train / 14 validation episodes）是否足够支撑 router diagnostic 结论？\n   - Cross-environment evidence（MATH 50 problems, ALFWorld 135 games）的角色和力度是否合理（放在 Limitations 而非 Experiments）？\n\n5. **可复现性**：\n   - 是否提供了足够的实验细节（hyperparameters, random seeds, compute resources）？\n   - Qwen2.5-7B-Instruct + vLLM 的具体版本是否应该注明？\n\n请输出完整审稿报告，格式为：Summary → Strengths → Weaknesses（每条标注 severity: critical/warning/info）→ Questions → Missing References → Score（1-5 分制）→ Confidence。"
  }
}
```

</details>

---


### Tool result

_source line 419 · 2026-05-15T00:03:31.772064+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 18084
}
```

</details>

---


### Tool call

_source line 420 · 2026-05-15T00:03:31.973595+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "simgate-modular-routing",
  "text": "## Round 1 审稿任务 — Reviewer 2（新颖性/完整性）\n\n### 投稿信息\n- **论文**: \"Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\"\n- **目标 Venue**: EMNLP 2026 Findings track\n- **ARR 截止**: 2026-05-25\n- **格式**: ACL 模板，short paper（正文 ≤ 4 页，参考文献不限，附录可选，附录不参与主审）\n- **匿名**: Double-blind review\n- **论文路径**: `projects/simgate-modular-routing/docs/paper/main.tex`（含 abstract.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, conclusion.tex）\n\n### 你的审查侧重：新颖性 / 完整性\n\n请重点审查以下方面：\n\n1. **贡献新颖性**：\n   - \"episode-level counterfactual analysis\" 作为方法论贡献是否足够新颖？与已有的 counterfactual evaluation 方法有何本质区别？\n   - \"Death Avoidance Factor\" 作为一个新指标，其概念贡献是否超越了简单的统计分解？\n   - 论文的核心发现（~90% routing signal from death avoidance）是否 surprising？还是 trivially expected given the -100 penalty？\n\n2. **Related Work 覆盖**：\n   - Tool-use learning（Toolformer, ART, Chameleon, ReTool）覆盖是否充分？\n   - Adaptive computation（CogRouter, ARES, MoR, MTRouter）定位是否准确？\n   - 是否遗漏关键相关工作？特别是：\n     - Agent safety / safe RL 文献（仅引了 Garcia & Fernandez 2015 综述）\n     - Catastrophic action detection / failure prediction\n     - Other counterfactual analysis in RL/agent settings\n   - 4 篇 concurrent work（tool-overuse-illusion, when2tool, tool-use-tax, to-call-or-not）的讨论是否充分？\n\n3. **Presentation 质量**：\n   - 论文的 story arc 是否清晰（problem → method → finding → implication）？\n   - Abstract 和 Introduction 是否准确反映实际贡献（不 overclaim/underclaim）？\n   - Figure 1（DAF scatter）和 Table 1（baselines）的信息传达效率？\n   - Limitations section 是否坦诚且全面？\n   - 行文是否流畅，术语是否一致？\n\n4. **格式合规性**：\n   - 正文是否严格在 4 页以内？\n   - 是否符合 ACL 模板要求？\n   - 匿名性是否完全保证（无 GitHub links, 无 institution 泄露）？\n   - 引用格式是否一致（natbib style）？\n   - Ethics statement 和 Limitations 是否包含且位置正确？\n\n5. **Cross-environment 证据**：\n   - MATH pilot（50 problems）和 ALFWorld（135 games）的讨论放在 Limitations 而非 Experiments 是否合理？\n   - 这些 preliminary 证据是否 strengthen 还是 weaken 了核心论点？\n   - ALFWorld 的机制差异（action space pruning vs death avoidance）是否被充分讨论？\n\n请输出完整审稿报告，格式为：Summary → Strengths → Weaknesses（每条标注 severity: critical/warning/info）→ Questions → Missing References → Score（1-5 分制）→ Confidence。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "simgate-modular-routing",
    "text": "## Round 1 审稿任务 — Reviewer 2（新颖性/完整性）\n\n### 投稿信息\n- **论文**: \"Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\"\n- **目标 Venue**: EMNLP 2026 Findings track\n- **ARR 截止**: 2026-05-25\n- **格式**: ACL 模板，short paper（正文 ≤ 4 页，参考文献不限，附录可选，附录不参与主审）\n- **匿名**: Double-blind review\n- **论文路径**: `projects/simgate-modular-routing/docs/paper/main.tex`（含 abstract.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, conclusion.tex）\n\n### 你的审查侧重：新颖性 / 完整性\n\n请重点审查以下方面：\n\n1. **贡献新颖性**：\n   - \"episode-level counterfactual analysis\" 作为方法论贡献是否足够新颖？与已有的 counterfactual evaluation 方法有何本质区别？\n   - \"Death Avoidance Factor\" 作为一个新指标，其概念贡献是否超越了简单的统计分解？\n   - 论文的核心发现（~90% routing signal from death avoidance）是否 surprising？还是 trivially expected given the -100 penalty？\n\n2. **Related Work 覆盖**：\n   - Tool-use learning（Toolformer, ART, Chameleon, ReTool）覆盖是否充分？\n   - Adaptive computation（CogRouter, ARES, MoR, MTRouter）定位是否准确？\n   - 是否遗漏关键相关工作？特别是：\n     - Agent safety / safe RL 文献（仅引了 Garcia & Fernandez 2015 综述）\n     - Catastrophic action detection / failure prediction\n     - Other counterfactual analysis in RL/agent settings\n   - 4 篇 concurrent work（tool-overuse-illusion, when2tool, tool-use-tax, to-call-or-not）的讨论是否充分？\n\n3. **Presentation 质量**：\n   - 论文的 story arc 是否清晰（problem → method → finding → implication）？\n   - Abstract 和 Introduction 是否准确反映实际贡献（不 overclaim/underclaim）？\n   - Figure 1（DAF scatter）和 Table 1（baselines）的信息传达效率？\n   - Limitations section 是否坦诚且全面？\n   - 行文是否流畅，术语是否一致？\n\n4. **格式合规性**：\n   - 正文是否严格在 4 页以内？\n   - 是否符合 ACL 模板要求？\n   - 匿名性是否完全保证（无 GitHub links, 无 institution 泄露）？\n   - 引用格式是否一致（natbib style）？\n   - Ethics statement 和 Limitations 是否包含且位置正确？\n\n5. **Cross-environment 证据**：\n   - MATH pilot（50 problems）和 ALFWorld（135 games）的讨论放在 Limitations 而非 Experiments 是否合理？\n   - 这些 preliminary 证据是否 strengthen 还是 weaken 了核心论点？\n   - ALFWorld 的机制差异（action space pruning vs death avoidance）是否被充分讨论？\n\n请输出完整审稿报告，格式为：Summary → Strengths → Weaknesses（每条标注 severity: critical/warning/info）→ Questions → Missing References → Score（1-5 分制）→ Confidence。"
  }
}
```

</details>

---


### Tool result

_source line 421 · 2026-05-15T00:03:33.239438+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1265
}
```

</details>

---


### Assistant

_source line 422 · 2026-05-15T00:03:40.618080+00:00_

两位 Reviewer 已分配完毕，正在等待独立初审结果返回。

- **Reviewer 1**（方法严谨性）→ 已触发
- **Reviewer 2**（新颖性/完整性）→ 已触发

收到双方审稿后将进入 Step 2（交叉分享 + 逐条回应）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 42

## Round 42

2 recorded events


### User

_source line 423 · 2026-05-15T00:06:57.844830+00:00_

[Reviewer 1 审稿意见]:
## 总体评分
**Overall**: 3.5/5（Findings track 可接收，需少量修改）
**一句话总结**: 方法论总体严谨，DAF 指标设计合理且有充分鲁棒性检验，但核心 claim 的 penalty-dependence 需要更显式的 qualification，且 11 个数据点的相关性分析虽有 LOO 支撑但 inferential power 有限。

## 官方维度打分（来自 ACL ARR Review Form）
| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4/5 | 实验设计 well-controlled，DAF 分解逻辑正确，鲁棒性检验充分（LOO, Spearman, bootstrap）；penalty-dependence 和小样本量是主要扣分点 |
| Excitement | 3/5 | 发现有意义（death avoidance 主导 routing signal 非 trivial），但单环境+单模型限制了 impact，且 negative result 性质限制兴奋度 |
| Overall Assessment | 3.5/5 | 符合 Findings track 标准（soundness + reproducibility），方法新颖度中等但分析深度足够 |

## Must-Fix 问题（影响接收决定）

**N1** [critical] DAF 指标的 penalty-dependence 在主文中 qualification 不足

- 具体位置：Abstract ("death avoidance accounts for approximately 90%"), §3.3, §4.1, Conclusion
- 问题：DAF = 1 - Δ_nd/Δ_full 在数学上等价于 DAF(P) = δ·P / (δ·P + Δ_nd)，其中 δ 为 death-rate differential。这意味着 DAF 是 penalty P 的单调递增函数。论文的 headline claim "~90%" 仅在 P=100 成立（Appendix D 显示 P=10 时 DAF=46.4%）。Abstract 和 Conclusion 仅用 "under the default -100 death penalty" 做了轻描淡写的限定，但读者的 takeaway 将是 "90%"。penalty-independent companion metric (78.9%) 衡量的是 label 比例而非 score gap 比例，二者概念不等价却并置呈现，容易造成混淆。
- 为什么影响接收：DAF 是论文的核心贡献指标。如果 reviewer 认为 "90%" 这个数字不具备内在意义（可通过调大 P 任意膨胀），则论文 contribution 的力度被削弱。
- 建议修改方向：(1) 在 Abstract/Introduction 中明确写出 DAF 随 P 变化的区间（如 "46%–95% across penalty magnitudes 10–200"），而非仅报 90%；(2) 更清晰地在主文（而非仅 Appendix）解释 DAF(P) 的函数形式和 penalty-independent metric 的互补关系；(3) 考虑将 78.9% death-asymmetry label fraction 提升为 co-equal headline metric，因为它不受 penalty 影响。

**N2** [critical] 11 个数据点的 Pearson r 支撑 "near-perfect correlation" 声明的 inferential power 有限

- 具体位置：§4.1 "Pearson r = 0.9698 (p = 8.12e-7)"，Figure 1
- 问题：虽然 p < 0.001 且 LOO 分析显示无 leverage point，但 n=11 的相关性分析存在根本局限：(a) 自由度仅为 9，统计功效对异常值极其敏感；(b) LOO r ∈ [0.963, 0.980] 看似稳定，但 LOO 在小样本下本身 overly optimistic（移除 1/11 的数据不会显著改变趋势）；(c) 高相关性可能部分由 restricted range 驱动——10/11 task types 的 death rate differential 和 Δ_full 高度共线（都由同一个 penalty 缩放）。
- 为什么影响接收：如果相关性声明的支撑不够 robust，则 "death avoidance explains cross-task variation" 的 generalizability claim 被削弱。
- 建议修改方向：(1) 在主文承认 n=11 是 inferential limitation（目前仅在 Limitations 提及 "covers 11 of 30 task types"，未从统计功效角度讨论）；(2) 补充 permutation test 作为非参数替代；(3) 弱化 "near-perfect" 措辞，改用 "strong positive correlation with r=0.97 across 11 task types"。

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Prescreening 排除 19/30 task types 的选择偏差未充分讨论

- 具体位置：§3.1 "After prescreening, we collect 245 episode pairs across 11 task types"，Appendix B
- 问题：排除标准是 "both strategies timed out on all seed variations within the 30-step budget"。这意味着论文的 findings 仅适用于模型有基本能力的 task types。如果 30-step budget 增加到 50 步，部分被排除的 task types 可能展现不同模式（例如非 death-dominated 的 routing signal）。此外，排除 63% 的 task types 后报告 "across ScienceWorld" 的结论可能 over-generalize。
- 建议：(1) 在 §3.1 明确写出 "our findings characterize routing signal for tasks where the model has baseline competence within the step budget"；(2) 讨论增加步数预算是否可能改变结论。

**W2** [warning] Router diagnostic 的 train/val split 过小，结论力度有限

- 具体位置：§4.3 "81 train, 14 validation episodes; 1734 train, 306 validation steps"
- 问题：14 个 validation episodes 的 balanced accuracy 估计方差极大。论文坦承 "we cannot conclusively distinguish structurally thin routing signal from data insufficiency"，这很诚实，但进一步削弱了 §4.3 的结论力度。4 seeds 的 std=0.8% 看似精确，但 internal recall 51.5%–81.8% 的巨大变异表明模型行为不稳定。
- 建议：(1) 使用 episode-level k-fold cross-validation 替代单次 85/15 split，以获得更可靠的性能估计；(2) 明确标注 router 结论为 "inconclusive diagnostic" 而非 evidence against learnability。

**W3** [warning] "Deterministic computation replaces only the state-transition prediction" 的精确含义需要更多操作化描述

- 具体位置：§3.1 第二段
- 问题：读者需要理解 deterministic strategy 的具体实现：LLM 是否仍然生成 chain-of-thought？如果是，它看到的 observation 是真实环境返回的（因为用了 exact simulator）还是自己幻觉的？如果 deterministic strategy 给 LLM 提供了真实的环境 observation（而 internal strategy 不提供），则 deterministic advantage 不仅来自 "避免 death"，还来自 "better informed action selection due to accurate observations"。这引入了混淆因素。
- 建议：用 1-2 句话精确描述两种 strategy 的信息流差异：LLM 在两种条件下分别看到什么 input，产生什么 output。

**W4** [warning] Cross-environment evidence 力度不足且方法论不统一

- 具体位置：Limitations §"Cross-environment evidence" (MATH 50 problems, ALFWorld 135 games)
- 问题：MATH pilot 仅 50 题且未报告 confidence intervals；ALFWorld 的 mechanism "differs from ScienceWorld"（action space pruning vs death avoidance），作者自己承认不能 "directly confirm that the DAF pattern generalizes"。将不同 mechanism 的 evidence 放在一起作为 "cross-environment evidence" 可能误导读者认为有泛化支撑。
- 建议：(1) 在 Conclusion 弱化 cross-environment claim 的措辞；(2) 明确 ALFWorld 展示的是 "catastrophic failure prevention 的广义现象" 而非 "DAF 指标的泛化"。

**W5** [warning] DAF 的 edge case 未讨论

- 具体位置：§3.3 DAF 定义
- 问题：DAF = 1 - Δ_nd/Δ_full。如果 Δ_nd < 0（non-death episodes 中 internal 反而更好）且 Δ_full > 0，则 DAF > 1，如何解释？虽然本数据中 Δ_nd = +2.84 > 0 不存在此问题，但作为一个 proposed metric，应讨论 edge cases（Δ_full ≤ 0, Δ_nd < 0, Δ_nd > Δ_full）的语义。
- 建议：加一句 "DAF is interpretable in [0, 1] when both Δ_full > 0 and 0 ≤ Δ_nd ≤ Δ_full; we verify these conditions hold for all 11 task types."

## 小问题（不影响接收）

- §4.3 "Qwen3-1.7B" 用于 router training，但 §3.1 数据收集用 "Qwen2.5-7B-Instruct"——两个不同模型的选择原因未解释。
- Ethics Statement 提到 "two RTX 5090 GPUs"——RTX 5090 为消费级 GPU，确认是否为 RTX 5090（vs A6000 等）以确保可复现性。
- vLLM 版本号未注明（影响可复现性）。
- Table 1 (baselines) 的 "Trained Router" 条目：是 best seed 还是 4-seed mean？应标注。
- Abstract "approximately 90%" 与主文 "90.41%" 的 precision 不一致——short paper 建议统一用 "~90%"。
- Related Work 中部分引用为 2026 年（如 cogrouter-2026, ares-2026, mtrouter-2026, retool-2026）——确认这些是已发表/preprint，而非 unpublished concurrent work misattributed as published。

## 主要优势

- **实验设计清晰且控制良好**：Pure-internal vs pure-deterministic 的对照设计干净地隔离了变量；episode-level analysis 是对 step-level oracle degeneracy 的合理回应。
- **鲁棒性检验充分**：Pearson + Spearman + Bootstrap CI + LOO + penalty sensitivity + labeling quality audit（Appendix A）——对一篇 short paper 而言，robustness evidence 的覆盖度超出预期。
- **Limitations 诚实且全面**：主动讨论了 single benchmark、penalty dependence、capability-dependent 等局限，且 cross-environment evidence 放在 Limitations 而非 overclaim 为 generalization。
- **Finding 具有实用意义**：如果 ~90% 的 routing signal 来自 death avoidance，则 routing research 的方向应从 "when to use tools" 转向 "how to predict/prevent catastrophic failure"——这对 community 有 re-framing value。
- **78.9% penalty-independent metric** 作为 companion measure 增强了 robustness，不完全依赖于 penalty magnitude 这一 hyperparameter。

## Questions for Authors

1. 在 deterministic strategy 中，LLM 的 action selection 是否基于 ground-truth environment state（即 simulator 返回的真实 observation）？如果是，deterministic advantage 是否部分来自 "更准确的 observation → 更好的 action"，而非仅 "避免 hallucination-induced death"？
2. 如果将 step budget 从 30 增加到 100，被排除的 19 个 task types 中有多少会产生 non-trivial counterfactual signal？这是否可能改变 DAF 的估计？
3. find-non-living-thing（零 death 率，Δ_full=+9.58）表明即使没有 death，deterministic computation 仍有优势。如果论文的 message 是 "routing signal = death avoidance"，如何 reconcile 这个 task type 的 routing signal 完全来自 non-death 因素？
4. Router training 用 Qwen3-1.7B 而非数据收集时的 Qwen2.5-7B-Instruct，这一 model mismatch 是否引入混淆？

## Missing References

- Garcia & Fernández (2015) "A comprehensive survey on safe reinforcement learning" 已引用 ✓
- 未见引用 **Constrained MDP / safe exploration** 方向的近期工作（如 CPO, LAMBDA 等），考虑到论文将 death avoidance 与 safe RL 关联
- 未见引用 **reward shaping / potential-based reward** 文献——death penalty 本质上是一种 reward shaping，其大小直接影响 DAF

## Confidence

4/5 — 我对方法论审查有较高信心；我熟悉 counterfactual analysis、sparse-reward environments、和 routing/tool-use 文献。对 ScienceWorld 环境的具体实现细节了解有限。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 424 · 2026-05-15T00:07:05.462982+00:00_

Reviewer 1 审稿已收到。等待 Reviewer 2 提交后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 43

## Round 43

2 recorded events


### User

_source line 425 · 2026-05-15T00:07:07.947175+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

**总结**：论文方法论总体严谨（Soundness 4/5），核心发现有意义。两个 critical 问题：(1) DAF 的 "90%" headline claim 对 penalty magnitude 的依赖在主文中 qualification 不足，可通过调大 P 任意膨胀；(2) n=11 的相关性分析 inferential power 有限，"near-perfect correlation" 措辞需弱化。5 个 warning 级问题涉及 prescreening 选择偏差、router train/val split 过小、deterministic strategy 信息流未明确、cross-environment evidence 力度不足、DAF edge cases 未讨论。Overall 推荐 3.5/5，适合 Findings track。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 426 · 2026-05-15T00:07:13.715517+00:00_

Reviewer 1 报告已收到。等待 Reviewer 2 提交。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 44

## Round 44

6 recorded events


### User

_source line 427 · 2026-05-15T00:08:38.896684+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 1 审稿报告（新颖性/完整性）

**论文**: "Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld"
**目标 Venue**: EMNLP 2026 Findings track

---

## 总体评分

**Overall**: 3/5（Findings track borderline accept）
**一句话总结**: 论文提出了清晰的 episode-level counterfactual 分析框架并发现 death avoidance 主导 routing signal，但核心发现在给定 penalty 设定下近乎 trivially expected，方法论贡献深度有限，且证据局限于单一环境/单一模型。

## 官方维度打分（来自 ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 | 主要 claim 有实验支撑，统计分析充分（bootstrap CI、LOO、Spearman），但 DAF~90% 在 P=100 下是 penalty magnitude 的直接后果，penalty-independent 指标（78.9%）更 robust 但被弱化呈现 |
| Excitement | 2/5 | 从 "capability routing" 到 "failure prevention" 的 reframing 有启发性，但 finding 的 surprising 程度有限；方法论（paired episode comparison）是标准做法的特定应用 |
| Overall | 3/5 | Findings track 可接受但需修改：贡献真实但偏窄，Related Work 有明显空缺，cross-environment 证据仅为 pilot |
| Reproducibility | 4/5 | 超参、数据划分、环境配置详尽（Appendix C），标注质量有审计（Appendix A），vLLM + ScienceWorld 均公开可用 |
| Confidence | 4/5 | 熟悉 LLM agent routing、safe RL、counterfactual evaluation 相关文献 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] DAF 的 ~90% headline claim 对 penalty magnitude 的依赖被低估

- 具体位置：Abstract 第 2 句、§3.3（DAF 定义）、Appendix E（Table 5）
- 问题：DAF = 1 − Δ_nd/Δ_full，而 Δ_full = δ·P + Δ_nd（Appendix E 公式），其中 δ=0.2653 是 death rate differential。当 P=100 时 DAF≈90%，但 P=10 时 DAF=46.4%。~90% 这个数字本质上是 penalty magnitude 的单调函数，而非 routing signal 的内在属性。论文在 §3.3 末尾和 Appendix E 确实展示了 penalty sensitivity，但 abstract、title、introduction、conclusion 全部以 "~90%" 为核心 claim，给读者的印象是这是一个 penalty-independent 的 robust finding。
- 为什么影响接收：高度依赖超参设定的度量被当作论文核心数字反复强调，存在 overclaim 风险。
- 建议修改方向：(1) 在 abstract 和 introduction 中同时强调 penalty-independent 指标（78.9% death-asymmetry labels），将其与 DAF 并列而非辅助；(2) 明确表述 "DAF is a function of penalty magnitude"；(3) 考虑将 78.9% 作为 headline number。

**N2** [critical] Related Work 缺失 counterfactual evaluation/explanation in RL 的关键文献

- 具体位置：§5 Related Work 全文、§3.1 contribution (1) 的 claim
- 问题：论文将 "episode-level counterfactual analysis" 定位为方法论贡献，但未讨论 RL 领域已有的 counterfactual explanation/evaluation 方法：
  - Explaining RL Agents through Counterfactual Action Outcomes (AAAI 2024)
  - Counterfactual Explanations for RL Agents (AAMAS 2023)
  - Counterfactual state explanations for RL via generative deep learning (AIJ 2021)
  - Off-policy evaluation 方法族
  论文的方法实际是 paired pure-strategy comparison，需与已有 counterfactual 方法精确定位。
- 为什么影响接收：方法论贡献是两个 claimed contributions 之一；定位不准确会使贡献被重估为仅剩一个 empirical finding。
- 建议修改方向：增加 "Counterfactual Evaluation in RL" 段落，精确定位 contribution 为 "applying episode-level paired comparison to diagnose routing signal composition"。

**N3** [critical] 核心 finding 的 "surprising" 程度存疑——缺少对 WHY 的分析

- 具体位置：§4.1 全文、§1 Introduction 第 7 段
- 问题：论文建立了 "death avoidance dominates" 的 WHAT，但几乎没分析 WHY。Internal strategy 42.9% death rate 从何而来？正文没有：死亡 episode 的 failure mode 分类、死亡的 temporal pattern、具体 death trajectory 示例。缺少这些分析使论文停留在近乎同义反复的层面。当读者已知 death penalty=−100 且 internal 死亡率 2.6×，DAF≈90% 可由算术直接推导。
- 为什么影响接收：对 short paper 而言，一个 "what" finding + 简单 decomposition metric，没有 "why" 分析，贡献密度偏低。
- 建议修改方向：加入 death trajectory 案例分析（可放 appendix），报告死亡 step 分布。

---

## Should-Fix 问题

**W1** [warning] Safe RL 文献覆盖不足
- 位置：§5 "Agent Frameworks" 段末
- 仅引 Garcia & Fernandez 2015 综述。缺失：Safe RL and Constrained MDPs survey (arXiv:2505.17342, 2025)、LLM agent failure attribution (ICML 2025)、"How Do LLMs Fail In Agentic Scenarios?" (arXiv:2512.07497)。
- 建议：增加 1-2 篇 2024+ safe RL / agent failure analysis 工作。

**W2** [warning] 11/30 task types 选择偏差未充分量化
- 位置：§3.1、Appendix B、Limitations
- 19/30 task types 被排除，可能是更难的任务，routing 模式可能不同。
- 建议：简要讨论被排除 task types 的特征。

**W3** [warning] Router training section 对 short paper 边际贡献低
- 位置：§4.3（约占正文 1/3 篇幅）
- Classification head 退化 + implicit router 58.1% ≈ chance，在 DAF≈90% 下近乎定义性结果。
- 建议：大幅压缩为一段，释放空间给 failure mode analysis。

**W4** [warning] find-non-living-thing 的存在 undermines "~90%" 泛化性
- 位置：§4.1 第 4 段、Appendix B
- n=40 零死亡但 Δ=+9.58，表明无 death risk 时 deterministic computation 仍有显著优势。
- 建议：更充分讨论其 implications。

**W5** [warning] Concurrent work 讨论深度不足
- 位置：§5 "Concurrent Work" 段
- tool-overuse-illusion 和 tool-use-tax 与本文高度相关，值得更深入的概念对齐。

---

## 小问题

- bib key 命名与年份不一致（toolformer-2024 实为 2023, retool-2026 实为 2025）
- react-2023 和 mixture-of-recursions-2025 在 OpenAlex 未精确匹配；dynathink-2025 first author 有 mismatch
- Data split 段放在 §4.3 末尾而非 method section，位置不常规
- 正文出现两种 DAF 值（89.6% vs 90.41%），计算口径不同但未在首次使用时说明
- Ethics Statement 提到 "two RTX 5090 GPUs"，不构成 de-anonymization 但有暗示

---

## Questions for Authors

1. 如果将 headline metric 从 DAF 改为 78.9% death-asymmetry fraction，核心 narrative 是否需要调整？
2. 105 个 internal 死亡 episode 中，死亡发生在第几步？是否集中在某些 action pattern？
3. find-non-living-thing 的 Δ=+9.58 来自什么具体的 non-death advantage？
4. 被排除的 19 个 task types 是否有共同特征？
5. 是否尝试过 larger model 的 pilot？

---

## Missing References

| 文献 | 原因 |
|------|------|
| Explaining RL Agents through Counterfactual Action Outcomes (AAAI 2024) | 需定位于已有 counterfactual-in-RL 文献 |
| Counterfactual Explanations for RL Agents (AAMAS 2023) | 同上 |
| A Survey of Safe RL and Constrained MDPs (2025) | 论文连接 safe RL 但仅引 2015 综述 |
| Which Agent Causes Task Failures and When? (ICML 2025) | Agent failure attribution 直接相关 |
| How Do LLMs Fail In Agentic Scenarios? (arXiv:2512.07497) | LLM agent failure mode categorization |

---

## 主要优势

- 清晰的实验设计：episode-level paired comparison 简洁有效，标注质量审计扎实
- 充分的统计分析：bootstrap CI、Pearson+Spearman、LOO、penalty sensitivity，统计素养高于 NLP 领域平均
- 诚实的 Limitations：坦诚承认所有主要局限
- 有价值的 reframing：routing 从 "capability matching" 到 "failure prevention"
- Cross-environment pilot 设计合理，ALFWorld 机制差异被诚实讨论

---

## Score Summary

| 项目 | 分数 |
|------|------|
| Soundness | 3/5 |
| Excitement | 2/5 |
| Overall | 3/5 |
| Reproducibility | 4/5 |
| Confidence | 4/5 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 428 · 2026-05-15T00:09:22.480417+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "simgate-modular-routing",
  "text": "## Step 2 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2（新颖性/完整性）的完整审稿意见。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n特别关注你们之间的**分歧点**和**互补发现**。\n\n---\n\n## Reviewer 2 — Round 1 审稿报告（新颖性/完整性）\n\n**Overall**: 3/5（Findings track borderline accept）\n\n### Must-Fix 问题\n\n**N1** [critical] DAF 的 ~90% headline claim 对 penalty magnitude 的依赖被低估\n- DAF = 1 − Δ_nd/Δ_full，而 Δ_full = δ·P + Δ_nd。~90% 本质上是 penalty magnitude 的单调函数，而非 routing signal 的内在属性。建议将 78.9% death-asymmetry labels 提升为 co-equal headline number。\n\n**N2** [critical] Related Work 缺失 counterfactual evaluation/explanation in RL 的关键文献\n- 论文将 \"episode-level counterfactual analysis\" 定位为方法论贡献，但未讨论 RL 领域已有的 counterfactual explanation/evaluation 方法（AAAI 2024, AAMAS 2023, AIJ 2021, off-policy evaluation）。方法论贡献定位不准确可能使贡献被重估为仅剩一个 empirical finding。\n\n**N3** [critical] 核心 finding 的 \"surprising\" 程度存疑——缺少对 WHY 的分析\n- 论文建立了 \"death avoidance dominates\" 的 WHAT，但几乎没分析 WHY。Internal strategy 42.9% death rate 从何而来？缺少死亡 episode 的 failure mode 分类、死亡的 temporal pattern、具体 death trajectory 示例。当读者已知 death penalty=−100 且 internal 死亡率 2.6×，DAF≈90% 可由算术直接推导。\n\n### Should-Fix 问题\n\n**W1** [warning] Safe RL 文献覆盖不足——仅引 Garcia & Fernandez 2015 综述，缺 2024+ safe RL / agent failure analysis 工作。\n\n**W2** [warning] 11/30 task types 选择偏差未充分量化——被排除的 19/30 task types 特征未讨论。\n\n**W3** [warning] Router training section（§4.3）对 short paper 边际贡献低——约占正文 1/3 篇幅，但 classification head 退化 + implicit router 58.1% ≈ chance 在 DAF≈90% 下是近乎定义性结果。建议大幅压缩为一段，释放空间给 failure mode analysis。\n\n**W4** [warning] find-non-living-thing 的存在 undermines \"~90%\" 泛化性——n=40 零死亡但 Δ=+9.58，表明无 death risk 时 deterministic computation 仍有显著优势。\n\n**W5** [warning] Concurrent work 讨论深度不足——tool-overuse-illusion 和 tool-use-tax 与本文高度相关。\n\n### 小问题\n- bib key 命名与年份不一致（toolformer-2024 实为 2023, retool-2026 实为 2025）\n- 正文两种 DAF 值（89.6% vs 90.41%），计算口径不同但未在首次使用时说明\n- Data split 段位置不常规\n- Ethics Statement \"two RTX 5090 GPUs\" 有暗示性\n\n### Questions\n1. 如果将 headline metric 从 DAF 改为 78.9% death-asymmetry fraction，核心 narrative 是否需要调整？\n2. 105 个 internal 死亡 episode 中，死亡发生在第几步？是否集中在某些 action pattern？\n3. find-non-living-thing 的 Δ=+9.58 来自什么具体的 non-death advantage？\n4. 被排除的 19 个 task types 是否有共同特征？\n\n### Missing References\n- Explaining RL Agents through Counterfactual Action Outcomes (AAAI 2024)\n- Counterfactual Explanations for RL Agents (AAMAS 2023)\n- A Survey of Safe RL and Constrained MDPs (2025)\n- Which Agent Causes Task Failures and When? (ICML 2025)\n- How Do LLMs Fail In Agentic Scenarios? (arXiv:2512.07497)\n\n### 主要优势\n- 清晰的实验设计、充分的统计分析、诚实的 Limitations、有价值的 reframing、cross-environment pilot 设计合理\n\n---\n\n请对以上每个 Must-Fix (N1-N3)、Should-Fix (W1-W5)、小问题、Questions 逐条给出 [AGREE] 或 [REBUT] 回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "simgate-modular-routing",
    "text": "## Step 2 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2（新颖性/完整性）的完整审稿意见。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n特别关注你们之间的**分歧点**和**互补发现**。\n\n---\n\n## Reviewer 2 — Round 1 审稿报告（新颖性/完整性）\n\n**Overall**: 3/5（Findings track borderline accept）\n\n### Must-Fix 问题\n\n**N1** [critical] DAF 的 ~90% headline claim 对 penalty magnitude 的依赖被低估\n- DAF = 1 − Δ_nd/Δ_full，而 Δ_full = δ·P + Δ_nd。~90% 本质上是 penalty magnitude 的单调函数，而非 routing signal 的内在属性。建议将 78.9% death-asymmetry labels 提升为 co-equal headline number。\n\n**N2** [critical] Related Work 缺失 counterfactual evaluation/explanation in RL 的关键文献\n- 论文将 \"episode-level counterfactual analysis\" 定位为方法论贡献，但未讨论 RL 领域已有的 counterfactual explanation/evaluation 方法（AAAI 2024, AAMAS 2023, AIJ 2021, off-policy evaluation）。方法论贡献定位不准确可能使贡献被重估为仅剩一个 empirical finding。\n\n**N3** [critical] 核心 finding 的 \"surprising\" 程度存疑——缺少对 WHY 的分析\n- 论文建立了 \"death avoidance dominates\" 的 WHAT，但几乎没分析 WHY。Internal strategy 42.9% death rate 从何而来？缺少死亡 episode 的 failure mode 分类、死亡的 temporal pattern、具体 death trajectory 示例。当读者已知 death penalty=−100 且 internal 死亡率 2.6×，DAF≈90% 可由算术直接推导。\n\n### Should-Fix 问题\n\n**W1** [warning] Safe RL 文献覆盖不足——仅引 Garcia & Fernandez 2015 综述，缺 2024+ safe RL / agent failure analysis 工作。\n\n**W2** [warning] 11/30 task types 选择偏差未充分量化——被排除的 19/30 task types 特征未讨论。\n\n**W3** [warning] Router training section（§4.3）对 short paper 边际贡献低——约占正文 1/3 篇幅，但 classification head 退化 + implicit router 58.1% ≈ chance 在 DAF≈90% 下是近乎定义性结果。建议大幅压缩为一段，释放空间给 failure mode analysis。\n\n**W4** [warning] find-non-living-thing 的存在 undermines \"~90%\" 泛化性——n=40 零死亡但 Δ=+9.58，表明无 death risk 时 deterministic computation 仍有显著优势。\n\n**W5** [warning] Concurrent work 讨论深度不足——tool-overuse-illusion 和 tool-use-tax 与本文高度相关。\n\n### 小问题\n- bib key 命名与年份不一致（toolformer-2024 实为 2023, retool-2026 实为 2025）\n- 正文两种 DAF 值（89.6% vs 90.41%），计算口径不同但未在首次使用时说明\n- Data split 段位置不常规\n- Ethics Statement \"two RTX 5090 GPUs\" 有暗示性\n\n### Questions\n1. 如果将 headline metric 从 DAF 改为 78.9% death-asymmetry fraction，核心 narrative 是否需要调整？\n2. 105 个 internal 死亡 episode 中，死亡发生在第几步？是否集中在某些 action pattern？\n3. find-non-living-thing 的 Δ=+9.58 来自什么具体的 non-death advantage？\n4. 被排除的 19 个 task types 是否有共同特征？\n\n### Missing References\n- Explaining RL Agents through Counterfactual Action Outcomes (AAAI 2024)\n- Counterfactual Explanations for RL Agents (AAMAS 2023)\n- A Survey of Safe RL and Constrained MDPs (2025)\n- Which Agent Causes Task Failures and When? (ICML 2025)\n- How Do LLMs Fail In Agentic Scenarios? (arXiv:2512.07497)\n\n### 主要优势\n- 清晰的实验设计、充分的统计分析、诚实的 Limitations、有价值的 reframing、cross-environment pilot 设计合理\n\n---\n\n请对以上每个 Must-Fix (N1-N3)、Should-Fix (W1-W5)、小问题、Questions 逐条给出 [AGREE] 或 [REBUT] 回应。"
  }
}
```

</details>

---


### Tool result

_source line 429 · 2026-05-15T00:09:55.654403+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 33173
}
```

</details>

---


### Tool call

_source line 430 · 2026-05-15T00:09:55.855613+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "simgate-modular-routing",
  "text": "## Step 2 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1（方法严谨性）的完整审稿意见。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n特别关注你们之间的**分歧点**和**互补发现**。\n\n---\n\n## Reviewer 1 — Round 1 审稿报告（方法严谨性）\n\n**Overall**: 3.5/5（Findings track 可接收，需少量修改）\n**Soundness**: 4/5 | **Excitement**: 3/5\n\n### Must-Fix 问题\n\n**N1** [critical] DAF 指标的 penalty-dependence 在主文中 qualification 不足\n- DAF(P) = δ·P / (δ·P + Δ_nd) 是 P 的单调递增函数。\"~90%\" 仅在 P=100 成立（P=10 时 DAF=46.4%）。Abstract 和 Conclusion 仅用 \"under the default -100 death penalty\" 做轻描淡写限定。78.9% penalty-independent companion metric 衡量的是 label 比例而非 score gap 比例，与 DAF 概念不等价却并置呈现。\n- 建议：(1) Abstract/Introduction 中写出 DAF 随 P 变化的区间；(2) 主文解释 DAF(P) 函数形式；(3) 考虑将 78.9% 提升为 co-equal headline metric。\n\n**N2** [critical] 11 个数据点的 Pearson r 支撑 \"near-perfect correlation\" 声明的 inferential power 有限\n- n=11 自由度仅为 9，LOO 在小样本下 overly optimistic。高相关性可能由 restricted range 驱动——10/11 task types 的 death rate differential 和 Δ_full 高度共线（都由同一个 penalty 缩放）。\n- 建议：(1) 承认 n=11 是 inferential limitation；(2) 补充 permutation test；(3) 弱化 \"near-perfect\" 措辞。\n\n### Should-Fix 问题\n\n**W1** [warning] Prescreening 排除 19/30 task types 的选择偏差未充分讨论\n- 排除标准是 \"both strategies timed out\"，findings 仅适用于模型有基本能力的 task types。增加步数预算可能改变结论。\n\n**W2** [warning] Router diagnostic 的 train/val split 过小\n- 14 validation episodes 的 balanced accuracy 估计方差极大。Internal recall 51.5%–81.8% 表明模型行为不稳定。\n- 建议：episode-level k-fold cross-validation。\n\n**W3** [warning] \"Deterministic computation replaces only the state-transition prediction\" 需更多操作化描述\n- 如果 deterministic strategy 给 LLM 提供了真实环境 observation（而 internal 不提供），则 deterministic advantage 不仅来自 \"避免 death\"，还来自 \"better informed action selection\"——引入混淆因素。\n\n**W4** [warning] Cross-environment evidence 力度不足且方法论不统一\n- MATH pilot 仅 50 题未报告 CI；ALFWorld mechanism 不同（action space pruning vs death avoidance）。\n\n**W5** [warning] DAF 的 edge case 未讨论\n- 如果 Δ_nd < 0（internal 反而更好）且 Δ_full > 0，则 DAF > 1。应讨论 edge cases 的语义。\n\n### 小问题\n- Qwen3-1.7B (router) vs Qwen2.5-7B-Instruct (data collection) 选择原因未解释\n- RTX 5090 确认\n- vLLM 版本号未注明\n- Table 1 \"Trained Router\" 是 best seed 还是 4-seed mean？\n- Abstract \"approximately 90%\" vs 主文 \"90.41%\" precision 不一致\n- 2026 年引用确认为已发表/preprint\n\n### Questions\n1. Deterministic strategy 中 LLM action selection 是否基于 ground-truth state？\n2. Step budget 增加到 100 时，被排除 task types 是否改变 DAF？\n3. find-non-living-thing 的 non-death routing signal 如何 reconcile with \"routing signal = death avoidance\"？\n4. Router training 的 model mismatch (Qwen3-1.7B vs Qwen2.5-7B) 是否引入混淆？\n\n### Missing References\n- Constrained MDP / safe exploration（CPO, LAMBDA 等）\n- Reward shaping / potential-based reward 文献\n\n### 主要优势\n- 实验设计清晰且控制良好\n- 鲁棒性检验充分（Pearson + Spearman + Bootstrap CI + LOO + penalty sensitivity + labeling quality audit）\n- Limitations 诚实且全面\n- Finding 具有实用意义（reframing routing research direction）\n- 78.9% penalty-independent metric 增强 robustness\n\n---\n\n请对以上每个 Must-Fix (N1-N2)、Should-Fix (W1-W5)、小问题、Questions 逐条给出 [AGREE] 或 [REBUT] 回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "simgate-modular-routing",
    "text": "## Step 2 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1（方法严谨性）的完整审稿意见。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n特别关注你们之间的**分歧点**和**互补发现**。\n\n---\n\n## Reviewer 1 — Round 1 审稿报告（方法严谨性）\n\n**Overall**: 3.5/5（Findings track 可接收，需少量修改）\n**Soundness**: 4/5 | **Excitement**: 3/5\n\n### Must-Fix 问题\n\n**N1** [critical] DAF 指标的 penalty-dependence 在主文中 qualification 不足\n- DAF(P) = δ·P / (δ·P + Δ_nd) 是 P 的单调递增函数。\"~90%\" 仅在 P=100 成立（P=10 时 DAF=46.4%）。Abstract 和 Conclusion 仅用 \"under the default -100 death penalty\" 做轻描淡写限定。78.9% penalty-independent companion metric 衡量的是 label 比例而非 score gap 比例，与 DAF 概念不等价却并置呈现。\n- 建议：(1) Abstract/Introduction 中写出 DAF 随 P 变化的区间；(2) 主文解释 DAF(P) 函数形式；(3) 考虑将 78.9% 提升为 co-equal headline metric。\n\n**N2** [critical] 11 个数据点的 Pearson r 支撑 \"near-perfect correlation\" 声明的 inferential power 有限\n- n=11 自由度仅为 9，LOO 在小样本下 overly optimistic。高相关性可能由 restricted range 驱动——10/11 task types 的 death rate differential 和 Δ_full 高度共线（都由同一个 penalty 缩放）。\n- 建议：(1) 承认 n=11 是 inferential limitation；(2) 补充 permutation test；(3) 弱化 \"near-perfect\" 措辞。\n\n### Should-Fix 问题\n\n**W1** [warning] Prescreening 排除 19/30 task types 的选择偏差未充分讨论\n- 排除标准是 \"both strategies timed out\"，findings 仅适用于模型有基本能力的 task types。增加步数预算可能改变结论。\n\n**W2** [warning] Router diagnostic 的 train/val split 过小\n- 14 validation episodes 的 balanced accuracy 估计方差极大。Internal recall 51.5%–81.8% 表明模型行为不稳定。\n- 建议：episode-level k-fold cross-validation。\n\n**W3** [warning] \"Deterministic computation replaces only the state-transition prediction\" 需更多操作化描述\n- 如果 deterministic strategy 给 LLM 提供了真实环境 observation（而 internal 不提供），则 deterministic advantage 不仅来自 \"避免 death\"，还来自 \"better informed action selection\"——引入混淆因素。\n\n**W4** [warning] Cross-environment evidence 力度不足且方法论不统一\n- MATH pilot 仅 50 题未报告 CI；ALFWorld mechanism 不同（action space pruning vs death avoidance）。\n\n**W5** [warning] DAF 的 edge case 未讨论\n- 如果 Δ_nd < 0（internal 反而更好）且 Δ_full > 0，则 DAF > 1。应讨论 edge cases 的语义。\n\n### 小问题\n- Qwen3-1.7B (router) vs Qwen2.5-7B-Instruct (data collection) 选择原因未解释\n- RTX 5090 确认\n- vLLM 版本号未注明\n- Table 1 \"Trained Router\" 是 best seed 还是 4-seed mean？\n- Abstract \"approximately 90%\" vs 主文 \"90.41%\" precision 不一致\n- 2026 年引用确认为已发表/preprint\n\n### Questions\n1. Deterministic strategy 中 LLM action selection 是否基于 ground-truth state？\n2. Step budget 增加到 100 时，被排除 task types 是否改变 DAF？\n3. find-non-living-thing 的 non-death routing signal 如何 reconcile with \"routing signal = death avoidance\"？\n4. Router training 的 model mismatch (Qwen3-1.7B vs Qwen2.5-7B) 是否引入混淆？\n\n### Missing References\n- Constrained MDP / safe exploration（CPO, LAMBDA 等）\n- Reward shaping / potential-based reward 文献\n\n### 主要优势\n- 实验设计清晰且控制良好\n- 鲁棒性检验充分（Pearson + Spearman + Bootstrap CI + LOO + penalty sensitivity + labeling quality audit）\n- Limitations 诚实且全面\n- Finding 具有实用意义（reframing routing research direction）\n- 78.9% penalty-independent metric 增强 robustness\n\n---\n\n请对以上每个 Must-Fix (N1-N2)、Should-Fix (W1-W5)、小问题、Questions 逐条给出 [AGREE] 或 [REBUT] 回应。"
  }
}
```

</details>

---


### Tool result

_source line 431 · 2026-05-15T00:09:57.216328+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1360
}
```

</details>

---


### Assistant

_source line 432 · 2026-05-15T00:10:00.018636+00:00_

交叉分享已发送。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 45

## Round 45

2 recorded events


### User

_source line 433 · 2026-05-15T00:10:02.589621+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

核心判断：Overall 3/5（Findings borderline accept）。三个 critical 问题：(1) DAF ~90% 是 penalty magnitude 的函数而非 robust finding，应以 78.9% death-asymmetry fraction 为主；(2) 缺失 counterfactual evaluation in RL 关键文献，方法论贡献定位偏高；(3) 只有 "what"（death avoidance dominates）没有 "why"（internal 为什么死那么多），贡献密度不足。五个 warning 级问题涉及 safe RL 文献覆盖、task selection bias、router training 占比过大等。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 434 · 2026-05-15T00:10:06.890543+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 46

## Round 46

2 recorded events


### User

_source line 435 · 2026-05-15T00:11:15.651356+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Must-Fix 问题

**[AGREE] R2-N1: DAF headline claim 对 penalty magnitude 的依赖被低估**

完全同意。这与我的 N1 高度一致。补充一点数学论证：DAF(P) = δP / (δP + Δ_nd) 是 P 的单调递增函数，极限为 lim_{P→∞} DAF = 1。因此任何 environment 只要有 non-zero death-rate differential，都能通过调大 penalty 得到任意接近 100% 的 DAF。这意味着 "90%" 不是 routing signal 的内在属性，而是 penalty 选择的产物。R2 建议将 78.9% death-asymmetry labels 提升为 co-equal headline metric，我支持——它度量的是 "多少比例的 routing decisions 由 death 驱动"，不受 penalty scaling 影响。

**[AGREE with nuance] R2-N2: Related Work 缺失 counterfactual evaluation/explanation in RL 文献**

同意缺失是一个问题，但对 severity 的判断略有不同。论文的 "episode-level counterfactual analysis" 与 RL counterfactual explanations 有概念重叠但操作上不同：RL counterfactual explanations（如 R2 所引 AAAI 2024, AAMAS 2023）通常是 post-hoc 解释已有 policy 的决策，而本文是 A/B 式对照实验（run two complete trajectories under different strategies）。Off-policy evaluation 更不同——它从 logged data 估计未执行 policy 的价值，不需要重新执行。

**但**，论文将 "counterfactual" 一词置于标题和 contribution statement，就有义务 contextualize 它与 RL counterfactual 文献的关系。建议在 Related Work 加一段区分："Unlike counterfactual explanations that explain why an agent chose action A over B (post-hoc), our counterfactual analysis runs complete episodes under alternative strategies (prospective A/B comparison)."

这不至于 "reframe contribution as mere empirical finding"（R2 的担忧），因为本文的方法论贡献不是 "发明 counterfactual analysis" 而是 "将 episode-level counterfactual 应用于 routing signal decomposition in sparse-reward environments"——加引用不会削弱这一定位。

**[REBUT] R2-N3: 核心 finding 的 "surprising" 程度存疑——缺少 WHY 分析**

部分不同意将此标为 critical。理由：

1. **论文的贡献定位是 decomposition/quantification，不是 mechanism explanation。** §1 明确将贡献表述为 "identifying step-level oracle degeneracy" 和 "the empirical finding that death avoidance accounts for ~90%"。这是一个 diagnostic/analytical contribution，而非 mechanistic explanation。要求 failure mode taxonomy 是要求作者写一篇不同的论文。

2. **"算术可推导" 的批评需要更精确。** R2 说 "当读者已知 death penalty=−100 且 death rate 2.6×，DAF≈90% 可由算术直接推导"。但这是事后诸葛亮——在做实验之前，谁知道 death rate differential 是 26.6 percentage points（42.9% vs 16.3%）？论文的贡献不是 DAF 公式本身，而是**经验性地发现** death-rate differential 如此之大以至于主导了整个 routing signal。这个经验事实不可由算术推导。

3. **但 R2 的建议有价值。** 如果论文能加入 1-2 句关于 death episodes 的 temporal pattern（e.g., "deaths cluster in steps 5-15 when the agent first interacts with temperature-sensitive objects"），会显著增强论文的 insight 密度，且 short paper 可以容纳。

**综合判断：** 降为 should-fix（W 级）更合适。Failure mode analysis 是 bonus 而非 acceptance-blocking requirement。

---

### Should-Fix 问题

**[AGREE] R2-W1: Safe RL 文献覆盖不足**

同意。我也在 Missing References 中指出了类似问题（CPO, LAMBDA 等 constrained MDP 工作）。仅引 Garcia & Fernandez 2015 综述对 2026 年的 paper 不够。

**[AGREE] R2-W2: 11/30 task types 选择偏差未充分量化**

同意，与我的 W1 一致。补充：Appendix B 给出了 prescreening 标准但未分析被排除 task types 的共同特征（是否更难？action space 更大？需要更多步？）。这类信息能帮助读者判断 findings 的 scope。

**[REBUT] R2-W3: Router section 对 short paper 边际贡献低，建议大幅压缩**

不同意。Router diagnostic section（§4.3）提供了 DAF 分析之外的**独立验证**：

1. **Classification head degeneration** 独立确认了 routing signal 的 thin nature——如果 signal 充足，即使简单的 linear head 也应学到 non-trivial pattern。Degeneration 为 "DAF≈90% → router headroom 仅 ~10%" 提供了 behavioral evidence。

2. **Implicit router 58.1% ≈ chance** 不是 "近乎定义性结果"。DAF≈90% 意味着 ~10% 的 signal 存在，一个好的 router 仍可能达到 ~65-70% balanced accuracy（如果能 capture 所有 non-death signal）。58.1% 说明 router 连 non-death signal 也无法有效学习——这额外表明 episode-to-step granularity mismatch 是独立瓶颈（§4.3 "Logit-level success rules out uninformative labels, pointing to the episode-to-step granularity mismatch as the bottleneck"）。

3. **End-to-end evaluation**（Table 1 trained router vs always-deterministic）是论文从 analytical finding 到 practical implication 的桥梁——"即使你训练了 router，也不比 always-det 好"。

建议：适度压缩（如删除 keyword baseline 的详细数据），但不应 "大幅压缩为一段"。

**[AGREE with nuance] R2-W4: find-non-living-thing undermines ~90% 泛化性**

部分同意。该 task type（n=40, zero deaths, Δ=+9.58）确实表明 deterministic advantage 可以完全来自 non-death factors。但论文在 §4.1 已明确讨论："deterministic computation can provide advantages through more accurate state tracking even when agents survive"。

问题不是 "undermine"——90% 是对 245 episodes 整体的正确 decomposition——而是论文应更显式地讨论 task-level heterogeneity。如果按 task type 计算 DAF，find-non-living-thing 的 DAF = 0%（因为 Δ_nd = Δ_full），而其他 10 个 task types 的 DAF > 90%。这种 bimodal 分布值得一句话指出。

**[AGREE] R2-W5: Concurrent work 讨论深度不足**

同意。tool-overuse-illusion 和 tool-use-tax 与本文的 "routing signal 主要是 failure prevention 而非 positive guidance" 结论高度互补。目前 Related Work 仅用一句 listing 带过，应解释本文如何 ground/quantify 这些框架的 insight。

---

### 小问题

**[AGREE]** bib key 命名与年份不一致——确认 Toolformer 为 Schick et al. 2023 NeurIPS，key 应为 toolformer-2023。

**[AGREE]** 正文两种 DAF 值（89.6% vs 90.41%）确实令人困惑。Appendix D 表注解释了计算口径差异（both-died episodes 是否纳入 non-death pool），但首次出现 89.6% 时（§3.3 penalty sensitivity 段）应即时注明 "differs from the main-text figure due to ..."。

**[AGREE]** Data split 段位于 §4.3 末尾位置不常规——通常 experimental setup / data split 应在 results 之前。

**[AGREE]** RTX 5090 注意——我也标注了此点。

---

### Questions 评估

**R2-Q1**（改 headline 为 78.9%）：与我的 N1 建议一致。我认为 dual reporting（DAF@P=100 + penalty-independent 78.9%）是最佳策略。

**R2-Q2**（death temporal pattern）：好问题。与 R2-N3 相关。如果死亡集中在早期步骤，说明 routing decision 可以很早做出；如果分散，说明需要 per-step dynamic routing。这对 practical implication 有重要影响。

**R2-Q3**（find-non-living-thing 的 non-death advantage 来源）：好问题。我在 Q3 也提出了相同问题。

**R2-Q4**（被排除 19 个 task types 的共同特征）：与 W2 相关，有价值。

---

### 总结：分歧与互补

**主要分歧：**
1. **R2-N3 severity**：R2 标为 critical，我认为应为 should-fix。论文定位为 decomposition/quantification contribution，不需要 mechanism explanation 作为 acceptance condition。
2. **R2-W3 router section**：R2 建议大幅压缩，我认为它提供了独立验证且结论不 trivially derivable from DAF。

**互补发现：**
1. R2 从新颖性角度指出的 counterfactual RL 文献缺失，补充了我从方法论角度关注的 "correlation ≠ causation" 问题——如果论文能 contextualize 其 counterfactual 方法在更广文献中的位置，会同时解决两个问题。
2. 我们对 N1（penalty-dependence）高度一致，双方独立发现说明这是 real concern。
3. R2 的 failure mode analysis 需求（N3）与我的 Q1（deterministic strategy 的 information flow）互补——两者都在问 "death avoidance 背后的具体 mechanism 是什么"。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 436 · 2026-05-15T00:11:21.457350+00:00_

收到 Reviewer 1 的交叉回应。等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 47

## Round 47

8 recorded events


### User

_source line 437 · 2026-05-15T00:11:22.499248+00:00_

[Reviewer 2 审稿结果]:
## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

### Must-Fix 问题

**[AGREE] R1-N1: DAF 的 penalty-dependence qualification 不足**

完全同意，这与我的 N1 发现一致。我要补充一点：R1 指出 "78.9% 衡量的是 label 比例而非 score gap 比例，与 DAF 概念不等价却并置呈现"——这个区分非常精准。论文在 §3.3 末尾将 78.9% 作为 "penalty-independent companion metric" 与 DAF 并列，但两者度量的维度不同（label count fraction vs score gap fraction），并置呈现确实容易误导读者以为两者互相验证同一结论。我的 N1 建议将 78.9% 提升为 headline metric；R1 的补充建议（写出 DAF(P) 函数形式、给出 DAF 随 P 变化区间）更具操作性。两条建议应同时采纳。

**[AGREE] R1-N2: n=11 的 Pearson r inferential power 有限**

同意核心论点。n=11、df=9 下即便 p=8.12×10⁻⁷ 看起来很小，但 restricted range 问题是真实的：10/11 task types 都有非零 death rate differential，death rate differential 和 Δ\_full 本质上通过同一个 P 线性耦合（Δ\_full = δ\_task · P + Δ\_nd\_task），因此高相关性部分是数学结构的产物而非独立的经验发现。论文的 Spearman ρ=0.986 和 LOO 分析（Appendix C）缓解了 outlier concern，但不解决 restricted range 和 structural coupling 问题。

不过我要补充：**permutation test 在这里的意义有限**——因为 structural coupling（两个变量共享 P 作为 scaling factor）不是 permutation test 能检测的问题，permutation test 只验证 null hypothesis of no association，而这里的问题是 association 部分来自数学结构而非经验。更有效的建议是：(1) 弱化 "near-perfect" 措辞为 "strong"；(2) 在正文承认 n=11 + structural coupling 的局限性；(3) 如果有多个 penalty 水平的真实数据（而非 Appendix E 的算术外推），可以做更有力的验证。

---

### Should-Fix 问题

**[AGREE] R1-W1: Prescreening 选择偏差**

同意，与我的 W2 一致。R1 额外指出 "增加步数预算可能改变结论"，这是一个我未提及的有效维度——如果 step budget 从 30 增加到 60/100，当前 timeout 的 task types 可能变得可分析，且 death pattern 可能不同（更多步数 → 更多 death 机会 → DAF 可能更高；或者更多步数 → 更多 recovery 机会 → DAF 可能更低）。方向性不确定，但值得作为 limitation 讨论。

**[AGREE] R1-W2: Router diagnostic train/val split 过小**

同意 14 validation episodes 的估计方差问题。但我对此 issue 的优先级判断不同：我在 W3 中建议**大幅压缩整个 §4.3**，因为 router training 在 DAF≈90% 的前提下是一个近乎定义性的 negative result。如果 §4.3 被压缩为一段总结，k-fold cross-validation 的需求也随之降低。如果作者选择保留 §4.3 的当前篇幅，则同意 R1 的 k-fold 建议。

**[REBUT] R1-W3: Deterministic strategy 的 "better informed action selection" 混淆因素**

R1 的担忧是：如果 deterministic strategy 给 LLM 提供了 ground-truth observation 而 internal strategy 没有，则 deterministic advantage 不仅来自 death avoidance，还来自 better informed action selection，引入混淆。

但 §3.1 第 2 段（method.tex 第 8 行）明确写道："deterministic computation replaces only the state-transition prediction, not action selection—equivalent to giving the agent access to a perfect dynamics model." 这说明**两种策略的 action selection 使用的是同一个 LLM**，区别仅在于 state transition 的来源（LLM hallucination vs ground-truth simulator）。如果 deterministic strategy 的 observation 更准确，那 LLM 在后续 step 会基于更准确的 state 做 action selection——但这正是 "避免 hallucination cascade 导致 death" 的机制本身，而非独立于 death avoidance 的混淆因素。

也就是说，R1 担忧的 "better informed action selection" **就是** death avoidance 的实现机制（accurate state → fewer hallucination-induced deaths），不是独立的混淆变量。find-non-living-thing 的 Δ=+9.58（零死亡）确实表明 accurate state tracking 本身有 non-death 价值，但论文已经在 §4.1 第 4 段讨论了这一点。

不过 R1 的提问角度揭示了一个表述问题：§3.1 的操作化描述确实不够详细——读者无法仅从 "replaces only the state-transition prediction" 判断 LLM 在 deterministic mode 下看到的 observation 是什么格式。建议增加 1-2 句操作化描述（如 "In deterministic mode, the LLM receives the ground-truth environment observation string after each action; in internal mode, the LLM generates its own prediction of the next observation"）。

**[AGREE] R1-W4: Cross-environment evidence 力度不足且方法论不统一**

同意。MATH pilot 50 题无 CI、ALFWorld 机制不同——这些都是真实局限。我在主审中未将此列为独立 issue，因为这些 evidence 已放在 Limitations 而非 Experiments。但 R1 的建议合理：如果要在 Conclusion 中引用这些 cross-environment evidence（conclusion.tex 确实引用了），则至少应为 MATH 报告 CI 或 effect size。

**[REBUT] R1-W5: DAF > 1 的 edge case**

R1 指出如果 Δ\_nd < 0（internal 在非死亡 episode 反超）且 Δ\_full > 0，则 DAF > 1。数学上正确，但在本文数据中这种情况未出现（Δ\_nd = +2.84 > 0）。作为一个 metric 定义的 completeness concern，这是合理的学术建议，但 severity 不应是 warning——它更接近 info level。

理由：(1) DAF 在本文中是一个 diagnostic metric applied to specific data，不是作为通用工具提出的；(2) DAF > 1 的语义其实很清晰——"death avoidance 的贡献超过了 full gap，因为 non-death signal 反方向"——这不是 undefined 或 nonsensical，只是需要 1 句话解释；(3) 对 short paper 而言，为一个在数据中未出现的 edge case 增加讨论篇幅的 ROI 很低。

建议折中：在 §3.3 脚注中加一句 "When Δ\_nd < 0, DAF exceeds 1, indicating that death avoidance more than accounts for the full gap" 即可。

---

### 小问题

**[AGREE] Qwen3-1.7B vs Qwen2.5-7B 选择原因未解释**
确认。这也与 R1 的 Question 4 相关。Router 用不同模型（更小、不同 generation）做 diagnostic 是合理的设计选择（避免用同一模型做 data collection 和 routing），但论文应说明理由。

**[AGREE] vLLM 版本号未注明**
合理的 reproducibility concern。

**[AGREE] Table 1 "Trained Router" 是 best seed 还是 4-seed mean 不明确**
确认。§4.3 第 2 段报告 4-seed balanced accuracy 但 Table 1 的 −10.70 未说明是哪个 seed 或均值。

**[AGREE] Abstract "approximately 90%" vs 主文 "90.41%" precision 不一致**
与我指出的 "两种 DAF 值（89.6% vs 90.41%）计算口径不同" 互补。论文中出现三个 DAF 数字：~90%（abstract）、90.41%（§4.1，strict neither-died filtering）、89.6%（Appendix E，includes both-died in non-death pool），需要统一或明确标注。

**[AGREE] RTX 5090 确认**
与我的观察一致，不构成 de-anonymization 但值得作者注意。

**[REBUT] 2026 年引用确认为已发表/preprint**
引用验证结果显示：cogrouter-2026、ares-2026、mtrouter-2026、tool-overuse-illusion-2026、when2tool-2026、tool-use-tax-2026、to-call-or-not-2026 均在 OpenAlex 验证通过。这些是合法的 arXiv preprint 或已发表工作，不需要特别确认。唯一需注意的是 mixture-of-recursions-2025 在 OpenAlex 未精确匹配（可能是索引延迟），建议核实。

---

### Questions

**[AGREE] Q1: Deterministic strategy 中 LLM action selection 是否基于 ground-truth state？**
如上 W3 回应中讨论，这是一个关键的操作化细节，论文应更清晰地描述。

**[AGREE] Q2: Step budget 增加时被排除 task types 是否改变 DAF？**
有效问题，与 W1 互补。

**[AGREE] Q3: find-non-living-thing 的 non-death signal 如何 reconcile？**
与我的 W4 一致——这是论文需要更充分讨论的关键 anomaly。

**[AGREE] Q4: Router model mismatch 是否引入混淆？**
与上述 Qwen3-1.7B vs Qwen2.5-7B 小问题一致。

---

### Missing References

**[AGREE] Constrained MDP / safe exploration（CPO, LAMBDA 等）**
与我的 W1 一致。论文连接 safe RL 但文献覆盖严重不足。

**[REBUT] Reward shaping / potential-based reward 文献**
不确定此建议的相关性。论文不做 reward shaping——DAF 是一个 post-hoc diagnostic metric，不修改 reward function。如果 R1 的意思是 "penalty magnitude 的选择等同于 reward design"，那 connection 比较间接。对 short paper 的 4 页正文限制而言，增加 reward shaping 文献的 ROI 偏低。

---

### 总结：关键分歧与互补

**分歧点：**
1. **W3（混淆因素）**：我认为 "better informed action selection" 是 death avoidance 的机制而非独立混淆变量，但同意 §3.1 操作化描述不足。
2. **W5（DAF edge case）**：我认为 severity 应降为 info，脚注即可处理。
3. **Reward shaping 文献**：我认为与本文关联度不够，不建议添加。

**互补发现：**
1. 我的 N2（缺失 counterfactual-in-RL 文献）和 N3（缺少 WHY 分析）是 R1 未重点覆盖的维度，与 R1 的方法严谨性审查形成互补。
2. R1 的 N2（n=11 inferential power + structural coupling）比我的处理更深入，我同意并补充了 permutation test 局限性。
3. 两位 reviewer 对 N1（DAF penalty-dependence）和 W1/W2（selection bias）高度一致，构成 convergent evidence for revision need。

---

[Reviewer 1 审稿结果]:
交叉回应已提交。主要分歧两点：(1) R2-N3（WHY 分析缺失）我认为应降为 should-fix，论文定位是 decomposition 而非 mechanism explanation；(2) R2-W3（router section 压缩）我反对大幅压缩，该 section 提供了独立验证。其余 N1（penalty-dependence）、W1/W2/W4/W5 高度一致。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 438 · 2026-05-15T00:11:51.511208+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 439 · 2026-05-15T00:11:51.612351+00:00_

1	- id: "R4-W1"
2	  summary: "DAF ~90% headline needs penalty conditioning (P=100) + penalty-independent metric (75/95=78.9%)"
3	  category: method
4	  severity: critical
5	  status: resolved
6	  first_raised_round: 4
7	  last_seen_round: 5
8	  mentions:
9	    - round: 4
10	      reviewers: [1, 2]
11	      note: "Consensus. DAF is monotonically increasing function of P."
12	    - round: 5
13	      reviewers: [1, 2]
14	      note: "RESOLVED. Related Work residual fixed via R5-CR1."
15	  action_items:
16	    - round: 4
17	      action: "Abstract/Conclusion add 'under P=100'; introduce 75/95=78.9%"
18	      assigned_to: main_agent
19	      status: done
20	  resolution: "All instances conditioned on P=100 including Related Work"
21	  resolution_round: 5
22	
23	- id: "R4-W2"
24	  summary: "Pearson r=0.9698 (n=11) needs Spearman/LOO/bootstrap robustness verification"
25	  category: experiment
26	  severity: critical
27	  status: resolved
28	  first_raised_round: 4
29	  last_seen_round: 5
30	  mentions:
31	    - round: 4
32	      reviewers: [1, 2]
33	      note: "Consensus."
34	    - round: 5
35	      reviewers: [1, 2]
36	      note: "FULLY RESOLVED. R1: 'short paper 典范'."
37	  action_items:
38	    - round: 4
39	      action: "Compute Spearman + bootstrap CI + LOO"
40	      assigned_to: main_agent
41	      status: done
42	  resolution: "Spearman ρ=0.986, bootstrap CI [0.952,0.995], LOO r∈[0.963,0.980]. §3.1 + Appendix C."
43	  resolution_round: 5
44	
45	- id: "R4-W3"
46	  summary: "Router diagnostic needs data-insufficiency caveat (81 train / 14 val episodes)"
47	  category: method
48	  severity: major
49	  status: resolved
50	  first_raised_round: 4
51	  last_seen_round: 5
52	  mentions:
53	    - round: 4
54	      reviewers: [1, 2]
55	      note: "Consensus."
56	    - round: 5
57	      reviewers: [1, 2]
58	      note: "RESOLVED."
59	  action_items:
60	    - round: 4
61	      action: "§3.3 add caveat + cautious wording + majority baseline"
62	      assigned_to: main_agent

…[truncated 6006 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 440 · 2026-05-15T00:14:10.771423+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "simgate-modular-routing",
  "issues_yaml": "- id: \"R4-W1\"\n  summary: \"DAF ~90% headline needs penalty conditioning (P=100) + penalty-independent metric (75/95=78.9%)\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 4\n  last_seen_round: 6\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"Consensus. DAF is monotonically increasing function of P.\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"RESOLVED. Related Work residual fixed via R5-CR1.\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"RECURRED. Previous fix (adding 'under P=100') deemed insufficient. Both reviewers independently demand: (1) DAF(P) function form in main text; (2) DAF range across P values in Abstract/Intro; (3) 78.9% promoted to co-equal headline metric. R2 suggests 78.9% as primary headline.\"\n  action_items:\n    - round: 4\n      action: \"Abstract/Conclusion add 'under P=100'; introduce 75/95=78.9%\"\n      assigned_to: main_agent\n      status: done\n    - round: 6\n      action: \"Rewrite Abstract/Intro/Conclusion to present DAF as P-dependent with range [46%-95%]; elevate 78.9% to co-equal headline; explain DAF(P) function form in §3.3 main text\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-W2\"\n  summary: \"Pearson r=0.9698 (n=11) inferential power limited by small sample and structural coupling\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 6\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"Consensus.\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"FULLY RESOLVED. R1: 'short paper 典范'.\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"RECURRED at warning level. Robustness stats (Spearman/LOO/bootstrap) present but: (1) 'near-perfect' wording needs softening to 'strong'; (2) structural coupling (both vars share P as scaling factor) not acknowledged; (3) n=11 inferential limitation not discussed from statistical power perspective.\"\n  action_items:\n    - round: 4\n      action: \"Compute Spearman + bootstrap CI + LOO\"\n      assigned_to: main_agent\n      status: done\n    - round: 6\n      action: \"Soften 'near-perfect' to 'strong positive correlation'; acknowledge n=11 + structural coupling limitation in main text\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-W3\"\n  summary: \"Router diagnostic needs data-insufficiency caveat (81 train / 14 val episodes)\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 6\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"Consensus.\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"RESOLVED.\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"Partially recurred. R1 suggests k-fold cross-validation. R2 suggests compressing §4.3 instead (divergent—R1 disagrees with compression).\"\n  action_items:\n    - round: 4\n      action: \"§3.3 add caveat + cautious wording + majority baseline\"\n      assigned_to: main_agent\n      status: done\n    - round: 6\n      action: \"Consider k-fold CV if space allows; ensure 'inconclusive diagnostic' framing\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-W4\"\n  summary: \"Single model (Qwen2.5-7B) external validity — model scaling may reduce DAF\"\n  category: experiment\n  severity: major\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 6\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"Consensus.\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"RESOLVED.\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"Not re-raised as independent issue. Limitations section adequately covers model scaling.\"\n  action_items:\n    - round: 4\n      action: \"Limitations add model scaling discussion\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"Limitations discusses stronger models → lower death rates → reduced DAF\"\n  resolution_round: 5\n\n- id: \"R4-W5\"\n  summary: \"Contribution (1) overclaims methodological novelty\"\n  category: framing\n  severity: major\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [2, 1]\n      note: \"R2 critical, R1 minor.\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"RESOLVED.\"\n  action_items:\n    - round: 4\n      action: \"Reframe contribution (1)\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"Reframed to 'identifying step-level oracle degeneracy...diagnosing routing signal composition'\"\n  resolution_round: 5\n\n- id: \"R4-W6\"\n  summary: \"Δ_nd symbol inconsistency (2.84 vs 3.07)\"\n  category: writing\n  severity: minor\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"RESOLVED. No 2.81 exists.\"\n  action_items:\n    - round: 4\n      action: \"Clarify calculation basis\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"All Δ_nd=2.84 consistent; Appendix E 3.07 explained via caption\"\n  resolution_round: 5\n\n- id: \"R4-W7\"\n  summary: \"58.1% vs 59.3% balanced accuracy inconsistency\"\n  category: writing\n  severity: minor\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"FULLY RESOLVED.\"\n  action_items:\n    - round: 4\n      action: \"Unify to 58.1±0.8%\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"Unified to 58.1±0.8% (4-seed mean±std)\"\n  resolution_round: 5\n\n- id: \"R4-W8\"\n  summary: \"ALFWorld Conclusion wording too strong\"\n  category: writing\n  severity: minor\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"FULLY RESOLVED.\"\n  action_items:\n    - round: 4\n      action: \"Specify mechanism difference\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"'catastrophic failure prevention...mechanism varies'\"\n  resolution_round: 5\n\n- id: \"R4-W9\"\n  summary: \"Prescreening scope: 19/30 (63%) excluded — selection bias\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 6\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"Consensus.\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"FULLY RESOLVED.\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"RECURRED. Previous fix (mentioning '11 of 30') too minimal. Need: (1) characterize excluded task types; (2) discuss step budget sensitivity; (3) scope findings as 'tasks where model has baseline competence'.\"\n  action_items:\n    - round: 4\n      action: \"Limitations add prescreening scope\"\n      assigned_to: main_agent\n      status: done\n    - round: 6\n      action: \"Add characterization of excluded tasks + step budget discussion + scope qualifier\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-W10\"\n  summary: \"Reproducibility: missing hyperparameters\"\n  category: format\n  severity: minor\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"FULLY RESOLVED.\"\n  action_items:\n    - round: 4\n      action: \"Appendix hyperparameter table\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"Appendix D Table 4 with full hyperparameters\"\n  resolution_round: 5\n\n- id: \"R5-CR1\"\n  summary: \"Related Work §4 two residual '~90%' without penalty conditioning\"\n  category: writing\n  severity: minor\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"Consensus.\"\n  action_items:\n    - round: 5\n      action: \"Add penalty conditioning to both instances\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"Both instances in related_work.tex now conditioned on P=100\"\n  resolution_round: 5\n\n- id: \"R5-CR3\"\n  summary: \"Intro contribution (2) 'failing to outperform' inconsistent wording\"\n  category: writing\n  severity: minor\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"Consensus.\"\n  action_items:\n    - round: 5\n      action: \"'failing to outperform' → 'does not significantly outperform'\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"introduction.tex updated\"\n  resolution_round: 5\n\n- id: \"R5-CR4\"\n  summary: \"§3.3 accuracy/recall single-seed mixed with 4-seed balanced accuracy\"\n  category: writing\n  severity: minor\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"Consensus. seed 42 best accuracy but worst recall.\"\n  action_items:\n    - round: 5\n      action: \"Replace single-seed with 4-seed ranges\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"Replaced with ranges: accuracy 39.9-65.4%, recall 51.5-81.8%, balanced acc 58.1±0.8% as headline\"\n  resolution_round: 5\n\n- id: \"R6-N1\"\n  summary: \"Missing counterfactual evaluation/explanation in RL literature — method contribution positioning\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [2, 1]\n      note: \"R2 critical (method contribution at risk without contextualization). R1 agrees with nuance: RL counterfactual methods are operationally different (post-hoc explanation vs prospective A/B), but 'counterfactual' in title obligates contextualization. Consensus: add Related Work paragraph distinguishing this work from RL counterfactual literature.\"\n  action_items:\n    - round: 6\n      action: \"Add 'Counterfactual Evaluation in RL' paragraph to Related Work; cite AAAI 2024, AAMAS 2023, AIJ 2021; distinguish prospective paired comparison from post-hoc counterfactual explanation\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-N2\"\n  summary: \"Missing WHY analysis — no failure mode taxonomy, death temporal pattern, or trajectory examples\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [2, 1]\n      note: \"DIVERGENT. R2 marks critical (contribution density too low without WHY). R1 rebuts to should-fix: paper is positioned as decomposition/quantification, not mechanism explanation; DAF's empirical magnitude is non-trivial even if formula is simple. R1 suggests 1-2 sentences on death temporal pattern as bonus. Director assessment: downgrade to warning — paper's contribution framing doesn't promise mechanism explanation, but adding temporal pattern data would meaningfully strengthen the paper.\"\n  action_items:\n    - round: 6\n      action: \"Add 1-2 sentences or appendix paragraph on death episode temporal pattern (which steps deaths occur) and brief failure mode characterization\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W1\"\n  summary: \"Safe RL / agent failure literature coverage insufficient — only Garcia 2015 survey cited\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"Consensus. Need 2024+ safe RL and/or agent failure analysis references.\"\n  action_items:\n    - round: 6\n      action: \"Add 1-2 recent safe RL / agent failure references (constrained MDP, LLM agent failure attribution)\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W2\"\n  summary: \"Deterministic strategy information flow description insufficient in §3.1\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1 raises as potential confound (better observation → better action selection). R2 rebuts confound claim (accurate observation IS the death avoidance mechanism) but agrees §3.1 needs 1-2 sentences of operational detail specifying what LLM sees in each mode.\"\n  action_items:\n    - round: 6\n      action: \"Add 1-2 sentences to §3.1 describing observation format in each strategy mode\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W3\"\n  summary: \"Cross-environment evidence (MATH 50, ALFWorld 135) strength and methodological consistency\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"Consensus. MATH pilot has no CI; ALFWorld mechanism differs (action space pruning vs death avoidance). Evidence placed in Limitations is appropriate but Conclusion references should be more cautious. R2 agrees MATH should have CI if cited in Conclusion.\"\n  action_items:\n    - round: 6\n      action: \"Add CI or effect size for MATH pilot; ensure Conclusion wording matches evidence strength\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W4\"\n  summary: \"find-non-living-thing (n=40, zero deaths, Δ=+9.58) implications insufficiently discussed\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R2 raises as undermining ~90% generalizability claim. R1 agrees with nuance: 90% is correct aggregate decomposition, but per-task DAF is bimodal (find-non-living-thing DAF=0% vs others >90%). Both agree paper should explicitly note this heterogeneity.\"\n  action_items:\n    - round: 6\n      action: \"Add 1 sentence noting bimodal per-task DAF distribution; discuss implications of zero-death task\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W5\"\n  summary: \"Concurrent work (tool-overuse-illusion, tool-use-tax) discussion too shallow\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"Consensus. These concurrent works are highly relevant to the 'failure prevention vs capability routing' reframing. Current one-sentence listing should explain conceptual alignment.\"\n  action_items:\n    - round: 6\n      action: \"Expand concurrent work paragraph to explain how DAF quantifies insights from tool-overuse-illusion and tool-use-tax\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W6\"\n  summary: \"§4.3 Router Training section space allocation — too large for short paper?\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"DIVERGENT. R2 says compress to one paragraph, reallocate to failure mode analysis. R1 rebuts: section provides independent verification (classification head degeneration, 58.1% not trivially derivable from DAF, end-to-end evaluation bridges analysis to practice). Director assessment: R1's argument is stronger — section has independent evidential value. Recommend moderate trimming but not wholesale compression.\"\n  action_items:\n    - round: 6\n      action: \"Consider moderate trimming of §4.3 (e.g., reduce keyword baseline detail) but retain core diagnostic evidence\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-I1\"\n  summary: \"Bib key naming inconsistency (toolformer-2024→2023, retool-2026→2025)\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [2]\n      note: \"Cosmetic but confusing for reviewers checking references.\"\n  action_items:\n    - round: 6\n      action: \"Fix bib keys to match actual publication year\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-I2\"\n  summary: \"Three DAF values (90%, 90.41%, 89.6%) without upfront explanation of calculation basis differences\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"Consensus. First appearance of 89.6% in §3.3 needs immediate footnote explaining calculation basis difference from 90.41%.\"\n  action_items:\n    - round: 6\n      action: \"Add footnote at first 89.6% appearance explaining both-died episode handling\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-I3\"\n  summary: \"Data split paragraph placement (§4.3 end vs before results)\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"Both agree placement is unconventional.\"\n  action_items:\n    - round: 6\n      action: \"Move data split paragraph to beginning of §4 or end of §3\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-I4\"\n  summary: \"Qwen3-1.7B (router) vs Qwen2.5-7B-Instruct (data collection) model choice rationale missing\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"Consensus. Design choice is reasonable but unexplained.\"\n  action_items:\n    - round: 6\n      action: \"Add 1 sentence explaining router model choice rationale\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-I5\"\n  summary: \"vLLM version number missing (reproducibility)\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1]\n      note: \"Minor reproducibility concern.\"\n  action_items:\n    - round: 6\n      action: \"Add vLLM version to experimental setup\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-I6\"\n  summary: \"Table 1 Trained Router score: best seed or 4-seed mean unclear\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"Consensus.\"\n  action_items:\n    - round: 6\n      action: \"Annotate Table 1 Trained Router entry with seed info\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "simgate-modular-routing",
    "issues_yaml": "- id: \"R4-W1\"\n  summary: \"DAF ~90% headline needs penalty conditioning (P=100) + penalty-independent metric (75/95=78.9%)\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 4\n  last_seen_round: 6\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"Consensus. DAF is monotonically increasing function of P.\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"RESOLVED. Related Work residual fixed via R5-CR1.\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"RECURRED. Previous fix (adding 'under P=100') deemed insufficient. Both reviewers independently demand: (1) DAF(P) function form in main text; (2) DAF range across P values in Abstract/Intro; (3) 78.9% promoted to co-equal headline metric. R2 suggests 78.9% as primary headline.\"\n  action_items:\n    - round: 4\n      action: \"Abstract/Conclusion add 'under P=100'; introduce 75/95=78.9%\"\n      assigned_to: main_agent\n      status: done\n    - round: 6\n      action: \"Rewrite Abstract/Intro/Conclusion to present DAF as P-dependent with range [46%-95%]; elevate 78.9% to co-equal headline; explain DAF(P) function form in §3.3 main text\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-W2\"\n  summary: \"Pearson r=0.9698 (n=11) inferential power limited by small sample and structural coupling\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 6\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"Consensus.\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"FULLY RESOLVED. R1: 'short paper 典范'.\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"RECURRED at warning level. Robustness stats (Spearman/LOO/bootstrap) present but: (1) 'near-perfect' wording needs softening to 'strong'; (2) structural coupling (both vars share P as scaling factor) not acknowledged; (3) n=11 inferential limitation not discussed from statistical power perspective.\"\n  action_items:\n    - round: 4\n      action: \"Compute Spearman + bootstrap CI + LOO\"\n      assigned_to: main_agent\n      status: done\n    - round: 6\n      action: \"Soften 'near-perfect' to 'strong positive correlation'; acknowledge n=11 + structural coupling limitation in main text\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-W3\"\n  summary: \"Router diagnostic needs data-insufficiency caveat (81 train / 14 val episodes)\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 6\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"Consensus.\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"RESOLVED.\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"Partially recurred. R1 suggests k-fold cross-validation. R2 suggests compressing §4.3 instead (divergent—R1 disagrees with compression).\"\n  action_items:\n    - round: 4\n      action: \"§3.3 add caveat + cautious wording + majority baseline\"\n      assigned_to: main_agent\n      status: done\n    - round: 6\n      action: \"Consider k-fold CV if space allows; ensure 'inconclusive diagnostic' framing\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-W4\"\n  summary: \"Single model (Qwen2.5-7B) external validity — model scaling may reduce DAF\"\n  category: experiment\n  severity: major\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 6\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"Consensus.\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"RESOLVED.\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"Not re-raised as independent issue. Limitations section adequately covers model scaling.\"\n  action_items:\n    - round: 4\n      action: \"Limitations add model scaling discussion\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"Limitations discusses stronger models → lower death rates → reduced DAF\"\n  resolution_round: 5\n\n- id: \"R4-W5\"\n  summary: \"Contribution (1) overclaims methodological novelty\"\n  category: framing\n  severity: major\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 4\n      reviewers: [2, 1]\n      note: \"R2 critical, R1 minor.\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"RESOLVED.\"\n  action_items:\n    - round: 4\n      action: \"Reframe contribution (1)\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"Reframed to 'identifying step-level oracle degeneracy...diagnosing routing signal composition'\"\n  resolution_round: 5\n\n- id: \"R4-W6\"\n  summary: \"Δ_nd symbol inconsistency (2.84 vs 3.07)\"\n  category: writing\n  severity: minor\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"RESOLVED. No 2.81 exists.\"\n  action_items:\n    - round: 4\n      action: \"Clarify calculation basis\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"All Δ_nd=2.84 consistent; Appendix E 3.07 explained via caption\"\n  resolution_round: 5\n\n- id: \"R4-W7\"\n  summary: \"58.1% vs 59.3% balanced accuracy inconsistency\"\n  category: writing\n  severity: minor\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"FULLY RESOLVED.\"\n  action_items:\n    - round: 4\n      action: \"Unify to 58.1±0.8%\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"Unified to 58.1±0.8% (4-seed mean±std)\"\n  resolution_round: 5\n\n- id: \"R4-W8\"\n  summary: \"ALFWorld Conclusion wording too strong\"\n  category: writing\n  severity: minor\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"FULLY RESOLVED.\"\n  action_items:\n    - round: 4\n      action: \"Specify mechanism difference\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"'catastrophic failure prevention...mechanism varies'\"\n  resolution_round: 5\n\n- id: \"R4-W9\"\n  summary: \"Prescreening scope: 19/30 (63%) excluded — selection bias\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 4\n  last_seen_round: 6\n  mentions:\n    - round: 4\n      reviewers: [1, 2]\n      note: \"Consensus.\"\n    - round: 5\n      reviewers: [1, 2]\n      note: \"FULLY RESOLVED.\"\n    - round: 6\n      reviewers: [1, 2]\n      note: \"RECURRED. Previous fix (mentioning '11 of 30') too minimal. Need: (1) characterize excluded task types; (2) discuss step budget sensitivity; (3) scope findings as 'tasks where model has baseline competence'.\"\n  action_items:\n    - round: 4\n      action: \"Limitations add prescreening scope\"\n      assigned_to: main_agent\n      status: done\n    - round: 6\n      action: \"Add characterization of excluded tasks + step budget discussion + scope qualifier\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R4-W10\"\n  summary: \"Reproducibility: missing hyperparameters\"\n  category: format\n  severity: minor\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"FULLY RESOLVED.\"\n  action_items:\n    - round: 4\n      action: \"Appendix hyperparameter table\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"Appendix D Table 4 with full hyperparameters\"\n  resolution_round: 5\n\n- id: \"R5-CR1\"\n  summary: \"Related Work §4 two residual '~90%' without penalty conditioning\"\n  category: writing\n  severity: minor\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"Consensus.\"\n  action_items:\n    - round: 5\n      action: \"Add penalty conditioning to both instances\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"Both instances in related_work.tex now conditioned on P=100\"\n  resolution_round: 5\n\n- id: \"R5-CR3\"\n  summary: \"Intro contribution (2) 'failing to outperform' inconsistent wording\"\n  category: writing\n  severity: minor\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"Consensus.\"\n  action_items:\n    - round: 5\n      action: \"'failing to outperform' → 'does not significantly outperform'\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"introduction.tex updated\"\n  resolution_round: 5\n\n- id: \"R5-CR4\"\n  summary: \"§3.3 accuracy/recall single-seed mixed with 4-seed balanced accuracy\"\n  category: writing\n  severity: minor\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 5\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n      note: \"Consensus. seed 42 best accuracy but worst recall.\"\n  action_items:\n    - round: 5\n      action: \"Replace single-seed with 4-seed ranges\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"Replaced with ranges: accuracy 39.9-65.4%, recall 51.5-81.8%, balanced acc 58.1±0.8% as headline\"\n  resolution_round: 5\n\n- id: \"R6-N1\"\n  summary: \"Missing counterfactual evaluation/explanation in RL literature — method contribution positioning\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [2, 1]\n      note: \"R2 critical (method contribution at risk without contextualization). R1 agrees with nuance: RL counterfactual methods are operationally different (post-hoc explanation vs prospective A/B), but 'counterfactual' in title obligates contextualization. Consensus: add Related Work paragraph distinguishing this work from RL counterfactual literature.\"\n  action_items:\n    - round: 6\n      action: \"Add 'Counterfactual Evaluation in RL' paragraph to Related Work; cite AAAI 2024, AAMAS 2023, AIJ 2021; distinguish prospective paired comparison from post-hoc counterfactual explanation\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-N2\"\n  summary: \"Missing WHY analysis — no failure mode taxonomy, death temporal pattern, or trajectory examples\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [2, 1]\n      note: \"DIVERGENT. R2 marks critical (contribution density too low without WHY). R1 rebuts to should-fix: paper is positioned as decomposition/quantification, not mechanism explanation; DAF's empirical magnitude is non-trivial even if formula is simple. R1 suggests 1-2 sentences on death temporal pattern as bonus. Director assessment: downgrade to warning — paper's contribution framing doesn't promise mechanism explanation, but adding temporal pattern data would meaningfully strengthen the paper.\"\n  action_items:\n    - round: 6\n      action: \"Add 1-2 sentences or appendix paragraph on death episode temporal pattern (which steps deaths occur) and brief failure mode characterization\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W1\"\n  summary: \"Safe RL / agent failure literature coverage insufficient — only Garcia 2015 survey cited\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"Consensus. Need 2024+ safe RL and/or agent failure analysis references.\"\n  action_items:\n    - round: 6\n      action: \"Add 1-2 recent safe RL / agent failure references (constrained MDP, LLM agent failure attribution)\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W2\"\n  summary: \"Deterministic strategy information flow description insufficient in §3.1\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R1 raises as potential confound (better observation → better action selection). R2 rebuts confound claim (accurate observation IS the death avoidance mechanism) but agrees §3.1 needs 1-2 sentences of operational detail specifying what LLM sees in each mode.\"\n  action_items:\n    - round: 6\n      action: \"Add 1-2 sentences to §3.1 describing observation format in each strategy mode\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W3\"\n  summary: \"Cross-environment evidence (MATH 50, ALFWorld 135) strength and methodological consistency\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"Consensus. MATH pilot has no CI; ALFWorld mechanism differs (action space pruning vs death avoidance). Evidence placed in Limitations is appropriate but Conclusion references should be more cautious. R2 agrees MATH should have CI if cited in Conclusion.\"\n  action_items:\n    - round: 6\n      action: \"Add CI or effect size for MATH pilot; ensure Conclusion wording matches evidence strength\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W4\"\n  summary: \"find-non-living-thing (n=40, zero deaths, Δ=+9.58) implications insufficiently discussed\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"R2 raises as undermining ~90% generalizability claim. R1 agrees with nuance: 90% is correct aggregate decomposition, but per-task DAF is bimodal (find-non-living-thing DAF=0% vs others >90%). Both agree paper should explicitly note this heterogeneity.\"\n  action_items:\n    - round: 6\n      action: \"Add 1 sentence noting bimodal per-task DAF distribution; discuss implications of zero-death task\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W5\"\n  summary: \"Concurrent work (tool-overuse-illusion, tool-use-tax) discussion too shallow\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"Consensus. These concurrent works are highly relevant to the 'failure prevention vs capability routing' reframing. Current one-sentence listing should explain conceptual alignment.\"\n  action_items:\n    - round: 6\n      action: \"Expand concurrent work paragraph to explain how DAF quantifies insights from tool-overuse-illusion and tool-use-tax\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W6\"\n  summary: \"§4.3 Router Training section space allocation — too large for short paper?\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"DIVERGENT. R2 says compress to one paragraph, reallocate to failure mode analysis. R1 rebuts: section provides independent verification (classification head degeneration, 58.1% not trivially derivable from DAF, end-to-end evaluation bridges analysis to practice). Director assessment: R1's argument is stronger — section has independent evidential value. Recommend moderate trimming but not wholesale compression.\"\n  action_items:\n    - round: 6\n      action: \"Consider moderate trimming of §4.3 (e.g., reduce keyword baseline detail) but retain core diagnostic evidence\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-I1\"\n  summary: \"Bib key naming inconsistency (toolformer-2024→2023, retool-2026→2025)\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [2]\n      note: \"Cosmetic but confusing for reviewers checking references.\"\n  action_items:\n    - round: 6\n      action: \"Fix bib keys to match actual publication year\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-I2\"\n  summary: \"Three DAF values (90%, 90.41%, 89.6%) without upfront explanation of calculation basis differences\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"Consensus. First appearance of 89.6% in §3.3 needs immediate footnote explaining calculation basis difference from 90.41%.\"\n  action_items:\n    - round: 6\n      action: \"Add footnote at first 89.6% appearance explaining both-died episode handling\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-I3\"\n  summary: \"Data split paragraph placement (§4.3 end vs before results)\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"Both agree placement is unconventional.\"\n  action_items:\n    - round: 6\n      action: \"Move data split paragraph to beginning of §4 or end of §3\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-I4\"\n  summary: \"Qwen3-1.7B (router) vs Qwen2.5-7B-Instruct (data collection) model choice rationale missing\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"Consensus. Design choice is reasonable but unexplained.\"\n  action_items:\n    - round: 6\n      action: \"Add 1 sentence explaining router model choice rationale\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-I5\"\n  summary: \"vLLM version number missing (reproducibility)\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1]\n      note: \"Minor reproducibility concern.\"\n  action_items:\n    - round: 6\n      action: \"Add vLLM version to experimental setup\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-I6\"\n  summary: \"Table 1 Trained Router score: best seed or 4-seed mean unclear\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"Consensus.\"\n  action_items:\n    - round: 6\n      action: \"Annotate Table 1 Trained Router entry with seed info\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 441 · 2026-05-15T00:14:10.874392+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml\", \"bytes\": 18501}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 442 · 2026-05-15T00:16:27.714118+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "simgate-modular-routing",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "borderline accept",
  "report": "# 审稿报告 — Round 6（Fresh Review）\n\n**论文**: \"Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\"\n**目标**: EMNLP 2026 Findings track | ARR deadline: 2026-05-25\n**Reviewer 编排**: 2 人（R1: 方法严谨性, R2: 新颖性/完整性）\n**外部审稿**: 未启用\n\n---\n\n## Summary\n\n论文提出 episode-level counterfactual analysis 方法诊断模块化 LLM agent 中的 routing signal 组成。在 ScienceWorld 环境中以 Qwen2.5-7B-Instruct 为 backbone，收集 245 个 episode 的 pure-internal 与 pure-deterministic 对照数据，发现在默认 P=100 死亡惩罚下，Death Avoidance Factor (DAF) = 90.41%——即确定性计算的优势约 90% 来自避免 agent 死亡而非正向任务引导。78.9% 的非平局 routing labels 由 death asymmetry 驱动（penalty-independent 指标）。训练的 router 仅达 58.1% balanced accuracy，不显著优于 always-deterministic baseline。\n\n---\n\n## Strengths\n\n1. **实验设计清晰且控制良好**：Pure-internal vs pure-deterministic 的对照设计干净地隔离了变量；episode-level analysis 是对 step-level oracle degeneracy（97.4% tie rate）的合理、well-motivated 回应。[R1, R2 共识]\n\n2. **统计分析深度超出 short paper 平均水平**：Bootstrap CI、Pearson + Spearman 双相关、LOO 逐任务检验、penalty sensitivity analysis、labeling quality audit（Appendix A）——robustness evidence 覆盖面广。[R1 特别肯定: \"short paper 标杆\"]\n\n3. **Limitations 诚实且全面**：主动讨论 single benchmark、penalty dependence、capability-dependent failure mode、cross-environment evidence 局限，未 overclaim。Cross-environment pilots（MATH, ALFWorld）放在 Limitations 而非 Experiments，体现学术诚信。[R1, R2 共识]\n\n4. **有价值的 community reframing**：从 \"when to use tools\"（capability matching）到 \"how to predict/prevent catastrophic failure\"（failure prevention），对 routing/tool-use 研究方向有启发意义。[R1, R2 共识]\n\n5. **可复现性高**（R2 评 4/5）：超参表（Appendix D）、数据划分、环境配置详尽，ScienceWorld + vLLM 均公开可用。\n\n---\n\n## Weaknesses\n\n### Critical（影响接收决定）\n\n**C1. DAF \"~90%\" headline claim 的 penalty-dependence 在主文中 qualification 严重不足** [R1-N1 + R2-N1, 共识]\n\nDAF(P) = δP / (δP + Δ_nd) 是 P 的单调递增函数，lim_{P→∞} DAF = 1。\"~90%\" 仅在 P=100 成立；P=10 时 DAF=46.4%，P=200 时 DAF=94.5%。Abstract、Introduction、Conclusion 反复以 \"~90%\" 为核心 claim，仅加 \"under the default −100 death penalty\" 轻描淡写。78.9% death-asymmetry label fraction 作为 penalty-independent companion metric 被弱化呈现，且与 DAF 度量维度不同（label count vs score gap）却并置，容易误导。\n\n**要求**: (1) Abstract/Introduction 写出 DAF 随 P 变化的区间（如 \"46%–95% across P=10–200\"）；(2) 主文（非仅 Appendix）解释 DAF(P) 函数形式；(3) 将 78.9% 提升为 co-equal headline metric。\n\n**C2. Related Work 缺失 counterfactual evaluation/explanation in RL 关键文献** [R2-N2, R1 同意 with nuance]\n\n论文以 \"counterfactual\" 为标题和核心方法论贡献，但未讨论 RL 领域已有的 counterfactual explanation/evaluation 方法（Explaining RL Agents through Counterfactual Action Outcomes, AAAI 2024; Counterfactual Explanations for RL Agents, AAMAS 2023; Counterfactual state explanations for RL, AIJ 2021; off-policy evaluation 方法族）。论文的方法与这些工作操作上不同（prospective paired comparison vs post-hoc explanation），但 \"counterfactual\" 一词在标题中出现就有义务 contextualize。\n\n**要求**: 增加 \"Counterfactual Evaluation in RL\" 段落，精确区分本文的 prospective A/B comparison 与 post-hoc counterfactual explanation。\n\n### Warning（影响评分但不一票否决）\n\n**W1. n=11 数据点的 Pearson r \"near-perfect correlation\" 声明 inferential power 有限** [R1-N2, R2 同意]\n\nn=11, df=9。LOO 和 bootstrap 缓解 outlier concern，但不解决 structural coupling 问题：death rate differential 和 Δ_full 通过同一个 P 线性耦合，高 r 部分是数学结构产物。R2 补充指出 permutation test 也不解决此问题。\n\n**建议**: 弱化 \"near-perfect\" 为 \"strong positive correlation\"；正文承认 n=11 + structural coupling 局限。\n\n**W2. Prescreening 排除 19/30 (63%) task types 的选择偏差未充分讨论** [R1-W1 + R2-W2, 共识]\n\n排除标准合理（both strategies timeout），但 findings 仅适用于模型有基本能力的 task types。被排除 task types 的共同特征（更难？action space 更大？）未分析。增加 step budget 可能改变结论（方向不确定）。\n\n**建议**: (1) 明确 scope qualifier；(2) 简述被排除 task types 特征；(3) 讨论 step budget 敏感性。\n\n**W3. 缺少 failure mode 分析（WHY death avoidance dominates）** [R2-N3 critical, R1 rebut to should-fix; **分歧点**]\n\n论文建立了 WHAT（death avoidance accounts for ~90%）但未分析 WHY（internal strategy 42.9% death rate 的 failure mode 分类、death 的 temporal pattern、trajectory 示例）。\n\nR2 认为 critical：contribution density 不足，finding 在已知 penalty=-100 + death rate 2.6× 后近乎算术推导。R1 反驳：论文定位是 decomposition/quantification 而非 mechanism explanation；death rate differential 的经验量级非先验可知，是真正的 empirical contribution。\n\n**Director 判断**: 降为 warning。论文贡献定位不承诺 mechanism explanation，但添加 death temporal pattern 数据（1-2 句或 appendix）会显著提升 insight 密度。\n\n**W4. Deterministic strategy 信息流操作化描述不足** [R1-W3, R2 rebut confound claim but agrees description issue]\n\n§3.1 \"replaces only the state-transition prediction\" 不够精确——读者不知 LLM 在两种 mode 下分别看到什么 observation。R2 clarified: \"better informed action selection\" 是 death avoidance 的实现机制而非独立混淆变量（accurate state → fewer hallucination-induced deaths），但同意操作化描述需加 1-2 句。\n\n**W5. Cross-environment evidence (MATH 50, ALFWorld 135) 力度不足** [R1-W4, R2 同意]\n\nMATH pilot 仅 50 题、无 CI；ALFWorld mechanism 不同（action space pruning vs death avoidance）。若 Conclusion 引用这些证据，至少应为 MATH 报告 CI。\n\n**W6. find-non-living-thing (n=40, zero deaths, Δ=+9.58) 的 implications 讨论不充分** [R2-W4, R1 同意 with nuance]\n\n该 task type 的 per-task DAF=0%（routing signal 完全来自 non-death 因素），与其他 10 个 task types 的 DAF>90% 构成 bimodal 分布。论文虽在 §4.1 提及，但未显式指出这种 heterogeneity。\n\n**W7. Concurrent work 讨论深度不足** [R2-W5, R1 同意]\n\ntool-overuse-illusion 和 tool-use-tax 与本文 \"failure prevention vs capability routing\" reframing 高度互补，目前仅 one-sentence listing。\n\n**W8. Safe RL 文献覆盖不足** [R2-W1, R1 同意]\n\n仅引 Garcia & Fernandez 2015 综述。需 2024+ safe RL 或 agent failure analysis 参考文献。\n\n### Info（不影响接收）\n\n- **I1**: Bib key 命名与年份不一致（toolformer-2024→2023, retool-2026→2025）\n- **I2**: 三个 DAF 数值（~90%, 90.41%, 89.6%）首次出现时未注明计算口径差异\n- **I3**: Data split 段位于 §4.3 末尾，位置不常规\n- **I4**: Qwen3-1.7B (router) vs Qwen2.5-7B-Instruct (data) 模型选择原因未解释\n- **I5**: vLLM 版本号未注明（可复现性）\n- **I6**: Table 1 \"Trained Router\" −10.70 未标注是 best seed 还是 4-seed mean\n- **I7**: DAF edge case（Δ_nd < 0 时 DAF > 1）可加脚注说明语义 [R1-W5, R2 降为 info]\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **DAF penalty-dependence 是论文最核心的 presentation 问题**——\"~90%\" 不是 routing signal 的内在属性而是 penalty 选择的产物，需要 reframe [C1, 两位独立发现]\n2. **Prescreening 选择偏差需要更透明的讨论** [W2]\n3. **Cross-environment evidence 力度有限，但放在 Limitations 的处理是正确的** [W5]\n4. **统计分析质量是论文的显著优势** [Strengths]\n5. **Limitations section 的诚实度是加分项** [Strengths]\n6. **78.9% penalty-independent metric 应被提升**——两位 reviewer 独立建议 [C1]\n7. **Counterfactual-in-RL 文献缺失是真实 gap**，但补充后不会削弱 contribution [C2]\n\n## Reviewer Divergence [REBUT]\n\n1. **R2-N3 severity（failure mode analysis）**: R2 标 critical（contribution density 不足），R1 标 should-fix（论文定位是 decomposition 不是 mechanism explanation）。**Director 采纳 R1 立场**——论文的贡献承诺不包含 mechanism explanation，但 temporal pattern 数据作为 bonus 会加分。\n\n2. **§4.3 Router section 空间分配**: R2 建议大幅压缩为一段，R1 反对（该 section 提供 classification head degeneration 作为独立验证、58.1% 不 trivially derivable from DAF、end-to-end evaluation 是 analysis-to-practice 桥梁）。**Director 采纳 R1 立场**——section 有独立证据价值，但可适度修剪 keyword baseline 细节。\n\n3. **R1-W3 deterministic confound vs R2 rebut**: R1 担忧 \"better informed action selection\" 是独立混淆变量；R2 论证它就是 death avoidance 的实现机制。**Director 采纳 R2 立场**——不是独立混淆变量，但 §3.1 操作化描述确实需要补充。\n\n---\n\n## Questions for Authors\n\n1. 如果将 headline metric 从 DAF 改为 78.9% death-asymmetry fraction（或 dual reporting），核心 narrative 是否需要调整？\n2. 105 个 internal 死亡 episode 中，死亡发生在第几步？是否集中在特定 action pattern（如温度操作、容器交互）？\n3. find-non-living-thing 的 Δ=+9.58 来自什么具体的 non-death advantage（state tracking accuracy? action coverage?）？\n4. 被排除的 19 个 task types 是否有共同特征（action space complexity? 需要更多步数? 需要特定 domain knowledge?）？\n5. Router training 用 Qwen3-1.7B 而非 Qwen2.5-7B-Instruct，这一 model mismatch 的设计理由是什么？\n6. 如果将 step budget 从 30 增加到 100，被排除的 19 个 task types 中有多少可能产生 non-trivial counterfactual signal？这是否可能改变 DAF 估计？\n\n---\n\n## Missing References\n\n| 文献 | 原因 | 来源 |\n|------|------|------|\n| Explaining RL Agents through Counterfactual Action Outcomes (AAAI 2024) | 需定位 counterfactual method 贡献 | R2 |\n| Counterfactual Explanations for RL Agents (AAMAS 2023) | 同上 | R2 |\n| Counterfactual state explanations for RL (AIJ 2021) | 同上 | R2 |\n| A Survey of Safe RL and Constrained MDPs (2025) | 论文连接 safe RL 但覆盖不足 | R2 |\n| Which Agent Causes Task Failures and When? (ICML 2025) | Agent failure attribution 直接相关 | R2 |\n| How Do LLMs Fail In Agentic Scenarios? (arXiv:2512.07497) | LLM agent failure mode 分类 | R2 |\n| Constrained MDP / safe exploration (CPO, LAMBDA) | Safe RL 方法论 | R1 |\n\n---\n\n## Overall Assessment\n\n**Score: Borderline Accept（适合 Findings track，需修改）**\n\n**R1**: 3.5/5 (Soundness 4/5, Excitement 3/5)\n**R2**: 3.0/5 (Soundness 3/5, Excitement 2/5)\n**Consolidated**: 3.25/5\n\n**Confidence**: 4/5（两位 reviewer 均表示高信心）\n\n**理由**: 论文有真实且有价值的 empirical contribution——定量分解 routing signal 并发现 death avoidance 的主导地位，统计分析质量高，实验设计严谨。主要问题集中在 presentation（DAF headline 的 penalty-dependence 需要更显式 qualification）和 positioning（缺失 counterfactual-in-RL 文献），这些都是可修复的。核心 finding 的 surprising 程度中等（R2 concern），但 R1 正确指出 death rate differential 的经验量级非先验可知。对 Findings track 而言，soundness + reproducibility + honest limitations 足以达到 acceptance bar，前提是 C1 和 C2 得到修复。\n\n**修改优先级**:\n1. [必做] C1: DAF penalty-dependence reframe + 78.9% 提升\n2. [必做] C2: 增加 counterfactual-in-RL 文献段落\n3. [强烈建议] W1: 弱化 \"near-perfect\" 措辞\n4. [强烈建议] W2: 扩展 prescreening 讨论\n5. [建议] W3-W8: 按优先级逐步改善\n\n---\n\n## Detailed Comments\n\n### Abstract\n- \"approximately 90% of the routing signal\" → 需同时提及 penalty-independent 78.9% 和 DAF 的 P-dependence 区间\n- \"Death Avoidance Factor\" 首次出现即应暗示其 penalty-dependent 性质\n\n### §1 Introduction\n- 第 7 段 contribution (1) \"identifying step-level oracle degeneracy and applying episode-level counterfactual analysis\" → 需在 Related Work 中 contextualize against RL counterfactual literature\n- 推荐 dual reporting: \"78.9% of non-tie routing labels are driven by death asymmetry (penalty-independent); under the default P=100 death penalty, this translates to a Death Avoidance Factor of 90.41%\"\n\n### §3.1 Method - Counterfactual Episode Collection\n- \"deterministic computation replaces only the state-transition prediction, not action selection\" → 补充操作化描述：in deterministic mode, LLM receives ground-truth environment observation string; in internal mode, LLM generates own prediction of next observation\n\n### §3.3 Death Avoidance Factor\n- DAF(P) 函数形式应在此出现（目前仅在 Appendix E）\n- 首次出现 89.6% 时即时注明与 90.41% 的计算口径差异\n- 考虑加脚注讨论 DAF > 1 的 edge case 语义\n\n### §4.1 Death Avoidance Decomposition\n- \"near-perfect cross-task correlation (r = 0.9698)\" → \"strong positive cross-task correlation (r = 0.97, n = 11)\"\n- 补充 1 句 structural coupling caveat\n- 指出 per-task DAF 的 bimodal 分布（find-non-living-thing DAF=0% vs others >90%）\n\n### §4.3 Router Training as Diagnostic\n- 可适度精简 keyword baseline 细节，释放少量空间\n- Table 1 Trained Router 标注 seed 信息\n- Data split 段建议前移\n\n### §5 Related Work\n- 增加 \"Counterfactual Evaluation in RL\" 段落 [C2]\n- 增加 1-2 篇 2024+ safe RL / agent failure 文献 [W8]\n- 扩展 concurrent work 讨论深度 [W7]\n\n### Limitations\n- 扩展 prescreening 讨论：被排除 task types 特征、step budget 敏感性 [W2]\n- Death temporal pattern 数据（可选 appendix）[W3]\n- MATH pilot 加 CI [W5]\n\n### Format\n- 修正 bib key 年份 [I1]\n- 补充 vLLM 版本号 [I5]\n- Router model choice rationale [I4]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "simgate-modular-routing",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "borderline accept",
    "report": "# 审稿报告 — Round 6（Fresh Review）\n\n**论文**: \"Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\"\n**目标**: EMNLP 2026 Findings track | ARR deadline: 2026-05-25\n**Reviewer 编排**: 2 人（R1: 方法严谨性, R2: 新颖性/完整性）\n**外部审稿**: 未启用\n\n---\n\n## Summary\n\n论文提出 episode-level counterfactual analysis 方法诊断模块化 LLM agent 中的 routing signal 组成。在 ScienceWorld 环境中以 Qwen2.5-7B-Instruct 为 backbone，收集 245 个 episode 的 pure-internal 与 pure-deterministic 对照数据，发现在默认 P=100 死亡惩罚下，Death Avoidance Factor (DAF) = 90.41%——即确定性计算的优势约 90% 来自避免 agent 死亡而非正向任务引导。78.9% 的非平局 routing labels 由 death asymmetry 驱动（penalty-independent 指标）。训练的 router 仅达 58.1% balanced accuracy，不显著优于 always-deterministic baseline。\n\n---\n\n## Strengths\n\n1. **实验设计清晰且控制良好**：Pure-internal vs pure-deterministic 的对照设计干净地隔离了变量；episode-level analysis 是对 step-level oracle degeneracy（97.4% tie rate）的合理、well-motivated 回应。[R1, R2 共识]\n\n2. **统计分析深度超出 short paper 平均水平**：Bootstrap CI、Pearson + Spearman 双相关、LOO 逐任务检验、penalty sensitivity analysis、labeling quality audit（Appendix A）——robustness evidence 覆盖面广。[R1 特别肯定: \"short paper 标杆\"]\n\n3. **Limitations 诚实且全面**：主动讨论 single benchmark、penalty dependence、capability-dependent failure mode、cross-environment evidence 局限，未 overclaim。Cross-environment pilots（MATH, ALFWorld）放在 Limitations 而非 Experiments，体现学术诚信。[R1, R2 共识]\n\n4. **有价值的 community reframing**：从 \"when to use tools\"（capability matching）到 \"how to predict/prevent catastrophic failure\"（failure prevention），对 routing/tool-use 研究方向有启发意义。[R1, R2 共识]\n\n5. **可复现性高**（R2 评 4/5）：超参表（Appendix D）、数据划分、环境配置详尽，ScienceWorld + vLLM 均公开可用。\n\n---\n\n## Weaknesses\n\n### Critical（影响接收决定）\n\n**C1. DAF \"~90%\" headline claim 的 penalty-dependence 在主文中 qualification 严重不足** [R1-N1 + R2-N1, 共识]\n\nDAF(P) = δP / (δP + Δ_nd) 是 P 的单调递增函数，lim_{P→∞} DAF = 1。\"~90%\" 仅在 P=100 成立；P=10 时 DAF=46.4%，P=200 时 DAF=94.5%。Abstract、Introduction、Conclusion 反复以 \"~90%\" 为核心 claim，仅加 \"under the default −100 death penalty\" 轻描淡写。78.9% death-asymmetry label fraction 作为 penalty-independent companion metric 被弱化呈现，且与 DAF 度量维度不同（label count vs score gap）却并置，容易误导。\n\n**要求**: (1) Abstract/Introduction 写出 DAF 随 P 变化的区间（如 \"46%–95% across P=10–200\"）；(2) 主文（非仅 Appendix）解释 DAF(P) 函数形式；(3) 将 78.9% 提升为 co-equal headline metric。\n\n**C2. Related Work 缺失 counterfactual evaluation/explanation in RL 关键文献** [R2-N2, R1 同意 with nuance]\n\n论文以 \"counterfactual\" 为标题和核心方法论贡献，但未讨论 RL 领域已有的 counterfactual explanation/evaluation 方法（Explaining RL Agents through Counterfactual Action Outcomes, AAAI 2024; Counterfactual Explanations for RL Agents, AAMAS 2023; Counterfactual state explanations for RL, AIJ 2021; off-policy evaluation 方法族）。论文的方法与这些工作操作上不同（prospective paired comparison vs post-hoc explanation），但 \"counterfactual\" 一词在标题中出现就有义务 contextualize。\n\n**要求**: 增加 \"Counterfactual Evaluation in RL\" 段落，精确区分本文的 prospective A/B comparison 与 post-hoc counterfactual explanation。\n\n### Warning（影响评分但不一票否决）\n\n**W1. n=11 数据点的 Pearson r \"near-perfect correlation\" 声明 inferential power 有限** [R1-N2, R2 同意]\n\nn=11, df=9。LOO 和 bootstrap 缓解 outlier concern，但不解决 structural coupling 问题：death rate differential 和 Δ_full 通过同一个 P 线性耦合，高 r 部分是数学结构产物。R2 补充指出 permutation test 也不解决此问题。\n\n**建议**: 弱化 \"near-perfect\" 为 \"strong positive correlation\"；正文承认 n=11 + structural coupling 局限。\n\n**W2. Prescreening 排除 19/30 (63%) task types 的选择偏差未充分讨论** [R1-W1 + R2-W2, 共识]\n\n排除标准合理（both strategies timeout），但 findings 仅适用于模型有基本能力的 task types。被排除 task types 的共同特征（更难？action space 更大？）未分析。增加 step budget 可能改变结论（方向不确定）。\n\n**建议**: (1) 明确 scope qualifier；(2) 简述被排除 task types 特征；(3) 讨论 step budget 敏感性。\n\n**W3. 缺少 failure mode 分析（WHY death avoidance dominates）** [R2-N3 critical, R1 rebut to should-fix; **分歧点**]\n\n论文建立了 WHAT（death avoidance accounts for ~90%）但未分析 WHY（internal strategy 42.9% death rate 的 failure mode 分类、death 的 temporal pattern、trajectory 示例）。\n\nR2 认为 critical：contribution density 不足，finding 在已知 penalty=-100 + death rate 2.6× 后近乎算术推导。R1 反驳：论文定位是 decomposition/quantification 而非 mechanism explanation；death rate differential 的经验量级非先验可知，是真正的 empirical contribution。\n\n**Director 判断**: 降为 warning。论文贡献定位不承诺 mechanism explanation，但添加 death temporal pattern 数据（1-2 句或 appendix）会显著提升 insight 密度。\n\n**W4. Deterministic strategy 信息流操作化描述不足** [R1-W3, R2 rebut confound claim but agrees description issue]\n\n§3.1 \"replaces only the state-transition prediction\" 不够精确——读者不知 LLM 在两种 mode 下分别看到什么 observation。R2 clarified: \"better informed action selection\" 是 death avoidance 的实现机制而非独立混淆变量（accurate state → fewer hallucination-induced deaths），但同意操作化描述需加 1-2 句。\n\n**W5. Cross-environment evidence (MATH 50, ALFWorld 135) 力度不足** [R1-W4, R2 同意]\n\nMATH pilot 仅 50 题、无 CI；ALFWorld mechanism 不同（action space pruning vs death avoidance）。若 Conclusion 引用这些证据，至少应为 MATH 报告 CI。\n\n**W6. find-non-living-thing (n=40, zero deaths, Δ=+9.58) 的 implications 讨论不充分** [R2-W4, R1 同意 with nuance]\n\n该 task type 的 per-task DAF=0%（routing signal 完全来自 non-death 因素），与其他 10 个 task types 的 DAF>90% 构成 bimodal 分布。论文虽在 §4.1 提及，但未显式指出这种 heterogeneity。\n\n**W7. Concurrent work 讨论深度不足** [R2-W5, R1 同意]\n\ntool-overuse-illusion 和 tool-use-tax 与本文 \"failure prevention vs capability routing\" reframing 高度互补，目前仅 one-sentence listing。\n\n**W8. Safe RL 文献覆盖不足** [R2-W1, R1 同意]\n\n仅引 Garcia & Fernandez 2015 综述。需 2024+ safe RL 或 agent failure analysis 参考文献。\n\n### Info（不影响接收）\n\n- **I1**: Bib key 命名与年份不一致（toolformer-2024→2023, retool-2026→2025）\n- **I2**: 三个 DAF 数值（~90%, 90.41%, 89.6%）首次出现时未注明计算口径差异\n- **I3**: Data split 段位于 §4.3 末尾，位置不常规\n- **I4**: Qwen3-1.7B (router) vs Qwen2.5-7B-Instruct (data) 模型选择原因未解释\n- **I5**: vLLM 版本号未注明（可复现性）\n- **I6**: Table 1 \"Trained Router\" −10.70 未标注是 best seed 还是 4-seed mean\n- **I7**: DAF edge case（Δ_nd < 0 时 DAF > 1）可加脚注说明语义 [R1-W5, R2 降为 info]\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **DAF penalty-dependence 是论文最核心的 presentation 问题**——\"~90%\" 不是 routing signal 的内在属性而是 penalty 选择的产物，需要 reframe [C1, 两位独立发现]\n2. **Prescreening 选择偏差需要更透明的讨论** [W2]\n3. **Cross-environment evidence 力度有限，但放在 Limitations 的处理是正确的** [W5]\n4. **统计分析质量是论文的显著优势** [Strengths]\n5. **Limitations section 的诚实度是加分项** [Strengths]\n6. **78.9% penalty-independent metric 应被提升**——两位 reviewer 独立建议 [C1]\n7. **Counterfactual-in-RL 文献缺失是真实 gap**，但补充后不会削弱 contribution [C2]\n\n## Reviewer Divergence [REBUT]\n\n1. **R2-N3 severity（failure mode analysis）**: R2 标 critical（contribution density 不足），R1 标 should-fix（论文定位是 decomposition 不是 mechanism explanation）。**Director 采纳 R1 立场**——论文的贡献承诺不包含 mechanism explanation，但 temporal pattern 数据作为 bonus 会加分。\n\n2. **§4.3 Router section 空间分配**: R2 建议大幅压缩为一段，R1 反对（该 section 提供 classification head degeneration 作为独立验证、58.1% 不 trivially derivable from DAF、end-to-end evaluation 是 analysis-to-practice 桥梁）。**Director 采纳 R1 立场**——section 有独立证据价值，但可适度修剪 keyword baseline 细节。\n\n3. **R1-W3 deterministic confound vs R2 rebut**: R1 担忧 \"better informed action selection\" 是独立混淆变量；R2 论证它就是 death avoidance 的实现机制。**Director 采纳 R2 立场**——不是独立混淆变量，但 §3.1 操作化描述确实需要补充。\n\n---\n\n## Questions for Authors\n\n1. 如果将 headline metric 从 DAF 改为 78.9% death-asymmetry fraction（或 dual reporting），核心 narrative 是否需要调整？\n2. 105 个 internal 死亡 episode 中，死亡发生在第几步？是否集中在特定 action pattern（如温度操作、容器交互）？\n3. find-non-living-thing 的 Δ=+9.58 来自什么具体的 non-death advantage（state tracking accuracy? action coverage?）？\n4. 被排除的 19 个 task types 是否有共同特征（action space complexity? 需要更多步数? 需要特定 domain knowledge?）？\n5. Router training 用 Qwen3-1.7B 而非 Qwen2.5-7B-Instruct，这一 model mismatch 的设计理由是什么？\n6. 如果将 step budget 从 30 增加到 100，被排除的 19 个 task types 中有多少可能产生 non-trivial counterfactual signal？这是否可能改变 DAF 估计？\n\n---\n\n## Missing References\n\n| 文献 | 原因 | 来源 |\n|------|------|------|\n| Explaining RL Agents through Counterfactual Action Outcomes (AAAI 2024) | 需定位 counterfactual method 贡献 | R2 |\n| Counterfactual Explanations for RL Agents (AAMAS 2023) | 同上 | R2 |\n| Counterfactual state explanations for RL (AIJ 2021) | 同上 | R2 |\n| A Survey of Safe RL and Constrained MDPs (2025) | 论文连接 safe RL 但覆盖不足 | R2 |\n| Which Agent Causes Task Failures and When? (ICML 2025) | Agent failure attribution 直接相关 | R2 |\n| How Do LLMs Fail In Agentic Scenarios? (arXiv:2512.07497) | LLM agent failure mode 分类 | R2 |\n| Constrained MDP / safe exploration (CPO, LAMBDA) | Safe RL 方法论 | R1 |\n\n---\n\n## Overall Assessment\n\n**Score: Borderline Accept（适合 Findings track，需修改）**\n\n**R1**: 3.5/5 (Soundness 4/5, Excitement 3/5)\n**R2**: 3.0/5 (Soundness 3/5, Excitement 2/5)\n**Consolidated**: 3.25/5\n\n**Confidence**: 4/5（两位 reviewer 均表示高信心）\n\n**理由**: 论文有真实且有价值的 empirical contribution——定量分解 routing signal 并发现 death avoidance 的主导地位，统计分析质量高，实验设计严谨。主要问题集中在 presentation（DAF headline 的 penalty-dependence 需要更显式 qualification）和 positioning（缺失 counterfactual-in-RL 文献），这些都是可修复的。核心 finding 的 surprising 程度中等（R2 concern），但 R1 正确指出 death rate differential 的经验量级非先验可知。对 Findings track 而言，soundness + reproducibility + honest limitations 足以达到 acceptance bar，前提是 C1 和 C2 得到修复。\n\n**修改优先级**:\n1. [必做] C1: DAF penalty-dependence reframe + 78.9% 提升\n2. [必做] C2: 增加 counterfactual-in-RL 文献段落\n3. [强烈建议] W1: 弱化 \"near-perfect\" 措辞\n4. [强烈建议] W2: 扩展 prescreening 讨论\n5. [建议] W3-W8: 按优先级逐步改善\n\n---\n\n## Detailed Comments\n\n### Abstract\n- \"approximately 90% of the routing signal\" → 需同时提及 penalty-independent 78.9% 和 DAF 的 P-dependence 区间\n- \"Death Avoidance Factor\" 首次出现即应暗示其 penalty-dependent 性质\n\n### §1 Introduction\n- 第 7 段 contribution (1) \"identifying step-level oracle degeneracy and applying episode-level counterfactual analysis\" → 需在 Related Work 中 contextualize against RL counterfactual literature\n- 推荐 dual reporting: \"78.9% of non-tie routing labels are driven by death asymmetry (penalty-independent); under the default P=100 death penalty, this translates to a Death Avoidance Factor of 90.41%\"\n\n### §3.1 Method - Counterfactual Episode Collection\n- \"deterministic computation replaces only the state-transition prediction, not action selection\" → 补充操作化描述：in deterministic mode, LLM receives ground-truth environment observation string; in internal mode, LLM generates own prediction of next observation\n\n### §3.3 Death Avoidance Factor\n- DAF(P) 函数形式应在此出现（目前仅在 Appendix E）\n- 首次出现 89.6% 时即时注明与 90.41% 的计算口径差异\n- 考虑加脚注讨论 DAF > 1 的 edge case 语义\n\n### §4.1 Death Avoidance Decomposition\n- \"near-perfect cross-task correlation (r = 0.9698)\" → \"strong positive cross-task correlation (r = 0.97, n = 11)\"\n- 补充 1 句 structural coupling caveat\n- 指出 per-task DAF 的 bimodal 分布（find-non-living-thing DAF=0% vs others >90%）\n\n### §4.3 Router Training as Diagnostic\n- 可适度精简 keyword baseline 细节，释放少量空间\n- Table 1 Trained Router 标注 seed 信息\n- Data split 段建议前移\n\n### §5 Related Work\n- 增加 \"Counterfactual Evaluation in RL\" 段落 [C2]\n- 增加 1-2 篇 2024+ safe RL / agent failure 文献 [W8]\n- 扩展 concurrent work 讨论深度 [W7]\n\n### Limitations\n- 扩展 prescreening 讨论：被排除 task types 特征、step budget 敏感性 [W2]\n- Death temporal pattern 数据（可选 appendix）[W3]\n- MATH pilot 加 CI [W5]\n\n### Format\n- 修正 bib key 年份 [I1]\n- 补充 vLLM 版本号 [I5]\n- Router model choice rationale [I4]"
  }
}
```

</details>

---


### Tool result

_source line 443 · 2026-05-15T00:16:31.784501+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_f6bffc7e8351600df8091f08a63cd5a0:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4070
}
```

</details>

---


### Assistant

_source line 444 · 2026-05-15T00:16:43.770375+00:00_

审稿报告已投递。

---

**📋 Round 6 审稿完成总结**

| 项目 | 内容 |
|------|------|
| **综合评分** | Borderline Accept（3.25/5） |
| **R1 评分** | 3.5/5（Soundness 4/5, Excitement 3/5） |
| **R2 评分** | 3.0/5（Soundness 3/5, Excitement 2/5） |
| **Critical 问题** | 2 个：(1) DAF "~90%" 对 penalty magnitude 依赖 qualification 不足；(2) 缺失 counterfactual-in-RL 文献 |
| **Warning 问题** | 8 个：n=11 inferential power、prescreening bias、failure mode analysis 缺失、deterministic strategy 描述、cross-env evidence、find-non-living-thing implications、concurrent work 深度、safe RL 文献 |
| **Info 问题** | 7 个：bib keys、DAF 三值混淆、data split 位置、model choice rationale、vLLM 版本、Table 1 seed 标注、DAF edge case |
| **主要分歧** | R2-N3（failure mode analysis）severity：R2 critical → Director 降为 warning；§4.3 压缩：R2 主张 → Director 采纳 R1 保留立场 |
| **Issue Tracker** | 已更新：3 个旧 issue 复发（R4-W1/W2/W9），12 个新 issue |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 48

## Round 48

98 recorded events


### User

_source line 445 · 2026-05-15T15:17:21.395367+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: simgate-modular-routing
- 论文路径: projects/simgate-modular-routing/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- Track: main conference
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 446 · 2026-05-15T15:17:29.113140+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 447 · 2026-05-15T15:17:29.115120+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 2458 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 1
}
```

</details>

---


### Tool call

_source line 448 · 2026-05-15T15:17:32.242733+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 449 · 2026-05-15T15:17:32.293485+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 450 · 2026-05-15T15:17:36.923338+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "simgate-modular-routing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "simgate-modular-routing"
  }
}
```

</details>

---


### Tool result

_source line 451 · 2026-05-15T15:17:37.878623+00:00_

{"result":"# 项目 simgate-modular-routing 概况\n\n## 实验状态 (68 个)\n\n- **plan-001b-gpu1-extra**: DONE (failed) — \n- **plan-001b-gpu1**: DONE (success) — \n- **plan-001b-gpu0-v2**: DONE (failed) — \n- **plan-011-rule-based**: DONE (success) — \n- **plan-001b-gpu0**: DONE (failed) — \n- **research-prescreening-gpu0**: DONE (killed) — \n- **research-prescreening-gpu1**: DONE (success) — \n- **research-boil-v3-gpu1**: DONE (success) — \n- **mvp-p1-gpu1-v3**: DONE (success) — \n- **mvp-p1-gpu0-vllm**: DONE (success) — \n- **mvp-p1-gpu0**: DONE (killed) — \n- **mvp-p1-gpu1-v2**: DONE (killed) — \n- **mvp-p1-gpu1-vllm**: DONE (killed) — \n- **mvp-p1-gpu1**: DONE (killed) — \n- **mvp-p0-forking**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-15\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| plan-006-deep-internal | 2-way vs 3-way routing ablation Phase 1: 收集 deep-internal (CoT/thinking mode) 轨迹，5-6 个 high-signal tasks × 20 episodes。与已有 fast-internal/deterministic 配对，为 3-way router 训练提供数据。如果 deep-internal 分数显著高于 fast-internal → 3-way routing 有价值；如果差异小 → 2-way suffices。 | — | — | — |\n\n## 待处理\n（无）\n\n## 近期结论\n- **plan-008-router-size-v3** (success): Router size ablation v3 (C2): 直接用原始 implicit_router_sft.py（seed-robustness 验证过），只改 --model_name。Qwen3-0.6B / 1.7B (sanity check) / 4B。不写新 wrapper，不改代码。1.7B 应复现 ~0.554-0.576。 ← 基于 plan-008-router-size-v2\n  [plan-008-v3-training-logs](/api/workspace-files/projects/simgate-modular-routing/artifacts/plan-008-router-size-v3/data/plan008_v3_results.md)\n- **plan-008-router-size-v2** (failed): Router size ablation v2 (C2 lightweight claim): Qwen3 同家族对比 0.6B / 1.7B / 4B。修复 v1 的 3 个 bug：生成式评估（非 logit argmax）、同家族模型（非混合 Qwen2.5/3）、episode-level stratified split（与 seed-robustness 一致）。 ← 基于 plan-008-router-size\n- **plan-008-router-size** (failed): Router size ablation (C2 lightweight claim): 对比 Qwen3-1.7B vs Qwen2.5-1.5B vs Qwen2.5-3B 作为 router，相同训练数据和配置。如果 1
…[truncated 1212 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 452 · 2026-05-15T15:17:38.380706+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 453 · 2026-05-15T15:17:38.783025+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\graphicspath{{figures/}}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{algorithm}
16	\usepackage{algorithmic}
17	
18	\title{Death Avoidance as the Dominant Routing Signal:\\A Counterfactual Analysis on ScienceWorld}
19	
20	\author{Anonymous}
21	
22	\begin{document}
23	\maketitle
24	
25	\input{abstract}
26	\input{introduction}
27	\input{method}
28	\input{experiments}
29	\input{related_work}
30	\input{discussion}
31	\input{conclusion}
32	
33	\section*{Limitations}
34	
35	Our analysis uses a single benchmark (ScienceWorld) with a single LLM backbone (Qwen2.5-7B-Instruct), and generalization to other interactive environments and model scales remains to be established. A preliminary cross-model pilot with Llama-3.1-8B-Instruct ($N{=}10$ episode pairs, 2 task types) shows directionally consistent death patterns (\S\ref{sec:cross-model}), but full-scale multi-model validation remains future work. The $-100$ death penalty may amplify DAF; environments with less catastrophic penalties could exhibit lower DAF, though the qualitative finding may still hold. On the 135 episodes (55.1\%) where neither strategy leads to catastrophic failure, deterministic computation retains a small advantage ($\Delta_{\text{nd}} = +2.84$), indicating non-zero routing signal beyond death avoidance. Our analysis covers 11 of 30 ScienceWorld task types; the remaining 19 (63\%) were excluded during prescreening because both strategies timed out on all seed variations within the 30-step budget, providing no counterfactual signal. These tasks likely require longer-horizon planning; increasing the step budget could surface additional routing signal whose composition may differ from the death-dominated pattern observed here. Stronger models (e.g
…[truncated 5690 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 454 · 2026-05-15T15:17:38.833732+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__read_local_file",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__read_local_file",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 455 · 2026-05-15T15:17:38.884471+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 456 · 2026-05-15T15:17:47.365220+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex",
  "offset": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex",
    "offset": "100"
  }
}
```

</details>

---


### Tool result

_source line 457 · 2026-05-15T15:17:47.365691+00:00_

100	Task removed & $r_{\text{LOO}}$ \\
101	\midrule
102	id-life-stages-1       & 0.963 \\
103	lifespan-long          & 0.969 \\
104	lifespan-l-then-s      & 0.976 \\
105	inclined-plane         & 0.969 \\
106	freeze                 & 0.971 \\
107	meas-melt-point        & 0.972 \\
108	id-life-stages-2       & 0.972 \\
109	find-animal            & 0.970 \\
110	grow-fruit             & 0.973 \\
111	chem-mix               & 0.969 \\
112	find-non-living        & 0.980 \\
113	\bottomrule
114	\end{tabular}
115	\caption{Leave-one-out Pearson $r$ for the death rate differential vs.\ $\Delta_{\text{full}}$ correlation. Full $r = 0.970$; LOO range $[0.963, 0.980]$. No single task type is a leverage point.}
116	\label{tab:loo}
117	\end{table}
118	
119	\section{Router Training Details}
120	\label{app:router-details}
121	
122	We use Qwen3-1.7B for the router to avoid circular dependency with the Qwen2.5-7B data-generating model.
123	
124	Gradient accumulation is critical for the implicit router: with gradient accumulation of 1, the model fails to achieve meaningful routing discrimination (internal recall 26.7\%); with gradient accumulation of 8, the model becomes non-degenerate (internal recall above 50\% across all seeds). All main-text results use gradient accumulation 8.
125	
126	Under a fixed data split, cross-seed balanced accuracy is stable (57--58\%), but internal recall varies from 51.5\% to 81.8\%, reflecting threshold sensitivity. When the data split is also varied, balanced accuracy variance increases 10$\times$ (Appendix~\ref{app:seed-robustness}). Deployed end-to-end, the trained router allocates 97.0\% of episodes to deterministic computation with 17.6\% death rate, and misrouting cost (death from internally-routed episodes) exceeds the benefit of correctly routing rare internal-preferred cases.
127	
128	\begin{table}[h]
129	\centering
130	\small
131	\resizebox{\columnwidth}{!}{%
132	\begin{tabular}{@{}lcc@{}}
133	\toprule
134	Hyperparameter & Classification Head & I
…[truncated 3605 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 458 · 2026-05-15T15:17:47.566591+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission deadline author guidelines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission deadline author guidelines"
  }
}
```

</details>

---


### Tool call

_source line 459 · 2026-05-15T15:17:48.168774+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "simgate-modular-routing",
  "file": "paper_checklist.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "simgate-modular-routing",
    "file": "paper_checklist.yaml"
  }
}
```

</details>

---


### Tool result

_source line 460 · 2026-05-15T15:17:56.557725+00:00_

Web search results for query: "EMNLP 2026 call for papers submission deadline author guidelines"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"Announcements | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"}]

Based on the search results, here's information about EMNLP 2026 regarding call for papers, submission deadlines, and author guidelines:

## Submission Deadline

The ARR submission deadline for long and short papers is May 25, 
…[truncated 1871 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "elapsed_ms": 8991
}
```

</details>

---


### Tool result

_source line 461 · 2026-05-15T15:17:56.558326+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'simgate-modular-routing'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 8389
}
```

</details>

---


### Tool call

_source line 462 · 2026-05-15T15:18:03.309206+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 paper format page limit template ACL style double blind anonymity requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 paper format page limit template ACL style double blind anonymity requirements"
  }
}
```

</details>

---


### Tool call

_source line 463 · 2026-05-15T15:18:04.263647+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 464 · 2026-05-15T15:18:04.967073+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/conclusion.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Glob",
  "elapsed_ms": 703
}
```

</details>

---


### Tool call

_source line 465 · 2026-05-15T15:18:04.967421+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__director_post_to_reviewer",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__director_post_to_reviewer",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 466 · 2026-05-15T15:18:05.017866+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 467 · 2026-05-15T15:18:10.241271+00:00_

Web search results for query: "EMNLP 2026 paper format page limit template ACL style double blind anonymity requirements"

Links: [{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"ClimateNLP 2026","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"Association for Computational Linguistics (ACL) conference - Overleaf, Online LaTeX Editor","url":"https://www.overleaf.com/latex/templates/association-for-computational-linguistics-acl-conference/jvxskxpnznfj"},{"title":"acl2026/formatting.md at master · Lilaizhen/acl2026","url":"https://github.com/Lilaizhen/acl2026/blob/master/formatting.md"},{"title":"GitHub - acl-org/acl-style-files: Official style files for papers submitted to venues of the Association for Computational Linguistics · GitHub","url":"https://github.com/acl-org/acl-style-files"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"GitHub - acl-org/emnlp-2026: Repository for the EMNLP 2026 conference · GitHub","url":"https://github.com/acl-org/emnlp-2026"}]

Based on my web search, here's comprehensive information about EMNLP 2026 paper submission requirements:

## Paper Format and Page Limits

EMNLP 2026 uses a two-column format with an 8-page limit for long papers and a 4-page limit for short papers. EMNLP uses the standard ACL style files, so the LaTeX template is identical to the one used for ACL, NAACL, and other *ACL conferences.

## Templates and Style Files

Official EMNLP 2026 LaTeX template uses ACL style files, a
…[truncated 896 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "elapsed_ms": 6932
}
```

</details>

---


### Tool call

_source line 468 · 2026-05-15T15:18:13.506405+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 469 · 2026-05-15T15:18:13.959223+00:00_

1	\begin{abstract}
2	Modular LLM agents that route between neural reasoning and deterministic computation promise improved reliability, yet understanding \emph{what} drives the value of routing decisions remains unclear. We propose episode-level counterfactual analysis: running complete episodes under pure strategies and comparing final outcomes to decompose routing signal into death-avoidance and non-death components. Across 245 ScienceWorld episodes (11 task types, Qwen2.5-7B-Instruct), death avoidance accounts for approximately 90\% of routing signal (DAF $= 90.41\%$ at $P{=}100$; Pearson $r = 0.97$, $p < 10^{-6}$), with 78.9\% of non-tie labels arising from death asymmetry alone. A trained router achieves only 57--59\% balanced accuracy, confirming thin learnable signal beyond survival. Cross-environment analysis on MATH ($N{=}300$) shows routing signal vanishes without a death penalty: the label distribution inverts from 86:9 (deterministic-preferred) to 30:17 (internal directionally favored), with a non-significant reversal of $+4.3$ percentage points. A Llama-3.1-8B pilot provides preliminary directional evidence that death-driven routing generalizes across model families. These findings indicate that in environments with catastrophic failure modes, routing value is dominated by safety---the router functions primarily as a safety critic rather than an efficiency optimizer.
3	\end{abstract}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 470 · 2026-05-15T15:18:13.959692+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 471 · 2026-05-15T15:18:14.914963+00:00_

1	\section{Introduction}
2	
3	Large language models deployed as interactive agents must repeatedly decide \emph{how} to compute: reason internally, or delegate to an external tool.
4	A Qwen2.5-7B-Instruct agent navigating ScienceWorld \cite{scienceworld-2022}---a text-based science simulation with 30 task types---faces this choice at every step. Tracking temperature thresholds, container states, and multi-step procedures via internal reasoning is error-prone: the model may hallucinate that water has boiled when the stove was never activated, or that an object has been moved when the action was invalid. Deterministic external computation (environment simulators, code interpreters) eliminates such hallucinations via exact state transitions. The practical question for agent design is therefore: \emph{when should an agent route computation externally versus reasoning internally?}
5	
6	Existing routing approaches frame this as a capability or efficiency decision.
7	Toolformer \cite{toolformer-2023} teaches models to insert API calls when doing so reduces perplexity; ART \cite{art-2023} decomposes tasks into tool-augmented programs; Chameleon \cite{chameleon-2023} selects among heterogeneous modules (search, code, vision) per subtask.
8	More recent adaptive-computation methods route to different reasoning depths \cite{cogrouter-2026,ares-2026} or model tiers \cite{mtrouter-2026}.
9	The shared assumption is that routing signal stems from diverse sources---accuracy, latency, capability matching---and that a learned router can exploit this signal to improve over any fixed strategy.
10	But this assumption has never been systematically verified: \emph{what actually drives the value of routing decisions in interactive environments?}
11	
12	We find a surprisingly concentrated answer: \textbf{death avoidance accounts for approximately 90\% of the routing signal} in ScienceWorld.
13	The internal strategy's hallucination-induced failures trigger catastrophic agent death (a $-100$ p
…[truncated 4549 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 472 · 2026-05-15T15:18:14.915403+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 473 · 2026-05-15T15:18:15.367319+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Problem Setup}
5	\label{sec:problem-setup}
6	
7	Consider an interactive environment $\mathcal{E}$ with state space $\mathcal{S}$, observation space $\mathcal{O}$, and action space $\mathcal{A}$. An agent follows a policy $\pi: \mathcal{O}^* \rightarrow \mathcal{A}$ that maps observation histories to actions. At each step $t$, the agent receives observation $o_t$, selects action $a_t = \pi(o_1, \ldots, o_t)$, and the environment transitions to state $s_{t+1}$.
8	
9	We define a modality set $\mathcal{M} = \{{\tt int}, {\tt det}\}$ governing how the agent processes state transitions:
10	\begin{itemize}
11	    \item \textbf{Internal} ($m = {\tt int}$): The agent uses its own generation to predict intermediate observations. The LLM interleaves chain-of-thought reasoning with environment actions following the ReAct paradigm \cite{react-2023}, but prediction errors compound across steps.
12	    \item \textbf{Deterministic} ($m = {\tt det}$): The agent receives ground-truth observations from the environment simulator at each step---equivalent to access to a perfect dynamics model. Action selection remains with the LLM; only the state-transition prediction is replaced.
13	\end{itemize}
14	
15	A \emph{routing policy} $\rho: \mathcal{O}^* \rightarrow \mathcal{M}$ selects which modality to use at each step. The goal of modality routing is to learn $\rho$ that maximizes expected episode return. Our analysis investigates what signal is available to learn such a router.
16	
17	\subsection{Counterfactual Episode Collection}
18	\label{sec:collection}
19	
20	Per-step oracle labeling assigns routing labels by comparing single-step outcomes under each computation modality. Under sparse terminal rewards, this approach degenerates: on ScienceWorld \cite{scienceworld-2022}, 97.4\% of steps (across 11 prescreened task types) produce identical intermediate scores regardless of modality, yielding no routing signal. We instead perform e
…[truncated 6940 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 474 · 2026-05-15T15:18:15.367713+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 475 · 2026-05-15T15:18:15.869823+00:00_

1	\section{Experiments}
2	
3	\subsection{Death Avoidance Decomposition}
4	\label{sec:death-decomp}
5	
6	\begin{figure}[t]
7	\centering
8	\includegraphics[width=\columnwidth]{figures/fig1_daf_scatter.pdf}
9	\caption{Per-task scatter plot: death rate differential (internal minus deterministic) vs.\ performance gap ($\Delta_{\text{full}}$). Pearson $r = 0.9698$ ($p = 8.12 \times 10^{-7}$). Each point is one of 11 ScienceWorld task types.}
10	\label{fig:decomposition}
11	\end{figure}
12	
13	The full performance gap between deterministic and internal strategies across 245 episodes is $\Delta_{\text{full}} = +29.60$ points. When we exclude all episodes where either strategy results in agent death, the gap collapses to $\Delta_{\text{nd}} = +2.84$. The resulting Death Avoidance Factor (\S\ref{sec:daf}) is 90.41\%: approximately 90\% of the deterministic strategy's advantage over internal reasoning is attributable to death avoidance rather than superior task performance when both agents survive.
14	
15	This concentration is consistent across task types (Appendix~\ref{app:per-task}). The Pearson correlation between per-task death rate differential and $\Delta_{\text{full}}$ is $r = 0.9698$ ($p = 8.12 \times 10^{-7}$; bootstrap 95\% CI $[0.952, 0.995]$), as shown in Figure~\ref{fig:decomposition}. Spearman rank correlation is $\rho = 0.986$ ($p = 2.4 \times 10^{-8}$), and leave-one-out analysis shows $r \in [0.963, 0.980]$---no single task type is a leverage point (Appendix~\ref{app:correlation}). We note that death rate differential and $\Delta_{\text{full}}$ are structurally coupled through the penalty term $P$, so high correlation is expected when death dominates. The empirically non-trivial finding is that 78.9\% of non-tie routing labels are driven by death asymmetry independent of $P$. Knowing how much more frequently the internal strategy dies is nearly sufficient to predict the full performance gap for a given task type. The internal strategy dies in 42.9\% of episode
…[truncated 7177 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 476 · 2026-05-15T15:18:15.870361+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 477 · 2026-05-15T15:18:16.372084+00:00_

1	\section{Related Work}
2	
3	\paragraph{Tool Use and External Computation in LLMs.}
4	A growing body of work augments language models with external tools.
5	Toolformer \cite{toolformer-2023} teaches LLMs to insert API calls via self-supervised loss filtering, while ToolkenGPT \cite{toolkengpt-2023} represents tools as special tokens in the embedding space, enabling frozen models to invoke massive tool libraries.
6	ART \cite{art-2023} decomposes tasks into multi-step programs that interleave reasoning with tool calls, and Chameleon \cite{chameleon-2023} composes heterogeneous modules (search, code, vision) via LLM-generated programs.
7	ReTool \cite{retool-2026} applies reinforcement learning to let models discover when code execution is preferable to chain-of-thought.
8	These approaches focus on \emph{learning to use tools}; our work instead asks a prior question: \emph{what signal drives the decision to route to an external modality at all?}
9	
10	Recent concurrent studies sharpen this question from multiple angles.
11	\citet{tool-overuse-illusion-2026} identify a cognitive-illusion effect in which LLMs default to external tools even when internal knowledge suffices.
12	\citet{when2tool-2026} show that tool-call decisions are already encoded in hidden states before explicit reasoning occurs.
13	\citet{tool-use-tax-2026} quantify a ``tool-use tax''---cases where invoking a tool degrades rather than improves performance.
14	\citet{to-call-or-not-2026} propose a necessity--utility--affordability framework for deciding whether to call a tool.
15	Our counterfactual decomposition provides complementary, environment-grounded evidence: in ScienceWorld, ${\sim}90\%$ of the routing signal at $P{=}100$ traces to catastrophic-failure prevention rather than general utility, offering a concrete quantification that these frameworks currently lack.
16	
17	\paragraph{Adaptive Computation and Routing.}
18	Rather than adding new tools, a parallel line of research routes inputs to dif
…[truncated 3985 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 478 · 2026-05-15T15:18:16.372478+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 479 · 2026-05-15T15:18:16.623507+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Cross-environment evidence.}
5	The death-avoidance finding in ScienceWorld raises a natural question: does routing signal persist in environments without catastrophic failure? An evaluation on MATH Level~4--5 (300 problems: 152 Level~4, 148 Level~5), using code interpreter as the deterministic modality, suggests not. Internal reasoning directionally outperforms code interpreter: 81.0\% accuracy (95\% CI [76.7, 85.3]) versus 76.7\% (95\% CI [72.0, 81.3]); the paired difference of $+4.3$~percentage points (95\% CI [0.0, $+8.7$]; McNemar $p = 0.079$) shows a directional reversal, though not statistically significant at the 95\% level. The label distribution inverts relative to ScienceWorld: 30 internal-preferred versus 17 deterministic-preferred (compared to 9:86 in ScienceWorld), with 84.3\% of problems (253 of 300) showing no modality preference. In the absence of death risk, the routing signal vanishes or reverses---consistent with death avoidance as the primary driver of the deterministic strategy's advantage observed in ScienceWorld. Figure~\ref{fig:signal-reversal} and Table~\ref{tab:cross-env} summarize this label distribution inversion.
6	
7	\begin{figure}[t]
8	\centering
9	\includegraphics[width=\columnwidth]{figures/signal_reversal.pdf}
10	\caption{Label distribution reversal across environments. In ScienceWorld (with $-100$ death penalty), deterministic-preferred labels dominate (86:9). In MATH (no death penalty), the pattern inverts (17:30), with 84.3\% showing no preference.}
11	\label{fig:signal-reversal}
12	\end{figure}
13	
14	\begin{table}[t]
15	\centering
16	\small
17	\resizebox{\columnwidth}{!}{%
18	\begin{tabular}{@{}lccccc@{}}
19	\toprule
20	Environment & $N$ & Det\% & Int\% & NoPref\% & Death? \\
21	\midrule
22	ScienceWorld & 245 & 35.1 & 3.7 & 61.2 & Yes ($-100$) \\
23	MATH & 300 & 5.7 & 10.0 & 84.3 & No \\
24	ALFWorld & 135 & 25.9 & 1.5 & 72.6 & No\textsuperscript{$\dagger$} \\
25	\b
…[truncated 5133 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 480 · 2026-05-15T15:18:16.624010+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 481 · 2026-05-15T15:18:16.674862+00:00_

1	\section{Conclusion}
2	
3	We introduced episode-level counterfactual analysis as a methodology for decomposing the routing signal in modular LLM agents into death-avoidance and non-death components. Applied to 245 ScienceWorld episodes across 11 task types with a Qwen2.5-7B-Instruct backbone, this analysis reveals that death avoidance accounts for approximately 90\% of routing value (DAF $= 90.41\%$ at $P{=}100$; $\Delta_\text{full} = 29.60$ vs.\ $\Delta_\text{nd} = 2.84$), with 78.9\% of non-tie labels arising from death asymmetry alone and strong cross-task correlation ($r = 0.97$, $p < 10^{-6}$).
4	
5	Two lines of evidence support the generality of this finding. First, cross-environment analysis on MATH ($N{=}300$), where no death penalty exists, shows that the routing signal vanishes and directionally reverses: internal reasoning directionally outperforms code execution by $+4.3$ percentage points (not statistically significant; \S\ref{sec:discussion}), and the label distribution inverts from 86:9 deterministic-preferred in ScienceWorld to 30:17 internal-preferred. This contrast confirms that death avoidance, not an inherent advantage of deterministic computation, is the primary driver. Second, a Llama-3.1-8B pilot replicates the direction of the death differential (freeze death gap $+20\%$, consistent with Qwen's $+30\%$), providing preliminary evidence that the pattern generalizes across model families.
6	
7	A trained routing classifier achieves only 57--59\% balanced accuracy across four seeds, confirming that once death avoidance is accounted for, the remaining learnable signal is thin. The classification head variant degenerates to always-deterministic predictions despite achieving non-trivial logit-level separation, suggesting that discriminative routing over LLM representations is fundamentally limited in this regime.
8	
9	These results carry a practical implication: in environments with catastrophic failure modes, routing value is dominated by safety r
…[truncated 774 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 482 · 2026-05-15T15:18:22.748530+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "simgate-modular-routing",
  "file": "decisions.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "simgate-modular-routing",
    "file": "decisions.yaml"
  }
}
```

</details>

---


### Tool result

_source line 483 · 2026-05-15T15:18:23.100430+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/decisions.yaml\", \"content\": \"_next_id: 60\\ndecisions:\\n- id: D001\\n  date: 2026-05-13 04:25 UTC\\n  summary: 'MVP 方案: ScienceWorld 信号检测——验证确定性模拟是否在规则驱动任务上优于 LLM 内部推理'\\n  rationale: 12 天 deadline 下必须快速验证核心假设。ScienceWorld 是 primary track，其 JVM 后端提供精确的规则化状态转移，与\\n    LLM 近似推理的差距应该最大。选 5 task types × 10 episodes 的小规模 counterfactual 比较，不训练 router，纯信号检测。Pass\\n    标准 ≥2/5 task types >5pp，基于 ITP-R vs CogRouter 7.4pp 差距的量级。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-13 04:28 UTC\\n  summary: 采纳 Reviewer 全部 4 条 warning，修订 MVP 为 Phase 0 + Phase 1 两阶段方案\\n  rationale: Reviewer 指出 D001 方案 3 个操作层缺陷：(1) counterfactual 方法未明确——改为 episode-level\\n    3-way (always-internal / always-deterministic / oracle-routing)，oracle 作为 selective\\n    routing 上界；(2) N=10 统计功效不足——增加到 20 episodes/task type + bootstrap 90% CI；(3) kill\\n    criteria 不完整——增加 Phase 0 工程 gate、灰区 conditional pass、pre-register 5 task types\\n    (3S+1M+1W)。无额外 GPU 成本，仅设计层修正。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-13 07:43 UTC\\n  summary: GPU0 继续收集 baseline，GPU1 停下修复 tie-break + 致死动作过滤后重跑\\n  rationale: Fork 诊断发现两个方法论缺陷：(1) tie-break >= 使 95% delta=0 步骤 oracle 永远选 internal，oracle\\n    数据不可信；(2) 致死动作 (score=-100) 污染三条线。修 >= 为 >（oracle 仅在 deterministic 严格更优时介入）+ 致死动作过滤。不做\\n    N-step rollout——1-step 局限性是真实发现，MVP 应如实反映。GPU0 baseline 数据有效，不浪费已有进度。\\n  related_experiments:\\n  - exp_id: mvp-p1-gpu0\\n    role: baseline data, continue\\n  - exp_id: mvp-p1-gpu1-vllm\\n    role: kill, fix, rerun\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-13 08:13 UTC\\n  summary: MVP 判定 primary metric 改为 always-deterministic vs always-internal，oracle\\n    降为 supplementary\\n  rationale: 1-step lookahead 在稀疏 reward 下 95% 步骤 delta=0，任何 tie-break 都使 oracle 退化（>=\\n    → always-internal，> → always-determinist
…[truncated 10983 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 484 · 2026-05-15T15:18:24.204290+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing"
  }
}
```

</details>

---


### Tool result

_source line 485 · 2026-05-15T15:18:24.505646+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Glob",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 486 · 2026-05-15T15:18:24.957550+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_reports/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_reports/**",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing"
  }
}
```

</details>

---


### Tool result

_source line 487 · 2026-05-15T15:18:25.459362+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_1.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_2.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_3.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_4.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_5.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_6.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Glob",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 488 · 2026-05-15T15:18:25.660379+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "references.*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "references.*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 489 · 2026-05-15T15:18:25.711473+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Glob",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 490 · 2026-05-15T15:18:40.020015+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 491 · 2026-05-15T15:18:40.472061+00:00_

1	@inproceedings{scienceworld-2022,
2	  title={ScienceWorld: Is Your Agent Smarter Than a 5th Grader?},
3	  author={Wang, Ruoyao and Jansen, Peter and C\^{o}t\'{e}, Marc-Alexandre and Ammanabrolu, Prithviraj},
4	  booktitle={Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
5	  year={2022}
6	}
7	
8	@inproceedings{react-2023,
9	  title={ReAct: Synergizing Reasoning and Acting in Language Models},
10	  author={Yao, Shunyu and Zhao, Jeffrey and Yu, Dian and Du, Nan and Shafran, Izhak and Narasimhan, Karthik and Cao, Yuan},
11	  booktitle={International Conference on Learning Representations (ICLR)},
12	  year={2023}
13	}
14	
15	@inproceedings{toolformer-2023,
16	  title={Toolformer: Language Models Can Teach Themselves to Use Tools},
17	  author={Schick, Timo and Dwivedi-Yu, Jane and Dess\`{i}, Roberto and Raileanu, Roberta and Lomeli, Maria and Hambro, Eric and Zettlemoyer, Luke and Cancedda, Nicola and Scialom, Thomas},
18	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
19	  year={2023}
20	}
21	
22	@article{art-2023,
23	  title={ART: Automatic Multi-step Reasoning and Tool-use for Large Language Models},
24	  author={Paranjape, Bhargavi and Lundberg, Scott and Singh, Sameer and Hajishirzi, Hannaneh and Zettlemoyer, Luke and Ribeiro, Marco Tulio},
25	  journal={arXiv preprint arXiv:2303.09014},
26	  year={2023}
27	}
28	
29	@inproceedings{chameleon-2023,
30	  title={Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models},
31	  author={Lu, Pan and Peng, Baolin and Cheng, Hao and Galley, Michel and Chang, Kai-Wei and Wu, Ying Nian and Zhu, Song-Chun and Gao, Jianfeng},
32	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
33	  year={2023}
34	}
35	
36	@article{retool-2026,
37	  title={ReTool: Reinforcement Learning for Strategic Tool Use in LLMs},
38	  author={Feng, Jiazhan and others},
39	  journal={arXiv preprint arXiv:2504.11536},
40	  year={2025}
41	}
…[truncated 5559 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 492 · 2026-05-15T15:18:42.429493+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Check external review config",
  "subagent_type": "Explore",
  "prompt": "Search for external_review or paperreview_ai configuration in project config files under /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/. Check files like config.yaml, project.yaml, settings.yaml, or any YAML/JSON config file that might contain an \"external_review\" section. Report whether external_review.paperreview_ai.enabled is true or false. Quick search."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Agent",
  "tool_args": {
    "description": "Check external review config",
    "subagent_type": "Explore",
    "prompt": "Search for external_review or paperreview_ai configuration in project config files under /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/. Check files like config.yaml, project.yaml, settings.yaml, or any YAML/JSON config file that might contain an \"external_review\" section. Report whether external_review.paperreview_ai.enabled is true or false. Quick search."
  }
}
```

</details>

---


### Tool call

_source line 493 · 2026-05-15T15:18:44.186391+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/**/*.{yaml,yml,json}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/**/*.{yaml,yml,json}"
  }
}
```

</details>

---


### Tool result

_source line 494 · 2026-05-15T15:18:44.287232+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/checkpoints/mvp-p0-forking_PREPARING_20260513T045005.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/checkpoints/mvp-p1-signal_PREPARING_20260513T045006.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/logs/workers/worker_infra_env-setup_20260513T045052_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/logs/workers/worker_code_mvp-scripts_20260513T045148_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/logs/workers/worker_infra_model-check_20260513T045724_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/logs/workers/worker_exp_phase0-run_20260513T045900_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/checkpoints/mvp-p0-forking_PREPARING_20260513T050948.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/checkpoints/mvp-p0-forking_QUEUED_20260513T050956.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/checkpoints/mvp-p0-forking_ALLOCATED_20260513T051008.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/checkpoints/mvp-p0-forking_DONE_20260513T051013.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/logs/workers/worker_exp_phase0-rerun_20260513T052947_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/logs/workers/worker_exp_phase1-deploy-gpu0_20260513T051059_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/checkpoints/mvp-p1-gpu1_PREPARING_20260513T054520.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/checkpoints/mvp-p1-gpu0_PREPARING_20260513T054522.json
/home/ubu
…[truncated 12686 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 495 · 2026-05-15T15:18:44.338035+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing -maxdepth 2 -type f \\( -name \"*.yaml\" -o -name \"*.yml\" -o -name \"*.json\" \\) | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing -maxdepth 2 -type f \\( -name \"*.yaml\" -o -name \"*.yml\" -o -name \"*.json\" \\) | head -20"
  }
}
```

</details>

---


### Tool result

_source line 496 · 2026-05-15T15:18:44.539362+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/writing_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/paper_provenance.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/checkpoints/plan-013-labeling-quality_PREPARING_20260514T120850.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/checkpoints/plan-011-rule-based_RUNNING_20260514T005127.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/checkpoints/alfworld-counterfactual-full_RUNNING_20260514T174638.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/checkpoints/research-prescreening-gpu0_QUEUED_20260513T162427.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/checkpoints/plan-004-ablation-b-seed789_RUNNING_20260514T092038.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/checkpoints/plan-002-formal_PREPARING_20260514T052833.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/checkpoints/plan-010-cross-task-transfer_PREPARING_20260515T123251.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/checkpoints/plan-002-formal-v3_PENDING_20260514T060209.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/checkpoints/plan-011-rule-based_RUNNING_20260514T005133.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/checkpoints/plan-004-ablation-b-seed123_QUEUED_20260514T092003.json
/home/ubuntu/.agent-
…[truncated 687 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 497 · 2026-05-15T15:18:46.800054+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview_ai",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "glob": "*.{yaml,yml,json}",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview_ai",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
    "glob": "*.{yaml,yml,json}",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---


### Tool result

_source line 498 · 2026-05-15T15:18:46.951152+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Grep",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 499 · 2026-05-15T15:18:46.951620+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/registry.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/registry.yaml"
  }
}
```

</details>

---


### Tool result

_source line 500 · 2026-05-15T15:18:47.253083+00:00_

File content (48427 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 501 · 2026-05-15T15:18:48.760215+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing -maxdepth 1 -type f \\( -name \"*config*\" -o -name \"*project*\" -o -name \"*settings*\" \\)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing -maxdepth 1 -type f \\( -name \"*config*\" -o -name \"*project*\" -o -name \"*settings*\" \\)"
  }
}
```

</details>

---


### Tool result

_source line 502 · 2026-05-15T15:18:49.011542+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 503 · 2026-05-15T15:18:49.162617+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "glob": "registry.yaml",
  "output_mode": "content",
  "head_limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
    "glob": "registry.yaml",
    "output_mode": "content",
    "head_limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 504 · 2026-05-15T15:18:49.213193+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 505 · 2026-05-15T15:18:50.618627+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing | grep -E \"\\.yaml|\\.json|config|settings\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing | grep -E \"\\.yaml|\\.json|config|settings\""
  }
}
```

</details>

---


### Tool result

_source line 506 · 2026-05-15T15:18:50.922209+00:00_

-rw-------  1 ubuntu ubuntu  59281 May 15 15:13 decisions.yaml
-rw-------  1 ubuntu ubuntu    970 May 13 16:24 dream_registry.yaml
-rw-r--r--  1 ubuntu ubuntu    975 May 13 16:24 dream_registry.yaml.bak
-rw-------  1 ubuntu ubuntu  10292 May 15 06:33 experiment_plan.yaml
-rw-r--r--  1 ubuntu ubuntu  12271 May 14 00:44 literature_map.yaml
-rw-------  1 ubuntu ubuntu  26385 May 15 15:14 paper_provenance.yaml
-rw-------  1 ubuntu ubuntu 129421 May 15 15:16 registry.yaml
-rw-r--r--  1 ubuntu ubuntu   7984 May 14 08:56 writing_plan.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 303
}
```

</details>

---


### Tool call

_source line 507 · 2026-05-15T15:18:50.922594+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\\|paperreview_ai\" /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing --include=\"*.yaml\" --include=\"*.json\" 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\\|paperreview_ai\" /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing --include=\"*.yaml\" --include=\"*.json\" 2>/dev/null | head -20"
  }
}
```

</details>

---


### Tool result

_source line 508 · 2026-05-15T15:18:51.023235+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 509 · 2026-05-15T15:18:53.233031+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -A 10 -B 2 \"external\" /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/registry.yaml | head -50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -A 10 -B 2 \"external\" /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/registry.yaml | head -50"
  }
}
```

</details>

---


### Tool result

_source line 510 · 2026-05-15T15:18:53.334125+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 511 · 2026-05-15T15:18:53.385171+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "head -100 /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/registry.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "tool_args": {
    "command": "head -100 /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/registry.yaml"
  }
}
```

</details>

---


### Tool result

_source line 512 · 2026-05-15T15:18:53.435898+00:00_

baseline: null
experiments:
  mvp-p0-forking:
    status: DONE
    retry_count: 0
    created_at: '2026-05-13T04:50:05.057Z'
    updated_at: '2026-05-13T05:10:18.587Z'
    spec:
      hypothesis: ScienceWorld action-replay state forking 可行：fork 成功率≥80%，单次 fork
        延迟<5s
      description: Phase 0 工程可行性验证 - ScienceWorld state forking
      checkpoint_path: N/A
      log_path: /root/autodl-tmp/simgate-modular-routing/results/mvp/phase0_validation.json
      command: python src/phase0_validate_forking.py
      server: westb-13313
      data_path: N/A
      data_count: 10
      model_name: N/A
      seed: 0
    conclusion: success
    completed_at: '2026-05-13T05:10:13.526Z'
    metrics:
      fork_success_rate: 1
      avg_latency_s: 1.67
      p50_latency_s: 1.53
      p95_latency_s: 2.37
      max_memory_mb: 20
      gate: PASS
  mvp-p1-signal:
    status: DONE
    retry_count: 0
    created_at: '2026-05-13T04:50:06.546Z'
    updated_at: '2026-05-15T12:33:26.918Z'
    spec:
      hypothesis: Oracle routing 在 strong task types 上显著优于 always-internal，证明 selective
        routing 存在信号
      description: Phase 1 信号检测 - 3-way comparison across 5 task types
      parent: mvp-p0-forking
      command: N/A (killed before execution)
      server: westb-13313
      data_path: N/A
      data_count: 0
      model_name: Qwen2.5-7B-Instruct
      seed: 42
    conclusion: killed
    checkpoint_path: N/A (killed)
    log_path: N/A (killed)
    completed_at: '2026-05-15T12:33:26.918Z'
  mvp-p1-gpu1:
    status: DONE
    retry_count: 0
    created_at: '2026-05-13T05:45:20.053Z'
    updated_at: '2026-05-13T07:09:59.347Z'
    spec:
      command: python src/phase1_signal.py --task_types 'chemistry-mix-paint-secondary-color,grow-plant'
        --episodes 20 --gpu_id 0 --max_steps 30 --output_dir results/mvp/ --model_path
        /root/autodl-tmp/models/Qwen/Qwen2___5-7B-Instruct/ --no_vllm
      server: westb-13313
      gpu:
      - cuda:1
      pid: '55775'
      log_path: ~/runs/si
…[truncated 1382 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 513 · 2026-05-15T15:18:55.845045+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_12 -name \"config.yaml\" -o -name \"project.yaml\" -o -name \"settings.yaml\" 2>/dev/null | head -10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_12 -name \"config.yaml\" -o -name \"project.yaml\" -o -name \"settings.yaml\" 2>/dev/null | head -10"
  }
}
```

</details>

---


### Tool result

_source line 514 · 2026-05-15T15:18:55.897708+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 515 · 2026-05-15T15:18:55.948661+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_12/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_12/"
  }
}
```

</details>

---


### Tool result

_source line 516 · 2026-05-15T15:18:55.999627+00:00_

total 44
drwxrwxr-x  9 ubuntu ubuntu 4096 May 10 18:14 .
drwxr-x--- 18 ubuntu ubuntu 4096 May 15 08:38 ..
drwxr-xr-x  3 ubuntu ubuntu 4096 May 10 18:14 .claude
-rw-r--r--  1 ubuntu ubuntu  355 May 15 15:17 AGENTS.md
drwxrwxr-x  4 ubuntu ubuntu 4096 May 15 15:18 config
drwxr-xr-x  4 ubuntu ubuntu 4096 May 15 15:17 global
drwxr-xr-x  2 ubuntu ubuntu 4096 May 13 04:23 idea_generator
drwxrwxr-x  5 ubuntu ubuntu 4096 May 13 04:23 projects
drwxr-xr-x  3 ubuntu ubuntu 4096 May 10 14:54 skills
drwxr-xr-x  2 ubuntu ubuntu 4096 May 15 15:18 state
-rw-r--r--  1 ubuntu ubuntu   13 May 10 14:54 workspace.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 517 · 2026-05-15T15:18:57.605904+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_12/config -type f \\( -name \"*.yaml\" -o -name \"*.json\" \\) | xargs ls -la"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_12/config -type f \\( -name \"*.yaml\" -o -name \"*.json\" \\) | xargs ls -la"
  }
}
```

</details>

---


### Tool result

_source line 518 · 2026-05-15T15:18:57.707114+00:00_

-rw-rw-r-- 1 ubuntu ubuntu  2901 May  9 09:00 /home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/approvals.yaml
-rw------- 1 ubuntu ubuntu   770 May 10 15:25 /home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/backend.yaml
-rw-r--r-- 1 ubuntu ubuntu  1148 May 15 15:17 /home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/claude_sessions.json
-rw------- 1 ubuntu ubuntu 13083 May 15 15:18 /home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/crons.yaml
-rw------- 1 ubuntu ubuntu   829 May 14 14:09 /home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/email_tokens.json
-rw------- 1 ubuntu ubuntu   148 May 15 09:17 /home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/feishu.yaml
-rw-r--r-- 1 ubuntu ubuntu  4782 May 15 14:30 /home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/keepalive.json
-rw-r--r-- 1 ubuntu ubuntu   342 May 10 14:54 /home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/mcp_config.json
-rw-r--r-- 1 ubuntu ubuntu   394 May 13 04:23 /home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/mcp_config_director.json
-rw-r--r-- 1 ubuntu ubuntu   420 May 13 16:04 /home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/mcp_config_dream_review_director.json
-rw-r--r-- 1 ubuntu ubuntu   398 May 10 18:14 /home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/mcp_config_no_project.json
-rw-r--r-- 1 ubuntu ubuntu   400 May 14 00:47 /home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/mcp_config_paper_agent.json
-rw-r--r-- 1 ubuntu ubuntu   408 May 14 12:28 /home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/mcp_config_review_director.json
-rw-r--r-- 1 ubuntu ubuntu   436 May 14 12:32 /home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/mcp_config_review_reviewer_1.json
-rw-r--r-- 1 ubuntu ubuntu   436 May 14 12:32 /home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/mcp_config_review_reviewer_2.json
-rw-r--r-- 1 ubuntu ubuntu   394 May 13 04:25 /home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/mcp_config_reviewer.json
-rw-
…[truncated 4879 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 519 · 2026-05-15T15:18:57.758214+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_12/config 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_12/config 2>/dev/null"
  }
}
```

</details>

---


### Tool result

_source line 520 · 2026-05-15T15:18:57.859059+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 521 · 2026-05-15T15:19:00.570251+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/projects/simgate-modular-routing.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/projects/simgate-modular-routing.yaml"
  }
}
```

</details>

---


### Tool result

_source line 522 · 2026-05-15T15:19:00.570621+00:00_

1	execution:
2	  account: root
3	  gpu_constraint:
4	  - autodl-simgate:cuda:0
5	  - autodl-simgate:cuda:1
6	  gpu_ids:
7	  - cuda:0
8	  - cuda:1
9	  project_path: /root/autodl-tmp/simgate-modular-routing
10	  servers:
11	  - westb-13313
12	feishu:
13	  chat_id: oc_f6bffc7e8351600df8091f08a63cd5a0
14	  operational_chat_id: oc_6551c2d0ac89db1b3b9e56f77fcf912d
15	  review_paper_path: projects/simgate-modular-routing/docs/paper/main.tex
16	  review_round: 7
17	  review_supplementary_paths: ''
18	  submission_chat_id: oc_0b622d6038b969b96148ee8a163a1a0c
19	project:
20	  created_at: '2026-05-13T04:23:23.832Z'
21	  description: 'SimGate: Learning When to Route LLM Agents to Deterministic Computation
22	    via Explicit Modular Gating'
23	  name: simgate-modular-routing
24	  phase: research
25	  source_idea_id: idea_010
26	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 523 · 2026-05-15T15:19:02.032919+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/backend.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/backend.yaml"
  }
}
```

</details>

---


### Tool result

_source line 524 · 2026-05-15T15:19:02.083798+00:00_

1	manager:
2	  enabled: true
3	  url: http://172.31.31.59:8700
4	  my_id: be-idea-gen-0509-12
5	  my_token: 9e18e2598f4aeed13fe1aa3f577dbb5b47ff15f6ccd3dc14f5e6a77e0eff40ca
6	  ingest_token: e1dc1e287cb57d2e8411481f152c3cfb22d694b1bc8043b04a543cc7f0e08b82
7	  api:
8	    listen_host: 0.0.0.0
9	    listen_port: 8420
10	    allowed_source_cidrs:
11	    - 10.0.0.0/8
12	    - 192.168.0.0/16
13	    - 172.16.0.0/12
14	    - 127.0.0.0/8
15	  capabilities:
16	    read: true
17	    bootstrap_project: true
18	    archive_project: true
19	    allocate_gpus: true
20	    release_gpus: true
21	    read_chat_history: true
22	    claude_account_login: true
23	    read_claude_pool: true
24	  local_approvals:
25	    bootstrap_project: false
26	    archive_project: false
27	    allocate_gpus: false
28	  heartbeat:
29	    enabled: true
30	    interval_sec: 60
31	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 525 · 2026-05-15T15:19:04.142909+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_12/global -type f \\( -name \"*.yaml\" -o -name \"*.json\" \\) 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_12/global -type f \\( -name \"*.yaml\" -o -name \"*.json\" \\) 2>/dev/null"
  }
}
```

</details>

---


### Tool result

_source line 526 · 2026-05-15T15:19:04.194216+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_12/global/logs/pending_queue/f8ae0a955f2c.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/global/logs/pending_queue/7de833f10a23.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/global/logs/pending_queue/6bd433183920.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/global/logs/workers/registry.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/global/approvals.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/global/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/global/checkpoints/plan-008-router-size_PREPARING_20260515T135527.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/global/checkpoints/scienceworld-data-consolidation_RUNNING_20260514T132601.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/global/checkpoints/plan-008-router-size-v2_DONE_20260515T144646.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/global/checkpoints/plan-008-router-size_DONE_20260515T135544.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/global/checkpoints/plan-008-router-size_RUNNING_20260515T135541.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/global/checkpoints/math-negative-contrast_RUNNING_20260515T070918.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/global/checkpoints/math-negative-contrast_QUEUED_20260515T070914.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/global/checkpoints/plan-008-router-size-v2_RUNNING_20260515T144641.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/global/checkpoints/scienceworld-data-consolidation_QUEUED_20260514T132548.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/global/checkpoints/math-negative-contrast_DONE_20260515T075229.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/global/checkpoints/scienceworld-data-consolidation_DONE_20260514T132607.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/global/checkpoints/plan-008-router-size_QUEUED_20260515T135537.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/
…[truncated 442 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 527 · 2026-05-15T15:19:04.244895+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_12 --include=\"*.yaml\" --include=\"*.json\" 2>/dev/null | head -5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_12 --include=\"*.yaml\" --include=\"*.json\" 2>/dev/null | head -5"
  }
}
```

</details>

---


### Tool result

_source line 528 · 2026-05-15T15:19:04.345771+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 529 · 2026-05-15T15:19:05.952215+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "head -100 /home/ubuntu/.agent-ml-research-idea_gen_0509_12/global/approvals.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "tool_args": {
    "command": "head -100 /home/ubuntu/.agent-ml-research-idea_gen_0509_12/global/approvals.yaml"
  }
}
```

</details>

---


### Tool result

_source line 530 · 2026-05-15T15:19:06.103262+00:00_

approvals:
  apr_20260513T162053_0kki:
    approval_id: apr_20260513T162053_0kki
    context:
      file_scope: 0
      task_type: exp:research-prescreening-gpu0
    created_at: '2026-05-13T16:20:53.128Z'
    feishu_card_message_id: om_x100b6f7e00b658a0c427ccebf720b8b
    project: simgate-modular-routing
    reject_reason: null
    resolved_at: '2026-05-13T16:21:56.916605+00:00'
    resolved_by: agent
    risk_score:
      auto_approve: false
      dimensions:
      - label: 任务类型
        level: medium
        name: task_type
        value: exp:research-prescreening-gpu0
      - label: 涉及文件数
        level: low
        name: file_scope
        value: 0
      overall: medium
      reason: 需要人工审批。维度：任务类型=exp:research-prescreening-gpu0(medium), 涉及文件数=0(low)
    status: approved
    subject_id: worker_exp_research-prescreening-gpu0_20260513T162053
    type: worker
  apr_20260513T162106_cu3p:
    approval_id: apr_20260513T162106_cu3p
    context:
      file_scope: 0
      task_type: exp:research-boil-v3-gpu1
    created_at: '2026-05-13T16:21:06.622Z'
    feishu_card_message_id: om_x100b6f7e01e33cacc434f5df5fd20a6
    project: simgate-modular-routing
    reject_reason: null
    resolved_at: '2026-05-13T16:21:57.119828+00:00'
    resolved_by: agent
    risk_score:
      auto_approve: false
      dimensions:
      - label: 任务类型
        level: medium
        name: task_type
        value: exp:research-boil-v3-gpu1
      - label: 涉及文件数
        level: low
        name: file_scope
        value: 0
      overall: medium
      reason: 需要人工审批。维度：任务类型=exp:research-boil-v3-gpu1(medium), 涉及文件数=0(low)
    status: approved
    subject_id: worker_exp_research-boil-v3-gpu1_20260513T162106
    type: worker
  apr_20260514T122334_wvww:
    approval_id: apr_20260514T122334_wvww
    context:
      chat_id: oc_f6bffc7e8351600df8091f08a63cd5a0
      deadline: ''
      has_prior_review: true
      mode_reason: 连续迭代修复，需验证 R2 问题是否彻底解决以及多章节压缩是否引入新问题。
      paper_path: projects/simgate-modular-routing
…[truncated 1531 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 531 · 2026-05-15T15:19:06.154323+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -i \"external\\|paperreview\\|review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_12/global/approvals.yaml | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -i \"external\\|paperreview\\|review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_12/global/approvals.yaml | head -20"
  }
}
```

</details>

---


### Tool result

_source line 532 · 2026-05-15T15:19:06.205042+00:00_

      has_prior_review: true
      recommended_review_mode: continue
      review_chat_id: oc_0b622d6038b969b96148ee8a163a1a0c
      review_mode: continue
      review_round: 0
      has_prior_review: true
      recommended_review_mode: continue
      review_chat_id: oc_0b622d6038b969b96148ee8a163a1a0c
      review_mode: continue
      review_round: 1
      has_prior_review: true
      recommended_review_mode: continue
      review_chat_id: oc_0b622d6038b969b96148ee8a163a1a0c
      review_mode: continue
      review_round: 2
      has_prior_review: true
      mode_reason: 三轮迭代后的终稿，fresh review 可给出无偏最终评估，避免 continue 模式的确认偏差。
      recommended_review_mode: fresh
      review_chat_id: oc_0b622d6038b969b96148ee8a163a1a0c
      review_mode: fresh

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 533 · 2026-05-15T15:19:08.363439+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /root -name \"*config*\" -type f \\( -name \"*.yaml\" -o -name \"*.json\" \\) 2>/dev/null | grep -i \"review\\|external\" | head -5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /root -name \"*config*\" -type f \\( -name \"*.yaml\" -o -name \"*.json\" \\) 2>/dev/null | grep -i \"review\\|external\" | head -5"
  }
}
```

</details>

---


### Tool call

_source line 534 · 2026-05-15T15:19:08.363964+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "env | grep -i \"review\\|paper\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "tool_args": {
    "command": "env | grep -i \"review\\|paper\""
  }
}
```

</details>

---


### Tool result

_source line 535 · 2026-05-15T15:19:08.818221+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 454
}
```

</details>

---


### Tool result

_source line 536 · 2026-05-15T15:19:08.818551+00:00_

PWD=/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/review_director_19d7e797

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Bash",
  "elapsed_ms": 454
}
```

</details>

---


### Tool result

_source line 537 · 2026-05-15T15:19:12.635204+00:00_

Based on my comprehensive search of the project configuration files, here is my finding:

**Search Result: No external_review configuration found**

I thoroughly searched the project configuration directory at `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/` and related configuration files, including:

1. Project config files: `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/projects/simgate-modular-routing.yaml`
2. Backend configuration: `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/config/backend.yaml`
3. Global configuration files: Various YAML files in `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/global/`
4. Project registry files: `registry.yaml`, `decisions.yaml`, etc.

**Conclusion:**
The setting `external_review.paperreview_ai.enabled` does **NOT appear to be configured** in any of the project's YAML or JSON configuration files. There are no references to "external_review" or "paperreview_ai" anywhere in the configuration structure. The system relies on other review mechanisms (Feishu approval workflows, internal review rounds) but does not have a dedicated external_review.paperreview_ai configuration section with an enabled flag.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Agent",
  "elapsed_ms": 30205
}
```

</details>

---


### Tool call

_source line 538 · 2026-05-15T15:20:05.801215+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "你是 Reviewer 1，负责审查**方法严谨性 + 实验充分性**。\n\n## 论文信息\n- **标题**: Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\n- **路径**: `projects/simgate-modular-routing/docs/paper/main.tex`（含 abstract.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, discussion.tex, conclusion.tex）\n- **目标 Venue**: EMNLP 2026 Main Conference (via ACL Rolling Review May 2026 cycle)\n- **Deadline**: 2026-05-25\n- **格式要求**: ACL style, 8 页正文, double-blind, 附录不计页数\n\n## 你的审查侧重\n\n### 1. Counterfactual 方法设计\n- Episode-level counterfactual 比较的有效性：pure-strategy 对比是否充分隔离了 modality 的影响？\n- 标注方案 (Algorithm 1) 的合理性：death-aware labeling 是否引入了偏差？\n- 97.4% step-level tie rate 的声明是否令人信服？这是否充分论证了 episode-level 标注的必要性？\n\n### 2. DAF Metric\n- DAF 的数学定义是否合理？分解公式 Δ_full ≈ δ·P + Δ_nd 的近似误差 (0.8%) 是否可接受？\n- DAF 随 P 单调递增是数学必然——论文是否充分承认这一点，避免将其作为经验发现？\n- 78.9% death-asymmetry label fraction 作为 penalty-independent companion metric 是否足够？\n\n### 3. 统计分析\n- 245 episodes, 11 task types 的样本量对支持 r=0.97 的声明是否足够？\n- Bootstrap CI、LOO 分析、Spearman 检验等统计方法使用是否恰当？\n- 95 个 non-tie labels 中 86:9 的极端不平衡——统计检验的功效是否足够？\n\n### 4. Router 训练诊断\n- Router balanced accuracy 57-59% 的解读是否合理？这是否真的表明 \"thin learnable signal\"？\n- Classification head 退化 (0% internal recall) 的分析是否充分？\n- Cross-split variance (5.2 pp) vs fixed-split variance (0.5 pp) 的对比说明了什么？\n\n### 5. 跨环境/跨模型验证\n- MATH 实验 (N=300): 4.3pp 差异不显著 (p=0.079) 但被用作论证——是否过度解读？\n- Llama pilot (N=10): 样本量极小，这个验证的价值有多大？\n- ALFWorld 数据 (Table 3) 从哪里来？论文中似乎缺少详细说明。\n\n### 6. 数据规模与代表性\n- 11/30 task types（19 个因超时排除）——论文是否充分讨论了选择偏差？\n- 单一模型 (Qwen2.5-7B-Instruct) + 单一环境的局限性\n- 20-40 episodes per task type 是否足够？\n\n请给出结构化审稿意见：Strengths、Weaknesses（分 Must-Fix / Should-Fix / Minor）、Questions、总体评分（1-5 分，3=borderline）。",
  "reviewer_id": "1",
  "project": "simgate-modular-routing",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "你是 Reviewer 1，负责审查**方法严谨性 + 实验充分性**。\n\n## 论文信息\n- **标题**: Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\n- **路径**: `projects/simgate-modular-routing/docs/paper/main.tex`（含 abstract.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, discussion.tex, conclusion.tex）\n- **目标 Venue**: EMNLP 2026 Main Conference (via ACL Rolling Review May 2026 cycle)\n- **Deadline**: 2026-05-25\n- **格式要求**: ACL style, 8 页正文, double-blind, 附录不计页数\n\n## 你的审查侧重\n\n### 1. Counterfactual 方法设计\n- Episode-level counterfactual 比较的有效性：pure-strategy 对比是否充分隔离了 modality 的影响？\n- 标注方案 (Algorithm 1) 的合理性：death-aware labeling 是否引入了偏差？\n- 97.4% step-level tie rate 的声明是否令人信服？这是否充分论证了 episode-level 标注的必要性？\n\n### 2. DAF Metric\n- DAF 的数学定义是否合理？分解公式 Δ_full ≈ δ·P + Δ_nd 的近似误差 (0.8%) 是否可接受？\n- DAF 随 P 单调递增是数学必然——论文是否充分承认这一点，避免将其作为经验发现？\n- 78.9% death-asymmetry label fraction 作为 penalty-independent companion metric 是否足够？\n\n### 3. 统计分析\n- 245 episodes, 11 task types 的样本量对支持 r=0.97 的声明是否足够？\n- Bootstrap CI、LOO 分析、Spearman 检验等统计方法使用是否恰当？\n- 95 个 non-tie labels 中 86:9 的极端不平衡——统计检验的功效是否足够？\n\n### 4. Router 训练诊断\n- Router balanced accuracy 57-59% 的解读是否合理？这是否真的表明 \"thin learnable signal\"？\n- Classification head 退化 (0% internal recall) 的分析是否充分？\n- Cross-split variance (5.2 pp) vs fixed-split variance (0.5 pp) 的对比说明了什么？\n\n### 5. 跨环境/跨模型验证\n- MATH 实验 (N=300): 4.3pp 差异不显著 (p=0.079) 但被用作论证——是否过度解读？\n- Llama pilot (N=10): 样本量极小，这个验证的价值有多大？\n- ALFWorld 数据 (Table 3) 从哪里来？论文中似乎缺少详细说明。\n\n### 6. 数据规模与代表性\n- 11/30 task types（19 个因超时排除）——论文是否充分讨论了选择偏差？\n- 单一模型 (Qwen2.5-7B-Instruct) + 单一环境的局限性\n- 20-40 episodes per task type 是否足够？\n\n请给出结构化审稿意见：Strengths、Weaknesses（分 Must-Fix / Should-Fix / Minor）、Questions、总体评分（1-5 分，3=borderline）。",
    "reviewer_id": "1",
    "project": "simgate-modular-routing",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 539 · 2026-05-15T15:20:22.657634+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 16856
}
```

</details>

---


### Tool call

_source line 540 · 2026-05-15T15:20:22.808760+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "你是 Reviewer 2，负责审查**新颖性 + 完整性 + 相关工作覆盖**。\n\n## 论文信息\n- **标题**: Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\n- **路径**: `projects/simgate-modular-routing/docs/paper/main.tex`（含 abstract.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, discussion.tex, conclusion.tex）\n- **目标 Venue**: EMNLP 2026 Main Conference (via ACL Rolling Review May 2026 cycle)\n- **Deadline**: 2026-05-25\n- **格式要求**: ACL style, 8 页正文, double-blind, 附录不计页数\n\n## 你的审查侧重\n\n### 1. 新颖性与贡献定位\n- \"Episode-level counterfactual analysis\" 作为方法论贡献的新颖性如何？与已有 counterfactual RL 解释方法 (Olson 2021, Gajcin 2023, Amitai 2024) 的本质区别是什么？\n- \"Death avoidance dominates routing signal\" 作为经验发现——这是否足够 surprising 且 generalizable 以支撑 EMNLP main conference？\n- DAF metric 的贡献独立性：是否只是一个简单的分解，还是有更深的方法论价值？\n- 论文的四个 contributions 是否清晰、独立、且每个都有足够支撑？\n\n### 2. 相关工作覆盖\n- Tool-use 文献 (Toolformer, ART, Chameleon, ToolkenGPT, ReTool) 覆盖是否充分？\n- Adaptive computation / routing 文献 (CogRouter, ARES, MoR, MTRouter) 是否遗漏重要工作？\n- Safe RL 文献是否充分？仅引 Garcia 2015 survey 是否够？\n- 2025-2026 最新相关工作 (tool-overuse-illusion, when2tool, tool-use-tax, to-call-or-not) 是否有遗漏？\n- 是否缺少 LLM agent benchmark 和 evaluation 方面的关键引用？\n- ScienceWorld 相关后续工作是否被引用？\n\n### 3. 论文结构与写作质量\n- Introduction 的 story arc 是否清晰：问题→方法→发现→贡献？\n- Method section 的形式化是否必要且清晰？\n- Experiments 和 Discussion 的边界是否合理？\n- Limitations section 是否充分覆盖了所有关键局限？\n- 整体篇幅分配是否合理（正文 vs 附录）？\n\n### 4. 格式合规性（EMNLP 2026 / ACL style）\n- `\\usepackage[review]{acl}` → 正确使用 review 模式\n- Double-blind：检查是否有任何 de-anonymization 线索（作者信息、仓库链接、致谢等）\n- 页数限制：正文是否在 8 页以内？\n- 引用格式：是否使用 natbib？`\\cite` 命令使用是否规范？\n- 图表质量：figure/table 是否清晰、有 caption、被正文引用？\n- 必须有 Limitations section（ACL 要求）\n\n### 5. 论文的\"隐含假设\"审查\n- \"Deterministic = 环境模拟器提供 ground-truth observations\" → 这在实际 agent 系统中是否现实？\n- \"Internal = ReAct paradigm\" → 为什么只测了 ReAct？其他推理范式（Tree of Thought, Reflexion 等）是否会改变结论？\n- 单一 backbone (Qwen2.5-7B) + 单一 environment (ScienceWorld) → generalizability 声明是否过强？\n\n请给出结构化审稿意见：Strengths、Weaknesses（分 Must-Fix / Should-Fix / Minor）、Questions、Missing References、总体评分（1-5 分，3=borderline）。",
  "reviewer_id": "2",
  "project": "simgate-modular-routing",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "你是 Reviewer 2，负责审查**新颖性 + 完整性 + 相关工作覆盖**。\n\n## 论文信息\n- **标题**: Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\n- **路径**: `projects/simgate-modular-routing/docs/paper/main.tex`（含 abstract.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, discussion.tex, conclusion.tex）\n- **目标 Venue**: EMNLP 2026 Main Conference (via ACL Rolling Review May 2026 cycle)\n- **Deadline**: 2026-05-25\n- **格式要求**: ACL style, 8 页正文, double-blind, 附录不计页数\n\n## 你的审查侧重\n\n### 1. 新颖性与贡献定位\n- \"Episode-level counterfactual analysis\" 作为方法论贡献的新颖性如何？与已有 counterfactual RL 解释方法 (Olson 2021, Gajcin 2023, Amitai 2024) 的本质区别是什么？\n- \"Death avoidance dominates routing signal\" 作为经验发现——这是否足够 surprising 且 generalizable 以支撑 EMNLP main conference？\n- DAF metric 的贡献独立性：是否只是一个简单的分解，还是有更深的方法论价值？\n- 论文的四个 contributions 是否清晰、独立、且每个都有足够支撑？\n\n### 2. 相关工作覆盖\n- Tool-use 文献 (Toolformer, ART, Chameleon, ToolkenGPT, ReTool) 覆盖是否充分？\n- Adaptive computation / routing 文献 (CogRouter, ARES, MoR, MTRouter) 是否遗漏重要工作？\n- Safe RL 文献是否充分？仅引 Garcia 2015 survey 是否够？\n- 2025-2026 最新相关工作 (tool-overuse-illusion, when2tool, tool-use-tax, to-call-or-not) 是否有遗漏？\n- 是否缺少 LLM agent benchmark 和 evaluation 方面的关键引用？\n- ScienceWorld 相关后续工作是否被引用？\n\n### 3. 论文结构与写作质量\n- Introduction 的 story arc 是否清晰：问题→方法→发现→贡献？\n- Method section 的形式化是否必要且清晰？\n- Experiments 和 Discussion 的边界是否合理？\n- Limitations section 是否充分覆盖了所有关键局限？\n- 整体篇幅分配是否合理（正文 vs 附录）？\n\n### 4. 格式合规性（EMNLP 2026 / ACL style）\n- `\\usepackage[review]{acl}` → 正确使用 review 模式\n- Double-blind：检查是否有任何 de-anonymization 线索（作者信息、仓库链接、致谢等）\n- 页数限制：正文是否在 8 页以内？\n- 引用格式：是否使用 natbib？`\\cite` 命令使用是否规范？\n- 图表质量：figure/table 是否清晰、有 caption、被正文引用？\n- 必须有 Limitations section（ACL 要求）\n\n### 5. 论文的\"隐含假设\"审查\n- \"Deterministic = 环境模拟器提供 ground-truth observations\" → 这在实际 agent 系统中是否现实？\n- \"Internal = ReAct paradigm\" → 为什么只测了 ReAct？其他推理范式（Tree of Thought, Reflexion 等）是否会改变结论？\n- 单一 backbone (Qwen2.5-7B) + 单一 environment (ScienceWorld) → generalizability 声明是否过强？\n\n请给出结构化审稿意见：Strengths、Weaknesses（分 Must-Fix / Should-Fix / Minor）、Questions、Missing References、总体评分（1-5 分，3=borderline）。",
    "reviewer_id": "2",
    "project": "simgate-modular-routing",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 541 · 2026-05-15T15:20:24.244204+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1435
}
```

</details>

---


### Assistant

_source line 542 · 2026-05-15T15:20:31.296790+00:00_

Round 1 任务已分配：

| Reviewer | 侧重 | 状态 |
|----------|------|------|
| Reviewer 1 | 方法严谨性 + 实验充分性 | 已派发，等待回复 |
| Reviewer 2 | 新颖性 + 完整性 + 相关工作 | 已派发，等待回复 |

等待两位 Reviewer 的独立初审结果返回，之后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 49

## Round 49

2 recorded events


### User

_source line 543 · 2026-05-15T15:25:04.571260+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿意见：Round 1

**论文**: Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld
**审查侧重**: 新颖性 + 完整性 + 相关工作覆盖

---

## 总体评分

| 维度 | 分数 | 理由 |
|------|------|------|
| Soundness | 3/5 | 主要 claim 在 ScienceWorld 内有充分支撑（bootstrap CI、LOO、Spearman），但 generalizability claim 超出数据支撑 |
| Excitement | 3/5 | "路由信号 ≈ 死亡回避"有洞察价值，但给定 -100 penalty + 42.9% death rate，结论有较强可预测性 |
| Overall | 3/5 (Findings) | Borderline——经验发现有价值但方法论贡献有限，generalizability 受制于实验范围 |
| Reproducibility | 4/5 | 超参数、分割、seed 均详细报告，但 blind review 下无代码/数据 |
| Confidence | 4/5 | 仔细通读全文含附录 |

---

## Must-Fix (3 items)

**N1** [critical] DAF 的 penalty-sensitivity 削弱"~90%" headline claim：DAF 随 P 单调递增是数学必然。P=10 → 46.4%，P=25 → 68.4%。标题/abstract 以"~90%"为 headline 完全依赖 P=100 这个特定设置。建议将 penalty-independent 的 78.9% death-asymmetry label fraction 提升为 primary metric。

**N2** [critical] 63% task types 被排除导致 selection bias：19/30 task types 因 30-step timeout 排除——这些长 horizon task 恰恰可能有 diverse routing signal。Introduction/conclusion 的 framing 未充分 qualify 此限制。

**N3** [critical] Safe RL 文献仅引 Garcia 2015 一篇综述（11 年前）：核心 insight 是"router = safety critic"，但未引用 CPO、safety Q-functions 等 safety critic 相关文献，文献基础不足。

## Should-Fix (5 items)

**W1** 方法论新颖性有限——episode-level counterfactual 本质是 paired A/B testing，DAF 是简单分解公式。

**W2** Cross-model pilot (N=10, 2 tasks) 过小——不应作为 Contribution 3 的一部分支撑"generalizes across model families"。

**W3** 缺少 Reflexion (Shinn 2023)、RouteLLM (Ong 2024)、tool-learning survey (Qu 2024)、ScienceWorld follow-up 等重要引用。

**W4** 仅测试 ReAct——Reflexion/ToT 等可能显著降低 death rate，改变 DAF。Limitations 中未讨论。

**W5** ALFWorld 分析 (Table 3) 缺乏方法论细节——deterministic 策略定义、数据收集过程均未交代。

## Minor (6 items)

M1: retool-2026 bib key 与实际年份 2025 不一致。M2: dynathink-2025 first author mismatch。M3: Related Work 位于 Experiments 之后（少见但合规）。M4: Contribution 1 和 2 有重叠。M5: Abstract 中"90.41%"精度暗示过高确信度。M6: Ethics 提及 RTX 5090 可能影响 anonymity。

## 主要优势

S1: 研究问题聚焦且定位精准（"what drives routing signal"vs"how to route"）。S2: 统计分析扎实透明（bootstrap、LOO、Spearman、seed robustness）。S3: MATH 实验提供有效 negative control。S4: Limitations section 异常坦诚详尽。S5: 写作清晰，story arc 流畅。

## 建议

以 Findings paper 水准看，本文质量合格——经验发现有价值、分析扎实。但冲 main conference 需要：(1) 扩大实验范围（更多 task types、更多模型、更多推理范式）以支撑 generalizability，(2) 补充 safe RL 文献以巩固 "router as safety critic" 的理论定位，(3) 重新 frame headline metric 以避免对 penalty-specific DAF 的过度依赖。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 544 · 2026-05-15T15:25:23.742795+00:00_

对话上下文仍在——服务器重启前我已完成以下步骤：

1. 读取论文全文（main.tex + 所有章节 + references.bib）
2. 搜索 EMNLP 2026 CFP（ACL style, 8 页正文, double-blind, ARR May 25 截止）
3. 分配 2 名 Reviewer（R1: 方法严谨性+实验充分性, R2: 新颖性+完整性+相关工作）

**当前状态**：Reviewer 2 已提交审稿意见（Overall 3/5 borderline），Reviewer 1 尚未返回。

收到 Reviewer 2 意见，记录要点：
- 3 个 Must-Fix：DAF headline 过度依赖 P=100、63% task types 排除导致 selection bias、Safe RL 文献不足
- 5 个 Should-Fix：方法论新颖性有限、cross-model pilot 过小、缺重要引用、仅测 ReAct、ALFWorld 细节缺失
- 6 个 Minor

等待 Reviewer 1 返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 50

## Round 50

6 recorded events


### User

_source line 545 · 2026-05-15T15:25:26.270128+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

总结：Overall 3/5 (Findings level)。3 个 Must-Fix：(1) DAF "~90%" headline 过度依赖特定 penalty 值 P=100，应以 penalty-independent 的 78.9% death-asymmetry fraction 为主指标；(2) 63% task types 被排除构成 selection bias；(3) Safe RL 文献仅引一篇 2015 综述，无法支撑"router = safety critic"的核心 insight。5 个 Should-Fix 涉及方法论新颖性有限、cross-model pilot 过小、缺少 Reflexion/RouteLLM 等关键引用、仅测试 ReAct、ALFWorld 细节缺失。优势在于研究问题聚焦、统计分析扎实、MATH negative control 有效、Limitations 坦诚。

---

[Reviewer 1 审稿意见]:
## Reviewer 1 — Round 1 审稿意见

**论文**: Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld
**审查侧重**: 方法严谨性 + 实验充分性

---

## 总体评分

**Overall**: 3/5（Borderline — Accept to Findings）
**一句话总结**: 方法学贡献扎实（episode-level counterfactual + DAF metric），核心发现在特定设定下令人信服，但证据基础过窄（单环境单模型为主）、router诊断结论存在混淆变量、ALFWorld数据来源不明，限制了结论的普适性和影响力。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 核心分解方法论严谨，统计分析扎实（bootstrap/LOO/Spearman），但router诊断结论（Contribution 4）的数据量混淆变量未充分分离，ALFWorld数据缺少方法论描述 |
| Excitement | 3.5/5 | "routing signal 的本质是什么"这个问题有真正的研究价值，episode-level counterfactual methodology 有推广潜力，但单环境结论的窄泛化性折扣 |
| Reproducibility | 3.5/5 | 超参数、种子、数据划分均已披露（Appendix D），但ALFWorld实验完全缺少细节，未提及代码/数据开源计划 |
| Overall Assessment | 3/5 | 方法论贡献值得发表（Findings级别），但must-fix问题解决前不具备main conference竞争力 |
| Confidence | 4/5 | 全文（含附录）逐节精读，引用已交叉核验，统计分析已核查 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] ALFWorld 数据来源与方法论缺失
- 具体位置：§5 Discussion, Table 3
- 问题：Table 3 呈现 ALFWorld 数据（N=135, 25.9% det-preferred, 1.5% int-preferred, 72.6% no-preference），并作为跨环境证据，但论文从未描述该数据的收集方法——使用了什么模型？deterministic modality 具体指什么？episode 长度限制？labeling 是否沿用 Algorithm 1？脚注仅提及"ALFWorld's deterministic advantage stems from action-space pruning (capability gap)"，但这个判断本身也缺乏支撑分析。
- 为什么影响接收：不可追溯的数据直接削弱跨环境验证的可信度。
- 建议：补充完整的 ALFWorld 实验方法，或将其移至 Appendix 并降低权重。

**N2** [critical] Router 训练诊断结论与数据量不足存在根本性混淆
- 具体位置：§3.3, Contribution 4
- 问题：论文将 router 低准确率（57-59%）解读为"thin learnable signal"。但训练集仅 81 样本（internal-preferred 仅约 8 个），验证集 14 个。在此数据规模下，以下因素无法与"信号稀薄"区分：(1) 极端类别不平衡（86:9），(2) 数据量不足以训练 1.7B 模型，(3) episode-to-step 粒度失配。Classification head 退化到 0% internal recall 在仅 ~8 正例下是预期行为。
- 为什么影响接收：Contribution 4 是四个贡献之一，核心论据不可靠。
- 建议：明确承认数据量不足是混淆变量，将 router 诊断降级为"初步观察"，或增加数据量消融实验。

**N3** [critical] 63% task types 排除——选择偏差讨论不足
- 具体位置：§2.2, Appendix B, Limitations
- 问题：19/30 task types（63%）因超时被排除。被排除任务可能有不同的 routing signal 构成。论文核心声明"~90% routing signal"仅适用于 11/30 可短期完成的任务。
- 为什么影响接收：标题"Dominant Routing Signal"需要更强的限定词。
- 建议：在 title/abstract/conclusion 中限定为短期任务；增加对排除任务特征的分析；讨论增加 step budget 的影响。

---

## Should-Fix 问题

**W1** [warning] MATH 结果 (p=0.079) 的不对称使用
- Abstract 和 Conclusion 呈现 label distribution inversion (86:9 → 30:17) 比 §5 正文更强势，但 p=0.079 未达显著性。构成选择性显著性标准。
- 建议：Abstract/Conclusion 一致标注"not statistically significant"。

**W2** [warning] Llama pilot (N=10) 作为贡献过度包装
- 10 episodes 几乎无统计功效，不应与 MATH (N=300) 并列为 Contribution 3 "Cross-context validation"。
- 建议：从 Contribution list 移除，仅在正文保留为方向性观察。

**W3** [warning] Pure-strategy → mixed-strategy gap 未分析
- 实际部署是 mixed routing，但 labeling 基于 pure-strategy。Death 在 pure-internal 下发生不等于 mixed routing 也会。DAgger citation 不够——需要分析 death 发生时间步以评估 mixed routing 可行性。

**W4** [warning] DAF=90.41% (P=100) 呈现权重过高
- P=10 时 DAF 仅 46.4%。78.9% death-asymmetry label fraction 作为 penalty-independent 指标应在 Abstract 中获得更高呈现权重。

**W5** [warning] r=0.97 的结构性耦合在 Abstract/Contributions 中披露不足
- Δ_full ≈ δ·P + Δ_nd 且 δ·P 占 90% 时，δ 与 Δ_full 的高相关是数学同义反复，非经验发现。Abstract 应加限定语。

---

## 小问题

- bib `retool-2026` key 与 year (2025) 不一致
- bib `dynathink-2025` author 顺序可能有误（OpenAlex 匹配差异）
- 未提及代码/数据开源计划
- `find-non-living-thing` 给了 40 episodes（其他 20），未解释原因

---

## 主要优势

1. 研究问题定位精准——"what drives routing value"是被忽视的先验问题
2. Episode-level counterfactual + DAF metric 可迁移到其他环境
3. 统计分析严谨且透明（bootstrap/LOO/Spearman/penalty sensitivity），主动披露结构性耦合
4. Contemporary related work 覆盖出色（多篇 2026 concurrent work）
5. 写作质量高，Limitations 坦诚全面

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 546 · 2026-05-15T15:25:48.766947+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "以下是 Reviewer 2 的完整 Round 1 审稿意见。请逐条回应：对每一条用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见：Round 1\n\n**审查侧重**: 新颖性 + 完整性 + 相关工作覆盖\n\n### 总体评分\nOverall: 3/5 (Findings level)。Soundness 3/5, Excitement 3/5, Reproducibility 4/5, Confidence 4/5。\n\n### Must-Fix (3 items)\n\n**N1** [critical] DAF 的 penalty-sensitivity 削弱\"~90%\" headline claim：DAF 随 P 单调递增是数学必然。P=10 → 46.4%，P=25 → 68.4%。标题/abstract 以\"~90%\"为 headline 完全依赖 P=100 这个特定设置。建议将 penalty-independent 的 78.9% death-asymmetry label fraction 提升为 primary metric。\n\n**N2** [critical] 63% task types 被排除导致 selection bias：19/30 task types 因 30-step timeout 排除——这些长 horizon task 恰恰可能有 diverse routing signal。Introduction/conclusion 的 framing 未充分 qualify 此限制。\n\n**N3** [critical] Safe RL 文献仅引 Garcia 2015 一篇综述（11 年前）：核心 insight 是\"router = safety critic\"，但未引用 CPO、safety Q-functions 等 safety critic 相关文献，文献基础不足。\n\n### Should-Fix (5 items)\n\n**W1** 方法论新颖性有限——episode-level counterfactual 本质是 paired A/B testing，DAF 是简单分解公式。\n\n**W2** Cross-model pilot (N=10, 2 tasks) 过小——不应作为 Contribution 3 的一部分支撑\"generalizes across model families\"。\n\n**W3** 缺少 Reflexion (Shinn 2023)、RouteLLM (Ong 2024)、tool-learning survey (Qu 2024)、ScienceWorld follow-up 等重要引用。\n\n**W4** 仅测试 ReAct——Reflexion/ToT 等可能显著降低 death rate，改变 DAF。Limitations 中未讨论。\n\n**W5** ALFWorld 分析 (Table 3) 缺乏方法论细节——deterministic 策略定义、数据收集过程均未交代。\n\n### Minor (6 items)\nM1: retool-2026 bib key 与实际年份 2025 不一致。M2: dynathink-2025 first author mismatch。M3: Related Work 位于 Experiments 之后（少见但合规）。M4: Contribution 1 和 2 有重叠。M5: Abstract 中\"90.41%\"精度暗示过高确信度。M6: Ethics 提及 RTX 5090 可能影响 anonymity。\n\n### 主要优势\nS1: 研究问题聚焦且定位精准。S2: 统计分析扎实透明。S3: MATH 实验提供有效 negative control。S4: Limitations section 异常坦诚详尽。S5: 写作清晰，story arc 流畅。",
  "reviewer_id": "1",
  "project": "simgate-modular-routing",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "以下是 Reviewer 2 的完整 Round 1 审稿意见。请逐条回应：对每一条用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿意见：Round 1\n\n**审查侧重**: 新颖性 + 完整性 + 相关工作覆盖\n\n### 总体评分\nOverall: 3/5 (Findings level)。Soundness 3/5, Excitement 3/5, Reproducibility 4/5, Confidence 4/5。\n\n### Must-Fix (3 items)\n\n**N1** [critical] DAF 的 penalty-sensitivity 削弱\"~90%\" headline claim：DAF 随 P 单调递增是数学必然。P=10 → 46.4%，P=25 → 68.4%。标题/abstract 以\"~90%\"为 headline 完全依赖 P=100 这个特定设置。建议将 penalty-independent 的 78.9% death-asymmetry label fraction 提升为 primary metric。\n\n**N2** [critical] 63% task types 被排除导致 selection bias：19/30 task types 因 30-step timeout 排除——这些长 horizon task 恰恰可能有 diverse routing signal。Introduction/conclusion 的 framing 未充分 qualify 此限制。\n\n**N3** [critical] Safe RL 文献仅引 Garcia 2015 一篇综述（11 年前）：核心 insight 是\"router = safety critic\"，但未引用 CPO、safety Q-functions 等 safety critic 相关文献，文献基础不足。\n\n### Should-Fix (5 items)\n\n**W1** 方法论新颖性有限——episode-level counterfactual 本质是 paired A/B testing，DAF 是简单分解公式。\n\n**W2** Cross-model pilot (N=10, 2 tasks) 过小——不应作为 Contribution 3 的一部分支撑\"generalizes across model families\"。\n\n**W3** 缺少 Reflexion (Shinn 2023)、RouteLLM (Ong 2024)、tool-learning survey (Qu 2024)、ScienceWorld follow-up 等重要引用。\n\n**W4** 仅测试 ReAct——Reflexion/ToT 等可能显著降低 death rate，改变 DAF。Limitations 中未讨论。\n\n**W5** ALFWorld 分析 (Table 3) 缺乏方法论细节——deterministic 策略定义、数据收集过程均未交代。\n\n### Minor (6 items)\nM1: retool-2026 bib key 与实际年份 2025 不一致。M2: dynathink-2025 first author mismatch。M3: Related Work 位于 Experiments 之后（少见但合规）。M4: Contribution 1 和 2 有重叠。M5: Abstract 中\"90.41%\"精度暗示过高确信度。M6: Ethics 提及 RTX 5090 可能影响 anonymity。\n\n### 主要优势\nS1: 研究问题聚焦且定位精准。S2: 统计分析扎实透明。S3: MATH 实验提供有效 negative control。S4: Limitations section 异常坦诚详尽。S5: 写作清晰，story arc 流畅。",
    "reviewer_id": "1",
    "project": "simgate-modular-routing",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 547 · 2026-05-15T15:25:59.229190+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 10462
}
```

</details>

---


### Tool call

_source line 548 · 2026-05-15T15:25:59.581125+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "以下是 Reviewer 1 的完整 Round 1 审稿意见。请逐条回应：对每一条用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 — Round 1 审稿意见\n\n**审查侧重**: 方法严谨性 + 实验充分性\n\n### 总体评分\nOverall: 3/5 (Borderline — Accept to Findings)。Soundness 3.5/5, Excitement 3.5/5, Reproducibility 3.5/5, Confidence 4/5。\n\n### Must-Fix (3 items)\n\n**N1** [critical] ALFWorld 数据来源与方法论缺失：Table 3 呈现 ALFWorld 数据（N=135, 25.9% det-preferred, 1.5% int-preferred, 72.6% no-preference），但论文从未描述该数据的收集方法——使用了什么模型？deterministic modality 具体指什么？episode 长度限制？labeling 是否沿用 Algorithm 1？脚注仅提及\"ALFWorld's deterministic advantage stems from action-space pruning (capability gap)\"，但这个判断本身也缺乏支撑分析。不可追溯的数据直接削弱跨环境验证的可信度。\n\n**N2** [critical] Router 训练诊断结论与数据量不足存在根本性混淆：论文将 router 低准确率（57-59%）解读为\"thin learnable signal\"。但训练集仅 81 样本（internal-preferred 仅约 8 个），验证集 14 个。在此数据规模下，以下因素无法与\"信号稀薄\"区分：(1) 极端类别不平衡（86:9），(2) 数据量不足以训练 1.7B 模型，(3) episode-to-step 粒度失配。Classification head 退化到 0% internal recall 在仅 ~8 正例下是预期行为。Contribution 4 是四个贡献之一，核心论据不可靠。\n\n**N3** [critical] 63% task types 排除——选择偏差讨论不足：19/30 task types（63%）因超时被排除。被排除任务可能有不同的 routing signal 构成。标题\"Dominant Routing Signal\"需要更强的限定词。\n\n### Should-Fix (5 items)\n\n**W1** MATH 结果 (p=0.079) 的不对称使用：Abstract 和 Conclusion 呈现 label distribution inversion (86:9 → 30:17) 比 §5 正文更强势，但 p=0.079 未达显著性。构成选择性显著性标准。\n\n**W2** Llama pilot (N=10) 作为贡献过度包装：10 episodes 几乎无统计功效，不应与 MATH (N=300) 并列为 Contribution 3。\n\n**W3** Pure-strategy → mixed-strategy gap 未分析：实际部署是 mixed routing，但 labeling 基于 pure-strategy。Death 在 pure-internal 下发生不等于 mixed routing 也会。DAgger citation 不够——需要分析 death 发生时间步以评估 mixed routing 可行性。\n\n**W4** DAF=90.41% (P=100) 呈现权重过高：P=10 时 DAF 仅 46.4%。78.9% death-asymmetry label fraction 作为 penalty-independent 指标应在 Abstract 中获得更高呈现权重。\n\n**W5** r=0.97 的结构性耦合在 Abstract/Contributions 中披露不足：Δ_full ≈ δ·P + Δ_nd 且 δ·P 占 90% 时，δ 与 Δ_full 的高相关是数学同义反复，非经验发现。Abstract 应加限定语。\n\n### 小问题\n- bib key/year 不一致\n- 未提及代码/数据开源计划\n- find-non-living-thing 给了 40 episodes（其他 20），未解释原因\n\n### 主要优势\n1. 研究问题定位精准\n2. Episode-level counterfactual + DAF metric 可迁移\n3. 统计分析严谨且透明\n4. Contemporary related work 覆盖出色\n5. 写作质量高，Limitations 坦诚全面",
  "reviewer_id": "2",
  "project": "simgate-modular-routing",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "以下是 Reviewer 1 的完整 Round 1 审稿意见。请逐条回应：对每一条用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 — Round 1 审稿意见\n\n**审查侧重**: 方法严谨性 + 实验充分性\n\n### 总体评分\nOverall: 3/5 (Borderline — Accept to Findings)。Soundness 3.5/5, Excitement 3.5/5, Reproducibility 3.5/5, Confidence 4/5。\n\n### Must-Fix (3 items)\n\n**N1** [critical] ALFWorld 数据来源与方法论缺失：Table 3 呈现 ALFWorld 数据（N=135, 25.9% det-preferred, 1.5% int-preferred, 72.6% no-preference），但论文从未描述该数据的收集方法——使用了什么模型？deterministic modality 具体指什么？episode 长度限制？labeling 是否沿用 Algorithm 1？脚注仅提及\"ALFWorld's deterministic advantage stems from action-space pruning (capability gap)\"，但这个判断本身也缺乏支撑分析。不可追溯的数据直接削弱跨环境验证的可信度。\n\n**N2** [critical] Router 训练诊断结论与数据量不足存在根本性混淆：论文将 router 低准确率（57-59%）解读为\"thin learnable signal\"。但训练集仅 81 样本（internal-preferred 仅约 8 个），验证集 14 个。在此数据规模下，以下因素无法与\"信号稀薄\"区分：(1) 极端类别不平衡（86:9），(2) 数据量不足以训练 1.7B 模型，(3) episode-to-step 粒度失配。Classification head 退化到 0% internal recall 在仅 ~8 正例下是预期行为。Contribution 4 是四个贡献之一，核心论据不可靠。\n\n**N3** [critical] 63% task types 排除——选择偏差讨论不足：19/30 task types（63%）因超时被排除。被排除任务可能有不同的 routing signal 构成。标题\"Dominant Routing Signal\"需要更强的限定词。\n\n### Should-Fix (5 items)\n\n**W1** MATH 结果 (p=0.079) 的不对称使用：Abstract 和 Conclusion 呈现 label distribution inversion (86:9 → 30:17) 比 §5 正文更强势，但 p=0.079 未达显著性。构成选择性显著性标准。\n\n**W2** Llama pilot (N=10) 作为贡献过度包装：10 episodes 几乎无统计功效，不应与 MATH (N=300) 并列为 Contribution 3。\n\n**W3** Pure-strategy → mixed-strategy gap 未分析：实际部署是 mixed routing，但 labeling 基于 pure-strategy。Death 在 pure-internal 下发生不等于 mixed routing 也会。DAgger citation 不够——需要分析 death 发生时间步以评估 mixed routing 可行性。\n\n**W4** DAF=90.41% (P=100) 呈现权重过高：P=10 时 DAF 仅 46.4%。78.9% death-asymmetry label fraction 作为 penalty-independent 指标应在 Abstract 中获得更高呈现权重。\n\n**W5** r=0.97 的结构性耦合在 Abstract/Contributions 中披露不足：Δ_full ≈ δ·P + Δ_nd 且 δ·P 占 90% 时，δ 与 Δ_full 的高相关是数学同义反复，非经验发现。Abstract 应加限定语。\n\n### 小问题\n- bib key/year 不一致\n- 未提及代码/数据开源计划\n- find-non-living-thing 给了 40 episodes（其他 20），未解释原因\n\n### 主要优势\n1. 研究问题定位精准\n2. Episode-level counterfactual + DAF metric 可迁移\n3. 统计分析严谨且透明\n4. Contemporary related work 覆盖出色\n5. 写作质量高，Limitations 坦诚全面",
    "reviewer_id": "2",
    "project": "simgate-modular-routing",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 549 · 2026-05-15T15:26:00.889853+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1308
}
```

</details>

---


### Assistant

_source line 550 · 2026-05-15T15:26:04.804359+00:00_

交叉分享已发出，等待两位 Reviewer 的逐条回应。收到后将进行收敛判断，决定是否需要下一轮或直接汇总最终报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 51

## Round 51

2 recorded events


### User

_source line 551 · 2026-05-15T15:26:06.310789+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

总结：论文在方法论上有实在的贡献（episode-level counterfactual + DAF metric），统计分析也做得扎实。但存在三个 must-fix 问题——ALFWorld 数据缺少方法论描述、router 诊断结论与数据量不足无法区分、63% task types 被排除导致选择偏差——限制了当前版本的 main conference 竞争力。给出 Overall 3/5（Findings 级别），等待修订后可能提升。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 552 · 2026-05-15T15:26:11.324429+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 52

## Round 52

2 recorded events


### User

_source line 553 · 2026-05-15T15:27:37.689901+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 — 对 Reviewer 2 Round 1 意见的交叉回应

### Must-Fix

**[AGREE] R2-N1: DAF penalty-sensitivity 削弱 headline claim**
同意。与我的 W4 一致。Appendix E (Table 5) 显示 P=10 → DAF=46.4%。"~90%" 完全由 P=100 决定。78.9% death-asymmetry label fraction 应提升为 primary metric。

**[AGREE] R2-N2: 63% task types 排除导致 selection bias**
同意。与我的 N3 一致。19/30 长 horizon tasks 被排除，标题 "Dominant Routing Signal" 缺乏 scope 限定。

**[REBUT] R2-N3: Safe RL 文献仅引 Garcia 2015 一篇**
不同意列为 critical。论文的贡献是分析性的，非算法性的。"Router = safety critic" 是 §5 Discussion 的 implication，非 primary contribution（Contribution 1-4 均非 safe RL）。Garcia (2015) 作为综述引用在 conceptual connection 层面充分。建议降级为 should-fix：补充 1-2 篇 safety critic 代表性工作即可，不应要求全面覆盖 safe RL 子领域。

### Should-Fix

**[AGREE with nuance] R2-W1: 方法论新颖性有限**
部分同意。组件简单，但应用层面有新颖性：识别 step-level degeneracy（97.4% tie rate, §2.2）并将 counterfactual 方法从 action-level perturbation 推进到 episode-level modality comparison。属于 "well-designed analytical framework" 而非 deep methodological contribution。

**[AGREE] R2-W2: Cross-model pilot N=10 过小**
完全同意。与我的 W2 一致。

**[AGREE with caveats] R2-W3: 缺少 Reflexion、RouteLLM 等引用**
RouteLLM 最为紧迫（直接做 routing），Reflexion 次之（与 W4 策略泛化关联）。ScienceWorld follow-up 如果存在则遗漏严重。

**[AGREE] R2-W4: 仅测试 ReAct，未讨论其他 reasoning 策略**
同意且补充：Reflexion 的 self-correction 或 ToT 的 backtracking 可能显著降低 death rate → 降低 DAF。论文的发现可能是 ReAct 的 single-pass vulnerability 的特性。Limitations 讨论了 model scale 影响但完全未讨论 reasoning strategy 影响。应补充。

**[AGREE] R2-W5: ALFWorld 缺乏方法论细节**
完全同意。与我的 N1 一致（我列为 critical）。

### Minor

**[AGREE]** R2-M1, M2: bib 细节问题。
**[REBUT]** R2-M3: Related Work 在 Experiments 后面是合理的叙事结构，ACL 不规定 section 顺序。
**[AGREE partially]** R2-M4: Contribution 1/2 有轻微重叠但概念可区分（method vs finding）。
**[AGREE]** R2-M5: "90.41%" 应改为 "~90%"。
**[AGREE partially]** R2-M6: RTX 5090 去匿名化风险低但修复成本也低，建议泛化。

### 两位 Reviewer 的共识汇总

以下问题被 R1 和 R2 独立提出，构成强共识：
1. **DAF penalty-sensitivity → 78.9% 应为 primary metric**（R1-W4, R2-N1）
2. **63% task types 排除的 selection bias**（R1-N3, R2-N2）
3. **ALFWorld 数据来源缺失**（R1-N1, R2-W5）
4. **Llama pilot N=10 过小不应作为 contribution**（R1-W2, R2-W2）
5. **bib 细节问题**（R1-Minor, R2-M1/M2）

R1 额外提出但 R2 未覆盖：router 训练数据量混淆变量（R1-N2）、r=0.97 结构性耦合（R1-W5）、pure-strategy vs mixed-strategy gap（R1-W3）、MATH p=0.079 不对称使用（R1-W1）。

R2 额外提出但 R1 未覆盖：safe RL 文献不足（R2-N3，我 rebut 为 should-fix）、reasoning strategy 泛化（R2-W4）、RouteLLM/Reflexion 等引用缺失（R2-W3）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 554 · 2026-05-15T15:27:48.735123+00:00_

Reviewer 1 的交叉回应已收到。等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 53

## Round 53

10 recorded events


### User

_source line 555 · 2026-05-15T15:27:49.701639+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。

**两位 Reviewer 的核心共识**：DAF penalty-sensitivity（78.9% 应为主指标）、63% task types 排除的选择偏差、ALFWorld 数据缺少方法论、Llama pilot 过小。我对 R2-N3（safe RL 文献不足）提出了 rebut——认为应从 critical 降级为 should-fix，因为论文的贡献是分析性而非算法性的。

---

[Reviewer 2 审稿意见]:
## Reviewer 2 — 对 Reviewer 1 Round 1 的逐条回应

### Must-Fix

- **[AGREE] R1-N1 (ALFWorld 方法论缺失)**: 完全同意，与我的 W5 一致。Table 3 的 ALFWorld 数据完全不可追溯。
- **[AGREE] R1-N2 (Router diagnostic vs data insufficiency)**: R1 最有力的 critique。81 训练样本、~8 internal-preferred、14 验证样本——无法区分"signal thin"和"data insufficient"。Contribution 4 存在根本缺陷。我在 Round 1 中对此关注不足。
- **[AGREE] R1-N3 (63% task 排除)**: 与我的 N2 一致。

### Should-Fix

- **[AGREE] R1-W1 (MATH p=0.079)**: 部分同意。Abstract 确实标注了"non-significant"，但"routing signal vanishes"的措辞仍过强。
- **[AGREE] R1-W2 (Llama N=10)**: 与我的 W2 一致。
- **[AGREE] R1-W3 (Pure→mixed strategy gap)**: 重要方法论问题，我在 Round 1 中遗漏。Death timing 分析缺失影响 DAF 的实际应用价值评估。
- **[REBUT] R1-W4 (DAF 呈现权重)**: 原则同意问题本身，但我认为应提升为 **Must-Fix**（我列为 N1），因为 P=10 时 DAF=46.4% 直接挑战论文标题的"dominant"声称。R1 列为 Should-Fix 低估了严重性。
- **[AGREE] R1-W5 (r=0.97 structural coupling)**: §4.1 有 caveat 但 Abstract/Contributions 未携带。

### 两位 Reviewer 共识

独立一致的问题：ALFWorld 缺失、63% task 排除、DAF penalty-sensitivity、Llama pilot 过小、r=0.97 coupling。

R1 独有重要 critique：router diagnostic confound (N2)、pure-to-mixed gap (W3)。
R2 独有重要 critique：Safe RL 文献不足 (N3)、缺少 Reflexion/RouteLLM (W3)、仅测 ReAct (W4)。

**总体判断维持 3/5 (Findings)**：经验发现有价值，但 generalizability claim 超出数据支撑，方法论贡献有限。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 556 · 2026-05-15T15:28:15.023089+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__submit_review_report_to_research_director",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__submit_review_report_to_research_director",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 557 · 2026-05-15T15:28:15.023576+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 558 · 2026-05-15T15:28:16.532188+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 559 · 2026-05-15T15:28:16.633159+00:00_

1	- id: "R6-C1"
2	  summary: "DAF penalty-dependence — need range 46-95% in Abstract + DAF(P) formula in main text + 78.9% co-equal"
3	  category: method
4	  severity: critical
5	  status: resolved
6	  first_raised_round: 4
7	  last_seen_round: 6
8	  mentions:
9	    - round: 6
10	      reviewers: [1, 2]
11	      note: "Fresh reviewers want full range + formula + dual reporting."
12	  action_items:
13	    - round: 6
14	      action: "Abstract/Intro/§3.3/Conclusion dual reporting + DAF(P) formula in method.tex"
15	      assigned_to: main_agent
16	      status: done
17	  resolution: "Abstract has dual reporting (78.9% + DAF 46-95%). method.tex has DAF(P) formula. Intro/Conclusion synced."
18	  resolution_round: 6
19	
20	- id: "R6-C2"
21	  summary: "Missing counterfactual-in-RL literature paragraph"
22	  category: writing
23	  severity: critical
24	  status: resolved
25	  first_raised_round: 6
26	  last_seen_round: 6
27	  mentions:
28	    - round: 6
29	      reviewers: [1, 2]
30	      note: "Paper uses 'counterfactual' in title, must contextualize."
31	  action_items:
32	    - round: 6
33	      action: "Add paragraph + 3 refs (Amitai AAAI'24, Gajcin AAMAS'23, Olson AIJ'21)"
34	      assigned_to: main_agent
35	      status: done
36	  resolution: "related_work.tex has 'prospective paired comparison vs post-hoc explanation' paragraph with all 3 citations."
37	  resolution_round: 6
38	
39	- id: "R6-W1"
40	  summary: "'near-perfect correlation' overclaims given n=11 + structural coupling"
41	  category: writing
42	  severity: warning
43	  status: resolved
44	  first_raised_round: 6
45	  last_seen_round: 6
46	  mentions:
47	    - round: 6
48	      reviewers: [1, 2]
49	      note: "High r partly mathematical due to penalty coupling."
50	  action_items:
51	    - round: 6
52	      action: "'near-perfect' → 'strong positive' + structural coupling caveat + redirect to 78.9%"
53	      assigned_to: main_agent
54	      status: done
55	  resolution: "experiments.tex uses 'strong posit
…[truncated 4348 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 560 · 2026-05-15T15:31:44.999831+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "simgate-modular-routing",
  "issues_yaml": "- id: \"R6-C1\"\n  summary: \"DAF penalty-dependence — headline ~90% anchored to P=100, 78.9% not co-equal\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 4\n  last_seen_round: 7\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"Fresh reviewers want full range + formula + dual reporting.\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"Resurfaced. Abstract still leads with DAF=90.41%. 78.9% present but not co-equal. R2 escalated to Must-Fix, R1 agreed on substance. Title 'Dominant' + P=10→46.4% tension unresolved.\"\n  action_items:\n    - round: 6\n      action: \"Abstract/Intro/§3.3/Conclusion dual reporting + DAF(P) formula in method.tex\"\n      assigned_to: main_agent\n      status: done\n    - round: 7\n      action: \"Promote 78.9% to primary metric in Abstract/Title; relegate DAF to secondary with explicit P-dependence caveat\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-C2\"\n  summary: \"Missing counterfactual-in-RL literature paragraph\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"Paper uses 'counterfactual' in title, must contextualize.\"\n  action_items:\n    - round: 6\n      action: \"Add paragraph + 3 refs (Amitai AAAI'24, Gajcin AAMAS'23, Olson AIJ'21)\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"related_work.tex has 'prospective paired comparison vs post-hoc explanation' paragraph with all 3 citations.\"\n  resolution_round: 6\n\n- id: \"R6-W1\"\n  summary: \"r=0.97 structural coupling not disclosed in Abstract/Contributions\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 7\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"High r partly mathematical due to penalty coupling.\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"Resurfaced. §4.1 has caveat but Abstract still reports r=0.97 without structural coupling qualifier.\"\n  action_items:\n    - round: 6\n      action: \"'near-perfect' → 'strong positive' + structural coupling caveat + redirect to 78.9%\"\n      assigned_to: main_agent\n      status: done\n    - round: 7\n      action: \"Add coupling qualifier in Abstract where r=0.97 is reported, or reduce its prominence\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W2\"\n  summary: \"Prescreening 19/30 exclusion — scope qualifier needed in title/abstract/conclusion\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 4\n  last_seen_round: 7\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"Want excluded task characteristics + step budget sensitivity.\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"Resurfaced as CRITICAL (escalated from warning). Both reviewers: title 'Dominant Routing Signal' needs scope qualifier. 63% exclusion = potential selection bias toward short-horizon death-prone tasks. Limitations discusses it but title/abstract/conclusion do not.\"\n  action_items:\n    - round: 6\n      action: \"Expand Limitations with excluded task characteristics + step budget\"\n      assigned_to: main_agent\n      status: done\n    - round: 7\n      action: \"Add scope qualifier to title/abstract/conclusion; analyze excluded task characteristics; discuss step budget sensitivity\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W3\"\n  summary: \"Missing failure mode analysis — death temporal pattern\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [2]\n      note: \"Director降为warning. Data extracted: median step 18/30.\"\n  action_items:\n    - round: 6\n      action: \"Extract death step from episodes.jsonl, add 1 sentence\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"Death temporal data extracted (median step 18/30, peak 14-17). Added to paper.\"\n  resolution_round: 6\n\n- id: \"R6-W4\"\n  summary: \"Deterministic strategy operationalization description insufficient\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"Need what LLM sees in each mode.\"\n  action_items:\n    - round: 6\n      action: \"§3.1 add ground-truth vs self-prediction description\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"method.tex describes ground-truth observation (det) vs self-prediction with compounding errors (internal).\"\n  resolution_round: 6\n\n- id: \"R6-W5\"\n  summary: \"MATH pilot (n=50) needs confidence intervals\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"Consensus.\"\n  action_items:\n    - round: 6\n      action: \"Add binomial 95% CI to MATH numbers\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"Limitations has MATH CIs.\"\n  resolution_round: 6\n\n- id: \"R6-W6\"\n  summary: \"find-non-living-thing bimodal DAF distribution not noted\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"DAF=0% vs others >85% heterogeneity.\"\n  action_items:\n    - round: 6\n      action: \"Add 1 sentence on bimodal distribution\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"experiments.tex notes bimodal DAF: find-non-living-thing ≈0% vs others >85%.\"\n  resolution_round: 6\n\n- id: \"R6-W7\"\n  summary: \"Concurrent work discussion too brief\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"tool-overuse-illusion and tool-use-tax need deeper discussion.\"\n  action_items:\n    - round: 6\n      action: \"Expand concurrent work in Related Work\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"Related Work expanded concurrent work discussion.\"\n  resolution_round: 6\n\n- id: \"R6-W8\"\n  summary: \"Safe RL literature coverage insufficient\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 7\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"Need 2024+ safe RL / agent failure refs.\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"Resurfaced. R2 raised as critical, R1 rebut to should-fix. Only Garcia 2015 survey cited. Need 1-2 safety critic works (CPO, safety Q-functions) for 'router = safety critic' claim in §5.\"\n  action_items:\n    - round: 6\n      action: \"Add recent safe RL / agent failure references\"\n      assigned_to: main_agent\n      status: done\n    - round: 7\n      action: \"Add 1-2 specific safety critic references (CPO or equivalent, 2020+)\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-N1\"\n  summary: \"ALFWorld data (Table 3, N=135) — no methodology description at all\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1 raised as Must-Fix, R2 agreed in cross-response. Model, deterministic modality definition, labeling process, episode length all missing. 'Capability gap' claim in footnote unsupported.\"\n  action_items:\n    - round: 7\n      action: \"Add full ALFWorld methodology (model, det definition, labeling, episode config) or move to Appendix with reduced weight\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-N2\"\n  summary: \"Router diagnostic conclusion confounded with data insufficiency (Contribution 4)\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1 raised as Must-Fix. R2 agreed: 'R1's strongest critique.' 81 train samples (~8 internal-preferred), 14 val samples. Cannot distinguish 'thin signal' from 'insufficient data'. Classification head 0% recall expected at ~8 positives.\"\n  action_items:\n    - round: 7\n      action: \"Acknowledge data-size confound explicitly; downgrade Contribution 4 to preliminary observation; or add data-size ablation\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W1\"\n  summary: \"MATH p=0.079 asymmetric use — 'vanishes' overstates non-significant result\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"Abstract/Conclusion present label inversion more strongly than §5. 'routing signal vanishes' too strong for p=0.079.\"\n  action_items:\n    - round: 7\n      action: \"Consistently mark 'not statistically significant' wherever MATH result appears\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W2\"\n  summary: \"Llama pilot (N=10) too small for Contribution 3\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"Both reviewers independently raised. No statistical power at N=10.\"\n  action_items:\n    - round: 7\n      action: \"Remove from Contribution 3 list; retain in text as directional observation only\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W3\"\n  summary: \"Pure-strategy labeling vs mixed-strategy deployment gap unanalyzed\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1 raised, R2 agreed in cross-response. Death in pure-internal ≠ death in mixed routing. DAgger cite insufficient. Death timing analysis needed.\"\n  action_items:\n    - round: 7\n      action: \"Analyze death timing; discuss mixed-routing implications in Limitations or Discussion\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W4\"\n  summary: \"Only ReAct tested — Reflexion/ToT may reduce death rate and change DAF\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R2 raised, R1 agreed in cross-response. Reflexion self-correction or ToT backtracking may lower death rate. Finding may be ReAct single-pass vulnerability, not general. Limitations discusses model scale but not reasoning strategy.\"\n  action_items:\n    - round: 7\n      action: \"Add reasoning strategy generalization discussion to Limitations\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W5\"\n  summary: \"Missing key references: RouteLLM, Reflexion, tool-learning survey\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R2 raised, R1 agreed RouteLLM most urgent (directly does routing). Reflexion ties to reasoning strategy gap.\"\n  action_items:\n    - round: 7\n      action: \"Add RouteLLM (Ong 2024), Reflexion (Shinn 2023), tool-learning survey (Qu 2024) to Related Work\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-m1\"\n  summary: \"Bib issues: retool-2026 key vs 2025 year; dynathink-2025 author mismatch\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"Both reviewers flagged.\"\n  action_items:\n    - round: 7\n      action: \"Fix bib key/year and author fields\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-m2\"\n  summary: \"Abstract '90.41%' false precision; Ethics 'RTX 5090' minor anonymity risk\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"90.41% → ~90%. RTX 5090 → 'consumer GPUs'.\"\n  action_items:\n    - round: 7\n      action: \"Round DAF to ~90%; generalize GPU mention\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-m3\"\n  summary: \"find-non-living-thing 40 episodes (vs 20 for others) unexplained; no code/data release plan\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [1]\n      note: \"Minor but should be addressed for reproducibility.\"\n  action_items:\n    - round: 7\n      action: \"Explain episode count difference; add code/data availability statement\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "simgate-modular-routing",
    "issues_yaml": "- id: \"R6-C1\"\n  summary: \"DAF penalty-dependence — headline ~90% anchored to P=100, 78.9% not co-equal\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 4\n  last_seen_round: 7\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"Fresh reviewers want full range + formula + dual reporting.\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"Resurfaced. Abstract still leads with DAF=90.41%. 78.9% present but not co-equal. R2 escalated to Must-Fix, R1 agreed on substance. Title 'Dominant' + P=10→46.4% tension unresolved.\"\n  action_items:\n    - round: 6\n      action: \"Abstract/Intro/§3.3/Conclusion dual reporting + DAF(P) formula in method.tex\"\n      assigned_to: main_agent\n      status: done\n    - round: 7\n      action: \"Promote 78.9% to primary metric in Abstract/Title; relegate DAF to secondary with explicit P-dependence caveat\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-C2\"\n  summary: \"Missing counterfactual-in-RL literature paragraph\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"Paper uses 'counterfactual' in title, must contextualize.\"\n  action_items:\n    - round: 6\n      action: \"Add paragraph + 3 refs (Amitai AAAI'24, Gajcin AAMAS'23, Olson AIJ'21)\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"related_work.tex has 'prospective paired comparison vs post-hoc explanation' paragraph with all 3 citations.\"\n  resolution_round: 6\n\n- id: \"R6-W1\"\n  summary: \"r=0.97 structural coupling not disclosed in Abstract/Contributions\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 7\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"High r partly mathematical due to penalty coupling.\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"Resurfaced. §4.1 has caveat but Abstract still reports r=0.97 without structural coupling qualifier.\"\n  action_items:\n    - round: 6\n      action: \"'near-perfect' → 'strong positive' + structural coupling caveat + redirect to 78.9%\"\n      assigned_to: main_agent\n      status: done\n    - round: 7\n      action: \"Add coupling qualifier in Abstract where r=0.97 is reported, or reduce its prominence\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W2\"\n  summary: \"Prescreening 19/30 exclusion — scope qualifier needed in title/abstract/conclusion\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 4\n  last_seen_round: 7\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"Want excluded task characteristics + step budget sensitivity.\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"Resurfaced as CRITICAL (escalated from warning). Both reviewers: title 'Dominant Routing Signal' needs scope qualifier. 63% exclusion = potential selection bias toward short-horizon death-prone tasks. Limitations discusses it but title/abstract/conclusion do not.\"\n  action_items:\n    - round: 6\n      action: \"Expand Limitations with excluded task characteristics + step budget\"\n      assigned_to: main_agent\n      status: done\n    - round: 7\n      action: \"Add scope qualifier to title/abstract/conclusion; analyze excluded task characteristics; discuss step budget sensitivity\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W3\"\n  summary: \"Missing failure mode analysis — death temporal pattern\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [2]\n      note: \"Director降为warning. Data extracted: median step 18/30.\"\n  action_items:\n    - round: 6\n      action: \"Extract death step from episodes.jsonl, add 1 sentence\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"Death temporal data extracted (median step 18/30, peak 14-17). Added to paper.\"\n  resolution_round: 6\n\n- id: \"R6-W4\"\n  summary: \"Deterministic strategy operationalization description insufficient\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"Need what LLM sees in each mode.\"\n  action_items:\n    - round: 6\n      action: \"§3.1 add ground-truth vs self-prediction description\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"method.tex describes ground-truth observation (det) vs self-prediction with compounding errors (internal).\"\n  resolution_round: 6\n\n- id: \"R6-W5\"\n  summary: \"MATH pilot (n=50) needs confidence intervals\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"Consensus.\"\n  action_items:\n    - round: 6\n      action: \"Add binomial 95% CI to MATH numbers\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"Limitations has MATH CIs.\"\n  resolution_round: 6\n\n- id: \"R6-W6\"\n  summary: \"find-non-living-thing bimodal DAF distribution not noted\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"DAF=0% vs others >85% heterogeneity.\"\n  action_items:\n    - round: 6\n      action: \"Add 1 sentence on bimodal distribution\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"experiments.tex notes bimodal DAF: find-non-living-thing ≈0% vs others >85%.\"\n  resolution_round: 6\n\n- id: \"R6-W7\"\n  summary: \"Concurrent work discussion too brief\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"tool-overuse-illusion and tool-use-tax need deeper discussion.\"\n  action_items:\n    - round: 6\n      action: \"Expand concurrent work in Related Work\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"Related Work expanded concurrent work discussion.\"\n  resolution_round: 6\n\n- id: \"R6-W8\"\n  summary: \"Safe RL literature coverage insufficient\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 6\n  last_seen_round: 7\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"Need 2024+ safe RL / agent failure refs.\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"Resurfaced. R2 raised as critical, R1 rebut to should-fix. Only Garcia 2015 survey cited. Need 1-2 safety critic works (CPO, safety Q-functions) for 'router = safety critic' claim in §5.\"\n  action_items:\n    - round: 6\n      action: \"Add recent safe RL / agent failure references\"\n      assigned_to: main_agent\n      status: done\n    - round: 7\n      action: \"Add 1-2 specific safety critic references (CPO or equivalent, 2020+)\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-N1\"\n  summary: \"ALFWorld data (Table 3, N=135) — no methodology description at all\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1 raised as Must-Fix, R2 agreed in cross-response. Model, deterministic modality definition, labeling process, episode length all missing. 'Capability gap' claim in footnote unsupported.\"\n  action_items:\n    - round: 7\n      action: \"Add full ALFWorld methodology (model, det definition, labeling, episode config) or move to Appendix with reduced weight\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-N2\"\n  summary: \"Router diagnostic conclusion confounded with data insufficiency (Contribution 4)\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1 raised as Must-Fix. R2 agreed: 'R1's strongest critique.' 81 train samples (~8 internal-preferred), 14 val samples. Cannot distinguish 'thin signal' from 'insufficient data'. Classification head 0% recall expected at ~8 positives.\"\n  action_items:\n    - round: 7\n      action: \"Acknowledge data-size confound explicitly; downgrade Contribution 4 to preliminary observation; or add data-size ablation\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W1\"\n  summary: \"MATH p=0.079 asymmetric use — 'vanishes' overstates non-significant result\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"Abstract/Conclusion present label inversion more strongly than §5. 'routing signal vanishes' too strong for p=0.079.\"\n  action_items:\n    - round: 7\n      action: \"Consistently mark 'not statistically significant' wherever MATH result appears\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W2\"\n  summary: \"Llama pilot (N=10) too small for Contribution 3\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"Both reviewers independently raised. No statistical power at N=10.\"\n  action_items:\n    - round: 7\n      action: \"Remove from Contribution 3 list; retain in text as directional observation only\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W3\"\n  summary: \"Pure-strategy labeling vs mixed-strategy deployment gap unanalyzed\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R1 raised, R2 agreed in cross-response. Death in pure-internal ≠ death in mixed routing. DAgger cite insufficient. Death timing analysis needed.\"\n  action_items:\n    - round: 7\n      action: \"Analyze death timing; discuss mixed-routing implications in Limitations or Discussion\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W4\"\n  summary: \"Only ReAct tested — Reflexion/ToT may reduce death rate and change DAF\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R2 raised, R1 agreed in cross-response. Reflexion self-correction or ToT backtracking may lower death rate. Finding may be ReAct single-pass vulnerability, not general. Limitations discusses model scale but not reasoning strategy.\"\n  action_items:\n    - round: 7\n      action: \"Add reasoning strategy generalization discussion to Limitations\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W5\"\n  summary: \"Missing key references: RouteLLM, Reflexion, tool-learning survey\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"R2 raised, R1 agreed RouteLLM most urgent (directly does routing). Reflexion ties to reasoning strategy gap.\"\n  action_items:\n    - round: 7\n      action: \"Add RouteLLM (Ong 2024), Reflexion (Shinn 2023), tool-learning survey (Qu 2024) to Related Work\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-m1\"\n  summary: \"Bib issues: retool-2026 key vs 2025 year; dynathink-2025 author mismatch\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"Both reviewers flagged.\"\n  action_items:\n    - round: 7\n      action: \"Fix bib key/year and author fields\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-m2\"\n  summary: \"Abstract '90.41%' false precision; Ethics 'RTX 5090' minor anonymity risk\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"90.41% → ~90%. RTX 5090 → 'consumer GPUs'.\"\n  action_items:\n    - round: 7\n      action: \"Round DAF to ~90%; generalize GPU mention\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-m3\"\n  summary: \"find-non-living-thing 40 episodes (vs 20 for others) unexplained; no code/data release plan\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 7\n  last_seen_round: 7\n  mentions:\n    - round: 7\n      reviewers: [1]\n      note: \"Minor but should be addressed for reproducibility.\"\n  action_items:\n    - round: 7\n      action: \"Explain episode count difference; add code/data availability statement\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 561 · 2026-05-15T15:31:45.100917+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml\", \"bytes\": 13054}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 562 · 2026-05-15T15:33:40.320827+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告 — Round 7 (Fresh Review)\n\n**论文**: Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\n**Venue**: EMNLP 2026 Main Conference (ARR May 2026 cycle)\n**Deadline**: 2026-05-25\n**Reviewers**: R1 (方法严谨性+实验充分性), R2 (新颖性+完整性+相关工作)\n**轮次**: Round 7 (Fresh review, 1 round + cross-sharing, converged)\n\n---\n\n## Summary\n\n本文提出 episode-level counterfactual analysis 方法，在 ScienceWorld 环境中比较 pure-internal (ReAct) 和 pure-deterministic 策略的 episode outcomes，发现 death avoidance 占据约 90% 的 routing signal（DAF=90.41% at P=100），78.9% 的 non-tie routing labels 由 death asymmetry 驱动。跨环境验证（MATH N=300）显示无 death penalty 时 routing signal 消失/反转。训练的 router 仅达 57-59% balanced accuracy，作者解读为 learnable signal 稀薄。\n\n---\n\n## Strengths\n\n**[S1] 研究问题定位精准** [R1, R2 共识]\n\"What drives routing signal\" 是 modular agent 设计中被忽视的先验问题。在大量工作关注 \"how to route\" 的背景下，本文追问 \"why routing helps\" 具有独立价值。\n\n**[S2] 统计分析严谨且透明** [R1, R2 共识]\nBootstrap CI、LOO analysis、Spearman rank correlation、seed robustness、penalty sensitivity analysis 全面覆盖。主动披露 r=0.97 的结构性耦合（§4.1），展现学术诚实度。\n\n**[S3] MATH 实验提供有效 negative control** [R1, R2 共识]\nN=300 的 MATH 评估在无 death penalty 环境下显示 routing signal 消失/反转（label distribution 86:9 → 30:17），有效支撑 death avoidance 是 ScienceWorld routing signal 的核心驱动力。\n\n**[S4] Limitations section 异常坦诚详尽** [R1, R2 共识]\n主动承认单环境单模型局限、penalty sensitivity、step-level mislabeling、capability dependence 等问题。\n\n**[S5] 写作质量高** [R1, R2 共识]\nStory arc 清晰（问题→step-level degeneracy→episode-level method→finding→cross-validation），结构紧凑，语言精准。\n\n**[S6] 当代相关工作覆盖出色** [R1]\n引用多篇 2026 concurrent work（tool-overuse-illusion、when2tool、tool-use-tax、to-call-or-not），展现对领域最新进展的把握。\n\n---\n\n## Weaknesses\n\n### Must-Fix (4 items)\n\n**[MF1] ALFWorld 数据来源与方法论完全缺失** [R1-N1, R2-W5; 共识: AGREE]\nTable 3 呈现 ALFWorld 数据（N=135），但论文未描述：使用什么模型、deterministic modality 具体定义、episode 长度、labeling 是否沿用 Algorithm 1。脚注关于 \"capability gap\" 的判断也缺乏支撑。不可追溯的数据严重削弱跨环境验证可信度。\n→ **Action**: 补充完整方法论描述，或移至 Appendix 并降低论证权重。\n\n**[MF2] Router 训练诊断结论与数据量不足存在根本性混淆** [R1-N2; R2 交叉回应 AGREE]\nRouter balanced accuracy 57-59% 被解读为 \"thin learnable signal\"（Contribution 4）。但训练集仅 81 样本（internal-preferred ~8 个），验证集 14 个。在此规模下，低准确率可能反映数据不足而非信号稀薄。Classification head 0% internal recall 在 ~8 正例下是预期行为，不构成独立证据。\n→ **Action**: 明确承认数据量混淆变量，将 Contribution 4 降级为初步观察，或提供数据量消融实验。\n\n**[MF3] 63% task types 排除构成严重选择偏差** [R1-N3, R2-N2; 共识: AGREE]\n19/30 task types 因 30-step timeout 排除。被排除的长 horizon 任务可能具有不同的 routing signal 构成（如更多非 death 信号）。标题 \"Dominant Routing Signal\" 和 abstract \"~90%\" 的 headline 未充分限定适用范围。\n→ **Action**: 标题/Abstract/Conclusion 增加 scope qualifier；分析被排除任务的特征；讨论 step budget 增加的潜在影响。\n\n**[MF4] DAF \"~90%\" headline 过度依赖 P=100 特定设置** [R2-N1, R1-W4; 共识: AGREE, R2 主张 Must-Fix]\nDAF 随 P 单调递增是数学必然。P=10→46.4%, P=25→68.4%, P=100→89.6%, P=200→94.5%。论文标题和 abstract 以 \"~90%\" 为 headline 完全锚定于 P=100。Penalty-independent 的 78.9% death-asymmetry label fraction 应提升为 primary metric。\n注：此问题在前轮审稿（R6-C1）中已标记为 resolved，但当前论文 abstract 仍以 DAF=90.41% 领衔，78.9% 仅作为补充指标出现，未达到 \"co-equal\" 标准。\n→ **Action**: Abstract/Title 中 78.9% 与 DAF 并列或优先呈现；明确标注 DAF 的 penalty-dependent 本质。\n\n### Should-Fix (7 items)\n\n**[SF1] MATH p=0.079 的不对称使用** [R1-W1; R2 AGREE]\nAbstract/Conclusion 呈现 label distribution inversion 比正文更强势，但 p=0.079 未达显著性。\"routing signal vanishes\" 的措辞过强。\n→ **Action**: 统一在所有出现处标注 \"not statistically significant\"。\n\n**[SF2] Llama pilot (N=10) 作为 contribution 过度包装** [R1-W2, R2-W2; 共识: AGREE]\n10 episodes 几乎无统计功效，不应与 MATH (N=300) 并列为 Contribution 3 \"Cross-context validation\"。\n→ **Action**: 从 Contribution list 移除，仅在正文保留为方向性观察。\n\n**[SF3] Pure-strategy → mixed-strategy gap 未分析** [R1-W3; R2 交叉回应 AGREE]\n标注基于 pure-strategy trajectory，但实际部署是 mixed routing。Death 在 pure-internal 全程下发生不等于在 mixed routing 中也会发生。DAgger citation 不够——需要 death timing 分析以评估 mixed routing 可行性。\n→ **Action**: 分析 death 发生时间步，讨论 mixed routing 下 death rate 的预期变化。\n\n**[SF4] r=0.97 结构性耦合在 Abstract/Contributions 中披露不足** [R1-W5; R2 AGREE]\nΔ_full ≈ δ·P + Δ_nd 且 δ·P 占 ~90% 时，δ 与 Δ_full 的高相关部分是数学同义反复。§4.1 有 caveat 但 Abstract/Contributions 未携带。\n→ **Action**: Abstract 中加结构性耦合限定语，或削弱 r=0.97 的呈现权重。\n\n**[SF5] Safe RL 文献覆盖不足** [R2-N3 raised as critical; R1 REBUT to should-fix; Director 裁定 should-fix]\n核心 insight 是 \"router = safety critic\"（§5 Discussion），但仅引 Garcia 2015 一篇 11 年前的综述。论文贡献是分析性非算法性的，但应补充 1-2 篇代表性 safety critic 工作。\n→ **Action**: 补充 CPO 或 safety Q-function 等 2020+ 代表性工作。\n\n**[SF6] 仅测试 ReAct，未讨论其他推理策略的影响** [R2-W4; R1 AGREE]\nReflexion 的 self-correction 或 ToT 的 backtracking 可能显著降低 death rate → 降低 DAF。论文发现可能是 ReAct single-pass vulnerability 的特性而非通用结论。Limitations 讨论了 model scale 影响但未讨论 reasoning strategy 影响。\n→ **Action**: Limitations 增加 reasoning strategy 泛化讨论。\n\n**[SF7] 缺少重要引用** [R2-W3; R1 部分 AGREE]\nRouteLLM (Ong et al., 2024)——直接做 routing，最为紧迫；Reflexion (Shinn et al., 2023)——与 ReAct 替代策略相关；tool-learning survey (Qu et al., 2024)。\n→ **Action**: 补充上述引用至 Related Work。\n\n### Minor (6 items)\n\n- **[m1]** `retool-2026` bib key 与实际出版年份 2025 不一致 [R1, R2]\n- **[m2]** `dynathink-2025` first author 信息可能有误 [R1, R2]\n- **[m3]** Abstract 中 \"90.41%\" 精度暗示过高确信度，建议改为 \"~90%\" [R2-M5; R1 AGREE]\n- **[m4]** Ethics 提及 \"RTX 5090\" 存在轻微去匿名化风险，建议泛化为 \"consumer GPUs\" [R2-M6]\n- **[m5]** `find-non-living-thing` 给了 40 episodes 而其他 task types 给 20，未解释原因 [R1]\n- **[m6]** 未提及代码/数据开源计划 [R1]\n\n---\n\n## Reviewer Consensus [AGREE]\n\n以下问题由两位 Reviewer 独立提出并在交叉回应中确认共识：\n1. **ALFWorld 数据来源缺失** (MF1) — 两位均列为 critical\n2. **63% task types 排除的选择偏差** (MF3) — 两位均列为 critical\n3. **DAF penalty-sensitivity → 78.9% 应为 primary metric** (MF4)\n4. **Llama pilot N=10 过小** (SF2)\n5. **r=0.97 结构性耦合披露不足** (SF4)\n6. **Bib 细节问题** (m1, m2)\n\n## Reviewer Divergence\n\n**[DAF 严重性等级]** R2 列 DAF penalty-sensitivity 为 Must-Fix，R1 列为 Should-Fix。**Director 裁定**：提升为 Must-Fix——标题含 \"Dominant\" 一词，headline metric 的 penalty-dependence 直接影响论文核心声明的可信度。\n\n**[Safe RL 文献]** R2 列为 Must-Fix (critical)，R1 REBUT 为 Should-Fix——论文贡献是分析性的，非算法性的。**Director 裁定**：降为 Should-Fix——R1 的论证更有说服力，\"router = safety critic\" 是 Discussion implication 而非 primary contribution。\n\n---\n\n## Questions for Authors\n\n1. ALFWorld 实验的完整方法论——模型、deterministic modality 定义、labeling 流程？\n2. 如果使用 Reflexion 或 ToT 替代 ReAct，预期 death rate 和 DAF 会如何变化？\n3. Router 低准确率（57-59%）在数据量增加 5-10 倍后是否会改善？是否考虑过合成数据扩增？\n4. 被排除的 19 个 task types 有哪些共同特征？增加 step budget 到 50 或 100 步是否可行？\n5. Death 事件通常发生在 episode 的哪个时间步？这对 mixed routing 策略有什么启示？\n\n## Missing References\n\n1. **RouteLLM** (Ong et al., 2024) — 直接做 LLM routing，高度相关\n2. **Reflexion** (Shinn et al., 2023) — LLM agent self-correction，与 death avoidance 机制相关\n3. **Tool-learning survey** (Qu et al., 2024) — 综述性引用\n4. **CPO / Safety critics** (2020+) — 支撑 \"router as safety critic\" 论述\n5. ScienceWorld follow-up works（如有）\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿未配置，无外部审稿结果。\n\n---\n\n## Overall Assessment\n\n**评分：Borderline Reject（偏向 Findings track）**\n**置信度：High (4/5)**\n\n两位 Reviewer 独立给出 3/5（Borderline/Findings level）且交叉回应后维持评分。\n\n**核心判断**：论文提出了一个有价值的研究问题（\"what drives routing signal\"），提供了方法论工具（episode-level counterfactual + DAF），并在 ScienceWorld 上给出了令人信服的经验发现。统计分析扎实，写作质量高。\n\n**但存在四个 Must-Fix 问题**阻碍 main conference 接收：\n1. ALFWorld 数据不可追溯（MF1）\n2. Router 诊断结论与数据量不足无法区分（MF2）\n3. 63% task types 排除的选择偏差未充分限定（MF3）\n4. DAF headline 过度依赖 P=100（MF4）\n\n**与前轮比较**：R6 标记为 resolved 的 4 个 issue（R6-C1 DAF penalty-dependence、R6-W1 r=0.97 overclaim、R6-W2 prescreening exclusion、R6-W8 Safe RL literature）在 fresh review 中重新浮现，说明前轮修复未达到预期效果或有回退。新增 2 个 critical issue（ALFWorld 方法论缺失、Router diagnostic confound）。\n\n**建议**：修复 4 个 Must-Fix 问题后适合 EMNLP 2026 Findings track。冲 main conference 需额外扩展实验范围（更多 task types、更多推理策略、更多模型）。\n\n---\n\n## Detailed Comments by Section\n\n### §1 Introduction\n- Story arc 清晰，但 \"death avoidance accounts for approximately 90%\" 应在首次出现时即标注 \"at P=100\"\n- Contribution 3 应移除 Llama pilot，仅保留 MATH\n- Contribution 4 需加 data-size caveat\n\n### §2 Method\n- Problem Setup (§2.1) 形式化清晰\n- Counterfactual collection (§2.2) 设计合理，97.4% tie rate 论证充分\n- Algorithm 1 清晰直观\n- DAF metric (§2.4) 数学定义合理，penalty sensitivity analysis (Appendix E) 充分\n\n### §3 Experiments\n- §3.1 Death decomposition 分析扎实（r=0.97 + LOO + bootstrap）\n- §3.2 Baselines 完整（always-int/det/random/oracle），oracle degeneracy 有说服力\n- §3.3 Router diagnostic 有方法论价值但 Contribution 4 claim 过强\n- §3.4 Cross-model (N=10) 过小，应降级\n\n### §4 Related Work\n- Tool-use 和 adaptive computation 覆盖充分\n- 缺 RouteLLM、Reflexion\n- Safe RL 需补 1-2 篇 2020+ 工作\n- Counterfactual RL 段落（Olson/Gajcin/Amitai）已有，定位清晰\n\n### §5 Discussion\n- MATH negative control 有效但 p=0.079 需统一标注\n- ALFWorld 数据缺方法论（最严重问题）\n- \"Router as safety critic\" 论述有洞察力但文献支撑不足\n- Penalty sensitivity 和 capability dependence 讨论到位\n\n### §6 Conclusion\n- 与 Introduction 呼应良好\n- 需同步所有 scope qualifiers 和 metric 调整\n\n### Limitations\n- 异常详尽坦诚（这是本文的一个突出优点）\n- 需增加 reasoning strategy generalization 讨论（Reflexion/ToT 对 death rate 的潜在影响）\n\n### Appendices\n- 统计附录（B, C, D, E, F）质量高\n- Labeling quality audit (A) 有效回应 oracle circularity concern\n\n---\n\n## Issue Tracker 同步状态\n\n已更新 `review_issues.yaml`：\n- 4 个前轮 resolved issue 重开（R6-C1, R6-W1, R6-W2, R6-W8）\n- 3 个新 critical issue（R7-N1 ALFWorld, R7-N2 Router confound）\n- 5 个新 warning issue（R7-W1 至 R7-W5）\n- 3 个新 info issue（R7-m1 至 R7-m3）\n- 总计 14 个 open issues（4 critical, 7 warning, 3 info）",
  "project": "simgate-modular-routing",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "borderline reject"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告 — Round 7 (Fresh Review)\n\n**论文**: Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\n**Venue**: EMNLP 2026 Main Conference (ARR May 2026 cycle)\n**Deadline**: 2026-05-25\n**Reviewers**: R1 (方法严谨性+实验充分性), R2 (新颖性+完整性+相关工作)\n**轮次**: Round 7 (Fresh review, 1 round + cross-sharing, converged)\n\n---\n\n## Summary\n\n本文提出 episode-level counterfactual analysis 方法，在 ScienceWorld 环境中比较 pure-internal (ReAct) 和 pure-deterministic 策略的 episode outcomes，发现 death avoidance 占据约 90% 的 routing signal（DAF=90.41% at P=100），78.9% 的 non-tie routing labels 由 death asymmetry 驱动。跨环境验证（MATH N=300）显示无 death penalty 时 routing signal 消失/反转。训练的 router 仅达 57-59% balanced accuracy，作者解读为 learnable signal 稀薄。\n\n---\n\n## Strengths\n\n**[S1] 研究问题定位精准** [R1, R2 共识]\n\"What drives routing signal\" 是 modular agent 设计中被忽视的先验问题。在大量工作关注 \"how to route\" 的背景下，本文追问 \"why routing helps\" 具有独立价值。\n\n**[S2] 统计分析严谨且透明** [R1, R2 共识]\nBootstrap CI、LOO analysis、Spearman rank correlation、seed robustness、penalty sensitivity analysis 全面覆盖。主动披露 r=0.97 的结构性耦合（§4.1），展现学术诚实度。\n\n**[S3] MATH 实验提供有效 negative control** [R1, R2 共识]\nN=300 的 MATH 评估在无 death penalty 环境下显示 routing signal 消失/反转（label distribution 86:9 → 30:17），有效支撑 death avoidance 是 ScienceWorld routing signal 的核心驱动力。\n\n**[S4] Limitations section 异常坦诚详尽** [R1, R2 共识]\n主动承认单环境单模型局限、penalty sensitivity、step-level mislabeling、capability dependence 等问题。\n\n**[S5] 写作质量高** [R1, R2 共识]\nStory arc 清晰（问题→step-level degeneracy→episode-level method→finding→cross-validation），结构紧凑，语言精准。\n\n**[S6] 当代相关工作覆盖出色** [R1]\n引用多篇 2026 concurrent work（tool-overuse-illusion、when2tool、tool-use-tax、to-call-or-not），展现对领域最新进展的把握。\n\n---\n\n## Weaknesses\n\n### Must-Fix (4 items)\n\n**[MF1] ALFWorld 数据来源与方法论完全缺失** [R1-N1, R2-W5; 共识: AGREE]\nTable 3 呈现 ALFWorld 数据（N=135），但论文未描述：使用什么模型、deterministic modality 具体定义、episode 长度、labeling 是否沿用 Algorithm 1。脚注关于 \"capability gap\" 的判断也缺乏支撑。不可追溯的数据严重削弱跨环境验证可信度。\n→ **Action**: 补充完整方法论描述，或移至 Appendix 并降低论证权重。\n\n**[MF2] Router 训练诊断结论与数据量不足存在根本性混淆** [R1-N2; R2 交叉回应 AGREE]\nRouter balanced accuracy 57-59% 被解读为 \"thin learnable signal\"（Contribution 4）。但训练集仅 81 样本（internal-preferred ~8 个），验证集 14 个。在此规模下，低准确率可能反映数据不足而非信号稀薄。Classification head 0% internal recall 在 ~8 正例下是预期行为，不构成独立证据。\n→ **Action**: 明确承认数据量混淆变量，将 Contribution 4 降级为初步观察，或提供数据量消融实验。\n\n**[MF3] 63% task types 排除构成严重选择偏差** [R1-N3, R2-N2; 共识: AGREE]\n19/30 task types 因 30-step timeout 排除。被排除的长 horizon 任务可能具有不同的 routing signal 构成（如更多非 death 信号）。标题 \"Dominant Routing Signal\" 和 abstract \"~90%\" 的 headline 未充分限定适用范围。\n→ **Action**: 标题/Abstract/Conclusion 增加 scope qualifier；分析被排除任务的特征；讨论 step budget 增加的潜在影响。\n\n**[MF4] DAF \"~90%\" headline 过度依赖 P=100 特定设置** [R2-N1, R1-W4; 共识: AGREE, R2 主张 Must-Fix]\nDAF 随 P 单调递增是数学必然。P=10→46.4%, P=25→68.4%, P=100→89.6%, P=200→94.5%。论文标题和 abstract 以 \"~90%\" 为 headline 完全锚定于 P=100。Penalty-independent 的 78.9% death-asymmetry label fraction 应提升为 primary metric。\n注：此问题在前轮审稿（R6-C1）中已标记为 resolved，但当前论文 abstract 仍以 DAF=90.41% 领衔，78.9% 仅作为补充指标出现，未达到 \"co-equal\" 标准。\n→ **Action**: Abstract/Title 中 78.9% 与 DAF 并列或优先呈现；明确标注 DAF 的 penalty-dependent 本质。\n\n### Should-Fix (7 items)\n\n**[SF1] MATH p=0.079 的不对称使用** [R1-W1; R2 AGREE]\nAbstract/Conclusion 呈现 label distribution inversion 比正文更强势，但 p=0.079 未达显著性。\"routing signal vanishes\" 的措辞过强。\n→ **Action**: 统一在所有出现处标注 \"not statistically significant\"。\n\n**[SF2] Llama pilot (N=10) 作为 contribution 过度包装** [R1-W2, R2-W2; 共识: AGREE]\n10 episodes 几乎无统计功效，不应与 MATH (N=300) 并列为 Contribution 3 \"Cross-context validation\"。\n→ **Action**: 从 Contribution list 移除，仅在正文保留为方向性观察。\n\n**[SF3] Pure-strategy → mixed-strategy gap 未分析** [R1-W3; R2 交叉回应 AGREE]\n标注基于 pure-strategy trajectory，但实际部署是 mixed routing。Death 在 pure-internal 全程下发生不等于在 mixed routing 中也会发生。DAgger citation 不够——需要 death timing 分析以评估 mixed routing 可行性。\n→ **Action**: 分析 death 发生时间步，讨论 mixed routing 下 death rate 的预期变化。\n\n**[SF4] r=0.97 结构性耦合在 Abstract/Contributions 中披露不足** [R1-W5; R2 AGREE]\nΔ_full ≈ δ·P + Δ_nd 且 δ·P 占 ~90% 时，δ 与 Δ_full 的高相关部分是数学同义反复。§4.1 有 caveat 但 Abstract/Contributions 未携带。\n→ **Action**: Abstract 中加结构性耦合限定语，或削弱 r=0.97 的呈现权重。\n\n**[SF5] Safe RL 文献覆盖不足** [R2-N3 raised as critical; R1 REBUT to should-fix; Director 裁定 should-fix]\n核心 insight 是 \"router = safety critic\"（§5 Discussion），但仅引 Garcia 2015 一篇 11 年前的综述。论文贡献是分析性非算法性的，但应补充 1-2 篇代表性 safety critic 工作。\n→ **Action**: 补充 CPO 或 safety Q-function 等 2020+ 代表性工作。\n\n**[SF6] 仅测试 ReAct，未讨论其他推理策略的影响** [R2-W4; R1 AGREE]\nReflexion 的 self-correction 或 ToT 的 backtracking 可能显著降低 death rate → 降低 DAF。论文发现可能是 ReAct single-pass vulnerability 的特性而非通用结论。Limitations 讨论了 model scale 影响但未讨论 reasoning strategy 影响。\n→ **Action**: Limitations 增加 reasoning strategy 泛化讨论。\n\n**[SF7] 缺少重要引用** [R2-W3; R1 部分 AGREE]\nRouteLLM (Ong et al., 2024)——直接做 routing，最为紧迫；Reflexion (Shinn et al., 2023)——与 ReAct 替代策略相关；tool-learning survey (Qu et al., 2024)。\n→ **Action**: 补充上述引用至 Related Work。\n\n### Minor (6 items)\n\n- **[m1]** `retool-2026` bib key 与实际出版年份 2025 不一致 [R1, R2]\n- **[m2]** `dynathink-2025` first author 信息可能有误 [R1, R2]\n- **[m3]** Abstract 中 \"90.41%\" 精度暗示过高确信度，建议改为 \"~90%\" [R2-M5; R1 AGREE]\n- **[m4]** Ethics 提及 \"RTX 5090\" 存在轻微去匿名化风险，建议泛化为 \"consumer GPUs\" [R2-M6]\n- **[m5]** `find-non-living-thing` 给了 40 episodes 而其他 task types 给 20，未解释原因 [R1]\n- **[m6]** 未提及代码/数据开源计划 [R1]\n\n---\n\n## Reviewer Consensus [AGREE]\n\n以下问题由两位 Reviewer 独立提出并在交叉回应中确认共识：\n1. **ALFWorld 数据来源缺失** (MF1) — 两位均列为 critical\n2. **63% task types 排除的选择偏差** (MF3) — 两位均列为 critical\n3. **DAF penalty-sensitivity → 78.9% 应为 primary metric** (MF4)\n4. **Llama pilot N=10 过小** (SF2)\n5. **r=0.97 结构性耦合披露不足** (SF4)\n6. **Bib 细节问题** (m1, m2)\n\n## Reviewer Divergence\n\n**[DAF 严重性等级]** R2 列 DAF penalty-sensitivity 为 Must-Fix，R1 列为 Should-Fix。**Director 裁定**：提升为 Must-Fix——标题含 \"Dominant\" 一词，headline metric 的 penalty-dependence 直接影响论文核心声明的可信度。\n\n**[Safe RL 文献]** R2 列为 Must-Fix (critical)，R1 REBUT 为 Should-Fix——论文贡献是分析性的，非算法性的。**Director 裁定**：降为 Should-Fix——R1 的论证更有说服力，\"router = safety critic\" 是 Discussion implication 而非 primary contribution。\n\n---\n\n## Questions for Authors\n\n1. ALFWorld 实验的完整方法论——模型、deterministic modality 定义、labeling 流程？\n2. 如果使用 Reflexion 或 ToT 替代 ReAct，预期 death rate 和 DAF 会如何变化？\n3. Router 低准确率（57-59%）在数据量增加 5-10 倍后是否会改善？是否考虑过合成数据扩增？\n4. 被排除的 19 个 task types 有哪些共同特征？增加 step budget 到 50 或 100 步是否可行？\n5. Death 事件通常发生在 episode 的哪个时间步？这对 mixed routing 策略有什么启示？\n\n## Missing References\n\n1. **RouteLLM** (Ong et al., 2024) — 直接做 LLM routing，高度相关\n2. **Reflexion** (Shinn et al., 2023) — LLM agent self-correction，与 death avoidance 机制相关\n3. **Tool-learning survey** (Qu et al., 2024) — 综述性引用\n4. **CPO / Safety critics** (2020+) — 支撑 \"router as safety critic\" 论述\n5. ScienceWorld follow-up works（如有）\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿未配置，无外部审稿结果。\n\n---\n\n## Overall Assessment\n\n**评分：Borderline Reject（偏向 Findings track）**\n**置信度：High (4/5)**\n\n两位 Reviewer 独立给出 3/5（Borderline/Findings level）且交叉回应后维持评分。\n\n**核心判断**：论文提出了一个有价值的研究问题（\"what drives routing signal\"），提供了方法论工具（episode-level counterfactual + DAF），并在 ScienceWorld 上给出了令人信服的经验发现。统计分析扎实，写作质量高。\n\n**但存在四个 Must-Fix 问题**阻碍 main conference 接收：\n1. ALFWorld 数据不可追溯（MF1）\n2. Router 诊断结论与数据量不足无法区分（MF2）\n3. 63% task types 排除的选择偏差未充分限定（MF3）\n4. DAF headline 过度依赖 P=100（MF4）\n\n**与前轮比较**：R6 标记为 resolved 的 4 个 issue（R6-C1 DAF penalty-dependence、R6-W1 r=0.97 overclaim、R6-W2 prescreening exclusion、R6-W8 Safe RL literature）在 fresh review 中重新浮现，说明前轮修复未达到预期效果或有回退。新增 2 个 critical issue（ALFWorld 方法论缺失、Router diagnostic confound）。\n\n**建议**：修复 4 个 Must-Fix 问题后适合 EMNLP 2026 Findings track。冲 main conference 需额外扩展实验范围（更多 task types、更多推理策略、更多模型）。\n\n---\n\n## Detailed Comments by Section\n\n### §1 Introduction\n- Story arc 清晰，但 \"death avoidance accounts for approximately 90%\" 应在首次出现时即标注 \"at P=100\"\n- Contribution 3 应移除 Llama pilot，仅保留 MATH\n- Contribution 4 需加 data-size caveat\n\n### §2 Method\n- Problem Setup (§2.1) 形式化清晰\n- Counterfactual collection (§2.2) 设计合理，97.4% tie rate 论证充分\n- Algorithm 1 清晰直观\n- DAF metric (§2.4) 数学定义合理，penalty sensitivity analysis (Appendix E) 充分\n\n### §3 Experiments\n- §3.1 Death decomposition 分析扎实（r=0.97 + LOO + bootstrap）\n- §3.2 Baselines 完整（always-int/det/random/oracle），oracle degeneracy 有说服力\n- §3.3 Router diagnostic 有方法论价值但 Contribution 4 claim 过强\n- §3.4 Cross-model (N=10) 过小，应降级\n\n### §4 Related Work\n- Tool-use 和 adaptive computation 覆盖充分\n- 缺 RouteLLM、Reflexion\n- Safe RL 需补 1-2 篇 2020+ 工作\n- Counterfactual RL 段落（Olson/Gajcin/Amitai）已有，定位清晰\n\n### §5 Discussion\n- MATH negative control 有效但 p=0.079 需统一标注\n- ALFWorld 数据缺方法论（最严重问题）\n- \"Router as safety critic\" 论述有洞察力但文献支撑不足\n- Penalty sensitivity 和 capability dependence 讨论到位\n\n### §6 Conclusion\n- 与 Introduction 呼应良好\n- 需同步所有 scope qualifiers 和 metric 调整\n\n### Limitations\n- 异常详尽坦诚（这是本文的一个突出优点）\n- 需增加 reasoning strategy generalization 讨论（Reflexion/ToT 对 death rate 的潜在影响）\n\n### Appendices\n- 统计附录（B, C, D, E, F）质量高\n- Labeling quality audit (A) 有效回应 oracle circularity concern\n\n---\n\n## Issue Tracker 同步状态\n\n已更新 `review_issues.yaml`：\n- 4 个前轮 resolved issue 重开（R6-C1, R6-W1, R6-W2, R6-W8）\n- 3 个新 critical issue（R7-N1 ALFWorld, R7-N2 Router confound）\n- 5 个新 warning issue（R7-W1 至 R7-W5）\n- 3 个新 info issue（R7-m1 至 R7-m3）\n- 总计 14 个 open issues（4 critical, 7 warning, 3 info）",
    "project": "simgate-modular-routing",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "borderline reject"
  }
}
```

</details>

---


### Tool result

_source line 563 · 2026-05-15T15:33:44.538263+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_f6bffc7e8351600df8091f08a63cd5a0:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4217
}
```

</details>

---


### Assistant

_source line 564 · 2026-05-15T15:33:52.618306+00:00_

审稿报告已投递至 Research Director。

**圆桌审稿完成 — Round 7 总结**：

- **评分**：Borderline Reject（偏向 Findings track）
- **4 个 Must-Fix**：ALFWorld 数据不可追溯、Router 诊断结论与数据量混淆、63% task types 排除的选择偏差、DAF headline 过度依赖 P=100
- **7 个 Should-Fix**：MATH p=0.079 不对称使用、Llama pilot 过度包装、pure→mixed gap、r=0.97 耦合披露、Safe RL 文献、ReAct-only 局限、缺少 RouteLLM/Reflexion 引用
- **关键共识**：两位 Reviewer 独立给出 3/5 并在交叉回应后维持。核心发现在 ScienceWorld 内有说服力，但 generalizability 声明超出数据支撑
- **前轮回退**：R6 标记 resolved 的 4 个 issue 重新浮现，需要更彻底的修复
- **Issue Tracker**：14 个 open issues 已同步更新

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 54

## Round 54

2 recorded events


### User

_source line 565 · 2026-05-15T15:33:54.123565+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交给 Review Director。总结：

- 对 R1 的 13 条意见（3 Must-Fix + 5 Should-Fix + 3 Minor + 2 Strengths dispute），我 **[AGREE] 12 条，[REBUT] 1 条**（W4 我认为应从 Should-Fix 提升为 Must-Fix）
- R1-N2（router diagnostic vs. data insufficiency confound）和 R1-W3（pure-to-mixed strategy gap）是我 Round 1 遗漏的重要问题，现已认同
- 两位 Reviewer 在 5 个核心问题上独立达成一致，总体评分均为 3/5 (Findings-level)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 566 · 2026-05-15T15:34:01.231547+00:00_

审稿报告已在上一轮提交完毕（Reviewer 2 的交叉回应在报告合成前已纳入）。本轮审稿流程已结束。

**最终状态**：
- 报告已投递至 Research Director
- Issue Tracker 已更新（14 个 open issues：4 critical / 7 warning / 3 info）
- 评分：**Borderline Reject**（偏向 Findings track）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 55

## Round 55

56 recorded events


### User

_source line 567 · 2026-05-16T12:19:05.536361+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: simgate-modular-routing
- 论文路径: projects/simgate-modular-routing/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Main Conference Long Paper
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 568 · 2026-05-16T12:19:12.687114+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 569 · 2026-05-16T12:19:12.688114+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 2458 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 1
}
```

</details>

---


### Tool call

_source line 570 · 2026-05-16T12:19:19.687151+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,WebSearch",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,WebSearch",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 571 · 2026-05-16T12:19:19.838175+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 572 · 2026-05-16T12:19:24.155789+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,request_external_review,get_external_review_status",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,request_external_review,get_external_review_status",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 573 · 2026-05-16T12:19:24.257190+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 574 · 2026-05-16T12:19:28.524535+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 575 · 2026-05-16T12:19:28.575197+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 576 · 2026-05-16T12:19:31.939065+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "simgate-modular-routing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "simgate-modular-routing"
  }
}
```

</details>

---


### Tool result

_source line 577 · 2026-05-16T12:19:33.646414+00:00_

{"result":"# 项目 simgate-modular-routing 概况\n\n## 实验状态 (87 个)\n\n- **plan-001b-gpu1-extra**: DONE (failed) — \n- **plan-001b-gpu1**: DONE (success) — \n- **plan-001b-gpu0-v2**: DONE (failed) — \n- **plan-011-rule-based**: DONE (success) — \n- **plan-001b-gpu0**: DONE (failed) — \n- **research-prescreening-gpu0**: DONE (killed) — \n- **research-prescreening-gpu1**: DONE (success) — \n- **research-boil-v3-gpu1**: DONE (success) — \n- **mvp-p1-gpu1-v3**: DONE (success) — \n- **mvp-p1-gpu0-vllm**: DONE (success) — \n- **mvp-p1-gpu0**: DONE (killed) — \n- **mvp-p1-gpu1-v2**: DONE (killed) — \n- **mvp-p1-gpu1-vllm**: DONE (killed) — \n- **mvp-p1-gpu1**: DONE (killed) — \n- **mvp-p0-forking**: DONE (success) — \n\n## 最新报告\n&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-16T07:36:51Z; do not edit — regenerated by auto_build_report_facts) -->\n## 📊 当前状态（auto-derived from registry）\n\n**总计**: 87 个实验 — DONE 86, RUNNING 1\n**DONE 分布**: failed 15, killed 18, negative 19, success 34\n\n### GPU 占用\n- **分配**: 2 张 — westb-13313:cuda:0, westb-13313:cuda:1\n- **实际运行**: 1 张 — westb-13313:cuda:0(llama-cross-model-v2)\n- **空闲（分配了没跑）**: westb-13313:cuda:1\n\n### 🏃 RUNNING\n| exp_id | server | gpu | pid | log |\n|--------|--------|-----|-----|-----|\n| `llama-cross-model-v2` | westb-13313 | cuda:0 | 961982 | `~/runs/simgate-modular-routing/llama-cross-model-v2.log` |\n\n### 📌 最近完成 (top 5)\n- `r7n2-supplement-100-200` [failed] — 2026-05-16T07:36:49 — EXIT_CODE=1 (generic error — check log tail)\n- `alfworld-daf-decomposition` [success] — 2026-05-16T06:59:58\n- `daf-sensitivity-extended` [success] — 2026-05-16T06:38:32\n- `r7n2-data-size-ablation-r3` [negative] — 2026-05-16T05:08:31\n- `r7n2-data-size-ablation-v2` [failed] — 2026-05-16T03:53:56\n\n### 🔴 最近失败原因 (top 3)\n- `r7n2-supplement-100-200`: EXIT_CODE=1 (generic error — check log tail)\n- `r7n2-data-size-ablation-v2`: _(no failure_reason — pre-2026-04-24 entry)_\n\n&lt;!-- AUTO-FACTS-END -->\n\n---\n\n# Handover — 2026-05-16\n\n> 由 Agent 生成，每次状态变
…[truncated 1800 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1707
}
```

</details>

---


### Tool call

_source line 578 · 2026-05-16T12:19:33.797618+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 579 · 2026-05-16T12:19:33.798261+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\graphicspath{{figures/}}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{algorithm}
16	\usepackage{algorithmic}
17	
18	\title{Death Avoidance as the Dominant Routing Signal:\\A Counterfactual Analysis on ScienceWorld}
19	
20	\author{Anonymous}
21	
22	\begin{document}
23	\maketitle
24	
25	\input{abstract}
26	\input{introduction}
27	\input{method}
28	\input{experiments}
29	\input{related_work}
30	\input{discussion}
31	\input{conclusion}
32	
33	\section*{Limitations}
34	
35	Our primary analysis uses a single environment (ScienceWorld, 11 of 30 task types) with one backbone (Qwen2.5-7B-Instruct); generalization requires further validation. The $-100$ death penalty amplifies DAF; environments with softer penalties would exhibit lower DAF values (Appendix~\ref{app:penalty}). The 19 excluded task types (63\%) lack routing signal because both strategies typically time out within 30 steps; increasing the step budget could surface additional signal. Our internal-reasoning baseline uses single-pass ReAct~\citep{react-2023}; more sophisticated strategies (e.g., Reflexion~\citep{reflexion-2023}) may reduce internal death rates and lower DAF. Episode-level labels may assign suboptimal routing to individual steps, particularly those preceding death events, and training on pure-strategy trajectories introduces distribution shift at deployment~\citep{dagger-2011}. Cross-environment analyses on MATH and ALFWorld (\S\ref{sec:discussion}, Appendix~\ref{app:cross-env}) provide supporting evidence but do not conclusively establish generalization. A Llama-3.1-8B pilot ($N{=}10$; Appendix~\ref{app:cross-model}) shows directional consistency but is insufficient for statistical inference.
36	
37	\section*{Ethics Statement}
38	
39	This 
…[truncated 5646 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 580 · 2026-05-16T12:19:47.368436+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex",
  "offset": "100",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex",
    "offset": "100",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 581 · 2026-05-16T12:19:47.519821+00:00_

100	inclined-plane         & 0.969 \\
101	freeze                 & 0.971 \\
102	meas-melt-point        & 0.972 \\
103	id-life-stages-2       & 0.972 \\
104	find-animal            & 0.970 \\
105	grow-fruit             & 0.973 \\
106	chem-mix               & 0.969 \\
107	find-non-living        & 0.980 \\
108	\bottomrule
109	\end{tabular}
110	\caption{Leave-one-out Pearson $r$ for the death rate differential vs.\ $\Delta_{\text{full}}$ correlation. Full $r = 0.970$; LOO range $[0.963, 0.980]$. No single task type is a leverage point.}
111	\label{tab:loo}
112	\end{table}
113	
114	\section{Router Training Details}
115	\label{app:router-details}
116	
117	We use Qwen3-1.7B for the router to avoid circular dependency with the Qwen2.5-7B data-generating model.
118	
119	With gradient accumulation of 1 (effective batch size 4), routing performance is highly sensitive to the evaluation split, suggesting overfitting to specific train/validation partition boundaries. With gradient accumulation of 8 (effective batch size 32), step-level performance stabilizes across splits (${\sim}54\%$ balanced accuracy). All reported results use gradient accumulation 8.
120	
121	Under step-level evaluation with a fixed data split, cross-seed balanced accuracy ranges from 52.7\% to 58.1\%, but internal recall varies from 51.5\% to 81.8\%, reflecting threshold sensitivity. However, episode-level evaluation reveals that this apparent discrimination does not generalize: balanced accuracy drops to $47.1 \pm 2.2\%$ across 8 cross-split seeds (Appendix~\ref{app:seed-robustness}). Deployed end-to-end, the trained router allocates 97.0\% of episodes to deterministic computation with 17.6\% death rate, and misrouting cost (death from internally-routed episodes) exceeds the benefit of correctly routing rare internal-preferred cases.
122	
123	\paragraph{Evaluation methods.} All results use \emph{generation-based evaluation}: the model generates a routing label as text (\texttt{enable\_thinking=False}), pars
…[truncated 15037 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 582 · 2026-05-16T12:19:52.540686+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex",
  "offset": "300",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex",
    "offset": "300",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 583 · 2026-05-16T12:19:52.541133+00:00_

300	\label{fig:signal-reversal}
301	\end{figure}
302	
303	\begin{table}[h]
304	\centering
305	\small
306	\resizebox{\columnwidth}{!}{%
307	\begin{tabular}{@{}lccccc@{}}
308	\toprule
309	Environment & $N$ & Det\% & Int\% & NoPref\% & Death? \\
310	\midrule
311	ScienceWorld & 245 & 35.1 & 3.7 & 61.2 & Yes ($-100$) \\
312	MATH & 300 & 5.7 & 10.0 & 84.3 & No \\
313	ALFWorld & 135 & 25.9 & 1.5 & 72.6 & No\textsuperscript{$\dagger$} \\
314	\bottomrule
315	\end{tabular}}
316	\caption{Cross-environment label distribution. $\dagger$\,ALFWorld's deterministic advantage stems from action-space pruning, not death avoidance.}
317	\label{tab:cross-env}
318	\end{table}
319	
320	\end{document}
321	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 584 · 2026-05-16T12:19:57.912477+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 585 · 2026-05-16T12:19:58.314353+00:00_

1	\begin{abstract}
2	Modular LLM agents that route between neural reasoning and deterministic computation promise improved reliability, yet understanding \emph{what} drives the value of routing decisions remains unclear. We propose episode-level counterfactual analysis: running complete episodes under pure strategies and comparing final outcomes to decompose routing signal into death-avoidance and non-death components. Among task types exhibiting meaningful routing signal in prescreening (11 of 30 available ScienceWorld task types, 245 episodes, Qwen2.5-7B-Instruct), 78.9\% of non-tie routing labels (75 of 95) are driven by death asymmetry---a penalty-independent metric. Under the default penalty $P{=}100$, the Death Avoidance Factor (DAF) is $90.4\%$ (95\% CI: $[81.6\%, 98.8\%]$), though DAF varies from 50\% ($P{=}10$) to 98\% ($P{=}500$) across penalty settings (Appendix~\ref{app:penalty}). Per-task death rate correlates strongly with routing signal ($r{=}0.97$, though partly structural as death penalties contribute directly to score differences; \S\ref{sec:death-decomp}). An exploratory step-level router trained on these labels achieves $54.1 \pm 5.4\%$ step-level balanced accuracy (with same-episode leakage) but only $47.1 \pm 2.2\%$ on held-out episodes (below the always-deterministic baseline of 50\%); data scaling ($32{\times}$) and capacity scaling (0.6B--4B) confirm this is structural rather than data-limited. Cross-environment analysis on MATH ($N{=}300$) shows routing signal vanishes without a death penalty: the label distribution inverts from 86:9 (deterministic-preferred) to 30:17 (internal directionally favored), with a directional trend favoring internal reasoning ($+4.3$ percentage points, $p = 0.079$, not reaching $\alpha{=}0.05$). A Llama-3.1-8B pilot provides preliminary directional evidence that death-driven routing generalizes across model families. These findings indicate that in environments with catastrophic failure modes, routing value is do
…[truncated 123 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 586 · 2026-05-16T12:19:58.314731+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 587 · 2026-05-16T12:19:58.716612+00:00_

1	\section{Introduction}
2	
3	Large language models deployed as interactive agents must repeatedly decide \emph{how} to compute: reason internally, or delegate to an external tool.
4	A Qwen2.5-7B-Instruct agent navigating ScienceWorld \cite{scienceworld-2022}---a text-based science simulation with 30 task types---faces this choice at every step. Tracking temperature thresholds, container states, and multi-step procedures via internal reasoning is error-prone: the model may hallucinate that water has boiled when the stove was never activated, or that an object has been moved when the action was invalid. Deterministic external computation (environment simulators, code interpreters) eliminates such hallucinations via exact state transitions. The practical question for agent design is therefore: \emph{when should an agent route computation externally versus reasoning internally?}
5	
6	Existing routing approaches frame this as a capability or efficiency decision.
7	Toolformer \cite{toolformer-2023} teaches models to insert API calls when doing so reduces perplexity; ART \cite{art-2023} decomposes tasks into tool-augmented programs; Chameleon \cite{chameleon-2023} selects among heterogeneous modules (search, code, vision) per subtask.
8	More recent adaptive-computation methods route to different reasoning depths \cite{cogrouter-2026,ares-2026} or model tiers \cite{mtrouter-2026}.
9	The shared assumption is that routing signal stems from diverse sources---accuracy, latency, capability matching---and that a learned router can exploit this signal to improve over any fixed strategy.
10	But this assumption has never been systematically verified: \emph{what actually drives the value of routing decisions in interactive environments?}
11	
12	We find a surprisingly concentrated answer: \textbf{death avoidance accounts for 90.4\% of the routing signal} (DAF $= 90.4\%$, 95\% CI: $[81.6\%, 98.8\%]$; at default penalty $P{=}100$) in ScienceWorld.
13	The internal strategy's hallucinati
…[truncated 4757 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 588 · 2026-05-16T12:19:58.817621+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 589 · 2026-05-16T12:19:58.818230+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Problem Setup}
5	\label{sec:problem-setup}
6	
7	Consider an interactive environment $\mathcal{E}$ with state space $\mathcal{S}$, observation space $\mathcal{O}$, and action space $\mathcal{A}$. An agent follows a policy $\pi: \mathcal{O}^* \rightarrow \mathcal{A}$ that maps observation histories to actions. At each step $t$, the agent receives observation $o_t$, selects action $a_t = \pi(o_1, \ldots, o_t)$, and the environment transitions to state $s_{t+1}$.
8	
9	We define a modality set $\mathcal{M} = \{{\tt int}, {\tt det}\}$ governing how the agent processes state transitions:
10	\begin{itemize}
11	    \item \textbf{Internal} ($m = {\tt int}$): The agent uses its own generation to predict intermediate observations. The LLM interleaves chain-of-thought reasoning with environment actions following the ReAct paradigm \cite{react-2023}, but prediction errors compound across steps.
12	    \item \textbf{Deterministic} ($m = {\tt det}$): The agent receives ground-truth observations from the environment simulator at each step---equivalent to access to a perfect dynamics model. Action selection remains with the LLM; only the state-transition prediction is replaced.
13	\end{itemize}
14	
15	\noindent We restrict $\mathcal{M}$ to two modalities. An ablation comparing chain-of-thought reasoning (deep internal) against direct-answer generation (fast internal) on 6 overlapping task types found no significant difference on any task (Mann--Whitney $p > 0.26$, $|d| \leq 0.31$) and near-identical death rates (41.8\% vs.\ 42.5\%), confirming that reasoning depth does not meaningfully alter internal-mode outcomes in this setting.
16	
17	A \emph{routing policy} $\rho: \mathcal{O}^* \rightarrow \mathcal{M}$ selects which modality to use at each step. The goal of modality routing is to learn $\rho$ that maximizes expected episode return. Our analysis investigates what signal is available to learn such a router.
18	
19	\subsection
…[truncated 7623 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 590 · 2026-05-16T12:20:04.041113+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 591 · 2026-05-16T12:20:04.393116+00:00_

1	\section{Experiments}
2	
3	\subsection{Death Avoidance Decomposition}
4	\label{sec:death-decomp}
5	
6	\begin{figure}[t]
7	\centering
8	\includegraphics[width=\columnwidth]{figures/fig1_daf_scatter.pdf}
9	\caption{Per-task scatter: death rate differential (internal $-$ deterministic) vs.\ performance gap ($\Delta_{\text{full}}$). $r = 0.97$, $p < 10^{-6}$, $n = 11$ task types.}
10	\label{fig:decomposition}
11	\end{figure}
12	
13	Across 245 episodes, $\Delta_{\text{full}} = +29.60$; excluding death episodes, $\Delta_{\text{nd}} = +2.84$, yielding DAF $= 90.4\%$ (95\% CI: $[81.6\%, 98.8\%]$; at default $P{=}100$). The penalty-independent death-asymmetry label fraction is 78.9\% (75 of 95 non-tie labels). The internal strategy dies in 42.9\% of episodes versus 16.3\% for deterministic (2.6$\times$). Per-task, death rate differential correlates strongly with $\Delta_{\text{full}}$ ($r = 0.97$, $p < 10^{-6}$; Figure~\ref{fig:decomposition}; robustness diagnostics in Appendix~\ref{app:correlation}). Of 245 episodes, 86 are \texttt{det\_preferred}, 9 \texttt{internal\_preferred}, and 150 \texttt{no\_preference}.
14	
15	One exception: \texttt{find-non-living-thing} ($n{=}40$, zero deaths) has DAF $= 0\%$ with $\Delta = +9.58$ entirely from non-death score differences; all 10 remaining types exceed DAF $> 85\%$. Bootstrap 95\% CIs confirm $\Delta > 0$ for 10 of 11 types; \texttt{chemistry-mix} ($N{=}20$, $\Delta = 21.8$, 95\% CI $[-5.0, 48.6]$) is the sole exception (Appendix~\ref{app:per-task}).
16	
17	\subsection{Baselines}
18	\label{sec:baselines}
19	
20	\begin{table}[t]
21	\centering
22	\small
23	\resizebox{\columnwidth}{!}{%
24	\begin{tabular}{@{}lccc@{}}
25	\toprule
26	Strategy & Score & 95\% CI & Death \% \\
27	\midrule
28	Always-Internal & $-39.07$ & [$-46.40$, $-32.27$] & 42.9 \\
29	Always-Deterministic & $-9.47$ & [$-14.71$, $-4.29$] & 16.3 \\
30	Random & $-22.38$ & [$-28.67$, $-15.75$] & 27.8 \\
31	Oracle & $-6.58$ & [$-11.54$, $-1.70$] & 14.3 \\
32	\midrule
33	T
…[truncated 1784 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 592 · 2026-05-16T12:20:04.494261+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 593 · 2026-05-16T12:20:04.897267+00:00_

1	\section{Related Work}
2	
3	\paragraph{Tool Use and External Computation in LLMs.}
4	A growing body of work augments language models with external tools \citep{tool-learning-survey-2024}.
5	Toolformer \cite{toolformer-2023} teaches LLMs to insert API calls via self-supervised loss filtering; ART \cite{art-2023} decomposes tasks into tool-augmented programs; Chameleon \cite{chameleon-2023} composes heterogeneous modules per subtask; ReTool \cite{retool-2025} applies RL to discover when code execution is preferable to chain-of-thought.
6	These focus on \emph{learning to use tools}; we ask a prior question: \emph{what signal drives the routing decision?}
7	Recent concurrent work sharpens this question: \citet{tool-overuse-illusion-2026} identify a cognitive-illusion effect in LLM tool use, \citet{when2tool-2026} show tool-call decisions are encoded in hidden states before reasoning, \citet{tool-use-tax-2026} quantify a ``tool-use tax'' where tools degrade performance, and \citet{to-call-or-not-2026} propose a necessity--utility--affordability framework.
8	Our counterfactual decomposition provides environment-grounded evidence: in ScienceWorld, $90.4\%$ of routing signal at $P{=}100$ traces to catastrophic-failure prevention.
9	
10	\paragraph{Adaptive Computation and Routing.}
11	CogRouter \cite{cogrouter-2026} adapts reasoning depth per step, ARES \cite{ares-2026} selects among reasoning effort levels, Mixture-of-Recursions \cite{mixture-of-recursions-2025} learns token-level recursion depths, and MTRouter \cite{mtrouter-2026} addresses multi-turn routing across heterogeneous models.
12	RouteLLM \citep{routellm-2024} learns routers from preference data to select between strong and weak models.
13	These optimize \emph{how} to route; we reveal \emph{why} routing helps---in interactive environments, the dominant signal is catastrophic-failure avoidance.
14	
15	\paragraph{Counterfactual Evaluation in RL.}
16	Prior work generates counterfactual explanations for RL agents 
…[truncated 1587 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 403
}
```

</details>

---


### Tool call

_source line 594 · 2026-05-16T12:20:04.948102+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 595 · 2026-05-16T12:20:05.400637+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Cross-environment evidence.}
5	Does routing signal persist without catastrophic failure? On MATH Level~4--5 (300 problems), using a code interpreter as the deterministic modality, internal reasoning directionally outperforms: 81.0\% vs.\ 76.7\% accuracy ($+4.3$~pp, 95\% CI $[0.0, +8.7]$; McNemar $p = 0.079$, not reaching $\alpha{=}0.05$). The label distribution inverts: 30 internal-preferred vs.\ 17 deterministic-preferred (cf.\ 9:86 in ScienceWorld), with 84.3\% no-preference. In the absence of death risk, the deterministic advantage vanishes---consistent with death avoidance as the primary driver. A complementary evaluation on ALFWorld ($N{=}135$) confirms that the counterfactual framework identifies different routing mechanisms across environments: the deterministic advantage there stems from information asymmetry (access to admissible actions) rather than death avoidance (Appendix~\ref{app:cross-env}).
6	
7	\paragraph{Penalty sensitivity.}
8	The $r = 0.97$ correlation is specific to catastrophic death (score $= -100$); defining ``failure'' as any non-positive score yields $r = -0.13$ ($p = 0.70$). The correlation emerges only at $P \geq 50$ ($r = 0.86$) and reflects that non-death episodes show near-zero performance differential ($\Delta_{\text{nd}} = 2.84$; Appendix~\ref{app:penalty}). Death is effectively the \emph{only} component generating differential routing signal in ScienceWorld. These findings may be capability-dependent: the 42.9\% internal death rate reflects a 7B model's hallucination vulnerability; larger models with lower death rates would reduce DAF, potentially revealing non-death routing signal currently masked by catastrophic failures.
9	
10	\paragraph{Implications for router design.}
11	The dominance of death avoidance (DAF $= 90.4\%$ at $P{=}100$) reframes modality routing as primarily a \emph{safety} problem rather than an efficiency-quality tradeoff. The router functions as a s
…[truncated 663 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 596 · 2026-05-16T12:20:05.401196+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 597 · 2026-05-16T12:20:05.501965+00:00_

1	\section{Conclusion}
2	
3	We introduced episode-level counterfactual analysis for decomposing routing signal in modular LLM agents. Applied to 245 ScienceWorld episodes (11 of 30 task types, Qwen2.5-7B-Instruct), 78.9\% of non-tie routing labels (75 of 95) arise from death asymmetry. The DAF reaches $90.4\%$ (95\% CI: $[81.6\%, 98.8\%]$) at $P{=}100$, with strong cross-task correlation ($r = 0.97$, $p < 10^{-6}$).
4	
5	Cross-environment evidence supports this finding: on MATH ($N{=}300$), routing signal vanishes without death penalty, with a directional trend favoring internal reasoning ($+4.3$~pp, $p = 0.079$). An exploratory router trained on counterfactual labels achieves only $47.1 \pm 2.2\%$ on held-out episodes---below always-deterministic---a structural limitation confirmed by data and capacity scaling ablations.
6	
7	In environments with catastrophic failure modes, routing value is dominated by safety: the router functions as a safety critic rather than an efficiency optimizer. Open directions include step-level counterfactual labeling, stronger backbones with lower intrinsic death rates, and environments with graded failure costs.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 598 · 2026-05-16T12:20:12.382747+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines author instructions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines author instructions"
  }
}
```

</details>

---


### Tool call

_source line 599 · 2026-05-16T12:20:12.584175+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "simgate-modular-routing",
  "file": "decisions.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "simgate-modular-routing",
    "file": "decisions.yaml"
  }
}
```

</details>

---


### Tool result

_source line 600 · 2026-05-16T12:20:21.959440+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines author instructions"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Announcements | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"}]

I've found the official EMNLP 2026 Call for Papers submission guidelines and author instructions. Here's a summary of the key information:

## EMNLP 2026 Call for Main Conference Papers

### Paper Types and Content
EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. In addition to traditional r
…[truncated 1997 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "elapsed_ms": 9576
}
```

</details>

---


### Tool result

_source line 601 · 2026-05-16T12:20:21.960591+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/decisions.yaml\", \"content\": \"_next_id: 95\\ndecisions:\\n- id: D001\\n  date: 2026-05-13 04:25 UTC\\n  summary: 'MVP 方案: ScienceWorld 信号检测——验证确定性模拟是否在规则驱动任务上优于 LLM 内部推理'\\n  rationale: 12 天 deadline 下必须快速验证核心假设。ScienceWorld 是 primary track，其 JVM 后端提供精确的规则化状态转移，与\\n    LLM 近似推理的差距应该最大。选 5 task types × 10 episodes 的小规模 counterfactual 比较，不训练 router，纯信号检测。Pass\\n    标准 ≥2/5 task types >5pp，基于 ITP-R vs CogRouter 7.4pp 差距的量级。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-13 04:28 UTC\\n  summary: 采纳 Reviewer 全部 4 条 warning，修订 MVP 为 Phase 0 + Phase 1 两阶段方案\\n  rationale: Reviewer 指出 D001 方案 3 个操作层缺陷：(1) counterfactual 方法未明确——改为 episode-level\\n    3-way (always-internal / always-deterministic / oracle-routing)，oracle 作为 selective\\n    routing 上界；(2) N=10 统计功效不足——增加到 20 episodes/task type + bootstrap 90% CI；(3) kill\\n    criteria 不完整——增加 Phase 0 工程 gate、灰区 conditional pass、pre-register 5 task types\\n    (3S+1M+1W)。无额外 GPU 成本，仅设计层修正。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-13 07:43 UTC\\n  summary: GPU0 继续收集 baseline，GPU1 停下修复 tie-break + 致死动作过滤后重跑\\n  rationale: Fork 诊断发现两个方法论缺陷：(1) tie-break >= 使 95% delta=0 步骤 oracle 永远选 internal，oracle\\n    数据不可信；(2) 致死动作 (score=-100) 污染三条线。修 >= 为 >（oracle 仅在 deterministic 严格更优时介入）+ 致死动作过滤。不做\\n    N-step rollout——1-step 局限性是真实发现，MVP 应如实反映。GPU0 baseline 数据有效，不浪费已有进度。\\n  related_experiments:\\n  - exp_id: mvp-p1-gpu0\\n    role: baseline data, continue\\n  - exp_id: mvp-p1-gpu1-vllm\\n    role: kill, fix, rerun\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-13 08:13 UTC\\n  summary: MVP 判定 primary metric 改为 always-deterministic vs always-internal，oracle\\n    降为 supplementary\\n  rationale: 1-step lookahead 在稀疏 reward 下 95% 步骤 delta=0，任何 tie-break 都使 oracle 退化（>=\\n    → always-internal，> → always-determinist
…[truncated 10983 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 9376
}
```

</details>

---


### Tool call

_source line 602 · 2026-05-16T12:20:28.991957+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 May cycle formatting requirements page limit template ARR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 May cycle formatting requirements page limit template ARR"
  }
}
```

</details>

---


### Tool call

_source line 603 · 2026-05-16T12:20:31.000557+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing"
  }
}
```

</details>

---


### Tool result

_source line 604 · 2026-05-16T12:20:31.101491+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool result

_source line 605 · 2026-05-16T12:20:35.520626+00:00_

Web search results for query: "ACL Rolling Review 2026 May cycle formatting requirements page limit template ARR"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"acl2026/formatting.md at master · Lilaizhen/acl2026","url":"https://github.com/Lilaizhen/acl2026/blob/master/formatting.md"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on the search results, here's information about ACL Rolling Review 2026 May cycle formatting requirements:

## Page Limits

The paper follows page limits (8 for long, 4 for short, not including limitations and ethical considerations).

## Formatting Requirements

Review versions of long papers may have up to eight (8) pages of content plus unlimited pages for references. 

## Template and Style Files

ARR abandons the
…[truncated 1029 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "elapsed_ms": 6528
}
```

</details>

---


### Tool call

_source line 606 · 2026-05-16T12:20:43.351142+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 607 · 2026-05-16T12:20:43.351515+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 608 · 2026-05-16T12:20:43.671434+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 609 · 2026-05-16T12:20:43.745807+00:00_

1	- id: "R6-C1"
2	  summary: "DAF penalty-dependence — headline ~90% anchored to P=100, 78.9% not co-equal"
3	  category: method
4	  severity: critical
5	  status: in_progress
6	  first_raised_round: 4
7	  last_seen_round: 7
8	  mentions:
9	    - round: 6
10	      reviewers: [1, 2]
11	      note: "Fresh reviewers want full range + formula + dual reporting."
12	    - round: 7
13	      reviewers: [1, 2]
14	      note: "Resurfaced. Abstract still leads with DAF=90.41%. 78.9% present but not co-equal. R2 escalated to Must-Fix, R1 agreed on substance. Title 'Dominant' + P=10→46.4% tension unresolved."
15	  action_items:
16	    - round: 6
17	      action: "Abstract/Intro/§3.3/Conclusion dual reporting + DAF(P) formula in method.tex"
18	      assigned_to: main_agent
19	      status: done
20	    - round: 7
21	      action: "Promote 78.9% to primary metric in Abstract/Title; relegate DAF to secondary with explicit P-dependence caveat"
22	      assigned_to: main_agent
23	      status: done
24	  resolution: ""
25	  resolution_round: null
26	
27	- id: "R6-C2"
28	  summary: "Missing counterfactual-in-RL literature paragraph"
29	  category: writing
30	  severity: critical
31	  status: resolved
32	  first_raised_round: 6
33	  last_seen_round: 6
34	  mentions:
35	    - round: 6
36	      reviewers: [1, 2]
37	      note: "Paper uses 'counterfactual' in title, must contextualize."
38	  action_items:
39	    - round: 6
40	      action: "Add paragraph + 3 refs (Amitai AAAI'24, Gajcin AAMAS'23, Olson AIJ'21)"
41	      assigned_to: main_agent
42	      status: done
43	  resolution: "related_work.tex has 'prospective paired comparison vs post-hoc explanation' paragraph with all 3 citations."
44	  resolution_round: 6
45	
46	- id: "R6-W1"
47	  summary: "r=0.97 structural coupling not disclosed in Abstract/Contributions"
48	  category: writing
49	  severity: warning
50	  status: in_progress
51	  first_raised_round: 6
52	  last_seen_round: 7
53	  mentions:
54	    - round: 6
55	      reviewers: [
…[truncated 12672 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 74
}
```

</details>

---


### Tool call

_source line 610 · 2026-05-16T12:22:08.585016+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "8",
  "text": "## Round 8 审稿任务 — Reviewer 1（方法严谨性 + 实验有效性）\n\n### Venue 信息\n- **会议**: EMNLP 2026 (通过 ARR May 2026 cycle 提交)\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页 + 无限参考文献页\n- **模板**: ACL LaTeX (`\\usepackage[review]{acl}`)\n- **匿名**: Double-blind\n- **Limitations**: 必须有，不计入页数\n\n### 论文路径\n`projects/simgate-modular-routing/docs/paper/main.tex`（含 `\\input{abstract}`, `\\input{introduction}`, `\\input{method}`, `\\input{experiments}`, `\\input{related_work}`, `\\input{discussion}`, `\\input{conclusion}`）\n\n### 你的审查侧重\n1. **DAF 指标定义与解读**：DAF = 90.4% 在 P=100 下，但 P=10 时仅 50%。论文是否充分披露了 penalty-dependence？78.9% death-asymmetry label fraction（penalty-independent）是否被给予同等地位？\n2. **统计方法**：r=0.97 相关性是否存在结构性耦合（death penalty 直接贡献到 score difference 再去算相关）？bootstrap CI 是否可靠？n=11 task types 的 Pearson r 功效如何？\n3. **Router 诊断结论**：47.1±2.2% episode-level accuracy < 50% baseline。论文声称这是\"structural limitation\"。但数据量极小（81 train samples, ~8 internal-preferred）。data scaling ablation (25%-800%) 是否真正排除了 data scarcity？augmentation 方式是否引入了 artifact？\n4. **Cross-environment 证据强度**：MATH p=0.079 未达显著性水平，ALFWorld 无死亡机制。这些 cross-env 分析在多大程度上支持了论文的核心 claim？\n5. **Ablation 充分性**：capacity scaling (0.6B-4B) 范围是否足够？reasoning depth ablation 的 n 是多少？\n\n### 上轮遗留 Issue（需验证是否已修复）\n\n**Critical (必须验证)**:\n- **R6-C1**: DAF penalty-dependence — headline 是否仍锚定 P=100？78.9% 是否已提升为 co-equal metric？Abstract/Title 是否有 scope qualifier？\n- **R6-W2**: 19/30 task types 被排除（63%）— title/abstract/conclusion 是否加了 scope qualifier？是否分析了排除 task 的特征？\n- **R7-N2**: Router diagnostic 结论 — 是否承认了 data-size confound？Contribution 列表是否降级了此结论？data scaling ablation 是否充分？\n\n**Warning (需验证)**:\n- **R6-W1**: r=0.97 是否在 Abstract 中标注了 structural coupling qualifier？\n- **R7-W3**: Pure-strategy labeling vs mixed-strategy deployment gap — Limitations 是否讨论了 distribution shift？\n- **R7-W4**: 只测了 ReAct — Limitations 是否讨论了 Reflexion/ToT 可能降低 death rate？\n\n### 输出格式\n请按以下结构输出审稿意见：\n1. Summary (2-3句)\n2. Strengths (逐条)\n3. Weaknesses (逐条，标明 severity: Must-Fix / Should-Fix / Minor)\n4. 上轮 Issue 验证结果（逐条：[RESOLVED] / [PARTIALLY FIXED] / [NOT FIXED] / [NEW ISSUE]）\n5. Questions for Authors\n6. Overall Assessment (strong reject / weak reject / borderline / weak accept / strong accept) + Confidence (1-5)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "8",
    "text": "## Round 8 审稿任务 — Reviewer 1（方法严谨性 + 实验有效性）\n\n### Venue 信息\n- **会议**: EMNLP 2026 (通过 ARR May 2026 cycle 提交)\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页 + 无限参考文献页\n- **模板**: ACL LaTeX (`\\usepackage[review]{acl}`)\n- **匿名**: Double-blind\n- **Limitations**: 必须有，不计入页数\n\n### 论文路径\n`projects/simgate-modular-routing/docs/paper/main.tex`（含 `\\input{abstract}`, `\\input{introduction}`, `\\input{method}`, `\\input{experiments}`, `\\input{related_work}`, `\\input{discussion}`, `\\input{conclusion}`）\n\n### 你的审查侧重\n1. **DAF 指标定义与解读**：DAF = 90.4% 在 P=100 下，但 P=10 时仅 50%。论文是否充分披露了 penalty-dependence？78.9% death-asymmetry label fraction（penalty-independent）是否被给予同等地位？\n2. **统计方法**：r=0.97 相关性是否存在结构性耦合（death penalty 直接贡献到 score difference 再去算相关）？bootstrap CI 是否可靠？n=11 task types 的 Pearson r 功效如何？\n3. **Router 诊断结论**：47.1±2.2% episode-level accuracy < 50% baseline。论文声称这是\"structural limitation\"。但数据量极小（81 train samples, ~8 internal-preferred）。data scaling ablation (25%-800%) 是否真正排除了 data scarcity？augmentation 方式是否引入了 artifact？\n4. **Cross-environment 证据强度**：MATH p=0.079 未达显著性水平，ALFWorld 无死亡机制。这些 cross-env 分析在多大程度上支持了论文的核心 claim？\n5. **Ablation 充分性**：capacity scaling (0.6B-4B) 范围是否足够？reasoning depth ablation 的 n 是多少？\n\n### 上轮遗留 Issue（需验证是否已修复）\n\n**Critical (必须验证)**:\n- **R6-C1**: DAF penalty-dependence — headline 是否仍锚定 P=100？78.9% 是否已提升为 co-equal metric？Abstract/Title 是否有 scope qualifier？\n- **R6-W2**: 19/30 task types 被排除（63%）— title/abstract/conclusion 是否加了 scope qualifier？是否分析了排除 task 的特征？\n- **R7-N2**: Router diagnostic 结论 — 是否承认了 data-size confound？Contribution 列表是否降级了此结论？data scaling ablation 是否充分？\n\n**Warning (需验证)**:\n- **R6-W1**: r=0.97 是否在 Abstract 中标注了 structural coupling qualifier？\n- **R7-W3**: Pure-strategy labeling vs mixed-strategy deployment gap — Limitations 是否讨论了 distribution shift？\n- **R7-W4**: 只测了 ReAct — Limitations 是否讨论了 Reflexion/ToT 可能降低 death rate？\n\n### 输出格式\n请按以下结构输出审稿意见：\n1. Summary (2-3句)\n2. Strengths (逐条)\n3. Weaknesses (逐条，标明 severity: Must-Fix / Should-Fix / Minor)\n4. 上轮 Issue 验证结果（逐条：[RESOLVED] / [PARTIALLY FIXED] / [NOT FIXED] / [NEW ISSUE]）\n5. Questions for Authors\n6. Overall Assessment (strong reject / weak reject / borderline / weak accept / strong accept) + Confidence (1-5)"
  }
}
```

</details>

---


### Tool result

_source line 611 · 2026-05-16T12:22:28.630313+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 20045
}
```

</details>

---


### Tool call

_source line 612 · 2026-05-16T12:22:28.781567+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "8",
  "text": "## Round 8 审稿任务 — Reviewer 2（新颖性 + 完整性 + 写作质量）\n\n### Venue 信息\n- **会议**: EMNLP 2026 (通过 ARR May 2026 cycle 提交)\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页 + 无限参考文献页\n- **模板**: ACL LaTeX (`\\usepackage[review]{acl}`)\n- **匿名**: Double-blind\n- **Limitations**: 必须有，不计入页数\n\n### 论文路径\n`projects/simgate-modular-routing/docs/paper/main.tex`（含 `\\input{abstract}`, `\\input{introduction}`, `\\input{method}`, `\\input{experiments}`, `\\input{related_work}`, `\\input{discussion}`, `\\input{conclusion}`）\n\n### 你的审查侧重\n1. **贡献新颖性**：episode-level counterfactual analysis 作为方法贡献是否足够 novel？DAF 指标本身是否有独立价值（vs 简单的 death rate comparison）？\"router 训练失败\"作为 negative result 是否有足够贡献？\n2. **Related Work 覆盖**：是否覆盖了 (a) RouteLLM, (b) tool-learning survey (Qu 2024), (c) Reflexion, (d) safe RL 近年工作（不仅是 Garcia 2015 survey）, (e) 2025-2026 concurrent routing 工作？\n3. **Cross-environment 叙事一致性**：MATH ($p=0.079$) 在 Abstract/Intro/Discussion/Conclusion 中的表述是否一致？是否有过度解读 non-significant result 的情况？ALFWorld 分析的方法论描述是否充分？\n4. **论文组织与写作**：Abstract 是否过长？信息密度是否恰当？Contributions 列表是否准确反映了实际完成的工作（特别是 cross-model generalization claim）？\n5. **格式与 Bib**：ACL template 合规性；bib entries 的 year/author 准确性；figure/table 引用完整性；匿名规则遵守\n\n### 上轮遗留 Issue（需验证是否已修复）\n\n**Critical (必须验证)**:\n- **R6-C1**: DAF=90.4% 是否仍作为 headline number？78.9% 是否被提升为同等重要的 penalty-independent metric？\n- **R7-N1**: ALFWorld (Table 3, N=135) — 是否添加了完整方法论描述（model, deterministic modality definition, labeling process, episode length）？\n\n**Warning (需验证)**:\n- **R6-W8**: Safe RL literature — 是否添加了 1-2 个 specific safety critic 引用（CPO, CRPO, safety Q-functions 等）来支持 §5 \"router = safety critic\" claim？\n- **R7-W1**: MATH p=0.079 — \"routing signal vanishes\" 是否改为了更审慎的措辞？\n- **R7-W2**: Llama pilot N=10 — 是否从 Contribution 列表中移除？是否降级为 directional observation？\n- **R7-W5**: Missing references — RouteLLM (Ong 2024), Reflexion (Shinn 2023), tool-learning survey (Qu 2024) 是否已添加？\n\n**Info (快速检查)**:\n- **R7-m1**: retool-2026 key/year 和 dynathink-2025 author 是否修正？\n- **R7-m2**: Abstract DAF 精度是否改为 ~90%？GPU 描述是否已泛化？\n- **R7-m3**: find-non-living-thing 40 episodes 是否有解释？code/data release plan 是否明确？\n\n### 输出格式\n请按以下结构输出审稿意见：\n1. Summary (2-3句)\n2. Strengths (逐条)\n3. Weaknesses (逐条，标明 severity: Must-Fix / Should-Fix / Minor)\n4. 上轮 Issue 验证结果（逐条：[RESOLVED] / [PARTIALLY FIXED] / [NOT FIXED] / [NEW ISSUE]）\n5. Missing References (如有)\n6. Questions for Authors\n7. Overall Assessment (strong reject / weak reject / borderline / weak accept / strong accept) + Confidence (1-5)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "8",
    "text": "## Round 8 审稿任务 — Reviewer 2（新颖性 + 完整性 + 写作质量）\n\n### Venue 信息\n- **会议**: EMNLP 2026 (通过 ARR May 2026 cycle 提交)\n- **截止日期**: 2026-05-25\n- **页数限制**: 正文 8 页 + 无限参考文献页\n- **模板**: ACL LaTeX (`\\usepackage[review]{acl}`)\n- **匿名**: Double-blind\n- **Limitations**: 必须有，不计入页数\n\n### 论文路径\n`projects/simgate-modular-routing/docs/paper/main.tex`（含 `\\input{abstract}`, `\\input{introduction}`, `\\input{method}`, `\\input{experiments}`, `\\input{related_work}`, `\\input{discussion}`, `\\input{conclusion}`）\n\n### 你的审查侧重\n1. **贡献新颖性**：episode-level counterfactual analysis 作为方法贡献是否足够 novel？DAF 指标本身是否有独立价值（vs 简单的 death rate comparison）？\"router 训练失败\"作为 negative result 是否有足够贡献？\n2. **Related Work 覆盖**：是否覆盖了 (a) RouteLLM, (b) tool-learning survey (Qu 2024), (c) Reflexion, (d) safe RL 近年工作（不仅是 Garcia 2015 survey）, (e) 2025-2026 concurrent routing 工作？\n3. **Cross-environment 叙事一致性**：MATH ($p=0.079$) 在 Abstract/Intro/Discussion/Conclusion 中的表述是否一致？是否有过度解读 non-significant result 的情况？ALFWorld 分析的方法论描述是否充分？\n4. **论文组织与写作**：Abstract 是否过长？信息密度是否恰当？Contributions 列表是否准确反映了实际完成的工作（特别是 cross-model generalization claim）？\n5. **格式与 Bib**：ACL template 合规性；bib entries 的 year/author 准确性；figure/table 引用完整性；匿名规则遵守\n\n### 上轮遗留 Issue（需验证是否已修复）\n\n**Critical (必须验证)**:\n- **R6-C1**: DAF=90.4% 是否仍作为 headline number？78.9% 是否被提升为同等重要的 penalty-independent metric？\n- **R7-N1**: ALFWorld (Table 3, N=135) — 是否添加了完整方法论描述（model, deterministic modality definition, labeling process, episode length）？\n\n**Warning (需验证)**:\n- **R6-W8**: Safe RL literature — 是否添加了 1-2 个 specific safety critic 引用（CPO, CRPO, safety Q-functions 等）来支持 §5 \"router = safety critic\" claim？\n- **R7-W1**: MATH p=0.079 — \"routing signal vanishes\" 是否改为了更审慎的措辞？\n- **R7-W2**: Llama pilot N=10 — 是否从 Contribution 列表中移除？是否降级为 directional observation？\n- **R7-W5**: Missing references — RouteLLM (Ong 2024), Reflexion (Shinn 2023), tool-learning survey (Qu 2024) 是否已添加？\n\n**Info (快速检查)**:\n- **R7-m1**: retool-2026 key/year 和 dynathink-2025 author 是否修正？\n- **R7-m2**: Abstract DAF 精度是否改为 ~90%？GPU 描述是否已泛化？\n- **R7-m3**: find-non-living-thing 40 episodes 是否有解释？code/data release plan 是否明确？\n\n### 输出格式\n请按以下结构输出审稿意见：\n1. Summary (2-3句)\n2. Strengths (逐条)\n3. Weaknesses (逐条，标明 severity: Must-Fix / Should-Fix / Minor)\n4. 上轮 Issue 验证结果（逐条：[RESOLVED] / [PARTIALLY FIXED] / [NOT FIXED] / [NEW ISSUE]）\n5. Missing References (如有)\n6. Questions for Authors\n7. Overall Assessment (strong reject / weak reject / borderline / weak accept / strong accept) + Confidence (1-5)"
  }
}
```

</details>

---


### Tool call

_source line 613 · 2026-05-16T12:22:29.033174+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "simgate-modular-routing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "simgate-modular-routing"
  }
}
```

</details>

---


### Tool result

_source line 614 · 2026-05-16T12:22:30.194217+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1412
}
```

</details>

---


### Tool result

_source line 615 · 2026-05-16T12:22:30.194728+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 1161
}
```

</details>

---


### Tool call

_source line 616 · 2026-05-16T12:22:35.224191+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "simgate-modular-routing",
  "file": "memory.md",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "simgate-modular-routing",
    "file": "memory.md",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 617 · 2026-05-16T12:22:35.274932+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/memory.md\", \"content\": \"# Memory — simgate-modular-routing\\n\\n## 经验教训\\n\\n### 🔴 GPU 进程启动硬性规定 (2026-05-16, Director 强制)\\n1. 任何实验进程启动前必须先注册 RUNNING\\n2. 启动 GPU 进程前必须 `nvidia-smi` 确认目标 GPU 空闲\\n3. 多 GPU 时必须 `CUDA_VISIBLE_DEVICES=X` 隔离，不要只用 `--gpu_id`\\n4. 脚本必须增量保存结果（每个 run 完成即写入），不要攒到最后\\n原因：r7n2 四次事故——3 次 OOM (eval batch 8→4→2)，1 次 SIGHUP 导致 9 个 run 结果全丢，1 次 rescue Worker 差点 OOM GPU0。\\n\\n### ⚠️ Majority-vote baseline: 所有 task types 都是 det-dominant (2026-05-16)\\n11 个 task_type 的 majority label 全部是 \\\"deterministic\\\"（train set 91.4% det）。TT-majority-vote = always-det = 0.5000 balanced_acc。Router cross-split 47.1% 比 always-det 还差 2.9pp——router 在 unseen episodes 上错误预测了多余的 \\\"internal\\\"。\\\"Signal at task-type level\\\" 的准确含义是 \\\"always use det\\\"，与 C1 death avoidance 预测一致。Episode-level split seeds 123/456 的 val set 100% det（无 internal 样本），只有 seed=42 给出有信息量的评估。\\n\\n### ⚠️ Cross-split robustness 失败：Router 不能跨 episode 泛化 (2026-05-16)\\ncross-split-robustness-8seed 结果：episode-level held-out balanced_acc=47.1±2.2%，比 step-level corrected eval (54.1±5.4%) 低 7pp，低于随机 50%。Router 在 step-level split 中 memorize 了 episode 内局部模式（65/66 episodes 跨越 train/val），但不能泛化到完全未见 episode。核心推论：routing signal 在 task-type level 而非 episode level。C1 (death avoidance) 不受影响（基于 counterfactual analysis，不依赖 router）。C2 (router as diagnostic probe) 需 scope 到 task-type level。Narrative A 已被 Director 批准 (D086)。\\n\\n### ⚠️ Seed 42 adapter split 不一致 (2026-05-16)\\n`checkpoints/plan-008-qwen3-1.7b/final_adapter/`（seed 42）使用 **episode-level stratified split**（56 train / 10 val episodes → 1740/300 steps），而 seeds 43-49 使用 `load_implicit_sft_data` 的 **step-level** split（同 episode steps 跨 train/val）。8-seed 汇总（55.7±5.0%）中 seed 42 的 eval 条件与其余 7 个不同。plan-008 训练脚本与 seed-robustness 脚本使用了不同的 split 函数。教训：多 seed 实验必须统一 eval pipeline，不能混用不同实验的 checkpoint。\\n\\n### ⚠️ ga=1 s
…[truncated 1398 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 618 · 2026-05-16T12:22:39.241258+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---


### Tool result

_source line 619 · 2026-05-16T12:22:39.342244+00:00_

Found 4 files
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/logs/chats/feishu_group_oc_0b622d6038b969b96148ee8a163a1a0c_director.jsonl
AGENTS.md
CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/logs/workers/worker_research_sighup-root-cause_20260514T021418.log

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Grep",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 620 · 2026-05-16T12:22:43.007606+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review.*enabled",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review.*enabled",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 621 · 2026-05-16T12:22:43.109769+00:00_

AGENTS.md:82:如果项目配置了外部审稿（`external_review.paperreview_ai.enabled: true`）：
CLAUDE.md:82:如果项目配置了外部审稿（`external_review.paperreview_ai.enabled: true`）：
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/logs/chats/feishu_group_oc_0b622d6038b969b96148ee8a163a1a0c_director.jsonl:17:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/logs/chats/feishu_group_oc_0b622d6038b969b96148ee8a163a1a0c_director.jsonl:193:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/logs/chats/feishu_group_oc_0b622d6038b969b96148ee8a163a1a0c_director.jsonl:329:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/logs/chats/feishu_group_oc_0b622d6038b969b96148ee8a163a1a0c_director.jsonl:372:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/logs/chats/feishu_group_oc_0b622d6038b969b96148ee8a163a1a0c_director.jsonl:389:{"ts": "2026-05-15T00:01:24.450067+00:00", "role": "tool", "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director", "text": "called Grep", "tool": "Grep", "tool_args": {"pattern": "external_review|paperreview_ai|enabled", "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/registry.yaml", "output_mode": "content", "head_limit": "50"}}
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/logs/chats/feishu_group_oc_0b622d6038b969b96148ee8a163a1a0c_director.jsonl:394:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/logs/chats/feishu_group_oc_0b622d6038b969b96148ee8a163a1a0c_director.jsonl:395:{"ts": "2026-05-15T00:01:28.661881+00:00", "role": "tool", "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director", "text": "called Bash", "tool": "Bash", "tool_args": {"comma
…[truncated 2809 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Grep",
  "elapsed_ms": 102
}
```

</details>

---


### Assistant

_source line 622 · 2026-05-16T12:22:55.686965+00:00_

外部审稿未配置（`status: not_requested`，项目未启用 `paperreview_ai`），本轮仅依赖内部圆桌。

**当前状态**：
- Reviewer 1（方法严谨性）已触发 ✓
- Reviewer 2（新颖性/完整性）已触发 ✓
- 外部审稿：未启用，跳过

等待两位 Reviewer 独立初审返回。收到后进入交叉分享阶段（Step 2）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 56

## Round 56

2 recorded events


### User

_source line 623 · 2026-05-16T12:25:35.877863+00:00_

[Reviewer 1 审稿意见]:
## Round 8 审稿意见 — Reviewer 1

### 1. Summary

本文提出 episode-level counterfactual analysis 方法，分析模块化 LLM agent 中路由信号的来源。在 ScienceWorld 的 11/30 任务类型（245 episodes）上，发现 78.9% 的非平局路由标签源自 death asymmetry（penalty-independent），DAF 在 P=100 时达 90.4%。论文同时训练了一个探索性 step-level router，发现其在 held-out episodes 上低于 always-deterministic baseline，并通过 data/capacity scaling 确认这是结构性限制。跨环境对比（MATH/ALFWorld）提供方向性支持证据。

### 2. Strengths

- **S1**: 方法论贡献清晰——episode-level counterfactual analysis 在 sparse-reward 环境中解决了 step-level oracle 退化问题，是一个实用且可复现的框架。
- **S2**: 透明度极高——论文主动披露 DAF 的 penalty-dependence（Abstract 中即标明 50%-98% 范围），r=0.97 的 structural coupling（Abstract 中加了 qualifier），11/30 task 的 scope（Title 中加了 "on ScienceWorld"）。相比前轮，disclosure 质量显著提升。
- **S3**: 78.9% death-asymmetry label fraction 作为 penalty-independent companion metric 与 DAF 并列呈现，解决了指标锚定问题。
- **S4**: Robustness diagnostics 丰富——LOO（Table 4）、bootstrap CI、Spearman ρ=0.986、anti-cherry-picking paragraph（Appendix B）均增强了主要发现的可信度。
- **S5**: Labeling quality audit（Appendix A）排除了 oracle circularity，zero labels depend on tie-breaking——这是一个重要的完整性检查。
- **S6**: 论文对 router failure 的诚实报告（47.1±2.2% < 50% baseline）比隐藏负面结果更有科学价值。

### 3. Weaknesses

**W1** [Should-Fix] **Data scaling ablation 的 minority-class confound**
- 具体位置：Appendix E, Table 5
- 问题：augmentation 使用 "synonym substitution + template variation on step observations"，这只增加 surface diversity，不增加 episode diversity。更关键的是，augmentation 使 majority class 比例从 89.6%（100%）上升到 97.7%（800%），internal-preferred episodes 始终只有原始的 ~8-9 个 episode 的变体。论文声称 "rules out data scarcity"，但实际上 augmentation 没有引入任何新的 minority-class routing patterns。在 25% unaugmented scale 已经 collapse 的事实确实有力，但论文应明确区分 "step-level data scarcity" 和 "episode-level minority-class scarcity"——后者才是真正的瓶颈，且 32× scaling 完全没有解决它。
- 建议：(1) 明确承认 augmentation 无法解决 episode-level minority-class scarcity；(2) 考虑加一句 "a definitive data-scarcity test would require collecting more internal-preferred episodes from additional task types or environments, which is impossible given the observed 86:9 ratio is the ground truth"；(3) 或者将结论从 "rules out data scarcity" 软化为 "consistent with a structural limitation, though cannot definitively rule out that more diverse minority-class episodes would help"。

**W2** [Should-Fix] **Capacity scaling 范围偏窄（0.6B-4B）**
- 具体位置：Appendix G
- 问题：0.6B、1.7B、4B 三个点均为小模型，且 step-level 评估（52.8%、54.1%、53.5%）没有明确趋势。但 step-level evaluation 本身有 same-episode leakage（论文已承认）。更关键的是：论文未在 episode-level 上报告 capacity scaling 结果——只有 step-level 数据。如果 episode-level 在所有 capacity 下都是 ~47-50%，这才是真正排除 capacity 限制的证据。
- 建议：补充 episode-level capacity scaling 结果；或明确声明 capacity scaling ablation 仅在 step-level 评估，因此对 episode-level generalization 的结论力度有限。

**W3** [Minor] **Reasoning depth ablation 的 sample size 未报告**
- 具体位置：§3.1 (Method) 和 Appendix G
- 问题：ablation 报告 "6 task types"，Mann-Whitney p>0.26，|d|≤0.31，但未报告 episode 数量。如果 n 很小（如每种 task 仅 5 episodes = 30 total），power 不足以检测 medium effect sizes。
- 建议：报告 n（total episodes per condition）并计算 post-hoc power。

**W4** [Minor] **Cross-environment evidence 的 claim 精度**
- 具体位置：§5 Discussion, Conclusion
- 问题：MATH 结果 p=0.079 未达显著性，论文正确报告了这一点。但 Conclusion 中 "routing signal vanishes without death penalty" 的措辞略超出 p=0.079 所支持的结论。严格来说，p=0.079 表明 "未能拒绝 null hypothesis"，而非 "signal vanishes"。
- 建议：Conclusion 中将 "routing signal vanishes" 修改为 "the deterministic advantage is not detected (p=0.079)" 或类似更保守的措辞。

**W5** [Minor] **r=0.97 的 structural coupling 已被承认但仍需更显式的量化**
- 具体位置：§4.1, Appendix D
- 问题：Abstract 和 Discussion 都承认了 structural coupling。Appendix D Table 6 清楚展示了 correlation 随 P 变化。但论文可以更显式地指出：由于 Δ_full ≈ δ·P + Δ_nd 且 Δ_nd 各 task 近似常数（mean non-death gap = -1.19 excl. outlier），r=0.97 在数学上几乎是必然的——它证明的是 Δ_nd 的近似均匀性（即 non-death signal 缺乏 task-specific variation），而非 death 的"预测力"。
- 建议：在 §4.1 或 Discussion 中加一句明确指出这一数学必然性的解读——"The high correlation reflects the near-uniformity of Δ_nd across task types rather than a predictive relationship"——使读者不会误读 r=0.97 为独立于 DAF decomposition 的额外证据。

### 4. 上轮 Issue 验证结果

**[RESOLVED] R6-C1**: DAF penalty-dependence 已充分披露。Abstract 中 DAF=90.4% 后立即标注 "though DAF varies from 50% (P=10) to 98% (P=500)"。78.9% penalty-independent metric 在 Abstract、Introduction、Experiments、Conclusion 中均出现，地位对等。Title 有 "on ScienceWorld" scope qualifier。

**[RESOLVED] R6-W2**: 19/30 task types 排除问题已解决。Title/Abstract 有 scope qualifier（"11 of 30"、"on ScienceWorld"）。Appendix B 包含 anti-cherry-picking paragraph，分析了 included vs excluded 的 death rate（17.8% vs 14.9%，无显著差异），并解释排除原因（both strategies time out）。

**[PARTIALLY FIXED] R7-N2**: Router diagnostic 结论——论文使用 "exploratory" qualifier，承认了 data scaling 的局限性。但 data scaling ablation 的方法论缺陷（augmentation 不增加 episode diversity，minority class 未真正 scaled）仍存在（见 W1）。Contribution 列表已适当降级（"An exploratory router...fails to outperform"）。

**[RESOLVED] R6-W1**: r=0.97 structural coupling 已在 Abstract 中标注 qualifier："though partly structural as death penalties contribute directly to score differences"。

**[RESOLVED] R7-W3**: Pure-strategy vs mixed-strategy distribution shift 已在 Limitations 中讨论，cite DAgger (2011)。

**[RESOLVED] R7-W4**: ReAct 唯一性已在 Limitations 中讨论，明确提到 Reflexion 可能降低 death rate。

### 5. Questions for Authors

Q1: Data scaling ablation 中，800% scale 的 internal-preferred episodes 是否仍然只是原始 ~8-9 个 episode 的 paraphrase variants？如果是，这是否真正测试了 "data scarcity" 假设？

Q2: Capacity scaling（0.6B-4B）在 episode-level 的表现如何？是否也呈现与 step-level 相似的 flat pattern？

Q3: 在 78.9% death-asymmetry labels 中，有多少是因为 internal 策略死亡（而 deterministic 存活）vs. deterministic 策略死亡（而 internal 存活）？从 Table 3 看是 70:5。这是否意味着一个简单的 "internal 策略 death predictor" 就足够了，routing 问题可以完全简化为单策略 death prediction？

Q4: 论文提到 "find-non-living-thing" 是 zero-death outlier（DAF=0%, Δ=+9.58）。这个 task 的 non-death routing signal 来自什么？是否分析过这些 non-death-driven labels 的特征，以理解 post-death-avoidance routing 的可能性？

Q5: Reasoning depth ablation 的 episode 总数是多少？Mann-Whitney test 的统计检验力（在 medium effect size d=0.5 下）是否足够？

### 6. Overall Assessment

**Overall**: 3.5/5 — Borderline to Weak Accept (Findings track)

**Confidence**: 4/5 — 对方法论和统计问题有较高确信度

---

**官方维度打分（ACL ARR Review Form）**

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 核心 decomposition 方法合理，disclosure 充分。但 data scaling ablation 存在方法论缺陷（不增加 episode diversity），capacity scaling 仅报告 step-level。主要 claim 有充分支撑，但"structural limitation"结论的证据链有一个弱环节。 |
| Excitement | 3/5 | 负面结果（router 不 work）+ 分析性贡献。方法论有价值但 scope 较窄（单环境、单模型为主）。"Safety critic" 框架有启发性但缺乏 actionable follow-up。 |
| Overall | 3.5/5 | 透明度高、方法论清晰、自我批判诚实。主要问题（W1-W2）属于 should-fix 级别，不影响核心发现的有效性，但影响 "structural limitation" 子结论的说服力。适合 Findings track。 |
| Reproducibility | 4/5 | 超参数完整（Table 2），seeds 报告，数据收集流程可复现。代码/数据承诺 release。唯一缺失：reasoning depth ablation 的 n 未报告。 |

**一句话总结**: 论文在透明度和自我批判方面达到了高标准，核心 decomposition 发现（78.9% death-asymmetry labels）well-supported；主要残余问题是 data scaling ablation 的方法论缺陷使 "structural limitation" 结论不够坚实，但不影响核心 claim。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 624 · 2026-05-16T12:25:55.485325+00:00_

Reviewer 1 审稿意见已收到。评分 3.5/5 (Borderline to Weak Accept)，核心发现认可，主要关注 data scaling ablation 方法论缺陷和 capacity scaling 仅报告 step-level 的问题。

等待 Reviewer 2 提交审稿意见后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 57

## Round 57

2 recorded events


### User

_source line 625 · 2026-05-16T12:25:57.960411+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交。总结：

- **Overall: 3.5/5 (Borderline to Weak Accept, Findings track)**
- 上轮 6 个 issue 中 5 个 RESOLVED，1 个 PARTIALLY FIXED（R7-N2 data scaling ablation 方法论）
- 新增 5 个 weakness：W1 (data scaling 的 minority-class confound, Should-Fix)、W2 (capacity scaling 仅 step-level, Should-Fix)、W3-W5 (Minor)
- 核心 decomposition 发现（78.9% death-asymmetry labels）well-supported，论文透明度显著提升
- 主要残余问题：data scaling ablation 用 paraphrase augmentation 无法真正增加 episode diversity，使 "rules out data scarcity" 结论不够坚实

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 626 · 2026-05-16T12:26:05.424581+00:00_

Reviewer 1 审稿意见已收到。等待 Reviewer 2 完成独立初审后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 58

## Round 58

6 recorded events


### User

_source line 627 · 2026-05-16T12:29:30.127657+00:00_

[Reviewer 2 审稿意见]:
## Round 8 审稿意见 — Reviewer 2（新颖性 + 完整性 + 写作质量）

### 1. Summary

本文提出 episode-level counterfactual analysis 方法来分解模块化 LLM agent 中的 routing signal，发现在 ScienceWorld 环境中，78.9% 的非 tie routing label 源于 death asymmetry（penalty-independent），DAF 在 P=100 下达到 90.4%。论文进一步展示 trained router 无法超越 always-deterministic baseline（47.1% vs 50.0% episode-level），并通过 MATH 和 ALFWorld 的 cross-environment 分析提供支撑证据。整体是一篇聚焦的 empirical insight paper，分析严谨但范围受限。

### 2. Strengths

- **S1**: 双指标设计（penalty-independent 的 78.9% label fraction + penalty-dependent DAF）比前版本显著改善了核心发现的可信度，读者可以自行判断 penalty 选择的影响。
- **S2**: Router failure 的诊断非常彻底——data scaling（32×）、capacity scaling（0.6B–4B）、per-task-type breakdown、classification head vs. SFT 对比——系统排除了简单假设，形成强力的 negative result。
- **S3**: Penalty sensitivity analysis（Appendix A.4, Table 5–6）和 mechanism boundary（threshold-specific correlation, r=0.97 at P=100 vs r=-0.13 at T=0）深化了 insight 的边界条件。
- **S4**: Related work 现在覆盖全面——RouteLLM、Reflexion、tool-learning survey、CRPO 均已纳入；2025–2026 concurrent routing 工作覆盖到位（6篇）。
- **S5**: Limitations section 诚实且具体——19 个排除 task types、episode-level label 的局限性、DAgger distribution shift、Llama pilot 的统计不足都被明确承认。

### 3. Weaknesses

**W1 [Should-Fix]** "routing signal vanishes" 措辞仍然 overstate non-significant result

Abstract 和 Conclusion 均写 "routing signal vanishes without a death penalty"，但 MATH 结果是 p=0.079（未达 α=0.05），95% CI [0.0, +8.7]。"vanishes" 暗示 signal 不存在，但 30:17 的 label distribution 和 +4.3 pp 的 directional trend 恰恰说明存在 signal——只是方向反转且未达显著。更准确的措辞应为 "the deterministic advantage disappears" 或 "death-driven routing signal is absent"。此外，Conclusion 中 "p = 0.079" 后缺少 "not reaching α=0.05" 的 hedge（Abstract 和 Introduction 中有此限定），造成叙事不一致。

**W2 [Should-Fix]** "Deterministic modality" 定义跨环境不一致，削弱 cross-environment 比较的说服力

ScienceWorld 中 deterministic = ground-truth observations（perfect dynamics model）；MATH 中 = code interpreter；ALFWorld 中 = admissible actions access。论文对 ALFWorld 明确标注了 "information asymmetry rather than a computation mode switch"（Appendix A.9），但 MATH 的 code interpreter 同样不是 ScienceWorld 意义上的 "deterministic computation"——它引入了代码生成、执行、debugging 等额外变量。Discussion §5 第一段将三个环境并列作为 "cross-environment evidence"，却未讨论 modality 定义的异质性对结论可迁移性的影响。建议在 Method 或 Discussion 中增加一段明确 modality 在各环境中的操作化定义，并讨论这一差异如何影响 DAF 的跨环境可比性。

**W3 [Should-Fix]** 11/30 task types 选择的 generalizability concern 未充分回应

63% 的 ScienceWorld task types 被排除（"both strategies time out"）。Appendix A.2 论证了 included vs excluded 的 death rate 相似（17.8% vs 14.9%），但这仅说明 death rate 无 selection bias，不能说明 routing signal 的结构相似。排除的 task types 可能存在不同的 failure modes（如 timeout 而非 death），其 routing signal 结构可能完全不同。论文的 central claim "death avoidance accounts for X% of routing signal" 实际上只适用于 "有 routing signal 的 task types"，但这一限定在 Abstract 和 Conclusion 中的表述不够显著。

**W4 [Minor]** Abstract 信息过载

Abstract 约 250 词，包含 DAF、penalty sensitivity range、78.9%、router training 结果、MATH、Llama pilot——信息密度高到几乎是 extended abstract。建议删减 penalty sensitivity range 和 Llama pilot 的 mention，专注于核心发现和最重要的验证结果。

**W5 [Minor]** "Safety critic" 类比过度延伸

Discussion 将 router 比作 "safety critic"（safe RL 中的术语），但 safe RL 中的 safety critic 是主动学习的约束机制，而本文的发现是 always-deterministic 就是最优策略——这更像是 "default to safe modality"，而非 learned safety critic。CRPO 的引用确认了 safe RL 的相关性，但类比本身不够精确。

**W6 [Minor]** Bib 中有 3 个 orphan entries

toolkengpt-2023、tot-2023、voyager-2023 在 bib 中存在但未被引用。tool-learning-survey-2024 的 bib year 为 2024，但 OpenAlex 记录为 2025 出版——应核实并统一。

### 4. 上轮 Issue 验证结果

| Issue | 状态 | 说明 |
|-------|------|------|
| **R6-C1** DAF 90.4% headline + 78.9% 提升 | [RESOLVED] | 78.9% 现在在 Abstract/Intro/Method/Experiments 中均先于或与 DAF 并列出现，明确标注 "penalty-independent metric"。双指标设计是本轮最重要的改进。 |
| **R7-N1** ALFWorld 方法论描述 | [RESOLVED] | Appendix A.9 现包含 model (Qwen2.5-7B)、deterministic modality 定义（admissible actions）、episode count (135)、max steps (50)、success metric (binary)。 |
| **R6-W8** Safe RL specific citation | [RESOLVED] | CRPO (Xu et al., 2021) 已添加至 Related Work §Safe RL 段落。 |
| **R7-W1** MATH "routing signal vanishes" 措辞 | [PARTIALLY FIXED] | 已添加 "directional trend" 和 "not reaching α=0.05" 限定，但 "vanishes" 一词仍保留在 Abstract 和 Conclusion 中，且 Conclusion 缺少 "not reaching α=0.05" hedge。见 W1。 |
| **R7-W2** Llama pilot 从 Contribution 列表移除 | [RESOLVED] | Contribution 列表中无 Llama/cross-model claim。降级为 "preliminary pilot" + "directionally consistent"。 |
| **R7-W5** 缺失 references | [RESOLVED] | RouteLLM、Reflexion、tool-learning survey 均已添加并引用。 |
| **R7-m1** retool key/year, dynathink author | [RESOLVED] | retool-2025 key/year 已修正（OpenAlex 验证通过）。dynathink-2025 author 格式正确。 |
| **R7-m2** Abstract DAF 精度 + GPU 描述 | [RESOLVED] | DAF 90.4% 保留精确值但附 CI；GPU 改为 "two consumer GPUs"。 |
| **R7-m3** find-non-living-thing 40 eps + code/data release | [RESOLVED] | Table 4 脚注解释了两批收集；Ethics Statement 明确 release plan。 |

### 5. Missing References

核心 references 已覆盖。可选改进：
- FrugalGPT (Chen et al., 2023) / HybridLLM (Ding et al., 2024) — cost-quality routing 先驱，与 "routing as safety vs efficiency" framing 直接相关
- 若要加强 "safety critic" 类比：CPO (Stooke et al., 2020) 或 safety Q-functions

### 6. Questions for Authors

**Q1**: MATH 中 code interpreter 作为 "deterministic modality" 与 ScienceWorld 中 ground-truth observations 的类比是否成立？Code interpreter 本身有 failure modes（syntax error、runtime error），这如何影响 DAF 跨环境可比性？

**Q2**: 19 个被排除的 task types 中，有多少因 timeout 而非 death 失败？如果 timeout 也是一种 "catastrophic failure"，DAF 分析是否应将其纳入？

**Q3**: Discussion 中说 "larger models with lower death rates would reduce DAF, potentially revealing non-death routing signal currently masked by catastrophic failures"——这是否意味着本文核心发现可能是 model capability 的 artifact 而非 environment structure 的 fundamental property？

### 7. Overall Assessment

**Overall**: 3.0/5 (Findings acceptance)
**Confidence**: 4/5

**Rationale**: 论文在选定范围内做了扎实的实验分析——DAF 分解、router diagnostic、penalty sensitivity、cross-environment checks 构成完整的 evidence chain。Round 6–7 的关键问题（DAF vs 78.9% 双指标、ALFWorld 方法论、missing references）已全部修复。

阻碍 main conference acceptance 的主要因素：(1) 核心发现绑定于 ScienceWorld 的特定 failure structure（-100 death penalty），generalizability 有限；(2) episode-level counterfactual analysis 方法论本身较为直接（paired comparison under two policies），方法创新性不足以单独支撑贡献；(3) MATH cross-environment validation 未达统计显著性，且 "deterministic modality" 定义跨环境不一致，削弱了 cross-environment 叙事。作为 Findings paper，insight 的清晰度和分析的彻底性达到 publishable 水平。

### 参考验证摘要（自动化工具）
- 29 bib entries, 26 cited, 3 orphan (toolkengpt, tot, voyager)
- 24/29 OpenAlex verified, 3 not found (react-2023/mixture-of-recursions-2025/gajcin2023 — likely API coverage gaps), 2 minor mismatches (dynathink author parsing, garcia accent)
- 0 missing bib entries (all citations have corresponding bib entries)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 628 · 2026-05-16T12:29:54.593541+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "8",
  "text": "## 交叉分享 — Reviewer 2 的完整审稿意见\n\n请逐条回应 Reviewer 2 的 Weaknesses：对每条标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 2 的完整审稿意见：\n\n### Summary\n本文提出 episode-level counterfactual analysis 方法来分解模块化 LLM agent 中的 routing signal，发现在 ScienceWorld 环境中，78.9% 的非 tie routing label 源于 death asymmetry（penalty-independent），DAF 在 P=100 下达到 90.4%。论文进一步展示 trained router 无法超越 always-deterministic baseline（47.1% vs 50.0% episode-level），并通过 MATH 和 ALFWorld 的 cross-environment 分析提供支撑证据。整体是一篇聚焦的 empirical insight paper，分析严谨但范围受限。\n\n### Strengths\n- S1: 双指标设计（penalty-independent 的 78.9% label fraction + penalty-dependent DAF）比前版本显著改善了核心发现的可信度。\n- S2: Router failure 的诊断非常彻底——data scaling（32×）、capacity scaling（0.6B–4B）、per-task-type breakdown、classification head vs. SFT 对比。\n- S3: Penalty sensitivity analysis 和 mechanism boundary（r=0.97 at P=100 vs r=-0.13 at T=0）深化了 insight 的边界条件。\n- S4: Related work 覆盖全面——RouteLLM、Reflexion、tool-learning survey、CRPO 均已纳入。\n- S5: Limitations section 诚实且具体。\n\n### Weaknesses\n\n**W1 [Should-Fix]** \"routing signal vanishes\" 措辞仍然 overstate non-significant result\n- Abstract 和 Conclusion 均写 \"routing signal vanishes without a death penalty\"，但 MATH 结果是 p=0.079（未达 α=0.05），95% CI [0.0, +8.7]。\"vanishes\" 暗示 signal 不存在，但 30:17 的 label distribution 和 +4.3 pp 的 directional trend 说明存在 signal——只是方向反转且未达显著。更准确的措辞应为 \"the deterministic advantage disappears\" 或 \"death-driven routing signal is absent\"。Conclusion 中 \"p=0.079\" 后缺少 \"not reaching α=0.05\" 的 hedge。\n\n**W2 [Should-Fix]** \"Deterministic modality\" 定义跨环境不一致，削弱 cross-environment 比较\n- ScienceWorld 中 deterministic = ground-truth observations；MATH 中 = code interpreter；ALFWorld 中 = admissible actions access。论文对 ALFWorld 明确标注了差异，但 MATH 的 code interpreter 同样不是 ScienceWorld 意义上的 \"deterministic computation\"。Discussion §5 将三个环境并列，却未讨论 modality 定义的异质性对结论可迁移性的影响。\n\n**W3 [Should-Fix]** 11/30 task types 选择的 generalizability concern 未充分回应\n- 63% 的 task types 被排除。Appendix A.2 论证了 death rate 相似（17.8% vs 14.9%），但排除的 task types 可能存在不同 failure modes（timeout 而非 death），routing signal 结构可能完全不同。\"death avoidance accounts for X% of routing signal\" 实际只适用于有 routing signal 的 task types。\n\n**W4 [Minor]** Abstract 信息过载（~250词）\n\n**W5 [Minor]** \"Safety critic\" 类比过度延伸——safe RL 的 safety critic 是主动学习的约束机制，本文发现是 always-deterministic 即最优，更像是 \"default to safe modality\" 而非 learned safety critic。\n\n**W6 [Minor]** Bib 中 3 个 orphan entries (toolkengpt-2023, tot-2023, voyager-2023)；tool-learning-survey-2024 的 year 可能是 2025。\n\n---\n\n请逐条回应（[AGREE] / [REBUT]）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "8",
    "text": "## 交叉分享 — Reviewer 2 的完整审稿意见\n\n请逐条回应 Reviewer 2 的 Weaknesses：对每条标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 2 的完整审稿意见：\n\n### Summary\n本文提出 episode-level counterfactual analysis 方法来分解模块化 LLM agent 中的 routing signal，发现在 ScienceWorld 环境中，78.9% 的非 tie routing label 源于 death asymmetry（penalty-independent），DAF 在 P=100 下达到 90.4%。论文进一步展示 trained router 无法超越 always-deterministic baseline（47.1% vs 50.0% episode-level），并通过 MATH 和 ALFWorld 的 cross-environment 分析提供支撑证据。整体是一篇聚焦的 empirical insight paper，分析严谨但范围受限。\n\n### Strengths\n- S1: 双指标设计（penalty-independent 的 78.9% label fraction + penalty-dependent DAF）比前版本显著改善了核心发现的可信度。\n- S2: Router failure 的诊断非常彻底——data scaling（32×）、capacity scaling（0.6B–4B）、per-task-type breakdown、classification head vs. SFT 对比。\n- S3: Penalty sensitivity analysis 和 mechanism boundary（r=0.97 at P=100 vs r=-0.13 at T=0）深化了 insight 的边界条件。\n- S4: Related work 覆盖全面——RouteLLM、Reflexion、tool-learning survey、CRPO 均已纳入。\n- S5: Limitations section 诚实且具体。\n\n### Weaknesses\n\n**W1 [Should-Fix]** \"routing signal vanishes\" 措辞仍然 overstate non-significant result\n- Abstract 和 Conclusion 均写 \"routing signal vanishes without a death penalty\"，但 MATH 结果是 p=0.079（未达 α=0.05），95% CI [0.0, +8.7]。\"vanishes\" 暗示 signal 不存在，但 30:17 的 label distribution 和 +4.3 pp 的 directional trend 说明存在 signal——只是方向反转且未达显著。更准确的措辞应为 \"the deterministic advantage disappears\" 或 \"death-driven routing signal is absent\"。Conclusion 中 \"p=0.079\" 后缺少 \"not reaching α=0.05\" 的 hedge。\n\n**W2 [Should-Fix]** \"Deterministic modality\" 定义跨环境不一致，削弱 cross-environment 比较\n- ScienceWorld 中 deterministic = ground-truth observations；MATH 中 = code interpreter；ALFWorld 中 = admissible actions access。论文对 ALFWorld 明确标注了差异，但 MATH 的 code interpreter 同样不是 ScienceWorld 意义上的 \"deterministic computation\"。Discussion §5 将三个环境并列，却未讨论 modality 定义的异质性对结论可迁移性的影响。\n\n**W3 [Should-Fix]** 11/30 task types 选择的 generalizability concern 未充分回应\n- 63% 的 task types 被排除。Appendix A.2 论证了 death rate 相似（17.8% vs 14.9%），但排除的 task types 可能存在不同 failure modes（timeout 而非 death），routing signal 结构可能完全不同。\"death avoidance accounts for X% of routing signal\" 实际只适用于有 routing signal 的 task types。\n\n**W4 [Minor]** Abstract 信息过载（~250词）\n\n**W5 [Minor]** \"Safety critic\" 类比过度延伸——safe RL 的 safety critic 是主动学习的约束机制，本文发现是 always-deterministic 即最优，更像是 \"default to safe modality\" 而非 learned safety critic。\n\n**W6 [Minor]** Bib 中 3 个 orphan entries (toolkengpt-2023, tot-2023, voyager-2023)；tool-learning-survey-2024 的 year 可能是 2025。\n\n---\n\n请逐条回应（[AGREE] / [REBUT]）。"
  }
}
```

</details>

---


### Tool result

_source line 629 · 2026-05-16T12:30:20.209861+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 25616
}
```

</details>

---


### Tool call

_source line 630 · 2026-05-16T12:30:20.312252+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "8",
  "text": "## 交叉分享 — Reviewer 1 的完整审稿意见\n\n请逐条回应 Reviewer 1 的 Weaknesses：对每条标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 1 的完整审稿意见：\n\n### Summary\n本文提出 episode-level counterfactual analysis 方法，分析模块化 LLM agent 中路由信号的来源。在 ScienceWorld 的 11/30 任务类型（245 episodes）上，发现 78.9% 的非平局路由标签源自 death asymmetry（penalty-independent），DAF 在 P=100 时达 90.4%。论文训练了一个探索性 step-level router，发现其在 held-out episodes 上低于 always-deterministic baseline，并通过 data/capacity scaling 确认这是结构性限制。跨环境对比（MATH/ALFWorld）提供方向性支持证据。\n\n### Strengths\n- S1: 方法论贡献清晰——episode-level counterfactual analysis 在 sparse-reward 环境中解决了 step-level oracle 退化问题。\n- S2: 透明度极高——DAF penalty-dependence、r=0.97 structural coupling、11/30 scope 均主动披露。\n- S3: 78.9% 作为 penalty-independent companion metric 与 DAF 并列呈现。\n- S4: Robustness diagnostics 丰富——LOO、bootstrap CI、Spearman ρ=0.986、anti-cherry-picking paragraph。\n- S5: Labeling quality audit 排除了 oracle circularity。\n- S6: Router failure 的诚实报告比隐藏负面结果更有科学价值。\n\n### Weaknesses\n\n**W1 [Should-Fix]** Data scaling ablation 的 minority-class confound\n- Augmentation 使用 \"synonym substitution + template variation\"，只增加 surface diversity 不增加 episode diversity。Majority class 比例从 89.6%（100%）上升到 97.7%（800%），internal-preferred episodes 始终只有 ~8-9 个 episode 的变体。25% unaugmented scale 已 collapse 的事实有力，但论文应区分 \"step-level data scarcity\" 和 \"episode-level minority-class scarcity\"——后者是真正瓶颈，32× scaling 没有解决它。\n- 建议：\"rules out data scarcity\" 应软化为 \"consistent with structural limitation, though cannot definitively rule out that more diverse minority-class episodes would help\"。\n\n**W2 [Should-Fix]** Capacity scaling 范围偏窄（0.6B-4B）\n- 三个点均为小模型。更关键的是：论文未在 episode-level 上报告 capacity scaling 结果——只有 step-level 数据。如果 episode-level 在所有 capacity 下都是 ~47-50%，这才是真正排除 capacity 限制的证据。\n\n**W3 [Minor]** Reasoning depth ablation 的 sample size 未报告\n- \"6 task types\"，Mann-Whitney p>0.26，|d|≤0.31，但未报告 episode 数量。\n\n**W4 [Minor]** Cross-environment evidence 的 claim 精度\n- Conclusion 中 \"routing signal vanishes\" 措辞略超出 p=0.079 所支持的结论。\n\n**W5 [Minor]** r=0.97 的 structural coupling 已被承认但需更显式量化\n- 由于 Δ_full ≈ δ·P + Δ_nd 且 Δ_nd 各 task 近似常数，r=0.97 在数学上几乎必然。它证明的是 Δ_nd 的近似均匀性，而非 death 的\"预测力\"。应加一句明确指出这一数学必然性。\n\n---\n\n### Overall Assessment\n**3.5/5** — Borderline to Weak Accept (Findings track)\n**Confidence**: 4/5\n\n---\n\n请逐条回应（[AGREE] / [REBUT]）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "8",
    "text": "## 交叉分享 — Reviewer 1 的完整审稿意见\n\n请逐条回应 Reviewer 1 的 Weaknesses：对每条标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 1 的完整审稿意见：\n\n### Summary\n本文提出 episode-level counterfactual analysis 方法，分析模块化 LLM agent 中路由信号的来源。在 ScienceWorld 的 11/30 任务类型（245 episodes）上，发现 78.9% 的非平局路由标签源自 death asymmetry（penalty-independent），DAF 在 P=100 时达 90.4%。论文训练了一个探索性 step-level router，发现其在 held-out episodes 上低于 always-deterministic baseline，并通过 data/capacity scaling 确认这是结构性限制。跨环境对比（MATH/ALFWorld）提供方向性支持证据。\n\n### Strengths\n- S1: 方法论贡献清晰——episode-level counterfactual analysis 在 sparse-reward 环境中解决了 step-level oracle 退化问题。\n- S2: 透明度极高——DAF penalty-dependence、r=0.97 structural coupling、11/30 scope 均主动披露。\n- S3: 78.9% 作为 penalty-independent companion metric 与 DAF 并列呈现。\n- S4: Robustness diagnostics 丰富——LOO、bootstrap CI、Spearman ρ=0.986、anti-cherry-picking paragraph。\n- S5: Labeling quality audit 排除了 oracle circularity。\n- S6: Router failure 的诚实报告比隐藏负面结果更有科学价值。\n\n### Weaknesses\n\n**W1 [Should-Fix]** Data scaling ablation 的 minority-class confound\n- Augmentation 使用 \"synonym substitution + template variation\"，只增加 surface diversity 不增加 episode diversity。Majority class 比例从 89.6%（100%）上升到 97.7%（800%），internal-preferred episodes 始终只有 ~8-9 个 episode 的变体。25% unaugmented scale 已 collapse 的事实有力，但论文应区分 \"step-level data scarcity\" 和 \"episode-level minority-class scarcity\"——后者是真正瓶颈，32× scaling 没有解决它。\n- 建议：\"rules out data scarcity\" 应软化为 \"consistent with structural limitation, though cannot definitively rule out that more diverse minority-class episodes would help\"。\n\n**W2 [Should-Fix]** Capacity scaling 范围偏窄（0.6B-4B）\n- 三个点均为小模型。更关键的是：论文未在 episode-level 上报告 capacity scaling 结果——只有 step-level 数据。如果 episode-level 在所有 capacity 下都是 ~47-50%，这才是真正排除 capacity 限制的证据。\n\n**W3 [Minor]** Reasoning depth ablation 的 sample size 未报告\n- \"6 task types\"，Mann-Whitney p>0.26，|d|≤0.31，但未报告 episode 数量。\n\n**W4 [Minor]** Cross-environment evidence 的 claim 精度\n- Conclusion 中 \"routing signal vanishes\" 措辞略超出 p=0.079 所支持的结论。\n\n**W5 [Minor]** r=0.97 的 structural coupling 已被承认但需更显式量化\n- 由于 Δ_full ≈ δ·P + Δ_nd 且 Δ_nd 各 task 近似常数，r=0.97 在数学上几乎必然。它证明的是 Δ_nd 的近似均匀性，而非 death 的\"预测力\"。应加一句明确指出这一数学必然性。\n\n---\n\n### Overall Assessment\n**3.5/5** — Borderline to Weak Accept (Findings track)\n**Confidence**: 4/5\n\n---\n\n请逐条回应（[AGREE] / [REBUT]）。"
  }
}
```

</details>

---


### Tool result

_source line 631 · 2026-05-16T12:30:21.671125+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1358
}
```

</details>

---


### Assistant

_source line 632 · 2026-05-16T12:30:25.131354+00:00_

交叉分享已发送。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 59

## Round 59

2 recorded events


### User

_source line 633 · 2026-05-16T12:30:27.635744+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**本轮核心结论**：Overall 3.0/5（Findings acceptance），Confidence 4/5。

上轮 9 个 issues 中 8 个 RESOLVED，1 个 PARTIALLY FIXED（R7-W1 "vanishes" 措辞）。本轮新发现 3 个 Should-Fix（"vanishes" 仍在、deterministic modality 跨环境定义不一致、11/30 task types generalizability）和 3 个 Minor（Abstract 过长、safety critic 类比过度延伸、orphan bib entries）。论文分析质量扎实，但核心发现的 generalizability 和方法创新性不足以支撑 main conference，建议 Findings track。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 634 · 2026-05-16T12:30:35.052269+00:00_

交叉分享已分发给两位 Reviewer，等待 [AGREE]/[REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 60

## Round 60

2 recorded events


### User

_source line 635 · 2026-05-16T12:31:29.714363+00:00_

[Reviewer 1 审稿意见]:
## 交叉回应 — Reviewer 1 对 Reviewer 2 Weaknesses 的逐条意见

---

**[AGREE] R2-W1: "routing signal vanishes" 措辞 overstate non-significant result**

同意 R2 的判断。这与我 R8 审稿中 W4 的发现一致。具体证据：

- Abstract: "routing signal vanishes without a death penalty...p = 0.079, not reaching α=0.05" — Abstract 确实附加了 hedge，但 "vanishes" 一词本身仍有误导性。
- Conclusion (§6): "on MATH (N=300), routing signal vanishes without death penalty, with a directional trend favoring internal reasoning (+4.3 pp, p = 0.079)" — 此处缺少 "not reaching α=0.05" 的 hedge，更加 problematic。
- 30:17 的 label distribution 和 +4.3pp 的 effect size 说明 signal 存在但方向反转，"vanishes" 暗示 null effect，与数据不符。

建议用 "the deterministic advantage disappears" 或 "death-driven routing signal is absent"，精确描述"特定类型的 signal 消失"而非"所有 signal 消失"。

---

**[REBUT] R2-W2: Deterministic modality 定义跨环境不一致**

R2 的关切有一定道理，但论文的 framework 设计是有意为之，且内部逻辑一致：

1. §3.1 定义 modality set 为 {int, det}，其中 det = "agent receives ground-truth observations from the environment simulator...equivalent to access to a perfect dynamics model"。在 MATH 中，code interpreter 对于数学计算确实是 deterministic 的——给定代码，输出确定无误。与 ScienceWorld 的平行关系是：LLM 仍负责高层决策（action selection / code writing），但 state transition / computation 由外部系统精确执行。

2. 论文的 cross-environment claim 不是 "同一个 router 泛化到 MATH"，而是一个 contrast argument：**有 death penalty → det-preferred dominance；无 death penalty → 优势消失或反转**。这个 contrast 不要求两个环境的 deterministic modality 定义相同——它只要求在每个环境内部，两种 modality 的对比是 fair 的。

3. ALFWorld 的异质性论文已显式标注（Appendix F: "This is an information asymmetry rather than a computation mode switch"），将其定位为 framework versatility 的 demonstration 而非 death-avoidance claim 的直接支持。

不过，建议论文在 Discussion §5 加一个 paragraph 明确讨论 "modality 定义的异质性及其对 cross-environment 推断的限制"——即使逻辑一致，显式讨论会增强说服力。这是 presentation 问题而非 soundness 问题。

---

**[REBUT] R2-W3: 11/30 task types 选择的 generalizability concern**

论文已充分回应了这一关切：

1. **Scope qualifier 贯穿全文**：Title "on ScienceWorld"、Abstract "Among task types exhibiting meaningful routing signal in prescreening (11 of 30)"、Conclusion 同样标注。Claims 从未声称适用于所有 30 个 task types。

2. **排除逻辑合理**：Appendix B 明确解释排除的 19 个 task types 是"both strategies time out on all seed variations"。你无法分析不存在的 routing signal——如果两种策略都在 30 步内 timeout 得到相同结果，counterfactual comparison 在数学上是 undefined 的（Δ_full = 0）。

3. **Anti-cherry-picking**：Appendix B 比较了 included vs excluded 的 death rate（17.8% vs 14.9%），确认选择不偏向 death-prone tasks。

4. **R2 的具体关切**——"排除的 task 可能有不同 failure modes（timeout 而非 death）"——恰恰证明了 scoping 的合理性：论文的 claim 是关于"有 death mechanism 的环境中 routing signal 的结构"，timeout-dominated tasks 属于不同的 failure regime，不在 scope 内。Limitations section 已承认 "increasing the step budget could surface additional signal"。

这属于 acknowledged scope limitation 而非 methodological flaw。

---

**[REBUT] R2-W4: Abstract 信息过载（~250 词）**

不同意这是一个问题：

1. ACL ARR 无明确的 abstract 字数限制（不同于 AAAI 的 150 词等）。
2. 前轮审稿（R6-C1、R6-W1）恰恰要求在 Abstract 中加入 penalty-dependence 范围、structural coupling qualifier 等信息。如果删减这些 qualifier 会重新引入之前的 disclosure 缺陷。
3. 每段信息都服务于 transparency 目的：scope（11/30）、penalty range（50%-98%）、CI、structural coupling qualifier、cross-env p-value with hedge。这些是前轮 review 要求的必要 qualifier。

如果要减少词数，唯一可删的是 Llama pilot 的提及（因为 N=10 的 pilot 在 abstract 中不具统计信息量）——这可以节约 ~20 词。

---

**[AGREE] R2-W5: "Safety critic" 类比过度延伸**

同意 R2 的语义区分。具体分析：

- Discussion §5: "The router functions as a safety critic—predicting which states lead to catastrophic failure under internal reasoning" — 但论文的实际发现是 router **失败了**（47.1% < 50%），且 always-deterministic 即最优。
- Safe RL 中的 safety critic 是一个 **learned** 机制，主动识别危险状态并施加约束。本文的发现更像是：routing 问题在 DAF=90.4% 时 **退化为** trivial safety default（always choose safe modality），根本不需要 learned critic。
- 更准确的类比是 "modality routing reduces to a safety-first default policy"，而非 "the router is a safety critic"。

建议将 Discussion 中的表述从 "The router functions as a safety critic" 修改为 "The routing problem reduces to safety-first modality selection—closer to a conservative default policy than to a learned safety critic in the safe RL sense"。

---

**[AGREE] R2-W6: Orphan bib entries + year 问题**

同意这是一个需要清理的格式问题。Orphan entries（toolkengpt-2023, tot-2023, voyager-2023）应当移除或 cite。Year 不一致应当与 publication venue 的实际年份核对。这些属于 camera-ready 级别的 cleanup，不影响评审决定。

---

### 汇总

| R2 Issue | 我的判断 | 核心理由 |
|----------|----------|----------|
| W1 "vanishes" overstate | AGREE | p=0.079 + 30:17 labels 说明 signal 存在但反转，"vanishes" 不准确 |
| W2 modality 定义不一致 | REBUT | Framework 内部逻辑一致（det = exact external computation），cross-env 是 contrast argument 而非 generalization claim；但建议加显式讨论 |
| W3 11/30 generalizability | REBUT | Scope 已充分标注，excluded tasks 无 routing signal 可分析，不构成 methodological flaw |
| W4 Abstract 过长 | REBUT | 密度必要——前轮 review 要求的 qualifier |
| W5 "safety critic" 过度类比 | AGREE | Actual finding 是 trivial default 而非 learned critic |
| W6 Orphan bib | AGREE | 格式问题，需清理 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 636 · 2026-05-16T12:31:35.563497+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 61

## Round 61

2 recorded events


### User

_source line 637 · 2026-05-16T12:31:38.167374+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。对 Reviewer 2 的 6 条 Weaknesses：3 条 AGREE（W1 措辞过强、W5 类比过度、W6 格式问题），3 条 REBUT（W2 modality 定义实际内部一致、W3 scope 已充分限定、W4 Abstract 密度是前轮 review 要求的结果）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 638 · 2026-05-16T12:31:43.694735+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 62

## Round 62

6 recorded events


### User

_source line 639 · 2026-05-16T12:31:47.573399+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 Weaknesses 的逐条回应

---

**[AGREE] R1-W1: Data scaling ablation 的 minority-class confound**

同意。这是本文 router diagnostic 中最值得补充说明的方法论漏洞。论文的 data scaling（Table 7）使用 "synonym substitution + template variation" 做 augmentation，仅增加 step-level surface diversity，不增加 episode-level diversity。核心问题是：internal-preferred episodes 始终只有 9 个 unique episode（来自 Table 4 的 86:9 label 分布），无论 augment 到多少倍，router 看到的都是同 9 个 episode 的 paraphrase 变体。

论文确实部分预见了这个问题——Appendix A.5 说 "the complete collapse to majority-class prediction (internal recall = 0.0) occurs even at the smallest unaugmented scale (25%, ~90% det)"，试图论证这不是 augmentation artifact。但 R1 的区分是准确的：25% scale 的 collapse 说明的是 "9 个 minority episode 的子集不够"，不是 "episode diversity 不重要"。

建议作者将 "rules out data scarcity" 软化为 "rules out step-level data scarcity; episode-level minority-class diversity remains a potential confound"。这不影响 structural limitation 的核心论点（DAF=90.4% 下 always-deterministic 确实 trivially near-optimal），但提高了 claim 精度。

---

**[AGREE] R1-W2: Capacity scaling 范围偏窄（0.6B–4B），缺 episode-level 报告**

同意，且补充两点：

(1) 0.6B → 1.7B → 4B 三个点均为小模型（<5B），在 LLM routing 文献中，更典型的 scaling 范围是 1B–70B。虽然论文旨在验证 "router capacity 不是瓶颈"，但 4B 仍可能不足以学习 episode-level generalization 所需的 abstract routing features。

(2) 更关键的是 R1 指出的 evaluation granularity 问题：Appendix A.7 只报告了 step-level balanced accuracy（52.8% / 54.1% / 53.5%），而论文的核心发现是 step-level vs episode-level 的 generalization gap（§4.3, Table 3）。如果 0.6B 和 4B 的 episode-level 结果也在 ~47–50% 范围内，这会实质性地加强 "structural limitation" 论点；如果 4B 的 episode-level 有所改善，则 structural limitation claim 需要弱化。缺少这组数据使得 capacity scaling ablation 不完整。

---

**[AGREE] R1-W3: Reasoning depth ablation 的 sample size 未报告**

同意。Method §2.1 报告了 "6 task types"、Mann-Whitney p > 0.26、|d| ≤ 0.31、death rates 41.8% vs 42.5%，但未说明每组的 episode 数量。在 effect size 较小（|d| ≤ 0.31）的情况下，sample size 决定了 power——如果每组只有 ~20 episodes，non-significant result 可能是 underpowered 而非 truly null。修复成本极低（加一个括号），应补充。

---

**[AGREE] R1-W4: "routing signal vanishes" 措辞**

强烈同意。我在自己的审稿中独立提出了相同问题（R2-W1）。补充一个 R1 未明确指出的细节：Conclusion 中 "routing signal vanishes without death penalty, with a directional trend favoring internal reasoning ($+4.3$~pp, $p = 0.079$)" 缺少 "not reaching α=0.05" 的 hedge——而 Abstract 和 Introduction 均有此限定。这造成了 paper 内部的叙事不一致：同一个 p=0.079 result 在不同位置的审慎程度不同。

建议统一修改为 "the deterministic advantage disappears" 或 "death-driven routing signal is absent"，并确保所有出现 p=0.079 的位置都附带 significance caveat。

---

**[AGREE with nuance] R1-W5: r=0.97 的 structural coupling 需更显式量化**

同意 R1 的核心判断——Δ_full ≈ δ·P + Δ_nd 中，当 Δ_nd 跨 task 近似常数（mean non-death gap = -1.19 excluding find-non-living-thing, 见 Appendix A.4）且 P=100 使 death term 远大于 Δ_nd 时，r≈1 是数学必然。

但需指出论文已在多处部分承认了这一点：
- Abstract: "r=0.97, though partly structural as death penalties contribute directly to score differences"
- Appendix A.4: Table 6 展示了 r 随 P 变化（P=10 → r=-0.08, P=25 → r=0.51, P=100 → r=0.97），并明确写道 "this is a mathematical consequence of the decomposition (DAF = δP/(δP + Δ_nd)), not evidence of mechanism robustness"
- Discussion: "death is effectively the only component generating differential routing signal"

所以问题不是 "未承认"，而是 §4.1 主文中首次报告 r=0.97 时没有足够 foreground 这个 structural coupling——读者可能在看到数字时形成过强的 "predictive power" 印象，到 Appendix 才看到 qualification。建议在 §4.1 报告 r=0.97 的位置加一句显式说明其数学近必然性，而非仅在 Abstract 用 "partly structural" 一笔带过。

---

### 总结

5 条 Weakness 中我对 4 条完全同意（W1–W4），对 W5 部分同意（核心判断正确但论文已有部分 acknowledgment）。R1 和 R2 的审查具有高度互补性：R1 聚焦 router diagnostic 的方法论严密性（W1 minority-class confound, W2 capacity scaling granularity），R2 聚焦跨环境叙事一致性（W2 modality definition inconsistency, W3 task selection generalizability）。

两位 Reviewer 独立收敛的共识问题：
1. **"routing signal vanishes" 措辞**（R1-W4 = R2-W1）——Must-Fix 级别
2. **Capacity/data scaling ablation 的局限性**（R1-W1 + R1-W2）——Should-Fix 级别
3. **r=0.97 structural coupling 的 prominence**（R1-W5）——Minor but recommended

整体评分维持 3.0/5 (Findings acceptance), Confidence 4/5。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 640 · 2026-05-16T12:34:10.178246+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "simgate-modular-routing",
  "issues_yaml": "- id: \"R6-C1\"\n  summary: \"DAF penalty-dependence — headline ~90% anchored to P=100, 78.9% not co-equal\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"Fresh reviewers want full range + formula + dual reporting.\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"Resurfaced. Abstract still leads with DAF=90.41%. 78.9% present but not co-equal.\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Both reviewers confirm RESOLVED. 78.9% now appears co-equal with DAF throughout Abstract/Intro/Method/Experiments/Conclusion. Penalty range (50%-98%) explicitly stated in Abstract.\"\n  action_items:\n    - round: 6\n      action: \"Abstract/Intro/§3.3/Conclusion dual reporting + DAF(P) formula in method.tex\"\n      assigned_to: main_agent\n      status: done\n    - round: 7\n      action: \"Promote 78.9% to primary metric in Abstract/Title; relegate DAF to secondary with explicit P-dependence caveat\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"Dual metric design confirmed by both R8 reviewers. 78.9% penalty-independent metric co-equal with DAF throughout paper.\"\n  resolution_round: 8\n\n- id: \"R6-C2\"\n  summary: \"Missing counterfactual-in-RL literature paragraph\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"Paper uses 'counterfactual' in title, must contextualize.\"\n  action_items:\n    - round: 6\n      action: \"Add paragraph + 3 refs (Amitai AAAI'24, Gajcin AAMAS'23, Olson AIJ'21)\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"related_work.tex has 'prospective paired comparison vs post-hoc explanation' paragraph with all 3 citations.\"\n  resolution_round: 6\n\n- id: \"R6-W1\"\n  summary: \"r=0.97 structural coupling not disclosed in Abstract/Contributions\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 8\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"High r partly mathematical due to penalty coupling.\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"Resurfaced. §4.1 has caveat but Abstract still reports r=0.97 without structural coupling qualifier.\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"RESOLVED. Abstract now includes 'though partly structural as death penalties contribute directly to score differences'. R1 suggests §4.1 could foreground the mathematical near-inevitability more explicitly (minor improvement, not a flaw).\"\n  action_items:\n    - round: 6\n      action: \"'near-perfect' → 'strong positive' + structural coupling caveat + redirect to 78.9%\"\n      assigned_to: main_agent\n      status: done\n    - round: 7\n      action: \"Add coupling qualifier in Abstract where r=0.97 is reported, or reduce its prominence\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"Abstract and §4.1 both contain structural coupling qualifiers. Appendix D Table 6 shows r variation with P.\"\n  resolution_round: 8\n\n- id: \"R6-W2\"\n  summary: \"Prescreening 19/30 exclusion — scope qualifier needed in title/abstract/conclusion\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"Want excluded task characteristics + step budget sensitivity.\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"Resurfaced as CRITICAL. Title 'Dominant' needs scope qualifier.\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1 confirms RESOLVED (scope qualifier + anti-cherry-picking paragraph). R2 raises residual generalizability concern but R1 rebuts: excluded tasks have no routing signal to analyze, scope is adequately qualified.\"\n  action_items:\n    - round: 6\n      action: \"Expand Limitations with excluded task characteristics + step budget\"\n      assigned_to: main_agent\n      status: done\n    - round: 7\n      action: \"Add scope qualifier to title/abstract/conclusion; analyze excluded task characteristics\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"Title has 'on ScienceWorld', Abstract has '11 of 30', Appendix B has anti-cherry-picking analysis. Residual generalizability is acknowledged scope limitation, not methodological flaw.\"\n  resolution_round: 8\n\n- id: \"R6-W3\"\n  summary: \"Missing failure mode analysis — death temporal pattern\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [2]\n      note: \"Director降为warning. Data extracted: median step 18/30.\"\n  action_items:\n    - round: 6\n      action: \"Extract death step from episodes.jsonl, add 1 sentence\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"Death temporal data extracted (median step 18/30, peak 14-17). Added to paper.\"\n  resolution_round: 6\n\n- id: \"R6-W4\"\n  summary: \"Deterministic strategy operationalization description insufficient\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"Need what LLM sees in each mode.\"\n  action_items:\n    - round: 6\n      action: \"§3.1 add ground-truth vs self-prediction description\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"method.tex describes ground-truth observation (det) vs self-prediction with compounding errors (internal).\"\n  resolution_round: 6\n\n- id: \"R6-W5\"\n  summary: \"MATH pilot (n=50) needs confidence intervals\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"Consensus.\"\n  action_items:\n    - round: 6\n      action: \"Add binomial 95% CI to MATH numbers\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"Limitations has MATH CIs.\"\n  resolution_round: 6\n\n- id: \"R6-W6\"\n  summary: \"find-non-living-thing bimodal DAF distribution not noted\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"DAF=0% vs others >85% heterogeneity.\"\n  action_items:\n    - round: 6\n      action: \"Add 1 sentence on bimodal distribution\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"experiments.tex notes bimodal DAF: find-non-living-thing ≈0% vs others >85%.\"\n  resolution_round: 6\n\n- id: \"R6-W7\"\n  summary: \"Concurrent work discussion too brief\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"tool-overuse-illusion and tool-use-tax need deeper discussion.\"\n  action_items:\n    - round: 6\n      action: \"Expand concurrent work in Related Work\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"Related Work expanded concurrent work discussion.\"\n  resolution_round: 6\n\n- id: \"R6-W8\"\n  summary: \"Safe RL literature coverage insufficient\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 8\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"Need 2024+ safe RL / agent failure refs.\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"Only Garcia 2015 survey cited. Need safety critic works.\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R2 confirms RESOLVED. CRPO (Xu 2021) added to Related Work.\"\n  action_items:\n    - round: 6\n      action: \"Add recent safe RL / agent failure references\"\n      assigned_to: main_agent\n      status: done\n    - round: 7\n      action: \"Add 1-2 specific safety critic references (CPO or equivalent, 2020+)\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"CRPO citation added. Safe RL paragraph now references both Garcia 2015 survey and CRPO 2021.\"\n  resolution_round: 8\n\n- id: \"R7-N1\"\n  summary: \"ALFWorld data (Table 3, N=135) — no methodology description at all\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"Model, deterministic modality definition, labeling process, episode length all missing.\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R2 confirms RESOLVED. Appendix A.9 now includes model, det modality definition, episode count, max steps, success metric.\"\n  action_items:\n    - round: 7\n      action: \"Add full ALFWorld methodology\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"Appendix A.9 contains complete ALFWorld methodology (Qwen2.5-7B, admissible actions, 135 games, 50 steps, binary success).\"\n  resolution_round: 8\n\n- id: \"R7-N2\"\n  summary: \"Router diagnostic conclusion confounded with data insufficiency (Contribution 4)\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"81 train samples (~8 internal-preferred), 14 val samples. Cannot distinguish 'thin signal' from 'insufficient data'.\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Partially fixed. 'exploratory' qualifier added, contribution downgraded. But data scaling ablation uses augmentation that doesn't increase episode diversity — 'rules out data scarcity' overstates. Both reviewers agree R1-W1 (minority-class confound) is residual issue.\"\n  action_items:\n    - round: 7\n      action: \"Acknowledge data-size confound explicitly; downgrade Contribution 4\"\n      assigned_to: main_agent\n      status: done\n    - round: 8\n      action: \"Soften 'rules out data scarcity' to 'rules out step-level data scarcity; episode-level minority-class diversity remains a potential confound' in Appendix E\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W1\"\n  summary: \"MATH p=0.079 asymmetric use — 'vanishes' overstates non-significant result\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"Abstract/Conclusion present label inversion more strongly than §5.\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Both reviewers independently re-raised (R1-W4 + R2-W1). 'vanishes' still in Abstract and Conclusion. Conclusion lacks 'not reaching α=0.05' hedge present elsewhere. Consensus Must-Fix.\"\n  action_items:\n    - round: 7\n      action: \"Consistently mark 'not statistically significant' wherever MATH result appears\"\n      assigned_to: main_agent\n      status: done\n    - round: 8\n      action: \"Replace 'routing signal vanishes' with 'the deterministic advantage disappears' or 'death-driven routing signal is absent' in Abstract and Conclusion; ensure Conclusion has 'not reaching α=0.05' hedge\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W2\"\n  summary: \"Llama pilot (N=10) too small for Contribution 3\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"No statistical power at N=10.\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1 confirms RESOLVED. Contribution list no longer includes cross-model claim. Llama pilot described as 'preliminary directional evidence' only.\"\n  action_items:\n    - round: 7\n      action: \"Remove from Contribution 3 list; retain in text as directional observation only\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"Llama pilot downgraded to directional observation. Not in contribution list.\"\n  resolution_round: 8\n\n- id: \"R7-W3\"\n  summary: \"Pure-strategy labeling vs mixed-strategy deployment gap unanalyzed\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"Death in pure-internal ≠ death in mixed routing. DAgger cite insufficient.\"\n    - round: 8\n      reviewers: [1]\n      note: \"R1 confirms RESOLVED. Limitations discusses distribution shift with DAgger citation.\"\n  action_items:\n    - round: 7\n      action: \"Analyze death timing; discuss mixed-routing implications in Limitations\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"Limitations section discusses pure-strategy vs mixed-routing distribution shift, cites DAgger (2011).\"\n  resolution_round: 8\n\n- id: \"R7-W4\"\n  summary: \"Only ReAct tested — Reflexion/ToT may reduce death rate and change DAF\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"Reflexion self-correction may lower death rate.\"\n    - round: 8\n      reviewers: [1]\n      note: \"R1 confirms RESOLVED. Limitations explicitly mentions Reflexion as potential death rate reducer.\"\n  action_items:\n    - round: 7\n      action: \"Add reasoning strategy generalization discussion to Limitations\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"Limitations discusses single-pass ReAct limitation and names Reflexion as potential reducer of internal death rate.\"\n  resolution_round: 8\n\n- id: \"R7-W5\"\n  summary: \"Missing key references: RouteLLM, Reflexion, tool-learning survey\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"RouteLLM most urgent.\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R2 confirms RESOLVED. All three references now present in Related Work.\"\n  action_items:\n    - round: 7\n      action: \"Add RouteLLM, Reflexion, tool-learning survey to Related Work\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"RouteLLM (Ong 2024), Reflexion (Shinn 2023), tool-learning survey (Qu 2024) all cited in Related Work.\"\n  resolution_round: 8\n\n- id: \"R7-m1\"\n  summary: \"Bib issues: retool-2026 key vs 2025 year; dynathink-2025 author mismatch\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"Both reviewers flagged.\"\n    - round: 8\n      reviewers: [2]\n      note: \"R2 confirms RESOLVED. retool-2025 key/year fixed, dynathink author correct.\"\n  action_items:\n    - round: 7\n      action: \"Fix bib key/year and author fields\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"Bib entries corrected and verified against OpenAlex.\"\n  resolution_round: 8\n\n- id: \"R7-m2\"\n  summary: \"Abstract '90.41%' false precision; Ethics 'RTX 5090' minor anonymity risk\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"90.41% → ~90%. RTX 5090 → 'consumer GPUs'.\"\n    - round: 8\n      reviewers: [2]\n      note: \"R2 confirms RESOLVED. DAF=90.4% with CI; GPU generalized to 'two consumer GPUs'.\"\n  action_items:\n    - round: 7\n      action: \"Round DAF to ~90%; generalize GPU mention\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"90.4% retained with CI brackets; GPU description generalized.\"\n  resolution_round: 8\n\n- id: \"R7-m3\"\n  summary: \"find-non-living-thing 40 episodes (vs 20 for others) unexplained; no code/data release plan\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n    - round: 7\n      reviewers: [1]\n      note: \"Minor but should be addressed for reproducibility.\"\n    - round: 8\n      reviewers: [2]\n      note: \"R2 confirms RESOLVED. Table footnote explains two-batch collection; Ethics Statement has release plan.\"\n  action_items:\n    - round: 7\n      action: \"Explain episode count difference; add code/data availability statement\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"Table 4 footnote explains n=40 (two batches); Ethics Statement confirms code/data release upon acceptance.\"\n  resolution_round: 8\n\n- id: \"R8-W1\"\n  summary: \"'routing signal vanishes' overstates non-significant MATH result (p=0.079)\"\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Both reviewers independently raised. Consensus Must-Fix. 'vanishes' implies null effect but 30:17 labels + 4.3pp trend show signal exists (direction reversed). Conclusion lacks 'not reaching α=0.05' hedge.\"\n  action_items:\n    - round: 8\n      action: \"Replace 'routing signal vanishes' with 'the deterministic advantage disappears' or 'death-driven routing signal is absent' in Abstract/Conclusion; add significance hedge in Conclusion\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W2\"\n  summary: \"Data scaling ablation minority-class confound — augmentation doesn't increase episode diversity\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Both reviewers agree. 32× augmentation only adds surface diversity to same 9 internal-preferred episodes. 'rules out data scarcity' overstates — should distinguish step-level vs episode-level scarcity.\"\n  action_items:\n    - round: 8\n      action: \"Soften 'rules out data scarcity' to 'rules out step-level data scarcity; episode-level minority-class diversity remains a potential confound' in Appendix E text\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W3\"\n  summary: \"Capacity scaling ablation lacks episode-level evaluation (only step-level reported)\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Both reviewers agree. 0.6B/1.7B/4B results only at step-level (52.8%/54.1%/53.5%). Episode-level results needed to strengthen 'structural limitation' claim. Range also narrow (all <5B).\"\n  action_items:\n    - round: 8\n      action: \"Add episode-level capacity scaling results; or explicitly state ablation is step-level only and note limited range\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W4\"\n  summary: \"'Safety critic' analogy overstretched — finding is trivial default, not learned mechanism\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Both agree. Router failed (47.1% < 50%), always-det is optimal. This is 'default to safe modality' not 'learned safety critic'. Analogy misleads about nature of finding.\"\n  action_items:\n    - round: 8\n      action: \"Revise Discussion: 'router functions as safety critic' → 'routing problem reduces to safety-first modality selection — closer to conservative default than learned safety critic'\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W5\"\n  summary: \"Deterministic modality definition varies across environments without explicit discussion\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [2]\n      note: \"R2 raised as Should-Fix. R1 rebuts: framework internally consistent (det = exact external computation), cross-env is contrast argument. But R1 agrees a paragraph discussing modality heterogeneity would improve presentation.\"\n  action_items:\n    - round: 8\n      action: \"Add 1 paragraph in Discussion acknowledging modality definition heterogeneity across environments and its implications for cross-environment inference\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W6\"\n  summary: \"Reasoning depth ablation sample size unreported\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Both agree. 6 task types, Mann-Whitney p>0.26, |d|≤0.31 reported but no episode count. Low fix cost (add n in parentheses).\"\n  action_items:\n    - round: 8\n      action: \"Report total episode count per condition for reasoning depth ablation\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W7\"\n  summary: \"r=0.97 mathematical near-inevitability not foregrounded in §4.1\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1 raised, R2 agrees with nuance (paper already partially acknowledges in Abstract + Appendix D). Issue is prominence: §4.1 first mention lacks explicit statement of mathematical necessity. Readers may overinterpret r=0.97 as independent evidence.\"\n  action_items:\n    - round: 8\n      action: \"Add explicit sentence in §4.1 noting that r≈1 follows mathematically from Δ_nd near-uniformity across tasks when P is large\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-m1\"\n  summary: \"3 orphan bib entries (toolkengpt-2023, tot-2023, voyager-2023); tool-learning-survey year may be 2025 not 2024\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R2 flagged, R1 agreed. Camera-ready cleanup level.\"\n  action_items:\n    - round: 8\n      action: \"Remove orphan bib entries or cite them; verify tool-learning-survey publication year\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "simgate-modular-routing",
    "issues_yaml": "- id: \"R6-C1\"\n  summary: \"DAF penalty-dependence — headline ~90% anchored to P=100, 78.9% not co-equal\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"Fresh reviewers want full range + formula + dual reporting.\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"Resurfaced. Abstract still leads with DAF=90.41%. 78.9% present but not co-equal.\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Both reviewers confirm RESOLVED. 78.9% now appears co-equal with DAF throughout Abstract/Intro/Method/Experiments/Conclusion. Penalty range (50%-98%) explicitly stated in Abstract.\"\n  action_items:\n    - round: 6\n      action: \"Abstract/Intro/§3.3/Conclusion dual reporting + DAF(P) formula in method.tex\"\n      assigned_to: main_agent\n      status: done\n    - round: 7\n      action: \"Promote 78.9% to primary metric in Abstract/Title; relegate DAF to secondary with explicit P-dependence caveat\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"Dual metric design confirmed by both R8 reviewers. 78.9% penalty-independent metric co-equal with DAF throughout paper.\"\n  resolution_round: 8\n\n- id: \"R6-C2\"\n  summary: \"Missing counterfactual-in-RL literature paragraph\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"Paper uses 'counterfactual' in title, must contextualize.\"\n  action_items:\n    - round: 6\n      action: \"Add paragraph + 3 refs (Amitai AAAI'24, Gajcin AAMAS'23, Olson AIJ'21)\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"related_work.tex has 'prospective paired comparison vs post-hoc explanation' paragraph with all 3 citations.\"\n  resolution_round: 6\n\n- id: \"R6-W1\"\n  summary: \"r=0.97 structural coupling not disclosed in Abstract/Contributions\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 8\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"High r partly mathematical due to penalty coupling.\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"Resurfaced. §4.1 has caveat but Abstract still reports r=0.97 without structural coupling qualifier.\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"RESOLVED. Abstract now includes 'though partly structural as death penalties contribute directly to score differences'. R1 suggests §4.1 could foreground the mathematical near-inevitability more explicitly (minor improvement, not a flaw).\"\n  action_items:\n    - round: 6\n      action: \"'near-perfect' → 'strong positive' + structural coupling caveat + redirect to 78.9%\"\n      assigned_to: main_agent\n      status: done\n    - round: 7\n      action: \"Add coupling qualifier in Abstract where r=0.97 is reported, or reduce its prominence\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"Abstract and §4.1 both contain structural coupling qualifiers. Appendix D Table 6 shows r variation with P.\"\n  resolution_round: 8\n\n- id: \"R6-W2\"\n  summary: \"Prescreening 19/30 exclusion — scope qualifier needed in title/abstract/conclusion\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"Want excluded task characteristics + step budget sensitivity.\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"Resurfaced as CRITICAL. Title 'Dominant' needs scope qualifier.\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1 confirms RESOLVED (scope qualifier + anti-cherry-picking paragraph). R2 raises residual generalizability concern but R1 rebuts: excluded tasks have no routing signal to analyze, scope is adequately qualified.\"\n  action_items:\n    - round: 6\n      action: \"Expand Limitations with excluded task characteristics + step budget\"\n      assigned_to: main_agent\n      status: done\n    - round: 7\n      action: \"Add scope qualifier to title/abstract/conclusion; analyze excluded task characteristics\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"Title has 'on ScienceWorld', Abstract has '11 of 30', Appendix B has anti-cherry-picking analysis. Residual generalizability is acknowledged scope limitation, not methodological flaw.\"\n  resolution_round: 8\n\n- id: \"R6-W3\"\n  summary: \"Missing failure mode analysis — death temporal pattern\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [2]\n      note: \"Director降为warning. Data extracted: median step 18/30.\"\n  action_items:\n    - round: 6\n      action: \"Extract death step from episodes.jsonl, add 1 sentence\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"Death temporal data extracted (median step 18/30, peak 14-17). Added to paper.\"\n  resolution_round: 6\n\n- id: \"R6-W4\"\n  summary: \"Deterministic strategy operationalization description insufficient\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"Need what LLM sees in each mode.\"\n  action_items:\n    - round: 6\n      action: \"§3.1 add ground-truth vs self-prediction description\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"method.tex describes ground-truth observation (det) vs self-prediction with compounding errors (internal).\"\n  resolution_round: 6\n\n- id: \"R6-W5\"\n  summary: \"MATH pilot (n=50) needs confidence intervals\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"Consensus.\"\n  action_items:\n    - round: 6\n      action: \"Add binomial 95% CI to MATH numbers\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"Limitations has MATH CIs.\"\n  resolution_round: 6\n\n- id: \"R6-W6\"\n  summary: \"find-non-living-thing bimodal DAF distribution not noted\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"DAF=0% vs others >85% heterogeneity.\"\n  action_items:\n    - round: 6\n      action: \"Add 1 sentence on bimodal distribution\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"experiments.tex notes bimodal DAF: find-non-living-thing ≈0% vs others >85%.\"\n  resolution_round: 6\n\n- id: \"R6-W7\"\n  summary: \"Concurrent work discussion too brief\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"tool-overuse-illusion and tool-use-tax need deeper discussion.\"\n  action_items:\n    - round: 6\n      action: \"Expand concurrent work in Related Work\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"Related Work expanded concurrent work discussion.\"\n  resolution_round: 6\n\n- id: \"R6-W8\"\n  summary: \"Safe RL literature coverage insufficient\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 8\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"Need 2024+ safe RL / agent failure refs.\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"Only Garcia 2015 survey cited. Need safety critic works.\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R2 confirms RESOLVED. CRPO (Xu 2021) added to Related Work.\"\n  action_items:\n    - round: 6\n      action: \"Add recent safe RL / agent failure references\"\n      assigned_to: main_agent\n      status: done\n    - round: 7\n      action: \"Add 1-2 specific safety critic references (CPO or equivalent, 2020+)\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"CRPO citation added. Safe RL paragraph now references both Garcia 2015 survey and CRPO 2021.\"\n  resolution_round: 8\n\n- id: \"R7-N1\"\n  summary: \"ALFWorld data (Table 3, N=135) — no methodology description at all\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"Model, deterministic modality definition, labeling process, episode length all missing.\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R2 confirms RESOLVED. Appendix A.9 now includes model, det modality definition, episode count, max steps, success metric.\"\n  action_items:\n    - round: 7\n      action: \"Add full ALFWorld methodology\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"Appendix A.9 contains complete ALFWorld methodology (Qwen2.5-7B, admissible actions, 135 games, 50 steps, binary success).\"\n  resolution_round: 8\n\n- id: \"R7-N2\"\n  summary: \"Router diagnostic conclusion confounded with data insufficiency (Contribution 4)\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"81 train samples (~8 internal-preferred), 14 val samples. Cannot distinguish 'thin signal' from 'insufficient data'.\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Partially fixed. 'exploratory' qualifier added, contribution downgraded. But data scaling ablation uses augmentation that doesn't increase episode diversity — 'rules out data scarcity' overstates. Both reviewers agree R1-W1 (minority-class confound) is residual issue.\"\n  action_items:\n    - round: 7\n      action: \"Acknowledge data-size confound explicitly; downgrade Contribution 4\"\n      assigned_to: main_agent\n      status: done\n    - round: 8\n      action: \"Soften 'rules out data scarcity' to 'rules out step-level data scarcity; episode-level minority-class diversity remains a potential confound' in Appendix E\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W1\"\n  summary: \"MATH p=0.079 asymmetric use — 'vanishes' overstates non-significant result\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"Abstract/Conclusion present label inversion more strongly than §5.\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Both reviewers independently re-raised (R1-W4 + R2-W1). 'vanishes' still in Abstract and Conclusion. Conclusion lacks 'not reaching α=0.05' hedge present elsewhere. Consensus Must-Fix.\"\n  action_items:\n    - round: 7\n      action: \"Consistently mark 'not statistically significant' wherever MATH result appears\"\n      assigned_to: main_agent\n      status: done\n    - round: 8\n      action: \"Replace 'routing signal vanishes' with 'the deterministic advantage disappears' or 'death-driven routing signal is absent' in Abstract and Conclusion; ensure Conclusion has 'not reaching α=0.05' hedge\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R7-W2\"\n  summary: \"Llama pilot (N=10) too small for Contribution 3\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"No statistical power at N=10.\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1 confirms RESOLVED. Contribution list no longer includes cross-model claim. Llama pilot described as 'preliminary directional evidence' only.\"\n  action_items:\n    - round: 7\n      action: \"Remove from Contribution 3 list; retain in text as directional observation only\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"Llama pilot downgraded to directional observation. Not in contribution list.\"\n  resolution_round: 8\n\n- id: \"R7-W3\"\n  summary: \"Pure-strategy labeling vs mixed-strategy deployment gap unanalyzed\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"Death in pure-internal ≠ death in mixed routing. DAgger cite insufficient.\"\n    - round: 8\n      reviewers: [1]\n      note: \"R1 confirms RESOLVED. Limitations discusses distribution shift with DAgger citation.\"\n  action_items:\n    - round: 7\n      action: \"Analyze death timing; discuss mixed-routing implications in Limitations\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"Limitations section discusses pure-strategy vs mixed-routing distribution shift, cites DAgger (2011).\"\n  resolution_round: 8\n\n- id: \"R7-W4\"\n  summary: \"Only ReAct tested — Reflexion/ToT may reduce death rate and change DAF\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"Reflexion self-correction may lower death rate.\"\n    - round: 8\n      reviewers: [1]\n      note: \"R1 confirms RESOLVED. Limitations explicitly mentions Reflexion as potential death rate reducer.\"\n  action_items:\n    - round: 7\n      action: \"Add reasoning strategy generalization discussion to Limitations\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"Limitations discusses single-pass ReAct limitation and names Reflexion as potential reducer of internal death rate.\"\n  resolution_round: 8\n\n- id: \"R7-W5\"\n  summary: \"Missing key references: RouteLLM, Reflexion, tool-learning survey\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"RouteLLM most urgent.\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R2 confirms RESOLVED. All three references now present in Related Work.\"\n  action_items:\n    - round: 7\n      action: \"Add RouteLLM, Reflexion, tool-learning survey to Related Work\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"RouteLLM (Ong 2024), Reflexion (Shinn 2023), tool-learning survey (Qu 2024) all cited in Related Work.\"\n  resolution_round: 8\n\n- id: \"R7-m1\"\n  summary: \"Bib issues: retool-2026 key vs 2025 year; dynathink-2025 author mismatch\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"Both reviewers flagged.\"\n    - round: 8\n      reviewers: [2]\n      note: \"R2 confirms RESOLVED. retool-2025 key/year fixed, dynathink author correct.\"\n  action_items:\n    - round: 7\n      action: \"Fix bib key/year and author fields\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"Bib entries corrected and verified against OpenAlex.\"\n  resolution_round: 8\n\n- id: \"R7-m2\"\n  summary: \"Abstract '90.41%' false precision; Ethics 'RTX 5090' minor anonymity risk\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"90.41% → ~90%. RTX 5090 → 'consumer GPUs'.\"\n    - round: 8\n      reviewers: [2]\n      note: \"R2 confirms RESOLVED. DAF=90.4% with CI; GPU generalized to 'two consumer GPUs'.\"\n  action_items:\n    - round: 7\n      action: \"Round DAF to ~90%; generalize GPU mention\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"90.4% retained with CI brackets; GPU description generalized.\"\n  resolution_round: 8\n\n- id: \"R7-m3\"\n  summary: \"find-non-living-thing 40 episodes (vs 20 for others) unexplained; no code/data release plan\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n    - round: 7\n      reviewers: [1]\n      note: \"Minor but should be addressed for reproducibility.\"\n    - round: 8\n      reviewers: [2]\n      note: \"R2 confirms RESOLVED. Table footnote explains two-batch collection; Ethics Statement has release plan.\"\n  action_items:\n    - round: 7\n      action: \"Explain episode count difference; add code/data availability statement\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"Table 4 footnote explains n=40 (two batches); Ethics Statement confirms code/data release upon acceptance.\"\n  resolution_round: 8\n\n- id: \"R8-W1\"\n  summary: \"'routing signal vanishes' overstates non-significant MATH result (p=0.079)\"\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Both reviewers independently raised. Consensus Must-Fix. 'vanishes' implies null effect but 30:17 labels + 4.3pp trend show signal exists (direction reversed). Conclusion lacks 'not reaching α=0.05' hedge.\"\n  action_items:\n    - round: 8\n      action: \"Replace 'routing signal vanishes' with 'the deterministic advantage disappears' or 'death-driven routing signal is absent' in Abstract/Conclusion; add significance hedge in Conclusion\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W2\"\n  summary: \"Data scaling ablation minority-class confound — augmentation doesn't increase episode diversity\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Both reviewers agree. 32× augmentation only adds surface diversity to same 9 internal-preferred episodes. 'rules out data scarcity' overstates — should distinguish step-level vs episode-level scarcity.\"\n  action_items:\n    - round: 8\n      action: \"Soften 'rules out data scarcity' to 'rules out step-level data scarcity; episode-level minority-class diversity remains a potential confound' in Appendix E text\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W3\"\n  summary: \"Capacity scaling ablation lacks episode-level evaluation (only step-level reported)\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Both reviewers agree. 0.6B/1.7B/4B results only at step-level (52.8%/54.1%/53.5%). Episode-level results needed to strengthen 'structural limitation' claim. Range also narrow (all <5B).\"\n  action_items:\n    - round: 8\n      action: \"Add episode-level capacity scaling results; or explicitly state ablation is step-level only and note limited range\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W4\"\n  summary: \"'Safety critic' analogy overstretched — finding is trivial default, not learned mechanism\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Both agree. Router failed (47.1% < 50%), always-det is optimal. This is 'default to safe modality' not 'learned safety critic'. Analogy misleads about nature of finding.\"\n  action_items:\n    - round: 8\n      action: \"Revise Discussion: 'router functions as safety critic' → 'routing problem reduces to safety-first modality selection — closer to conservative default than learned safety critic'\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W5\"\n  summary: \"Deterministic modality definition varies across environments without explicit discussion\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [2]\n      note: \"R2 raised as Should-Fix. R1 rebuts: framework internally consistent (det = exact external computation), cross-env is contrast argument. But R1 agrees a paragraph discussing modality heterogeneity would improve presentation.\"\n  action_items:\n    - round: 8\n      action: \"Add 1 paragraph in Discussion acknowledging modality definition heterogeneity across environments and its implications for cross-environment inference\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W6\"\n  summary: \"Reasoning depth ablation sample size unreported\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Both agree. 6 task types, Mann-Whitney p>0.26, |d|≤0.31 reported but no episode count. Low fix cost (add n in parentheses).\"\n  action_items:\n    - round: 8\n      action: \"Report total episode count per condition for reasoning depth ablation\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-W7\"\n  summary: \"r=0.97 mathematical near-inevitability not foregrounded in §4.1\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1 raised, R2 agrees with nuance (paper already partially acknowledges in Abstract + Appendix D). Issue is prominence: §4.1 first mention lacks explicit statement of mathematical necessity. Readers may overinterpret r=0.97 as independent evidence.\"\n  action_items:\n    - round: 8\n      action: \"Add explicit sentence in §4.1 noting that r≈1 follows mathematically from Δ_nd near-uniformity across tasks when P is large\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R8-m1\"\n  summary: \"3 orphan bib entries (toolkengpt-2023, tot-2023, voyager-2023); tool-learning-survey year may be 2025 not 2024\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R2 flagged, R1 agreed. Camera-ready cleanup level.\"\n  action_items:\n    - round: 8\n      action: \"Remove orphan bib entries or cite them; verify tool-learning-survey publication year\"\n      assigned_to: main_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 641 · 2026-05-16T12:34:10.280474+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml\", \"bytes\": 21960}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 642 · 2026-05-16T12:36:18.606351+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告 — Round 8\n\n**论文**: Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\n**Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**Deadline**: 2026-05-25\n**Reviewers**: R1 (方法严谨性 + 实验有效性), R2 (新颖性 + 完整性 + 写作质量)\n\n---\n\n## Summary\n\n本文提出 episode-level counterfactual analysis 方法来分解模块化 LLM agent 中的 routing signal。在 ScienceWorld 的 11/30 任务类型（245 episodes, Qwen2.5-7B-Instruct）上，发现 78.9% 的非平局路由标签源自 death asymmetry（penalty-independent），DAF 在 P=100 时达 90.4%（95% CI [81.6%, 98.8%]）。一个探索性 step-level router 在 held-out episodes 上低于 always-deterministic baseline（47.1% vs 50.0%），data scaling（32×）和 capacity scaling（0.6B-4B）确认结构性限制。MATH 和 ALFWorld 的 cross-environment 分析提供方向性支撑。\n\n## Strengths\n\n1. **双指标设计解决了 R6-C1 的核心关切**：78.9% penalty-independent label fraction 与 DAF 并列贯穿全文，读者可自行评估 penalty 选择的影响。[R1-S3, R2-S1, 共识]\n2. **透明度极高**：DAF penalty-dependence (50%-98%)、r=0.97 structural coupling、11/30 scope 均主动在 Abstract 中披露。前轮要求的所有 qualifier 均已落实。[R1-S2]\n3. **Router failure 诊断彻底**：data scaling、capacity scaling、per-task-type breakdown、classification head vs SFT、cross-split robustness (8 seeds) 构成系统性的 negative-result 证据链。[R1-S6, R2-S2]\n4. **Robustness diagnostics 丰富**：LOO Pearson r [0.963, 0.980]、bootstrap CI、Spearman ρ=0.986、anti-cherry-picking paragraph、penalty sensitivity analysis (Table 5-6) 深化了边界条件。[R1-S4, R2-S3]\n5. **Labeling quality audit** (Appendix A) 排除 oracle circularity——zero labels depend on tie-breaking。[R1-S5]\n6. **Related Work 覆盖全面**——RouteLLM、Reflexion、tool-learning survey、CRPO、6 篇 2025-2026 concurrent work 均已纳入。[R2-S4]\n7. **Limitations 诚实具体**——19 个排除 task types、episode-level label 粗粒度、DAgger distribution shift、ReAct-only、Llama pilot 统计不足均被明确承认。[R2-S5]\n\n## Weaknesses\n\n### Must-Fix（共识）\n\n**W1** [R1-W4 + R2-W1, 共识 AGREE]: **\"routing signal vanishes\" 措辞过度解读 non-significant result**\n- Abstract 和 Conclusion 中 \"routing signal vanishes without a death penalty\" 暗示 null effect，但 MATH 数据显示 30:17 label distribution 和 +4.3pp directional trend——signal 存在但方向反转。p=0.079 未达 α=0.05，Conclusion 中缺少 significance hedge（Abstract/Introduction 中有）。\n- 修复：替换为 \"the deterministic advantage disappears\" 或 \"death-driven routing signal is absent\"；Conclusion 统一添加 \"not reaching α=0.05\"。\n\n### Should-Fix（共识）\n\n**W2** [R1-W1, R2 AGREE]: **Data scaling ablation minority-class confound**\n- 32× augmentation（synonym substitution + template variation）仅增加 step-level surface diversity，internal-preferred episodes 始终只有 9 个 unique episode 的 paraphrase 变体。\"rules out data scarcity\" 混淆了 step-level scarcity 和 episode-level minority-class scarcity。25% unaugmented scale 的 collapse 说明 \"9 个 episode 的子集不够\"，不等于 \"episode diversity 不重要\"。\n- 修复：软化为 \"rules out step-level data scarcity; episode-level minority-class diversity remains a potential confound that cannot be resolved without collecting more internal-preferred episodes—which the 86:9 ground-truth ratio makes structurally impossible in this environment\"。\n\n**W3** [R1-W2, R2 AGREE]: **Capacity scaling ablation缺 episode-level 评估**\n- Appendix G 仅报告 step-level balanced accuracy (52.8%/54.1%/53.5%)。论文核心发现是 step-level vs episode-level 的 generalization gap (§4.3)。episode-level capacity scaling 结果缺失使 \"structural limitation\" 结论在 capacity 维度上不完整。范围也偏窄（0.6B-4B，均 <5B）。\n- 修复：补充 episode-level capacity scaling 数据；或明确声明 ablation 仅为 step-level 并注明局限。\n\n**W4** [R2-W5, R1 AGREE]: **\"Safety critic\" 类比过度延伸**\n- Discussion 称 \"The router functions as a safety critic\"，但论文实际发现是 router 失败（47.1% < 50%）且 always-deterministic 即最优。Safe RL 中 safety critic 是 learned 约束机制；本文发现更像 \"default to safe modality\"——trivial default policy，非 learned critic。\n- 修复：修改为 \"The routing problem reduces to safety-first modality selection—closer to a conservative default policy than to a learned safety critic\"。\n\n### Should-Fix（R2 raised, R1 partial rebut — 建议改为 presentation fix）\n\n**W5** [R2-W2, R1 REBUT with caveat]: **Deterministic modality 跨环境定义不一致未显式讨论**\n- ScienceWorld (ground-truth obs) / MATH (code interpreter) / ALFWorld (admissible actions) 的 det modality 定义不同。R1 rebut: cross-env 是 contrast argument（有 death → det wins; 无 death → advantage gone），不要求同一 modality 定义。但 R1 同意加一段显式讨论会改善 presentation。\n- 修复：Discussion 中加 1 paragraph 明确三环境 modality 定义及其对跨环境推断的限制。\n\n### Minor（共识或单方）\n\n**W6** [R1-W3, R2 AGREE]: Reasoning depth ablation 未报告 episode 数量（n per condition）。修复：加括号注明 n。\n\n**W7** [R1-W5, R2 AGREE with nuance]: r=0.97 数学近必然性在 §4.1 首次出现时 foreground 不够——读者可能误读为独立于 DAF decomposition 的额外证据。Abstract 和 Appendix D 已有 qualification，但 §4.1 应加一句显式说明。\n\n**W8** [R2-W6, R1 AGREE]: 3 个 orphan bib entries (toolkengpt, tot, voyager)；tool-learning-survey year 可能应为 2025。Camera-ready 级别 cleanup。\n\n## Reviewer Consensus\n\n| 问题 | R1 | R2 | 判定 |\n|------|----|----|------|\n| \"vanishes\" overstatement | AGREE | AGREE | **Must-Fix** |\n| Data scaling minority-class confound | Raised | AGREE | Should-Fix |\n| Capacity scaling 缺 episode-level | Raised | AGREE | Should-Fix |\n| Safety critic 类比 | AGREE | Raised | Should-Fix |\n| Modality 定义异质性 | REBUT (presentation) | Raised | Presentation fix |\n| 11/30 generalizability | REBUT (adequately scoped) | Raised | No action (scope acknowledged) |\n| Abstract 过长 | REBUT (prior review required density) | Raised | No action |\n\n## Reviewer Divergence\n\n- **R2-W3 (11/30 scope)**: R2 认为 63% 排除率仍是 generalizability concern；R1 rebut: excluded tasks 无 routing signal (Δ_full=0)，无法分析不存在的东西，scope 已充分限定。Director 判定：R1 论据成立——这是 acknowledged scope limitation，论文已正确处理。\n- **R2-W4 (Abstract 长度)**: R2 认为 ~250 词过载；R1 rebut: 密度是前轮 review 要求 qualifier 的直接结果。Director 判定：R1 论据成立——可选择性删除 Llama pilot mention 以节约 ~20 词，但不构成问题。\n\n## Questions for Authors\n\n1. Data scaling 800% scale 的 internal-preferred episodes 是否仍只是 9 个原始 episode 的 paraphrase？如果是，这对 \"rules out data scarcity\" 结论有什么影响？\n2. Capacity scaling (0.6B-4B) 在 episode-level 的表现如何？是否也 flat at ~47-50%？\n3. 70 of 75 death-asymmetry labels 是 internal-dies-det-survives。是否一个简单的 \"internal death predictor\" 就足够了——routing 可完全简化为单策略 death prediction？\n4. find-non-living-thing 的 non-death routing signal (Δ=+9.58) 来源是什么？是否分析过 post-death-avoidance routing 的可能性？\n5. Reasoning depth ablation 的 n (per condition) 是多少？\n\n## Missing References\n\n核心 references 已覆盖。可选建议（非必须）：\n- FrugalGPT (Chen et al., 2023) / HybridLLM (Ding et al., 2024)——cost-quality routing 先驱\n- CPO (Stooke et al., 2020)——若要加强 safety critic 类比精度\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求（项目配置中未检测到 `external_review.paperreview_ai.enabled: true`）。\n\n## Overall Assessment\n\n**Score: Borderline (3.25/5)**\n- R1: 3.5/5 (Borderline to Weak Accept, Findings track)\n- R2: 3.0/5 (Findings acceptance)\n- Confidence: 4/5 (both reviewers)\n\n**判定**：论文在选定范围内做了扎实的 empirical analysis。核心发现（78.9% death-asymmetry labels, DAF=90.4%）可信且有 insight 价值。Router failure 的诊断彻底、透明度高、前轮 critical issues 已全部修复。\n\n阻碍 main conference acceptance 的主要因素：\n1. 核心发现绑定于 ScienceWorld 的特定 failure structure（-100 death penalty），generalizability 受限\n2. Episode-level counterfactual analysis 方法论本身较为直接（paired comparison），方法创新性不足以单独支撑 main track\n3. Cross-environment validation 的 MATH 结果未达统计显著性 (p=0.079)，且 modality 定义跨环境不一致\n\n**推荐**：**Findings track acceptance**。论文的 insight 清晰度、分析彻底性和自我批判诚实度达到 publishable 水平，适合作为 empirical findings paper。如能修复 Must-Fix（\"vanishes\" 措辞）和 2-3 个 Should-Fix，可进一步加强。\n\n## Detailed Comments\n\n### §Abstract\n- \"routing signal vanishes\" → Must-Fix (W1)\n- 可选删除 Llama pilot mention 以缩短 ~20 词\n\n### §3.3 (DAF Definition)\n- 双指标设计优秀，无修改需求\n\n### §4.1 (Death Avoidance Decomposition)\n- r=0.97 处加一句 mathematical near-inevitability 说明 (W7)\n\n### §4.3 (Router Training as Diagnostic)\n- \"rules out data scarcity\" 需软化 (W2)\n- Capacity scaling 补充 episode-level 或注明局限 (W3)\n\n### §5 (Discussion)\n- \"safety critic\" 类比修改 (W4)\n- 加 modality heterogeneity paragraph (W5)\n\n### §6 (Conclusion)\n- \"routing signal vanishes\" → Must-Fix (W1)\n- 确保 p=0.079 后有 \"not reaching α=0.05\" hedge\n\n### Appendix E (Data Scaling)\n- 区分 step-level vs episode-level data scarcity (W2)\n\n### Appendix G (Capacity Scaling)\n- 补 episode-level 或声明 step-level only (W3)\n\n### §3.1 (Method)\n- 报告 reasoning depth ablation 的 n (W6)\n\n### Bib\n- 删除 orphan entries；核实 tool-learning-survey year (W8)",
  "project": "simgate-modular-routing",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "borderline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告 — Round 8\n\n**论文**: Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\n**Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**Deadline**: 2026-05-25\n**Reviewers**: R1 (方法严谨性 + 实验有效性), R2 (新颖性 + 完整性 + 写作质量)\n\n---\n\n## Summary\n\n本文提出 episode-level counterfactual analysis 方法来分解模块化 LLM agent 中的 routing signal。在 ScienceWorld 的 11/30 任务类型（245 episodes, Qwen2.5-7B-Instruct）上，发现 78.9% 的非平局路由标签源自 death asymmetry（penalty-independent），DAF 在 P=100 时达 90.4%（95% CI [81.6%, 98.8%]）。一个探索性 step-level router 在 held-out episodes 上低于 always-deterministic baseline（47.1% vs 50.0%），data scaling（32×）和 capacity scaling（0.6B-4B）确认结构性限制。MATH 和 ALFWorld 的 cross-environment 分析提供方向性支撑。\n\n## Strengths\n\n1. **双指标设计解决了 R6-C1 的核心关切**：78.9% penalty-independent label fraction 与 DAF 并列贯穿全文，读者可自行评估 penalty 选择的影响。[R1-S3, R2-S1, 共识]\n2. **透明度极高**：DAF penalty-dependence (50%-98%)、r=0.97 structural coupling、11/30 scope 均主动在 Abstract 中披露。前轮要求的所有 qualifier 均已落实。[R1-S2]\n3. **Router failure 诊断彻底**：data scaling、capacity scaling、per-task-type breakdown、classification head vs SFT、cross-split robustness (8 seeds) 构成系统性的 negative-result 证据链。[R1-S6, R2-S2]\n4. **Robustness diagnostics 丰富**：LOO Pearson r [0.963, 0.980]、bootstrap CI、Spearman ρ=0.986、anti-cherry-picking paragraph、penalty sensitivity analysis (Table 5-6) 深化了边界条件。[R1-S4, R2-S3]\n5. **Labeling quality audit** (Appendix A) 排除 oracle circularity——zero labels depend on tie-breaking。[R1-S5]\n6. **Related Work 覆盖全面**——RouteLLM、Reflexion、tool-learning survey、CRPO、6 篇 2025-2026 concurrent work 均已纳入。[R2-S4]\n7. **Limitations 诚实具体**——19 个排除 task types、episode-level label 粗粒度、DAgger distribution shift、ReAct-only、Llama pilot 统计不足均被明确承认。[R2-S5]\n\n## Weaknesses\n\n### Must-Fix（共识）\n\n**W1** [R1-W4 + R2-W1, 共识 AGREE]: **\"routing signal vanishes\" 措辞过度解读 non-significant result**\n- Abstract 和 Conclusion 中 \"routing signal vanishes without a death penalty\" 暗示 null effect，但 MATH 数据显示 30:17 label distribution 和 +4.3pp directional trend——signal 存在但方向反转。p=0.079 未达 α=0.05，Conclusion 中缺少 significance hedge（Abstract/Introduction 中有）。\n- 修复：替换为 \"the deterministic advantage disappears\" 或 \"death-driven routing signal is absent\"；Conclusion 统一添加 \"not reaching α=0.05\"。\n\n### Should-Fix（共识）\n\n**W2** [R1-W1, R2 AGREE]: **Data scaling ablation minority-class confound**\n- 32× augmentation（synonym substitution + template variation）仅增加 step-level surface diversity，internal-preferred episodes 始终只有 9 个 unique episode 的 paraphrase 变体。\"rules out data scarcity\" 混淆了 step-level scarcity 和 episode-level minority-class scarcity。25% unaugmented scale 的 collapse 说明 \"9 个 episode 的子集不够\"，不等于 \"episode diversity 不重要\"。\n- 修复：软化为 \"rules out step-level data scarcity; episode-level minority-class diversity remains a potential confound that cannot be resolved without collecting more internal-preferred episodes—which the 86:9 ground-truth ratio makes structurally impossible in this environment\"。\n\n**W3** [R1-W2, R2 AGREE]: **Capacity scaling ablation缺 episode-level 评估**\n- Appendix G 仅报告 step-level balanced accuracy (52.8%/54.1%/53.5%)。论文核心发现是 step-level vs episode-level 的 generalization gap (§4.3)。episode-level capacity scaling 结果缺失使 \"structural limitation\" 结论在 capacity 维度上不完整。范围也偏窄（0.6B-4B，均 <5B）。\n- 修复：补充 episode-level capacity scaling 数据；或明确声明 ablation 仅为 step-level 并注明局限。\n\n**W4** [R2-W5, R1 AGREE]: **\"Safety critic\" 类比过度延伸**\n- Discussion 称 \"The router functions as a safety critic\"，但论文实际发现是 router 失败（47.1% < 50%）且 always-deterministic 即最优。Safe RL 中 safety critic 是 learned 约束机制；本文发现更像 \"default to safe modality\"——trivial default policy，非 learned critic。\n- 修复：修改为 \"The routing problem reduces to safety-first modality selection—closer to a conservative default policy than to a learned safety critic\"。\n\n### Should-Fix（R2 raised, R1 partial rebut — 建议改为 presentation fix）\n\n**W5** [R2-W2, R1 REBUT with caveat]: **Deterministic modality 跨环境定义不一致未显式讨论**\n- ScienceWorld (ground-truth obs) / MATH (code interpreter) / ALFWorld (admissible actions) 的 det modality 定义不同。R1 rebut: cross-env 是 contrast argument（有 death → det wins; 无 death → advantage gone），不要求同一 modality 定义。但 R1 同意加一段显式讨论会改善 presentation。\n- 修复：Discussion 中加 1 paragraph 明确三环境 modality 定义及其对跨环境推断的限制。\n\n### Minor（共识或单方）\n\n**W6** [R1-W3, R2 AGREE]: Reasoning depth ablation 未报告 episode 数量（n per condition）。修复：加括号注明 n。\n\n**W7** [R1-W5, R2 AGREE with nuance]: r=0.97 数学近必然性在 §4.1 首次出现时 foreground 不够——读者可能误读为独立于 DAF decomposition 的额外证据。Abstract 和 Appendix D 已有 qualification，但 §4.1 应加一句显式说明。\n\n**W8** [R2-W6, R1 AGREE]: 3 个 orphan bib entries (toolkengpt, tot, voyager)；tool-learning-survey year 可能应为 2025。Camera-ready 级别 cleanup。\n\n## Reviewer Consensus\n\n| 问题 | R1 | R2 | 判定 |\n|------|----|----|------|\n| \"vanishes\" overstatement | AGREE | AGREE | **Must-Fix** |\n| Data scaling minority-class confound | Raised | AGREE | Should-Fix |\n| Capacity scaling 缺 episode-level | Raised | AGREE | Should-Fix |\n| Safety critic 类比 | AGREE | Raised | Should-Fix |\n| Modality 定义异质性 | REBUT (presentation) | Raised | Presentation fix |\n| 11/30 generalizability | REBUT (adequately scoped) | Raised | No action (scope acknowledged) |\n| Abstract 过长 | REBUT (prior review required density) | Raised | No action |\n\n## Reviewer Divergence\n\n- **R2-W3 (11/30 scope)**: R2 认为 63% 排除率仍是 generalizability concern；R1 rebut: excluded tasks 无 routing signal (Δ_full=0)，无法分析不存在的东西，scope 已充分限定。Director 判定：R1 论据成立——这是 acknowledged scope limitation，论文已正确处理。\n- **R2-W4 (Abstract 长度)**: R2 认为 ~250 词过载；R1 rebut: 密度是前轮 review 要求 qualifier 的直接结果。Director 判定：R1 论据成立——可选择性删除 Llama pilot mention 以节约 ~20 词，但不构成问题。\n\n## Questions for Authors\n\n1. Data scaling 800% scale 的 internal-preferred episodes 是否仍只是 9 个原始 episode 的 paraphrase？如果是，这对 \"rules out data scarcity\" 结论有什么影响？\n2. Capacity scaling (0.6B-4B) 在 episode-level 的表现如何？是否也 flat at ~47-50%？\n3. 70 of 75 death-asymmetry labels 是 internal-dies-det-survives。是否一个简单的 \"internal death predictor\" 就足够了——routing 可完全简化为单策略 death prediction？\n4. find-non-living-thing 的 non-death routing signal (Δ=+9.58) 来源是什么？是否分析过 post-death-avoidance routing 的可能性？\n5. Reasoning depth ablation 的 n (per condition) 是多少？\n\n## Missing References\n\n核心 references 已覆盖。可选建议（非必须）：\n- FrugalGPT (Chen et al., 2023) / HybridLLM (Ding et al., 2024)——cost-quality routing 先驱\n- CPO (Stooke et al., 2020)——若要加强 safety critic 类比精度\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求（项目配置中未检测到 `external_review.paperreview_ai.enabled: true`）。\n\n## Overall Assessment\n\n**Score: Borderline (3.25/5)**\n- R1: 3.5/5 (Borderline to Weak Accept, Findings track)\n- R2: 3.0/5 (Findings acceptance)\n- Confidence: 4/5 (both reviewers)\n\n**判定**：论文在选定范围内做了扎实的 empirical analysis。核心发现（78.9% death-asymmetry labels, DAF=90.4%）可信且有 insight 价值。Router failure 的诊断彻底、透明度高、前轮 critical issues 已全部修复。\n\n阻碍 main conference acceptance 的主要因素：\n1. 核心发现绑定于 ScienceWorld 的特定 failure structure（-100 death penalty），generalizability 受限\n2. Episode-level counterfactual analysis 方法论本身较为直接（paired comparison），方法创新性不足以单独支撑 main track\n3. Cross-environment validation 的 MATH 结果未达统计显著性 (p=0.079)，且 modality 定义跨环境不一致\n\n**推荐**：**Findings track acceptance**。论文的 insight 清晰度、分析彻底性和自我批判诚实度达到 publishable 水平，适合作为 empirical findings paper。如能修复 Must-Fix（\"vanishes\" 措辞）和 2-3 个 Should-Fix，可进一步加强。\n\n## Detailed Comments\n\n### §Abstract\n- \"routing signal vanishes\" → Must-Fix (W1)\n- 可选删除 Llama pilot mention 以缩短 ~20 词\n\n### §3.3 (DAF Definition)\n- 双指标设计优秀，无修改需求\n\n### §4.1 (Death Avoidance Decomposition)\n- r=0.97 处加一句 mathematical near-inevitability 说明 (W7)\n\n### §4.3 (Router Training as Diagnostic)\n- \"rules out data scarcity\" 需软化 (W2)\n- Capacity scaling 补充 episode-level 或注明局限 (W3)\n\n### §5 (Discussion)\n- \"safety critic\" 类比修改 (W4)\n- 加 modality heterogeneity paragraph (W5)\n\n### §6 (Conclusion)\n- \"routing signal vanishes\" → Must-Fix (W1)\n- 确保 p=0.079 后有 \"not reaching α=0.05\" hedge\n\n### Appendix E (Data Scaling)\n- 区分 step-level vs episode-level data scarcity (W2)\n\n### Appendix G (Capacity Scaling)\n- 补 episode-level 或声明 step-level only (W3)\n\n### §3.1 (Method)\n- 报告 reasoning depth ablation 的 n (W6)\n\n### Bib\n- 删除 orphan entries；核实 tool-learning-survey year (W8)",
    "project": "simgate-modular-routing",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "borderline"
  }
}
```

</details>

---


### Tool result

_source line 643 · 2026-05-16T12:36:22.524458+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_f6bffc7e8351600df8091f08a63cd5a0:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 3918
}
```

</details>

---


### Assistant

_source line 644 · 2026-05-16T12:36:30.199853+00:00_

---

**Round 8 审稿完成。**

汇总：
- **评分**: Borderline (3.25/5)，推荐 **Findings track acceptance**
- **Must-Fix (1)**："routing signal vanishes" 措辞过度解读 p=0.079 的 non-significant result
- **Should-Fix (4)**：data scaling minority-class confound、capacity scaling 缺 episode-level、safety critic 类比过度、modality 定义异质性未讨论
- **Minor (3)**：ablation sample size、r=0.97 prominence、orphan bib entries
- **历史 issue 状态**：14 个历史 issue 中 12 个 RESOLVED，2 个 in_progress（R7-N2 + R7-W1 各留有一个子问题被本轮新 issue 覆盖）

报告已投递至 Research Director。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 63

## Round 63

2 recorded events


### User

_source line 645 · 2026-05-16T12:36:32.716678+00:00_

[Reviewer 2 审稿结果]:
已提交交叉回应。对 R1 的 5 条 Weakness：4 条完全同意（W1–W4），W5 部分同意（论文已有部分 acknowledgment 但 prominence 不够）。两位 Reviewer 独立收敛的共识问题是 "routing signal vanishes" 措辞和 scaling ablation 的方法论局限。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 646 · 2026-05-16T12:36:44.157424+00:00_

Round 8 审稿已完成。审稿报告已投递至 Research Director。

**汇总**：
- R1: 3.5/5 | R2: 3.0/5 → 综合 **Borderline (3.25/5)**
- 推荐 **Findings track acceptance**
- 1 个 Must-Fix（"vanishes" 措辞）、4 个 Should-Fix、4 个 Minor
- 前轮 14 个 issue 中 12 个 RESOLVED，2 个 in_progress（R7-N2 已部分修复，R7-W1 与本轮 W1 合并）
- Issue Tracker 已同步更新（新增 8 条 R8 issue）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 64

## Round 64

2 recorded events


### User

_source line 647 · 2026-05-16T13:12:53.537156+00:00_

[飞书用户 贾骁涵 (ou_ae39b520a3e04736652f6fa0d89e4353)]: 有发现格式问题吗

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "feishu:oc_0b622d6038b969b96148ee8a163a1a0c"
}
```

</details>

---


### Assistant

_source line 648 · 2026-05-16T13:13:09.369690+00:00_

格式问题汇总（Round 8 发现）：

1. **Orphan bib entries**：toolkengpt-2023、tot-2023、voyager-2023 在 .bib 中存在但正文未引用，需删除或 cite。tool-learning-survey-2024 的出版年份可能应为 2025（OpenAlex 记录不一致），需核实。

2. **ACL 模板合规**：`\usepackage[review]{acl}` ✓、Anonymous ✓、Limitations 独立 section ✓、Ethics Statement ✓——无违规。

3. **匿名性**：前轮 "RTX 5090" 已改为 "two consumer GPUs" ✓，本轮未发现新的 de-anonymization 风险。

4. **页数**：正文含 `\input` 共 7 个 section + Limitations + Ethics，未见超 8 页迹象（需编译确认）。

总结：仅有 bib 清理问题（3 orphan entries + 1 year 待核实），属于 camera-ready 级别，不影响评审决定。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 65

## Round 65

46 recorded events


### User

_source line 649 · 2026-05-16T19:02:13.135376+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: simgate-modular-routing
- 论文路径: projects/simgate-modular-routing/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Main Conference Long Paper
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 650 · 2026-05-16T19:02:19.594619+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 651 · 2026-05-16T19:02:19.695851+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 2458 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 652 · 2026-05-16T19:02:24.868658+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
  "max_results": "8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
    "max_results": "8"
  }
}
```

</details>

---


### Tool result

_source line 653 · 2026-05-16T19:02:24.919193+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 654 · 2026-05-16T19:02:29.961703+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "simgate-modular-routing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "simgate-modular-routing"
  }
}
```

</details>

---


### Tool result

_source line 655 · 2026-05-16T19:02:31.801729+00:00_

{"result":"# 项目 simgate-modular-routing 概况\n\n## 实验状态 (92 个)\n\n- **plan-001b-gpu1-extra**: DONE (failed) — \n- **plan-001b-gpu1**: DONE (success) — \n- **plan-001b-gpu0-v2**: DONE (failed) — \n- **plan-011-rule-based**: DONE (success) — \n- **plan-001b-gpu0**: DONE (failed) — \n- **research-prescreening-gpu0**: DONE (killed) — \n- **research-prescreening-gpu1**: DONE (success) — \n- **research-boil-v3-gpu1**: DONE (success) — \n- **mvp-p1-gpu1-v3**: DONE (success) — \n- **mvp-p1-gpu0-vllm**: DONE (success) — \n- **mvp-p1-gpu0**: DONE (killed) — \n- **mvp-p1-gpu1-v2**: DONE (killed) — \n- **mvp-p1-gpu1-vllm**: DONE (killed) — \n- **mvp-p1-gpu1**: DONE (killed) — \n- **mvp-p0-forking**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-16\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **daf-bootstrap-ci-full** (success): Full 245-episode bootstrap (10000 resamples) validates DAF point estimate ≈ 0.90 with tight 95% CI. Per-task DAF provides granular decomposition.\n- **sci-concentration-index** (success): Signal Concentration Index (SCI) quantifies how concentrated routing signal is across task types. Expected SCI ≈ 1.0 (death avoidance dominates, signal highly concentrated in few tasks).\n- **cross-model-guided-router-eval** (negative): Qwen-derived death risk labels transfer to Llama: applying Qwen task-type routing rule on Llama episodes yields balanced_acc > 50%, validating cross-model transferability of the routing signal.\n  [cross-model-guided-router-eval-results](/api/workspace-files/projects/simgate-modular-routing/artifacts/cross-model-guided-router-eval/data/cross_model_results.json)\n\n## 趋势\n成功 38 / 负向 22 / 失败 14 / 共 92\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestb-13313: 无 GPU 信息\n\n## 告警\n- gpu0-v6-lifespan: 已被终止 — unknown\n- llama-cross-model-expanded: 已被终止 — unknown\n- math-200-fixed: 训练失败 — unknown\n- mvp-p1-gpu0: 已被终止 — unknown\n- mvp-p1-gpu1: 已被终止 — unknown\n- mvp-p1-gpu1-v2: 已被终止 — unknown\n- mvp-p1-g
…[truncated 1034 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1840
}
```

</details>

---


### Tool call

_source line 656 · 2026-05-16T19:02:31.802196+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 657 · 2026-05-16T19:02:32.204145+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\graphicspath{{figures/}}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{algorithm}
16	\usepackage{algorithmic}
17	
18	\title{Death Avoidance as the Dominant Routing Signal:\\A Counterfactual Analysis on ScienceWorld}
19	
20	\author{Anonymous}
21	
22	\begin{document}
23	\nolinenumbers
24	\maketitle
25	
26	\input{abstract}
27	\input{introduction}
28	\input{method}
29	\input{experiments}
30	\input{related_work}
31	\input{discussion}
32	\input{conclusion}
33	
34	\section*{Limitations}
35	
36	Our primary analysis uses a single environment (ScienceWorld, 11 of 30 task types) with one backbone (Qwen2.5-7B-Instruct); generalization requires further validation. The $-100$ death penalty amplifies DAF; environments with softer penalties would exhibit lower DAF values (Appendix~\ref{app:penalty}). The 19 excluded task types (63\%) lack routing signal because both strategies typically time out within 30 steps; increasing the step budget could surface additional signal. Our internal-reasoning baseline uses single-pass ReAct~\citep{react-2023}; more sophisticated strategies (e.g., Reflexion~\citep{reflexion-2023} or Tree-of-Thought backtracking~\citep{tot-2023}) may reduce internal death rates and lower DAF. Episode-level labels may assign suboptimal routing to individual steps, particularly those preceding death events, and training on pure-strategy trajectories introduces distribution shift at deployment~\citep{dagger-2011}. Cross-environment analyses on MATH and ALFWorld (\S\ref{sec:discussion}, Appendix~\ref{app:cross-env}) provide supporting evidence but do not conclusively establish generalization. A Llama-3.1-8B-Instruct replication (7 task types, $N{=}70$; Appendix~\ref{app:cross-model}) confirms direction-consisten
…[truncated 26216 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 658 · 2026-05-16T19:02:32.204529+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 659 · 2026-05-16T19:02:32.305157+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 660 · 2026-05-16T19:02:39.632217+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines author"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines author"
  }
}
```

</details>

---


### Tool call

_source line 661 · 2026-05-16T19:02:40.084428+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "simgate-modular-routing",
  "file": "decisions.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "simgate-modular-routing",
    "file": "decisions.yaml"
  }
}
```

</details>

---


### Tool result

_source line 662 · 2026-05-16T19:02:48.790681+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines author"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 on X: \"Here is more precise submission policy. For full details, please check the latest CFP on our website! https://t.co/6dttoXBIT9 https://t.co/ta6IuAjIVm\" / X","url":"https://x.com/emnlpmeeting/status/2047977818928320807"},{"title":"2026 *ACL Conference Dates | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement/view/14"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"}]

Based on the search results, here is comprehensive information about EMNLP 2026 call for papers submission guidelines:

## Paper Types and Focus

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished resear
…[truncated 1887 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "elapsed_ms": 9158
}
```

</details>

---


### Tool result

_source line 663 · 2026-05-16T19:02:48.791722+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/decisions.yaml\", \"content\": \"_next_id: 96\\ndecisions:\\n- id: D001\\n  date: 2026-05-13 04:25 UTC\\n  summary: 'MVP 方案: ScienceWorld 信号检测——验证确定性模拟是否在规则驱动任务上优于 LLM 内部推理'\\n  rationale: 12 天 deadline 下必须快速验证核心假设。ScienceWorld 是 primary track，其 JVM 后端提供精确的规则化状态转移，与\\n    LLM 近似推理的差距应该最大。选 5 task types × 10 episodes 的小规模 counterfactual 比较，不训练 router，纯信号检测。Pass\\n    标准 ≥2/5 task types >5pp，基于 ITP-R vs CogRouter 7.4pp 差距的量级。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-13 04:28 UTC\\n  summary: 采纳 Reviewer 全部 4 条 warning，修订 MVP 为 Phase 0 + Phase 1 两阶段方案\\n  rationale: Reviewer 指出 D001 方案 3 个操作层缺陷：(1) counterfactual 方法未明确——改为 episode-level\\n    3-way (always-internal / always-deterministic / oracle-routing)，oracle 作为 selective\\n    routing 上界；(2) N=10 统计功效不足——增加到 20 episodes/task type + bootstrap 90% CI；(3) kill\\n    criteria 不完整——增加 Phase 0 工程 gate、灰区 conditional pass、pre-register 5 task types\\n    (3S+1M+1W)。无额外 GPU 成本，仅设计层修正。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-13 07:43 UTC\\n  summary: GPU0 继续收集 baseline，GPU1 停下修复 tie-break + 致死动作过滤后重跑\\n  rationale: Fork 诊断发现两个方法论缺陷：(1) tie-break >= 使 95% delta=0 步骤 oracle 永远选 internal，oracle\\n    数据不可信；(2) 致死动作 (score=-100) 污染三条线。修 >= 为 >（oracle 仅在 deterministic 严格更优时介入）+ 致死动作过滤。不做\\n    N-step rollout——1-step 局限性是真实发现，MVP 应如实反映。GPU0 baseline 数据有效，不浪费已有进度。\\n  related_experiments:\\n  - exp_id: mvp-p1-gpu0\\n    role: baseline data, continue\\n  - exp_id: mvp-p1-gpu1-vllm\\n    role: kill, fix, rerun\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-13 08:13 UTC\\n  summary: MVP 判定 primary metric 改为 always-deterministic vs always-internal，oracle\\n    降为 supplementary\\n  rationale: 1-step lookahead 在稀疏 reward 下 95% 步骤 delta=0，任何 tie-break 都使 oracle 退化（>=\\n    → always-internal，> → always-determinist
…[truncated 10983 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 8707
}
```

</details>

---


### Tool call

_source line 664 · 2026-05-16T19:02:54.022401+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 long paper page limit format template double blind ARR submission"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 long paper page limit format template double blind ARR submission"
  }
}
```

</details>

---


### Tool call

_source line 665 · 2026-05-16T19:02:55.225688+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 666 · 2026-05-16T19:02:55.277145+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool result

_source line 667 · 2026-05-16T19:02:59.735438+00:00_

Web search results for query: "EMNLP 2026 long paper page limit format template double blind ARR submission"

Links: [{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"ClimateNLP 2026","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"EMNLP: Empirical Methods in Natural Language Processing 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=883"},{"title":"Submissions | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/about/submissions"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"}]

Based on the search results, here's the information about EMNLP 2026 long paper submissions:

## Page Limit and Format

Long papers have an 8-page limit, and the format is two-column.

## Template

EMNLP 2026 uses the official LaTeX template with ACL style files. EMNLP uses the standard ACL style files, so the LaTeX template is identical to the one used for ACL, NAACL, and other *ACL conferences. The templates are available at github.com/acl-org/acl-style-files.

## Double-Blind Review

The workshop examples in the search results mention submissions will be reviewed in a double-blind peer review process, thus it is important to only submit anonymized papers.

## ARR Subm
…[truncated 479 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "WebSearch",
  "elapsed_ms": 5713
}
```

</details>

---


### Tool call

_source line 668 · 2026-05-16T19:03:04.281952+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "simgate-modular-routing",
  "file": "memory.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "simgate-modular-routing",
    "file": "memory.md"
  }
}
```

</details>

---


### Tool result

_source line 669 · 2026-05-16T19:03:04.733604+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/memory.md\", \"content\": \"# Memory — simgate-modular-routing\\n\\n## 经验教训\\n\\n### 🔴 GPU 进程启动硬性规定 (2026-05-16, Director 强制)\\n1. 任何实验进程启动前必须先注册 RUNNING\\n2. 启动 GPU 进程前必须 `nvidia-smi` 确认目标 GPU 空闲\\n3. 多 GPU 时必须 `CUDA_VISIBLE_DEVICES=X` 隔离，不要只用 `--gpu_id`\\n4. 脚本必须增量保存结果（每个 run 完成即写入），不要攒到最后\\n原因：r7n2 四次事故——3 次 OOM (eval batch 8→4→2)，1 次 SIGHUP 导致 9 个 run 结果全丢，1 次 rescue Worker 差点 OOM GPU0。\\n\\n### ⚠️ Majority-vote baseline: 所有 task types 都是 det-dominant (2026-05-16)\\n11 个 task_type 的 majority label 全部是 \\\"deterministic\\\"（train set 91.4% det）。TT-majority-vote = always-det = 0.5000 balanced_acc。Router cross-split 47.1% 比 always-det 还差 2.9pp——router 在 unseen episodes 上错误预测了多余的 \\\"internal\\\"。\\\"Signal at task-type level\\\" 的准确含义是 \\\"always use det\\\"，与 C1 death avoidance 预测一致。Episode-level split seeds 123/456 的 val set 100% det（无 internal 样本），只有 seed=42 给出有信息量的评估。\\n\\n### ⚠️ Cross-split robustness 失败：Router 不能跨 episode 泛化 (2026-05-16)\\ncross-split-robustness-8seed 结果：episode-level held-out balanced_acc=47.1±2.2%，比 step-level corrected eval (54.1±5.4%) 低 7pp，低于随机 50%。Router 在 step-level split 中 memorize 了 episode 内局部模式（65/66 episodes 跨越 train/val），但不能泛化到完全未见 episode。核心推论：routing signal 在 task-type level 而非 episode level。C1 (death avoidance) 不受影响（基于 counterfactual analysis，不依赖 router）。C2 (router as diagnostic probe) 需 scope 到 task-type level。Narrative A 已被 Director 批准 (D086)。\\n\\n### ⚠️ Seed 42 adapter split 不一致 (2026-05-16)\\n`checkpoints/plan-008-qwen3-1.7b/final_adapter/`（seed 42）使用 **episode-level stratified split**（56 train / 10 val episodes → 1740/300 steps），而 seeds 43-49 使用 `load_implicit_sft_data` 的 **step-level** split（同 episode steps 跨 train/val）。8-seed 汇总（55.7±5.0%）中 seed 42 的 eval 条件与其余 7 个不同。plan-008 训练脚本与 seed-robustness 脚本使用了不同的 split 函数。教训：多 seed 实验必须统一 eval pipeline，不能混用不同实验的 checkpoint。\\n\\n### ⚠️ ga=1 s
…[truncated 2647 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 670 · 2026-05-16T19:03:05.736919+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
    "output_mode": "content"
  }
}
```

</details>

---


### Tool result

_source line 671 · 2026-05-16T19:03:05.891735+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_8.md:102:外部审稿：未请求（项目配置中未检测到 `external_review.paperreview_ai.enabled: true`）。
AGENTS.md:82:如果项目配置了外部审稿（`external_review.paperreview_ai.enabled: true`）：
AGENTS.md:83:- 在分配内部 Reviewer 的同时，调用 `request_external_review()` 向用户群发送协助卡片
AGENTS.md:87:- 如果内部审稿结束时外部结果仍未返回，用 `get_external_review_status()` 检查状态，在报告中标注「外部审稿：未返回」
AGENTS.md:151:`director_get_project_overview`, `director_post_to_reviewer`, `get_external_review_status`, `read_local_file`, `read_project_file`, `request_external_review`, `request_study_approval`, `submit_review_report_to_research_director`, `update_review_issues`
CLAUDE.md:82:如果项目配置了外部审稿（`external_review.paperreview_ai.enabled: true`）：
CLAUDE.md:83:- 在分配内部 Reviewer 的同时，调用 `request_external_review()` 向用户群发送协助卡片
CLAUDE.md:87:- 如果内部审稿结束时外部结果仍未返回，用 `get_external_review_status()` 检查状态，在报告中标注「外部审稿：未返回」
CLAUDE.md:151:`director_get_project_overview`, `director_post_to_reviewer`, `get_external_review_status`, `read_local_file`, `read_project_file`, `request_external_review`, `request_study_approval`, `submit_review_report_to_research_director`, `update_review_issues`
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/logs/chats/archive/feishu_group_oc_f6bffc7e8351600df8091f08a63cd5a0_director_20260516T131900_208238.jsonl:922:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/logs/workers/worker_research_sighup-root-cause_20260514T021418.log:252:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/logs/workers/worker_research_sighup-root-cause_20260514T021418.log:257:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/logs/chats/feishu_group_oc_0b622d6038b969b96148ee8a163a1a0c_director.jsonl:2:[Omitted long matching line]
/home/ubuntu/.agent-ml-rese
…[truncated 17133 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Grep",
  "elapsed_ms": 154
}
```

</details>

---


### Tool call

_source line 672 · 2026-05-16T19:03:13.673656+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 673 · 2026-05-16T19:03:14.830315+00:00_

1	\begin{abstract}
2	Modular LLM agents that route between neural reasoning and deterministic computation promise improved reliability, yet understanding \emph{what} drives the value of routing decisions remains unclear. We introduce a formal diagnostic framework---episode-level counterfactual analysis with the Death Avoidance Factor (DAF) metric---that decomposes routing signal into death-avoidance and non-death components by running complete episodes under pure strategies and comparing final outcomes. The framework is environment-agnostic, requiring only paired episode outcomes under two modalities. Applied to ScienceWorld (11 of 30 task types, 245 episodes, Qwen2.5-7B-Instruct), 78.9\% of non-tie routing labels (75 of 95) are driven by death asymmetry---a penalty-independent metric---and DAF $= 90.4\%$ (95\% CI: $[81.6\%, 98.8\%]$) at default penalty $P{=}100$. Per-task death rate correlates strongly with routing signal ($r{=}0.97$, partly structural; \S\ref{sec:death-decomp}). An exploratory router yields an informative negative: episode-level balanced accuracy remains at or below chance at practical scales (0.6B--1.7B) and reaches only $59.0\%$ at 4B ($p < 0.005$), a disproportionate cost for $+9$\,pp above random---validating the analytical framework over brute-force learned routing. Cross-environment analysis on MATH ($N{=}300$) shows the death-driven routing signal is not statistically detectable without a death penalty ($+4.3$~pp, $p = 0.079$, not reaching $\alpha{=}0.05$). A Llama-3.1-8B-Instruct replication (7 task types, 70 episodes) confirms direction-consistent death patterns for all task types ($+34.3\%$ vs.\ $+26.6\%$ death-rate differential). These findings indicate that in environments with catastrophic failure modes, routing value is dominated by safety---the routing problem reduces to safety-first modality selection rather than efficiency optimization.
3	\end{abstract}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 1156
}
```

</details>

---


### Tool call

_source line 674 · 2026-05-16T19:03:14.932365+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 675 · 2026-05-16T19:03:14.983086+00:00_

1	\section{Introduction}
2	
3	Large language models deployed as interactive agents must repeatedly decide \emph{how} to compute: reason internally, or delegate to an external tool.
4	A Qwen2.5-7B-Instruct agent navigating ScienceWorld \cite{scienceworld-2022}---a text-based science simulation with 30 task types---faces this choice at every step. Tracking temperature thresholds, container states, and multi-step procedures via internal reasoning is error-prone: the model may hallucinate that water has boiled when the stove was never activated, or that an object has been moved when the action was invalid. Deterministic external computation (environment simulators, code interpreters) eliminates such hallucinations via exact state transitions. The practical question for agent design is therefore: \emph{when should an agent route computation externally versus reasoning internally?}
5	
6	Existing routing approaches frame this as a capability or efficiency decision.
7	Toolformer \cite{toolformer-2023} teaches models to insert API calls when doing so reduces perplexity; ART \cite{art-2023} decomposes tasks into tool-augmented programs; Chameleon \cite{chameleon-2023} selects among heterogeneous modules (search, code, vision) per subtask.
8	More recent adaptive-computation methods route to different reasoning depths \cite{cogrouter-2026,ares-2026} or model tiers \cite{mtrouter-2026}.
9	The shared assumption is that routing signal stems from diverse sources---accuracy, latency, capability matching---and that a learned router can exploit this signal to improve over any fixed strategy.
10	But this assumption has never been systematically verified: \emph{what actually drives the value of routing decisions in interactive environments?}
11	
12	We propose a \emph{formal diagnostic framework} for answering this question. The framework comprises (i)~episode-level counterfactual labeling under pure strategies (\S\ref{sec:collection}--\ref{sec:labeling}), and (ii)~the Death Avoidance Fa
…[truncated 5620 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 676 · 2026-05-16T19:03:15.134086+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 677 · 2026-05-16T19:03:15.134728+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Problem Setup}
5	\label{sec:problem-setup}
6	
7	Consider an interactive environment $\mathcal{E}$ with state space $\mathcal{S}$, observation space $\mathcal{O}$, and action space $\mathcal{A}$. An agent follows a policy $\pi: \mathcal{O}^* \rightarrow \mathcal{A}$ that maps observation histories to actions. At each step $t$, the agent receives observation $o_t$, selects action $a_t = \pi(o_1, \ldots, o_t)$, and the environment transitions to state $s_{t+1}$.
8	
9	We define a modality set $\mathcal{M} = \{{\tt int}, {\tt det}\}$ governing how the agent processes state transitions:
10	\begin{itemize}
11	    \item \textbf{Internal} ($m = {\tt int}$): The agent uses its own generation to predict intermediate observations. The LLM interleaves chain-of-thought reasoning with environment actions following the ReAct paradigm \cite{react-2023}, but prediction errors compound across steps.
12	    \item \textbf{Deterministic} ($m = {\tt det}$): The agent receives ground-truth observations from the environment simulator at each step---equivalent to access to a perfect dynamics model. Action selection remains with the LLM; only the state-transition prediction is replaced.
13	\end{itemize}
14	
15	\noindent We restrict $\mathcal{M}$ to two modalities. An ablation comparing chain-of-thought reasoning (deep internal) against direct-answer generation (fast internal) on 6 overlapping task types ($n{=}120$ episodes per condition) found no significant difference on any task (Mann--Whitney $p > 0.26$, $|d| \leq 0.31$) and near-identical death rates (41.8\% vs.\ 42.5\%), confirming that reasoning depth does not meaningfully alter internal-mode outcomes in this setting.
16	
17	A \emph{routing policy} $\rho: \mathcal{O}^* \rightarrow \mathcal{M}$ selects which modality to use at each step. The goal of modality routing is to learn $\rho$ that maximizes expected episode return. Our analysis investigates what signal is available to lear
…[truncated 7658 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 678 · 2026-05-16T19:03:24.629846+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 679 · 2026-05-16T19:03:24.630380+00:00_

1	\section{Experiments}
2	
3	\subsection{Death Avoidance Decomposition}
4	\label{sec:death-decomp}
5	
6	\begin{figure}[t]
7	\centering
8	\includegraphics[width=\columnwidth]{figures/fig1_daf_scatter.pdf}
9	\caption{Per-task scatter: death rate differential (internal $-$ deterministic) vs.\ performance gap ($\Delta_{\text{full}}$). $r = 0.97$, $p < 10^{-6}$, $n = 11$ task types.}
10	\label{fig:decomposition}
11	\end{figure}
12	
13	Across 245 episodes, $\Delta_{\text{full}} = +29.60$; excluding death episodes, $\Delta_{\text{nd}} = +2.84$, yielding DAF $= 90.4\%$ (95\% CI: $[81.6\%, 98.8\%]$; at default $P{=}100$). The penalty-independent death-asymmetry label fraction is 78.9\% (75 of 95 non-tie labels). The internal strategy dies in 42.9\% of episodes versus 16.3\% for deterministic (2.6$\times$). Per-task, death rate differential correlates strongly with $\Delta_{\text{full}}$ ($r = 0.97$, $p < 10^{-6}$; Figure~\ref{fig:decomposition}; robustness diagnostics in Appendix~\ref{app:correlation}). A high correlation is expected whenever the scaled death-rate differential ($P \times \Delta_d$) dominates between-task variance---formally, when $\text{Var}(P \cdot \Delta_d) \gg \text{Var}(\Delta_{\text{nd}})$. At $P{=}100$, this condition holds for all but one task type (\texttt{find-non-living-thing}, which has zero deaths). The sensitivity analysis (Appendix~\ref{app:penalty}) confirms that $r$ drops below significance at $P \leq 25$, where this dominance condition no longer holds. Of 245 episodes, 86 are \texttt{det\_preferred}, 9 \texttt{internal\_preferred}, and 150 \texttt{no\_preference}.
14	
15	One exception: \texttt{find-non-living-thing} ($n{=}40$, zero deaths) has DAF $= 0\%$ with $\Delta = +9.58$ entirely from non-death score differences; all 10 remaining types exceed DAF $> 85\%$. Bootstrap 95\% CIs confirm $\Delta > 0$ for 10 of 11 types; \texttt{chemistry-mix} ($N{=}20$, $\Delta = 21.8$, 95\% CI $[-5.0, 48.6]$) is the sole exception (Appendix~\ref{app:per-ta
…[truncated 3101 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 680 · 2026-05-16T19:03:24.780963+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 681 · 2026-05-16T19:03:24.781381+00:00_

1	\section{Related Work}
2	
3	\paragraph{Tool Use and External Computation in LLMs.}
4	A growing body of work augments language models with external tools \citep{tool-learning-survey-2024}.
5	Toolformer \cite{toolformer-2023} teaches LLMs to insert API calls via self-supervised loss filtering; ToolkenGPT \cite{toolkengpt-2023} represents tools as special tokens enabling frozen models to invoke massive tool libraries; ART \cite{art-2023} decomposes tasks into tool-augmented programs; Chameleon \cite{chameleon-2023} composes heterogeneous modules per subtask; ReTool \cite{retool-2025} applies RL to discover when code execution is preferable to chain-of-thought.
6	These focus on \emph{learning to use tools}; we ask a prior question: \emph{what signal drives the routing decision?}
7	Recent concurrent work sharpens this question: \citet{tool-overuse-illusion-2026} identify a cognitive-illusion effect in LLM tool use, \citet{when2tool-2026} show tool-call decisions are encoded in hidden states before reasoning, \citet{tool-use-tax-2026} quantify a ``tool-use tax'' where tools degrade performance, and \citet{to-call-or-not-2026} propose a necessity--utility--affordability framework.
8	Our counterfactual decomposition provides environment-grounded evidence: in ScienceWorld, $90.4\%$ of routing signal at $P{=}100$ traces to catastrophic-failure prevention.
9	
10	\paragraph{Adaptive Computation and Routing.}
11	CogRouter \cite{cogrouter-2026} adapts reasoning depth per step, ARES \cite{ares-2026} selects among reasoning effort levels, Mixture-of-Recursions \cite{mixture-of-recursions-2025} learns token-level recursion depths, and MTRouter \cite{mtrouter-2026} addresses multi-turn routing across heterogeneous models.
12	RouteLLM \citep{routellm-2024} learns routers from preference data to select between strong and weak models.
13	These optimize \emph{how} to route; we reveal \emph{why} routing helps---in interactive environments, the dominant signal is catastrophic-failure avo
…[truncated 1819 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 682 · 2026-05-16T19:03:24.781577+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 683 · 2026-05-16T19:03:24.932267+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Cross-environment evidence.}
5	Does routing signal persist without catastrophic failure? On MATH Level~4--5 (300 problems), using a code interpreter as the deterministic modality, internal reasoning directionally outperforms: 81.0\% vs.\ 76.7\% accuracy ($+4.3$~pp, 95\% CI $[0.0, +8.7]$; McNemar $p = 0.079$, not reaching $\alpha{=}0.05$). The label distribution inverts: 30 internal-preferred vs.\ 17 deterministic-preferred (cf.\ 9:86 in ScienceWorld), with 84.3\% no-preference. In the absence of death risk, the death-driven routing signal is not statistically detectable---consistent with death avoidance as the primary driver. A complementary evaluation on ALFWorld ($N{=}135$) confirms that the counterfactual framework identifies different routing mechanisms across environments: the deterministic advantage there stems from information asymmetry (access to admissible actions) rather than death avoidance (Appendix~\ref{app:cross-env}).
6	
7	\paragraph{Penalty sensitivity.}
8	The $r = 0.97$ correlation is specific to catastrophic death (score $= -100$); defining ``failure'' as any non-positive score yields $r = -0.13$ ($p = 0.70$). The correlation emerges only at $P \geq 50$ ($r = 0.86$) and reflects that non-death episodes show near-zero performance differential ($\Delta_{\text{nd}} = 2.84$; Appendix~\ref{app:penalty}). Death is effectively the \emph{only} component generating differential routing signal in ScienceWorld. These findings may be capability-dependent: the 42.9\% internal death rate reflects a 7B model's hallucination vulnerability; larger models with lower death rates would reduce DAF, potentially revealing non-death routing signal currently masked by catastrophic failures.
9	
10	\paragraph{Implications for router design.}
11	The dominance of death avoidance (DAF $= 90.4\%$ at $P{=}100$) reframes modality routing as primarily a \emph{safety} problem rather than an efficiency-quality tradeoff. 
…[truncated 2519 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 684 · 2026-05-16T19:03:24.982910+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 685 · 2026-05-16T19:03:25.033501+00:00_

1	\section{Conclusion}
2	
3	We introduced a formal diagnostic framework---episode-level counterfactual analysis with the DAF metric---for decomposing routing signal in modular LLM agents. Applied to 245 ScienceWorld episodes (11 of 30 task types, Qwen2.5-7B-Instruct), 78.9\% of non-tie routing labels (75 of 95) arise from death asymmetry. The DAF reaches $90.4\%$ (95\% CI: $[81.6\%, 98.8\%]$) at $P{=}100$, with strong cross-task correlation ($r = 0.97$, $p < 10^{-6}$).
4	
5	Cross-environment evidence supports this finding: on MATH ($N{=}300$), the death-driven routing signal is not statistically detectable without death penalty ($+4.3$~pp, $p = 0.079$, not reaching $\alpha{=}0.05$). A Llama-3.1-8B-Instruct replication (7 task types, 70 episodes) confirms direction-consistent death patterns for all tasks with a larger differential ($+34.3\%$ vs.\ $+26.6\%$). An exploratory router trained on counterfactual labels achieves only $47.1 \pm 2.2\%$ on held-out episodes---below always-deterministic---a capacity-dependent limitation confirmed by data scaling; the 4B scale yields $59.0\%$ episode-level accuracy but the cost is disproportionate to the routing benefit.
6	
7	In environments with catastrophic failure modes, routing value is dominated by safety: the routing problem reduces to safety-first modality selection rather than efficiency optimization. The framework is environment-agnostic and applicable wherever paired episode outcomes under two modalities can be collected. Open directions include step-level counterfactual labeling, stronger backbones with lower intrinsic death rates (which our framework predicts will lower DAF), and environments with graded failure costs.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 686 · 2026-05-16T19:03:31.066916+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 687 · 2026-05-16T19:03:31.569711+00:00_

1	- id: "R6-C1"
2	  summary: "DAF penalty-dependence — headline ~90% anchored to P=100, 78.9% not co-equal"
3	  category: method
4	  severity: critical
5	  status: resolved
6	  first_raised_round: 4
7	  last_seen_round: 8
8	  mentions:
9	    - round: 6
10	      reviewers: [1, 2]
11	      note: "Fresh reviewers want full range + formula + dual reporting."
12	    - round: 7
13	      reviewers: [1, 2]
14	      note: "Resurfaced. Abstract still leads with DAF=90.41%. 78.9% present but not co-equal."
15	    - round: 8
16	      reviewers: [1, 2]
17	      note: "Both reviewers confirm RESOLVED. 78.9% now appears co-equal with DAF throughout."
18	  action_items:
19	    - round: 6
20	      action: "Abstract/Intro/§3.3/Conclusion dual reporting + DAF(P) formula"
21	      assigned_to: main_agent
22	      status: done
23	    - round: 7
24	      action: "Promote 78.9% to primary metric"
25	      assigned_to: main_agent
26	      status: done
27	  resolution: "Dual metric design confirmed by both R8 reviewers."
28	  resolution_round: 8
29	
30	- id: "R6-C2"
31	  summary: "Missing counterfactual-in-RL literature paragraph"
32	  category: writing
33	  severity: critical
34	  status: resolved
35	  first_raised_round: 6
36	  last_seen_round: 6
37	  mentions:
38	    - round: 6
39	      reviewers: [1, 2]
40	      note: "Paper uses 'counterfactual' in title, must contextualize."
41	  action_items:
42	    - round: 6
43	      action: "Add paragraph + 3 refs"
44	      assigned_to: main_agent
45	      status: done
46	  resolution: "related_work.tex has prospective paired comparison paragraph."
47	  resolution_round: 6
48	
49	- id: "R6-W1"
50	  summary: "r=0.97 structural coupling not disclosed in Abstract/Contributions"
51	  category: writing
52	  severity: warning
53	  status: resolved
54	  first_raised_round: 6
55	  last_seen_round: 8
56	  mentions:
57	    - round: 6
58	      reviewers: [1, 2]
59	      note: "High r partly mathematical due to penalty coupling."
60	    - round: 7
61	      re
…[truncated 18610 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 688 · 2026-05-16T19:03:31.871079+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_reports/round_*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_reports/round_*.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts"
  }
}
```

</details>

---


### Tool result

_source line 689 · 2026-05-16T19:03:31.921775+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_1.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_2.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_3.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_4.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_5.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_6.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_7.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_reports/round_8.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 690 · 2026-05-16T19:04:28.265232+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## Round 9 审稿任务 — Reviewer 1（方法严谨性 + 实验设计）\n\n### Venue 信息\n- **目标**: EMNLP 2026 Main Conference Long Paper (ARR May cycle)\n- **Deadline**: 2026-05-25\n- **格式**: ACL 模板, 8 页正文, 双栏, double-blind\n- **匿名规则**: 必须匿名提交\n\n### 论文路径\n`projects/simgate-modular-routing/docs/paper/main.tex`（含 abstract.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, discussion.tex, conclusion.tex）\n\n### 你的审查侧重\n\n**方法严谨性 + 实验设计**，重点关注：\n\n1. **DAF 指标设计合理性**：\n   - DAF = 1 - Δ_nd / Δ_full 的定义是否在数学上严谨？边界条件/退化情况处理？\n   - DAF 随 P 单调递增是数学必然还是经验发现？论文是否清晰区分？\n   - 78.9% penalty-independent metric 与 DAF 的互补关系是否合理呈现？\n\n2. **统计方法**：\n   - N=245 (11 task types) 样本量是否足以支撑论文声称？\n   - r=0.97 (n=11) — 只有 11 个数据点的相关系数可信度？是否存在结构性耦合未充分说明？\n   - Bootstrap CI 方法是否恰当？\n   - MATH p=0.079 的使用是否前后一致？\n\n3. **Router Diagnostic**：\n   - 47.1% episode-level accuracy 作为 \"negative result\" 的结论是否严谨？\n   - 数据规模 (245 episodes, ~1735 steps) 能否支撑 \"structural limitation\" 的结论？\n   - 4B → 59% 的 capacity scaling 证据强度？\n   - Data scaling (25%-800%) 用 augmentation 的方法论问题？\n\n4. **Cross-environment 实验设计**：\n   - MATH (N=300) 和 ALFWorld (N=135) 作为对比环境是否设计合理？\n   - \"deterministic modality\" 在三个环境中定义不同——这是否削弱可比性？\n   - Llama replication (7 tasks, N=70) 的统计效力？\n\n5. **形式问题**：\n   - Algorithm 1 是否完备无歧义？\n   - 所有 CI 和 p-value 的报告是否规范？\n\n请按以下格式输出审稿意见：\n```\n## Summary (2-3句)\n## Strengths (逐条)\n## Weaknesses (逐条，标注 [Critical] / [Major] / [Minor])\n## Questions (需作者回应)\n## Missing References\n## Overall Assessment (strong reject / weak reject / borderline / weak accept / strong accept) + 置信度 (1-5)\n```",
  "project": "simgate-modular-routing"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## Round 9 审稿任务 — Reviewer 1（方法严谨性 + 实验设计）\n\n### Venue 信息\n- **目标**: EMNLP 2026 Main Conference Long Paper (ARR May cycle)\n- **Deadline**: 2026-05-25\n- **格式**: ACL 模板, 8 页正文, 双栏, double-blind\n- **匿名规则**: 必须匿名提交\n\n### 论文路径\n`projects/simgate-modular-routing/docs/paper/main.tex`（含 abstract.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, discussion.tex, conclusion.tex）\n\n### 你的审查侧重\n\n**方法严谨性 + 实验设计**，重点关注：\n\n1. **DAF 指标设计合理性**：\n   - DAF = 1 - Δ_nd / Δ_full 的定义是否在数学上严谨？边界条件/退化情况处理？\n   - DAF 随 P 单调递增是数学必然还是经验发现？论文是否清晰区分？\n   - 78.9% penalty-independent metric 与 DAF 的互补关系是否合理呈现？\n\n2. **统计方法**：\n   - N=245 (11 task types) 样本量是否足以支撑论文声称？\n   - r=0.97 (n=11) — 只有 11 个数据点的相关系数可信度？是否存在结构性耦合未充分说明？\n   - Bootstrap CI 方法是否恰当？\n   - MATH p=0.079 的使用是否前后一致？\n\n3. **Router Diagnostic**：\n   - 47.1% episode-level accuracy 作为 \"negative result\" 的结论是否严谨？\n   - 数据规模 (245 episodes, ~1735 steps) 能否支撑 \"structural limitation\" 的结论？\n   - 4B → 59% 的 capacity scaling 证据强度？\n   - Data scaling (25%-800%) 用 augmentation 的方法论问题？\n\n4. **Cross-environment 实验设计**：\n   - MATH (N=300) 和 ALFWorld (N=135) 作为对比环境是否设计合理？\n   - \"deterministic modality\" 在三个环境中定义不同——这是否削弱可比性？\n   - Llama replication (7 tasks, N=70) 的统计效力？\n\n5. **形式问题**：\n   - Algorithm 1 是否完备无歧义？\n   - 所有 CI 和 p-value 的报告是否规范？\n\n请按以下格式输出审稿意见：\n```\n## Summary (2-3句)\n## Strengths (逐条)\n## Weaknesses (逐条，标注 [Critical] / [Major] / [Minor])\n## Questions (需作者回应)\n## Missing References\n## Overall Assessment (strong reject / weak reject / borderline / weak accept / strong accept) + 置信度 (1-5)\n```",
    "project": "simgate-modular-routing"
  }
}
````

</details>

---


### Tool result

_source line 691 · 2026-05-16T19:04:44.461920+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 16196
}
```

</details>

---


### Tool call

_source line 692 · 2026-05-16T19:04:44.613122+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## Round 9 审稿任务 — Reviewer 2（新颖性 + 完整性）\n\n### Venue 信息\n- **目标**: EMNLP 2026 Main Conference Long Paper (ARR May cycle)\n- **Deadline**: 2026-05-25\n- **格式**: ACL 模板, 8 页正文, 双栏, double-blind\n- **匿名规则**: 必须匿名提交\n\n### 论文路径\n`projects/simgate-modular-routing/docs/paper/main.tex`（含 abstract.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, discussion.tex, conclusion.tex）\n\n### 你的审查侧重\n\n**新颖性 + 完整性**，重点关注：\n\n1. **贡献新颖性**：\n   - \"episode-level counterfactual analysis + DAF metric\" 作为 diagnostic framework，novelty 是否足够？\n   - \"Death avoidance dominance\" 作为 empirical finding，是否足够 surprising/impactful？还是只是 \"internal reasoning hallucination kills agent\" 这个显然观察的量化？\n   - 与 RouteLLM, CogRouter, ARES, ReTool 等 routing 工作的差异是否清晰？\n   - \"Negative result\" (router fails) 是否有独立贡献价值？\n\n2. **论述逻辑一致性**：\n   - Abstract → Introduction → Method → Experiments → Discussion → Conclusion 的论证链是否完整连贯？\n   - 三个 Contributions 是否都有充分支撑？是否有 over-claim？\n   - \"routing problem reduces to safety-first modality selection\" 这个结论是否过度泛化？（仅基于 ScienceWorld + 部分 cross-env 证据）\n\n3. **Related Work 覆盖**：\n   - Tool-use learning (Toolformer/ART/Chameleon/ReTool)、adaptive computation (CogRouter/ARES/RouteLLM)、counterfactual RL、safe RL、LLM agents 五个方向是否充分覆盖？\n   - 是否遗漏 2025-2026 年重要相关工作？\n   - 论文定位与现有工作的关系是否清晰？\n\n4. **写作质量**：\n   - 术语使用是否一致（modality/strategy/mode/computation type）？\n   - 论文结构是否合理？各 section 比例是否适当？\n   - Figure 和 Table 的信息量和呈现质量？\n   - Limitations 是否充分讨论了核心局限？\n\n5. **EMNLP 2026 匹配度**：\n   - 是否属于 EMNLP 传统收录范围（empirical methods for NLP）？\n   - 论文更偏 NLP/LLM agents 还是偏 RL？audience fit?\n\n请按以下格式输出审稿意见：\n```\n## Summary (2-3句)\n## Strengths (逐条)\n## Weaknesses (逐条，标注 [Critical] / [Major] / [Minor])\n## Questions (需作者回应)\n## Missing References\n## Overall Assessment (strong reject / weak reject / borderline / weak accept / strong accept) + 置信度 (1-5)\n```",
  "project": "simgate-modular-routing"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## Round 9 审稿任务 — Reviewer 2（新颖性 + 完整性）\n\n### Venue 信息\n- **目标**: EMNLP 2026 Main Conference Long Paper (ARR May cycle)\n- **Deadline**: 2026-05-25\n- **格式**: ACL 模板, 8 页正文, 双栏, double-blind\n- **匿名规则**: 必须匿名提交\n\n### 论文路径\n`projects/simgate-modular-routing/docs/paper/main.tex`（含 abstract.tex, introduction.tex, method.tex, experiments.tex, related_work.tex, discussion.tex, conclusion.tex）\n\n### 你的审查侧重\n\n**新颖性 + 完整性**，重点关注：\n\n1. **贡献新颖性**：\n   - \"episode-level counterfactual analysis + DAF metric\" 作为 diagnostic framework，novelty 是否足够？\n   - \"Death avoidance dominance\" 作为 empirical finding，是否足够 surprising/impactful？还是只是 \"internal reasoning hallucination kills agent\" 这个显然观察的量化？\n   - 与 RouteLLM, CogRouter, ARES, ReTool 等 routing 工作的差异是否清晰？\n   - \"Negative result\" (router fails) 是否有独立贡献价值？\n\n2. **论述逻辑一致性**：\n   - Abstract → Introduction → Method → Experiments → Discussion → Conclusion 的论证链是否完整连贯？\n   - 三个 Contributions 是否都有充分支撑？是否有 over-claim？\n   - \"routing problem reduces to safety-first modality selection\" 这个结论是否过度泛化？（仅基于 ScienceWorld + 部分 cross-env 证据）\n\n3. **Related Work 覆盖**：\n   - Tool-use learning (Toolformer/ART/Chameleon/ReTool)、adaptive computation (CogRouter/ARES/RouteLLM)、counterfactual RL、safe RL、LLM agents 五个方向是否充分覆盖？\n   - 是否遗漏 2025-2026 年重要相关工作？\n   - 论文定位与现有工作的关系是否清晰？\n\n4. **写作质量**：\n   - 术语使用是否一致（modality/strategy/mode/computation type）？\n   - 论文结构是否合理？各 section 比例是否适当？\n   - Figure 和 Table 的信息量和呈现质量？\n   - Limitations 是否充分讨论了核心局限？\n\n5. **EMNLP 2026 匹配度**：\n   - 是否属于 EMNLP 传统收录范围（empirical methods for NLP）？\n   - 论文更偏 NLP/LLM agents 还是偏 RL？audience fit?\n\n请按以下格式输出审稿意见：\n```\n## Summary (2-3句)\n## Strengths (逐条)\n## Weaknesses (逐条，标注 [Critical] / [Major] / [Minor])\n## Questions (需作者回应)\n## Missing References\n## Overall Assessment (strong reject / weak reject / borderline / weak accept / strong accept) + 置信度 (1-5)\n```",
    "project": "simgate-modular-routing"
  }
}
````

</details>

---


### Tool result

_source line 693 · 2026-05-16T19:04:45.822524+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1209
}
```

</details>

---


### Assistant

_source line 694 · 2026-05-16T19:04:51.068866+00:00_

两位 Reviewer 已分配任务：
- **Reviewer 1** → 方法严谨性 + 实验设计（DAF 指标、统计方法、router diagnostic、cross-env 设计）
- **Reviewer 2** → 新颖性 + 完整性（贡献定位、论述逻辑、related work、写作质量、venue fit）

等待 Reviewer 返回初审意见，收齐后进入 Step 2（交叉分享）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 66

## Round 66

2 recorded events


### User

_source line 695 · 2026-05-16T19:09:09.962313+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 9 审稿意见（新颖性 + 完整性）

---

## Summary (2-3句)

本文提出 episode-level counterfactual analysis + DAF metric 框架，用于分解模块化 LLM agent 的 routing signal 来源。在 ScienceWorld 上发现 death avoidance 主导 routing signal（DAF=90.4% at P=100），训练的 router 无法超越 always-deterministic baseline。跨环境分析（MATH、ALFWorld）显示无 death penalty 时该信号消失。

---

## Strengths

**S1. 问题定位精准且有价值。** 在 routing 领域大量工作集中于"如何 route"时，本文退后一步问"什么驱动 routing signal"——这是一个被忽视但重要的元问题。Section 1 对此动机的阐述清晰。

**S2. 方法论简洁可复现。** 框架仅需 paired episode outcomes，Algorithm 1 清晰易实现，DAF/SCI 指标定义明确。框架的 environment-agnostic 属性通过在三个结构迥异的环境（ScienceWorld/MATH/ALFWorld）上应用得到初步验证。

**S3. 实验严谨性高。** 多层面 robustness checks 令人印象深刻：bootstrap CI、LOO correlation（Appendix B）、8-seed cross-split evaluation、data scaling ablation（25%-800%）、capacity scaling（0.6B-4B）、cross-model replication（Llama-3.1-8B）、penalty sensitivity analysis。这些大幅加强了核心发现的可信度。

**S4. 对 negative result 的呈现诚实且有建设性。** Router 在 episode-level 低于 chance 的结果被正确解读为 structural limitation 而非简单的 training failure。Data scaling 排除 data scarcity、capacity scaling 定位 capacity bottleneck——这种系统性诊断本身就是贡献。

**S5. Limitations 坦诚且具体。** 明确列出 19/30 task types excluded、penalty amplification effect、single-pass ReAct baseline、distribution shift 问题（citing DAgger）等，未试图掩盖。

**S6. 2026 concurrent work 覆盖充分。** Tool-overuse-illusion、When2Tool、Tool-Use-Tax、To-Call-or-Not 四篇 2026 concurrent work 的引用表明作者充分关注最新进展，定位差异清晰。

---

## Weaknesses

**W1 [Critical] DAF 的 headline number 被 penalty magnitude 机械放大，framing 存在误导。**

- 具体位置：Section 3.4（DAF 定义）、Abstract、Section 4.1
- 问题：DAF = δP/(δP + Δ_nd) 是 P 的单调递增函数（论文自己在 §3.4 第三段承认 "a mathematical consequence, not an empirical finding"）。90.4% 这个数字依赖于 P=100 的选择；在 P=10 时 DAF 仅为 50.4%（Table 9）。然而 Abstract 和 Conclusion 将 "DAF=90.4%" 作为核心卖点反复强调（Abstract 出现 2 次，Conclusion 1 次），给读者"death 占九成"的强印象——但这本质上是说"当 penalty 是 score gap 的 35 倍时，penalty 项主导总 gap"，接近同义反复。
- 论文确实报告了 penalty-independent 指标（78.9% death-asymmetry labels），但这个更稳健的数字在 Abstract 中处于从属位置。
- 为什么影响接收：如果核心 quantitative claim 的 magnitude 主要由 environment parameter 决定而非 empirical discovery，则该 claim 的 informativeness 和 generalizability 大打折扣。Reviewers 会质疑"你发现的是 P 很大，还是 death 很重要？"
- 建议修改方向：将 **78.9% death-asymmetry label fraction**（penalty-independent）提升为 primary metric，DAF 作为 penalty-parametric companion；或明确论证 P=100 是"typical catastrophic penalty magnitude"具有外部效度。

**W2 [Critical] "Routing problem reduces to safety-first modality selection" 过度泛化。**

- 具体位置：Abstract 最后一句、Section 5 第三段、Section 6 第二段
- 问题：这一结论仅基于 ScienceWorld（1 个有 death penalty 的环境，11/30 task types，1 个 7B backbone）。论文自身的 MATH 结果（p=0.079，internal 方向性领先）和 ALFWorld（information asymmetry 而非 death）恰恰说明该结论不成立于无 death penalty 环境。所以这不是一个关于"routing problem"的一般性结论，而是一个关于"有 catastrophic failure mode 的环境中的 routing problem"的条件性结论。
- 论文在 Discussion §5 Framework applicability 段有 qualifier（"applies most directly to environments with two properties..."），但 Abstract 和 Conclusion 的表述丢掉了这些 qualifiers。
- 为什么影响接收：Over-claim 是 *ACL reviewer 最常见的 rejection reason 之一。当 Abstract 的结论与论文自身数据矛盾时（MATH 显示相反方向），这是严重的逻辑一致性问题。
- 建议修改方向：收窄为 "In environments with catastrophic failure modes, routing value is dominated by safety" 并在 Abstract 保持这个 qualifier。或者提供更多支持泛化的证据（如多个有 death penalty 的环境）。

**W3 [Major] "Internal modality" 的定义混淆了 hallucination 与 reasoning。**

- 具体位置：Section 3.1 Problem Setup
- 问题："Internal" 定义为 agent 自己生成中间 observation（即预测 state transition）。但论文的 insight 本质上是：**hallucinated state predictions 导致 death**，而非 "internal reasoning" 本身有害。如果一个 agent 做 internal reasoning 但在每步后 verify observation（如 Reflexion 的 self-correction），death rate 可能大幅下降——论文在 Limitations 中承认这一点。这意味着 "modality routing" 的 framing 可能不是最 informative 的抽象层次；真正的 bottleneck 是 observation accuracy，不是 computation mode。
- 为什么影响接收：如果核心发现可以更精确地表述为 "agents with unverified state predictions die more often"（一个相对 obvious 的 observation），那么 "routing signal" framing 增加的 insight 有多少？
- 建议修改方向：明确讨论 "modality" 与 "observation reliability" 的关系；如果有数据显示 internal mode 中 death 确实由 state hallucination 引起（Appendix F 有定性描述但无量化），量化 hallucination-death causality 会大幅加强论文。

**W4 [Major] Contribution 3（cross-context validation）证据力不足。**

- 具体位置：Section 5 第一段、Section 1 Contribution 3
- 问题：
  - MATH：p=0.079 不显著（论文自己承认），且方向相反（internal > deterministic），实际上 **不支持** death-avoidance dominance 结论——它只证明 "没有 death penalty 时没有 death-driven signal"，这是 tautological。
  - ALFWorld：mechanism 完全不同（information asymmetry），没有 death，label 分布也不支持论文主论点。
  - 两个 cross-env 都没有 death penalty，所以它们不能 validate "death avoidance dominance" 这个 finding——它们只能说 "without death, no death signal"。真正的 validation 需要另一个 **有** catastrophic failure 的环境重现类似 DAF。
- 为什么影响接收：把 "absence of evidence"（无 death→无 death signal）包装为 "cross-context validation" 是 overselling。如果唯一真正支持 main claim 的数据只来自 ScienceWorld，generalizability 是重大担忧。
- 建议修改方向：降低 Contribution 3 的 claim 强度（改为 "framework applicability demonstration" 而非 "validation"），或增加一个有 catastrophic failure 的第二环境（如 NetHack、Crafter 等有 death 的 RL 环境）。

**W5 [Major] 样本量和环境覆盖的统计 power 有限。**

- 具体位置：Abstract（"11 of 30 task types, 245 episodes"）、Appendix A
- 问题：
  - 245 episodes 中仅 95 non-tie（61.2% 是 no-preference），实际 training signal 很少。
  - Internal-preferred 仅 9 episodes（3.7%），使得任何关于 "什么时候 internal 更好" 的结论统计效力极低。
  - 19/30 task types（63%）被排除——论文说是因为 "both strategies time out"，但这意味着大多数 ScienceWorld tasks 实际上对两种 strategy 都不 tractable，削弱了 "ScienceWorld 上 routing signal 分析" 的代表性。
  - Cross-model replication 仅 70 episodes、7 task types，且两个 model 都是 7-8B 范围。
- 为什么影响接收：虽然 bootstrap CI 处理了 point estimate 的 uncertainty，但 environment diversity 和 task coverage 的限制是 CI 无法解决的 external validity 问题。
- 建议修改方向：承认这是 case study 而非 broad empirical law；或增加至少一个有 death penalty 的第二环境。

**W6 [Minor] 术语使用不完全一致。**

- "modality" vs "strategy" vs "computation type"：Section 3.1 定义 "modality set M"，但 Section 4 多处用 "pure-strategy trajectories"，abstract 用 "two modalities"。在 game-theory 语境下 "strategy" 有特定含义（policy），而 "modality" 更接近 agent 的 computation mode。混用可能造成 confusion。
- 建议：统一使用 "modality" 或在首次出现时明确二者关系。

**W7 [Minor] Figure/Table 信息密度不均。**

- Figure 1（scatter plot）信息量较低——11 个点的 scatter 本质上可由一个相关系数概括。
- Table 1（baselines）仅 5 行，可能更适合 inline 呈现。
- 相比之下，Appendix 中的 per-task decomposition（Table 3）、seed robustness（Table 5）、data scaling（Table 6）信息量很高但被放在 Appendix——考虑将 key ablation 移入正文。

**W8 [Minor] EMNLP audience fit 存在一定张力。**

- 论文的核心贡献（counterfactual diagnostic framework + DAF metric）是 environment-agnostic 的方法论，primary testbed 是 ScienceWorld（一个 RL-style text game），且结论关于 safe RL 和 agent safety。
- 这更接近 ICML/NeurIPS agent track 或 AAAI 的受众，而非传统 EMNLP（empirical methods for NLP）。
- 但考虑到 EMNLP 近年来已收录大量 LLM agent 论文（包括 ScienceWorld 本身在 EMNLP 2022 发表），这不是 disqualifying 的。

---

## Questions（需作者回应）

**Q1.** 如果将 "internal" modality 改为 "internal reasoning + observation verification"（如每步后 call environment 一次确认 state），预计 death rate 会降到多少？这是否会让 DAF 大幅下降从而 undermine 主结论？

**Q2.** 论文声称 framework 是 "environment-agnostic"，但唯一 positive evidence 来自 ScienceWorld。能否在另一个有 death penalty 的环境（如 NetHack Learning Environment、Crafter）上复现类似 DAF？

**Q3.** "78.9% of non-tie labels are death-driven" 中，如果将 death asymmetry episodes 中 surviving strategy 的 score 也纳入考虑（即：即使 internal 没死，它的 score 是否也低于 deterministic？），是否存在 death 与 low-score 的 confound？

**Q4.** 论文承认 19/30 task types 因 "both time out" 被排除。在这些 tasks 上，如果增加 step budget（如 60 steps），routing signal 的结构是否会不同？

**Q5.** Capacity scaling（4B → 59%）的趋势是否意味着 70B 级 router 可能 work？如果是，这是否 undermine "routing problem reduces to safety-first selection" 的结论？

---

## Missing References

1. **AgentBench** (Liu et al., 2023) — 多环境 LLM agent benchmark，提供更广泛的 agent 评估视角
2. **WebArena** (Zhou et al., 2024) — 另一个有 failure mode 的 interactive web environment
3. **LATS** (Zhou et al., 2023) — Language Agent Tree Search，结合 planning + search 的 agent 方法
4. **Safe RLHF** (Dai et al., 2024) — 安全对齐中 catastrophic failure 的处理
5. **ToolBench** (Qin et al., 2023) — Tool use benchmark with failure modes
6. **MINT** (Wang et al., 2024) — Multi-turn interactive evaluation，有 multi-step failure analysis

---

## Overall Assessment

**Overall**: 3.0/5 — Findings（接近 borderline conference）

**一句话总结**: 方法论贡献扎实、实验严谨，但核心 quantitative claim（DAF=90.4%）被 penalty parameter 机械放大，结论过度泛化超出数据支撑范围，cross-env "validation" 实为 absence-of-evidence 而非 positive replication。

---

## 官方维度打分（ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 方法论正确，统计推断严谨（bootstrap CI, robustness checks），但 DAF 指标的 informativeness 受 penalty magnitude 控制，over-claim 问题影响结论有效性 |
| Excitement | 3.0/5 | 问题定位有价值（meta-question about routing signal），negative result 有 community interest，但 insight 的 depth（"hallucination kills agents"）可能不够 surprising |
| Overall | 3.0/5 | Findings-level：方法论贡献 solid，实验 thorough，但 generalizability 受限于单一 death-penalty 环境，核心结论的 framing 需要收窄 |
| Reproducibility | 4.5/5 | Algorithm 1 明确，hyperparameters 完整（Table 4），承诺 code release，bootstrap/seed details 充分 |
| Confidence | 4/5 | 熟悉 LLM agent routing 和 counterfactual evaluation 文献，仔细阅读了全文含 Appendix |

---

## 置信度

**4/5** — Quite sure. I checked the important points carefully and am familiar with the related literature on LLM routing, tool use, and interactive agent evaluation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 696 · 2026-05-16T19:09:19.177198+00:00_

Reviewer 2 审稿意见已收到。等待 Reviewer 1 返回。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 67

## Round 67

6 recorded events


### User

_source line 697 · 2026-05-16T19:09:20.112929+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

核心判断：论文方法论扎实、实验严谨，但存在两个 Critical 问题——DAF=90.4% 的 headline number 被 penalty magnitude 机械放大（P=10 时仅 50.4%），以及 "routing reduces to safety-first selection" 的结论过度泛化超出单一环境数据的支撑范围。给出 Overall 3.0（Findings level），Soundness 3.5，Excitement 3.0。

---

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿意见 — Round 9（方法严谨性 + 实验设计）

### Summary (2-3句)

本文提出 episode-level counterfactual 分析框架和 Death Avoidance Factor (DAF) 指标，分解 modular LLM agent 路由信号来源。ScienceWorld (11/30 tasks, N=245) 上 90.4% routing signal 来自死亡回避，MATH/ALFWorld 跨环境对比和 Llama 跨模型复制提供支撑证据。Trained router 在 held-out episodes 上低于 chance baseline，作为 informative negative 验证分析框架。

### Strengths

**S1. 清晰方法论贡献**：DAF 分解概念简洁，Algorithm 1 完备无歧义，78.9% penalty-independent metric 与 DAF 形成合理互补。

**S2. 诚实统计报告**：全文 p=0.079 始终标注 "not reaching α=0.05"，r=0.97 声明 "partly structural"，近似误差定量，配置差异有 caveat。

**S3. 多层次 robustness**：LOO (r: 0.963-0.980), Spearman ρ=0.986, bootstrap 10K, 8-seed cross-split, penalty sweep, reasoning-depth ablation。

**S4. 负结果有价值**：Router diagnostic 清晰展示 always-deterministic 的 trivial near-optimality，对社区有建设性。

**S5. 框架可移植性**：三个结构不同环境正确识别不同 routing mechanisms。

### Weaknesses

**W1. [Critical] r=0.97 结构性耦合被低估呈现**
- Section 3.1 / Abstract / Conclusion
- 当 DAF=90.4%，Corr(δ, 100δ+ε) ≈ 1 是数学必然。论文正文有一句 acknowledgment，但 Abstract 仅标 "partly structural"，Conclusion 完全不提。可能误导读者认为是独立经验 evidence。
- 建议：Conclusion 显式标注 "largely mathematical consequence of DAF dominance"，或降级为 robustness check。

**W2. [Critical] Data scaling 用 augmentation 而非真实数据**
- Appendix D / §3.3
- "Paraphrase-based augmentation" 不等比例放大 majority class (89.6%→97.7%)，不增加新 routing signal 模式。无法区分 "signal doesn't exist" 和 "augmentation can't create it"。论文自己估算需 ~1350 pairs 才能收集 50 个 minority-class examples。
- 建议：弱化结论为 "augmentation-based scaling provides no improvement; real-data scaling remains open"。

**W3. [Major] Capacity scaling 仅 3 个不可比数据点**
- Appendix F / §3.3
- 1.7B (47.1%) < 0.6B (50.67%)，非单调 curve。1.7B 用 8 seeds / 0.6B/4B 用 4 seeds，配置不可比。仅有 4B→59% 一个超越 baseline 的数据点。
- 建议：统一配置重跑或将 capacity claim 降级为 preliminary observation。

**W4. [Major] n=11 correlation 的 bootstrap CI 在结构耦合下 overconfident**
- §3.1, Appendix B
- Bootstrap 保留了 Δ_full ≈ δ·P 的结构，CI [0.952, 0.995] 不反映 "换一组 task types" 的 variability。
- 建议：讨论 limitation，考虑 partial correlation。

**W5. [Major] Llama replication (N=70, 0 internal-preferred) 不足以验证 framework 泛化**
- Appendix E
- 0 个 minority-class observation，只能说 "Llama dies more"，不能说 "DAF framework generalizes"。
- 建议：限定 contribution 为 "death-rate asymmetry direction generalizes"。

**W6. [Major] MATH p=0.079 — absence of evidence ≠ evidence of absence**
- §4 / Abstract / Conclusion
- N=300, effect +4.3pp, 推测 power < 50%。不显著可能仅是 underpowered。
- 建议：报告 post-hoc power 或 equivalence test。

**W7. [Minor] SCI 缺乏 null distribution**
- §2.4, SCI=0.2147 无 baseline 对比。

**W8. [Minor] 63% tasks excluded 限制泛化声明**

**W9. [Minor] 78.9% (label-level) 与 90.4% (score-level) 并列时语义不清**

### Questions

Q1: Partial correlation (控制 δ·P) 的 residual r 是多少？
Q2: 是否尝试过 class-balanced sampling / focal loss 处理 86:9 imbalance？
Q3: MATH 实验 post-hoc power 是多少？
Q4: 1.7B vs 0.6B 配置差异是否解释非单调结果？
Q5: P=100 相对于 ScienceWorld score range 的比例？

### Missing References
- Lakens 2017 (equivalence testing / TOST)
- Cohen 1988 / Brysbaert & Stevens 2018 (power analysis reporting)
- SMOTE / focal loss (class-imbalanced learning)

### Overall Assessment

**Overall**: 3.0 / 5 (Findings track — 方法框架合理但 evidence 层次有多个薄弱环节)
**Soundness**: 3.5 / 5
**Excitement**: 3.0 / 5
**Reproducibility**: 4.0 / 5
**Confidence**: 4 / 5

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 698 · 2026-05-16T19:09:59.006574+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## 交叉分享 — Reviewer 2 的完整审稿意见\n\n请逐条回应 Reviewer 2 的每个 Weakness 和 Question：对每条标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（引用论文具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 2 的完整审稿意见：\n\n## Weaknesses\n\n**W1 [Critical] DAF 的 headline number 被 penalty magnitude 机械放大，framing 存在误导。**\n- DAF = δP/(δP + Δ_nd) 是 P 的单调递增函数（论文 §3.4 承认 \"a mathematical consequence, not an empirical finding\"）。90.4% 依赖于 P=100 的选择；P=10 时 DAF 仅为 50.4%。但 Abstract 和 Conclusion 将 \"DAF=90.4%\" 作为核心卖点反复强调，给读者\"death 占九成\"的强印象——本质上是\"当 penalty 是 score gap 的 35 倍时，penalty 项主导总 gap\"，接近同义反复。78.9% penalty-independent 指标更稳健但在 Abstract 中处于从属位置。\n\n**W2 [Critical] \"Routing problem reduces to safety-first modality selection\" 过度泛化。**\n- 结论仅基于 ScienceWorld（1 个有 death penalty 的环境，11/30 task types，1 个 7B backbone）。MATH 和 ALFWorld 恰恰说明该结论不成立于无 death penalty 环境。Abstract 和 Conclusion 丢掉了 Discussion 中的 qualifiers。\n\n**W3 [Major] \"Internal modality\" 的定义混淆了 hallucination 与 reasoning。**\n- \"Internal\" 定义为 agent 自己生成中间 observation。论文 insight 本质上是 hallucinated state predictions 导致 death，不是 \"internal reasoning\" 本身有害。如果有 observation verification，death rate 可能大幅下降。真正 bottleneck 是 observation accuracy 而非 computation mode。核心发现可以更精确表述为 \"agents with unverified state predictions die more often\"——一个相对 obvious 的 observation。\n\n**W4 [Major] Contribution 3（cross-context validation）证据力不足。**\n- MATH p=0.079 不显著，方向相反，只证明 \"没有 death penalty 时没有 death-driven signal\"——tautological。ALFWorld mechanism 完全不同。两个 cross-env 都没有 death penalty，不能 validate \"death avoidance dominance\"——只能说 \"without death, no death signal\"。真正的 validation 需要另一个有 catastrophic failure 的环境重现类似 DAF。\n\n**W5 [Major] 样本量和环境覆盖的统计 power 有限。**\n- 245 episodes 中仅 95 non-tie（61.2% no-preference）。Internal-preferred 仅 9 episodes（3.7%）。19/30 task types（63%）被排除。Cross-model 仅 70 episodes、7 task types，两个 model 都是 7-8B。\n\n**W6 [Minor] 术语使用不完全一致。** \"modality\" vs \"strategy\" vs \"computation type\" 混用。\n\n**W7 [Minor] Figure/Table 信息密度不均。** Figure 1（11点scatter）信息量低；Table 1 仅 5 行；Appendix 中高信息量内容被推出正文。\n\n**W8 [Minor] EMNLP audience fit 存在一定张力。** 更接近 ICML/NeurIPS agent track。\n\n## Questions\n\nQ1. 如果 \"internal\" 改为 \"internal + observation verification\"，death rate 会降到多少？是否 undermine 主结论？\nQ2. 能否在另一个有 death penalty 的环境（NetHack/Crafter）上复现 DAF？\nQ3. Death asymmetry episodes 中 surviving strategy 的 score 是否与 death 存在 confound？\nQ4. 19/30 excluded tasks 增加 step budget 后 routing signal 结构是否不同？\nQ5. 4B→59% 的趋势是否意味着 70B router 可能 work，从而 undermine 结论？\n\n---\n\n请对每个 W1-W8 和 Q1-Q5 逐条回应 [AGREE] 或 [REBUT]。",
  "project": "simgate-modular-routing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## 交叉分享 — Reviewer 2 的完整审稿意见\n\n请逐条回应 Reviewer 2 的每个 Weakness 和 Question：对每条标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（引用论文具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 2 的完整审稿意见：\n\n## Weaknesses\n\n**W1 [Critical] DAF 的 headline number 被 penalty magnitude 机械放大，framing 存在误导。**\n- DAF = δP/(δP + Δ_nd) 是 P 的单调递增函数（论文 §3.4 承认 \"a mathematical consequence, not an empirical finding\"）。90.4% 依赖于 P=100 的选择；P=10 时 DAF 仅为 50.4%。但 Abstract 和 Conclusion 将 \"DAF=90.4%\" 作为核心卖点反复强调，给读者\"death 占九成\"的强印象——本质上是\"当 penalty 是 score gap 的 35 倍时，penalty 项主导总 gap\"，接近同义反复。78.9% penalty-independent 指标更稳健但在 Abstract 中处于从属位置。\n\n**W2 [Critical] \"Routing problem reduces to safety-first modality selection\" 过度泛化。**\n- 结论仅基于 ScienceWorld（1 个有 death penalty 的环境，11/30 task types，1 个 7B backbone）。MATH 和 ALFWorld 恰恰说明该结论不成立于无 death penalty 环境。Abstract 和 Conclusion 丢掉了 Discussion 中的 qualifiers。\n\n**W3 [Major] \"Internal modality\" 的定义混淆了 hallucination 与 reasoning。**\n- \"Internal\" 定义为 agent 自己生成中间 observation。论文 insight 本质上是 hallucinated state predictions 导致 death，不是 \"internal reasoning\" 本身有害。如果有 observation verification，death rate 可能大幅下降。真正 bottleneck 是 observation accuracy 而非 computation mode。核心发现可以更精确表述为 \"agents with unverified state predictions die more often\"——一个相对 obvious 的 observation。\n\n**W4 [Major] Contribution 3（cross-context validation）证据力不足。**\n- MATH p=0.079 不显著，方向相反，只证明 \"没有 death penalty 时没有 death-driven signal\"——tautological。ALFWorld mechanism 完全不同。两个 cross-env 都没有 death penalty，不能 validate \"death avoidance dominance\"——只能说 \"without death, no death signal\"。真正的 validation 需要另一个有 catastrophic failure 的环境重现类似 DAF。\n\n**W5 [Major] 样本量和环境覆盖的统计 power 有限。**\n- 245 episodes 中仅 95 non-tie（61.2% no-preference）。Internal-preferred 仅 9 episodes（3.7%）。19/30 task types（63%）被排除。Cross-model 仅 70 episodes、7 task types，两个 model 都是 7-8B。\n\n**W6 [Minor] 术语使用不完全一致。** \"modality\" vs \"strategy\" vs \"computation type\" 混用。\n\n**W7 [Minor] Figure/Table 信息密度不均。** Figure 1（11点scatter）信息量低；Table 1 仅 5 行；Appendix 中高信息量内容被推出正文。\n\n**W8 [Minor] EMNLP audience fit 存在一定张力。** 更接近 ICML/NeurIPS agent track。\n\n## Questions\n\nQ1. 如果 \"internal\" 改为 \"internal + observation verification\"，death rate 会降到多少？是否 undermine 主结论？\nQ2. 能否在另一个有 death penalty 的环境（NetHack/Crafter）上复现 DAF？\nQ3. Death asymmetry episodes 中 surviving strategy 的 score 是否与 death 存在 confound？\nQ4. 19/30 excluded tasks 增加 step budget 后 routing signal 结构是否不同？\nQ5. 4B→59% 的趋势是否意味着 70B router 可能 work，从而 undermine 结论？\n\n---\n\n请对每个 W1-W8 和 Q1-Q5 逐条回应 [AGREE] 或 [REBUT]。",
    "project": "simgate-modular-routing"
  }
}
```

</details>

---


### Tool result

_source line 699 · 2026-05-16T19:10:08.414534+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 9407
}
```

</details>

---


### Tool call

_source line 700 · 2026-05-16T19:10:08.465219+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## 交叉分享 — Reviewer 1 的完整审稿意见\n\n请逐条回应 Reviewer 1 的每个 Weakness 和 Question：对每条标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（引用论文具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 1 的完整审稿意见：\n\n## Weaknesses\n\n**W1 [Critical] r=0.97 结构性耦合被低估呈现**\n- 当 DAF=90.4%，Corr(δ, 100δ+ε) ≈ 1 是数学必然。论文正文有一句 acknowledgment（§4.1 \"partly structural\"），但 Abstract 仅标 \"partly structural\"，Conclusion 完全不提。可能误导读者认为是独立经验 evidence。建议 Conclusion 显式标注 \"largely mathematical consequence\" 或降级为 robustness check。\n\n**W2 [Critical] Data scaling 用 augmentation 而非真实数据**\n- \"Paraphrase-based augmentation\" 不等比例放大 majority class (89.6%→97.7%)，不增加新 routing signal 模式。无法区分 \"signal doesn't exist\" 和 \"augmentation can't create it\"。论文自己估算需 ~1350 pairs。建议弱化结论为 \"augmentation-based scaling provides no improvement; real-data scaling remains open\"。\n\n**W3 [Major] Capacity scaling 仅 3 个不可比数据点**\n- 1.7B (47.1%) < 0.6B (50.67%)，非单调 curve。1.7B 用 8 seeds / 0.6B/4B 用 4 seeds。仅 4B→59% 一个超越 baseline 的数据点。建议统一配置重跑或降级为 preliminary observation。\n\n**W4 [Major] n=11 correlation 的 bootstrap CI 在结构耦合下 overconfident**\n- Bootstrap 保留了 Δ_full ≈ δ·P 结构，CI [0.952, 0.995] 不反映 \"换一组 task types\" 的 variability。建议讨论 limitation，考虑 partial correlation。\n\n**W5 [Major] Llama replication (N=70, 0 internal-preferred) 不足以验证 framework 泛化**\n- 0 个 minority-class observation，只能说 \"Llama dies more\"，不能说 \"DAF framework generalizes\"。建议限定为 \"death-rate asymmetry direction generalizes\"。\n\n**W6 [Major] MATH p=0.079 — absence of evidence ≠ evidence of absence**\n- N=300, effect +4.3pp, power < 50%。不显著可能仅是 underpowered。建议报告 post-hoc power 或 equivalence test。\n\n**W7 [Minor] SCI 缺乏 null distribution**\n\n**W8 [Minor] 63% tasks excluded 限制泛化声明**\n\n**W9 [Minor] 78.9% (label-level) 与 90.4% (score-level) 并列时语义不清**\n\n## Questions\n\nQ1: Partial correlation (控制 δ·P) 的 residual r 是多少？\nQ2: 是否尝试过 class-balanced sampling / focal loss 处理 86:9 imbalance？\nQ3: MATH 实验 post-hoc power 是多少？\nQ4: 1.7B vs 0.6B 配置差异是否解释非单调结果？\nQ5: P=100 相对于 ScienceWorld score range 的比例？\n\n---\n\n请对每个 W1-W9 和 Q1-Q5 逐条回应 [AGREE] 或 [REBUT]。",
  "project": "simgate-modular-routing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## 交叉分享 — Reviewer 1 的完整审稿意见\n\n请逐条回应 Reviewer 1 的每个 Weakness 和 Question：对每条标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（引用论文具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 1 的完整审稿意见：\n\n## Weaknesses\n\n**W1 [Critical] r=0.97 结构性耦合被低估呈现**\n- 当 DAF=90.4%，Corr(δ, 100δ+ε) ≈ 1 是数学必然。论文正文有一句 acknowledgment（§4.1 \"partly structural\"），但 Abstract 仅标 \"partly structural\"，Conclusion 完全不提。可能误导读者认为是独立经验 evidence。建议 Conclusion 显式标注 \"largely mathematical consequence\" 或降级为 robustness check。\n\n**W2 [Critical] Data scaling 用 augmentation 而非真实数据**\n- \"Paraphrase-based augmentation\" 不等比例放大 majority class (89.6%→97.7%)，不增加新 routing signal 模式。无法区分 \"signal doesn't exist\" 和 \"augmentation can't create it\"。论文自己估算需 ~1350 pairs。建议弱化结论为 \"augmentation-based scaling provides no improvement; real-data scaling remains open\"。\n\n**W3 [Major] Capacity scaling 仅 3 个不可比数据点**\n- 1.7B (47.1%) < 0.6B (50.67%)，非单调 curve。1.7B 用 8 seeds / 0.6B/4B 用 4 seeds。仅 4B→59% 一个超越 baseline 的数据点。建议统一配置重跑或降级为 preliminary observation。\n\n**W4 [Major] n=11 correlation 的 bootstrap CI 在结构耦合下 overconfident**\n- Bootstrap 保留了 Δ_full ≈ δ·P 结构，CI [0.952, 0.995] 不反映 \"换一组 task types\" 的 variability。建议讨论 limitation，考虑 partial correlation。\n\n**W5 [Major] Llama replication (N=70, 0 internal-preferred) 不足以验证 framework 泛化**\n- 0 个 minority-class observation，只能说 \"Llama dies more\"，不能说 \"DAF framework generalizes\"。建议限定为 \"death-rate asymmetry direction generalizes\"。\n\n**W6 [Major] MATH p=0.079 — absence of evidence ≠ evidence of absence**\n- N=300, effect +4.3pp, power < 50%。不显著可能仅是 underpowered。建议报告 post-hoc power 或 equivalence test。\n\n**W7 [Minor] SCI 缺乏 null distribution**\n\n**W8 [Minor] 63% tasks excluded 限制泛化声明**\n\n**W9 [Minor] 78.9% (label-level) 与 90.4% (score-level) 并列时语义不清**\n\n## Questions\n\nQ1: Partial correlation (控制 δ·P) 的 residual r 是多少？\nQ2: 是否尝试过 class-balanced sampling / focal loss 处理 86:9 imbalance？\nQ3: MATH 实验 post-hoc power 是多少？\nQ4: 1.7B vs 0.6B 配置差异是否解释非单调结果？\nQ5: P=100 相对于 ScienceWorld score range 的比例？\n\n---\n\n请对每个 W1-W9 和 Q1-Q5 逐条回应 [AGREE] 或 [REBUT]。",
    "project": "simgate-modular-routing"
  }
}
```

</details>

---


### Tool result

_source line 701 · 2026-05-16T19:10:09.620842+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1155
}
```

</details>

---


### Assistant

_source line 702 · 2026-05-16T19:10:16.392619+00:00_

交叉分享已发出，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 68

## Round 68

2 recorded events


### User

_source line 703 · 2026-05-16T19:10:17.898097+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

总结：评分 **Overall 3.0/5 (Findings track)**。主要优势是框架设计清晰、统计报告诚实、robustness 检验充分。两个 Critical 问题：(1) r=0.97 的结构性耦合在 Abstract/Conclusion 中呈现不足，可能被误读为独立经验证据；(2) data scaling ablation 用 paraphrase augmentation 代替真实数据，无法区分 "signal 不存在" 和 "augmentation 无法生成 signal"。四个 Major 问题涉及 capacity scaling 不可比配置、n=11 bootstrap CI overconfidence、Llama replication 统计效力不足、MATH p=0.079 的 absence-of-evidence 逻辑跳跃。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 704 · 2026-05-16T19:10:23.540558+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 69

## Round 69

2 recorded events


### User

_source line 705 · 2026-05-16T19:12:27.140067+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 意见的交叉回应

---

### Weaknesses 逐条回应

**[AGREE] R1-W1: r=0.97 结构性耦合被低估呈现**

同意。与我 W1 的核心担忧一致。Corr(δ, P·δ + ε) → 1 when P·δ ≫ ε 是代数必然。§4.1 有 "partly structural" caveat + Appendix E Table 10 显示 P≤25 时不显著，但 Abstract 括号标注 + Conclusion 完全省略 qualifier，确实存在 selective qualification。降级为 robustness check 的建议合理。

**[AGREE] R1-W2: Data scaling 用 augmentation 而非真实数据**

同意。Appendix D 的 augmentation 使 Det% 从 89.6%→97.7%（Table 6），不能创造新 routing patterns。论文自估需 ~1,350 真实 pairs 但未执行。"Augmentation-based scaling provides no improvement; real-data scaling remains open" 是更准确的 reframing。

**[AGREE] R1-W3: Capacity scaling 仅 3 个不可比数据点**

同意。Table 8: 0.6B=50.67%, 1.7B=47.1%, 4B=58.96%——非单调。Table 8 caption 自己标注 1.7B 用不同 training configuration（8 seeds vs 4 seeds）。仅凭 4B 一个点超越 baseline +9pp 就声称 "capacity-dependent limitation"，证据单薄。

**[AGREE] R1-W4: Bootstrap CI 在结构耦合下 overconfident**

同意。深刻的统计观察。CI [0.952, 0.995] 度量 sampling variance of structurally coupled quantity，不度量 external validity（换一组 task types 是否仍成立）。Appendix B LOO 同理——只证明无 single leverage point，不证明泛化。

**[AGREE] R1-W5: Llama replication 不足以验证 framework 泛化**

同意。Appendix G: 70 episodes, 0 internal-preferred。无 minority-class → 无法验证 framework 识别 internal-preferred 的能力。只能说 "death-rate asymmetry direction generalizes"，与我 W5 一致。

**[AGREE] R1-W6: MATH p=0.079 — absence of evidence ≠ evidence of absence**

强烈同意。与我 W4 呈相同核心问题。Post-hoc power 估计 ~42%（N=300, effect=+4.3pp, McNemar）。不显著可能纯粹因为 underpowered。论文应报告 TOST equivalence test 或 power analysis。

**[AGREE] R1-W7: SCI 缺乏 null distribution**

同意。SCI=0.2147 需 reference distribution 才能判断 "low"。Permutation null 下的 expected Gini 未报告。Minor 但应补充。

**[REBUT] R1-W8: 63% tasks excluded 限制泛化声明**

部分反驳。Appendix A 提供 anti-cherry-picking 证据："deterministic death rate comparable between included (17.8%) and excluded (14.9%) task types"。排除标准是 "both strategies time out on all variations"——counterfactual comparison 在此条件下没有定义（无 performance gap 可分解），所以排除是 applicability boundary 而非 cherry-picking。

但同意 generalization 担忧：framework 只覆盖 37% tasks 应明确说明。

**[AGREE] R1-W9: 78.9% vs 90.4% 并列语义不清**

同意。Label-level（penalty-independent）vs score-level（penalty-dependent）在 Abstract 并列确实可能混淆。建议 primary metric 用 78.9%。

---

### Questions 回应

**[AGREE] Q1: Partial correlation** — 极好建议。根据 §5 数据（"mean non-death gap = -1.19 excluding outlier"），Δ_nd 各 task 近乎 uniform，partial r 应接近 0——恰证明 r=0.97 是结构性的。

**[AGREE] Q2: Class-balanced sampling / focal loss** — 合理 gap。86:9 极端 imbalance + Table 6 所有 scale internal recall=0.0。但 ground truth 仅 9 个 internal-preferred episodes，oversampling 可能只是 overfit。

**[AGREE] Q3: MATH post-hoc power** — 应报告。估计 ~42%，insufficient。

**[AGREE] Q4: 1.7B vs 0.6B 配置差异** — Table 8 caption 已标注，很可能解释 non-monotonicity，但缺 controlled comparison 确认。

**[REBUT] Q5: P=100 vs score range** — 论文已隐含回答：Table 1 显示典型 score 在 -9 到 -39 范围，ScienceWorld 用 0-100 normalized scoring + -100 death penalty，所以 P=100 = max positive score range。这是 environment designer 的设定，不是 empirical discovery，但论文应明确 contextualize。

---

### 总体评估

R1 的 9 个 Weakness 中我同意 8 个（W1-W7, W9），部分反驳 1 个（W8）。两份审稿的核心担忧高度一致：(a) DAF/correlation 的结构性 vs empirical 被 understated；(b) cross-env "validation" 实为 absence-of-evidence；(c) generalizability 受限于单一 death-penalty 环境。

R1 的统计建议（partial correlation, post-hoc power, equivalence test, SCI null distribution）比我更具操作性，全部应采纳。

我维持我的 Overall 3.0/5（Findings level）评分不变。R1 的分析加强了我的判断：方法论 solid、实验 thorough，但核心 quantitative claim 的 framing 需收窄，cross-env evidence 需正确定性，generalizability 需更多 positive evidence。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 706 · 2026-05-16T19:12:48.633188+00:00_

收到 Reviewer 2 对 Reviewer 1 的交叉回应。等待 Reviewer 1 对 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 70

## Round 70

8 recorded events


### User

_source line 707 · 2026-05-16T19:12:49.574452+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。对 R1 的 9 个 Weakness 中同意 8 个（W1-W7, W9），部分反驳 1 个（W8：排除 63% tasks 有方法论正当性但 generalization 担忧仍成立）。5 个 Questions 中同意 4 个，部分反驳 Q5（论文隐含已回答但应显式 contextualize）。两份审稿的核心判断一致：Findings-level，需收窄 framing 和补充 generalizability evidence。

---

[Reviewer 1 审稿意见]:
## Reviewer 1 交叉回应 — Reviewer 2 意见

### Weaknesses 回应

**[AGREE] R2-W1: DAF=90.4% headline framing 有误导**
同意。DAF = δP/(δP + Δ_nd) 在 P=100 时接近同义反复。与我的 R1-W1（r=0.97 结构耦合）根源相同。补充：78.9% penalty-independent metric 也受 Algorithm 1 labeling 优先级影响（death asymmetry 优先于 score comparison），反映 death 事件频率而非 utility 贡献。两个 metric 各有局限。

**[REBUT] R2-W2: 结论并非无条件泛化**
论文 Abstract 和 Conclusion 明确限定 "in environments with catastrophic failure modes"，不是对所有环境的泛化。MATH/ALFWorld 是 framework 正常工作的证据（不同环境→不同结论）。但同意 underlying concern：单一有 death penalty 的环境不充分——这是 evidence basis 问题（=W5 coverage），非 overclaiming 问题。

**[REBUT] R2-W3: "Obvious observation" 低估了论文贡献**
R2 的 reframing ("unverified predictions cause death") 忽略三层贡献：(1) Framework 本身（Algorithm 1 + DAF + SCI）是方法论工具；(2) 量化精度（78.9%, DAF=90.4%, SCI=0.2147）此前文献没有；(3) Router negative result 证明 analytical > learned routing。但部分同意：论文应更清晰区分 "unverified state prediction" 与 "internal reasoning"。

**[AGREE] R2-W4: Cross-context validation 近循环**
R2 最 sharp 的 observation。MATH "no death → no death signal" 接近 tautological，ALFWorld 识别不同 mechanism 但不验证 DAF 量化能力。真正 validation 需另一个 catastrophic-failure 环境。与我的 R1-W6（MATH underpowered）互补。

**[AGREE] R2-W5: 样本量限制**
与 R1-W5/W8 一致。补充：9 internal-preferred episodes 的 binomial 95% CI 为 [1.7%, 6.9%]，absolute count 太小无法做 per-category analysis。

**[AGREE] R2-W6: 术语不一致** Minor，确认存在。

**[REBUT] R2-W7: 正文信息密度是合理写作选择**
8页限制下 per-task/seed/scaling tables 推至 Appendix 是 ACL 标准做法。Figure 1 虽仅 11 点但传达跨 task 一致性。

**[REBUT] R2-W8: EMNLP audience fit 合理**
LLM agent/tool use/reasoning 在 *CL venues 已有大量先例（ReAct, Toolformer, ART）。

### Questions 回应

**[AGREE] R2-Q1**: Observation verification ablation 缺失是 gap。如果简单 verification 将 internal death rate 从 42.9% 降至 ~16%，DAF 会 collapse。

**[AGREE] R2-Q2**: 另一个 catastrophic-failure 环境（NetHack/Crafter）是最重要的补充实验。

**[REBUT] R2-Q3**: 论文 §2.4 报告残差 0.23（0.8% of Δ_full），定量控制了 surviving score confound。

**[AGREE] R2-Q4**: 增加 step budget 可能改变 excluded 63% tasks 的 routing signal 结构。

**[REBUT] R2-Q5**: 70B router 给 7B agent 做 routing 本身是 absurd resource allocation，恰恰加强 "analytical > learned routing" 的 argument。论文正确区分了 "signal exists but capacity-starved" vs "no signal"。

### 总结评估调整

Reviewer 2 的 W1（DAF framing）和 W4（cross-env tautology）是最有力的新 critique，加上我的 W1（r=0.97 coupling）和 W2（augmentation scaling），论文的 evidence 层次确实有多个薄弱环节。但 W3（obvious finding）过于 reductive，W2（overclaiming）未准确反映论文的 qualified scope。

维持我的 overall 3.0/5 (Findings track) 不变。

---

[Reviewer 1 审稿结果]:
交叉回应已提交。对 R2 的 8 个 Weakness 和 5 个 Question：

- **AGREE**: W1 (DAF framing), W4 (cross-env tautology), W5 (sample size), W6 (terminology) — 及 Q1, Q2, Q4
- **REBUT**: W2 (overclaiming — 论文有 qualifier), W3 (obvious — 低估 framework 贡献), W7 (info density — 标准做法), W8 (venue fit — *CL 有先例) — 及 Q3 (残差 0.8% 已控制), Q5 (70B 恰恰加强 cost argument)

最有力的新视角是 R2-W4（cross-env validation 的近循环性）和 R2-Q1（observation verification ablation 的缺失）。维持 overall 3.0/5 不变。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 708 · 2026-05-16T19:13:16.807507+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 709 · 2026-05-16T19:13:16.858154+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 710 · 2026-05-16T19:16:19.888750+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "simgate-modular-routing",
  "issues_yaml": "- id: \"R6-C1\"\n  summary: \"DAF penalty-dependence — headline ~90% anchored to P=100, 78.9% not primary\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 4\n  last_seen_round: 9\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"Fresh reviewers want full range + formula + dual reporting.\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"Resurfaced. Abstract still leads with DAF=90.41%. 78.9% present but not co-equal.\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Both reviewers confirm RESOLVED. 78.9% now appears co-equal with DAF throughout.\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"REOPENED. R9 reviewers argue DAF=90.4% remains headline despite co-equal presentation. Core issue: DAF = δP/(δP + Δ_nd) is monotonic in P — 90.4% at P=100 approaches tautology. Want 78.9% as PRIMARY metric, DAF as parametric companion.\"\n  action_items:\n    - round: 6\n      action: \"Abstract/Intro/§3.3/Conclusion dual reporting + DAF(P) formula\"\n      assigned_to: main_agent\n      status: done\n    - round: 7\n      action: \"Promote 78.9% to primary metric\"\n      assigned_to: main_agent\n      status: done\n    - round: 9\n      action: \"Reframe: 78.9% death-asymmetry label fraction as PRIMARY claim; DAF as penalty-parametric illustration. Or argue external validity of P=100 as typical catastrophic penalty magnitude.\"\n      assigned_to: research_director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W1\"\n  summary: \"r=0.97 structural coupling — qualifier insufficient in Abstract/Conclusion\"\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 6\n  last_seen_round: 9\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"High r partly mathematical due to penalty coupling.\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"Resurfaced. §4.1 has caveat but Abstract still reports r=0.97 without qualifier.\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"RESOLVED. Abstract now includes structural coupling qualifier.\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"REOPENED. 'Partly structural' qualifier deemed insufficient. Corr(δ, P·δ+ε)→1 when DAF=90.4% is LARGELY mathematical, not partly. Conclusion still lacks qualifier. Suggest: downgrade to robustness check OR explicitly state 'largely mathematical consequence of DAF dominance'.\"\n  action_items:\n    - round: 6\n      action: \"Add structural coupling caveat\"\n      assigned_to: main_agent\n      status: done\n    - round: 7\n      action: \"Add coupling qualifier in Abstract\"\n      assigned_to: main_agent\n      status: done\n    - round: 9\n      action: \"Strengthen qualifier: 'partly structural' → 'largely a mathematical consequence of death dominance'. Add qualifier in Conclusion. Consider demoting r=0.97 from Contribution-level claim to robustness diagnostic.\"\n      assigned_to: research_director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-C1\"\n  summary: \"Cross-env 'validation' is near-tautological — absence of death signal without death penalty is expected, not confirmatory\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Consensus. MATH (no death→no death signal) is absence-of-evidence not positive replication. ALFWorld identifies different mechanism but doesn't validate DAF. True validation requires a SECOND catastrophic-failure environment. Contribution 3 'cross-context validation' oversells.\"\n  action_items:\n    - round: 9\n      action: \"Reframe Contribution 3 as 'framework applicability demonstration' not 'validation'. Or add a second death-penalty environment (NetHack/Crafter).\"\n      assigned_to: research_director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-W1\"\n  summary: \"Data scaling ablation uses augmentation — cannot distinguish 'no signal' from 'augmentation cannot create signal'\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Consensus. Paraphrase augmentation disproportionately inflates majority class (89.6%→97.7%). Doesn't generate new routing patterns. Paper self-estimates ~1,350 real pairs needed but doesn't execute. Claim 'rules out data scarcity' too strong.\"\n  action_items:\n    - round: 9\n      action: \"Weaken conclusion to 'augmentation-based scaling provides no improvement; real-data scaling (requiring ~1,350 episode pairs) remains open'. Distinguish step-level scarcity (ruled out) vs episode-level minority-class diversity (not ruled out).\"\n      assigned_to: research_director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-W2\"\n  summary: \"Capacity scaling: 3 non-comparable data points, non-monotonic curve\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Consensus. 0.6B=50.67%, 1.7B=47.1%, 4B=58.96% — non-monotonic. 1.7B uses 8 seeds vs 4 for others. Only 4B exceeds baseline. 'Capacity-dependent limitation' claim rests on single data point.\"\n  action_items:\n    - round: 9\n      action: \"Add caveat about configuration non-comparability (Table 8 caption already notes, but text should acknowledge). Consider: unify seeds or frame as 'preliminary evidence of capacity dependence'.\"\n      assigned_to: research_director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-W3\"\n  summary: \"MATH p=0.079 underpowered — need post-hoc power analysis or equivalence test\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Consensus. Estimated post-hoc power ~42%. Non-significance may be purely due to insufficient N. Absence of evidence ≠ evidence of absence. Paper should report power or TOST equivalence test.\"\n  action_items:\n    - round: 9\n      action: \"Add post-hoc power estimate (~42%) or TOST equivalence test. If underpowered, explicitly state 'insufficient power to detect effects &lt;X pp'.\"\n      assigned_to: research_director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-W4\"\n  summary: \"Llama replication (N=70, 0 internal-preferred) insufficient for framework generalization claim\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Consensus. Zero minority-class observations — can only confirm 'Llama dies more in internal mode', not 'DAF framework generalizes'. Contribution should be limited to 'death-rate asymmetry direction generalizes across model families'.\"\n  action_items:\n    - round: 9\n      action: \"Narrow Llama contribution claim to 'direction-consistent death patterns' — avoid implying full framework validation.\"\n      assigned_to: research_director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-W5\"\n  summary: \"Bootstrap CI [0.952, 0.995] on r=0.97 reflects sampling variance only, not external validity\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Consensus. Bootstrap preserves structural coupling — CI measures within-sample stability, not generalization to new task types. LOO similarly only shows no single leverage point. Partial correlation (controlling δ·P) would likely yield r≈0.\"\n  action_items:\n    - round: 9\n      action: \"Discuss limitation: CI measures sampling stability not external validity. Consider reporting partial correlation or explicitly noting Corr(Δ_nd, Δ_full) without death term.\"\n      assigned_to: research_director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-W6\"\n  summary: \"Over-generalization: Abstract/Conclusion drop 'catastrophic failure mode' qualifier\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [2]\n      note: \"R2 raised as Critical. R1 partially rebuts: paper does say 'in environments with catastrophic failure modes' but agrees underlying evidence basis (single environment) is thin. Director downgrades to warning — qualifier exists but could be more prominent.\"\n  action_items:\n    - round: 9\n      action: \"Ensure Abstract final sentence and Conclusion consistently include 'in environments with catastrophic failure modes' qualifier. Currently present but could be lost in fast reading.\"\n      assigned_to: research_director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-W7\"\n  summary: \"Internal modality conflates hallucination with reasoning — observation verification ablation missing\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R2 raised as Major, R1 agreed. Core concern: if 'internal + verification' reduces death rate to ~16%, DAF collapses. The real bottleneck may be observation accuracy, not computation mode. Missing ablation weakens the 'modality routing' framing vs simpler 'verification suffices' explanation.\"\n  action_items:\n    - round: 9\n      action: \"Discuss in Limitations or Future Work: verification-augmented internal mode as potential DAF-reducer. Acknowledge this as most important ablation not conducted.\"\n      assigned_to: research_director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-m1\"\n  summary: \"Terminology inconsistency: modality/strategy/computation type used interchangeably\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Minor. §3.1 defines 'modality set M' but experiments use 'pure-strategy trajectories'. Potential semantic confusion.\"\n  action_items:\n    - round: 9\n      action: \"Unify terminology or add clarifying sentence at first use.\"\n      assigned_to: research_director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-m2\"\n  summary: \"78.9% (label-level) vs 90.4% (score-level) juxtaposition semantically unclear\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"One is count-based (labels), other is score-gap-based (DAF). When presented together readers may conflate.\"\n  action_items:\n    - round: 9\n      action: \"Add explicit 1-sentence clarification distinguishing the two metrics' domains when first juxtaposed.\"\n      assigned_to: research_director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-m3\"\n  summary: \"SCI=0.2147 lacks null distribution baseline\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Minor. No permutation null or expected Gini under random routing signal distribution.\"\n  action_items:\n    - round: 9\n      action: \"Add permutation null or note expected value under uniform distribution for reference.\"\n      assigned_to: research_director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# Previously resolved issues (Rounds 4-8) — retained for history\n- id: \"R6-C2\"\n  summary: \"Missing counterfactual-in-RL literature paragraph\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"Paper uses 'counterfactual' in title, must contextualize.\"\n  action_items:\n    - round: 6\n      action: \"Add paragraph + 3 refs\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"related_work.tex has prospective paired comparison paragraph.\"\n  resolution_round: 6\n\n- id: \"R6-W2\"\n  summary: \"Prescreening 19/30 exclusion — scope qualifier needed\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"Want excluded task characteristics.\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"Resurfaced as CRITICAL.\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1 confirms RESOLVED. R2 residual concern rebutted by R1.\"\n  action_items:\n    - round: 6\n      action: \"Expand Limitations with excluded task characteristics\"\n      assigned_to: main_agent\n      status: done\n    - round: 7\n      action: \"Add scope qualifier to title/abstract/conclusion\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"Title has 'on ScienceWorld', Abstract has '11 of 30', Appendix B has anti-cherry-picking.\"\n  resolution_round: 8\n\n- id: \"R6-W3\"\n  summary: \"Missing failure mode analysis — death temporal pattern\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [2]\n      note: \"Director降为warning.\"\n  action_items:\n    - round: 6\n      action: \"Extract death step data\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"Death temporal data extracted.\"\n  resolution_round: 6\n\n- id: \"R6-W4\"\n  summary: \"Deterministic strategy operationalization description insufficient\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"Need what LLM sees in each mode.\"\n  action_items:\n    - round: 6\n      action: \"§3.1 add ground-truth vs self-prediction description\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"method.tex describes both modes.\"\n  resolution_round: 6\n\n- id: \"R6-W5\"\n  summary: \"MATH pilot (n=50) needs confidence intervals\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"Consensus.\"\n  action_items:\n    - round: 6\n      action: \"Add binomial 95% CI\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"Limitations has MATH CIs.\"\n  resolution_round: 6\n\n- id: \"R6-W6\"\n  summary: \"find-non-living-thing bimodal DAF distribution not noted\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"DAF=0% vs others >85% heterogeneity.\"\n  action_items:\n    - round: 6\n      action: \"Add 1 sentence on bimodal distribution\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"experiments.tex notes bimodal DAF.\"\n  resolution_round: 6\n\n- id: \"R6-W7\"\n  summary: \"Concurrent work discussion too brief\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"tool-overuse-illusion and tool-use-tax need deeper discussion.\"\n  action_items:\n    - round: 6\n      action: \"Expand concurrent work\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"Related Work expanded.\"\n  resolution_round: 6\n\n- id: \"R6-W8\"\n  summary: \"Safe RL literature coverage insufficient\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 8\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"Need 2024+ safe RL refs.\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"Only Garcia 2015 survey cited.\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R2 confirms RESOLVED. CRPO added.\"\n  action_items:\n    - round: 6\n      action: \"Add recent safe RL references\"\n      assigned_to: main_agent\n      status: done\n    - round: 7\n      action: \"Add specific safety critic references\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"CRPO citation added.\"\n  resolution_round: 8\n\n- id: \"R7-N1\"\n  summary: \"ALFWorld data — no methodology description\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"Model, det modality, labeling process all missing.\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"RESOLVED. Appendix A.9 complete.\"\n  action_items:\n    - round: 7\n      action: \"Add full ALFWorld methodology\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"Appendix A.9 contains complete ALFWorld methodology.\"\n  resolution_round: 8\n\n- id: \"R7-N2\"\n  summary: \"Router diagnostic conclusion confounded with data insufficiency\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"81 train samples, cannot distinguish thin signal from insufficient data.\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Partially fixed. Residual: augmentation doesn't increase episode diversity.\"\n  action_items:\n    - round: 7\n      action: \"Acknowledge data-size confound; downgrade Contribution 4\"\n      assigned_to: main_agent\n      status: done\n    - round: 8\n      action: \"Soften 'rules out data scarcity'\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Step-level vs episode-level scarcity distinction added with 1,350 paired episodes estimate.\"\n  resolution_round: 8\n\n- id: \"R7-W1\"\n  summary: \"MATH p=0.079 asymmetric use — 'vanishes' overstates\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"Abstract/Conclusion present label inversion too strongly.\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Consensus Must-Fix. 'vanishes' still present.\"\n  action_items:\n    - round: 7\n      action: \"Mark 'not statistically significant' consistently\"\n      assigned_to: main_agent\n      status: done\n    - round: 8\n      action: \"Replace 'vanishes' with hedged alternatives\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"All 5 occurrences replaced. Conclusion has 'not reaching α=0.05'.\"\n  resolution_round: 8\n\n- id: \"R7-W2\"\n  summary: \"Llama pilot (N=10) too small for Contribution 3\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"No statistical power at N=10.\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"RESOLVED. Llama downgraded to directional observation.\"\n  action_items:\n    - round: 7\n      action: \"Remove from Contribution 3; retain as directional\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"Now upgraded to 7 tasks, 70 episodes, 7/7 direction consistent.\"\n  resolution_round: 8\n\n- id: \"R7-W3\"\n  summary: \"Pure-strategy labeling vs mixed-strategy deployment gap\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"DAgger cite insufficient.\"\n    - round: 8\n      reviewers: [1]\n      note: \"RESOLVED.\"\n  action_items:\n    - round: 7\n      action: \"Analyze death timing; discuss mixed-routing implications\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"Limitations discusses distribution shift with DAgger citation.\"\n  resolution_round: 8\n\n- id: \"R7-W4\"\n  summary: \"Only ReAct tested — Reflexion/ToT may reduce death rate\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"Reflexion self-correction may lower death rate.\"\n    - round: 8\n      reviewers: [1]\n      note: \"RESOLVED.\"\n  action_items:\n    - round: 7\n      action: \"Add reasoning strategy generalization discussion\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"Limitations discusses Reflexion.\"\n  resolution_round: 8\n\n- id: \"R7-W5\"\n  summary: \"Missing key references: RouteLLM, Reflexion, tool-learning survey\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"RouteLLM most urgent.\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"RESOLVED. All three present.\"\n  action_items:\n    - round: 7\n      action: \"Add RouteLLM, Reflexion, tool-learning survey\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"All cited in Related Work.\"\n  resolution_round: 8\n\n- id: \"R7-m1\"\n  summary: \"Bib issues: retool-2026 key vs 2025 year\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"Both flagged.\"\n    - round: 8\n      reviewers: [2]\n      note: \"RESOLVED.\"\n  action_items:\n    - round: 7\n      action: \"Fix bib key/year\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"Bib entries corrected.\"\n  resolution_round: 8\n\n- id: \"R7-m2\"\n  summary: \"Abstract '90.41%' false precision; Ethics 'RTX 5090'\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"90.41% → ~90%. RTX 5090 → consumer GPUs.\"\n    - round: 8\n      reviewers: [2]\n      note: \"RESOLVED.\"\n  action_items:\n    - round: 7\n      action: \"Round DAF; generalize GPU\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"90.4% with CI; GPU generalized.\"\n  resolution_round: 8\n\n- id: \"R7-m3\"\n  summary: \"find-non-living-thing 40 episodes unexplained; no code/data release\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n    - round: 7\n      reviewers: [1]\n      note: \"Minor reproducibility.\"\n    - round: 8\n      reviewers: [2]\n      note: \"RESOLVED.\"\n  action_items:\n    - round: 7\n      action: \"Explain episode count; add availability statement\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"Table footnote + Ethics Statement.\"\n  resolution_round: 8\n\n- id: \"R8-W1\"\n  summary: \"'routing signal vanishes' overstates non-significant MATH result\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Consensus Must-Fix.\"\n  action_items:\n    - round: 8\n      action: \"Replace 'vanishes' with hedged alternatives\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"5 occurrences replaced.\"\n  resolution_round: 8\n\n- id: \"R8-W2\"\n  summary: \"Data scaling minority-class confound — augmentation doesn't increase episode diversity\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"32x augmentation only adds surface diversity.\"\n  action_items:\n    - round: 8\n      action: \"Soften 'rules out data scarcity'\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Step-level vs episode-level distinction added.\"\n  resolution_round: 8\n\n- id: \"R8-W3\"\n  summary: \"Capacity scaling ablation lacks episode-level evaluation\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Only step-level reported.\"\n  action_items:\n    - round: 8\n      action: \"Run episode-level eval on existing checkpoints\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"Episode-level eval: 0.6B=50.67%, 1.7B=47.1%, 4B=58.96%.\"\n  resolution_round: 8\n\n- id: \"R8-W4\"\n  summary: \"'Safety critic' analogy overstretched\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Router failed, this is default policy not learned critic.\"\n  action_items:\n    - round: 8\n      action: \"Revise to 'safety-first modality selection'\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Revised throughout.\"\n  resolution_round: 8\n\n- id: \"R8-W5\"\n  summary: \"Deterministic modality definition varies across environments\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [2]\n      note: \"R2 raised, R1 rebuts but agrees presentation improvement.\"\n  action_items:\n    - round: 8\n      action: \"Add modality heterogeneity paragraph in Discussion\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Discussion paragraph added.\"\n  resolution_round: 8\n\n- id: \"R8-W6\"\n  summary: \"Reasoning depth ablation sample size unreported\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"n per condition missing.\"\n  action_items:\n    - round: 8\n      action: \"Report n=120 episodes per condition\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"n=120 added.\"\n  resolution_round: 8\n\n- id: \"R8-W7\"\n  summary: \"r=0.97 mathematical near-inevitability not foregrounded in §4.1\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"§4.1 first mention lacks explicit condition.\"\n  action_items:\n    - round: 8\n      action: \"Add Var condition statement\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"§4.1 has 3-sentence addition.\"\n  resolution_round: 8\n\n- id: \"R8-m1\"\n  summary: \"3 orphan bib entries; tool-learning-survey year uncertain\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Camera-ready cleanup.\"\n  action_items:\n    - round: 8\n      action: \"Verify citations\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"All cited. tot-2023 bib added.\"\n  resolution_round: 8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "simgate-modular-routing",
    "issues_yaml": "- id: \"R6-C1\"\n  summary: \"DAF penalty-dependence — headline ~90% anchored to P=100, 78.9% not primary\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 4\n  last_seen_round: 9\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"Fresh reviewers want full range + formula + dual reporting.\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"Resurfaced. Abstract still leads with DAF=90.41%. 78.9% present but not co-equal.\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Both reviewers confirm RESOLVED. 78.9% now appears co-equal with DAF throughout.\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"REOPENED. R9 reviewers argue DAF=90.4% remains headline despite co-equal presentation. Core issue: DAF = δP/(δP + Δ_nd) is monotonic in P — 90.4% at P=100 approaches tautology. Want 78.9% as PRIMARY metric, DAF as parametric companion.\"\n  action_items:\n    - round: 6\n      action: \"Abstract/Intro/§3.3/Conclusion dual reporting + DAF(P) formula\"\n      assigned_to: main_agent\n      status: done\n    - round: 7\n      action: \"Promote 78.9% to primary metric\"\n      assigned_to: main_agent\n      status: done\n    - round: 9\n      action: \"Reframe: 78.9% death-asymmetry label fraction as PRIMARY claim; DAF as penalty-parametric illustration. Or argue external validity of P=100 as typical catastrophic penalty magnitude.\"\n      assigned_to: research_director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R6-W1\"\n  summary: \"r=0.97 structural coupling — qualifier insufficient in Abstract/Conclusion\"\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 6\n  last_seen_round: 9\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"High r partly mathematical due to penalty coupling.\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"Resurfaced. §4.1 has caveat but Abstract still reports r=0.97 without qualifier.\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"RESOLVED. Abstract now includes structural coupling qualifier.\"\n    - round: 9\n      reviewers: [1, 2]\n      note: \"REOPENED. 'Partly structural' qualifier deemed insufficient. Corr(δ, P·δ+ε)→1 when DAF=90.4% is LARGELY mathematical, not partly. Conclusion still lacks qualifier. Suggest: downgrade to robustness check OR explicitly state 'largely mathematical consequence of DAF dominance'.\"\n  action_items:\n    - round: 6\n      action: \"Add structural coupling caveat\"\n      assigned_to: main_agent\n      status: done\n    - round: 7\n      action: \"Add coupling qualifier in Abstract\"\n      assigned_to: main_agent\n      status: done\n    - round: 9\n      action: \"Strengthen qualifier: 'partly structural' → 'largely a mathematical consequence of death dominance'. Add qualifier in Conclusion. Consider demoting r=0.97 from Contribution-level claim to robustness diagnostic.\"\n      assigned_to: research_director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-C1\"\n  summary: \"Cross-env 'validation' is near-tautological — absence of death signal without death penalty is expected, not confirmatory\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Consensus. MATH (no death→no death signal) is absence-of-evidence not positive replication. ALFWorld identifies different mechanism but doesn't validate DAF. True validation requires a SECOND catastrophic-failure environment. Contribution 3 'cross-context validation' oversells.\"\n  action_items:\n    - round: 9\n      action: \"Reframe Contribution 3 as 'framework applicability demonstration' not 'validation'. Or add a second death-penalty environment (NetHack/Crafter).\"\n      assigned_to: research_director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-W1\"\n  summary: \"Data scaling ablation uses augmentation — cannot distinguish 'no signal' from 'augmentation cannot create signal'\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Consensus. Paraphrase augmentation disproportionately inflates majority class (89.6%→97.7%). Doesn't generate new routing patterns. Paper self-estimates ~1,350 real pairs needed but doesn't execute. Claim 'rules out data scarcity' too strong.\"\n  action_items:\n    - round: 9\n      action: \"Weaken conclusion to 'augmentation-based scaling provides no improvement; real-data scaling (requiring ~1,350 episode pairs) remains open'. Distinguish step-level scarcity (ruled out) vs episode-level minority-class diversity (not ruled out).\"\n      assigned_to: research_director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-W2\"\n  summary: \"Capacity scaling: 3 non-comparable data points, non-monotonic curve\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Consensus. 0.6B=50.67%, 1.7B=47.1%, 4B=58.96% — non-monotonic. 1.7B uses 8 seeds vs 4 for others. Only 4B exceeds baseline. 'Capacity-dependent limitation' claim rests on single data point.\"\n  action_items:\n    - round: 9\n      action: \"Add caveat about configuration non-comparability (Table 8 caption already notes, but text should acknowledge). Consider: unify seeds or frame as 'preliminary evidence of capacity dependence'.\"\n      assigned_to: research_director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-W3\"\n  summary: \"MATH p=0.079 underpowered — need post-hoc power analysis or equivalence test\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Consensus. Estimated post-hoc power ~42%. Non-significance may be purely due to insufficient N. Absence of evidence ≠ evidence of absence. Paper should report power or TOST equivalence test.\"\n  action_items:\n    - round: 9\n      action: \"Add post-hoc power estimate (~42%) or TOST equivalence test. If underpowered, explicitly state 'insufficient power to detect effects &lt;X pp'.\"\n      assigned_to: research_director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-W4\"\n  summary: \"Llama replication (N=70, 0 internal-preferred) insufficient for framework generalization claim\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Consensus. Zero minority-class observations — can only confirm 'Llama dies more in internal mode', not 'DAF framework generalizes'. Contribution should be limited to 'death-rate asymmetry direction generalizes across model families'.\"\n  action_items:\n    - round: 9\n      action: \"Narrow Llama contribution claim to 'direction-consistent death patterns' — avoid implying full framework validation.\"\n      assigned_to: research_director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-W5\"\n  summary: \"Bootstrap CI [0.952, 0.995] on r=0.97 reflects sampling variance only, not external validity\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Consensus. Bootstrap preserves structural coupling — CI measures within-sample stability, not generalization to new task types. LOO similarly only shows no single leverage point. Partial correlation (controlling δ·P) would likely yield r≈0.\"\n  action_items:\n    - round: 9\n      action: \"Discuss limitation: CI measures sampling stability not external validity. Consider reporting partial correlation or explicitly noting Corr(Δ_nd, Δ_full) without death term.\"\n      assigned_to: research_director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-W6\"\n  summary: \"Over-generalization: Abstract/Conclusion drop 'catastrophic failure mode' qualifier\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [2]\n      note: \"R2 raised as Critical. R1 partially rebuts: paper does say 'in environments with catastrophic failure modes' but agrees underlying evidence basis (single environment) is thin. Director downgrades to warning — qualifier exists but could be more prominent.\"\n  action_items:\n    - round: 9\n      action: \"Ensure Abstract final sentence and Conclusion consistently include 'in environments with catastrophic failure modes' qualifier. Currently present but could be lost in fast reading.\"\n      assigned_to: research_director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-W7\"\n  summary: \"Internal modality conflates hallucination with reasoning — observation verification ablation missing\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"R2 raised as Major, R1 agreed. Core concern: if 'internal + verification' reduces death rate to ~16%, DAF collapses. The real bottleneck may be observation accuracy, not computation mode. Missing ablation weakens the 'modality routing' framing vs simpler 'verification suffices' explanation.\"\n  action_items:\n    - round: 9\n      action: \"Discuss in Limitations or Future Work: verification-augmented internal mode as potential DAF-reducer. Acknowledge this as most important ablation not conducted.\"\n      assigned_to: research_director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-m1\"\n  summary: \"Terminology inconsistency: modality/strategy/computation type used interchangeably\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Minor. §3.1 defines 'modality set M' but experiments use 'pure-strategy trajectories'. Potential semantic confusion.\"\n  action_items:\n    - round: 9\n      action: \"Unify terminology or add clarifying sentence at first use.\"\n      assigned_to: research_director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-m2\"\n  summary: \"78.9% (label-level) vs 90.4% (score-level) juxtaposition semantically unclear\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"One is count-based (labels), other is score-gap-based (DAF). When presented together readers may conflate.\"\n  action_items:\n    - round: 9\n      action: \"Add explicit 1-sentence clarification distinguishing the two metrics' domains when first juxtaposed.\"\n      assigned_to: research_director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"R9-m3\"\n  summary: \"SCI=0.2147 lacks null distribution baseline\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 9\n  last_seen_round: 9\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"Minor. No permutation null or expected Gini under random routing signal distribution.\"\n  action_items:\n    - round: 9\n      action: \"Add permutation null or note expected value under uniform distribution for reference.\"\n      assigned_to: research_director\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# Previously resolved issues (Rounds 4-8) — retained for history\n- id: \"R6-C2\"\n  summary: \"Missing counterfactual-in-RL literature paragraph\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"Paper uses 'counterfactual' in title, must contextualize.\"\n  action_items:\n    - round: 6\n      action: \"Add paragraph + 3 refs\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"related_work.tex has prospective paired comparison paragraph.\"\n  resolution_round: 6\n\n- id: \"R6-W2\"\n  summary: \"Prescreening 19/30 exclusion — scope qualifier needed\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 8\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"Want excluded task characteristics.\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"Resurfaced as CRITICAL.\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R1 confirms RESOLVED. R2 residual concern rebutted by R1.\"\n  action_items:\n    - round: 6\n      action: \"Expand Limitations with excluded task characteristics\"\n      assigned_to: main_agent\n      status: done\n    - round: 7\n      action: \"Add scope qualifier to title/abstract/conclusion\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"Title has 'on ScienceWorld', Abstract has '11 of 30', Appendix B has anti-cherry-picking.\"\n  resolution_round: 8\n\n- id: \"R6-W3\"\n  summary: \"Missing failure mode analysis — death temporal pattern\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [2]\n      note: \"Director降为warning.\"\n  action_items:\n    - round: 6\n      action: \"Extract death step data\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"Death temporal data extracted.\"\n  resolution_round: 6\n\n- id: \"R6-W4\"\n  summary: \"Deterministic strategy operationalization description insufficient\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"Need what LLM sees in each mode.\"\n  action_items:\n    - round: 6\n      action: \"§3.1 add ground-truth vs self-prediction description\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"method.tex describes both modes.\"\n  resolution_round: 6\n\n- id: \"R6-W5\"\n  summary: \"MATH pilot (n=50) needs confidence intervals\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"Consensus.\"\n  action_items:\n    - round: 6\n      action: \"Add binomial 95% CI\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"Limitations has MATH CIs.\"\n  resolution_round: 6\n\n- id: \"R6-W6\"\n  summary: \"find-non-living-thing bimodal DAF distribution not noted\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"DAF=0% vs others >85% heterogeneity.\"\n  action_items:\n    - round: 6\n      action: \"Add 1 sentence on bimodal distribution\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"experiments.tex notes bimodal DAF.\"\n  resolution_round: 6\n\n- id: \"R6-W7\"\n  summary: \"Concurrent work discussion too brief\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 6\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"tool-overuse-illusion and tool-use-tax need deeper discussion.\"\n  action_items:\n    - round: 6\n      action: \"Expand concurrent work\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"Related Work expanded.\"\n  resolution_round: 6\n\n- id: \"R6-W8\"\n  summary: \"Safe RL literature coverage insufficient\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 8\n  mentions:\n    - round: 6\n      reviewers: [1, 2]\n      note: \"Need 2024+ safe RL refs.\"\n    - round: 7\n      reviewers: [1, 2]\n      note: \"Only Garcia 2015 survey cited.\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"R2 confirms RESOLVED. CRPO added.\"\n  action_items:\n    - round: 6\n      action: \"Add recent safe RL references\"\n      assigned_to: main_agent\n      status: done\n    - round: 7\n      action: \"Add specific safety critic references\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"CRPO citation added.\"\n  resolution_round: 8\n\n- id: \"R7-N1\"\n  summary: \"ALFWorld data — no methodology description\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"Model, det modality, labeling process all missing.\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"RESOLVED. Appendix A.9 complete.\"\n  action_items:\n    - round: 7\n      action: \"Add full ALFWorld methodology\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"Appendix A.9 contains complete ALFWorld methodology.\"\n  resolution_round: 8\n\n- id: \"R7-N2\"\n  summary: \"Router diagnostic conclusion confounded with data insufficiency\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"81 train samples, cannot distinguish thin signal from insufficient data.\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Partially fixed. Residual: augmentation doesn't increase episode diversity.\"\n  action_items:\n    - round: 7\n      action: \"Acknowledge data-size confound; downgrade Contribution 4\"\n      assigned_to: main_agent\n      status: done\n    - round: 8\n      action: \"Soften 'rules out data scarcity'\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Step-level vs episode-level scarcity distinction added with 1,350 paired episodes estimate.\"\n  resolution_round: 8\n\n- id: \"R7-W1\"\n  summary: \"MATH p=0.079 asymmetric use — 'vanishes' overstates\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"Abstract/Conclusion present label inversion too strongly.\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Consensus Must-Fix. 'vanishes' still present.\"\n  action_items:\n    - round: 7\n      action: \"Mark 'not statistically significant' consistently\"\n      assigned_to: main_agent\n      status: done\n    - round: 8\n      action: \"Replace 'vanishes' with hedged alternatives\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"All 5 occurrences replaced. Conclusion has 'not reaching α=0.05'.\"\n  resolution_round: 8\n\n- id: \"R7-W2\"\n  summary: \"Llama pilot (N=10) too small for Contribution 3\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"No statistical power at N=10.\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"RESOLVED. Llama downgraded to directional observation.\"\n  action_items:\n    - round: 7\n      action: \"Remove from Contribution 3; retain as directional\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"Now upgraded to 7 tasks, 70 episodes, 7/7 direction consistent.\"\n  resolution_round: 8\n\n- id: \"R7-W3\"\n  summary: \"Pure-strategy labeling vs mixed-strategy deployment gap\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"DAgger cite insufficient.\"\n    - round: 8\n      reviewers: [1]\n      note: \"RESOLVED.\"\n  action_items:\n    - round: 7\n      action: \"Analyze death timing; discuss mixed-routing implications\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"Limitations discusses distribution shift with DAgger citation.\"\n  resolution_round: 8\n\n- id: \"R7-W4\"\n  summary: \"Only ReAct tested — Reflexion/ToT may reduce death rate\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"Reflexion self-correction may lower death rate.\"\n    - round: 8\n      reviewers: [1]\n      note: \"RESOLVED.\"\n  action_items:\n    - round: 7\n      action: \"Add reasoning strategy generalization discussion\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"Limitations discusses Reflexion.\"\n  resolution_round: 8\n\n- id: \"R7-W5\"\n  summary: \"Missing key references: RouteLLM, Reflexion, tool-learning survey\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"RouteLLM most urgent.\"\n    - round: 8\n      reviewers: [1, 2]\n      note: \"RESOLVED. All three present.\"\n  action_items:\n    - round: 7\n      action: \"Add RouteLLM, Reflexion, tool-learning survey\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"All cited in Related Work.\"\n  resolution_round: 8\n\n- id: \"R7-m1\"\n  summary: \"Bib issues: retool-2026 key vs 2025 year\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"Both flagged.\"\n    - round: 8\n      reviewers: [2]\n      note: \"RESOLVED.\"\n  action_items:\n    - round: 7\n      action: \"Fix bib key/year\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"Bib entries corrected.\"\n  resolution_round: 8\n\n- id: \"R7-m2\"\n  summary: \"Abstract '90.41%' false precision; Ethics 'RTX 5090'\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n    - round: 7\n      reviewers: [1, 2]\n      note: \"90.41% → ~90%. RTX 5090 → consumer GPUs.\"\n    - round: 8\n      reviewers: [2]\n      note: \"RESOLVED.\"\n  action_items:\n    - round: 7\n      action: \"Round DAF; generalize GPU\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"90.4% with CI; GPU generalized.\"\n  resolution_round: 8\n\n- id: \"R7-m3\"\n  summary: \"find-non-living-thing 40 episodes unexplained; no code/data release\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  mentions:\n    - round: 7\n      reviewers: [1]\n      note: \"Minor reproducibility.\"\n    - round: 8\n      reviewers: [2]\n      note: \"RESOLVED.\"\n  action_items:\n    - round: 7\n      action: \"Explain episode count; add availability statement\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"Table footnote + Ethics Statement.\"\n  resolution_round: 8\n\n- id: \"R8-W1\"\n  summary: \"'routing signal vanishes' overstates non-significant MATH result\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Consensus Must-Fix.\"\n  action_items:\n    - round: 8\n      action: \"Replace 'vanishes' with hedged alternatives\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"5 occurrences replaced.\"\n  resolution_round: 8\n\n- id: \"R8-W2\"\n  summary: \"Data scaling minority-class confound — augmentation doesn't increase episode diversity\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"32x augmentation only adds surface diversity.\"\n  action_items:\n    - round: 8\n      action: \"Soften 'rules out data scarcity'\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Step-level vs episode-level distinction added.\"\n  resolution_round: 8\n\n- id: \"R8-W3\"\n  summary: \"Capacity scaling ablation lacks episode-level evaluation\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Only step-level reported.\"\n  action_items:\n    - round: 8\n      action: \"Run episode-level eval on existing checkpoints\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"Episode-level eval: 0.6B=50.67%, 1.7B=47.1%, 4B=58.96%.\"\n  resolution_round: 8\n\n- id: \"R8-W4\"\n  summary: \"'Safety critic' analogy overstretched\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Router failed, this is default policy not learned critic.\"\n  action_items:\n    - round: 8\n      action: \"Revise to 'safety-first modality selection'\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Revised throughout.\"\n  resolution_round: 8\n\n- id: \"R8-W5\"\n  summary: \"Deterministic modality definition varies across environments\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [2]\n      note: \"R2 raised, R1 rebuts but agrees presentation improvement.\"\n  action_items:\n    - round: 8\n      action: \"Add modality heterogeneity paragraph in Discussion\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"Discussion paragraph added.\"\n  resolution_round: 8\n\n- id: \"R8-W6\"\n  summary: \"Reasoning depth ablation sample size unreported\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"n per condition missing.\"\n  action_items:\n    - round: 8\n      action: \"Report n=120 episodes per condition\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"n=120 added.\"\n  resolution_round: 8\n\n- id: \"R8-W7\"\n  summary: \"r=0.97 mathematical near-inevitability not foregrounded in §4.1\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"§4.1 first mention lacks explicit condition.\"\n  action_items:\n    - round: 8\n      action: \"Add Var condition statement\"\n      assigned_to: paper_agent\n      status: done\n  resolution: \"§4.1 has 3-sentence addition.\"\n  resolution_round: 8\n\n- id: \"R8-m1\"\n  summary: \"3 orphan bib entries; tool-learning-survey year uncertain\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 8\n  mentions:\n    - round: 8\n      reviewers: [1, 2]\n      note: \"Camera-ready cleanup.\"\n  action_items:\n    - round: 8\n      action: \"Verify citations\"\n      assigned_to: main_agent\n      status: done\n  resolution: \"All cited. tot-2023 bib added.\"\n  resolution_round: 8"
  }
}
```

</details>

---


### Tool result

_source line 711 · 2026-05-16T19:16:19.990103+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/review_issues.yaml\", \"bytes\": 26223}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 712 · 2026-05-16T19:18:18.108172+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 9 审稿报告 — simgate-modular-routing\n\n**论文**: \"Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\"\n**Venue**: EMNLP 2026 Main Conference Long Paper (ARR May cycle)\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计; R2: 新颖性+完整性）\n**流程**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮即达共识）\n\n---\n\n## Summary\n\n本文提出 episode-level counterfactual analysis 框架和 Death Avoidance Factor (DAF) 指标，分解 modular LLM agent 的 routing signal 来源。在 ScienceWorld（11/30 task types, N=245, Qwen2.5-7B-Instruct）上发现 78.9% 的 non-tie routing labels 由 death asymmetry 驱动，DAF=90.4%（P=100）。Trained router 在 held-out episodes 上低于 chance baseline（47.1% vs 50%）。跨环境分析（MATH N=300, ALFWorld N=135）和跨模型复制（Llama-3.1-8B, N=70）提供辅助证据。\n\n---\n\n## Strengths\n\n**S1. 问题定位精准。** 在 routing 文献集中于\"如何 route\"时，退后一步问\"什么驱动 routing signal\"——是被忽视的元问题，具有方法论价值。\n\n**S2. 框架设计简洁可复现。** Algorithm 1 完备无歧义，仅需 paired episode outcomes，environment-agnostic 属性通过三个结构迥异环境得到演示。\n\n**S3. 统计报告诚实严谨。** p=0.079 始终标注 \"not reaching α=0.05\"，r=0.97 标注 \"partly structural\"，Bootstrap/LOO/Spearman 三重 robustness，8-seed cross-split evaluation。\n\n**S4. 多层次 robustness 检验。** LOO (r: 0.963-0.980), Spearman ρ=0.986, 10K bootstrap, penalty sweep (P=10-500), reasoning-depth ablation, data scaling (25%-800%), capacity scaling (0.6B-4B), cross-model replication。\n\n**S5. Negative result 呈现诚实且有建设性。** Router diagnostic 清晰展示 always-deterministic 的 trivial near-optimality，对社区有建设性信息。\n\n**S6. Limitations 坦诚具体。** 19/30 exclusion, penalty amplification, single-pass ReAct, distribution shift (DAgger), 7-8B scale limitation 均明确列出。\n\n---\n\n## Weaknesses\n\n### Must-Fix (Critical)\n\n**W1. DAF=90.4% headline number 被 penalty magnitude 机械放大 [Consensus]**\n- DAF = δP/(δP + Δ_nd) 是 P 的单调递增函数。在 P=100 时 90.4% 接近同义反复（\"当 penalty 是 score gap 的 35 倍时，penalty 项主导总 gap\"）。P=10 时仅 50.4%。\n- 78.9% penalty-independent metric 更稳健但仍处于从属位置。\n- 论文自承 \"mathematical consequence, not empirical finding\"（§3.4），但 Abstract/Conclusion 的 framing 仍以 DAF 为核心卖点。\n- **要求**：将 78.9% death-asymmetry label fraction 提升为 PRIMARY quantitative claim；或论证 P=100 具有外部效度（typical catastrophic penalty magnitude across environments）。\n\n**W2. r=0.97 结构性耦合呈现不足 [Consensus]**\n- 当 DAF=90.4%（即 Δ_full ≈ δ·P），Corr(δ, δ·P + ε) → 1 是代数必然。\n- Abstract 标 \"partly structural\" 不够——应为 \"largely a mathematical consequence of death dominance\"。Conclusion 完全未提及。\n- Partial correlation（控制 δ·P）预计 r ≈ 0，证实这不是独立经验证据。\n- **要求**：Conclusion 加强 qualifier；或将 r=0.97 从 Contribution-level claim 降级为 robustness diagnostic。\n\n**W3. Cross-env \"validation\" 近循环 [Consensus]**\n- MATH（无 death → 无 death signal）是 absence-of-evidence，不是 positive replication。ALFWorld 识别不同 mechanism 但不验证 DAF 量化能力。\n- 真正的 validation 需要第二个有 catastrophic failure 的环境（如 NetHack/Crafter）重现 similar DAF。\n- Contribution 3 标为 \"cross-context validation\" 属 overselling。\n- **要求**：重新定性为 \"framework applicability demonstration\"；或补充第二个 death-penalty 环境数据。\n\n**W4. Data scaling ablation 用 augmentation 代替真实数据 [Consensus]**\n- Paraphrase augmentation 不等比例放大 majority class（89.6%→97.7%），不创造新 routing patterns。\n- 无法区分 \"signal 不存在\" 和 \"augmentation 无法创造 signal\"。论文自估需 ~1,350 真实 pairs 但未执行。\n- **要求**：弱化为 \"augmentation-based scaling provides no improvement; real-data scaling (requiring ~1,350 episode pairs for 50 minority-class examples) remains open\"。\n\n### Should-Fix (Warning)\n\n**W5. Capacity scaling: 3 个不可比数据点 [Consensus]**\n- 0.6B=50.67%, 1.7B=47.1%, 4B=58.96%——非单调。1.7B 用 8 seeds vs 4 seeds for others。仅 4B 一个点超越 baseline。\n- \"Capacity-dependent limitation\" 结论单薄。\n\n**W6. MATH p=0.079 underpowered [Consensus]**\n- Post-hoc power 估计 ~42%。Non-significance 可能纯粹因为 insufficient N。\n- 应报告 power analysis 或 TOST equivalence test。\n\n**W7. Llama replication (N=70, 0 internal-preferred) 不足 [Consensus]**\n- 零 minority-class observations → 只能说 \"death-rate asymmetry direction generalizes\"，不能说 \"framework generalizes\"。\n\n**W8. Bootstrap CI 在结构耦合下 overconfident [Consensus]**\n- CI [0.952, 0.995] 度量 sampling variance，不度量 external validity（换一组 task types 是否成立）。\n\n**W9. Over-generalization: Abstract/Conclusion qualifier 不够突出 [R2 raised, R1 partially agrees]**\n- \"In environments with catastrophic failure modes\" qualifier 存在但可能在快速阅读中被遗漏。\n\n**W10. \"Internal modality\" 混淆 hallucination 与 reasoning [Consensus]**\n- 如果 \"internal + observation verification\" 降低 death rate 至 ~16%，DAF 会 collapse。\n- 真正 bottleneck 可能是 observation accuracy 而非 computation mode——缺 verification ablation。\n\n### Nice-to-Fix (Info)\n\n**W11.** 术语不一致：modality/strategy/computation type 混用。\n**W12.** 78.9%（label-level）与 90.4%（score-level）并列时语义不清。\n**W13.** SCI=0.2147 缺 null distribution baseline。\n\n---\n\n## Reviewer Consensus\n\n两位 Reviewer 在以下关键判断上完全一致 [AGREE]：\n1. DAF headline framing 存在 penalty-parameter 机械放大问题\n2. r=0.97 大部分是结构性耦合的数学必然\n3. Cross-env evidence 是 absence-of-evidence 而非 positive validation\n4. Data scaling augmentation 不能替代 real-data scaling\n5. 方法论框架本身（Algorithm 1 + DAF + counterfactual labeling）是 solid 的\n6. Negative result（router fails）有 community value\n7. 统计报告和 robustness checks 质量高\n8. 论文处于 Findings track / borderline 水平\n\n---\n\n## Reviewer Divergence\n\n| 问题 | R1 | R2 | Director 判定 |\n|------|----|----|--------------|\n| \"Routing reduces to safety-first selection\" 是否 overclaim | 部分反驳——论文有 qualifier | Critical overclaim | **Warning**：qualifier 存在但不够突出 |\n| \"Obvious observation\" 低估贡献 | 反驳——framework+量化+negative result 三层贡献 | 核心 insight 可能不够 surprising | 采纳 R1：量化精度和诊断框架是非 trivial 贡献 |\n| Figure/Table 信息密度 | 反驳——8页限制下正常做法 | 提出改进建议 | Minor，不影响接收 |\n| EMNLP audience fit | 反驳——*CL 有先例 | 存在张力但不 disqualifying | 不构成问题 |\n| 63% tasks excluded | — | 部分反驳——有 anti-cherry-picking 证据 | 排除有方法论正当性，但 generalization 担忧成立 |\n\n---\n\n## Questions（需作者回应）\n\n**Q1.** Partial correlation (控制 δ·P 后) 的 residual r 是多少？如果 ≈ 0，r=0.97 应如何重新定位？\n\n**Q2.** 如果 \"internal + observation verification\"（每步后 call environment 确认 state），预计 death rate 降到多少？这是否使 DAF 大幅下降？\n\n**Q3.** 能否在 NetHack/Crafter 等有 catastrophic failure 的第二环境复现 DAF？\n\n**Q4.** MATH 实验 post-hoc power 是多少？是否 sufficient to detect effect < 5pp？\n\n**Q5.** P=100 在 ScienceWorld score range (0-100 normalized) 中处于什么位置？这对 DAF 的 external validity 意味着什么？\n\n**Q6.** 1.7B vs 0.6B 的非单调结果（47.1% < 50.67%）是否由配置差异（8 seeds vs 4 seeds）解释？\n\n---\n\n## Missing References\n\n- **Lakens 2017** — Equivalence testing (TOST) for non-significant results\n- **Cohen 1988 / Brysbaert & Stevens 2018** — Power analysis reporting standards\n- **AgentBench** (Liu et al., 2023) — Multi-environment LLM agent benchmark\n- **WebArena** (Zhou et al., 2024) — Interactive web environment with failure modes\n- **LATS** (Zhou et al., 2023) — Language Agent Tree Search\n- **Safe RLHF** (Dai et al., 2024) — Catastrophic failure in safety alignment\n- **ToolBench** (Qin et al., 2023) — Tool use benchmark with failure modes\n- **MINT** (Wang et al., 2024) — Multi-turn interactive evaluation\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求（项目配置中未检测到 `external_review.paperreview_ai.enabled: true`）。\n\n---\n\n## Overall Assessment\n\n**评分**: borderline (3.0/5)\n**置信度**: 4/5\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3.5 | 3.5 | 3.5 |\n| Excitement | 3.0 | 3.0 | 3.0 |\n| Reproducibility | 4.0 | 4.5 | 4.25 |\n| Overall | 3.0 | 3.0 | **3.0** |\n\n**综合判断**：方法论框架设计 solid（Algorithm 1 + DAF 指标简洁可复现），统计报告诚实严谨（robustness checks 充分），negative result 对社区有建设性。但存在 4 个 Critical 问题：(1) 核心 quantitative claim 的 magnitude 由 environment parameter 控制而非 empirical discovery；(2) r=0.97 的独立经验证据性被高估；(3) \"cross-context validation\" 本质是 absence-of-evidence；(4) data scaling ablation 无法区分 signal absence 和 method limitation。这些共同削弱了论文的 informativeness 和 generalizability。\n\n**可接收路径**：修复 W1-W4 的 framing/claim 问题（无需新实验，纯 writing），将论文定位为 \"single-environment case study + diagnostic framework proposal\"，降低泛化声称，r=0.97 和 DAF 给予正确数学定性。如此可达 weak accept 水平。如果能补充第二个 death-penalty 环境数据，可进一步提升至 accept。\n\n---\n\n## Detailed Comments\n\n### Abstract\n- \"DAF = 90.4%\" 应降级，以 \"78.9% of non-tie routing labels are driven by death asymmetry (penalty-independent)\" 为 lead\n- \"partly structural\" → \"largely a mathematical consequence\" 或更长 explanation\n- 最后一句 \"routing problem reduces to safety-first modality selection\" 需加 \"in environments with catastrophic failure modes\" qualifier（当前版本已有 \"in environments with catastrophic failure modes\" 但结构上不够突出）\n\n### §3.4 (DAF Definition)\n- 明确：DAF 的 informativeness 在于 **给定环境 penalty 设定下** 的 routing signal 构成，而非跨环境 universal law\n- 考虑添加 \"DAF should be interpreted relative to the environment's penalty magnitude\" 的显式 caveat\n\n### §4.1 (Death Decomposition)\n- r=0.97 需要更强的结构性耦合说明：当 Var(P·Δ_d) ≫ Var(Δ_nd) 时 high correlation 是 mathematical given，而论文数据恰好满足此条件\n- §4.1 当前 3-sentence caveat 是 R8 修改的结果——但 Abstract/Conclusion 未同步到位\n\n### §4.3 (Router Diagnostic)\n- Data scaling 结论需弱化：明确区分 \"step-level scarcity (ruled out)\" vs \"episode-level minority-class diversity (open question requiring ~1,350 real pairs)\"\n- Capacity scaling 非单调性需 acknowledge——当前 Table 8 caption 有 caveat 但正文表述过于 confident\n\n### §5 (Discussion)\n- \"Cross-environment evidence\" 段：MATH 从 \"validation\" 重新定性为 \"consistent with framework prediction (no death → no death signal)\"\n- Framework applicability 段的 qualifier 应 propagate 到 Abstract 和 Conclusion\n\n### Contribution 3\n- \"Cross-context validation\" → \"Cross-context applicability demonstration\"\n- 当前 evidence 支持 \"framework correctly identifies different mechanisms in different environments\"，不支持 \"DAF quantification generalizes\"",
  "project": "simgate-modular-routing",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "borderline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Round 9 审稿报告 — simgate-modular-routing\n\n**论文**: \"Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\"\n**Venue**: EMNLP 2026 Main Conference Long Paper (ARR May cycle)\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计; R2: 新颖性+完整性）\n**流程**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮即达共识）\n\n---\n\n## Summary\n\n本文提出 episode-level counterfactual analysis 框架和 Death Avoidance Factor (DAF) 指标，分解 modular LLM agent 的 routing signal 来源。在 ScienceWorld（11/30 task types, N=245, Qwen2.5-7B-Instruct）上发现 78.9% 的 non-tie routing labels 由 death asymmetry 驱动，DAF=90.4%（P=100）。Trained router 在 held-out episodes 上低于 chance baseline（47.1% vs 50%）。跨环境分析（MATH N=300, ALFWorld N=135）和跨模型复制（Llama-3.1-8B, N=70）提供辅助证据。\n\n---\n\n## Strengths\n\n**S1. 问题定位精准。** 在 routing 文献集中于\"如何 route\"时，退后一步问\"什么驱动 routing signal\"——是被忽视的元问题，具有方法论价值。\n\n**S2. 框架设计简洁可复现。** Algorithm 1 完备无歧义，仅需 paired episode outcomes，environment-agnostic 属性通过三个结构迥异环境得到演示。\n\n**S3. 统计报告诚实严谨。** p=0.079 始终标注 \"not reaching α=0.05\"，r=0.97 标注 \"partly structural\"，Bootstrap/LOO/Spearman 三重 robustness，8-seed cross-split evaluation。\n\n**S4. 多层次 robustness 检验。** LOO (r: 0.963-0.980), Spearman ρ=0.986, 10K bootstrap, penalty sweep (P=10-500), reasoning-depth ablation, data scaling (25%-800%), capacity scaling (0.6B-4B), cross-model replication。\n\n**S5. Negative result 呈现诚实且有建设性。** Router diagnostic 清晰展示 always-deterministic 的 trivial near-optimality，对社区有建设性信息。\n\n**S6. Limitations 坦诚具体。** 19/30 exclusion, penalty amplification, single-pass ReAct, distribution shift (DAgger), 7-8B scale limitation 均明确列出。\n\n---\n\n## Weaknesses\n\n### Must-Fix (Critical)\n\n**W1. DAF=90.4% headline number 被 penalty magnitude 机械放大 [Consensus]**\n- DAF = δP/(δP + Δ_nd) 是 P 的单调递增函数。在 P=100 时 90.4% 接近同义反复（\"当 penalty 是 score gap 的 35 倍时，penalty 项主导总 gap\"）。P=10 时仅 50.4%。\n- 78.9% penalty-independent metric 更稳健但仍处于从属位置。\n- 论文自承 \"mathematical consequence, not empirical finding\"（§3.4），但 Abstract/Conclusion 的 framing 仍以 DAF 为核心卖点。\n- **要求**：将 78.9% death-asymmetry label fraction 提升为 PRIMARY quantitative claim；或论证 P=100 具有外部效度（typical catastrophic penalty magnitude across environments）。\n\n**W2. r=0.97 结构性耦合呈现不足 [Consensus]**\n- 当 DAF=90.4%（即 Δ_full ≈ δ·P），Corr(δ, δ·P + ε) → 1 是代数必然。\n- Abstract 标 \"partly structural\" 不够——应为 \"largely a mathematical consequence of death dominance\"。Conclusion 完全未提及。\n- Partial correlation（控制 δ·P）预计 r ≈ 0，证实这不是独立经验证据。\n- **要求**：Conclusion 加强 qualifier；或将 r=0.97 从 Contribution-level claim 降级为 robustness diagnostic。\n\n**W3. Cross-env \"validation\" 近循环 [Consensus]**\n- MATH（无 death → 无 death signal）是 absence-of-evidence，不是 positive replication。ALFWorld 识别不同 mechanism 但不验证 DAF 量化能力。\n- 真正的 validation 需要第二个有 catastrophic failure 的环境（如 NetHack/Crafter）重现 similar DAF。\n- Contribution 3 标为 \"cross-context validation\" 属 overselling。\n- **要求**：重新定性为 \"framework applicability demonstration\"；或补充第二个 death-penalty 环境数据。\n\n**W4. Data scaling ablation 用 augmentation 代替真实数据 [Consensus]**\n- Paraphrase augmentation 不等比例放大 majority class（89.6%→97.7%），不创造新 routing patterns。\n- 无法区分 \"signal 不存在\" 和 \"augmentation 无法创造 signal\"。论文自估需 ~1,350 真实 pairs 但未执行。\n- **要求**：弱化为 \"augmentation-based scaling provides no improvement; real-data scaling (requiring ~1,350 episode pairs for 50 minority-class examples) remains open\"。\n\n### Should-Fix (Warning)\n\n**W5. Capacity scaling: 3 个不可比数据点 [Consensus]**\n- 0.6B=50.67%, 1.7B=47.1%, 4B=58.96%——非单调。1.7B 用 8 seeds vs 4 seeds for others。仅 4B 一个点超越 baseline。\n- \"Capacity-dependent limitation\" 结论单薄。\n\n**W6. MATH p=0.079 underpowered [Consensus]**\n- Post-hoc power 估计 ~42%。Non-significance 可能纯粹因为 insufficient N。\n- 应报告 power analysis 或 TOST equivalence test。\n\n**W7. Llama replication (N=70, 0 internal-preferred) 不足 [Consensus]**\n- 零 minority-class observations → 只能说 \"death-rate asymmetry direction generalizes\"，不能说 \"framework generalizes\"。\n\n**W8. Bootstrap CI 在结构耦合下 overconfident [Consensus]**\n- CI [0.952, 0.995] 度量 sampling variance，不度量 external validity（换一组 task types 是否成立）。\n\n**W9. Over-generalization: Abstract/Conclusion qualifier 不够突出 [R2 raised, R1 partially agrees]**\n- \"In environments with catastrophic failure modes\" qualifier 存在但可能在快速阅读中被遗漏。\n\n**W10. \"Internal modality\" 混淆 hallucination 与 reasoning [Consensus]**\n- 如果 \"internal + observation verification\" 降低 death rate 至 ~16%，DAF 会 collapse。\n- 真正 bottleneck 可能是 observation accuracy 而非 computation mode——缺 verification ablation。\n\n### Nice-to-Fix (Info)\n\n**W11.** 术语不一致：modality/strategy/computation type 混用。\n**W12.** 78.9%（label-level）与 90.4%（score-level）并列时语义不清。\n**W13.** SCI=0.2147 缺 null distribution baseline。\n\n---\n\n## Reviewer Consensus\n\n两位 Reviewer 在以下关键判断上完全一致 [AGREE]：\n1. DAF headline framing 存在 penalty-parameter 机械放大问题\n2. r=0.97 大部分是结构性耦合的数学必然\n3. Cross-env evidence 是 absence-of-evidence 而非 positive validation\n4. Data scaling augmentation 不能替代 real-data scaling\n5. 方法论框架本身（Algorithm 1 + DAF + counterfactual labeling）是 solid 的\n6. Negative result（router fails）有 community value\n7. 统计报告和 robustness checks 质量高\n8. 论文处于 Findings track / borderline 水平\n\n---\n\n## Reviewer Divergence\n\n| 问题 | R1 | R2 | Director 判定 |\n|------|----|----|--------------|\n| \"Routing reduces to safety-first selection\" 是否 overclaim | 部分反驳——论文有 qualifier | Critical overclaim | **Warning**：qualifier 存在但不够突出 |\n| \"Obvious observation\" 低估贡献 | 反驳——framework+量化+negative result 三层贡献 | 核心 insight 可能不够 surprising | 采纳 R1：量化精度和诊断框架是非 trivial 贡献 |\n| Figure/Table 信息密度 | 反驳——8页限制下正常做法 | 提出改进建议 | Minor，不影响接收 |\n| EMNLP audience fit | 反驳——*CL 有先例 | 存在张力但不 disqualifying | 不构成问题 |\n| 63% tasks excluded | — | 部分反驳——有 anti-cherry-picking 证据 | 排除有方法论正当性，但 generalization 担忧成立 |\n\n---\n\n## Questions（需作者回应）\n\n**Q1.** Partial correlation (控制 δ·P 后) 的 residual r 是多少？如果 ≈ 0，r=0.97 应如何重新定位？\n\n**Q2.** 如果 \"internal + observation verification\"（每步后 call environment 确认 state），预计 death rate 降到多少？这是否使 DAF 大幅下降？\n\n**Q3.** 能否在 NetHack/Crafter 等有 catastrophic failure 的第二环境复现 DAF？\n\n**Q4.** MATH 实验 post-hoc power 是多少？是否 sufficient to detect effect < 5pp？\n\n**Q5.** P=100 在 ScienceWorld score range (0-100 normalized) 中处于什么位置？这对 DAF 的 external validity 意味着什么？\n\n**Q6.** 1.7B vs 0.6B 的非单调结果（47.1% < 50.67%）是否由配置差异（8 seeds vs 4 seeds）解释？\n\n---\n\n## Missing References\n\n- **Lakens 2017** — Equivalence testing (TOST) for non-significant results\n- **Cohen 1988 / Brysbaert & Stevens 2018** — Power analysis reporting standards\n- **AgentBench** (Liu et al., 2023) — Multi-environment LLM agent benchmark\n- **WebArena** (Zhou et al., 2024) — Interactive web environment with failure modes\n- **LATS** (Zhou et al., 2023) — Language Agent Tree Search\n- **Safe RLHF** (Dai et al., 2024) — Catastrophic failure in safety alignment\n- **ToolBench** (Qin et al., 2023) — Tool use benchmark with failure modes\n- **MINT** (Wang et al., 2024) — Multi-turn interactive evaluation\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求（项目配置中未检测到 `external_review.paperreview_ai.enabled: true`）。\n\n---\n\n## Overall Assessment\n\n**评分**: borderline (3.0/5)\n**置信度**: 4/5\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3.5 | 3.5 | 3.5 |\n| Excitement | 3.0 | 3.0 | 3.0 |\n| Reproducibility | 4.0 | 4.5 | 4.25 |\n| Overall | 3.0 | 3.0 | **3.0** |\n\n**综合判断**：方法论框架设计 solid（Algorithm 1 + DAF 指标简洁可复现），统计报告诚实严谨（robustness checks 充分），negative result 对社区有建设性。但存在 4 个 Critical 问题：(1) 核心 quantitative claim 的 magnitude 由 environment parameter 控制而非 empirical discovery；(2) r=0.97 的独立经验证据性被高估；(3) \"cross-context validation\" 本质是 absence-of-evidence；(4) data scaling ablation 无法区分 signal absence 和 method limitation。这些共同削弱了论文的 informativeness 和 generalizability。\n\n**可接收路径**：修复 W1-W4 的 framing/claim 问题（无需新实验，纯 writing），将论文定位为 \"single-environment case study + diagnostic framework proposal\"，降低泛化声称，r=0.97 和 DAF 给予正确数学定性。如此可达 weak accept 水平。如果能补充第二个 death-penalty 环境数据，可进一步提升至 accept。\n\n---\n\n## Detailed Comments\n\n### Abstract\n- \"DAF = 90.4%\" 应降级，以 \"78.9% of non-tie routing labels are driven by death asymmetry (penalty-independent)\" 为 lead\n- \"partly structural\" → \"largely a mathematical consequence\" 或更长 explanation\n- 最后一句 \"routing problem reduces to safety-first modality selection\" 需加 \"in environments with catastrophic failure modes\" qualifier（当前版本已有 \"in environments with catastrophic failure modes\" 但结构上不够突出）\n\n### §3.4 (DAF Definition)\n- 明确：DAF 的 informativeness 在于 **给定环境 penalty 设定下** 的 routing signal 构成，而非跨环境 universal law\n- 考虑添加 \"DAF should be interpreted relative to the environment's penalty magnitude\" 的显式 caveat\n\n### §4.1 (Death Decomposition)\n- r=0.97 需要更强的结构性耦合说明：当 Var(P·Δ_d) ≫ Var(Δ_nd) 时 high correlation 是 mathematical given，而论文数据恰好满足此条件\n- §4.1 当前 3-sentence caveat 是 R8 修改的结果——但 Abstract/Conclusion 未同步到位\n\n### §4.3 (Router Diagnostic)\n- Data scaling 结论需弱化：明确区分 \"step-level scarcity (ruled out)\" vs \"episode-level minority-class diversity (open question requiring ~1,350 real pairs)\"\n- Capacity scaling 非单调性需 acknowledge——当前 Table 8 caption 有 caveat 但正文表述过于 confident\n\n### §5 (Discussion)\n- \"Cross-environment evidence\" 段：MATH 从 \"validation\" 重新定性为 \"consistent with framework prediction (no death → no death signal)\"\n- Framework applicability 段的 qualifier 应 propagate 到 Abstract 和 Conclusion\n\n### Contribution 3\n- \"Cross-context validation\" → \"Cross-context applicability demonstration\"\n- 当前 evidence 支持 \"framework correctly identifies different mechanisms in different environments\"，不支持 \"DAF quantification generalizes\"",
    "project": "simgate-modular-routing",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "borderline"
  }
}
```

</details>

---


### Tool result

_source line 713 · 2026-05-16T19:18:21.923547+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_f6bffc7e8351600df8091f08a63cd5a0:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 3815
}
```

</details>

---


### Assistant

_source line 714 · 2026-05-16T19:18:28.340596+00:00_

---

**Round 9 审稿完成。**

报告已投递至 Research Director。核心结论：

- **评分**: borderline (3.0/5)
- **Critical 问题 (4)**：DAF 被 penalty 机械放大、r=0.97 结构耦合呈现不足、cross-env "validation" 近循环、data scaling 用 augmentation 不可靠
- **可接收路径**：修复 framing/claim（无需新实验），将论文定位为 single-environment case study + framework proposal，降低泛化声称。如补充第二个 death-penalty 环境可进一步提升。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director"
}
```

</details>

---


## Round 71

## Round 71

60 recorded events


### User

_source line 715 · 2026-05-16T19:38:45.875290+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: simgate-modular-routing
- 论文路径: projects/simgate-modular-routing/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Main Conference Long Paper
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 716 · 2026-05-16T19:38:53.188731+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 717 · 2026-05-16T19:38:53.290362+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 2458 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 718 · 2026-05-16T19:39:00.114274+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,WebSearch",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,WebSearch",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 719 · 2026-05-16T19:39:00.164841+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 720 · 2026-05-16T19:39:04.441026+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,request_external_review,director_post_to_reviewer",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,request_external_review,director_post_to_reviewer",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 721 · 2026-05-16T19:39:04.441387+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 722 · 2026-05-16T19:39:07.955118+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_post_to_reviewer",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_post_to_reviewer",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 723 · 2026-05-16T19:39:08.005675+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 724 · 2026-05-16T19:39:11.592519+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "simgate-modular-routing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "simgate-modular-routing"
  }
}
```

</details>

---


### Tool result

_source line 725 · 2026-05-16T19:39:13.011603+00:00_

{"result":"# 项目 simgate-modular-routing 概况\n\n## 实验状态 (92 个)\n\n- **plan-001b-gpu1-extra**: DONE (failed) — \n- **plan-001b-gpu1**: DONE (success) — \n- **plan-001b-gpu0-v2**: DONE (failed) — \n- **plan-011-rule-based**: DONE (success) — \n- **plan-001b-gpu0**: DONE (failed) — \n- **research-prescreening-gpu0**: DONE (killed) — \n- **research-prescreening-gpu1**: DONE (success) — \n- **research-boil-v3-gpu1**: DONE (success) — \n- **mvp-p1-gpu1-v3**: DONE (success) — \n- **mvp-p1-gpu0-vllm**: DONE (success) — \n- **mvp-p1-gpu0**: DONE (killed) — \n- **mvp-p1-gpu1-v2**: DONE (killed) — \n- **mvp-p1-gpu1-vllm**: DONE (killed) — \n- **mvp-p1-gpu1**: DONE (killed) — \n- **mvp-p0-forking**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-16\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n（无）\n\n## 近期结论\n- **daf-bootstrap-ci-full** (success): Full 245-episode bootstrap (10000 resamples) validates DAF point estimate ≈ 0.90 with tight 95% CI. Per-task DAF provides granular decomposition.\n- **sci-concentration-index** (success): Signal Concentration Index (SCI) quantifies how concentrated routing signal is across task types. Expected SCI ≈ 1.0 (death avoidance dominates, signal highly concentrated in few tasks).\n- **cross-model-guided-router-eval** (negative): Qwen-derived death risk labels transfer to Llama: applying Qwen task-type routing rule on Llama episodes yields balanced_acc > 50%, validating cross-model transferability of the routing signal.\n  [cross-model-guided-router-eval-results](/api/workspace-files/projects/simgate-modular-routing/artifacts/cross-model-guided-router-eval/data/cross_model_results.json)\n\n## 趋势\n成功 38 / 负向 22 / 失败 14 / 共 92\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestb-13313: 无 GPU 信息\n\n## 告警\n- gpu0-v6-lifespan: 已被终止 — unknown\n- llama-cross-model-expanded: 已被终止 — unknown\n- math-200-fixed: 训练失败 — unknown\n- mvp-p1-gpu0: 已被终止 — unknown\n- mvp-p1-gpu1: 已被终止 — unknown\n- mvp-p1-gpu1-v2: 已被终止 — unknown\n- mvp-p1-g
…[truncated 1034 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_0b622d6038b969b96148ee8a163a1a0c:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1419
}
```

</details>

---
