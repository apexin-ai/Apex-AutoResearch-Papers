# research circuit discovery survey — Part 2 of 2

**Transformer Model EAP-IG** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../research-circuit-discovery-survey.md) · [Structured JSON](../../../sessions/a3/a392b4a33b8633107758.json)

## Round 4

### Tool result

_source line 463 · 2026-05-12T22:16:12.479Z_

<details><summary>↩ Tool result · `toolu_01JYAVxaD8PChTg5KgKGo2bJ`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/related_work_notes.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "68a7c083-4416-45d6-84f9-815f45fc4451",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/related_work_notes.md",
    "content": "# Circuit Discovery Related Work Notes (2024-2026)\n\n> 调研日期：2026-05-12 | 项目：structfuse-context\n> 核心问题：CSS（Cross-method Stability Scoring）的 novelty 是否站得住？\n\n---\n\n## 1. 方法一致性比较（Novelty 关键）\n\n**结论：没有论文以\"跨方法一致性分析\"为核心贡献。** 多篇论文在评估新方法时附带比较了不同方法的表现，但比较维度是各方法 vs ground-truth 的 faithfulness/AUC，而非方法之间的 pairwise agreement。\n\n### 直接比较多方法的论文\n\n| 论文 | 方法比较 | 比较维度 | 是否测量方法间一致性 |\n|------|----------|----------|---------------------|\n| Conmy et al. \"Towards Automated Circuit Discovery\" (NeurIPS 2023) | ACDC vs SP vs HISP | ROC AUC vs ground-truth | ❌ 不测方法间 overlap |\n| Syed et al. \"Attribution Patching Outperforms Automated Circuit Discovery\" (BlackboxNLP 2024) | EAP vs ACDC vs SP vs HISP | AUC vs ground-truth | ❌ |\n| Bhaskar et al. \"Finding Transformer Circuits with Edge Pruning\" (NeurIPS 2024 Spotlight) | Edge Pruning vs ACDC vs EAP | Faithfulness at various sparsities | ❌ 但隐含表明方法差异大：EP 找到的边不到 ACDC/EAP 的一半 |\n| Hsu et al. \"CD-T\" (ICLR 2025) | CD-T vs ACDC vs EAP | ROC AUC vs ground-truth | ❌ |\n| Edin et al. \"GIM\" (2025, arXiv) | GIM vs EActP vs EAP vs EAP-IG vs NAP vs IFR vs UGS | Faithfulness metrics | ❌ |\n| InterpBench (NeurIPS 2024 D&B) | ACDC vs EAP vs SP on 86 semi-synthetic models | Ground-truth recovery | ❌ 但发现 ACDC 与 EAP-IG 统计上不可区分 |\n\n### 最接近\"一致性分析\"的论文\n\n**Hanna et al. \"Have Faith in Faithfulness: Going Beyond Circuit Overlap\" (2024, arXiv 2403.17806)**\n- 比较 EAP vs EAP-IG 的 **node overlap**，发现两者 overlap 很高但 faithfulness 差异大\n- 核心结论：overlap ≠ faithfulness，高 overlap 不代表电路功能等价\n- **与 CSS 的关系**：这是对 overlap-based 评估的警告，但不是跨方法一致性的系统研究\n\n**Méloux et al. \"Mechanistic Interpretability as Statistical Estimation: A Variance Analysis\" (2025, arXiv 2510.00845)**\n- 对 EAP-IG 做 bootstrap resampling，发现 **单方法内** Jaccard 仅 0.561\n- 超参数变化导致 Jaccard 从 0.086 到 1.0 不等\n- **与 CSS 的关系**：揭示了电路不稳定性问题（motivates CSS），但仅限单方法内变异，未跨方法\n\n**总结：无人系统测量不同方法间的 pairwise Jaccard / agreement matrix。这正是 CSS 要填补的空白。**\n\n---\n\n## 2. Circuit Aggregation / Ensemble（Novelty 威胁）\n\n### 🔴 最高威胁：CIRCUS\n\n**CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles**\n- 作者：Swapnil Parekh\n- 时间：2026年3月, arXiv 2603.00523\n- 方法：对单一归因方法，在多组剪枝阈值配置下运行，计算每条边的 inclusion frequency → stability score s(e) ∈ [0,1]，提取 consensus circuit（所有配置下都存在的边），分为 core/contingent/noise\n- **与 CSS 的区别**：CIRCUS 变化的是**单方法内的超参数**（剪枝阈值），不是跨不同算法族。它不运行 ACDC + EAP + SP 然后求交集\n- **与 CSS 的相似度**：数学框架高度相似（per-edge stability scoring, consensus extraction, core/contingent taxonomy）\n- **威胁评级**：🔴 HIGH — 概念上最接近，但维度不同（intra-method vs cross-method）\n\n### 🟡 中等威胁：Mondorf et al. Ensemble\n\n**Mondorf et al. \"Exploring Ensemble Strategies for Circuit Localization Methods\" (BlackboxNLP 2025, arXiv 2510.06811)**\n- 方法：组合 EAP, EAP-IG-inputs, EAP-IG-activations, Edge Pruning 的输出\n  - Max = union（任一方法选中）\n  - Min = intersection（所有方法选中）\n  - Mean = 连续分数平均\n  - Hybrid = 并行+串行组合\n- 结果：Mean > union/intersection，Hybrid 最佳 (CMD 0.03, CPR 1.83)\n- **与 CSS 的区别**：聚合的是**连续归因分数**（mean/min/max），不是二值 edge-in/edge-out；方法主要是 EAP 变体，不是真正不同的算法族；workshop 短文非完整方法贡献\n- **与 CSS 的相似度**：确实跨方法组合（attribution + pruning），实现了 union/intersection 操作\n- **威胁评级**：🟡 MODERATE — 最接近跨方法聚合，但 framing 为 shared task 工程方案非方法论贡献\n\n### 🟢 低威胁\n\n| 论文 | 方法 | 与 CSS 区别 | 威胁 |\n|------|------|------------|------|\n| Nikankin et al. \"Improving Circuit Faithfulness via Better Edge Selection\" (BlackboxNLP 2025) | Bootstrap EAP-IG scores across data resamples | 单方法 + 数据重采样，非跨方法 | 🟢 LOW |\n| Anani et al. \"Certified Circuits: Stability Guarantees\" (2026, arXiv 2602.22968) | 随机化数据子采样 + 删除平滑认证 | 单方法 wrapper，不聚合多方法 | 🟢 LOW |\n| Miller et al. \"Transformer Circuit Faithfulness Metrics are not Robust\" (CoLM 2024) | 分析 faithfulness 指标敏感性 | 纯诊断，不提出聚合 | 🟢 LOW |\n\n**总结：没有论文提出 CSS 的精确方案——运行 N 种根本不同的算法族（ACDC, EAP, SP, EP），对每种输出做二值化，然后计算跨方法 binary consensus。CIRCUS 最接近但维度不同（intra-method threshold variation vs cross-method）。Mondorf et al. 确实跨方法但用连续分数聚合且为 workshop 工程方案。**\n\n---\n\n## 3. 2024-2026 新方法\n\n| 方法 | 论文 | 年份 | 会议 | 算法族 | 备注 |\n|------|------|------|------|--------|------|\n| CD-T | Hsu et al. \"Efficient Automated Circuit Discovery using Contextual Decomposition\" | 2024 | ICLR 2025 | 分解 (decomposition) | 无需 activation patching，秒级发现，97% AUC |\n| DiscoGP | Yu et al. \"Functional Faithfulness in the Wild\" | 2024 | ICML 2024 | 可微剪枝 | 联合权重+边剪枝，端到端学习二值 mask |\n| Transcoders | Dunefsky et al. \"Transcoders Find Interpretable LLM Feature Circuits\" | 2024 | NeurIPS 2024 | 稀疏替换模型 | 用稀疏 MLP 替换原 MLP，实现 weights-based 电路分析 |\n| Sparse Feature Circuits | Marks et al. \"Discovering and Editing Interpretable Causal Graphs\" | 2024 | ICLR 2025 (Oral) | 归因 + SAE 特征 | 在 SAE 特征级别发现电路，支持 SHIFT 编辑 |\n| Circuit Tracing | Ameisen, Olah et al. (Anthropic) \"Attribution Graphs\" | 2025 | Tech Report | 稀疏替换 + 归因 | Cross-layer transcoders → per-prompt DAG，应用于 Claude 3.5 |\n| GIM | Edin et al. \"Improved Interpretability for LLMs\" | 2025 | arXiv | 梯度修正 | 修正 softmax/LayerNorm 反传，MIB 排行榜第一 |\n| HAP | Gu et al. \"Hybrid Attribution and Pruning Framework\" | 2025 | arXiv | 混合 (EAP → EP) | 先 EAP 粗筛再 EP 精修，比 EP 快 46% |\n| ModCirc | He et al. \"Modular Circuits of LLMs\" | 2025 | ICML 2025 | 模块化分解 | 发现跨任务共享的模块化电路词表 |\n| Stream | Rosser et al. \"Scaling up MI to Long Context\" | 2025 | arXiv | 层次化剪枝 | O(T log T) 稀疏注意力 mask，支持 100K+ token |\n| Weight-Sparse Circuits | Gao et al. (OpenAI) | 2025 | arXiv | 稀疏训练 | 极端权重稀疏 (~1/1000) → 天然可解释电路 |\n| Formal MI | Hadad et al. \"Automated Circuit Discovery with Provable Guarantees\" | 2026 | ICLR 2026 | 验证 (verification) | 首个可证明保证的电路发现（鲁棒性 + 最小性） |\n| SVD Directional Masking | Ahmad et al. \"Beyond Components\" | 2025 | arXiv | SVD + 可微 mask | 揭示单头内叠加子功能 |\n\n---\n\n## 4. 顶会论文列表\n\n### ICLR 2024\n| 论文 | 主要贡献 |\n|------|----------|\n| Sparse Autoencoders Find Highly Interpretable Features in LMs | SAE 发现单语义特征，解决 superposition |\n| Towards Best Practices of Activation Patching in LMs | 系统分析 patching 方法选择对电路发现的影响 |\n| Circuit Component Reuse Across Tasks | IOI 电路 ~78% 被 Colored Objects 复用 |\n| Successor Heads: Recurring Interpretable Attention Heads | 发现跨架构的 successor heads（递增操作） |\n\n### ICLR 2025\n| 论文 | 主要贡献 |\n|------|----------|\n| Sparse Feature Circuits (Oral) | SAE 特征级电路发现 + SHIFT 编辑 |\n| Scaling and Evaluating Sparse Autoencoders (Oral) | k-sparse SAE 扩展到 GPT-4，16M latents |\n| CD-T: Contextual Decomposition for Circuit Discovery | 秒级电路发现，97% AUC |\n| Computational Complexity of Circuit Discovery (Spotlight) | 证明多数电路发现查询 NP-hard |\n| Everything Everywhere All at Once: Is MI Identifiable? | 电路非唯一性：多电路可复现同一行为 |\n| SAEs Do Not Find Canonical Units of Analysis | SAE stitching 证明特征非原子/非完备 |\n| Unifying and Verifying Mechanistic Interpretations | 统一群运算网络的机制解释并形式化证明 |\n\n### NeurIPS 2024\n| 论文 | 主要贡献 |\n|------|----------|\n| Finding Transformer Circuits with Edge Pruning (Spotlight) | EP 方法，更忠实且更稀疏，扩展到 13B |\n| Transcoders Find Interpretable LLM Feature Circuits | 稀疏 MLP 替换实现 weights-based 电路分析 |\n| LLM Circuit Analyses Are Consistent Across Training and Scale | 电路在训练过程和模型规模间一致出现 |\n| Compact Proofs of Model Performance via MI | MI → 可证明的准确率下界 |\n| Hypothesis Testing the Circuit Hypothesis | 形式化电路假设的假设检验 |\n| InterpBench: Semi-Synthetic Transformers for Evaluating MI | 86 个有 ground-truth 的半合成模型评估基准 |\n\n### ICML 2025\n| 论文 | 主要贡献 |\n|------|----------|\n| MIB: A Mechanistic Interpretability Benchmark | 标准化电路定位基准，归因+mask 优化方法领先 |\n| ModCirc: Modular Circuits of LLMs | 跨任务模块化电路词表 |\n| Towards Understanding Fine-Tuning via Circuit Analysis | 追踪微调中电路变化，提出 circuit-aware LoRA |\n\n---\n\n## 5. Novelty 评估\n\n### CSS 的 novelty 站得住吗？**站得住，但需要精确定位差异化。**\n\n#### ✅ Novelty 成立的理由\n\n1. **无人做跨算法族的 binary consensus**：所有现有工作要么是单方法内变异分析（CIRCUS, Méloux），要么是连续分数聚合（Mondorf），要么只是各方法 vs ground-truth 的性能比较。CSS 提出跨 N 种根本不同的算法族做二值共识，这个精确配方是新的。\n\n2. **方法间差异的系统分析是空白**：没有论文报告过不同方法的 pairwise Jaccard matrix / agreement heatmap。大量论文隐含表明方法差异很大（EP 边数不到 ACDC 一半），但无人将此作为研究问题。\n\n3. **core/contingent 分类的跨方法版本未被探索**：CIRCUS 做了类似的 core/contingent/noise taxonomy，但基于 intra-method threshold variation。CSS 基于 cross-method agreement 做分类，维度不同且信息更丰富。\n\n#### ⚠️ 需要小心的 Novelty 威胁\n\n1. **CIRCUS (2603.00523)** 是最大威胁。虽然维度不同，但 reviewer 可能认为 conceptual overlap 太大。**建议**：论文中必须明确讨论 CIRCUS，强调区别（intra-method hyperparameter variation vs cross-method algorithmic diversity），并论证为何跨方法维度更有意义（不同方法有不同 inductive bias，而阈值变化只探索同一方法的 Rashomon set）。\n\n2. **Mondorf et al.** 已经实现了 union/intersection 操作并发现 mean 优于两者。CSS 需要论证 binary consensus 相比连续分数平均的优势（如可解释性、对阈值选择的鲁棒性）。\n\n3. **Méloux et al. 的 intra-method instability 问题**：如果单方法内 Jaccard 仅 0.56，跨方法 consensus 可能更低。需要实验证明 CSS-core 的 faithfulness 确实优于单方法，否则 consensus 可能只是噪声的交集。\n\n4. **非唯一性问题 (ICLR 2025 \"Everything Everywhere All at Once\")**：如果电路本身就非唯一，跨方法共识的理论基础需要更强的论证。\n\n#### 🎯 差异化建议\n\n- **vs CIRCUS**：CSS 跨算法族（不同 inductive bias），CIRCUS 跨阈值（同一方法的 Rashomon set）。论证：不同方法捕获不同类型的因果关系，其交集比单方法阈值交集更有意义。\n- **vs Mondorf et al.**：CSS 是二值共识（edge in/out），Mondorf 是连续分数平均。论证：二值化消除了方法间分数不可比的问题，且产出可直接解释的 agreement matrix。\n- **vs MIB benchmark**：MIB 评估单方法表现，CSS 分析方法间关系。互补而非竞争。\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---


### Tool call

_source line 464_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01FtFvCveFXyQbhuip2Jecyz`</summary>

```json
{
  "name": "related_work_notes",
  "type": "report",
  "description": "Circuit Discovery 文献调研报告（2024-2026），聚焦 CSS novelty 验证，覆盖方法一致性比较、聚合/ensemble、新方法、顶会论文",
  "project": "structfuse-context",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/related_work_notes.md",
  "tags": [
    "literature-survey",
    "novelty",
    "circuit-discovery",
    "CSS"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "0c77fd36-0f56-493f-945f-0788d90c7796",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015HY4wRnZEfgz4E2qjwx8Df",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4898,
      "cache_read_input_tokens": 37616,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4898
      },
      "output_tokens": 50,
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

_source line 465 · 2026-05-12T22:16:18.677Z_

<details><summary>↩ Tool result · `toolu_01FtFvCveFXyQbhuip2Jecyz`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260512_1c4c99\", \"name\": \"related_work_notes\", \"type\": \"report\", \"description\": \"Circuit Discovery 文献调研报告（2024-2026），聚焦 CSS novelty 验证，覆盖方法一致性比较、聚合/ensemble、新方法、顶会论文\", \"path\": \"projects/structfuse-context/artifacts/_project/report/related_work_notes.md\", \"url\": null, \"project\": \"structfuse-context\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-12T22:16:18.634607+00:00\", \"tags\": [\"literature-survey\", \"novelty\", \"circuit-discovery\", \"CSS\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "11ca896b-67a9-48a9-9766-63c1b33ca50c",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260512_1c4c99\\\", \\\"name\\\": \\\"related_work_notes\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"Circuit Discovery 文献调研报告（2024-2026），聚焦 CSS novelty 验证，覆盖方法一致性比较、聚合/ensemble、新方法、顶会论文\\\", \\\"path\\\": \\\"projects/structfuse-context/artifacts/_project/report/related_work_notes.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"structfuse-context\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-12T22:16:18.634607+00:00\\\", \\\"tags\\\": [\\\"literature-survey\\\", \\\"novelty\\\", \\\"circuit-discovery\\\", \\\"CSS\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260512_1c4c99\", \"name\": \"related_work_notes\", \"type\": \"report\", \"description\": \"Circuit Discovery 文献调研报告（2024-2026），聚焦 CSS novelty 验证，覆盖方法一致性比较、聚合/ensemble、新方法、顶会论文\", \"path\": \"projects/structfuse-context/artifacts/_project/report/related_work_notes.md\", \"url\": null, \"project\": \"structfuse-context\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-12T22:16:18.634607+00:00\", \"tags\": [\"literature-survey\", \"novelty\", \"circuit-discovery\", \"CSS\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 466_

报告已写入 `artifacts/related_work_notes.md` 并注册。

---

## 核心结论

**Q1 方法一致性比较**：**无人将此作为核心贡献。** 多篇论文附带比较了不同方法的 faithfulness（vs ground-truth），但没有论文系统测量方法之间的 pairwise agreement / Jaccard matrix。Méloux et al. 做了单方法内的 variance analysis（Jaccard 仅 0.56），Hanna et al. 发现 overlap 高但 faithfulness 差异大——都是局部证据，不是系统的跨方法一致性研究。

**Q2 Circuit Aggregation**：**无直接竞品，但有两个需要讨论的工作：**
- **CIRCUS (2026.03, arXiv 2603.00523)** 🔴 最大威胁——per-edge stability scoring + consensus extraction，数学框架与 CSS 高度相似。但它变化的是**单方法内的剪枝阈值**，不是跨算法族。必须在论文中明确区分。
- **Mondorf et al. (BlackboxNLP 2025)** 🟡 中等威胁——确实组合了 EAP + EP 的输出（含 union/intersection），但用连续分数平均，且为 workshop 短文。

**Novelty 评估：CSS 的 novelty 站得住。** 跨 N 种根本不同算法族的二值共识、方法间 agreement matrix 分析、基于跨方法共识的 core/contingent 分类——这个精确配方没有被做过。关键是论文中必须：
1. 正面讨论 CIRCUS，论证 cross-method vs intra-method variation 的本质区别
2. 论证二值共识相比连续分数平均（Mondorf）的优势
3. 实验证明 CSS-core 的 faithfulness 确实优于单方法结果

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "uuid": "5190dbc8-d3cf-4131-89af-39199b89c1c4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W5Ke9J1RbDag7R8VLXjptr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 667,
      "cache_read_input_tokens": 42514,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 667
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

_source line 467_

报告已写入 `artifacts/related_work_notes.md` 并注册。

---

## 核心结论

**Q1 方法一致性比较**：**无人将此作为核心贡献。** 多篇论文附带比较了不同方法的 faithfulness（vs ground-truth），但没有论文系统测量方法之间的 pairwise agreement / Jaccard matrix。Méloux et al. 做了单方法内的 variance analysis（Jaccard 仅 0.56），Hanna et al. 发现 overlap 高但 faithfulness 差异大——都是局部证据，不是系统的跨方法一致性研究。

**Q2 Circuit Aggregation**：**无直接竞品，但有两个需要讨论的工作：**
- **CIRCUS (2026.03, arXiv 2603.00523)** 🔴 最大威胁——per-edge stability scoring + consensus extraction，数学框架与 CSS 高度相似。但它变化的是**单方法内的剪枝阈值**，不是跨算法族。必须在论文中明确区分。
- **Mondorf et al. (BlackboxNLP 2025)** 🟡 中等威胁——确实组合了 EAP + EP 的输出（含 union/intersection），但用连续分数平均，且为 workshop 短文。

**Novelty 评估：CSS 的 novelty 站得住。** 跨 N 种根本不同算法族的二值共识、方法间 agreement matrix 分析、基于跨方法共识的 core/contingent 分类——这个精确配方没有被做过。关键是论文中必须：
1. 正面讨论 CIRCUS，论证 cross-method vs intra-method variation 的本质区别
2. 论证二值共识相比连续分数平均（Mondorf）的优势
3. 实验证明 CSS-core 的 faithfulness 确实优于单方法结果

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 539439,
  "duration_api_ms": 1577513,
  "num_turns": 9,
  "stop_reason": "end_turn",
  "session_id": "a4897adb-444f-47e1-81f6-81048ce3e3e1",
  "total_cost_usd": 5.938801250000001,
  "usage": {
    "input_tokens": 4801,
    "cache_creation_input_tokens": 31340,
    "cache_read_input_tokens": 172479,
    "output_tokens": 7446,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 31340,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 557,
        "cache_read_input_tokens": 42514,
        "cache_creation_input_tokens": 667,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 667
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1720695,
      "outputTokens": 55555,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 87,
      "costUSD": 2.86847,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 11915,
      "outputTokens": 30473,
      "cacheReadInputTokens": 2308850,
      "cacheCreationInputTokens": 175121,
      "webSearchRequests": 0,
      "costUSD": 3.0703312499999997,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "09bd1323-5a7d-45fb-b8a7-27a9dda32c50"
}
```

</details>

---
