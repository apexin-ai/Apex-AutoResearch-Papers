# Research conversation: You need to query the experiment registry for the gen-depth-contamination project to get metrics for domain-specific exp

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 22
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-aa09eae889717e82e.jsonl`
- **Structured JSON:** [`ba4badbc951c3ba893bb.json`](../../sessions/ba/ba4badbc951c3ba893bb.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

22 recorded events

### User

_source line 1 · 2026-05-25T19:45:17.567Z_

You need to query the experiment registry for the gen-depth-contamination project to get metrics for domain-specific experiments. 

Use the tool mcp__agent-ml-research__read_registry with project="gen-depth-contamination", fields=["*"], and pull experiments in batches to find these specific exp_ids:

1. exp_023_domain_ablation (Wiki Qwen)
2. wiki_domain_mistral (Wiki Mistral)
3. wiki_domain_llama (Wiki LLaMA)
4. exp_024_arxiv_domain (arXiv experiments)
5. arxiv_multi_source (arXiv multi-source)
6. code_domain_mistral (Code Mistral)
7. code_domain_qwen7b (Code Qwen-7B)
8. code_domain_olmo (Code OLMo)
9. exp_015_neural_probe (neural probe)
10. seed_gemma27b_c4_s42 (Gemma-27B)
11. exp_pythia69b_c4_depth_chain_v2 (Pythia-6.9B)
12. exp_gemma2b_depth (Gemma-2B)
13. exp_arXiv_qwen1b5_crossscorer (arXiv cross-scorer Qwen)
14. exp_arXiv_llama8b_crossscorer (arXiv cross-scorer LLaMA)
15. exp_arXiv_mistral7b_crossscorer (arXiv cross-scorer Mistral)
16. exp_arXiv_qwen7b_crossscorer (arXiv cross-scorer Qwen-7B)
17. exp_wiki_scorer_confound (Wiki scorer confound)
18. exp_wiki_scorer_confound_1b5 (Wiki scorer confound 1.5B)
19. exp_wiki_qwen7b (Wiki Qwen-7B)
20. exp_wiki_llama8b (Wiki LLaMA-8B)
21. exp_wiki_mistral7b (Wiki Mistral-7B)
22. exp_arXiv_llama8b (arXiv LLaMA-8B)
23. exp_arXiv_mistral7b (arXiv Mistral-7B)
24. exp_arXiv_qwen7b (arXiv Qwen-7B)
25. exp_code_qwen1b5 (Code Qwen-1.5B)
26. exp_code_llama8b (Code LLaMA-8B)
27. exp_code_mistral7b (Code Mistral-7B)
28. exp_code_qwen7b (Code Qwen-7B)
29. olmo_arxiv_cross_scorer (OLMo arXiv cross-scorer)
30. olmo_c4_cross_scorer (OLMo C4 cross-scorer)

The registry returns experiments as a dict keyed by exp_id. Query in batches (limit=30 or so). For each found experiment, report:
- exp_id
- The full metrics dict (especially pairwise AUC values like auc_0v1, auc_1v2, auc_2v3, kstar, etc.)
- Any conclusion or notes

Report ALL metrics found for EACH experiment.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "4b1e9bd3-a514-43a0-8b8b-ee4e7298d832",
  "agentId": "aa09eae889717e82e",
  "type": "user",
  "uuid": "1c0acf07-3b86-449c-a064-6f3880d6fde3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d0900953-8129-4d2a-95a5-2cd8b707bc5a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-25T19:45:17.568Z_

```json
{
  "parentUuid": "1c0acf07-3b86-449c-a064-6f3880d6fde3",
  "isSidechain": true,
  "agentId": "aa09eae889717e82e",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__update_registry"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__update_registry"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "f99cb270-a780-4da0-b442-6d4e2062bd54",
  "timestamp": "2026-05-25T19:45:17.568Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d0900953-8129-4d2a-95a5-2cd8b707bc5a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 3 · 2026-05-25T19:45:19.858Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_018bcqtBFLnejhhBoA2HJyBE`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f99cb270-a780-4da0-b442-6d4e2062bd54",
  "isSidechain": true,
  "agentId": "aa09eae889717e82e",
  "requestId": "req_011CbPrvPoDFzPBshTqzAk9q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "81427b86-a1a0-42be-b4d2-b308784e06b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d0900953-8129-4d2a-95a5-2cd8b707bc5a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01G7xusCepiNFh8S5Be8JDMk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7468,
      "cache_read_input_tokens": 8113,
      "output_tokens": 86,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7468
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 86,
          "cache_read_input_tokens": 8113,
          "cache_creation_input_tokens": 7468,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7468,
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

_source line 4 · 2026-05-25T19:45:19.861Z_

<details><summary>↩ Tool result · `toolu_018bcqtBFLnejhhBoA2HJyBE`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_registry"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "81427b86-a1a0-42be-b4d2-b308784e06b2",
  "isSidechain": true,
  "promptId": "4b1e9bd3-a514-43a0-8b8b-ee4e7298d832",
  "agentId": "aa09eae889717e82e",
  "type": "user",
  "uuid": "4e0305cd-5be2-49c6-bee9-9cd3eb7f127b",
  "sourceToolAssistantUUID": "81427b86-a1a0-42be-b4d2-b308784e06b2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d0900953-8129-4d2a-95a5-2cd8b707bc5a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-25T19:45:22.146Z_

I'll query the registry in batches to find all the specified experiments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4e0305cd-5be2-49c6-bee9-9cd3eb7f127b",
  "isSidechain": true,
  "agentId": "aa09eae889717e82e",
  "requestId": "req_011CbPrvZfHTQ69Uf3snT84H",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dcbaceed-9deb-4630-a246-959b2ef7fe1a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d0900953-8129-4d2a-95a5-2cd8b707bc5a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01RSmLM6wpBotVXJWbYrDe69",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1283,
      "cache_read_input_tokens": 15581,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1283,
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

_source line 6 · 2026-05-25T19:45:22.521Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_019QgVZfMMshQCMum8VuYF8Y`</summary>

```json
{
  "project": "gen-depth-contamination",
  "fields": [
    "*"
  ],
  "limit": 30
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dcbaceed-9deb-4630-a246-959b2ef7fe1a",
  "isSidechain": true,
  "agentId": "aa09eae889717e82e",
  "requestId": "req_011CbPrvZfHTQ69Uf3snT84H",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "29e577c3-a7f5-4bdd-94c7-3c826fec14a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d0900953-8129-4d2a-95a5-2cd8b707bc5a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01RSmLM6wpBotVXJWbYrDe69",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1283,
      "cache_read_input_tokens": 15581,
      "output_tokens": 119,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1283
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 119,
          "cache_read_input_tokens": 15581,
          "cache_creation_input_tokens": 1283,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1283,
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

_source line 7 · 2026-05-25T19:45:23.142Z_

<details><summary>↩ Tool result · `toolu_019QgVZfMMshQCMum8VuYF8Y`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"exp_014_independent_metrics\": {\"status\": \"PENDING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T07:13:38.986Z\", \"updated_at\": \"2026-05-25T16:06:48.657Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo 2>/dev/null; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/gen-depth-contamination && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && CUDA_VISIBLE_DEVICES=1 python scripts/exp014_v1_independent_metrics.py 2>&1 | tee results/exp014_v2/independent_metrics.log && CUDA_VISIBLE_DEVICES=1 python scripts/exp014_v1_independent_analysis.py 2>&1 | tee results/exp014_v2/independent_analysis.log\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:1\"], \"pid\": \"255048\", \"log_path\": \"~/runs/gen-depth-contamination/exp_014_independent_metrics.log\", \"submitted_at\": \"2026-05-25T16:06:48.132Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"hypothesis\": \"补算 6 个与 OBD 15D 特征完全独立的质量指标（GPT-2 Large PPL, MTLD, HD-D, 3/4-gram rep rate, MAUVE, Zipf coefficient），修正 v2 初版的循环论证问题。独立指标与 predicted depth 的 Spearman correlation 应显著（Bonferroni α=0.0083），验证 depth signal 的 ecological validity 不依赖 OBD 自身特征。\", \"parent\": \"exp_014_naturalistic_v2\", \"conclusion\": \"failed\", \"notes\": \"依赖 v2 产出的 cc_predictions.csv，v2 因 FineWeb 下载失败未产出该文件，导致无限 while 循环等待 8h+。PID 234919 已 kill。bash 命令中 $(date) 在构造时被提前展开（每轮打印相同时间戳），需改为单引号转义。\", \"checkpoint_path\": \"N/A (failed, no output)\", \"log_path\": \"~/runs/gen-depth-contamination/exp_014_independent_metrics.log\"}, \"exp_014_naturalistic_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T06:43:51.317Z\", \"updated_at\": \"2026-05-25T15:43:33.328Z\", \"hypothesis\": \"OBD predicted depth 在 wild web text (FineWeb CC-MAIN-2025-26, 50K docs) 上与 6 个完全独立的质量指标（GPT-2 PPL, MTLD, vocd-D, n-gram repetition, MAUVE, Zipf coefficient）显著相关，验证 depth signal 的 ecological validity。Predicted depth 反映文本与 depth-k 生成文本的相似度，而非声称 CC 文本是 prompt-chain 产物。v1 仅测了 4 个指标（binary_auc/freq_entropy/ttr/cc_depth0_ratio），本次完整覆盖 9 指标 + stratified analysis + bootstrap CI。\", \"parent\": \"exp_014_naturalistic\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python scripts/exp014_naturalistic_v2.py\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:1\"], \"pid\": \"233952\", \"log_path\": \"~/runs/gen-depth-contamination/exp_014_naturalistic_v2.log\", \"submitted_at\": \"2026-05-25T06:51:43.798Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"FineWeb CC-MAIN-2025-26 (50K docs streaming)\", \"data_count\": 50000, \"model_name\": \"Qwen2.5-1.5B-Instruct (scorer) + GPT-2 Large (PPL/MAUVE)\", \"seed\": 42, \"checkpoint_source\": \"exp_qwen_cont_10k (OBD LightGBM trained on Qwen continuation features)\", \"eval_data\": \"FineWeb CC-MAIN-2025-26 50K English docs, 50-1000 words, truncated 256 tokens\", \"wall_clock_seconds\": 31906.8, \"gpu_hours\": 8.86}, \"checkpoint_path\": \"N/A (failed, no output)\", \"log_path\": \"results/exp014_v2/run.log\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-25T15:43:30.622Z\", \"notes\": \"FineWeb CC-MAIN-2024-51 streaming 下载失败（Server disconnected），脚本静默退出（exit code 0 但无产出）。错误处理缺失：未 raise RuntimeError。已修复脚本增加异常处理。\"}, \"runtime_benchmark\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T13:11:11.536Z\", \"updated_at\": \"2026-05-25T06:45:44.306Z\", \"spec\": {\"command\": \"python scripts/runtime_benchmark.py\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:0\"], \"pid\": \"232163\", \"log_path\": \"~/runs/gen-depth-contamination/runtime_benchmark.log\", \"submitted_at\": \"2026-05-25T06:37:46.951Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"existing depth chain data\", \"data_count\": 1000, \"model_name\": \"Qwen2.5-1.5B-Instruct + GPT-2 Large + OLMo-1B\", \"seed\": 42, \"wall_clock_seconds\": 289.8, \"gpu_hours\": 0.08}, \"hypothesis\": \"OBD 15D feature extraction + LightGBM classifier 的 per-document inference time 显著低于 neural baselines (Binoculars/DivEye/neural probe)，且 throughput 满足大规模数据审计需求（>100 docs/sec on single GPU）。Reviewer 预期会问计算开销。\", \"conclusion\": \"negative\", \"checkpoint_path\": \"N/A (benchmark, no checkpoint)\", \"log_path\": \"results/runtime_benchmark/run.log\", \"completed_at\": \"2026-05-25T06:42:36.705Z\", \"metrics\": {\"obd_pipeline\": {\"ms_per_doc\": 44.3, \"ms_per_doc_std\": 7.8, \"throughput_docs_per_sec\": 22.6, \"gpu_memory_mb\": 3102, \"breakdown\": {\"scorer_forward_ms\": 20.1, \"cpu_feature_extraction_ms\": 23.4, \"classifier_ms\": 0.77}}, \"binoculars\": {\"ms_per_doc\": 17, \"ms_per_doc_std\": 1.2, \"throughput_docs_per_sec\": 58.8, \"gpu_memory_mb\": 5049}, \"diveye\": {\"ms_per_doc\": 14.2, \"ms_per_doc_std\": 0.2, \"throughput_docs_per_sec\": 70.3, \"gpu_memory_mb\": 3102}, \"neural_probe\": {\"ms_per_doc\": 14.6, \"ms_per_doc_std\": 0.2, \"throughput_docs_per_sec\": 68.3, \"gpu_memory_mb\": 3061}, \"key_finding\": \"OBD ~2.6× slower than baselines due to CPU-side self-BLEU computation (53% of time). But OBD uses less GPU memory than Binoculars (3.1 vs 5.0 GB) and provides 15D interpretable features + ordinal depth estimation vs binary-only detection. 22.6 docs/s = 50K docs in ~37min, practical for large-scale auditing.\"}, \"notes\": \"Hypothesis 被证伪：OBD 44.3ms/doc 是最慢方法（vs DivEye 14.2ms, Neural Probe 14.6ms, Binoculars 17.0ms），throughput 22.6 docs/s 未达假设的 >100 docs/s。瓶颈在 CPU self-BLEU (53%)。Rebuttal framing: OBD trades 2-3× latency for unique depth discrimination capability (K*=2 vs baselines K*=1)，不回避更慢事实，强调功能维度优势。不写入正文，仅 reviewer 显式要求时使用。\"}, \"exp_014_naturalistic\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T11:19:56.644Z\", \"updated_at\": \"2026-05-25T06:43:30.215Z\", \"hypothesis\": \"OBD predicted depth 在 wild web text (FineWeb CC-MAIN-2025-26) 上与独立质量指标（GPT-2 PPL, MTLD, vocd-D, n-gram repetition, MAUVE, Zipf coefficient）显著相关，验证 depth signal 的 ecological validity：depth signal 反映的文本退化模式不仅存在于实验室 prompt-chain，也可在自然 web 文本中观测到。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python /root/autodl-tmp/gen-depth-contamination/scripts/run_naturalistic_validation.py\", \"server\": \"cqa1-22115\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data_exp016_qwen_base/features.csv\", \"data_count\": 5000, \"model_name\": \"Qwen/Qwen2.5-1.5B\", \"seed\": 42, \"checkpoint_path\": \"N/A (eval-only)\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/data/exp014_naturalistic/\"}, \"conclusion\": \"success\", \"metrics\": {\"binary_auc\": 0.9919, \"cc_depth0_ratio\": 0.89, \"freq_entropy_rho\": -0.78, \"ttr_rho\": 0.17, \"note\": \"TTR rho=+0.17 contradicts hypothesis (expected negative). Paper should only report freq_entropy and CC classification, not TTR (or explicitly flag anomalous direction).\"}, \"completed_at\": \"2026-05-20T13:12:42.795Z\"}, \"gemma27b_filtering\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T09:52:09.087Z\", \"updated_at\": \"2026-05-24T11:40:31.003Z\", \"hypothesis\": \"Binary filtering on Gemma-27B generated contaminated text will still outperform no-filter (MMLU degradation ≤1pp), despite 27B text being harder to detect (cross-scorer K*=1, 0v1 AUC=0.887). This validates OBD binary curation robustness against unknown large generators.\", \"spec\": {\"command\": \"python scripts/exp_expanded_downstream_eval.py (adapted for Gemma-27B filtering)\", \"server\": \"cqa1-22115\", \"data_path\": \"data/exp_gemma27b_c4/ (5000 Gemma-27B generated docs)\", \"data_count\": \"5000 docs, 9 runs (3 strategies x 3 seeds)\", \"model_name\": \"Gemma-2-27B (generator) + Qwen2.5-1.5B-Instruct (OBD scorer) + GPT-2 (trainee)\", \"seed\": \"42,123,456\", \"gpu\": \"cuda:3\", \"pid\": \"169724\"}, \"failure_reason\": \"startup recovery: process dead, no active cron monitor\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-24T11:12:46.050Z\", \"metrics\": {\"results_by_strategy\": {\"no_filter\": {\"mmlu_avg\": 0.5956, \"hellaswag_avg\": 0.6633, \"mmlu_seeds\": [0.596, 0.5954, 0.5953], \"hellaswag_seeds\": [0.6638, 0.6636, 0.6626]}, \"binary_ours\": {\"mmlu_avg\": 0.5958, \"hellaswag_avg\": 0.6674, \"mmlu_seeds\": [0.5975, 0.5946, 0.5953], \"hellaswag_seeds\": [0.6775, 0.662, 0.6626]}, \"graduated_a09\": {\"mmlu_avg\": 0.5953, \"hellaswag_avg\": 0.6629, \"mmlu_seeds\": [0.5954, 0.5953, 0.5953], \"hellaswag_seeds\": [0.6636, 0.6626, 0.6626]}}, \"binary_vs_nofilter_delta\": {\"mmlu\": \"+0.02pp\", \"hellaswag\": \"+0.41pp\"}, \"key_finding\": \"OBD binary filtering on Gemma-27B text (cross-scorer K*=1) does not degrade quality: MMLU delta=+0.02pp, HellaSwag delta=+0.41pp. Filter robust against hard-to-detect 27B contamination. Graduated shows no advantage over binary.\"}}, \"code_domain_olmo\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T09:39:27.111Z\", \"updated_at\": \"2026-05-24T11:40:24.803Z\", \"hypothesis\": \"OLMo-1B on Python Code domain will yield K*=1 (competence-limited, similar to Pythia-1.4B on Code) or K*=2 (reaching Code ceiling). Either outcome strengthens the domain ceiling framework: K*=1 confirms competence limitation pattern, K*=2 confirms ceiling universality.\", \"spec\": {\"command\": \"python scripts/run_code_domain_olmo.py\", \"server\": \"cqa1-22115\", \"data_path\": \"data/exp_code_olmo/ (5500 Python code docs x 6 depths)\", \"data_count\": \"5500 docs x 6 depths = 33000 samples\", \"model_name\": \"OLMo-1B (generator) + Qwen2.5-1.5B-Instruct (cross-scorer)\", \"seed\": 42, \"gpu\": \"cuda:1\", \"pid\": \"167297\"}, \"failure_reason\": \"startup recovery: process dead, no active cron monitor\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-24T11:12:41.368Z\", \"metrics\": {\"k_star\": 1, \"pairwise_auc\": {\"0v1\": 0.9996, \"1v2\": 0.5567, \"2v3\": 0.5, \"3v4\": 0.5, \"4v5\": 0.5}, \"pairwise_jsd\": {\"0v1\": 0.334, \"1v2\": 0.006, \"2v3\": 0.003}, \"ordinal_mae\": 1.289, \"ordinal_accuracy\": 0.346, \"scorer\": \"Qwen2.5-1.5B-Instruct\", \"key_finding\": \"OLMo-1B Code K*=1 (competence-limited). 0v1 near-perfect (0.9996) but 1v2=0.5567 below θ. Completes OLMo 3-domain profile: C4=1, arXiv=1, Code=1 — uniformly competence-limited across all domains.\"}}, \"olmo_arxiv_cross_scorer\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T11:00:35.750Z\", \"updated_at\": \"2026-05-24T11:01:18.651Z\", \"hypothesis\": \"OLMo-1B on arXiv with cross-scorer (Qwen-1.5B) will confirm K*=1, consistent with self-scoring. While other models (Qwen, LLaMA, Mistral, Pythia) achieve K*=3 on arXiv, OLMo is competence-limited and cannot sustain distinguishable depth structure beyond generation 1.\", \"conclusion\": \"success\", \"metrics\": {\"k_star\": 1, \"pairwise_auc\": {\"0v1\": 0.9994, \"1v2\": 0.4996, \"2v3\": 0.4971, \"3v4\": 0.5091, \"4v5\": 0.536}, \"bootstrap_ci_95\": {\"0v1\": [0.999, 0.9997], \"1v2\": [0.4828, 0.5166], \"2v3\": [0.4796, 0.5138], \"3v4\": [0.4922, 0.5262], \"4v5\": [0.5183, 0.5533]}, \"p_perm\": {\"0v1\": 0.0001, \"1v2\": 0.51, \"2v3\": 0.6267, \"3v4\": 0.1488, \"4v5\": 0.0001}, \"scorer\": \"Qwen2.5-1.5B-Instruct\", \"key_finding\": \"OLMo-1B arXiv cross-scorer K*=1 confirmed. 1v2=0.4996 (chance). Sole exception to arXiv ceiling=3. All other models (Qwen/LLaMA/Mistral/Pythia) reach K*=3.\"}, \"spec\": {\"command\": \"python scripts/run_olmo_arxiv_cross_scorer.py\", \"server\": \"cqa1-22115\", \"data_path\": \"data/exp_024_arxiv/ (OLMo subset)\", \"data_count\": \"2200 docs x 6 depths\", \"model_name\": \"OLMo-1B + Qwen2.5-1.5B-Instruct (scorer)\", \"seed\": 42, \"gpu\": \"cuda:0\", \"checkpoint_path\": \"results/olmo_arxiv_cross_scorer/\", \"log_path\": \"results/olmo_arxiv_cross_scorer/\"}, \"completed_at\": \"2026-05-24T11:01:18.651Z\"}, \"olmo_c4_cross_scorer\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T10:59:03.914Z\", \"updated_at\": \"2026-05-24T10:59:48.614Z\", \"hypothesis\": \"OLMo-1B on C4 with cross-scorer (Qwen-1.5B) will confirm K*=1, matching self-scoring result. This validates OLMo as competence-limited on C4 (ceiling=2 but OLMo only reaches K*=1), completing the OLMo domain profile for the weak model exception narrative.\", \"metrics\": {\"k_star\": 1, \"pairwise_auc\": {\"0v1\": 0.986, \"1v2\": 0.4999, \"2v3\": 0.4982, \"3v4\": 0.5016, \"4v5\": 0.4946}, \"bootstrap_ci_95\": {\"0v1\": [0.9842, 0.9877], \"1v2\": [0.4885, 0.5112], \"2v3\": [0.4869, 0.5096], \"3v4\": [0.4903, 0.513], \"4v5\": [0.483, 0.506]}, \"p_perm\": {\"0v1\": 0.0001, \"1v2\": 0.5056, \"2v3\": 0.6286, \"3v4\": 0.3955, \"4v5\": 0.8183}, \"scorer\": \"Qwen2.5-1.5B-Instruct\", \"key_finding\": \"OLMo-1B C4 cross-scorer K*=1. 1v2=0.4999 (chance). Consistent across 3 pipelines. Confirms OLMo as competence-limited weak model.\"}, \"conclusion\": \"success\", \"spec\": {\"command\": \"python scripts/run_olmo_c4_cross_scorer.py\", \"server\": \"cqa1-22115\", \"data_path\": \"data/exp_olmo1b_10k/ (reused OLMo C4 data)\", \"data_count\": \"5000 docs x 6 depths\", \"model_name\": \"OLMo-1B + Qwen2.5-1.5B-Instruct (scorer)\", \"seed\": 42, \"gpu\": \"cuda:2\", \"checkpoint_path\": \"results/olmo_c4_cross_scorer/\", \"log_path\": \"results/olmo_c4_cross_scorer/\"}, \"completed_at\": \"2026-05-24T10:59:48.614Z\"}, \"arxiv_multi_source\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T08:26:09.176Z\", \"updated_at\": \"2026-05-24T10:58:24.019Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/gen-depth-contamination && python scripts/run_arxiv_multi_source_1b5.py\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:0\"], \"pid\": \"165918\", \"log_path\": \"~/runs/gen-depth-contamination/arxiv_multi_source.log\", \"submitted_at\": \"2026-05-24T09:15:24.821Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/exp_024_arxiv/ (2200 docs × 6 depths × 3 generators)\", \"data_count\": \"2200 docs × 6 depths × 3 models = 39600 samples\", \"model_name\": \"Pythia-1.4B + OLMo-1B + Qwen-1.5B (generators), Qwen2.5-1.5B-Instruct (scorer)\", \"seed\": 42, \"checkpoint_path\": \"results/arxiv_multi_source/\", \"wall_clock_seconds\": 3422.1, \"gpu_hours\": 0.95}, \"conclusion\": \"success\", \"hypothesis\": \"ArXiv domain K*=3 is domain-intrinsic (not model-specific): Pythia-1.4B and OLMo-1B on arXiv will also yield K*=3 (matching Qwen-1.5B exp-024), confirming that formulaic academic text structure creates larger per-generation distributional shifts that sustain one additional discriminable depth level beyond web text K*=2.\", \"metrics\": {\"k_star\": 3, \"pairwise_auc\": {\"0v1\": 0.9948, \"1v2\": 0.8581, \"2v3\": 0.6436, \"3v4\": 0.544, \"4v5\": 0.5299}, \"bootstrap_ci_bonf_qwen\": {\"2v3\": [0.629, 0.6587]}, \"bootstrap_ci_bonf_pythia\": {\"2v3\": [0.6338, 0.6626]}, \"bootstrap_ci_bonf_pooled\": {\"2v3\": [0.6466, 0.6666]}, \"per_model_2v3_auc\": {\"Qwen-1.5B\": 0.6437, \"Pythia-1.4B\": 0.6484, \"Pooled\": 0.6565}, \"bonf_p_all\": \"<0.005\", \"scorer\": \"Qwen2.5-1.5B-Instruct\", \"key_finding\": \"K*=3 statistically confirmed across all configs. Per-model: Qwen 2v3 CI [0.629,0.659], Pythia 2v3 CI [0.634,0.663], Pooled 2v3 CI [0.647,0.667]. All CI lower > θ=0.60.\"}, \"completed_at\": \"2026-05-24T10:12:26.970Z\"}, \"wiki_domain_llama\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T09:46:34.758Z\", \"updated_at\": \"2026-05-24T10:36:29.902Z\", \"hypothesis\": \"LLaMA-3.1-8B on Wikipedia will yield K*=1 (scorer-controlled), consistent with all other models on Wiki. Combined with C4 K*=2 and arXiv K*=3, this completes a 3-domain profile showing the same monotonic domain ceiling pattern as Mistral.\", \"metrics\": {\"k_star\": 1, \"pairwise_auc\": {\"0v1\": 0.9321, \"1v2\": 0.5919, \"2v3\": 0.5379, \"3v4\": 0.5105, \"4v5\": 0.5051}, \"bootstrap_ci_bonf\": {\"0v1\": [0.926, 0.938], \"1v2\": [0.5788, 0.6049], \"2v3\": [0.524, 0.5514], \"3v4\": [0.4962, 0.5244], \"4v5\": [0.4908, 0.5193]}, \"bonf_p\": {\"0v1\": 0.0005, \"1v2\": 0.0005, \"2v3\": 0.0005, \"3v4\": 0.231, \"4v5\": 1}, \"scorer\": \"Qwen2.5-1.5B-Instruct\", \"key_finding\": \"LLaMA-8B Wiki K*=1. NOTE: 1v2 AUC=0.5919, Bonf CI upper=0.6049 marginally crosses θ but point estimate < θ. Borderline case — K*=1 by convention.\"}, \"conclusion\": \"success\", \"spec\": {\"command\": \"OBD pipeline on pre-existing LLaMA-8B Wiki data\", \"server\": \"cqa1-22115\", \"data_path\": \"data/exp_wiki_llama8b/\", \"data_count\": \"5000 docs x 6 depths\", \"model_name\": \"LLaMA-3.1-8B + Qwen2.5-1.5B-Instruct (scorer)\", \"seed\": 42, \"checkpoint_path\": \"data/exp_wiki_llama8b/\", \"log_path\": \"data/exp_wiki_llama8b/\"}, \"completed_at\": \"2026-05-24T09:57:17.414Z\"}, \"wiki_domain_mistral\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T09:44:10.196Z\", \"updated_at\": \"2026-05-24T10:36:26.391Z\", \"hypothesis\": \"Mistral-7B on Wikipedia will yield K*=1 (scorer-controlled), completing the first 4-domain profile for a single model (Wiki=1, C4=1, Code=2, arXiv=3). This monotonic domain ceiling staircase within one model family is the strongest single-model evidence for domain-dependent K*.\", \"metrics\": {\"k_star\": 1, \"pairwise_auc\": {\"0v1\": 0.9614, \"1v2\": 0.5576, \"2v3\": 0.5193, \"3v4\": 0.5172, \"4v5\": 0.5011}, \"bootstrap_ci_bonf\": {\"0v1\": [0.9571, 0.9654], \"1v2\": [0.5434, 0.5716], \"2v3\": [0.5046, 0.5337], \"3v4\": [0.5029, 0.5317], \"4v5\": [0.4866, 0.5155]}, \"bonf_p\": {\"0v1\": 0.0005, \"1v2\": 0.0005, \"2v3\": 0.002, \"3v4\": 0.01, \"4v5\": 1}, \"scorer\": \"Qwen2.5-1.5B-Instruct\", \"key_finding\": \"Mistral-7B Wiki K*=1 confirmed. 1v2 CI upper=0.5716 < θ=0.60.\"}, \"conclusion\": \"success\", \"spec\": {\"command\": \"OBD pipeline on pre-existing Mistral-7B Wiki data\", \"server\": \"cqa1-22115\", \"data_path\": \"data/exp_wiki_mistral7b/\", \"data_count\": \"5000 docs x 6 depths\", \"model_name\": \"Mistral-7B + Qwen2.5-1.5B-Instruct (scorer)\", \"seed\": 42, \"checkpoint_path\": \"results/exp_wiki_mistral7b/\", \"log_path\": \"results/exp_wiki_mistral7b/\"}, \"completed_at\": \"2026-05-24T09:57:15.436Z\"}, \"code_domain_qwen7b\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T09:48:59.617Z\", \"updated_at\": \"2026-05-24T10:36:23.146Z\", \"hypothesis\": \"Qwen2.5-7B on Python Code domain will yield K*=2 (matching Code ceiling=2 from Qwen-1.5B, LLaMA-8B, Mistral-7B), confirming Code ceiling=2 is scale-invariant within the Qwen family. This fills the last \\\"pending\\\" slot in paper_framing for Code domain.\", \"metrics\": {\"k_star\": 2, \"pairwise_auc\": {\"0v1\": 0.905, \"1v2\": 0.7273, \"2v3\": 0.5367, \"3v4\": 0.5088, \"4v5\": 0.5137}, \"bootstrap_ci_bonf\": {\"0v1\": [0.8985, 0.9118], \"1v2\": [0.7153, 0.7389], \"2v3\": [0.5237, 0.5496], \"3v4\": [0.495, 0.5223], \"4v5\": [0.5002, 0.5274]}, \"bonf_p\": {\"0v1\": 0.0005, \"1v2\": 0.0005, \"2v3\": 0.0005, \"3v4\": 0.295, \"4v5\": 0.0415}, \"scorer\": \"Qwen2.5-1.5B-Instruct\", \"key_finding\": \"Qwen-7B Code K*=2 confirmed. 1v2 AUC=0.7273, well above θ. Scale-invariant within Qwen family.\"}, \"conclusion\": \"success\", \"spec\": {\"command\": \"OBD pipeline on pre-existing Qwen-7B Code data\", \"server\": \"cqa1-22115\", \"data_path\": \"data/exp_code_qwen7b/ (reused from exp_code_qwen7b)\", \"data_count\": \"5500 docs x 6 depths\", \"model_name\": \"Qwen2.5-7B + Qwen2.5-1.5B-Instruct (scorer)\", \"seed\": 42, \"checkpoint_path\": \"results/exp_code_qwen7b/\", \"log_path\": \"results/exp_code_qwen7b/\"}, \"completed_at\": \"2026-05-24T09:57:13.302Z\"}, \"code_domain_mistral\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T09:38:44.455Z\", \"updated_at\": \"2026-05-24T10:36:19.220Z\", \"hypothesis\": \"Mistral-7B on Python Code domain will yield K*=2 (matching Code ceiling=2 from Qwen-1.5B and LLaMA-8B), or K*=1 if competence-limited. Combined with Mistral C4 K*=1 and arXiv K*=3, this would demonstrate domain-dependent K* variation within a single model family.\", \"metrics\": {\"k_star\": 2, \"pairwise_auc\": {\"0v1\": 0.9189, \"1v2\": 0.615, \"2v3\": 0.5292, \"3v4\": 0.5286, \"4v5\": 0.5099}, \"bootstrap_ci_bonf\": {\"0v1\": [0.9127, 0.9251], \"1v2\": [0.6024, 0.6281], \"2v3\": [0.5155, 0.5426], \"3v4\": [0.5152, 0.5418], \"4v5\": [0.4961, 0.5235]}, \"bonf_p\": {\"0v1\": 0.0005, \"1v2\": 0.0005, \"2v3\": 0.0005, \"3v4\": 0.0005, \"4v5\": 0.187}, \"scorer\": \"Qwen2.5-1.5B-Instruct\", \"key_finding\": \"Mistral-7B Code K*=2. Bonferroni CI lower=0.6024 > θ=0.60 — statistically confirmed despite borderline AUC. Domain profile: Wiki=1, C4=1, Code=2, arXiv=3.\"}, \"conclusion\": \"success\", \"spec\": {\"command\": \"OBD pipeline on pre-existing Mistral-7B Code data\", \"server\": \"cqa1-22115\", \"data_path\": \"data/exp_code_mistral7b/\", \"data_count\": \"5500 docs x 6 depths\", \"model_name\": \"Mistral-7B + Qwen2.5-1.5B-Instruct (scorer)\", \"seed\": 42, \"checkpoint_path\": \"results/exp_code_mistral7b/\", \"log_path\": \"results/exp_code_mistral7b/\"}, \"completed_at\": \"2026-05-24T09:57:11.346Z\"}, \"gemma27b_cross_transfer\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T09:41:08.133Z\", \"updated_at\": \"2026-05-24T09:57:19.347Z\", \"hypothesis\": \"Cross-model transfer retention across 18x scale gap (27B to 1.5B) will maintain 80%+ retention, confirming depth signal is text-intrinsic and scale-invariant. OBD classifiers trained on 27B-generated text should generalize to smaller model outputs without retraining.\", \"metrics\": {\"transfer_matrix_accuracy\": {\"Gemma27B→Gemma27B\": 0.3106, \"Gemma27B→LLaMA8B\": 0.3218, \"Gemma27B→Qwen1.5B\": 0.3331, \"Gemma27B→Pythia\": 0.3214, \"Gemma27B→OLMo\": 0.2892, \"LLaMA8B→Gemma27B\": 0.3048, \"Qwen1.5B→Gemma27B\": 0.2693, \"Pythia→Gemma27B\": 0.286, \"OLMo→Gemma27B\": 0.2457}, \"transfer_matrix_mean_auc\": {\"Gemma27B→Gemma27B\": 0.6019, \"Gemma27B→LLaMA8B\": 0.6147, \"Gemma27B→Qwen1.5B\": 0.6274, \"Gemma27B→Pythia\": 0.6166, \"Gemma27B→OLMo\": 0.5934, \"LLaMA8B→Gemma27B\": 0.6037, \"Qwen1.5B→Gemma27B\": 0.5949, \"Pythia→Gemma27B\": 0.5973, \"OLMo→Gemma27B\": 0.5455}, \"retention_27b_to_small\": {\"avg_acc\": \"101.3%\", \"LLaMA8B\": \"103.6%\", \"Qwen1.5B\": \"107.2%\", \"Pythia\": \"103.5%\", \"OLMo\": \"93.1%\"}, \"retention_small_to_27b\": {\"avg_acc\": \"76.5%\", \"LLaMA8B\": \"92.1%\", \"Qwen1.5B\": \"71.3%\", \"Pythia\": \"80.9%\", \"OLMo\": \"77.3%\"}, \"retention_1.5b_inter_model\": \"88.9%\", \"result_path\": \"results/gemma27b_cross_transfer/cross_transfer_gemma27b_matrix.json\", \"key_finding\": \"27B→small retention 101.3% (>100%!): classifier trained on 27B data works BETTER on smaller models. 27B learns universal depth features. Small→27B only 76.5% due to weaker depth signal in 27B text. Strong asymmetry confirms depth signal is text-intrinsic but scale-modulated.\"}, \"conclusion\": \"success\", \"spec\": {\"command\": \"5x5 cross-transfer matrix analysis (CPU)\", \"server\": \"cqa1-22115\", \"data_path\": \"data/exp_gemma27b_c4/ + data from Qwen/Pythia/OLMo/LLaMA\", \"data_count\": \"5x5 model pairs, 5000 docs each\", \"model_name\": \"Gemma-2-27B + 4 smaller models, Qwen2.5-1.5B-Instruct (scorer)\", \"seed\": 42, \"checkpoint_path\": \"results/gemma27b_cross_transfer/\", \"log_path\": \"results/gemma27b_cross_transfer/\"}, \"completed_at\": \"2026-05-24T09:57:19.347Z\"}, \"exp_gemma27b_c4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T07:57:19.726Z\", \"updated_at\": \"2026-05-24T09:13:49.177Z\", \"hypothesis\": \"Gemma-2-27B (27B params, base model) on C4 domain will show slower depth saturation (higher K*) than smaller models due to greater generation capacity, while maintaining the universal depth-dependent distinguishability pattern observed across model families.\", \"metrics\": {\"self_scorer_k_star\": 2, \"self_scorer_pairwise_auc\": {\"0v1\": 0.9695, \"1v2\": 0.6196, \"2v3\": 0.5388, \"3v4\": 0.5069, \"4v5\": 0.5124}, \"self_scorer_bootstrap_ci\": {\"0v1\": {\"auc\": 0.9695, \"ci_lower\": 0.9666, \"ci_upper\": 0.9721, \"perm_p\": 0.0001}, \"1v2\": {\"auc\": 0.6196, \"ci_lower\": 0.6096, \"ci_upper\": 0.6296, \"perm_p\": 0.0001}, \"2v3\": {\"auc\": 0.5388, \"ci_lower\": 0.5279, \"ci_upper\": 0.549, \"perm_p\": 0.0001}, \"3v4\": {\"auc\": 0.5069, \"ci_lower\": 0.4959, \"ci_upper\": 0.5172, \"perm_p\": 0.1099}, \"4v5\": {\"auc\": 0.5124, \"ci_lower\": 0.5012, \"ci_upper\": 0.5234, \"perm_p\": 0.0147}}, \"cross_scorer_k_star\": 1, \"cross_scorer\": \"Qwen2.5-1.5B-Instruct\", \"cross_scorer_pairwise_auc\": {\"0v1\": 0.8871, \"1v2\": 0.5895, \"2v3\": 0.515, \"3v4\": 0.5061, \"4v5\": 0.5108}, \"cross_scorer_bootstrap_ci\": {\"0v1\": {\"auc\": 0.8871, \"ci_lower\": 0.8811, \"ci_upper\": 0.893, \"perm_p\": 0.0001}, \"1v2\": {\"auc\": 0.5895, \"ci_lower\": 0.5795, \"ci_upper\": 0.5997, \"perm_p\": 0.0001}, \"2v3\": {\"auc\": 0.515, \"ci_lower\": 0.5045, \"ci_upper\": 0.5254, \"perm_p\": 0.0027}, \"3v4\": {\"auc\": 0.5061, \"ci_lower\": 0.4952, \"ci_upper\": 0.5165, \"perm_p\": 0.1346}, \"4v5\": {\"auc\": 0.5108, \"ci_lower\": 0.4998, \"ci_upper\": 0.5218, \"perm_p\": 0.0282}}, \"cross_scorer_jsd\": {\"0v1\": 0.0643, \"1v2\": 0.0106, \"2v3\": 0.0049, \"3v4\": 0.0042, \"4v5\": 0.0031}, \"bootstrap_resamples\": 10000, \"permutation_resamples\": 10000, \"key_finding\": \"Self-scorer K*=2 (1v2 CI lower=0.6096>0.60, robust). Cross-scorer K*=1 (1v2 CI upper=0.5997<0.60). 27B scale does NOT elevate K* — consistent with universal K*<=2 for web text. Cross-scorer gap reflects scale mismatch (1.5B scorer vs 27B generator).\"}, \"spec\": {\"command\": \"python scripts/run_gemma27b_depth.py (depth chain + features + bootstrap CI)\", \"server\": \"cqa1-22115\", \"data_path\": \"data/exp_gemma27b_c4/ + data/exp_gemma27b_c4_qwen_scorer/\", \"data_count\": \"5000 docs x 6 depths = 30000 samples\", \"model_name\": \"google/gemma-2-27b (generator) + Qwen2.5-1.5B-Instruct (cross-scorer)\", \"seed\": 42, \"checkpoint_path\": \"N/A (inference only)\", \"log_path\": \"results/exp_gemma27b_c4/\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-24T09:13:49.177Z\"}, \"7b-cross-transfer\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T13:51:00.658Z\", \"updated_at\": \"2026-05-24T09:01:43.476Z\", \"conclusion\": \"success\", \"metrics\": {\"transfer_matrix_accuracy\": {\"Qwen7B→Qwen7B\": 0.378, \"Qwen7B→LLaMA8B\": 0.312, \"LLaMA8B→Qwen7B\": 0.346, \"LLaMA8B→LLaMA8B\": 0.331}, \"transfer_matrix_mae\": {\"Qwen7B→Qwen7B\": 1.169, \"Qwen7B→LLaMA8B\": 1.51, \"LLaMA8B→Qwen7B\": 1.249, \"LLaMA8B→LLaMA8B\": 1.321}, \"transfer_matrix_tau_b\": {\"Qwen7B→Qwen7B\": 0.463, \"Qwen7B→LLaMA8B\": 0.376, \"LLaMA8B→Qwen7B\": 0.418, \"LLaMA8B→LLaMA8B\": 0.383}, \"transfer_matrix_mean_auc\": {\"Qwen7B→Qwen7B\": 0.64, \"Qwen7B→LLaMA8B\": 0.619, \"LLaMA8B→Qwen7B\": 0.635, \"LLaMA8B→LLaMA8B\": 0.62}, \"transfer_retention\": {\"Qwen→LLaMA_acc\": \"82.7%\", \"Qwen→LLaMA_tau\": \"81.2%\", \"Qwen→LLaMA_auc\": \"85.0%\", \"LLaMA→Qwen_acc\": \"104.4%\", \"LLaMA→Qwen_tau\": \"109.3%\", \"LLaMA→Qwen_auc\": \"111.8%\"}, \"key_finding\": \"7B-scale transfer retention 82-85% (Qwen→LLaMA), consistent with 1.5B-scale patterns (80-92%). LLaMA→Qwen >100% because Qwen signal stronger. Cross-scale transfer universality confirmed.\", \"data_source\": \"Qwen-7B from exp_qwen_cont_10k (subsampled 5K), LLaMA-8B from exp-018. Both Qwen2.5-1.5B cross-scored.\", \"result_path\": \"results/7b_cross_transfer_v2/cross_transfer_7b_full_metrics.json\"}, \"spec\": {\"command\": \"python scripts/run_7b_cross_transfer_v2.py\", \"server\": \"cqa1-22115\", \"data_path\": \"data/exp_018_llama8b/features.csv + exp_qwen_cont_10k features\", \"data_count\": \"5000 docs × 6 depths × 2 models\", \"model_name\": \"Qwen2.5-7B + LLaMA-3.1-8B (OBD transfer, no GPU needed)\", \"seed\": 42, \"checkpoint_path\": \"N/A (CPU analysis)\", \"log_path\": \"results/7b_cross_transfer_v2/\"}, \"hypothesis\": \"Cross-model transfer retention at 7B scale (Qwen-7B ↔ LLaMA-8B) will match 1.5B-scale patterns (80-92%), confirming that depth signal is text-intrinsic rather than scale-dependent, and that OBD classifiers trained on one 7B model generalize to another without retraining.\", \"completed_at\": \"2026-05-24T09:01:43.476Z\"}, \"exp_015_neural_probe\": {\"status\": \"DONE\", \"retry_count\": 3, \"created_at\": \"2026-05-13T18:53:34.791Z\", \"updated_at\": \"2026-05-23T11:54:24.971Z\", \"hypothesis\": \"Learned representations (frozen LLM → MLP) 的 K* 是否高于 hand-crafted 15D features？若 K*_neural > K*_15D，说明 15D projection 是 K*=2 的部分原因；若相同，加强 information-theoretic impossibility 论证\", \"notes\": \"v4 completed successfully. 3 models: Pythia K*_neural=2, OLMo K*_neural=2, Qwen-cont K*_neural=3. Neural probe improves 2v3 AUC across all models (Pythia +0.044, OLMo +0.039, Qwen +0.055) but only Qwen-cont self-scorer crosses θ=0.60. EXIT_CODE=129 (SIGHUP after completion) did not affect results.\", \"completed_at\": \"2026-05-14T02:58:02.023Z\", \"failure_reason\": \"CUDA OOM: CUDA out of memory. Tried to allocate 26.00 MiB. GPU 0 has a total capacity of 23.52 GiB of which 20.06 MiB is free. Process 55665 has 13.36 GiB memory in use. Process 56371 has 9.09 GiB memory in use. Including non-PyTorch memory, this process has 1\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"v4 run in progress (PID 108774, tmux: exp015, westc-26893). Root cause of prior failures: v2=OOM (concurrent exp-006 占 GPU), v3=SIGHUP/EXIT_CODE=129 (SSH 断连，未在 tmux 中)。v4 在 tmux 中安全运行，Pythia 86% → OLMo → Qwen-cont → MLP training。内存管理正确 (del+gc+empty_cache)，6.7GB/24GB。ETA ~25-30min from 09:28 UTC.\"}, \"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T09:21:59.744073+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T09:31:39.481148+00:00\"}]}, \"reproduce\": {\"finished_at\": \"2026-05-15T09:31:35.099Z\"}, \"conclusion\": \"success\", \"metrics\": {\"k_star_qwen\": 3, \"k_star_pythia\": 2, \"k_star_olmo\": 1, \"qwen_pairwise_auc\": {\"0v1\": 0.988, \"1v2\": 0.702, \"2v3\": 0.616, \"3v4\": 0.59, \"4v5\": 0.566}, \"pythia_pairwise_auc\": {\"0v1\": 0.966, \"1v2\": 0.676, \"2v3\": 0.596, \"3v4\": 0.555, \"4v5\": 0.532}, \"olmo_pairwise_auc\": {\"0v1\": 0.9773, \"1v2\": 0.5054, \"2v3\": 0.5056, \"3v4\": 0.5032, \"4v5\": 0.4999}, \"olmo_rerun_source\": \"exp015_olmo_rerun/neural_probe_results.json\", \"notes\": \"OLMo values updated from rerun (self-probe). Original cross-model probe had K*=2 (1v2=0.657) but was superseded by self-probe rerun (K*=1, 1v2=0.5054). Paper Table 3 correctly uses rerun values.\"}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/artifacts/exp015_neural_probe_results.json\", \"log_path\": \"~/runs/gen-depth-contamination/exp_015_neural_probe.log\", \"spec\": {\"command\": \"python scripts/run_exp015_neural_probe.py --device cuda:0 --embed_batch_size 8\", \"server\": \"westc-26893\", \"data_path\": \"data_exp001_pythia + data_exp002_olmo + data_exp017_qwen_cont\", \"data_count\": 90000, \"model_name\": \"Qwen/Qwen2.5-1.5B-Instruct (frozen encoder -> MLP probe)\", \"seed\": \"5-fold CV\"}}, \"exp_gemma2b_10k\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T18:00:38.686Z\", \"updated_at\": \"2026-05-23T00:21:06.691Z\", \"hypothesis\": \"Gemma-2-2B 10K sample-size robustness: 5K borderline K*=1 (1v2 AUC=0.5981, just below θ=0.60) should remain K*=1 at 10K, confirming between-sample stability for borderline verdicts. Adds a K*=1 datapoint to the 10K robustness table (currently only K*=2 configs).\", \"spec\": {\"server\": \"cqa1-22115\", \"pid\": 54709, \"gpu\": \"cuda:3\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_gemma2b_10k/\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_gemma2b_10k/run.log\", \"completed_at\": \"2026-05-22T23:16:00.183Z\", \"metrics\": {\"K_star_self\": 2, \"K_star_qwen\": 2, \"scorer\": \"Qwen2.5-1.5B-Instruct (cross-scored)\", \"pairwise_auc_self\": {\"0v1\": 0.9817, \"1v2\": 0.643, \"2v3\": 0.555, \"3v4\": 0.5173, \"4v5\": 0.5101}, \"pairwise_auc_qwen\": {\"0v1\": 0.9533, \"1v2\": 0.6099, \"2v3\": 0.5409, \"3v4\": 0.5174, \"4v5\": 0.5158}, \"bootstrap_ci_1v2\": {\"auc_oof\": 0.6099, \"boot_std\": 0.0034, \"ci_95\": [0.6031, 0.6167], \"ci_995_bonferroni_pct\": [0.5998, 0.6192], \"ci_995_bonferroni_norm\": [0.6003, 0.6196], \"perm_p\": 0.0001, \"bonferroni_pass_pct\": false, \"bonferroni_pass_norm\": true}, \"note\": \"5K K*=1 (1v2=0.5981), 10K Qwen cross-scored K*=2 (1v2=0.6099). Bonferroni split: percentile FAIL (0.5998), normal PASS (0.6003). Extremely borderline.\"}}, \"seed_gemma27b_c4_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T10:05:43.080Z\", \"updated_at\": \"2026-05-23T00:00:23.931Z\", \"spec\": {\"server\": \"cqa1-22115\", \"pid\": 26893, \"gpu\": \"cuda:0\"}, \"conclusion\": \"success\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_gemma27b_c4/run.log\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_gemma27b_c4/\", \"hypothesis\": \"Gemma-2-27B, the largest model tested, will exhibit K*=2 consistent with smaller models, confirming that generational depth saturation is model-scale-invariant for the surprisal-feature OBD pipeline.\", \"completed_at\": \"2026-05-22T23:06:04.697Z\", \"metrics\": {\"K_star\": 1, \"scorer\": \"Qwen2.5-1.5B-Instruct (cross-scored)\", \"pairwise_auc_self\": {\"0v1\": 0.9695, \"1v2\": 0.6196, \"2v3\": 0.5388, \"3v4\": 0.5069, \"4v5\": 0.5124}, \"pairwise_auc_qwen\": {\"0v1\": 0.8874, \"1v2\": 0.5894}, \"note\": \"Self-scored K*=2 (1v2=0.6196), Qwen cross-scored K*=1 (1v2=0.5894 < θ=0.60). Self→Cross inflation: 1v2 Δ=-3.0pp, 0v1 Δ=-8.2pp.\"}}, \"exp_olmo1b_10k\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T20:05:20.014Z\", \"updated_at\": \"2026-05-22T22:34:48.584Z\", \"hypothesis\": \"OLMo-1B on 10K C4 samples will show saturation at depth K*=1, meaning generation-depth signal is only distinguishable between real (depth-0) and first-generation synthetic text, with deeper depths being indistinguishable from each other.\", \"spec\": {\"command\": \"bash /tmp/exp_olmo1b_10k.sh (Phase1: OLMo-1B continuation gen + Phase2: Qwen scorer)\", \"server\": \"cqa1-22115\", \"gpu\": \"cuda:2\", \"pid\": 66415, \"data_path\": \"data/olmo1b_c4_10k\", \"data_count\": 10000, \"model_name\": \"allenai/OLMo-1B-hf (gen) + Qwen2.5-1.5B-Instruct (scorer)\", \"seed\": 42, \"log_path\": \"/tmp/exp_olmo1b_10k.log\", \"checkpoint_path\": \"results/olmo1b_c4_10k/\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T22:34:45.698Z\", \"metrics\": {\"pairwise_auc\": {\"0v1\": 0.9871, \"1v2\": 0.4984, \"2v3\": 0.5059, \"3v4\": 0.5061, \"4v5\": 0.5074}, \"K_star\": 1, \"ordinal_mae\": 1.4145, \"ordinal_accuracy\": 0.3152, \"pairwise_jsd\": {\"0v1\": 0.230018, \"1v2\": 0.001457, \"2v3\": 0.001512, \"3v4\": 0.001413, \"4v5\": 0.001535}, \"top_features\": [\"freq_entropy\", \"surp_d1_mean\", \"freq_kurtosis\", \"surp_d2_mean\", \"surp_d1_skew\"]}}, \"exp_002_olmo_depth\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-12T20:06:24.766Z\", \"updated_at\": \"2026-05-22T22:04:07.552Z\", \"hypothesis\": \"K* 跨模型一致性验证：OLMo-1B 在相同种子数据和解码策略下的 K* 是否与 Qwen2.5-1.5B 一致（K*=2）\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo 2>/dev/null && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_ENDPOINT=https://hf-mirror.com && cd /root/autodl-tmp/gen-depth-contamination && python scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/allenai/OLMo-1B-hf --data_dir /root/autodl-tmp/gen-depth-contamination/data_exp002_olmo --results_dir /root/autodl-tmp/gen-depth-contamination/results_exp002_olmo --num_samples 5000 --max_depth 5 --batch_size 16 --generation_mode continuation\\\"\", \"server\": \"autodl-4090d\", \"gpu\": [\"cuda:0\"], \"pid\": \"20225\", \"log_path\": \"~/runs/gen-depth-contamination/exp_002_olmo_depth.log\", \"submitted_at\": \"2026-05-13T00:16:07.960Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data_exp002_olmo\", \"data_count\": 5000, \"model_name\": \"allenai/OLMo-1B-hf\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/data_exp002_olmo/\", \"wall_clock_seconds\": 8384.9, \"gpu_hours\": 2.33}, \"reproduce\": {\"finished_at\": \"2026-05-13T02:31:18.880Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-13T02:31:19.738113+00:00\"}]}, \"metrics\": {\"k_star\": 1, \"pairwise_auc\": {\"0v1\": 0.9861, \"1v2\": 0.5001, \"2v3\": 0.4972, \"3v4\": 0.5034, \"4v5\": 0.4971}, \"scorer\": \"Qwen2.5-1.5B-Instruct\", \"note\": \"Updated to Qwen cross-scoring (D107). Self-scored 1v2=0.6145 K*=2, Qwen-scored 1v2=0.5001 K*=1.\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T02:35:52.823Z\", \"parent\": \"exp_001_pythia_depth\"}, \"exp_001_pythia_depth\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-12T20:06:23.803Z\", \"updated_at\": \"2026-05-22T22:04:05.591Z\", \"hypothesis\": \"K* 跨模型一致性验证：Pythia-1.4B 在相同种子数据和解码策略下的 K* 是否与 Qwen2.5-1.5B 一致（K*=2）\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo 2>/dev/null && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_ENDPOINT=https://hf-mirror.com && cd /root/autodl-tmp/gen-depth-contamination && python scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/EleutherAI/pythia-1.4b --data_dir /root/autodl-tmp/gen-depth-contamination/data_exp001_pythia --results_dir /root/autodl-tmp/gen-depth-contamination/results_exp001_pythia --num_samples 5000 --max_depth 5 --batch_size 16 --generation_mode continuation\\\"\", \"server\": \"autodl-4090d\", \"gpu\": [\"cuda:0\"], \"pid\": \"17138\", \"log_path\": \"~/runs/gen-depth-contamination/exp_001_pythia_depth.log\", \"submitted_at\": \"2026-05-12T20:50:31.471Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data_exp001_pythia\", \"data_count\": 5000, \"model_name\": \"EleutherAI/pythia-1.4b\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/data_exp001_pythia/\", \"wall_clock_seconds\": 12344.9, \"gpu_hours\": 3.43}, \"conclusion\": \"success\", \"metrics\": {\"k_star\": 2, \"pairwise_auc\": {\"0v1\": 0.9722, \"1v2\": 0.6074, \"2v3\": 0.544, \"3v4\": 0.5051, \"4v5\": 0.5079}, \"pairwise_auc_std\": {\"0v1\": 0.0039, \"1v2\": 0.0078, \"2v3\": 0.0067, \"3v4\": 0.0032, \"4v5\": 0.0101}, \"bootstrap_ci\": {\"1v2\": {\"auc_oof\": 0.6072, \"boot_mean\": 0.6073, \"boot_std\": 0.005, \"ci_95\": [0.5975, 0.6172], \"ci_995_bonferroni\": [0.5934, 0.621], \"perm_p\": 0.0001, \"bonferroni_pass\": false}}, \"scorer\": \"Qwen2.5-1.5B-Instruct\", \"note\": \"Updated to Qwen cross-scoring (D107). Self-scored 1v2=0.6539, Qwen-scored 1v2=0.6074.\"}, \"completed_at\": \"2026-05-13T00:16:16.359Z\"}, \"exp_llama8b_10k\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T09:25:55.895Z\", \"updated_at\": \"2026-05-22T20:26:09.870Z\", \"hypothesis\": \"增加 LLaMA-8B C4 样本量从 5k→10k 可将 1v2 bootstrap std 缩小 ~√2 倍，使 Bonferroni 99.5% CI lower bound 恢复到 θ=0.60 以上\", \"spec\": {\"server\": \"cqa1-22115\", \"pid\": 23232, \"checkpoint_path\": \"results/exp_llama8b_10k/\", \"log_path\": \"/tmp/exp_llama8b_10k.log\"}, \"conclusion\": \"negative\", \"metrics\": {\"K_star\": 1, \"AUC_0v1\": 0.9282, \"AUC_1v2\": 0.6148, \"AUC_1v2_oof\": 0.588, \"AUC_2v3\": 0.5247, \"AUC_3v4\": 0.5519, \"AUC_4v5\": 0.5262, \"bootstrap_1v2_oof_auc\": 0.588, \"bootstrap_1v2_95CI\": [0.5809, 0.595], \"bootstrap_1v2_995CI_bonferroni\": [0.5776, 0.5978], \"bonferroni_pass\": false, \"perm_pvalue_1v2\": 0.0001, \"scorer\": \"Qwen2.5-1.5B-Instruct\", \"note\": \"All pairwise AUC from Qwen cross-scoring (Phase 2). Pipeline AUC 1v2=0.6148 (mean-of-folds).\"}, \"completed_at\": \"2026-05-22T19:21:09.215Z\"}, \"exp_pythia14b_c4_10k\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T11:57:18.681Z\", \"updated_at\": \"2026-05-22T14:59:24.436Z\", \"hypothesis\": \"统一所有 K*=2 configs 的样本量至 10K，避免 selective precision boosting 质疑。Pythia-1.4B 5K 已稳定通过 Bonferroni (CI_lower≈0.641>0.60)，10K 为一致性验证。\", \"spec\": {\"command\": \"python3 scripts/run_pipeline.py --model_path pythia-1.4b --num_samples 10000 --max_depth 5 --batch_size 32 --generation_mode continuation + Phase2 Qwen scorer\", \"server\": \"cqa1-22115\", \"gpu\": \"cuda:3 (RTX PRO 6000 Blackwell 96GB)\", \"data_path\": \"data/exp_pythia14b_c4_10k\", \"data_count\": 10000, \"model_name\": \"Pythia-1.4B (gen) + Qwen2.5-1.5B-Instruct (scorer)\", \"seed\": 42, \"log_path\": \"/tmp/exp_pythia14b_c4_10k.log\", \"checkpoint_path\": \"results/exp_pythia14b_c4_10k/\"}, \"metrics\": {\"K_star\": 2, \"AUC_0v1\": 0.9712, \"AUC_1v2\": 0.6175, \"AUC_2v3\": 0.5364, \"AUC_3v4\": 0.5134, \"AUC_4v5\": 0.5088, \"bootstrap_1v2_95CI\": [0.6108, 0.6242], \"bootstrap_1v2_995CI_bonferroni\": [0.6078, 0.6273], \"perm_pvalue_1v2\": 0.0001, \"bonferroni_pass\": true, \"top_feature\": \"freq_entropy\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T14:14:41.623Z\"}, \"exp_qwen_cont_10k\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T09:27:38.591Z\", \"updated_at\": \"2026-05-22T14:59:22.490Z\", \"hypothesis\": \"增加 Qwen-cont C4 样本量从 5k→10k 可将 1v2 bootstrap std 缩小 ~√2 倍，使 Bonferroni 99.5% CI lower bound 恢复到 θ=0.60 以上\", \"spec\": {\"command\": \"bash /tmp/run_qwen_cont_10k.sh (Phase1: base generation + Phase2: instruct scoring)\", \"server\": \"cqa1-22115\", \"gpu\": \"cuda:1 (RTX PRO 6000 Blackwell 96GB)\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/exp_qwen_cont_10k\", \"data_count\": 10000, \"model_name\": \"Qwen/Qwen2.5-1.5B (base, continuation) + Qwen/Qwen2.5-1.5B-Instruct (scorer)\", \"seed\": 42, \"checkpoint_path\": \"results/exp_qwen_cont_10k/\", \"log_path\": \"/tmp/exp_qwen_cont_10k_phase1.log\"}, \"metrics\": {\"K_star\": 2, \"AUC_0v1\": 0.9875, \"AUC_1v2\": 0.6346, \"AUC_2v3\": 0.5616, \"AUC_3v4\": 0.5451, \"AUC_4v5\": 0.5254, \"bootstrap_1v2_95CI\": [0.6282, 0.6409], \"bootstrap_1v2_995CI_bonferroni\": [0.6255, 0.6436], \"perm_pvalue_1v2\": 0.0001, \"bonferroni_pass\": true, \"top_feature\": \"freq_entropy\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T14:47:57.847Z\"}, \"exp_pythia14b_10k\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T11:59:05.554Z\", \"updated_at\": \"2026-05-22T12:00:24.157Z\", \"hypothesis\": \"统一所有 K*=2 configs 样本量至 10K，避免 selective precision boosting 质疑。Pythia-1.4B 5K 已稳定通过 Bonferroni (CI_lower≈0.641>0.60)，10K 为一致性验证。\", \"spec\": {\"command\": \"python3 scripts/run_pipeline.py --model_path pythia-1.4b --num_samples 10000 --max_depth 5 --batch_size 32 --generation_mode continuation + Phase2 Qwen scorer\", \"server\": \"cqa1-22115\", \"gpu\": \"cuda:3 (RTX PRO 6000 Blackwell 96GB)\", \"data_path\": \"data/exp_pythia14b_c4_10k\", \"data_count\": 10000, \"model_name\": \"Pythia-1.4B (gen) + Qwen2.5-1.5B-Instruct (scorer)\", \"seed\": 42, \"log_path\": \"N/A\", \"note\": \"重复条目，已合并到 exp_pythia14b_c4_10k\", \"checkpoint_path\": \"N/A\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-22T12:00:24.157Z\"}, \"seed_qwen15b_c4_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T00:34:11.792Z\", \"updated_at\": \"2026-05-22T06:39:21.815Z\", \"hypothesis\": \"Qwen-1.5B C4 的 K*=2 结论在 seed=123 下仍成立（原始 seed=42），验证 OBD 的 depth boundary 不依赖随机种子\", \"spec\": {\"command\": \"run_pipeline.py --generation_mode rewrite --top_p 0.95 --seed 123 (C4)\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:3\"], \"pid\": \"3156\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/results/seed_qwen15b_c4_s123/\", \"submitted_at\": \"2026-05-22T03:58:27.354Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/seed_robustness/seed_qwen15b_c4_s123\", \"data_count\": 5000, \"model_name\": \"Qwen2.5-1.5B-Instruct\", \"seed\": 123, \"metrics\": {\"K_star\": 2, \"auc_0v1\": 0.9956, \"auc_1v2\": 0.7014, \"auc_2v3\": 0.5911, \"auc_3v4\": 0.5405, \"auc_4v5\": 0.5335}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/seed_qwen15b_c4_s123/\", \"wall_clock_seconds\": 9654.5, \"gpu_hours\": 2.68}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T06:39:21.815Z\"}, \"seed_qwen15b_wiki_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T00:34:09.969Z\", \"updated_at\": \"2026-05-22T06:39:19.860Z\", \"hypothesis\": \"Qwen-1.5B WikiText 的 K*=2 结论在 seed=123 下仍成立（原始 seed=42），验证 OBD 的 depth boundary 不依赖随机种子\", \"spec\": {\"command\": \"run_pipeline.py --generation_mode rewrite --top_p 0.95 --seed 123\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:2\"], \"pid\": \"3005\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/results/seed_qwen15b_wiki_s123/\", \"submitted_at\": \"2026-05-22T03:58:25.151Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/seed_robustness/seed_qwen15b_wiki_s123\", \"data_count\": 5000, \"model_name\": \"Qwen2.5-1.5B-Instruct\", \"seed\": 123, \"metrics\": {\"K_star\": 3, \"auc_0v1\": 0.9945, \"auc_1v2\": 0.7059, \"auc_2v3\": 0.6067, \"auc_3v4\": 0.5531, \"auc_4v5\": 0.5292}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/seed_qwen15b_wiki_s123/\", \"wall_clock_seconds\": 9654.7, \"gpu_hours\": 2.68}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-22T06:39:19.860Z\"}, \"seed_pythia14b_wiki_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T00:34:08.091Z\", \"updated_at\": \"2026-05-22T06:39:17.971Z\", \"hypothesis\": \"Pythia-1.4B WikiText 的 K*=2 结论在 seed=123 下仍成立（原始 seed=42），验证 OBD 的 depth boundary 不依赖随机种子\", \"spec\": {\"command\": \"run_pipeline.py --generation_mode continuation --top_p 0.95 --seed 123 (two-phase: Pythia gen + Qwen score)\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:1\"], \"pid\": \"2863\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/results/seed_pythia14b_wiki_s123/\", \"submitted_at\": \"2026-05-22T03:58:22.018Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/seed_robustness/seed_pythia14b_wiki_s123\", \"data_count\": 5000, \"model_name\": \"EleutherAI/pythia-1.4b (generator) + Qwen2.5-1.5B-Instruct (scorer)\", \"seed\": 123, \"metrics\": {\"K_star\": 1, \"auc_0v1\": 0.9751, \"auc_1v2\": 0.5766, \"auc_2v3\": 0.5318, \"auc_3v4\": 0.5175, \"auc_4v5\": 0.527}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/seed_pythia14b_wiki_s123/\", \"wall_clock_seconds\": 9656.0, \"gpu_hours\": 2.68}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T06:39:17.971Z\"}, \"sweep_r10_nofilter\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:16:37.475Z\", \"updated_at\": \"2026-05-22T00:54:53.730Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/gen-depth-contamination && CUDA_VISIBLE_DEVICES=1 python scripts/exp_contamination_rate_sweep.py --rate 10 --strategy no_filter --device cuda:0\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:1\"], \"pid\": \"333215\", \"log_path\": \"~/runs/gen-depth-contamination/sweep_r10_nofilter.log\", \"submitted_at\": \"2026-05-20T17:16:36.869Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}}, \"count\": 30, \"total\": 176, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5065}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "29e577c3-a7f5-4bdd-94c7-3c826fec14a8",
  "isSidechain": true,
  "promptId": "4b1e9bd3-a514-43a0-8b8b-ee4e7298d832",
  "agentId": "aa09eae889717e82e",
  "type": "user",
  "uuid": "51d7e60e-4c5b-450d-b095-afafc974311c",
  "sourceToolAssistantUUID": "29e577c3-a7f5-4bdd-94c7-3c826fec14a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d0900953-8129-4d2a-95a5-2cd8b707bc5a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 8 · 2026-05-25T19:45:26.460Z_

The first batch returned 30 experiments but didn't include most of the target ones. Let me query more batches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "51d7e60e-4c5b-450d-b095-afafc974311c",
  "isSidechain": true,
  "agentId": "aa09eae889717e82e",
  "requestId": "req_011CbPrvoZx6tgKY2YEJvgjH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a1eb6cbd-9982-4e89-af63-db61cac88b1e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d0900953-8129-4d2a-95a5-2cd8b707bc5a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_015gPNoUZL1sf6vhBFXMg8S4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22883,
      "cache_read_input_tokens": 16864,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 22883,
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

_source line 9 · 2026-05-25T19:45:27.505Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_018UVGnyJ5RwGtFWSEnv4nNR`</summary>

```json
{
  "project": "gen-depth-contamination",
  "fields": [
    "*"
  ],
  "limit": 30,
  "filters": {
    "status": "DONE"
  }
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a1eb6cbd-9982-4e89-af63-db61cac88b1e",
  "isSidechain": true,
  "agentId": "aa09eae889717e82e",
  "requestId": "req_011CbPrvoZx6tgKY2YEJvgjH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "53a3fd63-b735-467f-84c3-dc3414b8c25c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d0900953-8129-4d2a-95a5-2cd8b707bc5a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_015gPNoUZL1sf6vhBFXMg8S4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22883,
      "cache_read_input_tokens": 16864,
      "output_tokens": 152,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 22883
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 152,
          "cache_read_input_tokens": 16864,
          "cache_creation_input_tokens": 22883,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 22883,
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

_source line 10 · 2026-05-25T19:45:28.731Z_

<details><summary>↩ Tool result · `toolu_018UVGnyJ5RwGtFWSEnv4nNR`</summary>

```text
&lt;persisted-output>
Output too large (49.3KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/d0900953-8129-4d2a-95a5-2cd8b707bc5a/tool-results/toolu_018UVGnyJ5RwGtFWSEnv4nNR.txt

Preview (first 2KB):
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"exp_014_naturalistic_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T06:43:51.317Z\", \"updated_at\": \"2026-05-25T15:43:33.328Z\", \"hypothesis\": \"OBD predicted depth 在 wild web text (FineWeb CC-MAIN-2025-26, 50K docs) 上与 6 个完全独立的质量指标（GPT-2 PPL, MTLD, vocd-D, n-gram repetition, MAUVE, Zipf coefficient）显著相关，验证 depth signal 的 ecological validity。Predicted depth 反映文本与 depth-k 生成文本的相似度，而非声称 CC 文本是 prompt-chain 产物。v1 仅测了 4 个指标（binary_auc/freq_entropy/ttr/cc_depth0_ratio），本次完整覆盖 9 指标 + stratified analysis + bootstrap CI。\", \"parent\": \"exp_014_naturalistic\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python scripts/exp014_naturalistic_v2.py\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:1\"], \"pid\": \"233952\", \"log_path\": \"~/runs/gen-depth-contamination/exp_014_naturalistic_v2.log\", \"submitted_at\": \"2026-05-25T06:51:43.798Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"FineWeb CC-MAIN-2025-26 (50K docs streaming)\", \"data_count\": 50000, \"model_name\": \"Qwen2.5-1.5B-Instruct (scorer) + GPT-2 Large (PPL/MAUVE)\", \"seed\": 42, \"checkpoint_source\": \"exp_qwen_cont_10k (OBD LightGBM trained on Qwen continuation features)\", \"eval_data\": \"FineWeb CC-MAIN-2025-26 50K English docs, 50-1000 words, truncated 256 tokens\", \"wall_clock_seconds\": 31906.8, \"gpu_hours\": 8.86}, \"checkpoint_path\": \"N/A (failed, no output)\", \"log_path\": \"results/exp014_v2/run.log\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-25T15:43:30.622Z\", \"notes\": \"FineWeb CC-MAIN-2024-51 streaming 下载失败（Server disconnected），脚本静默退出（exit code 0 但无产出）。错误处理缺失：未 raise RuntimeError。已修复脚本增加异常处理。\"}, \"runtime_benchmark\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T13:11:11.536Z\", \"updated_at\": \"2026-05-25T06:45:44.306Z\", \"spec\": {\"command\": \"python scripts/runtime_benchmark
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "53a3fd63-b735-467f-84c3-dc3414b8c25c",
  "isSidechain": true,
  "promptId": "4b1e9bd3-a514-43a0-8b8b-ee4e7298d832",
  "agentId": "aa09eae889717e82e",
  "type": "user",
  "uuid": "26294707-c3c2-49bb-8b83-f0920632f844",
  "sourceToolAssistantUUID": "53a3fd63-b735-467f-84c3-dc3414b8c25c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d0900953-8129-4d2a-95a5-2cd8b707bc5a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-25T19:45:31.846Z_

The filtered query still returns from newest first. I need to look through more of the registry. Let me read the full saved output and also query with specific exp_ids.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "26294707-c3c2-49bb-8b83-f0920632f844",
  "isSidechain": true,
  "agentId": "aa09eae889717e82e",
  "requestId": "req_011CbPrwDStKvpjYS8jvptzw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1a908671-b41f-416d-a8eb-b4157b11e809",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d0900953-8129-4d2a-95a5-2cd8b707bc5a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01YQG9NkPjfYf2NwskJatxdd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1180,
      "cache_read_input_tokens": 39747,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1180,
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

_source line 12 · 2026-05-25T19:45:32.520Z_

<details open><summary>🔧 Tool call — Read · `toolu_018x9j8zcPTKzG7V89igH2is`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/d0900953-8129-4d2a-95a5-2cd8b707bc5a/tool-results/toolu_018UVGnyJ5RwGtFWSEnv4nNR.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1a908671-b41f-416d-a8eb-b4157b11e809",
  "isSidechain": true,
  "agentId": "aa09eae889717e82e",
  "requestId": "req_011CbPrwDStKvpjYS8jvptzw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6c12b7bd-9dd0-4e58-ab88-81f50b68b29d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d0900953-8129-4d2a-95a5-2cd8b707bc5a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01YQG9NkPjfYf2NwskJatxdd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1180,
      "cache_read_input_tokens": 39747,
      "output_tokens": 183,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1180
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 183,
          "cache_read_input_tokens": 39747,
          "cache_creation_input_tokens": 1180,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1180,
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

_source line 13 · 2026-05-25T19:45:32.865Z_

<details><summary>↩ Tool result · `toolu_018x9j8zcPTKzG7V89igH2is`</summary>

```text
1	{"result":"{\"success\": true, \"data\": {\"experiments\": {\"exp_014_naturalistic_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T06:43:51.317Z\", \"updated_at\": \"2026-05-25T15:43:33.328Z\", \"hypothesis\": \"OBD predicted depth 在 wild web text (FineWeb CC-MAIN-2025-26, 50K docs) 上与 6 个完全独立的质量指标（GPT-2 PPL, MTLD, vocd-D, n-gram repetition, MAUVE, Zipf coefficient）显著相关，验证 depth signal 的 ecological validity。Predicted depth 反映文本与 depth-k 生成文本的相似度，而非声称 CC 文本是 prompt-chain 产物。v1 仅测了 4 个指标（binary_auc/freq_entropy/ttr/cc_depth0_ratio），本次完整覆盖 9 指标 + stratified analysis + bootstrap CI。\", \"parent\": \"exp_014_naturalistic\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python scripts/exp014_naturalistic_v2.py\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:1\"], \"pid\": \"233952\", \"log_path\": \"~/runs/gen-depth-contamination/exp_014_naturalistic_v2.log\", \"submitted_at\": \"2026-05-25T06:51:43.798Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"FineWeb CC-MAIN-2025-26 (50K docs streaming)\", \"data_count\": 50000, \"model_name\": \"Qwen2.5-1.5B-Instruct (scorer) + GPT-2 Large (PPL/MAUVE)\", \"seed\": 42, \"checkpoint_source\": \"exp_qwen_cont_10k (OBD LightGBM trained on Qwen continuation features)\", \"eval_data\": \"FineWeb CC-MAIN-2025-26 50K English docs, 50-1000 words, truncated 256 tokens\", \"wall_clock_seconds\": 31906.8, \"gpu_hours\": 8.86}, \"checkpoint_path\": \"N/A (failed, no output)\", \"log_path\": \"results/exp014_v2/run.log\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-25T15:43:30.622Z\", \"notes\": \"FineWeb CC-MAIN-2024-51 streaming 下载失败（Server disconnected），脚本静默退出（exit code 0 但无产出）。错误处理缺失：未 raise RuntimeError。已修复脚本增加异常处理。\"}, \"runtime_benchmark\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T13:11:11.536Z\", \"updated_at\": \"2026-05-25T06:45:44.306Z\", \"spec\": {\"command\": \"python scripts/runtime_benchmark.py\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:0\"], \"pid\": \"232163\", \"log_path\": \"~/runs/gen-depth-contamination/runtime_benchmark.log\", \"submitted_at\": \"2026-05-25T06:37:46.951Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"existing depth chain data\", \"data_count\": 1000, \"model_name\": \"Qwen2.5-1.5B-Instruct + GPT-2 Large + OLMo-1B\", \"seed\": 42, \"wall_clock_seconds\": 289.8, \"gpu_hours\": 0.08}, \"hypothesis\": \"OBD 15D feature extraction + LightGBM classifier 的 per-document inference time 显著低于 neural baselines (Binoculars/DivEye/neural probe)，且 throughput 满足大规模数据审计需求（>100 docs/sec on single GPU）。Reviewer 预期会问计算开销。\", \"conclusion\": \"negative\", \"checkpoint_path\": \"N/A (benchmark, no checkpoint)\", \"log_path\": \"results/runtime_benchmark/run.log\", \"completed_at\": \"2026-05-25T06:42:36.705Z\", \"metrics\": {\"obd_pipeline\": {\"ms_per_doc\": 44.3, \"ms_per_doc_std\": 7.8, \"throughput_docs_per_sec\": 22.6, \"gpu_memory_mb\": 3102, \"breakdown\": {\"scorer_forward_ms\": 20.1, \"cpu_feature_extraction_ms\": 23.4, \"classifier_ms\": 0.77}}, \"binoculars\": {\"ms_per_doc\": 17, \"ms_per_doc_std\": 1.2, \"throughput_docs_per_sec\": 58.8, \"gpu_memory_mb\": 5049}, \"diveye\": {\"ms_per_doc\": 14.2, \"ms_per_doc_std\": 0.2, \"throughput_docs_per_sec\": 70.3, \"gpu_memory_mb\": 3102}, \"neural_probe\": {\"ms_per_doc\": 14.6, \"ms_per_doc_std\": 0.2, \"throughput_docs_per_sec\": 68.3, \"gpu_memory_mb\": 3061}, \"key_finding\": \"OBD ~2.6× slower than baselines due to CPU-side self-BLEU computation (53% of time). But OBD uses less GPU memory than Binoculars (3.1 vs 5.0 GB) and provides 15D interpretable features + ordinal depth estimation vs binary-only detection. 22.6 docs/s = 50K docs in ~37min, practical for large-scale auditing.\"}, \"notes\": \"Hypothesis 被证伪：OBD 44.3ms/doc 是最慢方法（vs DivEye 14.2ms, Neural Probe 14.6ms, Binoculars 17.0ms），throughput 22.6 docs/s 未达假设的 >100 docs/s。瓶颈在 CPU self-BLEU (53%)。Rebuttal framing: OBD trades 2-3× latency for unique depth discrimination capability (K*=2 vs baselines K*=1)，不回避更慢事实，强调功能维度优势。不写入正文，仅 reviewer 显式要求时使用。\"}, \"exp_014_naturalistic\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T11:19:56.644Z\", \"updated_at\": \"2026-05-25T06:43:30.215Z\", \"hypothesis\": \"OBD predicted depth 在 wild web text (FineWeb CC-MAIN-2025-26) 上与独立质量指标（GPT-2 PPL, MTLD, vocd-D, n-gram repetition, MAUVE, Zipf coefficient）显著相关，验证 depth signal 的 ecological validity：depth signal 反映的文本退化模式不仅存在于实验室 prompt-chain，也可在自然 web 文本中观测到。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python /root/autodl-tmp/gen-depth-contamination/scripts/run_naturalistic_validation.py\", \"server\": \"cqa1-22115\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data_exp016_qwen_base/features.csv\", \"data_count\": 5000, \"model_name\": \"Qwen/Qwen2.5-1.5B\", \"seed\": 42, \"checkpoint_path\": \"N/A (eval-only)\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/data/exp014_naturalistic/\"}, \"conclusion\": \"success\", \"metrics\": {\"binary_auc\": 0.9919, \"cc_depth0_ratio\": 0.89, \"freq_entropy_rho\": -0.78, \"ttr_rho\": 0.17, \"note\": \"TTR rho=+0.17 contradicts hypothesis (expected negative). Paper should only report freq_entropy and CC classification, not TTR (or explicitly flag anomalous direction).\"}, \"completed_at\": \"2026-05-20T13:12:42.795Z\"}, \"gemma27b_filtering\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T09:52:09.087Z\", \"updated_at\": \"2026-05-24T11:40:31.003Z\", \"hypothesis\": \"Binary filtering on Gemma-27B generated contaminated text will still outperform no-filter (MMLU degradation ≤1pp), despite 27B text being harder to detect (cross-scorer K*=1, 0v1 AUC=0.887). This validates OBD binary curation robustness against unknown large generators.\", \"spec\": {\"command\": \"python scripts/exp_expanded_downstream_eval.py (adapted for Gemma-27B filtering)\", \"server\": \"cqa1-22115\", \"data_path\": \"data/exp_gemma27b_c4/ (5000 Gemma-27B generated docs)\", \"data_count\": \"5000 docs, 9 runs (3 strategies x 3 seeds)\", \"model_name\": \"Gemma-2-27B (generator) + Qwen2.5-1.5B-Instruct (OBD scorer) + GPT-2 (trainee)\", \"seed\": \"42,123,456\", \"gpu\": \"cuda:3\", \"pid\": \"169724\"}, \"failure_reason\": \"startup recovery: process dead, no active cron monitor\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-24T11:12:46.050Z\", \"metrics\": {\"results_by_strategy\": {\"no_filter\": {\"mmlu_avg\": 0.5956, \"hellaswag_avg\": 0.6633, \"mmlu_seeds\": [0.596, 0.5954, 0.5953], \"hellaswag_seeds\": [0.6638, 0.6636, 0.6626]}, \"binary_ours\": {\"mmlu_avg\": 0.5958, \"hellaswag_avg\": 0.6674, \"mmlu_seeds\": [0.5975, 0.5946, 0.5953], \"hellaswag_seeds\": [0.6775, 0.662, 0.6626]}, \"graduated_a09\": {\"mmlu_avg\": 0.5953, \"hellaswag_avg\": 0.6629, \"mmlu_seeds\": [0.5954, 0.5953, 0.5953], \"hellaswag_seeds\": [0.6636, 0.6626, 0.6626]}}, \"binary_vs_nofilter_delta\": {\"mmlu\": \"+0.02pp\", \"hellaswag\": \"+0.41pp\"}, \"key_finding\": \"OBD binary filtering on Gemma-27B text (cross-scorer K*=1) does not degrade quality: MMLU delta=+0.02pp, HellaSwag delta=+0.41pp. Filter robust against hard-to-detect 27B contamination. Graduated shows no advantage over binary.\"}}, \"code_domain_olmo\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T09:39:27.111Z\", \"updated_at\": \"2026-05-24T11:40:24.803Z\", \"hypothesis\": \"OLMo-1B on Python Code domain will yield K*=1 (competence-limited, similar to Pythia-1.4B on Code) or K*=2 (reaching Code ceiling). Either outcome strengthens the domain ceiling framework: K*=1 confirms competence limitation pattern, K*=2 confirms ceiling universality.\", \"spec\": {\"command\": \"python scripts/run_code_domain_olmo.py\", \"server\": \"cqa1-22115\", \"data_path\": \"data/exp_code_olmo/ (5500 Python code docs x 6 depths)\", \"data_count\": \"5500 docs x 6 depths = 33000 samples\", \"model_name\": \"OLMo-1B (generator) + Qwen2.5-1.5B-Instruct (cross-scorer)\", \"seed\": 42, \"gpu\": \"cuda:1\", \"pid\": \"167297\"}, \"failure_reason\": \"startup recovery: process dead, no active cron monitor\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-24T11:12:41.368Z\", \"metrics\": {\"k_star\": 1, \"pairwise_auc\": {\"0v1\": 0.9996, \"1v2\": 0.5567, \"2v3\": 0.5, \"3v4\": 0.5, \"4v5\": 0.5}, \"pairwise_jsd\": {\"0v1\": 0.334, \"1v2\": 0.006, \"2v3\": 0.003}, \"ordinal_mae\": 1.289, \"ordinal_accuracy\": 0.346, \"scorer\": \"Qwen2.5-1.5B-Instruct\", \"key_finding\": \"OLMo-1B Code K*=1 (competence-limited). 0v1 near-perfect (0.9996) but 1v2=0.5567 below θ. Completes OLMo 3-domain profile: C4=1, arXiv=1, Code=1 — uniformly competence-limited across all domains.\"}}, \"olmo_arxiv_cross_scorer\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T11:00:35.750Z\", \"updated_at\": \"2026-05-24T11:01:18.651Z\", \"hypothesis\": \"OLMo-1B on arXiv with cross-scorer (Qwen-1.5B) will confirm K*=1, consistent with self-scoring. While other models (Qwen, LLaMA, Mistral, Pythia) achieve K*=3 on arXiv, OLMo is competence-limited and cannot sustain distinguishable depth structure beyond generation 1.\", \"conclusion\": \"success\", \"metrics\": {\"k_star\": 1, \"pairwise_auc\": {\"0v1\": 0.9994, \"1v2\": 0.4996, \"2v3\": 0.4971, \"3v4\": 0.5091, \"4v5\": 0.536}, \"bootstrap_ci_95\": {\"0v1\": [0.999, 0.9997], \"1v2\": [0.4828, 0.5166], \"2v3\": [0.4796, 0.5138], \"3v4\": [0.4922, 0.5262], \"4v5\": [0.5183, 0.5533]}, \"p_perm\": {\"0v1\": 0.0001, \"1v2\": 0.51, \"2v3\": 0.6267, \"3v4\": 0.1488, \"4v5\": 0.0001}, \"scorer\": \"Qwen2.5-1.5B-Instruct\", \"key_finding\": \"OLMo-1B arXiv cross-scorer K*=1 confirmed. 1v2=0.4996 (chance). Sole exception to arXiv ceiling=3. All other models (Qwen/LLaMA/Mistral/Pythia) reach K*=3.\"}, \"spec\": {\"command\": \"python scripts/run_olmo_arxiv_cross_scorer.py\", \"server\": \"cqa1-22115\", \"data_path\": \"data/exp_024_arxiv/ (OLMo subset)\", \"data_count\": \"2200 docs x 6 depths\", \"model_name\": \"OLMo-1B + Qwen2.5-1.5B-Instruct (scorer)\", \"seed\": 42, \"gpu\": \"cuda:0\", \"checkpoint_path\": \"results/olmo_arxiv_cross_scorer/\", \"log_path\": \"results/olmo_arxiv_cross_scorer/\"}, \"completed_at\": \"2026-05-24T11:01:18.651Z\"}, \"olmo_c4_cross_scorer\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T10:59:03.914Z\", \"updated_at\": \"2026-05-24T10:59:48.614Z\", \"hypothesis\": \"OLMo-1B on C4 with cross-scorer (Qwen-1.5B) will confirm K*=1, matching self-scoring result. This validates OLMo as competence-limited on C4 (ceiling=2 but OLMo only reaches K*=1), completing the OLMo domain profile for the weak model exception narrative.\", \"metrics\": {\"k_star\": 1, \"pairwise_auc\": {\"0v1\": 0.986, \"1v2\": 0.4999, \"2v3\": 0.4982, \"3v4\": 0.5016, \"4v5\": 0.4946}, \"bootstrap_ci_95\": {\"0v1\": [0.9842, 0.9877], \"1v2\": [0.4885, 0.5112], \"2v3\": [0.4869, 0.5096], \"3v4\": [0.4903, 0.513], \"4v5\": [0.483, 0.506]}, \"p_perm\": {\"0v1\": 0.0001, \"1v2\": 0.5056, \"2v3\": 0.6286, \"3v4\": 0.3955, \"4v5\": 0.8183}, \"scorer\": \"Qwen2.5-1.5B-Instruct\", \"key_finding\": \"OLMo-1B C4 cross-scorer K*=1. 1v2=0.4999 (chance). Consistent across 3 pipelines. Confirms OLMo as competence-limited weak model.\"}, \"conclusion\": \"success\", \"spec\": {\"command\": \"python scripts/run_olmo_c4_cross_scorer.py\", \"server\": \"cqa1-22115\", \"data_path\": \"data/exp_olmo1b_10k/ (reused OLMo C4 data)\", \"data_count\": \"5000 docs x 6 depths\", \"model_name\": \"OLMo-1B + Qwen2.5-1.5B-Instruct (scorer)\", \"seed\": 42, \"gpu\": \"cuda:2\", \"checkpoint_path\": \"results/olmo_c4_cross_scorer/\", \"log_path\": \"results/olmo_c4_cross_scorer/\"}, \"completed_at\": \"2026-05-24T10:59:48.614Z\"}, \"arxiv_multi_source\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T08:26:09.176Z\", \"updated_at\": \"2026-05-24T10:58:24.019Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/gen-depth-contamination && python scripts/run_arxiv_multi_source_1b5.py\\\"\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:0\"], \"pid\": \"165918\", \"log_path\": \"~/runs/gen-depth-contamination/arxiv_multi_source.log\", \"submitted_at\": \"2026-05-24T09:15:24.821Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/exp_024_arxiv/ (2200 docs × 6 depths × 3 generators)\", \"data_count\": \"2200 docs × 6 depths × 3 models = 39600 samples\", \"model_name\": \"Pythia-1.4B + OLMo-1B + Qwen-1.5B (generators), Qwen2.5-1.5B-Instruct (scorer)\", \"seed\": 42, \"checkpoint_path\": \"results/arxiv_multi_source/\", \"wall_clock_seconds\": 3422.1, \"gpu_hours\": 0.95}, \"conclusion\": \"success\", \"hypothesis\": \"ArXiv domain K*=3 is domain-intrinsic (not model-specific): Pythia-1.4B and OLMo-1B on arXiv will also yield K*=3 (matching Qwen-1.5B exp-024), confirming that formulaic academic text structure creates larger per-generation distributional shifts that sustain one additional discriminable depth level beyond web text K*=2.\", \"metrics\": {\"k_star\": 3, \"pairwise_auc\": {\"0v1\": 0.9948, \"1v2\": 0.8581, \"2v3\": 0.6436, \"3v4\": 0.544, \"4v5\": 0.5299}, \"bootstrap_ci_bonf_qwen\": {\"2v3\": [0.629, 0.6587]}, \"bootstrap_ci_bonf_pythia\": {\"2v3\": [0.6338, 0.6626]}, \"bootstrap_ci_bonf_pooled\": {\"2v3\": [0.6466, 0.6666]}, \"per_model_2v3_auc\": {\"Qwen-1.5B\": 0.6437, \"Pythia-1.4B\": 0.6484, \"Pooled\": 0.6565}, \"bonf_p_all\": \"<0.005\", \"scorer\": \"Qwen2.5-1.5B-Instruct\", \"key_finding\": \"K*=3 statistically confirmed across all configs. Per-model: Qwen 2v3 CI [0.629,0.659], Pythia 2v3 CI [0.634,0.663], Pooled 2v3 CI [0.647,0.667]. All CI lower > θ=0.60.\"}, \"completed_at\": \"2026-05-24T10:12:26.970Z\"}, \"wiki_domain_llama\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T09:46:34.758Z\", \"updated_at\": \"2026-05-24T10:36:29.902Z\", \"hypothesis\": \"LLaMA-3.1-8B on Wikipedia will yield K*=1 (scorer-controlled), consistent with all other models on Wiki. Combined with C4 K*=2 and arXiv K*=3, this completes a 3-domain profile showing the same monotonic domain ceiling pattern as Mistral.\", \"metrics\": {\"k_star\": 1, \"pairwise_auc\": {\"0v1\": 0.9321, \"1v2\": 0.5919, \"2v3\": 0.5379, \"3v4\": 0.5105, \"4v5\": 0.5051}, \"bootstrap_ci_bonf\": {\"0v1\": [0.926, 0.938], \"1v2\": [0.5788, 0.6049], \"2v3\": [0.524, 0.5514], \"3v4\": [0.4962, 0.5244], \"4v5\": [0.4908, 0.5193]}, \"bonf_p\": {\"0v1\": 0.0005, \"1v2\": 0.0005, \"2v3\": 0.0005, \"3v4\": 0.231, \"4v5\": 1}, \"scorer\": \"Qwen2.5-1.5B-Instruct\", \"key_finding\": \"LLaMA-8B Wiki K*=1. NOTE: 1v2 AUC=0.5919, Bonf CI upper=0.6049 marginally crosses θ but point estimate < θ. Borderline case — K*=1 by convention.\"}, \"conclusion\": \"success\", \"spec\": {\"command\": \"OBD pipeline on pre-existing LLaMA-8B Wiki data\", \"server\": \"cqa1-22115\", \"data_path\": \"data/exp_wiki_llama8b/\", \"data_count\": \"5000 docs x 6 depths\", \"model_name\": \"LLaMA-3.1-8B + Qwen2.5-1.5B-Instruct (scorer)\", \"seed\": 42, \"checkpoint_path\": \"data/exp_wiki_llama8b/\", \"log_path\": \"data/exp_wiki_llama8b/\"}, \"completed_at\": \"2026-05-24T09:57:17.414Z\"}, \"wiki_domain_mistral\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T09:44:10.196Z\", \"updated_at\": \"2026-05-24T10:36:26.391Z\", \"hypothesis\": \"Mistral-7B on Wikipedia will yield K*=1 (scorer-controlled), completing the first 4-domain profile for a single model (Wiki=1, C4=1, Code=2, arXiv=3). This monotonic domain ceiling staircase within one model family is the strongest single-model evidence for domain-dependent K*.\", \"metrics\": {\"k_star\": 1, \"pairwise_auc\": {\"0v1\": 0.9614, \"1v2\": 0.5576, \"2v3\": 0.5193, \"3v4\": 0.5172, \"4v5\": 0.5011}, \"bootstrap_ci_bonf\": {\"0v1\": [0.9571, 0.9654], \"1v2\": [0.5434, 0.5716], \"2v3\": [0.5046, 0.5337], \"3v4\": [0.5029, 0.5317], \"4v5\": [0.4866, 0.5155]}, \"bonf_p\": {\"0v1\": 0.0005, \"1v2\": 0.0005, \"2v3\": 0.002, \"3v4\": 0.01, \"4v5\": 1}, \"scorer\": \"Qwen2.5-1.5B-Instruct\", \"key_finding\": \"Mistral-7B Wiki K*=1 confirmed. 1v2 CI upper=0.5716 < θ=0.60.\"}, \"conclusion\": \"success\", \"spec\": {\"command\": \"OBD pipeline on pre-existing Mistral-7B Wiki data\", \"server\": \"cqa1-22115\", \"data_path\": \"data/exp_wiki_mistral7b/\", \"data_count\": \"5000 docs x 6 depths\", \"model_name\": \"Mistral-7B + Qwen2.5-1.5B-Instruct (scorer)\", \"seed\": 42, \"checkpoint_path\": \"results/exp_wiki_mistral7b/\", \"log_path\": \"results/exp_wiki_mistral7b/\"}, \"completed_at\": \"2026-05-24T09:57:15.436Z\"}, \"code_domain_qwen7b\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T09:48:59.617Z\", \"updated_at\": \"2026-05-24T10:36:23.146Z\", \"hypothesis\": \"Qwen2.5-7B on Python Code domain will yield K*=2 (matching Code ceiling=2 from Qwen-1.5B, LLaMA-8B, Mistral-7B), confirming Code ceiling=2 is scale-invariant within the Qwen family. This fills the last \\\"pending\\\" slot in paper_framing for Code domain.\", \"metrics\": {\"k_star\": 2, \"pairwise_auc\": {\"0v1\": 0.905, \"1v2\": 0.7273, \"2v3\": 0.5367, \"3v4\": 0.5088, \"4v5\": 0.5137}, \"bootstrap_ci_bonf\": {\"0v1\": [0.8985, 0.9118], \"1v2\": [0.7153, 0.7389], \"2v3\": [0.5237, 0.5496], \"3v4\": [0.495, 0.5223], \"4v5\": [0.5002, 0.5274]}, \"bonf_p\": {\"0v1\": 0.0005, \"1v2\": 0.0005, \"2v3\": 0.0005, \"3v4\": 0.295, \"4v5\": 0.0415}, \"scorer\": \"Qwen2.5-1.5B-Instruct\", \"key_finding\": \"Qwen-7B Code K*=2 confirmed. 1v2 AUC=0.7273, well above θ. Scale-invariant within Qwen family.\"}, \"conclusion\": \"success\", \"spec\": {\"command\": \"OBD pipeline on pre-existing Qwen-7B Code data\", \"server\": \"cqa1-22115\", \"data_path\": \"data/exp_code_qwen7b/ (reused from exp_code_qwen7b)\", \"data_count\": \"5500 docs x 6 depths\", \"model_name\": \"Qwen2.5-7B + Qwen2.5-1.5B-Instruct (scorer)\", \"seed\": 42, \"checkpoint_path\": \"results/exp_code_qwen7b/\", \"log_path\": \"results/exp_code_qwen7b/\"}, \"completed_at\": \"2026-05-24T09:57:13.302Z\"}, \"code_domain_mistral\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T09:38:44.455Z\", \"updated_at\": \"2026-05-24T10:36:19.220Z\", \"hypothesis\": \"Mistral-7B on Python Code domain will yield K*=2 (matching Code ceiling=2 from Qwen-1.5B and LLaMA-8B), or K*=1 if competence-limited. Combined with Mistral C4 K*=1 and arXiv K*=3, this would demonstrate domain-dependent K* variation within a single model family.\", \"metrics\": {\"k_star\": 2, \"pairwise_auc\": {\"0v1\": 0.9189, \"1v2\": 0.615, \"2v3\": 0.5292, \"3v4\": 0.5286, \"4v5\": 0.5099}, \"bootstrap_ci_bonf\": {\"0v1\": [0.9127, 0.9251], \"1v2\": [0.6024, 0.6281], \"2v3\": [0.5155, 0.5426], \"3v4\": [0.5152, 0.5418], \"4v5\": [0.4961, 0.5235]}, \"bonf_p\": {\"0v1\": 0.0005, \"1v2\": 0.0005, \"2v3\": 0.0005, \"3v4\": 0.0005, \"4v5\": 0.187}, \"scorer\": \"Qwen2.5-1.5B-Instruct\", \"key_finding\": \"Mistral-7B Code K*=2. Bonferroni CI lower=0.6024 > θ=0.60 — statistically confirmed despite borderline AUC. Domain profile: Wiki=1, C4=1, Code=2, arXiv=3.\"}, \"conclusion\": \"success\", \"spec\": {\"command\": \"OBD pipeline on pre-existing Mistral-7B Code data\", \"server\": \"cqa1-22115\", \"data_path\": \"data/exp_code_mistral7b/\", \"data_count\": \"5500 docs x 6 depths\", \"model_name\": \"Mistral-7B + Qwen2.5-1.5B-Instruct (scorer)\", \"seed\": 42, \"checkpoint_path\": \"results/exp_code_mistral7b/\", \"log_path\": \"results/exp_code_mistral7b/\"}, \"completed_at\": \"2026-05-24T09:57:11.346Z\"}, \"gemma27b_cross_transfer\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T09:41:08.133Z\", \"updated_at\": \"2026-05-24T09:57:19.347Z\", \"hypothesis\": \"Cross-model transfer retention across 18x scale gap (27B to 1.5B) will maintain 80%+ retention, confirming depth signal is text-intrinsic and scale-invariant. OBD classifiers trained on 27B-generated text should generalize to smaller model outputs without retraining.\", \"metrics\": {\"transfer_matrix_accuracy\": {\"Gemma27B→Gemma27B\": 0.3106, \"Gemma27B→LLaMA8B\": 0.3218, \"Gemma27B→Qwen1.5B\": 0.3331, \"Gemma27B→Pythia\": 0.3214, \"Gemma27B→OLMo\": 0.2892, \"LLaMA8B→Gemma27B\": 0.3048, \"Qwen1.5B→Gemma27B\": 0.2693, \"Pythia→Gemma27B\": 0.286, \"OLMo→Gemma27B\": 0.2457}, \"transfer_matrix_mean_auc\": {\"Gemma27B→Gemma27B\": 0.6019, \"Gemma27B→LLaMA8B\": 0.6147, \"Gemma27B→Qwen1.5B\": 0.6274, \"Gemma27B→Pythia\": 0.6166, \"Gemma27B→OLMo\": 0.5934, \"LLaMA8B→Gemma27B\": 0.6037, \"Qwen1.5B→Gemma27B\": 0.5949, \"Pythia→Gemma27B\": 0.5973, \"OLMo→Gemma27B\": 0.5455}, \"retention_27b_to_small\": {\"avg_acc\": \"101.3%\", \"LLaMA8B\": \"103.6%\", \"Qwen1.5B\": \"107.2%\", \"Pythia\": \"103.5%\", \"OLMo\": \"93.1%\"}, \"retention_small_to_27b\": {\"avg_acc\": \"76.5%\", \"LLaMA8B\": \"92.1%\", \"Qwen1.5B\": \"71.3%\", \"Pythia\": \"80.9%\", \"OLMo\": \"77.3%\"}, \"retention_1.5b_inter_model\": \"88.9%\", \"result_path\": \"results/gemma27b_cross_transfer/cross_transfer_gemma27b_matrix.json\", \"key_finding\": \"27B→small retention 101.3% (>100%!): classifier trained on 27B data works BETTER on smaller models. 27B learns universal depth features. Small→27B only 76.5% due to weaker depth signal in 27B text. Strong asymmetry confirms depth signal is text-intrinsic but scale-modulated.\"}, \"conclusion\": \"success\", \"spec\": {\"command\": \"5x5 cross-transfer matrix analysis (CPU)\", \"server\": \"cqa1-22115\", \"data_path\": \"data/exp_gemma27b_c4/ + data from Qwen/Pythia/OLMo/LLaMA\", \"data_count\": \"5x5 model pairs, 5000 docs each\", \"model_name\": \"Gemma-2-27B + 4 smaller models, Qwen2.5-1.5B-Instruct (scorer)\", \"seed\": 42, \"checkpoint_path\": \"results/gemma27b_cross_transfer/\", \"log_path\": \"results/gemma27b_cross_transfer/\"}, \"completed_at\": \"2026-05-24T09:57:19.347Z\"}, \"exp_gemma27b_c4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T07:57:19.726Z\", \"updated_at\": \"2026-05-24T09:13:49.177Z\", \"hypothesis\": \"Gemma-2-27B (27B params, base model) on C4 domain will show slower depth saturation (higher K*) than smaller models due to greater generation capacity, while maintaining the universal depth-dependent distinguishability pattern observed across model families.\", \"metrics\": {\"self_scorer_k_star\": 2, \"self_scorer_pairwise_auc\": {\"0v1\": 0.9695, \"1v2\": 0.6196, \"2v3\": 0.5388, \"3v4\": 0.5069, \"4v5\": 0.5124}, \"self_scorer_bootstrap_ci\": {\"0v1\": {\"auc\": 0.9695, \"ci_lower\": 0.9666, \"ci_upper\": 0.9721, \"perm_p\": 0.0001}, \"1v2\": {\"auc\": 0.6196, \"ci_lower\": 0.6096, \"ci_upper\": 0.6296, \"perm_p\": 0.0001}, \"2v3\": {\"auc\": 0.5388, \"ci_lower\": 0.5279, \"ci_upper\": 0.549, \"perm_p\": 0.0001}, \"3v4\": {\"auc\": 0.5069, \"ci_lower\": 0.4959, \"ci_upper\": 0.5172, \"perm_p\": 0.1099}, \"4v5\": {\"auc\": 0.5124, \"ci_lower\": 0.5012, \"ci_upper\": 0.5234, \"perm_p\": 0.0147}}, \"cross_scorer_k_star\": 1, \"cross_scorer\": \"Qwen2.5-1.5B-Instruct\", \"cross_scorer_pairwise_auc\": {\"0v1\": 0.8871, \"1v2\": 0.5895, \"2v3\": 0.515, \"3v4\": 0.5061, \"4v5\": 0.5108}, \"cross_scorer_bootstrap_ci\": {\"0v1\": {\"auc\": 0.8871, \"ci_lower\": 0.8811, \"ci_upper\": 0.893, \"perm_p\": 0.0001}, \"1v2\": {\"auc\": 0.5895, \"ci_lower\": 0.5795, \"ci_upper\": 0.5997, \"perm_p\": 0.0001}, \"2v3\": {\"auc\": 0.515, \"ci_lower\": 0.5045, \"ci_upper\": 0.5254, \"perm_p\": 0.0027}, \"3v4\": {\"auc\": 0.5061, \"ci_lower\": 0.4952, \"ci_upper\": 0.5165, \"perm_p\": 0.1346}, \"4v5\": {\"auc\": 0.5108, \"ci_lower\": 0.4998, \"ci_upper\": 0.5218, \"perm_p\": 0.0282}}, \"cross_scorer_jsd\": {\"0v1\": 0.0643, \"1v2\": 0.0106, \"2v3\": 0.0049, \"3v4\": 0.0042, \"4v5\": 0.0031}, \"bootstrap_resamples\": 10000, \"permutation_resamples\": 10000, \"key_finding\": \"Self-scorer K*=2 (1v2 CI lower=0.6096>0.60, robust). Cross-scorer K*=1 (1v2 CI upper=0.5997<0.60). 27B scale does NOT elevate K* — consistent with universal K*<=2 for web text. Cross-scorer gap reflects scale mismatch (1.5B scorer vs 27B generator).\"}, \"spec\": {\"command\": \"python scripts/run_gemma27b_depth.py (depth chain + features + bootstrap CI)\", \"server\": \"cqa1-22115\", \"data_path\": \"data/exp_gemma27b_c4/ + data/exp_gemma27b_c4_qwen_scorer/\", \"data_count\": \"5000 docs x 6 depths = 30000 samples\", \"model_name\": \"google/gemma-2-27b (generator) + Qwen2.5-1.5B-Instruct (cross-scorer)\", \"seed\": 42, \"checkpoint_path\": \"N/A (inference only)\", \"log_path\": \"results/exp_gemma27b_c4/\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-24T09:13:49.177Z\"}, \"7b-cross-transfer\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T13:51:00.658Z\", \"updated_at\": \"2026-05-24T09:01:43.476Z\", \"conclusion\": \"success\", \"metrics\": {\"transfer_matrix_accuracy\": {\"Qwen7B→Qwen7B\": 0.378, \"Qwen7B→LLaMA8B\": 0.312, \"LLaMA8B→Qwen7B\": 0.346, \"LLaMA8B→LLaMA8B\": 0.331}, \"transfer_matrix_mae\": {\"Qwen7B→Qwen7B\": 1.169, \"Qwen7B→LLaMA8B\": 1.51, \"LLaMA8B→Qwen7B\": 1.249, \"LLaMA8B→LLaMA8B\": 1.321}, \"transfer_matrix_tau_b\": {\"Qwen7B→Qwen7B\": 0.463, \"Qwen7B→LLaMA8B\": 0.376, \"LLaMA8B→Qwen7B\": 0.418, \"LLaMA8B→LLaMA8B\": 0.383}, \"transfer_matrix_mean_auc\": {\"Qwen7B→Qwen7B\": 0.64, \"Qwen7B→LLaMA8B\": 0.619, \"LLaMA8B→Qwen7B\": 0.635, \"LLaMA8B→LLaMA8B\": 0.62}, \"transfer_retention\": {\"Qwen→LLaMA_acc\": \"82.7%\", \"Qwen→LLaMA_tau\": \"81.2%\", \"Qwen→LLaMA_auc\": \"85.0%\", \"LLaMA→Qwen_acc\": \"104.4%\", \"LLaMA→Qwen_tau\": \"109.3%\", \"LLaMA→Qwen_auc\": \"111.8%\"}, \"key_finding\": \"7B-scale transfer retention 82-85% (Qwen→LLaMA), consistent with 1.5B-scale patterns (80-92%). LLaMA→Qwen >100% because Qwen signal stronger. Cross-scale transfer universality confirmed.\", \"data_source\": \"Qwen-7B from exp_qwen_cont_10k (subsampled 5K), LLaMA-8B from exp-018. Both Qwen2.5-1.5B cross-scored.\", \"result_path\": \"results/7b_cross_transfer_v2/cross_transfer_7b_full_metrics.json\"}, \"spec\": {\"command\": \"python scripts/run_7b_cross_transfer_v2.py\", \"server\": \"cqa1-22115\", \"data_path\": \"data/exp_018_llama8b/features.csv + exp_qwen_cont_10k features\", \"data_count\": \"5000 docs × 6 depths × 2 models\", \"model_name\": \"Qwen2.5-7B + LLaMA-3.1-8B (OBD transfer, no GPU needed)\", \"seed\": 42, \"checkpoint_path\": \"N/A (CPU analysis)\", \"log_path\": \"results/7b_cross_transfer_v2/\"}, \"hypothesis\": \"Cross-model transfer retention at 7B scale (Qwen-7B ↔ LLaMA-8B) will match 1.5B-scale patterns (80-92%), confirming that depth signal is text-intrinsic rather than scale-dependent, and that OBD classifiers trained on one 7B model generalize to another without retraining.\", \"completed_at\": \"2026-05-24T09:01:43.476Z\"}, \"exp_015_neural_probe\": {\"status\": \"DONE\", \"retry_count\": 3, \"created_at\": \"2026-05-13T18:53:34.791Z\", \"updated_at\": \"2026-05-23T11:54:24.971Z\", \"hypothesis\": \"Learned representations (frozen LLM → MLP) 的 K* 是否高于 hand-crafted 15D features？若 K*_neural > K*_15D，说明 15D projection 是 K*=2 的部分原因；若相同，加强 information-theoretic impossibility 论证\", \"notes\": \"v4 completed successfully. 3 models: Pythia K*_neural=2, OLMo K*_neural=2, Qwen-cont K*_neural=3. Neural probe improves 2v3 AUC across all models (Pythia +0.044, OLMo +0.039, Qwen +0.055) but only Qwen-cont self-scorer crosses θ=0.60. EXIT_CODE=129 (SIGHUP after completion) did not affect results.\", \"completed_at\": \"2026-05-14T02:58:02.023Z\", \"failure_reason\": \"CUDA OOM: CUDA out of memory. Tried to allocate 26.00 MiB. GPU 0 has a total capacity of 23.52 GiB of which 20.06 MiB is free. Process 55665 has 13.36 GiB memory in use. Process 56371 has 9.09 GiB memory in use. Including non-PyTorch memory, this process has 1\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"v4 run in progress (PID 108774, tmux: exp015, westc-26893). Root cause of prior failures: v2=OOM (concurrent exp-006 占 GPU), v3=SIGHUP/EXIT_CODE=129 (SSH 断连，未在 tmux 中)。v4 在 tmux 中安全运行，Pythia 86% → OLMo → Qwen-cont → MLP training。内存管理正确 (del+gc+empty_cache)，6.7GB/24GB。ETA ~25-30min from 09:28 UTC.\"}, \"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T09:21:59.744073+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T09:31:39.481148+00:00\"}]}, \"reproduce\": {\"finished_at\": \"2026-05-15T09:31:35.099Z\"}, \"conclusion\": \"success\", \"metrics\": {\"k_star_qwen\": 3, \"k_star_pythia\": 2, \"k_star_olmo\": 1, \"qwen_pairwise_auc\": {\"0v1\": 0.988, \"1v2\": 0.702, \"2v3\": 0.616, \"3v4\": 0.59, \"4v5\": 0.566}, \"pythia_pairwise_auc\": {\"0v1\": 0.966, \"1v2\": 0.676, \"2v3\": 0.596, \"3v4\": 0.555, \"4v5\": 0.532}, \"olmo_pairwise_auc\": {\"0v1\": 0.9773, \"1v2\": 0.5054, \"2v3\": 0.5056, \"3v4\": 0.5032, \"4v5\": 0.4999}, \"olmo_rerun_source\": \"exp015_olmo_rerun/neural_probe_results.json\", \"notes\": \"OLMo values updated from rerun (self-probe). Original cross-model probe had K*=2 (1v2=0.657) but was superseded by self-probe rerun (K*=1, 1v2=0.5054). Paper Table 3 correctly uses rerun values.\"}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/artifacts/exp015_neural_probe_results.json\", \"log_path\": \"~/runs/gen-depth-contamination/exp_015_neural_probe.log\", \"spec\": {\"command\": \"python scripts/run_exp015_neural_probe.py --device cuda:0 --embed_batch_size 8\", \"server\": \"westc-26893\", \"data_path\": \"data_exp001_pythia + data_exp002_olmo + data_exp017_qwen_cont\", \"data_count\": 90000, \"model_name\": \"Qwen/Qwen2.5-1.5B-Instruct (frozen encoder -> MLP probe)\", \"seed\": \"5-fold CV\"}}, \"exp_gemma2b_10k\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T18:00:38.686Z\", \"updated_at\": \"2026-05-23T00:21:06.691Z\", \"hypothesis\": \"Gemma-2-2B 10K sample-size robustness: 5K borderline K*=1 (1v2 AUC=0.5981, just below θ=0.60) should remain K*=1 at 10K, confirming between-sample stability for borderline verdicts. Adds a K*=1 datapoint to the 10K robustness table (currently only K*=2 configs).\", \"spec\": {\"server\": \"cqa1-22115\", \"pid\": 54709, \"gpu\": \"cuda:3\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_gemma2b_10k/\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_gemma2b_10k/run.log\", \"completed_at\": \"2026-05-22T23:16:00.183Z\", \"metrics\": {\"K_star_self\": 2, \"K_star_qwen\": 2, \"scorer\": \"Qwen2.5-1.5B-Instruct (cross-scored)\", \"pairwise_auc_self\": {\"0v1\": 0.9817, \"1v2\": 0.643, \"2v3\": 0.555, \"3v4\": 0.5173, \"4v5\": 0.5101}, \"pairwise_auc_qwen\": {\"0v1\": 0.9533, \"1v2\": 0.6099, \"2v3\": 0.5409, \"3v4\": 0.5174, \"4v5\": 0.5158}, \"bootstrap_ci_1v2\": {\"auc_oof\": 0.6099, \"boot_std\": 0.0034, \"ci_95\": [0.6031, 0.6167], \"ci_995_bonferroni_pct\": [0.5998, 0.6192], \"ci_995_bonferroni_norm\": [0.6003, 0.6196], \"perm_p\": 0.0001, \"bonferroni_pass_pct\": false, \"bonferroni_pass_norm\": true}, \"note\": \"5K K*=1 (1v2=0.5981), 10K Qwen cross-scored K*=2 (1v2=0.6099). Bonferroni split: percentile FAIL (0.5998), normal PASS (0.6003). Extremely borderline.\"}}, \"seed_gemma27b_c4_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T10:05:43.080Z\", \"updated_at\": \"2026-05-23T00:00:23.931Z\", \"spec\": {\"server\": \"cqa1-22115\", \"pid\": 26893, \"gpu\": \"cuda:0\"}, \"conclusion\": \"success\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_gemma27b_c4/run.log\", \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/exp_gemma27b_c4/\", \"hypothesis\": \"Gemma-2-27B, the largest model tested, will exhibit K*=2 consistent with smaller models, confirming that generational depth saturation is model-scale-invariant for the surprisal-feature OBD pipeline.\", \"completed_at\": \"2026-05-22T23:06:04.697Z\", \"metrics\": {\"K_star\": 1, \"scorer\": \"Qwen2.5-1.5B-Instruct (cross-scored)\", \"pairwise_auc_self\": {\"0v1\": 0.9695, \"1v2\": 0.6196, \"2v3\": 0.5388, \"3v4\": 0.5069, \"4v5\": 0.5124}, \"pairwise_auc_qwen\": {\"0v1\": 0.8874, \"1v2\": 0.5894}, \"note\": \"Self-scored K*=2 (1v2=0.6196), Qwen cross-scored K*=1 (1v2=0.5894 < θ=0.60). Self→Cross inflation: 1v2 Δ=-3.0pp, 0v1 Δ=-8.2pp.\"}}, \"exp_olmo1b_10k\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T20:05:20.014Z\", \"updated_at\": \"2026-05-22T22:34:48.584Z\", \"hypothesis\": \"OLMo-1B on 10K C4 samples will show saturation at depth K*=1, meaning generation-depth signal is only distinguishable between real (depth-0) and first-generation synthetic text, with deeper depths being indistinguishable from each other.\", \"spec\": {\"command\": \"bash /tmp/exp_olmo1b_10k.sh (Phase1: OLMo-1B continuation gen + Phase2: Qwen scorer)\", \"server\": \"cqa1-22115\", \"gpu\": \"cuda:2\", \"pid\": 66415, \"data_path\": \"data/olmo1b_c4_10k\", \"data_count\": 10000, \"model_name\": \"allenai/OLMo-1B-hf (gen) + Qwen2.5-1.5B-Instruct (scorer)\", \"seed\": 42, \"log_path\": \"/tmp/exp_olmo1b_10k.log\", \"checkpoint_path\": \"results/olmo1b_c4_10k/\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T22:34:45.698Z\", \"metrics\": {\"pairwise_auc\": {\"0v1\": 0.9871, \"1v2\": 0.4984, \"2v3\": 0.5059, \"3v4\": 0.5061, \"4v5\": 0.5074}, \"K_star\": 1, \"ordinal_mae\": 1.4145, \"ordinal_accuracy\": 0.3152, \"pairwise_jsd\": {\"0v1\": 0.230018, \"1v2\": 0.001457, \"2v3\": 0.001512, \"3v4\": 0.001413, \"4v5\": 0.001535}, \"top_features\": [\"freq_entropy\", \"surp_d1_mean\", \"freq_kurtosis\", \"surp_d2_mean\", \"surp_d1_skew\"]}}, \"exp_002_olmo_depth\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-12T20:06:24.766Z\", \"updated_at\": \"2026-05-22T22:04:07.552Z\", \"hypothesis\": \"K* 跨模型一致性验证：OLMo-1B 在相同种子数据和解码策略下的 K* 是否与 Qwen2.5-1.5B 一致（K*=2）\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo 2>/dev/null && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_ENDPOINT=https://hf-mirror.com && cd /root/autodl-tmp/gen-depth-contamination && python scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/allenai/OLMo-1B-hf --data_dir /root/autodl-tmp/gen-depth-contamination/data_exp002_olmo --results_dir /root/autodl-tmp/gen-depth-contamination/results_exp002_olmo --num_samples 5000 --max_depth 5 --batch_size 16 --generation_mode continuation\\\"\", \"server\": \"autodl-4090d\", \"gpu\": [\"cuda:0\"], \"pid\": \"20225\", \"log_path\": \"~/runs/gen-depth-contamination/exp_002_olmo_depth.log\", \"submitted_at\": \"2026-05-13T00:16:07.960Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data_exp002_olmo\", \"data_count\": 5000, \"model_name\": \"allenai/OLMo-1B-hf\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/data_exp002_olmo/\", \"wall_clock_seconds\": 8384.9, \"gpu_hours\": 2.33}, \"reproduce\": {\"finished_at\": \"2026-05-13T02:31:18.880Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-13T02:31:19.738113+00:00\"}]}, \"metrics\": {\"k_star\": 1, \"pairwise_auc\": {\"0v1\": 0.9861, \"1v2\": 0.5001, \"2v3\": 0.4972, \"3v4\": 0.5034, \"4v5\": 0.4971}, \"scorer\": \"Qwen2.5-1.5B-Instruct\", \"note\": \"Updated to Qwen cross-scoring (D107). Self-scored 1v2=0.6145 K*=2, Qwen-scored 1v2=0.5001 K*=1.\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T02:35:52.823Z\", \"parent\": \"exp_001_pythia_depth\"}, \"exp_001_pythia_depth\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-12T20:06:23.803Z\", \"updated_at\": \"2026-05-22T22:04:05.591Z\", \"hypothesis\": \"K* 跨模型一致性验证：Pythia-1.4B 在相同种子数据和解码策略下的 K* 是否与 Qwen2.5-1.5B 一致（K*=2）\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && source /etc/network_turbo 2>/dev/null && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && export HF_ENDPOINT=https://hf-mirror.com && cd /root/autodl-tmp/gen-depth-contamination && python scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/EleutherAI/pythia-1.4b --data_dir /root/autodl-tmp/gen-depth-contamination/data_exp001_pythia --results_dir /root/autodl-tmp/gen-depth-contamination/results_exp001_pythia --num_samples 5000 --max_depth 5 --batch_size 16 --generation_mode continuation\\\"\", \"server\": \"autodl-4090d\", \"gpu\": [\"cuda:0\"], \"pid\": \"17138\", \"log_path\": \"~/runs/gen-depth-contamination/exp_001_pythia_depth.log\", \"submitted_at\": \"2026-05-12T20:50:31.471Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data_exp001_pythia\", \"data_count\": 5000, \"model_name\": \"EleutherAI/pythia-1.4b\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/data_exp001_pythia/\", \"wall_clock_seconds\": 12344.9, \"gpu_hours\": 3.43}, \"conclusion\": \"success\", \"metrics\": {\"k_star\": 2, \"pairwise_auc\": {\"0v1\": 0.9722, \"1v2\": 0.6074, \"2v3\": 0.544, \"3v4\": 0.5051, \"4v5\": 0.5079}, \"pairwise_auc_std\": {\"0v1\": 0.0039, \"1v2\": 0.0078, \"2v3\": 0.0067, \"3v4\": 0.0032, \"4v5\": 0.0101}, \"bootstrap_ci\": {\"1v2\": {\"auc_oof\": 0.6072, \"boot_mean\": 0.6073, \"boot_std\": 0.005, \"ci_95\": [0.5975, 0.6172], \"ci_995_bonferroni\": [0.5934, 0.621], \"perm_p\": 0.0001, \"bonferroni_pass\": false}}, \"scorer\": \"Qwen2.5-1.5B-Instruct\", \"note\": \"Updated to Qwen cross-scoring (D107). Self-scored 1v2=0.6539, Qwen-scored 1v2=0.6074.\"}, \"completed_at\": \"2026-05-13T00:16:16.359Z\"}, \"exp_llama8b_10k\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T09:25:55.895Z\", \"updated_at\": \"2026-05-22T20:26:09.870Z\", \"hypothesis\": \"增加 LLaMA-8B C4 样本量从 5k→10k 可将 1v2 bootstrap std 缩小 ~√2 倍，使 Bonferroni 99.5% CI lower bound 恢复到 θ=0.60 以上\", \"spec\": {\"server\": \"cqa1-22115\", \"pid\": 23232, \"checkpoint_path\": \"results/exp_llama8b_10k/\", \"log_path\": \"/tmp/exp_llama8b_10k.log\"}, \"conclusion\": \"negative\", \"metrics\": {\"K_star\": 1, \"AUC_0v1\": 0.9282, \"AUC_1v2\": 0.6148, \"AUC_1v2_oof\": 0.588, \"AUC_2v3\": 0.5247, \"AUC_3v4\": 0.5519, \"AUC_4v5\": 0.5262, \"bootstrap_1v2_oof_auc\": 0.588, \"bootstrap_1v2_95CI\": [0.5809, 0.595], \"bootstrap_1v2_995CI_bonferroni\": [0.5776, 0.5978], \"bonferroni_pass\": false, \"perm_pvalue_1v2\": 0.0001, \"scorer\": \"Qwen2.5-1.5B-Instruct\", \"note\": \"All pairwise AUC from Qwen cross-scoring (Phase 2). Pipeline AUC 1v2=0.6148 (mean-of-folds).\"}, \"completed_at\": \"2026-05-22T19:21:09.215Z\"}, \"exp_pythia14b_c4_10k\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T11:57:18.681Z\", \"updated_at\": \"2026-05-22T14:59:24.436Z\", \"hypothesis\": \"统一所有 K*=2 configs 的样本量至 10K，避免 selective precision boosting 质疑。Pythia-1.4B 5K 已稳定通过 Bonferroni (CI_lower≈0.641>0.60)，10K 为一致性验证。\", \"spec\": {\"command\": \"python3 scripts/run_pipeline.py --model_path pythia-1.4b --num_samples 10000 --max_depth 5 --batch_size 32 --generation_mode continuation + Phase2 Qwen scorer\", \"server\": \"cqa1-22115\", \"gpu\": \"cuda:3 (RTX PRO 6000 Blackwell 96GB)\", \"data_path\": \"data/exp_pythia14b_c4_10k\", \"data_count\": 10000, \"model_name\": \"Pythia-1.4B (gen) + Qwen2.5-1.5B-Instruct (scorer)\", \"seed\": 42, \"log_path\": \"/tmp/exp_pythia14b_c4_10k.log\", \"checkpoint_path\": \"results/exp_pythia14b_c4_10k/\"}, \"metrics\": {\"K_star\": 2, \"AUC_0v1\": 0.9712, \"AUC_1v2\": 0.6175, \"AUC_2v3\": 0.5364, \"AUC_3v4\": 0.5134, \"AUC_4v5\": 0.5088, \"bootstrap_1v2_95CI\": [0.6108, 0.6242], \"bootstrap_1v2_995CI_bonferroni\": [0.6078, 0.6273], \"perm_pvalue_1v2\": 0.0001, \"bonferroni_pass\": true, \"top_feature\": \"freq_entropy\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T14:14:41.623Z\"}, \"exp_qwen_cont_10k\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T09:27:38.591Z\", \"updated_at\": \"2026-05-22T14:59:22.490Z\", \"hypothesis\": \"增加 Qwen-cont C4 样本量从 5k→10k 可将 1v2 bootstrap std 缩小 ~√2 倍，使 Bonferroni 99.5% CI lower bound 恢复到 θ=0.60 以上\", \"spec\": {\"command\": \"bash /tmp/run_qwen_cont_10k.sh (Phase1: base generation + Phase2: instruct scoring)\", \"server\": \"cqa1-22115\", \"gpu\": \"cuda:1 (RTX PRO 6000 Blackwell 96GB)\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/exp_qwen_cont_10k\", \"data_count\": 10000, \"model_name\": \"Qwen/Qwen2.5-1.5B (base, continuation) + Qwen/Qwen2.5-1.5B-Instruct (scorer)\", \"seed\": 42, \"checkpoint_path\": \"results/exp_qwen_cont_10k/\", \"log_path\": \"/tmp/exp_qwen_cont_10k_phase1.log\"}, \"metrics\": {\"K_star\": 2, \"AUC_0v1\": 0.9875, \"AUC_1v2\": 0.6346, \"AUC_2v3\": 0.5616, \"AUC_3v4\": 0.5451, \"AUC_4v5\": 0.5254, \"bootstrap_1v2_95CI\": [0.6282, 0.6409], \"bootstrap_1v2_995CI_bonferroni\": [0.6255, 0.6436], \"perm_pvalue_1v2\": 0.0001, \"bonferroni_pass\": true, \"top_feature\": \"freq_entropy\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T14:47:57.847Z\"}, \"exp_pythia14b_10k\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T11:59:05.554Z\", \"updated_at\": \"2026-05-22T12:00:24.157Z\", \"hypothesis\": \"统一所有 K*=2 configs 样本量至 10K，避免 selective precision boosting 质疑。Pythia-1.4B 5K 已稳定通过 Bonferroni (CI_lower≈0.641>0.60)，10K 为一致性验证。\", \"spec\": {\"command\": \"python3 scripts/run_pipeline.py --model_path pythia-1.4b --num_samples 10000 --max_depth 5 --batch_size 32 --generation_mode continuation + Phase2 Qwen scorer\", \"server\": \"cqa1-22115\", \"gpu\": \"cuda:3 (RTX PRO 6000 Blackwell 96GB)\", \"data_path\": \"data/exp_pythia14b_c4_10k\", \"data_count\": 10000, \"model_name\": \"Pythia-1.4B (gen) + Qwen2.5-1.5B-Instruct (scorer)\", \"seed\": 42, \"log_path\": \"N/A\", \"note\": \"重复条目，已合并到 exp_pythia14b_c4_10k\", \"checkpoint_path\": \"N/A\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-22T12:00:24.157Z\"}, \"seed_qwen15b_c4_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T00:34:11.792Z\", \"updated_at\": \"2026-05-22T06:39:21.815Z\", \"hypothesis\": \"Qwen-1.5B C4 的 K*=2 结论在 seed=123 下仍成立（原始 seed=42），验证 OBD 的 depth boundary 不依赖随机种子\", \"spec\": {\"command\": \"run_pipeline.py --generation_mode rewrite --top_p 0.95 --seed 123 (C4)\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:3\"], \"pid\": \"3156\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/results/seed_qwen15b_c4_s123/\", \"submitted_at\": \"2026-05-22T03:58:27.354Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/seed_robustness/seed_qwen15b_c4_s123\", \"data_count\": 5000, \"model_name\": \"Qwen2.5-1.5B-Instruct\", \"seed\": 123, \"metrics\": {\"K_star\": 2, \"auc_0v1\": 0.9956, \"auc_1v2\": 0.7014, \"auc_2v3\": 0.5911, \"auc_3v4\": 0.5405, \"auc_4v5\": 0.5335}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/seed_qwen15b_c4_s123/\", \"wall_clock_seconds\": 9654.5, \"gpu_hours\": 2.68}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T06:39:21.815Z\"}, \"seed_qwen15b_wiki_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T00:34:09.969Z\", \"updated_at\": \"2026-05-22T06:39:19.860Z\", \"hypothesis\": \"Qwen-1.5B WikiText 的 K*=2 结论在 seed=123 下仍成立（原始 seed=42），验证 OBD 的 depth boundary 不依赖随机种子\", \"spec\": {\"command\": \"run_pipeline.py --generation_mode rewrite --top_p 0.95 --seed 123\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:2\"], \"pid\": \"3005\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/results/seed_qwen15b_wiki_s123/\", \"submitted_at\": \"2026-05-22T03:58:25.151Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/seed_robustness/seed_qwen15b_wiki_s123\", \"data_count\": 5000, \"model_name\": \"Qwen2.5-1.5B-Instruct\", \"seed\": 123, \"metrics\": {\"K_star\": 3, \"auc_0v1\": 0.9945, \"auc_1v2\": 0.7059, \"auc_2v3\": 0.6067, \"auc_3v4\": 0.5531, \"auc_4v5\": 0.5292}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/seed_qwen15b_wiki_s123/\", \"wall_clock_seconds\": 9654.7, \"gpu_hours\": 2.68}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-22T06:39:19.860Z\"}, \"seed_pythia14b_wiki_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T00:34:08.091Z\", \"updated_at\": \"2026-05-22T06:39:17.971Z\", \"hypothesis\": \"Pythia-1.4B WikiText 的 K*=2 结论在 seed=123 下仍成立（原始 seed=42），验证 OBD 的 depth boundary 不依赖随机种子\", \"spec\": {\"command\": \"run_pipeline.py --generation_mode continuation --top_p 0.95 --seed 123 (two-phase: Pythia gen + Qwen score)\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:1\"], \"pid\": \"2863\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/results/seed_pythia14b_wiki_s123/\", \"submitted_at\": \"2026-05-22T03:58:22.018Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/gen-depth-contamination/data/seed_robustness/seed_pythia14b_wiki_s123\", \"data_count\": 5000, \"model_name\": \"EleutherAI/pythia-1.4b (generator) + Qwen2.5-1.5B-Instruct (scorer)\", \"seed\": 123, \"metrics\": {\"K_star\": 1, \"auc_0v1\": 0.9751, \"auc_1v2\": 0.5766, \"auc_2v3\": 0.5318, \"auc_3v4\": 0.5175, \"auc_4v5\": 0.527}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/results/seed_pythia14b_wiki_s123/\", \"wall_clock_seconds\": 9656.0, \"gpu_hours\": 2.68}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T06:39:17.971Z\"}, \"exp_pythia69b_c4_nuc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T13:57:54.120Z\", \"updated_at\": \"2026-05-21T23:00:07.454Z\", \"hypothesis\": \"Pythia-6.9B 在 C4 上使用 nucleus sampling（非 greedy）的 K*=2，与其他 continuation 模型的 decoding 策略对齐，消除 greedy 高估 confound。生成阶段自评，完成后用 Qwen-1.5B scorer 重跑 features+OBD（方案 2）。\", \"parent\": \"exp_pythia69b_c4_depth_chain_v3\", \"spec\": {\"command\": \"python scripts/run_pipeline.py --model_path ... --scorer_path Qwen2.5-1.5B --num_samples 5000 --max_depth 5 --generation_mode continuation --data_dir data/exp_pythia69b_c4_nuc --results_dir results/exp_pythia69b_c4_nuc\", \"server\": \"cqa1-22115\", \"data_path\": \"data/exp_pythia69b_c4_nuc\", \"data_count\": 5000, \"model_name\": \"EleutherAI/pythia-6.9b\", \"seed\": \"default\", \"checkpoint_source\": \"N/A\", \"eval_data\": \"N/A (full pipeline: seed->generation->features->OBD)\", \"log_path\": \"/root/autodl-tmp/gen-depth-contamination/logs/pythia69b_nuc_v2.log\", \"checkpoint_path\": \"results/exp_pythia69b_c4_nuc_qwen/\"}, \"conclusion\": \"negative\", \"metrics\": {\"K_star\": 1, \"pairwise_auc\": {\"0v1\": 0.9599, \"1v2\": 0.5955, \"2v3\": 0.5298, \"3v4\": 0.5135}, \"scorer\": \"Qwen-1.5B\", \"theta\": 0.6, \"note\": \"1v2 AUC borderline (0.0045 below threshold)\"}, \"completed_at\": \"2026-05-21T23:00:07.454Z\"}, \"exp_pythia69b_c4_depth_chain_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T03:21:54.364Z\", \"updated_at\": \"2026-05-21T19:55:37.923Z\", \"hypothesis\": \"Pythia-6.9B 在 C4 上的 K*=2，与其他 ≥7B 模型一致，验证 K*=2 不依赖 Qwen 家族。使用 Qwen-1.5B scorer（D095）。\", \"parent\": \"exp_pythia69b_c4_depth_chain_v2\", \"spec\": {\"command\": \"python scripts/run_pipeline.py --model_path /root/autodl-tmp/.hf_cache/models--EleutherAI--pythia-6.9b/snapshots/c0e3eee36dc47af0c49f361c74cfe459c09f7f23 --scorer_path /root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B --num_samples 5000 --max_depth 5 --batch_size 4 --feat_batch_size 2 --generation_mode continuation --no_sample --data_dir data/exp_pythia69b_c4 --results_dir results/exp_pythia69b_c4\", \"server\": \"cqa1-22115\", \"gpu\": [\"cuda:0\"], \"pid\": \"395575\", \"log_path\": \"~/runs/gen-depth-contamination/exp_pythia69b_c4_depth_chain_v3.log\", \"submitted_at\": \"2026-05-21T03:22:20.098Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"EleutherAI/pythia-6.9b\", \"model_path\": \"/root/autodl-tmp/.hf_cache/models--EleutherAI--pythia-6.9b/snapshots/c0e3eee36dc47af0c49f361c74cfe459c09f7f23\", \"scorer_path\": \"/root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B\", \"data_path\": \"data/exp_pythia69b_c4\", \"data_count\": 5000, \"seed\": \"default\", \"generation_mode\": \"continuation\", \"no_sample\": true, \"max_depth\": 5, \"checkpoint_source\": \"N/A (full pipeline)\", \"eval_data\": \"N/A (full pipeline: seed->generation->features->OBD)\", \"wall_clock_seconds\": 32849.3, \"gpu_hours\": 9.12}, \"reproduce\": {\"finished_at\": \"2026-05-21T12:29:46.273Z\"}, \"failure_reason\": \"greedy confound (--no_sample): AUC_1v2 inflated to 0.8542, not usable for cross-model comparison. K*=2 under greedy is artifact, not genuine nucleus result.\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-21T12:29:49.365Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-21T12:29:53.480338+00:00\"}]}, \"metrics\": {\"0v1_auc\": 0.9941, \"1v2_auc\": 0.8542, \"2v3_auc\": 0.5373, \"3v4_auc\": 0.5339, \"4v5_auc\": 0.5211, \"kstar_at_060\": 2, \"0v1_jsd\": 0.53459, \"1v2_jsd\": 0.06438, \"2v3_jsd\": 0.00502, \"empty_texts_total\": 144, \"features_rows\": 30000}, \"checkpoint_path\": \"/root/autodl-tmp/gen-depth-contamination/data/exp_pythia69b_c4/features.csv\", \"log_path\": \"~/runs/gen-depth-contamination/exp_pythia69b_c4_depth_chain_v3.log\"}}, \"count\": 30, \"total\": 140, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5011}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6c12b7bd-9dd0-4e58-ab88-81f50b68b29d",
  "isSidechain": true,
  "promptId": "4b1e9bd3-a514-43a0-8b8b-ee4e7298d832",
  "agentId": "aa09eae889717e82e",
  "type": "user",
  "uuid": "b7525217-3f12-4165-9489-80e78aa1dedf",
  "sourceToolAssistantUUID": "6c12b7bd-9dd0-4e58-ab88-81f50b68b29d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d0900953-8129-4d2a-95a5-2cd8b707bc5a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-25T19:45:35.804Z_

I need more batches. Let me query the registry for the remaining experiments, using larger limits to get all 176 total.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b7525217-3f12-4165-9489-80e78aa1dedf",
  "isSidechain": true,
  "agentId": "aa09eae889717e82e",
  "requestId": "req_011CbPrwX8mDLyDWkyfCp8Tw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3a2b97b2-ca46-4a69-b0d2-14afa7b50e38",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d0900953-8129-4d2a-95a5-2cd8b707bc5a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0116L8gcDqErGdSSp9cWHbhz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23695,
      "cache_read_input_tokens": 40927,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 23695,
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

_source line 15 · 2026-05-25T19:45:36.714Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_018nY6a7GR3qzioU6UXd1dae`</summary>

```json
{
  "project": "gen-depth-contamination",
  "fields": [
    "exp_id",
    "metrics",
    "conclusion",
    "notes",
    "status"
  ],
  "limit": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a2b97b2-ca46-4a69-b0d2-14afa7b50e38",
  "isSidechain": true,
  "agentId": "aa09eae889717e82e",
  "requestId": "req_011CbPrwX8mDLyDWkyfCp8Tw",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9882d95d-5627-4cea-b11f-6ac314146508",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d0900953-8129-4d2a-95a5-2cd8b707bc5a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0116L8gcDqErGdSSp9cWHbhz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23695,
      "cache_read_input_tokens": 40927,
      "output_tokens": 145,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 23695
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 145,
          "cache_read_input_tokens": 40927,
          "cache_creation_input_tokens": 23695,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 23695,
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

_source line 16 · 2026-05-25T19:45:37.568Z_

<details><summary>↩ Tool result · `toolu_018nY6a7GR3qzioU6UXd1dae`</summary>

```text
Error: result (102,284 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/d0900953-8129-4d2a-95a5-2cd8b707bc5a/tool-results/mcp-agent-ml-research-read_registry-1779738337554.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/d0900953-8129-4d2a-95a5-2cd8b707bc5a/tool-results/mcp-agent-ml-research-read_registry-1779738337554.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/d0900953-8129-4d2a-95a5-2cd8b707bc5a/tool-results/mcp-agent-ml-research-read_registry-1779738337554.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9882d95d-5627-4cea-b11f-6ac314146508",
  "isSidechain": true,
  "promptId": "4b1e9bd3-a514-43a0-8b8b-ee4e7298d832",
  "agentId": "aa09eae889717e82e",
  "type": "user",
  "uuid": "b3bf19cb-e1e4-4335-bce5-eec3a56ff355",
  "sourceToolAssistantUUID": "9882d95d-5627-4cea-b11f-6ac314146508",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d0900953-8129-4d2a-95a5-2cd8b707bc5a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-25T19:45:48.524Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01DU6Mwvxss2thcH836sM54V`</summary>

```json
{
  "command": "jq -r '.result' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/d0900953-8129-4d2a-95a5-2cd8b707bc5a/tool-results/mcp-agent-ml-research-read_registry-1779738337554.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nexps = data['data']['experiments']\ntarget_ids = [\n    'exp_023_domain_ablation', 'wiki_domain_mistral', 'wiki_domain_llama',\n    'exp_024_arxiv_domain', 'arxiv_multi_source', 'code_domain_mistral',\n    'code_domain_qwen7b', 'code_domain_olmo', 'exp_015_neural_probe',\n    'seed_gemma27b_c4_s42', 'exp_pythia69b_c4_depth_chain_v2', 'exp_gemma2b_depth',\n    'exp_arXiv_qwen1b5_crossscorer', 'exp_arXiv_llama8b_crossscorer',\n    'exp_arXiv_mistral7b_crossscorer', 'exp_arXiv_qwen7b_crossscorer',\n    'exp_wiki_scorer_confound', 'exp_wiki_scorer_confound_1b5',\n    'exp_wiki_qwen7b', 'exp_wiki_llama8b', 'exp_wiki_mistral7b',\n    'exp_arXiv_llama8b', 'exp_arXiv_mistral7b', 'exp_arXiv_qwen7b',\n    'exp_code_qwen1b5', 'exp_code_llama8b', 'exp_code_mistral7b', 'exp_code_qwen7b',\n    'olmo_arxiv_cross_scorer', 'olmo_c4_cross_scorer'\n]\nprint('=== ALL EXPERIMENT IDs IN REGISTRY ===')\nfor eid in sorted(exps.keys()):\n    print(eid)\nprint()\nprint('=== TARGET EXPERIMENTS FOUND ===')\nfor tid in target_ids:\n    if tid in exps:\n        e = exps[tid]\n        print(f'FOUND: {tid}')\n    else:\n        print(f'MISSING: {tid}')\n\"\n",
  "description": "List all experiment IDs and check which target IDs are present"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b3bf19cb-e1e4-4335-bce5-eec3a56ff355",
  "isSidechain": true,
  "agentId": "aa09eae889717e82e",
  "requestId": "req_011CbPrwsFEkiAaP4fjBQ1ib",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cae48387-2de0-4b92-9672-5756a3c33450",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d0900953-8129-4d2a-95a5-2cd8b707bc5a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01MxPmxGfoBCz7LPMMu57uvz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 656,
      "cache_read_input_tokens": 64622,
      "output_tokens": 709,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 656
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 709,
          "cache_read_input_tokens": 64622,
          "cache_creation_input_tokens": 656,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 656,
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

_source line 18 · 2026-05-25T19:45:48.738Z_

<details><summary>↩ Tool result · `toolu_01DU6Mwvxss2thcH836sM54V`</summary>

```text
=== ALL EXPERIMENT IDs IN REGISTRY ===
7b-cross-transfer
arxiv_multi_source
code_domain_mistral
code_domain_olmo
code_domain_qwen7b
deberta_filter_deberta_binary
deberta_filter_deberta_graduated
deberta_filter_no_filter
deberta_filter_obd_binary
deberta_filtering_predict
exp-008-retrain-chain
exp-014
exp_001_pythia_depth
exp_002_olmo_depth
exp_003_decoding_ablation
exp_004_7b_crossscale
exp_005_degradation
exp_006_graduated_filtering
exp_007_bootstrap_ci
exp_008_retrain_chain
exp_008_retrain_chain_v2
exp_009_dose_10pct
exp_009_dose_10pct_v2
exp_009_dose_10pct_v3
exp_009_dose_30pct
exp_009_dose_30pct_v2
exp_009_dose_30pct_v3
exp_009_dose_50pct
exp_009_dose_50pct_v2
exp_009_dose_50pct_v3
exp_009_dose_response
exp_010_ordinal_baseline
exp_011_llm_zeroshot
exp_012_binary_confidence
exp_013_cross_transfer
exp_014_independent_metrics
exp_014_naturalistic
exp_014_naturalistic_v2
exp_015_neural_probe
exp_016_base_vs_instruct
exp_017_qwen_continuation
exp_018_llama8b_depth
exp_019_mistral7b_depth
exp_019b_mistral_cross_scorer
exp_020_pythia_decoding
exp_021_length_ablation
exp_022_cross_scorer_matrix
exp_023_domain_ablation
exp_024_arxiv_domain
exp_025_pythia_arxiv
exp_025_pythia_filtering
exp_026_arxiv_filtering
exp_026_feature_stability
exp_026_feature_stability_v2
exp_027
exp_027_latex_ablation
exp_027_retrain_bootstrap
exp_028_power_curve
exp_028_subsampling_power
exp_14b_c4
exp_32b_c4
exp_32b_c4_6class
exp_7b_scorer_ablation
exp_7b_scorer_arxiv
exp_A_alt_scorer
exp_B_14d_ablation
exp_C_permutation_10k
exp_D_obd_n500
exp_E_paired_stats
exp_arXiv_llama8b
exp_arXiv_llama8b_crossscorer
exp_arXiv_mistral7b
exp_arXiv_mistral7b_crossscorer
exp_arXiv_olmo
exp_arXiv_qwen1b5_crossscorer
exp_arXiv_qwen7b
exp_arXiv_qwen7b_crossscorer
exp_bootstrap_10k
exp_changepoint_kstar
exp_code_llama8b
exp_code_mistral7b
exp_code_multi_source
exp_code_pythia1b4
exp_code_qwen1b5
exp_code_qwen1b5_pythia_scorer
exp_code_qwen7b
exp_contamination_rate_sweep
exp_cross_transfer_llama8b_to_qwen7b
exp_cross_transfer_llama8b_to_qwen7b_v2
exp_cross_transfer_qwen7b_to_llama8b
exp_deberta_arxiv_qwen1b5
exp_deberta_c4
exp_deberta_c4_1b5
exp_deberta_c4_1b5_pythia
exp_deberta_c4_1b5_qwen_cont
exp_deberta_code_qwen1b5
exp_deberta_cross_transfer_gpu1
exp_deberta_cross_transfer_gpu2
exp_deberta_cross_transfer_gpu3
exp_deberta_cross_transfer_wiki
exp_deberta_filtering_comparison
exp_deberta_upperbound
exp_expanded_downstream_eval
exp_gemma27b_c4
exp_gemma2b_10k
exp_gemma2b_depth
exp_kstar_theta
exp_llama8b_10k
exp_multi_source_arxiv
exp_multi_source_detection
exp_olmo1b_10k
exp_olmo1b_c4_rerun
exp_olmo_retrain_chain
exp_olmo_retrain_v2
exp_olmo_retrain_v3
exp_pythia14b_10k
exp_pythia14b_c4_10k
exp_pythia14b_c4_rerun
exp_pythia69b_c4_depth_chain
exp_pythia69b_c4_depth_chain_v2
exp_pythia69b_c4_depth_chain_v3
exp_pythia69b_c4_nuc
exp_pythia_retrain_depth7
exp_qwen_cont_10k
exp_qwen_retrain_chain
exp_qwen_retrain_depth7
exp_wiki_llama8b
exp_wiki_mistral7b
exp_wiki_multi_source
exp_wiki_olmo
exp_wiki_olmo_v2
exp_wiki_pythia
exp_wiki_pythia_v2
exp_wiki_qwen7b
exp_wiki_scorer_confound
exp_wiki_scorer_confound_1b5
gemma27b_cross_transfer
gemma27b_filtering
gsm8k-serial-rerun
gsm8k_patch_bo_s0
gsm8k_patch_grad_s0
gsm8k_patch_nf_s0
mvp_pilot_sat_v1
olmo_arxiv_cross_scorer
olmo_c4_cross_scorer
runtime_benchmark
seed2_binary_ours
seed2_graduated
seed2_no_filter
seed_gemma27b_c4_s42
seed_pythia14b_wiki_s123
seed_qwen15b_c4_s123
seed_qwen15b_wiki_s123
sweep_eval_r10_bin
sweep_eval_r10_binary
sweep_eval_r10_grad
sweep_eval_r10_graduated
sweep_eval_r10_nf
sweep_eval_r10_nf_v2
sweep_eval_r10_nofilter
sweep_eval_r30_nf
sweep_eval_r30_nofilter
sweep_r100_binary
sweep_r100_graduated
sweep_r100_nf
sweep_r10_binary
sweep_r10_graduated
sweep_r10_nofilter
sweep_r30_binary
sweep_r30_graduated
sweep_r30_nofilter
sweep_r50_binary
sweep_r50_graduated
sweep_r50_nf
wiki_domain_llama
wiki_domain_mistral

=== TARGET EXPERIMENTS FOUND ===
FOUND: exp_023_domain_ablation
FOUND: wiki_domain_mistral
FOUND: wiki_domain_llama
FOUND: exp_024_arxiv_domain
FOUND: arxiv_multi_source
FOUND: code_domain_mistral
FOUND: code_domain_qwen7b
FOUND: code_domain_olmo
FOUND: exp_015_neural_probe
FOUND: seed_gemma27b_c4_s42
FOUND: exp_pythia69b_c4_depth_chain_v2
FOUND: exp_gemma2b_depth
FOUND: exp_arXiv_qwen1b5_crossscorer
FOUND: exp_arXiv_llama8b_crossscorer
FOUND: exp_arXiv_mistral7b_crossscorer
FOUND: exp_arXiv_qwen7b_crossscorer
FOUND: exp_wiki_scorer_confound
FOUND: exp_wiki_scorer_confound_1b5
FOUND: exp_wiki_qwen7b
FOUND: exp_wiki_llama8b
FOUND: exp_wiki_mistral7b
FOUND: exp_arXiv_llama8b
FOUND: exp_arXiv_mistral7b
FOUND: exp_arXiv_qwen7b
FOUND: exp_code_qwen1b5
FOUND: exp_code_llama8b
FOUND: exp_code_mistral7b
FOUND: exp_code_qwen7b
FOUND: olmo_arxiv_cross_scorer
FOUND: olmo_c4_cross_scorer
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cae48387-2de0-4b92-9672-5756a3c33450",
  "isSidechain": true,
  "promptId": "4b1e9bd3-a514-43a0-8b8b-ee4e7298d832",
  "agentId": "aa09eae889717e82e",
  "type": "user",
  "uuid": "f4c67808-0dfb-4354-92f6-b8409978cee7",
  "sourceToolAssistantUUID": "cae48387-2de0-4b92-9672-5756a3c33450",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d0900953-8129-4d2a-95a5-2cd8b707bc5a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-25T19:45:50.954Z_

All 30 are found. Now extract full metrics for each.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f4c67808-0dfb-4354-92f6-b8409978cee7",
  "isSidechain": true,
  "agentId": "aa09eae889717e82e",
  "requestId": "req_011CbPrxh1cK24P2DFbXRJSX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a91d48c1-80d0-46e5-bc3e-fb4a06c7f46a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d0900953-8129-4d2a-95a5-2cd8b707bc5a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01KXEsegg78fHLGyR7gXhzWM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2901,
      "cache_read_input_tokens": 65278,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2901,
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

_source line 20 · 2026-05-25T19:45:59.622Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01FbZinCtspkLqhKeyYQduDM`</summary>

```json
{
  "command": "jq -r '.result' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/d0900953-8129-4d2a-95a5-2cd8b707bc5a/tool-results/mcp-agent-ml-research-read_registry-1779738337554.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nexps = data['data']['experiments']\ntarget_ids = [\n    'exp_023_domain_ablation', 'wiki_domain_mistral', 'wiki_domain_llama',\n    'exp_024_arxiv_domain', 'arxiv_multi_source', 'code_domain_mistral',\n    'code_domain_qwen7b', 'code_domain_olmo', 'exp_015_neural_probe',\n    'seed_gemma27b_c4_s42', 'exp_pythia69b_c4_depth_chain_v2', 'exp_gemma2b_depth',\n    'exp_arXiv_qwen1b5_crossscorer', 'exp_arXiv_llama8b_crossscorer',\n    'exp_arXiv_mistral7b_crossscorer', 'exp_arXiv_qwen7b_crossscorer',\n    'exp_wiki_scorer_confound', 'exp_wiki_scorer_confound_1b5',\n    'exp_wiki_qwen7b', 'exp_wiki_llama8b', 'exp_wiki_mistral7b',\n    'exp_arXiv_llama8b', 'exp_arXiv_mistral7b', 'exp_arXiv_qwen7b',\n    'exp_code_qwen1b5', 'exp_code_llama8b', 'exp_code_mistral7b', 'exp_code_qwen7b',\n    'olmo_arxiv_cross_scorer', 'olmo_c4_cross_scorer'\n]\nfor tid in target_ids:\n    e = exps[tid]\n    print(f'=== {tid} ===')\n    print(f'status: {e.get(\\\"status\\\")}')\n    print(f'conclusion: {e.get(\\\"conclusion\\\")}')\n    print(f'metrics: {json.dumps(e.get(\\\"metrics\\\"), indent=2)}')\n    if e.get('notes'):\n        print(f'notes: {e[\\\"notes\\\"]}')\n    print()\n\"\n",
  "description": "Extract metrics and conclusions for all 30 target experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a91d48c1-80d0-46e5-bc3e-fb4a06c7f46a",
  "isSidechain": true,
  "agentId": "aa09eae889717e82e",
  "requestId": "req_011CbPrxh1cK24P2DFbXRJSX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f0e7704e-a318-44fa-a652-4256723f87ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d0900953-8129-4d2a-95a5-2cd8b707bc5a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01KXEsegg78fHLGyR7gXhzWM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2901,
      "cache_read_input_tokens": 65278,
      "output_tokens": 737,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2901
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 737,
          "cache_read_input_tokens": 65278,
          "cache_creation_input_tokens": 2901,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2901,
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

_source line 21 · 2026-05-25T19:45:59.727Z_

<details><summary>↩ Tool result · `toolu_01FbZinCtspkLqhKeyYQduDM`</summary>

```text
=== exp_023_domain_ablation ===
status: DONE
conclusion: success
metrics: {
  "K_star": 2,
  "1v2_auc": 0.6193,
  "2v3_auc": 0.5498,
  "all_folds_above_060": true,
  "top_feature": "freq_entropy",
  "ordinal_accuracy": 0.377
}

=== wiki_domain_mistral ===
status: DONE
conclusion: success
metrics: {
  "k_star": 1,
  "pairwise_auc": {
    "0v1": 0.9614,
    "1v2": 0.5576,
    "2v3": 0.5193,
    "3v4": 0.5172,
    "4v5": 0.5011
  },
  "bootstrap_ci_bonf": {
    "0v1": [
      0.9571,
      0.9654
    ],
    "1v2": [
      0.5434,
      0.5716
    ],
    "2v3": [
      0.5046,
      0.5337
    ],
    "3v4": [
      0.5029,
      0.5317
    ],
    "4v5": [
      0.4866,
      0.5155
    ]
  },
  "bonf_p": {
    "0v1": 0.0005,
    "1v2": 0.0005,
    "2v3": 0.002,
    "3v4": 0.01,
    "4v5": 1
  },
  "scorer": "Qwen2.5-1.5B-Instruct",
  "key_finding": "Mistral-7B Wiki K*=1 confirmed. 1v2 CI upper=0.5716 < \u03b8=0.60."
}

=== wiki_domain_llama ===
status: DONE
conclusion: success
metrics: {
  "k_star": 1,
  "pairwise_auc": {
    "0v1": 0.9321,
    "1v2": 0.5919,
    "2v3": 0.5379,
    "3v4": 0.5105,
    "4v5": 0.5051
  },
  "bootstrap_ci_bonf": {
    "0v1": [
      0.926,
      0.938
    ],
    "1v2": [
      0.5788,
      0.6049
    ],
    "2v3": [
      0.524,
      0.5514
    ],
    "3v4": [
      0.4962,
      0.5244
    ],
    "4v5": [
      0.4908,
      0.5193
    ]
  },
  "bonf_p": {
    "0v1": 0.0005,
    "1v2": 0.0005,
    "2v3": 0.0005,
    "3v4": 0.231,
    "4v5": 1
  },
  "scorer": "Qwen2.5-1.5B-Instruct",
  "key_finding": "LLaMA-8B Wiki K*=1. NOTE: 1v2 AUC=0.5919, Bonf CI upper=0.6049 marginally crosses \u03b8 but point estimate < \u03b8. Borderline case \u2014 K*=1 by convention."
}

=== exp_024_arxiv_domain ===
status: DONE
conclusion: success
metrics: {
  "K_star": 3,
  "pairwise_auc": {
    "0v1": 0.9946,
    "1v2": 0.858,
    "2v3": 0.6427,
    "3v4": 0.5437,
    "4v5": 0.5294
  },
  "bootstrap_ci": {
    "0v1": {
      "auc": 0.9946,
      "ci_lower": 0.9929,
      "ci_upper": 0.9961,
      "perm_p": 0.0001
    },
    "1v2": {
      "auc": 0.858,
      "ci_lower": 0.848,
      "ci_upper": 0.8679,
      "perm_p": 0.0001
    },
    "2v3": {
      "auc": 0.6427,
      "ci_lower": 0.6275,
      "ci_upper": 0.6575,
      "perm_p": 0.0001
    },
    "3v4": {
      "auc": 0.5437,
      "ci_lower": 0.5276,
      "ci_upper": 0.5598,
      "perm_p": 0.0001
    },
    "4v5": {
      "auc": 0.5294,
      "ci_lower": 0.5133,
      "ci_upper": 0.5455,
      "perm_p": 0.0006
    }
  },
  "bootstrap_resamples": 10000,
  "permutation_resamples": 10000,
  "key_finding": "arXiv domain K*=3 (CI-confirmed). 2v3 CI lower=0.6275 > \u03b8=0.60. First condition with K*>2. 1v2 AUC=0.858 far exceeds C4/Wiki (~0.61-0.69)."
}
notes: 2026-05-16 15:05 重启成功。PID 48295, cuda:2, 73% util。修复：depth_0.jsonl 已有 2200 行 arXiv 数据，prepare_seed_data 行数检查通过后跳过 C4 下载，HF_DATASETS_OFFLINE=1 不再冲突。n_docs=2200。预计 ~20 min 完成剩余 depth。

=== arxiv_multi_source ===
status: DONE
conclusion: success
metrics: {
  "k_star": 3,
  "pairwise_auc": {
    "0v1": 0.9948,
    "1v2": 0.8581,
    "2v3": 0.6436,
    "3v4": 0.544,
    "4v5": 0.5299
  },
  "bootstrap_ci_bonf_qwen": {
    "2v3": [
      0.629,
      0.6587
    ]
  },
  "bootstrap_ci_bonf_pythia": {
    "2v3": [
      0.6338,
      0.6626
    ]
  },
  "bootstrap_ci_bonf_pooled": {
    "2v3": [
      0.6466,
      0.6666
    ]
  },
  "per_model_2v3_auc": {
    "Qwen-1.5B": 0.6437,
    "Pythia-1.4B": 0.6484,
    "Pooled": 0.6565
  },
  "bonf_p_all": "<0.005",
  "scorer": "Qwen2.5-1.5B-Instruct",
  "key_finding": "K*=3 statistically confirmed across all configs. Per-model: Qwen 2v3 CI [0.629,0.659], Pythia 2v3 CI [0.634,0.663], Pooled 2v3 CI [0.647,0.667]. All CI lower > \u03b8=0.60."
}

=== code_domain_mistral ===
status: DONE
conclusion: success
metrics: {
  "k_star": 2,
  "pairwise_auc": {
    "0v1": 0.9189,
    "1v2": 0.615,
    "2v3": 0.5292,
    "3v4": 0.5286,
    "4v5": 0.5099
  },
  "bootstrap_ci_bonf": {
    "0v1": [
      0.9127,
      0.9251
    ],
    "1v2": [
      0.6024,
      0.6281
    ],
    "2v3": [
      0.5155,
      0.5426
    ],
    "3v4": [
      0.5152,
      0.5418
    ],
    "4v5": [
      0.4961,
      0.5235
    ]
  },
  "bonf_p": {
    "0v1": 0.0005,
    "1v2": 0.0005,
    "2v3": 0.0005,
    "3v4": 0.0005,
    "4v5": 0.187
  },
  "scorer": "Qwen2.5-1.5B-Instruct",
  "key_finding": "Mistral-7B Code K*=2. Bonferroni CI lower=0.6024 > \u03b8=0.60 \u2014 statistically confirmed despite borderline AUC. Domain profile: Wiki=1, C4=1, Code=2, arXiv=3."
}

=== code_domain_qwen7b ===
status: DONE
conclusion: success
metrics: {
  "k_star": 2,
  "pairwise_auc": {
    "0v1": 0.905,
    "1v2": 0.7273,
    "2v3": 0.5367,
    "3v4": 0.5088,
    "4v5": 0.5137
  },
  "bootstrap_ci_bonf": {
    "0v1": [
      0.8985,
      0.9118
    ],
    "1v2": [
      0.7153,
      0.7389
    ],
    "2v3": [
      0.5237,
      0.5496
    ],
    "3v4": [
      0.495,
      0.5223
    ],
    "4v5": [
      0.5002,
      0.5274
    ]
  },
  "bonf_p": {
    "0v1": 0.0005,
    "1v2": 0.0005,
    "2v3": 0.0005,
    "3v4": 0.295,
    "4v5": 0.0415
  },
  "scorer": "Qwen2.5-1.5B-Instruct",
  "key_finding": "Qwen-7B Code K*=2 confirmed. 1v2 AUC=0.7273, well above \u03b8. Scale-invariant within Qwen family."
}

=== code_domain_olmo ===
status: DONE
conclusion: success
metrics: {
  "k_star": 1,
  "pairwise_auc": {
    "0v1": 0.9996,
    "1v2": 0.5567,
    "2v3": 0.5,
    "3v4": 0.5,
    "4v5": 0.5
  },
  "pairwise_jsd": {
    "0v1": 0.334,
    "1v2": 0.006,
    "2v3": 0.003
  },
  "ordinal_mae": 1.289,
  "ordinal_accuracy": 0.346,
  "scorer": "Qwen2.5-1.5B-Instruct",
  "key_finding": "OLMo-1B Code K*=1 (competence-limited). 0v1 near-perfect (0.9996) but 1v2=0.5567 below \u03b8. Completes OLMo 3-domain profile: C4=1, arXiv=1, Code=1 \u2014 uniformly competence-limited across all domains."
}

=== exp_015_neural_probe ===
status: DONE
conclusion: success
metrics: {
  "k_star_qwen": 3,
  "k_star_pythia": 2,
  "k_star_olmo": 1,
  "qwen_pairwise_auc": {
    "0v1": 0.988,
    "1v2": 0.702,
    "2v3": 0.616,
    "3v4": 0.59,
    "4v5": 0.566
  },
  "pythia_pairwise_auc": {
    "0v1": 0.966,
    "1v2": 0.676,
    "2v3": 0.596,
    "3v4": 0.555,
    "4v5": 0.532
  },
  "olmo_pairwise_auc": {
    "0v1": 0.9773,
    "1v2": 0.5054,
    "2v3": 0.5056,
    "3v4": 0.5032,
    "4v5": 0.4999
  },
  "olmo_rerun_source": "exp015_olmo_rerun/neural_probe_results.json",
  "notes": "OLMo values updated from rerun (self-probe). Original cross-model probe had K*=2 (1v2=0.657) but was superseded by self-probe rerun (K*=1, 1v2=0.5054). Paper Table 3 correctly uses rerun values."
}
notes: v4 completed successfully. 3 models: Pythia K*_neural=2, OLMo K*_neural=2, Qwen-cont K*_neural=3. Neural probe improves 2v3 AUC across all models (Pythia +0.044, OLMo +0.039, Qwen +0.055) but only Qwen-cont self-scorer crosses θ=0.60. EXIT_CODE=129 (SIGHUP after completion) did not affect results.

=== seed_gemma27b_c4_s42 ===
status: DONE
conclusion: success
metrics: {
  "K_star": 1,
  "scorer": "Qwen2.5-1.5B-Instruct (cross-scored)",
  "pairwise_auc_self": {
    "0v1": 0.9695,
    "1v2": 0.6196,
    "2v3": 0.5388,
    "3v4": 0.5069,
    "4v5": 0.5124
  },
  "pairwise_auc_qwen": {
    "0v1": 0.8874,
    "1v2": 0.5894
  },
  "note": "Self-scored K*=2 (1v2=0.6196), Qwen cross-scored K*=1 (1v2=0.5894 < \u03b8=0.60). Self\u2192Cross inflation: 1v2 \u0394=-3.0pp, 0v1 \u0394=-8.2pp."
}

=== exp_pythia69b_c4_depth_chain_v2 ===
status: DONE
conclusion: failed
metrics: null

=== exp_gemma2b_depth ===
status: DONE
conclusion: negative
metrics: {
  "k_star": 1,
  "pairwise_auc": {
    "0v1": 0.9534,
    "1v2": 0.5981,
    "2v3": 0.5342,
    "3v4": 0.503,
    "4v5": 0.5026
  },
  "pairwise_auc_std": {
    "0v1": 0.003,
    "1v2": 0.008,
    "2v3": 0.013,
    "3v4": 0.003,
    "4v5": 0.013
  },
  "bootstrap_ci_1v2": {
    "ci_lower": 0.5882,
    "ci_upper": 0.6076
  },
  "jsd": {
    "0v1": 0.09882,
    "1v2": 0.008852,
    "2v3": 0.004904,
    "3v4": 0.003742,
    "4v5": 0.003167
  },
  "ordinal_mae": 1.3152,
  "ordinal_accuracy": 0.3321,
  "note": "K*=1, NOT borderline K*=2. 1v2 AUC=0.5981 < theta=0.60. CI upper=0.6076 crosses theta but point estimate below."
}

=== exp_arXiv_qwen1b5_crossscorer ===
status: DONE
conclusion: success
metrics: {
  "k_star": 3,
  "auc_0v1": 0.9748,
  "auc_1v2": 0.8105,
  "auc_2v3": 0.6317,
  "auc_3v4": 0.5437,
  "auc_4v5": 0.5294,
  "jsd_0v1": 0.154297,
  "jsd_1v2": 0.066782,
  "jsd_2v3": 0.019268,
  "jsd_3v4": 0.008867,
  "jsd_4v5": 0.006991,
  "ordinal_mae": 0.9017,
  "ordinal_accuracy": 0.4402
}
notes: 首次提交因 symlink 问题失败 (EXIT_CODE=1)，Worker 修复后重跑成功 (EXIT_CODE=0)。Pythia-1.4B scorer 重评 Qwen-1.5B arXiv 文本 K*=3，与 Qwen scorer 一致，确认 arXiv K*=3 scorer-independent。

=== exp_arXiv_llama8b_crossscorer ===
status: DONE
conclusion: success
metrics: {
  "k_star": 3,
  "auc_0v1": 0.9629,
  "auc_1v2": 0.8433,
  "auc_2v3": 0.6201,
  "auc_3v4": 0.523,
  "auc_4v5": 0.5245,
  "jsd_0v1": 0.1214,
  "jsd_1v2": 0.0815,
  "jsd_2v3": 0.0195,
  "jsd_3v4": 0.0083,
  "jsd_4v5": 0.0082,
  "ordinal_mae": 0.9025,
  "ordinal_accuracy": 0.4407,
  "scorer": "pythia-1.4b"
}

=== exp_arXiv_mistral7b_crossscorer ===
status: DONE
conclusion: success
metrics: {
  "k_star": 3,
  "scorer": "pythia-1.4b",
  "auc_0v1": 0.9798,
  "auc_1v2": 0.8141,
  "auc_2v3": 0.6075,
  "auc_3v4": 0.5489,
  "auc_4v5": 0.5391,
  "jsd_0v1": 0.135575,
  "jsd_1v2": 0.078,
  "jsd_2v3": 0.020452,
  "jsd_3v4": 0.010992,
  "jsd_4v5": 0.008831,
  "ordinal_mae": 0.9061,
  "ordinal_accuracy": 0.4412
}
notes: Pythia-1.4B cross-scorer confirms K*=3 for Mistral-7B arXiv, matching Qwen-1.5B original. Max AUC delta = 0.02 (at 2v3). arXiv Mistral K*=3 is scorer-independent. Contrasts with Wikipedia where scorer choice affected K*.

=== exp_arXiv_qwen7b_crossscorer ===
status: DONE
conclusion: negative
metrics: {
  "k_star": 2,
  "auc_0v1": 0.9575,
  "auc_1v2": 0.8171,
  "auc_2v3": 0.5989,
  "auc_3v4": 0.5417,
  "auc_4v5": 0.5192,
  "jsd_0v1": 0.137085,
  "jsd_1v2": 0.059688,
  "jsd_2v3": 0.013508,
  "jsd_3v4": 0.009125,
  "jsd_4v5": 0.006738,
  "ordinal_mae": 0.9617,
  "ordinal_accuracy": 0.4255
}
notes: Hypothesis rejected: cross-scorer 2v3 AUC=0.5989 < 0.60, K* drops from 3→2. Mild Qwen family bias (~0.027 AUC at 2v3) inflates original K*=3. Scorer-independent K*=2. Borderline: 3/5 folds above 0.60. Depths 0-2 robustly scorer-independent.

=== exp_wiki_scorer_confound ===
status: DONE
conclusion: negative
metrics: {
  "k_star": 1,
  "confound_verdict": "confirmed",
  "auc_0v1": 0.9404,
  "auc_1v2": 0.587,
  "auc_2v3": 0.5456,
  "auc_3v4": 0.525,
  "auc_4v5": 0.5172,
  "critical_delta_1v2": -0.0238
}

=== exp_wiki_scorer_confound_1b5 ===
status: DONE
conclusion: negative
metrics: {
  "k_star": 1,
  "confound_verdict": "confirmed",
  "auc_0v1": 0.9729,
  "auc_1v2": 0.5994,
  "auc_2v3": 0.533,
  "auc_3v4": 0.5214,
  "auc_4v5": 0.5068,
  "jsd_0v1": 0.0886,
  "ordinal_mae": 1.2995,
  "ordinal_accuracy": 0.3466
}

=== exp_wiki_qwen7b ===
status: DONE
conclusion: success
metrics: {
  "K_star": 2,
  "auc_0v1": 0.9673,
  "auc_1v2": 0.6108,
  "auc_2v3": 0.5562,
  "auc_3v4": 0.5297,
  "auc_4v5": 0.529,
  "jsd_0v1": 0.083514,
  "jsd_1v2": 0.010991,
  "jsd_2v3": 0.00555,
  "jsd_3v4": 0.004611,
  "jsd_4v5": 0.003894,
  "ordinal_mae": 1.2501,
  "ordinal_accuracy": 0.3532
}

=== exp_wiki_llama8b ===
status: DONE
conclusion: negative
metrics: {
  "K_star": 1,
  "ordinal_mae": 1.2954,
  "ordinal_accuracy": 0.3313,
  "auc_0v1": 0.9316,
  "auc_1v2": 0.5954,
  "auc_2v3": 0.5392,
  "auc_3v4": 0.5221,
  "auc_4v5": 0.5212,
  "jsd_0v1": 0.06169,
  "jsd_1v2": 0.00931
}

=== exp_wiki_mistral7b ===
status: DONE
conclusion: success
metrics: {
  "K_star": 1,
  "ordinal_mae": 1.3445,
  "ordinal_accuracy": 0.3273,
  "auc_0v1": 0.9607,
  "auc_1v2": 0.5552,
  "auc_2v3": 0.5236,
  "auc_3v4": 0.5181,
  "auc_4v5": 0.5012,
  "jsd_0v1": 0.054134,
  "jsd_1v2": 0.005678,
  "jsd_2v3": 0.003698,
  "jsd_3v4": 0.003459,
  "jsd_4v5": 0.003274
}

=== exp_arXiv_llama8b ===
status: DONE
conclusion: success
metrics: {
  "K_star": 3,
  "auc_0v1": 0.9754,
  "auc_1v2": 0.8447,
  "auc_2v3": 0.6215,
  "auc_3v4": 0.5362,
  "auc_4v5": 0.5331,
  "jsd_0v1": 0.1296,
  "jsd_1v2": 0.0785,
  "jsd_2v3": 0.0177,
  "ordinal_acc": 0.4549,
  "ordinal_mae": 0.8806
}

=== exp_arXiv_mistral7b ===
status: DONE
conclusion: success
metrics: {
  "k_star": 3,
  "pairwise_auc": {
    "0v1": 0.9848,
    "1v2": 0.8201,
    "2v3": 0.6275,
    "3v4": 0.5295,
    "4v5": 0.5295
  },
  "jsd": {
    "0v1": 0.14249,
    "1v2": 0.076232,
    "2v3": 0.018972,
    "3v4": 0.009908,
    "4v5": 0.008877
  },
  "ordinal_mae": 0.8958,
  "ordinal_accuracy": 0.4474,
  "top_features": [
    "freq_entropy",
    "surp_std",
    "surp_d1_skew",
    "surp_mean",
    "surp_d2_mean"
  ]
}

=== exp_arXiv_qwen7b ===
status: DONE
conclusion: success
metrics: {
  "k_star": 3,
  "pairwise_auc": {
    "0v1": 0.983,
    "1v2": 0.835,
    "2v3": 0.626,
    "3v4": 0.544,
    "4v5": 0.513
  },
  "pairwise_jsd": {
    "0v1": 0.1656,
    "1v2": 0.0668,
    "2v3": 0.0156,
    "3v4": 0.0089,
    "4v5": 0.0061
  },
  "ordinal_mae": 0.9,
  "ordinal_accuracy": 0.446
}

=== exp_code_qwen1b5 ===
status: DONE
conclusion: success
metrics: {
  "K_star": 2,
  "theta": 0.6,
  "auc_0v1": 0.9388,
  "auc_1v2": 0.7382,
  "auc_2v3": 0.53,
  "auc_3v4": 0.5022,
  "auc_4v5": 0.5219,
  "ci_0v1": [
    0.929,
    0.949
  ],
  "ci_1v2": [
    0.709,
    0.767
  ],
  "ci_2v3": [
    0.514,
    0.546
  ],
  "jsd_0v1": 0.0814,
  "jsd_1v2": 0.0443,
  "jsd_2v3": 0.0038,
  "ordinal_accuracy": 0.359,
  "ordinal_mae": 1.204
}
notes: Code domain (Python/CodeSearchNet) K*=2, same as C4. 1v2 AUC=0.7382 well above θ, 2v3 drops to 0.5300. Bug fix: run_pipeline.py:462 int(doc_id) patched for string IDs. Top features: freq_entropy, surp_d2_mean, surp_d1_mean. Data source: CodeSearchNet Python subset (Husain et al. 2019).

=== exp_code_llama8b ===
status: DONE
conclusion: success
metrics: {
  "K_star": 2,
  "pairwise_auc": {
    "0v1": 0.9161,
    "1v2": 0.7394,
    "2v3": 0.5112,
    "3v4": 0.52,
    "4v5": 0.4996
  },
  "pairwise_auc_std": {
    "0v1": 0.004,
    "1v2": 0.0101,
    "2v3": 0.0095,
    "3v4": 0.0137,
    "4v5": 0.0069
  },
  "pairwise_jsd": {
    "0v1": 0.060406,
    "1v2": 0.047034,
    "2v3": 0.003473,
    "3v4": 0.003026,
    "4v5": 0.002892
  },
  "ordinal_mae": 1.2542,
  "ordinal_accuracy": 0.3485,
  "top_features": [
    "freq_entropy",
    "surp_d1_mean",
    "surp_d2_mean"
  ]
}
notes: Generation completed normally (11.37 GPU-hours). Analysis step crashed on M010 bug (int(doc_id) on string 'code_py_0'). Bug was already patched in code (try/except at line 462-466). Worker re-ran analysis only → K*=2 confirmed. Results in results/exp_code_llama8b/.

=== exp_code_mistral7b ===
status: DONE
conclusion: success
metrics: {
  "k_star": 2,
  "pairwise_auc": {
    "0v1": 0.9191,
    "1v2": 0.6152,
    "2v3": 0.5293,
    "3v4": 0.5286,
    "4v5": 0.5099
  },
  "pairwise_auc_ci": {
    "0v1": 0.0017,
    "1v2": 0.012,
    "2v3": 0.0091,
    "3v4": 0.0104,
    "4v5": 0.006
  },
  "pairwise_jsd": {
    "0v1": 0.046984,
    "1v2": 0.011845,
    "2v3": 0.003717,
    "3v4": 0.003206,
    "4v5": 0.003083
  },
  "ordinal_mae": 1.3191,
  "ordinal_accuracy": 0.3243,
  "top3_features": [
    "freq_entropy",
    "surp_d2_mean",
    "surp_d1_mean"
  ]
}
notes: Log writes to /dev/pts/3 (terminal session), not a file. Progress inferred from data dir: depth_1.jsonl done (5500 lines), depth_2 in progress. No persistent log file for post-mortem analysis.

=== exp_code_qwen7b ===
status: DONE
conclusion: success
metrics: {
  "pairwise_auc": {
    "0v1": {
      "mean": 0.9051,
      "ci95_half": 0.0043,
      "folds": [
        0.9073,
        0.9012,
        0.912,
        0.9049,
        0.9003
      ]
    },
    "1v2": {
      "mean": 0.7276,
      "ci95_half": 0.0055,
      "folds": [
        0.7377,
        0.7254,
        0.724,
        0.722,
        0.7289
      ]
    },
    "2v3": {
      "mean": 0.5368,
      "ci95_half": 0.0145,
      "folds": [
        0.5179,
        0.5332,
        0.5275,
        0.5462,
        0.5593
      ]
    },
    "3v4": {
      "mean": 0.509,
      "ci95_half": 0.0055,
      "folds": [
        0.5029,
        0.5054,
        0.5085,
        0.5092,
        0.5191
      ]
    },
    "4v5": {
      "mean": 0.5139,
      "ci95_half": 0.0128,
      "folds": [
        0.5016,
        0.5317,
        0.5264,
        0.509,
        0.5007
      ]
    }
  },
  "pairwise_jsd": {
    "0v1": 0.061265,
    "1v2": 0.042256,
    "2v3": 0.00413,
    "3v4": 0.003198,
    "4v5": 0.003393
  },
  "k_star": 2,
  "ordinal": {
    "mae": 1.2651,
    "accuracy": 0.3423
  },
  "top_features": [
    {
      "name": "freq_entropy",
      "importance": 9730
    },
    {
      "name": "surp_d2_mean",
      "importance": 9236.2
    },
    {
      "name": "surp_d1_mean",
      "importance": 9126.2
    },
    {
      "name": "surp_d1_skew",
      "importance": 8833.4
    },
    {
      "name": "surp_std",
      "importance": 8110.2
    },
    {
      "name": "freq_kurtosis",
      "importance": 7838.6
    },
    {
      "name": "surp_mean",
      "importance": 7586
    },
    {
      "name": "surp_kurt",
      "importance": 6769.2
    },
    {
      "name": "hapax_ratio",
      "importance": 6636.4
    },
    {
      "name": "ttr",
      "importance": 6332.6
    }
  ]
}
notes: Attempts 1-3 failed: huggingface.co unreachable (000), httpx client closed during datasets.load_dataset. Attempt 4 success: copied depth_0.jsonl from exp_code_qwen1b5 (MD5 match), set HF_ENDPOINT=https://hf-mirror.com. PID 114228, GPU util 96%, 15211/24564 MiB. nvidia-smi verified.

=== olmo_arxiv_cross_scorer ===
status: DONE
conclusion: success
metrics: {
  "k_star": 1,
  "pairwise_auc": {
    "0v1": 0.9994,
    "1v2": 0.4996,
    "2v3": 0.4971,
    "3v4": 0.5091,
    "4v5": 0.536
  },
  "bootstrap_ci_95": {
    "0v1": [
      0.999,
      0.9997
    ],
    "1v2": [
      0.4828,
      0.5166
    ],
    "2v3": [
      0.4796,
      0.5138
    ],
    "3v4": [
      0.4922,
      0.5262
    ],
    "4v5": [
      0.5183,
      0.5533
    ]
  },
  "p_perm": {
    "0v1": 0.0001,
    "1v2": 0.51,
    "2v3": 0.6267,
    "3v4": 0.1488,
    "4v5": 0.0001
  },
  "scorer": "Qwen2.5-1.5B-Instruct",
  "key_finding": "OLMo-1B arXiv cross-scorer K*=1 confirmed. 1v2=0.4996 (chance). Sole exception to arXiv ceiling=3. All other models (Qwen/LLaMA/Mistral/Pythia) reach K*=3."
}

=== olmo_c4_cross_scorer ===
status: DONE
conclusion: success
metrics: {
  "k_star": 1,
  "pairwise_auc": {
    "0v1": 0.986,
    "1v2": 0.4999,
    "2v3": 0.4982,
    "3v4": 0.5016,
    "4v5": 0.4946
  },
  "bootstrap_ci_95": {
    "0v1": [
      0.9842,
      0.9877
    ],
    "1v2": [
      0.4885,
      0.5112
    ],
    "2v3": [
      0.4869,
      0.5096
    ],
    "3v4": [
      0.4903,
      0.513
    ],
    "4v5": [
      0.483,
      0.506
    ]
  },
  "p_perm": {
    "0v1": 0.0001,
    "1v2": 0.5056,
    "2v3": 0.6286,
    "3v4": 0.3955,
    "4v5": 0.8183
  },
  "scorer": "Qwen2.5-1.5B-Instruct",
  "key_finding": "OLMo-1B C4 cross-scorer K*=1. 1v2=0.4999 (chance). Consistent across 3 pipelines. Confirms OLMo as competence-limited weak model."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f0e7704e-a318-44fa-a652-4256723f87ff",
  "isSidechain": true,
  "promptId": "4b1e9bd3-a514-43a0-8b8b-ee4e7298d832",
  "agentId": "aa09eae889717e82e",
  "type": "user",
  "uuid": "358b0106-0e42-4ddd-b023-4e9d357d7d28",
  "sourceToolAssistantUUID": "f0e7704e-a318-44fa-a652-4256723f87ff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d0900953-8129-4d2a-95a5-2cd8b707bc5a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-25T19:47:24.083Z_

All 30 experiments are found and extracted. Here is the complete report:

---

All 30 target experiments were found in the registry. Here are full metrics for each:

---

**1. exp_023_domain_ablation (Wiki Qwen)**
- status: DONE, conclusion: success
- K_star: 2
- 1v2_auc: 0.6193, 2v3_auc: 0.5498
- all_folds_above_060: true, top_feature: freq_entropy, ordinal_accuracy: 0.377

---

**2. wiki_domain_mistral (Wiki Mistral)**
- status: DONE, conclusion: success
- k_star: 1, scorer: Qwen2.5-1.5B-Instruct
- pairwise_auc: 0v1=0.9614, 1v2=0.5576, 2v3=0.5193, 3v4=0.5172, 4v5=0.5011
- bootstrap_ci_bonf 1v2: [0.5434, 0.5716] — CI upper < θ=0.60, K*=1 confirmed
- bonf_p: 0v1=0.0005, 1v2=0.0005, 2v3=0.002, 3v4=0.01, 4v5=1

---

**3. wiki_domain_llama (Wiki LLaMA)**
- status: DONE, conclusion: success
- k_star: 1, scorer: Qwen2.5-1.5B-Instruct
- pairwise_auc: 0v1=0.9321, 1v2=0.5919, 2v3=0.5379, 3v4=0.5105, 4v5=0.5051
- bootstrap_ci_bonf 1v2: [0.5788, 0.6049] — point estimate < θ, borderline K*=1 by convention
- bonf_p: 0v1=0.0005, 1v2=0.0005, 2v3=0.0005, 3v4=0.231, 4v5=1

---

**4. exp_024_arxiv_domain (arXiv experiments)**
- status: DONE, conclusion: success
- K_star: 3
- pairwise_auc: 0v1=0.9946, 1v2=0.858, 2v3=0.6427, 3v4=0.5437, 4v5=0.5294
- bootstrap_ci 2v3: [0.6275, 0.6575], CI lower > θ=0.60 — K*=3 confirmed
- bootstrap_ci 1v2: [0.848, 0.868], all p_perm ≤0.0006

---

**5. arxiv_multi_source (arXiv multi-source)**
- status: DONE, conclusion: success
- k_star: 3 (pooled Qwen-1.5B + Pythia-1.4B + OLMo-1B)
- pairwise_auc (pooled): 0v1=0.9948, 1v2=0.8581, 2v3=0.6436, 3v4=0.544, 4v5=0.5299
- per_model 2v3 AUC: Qwen-1.5B=0.6437, Pythia-1.4B=0.6484, Pooled=0.6565
- bootstrap_ci_bonf 2v3: Qwen [0.629,0.659], Pythia [0.634,0.663], Pooled [0.647,0.667] — all lower > θ

---

**6. code_domain_mistral (Code Mistral)**
- status: DONE, conclusion: success
- k_star: 2, scorer: Qwen2.5-1.5B-Instruct
- pairwise_auc: 0v1=0.9189, 1v2=0.615, 2v3=0.5292, 3v4=0.5286, 4v5=0.5099
- bootstrap_ci_bonf 1v2: [0.6024, 0.6281] — CI lower > θ, statistically confirmed despite borderline AUC
- bonf_p: all pairs ≤0.0005 except 4v5=0.187

---

**7. code_domain_qwen7b (Code Qwen-7B)**
- status: DONE, conclusion: success
- k_star: 2, scorer: Qwen2.5-1.5B-Instruct
- pairwise_auc: 0v1=0.905, 1v2=0.7273, 2v3=0.5367, 3v4=0.5088, 4v5=0.5137
- bootstrap_ci_bonf 1v2: [0.7153, 0.7389] — well above θ, scale-invariant within Qwen family

---

**8. code_domain_olmo (Code OLMo)**
- status: DONE, conclusion: success
- k_star: 1, scorer: Qwen2.5-1.5B-Instruct
- pairwise_auc: 0v1=0.9996, 1v2=0.5567, 2v3=0.5, 3v4=0.5, 4v5=0.5
- pairwise_jsd: 0v1=0.334, 1v2=0.006, 2v3=0.003
- ordinal_mae: 1.289, ordinal_accuracy: 0.346
- OLMo full domain profile: C4=1, arXiv=1, Code=1 — uniformly competence-limited

---

**9. exp_015_neural_probe (neural probe)**
- status: DONE, conclusion: success
- k_star_qwen: 3, k_star_pythia: 2, k_star_olmo: 1
- qwen_pairwise_auc: 0v1=0.988, 1v2=0.702, 2v3=0.616, 3v4=0.59, 4v5=0.566
- pythia_pairwise_auc: 0v1=0.966, 1v2=0.676, 2v3=0.596, 3v4=0.555, 4v5=0.532
- olmo_pairwise_auc: 0v1=0.9773, 1v2=0.5054, 2v3=0.5056, 3v4=0.5032, 4v5=0.4999
- Notes: OLMo values from self-probe rerun (K*=1). Neural probe improves 2v3 AUC vs 15D features (Pythia +0.044, OLMo +0.039, Qwen +0.055) but only Qwen crosses θ=0.60 at 2v3.

---

**10. seed_gemma27b_c4_s42 (Gemma-27B)**
- status: DONE, conclusion: success
- K_star: 1 (cross-scored), scorer: Qwen2.5-1.5B-Instruct
- pairwise_auc_self: 0v1=0.9695, 1v2=0.6196, 2v3=0.5388, 3v4=0.5069, 4v5=0.5124
- pairwise_auc_qwen: 0v1=0.8874, 1v2=0.5894
- Self-scored K*=2 (1v2=0.6196), Qwen cross-scored K*=1 (1v2=0.5894 < θ). Self→Cross inflation: 1v2 Δ=-3.0pp, 0v1 Δ=-8.2pp.

---

**11. exp_pythia69b_c4_depth_chain_v2 (Pythia-6.9B)**
- status: DONE, conclusion: **failed**
- metrics: null (no metrics recorded)

---

**12. exp_gemma2b_depth (Gemma-2B)**
- status: DONE, conclusion: negative
- k_star: 1
- pairwise_auc: 0v1=0.9534, 1v2=0.5981, 2v3=0.5342, 3v4=0.503, 4v5=0.5026
- pairwise_auc_std: 0v1=0.003, 1v2=0.008, 2v3=0.013, 3v4=0.003, 4v5=0.013
- bootstrap_ci_1v2: [0.5882, 0.6076] — point estimate below θ
- jsd: 0v1=0.099, 1v2=0.009, 2v3=0.005, 3v4=0.004, 4v5=0.003
- ordinal_mae: 1.3152, ordinal_accuracy: 0.3321

---

**13. exp_arXiv_qwen1b5_crossscorer (arXiv cross-scorer Qwen-1.5B)**
- status: DONE, conclusion: success
- k_star: 3, scorer: Pythia-1.4B (cross-scoring Qwen-1.5B arXiv text)
- auc: 0v1=0.9748, 1v2=0.8105, 2v3=0.6317, 3v4=0.5437, 4v5=0.5294
- jsd: 0v1=0.154, 1v2=0.067, 2v3=0.019, 3v4=0.009, 4v5=0.007
- ordinal_mae: 0.9017, ordinal_accuracy: 0.4402
- arXiv K*=3 scorer-independent confirmed

---

**14. exp_arXiv_llama8b_crossscorer (arXiv cross-scorer LLaMA-8B)**
- status: DONE, conclusion: success
- k_star: 3, scorer: pythia-1.4b
- auc: 0v1=0.9629, 1v2=0.8433, 2v3=0.6201, 3v4=0.523, 4v5=0.5245
- jsd: 0v1=0.1214, 1v2=0.0815, 2v3=0.0195, 3v4=0.0083, 4v5=0.0082
- ordinal_mae: 0.9025, ordinal_accuracy: 0.4407

---

**15. exp_arXiv_mistral7b_crossscorer (arXiv cross-scorer Mistral-7B)**
- status: DONE, conclusion: success
- k_star: 3, scorer: pythia-1.4b
- auc: 0v1=0.9798, 1v2=0.8141, 2v3=0.6075, 3v4=0.5489, 4v5=0.5391
- jsd: 0v1=0.136, 1v2=0.078, 2v3=0.020, 3v4=0.011, 4v5=0.009
- ordinal_mae: 0.9061, ordinal_accuracy: 0.4412
- Notes: Max AUC delta vs Qwen scorer = 0.02 at 2v3. K*=3 scorer-independent for Mistral arXiv.

---

**16. exp_arXiv_qwen7b_crossscorer (arXiv cross-scorer Qwen-7B)**
- status: DONE, conclusion: **negative** (K* drops 3→2 under cross-scorer)
- k_star: 2, scorer: Pythia-1.4B (cross-scoring Qwen-7B arXiv text)
- auc: 0v1=0.9575, 1v2=0.8171, 2v3=0.5989, 3v4=0.5417, 4v5=0.5192
- jsd: 0v1=0.137, 1v2=0.060, 2v3=0.014, 3v4=0.009, 4v5=0.007
- ordinal_mae: 0.9617, ordinal_accuracy: 0.4255
- Notes: 2v3 AUC=0.5989 < θ=0.60, mild Qwen family bias (~0.027 AUC at 2v3) inflated original K*=3.

---

**17. exp_wiki_scorer_confound (Wiki scorer confound)**
- status: DONE, conclusion: **negative** (confound confirmed)
- k_star: 1, confound_verdict: confirmed
- auc: 0v1=0.9404, 1v2=0.587, 2v3=0.5456, 3v4=0.525, 4v5=0.5172
- critical_delta_1v2: -0.0238

---

**18. exp_wiki_scorer_confound_1b5 (Wiki scorer confound 1.5B)**
- status: DONE, conclusion: **negative** (confound confirmed)
- k_star: 1, confound_verdict: confirmed
- auc: 0v1=0.9729, 1v2=0.5994, 2v3=0.533, 3v4=0.5214, 4v5=0.5068
- jsd_0v1: 0.0886, ordinal_mae: 1.2995, ordinal_accuracy: 0.3466

---

**19. exp_wiki_qwen7b (Wiki Qwen-7B)**
- status: DONE, conclusion: success
- K_star: 2
- auc: 0v1=0.9673, 1v2=0.6108, 2v3=0.5562, 3v4=0.5297, 4v5=0.529
- jsd: 0v1=0.084, 1v2=0.011, 2v3=0.006, 3v4=0.005, 4v5=0.004
- ordinal_mae: 1.2501, ordinal_accuracy: 0.3532

---

**20. exp_wiki_llama8b (Wiki LLaMA-8B)**
- status: DONE, conclusion: **negative**
- K_star: 1
- auc: 0v1=0.9316, 1v2=0.5954, 2v3=0.5392, 3v4=0.5221, 4v5=0.5212
- jsd: 0v1=0.062, 1v2=0.009
- ordinal_mae: 1.2954, ordinal_accuracy: 0.3313

---

**21. exp_wiki_mistral7b (Wiki Mistral-7B)**
- status: DONE, conclusion: success
- K_star: 1
- auc: 0v1=0.9607, 1v2=0.5552, 2v3=0.5236, 3v4=0.5181, 4v5=0.5012
- jsd: 0v1=0.054, 1v2=0.006, 2v3=0.004, 3v4=0.003, 4v5=0.003
- ordinal_mae: 1.3445, ordinal_accuracy: 0.3273

---

**22. exp_arXiv_llama8b (arXiv LLaMA-8B)**
- status: DONE, conclusion: success
- K_star: 3
- auc: 0v1=0.9754, 1v2=0.8447, 2v3=0.6215, 3v4=0.5362, 4v5=0.5331
- jsd: 0v1=0.130, 1v2=0.079, 2v3=0.018
- ordinal_acc: 0.4549, ordinal_mae: 0.8806

---

**23. exp_arXiv_mistral7b (arXiv Mistral-7B)**
- status: DONE, conclusion: success
- k_star: 3
- pairwise_auc: 0v1=0.9848, 1v2=0.8201, 2v3=0.6275, 3v4=0.5295, 4v5=0.5295
- jsd: 0v1=0.142, 1v2=0.076, 2v3=0.019, 3v4=0.010, 4v5=0.009
- ordinal_mae: 0.8958, ordinal_accuracy: 0.4474
- top_features: freq_entropy, surp_std, surp_d1_skew, surp_mean, surp_d2_mean

---

**24. exp_arXiv_qwen7b (arXiv Qwen-7B)**
- status: DONE, conclusion: success
- k_star: 3
- pairwise_auc: 0v1=0.983, 1v2=0.835, 2v3=0.626, 3v4=0.544, 4v5=0.513
- pairwise_jsd: 0v1=0.166, 1v2=0.067, 2v3=0.016, 3v4=0.009, 4v5=0.006
- ordinal_mae: 0.9, ordinal_accuracy: 0.446

---

**25. exp_code_qwen1b5 (Code Qwen-1.5B)**
- status: DONE, conclusion: success
- K_star: 2, theta: 0.6
- auc: 0v1=0.9388, 1v2=0.7382, 2v3=0.53, 3v4=0.5022, 4v5=0.5219
- ci_1v2: [0.709, 0.767]
- jsd: 0v1=0.081, 1v2=0.044, 2v3=0.004
- ordinal_accuracy: 0.359, ordinal_mae: 1.204

---

**26. exp_code_llama8b (Code LLaMA-8B)**
- status: DONE, conclusion: success
- K_star: 2
- pairwise_auc: 0v1=0.9161, 1v2=0.7394, 2v3=0.5112, 3v4=0.52, 4v5=0.4996
- pairwise_auc_std: 0v1=0.004, 1v2=0.010, 2v3=0.010, 3v4=0.014, 4v5=0.007
- pairwise_jsd: 0v1=0.060, 1v2=0.047, 2v3=0.003, 3v4=0.003, 4v5=0.003
- ordinal_mae: 1.2542, ordinal_accuracy: 0.3485
- top_features: freq_entropy, surp_d1_mean, surp_d2_mean

---

**27. exp_code_mistral7b (Code Mistral-7B)**
- status: DONE, conclusion: success
- k_star: 2
- pairwise_auc: 0v1=0.9191, 1v2=0.6152, 2v3=0.5293, 3v4=0.5286, 4v5=0.5099
- pairwise_auc_ci (half-width): 0v1=0.0017, 1v2=0.012, 2v3=0.009, 3v4=0.010, 4v5=0.006
- pairwise_jsd: 0v1=0.047, 1v2=0.012, 2v3=0.004, 3v4=0.003, 4v5=0.003
- ordinal_mae: 1.3191, ordinal_accuracy: 0.3243
- top3_features: freq_entropy, surp_d2_mean, surp_d1_mean

---

**28. exp_code_qwen7b (Code Qwen-7B)**
- status: DONE, conclusion: success
- k_star: 2
- pairwise_auc (mean ± ci95_half): 0v1=0.9051±0.004, 1v2=0.7276±0.006, 2v3=0.5368±0.015, 3v4=0.509±0.006, 4v5=0.5139±0.013
- pairwise_jsd: 0v1=0.061, 1v2=0.042, 2v3=0.004, 3v4=0.003, 4v5=0.003
- ordinal_mae: 1.2651, ordinal_accuracy: 0.3423
- top features: freq_entropy (9730), surp_d2_mean (9236), surp_d1_mean (9126), surp_d1_skew (8833), surp_std (8110)

---

**29. olmo_arxiv_cross_scorer (OLMo arXiv cross-scorer)**
- status: DONE, conclusion: success
- k_star: 1, scorer: Qwen2.5-1.5B-Instruct
- pairwise_auc: 0v1=0.9994, 1v2=0.4996, 2v3=0.4971, 3v4=0.5091, 4v5=0.536
- bootstrap_ci_95 1v2: [0.4828, 0.5166]
- p_perm: 0v1=0.0001, 1v2=0.51 (not significant)
- OLMo sole exception to arXiv ceiling=3; all other models reach K*=3

---

**30. olmo_c4_cross_scorer (OLMo C4 cross-scorer)**
- status: DONE, conclusion: success
- k_star: 1, scorer: Qwen2.5-1.5B-Instruct
- pairwise_auc: 0v1=0.986, 1v2=0.4999, 2v3=0.4982, 3v4=0.5016, 4v5=0.4946
- bootstrap_ci_95 1v2: [0.4885, 0.5112]
- p_perm: 0v1=0.0001, 1v2=0.5056 (not significant)
- Consistent across all 3 OLMo pipelines; confirms OLMo as competence-limited weak model

---

**Summary notes on special cases:**
- `exp_pythia69b_c4_depth_chain_v2`: failed with no metrics (the v3/nuc reruns are the usable Pythia-6.9B results)
- `exp_arXiv_qwen7b_crossscorer`: K* drops 3→2 under cross-scorer (Qwen family bias at 2v3 ~0.027 AUC)
- `exp_wiki_scorer_confound` and `exp_wiki_scorer_confound_1b5`: both confirm scorer confound on Wikipedia
- `seed_gemma27b_c4_s42`: uses cross-scored K*=1 (self-scored would be K*=2)
- `exp_gemma2b_depth`: borderline K*=1 (1v2=0.5981, CI upper crosses θ but point estimate below)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "358b0106-0e42-4ddd-b023-4e9d357d7d28",
  "isSidechain": true,
  "agentId": "aa09eae889717e82e",
  "requestId": "req_011CbPryW1MQzVmf6Dy2HE63",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d37bc103-0392-44e5-8411-e698067d779d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "d0900953-8129-4d2a-95a5-2cd8b707bc5a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01UDRTcD5ueNXhAZmpkN3eEG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11017,
      "cache_read_input_tokens": 68179,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11017,
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
