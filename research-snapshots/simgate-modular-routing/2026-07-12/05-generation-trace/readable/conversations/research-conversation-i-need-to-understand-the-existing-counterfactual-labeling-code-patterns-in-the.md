# Research conversation: I need to understand the existing counterfactual labeling code patterns in the simgate-modular-routing project so I can 

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 35
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-aaafa5e9203d8d469.jsonl`
- **Structured JSON:** [`cb7230324e5d001a932b.json`](../../sessions/cb/cb7230324e5d001a932b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

35 recorded events

### User

_source line 1 · 2026-05-14T13:30:15.531Z_

I need to understand the existing counterfactual labeling code patterns in the simgate-modular-routing project so I can build a consistent ALFWorld counterfactual pipeline.

The project is at /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/

Please read and summarize the key patterns from these files:
1. src/counterfactual_labeling.py - the ScienceWorld counterfactual labeling code
2. src/math_counterfactual.py - the MATH counterfactual labeling code
3. src/llm_agent.py - the LLM agent interface

For each file, I need:
- The overall structure and main functions
- How "internal" vs "deterministic" modes are implemented
- How episodes are run and labeled
- The output JSONL format
- How the LLM is called (local vLLM? transformers? API?)
- Any state forking mechanism used

Read these files thoroughly - I need enough detail to write consistent ALFWorld code.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "873d52d2-4b2b-4bc2-850b-aec21329b090",
  "agentId": "aaafa5e9203d8d469",
  "type": "user",
  "uuid": "8953b5fc-ee7b-4310-804a-a08ef0713895",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "ee553895-1021-4931-aae1-4600fac1ac8a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-14T13:30:16.975Z_

I'll help you understand the counterfactual labeling patterns in this project. Let me start by exploring the project structure and reading those three key files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8953b5fc-ee7b-4310-804a-a08ef0713895",
  "isSidechain": true,
  "agentId": "aaafa5e9203d8d469",
  "requestId": "req_011Cb2YRbmZ9pf7Sbuo4zrGK",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1de363f6-319f-4550-990e-e7e7691f6365",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "ee553895-1021-4931-aae1-4600fac1ac8a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EuKBpWb4frJH4RxUuMDa6o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17128,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17128,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T13:30:17.126Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01WEVMVxEiXzvy8ra795FndU`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing -type f -name \"*.py\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1de363f6-319f-4550-990e-e7e7691f6365",
  "isSidechain": true,
  "agentId": "aaafa5e9203d8d469",
  "requestId": "req_011Cb2YRbmZ9pf7Sbuo4zrGK",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4c9333ca-93e4-4fac-ad3f-8d4daa6a5779",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "ee553895-1021-4931-aae1-4600fac1ac8a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EuKBpWb4frJH4RxUuMDa6o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17128,
      "cache_read_input_tokens": 0,
      "output_tokens": 127,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 17128
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 127,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 17128,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 17128,
            "ephemeral_1h_input_tokens": 0
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

_source line 4 · 2026-05-14T13:30:17.353Z_

<details><summary>↩ Tool result · `toolu_01WEVMVxEiXzvy8ra795FndU`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/src/phase1_signal.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/src/alfworld_counterfactual.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/src/ablation_implicit_1_7b.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/src/eval_implicit_router.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/src/scienceworld_utils.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/src/llm_agent.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/src/evaluation/ablation_comparison.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/src/evaluation/prompt_routing_eval.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/src/ablation_eval_common.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/src/episode_level_collection.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/src/rule_based_accuracy.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/src/analysis.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/src/router_sft_eval.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/src/eval_end_to_end.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/src/phase0_validate_forking.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/src/counterfactual_labeling.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/src/death_decomposition.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/src/training/format_implicit_data.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/src/training/router_sft.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/src/training/implicit_router_sft.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4c9333ca-93e4-4fac-ad3f-8d4daa6a5779",
  "isSidechain": true,
  "promptId": "873d52d2-4b2b-4bc2-850b-aec21329b090",
  "agentId": "aaafa5e9203d8d469",
  "type": "user",
  "uuid": "92a51afa-4638-4c1a-9b9e-27584bc85c77",
  "sourceToolAssistantUUID": "4c9333ca-93e4-4fac-ad3f-8d4daa6a5779",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "ee553895-1021-4931-aae1-4600fac1ac8a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-14T13:30:18.717Z_

Now let me read the three key files you mentioned:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "92a51afa-4638-4c1a-9b9e-27584bc85c77",
  "isSidechain": true,
  "agentId": "aaafa5e9203d8d469",
  "requestId": "req_011Cb2YRjfp2e9trXg8FfTCu",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d81a915d-8e3e-494c-97bd-242611220001",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "ee553895-1021-4931-aae1-4600fac1ac8a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012q5EDVRG3tAcogatXYgdUk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1788,
      "cache_read_input_tokens": 17128,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1788,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-14T13:30:18.968Z_

<details open><summary>🔧 Tool call — Read · `toolu_012PeV6FUysi8t3YRixqv1pv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/src/counterfactual_labeling.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d81a915d-8e3e-494c-97bd-242611220001",
  "isSidechain": true,
  "agentId": "aaafa5e9203d8d469",
  "requestId": "req_011Cb2YRjfp2e9trXg8FfTCu",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "18461534-89fa-45b9-b414-ee02c3609d7d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "ee553895-1021-4931-aae1-4600fac1ac8a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012q5EDVRG3tAcogatXYgdUk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1788,
      "cache_read_input_tokens": 17128,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1788,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-14T13:30:18.987Z_

<details><summary>↩ Tool result · `toolu_012PeV6FUysi8t3YRixqv1pv`</summary>

```text
1	"""Episode-terminal counterfactual labeling for SimGate routing.
2	
3	Problem: 1-step oracle labeling (phase1_signal.py) yields 98.2% tie rate because
4	single-step score deltas are almost always 0. This script instead forks the
5	environment at action-diverge points and continues for K steps, using the
6	final score difference as the label signal.
7	
8	Pipeline per episode:
9	  1. Run main episode step-by-step
10	  2. At each step, get internal_action (ReAct) and det_action (fork-evaluate candidates)
11	  3. If they agree → tie, advance
12	  4. If they differ → fork twice (one per action), continue K steps with base policy,
13	     compare final scores → label = deterministic / internal / tie
14	  5. Advance main env with the oracle-chosen action
15	
16	Inputs:  task type, LLM agent (Qwen2.5-7B on GPU)
17	Outputs: {output_dir}/{task_type}/cf_labels.jsonl
18	
19	Relation to phase1_signal.py:
20	  - Reuses the same ScienceWorldEnv / LLMAgent / fork_and_lookahead infra
21	  - Replaces the 1-step oracle with K-step counterfactual evaluation
22	"""
23	
24	import argparse
25	import json
26	import os
27	import random
28	import sys
29	import time
30	from typing import List, Dict, Any, Optional, Tuple
31	
32	sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
33	from scienceworld_utils import (
34	    create_env, reset_env, get_valid_actions, get_score,
35	    step_env, close_env, fork_and_lookahead, get_task_types,
36	    get_max_variations,
37	)
38	from llm_agent import LLMAgent, find_model_path
39	
40	
41	def resolve_task_type(name: str) -> str:
42	    try:
43	        available = get_task_types()
44	    except Exception:
45	        return name
46	    if name in available:
47	        return name
48	    matches = [t for t in available if name.lower() in t.lower()]
49	    if matches:
50	        return matches[0]
51	    return name
52	
53	
54	def is_lethal(fr: Dict[str, Any]) -> bool:
55	    if fr["done"] and fr["score"] < 0:
56	        return True
57	    if fr["score"] <= -100:
58	        return True
59	    return False
60	
61	
62	def get_deterministic_action(
63	    agent: LLMAgent,
64	    task_name: str,
65	    variation_idx: int,
66	    obs: str,
67	    valid_actions: List[str],
68	    action_history: List[str],
69	    history_dicts: List[dict],
70	    n_candidates: int = 3,
71	) -> Tuple[str, float, List[dict]]:
72	    """Generate candidates via LLM, fork-evaluate each with 1-step lookahead,
73	    return (best_action, best_delta, fork_results). Filters lethal actions."""
74	    candidates, _ = agent.generate_candidate_actions(
75	        obs, valid_actions, history_dicts, n=n_candidates
76	    )
77	
78	    best_action = None
79	    best_delta = float("-inf")
80	    best_fallback = None
81	    best_delta_fb = float("-inf")
82	    fork_results = []
83	
84	    for cand in candidates:
85	        fr = fork_and_lookahead(task_name, variation_idx, action_history, cand)
86	        lethal = is_lethal(fr)
87	        fork_results.append({
88	            "action": cand, "score_delta": fr["score_delta"],
89	            "score": fr["score"], "lethal": lethal,
90	        })
91	        if fr["score_delta"] > best_delta_fb:
92	            best_delta_fb = fr["score_delta"]
93	            best_fallback = cand
94	        if not lethal and fr["score_delta"] > best_delta:
95	            best_delta = fr["score_delta"]
96	            best_action = cand
97	
98	    if best_action is None:
99	        best_action = best_fallback if best_fallback else valid_actions[0]
100	        best_delta = best_delta_fb
101	
102	    return best_action, best_delta, fork_results
103	
104	
105	def fork_and_continue(
106	    agent: LLMAgent,
107	    task_name: str,
108	    variation_idx: int,
109	    action_history: List[str],
110	    first_action: str,
111	    continuation_steps: int = 10,
112	) -> float:
113	    """Fork env, execute first_action, then continue K steps with base policy
114	    (always-internal ReAct). Returns final score. Always closes the forked env."""
115	    fork_env = None
116	    try:
117	        fork_env = create_env(task_name, variation_idx)
118	        reset_env(fork_env)
119	
120	        for past_action in action_history:
121	            step_env(fork_env, past_action)
122	
123	        obs, reward, done, info = step_env(fork_env, first_action)
124	
125	        history_dicts = []
126	        for k in range(continuation_steps):
127	            if done:
128	                break
129	            valid = get_valid_actions(fork_env)
130	            if not valid:
131	                break
132	            action, _ = agent.select_action_react(obs, valid, history_dicts)
133	            obs, reward, done, info = step_env(fork_env, action)
134	            history_dicts.append({"action": action, "observation": obs[:200], "score": get_score(fork_env)})
135	
136	        return get_score(fork_env)
137	    except Exception as e:
138	        print(f"  [WARN] fork_and_continue failed: {e}")
139	        return 0.0
140	    finally:
141	        if fork_env is not None:
142	            close_env(fork_env)
143	
144	
145	def run_episode(
146	    agent: LLMAgent,
147	    task_name: str,
148	    variation_idx: int,
149	    max_steps: int,
150	    continuation_steps: int,
151	    n_candidates: int = 3,
152	) -> Dict[str, Any]:
153	    env = create_env(task_name, variation_idx)
154	    obs, _ = reset_env(env)
155	
156	    labels = []
157	    action_history = []
158	    history_dicts = []
159	    fork_times = []
160	    t0 = time.time()
161	
162	    for step_idx in range(max_steps):
163	        valid_actions = get_valid_actions(env)
164	        if not valid_actions:
165	            break
166	
167	        # Internal action (ReAct)
168	        internal_action, react_raw = agent.select_action_react(obs, valid_actions, history_dicts)
169	
170	        # Death filter for internal action
171	        _remaining = list(valid_actions)
172	        for _retry in range(3):
173	            fr = fork_and_lookahead(task_name, variation_idx, action_history, internal_action)
174	            if not is_lethal(fr):
175	                break
176	            _remaining = [a for a in _remaining if a != internal_action]
177	            if not _remaining:
178	                break
179	            internal_action, react_raw = agent.select_action_react(obs, _remaining, history_dicts)
180	
181	        # Deterministic action
182	        det_action, det_delta, det_forks = get_deterministic_action(
183	            agent, task_name, variation_idx, obs, valid_actions,
184	            action_history, history_dicts, n_candidates,
185	        )
186	
187	        if internal_action == det_action:
188	            labels.append({"step": step_idx, "label": "tie", "score_diff": 0.0})
189	            chosen = internal_action
190	        else:
191	            # Fork both and continue K steps
192	            t_fork = time.time()
193	            fork_int_score = fork_and_continue(
194	                agent, task_name, variation_idx, action_history,
195	                internal_action, continuation_steps,
196	            )
197	            fork_det_score = fork_and_continue(
198	                agent, task_name, variation_idx, action_history,
199	                det_action, continuation_steps,
200	            )
201	            fork_elapsed = time.time() - t_fork
202	            fork_times.append(fork_elapsed)
203	
204	            score_diff = fork_det_score - fork_int_score
205	            if score_diff > 0:
206	                best = "deterministic"
207	            elif score_diff < 0:
208	                best = "internal"
209	            else:
210	                best = "tie"
211	
212	            labels.append({
213	                "step": step_idx,
214	                "obs": obs[:500],
215	                "internal_action": internal_action,
216	                "det_action": det_action,
217	                "fork_internal_score": fork_int_score,
218	                "fork_det_score": fork_det_score,
219	                "score_diff": score_diff,
220	                "label": best,
221	                "fork_time_s": round(fork_elapsed, 2),
222	            })
223	
224	            chosen = det_action if score_diff > 0 else internal_action
225	
226	        score_before = get_score(env)
227	        obs_new, reward, done, info = step_env(env, chosen)
228	        score_after = get_score(env)
229	
230	        action_history.append(chosen)
231	        history_dicts.append({"action": chosen, "observation": obs_new[:200], "score": score_after})
232	        obs = obs_new
233	
234	        diverge_tag = "" if internal_action == det_action else f" DIVERGE→{labels[-1]['label']}"
235	        print(f"    step {step_idx}: score {score_before:.0f}→{score_after:.0f} "
236	              f"action='{chosen[:40]}'{diverge_tag}")
237	
238	        if done:
239	            break
240	
241	    final_score = get_score(env)
242	    close_env(env)
243	
244	    label_counts = {"deterministic": 0, "internal": 0, "tie": 0}
245	    for lb in labels:
246	        label_counts[lb["label"]] += 1
247	    diverge_steps = label_counts["deterministic"] + label_counts["internal"]
248	
249	    return {
250	        "episode": -1,  # filled by caller
251	        "variation": variation_idx,
252	        "total_steps": len(labels),
253	        "diverge_steps": diverge_steps,
254	        "tie_steps": label_counts["tie"],
255	        "labels": labels,
256	        "final_score": final_score,
257	        "label_summary": label_counts,
258	        "total_time_s": round(time.time() - t0, 1),
259	        "avg_fork_time_s": round(sum(fork_times) / len(fork_times), 2) if fork_times else 0.0,
260	    }
261	
262	
263	def main():
264	    parser = argparse.ArgumentParser(
265	        description="Episode-terminal counterfactual labeling for SimGate routing"
266	    )
267	    parser.add_argument("--task_type", type=str, required=True,
268	                        help="ScienceWorld task name (e.g. boil, melt)")
269	    parser.add_argument("--episodes", type=int, default=20)
270	    parser.add_argument("--gpu_id", type=int, default=0)
271	    parser.add_argument("--max_steps", type=int, default=30)
272	    parser.add_argument("--continuation_steps", type=int, default=10,
273	                        help="K: steps to continue after fork")
274	    parser.add_argument("--output_dir", type=str, default="results/cf_labels/")
275	    parser.add_argument("--model_path", type=str, default=None)
276	    parser.add_argument("--use_vllm", action="store_true", default=True)
277	    parser.add_argument("--no_vllm", action="store_true", default=False)
278	    parser.add_argument("--n_candidates", type=int, default=3)
279	    parser.add_argument("--seed", type=int, default=42)
280	    args = parser.parse_args()
281	
282	    if args.no_vllm:
283	        args.use_vllm = False
284	
285	    random.seed(args.seed)
286	    task_name = resolve_task_type(args.task_type)
287	
288	    print(f"=== CF LABELING SETUP ===")
289	    print(f"Task: {task_name} | Episodes: {args.episodes} | Max steps: {args.max_steps}")
290	    print(f"Continuation K={args.continuation_steps} | GPU: {args.gpu_id} | Seed: {args.seed}")
291	
292	    agent = LLMAgent(
293	        model_path=args.model_path,
294	        use_vllm=args.use_vllm,
295	        gpu_id=args.gpu_id,
296	    )
297	
298	    max_var = get_max_variations(task_name)
299	    task_dir = os.path.join(args.output_dir, task_name.replace(" ", "_"))
300	    os.makedirs(task_dir, exist_ok=True)
301	    out_file = os.path.join(task_dir, "cf_labels.jsonl")
302	
303	    all_diverge = 0
304	    all_steps = 0
305	    all_labels = {"deterministic": 0, "internal": 0, "tie": 0}
306	    all_fork_times = []
307	
308	    for ep_idx in range(args.episodes):
309	        variation_idx = ep_idx % max_var
310	        print(f"\n--- Episode {ep_idx}/{args.episodes} (variation={variation_idx}) ---")
311	
312	        result = run_episode(
313	            agent, task_name, variation_idx,
314	            args.max_steps, args.continuation_steps, args.n_candidates,
315	        )
316	        result["episode"] = ep_idx
317	
318	        with open(out_file, "a") as f:
319	            f.write(json.dumps(result, default=str) + "\n")
320	
321	        all_steps += result["total_steps"]
322	        all_diverge += result["diverge_steps"]
323	        for k in ("deterministic", "internal", "tie"):
324	            all_labels[k] += result["label_summary"][k]
325	        if result["avg_fork_time_s"] > 0:
326	            all_fork_times.append(result["avg_fork_time_s"])
327	
328	        print(f"  → score={result['final_score']:.1f} | "
329	              f"diverge={result['diverge_steps']}/{result['total_steps']} | "
330	              f"labels: det={result['label_summary']['deterministic']} "
331	              f"int={result['label_summary']['internal']} "
332	              f"tie={result['label_summary']['tie']} | "
333	              f"{result['total_time_s']:.0f}s")
334	
335	    # Summary
336	    diverge_pct = 100.0 * all_diverge / all_steps if all_steps > 0 else 0
337	    avg_fork = sum(all_fork_times) / len(all_fork_times) if all_fork_times else 0
338	    print(f"\n{'='*50}")
339	    print(f"=== CF LABELING: {task_name} ===")
340	    print(f"Episodes: {args.episodes}")
341	    print(f"Total steps: {all_steps}")
342	    print(f"Diverge steps: {all_diverge} ({diverge_pct:.1f}%)")
343	    print(f"Labels: det={all_labels['deterministic']}, int={all_labels['internal']}, tie={all_labels['tie']}")
344	    print(f"Avg continuation time per fork: {avg_fork:.1f}s")
345	    print(f"Output: {out_file}")
346	    print(f"{'='*50}")
347	
348	
349	if __name__ == "__main__":
350	    main()
351	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "18461534-89fa-45b9-b414-ee02c3609d7d",
  "isSidechain": true,
  "promptId": "873d52d2-4b2b-4bc2-850b-aec21329b090",
  "agentId": "aaafa5e9203d8d469",
  "type": "user",
  "uuid": "a21970c5-5ce0-4496-aa53-a9d951c4ba42",
  "sourceToolAssistantUUID": "18461534-89fa-45b9-b414-ee02c3609d7d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "ee553895-1021-4931-aae1-4600fac1ac8a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-14T13:30:19.171Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WevThMFCZhFerqj6BknnsR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/src/math_counterfactual.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a21970c5-5ce0-4496-aa53-a9d951c4ba42",
  "isSidechain": true,
  "agentId": "aaafa5e9203d8d469",
  "requestId": "req_011Cb2YRjfp2e9trXg8FfTCu",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8000c723-f085-415c-aa1b-6a850a6fd0e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "ee553895-1021-4931-aae1-4600fac1ac8a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012q5EDVRG3tAcogatXYgdUk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1788,
      "cache_read_input_tokens": 17128,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1788,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-14T13:30:19.187Z_

<details><summary>↩ Tool result · reported error · `toolu_01WevThMFCZhFerqj6BknnsR`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8000c723-f085-415c-aa1b-6a850a6fd0e8",
  "isSidechain": true,
  "promptId": "873d52d2-4b2b-4bc2-850b-aec21329b090",
  "agentId": "aaafa5e9203d8d469",
  "type": "user",
  "uuid": "d3085dfd-a046-4805-921d-3e3b1c149c9c",
  "toolUseResult": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing.",
  "sourceToolAssistantUUID": "8000c723-f085-415c-aa1b-6a850a6fd0e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "ee553895-1021-4931-aae1-4600fac1ac8a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-14T13:30:19.453Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CgzF1Fw1Vu4dTFwrC8AHLR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/src/llm_agent.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d3085dfd-a046-4805-921d-3e3b1c149c9c",
  "isSidechain": true,
  "agentId": "aaafa5e9203d8d469",
  "requestId": "req_011Cb2YRjfp2e9trXg8FfTCu",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "90409e72-a041-4aed-98a2-82ef6c6a21e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "ee553895-1021-4931-aae1-4600fac1ac8a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012q5EDVRG3tAcogatXYgdUk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1788,
      "cache_read_input_tokens": 17128,
      "output_tokens": 253,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1788
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 253,
          "cache_read_input_tokens": 17128,
          "cache_creation_input_tokens": 1788,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1788,
            "ephemeral_1h_input_tokens": 0
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

_source line 11 · 2026-05-14T13:30:19.459Z_

<details><summary>↩ Tool result · `toolu_01CgzF1Fw1Vu4dTFwrC8AHLR`</summary>

```text
1	"""LLM Agent: Qwen2.5-7B-Instruct ReAct agent for ScienceWorld.
2	
3	Supports vLLM serving (default) or HuggingFace transformers local inference.
4	Provides:
5	  - select_action_react(): standard ReAct single-action selection
6	  - generate_candidate_actions(): top-n candidate generation for deterministic routing
7	
8	Usage:
9	  agent = LLMAgent(model_path="/root/autodl-tmp/models/Qwen2.5-7B-Instruct", gpu_id=0)
10	  action = agent.select_action_react(obs, valid_actions, history)
11	"""
12	
13	import os
14	import re
15	import glob
16	import json
17	import time
18	from typing import List, Optional, Tuple
19	
20	# Detect model path: ModelScope or HuggingFace naming conventions
21	MODEL_SEARCH_PATHS = [
22	    "/root/autodl-tmp/models/Qwen2.5-7B-Instruct",
23	    "/root/autodl-tmp/models/Qwen/Qwen2.5-7B-Instruct",
24	    "/root/autodl-tmp/models/Qwen/Qwen2___5-7B-Instruct",
25	    "/root/autodl-tmp/models/qwen/Qwen2.5-7B-Instruct",
26	    "/root/autodl-tmp/.hf_cache/models--Qwen--Qwen2.5-7B-Instruct",
27	]
28	
29	
30	def find_model_path(hint: Optional[str] = None) -> str:
31	    """Find Qwen2.5-7B-Instruct model path on disk."""
32	    if hint and os.path.isdir(hint):
33	        return hint
34	    for p in MODEL_SEARCH_PATHS:
35	        if os.path.isdir(p):
36	            return p
37	    # Glob fallback
38	    for pattern in ["/root/autodl-tmp/models/**/Qwen2*7B*Instruct",
39	                    "/root/autodl-tmp/.hf_cache/**/Qwen2*7B*"]:
40	        matches = glob.glob(pattern, recursive=True)
41	        if matches:
42	            return matches[0]
43	    raise FileNotFoundError(
44	        "Cannot find Qwen2.5-7B-Instruct. Searched: " + str(MODEL_SEARCH_PATHS)
45	    )
46	
47	
48	# ---------------------------------------------------------------------------
49	# Prompt templates
50	# ---------------------------------------------------------------------------
51	
52	SYSTEM_PROMPT = """You are an agent interacting with a ScienceWorld text environment. Your goal is to complete the given task by choosing actions from the available action list.
53	
54	Use the following format for each step:
55	Thought: &lt;your reasoning about what to do next>
56	Action: &lt;exact action string from the valid actions list>
57	
58	Rules:
59	- You MUST choose an action from the valid actions list. Do not invent actions.
60	- Think step by step about what physical/scientific process is needed.
61	- Pay attention to the current observation for clues about object states."""
62	
63	REACT_USER_TEMPLATE = """Current observation:
64	{observation}
65	
66	Valid actions:
67	{valid_actions_str}
68	
69	Previous actions taken: {history_str}
70	
71	Choose your next action."""
72	
73	CANDIDATE_USER_TEMPLATE = """Current observation:
74	{observation}
75	
76	Valid actions:
77	{valid_actions_str}
78	
79	Previous actions taken: {history_str}
80	
81	Generate the top {n} most promising actions from the valid actions list, ranked by how likely they are to make progress on the task. Output exactly {n} actions, one per line, in this format:
82	1. &lt;action>
83	2. &lt;action>
84	3. &lt;action>"""
85	
86	
87	def _format_history(history: List[dict], last_k: int = 10) -> str:
88	    """Format recent action history for prompt."""
89	    if not history:
90	        return "(none)"
91	    recent = history[-last_k:]
92	    parts = []
93	    for h in recent:
94	        if isinstance(h, dict):
95	            parts.append(f"- {h.get('action', str(h))}")
96	        else:
97	            parts.append(f"- {h}")
98	    return "\n".join(parts)
99	
100	
101	def _format_valid_actions(actions: List[str], max_show: int = 50) -> str:
102	    """Format valid actions list, truncating if too long."""
103	    if len(actions) <= max_show:
104	        return "\n".join(f"  [{i}] {a}" for i, a in enumerate(actions))
105	    shown = actions[:max_show]
106	    return "\n".join(f"  [{i}] {a}" for i, a in enumerate(shown)) + \
107	           f"\n  ... and {len(actions) - max_show} more actions"
108	
109	
110	def parse_action(text: str, valid_actions: List[str]) -> Optional[str]:
111	    """Parse LLM output to extract action. Tries multiple patterns."""
112	    # Pattern 1: "Action: &lt;action>"
113	    m = re.search(r"Action:\s*(.+?)(?:\n|$)", text, re.IGNORECASE)
114	    if m:
115	        action_str = m.group(1).strip().strip('"').strip("'")
116	        if action_str in valid_actions:
117	            return action_str
118	        # Fuzzy match: case-insensitive
119	        for va in valid_actions:
120	            if va.lower() == action_str.lower():
121	                return va
122	
123	    # Pattern 2: Exact match anywhere in text
124	    for va in valid_actions:
125	        if va in text:
126	            return va
127	
128	    # Pattern 3: Bracketed index "[0]", "[1]" etc.
129	    m = re.search(r"\[(\d+)\]", text)
130	    if m:
131	        idx = int(m.group(1))
132	        if 0 <= idx < len(valid_actions):
133	            return valid_actions[idx]
134	
135	    return None
136	
137	
138	def parse_candidates(text: str, valid_actions: List[str], n: int) -> List[str]:
139	    """Parse top-n candidates from LLM output."""
140	    candidates = []
141	    # Pattern: "1. &lt;action>" or "1: &lt;action>"
142	    for line in text.split("\n"):
143	        m = re.match(r"\d+[.):\s]+(.+)", line.strip())
144	        if m:
145	            action_str = m.group(1).strip().strip('"').strip("'")
146	            matched = None
147	            if action_str in valid_actions:
148	                matched = action_str
149	            else:
150	                for va in valid_actions:
151	                    if va.lower() == action_str.lower():
152	                        matched = va
153	                        break
154	            if matched and matched not in candidates:
155	                candidates.append(matched)
156	
157	    # If we didn't get enough, try Action: pattern
158	    if len(candidates) < n:
159	        for va in valid_actions:
160	            if va in text and va not in candidates:
161	                candidates.append(va)
162	                if len(candidates) >= n:
163	                    break
164	
165	    return candidates[:n]
166	
167	
168	class LLMAgent:
169	    """ReAct agent using Qwen2.5-7B-Instruct."""
170	
171	    def __init__(
172	        self,
173	        model_path: Optional[str] = None,
174	        use_vllm: bool = True,
175	        gpu_id: int = 0,
176	        max_new_tokens: int = 256,
177	        temperature: float = 0.3,
178	    ):
179	        self.model_path = find_model_path(model_path)
180	        self.use_vllm = use_vllm
181	        self.gpu_id = gpu_id
182	        self.max_new_tokens = max_new_tokens
183	        self.temperature = temperature
184	        self._model = None
185	        self._tokenizer = None
186	        self._llm = None  # vLLM engine
187	
188	        print(f"[LLMAgent] Model path: {self.model_path}")
189	        print(f"[LLMAgent] Backend: {'vLLM' if use_vllm else 'HF transformers'}, GPU: {gpu_id}")
190	
191	    def _load_vllm(self):
192	        if self._llm is not None:
193	            return
194	        from vllm import LLM, SamplingParams
195	        os.environ["CUDA_VISIBLE_DEVICES"] = str(self.gpu_id)
196	        self._llm = LLM(
197	            model=self.model_path,
198	            tensor_parallel_size=1,
199	            gpu_memory_utilization=0.85,
200	            max_model_len=4096,
201	            trust_remote_code=True,
202	        )
203	        self._SamplingParams = SamplingParams
204	
205	    def _load_hf(self):
206	        if self._model is not None:
207	            return
208	        import torch
209	        from transformers import AutoModelForCausalLM, AutoTokenizer
210	        self._tokenizer = AutoTokenizer.from_pretrained(
211	            self.model_path, trust_remote_code=True
212	        )
213	        self._model = AutoModelForCausalLM.from_pretrained(
214	            self.model_path,
215	            torch_dtype=torch.float16,
216	            device_map=f"cuda:{self.gpu_id}",
217	            trust_remote_code=True,
218	        )
219	        self._model.eval()
220	
221	    def _generate(self, messages: List[dict], temperature: Optional[float] = None) -> str:
222	        """Generate text from chat messages."""
223	        temp = temperature if temperature is not None else self.temperature
224	        if self.use_vllm:
225	            return self._generate_vllm(messages, temp)
226	        else:
227	            return self._generate_hf(messages, temp)
228	
229	    def _generate_vllm(self, messages: List[dict], temperature: float) -> str:
230	        self._load_vllm()
231	        from vllm import SamplingParams
232	        # Build prompt from messages using chat template
233	        from transformers import AutoTokenizer
234	        if self._tokenizer is None:
235	            self._tokenizer = AutoTokenizer.from_pretrained(
236	                self.model_path, trust_remote_code=True
237	            )
238	        prompt = self._tokenizer.apply_chat_template(
239	            messages, tokenize=False, add_generation_prompt=True
240	        )
241	        params = SamplingParams(
242	            temperature=max(temperature, 0.01),
243	            max_tokens=self.max_new_tokens,
244	            stop=["Observation:", "\nObservation"],
245	        )
246	        outputs = self._llm.generate([prompt], params)
247	        return outputs[0].outputs[0].text.strip()
248	
249	    def _generate_hf(self, messages: List[dict], temperature: float) -> str:
250	        self._load_hf()
251	        import torch
252	        text = self._tokenizer.apply_chat_template(
253	            messages, tokenize=False, add_generation_prompt=True
254	        )
255	        inputs = self._tokenizer(text, return_tensors="pt").to(self._model.device)
256	        with torch.no_grad():
257	            outputs = self._model.generate(
258	                **inputs,
259	                max_new_tokens=self.max_new_tokens,
260	                temperature=max(temperature, 0.01),
261	                do_sample=temperature > 0,
262	                top_p=0.9,
263	            )
264	        new_tokens = outputs[0][inputs["input_ids"].shape[1]:]
265	        return self._tokenizer.decode(new_tokens, skip_special_tokens=True).strip()
266	
267	    def select_action_react(
268	        self,
269	        observation: str,
270	        valid_actions: List[str],
271	        history: List[dict],
272	    ) -> Tuple[str, str]:
273	        """Standard ReAct: LLM picks one action.
274	
275	        Returns (action, raw_llm_output).
276	        Falls back to first valid action if parsing fails.
277	        """
278	        messages = [
279	            {"role": "system", "content": SYSTEM_PROMPT},
280	            {"role": "user", "content": REACT_USER_TEMPLATE.format(
281	                observation=observation,
282	                valid_actions_str=_format_valid_actions(valid_actions),
283	                history_str=_format_history(history),
284	            )},
285	        ]
286	        raw = self._generate(messages)
287	        action = parse_action(raw, valid_actions)
288	        if action is None:
289	            action = valid_actions[0]  # fallback
290	        return action, raw
291	
292	    def generate_candidate_actions(
293	        self,
294	        observation: str,
295	        valid_actions: List[str],
296	        history: List[dict],
297	        n: int = 3,
298	    ) -> Tuple[List[str], str]:
299	        """Generate top-n candidate actions for deterministic evaluation.
300	
301	        Returns (list of actions, raw_llm_output).
302	        Pads with random valid actions if fewer than n parsed.
303	        """
304	        messages = [
305	            {"role": "system", "content": SYSTEM_PROMPT},
306	            {"role": "user", "content": CANDIDATE_USER_TEMPLATE.format(
307	                observation=observation,
308	                valid_actions_str=_format_valid_actions(valid_actions),
309	                history_str=_format_history(history),
310	                n=n,
311	            )},
312	        ]
313	        raw = self._generate(messages, temperature=0.5)
314	        candidates = parse_candidates(raw, valid_actions, n)
315	
316	        # Pad if needed
317	        import random
318	        remaining = [a for a in valid_actions if a not in candidates]
319	        while len(candidates) < n and remaining:
320	            pick = random.choice(remaining)
321	            candidates.append(pick)
322	            remaining.remove(pick)
323	
324	        return candidates, raw
325	
326	
327	def build_agent(args) -> LLMAgent:
328	    """Build LLMAgent from argparse namespace."""
329	    return LLMAgent(
330	        model_path=getattr(args, "model_path", None),
331	        use_vllm=getattr(args, "use_vllm", True),
332	        gpu_id=getattr(args, "gpu_id", 0),
333	    )
334	
335	
336	if __name__ == "__main__":
337	    import argparse
338	    parser = argparse.ArgumentParser()
339	    parser.add_argument("--model_path", type=str, default=None)
340	    parser.add_argument("--use_vllm", type=bool, default=True)
341	    parser.add_argument("--gpu_id", type=int, default=0)
342	    args = parser.parse_args()
343	    agent = build_agent(args)
344	    print(f"Agent initialized. Model: {agent.model_path}")
345	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "90409e72-a041-4aed-98a2-82ef6c6a21e5",
  "isSidechain": true,
  "promptId": "873d52d2-4b2b-4bc2-850b-aec21329b090",
  "agentId": "aaafa5e9203d8d469",
  "type": "user",
  "uuid": "e39aa4b8-6975-4bb2-ad51-32f826b4195c",
  "sourceToolAssistantUUID": "90409e72-a041-4aed-98a2-82ef6c6a21e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "ee553895-1021-4931-aae1-4600fac1ac8a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-14T13:30:21.331Z_

The math_counterfactual.py file doesn't exist. Let me search for files related to MATH counterfactual and also check for any existing ALFWorld code:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e39aa4b8-6975-4bb2-ad51-32f826b4195c",
  "isSidechain": true,
  "agentId": "aaafa5e9203d8d469",
  "requestId": "req_011Cb2YRtnVtSYaDKnAo1GLF",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "bc39cef1-dd6a-4c91-8f18-30f2d7c6f53b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "ee553895-1021-4931-aae1-4600fac1ac8a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HDfyrJQcLrX6kF18JoaGm3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 9310,
      "cache_read_input_tokens": 18916,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9310,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T13:30:22.239Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01AA46a8g5HVUoN1s4U13WhG`</summary>

```json
{
  "pattern": "**/*counterfactual*.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bc39cef1-dd6a-4c91-8f18-30f2d7c6f53b",
  "isSidechain": true,
  "agentId": "aaafa5e9203d8d469",
  "requestId": "req_011Cb2YRtnVtSYaDKnAo1GLF",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9b5a4c8b-3b53-4b43-8a03-ce001e0a107a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "ee553895-1021-4931-aae1-4600fac1ac8a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HDfyrJQcLrX6kF18JoaGm3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 9310,
      "cache_read_input_tokens": 18916,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9310,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T13:30:22.260Z_

<details><summary>↩ Tool result · `toolu_01AA46a8g5HVUoN1s4U13WhG`</summary>

```text
src/counterfactual_labeling.py
src/alfworld_counterfactual.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9b5a4c8b-3b53-4b43-8a03-ce001e0a107a",
  "isSidechain": true,
  "promptId": "873d52d2-4b2b-4bc2-850b-aec21329b090",
  "agentId": "aaafa5e9203d8d469",
  "type": "user",
  "uuid": "228c7831-8920-4270-926b-428bd4d611a4",
  "sourceToolAssistantUUID": "9b5a4c8b-3b53-4b43-8a03-ce001e0a107a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "ee553895-1021-4931-aae1-4600fac1ac8a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T13:30:22.443Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01MkLy4YLDG5VAbqEmPSiS8M`</summary>

```json
{
  "pattern": "**/*math*.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "228c7831-8920-4270-926b-428bd4d611a4",
  "isSidechain": true,
  "agentId": "aaafa5e9203d8d469",
  "requestId": "req_011Cb2YRtnVtSYaDKnAo1GLF",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8582de77-d5f2-41f1-adfd-4397d9560de4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "ee553895-1021-4931-aae1-4600fac1ac8a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HDfyrJQcLrX6kF18JoaGm3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 9310,
      "cache_read_input_tokens": 18916,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9310,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T13:30:22.456Z_

<details><summary>↩ Tool result · `toolu_01MkLy4YLDG5VAbqEmPSiS8M`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8582de77-d5f2-41f1-adfd-4397d9560de4",
  "isSidechain": true,
  "promptId": "873d52d2-4b2b-4bc2-850b-aec21329b090",
  "agentId": "aaafa5e9203d8d469",
  "type": "user",
  "uuid": "8dd2e8df-a8b4-4637-a08e-56c24cf00968",
  "sourceToolAssistantUUID": "8582de77-d5f2-41f1-adfd-4397d9560de4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "ee553895-1021-4931-aae1-4600fac1ac8a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-14T13:30:22.710Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01FHkozoQon1ZL2r4L2Nd4Wx`</summary>

```json
{
  "pattern": "**/*alfworld*.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8dd2e8df-a8b4-4637-a08e-56c24cf00968",
  "isSidechain": true,
  "agentId": "aaafa5e9203d8d469",
  "requestId": "req_011Cb2YRtnVtSYaDKnAo1GLF",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8e04bb18-6692-4fac-9d39-68169032f02f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "ee553895-1021-4931-aae1-4600fac1ac8a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HDfyrJQcLrX6kF18JoaGm3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 9310,
      "cache_read_input_tokens": 18916,
      "output_tokens": 312,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9310
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 312,
          "cache_read_input_tokens": 18916,
          "cache_creation_input_tokens": 9310,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9310,
            "ephemeral_1h_input_tokens": 0
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

_source line 18 · 2026-05-14T13:30:22.730Z_

<details><summary>↩ Tool result · `toolu_01FHkozoQon1ZL2r4L2Nd4Wx`</summary>

```text
src/alfworld_counterfactual.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8e04bb18-6692-4fac-9d39-68169032f02f",
  "isSidechain": true,
  "promptId": "873d52d2-4b2b-4bc2-850b-aec21329b090",
  "agentId": "aaafa5e9203d8d469",
  "type": "user",
  "uuid": "f5525d6a-a9b4-43a9-a131-14e2de94d171",
  "sourceToolAssistantUUID": "8e04bb18-6692-4fac-9d39-68169032f02f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "ee553895-1021-4931-aae1-4600fac1ac8a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-14T13:30:24.270Z_

Great! There's an ALFWorld counterfactual file. Let me read it and also check scienceworld_utils.py to understand the environment forking mechanism:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f5525d6a-a9b4-43a9-a131-14e2de94d171",
  "isSidechain": true,
  "agentId": "aaafa5e9203d8d469",
  "requestId": "req_011Cb2YS8WFHyVEAL6B38X6q",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "467162d9-10fc-4a9f-8014-7bb7371a545e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "ee553895-1021-4931-aae1-4600fac1ac8a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01MEHT4Lk3S4jiRcuuy2Gn4Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 434,
      "cache_read_input_tokens": 28226,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 434,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-14T13:30:24.425Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QFHb6fzgfam42dWpEU56nu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/src/alfworld_counterfactual.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "467162d9-10fc-4a9f-8014-7bb7371a545e",
  "isSidechain": true,
  "agentId": "aaafa5e9203d8d469",
  "requestId": "req_011Cb2YS8WFHyVEAL6B38X6q",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d6ec1a22-0263-47e4-a6e1-f7a13274cf48",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "ee553895-1021-4931-aae1-4600fac1ac8a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01MEHT4Lk3S4jiRcuuy2Gn4Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 434,
      "cache_read_input_tokens": 28226,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 434,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-14T13:30:24.431Z_

<details><summary>↩ Tool result · `toolu_01QFHb6fzgfam42dWpEU56nu`</summary>

```text
1	"""ALFWorld counterfactual labeling pipeline.
2	
3	Runs two agents per task:
4	  - Internal: Qwen2.5-7B ReAct agent (LLM-only decision making)
5	  - Deterministic: ALFWorld HandCodedTWAgent (heuristic PDDL-based expert)
6	
7	Produces episode-level labels: det-preferred / internal-preferred / no-preference.
8	Output: JSONL with unified format for multi-env router training.
9	"""
10	
11	import argparse
12	import json
13	import os
14	import random
15	import sys
16	import time
17	from collections import Counter
18	from typing import List, Dict, Any, Optional, Tuple
19	
20	import textworld
21	import textworld.gym
22	from alfworld.agents.environment.alfred_tw_env import AlfredDemangler, AlfredInfos
23	from alfworld.agents.expert.handcoded_expert_tw import HandCodedTWAgent
24	
25	sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
26	from llm_agent import LLMAgent, find_model_path
27	
28	# ---------------------------------------------------------------------------
29	# ALFWorld-specific prompts
30	# ---------------------------------------------------------------------------
31	
32	ALFWORLD_SYSTEM_PROMPT = """You are an agent in a household environment (ALFWorld). You must complete a given task by choosing actions from the available action list.
33	
34	Use the following format for each step:
35	Thought: &lt;your reasoning about what to do next>
36	Action: &lt;exact action string from the valid actions list>
37	
38	Rules:
39	- You MUST choose an action from the valid actions list. Do not invent actions.
40	- Common actions: go to &lt;receptacle>, take &lt;obj> from &lt;receptacle>, put &lt;obj> in/on &lt;receptacle>, open/close &lt;receptacle>, use &lt;obj>, clean/heat/cool &lt;obj> with &lt;receptacle>, examine &lt;obj/receptacle>, look, inventory.
41	- Think step by step: first locate the target object, then perform required operations (clean/heat/cool if needed), then place it at the destination."""
42	
43	ALFWORLD_REACT_TEMPLATE = """Current observation:
44	{observation}
45	
46	Your task: {task_desc}
47	
48	Valid actions:
49	{valid_actions_str}
50	
51	Previous actions taken: {history_str}
52	
53	Choose your next action."""
54	
55	# ---------------------------------------------------------------------------
56	# Task type constants
57	# ---------------------------------------------------------------------------
58	
59	TASK_TYPES = [
60	    "pick_and_place",
61	    "pick_clean_then_place",
62	    "pick_heat_then_place",
63	    "pick_cool_then_place",
64	    "look_at_obj_in_light",
65	    "pick_two_obj_and_place",
66	]
67	
68	
69	def extract_task_type(game_dir: str) -> str:
70	    """Extract task type from game directory name."""
71	    dirname = os.path.basename(os.path.dirname(game_dir))
72	    for tt in TASK_TYPES:
73	        if dirname.startswith(tt):
74	            return tt
75	    return "unknown"
76	
77	
78	def extract_task_desc(obs: str) -> str:
79	    """Extract task description from initial observation."""
80	    if "Your task is to:" in obs:
81	        return obs.split("Your task is to:")[-1].strip().rstrip(".")
82	    return ""
83	
84	
85	def collect_game_files(data_root: str, split: str = "valid_seen",
86	                       task_types: Optional[List[str]] = None,
87	                       max_per_type: int = 0) -> List[Dict[str, str]]:
88	    """Collect game files from ALFWorld data directory.
89	
90	    Returns list of dicts with keys: game_path, task_type, task_id, game_dir.
91	    """
92	    split_path = os.path.join(data_root, split)
93	    if not os.path.exists(split_path):
94	        raise FileNotFoundError(f"Split path not found: {split_path}")
95	
96	    games = []
97	    type_counts = Counter()
98	
99	    for task_dir in sorted(os.listdir(split_path)):
100	        task_type = None
101	        for tt in TASK_TYPES:
102	            if task_dir.startswith(tt):
103	                task_type = tt
104	                break
105	        if task_type is None:
106	            continue
107	        if task_types and task_type not in task_types:
108	            continue
109	        if max_per_type > 0 and type_counts[task_type] >= max_per_type:
110	            continue
111	
112	        full_dir = os.path.join(split_path, task_dir)
113	        trials = [d for d in os.listdir(full_dir) if d.startswith("trial_")]
114	        if not trials:
115	            continue
116	
117	        trial_dir = os.path.join(full_dir, trials[0])
118	        game_path = os.path.join(trial_dir, "game.tw-pddl")
119	        if not os.path.exists(game_path):
120	            continue
121	
122	        games.append({
123	            "game_path": game_path,
124	            "task_type": task_type,
125	            "task_id": f"{task_dir}/{trials[0]}",
126	            "game_dir": trial_dir,
127	        })
128	        type_counts[task_type] += 1
129	
130	    return games
131	
132	
133	# ---------------------------------------------------------------------------
134	# Environment helpers
135	# ---------------------------------------------------------------------------
136	
137	def make_env(game_path: str, max_steps: int = 50):
138	    """Create a TextWorld gym env for a single ALFWorld game."""
139	    request_infos = textworld.EnvInfos(
140	        won=True,
141	        admissible_commands=True,
142	        facts=True,
143	        extras=["gamefile"],
144	    )
145	    env_id = textworld.gym.register_games(
146	        [game_path],
147	        request_infos,
148	        batch_size=1,
149	        max_episode_steps=max_steps,
150	        wrappers=[AlfredDemangler, AlfredInfos],
151	    )
152	    return textworld.gym.make(env_id)
153	
154	
155	def unpack_obs(obs, infos) -> Tuple[str, List[str], list, bool]:
156	    """Unpack batched gym output to single-game values."""
157	    obs_text = obs[0] if isinstance(obs, (tuple, list)) else obs
158	    admissible = infos["admissible_commands"][0]
159	    facts = infos.get("facts", [[]])[0]
160	    won = infos["won"][0] if isinstance(infos["won"], list) else infos["won"]
161	    return obs_text, admissible, facts, won
162	
163	
164	def make_game_state(obs_text: str, admissible: List[str], facts: list) -> dict:
165	    """Construct game_state dict expected by HandCodedTWAgent."""
166	    return {
167	        "feedback": obs_text,
168	        "admissible_commands": admissible,
169	        "facts": facts,
170	    }
171	
172	
173	# ---------------------------------------------------------------------------
174	# LLM agent wrapper for ALFWorld
175	# ---------------------------------------------------------------------------
176	
177	def _format_history(history: List[dict], last_k: int = 10) -> str:
178	    if not history:
179	        return "(none)"
180	    recent = history[-last_k:]
181	    return "\n".join(f"- {h.get('action', str(h))}" for h in recent)
182	
183	
184	def _format_valid_actions(actions: List[str], max_show: int = 40) -> str:
185	    if len(actions) <= max_show:
186	        return "\n".join(f"  [{i}] {a}" for i, a in enumerate(actions))
187	    shown = actions[:max_show]
188	    return "\n".join(f"  [{i}] {a}" for i, a in enumerate(shown)) + \
189	           f"\n  ... and {len(actions) - max_show} more actions"
190	
191	
192	def parse_action_alfworld(text: str, valid_actions: List[str]) -> Optional[str]:
193	    """Parse LLM output to extract action for ALFWorld."""
194	    import re
195	    # Pattern: "Action: &lt;action>"
196	    m = re.search(r"Action:\s*(.+?)(?:\n|$)", text, re.IGNORECASE)
197	    if m:
198	        action_str = m.group(1).strip().strip('"').strip("'")
199	        if action_str in valid_actions:
200	            return action_str
201	        # Fuzzy match
202	        action_lower = action_str.lower()
203	        for va in valid_actions:
204	            if va.lower() == action_lower:
205	                return va
206	        # Substring match
207	        for va in valid_actions:
208	            if action_lower in va.lower() or va.lower() in action_lower:
209	                return va
210	
211	    # Fallback: check if any valid action appears in the text
212	    for va in valid_actions:
213	        if va in text:
214	            return va
215	
216	    return None
217	
218	
219	def llm_select_action(agent: LLMAgent, obs: str, valid_actions: List[str],
220	                       history: List[dict], task_desc: str) -> Tuple[str, str]:
221	    """Use LLM to select an action via ReAct prompting."""
222	    messages = [
223	        {"role": "system", "content": ALFWORLD_SYSTEM_PROMPT},
224	        {"role": "user", "content": ALFWORLD_REACT_TEMPLATE.format(
225	            observation=obs,
226	            task_desc=task_desc,
227	            valid_actions_str=_format_valid_actions(valid_actions),
228	            history_str=_format_history(history),
229	        )},
230	    ]
231	    raw = agent._generate(messages)
232	    action = parse_action_alfworld(raw, valid_actions)
233	    if action is None:
234	        action = valid_actions[0]
235	    return action, raw
236	
237	
238	# ---------------------------------------------------------------------------
239	# Episode runners
240	# ---------------------------------------------------------------------------
241	
242	def run_internal_episode(game_info: dict, agent: LLMAgent,
243	                         max_steps: int = 50) -> dict:
244	    """Run an episode with LLM ReAct agent."""
245	    env = make_env(game_info["game_path"], max_steps)
246	    trajectory = []
247	    try:
248	        obs, infos = env.reset()
249	        obs_text, admissible, facts, won = unpack_obs(obs, infos)
250	        task_desc = extract_task_desc(obs_text)
251	        history = []
252	
253	        for step in range(max_steps):
254	            action, raw_output = llm_select_action(
255	                agent, obs_text, admissible, history, task_desc
256	            )
257	            trajectory.append({
258	                "step": step,
259	                "observation": obs_text[:500],
260	                "thought": raw_output[:300],
261	                "action": action,
262	                "reward": 0,
263	            })
264	            history.append({"action": action, "obs": obs_text[:200]})
265	
266	            obs, score, done, infos = env.step([action])
267	            obs_text, admissible, facts, won = unpack_obs(obs, infos)
268	            trajectory[-1]["reward"] = score
269	
270	            if done or won:
271	                break
272	
273	        return {
274	            "trajectory": trajectory,
275	            "success": bool(won),
276	            "n_steps": len(trajectory),
277	            "score": 1.0 if won else 0.0,
278	        }
279	    finally:
280	        env.close()
281	
282	
283	def run_deterministic_episode(game_info: dict, max_steps: int = 50) -> dict:
284	    """Run an episode with HandCodedTWAgent (heuristic expert)."""
285	    env = make_env(game_info["game_path"], max_steps)
286	    expert = HandCodedTWAgent(max_steps=max_steps)
287	    trajectory = []
288	
289	    try:
290	        obs, infos = env.reset()
291	        obs_text, admissible, facts, won = unpack_obs(obs, infos)
292	
293	        expert.reset(game=game_info["game_path"])
294	        game_state = make_game_state(obs_text, admissible, facts)
295	
296	        last_action = ""
297	        reward = 0
298	        done = False
299	
300	        for step in range(max_steps):
301	            try:
302	                action = expert.act(game_state, reward, done, last_action)
303	            except Exception:
304	                # Expert failed or timed out - pick random admissible action
305	                action = random.choice(admissible) if admissible else "look"
306	
307	            if action not in admissible:
308	                action = random.choice(admissible) if admissible else "look"
309	
310	            trajectory.append({
311	                "step": step,
312	                "observation": obs_text[:500],
313	                "thought": f"[expert-heuristic] {action}",
314	                "action": action,
315	                "reward": 0,
316	            })
317	
318	            obs, score, done, infos = env.step([action])
319	            obs_text, admissible, facts, won = unpack_obs(obs, infos)
320	            game_state = make_game_state(obs_text, admissible, facts)
321	
322	            trajectory[-1]["reward"] = score
323	            last_action = action
324	            reward = score
325	
326	            if done or won:
327	                break
328	
329	        return {
330	            "trajectory": trajectory,
331	            "success": bool(won),
332	            "n_steps": len(trajectory),
333	            "score": 1.0 if won else 0.0,
334	        }
335	    finally:
336	        env.close()
337	
338	
339	# ---------------------------------------------------------------------------
340	# Labeling
341	# ---------------------------------------------------------------------------
342	
343	def compute_label(internal: dict, deterministic: dict) -> str:
344	    if deterministic["success"] and not internal["success"]:
345	        return "det-preferred"
346	    elif internal["success"] and not deterministic["success"]:
347	        return "internal-preferred"
348	    else:
349	        return "no-preference"
350	
351	
352	# ---------------------------------------------------------------------------
353	# Main pipeline
354	# ---------------------------------------------------------------------------
355	
356	def run_pipeline(args):
357	    data_root = os.path.expanduser(args.data_root)
358	    games = collect_game_files(
359	        data_root,
360	        split=args.split,
361	        task_types=args.task_types.split(",") if args.task_types else None,
362	        max_per_type=args.max_per_type,
363	    )
364	
365	    if args.n_tasks > 0:
366	        games = games[:args.n_tasks]
367	
368	    print(f"=== ALFWorld CF Labeling ===")
369	    print(f"Split: {args.split} | Tasks: {len(games)} | Max steps: {args.max_steps}")
370	    print(f"GPU: {args.gpu_id} | vLLM: {not args.no_vllm}")
371	
372	    agent = LLMAgent(
373	        model_path=args.model_path,
374	        use_vllm=not args.no_vllm,
375	        gpu_id=args.gpu_id,
376	    )
377	
378	    os.makedirs(os.path.dirname(args.output) or ".", exist_ok=True)
379	
380	    label_counts = Counter()
381	    total_time = 0
382	    results = []
383	
384	    for i, game in enumerate(games):
385	        t0 = time.time()
386	        print(f"\n--- [{i+1}/{len(games)}] {game['task_type']}: {game['task_id'][:60]} ---")
387	
388	        # Run internal (LLM)
389	        internal_result = run_internal_episode(game, agent, args.max_steps)
390	        print(f"  Internal: {'SUCCESS' if internal_result['success'] else 'FAIL'} "
391	              f"({internal_result['n_steps']} steps)")
392	
393	        # Run deterministic (expert)
394	        det_result = run_deterministic_episode(game, args.max_steps)
395	        print(f"  Deterministic: {'SUCCESS' if det_result['success'] else 'FAIL'} "
396	              f"({det_result['n_steps']} steps)")
397	
398	        label = compute_label(internal_result, det_result)
399	        label_counts[label] += 1
400	        elapsed = round(time.time() - t0, 1)
401	        total_time += elapsed
402	
403	        task_desc = extract_task_desc(
404	            internal_result["trajectory"][0]["observation"] if internal_result["trajectory"] else ""
405	        )
406	
407	        record = {
408	            "episode_id": f"alfworld_{game['task_type']}_{i:03d}",
409	            "environment": "alfworld",
410	            "task_type": game["task_type"],
411	            "task_id": game["task_id"],
412	            "task_desc": task_desc,
413	            "internal": internal_result,
414	            "deterministic": det_result,
415	            "label": label,
416	            "metadata": {
417	                "subtask_type": game["task_type"],
418	                "split": args.split,
419	                "time_s": elapsed,
420	            },
421	        }
422	        results.append(record)
423	
424	        with open(args.output, "a") as f:
425	            f.write(json.dumps(record, default=str) + "\n")
426	
427	        print(f"  Label: {label} | Time: {elapsed}s")
428	
429	    # Summary
430	    print(f"\n{'='*50}")
431	    print(f"=== ALFWorld CF Labeling Summary ===")
432	    print(f"Tasks: {len(games)}")
433	    print(f"Labels: {dict(label_counts)}")
434	    int_success = sum(1 for r in results if r["internal"]["success"])
435	    det_success = sum(1 for r in results if r["deterministic"]["success"])
436	    print(f"Internal success rate: {int_success}/{len(results)} "
437	          f"({100*int_success/len(results):.1f}%)" if results else "")
438	    print(f"Deterministic success rate: {det_success}/{len(results)} "
439	          f"({100*det_success/len(results):.1f}%)" if results else "")
440	    print(f"Total time: {total_time:.0f}s")
441	    print(f"Output: {args.output}")
442	    print(f"{'='*50}")
443	
444	    return results
445	
446	
447	def main():
448	    parser = argparse.ArgumentParser(
449	        description="ALFWorld counterfactual labeling pipeline"
450	    )
451	    parser.add_argument("--data_root", type=str,
452	                        default="/root/.cache/alfworld/json_2.1.1",
453	                        help="ALFWorld data root")
454	    parser.add_argument("--split", type=str, default="valid_seen")
455	    parser.add_argument("--task_types", type=str, default=None,
456	                        help="Comma-separated task types to include")
457	    parser.add_argument("--max_per_type", type=int, default=0,
458	                        help="Max tasks per type (0=all)")
459	    parser.add_argument("--n_tasks", type=int, default=0,
460	                        help="Total tasks to run (0=all)")
461	    parser.add_argument("--max_steps", type=int, default=50)
462	    parser.add_argument("--gpu_id", type=int, default=1)
463	    parser.add_argument("--model_path", type=str, default=None)
464	    parser.add_argument("--no_vllm", action="store_true", default=False)
465	    parser.add_argument("--output", type=str,
466	                        default="data/alfworld-counterfactual/episodes.jsonl")
467	    parser.add_argument("--seed", type=int, default=42)
468	    args = parser.parse_args()
469	
470	    random.seed(args.seed)
471	    run_pipeline(args)
472	
473	
474	if __name__ == "__main__":
475	    main()
476	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d6ec1a22-0263-47e4-a6e1-f7a13274cf48",
  "isSidechain": true,
  "promptId": "873d52d2-4b2b-4bc2-850b-aec21329b090",
  "agentId": "aaafa5e9203d8d469",
  "type": "user",
  "uuid": "711cc434-bb32-4937-8284-6339201e5604",
  "sourceToolAssistantUUID": "d6ec1a22-0263-47e4-a6e1-f7a13274cf48",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "ee553895-1021-4931-aae1-4600fac1ac8a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-14T13:30:24.596Z_

<details open><summary>🔧 Tool call — Read · `toolu_019gSgztNgBqMSZf6jHodnqG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/src/scienceworld_utils.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "711cc434-bb32-4937-8284-6339201e5604",
  "isSidechain": true,
  "agentId": "aaafa5e9203d8d469",
  "requestId": "req_011Cb2YS8WFHyVEAL6B38X6q",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0ca4d36a-5823-41af-b965-78c8091c02b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "ee553895-1021-4931-aae1-4600fac1ac8a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01MEHT4Lk3S4jiRcuuy2Gn4Z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 434,
      "cache_read_input_tokens": 28226,
      "output_tokens": 204,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 434
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 204,
          "cache_read_input_tokens": 28226,
          "cache_creation_input_tokens": 434,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 434,
            "ephemeral_1h_input_tokens": 0
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

_source line 23 · 2026-05-14T13:30:24.600Z_

<details><summary>↩ Tool result · `toolu_019gSgztNgBqMSZf6jHodnqG`</summary>

```text
1	"""ScienceWorld environment utilities: creation, forking via action-replay, episode logging.
2	
3	Dependencies: scienceworld (pip install scienceworld)
4	Key constraint: ScienceWorld uses py4j → each env is a separate JVM process.
5	Fork = new JVM instance + replay all historical actions.
6	"""
7	
8	import time
9	import os
10	import traceback
11	from typing import List, Tuple, Optional, Dict, Any
12	
13	import scienceworld
14	
15	# ---------------------------------------------------------------------------
16	# Task type constants — update after running get_task_types() on the server
17	# ---------------------------------------------------------------------------
18	STRONG_TASKS = [
19	    "boil",
20	    "melt",
21	    "change-the-state-of-matter-of",
22	]
23	MEDIUM_TASKS = [
24	    "chemistry-mix-paint-secondary-color",
25	]
26	WEAK_TASKS = [
27	    "grow-plant",
28	]
29	ALL_MVP_TASKS = STRONG_TASKS + MEDIUM_TASKS + WEAK_TASKS
30	
31	
32	def get_task_types() -> List[str]:
33	    """Return all ScienceWorld task type names."""
34	    env = scienceworld.ScienceWorldEnv("")
35	    try:
36	        names = env.get_task_names()
37	    finally:
38	        env.close()
39	    return list(names)
40	
41	
42	def get_max_variations(task_name: str) -> int:
43	    """Return the number of available variations for a task type."""
44	    env = scienceworld.ScienceWorldEnv("")
45	    try:
46	        n = env.get_max_variations(task_name)
47	        return int(n)
48	    except Exception:
49	        return 100
50	    finally:
51	        env.close()
52	
53	
54	def create_env(task_name: str, variation_idx: int = 0,
55	               simplification_str: str = "") -> scienceworld.ScienceWorldEnv:
56	    """Create and initialize a ScienceWorld environment."""
57	    env = scienceworld.ScienceWorldEnv(task_name, envStepLimit=100)
58	    env.load(task_name, variation_idx, simplificationStr=simplification_str)
59	    return env
60	
61	
62	def reset_env(env: scienceworld.ScienceWorldEnv) -> Tuple[str, dict]:
63	    """Reset environment, return (observation, info). Tracks score via info dict."""
64	    result = env.reset()
65	    if isinstance(result, tuple):
66	        obs = str(result[0])
67	        info = result[1] if len(result) > 1 else {}
68	    else:
69	        obs = str(result)
70	        info = {}
71	    env._last_score = float(info.get("score", 0))
72	    return obs, info
73	
74	
75	def get_valid_actions(env: scienceworld.ScienceWorldEnv) -> List[str]:
76	    """Get current valid action list."""
77	    actions = env.get_valid_action_object_combinations()
78	    if isinstance(actions, list):
79	        return actions
80	    return list(actions)
81	
82	
83	def get_score(env: scienceworld.ScienceWorldEnv) -> float:
84	    """Get score cached from last step()/reset() info dict."""
85	    return getattr(env, "_last_score", 0.0)
86	
87	
88	def step_env(env: scienceworld.ScienceWorldEnv, action: str
89	             ) -> Tuple[str, float, bool, dict]:
90	    """Execute action, return (observation, reward, done, info). Updates cached score."""
91	    result = env.step(action)
92	    if isinstance(result, tuple) and len(result) >= 3:
93	        obs = str(result[0])
94	        reward = float(result[1])
95	        done = bool(result[2])
96	        info = result[3] if len(result) > 3 else {}
97	        env._last_score = float(info.get("score", 0))
98	        return obs, reward, done, info
99	    return str(result), 0.0, False, {}
100	
101	
102	def close_env(env: scienceworld.ScienceWorldEnv) -> None:
103	    """Safely close environment and release JVM resources."""
104	    try:
105	        env.close()
106	    except Exception:
107	        pass
108	
109	
110	# ---------------------------------------------------------------------------
111	# State forking via action-replay
112	# ---------------------------------------------------------------------------
113	
114	def fork_and_lookahead(
115	    task_name: str,
116	    variation_idx: int,
117	    action_history: List[str],
118	    candidate_action: str,
119	    simplification_str: str = "",
120	) -> Dict[str, Any]:
121	    """Fork environment state and evaluate a candidate action.
122	
123	    Creates a fresh JVM instance, replays action_history, then executes
124	    candidate_action. Returns dict with observation, score, score_delta,
125	    replay_success, and timing info. Always closes the forked env.
126	    """
127	    t0 = time.time()
128	    fork_env = None
129	    try:
130	        fork_env = create_env(task_name, variation_idx, simplification_str)
131	        reset_env(fork_env)
132	
133	        # Replay history
134	        replay_ok = True
135	        replay_errors = []
136	        score_before_candidate = 0.0
137	        for i, past_action in enumerate(action_history):
138	            try:
139	                step_env(fork_env, past_action)
140	            except Exception as e:
141	                replay_ok = False
142	                replay_errors.append({"step": i, "action": past_action, "error": str(e)})
143	
144	        score_before_candidate = get_score(fork_env)
145	
146	        # Execute candidate
147	        obs, reward, done, info = step_env(fork_env, candidate_action)
148	        score_after = get_score(fork_env)
149	        score_delta = score_after - score_before_candidate
150	
151	        elapsed = time.time() - t0
152	        return {
153	            "observation": obs,
154	            "score": score_after,
155	            "score_delta": score_delta,
156	            "score_before": score_before_candidate,
157	            "reward": reward,
158	            "done": done,
159	            "replay_success": replay_ok,
160	            "replay_errors": replay_errors,
161	            "elapsed_seconds": elapsed,
162	        }
163	    except Exception as e:
164	        elapsed = time.time() - t0
165	        return {
166	            "observation": "",
167	            "score": 0.0,
168	            "score_delta": 0.0,
169	            "score_before": 0.0,
170	            "reward": 0.0,
171	            "done": False,
172	            "replay_success": False,
173	            "replay_errors": [{"step": -1, "action": "fork_init", "error": str(e)}],
174	            "elapsed_seconds": elapsed,
175	        }
176	    finally:
177	        if fork_env is not None:
178	            close_env(fork_env)
179	
180	
181	def run_episode_with_logging(
182	    task_name: str,
183	    variation_idx: int = 0,
184	    max_steps: int = 100,
185	    action_selector=None,
186	    simplification_str: str = "",
187	) -> Dict[str, Any]:
188	    """Run a full episode, recording (action, obs, score) at each step.
189	
190	    Args:
191	        action_selector: callable(obs, valid_actions, history) -> action string.
192	            If None, picks first valid action (for testing).
193	
194	    Returns dict with steps list, final_score, total_time, etc.
195	    """
196	    env = create_env(task_name, variation_idx, simplification_str)
197	    obs, info = reset_env(env)
198	    initial_score = get_score(env)
199	
200	    steps = []
201	    action_history = []
202	    t0 = time.time()
203	
204	    for step_idx in range(max_steps):
205	        valid_actions = get_valid_actions(env)
206	        if not valid_actions:
207	            break
208	
209	        if action_selector is not None:
210	            action = action_selector(obs, valid_actions, action_history)
211	        else:
212	            action = valid_actions[0]
213	
214	        obs_new, reward, done, step_info = step_env(env, action)
215	        score = get_score(env)
216	
217	        steps.append({
218	            "step": step_idx,
219	            "action": action,
220	            "observation": obs_new,
221	            "score": score,
222	            "reward": reward,
223	            "done": done,
224	        })
225	        action_history.append(action)
226	        obs = obs_new
227	
228	        if done:
229	            break
230	
231	    total_time = time.time() - t0
232	    final_score = get_score(env)
233	    close_env(env)
234	
235	    return {
236	        "task_name": task_name,
237	        "variation_idx": variation_idx,
238	        "steps": steps,
239	        "action_history": action_history,
240	        "final_score": final_score,
241	        "initial_score": initial_score,
242	        "num_steps": len(steps),
243	        "total_time_seconds": total_time,
244	    }
245	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0ca4d36a-5823-41af-b965-78c8091c02b6",
  "isSidechain": true,
  "promptId": "873d52d2-4b2b-4bc2-850b-aec21329b090",
  "agentId": "aaafa5e9203d8d469",
  "type": "user",
  "uuid": "b89c968d-078a-4784-9fd3-f59c9d1c6065",
  "sourceToolAssistantUUID": "0ca4d36a-5823-41af-b965-78c8091c02b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "ee553895-1021-4931-aae1-4600fac1ac8a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-14T13:30:26.923Z_

Perfect! Now let me also check if there are any other related files that might show how the data is used for training:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b89c968d-078a-4784-9fd3-f59c9d1c6065",
  "isSidechain": true,
  "agentId": "aaafa5e9203d8d469",
  "requestId": "req_011Cb2YSHPHhK2szvFohnwMS",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a7a1c768-3230-4c49-8441-b9c629a71066",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "ee553895-1021-4931-aae1-4600fac1ac8a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019QFAuFHk1w5vH8mQWh2GKW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 8793,
      "cache_read_input_tokens": 28660,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8793,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-14T13:30:27.783Z_

<details open><summary>🔧 Tool call — Bash · `toolu_014beGbY1sKi6fgopqLWoHBF`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/src/ | head -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a7a1c768-3230-4c49-8441-b9c629a71066",
  "isSidechain": true,
  "agentId": "aaafa5e9203d8d469",
  "requestId": "req_011Cb2YSHPHhK2szvFohnwMS",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "dd6655a6-d393-48d5-8d01-041d59df5be3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "ee553895-1021-4931-aae1-4600fac1ac8a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019QFAuFHk1w5vH8mQWh2GKW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 8793,
      "cache_read_input_tokens": 28660,
      "output_tokens": 116,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8793
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 116,
          "cache_read_input_tokens": 28660,
          "cache_creation_input_tokens": 8793,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8793,
            "ephemeral_1h_input_tokens": 0
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

_source line 26 · 2026-05-14T13:30:27.887Z_

<details><summary>↩ Tool result · `toolu_014beGbY1sKi6fgopqLWoHBF`</summary>

```text
total 360
drwxr-xr-x  5 ubuntu ubuntu  4096 May 14 13:29 .
drwxr-xr-x 10 ubuntu ubuntu  4096 May 14 13:19 ..
-rw-r--r--  1 ubuntu ubuntu  5063 May 13 22:17 ablation_data_converter.py
-rw-r--r--  1 ubuntu ubuntu 10996 May 13 22:16 ablation_eval_common.py
-rw-r--r--  1 ubuntu ubuntu 12195 May 13 22:18 ablation_implicit_1_7b.py
-rw-r--r--  1 ubuntu ubuntu  8067 May 13 22:18 ablation_implicit_7b.py
-rw-r--r--  1 ubuntu ubuntu  5005 May 13 17:12 action_divergence_analysis.py
-rw-r--r--  1 ubuntu ubuntu 16531 May 14 13:29 alfworld_counterfactual.py
drwxr-xr-x  2 ubuntu ubuntu  4096 May 14 04:17 analysis
-rw-r--r--  1 ubuntu ubuntu  7237 May 13 05:02 analysis.py
-rw-r--r--  1 ubuntu ubuntu 12373 May 13 17:12 counterfactual_labeling.py
-rw-r--r--  1 ubuntu ubuntu  9794 May 14 00:46 death_aware_labeling.py
-rw-r--r--  1 ubuntu ubuntu 22053 May 13 20:50 death_decomposition.py
-rw-r--r--  1 ubuntu ubuntu 21371 May 13 21:01 episode_level_collection.py
-rw-r--r--  1 ubuntu ubuntu 26244 May 14 07:22 eval_end_to_end.py
-rw-r--r--  1 ubuntu ubuntu 17224 May 14 08:51 eval_implicit_router.py
drwxr-xr-x  2 ubuntu ubuntu  4096 May 14 04:31 evaluation
-rw-r--r--  1 ubuntu ubuntu 11969 May 13 04:54 llm_agent.py
-rw-r--r--  1 ubuntu ubuntu  9974 May 13 05:05 phase0_validate_forking.py
-rw-r--r--  1 ubuntu ubuntu 17609 May 13 07:46 phase1_signal.py
-rw-r--r--  1 ubuntu ubuntu 10267 May 13 22:15 plot_death_decomposition.py
-rw-r--r--  1 ubuntu ubuntu 10513 May 14 00:47 router_sft_eval.py
-rw-r--r--  1 ubuntu ubuntu 19589 May 13 22:16 router_sft_train.py
-rw-r--r--  1 ubuntu ubuntu 17754 May 13 23:36 routing_pattern_analysis.py
-rw-r--r--  1 ubuntu ubuntu 10610 May 13 21:21 rule_based_accuracy.py
-rw-r--r--  1 ubuntu ubuntu   156 May 14 04:17 rule_based_keywords.json
-rw-r--r--  1 ubuntu ubuntu   673 May 13 21:21 rule_based_keywords_v2.json
-rwxr-xr-x  1 ubuntu ubuntu  2773 May 13 05:05 run_all.sh
-rw-r--r--  1 ubuntu ubuntu  7516 May 13 05:05 scienceworld_utils.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dd6655a6-d393-48d5-8d01-041d59df5be3",
  "isSidechain": true,
  "promptId": "873d52d2-4b2b-4bc2-850b-aec21329b090",
  "agentId": "aaafa5e9203d8d469",
  "type": "user",
  "uuid": "c0f3f167-bd07-43bf-ae8e-f3f5bf5c636f",
  "sourceToolAssistantUUID": "dd6655a6-d393-48d5-8d01-041d59df5be3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "ee553895-1021-4931-aae1-4600fac1ac8a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-14T13:30:29.365Z_

Let me check a few more related files to understand the full pipeline better:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c0f3f167-bd07-43bf-ae8e-f3f5bf5c636f",
  "isSidechain": true,
  "agentId": "aaafa5e9203d8d469",
  "requestId": "req_011Cb2YSWdGKo2QaMctTnBFz",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "886dc4e3-244a-48ea-b469-063a9735f437",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "ee553895-1021-4931-aae1-4600fac1ac8a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UuoDA5s8h3eGkFQBkBuN9a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1083,
      "cache_read_input_tokens": 37453,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1083,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-14T13:30:30.499Z_

<details open><summary>🔧 Tool call — Read · `toolu_0154sjgtWTV51E2FZkbz7iqe`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/src/phase1_signal.py",
  "limit": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "886dc4e3-244a-48ea-b469-063a9735f437",
  "isSidechain": true,
  "agentId": "aaafa5e9203d8d469",
  "requestId": "req_011Cb2YSWdGKo2QaMctTnBFz",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ad06d3d1-cc4c-440f-988a-0ba07f2aedee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "ee553895-1021-4931-aae1-4600fac1ac8a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UuoDA5s8h3eGkFQBkBuN9a",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1083,
      "cache_read_input_tokens": 37453,
      "output_tokens": 215,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1083
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 215,
          "cache_read_input_tokens": 37453,
          "cache_creation_input_tokens": 1083,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1083,
            "ephemeral_1h_input_tokens": 0
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

_source line 29 · 2026-05-14T13:30:30.506Z_

<details open><summary>🔧 Tool call — Read · `toolu_017uTDCRpS8jcfPXvtXDQWTX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/src/death_aware_labeling.py",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad06d3d1-cc4c-440f-988a-0ba07f2aedee",
  "isSidechain": true,
  "agentId": "aaafa5e9203d8d469",
  "requestId": "req_011Cb2YSWdGKo2QaMctTnBFz",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "dda71cca-fe3f-4cc2-8132-a711a11bd8ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "ee553895-1021-4931-aae1-4600fac1ac8a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UuoDA5s8h3eGkFQBkBuN9a",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1083,
      "cache_read_input_tokens": 37453,
      "output_tokens": 215,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1083
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 215,
          "cache_read_input_tokens": 37453,
          "cache_creation_input_tokens": 1083,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1083,
            "ephemeral_1h_input_tokens": 0
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

_source line 30 · 2026-05-14T13:30:30.513Z_

<details><summary>↩ Tool result · `toolu_0154sjgtWTV51E2FZkbz7iqe`</summary>

```text
1	"""Phase 1: 3-way signal detection — always-internal vs always-deterministic vs oracle-routing.
2	
3	For each task type × episode:
4	  A) always-internal: ReAct LLM picks every action
5	  B) always-deterministic: LLM generates candidates, fork evaluates each, pick best score_delta
6	  C) oracle-routing: run both A and B, pick whichever has higher score_delta
7	
8	Usage:
9	  python src/phase1_signal.py --task_types "boil,melt" --episodes 20 --gpu_id 0
10	"""
11	
12	import argparse
13	import json
14	import os
15	import random
16	import sys
17	import time
18	from typing import List, Dict, Any, Optional
19	
20	sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
21	from scienceworld_utils import (
22	    create_env, reset_env, get_valid_actions, get_score,
23	    step_env, close_env, fork_and_lookahead, get_task_types,
24	    get_max_variations,
25	    STRONG_TASKS, MEDIUM_TASKS, WEAK_TASKS, ALL_MVP_TASKS,
26	)
27	from llm_agent import LLMAgent, find_model_path
28	
29	
30	def resolve_task_type(name: str) -> str:
31	    """Resolve a short task name to the actual ScienceWorld task name."""
32	    try:
33	        available = get_task_types()
34	    except Exception:
35	        return name
36	    if name in available:
37	        return name
38	    matches = [t for t in available if name.lower() in t.lower()]
39	    if matches:
40	        return matches[0]
41	    return name
42	
43	
44	def is_lethal(fr: Dict[str, Any]) -> bool:
45	    """Check if a fork result indicates a lethal action."""
46	    if fr["done"] and fr["score"] < 0:
47	        return True
48	    if fr["score"] <= -100:
49	        return True
50	    return False
51	
52	
53	def run_episode_always_internal(
54	    agent: LLMAgent,
55	    task_name: str,
56	    variation_idx: int,
57	    max_steps: int,
58	) -> Dict[str, Any]:
59	    """Mode A: LLM ReAct picks every action."""
60	    env = create_env(task_name, variation_idx)
61	    obs, _ = reset_env(env)
62	    initial_score = get_score(env)
63	
64	    steps = []
65	    action_history = []
66	    history_dicts = []
67	    t0 = time.time()
68	
69	    for step_idx in range(max_steps):
70	        valid_actions = get_valid_actions(env)
71	        if not valid_actions:
72	            break
73	
74	        action, raw_output = agent.select_action_react(obs, valid_actions, history_dicts)
75	        _remaining = list(valid_actions)
76	        for _retry in range(3):
77	            fr = fork_and_lookahead(task_name, variation_idx, action_history, action)
78	            if not is_lethal(fr):
79	                break
80	            _remaining = [a for a in _remaining if a != action]
81	            if not _remaining:
82	                break
83	            action, raw_output = agent.select_action_react(obs, _remaining, history_dicts)
84	
85	        score_before = get_score(env)
86	        obs_new, reward, done, info = step_env(env, action)
87	        score_after = get_score(env)
88	
89	        step_record = {
90	            "step": step_idx,
91	            "action": action,
92	            "modality": "internal",
93	            "score_before": score_before,
94	            "score_after": score_after,
95	            "score_delta": score_after - score_before,
96	            "observation": obs_new[:500],
97	            "llm_output": raw_output[:300],
98	        }
99	        steps.append(step_record)
100	        action_history.append(action)
101	        history_dicts.append({"action": action, "observation": obs_new[:200], "score": score_after})
102	        obs = obs_new
103	
104	        if done:
105	            break
106	
107	    final_score = get_score(env)
108	    close_env(env)
109	
110	    return {
111	        "mode": "always-internal",
112	        "task_name": task_name,
113	        "variation_idx": variation_idx,
114	        "final_score": final_score,
115	        "initial_score": initial_score,
116	        "num_steps": len(steps),
117	        "total_time_s": time.time() - t0,
118	        "steps": steps,
119	        "action_history": action_history,
120	    }
121	
122	
123	def run_episode_always_deterministic(
124	    agent: LLMAgent,
125	    task_name: str,
126	    variation_idx: int,
127	    max_steps: int,
128	    n_candidates: int = 3,
129	) -> Dict[str, Any]:
130	    """Mode B: LLM generates candidates, fork evaluates each, pick best."""
131	    env = create_env(task_name, variation_idx)
132	    obs, _ = reset_env(env)
133	    initial_score = get_score(env)
134	
135	    steps = []
136	    action_history = []
137	    history_dicts = []
138	    t0 = time.time()
139	
140	    for step_idx in range(max_steps):
141	        valid_actions = get_valid_actions(env)
142	        if not valid_actions:
143	            break
144	
145	        candidates, raw_output = agent.generate_candidate_actions(
146	            obs, valid_actions, history_dicts, n=n_candidates
147	        )
148	
149	        # Fork-evaluate each candidate (filter lethal)
150	        best_action = None
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ad06d3d1-cc4c-440f-988a-0ba07f2aedee",
  "isSidechain": true,
  "promptId": "873d52d2-4b2b-4bc2-850b-aec21329b090",
  "agentId": "aaafa5e9203d8d469",
  "type": "user",
  "uuid": "d63cce0d-37a4-4c72-ad1e-c13a6bdbd379",
  "sourceToolAssistantUUID": "ad06d3d1-cc4c-440f-988a-0ba07f2aedee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "ee553895-1021-4931-aae1-4600fac1ac8a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-14T13:30:30.516Z_

<details><summary>↩ Tool result · `toolu_017uTDCRpS8jcfPXvtXDQWTX`</summary>

```text
1	# Death-aware 3-label labeling for router SFT training.
2	# Reads episode JSONL files, classifies each episode as det-preferred / internal-preferred / no-preference
3	# based on death asymmetry (primary signal) and score comparison (secondary signal).
4	# Outputs step-level SFT triples: (observation, action_history) → label.
5	
6	import argparse
7	import json
8	import os
9	import sys
10	from collections import defaultdict
11	from typing import Dict, List, Any, Tuple
12	
13	DEATH_THRESHOLD = -100
14	
15	
16	def is_dead(final_score: float) -> bool:
17	    return final_score <= DEATH_THRESHOLD
18	
19	
20	def classify_episode(int_score: float, det_score: float) -> Tuple[str, str, str]:
21	    """Returns (label, reason, signal_source). Never discards."""
22	    int_died = is_dead(int_score)
23	    det_died = is_dead(det_score)
24	
25	    if int_died and not det_died:
26	        return "det-preferred", "int_died_det_alive", "death_asymmetry"
27	    if det_died and not int_died:
28	        return "internal-preferred", "det_died_int_alive", "death_asymmetry"
29	    if int_died and det_died:
30	        return "no-preference", "both_died", "both_dead"
31	    if det_score > int_score:
32	        return "det-preferred", "both_alive_det_wins", "score_comparison"
33	    if int_score > det_score:
34	        return "internal-preferred", "both_alive_int_wins", "score_comparison"
35	    return "no-preference", "tie", "tied_alive"
36	
37	
38	def extract_steps(episode_data: Dict, label: str, reason: str,
39	                  signal_source: str,
40	                  task_type: str, episode_idx: int, variation_idx: int,
41	                  int_score: float, det_score: float,
42	                  int_died: bool, det_died: bool) -> List[Dict]:
43	    if label == "internal-preferred":
44	        source_key = "always_internal"
45	    elif label == "det-preferred":
46	        source_key = "always_deterministic"
47	    else:
48	        source_key = "always_internal"
49	
50	    source_ep = episode_data[source_key]
51	    steps = source_ep.get("steps", [])
52	    action_history = []
53	    triples = []
54	
55	    for s in steps:
56	        triples.append({
57	            "task_type": task_type,
58	            "episode_id": episode_idx,
59	            "variation": variation_idx,
60	            "step_idx": s["step"],
61	            "observation": s.get("observation", ""),
62	            "action": s["action"],
63	            "action_history": list(action_history),
64	            "label": label,
65	            "signal_source": signal_source,
66	            "labeling_reason": reason,
67	            "episode_score_internal": int_score,
68	            "episode_score_det": det_score,
69	            "internal_died": int_died,
70	            "det_died": det_died,
71	        })
72	        action_history.append(s["action"])
73	
74	    return triples
75	
76	
77	def process_dir(input_dir: str) -> Tuple[List[Dict], Dict[str, int]]:
78	    """Process a single task directory containing episodes.jsonl."""
79	    task_type = os.path.basename(input_dir.rstrip("/"))
80	    episodes_path = os.path.join(input_dir, "episodes.jsonl")
81	    if not os.path.exists(episodes_path):
82	        print(f"  SKIP {task_type}: no episodes.jsonl")
83	        return [], {}
84	
85	    stats = defaultdict(int)
86	    all_triples = []
87	
88	    with open(episodes_path) as f:
89	        for line in f:
90	            line = line.strip()
91	            if not line:
92	                continue
93	            ep = json.loads(line)
94	
95	            episode_idx = ep.get("episode_idx", stats["total_episodes"])
96	            variation_idx = ep.get("variation_idx", 0)
97	
98	            if "always_internal" in ep and "always_deterministic" in ep:
99	                int_score = ep["always_internal"]["final_score"]
100	                det_score = ep["always_deterministic"]["final_score"]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dda71cca-fe3f-4cc2-8132-a711a11bd8ec",
  "isSidechain": true,
  "promptId": "873d52d2-4b2b-4bc2-850b-aec21329b090",
  "agentId": "aaafa5e9203d8d469",
  "type": "user",
  "uuid": "8379e7f6-189e-4875-b2a5-2c2cd4c5fb84",
  "sourceToolAssistantUUID": "dda71cca-fe3f-4cc2-8132-a711a11bd8ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "ee553895-1021-4931-aae1-4600fac1ac8a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-14T13:30:32.728Z_

Excellent! Now let me create a comprehensive summary document. Let me read one more file to understand training data format:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8379e7f6-189e-4875-b2a5-2c2cd4c5fb84",
  "isSidechain": true,
  "agentId": "aaafa5e9203d8d469",
  "requestId": "req_011Cb2YSi56f85xuQwGfR6XR",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "fcaccae4-8d57-4520-b8b5-616e3ae13776",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "ee553895-1021-4931-aae1-4600fac1ac8a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01NunjvAEeKH1RGnzmWXgH7u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 3241,
      "cache_read_input_tokens": 38536,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3241,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-14T13:30:33.796Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01HYQN8ePRRq2mjFJXMwbXUm`</summary>

```json
{
  "command": "head -100 /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/src/router_sft_train.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fcaccae4-8d57-4520-b8b5-616e3ae13776",
  "isSidechain": true,
  "agentId": "aaafa5e9203d8d469",
  "requestId": "req_011Cb2YSi56f85xuQwGfR6XR",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5c9b5052-7df8-4485-8b2f-598ccfe22047",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "ee553895-1021-4931-aae1-4600fac1ac8a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01NunjvAEeKH1RGnzmWXgH7u",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 3241,
      "cache_read_input_tokens": 38536,
      "output_tokens": 120,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3241
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 120,
          "cache_read_input_tokens": 38536,
          "cache_creation_input_tokens": 3241,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3241,
            "ephemeral_1h_input_tokens": 0
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

_source line 34 · 2026-05-14T13:30:33.856Z_

<details><summary>↩ Tool result · `toolu_01HYQN8ePRRq2mjFJXMwbXUm`</summary>

```text
# Router SFT training script for SimGate modular routing.
# Finetunes Qwen3-1.7B (or fallback) on episode-level labeled data
# from Plan C (labeled_steps.jsonl) for 2-way classification: internal vs deterministic.
#
# Data dependency: results/plan_c/{task_type}/labeled_steps.jsonl
# Usage: python src/router_sft_train.py --help

import argparse
import json
import os
import glob
import random
import warnings
from collections import Counter
from typing import List, Dict, Any, Optional, Tuple

import numpy as np
import torch
from torch.utils.data import Dataset, DataLoader, WeightedRandomSampler
from sklearn.metrics import accuracy_score, precision_recall_fscore_support, confusion_matrix
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    TrainingArguments,
    Trainer,
    EarlyStoppingCallback,
)
from peft import LoraConfig, get_peft_model, TaskType

LABEL2ID = {"internal": 0, "deterministic": 1}
ID2LABEL = {0: "internal", 1: "deterministic"}

RAW_LABEL_MAP = {
    "internal-preferred": "internal",
    "det-preferred": "deterministic",
    "internal": "internal",
    "deterministic": "deterministic",
}

SYSTEM_PROMPT = (
    "You are a routing classifier. Given the current observation and action history, "
    "predict which reasoning modality will lead to a better outcome."
)


def parse_args():
    p = argparse.ArgumentParser(description="Router SFT: finetune LLM for 2-way routing classification")
    p.add_argument("--data_path", type=str, default=None,
                    help="Single JSONL file (e.g. sft_triples.jsonl from death_aware_labeling)")
    p.add_argument("--data_dir", type=str, default=None,
                    help="Directory containing {task_type}/labeled_steps.jsonl (legacy)")
    p.add_argument("--model_name", type=str, default="Qwen/Qwen3-1.7B",
                    help="HuggingFace model name or local path")
    p.add_argument("--output_dir", type=str, default="results/router_sft/",
                    help="Output directory for checkpoints and reports")
    p.add_argument("--epochs", type=int, default=3)
    p.add_argument("--batch_size", type=int, default=32)
    p.add_argument("--eval_batch_size", type=int, default=32)
    p.add_argument("--lr", type=float, default=2e-5)
    p.add_argument("--lora_r", type=int, default=16)
    p.add_argument("--lora_alpha", type=int, default=32)
    p.add_argument("--lora_dropout", type=float, default=0.05)
    p.add_argument("--max_seq_len", type=int, default=2048)
    p.add_argument("--gpu_id", type=int, default=0)
    p.add_argument("--wandb_project", type=str, default="simgate-router-sft")
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--eval_split", type=float, default=0.2)
    p.add_argument("--warmup_ratio", type=float, default=0.1)
    p.add_argument("--weight_decay", type=float, default=0.01)
    p.add_argument("--early_stopping_patience", type=int, default=2)
    p.add_argument("--dry_run", action="store_true", help="Only validate imports and args, skip training")
    p.add_argument("--class_weights", type=str, default=None,
                    help='"auto" for inverse-frequency weights, or "w0,w1" (internal:w0, det:w1)')
    p.add_argument("--min_internal_samples", type=int, default=10,
                    help="Warn if internal samples < this threshold (default: 10)")
    p.add_argument("--upsample_minority", action="store_true",
                    help="Use WeightedRandomSampler to oversample minority class")
    return p.parse_args()


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

def summarize_action_history(action_history: List[str], max_actions: int = 5) -> str:
    """Keep the most recent N actions as a summary."""
    recent = action_history[-max_actions:] if action_history else []
    if not recent:
        return "(none)"
    return " → ".join(recent)


def build_prompt(observation: str, action_history: List[str]) -> str:
    history_summary = summarize_action_history(action_history)
    return (
        f"<|im_start|>system\n{SYSTEM_PROMPT}<|im_end|>\n"
        f"<|im_start|>user\n"
        f"Observation: {observation}\n"
        f"Action history: {history_summary}<|im_end|>"
    )
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5c9b5052-7df8-4485-8b2f-598ccfe22047",
  "isSidechain": true,
  "promptId": "873d52d2-4b2b-4bc2-850b-aec21329b090",
  "agentId": "aaafa5e9203d8d469",
  "type": "user",
  "uuid": "444f5c0b-eb36-46f0-a477-e9cc75d22a48",
  "sourceToolAssistantUUID": "5c9b5052-7df8-4485-8b2f-598ccfe22047",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "ee553895-1021-4931-aae1-4600fac1ac8a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-14T13:31:10.767Z_

Perfect! Now I have a comprehensive understanding. Let me create a detailed summary:

## Counterfactual Labeling Code Patterns Analysis

Based on my review of the codebase, here's a detailed breakdown of the key patterns for building a consistent ALFWorld counterfactual pipeline:

---

## 1. **Overall Architecture & Patterns**

### File Structure
- **`counterfactual_labeling.py`** (ScienceWorld): Step-level divergence detection with K-step continuation
- **`alfworld_counterfactual.py`** (ALFWorld): Episode-level success comparison
- **`llm_agent.py`** (Shared LLM interface): Qwen2.5-7B ReAct & candidate generation
- **`scienceworld_utils.py`** (Shared environment utilities): Environment forking via action-replay

### Fundamental Design
The project uses a **2-modality routing** approach:
1. **Internal**: Pure LLM reasoning (ReAct format)
2. **Deterministic**: Heuristic/expert policy (fork-evaluated candidates or HandCodedTWAgent)

---

## 2. **Internal vs Deterministic Modes**

### How They're Implemented

**Internal Mode (LLM-based)**
- Uses `agent.select_action_react(observation, valid_actions, history)` 
- Returns single action via ReAct prompt: `Thought:... Action:...`
- Deterministic temperature = 0.3 (low randomness)
- In ScienceWorld: Direct ReAct selection
- In ALFWorld: Direct ReAct selection via `llm_select_action()`

**Deterministic Mode (Heuristic)**
- **ScienceWorld**: Uses `agent.generate_candidate_actions(n=3)` + fork evaluation
  - Generates n=3 candidates via higher-temp (0.5) LLM prompt
  - Fork-evaluates each with 1-step lookahead via `fork_and_lookahead()`
  - Picks action with highest `score_delta` (filters lethal actions)
  - See `get_deterministic_action()` in counterfactual_labeling.py
  
- **ALFWorld**: Uses `HandCodedTWAgent` (PDDL-based expert)
  - Calls `expert.act(game_state, reward, done, last_action)`
  - Fallback to random admissible action if expert fails

---

## 3. **Episode Execution & Labeling**

### ScienceWorld Pattern (counterfactual_labeling.py)

**Per-Step Flow:**
```
For each step:
  1. Get internal_action via ReAct
  2. Apply death filter (retry if lethal)
  3. Get det_action via candidate generation + fork-eval
  4. If actions match → label="tie", advance with that action
  5. If actions differ → FORK BOTH (K-step continuation):
     - Fork 1: Execute internal_action, continue 10 steps with ReAct
     - Fork 2: Execute det_action, continue 10 steps with ReAct
     - Compare final scores → label = "deterministic" / "internal" / "tie"
     - Advance main env with oracle-chosen action (score_diff > 0 → det, else internal)
```

**Output Format (JSONL per episode):**
```json
{
  "episode": 0,
  "variation": 0,
  "total_steps": 15,
  "diverge_steps": 3,
  "tie_steps": 12,
  "labels": [
    {
      "step": 0,
      "label": "tie",
      "score_diff": 0.0
    },
    {
      "step": 5,
      "obs": "observation text",
      "internal_action": "action_str",
      "det_action": "different_action_str",
      "fork_internal_score": 45.0,
      "fork_det_score": 52.0,
      "score_diff": 7.0,
      "label": "deterministic",
      "fork_time_s": 2.45
    }
  ],
  "final_score": 100.0,
  "label_summary": {"deterministic": 2, "internal": 1, "tie": 12},
  "total_time_s": 45.2,
  "avg_fork_time_s": 2.35
}
```

### ALFWorld Pattern (alfworld_counterfactual.py)

**Episode-Level Flow:**
```
For each game:
  1. Run internal_episode: LLM ReAct for full episode → final_score
  2. Run deterministic_episode: HandCodedTWAgent for full episode → final_score
  3. Compare final scores:
     - det_success=True, int_success=False → "det-preferred"
     - int_success=True, det_success=False → "internal-preferred"
     - Otherwise → "no-preference"
```

**Output Format (JSONL per episode):**
```json
{
  "episode_id": "alfworld_pick_and_place_000",
  "environment": "alfworld",
  "task_type": "pick_and_place",
  "task_id": "pick_and_place.f5ea3c1d.trial_0",
  "task_desc": "your task is to put a papered paperweights in/on a desk",
  "internal": {
    "trajectory": [
      {
        "step": 0,
        "observation": "...",
        "thought": "...",
        "action": "go to desk",
        "reward": 0
      }
    ],
    "success": true,
    "n_steps": 8,
    "score": 1.0
  },
  "deterministic": {
    "trajectory": [...],
    "success": false,
    "n_steps": 12,
    "score": 0.0
  },
  "label": "internal-preferred",
  "metadata": {
    "subtask_type": "pick_and_place",
    "split": "valid_seen",
    "time_s": 42.5
  }
}
```

---

## 4. **LLM Inference Backend (llm_agent.py)**

### Dual Backend Support

**vLLM (Default, Production)**
- Loads via `LLM()` with tensor parallelism
- GPU memory utilization: 0.85
- Max model length: 4096 tokens
- Fast batch inference
- Enabled by: `--use_vllm` (default True)

**HuggingFace Transformers (Fallback)**
- AutoModelForCausalLM with torch.float16
- device_map=f"cuda:{gpu_id}"
- Single inference at a time
- Enabled by: `--no_vllm` flag

### Prompt Templates

**ReAct Template (both envs, temperature=0.3):**
```
System: You are an agent interacting with a [ScienceWorld|ALFWorld] environment...
User: Current observation:
{observation}

Valid actions:
{formatted_list}

Previous actions taken: {history}

Choose your next action.
```

**Candidate Generation (ScienceWorld only, temperature=0.5):**
```
System: [same]
User: ...Valid actions...
Generate the top 3 most promising actions... Output exactly 3 actions, one per line:
1. &lt;action>
2. &lt;action>
3. &lt;action>
```

### Action Parsing
- **Pattern 1**: Extract `Action: &lt;text>` via regex
- **Pattern 2**: Fuzzy case-insensitive matching
- **Pattern 3**: Substring matching (for ALFWorld)
- **Fallback**: Return first valid action

### Return Values
- `select_action_react()` → `(action: str, raw_llm_output: str)`
- `generate_candidate_actions()` → `(candidates: List[str], raw_llm_output: str)`

---

## 5. **State Forking Mechanism (scienceworld_utils.py)**

### Core Forking Principle
**Each fork is a new JVM instance** (due to py4j) that replays historical actions:

```python
fork_and_lookahead(task_name, variation_idx, action_history, candidate_action):
  1. Create fresh env instance
  2. Reset to initial state
  3. Replay all actions in action_history sequentially
  4. Execute candidate_action
  5. Return {"score", "score_delta", "done", "observation", "replay_errors"}
  6. Close env (cleanup JVM)
```

### Key Properties
- **Deterministic**: Same action_history → same state
- **Expensive**: Each fork = new JVM + full replay (O(n) for n historical actions)
- **Robust**: Returns `replay_errors` if any action fails
- **Score Tracking**: Cached via `env._last_score` in info dict

### Continuation Pattern (fork_and_continue)
```python
fork_and_continue(agent, task_name, variation_idx, action_history, first_action, K=10):
  1. Fork env with action_history
  2. Execute first_action
  3. Continue K steps with base policy (always ReAct)
  4. Return final_score
```

---

## 6. **Output JSONL Formats**

### ScienceWorld CF Labels (counterfactual_labeling.py)
- **File**: `results/cf_labels/{task_type}/cf_labels.jsonl`
- **One line per episode**
- **Contains**: Divergence labels (deterministic/internal/tie) at step level
- **Key fields**: `episode`, `variation`, `total_steps`, `labels[]` (with fork scores)

### ALFWorld CF Labels (alfworld_counterfactual.py)
- **File**: `data/alfworld-counterfactual/episodes.jsonl`
- **One line per episode**
- **Contains**: Episode-level labels (episode_id, internal result, deterministic result, final label)
- **Key fields**: `internal.success`, `deterministic.success`, `label`

### Router SFT Training Data (death_aware_labeling.py)
- **File**: `sft_triples.jsonl` or `{task_type}/labeled_steps.jsonl`
- **One line per step** (converted from episode data)
- **Used for**: Fine-tuning router LLM on 2-way classification
- **Labels**: Internal vs Deterministic (binary)
- **Signal sources**: Death asymmetry (primary) or score comparison (secondary)

---

## 7. **Death Filtering & Lethal Actions**

### Definition
```python
is_lethal(fork_result):
  return fork_result["done"] and fork_result["score"] < 0
         or fork_result["score"] <= -100
```

### Application
- **Deterministic mode**: Skip lethal candidates, pick best non-lethal
- **Internal mode**: Retry LLM up to 3 times if selected action is lethal
- **Fallback**: If all actions lethal, pick least-bad option

---

## 8. **Key Implementation Details for ALFWorld**

### Environment Setup
```python
make_env(game_path):
  - Uses textworld.gym.register_games()
  - Wraps with AlfredDemangler, AlfredInfos
  - Returns TextWorld gym interface
```

### Game State Management
```python
game_state = {
  "feedback": observation_text,
  "admissible_commands": valid_actions,
  "facts": world_state_facts
}
expert.act(game_state, reward, done, last_action)
```

### Episode Data Collection
```python
run_internal_episode():
  - LLM drives every action via ReAct
  - Trajectory: list of {step, observation, thought, action, reward}
  - Returns: {trajectory, success, n_steps, score}

run_deterministic_episode():
  - HandCodedTWAgent drives every action
  - Same trajectory format
  - Returns: {trajectory, success, n_steps, score}
```

---

## 9. **Key Configuration Parameters**

| Parameter | ScienceWorld | ALFWorld | Notes |
|-----------|--------------|----------|-------|
| `max_steps` | 30 (default) | 50 (default) | Episode length |
| `continuation_steps` / `K` | 10 | N/A | Steps to continue after fork |
| `n_candidates` | 3 | N/A | Candidates for deterministic eval |
| `temperature` | 0.3 (ReAct), 0.5 (candidates) | 0.3 | LLM sampling |
| `max_new_tokens` | 256 | 256 | LLM generation limit |
| `gpu_id` | 0 (default) | 1 (default) | CUDA device |
| `use_vllm` | True (default) | True (default) | Backend |
| `episodes` / `n_tasks` | 20 (default) | 10 (implied) | Number of runs |

---

## 10. **Patterns to Replicate for ALFWorld Pipeline**

To build a **consistent ALFWorld counterfactual pipeline**, replicate:

1. **Agent initialization** (llm_agent.py):
   ```python
   agent = LLMAgent(model_path=..., use_vllm=True, gpu_id=0)
   ```

2. **Episode runners** (alfworld_counterfactual.py pattern):
   - `run_internal_episode()` → LLM-only trajectory
   - `run_deterministic_episode()` → Expert-only trajectory
   - Compare final scores/success

3. **Labeling logic** (episode-level, not step-level):
   - Success ratio or final score comparison
   - Asymmetric signals preferred (success diff)

4. **Output format**:
   - JSONL with `episode_id`, `environment`, `task_type`, `label`
   - Include both `internal` and `deterministic` full trajectories
   - Optional: add step-level divergence tracking

5. **Configuration interface**:
   - Use argparse with task selection, output path, GPU ID, vLLM toggle
   - Support filtering by task types and max-per-type

---

## 11. **Critical Differences: ScienceWorld vs ALFWorld**

| Aspect | ScienceWorld | ALFWorld |
|--------|--------------|----------|
| **Forking** | Action-replay (py4j JVM) | No forking (sequential episodes) |
| **Deterministic** | LLM candidates + fork-eval | HandCodedTWAgent (PDDL expert) |
| **Labeling** | Step-level (K-step continuation) | Episode-level (final score/success) |
| **Score** | Continuous (0-100+) | Binary success (0.0 or 1.0) |
| **Fork cost** | ~1-2s per fork | N/A |
| **Tie rate** | Expected high (~65%) | Expected lower (binary outcomes) |
| **History size** | Typical 5-15 actions | Typical 5-12 steps |

---

## Summary for Your ALFWorld Pipeline

**Key implementation points:**
1. Keep the **episode-level labeling** (not step-level) like ALFWorld original
2. Use **LLMAgent for internal**, **expert/heuristic for deterministic**
3. **No forking needed** — run two full independent episodes and compare
4. Output **unified JSONL** with both trajectories + label
5. Support **task selection & filtering** like the existing pipeline
6. Use **vLLM backend** for fast inference on Qwen2.5-7B
7. Track **success/score metrics** for labeling (death asymmetry preferred)

The `alfworld_counterfactual.py` file is already a complete reference implementation — you can adapt it by adjusting task collection, expert policy, or labeling logic as needed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "444f5c0b-eb36-46f0-a477-e9cc75d22a48",
  "isSidechain": true,
  "agentId": "aaafa5e9203d8d469",
  "requestId": "req_011Cb2YSx5xYdeupkHybvhUJ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e2495d8d-8856-4c5f-8f02-1c74f1540bf3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "sessionId": "ee553895-1021-4931-aae1-4600fac1ac8a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01XA1U2nChctbGYUa5r7kdwC",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1470,
      "cache_read_input_tokens": 41777,
      "output_tokens": 3955,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1470
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 3955,
          "cache_read_input_tokens": 41777,
          "cache_creation_input_tokens": 1470,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1470,
            "ephemeral_1h_input_tokens": 0
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
