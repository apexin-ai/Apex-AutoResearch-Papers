# Research conversation: <project_context> # 项目: symb_invariant_consensus ## 运行环境 - 服务器名: westd-25068 - SSH 连接命令: ssh westd-25068 # 必须用此命令，~/.ssh — Part 2 of 2

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction (July export snapshot)** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../research-conversation-project-context-symb-invariant-consensus-westd-25068-ssh-ssh-westd-25068-ssh-copy-210.md) · [Structured JSON](../../../sessions/7c/7c8475b858b3785de070.json)

## Round 1

### Assistant

_source line 344 · 2026-05-20T10:42:42.568Z_

## 报告

### 下载方式
**aria2c 多线程 + ModelScope CDN** 成功。HF mirror 和 ModelScope Python SDK 都在大文件下载时卡住（xet bridge 限速 / 连接中断），最终用 `aria2c -x 16` 直接从 ModelScope CDN 下载 pytorch_model.bin，17 MB/s，约 90 秒完成。小文件（config/tokenizer/vocab）由 HF mirror 的 `snapshot_download` 先行下载成功。

模型存放在根分区 `/root/models/deberta-large-mnli/`（数据盘 `/root/autodl-tmp` 仅剩 1.7GB 不够用）。

### 模型大小
**406.2M 参数**，pytorch_model.bin = 1.51 GB

### 实验结果

| 方法 | Accuracy | Correct/Total | Delta vs SC |
|------|----------|---------------|-------------|
| SC baseline | 54.41% | 111/204 | — |
| SICA baseline | 59.31% | 121/204 | +4.90pp |
| **NLI standalone** | **49.51%** | 101/204 | **-4.90pp** |
| NLI as SC verifier (abstain on disagree) | 68.48% (coverage 45.1%) | 63/92 | — |
| **NLI + SC combo (w=1)** | **57.84%** | 118/204 | **+3.43pp** |
| **NLI + SC combo (w=3)** | **58.82%** | 120/204 | **+4.41pp** |

### 关键发现
- DeBERTa-large-mnli 单独做 NLI 只有 49.51%，严重低估 "Unknown"（预测 22 个 vs 真实 69 个），偏向 True/False
- 但作为投票成员加入 SC（weight=3），达到 58.82%，比 SC 提高 +4.41pp，接近 SICA（59.31%）
- DeBERTa 与 SC 一致时（45.1% 的问题）准确率高达 68.48%，说明在确定性高的子集上有互补价值

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "13a461c7-0f12-41ca-91be-d44b52ce244d",
  "isSidechain": false,
  "requestId": "req_011CbDgV21dchmJufDAd9Lr7",
  "type": "assistant",
  "uuid": "1a0ccaac-d3be-49e1-8953-74bb24fac685",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "dc0d53dd-8a2d-41a4-b3ab-8a15a4c046cc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y2wg2PVUzSRJ5SUDkd7kWG",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 651,
      "cache_read_input_tokens": 91099,
      "output_tokens": 628,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 651,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 628,
          "cache_read_input_tokens": 91099,
          "cache_creation_input_tokens": 651,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 651
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

_source line 345_

```json
{
  "type": "last-prompt",
  "leafUuid": "1a0ccaac-d3be-49e1-8953-74bb24fac685",
  "sessionId": "dc0d53dd-8a2d-41a4-b3ab-8a15a4c046cc"
}
```

---


### Runtime record

_source line 346_

```json
{
  "type": "ai-title",
  "aiTitle": "Download DeBERTa MNLI and run Direction R",
  "sessionId": "dc0d53dd-8a2d-41a4-b3ab-8a15a4c046cc"
}
```

---
