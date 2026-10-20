# Research conversation: <project_context> # 项目: trace-verdict-study ## 运行环境 - 服务器名: westd-11235 - SSH 账户: root（调用 ssh_execute / submit_training_ — Part 2 of 2

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects (July export snapshot)** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../research-conversation-project-context-trace-verdict-study-westd-11235-ssh-root-ssh-execute-submit-tr-copy-33.md) · [Structured JSON](../../../sessions/36/36fa33e53e36c4bf7966.json)

## Round 1

### Assistant

_source line 354 · 2026-05-18T14:07:39.871Z_

完成。4 模型 exception_only calibration 结果：

| Model | Accuracy | ECE | MCE | Brier |
|---|---|---|---|---|
| **Qwen-7B** | 0.9983 | 0.0027 | 0.8355 | 0.0013 |
| **Qwen-1.5B** | 0.9983 | 0.0020 | 0.7549 | 0.0013 |
| **DeepSeek-6.7B** | 0.9933 | 0.0064 | 0.7756 | 0.0061 |
| **CodeLlama-13B** | 0.9983 | 0.0020 | 0.0411 | 0.0013 |

关键发现：
- ECE 跨模型一致性好（0.002-0.006），exception-only 微调在不同架构/尺寸上均产生良好校准
- 3/4 模型精度相同（99.83%），DeepSeek 略低（99.33%）
- CodeLlama-13B 校准最优：MCE 仅 0.041（其余模型的高 MCE 是 1-sample bin 的统计伪影）
- DeepSeek 有独特失败模式：[0.90, 0.95) 区间 7 个样本置信度 0.918 但准确率仅 14.3%（过度自信的误分类）

结果已保存至 `artifacts/cross_model_calibration.md` 并注册。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f44a92c7-fa65-46dc-9a83-ea52f9dcc265",
  "isSidechain": false,
  "requestId": "req_011CbAAVzrwqeM8feTqvKWMv",
  "type": "assistant",
  "uuid": "84951af5-0bfa-4fff-815e-1fe04bc89884",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study",
  "sessionId": "ba0781db-d5df-4732-bd8b-6a170f64e9ce",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017xXihhxkTcVuZre15HohdF",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 579,
      "cache_read_input_tokens": 92677,
      "output_tokens": 427,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 579,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 427,
          "cache_read_input_tokens": 92677,
          "cache_creation_input_tokens": 579,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 579
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

_source line 355_

```json
{
  "type": "last-prompt",
  "leafUuid": "84951af5-0bfa-4fff-815e-1fe04bc89884",
  "sessionId": "ba0781db-d5df-4732-bd8b-6a170f64e9ce"
}
```

---


### Runtime record

_source line 356_

```json
{
  "type": "ai-title",
  "aiTitle": "Calculate calibration metrics for 4 exception_only models",
  "sessionId": "ba0781db-d5df-4732-bd8b-6a170f64e9ce"
}
```

---
