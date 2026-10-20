# Research conversation: [CRON] 实验进程已正常退出，状态已转为 ANALYZING，需要你分析结果并推进到 DONE。 详情: Process exited cleanly, W&B data available - exp_id: plan_016_lla — Part 2 of 2

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction (July export snapshot)** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../research-conversation-cron-analyzing-done-process-exited-cleanly-w-b-data-available-exp-id-plan-016-copy-3.md) · [Structured JSON](../../../sessions/50/501334035f9a1400c2f9.json)

## Round 1

### Tool call

_source line 167 · 2026-05-16T14:20:17.282Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file · `toolu_018vtZsL3KWDy76k7rVE6uTB`</summary>

````json
{
  "project": "faith-evidence-ie",
  "file": "memory.md",
  "content": "# RSFT Scoring Commands\n\n## 验证结果\n\n- **脚本路径**: `/root/autodl-tmp/freige/training/rsft_score_filter.py`\n- **模块导入**: `from freige.training.rsft_score_filter import main` ✅ OK\n- **NLI 模型**: `/root/autodl-tmp/.hf_cache/models--cross-encoder--nli-deberta-v3-base/snapshots/6c749ce3425cd33b46d187e45b92bbf96ee12ec7`\n\n## Argparse 参数列表\n\n| 参数 | 必填 | 默认值 | 说明 |\n|------|------|--------|------|\n| `--input_dir` | ✅ | - | rsft_generate 输出目录（含 generations.jsonl） |\n| `--output_path` | ✅ | - | 筛选结果输出目录 |\n| `--nli_model_path` | ❌ | (内置默认) | NLI 模型路径 |\n| `--nli_device` | ❌ | auto | NLI 模型运行设备 |\n| `--tau` | ❌ | 0.5 | CED tau 阈值 |\n| `--scoring_mode` | ❌ | ced | {ced, flat_nli} |\n| `--format_weight` | ❌ | 0.2 | combined_score 中 format_reward 权重 |\n| `--f1_weight` | ❌ | 0.4 | combined_score 中 f1_reward 权重 |\n| `--ced_weight` | ❌ | 0.4 | combined_score 中 ced_reward 权重 |\n| `--format_threshold` | ❌ | 0.5 | format_reward 最低阈值 |\n| `--f1_threshold` | ❌ | 0.1 | f1_reward 最低阈值 |\n| `--ced_threshold` | ❌ | 0.0 | ced_reward 最低阈值 |\n| `--selection_strategy` | ❌ | top_pct | {threshold, top_k, top_pct} |\n| `--top_k` | ❌ | 2 | top_k 策略: 每个文档取 top-K |\n| `--top_pct` | ❌ | 25 | top_pct 策略: 每个文档取 top N% |\n\n## Candidate Generation 状态 (2026-05-16 22:03)\n\n- **1.7B**: GPU 0, 57/3053 docs completed, output → `/root/autodl-tmp/freige/outputs/rsft_candidates_1_7b`\n- **8B**: GPU 3, 47/3053 docs completed, output → `/root/autodl-tmp/freige/outputs/rsft_candidates_8b`\n- **LLaMA-3.1-8B**: GPU 1, 刚提交 (2026-05-16 14:16 UTC), output → `/root/autodl-tmp/rsft_candidates_llama_3_1_8b`\n- **预计完成时间**: ~10-13 小时（1.7B 更快）\n\n## 命令模板\n\n### 1.7B CED Scoring\n\n```bash\nbash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=0 python -m freige.training.rsft_score_filter \\\n    --input_dir /root/autodl-tmp/freige/outputs/rsft_candidates_1_7b \\\n    --output_path /root/autodl-tmp/freige/outputs/rsft_scored_1_7b \\\n    --nli_model_path /root/autodl-tmp/.hf_cache/models--cross-encoder--nli-deberta-v3-base/snapshots/6c749ce3425cd33b46d187e45b92bbf96ee12ec7 \\\n    --nli_device cuda:0 \\\n    --scoring_mode ced \\\n    --selection_strategy top_pct --top_pct 25\"\n```\n\n### 8B CED Scoring\n\n```bash\nbash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && CUDA_VISIBLE_DEVICES=3 python -m freige.training.rsft_score_filter \\\n    --input_dir /root/autodl-tmp/freige/outputs/rsft_candidates_8b \\\n    --output_path /root/autodl-tmp/freige/outputs/rsft_scored_8b \\\n    --nli_model_path /root/autodl-tmp/.hf_cache/models--cross-encoder--nli-deberta-v3-base/snapshots/6c749ce3425cd33b46d187e45b92bbf96ee12ec7 \\\n    --nli_device cuda:0 \\\n    --scoring_mode ced \\\n    --selection_strategy top_pct --top_pct 25\"\n```\n\n### 备选: flat_nli 模式（作为对比实验）\n\n将 `--scoring_mode ced` 替换为 `--scoring_mode flat_nli`，输出路径改为 `rsft_scored_1_7b_flat_nli` / `rsft_scored_8b_flat_nli`。\n\n## GPU 需求\n\n- CED scoring 使用 DeBERTa-v3-base NLI 模型，~400MB 显存，**任意一张卡即可**\n- 计算量主要在 CPU 侧（JSON 解析、F1 计算）+ 少量 NLI 推理\n- 可与其他轻量任务共享 GPU，但建议等 generation 完成后使用同一张卡避免冲突\n\n## 注意事项\n\n1. **等 generation 完成再执行 scoring**——当前两个 gen 任务仍在运行（GPU 0 和 GPU 3 被占用）\n2. **CUDA_VISIBLE_DEVICES 必须设置**（C002/C003 约束），`--nli_device cuda:0` 指的是 CUDA_VISIBLE_DEVICES 映射后的设备 0\n3. 输出包含 3 个文件: `rsft_train.jsonl`（SFT 训练数据）、`rsft_scores.jsonl`（带分数完整记录）、`rsft_report.json`（统计报告）\n4. 默认 top_pct=25 意味着每个文档的 8 个 generation 中取分数最高的 2 个（25% of 8 = 2）\n5. 如需 top_k 策略：改 `--selection_strategy top_k --top_k 3`\n\n## Evidence Tax 跨家族跨规模规律 (2026-05-16)\n\n**核心发现**：evidence tax（要求模型同时输出 evidence 的代价）随模型规模消失，且跨模型家族成立。\n\n| Model | Size | Evidence Tax (rel_f1 pp) | 备注 |\n|-------|------|--------------------------|------|\n| Qwen3-1.7B | 1.7B | -8.42 (反转) | 受严重截断混淆 (50.9%) |\n| Qwen3-4B | 4B | +8.44 | 基线模型 |\n| Qwen3-8B | 8B | +0.21 ≈ 0 | D079 确认 |\n| LLaMA-3.1-8B | 8B | +1.10 ≈ 0 | 跨家族验证 |\n\n**决策原因**：\n- 8B 模型的 evidence tax ≈ 0 说明生成 evidence 不是 rel_f1 下降的根因——4B 的 8pp tax 可能是容量不足导致多任务干扰\n- 1.7B 反转很可能是假象：50.9% 截断率意味着大量 no-evidence 预测被截断丢失 relation triples，人为压低了 no-evidence 分数\n- LLaMA 的 with-evidence rel_f1=0.5514 是所有模型最高，表明 8B 模型可以同时做好抽取和 evidence 生成\n\n**对 Paper Story 的影响**：\n- Claim 1 可升级为 architecture-independent 结论\n- 4B 的 evidence tax 可解释为 capacity bottleneck，而非 evidence generation 本身的固有代价\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6bc2996f-f75b-406b-9cf3-3d51716954e4",
  "isSidechain": false,
  "requestId": "req_011Cb6PoNQDYTmQkKR23P2mb",
  "type": "assistant",
  "uuid": "18316c71-3af1-452c-ad66-d6b5e7a32d0c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/agent_66be7425",
  "sessionId": "fcf4799b-8941-465e-af7d-b1a6d7adc112",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016FoEEVsKacguLcofh7hK8F",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2380,
      "cache_read_input_tokens": 95878,
      "output_tokens": 2521,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2380,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2521,
          "cache_read_input_tokens": 95878,
          "cache_creation_input_tokens": 2380,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2380
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

_source line 168 · 2026-05-16T14:20:17.301Z_

<details><summary>↩ Tool result · `toolu_018vtZsL3KWDy76k7rVE6uTB`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/memory.md\", \"saved\": true}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "18316c71-3af1-452c-ad66-d6b5e7a32d0c",
  "isSidechain": false,
  "promptId": "4b53c7d5-6da7-4a38-aef6-36a26239da81",
  "type": "user",
  "uuid": "e2d7d862-098c-42ca-b4ea-76a0c4d639c6",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/memory.md\\\", \\\"saved\\\": true}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/memory.md\", \"saved\": true}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "18316c71-3af1-452c-ad66-d6b5e7a32d0c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/.claude/sessions/agent_66be7425",
  "sessionId": "fcf4799b-8941-465e-af7d-b1a6d7adc112",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---
