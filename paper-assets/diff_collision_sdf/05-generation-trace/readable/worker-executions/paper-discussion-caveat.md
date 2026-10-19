# paper discussion caveat

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 0
- **Tool calls:** 4
- **Original source:** `logs/workers/worker_paper_discussion-caveat_20260529T001938.log`
- **Structured JSON:** [`46272ffe145dcbe4ead0.json`](../../sessions/46/46272ffe145dcbe4ead0.json)

## Before a recorded user message

17 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf",
  "session_id": "93e98b7e-e124-473c-86b6-1a710194a867",
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
  "uuid": "1d9ad5ba-99e8-4f81-9615-5ba82cb4ae8d",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-projects-diff-collision-sdf/memory/"
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
    "resetsAt": 1780031400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "f9ff4b0e-8bc8-4560-b8de-427a069095b1",
  "session_id": "93e98b7e-e124-473c-86b6-1a710194a867"
}
```

---

### Assistant

_source line 4_

Let me read the discussion.tex file first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "93e98b7e-e124-473c-86b6-1a710194a867",
  "uuid": "b6402844-bb5e-45bd-aa2f-7014d1fd689a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fgc794qcnQdUPDCe1Pp4Bn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13100,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13100
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

<details open><summary>🔧 Tool call — Read · `toolu_01A7mbwbTdSML3NMciryWunV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "93e98b7e-e124-473c-86b6-1a710194a867",
  "uuid": "e26220af-ab99-4ebb-bdba-7e298f6babc5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fgc794qcnQdUPDCe1Pp4Bn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13100,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13100
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

_source line 6 · 2026-05-29T00:19:51.142Z_

<details><summary>↩ Tool result · `toolu_01A7mbwbTdSML3NMciryWunV`</summary>

```text
1	\section{Discussion and Conclusion}\label{sec:conclusion}
2	
3	Across 100+ experiments and 6000+ evaluation episodes on two VLA model families, three findings converge: CAR-based VLA safety evaluation on SafeLIBERO is structurally unreliable. Action collapse renders reported CAR illusory (\S\ref{sec:dfcar}); EE-only oracle refinement is counterproductive (\S\ref{sec:ee_only}); and collision-free demonstrations account for nearly all measured avoidance gains, with EE-only SDF contributing no statistically significant improvement (\S\ref{sec:avoidance_source}).
4	
5	\begin{figure}[t]
6	\centering
7	\includegraphics[width=\columnwidth]{fig5_lambda_curve}
8	\caption{Effect of SDF loss weight $\lambda$ on CAR and TSR. $\lambda = 0$: LoRA-only. The $\lambda \in \{0.01, 0.1\}$ values remain within the null band ($p > 0.05$), consistent with the absence of statistically significant improvement across a 20$\times$ loss-weight range.}
9	\label{fig:lambda_car}
10	\end{figure}
11	\paragraph{Why EE-only SDF fails.}
12	Two independent causes explain the null result. \textit{(i)~Demonstration data subsumes the SDF signal.} Collision-free demonstrations implicitly encode spatial avoidance; the ${\sim}$26\,pp CAR gain arises from this distributional shift, with per-task ordering invariant across all SDF conditions (\S\ref{sec:avoidance_source}). Even at $\lambda = 0.1$, CAR remains within the null distribution ($p = 0.155$). \textit{(ii)~EE monitoring cannot prevent full-body collisions.} The SDF gradient acts on a single point while collisions occur along intermediate links; ground-truth oracle refinement \emph{reduces} CAR by 5--10\,pp (\S\ref{sec:ee_only}) because pushing the EE away rotates unmonitored links through obstacles. These causes are independent; effective geometric safety requires both full-body supervision and training signals beyond demonstrations.
13	
14	\paragraph{Implications for evaluation.}
15	dfCAR corrects action-collapse contamination using only EE position logging, already available in most evaluation pipelines. We recommend reporting both CAR and dfCAR as a diagnostic complement; the gap quantifies contamination across a ${\sim}$4000$\times$ parameter range.
16	
17	\paragraph{Future work.}
18	Three directions follow: (1) full-body SDF supervision along the kinematic chain; (2) cross-architecture evaluation on OpenVLA, RT-2, and other VLA families; (3) planning-layer safety constraints in joint space integrating with constrained-optimization frameworks.
19	
20	\section{Limitations}\label{sec:limitations}
21	
22	All experiments use MuJoCo simulation (SafeLIBERO, two VLA families, four pick-and-place tasks). Action collapse is structurally general but untested on other benchmarks and real hardware. The EE-only SDF null result is specific to auxiliary loss integration and should not be extrapolated to alternative pathways (Section~\ref{sec:related}). The sim-to-real gap introduces uncertainty: collision detection precision and contact dynamics differ on physical hardware. However, the core diagnostic---near-zero motor output inflating CAR---is kinematic; dfCAR requires only EE position logging and applies on physical platforms. Statistical power is limited by $n{=}3$ seeds per condition (MDE ${\approx}$ 5.6\,pp at 80\% power); a genuine SDF benefit below this threshold would go undetected, and larger-scale experiments could reveal effects in the 2--5\,pp range that our design cannot resolve. Oracle experiments used largely action-collapsed baselines; validation on actively moving policies and full-body SDF remain necessary before generalizing the counterproductive finding to non-collapsed settings. Run-to-run variance (same model, training seed, evaluation seed) is approximately 0.5\,pp CAR and 5.5\,pp TSR, bounding measurement precision.
23	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "93e98b7e-e124-473c-86b6-1a710194a867",
  "uuid": "114d1e4d-2115-430c-8564-d0c56ffd6402",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex",
      "content": "\\section{Discussion and Conclusion}\\label{sec:conclusion}\n\nAcross 100+ experiments and 6000+ evaluation episodes on two VLA model families, three findings converge: CAR-based VLA safety evaluation on SafeLIBERO is structurally unreliable. Action collapse renders reported CAR illusory (\\S\\ref{sec:dfcar}); EE-only oracle refinement is counterproductive (\\S\\ref{sec:ee_only}); and collision-free demonstrations account for nearly all measured avoidance gains, with EE-only SDF contributing no statistically significant improvement (\\S\\ref{sec:avoidance_source}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig5_lambda_curve}\n\\caption{Effect of SDF loss weight $\\lambda$ on CAR and TSR. $\\lambda = 0$: LoRA-only. The $\\lambda \\in \\{0.01, 0.1\\}$ values remain within the null band ($p > 0.05$), consistent with the absence of statistically significant improvement across a 20$\\times$ loss-weight range.}\n\\label{fig:lambda_car}\n\\end{figure}\n\\paragraph{Why EE-only SDF fails.}\nTwo independent causes explain the null result. \\textit{(i)~Demonstration data subsumes the SDF signal.} Collision-free demonstrations implicitly encode spatial avoidance; the ${\\sim}$26\\,pp CAR gain arises from this distributional shift, with per-task ordering invariant across all SDF conditions (\\S\\ref{sec:avoidance_source}). Even at $\\lambda = 0.1$, CAR remains within the null distribution ($p = 0.155$). \\textit{(ii)~EE monitoring cannot prevent full-body collisions.} The SDF gradient acts on a single point while collisions occur along intermediate links; ground-truth oracle refinement \\emph{reduces} CAR by 5--10\\,pp (\\S\\ref{sec:ee_only}) because pushing the EE away rotates unmonitored links through obstacles. These causes are independent; effective geometric safety requires both full-body supervision and training signals beyond demonstrations.\n\n\\paragraph{Implications for evaluation.}\ndfCAR corrects action-collapse contamination using only EE position logging, already available in most evaluation pipelines. We recommend reporting both CAR and dfCAR as a diagnostic complement; the gap quantifies contamination across a ${\\sim}$4000$\\times$ parameter range.\n\n\\paragraph{Future work.}\nThree directions follow: (1) full-body SDF supervision along the kinematic chain; (2) cross-architecture evaluation on OpenVLA, RT-2, and other VLA families; (3) planning-layer safety constraints in joint space integrating with constrained-optimization frameworks.\n\n\\section{Limitations}\\label{sec:limitations}\n\nAll experiments use MuJoCo simulation (SafeLIBERO, two VLA families, four pick-and-place tasks). Action collapse is structurally general but untested on other benchmarks and real hardware. The EE-only SDF null result is specific to auxiliary loss integration and should not be extrapolated to alternative pathways (Section~\\ref{sec:related}). The sim-to-real gap introduces uncertainty: collision detection precision and contact dynamics differ on physical hardware. However, the core diagnostic---near-zero motor output inflating CAR---is kinematic; dfCAR requires only EE position logging and applies on physical platforms. Statistical power is limited by $n{=}3$ seeds per condition (MDE ${\\approx}$ 5.6\\,pp at 80\\% power); a genuine SDF benefit below this threshold would go undetected, and larger-scale experiments could reveal effects in the 2--5\\,pp range that our design cannot resolve. Oracle experiments used largely action-collapsed baselines; validation on actively moving policies and full-body SDF remain necessary before generalizing the counterproductive finding to non-collapsed settings. Run-to-run variance (same model, training seed, evaluation seed) is approximately 0.5\\,pp CAR and 5.5\\,pp TSR, bounding measurement precision.\n",
      "numLines": 23,
      "startLine": 1,
      "totalLines": 23
    }
  }
}
```

</details>

---

### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
I need to insert the caveat sentence after `($p = 0.155$).` and before `\textit{(ii)~EE monitoring`. Let me construct the edit.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "93e98b7e-e124-473c-86b6-1a710194a867",
  "uuid": "05d38738-39d6-4f00-aa1c-24e33a89d8c0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HUMWFrr7nnrjoVNtWt4Nk9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1148,
      "cache_read_input_tokens": 24551,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1148
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

_source line 8_

Now I'll insert the caveat sentence.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "93e98b7e-e124-473c-86b6-1a710194a867",
  "uuid": "001e9dee-468a-436a-b31b-464a24535cca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HUMWFrr7nnrjoVNtWt4Nk9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1148,
      "cache_read_input_tokens": 24551,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1148
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

_source line 9_

<details open><summary>🔧 Tool call — Edit · `toolu_014AYooYwfsXNw1CyUmTdsrL`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex",
  "old_string": "($p = 0.155$). \\textit{(ii)~EE monitoring",
  "new_string": "($p = 0.155$). We emphasize that our conclusion is absence of a detectable benefit at our experimental scale; a genuine 2--3\\,pp effect remains consistent with our data but would require substantially larger experiments to resolve. \\textit{(ii)~EE monitoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "93e98b7e-e124-473c-86b6-1a710194a867",
  "uuid": "58acfe57-01db-4247-8ad3-d20b4190572b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HUMWFrr7nnrjoVNtWt4Nk9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1148,
      "cache_read_input_tokens": 24551,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1148
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

_source line 10 · 2026-05-29T00:19:55.850Z_

<details><summary>↩ Tool result · `toolu_014AYooYwfsXNw1CyUmTdsrL`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "93e98b7e-e124-473c-86b6-1a710194a867",
  "uuid": "52eca8ea-c509-469f-b472-77c69d478c88",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex",
    "oldString": "($p = 0.155$). \\textit{(ii)~EE monitoring",
    "newString": "($p = 0.155$). We emphasize that our conclusion is absence of a detectable benefit at our experimental scale; a genuine 2--3\\,pp effect remains consistent with our data but would require substantially larger experiments to resolve. \\textit{(ii)~EE monitoring",
    "originalFile": "\\section{Discussion and Conclusion}\\label{sec:conclusion}\n\nAcross 100+ experiments and 6000+ evaluation episodes on two VLA model families, three findings converge: CAR-based VLA safety evaluation on SafeLIBERO is structurally unreliable. Action collapse renders reported CAR illusory (\\S\\ref{sec:dfcar}); EE-only oracle refinement is counterproductive (\\S\\ref{sec:ee_only}); and collision-free demonstrations account for nearly all measured avoidance gains, with EE-only SDF contributing no statistically significant improvement (\\S\\ref{sec:avoidance_source}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig5_lambda_curve}\n\\caption{Effect of SDF loss weight $\\lambda$ on CAR and TSR. $\\lambda = 0$: LoRA-only. The $\\lambda \\in \\{0.01, 0.1\\}$ values remain within the null band ($p > 0.05$), consistent with the absence of statistically significant improvement across a 20$\\times$ loss-weight range.}\n\\label{fig:lambda_car}\n\\end{figure}\n\\paragraph{Why EE-only SDF fails.}\nTwo independent causes explain the null result. \\textit{(i)~Demonstration data subsumes the SDF signal.} Collision-free demonstrations implicitly encode spatial avoidance; the ${\\sim}$26\\,pp CAR gain arises from this distributional shift, with per-task ordering invariant across all SDF conditions (\\S\\ref{sec:avoidance_source}). Even at $\\lambda = 0.1$, CAR remains within the null distribution ($p = 0.155$). \\textit{(ii)~EE monitoring cannot prevent full-body collisions.} The SDF gradient acts on a single point while collisions occur along intermediate links; ground-truth oracle refinement \\emph{reduces} CAR by 5--10\\,pp (\\S\\ref{sec:ee_only}) because pushing the EE away rotates unmonitored links through obstacles. These causes are independent; effective geometric safety requires both full-body supervision and training signals beyond demonstrations.\n\n\\paragraph{Implications for evaluation.}\ndfCAR corrects action-collapse contamination using only EE position logging, already available in most evaluation pipelines. We recommend reporting both CAR and dfCAR as a diagnostic complement; the gap quantifies contamination across a ${\\sim}$4000$\\times$ parameter range.\n\n\\paragraph{Future work.}\nThree directions follow: (1) full-body SDF supervision along the kinematic chain; (2) cross-architecture evaluation on OpenVLA, RT-2, and other VLA families; (3) planning-layer safety constraints in joint space integrating with constrained-optimization frameworks.\n\n\\section{Limitations}\\label{sec:limitations}\n\nAll experiments use MuJoCo simulation (SafeLIBERO, two VLA families, four pick-and-place tasks). Action collapse is structurally general but untested on other benchmarks and real hardware. The EE-only SDF null result is specific to auxiliary loss integration and should not be extrapolated to alternative pathways (Section~\\ref{sec:related}). The sim-to-real gap introduces uncertainty: collision detection precision and contact dynamics differ on physical hardware. However, the core diagnostic---near-zero motor output inflating CAR---is kinematic; dfCAR requires only EE position logging and applies on physical platforms. Statistical power is limited by $n{=}3$ seeds per condition (MDE ${\\approx}$ 5.6\\,pp at 80\\% power); a genuine SDF benefit below this threshold would go undetected, and larger-scale experiments could reveal effects in the 2--5\\,pp range that our design cannot resolve. Oracle experiments used largely action-collapsed baselines; validation on actively moving policies and full-body SDF remain necessary before generalizing the counterproductive finding to non-collapsed settings. Run-to-run variance (same model, training seed, evaluation seed) is approximately 0.5\\,pp CAR and 5.5\\,pp TSR, bounding measurement precision.\n",
    "structuredPatch": [
      {
        "oldStart": 9,
        "oldLines": 7,
        "newStart": 9,
        "newLines": 7,
        "lines": [
          " \\label{fig:lambda_car}",
          " \\end{figure}",
          " \\paragraph{Why EE-only SDF fails.}",
          "-Two independent causes explain the null result. \\textit{(i)~Demonstration data subsumes the SDF signal.} Collision-free demonstrations implicitly encode spatial avoidance; the ${\\sim}$26\\,pp CAR gain arises from this distributional shift, with per-task ordering invariant across all SDF conditions (\\S\\ref{sec:avoidance_source}). Even at $\\lambda = 0.1$, CAR remains within the null distribution ($p = 0.155$). \\textit{(ii)~EE monitoring cannot prevent full-body collisions.} The SDF gradient acts on a single point while collisions occur along intermediate links; ground-truth oracle refinement \\emph{reduces} CAR by 5--10\\,pp (\\S\\ref{sec:ee_only}) because pushing the EE away rotates unmonitored links through obstacles. These causes are independent; effective geometric safety requires both full-body supervision and training signals beyond demonstrations.",
          "+Two independent causes explain the null result. \\textit{(i)~Demonstration data subsumes the SDF signal.} Collision-free demonstrations implicitly encode spatial avoidance; the ${\\sim}$26\\,pp CAR gain arises from this distributional shift, with per-task ordering invariant across all SDF conditions (\\S\\ref{sec:avoidance_source}). Even at $\\lambda = 0.1$, CAR remains within the null distribution ($p = 0.155$). We emphasize that our conclusion is absence of a detectable benefit at our experimental scale; a genuine 2--3\\,pp effect remains consistent with our data but would require substantially larger experiments to resolve. \\textit{(ii)~EE monitoring cannot prevent full-body collisions.} The SDF gradient acts on a single point while collisions occur along intermediate links; ground-truth oracle refinement \\emph{reduces} CAR by 5--10\\,pp (\\S\\ref{sec:ee_only}) because pushing the EE away rotates unmonitored links through obstacles. These causes are independent; effective geometric safety requires both full-body supervision and training signals beyond demonstrations.",
          " ",
          " \\paragraph{Implications for evaluation.}",
          " dfCAR corrects action-collapse contamination using only EE position logging, already available in most evaluation pipelines. We recommend reporting both CAR and dfCAR as a diagnostic complement; the gap quantifies contamination across a ${\\sim}$4000$\\times$ parameter range."
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

_source line 11_

Now let me run paper_switch.py --verify.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "93e98b7e-e124-473c-86b6-1a710194a867",
  "uuid": "572c5a0d-4089-4918-ba49-fc1fcf82f667",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JM7zyHd1oyfAsV8FmXiaRx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 345,
      "cache_read_input_tokens": 25699,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 345
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

_source line 12_

<details open><summary>🔧 Tool call — Bash · `toolu_015fcPcMjmXYW6bRz49XYhzM`</summary>

```json
{
  "command": "python artifacts/paper_switch.py --verify 2>&1",
  "description": "Verify paper anchors after edit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "93e98b7e-e124-473c-86b6-1a710194a867",
  "uuid": "f834d418-09a5-4f53-84d9-d33ea3539e75",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JM7zyHd1oyfAsV8FmXiaRx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 345,
      "cache_read_input_tokens": 25699,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 345
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

_source line 13 · 2026-05-29T00:19:59.528Z_

<details><summary>↩ Tool result · reported error · `toolu_015fcPcMjmXYW6bRz49XYhzM`</summary>

```text
Exit code 127
/bin/bash: line 1: python: command not found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "93e98b7e-e124-473c-86b6-1a710194a867",
  "uuid": "4324bf47-95e1-4201-9440-089ccd52751a",
  "tool_use_result": "Error: Exit code 127\n/bin/bash: line 1: python: command not found"
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — Bash · `toolu_01Nu4Kke6EAD7fg7TxUXMkBf`</summary>

```json
{
  "command": "python3 artifacts/paper_switch.py --verify 2>&1",
  "description": "Verify paper anchors after edit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "93e98b7e-e124-473c-86b6-1a710194a867",
  "uuid": "8c72502c-134b-4889-99d6-d3df22dbf62f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013JQ4sdJDfVqGyajeu62HMM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 140,
      "cache_read_input_tokens": 26044,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 140
      },
      "output_tokens": 69,
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

_source line 15 · 2026-05-29T00:20:02.831Z_

<details><summary>↩ Tool result · `toolu_01Nu4Kke6EAD7fg7TxUXMkBf`</summary>

```text
--- Scenario B (10 items) ---
  [OK]      abstract L5 training                abstract.tex
  [OK]      abstract L6 conclusion              abstract.tex
  [OK]      claim3 L3 scope                     claim3.tex
  [OK]      claim3 L7 caption                   claim3.tex
  [OK]      claim3 L20 table row                claim3.tex
  [OK]      claim3 L27 body                     claim3.tex
  [OK]      claim3 L32-33 dose-response         claim3.tex
  [OK]      discussion fig caption              discussion.tex
  [OK]      discussion L6                       discussion.tex
  [OK]      discussion L12 limitation           discussion.tex
--- Scenario C (11 items) ---
  [OK]      abstract L5 training                abstract.tex
  [OK]      abstract L6 conclusion              abstract.tex
  [OK]      claim3 L3 scope                     claim3.tex
  [OK]      claim3 L7 caption                   claim3.tex
  [OK]      claim3 L20 table row                claim3.tex
  [OK]      claim3 L27 body                     claim3.tex
  [OK]      claim3 L32-33 dose-response         claim3.tex
  [OK]      discussion fig caption              discussion.tex
  [OK]      discussion L3 scope                 discussion.tex
  [OK]      discussion L6                       discussion.tex
  [OK]      discussion L12 limitation           discussion.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "93e98b7e-e124-473c-86b6-1a710194a867",
  "uuid": "994bb246-3fba-4984-b8e3-0086e2fc560e",
  "tool_use_result": {
    "stdout": "--- Scenario B (10 items) ---\n  [OK]      abstract L5 training                abstract.tex\n  [OK]      abstract L6 conclusion              abstract.tex\n  [OK]      claim3 L3 scope                     claim3.tex\n  [OK]      claim3 L7 caption                   claim3.tex\n  [OK]      claim3 L20 table row                claim3.tex\n  [OK]      claim3 L27 body                     claim3.tex\n  [OK]      claim3 L32-33 dose-response         claim3.tex\n  [OK]      discussion fig caption              discussion.tex\n  [OK]      discussion L6                       discussion.tex\n  [OK]      discussion L12 limitation           discussion.tex\n--- Scenario C (11 items) ---\n  [OK]      abstract L5 training                abstract.tex\n  [OK]      abstract L6 conclusion              abstract.tex\n  [OK]      claim3 L3 scope                     claim3.tex\n  [OK]      claim3 L7 caption                   claim3.tex\n  [OK]      claim3 L20 table row                claim3.tex\n  [OK]      claim3 L27 body                     claim3.tex\n  [OK]      claim3 L32-33 dose-response         claim3.tex\n  [OK]      discussion fig caption              discussion.tex\n  [OK]      discussion L3 scope                 discussion.tex\n  [OK]      discussion L6                       discussion.tex\n  [OK]      discussion L12 limitation           discussion.tex",
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

_source line 16_

21/21 全部通过。

discussion.tex 已更新：在 `$p = 0.155$` 之后插入了统计功效 caveat 句，paper_switch.py 验证 21/21 OK。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "93e98b7e-e124-473c-86b6-1a710194a867",
  "uuid": "92c775a5-4d9a-4280-818e-78b198082fea",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GuzTjVpMLjS2Kh4nCwcWC1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 479,
      "cache_read_input_tokens": 26184,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 479
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

_source line 17_

21/21 全部通过。

discussion.tex 已更新：在 `$p = 0.155$` 之后插入了统计功效 caveat 句，paper_switch.py 验证 21/21 OK。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 17994,
  "duration_api_ms": 18582,
  "num_turns": 5,
  "stop_reason": "end_turn",
  "session_id": "93e98b7e-e124-473c-86b6-1a710194a867",
  "total_cost_usd": 0.17077350000000002,
  "usage": {
    "input_tokens": 6,
    "cache_creation_input_tokens": 15212,
    "cache_read_input_tokens": 113929,
    "output_tokens": 687,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 15212,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 64,
        "cache_read_input_tokens": 26184,
        "cache_creation_input_tokens": 479,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 479
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1449,
      "outputTokens": 16,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001529,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 6,
      "outputTokens": 687,
      "cacheReadInputTokens": 113929,
      "cacheCreationInputTokens": 15212,
      "webSearchRequests": 0,
      "costUSD": 0.16924450000000002,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "38576722-2593-4f67-aa77-f19851096f9a"
}
```

</details>

---
