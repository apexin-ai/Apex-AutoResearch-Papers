# Research conversation: <project_context> # 项目: contamcal-irt-calibration ## 运行环境 - 服务器名: cqa1-21977 - SSH 连接命令: ssh connect.cqa1.seetacloud.com — Part 2 of 2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families (July export snapshot)** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../research-conversation-project-context-contamcal-irt-calibration-cqa1-21977-ssh-ssh-connect-cqa1-seet-copy-1055.md) · [Structured JSON](../../../sessions/09/091a0caa5c608f336661.json)

## Round 1

### Assistant

_source line 276 · 2026-05-14T16:00:36.681Z_

<details><summary>Logged reasoning block</summary>

```text
Dramatic difference:

| Metric | Raw model | d000 model |
|--------|-----------|-----------|
| Unique predictions | 419 | 208 |
| Top 1 pred covers | 43 | **134** |
| Top 5 preds cover | 184 | **360** |
| Top 20 preds cover | 518 | **793** |

The d000 model's predictions are much more concentrated - 208 unique values vs 419 for raw. The top prediction alone covers 134 samples (vs 43 for raw). Top 20 predictions cover 793/1319 = 60% of all samples for d000 vs 518/1319 = 39% for raw.


The d000 model has clearly lost diversity in its predictions, collapsing to a narrow set of common outputs rather than reasoning through each problem individually. Let me check if the 1.5B variant shows the same pattern, but I'm already seeing the diagnosis: the SFT training on SlimOrca with those hyperparameters is causing catastrophic forgetting of chain-of-thought reasoning in math problems, which explains the 12.0% performance drop on GSM8K.

Looking at the specifics, the 3B model went from 419 unique predictions down to just 208, with "20" dominating the outputs. The MCQ benchmarks stay stable because they rely on probability scoring rather than generation. The 1.5B model retained its math ability at 65.4%, suggesting the 3B is more vulnerable to these particular training settings. This means the d100 versus d000 gap is artificially inflated by this collapse.

The real contamination signal should be around 9 percentage points when comparing d100 to the raw baseline, not the 57.7pp we're seeing. I should try lowering the learning rate for the 3B model, reducing the LoRA rank, or retraining with more conservative hyperparameters to preserve the base model's reasoning capability. I also want to check whether the 1.5B d000 has the same prediction diversity problem and look at how the d005 model performs.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa490943-6ea5-4818-ad68-4bdd41c033ae",
  "isSidechain": false,
  "requestId": "req_011Cb2jrApbtLMxxXTKzp1qF",
  "type": "assistant",
  "uuid": "3369ba1d-ff72-4cae-aee2-7e3c7f1e252f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "5bfc64b4-6f42-48ba-aa26-8171bcc7843f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016XFiEU7XkRrBeFVYyrkx5P",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1524,
      "cache_read_input_tokens": 104899,
      "output_tokens": 1447,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1524,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1447,
          "cache_read_input_tokens": 104899,
          "cache_creation_input_tokens": 1524,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1524
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


### Assistant

_source line 277 · 2026-05-14T16:00:36.792Z_

数据非常清楚。让我最后对比一下 1.5B d000 的分布，确认这是 3B 独有的问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3369ba1d-ff72-4cae-aee2-7e3c7f1e252f",
  "isSidechain": false,
  "requestId": "req_011Cb2jrApbtLMxxXTKzp1qF",
  "type": "assistant",
  "uuid": "f8b3a942-2df2-49d7-9a6d-b6d0a2e34855",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "5bfc64b4-6f42-48ba-aa26-8171bcc7843f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016XFiEU7XkRrBeFVYyrkx5P",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1524,
      "cache_read_input_tokens": 104899,
      "output_tokens": 1447,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1524,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1447,
          "cache_read_input_tokens": 104899,
          "cache_creation_input_tokens": 1524,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1524
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

_source line 278 · 2026-05-14T16:00:42.617Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01RkxLYFRQoxtaPY2PyHu7ZJ`</summary>

```json
{
  "server": "cqa1-21977",
  "command": "/root/miniconda3/bin/python -c \"\nimport json\n\n# 1.5B d000 aligned\nwith open('/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s42_aligned/eval_results.json') as f:\n    data = json.load(f)\ngsm = data['benchmarks']['gsm8k']\npreds = [item['pred'] for item in gsm['per_item']]\n\nfrom collections import Counter\npred_counts = Counter(str(p) for p in preds)\nprint('1.5B d000 - GSM8K accuracy:', gsm['accuracy'])\nprint('1.5B d000 - Unique predictions:', len(pred_counts))\nprint('1.5B d000 - top 1 pred covers:', pred_counts.most_common(1)[0][1])\nprint('1.5B d000 - top 5 preds cover:', sum(c for _, c in pred_counts.most_common(5)))\nprint('Top 5:', [(v,c) for v,c in pred_counts.most_common(5)])\nprint()\n\n# 3B d100 aligned\nwith open('/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_s42_aligned/eval_results.json') as f:\n    data2 = json.load(f)\ngsm2 = data2['benchmarks']['gsm8k']\npreds2 = [item['pred'] for item in gsm2['per_item']]\npred_counts2 = Counter(str(p) for p in preds2)\nprint('3B d100 - GSM8K accuracy:', gsm2['accuracy'])\nprint('3B d100 - Unique predictions:', len(pred_counts2))\nprint('3B d100 - top 1 pred covers:', pred_counts2.most_common(1)[0][1])\nprint('3B d100 - top 5 preds cover:', sum(c for _, c in pred_counts2.most_common(5)))\nprint('Top 5:', [(v,c) for v,c in pred_counts2.most_common(5)])\n\"\n",
  "warn": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f8b3a942-2df2-49d7-9a6d-b6d0a2e34855",
  "isSidechain": false,
  "requestId": "req_011Cb2jrApbtLMxxXTKzp1qF",
  "type": "assistant",
  "uuid": "db0b5abb-616d-4451-b1f5-76de320a485b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "5bfc64b4-6f42-48ba-aa26-8171bcc7843f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016XFiEU7XkRrBeFVYyrkx5P",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1524,
      "cache_read_input_tokens": 104899,
      "output_tokens": 1447,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1524,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1447,
          "cache_read_input_tokens": 104899,
          "cache_creation_input_tokens": 1524,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1524
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

_source line 279 · 2026-05-14T16:00:43.213Z_

<details><summary>↩ Tool result · `toolu_01RkxLYFRQoxtaPY2PyHu7ZJ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"1.5B d000 - GSM8K accuracy: 0.6542835481425322\\n1.5B d000 - Unique predictions: 395\\n1.5B d000 - top 1 pred covers: 39\\n1.5B d000 - top 5 preds cover: 173\\nTop 5: [('5', 39), ('3', 36), ('2', 35), ('4', 33), ('20', 30)]\\n\\n3B d100 - GSM8K accuracy: 0.6967399545109931\\n3B d100 - Unique predictions: 396\\n3B d100 - top 1 pred covers: 78\\n3B d100 - top 5 preds cover: 199\\nTop 5: [('250', 78), ('4', 31), ('5', 31), ('3', 30), ('12', 29)]\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "db0b5abb-616d-4451-b1f5-76de320a485b",
  "isSidechain": false,
  "promptId": "96b5e8b9-2b59-4bf4-9f95-cfc24e4ea82c",
  "type": "user",
  "uuid": "e5c7915f-548b-4e9c-8dcc-e00c5b4a11d0",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"1.5B d000 - GSM8K accuracy: 0.6542835481425322\\\\n1.5B d000 - Unique predictions: 395\\\\n1.5B d000 - top 1 pred covers: 39\\\\n1.5B d000 - top 5 preds cover: 173\\\\nTop 5: [('5', 39), ('3', 36), ('2', 35), ('4', 33), ('20', 30)]\\\\n\\\\n3B d100 - GSM8K accuracy: 0.6967399545109931\\\\n3B d100 - Unique predictions: 396\\\\n3B d100 - top 1 pred covers: 78\\\\n3B d100 - top 5 preds cover: 199\\\\nTop 5: [('250', 78), ('4', 31), ('5', 31), ('3', 30), ('12', 29)]\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.5}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"1.5B d000 - GSM8K accuracy: 0.6542835481425322\\n1.5B d000 - Unique predictions: 395\\n1.5B d000 - top 1 pred covers: 39\\n1.5B d000 - top 5 preds cover: 173\\nTop 5: [('5', 39), ('3', 36), ('2', 35), ('4', 33), ('20', 30)]\\n\\n3B d100 - GSM8K accuracy: 0.6967399545109931\\n3B d100 - Unique predictions: 396\\n3B d100 - top 1 pred covers: 78\\n3B d100 - top 5 preds cover: 199\\nTop 5: [('250', 78), ('4', 31), ('5', 31), ('3', 30), ('12', 29)]\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5}}"
    }
  },
  "sourceToolAssistantUUID": "db0b5abb-616d-4451-b1f5-76de320a485b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "5bfc64b4-6f42-48ba-aa26-8171bcc7843f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Assistant

_source line 280 · 2026-05-14T16:01:08.888Z_

<details><summary>Logged reasoning block</summary>

```text
This confirms everything:

| Model | GSM8K | Unique preds | Top 1 covers | Top 5 cover |
|-------|-------|-------------|-------------|-------------|
| 3B raw | 60.5% | 419 | 43 | 184 |
| 3B d000 | 12.0% | **208** | **134** | **360** |
| 3B d100 | 69.7% | 396 | 78 | 199 |


| 1.5B d000 | 65.4% | 395 | 39 | 173 |

The 3B d000 model is clearly suffering from catastrophic forgetting—it's only generating 208 unique predictions compared to 395-419 for the healthy models, and its top prediction covers 134 samples while the others range from 39-78. The 3B d100 recovered well with 396 unique predictions, showing the issue is specific to that particular training run.

What's interesting is that d100's most common prediction "250" appears 78 times versus the raw model's top answer at 43 times, suggesting the contaminated training data biased it slightly toward GSM8K answers, but the overall diversity remained intact. Now I'm ready to synthesize the full diagnosis and recommendations.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e5c7915f-548b-4e9c-8dcc-e00c5b4a11d0",
  "isSidechain": false,
  "requestId": "req_011Cb2ju5H4QjLvEJfzYTpKe",
  "type": "assistant",
  "uuid": "953d31fb-51e9-4586-be30-910a5a6aa141",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "5bfc64b4-6f42-48ba-aa26-8171bcc7843f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016pRtAjtZiSTwEV1sKMSLoM",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1747,
      "cache_read_input_tokens": 106423,
      "output_tokens": 1491,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1747,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1491,
          "cache_read_input_tokens": 106423,
          "cache_creation_input_tokens": 1747,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1747
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


### Assistant

_source line 281 · 2026-05-14T16:01:31.480Z_

诊断完成。以下是完整结论。

---

## 诊断结果：3B d000 GSM8K 12.0% 根因

### 结论：**不是 parsing/eval bug，是 SFT 导致 3B 模型生成能力崩溃**

### 证据链

**1. 跨模型对比排除 eval 代码问题**

| Model | GSM8K | MMLU | ARC |
|-------|-------|------|-----|
| 3B raw (无 SFT) | **60.5%** | — | — |
| 3B d000 (SFT SlimOrca) | **12.0%** | 63.4% | 82.8% |
| 3B d100 (SFT+contamination) | **69.7%** | — | — |
| 1.5B d000 (同样 SFT) | **65.4%** | — | — |

- MMLU/ARC（logprob 评估）正常 → eval 代码和 prompt 没问题
- 1.5B d000 GSM8K 正常 → 不是 SlimOrca 数据本身的问题
- **问题仅出现在 3B + GSM8K（生成式评估）**

**2. 预测分布确认生成质量崩溃**

| 指标 | 3B raw | 3B d000 | 3B d100 | 1.5B d000 |
|------|--------|---------|---------|-----------|
| 唯一预测值数 | 419 | **208** | 396 | 395 |
| 最频繁预测出现次数 | 43 | **134** ("20") | 78 | 39 |
| Top 5 覆盖样本数 | 184 | **360** | 199 | 173 |

3B d000 模型预测坍缩到少数几个常见数字（"20" 出现 134 次占 10.2%），丧失了逐题推理的能力。

**3. 解析问题可忽略**
- 0 个 None 预测（parser 总能提取到数字）
- 仅 6 个浮点格式近似不匹配（"16.00" vs "16" 等），对结果影响 <0.5pp

**4. 两个 seed 一致复现**
- d000 s42: 12.0% (158/1319)
- d000 s123: 17.6% (232/1319)

### 根因

LoRA SFT 超参（lr=2e-4, r=16, alpha=32, 全 7 模块）对 3B 模型过于激进，导致 CoT 生成能力灾难性遗忘。1.5B 模型同样参数不受影响，说明 3B 的参数空间对此学习率更敏感。

### 对 contamination 实验的影响

d100 - d000 = +57.7pp **是被严重夸大的 artifact**：
- d000 基线被 SFT 人为压低到 12%（实际应 ~60%）
- d100 训练数据中包含 GSM8K 题目，恢复（甚至提升）了数学能力
- 公平基准应对比 raw 60.5% vs d100 69.7% → **真实 contamination signal ~9pp**

### 修复建议

1. **降低 3B 学习率**：2e-4 → 5e-5 或更低，重训 d000 并重新评估
2. **或者降低 LoRA alpha**：alpha=32 → alpha=16（scaling factor 从 2.0 降到 1.0）
3. **分析中增加 raw baseline 对比**：在所有 3B 结果中都与 raw model 分数做 delta

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "953d31fb-51e9-4586-be30-910a5a6aa141",
  "isSidechain": false,
  "requestId": "req_011Cb2ju5H4QjLvEJfzYTpKe",
  "type": "assistant",
  "uuid": "760bc250-4468-4c7b-a22f-e183cc20f056",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "5bfc64b4-6f42-48ba-aa26-8171bcc7843f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016pRtAjtZiSTwEV1sKMSLoM",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1747,
      "cache_read_input_tokens": 106423,
      "output_tokens": 1491,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1747,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1491,
          "cache_read_input_tokens": 106423,
          "cache_creation_input_tokens": 1747,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1747
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

_source line 282_

```json
{
  "type": "last-prompt",
  "leafUuid": "760bc250-4468-4c7b-a22f-e183cc20f056",
  "sessionId": "5bfc64b4-6f42-48ba-aa26-8171bcc7843f"
}
```

---


### Runtime record

_source line 283_

```json
{
  "type": "ai-title",
  "aiTitle": "Debug 3B d000 GSM8K 12% anomaly",
  "sessionId": "5bfc64b4-6f42-48ba-aa26-8171bcc7843f"
}
```

---
