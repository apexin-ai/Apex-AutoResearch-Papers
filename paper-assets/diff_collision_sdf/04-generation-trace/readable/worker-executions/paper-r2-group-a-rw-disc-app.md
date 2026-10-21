# paper r2 group a rw disc app

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 108
- **Recorded user turns:** 0
- **Tool calls:** 40
- **Original source:** `logs/workers/worker_paper_r2-group-a-rw-disc-app_20260528T065004.log`
- **Structured JSON:** [`7403f682450c992002ee.json`](../../sessions/74/7403f682450c992002ee.json)

## Before a recorded user message

108 recorded events

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
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
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
  "uuid": "c0b4dfc7-6985-4fb0-9eb9-64a287a9ad46",
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
    "resetsAt": 1779966600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "cee7777b-d634-42e3-a105-dccd1f338004",
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading all three files and finding the bib file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "2c50d876-14ea-4517-b2a0-b61a70991f5a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AspgegkKAc14hRyJk6zMou",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12904,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12904
      },
      "output_tokens": 30,
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

_source line 5_

先读取三个目标文件和查找 bib 文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "49f6fde0-ddf7-4436-8b27-ced59d008a70",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AspgegkKAc14hRyJk6zMou",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12904,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12904
      },
      "output_tokens": 30,
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

_source line 6_

<details open><summary>🔧 Tool call — Read · `toolu_01L2uDmxEktF5cDbqXbM5JNs`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "122b9c91-fc35-4345-ad50-a7ae2ae8c0d0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AspgegkKAc14hRyJk6zMou",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12904,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12904
      },
      "output_tokens": 30,
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

_source line 7 · 2026-05-28T06:50:19.897Z_

<details><summary>↩ Tool result · `toolu_01L2uDmxEktF5cDbqXbM5JNs`</summary>

```text
1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Vision-Language-Action Models.}
4	VLA models combine pretrained vision-language backbones with action prediction for generalist manipulation~\cite{brohan2023rt2,black2024pi0,chi2023diffusionpolicy,kim2024openvla}. Recent work enhances spatial reasoning through auxiliary 3D supervision~\cite{li2025spatialforcing,li2025qdepth,depthvla2025}, but safety considerations remain largely absent: most VLAs train on collision-free demonstrations and evaluate task success alone, with no mechanism to distinguish genuine avoidance from incidental collision-free trajectories.
5	
6	\paragraph{Safety in Robot Learning.}
7	Safety-aware approaches span training-time constrained RL~\cite{zhang2025safevla} and test-time filters: control barrier functions~\cite{hu2025vlsa}, collision risk gating~\cite{cofreeevla2026}, inverse kinematics QP~\cite{spalter2024ikinqp}, and diffusion-process collision costs~\cite{li2024langguided,yang2025cape}. SafeDiffuser~\cite{xiao2025safediffuser} integrates control barrier functions directly into diffusion denoising to enforce safety invariance during planning; like other test-time shields, it does not learn intrinsic collision awareness within the policy. A recent survey~\cite{li2026vlasafety} categorizes these into runtime shields, constrained optimization, and representation-based methods. Common to all is that safety is imposed externally rather than learned within the policy's representations. This work tests whether auxiliary SDF supervision can produce intrinsic collision awareness.
8	
9	\paragraph{Signed Distance Functions in Robotics.}
10	SDFs encode minimum surface distance, where the sign indicates free space or penetration. Neural SDFs~\cite{park2019deepsdf} enable continuous shape representation; in robotics, SDFs serve perception~\cite{ortiz2022isdf}, planning~\cite{huang2023voxposer,vasilopoulos2023ramp}, and differentiable collision detection~\cite{zhi2021diffco}. CDF~\cite{li2024cdf} extends SDFs to robot configuration space, learning neural distance fields that provide efficient joint-angle queries with analytical gradients for manipulation planning; CSSDF-Net~\cite{chen2026cssdfnet} further develops this direction for safe motion planning. RDF~\cite{li2024rdf} represents robot geometry itself as composable per-link SDFs along the kinematic chain, enabling whole-body collision queries---directly relevant to the full-body awareness gap our work identifies. Neural SDF-based model predictive control~\cite{jacquet2025neuralnmpc} demonstrates effectiveness in classical pipelines, but integration into end-to-end learned policies remains unexplored.
11	
12	\paragraph{SDF integration pathways.} Geometric supervision via signed distance fields can be integrated into VLA policies through fundamentally different mechanisms. (a)~\emph{Training-time auxiliary loss}: an SDF-based collision penalty is added to the training objective, supervising only the end-effector trajectory (the approach tested in this work). (b)~\emph{Constraint-based planning}: SafeVLA~\citep{zhang2025safevla} formulates collision avoidance as a constrained MDP, using SDF constraints during planning rather than training. (c)~\emph{Runtime filtering}: VLSA~\citep{hu2025vlsa} applies control barrier functions (CBFs) with SDF at inference time, filtering unsafe actions post-hoc. Our negative finding---that EE-only auxiliary SDF loss is redundant---is specific to pathway~(a) and does not apply to pathways~(b) and~(c), which bypass the structural limitation of supervising only the end-effector during training.
13	
14	\paragraph{Evaluation Metrics for Safe Manipulation.}
15	SafeLIBERO~\cite{hu2025vlsa} extends LIBERO~\cite{liu2023libero} with obstacle-augmented environments and a collision avoidance rate (CAR) metric. However, CAR treats all collision-free episodes identically: an action-collapsed robot scores near-perfect CAR without any avoidance behavior. This failure mode echoes concerns about metric reliability~\cite{karwowski2024goodhart,gururangan2018annotation} and binary success metrics under limited samples~\cite{snyder2026beyond}. Action collapse in diffusion policies~\cite{dong2025conditioning} systematically inflates CAR but has not been previously examined as a safety evaluation confounder. We propose dfCAR (\S\ref{sec:dfcar}) to detect this contamination.
16	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "5f6c4a07-6f69-441f-b366-8a279b91543d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/related_work.tex",
      "content": "\\section{Related Work}\\label{sec:related}\n\n\\paragraph{Vision-Language-Action Models.}\nVLA models combine pretrained vision-language backbones with action prediction for generalist manipulation~\\cite{brohan2023rt2,black2024pi0,chi2023diffusionpolicy,kim2024openvla}. Recent work enhances spatial reasoning through auxiliary 3D supervision~\\cite{li2025spatialforcing,li2025qdepth,depthvla2025}, but safety considerations remain largely absent: most VLAs train on collision-free demonstrations and evaluate task success alone, with no mechanism to distinguish genuine avoidance from incidental collision-free trajectories.\n\n\\paragraph{Safety in Robot Learning.}\nSafety-aware approaches span training-time constrained RL~\\cite{zhang2025safevla} and test-time filters: control barrier functions~\\cite{hu2025vlsa}, collision risk gating~\\cite{cofreeevla2026}, inverse kinematics QP~\\cite{spalter2024ikinqp}, and diffusion-process collision costs~\\cite{li2024langguided,yang2025cape}. SafeDiffuser~\\cite{xiao2025safediffuser} integrates control barrier functions directly into diffusion denoising to enforce safety invariance during planning; like other test-time shields, it does not learn intrinsic collision awareness within the policy. A recent survey~\\cite{li2026vlasafety} categorizes these into runtime shields, constrained optimization, and representation-based methods. Common to all is that safety is imposed externally rather than learned within the policy's representations. This work tests whether auxiliary SDF supervision can produce intrinsic collision awareness.\n\n\\paragraph{Signed Distance Functions in Robotics.}\nSDFs encode minimum surface distance, where the sign indicates free space or penetration. Neural SDFs~\\cite{park2019deepsdf} enable continuous shape representation; in robotics, SDFs serve perception~\\cite{ortiz2022isdf}, planning~\\cite{huang2023voxposer,vasilopoulos2023ramp}, and differentiable collision detection~\\cite{zhi2021diffco}. CDF~\\cite{li2024cdf} extends SDFs to robot configuration space, learning neural distance fields that provide efficient joint-angle queries with analytical gradients for manipulation planning; CSSDF-Net~\\cite{chen2026cssdfnet} further develops this direction for safe motion planning. RDF~\\cite{li2024rdf} represents robot geometry itself as composable per-link SDFs along the kinematic chain, enabling whole-body collision queries---directly relevant to the full-body awareness gap our work identifies. Neural SDF-based model predictive control~\\cite{jacquet2025neuralnmpc} demonstrates effectiveness in classical pipelines, but integration into end-to-end learned policies remains unexplored.\n\n\\paragraph{SDF integration pathways.} Geometric supervision via signed distance fields can be integrated into VLA policies through fundamentally different mechanisms. (a)~\\emph{Training-time auxiliary loss}: an SDF-based collision penalty is added to the training objective, supervising only the end-effector trajectory (the approach tested in this work). (b)~\\emph{Constraint-based planning}: SafeVLA~\\citep{zhang2025safevla} formulates collision avoidance as a constrained MDP, using SDF constraints during planning rather than training. (c)~\\emph{Runtime filtering}: VLSA~\\citep{hu2025vlsa} applies control barrier functions (CBFs) with SDF at inference time, filtering unsafe actions post-hoc. Our negative finding---that EE-only auxiliary SDF loss is redundant---is specific to pathway~(a) and does not apply to pathways~(b) and~(c), which bypass the structural limitation of supervising only the end-effector during training.\n\n\\paragraph{Evaluation Metrics for Safe Manipulation.}\nSafeLIBERO~\\cite{hu2025vlsa} extends LIBERO~\\cite{liu2023libero} with obstacle-augmented environments and a collision avoidance rate (CAR) metric. However, CAR treats all collision-free episodes identically: an action-collapsed robot scores near-perfect CAR without any avoidance behavior. This failure mode echoes concerns about metric reliability~\\cite{karwowski2024goodhart,gururangan2018annotation} and binary success metrics under limited samples~\\cite{snyder2026beyond}. Action collapse in diffusion policies~\\cite{dong2025conditioning} systematically inflates CAR but has not been previously examined as a safety evaluation confounder. We propose dfCAR (\\S\\ref{sec:dfcar}) to detect this contamination.\n",
      "numLines": 16,
      "startLine": 1,
      "totalLines": 16
    }
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Read · `toolu_01TQR3yfo1NWTK5VDeDXjhm2`</summary>

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
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "c001853f-2fa0-457f-91bf-ecdeba1dda7a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AspgegkKAc14hRyJk6zMou",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12904,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12904
      },
      "output_tokens": 30,
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

_source line 9 · 2026-05-28T06:50:20.569Z_

<details><summary>↩ Tool result · `toolu_01TQR3yfo1NWTK5VDeDXjhm2`</summary>

```text
1	\section{Discussion and Conclusion}\label{sec:conclusion}
2	
3	Across 100+ experiments and 6000+ evaluation episodes on two VLA model families, three findings converge: current VLA safety evaluation is structurally unreliable. Action collapse renders reported CAR illusory (\S\ref{sec:dfcar}); EE-only oracle refinement is counterproductive (\S\ref{sec:ee_only}); and collision-free demonstrations account for nearly all measured avoidance gains, with EE-only SDF contributing no statistically significant improvement (\S\ref{sec:avoidance_source}).
4	
5	\paragraph{Why EE-only SDF fails.}
6	Two independent causes explain the null result. \textit{(i)~Demonstration data largely subsumes the SDF signal.} Collision-free demonstrations implicitly encode spatial avoidance; the ${\sim}$26\,pp CAR gain arises primarily from this distributional shift, with per-task ordering invariant across all SDF conditions (\S\ref{sec:avoidance_source}). Even at $\lambda = 0.1$ (20$\times$ the lowest tested weight), CAR remains within the null distribution ($p = 0.131$), suggesting that EE-only auxiliary SDF loss does not overcome Level~A signal masking---the limitation is architectural for this integration pathway. \textit{(ii)~EE monitoring cannot prevent full-body collisions.} The SDF gradient acts on a single point while collisions occur along intermediate links. Oracle experiments confirm this: ground-truth SDF refinement \emph{reduces} CAR by 6--10\,pp below unrefined baselines (\S\ref{sec:ee_only}), because pushing the EE away rotates unmonitored links through obstacles. We hypothesize that collision-free demonstration trajectories implicitly encode workspace priors through their spatial distribution: the robot learns to favor regions of the workspace that are inherently collision-free, without requiring explicit geometric supervision. These two causes are independent; effective geometric safety requires both full-body supervision and training signals beyond demonstrations. The failure of EE-only auxiliary SDF loss is architectural; constraint-based and runtime filtering approaches bypass this structural limitation through fundamentally different integration mechanisms.
7	
8	\paragraph{Implications for evaluation.}
9	dfCAR corrects action-collapse contamination using only EE position logging, already available in most evaluation pipelines. The bimodal displacement distribution makes $\tau_d$ robust across five orders of magnitude. We recommend reporting both CAR and dfCAR; the gap quantifies contamination. This contamination spans a 4000$\times$ parameter range (Pi0 Full-FT ${\sim}$2.5B to Pi0+A1 ${\sim}$658K trainable), a structural consequence of evaluating avoidance without verifying motion. More broadly, safety may need to operate at the planning or joint-space constraint layer, since any EE-centric loss inherits the same blind spot.
10	
11	\paragraph{Scope and generalizability.} Our findings are drawn from a single benchmark (SafeLIBERO) covering two VLA model families and four pick-and-place manipulation tasks in MuJoCo simulation. The action-collapse mechanism (Claim~1) is structurally general---any policy prone to action collapse will inflate CAR under standard evaluation---but its prevalence across other benchmarks, task types, and real hardware remains an open question. The SDF redundancy finding (Claim~3) is specific to EE-only auxiliary loss integration and should not be extrapolated to alternative SDF integration pathways (Section~\ref{sec:related}).
12	
13	\paragraph{Limitations.}
14	All experiments are conducted in MuJoCo simulation within the SafeLIBERO benchmark. The sim-to-real gap introduces uncertainty: collision detection precision differs between simulation and physical hardware, sensor noise may affect displacement-filtered CAR differently on real robots, and the prevalence of action collapse in physical deployments remains untested. Our evaluation covers only four pick-and-place manipulation tasks with tabletop obstacles; whether the findings generalize to more diverse task families (e.g., bi-manual manipulation, deformable objects, dynamic obstacles) is an open question. Statistical power is limited by $n{=}3$ training seeds per condition, yielding a minimum detectable effect of approximately 5 percentage points at 80\% power---smaller genuine effects, if they exist, would not be detected at this sample size. Oracle experiments used a largely action-collapsed model (Pi0+A1, TSR${\approx}$0\%); testing on an actively moving policy would better isolate the structural limitation. Full-body SDF remains untested. Fine-tuning degrades TSR by ${\sim}$18--20\,pp, yet SSR/TSR increases from 0.39 to 0.51--0.60 (Appendix~\ref{sec:appendix_ssr}); reduced exposure alone does not explain the pattern.
15	
16	\paragraph{Future work.}
17	Three directions follow: (1) full-body SDF supervision along the kinematic chain; (2) cross-architecture evaluation on OpenVLA, RT-2, and other VLA families; (3) planning-layer safety constraints in joint space rather than EE space.
18	
19	\paragraph{Broader impact.}
20	The displacement-filtered CAR metric (dfCAR) is intended as a diagnostic complement to standard CAR, not a replacement; practitioners should report both metrics to distinguish genuine avoidance from action-collapse artifacts. Our finding that EE-only SDF supervision is redundant with demonstration data is an evaluation-methodology insight, not a verdict against safety-aware training---geometric supervision may prove effective through alternative integration pathways or with full-body collision surfaces. We caution against interpreting these results as evidence that VLA safety research is futile; rather, they highlight the need for evaluation protocols that can reliably separate safety improvements from measurement artifacts.
21	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "f1223b1f-fdae-43ae-830d-f1ab4559cee0",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex",
      "content": "\\section{Discussion and Conclusion}\\label{sec:conclusion}\n\nAcross 100+ experiments and 6000+ evaluation episodes on two VLA model families, three findings converge: current VLA safety evaluation is structurally unreliable. Action collapse renders reported CAR illusory (\\S\\ref{sec:dfcar}); EE-only oracle refinement is counterproductive (\\S\\ref{sec:ee_only}); and collision-free demonstrations account for nearly all measured avoidance gains, with EE-only SDF contributing no statistically significant improvement (\\S\\ref{sec:avoidance_source}).\n\n\\paragraph{Why EE-only SDF fails.}\nTwo independent causes explain the null result. \\textit{(i)~Demonstration data largely subsumes the SDF signal.} Collision-free demonstrations implicitly encode spatial avoidance; the ${\\sim}$26\\,pp CAR gain arises primarily from this distributional shift, with per-task ordering invariant across all SDF conditions (\\S\\ref{sec:avoidance_source}). Even at $\\lambda = 0.1$ (20$\\times$ the lowest tested weight), CAR remains within the null distribution ($p = 0.131$), suggesting that EE-only auxiliary SDF loss does not overcome Level~A signal masking---the limitation is architectural for this integration pathway. \\textit{(ii)~EE monitoring cannot prevent full-body collisions.} The SDF gradient acts on a single point while collisions occur along intermediate links. Oracle experiments confirm this: ground-truth SDF refinement \\emph{reduces} CAR by 6--10\\,pp below unrefined baselines (\\S\\ref{sec:ee_only}), because pushing the EE away rotates unmonitored links through obstacles. We hypothesize that collision-free demonstration trajectories implicitly encode workspace priors through their spatial distribution: the robot learns to favor regions of the workspace that are inherently collision-free, without requiring explicit geometric supervision. These two causes are independent; effective geometric safety requires both full-body supervision and training signals beyond demonstrations. The failure of EE-only auxiliary SDF loss is architectural; constraint-based and runtime filtering approaches bypass this structural limitation through fundamentally different integration mechanisms.\n\n\\paragraph{Implications for evaluation.}\ndfCAR corrects action-collapse contamination using only EE position logging, already available in most evaluation pipelines. The bimodal displacement distribution makes $\\tau_d$ robust across five orders of magnitude. We recommend reporting both CAR and dfCAR; the gap quantifies contamination. This contamination spans a 4000$\\times$ parameter range (Pi0 Full-FT ${\\sim}$2.5B to Pi0+A1 ${\\sim}$658K trainable), a structural consequence of evaluating avoidance without verifying motion. More broadly, safety may need to operate at the planning or joint-space constraint layer, since any EE-centric loss inherits the same blind spot.\n\n\\paragraph{Scope and generalizability.} Our findings are drawn from a single benchmark (SafeLIBERO) covering two VLA model families and four pick-and-place manipulation tasks in MuJoCo simulation. The action-collapse mechanism (Claim~1) is structurally general---any policy prone to action collapse will inflate CAR under standard evaluation---but its prevalence across other benchmarks, task types, and real hardware remains an open question. The SDF redundancy finding (Claim~3) is specific to EE-only auxiliary loss integration and should not be extrapolated to alternative SDF integration pathways (Section~\\ref{sec:related}).\n\n\\paragraph{Limitations.}\nAll experiments are conducted in MuJoCo simulation within the SafeLIBERO benchmark. The sim-to-real gap introduces uncertainty: collision detection precision differs between simulation and physical hardware, sensor noise may affect displacement-filtered CAR differently on real robots, and the prevalence of action collapse in physical deployments remains untested. Our evaluation covers only four pick-and-place manipulation tasks with tabletop obstacles; whether the findings generalize to more diverse task families (e.g., bi-manual manipulation, deformable objects, dynamic obstacles) is an open question. Statistical power is limited by $n{=}3$ training seeds per condition, yielding a minimum detectable effect of approximately 5 percentage points at 80\\% power---smaller genuine effects, if they exist, would not be detected at this sample size. Oracle experiments used a largely action-collapsed model (Pi0+A1, TSR${\\approx}$0\\%); testing on an actively moving policy would better isolate the structural limitation. Full-body SDF remains untested. Fine-tuning degrades TSR by ${\\sim}$18--20\\,pp, yet SSR/TSR increases from 0.39 to 0.51--0.60 (Appendix~\\ref{sec:appendix_ssr}); reduced exposure alone does not explain the pattern.\n\n\\paragraph{Future work.}\nThree directions follow: (1) full-body SDF supervision along the kinematic chain; (2) cross-architecture evaluation on OpenVLA, RT-2, and other VLA families; (3) planning-layer safety constraints in joint space rather than EE space.\n\n\\paragraph{Broader impact.}\nThe displacement-filtered CAR metric (dfCAR) is intended as a diagnostic complement to standard CAR, not a replacement; practitioners should report both metrics to distinguish genuine avoidance from action-collapse artifacts. Our finding that EE-only SDF supervision is redundant with demonstration data is an evaluation-methodology insight, not a verdict against safety-aware training---geometric supervision may prove effective through alternative integration pathways or with full-body collision surfaces. We caution against interpreting these results as evidence that VLA safety research is futile; rather, they highlight the need for evaluation protocols that can reliably separate safety improvements from measurement artifacts.\n",
      "numLines": 21,
      "startLine": 1,
      "totalLines": 21
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Read · `toolu_01TYrjJbiuvuan2ZrFKgK72K`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "dfc2bfda-497e-4682-8dce-5597b9370191",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AspgegkKAc14hRyJk6zMou",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12904,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12904
      },
      "output_tokens": 30,
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

_source line 11 · 2026-05-28T06:50:21.106Z_

<details><summary>↩ Tool result · `toolu_01TYrjJbiuvuan2ZrFKgK72K`</summary>

```text
1	\section{Displacement Distribution}
2	\label{sec:appendix_displacement}
3	
4	\begin{figure}[h]
5	\centering
6	\includegraphics[width=\linewidth]{fig2_ee_displacement_distribution}
7	\caption{Displacement distribution across evaluation episodes. Pi0-family models (blue) cluster below 1\,$\mu$m, while Pi0.5 episodes (orange) exceed 200\,mm. The five-order-of-magnitude gap makes $\tau_d$ robust to any value in $[2, 200]$\,mm.}
8	\label{fig:displacement}
9	\end{figure}
10	
11	\section{Displacement Threshold Sensitivity Analysis}
12	\label{sec:appendix_threshold}
13	
14	To validate the robustness of our displacement threshold $\tau_d$, we evaluate the action-collapse rate across four orders of magnitude. Table~\ref{tab:threshold_sensitivity} shows that the action-collapse pattern persists across all reasonable threshold choices: A1-LoRA exhibits near-total action collapse regardless of threshold, while Pi0.5+A1 maintains 0\% action-collapse rate even at the most conservative setting.
15	
16	\begin{table}[h]
17	\centering
18	\caption{Action-collapse rate (\% of episodes with $d_\mathrm{max} < \tau_d$) across threshold values.}
19	\label{tab:threshold_sensitivity}
20	\begin{tabular}{lccc}
21	\toprule
22	$\tau_d$ & A1-LoRA (Pi0) & Pi0.5 Baseline & Pi0.5+A1 (SDF aux) \\
23	\midrule
24	0.001 mm (1\,$\mu$m) & 73.9 & 0.0 & 0.0 \\
25	0.1 mm  & 99.6 & 0.0 & 0.0 \\
26	1.0 mm  & 100.0 & 0.0 & 0.0 \\
27	10 mm   & 100.0 & 0.0 & 0.0 \\
28	\bottomrule
29	\end{tabular}
30	\end{table}
31	
32	The choice of $\tau_d = 0.1$\,mm represents a conservative threshold: displacement below this value is physically negligible in manipulation tasks where typical action magnitudes are 1--10\,mm per step. Even at $\tau_d = 1$\,$\mu$m, 73.9\% of A1-LoRA safe episodes are classified as action-collapsed, while all Pi0.5 episodes remain above threshold at every level tested.
33	
34	Table~\ref{tab:dfcar_threshold} extends this analysis to dfCAR across fine-tuned Pi0.5 configurations. All eight model-seed combinations yield identical dfCAR for $\tau_d \in [2, 200]$\,mm. At $\tau_d = 300$\,mm, 0--2 episodes per seed fall below threshold (displacement 200--300\,mm), causing $\leq$0.5\,pp deviation. Our conclusions hold across the entire tested range.
35	
36	\begin{table}[h]
37	\centering
38	\caption{dfCAR (\%) across displacement thresholds for fine-tuned Pi0.5 configurations ($n = 200$ episodes per seed). Values are identical across $\tau_d \in [2, 200]$\,mm; at $\tau_d = 300$\,mm, at most 2 episodes are excluded.}
39	\label{tab:dfcar_threshold}
40	\vspace{2pt}
41	\footnotesize
42	\begin{tabular}{lcccccccc}
43	\toprule
44	& \multicolumn{8}{c}{$\tau_d$ (mm)} \\
45	\cmidrule(lr){2-9}
46	Condition & 2 & 5 & 10 & 20 & 50 & 100 & 200 & 300 \\
47	\midrule
48	LoRA s0            & 56.5 & 56.5 & 56.5 & 56.5 & 56.5 & 56.5 & 56.5 & 56.5 \\
49	LoRA s1            & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 \\
50	SDF $\lambda{=}0.005$ s0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.1 \\
51	SDF $\lambda{=}0.005$ s1 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 \\
52	SDF $\lambda{=}0.005$ s2 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.3 \\
53	SDF $\lambda{=}0.01$ s0  & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 \\
54	SDF $\lambda{=}0.01$ s1  & 57.5 & 57.5 & 57.5 & 57.5 & 57.5 & 57.5 & 57.5 & 57.1 \\
55	SDF $\lambda{=}0.01$ s2  & 54.5 & 54.5 & 54.5 & 54.5 & 54.5 & 54.5 & 54.5 & 54.0 \\
56	\bottomrule
57	\end{tabular}
58	\end{table}
59	
60	
61	\section{Per-Task TSR Breakdown}\label{sec:appendix_tsr_pertask}
62	
63	Table~\ref{tab:per_task_tsr} decomposes TSR by task for the avoidance source attribution experiments (Section~\ref{sec:avoidance_source}). All tasks retain meaningful success rates after fine-tuning, with Chocolate Pudding most resilient and Orange Juice most affected.
64	
65	\begin{table}[h]
66	\centering
67	\caption{Per-task TSR (\%) at 30K training steps. Baseline reports the unified seed-7 re-evaluation (aggregate TSR\,=\,71.5\%). LoRA-only reports 3-seed means (re-evaluated with unified seed-7 protocol); SDF conditions report 3-seed means.}
68	\label{tab:per_task_tsr}
69	\vspace{2pt}
70	\small
71	\begin{tabular}{lcccc}
72	\toprule
73	Task & Pi0.5 Base & LoRA-only & SDF $\lambda{=}0.005$ & SDF $\lambda{=}0.01$ \\
74	 & (seed\,=\,7) & (3 seeds) & (3 seeds) & (3 seeds) \\
75	\midrule
76	Orange Juice      & 74.0 & 30.0 & 33.3 & 24.7 \\
77	Choco.\ Pudding   & 80.0 & 70.7 & 78.0 & 76.7 \\
78	Milk              & 66.0 & 44.7 & 35.3 & 48.7 \\
79	BBQ Sauce         & 66.0 & 60.7 & 69.3 & 65.3 \\
80	\midrule
81	Mean              & 71.5 & 51.5 & 54.0 & 53.8 \\
82	\bottomrule
83	\end{tabular}
84	\end{table}
85	
86	\section{Per-Task CAR Breakdown}\label{sec:appendix_pertask_car}
87	
88	Table~\ref{tab:per_task_car} decomposes CAR by task for all fine-tuned conditions, supporting the claim that per-task ordering is preserved across SDF loss weights (\S\ref{sec:avoidance_source}). Chocolate Pudding is consistently highest and BBQ Sauce consistently lowest across all conditions, including $\lambda = 0.1$. The intermediate tasks (Orange Juice and Milk) exchange rank between seeds but remain bounded by the extremes. This invariance indicates that avoidance patterns reflect the spatial statistics of collision-free demonstrations rather than geometric supervision.
89	
90	\begin{table}[h]
91	\centering
92	\caption{Per-task CAR (\%) at 30K steps. $\lambda{=}0.005$, $\lambda{=}0.01$, and $\lambda{=}0.1$ report 3-seed means alongside individual seeds. Per-task ordering (CP highest, BBQ lowest) is preserved across all conditions.}
93	\label{tab:per_task_car}
94	\vspace{2pt}
95	\small
96	\begin{tabular}{lccccc}
97	\toprule
98	Condition & OJ & CP & Milk & BBQ & Agg. \\
99	\midrule
100	LoRA s0 & 56 & 74 & 70 & 26 & 56.5 \\
101	LoRA s1 & 54 & 68 & 72 & 16 & 52.5 \\
102	LoRA s2 & 56 & 76 & 62 & 26 & 55.0 \\
103	SDF $\lambda{=}0.005$ (3-seed) & 54.0 & 72.7 & 71.3 & 20.0 & 54.5 \\
104	SDF $\lambda{=}0.01$ (3-seed) & 57.3 & 72.7 & 72.0 & 23.3 & 56.3 \\
105	SDF $\lambda{=}0.1$ s0 & 60 & 74 & 68 & 30 & 58.0 \\
106	SDF $\lambda{=}0.1$ s1 & 66 & 72 & 70 & 26 & 58.5 \\
107	SDF $\lambda{=}0.1$ s2 & 56 & 76 & 70 & 16 & 54.5 \\
108	SDF $\lambda{=}0.1$ (3-seed) & 60.7 & 74.0 & 69.3 & 24.0 & 57.0 \\
109	\bottomrule
110	\end{tabular}
111	\end{table}
112	
113	For the $\lambda = 0.1$ condition, seed~1 records \texttt{avg\_max\_obstacle\_displacement} of 0.0553\,m (per-task: OJ\,=\,0.033, CP\,=\,0.055, Milk\,=\,0.041, BBQ\,=\,0.093), comparable to other fine-tuned conditions and consistent with active manipulation rather than action-collapsed behavior.
114	
115	\begin{figure}[t]
116	\centering
117	\includegraphics[width=\linewidth]{fig_pertask_car_fingerprint}
118	\caption{Per-task CAR fingerprint across conditions. Each bar shows the 3-seed mean; dots indicate individual seeds. The task ordering (chocolate\_pudding highest, bbq\_sauce lowest) is preserved across all $\lambda$ values, confirming that avoidance patterns reflect the demonstration distribution rather than geometric supervision. LoRA-only: 3-seed mean.}
119	\label{fig:pertask_fingerprint}
120	\end{figure}
121	
122	\section{Safe Success Rate Analysis}\label{sec:appendix_ssr}
123	
124	Table~\ref{tab:ssr} reports the Safe Success Rate (SSR\,=\,TSR\,$\cap$\,CAR), the fraction of episodes achieving both task completion and collision avoidance. The SSR/TSR ratio quantifies the proportion of successful episodes that are also collision-free, controlling for task-completion rate.
125	
126	\begin{table}[h]
127	\centering
128	\caption{SSR and SSR/TSR ratio across conditions. The ratio increase from 0.39 (baseline) to 0.51--0.60 (fine-tuned) indicates that CAR gains reflect learned safer execution, not reduced task exposure.}
129	\label{tab:ssr}
130	\vspace{2pt}
131	\small
132	\begin{tabular}{lcccc}
133	\toprule
134	Condition & TSR (\%) & CAR (\%) & SSR (\%) & SSR/TSR \\
135	\midrule
136	Pi0.5 baseline & 71.5 & 28.5 & 28.0 & 0.39 \\
137	LoRA-only (3 seeds) & 51.5 & 54.67 & 27.7 & 0.54 \\
138	SDF $\lambda{=}0.005$ (3 seeds) & 54.0 & 54.5 & 27.8 & 0.51 \\
139	SDF $\lambda{=}0.01$ (3 seeds) & 53.8 & 56.33 & 30.2 & 0.56 \\
140	SDF $\lambda{=}0.1$ (3 seeds) & 50.2 & 57.00 & 30.2 & 0.60 \\
141	\bottomrule
142	\end{tabular}
143	\end{table}
144	
145	\section{Per-Task Oracle Analysis}
146	\label{sec:appendix_pertask}
147	\label{sec:appendix_pertask_oracle}
148	
149	Table~\ref{tab:oracle_pertask} shows per-task CAR for oracle refinement. On task~1 (\texttt{chocolate\_pudding}), where the EE is the primary collision body and the LoRA baseline achieves only 46.0\% CAR, Oracle-adaptive improves to 55.0\% and Oracle-feature to 47.5\%. On the remaining tasks, all oracle variants degrade: Oracle-adaptive reduces task~0 (\texttt{orange\_juice}) from 96.0\% to 82.5\% and task~2 (\texttt{milk}) from 98.0\% to 77.5\%. The SDF gradient pushes the EE away from the nearest surface, but the resulting joint-space displacement rotates intermediate arm links into obstacle volumes.
150	
151	The feature-space oracle fires on nearly every timestep (241.7 refinements/episode vs.\ 14.2 for Cartesian variants) but with gradient magnitudes two orders of magnitude smaller (0.004--0.006 vs.\ 0.18--0.49), and CAR (76.9\%) shows no advantage despite 17$\times$ more steps. The A3 learned SDF never triggers refinement (0 steps/episode), as its outputs avoid the activation threshold.
152	
153	\begin{table}[h]
154	\centering
155	\caption{Per-task CAR (\%) for oracle SDF refinement variants. EE-only refinement helps only on task~1 where the EE is the primary collision body; on other tasks it trades one collision site for another.}
156	\label{tab:oracle_pertask}
157	\vspace{2pt}
158	\small
159	\begin{tabular}{lccccc}
160	\toprule
161	Method & Task 0 & Task 1 & Task 2 & Task 3 & Agg. \\
162	\midrule
163	LoRA baseline & 96.0 & 46.0 & 98.0 & 88.0 & 82.0 \\
164	\midrule
165	Oracle-adaptive & 82.5 & 55.0 & 77.5 & 85.0 & 75.0 \\
166	Oracle-fixed & 85.0 & 50.0 & 77.5 & 80.0 & 73.1 \\
167	Oracle-feature & 90.0 & 47.5 & 82.5 & 87.5 & 76.9 \\
168	\bottomrule
169	\end{tabular}
170	\end{table}
171	
172	
173	\section{Null Distribution for SDF Loss Weight Analysis}
174	\label{sec:appendix_null}
175	
176	We construct a null distribution by pooling the three LoRA-only seeds and three $\lambda = 0.005$ seeds into six per-seed CAR measurements: 56.5\% (LoRA s0, re-evaluated), 52.5\% (LoRA s1), 55.0\% (LoRA s2), 57.0\% ($\lambda{=}0.005$ s0), 54.0\% ($\lambda{=}0.005$ s1), 52.5\% ($\lambda{=}0.005$ s2), yielding mean 54.58\% and standard deviation 1.93\% (Bessel-corrected, $n{-}1 = 5$). We treat these as exchangeable because SDF at $\lambda = 0.005$ produces no separation from LoRA-only. The $\lambda = 0.01$ mean of 56.33\% falls within $0.8\sigma$ of this null ($p > 0.1$), consistent with seed-to-seed variation rather than a treatment effect. The $\lambda = 0.1$ 30K mean of 57.00\% (3 seeds: 58.0\%, 58.5\%, 54.5\%) yields a two-tailed permutation $p = 0.131$ (one-tailed $p = 0.071$). The result is non-significant at conventional thresholds ($\alpha = 0.05$).
177	
178	The permutation test makes no distributional assumptions. Pooling the six null values $\{56.5, 52.5, 55, 57, 54, 52.5\}$ and three $\lambda = 0.1$ values $\{58, 58.5, 54.5\}$ into nine measurements, we enumerate all $\binom{9}{3} = 84$ three-element combinations and compute the fraction whose mean $\geq 57.00$. Six combinations meet this threshold, yielding an exact one-tailed permutation $p = 6/84 \approx 0.071$. For the two-tailed test, we additionally count combinations on the lower tail with equal or greater distance from the pooled mean, yielding $p = 11/84 \approx 0.131$. With the third seed ($s_2 = 54.5\%$) pulling the $\lambda = 0.1$ mean from 58.25\% (2 seeds) down to 57.00\%, the marginal signal observed at $n = 2$ dissolves into seed-to-seed variance.
179	
180	\paragraph{Alternative null construction (Null~A).}
181	If only the three LoRA-only seeds are used as the null pool ($\{56.5, 52.5, 55.0\}$), we obtain $\binom{6}{3} = 20$ permutations for each comparison. For $\lambda = 0.1$ (treatment mean 57.00\%): one-tailed $p = 3/20 = 0.150$, two-tailed $p = 6/20 = 0.300$. For $\lambda = 0.01$ (treatment mean 56.33\%): one-tailed $p = 4/20 = 0.200$, two-tailed $p = 8/20 = 0.400$. Under the broader Null~B pool, $\lambda = 0.01$ yields one-tailed $p = 10/84 \approx 0.119$, two-tailed $p = 22/84 \approx 0.262$. All tests are non-significant at $\alpha = 0.05$; the narrower Null~A yields \emph{larger} $p$-values because the LoRA-only pool already contains a high seed (56.5\%), making the treatment means less extreme by comparison.
182	
183	A Phase~2 ablation reinforces this conclusion. Setting $\lambda = 0$ during Phase~2 (steps 5K--18K), so that SDF supervision is active only during auxiliary head warmup (Phase~1, steps 0--5K), yields CAR of 58.0\% at the 18K checkpoint (13K steps of Phase~2 training, single seed, s2).\footnote{Full 30K training did not complete due to disk constraints; this result uses the last complete checkpoint at step 18K.} This value lies within the null range, indicating that SDF training produces no lasting behavioral effect on collision avoidance.
184	
185	\section{Step-wise Checkpoint Analysis for \texorpdfstring{$\lambda = 0.1$}{lambda = 0.1}}
186	\label{sec:appendix_stepwise}
187	
188	Table~\ref{tab:stepwise_lambda01} reports per-seed CAR at seven checkpoints for $\lambda = 0.1$. Seeds~0 and~1 are available at 16K, 20K, 22K, and 30K; 24K--28K report seed-0 only; seed~2 is available at 30K only. The seed-0 curve shows no monotonic trend through 28K. At 30K, the addition of seed~2 (54.5\%) pulls the three-seed mean to 57.00\%, within the null band ($p = 0.131$).
189	
190	\begin{table}[h]
191	\centering
192	\caption{Per-seed CAR (\%) at training checkpoints for $\lambda = 0.1$ (200 episodes each). 24K--28K: seed-0 only. The 30K checkpoint includes all three seeds; the three-seed mean (57.00\%) remains within the null band ($p = 0.131$, two-tailed permutation).}
193	\label{tab:stepwise_lambda01}
194	\vspace{2pt}
195	\small
196	\begin{tabular}{lcccc}
197	\toprule
198	Checkpoint & Seed 0 & Seed 1 & Seed 2 & Mean \\
199	\midrule
200	16K steps & 55.5 & 56.0 & -- & 55.75 \\
201	20K steps & 55.0 & 56.0 & -- & 55.5 \\
202	22K steps & 60.5 & 56.5 & -- & 58.5 \\
203	24K steps & 52.5 & -- & -- & -- \\
204	26K steps & 53.5 & -- & -- & -- \\
205	28K steps & 54.5 & -- & -- & -- \\
206	30K steps & 58.0 & 58.5 & 54.5 & 57.00 \\
207	\bottomrule
208	\end{tabular}
209	\end{table}
210	
211	Individual seeds exhibit checkpoint-to-checkpoint CAR fluctuations of up to 8\,pp (seed~0: 52.5--60.5\%), larger than the cross-seed standard deviation at any fixed checkpoint ($\leq$3\,pp). This is consistent with binomial sampling noise at $n = 50$ episodes per task ($\sigma \approx 7$\,pp per task for $p \approx 0.5$). At 30K, the third seed ($s_2 = 54.5\%$) falls well within the null range, pulling the three-seed mean to 57.00\% and rendering the earlier two-seed departure non-significant ($p = 0.131$). The seed-averaged curve shows no monotonic trend, confirming that SDF loss weight does not produce a progressive training signal.
212	
213	
214	\section{Oracle SDF Refinement Details}
215	\label{sec:appendix_oracle}
216	
217	All oracle variants replace the learned SDF decoder with ground-truth distance fields computed from the simulation geometry. Each is evaluated for 160 episodes (4 tasks $\times$ 40).
218	
219	\paragraph{Oracle-adaptive.} At each timestep, if the ground-truth SDF at the end-effector position falls below a safety margin, the action is adjusted by a step in the negative SDF gradient direction. The step size $\alpha$ is scaled inversely with distance: smaller distances produce larger corrections. This mimics an adaptive potential field controller.
220	
221	\paragraph{Oracle-fixed.} Identical to Oracle-adaptive except the step size is fixed at $\alpha = 0.005$ regardless of distance. This isolates the effect of step-size adaptation from the refinement geometry.
222	
223	\paragraph{Oracle-feature.} Instead of modifying the action directly in Cartesian space, this variant applies the SDF gradient in the policy's latent feature space via backpropagation. The gradient of the ground-truth SDF value with respect to the intermediate features is computed and used to perturb the features before the action head decodes them. This tests whether geometric corrections are more effective when applied in the model's learned representation space. In practice, the feature-space variant fires on nearly every timestep (241.7 refinements per episode vs.\ 14.2 for Cartesian variants) but with gradient magnitudes two orders of magnitude smaller (0.004--0.006 vs.\ 0.18--0.49 in action space).
224	
225	
226	\section{Cross-Scene Validation: spatial\_bowl}
227	\label{sec:appendix_spatial_bowl}
228	
229	To test whether the SDF redundancy finding generalizes beyond the primary \texttt{object\_pudding} scene, we replicate the core comparison on \texttt{spatial\_bowl}, a separate SafeLIBERO suite with a distinct obstacle layout (moka pot, wine bottle, milk carton, red coffee mug, yellow book). Both conditions use the same architecture, hyperparameters, and two-phase training schedule (30K steps), differing only in the training scene.
230	
231	Table~\ref{tab:spatial_bowl} reports the results. The SDF condition ($\lambda = 0.005$) yields CAR of 11.5\% versus 12.0\% for LoRA-only, a $-$0.5\,pp difference well within the noise floor, indicating that SDF is essentially identical to LoRA-only on this scene. TSR is comparable across conditions (49.0\% vs.\ 51.5\%). Both evaluations use a single training seed (seed~0) and a single evaluation seed (seed~7, 200 episodes), so statistical power is limited; nevertheless, the qualitative pattern---SDF failing to improve over LoRA-only---is consistent with the \texttt{object\_pudding} findings.
232	
233	\begin{table}[h]
234	\centering
235	\caption{Cross-scene validation on \texttt{spatial\_bowl} (single training seed, 200 episodes, 30K checkpoint). The $-$0.5\,pp CAR difference is well within noise, consistent with the SDF redundancy observed on \texttt{object\_pudding}.}
236	\label{tab:spatial_bowl}
237	\vspace{2pt}
238	\small
239	\begin{tabular}{lcc}
240	\toprule
241	Condition & CAR (\%) & TSR (\%) \\
242	\midrule
243	LoRA-only & 12.0 & 49.0 \\
244	SDF $\lambda{=}0.005$ & 11.5 & 51.5 \\
245	\bottomrule
246	\end{tabular}
247	\end{table}
248	
249	The substantially lower CAR on \texttt{spatial\_bowl} relative to \texttt{object\_pudding} (11--12\% vs.\ 54--57\%) reflects the greater scene difficulty: \texttt{spatial\_bowl} places five cluttered obstacles around the workspace, making collision-free manipulation considerably harder. This difficulty affects both conditions equally, and the SDF condition performs comparably ($\Delta$CAR\,=\,$-$0.5\,pp, well within noise), reinforcing the conclusion that EE-only SDF auxiliary supervision does not produce a meaningful collision avoidance benefit beyond LoRA-only fine-tuning.
250	
251	
252	\section{Evaluation Seed Robustness}
253	\label{sec:appendix_eval_seed}
254	
255	To verify that our conclusions are not artifacts of a particular evaluation seed, we re-evaluate the LoRA-only (s0) and SDF $\lambda{=}0.1$ (s0) checkpoints under multiple evaluation seeds. Table~\ref{tab:eval_seed_car} reports aggregate CAR and Table~\ref{tab:eval_seed_tsr} reports aggregate TSR.
256	
257	\begin{table}[h]
258	\centering
259	\caption{Aggregate CAR (\%) across evaluation seeds (200 episodes each). The LoRA vs.\ SDF $\lambda{=}0.1$ ordering is preserved across all tested seeds, and per-task CAR fingerprints (CP highest, BBQ lowest) remain invariant.}
260	\label{tab:eval_seed_car}
261	\vspace{2pt}
262	\small
263	\begin{tabular}{lcccccc}
264	\toprule
265	& \multicolumn{4}{c}{Per-task CAR (\%)} & & \\
266	\cmidrule(lr){2-5}
267	Condition (eval seed) & OJ & CP & Milk & BBQ & Agg. \\
268	\midrule
269	LoRA s0 (seed\,=\,7)   & 56 & 74 & 70 & 26 & 56.5 \\
270	LoRA s0 (seed\,=\,42)  & 60 & 70 & 68 & 28 & 56.5 \\
271	LoRA s0 (seed\,=\,123) & 52 & 74 & 66 & 20 & 53.0 \\
272	LoRA s0 mean $\pm$ std & 56.0$\pm$4.0 & 72.7$\pm$2.3 & 68.0$\pm$2.0 & 24.7$\pm$4.2 & 55.3$\pm$2.0 \\
273	\midrule
274	SDF $\lambda{=}0.1$ s0 (seed\,=\,7)   & 60 & 74 & 68 & 30 & 58.0 \\
275	SDF $\lambda{=}0.1$ s0 (seed\,=\,42)  & 64 & 74 & 74 & 24 & 59.0 \\
276	SDF $\lambda{=}0.1$ s0 (seed\,=\,123) & 62 & 76 & 74 & 22 & 58.5 \\
277	SDF $\lambda{=}0.1$ s0 (seed\,=\,256) & 60 & 72 & 66 & 30 & 57.0 \\
278	SDF $\lambda{=}0.1$ s0 mean $\pm$ std & 61.5$\pm$1.9 & 74.0$\pm$1.6 & 70.5$\pm$4.1 & 26.5$\pm$4.1 & 58.1$\pm$0.9 \\
279	\bottomrule
280	\end{tabular}
281	\end{table}
282	
283	\begin{table}[h]
284	\centering
285	\caption{Aggregate TSR (\%) across evaluation seeds. TSR varies more across seeds than CAR (seed\,=\,42 yields consistently lower TSR), but the relative ordering between LoRA and SDF is stable.}
286	\label{tab:eval_seed_tsr}
287	\vspace{2pt}
288	\small
289	\begin{tabular}{lcccccc}
290	\toprule
291	& \multicolumn{4}{c}{Per-task TSR (\%)} & & \\
292	\cmidrule(lr){2-5}
293	Condition (eval seed) & OJ & CP & Milk & BBQ & Agg. \\
294	\midrule
295	LoRA s0 (seed\,=\,7)   & 32 & 74 & 42 & 58 & 51.5 \\
296	LoRA s0 (seed\,=\,42)  & 22 & 70 & 32 & 60 & 46.0 \\
297	LoRA s0 (seed\,=\,123) & 30 & 70 & 40 & 62 & 50.5 \\
298	LoRA s0 mean $\pm$ std & 28.0$\pm$5.3 & 71.3$\pm$2.3 & 38.0$\pm$5.3 & 60.0$\pm$2.0 & 49.3$\pm$3.0 \\
299	\midrule
300	SDF $\lambda{=}0.1$ s0 (seed\,=\,7)   & 28 & 78 & 44 & 60 & 52.5 \\
301	SDF $\lambda{=}0.1$ s0 (seed\,=\,42)  & 18 & 78 & 42 & 72 & 52.5 \\
302	SDF $\lambda{=}0.1$ s0 (seed\,=\,123) & 26 & 82 & 38 & 68 & 53.5 \\
303	SDF $\lambda{=}0.1$ s0 (seed\,=\,256) & 28 & 74 & 32 & 58 & 48.0 \\
304	SDF $\lambda{=}0.1$ s0 mean $\pm$ std & 25.0$\pm$4.8 & 78.0$\pm$3.3 & 39.0$\pm$5.4 & 64.5$\pm$6.6 & 51.6$\pm$2.4 \\
305	\bottomrule
306	\end{tabular}
307	\end{table}
308	
309	Across three matched evaluation seeds (7, 42, 123), the SDF $\lambda{=}0.1$ condition yields higher aggregate CAR than LoRA-only in all cases ($\Delta$CAR\,=\,+1.5, +2.5, +5.5\,pp). Cross-seed CAR standard deviation is 2.0\,pp for LoRA and 0.9\,pp for SDF, both small relative to the within-seed per-task variation. The per-task ordering (CP highest, BBQ lowest) is preserved across all seeds and both conditions, reinforcing the conclusion that avoidance patterns reflect the spatial statistics of training demonstrations.
310	
311	
312	\section{Training Details}
313	\label{sec:appendix_training}
314	
315	\paragraph{Architecture.}
316	We use LoRA~\citep{hu2022lora} adapters injected into the PaliGemma vision encoder (rank 16, $\alpha$=16) and the action expert (rank 32, $\alpha$=32), following the configuration of OpenPi. The SDF decoder is a 4-layer MLP (hidden dimension 256) with skip connections, taking pooled suffix features (1024-d) and query points (3-d) as input. The end-effector extractor is a 2-layer MLP (1024 $\to$ 256 $\to$ 3).
317	
318	\paragraph{Training schedule.}
319	Training proceeds in two phases:
320	\begin{itemize}
321	    \item \textbf{Phase 1} (steps 0--5000): Backbone and LoRA parameters are frozen. Only the SDF decoder and EE extractor are trained, allowing them to learn meaningful representations before the policy adapts.
322	    \item \textbf{Phase 2} (steps 5000--30000): LoRA parameters are unfrozen with a 100-step gradient warmup ramp. All auxiliary heads continue training jointly with the policy.
323	\end{itemize}
324	
325	\paragraph{Hyperparameters.}
326	\begin{table}[h]
327	\centering
328	\caption{Training hyperparameters.}
329	\label{tab:hyperparams}
330	\begin{tabular}{ll}
331	\toprule
332	Parameter & Value \\
333	\midrule
334	Base model & Pi0.5 (OpenPi, $\sim$3.5B parameters) \\
335	Optimizer & AdamW \\
336	Learning rate & $2.5 \times 10^{-5}$ (cosine decay to $\mathrm{lr}/10$) \\
337	Warmup steps & 1000 \\
338	Batch size & 32 \\
339	Total steps & 30000 \\
340	$\lambda_\mathrm{sdf}$ & \{0.005, 0.01, 0.1\} \\
341	$\lambda_\mathrm{ee}$ & 0.01 \\
342	SDF query points per step & 64 \\
343	SDF clamp $\delta$ & 0.05 m \\
344	Eikonal weight & 0.1 \\
345	LoRA rank (vision) & 16 \\
346	LoRA rank (action) & 32 \\
347	Phase 1 duration & 5000 steps \\
348	\bottomrule
349	\end{tabular}
350	\end{table}
351	
352	\paragraph{Evaluation protocol.}
353	Each episode runs for at most 300 timesteps. The policy generates a 50-step action trajectory via flow matching and executes the first 5 steps before replanning. An episode terminates early upon task completion. Collision detection uses MuJoCo's built-in contact detection: any contact between the robot and a non-target object registers as a collision. For Pi0.5 evaluations, camera images are rotated 180$^\circ$ to match the pre-training viewpoint convention; this correction was verified to restore TSR from ${\sim}$5\% to ${\sim}$52\% while leaving CAR comparable. Oracle variants use 40 episodes per task (160 total) with a single seed; all other configurations use 50 episodes per task (200 total).
354	
355	\paragraph{Data.}
356	We use the SafeLIBERO object\_pudding suite with pre-computed SDF ground truth. SDF values are computed offline from the obstacle mesh using a dense $64^3$ voxel grid. During training, 64 query points are randomly sampled per step from this grid.
357	
358	\paragraph{Computational resources.}
359	All training and evaluation experiments are conducted on NVIDIA RTX PRO 6000 GPUs (96\,GB). Phase~1 (5K steps) takes approximately 6 hours on a single GPU; Phase~2 (25K steps) takes approximately 32 hours. Evaluation of 200 episodes requires approximately 4 hours. Across 100+ experiments (training runs, evaluations, oracle variants, and ablations), the total computational budget is approximately 700 GPU-hours.
360	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "542d8e21-32f7-41ca-850a-146799468747",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex",
      "content": "\\section{Displacement Distribution}\n\\label{sec:appendix_displacement}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\linewidth]{fig2_ee_displacement_distribution}\n\\caption{Displacement distribution across evaluation episodes. Pi0-family models (blue) cluster below 1\\,$\\mu$m, while Pi0.5 episodes (orange) exceed 200\\,mm. The five-order-of-magnitude gap makes $\\tau_d$ robust to any value in $[2, 200]$\\,mm.}\n\\label{fig:displacement}\n\\end{figure}\n\n\\section{Displacement Threshold Sensitivity Analysis}\n\\label{sec:appendix_threshold}\n\nTo validate the robustness of our displacement threshold $\\tau_d$, we evaluate the action-collapse rate across four orders of magnitude. Table~\\ref{tab:threshold_sensitivity} shows that the action-collapse pattern persists across all reasonable threshold choices: A1-LoRA exhibits near-total action collapse regardless of threshold, while Pi0.5+A1 maintains 0\\% action-collapse rate even at the most conservative setting.\n\n\\begin{table}[h]\n\\centering\n\\caption{Action-collapse rate (\\% of episodes with $d_\\mathrm{max} < \\tau_d$) across threshold values.}\n\\label{tab:threshold_sensitivity}\n\\begin{tabular}{lccc}\n\\toprule\n$\\tau_d$ & A1-LoRA (Pi0) & Pi0.5 Baseline & Pi0.5+A1 (SDF aux) \\\\\n\\midrule\n0.001 mm (1\\,$\\mu$m) & 73.9 & 0.0 & 0.0 \\\\\n0.1 mm  & 99.6 & 0.0 & 0.0 \\\\\n1.0 mm  & 100.0 & 0.0 & 0.0 \\\\\n10 mm   & 100.0 & 0.0 & 0.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe choice of $\\tau_d = 0.1$\\,mm represents a conservative threshold: displacement below this value is physically negligible in manipulation tasks where typical action magnitudes are 1--10\\,mm per step. Even at $\\tau_d = 1$\\,$\\mu$m, 73.9\\% of A1-LoRA safe episodes are classified as action-collapsed, while all Pi0.5 episodes remain above threshold at every level tested.\n\nTable~\\ref{tab:dfcar_threshold} extends this analysis to dfCAR across fine-tuned Pi0.5 configurations. All eight model-seed combinations yield identical dfCAR for $\\tau_d \\in [2, 200]$\\,mm. At $\\tau_d = 300$\\,mm, 0--2 episodes per seed fall below threshold (displacement 200--300\\,mm), causing $\\leq$0.5\\,pp deviation. Our conclusions hold across the entire tested range.\n\n\\begin{table}[h]\n\\centering\n\\caption{dfCAR (\\%) across displacement thresholds for fine-tuned Pi0.5 configurations ($n = 200$ episodes per seed). Values are identical across $\\tau_d \\in [2, 200]$\\,mm; at $\\tau_d = 300$\\,mm, at most 2 episodes are excluded.}\n\\label{tab:dfcar_threshold}\n\\vspace{2pt}\n\\footnotesize\n\\begin{tabular}{lcccccccc}\n\\toprule\n& \\multicolumn{8}{c}{$\\tau_d$ (mm)} \\\\\n\\cmidrule(lr){2-9}\nCondition & 2 & 5 & 10 & 20 & 50 & 100 & 200 & 300 \\\\\n\\midrule\nLoRA s0            & 56.5 & 56.5 & 56.5 & 56.5 & 56.5 & 56.5 & 56.5 & 56.5 \\\\\nLoRA s1            & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 \\\\\nSDF $\\lambda{=}0.005$ s0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.1 \\\\\nSDF $\\lambda{=}0.005$ s1 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 \\\\\nSDF $\\lambda{=}0.005$ s2 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.3 \\\\\nSDF $\\lambda{=}0.01$ s0  & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 \\\\\nSDF $\\lambda{=}0.01$ s1  & 57.5 & 57.5 & 57.5 & 57.5 & 57.5 & 57.5 & 57.5 & 57.1 \\\\\nSDF $\\lambda{=}0.01$ s2  & 54.5 & 54.5 & 54.5 & 54.5 & 54.5 & 54.5 & 54.5 & 54.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Per-Task TSR Breakdown}\\label{sec:appendix_tsr_pertask}\n\nTable~\\ref{tab:per_task_tsr} decomposes TSR by task for the avoidance source attribution experiments (Section~\\ref{sec:avoidance_source}). All tasks retain meaningful success rates after fine-tuning, with Chocolate Pudding most resilient and Orange Juice most affected.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-task TSR (\\%) at 30K training steps. Baseline reports the unified seed-7 re-evaluation (aggregate TSR\\,=\\,71.5\\%). LoRA-only reports 3-seed means (re-evaluated with unified seed-7 protocol); SDF conditions report 3-seed means.}\n\\label{tab:per_task_tsr}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nTask & Pi0.5 Base & LoRA-only & SDF $\\lambda{=}0.005$ & SDF $\\lambda{=}0.01$ \\\\\n & (seed\\,=\\,7) & (3 seeds) & (3 seeds) & (3 seeds) \\\\\n\\midrule\nOrange Juice      & 74.0 & 30.0 & 33.3 & 24.7 \\\\\nChoco.\\ Pudding   & 80.0 & 70.7 & 78.0 & 76.7 \\\\\nMilk              & 66.0 & 44.7 & 35.3 & 48.7 \\\\\nBBQ Sauce         & 66.0 & 60.7 & 69.3 & 65.3 \\\\\n\\midrule\nMean              & 71.5 & 51.5 & 54.0 & 53.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Per-Task CAR Breakdown}\\label{sec:appendix_pertask_car}\n\nTable~\\ref{tab:per_task_car} decomposes CAR by task for all fine-tuned conditions, supporting the claim that per-task ordering is preserved across SDF loss weights (\\S\\ref{sec:avoidance_source}). Chocolate Pudding is consistently highest and BBQ Sauce consistently lowest across all conditions, including $\\lambda = 0.1$. The intermediate tasks (Orange Juice and Milk) exchange rank between seeds but remain bounded by the extremes. This invariance indicates that avoidance patterns reflect the spatial statistics of collision-free demonstrations rather than geometric supervision.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-task CAR (\\%) at 30K steps. $\\lambda{=}0.005$, $\\lambda{=}0.01$, and $\\lambda{=}0.1$ report 3-seed means alongside individual seeds. Per-task ordering (CP highest, BBQ lowest) is preserved across all conditions.}\n\\label{tab:per_task_car}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nCondition & OJ & CP & Milk & BBQ & Agg. \\\\\n\\midrule\nLoRA s0 & 56 & 74 & 70 & 26 & 56.5 \\\\\nLoRA s1 & 54 & 68 & 72 & 16 & 52.5 \\\\\nLoRA s2 & 56 & 76 & 62 & 26 & 55.0 \\\\\nSDF $\\lambda{=}0.005$ (3-seed) & 54.0 & 72.7 & 71.3 & 20.0 & 54.5 \\\\\nSDF $\\lambda{=}0.01$ (3-seed) & 57.3 & 72.7 & 72.0 & 23.3 & 56.3 \\\\\nSDF $\\lambda{=}0.1$ s0 & 60 & 74 & 68 & 30 & 58.0 \\\\\nSDF $\\lambda{=}0.1$ s1 & 66 & 72 & 70 & 26 & 58.5 \\\\\nSDF $\\lambda{=}0.1$ s2 & 56 & 76 & 70 & 16 & 54.5 \\\\\nSDF $\\lambda{=}0.1$ (3-seed) & 60.7 & 74.0 & 69.3 & 24.0 & 57.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nFor the $\\lambda = 0.1$ condition, seed~1 records \\texttt{avg\\_max\\_obstacle\\_displacement} of 0.0553\\,m (per-task: OJ\\,=\\,0.033, CP\\,=\\,0.055, Milk\\,=\\,0.041, BBQ\\,=\\,0.093), comparable to other fine-tuned conditions and consistent with active manipulation rather than action-collapsed behavior.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{fig_pertask_car_fingerprint}\n\\caption{Per-task CAR fingerprint across conditions. Each bar shows the 3-seed mean; dots indicate individual seeds. The task ordering (chocolate\\_pudding highest, bbq\\_sauce lowest) is preserved across all $\\lambda$ values, confirming that avoidance patterns reflect the demonstration distribution rather than geometric supervision. LoRA-only: 3-seed mean.}\n\\label{fig:pertask_fingerprint}\n\\end{figure}\n\n\\section{Safe Success Rate Analysis}\\label{sec:appendix_ssr}\n\nTable~\\ref{tab:ssr} reports the Safe Success Rate (SSR\\,=\\,TSR\\,$\\cap$\\,CAR), the fraction of episodes achieving both task completion and collision avoidance. The SSR/TSR ratio quantifies the proportion of successful episodes that are also collision-free, controlling for task-completion rate.\n\n\\begin{table}[h]\n\\centering\n\\caption{SSR and SSR/TSR ratio across conditions. The ratio increase from 0.39 (baseline) to 0.51--0.60 (fine-tuned) indicates that CAR gains reflect learned safer execution, not reduced task exposure.}\n\\label{tab:ssr}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nCondition & TSR (\\%) & CAR (\\%) & SSR (\\%) & SSR/TSR \\\\\n\\midrule\nPi0.5 baseline & 71.5 & 28.5 & 28.0 & 0.39 \\\\\nLoRA-only (3 seeds) & 51.5 & 54.67 & 27.7 & 0.54 \\\\\nSDF $\\lambda{=}0.005$ (3 seeds) & 54.0 & 54.5 & 27.8 & 0.51 \\\\\nSDF $\\lambda{=}0.01$ (3 seeds) & 53.8 & 56.33 & 30.2 & 0.56 \\\\\nSDF $\\lambda{=}0.1$ (3 seeds) & 50.2 & 57.00 & 30.2 & 0.60 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Per-Task Oracle Analysis}\n\\label{sec:appendix_pertask}\n\\label{sec:appendix_pertask_oracle}\n\nTable~\\ref{tab:oracle_pertask} shows per-task CAR for oracle refinement. On task~1 (\\texttt{chocolate\\_pudding}), where the EE is the primary collision body and the LoRA baseline achieves only 46.0\\% CAR, Oracle-adaptive improves to 55.0\\% and Oracle-feature to 47.5\\%. On the remaining tasks, all oracle variants degrade: Oracle-adaptive reduces task~0 (\\texttt{orange\\_juice}) from 96.0\\% to 82.5\\% and task~2 (\\texttt{milk}) from 98.0\\% to 77.5\\%. The SDF gradient pushes the EE away from the nearest surface, but the resulting joint-space displacement rotates intermediate arm links into obstacle volumes.\n\nThe feature-space oracle fires on nearly every timestep (241.7 refinements/episode vs.\\ 14.2 for Cartesian variants) but with gradient magnitudes two orders of magnitude smaller (0.004--0.006 vs.\\ 0.18--0.49), and CAR (76.9\\%) shows no advantage despite 17$\\times$ more steps. The A3 learned SDF never triggers refinement (0 steps/episode), as its outputs avoid the activation threshold.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-task CAR (\\%) for oracle SDF refinement variants. EE-only refinement helps only on task~1 where the EE is the primary collision body; on other tasks it trades one collision site for another.}\n\\label{tab:oracle_pertask}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nMethod & Task 0 & Task 1 & Task 2 & Task 3 & Agg. \\\\\n\\midrule\nLoRA baseline & 96.0 & 46.0 & 98.0 & 88.0 & 82.0 \\\\\n\\midrule\nOracle-adaptive & 82.5 & 55.0 & 77.5 & 85.0 & 75.0 \\\\\nOracle-fixed & 85.0 & 50.0 & 77.5 & 80.0 & 73.1 \\\\\nOracle-feature & 90.0 & 47.5 & 82.5 & 87.5 & 76.9 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Null Distribution for SDF Loss Weight Analysis}\n\\label{sec:appendix_null}\n\nWe construct a null distribution by pooling the three LoRA-only seeds and three $\\lambda = 0.005$ seeds into six per-seed CAR measurements: 56.5\\% (LoRA s0, re-evaluated), 52.5\\% (LoRA s1), 55.0\\% (LoRA s2), 57.0\\% ($\\lambda{=}0.005$ s0), 54.0\\% ($\\lambda{=}0.005$ s1), 52.5\\% ($\\lambda{=}0.005$ s2), yielding mean 54.58\\% and standard deviation 1.93\\% (Bessel-corrected, $n{-}1 = 5$). We treat these as exchangeable because SDF at $\\lambda = 0.005$ produces no separation from LoRA-only. The $\\lambda = 0.01$ mean of 56.33\\% falls within $0.8\\sigma$ of this null ($p > 0.1$), consistent with seed-to-seed variation rather than a treatment effect. The $\\lambda = 0.1$ 30K mean of 57.00\\% (3 seeds: 58.0\\%, 58.5\\%, 54.5\\%) yields a two-tailed permutation $p = 0.131$ (one-tailed $p = 0.071$). The result is non-significant at conventional thresholds ($\\alpha = 0.05$).\n\nThe permutation test makes no distributional assumptions. Pooling the six null values $\\{56.5, 52.5, 55, 57, 54, 52.5\\}$ and three $\\lambda = 0.1$ values $\\{58, 58.5, 54.5\\}$ into nine measurements, we enumerate all $\\binom{9}{3} = 84$ three-element combinations and compute the fraction whose mean $\\geq 57.00$. Six combinations meet this threshold, yielding an exact one-tailed permutation $p = 6/84 \\approx 0.071$. For the two-tailed test, we additionally count combinations on the lower tail with equal or greater distance from the pooled mean, yielding $p = 11/84 \\approx 0.131$. With the third seed ($s_2 = 54.5\\%$) pulling the $\\lambda = 0.1$ mean from 58.25\\% (2 seeds) down to 57.00\\%, the marginal signal observed at $n = 2$ dissolves into seed-to-seed variance.\n\n\\paragraph{Alternative null construction (Null~A).}\nIf only the three LoRA-only seeds are used as the null pool ($\\{56.5, 52.5, 55.0\\}$), we obtain $\\binom{6}{3} = 20$ permutations for each comparison. For $\\lambda = 0.1$ (treatment mean 57.00\\%): one-tailed $p = 3/20 = 0.150$, two-tailed $p = 6/20 = 0.300$. For $\\lambda = 0.01$ (treatment mean 56.33\\%): one-tailed $p = 4/20 = 0.200$, two-tailed $p = 8/20 = 0.400$. Under the broader Null~B pool, $\\lambda = 0.01$ yields one-tailed $p = 10/84 \\approx 0.119$, two-tailed $p = 22/84 \\approx 0.262$. All tests are non-significant at $\\alpha = 0.05$; the narrower Null~A yields \\emph{larger} $p$-values because the LoRA-only pool already contains a high seed (56.5\\%), making the treatment means less extreme by comparison.\n\nA Phase~2 ablation reinforces this conclusion. Setting $\\lambda = 0$ during Phase~2 (steps 5K--18K), so that SDF supervision is active only during auxiliary head warmup (Phase~1, steps 0--5K), yields CAR of 58.0\\% at the 18K checkpoint (13K steps of Phase~2 training, single seed, s2).\\footnote{Full 30K training did not complete due to disk constraints; this result uses the last complete checkpoint at step 18K.} This value lies within the null range, indicating that SDF training produces no lasting behavioral effect on collision avoidance.\n\n\\section{Step-wise Checkpoint Analysis for \\texorpdfstring{$\\lambda = 0.1$}{lambda = 0.1}}\n\\label{sec:appendix_stepwise}\n\nTable~\\ref{tab:stepwise_lambda01} reports per-seed CAR at seven checkpoints for $\\lambda = 0.1$. Seeds~0 and~1 are available at 16K, 20K, 22K, and 30K; 24K--28K report seed-0 only; seed~2 is available at 30K only. The seed-0 curve shows no monotonic trend through 28K. At 30K, the addition of seed~2 (54.5\\%) pulls the three-seed mean to 57.00\\%, within the null band ($p = 0.131$).\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-seed CAR (\\%) at training checkpoints for $\\lambda = 0.1$ (200 episodes each). 24K--28K: seed-0 only. The 30K checkpoint includes all three seeds; the three-seed mean (57.00\\%) remains within the null band ($p = 0.131$, two-tailed permutation).}\n\\label{tab:stepwise_lambda01}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nCheckpoint & Seed 0 & Seed 1 & Seed 2 & Mean \\\\\n\\midrule\n16K steps & 55.5 & 56.0 & -- & 55.75 \\\\\n20K steps & 55.0 & 56.0 & -- & 55.5 \\\\\n22K steps & 60.5 & 56.5 & -- & 58.5 \\\\\n24K steps & 52.5 & -- & -- & -- \\\\\n26K steps & 53.5 & -- & -- & -- \\\\\n28K steps & 54.5 & -- & -- & -- \\\\\n30K steps & 58.0 & 58.5 & 54.5 & 57.00 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nIndividual seeds exhibit checkpoint-to-checkpoint CAR fluctuations of up to 8\\,pp (seed~0: 52.5--60.5\\%), larger than the cross-seed standard deviation at any fixed checkpoint ($\\leq$3\\,pp). This is consistent with binomial sampling noise at $n = 50$ episodes per task ($\\sigma \\approx 7$\\,pp per task for $p \\approx 0.5$). At 30K, the third seed ($s_2 = 54.5\\%$) falls well within the null range, pulling the three-seed mean to 57.00\\% and rendering the earlier two-seed departure non-significant ($p = 0.131$). The seed-averaged curve shows no monotonic trend, confirming that SDF loss weight does not produce a progressive training signal.\n\n\n\\section{Oracle SDF Refinement Details}\n\\label{sec:appendix_oracle}\n\nAll oracle variants replace the learned SDF decoder with ground-truth distance fields computed from the simulation geometry. Each is evaluated for 160 episodes (4 tasks $\\times$ 40).\n\n\\paragraph{Oracle-adaptive.} At each timestep, if the ground-truth SDF at the end-effector position falls below a safety margin, the action is adjusted by a step in the negative SDF gradient direction. The step size $\\alpha$ is scaled inversely with distance: smaller distances produce larger corrections. This mimics an adaptive potential field controller.\n\n\\paragraph{Oracle-fixed.} Identical to Oracle-adaptive except the step size is fixed at $\\alpha = 0.005$ regardless of distance. This isolates the effect of step-size adaptation from the refinement geometry.\n\n\\paragraph{Oracle-feature.} Instead of modifying the action directly in Cartesian space, this variant applies the SDF gradient in the policy's latent feature space via backpropagation. The gradient of the ground-truth SDF value with respect to the intermediate features is computed and used to perturb the features before the action head decodes them. This tests whether geometric corrections are more effective when applied in the model's learned representation space. In practice, the feature-space variant fires on nearly every timestep (241.7 refinements per episode vs.\\ 14.2 for Cartesian variants) but with gradient magnitudes two orders of magnitude smaller (0.004--0.006 vs.\\ 0.18--0.49 in action space).\n\n\n\\section{Cross-Scene Validation: spatial\\_bowl}\n\\label{sec:appendix_spatial_bowl}\n\nTo test whether the SDF redundancy finding generalizes beyond the primary \\texttt{object\\_pudding} scene, we replicate the core comparison on \\texttt{spatial\\_bowl}, a separate SafeLIBERO suite with a distinct obstacle layout (moka pot, wine bottle, milk carton, red coffee mug, yellow book). Both conditions use the same architecture, hyperparameters, and two-phase training schedule (30K steps), differing only in the training scene.\n\nTable~\\ref{tab:spatial_bowl} reports the results. The SDF condition ($\\lambda = 0.005$) yields CAR of 11.5\\% versus 12.0\\% for LoRA-only, a $-$0.5\\,pp difference well within the noise floor, indicating that SDF is essentially identical to LoRA-only on this scene. TSR is comparable across conditions (49.0\\% vs.\\ 51.5\\%). Both evaluations use a single training seed (seed~0) and a single evaluation seed (seed~7, 200 episodes), so statistical power is limited; nevertheless, the qualitative pattern---SDF failing to improve over LoRA-only---is consistent with the \\texttt{object\\_pudding} findings.\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-scene validation on \\texttt{spatial\\_bowl} (single training seed, 200 episodes, 30K checkpoint). The $-$0.5\\,pp CAR difference is well within noise, consistent with the SDF redundancy observed on \\texttt{object\\_pudding}.}\n\\label{tab:spatial_bowl}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nCondition & CAR (\\%) & TSR (\\%) \\\\\n\\midrule\nLoRA-only & 12.0 & 49.0 \\\\\nSDF $\\lambda{=}0.005$ & 11.5 & 51.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe substantially lower CAR on \\texttt{spatial\\_bowl} relative to \\texttt{object\\_pudding} (11--12\\% vs.\\ 54--57\\%) reflects the greater scene difficulty: \\texttt{spatial\\_bowl} places five cluttered obstacles around the workspace, making collision-free manipulation considerably harder. This difficulty affects both conditions equally, and the SDF condition performs comparably ($\\Delta$CAR\\,=\\,$-$0.5\\,pp, well within noise), reinforcing the conclusion that EE-only SDF auxiliary supervision does not produce a meaningful collision avoidance benefit beyond LoRA-only fine-tuning.\n\n\n\\section{Evaluation Seed Robustness}\n\\label{sec:appendix_eval_seed}\n\nTo verify that our conclusions are not artifacts of a particular evaluation seed, we re-evaluate the LoRA-only (s0) and SDF $\\lambda{=}0.1$ (s0) checkpoints under multiple evaluation seeds. Table~\\ref{tab:eval_seed_car} reports aggregate CAR and Table~\\ref{tab:eval_seed_tsr} reports aggregate TSR.\n\n\\begin{table}[h]\n\\centering\n\\caption{Aggregate CAR (\\%) across evaluation seeds (200 episodes each). The LoRA vs.\\ SDF $\\lambda{=}0.1$ ordering is preserved across all tested seeds, and per-task CAR fingerprints (CP highest, BBQ lowest) remain invariant.}\n\\label{tab:eval_seed_car}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\n& \\multicolumn{4}{c}{Per-task CAR (\\%)} & & \\\\\n\\cmidrule(lr){2-5}\nCondition (eval seed) & OJ & CP & Milk & BBQ & Agg. \\\\\n\\midrule\nLoRA s0 (seed\\,=\\,7)   & 56 & 74 & 70 & 26 & 56.5 \\\\\nLoRA s0 (seed\\,=\\,42)  & 60 & 70 & 68 & 28 & 56.5 \\\\\nLoRA s0 (seed\\,=\\,123) & 52 & 74 & 66 & 20 & 53.0 \\\\\nLoRA s0 mean $\\pm$ std & 56.0$\\pm$4.0 & 72.7$\\pm$2.3 & 68.0$\\pm$2.0 & 24.7$\\pm$4.2 & 55.3$\\pm$2.0 \\\\\n\\midrule\nSDF $\\lambda{=}0.1$ s0 (seed\\,=\\,7)   & 60 & 74 & 68 & 30 & 58.0 \\\\\nSDF $\\lambda{=}0.1$ s0 (seed\\,=\\,42)  & 64 & 74 & 74 & 24 & 59.0 \\\\\nSDF $\\lambda{=}0.1$ s0 (seed\\,=\\,123) & 62 & 76 & 74 & 22 & 58.5 \\\\\nSDF $\\lambda{=}0.1$ s0 (seed\\,=\\,256) & 60 & 72 & 66 & 30 & 57.0 \\\\\nSDF $\\lambda{=}0.1$ s0 mean $\\pm$ std & 61.5$\\pm$1.9 & 74.0$\\pm$1.6 & 70.5$\\pm$4.1 & 26.5$\\pm$4.1 & 58.1$\\pm$0.9 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{Aggregate TSR (\\%) across evaluation seeds. TSR varies more across seeds than CAR (seed\\,=\\,42 yields consistently lower TSR), but the relative ordering between LoRA and SDF is stable.}\n\\label{tab:eval_seed_tsr}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\n& \\multicolumn{4}{c}{Per-task TSR (\\%)} & & \\\\\n\\cmidrule(lr){2-5}\nCondition (eval seed) & OJ & CP & Milk & BBQ & Agg. \\\\\n\\midrule\nLoRA s0 (seed\\,=\\,7)   & 32 & 74 & 42 & 58 & 51.5 \\\\\nLoRA s0 (seed\\,=\\,42)  & 22 & 70 & 32 & 60 & 46.0 \\\\\nLoRA s0 (seed\\,=\\,123) & 30 & 70 & 40 & 62 & 50.5 \\\\\nLoRA s0 mean $\\pm$ std & 28.0$\\pm$5.3 & 71.3$\\pm$2.3 & 38.0$\\pm$5.3 & 60.0$\\pm$2.0 & 49.3$\\pm$3.0 \\\\\n\\midrule\nSDF $\\lambda{=}0.1$ s0 (seed\\,=\\,7)   & 28 & 78 & 44 & 60 & 52.5 \\\\\nSDF $\\lambda{=}0.1$ s0 (seed\\,=\\,42)  & 18 & 78 & 42 & 72 & 52.5 \\\\\nSDF $\\lambda{=}0.1$ s0 (seed\\,=\\,123) & 26 & 82 & 38 & 68 & 53.5 \\\\\nSDF $\\lambda{=}0.1$ s0 (seed\\,=\\,256) & 28 & 74 & 32 & 58 & 48.0 \\\\\nSDF $\\lambda{=}0.1$ s0 mean $\\pm$ std & 25.0$\\pm$4.8 & 78.0$\\pm$3.3 & 39.0$\\pm$5.4 & 64.5$\\pm$6.6 & 51.6$\\pm$2.4 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAcross three matched evaluation seeds (7, 42, 123), the SDF $\\lambda{=}0.1$ condition yields higher aggregate CAR than LoRA-only in all cases ($\\Delta$CAR\\,=\\,+1.5, +2.5, +5.5\\,pp). Cross-seed CAR standard deviation is 2.0\\,pp for LoRA and 0.9\\,pp for SDF, both small relative to the within-seed per-task variation. The per-task ordering (CP highest, BBQ lowest) is preserved across all seeds and both conditions, reinforcing the conclusion that avoidance patterns reflect the spatial statistics of training demonstrations.\n\n\n\\section{Training Details}\n\\label{sec:appendix_training}\n\n\\paragraph{Architecture.}\nWe use LoRA~\\citep{hu2022lora} adapters injected into the PaliGemma vision encoder (rank 16, $\\alpha$=16) and the action expert (rank 32, $\\alpha$=32), following the configuration of OpenPi. The SDF decoder is a 4-layer MLP (hidden dimension 256) with skip connections, taking pooled suffix features (1024-d) and query points (3-d) as input. The end-effector extractor is a 2-layer MLP (1024 $\\to$ 256 $\\to$ 3).\n\n\\paragraph{Training schedule.}\nTraining proceeds in two phases:\n\\begin{itemize}\n    \\item \\textbf{Phase 1} (steps 0--5000): Backbone and LoRA parameters are frozen. Only the SDF decoder and EE extractor are trained, allowing them to learn meaningful representations before the policy adapts.\n    \\item \\textbf{Phase 2} (steps 5000--30000): LoRA parameters are unfrozen with a 100-step gradient warmup ramp. All auxiliary heads continue training jointly with the policy.\n\\end{itemize}\n\n\\paragraph{Hyperparameters.}\n\\begin{table}[h]\n\\centering\n\\caption{Training hyperparameters.}\n\\label{tab:hyperparams}\n\\begin{tabular}{ll}\n\\toprule\nParameter & Value \\\\\n\\midrule\nBase model & Pi0.5 (OpenPi, $\\sim$3.5B parameters) \\\\\nOptimizer & AdamW \\\\\nLearning rate & $2.5 \\times 10^{-5}$ (cosine decay to $\\mathrm{lr}/10$) \\\\\nWarmup steps & 1000 \\\\\nBatch size & 32 \\\\\nTotal steps & 30000 \\\\\n$\\lambda_\\mathrm{sdf}$ & \\{0.005, 0.01, 0.1\\} \\\\\n$\\lambda_\\mathrm{ee}$ & 0.01 \\\\\nSDF query points per step & 64 \\\\\nSDF clamp $\\delta$ & 0.05 m \\\\\nEikonal weight & 0.1 \\\\\nLoRA rank (vision) & 16 \\\\\nLoRA rank (action) & 32 \\\\\nPhase 1 duration & 5000 steps \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Evaluation protocol.}\nEach episode runs for at most 300 timesteps. The policy generates a 50-step action trajectory via flow matching and executes the first 5 steps before replanning. An episode terminates early upon task completion. Collision detection uses MuJoCo's built-in contact detection: any contact between the robot and a non-target object registers as a collision. For Pi0.5 evaluations, camera images are rotated 180$^\\circ$ to match the pre-training viewpoint convention; this correction was verified to restore TSR from ${\\sim}$5\\% to ${\\sim}$52\\% while leaving CAR comparable. Oracle variants use 40 episodes per task (160 total) with a single seed; all other configurations use 50 episodes per task (200 total).\n\n\\paragraph{Data.}\nWe use the SafeLIBERO object\\_pudding suite with pre-computed SDF ground truth. SDF values are computed offline from the obstacle mesh using a dense $64^3$ voxel grid. During training, 64 query points are randomly sampled per step from this grid.\n\n\\paragraph{Computational resources.}\nAll training and evaluation experiments are conducted on NVIDIA RTX PRO 6000 GPUs (96\\,GB). Phase~1 (5K steps) takes approximately 6 hours on a single GPU; Phase~2 (25K steps) takes approximately 32 hours. Evaluation of 200 episodes requires approximately 4 hours. Across 100+ experiments (training runs, evaluations, oracle variants, and ablations), the total computational budget is approximately 700 GPU-hours.\n",
      "numLines": 360,
      "startLine": 1,
      "totalLines": 360
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Glob · `toolu_01LFWDPqWsTfChgZCGycFJ1e`</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "cf6a51ac-69f0-427c-b2ee-7ad8442ae951",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AspgegkKAc14hRyJk6zMou",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12904,
      "cache_read_input_tokens": 11451,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12904
      },
      "output_tokens": 30,
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

_source line 13 · 2026-05-28T06:50:21.329Z_

<details><summary>↩ Tool result · `toolu_01LFWDPqWsTfChgZCGycFJ1e`</summary>

```text
docs/paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "b7faca2e-df7c-49ef-bd1a-2f4107c844f0",
  "tool_use_result": {
    "filenames": [
      "docs/paper/references.bib"
    ],
    "durationMs": 12,
    "numFiles": 1,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 14_

<details><summary>Logged reasoning block</summary>

```text
Now I have all three files and found the bib file. Let me also search for "redundant" across these files and search for "20" patterns. Let me also start the web searches for the citations.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "429facc7-97da-4ad7-b9a5-9f8f43010f5c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PDpNVELYqKyE855yjsQLXF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13362,
      "cache_read_input_tokens": 24355,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13362
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

_source line 15_

文件已读取。现在搜索 "redundant" 和 "20" 模式，同时搜索需要补充的引用信息。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "fc8679f6-3f4a-48b6-b4a0-77547956c1fc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PDpNVELYqKyE855yjsQLXF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13362,
      "cache_read_input_tokens": 24355,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13362
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

_source line 16_

<details open><summary>🔧 Tool call — Grep · `toolu_015AXAMAJuUT44KrWpS3dwzi`</summary>

```json
{
  "pattern": "redundant",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "6630bcff-4dab-4f77-94d9-c95e89698215",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PDpNVELYqKyE855yjsQLXF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13362,
      "cache_read_input_tokens": 24355,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13362
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

_source line 17 · 2026-05-28T06:50:28.358Z_

<details><summary>↩ Tool result · `toolu_015AXAMAJuUT44KrWpS3dwzi`</summary>

```text
docs/paper/related_work.tex:12:[Omitted long matching line]
docs/paper/discussion.tex:20:[Omitted long matching line]
docs/paper/archive/analysis_claim3.tex:28:[Omitted long matching line]
docs/paper/archive/analysis_claim3.tex:72:\placeholder{Pending: $\lambda = 0.1$ results will determine whether SDF supervision shows dose-dependent effects at higher loss weights or remains redundant across the full $\lambda$ range. Final narrative deferred until experimental results are available.}
docs/paper/contingency_claim3.tex:19:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "96f53cad-8dfe-4317-a744-42679779593e",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/related_work.tex:12:[Omitted long matching line]\ndocs/paper/discussion.tex:20:[Omitted long matching line]\ndocs/paper/archive/analysis_claim3.tex:28:[Omitted long matching line]\ndocs/paper/archive/analysis_claim3.tex:72:\\placeholder{Pending: $\\lambda = 0.1$ results will determine whether SDF supervision shows dose-dependent effects at higher loss weights or remains redundant across the full $\\lambda$ range. Final narrative deferred until experimental results are available.}\ndocs/paper/contingency_claim3.tex:19:[Omitted long matching line]",
    "numLines": 5
  }
}
```

</details>

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — Grep · `toolu_01BLnaryg7v7jofZSKLnFkjr`</summary>

```json
{
  "pattern": "20.*\\\\\\\\times|\\\\$20",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "85ce4170-a0d6-4d0c-bcef-c0dad7f40b75",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PDpNVELYqKyE855yjsQLXF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13362,
      "cache_read_input_tokens": 24355,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13362
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

_source line 19 · 2026-05-28T06:50:29.530Z_

<details><summary>↩ Tool result · `toolu_01BLnaryg7v7jofZSKLnFkjr`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "d07d75f3-d810-43f8-9d25-91712949d4f8",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  }
}
```

</details>

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Grep · `toolu_01PTXmJTYtyRtLHsR1hZQzne`</summary>

```json
{
  "pattern": "20.*\\\\\\\\times|\\\\$20",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "ba4fe175-e0ff-4ec4-b97e-e9797b8e7d25",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PDpNVELYqKyE855yjsQLXF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13362,
      "cache_read_input_tokens": 24355,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13362
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

_source line 21 · 2026-05-28T06:50:30.458Z_

<details><summary>↩ Tool result · `toolu_01PTXmJTYtyRtLHsR1hZQzne`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "bf69d2db-01a6-4468-b3aa-73e9dd6c5879",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  }
}
```

</details>

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01QSPcm9ftBFNejFMt13MKtT`</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "93bbd80d-6fa0-4a4b-b3a9-f9bae0894919",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PDpNVELYqKyE855yjsQLXF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13362,
      "cache_read_input_tokens": 24355,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13362
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

_source line 23 · 2026-05-28T06:50:30.914Z_

<details><summary>↩ Tool result · `toolu_01QSPcm9ftBFNejFMt13MKtT`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
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
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "9ac20028-bd43-4f6a-bf57-db6c527314a7",
  "tool_use_result": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 24_

<details><summary>Logged reasoning block</summary>

```text
Let me search for the "20×" pattern more carefully in discussion.tex and appendix.tex, and also search for the redundant occurrences in appendix.tex specifically. Let me also do the web searches for HazardArena and VLA-Risk.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "86b2dd4d-3240-416a-9c5e-d84c2e586064",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TU68cK8rdUavKXXidsBHdm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1439,
      "cache_read_input_tokens": 37717,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1439
      },
      "output_tokens": 9,
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

_source line 25_

Let me search more carefully for the "20×" pattern and the appendix "redundant" occurrences, and do the web searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "7768e39d-3e1e-4329-a377-9447dbede69e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TU68cK8rdUavKXXidsBHdm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1439,
      "cache_read_input_tokens": 37717,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1439
      },
      "output_tokens": 9,
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

_source line 26_

<details open><summary>🔧 Tool call — Grep · `toolu_01BndTLwMHxQriiy6R6S4UPD`</summary>

```json
{
  "pattern": "20",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "ff514b4a-32e4-4436-bed7-2396015cb839",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TU68cK8rdUavKXXidsBHdm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1439,
      "cache_read_input_tokens": 37717,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1439
      },
      "output_tokens": 9,
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

_source line 27 · 2026-05-28T06:50:36.717Z_

<details><summary>↩ Tool result · `toolu_01BndTLwMHxQriiy6R6S4UPD`</summary>

```text
6:[Omitted long matching line]
14:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "1a2000c8-74cc-4366-a934-4b34ae920407",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "6:[Omitted long matching line]\n14:[Omitted long matching line]",
    "numLines": 2
  }
}
```

</details>

---

### Tool call

_source line 28_

<details open><summary>🔧 Tool call — Grep · `toolu_01JW842dTQWebR2qB6UW5Kq8`</summary>

```json
{
  "pattern": "redundan|absence of SDF|non-significance",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "507562a5-1fd2-4bab-b72c-8e1b452cfe04",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TU68cK8rdUavKXXidsBHdm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1439,
      "cache_read_input_tokens": 37717,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1439
      },
      "output_tokens": 9,
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

_source line 29 · 2026-05-28T06:50:38.133Z_

<details><summary>↩ Tool result · `toolu_01JW842dTQWebR2qB6UW5Kq8`</summary>

```text
229:To test whether the SDF redundancy finding generalizes beyond the primary \texttt{object\_pudding} scene, we replicate the core comparison on \texttt{spatial\_bowl}, a separate SafeLIBERO suite with a distinct obstacle layout (moka pot, wine bottle, milk carton, red coffee mug, yellow book). Both conditions use the same architecture, hyperparameters, and two-phase training schedule (30K steps), differing only in the training scene.
235:\caption{Cross-scene validation on \texttt{spatial\_bowl} (single training seed, 200 episodes, 30K checkpoint). The $-$0.5\,pp CAR difference is well within noise, consistent with the SDF redundancy observed on \texttt{object\_pudding}.}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "7c002fd6-e49d-43f0-9c70-217a94371368",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "229:To test whether the SDF redundancy finding generalizes beyond the primary \\texttt{object\\_pudding} scene, we replicate the core comparison on \\texttt{spatial\\_bowl}, a separate SafeLIBERO suite with a distinct obstacle layout (moka pot, wine bottle, milk carton, red coffee mug, yellow book). Both conditions use the same architecture, hyperparameters, and two-phase training schedule (30K steps), differing only in the training scene.\n235:\\caption{Cross-scene validation on \\texttt{spatial\\_bowl} (single training seed, 200 episodes, 30K checkpoint). The $-$0.5\\,pp CAR difference is well within noise, consistent with the SDF redundancy observed on \\texttt{object\\_pudding}.}",
    "numLines": 2
  }
}
```

</details>

---

### Tool call

_source line 30_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GgXcjnaURAg5T6v9o52wa9`</summary>

```json
{
  "query": "HazardArena arXiv 2604.12447 VLA safety evaluation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "65e2f453-ba2a-4492-ba41-a185e2fc26f5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TU68cK8rdUavKXXidsBHdm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1439,
      "cache_read_input_tokens": 37717,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1439
      },
      "output_tokens": 9,
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

_source line 31_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019PHdenZyZje8V8jbUAXUhu`</summary>

```json
{
  "query": "VLA-Risk OpenReview 2025 VLA robustness benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "16597927-7c68-4d44-aab8-ebcbd8077994",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TU68cK8rdUavKXXidsBHdm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1439,
      "cache_read_input_tokens": 37717,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1439
      },
      "output_tokens": 9,
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

_source line 32 · 2026-05-28T06:50:45.956Z_

<details><summary>↩ Tool result · `toolu_01GgXcjnaURAg5T6v9o52wa9`</summary>

```text
Web search results for query: "HazardArena arXiv 2604.12447 VLA safety evaluation"

Links: [{"title":"HazardArena: Evaluating Semantic Safety in Vision–Language–Action Models","url":"https://arxiv.org/html/2604.12447"},{"title":"[2604.12447] HazardArena: Evaluating Semantic Safety in Vision-Language-Action Models","url":"https://arxiv.org/abs/2604.12447"},{"title":"Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms","url":"https://arxiv.org/html/2604.23775v1"},{"title":"Concept-Based Dictionary Learning for Inference-Time Safety in Vision Language Action Models","url":"https://arxiv.org/pdf/2602.01834"},{"title":"[2604.23775] Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms","url":"https://arxiv.org/abs/2604.23775"},{"title":"SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Safe Reinforcement Learning","url":"https://arxiv.org/html/2503.03480v1"}]

Based on the search results, here's what I found about HazardArena (arXiv 2604.12447):

## Overview

HazardArena is a benchmark designed to evaluate semantic safety in VLA models under controlled settings that expose explicit semantic risk.

## Key Problem

Existing evaluations largely focus on action execution success, leaving action policies loosely coupled with visual-linguistic semantics. This decoupling exposes a systematic vulnerability whereby correct action execution may induce unsafe outcomes under semantic risk.

## Methodology

HazardArena is constructed from safe/unsafe twin scenarios that share matched objects, layouts, and action requirements, differing only in the semantic context that determines whether an action is unsafe.

## Key Findings

VLA models trained exclusively on safe scenarios often fail to behave safely when evaluated in their corresponding unsafe counterparts.

The paper was submitted to arXiv on April 14, 2026, and addresses an important gap in VLA safety evaluation by focusing on semantic understanding rather than just action execution accuracy.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "27ab648a-4526-4c86-a312-18b70f05ddb6",
  "tool_use_result": {
    "query": "HazardArena arXiv 2604.12447 VLA safety evaluation",
    "results": [
      {
        "tool_use_id": "srvtoolu_01S1Z4TBVdVMotir5CL3kvkt",
        "content": [
          {
            "title": "HazardArena: Evaluating Semantic Safety in Vision–Language–Action Models",
            "url": "https://arxiv.org/html/2604.12447"
          },
          {
            "title": "[2604.12447] HazardArena: Evaluating Semantic Safety in Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2604.12447"
          },
          {
            "title": "Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms",
            "url": "https://arxiv.org/html/2604.23775v1"
          },
          {
            "title": "Concept-Based Dictionary Learning for Inference-Time Safety in Vision Language Action Models",
            "url": "https://arxiv.org/pdf/2602.01834"
          },
          {
            "title": "[2604.23775] Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms",
            "url": "https://arxiv.org/abs/2604.23775"
          },
          {
            "title": "SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Safe Reinforcement Learning",
            "url": "https://arxiv.org/html/2503.03480v1"
          }
        ]
      },
      "Based on the search results, here's what I found about HazardArena (arXiv 2604.12447):\n\n## Overview\n\nHazardArena is a benchmark designed to evaluate semantic safety in VLA models under controlled settings that expose explicit semantic risk.\n\n## Key Problem\n\nExisting evaluations largely focus on action execution success, leaving action policies loosely coupled with visual-linguistic semantics. This decoupling exposes a systematic vulnerability whereby correct action execution may induce unsafe outcomes under semantic risk.\n\n## Methodology\n\nHazardArena is constructed from safe/unsafe twin scenarios that share matched objects, layouts, and action requirements, differing only in the semantic context that determines whether an action is unsafe.\n\n## Key Findings\n\nVLA models trained exclusively on safe scenarios often fail to behave safely when evaluated in their corresponding unsafe counterparts.\n\nThe paper was submitted to arXiv on April 14, 2026, and addresses an important gap in VLA safety evaluation by focusing on semantic understanding rather than just action execution accuracy."
    ],
    "durationSeconds": 7.333381285
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-28T06:50:46.085Z_

<details><summary>↩ Tool result · `toolu_019PHdenZyZje8V8jbUAXUhu`</summary>

```text
Web search results for query: "VLA-Risk OpenReview 2025 VLA robustness benchmark"

Links: [{"title":"VLA-Risk: Benchmarking Vision-Language-Action Models with Physical Robustness | OpenReview","url":"https://openreview.net/forum?id=31EjDFwFEe"},{"title":"In-depth Robustness Analysis for Vision-Language-Action Models | OpenReview","url":"https://openreview.net/forum?id=6mEfYoMRpF"},{"title":"On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations | OpenReview","url":"https://openreview.net/forum?id=cS6xizdYD5"},{"title":"VLA-RISK: BENCHMARKING VISION-LANGUAGE","url":"https://openreview.net/pdf/2b0044c5e9586d1b0dce44c7f3a73dbc43d13da0.pdf"},{"title":"What Can RL Bring to VLA Generalization? An Empirical Study | OpenReview","url":"https://openreview.net/forum?id=qmBMPInbZC"},{"title":"On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations","url":"https://arxiv.org/pdf/2510.00037"},{"title":"GitHub - OpenMOSS/VLABench: Official repo of VLABench, a large scale benchmark designed for fairly evaluating VLA, Embodied Agent, and VLMs. · GitHub","url":"https://github.com/OpenMOSS/VLABench"},{"title":"IN-DEPTH ROBUSTNESS ANALYSIS FOR VISION- ...","url":"https://openreview.net/pdf/bf4411a9941dccca2977e464f53188af2a03a6d3.pdf"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/pdf/2510.13626"},{"title":"VLA-RFT: Vision-Language-Action Reinforcement Fine-Tuning with Verified Rewards in World Simulators | OpenReview","url":"https://openreview.net/forum?id=Jaut99EHeu"}]

Based on the search results, I found information about VLA-Risk on OpenReview:

VLA-Risk is a benchmark for assessing the risks of Vision-Language-Action (VLA) models across different input modalities (such as image and instruction) and along three fundamental task dimensions: object, action, and space.

VLA-Risk spans 296 scenarios and 3784 episodes, covering diverse settings such as simple manipulation, semantic reasoning, and autonomous driving. 

The paper was submitted to ICLR 2026 on September 20, 2025 and modified on February 11, 2026. VLA models introduce new attack surfaces and vulnerabilities across both instruction execution and visual understanding.

The benchmark appears to address the gap in systematic evaluation of VLA robustness by providing a principled framework for analyzing vulnerabilities across multiple modalities and task dimensions. You can access the full paper at the OpenReview link: https://openreview.net/forum?id=31EjDFwFEe


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "ffbca8c9-d5a3-4af5-a4ab-a8d711d816bf",
  "tool_use_result": {
    "query": "VLA-Risk OpenReview 2025 VLA robustness benchmark",
    "results": [
      {
        "tool_use_id": "srvtoolu_0121XVqjCYCTduo3TNksCNeG",
        "content": [
          {
            "title": "VLA-Risk: Benchmarking Vision-Language-Action Models with Physical Robustness | OpenReview",
            "url": "https://openreview.net/forum?id=31EjDFwFEe"
          },
          {
            "title": "In-depth Robustness Analysis for Vision-Language-Action Models | OpenReview",
            "url": "https://openreview.net/forum?id=6mEfYoMRpF"
          },
          {
            "title": "On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations | OpenReview",
            "url": "https://openreview.net/forum?id=cS6xizdYD5"
          },
          {
            "title": "VLA-RISK: BENCHMARKING VISION-LANGUAGE",
            "url": "https://openreview.net/pdf/2b0044c5e9586d1b0dce44c7f3a73dbc43d13da0.pdf"
          },
          {
            "title": "What Can RL Bring to VLA Generalization? An Empirical Study | OpenReview",
            "url": "https://openreview.net/forum?id=qmBMPInbZC"
          },
          {
            "title": "On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations",
            "url": "https://arxiv.org/pdf/2510.00037"
          },
          {
            "title": "GitHub - OpenMOSS/VLABench: Official repo of VLABench, a large scale benchmark designed for fairly evaluating VLA, Embodied Agent, and VLMs. · GitHub",
            "url": "https://github.com/OpenMOSS/VLABench"
          },
          {
            "title": "IN-DEPTH ROBUSTNESS ANALYSIS FOR VISION- ...",
            "url": "https://openreview.net/pdf/bf4411a9941dccca2977e464f53188af2a03a6d3.pdf"
          },
          {
            "title": "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://arxiv.org/pdf/2510.13626"
          },
          {
            "title": "VLA-RFT: Vision-Language-Action Reinforcement Fine-Tuning with Verified Rewards in World Simulators | OpenReview",
            "url": "https://openreview.net/forum?id=Jaut99EHeu"
          }
        ]
      },
      "Based on the search results, I found information about VLA-Risk on OpenReview:\n\nVLA-Risk is a benchmark for assessing the risks of Vision-Language-Action (VLA) models across different input modalities (such as image and instruction) and along three fundamental task dimensions: object, action, and space.\n\nVLA-Risk spans 296 scenarios and 3784 episodes, covering diverse settings such as simple manipulation, semantic reasoning, and autonomous driving. \n\nThe paper was submitted to ICLR 2026 on September 20, 2025 and modified on February 11, 2026. VLA models introduce new attack surfaces and vulnerabilities across both instruction execution and visual understanding.\n\nThe benchmark appears to address the gap in systematic evaluation of VLA robustness by providing a principled framework for analyzing vulnerabilities across multiple modalities and task dimensions. You can access the full paper at the OpenReview link: https://openreview.net/forum?id=31EjDFwFEe"
    ],
    "durationSeconds": 7.183466259999998
  }
}
```

</details>

---

### Assistant

_source line 34_

<details><summary>Logged reasoning block</summary>

```text
Now let me get more details about both papers. Let me fetch the actual arXiv page for HazardArena to get authors.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "ea884eb7-552a-49b0-818c-86c40c17315d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PCiJ2ic3ZqDvRxrUa6Z9Lg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2142,
      "cache_read_input_tokens": 39156,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2142
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

_source line 35_

Let me get author details for both papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "eeb99716-ca67-41e4-8c25-abcbff4f21ff",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PCiJ2ic3ZqDvRxrUa6Z9Lg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2142,
      "cache_read_input_tokens": 39156,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2142
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

_source line 36_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RdQqZtxVv6ncpoenRRPUPJ`</summary>

```json
{
  "query": "HazardArena arXiv 2604.12447 authors list 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "abee6375-ac26-4aaf-b965-53fbefa86ee0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PCiJ2ic3ZqDvRxrUa6Z9Lg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2142,
      "cache_read_input_tokens": 39156,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2142
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

_source line 37_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015zHMKD79wcDWJqY7A95KTm`</summary>

```json
{
  "query": "VLA-Risk benchmarking vision-language-action physical robustness authors OpenReview ICLR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "a61068c7-113a-401a-8bf2-fb0964797805",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PCiJ2ic3ZqDvRxrUa6Z9Lg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2142,
      "cache_read_input_tokens": 39156,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2142
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

_source line 38_

<details open><summary>🔧 Tool call — Read · `toolu_011x9BgsWTyajVy8tcrm6BnK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "43bc447b-5ae0-46a0-a539-947361103307",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PCiJ2ic3ZqDvRxrUa6Z9Lg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2142,
      "cache_read_input_tokens": 39156,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2142
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

_source line 39 · 2026-05-28T06:50:50.862Z_

<details><summary>↩ Tool result · `toolu_011x9BgsWTyajVy8tcrm6BnK`</summary>

```text
1	% The Safety Illusion — References
2	% Analysis paper on fake safety in VLA collision avoidance evaluation
3	% Generated: 2026-05-24
4	
5	% ===== VLA Foundation Models =====
6	
7	@article{black2024pi0,
8	  title={$\pi_0$: A Vision-Language-Action Flow Model for General Robot Control},
9	  author={Black, Kevin and Brown, Noah and Driess, Danny and Esmail, Adnan and Equi, Michael and Finn, Chelsea and Fusai, Niccolo and Groom, Lachy and Hausman, Karol and Ichter, Brian and others},
10	  journal={arXiv preprint arXiv:2410.24164},
11	  year={2024}
12	}
13	
14	@inproceedings{kim2024openvla,
15	  title={{OpenVLA}: An Open-Source Vision-Language-Action Model},
16	  author={Kim, Moo Jin and Pertsch, Karl and Karamcheti, Siddharth and Xiao, Ted and Balakrishna, Ashwin and Nair, Suraj and Rafailov, Rafael and Foster, Ethan and Lam, Grace and Nasiriany, Mohan and others},
17	  booktitle={Conference on Robot Learning (CoRL)},
18	  year={2024}
19	}
20	
21	@inproceedings{brohan2023rt2,
22	  title={{RT-2}: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},
23	  author={Brohan, Anthony and Brown, Noah and Carbajal, Justice and Chebotar, Yevgen and Chen, Xi and Choromanski, Krzysztof and Ding, Tianli and Driess, Danny and Dubey, Avinava and Finn, Chelsea and others},
24	  booktitle={Conference on Robot Learning (CoRL)},
25	  year={2023}
26	}
27	
28	% ===== Collision-Aware VLA Methods =====
29	
30	@article{hu2025vlsa,
31	  title={{VLSA}: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer},
32	  author={Hu, Songqiao and Liu, Zeyi and Liu, Shuang and Cen, Jun and Meng, Zihan and He, Xiao},
33	  journal={arXiv preprint arXiv:2512.11891},
34	  year={2025}
35	}
36	
37	@inproceedings{zhang2025safevla,
38	  title={{SafeVLA}: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning},
39	  author={Zhang, Borong and Zhang, Yuhao and Ji, Jiaming and Lei, Yingshan and Dai, Josef and Chen, Yuanpei and Yang, Yaodong},
40	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
41	  year={2025}
42	}
43	
44	@article{cofreeevla2026,
45	  title={{CoFreeVLA}: Collision-Free Dual-Arm Manipulation via Vision-Language-Action Model and Risk Estimation},
46	  author={Zhai, Xuanran and Ou, Binkai and Yu, Qiaojun and Hao, Ce and Liu, Yaohua},
47	  journal={arXiv preprint arXiv:2601.21712},
48	  year={2026}
49	}
50	
51	@article{spalter2024ikinqp,
52	  title={Towards Online Safety Corrections for Robotic Manipulation Policies},
53	  author={Spalter, Ariana and Roberts, Mark and Hiatt, Laura M.},
54	  journal={arXiv preprint arXiv:2409.08233},
55	  year={2024}
56	}
57	
58	@inproceedings{li2024langguided,
59	  title={Language-Guided Object-Centric Diffusion Policy for Collision-Aware Robotic Manipulation},
60	  author={Li, Hang and Feng, Qian and Zheng, Zhi and Feng, Jianxiang and Chen, Zhaopeng and Knoll, Alois},
61	  booktitle={IEEE International Conference on Robotics and Automation (ICRA)},
62	  year={2025}
63	}
64	
65	@article{yang2025cape,
66	  title={{CAPE}: Context-Aware Diffusion Policy Via Proximal Mode Expansion for Collision Avoidance},
67	  author={Yang, Rui Heng and Zhao, Xuan and Brunswic, Leo Maxime and Alban, Montgomery and Clemente, Mateo and Cao, Tongtong and Jin, Jun and Rasouli, Amir},
68	  journal={arXiv preprint arXiv:2511.22773},
69	  year={2025}
70	}
71	
72	% ===== Safety in Diffusion Planning =====
73	
74	@inproceedings{xiao2025safediffuser,
75	  title={{SafeDiffuser}: Safe Planning with Diffusion Probabilistic Models},
76	  author={Xiao, Wei and Wang, Tsun-Hsuan and Gan, Chuang and Hasani, Ramin and Lechner, Mathias and Rus, Daniela},
77	  booktitle={International Conference on Learning Representations (ICLR)},
78	  year={2025}
79	}
80	
81	% ===== SDF in Robotics =====
82	
83	@inproceedings{park2019deepsdf,
84	  title={{DeepSDF}: Learning Continuous Signed Distance Functions for Shape Representation},
85	  author={Park, Jeong Joon and Florence, Peter and Straub, Julian and Newcombe, Richard and Lovegrove, Steven},
86	  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
87	  year={2019}
88	}
89	
90	@inproceedings{ortiz2022isdf,
91	  title={{iSDF}: Real-Time Neural Signed Distance Fields for Robot Perception},
92	  author={Ortiz, Joseph and Clegg, Alexander and Dong, Jing and Sucar, Edgar and Novotny, David and Zollh{\"o}fer, Michael and Mukadam, Mustafa},
93	  booktitle={Robotics: Science and Systems (RSS)},
94	  year={2022}
95	}
96	
97	@article{zhi2021diffco,
98	  title={{DiffCo}: Auto-Differentiable Proxy Collision Detection with Multi-class Labels for Safety-Aware Trajectory Optimization},
99	  author={Zhi, Yuheng and Das, Nikhil and Yip, Michael},
100	  journal={IEEE Transactions on Robotics},
101	  volume={38},
102	  number={5},
103	  pages={2668--2685},
104	  year={2022}
105	}
106	
107	@inproceedings{huang2023voxposer,
108	  title={{VoxPoser}: Composable {3D} Value Maps for Robotic Manipulation with Language Models},
109	  author={Huang, Wenlong and Wang, Chen and Zhang, Ruohan and Li, Yunzhu and Wu, Jiajun and Fei-Fei, Li},
110	  booktitle={Conference on Robot Learning (CoRL)},
111	  year={2023}
112	}
113	
114	% ===== Benchmarks and Training =====
115	
116	@inproceedings{liu2023libero,
117	  title={{LIBERO}: Benchmarking Knowledge Transfer for Lifelong Robot Learning},
118	  author={Liu, Bo and Zhu, Yifeng and Gao, Chongkai and Feng, Yihao and Liu, Qiang and Zhu, Yuke and Stone, Peter},
119	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
120	  year={2023}
121	}
122	
123	@inproceedings{lipman2023flow,
124	  title={Flow Matching for Generative Modeling},
125	  author={Lipman, Yaron and Chen, Ricky T. Q. and Ben-Hamu, Heli and Nickel, Maximilian and Le, Matt},
126	  booktitle={International Conference on Learning Representations (ICLR)},
127	  year={2023}
128	}
129	
130	% ===== Evaluation Reliability =====
131	
132	@inproceedings{gururangan2018annotation,
133	  title={Annotation Artifacts in Natural Language Inference Data},
134	  author={Gururangan, Suchin and Swayamdipta, Swabha and Levy, Omer and Schwartz, Roy and Bowman, Samuel and Smith, Noah A.},
135	  booktitle={Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},
136	  year={2018}
137	}
138	
139	@inproceedings{karwowski2024goodhart,
140	  title={Goodhart's Law in Reinforcement Learning},
141	  author={Karwowski, Jacek and Hayman, Oliver and Bai, Xingjian and Kiendlhofer, Klaus and Griffin, Charlie and Sherburn, Joar},
142	  booktitle={International Conference on Learning Representations (ICLR)},
143	  year={2024}
144	}
145	
146	% ===== Diffusion Policy =====
147	
148	@inproceedings{chi2023diffusionpolicy,
149	  title={Diffusion Policy: Visuomotor Policy Learning via Action Diffusion},
150	  author={Chi, Cheng and Feng, Siyuan and Du, Yilun and Xu, Zhenjia and Cousineau, Eric and Burchfiel, Benjamin and Song, Shuran},
151	  booktitle={Robotics: Science and Systems (RSS)},
152	  year={2023}
153	}
154	
155	% ===== Configuration/Robot-Body SDF =====
156	
157	@inproceedings{li2024cdf,
158	  title={Configuration Space Distance Fields for Manipulation Planning},
159	  author={Li, Yiming and Chi, Xuemin and Razmjoo, Amirreza and Calinon, Sylvain},
160	  booktitle={Robotics: Science and Systems (RSS)},
161	  year={2024}
162	}
163	
164	@inproceedings{li2024rdf,
165	  title={Representing Robot Geometry as Distance Fields: Applications to Whole-body Manipulation},
166	  author={Li, Yiming and Zhang, Yan and Razmjoo, Amirreza and Calinon, Sylvain},
167	  booktitle={IEEE International Conference on Robotics and Automation (ICRA)},
168	  year={2024}
169	}
170	
171	% ===== SDF in Robotics (additional) =====
172	
173	@inproceedings{vasilopoulos2023ramp,
174	  title={{RAMP}: Hierarchical Reactive Motion Planning for Manipulation Tasks Using Implicit Signed Distance Functions},
175	  author={Vasilopoulos, Vasileios and Garg, Suveer and Piacenza, Pedro and Huh, Jinwook and Isler, Volkan},
176	  booktitle={IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)},
177	  year={2023}
178	}
179	
180	@article{chen2026cssdfnet,
181	  title={{CSSDF-Net}: Safe Motion Planning Based on Neural Implicit Representations of Configuration Space Distance Field},
182	  author={Chen, Haohua and Zhou, Yixuan and Zhou, Yifan and Wang, Hesheng},
183	  journal={arXiv preprint arXiv:2603.18669},
184	  year={2026}
185	}
186	
187	@article{jacquet2025neuralnmpc,
188	  title={Neural {NMPC} through Signed Distance Field Encoding for Collision Avoidance},
189	  author={Jacquet, Martin and Harms, Marvin and Alexis, Kostas},
190	  journal={The International Journal of Robotics Research},
191	  year={2025}
192	}
193	
194	% ===== 3D-Aware VLA Methods =====
195	
196	@article{depthvla2025,
197	  title={{DepthVLA}: Enhancing Vision-Language-Action Models with Depth-Aware Spatial Reasoning},
198	  author={Yuan, Tianyuan and Liu, Yicheng and Lu, Chenhao and Chen, Zhuoguang and Jiang, Tao and Zhao, Hang},
199	  journal={arXiv preprint arXiv:2510.13375},
200	  year={2025}
201	}
202	
203	@article{li2025qdepth,
204	  title={{QDepth-VLA}: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models},
205	  author={Li, Yixuan and Chen, Yuhui and Zhou, Mingcai and Li, Haoran and Zhang, Zhengtao and Zhao, Dongbin},
206	  journal={arXiv preprint arXiv:2510.14836},
207	  year={2025}
208	}
209	
210	@article{li2025spatialforcing,
211	  title={Spatial Forcing: Implicit Spatial Representation Alignment for Vision-Language-Action Model},
212	  author={Li, Fuhao and Song, Wenxuan and Zhao, Han and Wang, Jingbo and Ding, Pengxiang and Wang, Donglin and Zeng, Long and Li, Haoang},
213	  journal={arXiv preprint arXiv:2510.12276},
214	  year={2025}
215	}
216	
217	% ===== Parameter-Efficient Fine-Tuning =====
218	
219	@inproceedings{hu2022lora,
220	  author    = {Hu, Edward J. and Shen, Yelong and Wallis, Phillip and Allen-Zhu, Zeyuan and Li, Yuanzhi and Wang, Shean and Wang, Lu and Chen, Weizhu},
221	  title     = {{LoRA}: Low-Rank Adaptation of Large Language Models},
222	  booktitle = {International Conference on Learning Representations (ICLR)},
223	  year      = {2022},
224	}
225	
226	% ===== VLA Safety Survey =====
227	
228	@article{li2026vlasafety,
229	  title={Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms},
230	  author={Li, Qi and Yin, Bo and Huang, Weiqi and Liu, Ruhao and Zou, Bojun and Yu, Runpeng and Ye, Jingwen and Yu, Weihao and Wang, Xinchao},
231	  journal={arXiv preprint arXiv:2604.23775},
232	  year={2026}
233	}
234	
235	% ===== Action Collapse =====
236	
237	@article{dong2025conditioning,
238	  title={Conditioning Matters: Training Diffusion Policies is Faster Than You Think},
239	  author={Dong, Zibin and Liu, Yicheng and Li, Yinchuan and Zhao, Hang and Hao, Jianye},
240	  journal={arXiv preprint arXiv:2505.11123},
241	  year={2025}
242	}
243	
244	% ===== Evaluation Methodology =====
245	
246	@article{snyder2026beyond,
247	  title={Beyond Binary Success: Sample-Efficient and Statistically Rigorous Robot Policy Comparison},
248	  author={Snyder, David and Badithela, Apurva and Matni, Nikolai and Pappas, George and Majumdar, Anirudha and Itkina, Masha and Nishimura, Haruki},
249	  journal={arXiv preprint arXiv:2603.13616},
250	  year={2026}
251	}
252	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "209ba5ab-0679-45af-9d37-e35cce0bcfc5",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/references.bib",
      "content": "% The Safety Illusion — References\n% Analysis paper on fake safety in VLA collision avoidance evaluation\n% Generated: 2026-05-24\n\n% ===== VLA Foundation Models =====\n\n@article{black2024pi0,\n  title={$\\pi_0$: A Vision-Language-Action Flow Model for General Robot Control},\n  author={Black, Kevin and Brown, Noah and Driess, Danny and Esmail, Adnan and Equi, Michael and Finn, Chelsea and Fusai, Niccolo and Groom, Lachy and Hausman, Karol and Ichter, Brian and others},\n  journal={arXiv preprint arXiv:2410.24164},\n  year={2024}\n}\n\n@inproceedings{kim2024openvla,\n  title={{OpenVLA}: An Open-Source Vision-Language-Action Model},\n  author={Kim, Moo Jin and Pertsch, Karl and Karamcheti, Siddharth and Xiao, Ted and Balakrishna, Ashwin and Nair, Suraj and Rafailov, Rafael and Foster, Ethan and Lam, Grace and Nasiriany, Mohan and others},\n  booktitle={Conference on Robot Learning (CoRL)},\n  year={2024}\n}\n\n@inproceedings{brohan2023rt2,\n  title={{RT-2}: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},\n  author={Brohan, Anthony and Brown, Noah and Carbajal, Justice and Chebotar, Yevgen and Chen, Xi and Choromanski, Krzysztof and Ding, Tianli and Driess, Danny and Dubey, Avinava and Finn, Chelsea and others},\n  booktitle={Conference on Robot Learning (CoRL)},\n  year={2023}\n}\n\n% ===== Collision-Aware VLA Methods =====\n\n@article{hu2025vlsa,\n  title={{VLSA}: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer},\n  author={Hu, Songqiao and Liu, Zeyi and Liu, Shuang and Cen, Jun and Meng, Zihan and He, Xiao},\n  journal={arXiv preprint arXiv:2512.11891},\n  year={2025}\n}\n\n@inproceedings{zhang2025safevla,\n  title={{SafeVLA}: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning},\n  author={Zhang, Borong and Zhang, Yuhao and Ji, Jiaming and Lei, Yingshan and Dai, Josef and Chen, Yuanpei and Yang, Yaodong},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2025}\n}\n\n@article{cofreeevla2026,\n  title={{CoFreeVLA}: Collision-Free Dual-Arm Manipulation via Vision-Language-Action Model and Risk Estimation},\n  author={Zhai, Xuanran and Ou, Binkai and Yu, Qiaojun and Hao, Ce and Liu, Yaohua},\n  journal={arXiv preprint arXiv:2601.21712},\n  year={2026}\n}\n\n@article{spalter2024ikinqp,\n  title={Towards Online Safety Corrections for Robotic Manipulation Policies},\n  author={Spalter, Ariana and Roberts, Mark and Hiatt, Laura M.},\n  journal={arXiv preprint arXiv:2409.08233},\n  year={2024}\n}\n\n@inproceedings{li2024langguided,\n  title={Language-Guided Object-Centric Diffusion Policy for Collision-Aware Robotic Manipulation},\n  author={Li, Hang and Feng, Qian and Zheng, Zhi and Feng, Jianxiang and Chen, Zhaopeng and Knoll, Alois},\n  booktitle={IEEE International Conference on Robotics and Automation (ICRA)},\n  year={2025}\n}\n\n@article{yang2025cape,\n  title={{CAPE}: Context-Aware Diffusion Policy Via Proximal Mode Expansion for Collision Avoidance},\n  author={Yang, Rui Heng and Zhao, Xuan and Brunswic, Leo Maxime and Alban, Montgomery and Clemente, Mateo and Cao, Tongtong and Jin, Jun and Rasouli, Amir},\n  journal={arXiv preprint arXiv:2511.22773},\n  year={2025}\n}\n\n% ===== Safety in Diffusion Planning =====\n\n@inproceedings{xiao2025safediffuser,\n  title={{SafeDiffuser}: Safe Planning with Diffusion Probabilistic Models},\n  author={Xiao, Wei and Wang, Tsun-Hsuan and Gan, Chuang and Hasani, Ramin and Lechner, Mathias and Rus, Daniela},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2025}\n}\n\n% ===== SDF in Robotics =====\n\n@inproceedings{park2019deepsdf,\n  title={{DeepSDF}: Learning Continuous Signed Distance Functions for Shape Representation},\n  author={Park, Jeong Joon and Florence, Peter and Straub, Julian and Newcombe, Richard and Lovegrove, Steven},\n  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  year={2019}\n}\n\n@inproceedings{ortiz2022isdf,\n  title={{iSDF}: Real-Time Neural Signed Distance Fields for Robot Perception},\n  author={Ortiz, Joseph and Clegg, Alexander and Dong, Jing and Sucar, Edgar and Novotny, David and Zollh{\\\"o}fer, Michael and Mukadam, Mustafa},\n  booktitle={Robotics: Science and Systems (RSS)},\n  year={2022}\n}\n\n@article{zhi2021diffco,\n  title={{DiffCo}: Auto-Differentiable Proxy Collision Detection with Multi-class Labels for Safety-Aware Trajectory Optimization},\n  author={Zhi, Yuheng and Das, Nikhil and Yip, Michael},\n  journal={IEEE Transactions on Robotics},\n  volume={38},\n  number={5},\n  pages={2668--2685},\n  year={2022}\n}\n\n@inproceedings{huang2023voxposer,\n  title={{VoxPoser}: Composable {3D} Value Maps for Robotic Manipulation with Language Models},\n  author={Huang, Wenlong and Wang, Chen and Zhang, Ruohan and Li, Yunzhu and Wu, Jiajun and Fei-Fei, Li},\n  booktitle={Conference on Robot Learning (CoRL)},\n  year={2023}\n}\n\n% ===== Benchmarks and Training =====\n\n@inproceedings{liu2023libero,\n  title={{LIBERO}: Benchmarking Knowledge Transfer for Lifelong Robot Learning},\n  author={Liu, Bo and Zhu, Yifeng and Gao, Chongkai and Feng, Yihao and Liu, Qiang and Zhu, Yuke and Stone, Peter},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2023}\n}\n\n@inproceedings{lipman2023flow,\n  title={Flow Matching for Generative Modeling},\n  author={Lipman, Yaron and Chen, Ricky T. Q. and Ben-Hamu, Heli and Nickel, Maximilian and Le, Matt},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2023}\n}\n\n% ===== Evaluation Reliability =====\n\n@inproceedings{gururangan2018annotation,\n  title={Annotation Artifacts in Natural Language Inference Data},\n  author={Gururangan, Suchin and Swayamdipta, Swabha and Levy, Omer and Schwartz, Roy and Bowman, Samuel and Smith, Noah A.},\n  booktitle={Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},\n  year={2018}\n}\n\n@inproceedings{karwowski2024goodhart,\n  title={Goodhart's Law in Reinforcement Learning},\n  author={Karwowski, Jacek and Hayman, Oliver and Bai, Xingjian and Kiendlhofer, Klaus and Griffin, Charlie and Sherburn, Joar},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2024}\n}\n\n% ===== Diffusion Policy =====\n\n@inproceedings{chi2023diffusionpolicy,\n  title={Diffusion Policy: Visuomotor Policy Learning via Action Diffusion},\n  author={Chi, Cheng and Feng, Siyuan and Du, Yilun and Xu, Zhenjia and Cousineau, Eric and Burchfiel, Benjamin and Song, Shuran},\n  booktitle={Robotics: Science and Systems (RSS)},\n  year={2023}\n}\n\n% ===== Configuration/Robot-Body SDF =====\n\n@inproceedings{li2024cdf,\n  title={Configuration Space Distance Fields for Manipulation Planning},\n  author={Li, Yiming and Chi, Xuemin and Razmjoo, Amirreza and Calinon, Sylvain},\n  booktitle={Robotics: Science and Systems (RSS)},\n  year={2024}\n}\n\n@inproceedings{li2024rdf,\n  title={Representing Robot Geometry as Distance Fields: Applications to Whole-body Manipulation},\n  author={Li, Yiming and Zhang, Yan and Razmjoo, Amirreza and Calinon, Sylvain},\n  booktitle={IEEE International Conference on Robotics and Automation (ICRA)},\n  year={2024}\n}\n\n% ===== SDF in Robotics (additional) =====\n\n@inproceedings{vasilopoulos2023ramp,\n  title={{RAMP}: Hierarchical Reactive Motion Planning for Manipulation Tasks Using Implicit Signed Distance Functions},\n  author={Vasilopoulos, Vasileios and Garg, Suveer and Piacenza, Pedro and Huh, Jinwook and Isler, Volkan},\n  booktitle={IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)},\n  year={2023}\n}\n\n@article{chen2026cssdfnet,\n  title={{CSSDF-Net}: Safe Motion Planning Based on Neural Implicit Representations of Configuration Space Distance Field},\n  author={Chen, Haohua and Zhou, Yixuan and Zhou, Yifan and Wang, Hesheng},\n  journal={arXiv preprint arXiv:2603.18669},\n  year={2026}\n}\n\n@article{jacquet2025neuralnmpc,\n  title={Neural {NMPC} through Signed Distance Field Encoding for Collision Avoidance},\n  author={Jacquet, Martin and Harms, Marvin and Alexis, Kostas},\n  journal={The International Journal of Robotics Research},\n  year={2025}\n}\n\n% ===== 3D-Aware VLA Methods =====\n\n@article{depthvla2025,\n  title={{DepthVLA}: Enhancing Vision-Language-Action Models with Depth-Aware Spatial Reasoning},\n  author={Yuan, Tianyuan and Liu, Yicheng and Lu, Chenhao and Chen, Zhuoguang and Jiang, Tao and Zhao, Hang},\n  journal={arXiv preprint arXiv:2510.13375},\n  year={2025}\n}\n\n@article{li2025qdepth,\n  title={{QDepth-VLA}: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models},\n  author={Li, Yixuan and Chen, Yuhui and Zhou, Mingcai and Li, Haoran and Zhang, Zhengtao and Zhao, Dongbin},\n  journal={arXiv preprint arXiv:2510.14836},\n  year={2025}\n}\n\n@article{li2025spatialforcing,\n  title={Spatial Forcing: Implicit Spatial Representation Alignment for Vision-Language-Action Model},\n  author={Li, Fuhao and Song, Wenxuan and Zhao, Han and Wang, Jingbo and Ding, Pengxiang and Wang, Donglin and Zeng, Long and Li, Haoang},\n  journal={arXiv preprint arXiv:2510.12276},\n  year={2025}\n}\n\n% ===== Parameter-Efficient Fine-Tuning =====\n\n@inproceedings{hu2022lora,\n  author    = {Hu, Edward J. and Shen, Yelong and Wallis, Phillip and Allen-Zhu, Zeyuan and Li, Yuanzhi and Wang, Shean and Wang, Lu and Chen, Weizhu},\n  title     = {{LoRA}: Low-Rank Adaptation of Large Language Models},\n  booktitle = {International Conference on Learning Representations (ICLR)},\n  year      = {2022},\n}\n\n% ===== VLA Safety Survey =====\n\n@article{li2026vlasafety,\n  title={Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms},\n  author={Li, Qi and Yin, Bo and Huang, Weiqi and Liu, Ruhao and Zou, Bojun and Yu, Runpeng and Ye, Jingwen and Yu, Weihao and Wang, Xinchao},\n  journal={arXiv preprint arXiv:2604.23775},\n  year={2026}\n}\n\n% ===== Action Collapse =====\n\n@article{dong2025conditioning,\n  title={Conditioning Matters: Training Diffusion Policies is Faster Than You Think},\n  author={Dong, Zibin and Liu, Yicheng and Li, Yinchuan and Zhao, Hang and Hao, Jianye},\n  journal={arXiv preprint arXiv:2505.11123},\n  year={2025}\n}\n\n% ===== Evaluation Methodology =====\n\n@article{snyder2026beyond,\n  title={Beyond Binary Success: Sample-Efficient and Statistically Rigorous Robot Policy Comparison},\n  author={Snyder, David and Badithela, Apurva and Matni, Nikolai and Pappas, George and Majumdar, Anirudha and Itkina, Masha and Nishimura, Haruki},\n  journal={arXiv preprint arXiv:2603.13616},\n  year={2026}\n}\n",
      "numLines": 252,
      "startLine": 1,
      "totalLines": 252
    }
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-28T06:50:54.425Z_

<details><summary>↩ Tool result · `toolu_01RdQqZtxVv6ncpoenRRPUPJ`</summary>

```text
Web search results for query: "HazardArena arXiv 2604.12447 authors list 2026"

Links: [{"title":"[2604.12447] HazardArena: Evaluating Semantic Safety in Vision-Language-Action Models","url":"https://arxiv.org/abs/2604.12447"},{"title":"HazardArena: Evaluating Semantic Safety in Vision–Language–Action Models","url":"https://arxiv.org/html/2604.12447"},{"title":"Language as Cost: Proactive Hazard Mapping using VLM for Robot Navigation","url":"https://arxiv.org/pdf/2508.03138"},{"title":"Differential risk of healthcare workers versus the general population during outbreak, war and pandemic crises","url":"https://www.medrxiv.org/content/10.1101/2024.05.30.24308231.full.pdf"},{"title":"Integration of Object Detection and Small VLMs for Construction Safety Hazard Identification","url":"https://arxiv.org/pdf/2604.05210"},{"title":"From Narratives to Probabilistic Reasoning: Predicting and Interpreting Drivers' Hazardous Actions in Crashes Using Large Language Model","url":"https://arxiv.org/pdf/2510.13002"},{"title":"Generation of four dimensional grid of probabilistic hazards for use by decision support tools","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8095314"},{"title":"Can Large Language Models assist in Hazard Analysis?","url":"https://arxiv.org/pdf/2303.15473"}]

Based on the search results, the authors of HazardArena (arXiv 2604.12447) are: Zixing Chen, Yifeng Gao, Li Wang, Yunhan Zhao, Yi Liu, Jiayu Li, Xiang Zheng, Zuxuan Wu, Cong Wang, Xingjun Ma, and Yu-Gang Jiang.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "654c65ff-8f04-44ef-be40-66cd95126362",
  "tool_use_result": {
    "query": "HazardArena arXiv 2604.12447 authors list 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_011RfiGF3DBf1JZ6Q7YXHJfy",
        "content": [
          {
            "title": "[2604.12447] HazardArena: Evaluating Semantic Safety in Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2604.12447"
          },
          {
            "title": "HazardArena: Evaluating Semantic Safety in Vision–Language–Action Models",
            "url": "https://arxiv.org/html/2604.12447"
          },
          {
            "title": "Language as Cost: Proactive Hazard Mapping using VLM for Robot Navigation",
            "url": "https://arxiv.org/pdf/2508.03138"
          },
          {
            "title": "Differential risk of healthcare workers versus the general population during outbreak, war and pandemic crises",
            "url": "https://www.medrxiv.org/content/10.1101/2024.05.30.24308231.full.pdf"
          },
          {
            "title": "Integration of Object Detection and Small VLMs for Construction Safety Hazard Identification",
            "url": "https://arxiv.org/pdf/2604.05210"
          },
          {
            "title": "From Narratives to Probabilistic Reasoning: Predicting and Interpreting Drivers' Hazardous Actions in Crashes Using Large Language Model",
            "url": "https://arxiv.org/pdf/2510.13002"
          },
          {
            "title": "Generation of four dimensional grid of probabilistic hazards for use by decision support tools",
            "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8095314"
          },
          {
            "title": "Can Large Language Models assist in Hazard Analysis?",
            "url": "https://arxiv.org/pdf/2303.15473"
          }
        ]
      },
      "Based on the search results, the authors of HazardArena (arXiv 2604.12447) are: Zixing Chen, Yifeng Gao, Li Wang, Yunhan Zhao, Yi Liu, Jiayu Li, Xiang Zheng, Zuxuan Wu, Cong Wang, Xingjun Ma, and Yu-Gang Jiang."
    ],
    "durationSeconds": 4.454814045999999
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-28T06:50:57.337Z_

<details><summary>↩ Tool result · `toolu_015zHMKD79wcDWJqY7A95KTm`</summary>

```text
Web search results for query: "VLA-Risk benchmarking vision-language-action physical robustness authors OpenReview ICLR 2026"

Links: [{"title":"VLA-Risk: Benchmarking Vision-Language-Action Models with Physical Robustness | OpenReview","url":"https://openreview.net/forum?id=31EjDFwFEe"},{"title":"VLA-RISK: BENCHMARKING VISION-LANGUAGE","url":"https://openreview.net/pdf/2b0044c5e9586d1b0dce44c7f3a73dbc43d13da0.pdf"},{"title":"Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms","url":"https://arxiv.org/html/2604.23775v1"},{"title":"On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations | OpenReview","url":"https://openreview.net/forum?id=cS6xizdYD5"},{"title":"Eva-VLA: Evaluating Vision-Language-Action Models' Robustness Under Real-World Physical Variations","url":"https://arxiv.org/pdf/2509.18953"},{"title":"In-depth Robustness Analysis for Vision-Language-Action Models | OpenReview","url":"https://openreview.net/forum?id=6mEfYoMRpF"},{"title":"On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations","url":"https://arxiv.org/pdf/2510.00037"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/pdf/2510.13626"}]

Based on the web search results, I found the information about VLA-Risk:

VLA-Risk is a paper under review as a conference paper at ICLR 2026, authored by anonymous authors (as it is under double-blind review on OpenReview).

The paper presents VLA-Risk, a benchmark for assessing the risks of Vision-Language-Action (VLA) models across different input modalities (such as image and instruction) and along three fundamental task dimensions: object, action, and space. VLA-Risk spans 296 scenarios and 3784 episodes, covering diverse settings such as simple manipulation, semantic reasoning, and autonomous driving.

By structuring attacks around these dimensions, VLA-Risk provides a principled framework for analyzing vulnerabilities and guiding the development of safer and more robust embodied agents. Extensive empirical evaluation further shows that the current state-of-the-art VLA models face substantial challenges under their attack tasks.

The paper is available on OpenReview at: https://openreview.net/forum?id=31EjDFwFEe


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "4ae379da-2092-4d28-888d-e0088984608e",
  "tool_use_result": {
    "query": "VLA-Risk benchmarking vision-language-action physical robustness authors OpenReview ICLR 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RkKKRedXfgk85kqGTLpJkz",
        "content": [
          {
            "title": "VLA-Risk: Benchmarking Vision-Language-Action Models with Physical Robustness | OpenReview",
            "url": "https://openreview.net/forum?id=31EjDFwFEe"
          },
          {
            "title": "VLA-RISK: BENCHMARKING VISION-LANGUAGE",
            "url": "https://openreview.net/pdf/2b0044c5e9586d1b0dce44c7f3a73dbc43d13da0.pdf"
          },
          {
            "title": "Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms",
            "url": "https://arxiv.org/html/2604.23775v1"
          },
          {
            "title": "On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations | OpenReview",
            "url": "https://openreview.net/forum?id=cS6xizdYD5"
          },
          {
            "title": "Eva-VLA: Evaluating Vision-Language-Action Models' Robustness Under Real-World Physical Variations",
            "url": "https://arxiv.org/pdf/2509.18953"
          },
          {
            "title": "In-depth Robustness Analysis for Vision-Language-Action Models | OpenReview",
            "url": "https://openreview.net/forum?id=6mEfYoMRpF"
          },
          {
            "title": "On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations",
            "url": "https://arxiv.org/pdf/2510.00037"
          },
          {
            "title": "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://arxiv.org/pdf/2510.13626"
          }
        ]
      },
      "Based on the web search results, I found the information about VLA-Risk:\n\nVLA-Risk is a paper under review as a conference paper at ICLR 2026, authored by anonymous authors (as it is under double-blind review on OpenReview).\n\nThe paper presents VLA-Risk, a benchmark for assessing the risks of Vision-Language-Action (VLA) models across different input modalities (such as image and instruction) and along three fundamental task dimensions: object, action, and space. VLA-Risk spans 296 scenarios and 3784 episodes, covering diverse settings such as simple manipulation, semantic reasoning, and autonomous driving.\n\nBy structuring attacks around these dimensions, VLA-Risk provides a principled framework for analyzing vulnerabilities and guiding the development of safer and more robust embodied agents. Extensive empirical evaluation further shows that the current state-of-the-art VLA models face substantial challenges under their attack tasks.\n\nThe paper is available on OpenReview at: https://openreview.net/forum?id=31EjDFwFEe"
    ],
    "durationSeconds": 6.841302372999999
  }
}
```

</details>

---

### Assistant

_source line 42_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need. Let me also search for the exact "20×" text in discussion.tex line 6 since my grep for "20" returned the long line. Let me read the specific lines more carefully.

From the files I've already read:

**discussion.tex line 6**: contains `20$\times$ the lowest tested weight` — this is the "20×" to replace
**appendix.tex**: I need to find the "20×" in appendix. Let me search more carefully.

Wait, the task says appendix.tex approximately L181. Let me look at that area. 

Looking at lines 176-183 of appendix.tex, I can see this is the null distribution section, so I need to search more precisely for the "20×" occurrence in that file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "fab3a9ee-2b08-4a09-9976-f2790ce584e5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GtVQ7rT2a5FiTjGnsSqhxi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4350,
      "cache_creation_input_tokens": 1504,
      "cache_read_input_tokens": 41298,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1504
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

_source line 43_

<details open><summary>🔧 Tool call — Grep · `toolu_01LodBxkYqw8s1rhvUvczSkq`</summary>

```json
{
  "pattern": "20",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex",
  "output_mode": "content",
  "-n": true,
  "glob": "*.tex",
  "-C": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "0a65ffd1-5880-4775-8990-e7b013ea95be",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GtVQ7rT2a5FiTjGnsSqhxi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4350,
      "cache_creation_input_tokens": 1504,
      "cache_read_input_tokens": 41298,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1504
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

_source line 44 · 2026-05-28T06:51:07.295Z_

<details><summary>↩ Tool result · `toolu_01LodBxkYqw8s1rhvUvczSkq`</summary>

```text
7:\caption{Displacement distribution across evaluation episodes. Pi0-family models (blue) cluster below 1\,$\mu$m, while Pi0.5 episodes (orange) exceed 200\,mm. The five-order-of-magnitude gap makes $\tau_d$ robust to any value in $[2, 200]$\,mm.}
34:Table~\ref{tab:dfcar_threshold} extends this analysis to dfCAR across fine-tuned Pi0.5 configurations. All eight model-seed combinations yield identical dfCAR for $\tau_d \in [2, 200]$\,mm. At $\tau_d = 300$\,mm, 0--2 episodes per seed fall below threshold (displacement 200--300\,mm), causing $\leq$0.5\,pp deviation. Our conclusions hold across the entire tested range.
38:\caption{dfCAR (\%) across displacement thresholds for fine-tuned Pi0.5 configurations ($n = 200$ episodes per seed). Values are identical across $\tau_d \in [2, 200]$\,mm; at $\tau_d = 300$\,mm, at most 2 episodes are excluded.}
46:Condition & 2 & 5 & 10 & 20 & 50 & 100 & 200 & 300 \\
103:SDF $\lambda{=}0.005$ (3-seed) & 54.0 & 72.7 & 71.3 & 20.0 & 54.5 \\
181:[Omitted long matching line]
188:Table~\ref{tab:stepwise_lambda01} reports per-seed CAR at seven checkpoints for $\lambda = 0.1$. Seeds~0 and~1 are available at 16K, 20K, 22K, and 30K; 24K--28K report seed-0 only; seed~2 is available at 30K only. The seed-0 curve shows no monotonic trend through 28K. At 30K, the addition of seed~2 (54.5\%) pulls the three-seed mean to 57.00\%, within the null band ($p = 0.131$).
192:\caption{Per-seed CAR (\%) at training checkpoints for $\lambda = 0.1$ (200 episodes each). 24K--28K: seed-0 only. The 30K checkpoint includes all three seeds; the three-seed mean (57.00\%) remains within the null band ($p = 0.131$, two-tailed permutation).}
201:20K steps & 55.0 & 56.0 & -- & 55.5 \\
231:[Omitted long matching line]
235:\caption{Cross-scene validation on \texttt{spatial\_bowl} (single training seed, 200 episodes, 30K checkpoint). The $-$0.5\,pp CAR difference is well within noise, consistent with the SDF redundancy observed on \texttt{object\_pudding}.}
259:\caption{Aggregate CAR (\%) across evaluation seeds (200 episodes each). The LoRA vs.\ SDF $\lambda{=}0.1$ ordering is preserved across all tested seeds, and per-task CAR fingerprints (CP highest, BBQ lowest) remain invariant.}
271:LoRA s0 (seed\,=\,123) & 52 & 74 & 66 & 20 & 53.0 \\
316:We use LoRA~\citep{hu2022lora} adapters injected into the PaliGemma vision encoder (rank 16, $\alpha$=16) and the action expert (rank 32, $\alpha$=32), following the configuration of OpenPi. The SDF decoder is a 4-layer MLP (hidden dimension 256) with skip connections, taking pooled suffix features (1024-d) and query points (3-d) as input. The end-effector extractor is a 2-layer MLP (1024 $\to$ 256 $\to$ 3).
353:[Omitted long matching line]
359:All training and evaluation experiments are conducted on NVIDIA RTX PRO 6000 GPUs (96\,GB). Phase~1 (5K steps) takes approximately 6 hours on a single GPU; Phase~2 (25K steps) takes approximately 32 hours. Evaluation of 200 episodes requires approximately 4 hours. Across 100+ experiments (training runs, evaluations, oracle variants, and ablations), the total computational budget is approximately 700 GPU-hours.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "bd07498f-609f-4a54-9821-05d70e63777e",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "7:\\caption{Displacement distribution across evaluation episodes. Pi0-family models (blue) cluster below 1\\,$\\mu$m, while Pi0.5 episodes (orange) exceed 200\\,mm. The five-order-of-magnitude gap makes $\\tau_d$ robust to any value in $[2, 200]$\\,mm.}\n34:Table~\\ref{tab:dfcar_threshold} extends this analysis to dfCAR across fine-tuned Pi0.5 configurations. All eight model-seed combinations yield identical dfCAR for $\\tau_d \\in [2, 200]$\\,mm. At $\\tau_d = 300$\\,mm, 0--2 episodes per seed fall below threshold (displacement 200--300\\,mm), causing $\\leq$0.5\\,pp deviation. Our conclusions hold across the entire tested range.\n38:\\caption{dfCAR (\\%) across displacement thresholds for fine-tuned Pi0.5 configurations ($n = 200$ episodes per seed). Values are identical across $\\tau_d \\in [2, 200]$\\,mm; at $\\tau_d = 300$\\,mm, at most 2 episodes are excluded.}\n46:Condition & 2 & 5 & 10 & 20 & 50 & 100 & 200 & 300 \\\\\n103:SDF $\\lambda{=}0.005$ (3-seed) & 54.0 & 72.7 & 71.3 & 20.0 & 54.5 \\\\\n181:[Omitted long matching line]\n188:Table~\\ref{tab:stepwise_lambda01} reports per-seed CAR at seven checkpoints for $\\lambda = 0.1$. Seeds~0 and~1 are available at 16K, 20K, 22K, and 30K; 24K--28K report seed-0 only; seed~2 is available at 30K only. The seed-0 curve shows no monotonic trend through 28K. At 30K, the addition of seed~2 (54.5\\%) pulls the three-seed mean to 57.00\\%, within the null band ($p = 0.131$).\n192:\\caption{Per-seed CAR (\\%) at training checkpoints for $\\lambda = 0.1$ (200 episodes each). 24K--28K: seed-0 only. The 30K checkpoint includes all three seeds; the three-seed mean (57.00\\%) remains within the null band ($p = 0.131$, two-tailed permutation).}\n201:20K steps & 55.0 & 56.0 & -- & 55.5 \\\\\n231:[Omitted long matching line]\n235:\\caption{Cross-scene validation on \\texttt{spatial\\_bowl} (single training seed, 200 episodes, 30K checkpoint). The $-$0.5\\,pp CAR difference is well within noise, consistent with the SDF redundancy observed on \\texttt{object\\_pudding}.}\n259:\\caption{Aggregate CAR (\\%) across evaluation seeds (200 episodes each). The LoRA vs.\\ SDF $\\lambda{=}0.1$ ordering is preserved across all tested seeds, and per-task CAR fingerprints (CP highest, BBQ lowest) remain invariant.}\n271:LoRA s0 (seed\\,=\\,123) & 52 & 74 & 66 & 20 & 53.0 \\\\\n316:We use LoRA~\\citep{hu2022lora} adapters injected into the PaliGemma vision encoder (rank 16, $\\alpha$=16) and the action expert (rank 32, $\\alpha$=32), following the configuration of OpenPi. The SDF decoder is a 4-layer MLP (hidden dimension 256) with skip connections, taking pooled suffix features (1024-d) and query points (3-d) as input. The end-effector extractor is a 2-layer MLP (1024 $\\to$ 256 $\\to$ 3).\n353:[Omitted long matching line]\n359:All training and evaluation experiments are conducted on NVIDIA RTX PRO 6000 GPUs (96\\,GB). Phase~1 (5K steps) takes approximately 6 hours on a single GPU; Phase~2 (25K steps) takes approximately 32 hours. Evaluation of 200 episodes requires approximately 4 hours. Across 100+ experiments (training runs, evaluations, oracle variants, and ablations), the total computational budget is approximately 700 GPU-hours.",
    "numLines": 16
  }
}
```

</details>

---

### Assistant

_source line 45_

<details><summary>Logged reasoning block</summary>

```text
Let me read appendix.tex line 181 to see the "20×" text there:
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "401bd83d-ace5-4b8c-b97e-46418bc99b32",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NcZ1ij2yJMqt3RJeM8xbd9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5935,
      "cache_read_input_tokens": 42802,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5935
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

_source line 46_

<details open><summary>🔧 Tool call — Read · `toolu_01G77Wpxdqp7bMqWS5YVGNhC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex",
  "offset": 178,
  "limit": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "f6eaebc1-991b-4328-bc2c-829cad2e007d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NcZ1ij2yJMqt3RJeM8xbd9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5935,
      "cache_read_input_tokens": 42802,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5935
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

_source line 47 · 2026-05-28T06:51:11.071Z_

<details><summary>↩ Tool result · `toolu_01G77Wpxdqp7bMqWS5YVGNhC`</summary>

```text
178	The permutation test makes no distributional assumptions. Pooling the six null values $\{56.5, 52.5, 55, 57, 54, 52.5\}$ and three $\lambda = 0.1$ values $\{58, 58.5, 54.5\}$ into nine measurements, we enumerate all $\binom{9}{3} = 84$ three-element combinations and compute the fraction whose mean $\geq 57.00$. Six combinations meet this threshold, yielding an exact one-tailed permutation $p = 6/84 \approx 0.071$. For the two-tailed test, we additionally count combinations on the lower tail with equal or greater distance from the pooled mean, yielding $p = 11/84 \approx 0.131$. With the third seed ($s_2 = 54.5\%$) pulling the $\lambda = 0.1$ mean from 58.25\% (2 seeds) down to 57.00\%, the marginal signal observed at $n = 2$ dissolves into seed-to-seed variance.
179	
180	\paragraph{Alternative null construction (Null~A).}
181	If only the three LoRA-only seeds are used as the null pool ($\{56.5, 52.5, 55.0\}$), we obtain $\binom{6}{3} = 20$ permutations for each comparison. For $\lambda = 0.1$ (treatment mean 57.00\%): one-tailed $p = 3/20 = 0.150$, two-tailed $p = 6/20 = 0.300$. For $\lambda = 0.01$ (treatment mean 56.33\%): one-tailed $p = 4/20 = 0.200$, two-tailed $p = 8/20 = 0.400$. Under the broader Null~B pool, $\lambda = 0.01$ yields one-tailed $p = 10/84 \approx 0.119$, two-tailed $p = 22/84 \approx 0.262$. All tests are non-significant at $\alpha = 0.05$; the narrower Null~A yields \emph{larger} $p$-values because the LoRA-only pool already contains a high seed (56.5\%), making the treatment means less extreme by comparison.
182	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "4e60324a-6bd2-4986-a7bd-2e89791ce377",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex",
      "content": "The permutation test makes no distributional assumptions. Pooling the six null values $\\{56.5, 52.5, 55, 57, 54, 52.5\\}$ and three $\\lambda = 0.1$ values $\\{58, 58.5, 54.5\\}$ into nine measurements, we enumerate all $\\binom{9}{3} = 84$ three-element combinations and compute the fraction whose mean $\\geq 57.00$. Six combinations meet this threshold, yielding an exact one-tailed permutation $p = 6/84 \\approx 0.071$. For the two-tailed test, we additionally count combinations on the lower tail with equal or greater distance from the pooled mean, yielding $p = 11/84 \\approx 0.131$. With the third seed ($s_2 = 54.5\\%$) pulling the $\\lambda = 0.1$ mean from 58.25\\% (2 seeds) down to 57.00\\%, the marginal signal observed at $n = 2$ dissolves into seed-to-seed variance.\n\n\\paragraph{Alternative null construction (Null~A).}\nIf only the three LoRA-only seeds are used as the null pool ($\\{56.5, 52.5, 55.0\\}$), we obtain $\\binom{6}{3} = 20$ permutations for each comparison. For $\\lambda = 0.1$ (treatment mean 57.00\\%): one-tailed $p = 3/20 = 0.150$, two-tailed $p = 6/20 = 0.300$. For $\\lambda = 0.01$ (treatment mean 56.33\\%): one-tailed $p = 4/20 = 0.200$, two-tailed $p = 8/20 = 0.400$. Under the broader Null~B pool, $\\lambda = 0.01$ yields one-tailed $p = 10/84 \\approx 0.119$, two-tailed $p = 22/84 \\approx 0.262$. All tests are non-significant at $\\alpha = 0.05$; the narrower Null~A yields \\emph{larger} $p$-values because the LoRA-only pool already contains a high seed (56.5\\%), making the treatment means less extreme by comparison.\n",
      "numLines": 5,
      "startLine": 178,
      "totalLines": 360
    }
  }
}
```

</details>

---

### Assistant

_source line 48_

<details><summary>Logged reasoning block</summary>

```text
Hmm, line 181 doesn't contain "20×". Let me look at the actual "20×" in the appendix more carefully. Looking at the discussion.tex line 6, I see `20$\times$ the lowest tested weight`. Let me search for the exact pattern in appendix.

Wait, looking back at the task description: "appendix.tex 约 L181" — but looking at the grep results, the match on line 181 was the omitted long matching line. Let me re-check the content. Actually, I think the "20" grep matched line 181 but it was omitted because it was long. But I just read line 181 and it doesn't contain "20×" — it contains "$\binom{6}{3} = 20$". 

So that "20" is from a binomial coefficient, not the "20×" I'm looking for. Let me search more systematically for "times" or similar language in the appendix to find the right reference.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "d206e959-76fb-4d2a-a0b3-0f472880f173",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BpjyxS7wpogLTEokpp8xPb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 762,
      "cache_read_input_tokens": 48737,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 762
      },
      "output_tokens": 35,
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

_source line 49_

<details open><summary>🔧 Tool call — Grep · `toolu_01SCqy4Aqzx96GreT8KGanZW`</summary>

```json
{
  "pattern": "\\\\\\\\times.*lowest|lowest.*\\\\\\\\times",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "6deae68b-173f-413a-a63e-8592e4ff3ec4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BpjyxS7wpogLTEokpp8xPb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 762,
      "cache_read_input_tokens": 48737,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 762
      },
      "output_tokens": 35,
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

_source line 50 · 2026-05-28T06:51:19.222Z_

<details><summary>↩ Tool result · `toolu_01SCqy4Aqzx96GreT8KGanZW`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "8583fb2c-a968-4b1e-bf80-9136c7d97521",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  }
}
```

</details>

---

### Tool call

_source line 51_

<details open><summary>🔧 Tool call — Grep · `toolu_01HaKKqRaWMseCqJUxYh2Xns`</summary>

```json
{
  "pattern": "\\\\\\\\times",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "7a48a709-7616-4190-87a9-f8bfd96c2ff0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BpjyxS7wpogLTEokpp8xPb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 762,
      "cache_read_input_tokens": 48737,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 762
      },
      "output_tokens": 35,
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

_source line 52 · 2026-05-28T06:51:19.742Z_

<details><summary>↩ Tool result · `toolu_01HaKKqRaWMseCqJUxYh2Xns`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "313503e9-04fc-49f1-9af0-0aa24ac02533",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  }
}
```

</details>

---

### Tool call

_source line 53_

<details open><summary>🔧 Tool call — Grep · `toolu_01QPvkM4jrgNA53QVFc2jBsa`</summary>

```json
{
  "pattern": "times",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "4c853256-8e96-4398-be68-55edf0377a3a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KKdzUddi8JpznEM7YybGiL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 574,
      "cache_read_input_tokens": 49499,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 574
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

_source line 54 · 2026-05-28T06:51:23.454Z_

<details><summary>↩ Tool result · `toolu_01QPvkM4jrgNA53QVFc2jBsa`</summary>

```text
151:The feature-space oracle fires on nearly every timestep (241.7 refinements/episode vs.\ 14.2 for Cartesian variants) but with gradient magnitudes two orders of magnitude smaller (0.004--0.006 vs.\ 0.18--0.49), and CAR (76.9\%) shows no advantage despite 17$\times$ more steps. The A3 learned SDF never triggers refinement (0 steps/episode), as its outputs avoid the activation threshold.
217:All oracle variants replace the learned SDF decoder with ground-truth distance fields computed from the simulation geometry. Each is evaluated for 160 episodes (4 tasks $\times$ 40).
219:\paragraph{Oracle-adaptive.} At each timestep, if the ground-truth SDF at the end-effector position falls below a safety margin, the action is adjusted by a step in the negative SDF gradient direction. The step size $\alpha$ is scaled inversely with distance: smaller distances produce larger corrections. This mimics an adaptive potential field controller.
223:[Omitted long matching line]
336:Learning rate & $2.5 \times 10^{-5}$ (cosine decay to $\mathrm{lr}/10$) \\
353:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "e4063e51-e1c8-4f1b-bbbd-028a6a0a7469",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "151:The feature-space oracle fires on nearly every timestep (241.7 refinements/episode vs.\\ 14.2 for Cartesian variants) but with gradient magnitudes two orders of magnitude smaller (0.004--0.006 vs.\\ 0.18--0.49), and CAR (76.9\\%) shows no advantage despite 17$\\times$ more steps. The A3 learned SDF never triggers refinement (0 steps/episode), as its outputs avoid the activation threshold.\n217:All oracle variants replace the learned SDF decoder with ground-truth distance fields computed from the simulation geometry. Each is evaluated for 160 episodes (4 tasks $\\times$ 40).\n219:\\paragraph{Oracle-adaptive.} At each timestep, if the ground-truth SDF at the end-effector position falls below a safety margin, the action is adjusted by a step in the negative SDF gradient direction. The step size $\\alpha$ is scaled inversely with distance: smaller distances produce larger corrections. This mimics an adaptive potential field controller.\n223:[Omitted long matching line]\n336:Learning rate & $2.5 \\times 10^{-5}$ (cosine decay to $\\mathrm{lr}/10$) \\\\\n353:[Omitted long matching line]",
    "numLines": 6
  }
}
```

</details>

---

### Assistant

_source line 55_

<details><summary>Logged reasoning block</summary>

```text
OK, so in the appendix, there's no "20×" occurrence. The only `$\times$` occurrences are `17$\times$` on line 151 and `4 tasks $\times$ 40` on line 217. The task instruction says appendix.tex 约 L181, but there's no "20×" there.

Let me re-read the task description:
> **P2 #8 partial: "20×" 减少（本组文件部分）**
> 搜索 "20" 或 "$20\\times$" 或 "20$\\times$"，找到以下位置并替换：


Found it in discussion.tex at line 6: `Even at $\lambda = 0.1$ (20$\times$ the lowest tested weight)` needs to be replaced with something like "across the tested range" or "spanning an order of magnitude". Now I need to find the corresponding location in appendix.tex around line 181 and make the same replacement.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "b6a8d484-a35f-45e2-8959-c657452a9f68",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SdAJdAby2KWWpAprSYtCTd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 450,
      "cache_read_input_tokens": 50073,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 450
      },
      "output_tokens": 26,
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

_source line 56_

<details open><summary>🔧 Tool call — Grep · `toolu_016nRL8JZQRrth6jn3vhZCEz`</summary>

```json
{
  "pattern": "20\\$",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "f45e7f12-bfa3-4397-998f-6d022d612cab",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SdAJdAby2KWWpAprSYtCTd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 450,
      "cache_read_input_tokens": 50073,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 450
      },
      "output_tokens": 26,
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

_source line 57 · 2026-05-28T06:51:33.232Z_

<details><summary>↩ Tool result · `toolu_016nRL8JZQRrth6jn3vhZCEz`</summary>

```text
181:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "ba95be8d-47fd-4eb4-ab64-a0d9287a56ba",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "181:[Omitted long matching line]",
    "numLines": 1
  }
}
```

</details>

---

### Tool call

_source line 58_

<details open><summary>🔧 Tool call — Grep · `toolu_01SauNssS1YaKPuxRn4z4Lu2`</summary>

```json
{
  "pattern": "lowest tested",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "0469d6c6-e6ca-4b43-a3cf-e27f057227e5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SdAJdAby2KWWpAprSYtCTd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 450,
      "cache_read_input_tokens": 50073,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 450
      },
      "output_tokens": 26,
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

_source line 59 · 2026-05-28T06:51:33.740Z_

<details><summary>↩ Tool result · `toolu_01SauNssS1YaKPuxRn4z4Lu2`</summary>

```text
docs/paper/discussion.tex:6:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "0ba859bf-a79c-4162-b6bf-2891553bf1df",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/discussion.tex:6:[Omitted long matching line]",
    "numLines": 1
  }
}
```

</details>

---

### Assistant

_source line 60_

<details><summary>Logged reasoning block</summary>

```text
It seems "20$" matches in appendix line 181. But I just read that line and it has "$\binom{6}{3} = 20$". Let me try a different search pattern.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "857b8978-5247-458b-8bf3-d2b83b33e15d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FBJCbG1UuA44a3ELzd6ekL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 647,
      "cache_read_input_tokens": 50523,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 647
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

_source line 61_

<details open><summary>🔧 Tool call — Grep · `toolu_013QLLvmodHqH7y5Z4jDMWNN`</summary>

```json
{
  "pattern": "20.{0,5}permutation|20.{0,5}\\\\\\\\times|\\\\$20",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "96af9d42-0942-4d8a-8487-22aa18f2e41a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FBJCbG1UuA44a3ELzd6ekL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 647,
      "cache_read_input_tokens": 50523,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 647
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

_source line 62 · 2026-05-28T06:51:38.733Z_

<details><summary>↩ Tool result · `toolu_013QLLvmodHqH7y5Z4jDMWNN`</summary>

```text
181:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "3b4c7c40-9155-4d95-8349-dec945c5aa7e",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "181:[Omitted long matching line]",
    "numLines": 1
  }
}
```

</details>

---

### Assistant

_source line 63_

<details><summary>Logged reasoning block</summary>

```text
The "20" on line 181 is from "$\binom{6}{3} = 20$" which is a permutation count, not a "20×" claim. The task says "appendix.tex 约 L181" but looking at the text on that line, the only "20" is "$\binom{6}{3} = 20$" — a mathematical result, not a "20×" multiplier.

Wait, maybe the task description was slightly off about the location. Let me search all .tex files in the paper directory for patterns involving "20" as a multiplier (not as permutation count or table data).


I'm wondering if the task author was pointing to something that's no longer in the appendix, or perhaps it was never there to begin with. I've already confirmed the "20×" replacement in discussion.tex is clear, but I can't find a corresponding "20×" text in appendix.tex despite searching for variations like "20-fold" or "20 times". Let me look more carefully at what's actually on that line.

The grep result shows `$\binom{6}{3} = 20$` — that's just a binomial coefficient equaling 20, not a "20×" claim that needs replacing. So there's nothing to change in appendix.tex after all.

Now I'll move forward with the actual edits. Starting with the SafeVLA classification error in related_work.tex at line 12, I need to change "Constraint-based planning" to "Constrained optimization" and revise the SafeVLA description. I'm working through a series of edits to clarify the paper's claims about safety approaches. I need to update the SafeVLA description to reflect that it uses constrained optimization during planning rather than constraint-based planning, adjust the discussion about how different approaches bypass the structural limitation of end-effector-only supervision, and add qualifications like "at the tested scale" to the redundancy findings to be more precise about their scope. I'm also planning to specify that the safety evaluation critique applies specifically to CAR-based approaches on SafeLIBERO rather than making a blanket statement about current VLA safety evaluation. I'm working through the edits to related_work.tex line 12, where I need to soften the language about the SDF redundancy finding across multiple places in that paragraph. Let me apply all the changes at once to keep the flow consistent. I need to revise the closing sentence since both (a) and (b) are training-time methods—the distinction is in their optimization approach, not when they're applied. So the "bypass" framing doesn't work for (b), which uses constrained optimization rather than auxiliary supervision. Instead, (b) constrains violation probability directly while (c) is the only one that operates entirely at inference time. Let me rewrite that paragraph to clarify these three distinct pathways and their mechanisms. I'm working through the specific edits needed for the paper. For the related work section, I need to keep "redundant" but qualify it with "at the tested scale" to be more precise about the scope of our finding. Then in the discussion, I should reframe the comparison between CMDP approaches and auxiliary loss methods as fundamentally different optimization paradigms—one directly constrains violation probability while the other adds geometric supervision—rather than just saying one is redundant. This distinction matters because it clarifies that our negative result applies specifically to the auxiliary loss pathway, not to constrained optimization or runtime filtering approaches that work through entirely different mechanisms.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "8506fac8-ab6b-44c3-b64b-cc943a29842f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AvCi8tReTLj5ABWoWGBYFG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 246,
      "cache_read_input_tokens": 51170,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 246
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

### Assistant

_source line 64_

appendix.tex 中没有 "20×" 倍数声明（L181 的 "20" 是 $\binom{6}{3}=20$ 排列组合数）。现在开始按优先级执行修改。

**P0 #1**: 先改 related_work.tex L12（SafeVLA 分类 + redundant 限定一起处理）和 discussion.tex L6。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "8a218893-1ea2-4f33-8988-ed38ea8e2f9b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AvCi8tReTLj5ABWoWGBYFG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 246,
      "cache_read_input_tokens": 51170,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 246
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

_source line 65_

<details open><summary>🔧 Tool call — Edit · `toolu_012yKvA4rfbuinjSjmhBsjJQ`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/related_work.tex",
  "old_string": "(b)~\\emph{Constraint-based planning}: SafeVLA~\\citep{zhang2025safevla} formulates collision avoidance as a constrained MDP, using SDF constraints during planning rather than training. (c)~\\emph{Runtime filtering}: VLSA~\\citep{hu2025vlsa} applies control barrier functions (CBFs) with SDF at inference time, filtering unsafe actions post-hoc. Our negative finding---that EE-only auxiliary SDF loss is redundant---is specific to pathway~(a) and does not apply to pathways~(b) and~(c), which bypass the structural limitation of supervising only the end-effector during training.",
  "new_string": "(b)~\\emph{Constrained optimization}: SafeVLA~\\citep{zhang2025safevla} formulates collision avoidance as a constrained MDP, embedding safety constraints into the training objective via Lagrangian optimization rather than adding SDF as an auxiliary loss. (c)~\\emph{Runtime filtering}: VLSA~\\citep{hu2025vlsa} applies control barrier functions (CBFs) with SDF at inference time, filtering unsafe actions post-hoc. Our negative finding---that EE-only auxiliary SDF loss is redundant at the tested scale---is specific to pathway~(a) and does not imply limitations for pathways~(b) and~(c), which address collision avoidance through fundamentally different mechanisms: constrained optimization of violation probability and runtime action filtering, respectively."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "521a1ce7-4156-4aa5-adc3-b0c44a6b82f2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AvCi8tReTLj5ABWoWGBYFG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 246,
      "cache_read_input_tokens": 51170,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 246
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

_source line 66 · 2026-05-28T06:52:27.174Z_

<details><summary>↩ Tool result · `toolu_012yKvA4rfbuinjSjmhBsjJQ`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/related_work.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "1f131219-7771-45db-b104-a15363f429e7",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/related_work.tex",
    "oldString": "(b)~\\emph{Constraint-based planning}: SafeVLA~\\citep{zhang2025safevla} formulates collision avoidance as a constrained MDP, using SDF constraints during planning rather than training. (c)~\\emph{Runtime filtering}: VLSA~\\citep{hu2025vlsa} applies control barrier functions (CBFs) with SDF at inference time, filtering unsafe actions post-hoc. Our negative finding---that EE-only auxiliary SDF loss is redundant---is specific to pathway~(a) and does not apply to pathways~(b) and~(c), which bypass the structural limitation of supervising only the end-effector during training.",
    "newString": "(b)~\\emph{Constrained optimization}: SafeVLA~\\citep{zhang2025safevla} formulates collision avoidance as a constrained MDP, embedding safety constraints into the training objective via Lagrangian optimization rather than adding SDF as an auxiliary loss. (c)~\\emph{Runtime filtering}: VLSA~\\citep{hu2025vlsa} applies control barrier functions (CBFs) with SDF at inference time, filtering unsafe actions post-hoc. Our negative finding---that EE-only auxiliary SDF loss is redundant at the tested scale---is specific to pathway~(a) and does not imply limitations for pathways~(b) and~(c), which address collision avoidance through fundamentally different mechanisms: constrained optimization of violation probability and runtime action filtering, respectively.",
    "originalFile": "\\section{Related Work}\\label{sec:related}\n\n\\paragraph{Vision-Language-Action Models.}\nVLA models combine pretrained vision-language backbones with action prediction for generalist manipulation~\\cite{brohan2023rt2,black2024pi0,chi2023diffusionpolicy,kim2024openvla}. Recent work enhances spatial reasoning through auxiliary 3D supervision~\\cite{li2025spatialforcing,li2025qdepth,depthvla2025}, but safety considerations remain largely absent: most VLAs train on collision-free demonstrations and evaluate task success alone, with no mechanism to distinguish genuine avoidance from incidental collision-free trajectories.\n\n\\paragraph{Safety in Robot Learning.}\nSafety-aware approaches span training-time constrained RL~\\cite{zhang2025safevla} and test-time filters: control barrier functions~\\cite{hu2025vlsa}, collision risk gating~\\cite{cofreeevla2026}, inverse kinematics QP~\\cite{spalter2024ikinqp}, and diffusion-process collision costs~\\cite{li2024langguided,yang2025cape}. SafeDiffuser~\\cite{xiao2025safediffuser} integrates control barrier functions directly into diffusion denoising to enforce safety invariance during planning; like other test-time shields, it does not learn intrinsic collision awareness within the policy. A recent survey~\\cite{li2026vlasafety} categorizes these into runtime shields, constrained optimization, and representation-based methods. Common to all is that safety is imposed externally rather than learned within the policy's representations. This work tests whether auxiliary SDF supervision can produce intrinsic collision awareness.\n\n\\paragraph{Signed Distance Functions in Robotics.}\nSDFs encode minimum surface distance, where the sign indicates free space or penetration. Neural SDFs~\\cite{park2019deepsdf} enable continuous shape representation; in robotics, SDFs serve perception~\\cite{ortiz2022isdf}, planning~\\cite{huang2023voxposer,vasilopoulos2023ramp}, and differentiable collision detection~\\cite{zhi2021diffco}. CDF~\\cite{li2024cdf} extends SDFs to robot configuration space, learning neural distance fields that provide efficient joint-angle queries with analytical gradients for manipulation planning; CSSDF-Net~\\cite{chen2026cssdfnet} further develops this direction for safe motion planning. RDF~\\cite{li2024rdf} represents robot geometry itself as composable per-link SDFs along the kinematic chain, enabling whole-body collision queries---directly relevant to the full-body awareness gap our work identifies. Neural SDF-based model predictive control~\\cite{jacquet2025neuralnmpc} demonstrates effectiveness in classical pipelines, but integration into end-to-end learned policies remains unexplored.\n\n\\paragraph{SDF integration pathways.} Geometric supervision via signed distance fields can be integrated into VLA policies through fundamentally different mechanisms. (a)~\\emph{Training-time auxiliary loss}: an SDF-based collision penalty is added to the training objective, supervising only the end-effector trajectory (the approach tested in this work). (b)~\\emph{Constraint-based planning}: SafeVLA~\\citep{zhang2025safevla} formulates collision avoidance as a constrained MDP, using SDF constraints during planning rather than training. (c)~\\emph{Runtime filtering}: VLSA~\\citep{hu2025vlsa} applies control barrier functions (CBFs) with SDF at inference time, filtering unsafe actions post-hoc. Our negative finding---that EE-only auxiliary SDF loss is redundant---is specific to pathway~(a) and does not apply to pathways~(b) and~(c), which bypass the structural limitation of supervising only the end-effector during training.\n\n\\paragraph{Evaluation Metrics for Safe Manipulation.}\nSafeLIBERO~\\cite{hu2025vlsa} extends LIBERO~\\cite{liu2023libero} with obstacle-augmented environments and a collision avoidance rate (CAR) metric. However, CAR treats all collision-free episodes identically: an action-collapsed robot scores near-perfect CAR without any avoidance behavior. This failure mode echoes concerns about metric reliability~\\cite{karwowski2024goodhart,gururangan2018annotation} and binary success metrics under limited samples~\\cite{snyder2026beyond}. Action collapse in diffusion policies~\\cite{dong2025conditioning} systematically inflates CAR but has not been previously examined as a safety evaluation confounder. We propose dfCAR (\\S\\ref{sec:dfcar}) to detect this contamination.\n",
    "structuredPatch": [
      {
        "oldStart": 9,
        "oldLines": 7,
        "newStart": 9,
        "newLines": 7,
        "lines": [
          " \\paragraph{Signed Distance Functions in Robotics.}",
          " SDFs encode minimum surface distance, where the sign indicates free space or penetration. Neural SDFs~\\cite{park2019deepsdf} enable continuous shape representation; in robotics, SDFs serve perception~\\cite{ortiz2022isdf}, planning~\\cite{huang2023voxposer,vasilopoulos2023ramp}, and differentiable collision detection~\\cite{zhi2021diffco}. CDF~\\cite{li2024cdf} extends SDFs to robot configuration space, learning neural distance fields that provide efficient joint-angle queries with analytical gradients for manipulation planning; CSSDF-Net~\\cite{chen2026cssdfnet} further develops this direction for safe motion planning. RDF~\\cite{li2024rdf} represents robot geometry itself as composable per-link SDFs along the kinematic chain, enabling whole-body collision queries---directly relevant to the full-body awareness gap our work identifies. Neural SDF-based model predictive control~\\cite{jacquet2025neuralnmpc} demonstrates effectiveness in classical pipelines, but integration into end-to-end learned policies remains unexplored.",
          " ",
          "-\\paragraph{SDF integration pathways.} Geometric supervision via signed distance fields can be integrated into VLA policies through fundamentally different mechanisms. (a)~\\emph{Training-time auxiliary loss}: an SDF-based collision penalty is added to the training objective, supervising only the end-effector trajectory (the approach tested in this work). (b)~\\emph{Constraint-based planning}: SafeVLA~\\citep{zhang2025safevla} formulates collision avoidance as a constrained MDP, using SDF constraints during planning rather than training. (c)~\\emph{Runtime filtering}: VLSA~\\citep{hu2025vlsa} applies control barrier functions (CBFs) with SDF at inference time, filtering unsafe actions post-hoc. Our negative finding---that EE-only auxiliary SDF loss is redundant---is specific to pathway~(a) and does not apply to pathways~(b) and~(c), which bypass the structural limitation of supervising only the end-effector during training.",
          "+\\paragraph{SDF integration pathways.} Geometric supervision via signed distance fields can be integrated into VLA policies through fundamentally different mechanisms. (a)~\\emph{Training-time auxiliary loss}: an SDF-based collision penalty is added to the training objective, supervising only the end-effector trajectory (the approach tested in this work). (b)~\\emph{Constrained optimization}: SafeVLA~\\citep{zhang2025safevla} formulates collision avoidance as a constrained MDP, embedding safety constraints into the training objective via Lagrangian optimization rather than adding SDF as an auxiliary loss. (c)~\\emph{Runtime filtering}: VLSA~\\citep{hu2025vlsa} applies control barrier functions (CBFs) with SDF at inference time, filtering unsafe actions post-hoc. Our negative finding---that EE-only auxiliary SDF loss is redundant at the tested scale---is specific to pathway~(a) and does not imply limitations for pathways~(b) and~(c), which address collision avoidance through fundamentally different mechanisms: constrained optimization of violation probability and runtime action filtering, respectively.",
          " ",
          " \\paragraph{Evaluation Metrics for Safe Manipulation.}",
          " SafeLIBERO~\\cite{hu2025vlsa} extends LIBERO~\\cite{liu2023libero} with obstacle-augmented environments and a collision avoidance rate (CAR) metric. However, CAR treats all collision-free episodes identically: an action-collapsed robot scores near-perfect CAR without any avoidance behavior. This failure mode echoes concerns about metric reliability~\\cite{karwowski2024goodhart,gururangan2018annotation} and binary success metrics under limited samples~\\cite{snyder2026beyond}. Action collapse in diffusion policies~\\cite{dong2025conditioning} systematically inflates CAR but has not been previously examined as a safety evaluation confounder. We propose dfCAR (\\S\\ref{sec:dfcar}) to detect this contamination."
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

### Tool call

_source line 67_

<details open><summary>🔧 Tool call — Edit · `toolu_01LSBjXbKEEbrR1fGr96wSQC`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex",
  "old_string": "The failure of EE-only auxiliary SDF loss is architectural; constraint-based and runtime filtering approaches bypass this structural limitation through fundamentally different integration mechanisms.",
  "new_string": "The failure of EE-only auxiliary SDF loss is architectural. Constrained-optimization approaches (e.g., SafeVLA) address collision avoidance through a fundamentally different optimization paradigm---directly constraining violation probability rather than adding geometric supervision---while runtime filtering sidesteps training altogether."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "1f5774cf-b2be-42d4-8af6-4c719d81a518",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AvCi8tReTLj5ABWoWGBYFG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 246,
      "cache_read_input_tokens": 51170,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 246
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

_source line 68 · 2026-05-28T06:52:28.653Z_

<details><summary>↩ Tool result · `toolu_01LSBjXbKEEbrR1fGr96wSQC`</summary>

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
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "24013dbf-ba7c-436f-a2b2-820539658857",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex",
    "oldString": "The failure of EE-only auxiliary SDF loss is architectural; constraint-based and runtime filtering approaches bypass this structural limitation through fundamentally different integration mechanisms.",
    "newString": "The failure of EE-only auxiliary SDF loss is architectural. Constrained-optimization approaches (e.g., SafeVLA) address collision avoidance through a fundamentally different optimization paradigm---directly constraining violation probability rather than adding geometric supervision---while runtime filtering sidesteps training altogether.",
    "originalFile": "\\section{Discussion and Conclusion}\\label{sec:conclusion}\n\nAcross 100+ experiments and 6000+ evaluation episodes on two VLA model families, three findings converge: current VLA safety evaluation is structurally unreliable. Action collapse renders reported CAR illusory (\\S\\ref{sec:dfcar}); EE-only oracle refinement is counterproductive (\\S\\ref{sec:ee_only}); and collision-free demonstrations account for nearly all measured avoidance gains, with EE-only SDF contributing no statistically significant improvement (\\S\\ref{sec:avoidance_source}).\n\n\\paragraph{Why EE-only SDF fails.}\nTwo independent causes explain the null result. \\textit{(i)~Demonstration data largely subsumes the SDF signal.} Collision-free demonstrations implicitly encode spatial avoidance; the ${\\sim}$26\\,pp CAR gain arises primarily from this distributional shift, with per-task ordering invariant across all SDF conditions (\\S\\ref{sec:avoidance_source}). Even at $\\lambda = 0.1$ (20$\\times$ the lowest tested weight), CAR remains within the null distribution ($p = 0.131$), suggesting that EE-only auxiliary SDF loss does not overcome Level~A signal masking---the limitation is architectural for this integration pathway. \\textit{(ii)~EE monitoring cannot prevent full-body collisions.} The SDF gradient acts on a single point while collisions occur along intermediate links. Oracle experiments confirm this: ground-truth SDF refinement \\emph{reduces} CAR by 6--10\\,pp below unrefined baselines (\\S\\ref{sec:ee_only}), because pushing the EE away rotates unmonitored links through obstacles. We hypothesize that collision-free demonstration trajectories implicitly encode workspace priors through their spatial distribution: the robot learns to favor regions of the workspace that are inherently collision-free, without requiring explicit geometric supervision. These two causes are independent; effective geometric safety requires both full-body supervision and training signals beyond demonstrations. The failure of EE-only auxiliary SDF loss is architectural; constraint-based and runtime filtering approaches bypass this structural limitation through fundamentally different integration mechanisms.\n\n\\paragraph{Implications for evaluation.}\ndfCAR corrects action-collapse contamination using only EE position logging, already available in most evaluation pipelines. The bimodal displacement distribution makes $\\tau_d$ robust across five orders of magnitude. We recommend reporting both CAR and dfCAR; the gap quantifies contamination. This contamination spans a 4000$\\times$ parameter range (Pi0 Full-FT ${\\sim}$2.5B to Pi0+A1 ${\\sim}$658K trainable), a structural consequence of evaluating avoidance without verifying motion. More broadly, safety may need to operate at the planning or joint-space constraint layer, since any EE-centric loss inherits the same blind spot.\n\n\\paragraph{Scope and generalizability.} Our findings are drawn from a single benchmark (SafeLIBERO) covering two VLA model families and four pick-and-place manipulation tasks in MuJoCo simulation. The action-collapse mechanism (Claim~1) is structurally general---any policy prone to action collapse will inflate CAR under standard evaluation---but its prevalence across other benchmarks, task types, and real hardware remains an open question. The SDF redundancy finding (Claim~3) is specific to EE-only auxiliary loss integration and should not be extrapolated to alternative SDF integration pathways (Section~\\ref{sec:related}).\n\n\\paragraph{Limitations.}\nAll experiments are conducted in MuJoCo simulation within the SafeLIBERO benchmark. The sim-to-real gap introduces uncertainty: collision detection precision differs between simulation and physical hardware, sensor noise may affect displacement-filtered CAR differently on real robots, and the prevalence of action collapse in physical deployments remains untested. Our evaluation covers only four pick-and-place manipulation tasks with tabletop obstacles; whether the findings generalize to more diverse task families (e.g., bi-manual manipulation, deformable objects, dynamic obstacles) is an open question. Statistical power is limited by $n{=}3$ training seeds per condition, yielding a minimum detectable effect of approximately 5 percentage points at 80\\% power---smaller genuine effects, if they exist, would not be detected at this sample size. Oracle experiments used a largely action-collapsed model (Pi0+A1, TSR${\\approx}$0\\%); testing on an actively moving policy would better isolate the structural limitation. Full-body SDF remains untested. Fine-tuning degrades TSR by ${\\sim}$18--20\\,pp, yet SSR/TSR increases from 0.39 to 0.51--0.60 (Appendix~\\ref{sec:appendix_ssr}); reduced exposure alone does not explain the pattern.\n\n\\paragraph{Future work.}\nThree directions follow: (1) full-body SDF supervision along the kinematic chain; (2) cross-architecture evaluation on OpenVLA, RT-2, and other VLA families; (3) planning-layer safety constraints in joint space rather than EE space.\n\n\\paragraph{Broader impact.}\nThe displacement-filtered CAR metric (dfCAR) is intended as a diagnostic complement to standard CAR, not a replacement; practitioners should report both metrics to distinguish genuine avoidance from action-collapse artifacts. Our finding that EE-only SDF supervision is redundant with demonstration data is an evaluation-methodology insight, not a verdict against safety-aware training---geometric supervision may prove effective through alternative integration pathways or with full-body collision surfaces. We caution against interpreting these results as evidence that VLA safety research is futile; rather, they highlight the need for evaluation protocols that can reliably separate safety improvements from measurement artifacts.\n",
    "structuredPatch": [
      {
        "oldStart": 3,
        "oldLines": 7,
        "newStart": 3,
        "newLines": 7,
        "lines": [
          " Across 100+ experiments and 6000+ evaluation episodes on two VLA model families, three findings converge: current VLA safety evaluation is structurally unreliable. Action collapse renders reported CAR illusory (\\S\\ref{sec:dfcar}); EE-only oracle refinement is counterproductive (\\S\\ref{sec:ee_only}); and collision-free demonstrations account for nearly all measured avoidance gains, with EE-only SDF contributing no statistically significant improvement (\\S\\ref{sec:avoidance_source}).",
          " ",
          " \\paragraph{Why EE-only SDF fails.}",
          "-Two independent causes explain the null result. \\textit{(i)~Demonstration data largely subsumes the SDF signal.} Collision-free demonstrations implicitly encode spatial avoidance; the ${\\sim}$26\\,pp CAR gain arises primarily from this distributional shift, with per-task ordering invariant across all SDF conditions (\\S\\ref{sec:avoidance_source}). Even at $\\lambda = 0.1$ (20$\\times$ the lowest tested weight), CAR remains within the null distribution ($p = 0.131$), suggesting that EE-only auxiliary SDF loss does not overcome Level~A signal masking---the limitation is architectural for this integration pathway. \\textit{(ii)~EE monitoring cannot prevent full-body collisions.} The SDF gradient acts on a single point while collisions occur along intermediate links. Oracle experiments confirm this: ground-truth SDF refinement \\emph{reduces} CAR by 6--10\\,pp below unrefined baselines (\\S\\ref{sec:ee_only}), because pushing the EE away rotates unmonitored links through obstacles. We hypothesize that collision-free demonstration trajectories implicitly encode workspace priors through their spatial distribution: the robot learns to favor regions of the workspace that are inherently collision-free, without requiring explicit geometric supervision. These two causes are independent; effective geometric safety requires both full-body supervision and training signals beyond demonstrations. The failure of EE-only auxiliary SDF loss is architectural; constraint-based and runtime filtering approaches bypass this structural limitation through fundamentally different integration mechanisms.",
          "+Two independent causes explain the null result. \\textit{(i)~Demonstration data largely subsumes the SDF signal.} Collision-free demonstrations implicitly encode spatial avoidance; the ${\\sim}$26\\,pp CAR gain arises primarily from this distributional shift, with per-task ordering invariant across all SDF conditions (\\S\\ref{sec:avoidance_source}). Even at $\\lambda = 0.1$ (20$\\times$ the lowest tested weight), CAR remains within the null distribution ($p = 0.131$), suggesting that EE-only auxiliary SDF loss does not overcome Level~A signal masking---the limitation is architectural for this integration pathway. \\textit{(ii)~EE monitoring cannot prevent full-body collisions.} The SDF gradient acts on a single point while collisions occur along intermediate links. Oracle experiments confirm this: ground-truth SDF refinement \\emph{reduces} CAR by 6--10\\,pp below unrefined baselines (\\S\\ref{sec:ee_only}), because pushing the EE away rotates unmonitored links through obstacles. We hypothesize that collision-free demonstration trajectories implicitly encode workspace priors through their spatial distribution: the robot learns to favor regions of the workspace that are inherently collision-free, without requiring explicit geometric supervision. These two causes are independent; effective geometric safety requires both full-body supervision and training signals beyond demonstrations. The failure of EE-only auxiliary SDF loss is architectural. Constrained-optimization approaches (e.g., SafeVLA) address collision avoidance through a fundamentally different optimization paradigm---directly constraining violation probability rather than adding geometric supervision---while runtime filtering sidesteps training altogether.",
          " ",
          " \\paragraph{Implications for evaluation.}",
          " dfCAR corrects action-collapse contamination using only EE position logging, already available in most evaluation pipelines. The bimodal displacement distribution makes $\\tau_d$ robust across five orders of magnitude. We recommend reporting both CAR and dfCAR; the gap quantifies contamination. This contamination spans a 4000$\\times$ parameter range (Pi0 Full-FT ${\\sim}$2.5B to Pi0+A1 ${\\sim}$658K trainable), a structural consequence of evaluating avoidance without verifying motion. More broadly, safety may need to operate at the planning or joint-space constraint layer, since any EE-centric loss inherits the same blind spot."
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

_source line 69_

P0 #1 done. Now **P1 #3** — remaining "redundant" instances (discussion.tex L20, L11; appendix.tex L229, L235):

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "137193e0-6cf8-497b-b10d-55c6582d0e7d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016yyGBFbqpQDyq3iRdN71nw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3310,
      "cache_read_input_tokens": 51416,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3310
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

_source line 70_

<details open><summary>🔧 Tool call — Edit · `toolu_013jjJKTRmzCr9c1XSwMvTgs`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex",
  "old_string": "Our finding that EE-only SDF supervision is redundant with demonstration data",
  "new_string": "Our finding that EE-only SDF supervision is redundant at the tested scale with demonstration data"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "d6e52b1a-65d2-4ba3-b811-27e7c83f746e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016yyGBFbqpQDyq3iRdN71nw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3310,
      "cache_read_input_tokens": 51416,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3310
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

_source line 71 · 2026-05-28T06:52:33.268Z_

<details><summary>↩ Tool result · `toolu_013jjJKTRmzCr9c1XSwMvTgs`</summary>

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
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "98a987ef-75c3-408c-b10f-9c633edcf82b",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex",
    "oldString": "Our finding that EE-only SDF supervision is redundant with demonstration data",
    "newString": "Our finding that EE-only SDF supervision is redundant at the tested scale with demonstration data",
    "originalFile": "\\section{Discussion and Conclusion}\\label{sec:conclusion}\n\nAcross 100+ experiments and 6000+ evaluation episodes on two VLA model families, three findings converge: current VLA safety evaluation is structurally unreliable. Action collapse renders reported CAR illusory (\\S\\ref{sec:dfcar}); EE-only oracle refinement is counterproductive (\\S\\ref{sec:ee_only}); and collision-free demonstrations account for nearly all measured avoidance gains, with EE-only SDF contributing no statistically significant improvement (\\S\\ref{sec:avoidance_source}).\n\n\\paragraph{Why EE-only SDF fails.}\nTwo independent causes explain the null result. \\textit{(i)~Demonstration data largely subsumes the SDF signal.} Collision-free demonstrations implicitly encode spatial avoidance; the ${\\sim}$26\\,pp CAR gain arises primarily from this distributional shift, with per-task ordering invariant across all SDF conditions (\\S\\ref{sec:avoidance_source}). Even at $\\lambda = 0.1$ (20$\\times$ the lowest tested weight), CAR remains within the null distribution ($p = 0.131$), suggesting that EE-only auxiliary SDF loss does not overcome Level~A signal masking---the limitation is architectural for this integration pathway. \\textit{(ii)~EE monitoring cannot prevent full-body collisions.} The SDF gradient acts on a single point while collisions occur along intermediate links. Oracle experiments confirm this: ground-truth SDF refinement \\emph{reduces} CAR by 6--10\\,pp below unrefined baselines (\\S\\ref{sec:ee_only}), because pushing the EE away rotates unmonitored links through obstacles. We hypothesize that collision-free demonstration trajectories implicitly encode workspace priors through their spatial distribution: the robot learns to favor regions of the workspace that are inherently collision-free, without requiring explicit geometric supervision. These two causes are independent; effective geometric safety requires both full-body supervision and training signals beyond demonstrations. The failure of EE-only auxiliary SDF loss is architectural. Constrained-optimization approaches (e.g., SafeVLA) address collision avoidance through a fundamentally different optimization paradigm---directly constraining violation probability rather than adding geometric supervision---while runtime filtering sidesteps training altogether.\n\n\\paragraph{Implications for evaluation.}\ndfCAR corrects action-collapse contamination using only EE position logging, already available in most evaluation pipelines. The bimodal displacement distribution makes $\\tau_d$ robust across five orders of magnitude. We recommend reporting both CAR and dfCAR; the gap quantifies contamination. This contamination spans a 4000$\\times$ parameter range (Pi0 Full-FT ${\\sim}$2.5B to Pi0+A1 ${\\sim}$658K trainable), a structural consequence of evaluating avoidance without verifying motion. More broadly, safety may need to operate at the planning or joint-space constraint layer, since any EE-centric loss inherits the same blind spot.\n\n\\paragraph{Scope and generalizability.} Our findings are drawn from a single benchmark (SafeLIBERO) covering two VLA model families and four pick-and-place manipulation tasks in MuJoCo simulation. The action-collapse mechanism (Claim~1) is structurally general---any policy prone to action collapse will inflate CAR under standard evaluation---but its prevalence across other benchmarks, task types, and real hardware remains an open question. The SDF redundancy finding (Claim~3) is specific to EE-only auxiliary loss integration and should not be extrapolated to alternative SDF integration pathways (Section~\\ref{sec:related}).\n\n\\paragraph{Limitations.}\nAll experiments are conducted in MuJoCo simulation within the SafeLIBERO benchmark. The sim-to-real gap introduces uncertainty: collision detection precision differs between simulation and physical hardware, sensor noise may affect displacement-filtered CAR differently on real robots, and the prevalence of action collapse in physical deployments remains untested. Our evaluation covers only four pick-and-place manipulation tasks with tabletop obstacles; whether the findings generalize to more diverse task families (e.g., bi-manual manipulation, deformable objects, dynamic obstacles) is an open question. Statistical power is limited by $n{=}3$ training seeds per condition, yielding a minimum detectable effect of approximately 5 percentage points at 80\\% power---smaller genuine effects, if they exist, would not be detected at this sample size. Oracle experiments used a largely action-collapsed model (Pi0+A1, TSR${\\approx}$0\\%); testing on an actively moving policy would better isolate the structural limitation. Full-body SDF remains untested. Fine-tuning degrades TSR by ${\\sim}$18--20\\,pp, yet SSR/TSR increases from 0.39 to 0.51--0.60 (Appendix~\\ref{sec:appendix_ssr}); reduced exposure alone does not explain the pattern.\n\n\\paragraph{Future work.}\nThree directions follow: (1) full-body SDF supervision along the kinematic chain; (2) cross-architecture evaluation on OpenVLA, RT-2, and other VLA families; (3) planning-layer safety constraints in joint space rather than EE space.\n\n\\paragraph{Broader impact.}\nThe displacement-filtered CAR metric (dfCAR) is intended as a diagnostic complement to standard CAR, not a replacement; practitioners should report both metrics to distinguish genuine avoidance from action-collapse artifacts. Our finding that EE-only SDF supervision is redundant with demonstration data is an evaluation-methodology insight, not a verdict against safety-aware training---geometric supervision may prove effective through alternative integration pathways or with full-body collision surfaces. We caution against interpreting these results as evidence that VLA safety research is futile; rather, they highlight the need for evaluation protocols that can reliably separate safety improvements from measurement artifacts.\n",
    "structuredPatch": [
      {
        "oldStart": 17,
        "oldLines": 4,
        "newStart": 17,
        "newLines": 4,
        "lines": [
          " Three directions follow: (1) full-body SDF supervision along the kinematic chain; (2) cross-architecture evaluation on OpenVLA, RT-2, and other VLA families; (3) planning-layer safety constraints in joint space rather than EE space.",
          " ",
          " \\paragraph{Broader impact.}",
          "-The displacement-filtered CAR metric (dfCAR) is intended as a diagnostic complement to standard CAR, not a replacement; practitioners should report both metrics to distinguish genuine avoidance from action-collapse artifacts. Our finding that EE-only SDF supervision is redundant with demonstration data is an evaluation-methodology insight, not a verdict against safety-aware training---geometric supervision may prove effective through alternative integration pathways or with full-body collision surfaces. We caution against interpreting these results as evidence that VLA safety research is futile; rather, they highlight the need for evaluation protocols that can reliably separate safety improvements from measurement artifacts.",
          "+The displacement-filtered CAR metric (dfCAR) is intended as a diagnostic complement to standard CAR, not a replacement; practitioners should report both metrics to distinguish genuine avoidance from action-collapse artifacts. Our finding that EE-only SDF supervision is redundant at the tested scale with demonstration data is an evaluation-methodology insight, not a verdict against safety-aware training---geometric supervision may prove effective through alternative integration pathways or with full-body collision surfaces. We caution against interpreting these results as evidence that VLA safety research is futile; rather, they highlight the need for evaluation protocols that can reliably separate safety improvements from measurement artifacts."
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

### Tool call

_source line 72_

<details open><summary>🔧 Tool call — Edit · `toolu_01DsmWQyJHQoAsxF5F9oJkYv`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex",
  "old_string": "The SDF redundancy finding (Claim~3)",
  "new_string": "The finding that EE-only SDF shows no significant benefit (Claim~3)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "12dab2a0-40da-41f1-a7a3-d8560453c600",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016yyGBFbqpQDyq3iRdN71nw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3310,
      "cache_read_input_tokens": 51416,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3310
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

_source line 73 · 2026-05-28T06:52:34.628Z_

<details><summary>↩ Tool result · `toolu_01DsmWQyJHQoAsxF5F9oJkYv`</summary>

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
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "907adbc0-f846-4ec7-baa3-8b0d7de83538",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex",
    "oldString": "The SDF redundancy finding (Claim~3)",
    "newString": "The finding that EE-only SDF shows no significant benefit (Claim~3)",
    "originalFile": "\\section{Discussion and Conclusion}\\label{sec:conclusion}\n\nAcross 100+ experiments and 6000+ evaluation episodes on two VLA model families, three findings converge: current VLA safety evaluation is structurally unreliable. Action collapse renders reported CAR illusory (\\S\\ref{sec:dfcar}); EE-only oracle refinement is counterproductive (\\S\\ref{sec:ee_only}); and collision-free demonstrations account for nearly all measured avoidance gains, with EE-only SDF contributing no statistically significant improvement (\\S\\ref{sec:avoidance_source}).\n\n\\paragraph{Why EE-only SDF fails.}\nTwo independent causes explain the null result. \\textit{(i)~Demonstration data largely subsumes the SDF signal.} Collision-free demonstrations implicitly encode spatial avoidance; the ${\\sim}$26\\,pp CAR gain arises primarily from this distributional shift, with per-task ordering invariant across all SDF conditions (\\S\\ref{sec:avoidance_source}). Even at $\\lambda = 0.1$ (20$\\times$ the lowest tested weight), CAR remains within the null distribution ($p = 0.131$), suggesting that EE-only auxiliary SDF loss does not overcome Level~A signal masking---the limitation is architectural for this integration pathway. \\textit{(ii)~EE monitoring cannot prevent full-body collisions.} The SDF gradient acts on a single point while collisions occur along intermediate links. Oracle experiments confirm this: ground-truth SDF refinement \\emph{reduces} CAR by 6--10\\,pp below unrefined baselines (\\S\\ref{sec:ee_only}), because pushing the EE away rotates unmonitored links through obstacles. We hypothesize that collision-free demonstration trajectories implicitly encode workspace priors through their spatial distribution: the robot learns to favor regions of the workspace that are inherently collision-free, without requiring explicit geometric supervision. These two causes are independent; effective geometric safety requires both full-body supervision and training signals beyond demonstrations. The failure of EE-only auxiliary SDF loss is architectural. Constrained-optimization approaches (e.g., SafeVLA) address collision avoidance through a fundamentally different optimization paradigm---directly constraining violation probability rather than adding geometric supervision---while runtime filtering sidesteps training altogether.\n\n\\paragraph{Implications for evaluation.}\ndfCAR corrects action-collapse contamination using only EE position logging, already available in most evaluation pipelines. The bimodal displacement distribution makes $\\tau_d$ robust across five orders of magnitude. We recommend reporting both CAR and dfCAR; the gap quantifies contamination. This contamination spans a 4000$\\times$ parameter range (Pi0 Full-FT ${\\sim}$2.5B to Pi0+A1 ${\\sim}$658K trainable), a structural consequence of evaluating avoidance without verifying motion. More broadly, safety may need to operate at the planning or joint-space constraint layer, since any EE-centric loss inherits the same blind spot.\n\n\\paragraph{Scope and generalizability.} Our findings are drawn from a single benchmark (SafeLIBERO) covering two VLA model families and four pick-and-place manipulation tasks in MuJoCo simulation. The action-collapse mechanism (Claim~1) is structurally general---any policy prone to action collapse will inflate CAR under standard evaluation---but its prevalence across other benchmarks, task types, and real hardware remains an open question. The SDF redundancy finding (Claim~3) is specific to EE-only auxiliary loss integration and should not be extrapolated to alternative SDF integration pathways (Section~\\ref{sec:related}).\n\n\\paragraph{Limitations.}\nAll experiments are conducted in MuJoCo simulation within the SafeLIBERO benchmark. The sim-to-real gap introduces uncertainty: collision detection precision differs between simulation and physical hardware, sensor noise may affect displacement-filtered CAR differently on real robots, and the prevalence of action collapse in physical deployments remains untested. Our evaluation covers only four pick-and-place manipulation tasks with tabletop obstacles; whether the findings generalize to more diverse task families (e.g., bi-manual manipulation, deformable objects, dynamic obstacles) is an open question. Statistical power is limited by $n{=}3$ training seeds per condition, yielding a minimum detectable effect of approximately 5 percentage points at 80\\% power---smaller genuine effects, if they exist, would not be detected at this sample size. Oracle experiments used a largely action-collapsed model (Pi0+A1, TSR${\\approx}$0\\%); testing on an actively moving policy would better isolate the structural limitation. Full-body SDF remains untested. Fine-tuning degrades TSR by ${\\sim}$18--20\\,pp, yet SSR/TSR increases from 0.39 to 0.51--0.60 (Appendix~\\ref{sec:appendix_ssr}); reduced exposure alone does not explain the pattern.\n\n\\paragraph{Future work.}\nThree directions follow: (1) full-body SDF supervision along the kinematic chain; (2) cross-architecture evaluation on OpenVLA, RT-2, and other VLA families; (3) planning-layer safety constraints in joint space rather than EE space.\n\n\\paragraph{Broader impact.}\nThe displacement-filtered CAR metric (dfCAR) is intended as a diagnostic complement to standard CAR, not a replacement; practitioners should report both metrics to distinguish genuine avoidance from action-collapse artifacts. Our finding that EE-only SDF supervision is redundant at the tested scale with demonstration data is an evaluation-methodology insight, not a verdict against safety-aware training---geometric supervision may prove effective through alternative integration pathways or with full-body collision surfaces. We caution against interpreting these results as evidence that VLA safety research is futile; rather, they highlight the need for evaluation protocols that can reliably separate safety improvements from measurement artifacts.\n",
    "structuredPatch": [
      {
        "oldStart": 8,
        "oldLines": 7,
        "newStart": 8,
        "newLines": 7,
        "lines": [
          " \\paragraph{Implications for evaluation.}",
          " dfCAR corrects action-collapse contamination using only EE position logging, already available in most evaluation pipelines. The bimodal displacement distribution makes $\\tau_d$ robust across five orders of magnitude. We recommend reporting both CAR and dfCAR; the gap quantifies contamination. This contamination spans a 4000$\\times$ parameter range (Pi0 Full-FT ${\\sim}$2.5B to Pi0+A1 ${\\sim}$658K trainable), a structural consequence of evaluating avoidance without verifying motion. More broadly, safety may need to operate at the planning or joint-space constraint layer, since any EE-centric loss inherits the same blind spot.",
          " ",
          "-\\paragraph{Scope and generalizability.} Our findings are drawn from a single benchmark (SafeLIBERO) covering two VLA model families and four pick-and-place manipulation tasks in MuJoCo simulation. The action-collapse mechanism (Claim~1) is structurally general---any policy prone to action collapse will inflate CAR under standard evaluation---but its prevalence across other benchmarks, task types, and real hardware remains an open question. The SDF redundancy finding (Claim~3) is specific to EE-only auxiliary loss integration and should not be extrapolated to alternative SDF integration pathways (Section~\\ref{sec:related}).",
          "+\\paragraph{Scope and generalizability.} Our findings are drawn from a single benchmark (SafeLIBERO) covering two VLA model families and four pick-and-place manipulation tasks in MuJoCo simulation. The action-collapse mechanism (Claim~1) is structurally general---any policy prone to action collapse will inflate CAR under standard evaluation---but its prevalence across other benchmarks, task types, and real hardware remains an open question. The finding that EE-only SDF shows no significant benefit (Claim~3) is specific to EE-only auxiliary loss integration and should not be extrapolated to alternative SDF integration pathways (Section~\\ref{sec:related}).",
          " ",
          " \\paragraph{Limitations.}",
          " All experiments are conducted in MuJoCo simulation within the SafeLIBERO benchmark. The sim-to-real gap introduces uncertainty: collision detection precision differs between simulation and physical hardware, sensor noise may affect displacement-filtered CAR differently on real robots, and the prevalence of action collapse in physical deployments remains untested. Our evaluation covers only four pick-and-place manipulation tasks with tabletop obstacles; whether the findings generalize to more diverse task families (e.g., bi-manual manipulation, deformable objects, dynamic obstacles) is an open question. Statistical power is limited by $n{=}3$ training seeds per condition, yielding a minimum detectable effect of approximately 5 percentage points at 80\\% power---smaller genuine effects, if they exist, would not be detected at this sample size. Oracle experiments used a largely action-collapsed model (Pi0+A1, TSR${\\approx}$0\\%); testing on an actively moving policy would better isolate the structural limitation. Full-body SDF remains untested. Fine-tuning degrades TSR by ${\\sim}$18--20\\,pp, yet SSR/TSR increases from 0.39 to 0.51--0.60 (Appendix~\\ref{sec:appendix_ssr}); reduced exposure alone does not explain the pattern."
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

### Tool call

_source line 74_

<details open><summary>🔧 Tool call — Edit · `toolu_018PjP3XcwfTmnz1tyQhQdqW`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex",
  "old_string": "To test whether the SDF redundancy finding generalizes",
  "new_string": "To test whether the absence of EE-only SDF benefit generalizes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "ec00c9a4-dadf-46bc-9afc-61aefbb6f631",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016yyGBFbqpQDyq3iRdN71nw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3310,
      "cache_read_input_tokens": 51416,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3310
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

_source line 75 · 2026-05-28T06:52:36.564Z_

<details><summary>↩ Tool result · `toolu_018PjP3XcwfTmnz1tyQhQdqW`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "77bb0795-1e2a-45f5-8681-a984714e0ed7",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex",
    "oldString": "To test whether the SDF redundancy finding generalizes",
    "newString": "To test whether the absence of EE-only SDF benefit generalizes",
    "originalFile": "\\section{Displacement Distribution}\n\\label{sec:appendix_displacement}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\linewidth]{fig2_ee_displacement_distribution}\n\\caption{Displacement distribution across evaluation episodes. Pi0-family models (blue) cluster below 1\\,$\\mu$m, while Pi0.5 episodes (orange) exceed 200\\,mm. The five-order-of-magnitude gap makes $\\tau_d$ robust to any value in $[2, 200]$\\,mm.}\n\\label{fig:displacement}\n\\end{figure}\n\n\\section{Displacement Threshold Sensitivity Analysis}\n\\label{sec:appendix_threshold}\n\nTo validate the robustness of our displacement threshold $\\tau_d$, we evaluate the action-collapse rate across four orders of magnitude. Table~\\ref{tab:threshold_sensitivity} shows that the action-collapse pattern persists across all reasonable threshold choices: A1-LoRA exhibits near-total action collapse regardless of threshold, while Pi0.5+A1 maintains 0\\% action-collapse rate even at the most conservative setting.\n\n\\begin{table}[h]\n\\centering\n\\caption{Action-collapse rate (\\% of episodes with $d_\\mathrm{max} < \\tau_d$) across threshold values.}\n\\label{tab:threshold_sensitivity}\n\\begin{tabular}{lccc}\n\\toprule\n$\\tau_d$ & A1-LoRA (Pi0) & Pi0.5 Baseline & Pi0.5+A1 (SDF aux) \\\\\n\\midrule\n0.001 mm (1\\,$\\mu$m) & 73.9 & 0.0 & 0.0 \\\\\n0.1 mm  & 99.6 & 0.0 & 0.0 \\\\\n1.0 mm  & 100.0 & 0.0 & 0.0 \\\\\n10 mm   & 100.0 & 0.0 & 0.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe choice of $\\tau_d = 0.1$\\,mm represents a conservative threshold: displacement below this value is physically negligible in manipulation tasks where typical action magnitudes are 1--10\\,mm per step. Even at $\\tau_d = 1$\\,$\\mu$m, 73.9\\% of A1-LoRA safe episodes are classified as action-collapsed, while all Pi0.5 episodes remain above threshold at every level tested.\n\nTable~\\ref{tab:dfcar_threshold} extends this analysis to dfCAR across fine-tuned Pi0.5 configurations. All eight model-seed combinations yield identical dfCAR for $\\tau_d \\in [2, 200]$\\,mm. At $\\tau_d = 300$\\,mm, 0--2 episodes per seed fall below threshold (displacement 200--300\\,mm), causing $\\leq$0.5\\,pp deviation. Our conclusions hold across the entire tested range.\n\n\\begin{table}[h]\n\\centering\n\\caption{dfCAR (\\%) across displacement thresholds for fine-tuned Pi0.5 configurations ($n = 200$ episodes per seed). Values are identical across $\\tau_d \\in [2, 200]$\\,mm; at $\\tau_d = 300$\\,mm, at most 2 episodes are excluded.}\n\\label{tab:dfcar_threshold}\n\\vspace{2pt}\n\\footnotesize\n\\begin{tabular}{lcccccccc}\n\\toprule\n& \\multicolumn{8}{c}{$\\tau_d$ (mm)} \\\\\n\\cmidrule(lr){2-9}\nCondition & 2 & 5 & 10 & 20 & 50 & 100 & 200 & 300 \\\\\n\\midrule\nLoRA s0            & 56.5 & 56.5 & 56.5 & 56.5 & 56.5 & 56.5 & 56.5 & 56.5 \\\\\nLoRA s1            & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 \\\\\nSDF $\\lambda{=}0.005$ s0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.1 \\\\\nSDF $\\lambda{=}0.005$ s1 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 \\\\\nSDF $\\lambda{=}0.005$ s2 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.3 \\\\\nSDF $\\lambda{=}0.01$ s0  & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 \\\\\nSDF $\\lambda{=}0.01$ s1  & 57.5 & 57.5 & 57.5 & 57.5 & 57.5 & 57.5 & 57.5 & 57.1 \\\\\nSDF $\\lambda{=}0.01$ s2  & 54.5 & 54.5 & 54.5 & 54.5 & 54.5 & 54.5 & 54.5 & 54.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Per-Task TSR Breakdown}\\label{sec:appendix_tsr_pertask}\n\nTable~\\ref{tab:per_task_tsr} decomposes TSR by task for the avoidance source attribution experiments (Section~\\ref{sec:avoidance_source}). All tasks retain meaningful success rates after fine-tuning, with Chocolate Pudding most resilient and Orange Juice most affected.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-task TSR (\\%) at 30K training steps. Baseline reports the unified seed-7 re-evaluation (aggregate TSR\\,=\\,71.5\\%). LoRA-only reports 3-seed means (re-evaluated with unified seed-7 protocol); SDF conditions report 3-seed means.}\n\\label{tab:per_task_tsr}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nTask & Pi0.5 Base & LoRA-only & SDF $\\lambda{=}0.005$ & SDF $\\lambda{=}0.01$ \\\\\n & (seed\\,=\\,7) & (3 seeds) & (3 seeds) & (3 seeds) \\\\\n\\midrule\nOrange Juice      & 74.0 & 30.0 & 33.3 & 24.7 \\\\\nChoco.\\ Pudding   & 80.0 & 70.7 & 78.0 & 76.7 \\\\\nMilk              & 66.0 & 44.7 & 35.3 & 48.7 \\\\\nBBQ Sauce         & 66.0 & 60.7 & 69.3 & 65.3 \\\\\n\\midrule\nMean              & 71.5 & 51.5 & 54.0 & 53.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Per-Task CAR Breakdown}\\label{sec:appendix_pertask_car}\n\nTable~\\ref{tab:per_task_car} decomposes CAR by task for all fine-tuned conditions, supporting the claim that per-task ordering is preserved across SDF loss weights (\\S\\ref{sec:avoidance_source}). Chocolate Pudding is consistently highest and BBQ Sauce consistently lowest across all conditions, including $\\lambda = 0.1$. The intermediate tasks (Orange Juice and Milk) exchange rank between seeds but remain bounded by the extremes. This invariance indicates that avoidance patterns reflect the spatial statistics of collision-free demonstrations rather than geometric supervision.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-task CAR (\\%) at 30K steps. $\\lambda{=}0.005$, $\\lambda{=}0.01$, and $\\lambda{=}0.1$ report 3-seed means alongside individual seeds. Per-task ordering (CP highest, BBQ lowest) is preserved across all conditions.}\n\\label{tab:per_task_car}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nCondition & OJ & CP & Milk & BBQ & Agg. \\\\\n\\midrule\nLoRA s0 & 56 & 74 & 70 & 26 & 56.5 \\\\\nLoRA s1 & 54 & 68 & 72 & 16 & 52.5 \\\\\nLoRA s2 & 56 & 76 & 62 & 26 & 55.0 \\\\\nSDF $\\lambda{=}0.005$ (3-seed) & 54.0 & 72.7 & 71.3 & 20.0 & 54.5 \\\\\nSDF $\\lambda{=}0.01$ (3-seed) & 57.3 & 72.7 & 72.0 & 23.3 & 56.3 \\\\\nSDF $\\lambda{=}0.1$ s0 & 60 & 74 & 68 & 30 & 58.0 \\\\\nSDF $\\lambda{=}0.1$ s1 & 66 & 72 & 70 & 26 & 58.5 \\\\\nSDF $\\lambda{=}0.1$ s2 & 56 & 76 & 70 & 16 & 54.5 \\\\\nSDF $\\lambda{=}0.1$ (3-seed) & 60.7 & 74.0 & 69.3 & 24.0 & 57.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nFor the $\\lambda = 0.1$ condition, seed~1 records \\texttt{avg\\_max\\_obstacle\\_displacement} of 0.0553\\,m (per-task: OJ\\,=\\,0.033, CP\\,=\\,0.055, Milk\\,=\\,0.041, BBQ\\,=\\,0.093), comparable to other fine-tuned conditions and consistent with active manipulation rather than action-collapsed behavior.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{fig_pertask_car_fingerprint}\n\\caption{Per-task CAR fingerprint across conditions. Each bar shows the 3-seed mean; dots indicate individual seeds. The task ordering (chocolate\\_pudding highest, bbq\\_sauce lowest) is preserved across all $\\lambda$ values, confirming that avoidance patterns reflect the demonstration distribution rather than geometric supervision. LoRA-only: 3-seed mean.}\n\\label{fig:pertask_fingerprint}\n\\end{figure}\n\n\\section{Safe Success Rate Analysis}\\label{sec:appendix_ssr}\n\nTable~\\ref{tab:ssr} reports the Safe Success Rate (SSR\\,=\\,TSR\\,$\\cap$\\,CAR), the fraction of episodes achieving both task completion and collision avoidance. The SSR/TSR ratio quantifies the proportion of successful episodes that are also collision-free, controlling for task-completion rate.\n\n\\begin{table}[h]\n\\centering\n\\caption{SSR and SSR/TSR ratio across conditions. The ratio increase from 0.39 (baseline) to 0.51--0.60 (fine-tuned) indicates that CAR gains reflect learned safer execution, not reduced task exposure.}\n\\label{tab:ssr}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nCondition & TSR (\\%) & CAR (\\%) & SSR (\\%) & SSR/TSR \\\\\n\\midrule\nPi0.5 baseline & 71.5 & 28.5 & 28.0 & 0.39 \\\\\nLoRA-only (3 seeds) & 51.5 & 54.67 & 27.7 & 0.54 \\\\\nSDF $\\lambda{=}0.005$ (3 seeds) & 54.0 & 54.5 & 27.8 & 0.51 \\\\\nSDF $\\lambda{=}0.01$ (3 seeds) & 53.8 & 56.33 & 30.2 & 0.56 \\\\\nSDF $\\lambda{=}0.1$ (3 seeds) & 50.2 & 57.00 & 30.2 & 0.60 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Per-Task Oracle Analysis}\n\\label{sec:appendix_pertask}\n\\label{sec:appendix_pertask_oracle}\n\nTable~\\ref{tab:oracle_pertask} shows per-task CAR for oracle refinement. On task~1 (\\texttt{chocolate\\_pudding}), where the EE is the primary collision body and the LoRA baseline achieves only 46.0\\% CAR, Oracle-adaptive improves to 55.0\\% and Oracle-feature to 47.5\\%. On the remaining tasks, all oracle variants degrade: Oracle-adaptive reduces task~0 (\\texttt{orange\\_juice}) from 96.0\\% to 82.5\\% and task~2 (\\texttt{milk}) from 98.0\\% to 77.5\\%. The SDF gradient pushes the EE away from the nearest surface, but the resulting joint-space displacement rotates intermediate arm links into obstacle volumes.\n\nThe feature-space oracle fires on nearly every timestep (241.7 refinements/episode vs.\\ 14.2 for Cartesian variants) but with gradient magnitudes two orders of magnitude smaller (0.004--0.006 vs.\\ 0.18--0.49), and CAR (76.9\\%) shows no advantage despite 17$\\times$ more steps. The A3 learned SDF never triggers refinement (0 steps/episode), as its outputs avoid the activation threshold.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-task CAR (\\%) for oracle SDF refinement variants. EE-only refinement helps only on task~1 where the EE is the primary collision body; on other tasks it trades one collision site for another.}\n\\label{tab:oracle_pertask}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nMethod & Task 0 & Task 1 & Task 2 & Task 3 & Agg. \\\\\n\\midrule\nLoRA baseline & 96.0 & 46.0 & 98.0 & 88.0 & 82.0 \\\\\n\\midrule\nOracle-adaptive & 82.5 & 55.0 & 77.5 & 85.0 & 75.0 \\\\\nOracle-fixed & 85.0 & 50.0 & 77.5 & 80.0 & 73.1 \\\\\nOracle-feature & 90.0 & 47.5 & 82.5 & 87.5 & 76.9 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Null Distribution for SDF Loss Weight Analysis}\n\\label{sec:appendix_null}\n\nWe construct a null distribution by pooling the three LoRA-only seeds and three $\\lambda = 0.005$ seeds into six per-seed CAR measurements: 56.5\\% (LoRA s0, re-evaluated), 52.5\\% (LoRA s1), 55.0\\% (LoRA s2), 57.0\\% ($\\lambda{=}0.005$ s0), 54.0\\% ($\\lambda{=}0.005$ s1), 52.5\\% ($\\lambda{=}0.005$ s2), yielding mean 54.58\\% and standard deviation 1.93\\% (Bessel-corrected, $n{-}1 = 5$). We treat these as exchangeable because SDF at $\\lambda = 0.005$ produces no separation from LoRA-only. The $\\lambda = 0.01$ mean of 56.33\\% falls within $0.8\\sigma$ of this null ($p > 0.1$), consistent with seed-to-seed variation rather than a treatment effect. The $\\lambda = 0.1$ 30K mean of 57.00\\% (3 seeds: 58.0\\%, 58.5\\%, 54.5\\%) yields a two-tailed permutation $p = 0.131$ (one-tailed $p = 0.071$). The result is non-significant at conventional thresholds ($\\alpha = 0.05$).\n\nThe permutation test makes no distributional assumptions. Pooling the six null values $\\{56.5, 52.5, 55, 57, 54, 52.5\\}$ and three $\\lambda = 0.1$ values $\\{58, 58.5, 54.5\\}$ into nine measurements, we enumerate all $\\binom{9}{3} = 84$ three-element combinations and compute the fraction whose mean $\\geq 57.00$. Six combinations meet this threshold, yielding an exact one-tailed permutation $p = 6/84 \\approx 0.071$. For the two-tailed test, we additionally count combinations on the lower tail with equal or greater distance from the pooled mean, yielding $p = 11/84 \\approx 0.131$. With the third seed ($s_2 = 54.5\\%$) pulling the $\\lambda = 0.1$ mean from 58.25\\% (2 seeds) down to 57.00\\%, the marginal signal observed at $n = 2$ dissolves into seed-to-seed variance.\n\n\\paragraph{Alternative null construction (Null~A).}\nIf only the three LoRA-only seeds are used as the null pool ($\\{56.5, 52.5, 55.0\\}$), we obtain $\\binom{6}{3} = 20$ permutations for each comparison. For $\\lambda = 0.1$ (treatment mean 57.00\\%): one-tailed $p = 3/20 = 0.150$, two-tailed $p = 6/20 = 0.300$. For $\\lambda = 0.01$ (treatment mean 56.33\\%): one-tailed $p = 4/20 = 0.200$, two-tailed $p = 8/20 = 0.400$. Under the broader Null~B pool, $\\lambda = 0.01$ yields one-tailed $p = 10/84 \\approx 0.119$, two-tailed $p = 22/84 \\approx 0.262$. All tests are non-significant at $\\alpha = 0.05$; the narrower Null~A yields \\emph{larger} $p$-values because the LoRA-only pool already contains a high seed (56.5\\%), making the treatment means less extreme by comparison.\n\nA Phase~2 ablation reinforces this conclusion. Setting $\\lambda = 0$ during Phase~2 (steps 5K--18K), so that SDF supervision is active only during auxiliary head warmup (Phase~1, steps 0--5K), yields CAR of 58.0\\% at the 18K checkpoint (13K steps of Phase~2 training, single seed, s2).\\footnote{Full 30K training did not complete due to disk constraints; this result uses the last complete checkpoint at step 18K.} This value lies within the null range, indicating that SDF training produces no lasting behavioral effect on collision avoidance.\n\n\\section{Step-wise Checkpoint Analysis for \\texorpdfstring{$\\lambda = 0.1$}{lambda = 0.1}}\n\\label{sec:appendix_stepwise}\n\nTable~\\ref{tab:stepwise_lambda01} reports per-seed CAR at seven checkpoints for $\\lambda = 0.1$. Seeds~0 and~1 are available at 16K, 20K, 22K, and 30K; 24K--28K report seed-0 only; seed~2 is available at 30K only. The seed-0 curve shows no monotonic trend through 28K. At 30K, the addition of seed~2 (54.5\\%) pulls the three-seed mean to 57.00\\%, within the null band ($p = 0.131$).\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-seed CAR (\\%) at training checkpoints for $\\lambda = 0.1$ (200 episodes each). 24K--28K: seed-0 only. The 30K checkpoint includes all three seeds; the three-seed mean (57.00\\%) remains within the null band ($p = 0.131$, two-tailed permutation).}\n\\label{tab:stepwise_lambda01}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nCheckpoint & Seed 0 & Seed 1 & Seed 2 & Mean \\\\\n\\midrule\n16K steps & 55.5 & 56.0 & -- & 55.75 \\\\\n20K steps & 55.0 & 56.0 & -- & 55.5 \\\\\n22K steps & 60.5 & 56.5 & -- & 58.5 \\\\\n24K steps & 52.5 & -- & -- & -- \\\\\n26K steps & 53.5 & -- & -- & -- \\\\\n28K steps & 54.5 & -- & -- & -- \\\\\n30K steps & 58.0 & 58.5 & 54.5 & 57.00 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nIndividual seeds exhibit checkpoint-to-checkpoint CAR fluctuations of up to 8\\,pp (seed~0: 52.5--60.5\\%), larger than the cross-seed standard deviation at any fixed checkpoint ($\\leq$3\\,pp). This is consistent with binomial sampling noise at $n = 50$ episodes per task ($\\sigma \\approx 7$\\,pp per task for $p \\approx 0.5$). At 30K, the third seed ($s_2 = 54.5\\%$) falls well within the null range, pulling the three-seed mean to 57.00\\% and rendering the earlier two-seed departure non-significant ($p = 0.131$). The seed-averaged curve shows no monotonic trend, confirming that SDF loss weight does not produce a progressive training signal.\n\n\n\\section{Oracle SDF Refinement Details}\n\\label{sec:appendix_oracle}\n\nAll oracle variants replace the learned SDF decoder with ground-truth distance fields computed from the simulation geometry. Each is evaluated for 160 episodes (4 tasks $\\times$ 40).\n\n\\paragraph{Oracle-adaptive.} At each timestep, if the ground-truth SDF at the end-effector position falls below a safety margin, the action is adjusted by a step in the negative SDF gradient direction. The step size $\\alpha$ is scaled inversely with distance: smaller distances produce larger corrections. This mimics an adaptive potential field controller.\n\n\\paragraph{Oracle-fixed.} Identical to Oracle-adaptive except the step size is fixed at $\\alpha = 0.005$ regardless of distance. This isolates the effect of step-size adaptation from the refinement geometry.\n\n\\paragraph{Oracle-feature.} Instead of modifying the action directly in Cartesian space, this variant applies the SDF gradient in the policy's latent feature space via backpropagation. The gradient of the ground-truth SDF value with respect to the intermediate features is computed and used to perturb the features before the action head decodes them. This tests whether geometric corrections are more effective when applied in the model's learned representation space. In practice, the feature-space variant fires on nearly every timestep (241.7 refinements per episode vs.\\ 14.2 for Cartesian variants) but with gradient magnitudes two orders of magnitude smaller (0.004--0.006 vs.\\ 0.18--0.49 in action space).\n\n\n\\section{Cross-Scene Validation: spatial\\_bowl}\n\\label{sec:appendix_spatial_bowl}\n\nTo test whether the SDF redundancy finding generalizes beyond the primary \\texttt{object\\_pudding} scene, we replicate the core comparison on \\texttt{spatial\\_bowl}, a separate SafeLIBERO suite with a distinct obstacle layout (moka pot, wine bottle, milk carton, red coffee mug, yellow book). Both conditions use the same architecture, hyperparameters, and two-phase training schedule (30K steps), differing only in the training scene.\n\nTable~\\ref{tab:spatial_bowl} reports the results. The SDF condition ($\\lambda = 0.005$) yields CAR of 11.5\\% versus 12.0\\% for LoRA-only, a $-$0.5\\,pp difference well within the noise floor, indicating that SDF is essentially identical to LoRA-only on this scene. TSR is comparable across conditions (49.0\\% vs.\\ 51.5\\%). Both evaluations use a single training seed (seed~0) and a single evaluation seed (seed~7, 200 episodes), so statistical power is limited; nevertheless, the qualitative pattern---SDF failing to improve over LoRA-only---is consistent with the \\texttt{object\\_pudding} findings.\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-scene validation on \\texttt{spatial\\_bowl} (single training seed, 200 episodes, 30K checkpoint). The $-$0.5\\,pp CAR difference is well within noise, consistent with the SDF redundancy observed on \\texttt{object\\_pudding}.}\n\\label{tab:spatial_bowl}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nCondition & CAR (\\%) & TSR (\\%) \\\\\n\\midrule\nLoRA-only & 12.0 & 49.0 \\\\\nSDF $\\lambda{=}0.005$ & 11.5 & 51.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe substantially lower CAR on \\texttt{spatial\\_bowl} relative to \\texttt{object\\_pudding} (11--12\\% vs.\\ 54--57\\%) reflects the greater scene difficulty: \\texttt{spatial\\_bowl} places five cluttered obstacles around the workspace, making collision-free manipulation considerably harder. This difficulty affects both conditions equally, and the SDF condition performs comparably ($\\Delta$CAR\\,=\\,$-$0.5\\,pp, well within noise), reinforcing the conclusion that EE-only SDF auxiliary supervision does not produce a meaningful collision avoidance benefit beyond LoRA-only fine-tuning.\n\n\n\\section{Evaluation Seed Robustness}\n\\label{sec:appendix_eval_seed}\n\nTo verify that our conclusions are not artifacts of a particular evaluation seed, we re-evaluate the LoRA-only (s0) and SDF $\\lambda{=}0.1$ (s0) checkpoints under multiple evaluation seeds. Table~\\ref{tab:eval_seed_car} reports aggregate CAR and Table~\\ref{tab:eval_seed_tsr} reports aggregate TSR.\n\n\\begin{table}[h]\n\\centering\n\\caption{Aggregate CAR (\\%) across evaluation seeds (200 episodes each). The LoRA vs.\\ SDF $\\lambda{=}0.1$ ordering is preserved across all tested seeds, and per-task CAR fingerprints (CP highest, BBQ lowest) remain invariant.}\n\\label{tab:eval_seed_car}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\n& \\multicolumn{4}{c}{Per-task CAR (\\%)} & & \\\\\n\\cmidrule(lr){2-5}\nCondition (eval seed) & OJ & CP & Milk & BBQ & Agg. \\\\\n\\midrule\nLoRA s0 (seed\\,=\\,7)   & 56 & 74 & 70 & 26 & 56.5 \\\\\nLoRA s0 (seed\\,=\\,42)  & 60 & 70 & 68 & 28 & 56.5 \\\\\nLoRA s0 (seed\\,=\\,123) & 52 & 74 & 66 & 20 & 53.0 \\\\\nLoRA s0 mean $\\pm$ std & 56.0$\\pm$4.0 & 72.7$\\pm$2.3 & 68.0$\\pm$2.0 & 24.7$\\pm$4.2 & 55.3$\\pm$2.0 \\\\\n\\midrule\nSDF $\\lambda{=}0.1$ s0 (seed\\,=\\,7)   & 60 & 74 & 68 & 30 & 58.0 \\\\\nSDF $\\lambda{=}0.1$ s0 (seed\\,=\\,42)  & 64 & 74 & 74 & 24 & 59.0 \\\\\nSDF $\\lambda{=}0.1$ s0 (seed\\,=\\,123) & 62 & 76 & 74 & 22 & 58.5 \\\\\nSDF $\\lambda{=}0.1$ s0 (seed\\,=\\,256) & 60 & 72 & 66 & 30 & 57.0 \\\\\nSDF $\\lambda{=}0.1$ s0 mean $\\pm$ std & 61.5$\\pm$1.9 & 74.0$\\pm$1.6 & 70.5$\\pm$4.1 & 26.5$\\pm$4.1 & 58.1$\\pm$0.9 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{Aggregate TSR (\\%) across evaluation seeds. TSR varies more across seeds than CAR (seed\\,=\\,42 yields consistently lower TSR), but the relative ordering between LoRA and SDF is stable.}\n\\label{tab:eval_seed_tsr}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\n& \\multicolumn{4}{c}{Per-task TSR (\\%)} & & \\\\\n\\cmidrule(lr){2-5}\nCondition (eval seed) & OJ & CP & Milk & BBQ & Agg. \\\\\n\\midrule\nLoRA s0 (seed\\,=\\,7)   & 32 & 74 & 42 & 58 & 51.5 \\\\\nLoRA s0 (seed\\,=\\,42)  & 22 & 70 & 32 & 60 & 46.0 \\\\\nLoRA s0 (seed\\,=\\,123) & 30 & 70 & 40 & 62 & 50.5 \\\\\nLoRA s0 mean $\\pm$ std & 28.0$\\pm$5.3 & 71.3$\\pm$2.3 & 38.0$\\pm$5.3 & 60.0$\\pm$2.0 & 49.3$\\pm$3.0 \\\\\n\\midrule\nSDF $\\lambda{=}0.1$ s0 (seed\\,=\\,7)   & 28 & 78 & 44 & 60 & 52.5 \\\\\nSDF $\\lambda{=}0.1$ s0 (seed\\,=\\,42)  & 18 & 78 & 42 & 72 & 52.5 \\\\\nSDF $\\lambda{=}0.1$ s0 (seed\\,=\\,123) & 26 & 82 & 38 & 68 & 53.5 \\\\\nSDF $\\lambda{=}0.1$ s0 (seed\\,=\\,256) & 28 & 74 & 32 & 58 & 48.0 \\\\\nSDF $\\lambda{=}0.1$ s0 mean $\\pm$ std & 25.0$\\pm$4.8 & 78.0$\\pm$3.3 & 39.0$\\pm$5.4 & 64.5$\\pm$6.6 & 51.6$\\pm$2.4 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAcross three matched evaluation seeds (7, 42, 123), the SDF $\\lambda{=}0.1$ condition yields higher aggregate CAR than LoRA-only in all cases ($\\Delta$CAR\\,=\\,+1.5, +2.5, +5.5\\,pp). Cross-seed CAR standard deviation is 2.0\\,pp for LoRA and 0.9\\,pp for SDF, both small relative to the within-seed per-task variation. The per-task ordering (CP highest, BBQ lowest) is preserved across all seeds and both conditions, reinforcing the conclusion that avoidance patterns reflect the spatial statistics of training demonstrations.\n\n\n\\section{Training Details}\n\\label{sec:appendix_training}\n\n\\paragraph{Architecture.}\nWe use LoRA~\\citep{hu2022lora} adapters injected into the PaliGemma vision encoder (rank 16, $\\alpha$=16) and the action expert (rank 32, $\\alpha$=32), following the configuration of OpenPi. The SDF decoder is a 4-layer MLP (hidden dimension 256) with skip connections, taking pooled suffix features (1024-d) and query points (3-d) as input. The end-effector extractor is a 2-layer MLP (1024 $\\to$ 256 $\\to$ 3).\n\n\\paragraph{Training schedule.}\nTraining proceeds in two phases:\n\\begin{itemize}\n    \\item \\textbf{Phase 1} (steps 0--5000): Backbone and LoRA parameters are frozen. Only the SDF decoder and EE extractor are trained, allowing them to learn meaningful representations before the policy adapts.\n    \\item \\textbf{Phase 2} (steps 5000--30000): LoRA parameters are unfrozen with a 100-step gradient warmup ramp. All auxiliary heads continue training jointly with the policy.\n\\end{itemize}\n\n\\paragraph{Hyperparameters.}\n\\begin{table}[h]\n\\centering\n\\caption{Training hyperparameters.}\n\\label{tab:hyperparams}\n\\begin{tabular}{ll}\n\\toprule\nParameter & Value \\\\\n\\midrule\nBase model & Pi0.5 (OpenPi, $\\sim$3.5B parameters) \\\\\nOptimizer & AdamW \\\\\nLearning rate & $2.5 \\times 10^{-5}$ (cosine decay to $\\mathrm{lr}/10$) \\\\\nWarmup steps & 1000 \\\\\nBatch size & 32 \\\\\nTotal steps & 30000 \\\\\n$\\lambda_\\mathrm{sdf}$ & \\{0.005, 0.01, 0.1\\} \\\\\n$\\lambda_\\mathrm{ee}$ & 0.01 \\\\\nSDF query points per step & 64 \\\\\nSDF clamp $\\delta$ & 0.05 m \\\\\nEikonal weight & 0.1 \\\\\nLoRA rank (vision) & 16 \\\\\nLoRA rank (action) & 32 \\\\\nPhase 1 duration & 5000 steps \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Evaluation protocol.}\nEach episode runs for at most 300 timesteps. The policy generates a 50-step action trajectory via flow matching and executes the first 5 steps before replanning. An episode terminates early upon task completion. Collision detection uses MuJoCo's built-in contact detection: any contact between the robot and a non-target object registers as a collision. For Pi0.5 evaluations, camera images are rotated 180$^\\circ$ to match the pre-training viewpoint convention; this correction was verified to restore TSR from ${\\sim}$5\\% to ${\\sim}$52\\% while leaving CAR comparable. Oracle variants use 40 episodes per task (160 total) with a single seed; all other configurations use 50 episodes per task (200 total).\n\n\\paragraph{Data.}\nWe use the SafeLIBERO object\\_pudding suite with pre-computed SDF ground truth. SDF values are computed offline from the obstacle mesh using a dense $64^3$ voxel grid. During training, 64 query points are randomly sampled per step from this grid.\n\n\\paragraph{Computational resources.}\nAll training and evaluation experiments are conducted on NVIDIA RTX PRO 6000 GPUs (96\\,GB). Phase~1 (5K steps) takes approximately 6 hours on a single GPU; Phase~2 (25K steps) takes approximately 32 hours. Evaluation of 200 episodes requires approximately 4 hours. Across 100+ experiments (training runs, evaluations, oracle variants, and ablations), the total computational budget is approximately 700 GPU-hours.\n",
    "structuredPatch": [
      {
        "oldStart": 226,
        "oldLines": 7,
        "newStart": 226,
        "newLines": 7,
        "lines": [
          " \\section{Cross-Scene Validation: spatial\\_bowl}",
          " \\label{sec:appendix_spatial_bowl}",
          " ",
          "-To test whether the SDF redundancy finding generalizes beyond the primary \\texttt{object\\_pudding} scene, we replicate the core comparison on \\texttt{spatial\\_bowl}, a separate SafeLIBERO suite with a distinct obstacle layout (moka pot, wine bottle, milk carton, red coffee mug, yellow book). Both conditions use the same architecture, hyperparameters, and two-phase training schedule (30K steps), differing only in the training scene.",
          "+To test whether the absence of EE-only SDF benefit generalizes beyond the primary \\texttt{object\\_pudding} scene, we replicate the core comparison on \\texttt{spatial\\_bowl}, a separate SafeLIBERO suite with a distinct obstacle layout (moka pot, wine bottle, milk carton, red coffee mug, yellow book). Both conditions use the same architecture, hyperparameters, and two-phase training schedule (30K steps), differing only in the training scene.",
          " ",
          " Table~\\ref{tab:spatial_bowl} reports the results. The SDF condition ($\\lambda = 0.005$) yields CAR of 11.5\\% versus 12.0\\% for LoRA-only, a $-$0.5\\,pp difference well within the noise floor, indicating that SDF is essentially identical to LoRA-only on this scene. TSR is comparable across conditions (49.0\\% vs.\\ 51.5\\%). Both evaluations use a single training seed (seed~0) and a single evaluation seed (seed~7, 200 episodes), so statistical power is limited; nevertheless, the qualitative pattern---SDF failing to improve over LoRA-only---is consistent with the \\texttt{object\\_pudding} findings.",
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

### Tool call

_source line 76_

<details open><summary>🔧 Tool call — Edit · `toolu_01EeyLEZVngaLG1aHGFyXrng`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex",
  "old_string": "consistent with the SDF redundancy observed on \\texttt{object\\_pudding}",
  "new_string": "consistent with the absence of SDF benefit observed on \\texttt{object\\_pudding}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "5830e314-db9b-4d1e-936e-7152b2e29bcd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016yyGBFbqpQDyq3iRdN71nw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3310,
      "cache_read_input_tokens": 51416,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3310
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

_source line 77 · 2026-05-28T06:52:37.860Z_

<details><summary>↩ Tool result · `toolu_01EeyLEZVngaLG1aHGFyXrng`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "bb33de4e-4e71-464e-9f75-7f96aae9c698",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex",
    "oldString": "consistent with the SDF redundancy observed on \\texttt{object\\_pudding}",
    "newString": "consistent with the absence of SDF benefit observed on \\texttt{object\\_pudding}",
    "originalFile": "\\section{Displacement Distribution}\n\\label{sec:appendix_displacement}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\linewidth]{fig2_ee_displacement_distribution}\n\\caption{Displacement distribution across evaluation episodes. Pi0-family models (blue) cluster below 1\\,$\\mu$m, while Pi0.5 episodes (orange) exceed 200\\,mm. The five-order-of-magnitude gap makes $\\tau_d$ robust to any value in $[2, 200]$\\,mm.}\n\\label{fig:displacement}\n\\end{figure}\n\n\\section{Displacement Threshold Sensitivity Analysis}\n\\label{sec:appendix_threshold}\n\nTo validate the robustness of our displacement threshold $\\tau_d$, we evaluate the action-collapse rate across four orders of magnitude. Table~\\ref{tab:threshold_sensitivity} shows that the action-collapse pattern persists across all reasonable threshold choices: A1-LoRA exhibits near-total action collapse regardless of threshold, while Pi0.5+A1 maintains 0\\% action-collapse rate even at the most conservative setting.\n\n\\begin{table}[h]\n\\centering\n\\caption{Action-collapse rate (\\% of episodes with $d_\\mathrm{max} < \\tau_d$) across threshold values.}\n\\label{tab:threshold_sensitivity}\n\\begin{tabular}{lccc}\n\\toprule\n$\\tau_d$ & A1-LoRA (Pi0) & Pi0.5 Baseline & Pi0.5+A1 (SDF aux) \\\\\n\\midrule\n0.001 mm (1\\,$\\mu$m) & 73.9 & 0.0 & 0.0 \\\\\n0.1 mm  & 99.6 & 0.0 & 0.0 \\\\\n1.0 mm  & 100.0 & 0.0 & 0.0 \\\\\n10 mm   & 100.0 & 0.0 & 0.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe choice of $\\tau_d = 0.1$\\,mm represents a conservative threshold: displacement below this value is physically negligible in manipulation tasks where typical action magnitudes are 1--10\\,mm per step. Even at $\\tau_d = 1$\\,$\\mu$m, 73.9\\% of A1-LoRA safe episodes are classified as action-collapsed, while all Pi0.5 episodes remain above threshold at every level tested.\n\nTable~\\ref{tab:dfcar_threshold} extends this analysis to dfCAR across fine-tuned Pi0.5 configurations. All eight model-seed combinations yield identical dfCAR for $\\tau_d \\in [2, 200]$\\,mm. At $\\tau_d = 300$\\,mm, 0--2 episodes per seed fall below threshold (displacement 200--300\\,mm), causing $\\leq$0.5\\,pp deviation. Our conclusions hold across the entire tested range.\n\n\\begin{table}[h]\n\\centering\n\\caption{dfCAR (\\%) across displacement thresholds for fine-tuned Pi0.5 configurations ($n = 200$ episodes per seed). Values are identical across $\\tau_d \\in [2, 200]$\\,mm; at $\\tau_d = 300$\\,mm, at most 2 episodes are excluded.}\n\\label{tab:dfcar_threshold}\n\\vspace{2pt}\n\\footnotesize\n\\begin{tabular}{lcccccccc}\n\\toprule\n& \\multicolumn{8}{c}{$\\tau_d$ (mm)} \\\\\n\\cmidrule(lr){2-9}\nCondition & 2 & 5 & 10 & 20 & 50 & 100 & 200 & 300 \\\\\n\\midrule\nLoRA s0            & 56.5 & 56.5 & 56.5 & 56.5 & 56.5 & 56.5 & 56.5 & 56.5 \\\\\nLoRA s1            & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 \\\\\nSDF $\\lambda{=}0.005$ s0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.1 \\\\\nSDF $\\lambda{=}0.005$ s1 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 & 54.0 \\\\\nSDF $\\lambda{=}0.005$ s2 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.5 & 52.3 \\\\\nSDF $\\lambda{=}0.01$ s0  & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 & 57.0 \\\\\nSDF $\\lambda{=}0.01$ s1  & 57.5 & 57.5 & 57.5 & 57.5 & 57.5 & 57.5 & 57.5 & 57.1 \\\\\nSDF $\\lambda{=}0.01$ s2  & 54.5 & 54.5 & 54.5 & 54.5 & 54.5 & 54.5 & 54.5 & 54.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Per-Task TSR Breakdown}\\label{sec:appendix_tsr_pertask}\n\nTable~\\ref{tab:per_task_tsr} decomposes TSR by task for the avoidance source attribution experiments (Section~\\ref{sec:avoidance_source}). All tasks retain meaningful success rates after fine-tuning, with Chocolate Pudding most resilient and Orange Juice most affected.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-task TSR (\\%) at 30K training steps. Baseline reports the unified seed-7 re-evaluation (aggregate TSR\\,=\\,71.5\\%). LoRA-only reports 3-seed means (re-evaluated with unified seed-7 protocol); SDF conditions report 3-seed means.}\n\\label{tab:per_task_tsr}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nTask & Pi0.5 Base & LoRA-only & SDF $\\lambda{=}0.005$ & SDF $\\lambda{=}0.01$ \\\\\n & (seed\\,=\\,7) & (3 seeds) & (3 seeds) & (3 seeds) \\\\\n\\midrule\nOrange Juice      & 74.0 & 30.0 & 33.3 & 24.7 \\\\\nChoco.\\ Pudding   & 80.0 & 70.7 & 78.0 & 76.7 \\\\\nMilk              & 66.0 & 44.7 & 35.3 & 48.7 \\\\\nBBQ Sauce         & 66.0 & 60.7 & 69.3 & 65.3 \\\\\n\\midrule\nMean              & 71.5 & 51.5 & 54.0 & 53.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Per-Task CAR Breakdown}\\label{sec:appendix_pertask_car}\n\nTable~\\ref{tab:per_task_car} decomposes CAR by task for all fine-tuned conditions, supporting the claim that per-task ordering is preserved across SDF loss weights (\\S\\ref{sec:avoidance_source}). Chocolate Pudding is consistently highest and BBQ Sauce consistently lowest across all conditions, including $\\lambda = 0.1$. The intermediate tasks (Orange Juice and Milk) exchange rank between seeds but remain bounded by the extremes. This invariance indicates that avoidance patterns reflect the spatial statistics of collision-free demonstrations rather than geometric supervision.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-task CAR (\\%) at 30K steps. $\\lambda{=}0.005$, $\\lambda{=}0.01$, and $\\lambda{=}0.1$ report 3-seed means alongside individual seeds. Per-task ordering (CP highest, BBQ lowest) is preserved across all conditions.}\n\\label{tab:per_task_car}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nCondition & OJ & CP & Milk & BBQ & Agg. \\\\\n\\midrule\nLoRA s0 & 56 & 74 & 70 & 26 & 56.5 \\\\\nLoRA s1 & 54 & 68 & 72 & 16 & 52.5 \\\\\nLoRA s2 & 56 & 76 & 62 & 26 & 55.0 \\\\\nSDF $\\lambda{=}0.005$ (3-seed) & 54.0 & 72.7 & 71.3 & 20.0 & 54.5 \\\\\nSDF $\\lambda{=}0.01$ (3-seed) & 57.3 & 72.7 & 72.0 & 23.3 & 56.3 \\\\\nSDF $\\lambda{=}0.1$ s0 & 60 & 74 & 68 & 30 & 58.0 \\\\\nSDF $\\lambda{=}0.1$ s1 & 66 & 72 & 70 & 26 & 58.5 \\\\\nSDF $\\lambda{=}0.1$ s2 & 56 & 76 & 70 & 16 & 54.5 \\\\\nSDF $\\lambda{=}0.1$ (3-seed) & 60.7 & 74.0 & 69.3 & 24.0 & 57.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nFor the $\\lambda = 0.1$ condition, seed~1 records \\texttt{avg\\_max\\_obstacle\\_displacement} of 0.0553\\,m (per-task: OJ\\,=\\,0.033, CP\\,=\\,0.055, Milk\\,=\\,0.041, BBQ\\,=\\,0.093), comparable to other fine-tuned conditions and consistent with active manipulation rather than action-collapsed behavior.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\linewidth]{fig_pertask_car_fingerprint}\n\\caption{Per-task CAR fingerprint across conditions. Each bar shows the 3-seed mean; dots indicate individual seeds. The task ordering (chocolate\\_pudding highest, bbq\\_sauce lowest) is preserved across all $\\lambda$ values, confirming that avoidance patterns reflect the demonstration distribution rather than geometric supervision. LoRA-only: 3-seed mean.}\n\\label{fig:pertask_fingerprint}\n\\end{figure}\n\n\\section{Safe Success Rate Analysis}\\label{sec:appendix_ssr}\n\nTable~\\ref{tab:ssr} reports the Safe Success Rate (SSR\\,=\\,TSR\\,$\\cap$\\,CAR), the fraction of episodes achieving both task completion and collision avoidance. The SSR/TSR ratio quantifies the proportion of successful episodes that are also collision-free, controlling for task-completion rate.\n\n\\begin{table}[h]\n\\centering\n\\caption{SSR and SSR/TSR ratio across conditions. The ratio increase from 0.39 (baseline) to 0.51--0.60 (fine-tuned) indicates that CAR gains reflect learned safer execution, not reduced task exposure.}\n\\label{tab:ssr}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nCondition & TSR (\\%) & CAR (\\%) & SSR (\\%) & SSR/TSR \\\\\n\\midrule\nPi0.5 baseline & 71.5 & 28.5 & 28.0 & 0.39 \\\\\nLoRA-only (3 seeds) & 51.5 & 54.67 & 27.7 & 0.54 \\\\\nSDF $\\lambda{=}0.005$ (3 seeds) & 54.0 & 54.5 & 27.8 & 0.51 \\\\\nSDF $\\lambda{=}0.01$ (3 seeds) & 53.8 & 56.33 & 30.2 & 0.56 \\\\\nSDF $\\lambda{=}0.1$ (3 seeds) & 50.2 & 57.00 & 30.2 & 0.60 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Per-Task Oracle Analysis}\n\\label{sec:appendix_pertask}\n\\label{sec:appendix_pertask_oracle}\n\nTable~\\ref{tab:oracle_pertask} shows per-task CAR for oracle refinement. On task~1 (\\texttt{chocolate\\_pudding}), where the EE is the primary collision body and the LoRA baseline achieves only 46.0\\% CAR, Oracle-adaptive improves to 55.0\\% and Oracle-feature to 47.5\\%. On the remaining tasks, all oracle variants degrade: Oracle-adaptive reduces task~0 (\\texttt{orange\\_juice}) from 96.0\\% to 82.5\\% and task~2 (\\texttt{milk}) from 98.0\\% to 77.5\\%. The SDF gradient pushes the EE away from the nearest surface, but the resulting joint-space displacement rotates intermediate arm links into obstacle volumes.\n\nThe feature-space oracle fires on nearly every timestep (241.7 refinements/episode vs.\\ 14.2 for Cartesian variants) but with gradient magnitudes two orders of magnitude smaller (0.004--0.006 vs.\\ 0.18--0.49), and CAR (76.9\\%) shows no advantage despite 17$\\times$ more steps. The A3 learned SDF never triggers refinement (0 steps/episode), as its outputs avoid the activation threshold.\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-task CAR (\\%) for oracle SDF refinement variants. EE-only refinement helps only on task~1 where the EE is the primary collision body; on other tasks it trades one collision site for another.}\n\\label{tab:oracle_pertask}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nMethod & Task 0 & Task 1 & Task 2 & Task 3 & Agg. \\\\\n\\midrule\nLoRA baseline & 96.0 & 46.0 & 98.0 & 88.0 & 82.0 \\\\\n\\midrule\nOracle-adaptive & 82.5 & 55.0 & 77.5 & 85.0 & 75.0 \\\\\nOracle-fixed & 85.0 & 50.0 & 77.5 & 80.0 & 73.1 \\\\\nOracle-feature & 90.0 & 47.5 & 82.5 & 87.5 & 76.9 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Null Distribution for SDF Loss Weight Analysis}\n\\label{sec:appendix_null}\n\nWe construct a null distribution by pooling the three LoRA-only seeds and three $\\lambda = 0.005$ seeds into six per-seed CAR measurements: 56.5\\% (LoRA s0, re-evaluated), 52.5\\% (LoRA s1), 55.0\\% (LoRA s2), 57.0\\% ($\\lambda{=}0.005$ s0), 54.0\\% ($\\lambda{=}0.005$ s1), 52.5\\% ($\\lambda{=}0.005$ s2), yielding mean 54.58\\% and standard deviation 1.93\\% (Bessel-corrected, $n{-}1 = 5$). We treat these as exchangeable because SDF at $\\lambda = 0.005$ produces no separation from LoRA-only. The $\\lambda = 0.01$ mean of 56.33\\% falls within $0.8\\sigma$ of this null ($p > 0.1$), consistent with seed-to-seed variation rather than a treatment effect. The $\\lambda = 0.1$ 30K mean of 57.00\\% (3 seeds: 58.0\\%, 58.5\\%, 54.5\\%) yields a two-tailed permutation $p = 0.131$ (one-tailed $p = 0.071$). The result is non-significant at conventional thresholds ($\\alpha = 0.05$).\n\nThe permutation test makes no distributional assumptions. Pooling the six null values $\\{56.5, 52.5, 55, 57, 54, 52.5\\}$ and three $\\lambda = 0.1$ values $\\{58, 58.5, 54.5\\}$ into nine measurements, we enumerate all $\\binom{9}{3} = 84$ three-element combinations and compute the fraction whose mean $\\geq 57.00$. Six combinations meet this threshold, yielding an exact one-tailed permutation $p = 6/84 \\approx 0.071$. For the two-tailed test, we additionally count combinations on the lower tail with equal or greater distance from the pooled mean, yielding $p = 11/84 \\approx 0.131$. With the third seed ($s_2 = 54.5\\%$) pulling the $\\lambda = 0.1$ mean from 58.25\\% (2 seeds) down to 57.00\\%, the marginal signal observed at $n = 2$ dissolves into seed-to-seed variance.\n\n\\paragraph{Alternative null construction (Null~A).}\nIf only the three LoRA-only seeds are used as the null pool ($\\{56.5, 52.5, 55.0\\}$), we obtain $\\binom{6}{3} = 20$ permutations for each comparison. For $\\lambda = 0.1$ (treatment mean 57.00\\%): one-tailed $p = 3/20 = 0.150$, two-tailed $p = 6/20 = 0.300$. For $\\lambda = 0.01$ (treatment mean 56.33\\%): one-tailed $p = 4/20 = 0.200$, two-tailed $p = 8/20 = 0.400$. Under the broader Null~B pool, $\\lambda = 0.01$ yields one-tailed $p = 10/84 \\approx 0.119$, two-tailed $p = 22/84 \\approx 0.262$. All tests are non-significant at $\\alpha = 0.05$; the narrower Null~A yields \\emph{larger} $p$-values because the LoRA-only pool already contains a high seed (56.5\\%), making the treatment means less extreme by comparison.\n\nA Phase~2 ablation reinforces this conclusion. Setting $\\lambda = 0$ during Phase~2 (steps 5K--18K), so that SDF supervision is active only during auxiliary head warmup (Phase~1, steps 0--5K), yields CAR of 58.0\\% at the 18K checkpoint (13K steps of Phase~2 training, single seed, s2).\\footnote{Full 30K training did not complete due to disk constraints; this result uses the last complete checkpoint at step 18K.} This value lies within the null range, indicating that SDF training produces no lasting behavioral effect on collision avoidance.\n\n\\section{Step-wise Checkpoint Analysis for \\texorpdfstring{$\\lambda = 0.1$}{lambda = 0.1}}\n\\label{sec:appendix_stepwise}\n\nTable~\\ref{tab:stepwise_lambda01} reports per-seed CAR at seven checkpoints for $\\lambda = 0.1$. Seeds~0 and~1 are available at 16K, 20K, 22K, and 30K; 24K--28K report seed-0 only; seed~2 is available at 30K only. The seed-0 curve shows no monotonic trend through 28K. At 30K, the addition of seed~2 (54.5\\%) pulls the three-seed mean to 57.00\\%, within the null band ($p = 0.131$).\n\n\\begin{table}[h]\n\\centering\n\\caption{Per-seed CAR (\\%) at training checkpoints for $\\lambda = 0.1$ (200 episodes each). 24K--28K: seed-0 only. The 30K checkpoint includes all three seeds; the three-seed mean (57.00\\%) remains within the null band ($p = 0.131$, two-tailed permutation).}\n\\label{tab:stepwise_lambda01}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nCheckpoint & Seed 0 & Seed 1 & Seed 2 & Mean \\\\\n\\midrule\n16K steps & 55.5 & 56.0 & -- & 55.75 \\\\\n20K steps & 55.0 & 56.0 & -- & 55.5 \\\\\n22K steps & 60.5 & 56.5 & -- & 58.5 \\\\\n24K steps & 52.5 & -- & -- & -- \\\\\n26K steps & 53.5 & -- & -- & -- \\\\\n28K steps & 54.5 & -- & -- & -- \\\\\n30K steps & 58.0 & 58.5 & 54.5 & 57.00 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nIndividual seeds exhibit checkpoint-to-checkpoint CAR fluctuations of up to 8\\,pp (seed~0: 52.5--60.5\\%), larger than the cross-seed standard deviation at any fixed checkpoint ($\\leq$3\\,pp). This is consistent with binomial sampling noise at $n = 50$ episodes per task ($\\sigma \\approx 7$\\,pp per task for $p \\approx 0.5$). At 30K, the third seed ($s_2 = 54.5\\%$) falls well within the null range, pulling the three-seed mean to 57.00\\% and rendering the earlier two-seed departure non-significant ($p = 0.131$). The seed-averaged curve shows no monotonic trend, confirming that SDF loss weight does not produce a progressive training signal.\n\n\n\\section{Oracle SDF Refinement Details}\n\\label{sec:appendix_oracle}\n\nAll oracle variants replace the learned SDF decoder with ground-truth distance fields computed from the simulation geometry. Each is evaluated for 160 episodes (4 tasks $\\times$ 40).\n\n\\paragraph{Oracle-adaptive.} At each timestep, if the ground-truth SDF at the end-effector position falls below a safety margin, the action is adjusted by a step in the negative SDF gradient direction. The step size $\\alpha$ is scaled inversely with distance: smaller distances produce larger corrections. This mimics an adaptive potential field controller.\n\n\\paragraph{Oracle-fixed.} Identical to Oracle-adaptive except the step size is fixed at $\\alpha = 0.005$ regardless of distance. This isolates the effect of step-size adaptation from the refinement geometry.\n\n\\paragraph{Oracle-feature.} Instead of modifying the action directly in Cartesian space, this variant applies the SDF gradient in the policy's latent feature space via backpropagation. The gradient of the ground-truth SDF value with respect to the intermediate features is computed and used to perturb the features before the action head decodes them. This tests whether geometric corrections are more effective when applied in the model's learned representation space. In practice, the feature-space variant fires on nearly every timestep (241.7 refinements per episode vs.\\ 14.2 for Cartesian variants) but with gradient magnitudes two orders of magnitude smaller (0.004--0.006 vs.\\ 0.18--0.49 in action space).\n\n\n\\section{Cross-Scene Validation: spatial\\_bowl}\n\\label{sec:appendix_spatial_bowl}\n\nTo test whether the absence of EE-only SDF benefit generalizes beyond the primary \\texttt{object\\_pudding} scene, we replicate the core comparison on \\texttt{spatial\\_bowl}, a separate SafeLIBERO suite with a distinct obstacle layout (moka pot, wine bottle, milk carton, red coffee mug, yellow book). Both conditions use the same architecture, hyperparameters, and two-phase training schedule (30K steps), differing only in the training scene.\n\nTable~\\ref{tab:spatial_bowl} reports the results. The SDF condition ($\\lambda = 0.005$) yields CAR of 11.5\\% versus 12.0\\% for LoRA-only, a $-$0.5\\,pp difference well within the noise floor, indicating that SDF is essentially identical to LoRA-only on this scene. TSR is comparable across conditions (49.0\\% vs.\\ 51.5\\%). Both evaluations use a single training seed (seed~0) and a single evaluation seed (seed~7, 200 episodes), so statistical power is limited; nevertheless, the qualitative pattern---SDF failing to improve over LoRA-only---is consistent with the \\texttt{object\\_pudding} findings.\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-scene validation on \\texttt{spatial\\_bowl} (single training seed, 200 episodes, 30K checkpoint). The $-$0.5\\,pp CAR difference is well within noise, consistent with the SDF redundancy observed on \\texttt{object\\_pudding}.}\n\\label{tab:spatial_bowl}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nCondition & CAR (\\%) & TSR (\\%) \\\\\n\\midrule\nLoRA-only & 12.0 & 49.0 \\\\\nSDF $\\lambda{=}0.005$ & 11.5 & 51.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe substantially lower CAR on \\texttt{spatial\\_bowl} relative to \\texttt{object\\_pudding} (11--12\\% vs.\\ 54--57\\%) reflects the greater scene difficulty: \\texttt{spatial\\_bowl} places five cluttered obstacles around the workspace, making collision-free manipulation considerably harder. This difficulty affects both conditions equally, and the SDF condition performs comparably ($\\Delta$CAR\\,=\\,$-$0.5\\,pp, well within noise), reinforcing the conclusion that EE-only SDF auxiliary supervision does not produce a meaningful collision avoidance benefit beyond LoRA-only fine-tuning.\n\n\n\\section{Evaluation Seed Robustness}\n\\label{sec:appendix_eval_seed}\n\nTo verify that our conclusions are not artifacts of a particular evaluation seed, we re-evaluate the LoRA-only (s0) and SDF $\\lambda{=}0.1$ (s0) checkpoints under multiple evaluation seeds. Table~\\ref{tab:eval_seed_car} reports aggregate CAR and Table~\\ref{tab:eval_seed_tsr} reports aggregate TSR.\n\n\\begin{table}[h]\n\\centering\n\\caption{Aggregate CAR (\\%) across evaluation seeds (200 episodes each). The LoRA vs.\\ SDF $\\lambda{=}0.1$ ordering is preserved across all tested seeds, and per-task CAR fingerprints (CP highest, BBQ lowest) remain invariant.}\n\\label{tab:eval_seed_car}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\n& \\multicolumn{4}{c}{Per-task CAR (\\%)} & & \\\\\n\\cmidrule(lr){2-5}\nCondition (eval seed) & OJ & CP & Milk & BBQ & Agg. \\\\\n\\midrule\nLoRA s0 (seed\\,=\\,7)   & 56 & 74 & 70 & 26 & 56.5 \\\\\nLoRA s0 (seed\\,=\\,42)  & 60 & 70 & 68 & 28 & 56.5 \\\\\nLoRA s0 (seed\\,=\\,123) & 52 & 74 & 66 & 20 & 53.0 \\\\\nLoRA s0 mean $\\pm$ std & 56.0$\\pm$4.0 & 72.7$\\pm$2.3 & 68.0$\\pm$2.0 & 24.7$\\pm$4.2 & 55.3$\\pm$2.0 \\\\\n\\midrule\nSDF $\\lambda{=}0.1$ s0 (seed\\,=\\,7)   & 60 & 74 & 68 & 30 & 58.0 \\\\\nSDF $\\lambda{=}0.1$ s0 (seed\\,=\\,42)  & 64 & 74 & 74 & 24 & 59.0 \\\\\nSDF $\\lambda{=}0.1$ s0 (seed\\,=\\,123) & 62 & 76 & 74 & 22 & 58.5 \\\\\nSDF $\\lambda{=}0.1$ s0 (seed\\,=\\,256) & 60 & 72 & 66 & 30 & 57.0 \\\\\nSDF $\\lambda{=}0.1$ s0 mean $\\pm$ std & 61.5$\\pm$1.9 & 74.0$\\pm$1.6 & 70.5$\\pm$4.1 & 26.5$\\pm$4.1 & 58.1$\\pm$0.9 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\caption{Aggregate TSR (\\%) across evaluation seeds. TSR varies more across seeds than CAR (seed\\,=\\,42 yields consistently lower TSR), but the relative ordering between LoRA and SDF is stable.}\n\\label{tab:eval_seed_tsr}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{lcccccc}\n\\toprule\n& \\multicolumn{4}{c}{Per-task TSR (\\%)} & & \\\\\n\\cmidrule(lr){2-5}\nCondition (eval seed) & OJ & CP & Milk & BBQ & Agg. \\\\\n\\midrule\nLoRA s0 (seed\\,=\\,7)   & 32 & 74 & 42 & 58 & 51.5 \\\\\nLoRA s0 (seed\\,=\\,42)  & 22 & 70 & 32 & 60 & 46.0 \\\\\nLoRA s0 (seed\\,=\\,123) & 30 & 70 & 40 & 62 & 50.5 \\\\\nLoRA s0 mean $\\pm$ std & 28.0$\\pm$5.3 & 71.3$\\pm$2.3 & 38.0$\\pm$5.3 & 60.0$\\pm$2.0 & 49.3$\\pm$3.0 \\\\\n\\midrule\nSDF $\\lambda{=}0.1$ s0 (seed\\,=\\,7)   & 28 & 78 & 44 & 60 & 52.5 \\\\\nSDF $\\lambda{=}0.1$ s0 (seed\\,=\\,42)  & 18 & 78 & 42 & 72 & 52.5 \\\\\nSDF $\\lambda{=}0.1$ s0 (seed\\,=\\,123) & 26 & 82 & 38 & 68 & 53.5 \\\\\nSDF $\\lambda{=}0.1$ s0 (seed\\,=\\,256) & 28 & 74 & 32 & 58 & 48.0 \\\\\nSDF $\\lambda{=}0.1$ s0 mean $\\pm$ std & 25.0$\\pm$4.8 & 78.0$\\pm$3.3 & 39.0$\\pm$5.4 & 64.5$\\pm$6.6 & 51.6$\\pm$2.4 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAcross three matched evaluation seeds (7, 42, 123), the SDF $\\lambda{=}0.1$ condition yields higher aggregate CAR than LoRA-only in all cases ($\\Delta$CAR\\,=\\,+1.5, +2.5, +5.5\\,pp). Cross-seed CAR standard deviation is 2.0\\,pp for LoRA and 0.9\\,pp for SDF, both small relative to the within-seed per-task variation. The per-task ordering (CP highest, BBQ lowest) is preserved across all seeds and both conditions, reinforcing the conclusion that avoidance patterns reflect the spatial statistics of training demonstrations.\n\n\n\\section{Training Details}\n\\label{sec:appendix_training}\n\n\\paragraph{Architecture.}\nWe use LoRA~\\citep{hu2022lora} adapters injected into the PaliGemma vision encoder (rank 16, $\\alpha$=16) and the action expert (rank 32, $\\alpha$=32), following the configuration of OpenPi. The SDF decoder is a 4-layer MLP (hidden dimension 256) with skip connections, taking pooled suffix features (1024-d) and query points (3-d) as input. The end-effector extractor is a 2-layer MLP (1024 $\\to$ 256 $\\to$ 3).\n\n\\paragraph{Training schedule.}\nTraining proceeds in two phases:\n\\begin{itemize}\n    \\item \\textbf{Phase 1} (steps 0--5000): Backbone and LoRA parameters are frozen. Only the SDF decoder and EE extractor are trained, allowing them to learn meaningful representations before the policy adapts.\n    \\item \\textbf{Phase 2} (steps 5000--30000): LoRA parameters are unfrozen with a 100-step gradient warmup ramp. All auxiliary heads continue training jointly with the policy.\n\\end{itemize}\n\n\\paragraph{Hyperparameters.}\n\\begin{table}[h]\n\\centering\n\\caption{Training hyperparameters.}\n\\label{tab:hyperparams}\n\\begin{tabular}{ll}\n\\toprule\nParameter & Value \\\\\n\\midrule\nBase model & Pi0.5 (OpenPi, $\\sim$3.5B parameters) \\\\\nOptimizer & AdamW \\\\\nLearning rate & $2.5 \\times 10^{-5}$ (cosine decay to $\\mathrm{lr}/10$) \\\\\nWarmup steps & 1000 \\\\\nBatch size & 32 \\\\\nTotal steps & 30000 \\\\\n$\\lambda_\\mathrm{sdf}$ & \\{0.005, 0.01, 0.1\\} \\\\\n$\\lambda_\\mathrm{ee}$ & 0.01 \\\\\nSDF query points per step & 64 \\\\\nSDF clamp $\\delta$ & 0.05 m \\\\\nEikonal weight & 0.1 \\\\\nLoRA rank (vision) & 16 \\\\\nLoRA rank (action) & 32 \\\\\nPhase 1 duration & 5000 steps \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Evaluation protocol.}\nEach episode runs for at most 300 timesteps. The policy generates a 50-step action trajectory via flow matching and executes the first 5 steps before replanning. An episode terminates early upon task completion. Collision detection uses MuJoCo's built-in contact detection: any contact between the robot and a non-target object registers as a collision. For Pi0.5 evaluations, camera images are rotated 180$^\\circ$ to match the pre-training viewpoint convention; this correction was verified to restore TSR from ${\\sim}$5\\% to ${\\sim}$52\\% while leaving CAR comparable. Oracle variants use 40 episodes per task (160 total) with a single seed; all other configurations use 50 episodes per task (200 total).\n\n\\paragraph{Data.}\nWe use the SafeLIBERO object\\_pudding suite with pre-computed SDF ground truth. SDF values are computed offline from the obstacle mesh using a dense $64^3$ voxel grid. During training, 64 query points are randomly sampled per step from this grid.\n\n\\paragraph{Computational resources.}\nAll training and evaluation experiments are conducted on NVIDIA RTX PRO 6000 GPUs (96\\,GB). Phase~1 (5K steps) takes approximately 6 hours on a single GPU; Phase~2 (25K steps) takes approximately 32 hours. Evaluation of 200 episodes requires approximately 4 hours. Across 100+ experiments (training runs, evaluations, oracle variants, and ablations), the total computational budget is approximately 700 GPU-hours.\n",
    "structuredPatch": [
      {
        "oldStart": 232,
        "oldLines": 7,
        "newStart": 232,
        "newLines": 7,
        "lines": [
          " ",
          " \\begin{table}[h]",
          " \\centering",
          "-\\caption{Cross-scene validation on \\texttt{spatial\\_bowl} (single training seed, 200 episodes, 30K checkpoint). The $-$0.5\\,pp CAR difference is well within noise, consistent with the SDF redundancy observed on \\texttt{object\\_pudding}.}",
          "+\\caption{Cross-scene validation on \\texttt{spatial\\_bowl} (single training seed, 200 episodes, 30K checkpoint). The $-$0.5\\,pp CAR difference is well within noise, consistent with the absence of SDF benefit observed on \\texttt{object\\_pudding}.}",
          " \\label{tab:spatial_bowl}",
          " \\vspace{2pt}",
          " \\small"
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

_source line 78_

P1 #3 done. Now **P1 #4** — discussion.tex 首句 scope:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "917662d6-fb13-4736-800f-afd240332011",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ft24ULnZBdCemg3Z2MLKUw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 968,
      "cache_read_input_tokens": 54726,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 968
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

_source line 79_

<details open><summary>🔧 Tool call — Edit · `toolu_015B25BJaRh9PgW1BkKZ1e1J`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex",
  "old_string": "three findings converge: current VLA safety evaluation is structurally unreliable.",
  "new_string": "three findings converge: CAR-based VLA safety evaluation, as currently practiced on SafeLIBERO, is structurally unreliable."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "33b53ef2-494d-474c-b279-5554c2b0788f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ft24ULnZBdCemg3Z2MLKUw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 968,
      "cache_read_input_tokens": 54726,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 968
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

_source line 80 · 2026-05-28T06:52:41.915Z_

<details><summary>↩ Tool result · `toolu_015B25BJaRh9PgW1BkKZ1e1J`</summary>

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
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "47ffff66-ccbc-409a-b216-d8f948498e8f",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex",
    "oldString": "three findings converge: current VLA safety evaluation is structurally unreliable.",
    "newString": "three findings converge: CAR-based VLA safety evaluation, as currently practiced on SafeLIBERO, is structurally unreliable.",
    "originalFile": "\\section{Discussion and Conclusion}\\label{sec:conclusion}\n\nAcross 100+ experiments and 6000+ evaluation episodes on two VLA model families, three findings converge: current VLA safety evaluation is structurally unreliable. Action collapse renders reported CAR illusory (\\S\\ref{sec:dfcar}); EE-only oracle refinement is counterproductive (\\S\\ref{sec:ee_only}); and collision-free demonstrations account for nearly all measured avoidance gains, with EE-only SDF contributing no statistically significant improvement (\\S\\ref{sec:avoidance_source}).\n\n\\paragraph{Why EE-only SDF fails.}\nTwo independent causes explain the null result. \\textit{(i)~Demonstration data largely subsumes the SDF signal.} Collision-free demonstrations implicitly encode spatial avoidance; the ${\\sim}$26\\,pp CAR gain arises primarily from this distributional shift, with per-task ordering invariant across all SDF conditions (\\S\\ref{sec:avoidance_source}). Even at $\\lambda = 0.1$ (20$\\times$ the lowest tested weight), CAR remains within the null distribution ($p = 0.131$), suggesting that EE-only auxiliary SDF loss does not overcome Level~A signal masking---the limitation is architectural for this integration pathway. \\textit{(ii)~EE monitoring cannot prevent full-body collisions.} The SDF gradient acts on a single point while collisions occur along intermediate links. Oracle experiments confirm this: ground-truth SDF refinement \\emph{reduces} CAR by 6--10\\,pp below unrefined baselines (\\S\\ref{sec:ee_only}), because pushing the EE away rotates unmonitored links through obstacles. We hypothesize that collision-free demonstration trajectories implicitly encode workspace priors through their spatial distribution: the robot learns to favor regions of the workspace that are inherently collision-free, without requiring explicit geometric supervision. These two causes are independent; effective geometric safety requires both full-body supervision and training signals beyond demonstrations. The failure of EE-only auxiliary SDF loss is architectural. Constrained-optimization approaches (e.g., SafeVLA) address collision avoidance through a fundamentally different optimization paradigm---directly constraining violation probability rather than adding geometric supervision---while runtime filtering sidesteps training altogether.\n\n\\paragraph{Implications for evaluation.}\ndfCAR corrects action-collapse contamination using only EE position logging, already available in most evaluation pipelines. The bimodal displacement distribution makes $\\tau_d$ robust across five orders of magnitude. We recommend reporting both CAR and dfCAR; the gap quantifies contamination. This contamination spans a 4000$\\times$ parameter range (Pi0 Full-FT ${\\sim}$2.5B to Pi0+A1 ${\\sim}$658K trainable), a structural consequence of evaluating avoidance without verifying motion. More broadly, safety may need to operate at the planning or joint-space constraint layer, since any EE-centric loss inherits the same blind spot.\n\n\\paragraph{Scope and generalizability.} Our findings are drawn from a single benchmark (SafeLIBERO) covering two VLA model families and four pick-and-place manipulation tasks in MuJoCo simulation. The action-collapse mechanism (Claim~1) is structurally general---any policy prone to action collapse will inflate CAR under standard evaluation---but its prevalence across other benchmarks, task types, and real hardware remains an open question. The finding that EE-only SDF shows no significant benefit (Claim~3) is specific to EE-only auxiliary loss integration and should not be extrapolated to alternative SDF integration pathways (Section~\\ref{sec:related}).\n\n\\paragraph{Limitations.}\nAll experiments are conducted in MuJoCo simulation within the SafeLIBERO benchmark. The sim-to-real gap introduces uncertainty: collision detection precision differs between simulation and physical hardware, sensor noise may affect displacement-filtered CAR differently on real robots, and the prevalence of action collapse in physical deployments remains untested. Our evaluation covers only four pick-and-place manipulation tasks with tabletop obstacles; whether the findings generalize to more diverse task families (e.g., bi-manual manipulation, deformable objects, dynamic obstacles) is an open question. Statistical power is limited by $n{=}3$ training seeds per condition, yielding a minimum detectable effect of approximately 5 percentage points at 80\\% power---smaller genuine effects, if they exist, would not be detected at this sample size. Oracle experiments used a largely action-collapsed model (Pi0+A1, TSR${\\approx}$0\\%); testing on an actively moving policy would better isolate the structural limitation. Full-body SDF remains untested. Fine-tuning degrades TSR by ${\\sim}$18--20\\,pp, yet SSR/TSR increases from 0.39 to 0.51--0.60 (Appendix~\\ref{sec:appendix_ssr}); reduced exposure alone does not explain the pattern.\n\n\\paragraph{Future work.}\nThree directions follow: (1) full-body SDF supervision along the kinematic chain; (2) cross-architecture evaluation on OpenVLA, RT-2, and other VLA families; (3) planning-layer safety constraints in joint space rather than EE space.\n\n\\paragraph{Broader impact.}\nThe displacement-filtered CAR metric (dfCAR) is intended as a diagnostic complement to standard CAR, not a replacement; practitioners should report both metrics to distinguish genuine avoidance from action-collapse artifacts. Our finding that EE-only SDF supervision is redundant at the tested scale with demonstration data is an evaluation-methodology insight, not a verdict against safety-aware training---geometric supervision may prove effective through alternative integration pathways or with full-body collision surfaces. We caution against interpreting these results as evidence that VLA safety research is futile; rather, they highlight the need for evaluation protocols that can reliably separate safety improvements from measurement artifacts.\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 6,
        "newStart": 1,
        "newLines": 6,
        "lines": [
          " \\section{Discussion and Conclusion}\\label{sec:conclusion}",
          " ",
          "-Across 100+ experiments and 6000+ evaluation episodes on two VLA model families, three findings converge: current VLA safety evaluation is structurally unreliable. Action collapse renders reported CAR illusory (\\S\\ref{sec:dfcar}); EE-only oracle refinement is counterproductive (\\S\\ref{sec:ee_only}); and collision-free demonstrations account for nearly all measured avoidance gains, with EE-only SDF contributing no statistically significant improvement (\\S\\ref{sec:avoidance_source}).",
          "+Across 100+ experiments and 6000+ evaluation episodes on two VLA model families, three findings converge: CAR-based VLA safety evaluation, as currently practiced on SafeLIBERO, is structurally unreliable. Action collapse renders reported CAR illusory (\\S\\ref{sec:dfcar}); EE-only oracle refinement is counterproductive (\\S\\ref{sec:ee_only}); and collision-free demonstrations account for nearly all measured avoidance gains, with EE-only SDF contributing no statistically significant improvement (\\S\\ref{sec:avoidance_source}).",
          " ",
          " \\paragraph{Why EE-only SDF fails.}",
          " Two independent causes explain the null result. \\textit{(i)~Demonstration data largely subsumes the SDF signal.} Collision-free demonstrations implicitly encode spatial avoidance; the ${\\sim}$26\\,pp CAR gain arises primarily from this distributional shift, with per-task ordering invariant across all SDF conditions (\\S\\ref{sec:avoidance_source}). Even at $\\lambda = 0.1$ (20$\\times$ the lowest tested weight), CAR remains within the null distribution ($p = 0.131$), suggesting that EE-only auxiliary SDF loss does not overcome Level~A signal masking---the limitation is architectural for this integration pathway. \\textit{(ii)~EE monitoring cannot prevent full-body collisions.} The SDF gradient acts on a single point while collisions occur along intermediate links. Oracle experiments confirm this: ground-truth SDF refinement \\emph{reduces} CAR by 6--10\\,pp below unrefined baselines (\\S\\ref{sec:ee_only}), because pushing the EE away rotates unmonitored links through obstacles. We hypothesize that collision-free demonstration trajectories implicitly encode workspace priors through their spatial distribution: the robot learns to favor regions of the workspace that are inherently collision-free, without requiring explicit geometric supervision. These two causes are independent; effective geometric safety requires both full-body supervision and training signals beyond demonstrations. The failure of EE-only auxiliary SDF loss is architectural. Constrained-optimization approaches (e.g., SafeVLA) address collision avoidance through a fundamentally different optimization paradigm---directly constraining violation probability rather than adding geometric supervision---while runtime filtering sidesteps training altogether."
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

_source line 81_

P1 #4 done. Now **P1 #10a/b** — add HazardArena and VLA-Risk citations. First add to related_work.tex evaluation paragraph, then to references.bib.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "fb7206ac-05a7-48a4-99ea-4bc96767fc34",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FfxbmFpNzh7gPT2wCgT3Y8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 273,
      "cache_read_input_tokens": 55694,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 273
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

_source line 82_

<details open><summary>🔧 Tool call — Edit · `toolu_01HTMBk8PBThanX9Yr2tp5gj`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/related_work.tex",
  "old_string": "Action collapse in diffusion policies~\\cite{dong2025conditioning} systematically inflates CAR but has not been previously examined as a safety evaluation confounder. We propose dfCAR (\\S\\ref{sec:dfcar}) to detect this contamination.",
  "new_string": "Action collapse in diffusion policies~\\cite{dong2025conditioning} systematically inflates CAR but has not been previously examined as a safety evaluation confounder. Concurrent work expands the evaluation landscape: HazardArena~\\cite{chen2026hazardarena} evaluates semantic safety through safe/unsafe twin scenarios, and VLA-Risk~\\cite{vlariskanon2026} benchmarks physical robustness across object, action, and spatial perturbation dimensions. We propose dfCAR (\\S\\ref{sec:dfcar}) to detect this contamination."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "d90570b3-5f35-4b2a-be33-ec008d462820",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FfxbmFpNzh7gPT2wCgT3Y8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 273,
      "cache_read_input_tokens": 55694,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 273
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

_source line 83 · 2026-05-28T06:52:50.582Z_

<details><summary>↩ Tool result · `toolu_01HTMBk8PBThanX9Yr2tp5gj`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/related_work.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "cf99e9bc-7162-426d-a509-cec45b9353f8",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/related_work.tex",
    "oldString": "Action collapse in diffusion policies~\\cite{dong2025conditioning} systematically inflates CAR but has not been previously examined as a safety evaluation confounder. We propose dfCAR (\\S\\ref{sec:dfcar}) to detect this contamination.",
    "newString": "Action collapse in diffusion policies~\\cite{dong2025conditioning} systematically inflates CAR but has not been previously examined as a safety evaluation confounder. Concurrent work expands the evaluation landscape: HazardArena~\\cite{chen2026hazardarena} evaluates semantic safety through safe/unsafe twin scenarios, and VLA-Risk~\\cite{vlariskanon2026} benchmarks physical robustness across object, action, and spatial perturbation dimensions. We propose dfCAR (\\S\\ref{sec:dfcar}) to detect this contamination.",
    "originalFile": "\\section{Related Work}\\label{sec:related}\n\n\\paragraph{Vision-Language-Action Models.}\nVLA models combine pretrained vision-language backbones with action prediction for generalist manipulation~\\cite{brohan2023rt2,black2024pi0,chi2023diffusionpolicy,kim2024openvla}. Recent work enhances spatial reasoning through auxiliary 3D supervision~\\cite{li2025spatialforcing,li2025qdepth,depthvla2025}, but safety considerations remain largely absent: most VLAs train on collision-free demonstrations and evaluate task success alone, with no mechanism to distinguish genuine avoidance from incidental collision-free trajectories.\n\n\\paragraph{Safety in Robot Learning.}\nSafety-aware approaches span training-time constrained RL~\\cite{zhang2025safevla} and test-time filters: control barrier functions~\\cite{hu2025vlsa}, collision risk gating~\\cite{cofreeevla2026}, inverse kinematics QP~\\cite{spalter2024ikinqp}, and diffusion-process collision costs~\\cite{li2024langguided,yang2025cape}. SafeDiffuser~\\cite{xiao2025safediffuser} integrates control barrier functions directly into diffusion denoising to enforce safety invariance during planning; like other test-time shields, it does not learn intrinsic collision awareness within the policy. A recent survey~\\cite{li2026vlasafety} categorizes these into runtime shields, constrained optimization, and representation-based methods. Common to all is that safety is imposed externally rather than learned within the policy's representations. This work tests whether auxiliary SDF supervision can produce intrinsic collision awareness.\n\n\\paragraph{Signed Distance Functions in Robotics.}\nSDFs encode minimum surface distance, where the sign indicates free space or penetration. Neural SDFs~\\cite{park2019deepsdf} enable continuous shape representation; in robotics, SDFs serve perception~\\cite{ortiz2022isdf}, planning~\\cite{huang2023voxposer,vasilopoulos2023ramp}, and differentiable collision detection~\\cite{zhi2021diffco}. CDF~\\cite{li2024cdf} extends SDFs to robot configuration space, learning neural distance fields that provide efficient joint-angle queries with analytical gradients for manipulation planning; CSSDF-Net~\\cite{chen2026cssdfnet} further develops this direction for safe motion planning. RDF~\\cite{li2024rdf} represents robot geometry itself as composable per-link SDFs along the kinematic chain, enabling whole-body collision queries---directly relevant to the full-body awareness gap our work identifies. Neural SDF-based model predictive control~\\cite{jacquet2025neuralnmpc} demonstrates effectiveness in classical pipelines, but integration into end-to-end learned policies remains unexplored.\n\n\\paragraph{SDF integration pathways.} Geometric supervision via signed distance fields can be integrated into VLA policies through fundamentally different mechanisms. (a)~\\emph{Training-time auxiliary loss}: an SDF-based collision penalty is added to the training objective, supervising only the end-effector trajectory (the approach tested in this work). (b)~\\emph{Constrained optimization}: SafeVLA~\\citep{zhang2025safevla} formulates collision avoidance as a constrained MDP, embedding safety constraints into the training objective via Lagrangian optimization rather than adding SDF as an auxiliary loss. (c)~\\emph{Runtime filtering}: VLSA~\\citep{hu2025vlsa} applies control barrier functions (CBFs) with SDF at inference time, filtering unsafe actions post-hoc. Our negative finding---that EE-only auxiliary SDF loss is redundant at the tested scale---is specific to pathway~(a) and does not imply limitations for pathways~(b) and~(c), which address collision avoidance through fundamentally different mechanisms: constrained optimization of violation probability and runtime action filtering, respectively.\n\n\\paragraph{Evaluation Metrics for Safe Manipulation.}\nSafeLIBERO~\\cite{hu2025vlsa} extends LIBERO~\\cite{liu2023libero} with obstacle-augmented environments and a collision avoidance rate (CAR) metric. However, CAR treats all collision-free episodes identically: an action-collapsed robot scores near-perfect CAR without any avoidance behavior. This failure mode echoes concerns about metric reliability~\\cite{karwowski2024goodhart,gururangan2018annotation} and binary success metrics under limited samples~\\cite{snyder2026beyond}. Action collapse in diffusion policies~\\cite{dong2025conditioning} systematically inflates CAR but has not been previously examined as a safety evaluation confounder. We propose dfCAR (\\S\\ref{sec:dfcar}) to detect this contamination.\n",
    "structuredPatch": [
      {
        "oldStart": 12,
        "oldLines": 4,
        "newStart": 12,
        "newLines": 4,
        "lines": [
          " \\paragraph{SDF integration pathways.} Geometric supervision via signed distance fields can be integrated into VLA policies through fundamentally different mechanisms. (a)~\\emph{Training-time auxiliary loss}: an SDF-based collision penalty is added to the training objective, supervising only the end-effector trajectory (the approach tested in this work). (b)~\\emph{Constrained optimization}: SafeVLA~\\citep{zhang2025safevla} formulates collision avoidance as a constrained MDP, embedding safety constraints into the training objective via Lagrangian optimization rather than adding SDF as an auxiliary loss. (c)~\\emph{Runtime filtering}: VLSA~\\citep{hu2025vlsa} applies control barrier functions (CBFs) with SDF at inference time, filtering unsafe actions post-hoc. Our negative finding---that EE-only auxiliary SDF loss is redundant at the tested scale---is specific to pathway~(a) and does not imply limitations for pathways~(b) and~(c), which address collision avoidance through fundamentally different mechanisms: constrained optimization of violation probability and runtime action filtering, respectively.",
          " ",
          " \\paragraph{Evaluation Metrics for Safe Manipulation.}",
          "-SafeLIBERO~\\cite{hu2025vlsa} extends LIBERO~\\cite{liu2023libero} with obstacle-augmented environments and a collision avoidance rate (CAR) metric. However, CAR treats all collision-free episodes identically: an action-collapsed robot scores near-perfect CAR without any avoidance behavior. This failure mode echoes concerns about metric reliability~\\cite{karwowski2024goodhart,gururangan2018annotation} and binary success metrics under limited samples~\\cite{snyder2026beyond}. Action collapse in diffusion policies~\\cite{dong2025conditioning} systematically inflates CAR but has not been previously examined as a safety evaluation confounder. We propose dfCAR (\\S\\ref{sec:dfcar}) to detect this contamination.",
          "+SafeLIBERO~\\cite{hu2025vlsa} extends LIBERO~\\cite{liu2023libero} with obstacle-augmented environments and a collision avoidance rate (CAR) metric. However, CAR treats all collision-free episodes identically: an action-collapsed robot scores near-perfect CAR without any avoidance behavior. This failure mode echoes concerns about metric reliability~\\cite{karwowski2024goodhart,gururangan2018annotation} and binary success metrics under limited samples~\\cite{snyder2026beyond}. Action collapse in diffusion policies~\\cite{dong2025conditioning} systematically inflates CAR but has not been previously examined as a safety evaluation confounder. Concurrent work expands the evaluation landscape: HazardArena~\\cite{chen2026hazardarena} evaluates semantic safety through safe/unsafe twin scenarios, and VLA-Risk~\\cite{vlariskanon2026} benchmarks physical robustness across object, action, and spatial perturbation dimensions. We propose dfCAR (\\S\\ref{sec:dfcar}) to detect this contamination."
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

_source line 84_

Now add the bib entries:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "f427d58e-f6d0-4cdf-8e28-50f42e193590",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U85LUmUNVoxpcGxjcyuXev",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 436,
      "cache_read_input_tokens": 55967,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 436
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

_source line 85_

<details open><summary>🔧 Tool call — Edit · `toolu_01KH1Afmtm2Y3mENgA9yQDhB`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/references.bib",
  "old_string": "% ===== Action Collapse =====",
  "new_string": "% ===== VLA Safety Evaluation Benchmarks =====\n\n@article{chen2026hazardarena,\n  title={{HazardArena}: Evaluating Semantic Safety in Vision-Language-Action Models},\n  author={Chen, Zixing and Gao, Yifeng and Wang, Li and Zhao, Yunhan and Liu, Yi and Li, Jiayu and Zheng, Xiang and Wu, Zuxuan and Wang, Cong and Ma, Xingjun and Jiang, Yu-Gang},\n  journal={arXiv preprint arXiv:2604.12447},\n  year={2026}\n}\n\n@inproceedings{vlariskanon2026,\n  title={{VLA-Risk}: Benchmarking Vision-Language-Action Models with Physical Robustness},\n  author={Anonymous},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2026},\n  note={Under review}\n}\n\n% ===== Action Collapse ====="
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "18e7c7d0-8ae3-4737-9430-8e44c037faa9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U85LUmUNVoxpcGxjcyuXev",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 436,
      "cache_read_input_tokens": 55967,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 436
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

_source line 86 · 2026-05-28T06:52:58.118Z_

<details><summary>↩ Tool result · `toolu_01KH1Afmtm2Y3mENgA9yQDhB`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/references.bib has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "bf1352f8-91e5-48f3-9484-45171a14a2fc",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/references.bib",
    "oldString": "% ===== Action Collapse =====",
    "newString": "% ===== VLA Safety Evaluation Benchmarks =====\n\n@article{chen2026hazardarena,\n  title={{HazardArena}: Evaluating Semantic Safety in Vision-Language-Action Models},\n  author={Chen, Zixing and Gao, Yifeng and Wang, Li and Zhao, Yunhan and Liu, Yi and Li, Jiayu and Zheng, Xiang and Wu, Zuxuan and Wang, Cong and Ma, Xingjun and Jiang, Yu-Gang},\n  journal={arXiv preprint arXiv:2604.12447},\n  year={2026}\n}\n\n@inproceedings{vlariskanon2026,\n  title={{VLA-Risk}: Benchmarking Vision-Language-Action Models with Physical Robustness},\n  author={Anonymous},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2026},\n  note={Under review}\n}\n\n% ===== Action Collapse =====",
    "originalFile": "% The Safety Illusion — References\n% Analysis paper on fake safety in VLA collision avoidance evaluation\n% Generated: 2026-05-24\n\n% ===== VLA Foundation Models =====\n\n@article{black2024pi0,\n  title={$\\pi_0$: A Vision-Language-Action Flow Model for General Robot Control},\n  author={Black, Kevin and Brown, Noah and Driess, Danny and Esmail, Adnan and Equi, Michael and Finn, Chelsea and Fusai, Niccolo and Groom, Lachy and Hausman, Karol and Ichter, Brian and others},\n  journal={arXiv preprint arXiv:2410.24164},\n  year={2024}\n}\n\n@inproceedings{kim2024openvla,\n  title={{OpenVLA}: An Open-Source Vision-Language-Action Model},\n  author={Kim, Moo Jin and Pertsch, Karl and Karamcheti, Siddharth and Xiao, Ted and Balakrishna, Ashwin and Nair, Suraj and Rafailov, Rafael and Foster, Ethan and Lam, Grace and Nasiriany, Mohan and others},\n  booktitle={Conference on Robot Learning (CoRL)},\n  year={2024}\n}\n\n@inproceedings{brohan2023rt2,\n  title={{RT-2}: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},\n  author={Brohan, Anthony and Brown, Noah and Carbajal, Justice and Chebotar, Yevgen and Chen, Xi and Choromanski, Krzysztof and Ding, Tianli and Driess, Danny and Dubey, Avinava and Finn, Chelsea and others},\n  booktitle={Conference on Robot Learning (CoRL)},\n  year={2023}\n}\n\n% ===== Collision-Aware VLA Methods =====\n\n@article{hu2025vlsa,\n  title={{VLSA}: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer},\n  author={Hu, Songqiao and Liu, Zeyi and Liu, Shuang and Cen, Jun and Meng, Zihan and He, Xiao},\n  journal={arXiv preprint arXiv:2512.11891},\n  year={2025}\n}\n\n@inproceedings{zhang2025safevla,\n  title={{SafeVLA}: Towards Safety Alignment of Vision-Language-Action Model via Constrained Learning},\n  author={Zhang, Borong and Zhang, Yuhao and Ji, Jiaming and Lei, Yingshan and Dai, Josef and Chen, Yuanpei and Yang, Yaodong},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2025}\n}\n\n@article{cofreeevla2026,\n  title={{CoFreeVLA}: Collision-Free Dual-Arm Manipulation via Vision-Language-Action Model and Risk Estimation},\n  author={Zhai, Xuanran and Ou, Binkai and Yu, Qiaojun and Hao, Ce and Liu, Yaohua},\n  journal={arXiv preprint arXiv:2601.21712},\n  year={2026}\n}\n\n@article{spalter2024ikinqp,\n  title={Towards Online Safety Corrections for Robotic Manipulation Policies},\n  author={Spalter, Ariana and Roberts, Mark and Hiatt, Laura M.},\n  journal={arXiv preprint arXiv:2409.08233},\n  year={2024}\n}\n\n@inproceedings{li2024langguided,\n  title={Language-Guided Object-Centric Diffusion Policy for Collision-Aware Robotic Manipulation},\n  author={Li, Hang and Feng, Qian and Zheng, Zhi and Feng, Jianxiang and Chen, Zhaopeng and Knoll, Alois},\n  booktitle={IEEE International Conference on Robotics and Automation (ICRA)},\n  year={2025}\n}\n\n@article{yang2025cape,\n  title={{CAPE}: Context-Aware Diffusion Policy Via Proximal Mode Expansion for Collision Avoidance},\n  author={Yang, Rui Heng and Zhao, Xuan and Brunswic, Leo Maxime and Alban, Montgomery and Clemente, Mateo and Cao, Tongtong and Jin, Jun and Rasouli, Amir},\n  journal={arXiv preprint arXiv:2511.22773},\n  year={2025}\n}\n\n% ===== Safety in Diffusion Planning =====\n\n@inproceedings{xiao2025safediffuser,\n  title={{SafeDiffuser}: Safe Planning with Diffusion Probabilistic Models},\n  author={Xiao, Wei and Wang, Tsun-Hsuan and Gan, Chuang and Hasani, Ramin and Lechner, Mathias and Rus, Daniela},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2025}\n}\n\n% ===== SDF in Robotics =====\n\n@inproceedings{park2019deepsdf,\n  title={{DeepSDF}: Learning Continuous Signed Distance Functions for Shape Representation},\n  author={Park, Jeong Joon and Florence, Peter and Straub, Julian and Newcombe, Richard and Lovegrove, Steven},\n  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  year={2019}\n}\n\n@inproceedings{ortiz2022isdf,\n  title={{iSDF}: Real-Time Neural Signed Distance Fields for Robot Perception},\n  author={Ortiz, Joseph and Clegg, Alexander and Dong, Jing and Sucar, Edgar and Novotny, David and Zollh{\\\"o}fer, Michael and Mukadam, Mustafa},\n  booktitle={Robotics: Science and Systems (RSS)},\n  year={2022}\n}\n\n@article{zhi2021diffco,\n  title={{DiffCo}: Auto-Differentiable Proxy Collision Detection with Multi-class Labels for Safety-Aware Trajectory Optimization},\n  author={Zhi, Yuheng and Das, Nikhil and Yip, Michael},\n  journal={IEEE Transactions on Robotics},\n  volume={38},\n  number={5},\n  pages={2668--2685},\n  year={2022}\n}\n\n@inproceedings{huang2023voxposer,\n  title={{VoxPoser}: Composable {3D} Value Maps for Robotic Manipulation with Language Models},\n  author={Huang, Wenlong and Wang, Chen and Zhang, Ruohan and Li, Yunzhu and Wu, Jiajun and Fei-Fei, Li},\n  booktitle={Conference on Robot Learning (CoRL)},\n  year={2023}\n}\n\n% ===== Benchmarks and Training =====\n\n@inproceedings{liu2023libero,\n  title={{LIBERO}: Benchmarking Knowledge Transfer for Lifelong Robot Learning},\n  author={Liu, Bo and Zhu, Yifeng and Gao, Chongkai and Feng, Yihao and Liu, Qiang and Zhu, Yuke and Stone, Peter},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2023}\n}\n\n@inproceedings{lipman2023flow,\n  title={Flow Matching for Generative Modeling},\n  author={Lipman, Yaron and Chen, Ricky T. Q. and Ben-Hamu, Heli and Nickel, Maximilian and Le, Matt},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2023}\n}\n\n% ===== Evaluation Reliability =====\n\n@inproceedings{gururangan2018annotation,\n  title={Annotation Artifacts in Natural Language Inference Data},\n  author={Gururangan, Suchin and Swayamdipta, Swabha and Levy, Omer and Schwartz, Roy and Bowman, Samuel and Smith, Noah A.},\n  booktitle={Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},\n  year={2018}\n}\n\n@inproceedings{karwowski2024goodhart,\n  title={Goodhart's Law in Reinforcement Learning},\n  author={Karwowski, Jacek and Hayman, Oliver and Bai, Xingjian and Kiendlhofer, Klaus and Griffin, Charlie and Sherburn, Joar},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2024}\n}\n\n% ===== Diffusion Policy =====\n\n@inproceedings{chi2023diffusionpolicy,\n  title={Diffusion Policy: Visuomotor Policy Learning via Action Diffusion},\n  author={Chi, Cheng and Feng, Siyuan and Du, Yilun and Xu, Zhenjia and Cousineau, Eric and Burchfiel, Benjamin and Song, Shuran},\n  booktitle={Robotics: Science and Systems (RSS)},\n  year={2023}\n}\n\n% ===== Configuration/Robot-Body SDF =====\n\n@inproceedings{li2024cdf,\n  title={Configuration Space Distance Fields for Manipulation Planning},\n  author={Li, Yiming and Chi, Xuemin and Razmjoo, Amirreza and Calinon, Sylvain},\n  booktitle={Robotics: Science and Systems (RSS)},\n  year={2024}\n}\n\n@inproceedings{li2024rdf,\n  title={Representing Robot Geometry as Distance Fields: Applications to Whole-body Manipulation},\n  author={Li, Yiming and Zhang, Yan and Razmjoo, Amirreza and Calinon, Sylvain},\n  booktitle={IEEE International Conference on Robotics and Automation (ICRA)},\n  year={2024}\n}\n\n% ===== SDF in Robotics (additional) =====\n\n@inproceedings{vasilopoulos2023ramp,\n  title={{RAMP}: Hierarchical Reactive Motion Planning for Manipulation Tasks Using Implicit Signed Distance Functions},\n  author={Vasilopoulos, Vasileios and Garg, Suveer and Piacenza, Pedro and Huh, Jinwook and Isler, Volkan},\n  booktitle={IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)},\n  year={2023}\n}\n\n@article{chen2026cssdfnet,\n  title={{CSSDF-Net}: Safe Motion Planning Based on Neural Implicit Representations of Configuration Space Distance Field},\n  author={Chen, Haohua and Zhou, Yixuan and Zhou, Yifan and Wang, Hesheng},\n  journal={arXiv preprint arXiv:2603.18669},\n  year={2026}\n}\n\n@article{jacquet2025neuralnmpc,\n  title={Neural {NMPC} through Signed Distance Field Encoding for Collision Avoidance},\n  author={Jacquet, Martin and Harms, Marvin and Alexis, Kostas},\n  journal={The International Journal of Robotics Research},\n  year={2025}\n}\n\n% ===== 3D-Aware VLA Methods =====\n\n@article{depthvla2025,\n  title={{DepthVLA}: Enhancing Vision-Language-Action Models with Depth-Aware Spatial Reasoning},\n  author={Yuan, Tianyuan and Liu, Yicheng and Lu, Chenhao and Chen, Zhuoguang and Jiang, Tao and Zhao, Hang},\n  journal={arXiv preprint arXiv:2510.13375},\n  year={2025}\n}\n\n@article{li2025qdepth,\n  title={{QDepth-VLA}: Quantized Depth Prediction as Auxiliary Supervision for Vision-Language-Action Models},\n  author={Li, Yixuan and Chen, Yuhui and Zhou, Mingcai and Li, Haoran and Zhang, Zhengtao and Zhao, Dongbin},\n  journal={arXiv preprint arXiv:2510.14836},\n  year={2025}\n}\n\n@article{li2025spatialforcing,\n  title={Spatial Forcing: Implicit Spatial Representation Alignment for Vision-Language-Action Model},\n  author={Li, Fuhao and Song, Wenxuan and Zhao, Han and Wang, Jingbo and Ding, Pengxiang and Wang, Donglin and Zeng, Long and Li, Haoang},\n  journal={arXiv preprint arXiv:2510.12276},\n  year={2025}\n}\n\n% ===== Parameter-Efficient Fine-Tuning =====\n\n@inproceedings{hu2022lora,\n  author    = {Hu, Edward J. and Shen, Yelong and Wallis, Phillip and Allen-Zhu, Zeyuan and Li, Yuanzhi and Wang, Shean and Wang, Lu and Chen, Weizhu},\n  title     = {{LoRA}: Low-Rank Adaptation of Large Language Models},\n  booktitle = {International Conference on Learning Representations (ICLR)},\n  year      = {2022},\n}\n\n% ===== VLA Safety Survey =====\n\n@article{li2026vlasafety,\n  title={Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms},\n  author={Li, Qi and Yin, Bo and Huang, Weiqi and Liu, Ruhao and Zou, Bojun and Yu, Runpeng and Ye, Jingwen and Yu, Weihao and Wang, Xinchao},\n  journal={arXiv preprint arXiv:2604.23775},\n  year={2026}\n}\n\n% ===== Action Collapse =====\n\n@article{dong2025conditioning,\n  title={Conditioning Matters: Training Diffusion Policies is Faster Than You Think},\n  author={Dong, Zibin and Liu, Yicheng and Li, Yinchuan and Zhao, Hang and Hao, Jianye},\n  journal={arXiv preprint arXiv:2505.11123},\n  year={2025}\n}\n\n% ===== Evaluation Methodology =====\n\n@article{snyder2026beyond,\n  title={Beyond Binary Success: Sample-Efficient and Statistically Rigorous Robot Policy Comparison},\n  author={Snyder, David and Badithela, Apurva and Matni, Nikolai and Pappas, George and Majumdar, Anirudha and Itkina, Masha and Nishimura, Haruki},\n  journal={arXiv preprint arXiv:2603.13616},\n  year={2026}\n}\n",
    "structuredPatch": [
      {
        "oldStart": 232,
        "oldLines": 6,
        "newStart": 232,
        "newLines": 23,
        "lines": [
          "   year={2026}",
          " }",
          " ",
          "+% ===== VLA Safety Evaluation Benchmarks =====",
          "+",
          "+@article{chen2026hazardarena,",
          "+  title={{HazardArena}: Evaluating Semantic Safety in Vision-Language-Action Models},",
          "+  author={Chen, Zixing and Gao, Yifeng and Wang, Li and Zhao, Yunhan and Liu, Yi and Li, Jiayu and Zheng, Xiang and Wu, Zuxuan and Wang, Cong and Ma, Xingjun and Jiang, Yu-Gang},",
          "+  journal={arXiv preprint arXiv:2604.12447},",
          "+  year={2026}",
          "+}",
          "+",
          "+@inproceedings{vlariskanon2026,",
          "+  title={{VLA-Risk}: Benchmarking Vision-Language-Action Models with Physical Robustness},",
          "+  author={Anonymous},",
          "+  booktitle={International Conference on Learning Representations (ICLR)},",
          "+  year={2026},",
          "+  note={Under review}",
          "+}",
          "+",
          " % ===== Action Collapse =====",
          " ",
          " @article{dong2025conditioning,"
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

_source line 87_

P1 #10a/b done. Now **P2 #8** — "20×" in discussion.tex L6:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "b89f269d-3183-48be-b2c7-6755be6d8666",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012j3jNzpBQ17w559qmoM7vd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 567,
      "cache_read_input_tokens": 56403,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 567
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

_source line 88_

<details open><summary>🔧 Tool call — Edit · `toolu_01Swvqo7kVYgWKvwUQBRvJst`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex",
  "old_string": "Even at $\\lambda = 0.1$ (20$\\times$ the lowest tested weight)",
  "new_string": "Even at $\\lambda = 0.1$ (spanning an order of magnitude above the lowest tested weight)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "53a410e8-f206-41f9-9930-364e6ba1e355",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012j3jNzpBQ17w559qmoM7vd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 567,
      "cache_read_input_tokens": 56403,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 567
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

_source line 89 · 2026-05-28T06:53:02.496Z_

<details><summary>↩ Tool result · `toolu_01Swvqo7kVYgWKvwUQBRvJst`</summary>

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
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "57bac160-7884-4248-87d7-8eccb2ed9741",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex",
    "oldString": "Even at $\\lambda = 0.1$ (20$\\times$ the lowest tested weight)",
    "newString": "Even at $\\lambda = 0.1$ (spanning an order of magnitude above the lowest tested weight)",
    "originalFile": "\\section{Discussion and Conclusion}\\label{sec:conclusion}\n\nAcross 100+ experiments and 6000+ evaluation episodes on two VLA model families, three findings converge: CAR-based VLA safety evaluation, as currently practiced on SafeLIBERO, is structurally unreliable. Action collapse renders reported CAR illusory (\\S\\ref{sec:dfcar}); EE-only oracle refinement is counterproductive (\\S\\ref{sec:ee_only}); and collision-free demonstrations account for nearly all measured avoidance gains, with EE-only SDF contributing no statistically significant improvement (\\S\\ref{sec:avoidance_source}).\n\n\\paragraph{Why EE-only SDF fails.}\nTwo independent causes explain the null result. \\textit{(i)~Demonstration data largely subsumes the SDF signal.} Collision-free demonstrations implicitly encode spatial avoidance; the ${\\sim}$26\\,pp CAR gain arises primarily from this distributional shift, with per-task ordering invariant across all SDF conditions (\\S\\ref{sec:avoidance_source}). Even at $\\lambda = 0.1$ (20$\\times$ the lowest tested weight), CAR remains within the null distribution ($p = 0.131$), suggesting that EE-only auxiliary SDF loss does not overcome Level~A signal masking---the limitation is architectural for this integration pathway. \\textit{(ii)~EE monitoring cannot prevent full-body collisions.} The SDF gradient acts on a single point while collisions occur along intermediate links. Oracle experiments confirm this: ground-truth SDF refinement \\emph{reduces} CAR by 6--10\\,pp below unrefined baselines (\\S\\ref{sec:ee_only}), because pushing the EE away rotates unmonitored links through obstacles. We hypothesize that collision-free demonstration trajectories implicitly encode workspace priors through their spatial distribution: the robot learns to favor regions of the workspace that are inherently collision-free, without requiring explicit geometric supervision. These two causes are independent; effective geometric safety requires both full-body supervision and training signals beyond demonstrations. The failure of EE-only auxiliary SDF loss is architectural. Constrained-optimization approaches (e.g., SafeVLA) address collision avoidance through a fundamentally different optimization paradigm---directly constraining violation probability rather than adding geometric supervision---while runtime filtering sidesteps training altogether.\n\n\\paragraph{Implications for evaluation.}\ndfCAR corrects action-collapse contamination using only EE position logging, already available in most evaluation pipelines. The bimodal displacement distribution makes $\\tau_d$ robust across five orders of magnitude. We recommend reporting both CAR and dfCAR; the gap quantifies contamination. This contamination spans a 4000$\\times$ parameter range (Pi0 Full-FT ${\\sim}$2.5B to Pi0+A1 ${\\sim}$658K trainable), a structural consequence of evaluating avoidance without verifying motion. More broadly, safety may need to operate at the planning or joint-space constraint layer, since any EE-centric loss inherits the same blind spot.\n\n\\paragraph{Scope and generalizability.} Our findings are drawn from a single benchmark (SafeLIBERO) covering two VLA model families and four pick-and-place manipulation tasks in MuJoCo simulation. The action-collapse mechanism (Claim~1) is structurally general---any policy prone to action collapse will inflate CAR under standard evaluation---but its prevalence across other benchmarks, task types, and real hardware remains an open question. The finding that EE-only SDF shows no significant benefit (Claim~3) is specific to EE-only auxiliary loss integration and should not be extrapolated to alternative SDF integration pathways (Section~\\ref{sec:related}).\n\n\\paragraph{Limitations.}\nAll experiments are conducted in MuJoCo simulation within the SafeLIBERO benchmark. The sim-to-real gap introduces uncertainty: collision detection precision differs between simulation and physical hardware, sensor noise may affect displacement-filtered CAR differently on real robots, and the prevalence of action collapse in physical deployments remains untested. Our evaluation covers only four pick-and-place manipulation tasks with tabletop obstacles; whether the findings generalize to more diverse task families (e.g., bi-manual manipulation, deformable objects, dynamic obstacles) is an open question. Statistical power is limited by $n{=}3$ training seeds per condition, yielding a minimum detectable effect of approximately 5 percentage points at 80\\% power---smaller genuine effects, if they exist, would not be detected at this sample size. Oracle experiments used a largely action-collapsed model (Pi0+A1, TSR${\\approx}$0\\%); testing on an actively moving policy would better isolate the structural limitation. Full-body SDF remains untested. Fine-tuning degrades TSR by ${\\sim}$18--20\\,pp, yet SSR/TSR increases from 0.39 to 0.51--0.60 (Appendix~\\ref{sec:appendix_ssr}); reduced exposure alone does not explain the pattern.\n\n\\paragraph{Future work.}\nThree directions follow: (1) full-body SDF supervision along the kinematic chain; (2) cross-architecture evaluation on OpenVLA, RT-2, and other VLA families; (3) planning-layer safety constraints in joint space rather than EE space.\n\n\\paragraph{Broader impact.}\nThe displacement-filtered CAR metric (dfCAR) is intended as a diagnostic complement to standard CAR, not a replacement; practitioners should report both metrics to distinguish genuine avoidance from action-collapse artifacts. Our finding that EE-only SDF supervision is redundant at the tested scale with demonstration data is an evaluation-methodology insight, not a verdict against safety-aware training---geometric supervision may prove effective through alternative integration pathways or with full-body collision surfaces. We caution against interpreting these results as evidence that VLA safety research is futile; rather, they highlight the need for evaluation protocols that can reliably separate safety improvements from measurement artifacts.\n",
    "structuredPatch": [
      {
        "oldStart": 3,
        "oldLines": 7,
        "newStart": 3,
        "newLines": 7,
        "lines": [
          " Across 100+ experiments and 6000+ evaluation episodes on two VLA model families, three findings converge: CAR-based VLA safety evaluation, as currently practiced on SafeLIBERO, is structurally unreliable. Action collapse renders reported CAR illusory (\\S\\ref{sec:dfcar}); EE-only oracle refinement is counterproductive (\\S\\ref{sec:ee_only}); and collision-free demonstrations account for nearly all measured avoidance gains, with EE-only SDF contributing no statistically significant improvement (\\S\\ref{sec:avoidance_source}).",
          " ",
          " \\paragraph{Why EE-only SDF fails.}",
          "-Two independent causes explain the null result. \\textit{(i)~Demonstration data largely subsumes the SDF signal.} Collision-free demonstrations implicitly encode spatial avoidance; the ${\\sim}$26\\,pp CAR gain arises primarily from this distributional shift, with per-task ordering invariant across all SDF conditions (\\S\\ref{sec:avoidance_source}). Even at $\\lambda = 0.1$ (20$\\times$ the lowest tested weight), CAR remains within the null distribution ($p = 0.131$), suggesting that EE-only auxiliary SDF loss does not overcome Level~A signal masking---the limitation is architectural for this integration pathway. \\textit{(ii)~EE monitoring cannot prevent full-body collisions.} The SDF gradient acts on a single point while collisions occur along intermediate links. Oracle experiments confirm this: ground-truth SDF refinement \\emph{reduces} CAR by 6--10\\,pp below unrefined baselines (\\S\\ref{sec:ee_only}), because pushing the EE away rotates unmonitored links through obstacles. We hypothesize that collision-free demonstration trajectories implicitly encode workspace priors through their spatial distribution: the robot learns to favor regions of the workspace that are inherently collision-free, without requiring explicit geometric supervision. These two causes are independent; effective geometric safety requires both full-body supervision and training signals beyond demonstrations. The failure of EE-only auxiliary SDF loss is architectural. Constrained-optimization approaches (e.g., SafeVLA) address collision avoidance through a fundamentally different optimization paradigm---directly constraining violation probability rather than adding geometric supervision---while runtime filtering sidesteps training altogether.",
          "+Two independent causes explain the null result. \\textit{(i)~Demonstration data largely subsumes the SDF signal.} Collision-free demonstrations implicitly encode spatial avoidance; the ${\\sim}$26\\,pp CAR gain arises primarily from this distributional shift, with per-task ordering invariant across all SDF conditions (\\S\\ref{sec:avoidance_source}). Even at $\\lambda = 0.1$ (spanning an order of magnitude above the lowest tested weight), CAR remains within the null distribution ($p = 0.131$), suggesting that EE-only auxiliary SDF loss does not overcome Level~A signal masking---the limitation is architectural for this integration pathway. \\textit{(ii)~EE monitoring cannot prevent full-body collisions.} The SDF gradient acts on a single point while collisions occur along intermediate links. Oracle experiments confirm this: ground-truth SDF refinement \\emph{reduces} CAR by 6--10\\,pp below unrefined baselines (\\S\\ref{sec:ee_only}), because pushing the EE away rotates unmonitored links through obstacles. We hypothesize that collision-free demonstration trajectories implicitly encode workspace priors through their spatial distribution: the robot learns to favor regions of the workspace that are inherently collision-free, without requiring explicit geometric supervision. These two causes are independent; effective geometric safety requires both full-body supervision and training signals beyond demonstrations. The failure of EE-only auxiliary SDF loss is architectural. Constrained-optimization approaches (e.g., SafeVLA) address collision avoidance through a fundamentally different optimization paradigm---directly constraining violation probability rather than adding geometric supervision---while runtime filtering sidesteps training altogether.",
          " ",
          " \\paragraph{Implications for evaluation.}",
          " dfCAR corrects action-collapse contamination using only EE position logging, already available in most evaluation pipelines. The bimodal displacement distribution makes $\\tau_d$ robust across five orders of magnitude. We recommend reporting both CAR and dfCAR; the gap quantifies contamination. This contamination spans a 4000$\\times$ parameter range (Pi0 Full-FT ${\\sim}$2.5B to Pi0+A1 ${\\sim}$658K trainable), a structural consequence of evaluating avoidance without verifying motion. More broadly, safety may need to operate at the planning or joint-space constraint layer, since any EE-centric loss inherits the same blind spot."
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

_source line 90_

P2 #8 done. Now verify all changes:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "043b7b1a-d6ac-425a-9703-7a4cf51845ee",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012xWakTCGrH4TqACEWq4i5f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 271,
      "cache_read_input_tokens": 56970,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 271
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

_source line 91_

<details open><summary>🔧 Tool call — Grep · `toolu_0165STZWfX1cyx8F61ip3T4N`</summary>

```json
{
  "pattern": "Constrained optimization",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "0537db0d-69c8-42fd-9912-c5923be536b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012xWakTCGrH4TqACEWq4i5f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 271,
      "cache_read_input_tokens": 56970,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 271
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

_source line 92 · 2026-05-28T06:53:05.991Z_

<details><summary>↩ Tool result · `toolu_0165STZWfX1cyx8F61ip3T4N`</summary>

```text
docs/paper/related_work.tex:12:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "92008391-eeb2-4dd0-b25b-f0f3e0832a4c",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/related_work.tex:12:[Omitted long matching line]",
    "numLines": 1
  }
}
```

</details>

---

### Tool call

_source line 93_

<details open><summary>🔧 Tool call — Grep · `toolu_01UmoGkygFUfnV1VaLMhckkW`</summary>

```json
{
  "pattern": "redundant",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "588c2a81-b9a7-4518-85cc-af2a99de4308",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012xWakTCGrH4TqACEWq4i5f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 271,
      "cache_read_input_tokens": 56970,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 271
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

_source line 94 · 2026-05-28T06:53:06.810Z_

<details><summary>↩ Tool result · `toolu_01UmoGkygFUfnV1VaLMhckkW`</summary>

```text
docs/paper/related_work.tex:12:[Omitted long matching line]
docs/paper/discussion.tex:20:[Omitted long matching line]
docs/paper/archive/analysis_claim3.tex:28:[Omitted long matching line]
docs/paper/archive/analysis_claim3.tex:72:\placeholder{Pending: $\lambda = 0.1$ results will determine whether SDF supervision shows dose-dependent effects at higher loss weights or remains redundant across the full $\lambda$ range. Final narrative deferred until experimental results are available.}
docs/paper/contingency_claim3.tex:19:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "93e31e5a-cdd8-49f4-9f18-7ee755f0fe13",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/related_work.tex:12:[Omitted long matching line]\ndocs/paper/discussion.tex:20:[Omitted long matching line]\ndocs/paper/archive/analysis_claim3.tex:28:[Omitted long matching line]\ndocs/paper/archive/analysis_claim3.tex:72:\\placeholder{Pending: $\\lambda = 0.1$ results will determine whether SDF supervision shows dose-dependent effects at higher loss weights or remains redundant across the full $\\lambda$ range. Final narrative deferred until experimental results are available.}\ndocs/paper/contingency_claim3.tex:19:[Omitted long matching line]",
    "numLines": 5
  }
}
```

</details>

---

### Tool call

_source line 95_

<details open><summary>🔧 Tool call — Grep · `toolu_018cPZ5KLsCxbu4gHKhZ95Fr`</summary>

```json
{
  "pattern": "CAR-based",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "cd799cdb-96c7-49ed-9278-9a909b89950e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012xWakTCGrH4TqACEWq4i5f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 271,
      "cache_read_input_tokens": 56970,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 271
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

_source line 96 · 2026-05-28T06:53:07.777Z_

<details><summary>↩ Tool result · `toolu_018cPZ5KLsCxbu4gHKhZ95Fr`</summary>

```text
3:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "d566ba59-8e17-4102-88b2-4a947a4e62c4",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "3:[Omitted long matching line]",
    "numLines": 1
  }
}
```

</details>

---

### Tool call

_source line 97_

<details open><summary>🔧 Tool call — Grep · `toolu_01Hsk834AnpwjN8Adssb6Yfn`</summary>

```json
{
  "pattern": "HazardArena|VLA-Risk",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "923d0140-4b9a-45e3-b328-743cee4bd792",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012xWakTCGrH4TqACEWq4i5f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 271,
      "cache_read_input_tokens": 56970,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 271
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

_source line 98 · 2026-05-28T06:53:08.703Z_

<details><summary>↩ Tool result · `toolu_01Hsk834AnpwjN8Adssb6Yfn`</summary>

```text
docs/paper/related_work.tex:15:[Omitted long matching line]
docs/paper/references.bib:238:  title={{HazardArena}: Evaluating Semantic Safety in Vision-Language-Action Models},
docs/paper/references.bib:245:  title={{VLA-Risk}: Benchmarking Vision-Language-Action Models with Physical Robustness},
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "f23a7b93-209b-4bd4-9bb8-15430b425c96",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/related_work.tex:15:[Omitted long matching line]\ndocs/paper/references.bib:238:  title={{HazardArena}: Evaluating Semantic Safety in Vision-Language-Action Models},\ndocs/paper/references.bib:245:  title={{VLA-Risk}: Benchmarking Vision-Language-Action Models with Physical Robustness},",
    "numLines": 3
  }
}
```

</details>

---

### Tool call

_source line 99_

<details open><summary>🔧 Tool call — Grep · `toolu_016Homnb63qBtyAy9ySduqZi`</summary>

```json
{
  "pattern": "spanning an order",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "e1a2b6c4-b450-497d-869b-8f16c7a3bea0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012xWakTCGrH4TqACEWq4i5f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 271,
      "cache_read_input_tokens": 56970,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 271
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

_source line 100 · 2026-05-28T06:53:10.109Z_

<details><summary>↩ Tool result · `toolu_016Homnb63qBtyAy9ySduqZi`</summary>

```text
docs/paper/discussion.tex:6:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "de4a0d0a-e3d2-41e9-8ccb-2561112b0f97",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/discussion.tex:6:[Omitted long matching line]",
    "numLines": 1
  }
}
```

</details>

---

### Tool call

_source line 101_

<details open><summary>🔧 Tool call — Grep · `toolu_019aQ1ZDWR76kMq5dTSGM7FG`</summary>

```json
{
  "pattern": "absence of.*SDF|SDF.*no significant benefit",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "1c637563-37ca-4a56-8dee-801ce2c87dc9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012xWakTCGrH4TqACEWq4i5f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 271,
      "cache_read_input_tokens": 56970,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 271
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

_source line 102 · 2026-05-28T06:53:10.944Z_

<details><summary>↩ Tool result · `toolu_019aQ1ZDWR76kMq5dTSGM7FG`</summary>

```text
docs/paper/discussion.tex:11:[Omitted long matching line]
docs/paper/appendix.tex:229:To test whether the absence of EE-only SDF benefit generalizes beyond the primary \texttt{object\_pudding} scene, we replicate the core comparison on \texttt{spatial\_bowl}, a separate SafeLIBERO suite with a distinct obstacle layout (moka pot, wine bottle, milk carton, red coffee mug, yellow book). Both conditions use the same architecture, hyperparameters, and two-phase training schedule (30K steps), differing only in the training scene.
docs/paper/appendix.tex:235:\caption{Cross-scene validation on \texttt{spatial\_bowl} (single training seed, 200 episodes, 30K checkpoint). The $-$0.5\,pp CAR difference is well within noise, consistent with the absence of SDF benefit observed on \texttt{object\_pudding}.}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "7a2a148c-73a0-428b-97a4-844bc99308d6",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/discussion.tex:11:[Omitted long matching line]\ndocs/paper/appendix.tex:229:To test whether the absence of EE-only SDF benefit generalizes beyond the primary \\texttt{object\\_pudding} scene, we replicate the core comparison on \\texttt{spatial\\_bowl}, a separate SafeLIBERO suite with a distinct obstacle layout (moka pot, wine bottle, milk carton, red coffee mug, yellow book). Both conditions use the same architecture, hyperparameters, and two-phase training schedule (30K steps), differing only in the training scene.\ndocs/paper/appendix.tex:235:\\caption{Cross-scene validation on \\texttt{spatial\\_bowl} (single training seed, 200 episodes, 30K checkpoint). The $-$0.5\\,pp CAR difference is well within noise, consistent with the absence of SDF benefit observed on \\texttt{object\\_pudding}.}",
    "numLines": 3
  }
}
```

</details>

---

### Assistant

_source line 103_

<details><summary>Logged reasoning block</summary>

```text
All changes verified. Let me also verify that "redundant" in related_work.tex and discussion.tex now has "at the tested scale" qualifier.

The remaining "redundant" hits are:
1. related_work.tex:12 — should now have "redundant at the tested scale" ✓
2. discussion.tex:20 — should now have "redundant at the tested scale" ✓ 
3. archive/analysis_claim3.tex:28 — archive file, not in scope


4. archive/analysis_claim3.tex:72 — archive file, not in scope
5. contingency_claim3.tex:19 — not in scope (different file group)

Now I'll check those two in-scope instances to confirm the qualifier is actually there.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "99823f21-f50a-46f7-b89f-2d68674e19d1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BWQx9AEDAEvmhuzcFWvSR5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1446,
      "cache_read_input_tokens": 57241,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1446
      },
      "output_tokens": 31,
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

_source line 104_

Let me verify the "redundant" occurrences in our target files have the qualifier:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "48ccd944-ea00-4d3c-9aac-4f0ea858768c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BWQx9AEDAEvmhuzcFWvSR5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1446,
      "cache_read_input_tokens": 57241,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1446
      },
      "output_tokens": 31,
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

_source line 105_

<details open><summary>🔧 Tool call — Grep · `toolu_01EqC9C7KkTcqc3h2BdpUPm3`</summary>

```json
{
  "pattern": "redundant at the tested scale",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "d6dcac65-1f8e-40a4-8322-ae22a258990e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BWQx9AEDAEvmhuzcFWvSR5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1446,
      "cache_read_input_tokens": 57241,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1446
      },
      "output_tokens": 31,
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

_source line 106 · 2026-05-28T06:53:17.880Z_

<details><summary>↩ Tool result · `toolu_01EqC9C7KkTcqc3h2BdpUPm3`</summary>

```text
docs/paper/related_work.tex:12:[Omitted long matching line]
docs/paper/discussion.tex:20:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "335d4413-8d1f-40d6-93e3-553c16bbe434",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/related_work.tex:12:[Omitted long matching line]\ndocs/paper/discussion.tex:20:[Omitted long matching line]",
    "numLines": 2
  }
}
```

</details>

---

### Assistant

_source line 107_

全部修改完成。汇总：

### P0 #1: SafeVLA 分类事实性错误
- **related_work.tex L12**: "Constraint-based planning" → "Constrained optimization"；SafeVLA 描述改为 CMDP + Lagrangian optimization 范式；结尾句从 "bypass" 改为区分 constrained optimization vs runtime filtering 两种不同机制
- **discussion.tex L6**: "constraint-based and runtime filtering approaches bypass..." → 分别描述 SafeVLA（CMDP 约束违规概率）和 runtime filtering（跳过训练）

### P1 #3: "redundant" 5 处分层处理
1. **related_work.tex L12**: → "redundant at the tested scale" ✓
2. **discussion.tex L20**: → "redundant at the tested scale" ✓
3. **discussion.tex L11**: "SDF redundancy finding" → "finding that EE-only SDF shows no significant benefit" ✓
4. **appendix.tex L229**: → "absence of EE-only SDF benefit" ✓
5. **appendix.tex L235**: → "absence of SDF benefit" ✓

### P1 #4: Discussion 首句 scope
- **discussion.tex L3**: → "CAR-based VLA safety evaluation, as currently practiced on SafeLIBERO, is structurally unreliable" ✓

### P1 #10a/b: 补充引用
- **related_work.tex L15**: 评估段落加入 HazardArena（语义安全 twin scenarios）和 VLA-Risk（物理鲁棒性 benchmark）
- **references.bib**: 新增 `chen2026hazardarena` 和 `vlariskanon2026` 条目

### P2 #8: "20×" 替换
- **discussion.tex L6**: "20$\times$ the lowest tested weight" → "spanning an order of magnitude above the lowest tested weight" ✓
- **appendix.tex L181**: 无 "20×" 倍数声明（该行 "20" 是排列组合数 $\binom{6}{3}=20$），无需修改

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "uuid": "356e4580-640e-4cec-b84b-34283b609e4a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Dn8KdQCbKvKepFWdbhGpr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 511,
      "cache_read_input_tokens": 58687,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 511
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

_source line 108_

全部修改完成。汇总：

### P0 #1: SafeVLA 分类事实性错误
- **related_work.tex L12**: "Constraint-based planning" → "Constrained optimization"；SafeVLA 描述改为 CMDP + Lagrangian optimization 范式；结尾句从 "bypass" 改为区分 constrained optimization vs runtime filtering 两种不同机制
- **discussion.tex L6**: "constraint-based and runtime filtering approaches bypass..." → 分别描述 SafeVLA（CMDP 约束违规概率）和 runtime filtering（跳过训练）

### P1 #3: "redundant" 5 处分层处理
1. **related_work.tex L12**: → "redundant at the tested scale" ✓
2. **discussion.tex L20**: → "redundant at the tested scale" ✓
3. **discussion.tex L11**: "SDF redundancy finding" → "finding that EE-only SDF shows no significant benefit" ✓
4. **appendix.tex L229**: → "absence of EE-only SDF benefit" ✓
5. **appendix.tex L235**: → "absence of SDF benefit" ✓

### P1 #4: Discussion 首句 scope
- **discussion.tex L3**: → "CAR-based VLA safety evaluation, as currently practiced on SafeLIBERO, is structurally unreliable" ✓

### P1 #10a/b: 补充引用
- **related_work.tex L15**: 评估段落加入 HazardArena（语义安全 twin scenarios）和 VLA-Risk（物理鲁棒性 benchmark）
- **references.bib**: 新增 `chen2026hazardarena` 和 `vlariskanon2026` 条目

### P2 #8: "20×" 替换
- **discussion.tex L6**: "20$\times$ the lowest tested weight" → "spanning an order of magnitude above the lowest tested weight" ✓
- **appendix.tex L181**: 无 "20×" 倍数声明（该行 "20" 是排列组合数 $\binom{6}{3}=20$），无需修改

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 198275,
  "duration_api_ms": 211449,
  "num_turns": 41,
  "stop_reason": "end_turn",
  "session_id": "6990a794-354e-41e2-98df-6fbecdb4bb79",
  "total_cost_usd": 1.11265225,
  "usage": {
    "input_tokens": 4372,
    "cache_creation_input_tokens": 47747,
    "cache_read_input_tokens": 893885,
    "output_tokens": 10288,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 47747,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 577,
        "cache_read_input_tokens": 58687,
        "cache_creation_input_tokens": 511,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 511
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 42011,
      "outputTokens": 1244,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 4,
      "costUSD": 0.088231,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 4372,
      "outputTokens": 10288,
      "cacheReadInputTokens": 893885,
      "cacheCreationInputTokens": 47747,
      "webSearchRequests": 0,
      "costUSD": 1.0244212499999998,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "5ff77a8e-f4e8-4de3-9928-84a6aafb9e34"
}
```

</details>

---
