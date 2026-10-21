# code subsample patch

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 0
- **Tool calls:** 5
- **Original source:** `logs/workers/worker_code_subsample-patch_20260513T040708.log`
- **Structured JSON:** [`2a33e03b5adb6770539a.json`](../../sessions/2a/2a33e03b5adb6770539a.json)

## Before a recorded user message

19 recorded events

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
  "session_id": "4548d576-751a-4385-85b2-ea3732bcaf07",
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
  "uuid": "bf90cdbc-e195-43e1-a274-f75206319c2f",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/memory/"
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
    "resetsAt": 1778659200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "6776e2a3-2fd6-46ae-99c5-feda056d2bf8",
  "session_id": "4548d576-751a-4385-85b2-ea3732bcaf07"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the necessary files to understand the current code structure.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4548d576-751a-4385-85b2-ea3732bcaf07",
  "uuid": "9c17c277-1776-4fe7-96e3-f6707a2c53a7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Haw9mreVN6GgYp1HQ1rWhs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12548,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12548
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

_source line 5_

先读取现有代码。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4548d576-751a-4385-85b2-ea3732bcaf07",
  "uuid": "c2bda881-d703-4a12-aeb7-4e3f98c6919a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Haw9mreVN6GgYp1HQ1rWhs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12548,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12548
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

_source line 6_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01YBRQBCjMZ8ZJher9pQtXL6`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
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
  "session_id": "4548d576-751a-4385-85b2-ea3732bcaf07",
  "uuid": "3e3012d7-57a6-4956-8637-b5265586316d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Haw9mreVN6GgYp1HQ1rWhs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12548,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12548
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

_source line 7 · 2026-05-13T04:07:21.176Z_

<details><summary>↩ Tool result · `toolu_01YBRQBCjMZ8ZJher9pQtXL6`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
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
  "session_id": "4548d576-751a-4385-85b2-ea3732bcaf07",
  "uuid": "0e18eab1-7466-4d3f-a1d6-60fe19bfea9b",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Lc5qVpURMV2c61fF39BzSf`</summary>

```json
{
  "project": "event-gated-adaptive-horizon",
  "file": "implementation_design.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4548d576-751a-4385-85b2-ea3732bcaf07",
  "uuid": "2b462b8e-e856-42b9-b74b-f2c92442b0cb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016GuVmj2V9ExwAqz6ZGPFNZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 473,
      "cache_read_input_tokens": 23995,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 473
      },
      "output_tokens": 70,
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

_source line 9 · 2026-05-13T04:07:24.003Z_

<details><summary>↩ Tool result · `toolu_01Lc5qVpURMV2c61fF39BzSf`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'implementation_design.md'\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4548d576-751a-4385-85b2-ea3732bcaf07",
  "uuid": "32e2a28c-0951-4b62-a97f-5a21f98ec7fd",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'implementation_design.md'\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'implementation_design.md'\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Read · `toolu_01G71hWgDGh2tbyCXMK7Te1Z`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/code/tools.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4548d576-751a-4385-85b2-ea3732bcaf07",
  "uuid": "886574cd-7034-453e-bba6-32129d910189",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016GuVmj2V9ExwAqz6ZGPFNZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 473,
      "cache_read_input_tokens": 23995,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 473
      },
      "output_tokens": 70,
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

_source line 11 · 2026-05-13T04:07:24.868Z_

<details><summary>↩ Tool result · `toolu_01G71hWgDGh2tbyCXMK7Te1Z`</summary>

```text
1	# Event-Gated Adaptive-Horizon DreamerV3 — Utility Functions
2	# Modified from NM512/dreamerv3-torch.
3	# Changes: added lambda_return_variable_dt and subsample_variable_dt.
4	
5	import datetime
6	import collections
7	import io
8	import os
9	import json
10	import math
11	import pathlib
12	import re
13	import time
14	import random
15	
16	import numpy as np
17	
18	import torch
19	from torch import nn
20	from torch.nn import functional as F
21	from torch import distributions as torchd
22	from torch.utils.tensorboard import SummaryWriter
23	
24	
25	to_np = lambda x: x.detach().cpu().numpy()
26	
27	
28	def symlog(x):
29	    return torch.sign(x) * torch.log(torch.abs(x) + 1.0)
30	
31	
32	def symexp(x):
33	    return torch.sign(x) * (torch.exp(torch.abs(x)) - 1.0)
34	
35	
36	class RequiresGrad:
37	    def __init__(self, model):
38	        self._model = model
39	
40	    def __enter__(self):
41	        self._model.requires_grad_(requires_grad=True)
42	
43	    def __exit__(self, *args):
44	        self._model.requires_grad_(requires_grad=False)
45	
46	
47	class TimeRecording:
48	    def __init__(self, comment):
49	        self._comment = comment
50	
51	    def __enter__(self):
52	        self._st = torch.cuda.Event(enable_timing=True)
53	        self._nd = torch.cuda.Event(enable_timing=True)
54	        self._st.record()
55	
56	    def __exit__(self, *args):
57	        self._nd.record()
58	        torch.cuda.synchronize()
59	        print(self._comment, self._st.elapsed_time(self._nd) / 1000)
60	
61	
62	class Logger:
63	    def __init__(self, logdir, step):
64	        self._logdir = logdir
65	        self._writer = SummaryWriter(log_dir=str(logdir), max_queue=1000)
66	        self._last_step = None
67	        self._last_time = None
68	        self._scalars = {}
69	        self._images = {}
70	        self._videos = {}
71	        self.step = step
72	
73	    def scalar(self, name, value):
74	        self._scalars[name] = float(value)
75	
76	    def image(self, name, value):
77	        self._images[name] = np.array(value)
78	
79	    def video(self, name, value):
80	        self._videos[name] = np.array(value)
81	
82	    def write(self, fps=False, step=False):
83	        if not step:
84	            step = self.step
85	        scalars = list(self._scalars.items())
86	        if fps:
87	            scalars.append(("fps", self._compute_fps(step)))
88	        print(f"[{step}]", " / ".join(f"{k} {v:.1f}" for k, v in scalars))
89	        with (self._logdir / "metrics.jsonl").open("a") as f:
90	            f.write(json.dumps({"step": step, **dict(scalars)}) + "\n")
91	        for name, value in scalars:
92	            if "/" not in name:
93	                self._writer.add_scalar("scalars/" + name, value, step)
94	            else:
95	                self._writer.add_scalar(name, value, step)
96	        for name, value in self._images.items():
97	            self._writer.add_image(name, value, step)
98	        for name, value in self._videos.items():
99	            name = name if isinstance(name, str) else name.decode("utf-8")
100	            if np.issubdtype(value.dtype, np.floating):
101	                value = np.clip(255 * value, 0, 255).astype(np.uint8)
102	            B, T, H, W, C = value.shape
103	            value = value.transpose(1, 4, 2, 0, 3).reshape((1, T, C, H, B * W))
104	            self._writer.add_video(name, value, step, 16)
105	
106	        self._writer.flush()
107	        self._scalars = {}
108	        self._images = {}
109	        self._videos = {}
110	
111	    def _compute_fps(self, step):
112	        if self._last_step is None:
113	            self._last_time = time.time()
114	            self._last_step = step
115	            return 0
116	        steps = step - self._last_step
117	        duration = time.time() - self._last_time
118	        self._last_time += duration
119	        self._last_step = step
120	        return steps / duration
121	
122	    def offline_scalar(self, name, value, step):
123	        self._writer.add_scalar("scalars/" + name, value, step)
124	
125	    def offline_video(self, name, value, step):
126	        if np.issubdtype(value.dtype, np.floating):
127	            value = np.clip(255 * value, 0, 255).astype(np.uint8)
128	        B, T, H, W, C = value.shape
129	        value = value.transpose(1, 4, 2, 0, 3).reshape((1, T, C, H, B * W))
130	        self._writer.add_video(name, value, step, 16)
131	
132	
133	def simulate(
134	    agent,
135	    envs,
136	    cache,
137	    directory,
138	    logger,
139	    is_eval=False,
140	    limit=None,
141	    steps=0,
142	    episodes=0,
143	    state=None,
144	):
145	    # initialize or unpack simulation state
146	    if state is None:
147	        step, episode = 0, 0
148	        done = np.ones(len(envs), bool)
149	        length = np.zeros(len(envs), np.int32)
150	        obs = [None] * len(envs)
151	        agent_state = None
152	        reward = [0] * len(envs)
153	    else:
154	        step, episode, done, length, obs, agent_state, reward = state
155	    while (steps and step < steps) or (episodes and episode < episodes):
156	        # reset envs if necessary
157	        if done.any():
158	            indices = [index for index, d in enumerate(done) if d]
159	            results = [envs[i].reset() for i in indices]
160	            results = [r() for r in results]
161	            for index, result in zip(indices, results):
162	                t = result.copy()
163	                t = {k: convert(v) for k, v in t.items()}
164	                # action will be added to transition in add_to_cache
165	                t["reward"] = 0.0
166	                t["discount"] = 1.0
167	                # initial state should be added to cache
168	                add_to_cache(cache, envs[index].id, t)
169	                # replace obs with done by initial state
170	                obs[index] = result
171	        # step agents
172	        obs = {k: np.stack([o[k] for o in obs]) for k in obs[0] if "log_" not in k}
173	        action, agent_state = agent(obs, done, agent_state)
174	        if isinstance(action, dict):
175	            action = [
176	                {k: np.array(action[k][i].detach().cpu()) for k in action}
177	                for i in range(len(envs))
178	            ]
179	        else:
180	            action = np.array(action)
181	        assert len(action) == len(envs)
182	        # step envs
183	        results = [e.step(a) for e, a in zip(envs, action)]
184	        results = [r() for r in results]
185	        obs, reward, done = zip(*[p[:3] for p in results])
186	        obs = list(obs)
187	        reward = list(reward)
188	        done = np.stack(done)
189	        episode += int(done.sum())
190	        length += 1
191	        step += len(envs)
192	        length *= 1 - done
193	        # add to cache
194	        for a, result, env in zip(action, results, envs):
195	            o, r, d, info = result
196	            o = {k: convert(v) for k, v in o.items()}
197	            transition = o.copy()
198	            if isinstance(a, dict):
199	                transition.update(a)
200	            else:
201	                transition["action"] = a
202	            transition["reward"] = r
203	            transition["discount"] = info.get("discount", np.array(1 - float(d)))
204	            add_to_cache(cache, env.id, transition)
205	
206	        if done.any():
207	            indices = [index for index, d in enumerate(done) if d]
208	            # logging for done episode
209	            for i in indices:
210	                save_episodes(directory, {envs[i].id: cache[envs[i].id]})
211	                length = len(cache[envs[i].id]["reward"]) - 1
212	                score = float(np.array(cache[envs[i].id]["reward"]).sum())
213	                video = cache[envs[i].id]["image"]
214	                # record logs given from environments
215	                for key in list(cache[envs[i].id].keys()):
216	                    if "log_" in key:
217	                        logger.scalar(
218	                            key, float(np.array(cache[envs[i].id][key]).sum())
219	                        )
220	                        # log items won't be used later
221	                        cache[envs[i].id].pop(key)
222	
223	                if not is_eval:
224	                    step_in_dataset = erase_over_episodes(cache, limit)
225	                    logger.scalar(f"dataset_size", step_in_dataset)
226	                    logger.scalar(f"train_return", score)
227	                    logger.scalar(f"train_length", length)
228	                    logger.scalar(f"train_episodes", len(cache))
229	                    logger.write(step=logger.step)
230	                else:
231	                    if not "eval_lengths" in locals():
232	                        eval_lengths = []
233	                        eval_scores = []
234	                        eval_done = False
235	                    # start counting scores for evaluation
236	                    eval_scores.append(score)
237	                    eval_lengths.append(length)
238	
239	                    score = sum(eval_scores) / len(eval_scores)
240	                    length = sum(eval_lengths) / len(eval_lengths)
241	                    logger.video(f"eval_policy", np.array(video)[None])
242	
243	                    if len(eval_scores) >= episodes and not eval_done:
244	                        logger.scalar(f"eval_return", score)
245	                        logger.scalar(f"eval_length", length)
246	                        logger.scalar(f"eval_episodes", len(eval_scores))
247	                        logger.write(step=logger.step)
248	                        eval_done = True
249	    if is_eval:
250	        # keep only last item for saving memory. this cache is used for video_pred later
251	        while len(cache) > 1:
252	            # FIFO
253	            cache.popitem(last=False)
254	    return (step - steps, episode - episodes, done, length, obs, agent_state, reward)
255	
256	
257	def add_to_cache(cache, id, transition):
258	    if id not in cache:
259	        cache[id] = dict()
260	        for key, val in transition.items():
261	            cache[id][key] = [convert(val)]
262	    else:
263	        for key, val in transition.items():
264	            if key not in cache[id]:
265	                # fill missing data(action, etc.) at second time
266	                cache[id][key] = [convert(0 * val)]
267	                cache[id][key].append(convert(val))
268	            else:
269	                cache[id][key].append(convert(val))
270	
271	
272	def erase_over_episodes(cache, dataset_size):
273	    step_in_dataset = 0
274	    for key, ep in reversed(sorted(cache.items(), key=lambda x: x[0])):
275	        if (
276	            not dataset_size
277	            or step_in_dataset + (len(ep["reward"]) - 1) <= dataset_size
278	        ):
279	            step_in_dataset += len(ep["reward"]) - 1
280	        else:
281	            del cache[key]
282	    return step_in_dataset
283	
284	
285	def convert(value, precision=32):
286	    value = np.array(value)
287	    if np.issubdtype(value.dtype, np.floating):
288	        dtype = {16: np.float16, 32: np.float32, 64: np.float64}[precision]
289	    elif np.issubdtype(value.dtype, np.signedinteger):
290	        dtype = {16: np.int16, 32: np.int32, 64: np.int64}[precision]
291	    elif np.issubdtype(value.dtype, np.uint8):
292	        dtype = np.uint8
293	    elif np.issubdtype(value.dtype, bool):
294	        dtype = bool
295	    else:
296	        raise NotImplementedError(value.dtype)
297	    return value.astype(dtype)
298	
299	
300	def save_episodes(directory, episodes):
301	    directory = pathlib.Path(directory).expanduser()
302	    directory.mkdir(parents=True, exist_ok=True)
303	    for filename, episode in episodes.items():
304	        length = len(episode["reward"])
305	        filename = directory / f"{filename}-{length}.npz"
306	        with io.BytesIO() as f1:
307	            np.savez_compressed(f1, **episode)
308	            f1.seek(0)
309	            with filename.open("wb") as f2:
310	                f2.write(f1.read())
311	    return True
312	
313	
314	def from_generator(generator, batch_size):
315	    while True:
316	        batch = []
317	        for _ in range(batch_size):
318	            batch.append(next(generator))
319	        data = {}
320	        for key in batch[0].keys():
321	            data[key] = []
322	            for i in range(batch_size):
323	                data[key].append(batch[i][key])
324	            data[key] = np.stack(data[key], 0)
325	        yield data
326	
327	
328	def sample_episodes(episodes, length, seed=0):
329	    np_random = np.random.RandomState(seed)
330	    while True:
331	        size = 0
332	        ret = None
333	        p = np.array(
334	            [len(next(iter(episode.values()))) for episode in episodes.values()]
335	        )
336	        p = p / np.sum(p)
337	        while size < length:
338	            episode = np_random.choice(list(episodes.values()), p=p)
339	            total = len(next(iter(episode.values())))
340	            # make sure at least one transition included
341	            if total < 2:
342	                continue
343	            if not ret:
344	                index = int(np_random.randint(0, total - 1))
345	                ret = {
346	                    k: v[index : min(index + length, total)].copy()
347	                    for k, v in episode.items()
348	                    if "log_" not in k
349	                }
350	                if "is_first" in ret:
351	                    ret["is_first"][0] = True
352	            else:
353	                # 'is_first' comes after 'is_last'
354	                index = 0
355	                possible = length - size
356	                ret = {
357	                    k: np.append(
358	                        ret[k], v[index : min(index + possible, total)].copy(), axis=0
359	                    )
360	                    for k, v in episode.items()
361	                    if "log_" not in k
362	                }
363	                if "is_first" in ret:
364	                    ret["is_first"][size] = True
365	            size = len(next(iter(ret.values())))
366	        yield ret
367	
368	
369	def load_episodes(directory, limit=None, reverse=True):
370	    directory = pathlib.Path(directory).expanduser()
371	    episodes = collections.OrderedDict()
372	    total = 0
373	    if reverse:
374	        for filename in reversed(sorted(directory.glob("*.npz"))):
375	            try:
376	                with filename.open("rb") as f:
377	                    episode = np.load(f)
378	                    episode = {k: episode[k] for k in episode.keys()}
379	            except Exception as e:
380	                print(f"Could not load episode: {e}")
381	                continue
382	            # extract only filename without extension
383	            episodes[str(os.path.splitext(os.path.basename(filename))[0])] = episode
384	            total += len(episode["reward"]) - 1
385	            if limit and total >= limit:
386	                break
387	    else:
388	        for filename in sorted(directory.glob("*.npz")):
389	            try:
390	                with filename.open("rb") as f:
391	                    episode = np.load(f)
392	                    episode = {k: episode[k] for k in episode.keys()}
393	            except Exception as e:
394	                print(f"Could not load episode: {e}")
395	                continue
396	            episodes[str(filename)] = episode
397	            total += len(episode["reward"]) - 1
398	            if limit and total >= limit:
399	                break
400	    return episodes
401	
402	
403	class SampleDist:
404	    def __init__(self, dist, samples=100):
405	        self._dist = dist
406	        self._samples = samples
407	
408	    @property
409	    def name(self):
410	        return "SampleDist"
411	
412	    def __getattr__(self, name):
413	        return getattr(self._dist, name)
414	
415	    def mean(self):
416	        samples = self._dist.sample(self._samples)
417	        return torch.mean(samples, 0)
418	
419	    def mode(self):
420	        sample = self._dist.sample(self._samples)
421	        logprob = self._dist.log_prob(sample)
422	        return sample[torch.argmax(logprob)][0]
423	
424	    def entropy(self):
425	        sample = self._dist.sample(self._samples)
426	        logprob = self.log_prob(sample)
427	        return -torch.mean(logprob, 0)
428	
429	
430	class OneHotDist(torchd.one_hot_categorical.OneHotCategorical):
431	    def __init__(self, logits=None, probs=None, unimix_ratio=0.0):
432	        if logits is not None and unimix_ratio > 0.0:
433	            probs = F.softmax(logits, dim=-1)
434	            probs = probs * (1.0 - unimix_ratio) + unimix_ratio / probs.shape[-1]
435	            logits = torch.log(probs)
436	            super().__init__(logits=logits, probs=None)
437	        else:
438	            super().__init__(logits=logits, probs=probs)
439	
440	    def mode(self):
441	        _mode = F.one_hot(
442	            torch.argmax(super().logits, axis=-1), super().logits.shape[-1]
443	        )
444	        return _mode.detach() + super().logits - super().logits.detach()
445	
446	    def sample(self, sample_shape=(), seed=None):
447	        if seed is not None:
448	            raise ValueError("need to check")
449	        sample = super().sample(sample_shape).detach()
450	        probs = super().probs
451	        while len(probs.shape) < len(sample.shape):
452	            probs = probs[None]
453	        sample += probs - probs.detach()
454	        return sample
455	
456	
457	class DiscDist:
458	    def __init__(
459	        self,
460	        logits,
461	        low=-20.0,
462	        high=20.0,
463	        transfwd=symlog,
464	        transbwd=symexp,
465	        device="cuda",
466	    ):
467	        self.logits = logits
468	        self.probs = torch.softmax(logits, -1)
469	        self.buckets = torch.linspace(low, high, steps=255, device=device)
470	        self.width = (self.buckets[-1] - self.buckets[0]) / 255
471	        self.transfwd = transfwd
472	        self.transbwd = transbwd
473	
474	    def mean(self):
475	        _mean = self.probs * self.buckets
476	        return self.transbwd(torch.sum(_mean, dim=-1, keepdim=True))
477	
478	    def mode(self):
479	        _mode = self.probs * self.buckets
480	        return self.transbwd(torch.sum(_mode, dim=-1, keepdim=True))
481	
482	    # Inside OneHotCategorical, log_prob is calculated using only max element in targets
483	    def log_prob(self, x):
484	        x = self.transfwd(x)
485	        # x(time, batch, 1)
486	        below = torch.sum((self.buckets <= x[..., None]).to(torch.int32), dim=-1) - 1
487	        above = len(self.buckets) - torch.sum(
488	            (self.buckets > x[..., None]).to(torch.int32), dim=-1
489	        )
490	        # this is implemented using clip at the original repo as the gradients are not backpropagated for the out of limits.
491	        below = torch.clip(below, 0, len(self.buckets) - 1)
492	        above = torch.clip(above, 0, len(self.buckets) - 1)
493	        equal = below == above
494	
495	        dist_to_below = torch.where(equal, 1, torch.abs(self.buckets[below] - x))
496	        dist_to_above = torch.where(equal, 1, torch.abs(self.buckets[above] - x))
497	        total = dist_to_below + dist_to_above
498	        weight_below = dist_to_above / total
499	        weight_above = dist_to_below / total
500	        target = (
501	            F.one_hot(below, num_classes=len(self.buckets)) * weight_below[..., None]
502	            + F.one_hot(above, num_classes=len(self.buckets)) * weight_above[..., None]
503	        )
504	        log_pred = self.logits - torch.logsumexp(self.logits, -1, keepdim=True)
505	        target = target.squeeze(-2)
506	
507	        return (target * log_pred).sum(-1)
508	
509	    def log_prob_target(self, target):
510	        log_pred = super().logits - torch.logsumexp(super().logits, -1, keepdim=True)
511	        return (target * log_pred).sum(-1)
512	
513	
514	class MSEDist:
515	    def __init__(self, mode, agg="sum"):
516	        self._mode = mode
517	        self._agg = agg
518	
519	    def mode(self):
520	        return self._mode
521	
522	    def mean(self):
523	        return self._mode
524	
525	    def log_prob(self, value):
526	        assert self._mode.shape == value.shape, (self._mode.shape, value.shape)
527	        distance = (self._mode - value) ** 2
528	        if self._agg == "mean":
529	            loss = distance.mean(list(range(len(distance.shape)))[2:])
530	        elif self._agg == "sum":
531	            loss = distance.sum(list(range(len(distance.shape)))[2:])
532	        else:
533	            raise NotImplementedError(self._agg)
534	        return -loss
535	
536	
537	class SymlogDist:
538	    def __init__(self, mode, dist="mse", agg="sum", tol=1e-8):
539	        self._mode = mode
540	        self._dist = dist
541	        self._agg = agg
542	        self._tol = tol
543	
544	    def mode(self):
545	        return symexp(self._mode)
546	
547	    def mean(self):
548	        return symexp(self._mode)
549	
550	    def log_prob(self, value):
551	        assert self._mode.shape == value.shape
552	        if self._dist == "mse":
553	            distance = (self._mode - symlog(value)) ** 2.0
554	            distance = torch.where(distance < self._tol, 0, distance)
555	        elif self._dist == "abs":
556	            distance = torch.abs(self._mode - symlog(value))
557	            distance = torch.where(distance < self._tol, 0, distance)
558	        else:
559	            raise NotImplementedError(self._dist)
560	        if self._agg == "mean":
561	            loss = distance.mean(list(range(len(distance.shape)))[2:])
562	        elif self._agg == "sum":
563	            loss = distance.sum(list(range(len(distance.shape)))[2:])
564	        else:
565	            raise NotImplementedError(self._agg)
566	        return -loss
567	
568	
569	class ContDist:
570	    def __init__(self, dist=None, absmax=None):
571	        super().__init__()
572	        self._dist = dist
573	        self.mean = dist.mean
574	        self.absmax = absmax
575	
576	    def __getattr__(self, name):
577	        return getattr(self._dist, name)
578	
579	    def entropy(self):
580	        return self._dist.entropy()
581	
582	    def mode(self):
583	        out = self._dist.mean
584	        if self.absmax is not None:
585	            out *= (self.absmax / torch.clip(torch.abs(out), min=self.absmax)).detach()
586	        return out
587	
588	    def sample(self, sample_shape=()):
589	        out = self._dist.rsample(sample_shape)
590	        if self.absmax is not None:
591	            out *= (self.absmax / torch.clip(torch.abs(out), min=self.absmax)).detach()
592	        return out
593	
594	    def log_prob(self, x):
595	        return self._dist.log_prob(x)
596	
597	
598	class Bernoulli:
599	    def __init__(self, dist=None):
600	        super().__init__()
601	        self._dist = dist
602	        self.mean = dist.mean
603	
604	    def __getattr__(self, name):
605	        return getattr(self._dist, name)
606	
607	    def entropy(self):
608	        return self._dist.entropy()
609	
610	    def mode(self):
611	        _mode = torch.round(self._dist.mean)
612	        return _mode.detach() + self._dist.mean - self._dist.mean.detach()
613	
614	    def sample(self, sample_shape=()):
615	        return self._dist.rsample(sample_shape)
616	
617	    def log_prob(self, x):
618	        _logits = self._dist.base_dist.logits
619	        log_probs0 = -F.softplus(_logits)
620	        log_probs1 = -F.softplus(-_logits)
621	
622	        return torch.sum(log_probs0 * (1 - x) + log_probs1 * x, -1)
623	
624	
625	class UnnormalizedHuber(torchd.normal.Normal):
626	    def __init__(self, loc, scale, threshold=1, **kwargs):
627	        super().__init__(loc, scale, **kwargs)
628	        self._threshold = threshold
629	
630	    def log_prob(self, event):
631	        return -(
632	            torch.sqrt((event - self.mean) ** 2 + self._threshold**2) - self._threshold
633	        )
634	
635	    def mode(self):
636	        return self.mean
637	
638	
639	class SafeTruncatedNormal(torchd.normal.Normal):
640	    def __init__(self, loc, scale, low, high, clip=1e-6, mult=1):
641	        super().__init__(loc, scale)
642	        self._low = low
643	        self._high = high
644	        self._clip = clip
645	        self._mult = mult
646	
647	    def sample(self, sample_shape):
648	        event = super().sample(sample_shape)
649	        if self._clip:
650	            clipped = torch.clip(event, self._low + self._clip, self._high - self._clip)
651	            event = event - event.detach() + clipped.detach()
652	        if self._mult:
653	            event *= self._mult
654	        return event
655	
656	
657	class TanhBijector(torchd.Transform):
658	    def __init__(self, validate_args=False, name="tanh"):
659	        super().__init__()
660	
661	    def _forward(self, x):
662	        return torch.tanh(x)
663	
664	    def _inverse(self, y):
665	        y = torch.where(
666	            (torch.abs(y) <= 1.0), torch.clamp(y, -0.99999997, 0.99999997), y
667	        )
668	        y = torch.atanh(y)
669	        return y
670	
671	    def _forward_log_det_jacobian(self, x):
672	        log2 = torch.math.log(2.0)
673	        return 2.0 * (log2 - x - torch.softplus(-2.0 * x))
674	
675	
676	def static_scan_for_lambda_return(fn, inputs, start):
677	    last = start
678	    indices = range(inputs[0].shape[0])
679	    indices = reversed(indices)
680	    flag = True
681	    for index in indices:
682	        # (inputs, pcont) -> (inputs[index], pcont[index])
683	        inp = lambda x: (_input[x] for _input in inputs)
684	        last = fn(last, *inp(index))
685	        if flag:
686	            outputs = last
687	            flag = False
688	        else:
689	            outputs = torch.cat([outputs, last], dim=-1)
690	    outputs = torch.reshape(outputs, [outputs.shape[0], outputs.shape[1], 1])
691	    outputs = torch.flip(outputs, [1])
692	    outputs = torch.unbind(outputs, dim=0)
693	    return outputs
694	
695	
696	def lambda_return(reward, value, pcont, bootstrap, lambda_, axis):
697	    # Setting lambda=1 gives a discounted Monte Carlo return.
698	    # Setting lambda=0 gives a fixed 1-step return.
699	    # assert reward.shape.ndims == value.shape.ndims, (reward.shape, value.shape)
700	    assert len(reward.shape) == len(value.shape), (reward.shape, value.shape)
701	    if isinstance(pcont, (int, float)):
702	        pcont = pcont * torch.ones_like(reward)
703	    dims = list(range(len(reward.shape)))
704	    dims = [axis] + dims[1:axis] + [0] + dims[axis + 1 :]
705	    if axis != 0:
706	        reward = reward.permute(dims)
707	        value = value.permute(dims)
708	        pcont = pcont.permute(dims)
709	    if bootstrap is None:
710	        bootstrap = torch.zeros_like(value[-1])
711	    next_values = torch.cat([value[1:], bootstrap[None]], 0)
712	    inputs = reward + pcont * next_values * (1 - lambda_)
713	    # returns = static_scan(
714	    #    lambda agg, cur0, cur1: cur0 + cur1 * lambda_ * agg,
715	    #    (inputs, pcont), bootstrap, reverse=True)
716	    # reimplement to optimize performance
717	    returns = static_scan_for_lambda_return(
718	        lambda agg, cur0, cur1: cur0 + cur1 * lambda_ * agg, (inputs, pcont), bootstrap
719	    )
720	    if axis != 0:
721	        returns = returns.permute(dims)
722	    return returns
723	
724	
725	def lambda_return_variable_dt(reward, value, pcont, dt, bootstrap, lambda_, axis):
726	    """Lambda-return with variable temporal strides.
727	
728	    Reward is assumed to be cumulative-discounted (pre-computed during sub-sampling).
729	    Discount is raised to the power of dt: gamma^dt.
730	    """
731	    assert len(reward.shape) == len(value.shape), (reward.shape, value.shape)
732	    if isinstance(pcont, (int, float)):
733	        pcont = pcont * torch.ones_like(reward)
734	    if dt.dim() == 2:
735	        dt = dt.unsqueeze(-1)
736	    dt = dt.float()
737	
738	    dims = list(range(len(reward.shape)))
739	    dims = [axis] + dims[1:axis] + [0] + dims[axis + 1:]
740	    if axis != 0:
741	        reward = reward.permute(dims)
742	        value = value.permute(dims)
743	        pcont = pcont.permute(dims)
744	        dt = dt.permute(dims)
745	
746	    if bootstrap is None:
747	        bootstrap = torch.zeros_like(value[-1])
748	
749	    pcont_adj = pcont ** dt
750	
751	    next_values = torch.cat([value[1:], bootstrap[None]], 0)
752	    inputs = reward + pcont_adj * next_values * (1 - lambda_)
753	
754	    returns = static_scan_for_lambda_return(
755	        lambda agg, cur0, cur1: cur0 + cur1 * lambda_ * agg,
756	        (inputs, pcont_adj), bootstrap
757	    )
758	    if axis != 0:
759	        returns = returns.permute(dims)
760	    return returns
761	
762	
763	def subsample_variable_dt(data, max_dt, discount):
764	    """Variable-dt sub-sampling of replay trajectories.
765	
766	    Samples per-element dt from log-uniform over [1, K]. Computes cumulative
767	    discounted reward and minimum continuation for each gap.
768	    """
769	    B, T = data["action"].shape[:2]
770	    device = data["action"].device
771	
772	    log_dt = torch.zeros(B, device=device).uniform_(0, math.log(max_dt))
773	    dt_per_elem = torch.clamp(torch.round(torch.exp(log_dt)).long(), 1, max_dt)
774	
775	    sub_len = torch.ceil(torch.tensor(T, dtype=torch.float) / dt_per_elem.float()).long()
776	    T_sub = sub_len.max().item()
777	
778	    data_sub = {}
779	    dt_labels = torch.ones(B, T_sub, dtype=torch.long, device=device)
780	    reward_cum = torch.zeros(B, T_sub, *data["reward"].shape[2:], device=device)
781	    cont_min = torch.ones(B, T_sub, *data["cont"].shape[2:], device=device)
782	
783	    for b in range(B):
784	        dt_b = dt_per_elem[b].item()
785	        indices = list(range(0, T, dt_b))
786	        L = len(indices)
787	
788	        for key in data:
789	            if key not in data_sub:
790	                data_sub[key] = torch.zeros(
791	                    B, T_sub, *data[key].shape[2:],
792	                    dtype=data[key].dtype, device=device,
793	                )
794	            data_sub[key][b, :L] = data[key][b, indices]
795	
796	        for i, t_start in enumerate(indices[:-1]):
797	            t_end = min(t_start + dt_b, T)
798	            span = t_end - t_start
799	            gamma_powers = discount ** torch.arange(
800	                span, dtype=torch.float, device=device
801	            )
802	            r_slice = data["reward"][b, t_start:t_end]
803	            reward_cum[b, i] = (gamma_powers * r_slice).sum(dim=0)
804	            cont_min[b, i] = data["cont"][b, t_start:t_end].min(dim=0).values
805	
806	        dt_labels[b, :L] = dt_b
807	
808	    data_sub["reward"] = reward_cum
809	    data_sub["cont"] = cont_min
810	    return data_sub, dt_labels
811	
812	
813	class Optimizer:
814	    def __init__(
815	        self,
816	        name,
817	        parameters,
818	        lr,
819	        eps=1e-4,
820	        clip=None,
821	        wd=None,
822	        wd_pattern=r".*",
823	        opt="adam",
824	        use_amp=False,
825	    ):
826	        assert 0 <= wd < 1
827	        assert not clip or 1 <= clip
828	        self._name = name
829	        self._parameters = parameters
830	        self._clip = clip
831	        self._wd = wd
832	        self._wd_pattern = wd_pattern
833	        self._opt = {
834	            "adam": lambda: torch.optim.Adam(parameters, lr=lr, eps=eps),
835	            "nadam": lambda: NotImplemented(f"{opt} is not implemented"),
836	            "adamax": lambda: torch.optim.Adamax(parameters, lr=lr, eps=eps),
837	            "sgd": lambda: torch.optim.SGD(parameters, lr=lr),
838	            "momentum": lambda: torch.optim.SGD(parameters, lr=lr, momentum=0.9),
839	        }[opt]()
840	        self._scaler = torch.cuda.amp.GradScaler(enabled=use_amp)
841	
842	    def __call__(self, loss, params, retain_graph=True):
843	        assert len(loss.shape) == 0, loss.shape
844	        metrics = {}
845	        metrics[f"{self._name}_loss"] = loss.detach().cpu().numpy()
846	        self._opt.zero_grad()
847	        self._scaler.scale(loss).backward(retain_graph=retain_graph)
848	        self._scaler.unscale_(self._opt)
849	        # loss.backward(retain_graph=retain_graph)
850	        norm = torch.nn.utils.clip_grad_norm_(params, self._clip)
851	        if self._wd:
852	            self._apply_weight_decay(params)
853	        self._scaler.step(self._opt)
854	        self._scaler.update()
855	        # self._opt.step()
856	        self._opt.zero_grad()
857	        metrics[f"{self._name}_grad_norm"] = to_np(norm)
858	        return metrics
859	
860	    def _apply_weight_decay(self, varibs):
861	        nontrivial = self._wd_pattern != r".*"
862	        if nontrivial:
863	            raise NotImplementedError
864	        for var in varibs:
865	            var.data = (1 - self._wd) * var.data
866	
867	
868	def args_type(default):
869	    def parse_string(x):
870	        if default is None:
871	            return x
872	        if isinstance(default, bool):
873	            return bool(["False", "True"].index(x))
874	        if isinstance(default, int):
875	            return float(x) if ("e" in x or "." in x) else int(x)
876	        if isinstance(default, (list, tuple)):
877	            return tuple(args_type(default[0])(y) for y in x.split(","))
878	        return type(default)(x)
879	
880	    def parse_object(x):
881	        if isinstance(default, (list, tuple)):
882	            return tuple(x)
883	        return x
884	
885	    return lambda x: parse_string(x) if isinstance(x, str) else parse_object(x)
886	
887	
888	def static_scan(fn, inputs, start):
889	    last = start
890	    indices = range(inputs[0].shape[0])
891	    flag = True
892	    for index in indices:
893	        inp = lambda x: (_input[x] for _input in inputs)
894	        last = fn(last, *inp(index))
895	        if flag:
896	            if type(last) == type({}):
897	                outputs = {
898	                    key: value.clone().unsqueeze(0) for key, value in last.items()
899	                }
900	            else:
901	                outputs = []
902	                for _last in last:
903	                    if type(_last) == type({}):
904	                        outputs.append(
905	                            {
906	                                key: value.clone().unsqueeze(0)
907	                                for key, value in _last.items()
908	                            }
909	                        )
910	                    else:
911	                        outputs.append(_last.clone().unsqueeze(0))
912	            flag = False
913	        else:
914	            if type(last) == type({}):
915	                for key in last.keys():
916	                    outputs[key] = torch.cat(
917	                        [outputs[key], last[key].unsqueeze(0)], dim=0
918	                    )
919	            else:
920	                for j in range(len(outputs)):
921	                    if type(last[j]) == type({}):
922	                        for key in last[j].keys():
923	                            outputs[j][key] = torch.cat(
924	                                [outputs[j][key], last[j][key].unsqueeze(0)], dim=0
925	                            )
926	                    else:
927	                        outputs[j] = torch.cat(
928	                            [outputs[j], last[j].unsqueeze(0)], dim=0
929	                        )
930	    if type(last) == type({}):
931	        outputs = [outputs]
932	    return outputs
933	
934	
935	class Every:
936	    def __init__(self, every):
937	        self._every = every
938	        self._last = None
939	
940	    def __call__(self, step):
941	        if not self._every:
942	            return 0
943	        if self._last is None:
944	            self._last = step
945	            return 1
946	        count = int((step - self._last) / self._every)
947	        self._last += self._every * count
948	        return count
949	
950	
951	class Once:
952	    def __init__(self):
953	        self._once = True
954	
955	    def __call__(self):
956	        if self._once:
957	            self._once = False
958	            return True
959	        return False
960	
961	
962	class Until:
963	    def __init__(self, until):
964	        self._until = until
965	
966	    def __call__(self, step):
967	        if not self._until:
968	            return True
969	        return step < self._until
970	
971	
972	def weight_init(m):
973	    if isinstance(m, nn.Linear):
974	        in_num = m.in_features
975	        out_num = m.out_features
976	        denoms = (in_num + out_num) / 2.0
977	        scale = 1.0 / denoms
978	        std = np.sqrt(scale) / 0.87962566103423978
979	        nn.init.trunc_normal_(
980	            m.weight.data, mean=0.0, std=std, a=-2.0 * std, b=2.0 * std
981	        )
982	        if hasattr(m.bias, "data"):
983	            m.bias.data.fill_(0.0)
984	    elif isinstance(m, nn.Conv2d) or isinstance(m, nn.ConvTranspose2d):
985	        space = m.kernel_size[0] * m.kernel_size[1]
986	        in_num = space * m.in_channels
987	        out_num = space * m.out_channels
988	        denoms = (in_num + out_num) / 2.0
989	        scale = 1.0 / denoms
990	        std = np.sqrt(scale) / 0.87962566103423978
991	        nn.init.trunc_normal_(
992	            m.weight.data, mean=0.0, std=std, a=-2.0 * std, b=2.0 * std
993	        )
994	        if hasattr(m.bias, "data"):
995	            m.bias.data.fill_(0.0)
996	    elif isinstance(m, nn.LayerNorm):
997	        m.weight.data.fill_(1.0)
998	        if hasattr(m.bias, "data"):
999	            m.bias.data.fill_(0.0)
1000	
1001	
1002	def uniform_weight_init(given_scale):
1003	    def f(m):
1004	        if isinstance(m, nn.Linear):
1005	            in_num = m.in_features
1006	            out_num = m.out_features
1007	            denoms = (in_num + out_num) / 2.0
1008	            scale = given_scale / denoms
1009	            limit = np.sqrt(3 * scale)
1010	            nn.init.uniform_(m.weight.data, a=-limit, b=limit)
1011	            if hasattr(m.bias, "data"):
1012	                m.bias.data.fill_(0.0)
1013	        elif isinstance(m, nn.Conv2d) or isinstance(m, nn.ConvTranspose2d):
1014	            space = m.kernel_size[0] * m.kernel_size[1]
1015	            in_num = space * m.in_channels
1016	            out_num = space * m.out_channels
1017	            denoms = (in_num + out_num) / 2.0
1018	            scale = given_scale / denoms
1019	            limit = np.sqrt(3 * scale)
1020	            nn.init.uniform_(m.weight.data, a=-limit, b=limit)
1021	            if hasattr(m.bias, "data"):
1022	                m.bias.data.fill_(0.0)
1023	        elif isinstance(m, nn.LayerNorm):
1024	            m.weight.data.fill_(1.0)
1025	            if hasattr(m.bias, "data"):
1026	                m.bias.data.fill_(0.0)
1027	
1028	    return f
1029	
1030	
1031	def tensorstats(tensor, prefix=None):
1032	    metrics = {
1033	        "mean": to_np(torch.mean(tensor)),
1034	        "std": to_np(torch.std(tensor)),
1035	        "min": to_np(torch.min(tensor)),
1036	        "max": to_np(torch.max(tensor)),
1037	    }
1038	    if prefix:
1039	        metrics = {f"{prefix}_{k}": v for k, v in metrics.items()}
1040	    return metrics
1041	
1042	
1043	def set_seed_everywhere(seed):
1044	    torch.manual_seed(seed)
1045	    if torch.cuda.is_available():
1046	        torch.cuda.manual_seed_all(seed)
1047	    np.random.seed(seed)
1048	    random.seed(seed)
1049	
1050	
1051	def enable_deterministic_run():
1052	    os.environ["CUBLAS_WORKSPACE_CONFIG"] = ":4096:8"
1053	    torch.backends.cudnn.benchmark = False
1054	    torch.use_deterministic_algorithms(True)
1055	
1056	
1057	def recursively_collect_optim_state_dict(
1058	    obj, path="", optimizers_state_dicts=None, visited=None
1059	):
1060	    if optimizers_state_dicts is None:
1061	        optimizers_state_dicts = {}
1062	    if visited is None:
1063	        visited = set()
1064	    # avoid cyclic reference
1065	    if id(obj) in visited:
1066	        return optimizers_state_dicts
1067	    else:
1068	        visited.add(id(obj))
1069	    attrs = obj.__dict__
1070	    if isinstance(obj, torch.nn.Module):
1071	        attrs.update(
1072	            {k: attr for k, attr in obj.named_modules() if "." not in k and obj != attr}
1073	        )
1074	    for name, attr in attrs.items():
1075	        new_path = path + "." + name if path else name
1076	        if isinstance(attr, torch.optim.Optimizer):
1077	            optimizers_state_dicts[new_path] = attr.state_dict()
1078	        elif hasattr(attr, "__dict__"):
1079	            optimizers_state_dicts.update(
1080	                recursively_collect_optim_state_dict(
1081	                    attr, new_path, optimizers_state_dicts, visited
1082	                )
1083	            )
1084	    return optimizers_state_dicts
1085	
1086	
1087	def recursively_load_optim_state_dict(obj, optimizers_state_dicts):
1088	    for path, state_dict in optimizers_state_dicts.items():
1089	        keys = path.split(".")
1090	        obj_now = obj
1091	        for key in keys:
1092	            obj_now = getattr(obj_now, key)
1093	        obj_now.load_state_dict(state_dict)
1094	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4548d576-751a-4385-85b2-ea3732bcaf07",
  "uuid": "7a0c5043-15aa-4ec0-be53-53e6267f1538",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/code/tools.py",
      "content": "# Event-Gated Adaptive-Horizon DreamerV3 — Utility Functions\n# Modified from NM512/dreamerv3-torch.\n# Changes: added lambda_return_variable_dt and subsample_variable_dt.\n\nimport datetime\nimport collections\nimport io\nimport os\nimport json\nimport math\nimport pathlib\nimport re\nimport time\nimport random\n\nimport numpy as np\n\nimport torch\nfrom torch import nn\nfrom torch.nn import functional as F\nfrom torch import distributions as torchd\nfrom torch.utils.tensorboard import SummaryWriter\n\n\nto_np = lambda x: x.detach().cpu().numpy()\n\n\ndef symlog(x):\n    return torch.sign(x) * torch.log(torch.abs(x) + 1.0)\n\n\ndef symexp(x):\n    return torch.sign(x) * (torch.exp(torch.abs(x)) - 1.0)\n\n\nclass RequiresGrad:\n    def __init__(self, model):\n        self._model = model\n\n    def __enter__(self):\n        self._model.requires_grad_(requires_grad=True)\n\n    def __exit__(self, *args):\n        self._model.requires_grad_(requires_grad=False)\n\n\nclass TimeRecording:\n    def __init__(self, comment):\n        self._comment = comment\n\n    def __enter__(self):\n        self._st = torch.cuda.Event(enable_timing=True)\n        self._nd = torch.cuda.Event(enable_timing=True)\n        self._st.record()\n\n    def __exit__(self, *args):\n        self._nd.record()\n        torch.cuda.synchronize()\n        print(self._comment, self._st.elapsed_time(self._nd) / 1000)\n\n\nclass Logger:\n    def __init__(self, logdir, step):\n        self._logdir = logdir\n        self._writer = SummaryWriter(log_dir=str(logdir), max_queue=1000)\n        self._last_step = None\n        self._last_time = None\n        self._scalars = {}\n        self._images = {}\n        self._videos = {}\n        self.step = step\n\n    def scalar(self, name, value):\n        self._scalars[name] = float(value)\n\n    def image(self, name, value):\n        self._images[name] = np.array(value)\n\n    def video(self, name, value):\n        self._videos[name] = np.array(value)\n\n    def write(self, fps=False, step=False):\n        if not step:\n            step = self.step\n        scalars = list(self._scalars.items())\n        if fps:\n            scalars.append((\"fps\", self._compute_fps(step)))\n        print(f\"[{step}]\", \" / \".join(f\"{k} {v:.1f}\" for k, v in scalars))\n        with (self._logdir / \"metrics.jsonl\").open(\"a\") as f:\n            f.write(json.dumps({\"step\": step, **dict(scalars)}) + \"\\n\")\n        for name, value in scalars:\n            if \"/\" not in name:\n                self._writer.add_scalar(\"scalars/\" + name, value, step)\n            else:\n                self._writer.add_scalar(name, value, step)\n        for name, value in self._images.items():\n            self._writer.add_image(name, value, step)\n        for name, value in self._videos.items():\n            name = name if isinstance(name, str) else name.decode(\"utf-8\")\n            if np.issubdtype(value.dtype, np.floating):\n                value = np.clip(255 * value, 0, 255).astype(np.uint8)\n            B, T, H, W, C = value.shape\n            value = value.transpose(1, 4, 2, 0, 3).reshape((1, T, C, H, B * W))\n            self._writer.add_video(name, value, step, 16)\n\n        self._writer.flush()\n        self._scalars = {}\n        self._images = {}\n        self._videos = {}\n\n    def _compute_fps(self, step):\n        if self._last_step is None:\n            self._last_time = time.time()\n            self._last_step = step\n            return 0\n        steps = step - self._last_step\n        duration = time.time() - self._last_time\n        self._last_time += duration\n        self._last_step = step\n        return steps / duration\n\n    def offline_scalar(self, name, value, step):\n        self._writer.add_scalar(\"scalars/\" + name, value, step)\n\n    def offline_video(self, name, value, step):\n        if np.issubdtype(value.dtype, np.floating):\n            value = np.clip(255 * value, 0, 255).astype(np.uint8)\n        B, T, H, W, C = value.shape\n        value = value.transpose(1, 4, 2, 0, 3).reshape((1, T, C, H, B * W))\n        self._writer.add_video(name, value, step, 16)\n\n\ndef simulate(\n    agent,\n    envs,\n    cache,\n    directory,\n    logger,\n    is_eval=False,\n    limit=None,\n    steps=0,\n    episodes=0,\n    state=None,\n):\n    # initialize or unpack simulation state\n    if state is None:\n        step, episode = 0, 0\n        done = np.ones(len(envs), bool)\n        length = np.zeros(len(envs), np.int32)\n        obs = [None] * len(envs)\n        agent_state = None\n        reward = [0] * len(envs)\n    else:\n        step, episode, done, length, obs, agent_state, reward = state\n    while (steps and step < steps) or (episodes and episode < episodes):\n        # reset envs if necessary\n        if done.any():\n            indices = [index for index, d in enumerate(done) if d]\n            results = [envs[i].reset() for i in indices]\n            results = [r() for r in results]\n            for index, result in zip(indices, results):\n                t = result.copy()\n                t = {k: convert(v) for k, v in t.items()}\n                # action will be added to transition in add_to_cache\n                t[\"reward\"] = 0.0\n                t[\"discount\"] = 1.0\n                # initial state should be added to cache\n                add_to_cache(cache, envs[index].id, t)\n                # replace obs with done by initial state\n                obs[index] = result\n        # step agents\n        obs = {k: np.stack([o[k] for o in obs]) for k in obs[0] if \"log_\" not in k}\n        action, agent_state = agent(obs, done, agent_state)\n        if isinstance(action, dict):\n            action = [\n                {k: np.array(action[k][i].detach().cpu()) for k in action}\n                for i in range(len(envs))\n            ]\n        else:\n            action = np.array(action)\n        assert len(action) == len(envs)\n        # step envs\n        results = [e.step(a) for e, a in zip(envs, action)]\n        results = [r() for r in results]\n        obs, reward, done = zip(*[p[:3] for p in results])\n        obs = list(obs)\n        reward = list(reward)\n        done = np.stack(done)\n        episode += int(done.sum())\n        length += 1\n        step += len(envs)\n        length *= 1 - done\n        # add to cache\n        for a, result, env in zip(action, results, envs):\n            o, r, d, info = result\n            o = {k: convert(v) for k, v in o.items()}\n            transition = o.copy()\n            if isinstance(a, dict):\n                transition.update(a)\n            else:\n                transition[\"action\"] = a\n            transition[\"reward\"] = r\n            transition[\"discount\"] = info.get(\"discount\", np.array(1 - float(d)))\n            add_to_cache(cache, env.id, transition)\n\n        if done.any():\n            indices = [index for index, d in enumerate(done) if d]\n            # logging for done episode\n            for i in indices:\n                save_episodes(directory, {envs[i].id: cache[envs[i].id]})\n                length = len(cache[envs[i].id][\"reward\"]) - 1\n                score = float(np.array(cache[envs[i].id][\"reward\"]).sum())\n                video = cache[envs[i].id][\"image\"]\n                # record logs given from environments\n                for key in list(cache[envs[i].id].keys()):\n                    if \"log_\" in key:\n                        logger.scalar(\n                            key, float(np.array(cache[envs[i].id][key]).sum())\n                        )\n                        # log items won't be used later\n                        cache[envs[i].id].pop(key)\n\n                if not is_eval:\n                    step_in_dataset = erase_over_episodes(cache, limit)\n                    logger.scalar(f\"dataset_size\", step_in_dataset)\n                    logger.scalar(f\"train_return\", score)\n                    logger.scalar(f\"train_length\", length)\n                    logger.scalar(f\"train_episodes\", len(cache))\n                    logger.write(step=logger.step)\n                else:\n                    if not \"eval_lengths\" in locals():\n                        eval_lengths = []\n                        eval_scores = []\n                        eval_done = False\n                    # start counting scores for evaluation\n                    eval_scores.append(score)\n                    eval_lengths.append(length)\n\n                    score = sum(eval_scores) / len(eval_scores)\n                    length = sum(eval_lengths) / len(eval_lengths)\n                    logger.video(f\"eval_policy\", np.array(video)[None])\n\n                    if len(eval_scores) >= episodes and not eval_done:\n                        logger.scalar(f\"eval_return\", score)\n                        logger.scalar(f\"eval_length\", length)\n                        logger.scalar(f\"eval_episodes\", len(eval_scores))\n                        logger.write(step=logger.step)\n                        eval_done = True\n    if is_eval:\n        # keep only last item for saving memory. this cache is used for video_pred later\n        while len(cache) > 1:\n            # FIFO\n            cache.popitem(last=False)\n    return (step - steps, episode - episodes, done, length, obs, agent_state, reward)\n\n\ndef add_to_cache(cache, id, transition):\n    if id not in cache:\n        cache[id] = dict()\n        for key, val in transition.items():\n            cache[id][key] = [convert(val)]\n    else:\n        for key, val in transition.items():\n            if key not in cache[id]:\n                # fill missing data(action, etc.) at second time\n                cache[id][key] = [convert(0 * val)]\n                cache[id][key].append(convert(val))\n            else:\n                cache[id][key].append(convert(val))\n\n\ndef erase_over_episodes(cache, dataset_size):\n    step_in_dataset = 0\n    for key, ep in reversed(sorted(cache.items(), key=lambda x: x[0])):\n        if (\n            not dataset_size\n            or step_in_dataset + (len(ep[\"reward\"]) - 1) <= dataset_size\n        ):\n            step_in_dataset += len(ep[\"reward\"]) - 1\n        else:\n            del cache[key]\n    return step_in_dataset\n\n\ndef convert(value, precision=32):\n    value = np.array(value)\n    if np.issubdtype(value.dtype, np.floating):\n        dtype = {16: np.float16, 32: np.float32, 64: np.float64}[precision]\n    elif np.issubdtype(value.dtype, np.signedinteger):\n        dtype = {16: np.int16, 32: np.int32, 64: np.int64}[precision]\n    elif np.issubdtype(value.dtype, np.uint8):\n        dtype = np.uint8\n    elif np.issubdtype(value.dtype, bool):\n        dtype = bool\n    else:\n        raise NotImplementedError(value.dtype)\n    return value.astype(dtype)\n\n\ndef save_episodes(directory, episodes):\n    directory = pathlib.Path(directory).expanduser()\n    directory.mkdir(parents=True, exist_ok=True)\n    for filename, episode in episodes.items():\n        length = len(episode[\"reward\"])\n        filename = directory / f\"{filename}-{length}.npz\"\n        with io.BytesIO() as f1:\n            np.savez_compressed(f1, **episode)\n            f1.seek(0)\n            with filename.open(\"wb\") as f2:\n                f2.write(f1.read())\n    return True\n\n\ndef from_generator(generator, batch_size):\n    while True:\n        batch = []\n        for _ in range(batch_size):\n            batch.append(next(generator))\n        data = {}\n        for key in batch[0].keys():\n            data[key] = []\n            for i in range(batch_size):\n                data[key].append(batch[i][key])\n            data[key] = np.stack(data[key], 0)\n        yield data\n\n\ndef sample_episodes(episodes, length, seed=0):\n    np_random = np.random.RandomState(seed)\n    while True:\n        size = 0\n        ret = None\n        p = np.array(\n            [len(next(iter(episode.values()))) for episode in episodes.values()]\n        )\n        p = p / np.sum(p)\n        while size < length:\n            episode = np_random.choice(list(episodes.values()), p=p)\n            total = len(next(iter(episode.values())))\n            # make sure at least one transition included\n            if total < 2:\n                continue\n            if not ret:\n                index = int(np_random.randint(0, total - 1))\n                ret = {\n                    k: v[index : min(index + length, total)].copy()\n                    for k, v in episode.items()\n                    if \"log_\" not in k\n                }\n                if \"is_first\" in ret:\n                    ret[\"is_first\"][0] = True\n            else:\n                # 'is_first' comes after 'is_last'\n                index = 0\n                possible = length - size\n                ret = {\n                    k: np.append(\n                        ret[k], v[index : min(index + possible, total)].copy(), axis=0\n                    )\n                    for k, v in episode.items()\n                    if \"log_\" not in k\n                }\n                if \"is_first\" in ret:\n                    ret[\"is_first\"][size] = True\n            size = len(next(iter(ret.values())))\n        yield ret\n\n\ndef load_episodes(directory, limit=None, reverse=True):\n    directory = pathlib.Path(directory).expanduser()\n    episodes = collections.OrderedDict()\n    total = 0\n    if reverse:\n        for filename in reversed(sorted(directory.glob(\"*.npz\"))):\n            try:\n                with filename.open(\"rb\") as f:\n                    episode = np.load(f)\n                    episode = {k: episode[k] for k in episode.keys()}\n            except Exception as e:\n                print(f\"Could not load episode: {e}\")\n                continue\n            # extract only filename without extension\n            episodes[str(os.path.splitext(os.path.basename(filename))[0])] = episode\n            total += len(episode[\"reward\"]) - 1\n            if limit and total >= limit:\n                break\n    else:\n        for filename in sorted(directory.glob(\"*.npz\")):\n            try:\n                with filename.open(\"rb\") as f:\n                    episode = np.load(f)\n                    episode = {k: episode[k] for k in episode.keys()}\n            except Exception as e:\n                print(f\"Could not load episode: {e}\")\n                continue\n            episodes[str(filename)] = episode\n            total += len(episode[\"reward\"]) - 1\n            if limit and total >= limit:\n                break\n    return episodes\n\n\nclass SampleDist:\n    def __init__(self, dist, samples=100):\n        self._dist = dist\n        self._samples = samples\n\n    @property\n    def name(self):\n        return \"SampleDist\"\n\n    def __getattr__(self, name):\n        return getattr(self._dist, name)\n\n    def mean(self):\n        samples = self._dist.sample(self._samples)\n        return torch.mean(samples, 0)\n\n    def mode(self):\n        sample = self._dist.sample(self._samples)\n        logprob = self._dist.log_prob(sample)\n        return sample[torch.argmax(logprob)][0]\n\n    def entropy(self):\n        sample = self._dist.sample(self._samples)\n        logprob = self.log_prob(sample)\n        return -torch.mean(logprob, 0)\n\n\nclass OneHotDist(torchd.one_hot_categorical.OneHotCategorical):\n    def __init__(self, logits=None, probs=None, unimix_ratio=0.0):\n        if logits is not None and unimix_ratio > 0.0:\n            probs = F.softmax(logits, dim=-1)\n            probs = probs * (1.0 - unimix_ratio) + unimix_ratio / probs.shape[-1]\n            logits = torch.log(probs)\n            super().__init__(logits=logits, probs=None)\n        else:\n            super().__init__(logits=logits, probs=probs)\n\n    def mode(self):\n        _mode = F.one_hot(\n            torch.argmax(super().logits, axis=-1), super().logits.shape[-1]\n        )\n        return _mode.detach() + super().logits - super().logits.detach()\n\n    def sample(self, sample_shape=(), seed=None):\n        if seed is not None:\n            raise ValueError(\"need to check\")\n        sample = super().sample(sample_shape).detach()\n        probs = super().probs\n        while len(probs.shape) < len(sample.shape):\n            probs = probs[None]\n        sample += probs - probs.detach()\n        return sample\n\n\nclass DiscDist:\n    def __init__(\n        self,\n        logits,\n        low=-20.0,\n        high=20.0,\n        transfwd=symlog,\n        transbwd=symexp,\n        device=\"cuda\",\n    ):\n        self.logits = logits\n        self.probs = torch.softmax(logits, -1)\n        self.buckets = torch.linspace(low, high, steps=255, device=device)\n        self.width = (self.buckets[-1] - self.buckets[0]) / 255\n        self.transfwd = transfwd\n        self.transbwd = transbwd\n\n    def mean(self):\n        _mean = self.probs * self.buckets\n        return self.transbwd(torch.sum(_mean, dim=-1, keepdim=True))\n\n    def mode(self):\n        _mode = self.probs * self.buckets\n        return self.transbwd(torch.sum(_mode, dim=-1, keepdim=True))\n\n    # Inside OneHotCategorical, log_prob is calculated using only max element in targets\n    def log_prob(self, x):\n        x = self.transfwd(x)\n        # x(time, batch, 1)\n        below = torch.sum((self.buckets <= x[..., None]).to(torch.int32), dim=-1) - 1\n        above = len(self.buckets) - torch.sum(\n            (self.buckets > x[..., None]).to(torch.int32), dim=-1\n        )\n        # this is implemented using clip at the original repo as the gradients are not backpropagated for the out of limits.\n        below = torch.clip(below, 0, len(self.buckets) - 1)\n        above = torch.clip(above, 0, len(self.buckets) - 1)\n        equal = below == above\n\n        dist_to_below = torch.where(equal, 1, torch.abs(self.buckets[below] - x))\n        dist_to_above = torch.where(equal, 1, torch.abs(self.buckets[above] - x))\n        total = dist_to_below + dist_to_above\n        weight_below = dist_to_above / total\n        weight_above = dist_to_below / total\n        target = (\n            F.one_hot(below, num_classes=len(self.buckets)) * weight_below[..., None]\n            + F.one_hot(above, num_classes=len(self.buckets)) * weight_above[..., None]\n        )\n        log_pred = self.logits - torch.logsumexp(self.logits, -1, keepdim=True)\n        target = target.squeeze(-2)\n\n        return (target * log_pred).sum(-1)\n\n    def log_prob_target(self, target):\n        log_pred = super().logits - torch.logsumexp(super().logits, -1, keepdim=True)\n        return (target * log_pred).sum(-1)\n\n\nclass MSEDist:\n    def __init__(self, mode, agg=\"sum\"):\n        self._mode = mode\n        self._agg = agg\n\n    def mode(self):\n        return self._mode\n\n    def mean(self):\n        return self._mode\n\n    def log_prob(self, value):\n        assert self._mode.shape == value.shape, (self._mode.shape, value.shape)\n        distance = (self._mode - value) ** 2\n        if self._agg == \"mean\":\n            loss = distance.mean(list(range(len(distance.shape)))[2:])\n        elif self._agg == \"sum\":\n            loss = distance.sum(list(range(len(distance.shape)))[2:])\n        else:\n            raise NotImplementedError(self._agg)\n        return -loss\n\n\nclass SymlogDist:\n    def __init__(self, mode, dist=\"mse\", agg=\"sum\", tol=1e-8):\n        self._mode = mode\n        self._dist = dist\n        self._agg = agg\n        self._tol = tol\n\n    def mode(self):\n        return symexp(self._mode)\n\n    def mean(self):\n        return symexp(self._mode)\n\n    def log_prob(self, value):\n        assert self._mode.shape == value.shape\n        if self._dist == \"mse\":\n            distance = (self._mode - symlog(value)) ** 2.0\n            distance = torch.where(distance < self._tol, 0, distance)\n        elif self._dist == \"abs\":\n            distance = torch.abs(self._mode - symlog(value))\n            distance = torch.where(distance < self._tol, 0, distance)\n        else:\n            raise NotImplementedError(self._dist)\n        if self._agg == \"mean\":\n            loss = distance.mean(list(range(len(distance.shape)))[2:])\n        elif self._agg == \"sum\":\n            loss = distance.sum(list(range(len(distance.shape)))[2:])\n        else:\n            raise NotImplementedError(self._agg)\n        return -loss\n\n\nclass ContDist:\n    def __init__(self, dist=None, absmax=None):\n        super().__init__()\n        self._dist = dist\n        self.mean = dist.mean\n        self.absmax = absmax\n\n    def __getattr__(self, name):\n        return getattr(self._dist, name)\n\n    def entropy(self):\n        return self._dist.entropy()\n\n    def mode(self):\n        out = self._dist.mean\n        if self.absmax is not None:\n            out *= (self.absmax / torch.clip(torch.abs(out), min=self.absmax)).detach()\n        return out\n\n    def sample(self, sample_shape=()):\n        out = self._dist.rsample(sample_shape)\n        if self.absmax is not None:\n            out *= (self.absmax / torch.clip(torch.abs(out), min=self.absmax)).detach()\n        return out\n\n    def log_prob(self, x):\n        return self._dist.log_prob(x)\n\n\nclass Bernoulli:\n    def __init__(self, dist=None):\n        super().__init__()\n        self._dist = dist\n        self.mean = dist.mean\n\n    def __getattr__(self, name):\n        return getattr(self._dist, name)\n\n    def entropy(self):\n        return self._dist.entropy()\n\n    def mode(self):\n        _mode = torch.round(self._dist.mean)\n        return _mode.detach() + self._dist.mean - self._dist.mean.detach()\n\n    def sample(self, sample_shape=()):\n        return self._dist.rsample(sample_shape)\n\n    def log_prob(self, x):\n        _logits = self._dist.base_dist.logits\n        log_probs0 = -F.softplus(_logits)\n        log_probs1 = -F.softplus(-_logits)\n\n        return torch.sum(log_probs0 * (1 - x) + log_probs1 * x, -1)\n\n\nclass UnnormalizedHuber(torchd.normal.Normal):\n    def __init__(self, loc, scale, threshold=1, **kwargs):\n        super().__init__(loc, scale, **kwargs)\n        self._threshold = threshold\n\n    def log_prob(self, event):\n        return -(\n            torch.sqrt((event - self.mean) ** 2 + self._threshold**2) - self._threshold\n        )\n\n    def mode(self):\n        return self.mean\n\n\nclass SafeTruncatedNormal(torchd.normal.Normal):\n    def __init__(self, loc, scale, low, high, clip=1e-6, mult=1):\n        super().__init__(loc, scale)\n        self._low = low\n        self._high = high\n        self._clip = clip\n        self._mult = mult\n\n    def sample(self, sample_shape):\n        event = super().sample(sample_shape)\n        if self._clip:\n            clipped = torch.clip(event, self._low + self._clip, self._high - self._clip)\n            event = event - event.detach() + clipped.detach()\n        if self._mult:\n            event *= self._mult\n        return event\n\n\nclass TanhBijector(torchd.Transform):\n    def __init__(self, validate_args=False, name=\"tanh\"):\n        super().__init__()\n\n    def _forward(self, x):\n        return torch.tanh(x)\n\n    def _inverse(self, y):\n        y = torch.where(\n            (torch.abs(y) <= 1.0), torch.clamp(y, -0.99999997, 0.99999997), y\n        )\n        y = torch.atanh(y)\n        return y\n\n    def _forward_log_det_jacobian(self, x):\n        log2 = torch.math.log(2.0)\n        return 2.0 * (log2 - x - torch.softplus(-2.0 * x))\n\n\ndef static_scan_for_lambda_return(fn, inputs, start):\n    last = start\n    indices = range(inputs[0].shape[0])\n    indices = reversed(indices)\n    flag = True\n    for index in indices:\n        # (inputs, pcont) -> (inputs[index], pcont[index])\n        inp = lambda x: (_input[x] for _input in inputs)\n        last = fn(last, *inp(index))\n        if flag:\n            outputs = last\n            flag = False\n        else:\n            outputs = torch.cat([outputs, last], dim=-1)\n    outputs = torch.reshape(outputs, [outputs.shape[0], outputs.shape[1], 1])\n    outputs = torch.flip(outputs, [1])\n    outputs = torch.unbind(outputs, dim=0)\n    return outputs\n\n\ndef lambda_return(reward, value, pcont, bootstrap, lambda_, axis):\n    # Setting lambda=1 gives a discounted Monte Carlo return.\n    # Setting lambda=0 gives a fixed 1-step return.\n    # assert reward.shape.ndims == value.shape.ndims, (reward.shape, value.shape)\n    assert len(reward.shape) == len(value.shape), (reward.shape, value.shape)\n    if isinstance(pcont, (int, float)):\n        pcont = pcont * torch.ones_like(reward)\n    dims = list(range(len(reward.shape)))\n    dims = [axis] + dims[1:axis] + [0] + dims[axis + 1 :]\n    if axis != 0:\n        reward = reward.permute(dims)\n        value = value.permute(dims)\n        pcont = pcont.permute(dims)\n    if bootstrap is None:\n        bootstrap = torch.zeros_like(value[-1])\n    next_values = torch.cat([value[1:], bootstrap[None]], 0)\n    inputs = reward + pcont * next_values * (1 - lambda_)\n    # returns = static_scan(\n    #    lambda agg, cur0, cur1: cur0 + cur1 * lambda_ * agg,\n    #    (inputs, pcont), bootstrap, reverse=True)\n    # reimplement to optimize performance\n    returns = static_scan_for_lambda_return(\n        lambda agg, cur0, cur1: cur0 + cur1 * lambda_ * agg, (inputs, pcont), bootstrap\n    )\n    if axis != 0:\n        returns = returns.permute(dims)\n    return returns\n\n\ndef lambda_return_variable_dt(reward, value, pcont, dt, bootstrap, lambda_, axis):\n    \"\"\"Lambda-return with variable temporal strides.\n\n    Reward is assumed to be cumulative-discounted (pre-computed during sub-sampling).\n    Discount is raised to the power of dt: gamma^dt.\n    \"\"\"\n    assert len(reward.shape) == len(value.shape), (reward.shape, value.shape)\n    if isinstance(pcont, (int, float)):\n        pcont = pcont * torch.ones_like(reward)\n    if dt.dim() == 2:\n        dt = dt.unsqueeze(-1)\n    dt = dt.float()\n\n    dims = list(range(len(reward.shape)))\n    dims = [axis] + dims[1:axis] + [0] + dims[axis + 1:]\n    if axis != 0:\n        reward = reward.permute(dims)\n        value = value.permute(dims)\n        pcont = pcont.permute(dims)\n        dt = dt.permute(dims)\n\n    if bootstrap is None:\n        bootstrap = torch.zeros_like(value[-1])\n\n    pcont_adj = pcont ** dt\n\n    next_values = torch.cat([value[1:], bootstrap[None]], 0)\n    inputs = reward + pcont_adj * next_values * (1 - lambda_)\n\n    returns = static_scan_for_lambda_return(\n        lambda agg, cur0, cur1: cur0 + cur1 * lambda_ * agg,\n        (inputs, pcont_adj), bootstrap\n    )\n    if axis != 0:\n        returns = returns.permute(dims)\n    return returns\n\n\ndef subsample_variable_dt(data, max_dt, discount):\n    \"\"\"Variable-dt sub-sampling of replay trajectories.\n\n    Samples per-element dt from log-uniform over [1, K]. Computes cumulative\n    discounted reward and minimum continuation for each gap.\n    \"\"\"\n    B, T = data[\"action\"].shape[:2]\n    device = data[\"action\"].device\n\n    log_dt = torch.zeros(B, device=device).uniform_(0, math.log(max_dt))\n    dt_per_elem = torch.clamp(torch.round(torch.exp(log_dt)).long(), 1, max_dt)\n\n    sub_len = torch.ceil(torch.tensor(T, dtype=torch.float) / dt_per_elem.float()).long()\n    T_sub = sub_len.max().item()\n\n    data_sub = {}\n    dt_labels = torch.ones(B, T_sub, dtype=torch.long, device=device)\n    reward_cum = torch.zeros(B, T_sub, *data[\"reward\"].shape[2:], device=device)\n    cont_min = torch.ones(B, T_sub, *data[\"cont\"].shape[2:], device=device)\n\n    for b in range(B):\n        dt_b = dt_per_elem[b].item()\n        indices = list(range(0, T, dt_b))\n        L = len(indices)\n\n        for key in data:\n            if key not in data_sub:\n                data_sub[key] = torch.zeros(\n                    B, T_sub, *data[key].shape[2:],\n                    dtype=data[key].dtype, device=device,\n                )\n            data_sub[key][b, :L] = data[key][b, indices]\n\n        for i, t_start in enumerate(indices[:-1]):\n            t_end = min(t_start + dt_b, T)\n            span = t_end - t_start\n            gamma_powers = discount ** torch.arange(\n                span, dtype=torch.float, device=device\n            )\n            r_slice = data[\"reward\"][b, t_start:t_end]\n            reward_cum[b, i] = (gamma_powers * r_slice).sum(dim=0)\n            cont_min[b, i] = data[\"cont\"][b, t_start:t_end].min(dim=0).values\n\n        dt_labels[b, :L] = dt_b\n\n    data_sub[\"reward\"] = reward_cum\n    data_sub[\"cont\"] = cont_min\n    return data_sub, dt_labels\n\n\nclass Optimizer:\n    def __init__(\n        self,\n        name,\n        parameters,\n        lr,\n        eps=1e-4,\n        clip=None,\n        wd=None,\n        wd_pattern=r\".*\",\n        opt=\"adam\",\n        use_amp=False,\n    ):\n        assert 0 <= wd < 1\n        assert not clip or 1 <= clip\n        self._name = name\n        self._parameters = parameters\n        self._clip = clip\n        self._wd = wd\n        self._wd_pattern = wd_pattern\n        self._opt = {\n            \"adam\": lambda: torch.optim.Adam(parameters, lr=lr, eps=eps),\n            \"nadam\": lambda: NotImplemented(f\"{opt} is not implemented\"),\n            \"adamax\": lambda: torch.optim.Adamax(parameters, lr=lr, eps=eps),\n            \"sgd\": lambda: torch.optim.SGD(parameters, lr=lr),\n            \"momentum\": lambda: torch.optim.SGD(parameters, lr=lr, momentum=0.9),\n        }[opt]()\n        self._scaler = torch.cuda.amp.GradScaler(enabled=use_amp)\n\n    def __call__(self, loss, params, retain_graph=True):\n        assert len(loss.shape) == 0, loss.shape\n        metrics = {}\n        metrics[f\"{self._name}_loss\"] = loss.detach().cpu().numpy()\n        self._opt.zero_grad()\n        self._scaler.scale(loss).backward(retain_graph=retain_graph)\n        self._scaler.unscale_(self._opt)\n        # loss.backward(retain_graph=retain_graph)\n        norm = torch.nn.utils.clip_grad_norm_(params, self._clip)\n        if self._wd:\n            self._apply_weight_decay(params)\n        self._scaler.step(self._opt)\n        self._scaler.update()\n        # self._opt.step()\n        self._opt.zero_grad()\n        metrics[f\"{self._name}_grad_norm\"] = to_np(norm)\n        return metrics\n\n    def _apply_weight_decay(self, varibs):\n        nontrivial = self._wd_pattern != r\".*\"\n        if nontrivial:\n            raise NotImplementedError\n        for var in varibs:\n            var.data = (1 - self._wd) * var.data\n\n\ndef args_type(default):\n    def parse_string(x):\n        if default is None:\n            return x\n        if isinstance(default, bool):\n            return bool([\"False\", \"True\"].index(x))\n        if isinstance(default, int):\n            return float(x) if (\"e\" in x or \".\" in x) else int(x)\n        if isinstance(default, (list, tuple)):\n            return tuple(args_type(default[0])(y) for y in x.split(\",\"))\n        return type(default)(x)\n\n    def parse_object(x):\n        if isinstance(default, (list, tuple)):\n            return tuple(x)\n        return x\n\n    return lambda x: parse_string(x) if isinstance(x, str) else parse_object(x)\n\n\ndef static_scan(fn, inputs, start):\n    last = start\n    indices = range(inputs[0].shape[0])\n    flag = True\n    for index in indices:\n        inp = lambda x: (_input[x] for _input in inputs)\n        last = fn(last, *inp(index))\n        if flag:\n            if type(last) == type({}):\n                outputs = {\n                    key: value.clone().unsqueeze(0) for key, value in last.items()\n                }\n            else:\n                outputs = []\n                for _last in last:\n                    if type(_last) == type({}):\n                        outputs.append(\n                            {\n                                key: value.clone().unsqueeze(0)\n                                for key, value in _last.items()\n                            }\n                        )\n                    else:\n                        outputs.append(_last.clone().unsqueeze(0))\n            flag = False\n        else:\n            if type(last) == type({}):\n                for key in last.keys():\n                    outputs[key] = torch.cat(\n                        [outputs[key], last[key].unsqueeze(0)], dim=0\n                    )\n            else:\n                for j in range(len(outputs)):\n                    if type(last[j]) == type({}):\n                        for key in last[j].keys():\n                            outputs[j][key] = torch.cat(\n                                [outputs[j][key], last[j][key].unsqueeze(0)], dim=0\n                            )\n                    else:\n                        outputs[j] = torch.cat(\n                            [outputs[j], last[j].unsqueeze(0)], dim=0\n                        )\n    if type(last) == type({}):\n        outputs = [outputs]\n    return outputs\n\n\nclass Every:\n    def __init__(self, every):\n        self._every = every\n        self._last = None\n\n    def __call__(self, step):\n        if not self._every:\n            return 0\n        if self._last is None:\n            self._last = step\n            return 1\n        count = int((step - self._last) / self._every)\n        self._last += self._every * count\n        return count\n\n\nclass Once:\n    def __init__(self):\n        self._once = True\n\n    def __call__(self):\n        if self._once:\n            self._once = False\n            return True\n        return False\n\n\nclass Until:\n    def __init__(self, until):\n        self._until = until\n\n    def __call__(self, step):\n        if not self._until:\n            return True\n        return step < self._until\n\n\ndef weight_init(m):\n    if isinstance(m, nn.Linear):\n        in_num = m.in_features\n        out_num = m.out_features\n        denoms = (in_num + out_num) / 2.0\n        scale = 1.0 / denoms\n        std = np.sqrt(scale) / 0.87962566103423978\n        nn.init.trunc_normal_(\n            m.weight.data, mean=0.0, std=std, a=-2.0 * std, b=2.0 * std\n        )\n        if hasattr(m.bias, \"data\"):\n            m.bias.data.fill_(0.0)\n    elif isinstance(m, nn.Conv2d) or isinstance(m, nn.ConvTranspose2d):\n        space = m.kernel_size[0] * m.kernel_size[1]\n        in_num = space * m.in_channels\n        out_num = space * m.out_channels\n        denoms = (in_num + out_num) / 2.0\n        scale = 1.0 / denoms\n        std = np.sqrt(scale) / 0.87962566103423978\n        nn.init.trunc_normal_(\n            m.weight.data, mean=0.0, std=std, a=-2.0 * std, b=2.0 * std\n        )\n        if hasattr(m.bias, \"data\"):\n            m.bias.data.fill_(0.0)\n    elif isinstance(m, nn.LayerNorm):\n        m.weight.data.fill_(1.0)\n        if hasattr(m.bias, \"data\"):\n            m.bias.data.fill_(0.0)\n\n\ndef uniform_weight_init(given_scale):\n    def f(m):\n        if isinstance(m, nn.Linear):\n            in_num = m.in_features\n            out_num = m.out_features\n            denoms = (in_num + out_num) / 2.0\n            scale = given_scale / denoms\n            limit = np.sqrt(3 * scale)\n            nn.init.uniform_(m.weight.data, a=-limit, b=limit)\n            if hasattr(m.bias, \"data\"):\n                m.bias.data.fill_(0.0)\n        elif isinstance(m, nn.Conv2d) or isinstance(m, nn.ConvTranspose2d):\n            space = m.kernel_size[0] * m.kernel_size[1]\n            in_num = space * m.in_channels\n            out_num = space * m.out_channels\n            denoms = (in_num + out_num) / 2.0\n            scale = given_scale / denoms\n            limit = np.sqrt(3 * scale)\n            nn.init.uniform_(m.weight.data, a=-limit, b=limit)\n            if hasattr(m.bias, \"data\"):\n                m.bias.data.fill_(0.0)\n        elif isinstance(m, nn.LayerNorm):\n            m.weight.data.fill_(1.0)\n            if hasattr(m.bias, \"data\"):\n                m.bias.data.fill_(0.0)\n\n    return f\n\n\ndef tensorstats(tensor, prefix=None):\n    metrics = {\n        \"mean\": to_np(torch.mean(tensor)),\n        \"std\": to_np(torch.std(tensor)),\n        \"min\": to_np(torch.min(tensor)),\n        \"max\": to_np(torch.max(tensor)),\n    }\n    if prefix:\n        metrics = {f\"{prefix}_{k}\": v for k, v in metrics.items()}\n    return metrics\n\n\ndef set_seed_everywhere(seed):\n    torch.manual_seed(seed)\n    if torch.cuda.is_available():\n        torch.cuda.manual_seed_all(seed)\n    np.random.seed(seed)\n    random.seed(seed)\n\n\ndef enable_deterministic_run():\n    os.environ[\"CUBLAS_WORKSPACE_CONFIG\"] = \":4096:8\"\n    torch.backends.cudnn.benchmark = False\n    torch.use_deterministic_algorithms(True)\n\n\ndef recursively_collect_optim_state_dict(\n    obj, path=\"\", optimizers_state_dicts=None, visited=None\n):\n    if optimizers_state_dicts is None:\n        optimizers_state_dicts = {}\n    if visited is None:\n        visited = set()\n    # avoid cyclic reference\n    if id(obj) in visited:\n        return optimizers_state_dicts\n    else:\n        visited.add(id(obj))\n    attrs = obj.__dict__\n    if isinstance(obj, torch.nn.Module):\n        attrs.update(\n            {k: attr for k, attr in obj.named_modules() if \".\" not in k and obj != attr}\n        )\n    for name, attr in attrs.items():\n        new_path = path + \".\" + name if path else name\n        if isinstance(attr, torch.optim.Optimizer):\n            optimizers_state_dicts[new_path] = attr.state_dict()\n        elif hasattr(attr, \"__dict__\"):\n            optimizers_state_dicts.update(\n                recursively_collect_optim_state_dict(\n                    attr, new_path, optimizers_state_dicts, visited\n                )\n            )\n    return optimizers_state_dicts\n\n\ndef recursively_load_optim_state_dict(obj, optimizers_state_dicts):\n    for path, state_dict in optimizers_state_dicts.items():\n        keys = path.split(\".\")\n        obj_now = obj\n        for key in keys:\n            obj_now = getattr(obj_now, key)\n        obj_now.load_state_dict(state_dict)\n",
      "numLines": 1094,
      "startLine": 1,
      "totalLines": 1094
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Read · `toolu_01NdjaFfUGkwNc6RCQmMPup4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/code/models.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4548d576-751a-4385-85b2-ea3732bcaf07",
  "uuid": "e6b31205-6133-4cc1-9f86-8c3d1b5af7ca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016GuVmj2V9ExwAqz6ZGPFNZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 473,
      "cache_read_input_tokens": 23995,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 473
      },
      "output_tokens": 70,
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

_source line 13 · 2026-05-13T04:07:25.312Z_

<details><summary>↩ Tool result · `toolu_01NdjaFfUGkwNc6RCQmMPup4`</summary>

```text
1	# Event-Gated Adaptive-Horizon DreamerV3 — World Model & Behavior
2	# Modified from NM512/dreamerv3-torch.
3	# Changes: WorldModel integrates EventGate + variable-dt sub-sampling;
4	#          ImagBehavior uses gate-driven dt in imagination + adapted lambda-returns.
5	
6	import copy
7	import math
8	
9	import torch
10	from torch import nn
11	from torch.nn import functional as F
12	
13	import networks
14	import tools
15	
16	to_np = lambda x: x.detach().cpu().numpy()
17	
18	
19	def compute_gate_targets(feats, max_dt):
20	    """Soft supervision target for the event gate derived from state deltas.
21	
22	    Large delta -> prefer small dt (index 0 = dt=1).
23	    Small delta -> prefer large dt (index K-1 = dt=K).
24	    """
25	    feats = feats.detach()
26	    deltas = torch.norm(feats[1:] - feats[:-1], dim=-1)  # (time-1, batch)
27	    delta_min = deltas.min(dim=0, keepdim=True).values
28	    delta_max = deltas.max(dim=0, keepdim=True).values
29	    delta_norm = (deltas - delta_min) / (delta_max - delta_min + 1e-8)
30	    preferred_dt = 1.0 + (max_dt - 1.0) * (1.0 - delta_norm)
31	    dt_indices = torch.arange(1, max_dt + 1, dtype=torch.float32, device=feats.device)
32	    sigma = 1.0
33	    log_probs = -0.5 * ((preferred_dt.unsqueeze(-1) - dt_indices) / sigma) ** 2
34	    target_dist = F.softmax(log_probs, dim=-1)
35	    return target_dist
36	
37	
38	def gate_loss_fn(gate_logits, target_dist):
39	    """Cross-entropy between gate predictions and supervision target."""
40	    log_probs = F.log_softmax(gate_logits, dim=-1)
41	    return -(target_dist * log_probs).sum(dim=-1)
42	
43	
44	class RewardEMA:
45	    """running mean and std"""
46	
47	    def __init__(self, device, alpha=1e-2):
48	        self.device = device
49	        self.alpha = alpha
50	        self.range = torch.tensor([0.05, 0.95], device=device)
51	
52	    def __call__(self, x, ema_vals):
53	        flat_x = torch.flatten(x.detach())
54	        x_quantile = torch.quantile(input=flat_x, q=self.range)
55	        # this should be in-place operation
56	        ema_vals[:] = self.alpha * x_quantile + (1 - self.alpha) * ema_vals
57	        scale = torch.clip(ema_vals[1] - ema_vals[0], min=1.0)
58	        offset = ema_vals[0]
59	        return offset.detach(), scale.detach()
60	
61	
62	class WorldModel(nn.Module):
63	    def __init__(self, obs_space, act_space, step, config):
64	        super(WorldModel, self).__init__()
65	        self._step = step
66	        self._use_amp = True if config.precision == 16 else False
67	        self._config = config
68	        shapes = {k: tuple(v.shape) for k, v in obs_space.spaces.items()}
69	        self.encoder = networks.MultiEncoder(shapes, **config.encoder)
70	        self.embed_size = self.encoder.outdim
71	        self.dynamics = networks.RSSM(
72	            config.dyn_stoch,
73	            config.dyn_deter,
74	            config.dyn_hidden,
75	            config.dyn_rec_depth,
76	            config.dyn_discrete,
77	            config.act,
78	            config.norm,
79	            config.dyn_mean_act,
80	            config.dyn_std_act,
81	            config.dyn_min_std,
82	            config.unimix_ratio,
83	            config.initial,
84	            config.num_actions,
85	            self.embed_size,
86	            config.device,
87	            max_dt=config.gate_max_dt if config.gate_enabled else 1,
88	            dt_embed_dim=config.gate_dt_embed_dim,
89	        )
90	        self.heads = nn.ModuleDict()
91	        if config.dyn_discrete:
92	            feat_size = config.dyn_stoch * config.dyn_discrete + config.dyn_deter
93	        else:
94	            feat_size = config.dyn_stoch + config.dyn_deter
95	        self.heads["decoder"] = networks.MultiDecoder(
96	            feat_size, shapes, **config.decoder
97	        )
98	        self.heads["reward"] = networks.MLP(
99	            feat_size,
100	            (255,) if config.reward_head["dist"] == "symlog_disc" else (),
101	            config.reward_head["layers"],
102	            config.units,
103	            config.act,
104	            config.norm,
105	            dist=config.reward_head["dist"],
106	            outscale=config.reward_head["outscale"],
107	            device=config.device,
108	            name="Reward",
109	        )
110	        self.heads["cont"] = networks.MLP(
111	            feat_size,
112	            (),
113	            config.cont_head["layers"],
114	            config.units,
115	            config.act,
116	            config.norm,
117	            dist="binary",
118	            outscale=config.cont_head["outscale"],
119	            device=config.device,
120	            name="Cont",
121	        )
122	
123	        if config.gate_enabled:
124	            self.event_gate = networks.EventGate(
125	                feat_size=feat_size,
126	                max_dt=config.gate_max_dt,
127	                hidden_units=config.gate_hidden_units,
128	                hidden_layers=config.gate_hidden_layers,
129	                act=config.act,
130	                norm=config.norm,
131	                tau_init=config.gate_tau_init,
132	                tau_final=config.gate_tau_final,
133	                tau_anneal_steps=config.gate_tau_anneal_steps,
134	            )
135	            self.register_buffer(
136	                "gate_step", torch.tensor(0, dtype=torch.long)
137	            )
138	        else:
139	            self.event_gate = None
140	
141	        for name in config.grad_heads:
142	            assert name in self.heads, name
143	        self._model_opt = tools.Optimizer(
144	            "model",
145	            self.parameters(),
146	            config.model_lr,
147	            config.opt_eps,
148	            config.grad_clip,
149	            config.weight_decay,
150	            opt=config.opt,
151	            use_amp=self._use_amp,
152	        )
153	        print(
154	            f"Optimizer model_opt has {sum(param.numel() for param in self.parameters())} variables."
155	        )
156	        # other losses are scaled by 1.0.
157	        self._scales = dict(
158	            reward=config.reward_head["loss_scale"],
159	            cont=config.cont_head["loss_scale"],
160	        )
161	
162	    def _train(self, data):
163	        # action (batch_size, batch_length, act_dim)
164	        # image (batch_size, batch_length, h, w, ch)
165	        # reward (batch_size, batch_length)
166	        # discount (batch_size, batch_length)
167	        data = self.preprocess(data)
168	
169	        if self._config.gate_enabled:
170	            self.gate_step += 1
171	            data, dt_labels = tools.subsample_variable_dt(
172	                data, self._config.gate_max_dt, self._config.discount,
173	            )
174	        else:
175	            dt_labels = None
176	
177	        with tools.RequiresGrad(self):
178	            with torch.cuda.amp.autocast(self._use_amp):
179	                embed = self.encoder(data)
180	                if dt_labels is not None:
181	                    post, prior = self.dynamics.observe(
182	                        embed, data["action"], data["is_first"],
183	                        dt_labels=dt_labels,
184	                    )
185	                else:
186	                    post, prior = self.dynamics.observe(
187	                        embed, data["action"], data["is_first"]
188	                    )
189	                kl_free = self._config.kl_free
190	                dyn_scale = self._config.dyn_scale
191	                rep_scale = self._config.rep_scale
192	                kl_loss, kl_value, dyn_loss, rep_loss = self.dynamics.kl_loss(
193	                    post, prior, kl_free, dyn_scale, rep_scale
194	                )
195	                assert kl_loss.shape == embed.shape[:2], kl_loss.shape
196	                preds = {}
197	                for name, head in self.heads.items():
198	                    grad_head = name in self._config.grad_heads
199	                    feat = self.dynamics.get_feat(post)
200	                    feat = feat if grad_head else feat.detach()
201	                    pred = head(feat)
202	                    if type(pred) is dict:
203	                        preds.update(pred)
204	                    else:
205	                        preds[name] = pred
206	                losses = {}
207	                for name, pred in preds.items():
208	                    loss = -pred.log_prob(data[name])
209	                    assert loss.shape == embed.shape[:2], (name, loss.shape)
210	                    losses[name] = loss
211	                scaled = {
212	                    key: value * self._scales.get(key, 1.0)
213	                    for key, value in losses.items()
214	                }
215	                model_loss = sum(scaled.values()) + kl_loss
216	                mean_model_loss = torch.mean(model_loss)
217	
218	                if self._config.gate_enabled and self.event_gate is not None:
219	                    gate_feat = self.dynamics.get_feat(post).detach()
220	                    B_g, T_g, D_g = gate_feat.shape
221	                    gate_feat_flat = gate_feat.reshape(B_g * T_g, D_g)
222	                    step = self.gate_step.item()
223	                    _, _, gate_logits_flat = self.event_gate(
224	                        gate_feat_flat, step, hard=False
225	                    )
226	                    gate_logits = gate_logits_flat.reshape(
227	                        B_g, T_g, self._config.gate_max_dt
228	                    )
229	
230	                    feat_time = gate_feat.permute(1, 0, 2)
231	                    target_dist = compute_gate_targets(
232	                        feat_time, self._config.gate_max_dt
233	                    )
234	
235	                    g_logits = gate_logits[:, 1:, :].permute(1, 0, 2)
236	                    g_loss = gate_loss_fn(g_logits, target_dist)
237	
238	                    g_entropy = self.event_gate.entropy(
239	                        g_logits.reshape(-1, self._config.gate_max_dt)
240	                    ).reshape(g_loss.shape)
241	
242	                    if step < self._config.gate_curriculum_phase1:
243	                        gate_scale = 0.0
244	                    elif step < self._config.gate_curriculum_phase2:
245	                        progress = (step - self._config.gate_curriculum_phase1) / (
246	                            self._config.gate_curriculum_phase2
247	                            - self._config.gate_curriculum_phase1
248	                        )
249	                        gate_scale = progress
250	                    else:
251	                        gate_scale = 1.0
252	
253	                    entropy_frac = min(
254	                        step / max(self._config.gate_tau_anneal_steps, 1), 1.0
255	                    )
256	                    effective_entropy_bonus = (
257	                        self._config.gate_entropy_bonus_init
258	                        + entropy_frac
259	                        * (
260	                            self._config.gate_entropy_bonus_final
261	                            - self._config.gate_entropy_bonus_init
262	                        )
263	                    )
264	
265	                    total_gate_loss = gate_scale * (
266	                        self._config.gate_loss_weight * g_loss.mean()
267	                        - effective_entropy_bonus * g_entropy.mean()
268	                    )
269	                    mean_model_loss = mean_model_loss + total_gate_loss
270	
271	            metrics = self._model_opt(mean_model_loss, self.parameters())
272	
273	        # Store scalar metrics to avoid keeping (batch,time) arrays until the next log step.
274	        metrics.update(
275	            {f"{name}_loss": to_np(torch.mean(loss)) for name, loss in losses.items()}
276	        )
277	        metrics["kl_free"] = kl_free
278	        metrics["dyn_scale"] = dyn_scale
279	        metrics["rep_scale"] = rep_scale
280	        metrics["dyn_loss"] = to_np(torch.mean(dyn_loss))
281	        metrics["rep_loss"] = to_np(torch.mean(rep_loss))
282	        metrics["kl"] = to_np(torch.mean(kl_value))
283	        with torch.cuda.amp.autocast(self._use_amp):
284	            metrics["prior_ent"] = to_np(
285	                torch.mean(self.dynamics.get_dist(prior).entropy())
286	            )
287	            metrics["post_ent"] = to_np(
288	                torch.mean(self.dynamics.get_dist(post).entropy())
289	            )
290	            context = dict(
291	                embed=embed,
292	                feat=self.dynamics.get_feat(post),
293	                kl=kl_value,
294	                postent=self.dynamics.get_dist(post).entropy(),
295	            )
296	
297	        if self._config.gate_enabled and self.event_gate is not None:
298	            metrics["gate_loss"] = to_np(total_gate_loss)
299	            metrics["gate_scale"] = gate_scale
300	            metrics["gate_entropy_bonus"] = effective_entropy_bonus
301	
302	        post = {k: v.detach() for k, v in post.items()}
303	        return post, context, metrics
304	
305	    # this function is called during both rollout and training
306	    def preprocess(self, obs):
307	        obs = {
308	            k: torch.tensor(v, device=self._config.device, dtype=torch.float32)
309	            for k, v in obs.items()
310	        }
311	        obs["image"] = obs["image"] / 255.0
312	        if "discount" in obs:
313	            obs["discount"] *= self._config.discount
314	            # (batch_size, batch_length) -> (batch_size, batch_length, 1)
315	            obs["discount"] = obs["discount"].unsqueeze(-1)
316	        # 'is_first' is necesarry to initialize hidden state at training
317	        assert "is_first" in obs
318	        # 'is_terminal' is necesarry to train cont_head
319	        assert "is_terminal" in obs
320	        obs["cont"] = (1.0 - obs["is_terminal"]).unsqueeze(-1)
321	        return obs
322	
323	    def video_pred(self, data):
324	        data = self.preprocess(data)
325	        embed = self.encoder(data)
326	
327	        states, _ = self.dynamics.observe(
328	            embed[:6, :5], data["action"][:6, :5], data["is_first"][:6, :5]
329	        )
330	        recon = self.heads["decoder"](self.dynamics.get_feat(states))["image"].mode()[
331	            :6
332	        ]
333	        reward_post = self.heads["reward"](self.dynamics.get_feat(states)).mode()[:6]
334	        init = {k: v[:, -1] for k, v in states.items()}
335	        prior = self.dynamics.imagine_with_action(data["action"][:6, 5:], init)
336	        openl = self.heads["decoder"](self.dynamics.get_feat(prior))["image"].mode()
337	        reward_prior = self.heads["reward"](self.dynamics.get_feat(prior)).mode()
338	        # observed image is given until 5 steps
339	        model = torch.cat([recon[:, :5], openl], 1)
340	        truth = data["image"][:6]
341	        model = model
342	        error = (model - truth + 1.0) / 2.0
343	
344	        return torch.cat([truth, model, error], 2)
345	
346	
347	class ImagBehavior(nn.Module):
348	    def __init__(self, config, world_model):
349	        super(ImagBehavior, self).__init__()
350	        self._use_amp = True if config.precision == 16 else False
351	        self._config = config
352	        self._world_model = world_model
353	        if config.dyn_discrete:
354	            feat_size = config.dyn_stoch * config.dyn_discrete + config.dyn_deter
355	        else:
356	            feat_size = config.dyn_stoch + config.dyn_deter
357	        self.actor = networks.MLP(
358	            feat_size,
359	            (config.num_actions,),
360	            config.actor["layers"],
361	            config.units,
362	            config.act,
363	            config.norm,
364	            config.actor["dist"],
365	            config.actor["std"],
366	            config.actor["min_std"],
367	            config.actor["max_std"],
368	            absmax=1.0,
369	            temp=config.actor["temp"],
370	            unimix_ratio=config.actor["unimix_ratio"],
371	            outscale=config.actor["outscale"],
372	            name="Actor",
373	        )
374	        self.value = networks.MLP(
375	            feat_size,
376	            (255,) if config.critic["dist"] == "symlog_disc" else (),
377	            config.critic["layers"],
378	            config.units,
379	            config.act,
380	            config.norm,
381	            config.critic["dist"],
382	            outscale=config.critic["outscale"],
383	            device=config.device,
384	            name="Value",
385	        )
386	        if config.critic["slow_target"]:
387	            self._slow_value = copy.deepcopy(self.value)
388	            self._updates = 0
389	        kw = dict(wd=config.weight_decay, opt=config.opt, use_amp=self._use_amp)
390	        self._actor_opt = tools.Optimizer(
391	            "actor",
392	            self.actor.parameters(),
393	            config.actor["lr"],
394	            config.actor["eps"],
395	            config.actor["grad_clip"],
396	            **kw,
397	        )
398	        print(
399	            f"Optimizer actor_opt has {sum(param.numel() for param in self.actor.parameters())} variables."
400	        )
401	        self._value_opt = tools.Optimizer(
402	            "value",
403	            self.value.parameters(),
404	            config.critic["lr"],
405	            config.critic["eps"],
406	            config.critic["grad_clip"],
407	            **kw,
408	        )
409	        print(
410	            f"Optimizer value_opt has {sum(param.numel() for param in self.value.parameters())} variables."
411	        )
412	        if self._config.reward_EMA:
413	            # register ema_vals to nn.Module for enabling torch.save and torch.load
414	            self.register_buffer(
415	                "ema_vals", torch.zeros((2,), device=self._config.device)
416	            )
417	            self.reward_ema = RewardEMA(device=self._config.device)
418	
419	    def _train(
420	        self,
421	        start,
422	        objective,
423	    ):
424	        self._update_slow_target()
425	        metrics = {}
426	
427	        with tools.RequiresGrad(self.actor):
428	            with torch.cuda.amp.autocast(self._use_amp):
429	                if self._config.gate_enabled:
430	                    imag_feat, imag_state, imag_action, dts = self._imagine(
431	                        start, self.actor, self._config.imag_horizon
432	                    )
433	                else:
434	                    imag_feat, imag_state, imag_action = self._imagine(
435	                        start, self.actor, self._config.imag_horizon
436	                    )
437	                    dts = None
438	                reward = objective(imag_feat, imag_state, imag_action)
439	                actor_ent = self.actor(imag_feat).entropy()
440	                state_ent = self._world_model.dynamics.get_dist(imag_state).entropy()
441	                # this target is not scaled by ema or sym_log.
442	                target, weights, base = self._compute_target(
443	                    imag_feat, imag_state, reward, dts=dts
444	                )
445	                actor_loss, mets = self._compute_actor_loss(
446	                    imag_feat,
447	                    imag_action,
448	                    target,
449	                    weights,
450	                    base,
451	                )
452	                actor_loss -= self._config.actor["entropy"] * actor_ent[:-1, ..., None]
453	                actor_loss = torch.mean(actor_loss)
454	                metrics.update(mets)
455	                value_input = imag_feat
456	
457	        with tools.RequiresGrad(self.value):
458	            with torch.cuda.amp.autocast(self._use_amp):
459	                value = self.value(value_input[:-1].detach())
460	                target = torch.stack(target, dim=1)
461	                # (time, batch, 1), (time, batch, 1) -> (time, batch)
462	                value_loss = -value.log_prob(target.detach())
463	                slow_target = self._slow_value(value_input[:-1].detach())
464	                if self._config.critic["slow_target"]:
465	                    value_loss -= value.log_prob(slow_target.mode().detach())
466	                # (time, batch, 1), (time, batch, 1) -> (1,)
467	                value_loss = torch.mean(weights[:-1] * value_loss[:, :, None])
468	
469	        metrics.update(tools.tensorstats(value.mode(), "value"))
470	        metrics.update(tools.tensorstats(target, "target"))
471	        metrics.update(tools.tensorstats(reward, "imag_reward"))
472	        if self._config.actor["dist"] in ["onehot"]:
473	            metrics.update(
474	                tools.tensorstats(
475	                    torch.argmax(imag_action, dim=-1).float(), "imag_action"
476	                )
477	            )
478	        else:
479	            metrics.update(tools.tensorstats(imag_action, "imag_action"))
480	        metrics["actor_entropy"] = to_np(torch.mean(actor_ent))
481	
482	        if self._config.gate_enabled and dts is not None:
483	            dts_float = dts.float()
484	            metrics["gate_dt_mean"] = to_np(torch.mean(dts_float))
485	            metrics["gate_dt_std"] = to_np(torch.std(dts_float))
486	            metrics["gate_dt_min"] = to_np(torch.min(dts_float))
487	            metrics["gate_dt_max"] = to_np(torch.max(dts_float))
488	            dt_counts = torch.bincount(
489	                dts.reshape(-1).long(),
490	                minlength=self._config.gate_max_dt + 1,
491	            )[1:]
492	            dt_dist = dt_counts.float() / dt_counts.sum()
493	            for k in range(self._config.gate_max_dt):
494	                metrics[f"gate_dt_{k+1}_frac"] = to_np(dt_dist[k])
495	            emp_entropy = -(dt_dist * torch.log(dt_dist + 1e-8)).sum()
496	            metrics["gate_empirical_entropy"] = to_np(emp_entropy)
497	            max_entropy = math.log(self._config.gate_max_dt)
498	            metrics["gate_entropy_ratio"] = to_np(emp_entropy) / max_entropy
499	
500	        with tools.RequiresGrad(self):
501	            metrics.update(self._actor_opt(actor_loss, self.actor.parameters()))
502	            metrics.update(self._value_opt(value_loss, self.value.parameters()))
503	        return imag_feat, imag_state, imag_action, weights, metrics
504	
505	    def _imagine(self, start, policy, horizon):
506	        dynamics = self._world_model.dynamics
507	        flatten = lambda x: x.reshape([-1] + list(x.shape[2:]))
508	        start = {k: flatten(v) for k, v in start.items()}
509	
510	        if self._config.gate_enabled:
511	            gate = self._world_model.event_gate
512	            config = self._config
513	            step = self._world_model.gate_step.item() if hasattr(
514	                self._world_model, "gate_step"
515	            ) else 0
516	            gate_active = (
517	                gate is not None and step > config.gate_curriculum_phase1
518	            )
519	
520	            def step_fn(prev, _):
521	                state, _, _, prev_dt = prev
522	                feat = dynamics.get_feat(state)
523	                inp = feat.detach()
524	                action = policy(inp).sample()
525	                succ = dynamics.img_step(state, action, dt=prev_dt)
526	                succ_feat = dynamics.get_feat(succ)
527	                if gate_active:
528	                    _, next_dt, _ = gate(succ_feat.detach(), step, hard=True)
529	                else:
530	                    batch_size = succ_feat.shape[0]
531	                    next_dt = torch.ones(
532	                        batch_size, dtype=torch.long, device=succ_feat.device
533	                    )
534	                return succ, feat, action, next_dt
535	
536	            init_dt = torch.ones(
537	                start[list(start.keys())[0]].shape[0],
538	                dtype=torch.long, device=config.device,
539	            )
540	            succ, feats, actions, dts = tools.static_scan(
541	                step_fn, [torch.arange(horizon)],
542	                (start, None, None, init_dt),
543	            )
544	            states = {
545	                k: torch.cat([start[k][None], v[:-1]], 0)
546	                for k, v in succ.items()
547	            }
548	            return feats, states, actions, dts
549	        else:
550	            def step(prev, _):
551	                state, _, _ = prev
552	                feat = dynamics.get_feat(state)
553	                inp = feat.detach()
554	                action = policy(inp).sample()
555	                succ = dynamics.img_step(state, action)
556	                return succ, feat, action
557	
558	            succ, feats, actions = tools.static_scan(
559	                step, [torch.arange(horizon)], (start, None, None)
560	            )
561	            states = {
562	                k: torch.cat([start[k][None], v[:-1]], 0)
563	                for k, v in succ.items()
564	            }
565	            return feats, states, actions
566	
567	    def _compute_target(self, imag_feat, imag_state, reward, dts=None):
568	        if "cont" in self._world_model.heads:
569	            inp = self._world_model.dynamics.get_feat(imag_state)
570	            discount = self._config.discount * self._world_model.heads["cont"](inp).mean
571	        else:
572	            discount = self._config.discount * torch.ones_like(reward)
573	        value = self.value(imag_feat).mode()
574	
575	        if dts is not None and self._config.gate_enabled:
576	            target = tools.lambda_return_variable_dt(
577	                reward[1:],
578	                value[:-1],
579	                discount[1:],
580	                dts[1:],
581	                bootstrap=value[-1],
582	                lambda_=self._config.discount_lambda,
583	                axis=0,
584	            )
585	            pcont_adj = discount ** dts.unsqueeze(-1).float()
586	            weights = torch.cumprod(
587	                torch.cat([torch.ones_like(pcont_adj[:1]), pcont_adj[:-1]], 0), 0
588	            ).detach()
589	        else:
590	            target = tools.lambda_return(
591	                reward[1:],
592	                value[:-1],
593	                discount[1:],
594	                bootstrap=value[-1],
595	                lambda_=self._config.discount_lambda,
596	                axis=0,
597	            )
598	            weights = torch.cumprod(
599	                torch.cat([torch.ones_like(discount[:1]), discount[:-1]], 0), 0
600	            ).detach()
601	        return target, weights, value[:-1]
602	
603	    def _compute_actor_loss(
604	        self,
605	        imag_feat,
606	        imag_action,
607	        target,
608	        weights,
609	        base,
610	    ):
611	        metrics = {}
612	        inp = imag_feat.detach()
613	        policy = self.actor(inp)
614	        # Q-val for actor is not transformed using symlog
615	        target = torch.stack(target, dim=1)
616	        if self._config.reward_EMA:
617	            offset, scale = self.reward_ema(target, self.ema_vals)
618	            normed_target = (target - offset) / scale
619	            normed_base = (base - offset) / scale
620	            adv = normed_target - normed_base
621	            metrics.update(tools.tensorstats(normed_target, "normed_target"))
622	            metrics["EMA_005"] = to_np(self.ema_vals[0])
623	            metrics["EMA_095"] = to_np(self.ema_vals[1])
624	        else:
625	            adv = target - base
626	
627	        if self._config.imag_gradient == "dynamics":
628	            actor_target = adv
629	        elif self._config.imag_gradient == "reinforce":
630	            actor_target = (
631	                policy.log_prob(imag_action)[:-1][:, :, None]
632	                * (target - self.value(imag_feat[:-1]).mode()).detach()
633	            )
634	        elif self._config.imag_gradient == "both":
635	            actor_target = (
636	                policy.log_prob(imag_action)[:-1][:, :, None]
637	                * (target - self.value(imag_feat[:-1]).mode()).detach()
638	            )
639	            mix = self._config.imag_gradient_mix
640	            actor_target = mix * target + (1 - mix) * actor_target
641	            metrics["imag_gradient_mix"] = mix
642	        else:
643	            raise NotImplementedError(self._config.imag_gradient)
644	        actor_loss = -weights[:-1] * actor_target
645	        return actor_loss, metrics
646	
647	    def _update_slow_target(self):
648	        if self._config.critic["slow_target"]:
649	            if self._updates % self._config.critic["slow_target_update"] == 0:
650	                mix = self._config.critic["slow_target_fraction"]
651	                for s, d in zip(self.value.parameters(), self._slow_value.parameters()):
652	                    d.data = mix * s.data + (1 - mix) * d.data
653	            self._updates += 1
654	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4548d576-751a-4385-85b2-ea3732bcaf07",
  "uuid": "4c4d003b-1ad1-47e6-9b8c-8149e43b3cce",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/code/models.py",
      "content": "# Event-Gated Adaptive-Horizon DreamerV3 — World Model & Behavior\n# Modified from NM512/dreamerv3-torch.\n# Changes: WorldModel integrates EventGate + variable-dt sub-sampling;\n#          ImagBehavior uses gate-driven dt in imagination + adapted lambda-returns.\n\nimport copy\nimport math\n\nimport torch\nfrom torch import nn\nfrom torch.nn import functional as F\n\nimport networks\nimport tools\n\nto_np = lambda x: x.detach().cpu().numpy()\n\n\ndef compute_gate_targets(feats, max_dt):\n    \"\"\"Soft supervision target for the event gate derived from state deltas.\n\n    Large delta -> prefer small dt (index 0 = dt=1).\n    Small delta -> prefer large dt (index K-1 = dt=K).\n    \"\"\"\n    feats = feats.detach()\n    deltas = torch.norm(feats[1:] - feats[:-1], dim=-1)  # (time-1, batch)\n    delta_min = deltas.min(dim=0, keepdim=True).values\n    delta_max = deltas.max(dim=0, keepdim=True).values\n    delta_norm = (deltas - delta_min) / (delta_max - delta_min + 1e-8)\n    preferred_dt = 1.0 + (max_dt - 1.0) * (1.0 - delta_norm)\n    dt_indices = torch.arange(1, max_dt + 1, dtype=torch.float32, device=feats.device)\n    sigma = 1.0\n    log_probs = -0.5 * ((preferred_dt.unsqueeze(-1) - dt_indices) / sigma) ** 2\n    target_dist = F.softmax(log_probs, dim=-1)\n    return target_dist\n\n\ndef gate_loss_fn(gate_logits, target_dist):\n    \"\"\"Cross-entropy between gate predictions and supervision target.\"\"\"\n    log_probs = F.log_softmax(gate_logits, dim=-1)\n    return -(target_dist * log_probs).sum(dim=-1)\n\n\nclass RewardEMA:\n    \"\"\"running mean and std\"\"\"\n\n    def __init__(self, device, alpha=1e-2):\n        self.device = device\n        self.alpha = alpha\n        self.range = torch.tensor([0.05, 0.95], device=device)\n\n    def __call__(self, x, ema_vals):\n        flat_x = torch.flatten(x.detach())\n        x_quantile = torch.quantile(input=flat_x, q=self.range)\n        # this should be in-place operation\n        ema_vals[:] = self.alpha * x_quantile + (1 - self.alpha) * ema_vals\n        scale = torch.clip(ema_vals[1] - ema_vals[0], min=1.0)\n        offset = ema_vals[0]\n        return offset.detach(), scale.detach()\n\n\nclass WorldModel(nn.Module):\n    def __init__(self, obs_space, act_space, step, config):\n        super(WorldModel, self).__init__()\n        self._step = step\n        self._use_amp = True if config.precision == 16 else False\n        self._config = config\n        shapes = {k: tuple(v.shape) for k, v in obs_space.spaces.items()}\n        self.encoder = networks.MultiEncoder(shapes, **config.encoder)\n        self.embed_size = self.encoder.outdim\n        self.dynamics = networks.RSSM(\n            config.dyn_stoch,\n            config.dyn_deter,\n            config.dyn_hidden,\n            config.dyn_rec_depth,\n            config.dyn_discrete,\n            config.act,\n            config.norm,\n            config.dyn_mean_act,\n            config.dyn_std_act,\n            config.dyn_min_std,\n            config.unimix_ratio,\n            config.initial,\n            config.num_actions,\n            self.embed_size,\n            config.device,\n            max_dt=config.gate_max_dt if config.gate_enabled else 1,\n            dt_embed_dim=config.gate_dt_embed_dim,\n        )\n        self.heads = nn.ModuleDict()\n        if config.dyn_discrete:\n            feat_size = config.dyn_stoch * config.dyn_discrete + config.dyn_deter\n        else:\n            feat_size = config.dyn_stoch + config.dyn_deter\n        self.heads[\"decoder\"] = networks.MultiDecoder(\n            feat_size, shapes, **config.decoder\n        )\n        self.heads[\"reward\"] = networks.MLP(\n            feat_size,\n            (255,) if config.reward_head[\"dist\"] == \"symlog_disc\" else (),\n            config.reward_head[\"layers\"],\n            config.units,\n            config.act,\n            config.norm,\n            dist=config.reward_head[\"dist\"],\n            outscale=config.reward_head[\"outscale\"],\n            device=config.device,\n            name=\"Reward\",\n        )\n        self.heads[\"cont\"] = networks.MLP(\n            feat_size,\n            (),\n            config.cont_head[\"layers\"],\n            config.units,\n            config.act,\n            config.norm,\n            dist=\"binary\",\n            outscale=config.cont_head[\"outscale\"],\n            device=config.device,\n            name=\"Cont\",\n        )\n\n        if config.gate_enabled:\n            self.event_gate = networks.EventGate(\n                feat_size=feat_size,\n                max_dt=config.gate_max_dt,\n                hidden_units=config.gate_hidden_units,\n                hidden_layers=config.gate_hidden_layers,\n                act=config.act,\n                norm=config.norm,\n                tau_init=config.gate_tau_init,\n                tau_final=config.gate_tau_final,\n                tau_anneal_steps=config.gate_tau_anneal_steps,\n            )\n            self.register_buffer(\n                \"gate_step\", torch.tensor(0, dtype=torch.long)\n            )\n        else:\n            self.event_gate = None\n\n        for name in config.grad_heads:\n            assert name in self.heads, name\n        self._model_opt = tools.Optimizer(\n            \"model\",\n            self.parameters(),\n            config.model_lr,\n            config.opt_eps,\n            config.grad_clip,\n            config.weight_decay,\n            opt=config.opt,\n            use_amp=self._use_amp,\n        )\n        print(\n            f\"Optimizer model_opt has {sum(param.numel() for param in self.parameters())} variables.\"\n        )\n        # other losses are scaled by 1.0.\n        self._scales = dict(\n            reward=config.reward_head[\"loss_scale\"],\n            cont=config.cont_head[\"loss_scale\"],\n        )\n\n    def _train(self, data):\n        # action (batch_size, batch_length, act_dim)\n        # image (batch_size, batch_length, h, w, ch)\n        # reward (batch_size, batch_length)\n        # discount (batch_size, batch_length)\n        data = self.preprocess(data)\n\n        if self._config.gate_enabled:\n            self.gate_step += 1\n            data, dt_labels = tools.subsample_variable_dt(\n                data, self._config.gate_max_dt, self._config.discount,\n            )\n        else:\n            dt_labels = None\n\n        with tools.RequiresGrad(self):\n            with torch.cuda.amp.autocast(self._use_amp):\n                embed = self.encoder(data)\n                if dt_labels is not None:\n                    post, prior = self.dynamics.observe(\n                        embed, data[\"action\"], data[\"is_first\"],\n                        dt_labels=dt_labels,\n                    )\n                else:\n                    post, prior = self.dynamics.observe(\n                        embed, data[\"action\"], data[\"is_first\"]\n                    )\n                kl_free = self._config.kl_free\n                dyn_scale = self._config.dyn_scale\n                rep_scale = self._config.rep_scale\n                kl_loss, kl_value, dyn_loss, rep_loss = self.dynamics.kl_loss(\n                    post, prior, kl_free, dyn_scale, rep_scale\n                )\n                assert kl_loss.shape == embed.shape[:2], kl_loss.shape\n                preds = {}\n                for name, head in self.heads.items():\n                    grad_head = name in self._config.grad_heads\n                    feat = self.dynamics.get_feat(post)\n                    feat = feat if grad_head else feat.detach()\n                    pred = head(feat)\n                    if type(pred) is dict:\n                        preds.update(pred)\n                    else:\n                        preds[name] = pred\n                losses = {}\n                for name, pred in preds.items():\n                    loss = -pred.log_prob(data[name])\n                    assert loss.shape == embed.shape[:2], (name, loss.shape)\n                    losses[name] = loss\n                scaled = {\n                    key: value * self._scales.get(key, 1.0)\n                    for key, value in losses.items()\n                }\n                model_loss = sum(scaled.values()) + kl_loss\n                mean_model_loss = torch.mean(model_loss)\n\n                if self._config.gate_enabled and self.event_gate is not None:\n                    gate_feat = self.dynamics.get_feat(post).detach()\n                    B_g, T_g, D_g = gate_feat.shape\n                    gate_feat_flat = gate_feat.reshape(B_g * T_g, D_g)\n                    step = self.gate_step.item()\n                    _, _, gate_logits_flat = self.event_gate(\n                        gate_feat_flat, step, hard=False\n                    )\n                    gate_logits = gate_logits_flat.reshape(\n                        B_g, T_g, self._config.gate_max_dt\n                    )\n\n                    feat_time = gate_feat.permute(1, 0, 2)\n                    target_dist = compute_gate_targets(\n                        feat_time, self._config.gate_max_dt\n                    )\n\n                    g_logits = gate_logits[:, 1:, :].permute(1, 0, 2)\n                    g_loss = gate_loss_fn(g_logits, target_dist)\n\n                    g_entropy = self.event_gate.entropy(\n                        g_logits.reshape(-1, self._config.gate_max_dt)\n                    ).reshape(g_loss.shape)\n\n                    if step < self._config.gate_curriculum_phase1:\n                        gate_scale = 0.0\n                    elif step < self._config.gate_curriculum_phase2:\n                        progress = (step - self._config.gate_curriculum_phase1) / (\n                            self._config.gate_curriculum_phase2\n                            - self._config.gate_curriculum_phase1\n                        )\n                        gate_scale = progress\n                    else:\n                        gate_scale = 1.0\n\n                    entropy_frac = min(\n                        step / max(self._config.gate_tau_anneal_steps, 1), 1.0\n                    )\n                    effective_entropy_bonus = (\n                        self._config.gate_entropy_bonus_init\n                        + entropy_frac\n                        * (\n                            self._config.gate_entropy_bonus_final\n                            - self._config.gate_entropy_bonus_init\n                        )\n                    )\n\n                    total_gate_loss = gate_scale * (\n                        self._config.gate_loss_weight * g_loss.mean()\n                        - effective_entropy_bonus * g_entropy.mean()\n                    )\n                    mean_model_loss = mean_model_loss + total_gate_loss\n\n            metrics = self._model_opt(mean_model_loss, self.parameters())\n\n        # Store scalar metrics to avoid keeping (batch,time) arrays until the next log step.\n        metrics.update(\n            {f\"{name}_loss\": to_np(torch.mean(loss)) for name, loss in losses.items()}\n        )\n        metrics[\"kl_free\"] = kl_free\n        metrics[\"dyn_scale\"] = dyn_scale\n        metrics[\"rep_scale\"] = rep_scale\n        metrics[\"dyn_loss\"] = to_np(torch.mean(dyn_loss))\n        metrics[\"rep_loss\"] = to_np(torch.mean(rep_loss))\n        metrics[\"kl\"] = to_np(torch.mean(kl_value))\n        with torch.cuda.amp.autocast(self._use_amp):\n            metrics[\"prior_ent\"] = to_np(\n                torch.mean(self.dynamics.get_dist(prior).entropy())\n            )\n            metrics[\"post_ent\"] = to_np(\n                torch.mean(self.dynamics.get_dist(post).entropy())\n            )\n            context = dict(\n                embed=embed,\n                feat=self.dynamics.get_feat(post),\n                kl=kl_value,\n                postent=self.dynamics.get_dist(post).entropy(),\n            )\n\n        if self._config.gate_enabled and self.event_gate is not None:\n            metrics[\"gate_loss\"] = to_np(total_gate_loss)\n            metrics[\"gate_scale\"] = gate_scale\n            metrics[\"gate_entropy_bonus\"] = effective_entropy_bonus\n\n        post = {k: v.detach() for k, v in post.items()}\n        return post, context, metrics\n\n    # this function is called during both rollout and training\n    def preprocess(self, obs):\n        obs = {\n            k: torch.tensor(v, device=self._config.device, dtype=torch.float32)\n            for k, v in obs.items()\n        }\n        obs[\"image\"] = obs[\"image\"] / 255.0\n        if \"discount\" in obs:\n            obs[\"discount\"] *= self._config.discount\n            # (batch_size, batch_length) -> (batch_size, batch_length, 1)\n            obs[\"discount\"] = obs[\"discount\"].unsqueeze(-1)\n        # 'is_first' is necesarry to initialize hidden state at training\n        assert \"is_first\" in obs\n        # 'is_terminal' is necesarry to train cont_head\n        assert \"is_terminal\" in obs\n        obs[\"cont\"] = (1.0 - obs[\"is_terminal\"]).unsqueeze(-1)\n        return obs\n\n    def video_pred(self, data):\n        data = self.preprocess(data)\n        embed = self.encoder(data)\n\n        states, _ = self.dynamics.observe(\n            embed[:6, :5], data[\"action\"][:6, :5], data[\"is_first\"][:6, :5]\n        )\n        recon = self.heads[\"decoder\"](self.dynamics.get_feat(states))[\"image\"].mode()[\n            :6\n        ]\n        reward_post = self.heads[\"reward\"](self.dynamics.get_feat(states)).mode()[:6]\n        init = {k: v[:, -1] for k, v in states.items()}\n        prior = self.dynamics.imagine_with_action(data[\"action\"][:6, 5:], init)\n        openl = self.heads[\"decoder\"](self.dynamics.get_feat(prior))[\"image\"].mode()\n        reward_prior = self.heads[\"reward\"](self.dynamics.get_feat(prior)).mode()\n        # observed image is given until 5 steps\n        model = torch.cat([recon[:, :5], openl], 1)\n        truth = data[\"image\"][:6]\n        model = model\n        error = (model - truth + 1.0) / 2.0\n\n        return torch.cat([truth, model, error], 2)\n\n\nclass ImagBehavior(nn.Module):\n    def __init__(self, config, world_model):\n        super(ImagBehavior, self).__init__()\n        self._use_amp = True if config.precision == 16 else False\n        self._config = config\n        self._world_model = world_model\n        if config.dyn_discrete:\n            feat_size = config.dyn_stoch * config.dyn_discrete + config.dyn_deter\n        else:\n            feat_size = config.dyn_stoch + config.dyn_deter\n        self.actor = networks.MLP(\n            feat_size,\n            (config.num_actions,),\n            config.actor[\"layers\"],\n            config.units,\n            config.act,\n            config.norm,\n            config.actor[\"dist\"],\n            config.actor[\"std\"],\n            config.actor[\"min_std\"],\n            config.actor[\"max_std\"],\n            absmax=1.0,\n            temp=config.actor[\"temp\"],\n            unimix_ratio=config.actor[\"unimix_ratio\"],\n            outscale=config.actor[\"outscale\"],\n            name=\"Actor\",\n        )\n        self.value = networks.MLP(\n            feat_size,\n            (255,) if config.critic[\"dist\"] == \"symlog_disc\" else (),\n            config.critic[\"layers\"],\n            config.units,\n            config.act,\n            config.norm,\n            config.critic[\"dist\"],\n            outscale=config.critic[\"outscale\"],\n            device=config.device,\n            name=\"Value\",\n        )\n        if config.critic[\"slow_target\"]:\n            self._slow_value = copy.deepcopy(self.value)\n            self._updates = 0\n        kw = dict(wd=config.weight_decay, opt=config.opt, use_amp=self._use_amp)\n        self._actor_opt = tools.Optimizer(\n            \"actor\",\n            self.actor.parameters(),\n            config.actor[\"lr\"],\n            config.actor[\"eps\"],\n            config.actor[\"grad_clip\"],\n            **kw,\n        )\n        print(\n            f\"Optimizer actor_opt has {sum(param.numel() for param in self.actor.parameters())} variables.\"\n        )\n        self._value_opt = tools.Optimizer(\n            \"value\",\n            self.value.parameters(),\n            config.critic[\"lr\"],\n            config.critic[\"eps\"],\n            config.critic[\"grad_clip\"],\n            **kw,\n        )\n        print(\n            f\"Optimizer value_opt has {sum(param.numel() for param in self.value.parameters())} variables.\"\n        )\n        if self._config.reward_EMA:\n            # register ema_vals to nn.Module for enabling torch.save and torch.load\n            self.register_buffer(\n                \"ema_vals\", torch.zeros((2,), device=self._config.device)\n            )\n            self.reward_ema = RewardEMA(device=self._config.device)\n\n    def _train(\n        self,\n        start,\n        objective,\n    ):\n        self._update_slow_target()\n        metrics = {}\n\n        with tools.RequiresGrad(self.actor):\n            with torch.cuda.amp.autocast(self._use_amp):\n                if self._config.gate_enabled:\n                    imag_feat, imag_state, imag_action, dts = self._imagine(\n                        start, self.actor, self._config.imag_horizon\n                    )\n                else:\n                    imag_feat, imag_state, imag_action = self._imagine(\n                        start, self.actor, self._config.imag_horizon\n                    )\n                    dts = None\n                reward = objective(imag_feat, imag_state, imag_action)\n                actor_ent = self.actor(imag_feat).entropy()\n                state_ent = self._world_model.dynamics.get_dist(imag_state).entropy()\n                # this target is not scaled by ema or sym_log.\n                target, weights, base = self._compute_target(\n                    imag_feat, imag_state, reward, dts=dts\n                )\n                actor_loss, mets = self._compute_actor_loss(\n                    imag_feat,\n                    imag_action,\n                    target,\n                    weights,\n                    base,\n                )\n                actor_loss -= self._config.actor[\"entropy\"] * actor_ent[:-1, ..., None]\n                actor_loss = torch.mean(actor_loss)\n                metrics.update(mets)\n                value_input = imag_feat\n\n        with tools.RequiresGrad(self.value):\n            with torch.cuda.amp.autocast(self._use_amp):\n                value = self.value(value_input[:-1].detach())\n                target = torch.stack(target, dim=1)\n                # (time, batch, 1), (time, batch, 1) -> (time, batch)\n                value_loss = -value.log_prob(target.detach())\n                slow_target = self._slow_value(value_input[:-1].detach())\n                if self._config.critic[\"slow_target\"]:\n                    value_loss -= value.log_prob(slow_target.mode().detach())\n                # (time, batch, 1), (time, batch, 1) -> (1,)\n                value_loss = torch.mean(weights[:-1] * value_loss[:, :, None])\n\n        metrics.update(tools.tensorstats(value.mode(), \"value\"))\n        metrics.update(tools.tensorstats(target, \"target\"))\n        metrics.update(tools.tensorstats(reward, \"imag_reward\"))\n        if self._config.actor[\"dist\"] in [\"onehot\"]:\n            metrics.update(\n                tools.tensorstats(\n                    torch.argmax(imag_action, dim=-1).float(), \"imag_action\"\n                )\n            )\n        else:\n            metrics.update(tools.tensorstats(imag_action, \"imag_action\"))\n        metrics[\"actor_entropy\"] = to_np(torch.mean(actor_ent))\n\n        if self._config.gate_enabled and dts is not None:\n            dts_float = dts.float()\n            metrics[\"gate_dt_mean\"] = to_np(torch.mean(dts_float))\n            metrics[\"gate_dt_std\"] = to_np(torch.std(dts_float))\n            metrics[\"gate_dt_min\"] = to_np(torch.min(dts_float))\n            metrics[\"gate_dt_max\"] = to_np(torch.max(dts_float))\n            dt_counts = torch.bincount(\n                dts.reshape(-1).long(),\n                minlength=self._config.gate_max_dt + 1,\n            )[1:]\n            dt_dist = dt_counts.float() / dt_counts.sum()\n            for k in range(self._config.gate_max_dt):\n                metrics[f\"gate_dt_{k+1}_frac\"] = to_np(dt_dist[k])\n            emp_entropy = -(dt_dist * torch.log(dt_dist + 1e-8)).sum()\n            metrics[\"gate_empirical_entropy\"] = to_np(emp_entropy)\n            max_entropy = math.log(self._config.gate_max_dt)\n            metrics[\"gate_entropy_ratio\"] = to_np(emp_entropy) / max_entropy\n\n        with tools.RequiresGrad(self):\n            metrics.update(self._actor_opt(actor_loss, self.actor.parameters()))\n            metrics.update(self._value_opt(value_loss, self.value.parameters()))\n        return imag_feat, imag_state, imag_action, weights, metrics\n\n    def _imagine(self, start, policy, horizon):\n        dynamics = self._world_model.dynamics\n        flatten = lambda x: x.reshape([-1] + list(x.shape[2:]))\n        start = {k: flatten(v) for k, v in start.items()}\n\n        if self._config.gate_enabled:\n            gate = self._world_model.event_gate\n            config = self._config\n            step = self._world_model.gate_step.item() if hasattr(\n                self._world_model, \"gate_step\"\n            ) else 0\n            gate_active = (\n                gate is not None and step > config.gate_curriculum_phase1\n            )\n\n            def step_fn(prev, _):\n                state, _, _, prev_dt = prev\n                feat = dynamics.get_feat(state)\n                inp = feat.detach()\n                action = policy(inp).sample()\n                succ = dynamics.img_step(state, action, dt=prev_dt)\n                succ_feat = dynamics.get_feat(succ)\n                if gate_active:\n                    _, next_dt, _ = gate(succ_feat.detach(), step, hard=True)\n                else:\n                    batch_size = succ_feat.shape[0]\n                    next_dt = torch.ones(\n                        batch_size, dtype=torch.long, device=succ_feat.device\n                    )\n                return succ, feat, action, next_dt\n\n            init_dt = torch.ones(\n                start[list(start.keys())[0]].shape[0],\n                dtype=torch.long, device=config.device,\n            )\n            succ, feats, actions, dts = tools.static_scan(\n                step_fn, [torch.arange(horizon)],\n                (start, None, None, init_dt),\n            )\n            states = {\n                k: torch.cat([start[k][None], v[:-1]], 0)\n                for k, v in succ.items()\n            }\n            return feats, states, actions, dts\n        else:\n            def step(prev, _):\n                state, _, _ = prev\n                feat = dynamics.get_feat(state)\n                inp = feat.detach()\n                action = policy(inp).sample()\n                succ = dynamics.img_step(state, action)\n                return succ, feat, action\n\n            succ, feats, actions = tools.static_scan(\n                step, [torch.arange(horizon)], (start, None, None)\n            )\n            states = {\n                k: torch.cat([start[k][None], v[:-1]], 0)\n                for k, v in succ.items()\n            }\n            return feats, states, actions\n\n    def _compute_target(self, imag_feat, imag_state, reward, dts=None):\n        if \"cont\" in self._world_model.heads:\n            inp = self._world_model.dynamics.get_feat(imag_state)\n            discount = self._config.discount * self._world_model.heads[\"cont\"](inp).mean\n        else:\n            discount = self._config.discount * torch.ones_like(reward)\n        value = self.value(imag_feat).mode()\n\n        if dts is not None and self._config.gate_enabled:\n            target = tools.lambda_return_variable_dt(\n                reward[1:],\n                value[:-1],\n                discount[1:],\n                dts[1:],\n                bootstrap=value[-1],\n                lambda_=self._config.discount_lambda,\n                axis=0,\n            )\n            pcont_adj = discount ** dts.unsqueeze(-1).float()\n            weights = torch.cumprod(\n                torch.cat([torch.ones_like(pcont_adj[:1]), pcont_adj[:-1]], 0), 0\n            ).detach()\n        else:\n            target = tools.lambda_return(\n                reward[1:],\n                value[:-1],\n                discount[1:],\n                bootstrap=value[-1],\n                lambda_=self._config.discount_lambda,\n                axis=0,\n            )\n            weights = torch.cumprod(\n                torch.cat([torch.ones_like(discount[:1]), discount[:-1]], 0), 0\n            ).detach()\n        return target, weights, value[:-1]\n\n    def _compute_actor_loss(\n        self,\n        imag_feat,\n        imag_action,\n        target,\n        weights,\n        base,\n    ):\n        metrics = {}\n        inp = imag_feat.detach()\n        policy = self.actor(inp)\n        # Q-val for actor is not transformed using symlog\n        target = torch.stack(target, dim=1)\n        if self._config.reward_EMA:\n            offset, scale = self.reward_ema(target, self.ema_vals)\n            normed_target = (target - offset) / scale\n            normed_base = (base - offset) / scale\n            adv = normed_target - normed_base\n            metrics.update(tools.tensorstats(normed_target, \"normed_target\"))\n            metrics[\"EMA_005\"] = to_np(self.ema_vals[0])\n            metrics[\"EMA_095\"] = to_np(self.ema_vals[1])\n        else:\n            adv = target - base\n\n        if self._config.imag_gradient == \"dynamics\":\n            actor_target = adv\n        elif self._config.imag_gradient == \"reinforce\":\n            actor_target = (\n                policy.log_prob(imag_action)[:-1][:, :, None]\n                * (target - self.value(imag_feat[:-1]).mode()).detach()\n            )\n        elif self._config.imag_gradient == \"both\":\n            actor_target = (\n                policy.log_prob(imag_action)[:-1][:, :, None]\n                * (target - self.value(imag_feat[:-1]).mode()).detach()\n            )\n            mix = self._config.imag_gradient_mix\n            actor_target = mix * target + (1 - mix) * actor_target\n            metrics[\"imag_gradient_mix\"] = mix\n        else:\n            raise NotImplementedError(self._config.imag_gradient)\n        actor_loss = -weights[:-1] * actor_target\n        return actor_loss, metrics\n\n    def _update_slow_target(self):\n        if self._config.critic[\"slow_target\"]:\n            if self._updates % self._config.critic[\"slow_target_update\"] == 0:\n                mix = self._config.critic[\"slow_target_fraction\"]\n                for s, d in zip(self.value.parameters(), self._slow_value.parameters()):\n                    d.data = mix * s.data + (1 - mix) * d.data\n            self._updates += 1\n",
      "numLines": 654,
      "startLine": 1,
      "totalLines": 654
    }
  }
}
```

</details>

---

### Assistant

_source line 14_

<details><summary>Logged reasoning block</summary>

```text
Now I have a clear understanding of the existing code. Let me write the patch file.

Key observations from the existing code:

1. `subsample_variable_dt` in tools.py (line 763-810): Takes `data`, `max_dt`, `discount`. Samples dt from log-uniform over [1, max_dt], does subsampling.

2. `WorldModel._train` in models.py (line 162-303): 
   - Line 169-173: When gate_enabled, calls `tools.subsample_variable_dt(data, self._config.gate_max_dt, self._config.discount)`
   - Line 242-251: Already has the gate_scale curriculum logic (phase1, phase2, etc.)

The patch needs to add an `effective_max_dt` parameter to `subsample_variable_dt` that skips subsampling when it's ≤ 1, otherwise uses it instead of `max_dt` for the log-uniform sampling range. Then in `WorldModel._train`, I'll compute `effective_max_dt` from `gate_scale` and pass it through.

The critical fix is reordering the code so gate_scale gets computed before the subsampling call happens, since right now it's backwards.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4548d576-751a-4385-85b2-ea3732bcaf07",
  "uuid": "e5ede874-35e7-4210-84e0-eeb6acd80dcd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N2Ehm5hQzCVgCeAJNJfNc5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23483,
      "cache_read_input_tokens": 24468,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 23483
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

现在编写补丁文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4548d576-751a-4385-85b2-ea3732bcaf07",
  "uuid": "855df943-62ca-4e7a-8a5d-650d6465633d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N2Ehm5hQzCVgCeAJNJfNc5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23483,
      "cache_read_input_tokens": 24468,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 23483
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

<details open><summary>🔧 Tool call — Write · `toolu_01JUYG1Sj9RTVUZUAaitJV5D`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/code/subsample_curriculum_patch.py",
  "content": "# Subsample Curriculum Patch\n# -------------------------\n# Problem: subsample_variable_dt applies variable-dt subsampling in Phase 1\n# (gate frozen, 0-50K steps), forcing RSSM to train on variable-dt data while\n# imagination only uses dt=1. This train/imagine mismatch hurts return (~40% of baseline).\n#\n# Fix: tie subsampling range to gate_scale curriculum.\n#   Phase 1 (gate_scale=0):    effective_max_dt=1 -> no subsampling (vanilla DreamerV3)\n#   Phase 2 (0&lt;gate_scale<1):  effective_max_dt linearly ramps from 1 to K\n#   Phase 3 (gate_scale=1):    effective_max_dt=K -> full log-uniform subsampling\n#\n# Deployment:\n#   1. Replace subsample_variable_dt in tools.py (around line 763)\n#   2. Replace the subsample call block in WorldModel._train in models.py (around line 169)\n\nimport math\nimport torch\n\n\n# =============================================================================\n# Part 1: Replace tools.subsample_variable_dt (tools.py ~line 763-810)\n# =============================================================================\n\ndef subsample_variable_dt(data, max_dt, discount, effective_max_dt=None):\n    \"\"\"Variable-dt sub-sampling of replay trajectories.\n\n    Samples per-element dt from log-uniform over [1, effective_max_dt].\n    Computes cumulative discounted reward and minimum continuation for each gap.\n\n    Args:\n        data: dict of tensors, each (B, T, ...).\n        max_dt: config maximum dt (used as upper bound clamp).\n        discount: scalar discount factor for cumulative reward.\n        effective_max_dt: curriculum-controlled max dt.\n            None or <=1 means no subsampling (pure dt=1, vanilla DreamerV3).\n    \"\"\"\n    B, T = data[\"action\"].shape[:2]\n    device = data[\"action\"].device\n\n    if effective_max_dt is None:\n        effective_max_dt = max_dt\n\n    effective_max_dt = max(1, min(int(round(effective_max_dt)), max_dt))\n\n    if effective_max_dt <= 1:\n        dt_labels = torch.ones(B, T, dtype=torch.long, device=device)\n        return data, dt_labels\n\n    log_dt = torch.zeros(B, device=device).uniform_(0, math.log(effective_max_dt))\n    dt_per_elem = torch.clamp(torch.round(torch.exp(log_dt)).long(), 1, effective_max_dt)\n\n    sub_len = torch.ceil(torch.tensor(T, dtype=torch.float) / dt_per_elem.float()).long()\n    T_sub = sub_len.max().item()\n\n    data_sub = {}\n    dt_labels = torch.ones(B, T_sub, dtype=torch.long, device=device)\n    reward_cum = torch.zeros(B, T_sub, *data[\"reward\"].shape[2:], device=device)\n    cont_min = torch.ones(B, T_sub, *data[\"cont\"].shape[2:], device=device)\n\n    for b in range(B):\n        dt_b = dt_per_elem[b].item()\n        indices = list(range(0, T, dt_b))\n        L = len(indices)\n\n        for key in data:\n            if key not in data_sub:\n                data_sub[key] = torch.zeros(\n                    B, T_sub, *data[key].shape[2:],\n                    dtype=data[key].dtype, device=device,\n                )\n            data_sub[key][b, :L] = data[key][b, indices]\n\n        for i, t_start in enumerate(indices[:-1]):\n            t_end = min(t_start + dt_b, T)\n            span = t_end - t_start\n            gamma_powers = discount ** torch.arange(\n                span, dtype=torch.float, device=device\n            )\n            r_slice = data[\"reward\"][b, t_start:t_end]\n            reward_cum[b, i] = (gamma_powers * r_slice).sum(dim=0)\n            cont_min[b, i] = data[\"cont\"][b, t_start:t_end].min(dim=0).values\n\n        dt_labels[b, :L] = dt_b\n\n    data_sub[\"reward\"] = reward_cum\n    data_sub[\"cont\"] = cont_min\n    return data_sub, dt_labels\n\n\n# =============================================================================\n# Part 2: Replace subsample call in WorldModel._train (models.py ~line 169-173)\n# =============================================================================\n# Original code:\n#\n#     if self._config.gate_enabled:\n#         self.gate_step += 1\n#         data, dt_labels = tools.subsample_variable_dt(\n#             data, self._config.gate_max_dt, self._config.discount,\n#         )\n#     else:\n#         dt_labels = None\n#\n# Replace with:\n#\n#     if self._config.gate_enabled:\n#         self.gate_step += 1\n#         step = self.gate_step.item()\n#         if step < self._config.gate_curriculum_phase1:\n#             gate_scale = 0.0\n#         elif step < self._config.gate_curriculum_phase2:\n#             progress = (step - self._config.gate_curriculum_phase1) / (\n#                 self._config.gate_curriculum_phase2\n#                 - self._config.gate_curriculum_phase1\n#             )\n#             gate_scale = progress\n#         else:\n#             gate_scale = 1.0\n#\n#         effective_max_dt = 1 + gate_scale * (self._config.gate_max_dt - 1)\n#         data, dt_labels = tools.subsample_variable_dt(\n#             data, self._config.gate_max_dt, self._config.discount,\n#             effective_max_dt=effective_max_dt,\n#         )\n#     else:\n#         dt_labels = None\n#\n# NOTE: The gate_scale computation later in _train (around line 242) already\n# duplicates the same curriculum logic for scaling the gate loss. After this\n# patch, both blocks use the same gate_scale value. You can optionally refactor\n# to compute gate_scale once and reuse it, but it is not required — the\n# duplicated computation is trivially cheap and keeps the patch minimal.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4548d576-751a-4385-85b2-ea3732bcaf07",
  "uuid": "68c2d2fa-6671-48cc-898a-ba7f3ab0fe18",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N2Ehm5hQzCVgCeAJNJfNc5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23483,
      "cache_read_input_tokens": 24468,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 23483
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

_source line 17 · 2026-05-13T04:08:02.628Z_

<details><summary>↩ Tool result · `toolu_01JUYG1Sj9RTVUZUAaitJV5D`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/code/subsample_curriculum_patch.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4548d576-751a-4385-85b2-ea3732bcaf07",
  "uuid": "4286145b-9764-4c0c-adf6-d6a4a87857dd",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/code/subsample_curriculum_patch.py",
    "content": "# Subsample Curriculum Patch\n# -------------------------\n# Problem: subsample_variable_dt applies variable-dt subsampling in Phase 1\n# (gate frozen, 0-50K steps), forcing RSSM to train on variable-dt data while\n# imagination only uses dt=1. This train/imagine mismatch hurts return (~40% of baseline).\n#\n# Fix: tie subsampling range to gate_scale curriculum.\n#   Phase 1 (gate_scale=0):    effective_max_dt=1 -> no subsampling (vanilla DreamerV3)\n#   Phase 2 (0&lt;gate_scale<1):  effective_max_dt linearly ramps from 1 to K\n#   Phase 3 (gate_scale=1):    effective_max_dt=K -> full log-uniform subsampling\n#\n# Deployment:\n#   1. Replace subsample_variable_dt in tools.py (around line 763)\n#   2. Replace the subsample call block in WorldModel._train in models.py (around line 169)\n\nimport math\nimport torch\n\n\n# =============================================================================\n# Part 1: Replace tools.subsample_variable_dt (tools.py ~line 763-810)\n# =============================================================================\n\ndef subsample_variable_dt(data, max_dt, discount, effective_max_dt=None):\n    \"\"\"Variable-dt sub-sampling of replay trajectories.\n\n    Samples per-element dt from log-uniform over [1, effective_max_dt].\n    Computes cumulative discounted reward and minimum continuation for each gap.\n\n    Args:\n        data: dict of tensors, each (B, T, ...).\n        max_dt: config maximum dt (used as upper bound clamp).\n        discount: scalar discount factor for cumulative reward.\n        effective_max_dt: curriculum-controlled max dt.\n            None or <=1 means no subsampling (pure dt=1, vanilla DreamerV3).\n    \"\"\"\n    B, T = data[\"action\"].shape[:2]\n    device = data[\"action\"].device\n\n    if effective_max_dt is None:\n        effective_max_dt = max_dt\n\n    effective_max_dt = max(1, min(int(round(effective_max_dt)), max_dt))\n\n    if effective_max_dt <= 1:\n        dt_labels = torch.ones(B, T, dtype=torch.long, device=device)\n        return data, dt_labels\n\n    log_dt = torch.zeros(B, device=device).uniform_(0, math.log(effective_max_dt))\n    dt_per_elem = torch.clamp(torch.round(torch.exp(log_dt)).long(), 1, effective_max_dt)\n\n    sub_len = torch.ceil(torch.tensor(T, dtype=torch.float) / dt_per_elem.float()).long()\n    T_sub = sub_len.max().item()\n\n    data_sub = {}\n    dt_labels = torch.ones(B, T_sub, dtype=torch.long, device=device)\n    reward_cum = torch.zeros(B, T_sub, *data[\"reward\"].shape[2:], device=device)\n    cont_min = torch.ones(B, T_sub, *data[\"cont\"].shape[2:], device=device)\n\n    for b in range(B):\n        dt_b = dt_per_elem[b].item()\n        indices = list(range(0, T, dt_b))\n        L = len(indices)\n\n        for key in data:\n            if key not in data_sub:\n                data_sub[key] = torch.zeros(\n                    B, T_sub, *data[key].shape[2:],\n                    dtype=data[key].dtype, device=device,\n                )\n            data_sub[key][b, :L] = data[key][b, indices]\n\n        for i, t_start in enumerate(indices[:-1]):\n            t_end = min(t_start + dt_b, T)\n            span = t_end - t_start\n            gamma_powers = discount ** torch.arange(\n                span, dtype=torch.float, device=device\n            )\n            r_slice = data[\"reward\"][b, t_start:t_end]\n            reward_cum[b, i] = (gamma_powers * r_slice).sum(dim=0)\n            cont_min[b, i] = data[\"cont\"][b, t_start:t_end].min(dim=0).values\n\n        dt_labels[b, :L] = dt_b\n\n    data_sub[\"reward\"] = reward_cum\n    data_sub[\"cont\"] = cont_min\n    return data_sub, dt_labels\n\n\n# =============================================================================\n# Part 2: Replace subsample call in WorldModel._train (models.py ~line 169-173)\n# =============================================================================\n# Original code:\n#\n#     if self._config.gate_enabled:\n#         self.gate_step += 1\n#         data, dt_labels = tools.subsample_variable_dt(\n#             data, self._config.gate_max_dt, self._config.discount,\n#         )\n#     else:\n#         dt_labels = None\n#\n# Replace with:\n#\n#     if self._config.gate_enabled:\n#         self.gate_step += 1\n#         step = self.gate_step.item()\n#         if step < self._config.gate_curriculum_phase1:\n#             gate_scale = 0.0\n#         elif step < self._config.gate_curriculum_phase2:\n#             progress = (step - self._config.gate_curriculum_phase1) / (\n#                 self._config.gate_curriculum_phase2\n#                 - self._config.gate_curriculum_phase1\n#             )\n#             gate_scale = progress\n#         else:\n#             gate_scale = 1.0\n#\n#         effective_max_dt = 1 + gate_scale * (self._config.gate_max_dt - 1)\n#         data, dt_labels = tools.subsample_variable_dt(\n#             data, self._config.gate_max_dt, self._config.discount,\n#             effective_max_dt=effective_max_dt,\n#         )\n#     else:\n#         dt_labels = None\n#\n# NOTE: The gate_scale computation later in _train (around line 242) already\n# duplicates the same curriculum logic for scaling the gate loss. After this\n# patch, both blocks use the same gate_scale value. You can optionally refactor\n# to compute gate_scale once and reuse it, but it is not required — the\n# duplicated computation is trivially cheap and keeps the patch minimal.\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 18_

补丁已写入 `artifacts/code/subsample_curriculum_patch.py`。

核心变更：

1. **`subsample_variable_dt`** — 新增 `effective_max_dt` 参数（默认 `None`，向后兼容）。当 `effective_max_dt <= 1` 时直接返回原始数据 + 全 1 的 `dt_labels`，等价于不子采样；否则用 `effective_max_dt` 替代 `max_dt` 作为 log-uniform 采样上界。

2. **`WorldModel._train`** — 在调用 `subsample_variable_dt` 前先计算 `gate_scale`（复用已有的 phase1/phase2 curriculum 逻辑），然后传入 `effective_max_dt = 1 + gate_scale * (K - 1)`。Phase 1 时 `effective_max_dt=1`，RSSM 训练数据与 imagination 的 dt=1 完全一致。

部署位置：
- `tools.py` 第 763 行起，整个 `subsample_variable_dt` 函数替换
- `models.py` 第 169-173 行，子采样调用块替换

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4548d576-751a-4385-85b2-ea3732bcaf07",
  "uuid": "297530aa-f982-4250-be22-08ea7acf2cda",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EwkomebeyUFn1BGqzktjU2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2154,
      "cache_read_input_tokens": 47951,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2154
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

_source line 19_

补丁已写入 `artifacts/code/subsample_curriculum_patch.py`。

核心变更：

1. **`subsample_variable_dt`** — 新增 `effective_max_dt` 参数（默认 `None`，向后兼容）。当 `effective_max_dt <= 1` 时直接返回原始数据 + 全 1 的 `dt_labels`，等价于不子采样；否则用 `effective_max_dt` 替代 `max_dt` 作为 log-uniform 采样上界。

2. **`WorldModel._train`** — 在调用 `subsample_variable_dt` 前先计算 `gate_scale`（复用已有的 phase1/phase2 curriculum 逻辑），然后传入 `effective_max_dt = 1 + gate_scale * (K - 1)`。Phase 1 时 `effective_max_dt=1`，RSSM 训练数据与 imagination 的 dt=1 完全一致。

部署位置：
- `tools.py` 第 763 行起，整个 `subsample_variable_dt` 函数替换
- `models.py` 第 169-173 行，子采样调用块替换

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 51994,
  "duration_api_ms": 52760,
  "num_turns": 6,
  "stop_reason": "end_turn",
  "session_id": "4548d576-751a-4385-85b2-ea3732bcaf07",
  "total_cost_usd": 0.36806600000000006,
  "usage": {
    "input_tokens": 7,
    "cache_creation_input_tokens": 38658,
    "cache_read_input_tokens": 107861,
    "output_tokens": 2816,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 38658,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 336,
        "cache_read_input_tokens": 47951,
        "cache_creation_input_tokens": 2154,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 2154
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1993,
      "outputTokens": 19,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002088,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 7,
      "outputTokens": 2816,
      "cacheReadInputTokens": 107861,
      "cacheCreationInputTokens": 38658,
      "webSearchRequests": 0,
      "costUSD": 0.365978,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "3dcaecbf-832f-4024-ae53-0b1eaf4aa679"
}
```

</details>

---
