# research literature scan — Part 2 of 2

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../research-literature-scan.md) · [Structured JSON](../../../sessions/ba/ba999cf84379c47360cd.json)

## Round 1

### Assistant

_source line 198_

文件验证通过：110,672 bytes, 116 篇论文（101 existing + 15 new）。

---

## 增量扫描报告

### 新增 15 篇论文，分布在 6 个新 Category（26-31）

#### Direction 1: DocRE Evidence Grounding（2 篇）
| 论文 | Venue | 与 FREIGE 关系 |
|------|-------|---------------|
| **ESTR-DocRE** — evidence-supervised transformer + multi-hop reasoning | Springer 2025 | `direct_competitor` — 最相关的 supervised evidence-grounded DocRE，但仍是 discriminative 范式 |
| **Dual Reasoning Enhanced DocRE** — 双 GCN+Transformer 推理 | Springer 2026 | `related_method` |

#### Direction 2: Faithfulness Cost / Benchmarking（2 篇）
| 论文 | Venue | 与 FREIGE 关系 |
|------|-------|---------------|
| **FaithCoT-Bench** — instance-level CoT faithfulness benchmark | **ICLR 2026** | `evaluation` — faithfulness 评估方法论 |
| **C2-Faith** — causal + coverage faithfulness | arXiv 2026 | `evaluation` — coverage 维度与 evidence completeness 相关 |

#### Direction 3: QLoRA/Quantization + RL Artifacts（3 篇）
| 论文 | Venue | 与 FREIGE 关系 |
|------|-------|---------------|
| **QuRL** — quantized rollout 中 actor divergence 指数增长 | arXiv 2026 | `related_method` — 直接解释 Claim 2 decoupling 机制 |
| **QaRL** — error tokens from quantized long-form generation | arXiv 2026 | `related_method` — error token 与 evidence hallucination 类似 |
| **PECFT Survey** — PEFT continual fine-tuning 综述 | arXiv 2025 | `background` |

#### Direction 4: RLVR for General Domains / IE（3 篇）
| 论文 | Venue | 与 FREIGE 关系 |
|------|-------|---------------|
| **RLPR** — 无需 verifier 的 RLVR 泛化 | arXiv 2025 | `method_component` — self-probability reward 可替代 CED |
| **RLVRR** — reference-based reward chain | **ICLR 2026** | `method_component` — reward chain 与 CED reranker 理念相关 |
| **RL-Struct** — RL for structured LLM output | arXiv 2025 | `method_component` |

#### Direction 5: Reward Hacking / Decoupling（2 篇）
| 论文 | Venue | 与 FREIGE 关系 |
|------|-------|---------------|
| **EPPO (Energy Loss Phenomenon)** | **ICML 2025** | `related_method` — 与 EDCR 互补的 representation-level diagnostic |
| **Composite Rewards for Reward Hacking Mitigation** | arXiv 2025 | `related_method` — 验证 CED reward 设计合理性 |

#### Bonus: RL vs Forgetting（3 篇，对 Claim 2 至关重要）
| 论文 | Venue | 与 FREIGE 关系 |
|------|-------|---------------|
| **RFT Naturally Mitigates Forgetting** | arXiv 2025 | `related_analysis` |
| **Why RFT Preserves Prior Knowledge** | arXiv 2025 | `related_analysis` |
| **RL's Razor** | arXiv 2025 | `related_analysis` |

这三篇共同论证：**full-precision RL 本身抗 forgetting**，因此 FREIGE 观察到的 evidence-extraction decoupling 更可能是 **QLoRA-specific**——强化了 Claim 2 的定位。

---

### ⚠️ 直接竞争者评估

**无直接竞争者做 exactly the same thing。** 最接近的是：

1. **EvidenceRL**（已在 map 中，Cat 13）— GRPO + evidence faithfulness reward，但在 QA 域而非 DocRE，且未报告 evidence tax
2. **ESTR-DocRE**（新增）— evidence-supervised DocRE，但 discriminative 范式，非 LLM+GRPO
3. **R1-RE**（已在 map 中）— RLVR for RE，但无 evidence grounding

FREIGE 的差异化仍然成立：**LLM generative DocRE + GRPO + evidence tax 量化 + QLoRA decoupling 发现**这个组合没有被覆盖。

### 文献覆盖薄弱方向

1. **"Evidence tax" 的精确量化**：没有其他论文系统测量 evidence generation 对 task performance 的代价。Claim 1 的 ~8pp cost 仍是独特发现。
2. **QLoRA + multi-task RL 的 task decoupling**：QuRL/QaRL 从 quantization-RL stability 角度提供了间接证据，但没有论文直接观察到 QLoRA GRPO 下的 task-specific decoupling。Claim 2 仍无直接竞争。
3. **Inference-time reranking for evidence recovery**：CED reranker 的 inference-time 恢复策略在文献中缺乏对应物。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a6db861b-6df3-4425-8c58-446422460fe8",
  "uuid": "1b1dbac5-c812-4e18-9e91-99f4a35b5eb3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YQ59WZy69zfFUG7AaRLLAY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 260,
      "cache_read_input_tokens": 71557,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 260
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

_source line 199_

文件验证通过：110,672 bytes, 116 篇论文（101 existing + 15 new）。

---

## 增量扫描报告

### 新增 15 篇论文，分布在 6 个新 Category（26-31）

#### Direction 1: DocRE Evidence Grounding（2 篇）
| 论文 | Venue | 与 FREIGE 关系 |
|------|-------|---------------|
| **ESTR-DocRE** — evidence-supervised transformer + multi-hop reasoning | Springer 2025 | `direct_competitor` — 最相关的 supervised evidence-grounded DocRE，但仍是 discriminative 范式 |
| **Dual Reasoning Enhanced DocRE** — 双 GCN+Transformer 推理 | Springer 2026 | `related_method` |

#### Direction 2: Faithfulness Cost / Benchmarking（2 篇）
| 论文 | Venue | 与 FREIGE 关系 |
|------|-------|---------------|
| **FaithCoT-Bench** — instance-level CoT faithfulness benchmark | **ICLR 2026** | `evaluation` — faithfulness 评估方法论 |
| **C2-Faith** — causal + coverage faithfulness | arXiv 2026 | `evaluation` — coverage 维度与 evidence completeness 相关 |

#### Direction 3: QLoRA/Quantization + RL Artifacts（3 篇）
| 论文 | Venue | 与 FREIGE 关系 |
|------|-------|---------------|
| **QuRL** — quantized rollout 中 actor divergence 指数增长 | arXiv 2026 | `related_method` — 直接解释 Claim 2 decoupling 机制 |
| **QaRL** — error tokens from quantized long-form generation | arXiv 2026 | `related_method` — error token 与 evidence hallucination 类似 |
| **PECFT Survey** — PEFT continual fine-tuning 综述 | arXiv 2025 | `background` |

#### Direction 4: RLVR for General Domains / IE（3 篇）
| 论文 | Venue | 与 FREIGE 关系 |
|------|-------|---------------|
| **RLPR** — 无需 verifier 的 RLVR 泛化 | arXiv 2025 | `method_component` — self-probability reward 可替代 CED |
| **RLVRR** — reference-based reward chain | **ICLR 2026** | `method_component` — reward chain 与 CED reranker 理念相关 |
| **RL-Struct** — RL for structured LLM output | arXiv 2025 | `method_component` |

#### Direction 5: Reward Hacking / Decoupling（2 篇）
| 论文 | Venue | 与 FREIGE 关系 |
|------|-------|---------------|
| **EPPO (Energy Loss Phenomenon)** | **ICML 2025** | `related_method` — 与 EDCR 互补的 representation-level diagnostic |
| **Composite Rewards for Reward Hacking Mitigation** | arXiv 2025 | `related_method` — 验证 CED reward 设计合理性 |

#### Bonus: RL vs Forgetting（3 篇，对 Claim 2 至关重要）
| 论文 | Venue | 与 FREIGE 关系 |
|------|-------|---------------|
| **RFT Naturally Mitigates Forgetting** | arXiv 2025 | `related_analysis` |
| **Why RFT Preserves Prior Knowledge** | arXiv 2025 | `related_analysis` |
| **RL's Razor** | arXiv 2025 | `related_analysis` |

这三篇共同论证：**full-precision RL 本身抗 forgetting**，因此 FREIGE 观察到的 evidence-extraction decoupling 更可能是 **QLoRA-specific**——强化了 Claim 2 的定位。

---

### ⚠️ 直接竞争者评估

**无直接竞争者做 exactly the same thing。** 最接近的是：

1. **EvidenceRL**（已在 map 中，Cat 13）— GRPO + evidence faithfulness reward，但在 QA 域而非 DocRE，且未报告 evidence tax
2. **ESTR-DocRE**（新增）— evidence-supervised DocRE，但 discriminative 范式，非 LLM+GRPO
3. **R1-RE**（已在 map 中）— RLVR for RE，但无 evidence grounding

FREIGE 的差异化仍然成立：**LLM generative DocRE + GRPO + evidence tax 量化 + QLoRA decoupling 发现**这个组合没有被覆盖。

### 文献覆盖薄弱方向

1. **"Evidence tax" 的精确量化**：没有其他论文系统测量 evidence generation 对 task performance 的代价。Claim 1 的 ~8pp cost 仍是独特发现。
2. **QLoRA + multi-task RL 的 task decoupling**：QuRL/QaRL 从 quantization-RL stability 角度提供了间接证据，但没有论文直接观察到 QLoRA GRPO 下的 task-specific decoupling。Claim 2 仍无直接竞争。
3. **Inference-time reranking for evidence recovery**：CED reranker 的 inference-time 恢复策略在文献中缺乏对应物。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 1234975,
  "duration_api_ms": 1360766,
  "num_turns": 53,
  "stop_reason": "end_turn",
  "session_id": "a6db861b-6df3-4425-8c58-446422460fe8",
  "total_cost_usd": 4.794749250000001,
  "usage": {
    "input_tokens": 3972,
    "cache_creation_input_tokens": 59976,
    "cache_read_input_tokens": 1639486,
    "output_tokens": 16211,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 59976,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 1533,
        "cache_read_input_tokens": 71557,
        "cache_creation_input_tokens": 260,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 260
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 437418,
      "outputTokens": 12388,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 24,
      "costUSD": 0.739358,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 3990,
      "outputTokens": 57870,
      "cacheReadInputTokens": 2301295,
      "cacheCreationInputTokens": 230087,
      "webSearchRequests": 0,
      "costUSD": 4.05539125,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "590a363c-e8a8-44eb-80c5-5ed3f5a9bb62"
}
```

</details>

---
