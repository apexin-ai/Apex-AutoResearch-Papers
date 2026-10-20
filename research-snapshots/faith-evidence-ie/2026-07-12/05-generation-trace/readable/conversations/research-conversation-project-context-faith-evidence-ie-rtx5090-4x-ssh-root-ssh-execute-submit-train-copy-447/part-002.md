# Research conversation: <project_context> # 项目: faith-evidence-ie ## 运行环境 - 服务器名: rtx5090-4x - SSH 账户: root（调用 ssh_execute / submit_training_job — Part 2 of 2

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction (July export snapshot)** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../research-conversation-project-context-faith-evidence-ie-rtx5090-4x-ssh-root-ssh-execute-submit-train-copy-447.md) · [Structured JSON](../../../sessions/cc/cc597810de11c66345cd.json)

## Round 1

### Assistant

_source line 119 · 2026-05-18T22:13:56.013Z_

数据收集完毕。inference.py 默认值：batch_size=**8**, max_new_tokens=1024, seed=42, quantize=**True**。这意味着缺省 batch_size 的实验用的是 8 而非 D076 的 4。

下面是完整审计报告。

---

## 4B Eval D076 协议一致性审计报告

### D076 协议标准
| 参数 | 要求值 | inference.py 默认值 |
|------|--------|-------------------|
| batch_size | 4 | **8** (不匹配!) |
| max_new_tokens | 1024 | 1024 |
| seed | 42 | 42 |
| quantize | --no-quantize | **True** (不匹配!) |
| model_path | base model (Qwen3-4B) | - |
| sft_adapter | adapter 路径 | - |

---

### 一、SFT Eval（4B 各 seed）

| exp_id | ign_f1 | BS | MNT | SEED | NoQuant | model_path | sft_adapter | D076 |
|--------|--------|----|-----|------|---------|------------|-------------|------|
| **reeval_sft_baseline_d076** | **0.3974** | 4 | 1024 | 42 | Yes | models/Qwen3-4B | sft_output | **PASS** |
| **wave1_sft_4b_s43_eval_r2** | **0.4365** | 4 | 1024 | 42 | Yes | models/Qwen3-4B | sft_output_seed43 | **PASS** |
| **wave1_sft_4b_s44_eval_r2** | *pending* | 4 | 1024 | 42 | Yes | models/Qwen3-4B | sft_output_seed44 | **PASS** |
| mvp2_sft_eval_r2 | 0.4057 | 16 | 1024 | 42 | No | sft_output (adapter!) | N/A | FAIL: BS=16, quantize, model_path=adapter |
| mvp2_sft_eval_r3 | 0.4057 | 16 | 1024 | 42 | No | sft_output (adapter!) | N/A | FAIL: 同上 |

**SFT s42 adapter 确认路径：`/root/autodl-tmp/sft_output/`**（不存在 `sft_output_seed42` 目录）

所有 sft_output 目录：
- `/root/autodl-tmp/sft_output/` — s42 (canonical)
- `/root/autodl-tmp/sft_output_seed43/` — s43
- `/root/autodl-tmp/sft_output_seed44/` — s44

---

### 二、RSFT CED k=1 Eval（4B 各 seed）

| exp_id | ign_f1 | BS | MNT | SEED | NoQuant | D076 | 备注 |
|--------|--------|----|-----|------|---------|------|------|
| **reeval_ced_s42** | **0.4423** | 4 | 1024 | 42 | Yes | **PASS** | |
| **rsft_s43_dev_eval_preds** | **0.4512** | 4 | 1024 | 42 | Yes | **PASS** | |
| eval_rsft_ced_s43 | 0.4512 | 4 | 1024 | **43** | Yes | FAIL: seed=43 | 但结果与 seed=42 版完全一致 |
| reeval_ced_s44 | 0.4511 | 4 | 1024 | **44** | Yes | FAIL: seed=44 | **无 D076 版本** |
| rsft_s44_dev_eval_preds | *failed* | 4 | 1024 | 42 | Yes | PASS(但 failed) | 需重跑 |
| eval_rsft_ced_s45 | 0.4416 | 4 | 1024 | **45** | Yes | FAIL: seed=45 | **无 D076 版本** |

**关于 seed 的影响：** CED s43 用 seed=42 和 seed=43 均得到 ign_f1=0.4512（完全一致）。inference 使用 `do_sample=False`（greedy decoding），seed 只影响 `torch.manual_seed`，对 greedy 结果无影响。因此 seed 不同的 eval 结果在实质上是可信的。

---

### 三、RSFT flat-NLI Eval（4B 各 seed）

| exp_id | ign_f1 | BS | MNT | SEED | NoQuant | D076 | 备注 |
|--------|--------|----|-----|------|---------|------|------|
| **reeval_flat_nli_s42** | **0.4448** | 4 | 1024 | 42 | Yes | **PASS** | |
| reeval_flat_nli_s43 | 0.4523 | **16** | ? | ? | ? | FAIL: BS=16 | log 确认 62 batches=BS16 |
| reeval_flat_nli_s43_r2 | 0.4503 | 4 | 1024 | **43** | Yes | FAIL: seed=43 | |
| eval_flat_nli_s44 | 0.4521 | 4 | 1024 | **44** | Yes | FAIL: seed=44 | |
| eval_flat_nli_seed45 | 0.4461 | 4 | 1024 | **45** | Yes | FAIL: seed=45 | |

---

### 四、其他 4B Eval

| exp_id | ign_f1 | BS | MNT | SEED | NoQuant | D076 | 备注 |
|--------|--------|----|-----|------|---------|------|------|
| **eval_plan_014_no_evidence_r2** | **0.4721** | 4 | 1024 | 42 | Yes | **PASS** | no-evidence 消融 |
| **plan_014_no_evidence_eval_d076** | **0.4721** | 4 | 1024 | 42 | Yes | **PASS** | 同上实验重复确认 |
| **random_rsft_k1_eval** | **0.4114** | 4 | 1024 | 42 | Yes | **PASS** | random RSFT baseline |
| **grpo_bf16_g4_ckpt100_eval** | **0.4431** | 4 | 1024 | 42 | Yes | **PASS** | |
| grpo_bf16_g4_ckpt200_eval | *RUNNING* | 4 | 1024 | 42 | Yes | **PASS** | |
| lead2_ckpt20_eval | 0.4533 | 4 | 1024 | 42 | Yes | PASS* | *base_model=merged_sft_rsft，非标准 |
| eval_plan_001_flat_nli | 0.4539 | **16** | 1024 | 42 | Yes | FAIL: BS=16 | |
| plan_011_grpo_g8_bf16_eval | 0.4549 | **16** | 1024 | 42 | Yes | FAIL: BS=16 | |
| mvp2_eval_rsft_s43_r2 | 0.4683 | **8**(default) | 1024 | 42 | Yes | FAIL: BS=8 | 缺省参数 |
| plan_007_redocred_4b_sft_eval_r2 | 0.3659 | 4 | 1024 | 42 | Yes | **PASS** | Re-DocRED |
| plan_007_redocred_rsft_eval_r5 | 0.4145 | 4 | 1024 | 42 | Yes | **PASS** | Re-DocRED RSFT |
| mvp2_eval_ced_kl001_* (9个) | 0.01~0.22 | N/A | N/A | N/A | No | FAIL | batch_eval 模块，完全不同 |

---

### 五、batch_size 对结果的实质影响

关键对照：flat-NLI s42 同一 adapter，不同 batch_size：
- BS=16: `eval_plan_001_flat_nli` → ign_f1 = 0.4539
- BS=4: `reeval_flat_nli_s42` → ign_f1 = 0.4448
- **差异 = -0.91pp**

这说明 batch_size 影响显著（padding 差异影响 attention 数值精度），D076 的 BS=4 标准化是必要的。

---

### 六、需要 D076 重跑的实验清单

**必须重跑（无 D076 合规版本）：**

| 优先级 | 实验 | 当前最佳值 | 问题 |
|--------|------|-----------|------|
| **HIGH** | RSFT CED s44 | 0.4511 (seed=44) | seed 不影响结果，但无 D076 记录 |
| **HIGH** | RSFT CED s45 | 0.4416 (seed=45) | 同上 |

**建议重跑（为完整性，但 seed 不影响 greedy decoding）：**

| 优先级 | 实验 | 当前最佳值 | 问题 |
|--------|------|-----------|------|
| LOW | flat-NLI s43 | 0.4503 (seed=43, BS=4) | 仅 seed 差异，结果可信 |
| LOW | flat-NLI s44 | 0.4521 (seed=44, BS=4) | 同上 |
| LOW | flat-NLI s45 | 0.4461 (seed=45, BS=4) | 同上 |

**不需要重跑（有验证 seed 无影响）：**
- RSFT CED s43: `rsft_s43_dev_eval_preds` (seed=42) 与 `eval_rsft_ced_s43` (seed=43) 结果完全一致 = 0.4512

---

### 七、结论

1. **SFT 三个 seed 全部 D076 合规**：s42=0.3974, s43=0.4365, s44=pending
2. **RSFT CED k=1**：s42 和 s43 有 D076 合规 eval，s44 和 s45 需要重跑（虽然 seed 不影响 greedy 结果）
3. **flat-NLI RSFT**：仅 s42 有 D076 合规 eval，s43/s44/s45 均需重跑（但 seed-only 差异，优先级低）
4. **batch_size 影响显著**（~0.9pp），早期 BS=16 的实验结果不可与 D076 直接比较
5. **D111 提到的三个 SFT s42 值**：0.4057 (mvp2, BS=16+quantize) / 0.3974 (D076) 差异来自 eval 配置不同，非模型差异

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5905d82f-c794-4164-b71d-154d5cc4ece6",
  "isSidechain": false,
  "requestId": "req_011CbAoUP7ATHfaPZ7wNS4o1",
  "type": "assistant",
  "uuid": "e4e857cb-8bee-44a1-bd98-78cfc6815a61",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "596d8411-63f5-4757-a2a4-2c57b1fcaba0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013FpBRDkktCU8nGPLxBYBJ9",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3300,
      "cache_read_input_tokens": 73803,
      "output_tokens": 6810,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3300,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6810,
          "cache_read_input_tokens": 73803,
          "cache_creation_input_tokens": 3300,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3300
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

_source line 120_

```json
{
  "type": "last-prompt",
  "leafUuid": "e4e857cb-8bee-44a1-bd98-78cfc6815a61",
  "sessionId": "596d8411-63f5-4757-a2a4-2c57b1fcaba0"
}
```

---


### Runtime record

_source line 121_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit 4B eval D076 protocol compliance",
  "sessionId": "596d8411-63f5-4757-a2a4-2c57b1fcaba0"
}
```

---
