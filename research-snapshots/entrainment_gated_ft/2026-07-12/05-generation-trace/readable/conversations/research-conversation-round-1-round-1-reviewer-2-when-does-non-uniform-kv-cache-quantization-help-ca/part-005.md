# Research conversation: [Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 2 **论文**: "When Does Non-Uniform KV Cache Quantization Help? Cardinality Cons — Part 5 of 5

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

[← Part 4](part-004.md) · [Transcript overview](../research-conversation-round-1-round-1-reviewer-2-when-does-non-uniform-kv-cache-quantization-help-ca.md) · [Structured JSON](../../../sessions/0e/0ea7c59a79c99a054386.json)

## Round 1

### Tool call

_source line 107 · 2026-05-15T04:24:59.386Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director · `toolu_01UF4dewQSyBoWD7FimYTYYh`</summary>

```json
{
  "text": "## Reviewer 2 — Round 1 完整审稿报告\n\n**论文**: \"When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic\"\n**Target Venue**: EMNLP 2026 Main Conference (ARR May 2026)\n\n---\n\n### 总体评分\n\n- **Overall**: 2/5 (Resubmit next cycle)\n- **Soundness**: 3/5 (Acceptable — 技术分析正确但 diagnostic framework 统计基础不足)\n- **Excitement**: 2/5 (Potentially Interesting — 4/5 模型无收益，practical impact 有限)\n- **Reproducibility**: 4/5\n- **Confidence**: 4/5\n\n**一句话总结**: 2-bit compounding 分析有价值，但 cardinality constraint 是标准技术的直接应用，diagnostic framework 仅基于 5 个模型（1 个正例），4/5 模型无收益严重削弱 practical value。\n\n---\n\n### Must-Fix 问题\n\n**N1** [critical] Diagnostic Framework 泛化性严重不足——5 个模型不构成 \"framework\"\n- Section 5.2, Table 4: 阈值 concentration ≳0.50 和 t₁/t₅ ≲0.70 来自 exactly 5 个数据点。\"Spread\" 类别仅 1 个正样本（Qwen）。论文自承 \"Both thresholds are illustrative\"（S5.2 L79），但标题/abstract 的 framing 未反映此 caveat。\n- 建议：扩展到 10-15 个模型，或将 claim 降级为 \"empirical observation\"。\n\n**N2** [critical] 4/5 模型无收益——方法 practical value 存疑\n- Table 2: Qwen 27.3% improvement，但 Llama Δ<0.02，Mistral/Gemma 比 uniform 更差，Yi 完全一致。Qwen 的 uniform 4-bit degradation 异常高（+57.5%），其他模型仅 +2.9%~4.7%——Qwen 可能是架构 outlier 而非方法普遍有效的证据。\n- 建议：分析 Qwen 为何异常，测试更多模型寻找 \"Spread\" 架构。\n\n**N3** [critical] Novelty 不足——cardinality constraint 是标准组合优化技术\n- Eq.(2) 是标准 knapsack cardinality constraint。Sensitivity-based mixed-precision 在 weight quant 领域已有 HAWQ/HAQ 等先驱。Genuine insight 在 compounding 诊断，但解决方案本身缺乏 algorithmic novelty。\n- 建议：formalize compounding 为 super-additive distortion model，或提出 interaction-aware objective。\n\n### Should-Fix 问题\n\n**W1** Related Work 遗漏严重：缺 HAWQ/HAWQ-V2/HAQ（mixed-precision bit allocation 先驱）；缺 PM-KVQ、Kitty、RotateKV、MiniKV（IJCAI/ACL/ICML 2025）、AQUA-KV（ICML 2025）等 2025 published KV cache 工作。\n\n**W2** 与 RateQuant 差异化不清晰：formulation 完全相同，主要区别是 bitwidth set 和 constraint。RateQuant 在 {2,4,8,16} 上是否也 fail？\n\n**W3** 标题/abstract framing 偏乐观：abstract 前半段突出 Qwen 的 27.3%，但实际 4/5 模型无收益。\n\n**W4** Solver equivalence 是 3 模型的 empirical observation，非 proven theorem——应提供 formal sufficient condition 或明确标注为 empirical。\n\n**W5** 缺少 per-head vs token-level granularity 的 tradeoff 讨论。\n\n### 小问题\n- Table 2 缺 Llama/Mistral/Yi/Gemma 的 unconstrained 结果\n- Standard vs hires profiling 数字混用可能造成混淆\n- Runtime benchmark（Appendix D）为模拟而非 real-kernel\n- GEAR/SKVQ 的 bib entry 应更新 venue\n\n### 主要优势\n- Compounding 分析深入（Section 3.3, Figure 2）\n- 实验诚实——negative results 完整报告\n- 写作清晰，逻辑链连贯\n- Multi-seed/cross-dataset stability 分析增强可信度\n- 匿名和格式合规\n\n### Missing References（web search 验证）\nHAWQ (ICCV'19), HAWQ-V2 (NeurIPS'20), HAQ (CVPR'19), PM-KVQ (arXiv'25), Kitty (arXiv'25), RotateKV (IJCAI'25), MiniKV (ACL Findings'25), AQUA-KV (ICML'25), \"Don't Waste Bits!\" (arXiv'26)\n\n### 引用验证\n22 bib entries 均真实存在，0 orphan / 0 missing。3 条 first-author mismatch 疑为 API 数据问题。",
  "reviewer_id": "2",
  "project": "ratekv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a77ceaa2-04e6-4666-aa8d-04e4f09934fe",
  "isSidechain": false,
  "requestId": "req_011Cb3iRFZ3mhEYWjHhZAGK4",
  "type": "assistant",
  "uuid": "53c51500-8745-4a24-a7f6-6c44c3f785dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_2_ee7a8b68",
  "sessionId": "9fbeb321-60cf-446a-bed1-530795e3f023",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PoV2nCTmZ57YjuNEwCHysQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 988,
      "cache_read_input_tokens": 74096,
      "output_tokens": 8890,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 988,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8890,
          "cache_read_input_tokens": 74096,
          "cache_creation_input_tokens": 988,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 988
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

_source line 108_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 2  **论文**: \"When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic\" **路径**: `projects/ratekv/docs/paper/mai…",
  "leafUuid": "53c51500-8745-4a24-a7f6-6c44c3f785dd",
  "sessionId": "9fbeb321-60cf-446a-bed1-530795e3f023"
}
```

---


### Runtime record

_source line 109_

```json
{
  "type": "ai-title",
  "aiTitle": "Review KV cache quantization paper for EMNLP",
  "sessionId": "9fbeb321-60cf-446a-bed1-530795e3f023"
}
```

---


### Tool result

_source line 110 · 2026-05-15T04:25:02.919Z_

<details><summary>↩ Tool result · `toolu_01UF4dewQSyBoWD7FimYTYYh`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "53c51500-8745-4a24-a7f6-6c44c3f785dd",
  "isSidechain": false,
  "promptId": "caa04877-ca66-4148-86c4-31f55af9d94e",
  "type": "user",
  "uuid": "cc5b6661-27b0-4ef4-8f59-b2f98646db78",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"review_director_key\\\": \\\"feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_ec66209ede0ea4e3bda924778c210d8e:director\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "53c51500-8745-4a24-a7f6-6c44c3f785dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_2_ee7a8b68",
  "sessionId": "9fbeb321-60cf-446a-bed1-530795e3f023",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Runtime record

_source line 111 · 2026-05-15T04:25:02.926Z_

```json
{
  "parentUuid": "cc5b6661-27b0-4ef4-8f59-b2f98646db78",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "f155ef15-f5e0-4e22-9b30-4585be582088",
  "timestamp": "2026-05-15T04:25:02.926Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_2_ee7a8b68",
  "sessionId": "9fbeb321-60cf-446a-bed1-530795e3f023",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---


### Runtime record

_source line 112_

```json
{
  "type": "ai-title",
  "aiTitle": "Review KV cache quantization paper for EMNLP",
  "sessionId": "9fbeb321-60cf-446a-bed1-530795e3f023"
}
```

---


### Runtime record

_source line 113 · 2026-05-15T04:26:13.144Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T04:26:13.144Z",
  "sessionId": "9fbeb321-60cf-446a-bed1-530795e3f023",
  "content": "[Round 1 审稿请求]:\n## Step 2 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿意见。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n### Reviewer 1 完整审稿报告\n\n**Overall**: 2.5/5 (Borderline)\n**Soundness**: 3/5 | **Excitement**: 3/5 | **Reproducibility**: 3.5/5 | **Confidence**: 4/5\n\n**一句话总结**: 核心发现有实践价值、negative results 诚实报告值得肯定，但评估存在系统性缺口——缺失 4/5 模型 unconstrained baselines、仅 Qwen 有 downstream evaluation、profiling 方法与 compounding 论点逻辑张力未解决、diagnostic 在 5 个同质模型上 overfit。建议补充 N2 和 N4 后作为 Findings paper 考虑。\n\n#### Must-Fix 问题\n\n**N1** [critical] Diagnostic framework 在 5 个数据点上完美拟合——overfitting 风险\n- Section 5.2, Table 6: 用 2 个 threshold（concentration ≳0.50, t1/t5 ≲0.70）在 5 个 architecture 上实现 100% 准确分类。用 2 个自由参数完美拟合 5 个样本是经典 overfitting 信号。\n- 建议：增加 2–3 个模型验证 threshold 鲁棒性，或降低 claim 力度为 exploratory finding。\n\n**N2** [critical] 4/5 模型缺失 unconstrained baseline\n- Table 2: Llama/Mistral/Yi-1.5/Gemma-2 的 unconstrained greedy 和 MCKP 列为 \"---\"，论文解释 \"those experiments were conducted only on Qwen\"。compounding 是核心发现，如果只在 1 个模型上验证，无法判断是 Qwen idiosyncratic 还是 general phenomenon。\n- 建议：在所有 5 个模型上补跑 unconstrained greedy/MCKP。\n\n**N3** [critical] Profiling methodology 与 compounding 论点的逻辑矛盾\n- Section 3.2 vs Section 3.3: Profiling 用 single-head isolation（keep others bf16），但论文论证 distortions 是 non-additive。如果 per-head distortions 是 non-additive 的，single-head profiling 的 d_h(b) 不能准确反映 multi-head actual distortion。\n- 建议：增加实验验证 single-head d_h(2) 与 multi-head actual distortion 的 correlation，或明确讨论 constraint 如何将 problem 压回 additive regime。\n\n**N4** [critical] Downstream evaluation 仅限 Qwen\n- Table 5: 0-shot downstream evaluation 仅在 Qwen 执行，其他 4 个模型无 downstream results。PPL 和 downstream accuracy 不总是正相关。\n- 建议：至少在 Llama 和 Yi-1.5 上补充 downstream evaluation。\n\n#### Should-Fix 问题\n\n**W1** Standard vs hires profiling 差异过大（37→100 sensitive heads），但 headline results 用 standard\n**W2** 统计报告不够充分——3 seeds, 仅报告 std，未报告 CI\n**W3** Cross-dataset stability 仅用两个 general-domain 数据集\n**W4** Solver equivalence 缺乏形式化证明，仅有 3 个模型经验观察\n**W5** Runtime benchmark 为 PyTorch simulation，无法支撑部署结论；8.5% overhead 未讨论 cost-benefit\n**W6** \"Non-additive\" 未被形式化定义（super-additive? multiplicative?）\n\n#### Questions for Authors\n1. 为什么没有在所有 5 个模型上运行 unconstrained baselines？\n2. Diagnostic 的 borderline cases（concentration ≈ 0.55, t1/t5 ≈ 0.65）如何处理？\n3. Within-layer brute-force oracle 能否验证 cross-layer compounding 的 near-optimality？\n4. 方法是否依赖 round-to-nearest quantization，对 GPTQ/AWQ 是否适用？\n5. 是否尝试过更高分辨率 profiling（128 seq × 4096 tok）？\n\n#### Missing References\n- MiKV (Yang et al., 2025, ICML 2025)\n- Quantization + eviction 联合策略作为 hybrid baseline\n- KIVI per-channel asymmetric 2-bit 策略\n\n#### 主要优势\n1. 2-bit distortion compounding 是 genuine、previously-undocumented 的问题\n2. 单个 cardinality constraint 是 minimal、elegant 的修复\n3. 4/5 模型 negative results 的诚实报告比只报 Qwen 正面结果更有科学价值\n4. Spread/spike/flat taxonomy 提供了有用的 conceptual vocabulary\n5. Cross-dataset validation、brute-force oracle、KV separation ablation 等设计显示 thorough evaluation 追求\n\n---\n\n请对以上每个 Must-Fix（N1-N4）和 Should-Fix（W1-W6）逐条给出 [AGREE] 或 [REBUT] 回应。"
}
```

---


### Runtime record

_source line 114 · 2026-05-15T04:26:13.145Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T04:26:13.145Z",
  "sessionId": "9fbeb321-60cf-446a-bed1-530795e3f023"
}
```

---


## Round 2

## Round 2

2 recorded events


### User

_source line 115 · 2026-05-15T04:26:13.125Z_

Continue from where you left off.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f155ef15-f5e0-4e22-9b30-4585be582088",
  "isSidechain": false,
  "promptId": "3889f2de-c2c3-4bad-830d-b08a3ef5c9de",
  "type": "user",
  "isMeta": true,
  "uuid": "a7b814b3-e82e-4f89-830d-473b18e0fb90",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_2_ee7a8b68",
  "sessionId": "9fbeb321-60cf-446a-bed1-530795e3f023",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Assistant

_source line 116 · 2026-05-15T04:26:13.125Z_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a7b814b3-e82e-4f89-830d-473b18e0fb90",
  "isSidechain": false,
  "type": "assistant",
  "uuid": "84b04103-7d1c-430b-ae64-0ef02a4958e0",
  "isApiErrorMessage": false,
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_2_ee7a8b68",
  "sessionId": "9fbeb321-60cf-446a-bed1-530795e3f023",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "id": "b56f0b60-bb8c-45fc-93fd-90e40d5ed8c5",
    "container": null,
    "model": "&lt;synthetic>",
    "stop_reason": "stop_sequence",
    "stop_sequence": "",
    "type": "message",
    "usage": {
      "input_tokens": 0,
      "output_tokens": 0,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 0,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": null,
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": null,
      "iterations": null,
      "speed": null
    },
    "context_management": null
  }
}
```

</details>

---


## Round 3

## Round 3

1 recorded events


### User

_source line 117 · 2026-05-15T04:26:13.262Z_

[Round 1 审稿请求]:
## Step 2 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见

以下是 Reviewer 1 的完整审稿意见。请逐条回应：
- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）

---

### Reviewer 1 完整审稿报告

**Overall**: 2.5/5 (Borderline)
**Soundness**: 3/5 | **Excitement**: 3/5 | **Reproducibility**: 3.5/5 | **Confidence**: 4/5

**一句话总结**: 核心发现有实践价值、negative results 诚实报告值得肯定，但评估存在系统性缺口——缺失 4/5 模型 unconstrained baselines、仅 Qwen 有 downstream evaluation、profiling 方法与 compounding 论点逻辑张力未解决、diagnostic 在 5 个同质模型上 overfit。建议补充 N2 和 N4 后作为 Findings paper 考虑。

#### Must-Fix 问题

**N1** [critical] Diagnostic framework 在 5 个数据点上完美拟合——overfitting 风险
- Section 5.2, Table 6: 用 2 个 threshold（concentration ≳0.50, t1/t5 ≲0.70）在 5 个 architecture 上实现 100% 准确分类。用 2 个自由参数完美拟合 5 个样本是经典 overfitting 信号。
- 建议：增加 2–3 个模型验证 threshold 鲁棒性，或降低 claim 力度为 exploratory finding。

**N2** [critical] 4/5 模型缺失 unconstrained baseline
- Table 2: Llama/Mistral/Yi-1.5/Gemma-2 的 unconstrained greedy 和 MCKP 列为 "---"，论文解释 "those experiments were conducted only on Qwen"。compounding 是核心发现，如果只在 1 个模型上验证，无法判断是 Qwen idiosyncratic 还是 general phenomenon。
- 建议：在所有 5 个模型上补跑 unconstrained greedy/MCKP。

**N3** [critical] Profiling methodology 与 compounding 论点的逻辑矛盾
- Section 3.2 vs Section 3.3: Profiling 用 single-head isolation（keep others bf16），但论文论证 distortions 是 non-additive。如果 per-head distortions 是 non-additive 的，single-head profiling 的 d_h(b) 不能准确反映 multi-head actual distortion。
- 建议：增加实验验证 single-head d_h(2) 与 multi-head actual distortion 的 correlation，或明确讨论 constraint 如何将 problem 压回 additive regime。

**N4** [critical] Downstream evaluation 仅限 Qwen
- Table 5: 0-shot downstream evaluation 仅在 Qwen 执行，其他 4 个模型无 downstream results。PPL 和 downstream accuracy 不总是正相关。
- 建议：至少在 Llama 和 Yi-1.5 上补充 downstream evaluation。

#### Should-Fix 问题

**W1** Standard vs hires profiling 差异过大（37→100 sensitive heads），但 headline results 用 standard
**W2** 统计报告不够充分——3 seeds, 仅报告 std，未报告 CI
**W3** Cross-dataset stability 仅用两个 general-domain 数据集
**W4** Solver equivalence 缺乏形式化证明，仅有 3 个模型经验观察
**W5** Runtime benchmark 为 PyTorch simulation，无法支撑部署结论；8.5% overhead 未讨论 cost-benefit
**W6** "Non-additive" 未被形式化定义（super-additive? multiplicative?）

#### Questions for Authors
1. 为什么没有在所有 5 个模型上运行 unconstrained baselines？
2. Diagnostic 的 borderline cases（concentration ≈ 0.55, t1/t5 ≈ 0.65）如何处理？
3. Within-layer brute-force oracle 能否验证 cross-layer compounding 的 near-optimality？
4. 方法是否依赖 round-to-nearest quantization，对 GPTQ/AWQ 是否适用？
5. 是否尝试过更高分辨率 profiling（128 seq × 4096 tok）？

#### Missing References
- MiKV (Yang et al., 2025, ICML 2025)
- Quantization + eviction 联合策略作为 hybrid baseline
- KIVI per-channel asymmetric 2-bit 策略

#### 主要优势
1. 2-bit distortion compounding 是 genuine、previously-undocumented 的问题
2. 单个 cardinality constraint 是 minimal、elegant 的修复
3. 4/5 模型 negative results 的诚实报告比只报 Qwen 正面结果更有科学价值
4. Spread/spike/flat taxonomy 提供了有用的 conceptual vocabulary
5. Cross-dataset validation、brute-force oracle、KV separation ablation 等设计显示 thorough evaluation 追求

---

请对以上每个 Must-Fix（N1-N4）和 Should-Fix（W1-W6）逐条给出 [AGREE] 或 [REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "84b04103-7d1c-430b-ae64-0ef02a4958e0",
  "isSidechain": false,
  "promptId": "3889f2de-c2c3-4bad-830d-b08a3ef5c9de",
  "type": "user",
  "uuid": "feeeda03-a247-4bf7-93e4-26e8e8679cef",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/.claude/sessions/review_reviewer_2_ee7a8b68",
  "sessionId": "9fbeb321-60cf-446a-bed1-530795e3f023",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---
