# research literature scan

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_literature-scan_20260516T012004_result.json`
- **Structured JSON:** [`7d94a93bec89656aa3ec.json`](../../sessions/7d/7d94a93bec89656aa3ec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

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

---
