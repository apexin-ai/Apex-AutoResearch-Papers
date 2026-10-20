# paper fix fig1 caption panel c

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 14
- **Recorded user turns:** 0
- **Tool calls:** 3
- **Original source:** `logs/workers/worker_paper_fix_fig1-caption-panel-c_20260526T151150.log`
- **Structured JSON:** [`7c12b32b90e39109d806.json`](../../sessions/7c/7c12b32b90e39109d806.json)

## Before a recorded user message

14 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla",
  "session_id": "0a2ad9c4-1f39-4180-8861-f3efff698425",
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
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__save_project_file"
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
  "uuid": "a2bcd7bc-3897-43bd-acf3-03ad803c982d",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-6/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-projects-occsafe-vla/memory/"
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
    "resetsAt": 1779809400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "c2096566-ddbf-4518-90fd-b2c8ea6c8ab4",
  "session_id": "0a2ad9c4-1f39-4180-8861-f3efff698425"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me search for the Fig 1 caption in the specified files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a2ad9c4-1f39-4180-8861-f3efff698425",
  "uuid": "33ce3a27-d173-4c1a-a89a-2907e136ba98",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RwoXCNRtq48L8wDF9UTCxf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11468,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11468
      },
      "output_tokens": 39,
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

<details open><summary>🔧 Tool call — Grep · `toolu_01466K73DYbCqfUvhFdvnAEZ`</summary>

```json
{
  "pattern": "fig.*overview|fig1|\\\\begin\\{figure\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper",
  "output_mode": "content",
  "-i": true,
  "-C": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a2ad9c4-1f39-4180-8861-f3efff698425",
  "uuid": "0735863e-375f-4a1f-9dd6-073ee8ab56a6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RwoXCNRtq48L8wDF9UTCxf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11468,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11468
      },
      "output_tokens": 39,
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

_source line 6 · 2026-05-26T15:12:04.857Z_

<details><summary>↩ Tool result · `toolu_01466K73DYbCqfUvhFdvnAEZ`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/main.fls-197-INPUT /usr/share/texlive/texmf-dist/fonts/vf/adobe/times/ptmr7t.vf
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/main.fls-198-INPUT /usr/share/texlive/texmf-dist/fonts/tfm/adobe/times/ptmr8r.tfm
docs/paper/main.fls:199:INPUT ./figures/fig1_overview.pdf
docs/paper/main.fls:200:INPUT ./figures/fig1_overview.pdf
docs/paper/main.fls:201:INPUT ./figures/fig1_overview.pdf
docs/paper/main.fls:202:INPUT ./figures/fig1_overview.pdf
docs/paper/main.fls:203:INPUT ./figures/fig1_overview.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/main.fls-204-INPUT ./related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/main.fls-205-INPUT ./related_work.tex
--
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/main.fdb_latexmk-131-  "figures/dose_response.pdf" 1779699034.66102 35275 5103cea87c868313b4e2f3e00984cd0c ""
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/main.fdb_latexmk-132-  "figures/factorial_2x2.pdf" 1779699032.13108 24546 2d6f521576c56471687ff44808a9e0b1 ""
docs/paper/main.fdb_latexmk:133:  "figures/fig1_overview.pdf" 1779702623.71006 76835 87e543f6253ba808476f183c46834bcd ""
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/main.fdb_latexmk-134-  "figures/gradient_analysis_combined.pdf" 1779562564.09097 37209 cfdb04dc5ca67edbf57c9a7795ac23e4 ""
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/main.fdb_latexmk-135-  "figures/per_layer_combined.pdf" 1779637063.93193 47712 23a37c02be2aa3f06b06c6401714a2e6 ""
--
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/main.log-535-{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-di
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/main.log-536-st/fonts/enc/dvips/base/8r.enc}]
docs/paper/main.log:537:&lt;figures/fig1_overview.pdf, id=109, 1021.64056pt x 322.61327pt>
docs/paper/main.log:538:File: figures/fig1_overview.pdf Graphic file (type pdf)
docs/paper/main.log:539:&lt;use figures/fig1_overview.pdf>
docs/paper/main.log:540:Package pdftex.def Info: figures/fig1_overview.pdf  used on input line 12.
docs/paper/main.log-541-(pdftex.def)             Requested size: 397.48499pt x 125.51837pt.
docs/paper/main.log:542:) (./related_work.tex [2 <./figures/fig1_overview.pdf>]) (./method.tex [3]
docs/paper/main.log-543-LaTeX Font Info:    Trying to load font information for TS1+ptm on input line 2
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/main.log-544-2.
--
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex-81-[Omitted long context line]
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex-82-
docs/paper/appendix.tex:83:\begin{figure}[h]
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex-84-\centering
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex-85-\includegraphics[width=\textwidth]{figures/per_layer_combined.pdf}
--
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex-93-[Omitted long context line]
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex-94-
docs/paper/appendix.tex:95:\begin{figure}[h]
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex-96-\centering
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex-97-\includegraphics[width=0.75\textwidth]{figures/dose_response.pdf}
--
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/introduction.tex-7-\begin{figure*}[t]
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/introduction.tex-8-\centering
docs/paper/introduction.tex:9:\includegraphics[width=\textwidth]{figures/fig1_overview.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/introduction.tex-10-[Omitted long context line]
docs/paper/introduction.tex:11:\label{fig:overview}
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/introduction.tex-12-\end{figure*}
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/introduction.tex-13-
docs/paper/introduction.tex:14:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/introduction.tex-15-
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/introduction.tex-16-[Omitted long context line]
--
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/main.aux-16-\citation{raja2024ogmcbf}
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/main.aux-17-\citation{zhang2025safevla}
docs/paper/main.aux:18:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/main.aux-19-\providecommand*\caption@xref[2]{\@setref\relax\@undefined{#1}}
docs/paper/main.aux:20:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/main.aux-21-\@writefile{toc}{\contentsline {section}{\numberline {2}Related Work}{2}{section.2}\protected@file@percent }
docs/paper/main.aux-22-\newlabel{sec:related}{{2}{2}{Related Work}{section.2}{}}
--
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex-66-\end{table}
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex-67-
docs/paper/results.tex:68:\begin{figure}[t]
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex-69-\centering
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex-70-\includegraphics[width=0.65\textwidth]{figures/factorial_2x2.pdf}
--
docs/paper/results.tex-76-\label{sec:gradient_dynamics}
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex-77-
docs/paper/results.tex:78:\begin{figure}[t]
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex-79-\centering
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex-80-\includegraphics[width=\textwidth]{figures/gradient_analysis_combined.pdf}
--
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/figures/fig1_overview.py-1-"""
docs/paper/figures/fig1_overview.py:2:fig1_overview.py — Hero figure for CoRL 2026 paper (Plan B framing).
docs/paper/figures/fig1_overview.py-3-Three-panel overview: (a) Training setup, (b) Factorial design, (c) Key result.
docs/paper/figures/fig1_overview.py-4-Narrative: "Auxiliary spatial supervision does not improve VLA collision avoidance."
--
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/figures/fig1_overview.py-302-# Save
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/figures/fig1_overview.py-303-out_dir = '/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/figures'
docs/paper/figures/fig1_overview.py:304:fig.savefig(f'{out_dir}/fig1_overview.png', dpi=300, bbox_inches='tight',
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/figures/fig1_overview.py-305-            pad_inches=0.05, facecolor='white')
docs/paper/figures/fig1_overview.py:306:fig.savefig(f'{out_dir}/fig1_overview.pdf', dpi=300, bbox_inches='tight',
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/figures/fig1_overview.py-307-            pad_inches=0.05, facecolor='white')
/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/figures/fig1_overview.py-308-plt.close()
docs/paper/figures/fig1_overview.py:309:print("Saved fig1_overview.png and fig1_overview.pdf")
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0a2ad9c4-1f39-4180-8861-f3efff698425",
  "uuid": "f2145831-cf4e-473d-a6b6-861251d7e8c0",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/main.fls-197-INPUT /usr/share/texlive/texmf-dist/fonts/vf/adobe/times/ptmr7t.vf\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/main.fls-198-INPUT /usr/share/texlive/texmf-dist/fonts/tfm/adobe/times/ptmr8r.tfm\ndocs/paper/main.fls:199:INPUT ./figures/fig1_overview.pdf\ndocs/paper/main.fls:200:INPUT ./figures/fig1_overview.pdf\ndocs/paper/main.fls:201:INPUT ./figures/fig1_overview.pdf\ndocs/paper/main.fls:202:INPUT ./figures/fig1_overview.pdf\ndocs/paper/main.fls:203:INPUT ./figures/fig1_overview.pdf\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/main.fls-204-INPUT ./related_work.tex\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/main.fls-205-INPUT ./related_work.tex\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/main.fdb_latexmk-131-  \"figures/dose_response.pdf\" 1779699034.66102 35275 5103cea87c868313b4e2f3e00984cd0c \"\"\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/main.fdb_latexmk-132-  \"figures/factorial_2x2.pdf\" 1779699032.13108 24546 2d6f521576c56471687ff44808a9e0b1 \"\"\ndocs/paper/main.fdb_latexmk:133:  \"figures/fig1_overview.pdf\" 1779702623.71006 76835 87e543f6253ba808476f183c46834bcd \"\"\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/main.fdb_latexmk-134-  \"figures/gradient_analysis_combined.pdf\" 1779562564.09097 37209 cfdb04dc5ca67edbf57c9a7795ac23e4 \"\"\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/main.fdb_latexmk-135-  \"figures/per_layer_combined.pdf\" 1779637063.93193 47712 23a37c02be2aa3f06b06c6401714a2e6 \"\"\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/main.log-535-{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}{/usr/share/texlive/texmf-di\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/main.log-536-st/fonts/enc/dvips/base/8r.enc}]\ndocs/paper/main.log:537:&lt;figures/fig1_overview.pdf, id=109, 1021.64056pt x 322.61327pt>\ndocs/paper/main.log:538:File: figures/fig1_overview.pdf Graphic file (type pdf)\ndocs/paper/main.log:539:&lt;use figures/fig1_overview.pdf>\ndocs/paper/main.log:540:Package pdftex.def Info: figures/fig1_overview.pdf  used on input line 12.\ndocs/paper/main.log-541-(pdftex.def)             Requested size: 397.48499pt x 125.51837pt.\ndocs/paper/main.log:542:) (./related_work.tex [2 <./figures/fig1_overview.pdf>]) (./method.tex [3]\ndocs/paper/main.log-543-LaTeX Font Info:    Trying to load font information for TS1+ptm on input line 2\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/main.log-544-2.\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex-81-[Omitted long context line]\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex-82-\ndocs/paper/appendix.tex:83:\\begin{figure}[h]\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex-84-\\centering\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex-85-\\includegraphics[width=\\textwidth]{figures/per_layer_combined.pdf}\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex-93-[Omitted long context line]\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex-94-\ndocs/paper/appendix.tex:95:\\begin{figure}[h]\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex-96-\\centering\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/appendix.tex-97-\\includegraphics[width=0.75\\textwidth]{figures/dose_response.pdf}\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/introduction.tex-7-\\begin{figure*}[t]\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/introduction.tex-8-\\centering\ndocs/paper/introduction.tex:9:\\includegraphics[width=\\textwidth]{figures/fig1_overview.pdf}\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/introduction.tex-10-[Omitted long context line]\ndocs/paper/introduction.tex:11:\\label{fig:overview}\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/introduction.tex-12-\\end{figure*}\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/introduction.tex-13-\ndocs/paper/introduction.tex:14:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/introduction.tex-15-\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/introduction.tex-16-[Omitted long context line]\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/main.aux-16-\\citation{raja2024ogmcbf}\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/main.aux-17-\\citation{zhang2025safevla}\ndocs/paper/main.aux:18:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/main.aux-19-\\providecommand*\\caption@xref[2]{\\@setref\\relax\\@undefined{#1}}\ndocs/paper/main.aux:20:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/main.aux-21-\\@writefile{toc}{\\contentsline {section}{\\numberline {2}Related Work}{2}{section.2}\\protected@file@percent }\ndocs/paper/main.aux-22-\\newlabel{sec:related}{{2}{2}{Related Work}{section.2}{}}\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex-66-\\end{table}\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex-67-\ndocs/paper/results.tex:68:\\begin{figure}[t]\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex-69-\\centering\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex-70-\\includegraphics[width=0.65\\textwidth]{figures/factorial_2x2.pdf}\n--\ndocs/paper/results.tex-76-\\label{sec:gradient_dynamics}\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex-77-\ndocs/paper/results.tex:78:\\begin{figure}[t]\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex-79-\\centering\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/results.tex-80-\\includegraphics[width=\\textwidth]{figures/gradient_analysis_combined.pdf}\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/figures/fig1_overview.py-1-\"\"\"\ndocs/paper/figures/fig1_overview.py:2:fig1_overview.py — Hero figure for CoRL 2026 paper (Plan B framing).\ndocs/paper/figures/fig1_overview.py-3-Three-panel overview: (a) Training setup, (b) Factorial design, (c) Key result.\ndocs/paper/figures/fig1_overview.py-4-Narrative: \"Auxiliary spatial supervision does not improve VLA collision avoidance.\"\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/figures/fig1_overview.py-302-# Save\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/figures/fig1_overview.py-303-out_dir = '/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/figures'\ndocs/paper/figures/fig1_overview.py:304:fig.savefig(f'{out_dir}/fig1_overview.png', dpi=300, bbox_inches='tight',\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/figures/fig1_overview.py-305-            pad_inches=0.05, facecolor='white')\ndocs/paper/figures/fig1_overview.py:306:fig.savefig(f'{out_dir}/fig1_overview.pdf', dpi=300, bbox_inches='tight',\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/figures/fig1_overview.py-307-            pad_inches=0.05, facecolor='white')\n/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/figures/fig1_overview.py-308-plt.close()\ndocs/paper/figures/fig1_overview.py:309:print(\"Saved fig1_overview.png and fig1_overview.pdf\")",
    "numLines": 83
  }
}
```

</details>

---

### Assistant

_source line 7_

Caption 在 `introduction.tex` 第 10 行。让我读取该文件的相关部分。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a2ad9c4-1f39-4180-8861-f3efff698425",
  "uuid": "1d257d2a-82de-4232-ae38-f4c1c9fc721e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VLBTsNdjFH7n6jiGk4xJS8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3437,
      "cache_read_input_tokens": 23309,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3437
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

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Read · `toolu_01Jzh5JvvuN9ime6tCnyPDpT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/introduction.tex",
  "limit": 15
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a2ad9c4-1f39-4180-8861-f3efff698425",
  "uuid": "294a716c-30f4-40ea-9dc8-46f66f8606b3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VLBTsNdjFH7n6jiGk4xJS8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3437,
      "cache_read_input_tokens": 23309,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3437
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

### Tool result

_source line 9 · 2026-05-26T15:12:08.510Z_

<details><summary>↩ Tool result · `toolu_01Jzh5JvvuN9ime6tCnyPDpT`</summary>

```text
1	\section{Introduction}
2	
3	Vision-language-action (VLA) models map visual observations and language instructions to robot actions, and recent fine-tuning recipes achieve high task success on standard manipulation benchmarks~\cite{brohan2023rt2, kim2024openvla, kim2025oft}. Behavioral safety, however, does not follow from task completion. On SafeLIBERO Level~I~\cite{hu2025vlsa}, OpenVLA-7B fine-tuned with the OFT recipe~\cite{kim2025oft} reaches a Task Success Rate (TSR) of 90.7\% but a Collision Avoidance Rate (CAR) of only 78.0\%. On the three most constrained tasks, collision rates reach 53--93\%. These numbers expose a gap between what training objectives optimize for and what safe deployment requires: the robot completes the task but fails to avoid contact with surrounding objects. Identifying which fine-tuning design choices affect collision avoidance is a prerequisite for closing this gap.
4	
5	Two active research threads address related but distinct aspects of this problem. The first enriches VLA models with auxiliary spatial prediction (occupancy grids, depth maps, point clouds) to inject 3D geometric structure into vision encoders~\cite{li2026spatialforcing, yuan2025depthvla, wu2025spatialvla, liu2025occvla}. At least fifteen such methods have appeared in the past year~\cite{wu2026stvla, chen2026gstvla, tu2026sgvla, xiao2026stemvla, li2025pointvla, sun2025geovla, bhat20253dcavla, li2025qdepthvla, abouzeid2025geoaware, rao2026augvla3d, li2026corridorvla}, all reporting improved task success. The implicit assumption in this literature is that better spatial awareness should also yield safer behavior, since the robot ``knows where things are.'' The second thread targets VLA safety directly through runtime action filtering~\cite{hu2025vlsa, zhai2026cofreevla, raja2024ogmcbf} or constrained reinforcement learning~\cite{zhang2025safevla}. These two lines of work are disconnected: no spatial method evaluates its effect on collision avoidance, and no safety method examines whether spatial representations contribute to or detract from safe behavior. A recent survey~\cite{li2026vlasafety} confirms that the relationship between auxiliary spatial supervision and collision safety remains an open question.
6	
7	\begin{figure*}[t]
8	\centering
9	\includegraphics[width=\textwidth]{figures/fig1_overview.pdf}
10	\caption{\textbf{Auxiliary spatial supervision does not improve VLA collision avoidance.} \textbf{(a)}~A fine-tuned OpenVLA-OFT achieves 90.7\% Task Success Rate but only 78.0\% Collision Avoidance Rate on SafeLIBERO Level~I; per-task collision rates reach 93\% on the most constrained tasks. \textbf{(b)}~Our factorial design varies five factors (gradient flow, label content, normalization type, spatial reference frame, temporal extent) across 12 conditions. An auxiliary spatial head is attached to the vision encoders during training and discarded at inference. \textbf{(c)}~All auxiliary spatial head configurations perform at or below the Vanilla baseline. A $2{\times}2$ factorial (gradient flow $\times$ normalization) reveals an ordinal interaction: gradient flow is detrimental to safety, and BatchNorm amplifies the damage.}
11	\label{fig:overview}
12	\end{figure*}
13	
14	We ask a direct question: does auxiliary spatial supervision during VLA fine-tuning improve collision avoidance? We conduct a systematic factorial study using OpenVLA-7B~\cite{kim2024openvla} with the OFT recipe~\cite{kim2025oft} and LoRA~\cite{hu2022lora} adaptation. Twelve experimental conditions vary five factors: gradient flow from the auxiliary head into the vision encoders, spatial label content, normalization type in the auxiliary head, spatial reference frame, and temporal extent of supervision (Figure~\ref{fig:overview}). This design is deliberate. Single-factor ablations, the dominant methodology in prior spatial VLA studies, cannot detect interactions between design choices. If gradient flow and normalization type interact in their effect on collision avoidance, a study that varies only one factor will attribute the joint effect to whichever factor it happens to test. Our $2{\times}2$ factorial subset (gradient flow $\times$ normalization) is the minimal design that can detect and quantify such interactions.
15	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0a2ad9c4-1f39-4180-8861-f3efff698425",
  "uuid": "89815827-de5b-4a4b-ac78-76a8c9eb55b7",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\nVision-language-action (VLA) models map visual observations and language instructions to robot actions, and recent fine-tuning recipes achieve high task success on standard manipulation benchmarks~\\cite{brohan2023rt2, kim2024openvla, kim2025oft}. Behavioral safety, however, does not follow from task completion. On SafeLIBERO Level~I~\\cite{hu2025vlsa}, OpenVLA-7B fine-tuned with the OFT recipe~\\cite{kim2025oft} reaches a Task Success Rate (TSR) of 90.7\\% but a Collision Avoidance Rate (CAR) of only 78.0\\%. On the three most constrained tasks, collision rates reach 53--93\\%. These numbers expose a gap between what training objectives optimize for and what safe deployment requires: the robot completes the task but fails to avoid contact with surrounding objects. Identifying which fine-tuning design choices affect collision avoidance is a prerequisite for closing this gap.\n\nTwo active research threads address related but distinct aspects of this problem. The first enriches VLA models with auxiliary spatial prediction (occupancy grids, depth maps, point clouds) to inject 3D geometric structure into vision encoders~\\cite{li2026spatialforcing, yuan2025depthvla, wu2025spatialvla, liu2025occvla}. At least fifteen such methods have appeared in the past year~\\cite{wu2026stvla, chen2026gstvla, tu2026sgvla, xiao2026stemvla, li2025pointvla, sun2025geovla, bhat20253dcavla, li2025qdepthvla, abouzeid2025geoaware, rao2026augvla3d, li2026corridorvla}, all reporting improved task success. The implicit assumption in this literature is that better spatial awareness should also yield safer behavior, since the robot ``knows where things are.'' The second thread targets VLA safety directly through runtime action filtering~\\cite{hu2025vlsa, zhai2026cofreevla, raja2024ogmcbf} or constrained reinforcement learning~\\cite{zhang2025safevla}. These two lines of work are disconnected: no spatial method evaluates its effect on collision avoidance, and no safety method examines whether spatial representations contribute to or detract from safe behavior. A recent survey~\\cite{li2026vlasafety} confirms that the relationship between auxiliary spatial supervision and collision safety remains an open question.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/fig1_overview.pdf}\n\\caption{\\textbf{Auxiliary spatial supervision does not improve VLA collision avoidance.} \\textbf{(a)}~A fine-tuned OpenVLA-OFT achieves 90.7\\% Task Success Rate but only 78.0\\% Collision Avoidance Rate on SafeLIBERO Level~I; per-task collision rates reach 93\\% on the most constrained tasks. \\textbf{(b)}~Our factorial design varies five factors (gradient flow, label content, normalization type, spatial reference frame, temporal extent) across 12 conditions. An auxiliary spatial head is attached to the vision encoders during training and discarded at inference. \\textbf{(c)}~All auxiliary spatial head configurations perform at or below the Vanilla baseline. A $2{\\times}2$ factorial (gradient flow $\\times$ normalization) reveals an ordinal interaction: gradient flow is detrimental to safety, and BatchNorm amplifies the damage.}\n\\label{fig:overview}\n\\end{figure*}\n\nWe ask a direct question: does auxiliary spatial supervision during VLA fine-tuning improve collision avoidance? We conduct a systematic factorial study using OpenVLA-7B~\\cite{kim2024openvla} with the OFT recipe~\\cite{kim2025oft} and LoRA~\\cite{hu2022lora} adaptation. Twelve experimental conditions vary five factors: gradient flow from the auxiliary head into the vision encoders, spatial label content, normalization type in the auxiliary head, spatial reference frame, and temporal extent of supervision (Figure~\\ref{fig:overview}). This design is deliberate. Single-factor ablations, the dominant methodology in prior spatial VLA studies, cannot detect interactions between design choices. If gradient flow and normalization type interact in their effect on collision avoidance, a study that varies only one factor will attribute the joint effect to whichever factor it happens to test. Our $2{\\times}2$ factorial subset (gradient flow $\\times$ normalization) is the minimal design that can detect and quantify such interactions.\n",
      "numLines": 15,
      "startLine": 1,
      "totalLines": 25
    }
  }
}
```

</details>

---

### Assistant

_source line 10_

找到了。第 10 行的 caption 包含 `\textbf{(c)}` 描述。需要删除从 `\textbf{(c)}` 开始到该句末尾的部分。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a2ad9c4-1f39-4180-8861-f3efff698425",
  "uuid": "9afba8d3-bc63-44b3-ac46-c58a8b4b7949",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011PmfSpEwVRy98MnPmUHNAa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1268,
      "cache_read_input_tokens": 26746,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1268
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

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — Edit · `toolu_01Q6Qbg1yFLU4LNS26Q8ciBc`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/introduction.tex",
  "old_string": " \\textbf{(c)}~All auxiliary spatial head configurations perform at or below the Vanilla baseline. A $2{\\times}2$ factorial (gradient flow $\\times$ normalization) reveals an ordinal interaction: gradient flow is detrimental to safety, and BatchNorm amplifies the damage.}",
  "new_string": "}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a2ad9c4-1f39-4180-8861-f3efff698425",
  "uuid": "eb7d1689-ff80-40a2-8684-7778ce423323",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011PmfSpEwVRy98MnPmUHNAa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1268,
      "cache_read_input_tokens": 26746,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1268
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

### Tool result

_source line 12 · 2026-05-26T15:12:16.509Z_

<details><summary>↩ Tool result · `toolu_01Q6Qbg1yFLU4LNS26Q8ciBc`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0a2ad9c4-1f39-4180-8861-f3efff698425",
  "uuid": "ec9d784e-b3a1-4c26-950b-07a3f8f680dd",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/introduction.tex",
    "oldString": " \\textbf{(c)}~All auxiliary spatial head configurations perform at or below the Vanilla baseline. A $2{\\times}2$ factorial (gradient flow $\\times$ normalization) reveals an ordinal interaction: gradient flow is detrimental to safety, and BatchNorm amplifies the damage.}",
    "newString": "}",
    "originalFile": "\\section{Introduction}\n\nVision-language-action (VLA) models map visual observations and language instructions to robot actions, and recent fine-tuning recipes achieve high task success on standard manipulation benchmarks~\\cite{brohan2023rt2, kim2024openvla, kim2025oft}. Behavioral safety, however, does not follow from task completion. On SafeLIBERO Level~I~\\cite{hu2025vlsa}, OpenVLA-7B fine-tuned with the OFT recipe~\\cite{kim2025oft} reaches a Task Success Rate (TSR) of 90.7\\% but a Collision Avoidance Rate (CAR) of only 78.0\\%. On the three most constrained tasks, collision rates reach 53--93\\%. These numbers expose a gap between what training objectives optimize for and what safe deployment requires: the robot completes the task but fails to avoid contact with surrounding objects. Identifying which fine-tuning design choices affect collision avoidance is a prerequisite for closing this gap.\n\nTwo active research threads address related but distinct aspects of this problem. The first enriches VLA models with auxiliary spatial prediction (occupancy grids, depth maps, point clouds) to inject 3D geometric structure into vision encoders~\\cite{li2026spatialforcing, yuan2025depthvla, wu2025spatialvla, liu2025occvla}. At least fifteen such methods have appeared in the past year~\\cite{wu2026stvla, chen2026gstvla, tu2026sgvla, xiao2026stemvla, li2025pointvla, sun2025geovla, bhat20253dcavla, li2025qdepthvla, abouzeid2025geoaware, rao2026augvla3d, li2026corridorvla}, all reporting improved task success. The implicit assumption in this literature is that better spatial awareness should also yield safer behavior, since the robot ``knows where things are.'' The second thread targets VLA safety directly through runtime action filtering~\\cite{hu2025vlsa, zhai2026cofreevla, raja2024ogmcbf} or constrained reinforcement learning~\\cite{zhang2025safevla}. These two lines of work are disconnected: no spatial method evaluates its effect on collision avoidance, and no safety method examines whether spatial representations contribute to or detract from safe behavior. A recent survey~\\cite{li2026vlasafety} confirms that the relationship between auxiliary spatial supervision and collision safety remains an open question.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/fig1_overview.pdf}\n\\caption{\\textbf{Auxiliary spatial supervision does not improve VLA collision avoidance.} \\textbf{(a)}~A fine-tuned OpenVLA-OFT achieves 90.7\\% Task Success Rate but only 78.0\\% Collision Avoidance Rate on SafeLIBERO Level~I; per-task collision rates reach 93\\% on the most constrained tasks. \\textbf{(b)}~Our factorial design varies five factors (gradient flow, label content, normalization type, spatial reference frame, temporal extent) across 12 conditions. An auxiliary spatial head is attached to the vision encoders during training and discarded at inference. \\textbf{(c)}~All auxiliary spatial head configurations perform at or below the Vanilla baseline. A $2{\\times}2$ factorial (gradient flow $\\times$ normalization) reveals an ordinal interaction: gradient flow is detrimental to safety, and BatchNorm amplifies the damage.}\n\\label{fig:overview}\n\\end{figure*}\n\nWe ask a direct question: does auxiliary spatial supervision during VLA fine-tuning improve collision avoidance? We conduct a systematic factorial study using OpenVLA-7B~\\cite{kim2024openvla} with the OFT recipe~\\cite{kim2025oft} and LoRA~\\cite{hu2022lora} adaptation. Twelve experimental conditions vary five factors: gradient flow from the auxiliary head into the vision encoders, spatial label content, normalization type in the auxiliary head, spatial reference frame, and temporal extent of supervision (Figure~\\ref{fig:overview}). This design is deliberate. Single-factor ablations, the dominant methodology in prior spatial VLA studies, cannot detect interactions between design choices. If gradient flow and normalization type interact in their effect on collision avoidance, a study that varies only one factor will attribute the joint effect to whichever factor it happens to test. Our $2{\\times}2$ factorial subset (gradient flow $\\times$ normalization) is the minimal design that can detect and quantify such interactions.\n\nThe central result is negative: \\textbf{all auxiliary spatial head configurations perform at or below the Vanilla baseline} on Collision Avoidance Rate. Auxiliary spatial supervision does not improve VLA collision avoidance under any of the twelve configurations tested. The $2{\\times}2$ factorial subset (gradient flow $\\times$ normalization) reveals an ordinal interaction between gradient flow and normalization. Gradient flow through the auxiliary head into the vision encoders is detrimental to safety ($\\Delta{=}-4.2$\\,pp within the BatchNorm conditions), and BatchNorm amplifies this damage compared to LayerNorm. The BatchNorm + gradient flow cell (Full OCC) is both the worst-performing and the most unstable configuration, with cross-seed standard deviation of 0.064, nearly three times that of the other factorial cells. Spatial label content does not affect outcomes: Full OCC (ground-truth occupancy), Random OCC (random binary labels), and Depth (egocentric depth maps) all fall within cross-seed variance of each other and of the Vanilla baseline. The spatial information itself, whether structured or random, is irrelevant to safety; the gradient pathway and normalization dynamics determine the outcome.\n\nOur contributions are:\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item \\textbf{Negative core finding.} We show that auxiliary spatial supervision does not improve VLA collision avoidance under any of 12 configurations tested. A $2{\\times}2$ factorial (gradient flow $\\times$ normalization) reveals an ordinal interaction: gradient flow is detrimental to safety, and BatchNorm amplifies the damage and increases training instability. Spatial label content (structured, random, depth) does not affect outcomes (\\S\\ref{sec:results}, Table~\\ref{tab:main_results}, Figure~\\ref{fig:factorial}).\n\n    \\item \\textbf{Factorial methodology for VLA auxiliary heads.} We introduce the first factorial experimental design for analyzing how auxiliary head design choices interact during VLA fine-tuning. This design reveals interactions that single-factor ablations would miss (\\S\\ref{sec:ablation}, Table~\\ref{tab:ablation_design}).\n\n    \\item \\textbf{Actionable guidelines at zero cost.} Do not add auxiliary spatial heads for the purpose of improving collision avoidance. If an auxiliary head is required by other objectives, use detached gradients with LayerNorm (Detach+LN), and never combine BatchNorm with gradient flow. No ground-truth spatial labels are needed; the auxiliary head is discarded at inference (\\S\\ref{sec:discussion}).\n\\end{enumerate}",
    "structuredPatch": [
      {
        "oldStart": 7,
        "oldLines": 7,
        "newStart": 7,
        "newLines": 7,
        "lines": [
          " \\begin{figure*}[t]",
          " \\centering",
          " \\includegraphics[width=\\textwidth]{figures/fig1_overview.pdf}",
          "-\\caption{\\textbf{Auxiliary spatial supervision does not improve VLA collision avoidance.} \\textbf{(a)}~A fine-tuned OpenVLA-OFT achieves 90.7\\% Task Success Rate but only 78.0\\% Collision Avoidance Rate on SafeLIBERO Level~I; per-task collision rates reach 93\\% on the most constrained tasks. \\textbf{(b)}~Our factorial design varies five factors (gradient flow, label content, normalization type, spatial reference frame, temporal extent) across 12 conditions. An auxiliary spatial head is attached to the vision encoders during training and discarded at inference. \\textbf{(c)}~All auxiliary spatial head configurations perform at or below the Vanilla baseline. A $2{\\times}2$ factorial (gradient flow $\\times$ normalization) reveals an ordinal interaction: gradient flow is detrimental to safety, and BatchNorm amplifies the damage.}",
          "+\\caption{\\textbf{Auxiliary spatial supervision does not improve VLA collision avoidance.} \\textbf{(a)}~A fine-tuned OpenVLA-OFT achieves 90.7\\% Task Success Rate but only 78.0\\% Collision Avoidance Rate on SafeLIBERO Level~I; per-task collision rates reach 93\\% on the most constrained tasks. \\textbf{(b)}~Our factorial design varies five factors (gradient flow, label content, normalization type, spatial reference frame, temporal extent) across 12 conditions. An auxiliary spatial head is attached to the vision encoders during training and discarded at inference.}",
          " \\label{fig:overview}",
          " \\end{figure*}",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 13_

已删除 caption 中 panel (c) 的描述，保留 (a) 和 (b)。最终 caption 以 (b) 的句子结尾，文字通顺。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a2ad9c4-1f39-4180-8861-f3efff698425",
  "uuid": "35b053ca-d8af-458e-8c10-8e82b54c78f9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015CBtLbbHmtoMReWy3RBFAs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 319,
      "cache_read_input_tokens": 28014,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 319
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

_source line 14_

已删除 caption 中 panel (c) 的描述，保留 (a) 和 (b)。最终 caption 以 (b) 的句子结尾，文字通顺。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 23475,
  "duration_api_ms": 24289,
  "num_turns": 4,
  "stop_reason": "end_turn",
  "session_id": "0a2ad9c4-1f39-4180-8861-f3efff698425",
  "total_cost_usd": 0.16525199999999998,
  "usage": {
    "input_tokens": 6,
    "cache_creation_input_tokens": 16492,
    "cache_read_input_tokens": 89910,
    "output_tokens": 634,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 16492,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 57,
        "cache_read_input_tokens": 28014,
        "cache_creation_input_tokens": 319,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 319
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1262,
      "outputTokens": 16,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001342,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 6,
      "outputTokens": 634,
      "cacheReadInputTokens": 89910,
      "cacheCreationInputTokens": 16492,
      "webSearchRequests": 0,
      "costUSD": 0.16391,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "793a286c-f190-468c-95b3-be1e9818b17b"
}
```

</details>

---
