# writing related work revision

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 30
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/workers/worker_writing_related-work-revision_20260515T044848.log`
- **Structured JSON:** [`d2f1f3fe2e703cb99149.json`](../../sessions/d2/d2f1f3fe2e703cb99149.json)

## Before a recorded user message

30 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon",
  "session_id": "6f05e234-65d5-4fab-b46e-1cc055fade54",
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
  "uuid": "36fafd58-cf3d-47a7-8481-ddf98e9f888e",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/memory/"
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
    "resetsAt": 1778836800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "c7b773d7-8686-4f52-a05a-4c11b1c4823b",
  "session_id": "6f05e234-65d5-4fab-b46e-1cc055fade54"
}
```

---

### Assistant

_source line 4_

I'll read the Related Work draft first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6f05e234-65d5-4fab-b46e-1cc055fade54",
  "uuid": "47416594-82b1-4958-aaf5-57fd3dcd73e7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BwFoWjLboYpnS77fHgpGf8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12330,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12330
      },
      "output_tokens": 4,
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

<details open><summary>🔧 Tool call — Read · `toolu_01P3BLbBdDVkWWsDgjYS35Da`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/paper_drafts/related_work_draft.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6f05e234-65d5-4fab-b46e-1cc055fade54",
  "uuid": "eeb6e235-6bd7-41db-90e6-db8b88d8478c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BwFoWjLboYpnS77fHgpGf8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12330,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12330
      },
      "output_tokens": 4,
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

_source line 6 · 2026-05-15T04:49:01.310Z_

<details><summary>↩ Tool result · `toolu_01P3BLbBdDVkWWsDgjYS35Da`</summary>

```text
1	# Related Work — Draft
2	
3	## 2.1 World-Model Reinforcement Learning
4	
5	World-model reinforcement learning trains agents by learning a predictive model of environment dynamics and using it to generate synthetic experience for policy optimization. The Dreamer family of algorithms \citep{hafner2020dreamerv1, hafner2021dreamerv2, hafner2023dreamerv3} epitomizes this paradigm: a recurrent state-space model (RSSM) learns latent dynamics from interaction data, and an actor-critic pair is trained entirely within the model's imagined rollouts. DreamerV3 \citep{hafner2023dreamerv3} introduced symlog normalization and discrete latent representations that enable a single set of hyperparameters to master diverse domains, establishing it as the dominant imagination-based architecture. More recently, DreamerV4 \citep{hafner2025dreamerv4} replaces RSSM with a transformer world model, demonstrating scalability to video pretraining, though the core imagination-based training paradigm remains unchanged.
6	
7	A well-known risk in model-based RL is \emph{model exploitation}: the policy optimizer can discover and exploit inaccuracies in the learned model, producing policies that perform well in imagination but fail in the real environment. \citet{janner2019mbpo} formalize this concern and propose short-horizon branched rollouts to limit exploitation. Pessimistic approaches such as MOPO \citep{yu2020mopo} penalize reward by model uncertainty to discourage exploitation of unreliable regions. An orthogonal line of work avoids imagination-based training altogether: TD-MPC2 \citep{hansen2024tdmpc2} performs online model-predictive control at test time, sidestepping the need for imagination-trained value functions. Our work operates squarely within the DreamerV3 imagination-based training paradigm and diagnoses a specific form of model exploitation—value overestimation triggered by temporal conditioning—that prior model exploitation analyses have not identified.
8	
9	## 2.2 Temporal Abstraction in Reinforcement Learning
10	
11	Temporal abstraction—the ability to reason and act at multiple timescales—has been a long-standing goal in RL. The options framework \citep{sutton1999options} formalizes temporally extended actions as option policies with initiation sets and termination conditions, operating at the semi-MDP level. In the model-free setting, several methods learn variable action persistence: FiGAR \citep{sharma2017figar} augments the action space with a discrete repeat count, \citet{lakshminarayanan2017dynamic} learn per-step repetition durations, and TempoRL \citep{biedenkapp2021temporl} trains a skip-policy that achieves up to 10$\times$ speedup on control tasks. These model-free approaches avoid the failure mode we identify because they do not train value functions on imagined rollouts with variable temporal granularity.
12	
13	Within world-model RL, temporal abstraction has been pursued primarily through \emph{hierarchical} architectures. Director \citep{hafner2022director} introduces subgoal-conditioned planning in the Dreamer latent space. THICK \citep{gumbsch2024thick} learns adaptive temporal abstractions via context-change detection, constructing a hierarchy of latent dynamics models. Hieros \citep{mattes2024hieros} builds multi-scale hierarchical imagination with S5 world models. LS-Imagine \citep{li2025lsimagine} extends the effective imagination horizon via goal-conditioned jumpy state transitions. These hierarchical methods sidestep the single-scale variable-$dt$ approach we investigate, and our diagnostic results provide a mechanistic explanation for why hierarchy may be preferable: flat $dt$-embedding conditioning introduces delusional critic dynamics that hierarchical decomposition avoids.
14	
15	Most relevant to our work is TAWM \citep{nhu2025tawm}, which explicitly conditions a world model on time-step size $\Delta t$ and trains over diverse $\Delta t$ values for multi-rate dynamics learning. TAWM demonstrates that $\Delta t$ conditioning \emph{improves} performance and data efficiency—but critically, TAWM is built on TD-MPC2 and uses online model-predictive control, not imagination-based actor-critic training. Our work reveals that the same $\Delta t$ conditioning that benefits MPC-based planning becomes pathological in imagination-based training: the critic exploits $dt$-conditioned value estimates from imprecise multi-step RSSM predictions, producing systematic overestimation. This paradigm-dependent asymmetry—beneficial in MPC, harmful in imagination-based actor-critic—is a central finding of our diagnostic analysis.
16	
17	The sensitivity of RL algorithms to time discretization has been studied theoretically: \citet{tallec2019making} show that Q-learning performance is highly sensitive to the discretization interval $\delta$ and propose architectural modifications for $\delta$-invariance. SAR \citep{park2021sar} achieves time-discretization-invariant action repetition in model-free policy gradient methods. MTS3 \citep{shaj2023mts3} proposes a probabilistic multi-time-scale state space model for variable-rate prediction. Our work demonstrates that world-model RL currently lacks this robustness: RSSM predictions trained at $\delta\!=\!1$ degrade substantially at $dt\!>\!1$, and temporal conditioning amplifies rather than compensates for this degradation.
18	
19	## 2.3 Value Overestimation and Delusional Bias
20	
21	Value overestimation in deep RL was first identified by \citet{thrun1993issues}, who showed that function approximation introduces systematic upward bias through the max operator in Q-learning. Double Q-learning \citep{vanhasselt2016double} addresses this by decoupling action selection from value estimation, and TD3 \citep{fujimoto2018td3} extends the idea to continuous control with clipped double critics. Ensemble methods such as SUNRISE \citep{lee2021sunrise} use uncertainty-weighted value estimation to further suppress overestimation. DreamerV3 uses a single critic trained via categorical cross-entropy with symlog normalization \citep{hafner2023dreamerv3}, which provides some implicit regularization against overestimation \citep{farebrother2024stopregressing} but, as we show, is insufficient to prevent $dt$-embedding-induced value exploitation.
22	
23	Distinct from general overestimation, \citet{lu2018nondelusional} formalize \emph{delusional bias}: inconsistencies arising when Q-value backups assume policies that lie outside the representable policy class, producing value estimates that no realizable policy can achieve. \citet{su2020conqur} extend this with consistency-penalized Q-labels. Our work identifies an analogous phenomenon in a fundamentally different setting. Where Lu et al.'s delusional bias arises from policy-class constraints in tabular or function-approximation Q-learning, our \emph{delusional critic} arises from temporal conditioning in world-model imagination: the critic learns precise $dt$-conditioned value estimates, but the RSSM's prediction fidelity at $dt\!>\!1$ is insufficient to support this precision. The result is systematic overestimation of imagined trajectories at longer temporal steps—a form of delusion specific to the interaction between temporal conditioning and model-based imagination, not to function approximation per se.
24	
25	Recent work has connected value overestimation to training dynamics in model-based settings. \citet{hussing2024dissecting} show that high update-to-data ratios drive value divergence through optimizer momentum, with overestimation occurring on both in-distribution and out-of-distribution data. \citet{voelcker2025madtd} address value misgeneralization from replay distribution mismatch using model-generated data. Our delusional critic mechanism is complementary: the overestimation we identify is not driven by update ratios or distribution mismatch, but by the critic's ability to exploit temporally conditioned predictions from an imprecise world model.
26	
27	## 2.4 Multi-Step Prediction and Compounding Error
28	
29	Compounding prediction error is a fundamental challenge in model-based RL: small per-step model inaccuracies accumulate over multi-step rollouts, producing trajectories that diverge from ground truth. \citet{venkatraman2015improving} establish theoretical guarantees relating single-step training error to multi-step prediction error via the Data-as-Demonstrator framework. \citet{asadi2019combating} propose multi-step models that predict several steps ahead in a single forward pass to bypass the sequential error accumulation of autoregressive rollouts. \citet{ke2019learning} incorporate long-term future information into dynamics learning via latent-variable autoregressive models. \citet{lambert2022investigating} provide a systematic empirical study of how compounding error properties vary across model architectures and training procedures.
30	
31	Recent work has examined the downstream consequences of rollout quality degradation. \citet{frauenknecht2025rollouts} show that trajectory-sampling rollouts diverge from ground truth after only a few steps and can actively harm policy learning, proposing uncertainty-based rollout termination as a mitigation. \citet{barkley2024stealing} demonstrate that synthetic rollouts degrade performance inconsistently across environments, with overestimation bias as a contributing factor.
32	
33	Our findings add a new dimension to this literature. When imagination operates at $dt\!>\!1$, the RSSM must predict further into the future per step, amplifying compounding error: we observe observation prediction MSE increasing from a $2.04\times$ gap (dt=1 vs.\ dt=2) at baseline to substantially degraded absolute accuracy in collapsed configurations. However, compounding error alone does not explain the catastrophic collapse we observe. Our controlled experiments show that configurations with identical compounding error exposure (same $dt$, same horizon) produce qualitatively different outcomes depending on whether the $dt$-embedding is trained: untrained $dt$-embedding yields stable learning despite degraded prediction quality, while trained $dt$-embedding triggers accelerating value overestimation and collapse. The root cause is not prediction error per se, but the critic's exploitation of precise temporal conditioning built on imprecise predictions—a failure mode that compounds \emph{on top of} the standard compounding error problem.
34	
35	---
36	
37	**Overall positioning.** Temporal abstraction in world-model RL sits at the intersection of four well-studied areas: world-model architecture, temporal abstraction methods, value overestimation, and multi-step prediction error. Yet the specific interaction between temporal conditioning and imagination-based actor-critic training has received virtually no attention. Existing temporal abstraction methods operate in model-free or MPC settings where the failure mode we identify does not arise; existing analyses of value overestimation and compounding error do not consider temporal conditioning as a causal factor. Our work fills this gap by providing the first systematic diagnosis of why variable-rate imagination fails in DreamerV3, identifying trained $dt$-embedding as the mechanism that bridges imprecise multi-step predictions to pathological value overestimation, and offering a practical mitigation: restricting imagination to $dt\!=\!1$ during multi-$dt$ training recovers 95\% of baseline performance without any architectural modification.
38	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6f05e234-65d5-4fab-b46e-1cc055fade54",
  "uuid": "23e7096a-9a6b-4506-9c4a-abb514864d55",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/paper_drafts/related_work_draft.md",
      "content": "# Related Work — Draft\n\n## 2.1 World-Model Reinforcement Learning\n\nWorld-model reinforcement learning trains agents by learning a predictive model of environment dynamics and using it to generate synthetic experience for policy optimization. The Dreamer family of algorithms \\citep{hafner2020dreamerv1, hafner2021dreamerv2, hafner2023dreamerv3} epitomizes this paradigm: a recurrent state-space model (RSSM) learns latent dynamics from interaction data, and an actor-critic pair is trained entirely within the model's imagined rollouts. DreamerV3 \\citep{hafner2023dreamerv3} introduced symlog normalization and discrete latent representations that enable a single set of hyperparameters to master diverse domains, establishing it as the dominant imagination-based architecture. More recently, DreamerV4 \\citep{hafner2025dreamerv4} replaces RSSM with a transformer world model, demonstrating scalability to video pretraining, though the core imagination-based training paradigm remains unchanged.\n\nA well-known risk in model-based RL is \\emph{model exploitation}: the policy optimizer can discover and exploit inaccuracies in the learned model, producing policies that perform well in imagination but fail in the real environment. \\citet{janner2019mbpo} formalize this concern and propose short-horizon branched rollouts to limit exploitation. Pessimistic approaches such as MOPO \\citep{yu2020mopo} penalize reward by model uncertainty to discourage exploitation of unreliable regions. An orthogonal line of work avoids imagination-based training altogether: TD-MPC2 \\citep{hansen2024tdmpc2} performs online model-predictive control at test time, sidestepping the need for imagination-trained value functions. Our work operates squarely within the DreamerV3 imagination-based training paradigm and diagnoses a specific form of model exploitation—value overestimation triggered by temporal conditioning—that prior model exploitation analyses have not identified.\n\n## 2.2 Temporal Abstraction in Reinforcement Learning\n\nTemporal abstraction—the ability to reason and act at multiple timescales—has been a long-standing goal in RL. The options framework \\citep{sutton1999options} formalizes temporally extended actions as option policies with initiation sets and termination conditions, operating at the semi-MDP level. In the model-free setting, several methods learn variable action persistence: FiGAR \\citep{sharma2017figar} augments the action space with a discrete repeat count, \\citet{lakshminarayanan2017dynamic} learn per-step repetition durations, and TempoRL \\citep{biedenkapp2021temporl} trains a skip-policy that achieves up to 10$\\times$ speedup on control tasks. These model-free approaches avoid the failure mode we identify because they do not train value functions on imagined rollouts with variable temporal granularity.\n\nWithin world-model RL, temporal abstraction has been pursued primarily through \\emph{hierarchical} architectures. Director \\citep{hafner2022director} introduces subgoal-conditioned planning in the Dreamer latent space. THICK \\citep{gumbsch2024thick} learns adaptive temporal abstractions via context-change detection, constructing a hierarchy of latent dynamics models. Hieros \\citep{mattes2024hieros} builds multi-scale hierarchical imagination with S5 world models. LS-Imagine \\citep{li2025lsimagine} extends the effective imagination horizon via goal-conditioned jumpy state transitions. These hierarchical methods sidestep the single-scale variable-$dt$ approach we investigate, and our diagnostic results provide a mechanistic explanation for why hierarchy may be preferable: flat $dt$-embedding conditioning introduces delusional critic dynamics that hierarchical decomposition avoids.\n\nMost relevant to our work is TAWM \\citep{nhu2025tawm}, which explicitly conditions a world model on time-step size $\\Delta t$ and trains over diverse $\\Delta t$ values for multi-rate dynamics learning. TAWM demonstrates that $\\Delta t$ conditioning \\emph{improves} performance and data efficiency—but critically, TAWM is built on TD-MPC2 and uses online model-predictive control, not imagination-based actor-critic training. Our work reveals that the same $\\Delta t$ conditioning that benefits MPC-based planning becomes pathological in imagination-based training: the critic exploits $dt$-conditioned value estimates from imprecise multi-step RSSM predictions, producing systematic overestimation. This paradigm-dependent asymmetry—beneficial in MPC, harmful in imagination-based actor-critic—is a central finding of our diagnostic analysis.\n\nThe sensitivity of RL algorithms to time discretization has been studied theoretically: \\citet{tallec2019making} show that Q-learning performance is highly sensitive to the discretization interval $\\delta$ and propose architectural modifications for $\\delta$-invariance. SAR \\citep{park2021sar} achieves time-discretization-invariant action repetition in model-free policy gradient methods. MTS3 \\citep{shaj2023mts3} proposes a probabilistic multi-time-scale state space model for variable-rate prediction. Our work demonstrates that world-model RL currently lacks this robustness: RSSM predictions trained at $\\delta\\!=\\!1$ degrade substantially at $dt\\!>\\!1$, and temporal conditioning amplifies rather than compensates for this degradation.\n\n## 2.3 Value Overestimation and Delusional Bias\n\nValue overestimation in deep RL was first identified by \\citet{thrun1993issues}, who showed that function approximation introduces systematic upward bias through the max operator in Q-learning. Double Q-learning \\citep{vanhasselt2016double} addresses this by decoupling action selection from value estimation, and TD3 \\citep{fujimoto2018td3} extends the idea to continuous control with clipped double critics. Ensemble methods such as SUNRISE \\citep{lee2021sunrise} use uncertainty-weighted value estimation to further suppress overestimation. DreamerV3 uses a single critic trained via categorical cross-entropy with symlog normalization \\citep{hafner2023dreamerv3}, which provides some implicit regularization against overestimation \\citep{farebrother2024stopregressing} but, as we show, is insufficient to prevent $dt$-embedding-induced value exploitation.\n\nDistinct from general overestimation, \\citet{lu2018nondelusional} formalize \\emph{delusional bias}: inconsistencies arising when Q-value backups assume policies that lie outside the representable policy class, producing value estimates that no realizable policy can achieve. \\citet{su2020conqur} extend this with consistency-penalized Q-labels. Our work identifies an analogous phenomenon in a fundamentally different setting. Where Lu et al.'s delusional bias arises from policy-class constraints in tabular or function-approximation Q-learning, our \\emph{delusional critic} arises from temporal conditioning in world-model imagination: the critic learns precise $dt$-conditioned value estimates, but the RSSM's prediction fidelity at $dt\\!>\\!1$ is insufficient to support this precision. The result is systematic overestimation of imagined trajectories at longer temporal steps—a form of delusion specific to the interaction between temporal conditioning and model-based imagination, not to function approximation per se.\n\nRecent work has connected value overestimation to training dynamics in model-based settings. \\citet{hussing2024dissecting} show that high update-to-data ratios drive value divergence through optimizer momentum, with overestimation occurring on both in-distribution and out-of-distribution data. \\citet{voelcker2025madtd} address value misgeneralization from replay distribution mismatch using model-generated data. Our delusional critic mechanism is complementary: the overestimation we identify is not driven by update ratios or distribution mismatch, but by the critic's ability to exploit temporally conditioned predictions from an imprecise world model.\n\n## 2.4 Multi-Step Prediction and Compounding Error\n\nCompounding prediction error is a fundamental challenge in model-based RL: small per-step model inaccuracies accumulate over multi-step rollouts, producing trajectories that diverge from ground truth. \\citet{venkatraman2015improving} establish theoretical guarantees relating single-step training error to multi-step prediction error via the Data-as-Demonstrator framework. \\citet{asadi2019combating} propose multi-step models that predict several steps ahead in a single forward pass to bypass the sequential error accumulation of autoregressive rollouts. \\citet{ke2019learning} incorporate long-term future information into dynamics learning via latent-variable autoregressive models. \\citet{lambert2022investigating} provide a systematic empirical study of how compounding error properties vary across model architectures and training procedures.\n\nRecent work has examined the downstream consequences of rollout quality degradation. \\citet{frauenknecht2025rollouts} show that trajectory-sampling rollouts diverge from ground truth after only a few steps and can actively harm policy learning, proposing uncertainty-based rollout termination as a mitigation. \\citet{barkley2024stealing} demonstrate that synthetic rollouts degrade performance inconsistently across environments, with overestimation bias as a contributing factor.\n\nOur findings add a new dimension to this literature. When imagination operates at $dt\\!>\\!1$, the RSSM must predict further into the future per step, amplifying compounding error: we observe observation prediction MSE increasing from a $2.04\\times$ gap (dt=1 vs.\\ dt=2) at baseline to substantially degraded absolute accuracy in collapsed configurations. However, compounding error alone does not explain the catastrophic collapse we observe. Our controlled experiments show that configurations with identical compounding error exposure (same $dt$, same horizon) produce qualitatively different outcomes depending on whether the $dt$-embedding is trained: untrained $dt$-embedding yields stable learning despite degraded prediction quality, while trained $dt$-embedding triggers accelerating value overestimation and collapse. The root cause is not prediction error per se, but the critic's exploitation of precise temporal conditioning built on imprecise predictions—a failure mode that compounds \\emph{on top of} the standard compounding error problem.\n\n---\n\n**Overall positioning.** Temporal abstraction in world-model RL sits at the intersection of four well-studied areas: world-model architecture, temporal abstraction methods, value overestimation, and multi-step prediction error. Yet the specific interaction between temporal conditioning and imagination-based actor-critic training has received virtually no attention. Existing temporal abstraction methods operate in model-free or MPC settings where the failure mode we identify does not arise; existing analyses of value overestimation and compounding error do not consider temporal conditioning as a causal factor. Our work fills this gap by providing the first systematic diagnosis of why variable-rate imagination fails in DreamerV3, identifying trained $dt$-embedding as the mechanism that bridges imprecise multi-step predictions to pathological value overestimation, and offering a practical mitigation: restricting imagination to $dt\\!=\\!1$ during multi-$dt$ training recovers 95\\% of baseline performance without any architectural modification.\n",
      "numLines": 38,
      "startLine": 1,
      "totalLines": 38
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
Now I have the full draft. Let me plan the 6 modifications:

1. **Item 1**: Find "95%" mentions and add the qualifier "preliminary results show near-baseline recovery (95% in initial seed)"
   - Line 37: "recovers 95\% of baseline performance" → needs modification

2. **Item 2**: Add a paragraph about diagnostic methodology, citing Engstrom et al. 2020 and Andrychowicz et al. 2021

3. **Item 3**: Add a sentence at end of Section 2.3 about ensemble/pessimistic not applicable
   
4. **Item 4**: Add a sentence in Section 2.1 about MuZero/EfficientZero

5. **Item 5**: Soften hierarchy claims - find mentions about hierarchical methods "avoiding" delusional critic

6. **Item 7**: Trim Section 2.4 by ~30-40%, removing overlap with 2.3

Let me start making these edits. First, I'll locate line 37 and change "recovers 95\% of baseline performance without any architectural modification" to "preliminary results show near-baseline recovery (95\% in initial seed) without any architectural modification". Then I'll add the diagnostic methodology paragraph as a new section 2.5, drawing on those two papers. I'll also add the ensemble note to 2.3, insert the MuZero reference into 2.1, soften the language around hierarchical methods avoiding delusional critic issues, and cut down 2.4 to eliminate redundancy with 2.3.

For the diagnostic methodology section, I'm thinking it makes sense to place it before the overall positioning paragraph rather than nested within an existing section. I'll add it after 2.4, creating a new 2.5 that discusses how we can diagnose these issues empirically. Then I need to soften line 13's claim about hierarchical decomposition avoiding delusional critic dynamics—changing it to acknowledge we don't actually test this hypothesis. Finally, I'll trim 2.4 significantly, removing the value overestimation discussion that overlaps with what's already in 2.3, particularly that third paragraph.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6f05e234-65d5-4fab-b46e-1cc055fade54",
  "uuid": "13c3bcef-d148-4249-aaf1-5a1904b46bb1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KbqMjxkTFNto5H8PGW2vhT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2842,
      "cache_read_input_tokens": 23777,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2842
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

I have the draft. Now I'll apply all 6 modifications.

**Item 1**: Fixing "95%" claim in the Overall positioning paragraph.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6f05e234-65d5-4fab-b46e-1cc055fade54",
  "uuid": "84d875e5-f3a3-4141-be36-9fb270a90c5d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KbqMjxkTFNto5H8PGW2vhT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2842,
      "cache_read_input_tokens": 23777,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2842
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

<details open><summary>🔧 Tool call — Edit · `toolu_01M92ZjXGtdCtbPVDLxBaVn6`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/paper_drafts/related_work_draft.md",
  "old_string": "restricting imagination to $dt\\!=\\!1$ during multi-$dt$ training recovers 95\\% of baseline performance without any architectural modification.",
  "new_string": "restricting imagination to $dt\\!=\\!1$ during multi-$dt$ training, where preliminary results show near-baseline recovery (95\\% in initial seed) without any architectural modification."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6f05e234-65d5-4fab-b46e-1cc055fade54",
  "uuid": "00c75972-2dd1-4a23-a135-1808e4829181",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KbqMjxkTFNto5H8PGW2vhT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2842,
      "cache_read_input_tokens": 23777,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2842
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

_source line 10 · 2026-05-15T04:49:21.366Z_

<details><summary>↩ Tool result · `toolu_01M92ZjXGtdCtbPVDLxBaVn6`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/paper_drafts/related_work_draft.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6f05e234-65d5-4fab-b46e-1cc055fade54",
  "uuid": "0a92ed9b-bfd8-4c9e-899b-f3daa01f6502",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/paper_drafts/related_work_draft.md",
    "oldString": "restricting imagination to $dt\\!=\\!1$ during multi-$dt$ training recovers 95\\% of baseline performance without any architectural modification.",
    "newString": "restricting imagination to $dt\\!=\\!1$ during multi-$dt$ training, where preliminary results show near-baseline recovery (95\\% in initial seed) without any architectural modification.",
    "originalFile": "# Related Work — Draft\n\n## 2.1 World-Model Reinforcement Learning\n\nWorld-model reinforcement learning trains agents by learning a predictive model of environment dynamics and using it to generate synthetic experience for policy optimization. The Dreamer family of algorithms \\citep{hafner2020dreamerv1, hafner2021dreamerv2, hafner2023dreamerv3} epitomizes this paradigm: a recurrent state-space model (RSSM) learns latent dynamics from interaction data, and an actor-critic pair is trained entirely within the model's imagined rollouts. DreamerV3 \\citep{hafner2023dreamerv3} introduced symlog normalization and discrete latent representations that enable a single set of hyperparameters to master diverse domains, establishing it as the dominant imagination-based architecture. More recently, DreamerV4 \\citep{hafner2025dreamerv4} replaces RSSM with a transformer world model, demonstrating scalability to video pretraining, though the core imagination-based training paradigm remains unchanged.\n\nA well-known risk in model-based RL is \\emph{model exploitation}: the policy optimizer can discover and exploit inaccuracies in the learned model, producing policies that perform well in imagination but fail in the real environment. \\citet{janner2019mbpo} formalize this concern and propose short-horizon branched rollouts to limit exploitation. Pessimistic approaches such as MOPO \\citep{yu2020mopo} penalize reward by model uncertainty to discourage exploitation of unreliable regions. An orthogonal line of work avoids imagination-based training altogether: TD-MPC2 \\citep{hansen2024tdmpc2} performs online model-predictive control at test time, sidestepping the need for imagination-trained value functions. Our work operates squarely within the DreamerV3 imagination-based training paradigm and diagnoses a specific form of model exploitation—value overestimation triggered by temporal conditioning—that prior model exploitation analyses have not identified.\n\n## 2.2 Temporal Abstraction in Reinforcement Learning\n\nTemporal abstraction—the ability to reason and act at multiple timescales—has been a long-standing goal in RL. The options framework \\citep{sutton1999options} formalizes temporally extended actions as option policies with initiation sets and termination conditions, operating at the semi-MDP level. In the model-free setting, several methods learn variable action persistence: FiGAR \\citep{sharma2017figar} augments the action space with a discrete repeat count, \\citet{lakshminarayanan2017dynamic} learn per-step repetition durations, and TempoRL \\citep{biedenkapp2021temporl} trains a skip-policy that achieves up to 10$\\times$ speedup on control tasks. These model-free approaches avoid the failure mode we identify because they do not train value functions on imagined rollouts with variable temporal granularity.\n\nWithin world-model RL, temporal abstraction has been pursued primarily through \\emph{hierarchical} architectures. Director \\citep{hafner2022director} introduces subgoal-conditioned planning in the Dreamer latent space. THICK \\citep{gumbsch2024thick} learns adaptive temporal abstractions via context-change detection, constructing a hierarchy of latent dynamics models. Hieros \\citep{mattes2024hieros} builds multi-scale hierarchical imagination with S5 world models. LS-Imagine \\citep{li2025lsimagine} extends the effective imagination horizon via goal-conditioned jumpy state transitions. These hierarchical methods sidestep the single-scale variable-$dt$ approach we investigate, and our diagnostic results provide a mechanistic explanation for why hierarchy may be preferable: flat $dt$-embedding conditioning introduces delusional critic dynamics that hierarchical decomposition avoids.\n\nMost relevant to our work is TAWM \\citep{nhu2025tawm}, which explicitly conditions a world model on time-step size $\\Delta t$ and trains over diverse $\\Delta t$ values for multi-rate dynamics learning. TAWM demonstrates that $\\Delta t$ conditioning \\emph{improves} performance and data efficiency—but critically, TAWM is built on TD-MPC2 and uses online model-predictive control, not imagination-based actor-critic training. Our work reveals that the same $\\Delta t$ conditioning that benefits MPC-based planning becomes pathological in imagination-based training: the critic exploits $dt$-conditioned value estimates from imprecise multi-step RSSM predictions, producing systematic overestimation. This paradigm-dependent asymmetry—beneficial in MPC, harmful in imagination-based actor-critic—is a central finding of our diagnostic analysis.\n\nThe sensitivity of RL algorithms to time discretization has been studied theoretically: \\citet{tallec2019making} show that Q-learning performance is highly sensitive to the discretization interval $\\delta$ and propose architectural modifications for $\\delta$-invariance. SAR \\citep{park2021sar} achieves time-discretization-invariant action repetition in model-free policy gradient methods. MTS3 \\citep{shaj2023mts3} proposes a probabilistic multi-time-scale state space model for variable-rate prediction. Our work demonstrates that world-model RL currently lacks this robustness: RSSM predictions trained at $\\delta\\!=\\!1$ degrade substantially at $dt\\!>\\!1$, and temporal conditioning amplifies rather than compensates for this degradation.\n\n## 2.3 Value Overestimation and Delusional Bias\n\nValue overestimation in deep RL was first identified by \\citet{thrun1993issues}, who showed that function approximation introduces systematic upward bias through the max operator in Q-learning. Double Q-learning \\citep{vanhasselt2016double} addresses this by decoupling action selection from value estimation, and TD3 \\citep{fujimoto2018td3} extends the idea to continuous control with clipped double critics. Ensemble methods such as SUNRISE \\citep{lee2021sunrise} use uncertainty-weighted value estimation to further suppress overestimation. DreamerV3 uses a single critic trained via categorical cross-entropy with symlog normalization \\citep{hafner2023dreamerv3}, which provides some implicit regularization against overestimation \\citep{farebrother2024stopregressing} but, as we show, is insufficient to prevent $dt$-embedding-induced value exploitation.\n\nDistinct from general overestimation, \\citet{lu2018nondelusional} formalize \\emph{delusional bias}: inconsistencies arising when Q-value backups assume policies that lie outside the representable policy class, producing value estimates that no realizable policy can achieve. \\citet{su2020conqur} extend this with consistency-penalized Q-labels. Our work identifies an analogous phenomenon in a fundamentally different setting. Where Lu et al.'s delusional bias arises from policy-class constraints in tabular or function-approximation Q-learning, our \\emph{delusional critic} arises from temporal conditioning in world-model imagination: the critic learns precise $dt$-conditioned value estimates, but the RSSM's prediction fidelity at $dt\\!>\\!1$ is insufficient to support this precision. The result is systematic overestimation of imagined trajectories at longer temporal steps—a form of delusion specific to the interaction between temporal conditioning and model-based imagination, not to function approximation per se.\n\nRecent work has connected value overestimation to training dynamics in model-based settings. \\citet{hussing2024dissecting} show that high update-to-data ratios drive value divergence through optimizer momentum, with overestimation occurring on both in-distribution and out-of-distribution data. \\citet{voelcker2025madtd} address value misgeneralization from replay distribution mismatch using model-generated data. Our delusional critic mechanism is complementary: the overestimation we identify is not driven by update ratios or distribution mismatch, but by the critic's ability to exploit temporally conditioned predictions from an imprecise world model.\n\n## 2.4 Multi-Step Prediction and Compounding Error\n\nCompounding prediction error is a fundamental challenge in model-based RL: small per-step model inaccuracies accumulate over multi-step rollouts, producing trajectories that diverge from ground truth. \\citet{venkatraman2015improving} establish theoretical guarantees relating single-step training error to multi-step prediction error via the Data-as-Demonstrator framework. \\citet{asadi2019combating} propose multi-step models that predict several steps ahead in a single forward pass to bypass the sequential error accumulation of autoregressive rollouts. \\citet{ke2019learning} incorporate long-term future information into dynamics learning via latent-variable autoregressive models. \\citet{lambert2022investigating} provide a systematic empirical study of how compounding error properties vary across model architectures and training procedures.\n\nRecent work has examined the downstream consequences of rollout quality degradation. \\citet{frauenknecht2025rollouts} show that trajectory-sampling rollouts diverge from ground truth after only a few steps and can actively harm policy learning, proposing uncertainty-based rollout termination as a mitigation. \\citet{barkley2024stealing} demonstrate that synthetic rollouts degrade performance inconsistently across environments, with overestimation bias as a contributing factor.\n\nOur findings add a new dimension to this literature. When imagination operates at $dt\\!>\\!1$, the RSSM must predict further into the future per step, amplifying compounding error: we observe observation prediction MSE increasing from a $2.04\\times$ gap (dt=1 vs.\\ dt=2) at baseline to substantially degraded absolute accuracy in collapsed configurations. However, compounding error alone does not explain the catastrophic collapse we observe. Our controlled experiments show that configurations with identical compounding error exposure (same $dt$, same horizon) produce qualitatively different outcomes depending on whether the $dt$-embedding is trained: untrained $dt$-embedding yields stable learning despite degraded prediction quality, while trained $dt$-embedding triggers accelerating value overestimation and collapse. The root cause is not prediction error per se, but the critic's exploitation of precise temporal conditioning built on imprecise predictions—a failure mode that compounds \\emph{on top of} the standard compounding error problem.\n\n---\n\n**Overall positioning.** Temporal abstraction in world-model RL sits at the intersection of four well-studied areas: world-model architecture, temporal abstraction methods, value overestimation, and multi-step prediction error. Yet the specific interaction between temporal conditioning and imagination-based actor-critic training has received virtually no attention. Existing temporal abstraction methods operate in model-free or MPC settings where the failure mode we identify does not arise; existing analyses of value overestimation and compounding error do not consider temporal conditioning as a causal factor. Our work fills this gap by providing the first systematic diagnosis of why variable-rate imagination fails in DreamerV3, identifying trained $dt$-embedding as the mechanism that bridges imprecise multi-step predictions to pathological value overestimation, and offering a practical mitigation: restricting imagination to $dt\\!=\\!1$ during multi-$dt$ training recovers 95\\% of baseline performance without any architectural modification.\n",
    "structuredPatch": [
      {
        "oldStart": 34,
        "oldLines": 4,
        "newStart": 34,
        "newLines": 4,
        "lines": [
          " ",
          " ---",
          " ",
          "-**Overall positioning.** Temporal abstraction in world-model RL sits at the intersection of four well-studied areas: world-model architecture, temporal abstraction methods, value overestimation, and multi-step prediction error. Yet the specific interaction between temporal conditioning and imagination-based actor-critic training has received virtually no attention. Existing temporal abstraction methods operate in model-free or MPC settings where the failure mode we identify does not arise; existing analyses of value overestimation and compounding error do not consider temporal conditioning as a causal factor. Our work fills this gap by providing the first systematic diagnosis of why variable-rate imagination fails in DreamerV3, identifying trained $dt$-embedding as the mechanism that bridges imprecise multi-step predictions to pathological value overestimation, and offering a practical mitigation: restricting imagination to $dt\\!=\\!1$ during multi-$dt$ training recovers 95\\% of baseline performance without any architectural modification.",
          "+**Overall positioning.** Temporal abstraction in world-model RL sits at the intersection of four well-studied areas: world-model architecture, temporal abstraction methods, value overestimation, and multi-step prediction error. Yet the specific interaction between temporal conditioning and imagination-based actor-critic training has received virtually no attention. Existing temporal abstraction methods operate in model-free or MPC settings where the failure mode we identify does not arise; existing analyses of value overestimation and compounding error do not consider temporal conditioning as a causal factor. Our work fills this gap by providing the first systematic diagnosis of why variable-rate imagination fails in DreamerV3, identifying trained $dt$-embedding as the mechanism that bridges imprecise multi-step predictions to pathological value overestimation, and offering a practical mitigation: restricting imagination to $dt\\!=\\!1$ during multi-$dt$ training, where preliminary results show near-baseline recovery (95\\% in initial seed) without any architectural modification."
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

**Item 4**: Adding MuZero/EfficientZero mention in Section 2.1.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6f05e234-65d5-4fab-b46e-1cc055fade54",
  "uuid": "b3eabaed-7cff-4795-83cd-367100baa7ae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B8AsPpumBVJnZJsN1f3ihn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 870,
      "cache_read_input_tokens": 26619,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 870
      },
      "output_tokens": 4,
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

<details open><summary>🔧 Tool call — Edit · `toolu_012iP5zdupBqYQ5WgtYyo7NV`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/paper_drafts/related_work_draft.md",
  "old_string": "An orthogonal line of work avoids imagination-based training altogether: TD-MPC2 \\citep{hansen2024tdmpc2} performs online model-predictive control at test time, sidestepping the need for imagination-trained value functions.",
  "new_string": "Planning-based approaches such as MuZero \\citep{schrittwieser2020muzero} and EfficientZero \\citep{ye2021efficientzero} use learned models for tree search rather than imagination rollouts for policy improvement, and thus do not exhibit the temporal-conditioning failure mode we diagnose. An orthogonal line of work avoids imagination-based training altogether: TD-MPC2 \\citep{hansen2024tdmpc2} performs online model-predictive control at test time, sidestepping the need for imagination-trained value functions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6f05e234-65d5-4fab-b46e-1cc055fade54",
  "uuid": "bbf9b122-15b7-4d7a-b0d5-0fc062c037f5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B8AsPpumBVJnZJsN1f3ihn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 870,
      "cache_read_input_tokens": 26619,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 870
      },
      "output_tokens": 4,
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

_source line 13 · 2026-05-15T04:49:28.335Z_

<details><summary>↩ Tool result · `toolu_012iP5zdupBqYQ5WgtYyo7NV`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/paper_drafts/related_work_draft.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6f05e234-65d5-4fab-b46e-1cc055fade54",
  "uuid": "265c0ecd-5717-4fe5-820d-0313b617d8f1",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/paper_drafts/related_work_draft.md",
    "oldString": "An orthogonal line of work avoids imagination-based training altogether: TD-MPC2 \\citep{hansen2024tdmpc2} performs online model-predictive control at test time, sidestepping the need for imagination-trained value functions.",
    "newString": "Planning-based approaches such as MuZero \\citep{schrittwieser2020muzero} and EfficientZero \\citep{ye2021efficientzero} use learned models for tree search rather than imagination rollouts for policy improvement, and thus do not exhibit the temporal-conditioning failure mode we diagnose. An orthogonal line of work avoids imagination-based training altogether: TD-MPC2 \\citep{hansen2024tdmpc2} performs online model-predictive control at test time, sidestepping the need for imagination-trained value functions.",
    "originalFile": "# Related Work — Draft\n\n## 2.1 World-Model Reinforcement Learning\n\nWorld-model reinforcement learning trains agents by learning a predictive model of environment dynamics and using it to generate synthetic experience for policy optimization. The Dreamer family of algorithms \\citep{hafner2020dreamerv1, hafner2021dreamerv2, hafner2023dreamerv3} epitomizes this paradigm: a recurrent state-space model (RSSM) learns latent dynamics from interaction data, and an actor-critic pair is trained entirely within the model's imagined rollouts. DreamerV3 \\citep{hafner2023dreamerv3} introduced symlog normalization and discrete latent representations that enable a single set of hyperparameters to master diverse domains, establishing it as the dominant imagination-based architecture. More recently, DreamerV4 \\citep{hafner2025dreamerv4} replaces RSSM with a transformer world model, demonstrating scalability to video pretraining, though the core imagination-based training paradigm remains unchanged.\n\nA well-known risk in model-based RL is \\emph{model exploitation}: the policy optimizer can discover and exploit inaccuracies in the learned model, producing policies that perform well in imagination but fail in the real environment. \\citet{janner2019mbpo} formalize this concern and propose short-horizon branched rollouts to limit exploitation. Pessimistic approaches such as MOPO \\citep{yu2020mopo} penalize reward by model uncertainty to discourage exploitation of unreliable regions. An orthogonal line of work avoids imagination-based training altogether: TD-MPC2 \\citep{hansen2024tdmpc2} performs online model-predictive control at test time, sidestepping the need for imagination-trained value functions. Our work operates squarely within the DreamerV3 imagination-based training paradigm and diagnoses a specific form of model exploitation—value overestimation triggered by temporal conditioning—that prior model exploitation analyses have not identified.\n\n## 2.2 Temporal Abstraction in Reinforcement Learning\n\nTemporal abstraction—the ability to reason and act at multiple timescales—has been a long-standing goal in RL. The options framework \\citep{sutton1999options} formalizes temporally extended actions as option policies with initiation sets and termination conditions, operating at the semi-MDP level. In the model-free setting, several methods learn variable action persistence: FiGAR \\citep{sharma2017figar} augments the action space with a discrete repeat count, \\citet{lakshminarayanan2017dynamic} learn per-step repetition durations, and TempoRL \\citep{biedenkapp2021temporl} trains a skip-policy that achieves up to 10$\\times$ speedup on control tasks. These model-free approaches avoid the failure mode we identify because they do not train value functions on imagined rollouts with variable temporal granularity.\n\nWithin world-model RL, temporal abstraction has been pursued primarily through \\emph{hierarchical} architectures. Director \\citep{hafner2022director} introduces subgoal-conditioned planning in the Dreamer latent space. THICK \\citep{gumbsch2024thick} learns adaptive temporal abstractions via context-change detection, constructing a hierarchy of latent dynamics models. Hieros \\citep{mattes2024hieros} builds multi-scale hierarchical imagination with S5 world models. LS-Imagine \\citep{li2025lsimagine} extends the effective imagination horizon via goal-conditioned jumpy state transitions. These hierarchical methods sidestep the single-scale variable-$dt$ approach we investigate, and our diagnostic results provide a mechanistic explanation for why hierarchy may be preferable: flat $dt$-embedding conditioning introduces delusional critic dynamics that hierarchical decomposition avoids.\n\nMost relevant to our work is TAWM \\citep{nhu2025tawm}, which explicitly conditions a world model on time-step size $\\Delta t$ and trains over diverse $\\Delta t$ values for multi-rate dynamics learning. TAWM demonstrates that $\\Delta t$ conditioning \\emph{improves} performance and data efficiency—but critically, TAWM is built on TD-MPC2 and uses online model-predictive control, not imagination-based actor-critic training. Our work reveals that the same $\\Delta t$ conditioning that benefits MPC-based planning becomes pathological in imagination-based training: the critic exploits $dt$-conditioned value estimates from imprecise multi-step RSSM predictions, producing systematic overestimation. This paradigm-dependent asymmetry—beneficial in MPC, harmful in imagination-based actor-critic—is a central finding of our diagnostic analysis.\n\nThe sensitivity of RL algorithms to time discretization has been studied theoretically: \\citet{tallec2019making} show that Q-learning performance is highly sensitive to the discretization interval $\\delta$ and propose architectural modifications for $\\delta$-invariance. SAR \\citep{park2021sar} achieves time-discretization-invariant action repetition in model-free policy gradient methods. MTS3 \\citep{shaj2023mts3} proposes a probabilistic multi-time-scale state space model for variable-rate prediction. Our work demonstrates that world-model RL currently lacks this robustness: RSSM predictions trained at $\\delta\\!=\\!1$ degrade substantially at $dt\\!>\\!1$, and temporal conditioning amplifies rather than compensates for this degradation.\n\n## 2.3 Value Overestimation and Delusional Bias\n\nValue overestimation in deep RL was first identified by \\citet{thrun1993issues}, who showed that function approximation introduces systematic upward bias through the max operator in Q-learning. Double Q-learning \\citep{vanhasselt2016double} addresses this by decoupling action selection from value estimation, and TD3 \\citep{fujimoto2018td3} extends the idea to continuous control with clipped double critics. Ensemble methods such as SUNRISE \\citep{lee2021sunrise} use uncertainty-weighted value estimation to further suppress overestimation. DreamerV3 uses a single critic trained via categorical cross-entropy with symlog normalization \\citep{hafner2023dreamerv3}, which provides some implicit regularization against overestimation \\citep{farebrother2024stopregressing} but, as we show, is insufficient to prevent $dt$-embedding-induced value exploitation.\n\nDistinct from general overestimation, \\citet{lu2018nondelusional} formalize \\emph{delusional bias}: inconsistencies arising when Q-value backups assume policies that lie outside the representable policy class, producing value estimates that no realizable policy can achieve. \\citet{su2020conqur} extend this with consistency-penalized Q-labels. Our work identifies an analogous phenomenon in a fundamentally different setting. Where Lu et al.'s delusional bias arises from policy-class constraints in tabular or function-approximation Q-learning, our \\emph{delusional critic} arises from temporal conditioning in world-model imagination: the critic learns precise $dt$-conditioned value estimates, but the RSSM's prediction fidelity at $dt\\!>\\!1$ is insufficient to support this precision. The result is systematic overestimation of imagined trajectories at longer temporal steps—a form of delusion specific to the interaction between temporal conditioning and model-based imagination, not to function approximation per se.\n\nRecent work has connected value overestimation to training dynamics in model-based settings. \\citet{hussing2024dissecting} show that high update-to-data ratios drive value divergence through optimizer momentum, with overestimation occurring on both in-distribution and out-of-distribution data. \\citet{voelcker2025madtd} address value misgeneralization from replay distribution mismatch using model-generated data. Our delusional critic mechanism is complementary: the overestimation we identify is not driven by update ratios or distribution mismatch, but by the critic's ability to exploit temporally conditioned predictions from an imprecise world model.\n\n## 2.4 Multi-Step Prediction and Compounding Error\n\nCompounding prediction error is a fundamental challenge in model-based RL: small per-step model inaccuracies accumulate over multi-step rollouts, producing trajectories that diverge from ground truth. \\citet{venkatraman2015improving} establish theoretical guarantees relating single-step training error to multi-step prediction error via the Data-as-Demonstrator framework. \\citet{asadi2019combating} propose multi-step models that predict several steps ahead in a single forward pass to bypass the sequential error accumulation of autoregressive rollouts. \\citet{ke2019learning} incorporate long-term future information into dynamics learning via latent-variable autoregressive models. \\citet{lambert2022investigating} provide a systematic empirical study of how compounding error properties vary across model architectures and training procedures.\n\nRecent work has examined the downstream consequences of rollout quality degradation. \\citet{frauenknecht2025rollouts} show that trajectory-sampling rollouts diverge from ground truth after only a few steps and can actively harm policy learning, proposing uncertainty-based rollout termination as a mitigation. \\citet{barkley2024stealing} demonstrate that synthetic rollouts degrade performance inconsistently across environments, with overestimation bias as a contributing factor.\n\nOur findings add a new dimension to this literature. When imagination operates at $dt\\!>\\!1$, the RSSM must predict further into the future per step, amplifying compounding error: we observe observation prediction MSE increasing from a $2.04\\times$ gap (dt=1 vs.\\ dt=2) at baseline to substantially degraded absolute accuracy in collapsed configurations. However, compounding error alone does not explain the catastrophic collapse we observe. Our controlled experiments show that configurations with identical compounding error exposure (same $dt$, same horizon) produce qualitatively different outcomes depending on whether the $dt$-embedding is trained: untrained $dt$-embedding yields stable learning despite degraded prediction quality, while trained $dt$-embedding triggers accelerating value overestimation and collapse. The root cause is not prediction error per se, but the critic's exploitation of precise temporal conditioning built on imprecise predictions—a failure mode that compounds \\emph{on top of} the standard compounding error problem.\n\n---\n\n**Overall positioning.** Temporal abstraction in world-model RL sits at the intersection of four well-studied areas: world-model architecture, temporal abstraction methods, value overestimation, and multi-step prediction error. Yet the specific interaction between temporal conditioning and imagination-based actor-critic training has received virtually no attention. Existing temporal abstraction methods operate in model-free or MPC settings where the failure mode we identify does not arise; existing analyses of value overestimation and compounding error do not consider temporal conditioning as a causal factor. Our work fills this gap by providing the first systematic diagnosis of why variable-rate imagination fails in DreamerV3, identifying trained $dt$-embedding as the mechanism that bridges imprecise multi-step predictions to pathological value overestimation, and offering a practical mitigation: restricting imagination to $dt\\!=\\!1$ during multi-$dt$ training, where preliminary results show near-baseline recovery (95\\% in initial seed) without any architectural modification.\n",
    "structuredPatch": [
      {
        "oldStart": 4,
        "oldLines": 7,
        "newStart": 4,
        "newLines": 7,
        "lines": [
          " ",
          " World-model reinforcement learning trains agents by learning a predictive model of environment dynamics and using it to generate synthetic experience for policy optimization. The Dreamer family of algorithms \\citep{hafner2020dreamerv1, hafner2021dreamerv2, hafner2023dreamerv3} epitomizes this paradigm: a recurrent state-space model (RSSM) learns latent dynamics from interaction data, and an actor-critic pair is trained entirely within the model's imagined rollouts. DreamerV3 \\citep{hafner2023dreamerv3} introduced symlog normalization and discrete latent representations that enable a single set of hyperparameters to master diverse domains, establishing it as the dominant imagination-based architecture. More recently, DreamerV4 \\citep{hafner2025dreamerv4} replaces RSSM with a transformer world model, demonstrating scalability to video pretraining, though the core imagination-based training paradigm remains unchanged.",
          " ",
          "-A well-known risk in model-based RL is \\emph{model exploitation}: the policy optimizer can discover and exploit inaccuracies in the learned model, producing policies that perform well in imagination but fail in the real environment. \\citet{janner2019mbpo} formalize this concern and propose short-horizon branched rollouts to limit exploitation. Pessimistic approaches such as MOPO \\citep{yu2020mopo} penalize reward by model uncertainty to discourage exploitation of unreliable regions. An orthogonal line of work avoids imagination-based training altogether: TD-MPC2 \\citep{hansen2024tdmpc2} performs online model-predictive control at test time, sidestepping the need for imagination-trained value functions. Our work operates squarely within the DreamerV3 imagination-based training paradigm and diagnoses a specific form of model exploitation—value overestimation triggered by temporal conditioning—that prior model exploitation analyses have not identified.",
          "+A well-known risk in model-based RL is \\emph{model exploitation}: the policy optimizer can discover and exploit inaccuracies in the learned model, producing policies that perform well in imagination but fail in the real environment. \\citet{janner2019mbpo} formalize this concern and propose short-horizon branched rollouts to limit exploitation. Pessimistic approaches such as MOPO \\citep{yu2020mopo} penalize reward by model uncertainty to discourage exploitation of unreliable regions. Planning-based approaches such as MuZero \\citep{schrittwieser2020muzero} and EfficientZero \\citep{ye2021efficientzero} use learned models for tree search rather than imagination rollouts for policy improvement, and thus do not exhibit the temporal-conditioning failure mode we diagnose. An orthogonal line of work avoids imagination-based training altogether: TD-MPC2 \\citep{hansen2024tdmpc2} performs online model-predictive control at test time, sidestepping the need for imagination-trained value functions. Our work operates squarely within the DreamerV3 imagination-based training paradigm and diagnoses a specific form of model exploitation—value overestimation triggered by temporal conditioning—that prior model exploitation analyses have not identified.",
          " ",
          " ## 2.2 Temporal Abstraction in Reinforcement Learning",
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

_source line 14_

**Item 5**: Softening hierarchy claims in Section 2.2.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6f05e234-65d5-4fab-b46e-1cc055fade54",
  "uuid": "269ec0a7-656a-457b-bd32-8f3b8ac26f8d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014keN1mpvZNwvWfCECL6q93",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 424,
      "cache_read_input_tokens": 27489,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 424
      },
      "output_tokens": 7,
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

_source line 15_

<details open><summary>🔧 Tool call — Edit · `toolu_01H8qKSDRoNy9DhnrVsVB9k3`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/paper_drafts/related_work_draft.md",
  "old_string": "These hierarchical methods sidestep the single-scale variable-$dt$ approach we investigate, and our diagnostic results provide a mechanistic explanation for why hierarchy may be preferable: flat $dt$-embedding conditioning introduces delusional critic dynamics that hierarchical decomposition avoids.",
  "new_string": "These hierarchical methods sidestep the single-scale variable-$dt$ approach we investigate. Hierarchical approaches may avoid the delusional critic phenomenon by operating at fixed temporal granularities within each level, though we do not test this hypothesis."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6f05e234-65d5-4fab-b46e-1cc055fade54",
  "uuid": "472c0935-39fb-415e-8dd7-0cff351898df",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014keN1mpvZNwvWfCECL6q93",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 424,
      "cache_read_input_tokens": 27489,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 424
      },
      "output_tokens": 7,
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

_source line 16 · 2026-05-15T04:49:35.013Z_

<details><summary>↩ Tool result · `toolu_01H8qKSDRoNy9DhnrVsVB9k3`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/paper_drafts/related_work_draft.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6f05e234-65d5-4fab-b46e-1cc055fade54",
  "uuid": "e97dad3d-c083-423e-a7b5-636b7d8fc50e",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/paper_drafts/related_work_draft.md",
    "oldString": "These hierarchical methods sidestep the single-scale variable-$dt$ approach we investigate, and our diagnostic results provide a mechanistic explanation for why hierarchy may be preferable: flat $dt$-embedding conditioning introduces delusional critic dynamics that hierarchical decomposition avoids.",
    "newString": "These hierarchical methods sidestep the single-scale variable-$dt$ approach we investigate. Hierarchical approaches may avoid the delusional critic phenomenon by operating at fixed temporal granularities within each level, though we do not test this hypothesis.",
    "originalFile": "# Related Work — Draft\n\n## 2.1 World-Model Reinforcement Learning\n\nWorld-model reinforcement learning trains agents by learning a predictive model of environment dynamics and using it to generate synthetic experience for policy optimization. The Dreamer family of algorithms \\citep{hafner2020dreamerv1, hafner2021dreamerv2, hafner2023dreamerv3} epitomizes this paradigm: a recurrent state-space model (RSSM) learns latent dynamics from interaction data, and an actor-critic pair is trained entirely within the model's imagined rollouts. DreamerV3 \\citep{hafner2023dreamerv3} introduced symlog normalization and discrete latent representations that enable a single set of hyperparameters to master diverse domains, establishing it as the dominant imagination-based architecture. More recently, DreamerV4 \\citep{hafner2025dreamerv4} replaces RSSM with a transformer world model, demonstrating scalability to video pretraining, though the core imagination-based training paradigm remains unchanged.\n\nA well-known risk in model-based RL is \\emph{model exploitation}: the policy optimizer can discover and exploit inaccuracies in the learned model, producing policies that perform well in imagination but fail in the real environment. \\citet{janner2019mbpo} formalize this concern and propose short-horizon branched rollouts to limit exploitation. Pessimistic approaches such as MOPO \\citep{yu2020mopo} penalize reward by model uncertainty to discourage exploitation of unreliable regions. Planning-based approaches such as MuZero \\citep{schrittwieser2020muzero} and EfficientZero \\citep{ye2021efficientzero} use learned models for tree search rather than imagination rollouts for policy improvement, and thus do not exhibit the temporal-conditioning failure mode we diagnose. An orthogonal line of work avoids imagination-based training altogether: TD-MPC2 \\citep{hansen2024tdmpc2} performs online model-predictive control at test time, sidestepping the need for imagination-trained value functions. Our work operates squarely within the DreamerV3 imagination-based training paradigm and diagnoses a specific form of model exploitation—value overestimation triggered by temporal conditioning—that prior model exploitation analyses have not identified.\n\n## 2.2 Temporal Abstraction in Reinforcement Learning\n\nTemporal abstraction—the ability to reason and act at multiple timescales—has been a long-standing goal in RL. The options framework \\citep{sutton1999options} formalizes temporally extended actions as option policies with initiation sets and termination conditions, operating at the semi-MDP level. In the model-free setting, several methods learn variable action persistence: FiGAR \\citep{sharma2017figar} augments the action space with a discrete repeat count, \\citet{lakshminarayanan2017dynamic} learn per-step repetition durations, and TempoRL \\citep{biedenkapp2021temporl} trains a skip-policy that achieves up to 10$\\times$ speedup on control tasks. These model-free approaches avoid the failure mode we identify because they do not train value functions on imagined rollouts with variable temporal granularity.\n\nWithin world-model RL, temporal abstraction has been pursued primarily through \\emph{hierarchical} architectures. Director \\citep{hafner2022director} introduces subgoal-conditioned planning in the Dreamer latent space. THICK \\citep{gumbsch2024thick} learns adaptive temporal abstractions via context-change detection, constructing a hierarchy of latent dynamics models. Hieros \\citep{mattes2024hieros} builds multi-scale hierarchical imagination with S5 world models. LS-Imagine \\citep{li2025lsimagine} extends the effective imagination horizon via goal-conditioned jumpy state transitions. These hierarchical methods sidestep the single-scale variable-$dt$ approach we investigate, and our diagnostic results provide a mechanistic explanation for why hierarchy may be preferable: flat $dt$-embedding conditioning introduces delusional critic dynamics that hierarchical decomposition avoids.\n\nMost relevant to our work is TAWM \\citep{nhu2025tawm}, which explicitly conditions a world model on time-step size $\\Delta t$ and trains over diverse $\\Delta t$ values for multi-rate dynamics learning. TAWM demonstrates that $\\Delta t$ conditioning \\emph{improves} performance and data efficiency—but critically, TAWM is built on TD-MPC2 and uses online model-predictive control, not imagination-based actor-critic training. Our work reveals that the same $\\Delta t$ conditioning that benefits MPC-based planning becomes pathological in imagination-based training: the critic exploits $dt$-conditioned value estimates from imprecise multi-step RSSM predictions, producing systematic overestimation. This paradigm-dependent asymmetry—beneficial in MPC, harmful in imagination-based actor-critic—is a central finding of our diagnostic analysis.\n\nThe sensitivity of RL algorithms to time discretization has been studied theoretically: \\citet{tallec2019making} show that Q-learning performance is highly sensitive to the discretization interval $\\delta$ and propose architectural modifications for $\\delta$-invariance. SAR \\citep{park2021sar} achieves time-discretization-invariant action repetition in model-free policy gradient methods. MTS3 \\citep{shaj2023mts3} proposes a probabilistic multi-time-scale state space model for variable-rate prediction. Our work demonstrates that world-model RL currently lacks this robustness: RSSM predictions trained at $\\delta\\!=\\!1$ degrade substantially at $dt\\!>\\!1$, and temporal conditioning amplifies rather than compensates for this degradation.\n\n## 2.3 Value Overestimation and Delusional Bias\n\nValue overestimation in deep RL was first identified by \\citet{thrun1993issues}, who showed that function approximation introduces systematic upward bias through the max operator in Q-learning. Double Q-learning \\citep{vanhasselt2016double} addresses this by decoupling action selection from value estimation, and TD3 \\citep{fujimoto2018td3} extends the idea to continuous control with clipped double critics. Ensemble methods such as SUNRISE \\citep{lee2021sunrise} use uncertainty-weighted value estimation to further suppress overestimation. DreamerV3 uses a single critic trained via categorical cross-entropy with symlog normalization \\citep{hafner2023dreamerv3}, which provides some implicit regularization against overestimation \\citep{farebrother2024stopregressing} but, as we show, is insufficient to prevent $dt$-embedding-induced value exploitation.\n\nDistinct from general overestimation, \\citet{lu2018nondelusional} formalize \\emph{delusional bias}: inconsistencies arising when Q-value backups assume policies that lie outside the representable policy class, producing value estimates that no realizable policy can achieve. \\citet{su2020conqur} extend this with consistency-penalized Q-labels. Our work identifies an analogous phenomenon in a fundamentally different setting. Where Lu et al.'s delusional bias arises from policy-class constraints in tabular or function-approximation Q-learning, our \\emph{delusional critic} arises from temporal conditioning in world-model imagination: the critic learns precise $dt$-conditioned value estimates, but the RSSM's prediction fidelity at $dt\\!>\\!1$ is insufficient to support this precision. The result is systematic overestimation of imagined trajectories at longer temporal steps—a form of delusion specific to the interaction between temporal conditioning and model-based imagination, not to function approximation per se.\n\nRecent work has connected value overestimation to training dynamics in model-based settings. \\citet{hussing2024dissecting} show that high update-to-data ratios drive value divergence through optimizer momentum, with overestimation occurring on both in-distribution and out-of-distribution data. \\citet{voelcker2025madtd} address value misgeneralization from replay distribution mismatch using model-generated data. Our delusional critic mechanism is complementary: the overestimation we identify is not driven by update ratios or distribution mismatch, but by the critic's ability to exploit temporally conditioned predictions from an imprecise world model.\n\n## 2.4 Multi-Step Prediction and Compounding Error\n\nCompounding prediction error is a fundamental challenge in model-based RL: small per-step model inaccuracies accumulate over multi-step rollouts, producing trajectories that diverge from ground truth. \\citet{venkatraman2015improving} establish theoretical guarantees relating single-step training error to multi-step prediction error via the Data-as-Demonstrator framework. \\citet{asadi2019combating} propose multi-step models that predict several steps ahead in a single forward pass to bypass the sequential error accumulation of autoregressive rollouts. \\citet{ke2019learning} incorporate long-term future information into dynamics learning via latent-variable autoregressive models. \\citet{lambert2022investigating} provide a systematic empirical study of how compounding error properties vary across model architectures and training procedures.\n\nRecent work has examined the downstream consequences of rollout quality degradation. \\citet{frauenknecht2025rollouts} show that trajectory-sampling rollouts diverge from ground truth after only a few steps and can actively harm policy learning, proposing uncertainty-based rollout termination as a mitigation. \\citet{barkley2024stealing} demonstrate that synthetic rollouts degrade performance inconsistently across environments, with overestimation bias as a contributing factor.\n\nOur findings add a new dimension to this literature. When imagination operates at $dt\\!>\\!1$, the RSSM must predict further into the future per step, amplifying compounding error: we observe observation prediction MSE increasing from a $2.04\\times$ gap (dt=1 vs.\\ dt=2) at baseline to substantially degraded absolute accuracy in collapsed configurations. However, compounding error alone does not explain the catastrophic collapse we observe. Our controlled experiments show that configurations with identical compounding error exposure (same $dt$, same horizon) produce qualitatively different outcomes depending on whether the $dt$-embedding is trained: untrained $dt$-embedding yields stable learning despite degraded prediction quality, while trained $dt$-embedding triggers accelerating value overestimation and collapse. The root cause is not prediction error per se, but the critic's exploitation of precise temporal conditioning built on imprecise predictions—a failure mode that compounds \\emph{on top of} the standard compounding error problem.\n\n---\n\n**Overall positioning.** Temporal abstraction in world-model RL sits at the intersection of four well-studied areas: world-model architecture, temporal abstraction methods, value overestimation, and multi-step prediction error. Yet the specific interaction between temporal conditioning and imagination-based actor-critic training has received virtually no attention. Existing temporal abstraction methods operate in model-free or MPC settings where the failure mode we identify does not arise; existing analyses of value overestimation and compounding error do not consider temporal conditioning as a causal factor. Our work fills this gap by providing the first systematic diagnosis of why variable-rate imagination fails in DreamerV3, identifying trained $dt$-embedding as the mechanism that bridges imprecise multi-step predictions to pathological value overestimation, and offering a practical mitigation: restricting imagination to $dt\\!=\\!1$ during multi-$dt$ training, where preliminary results show near-baseline recovery (95\\% in initial seed) without any architectural modification.\n",
    "structuredPatch": [
      {
        "oldStart": 10,
        "oldLines": 7,
        "newStart": 10,
        "newLines": 7,
        "lines": [
          " ",
          " Temporal abstraction—the ability to reason and act at multiple timescales—has been a long-standing goal in RL. The options framework \\citep{sutton1999options} formalizes temporally extended actions as option policies with initiation sets and termination conditions, operating at the semi-MDP level. In the model-free setting, several methods learn variable action persistence: FiGAR \\citep{sharma2017figar} augments the action space with a discrete repeat count, \\citet{lakshminarayanan2017dynamic} learn per-step repetition durations, and TempoRL \\citep{biedenkapp2021temporl} trains a skip-policy that achieves up to 10$\\times$ speedup on control tasks. These model-free approaches avoid the failure mode we identify because they do not train value functions on imagined rollouts with variable temporal granularity.",
          " ",
          "-Within world-model RL, temporal abstraction has been pursued primarily through \\emph{hierarchical} architectures. Director \\citep{hafner2022director} introduces subgoal-conditioned planning in the Dreamer latent space. THICK \\citep{gumbsch2024thick} learns adaptive temporal abstractions via context-change detection, constructing a hierarchy of latent dynamics models. Hieros \\citep{mattes2024hieros} builds multi-scale hierarchical imagination with S5 world models. LS-Imagine \\citep{li2025lsimagine} extends the effective imagination horizon via goal-conditioned jumpy state transitions. These hierarchical methods sidestep the single-scale variable-$dt$ approach we investigate, and our diagnostic results provide a mechanistic explanation for why hierarchy may be preferable: flat $dt$-embedding conditioning introduces delusional critic dynamics that hierarchical decomposition avoids.",
          "+Within world-model RL, temporal abstraction has been pursued primarily through \\emph{hierarchical} architectures. Director \\citep{hafner2022director} introduces subgoal-conditioned planning in the Dreamer latent space. THICK \\citep{gumbsch2024thick} learns adaptive temporal abstractions via context-change detection, constructing a hierarchy of latent dynamics models. Hieros \\citep{mattes2024hieros} builds multi-scale hierarchical imagination with S5 world models. LS-Imagine \\citep{li2025lsimagine} extends the effective imagination horizon via goal-conditioned jumpy state transitions. These hierarchical methods sidestep the single-scale variable-$dt$ approach we investigate. Hierarchical approaches may avoid the delusional critic phenomenon by operating at fixed temporal granularities within each level, though we do not test this hypothesis.",
          " ",
          " Most relevant to our work is TAWM \\citep{nhu2025tawm}, which explicitly conditions a world model on time-step size $\\Delta t$ and trains over diverse $\\Delta t$ values for multi-rate dynamics learning. TAWM demonstrates that $\\Delta t$ conditioning \\emph{improves} performance and data efficiency—but critically, TAWM is built on TD-MPC2 and uses online model-predictive control, not imagination-based actor-critic training. Our work reveals that the same $\\Delta t$ conditioning that benefits MPC-based planning becomes pathological in imagination-based training: the critic exploits $dt$-conditioned value estimates from imprecise multi-step RSSM predictions, producing systematic overestimation. This paradigm-dependent asymmetry—beneficial in MPC, harmful in imagination-based actor-critic—is a central finding of our diagnostic analysis.",
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

_source line 17_

**Item 3**: Adding ensemble/pessimistic inapplicability explanation at end of Section 2.3.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6f05e234-65d5-4fab-b46e-1cc055fade54",
  "uuid": "d2f260bc-3b5a-42c7-91ad-75cc8e832028",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ZqiVXE6fJbn63LzKq4swA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 341,
      "cache_read_input_tokens": 27913,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 341
      },
      "output_tokens": 4,
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

_source line 18_

<details open><summary>🔧 Tool call — Edit · `toolu_01Ebxq6TrVztkGLxLrWgee5f`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/paper_drafts/related_work_draft.md",
  "old_string": "Our delusional critic mechanism is complementary: the overestimation we identify is not driven by update ratios or distribution mismatch, but by the critic's ability to exploit temporally conditioned predictions from an imprecise world model.\n\n## 2.4",
  "new_string": "Our delusional critic mechanism is complementary: the overestimation we identify is not driven by update ratios or distribution mismatch, but by the critic's ability to exploit temporally conditioned predictions from an imprecise world model. Crucially, the overestimation we identify arises from temporal conditioning on imprecise multi-step predictions rather than function approximation noise, rendering ensemble-based or pessimistic corrections insufficient as they target a different source of error.\n\n## 2.4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6f05e234-65d5-4fab-b46e-1cc055fade54",
  "uuid": "b708c65d-e7a9-468b-8839-170abe6e7613",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ZqiVXE6fJbn63LzKq4swA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 341,
      "cache_read_input_tokens": 27913,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 341
      },
      "output_tokens": 4,
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

_source line 19 · 2026-05-15T04:49:43.271Z_

<details><summary>↩ Tool result · `toolu_01Ebxq6TrVztkGLxLrWgee5f`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/paper_drafts/related_work_draft.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6f05e234-65d5-4fab-b46e-1cc055fade54",
  "uuid": "694d647f-590c-4457-940a-da75b10f668b",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/paper_drafts/related_work_draft.md",
    "oldString": "Our delusional critic mechanism is complementary: the overestimation we identify is not driven by update ratios or distribution mismatch, but by the critic's ability to exploit temporally conditioned predictions from an imprecise world model.\n\n## 2.4",
    "newString": "Our delusional critic mechanism is complementary: the overestimation we identify is not driven by update ratios or distribution mismatch, but by the critic's ability to exploit temporally conditioned predictions from an imprecise world model. Crucially, the overestimation we identify arises from temporal conditioning on imprecise multi-step predictions rather than function approximation noise, rendering ensemble-based or pessimistic corrections insufficient as they target a different source of error.\n\n## 2.4",
    "originalFile": "# Related Work — Draft\n\n## 2.1 World-Model Reinforcement Learning\n\nWorld-model reinforcement learning trains agents by learning a predictive model of environment dynamics and using it to generate synthetic experience for policy optimization. The Dreamer family of algorithms \\citep{hafner2020dreamerv1, hafner2021dreamerv2, hafner2023dreamerv3} epitomizes this paradigm: a recurrent state-space model (RSSM) learns latent dynamics from interaction data, and an actor-critic pair is trained entirely within the model's imagined rollouts. DreamerV3 \\citep{hafner2023dreamerv3} introduced symlog normalization and discrete latent representations that enable a single set of hyperparameters to master diverse domains, establishing it as the dominant imagination-based architecture. More recently, DreamerV4 \\citep{hafner2025dreamerv4} replaces RSSM with a transformer world model, demonstrating scalability to video pretraining, though the core imagination-based training paradigm remains unchanged.\n\nA well-known risk in model-based RL is \\emph{model exploitation}: the policy optimizer can discover and exploit inaccuracies in the learned model, producing policies that perform well in imagination but fail in the real environment. \\citet{janner2019mbpo} formalize this concern and propose short-horizon branched rollouts to limit exploitation. Pessimistic approaches such as MOPO \\citep{yu2020mopo} penalize reward by model uncertainty to discourage exploitation of unreliable regions. Planning-based approaches such as MuZero \\citep{schrittwieser2020muzero} and EfficientZero \\citep{ye2021efficientzero} use learned models for tree search rather than imagination rollouts for policy improvement, and thus do not exhibit the temporal-conditioning failure mode we diagnose. An orthogonal line of work avoids imagination-based training altogether: TD-MPC2 \\citep{hansen2024tdmpc2} performs online model-predictive control at test time, sidestepping the need for imagination-trained value functions. Our work operates squarely within the DreamerV3 imagination-based training paradigm and diagnoses a specific form of model exploitation—value overestimation triggered by temporal conditioning—that prior model exploitation analyses have not identified.\n\n## 2.2 Temporal Abstraction in Reinforcement Learning\n\nTemporal abstraction—the ability to reason and act at multiple timescales—has been a long-standing goal in RL. The options framework \\citep{sutton1999options} formalizes temporally extended actions as option policies with initiation sets and termination conditions, operating at the semi-MDP level. In the model-free setting, several methods learn variable action persistence: FiGAR \\citep{sharma2017figar} augments the action space with a discrete repeat count, \\citet{lakshminarayanan2017dynamic} learn per-step repetition durations, and TempoRL \\citep{biedenkapp2021temporl} trains a skip-policy that achieves up to 10$\\times$ speedup on control tasks. These model-free approaches avoid the failure mode we identify because they do not train value functions on imagined rollouts with variable temporal granularity.\n\nWithin world-model RL, temporal abstraction has been pursued primarily through \\emph{hierarchical} architectures. Director \\citep{hafner2022director} introduces subgoal-conditioned planning in the Dreamer latent space. THICK \\citep{gumbsch2024thick} learns adaptive temporal abstractions via context-change detection, constructing a hierarchy of latent dynamics models. Hieros \\citep{mattes2024hieros} builds multi-scale hierarchical imagination with S5 world models. LS-Imagine \\citep{li2025lsimagine} extends the effective imagination horizon via goal-conditioned jumpy state transitions. These hierarchical methods sidestep the single-scale variable-$dt$ approach we investigate. Hierarchical approaches may avoid the delusional critic phenomenon by operating at fixed temporal granularities within each level, though we do not test this hypothesis.\n\nMost relevant to our work is TAWM \\citep{nhu2025tawm}, which explicitly conditions a world model on time-step size $\\Delta t$ and trains over diverse $\\Delta t$ values for multi-rate dynamics learning. TAWM demonstrates that $\\Delta t$ conditioning \\emph{improves} performance and data efficiency—but critically, TAWM is built on TD-MPC2 and uses online model-predictive control, not imagination-based actor-critic training. Our work reveals that the same $\\Delta t$ conditioning that benefits MPC-based planning becomes pathological in imagination-based training: the critic exploits $dt$-conditioned value estimates from imprecise multi-step RSSM predictions, producing systematic overestimation. This paradigm-dependent asymmetry—beneficial in MPC, harmful in imagination-based actor-critic—is a central finding of our diagnostic analysis.\n\nThe sensitivity of RL algorithms to time discretization has been studied theoretically: \\citet{tallec2019making} show that Q-learning performance is highly sensitive to the discretization interval $\\delta$ and propose architectural modifications for $\\delta$-invariance. SAR \\citep{park2021sar} achieves time-discretization-invariant action repetition in model-free policy gradient methods. MTS3 \\citep{shaj2023mts3} proposes a probabilistic multi-time-scale state space model for variable-rate prediction. Our work demonstrates that world-model RL currently lacks this robustness: RSSM predictions trained at $\\delta\\!=\\!1$ degrade substantially at $dt\\!>\\!1$, and temporal conditioning amplifies rather than compensates for this degradation.\n\n## 2.3 Value Overestimation and Delusional Bias\n\nValue overestimation in deep RL was first identified by \\citet{thrun1993issues}, who showed that function approximation introduces systematic upward bias through the max operator in Q-learning. Double Q-learning \\citep{vanhasselt2016double} addresses this by decoupling action selection from value estimation, and TD3 \\citep{fujimoto2018td3} extends the idea to continuous control with clipped double critics. Ensemble methods such as SUNRISE \\citep{lee2021sunrise} use uncertainty-weighted value estimation to further suppress overestimation. DreamerV3 uses a single critic trained via categorical cross-entropy with symlog normalization \\citep{hafner2023dreamerv3}, which provides some implicit regularization against overestimation \\citep{farebrother2024stopregressing} but, as we show, is insufficient to prevent $dt$-embedding-induced value exploitation.\n\nDistinct from general overestimation, \\citet{lu2018nondelusional} formalize \\emph{delusional bias}: inconsistencies arising when Q-value backups assume policies that lie outside the representable policy class, producing value estimates that no realizable policy can achieve. \\citet{su2020conqur} extend this with consistency-penalized Q-labels. Our work identifies an analogous phenomenon in a fundamentally different setting. Where Lu et al.'s delusional bias arises from policy-class constraints in tabular or function-approximation Q-learning, our \\emph{delusional critic} arises from temporal conditioning in world-model imagination: the critic learns precise $dt$-conditioned value estimates, but the RSSM's prediction fidelity at $dt\\!>\\!1$ is insufficient to support this precision. The result is systematic overestimation of imagined trajectories at longer temporal steps—a form of delusion specific to the interaction between temporal conditioning and model-based imagination, not to function approximation per se.\n\nRecent work has connected value overestimation to training dynamics in model-based settings. \\citet{hussing2024dissecting} show that high update-to-data ratios drive value divergence through optimizer momentum, with overestimation occurring on both in-distribution and out-of-distribution data. \\citet{voelcker2025madtd} address value misgeneralization from replay distribution mismatch using model-generated data. Our delusional critic mechanism is complementary: the overestimation we identify is not driven by update ratios or distribution mismatch, but by the critic's ability to exploit temporally conditioned predictions from an imprecise world model.\n\n## 2.4 Multi-Step Prediction and Compounding Error\n\nCompounding prediction error is a fundamental challenge in model-based RL: small per-step model inaccuracies accumulate over multi-step rollouts, producing trajectories that diverge from ground truth. \\citet{venkatraman2015improving} establish theoretical guarantees relating single-step training error to multi-step prediction error via the Data-as-Demonstrator framework. \\citet{asadi2019combating} propose multi-step models that predict several steps ahead in a single forward pass to bypass the sequential error accumulation of autoregressive rollouts. \\citet{ke2019learning} incorporate long-term future information into dynamics learning via latent-variable autoregressive models. \\citet{lambert2022investigating} provide a systematic empirical study of how compounding error properties vary across model architectures and training procedures.\n\nRecent work has examined the downstream consequences of rollout quality degradation. \\citet{frauenknecht2025rollouts} show that trajectory-sampling rollouts diverge from ground truth after only a few steps and can actively harm policy learning, proposing uncertainty-based rollout termination as a mitigation. \\citet{barkley2024stealing} demonstrate that synthetic rollouts degrade performance inconsistently across environments, with overestimation bias as a contributing factor.\n\nOur findings add a new dimension to this literature. When imagination operates at $dt\\!>\\!1$, the RSSM must predict further into the future per step, amplifying compounding error: we observe observation prediction MSE increasing from a $2.04\\times$ gap (dt=1 vs.\\ dt=2) at baseline to substantially degraded absolute accuracy in collapsed configurations. However, compounding error alone does not explain the catastrophic collapse we observe. Our controlled experiments show that configurations with identical compounding error exposure (same $dt$, same horizon) produce qualitatively different outcomes depending on whether the $dt$-embedding is trained: untrained $dt$-embedding yields stable learning despite degraded prediction quality, while trained $dt$-embedding triggers accelerating value overestimation and collapse. The root cause is not prediction error per se, but the critic's exploitation of precise temporal conditioning built on imprecise predictions—a failure mode that compounds \\emph{on top of} the standard compounding error problem.\n\n---\n\n**Overall positioning.** Temporal abstraction in world-model RL sits at the intersection of four well-studied areas: world-model architecture, temporal abstraction methods, value overestimation, and multi-step prediction error. Yet the specific interaction between temporal conditioning and imagination-based actor-critic training has received virtually no attention. Existing temporal abstraction methods operate in model-free or MPC settings where the failure mode we identify does not arise; existing analyses of value overestimation and compounding error do not consider temporal conditioning as a causal factor. Our work fills this gap by providing the first systematic diagnosis of why variable-rate imagination fails in DreamerV3, identifying trained $dt$-embedding as the mechanism that bridges imprecise multi-step predictions to pathological value overestimation, and offering a practical mitigation: restricting imagination to $dt\\!=\\!1$ during multi-$dt$ training, where preliminary results show near-baseline recovery (95\\% in initial seed) without any architectural modification.\n",
    "structuredPatch": [
      {
        "oldStart": 22,
        "oldLines": 7,
        "newStart": 22,
        "newLines": 7,
        "lines": [
          " ",
          " Distinct from general overestimation, \\citet{lu2018nondelusional} formalize \\emph{delusional bias}: inconsistencies arising when Q-value backups assume policies that lie outside the representable policy class, producing value estimates that no realizable policy can achieve. \\citet{su2020conqur} extend this with consistency-penalized Q-labels. Our work identifies an analogous phenomenon in a fundamentally different setting. Where Lu et al.'s delusional bias arises from policy-class constraints in tabular or function-approximation Q-learning, our \\emph{delusional critic} arises from temporal conditioning in world-model imagination: the critic learns precise $dt$-conditioned value estimates, but the RSSM's prediction fidelity at $dt\\!>\\!1$ is insufficient to support this precision. The result is systematic overestimation of imagined trajectories at longer temporal steps—a form of delusion specific to the interaction between temporal conditioning and model-based imagination, not to function approximation per se.",
          " ",
          "-Recent work has connected value overestimation to training dynamics in model-based settings. \\citet{hussing2024dissecting} show that high update-to-data ratios drive value divergence through optimizer momentum, with overestimation occurring on both in-distribution and out-of-distribution data. \\citet{voelcker2025madtd} address value misgeneralization from replay distribution mismatch using model-generated data. Our delusional critic mechanism is complementary: the overestimation we identify is not driven by update ratios or distribution mismatch, but by the critic's ability to exploit temporally conditioned predictions from an imprecise world model.",
          "+Recent work has connected value overestimation to training dynamics in model-based settings. \\citet{hussing2024dissecting} show that high update-to-data ratios drive value divergence through optimizer momentum, with overestimation occurring on both in-distribution and out-of-distribution data. \\citet{voelcker2025madtd} address value misgeneralization from replay distribution mismatch using model-generated data. Our delusional critic mechanism is complementary: the overestimation we identify is not driven by update ratios or distribution mismatch, but by the critic's ability to exploit temporally conditioned predictions from an imprecise world model. Crucially, the overestimation we identify arises from temporal conditioning on imprecise multi-step predictions rather than function approximation noise, rendering ensemble-based or pessimistic corrections insufficient as they target a different source of error.",
          " ",
          " ## 2.4 Multi-Step Prediction and Compounding Error",
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

_source line 20_

**Item 7**: Trimming Section 2.4 — removing value overestimation overlap with 2.3.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6f05e234-65d5-4fab-b46e-1cc055fade54",
  "uuid": "e281a8ef-dc9c-422d-8626-8442ac36f7cb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PwmzF46e9e9KL85MWyLyei",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 509,
      "cache_read_input_tokens": 28254,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 509
      },
      "output_tokens": 4,
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

_source line 21_

<details open><summary>🔧 Tool call — Edit · `toolu_01GzouwbvCacvZ5EX4TNDrzZ`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/paper_drafts/related_work_draft.md",
  "old_string": "Compounding prediction error is a fundamental challenge in model-based RL: small per-step model inaccuracies accumulate over multi-step rollouts, producing trajectories that diverge from ground truth. \\citet{venkatraman2015improving} establish theoretical guarantees relating single-step training error to multi-step prediction error via the Data-as-Demonstrator framework. \\citet{asadi2019combating} propose multi-step models that predict several steps ahead in a single forward pass to bypass the sequential error accumulation of autoregressive rollouts. \\citet{ke2019learning} incorporate long-term future information into dynamics learning via latent-variable autoregressive models. \\citet{lambert2022investigating} provide a systematic empirical study of how compounding error properties vary across model architectures and training procedures.\n\nRecent work has examined the downstream consequences of rollout quality degradation. \\citet{frauenknecht2025rollouts} show that trajectory-sampling rollouts diverge from ground truth after only a few steps and can actively harm policy learning, proposing uncertainty-based rollout termination as a mitigation. \\citet{barkley2024stealing} demonstrate that synthetic rollouts degrade performance inconsistently across environments, with overestimation bias as a contributing factor.\n\nOur findings add a new dimension to this literature. When imagination operates at $dt\\!>\\!1$, the RSSM must predict further into the future per step, amplifying compounding error: we observe observation prediction MSE increasing from a $2.04\\times$ gap (dt=1 vs.\\ dt=2) at baseline to substantially degraded absolute accuracy in collapsed configurations. However, compounding error alone does not explain the catastrophic collapse we observe. Our controlled experiments show that configurations with identical compounding error exposure (same $dt$, same horizon) produce qualitatively different outcomes depending on whether the $dt$-embedding is trained: untrained $dt$-embedding yields stable learning despite degraded prediction quality, while trained $dt$-embedding triggers accelerating value overestimation and collapse. The root cause is not prediction error per se, but the critic's exploitation of precise temporal conditioning built on imprecise predictions—a failure mode that compounds \\emph{on top of} the standard compounding error problem.",
  "new_string": "Compounding prediction error is a fundamental challenge in model-based RL: small per-step model inaccuracies accumulate over multi-step rollouts, producing trajectories that diverge from ground truth \\citep{venkatraman2015improving, lambert2022investigating}. \\citet{asadi2019combating} propose multi-step models that predict several steps ahead in a single forward pass to bypass sequential error accumulation. \\citet{frauenknecht2025rollouts} show that trajectory-sampling rollouts can diverge from ground truth after only a few steps and actively harm policy learning.\n\nOur findings add a new dimension: when imagination operates at $dt\\!>\\!1$, the RSSM must predict further into the future per step, amplifying compounding error. However, compounding error alone does not explain the catastrophic collapse we observe. Configurations with identical compounding error exposure (same $dt$, same horizon) produce qualitatively different outcomes depending on whether the $dt$-embedding is trained: untrained $dt$-embedding yields stable learning despite degraded prediction quality, while trained $dt$-embedding triggers collapse. The root cause is the critic's exploitation of precise temporal conditioning built on imprecise predictions (see Section~2.3)—a failure mode that compounds \\emph{on top of} the standard compounding error problem."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6f05e234-65d5-4fab-b46e-1cc055fade54",
  "uuid": "e41ab93f-9e3d-415d-a74d-d573be91f32a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PwmzF46e9e9KL85MWyLyei",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 509,
      "cache_read_input_tokens": 28254,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 509
      },
      "output_tokens": 4,
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

_source line 22 · 2026-05-15T04:50:09.377Z_

<details><summary>↩ Tool result · `toolu_01GzouwbvCacvZ5EX4TNDrzZ`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/paper_drafts/related_work_draft.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6f05e234-65d5-4fab-b46e-1cc055fade54",
  "uuid": "8374d8f2-0834-4993-a393-3e8ef950cd5f",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/paper_drafts/related_work_draft.md",
    "oldString": "Compounding prediction error is a fundamental challenge in model-based RL: small per-step model inaccuracies accumulate over multi-step rollouts, producing trajectories that diverge from ground truth. \\citet{venkatraman2015improving} establish theoretical guarantees relating single-step training error to multi-step prediction error via the Data-as-Demonstrator framework. \\citet{asadi2019combating} propose multi-step models that predict several steps ahead in a single forward pass to bypass the sequential error accumulation of autoregressive rollouts. \\citet{ke2019learning} incorporate long-term future information into dynamics learning via latent-variable autoregressive models. \\citet{lambert2022investigating} provide a systematic empirical study of how compounding error properties vary across model architectures and training procedures.\n\nRecent work has examined the downstream consequences of rollout quality degradation. \\citet{frauenknecht2025rollouts} show that trajectory-sampling rollouts diverge from ground truth after only a few steps and can actively harm policy learning, proposing uncertainty-based rollout termination as a mitigation. \\citet{barkley2024stealing} demonstrate that synthetic rollouts degrade performance inconsistently across environments, with overestimation bias as a contributing factor.\n\nOur findings add a new dimension to this literature. When imagination operates at $dt\\!>\\!1$, the RSSM must predict further into the future per step, amplifying compounding error: we observe observation prediction MSE increasing from a $2.04\\times$ gap (dt=1 vs.\\ dt=2) at baseline to substantially degraded absolute accuracy in collapsed configurations. However, compounding error alone does not explain the catastrophic collapse we observe. Our controlled experiments show that configurations with identical compounding error exposure (same $dt$, same horizon) produce qualitatively different outcomes depending on whether the $dt$-embedding is trained: untrained $dt$-embedding yields stable learning despite degraded prediction quality, while trained $dt$-embedding triggers accelerating value overestimation and collapse. The root cause is not prediction error per se, but the critic's exploitation of precise temporal conditioning built on imprecise predictions—a failure mode that compounds \\emph{on top of} the standard compounding error problem.",
    "newString": "Compounding prediction error is a fundamental challenge in model-based RL: small per-step model inaccuracies accumulate over multi-step rollouts, producing trajectories that diverge from ground truth \\citep{venkatraman2015improving, lambert2022investigating}. \\citet{asadi2019combating} propose multi-step models that predict several steps ahead in a single forward pass to bypass sequential error accumulation. \\citet{frauenknecht2025rollouts} show that trajectory-sampling rollouts can diverge from ground truth after only a few steps and actively harm policy learning.\n\nOur findings add a new dimension: when imagination operates at $dt\\!>\\!1$, the RSSM must predict further into the future per step, amplifying compounding error. However, compounding error alone does not explain the catastrophic collapse we observe. Configurations with identical compounding error exposure (same $dt$, same horizon) produce qualitatively different outcomes depending on whether the $dt$-embedding is trained: untrained $dt$-embedding yields stable learning despite degraded prediction quality, while trained $dt$-embedding triggers collapse. The root cause is the critic's exploitation of precise temporal conditioning built on imprecise predictions (see Section~2.3)—a failure mode that compounds \\emph{on top of} the standard compounding error problem.",
    "originalFile": "# Related Work — Draft\n\n## 2.1 World-Model Reinforcement Learning\n\nWorld-model reinforcement learning trains agents by learning a predictive model of environment dynamics and using it to generate synthetic experience for policy optimization. The Dreamer family of algorithms \\citep{hafner2020dreamerv1, hafner2021dreamerv2, hafner2023dreamerv3} epitomizes this paradigm: a recurrent state-space model (RSSM) learns latent dynamics from interaction data, and an actor-critic pair is trained entirely within the model's imagined rollouts. DreamerV3 \\citep{hafner2023dreamerv3} introduced symlog normalization and discrete latent representations that enable a single set of hyperparameters to master diverse domains, establishing it as the dominant imagination-based architecture. More recently, DreamerV4 \\citep{hafner2025dreamerv4} replaces RSSM with a transformer world model, demonstrating scalability to video pretraining, though the core imagination-based training paradigm remains unchanged.\n\nA well-known risk in model-based RL is \\emph{model exploitation}: the policy optimizer can discover and exploit inaccuracies in the learned model, producing policies that perform well in imagination but fail in the real environment. \\citet{janner2019mbpo} formalize this concern and propose short-horizon branched rollouts to limit exploitation. Pessimistic approaches such as MOPO \\citep{yu2020mopo} penalize reward by model uncertainty to discourage exploitation of unreliable regions. Planning-based approaches such as MuZero \\citep{schrittwieser2020muzero} and EfficientZero \\citep{ye2021efficientzero} use learned models for tree search rather than imagination rollouts for policy improvement, and thus do not exhibit the temporal-conditioning failure mode we diagnose. An orthogonal line of work avoids imagination-based training altogether: TD-MPC2 \\citep{hansen2024tdmpc2} performs online model-predictive control at test time, sidestepping the need for imagination-trained value functions. Our work operates squarely within the DreamerV3 imagination-based training paradigm and diagnoses a specific form of model exploitation—value overestimation triggered by temporal conditioning—that prior model exploitation analyses have not identified.\n\n## 2.2 Temporal Abstraction in Reinforcement Learning\n\nTemporal abstraction—the ability to reason and act at multiple timescales—has been a long-standing goal in RL. The options framework \\citep{sutton1999options} formalizes temporally extended actions as option policies with initiation sets and termination conditions, operating at the semi-MDP level. In the model-free setting, several methods learn variable action persistence: FiGAR \\citep{sharma2017figar} augments the action space with a discrete repeat count, \\citet{lakshminarayanan2017dynamic} learn per-step repetition durations, and TempoRL \\citep{biedenkapp2021temporl} trains a skip-policy that achieves up to 10$\\times$ speedup on control tasks. These model-free approaches avoid the failure mode we identify because they do not train value functions on imagined rollouts with variable temporal granularity.\n\nWithin world-model RL, temporal abstraction has been pursued primarily through \\emph{hierarchical} architectures. Director \\citep{hafner2022director} introduces subgoal-conditioned planning in the Dreamer latent space. THICK \\citep{gumbsch2024thick} learns adaptive temporal abstractions via context-change detection, constructing a hierarchy of latent dynamics models. Hieros \\citep{mattes2024hieros} builds multi-scale hierarchical imagination with S5 world models. LS-Imagine \\citep{li2025lsimagine} extends the effective imagination horizon via goal-conditioned jumpy state transitions. These hierarchical methods sidestep the single-scale variable-$dt$ approach we investigate. Hierarchical approaches may avoid the delusional critic phenomenon by operating at fixed temporal granularities within each level, though we do not test this hypothesis.\n\nMost relevant to our work is TAWM \\citep{nhu2025tawm}, which explicitly conditions a world model on time-step size $\\Delta t$ and trains over diverse $\\Delta t$ values for multi-rate dynamics learning. TAWM demonstrates that $\\Delta t$ conditioning \\emph{improves} performance and data efficiency—but critically, TAWM is built on TD-MPC2 and uses online model-predictive control, not imagination-based actor-critic training. Our work reveals that the same $\\Delta t$ conditioning that benefits MPC-based planning becomes pathological in imagination-based training: the critic exploits $dt$-conditioned value estimates from imprecise multi-step RSSM predictions, producing systematic overestimation. This paradigm-dependent asymmetry—beneficial in MPC, harmful in imagination-based actor-critic—is a central finding of our diagnostic analysis.\n\nThe sensitivity of RL algorithms to time discretization has been studied theoretically: \\citet{tallec2019making} show that Q-learning performance is highly sensitive to the discretization interval $\\delta$ and propose architectural modifications for $\\delta$-invariance. SAR \\citep{park2021sar} achieves time-discretization-invariant action repetition in model-free policy gradient methods. MTS3 \\citep{shaj2023mts3} proposes a probabilistic multi-time-scale state space model for variable-rate prediction. Our work demonstrates that world-model RL currently lacks this robustness: RSSM predictions trained at $\\delta\\!=\\!1$ degrade substantially at $dt\\!>\\!1$, and temporal conditioning amplifies rather than compensates for this degradation.\n\n## 2.3 Value Overestimation and Delusional Bias\n\nValue overestimation in deep RL was first identified by \\citet{thrun1993issues}, who showed that function approximation introduces systematic upward bias through the max operator in Q-learning. Double Q-learning \\citep{vanhasselt2016double} addresses this by decoupling action selection from value estimation, and TD3 \\citep{fujimoto2018td3} extends the idea to continuous control with clipped double critics. Ensemble methods such as SUNRISE \\citep{lee2021sunrise} use uncertainty-weighted value estimation to further suppress overestimation. DreamerV3 uses a single critic trained via categorical cross-entropy with symlog normalization \\citep{hafner2023dreamerv3}, which provides some implicit regularization against overestimation \\citep{farebrother2024stopregressing} but, as we show, is insufficient to prevent $dt$-embedding-induced value exploitation.\n\nDistinct from general overestimation, \\citet{lu2018nondelusional} formalize \\emph{delusional bias}: inconsistencies arising when Q-value backups assume policies that lie outside the representable policy class, producing value estimates that no realizable policy can achieve. \\citet{su2020conqur} extend this with consistency-penalized Q-labels. Our work identifies an analogous phenomenon in a fundamentally different setting. Where Lu et al.'s delusional bias arises from policy-class constraints in tabular or function-approximation Q-learning, our \\emph{delusional critic} arises from temporal conditioning in world-model imagination: the critic learns precise $dt$-conditioned value estimates, but the RSSM's prediction fidelity at $dt\\!>\\!1$ is insufficient to support this precision. The result is systematic overestimation of imagined trajectories at longer temporal steps—a form of delusion specific to the interaction between temporal conditioning and model-based imagination, not to function approximation per se.\n\nRecent work has connected value overestimation to training dynamics in model-based settings. \\citet{hussing2024dissecting} show that high update-to-data ratios drive value divergence through optimizer momentum, with overestimation occurring on both in-distribution and out-of-distribution data. \\citet{voelcker2025madtd} address value misgeneralization from replay distribution mismatch using model-generated data. Our delusional critic mechanism is complementary: the overestimation we identify is not driven by update ratios or distribution mismatch, but by the critic's ability to exploit temporally conditioned predictions from an imprecise world model. Crucially, the overestimation we identify arises from temporal conditioning on imprecise multi-step predictions rather than function approximation noise, rendering ensemble-based or pessimistic corrections insufficient as they target a different source of error.\n\n## 2.4 Multi-Step Prediction and Compounding Error\n\nCompounding prediction error is a fundamental challenge in model-based RL: small per-step model inaccuracies accumulate over multi-step rollouts, producing trajectories that diverge from ground truth. \\citet{venkatraman2015improving} establish theoretical guarantees relating single-step training error to multi-step prediction error via the Data-as-Demonstrator framework. \\citet{asadi2019combating} propose multi-step models that predict several steps ahead in a single forward pass to bypass the sequential error accumulation of autoregressive rollouts. \\citet{ke2019learning} incorporate long-term future information into dynamics learning via latent-variable autoregressive models. \\citet{lambert2022investigating} provide a systematic empirical study of how compounding error properties vary across model architectures and training procedures.\n\nRecent work has examined the downstream consequences of rollout quality degradation. \\citet{frauenknecht2025rollouts} show that trajectory-sampling rollouts diverge from ground truth after only a few steps and can actively harm policy learning, proposing uncertainty-based rollout termination as a mitigation. \\citet{barkley2024stealing} demonstrate that synthetic rollouts degrade performance inconsistently across environments, with overestimation bias as a contributing factor.\n\nOur findings add a new dimension to this literature. When imagination operates at $dt\\!>\\!1$, the RSSM must predict further into the future per step, amplifying compounding error: we observe observation prediction MSE increasing from a $2.04\\times$ gap (dt=1 vs.\\ dt=2) at baseline to substantially degraded absolute accuracy in collapsed configurations. However, compounding error alone does not explain the catastrophic collapse we observe. Our controlled experiments show that configurations with identical compounding error exposure (same $dt$, same horizon) produce qualitatively different outcomes depending on whether the $dt$-embedding is trained: untrained $dt$-embedding yields stable learning despite degraded prediction quality, while trained $dt$-embedding triggers accelerating value overestimation and collapse. The root cause is not prediction error per se, but the critic's exploitation of precise temporal conditioning built on imprecise predictions—a failure mode that compounds \\emph{on top of} the standard compounding error problem.\n\n---\n\n**Overall positioning.** Temporal abstraction in world-model RL sits at the intersection of four well-studied areas: world-model architecture, temporal abstraction methods, value overestimation, and multi-step prediction error. Yet the specific interaction between temporal conditioning and imagination-based actor-critic training has received virtually no attention. Existing temporal abstraction methods operate in model-free or MPC settings where the failure mode we identify does not arise; existing analyses of value overestimation and compounding error do not consider temporal conditioning as a causal factor. Our work fills this gap by providing the first systematic diagnosis of why variable-rate imagination fails in DreamerV3, identifying trained $dt$-embedding as the mechanism that bridges imprecise multi-step predictions to pathological value overestimation, and offering a practical mitigation: restricting imagination to $dt\\!=\\!1$ during multi-$dt$ training, where preliminary results show near-baseline recovery (95\\% in initial seed) without any architectural modification.\n",
    "structuredPatch": [
      {
        "oldStart": 26,
        "oldLines": 12,
        "newStart": 26,
        "newLines": 10,
        "lines": [
          " ",
          " ## 2.4 Multi-Step Prediction and Compounding Error",
          " ",
          "-Compounding prediction error is a fundamental challenge in model-based RL: small per-step model inaccuracies accumulate over multi-step rollouts, producing trajectories that diverge from ground truth. \\citet{venkatraman2015improving} establish theoretical guarantees relating single-step training error to multi-step prediction error via the Data-as-Demonstrator framework. \\citet{asadi2019combating} propose multi-step models that predict several steps ahead in a single forward pass to bypass the sequential error accumulation of autoregressive rollouts. \\citet{ke2019learning} incorporate long-term future information into dynamics learning via latent-variable autoregressive models. \\citet{lambert2022investigating} provide a systematic empirical study of how compounding error properties vary across model architectures and training procedures.",
          "+Compounding prediction error is a fundamental challenge in model-based RL: small per-step model inaccuracies accumulate over multi-step rollouts, producing trajectories that diverge from ground truth \\citep{venkatraman2015improving, lambert2022investigating}. \\citet{asadi2019combating} propose multi-step models that predict several steps ahead in a single forward pass to bypass sequential error accumulation. \\citet{frauenknecht2025rollouts} show that trajectory-sampling rollouts can diverge from ground truth after only a few steps and actively harm policy learning.",
          " ",
          "-Recent work has examined the downstream consequences of rollout quality degradation. \\citet{frauenknecht2025rollouts} show that trajectory-sampling rollouts diverge from ground truth after only a few steps and can actively harm policy learning, proposing uncertainty-based rollout termination as a mitigation. \\citet{barkley2024stealing} demonstrate that synthetic rollouts degrade performance inconsistently across environments, with overestimation bias as a contributing factor.",
          "+Our findings add a new dimension: when imagination operates at $dt\\!>\\!1$, the RSSM must predict further into the future per step, amplifying compounding error. However, compounding error alone does not explain the catastrophic collapse we observe. Configurations with identical compounding error exposure (same $dt$, same horizon) produce qualitatively different outcomes depending on whether the $dt$-embedding is trained: untrained $dt$-embedding yields stable learning despite degraded prediction quality, while trained $dt$-embedding triggers collapse. The root cause is the critic's exploitation of precise temporal conditioning built on imprecise predictions (see Section~2.3)—a failure mode that compounds \\emph{on top of} the standard compounding error problem.",
          " ",
          "-Our findings add a new dimension to this literature. When imagination operates at $dt\\!>\\!1$, the RSSM must predict further into the future per step, amplifying compounding error: we observe observation prediction MSE increasing from a $2.04\\times$ gap (dt=1 vs.\\ dt=2) at baseline to substantially degraded absolute accuracy in collapsed configurations. However, compounding error alone does not explain the catastrophic collapse we observe. Our controlled experiments show that configurations with identical compounding error exposure (same $dt$, same horizon) produce qualitatively different outcomes depending on whether the $dt$-embedding is trained: untrained $dt$-embedding yields stable learning despite degraded prediction quality, while trained $dt$-embedding triggers accelerating value overestimation and collapse. The root cause is not prediction error per se, but the critic's exploitation of precise temporal conditioning built on imprecise predictions—a failure mode that compounds \\emph{on top of} the standard compounding error problem.",
          "-",
          " ---",
          " ",
          " **Overall positioning.** Temporal abstraction in world-model RL sits at the intersection of four well-studied areas: world-model architecture, temporal abstraction methods, value overestimation, and multi-step prediction error. Yet the specific interaction between temporal conditioning and imagination-based actor-critic training has received virtually no attention. Existing temporal abstraction methods operate in model-free or MPC settings where the failure mode we identify does not arise; existing analyses of value overestimation and compounding error do not consider temporal conditioning as a causal factor. Our work fills this gap by providing the first systematic diagnosis of why variable-rate imagination fails in DreamerV3, identifying trained $dt$-embedding as the mechanism that bridges imprecise multi-step predictions to pathological value overestimation, and offering a practical mitigation: restricting imagination to $dt\\!=\\!1$ during multi-$dt$ training, where preliminary results show near-baseline recovery (95\\% in initial seed) without any architectural modification."
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

_source line 23_

**Item 2**: Adding diagnostic methodology paragraph as new Section 2.5.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6f05e234-65d5-4fab-b46e-1cc055fade54",
  "uuid": "95094962-3e08-482b-9d47-6e94ddfe6a85",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018wpgvN2MFysnXie1BRhe9M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1045,
      "cache_read_input_tokens": 28763,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1045
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

_source line 24_

<details open><summary>🔧 Tool call — Edit · `toolu_01LkJ7EQHzK126F7XtuxN7xV`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/paper_drafts/related_work_draft.md",
  "old_string": "---\n\n**Overall positioning.**",
  "new_string": "## 2.5 Diagnostic Methodology\n\nOur diagnostic methodology follows a tradition of systematic controlled experiments in RL. \\citet{engstrom2020implementation} demonstrate that implementation-level details—code-level choices typically unreported in publications—can account for most of the performance gains attributed to algorithmic innovations in deep policy gradients. \\citet{andrychowicz2021matters} extend this approach to on-policy RL, systematically evaluating the impact of individual design choices through matched ablations. In the same spirit, our work isolates individual factors (temporal conditioning, imagination horizon, $dt$-embedding training) through controlled ablations within a single codebase, rather than proposing new algorithms. This diagnostic framing allows us to identify the precise mechanism—trained $dt$-embedding interacting with imprecise multi-step predictions—responsible for the observed failure mode.\n\n---\n\n**Overall positioning.**"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6f05e234-65d5-4fab-b46e-1cc055fade54",
  "uuid": "04cf5bc1-948f-48c2-ac79-53f70fcad19c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018wpgvN2MFysnXie1BRhe9M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1045,
      "cache_read_input_tokens": 28763,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1045
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

_source line 25 · 2026-05-15T04:50:22.100Z_

<details><summary>↩ Tool result · `toolu_01LkJ7EQHzK126F7XtuxN7xV`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/paper_drafts/related_work_draft.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6f05e234-65d5-4fab-b46e-1cc055fade54",
  "uuid": "6d77996e-d675-4413-8bf5-b3c3f99a8215",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/paper_drafts/related_work_draft.md",
    "oldString": "---\n\n**Overall positioning.**",
    "newString": "## 2.5 Diagnostic Methodology\n\nOur diagnostic methodology follows a tradition of systematic controlled experiments in RL. \\citet{engstrom2020implementation} demonstrate that implementation-level details—code-level choices typically unreported in publications—can account for most of the performance gains attributed to algorithmic innovations in deep policy gradients. \\citet{andrychowicz2021matters} extend this approach to on-policy RL, systematically evaluating the impact of individual design choices through matched ablations. In the same spirit, our work isolates individual factors (temporal conditioning, imagination horizon, $dt$-embedding training) through controlled ablations within a single codebase, rather than proposing new algorithms. This diagnostic framing allows us to identify the precise mechanism—trained $dt$-embedding interacting with imprecise multi-step predictions—responsible for the observed failure mode.\n\n---\n\n**Overall positioning.**",
    "originalFile": "# Related Work — Draft\n\n## 2.1 World-Model Reinforcement Learning\n\nWorld-model reinforcement learning trains agents by learning a predictive model of environment dynamics and using it to generate synthetic experience for policy optimization. The Dreamer family of algorithms \\citep{hafner2020dreamerv1, hafner2021dreamerv2, hafner2023dreamerv3} epitomizes this paradigm: a recurrent state-space model (RSSM) learns latent dynamics from interaction data, and an actor-critic pair is trained entirely within the model's imagined rollouts. DreamerV3 \\citep{hafner2023dreamerv3} introduced symlog normalization and discrete latent representations that enable a single set of hyperparameters to master diverse domains, establishing it as the dominant imagination-based architecture. More recently, DreamerV4 \\citep{hafner2025dreamerv4} replaces RSSM with a transformer world model, demonstrating scalability to video pretraining, though the core imagination-based training paradigm remains unchanged.\n\nA well-known risk in model-based RL is \\emph{model exploitation}: the policy optimizer can discover and exploit inaccuracies in the learned model, producing policies that perform well in imagination but fail in the real environment. \\citet{janner2019mbpo} formalize this concern and propose short-horizon branched rollouts to limit exploitation. Pessimistic approaches such as MOPO \\citep{yu2020mopo} penalize reward by model uncertainty to discourage exploitation of unreliable regions. Planning-based approaches such as MuZero \\citep{schrittwieser2020muzero} and EfficientZero \\citep{ye2021efficientzero} use learned models for tree search rather than imagination rollouts for policy improvement, and thus do not exhibit the temporal-conditioning failure mode we diagnose. An orthogonal line of work avoids imagination-based training altogether: TD-MPC2 \\citep{hansen2024tdmpc2} performs online model-predictive control at test time, sidestepping the need for imagination-trained value functions. Our work operates squarely within the DreamerV3 imagination-based training paradigm and diagnoses a specific form of model exploitation—value overestimation triggered by temporal conditioning—that prior model exploitation analyses have not identified.\n\n## 2.2 Temporal Abstraction in Reinforcement Learning\n\nTemporal abstraction—the ability to reason and act at multiple timescales—has been a long-standing goal in RL. The options framework \\citep{sutton1999options} formalizes temporally extended actions as option policies with initiation sets and termination conditions, operating at the semi-MDP level. In the model-free setting, several methods learn variable action persistence: FiGAR \\citep{sharma2017figar} augments the action space with a discrete repeat count, \\citet{lakshminarayanan2017dynamic} learn per-step repetition durations, and TempoRL \\citep{biedenkapp2021temporl} trains a skip-policy that achieves up to 10$\\times$ speedup on control tasks. These model-free approaches avoid the failure mode we identify because they do not train value functions on imagined rollouts with variable temporal granularity.\n\nWithin world-model RL, temporal abstraction has been pursued primarily through \\emph{hierarchical} architectures. Director \\citep{hafner2022director} introduces subgoal-conditioned planning in the Dreamer latent space. THICK \\citep{gumbsch2024thick} learns adaptive temporal abstractions via context-change detection, constructing a hierarchy of latent dynamics models. Hieros \\citep{mattes2024hieros} builds multi-scale hierarchical imagination with S5 world models. LS-Imagine \\citep{li2025lsimagine} extends the effective imagination horizon via goal-conditioned jumpy state transitions. These hierarchical methods sidestep the single-scale variable-$dt$ approach we investigate. Hierarchical approaches may avoid the delusional critic phenomenon by operating at fixed temporal granularities within each level, though we do not test this hypothesis.\n\nMost relevant to our work is TAWM \\citep{nhu2025tawm}, which explicitly conditions a world model on time-step size $\\Delta t$ and trains over diverse $\\Delta t$ values for multi-rate dynamics learning. TAWM demonstrates that $\\Delta t$ conditioning \\emph{improves} performance and data efficiency—but critically, TAWM is built on TD-MPC2 and uses online model-predictive control, not imagination-based actor-critic training. Our work reveals that the same $\\Delta t$ conditioning that benefits MPC-based planning becomes pathological in imagination-based training: the critic exploits $dt$-conditioned value estimates from imprecise multi-step RSSM predictions, producing systematic overestimation. This paradigm-dependent asymmetry—beneficial in MPC, harmful in imagination-based actor-critic—is a central finding of our diagnostic analysis.\n\nThe sensitivity of RL algorithms to time discretization has been studied theoretically: \\citet{tallec2019making} show that Q-learning performance is highly sensitive to the discretization interval $\\delta$ and propose architectural modifications for $\\delta$-invariance. SAR \\citep{park2021sar} achieves time-discretization-invariant action repetition in model-free policy gradient methods. MTS3 \\citep{shaj2023mts3} proposes a probabilistic multi-time-scale state space model for variable-rate prediction. Our work demonstrates that world-model RL currently lacks this robustness: RSSM predictions trained at $\\delta\\!=\\!1$ degrade substantially at $dt\\!>\\!1$, and temporal conditioning amplifies rather than compensates for this degradation.\n\n## 2.3 Value Overestimation and Delusional Bias\n\nValue overestimation in deep RL was first identified by \\citet{thrun1993issues}, who showed that function approximation introduces systematic upward bias through the max operator in Q-learning. Double Q-learning \\citep{vanhasselt2016double} addresses this by decoupling action selection from value estimation, and TD3 \\citep{fujimoto2018td3} extends the idea to continuous control with clipped double critics. Ensemble methods such as SUNRISE \\citep{lee2021sunrise} use uncertainty-weighted value estimation to further suppress overestimation. DreamerV3 uses a single critic trained via categorical cross-entropy with symlog normalization \\citep{hafner2023dreamerv3}, which provides some implicit regularization against overestimation \\citep{farebrother2024stopregressing} but, as we show, is insufficient to prevent $dt$-embedding-induced value exploitation.\n\nDistinct from general overestimation, \\citet{lu2018nondelusional} formalize \\emph{delusional bias}: inconsistencies arising when Q-value backups assume policies that lie outside the representable policy class, producing value estimates that no realizable policy can achieve. \\citet{su2020conqur} extend this with consistency-penalized Q-labels. Our work identifies an analogous phenomenon in a fundamentally different setting. Where Lu et al.'s delusional bias arises from policy-class constraints in tabular or function-approximation Q-learning, our \\emph{delusional critic} arises from temporal conditioning in world-model imagination: the critic learns precise $dt$-conditioned value estimates, but the RSSM's prediction fidelity at $dt\\!>\\!1$ is insufficient to support this precision. The result is systematic overestimation of imagined trajectories at longer temporal steps—a form of delusion specific to the interaction between temporal conditioning and model-based imagination, not to function approximation per se.\n\nRecent work has connected value overestimation to training dynamics in model-based settings. \\citet{hussing2024dissecting} show that high update-to-data ratios drive value divergence through optimizer momentum, with overestimation occurring on both in-distribution and out-of-distribution data. \\citet{voelcker2025madtd} address value misgeneralization from replay distribution mismatch using model-generated data. Our delusional critic mechanism is complementary: the overestimation we identify is not driven by update ratios or distribution mismatch, but by the critic's ability to exploit temporally conditioned predictions from an imprecise world model. Crucially, the overestimation we identify arises from temporal conditioning on imprecise multi-step predictions rather than function approximation noise, rendering ensemble-based or pessimistic corrections insufficient as they target a different source of error.\n\n## 2.4 Multi-Step Prediction and Compounding Error\n\nCompounding prediction error is a fundamental challenge in model-based RL: small per-step model inaccuracies accumulate over multi-step rollouts, producing trajectories that diverge from ground truth \\citep{venkatraman2015improving, lambert2022investigating}. \\citet{asadi2019combating} propose multi-step models that predict several steps ahead in a single forward pass to bypass sequential error accumulation. \\citet{frauenknecht2025rollouts} show that trajectory-sampling rollouts can diverge from ground truth after only a few steps and actively harm policy learning.\n\nOur findings add a new dimension: when imagination operates at $dt\\!>\\!1$, the RSSM must predict further into the future per step, amplifying compounding error. However, compounding error alone does not explain the catastrophic collapse we observe. Configurations with identical compounding error exposure (same $dt$, same horizon) produce qualitatively different outcomes depending on whether the $dt$-embedding is trained: untrained $dt$-embedding yields stable learning despite degraded prediction quality, while trained $dt$-embedding triggers collapse. The root cause is the critic's exploitation of precise temporal conditioning built on imprecise predictions (see Section~2.3)—a failure mode that compounds \\emph{on top of} the standard compounding error problem.\n\n---\n\n**Overall positioning.** Temporal abstraction in world-model RL sits at the intersection of four well-studied areas: world-model architecture, temporal abstraction methods, value overestimation, and multi-step prediction error. Yet the specific interaction between temporal conditioning and imagination-based actor-critic training has received virtually no attention. Existing temporal abstraction methods operate in model-free or MPC settings where the failure mode we identify does not arise; existing analyses of value overestimation and compounding error do not consider temporal conditioning as a causal factor. Our work fills this gap by providing the first systematic diagnosis of why variable-rate imagination fails in DreamerV3, identifying trained $dt$-embedding as the mechanism that bridges imprecise multi-step predictions to pathological value overestimation, and offering a practical mitigation: restricting imagination to $dt\\!=\\!1$ during multi-$dt$ training, where preliminary results show near-baseline recovery (95\\% in initial seed) without any architectural modification.\n",
    "structuredPatch": [
      {
        "oldStart": 30,
        "oldLines": 6,
        "newStart": 30,
        "newLines": 10,
        "lines": [
          " ",
          " Our findings add a new dimension: when imagination operates at $dt\\!>\\!1$, the RSSM must predict further into the future per step, amplifying compounding error. However, compounding error alone does not explain the catastrophic collapse we observe. Configurations with identical compounding error exposure (same $dt$, same horizon) produce qualitatively different outcomes depending on whether the $dt$-embedding is trained: untrained $dt$-embedding yields stable learning despite degraded prediction quality, while trained $dt$-embedding triggers collapse. The root cause is the critic's exploitation of precise temporal conditioning built on imprecise predictions (see Section~2.3)—a failure mode that compounds \\emph{on top of} the standard compounding error problem.",
          " ",
          "+## 2.5 Diagnostic Methodology",
          "+",
          "+Our diagnostic methodology follows a tradition of systematic controlled experiments in RL. \\citet{engstrom2020implementation} demonstrate that implementation-level details—code-level choices typically unreported in publications—can account for most of the performance gains attributed to algorithmic innovations in deep policy gradients. \\citet{andrychowicz2021matters} extend this approach to on-policy RL, systematically evaluating the impact of individual design choices through matched ablations. In the same spirit, our work isolates individual factors (temporal conditioning, imagination horizon, $dt$-embedding training) through controlled ablations within a single codebase, rather than proposing new algorithms. This diagnostic framing allows us to identify the precise mechanism—trained $dt$-embedding interacting with imprecise multi-step predictions—responsible for the observed failure mode.",
          "+",
          " ---",
          " ",
          " **Overall positioning.** Temporal abstraction in world-model RL sits at the intersection of four well-studied areas: world-model architecture, temporal abstraction methods, value overestimation, and multi-step prediction error. Yet the specific interaction between temporal conditioning and imagination-based actor-critic training has received virtually no attention. Existing temporal abstraction methods operate in model-free or MPC settings where the failure mode we identify does not arise; existing analyses of value overestimation and compounding error do not consider temporal conditioning as a causal factor. Our work fills this gap by providing the first systematic diagnosis of why variable-rate imagination fails in DreamerV3, identifying trained $dt$-embedding as the mechanism that bridges imprecise multi-step predictions to pathological value overestimation, and offering a practical mitigation: restricting imagination to $dt\\!=\\!1$ during multi-$dt$ training, where preliminary results show near-baseline recovery (95\\% in initial seed) without any architectural modification."
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

_source line 26_

Let me verify the final result.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6f05e234-65d5-4fab-b46e-1cc055fade54",
  "uuid": "3f6c0a65-d269-49ab-87d9-ef2d60abc63b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GiGc2bg3DNGYiBt5YRnJBR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 434,
      "cache_read_input_tokens": 29808,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 434
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

_source line 27_

<details open><summary>🔧 Tool call — Read · `toolu_01BSJakPfmdwJuLEx52jgpi7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/paper_drafts/related_work_draft.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6f05e234-65d5-4fab-b46e-1cc055fade54",
  "uuid": "9258f55d-690d-454b-9d06-6aaf4a9b026a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GiGc2bg3DNGYiBt5YRnJBR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 434,
      "cache_read_input_tokens": 29808,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 434
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

_source line 28 · 2026-05-15T04:50:25.147Z_

<details><summary>↩ Tool result · `toolu_01BSJakPfmdwJuLEx52jgpi7`</summary>

```text
1	# Related Work — Draft
2	
3	## 2.1 World-Model Reinforcement Learning
4	
5	World-model reinforcement learning trains agents by learning a predictive model of environment dynamics and using it to generate synthetic experience for policy optimization. The Dreamer family of algorithms \citep{hafner2020dreamerv1, hafner2021dreamerv2, hafner2023dreamerv3} epitomizes this paradigm: a recurrent state-space model (RSSM) learns latent dynamics from interaction data, and an actor-critic pair is trained entirely within the model's imagined rollouts. DreamerV3 \citep{hafner2023dreamerv3} introduced symlog normalization and discrete latent representations that enable a single set of hyperparameters to master diverse domains, establishing it as the dominant imagination-based architecture. More recently, DreamerV4 \citep{hafner2025dreamerv4} replaces RSSM with a transformer world model, demonstrating scalability to video pretraining, though the core imagination-based training paradigm remains unchanged.
6	
7	A well-known risk in model-based RL is \emph{model exploitation}: the policy optimizer can discover and exploit inaccuracies in the learned model, producing policies that perform well in imagination but fail in the real environment. \citet{janner2019mbpo} formalize this concern and propose short-horizon branched rollouts to limit exploitation. Pessimistic approaches such as MOPO \citep{yu2020mopo} penalize reward by model uncertainty to discourage exploitation of unreliable regions. Planning-based approaches such as MuZero \citep{schrittwieser2020muzero} and EfficientZero \citep{ye2021efficientzero} use learned models for tree search rather than imagination rollouts for policy improvement, and thus do not exhibit the temporal-conditioning failure mode we diagnose. An orthogonal line of work avoids imagination-based training altogether: TD-MPC2 \citep{hansen2024tdmpc2} performs online model-predictive control at test time, sidestepping the need for imagination-trained value functions. Our work operates squarely within the DreamerV3 imagination-based training paradigm and diagnoses a specific form of model exploitation—value overestimation triggered by temporal conditioning—that prior model exploitation analyses have not identified.
8	
9	## 2.2 Temporal Abstraction in Reinforcement Learning
10	
11	Temporal abstraction—the ability to reason and act at multiple timescales—has been a long-standing goal in RL. The options framework \citep{sutton1999options} formalizes temporally extended actions as option policies with initiation sets and termination conditions, operating at the semi-MDP level. In the model-free setting, several methods learn variable action persistence: FiGAR \citep{sharma2017figar} augments the action space with a discrete repeat count, \citet{lakshminarayanan2017dynamic} learn per-step repetition durations, and TempoRL \citep{biedenkapp2021temporl} trains a skip-policy that achieves up to 10$\times$ speedup on control tasks. These model-free approaches avoid the failure mode we identify because they do not train value functions on imagined rollouts with variable temporal granularity.
12	
13	Within world-model RL, temporal abstraction has been pursued primarily through \emph{hierarchical} architectures. Director \citep{hafner2022director} introduces subgoal-conditioned planning in the Dreamer latent space. THICK \citep{gumbsch2024thick} learns adaptive temporal abstractions via context-change detection, constructing a hierarchy of latent dynamics models. Hieros \citep{mattes2024hieros} builds multi-scale hierarchical imagination with S5 world models. LS-Imagine \citep{li2025lsimagine} extends the effective imagination horizon via goal-conditioned jumpy state transitions. These hierarchical methods sidestep the single-scale variable-$dt$ approach we investigate. Hierarchical approaches may avoid the delusional critic phenomenon by operating at fixed temporal granularities within each level, though we do not test this hypothesis.
14	
15	Most relevant to our work is TAWM \citep{nhu2025tawm}, which explicitly conditions a world model on time-step size $\Delta t$ and trains over diverse $\Delta t$ values for multi-rate dynamics learning. TAWM demonstrates that $\Delta t$ conditioning \emph{improves} performance and data efficiency—but critically, TAWM is built on TD-MPC2 and uses online model-predictive control, not imagination-based actor-critic training. Our work reveals that the same $\Delta t$ conditioning that benefits MPC-based planning becomes pathological in imagination-based training: the critic exploits $dt$-conditioned value estimates from imprecise multi-step RSSM predictions, producing systematic overestimation. This paradigm-dependent asymmetry—beneficial in MPC, harmful in imagination-based actor-critic—is a central finding of our diagnostic analysis.
16	
17	The sensitivity of RL algorithms to time discretization has been studied theoretically: \citet{tallec2019making} show that Q-learning performance is highly sensitive to the discretization interval $\delta$ and propose architectural modifications for $\delta$-invariance. SAR \citep{park2021sar} achieves time-discretization-invariant action repetition in model-free policy gradient methods. MTS3 \citep{shaj2023mts3} proposes a probabilistic multi-time-scale state space model for variable-rate prediction. Our work demonstrates that world-model RL currently lacks this robustness: RSSM predictions trained at $\delta\!=\!1$ degrade substantially at $dt\!>\!1$, and temporal conditioning amplifies rather than compensates for this degradation.
18	
19	## 2.3 Value Overestimation and Delusional Bias
20	
21	Value overestimation in deep RL was first identified by \citet{thrun1993issues}, who showed that function approximation introduces systematic upward bias through the max operator in Q-learning. Double Q-learning \citep{vanhasselt2016double} addresses this by decoupling action selection from value estimation, and TD3 \citep{fujimoto2018td3} extends the idea to continuous control with clipped double critics. Ensemble methods such as SUNRISE \citep{lee2021sunrise} use uncertainty-weighted value estimation to further suppress overestimation. DreamerV3 uses a single critic trained via categorical cross-entropy with symlog normalization \citep{hafner2023dreamerv3}, which provides some implicit regularization against overestimation \citep{farebrother2024stopregressing} but, as we show, is insufficient to prevent $dt$-embedding-induced value exploitation.
22	
23	Distinct from general overestimation, \citet{lu2018nondelusional} formalize \emph{delusional bias}: inconsistencies arising when Q-value backups assume policies that lie outside the representable policy class, producing value estimates that no realizable policy can achieve. \citet{su2020conqur} extend this with consistency-penalized Q-labels. Our work identifies an analogous phenomenon in a fundamentally different setting. Where Lu et al.'s delusional bias arises from policy-class constraints in tabular or function-approximation Q-learning, our \emph{delusional critic} arises from temporal conditioning in world-model imagination: the critic learns precise $dt$-conditioned value estimates, but the RSSM's prediction fidelity at $dt\!>\!1$ is insufficient to support this precision. The result is systematic overestimation of imagined trajectories at longer temporal steps—a form of delusion specific to the interaction between temporal conditioning and model-based imagination, not to function approximation per se.
24	
25	Recent work has connected value overestimation to training dynamics in model-based settings. \citet{hussing2024dissecting} show that high update-to-data ratios drive value divergence through optimizer momentum, with overestimation occurring on both in-distribution and out-of-distribution data. \citet{voelcker2025madtd} address value misgeneralization from replay distribution mismatch using model-generated data. Our delusional critic mechanism is complementary: the overestimation we identify is not driven by update ratios or distribution mismatch, but by the critic's ability to exploit temporally conditioned predictions from an imprecise world model. Crucially, the overestimation we identify arises from temporal conditioning on imprecise multi-step predictions rather than function approximation noise, rendering ensemble-based or pessimistic corrections insufficient as they target a different source of error.
26	
27	## 2.4 Multi-Step Prediction and Compounding Error
28	
29	Compounding prediction error is a fundamental challenge in model-based RL: small per-step model inaccuracies accumulate over multi-step rollouts, producing trajectories that diverge from ground truth \citep{venkatraman2015improving, lambert2022investigating}. \citet{asadi2019combating} propose multi-step models that predict several steps ahead in a single forward pass to bypass sequential error accumulation. \citet{frauenknecht2025rollouts} show that trajectory-sampling rollouts can diverge from ground truth after only a few steps and actively harm policy learning.
30	
31	Our findings add a new dimension: when imagination operates at $dt\!>\!1$, the RSSM must predict further into the future per step, amplifying compounding error. However, compounding error alone does not explain the catastrophic collapse we observe. Configurations with identical compounding error exposure (same $dt$, same horizon) produce qualitatively different outcomes depending on whether the $dt$-embedding is trained: untrained $dt$-embedding yields stable learning despite degraded prediction quality, while trained $dt$-embedding triggers collapse. The root cause is the critic's exploitation of precise temporal conditioning built on imprecise predictions (see Section~2.3)—a failure mode that compounds \emph{on top of} the standard compounding error problem.
32	
33	## 2.5 Diagnostic Methodology
34	
35	Our diagnostic methodology follows a tradition of systematic controlled experiments in RL. \citet{engstrom2020implementation} demonstrate that implementation-level details—code-level choices typically unreported in publications—can account for most of the performance gains attributed to algorithmic innovations in deep policy gradients. \citet{andrychowicz2021matters} extend this approach to on-policy RL, systematically evaluating the impact of individual design choices through matched ablations. In the same spirit, our work isolates individual factors (temporal conditioning, imagination horizon, $dt$-embedding training) through controlled ablations within a single codebase, rather than proposing new algorithms. This diagnostic framing allows us to identify the precise mechanism—trained $dt$-embedding interacting with imprecise multi-step predictions—responsible for the observed failure mode.
36	
37	---
38	
39	**Overall positioning.** Temporal abstraction in world-model RL sits at the intersection of four well-studied areas: world-model architecture, temporal abstraction methods, value overestimation, and multi-step prediction error. Yet the specific interaction between temporal conditioning and imagination-based actor-critic training has received virtually no attention. Existing temporal abstraction methods operate in model-free or MPC settings where the failure mode we identify does not arise; existing analyses of value overestimation and compounding error do not consider temporal conditioning as a causal factor. Our work fills this gap by providing the first systematic diagnosis of why variable-rate imagination fails in DreamerV3, identifying trained $dt$-embedding as the mechanism that bridges imprecise multi-step predictions to pathological value overestimation, and offering a practical mitigation: restricting imagination to $dt\!=\!1$ during multi-$dt$ training, where preliminary results show near-baseline recovery (95\% in initial seed) without any architectural modification.
40	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6f05e234-65d5-4fab-b46e-1cc055fade54",
  "uuid": "82ca5dec-fd98-4562-9842-6c57e5197ad1",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/paper_drafts/related_work_draft.md",
      "content": "# Related Work — Draft\n\n## 2.1 World-Model Reinforcement Learning\n\nWorld-model reinforcement learning trains agents by learning a predictive model of environment dynamics and using it to generate synthetic experience for policy optimization. The Dreamer family of algorithms \\citep{hafner2020dreamerv1, hafner2021dreamerv2, hafner2023dreamerv3} epitomizes this paradigm: a recurrent state-space model (RSSM) learns latent dynamics from interaction data, and an actor-critic pair is trained entirely within the model's imagined rollouts. DreamerV3 \\citep{hafner2023dreamerv3} introduced symlog normalization and discrete latent representations that enable a single set of hyperparameters to master diverse domains, establishing it as the dominant imagination-based architecture. More recently, DreamerV4 \\citep{hafner2025dreamerv4} replaces RSSM with a transformer world model, demonstrating scalability to video pretraining, though the core imagination-based training paradigm remains unchanged.\n\nA well-known risk in model-based RL is \\emph{model exploitation}: the policy optimizer can discover and exploit inaccuracies in the learned model, producing policies that perform well in imagination but fail in the real environment. \\citet{janner2019mbpo} formalize this concern and propose short-horizon branched rollouts to limit exploitation. Pessimistic approaches such as MOPO \\citep{yu2020mopo} penalize reward by model uncertainty to discourage exploitation of unreliable regions. Planning-based approaches such as MuZero \\citep{schrittwieser2020muzero} and EfficientZero \\citep{ye2021efficientzero} use learned models for tree search rather than imagination rollouts for policy improvement, and thus do not exhibit the temporal-conditioning failure mode we diagnose. An orthogonal line of work avoids imagination-based training altogether: TD-MPC2 \\citep{hansen2024tdmpc2} performs online model-predictive control at test time, sidestepping the need for imagination-trained value functions. Our work operates squarely within the DreamerV3 imagination-based training paradigm and diagnoses a specific form of model exploitation—value overestimation triggered by temporal conditioning—that prior model exploitation analyses have not identified.\n\n## 2.2 Temporal Abstraction in Reinforcement Learning\n\nTemporal abstraction—the ability to reason and act at multiple timescales—has been a long-standing goal in RL. The options framework \\citep{sutton1999options} formalizes temporally extended actions as option policies with initiation sets and termination conditions, operating at the semi-MDP level. In the model-free setting, several methods learn variable action persistence: FiGAR \\citep{sharma2017figar} augments the action space with a discrete repeat count, \\citet{lakshminarayanan2017dynamic} learn per-step repetition durations, and TempoRL \\citep{biedenkapp2021temporl} trains a skip-policy that achieves up to 10$\\times$ speedup on control tasks. These model-free approaches avoid the failure mode we identify because they do not train value functions on imagined rollouts with variable temporal granularity.\n\nWithin world-model RL, temporal abstraction has been pursued primarily through \\emph{hierarchical} architectures. Director \\citep{hafner2022director} introduces subgoal-conditioned planning in the Dreamer latent space. THICK \\citep{gumbsch2024thick} learns adaptive temporal abstractions via context-change detection, constructing a hierarchy of latent dynamics models. Hieros \\citep{mattes2024hieros} builds multi-scale hierarchical imagination with S5 world models. LS-Imagine \\citep{li2025lsimagine} extends the effective imagination horizon via goal-conditioned jumpy state transitions. These hierarchical methods sidestep the single-scale variable-$dt$ approach we investigate. Hierarchical approaches may avoid the delusional critic phenomenon by operating at fixed temporal granularities within each level, though we do not test this hypothesis.\n\nMost relevant to our work is TAWM \\citep{nhu2025tawm}, which explicitly conditions a world model on time-step size $\\Delta t$ and trains over diverse $\\Delta t$ values for multi-rate dynamics learning. TAWM demonstrates that $\\Delta t$ conditioning \\emph{improves} performance and data efficiency—but critically, TAWM is built on TD-MPC2 and uses online model-predictive control, not imagination-based actor-critic training. Our work reveals that the same $\\Delta t$ conditioning that benefits MPC-based planning becomes pathological in imagination-based training: the critic exploits $dt$-conditioned value estimates from imprecise multi-step RSSM predictions, producing systematic overestimation. This paradigm-dependent asymmetry—beneficial in MPC, harmful in imagination-based actor-critic—is a central finding of our diagnostic analysis.\n\nThe sensitivity of RL algorithms to time discretization has been studied theoretically: \\citet{tallec2019making} show that Q-learning performance is highly sensitive to the discretization interval $\\delta$ and propose architectural modifications for $\\delta$-invariance. SAR \\citep{park2021sar} achieves time-discretization-invariant action repetition in model-free policy gradient methods. MTS3 \\citep{shaj2023mts3} proposes a probabilistic multi-time-scale state space model for variable-rate prediction. Our work demonstrates that world-model RL currently lacks this robustness: RSSM predictions trained at $\\delta\\!=\\!1$ degrade substantially at $dt\\!>\\!1$, and temporal conditioning amplifies rather than compensates for this degradation.\n\n## 2.3 Value Overestimation and Delusional Bias\n\nValue overestimation in deep RL was first identified by \\citet{thrun1993issues}, who showed that function approximation introduces systematic upward bias through the max operator in Q-learning. Double Q-learning \\citep{vanhasselt2016double} addresses this by decoupling action selection from value estimation, and TD3 \\citep{fujimoto2018td3} extends the idea to continuous control with clipped double critics. Ensemble methods such as SUNRISE \\citep{lee2021sunrise} use uncertainty-weighted value estimation to further suppress overestimation. DreamerV3 uses a single critic trained via categorical cross-entropy with symlog normalization \\citep{hafner2023dreamerv3}, which provides some implicit regularization against overestimation \\citep{farebrother2024stopregressing} but, as we show, is insufficient to prevent $dt$-embedding-induced value exploitation.\n\nDistinct from general overestimation, \\citet{lu2018nondelusional} formalize \\emph{delusional bias}: inconsistencies arising when Q-value backups assume policies that lie outside the representable policy class, producing value estimates that no realizable policy can achieve. \\citet{su2020conqur} extend this with consistency-penalized Q-labels. Our work identifies an analogous phenomenon in a fundamentally different setting. Where Lu et al.'s delusional bias arises from policy-class constraints in tabular or function-approximation Q-learning, our \\emph{delusional critic} arises from temporal conditioning in world-model imagination: the critic learns precise $dt$-conditioned value estimates, but the RSSM's prediction fidelity at $dt\\!>\\!1$ is insufficient to support this precision. The result is systematic overestimation of imagined trajectories at longer temporal steps—a form of delusion specific to the interaction between temporal conditioning and model-based imagination, not to function approximation per se.\n\nRecent work has connected value overestimation to training dynamics in model-based settings. \\citet{hussing2024dissecting} show that high update-to-data ratios drive value divergence through optimizer momentum, with overestimation occurring on both in-distribution and out-of-distribution data. \\citet{voelcker2025madtd} address value misgeneralization from replay distribution mismatch using model-generated data. Our delusional critic mechanism is complementary: the overestimation we identify is not driven by update ratios or distribution mismatch, but by the critic's ability to exploit temporally conditioned predictions from an imprecise world model. Crucially, the overestimation we identify arises from temporal conditioning on imprecise multi-step predictions rather than function approximation noise, rendering ensemble-based or pessimistic corrections insufficient as they target a different source of error.\n\n## 2.4 Multi-Step Prediction and Compounding Error\n\nCompounding prediction error is a fundamental challenge in model-based RL: small per-step model inaccuracies accumulate over multi-step rollouts, producing trajectories that diverge from ground truth \\citep{venkatraman2015improving, lambert2022investigating}. \\citet{asadi2019combating} propose multi-step models that predict several steps ahead in a single forward pass to bypass sequential error accumulation. \\citet{frauenknecht2025rollouts} show that trajectory-sampling rollouts can diverge from ground truth after only a few steps and actively harm policy learning.\n\nOur findings add a new dimension: when imagination operates at $dt\\!>\\!1$, the RSSM must predict further into the future per step, amplifying compounding error. However, compounding error alone does not explain the catastrophic collapse we observe. Configurations with identical compounding error exposure (same $dt$, same horizon) produce qualitatively different outcomes depending on whether the $dt$-embedding is trained: untrained $dt$-embedding yields stable learning despite degraded prediction quality, while trained $dt$-embedding triggers collapse. The root cause is the critic's exploitation of precise temporal conditioning built on imprecise predictions (see Section~2.3)—a failure mode that compounds \\emph{on top of} the standard compounding error problem.\n\n## 2.5 Diagnostic Methodology\n\nOur diagnostic methodology follows a tradition of systematic controlled experiments in RL. \\citet{engstrom2020implementation} demonstrate that implementation-level details—code-level choices typically unreported in publications—can account for most of the performance gains attributed to algorithmic innovations in deep policy gradients. \\citet{andrychowicz2021matters} extend this approach to on-policy RL, systematically evaluating the impact of individual design choices through matched ablations. In the same spirit, our work isolates individual factors (temporal conditioning, imagination horizon, $dt$-embedding training) through controlled ablations within a single codebase, rather than proposing new algorithms. This diagnostic framing allows us to identify the precise mechanism—trained $dt$-embedding interacting with imprecise multi-step predictions—responsible for the observed failure mode.\n\n---\n\n**Overall positioning.** Temporal abstraction in world-model RL sits at the intersection of four well-studied areas: world-model architecture, temporal abstraction methods, value overestimation, and multi-step prediction error. Yet the specific interaction between temporal conditioning and imagination-based actor-critic training has received virtually no attention. Existing temporal abstraction methods operate in model-free or MPC settings where the failure mode we identify does not arise; existing analyses of value overestimation and compounding error do not consider temporal conditioning as a causal factor. Our work fills this gap by providing the first systematic diagnosis of why variable-rate imagination fails in DreamerV3, identifying trained $dt$-embedding as the mechanism that bridges imprecise multi-step predictions to pathological value overestimation, and offering a practical mitigation: restricting imagination to $dt\\!=\\!1$ during multi-$dt$ training, where preliminary results show near-baseline recovery (95\\% in initial seed) without any architectural modification.\n",
      "numLines": 40,
      "startLine": 1,
      "totalLines": 40
    }
  }
}
```

</details>

---

### Assistant

_source line 29_

All 6 modifications applied. Summary:

| Item | Change | Location |
|------|--------|----------|
| **1** | "recovers 95%" → "preliminary results show near-baseline recovery (95% in initial seed)" | Line 39 (Overall positioning) |
| **2** | New Section 2.5 "Diagnostic Methodology" citing Engstrom et al. 2020 & Andrychowicz et al. 2021 | Lines 33–35 |
| **3** | Added sentence explaining ensemble/pessimistic methods target wrong error source | Line 25, end of Section 2.3 |
| **4** | Added MuZero/EfficientZero sentence (tree search, not imagination rollouts) | Line 7, Section 2.1 |
| **5** | "avoids" → "may avoid … though we do not test this hypothesis" for hierarchy claims | Line 13, Section 2.2 |
| **7** | Section 2.4 trimmed ~35%: removed Ke2019, Barkley2024, redundant value overestimation discussion; consolidated citations; added cross-ref to Section 2.3 | Lines 29–31 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6f05e234-65d5-4fab-b46e-1cc055fade54",
  "uuid": "28ecc3fd-161d-45a7-a3e5-c21663aea84f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012EcdKnh5rSUoBJo8EWUiJ3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2950,
      "cache_read_input_tokens": 30242,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2950
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

_source line 30_

All 6 modifications applied. Summary:

| Item | Change | Location |
|------|--------|----------|
| **1** | "recovers 95%" → "preliminary results show near-baseline recovery (95% in initial seed)" | Line 39 (Overall positioning) |
| **2** | New Section 2.5 "Diagnostic Methodology" citing Engstrom et al. 2020 & Andrychowicz et al. 2021 | Lines 33–35 |
| **3** | Added sentence explaining ensemble/pessimistic methods target wrong error source | Line 25, end of Section 2.3 |
| **4** | Added MuZero/EfficientZero sentence (tree search, not imagination rollouts) | Line 7, Section 2.1 |
| **5** | "avoids" → "may avoid … though we do not test this hypothesis" for hierarchy claims | Line 13, Section 2.2 |
| **7** | Section 2.4 trimmed ~35%: removed Ke2019, Barkley2024, redundant value overestimation discussion; consolidated citations; added cross-ref to Section 2.3 | Lines 29–31 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 96451,
  "duration_api_ms": 97542,
  "num_turns": 9,
  "stop_reason": "end_turn",
  "session_id": "6f05e234-65d5-4fab-b46e-1cc055fade54",
  "total_cost_usd": 0.34561325,
  "usage": {
    "input_tokens": 10,
    "cache_creation_input_tokens": 21745,
    "cache_read_input_tokens": 234312,
    "output_tokens": 3625,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 21745,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 290,
        "cache_read_input_tokens": 30242,
        "cache_creation_input_tokens": 2950,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 2950
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1781,
      "outputTokens": 19,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001876,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 10,
      "outputTokens": 3625,
      "cacheReadInputTokens": 234312,
      "cacheCreationInputTokens": 21745,
      "webSearchRequests": 0,
      "costUSD": 0.34373725,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "555e3f0c-3cc9-4aaf-84cf-8b61914447f0"
}
```

</details>

---
