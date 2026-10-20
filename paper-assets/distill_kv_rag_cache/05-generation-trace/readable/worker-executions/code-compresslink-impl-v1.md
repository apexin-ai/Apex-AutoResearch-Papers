# code compresslink impl v1

**distill kv rag cache** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 36
- **Recorded user turns:** 3
- **Tool calls:** 8
- **Original source:** `logs/workers/worker_code_compresslink-impl-v1_20260514T051327.log`
- **Structured JSON:** [`72e29bc90212eda31bc9.json`](../../sessions/72/72e29bc90212eda31bc9.json)

## Before a recorded user message

9 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/distill_kv_rag_cache",
  "session_id": "fdf71b47-8f0f-4233-b6c0-f01ae22a3454",
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
    "mcp__agent-ml-research__register_artifact",
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
  "uuid": "68cf4367-5d40-4581-8d62-c2c812e9fd1e",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-distill-kv-rag-cache/memory/"
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
    "resetsAt": 1778751600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "8110bc78-f25f-4af2-b2b5-3503eb799812",
  "session_id": "fdf71b47-8f0f-4233-b6c0-f01ae22a3454"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to implement the CompressLink MVP codebase. This is a substantial coding task with multiple files. Let me plan the implementation and then write all the files.

Let me first check what already exists in the artifacts directory, then write all the code files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fdf71b47-8f0f-4233-b6c0-f01ae22a3454",
  "uuid": "fda8fa40-1b48-4d75-83bc-7b0c59c80c06",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QZXFqyKKViyspN5qe6KN8U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15162,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15162
      },
      "output_tokens": 27,
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

Let me check the current state of the artifacts directory, then write all the code files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fdf71b47-8f0f-4233-b6c0-f01ae22a3454",
  "uuid": "d347fcd1-f49b-4565-9234-339c2c51d8e0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QZXFqyKKViyspN5qe6KN8U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15162,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15162
      },
      "output_tokens": 27,
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

<details open><summary>🔧 Tool call — Bash · `toolu_01UPQk8uxtBTKnXVC5t5GVs8`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/distill_kv_rag_cache/artifacts/ 2>/dev/null; echo \"---\"; ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/distill_kv_rag_cache/artifacts/compresslink_code/ 2>/dev/null || echo \"DIR_NOT_EXISTS\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fdf71b47-8f0f-4233-b6c0-f01ae22a3454",
  "uuid": "df04cc70-b3ad-4d36-9869-8219595c3763",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QZXFqyKKViyspN5qe6KN8U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15162,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15162
      },
      "output_tokens": 27,
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

_source line 7 · 2026-05-14T05:13:43.903Z_

<details><summary>↩ Tool result · `toolu_01UPQk8uxtBTKnXVC5t5GVs8`</summary>

```text
total 92
drwxr-xr-x 3 ubuntu ubuntu  4096 May 14 04:59 .
drwxr-xr-x 6 ubuntu ubuntu  4096 May 14 04:52 ..
drwxr-xr-x 3 ubuntu ubuntu  4096 May 14 04:28 _project
-rw-r--r-- 1 ubuntu ubuntu 22059 May 14 04:28 kvtc_survey.md
-rw-r--r-- 1 ubuntu ubuntu  2333 May 14 04:59 manifest.yaml
-rw-r--r-- 1 ubuntu ubuntu 17030 May 14 04:51 mepic_survey.md
-rw-r--r-- 1 ubuntu ubuntu 29988 May 14 04:59 prophetkv_survey.md
---
DIR_NOT_EXISTS
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fdf71b47-8f0f-4233-b6c0-f01ae22a3454",
  "uuid": "53def690-4601-482b-bec0-164b7d4fbba0",
  "tool_use_result": {
    "stdout": "total 92\ndrwxr-xr-x 3 ubuntu ubuntu  4096 May 14 04:59 .\ndrwxr-xr-x 6 ubuntu ubuntu  4096 May 14 04:52 ..\ndrwxr-xr-x 3 ubuntu ubuntu  4096 May 14 04:28 _project\n-rw-r--r-- 1 ubuntu ubuntu 22059 May 14 04:28 kvtc_survey.md\n-rw-r--r-- 1 ubuntu ubuntu  2333 May 14 04:59 manifest.yaml\n-rw-r--r-- 1 ubuntu ubuntu 17030 May 14 04:51 mepic_survey.md\n-rw-r--r-- 1 ubuntu ubuntu 29988 May 14 04:59 prophetkv_survey.md\n---\nDIR_NOT_EXISTS",
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

_source line 8_

<details open><summary>🔧 Tool call — Agent · `toolu_01AxWdWziX2UN5if8HFGfTaN`</summary>

```json
{
  "description": "Read KVTC survey for API",
  "subagent_type": "Explore",
  "prompt": "Read the KVTC survey file at /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/distill_kv_rag_cache/artifacts/kvtc_survey.md to understand the KVTC API (function signatures, module structure, data structures). Report back the key API details: module paths, function signatures for compress/decompress/bit_allocation/PCA, and data structure definitions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fdf71b47-8f0f-4233-b6c0-f01ae22a3454",
  "uuid": "2d7a1e79-527b-4014-bec3-26659b13efe2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018XJLSFkKTjH8XZd1N3TCqn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 489,
      "cache_read_input_tokens": 27003,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 489
      },
      "output_tokens": 45,
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

### System

_source line 9_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "ae11cdb486c92a588",
  "tool_use_id": "toolu_01AxWdWziX2UN5if8HFGfTaN",
  "description": "Read KVTC survey for API",
  "task_type": "local_agent",
  "prompt": "Read the KVTC survey file at /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/distill_kv_rag_cache/artifacts/kvtc_survey.md to understand the KVTC API (function signatures, module structure, data structures). Report back the key API details: module paths, function signatures for compress/decompress/bit_allocation/PCA, and data structure definitions.",
  "uuid": "40a30011-ff77-4ca8-94fd-0f4f9cc13d95",
  "session_id": "fdf71b47-8f0f-4233-b6c0-f01ae22a3454"
}
```

---

## Round 1

3 recorded events

### User

_source line 10 · 2026-05-14T05:13:48.803Z_

Read the KVTC survey file at /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/distill_kv_rag_cache/artifacts/kvtc_survey.md to understand the KVTC API (function signatures, module structure, data structures). Report back the key API details: module paths, function signatures for compress/decompress/bit_allocation/PCA, and data structure definitions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01AxWdWziX2UN5if8HFGfTaN",
  "session_id": "fdf71b47-8f0f-4233-b6c0-f01ae22a3454",
  "uuid": "06a6f99b-d42f-4e4e-a417-a428e43017dd"
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — Agent · `toolu_016cLANJVDSeHpFC5Ng7XfBw`</summary>

```json
{
  "description": "Read MEPIC survey for NoPE",
  "subagent_type": "Explore",
  "prompt": "Read the MEPIC survey file at /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/distill_kv_rag_cache/artifacts/mepic_survey.md to understand the MEPIC NoPE implementation details. Report back: how NoPE KV storage works, how boundary recomputation works, monkey-patching approach, and any code snippets."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fdf71b47-8f0f-4233-b6c0-f01ae22a3454",
  "uuid": "280070d9-6525-404c-b96a-99948b670bc9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018XJLSFkKTjH8XZd1N3TCqn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 489,
      "cache_read_input_tokens": 27003,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 489
      },
      "output_tokens": 45,
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

### System

_source line 12_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "ac52294b4d40fe0d9",
  "tool_use_id": "toolu_016cLANJVDSeHpFC5Ng7XfBw",
  "description": "Read MEPIC survey for NoPE",
  "task_type": "local_agent",
  "prompt": "Read the MEPIC survey file at /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/distill_kv_rag_cache/artifacts/mepic_survey.md to understand the MEPIC NoPE implementation details. Report back: how NoPE KV storage works, how boundary recomputation works, monkey-patching approach, and any code snippets.",
  "uuid": "1c739602-05fc-4f50-8acd-5bd05ac88f5a",
  "session_id": "fdf71b47-8f0f-4233-b6c0-f01ae22a3454"
}
```

---

## Round 2

9 recorded events

### User

_source line 13 · 2026-05-14T05:13:50.703Z_

Read the MEPIC survey file at /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/distill_kv_rag_cache/artifacts/mepic_survey.md to understand the MEPIC NoPE implementation details. Report back: how NoPE KV storage works, how boundary recomputation works, monkey-patching approach, and any code snippets.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016cLANJVDSeHpFC5Ng7XfBw",
  "session_id": "fdf71b47-8f0f-4233-b6c0-f01ae22a3454",
  "uuid": "86484b8b-69f4-4fac-bbf7-63809d5ffb4f"
}
```

</details>

---

### System

_source line 14_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ae11cdb486c92a588",
  "tool_use_id": "toolu_01AxWdWziX2UN5if8HFGfTaN",
  "description": "Reading artifacts/kvtc_survey.md",
  "usage": {
    "total_tokens": 18473,
    "tool_uses": 1,
    "duration_ms": 1921
  },
  "last_tool_name": "Read",
  "uuid": "fc9e2134-c5df-4408-b622-914a4967a853",
  "session_id": "fdf71b47-8f0f-4233-b6c0-f01ae22a3454"
}
```

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Read · `toolu_01CFqZctQ3XZkUMBkdUFrvsy`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/distill_kv_rag_cache/artifacts/kvtc_survey.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01AxWdWziX2UN5if8HFGfTaN",
  "session_id": "fdf71b47-8f0f-4233-b6c0-f01ae22a3454",
  "uuid": "71751ab7-cd1a-4b20-b697-a3fb88f14b99",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013Fa5Vd6hZhn6fAFomtBBgo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18454,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18454,
        "ephemeral_1h_input_tokens": 0
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

_source line 16 · 2026-05-14T05:13:50.746Z_

<details><summary>↩ Tool result · `toolu_01CFqZctQ3XZkUMBkdUFrvsy`</summary>

````text
1	# KVTC 代码库深度调研报告
2	
3	> 仓库: https://github.com/OnlyTerp/kvtc  
4	> 论文: arXiv 2511.01815 (ICLR 2026)  
5	> 调研日期: 2026-05-14  
6	> 目的: 为 CompressLink RABA 修改方案提供代码级依据
7	
8	---
9	
10	## 1. 仓库概览
11	
12	### 1.1 项目结构
13	
14	```
15	kvtc/
16	├── src/
17	│   ├── common.py              # 核心数据结构 (CalibrationData, CompressedKVCache, PCAEntry 等)
18	│   ├── pca.py                 # PCA transform, RoPE undo/reapply, PCACalibrator
19	│   ├── quantize.py            # DP bit allocation (精确版), uniform quantize/dequantize
20	│   ├── gpu_ops.py             # greedy bit allocation (近似版), batch quantize/dequantize
21	│   ├── entropy.py             # zlib DEFLATE + bit packing/unpacking
22	│   ├── ans_entropy.py         # rANS entropy coding (triple-mode picker: zlib/LZMA/rANS)
23	│   ├── adaptive_budget.py     # 基于 eigenvalue entropy 的 per-layer adaptive bit budget
24	│   ├── fused_ops.py           # Fused PCA+Quantize 单 pass kernel
25	│   ├── pipeline.py            # 参考 pipeline (CPU, ~160 行)
26	│   ├── pipeline_fast.py       # GPU 加速 pipeline (~233 行)
27	│   ├── triton_kernels.py      # Triton GPU kernels (bit packing)
28	│   ├── cache.py               # HuggingFace DynamicCache 包装
29	│   ├── calibrate.py           # PCA calibration (从模型+数据集)
30	│   ├── calibrate_vllm.py      # vLLM 专用 calibration
31	│   ├── vllm_backend.py        # vLLM attention backend
32	│   ├── vllm_triton.py         # Fused Triton decode attention kernel
33	│   ├── test_kvtc.py           # 38 个单元测试
34	│   └── test_real_model.py     # TinyLlama 集成测试
35	├── cuda/
36	│   ├── kvtc.h                 # CUDA kernel C API header
37	│   ├── kvtc_kernels.cu        # CUDA kernel 实现
38	│   └── CMakeLists.txt
39	├── benchmarks/
40	│   ├── benchmark_v1-v4.py     # 各版本 benchmark
41	│   ├── results_v1-v4.json     # 结果数据
42	│   └── benchmark_perplexity.py
43	└── setup.py
44	```
45	
46	### 1.2 依赖
47	
48	- **核心**: `torch`, `numpy`, `transformers`
49	- **开发**: `pytest`
50	- **可选**: `triton` (GPU bit packing), CUDA toolkit (原生 kernels)
51	- Python 3.10+, PyTorch 2.10+
52	
53	### 1.3 支持模型
54	
55	代码通过 HuggingFace `transformers` 加载模型，理论上支持所有 causal LM。已验证:
56	- Qwen2.5-7B-Instruct (主要 benchmark 模型, 28 layers, 4 KV heads, dim=128)
57	- Llama-3.1-8B-Instruct
58	- TinyLlama (测试用)
59	- Mistral-7B-Instruct
60	
61	PCA calibration 按 `(layer, head_group, kind)` 存储，天然适配不同模型架构。
62	
63	---
64	
65	## 2. 数据流概览
66	
67	```
68	原始 KV cache [layers, tokens, heads, dim] FP16
69	  │
70	  ├── 前 4 tokens → sink buffer (FP16 保留)
71	  ├── 后 128 tokens → window buffer (FP16 保留)
72	  └── 中间 tokens → 压缩流水线:
73	        │
74	        ▼
75	      RoPE Undo (仅 keys, 用 -sin 反转旋转)
76	        │
77	        ▼
78	      PCA Transform: centered = x - mean; coeffs = centered @ Vh.T
79	        │
80	        ▼
81	      DP Bit Allocation: eigenvalues + budget → per-component bit widths [0-16]
82	        │
83	        ▼
84	      Uniform Quantize: per-component affine 量化
85	        │
86	        ▼
87	      Bit Packing → Entropy Coding (zlib/LZMA/rANS triple picker)
88	        │
89	        ▼
90	      CompressedKVCache (bytes + metadata)
91	```
92	
93	---
94	
95	## 3. PCA Pipeline 详解
96	
97	### 3.1 文件位置
98	
99	- `src/pca.py`: PCA transform/inverse, RoPE 操作, `PCACalibrator` 类
100	- `src/calibrate.py`: `KVTCCalibrator` 高层封装
101	
102	### 3.2 PCA 训练数据
103	
104	**离线 one-time calibration**, 流程:
105	1. 选取 ~10 个文本样本
106	2. 前向传播获取 `past_key_values`
107	3. 对 keys 先做 RoPE inverse (消除位置旋转)
108	4. 按 `(layer, head_group, kind)` 分组拼接
109	5. 对每组做 SVD: `U, S, Vh = torch.linalg.svd(centered, full_matrices=False)`
110	6. `eigenvalues = S² / (n-1)`, `eigenvectors = Vh`
111	
112	关键代码 (`pca.py:222-296`):
113	```python
114	def compute(self, bit_budget_ratio: float = 0.25) -> CalibrationData:
115	    data = torch.cat(sample_list, dim=0)  # [total_rows, dim]
116	    mean = data.mean(dim=0)
117	    centered = data - mean
118	    _, singular_values, vh = torch.linalg.svd(centered, full_matrices=False)
119	    eigenvalues = singular_values.square() / max(centered.shape[0] - 1, 1)
120	    # ...
121	    bit_widths = dp_bit_allocation(eigenvalues, bit_budget=total_bits, max_bits=16)
122	```
123	
124	### 3.3 PCA 维度策略
125	
126	- **每层每头独立 PCA** (默认 `head_group_size=1`)，最大化 per-head decorrelation
127	- 保留全部 dim 个 PCA component，但通过 DP bit allocation 将低方差 component 的 bits 设为 0（等效剪枝）
128	- 不做显式维度裁剪——裁剪由 DP 自动发现
129	
130	### 3.4 RoPE 处理
131	
132	- Keys: 压缩前 `apply_rope_inverse` (rotation by -θ)，解压后 `apply_rope` (rotation by θ)
133	- Values: 不使用 RoPE，无需处理
134	- 逆变换精确 (误差 < 1e-5，旋转矩阵的逆就是转置)
135	
136	---
137	
138	## 4. DP Bit Allocation Solver 详解
139	
140	### 4.1 文件位置与行号
141	
142	**精确 DP 版本**: `src/quantize.py:16-56` (41 行)  
143	**贪心近似版本**: `src/gpu_ops.py:10-57` (48 行)
144	
145	### 4.2 精确 DP 版本 (`quantize.py:16-56`)
146	
147	#### 输入
148	- `eigenvalues: Tensor[d]` — PCA eigenvalues (方差), 从 calibration 获取
149	- `bit_budget: int` — 总 bit 预算 (e.g., `dim * 16 * bit_budget_ratio`)
150	- `max_bits: int = 16` — 每 component 最大 bit 宽度
151	- `group_size: int = 1` — component 分组大小
152	
153	#### 输出
154	- `widths: Tensor[d]` — per-component bit 分配, 每个值 ∈ [0, 16]
155	
156	#### Error Function (核心)
157	
158	```python
159	error = variance if bits == 0 else variance / (4 ** bits)
160	```
161	
162	即: `E(i, b) = λ_i / 4^b`
163	
164	- `λ_i` 是第 i 个 PCA component 的 eigenvalue (方差)
165	- `4^b` 是 b bits 量化带来的 MSE 降低因子 (每 bit 减半量化步长, MSE 减为 1/4)
166	- `bits == 0` 时 error 就是 variance 本身 (完全丢弃该 component)
167	
168	#### DP 状态转移
169	
170	```
171	dp[i][b] = min total MSE using components 0..i-1 with total budget b
172	```
173	
174	转移:
175	```
176	dp[i][cost] = min over w in {0..16}:  dp[i-1][used] + λ_group / 4^w
177	              where cost = used + w * group_width
178	```
179	
180	回溯得到每个 component 的 bit 分配。
181	
182	#### 复杂度
183	
184	`O(d × B × max_bits)` = O(128 × 512 × 16) ≈ 1M ops per entry. 足够快。
185	
186	#### 完整代码
187	
188	```python
189	def dp_bit_allocation(eigenvalues, bit_budget, max_bits=16, group_size=1):
190	    values = eigenvalues.detach().to(torch.float64).flatten()
191	    groups = _component_groups(values, group_size)
192	    max_budget = max(int(bit_budget), 0)
193	    num_groups = len(groups)
194	    inf = float("inf")
195	    dp = [[inf] * (max_budget + 1) for _ in range(num_groups + 1)]
196	    back = [[0] * (max_budget + 1) for _ in range(num_groups + 1)]
197	    dp[0][0] = 0.0
198	    for idx, group in enumerate(groups, start=1):
199	        variance = float(group.sum().item())
200	        width = group.numel()
201	        for used in range(max_budget + 1):
202	            if dp[idx - 1][used] == inf:
203	                continue
204	            for bits in range(0, max_bits + 1):
205	                cost = used + bits * width
206	                if cost > max_budget:
207	                    continue
208	                error = variance if bits == 0 else variance / (4 ** bits)
209	                candidate = dp[idx - 1][used] + error
210	                if candidate < dp[idx][cost]:
211	                    dp[idx][cost] = candidate
212	                    back[idx][cost] = bits
213	    best_budget = min(range(max_budget + 1), key=lambda b: dp[num_groups][b])
214	    # backtrack ...
215	    return widths
216	```
217	
218	### 4.3 贪心近似版本 (`gpu_ops.py:10-57`)
219	
220	生产管线 `pipeline_fast.py` 使用此版本。原理:
221	
222	```
223	gain(i, b) = λ_i × 3 / 4^b
224	```
225	
226	预计算所有 `(component, bit_level)` 的 marginal gain, flatten + topk 取 top-B 个, bincount 得 per-component bits。
227	
228	复杂度 `O(B log(d × max_bits))`, 远快于精确 DP。
229	
230	由于 gain 在 bit_level 上单调递减, 贪心解等价于最优解（标准可分离凸优化问题）。
231	
232	### 4.4 调用链
233	
234	1. **Calibration 时**: `pca.py:PCACalibrator.compute()` → `quantize.py:dp_bit_allocation()` → 存入 `PCAEntry.bit_widths`
235	2. **参考 pipeline**: `pipeline.py:compress()` → `quantize.py:dp_bit_allocation()` (每次压缩重新计算)
236	3. **GPU pipeline**: `pipeline_fast.py:compress()` → `gpu_ops.py:greedy_bit_allocation()` (用 calibration 的 bit_budget)
237	
238	---
239	
240	## 5. RABA 修改方案
241	
242	### 5.1 RABA 核心思想
243	
244	将 error function 从:
245	```
246	E(i, b) = λ_i / 4^b
247	```
248	修改为:
249	```
250	E(i, b, t) = (1 - p_r(t)) × λ_i / 4^b
251	```
252	
253	其中 `p_r(t)` 是 token t 被 RAG cache 恢复的概率。对于高概率被恢复的 token，其量化误差在最终重建时会被精确值覆盖，因此可以分配更少的 bits。
254	
255	### 5.2 需要修改的文件和函数
256	
257	#### 修改 1: `src/quantize.py` — `dp_bit_allocation()`
258	
259	**当前签名** (line 16):
260	```python
261	def dp_bit_allocation(eigenvalues, bit_budget, max_bits=16, group_size=1):
262	```
263	
264	**RABA 签名**:
265	```python
266	def dp_bit_allocation(eigenvalues, bit_budget, max_bits=16, group_size=1, 
267	                      restoration_weights=None):
268	```
269	
270	**修改位置** (line 42):
271	```python
272	# 当前:
273	error = variance if bits == 0 else variance / (4 ** bits)
274	
275	# RABA:
276	if restoration_weights is not None:
277	    # weighted_variance = sum of (1 - p_r(t)) * lambda_i for tokens in group
278	    # 但注意: DP 是 per-component 的, p_r(t) 是 per-token 的
279	    # 这里需要将 per-token weights 聚合为 per-component weight
280	    weight = restoration_weights[idx - 1]  # 预计算的 weighted variance
281	    error = weight if bits == 0 else weight / (4 ** bits)
282	else:
283	    error = variance if bits == 0 else variance / (4 ** bits)
284	```
285	
286	**关键设计问题**: DP 是 per-PCA-component 的, 但 `p_r(t)` 是 per-token 的。需要决定聚合方式:
287	
288	- **方案 A (per-token DP)**: 将 DP 扩展为 per-token × per-component, 复杂度 O(T × d × B × 16), 对长序列不可行
289	- **方案 B (aggregate then DP)**: 将 weighted variance 预计算为 `weighted_λ_i = Σ_t (1 - p_r(t)) × pca_coeffs[t, i]²`, 替换 eigenvalue 输入 DP. 复杂度不变. **推荐方案**
290	- **方案 C (per-token bit allocation)**: 对每个 token 独立运行 DP (根据其 p_r), 复杂度 O(T × d × B × 16), 但 bit widths 变为 per-token, bit packing 变复杂
291	
292	**推荐方案 B 的实现**:
293	
294	```python
295	def compute_restoration_weighted_eigenvalues(
296	    pca_coeffs: torch.Tensor,      # [num_tokens, dim]
297	    restoration_probs: torch.Tensor, # [num_tokens]
298	) -> torch.Tensor:
299	    """计算 RABA weighted eigenvalues.
300	    
301	    weighted_λ_i = mean_t[(1 - p_r(t)) × pca_coeffs[t, i]²]
302	    """
303	    weights = (1 - restoration_probs).unsqueeze(1)  # [T, 1]
304	    weighted_var = (weights * pca_coeffs ** 2).mean(dim=0)  # [dim]
305	    return weighted_var
306	```
307	
308	然后将 `weighted_eigenvalues` 传入 `dp_bit_allocation` 替代原始 `eigenvalues`。
309	
310	#### 修改 2: `src/gpu_ops.py` — `greedy_bit_allocation()`
311	
312	**当前签名** (line 10):
313	```python
314	def greedy_bit_allocation(eigenvalues, bit_budget, max_bits=16):
315	```
316	
317	**RABA 修改**: 与精确 DP 类似, 传入 weighted eigenvalues 即可, gain 计算自动适配:
318	```python
319	gains_matrix = ev.unsqueeze(1) * 3.0 / (4.0 ** bit_levels.unsqueeze(0))
320	```
321	这里 `ev` 替换为 `weighted_ev` 即可。无需改内部逻辑。
322	
323	#### 修改 3: `src/pipeline.py` 和 `src/pipeline_fast.py` — `compress()`
324	
325	需要在 compress 方法中:
326	1. 新增 `restoration_probs` 参数 (per-token 概率向量)
327	2. 压缩前计算 `pca_coeffs`
328	3. 调用 `compute_restoration_weighted_eigenvalues` 得到 weighted eigenvalues
329	4. 将 weighted eigenvalues 传入 bit allocation
330	
331	**`pipeline.py` 修改** (line 23):
332	```python
333	def compress(self, kv_cache, positions, restoration_probs=None):
334	```
335	
336	在 line 68 附近, PCA transform 之后:
337	```python
338	pca_values = pca_transform(centered, entry.eigenvectors.to(rows.device))
339	
340	# RABA: 如果提供了 restoration_probs, 用 weighted eigenvalues
341	if restoration_probs is not None:
342	    # restoration_probs shape: [middle_len]
343	    # rows shape: [middle_len * group_heads, dim]
344	    # 需要 expand p_r 到 group_heads
345	    pr_expanded = restoration_probs.repeat_interleave(group_heads)
346	    weighted_ev = compute_restoration_weighted_eigenvalues(pca_values, pr_expanded)
347	    bit_widths = dp_bit_allocation(weighted_ev, entry.bit_budget, group_size=1)
348	else:
349	    bit_widths = dp_bit_allocation(entry.eigenvalues.to(rows.device), entry.bit_budget, group_size=1)
350	```
351	
352	**`pipeline_fast.py` 修改** (line 37): 同理, 但用 `greedy_bit_allocation`。
353	
354	#### 修改 4: `src/calibrate.py` — 可选
355	
356	Calibration 阶段不需要 RABA (p_r 在推理时才知道)。但可以在 calibration 时额外存储 PCA coefficient 统计, 以加速运行时的 weighted eigenvalue 计算。
357	
358	### 5.3 额外传入参数
359	
360	- `restoration_probs: torch.Tensor` — shape `[middle_len]`, 值域 [0, 1]
361	  - p_r(t) = 0: token t 不会被恢复, 正常压缩
362	  - p_r(t) = 1: token t 必定被恢复, 可分配 0 bits (极端情况)
363	  - p_r(t) ∈ (0, 1): 按概率加权降低该 token 的 error 权重
364	
365	### 5.4 修改复杂度评估
366	
367	| 文件 | 函数 | 改动行数 | 难度 |
368	|------|------|---------|------|
369	| `quantize.py` | `dp_bit_allocation` | ~10 行 (新增 weighted_ev 路径) | 低 |
370	| `gpu_ops.py` | `greedy_bit_allocation` | ~5 行 (传入 weighted_ev) | 低 |
371	| `pipeline.py` | `compress` | ~15 行 (参数 + weighted_ev 计算) | 低 |
372	| `pipeline_fast.py` | `compress` | ~15 行 (同上) | 低 |
373	| 新增 | `compute_restoration_weighted_eigenvalues` | ~10 行 | 低 |
374	| `common.py` | 数据结构 | 0 行 (不需要改) | — |
375	| `entropy.py` | — | 0 行 | — |
376	
377	**总改动: ~55 行代码**, 主要集中在 bit allocation 调用处。不影响量化/编码/解码逻辑。
378	
379	### 5.5 代码 Diff 草稿
380	
381	```diff
382	--- a/src/quantize.py
383	+++ b/src/quantize.py
384	@@ -1,5 +1,6 @@
385	 """Quantization utilities for KVTC."""
386	 
387	+from __future__ import annotations
388	 from typing import List
389	 import torch
390	 from .common import QuantizationParams
391	@@ -12,6 +13,20 @@
392	     return [eigenvalues[i : i + group_size] for i in range(0, eigenvalues.numel(), group_size)]
393	 
394	 
395	+def compute_restoration_weighted_eigenvalues(
396	+    pca_coeffs: torch.Tensor,
397	+    restoration_probs: torch.Tensor,
398	+) -> torch.Tensor:
399	+    """Compute RABA weighted eigenvalues.
400	+    
401	+    weighted_lambda_i = mean_t[(1 - p_r(t)) * pca_coeffs[t, i]^2]
402	+    """
403	+    weights = (1 - restoration_probs).unsqueeze(1)  # [T, 1]
404	+    weighted_var = (weights * pca_coeffs ** 2).mean(dim=0)  # [dim]
405	+    return weighted_var
406	+
407	+
408	 def dp_bit_allocation(
409	     eigenvalues: torch.Tensor,
410	     bit_budget: int,
411	```
412	
413	```diff
414	--- a/src/pipeline_fast.py
415	+++ b/src/pipeline_fast.py
416	@@ -37,7 +37,7 @@
417	-    def compress(self, kv_cache, positions):
418	+    def compress(self, kv_cache, positions, restoration_probs=None):
419	         # ... (unchanged until after PCA transform) ...
420	 
421	                         pca_values = pca_transform(centered, ev)
422	 
423	+                        # RABA: use weighted eigenvalues if restoration probs provided
424	+                        if restoration_probs is not None:
425	+                            pr = restoration_probs.to(pca_values.device)
426	+                            pr_expanded = pr.repeat_interleave(group_heads)
427	+                            weighted_ev = compute_restoration_weighted_eigenvalues(
428	+                                pca_values, pr_expanded
429	+                            )
430	+                            bit_widths = greedy_bit_allocation(weighted_ev, entry.bit_budget)
431	+                        else:
432	-                        bit_widths = greedy_bit_allocation(
433	-                            entry.eigenvalues.to(rows.device), entry.bit_budget,
434	-                        )
435	+                            bit_widths = greedy_bit_allocation(
436	+                                entry.eigenvalues.to(rows.device), entry.bit_budget,
437	+                            )
438	```
439	
440	### 5.6 不影响的模块
441	
442	- **PCA transform/inverse**: 不受影响, 仍用相同 eigenvectors
443	- **Quantization**: 不受影响, 仍用 uniform affine quantization
444	- **Entropy coding**: 不受影响, 仍对量化后的 bytes 做压缩
445	- **RoPE**: 不受影响
446	- **Token protection** (sink/window): 不受影响
447	- **Decompression**: 不受影响, metadata 中已存储 bit_widths
448	
449	---
450	
451	## 6. 压缩比评估
452	
453	### 6.1 Benchmark 数据 (RTX 5090, Qwen2.5-7B)
454	
455	| Config | K bits | V bits | 压缩比 | K Cosine | V Cosine | 质量 |
456	|--------|--------|--------|:------:|:--------:|:--------:|------|
457	| K1V2-FULL | 1 | 2 | **12.8x** | 0.9925 | 0.9120 | 低 |
458	| K1V3-FULL | 1 | 3 | **8.9x** | 0.9925 | 0.9874 | 可用 |
459	| K1V4-FULL | 1 | 4 | **7.1x** | 0.9925 | 0.9974 | 优 |
460	| K2V3-FULL | 2 | 3 | **7.2x** | 0.9970 | 0.9874 | 可用 |
461	| K2V4-FULL | 2 | 4 | **5.9x** | 0.9970 | 0.9974 | 优 |
462	| K3V4-FULL | 3 | 4 | **5.0x** | 0.9993 | 0.9974 | 优 |
463	
464	### 6.2 8x 压缩比可达性评估
465	
466	**K1V3 配置达到 8.9x**, cosine similarity 0.987-0.993, 质量为 "Good"。
467	
468	**RABA 对 8x 目标的影响**:
469	- RABA 会让部分 token 分配更少 bits (高 p_r tokens) → 平均 bits 降低 → 压缩比提升
470	- 但总 bit budget 不变, 只是重分配: 高 p_r tokens 少分, 低 p_r tokens 多分
471	- 净效应: 如果大量 tokens 有高 p_r, 可以用更少的 bit budget 达到相同重建质量 → **提升有效压缩比**
472	- 在 K2V4 基础上 + RABA (假设 50% tokens 有 p_r > 0.5), 有效压缩比可达 7-9x 同时保持更高质量
473	
474	**结论**: 8x 在 KVTC 可达范围内。K1V3 直接达到 8.9x, K2V4 + RABA 可在保持更高质量的同时逼近 8x。
475	
476	### 6.3 Benchmark 脚本
477	
478	```bash
479	# 完整 benchmark
480	python benchmarks/benchmark_v4.py --model Qwen/Qwen2.5-7B-Instruct --device cuda
481	
482	# 指定配置
483	python benchmarks/benchmark_v3.py --model meta-llama/Llama-3.1-8B-Instruct --device cuda
484	
485	# 单元测试 (无需 GPU)
486	pytest src/test_kvtc.py -v
487	```
488	
489	---
490	
491	## 7. Entropy Coding 流程
492	
493	### 7.1 编码方法
494	
495	三种编码器, triple-mode picker 选最小:
496	
497	| 编码器 | 文件 | 说明 |
498	|--------|------|------|
499	| **zlib (DEFLATE)** | `entropy.py` | 默认, 压缩 level 6-9 |
500	| **LZMA2** | `ans_entropy.py:compress_best()` | Python `lzma` module |
501	| **rANS** | `ans_entropy.py:rans_encode()` | 纯 Python 实现, 16-bit precision |
502	
503	Triple picker (`ans_entropy.py:184-230`):
504	```python
505	def compress_best(packed_bytes, level=6):
506	    candidates = []
507	    candidates.append((b"Z" + zlib.compress(packed_bytes, 9), "zlib"))
508	    candidates.append((b"L" + lzma.compress(packed_bytes, preset=6), "lzma"))
509	    candidates.append((b"A" + rans_encode(packed_bytes), "rans"))
510	    best = min(candidates, key=lambda x: len(x[0]))
511	    return best[0], ratio
512	```
513	
514	1-byte tag 前缀标识编码器: `Z`=zlib, `L`=LZMA, `A`=rANS.
515	
516	### 7.2 编解码 API
517	
518	**编码**:
519	```python
520	from src.entropy import pack_bits, compress
521	from src.ans_entropy import compress_best
522	
523	# Step 1: 将量化 indices 打包为 bytes
524	packed = pack_bits(indices_list, bit_widths)
525	
526	# Step 2a: zlib 压缩
527	compressed, ratio = compress(packed, level=6)
528	
529	# Step 2b: 或用 triple picker
530	compressed, ratio = compress_best(packed, level=6)
531	```
532	
533	**解码**:
534	```python
535	from src.entropy import decompress, unpack_bits
536	from src.ans_entropy import decompress_best
537	
538	# Step 1: 解压
539	packed = decompress(compressed, original_size)
540	# 或 triple picker
541	packed = decompress_best(compressed, original_size)
542	
543	# Step 2: 解包
544	indices_list = unpack_bits(packed, bit_widths, lengths)
545	```
546	
547	### 7.3 Bit Packing
548	
549	`entropy.py:47-83`: 按 component 顺序逐个打包 (comp 0 所有 rows, 然后 comp 1, ...), 变宽 bit stream, 无对齐要求。
550	
551	GPU 加速版在 `gpu_ops.py:fast_pack_bits()` 和 `triton_kernels.py:gpu_pack_variable_width()`。
552	
553	---
554	
555	## 8. Adaptive Budget (per-layer)
556	
557	### 8.1 原理
558	
559	`adaptive_budget.py`: 不同 layer 的 PCA eigenvalue spectrum "平坦度"不同:
560	- 平坦 (high Shannon entropy) → 难压缩 → 分配更多 bits
561	- 陡峭 (low entropy) → 易压缩 → 分配更少 bits
562	
563	总预算守恒, 只做重分配。
564	
565	### 8.2 API
566	
567	```python
568	from src.adaptive_budget import apply_adaptive_budgets
569	
570	key_diff, val_diff = apply_adaptive_budgets(
571	    calibration, key_bits_avg=2, value_bits_avg=4, strength=1.0
572	)
573	```
574	
575	`strength=0` 为均匀分配, `strength=1` 为完全自适应。
576	
577	---
578	
579	## 9. 集成风险和注意事项
580	
581	### 9.1 RABA 集成风险
582	
583	| 风险 | 说明 | 缓解 |
584	|------|------|------|
585	| **DP 粒度不匹配** | DP 是 per-component, p_r 是 per-token | 用方案 B: 预聚合 weighted eigenvalues |
586	| **p_r 精度要求** | p_r 误估可能导致分配不当 | 加 clamp(0.01, 0.99) 防极端值 |
587	| **与 adaptive budget 交互** | RABA 和 adaptive budget 都改 bit allocation | 两者正交: adaptive 改 per-layer budget, RABA 改 per-component allocation |
588	| **解压不需要 p_r** | metadata 中已存 bit_widths | 正确, 解压路径零改动 |
589	| **Calibration 兼容** | RABA 修改运行时 bit allocation, 不改 calibration | 完全兼容, 无需重新 calibrate |
590	
591	### 9.2 性能影响
592	
593	- 压缩时增加 `weighted_eigenvalue` 计算: 一次矩阵乘 `O(T × d)`, 可忽略
594	- Bit allocation (贪心版) 运行时间不变
595	- 解压路径零开销
596	
597	### 9.3 代码质量观察
598	
599	- 代码组织清晰, pipeline → pca → quantize → entropy 模块化良好
600	- 两个 pipeline (参考 + GPU) 保持接口一致, 修改一个的经验可直接复用
601	- 38 个测试覆盖所有核心功能, 添加 RABA 后应增加对应测试
602	- `group_size=1` 默认设置意味着 per-head PCA, 对 RABA 的 per-token weight 聚合较友好
603	
604	### 9.4 推荐实施顺序
605	
606	1. 在 `quantize.py` 新增 `compute_restoration_weighted_eigenvalues()` 函数
607	2. 修改 `pipeline.py` (参考版) 的 `compress()` 方法, 添加 RABA 支持
608	3. 编写单元测试: weighted eigenvalues 计算正确性, RABA bit allocation 向后兼容 (p_r=0 时等价原版)
609	4. 验证: p_r=0 应产生与原版完全相同的 bit allocation
610	5. 修改 `pipeline_fast.py` (GPU 版)
611	6. 端到端测试: 带 RABA 的压缩-解压 roundtrip
612	
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01AxWdWziX2UN5if8HFGfTaN",
  "session_id": "fdf71b47-8f0f-4233-b6c0-f01ae22a3454",
  "uuid": "bd373ff5-4bb4-44b8-8779-ed18fd3e3272"
}
```

</details>

---

### System

_source line 17_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac52294b4d40fe0d9",
  "tool_use_id": "toolu_016cLANJVDSeHpFC5Ng7XfBw",
  "description": "Reading artifacts/mepic_survey.md",
  "usage": {
    "total_tokens": 18459,
    "tool_uses": 1,
    "duration_ms": 1151
  },
  "last_tool_name": "Read",
  "uuid": "f76a2c18-6ef0-4a44-8fd0-32418b64f5e5",
  "session_id": "fdf71b47-8f0f-4233-b6c0-f01ae22a3454"
}
```

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — Read · `toolu_01ANVRb2TCFq67VNV1U6cfn7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/distill_kv_rag_cache/artifacts/mepic_survey.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016cLANJVDSeHpFC5Ng7XfBw",
  "session_id": "fdf71b47-8f0f-4233-b6c0-f01ae22a3454",
  "uuid": "f38facc0-48fc-4e3d-a169-1dffdafeed2d",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018CQCugwPsNP8QfA9ETFspH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 516,
      "cache_read_input_tokens": 17934,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 516,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 19 · 2026-05-14T05:13:51.860Z_

<details><summary>↩ Tool result · `toolu_01ANVRb2TCFq67VNV1U6cfn7`</summary>

````text
1	# MEPIC 技术调研报告
2	
3	## 1. 概述
4	
5	**MEPIC** (Memory-Efficient Position-Independent Caching) 是一种面向 LLM serving 的 KV cache 复用系统，核心思想是将 KV cache 以 **NoPE (No Positional Encoding)** 格式存储，在 attention 计算时通过 fused kernel 动态注入 RoPE，从而实现 chunk-level KV 在不同位置、不同请求、不同 batch 间的无损复用。
6	
7	- **论文**: [arXiv:2512.16822](https://arxiv.org/abs/2512.16822) (2025.12)
8	- **作者**: Qian Wang, Zahra Yousefijamarani, Morgan Lindsay Heisler, Rongzhi Gu 等
9	- **代码**: **未开源**。论文基于 vLLM + LMCache 实现，但无公开仓库。
10	- **前身**: [EPIC](https://arxiv.org/abs/2410.15332) (ICML 2025)，代码开源于 [GitHub](https://github.com/DerekHJH/epic)（vLLM 0.7.0 fork）
11	
12	### 1.1 相关工作谱系
13	
14	| 系统 | 核心策略 | RoPE 处理 | 复用粒度 | 代码 |
15	|------|---------|-----------|---------|------|
16	| **CacheBlend** (EuroSys'25) | 比较 ΔK 选 15% token 重算 | 标准 post-RoPE 存储 | Token-level | ✗ |
17	| **EPIC** (ICML'25) | LegoLink: 重算每 chunk 前 k 个 token | 标准 post-RoPE 存储 | Token-level | [✓](https://github.com/DerekHJH/epic) |
18	| **MEPIC** (2025.12) | NoPE 存储 + fused RoPE attention | **NoPE: 去除 RoPE** | Block-level | ✗ |
19	| **KV Packet** (2026.04) | Soft-token adapter 包裹 chunk | 无需修改 RoPE | Chunk-level | ✗ |
20	
21	---
22	
23	## 2. 核心技术机制
24	
25	### 2.1 NoPE KV 存储
26	
27	**标准流程** (HuggingFace transformers / vLLM):
28	```
29	Q, K, V = proj(hidden_states)
30	Q_rope, K_rope = apply_rotary_pos_emb(Q, K, cos, sin)  # RoPE 嵌入位置信息
31	cache.update(K_rope, V)  # 存储 post-RoPE 的 K
32	attn = softmax(Q_rope @ K_rope^T / sqrt(d)) @ V
33	```
34	
35	**MEPIC NoPE 流程**:
36	```
37	Q, K, V = proj(hidden_states)
38	Q_rope = apply_rotary_pos_emb(Q, cos, sin)  # 仅 Q 应用 RoPE
39	cache.update(K, V)  # 存储 pre-RoPE 的 K（NoPE 格式）
40	# attention 计算时在 fused kernel 中动态对 K 应用 RoPE
41	attn = fused_rope_attention(Q_rope, K_nope, V, position_offsets)
42	```
43	
44	**关键差异**: KV cache 中的 key 不包含位置信息，因此同一 chunk 的 KV 可在任意位置复用。
45	
46	### 2.2 RoPE 数学基础
47	
48	RoPE 对 d 维向量按 d/2 对逐对旋转：
49	
50	**正向 (apply)**:
51	```
52	θ_i = 10000^(-2(i-1)/d),  i ∈ [1, d/2]
53	
54	RoPE(x, m) = [x_1·cos(mθ_1) - x_{d/2+1}·sin(mθ_1),
55	               x_2·cos(mθ_2) - x_{d/2+2}·sin(mθ_2),
56	               ...,
57	               x_{d/2+1}·cos(mθ_1) + x_1·sin(mθ_1),
58	               ...]
59	```
60	
61	HuggingFace 实现:
62	```python
63	def rotate_half(x):
64	    x1 = x[..., :x.shape[-1] // 2]
65	    x2 = x[..., x.shape[-1] // 2:]
66	    return torch.cat((-x2, x1), dim=-1)
67	
68	def apply_rotary_pos_emb(q, k, cos, sin):
69	    q_embed = (q * cos) + (rotate_half(q) * sin)
70	    k_embed = (k * cos) + (rotate_half(k) * sin)
71	    return q_embed, k_embed
72	```
73	
74	**逆向 (remove/undo)**:
75	旋转矩阵的逆就是转置（等价于用 -θ 旋转）：
76	```python
77	def remove_rotary_pos_emb(k_rope, cos, sin):
78	    """从 post-RoPE key 恢复 pre-RoPE key"""
79	    k_nope = (k_rope * cos) + (rotate_half(k_rope) * (-sin))
80	    return k_nope
81	    # 等价于: k_nope = (k_rope * cos) - (rotate_half(k_rope) * sin)
82	```
83	
84	**Attention score 不变性**:
85	```
86	⟨RoPE(q, m), RoPE(k, n)⟩ = ⟨RoPE(q, m-n), k⟩
87	```
88	即：如果 key 未应用 RoPE，只需在 query 上应用相对位置 (m-n) 的旋转即可得到正确的 attention score。这是 MEPIC NoPE 方案的数学基础。
89	
90	### 2.3 Fused RoPE-Attention Kernel
91	
92	MEPIC 将 RoPE 应用融合到 attention kernel 中：
93	
94	```
95	// Pseudocode for fused kernel
96	for each query token at position m:
97	    for each key block at position range [n_start, n_end]:
98	        // 从 HBM 加载 NoPE key block
99	        K_nope = load_from_hbm(block_id)
100	        // 在 SRAM 中动态应用 RoPE offset
101	        for each key at position n in [n_start, n_end]:
102	            K_rope[n] = apply_rope(K_nope[n], cos[n], sin[n])
103	        // 计算 attention score
104	        score = Q_rope[m] @ K_rope^T / sqrt(d)
105	```
106	
107	vLLM 已有 `rope_kvcache_fusion` 编译 pass，将 RoPE 和 KV cache 写入操作融合为单一 kernel。MEPIC 在此基础上进一步将 RoPE 推迟到 attention 计算阶段。
108	
109	### 2.4 Block 对齐与 Padding
110	
111	MEPIC 使用 **非对称 padding** 确保每个 chunk 的起始对齐到 KV page boundary：
112	
113	| 段类型 | Padding 方式 | 原因 |
114	|--------|-------------|------|
115	| Chunk 段 | **前导 padding** (leading) | 确保 chunk 起始对齐到 block 边界 |
116	| Prompt 段 | **尾部 padding** (trailing) | 填充到 block 边界 |
117	| 最后一个 Prompt 段 | 无 padding | 避免浪费 |
118	
119	Padding pattern 还隐式编码了段类型，计算路径无需额外 metadata 即可区分 chunk 和 prompt。
120	
121	**示例**: Block size = 16 tokens
122	```
123	[pad pad pad chunk_token_1 ... chunk_token_16] [chunk_token_17 ... chunk_token_32] ...
124	     leading padding           block 1 (first block)        block 2 (canonical, shareable)
125	```
126	
127	### 2.5 First-Block Recomputation
128	
129	这是 MEPIC 最关键的设计之一：
130	
131	**规则**: 对于每个 cached chunk，仅重新计算其**第一个 KV block**，其余 block 直接复用 canonical KV。
132	
133	**原因**:
134	1. Chunk 第一个 block 包含与前文（其他 chunk 或 prompt）的 cross-attention 边界效应
135	2. 后续 block 的 KV 主要取决于 chunk 内部上下文，位置无关
136	3. 重算一个 block（通常 16 tokens）的开销远小于重算整个 chunk
137	
138	**实现**:
139	- 第一个 block: 通过 vLLM prefix cache 分配和重算（request-specific）
140	- 后续 block: 通过 chunk cache 管理（canonical, shared across requests）
141	
142	**与 EPIC LegoLink 的对比**:
143	| | EPIC LegoLink | MEPIC First-Block |
144	|---|---|---|
145	| 重算粒度 | Token-level (前 k 个 token) | Block-level (第一个 block) |
146	| 选择策略 | 静态: k ≤ 32 | 固定: 1 个 block |
147	| 复杂度 | O(kN) | O(B) where B = block_size |
148	| 存储格式 | Post-RoPE | NoPE |
149	
150	### 2.6 Scheduling Path (Algorithm 1)
151	
152	```
153	Input:  Request tokens T with segment markers
154	Output: Padded tokens T_align + paged KV block mapping, or Reject
155	
156	1. Segmentation: 根据 markers 将 T 分为 {S_1, ..., S_m}
157	2. Canonicalization: 
158	   - 确定每段类型 (chunk / prompt)
159	   - 对每段应用 padding 实现 block 对齐
160	   - 构造 T_align
161	3. Residency Resolution:
162	   - 对每段检查 HBM 驻留状态
163	   - Hash chunk 的 padded token 序列确定身份
164	4. Admission Check:
165	   - 估算非驻留段需要的 KV blocks
166	   - 若不够且无法通过 LRU 回收 → Reject
167	5. KV Block Allocation:
168	   - 按驻留/类型分配 paged KV blocks
169	   - Return T_align + block mapping
170	```
171	
172	### 2.7 系统架构
173	
174	MEPIC 扩展 vLLM 的 paged KV 管理：
175	
176	```
177	┌─ Scheduling Path ─────────────────────────────────┐
178	│  Chunk Processor → Chunk Matcher → Hybrid KV Mgr  │
179	│  (segmentation/    (residency     (prefix/chunk    │
180	│   canonicalization) resolution)    coordination)   │
181	│                                  + Chunk LRU Mgr   │
182	└────────────────────────────────────────────────────┘
183	                          │
184	                          ▼
185	┌─ Computation Path ────────────────────────────────┐
186	│  Selective Recomputation → Fused-RoPE Attention    │
187	│  (first block only)       (NoPE → RoPE on-the-fly) │
188	└────────────────────────────────────────────────────┘
189	```
190	
191	---
192	
193	## 3. 性能评估
194	
195	### 3.1 HBM 节省
196	
197	| 对比基线 | HBM 节省倍数 | 条件 |
198	|---------|-------------|------|
199	| CacheBlend | 2× | 常规场景 |
200	| EPIC | 2× | 常规场景 |
201	| CacheBlend | 5.74× | 高 QPS |
202	| EPIC | 5.25× | 高 QPS |
203	| 长 prompt | 5× | 长上下文 |
204	
205	### 3.2 延迟
206	
207	- 比 EPIC 低 9.1%
208	- 比 CacheBlend 低 11.48%
209	
210	### 3.3 精度
211	
212	在 SQuAD, NewsQA, NarrativeQA, emrQA 上 F1/Rouge-L 与 baseline 持平或略优。
213	
214	### 3.4 Recomputation 开销
215	
216	各数据集平均每个 request 需重算 29-521 tokens。
217	
218	---
219	
220	## 4. EPIC 代码分析（可参考实现）
221	
222	EPIC 是 MEPIC 的前身，有开源代码 ([GitHub](https://github.com/DerekHJH/epic))，基于 vLLM 0.7.0 fork，约 2K 行 Python。
223	
224	### 4.1 核心模块
225	
226	| 模块 | 功能 |
227	|------|------|
228	| **KVGen** | 为静态 chunk 预生成 KV cache |
229	| **KVStore** | 管理 KV cache 存储 (HBM/DRAM/filesystem) |
230	| **KVLink** | 检索、拼接 KV cache，执行 LegoLink 选择性重算 |
231	| **KVSplit** | 可选的语义切分模块 |
232	
233	### 4.2 关键修改点
234	
235	1. **Attention backend**: 支持 masked attention across scattered positions
236	2. **Memory management**: 扩展至 DRAM/filesystem
237	3. **Scheduler**: 管理 cache 生命周期 (create/expire)
238	
239	### 4.3 LegoLink 重算流程
240	
241	```python
242	# Pseudocode
243	for each chunk (except first):
244	    # 取前 k 个 token 的 embedding
245	    embeds = get_embeddings(chunk[:k])
246	    Q, K, V = project(embeds)
247	    # 拼接已缓存的 KV
248	    K_expanded = concat(cached_KV, K)
249	    # 带 mask 的 attention (causal + chunk boundary)
250	    attn = masked_attention(Q, K_expanded, mask)
251	    # 更新这 k 个 token 的 KV cache
252	    update_cache(chunk[:k], new_KV)
253	```
254	
255	---
256	
257	## 5. 为 CompressLink 实现 MEPIC 的设计方案
258	
259	### 5.1 实现策略选择
260	
261	鉴于 MEPIC 没有开源代码，且其实现依赖 vLLM 的 paged attention 和自定义 CUDA kernel，**不建议直接复刻 MEPIC 的 serving 系统**。
262	
263	对于 CompressLink，我们需要的是 MEPIC 的**核心算法组件**（NoPE KV + RoPE-on-query），而非其 serving 框架。建议基于 HuggingFace transformers 实现 functional MEPIC。
264	
265	### 5.2 需要 Hook/修改的模块
266	
267	#### (1) `apply_rotary_pos_emb` — 分离 Q/K 的 RoPE
268	
269	**文件**: `transformers/models/llama/modeling_llama.py` (或目标模型)
270	
271	**当前代码** (~L95):
272	```python
273	cos, sin = position_embeddings
274	query_states, key_states = apply_rotary_pos_emb(query_states, key_states, cos, sin)
275	```
276	
277	**修改方案**: 仅对 query 应用 RoPE，key 保持 NoPE
278	```python
279	cos, sin = position_embeddings
280	if use_nope_kv:
281	    query_states = apply_rotary_pos_emb_query_only(query_states, cos, sin)
282	    # key_states 保持原样 (NoPE)
283	else:
284	    query_states, key_states = apply_rotary_pos_emb(query_states, key_states, cos, sin)
285	```
286	
287	#### (2) KV Cache 更新 — 存储 NoPE keys
288	
289	**当前代码**:
290	```python
291	# RoPE 已应用后才存入 cache
292	key_states, value_states = past_key_values.update(key_states, value_states, self.layer_idx)
293	```
294	
295	**修改**: NoPE 模式下，存入 cache 的 key 不含 RoPE。无需修改 cache.update 本身，因为 key_states 已经是 NoPE 的。
296	
297	#### (3) Attention 计算 — 动态 RoPE
298	
299	**修改方案**: 从 cache 取出 NoPE keys 后，在 attention 前动态施加 RoPE
300	
301	```python
302	def nope_attention(query_states, key_states, value_states, cos_full, sin_full):
303	    """
304	    query_states: 已应用 RoPE 的 Q [B, H, L_q, D]
305	    key_states:   NoPE 格式的 K [B, H, L_kv, D]  (从 cache 取出)
306	    cos_full/sin_full: 所有 key 位置对应的 cos/sin
307	    """
308	    # 对 NoPE keys 动态施加 RoPE
309	    key_states_rope = apply_rotary_pos_emb_key_only(key_states, cos_full, sin_full)
310	    # 标准 attention
311	    attn_weights = torch.matmul(query_states, key_states_rope.transpose(-2, -1)) / math.sqrt(d)
312	    attn_weights = F.softmax(attn_weights, dim=-1)
313	    attn_output = torch.matmul(attn_weights, value_states)
314	    return attn_output
315	```
316	
317	#### (4) 辅助函数
318	
319	```python
320	def apply_rotary_pos_emb_query_only(q, cos, sin):
321	    """仅对 query 应用 RoPE"""
322	    return (q * cos) + (rotate_half(q) * sin)
323	
324	def apply_rotary_pos_emb_key_only(k, cos, sin):
325	    """对 NoPE key 施加指定位置的 RoPE"""
326	    return (k * cos) + (rotate_half(k) * sin)
327	
328	def remove_rotary_pos_emb(k_rope, cos, sin):
329	    """从 post-RoPE key 恢复 NoPE key (用于转换已有 cache)"""
330	    return (k_rope * cos) - (rotate_half(k_rope) * sin)
331	```
332	
333	### 5.3 Boundary Recomputation 实现
334	
335	```python
336	class BoundaryRecomputer:
337	    def __init__(self, model, block_size=16):
338	        self.model = model
339	        self.block_size = block_size
340	    
341	    def recompute_first_block(self, chunk_kv, prefix_hidden_states, chunk_tokens):
342	        """
343	        重算 chunk 第一个 block 的 KV。
344	        
345	        Args:
346	            chunk_kv: cached NoPE KV for the full chunk
347	            prefix_hidden_states: 前文的 hidden states (用于 cross attention)
348	            chunk_tokens: chunk 的 token ids
349	        
350	        Returns:
351	            updated chunk_kv with recomputed first block
352	        """
353	        first_block_tokens = chunk_tokens[:self.block_size]
354	        # 将前文 + 第一个 block 一起前向传播
355	        combined_input = concat(prefix_hidden_states, first_block_tokens)
356	        new_kv = self.model.forward_partial(combined_input)
357	        # 替换第一个 block 的 KV
358	        chunk_kv[:, :, :self.block_size, :] = new_kv[:, :, -self.block_size:, :]
359	        return chunk_kv
360	```
361	
362	### 5.4 预估代码量与难度
363	
364	| 组件 | 代码量 | 难度 | 说明 |
365	|------|--------|------|------|
366	| NoPE KV 存储 (Q-only RoPE) | ~50 行 | 低 | 修改 attention forward |
367	| 动态 RoPE attention | ~80 行 | 中 | 需处理 position_ids mapping |
368	| Boundary recomputation | ~150 行 | 中 | 需 partial forward 支持 |
369	| RoPE remove/restore 工具函数 | ~30 行 | 低 | 纯数学操作 |
370	| Chunk 管理 (segmentation/padding) | ~200 行 | 中 | 对齐逻辑 |
371	| 测试与验证 | ~200 行 | 低 | 正确性验证 |
372	| **总计** | **~710 行** | **中** | |
373	
374	---
375	
376	## 6. 与 KVTC 的兼容性分析
377	
378	### 6.1 共同基础: RoPE-Free Keys
379	
380	**KVTC** 和 **MEPIC** 都依赖 RoPE-free keys：
381	
382	| | KVTC | MEPIC |
383	|---|---|---|
384	| 为何去除 RoPE | RoPE 掩盖了 key 的低秩结构，影响 PCA 压缩率 | 使 KV 位置无关，支持 chunk 复用 |
385	| 去除时机 | 压缩前 remove，解压后 re-apply | 存储时不 apply，attention 时 apply |
386	| 数学操作 | `k_nope = (k_rope * cos) - (rotate_half(k_rope) * sin)` | 直接不应用 RoPE |
387	
388	**兼容性结论**: 两者天然互补。
389	- MEPIC 生成的 NoPE KV 可以直接送入 KVTC 的 PCA 压缩流程（无需额外 remove RoPE 步骤）
390	- KVTC 解压后的 NoPE KV 可以直接用 MEPIC 的 fused RoPE attention 消费
391	
392	### 6.2 CompressLink 集成方案
393	
394	```
395	Chunk Input → NoPE KV 生成 (MEPIC) → KVTC 压缩 → 存储
396	                                                      ↓
397	Query 到达 → KVTC 解压 → First-Block Recomputation → Fused RoPE Attention → Output
398	```
399	
400	---
401	
402	## 7. 与 CEGR (Compression-Error-Guided Restoration) 的关系
403	
404	### 7.1 机制对比
405	
406	| | MEPIC First-Block Recomputation | CEGR |
407	|---|---|---|
408	| 触发条件 | 固定: 每个 cached chunk 的第一个 block | 动态: 基于压缩误差阈值 |
409	| 选择策略 | 位置固定 (block boundary) | 误差驱动 (高误差 token) |
410	| 计算开销 | 低且可预测 (1 block per chunk) | 可变 (取决于压缩质量) |
411	| 适用场景 | Chunk-level KV 复用 | KV 压缩后的质量恢复 |
412	
413	### 7.2 互补性
414	
415	- MEPIC 的 first-block recomputation 处理的是 **chunk 拼接边界** 的上下文断裂问题
416	- CEGR 处理的是 **压缩损失** 导致的 KV 精度退化问题
417	- 两者解决不同层面的问题，可以叠加使用
418	
419	**建议**: 在 CompressLink 中，先用 MEPIC 做 boundary recomputation（修复拼接误差），再用 CEGR 做 compression error restoration（修复压缩误差）。
420	
421	---
422	
423	## 8. 总结与建议
424	
425	### 8.1 关键发现
426	
427	1. **MEPIC 未开源**，但核心算法（NoPE KV + fused RoPE attention）可从论文中完整复现
428	2. **EPIC 有代码**（vLLM fork），但采用不同技术路线（post-RoPE + token-level recomputation），参考价值有限
429	3. **NoPE 格式是 KVTC 和 MEPIC 的共同基础**，CompressLink 应以 NoPE 作为核心 KV 表示
430	4. RoPE 的 apply/remove 是简单的旋转操作，实现难度低
431	5. 主要实现挑战在于 **boundary recomputation 的 partial forward** 和 **position_ids 的正确管理**
432	
433	### 8.2 实现优先级建议
434	
435	1. **P0**: NoPE KV 存储 + Q-only RoPE（基础能力，~50 行）
436	2. **P0**: RoPE remove/restore 工具函数（KVTC 集成需要，~30 行）
437	3. **P1**: 动态 RoPE attention（支持从 NoPE cache 消费 KV，~80 行）
438	4. **P1**: Boundary recomputation（chunk 复用时的精度保障，~150 行）
439	5. **P2**: Chunk 管理与 padding 对齐（production-level 特性，~200 行）
440	
441	### 8.3 风险点
442	
443	- **精度验证**: NoPE 存储在数学上等价，但浮点误差累积可能影响长序列结果，需跑 benchmark 验证
444	- **Flash Attention 兼容**: 标准 Flash Attention 不支持在 kernel 内动态 apply RoPE，可能需要退回到 eager attention 或使用自定义 kernel
445	- **Partial forward**: HuggingFace transformers 没有原生的 partial layer forward，boundary recomputation 需要额外工程
446	
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016cLANJVDSeHpFC5Ng7XfBw",
  "session_id": "fdf71b47-8f0f-4233-b6c0-f01ae22a3454",
  "uuid": "810bc9c9-fab5-4623-b961-321daee62f89"
}
```

</details>

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Agent · `toolu_016vF9RQ7AzbFvvXvhj3J5WE`</summary>

```json
{
  "description": "Read ProphetKV survey",
  "subagent_type": "Explore",
  "prompt": "Read the ProphetKV survey file at /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/distill_kv_rag_cache/artifacts/prophetkv_survey.md to understand ProphetKV's query relevance mechanism. Report back: how query relevance is computed, token selection strategy, and any code snippets for the probe mechanism."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fdf71b47-8f0f-4233-b6c0-f01ae22a3454",
  "uuid": "6c6fc5b1-5a84-43c9-b819-50180910d6ed",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018XJLSFkKTjH8XZd1N3TCqn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 489,
      "cache_read_input_tokens": 27003,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 489
      },
      "output_tokens": 45,
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

### System

_source line 21_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a7fb22f008ca138e6",
  "tool_use_id": "toolu_016vF9RQ7AzbFvvXvhj3J5WE",
  "description": "Read ProphetKV survey",
  "task_type": "local_agent",
  "prompt": "Read the ProphetKV survey file at /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/distill_kv_rag_cache/artifacts/prophetkv_survey.md to understand ProphetKV's query relevance mechanism. Report back: how query relevance is computed, token selection strategy, and any code snippets for the probe mechanism.",
  "uuid": "1584a05c-bf84-4302-b2cc-f152de362fb6",
  "session_id": "fdf71b47-8f0f-4233-b6c0-f01ae22a3454"
}
```

---

## Round 3

15 recorded events

### User

_source line 22 · 2026-05-14T05:13:52.634Z_

Read the ProphetKV survey file at /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/distill_kv_rag_cache/artifacts/prophetkv_survey.md to understand ProphetKV's query relevance mechanism. Report back: how query relevance is computed, token selection strategy, and any code snippets for the probe mechanism.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016vF9RQ7AzbFvvXvhj3J5WE",
  "session_id": "fdf71b47-8f0f-4233-b6c0-f01ae22a3454",
  "uuid": "e03c58ce-5988-4e98-b41f-904a306bed46"
}
```

</details>

---

### System

_source line 23_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a7fb22f008ca138e6",
  "tool_use_id": "toolu_016vF9RQ7AzbFvvXvhj3J5WE",
  "description": "Reading artifacts/prophetkv_survey.md",
  "usage": {
    "total_tokens": 18462,
    "tool_uses": 1,
    "duration_ms": 1291
  },
  "last_tool_name": "Read",
  "uuid": "0aba9d0d-de06-4d11-bc21-88ca1cc00b72",
  "session_id": "fdf71b47-8f0f-4233-b6c0-f01ae22a3454"
}
```

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — Read · `toolu_01FMEg35zF6gv7DAYoTTkV3Y`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/distill_kv_rag_cache/artifacts/prophetkv_survey.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_016vF9RQ7AzbFvvXvhj3J5WE",
  "session_id": "fdf71b47-8f0f-4233-b6c0-f01ae22a3454",
  "uuid": "92b504af-b385-4ec5-989f-6d74d4a912fb",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012641sRnQLziRLUvCDZcihC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 509,
      "cache_read_input_tokens": 17934,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 509,
        "ephemeral_1h_input_tokens": 0
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

_source line 25 · 2026-05-14T05:13:54.223Z_

<details><summary>↩ Tool result · `toolu_01FMEg35zF6gv7DAYoTTkV3Y`</summary>

````text
1	# ProphetKV 及 Query-Aware KV Cache 方法调研报告
2	
3	> 论文: arXiv 2602.02579 (Feb 2026)  
4	> 作者: Shihao Wang, Jiahao Chen et al. (HIT Shenzhen, Yanrong Technology)  
5	> 代码: **无公开代码仓库**  
6	> 调研日期: 2026-05-14 (v2 更新)  
7	> 目的: 为 CompressLink 的 query relevance probe (p_r(t)) 提供方法论依据和实现方案
8	
9	---
10	
11	## 快速参考
12	
13	### 方法对比表
14	
15	| 维度 | ProphetKV | SnapKV | kvpress ExpectedAttn |
16	|------|-----------|--------|---------------------|
17	| 核心信号 | query attn column sum, 跨所有层 | observation window attn, per-layer | Gaussian E[attn], per-layer |
18	| 场景 | Chunked prefill 后 KV 修复 | Prefill KV eviction | Prefill KV eviction |
19	| 需要 query? | ✅ | ❌ (用 window proxy) | ❌ (统计预测) |
20	| Score 粒度 | per-layer → fuse to global per-token | per-head per-layer | per-head per-layer |
21	| 计算开销 | O(\|Q\|×s) per layer | O(window×s) per layer | O(s×d) per layer |
22	| 开源代码 | ❌ | ✅ FasterDecoding/SnapKV | ✅ NVIDIA/kvpress |
23	| HF 集成 | — | Monkey-patch | Forward hook (context mgr) |
24	
25	### 核心公式速查
26	
27	```
28	ProphetKV:  α_l(t) = Φ̂'_{Q_s,t}^(l) = (1/|Q|) Σ_q softmax(q·K'/√d)_t
29	            ᾱ(t) = (1/L) Σ_l α_l(t)
30	            T_p = Top-p(ᾱ(t))
31	
32	SnapKV:     scores = AvgPool1d(attn[:,:,-W:,:-W].mean(dim=-2), kernel=5)
33	            keep = TopK(scores, capacity - window)
34	
35	ExpAttn:    E(A)_i = exp(μ_q^T k_i/√d + k_i^T Σ_q k_i/(2d))
36	            score_i = softmax(E(A))_i · (ε + ||v_i||₂)
37	```
38	
39	### 代码量估计
40	
41	| 组件 | 行数 | 依赖 |
42	|------|------|------|
43	| 位置先验 p_r (MVP Phase 0) | ~50 | MEPIC chunk boundaries |
44	| ProphetKV-style query probe (Phase 1) | ~200 | HF attn hook, NoPE KV cache |
45	| RABA DP solver 修改 | ~100 | KVTC DP solver |
46	| CEGR scoring | ~80 | Decompression metadata |
47	| 端到端 pipeline glue | ~150 | 以上全部 |
48	| **总计** | **~580** | |
49	
50	---
51	
52	## 1. ProphetKV 核心方法
53	
54	### 1.1 问题场景
55	
56	ProphetKV 针对 RAG 场景中的 **position-independent KV cache reuse**。典型流程:
57	1. 多个 RAG 文档各自独立预计算 KV cache（chunk-wise precomputation）
58	2. 用户请求时，拼接各 chunk 的 KV cache → **缺失 cross-chunk attention**
59	3. 需要选择性 recompute 部分 token 来恢复关键的 cross-attention
60	
61	**核心洞察**: 现有方法（CacheBlend、EPIC、KVShare）使用全局 saliency 指标选 token，导致 **crowding-out effect** — 全局显著但与用户查询无关的 token 占满 recomputation budget，挤走真正关键的 token。
62	
63	### 1.2 "User Query as a Prophet" — 核心假设
64	
65	**实验发现**: 用户查询 attention 到的 token 子集，与 decoding 阶段被 attend 到的 token 子集有 **高度重叠**（overlap ratio 在 top-p=0.2 时已达 80%+，跨 Llama3-8B、Qwen2.5-14B、Qwen3-14B 均稳健）。
66	
67	→ 用户查询的 attention pattern 可作为 decoding 阶段 token 重要性的 **先知 (prophet)**。
68	
69	### 1.3 数学推导
70	
71	#### 1.3.1 Attention 输出分解
72	
73	对于生成 token n > s（s 为输入长度），attention 输出可分解为:
74	
75	```
76	AttnOut_n = Σ_{1≤t≤s} Φ_{n,t} V_t + Σ_{s&lt;t≤n} Φ_{n,t} V_t
77	            ├── 输入 token 贡献 ──┘   └── 生成 token 贡献 ──┘
78	```
79	
80	#### 1.3.2 Query Attention 作为代理
81	
82	定义 **query token 对 context token t 的平均 attention**:
83	
84	```
85	Φ̂_{Q_s,t} = (1/|Q_s|) Σ_{q∈Q_s} Φ_{q,t}
86	```
87	
88	其中 Q_s 是用户查询 token 集合。核心近似:
89	
90	```
91	Φ_{n,t} ≈ Φ̂_{Q_s,t}   (for n > s)
92	```
93	
94	#### 1.3.3 Semantic Loss 定义
95	
96	Precise KV cache (有 cross-attention) vs Imprecise KV cache (无 cross-attention) 的差距:
97	
98	```
99	L_semantic = ||Σ_{1≤t≤s} Φ̂_{Q_s,t} V_t - Σ_{1≤t≤s} Φ̂'_{Q_s,t} V'_t||_2   ... (Eq. 2)
100	```
101	
102	其中 V'_t 和 Φ̂'_{Q_s,t} 是 imprecise 版本（chunk 独立计算、无 cross-attention）。
103	
104	上界（三角不等式）:
105	
106	```
107	L_semantic ≤ L = Σ_{1≤t≤s} ||Φ̂'_{Q_s,t} V'_t - Φ̂_{Q_s,t} V_t||_2   ... (Eq. 3)
108	```
109	
110	#### 1.3.4 Token 选择的 Value Function
111	
112	给定 recomputation budget p，residual loss:
113	
114	```
115	L_{α,p} = Σ_{t∉TOP_p(α(t))} ||Φ̂'_{Q_s,t} V'_t - Φ̂_{Q_s,t} V_t||_2   ... (Eq. 4)
116	```
117	
118	**理想 value function**（不可直接计算）:
119	
120	```
121	α_ideal(t) = ||Φ̂_{Q_s,t} V_t - Φ̂'_{Q_s,t} V'_t||_2   ... (Eq. 5)
122	```
123	
124	**实际 value function**（可直接观测）:
125	
126	```
127	α(t) = Φ̂'_{Q_s,t}   — 用户查询对 imprecise Key cache 的平均 attention
128	```
129	
130	关键: Φ̂'_{Q_s,t} 可通过仅在 short user query 上运行 Transformer 轻量获得，无需完整 prefill。
131	
132	#### 1.3.5 Layer-wise Fusion
133	
134	不同层的 attention pattern 差异很大（Figure 7: 不同层的 optimal token 子集差异显著）。融合公式:
135	
136	```
137	ᾱ(t) = (1/L) Σ_{l=1}^{L} α_l(t)   ... (Eq. 7)
138	```
139	
140	其中 α_l(t) = Φ̂'_{Q_s,t}^{(l)} 是第 l 层的 query-to-context attention column sum。
141	
142	### 1.4 双阶段流程 (Dual-Stage Pipeline)
143	
144	#### Stage I: Metric Generation (轻量 pass)
145	
146	```
147	Input:  用户查询 Q_s, 各 chunk 的预计算 KV cache {K'_chunk, V'_chunk}
148	For each layer l:
149	    1. 拼接所有 chunk 的 Key cache: K' = concat(K'_chunk1, K'_chunk2, ...)
150	    2. 计算 Q_s 对 K' 的 attention weights (softmax(Q_s @ K'^T / √d))
151	    3. Column sum → α_l(t) = Σ_{q∈Q_s} attn(q, t) / |Q_s|
152	Output: 每层每 token 的重要性 α_l(t)
153	```
154	
155	**复杂度**: O(|Q_s| × s) per layer，其中 |Q_s| ≪ s（查询通常几十 token，context 几千到几万）
156	
157	#### Stage II: Selective Recomputation
158	
159	```
160	1. Fuse: ᾱ(t) = mean_l(α_l(t))
161	2. Select: TOP_p(ᾱ(t)) — 选 top-p 比例的 token
162	3. Recompute: 对选中 token 在所有层做完整 prefill（恢复 cross-attention）
163	4. Update: 将 recomputed KV 替换到对应位置
164	```
165	
166	**关键**: Stage II 中 selection 对所有层是统一的（同一批 token），保证计算效率。
167	
168	### 1.5 性能指标
169	
170	| 配置 | RULER Avg | LongBench Avg |
171	|------|-----------|---------------|
172	| Full Recompute | 基准 | 基准 |
173	| Naive Reuse (0%) | -7~-44% | -10~-43% |
174	| CacheBlend (20%) | +39.8% vs naive | 中等 |
175	| ProphetKV (20%) | **96-101% of full** | **+18.6-50.9% vs SOTA** |
176	
177	**效率**: 20% recomputation ratio → 5× speedup over full recompute (8K-16K context)
178	
179	---
180	
181	## 2. 相关方法对比
182	
183	### 2.1 方法矩阵
184	
185	| 方法 | Token 选择策略 | Query-Aware? | 粒度 | 适用场景 | 代码 |
186	|------|---------------|-------------|------|---------|------|
187	| **ProphetKV** | Query attention column sum, layer fusion | ✅ 全局 | per-token, global | RAG recomputation | 无 |
188	| **SnapKV** | Observation window attention + pooling | ⚠️ 局部 (window) | per-layer, per-head | Prefill compression | ✅ FasterDecoding/SnapKV |
189	| **H2O** | Accumulated attention score (Heavy Hitter) | ❌ 全局 saliency | per-layer | Decode-time eviction | ✅ HF transformers |
190	| **PyramidKV** | Layer-wise pyramidal budget + attention | ❌ 全局 saliency | per-layer, adaptive budget | Prefill compression | ✅ Zefan-Cai/PyramidKV |
191	| **Expected Attention** | Gaussian query distribution → closed-form E[attn] | ✅ 统计预测 | per-layer, per-head | Prefill compression | ✅ NVIDIA/kvpress |
192	| **AdaKV** | SnapKV/PyramidKV + adaptive per-head budget | ⚠️ 局部 | per-head adaptive | Prefill compression | ✅ FFY0/AdaKV |
193	| **CakeKV** | - | - | - | - | ✅ antgroup/cakekv |
194	| **KVzip** | Query-agnostic attention + context distillation | ❌ | per-token | Memory reduction | ✅ snu-mllab/KVzip |
195	
196	### 2.2 SnapKV 详解
197	
198	**论文**: "SnapKV: LLM Knows What You are Looking for Before Generation" (NeurIPS 2024)
199	
200	**核心思路**: 用 prompt 末尾的 **observation window**（最后 ~64 token）的 attention pattern 来识别 prompt 中的关键 token。
201	
202	**实现** (基于 NVIDIA/kvpress 的 SnapKVPress):
203	
204	```python
205	class SnapKVPress(ScorerPress):
206	    compression_ratio: float = 0.0   # 移除的 KV 比例
207	    window_size: int = 64            # observation window 大小
208	    kernel_size: int = 5             # pooling kernel
209	
210	    def score(self, module, hidden_states, keys, values, attentions, kwargs):
211	        # 1. 获取 observation window 的 attention weights
212	        #    取最后 window_size 个 query 对前面所有 key 的 attention
213	        attn_weights = compute_window_attention(...)  # or from `attentions`
214	
215	        # 2. 聚合: 对 query 维度取均值
216	        scores = attn_weights.mean(dim=-2)  # [batch, heads, seq_len]
217	
218	        # 3. Pooling 平滑 (avg_pool1d, kernel=5)
219	        scores = F.avg_pool1d(scores, kernel_size=5, padding=2, stride=1)
220	
221	        # 4. 跨 KV head group 平均
222	        scores = scores.reshape(batch, num_kv_heads, num_groups, seq).mean(dim=2)
223	
224	        # 5. 保护 observation window: 给最后 window_size 个 token 赋最大分数
225	        scores = F.pad(scores, (0, window_size), value=scores.max().item() + 1)
226	
227	        return scores  # [batch, num_kv_heads, seq_len]
228	```
229	
230	**与 HuggingFace 集成**: monkey-patch attention forward（SnapKV 原版）或 forward hook（kvpress 版）
231	
232	### 2.3 H2O (Heavy-Hitter Oracle)
233	
234	**论文**: NeurIPS 2023
235	
236	**核心**: **累积 attention score** — 每个 token 在所有之前的 attention 计算中被 attend 到的总量。ProphetKV **明确反对** early-layer prediction（论文 Figure 11 展示低层关注 nearby tokens、高层关注 distant tokens，pattern 差异显著），因此跨所有层计算后融合。
237	
238	```
239	score(t) = Σ_{n: n已生成} Σ_{h: 所有head} attn_weight(n, h, t)
240	```
241	
242	保留策略: 保留 **recent tokens + top-K heavy hitters**。
243	
244	**局限**: 在长上下文中，attention 是 power-law 分布，早期 token（attention sink）和近期 token 会主导，中间关键信息易被丢弃。
245	
246	### 2.4 Expected Attention (NVIDIA kvpress)
247	
248	**论文**: arXiv 2510.00636
249	
250	**核心创新**: 不依赖实际 future query，而是 **统计建模 future query 的分布**:
251	
252	```
253	假设 hidden states ~ N(μ, Σ)
254	→ queries ~ N(μ_q, Σ_q) (线性变换)
255	→ 对未来 T 个位置的 RoPE 取平均，得到 position-averaged query 分布
256	
257	Expected unnormalized attention:
258	ẑ_i = exp(μ̄_q^T k_i / √d + k_i^T Σ̄_q k_i / (2d))
259	
260	Normalized:
261	â_i = ẑ_i / Σ_j ẑ_j
262	
263	Final score (结合 value norm):
264	score_i = (â_i + ε) × ||W_o v_i||
265	```
266	
267	**实现** (kvpress ExpectedAttentionPress):
268	
269	```python
270	def score(self, module, hidden_states, keys, values, attentions, kwargs):
271	    # 1. 计算 query 的均值和协方差 (排除 sink tokens)
272	    mean_query = queries.mean(dim=2)  # [batch, heads, dim]
273	    cov_query = einsum("bnsi,bnsj->bnij", centered, centered) / seq_len
274	
275	    # 2. 对未来 T 个位置的 RoPE 取平均 → position-averaged rotation
276	    R_avg = average_rope_matrix(positions, n_future=512)
277	    mean_query = mean_query @ R_avg.T
278	    cov_query = R_avg @ cov_query @ R_avg.T
279	
280	    # 3. Expected attention score (closed-form)
281	    scores = (mean_query @ keys.T) / sqrt(d)
282	    if use_covariance:
283	        scores += einsum("bhin,bhij,bhjn->bhn", keys, cov_query, keys) / d / 2
284	    scores = softmax(scores)
285	
286	    # 4. 结合 value norm
287	    scores = (scores + epsilon) * values.norm(dim=-1)
288	    return scores
289	```
290	
291	### 2.5 PyramidKV
292	
293	**核心**: 不同层分配不同的 KV cache budget:
294	- **低层**: attention 分散 → 保留更多 token
295	- **高层**: attention 集中 → 保留更少 token
296	
297	形成 **金字塔形** budget 分配。
298	
299	---
300	
301	## 3. NVIDIA kvpress 框架分析
302	
303	### 3.1 架构设计
304	
305	```
306	BasePress          — 基类, forward hook 注册机制
307	  └─ ScorerPress   — 基于分数的剪枝基类
308	       ├── SnapKVPress
309	       ├── ObservedAttentionPress  (H2O 变体)
310	       ├── ExpectedAttentionPress
311	       ├── PyramidKVPress
312	       ├── KnormPress
313	       ├── TOVAPress
314	       └── ... (20+ 实现)
315	```
316	
317	### 3.2 核心接口
318	
319	```python
320	# 使用方式 (context manager)
321	with press(model):
322	    outputs = model.generate(...)
323	
324	# ScorerPress 子类需实现:
325	def score(self, module: nn.Module, hidden_states: torch.Tensor,
326	          keys: torch.Tensor,       # (batch, num_kv_heads, seq_len, head_dim)
327	          values: torch.Tensor,     # (batch, num_kv_heads, seq_len, head_dim)
328	          attentions: torch.Tensor, # (batch, num_heads, seq_len, seq_len)
329	          kwargs: dict
330	    ) -> torch.Tensor:              # (batch, num_kv_heads, seq_len) ← per-head 粒度
331	    """分数越高 = token 越重要 = 越不会被剪"""
332	    ...
333	
334	# ScorerPress.compress() 的实际实现:
335	def compress(self, module, hidden_states, keys, values, attentions, kwargs):
336	    if self.compression_ratio == 0: return keys, values
337	    scores = self.score(module, hidden_states, keys, values, attentions, kwargs)
338	    n_kept = int(seq_len * (1 - self.compression_ratio))
339	    indices = scores.topk(n_kept, dim=-1).indices          # (batch, heads, n_kept)
340	    indices_exp = indices.unsqueeze(-1).expand(-1,-1,-1, head_dim)
341	    keys = keys.gather(2, indices_exp).contiguous()        # (batch, heads, n_kept, dim)
342	    values = values.gather(2, indices_exp).contiguous()
343	    return keys, values
344	
345	# 关键: score 返回 per-head 粒度 → 每个 KV head 独立决定保留哪些 token
346	```
347	
348	### 3.3 Hook 机制
349	
350	```python
351	# BasePress 通过 context manager 注册 hook
352	class BasePress:
353	    def __call__(self, model):
354	        # 对每个 attention layer 注册 forward_hook
355	        for layer in model.model.layers:
356	            layer.self_attn.register_forward_hook(self.forward_hook)
357	
358	    def forward_hook(self, module, input, output):
359	        # 在 attention forward 之后执行
360	        # 获取 keys, values, attentions
361	        # 调用 compress() → score() → topk → prune
362	        ...
363	```
364	
365	---
366	
367	## 4. CompressLink Query Relevance Probe 实现方案
368	
369	### 4.1 需求分析
370	
371	CompressLink 需要 **p_r(t)** — 每个 token 被 restoration 的概率，用于:
372	1. **RABA**: p_r 高 → 分配更少 compression bits（因为会被 restore）
373	2. **CEGR**: 结合 compression error ε(t) 和 p_r(t) 选择要 restore 的 token
374	
375	**关键区别**（CompressLink vs ProphetKV）:
376	- ProphetKV: 场景是 **position-independent KV reuse**，关注 cross-attention 恢复
377	- CompressLink: 场景是 **compression + selective restoration**，关注哪些 token 值得高精度保留
378	
379	但 **底层信号完全一致**: 都是用 query attention 预测 token 重要性。
380	
381	### 4.2 推荐实现方案
382	
383	#### 方案 A: ProphetKV 式 — Query Attention Column Sum (推荐)
384	
385	```python
386	class QueryRelevanceProbe:
387	    """
388	    计算 p_r(t): 每个 context token 被 future query attend 到的概率。
389	    基于 ProphetKV 的 "user query as prophet" 假设。
390	    """
391	
392	    def __init__(self, model, probe_layers=None, aggregation='mean'):
393	        self.model = model
394	        # 可选: 只用部分层 (e.g., 后半部分层更 semantic)
395	        self.probe_layers = probe_layers  # None = 全部层
396	        self.aggregation = aggregation    # 'mean' or 'max'
397	        self._hooks = []
398	        self._attention_scores = {}
399	
400	    def _register_hooks(self):
401	        """在每个 attention layer 注册 hook 收集 attention weights"""
402	        for idx, layer in enumerate(self.model.model.layers):
403	            if self.probe_layers and idx not in self.probe_layers:
404	                continue
405	
406	            def hook_fn(module, input, output, layer_idx=idx):
407	                # 获取 attention weights: [batch, heads, q_len, kv_len]
408	                # 需要 output_attentions=True 或手动计算
409	                attn_weights = output[1]  # depends on model
410	                # Column sum (对 query 维度求和) → per-token importance
411	                # [batch, heads, kv_len]
412	                col_sum = attn_weights.sum(dim=-2)
413	                # 归一化: 除以 query 数量
414	                col_sum = col_sum / attn_weights.shape[-2]
415	                # 跨 head 平均
416	                col_sum = col_sum.mean(dim=1)  # [batch, kv_len]
417	                self._attention_scores[layer_idx] = col_sum
418	
419	            self._hooks.append(
420	                layer.self_attn.register_forward_hook(hook_fn)
421	            )
422	
423	    def compute_relevance(self, query_input_ids, kv_cache):
424	        """
425	        Stage I: 轻量 pass，只让 query tokens attend to cached keys
426	
427	        Args:
428	            query_input_ids: 用户查询的 token ids
429	            kv_cache: 已压缩/预计算的 KV cache
430	
431	        Returns:
432	            p_r: [seq_len] tensor, 每个 context token 的 relevance probability
433	        """
434	        self._attention_scores = {}
435	        self._register_hooks()
436	
437	        try:
438	            # 只对 query tokens 做 forward, 使用已有 KV cache
439	            with torch.no_grad():
440	                self.model(
441	                    query_input_ids,
442	                    past_key_values=kv_cache,
443	                    output_attentions=True,
444	                    use_cache=True,
445	                )
446	        finally:
447	            for h in self._hooks:
448	                h.remove()
449	            self._hooks = []
450	
451	        # Layer fusion: ᾱ(t) = mean_l(α_l(t))
452	        all_scores = torch.stack(list(self._attention_scores.values()))
453	        if self.aggregation == 'mean':
454	            fused = all_scores.mean(dim=0)  # [batch, kv_len]
455	        else:
456	            fused = all_scores.max(dim=0).values
457	
458	        # Score → Probability: softmax or min-max normalization
459	        p_r = self._score_to_probability(fused)
460	        return p_r
461	
462	    def _score_to_probability(self, scores):
463	        """将 raw attention score 转换为 [0, 1] 概率"""
464	        # 方法 1: Min-max normalization
465	        s_min, s_max = scores.min(dim=-1, keepdim=True).values, \
466	                       scores.max(dim=-1, keepdim=True).values
467	        p_r = (scores - s_min) / (s_max - s_min + 1e-8)
468	
469	        # 方法 2 (替代): Temperature-scaled softmax
470	        # p_r = F.softmax(scores / temperature, dim=-1)
471	
472	        return p_r
473	```
474	
475	#### 方案 B: Expected Attention 式 — 无需 Query (备选)
476	
477	适用于 **query 不可用** 的场景（如 prefill 阶段 compression，此时 user query 还没到）:
478	
479	```python
480	class ExpectedRelevanceProbe:
481	    """
482	    基于 Expected Attention 方法，统计估算 future query 的 attention。
483	    不需要实际 query，但精度略低于方案 A。
484	    """
485	
486	    def compute_relevance(self, keys, queries_so_far, values):
487	        """
488	        从已有 query 的统计特征预测 future attention
489	
490	        keys: [batch, heads, seq, dim]
491	        queries_so_far: [batch, heads, seq, dim] — prefill 阶段的 query
492	        values: [batch, heads, seq, dim]
493	        """
494	        d = keys.shape[-1]
495	
496	        # 1. Query distribution: mean + covariance
497	        mu_q = queries_so_far.mean(dim=2)     # [batch, heads, dim]
498	        centered = queries_so_far - mu_q.unsqueeze(2)
499	        cov_q = torch.einsum("bhsi,bhsj->bhij", centered, centered) / queries_so_far.shape[2]
500	
501	        # 2. Expected attention (Gaussian closed-form)
502	        # E[exp(q^T k / √d)] = exp(μ^T k/√d + k^T Σ k/(2d))
503	        mean_scores = torch.matmul(mu_q.unsqueeze(2), keys.transpose(-1, -2)).squeeze(2) / math.sqrt(d)
504	        cov_scores = torch.einsum("bhin,bhij,bhjn->bhn", keys, cov_q, keys) / d / 2
505	        scores = F.softmax(mean_scores + cov_scores, dim=-1)
506	
507	        # 3. 结合 value norm
508	        v_norm = values.norm(dim=-1)
509	        scores = (scores + 0.02) * v_norm
510	
511	        # 4. Layer aggregation + normalization → p_r
512	        p_r = self._normalize(scores.mean(dim=1))  # average across heads
513	        return p_r
514	```
515	
516	#### 方案 C: SnapKV 式 — Observation Window (轻量备选)
517	
518	适用于 **在线 streaming** 场景:
519	
520	```python
521	class ObservationWindowProbe:
522	    """
523	    用最后 window_size 个 token 的 attention pattern 估计 token 重要性。
524	    不需要独立的 query forward pass。
525	    """
526	
527	    def __init__(self, window_size=64, kernel_size=5):
528	        self.window_size = window_size
529	        self.kernel_size = kernel_size
530	
531	    def compute_relevance(self, attn_weights):
532	        """
533	        attn_weights: [batch, heads, seq, seq] — 最后一个 attention layer 的输出
534	
535	        Returns: p_r [batch, seq]
536	        """
537	        # 取最后 window_size 个 query 对前面 token 的 attention
538	        window_attn = attn_weights[:, :, -self.window_size:, :-self.window_size]
539	
540	        # 对 query 维度求和
541	        scores = window_attn.sum(dim=-2)  # [batch, heads, prefix_len]
542	
543	        # Avg pooling 平滑
544	        scores = F.avg_pool1d(scores, kernel_size=self.kernel_size,
545	                              padding=self.kernel_size // 2, stride=1)
546	
547	        # 跨 head 平均
548	        scores = scores.mean(dim=1)  # [batch, prefix_len]
549	
550	        # 补齐 window tokens (它们的 p_r 应为 1.0, 因为是最近的)
551	        window_scores = torch.ones(scores.shape[0], self.window_size, device=scores.device)
552	        scores = torch.cat([scores, window_scores], dim=-1)
553	
554	        # Normalize to [0, 1]
555	        p_r = (scores - scores.min()) / (scores.max() - scores.min() + 1e-8)
556	        return p_r
557	```
558	
559	### 4.3 方案选择建议
560	
561	| 维度 | 方案 A (ProphetKV式) | 方案 B (Expected Attn式) | 方案 C (SnapKV式) |
562	|------|---------------------|------------------------|--------------------|
563	| 精度 | ★★★★★ | ★★★★ | ★★★ |
564	| 需要 query? | 是 | 否 | 否 (用 window) |
565	| 额外开销 | 轻量 forward (O(|Q|×s)) | 统计计算 (O(s×d²)) | 无额外 pass |
566	| 适用时机 | Decode 前/Compression 后 | Prefill 时 | Prefill 时 |
567	| **推荐用于** | **CEGR** (有 query 时) | RABA (prefill 时预估) | 快速 fallback |
568	
569	**CompressLink 推荐**: **两阶段策略**
570	1. **Prefill/Compression 阶段**: 用 方案 B 或 C 计算 **初始 p_r_est**，用于 RABA bit allocation
571	2. **Decode/Restoration 阶段**: 用 方案 A 计算 **精确 p_r**，用于 CEGR restoration selection
572	
573	### 4.4 p_r(t) 的关键设计决策
574	
575	#### 4.4.1 获取时机
576	
577	```
578	Timeline:
579	  Prefill ──→ Compression ──→ User Query arrives ──→ Decode
580	                                      ↑
581	                              ProphetKV Stage I 在这里计算 p_r
582	```
583	
584	- **RABA 需求**: compression 时就需要 p_r → 此时 query 未到 → 需要 **预估** (方案 B/C)
585	- **CEGR 需求**: decode 前选择 restore 哪些 token → query 已到 → 可以用 **精确** p_r (方案 A)
586	
587	**解决方案**: RABA 的 p_r 可以用 Expected Attention 预估，或者采用 **在线更新**:
588	1. Prefill 时用 uniform p_r 做初始 bit allocation
589	2. Query 到达后用方案 A 计算精确 p_r
590	3. 对 p_r 高但 compression error 大的 token 做 restoration
591	
592	#### 4.4.2 粒度
593	
594	ProphetKV 使用 **per-token, global (all layers)** 的粒度:
595	
596	```
597	α_l(t) = per-layer per-token
598	ᾱ(t) = per-token (fused across layers) → 用于 token selection
599	```
600	
601	对 CompressLink:
602	- **RABA**: 需要 per-layer per-token 的 p_r（因为 KVTC 是 per-layer 做 bit allocation）
603	- **CEGR**: 需要 per-token global 的 p_r（因为 restoration 是 per-token 的）
604	
605	→ **同时保留 per-layer 和 fused 两个粒度**
606	
607	#### 4.4.3 Score → Probability 转换
608	
609	ProphetKV 直接用 raw attention score (Φ̂'_{Q_s,t}) 做 TOP_p 选择，没有显式转为概率。
610	
611	CompressLink 需要 [0,1] 概率，建议:
612	
613	```python
614	# 方法 1: 基于排序的分位数映射 (推荐)
615	ranks = scores.argsort(descending=True).argsort()  # rank of each token
616	p_r = 1.0 - ranks.float() / len(scores)  # top token → p_r ≈ 1.0
617	
618	# 方法 2: Temperature softmax
619	p_r = F.softmax(scores / tau, dim=-1) * len(scores)  # scale to ~[0, num_tokens]
620	p_r = p_r.clamp(0, 1)
621	
622	# 方法 3: Sigmoid with learned threshold
623	p_r = torch.sigmoid((scores - scores.median()) / tau)
624	```
625	
626	### 4.5 与 KVTC Compression Pipeline 的接口
627	
628	```python
629	# 在 KVTC 的 pipeline_fast.py 中集成
630	
631	class CompressLinkPipeline:
632	    def __init__(self, model, kvtc_pipeline, relevance_probe):
633	        self.model = model
634	        self.kvtc = kvtc_pipeline
635	        self.probe = relevance_probe  # QueryRelevanceProbe
636	
637	    def compress_with_raba(self, kv_cache, p_r_est=None):
638	        """
639	        RABA: Restoration-Aware Bit Allocation
640	        p_r 高的 token → 更少 bits (会被 restore)
641	        p_r 低的 token → 更多 bits (不会被 restore, 需要高保真)
642	        """
643	        for layer_idx in range(self.model.config.num_hidden_layers):
644	            keys = kv_cache[layer_idx][0]
645	            values = kv_cache[layer_idx][1]
646	
647	            if p_r_est is not None:
648	                # 调整 KVTC 的 per-token bit budget
649	                # base_bits: KVTC 的默认 bit allocation (e.g., from eigenvalue entropy)
650	                base_bits = self.kvtc.compute_bit_budget(keys, layer_idx)
651	                # RABA 调整: p_r 高 → 减少 bits
652	                adjusted_bits = base_bits * (1 - beta * p_r_est[layer_idx])
653	                adjusted_bits = adjusted_bits.clamp(min=min_bits)
654	            else:
655	                adjusted_bits = self.kvtc.compute_bit_budget(keys, layer_idx)
656	
657	            compressed = self.kvtc.compress(keys, values, bits=adjusted_bits)
658	            ...
659	
660	    def restore_with_cegr(self, compressed_cache, query_ids, budget_ratio=0.2):
661	        """
662	        CEGR: Compression-Error-Guided Restoration
663	        选择 restore 哪些 token, 基于:
664	        - p_r(t): query relevance (高 → 更值得 restore)
665	        - ε(t): compression error (高 → restore 收益大)
666	        """
667	        # 1. 计算精确 p_r (方案 A)
668	        p_r = self.probe.compute_relevance(query_ids, compressed_cache)
669	
670	        # 2. 计算 compression error
671	        epsilon = self.kvtc.estimate_error(compressed_cache)
672	
673	        # 3. 综合分数: 同时考虑 relevance 和 error
674	        # score = p_r * ε  (relevance × error magnitude)
675	        restore_score = p_r * epsilon
676	
677	        # 4. 选 top-budget_ratio 的 token restore
678	        n_restore = int(len(restore_score) * budget_ratio)
679	        restore_indices = restore_score.topk(n_restore).indices
680	
681	        # 5. Recompute selected tokens
682	        restored_cache = self.recompute(compressed_cache, restore_indices)
683	        return restored_cache
684	```
685	
686	### 4.6 与 MEPIC Boundary Recomputation 的关系
687	
688	ProphetKV 的 overlap 分析（Figure 4）显示 query-attended tokens 与 decoding-attended tokens 高度重叠。
689	
690	**推测**: MEPIC 的 chunk boundary tokens（chunk 首尾几个 token）:
691	- 如果它们是 cross-chunk attention 的关键节点 → p_r 应该自然偏高
692	- 但 ProphetKV 的分析表明，重要 token 不一定在 boundary 位置 → **p_r 比固定 boundary 更灵活**
693	
694	→ CompressLink 中，MEPIC boundary recomputation 可以被 CEGR **替代或增强**:
695	- CEGR 用 p_r + ε 自动选择需要 restore 的 token（包含但不限于 boundary）
696	- 如果 boundary token 确实重要，它们的 p_r 和 ε 自然会高，会被 CEGR 选中
697	
698	---
699	
700	## 5. 可复用代码资源
701	
702	### 5.1 NVIDIA kvpress (推荐参考)
703	
704	- **仓库**: https://github.com/NVIDIA/kvpress
705	- **许可**: MIT (推测, 需确认)
706	- **价值**: 完整的 hook-based KV cache compression 框架，支持 20+ 方法
707	- **关键文件**:
708	  - `kvpress/presses/scorer_press.py` — ScorerPress 基类，forward hook + topk 剪枝
709	  - `kvpress/presses/snapkv_press.py` — SnapKV 实现，observation window + pooling
710	  - `kvpress/presses/expected_attention_press.py` — Expected Attention，Gaussian closed-form
711	  - `kvpress/presses/observed_attention_press.py` — H2O 式累积 attention
712	
713	### 5.2 SnapKV 原版
714	
715	- **仓库**: https://github.com/FasterDecoding/SnapKV
716	- **关键文件**:
717	  - `snapkv/monkeypatch/snapkv_utils.py` — 核心 attention score 计算
718	  - `snapkv/monkeypatch/llama_hijack_4_37.py` — Llama monkey-patch 示例
719	- **集成方式**: monkey-patch attention forward（较 invasive，不如 kvpress 的 hook 方式优雅）
720	
721	### 5.3 HuggingFace Transformers 原生支持
722	
723	- **Issue #30758**: H2O-style KV cache sparsity 已作为 feature request
724	- 部分 cache 管理功能已内置于 `transformers.QuantizedCache`
725	
726	---
727	
728	## 6. 总结与建议
729	
730	### 6.1 关键发现
731	
732	1. **ProphetKV 无公开代码**，但方法足够清晰可以从论文复现
733	2. **核心公式极其简单**: p_r(t) = mean_l(column_sum(softmax(Q_s @ K_l^T / √d)))
734	3. **NVIDIA kvpress 是最佳参考框架**: hook-based 设计可直接复用
735	4. **Expected Attention 是 query 不可用时的最佳替代**
736	5. **SnapKV 的 observation window 是最轻量的方案** 但精度有限
737	
738	### 6.2 CompressLink 实施路线
739	
740	```
741	Phase 1: 实现 QueryRelevanceProbe (方案 A)
742	  - 基于 kvpress ScorerPress 的 hook 机制
743	  - Column sum + layer fusion
744	  - Score → probability 转换
745	
746	Phase 2: 集成到 RABA
747	  - Prefill 阶段用 Expected Attention (方案 B) 预估 p_r
748	  - 调整 KVTC per-token bit budget
749	
750	Phase 3: 集成到 CEGR
751	  - Query 到达后计算精确 p_r (方案 A)
752	  - 结合 compression error 选择 restore token
753	  - 替代/增强 MEPIC boundary recomputation
754	
755	Phase 4: 端到端优化
756	  - p_r 计算与 KV cache decode 的 overlap
757	  - 选择性 layer probe (只用后半部分层?)
758	  - Adaptive temperature for score → probability
759	```
760	
761	### 6.3 风险与未知
762	
763	1. **ProphetKV 假设 RAG 场景** — CompressLink 的 general compression 场景中 query 的预测力是否同样强需要验证
764	2. **Expected Attention 的 Gaussian 假设** — 实际 hidden states 未必 Gaussian，需要验证误差
765	3. **p_r 在 RABA 中的反向使用** — ProphetKV 用 p_r 选 token 做 recompute，RABA 用 p_r 决定 bit allocation，逻辑一致性需要理论分析
766	4. **Per-layer vs Global p_r** — KVTC 是 per-layer 操作，但 ProphetKV 建议 fusion 效果更好，需要实验对比
767	5. **NoPE 兼容性** — ProphetKV 和 kvpress 都假设标准 RoPE attention。MEPIC 存储 NoPE KV cache (不含位置编码)，query 侧加 RoPE。计算 p_r 时需手动做 RoPE-query × NoPE-key attention，不能直接用 HF 的 output_attentions=True
768	6. **Boundary tokens 硬约束** — MEPIC chunk 边界 token 的 p_r 必须 = 1.0（RABA 给 0 bits，反正要 recompute）。CEGR budget 应排除 boundary tokens（mandatory ~5-10%），discretionary budget 仅 ~10-15%
769	
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_016vF9RQ7AzbFvvXvhj3J5WE",
  "session_id": "fdf71b47-8f0f-4233-b6c0-f01ae22a3454",
  "uuid": "9b54f7a8-58f2-4bac-a834-90e0ecbec19e"
}
```

</details>

---

### System

_source line 26_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "ae11cdb486c92a588",
  "tool_use_id": "toolu_01AxWdWziX2UN5if8HFGfTaN",
  "status": "completed",
  "output_file": "",
  "summary": "Read KVTC survey for API",
  "usage": {
    "total_tokens": 29611,
    "tool_uses": 1,
    "duration_ms": 16887
  },
  "uuid": "add0c299-2f38-43b7-9c1f-33edf9600de1",
  "session_id": "fdf71b47-8f0f-4233-b6c0-f01ae22a3454"
}
```

---

### Tool result

_source line 27 · 2026-05-14T05:14:05.694Z_

<details><summary>↩ Tool result · `toolu_01AxWdWziX2UN5if8HFGfTaN`</summary>

````text
Based on the KVTC survey file, here are the key API details:

## Module Paths

```
src/
├── common.py              # Core data structures
├── pca.py                 # PCA transforms, RoPE operations
├── quantize.py            # DP bit allocation (exact), uniform quantize/dequantize
├── gpu_ops.py             # Greedy bit allocation (approximate), batch ops
├── entropy.py             # zlib DEFLATE + bit packing/unpacking
├── ans_entropy.py         # rANS entropy coding (triple-mode picker)
├── pipeline.py            # Reference pipeline (CPU)
├── pipeline_fast.py       # GPU accelerated pipeline
├── calibrate.py           # PCA calibration
```

## Function Signatures

### Compression/Decompression

**Entropy (bit packing & compression)**:
```python
# src/entropy.py
pack_bits(indices_list, bit_widths) -> bytes
unpack_bits(packed, bit_widths, lengths) -> list
compress(packed, level=6) -> (bytes, ratio)
decompress(compressed, original_size) -> bytes

# src/ans_entropy.py
compress_best(packed_bytes, level=6) -> (bytes, ratio)  # Triple picker: zlib/LZMA/rANS
decompress_best(compressed, original_size) -> bytes
```

### Bit Allocation

**Exact DP version** (`src/quantize.py:16-56`):
```python
def dp_bit_allocation(eigenvalues, bit_budget, max_bits=16, group_size=1):
    # Returns: widths[d] with each value in [0, 16]
    # Error function: E(i, b) = λ_i / 4^b (if bits > 0) else λ_i
```

**Greedy approximate version** (`src/gpu_ops.py:10-57`):
```python
def greedy_bit_allocation(eigenvalues, bit_budget, max_bits=16):
    # Gain function: gain(i, b) = λ_i × 3 / 4^b
    # Returns: per-component bit widths via topk selection
```

### PCA Operations

**PCA Transform** (`src/pca.py`):
```python
# Transform
pca_transform(centered, eigenvectors) -> coefficients

# RoPE handling (keys only)
apply_rope_inverse(keys, positions) -> unrotated_keys  # rotation by -θ
apply_rope(keys, positions) -> rotated_keys            # rotation by θ
apply_rope_undo(cos, sin) -> rotated_values            # for efficient inversion

# Calibration
class PCACalibrator:
    def compute(self, bit_budget_ratio: float = 0.25) -> CalibrationData
        # SVD-based calibration: U, S, Vh = torch.linalg.svd(centered)
        # eigenvalues = S² / (n-1)
        # Returns CalibrationData with mean, eigenvectors, eigenvalues, bit_widths
```

### Pipeline Compression

**Reference CPU pipeline** (`src/pipeline.py:23`):
```python
def compress(self, kv_cache, positions):
    # Returns CompressedKVCache with metadata and bytes
```

**GPU accelerated pipeline** (`src/pipeline_fast.py:37`):
```python
def compress(self, kv_cache, positions):
    # Uses greedy_bit_allocation instead of exact DP
    # Returns CompressedKVCache
```

## Data Structure Definitions

**Core data structures** (`src/common.py`):

```python
class CalibrationData:
    mean: torch.Tensor              # [dim] - per-component mean
    eigenvectors: torch.Tensor      # [dim, dim] or [dim, kept_dims]
    eigenvalues: torch.Tensor       # [dim] - variance spectrum
    bit_widths: torch.Tensor        # [dim] - DP-allocated bit widths
    bit_budget: int                 # Total bits available

class CompressedKVCache:
    compressed_data: bytes          # Entropy-coded bit-packed data
    metadata: dict                  # Stores bit_widths and dimensions
    sink_k: torch.Tensor           # FP16 uncompressed (first 4 tokens)
    sink_v: torch.Tensor
    window_k: torch.Tensor         # FP16 uncompressed (last 128 tokens)
    window_v: torch.Tensor

class PCAEntry:
    mean: torch.Tensor
    eigenvectors: torch.Tensor     # Vh from SVD
    eigenvalues: torch.Tensor
    bit_widths: torch.Tensor       # Per-component allocation
    bit_budget: int

class QuantizationParams:
    scale: torch.Tensor            # Per-component scale
    zero_point: torch.Tensor       # Per-component offset
```

## Key Design Points

1. **Data Flow**: Raw KV → RoPE undo (keys) → PCA transform → DP bit allocation → Uniform quantize → Bit packing → Entropy coding (triple picker: zlib/LZMA/rANS)

2. **Bit Allocation Error Function**: `E(i, b) = λ_i / 4^b` where λ_i is eigenvalue and 4^b is MSE reduction factor (each bit halves quantization step)

3. **Token Protection**: First 4 tokens (sink) + last 128 tokens (window) kept in FP16, middle tokens compressed

4. **Per-Head PCA**: Default `group_size=1` means per-head independent PCA for maximum decorrelation

5. **Entropy Coding**: Triple-mode picker with 1-byte prefix tag (`Z`=zlib, `L`=LZMA, `A`=rANS) selects smallest

6. **Decompression**: No restoration probabilities needed—bit_widths stored in metadata
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fdf71b47-8f0f-4233-b6c0-f01ae22a3454",
  "uuid": "5c3415fb-356e-4686-b466-d0d0ea4dcdf6",
  "tool_use_result": {
    "status": "completed",
    "prompt": "Read the KVTC survey file at /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/distill_kv_rag_cache/artifacts/kvtc_survey.md to understand the KVTC API (function signatures, module structure, data structures). Report back the key API details: module paths, function signatures for compress/decompress/bit_allocation/PCA, and data structure definitions.",
    "agentId": "ae11cdb486c92a588",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Based on the KVTC survey file, here are the key API details:\n\n## Module Paths\n\n```\nsrc/\n├── common.py              # Core data structures\n├── pca.py                 # PCA transforms, RoPE operations\n├── quantize.py            # DP bit allocation (exact), uniform quantize/dequantize\n├── gpu_ops.py             # Greedy bit allocation (approximate), batch ops\n├── entropy.py             # zlib DEFLATE + bit packing/unpacking\n├── ans_entropy.py         # rANS entropy coding (triple-mode picker)\n├── pipeline.py            # Reference pipeline (CPU)\n├── pipeline_fast.py       # GPU accelerated pipeline\n├── calibrate.py           # PCA calibration\n```\n\n## Function Signatures\n\n### Compression/Decompression\n\n**Entropy (bit packing & compression)**:\n```python\n# src/entropy.py\npack_bits(indices_list, bit_widths) -> bytes\nunpack_bits(packed, bit_widths, lengths) -> list\ncompress(packed, level=6) -> (bytes, ratio)\ndecompress(compressed, original_size) -> bytes\n\n# src/ans_entropy.py\ncompress_best(packed_bytes, level=6) -> (bytes, ratio)  # Triple picker: zlib/LZMA/rANS\ndecompress_best(compressed, original_size) -> bytes\n```\n\n### Bit Allocation\n\n**Exact DP version** (`src/quantize.py:16-56`):\n```python\ndef dp_bit_allocation(eigenvalues, bit_budget, max_bits=16, group_size=1):\n    # Returns: widths[d] with each value in [0, 16]\n    # Error function: E(i, b) = λ_i / 4^b (if bits > 0) else λ_i\n```\n\n**Greedy approximate version** (`src/gpu_ops.py:10-57`):\n```python\ndef greedy_bit_allocation(eigenvalues, bit_budget, max_bits=16):\n    # Gain function: gain(i, b) = λ_i × 3 / 4^b\n    # Returns: per-component bit widths via topk selection\n```\n\n### PCA Operations\n\n**PCA Transform** (`src/pca.py`):\n```python\n# Transform\npca_transform(centered, eigenvectors) -> coefficients\n\n# RoPE handling (keys only)\napply_rope_inverse(keys, positions) -> unrotated_keys  # rotation by -θ\napply_rope(keys, positions) -> rotated_keys            # rotation by θ\napply_rope_undo(cos, sin) -> rotated_values            # for efficient inversion\n\n# Calibration\nclass PCACalibrator:\n    def compute(self, bit_budget_ratio: float = 0.25) -> CalibrationData\n        # SVD-based calibration: U, S, Vh = torch.linalg.svd(centered)\n        # eigenvalues = S² / (n-1)\n        # Returns CalibrationData with mean, eigenvectors, eigenvalues, bit_widths\n```\n\n### Pipeline Compression\n\n**Reference CPU pipeline** (`src/pipeline.py:23`):\n```python\ndef compress(self, kv_cache, positions):\n    # Returns CompressedKVCache with metadata and bytes\n```\n\n**GPU accelerated pipeline** (`src/pipeline_fast.py:37`):\n```python\ndef compress(self, kv_cache, positions):\n    # Uses greedy_bit_allocation instead of exact DP\n    # Returns CompressedKVCache\n```\n\n## Data Structure Definitions\n\n**Core data structures** (`src/common.py`):\n\n```python\nclass CalibrationData:\n    mean: torch.Tensor              # [dim] - per-component mean\n    eigenvectors: torch.Tensor      # [dim, dim] or [dim, kept_dims]\n    eigenvalues: torch.Tensor       # [dim] - variance spectrum\n    bit_widths: torch.Tensor        # [dim] - DP-allocated bit widths\n    bit_budget: int                 # Total bits available\n\nclass CompressedKVCache:\n    compressed_data: bytes          # Entropy-coded bit-packed data\n    metadata: dict                  # Stores bit_widths and dimensions\n    sink_k: torch.Tensor           # FP16 uncompressed (first 4 tokens)\n    sink_v: torch.Tensor\n    window_k: torch.Tensor         # FP16 uncompressed (last 128 tokens)\n    window_v: torch.Tensor\n\nclass PCAEntry:\n    mean: torch.Tensor\n    eigenvectors: torch.Tensor     # Vh from SVD\n    eigenvalues: torch.Tensor\n    bit_widths: torch.Tensor       # Per-component allocation\n    bit_budget: int\n\nclass QuantizationParams:\n    scale: torch.Tensor            # Per-component scale\n    zero_point: torch.Tensor       # Per-component offset\n```\n\n## Key Design Points\n\n1. **Data Flow**: Raw KV → RoPE undo (keys) → PCA transform → DP bit allocation → Uniform quantize → Bit packing → Entropy coding (triple picker: zlib/LZMA/rANS)\n\n2. **Bit Allocation Error Function**: `E(i, b) = λ_i / 4^b` where λ_i is eigenvalue and 4^b is MSE reduction factor (each bit halves quantization step)\n\n3. **Token Protection**: First 4 tokens (sink) + last 128 tokens (window) kept in FP16, middle tokens compressed\n\n4. **Per-Head PCA**: Default `group_size=1` means per-head independent PCA for maximum decorrelation\n\n5. **Entropy Coding**: Triple-mode picker with 1-byte prefix tag (`Z`=zlib, `L`=LZMA, `A`=rANS) selects smallest\n\n6. **Decompression**: No restoration probabilities needed—bit_widths stored in metadata"
      }
    ],
    "totalDurationMs": 16888,
    "totalTokens": 31083,
    "totalToolUseCount": 1,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 11135,
      "cache_read_input_tokens": 18454,
      "output_tokens": 1489,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 11135
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 1489,
          "cache_read_input_tokens": 18454,
          "cache_creation_input_tokens": 11135,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 11135,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 1,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  }
}
````

</details>

---

### System

_source line 28_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a7fb22f008ca138e6",
  "tool_use_id": "toolu_016vF9RQ7AzbFvvXvhj3J5WE",
  "status": "completed",
  "output_file": "",
  "summary": "Read ProphetKV survey",
  "usage": {
    "total_tokens": 32710,
    "tool_uses": 1,
    "duration_ms": 14894
  },
  "uuid": "1343a45d-dda0-4a70-b1fa-7d34226b177e",
  "session_id": "fdf71b47-8f0f-4233-b6c0-f01ae22a3454"
}
```

---

### Tool result

_source line 29 · 2026-05-14T05:14:07.530Z_

<details><summary>↩ Tool result · `toolu_016vF9RQ7AzbFvvXvhj3J5WE`</summary>

````text
Based on the ProphetKV survey file, here's a comprehensive report on the query relevance mechanism:

## Query Relevance Computation

**ProphetKV's core principle**: "User Query as a Prophet" - the assumption that user query attention patterns predict token importance during decoding. The method computes relevance through query attention column sums across all transformer layers.

**Formula** (Equations 28-30):
```
α_l(t) = Φ̂'_{Q_s,t}^(l) = (1/|Q_s|) Σ_q softmax(q·K'/√d)_t
ᾱ(t) = (1/L) Σ_l α_l(t)
T_p = Top-p(ᾱ(t))
```

Where:
- `α_l(t)`: Per-layer, per-token relevance score (average attention across query tokens attending to context token t)
- `ᾱ(t)`: Fused global relevance (mean across all L layers)
- K' is the imprecise (cached/chunked) key matrix

**Computational complexity**: O(|Q_s| × s) per layer, where |Q_s| ≪ s (queries typically ~20-100 tokens, context is thousands-tens of thousands).

## Token Selection Strategy

The two-stage pipeline:

**Stage I: Lightweight Metric Generation**
- Concatenate all chunked KV caches
- Compute user query Q_s attention weights over cached keys
- Column sum for each layer → `α_l(t)` per token
- No need for full prefill

**Stage II: Selective Recomputation**
1. **Fuse**: Average scores across layers: `ᾱ(t) = mean_l(α_l(t))`
2. **Select**: Top-p selection on fused scores
3. **Recompute**: Full prefill on selected tokens to restore cross-attention
4. **Update**: Replace computed KV into cache positions

**Key insight**: Layer-wise fusion is critical because different layers attend to different subsets of tokens (Figure 7 shows significant variance across layers). A single early-layer prediction would miss high-layer important tokens.

## Probe Mechanism Code Snippets

The survey provides a detailed implementation template at **Section 4.2, Method A (ProphetKV-style Query Attention Column Sum)**, lines 386-473:

```python
class QueryRelevanceProbe:
    def _register_hooks(self):
        """Register hooks on attention layers to collect attention weights"""
        for idx, layer in enumerate(self.model.model.layers):
            def hook_fn(module, input, output, layer_idx=idx):
                attn_weights = output[1]  # [batch, heads, q_len, kv_len]
                col_sum = attn_weights.sum(dim=-2)  # Column sum
                col_sum = col_sum / attn_weights.shape[-2]  # Normalize by query count
                col_sum = col_sum.mean(dim=1)  # Average across heads
                self._attention_scores[layer_idx] = col_sum
            self._hooks.append(layer.self_attn.register_forward_hook(hook_fn))

    def compute_relevance(self, query_input_ids, kv_cache):
        """Stage I: lightweight pass computing query relevance"""
        self._attention_scores = {}
        self._register_hooks()
        try:
            with torch.no_grad():
                self.model(query_input_ids, past_key_values=kv_cache,
                          output_attentions=True, use_cache=True)
        finally:
            for h in self._hooks: h.remove()
        
        # Layer fusion
        all_scores = torch.stack(list(self._attention_scores.values()))
        fused = all_scores.mean(dim=0)  # [batch, kv_len]
        p_r = self._score_to_probability(fused)
        return p_r
```

**Key implementation details**:
- Uses forward hooks to intercept attention computation (non-invasive)
- Computes column sum per layer by summing attention across query dimension
- Averages across attention heads
- Fuses across layers via mean aggregation
- Converts raw scores to [0,1] probability via min-max normalization or temperature-scaled softmax

The survey also provides alternatives for when query is unavailable (Expected Attention method, lines 480-514) and a lightweight observation window approach (SnapKV-style, lines 521-557).
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fdf71b47-8f0f-4233-b6c0-f01ae22a3454",
  "uuid": "d513acff-312d-4700-b791-babae18377ce",
  "tool_use_result": {
    "status": "completed",
    "prompt": "Read the ProphetKV survey file at /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/distill_kv_rag_cache/artifacts/prophetkv_survey.md to understand ProphetKV's query relevance mechanism. Report back: how query relevance is computed, token selection strategy, and any code snippets for the probe mechanism.",
    "agentId": "a7fb22f008ca138e6",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Based on the ProphetKV survey file, here's a comprehensive report on the query relevance mechanism:\n\n## Query Relevance Computation\n\n**ProphetKV's core principle**: \"User Query as a Prophet\" - the assumption that user query attention patterns predict token importance during decoding. The method computes relevance through query attention column sums across all transformer layers.\n\n**Formula** (Equations 28-30):\n```\nα_l(t) = Φ̂'_{Q_s,t}^(l) = (1/|Q_s|) Σ_q softmax(q·K'/√d)_t\nᾱ(t) = (1/L) Σ_l α_l(t)\nT_p = Top-p(ᾱ(t))\n```\n\nWhere:\n- `α_l(t)`: Per-layer, per-token relevance score (average attention across query tokens attending to context token t)\n- `ᾱ(t)`: Fused global relevance (mean across all L layers)\n- K' is the imprecise (cached/chunked) key matrix\n\n**Computational complexity**: O(|Q_s| × s) per layer, where |Q_s| ≪ s (queries typically ~20-100 tokens, context is thousands-tens of thousands).\n\n## Token Selection Strategy\n\nThe two-stage pipeline:\n\n**Stage I: Lightweight Metric Generation**\n- Concatenate all chunked KV caches\n- Compute user query Q_s attention weights over cached keys\n- Column sum for each layer → `α_l(t)` per token\n- No need for full prefill\n\n**Stage II: Selective Recomputation**\n1. **Fuse**: Average scores across layers: `ᾱ(t) = mean_l(α_l(t))`\n2. **Select**: Top-p selection on fused scores\n3. **Recompute**: Full prefill on selected tokens to restore cross-attention\n4. **Update**: Replace computed KV into cache positions\n\n**Key insight**: Layer-wise fusion is critical because different layers attend to different subsets of tokens (Figure 7 shows significant variance across layers). A single early-layer prediction would miss high-layer important tokens.\n\n## Probe Mechanism Code Snippets\n\nThe survey provides a detailed implementation template at **Section 4.2, Method A (ProphetKV-style Query Attention Column Sum)**, lines 386-473:\n\n```python\nclass QueryRelevanceProbe:\n    def _register_hooks(self):\n        \"\"\"Register hooks on attention layers to collect attention weights\"\"\"\n        for idx, layer in enumerate(self.model.model.layers):\n            def hook_fn(module, input, output, layer_idx=idx):\n                attn_weights = output[1]  # [batch, heads, q_len, kv_len]\n                col_sum = attn_weights.sum(dim=-2)  # Column sum\n                col_sum = col_sum / attn_weights.shape[-2]  # Normalize by query count\n                col_sum = col_sum.mean(dim=1)  # Average across heads\n                self._attention_scores[layer_idx] = col_sum\n            self._hooks.append(layer.self_attn.register_forward_hook(hook_fn))\n\n    def compute_relevance(self, query_input_ids, kv_cache):\n        \"\"\"Stage I: lightweight pass computing query relevance\"\"\"\n        self._attention_scores = {}\n        self._register_hooks()\n        try:\n            with torch.no_grad():\n                self.model(query_input_ids, past_key_values=kv_cache,\n                          output_attentions=True, use_cache=True)\n        finally:\n            for h in self._hooks: h.remove()\n        \n        # Layer fusion\n        all_scores = torch.stack(list(self._attention_scores.values()))\n        fused = all_scores.mean(dim=0)  # [batch, kv_len]\n        p_r = self._score_to_probability(fused)\n        return p_r\n```\n\n**Key implementation details**:\n- Uses forward hooks to intercept attention computation (non-invasive)\n- Computes column sum per layer by summing attention across query dimension\n- Averages across attention heads\n- Fuses across layers via mean aggregation\n- Converts raw scores to [0,1] probability via min-max normalization or temperature-scaled softmax\n\nThe survey also provides alternatives for when query is unavailable (Expected Attention method, lines 480-514) and a lightweight observation window approach (SnapKV-style, lines 521-557)."
      }
    ],
    "totalDurationMs": 14895,
    "totalTokens": 33805,
    "totalToolUseCount": 1,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 14245,
      "cache_read_input_tokens": 18443,
      "output_tokens": 1112,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 14245
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 1112,
          "cache_read_input_tokens": 18443,
          "cache_creation_input_tokens": 14245,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 14245,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 1,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  }
}
````

</details>

---

### System

_source line 30_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "ac52294b4d40fe0d9",
  "tool_use_id": "toolu_016cLANJVDSeHpFC5Ng7XfBw",
  "status": "completed",
  "output_file": "",
  "summary": "Read MEPIC survey for NoPE",
  "usage": {
    "total_tokens": 27371,
    "tool_uses": 1,
    "duration_ms": 19850
  },
  "uuid": "36e640de-43b9-4923-9485-7068b12c29d4",
  "session_id": "fdf71b47-8f0f-4233-b6c0-f01ae22a3454"
}
```

---

### Tool result

_source line 31 · 2026-05-14T05:14:10.556Z_

<details><summary>↩ Tool result · `toolu_016cLANJVDSeHpFC5Ng7XfBw`</summary>

````text
Perfect! I've read the MEPIC survey file. Here's a comprehensive summary of the key implementation details:

## MEPIC NoPE Implementation Details

### 1. **NoPE KV Storage**

The core innovation is storing KV cache in "NoPE" (No Positional Encoding) format:

**Standard approach:**
```python
Q, K, V = proj(hidden_states)
Q_rope, K_rope = apply_rotary_pos_emb(Q, K, cos, sin)  # RoPE applied to both
cache.update(K_rope, V)  # Stores post-RoPE keys
attn = softmax(Q_rope @ K_rope^T / sqrt(d)) @ V
```

**MEPIC NoPE approach:**
```python
Q, K, V = proj(hidden_states)
Q_rope = apply_rotary_pos_emb(Q, cos, sin)  # Only Q gets RoPE
cache.update(K, V)  # Stores pre-RoPE keys (NoPE format)
# RoPE applied dynamically in fused kernel during attention
attn = fused_rope_attention(Q_rope, K_nope, V, position_offsets)
```

**Key insight**: Since KV cache lacks position information, the same chunk can be reused at any position without loss of correctness. This is mathematically valid because: `⟨RoPE(q, m), RoPE(k, n)⟩ = ⟨RoPE(q, m-n), k⟩`

### 2. **Boundary Recomputation (First-Block Strategy)**

MEPIC uses a targeted recomputation approach:

**Rule**: For each cached chunk, **only recompute the first KV block**, reuse subsequent blocks directly.

**Why this works:**
- The first block contains cross-attention boundaries with preceding context (other chunks or prompt)
- Subsequent blocks depend mainly on internal chunk context, relatively position-independent
- Overhead is minimal (1 block ≈ 16 tokens recomputed per chunk)

**Comparison to EPIC LegoLink:**

| Aspect | EPIC LegoLink | MEPIC First-Block |
|--------|---|---|
| Granularity | Token-level (first k tokens) | Block-level (first block) |
| Strategy | Static: k ≤ 32 | Fixed: 1 block |
| Complexity | O(kN) | O(B) where B = block_size |
| Storage | Post-RoPE | NoPE |

### 3. **Monkey-Patching / Hook Points**

The implementation requires modifying 4 key locations in HuggingFace transformers:

**a) Separate Q/K RoPE application** (apply_rotary_pos_emb):
```python
if use_nope_kv:
    query_states = apply_rotary_pos_emb_query_only(query_states, cos, sin)
    # key_states stays NoPE
else:
    query_states, key_states = apply_rotary_pos_emb(query_states, key_states, cos, sin)
```

**b) KV Cache storage** (unchanged from user's perspective, since keys are already NoPE)

**c) Attention computation** (dynamic RoPE application):
```python
def nope_attention(query_states, key_states, value_states, cos_full, sin_full):
    # Apply RoPE to NoPE keys dynamically
    key_states_rope = apply_rotary_pos_emb_key_only(key_states, cos_full, sin_full)
    attn_weights = torch.matmul(query_states, key_states_rope.transpose(-2, -1)) / math.sqrt(d)
    attn_weights = F.softmax(attn_weights, dim=-1)
    attn_output = torch.matmul(attn_weights, value_states)
    return attn_output
```

**d) Helper functions:**
```python
def apply_rotary_pos_emb_query_only(q, cos, sin):
    return (q * cos) + (rotate_half(q) * sin)

def apply_rotary_pos_emb_key_only(k, cos, sin):
    return (k * cos) + (rotate_half(k) * sin)

def remove_rotary_pos_emb(k_rope, cos, sin):
    """Recover NoPE key from post-RoPE (for cache migration)"""
    return (k_rope * cos) - (rotate_half(k_rope) * sin)
```

### 4. **RoPE Mathematics**

**Forward application (rotation by angle mθ):**
```python
def rotate_half(x):
    x1 = x[..., :x.shape[-1] // 2]
    x2 = x[..., x.shape[-1] // 2:]
    return torch.cat((-x2, x1), dim=-1)

def apply_rotary_pos_emb(q, k, cos, sin):
    q_embed = (q * cos) + (rotate_half(q) * sin)
    k_embed = (k * cos) + (rotate_half(k) * sin)
    return q_embed, k_embed
```

**Reverse operation (undo RoPE via inverse rotation):**
```python
def remove_rotary_pos_emb(k_rope, cos, sin):
    k_nope = (k_rope * cos) + (rotate_half(k_rope) * (-sin))
    # Equivalent to: (k_rope * cos) - (rotate_half(k_rope) * sin)
```

### 5. **Fused RoPE-Attention Kernel (Pseudocode)**

```c
for each query token at position m:
    for each key block at position range [n_start, n_end]:
        K_nope = load_from_hbm(block_id)
        for each key at position n in [n_start, n_end]:
            K_rope[n] = apply_rope(K_nope[n], cos[n], sin[n])
        score = Q_rope[m] @ K_rope^T / sqrt(d)
```

### 6. **Boundary Recomputation Implementation Pattern**

```python
class BoundaryRecomputer:
    def recompute_first_block(self, chunk_kv, prefix_hidden_states, chunk_tokens):
        first_block_tokens = chunk_tokens[:self.block_size]
        combined_input = concat(prefix_hidden_states, first_block_tokens)
        new_kv = self.model.forward_partial(combined_input)
        chunk_kv[:, :, :self.block_size, :] = new_kv[:, :, -self.block_size:, :]
        return chunk_kv
```

### 7. **Implementation Estimate**

| Component | Lines | Difficulty |
|-----------|-------|-----------|
| NoPE KV storage (Q-only RoPE) | 50 | Low |
| Dynamic RoPE attention | 80 | Medium |
| Boundary recomputation | 150 | Medium |
| RoPE remove/restore utilities | 30 | Low |
| Chunk management (segmentation/padding) | 200 | Medium |
| Testing & verification | 200 | Low |
| **Total** | **~710** | **Medium** |

### 8. **Key Compatibility with KVTC**

Both MEPIC and KVTC are built on RoPE-free keys:
- MEPIC generates NoPE KV (stores without RoPE)
- KVTC removes RoPE before PCA compression
- **Synergy**: MEPIC output can directly feed into KVTC compression without extra processing

The survey file location is: `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/distill_kv_rag_cache/artifacts/mepic_survey.md`
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fdf71b47-8f0f-4233-b6c0-f01ae22a3454",
  "uuid": "4a6ffbce-00d9-44ba-8745-6d6de3ce6aff",
  "tool_use_result": {
    "status": "completed",
    "prompt": "Read the MEPIC survey file at /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/distill_kv_rag_cache/artifacts/mepic_survey.md to understand the MEPIC NoPE implementation details. Report back: how NoPE KV storage works, how boundary recomputation works, monkey-patching approach, and any code snippets.",
    "agentId": "ac52294b4d40fe0d9",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! I've read the MEPIC survey file. Here's a comprehensive summary of the key implementation details:\n\n## MEPIC NoPE Implementation Details\n\n### 1. **NoPE KV Storage**\n\nThe core innovation is storing KV cache in \"NoPE\" (No Positional Encoding) format:\n\n**Standard approach:**\n```python\nQ, K, V = proj(hidden_states)\nQ_rope, K_rope = apply_rotary_pos_emb(Q, K, cos, sin)  # RoPE applied to both\ncache.update(K_rope, V)  # Stores post-RoPE keys\nattn = softmax(Q_rope @ K_rope^T / sqrt(d)) @ V\n```\n\n**MEPIC NoPE approach:**\n```python\nQ, K, V = proj(hidden_states)\nQ_rope = apply_rotary_pos_emb(Q, cos, sin)  # Only Q gets RoPE\ncache.update(K, V)  # Stores pre-RoPE keys (NoPE format)\n# RoPE applied dynamically in fused kernel during attention\nattn = fused_rope_attention(Q_rope, K_nope, V, position_offsets)\n```\n\n**Key insight**: Since KV cache lacks position information, the same chunk can be reused at any position without loss of correctness. This is mathematically valid because: `⟨RoPE(q, m), RoPE(k, n)⟩ = ⟨RoPE(q, m-n), k⟩`\n\n### 2. **Boundary Recomputation (First-Block Strategy)**\n\nMEPIC uses a targeted recomputation approach:\n\n**Rule**: For each cached chunk, **only recompute the first KV block**, reuse subsequent blocks directly.\n\n**Why this works:**\n- The first block contains cross-attention boundaries with preceding context (other chunks or prompt)\n- Subsequent blocks depend mainly on internal chunk context, relatively position-independent\n- Overhead is minimal (1 block ≈ 16 tokens recomputed per chunk)\n\n**Comparison to EPIC LegoLink:**\n\n| Aspect | EPIC LegoLink | MEPIC First-Block |\n|--------|---|---|\n| Granularity | Token-level (first k tokens) | Block-level (first block) |\n| Strategy | Static: k ≤ 32 | Fixed: 1 block |\n| Complexity | O(kN) | O(B) where B = block_size |\n| Storage | Post-RoPE | NoPE |\n\n### 3. **Monkey-Patching / Hook Points**\n\nThe implementation requires modifying 4 key locations in HuggingFace transformers:\n\n**a) Separate Q/K RoPE application** (apply_rotary_pos_emb):\n```python\nif use_nope_kv:\n    query_states = apply_rotary_pos_emb_query_only(query_states, cos, sin)\n    # key_states stays NoPE\nelse:\n    query_states, key_states = apply_rotary_pos_emb(query_states, key_states, cos, sin)\n```\n\n**b) KV Cache storage** (unchanged from user's perspective, since keys are already NoPE)\n\n**c) Attention computation** (dynamic RoPE application):\n```python\ndef nope_attention(query_states, key_states, value_states, cos_full, sin_full):\n    # Apply RoPE to NoPE keys dynamically\n    key_states_rope = apply_rotary_pos_emb_key_only(key_states, cos_full, sin_full)\n    attn_weights = torch.matmul(query_states, key_states_rope.transpose(-2, -1)) / math.sqrt(d)\n    attn_weights = F.softmax(attn_weights, dim=-1)\n    attn_output = torch.matmul(attn_weights, value_states)\n    return attn_output\n```\n\n**d) Helper functions:**\n```python\ndef apply_rotary_pos_emb_query_only(q, cos, sin):\n    return (q * cos) + (rotate_half(q) * sin)\n\ndef apply_rotary_pos_emb_key_only(k, cos, sin):\n    return (k * cos) + (rotate_half(k) * sin)\n\ndef remove_rotary_pos_emb(k_rope, cos, sin):\n    \"\"\"Recover NoPE key from post-RoPE (for cache migration)\"\"\"\n    return (k_rope * cos) - (rotate_half(k_rope) * sin)\n```\n\n### 4. **RoPE Mathematics**\n\n**Forward application (rotation by angle mθ):**\n```python\ndef rotate_half(x):\n    x1 = x[..., :x.shape[-1] // 2]\n    x2 = x[..., x.shape[-1] // 2:]\n    return torch.cat((-x2, x1), dim=-1)\n\ndef apply_rotary_pos_emb(q, k, cos, sin):\n    q_embed = (q * cos) + (rotate_half(q) * sin)\n    k_embed = (k * cos) + (rotate_half(k) * sin)\n    return q_embed, k_embed\n```\n\n**Reverse operation (undo RoPE via inverse rotation):**\n```python\ndef remove_rotary_pos_emb(k_rope, cos, sin):\n    k_nope = (k_rope * cos) + (rotate_half(k_rope) * (-sin))\n    # Equivalent to: (k_rope * cos) - (rotate_half(k_rope) * sin)\n```\n\n### 5. **Fused RoPE-Attention Kernel (Pseudocode)**\n\n```c\nfor each query token at position m:\n    for each key block at position range [n_start, n_end]:\n        K_nope = load_from_hbm(block_id)\n        for each key at position n in [n_start, n_end]:\n            K_rope[n] = apply_rope(K_nope[n], cos[n], sin[n])\n        score = Q_rope[m] @ K_rope^T / sqrt(d)\n```\n\n### 6. **Boundary Recomputation Implementation Pattern**\n\n```python\nclass BoundaryRecomputer:\n    def recompute_first_block(self, chunk_kv, prefix_hidden_states, chunk_tokens):\n        first_block_tokens = chunk_tokens[:self.block_size]\n        combined_input = concat(prefix_hidden_states, first_block_tokens)\n        new_kv = self.model.forward_partial(combined_input)\n        chunk_kv[:, :, :self.block_size, :] = new_kv[:, :, -self.block_size:, :]\n        return chunk_kv\n```\n\n### 7. **Implementation Estimate**\n\n| Component | Lines | Difficulty |\n|-----------|-------|-----------|\n| NoPE KV storage (Q-only RoPE) | 50 | Low |\n| Dynamic RoPE attention | 80 | Medium |\n| Boundary recomputation | 150 | Medium |\n| RoPE remove/restore utilities | 30 | Low |\n| Chunk management (segmentation/padding) | 200 | Medium |\n| Testing & verification | 200 | Low |\n| **Total** | **~710** | **Medium** |\n\n### 8. **Key Compatibility with KVTC**\n\nBoth MEPIC and KVTC are built on RoPE-free keys:\n- MEPIC generates NoPE KV (stores without RoPE)\n- KVTC removes RoPE before PCA compression\n- **Synergy**: MEPIC output can directly feed into KVTC compression without extra processing\n\nThe survey file location is: `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/distill_kv_rag_cache/artifacts/mepic_survey.md`"
      }
    ],
    "totalDurationMs": 19852,
    "totalTokens": 29348,
    "totalToolUseCount": 1,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 8909,
      "cache_read_input_tokens": 18450,
      "output_tokens": 1984,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8909
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 1984,
          "cache_read_input_tokens": 18450,
          "cache_creation_input_tokens": 8909,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8909,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 1,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  }
}
````

</details>

---

### Assistant

_source line 32_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the context needed. Let me create the directory structure and write all the files. I'll write them in parallel where possible.

Let me plan the files:

1. `compresslink/__init__.py`
2. `compresslink/rope_utils.py` - RoPE utilities
3. `compresslink/nope_kv.py` - MEPIC NoPE KV storage
4. `compresslink/boundary_recomp.py` - Boundary recomputation
5. `compresslink/raba.py` - RABA


6. `compresslink/cegr.py` - CEGR-MSE
7. `compresslink/query_probe.py` - ProphetKV query probe
8. `compresslink/pipeline.py` - Main pipeline
9. `compresslink/eval_runner.py` - Evaluation script
10. `configs/mvp_config.yaml`
11. `tests/test_rope_utils.py`
12. `tests/test_raba.py`
13. `tests/test_pipeline.py`
14. `requirements.txt`
15. `README.md`

Now I'll start writing all these files, being careful about implementation details and making sure everything integrates properly.

I'm reviewing the KVTC module structure from the survey to understand the API I need to work with - there are bit allocation functions in quantize.py and gpu_ops.py, PCA and RoPE operations in pca.py, compress/decompress in pipeline.py, and data structures in common.py. Since I don't have the exact import paths, I'll create an adapter layer that wraps the KVTC functionality so the rest of the codebase can use it cleanly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fdf71b47-8f0f-4233-b6c0-f01ae22a3454",
  "uuid": "6d793a69-10e0-450c-8994-0c391fdddc65",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VjNS3QdDHZztvCN7ZovNff",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1139,
      "cache_creation_input_tokens": 4053,
      "cache_read_input_tokens": 27492,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4053
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

_source line 33_

Now I have all the API details. Let me create the directory structure and write all files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fdf71b47-8f0f-4233-b6c0-f01ae22a3454",
  "uuid": "21df0bd8-42b2-4863-b640-80c917d9932d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VjNS3QdDHZztvCN7ZovNff",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1139,
      "cache_creation_input_tokens": 4053,
      "cache_read_input_tokens": 27492,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4053
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

_source line 34_

<details open><summary>🔧 Tool call — Bash · `toolu_014hujC66kgbdopVZnKsfVAb`</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/distill_kv_rag_cache/artifacts/compresslink_code/{compresslink,configs,tests}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fdf71b47-8f0f-4233-b6c0-f01ae22a3454",
  "uuid": "cd6ea89f-adbc-449a-b0a4-7d0a667ef778",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VjNS3QdDHZztvCN7ZovNff",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1139,
      "cache_creation_input_tokens": 4053,
      "cache_read_input_tokens": 27492,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4053
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

_source line 35 · 2026-05-14T05:14:24.729Z_

<details><summary>↩ Tool result · `toolu_014hujC66kgbdopVZnKsfVAb`</summary>

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
  "session_id": "fdf71b47-8f0f-4233-b6c0-f01ae22a3454",
  "uuid": "e65f46fe-2cd3-4b25-b92e-ca1f71690205",
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

_source line 36_

Writing all source files now. Starting with the foundation modules in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fdf71b47-8f0f-4233-b6c0-f01ae22a3454",
  "uuid": "2b823a75-0831-40e5-ab1d-27c5ba6bcb67",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GZLUhbEyfMBCPdH5RhdMDV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1751,
      "cache_read_input_tokens": 31545,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1751
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
