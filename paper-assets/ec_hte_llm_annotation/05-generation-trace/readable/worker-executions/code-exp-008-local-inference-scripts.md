# code exp 008 local inference scripts

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 18
- **Recorded user turns:** 0
- **Tool calls:** 5
- **Original source:** `logs/workers/worker_code_exp-008-local-inference-scripts_20260521T115154.log`
- **Structured JSON:** [`e465234bc321501236ba.json`](../../sessions/e4/e465234bc321501236ba.json)

## Before a recorded user message

18 recorded events

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
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "session_id": "f991a6f3-a4d6-4823-9492-c23c8eb8d67e",
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
  "uuid": "e36ca1c4-db00-4df7-bf34-464e0844374b",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude/projects/-home-ubuntu-ec-hte-llm-annotation/memory/"
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
    "resetsAt": 1779378600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "dd1b5300-1b52-4d80-ae14-41c4b1340198",
  "session_id": "f991a6f3-a4d6-4823-9492-c23c8eb8d67e"
}
```

---

### Assistant

_source line 4_

I'll start by reading the reference files to understand the existing patterns, then write both scripts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f991a6f3-a4d6-4823-9492-c23c8eb8d67e",
  "uuid": "2a51efb0-9c9e-47be-9556-cc2f9453f738",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P4nwE13Bu7hWx7CwKmDtxH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 6438,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6438
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

<details open><summary>🔧 Tool call — Read · `toolu_01LztfjuV1ezMb1ij9pkP49f`</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/exp008_gpt5x_annotate.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f991a6f3-a4d6-4823-9492-c23c8eb8d67e",
  "uuid": "98a76471-2db3-4a52-b0ed-56266b81cf58",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P4nwE13Bu7hWx7CwKmDtxH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 6438,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6438
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

_source line 6 · 2026-05-21T11:52:04.178Z_

<details><summary>↩ Tool result · `toolu_01LztfjuV1ezMb1ij9pkP49f`</summary>

```text
1	"""GPT-5.x annotation for exp-008. Tries gpt-5.4 → gpt-5 → gpt-5-mini in order."""
2	import json, os, sys, time
3	import pandas as pd
4	from openai import OpenAI
5	
6	API_KEY = [REDACTED]'/home/ubuntu/ec_hte_llm_annotation/.api_key').read().strip()
7	CLIENT = OpenAI(api_key=[REDACTED], base_url='http://47.94.22.126/v1')
8	MODELS_TO_TRY = ['gpt-5.4', 'gpt-5', 'gpt-5-mini']
9	PROMPT = (
10	    'Classify the sentiment of the following tweet as exactly one of: '
11	    'positive, neutral, negative.\n\n'
12	    'Tweet: "{text}"\n\n'
13	    'Reply with ONLY one word: positive, neutral, or negative.'
14	)
15	DATA = '/home/ubuntu/ec_hte_llm_annotation/results/pilot_gemini_annotations.csv'
16	
17	def test_model(model_name):
18	    """Test if a model works with a simple prompt. Returns True if ok."""
19	    try:
20	        resp = CLIENT.chat.completions.create(
21	            model=model_name,
22	            messages=[{"role": "user", "content": "Say hello."}],
23	            max_tokens=50
24	        )
25	        content = resp.choices[0].message.content
26	        if content and len(content.strip()) > 0:
27	            print(f"  ✓ {model_name} works: '{content.strip()[:50]}'")
28	            return True
29	        print(f"  ✗ {model_name}: empty response")
30	        return False
31	    except Exception as e:
32	        print(f"  ✗ {model_name}: {e}")
33	        return False
34	
35	def find_working_model():
36	    print("Testing GPT-5.x models...")
37	    for m in MODELS_TO_TRY:
38	        if test_model(m):
39	            return m
40	    return None
41	
42	def classify(model, text, max_retries=3):
43	    label_map = {'negative': 0, 'neutral': 1, 'positive': 2}
44	    for attempt in range(max_retries):
45	        try:
46	            resp = CLIENT.chat.completions.create(
47	                model=model,
48	                messages=[{"role": "user", "content": PROMPT.format(text=text)}],
49	                max_tokens=500
50	            )
51	            s = resp.choices[0].message.content.strip().lower()
52	            if s in label_map:
53	                return label_map[s]
54	            for k in label_map:
55	                if k in s:
56	                    return label_map[k]
57	            print(f"  Unparseable: '{s[:60]}', retry {attempt+1}")
58	        except Exception as e:
59	            print(f"  Error: {e}, retry {attempt+1}")
60	            time.sleep(10)
61	    return -1
62	
63	def main():
64	    model = find_working_model()
65	    if not model:
66	        print("ERROR: No GPT-5.x model available. Exiting.")
67	        sys.exit(1)
68	
69	    print(f"\nUsing model: {model}")
70	    ckpt = f'/home/ubuntu/ec_hte_llm_annotation/results/exp008_checkpoint_{model}.json'
71	
72	    df = pd.read_csv(DATA)
73	    results = []
74	    start_idx = 0
75	    if os.path.exists(ckpt):
76	        existing = json.load(open(ckpt))
77	        start_idx = len(existing)
78	        results = existing
79	        print(f"Resuming from {start_idx}")
80	
81	    for i in range(start_idx, len(df)):
82	        text = df.iloc[i]['text']
83	        label = classify(model, text)
84	        results.append(label)
85	        if (i + 1) % 50 == 0:
86	            json.dump(results, open(ckpt, 'w'))
87	            ok = sum(1 for r in results if r >= 0)
88	            print(f"[{i+1}/{len(df)}] done, {ok} valid", flush=True)
89	        time.sleep(1.0)
90	
91	    json.dump(results, open(ckpt, 'w'))
92	    ok = sum(1 for r in results if r >= 0)
93	    print(f"\nDONE: model={model}, {len(results)} total, {ok} valid")
94	    # Write model name for downstream script
95	    with open('/home/ubuntu/ec_hte_llm_annotation/results/exp008_gpt5x_model_used.txt', 'w') as f:
96	        f.write(model)
97	
98	if __name__ == '__main__':
99	    main()
100	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f991a6f3-a4d6-4823-9492-c23c8eb8d67e",
  "uuid": "6601f042-842d-4a9a-aab5-38fa6fa707f6",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/ec_hte_llm_annotation/exp008_gpt5x_annotate.py",
      "content": "\"\"\"GPT-5.x annotation for exp-008. Tries gpt-5.4 → gpt-5 → gpt-5-mini in order.\"\"\"\nimport json, os, sys, time\nimport pandas as pd\nfrom openai import OpenAI\n\nAPI_KEY = [REDACTED]'/home/ubuntu/ec_hte_llm_annotation/.api_key').read().strip()\nCLIENT = OpenAI(api_key=[REDACTED], base_url='http://47.94.22.126/v1')\nMODELS_TO_TRY = ['gpt-5.4', 'gpt-5', 'gpt-5-mini']\nPROMPT = (\n    'Classify the sentiment of the following tweet as exactly one of: '\n    'positive, neutral, negative.\\n\\n'\n    'Tweet: \"{text}\"\\n\\n'\n    'Reply with ONLY one word: positive, neutral, or negative.'\n)\nDATA = '/home/ubuntu/ec_hte_llm_annotation/results/pilot_gemini_annotations.csv'\n\ndef test_model(model_name):\n    \"\"\"Test if a model works with a simple prompt. Returns True if ok.\"\"\"\n    try:\n        resp = CLIENT.chat.completions.create(\n            model=model_name,\n            messages=[{\"role\": \"user\", \"content\": \"Say hello.\"}],\n            max_tokens=50\n        )\n        content = resp.choices[0].message.content\n        if content and len(content.strip()) > 0:\n            print(f\"  ✓ {model_name} works: '{content.strip()[:50]}'\")\n            return True\n        print(f\"  ✗ {model_name}: empty response\")\n        return False\n    except Exception as e:\n        print(f\"  ✗ {model_name}: {e}\")\n        return False\n\ndef find_working_model():\n    print(\"Testing GPT-5.x models...\")\n    for m in MODELS_TO_TRY:\n        if test_model(m):\n            return m\n    return None\n\ndef classify(model, text, max_retries=3):\n    label_map = {'negative': 0, 'neutral': 1, 'positive': 2}\n    for attempt in range(max_retries):\n        try:\n            resp = CLIENT.chat.completions.create(\n                model=model,\n                messages=[{\"role\": \"user\", \"content\": PROMPT.format(text=text)}],\n                max_tokens=500\n            )\n            s = resp.choices[0].message.content.strip().lower()\n            if s in label_map:\n                return label_map[s]\n            for k in label_map:\n                if k in s:\n                    return label_map[k]\n            print(f\"  Unparseable: '{s[:60]}', retry {attempt+1}\")\n        except Exception as e:\n            print(f\"  Error: {e}, retry {attempt+1}\")\n            time.sleep(10)\n    return -1\n\ndef main():\n    model = find_working_model()\n    if not model:\n        print(\"ERROR: No GPT-5.x model available. Exiting.\")\n        sys.exit(1)\n\n    print(f\"\\nUsing model: {model}\")\n    ckpt = f'/home/ubuntu/ec_hte_llm_annotation/results/exp008_checkpoint_{model}.json'\n\n    df = pd.read_csv(DATA)\n    results = []\n    start_idx = 0\n    if os.path.exists(ckpt):\n        existing = json.load(open(ckpt))\n        start_idx = len(existing)\n        results = existing\n        print(f\"Resuming from {start_idx}\")\n\n    for i in range(start_idx, len(df)):\n        text = df.iloc[i]['text']\n        label = classify(model, text)\n        results.append(label)\n        if (i + 1) % 50 == 0:\n            json.dump(results, open(ckpt, 'w'))\n            ok = sum(1 for r in results if r >= 0)\n            print(f\"[{i+1}/{len(df)}] done, {ok} valid\", flush=True)\n        time.sleep(1.0)\n\n    json.dump(results, open(ckpt, 'w'))\n    ok = sum(1 for r in results if r >= 0)\n    print(f\"\\nDONE: model={model}, {len(results)} total, {ok} valid\")\n    # Write model name for downstream script\n    with open('/home/ubuntu/ec_hte_llm_annotation/results/exp008_gpt5x_model_used.txt', 'w') as f:\n        f.write(model)\n\nif __name__ == '__main__':\n    main()\n",
      "numLines": 100,
      "startLine": 1,
      "totalLines": 100
    }
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Bash · `toolu_01AP2wRRH78VXXLXygoKLyzn`</summary>

```json
{
  "command": "head -5 /home/ubuntu/ec_hte_llm_annotation/results/pilot_gemini_annotations.csv",
  "description": "Check CSV structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f991a6f3-a4d6-4823-9492-c23c8eb8d67e",
  "uuid": "5ac16f61-11f1-4716-87e5-8d1d3196d969",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P4nwE13Bu7hWx7CwKmDtxH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 6438,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6438
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

_source line 8 · 2026-05-21T11:52:05.306Z_

<details><summary>↩ Tool result · `toolu_01AP2wRRH78VXXLXygoKLyzn`</summary>

```text
idx,text,true_label,llm_label,has_hashtag,has_mention,text_length_bin
10476,"when you jacked into your house without keys. hell yeah, i'm david blaine jr.",2,2,False,False,short
1824,Cigarettes and Valentines,1,1,False,False,short
409,@user we'll miss you in Seattle! Especially when you win your NL Cy Young award!,2,2,False,True,medium
12149,I'm not going to sack Tony romo but I will sack dak,0,0,False,False,short
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f991a6f3-a4d6-4823-9492-c23c8eb8d67e",
  "uuid": "3c63f98c-89ce-4dc2-8051-13fc35aa0816",
  "tool_use_result": {
    "stdout": "idx,text,true_label,llm_label,has_hashtag,has_mention,text_length_bin\n10476,\"when you jacked into your house without keys. hell yeah, i'm david blaine jr.\",2,2,False,False,short\n1824,Cigarettes and Valentines,1,1,False,False,short\n409,@user we'll miss you in Seattle! Especially when you win your NL Cy Young award!,2,2,False,True,medium\n12149,I'm not going to sack Tony romo but I will sack dak,0,0,False,False,short",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Bash · `toolu_01R9RBwJRHzS1Kd2A3yzZ1qD`</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/ec_hte_llm_annotation/artifacts/exp-008/scripts/",
  "description": "Create output directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f991a6f3-a4d6-4823-9492-c23c8eb8d67e",
  "uuid": "df3d185f-7366-43f3-8ac0-298d75e60661",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P4nwE13Bu7hWx7CwKmDtxH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 6438,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6438
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

_source line 10 · 2026-05-21T11:52:05.685Z_

<details><summary>↩ Tool result · `toolu_01R9RBwJRHzS1Kd2A3yzZ1qD`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f991a6f3-a4d6-4823-9492-c23c8eb8d67e",
  "uuid": "441a3d55-d93e-49b8-8431-f4b357d4ed56",
  "tool_use_result": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": true
  }
}
```

</details>

---

### Assistant

_source line 11_

<details><summary>Logged reasoning block</summary>

```text
Now I have a good understanding of the reference script and data format. Let me write both scripts.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f991a6f3-a4d6-4823-9492-c23c8eb8d67e",
  "uuid": "ba94aa0a-5efb-427f-ba99-d1b19fcf0e42",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016t7zCXBGUGXSTYFU23A5iW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1890,
      "cache_read_input_tokens": 18279,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1890
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

_source line 12_

Now I'll write both scripts in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f991a6f3-a4d6-4823-9492-c23c8eb8d67e",
  "uuid": "18839598-feb3-46b4-8e3e-2e07511a9683",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016t7zCXBGUGXSTYFU23A5iW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1890,
      "cache_read_input_tokens": 18279,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1890
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

_source line 13_

<details open><summary>🔧 Tool call — Write · `toolu_01RaMrQhsYjuZRK2qDXUKXwq`</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/artifacts/exp-008/scripts/llama31_8b_annotate.py",
  "content": "# exp-008: Local Llama-3.1-8B-Instruct sentiment annotation for TweetEval\n#\n# Input:  results/pilot_gemini_annotations.csv (500 tweets, cols: idx, text, true_label, ...)\n# Output: results/exp008_checkpoint_llama-3.1-8b.json (list of integer labels per row)\n#         results/exp008_local_model_used.txt (model identifier)\n# Labels: 0=negative, 1=neutral, 2=positive, -1=parse failure\n#\n# Usage:\n#   pip install transformers torch accelerate\n#   python llama31_8b_annotate.py [--device cuda:0] [--batch-size 1] [--resume] [--model-path PATH]\n\nimport argparse\nimport json\nimport os\nimport re\nimport sys\nimport time\n\nimport pandas as pd\nimport torch\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\n\nPROJECT_ROOT = \"/home/ubuntu/ec_hte_llm_annotation\"\nDATA_PATH = os.path.join(PROJECT_ROOT, \"results/pilot_gemini_annotations.csv\")\nCHECKPOINT_PATH = os.path.join(PROJECT_ROOT, \"results/exp008_checkpoint_llama-3.1-8b.json\")\nMODEL_USED_PATH = os.path.join(PROJECT_ROOT, \"results/exp008_local_model_used.txt\")\nDEFAULT_MODEL = \"meta-llama/Llama-3.1-8B-Instruct\"\n\nPROMPT_TEMPLATE = (\n    'Classify the sentiment of the following tweet as exactly one of: '\n    'positive, neutral, negative.\\n\\n'\n    'Tweet: \"{text}\"\\n\\n'\n    'Reply with ONLY one word: positive, neutral, or negative.'\n)\n\nLABEL_MAP = {\"negative\": 0, \"neutral\": 1, \"positive\": 2}\n\n\ndef parse_label(text: str) -> int:\n    text = text.strip().lower()\n    if text in LABEL_MAP:\n        return LABEL_MAP[text]\n    for keyword in LABEL_MAP:\n        if keyword in text:\n            return LABEL_MAP[keyword]\n    match = re.search(r\"\\b(positive|neutral|negative)\\b\", text)\n    if match:\n        return LABEL_MAP[match.group(1)]\n    return -1\n\n\ndef load_model(model_path: str, device: str):\n    print(f\"Loading tokenizer from {model_path} ...\")\n    tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n\n    dtype = torch.bfloat16 if torch.cuda.is_bf16_supported() else torch.float16\n    print(f\"Loading model in {dtype} on {device} ...\")\n    model = AutoModelForCausalLM.from_pretrained(\n        model_path,\n        torch_dtype=dtype,\n        device_map=device,\n        trust_remote_code=True,\n    )\n    model.eval()\n    return model, tokenizer\n\n\ndef classify_single(model, tokenizer, tweet_text: str, device: str) -> int:\n    messages = [\n        {\"role\": \"user\", \"content\": PROMPT_TEMPLATE.format(text=tweet_text)},\n    ]\n    input_ids = tokenizer.apply_chat_template(messages, return_tensors=\"pt\", add_generation_prompt=True)\n    input_ids = input_ids.to(model.device)\n\n    with torch.no_grad():\n        output_ids = model.generate(\n            input_ids,\n            max_new_tokens=10,\n            do_sample=False,\n            temperature=None,\n            top_p=None,\n        )\n\n    new_tokens = output_ids[0, input_ids.shape[1]:]\n    response = tokenizer.decode(new_tokens, skip_special_tokens=True)\n    return parse_label(response)\n\n\ndef warmup(model, tokenizer, device: str) -> float:\n    print(\"Running warmup inference ...\")\n    start = time.time()\n    classify_single(model, tokenizer, \"This is a test tweet.\", device)\n    elapsed = time.time() - start\n    print(f\"Warmup done in {elapsed:.2f}s\")\n    return elapsed\n\n\ndef main():\n    parser = argparse.ArgumentParser(description=\"Llama-3.1-8B TweetEval sentiment annotation\")\n    parser.add_argument(\"--device\", default=\"cuda:0\", help=\"Torch device (default: cuda:0)\")\n    parser.add_argument(\"--batch-size\", type=int, default=1, help=\"Batch size (default: 1)\")\n    parser.add_argument(\"--resume\", action=\"store_true\", help=\"Resume from checkpoint\")\n    parser.add_argument(\"--model-path\", default=DEFAULT_MODEL, help=\"HuggingFace model ID or local path\")\n    args = parser.parse_args()\n\n    df = pd.read_csv(DATA_PATH)\n    total = len(df)\n    print(f\"Loaded {total} tweets from {DATA_PATH}\")\n\n    results = []\n    start_idx = 0\n    if args.resume and os.path.exists(CHECKPOINT_PATH):\n        with open(CHECKPOINT_PATH) as f:\n            results = json.load(f)\n        start_idx = len(results)\n        print(f\"Resuming from index {start_idx}\")\n\n    if start_idx >= total:\n        print(\"All annotations already complete.\")\n        return\n\n    try:\n        model, tokenizer = load_model(args.model_path, args.device)\n    except RuntimeError as e:\n        if \"out of memory\" in str(e).lower() or \"CUDA\" in str(e):\n            print(f\"OOM loading model: {e}\")\n            print(\"Try: --device cpu (slow) or use a GPU with >=16GB VRAM\")\n            sys.exit(1)\n        raise\n\n    per_item = warmup(model, tokenizer, args.device)\n    remaining = total - start_idx\n    est_minutes = (remaining * per_item) / 60\n    print(f\"Estimated time for {remaining} remaining tweets: {est_minutes:.1f} min\")\n\n    failed = 0\n    t0 = time.time()\n\n    for i in range(start_idx, total):\n        tweet = df.iloc[i][\"text\"]\n        try:\n            label = classify_single(model, tokenizer, str(tweet), args.device)\n        except RuntimeError as e:\n            if \"out of memory\" in str(e).lower():\n                torch.cuda.empty_cache()\n                print(f\"OOM at index {i}. Try reducing --batch-size or use a larger GPU.\")\n                with open(CHECKPOINT_PATH, \"w\") as f:\n                    json.dump(results, f)\n                print(f\"Checkpoint saved at {len(results)} annotations.\")\n                sys.exit(1)\n            raise\n\n        results.append(label)\n        if label == -1:\n            failed += 1\n\n        if (i + 1) % 50 == 0:\n            with open(CHECKPOINT_PATH, \"w\") as f:\n                json.dump(results, f)\n            valid = sum(1 for r in results if r >= 0)\n            elapsed = time.time() - t0\n            rate = (i - start_idx + 1) / elapsed\n            print(f\"[{i + 1}/{total}] {valid} valid, {failed} failed, {rate:.1f} tweets/s\", flush=True)\n\n    with open(CHECKPOINT_PATH, \"w\") as f:\n        json.dump(results, f)\n\n    with open(MODEL_USED_PATH, \"w\") as f:\n        f.write(args.model_path)\n\n    valid = sum(1 for r in results if r >= 0)\n    elapsed = time.time() - t0\n    print(f\"\\n--- Summary ---\")\n    print(f\"Model:   {args.model_path}\")\n    print(f\"Total:   {len(results)}\")\n    print(f\"Valid:   {valid}\")\n    print(f\"Failed:  {failed}\")\n    print(f\"Time:    {elapsed:.1f}s ({elapsed / 60:.1f} min)\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f991a6f3-a4d6-4823-9492-c23c8eb8d67e",
  "uuid": "a3a0277c-2d68-4f2b-91b9-868570181f89",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016t7zCXBGUGXSTYFU23A5iW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1890,
      "cache_read_input_tokens": 18279,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1890
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

_source line 14 · 2026-05-21T11:52:37.934Z_

<details><summary>↩ Tool result · `toolu_01RaMrQhsYjuZRK2qDXUKXwq`</summary>

```text
File created successfully at: /home/ubuntu/ec_hte_llm_annotation/artifacts/exp-008/scripts/llama31_8b_annotate.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f991a6f3-a4d6-4823-9492-c23c8eb8d67e",
  "uuid": "1dfe3aba-170f-4075-88b3-b78431ea5130",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/ec_hte_llm_annotation/artifacts/exp-008/scripts/llama31_8b_annotate.py",
    "content": "# exp-008: Local Llama-3.1-8B-Instruct sentiment annotation for TweetEval\n#\n# Input:  results/pilot_gemini_annotations.csv (500 tweets, cols: idx, text, true_label, ...)\n# Output: results/exp008_checkpoint_llama-3.1-8b.json (list of integer labels per row)\n#         results/exp008_local_model_used.txt (model identifier)\n# Labels: 0=negative, 1=neutral, 2=positive, -1=parse failure\n#\n# Usage:\n#   pip install transformers torch accelerate\n#   python llama31_8b_annotate.py [--device cuda:0] [--batch-size 1] [--resume] [--model-path PATH]\n\nimport argparse\nimport json\nimport os\nimport re\nimport sys\nimport time\n\nimport pandas as pd\nimport torch\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\n\nPROJECT_ROOT = \"/home/ubuntu/ec_hte_llm_annotation\"\nDATA_PATH = os.path.join(PROJECT_ROOT, \"results/pilot_gemini_annotations.csv\")\nCHECKPOINT_PATH = os.path.join(PROJECT_ROOT, \"results/exp008_checkpoint_llama-3.1-8b.json\")\nMODEL_USED_PATH = os.path.join(PROJECT_ROOT, \"results/exp008_local_model_used.txt\")\nDEFAULT_MODEL = \"meta-llama/Llama-3.1-8B-Instruct\"\n\nPROMPT_TEMPLATE = (\n    'Classify the sentiment of the following tweet as exactly one of: '\n    'positive, neutral, negative.\\n\\n'\n    'Tweet: \"{text}\"\\n\\n'\n    'Reply with ONLY one word: positive, neutral, or negative.'\n)\n\nLABEL_MAP = {\"negative\": 0, \"neutral\": 1, \"positive\": 2}\n\n\ndef parse_label(text: str) -> int:\n    text = text.strip().lower()\n    if text in LABEL_MAP:\n        return LABEL_MAP[text]\n    for keyword in LABEL_MAP:\n        if keyword in text:\n            return LABEL_MAP[keyword]\n    match = re.search(r\"\\b(positive|neutral|negative)\\b\", text)\n    if match:\n        return LABEL_MAP[match.group(1)]\n    return -1\n\n\ndef load_model(model_path: str, device: str):\n    print(f\"Loading tokenizer from {model_path} ...\")\n    tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n\n    dtype = torch.bfloat16 if torch.cuda.is_bf16_supported() else torch.float16\n    print(f\"Loading model in {dtype} on {device} ...\")\n    model = AutoModelForCausalLM.from_pretrained(\n        model_path,\n        torch_dtype=dtype,\n        device_map=device,\n        trust_remote_code=True,\n    )\n    model.eval()\n    return model, tokenizer\n\n\ndef classify_single(model, tokenizer, tweet_text: str, device: str) -> int:\n    messages = [\n        {\"role\": \"user\", \"content\": PROMPT_TEMPLATE.format(text=tweet_text)},\n    ]\n    input_ids = tokenizer.apply_chat_template(messages, return_tensors=\"pt\", add_generation_prompt=True)\n    input_ids = input_ids.to(model.device)\n\n    with torch.no_grad():\n        output_ids = model.generate(\n            input_ids,\n            max_new_tokens=10,\n            do_sample=False,\n            temperature=None,\n            top_p=None,\n        )\n\n    new_tokens = output_ids[0, input_ids.shape[1]:]\n    response = tokenizer.decode(new_tokens, skip_special_tokens=True)\n    return parse_label(response)\n\n\ndef warmup(model, tokenizer, device: str) -> float:\n    print(\"Running warmup inference ...\")\n    start = time.time()\n    classify_single(model, tokenizer, \"This is a test tweet.\", device)\n    elapsed = time.time() - start\n    print(f\"Warmup done in {elapsed:.2f}s\")\n    return elapsed\n\n\ndef main():\n    parser = argparse.ArgumentParser(description=\"Llama-3.1-8B TweetEval sentiment annotation\")\n    parser.add_argument(\"--device\", default=\"cuda:0\", help=\"Torch device (default: cuda:0)\")\n    parser.add_argument(\"--batch-size\", type=int, default=1, help=\"Batch size (default: 1)\")\n    parser.add_argument(\"--resume\", action=\"store_true\", help=\"Resume from checkpoint\")\n    parser.add_argument(\"--model-path\", default=DEFAULT_MODEL, help=\"HuggingFace model ID or local path\")\n    args = parser.parse_args()\n\n    df = pd.read_csv(DATA_PATH)\n    total = len(df)\n    print(f\"Loaded {total} tweets from {DATA_PATH}\")\n\n    results = []\n    start_idx = 0\n    if args.resume and os.path.exists(CHECKPOINT_PATH):\n        with open(CHECKPOINT_PATH) as f:\n            results = json.load(f)\n        start_idx = len(results)\n        print(f\"Resuming from index {start_idx}\")\n\n    if start_idx >= total:\n        print(\"All annotations already complete.\")\n        return\n\n    try:\n        model, tokenizer = load_model(args.model_path, args.device)\n    except RuntimeError as e:\n        if \"out of memory\" in str(e).lower() or \"CUDA\" in str(e):\n            print(f\"OOM loading model: {e}\")\n            print(\"Try: --device cpu (slow) or use a GPU with >=16GB VRAM\")\n            sys.exit(1)\n        raise\n\n    per_item = warmup(model, tokenizer, args.device)\n    remaining = total - start_idx\n    est_minutes = (remaining * per_item) / 60\n    print(f\"Estimated time for {remaining} remaining tweets: {est_minutes:.1f} min\")\n\n    failed = 0\n    t0 = time.time()\n\n    for i in range(start_idx, total):\n        tweet = df.iloc[i][\"text\"]\n        try:\n            label = classify_single(model, tokenizer, str(tweet), args.device)\n        except RuntimeError as e:\n            if \"out of memory\" in str(e).lower():\n                torch.cuda.empty_cache()\n                print(f\"OOM at index {i}. Try reducing --batch-size or use a larger GPU.\")\n                with open(CHECKPOINT_PATH, \"w\") as f:\n                    json.dump(results, f)\n                print(f\"Checkpoint saved at {len(results)} annotations.\")\n                sys.exit(1)\n            raise\n\n        results.append(label)\n        if label == -1:\n            failed += 1\n\n        if (i + 1) % 50 == 0:\n            with open(CHECKPOINT_PATH, \"w\") as f:\n                json.dump(results, f)\n            valid = sum(1 for r in results if r >= 0)\n            elapsed = time.time() - t0\n            rate = (i - start_idx + 1) / elapsed\n            print(f\"[{i + 1}/{total}] {valid} valid, {failed} failed, {rate:.1f} tweets/s\", flush=True)\n\n    with open(CHECKPOINT_PATH, \"w\") as f:\n        json.dump(results, f)\n\n    with open(MODEL_USED_PATH, \"w\") as f:\n        f.write(args.model_path)\n\n    valid = sum(1 for r in results if r >= 0)\n    elapsed = time.time() - t0\n    print(f\"\\n--- Summary ---\")\n    print(f\"Model:   {args.model_path}\")\n    print(f\"Total:   {len(results)}\")\n    print(f\"Valid:   {valid}\")\n    print(f\"Failed:  {failed}\")\n    print(f\"Time:    {elapsed:.1f}s ({elapsed / 60:.1f} min)\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Write · `toolu_01HeCcoR41jrRRJHzhezkTys`</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/artifacts/exp-008/scripts/qwen25_7b_annotate.py",
  "content": "# exp-008: Local Qwen2.5-7B-Instruct sentiment annotation for TweetEval\n#\n# Input:  results/pilot_gemini_annotations.csv (500 tweets, cols: idx, text, true_label, ...)\n# Output: results/exp008_checkpoint_qwen2.5-7b.json (list of integer labels per row)\n#         results/exp008_local_model_used.txt (model identifier)\n# Labels: 0=negative, 1=neutral, 2=positive, -1=parse failure\n#\n# Usage:\n#   pip install transformers torch accelerate\n#   python qwen25_7b_annotate.py [--device cuda:0] [--batch-size 1] [--resume] [--model-path PATH]\n\nimport argparse\nimport json\nimport os\nimport re\nimport sys\nimport time\n\nimport pandas as pd\nimport torch\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\n\nPROJECT_ROOT = \"/home/ubuntu/ec_hte_llm_annotation\"\nDATA_PATH = os.path.join(PROJECT_ROOT, \"results/pilot_gemini_annotations.csv\")\nCHECKPOINT_PATH = os.path.join(PROJECT_ROOT, \"results/exp008_checkpoint_qwen2.5-7b.json\")\nMODEL_USED_PATH = os.path.join(PROJECT_ROOT, \"results/exp008_local_model_used.txt\")\nDEFAULT_MODEL = \"Qwen/Qwen2.5-7B-Instruct\"\n\nPROMPT_TEMPLATE = (\n    'Classify the sentiment of the following tweet as exactly one of: '\n    'positive, neutral, negative.\\n\\n'\n    'Tweet: \"{text}\"\\n\\n'\n    'Reply with ONLY one word: positive, neutral, or negative.'\n)\n\nLABEL_MAP = {\"negative\": 0, \"neutral\": 1, \"positive\": 2}\n\n\ndef parse_label(text: str) -> int:\n    text = text.strip().lower()\n    if text in LABEL_MAP:\n        return LABEL_MAP[text]\n    for keyword in LABEL_MAP:\n        if keyword in text:\n            return LABEL_MAP[keyword]\n    match = re.search(r\"\\b(positive|neutral|negative)\\b\", text)\n    if match:\n        return LABEL_MAP[match.group(1)]\n    return -1\n\n\ndef load_model(model_path: str, device: str):\n    print(f\"Loading tokenizer from {model_path} ...\")\n    tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n\n    dtype = torch.bfloat16 if torch.cuda.is_bf16_supported() else torch.float16\n    print(f\"Loading model in {dtype} on {device} ...\")\n    model = AutoModelForCausalLM.from_pretrained(\n        model_path,\n        torch_dtype=dtype,\n        device_map=device,\n        trust_remote_code=True,\n    )\n    model.eval()\n    return model, tokenizer\n\n\ndef classify_single(model, tokenizer, tweet_text: str, device: str) -> int:\n    messages = [\n        {\"role\": \"system\", \"content\": \"You are a helpful assistant.\"},\n        {\"role\": \"user\", \"content\": PROMPT_TEMPLATE.format(text=tweet_text)},\n    ]\n    input_text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)\n    inputs = tokenizer(input_text, return_tensors=\"pt\").to(model.device)\n\n    with torch.no_grad():\n        output_ids = model.generate(\n            **inputs,\n            max_new_tokens=10,\n            do_sample=False,\n            temperature=None,\n            top_p=None,\n        )\n\n    new_tokens = output_ids[0, inputs[\"input_ids\"].shape[1]:]\n    response = tokenizer.decode(new_tokens, skip_special_tokens=True)\n    return parse_label(response)\n\n\ndef warmup(model, tokenizer, device: str) -> float:\n    print(\"Running warmup inference ...\")\n    start = time.time()\n    classify_single(model, tokenizer, \"This is a test tweet.\", device)\n    elapsed = time.time() - start\n    print(f\"Warmup done in {elapsed:.2f}s\")\n    return elapsed\n\n\ndef main():\n    parser = argparse.ArgumentParser(description=\"Qwen2.5-7B TweetEval sentiment annotation\")\n    parser.add_argument(\"--device\", default=\"cuda:0\", help=\"Torch device (default: cuda:0)\")\n    parser.add_argument(\"--batch-size\", type=int, default=1, help=\"Batch size (default: 1)\")\n    parser.add_argument(\"--resume\", action=\"store_true\", help=\"Resume from checkpoint\")\n    parser.add_argument(\"--model-path\", default=DEFAULT_MODEL, help=\"HuggingFace model ID or local path\")\n    args = parser.parse_args()\n\n    df = pd.read_csv(DATA_PATH)\n    total = len(df)\n    print(f\"Loaded {total} tweets from {DATA_PATH}\")\n\n    results = []\n    start_idx = 0\n    if args.resume and os.path.exists(CHECKPOINT_PATH):\n        with open(CHECKPOINT_PATH) as f:\n            results = json.load(f)\n        start_idx = len(results)\n        print(f\"Resuming from index {start_idx}\")\n\n    if start_idx >= total:\n        print(\"All annotations already complete.\")\n        return\n\n    try:\n        model, tokenizer = load_model(args.model_path, args.device)\n    except RuntimeError as e:\n        if \"out of memory\" in str(e).lower() or \"CUDA\" in str(e):\n            print(f\"OOM loading model: {e}\")\n            print(\"Try: --device cpu (slow) or use a GPU with >=16GB VRAM\")\n            sys.exit(1)\n        raise\n\n    per_item = warmup(model, tokenizer, args.device)\n    remaining = total - start_idx\n    est_minutes = (remaining * per_item) / 60\n    print(f\"Estimated time for {remaining} remaining tweets: {est_minutes:.1f} min\")\n\n    failed = 0\n    t0 = time.time()\n\n    for i in range(start_idx, total):\n        tweet = df.iloc[i][\"text\"]\n        try:\n            label = classify_single(model, tokenizer, str(tweet), args.device)\n        except RuntimeError as e:\n            if \"out of memory\" in str(e).lower():\n                torch.cuda.empty_cache()\n                print(f\"OOM at index {i}. Try reducing --batch-size or use a larger GPU.\")\n                with open(CHECKPOINT_PATH, \"w\") as f:\n                    json.dump(results, f)\n                print(f\"Checkpoint saved at {len(results)} annotations.\")\n                sys.exit(1)\n            raise\n\n        results.append(label)\n        if label == -1:\n            failed += 1\n\n        if (i + 1) % 50 == 0:\n            with open(CHECKPOINT_PATH, \"w\") as f:\n                json.dump(results, f)\n            valid = sum(1 for r in results if r >= 0)\n            elapsed = time.time() - t0\n            rate = (i - start_idx + 1) / elapsed\n            print(f\"[{i + 1}/{total}] {valid} valid, {failed} failed, {rate:.1f} tweets/s\", flush=True)\n\n    with open(CHECKPOINT_PATH, \"w\") as f:\n        json.dump(results, f)\n\n    with open(MODEL_USED_PATH, \"w\") as f:\n        f.write(args.model_path)\n\n    valid = sum(1 for r in results if r >= 0)\n    elapsed = time.time() - t0\n    print(f\"\\n--- Summary ---\")\n    print(f\"Model:   {args.model_path}\")\n    print(f\"Total:   {len(results)}\")\n    print(f\"Valid:   {valid}\")\n    print(f\"Failed:  {failed}\")\n    print(f\"Time:    {elapsed:.1f}s ({elapsed / 60:.1f} min)\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f991a6f3-a4d6-4823-9492-c23c8eb8d67e",
  "uuid": "793b73c3-27c0-423d-ba28-f5a09f7f7739",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016t7zCXBGUGXSTYFU23A5iW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1890,
      "cache_read_input_tokens": 18279,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1890
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

_source line 16 · 2026-05-21T11:52:54.552Z_

<details><summary>↩ Tool result · `toolu_01HeCcoR41jrRRJHzhezkTys`</summary>

```text
File created successfully at: /home/ubuntu/ec_hte_llm_annotation/artifacts/exp-008/scripts/qwen25_7b_annotate.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f991a6f3-a4d6-4823-9492-c23c8eb8d67e",
  "uuid": "85f17dbf-57e1-4261-91fd-2f9083eb1da3",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/ec_hte_llm_annotation/artifacts/exp-008/scripts/qwen25_7b_annotate.py",
    "content": "# exp-008: Local Qwen2.5-7B-Instruct sentiment annotation for TweetEval\n#\n# Input:  results/pilot_gemini_annotations.csv (500 tweets, cols: idx, text, true_label, ...)\n# Output: results/exp008_checkpoint_qwen2.5-7b.json (list of integer labels per row)\n#         results/exp008_local_model_used.txt (model identifier)\n# Labels: 0=negative, 1=neutral, 2=positive, -1=parse failure\n#\n# Usage:\n#   pip install transformers torch accelerate\n#   python qwen25_7b_annotate.py [--device cuda:0] [--batch-size 1] [--resume] [--model-path PATH]\n\nimport argparse\nimport json\nimport os\nimport re\nimport sys\nimport time\n\nimport pandas as pd\nimport torch\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\n\nPROJECT_ROOT = \"/home/ubuntu/ec_hte_llm_annotation\"\nDATA_PATH = os.path.join(PROJECT_ROOT, \"results/pilot_gemini_annotations.csv\")\nCHECKPOINT_PATH = os.path.join(PROJECT_ROOT, \"results/exp008_checkpoint_qwen2.5-7b.json\")\nMODEL_USED_PATH = os.path.join(PROJECT_ROOT, \"results/exp008_local_model_used.txt\")\nDEFAULT_MODEL = \"Qwen/Qwen2.5-7B-Instruct\"\n\nPROMPT_TEMPLATE = (\n    'Classify the sentiment of the following tweet as exactly one of: '\n    'positive, neutral, negative.\\n\\n'\n    'Tweet: \"{text}\"\\n\\n'\n    'Reply with ONLY one word: positive, neutral, or negative.'\n)\n\nLABEL_MAP = {\"negative\": 0, \"neutral\": 1, \"positive\": 2}\n\n\ndef parse_label(text: str) -> int:\n    text = text.strip().lower()\n    if text in LABEL_MAP:\n        return LABEL_MAP[text]\n    for keyword in LABEL_MAP:\n        if keyword in text:\n            return LABEL_MAP[keyword]\n    match = re.search(r\"\\b(positive|neutral|negative)\\b\", text)\n    if match:\n        return LABEL_MAP[match.group(1)]\n    return -1\n\n\ndef load_model(model_path: str, device: str):\n    print(f\"Loading tokenizer from {model_path} ...\")\n    tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n\n    dtype = torch.bfloat16 if torch.cuda.is_bf16_supported() else torch.float16\n    print(f\"Loading model in {dtype} on {device} ...\")\n    model = AutoModelForCausalLM.from_pretrained(\n        model_path,\n        torch_dtype=dtype,\n        device_map=device,\n        trust_remote_code=True,\n    )\n    model.eval()\n    return model, tokenizer\n\n\ndef classify_single(model, tokenizer, tweet_text: str, device: str) -> int:\n    messages = [\n        {\"role\": \"system\", \"content\": \"You are a helpful assistant.\"},\n        {\"role\": \"user\", \"content\": PROMPT_TEMPLATE.format(text=tweet_text)},\n    ]\n    input_text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)\n    inputs = tokenizer(input_text, return_tensors=\"pt\").to(model.device)\n\n    with torch.no_grad():\n        output_ids = model.generate(\n            **inputs,\n            max_new_tokens=10,\n            do_sample=False,\n            temperature=None,\n            top_p=None,\n        )\n\n    new_tokens = output_ids[0, inputs[\"input_ids\"].shape[1]:]\n    response = tokenizer.decode(new_tokens, skip_special_tokens=True)\n    return parse_label(response)\n\n\ndef warmup(model, tokenizer, device: str) -> float:\n    print(\"Running warmup inference ...\")\n    start = time.time()\n    classify_single(model, tokenizer, \"This is a test tweet.\", device)\n    elapsed = time.time() - start\n    print(f\"Warmup done in {elapsed:.2f}s\")\n    return elapsed\n\n\ndef main():\n    parser = argparse.ArgumentParser(description=\"Qwen2.5-7B TweetEval sentiment annotation\")\n    parser.add_argument(\"--device\", default=\"cuda:0\", help=\"Torch device (default: cuda:0)\")\n    parser.add_argument(\"--batch-size\", type=int, default=1, help=\"Batch size (default: 1)\")\n    parser.add_argument(\"--resume\", action=\"store_true\", help=\"Resume from checkpoint\")\n    parser.add_argument(\"--model-path\", default=DEFAULT_MODEL, help=\"HuggingFace model ID or local path\")\n    args = parser.parse_args()\n\n    df = pd.read_csv(DATA_PATH)\n    total = len(df)\n    print(f\"Loaded {total} tweets from {DATA_PATH}\")\n\n    results = []\n    start_idx = 0\n    if args.resume and os.path.exists(CHECKPOINT_PATH):\n        with open(CHECKPOINT_PATH) as f:\n            results = json.load(f)\n        start_idx = len(results)\n        print(f\"Resuming from index {start_idx}\")\n\n    if start_idx >= total:\n        print(\"All annotations already complete.\")\n        return\n\n    try:\n        model, tokenizer = load_model(args.model_path, args.device)\n    except RuntimeError as e:\n        if \"out of memory\" in str(e).lower() or \"CUDA\" in str(e):\n            print(f\"OOM loading model: {e}\")\n            print(\"Try: --device cpu (slow) or use a GPU with >=16GB VRAM\")\n            sys.exit(1)\n        raise\n\n    per_item = warmup(model, tokenizer, args.device)\n    remaining = total - start_idx\n    est_minutes = (remaining * per_item) / 60\n    print(f\"Estimated time for {remaining} remaining tweets: {est_minutes:.1f} min\")\n\n    failed = 0\n    t0 = time.time()\n\n    for i in range(start_idx, total):\n        tweet = df.iloc[i][\"text\"]\n        try:\n            label = classify_single(model, tokenizer, str(tweet), args.device)\n        except RuntimeError as e:\n            if \"out of memory\" in str(e).lower():\n                torch.cuda.empty_cache()\n                print(f\"OOM at index {i}. Try reducing --batch-size or use a larger GPU.\")\n                with open(CHECKPOINT_PATH, \"w\") as f:\n                    json.dump(results, f)\n                print(f\"Checkpoint saved at {len(results)} annotations.\")\n                sys.exit(1)\n            raise\n\n        results.append(label)\n        if label == -1:\n            failed += 1\n\n        if (i + 1) % 50 == 0:\n            with open(CHECKPOINT_PATH, \"w\") as f:\n                json.dump(results, f)\n            valid = sum(1 for r in results if r >= 0)\n            elapsed = time.time() - t0\n            rate = (i - start_idx + 1) / elapsed\n            print(f\"[{i + 1}/{total}] {valid} valid, {failed} failed, {rate:.1f} tweets/s\", flush=True)\n\n    with open(CHECKPOINT_PATH, \"w\") as f:\n        json.dump(results, f)\n\n    with open(MODEL_USED_PATH, \"w\") as f:\n        f.write(args.model_path)\n\n    valid = sum(1 for r in results if r >= 0)\n    elapsed = time.time() - t0\n    print(f\"\\n--- Summary ---\")\n    print(f\"Model:   {args.model_path}\")\n    print(f\"Total:   {len(results)}\")\n    print(f\"Valid:   {valid}\")\n    print(f\"Failed:  {failed}\")\n    print(f\"Time:    {elapsed:.1f}s ({elapsed / 60:.1f} min)\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 17_

Done. Two scripts written to `artifacts/exp-008/scripts/`:

**`llama31_8b_annotate.py`** — `meta-llama/Llama-3.1-8B-Instruct`
- Uses `tokenizer.apply_chat_template` with Llama's native chat format (no system message, as Llama 3.1 works fine with user-only)
- Returns tensors directly from `apply_chat_template`

**`qwen25_7b_annotate.py`** — `Qwen/Qwen2.5-7B-Instruct`
- Uses Qwen's chat template with a system message (`"You are a helpful assistant."`, Qwen's default)
- Calls `apply_chat_template(tokenize=False)` then tokenizes separately, matching Qwen's recommended pattern

Both scripts share the same structure: same prompt as exp-008, bfloat16/float16 auto-select, greedy decoding (`do_sample=False`, `max_new_tokens=10`), checkpoint every 50 to JSON, OOM handling, `--device`/`--batch-size`/`--resume`/`--model-path` CLI flags, warmup timing estimate, and end-of-run summary.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f991a6f3-a4d6-4823-9492-c23c8eb8d67e",
  "uuid": "87cd8b4f-9a46-4534-be49-20e4fbf6fe04",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HhWdmH3Qc3pXdzr2PrkSgG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4573,
      "cache_read_input_tokens": 20169,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4573
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

_source line 18_

Done. Two scripts written to `artifacts/exp-008/scripts/`:

**`llama31_8b_annotate.py`** — `meta-llama/Llama-3.1-8B-Instruct`
- Uses `tokenizer.apply_chat_template` with Llama's native chat format (no system message, as Llama 3.1 works fine with user-only)
- Returns tensors directly from `apply_chat_template`

**`qwen25_7b_annotate.py`** — `Qwen/Qwen2.5-7B-Instruct`
- Uses Qwen's chat template with a system message (`"You are a helpful assistant."`, Qwen's default)
- Calls `apply_chat_template(tokenize=False)` then tokenizes separately, matching Qwen's recommended pattern

Both scripts share the same structure: same prompt as exp-008, bfloat16/float16 auto-select, greedy decoding (`do_sample=False`, `max_new_tokens=10`), checkpoint every 50 to JSON, OOM handling, `--device`/`--batch-size`/`--resume`/`--model-path` CLI flags, warmup timing estimate, and end-of-run summary.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 62769,
  "duration_api_ms": 63740,
  "num_turns": 6,
  "stop_reason": "end_turn",
  "session_id": "f991a6f3-a4d6-4823-9492-c23c8eb8d67e",
  "total_cost_usd": 0.23245675,
  "usage": {
    "input_tokens": 4,
    "cache_creation_input_tokens": 12901,
    "cache_read_input_tokens": 50289,
    "output_tokens": 5003,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 12901,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 306,
        "cache_read_input_tokens": 20169,
        "cache_creation_input_tokens": 4573,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 4573
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1481,
      "outputTokens": 21,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001586,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 4,
      "outputTokens": 5003,
      "cacheReadInputTokens": 50289,
      "cacheCreationInputTokens": 12901,
      "webSearchRequests": 0,
      "costUSD": 0.23087074999999999,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "b167cf28-081f-45da-b8cb-263947f53830"
}
```

</details>

---
