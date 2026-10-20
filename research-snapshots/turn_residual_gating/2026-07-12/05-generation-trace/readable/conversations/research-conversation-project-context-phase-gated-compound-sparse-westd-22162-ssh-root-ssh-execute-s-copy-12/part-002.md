# Research conversation: <project_context> # 项目: phase-gated-compound-sparse ## 运行环境 - 服务器名: westd-22162 - SSH 账户: root（调用 ssh_execute / submit_t — Part 2 of 2

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue (July export snapshot)** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../research-conversation-project-context-phase-gated-compound-sparse-westd-22162-ssh-root-ssh-execute-s-copy-12.md) · [Structured JSON](../../../sessions/5d/5d6c63670e1f24e42a24.json)

## Round 1

### Assistant

_source line 198 · 2026-05-14T03:21:20.739Z_

完成。

**脚本**: `/root/autodl-tmp/pacs/analysis/bootstrap_phase_gradient.py`

**Dry-run 结果** (s=0.15, importance + random):

| 指标 | Importance | Random |
|---|---|---|
| Gradient (median_low/median_high) | **14.27** [11.97, 17.42] | **1.17** [0.93, 1.60] |
| Cohen's d (low vs high) | 0.71 | 0.01 |
| MW-U p (low vs high) | 2.98e-116 | 0.352 (ns) |
| Imp vs Rnd gradient p | < 0.001 *** | |

**关键发现**: Importance masking 下 low-sparsity phase 的 II 是 high-sparsity 的 ~14×，CI 远离 1；random masking gradient ~1（无相位依赖）。差异 p < 0.001，phase gradient 统计显著。

**技术说明**: 因 profiling_results.json 不保存 per-segment 原始 II 值，脚本使用 log-normal 参数化重建（精确匹配存储的 mean 和 median），然后做 bootstrap resample。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a3755cb6-6965-400e-a7e6-1a2b78018980",
  "isSidechain": false,
  "requestId": "req_011Cb1jygeARh5dry9tt2q9h",
  "type": "assistant",
  "uuid": "4a8160b5-eb32-4dd0-a400-2a8a2d64ca6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "995bb223-12dd-4ba6-a083-6c3b8aea1195",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RDeeXz297AeGCWrRFNUXwX",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 412,
      "cache_read_input_tokens": 124264,
      "output_tokens": 341,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 412,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 341,
          "cache_read_input_tokens": 124264,
          "cache_creation_input_tokens": 412,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 412
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


### Runtime record

_source line 199_

```json
{
  "type": "last-prompt",
  "leafUuid": "4a8160b5-eb32-4dd0-a400-2a8a2d64ca6b",
  "sessionId": "995bb223-12dd-4ba6-a083-6c3b8aea1195"
}
```

---


### Runtime record

_source line 200_

```json
{
  "type": "ai-title",
  "aiTitle": "Write M1' bootstrap CI analysis script",
  "sessionId": "995bb223-12dd-4ba6-a083-6c3b8aea1195"
}
```

---
