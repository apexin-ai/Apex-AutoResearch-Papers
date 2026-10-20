# Research conversation: [Round 1 审稿请求]: ## Round 1 审稿任务 — Reviewer 2（新颖性 + 完整性 + 写作质量） ### 目标 Venue - **EMNLP 2026**（通过 ARR May 2026 提交） - 截止日期： — Part 2 of 2

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../research-conversation-round-1-round-1-reviewer-2-venue-emnlp-2026-arr-may-2026.md) · [Structured JSON](../../../sessions/a4/a4bd8d0a0c663f141dac.json)

## Round 5

### Assistant

_source line 159 · 2026-05-19T10:06:51.878Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a detailed understanding of the Dream paper. Let me compare it with the original paper I reviewed earlier and also with the review_context.yaml (which contains the imagined experiments).

Key differences between the Dream paper and the original:
1. **Title change**: "Bounded Depth Discrimination in Recursive Synthetic Text: Measuring K* Across Domains, Architectures, and Scales" vs. original "Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary"
2. **Code domain added**: New fourth domain (Python code), making the hierarchy 4 domains instead of 3


3. **Extended scale range**: Now includes a 32B model alongside the original 14B, plus additional architecture families (6 instead of 5)
4. **Formalized domain ceiling framework**: Separated out as its own contribution distinct from competence measurement
5. **Naturalistic validation**: Added 50K Common Crawl documents from 2025/2026 to test against real-world text
6. **Higher saturation threshold**: K*≥7 for retrain-chain versus K*≥4 in the original
7. **Stronger claims**: The paper now asserts that domain structural complexity is the sole systematic determinant of K*, and uses DPI to prove finite saturation in the introduction—both more definitive than the original framing

Now I'm structuring my review around novelty, related work coverage, and consistency between claims and experiments. Looking at the core contributions, the K* measurement itself remains the same foundational framework from the original work. The domain ceiling concept adds a useful lens but functions more as a post-hoc explanation of the data rather than a predictive tool. The Code domain and 32B extension feel incremental—the latter likely just confirms what we'd expect at larger scales. Against Drayson et al., this generalizes from binary to ordinal relationships, which is a natural progression. For related work, I'm noticing some gaps in coverage, particularly around citations that should be included.

I'm also catching a potential inconsistency in the narrative. The abstract and conclusion claim that domain structural complexity is the sole systematic determinant of K*, but the ANOVA results show Generator effects with substantial effect sizes that aren't being reported or reconciled with this claim.

There's a gap between what the paper claims about proving recursive generation must reach saturation—the DPI argument motivates this but doesn't formally establish that pairwise AUC between adjacent generations converges to a specific K*. The logical leap feels stronger than the evidence supports.

The domain ceiling framework has a circularity problem: it's fit to the data then validated against the same observations, and any K* value can be post-hoc explained as either hitting the ceiling or falling short of it. This makes the framework unfalsifiable rather than the predictive tool it's presented as.

There are also some inconsistencies in the numbers—the retrain-chain K* appears to be ≥7 in the discussion versus ≥4 in the original, which suggests either different operationalization or potential inflation. The naturalistic validation on wild data lacks ground truth, and the correlations with AlignScore and TTR are somewhat expected given that TTR is already part of the feature set and AlignScore correlates with perplexity. The binary K*-aware filtering improvement is quite modest at around 0.8 percentage points, though it's presented more prominently here. I'm also noticing the PDF seems to be missing a references section entirely, which is a significant completeness issue for a top-tier venue submission.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad04da8d-f973-4a20-aa75-1ca790ea153b",
  "isSidechain": false,
  "requestId": "req_011CbBjv1omHz3mBQJCfqqbg",
  "type": "assistant",
  "uuid": "10aaae8f-806a-4fa7-9a68-badbe1facce2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015ML7XHuWxjXQdQGD1x2jRQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8472,
      "cache_read_input_tokens": 128934,
      "output_tokens": 4918,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8472,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4918,
          "cache_read_input_tokens": 128934,
          "cache_creation_input_tokens": 8472,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8472
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---


### Assistant

_source line 160 · 2026-05-19T10:06:52.225Z_

我已获取了 Dream 论文的完整内容和实验设计上下文。现在撰写审稿报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "10aaae8f-806a-4fa7-9a68-badbe1facce2",
  "isSidechain": false,
  "requestId": "req_011CbBjv1omHz3mBQJCfqqbg",
  "type": "assistant",
  "uuid": "ca81bf92-715e-46d6-be87-40da01cb9e71",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015ML7XHuWxjXQdQGD1x2jRQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8472,
      "cache_read_input_tokens": 128934,
      "output_tokens": 4918,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8472,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4918,
          "cache_read_input_tokens": 128934,
          "cache_creation_input_tokens": 8472,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8472
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---


### Tool call

_source line 161 · 2026-05-19T10:08:03.528Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director · `toolu_01T7wVtwz3PyVMbouHS6uUaB`</summary>

```json
{
  "text": "## Reviewer 2 — Dream 审稿报告（新颖性 + 相关工作 + Story 一致性）\n\n**论文**: Bounded Depth Discrimination in Recursive Synthetic Text: Measuring K* Across Domains, Architectures, and Scales\n**评分标准**: Top ML venue 通用标准（6 分制）\n\n---\n\n### 1. Summary\n\n论文提出基于 DPI 的 generational depth discrimination boundary K\\* 框架，通过 4 个域（Wikipedia, C4, Code, arXiv）、6 个架构族（1B-32B）、4 种解码策略的交叉实验，建立了 K\\* ∈ {1,2,3} 的 domain hierarchy（Wiki=1, C4=Code=2, arXiv=3）。核心 claim 是 domain structural complexity 是 K\\* 的唯一系统性决定因子，并提出 domain ceiling framework 统一解释所有观测值。附加贡献包括 Common Crawl 野外验证和 K\\*-aware binary filtering 的实用价值。\n\n---\n\n### 2. Strengths\n\n- **问题定义清晰且有实际意义**：将 recursive contamination 从 binary detection 推广到 ordinal depth estimation，K\\* 作为 domain-level 属性的概念化有学术和实用价值。\n\n- **实验覆盖广**（idea 层面）：4 域 × 6 架构 × 1B-32B × 4 解码策略的交叉设计，相比仅做 web text 的 detection 工作，大幅提升了 claim 的支撑面。Code 域的加入将框架从 natural language 扩展到 code modality，是有意义的 generalization。\n\n- **Domain ceiling framework 概念有解释力**（idea 层面）：将 K\\* 分解为 domain ceiling 和 model competence 两个独立因子，提供了统一的叙事框架。Mistral-7B 跨三域 K\\*={1,2,3} 的 ladder 是一个非常有说服力的案例（Table 6）。\n\n- **Naturalistic validation 方向正确**（idea 层面）：在 50K Common Crawl 文档上做 plausibility check，虽然没有 ground truth，但与 AlignScore / TTR 的 correlation direction 验证了框架在 wild 数据上的行为合理性。\n\n---\n\n### 3. Weaknesses\n\n**W1** [Major, idea 层面] **\"Sole systematic determinant\" 是明确的 overclaim，论文内部证据自相矛盾**\n\nAbstract 声称 \"domain structural complexity is the sole systematic determinant of K\\*\"，Conclusion 重复此 claim。但论文自身报告：\n- Mistral-7B C4 K\\*=1 而其他 7 个模型 K\\*=2 → model identity 确实影响 K\\*\n- Pythia-1.4B Code K\\*=1 而其他 4 个模型 K\\*=2 → 同上\n- OLMo-1B arXiv K\\*=1 而其他 5 个模型 K\\*=3 → 同上\n\n论文通过 \"competence failure\" 事后解释这些异常，但这恰恰说明 model identity 不是 irrelevant——domain ceiling 设定了 upper bound，而 model competence 决定实际 K\\*。正确表述应为 \"domain structure sets the ceiling; model competence determines whether the ceiling is reached\"，这在 Section 5.1 内文中确实如此表述，但 Abstract 和 Conclusion 的 \"sole determinant\" 与之矛盾。这是 story consistency 的核心问题。\n\n**W2** [Major, idea 层面] **DPI → finite K\\* 的理论论证有逻辑跳跃，Contribution 1 的 \"prove\" 过强**\n\nContribution 1 声称 \"formalize K\\* via DPI and prove that recursive generation must produce a finite saturation point\"。但：\n- DPI 保证 I(X₀; Xₖ) 单调递减 → 正确\n- 但 K\\* 定义为 adjacent-generation pairwise AUC > θ，即 AUC(Xₖ₋₁ vs Xₖ)，这是不同的量。I(X₀; Xₖ) 递减不直接蕴含 adjacent-generation 信号递减\n- 从 mutual information 递减到 finite K\\* 需要额外的 Markov chain mixing rate 假设（contraction mapping 或 ergodicity conditions），论文未提供\n- \"prove\" 应改为 \"motivate\" 或 \"provide theoretical grounding under standard assumptions\"\n\n这不是 fatal flaw（论文的核心价值在 empirical characterization 而非 theory），但 Contribution 1 的措辞与实际论证力度不匹配。\n\n**W3** [Major, idea 层面] **Domain ceiling framework 存在不可证伪性问题**\n\nFramework 的逻辑：K\\* = ceiling → model competent; K\\* < ceiling → model lacks competence. 但 \"competence\" 的定义依赖于观测到的 K\\* 本身：\n- 如何 a priori 判断一个模型是否 \"domain-competent\"？论文提到 \"pretraining data mismatch\"（Mistral 的 web bias, Pythia 的 code-sparse Pile），但这些是 post-hoc rationalizations\n- Framework 无法预测一个新模型在一个新域上的 K\\*，因为 \"competence\" 只能在观测 K\\* 后确认\n- 声称 \"falsifiable predictions\"（Section 5.1）但实际上任何 K\\* 值都可以被框架解释\n\n建议：要使 framework 真正 falsifiable，需要一个独立的 competence proxy（如 domain-specific benchmark score vs. K\\* 的 correlation），而非循环定义。\n\n**W4** [Minor, idea 层面] **Naturalistic CC validation 存在部分循环性**\n\nTTR（type-token ratio）和 hapax ratio 是 15D 特征集的组成部分（Section 3.5），depth 分类器本身就使用这些特征做预测。因此 \"predicted depth 与 TTR/hapax 负相关\" 在一定程度上是 tautological——分类器使用 TTR 作为特征来预测 depth，然后发现 predicted depth 与 TTR 相关。AlignScore 是独立指标，其 correlation (ρ=-0.31) 是有意义的，但 TTR/hapax 的 correlation 价值有限。\n\n**W5** [Minor, presentation 层面] **Related Work 覆盖不足，遗漏重要工作**\n\n基于论文内容，以下重要工作似乎未被引用或讨论不充分：\n- **Gambetta et al. (2024) surplexity**: 唯一一个提出 per-text collapse indicator 的工作，与本文最直接相关，必须讨论差异\n- **Binoculars (Hans et al. 2024)**: 基于 PPL ratio 的 zero-shot detection，与本文 cross-scorer 实验直接相关\n- **Fast-DetectGPT (Bao et al. 2024)**: conditional probability curvature 方法\n- **DivEye (Basani & Chen 2026)**: 使用 diversity features，与 15D 特征集高度重叠\n- **Drayson et al. (2025)**: binary detection + importance resampling，是 K\\*=1 的 special case，必须显式讨论\n- **Deep ordinal regression (CORAL, Cao et al. 2020)**: 作为 OBD 的 alternative 应被讨论\n- **LightGBM (Ke et al. 2017)**: 核心分类器的原始引用\n\n此外，reference list 在 PDF 中似乎缺失或被截断，这是完整度问题。\n\n**W6** [Minor, presentation 层面] **引用密度偏低**\n\nRelated Work 仅约半页、4 个 paragraph，对于 top venue 明显不足。相比之下，同类论文（如 DetectGPT, Binoculars）的 Related Work 通常覆盖 30-40 篇引用。论文应至少覆盖：model collapse (5-8 篇)、binary detection (6-10 篇)、data curation (4-6 篇)、ordinal classification (2-3 篇)、information-theoretic foundations (2-3 篇)。\n\n**W7** [Minor, idea 层面] **Code 域与 C4 域 K\\*=2 的等价性缺乏深入分析**\n\nCode 和 C4 都给出 K\\*=2，但它们的信息结构显著不同（syntax trees vs. free-form text）。Section 5.1 指出 JSD cliff 位置不同（Code 在 1v2→2v3，C4 在 0v1→1v2），这是有趣的观察，但论文未深入分析为何结构如此不同的两个域给出相同的 K\\*。这削弱了 \"domain structural complexity determines K\\*\" 的因果解释——如果两个结构截然不同的域碰巧 K\\* 相同，那 \"complexity\" 到底测量的是什么？\n\n**W8** [Minor, idea 层面] **Retrain-chain K\\*≥7 与 prompt-chain K\\*=2 的巨大差距未充分讨论**\n\nDiscussion 提到 retrain-chain K\\*≥7（vs prompt-chain K\\*=2），但将其归因于 \"model-adaptation artifacts\" 并声称 \"prompt-chain K\\* is the operational boundary for data curation\"。这一判断缺乏论证：现实世界的 recursive contamination 混合了 prompting 和 retraining，为何 prompt-chain 的 K\\* 更 \"operational\"？如果某人用合成数据 fine-tune 模型后再生成，K\\* 应取哪个值？\n\n---\n\n### 4. Questions for Authors\n\nQ1. 能否提供一个独立的 \"domain competence\" proxy（如 domain-specific perplexity 或 benchmark score），并展示它与 K\\* 的 correlation，使 ceiling framework 变为 predictive 而非 explanatory？\n\nQ2. 如果在 C4 上训练分类器但在 Code 上测试（或反之），transfer accuracy 如何？同 K\\*=2 是否意味着相同的 depth features？\n\nQ3. DPI 从 I(X₀;Xₖ) 递减到 adjacent-pair AUC 递减的推导中，需要什么 exact conditions？是否存在 Markov chain 满足 DPI 但 adjacent-pair AUC 非单调递减的 counterexample？\n\nQ4. Common Crawl validation 中，如果从 correlation 分析中移除 TTR 和 hapax ratio（即分类器自身使用的特征），仅保留 AlignScore，correlation structure 是否仍然成立？\n\nQ5. 为什么 retrain-chain K\\*≥7 而非 ≥4（与原始工作的差异）？操作定义是否发生了变化？\n\n---\n\n### 5. 评分建议\n\n**Novelty + Related Work + Story Consistency 综合评分: 4 / 6 (Borderline Accept)**\n\n**理由**：\n\n加分项：\n- K\\* 作为 domain-level 属性的概念化是 genuinely novel，此前无工作形式化并测量 recursive generation 的 discrimination boundary\n- 4 域 × 6 架构 × 32B 的实验覆盖对于 empirical contribution 论文是充分的\n- Domain ceiling framework 虽有可证伪性问题，但作为 organizing principle 有价值\n- Mistral cross-domain ladder 是 compelling evidence\n\n减分项：\n- Abstract/Conclusion 的 \"sole determinant\" 与论文内部证据矛盾（W1），这是 story consistency 的核心缺陷\n- Contribution 1 的 \"prove\" 声称过强（W2），与实际论证力度不匹配\n- Domain ceiling framework 的不可证伪性（W3）削弱了其作为独立 contribution 的分量\n- Related Work 覆盖明显不足，遗漏 5+ 篇直接相关工作（W5, W6）\n- Code 与 C4 的 K\\*=2 等价性缺乏因果解释（W7）\n\n如果 W1 的 overclaim 被修正（\"sole\" → \"primary\"）、W2 的 \"prove\" 被弱化、W5 的缺失引用被补充，论文可达 Accept 水平。当前版本的 story consistency 问题（claim 强于 evidence）是主要拦路石。",
  "reviewer_id": "2",
  "project": "gen-depth-contamination"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ca81bf92-715e-46d6-be87-40da01cb9e71",
  "isSidechain": false,
  "requestId": "req_011CbBjv1omHz3mBQJCfqqbg",
  "type": "assistant",
  "uuid": "66ed97ed-260a-4af1-880b-796e5cef87f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015ML7XHuWxjXQdQGD1x2jRQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8472,
      "cache_read_input_tokens": 128934,
      "output_tokens": 4918,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8472,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4918,
          "cache_read_input_tokens": 128934,
          "cache_creation_input_tokens": 8472,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8472
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---


### Tool result

_source line 162 · 2026-05-19T10:08:07.432Z_

<details><summary>↩ Tool result · `toolu_01T7wVtwz3PyVMbouHS6uUaB`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "66ed97ed-260a-4af1-880b-796e5cef87f8",
  "isSidechain": false,
  "promptId": "28ce5ee5-0c5a-4cb9-810b-2c245f14d06b",
  "type": "user",
  "uuid": "6c341207-4e5a-4667-a976-dd361ee079df",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"review_director_key\\\": \\\"feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_0f6dcb30efaa4f47425ef1d9874a89d7:director\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "66ed97ed-260a-4af1-880b-796e5cef87f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 163 · 2026-05-19T10:08:07.437Z_

```json
{
  "parentUuid": "6c341207-4e5a-4667-a976-dd361ee079df",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "619dd413-a72d-4e70-b075-b5057844632b",
  "timestamp": "2026-05-19T10:08:07.437Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Runtime record

_source line 164_

```json
{
  "type": "ai-title",
  "aiTitle": "Review paper on data contamination detection for EMNLP 2026",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77"
}
```

---


### Runtime record

_source line 165 · 2026-05-19T13:05:10.821Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-19T13:05:10.821Z",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77",
  "content": "[Round 2 审稿请求]:\n## Round 9（继续审稿）— Reviewer 2（新颖性 + 完整性 + 写作质量）\n\n上轮评分：3.5 (Borderline Conference)。论文已大幅修订，请重点验证以下 open/in_progress issues 是否已充分修复。\n\n### 论文路径\n`projects/gen-depth-contamination/docs/paper/main.tex`\n\n### Venue\nEMNLP 2026 (ARR May), Long paper 8 页, double-blind, deadline 2026-05-25\n\n---\n\n### 需逐条标注 [RESOLVED] 或 [STILL_OPEN] 的 Issue 清单\n\n**CRITICAL issues (in_progress):**\n\n**R8-N1** θ=0.60 post-hoc 选择\n- 已知修改：LOFO cross-validation 入稿（θ̂∈[0.5725, 0.6004]，8/9 agreement）\n- 请验证：LOFO 是否真正独立？是否充分回应你上轮的 held-out validation 建议？\n\n**R8-N2** prompt-chain vs retrain-chain gap\n- 已知修改：(1) Section 5 明确 \"consistency check using prompt-chain\"；(2) retrain-chain K*=7（2 模型）；(3) Limitations 更新\n- 请验证：practical claim 是否已充分限定？\n\n**R8-N3** \"sole\" → \"primary\"\n- 请检查全文一致性。\n\n**WARNING issues (in_progress/open):**\n\n**R8-W1** DPI \"motivates\" 限定\n**R8-W2** Qwen 5/9 偏向 → family-level reporting\n**R8-W3** Filtering 框定为 consistency check\n**R8-W4** Transfer matrix 仅 4/9 (OPEN)\n**R8-W5** Cross-scorer 措辞 + McNemar 修正\n**R8-W6** One-wash 精确化\n**R8-W7** arXiv cross-scorer CI 表述\n\n**INFO issues:**\n\n**R8-M2** Missing references (LightGBM \\cite{ke2017lightgbm}, CORAL \\cite{cao2020coral}, Oren 2024, DivEye 讨论)\n**R8-M3** -ing phrases 改写\n**R8-M4** Abstract 术语 + Neural probe 样本量\n\n**新增 Round 10 issues:**\n\n**R10-N1** McNemar false claim 修正\n**R10-N2** Code domain 作为第 4 域\n\n---\n\n### 审查重点\n\n1. 逐条标注每个 issue 为 [RESOLVED] 或 [STILL_OPEN]\n2. **写作质量重新评估**：Related Work 覆盖度是否改善？引用密度？-ing phrases 是否减少？\n3. **新颖性重新评估**：Code domain + 4-domain ordering + retrain-chain K*=7 是否提升 Excitement？\n4. **正文 8 页限制**：新增 code 域 + LOFO 内容后是否超页？\n5. 检查修改是否引入新问题\n6. 用户规则检查：正文行文中是否出现破折号（专有名词除外）？\n\n请出具：Issue Resolution Status → New Issues (if any) → Updated Strengths/Weaknesses → Updated Overall Assessment（ARR 标准）"
}
```

---


### Runtime record

_source line 166 · 2026-05-19T13:05:10.821Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-19T13:05:10.821Z",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77"
}
```

---


## Round 6

## Round 6

2 recorded events


### User

_source line 167 · 2026-05-19T13:05:10.793Z_

Continue from where you left off.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "619dd413-a72d-4e70-b075-b5057844632b",
  "isSidechain": false,
  "promptId": "12172553-d9aa-40c5-a42d-a4d4469a539a",
  "type": "user",
  "isMeta": true,
  "uuid": "f48fed6a-14bd-4a8c-a094-0fa3ce4681bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Assistant

_source line 168 · 2026-05-19T13:05:10.794Z_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f48fed6a-14bd-4a8c-a094-0fa3ce4681bd",
  "isSidechain": false,
  "type": "assistant",
  "uuid": "7510d974-76f7-47d4-a652-87e3ada18e0e",
  "isApiErrorMessage": false,
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "id": "12bb95ef-d512-43f8-8f68-eddf5b453bd3",
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


## Round 7

## Round 7

29 recorded events


### User

_source line 169 · 2026-05-19T13:05:10.917Z_

[Round 2 审稿请求]:
## Round 9（继续审稿）— Reviewer 2（新颖性 + 完整性 + 写作质量）

上轮评分：3.5 (Borderline Conference)。论文已大幅修订，请重点验证以下 open/in_progress issues 是否已充分修复。

### 论文路径
`projects/gen-depth-contamination/docs/paper/main.tex`

### Venue
EMNLP 2026 (ARR May), Long paper 8 页, double-blind, deadline 2026-05-25

---

### 需逐条标注 [RESOLVED] 或 [STILL_OPEN] 的 Issue 清单

**CRITICAL issues (in_progress):**

**R8-N1** θ=0.60 post-hoc 选择
- 已知修改：LOFO cross-validation 入稿（θ̂∈[0.5725, 0.6004]，8/9 agreement）
- 请验证：LOFO 是否真正独立？是否充分回应你上轮的 held-out validation 建议？

**R8-N2** prompt-chain vs retrain-chain gap
- 已知修改：(1) Section 5 明确 "consistency check using prompt-chain"；(2) retrain-chain K*=7（2 模型）；(3) Limitations 更新
- 请验证：practical claim 是否已充分限定？

**R8-N3** "sole" → "primary"
- 请检查全文一致性。

**WARNING issues (in_progress/open):**

**R8-W1** DPI "motivates" 限定
**R8-W2** Qwen 5/9 偏向 → family-level reporting
**R8-W3** Filtering 框定为 consistency check
**R8-W4** Transfer matrix 仅 4/9 (OPEN)
**R8-W5** Cross-scorer 措辞 + McNemar 修正
**R8-W6** One-wash 精确化
**R8-W7** arXiv cross-scorer CI 表述

**INFO issues:**

**R8-M2** Missing references (LightGBM \cite{ke2017lightgbm}, CORAL \cite{cao2020coral}, Oren 2024, DivEye 讨论)
**R8-M3** -ing phrases 改写
**R8-M4** Abstract 术语 + Neural probe 样本量

**新增 Round 10 issues:**

**R10-N1** McNemar false claim 修正
**R10-N2** Code domain 作为第 4 域

---

### 审查重点

1. 逐条标注每个 issue 为 [RESOLVED] 或 [STILL_OPEN]
2. **写作质量重新评估**：Related Work 覆盖度是否改善？引用密度？-ing phrases 是否减少？
3. **新颖性重新评估**：Code domain + 4-domain ordering + retrain-chain K*=7 是否提升 Excitement？
4. **正文 8 页限制**：新增 code 域 + LOFO 内容后是否超页？
5. 检查修改是否引入新问题
6. 用户规则检查：正文行文中是否出现破折号（专有名词除外）？

请出具：Issue Resolution Status → New Issues (if any) → Updated Strengths/Weaknesses → Updated Overall Assessment（ARR 标准）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7510d974-76f7-47d4-a652-87e3ada18e0e",
  "isSidechain": false,
  "promptId": "12172553-d9aa-40c5-a42d-a4d4469a539a",
  "type": "user",
  "uuid": "ee3b00fc-f551-4d41-a8e7-50d47cce247c",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Assistant

_source line 170 · 2026-05-19T13:05:15.558Z_

开始 Round 2 审稿。重新读取修订后的论文全部章节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ee3b00fc-f551-4d41-a8e7-50d47cce247c",
  "isSidechain": false,
  "requestId": "req_011CbByZGQtZEGUDeiPCaKvC",
  "type": "assistant",
  "uuid": "d49d1d13-3e47-4a11-b49e-42eaade0c809",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R5aasAvdxKFuGzJ54fMWnH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 129871,
      "cache_read_input_tokens": 11841,
      "output_tokens": 479,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 129871,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 479,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 129871,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 129871
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---


### Tool call

_source line 171 · 2026-05-19T13:05:16.983Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YHFqDUi67z2TDmiysx2szT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d49d1d13-3e47-4a11-b49e-42eaade0c809",
  "isSidechain": false,
  "requestId": "req_011CbByZGQtZEGUDeiPCaKvC",
  "type": "assistant",
  "uuid": "8ca77a69-59af-4a00-b8a9-b53c34ac152a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R5aasAvdxKFuGzJ54fMWnH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 129871,
      "cache_read_input_tokens": 11841,
      "output_tokens": 479,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 129871,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 479,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 129871,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 129871
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---


### Tool result

_source line 172 · 2026-05-19T13:05:17.001Z_

<details><summary>↩ Tool result · `toolu_01YHFqDUi67z2TDmiysx2szT`</summary>

```text
1	% EMNLP 2026 Main - ARR May 2026
2	% Generational Depth Contamination
3	\documentclass[11pt]{article}
4	\usepackage[review]{acl}
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\usepackage{amsmath}
12	\usepackage{amssymb}
13	\usepackage{booktabs}
14	\usepackage{multirow}
15	\usepackage{enumitem}
16	\usepackage{subcaption}
17	\usepackage{pifont}
18	\newcommand{\cmark}{\ding{51}}
19	\newcommand{\xmark}{\ding{55}}
20	\usepackage[section]{placeins}
21	
22	\newcommand{\Kstar}{{K^*}}
23	\newcommand{\Kempirical}{{K^*_{\text{empirical}}}}
24	\newcommand{\Ktheory}{{K^*_{\text{theory}}}}
25	\newcommand{\auc}{\text{AUC}}
26	\newcommand{\jsd}{\text{JSD}}
27	\newcommand{\tpm}{\ensuremath{\,\pm\,}}
28	
29	\title{Generational Depth Estimation of Recursive Synthetic Text:\\Measuring the Discrimination Boundary}
30	
31	\author{Anonymous}
32	
33	\begin{document}
34	\maketitle
35	
36	% === Abstract ===
37	\begin{abstract}
38	Web-scale corpora are increasingly contaminated by recursive synthetic content, yet no method estimates a document's generational depth.
39	We measure the discrimination boundary $\Kempirical$ (the maximum depth at which adjacent generations remain distinguishable) using 15 statistical features and an OBD-LightGBM classifier.
40	Across five architecture families (1B--14B), four source domains (three text, one code), and four decoding strategies at $\theta{=}0.60$ (AUC decision threshold), $\Kempirical{=}2$ for general web text (8/9 model configurations), $\Kempirical{=}1$--$2$ for code (Python, model-dependent), and $\Kempirical{=}3$ for structured academic text (arXiv).
41	A single additional generation pass suffices to render first-generation synthetic web text indistinguishable from deeper synthetic content, a \emph{one-wash laundering} effect.
42	Largely generator-independent statistical features, computed via a fixed reference scorer, enable 80--92\% accuracy retention among continuation-mode generators, and cross-scorer validation confirms that $\Kempirical$ is largely robust to scorer choice.
43	Downstream, $\Kempirical$ characterizes discriminability boundaries that inform, but do not directly determine, filtering strategy; for web text ($\Kempirical{=}2$), binary filtering aligns with the two-level discriminability structure.
44	\end{abstract}
45	
46	% === Section 1: Introduction ===
47	\input{introduction}
48	
49	% === Section 2: Related Work ===
50	\input{related_work}
51	
52	% === Section 3: Method ===
53	\input{method}
54	
55	% === Section 4: Experiments ===
56	\input{experiments_c1}
57	
58	% === Section 5: K*-Aware Data Filtering ===
59	\input{experiments_c3}
60	
61	% === Section 6: Discussion ===
62	\input{discussion}
63	
64	% === Section 7: Conclusion ===
65	\input{conclusion}
66	
67	% === Limitations (ACL required, unnumbered) ===
68	\clearpage
69	\section*{Limitations}
70	
71	Our findings are bounded by:
72	(1)~\emph{Scope}: model scale $\leq$14B (5 architecture families), English text (C4, Wikipedia, arXiv) and Python code (CodeSearchNet), four decoding strategies; arXiv $\Kempirical{=}3$ is confirmed with five models across four architecture families but with reduced sample size ($n{=}2{,}200$ per model); code domain tested with five models across four families (Qwen2.5-1.5B/7B, LLaMA-3.1-8B, Mistral-7B-v0.3, $\Kempirical{=}2$; Pythia-1.4B, $\Kempirical{=}1$ with 1v2 CI upper bound $> \theta$); subsampling analysis indicates $n{\geq}2{,}000$ suffices for 100\% reliable $\Kempirical$ determination (Appendix~\ref{sec:power_curve}).
73	(2)~\emph{Protocol}: all main experiments use prompt-chain, which isolates text-intrinsic degradation from training dynamics; real-world contamination involves both prompting and retraining, and retrain-chain yields $\Kempirical{=}7$ (both Qwen-1.5B and Pythia-1.4B LoRA; Appendix~\ref{sec:extended_limitations}), so prompt-chain $\Kempirical$ may underestimate discriminability in mixed settings.
74	(3)~\emph{Threshold}: $\Kempirical$ ranges from 2--3 at $\theta{=}0.55$ to 1 at $\theta{=}0.70$; 8/9 configurations yield $\Kempirical{=}2$ at $\theta{=}0.60$ (Mistral-7B: $\Kempirical{=}1$).
75	(4)~\emph{Marginal boundary}: Qwen-continuation's 1v2 CI lower bound exceeds $\theta$ by only 0.002; cross-scorer validation drops this to $\Kempirical{=}1$ (Section~\ref{sec:transfer}). LLaMA-3.1-8B (C4) and Mistral-7B-v0.3 (code) represent the most marginal $\Kempirical{=}2$ assignments, with 1v2 CI lower bounds within 0.3 percentage points of $\theta$.
76	(5)~\emph{Feature set}: the 15D features yield a feature-set-specific lower bound ($\Ktheory$ may be strictly higher); neural probe $\Kempirical$ is model-dependent ($3$ for Qwen, $2$ for Pythia/OLMo).
77	(6)~\emph{Segment length}: $\Kempirical{=}2$ confirmed for 128 and 256 tokens (CI lower $> \theta$); 512 tokens yields point estimate $\Kempirical{=}2$ but CI lower marginally below $\theta$ ($0.5979$); the boundary weakens at longer generation lengths.
78	(7)~\emph{Curation applicability}: the filtering evaluation is validated on two architectures (Qwen2.5-1.5B-Instruct and Pythia-1.4B) with consistent strategy ordering (Appendix~\ref{sec:pythia_filtering}), though absolute improvement remains small and effect sizes diminish at lower contamination ratios (10--50\%; Appendix~\ref{sec:dose_response}).
79	(8)~\emph{Family balance}: the Qwen2.5 family provides 5/9 configurations; though spanning three scales (1.5B, 7B, 14B) and two training variants (base, instruct), aggregate statistics weight this family more heavily than the four single-configuration families.
80	Additional limitations (cross-model scoring sensitivity, feature ranking variability at the 1v2 boundary, structural composition confound analysis) appear in Appendix~\ref{sec:extended_limitations}.
81	
82	% === Ethics Statement (ACL required, unnumbered) ===
83	\section*{Ethics Statement}
84	
85	Generational depth estimation is intended for data curation and corpus auditing, positive-sum applications that improve training data quality.
86	Our experiments use publicly available corpora (C4, Wikipedia, arXiv abstracts) and do not involve personally identifiable information.
87	A potential dual-use concern is that depth estimation techniques could inform adversarial strategies to evade detection (e.g., by calibrating rewriting to mimic earlier-generation statistics); we note that this risk is shared by all detection research and that the binary detection boundary ($\auc \geq 0.96$ at 0v1) remains robust.
88	Code and generated corpora will be released upon acceptance to enable reproducibility.
89	
90	\bibliography{references}
91	
92	\input{appendix}
93	\input{appendix_extended}
94	
95	\end{document}
96	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8ca77a69-59af-4a00-b8a9-b53c34ac152a",
  "isSidechain": false,
  "promptId": "12172553-d9aa-40c5-a42d-a4d4469a539a",
  "type": "user",
  "uuid": "7a178695-e5d7-4e50-b9f0-c38ad2330bca",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex",
      "content": "% EMNLP 2026 Main - ARR May 2026\n% Generational Depth Contamination\n\\documentclass[11pt]{article}\n\\usepackage[review]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{enumitem}\n\\usepackage{subcaption}\n\\usepackage{pifont}\n\\newcommand{\\cmark}{\\ding{51}}\n\\newcommand{\\xmark}{\\ding{55}}\n\\usepackage[section]{placeins}\n\n\\newcommand{\\Kstar}{{K^*}}\n\\newcommand{\\Kempirical}{{K^*_{\\text{empirical}}}}\n\\newcommand{\\Ktheory}{{K^*_{\\text{theory}}}}\n\\newcommand{\\auc}{\\text{AUC}}\n\\newcommand{\\jsd}{\\text{JSD}}\n\\newcommand{\\tpm}{\\ensuremath{\\,\\pm\\,}}\n\n\\title{Generational Depth Estimation of Recursive Synthetic Text:\\\\Measuring the Discrimination Boundary}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n% === Abstract ===\n\\begin{abstract}\nWeb-scale corpora are increasingly contaminated by recursive synthetic content, yet no method estimates a document's generational depth.\nWe measure the discrimination boundary $\\Kempirical$ (the maximum depth at which adjacent generations remain distinguishable) using 15 statistical features and an OBD-LightGBM classifier.\nAcross five architecture families (1B--14B), four source domains (three text, one code), and four decoding strategies at $\\theta{=}0.60$ (AUC decision threshold), $\\Kempirical{=}2$ for general web text (8/9 model configurations), $\\Kempirical{=}1$--$2$ for code (Python, model-dependent), and $\\Kempirical{=}3$ for structured academic text (arXiv).\nA single additional generation pass suffices to render first-generation synthetic web text indistinguishable from deeper synthetic content, a \\emph{one-wash laundering} effect.\nLargely generator-independent statistical features, computed via a fixed reference scorer, enable 80--92\\% accuracy retention among continuation-mode generators, and cross-scorer validation confirms that $\\Kempirical$ is largely robust to scorer choice.\nDownstream, $\\Kempirical$ characterizes discriminability boundaries that inform, but do not directly determine, filtering strategy; for web text ($\\Kempirical{=}2$), binary filtering aligns with the two-level discriminability structure.\n\\end{abstract}\n\n% === Section 1: Introduction ===\n\\input{introduction}\n\n% === Section 2: Related Work ===\n\\input{related_work}\n\n% === Section 3: Method ===\n\\input{method}\n\n% === Section 4: Experiments ===\n\\input{experiments_c1}\n\n% === Section 5: K*-Aware Data Filtering ===\n\\input{experiments_c3}\n\n% === Section 6: Discussion ===\n\\input{discussion}\n\n% === Section 7: Conclusion ===\n\\input{conclusion}\n\n% === Limitations (ACL required, unnumbered) ===\n\\clearpage\n\\section*{Limitations}\n\nOur findings are bounded by:\n(1)~\\emph{Scope}: model scale $\\leq$14B (5 architecture families), English text (C4, Wikipedia, arXiv) and Python code (CodeSearchNet), four decoding strategies; arXiv $\\Kempirical{=}3$ is confirmed with five models across four architecture families but with reduced sample size ($n{=}2{,}200$ per model); code domain tested with five models across four families (Qwen2.5-1.5B/7B, LLaMA-3.1-8B, Mistral-7B-v0.3, $\\Kempirical{=}2$; Pythia-1.4B, $\\Kempirical{=}1$ with 1v2 CI upper bound $> \\theta$); subsampling analysis indicates $n{\\geq}2{,}000$ suffices for 100\\% reliable $\\Kempirical$ determination (Appendix~\\ref{sec:power_curve}).\n(2)~\\emph{Protocol}: all main experiments use prompt-chain, which isolates text-intrinsic degradation from training dynamics; real-world contamination involves both prompting and retraining, and retrain-chain yields $\\Kempirical{=}7$ (both Qwen-1.5B and Pythia-1.4B LoRA; Appendix~\\ref{sec:extended_limitations}), so prompt-chain $\\Kempirical$ may underestimate discriminability in mixed settings.\n(3)~\\emph{Threshold}: $\\Kempirical$ ranges from 2--3 at $\\theta{=}0.55$ to 1 at $\\theta{=}0.70$; 8/9 configurations yield $\\Kempirical{=}2$ at $\\theta{=}0.60$ (Mistral-7B: $\\Kempirical{=}1$).\n(4)~\\emph{Marginal boundary}: Qwen-continuation's 1v2 CI lower bound exceeds $\\theta$ by only 0.002; cross-scorer validation drops this to $\\Kempirical{=}1$ (Section~\\ref{sec:transfer}). LLaMA-3.1-8B (C4) and Mistral-7B-v0.3 (code) represent the most marginal $\\Kempirical{=}2$ assignments, with 1v2 CI lower bounds within 0.3 percentage points of $\\theta$.\n(5)~\\emph{Feature set}: the 15D features yield a feature-set-specific lower bound ($\\Ktheory$ may be strictly higher); neural probe $\\Kempirical$ is model-dependent ($3$ for Qwen, $2$ for Pythia/OLMo).\n(6)~\\emph{Segment length}: $\\Kempirical{=}2$ confirmed for 128 and 256 tokens (CI lower $> \\theta$); 512 tokens yields point estimate $\\Kempirical{=}2$ but CI lower marginally below $\\theta$ ($0.5979$); the boundary weakens at longer generation lengths.\n(7)~\\emph{Curation applicability}: the filtering evaluation is validated on two architectures (Qwen2.5-1.5B-Instruct and Pythia-1.4B) with consistent strategy ordering (Appendix~\\ref{sec:pythia_filtering}), though absolute improvement remains small and effect sizes diminish at lower contamination ratios (10--50\\%; Appendix~\\ref{sec:dose_response}).\n(8)~\\emph{Family balance}: the Qwen2.5 family provides 5/9 configurations; though spanning three scales (1.5B, 7B, 14B) and two training variants (base, instruct), aggregate statistics weight this family more heavily than the four single-configuration families.\nAdditional limitations (cross-model scoring sensitivity, feature ranking variability at the 1v2 boundary, structural composition confound analysis) appear in Appendix~\\ref{sec:extended_limitations}.\n\n% === Ethics Statement (ACL required, unnumbered) ===\n\\section*{Ethics Statement}\n\nGenerational depth estimation is intended for data curation and corpus auditing, positive-sum applications that improve training data quality.\nOur experiments use publicly available corpora (C4, Wikipedia, arXiv abstracts) and do not involve personally identifiable information.\nA potential dual-use concern is that depth estimation techniques could inform adversarial strategies to evade detection (e.g., by calibrating rewriting to mimic earlier-generation statistics); we note that this risk is shared by all detection research and that the binary detection boundary ($\\auc \\geq 0.96$ at 0v1) remains robust.\nCode and generated corpora will be released upon acceptance to enable reproducibility.\n\n\\bibliography{references}\n\n\\input{appendix}\n\\input{appendix_extended}\n\n\\end{document}\n",
      "numLines": 96,
      "startLine": 1,
      "totalLines": 96
    }
  },
  "sourceToolAssistantUUID": "8ca77a69-59af-4a00-b8a9-b53c34ac152a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool result

_source line 173 · 2026-05-19T13:05:19.692Z_

<details><summary>↩ Tool result · `toolu_01775eNpWW5jomHzQGFGdraA`</summary>

```text
1	\section{$\Kempirical$-Consistent Filtering}
2	\label{sec:filtering}
3	
4	$\Kempirical{=}2$ predicts that binary curation should suffice for web text; we test this as a consistency check using prompt-chain documents (Qwen2.5-1.5B-Instruct, proof of concept).
5	We compare six strategies on 30{,}000 documents (depths 0--5): no-filter, binary-ours (15D LightGBM), binary-Drayson~\citep{drayson2025}, graduated ($w = \exp(-\alpha \hat{d})$, $\alpha \in \{0.1,\ldots,0.9\}$), surprisal, and DSIR~\citep{xie2023dsir}, fine-tuning via LoRA on MMLU and HellaSwag across 5 seeds (51 runs; 100\% synthetic upper bound~\cite{shumailov2024collapse, dohmatob2024model}).
6	
7	\begin{table}[t]
8	\centering
9	\small
10	\caption{Filtering performance (mean $\pm$ std, 5 seeds). Full $\alpha$ sweep in Appendix~\ref{sec:extended_limitations}.}
11	\label{tab:tab_filtering_main}
12	\resizebox{\columnwidth}{!}{\input{tables/tab_filtering_main}}
13	\end{table}
14	
15	Binary-ours reduces MMLU degradation from $-$1.53\,pp (no-filter) to $-$0.77\,pp ($p_{\text{corr}} < 0.05$; Table~\ref{tab:tab_filtering_main}); the modest absolute improvement reflects the constrained dynamic range of a fully synthetic setting.
16	The strategy ordering is consistent with $\Kempirical{=}2$: binary exploits the one reliable boundary (0v1), while graduated strategies weight depths 2--5 using near-random classifier outputs, injecting noise; at $\alpha{=}0.9$, graduated matches binary on HellaSwag but remains worse on MMLU ($p_{\text{corr}} = 0.011$).
17	Cross-model replication on Pythia-1.4B confirms binary $>$ graduated (Appendix~\ref{sec:pythia_filtering}); graduated weighting is indistinguishable from no-filter at all contamination ratios (10--50\%; Appendix~\ref{sec:dose_response}).
18	On arXiv ($\Kempirical{=}3$), graduated filtering similarly fails: the statistical features separating depths 2 and 3 do not produce differential downstream training signal, so $\Kempirical$ accurately measures discriminability but overestimates filtering utility (Appendix~\ref{sec:extended_limitations}).
19	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "86a6e627-38c8-48f1-9083-5019e1d5567e",
  "isSidechain": false,
  "promptId": "12172553-d9aa-40c5-a42d-a4d4469a539a",
  "type": "user",
  "uuid": "8f61558a-2de6-4a81-a240-3a7721a24000",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c3.tex",
      "content": "\\section{$\\Kempirical$-Consistent Filtering}\n\\label{sec:filtering}\n\n$\\Kempirical{=}2$ predicts that binary curation should suffice for web text; we test this as a consistency check using prompt-chain documents (Qwen2.5-1.5B-Instruct, proof of concept).\nWe compare six strategies on 30{,}000 documents (depths 0--5): no-filter, binary-ours (15D LightGBM), binary-Drayson~\\citep{drayson2025}, graduated ($w = \\exp(-\\alpha \\hat{d})$, $\\alpha \\in \\{0.1,\\ldots,0.9\\}$), surprisal, and DSIR~\\citep{xie2023dsir}, fine-tuning via LoRA on MMLU and HellaSwag across 5 seeds (51 runs; 100\\% synthetic upper bound~\\cite{shumailov2024collapse, dohmatob2024model}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Filtering performance (mean $\\pm$ std, 5 seeds). Full $\\alpha$ sweep in Appendix~\\ref{sec:extended_limitations}.}\n\\label{tab:tab_filtering_main}\n\\resizebox{\\columnwidth}{!}{\\input{tables/tab_filtering_main}}\n\\end{table}\n\nBinary-ours reduces MMLU degradation from $-$1.53\\,pp (no-filter) to $-$0.77\\,pp ($p_{\\text{corr}} < 0.05$; Table~\\ref{tab:tab_filtering_main}); the modest absolute improvement reflects the constrained dynamic range of a fully synthetic setting.\nThe strategy ordering is consistent with $\\Kempirical{=}2$: binary exploits the one reliable boundary (0v1), while graduated strategies weight depths 2--5 using near-random classifier outputs, injecting noise; at $\\alpha{=}0.9$, graduated matches binary on HellaSwag but remains worse on MMLU ($p_{\\text{corr}} = 0.011$).\nCross-model replication on Pythia-1.4B confirms binary $>$ graduated (Appendix~\\ref{sec:pythia_filtering}); graduated weighting is indistinguishable from no-filter at all contamination ratios (10--50\\%; Appendix~\\ref{sec:dose_response}).\nOn arXiv ($\\Kempirical{=}3$), graduated filtering similarly fails: the statistical features separating depths 2 and 3 do not produce differential downstream training signal, so $\\Kempirical$ accurately measures discriminability but overestimates filtering utility (Appendix~\\ref{sec:extended_limitations}).\n",
      "numLines": 19,
      "startLine": 1,
      "totalLines": 19
    }
  },
  "sourceToolAssistantUUID": "86a6e627-38c8-48f1-9083-5019e1d5567e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 174 · 2026-05-19T13:05:17.457Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UiB1Pu2qT8UtijPBuPXQzq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7a178695-e5d7-4e50-b9f0-c38ad2330bca",
  "isSidechain": false,
  "requestId": "req_011CbByZGQtZEGUDeiPCaKvC",
  "type": "assistant",
  "uuid": "0a2f7473-c341-430a-b37f-e5a915a1488c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R5aasAvdxKFuGzJ54fMWnH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 129871,
      "cache_read_input_tokens": 11841,
      "output_tokens": 479,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 129871,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 479,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 129871,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 129871
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---


### Tool result

_source line 175 · 2026-05-19T13:05:17.462Z_

<details><summary>↩ Tool result · `toolu_01UiB1Pu2qT8UtijPBuPXQzq`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Web-scale text corpora are increasingly contaminated by synthetic content that has itself been generated from earlier synthetic content.
5	Estimates suggest that a substantial fraction of online text is machine-generated~\cite{sun2025aigt, spennemann2025quantifying}, and this share continues to rise.
6	When models train on the outputs of earlier models, the resulting multi-generational synthetic text degrades with each iteration: tail modes vanish, lexical diversity contracts, and surprisal distributions flatten~\cite{shumailov2024collapse, dohmatob2024model}.
7	This degradation arises in both \emph{retrain-chains} (iteratively training on model outputs) and \emph{prompt-chains} (recursively generating from previous outputs without retraining); we study the latter, which isolates generation-level information loss from training dynamics (Appendix~\ref{sec:extended_limitations}).
8	Yet the dominant paradigm treats all machine-generated text identically and ignores the generational depth dimension.
9	
10	This gap cuts across multiple communities.
11	Binary detectors~\cite{basani2026diveye, zhang2024minkpp} produce no depth estimate (Section~\ref{sec:binary_confidence}).
12	Membership inference~\cite{zawalski2026codec} addresses a different question, and the model collapse literature~\cite{shumailov2024collapse, alemohammad2024selfconsuming, schaeffer2025position} provides no per-text tool.
13	Data selection methods~\cite{xie2023dsir, tirumala2023d4, drayson2025} likewise ignore recursive depth.
14	No existing method estimates how many rounds of recursive generation a text has undergone.
15	
16	Knowing whether the discriminable depth is finite, and where it saturates, has direct practical consequences.
17	For data curation, the saturation point determines filtering granularity: if discrimination collapses at depth 2, graduated weighting beyond that boundary injects noise, and binary filtering becomes the principled choice.
18	Model collapse theory predicts monotonic quality degradation across generations, but existing analyses are population-level and provide no per-text measure of where degradation saturates.
19	$\Kempirical$ fills this gap by localizing the generation at which adjacent outputs become empirically indistinguishable.
20	
21	The Data Processing Inequality implies that information degrades monotonically across generations, motivating a finite discrimination boundary $\Kstar$; its actual value is determined empirically.
22	We empirically measure $\Kempirical$ (the maximum depth at which a classifier reliably distinguishes adjacent generations) using 15 statistical features computed via a fixed reference scorer (Section~\ref{sec:features}) and an Ordinal Binary Decomposition (OBD) LightGBM classifier.
23	We operationalize $\Kempirical$ as the deepest $k \geq 1$ where the pairwise $\auc_{k-1,k}$ exceeds $\theta = 0.60$ (Section~\ref{sec:formulation}).
24	
25	Our contributions:
26	\begin{enumerate}[label=(\alph*),nosep]
27	  \item \textbf{First empirical measurement of $\Kempirical$} across 9 model configurations (5 architecture families, 1B--14B), 4 source domains (3 text + 1 code), and 4 decoding strategies at $\theta{=}0.60$: 4/5 families (8/9 configurations) yield $\Kempirical{=}2$ on C4 ($p \leq 0.002$; Section~\ref{sec:kstar_boundary}).
28	  Both supervised OBD and zero-shot frontier Large Language Models (LLMs) show no statistically significant difference beyond $\Kempirical$ (McNemar $p > 0.05$, $N{=}500$; Section~\ref{sec:why_kstar}).
29	  \item \textbf{Domain ordering}: arXiv ($\Kempirical{=}3$) $>$ C4 ($\Kempirical{=}2$) $\geq$ Code ($\Kempirical{=}1$--$2$) $\geq$ Wikipedia ($\Kempirical{=}1$) holds across tested configurations; code (Python) approximates web text depth despite a different modality, with model-dependent variation at the boundary (Section~\ref{sec:cross_domain}).
30	  \item \textbf{Practical validation}: largely generator-independent features enable 80--92\% accuracy retention among tested continuation-mode configurations ($\rho > 0.90$; Section~\ref{sec:transfer}); as a consistency check, $\Kempirical{=}2$ correctly predicts binary $>$ graduated filtering for web text (Section~\ref{sec:filtering}).
31	\end{enumerate}
32	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0a2f7473-c341-430a-b37f-e5a915a1488c",
  "isSidechain": false,
  "promptId": "12172553-d9aa-40c5-a42d-a4d4469a539a",
  "type": "user",
  "uuid": "218c7883-6146-4736-b037-8151eb4850e3",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nWeb-scale text corpora are increasingly contaminated by synthetic content that has itself been generated from earlier synthetic content.\nEstimates suggest that a substantial fraction of online text is machine-generated~\\cite{sun2025aigt, spennemann2025quantifying}, and this share continues to rise.\nWhen models train on the outputs of earlier models, the resulting multi-generational synthetic text degrades with each iteration: tail modes vanish, lexical diversity contracts, and surprisal distributions flatten~\\cite{shumailov2024collapse, dohmatob2024model}.\nThis degradation arises in both \\emph{retrain-chains} (iteratively training on model outputs) and \\emph{prompt-chains} (recursively generating from previous outputs without retraining); we study the latter, which isolates generation-level information loss from training dynamics (Appendix~\\ref{sec:extended_limitations}).\nYet the dominant paradigm treats all machine-generated text identically and ignores the generational depth dimension.\n\nThis gap cuts across multiple communities.\nBinary detectors~\\cite{basani2026diveye, zhang2024minkpp} produce no depth estimate (Section~\\ref{sec:binary_confidence}).\nMembership inference~\\cite{zawalski2026codec} addresses a different question, and the model collapse literature~\\cite{shumailov2024collapse, alemohammad2024selfconsuming, schaeffer2025position} provides no per-text tool.\nData selection methods~\\cite{xie2023dsir, tirumala2023d4, drayson2025} likewise ignore recursive depth.\nNo existing method estimates how many rounds of recursive generation a text has undergone.\n\nKnowing whether the discriminable depth is finite, and where it saturates, has direct practical consequences.\nFor data curation, the saturation point determines filtering granularity: if discrimination collapses at depth 2, graduated weighting beyond that boundary injects noise, and binary filtering becomes the principled choice.\nModel collapse theory predicts monotonic quality degradation across generations, but existing analyses are population-level and provide no per-text measure of where degradation saturates.\n$\\Kempirical$ fills this gap by localizing the generation at which adjacent outputs become empirically indistinguishable.\n\nThe Data Processing Inequality implies that information degrades monotonically across generations, motivating a finite discrimination boundary $\\Kstar$; its actual value is determined empirically.\nWe empirically measure $\\Kempirical$ (the maximum depth at which a classifier reliably distinguishes adjacent generations) using 15 statistical features computed via a fixed reference scorer (Section~\\ref{sec:features}) and an Ordinal Binary Decomposition (OBD) LightGBM classifier.\nWe operationalize $\\Kempirical$ as the deepest $k \\geq 1$ where the pairwise $\\auc_{k-1,k}$ exceeds $\\theta = 0.60$ (Section~\\ref{sec:formulation}).\n\nOur contributions:\n\\begin{enumerate}[label=(\\alph*),nosep]\n  \\item \\textbf{First empirical measurement of $\\Kempirical$} across 9 model configurations (5 architecture families, 1B--14B), 4 source domains (3 text + 1 code), and 4 decoding strategies at $\\theta{=}0.60$: 4/5 families (8/9 configurations) yield $\\Kempirical{=}2$ on C4 ($p \\leq 0.002$; Section~\\ref{sec:kstar_boundary}).\n  Both supervised OBD and zero-shot frontier Large Language Models (LLMs) show no statistically significant difference beyond $\\Kempirical$ (McNemar $p > 0.05$, $N{=}500$; Section~\\ref{sec:why_kstar}).\n  \\item \\textbf{Domain ordering}: arXiv ($\\Kempirical{=}3$) $>$ C4 ($\\Kempirical{=}2$) $\\geq$ Code ($\\Kempirical{=}1$--$2$) $\\geq$ Wikipedia ($\\Kempirical{=}1$) holds across tested configurations; code (Python) approximates web text depth despite a different modality, with model-dependent variation at the boundary (Section~\\ref{sec:cross_domain}).\n  \\item \\textbf{Practical validation}: largely generator-independent features enable 80--92\\% accuracy retention among tested continuation-mode configurations ($\\rho > 0.90$; Section~\\ref{sec:transfer}); as a consistency check, $\\Kempirical{=}2$ correctly predicts binary $>$ graduated filtering for web text (Section~\\ref{sec:filtering}).\n\\end{enumerate}\n",
      "numLines": 32,
      "startLine": 1,
      "totalLines": 32
    }
  },
  "sourceToolAssistantUUID": "0a2f7473-c341-430a-b37f-e5a915a1488c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 176 · 2026-05-19T13:05:17.931Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XLb4EUsroNphAUsWcRimy7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "218c7883-6146-4736-b037-8151eb4850e3",
  "isSidechain": false,
  "requestId": "req_011CbByZGQtZEGUDeiPCaKvC",
  "type": "assistant",
  "uuid": "c2dcba63-0794-4ac0-8aa9-e58bf7a16554",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R5aasAvdxKFuGzJ54fMWnH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 129871,
      "cache_read_input_tokens": 11841,
      "output_tokens": 479,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 129871,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 479,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 129871,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 129871
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---


### Tool result

_source line 177 · 2026-05-19T13:05:17.935Z_

<details><summary>↩ Tool result · `toolu_01XLb4EUsroNphAUsWcRimy7`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Model collapse and recursive degradation.}
5	Iterative training on model outputs causes tail-distribution degradation~\cite{shumailov2024collapse, alemohammad2024selfconsuming, dohmatob2024model, dohmatob2025strong}, diversity contraction~\cite{guo2024curious, padmakumar2024writing, briesch2023selfconsuming}, and predictable convergence~\cite{bertrand2024stability, schaeffer2025position, kazdan2025collapse, gerstgrasser2024model, shi2025collapse}.
6	\citet{gambetta2024surplexity} propose surplexity, a single surprisal-based collapse indicator; our 15-dimensional feature set captures richer distributional structure and enables cross-model transfer.
7	\citet{amin2025escaping} show that weak-data curation can mitigate collapse, connecting to our filtering evaluation (Section~\ref{sec:filtering}).
8	Our prompt-chain operates in the replace regime~\cite{kazdan2025collapse}; $\Kempirical = 2$ is therefore a conservative lower bound.
9	This literature establishes convergence but provides no per-text depth measurement, does not predict domain dependence of saturation (Wikipedia depth 1 vs.\ arXiv depth 3), and does not characterize the prompt-chain vs.\ retrain-chain gap ($\Kempirical{=}2$ vs.\ $7$).
10	
11	\paragraph{Beyond binary detection.}
12	Binary detectors~\cite{gehrmann2019gltr, mitchell2023detectgpt, bao2024fast, yang2024dnagpt, hans2024binoculars, verma2024ghostbuster, basani2026diveye, zhang2024minkpp} achieve strong human-vs.-machine separation but produce no depth estimate; surveys~\cite{wu2023survey, tang2024science} consolidate this landscape but frame detection as binary.
13	Recent work extends beyond binary labels to collaboration degree~\cite{cheng2025beyond}, contamination hierarchies~\cite{mehta2025beyond}, and multigenerator benchmarks~\cite{wang2024semeval}; robustness concerns arise under paraphrasing~\cite{sadasivan2023detect, krishna2023paraphrasing} and cross-mode transfer~\cite{hao2025rewrite}; CoDeC~\cite{zawalski2026codec} addresses contamination via membership inference.
14	None estimates recursive generation depth.
15	Watermarking~\cite{kirchenbauer2023watermark} embeds detectable signals at generation time but does not apply to text already in the wild.
16	
17	\paragraph{Data selection and curation.}
18	DSIR~\cite{xie2023dsir}, D4~\cite{tirumala2023d4}, DoReMi~\cite{xie2023doremi}, and FineWeb~\cite{penedo2024fineweb} address corpus quality for large web corpora such as C4~\cite{raffel2020t5} through domain-aware filtering and deduplication but are depth-agnostic; Drayson et al.~\cite{drayson2025} combined binary detection with importance resampling, a special case when $\Kstar = 1$.
19	\citet{oren2024proving} address contamination detection in pre-training data; our method extends this to depth-granular resolution.
20	
21	\paragraph{Ordinal classification and probing.}
22	Our surprisal features build on information-theoretic processing cost~\cite{hale2001surprisal, levy2008expectation}, repurposed to track generational degradation.
23	Our OBD classifier follows Frank \& Hall's~\cite{frank2001ordinal} binary decomposition; CORAL~\cite{cao2020coral} provides a rank-consistent neural alternative.
24	Our neural probe extends probing~\cite{alain2017understanding, belinkov2022probing} to the discrimination boundary.
25	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c2dcba63-0794-4ac0-8aa9-e58bf7a16554",
  "isSidechain": false,
  "promptId": "12172553-d9aa-40c5-a42d-a4d4469a539a",
  "type": "user",
  "uuid": "afcd03db-73a1-44b4-a074-4274c701103d",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\paragraph{Model collapse and recursive degradation.}\nIterative training on model outputs causes tail-distribution degradation~\\cite{shumailov2024collapse, alemohammad2024selfconsuming, dohmatob2024model, dohmatob2025strong}, diversity contraction~\\cite{guo2024curious, padmakumar2024writing, briesch2023selfconsuming}, and predictable convergence~\\cite{bertrand2024stability, schaeffer2025position, kazdan2025collapse, gerstgrasser2024model, shi2025collapse}.\n\\citet{gambetta2024surplexity} propose surplexity, a single surprisal-based collapse indicator; our 15-dimensional feature set captures richer distributional structure and enables cross-model transfer.\n\\citet{amin2025escaping} show that weak-data curation can mitigate collapse, connecting to our filtering evaluation (Section~\\ref{sec:filtering}).\nOur prompt-chain operates in the replace regime~\\cite{kazdan2025collapse}; $\\Kempirical = 2$ is therefore a conservative lower bound.\nThis literature establishes convergence but provides no per-text depth measurement, does not predict domain dependence of saturation (Wikipedia depth 1 vs.\\ arXiv depth 3), and does not characterize the prompt-chain vs.\\ retrain-chain gap ($\\Kempirical{=}2$ vs.\\ $7$).\n\n\\paragraph{Beyond binary detection.}\nBinary detectors~\\cite{gehrmann2019gltr, mitchell2023detectgpt, bao2024fast, yang2024dnagpt, hans2024binoculars, verma2024ghostbuster, basani2026diveye, zhang2024minkpp} achieve strong human-vs.-machine separation but produce no depth estimate; surveys~\\cite{wu2023survey, tang2024science} consolidate this landscape but frame detection as binary.\nRecent work extends beyond binary labels to collaboration degree~\\cite{cheng2025beyond}, contamination hierarchies~\\cite{mehta2025beyond}, and multigenerator benchmarks~\\cite{wang2024semeval}; robustness concerns arise under paraphrasing~\\cite{sadasivan2023detect, krishna2023paraphrasing} and cross-mode transfer~\\cite{hao2025rewrite}; CoDeC~\\cite{zawalski2026codec} addresses contamination via membership inference.\nNone estimates recursive generation depth.\nWatermarking~\\cite{kirchenbauer2023watermark} embeds detectable signals at generation time but does not apply to text already in the wild.\n\n\\paragraph{Data selection and curation.}\nDSIR~\\cite{xie2023dsir}, D4~\\cite{tirumala2023d4}, DoReMi~\\cite{xie2023doremi}, and FineWeb~\\cite{penedo2024fineweb} address corpus quality for large web corpora such as C4~\\cite{raffel2020t5} through domain-aware filtering and deduplication but are depth-agnostic; Drayson et al.~\\cite{drayson2025} combined binary detection with importance resampling, a special case when $\\Kstar = 1$.\n\\citet{oren2024proving} address contamination detection in pre-training data; our method extends this to depth-granular resolution.\n\n\\paragraph{Ordinal classification and probing.}\nOur surprisal features build on information-theoretic processing cost~\\cite{hale2001surprisal, levy2008expectation}, repurposed to track generational degradation.\nOur OBD classifier follows Frank \\& Hall's~\\cite{frank2001ordinal} binary decomposition; CORAL~\\cite{cao2020coral} provides a rank-consistent neural alternative.\nOur neural probe extends probing~\\cite{alain2017understanding, belinkov2022probing} to the discrimination boundary.\n",
      "numLines": 25,
      "startLine": 1,
      "totalLines": 25
    }
  },
  "sourceToolAssistantUUID": "c2dcba63-0794-4ac0-8aa9-e58bf7a16554",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 178 · 2026-05-19T13:05:18.874Z_

<details open><summary>🔧 Tool call — Read · `toolu_01L5R2fVdSN73cWjHbHbhK57`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "afcd03db-73a1-44b4-a074-4274c701103d",
  "isSidechain": false,
  "requestId": "req_011CbByZGQtZEGUDeiPCaKvC",
  "type": "assistant",
  "uuid": "2b71e446-55cf-4aa2-ad79-1b468bcea3b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R5aasAvdxKFuGzJ54fMWnH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 129871,
      "cache_read_input_tokens": 11841,
      "output_tokens": 479,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 129871,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 479,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 129871,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 129871
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---


### Tool result

_source line 179 · 2026-05-19T13:05:18.879Z_

<details><summary>↩ Tool result · `toolu_01L5R2fVdSN73cWjHbHbhK57`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\begin{figure*}[t]
5	\centering
6	\includegraphics[width=\textwidth]{figures/pipeline.pdf}
7	\caption{Generational depth estimation pipeline. Seed documents are recursively passed through a generation operator $G_\delta$ to produce a depth chain. Statistical features are fed to the OBD-LightGBM classifier for depth prediction.}
8	\label{fig:pipeline}
9	\end{figure*}
10	
11	\subsection{Problem Formulation}
12	\label{sec:formulation}
13	
14	A generation operator $G_\delta$ (LLM + decoding strategy $\delta$) produces successive generations $X \to Y_1 \to \cdots \to Y_K$, where $Y_k = G_\delta(Y_{k-1})$ and $Y_0 \triangleq X$ (Figure~\ref{fig:pipeline}).
15	This sequence forms a Markov chain.
16	By the Data Processing Inequality, $I(X; Y_1) \geq I(X; Y_2) \geq \cdots \geq 0$: the original signal degrades monotonically.
17	Together with Markov chain convergence, this motivates a finite $\Ktheory$ beyond which adjacent generations become indistinguishable; DPI guarantees existence but does not bound $\Ktheory$, so the actual saturation depth must be measured empirically.
18	
19	We define the operational lower bound:
20	\begin{equation}
21	  \Kempirical = \max\{k \geq 1 : \mathrm{CI}_{\mathrm{low}}(\auc_{k-1,k}) > \theta\},
22	  \label{eq:kstar}
23	\end{equation}
24	where $\mathrm{CI}_{\mathrm{low}}(\auc_{k-1,k})$ is the lower bound of a 95\% bootstrap confidence interval (1{,}000 resamples\footnote{Boundary-pair results in Table~\ref{tab:kstar_ci} use 1{,}000 resamples; arXiv cross-scorer CIs (Table~\ref{tab:arxiv_crossscorer_ci}) use 10{,}000 for tighter bounds at the margin.}) over the pairwise AUC (Area Under the ROC Curve) between depths $k{-}1$ and $k$, and $\theta = 0.60$ is a post-hoc operational threshold (motivated below).
25	This criterion ensures that $\Kempirical$ reflects statistically robust discriminability rather than sampling noise.
26	$\Kempirical$ characterizes a discriminability regime at a given $\theta$; the domain ordering is stable across $\theta \in [0.575, 0.65]$ (Section~\ref{sec:kstar_boundary}).
27	We additionally verify that non-boundary-pair CI upper bounds fall below $\theta$ (Section~\ref{sec:kstar_boundary}).
28	
29	\paragraph{Threshold choice.}
30	We set $\theta{=}0.60$ as a post-hoc operational threshold, chosen at the empirical discontinuity in the AUC distribution (Figure~\ref{fig:kstar_theta}).
31	A 10{,}000-iteration permutation test yields a 95th-percentile null of ${<}\,0.55$ and $p < 0.002$ for all boundary comparisons, placing $\theta{=}0.60$ well above the empirical null.
32	$\Kempirical{=}2$ is stable across $\theta \in [0.55, 0.65]$ for all but two marginal configurations (Table~\ref{tab:kstar_ci_extended}): 1v2 AUC values cluster at $0.61$--$0.70$ while 2v3 values cluster at $0.55$--$0.59$, creating a ${\sim}$5--11\,pp discontinuity.
33	Only at extremes does $\Kempirical$ shift: $\theta{=}0.55$ yields $\Kempirical{=}3$ for two Qwen configurations; $\theta{=}0.70$ yields $\Kempirical{=}1$ across all configurations.
34	The downstream filtering evaluation (Section~\ref{sec:filtering}) uses the OBD classifier without re-optimizing $\theta$, avoiding circularity.
35	A leave-one-family-out (LOFO) cross-validation on C4 independently validates this choice: each of five folds derives $\hat{\theta}$ from the gap midpoint between $\min(\auc_{1v2})$ and $\max(\auc_{2v3})$ over the remaining families, yielding $\hat{\theta} \in [0.5725, 0.6004]$; $\theta{=}0.60$ falls within this range, and 8/9 held-out predictions match the original $\Kempirical$ (the single mismatch is the borderline rewrite-mode configuration; Table~\ref{tab:theta_lofo}).
36	ArXiv corroborates with 6/6 LOFO agreement; Wikipedia is underdetermined because most models produce near-chance 1v2 AUC, invalidating the gap-based derivation (Appendix~\ref{sec:theta_lofo}).
37	
38	
39	\subsection{Features and Classifier}
40	\label{sec:features}
41	
42	Each document is characterized by a 15-dimensional feature vector spanning four groups: \emph{surprisal moments} (mean, std, skewness, kurtosis; 4~dims), \emph{surprisal derivatives} (mean and std of first- and second-order differences, plus first-order skewness; 5~dims), \emph{vocabulary diversity} (type-token ratio, hapax legomena ratio, self-BLEU; 3~dims), and \emph{frequency tail statistics} (frequency kurtosis, entropy, rare token fraction; 3~dims).
43	All features are computed from token-level surprisal values via an external scorer model (full definitions in Table~\ref{tab:s5_features}, Appendix).
44	Self-BLEU is computed within each CV fold using only same-fold, same-depth reference samples to prevent leakage; it ranks \#1 in 1/8 conditions (greedy decoding) but is absent from the top-3 in all 7 others.
45	Removing self-BLEU reduces mean $\auc_{1v2}$ by $< 1$\,pp across all models (14D $\Kempirical = 2$ for all 4 configurations; bootstrap CIs in Table~\ref{tab:selfbleu_ablation}); in deployment where depth labels are unavailable, self-BLEU can be replaced with corpus-level self-similarity or omitted with minimal performance loss.
46	Hand-crafted features enable cross-generator transfer without retraining and permit attribution of discriminative power to specific text properties.
47	
48	We use \emph{Ordinal Binary Decomposition} (OBD), decomposing the $(K{+}1)$-class problem into $K$ cumulative binary sub-classifiers, each estimating $P(\text{depth} > k \mid \mathbf{x})$ via LightGBM~\cite{ke2017lightgbm} (hyperparameters in Table~\ref{tab:s6_lgbm_params}).
49	OBD achieves lower MAE than multiclass LightGBM (e.g., 0.984 vs.\ 1.016 on Qwen-rewrite) while maintaining superior pairwise $\auc$ (mean 0.6095 vs.\ 0.4883 for ordinal logistic regression).
50	
51	\subsection{Experimental Setup}
52	\label{sec:experimental_setup}
53	
54	We evaluate nine configurations spanning five architecture families (Table~\ref{tab:setup}): Qwen2.5-1.5B-Instruct (rewrite and continuation modes), Qwen2.5-1.5B (base, continuation), Qwen2.5-7B, Qwen2.5-14B, Pythia-1.4B, OLMo-1B, LLaMA-3.1-8B, and Mistral-7B (all continuation except Qwen-rw).
55	Each uses 5{,}000 C4~\cite{raffel2020t5} seeds truncated to 256 tokens, recursively generated for $K{=}5$ iterations (30{,}000 documents per configuration).
56	Default decoding: nucleus $p{=}0.95$, $T{=}1.0$; decoding ablation covers greedy, $T{=}0.7$, and $T{=}1.2$.
57	Continuation mode truncates seeds to 128 tokens and extends to 256; rewrite mode paraphrases the full text.
58	Evaluation: 5-fold GroupKFold cross-validation grouped by seed document; pairwise $\auc$ as primary metric.
59	
60	\begin{table}[t]
61	\centering
62	\small
63	\caption{Experimental configurations for depth-chain generation. \textbf{Config}: shorthand identifier; \textbf{Model}: architecture and parameter count; \textbf{Mode}: generation strategy (continuation or rewrite); $N$: number of seed documents per depth level.}
64	\label{tab:setup}
65	\resizebox{\columnwidth}{!}{%
66	\begin{tabular}{llcc}
67	\toprule
68	\textbf{Config} & \textbf{Model} & \textbf{Mode} & $N$ \\
69	\midrule
70	Qwen-rw   & Qwen2.5-1.5B-Instruct & Rewrite & 5{,}000 \\
71	Qwen-cont & Qwen2.5-1.5B-Instruct & Continuation & 5{,}000 \\
72	Qwen-base & Qwen2.5-1.5B          & Continuation & 5{,}000 \\
73	Pythia    & Pythia-1.4B            & Continuation & 5{,}000 \\
74	OLMo      & OLMo-1B               & Continuation & 5{,}000 \\
75	Qwen-7B   & Qwen2.5-7B            & Continuation & 5{,}000 \\
76	Qwen-14B  & Qwen2.5-14B           & Continuation & 5{,}000 \\
77	LLaMA-8B  & LLaMA-3.1-8B          & Continuation & 5{,}000 \\
78	Mistral   & Mistral-7B            & Continuation & 5{,}000 \\
79	\bottomrule
80	\end{tabular}}
81	\end{table}
82	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2b71e446-55cf-4aa2-ad79-1b468bcea3b1",
  "isSidechain": false,
  "promptId": "12172553-d9aa-40c5-a42d-a4d4469a539a",
  "type": "user",
  "uuid": "2e2175e5-99d2-4524-89d8-75929df2674d",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/pipeline.pdf}\n\\caption{Generational depth estimation pipeline. Seed documents are recursively passed through a generation operator $G_\\delta$ to produce a depth chain. Statistical features are fed to the OBD-LightGBM classifier for depth prediction.}\n\\label{fig:pipeline}\n\\end{figure*}\n\n\\subsection{Problem Formulation}\n\\label{sec:formulation}\n\nA generation operator $G_\\delta$ (LLM + decoding strategy $\\delta$) produces successive generations $X \\to Y_1 \\to \\cdots \\to Y_K$, where $Y_k = G_\\delta(Y_{k-1})$ and $Y_0 \\triangleq X$ (Figure~\\ref{fig:pipeline}).\nThis sequence forms a Markov chain.\nBy the Data Processing Inequality, $I(X; Y_1) \\geq I(X; Y_2) \\geq \\cdots \\geq 0$: the original signal degrades monotonically.\nTogether with Markov chain convergence, this motivates a finite $\\Ktheory$ beyond which adjacent generations become indistinguishable; DPI guarantees existence but does not bound $\\Ktheory$, so the actual saturation depth must be measured empirically.\n\nWe define the operational lower bound:\n\\begin{equation}\n  \\Kempirical = \\max\\{k \\geq 1 : \\mathrm{CI}_{\\mathrm{low}}(\\auc_{k-1,k}) > \\theta\\},\n  \\label{eq:kstar}\n\\end{equation}\nwhere $\\mathrm{CI}_{\\mathrm{low}}(\\auc_{k-1,k})$ is the lower bound of a 95\\% bootstrap confidence interval (1{,}000 resamples\\footnote{Boundary-pair results in Table~\\ref{tab:kstar_ci} use 1{,}000 resamples; arXiv cross-scorer CIs (Table~\\ref{tab:arxiv_crossscorer_ci}) use 10{,}000 for tighter bounds at the margin.}) over the pairwise AUC (Area Under the ROC Curve) between depths $k{-}1$ and $k$, and $\\theta = 0.60$ is a post-hoc operational threshold (motivated below).\nThis criterion ensures that $\\Kempirical$ reflects statistically robust discriminability rather than sampling noise.\n$\\Kempirical$ characterizes a discriminability regime at a given $\\theta$; the domain ordering is stable across $\\theta \\in [0.575, 0.65]$ (Section~\\ref{sec:kstar_boundary}).\nWe additionally verify that non-boundary-pair CI upper bounds fall below $\\theta$ (Section~\\ref{sec:kstar_boundary}).\n\n\\paragraph{Threshold choice.}\nWe set $\\theta{=}0.60$ as a post-hoc operational threshold, chosen at the empirical discontinuity in the AUC distribution (Figure~\\ref{fig:kstar_theta}).\nA 10{,}000-iteration permutation test yields a 95th-percentile null of ${<}\\,0.55$ and $p < 0.002$ for all boundary comparisons, placing $\\theta{=}0.60$ well above the empirical null.\n$\\Kempirical{=}2$ is stable across $\\theta \\in [0.55, 0.65]$ for all but two marginal configurations (Table~\\ref{tab:kstar_ci_extended}): 1v2 AUC values cluster at $0.61$--$0.70$ while 2v3 values cluster at $0.55$--$0.59$, creating a ${\\sim}$5--11\\,pp discontinuity.\nOnly at extremes does $\\Kempirical$ shift: $\\theta{=}0.55$ yields $\\Kempirical{=}3$ for two Qwen configurations; $\\theta{=}0.70$ yields $\\Kempirical{=}1$ across all configurations.\nThe downstream filtering evaluation (Section~\\ref{sec:filtering}) uses the OBD classifier without re-optimizing $\\theta$, avoiding circularity.\nA leave-one-family-out (LOFO) cross-validation on C4 independently validates this choice: each of five folds derives $\\hat{\\theta}$ from the gap midpoint between $\\min(\\auc_{1v2})$ and $\\max(\\auc_{2v3})$ over the remaining families, yielding $\\hat{\\theta} \\in [0.5725, 0.6004]$; $\\theta{=}0.60$ falls within this range, and 8/9 held-out predictions match the original $\\Kempirical$ (the single mismatch is the borderline rewrite-mode configuration; Table~\\ref{tab:theta_lofo}).\nArXiv corroborates with 6/6 LOFO agreement; Wikipedia is underdetermined because most models produce near-chance 1v2 AUC, invalidating the gap-based derivation (Appendix~\\ref{sec:theta_lofo}).\n\n\n\\subsection{Features and Classifier}\n\\label{sec:features}\n\nEach document is characterized by a 15-dimensional feature vector spanning four groups: \\emph{surprisal moments} (mean, std, skewness, kurtosis; 4~dims), \\emph{surprisal derivatives} (mean and std of first- and second-order differences, plus first-order skewness; 5~dims), \\emph{vocabulary diversity} (type-token ratio, hapax legomena ratio, self-BLEU; 3~dims), and \\emph{frequency tail statistics} (frequency kurtosis, entropy, rare token fraction; 3~dims).\nAll features are computed from token-level surprisal values via an external scorer model (full definitions in Table~\\ref{tab:s5_features}, Appendix).\nSelf-BLEU is computed within each CV fold using only same-fold, same-depth reference samples to prevent leakage; it ranks \\#1 in 1/8 conditions (greedy decoding) but is absent from the top-3 in all 7 others.\nRemoving self-BLEU reduces mean $\\auc_{1v2}$ by $< 1$\\,pp across all models (14D $\\Kempirical = 2$ for all 4 configurations; bootstrap CIs in Table~\\ref{tab:selfbleu_ablation}); in deployment where depth labels are unavailable, self-BLEU can be replaced with corpus-level self-similarity or omitted with minimal performance loss.\nHand-crafted features enable cross-generator transfer without retraining and permit attribution of discriminative power to specific text properties.\n\nWe use \\emph{Ordinal Binary Decomposition} (OBD), decomposing the $(K{+}1)$-class problem into $K$ cumulative binary sub-classifiers, each estimating $P(\\text{depth} > k \\mid \\mathbf{x})$ via LightGBM~\\cite{ke2017lightgbm} (hyperparameters in Table~\\ref{tab:s6_lgbm_params}).\nOBD achieves lower MAE than multiclass LightGBM (e.g., 0.984 vs.\\ 1.016 on Qwen-rewrite) while maintaining superior pairwise $\\auc$ (mean 0.6095 vs.\\ 0.4883 for ordinal logistic regression).\n\n\\subsection{Experimental Setup}\n\\label{sec:experimental_setup}\n\nWe evaluate nine configurations spanning five architecture families (Table~\\ref{tab:setup}): Qwen2.5-1.5B-Instruct (rewrite and continuation modes), Qwen2.5-1.5B (base, continuation), Qwen2.5-7B, Qwen2.5-14B, Pythia-1.4B, OLMo-1B, LLaMA-3.1-8B, and Mistral-7B (all continuation except Qwen-rw).\nEach uses 5{,}000 C4~\\cite{raffel2020t5} seeds truncated to 256 tokens, recursively generated for $K{=}5$ iterations (30{,}000 documents per configuration).\nDefault decoding: nucleus $p{=}0.95$, $T{=}1.0$; decoding ablation covers greedy, $T{=}0.7$, and $T{=}1.2$.\nContinuation mode truncates seeds to 128 tokens and extends to 256; rewrite mode paraphrases the full text.\nEvaluation: 5-fold GroupKFold cross-validation grouped by seed document; pairwise $\\auc$ as primary metric.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Experimental configurations for depth-chain generation. \\textbf{Config}: shorthand identifier; \\textbf{Model}: architecture and parameter count; \\textbf{Mode}: generation strategy (continuation or rewrite); $N$: number of seed documents per depth level.}\n\\label{tab:setup}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Config} & \\textbf{Model} & \\textbf{Mode} & $N$ \\\\\n\\midrule\nQwen-rw   & Qwen2.5-1.5B-Instruct & Rewrite & 5{,}000 \\\\\nQwen-cont & Qwen2.5-1.5B-Instruct & Continuation & 5{,}000 \\\\\nQwen-base & Qwen2.5-1.5B          & Continuation & 5{,}000 \\\\\nPythia    & Pythia-1.4B            & Continuation & 5{,}000 \\\\\nOLMo      & OLMo-1B               & Continuation & 5{,}000 \\\\\nQwen-7B   & Qwen2.5-7B            & Continuation & 5{,}000 \\\\\nQwen-14B  & Qwen2.5-14B           & Continuation & 5{,}000 \\\\\nLLaMA-8B  & LLaMA-3.1-8B          & Continuation & 5{,}000 \\\\\nMistral   & Mistral-7B            & Continuation & 5{,}000 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n",
      "numLines": 82,
      "startLine": 1,
      "totalLines": 82
    }
  },
  "sourceToolAssistantUUID": "2b71e446-55cf-4aa2-ad79-1b468bcea3b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 180 · 2026-05-19T13:05:19.337Z_

<details open><summary>🔧 Tool call — Read · `toolu_018T1BW4mUHJWAXzd2S9bp48`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e2175e5-99d2-4524-89d8-75929df2674d",
  "isSidechain": false,
  "requestId": "req_011CbByZGQtZEGUDeiPCaKvC",
  "type": "assistant",
  "uuid": "b14a8195-4cdb-464f-9351-298c742145c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R5aasAvdxKFuGzJ54fMWnH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 129871,
      "cache_read_input_tokens": 11841,
      "output_tokens": 479,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 129871,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 479,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 129871,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 129871
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---


### Tool result

_source line 181 · 2026-05-19T13:05:19.343Z_

<details><summary>↩ Tool result · `toolu_018T1BW4mUHJWAXzd2S9bp48`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate generational depth estimation on nine model configurations spanning five architecture families:
5	Pythia-1.4B, OLMo-1B, Qwen2.5-1.5B-Instruct (rewrite and continuation), Qwen2.5-1.5B (base), Qwen2.5-7B, Qwen2.5-14B, LLaMA-3.1-8B, and Mistral-7B, all in continuation mode except where noted.
6	All experiments use the OBD-LightGBM classifier with the 15-dimensional feature set (Section~\ref{sec:method}), with 5{,}000 texts per depth level (generations 0--5; power analysis in Appendix~\ref{sec:power_curve}).
7	
8	%% ====================================================================
9	\subsection{\texorpdfstring{$\Kempirical \leq 2$}{K*<=2} Across Model Configurations (C4)}
10	\label{sec:kstar_boundary}
11	
12	\begin{table*}[t]
13	\centering
14	\small
15	\caption{Pairwise $\auc$ for adjacent depth pairs with bootstrap 95\% CIs and permutation $p$-values for boundary rows.
16	$\Kempirical = 2$ requires 1v2 CI lower bound $> \theta{=}0.60$ and 2v3 CI lower bound $\leq \theta$ (Eq.~\ref{eq:kstar}).
17	Extended results (all models) in Table~\ref{tab:kstar_ci_extended}.}
18	\label{tab:kstar_ci}
19	\begin{tabular}{lcccccccccc}
20	\toprule
21	 & \multicolumn{2}{c}{Qwen-rw} & \multicolumn{2}{c}{Pythia} & \multicolumn{2}{c}{OLMo} & \multicolumn{2}{c}{Qwen-cont} & \multicolumn{2}{c}{Qwen-7B\rlap{$^\ddagger$}} \\
22	\cmidrule(lr){2-3}\cmidrule(lr){4-5}\cmidrule(lr){6-7}\cmidrule(lr){8-9}\cmidrule(lr){10-11}
23	 & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI \\
24	\midrule
25	0v1 & .9956 & & .9932 & & .9970 & & .9971 & & .9638 & [.961,\,.967] \\
26	1v2 & .6955 & [.686,\,.704]\rlap{$^*$} & .6539 & [.645,\,.663]\rlap{$^*$} & .6145 & [.605,\,.625]\rlap{$^*$} & .6112 & [.602,\,.621]\rlap{$^*$} & .6168 & [.608,\,.626]\rlap{$^*$} \\
27	2v3 & .5893 & [.580,\,.599] & .5514 & [.542,\,.563] & .5496 & [.540,\,.560] & .5609 & [.551,\,.571] & .5492 & [.539,\,.559] \\
28	3v4 & .5435 & & .5152 & & .5091 & & .5409 & & .5276 & \\
29	4v5 & .5340 & & .5136 & & .5045 & & .5141 & & .5085 & \\
30	\bottomrule
31	\multicolumn{11}{l}{\footnotesize $^*$Permutation $p < 0.001$ for all 1v2 comparisons shown.} \\
32	\multicolumn{11}{l}{\footnotesize $^\ddagger$Generator: Qwen2.5-7B (fp16); scorer: Qwen2.5-1.5B.}
33	\end{tabular}
34	\end{table*}
35	
36	\begin{figure}[t]
37	\centering
38	\includegraphics[width=\columnwidth]{figures/fig2_auc_decay.pdf}
39	\caption{Pairwise $\auc$ decay across depth pairs for model-mode configurations (solid) and decoding strategies (dashed). The horizontal dashed line marks $\theta = 0.60$.}
40	\label{fig:auc_decay}
41	\end{figure}
42	
43	Table~\ref{tab:kstar_ci} and Figure~\ref{fig:auc_decay} show $\Kempirical \leq 2$ across all 9 model configurations: 8/9 yield $\Kempirical{=}2$ (1v2 $\auc$ range: 0.6112--0.6955; all CI lower bounds $> \theta$; permutation $p < 0.001$), while Mistral-7B is the only exception ($\Kempirical{=}1$; 1v2 $\auc = 0.594$, below $\theta$; Section~\ref{sec:boundary_cases}).
44	LLaMA-3.1-8B yields $\Kempirical{=}2$ (0v1 $\auc = 0.9225$, 1v2 $\auc = 0.6123$, 95\% CI $[0.603, 0.622]$; borderline: 1/5 folds falls below $\theta$; Table~\ref{tab:kstar_ci_extended}).
45	Among non-Qwen families: Pythia and OLMo yield clear $\Kempirical{=}2$, LLaMA is borderline (CI lower $= 0.603$), and Mistral yields $\Kempirical{=}1$; the Qwen-heavy configuration space (5/9) does not alter this per-family pattern.
46	All four decoding strategies likewise yield $\Kempirical{=}2$ (Table~\ref{tab:s2_decoding}).
47	The 1v2 spread due to generation mode ($\Delta = 8.4$\,pp within Qwen) exceeds the spread across models in continuation mode ($\Delta = 3.9$\,pp).
48	
49	\paragraph{Scale and instruction-tuning invariance.}
50	$\Kempirical{=}2$ persists from 1.5B through 14B: Qwen-14B (1v2 $\auc = 0.621$ $[0.612, 0.630]$), Qwen-7B ($0.6168$ $[0.608, 0.626]$), and LLaMA-3.1-8B ($0.6123$) all exceed $\theta$, despite progressively reduced 0v1 signal (0.960 at 14B, 0.964 at 7B, 0.923 at 8B vs.\ $> 0.99$ at $\leq$1.5B).
51	A base-vs.-instruct ablation at 1.5B likewise yields $\Kempirical = 2$ (1v2 $\auc = 0.626$); the boundary is not an instruction-tuning artifact.
52	
53	\begin{figure}[t]
54	\centering
55	\includegraphics[width=\columnwidth]{figures/fig_kstar_theta.pdf}
56	\caption{$\Kempirical(\theta)$ sensitivity curve for six configurations. $\Kempirical$: maximum discriminable depth; $\theta$: AUC decision threshold. All configurations yield $\Kempirical{=}2$ at $\theta{=}0.60$ (dashed line). At $\theta{=}0.70$, all drop to $\Kempirical{=}1$.}
57	\label{fig:kstar_theta}
58	\end{figure}
59	
60	Figure~\ref{fig:kstar_theta} shows $\Kempirical$ as a function of $\theta$: web text $\Kempirical{=}2$ is stable across a 5\,pp window ($\theta \in [0.575, 0.625]$), with a gradual transition to $\Kempirical{=}3$ at $\theta{=}0.55$ (two Qwen configurations) and $\Kempirical{=}1$ at $\theta{=}0.70$.
61	The domain ordering (arXiv $>$ web $\geq$ cross-scorer) is preserved across the full $\theta$ range (Table~\ref{tab:theta_sensitivity}; Figure~\ref{fig:theta_sensitivity} in Appendix).
62	
63	%% ====================================================================
64	\subsection{Largely Generator-Independent Transfer}
65	\label{sec:transfer}
66	
67	\begin{figure}[t]
68	\centering
69	\includegraphics[width=0.85\columnwidth]{figures/fig3_transfer_heatmap.pdf}
70	\caption{Cross-model transfer heatmap. Each cell shows 6-class ordinal accuracy when trained on the row model and tested on the column model, divided by in-domain accuracy (retention rate). Pythia$\leftrightarrow$OLMo: 90--92\%; Qwen-rewrite$\to$continuation: 61--63\%.}
71	\label{fig:transfer_heatmap}
72	\end{figure}
73	
74	Continuation-mode classifiers transfer well across generators (Figure~\ref{fig:transfer_heatmap}; full matrix in Table~\ref{tab:s1_transfer}): Pythia$\leftrightarrow$OLMo retains 90--92\%, Qwen-cont$\leftrightarrow$Pythia 84--85\%, Qwen-cont$\leftrightarrow$OLMo 80--85\% (0v1 cross-model $\auc > 0.96$ for all pairs).
75	Qwen-rewrite classifiers transfer poorly (61--63\%), consistent with reliance on mode-specific artifacts rather than generalizable depth features.
76	
77	\paragraph{Cross-scorer validation.}
78	Replacing the self-scorer with Pythia-1.4B or OLMo-1B preserves feature rankings ($\rho > 0.90$; Table~\ref{tab:crossscorer}).
79	$\Kempirical$ is largely robust to scorer choice: across 22 cross-scorer configurations on C4 and arXiv, $\Kempirical$ was preserved in 20 cases; the two exceptions (Qwen-cont scored by Pythia on C4, Qwen-7B cross-scored on arXiv) are borderline, with AUC within 0.002 of $\theta$.
80	Qwen-cont is the most scorer-sensitive continuation-mode configuration: its self-scored 1v2 CI lower bound exceeds $\theta$ by only 0.2\,pp (Table~\ref{tab:kstar_ci}), and cross-family scoring pushes it below $\theta$.
81	For arXiv, Pythia-1.4B cross-scoring preserves $\Kempirical{=}3$ for 3/4 generators (2v3 $\auc$: 0.608--0.632); Qwen-7B drops to borderline $\Kempirical{=}2$ ($\Delta = -2.7$\,pp), consistent with Qwen scorer sensitivity on C4 and Wikipedia (Table~\ref{tab:arxiv_crossscorer_ci}).
82	A three-way ANOVA (Generator $\times$ Scorer $\times$ Depth-Pair; $N{=}300$; Table~\ref{tab:anova_crossscorer}) confirms that Depth-Pair dominates variance ($\eta^2_p = 0.998$); Scorer is statistically significant ($p < .001$) but practically minor ($\eta^2_p = 0.192$), consistent with a detectable but small scorer influence on absolute discriminability.
83	
84	%% ====================================================================
85	\subsection{Feature Ordering and Generation Mode}
86	\label{sec:feature_degradation}
87	\label{sec:generation_mode}
88	
89	Among continuation-mode models, single-feature $\auc$ rankings are highly correlated ($\rho \geq 0.85$; Table~\ref{tab:top_features}).
90	The top-3 features (\texttt{surp\_d1\_std}, \texttt{surp\_std}, \texttt{surp\_d2\_std}) are shared across all three families: autoregressive generation progressively damps surprisal variability; however, no single feature subset of size ${<}8$ reliably sustains $\Kempirical{=}2$ (Appendix~\ref{sec:feature_subset}).
91	A feature group ablation (Appendix~\ref{sec:feature_ablation}) confirms that surprisal (base) dominates on arXiv (single AUC $= 0.809$, LOO $\Delta = 0.031$); on C4 and Wikipedia, all LOO drops fall within fold variance ($\leq 0.007$).
92	Qwen-rewrite diverges (\texttt{freq\_entropy} dominates), consistent with its poor cross-model transfer (61--63\%).
93	Within Qwen, rewrite yields 1v2 $\auc = 0.6955$ vs.\ continuation's $0.6112$ ($\Delta = +8.4$\,pp); continuation mode is therefore recommended as the canonical condition.
94	
95	%% ====================================================================
96	\subsection{Neural Probe}
97	\label{sec:neural_probe}
98	
99	Replacing the 15D features with frozen encoder hidden states (MLP probe, 5{,}000 texts per depth; Table~\ref{tab:neural_probe_crossmodel}), Qwen achieves $\Kempirical^{\text{neural}} = 3$ (2v3 $\auc = 0.6159$), while Pythia and OLMo remain at $\Kempirical^{\text{neural}} = 2$ ($\auc_{2v3}$: 0.5963, 0.5892).
100	The Qwen-only elevation reflects self-familiarity artifacts that transfer poorly (Section~\ref{sec:transfer}); the 15D features yield consistent $\Kempirical = 2$ across all families.
101	
102	\noindent\begin{minipage}{\columnwidth}
103	\centering
104	\footnotesize
105	\captionof{table}{Neural probe pairwise AUC using frozen-encoder MLP. Each cell reports AUC for classifying depth $d$ vs.\ $d{+}1$ text. $\Kempirical^{\text{neural}}$: maximum depth where AUC exceeds $\theta = 0.60$.}
106	\label{tab:neural_probe_crossmodel}
107	\resizebox{\columnwidth}{!}{%
108	\begin{tabular}{lccc}
109	\toprule
110	\textbf{Model} & \textbf{2v3 $\auc$} & \textbf{95\% CI} & $\Kempirical^{\text{neural}}$ \\
111	\midrule
112	Qwen-1.5B  & 0.6159 & $[0.610,\,0.622]$ & 3 \\
113	Pythia-1.4B & 0.5963 & $[0.589,\,0.603]$ & 2 \\
114	OLMo-1B    & 0.5892 & $[0.582,\,0.597]$ & 2 \\
115	\bottomrule
116	\end{tabular}}
117	\end{minipage}
118	
119	%% ====================================================================
120	\subsection{Cross-Domain Variation}
121	\label{sec:cross_domain}
122	
123	The preceding experiments use C4 (general web text).
124	To test whether $\Kempirical$ reflects domain structure or model identity, we evaluate on arXiv abstracts ($n{=}2{,}200$ per model) and Wikipedia ($n{=}5{,}000$ per model) across six model configurations spanning four architecture families (Table~\ref{tab:domain_kstar}).
125	
126	\paragraph{arXiv ($\Kempirical{=}3$): five-model cross-validation.}
127	All five domain-competent models yield $\Kempirical{=}3$ on arXiv, with boundary-pair $\auc$ (2v3) ranging from 0.6215 to 0.6545, all exceeding $\theta$.
128	The elevated signal reflects higher per-generation distributional shift (1v2 JSD $= 0.077$ vs.\ ${\sim}0.01$ for C4): formulaic features (LaTeX formatting, citation patterns, mathematical notation) degrade slowly under autoregressive generation and supply persistent depth signal across four architecture families and 1.4B--8B parameters.
129	Removing LaTeX markup reduces 2v3 AUC by ${\sim}$1.8\,pp but preserves $\Kempirical{=}3$ (CI lower $= 0.610 > \theta$; Table~\ref{tab:latex_ablation}); content-level properties dominate.
130	OLMo-1B is a capacity failure (0v1 JSD $= 0.33$, near-total information loss), not a counter-example.
131	Mistral-7B provides the strongest domain-dependence evidence: $\Kempirical{=}1$ on C4 (Section~\ref{sec:boundary_cases}) but $\Kempirical{=}3$ on arXiv: domain structure alone can shift $\Kempirical$ by two levels within the same model.
132	
133	\paragraph{Wikipedia ($\Kempirical{=}1$): single-generation saturation.}
134	With scorer confound controlled (Pythia-1.4B for Qwen generators; Qwen-1.5B, itself cross-family, for all others), all six models yield $\Kempirical{=}1$ on Wikipedia: 1v2 $\auc$ ranges from 0.499 (OLMo) to 0.595 (LLaMA), all below $\theta$.
135	Wikipedia represents the simplest domain tested; its encyclopedic regularity provides minimal structural signal beyond the 0v1 boundary, and a single generation pass suffices for complete saturation.
136	Same-family scoring inflates Qwen $\Kempirical$ to 2 on Wikipedia ($\Delta = +2.4$\,pp); cross-family scoring controls this bias without affecting C4 results (Appendix~\ref{sec:wiki_domain}).
137	
138	\paragraph{Code ($\Kempirical{=}1$--$2$): cross-modality confirmation.}
139	Python functions from CodeSearchNet~\cite{husain2019codesearchnet} ($n{=}5{,}000$) yield $\Kempirical{=}2$ for four models (Qwen-1.5B/7B, LLaMA-8B, Mistral-7B; 1v2 $\auc$: 0.615--0.739; Table~\ref{tab:code_crossmodel_kstar}), but $\Kempirical{=}1$ for capacity-limited Pythia-1.4B ($\auc = 0.598$, CI upper $= 0.603$).
140	Code matches C4 despite a different modality, with the same sharp 2v3 collapse (JSD ratio $11.7$--$13.5\times$).
141	Cross-family scorer validation confirms Code $\Kempirical{=}2$ is text-intrinsic ($\Delta \leq 1.9$\,pp; Appendix~\ref{sec:code_domain}).
142	
143	\paragraph{Domain as the primary factor.}
144	With the scorer confound controlled, the domain ordering is: arXiv ($\Kempirical{=}3$) $>$ C4 ($\Kempirical{=}2$) $\geq$ Code ($\Kempirical{=}1$--$2$) $\geq$ Wikipedia ($\Kempirical{=}1$).
145	Scale (1B--14B) and architecture do not alter the C4/arXiv/Wikipedia ordering; code shows model-dependent variation at the boundary, but domain structural complexity remains the primary determinant of $\Kempirical$.
146	
147	\noindent\begin{minipage}{\columnwidth}
148	\centering
149	\footnotesize
150	\captionof{table}{Domain $\times$ Model $\Kempirical$ matrix (scorer-controlled). Wikipedia values use cross-family scorer (Pythia-1.4B). $^*$OLMo arXiv: capacity failure. $^\dagger$Same-family scorer yields $\Kempirical{=}2$; controlled value shown. $^\ddagger$Borderline: Pythia CI upper $= 0.603$, Mistral CI lower $= 0.603$.}
151	\label{tab:domain_kstar}
152	\resizebox{\columnwidth}{!}{%
153	\begin{tabular}{lcccc}
154	\toprule
155	\textbf{Model} & \textbf{C4} & \textbf{Code} & \textbf{arXiv} & \textbf{Wikipedia} \\
156	\midrule
157	Qwen-1.5B    & 2 & 2 & 3 & 1$^\dagger$ \\
158	Qwen-7B      & 2 & 2 & 3 & 1$^\dagger$ \\
159	Pythia-1.4B  & 2 & 1$^\ddagger$ & 3 & 1 \\
160	OLMo-1B      & 2 & --- & 1$^*$ & 1 \\
161	LLaMA-3.1-8B & 2 & 2 & 3 & 1 \\
162	Mistral-7B   & 1 & 2$^\ddagger$ & 3 & 1 \\
163	\bottomrule
164	\end{tabular}}
165	\end{minipage}
166	
167	%% ====================================================================
168	\subsection{Binary Detector Confidence}
169	\label{sec:binary_confidence}
170	
171	Binary detectors (DivEye~\cite{basani2026diveye}, Binoculars~\cite{hans2024binoculars}) show moderate rank correlations with depth ($|\rho| = 0.06$--$0.46$; Table~\ref{tab:s9_binary_spearman}) but fail as depth proxies: 6-class accuracy is at or below chance ($\leq 0.199$ vs.\ 0.167 baseline), pairwise $\auc$ yields $\Kempirical^{\text{binary}} \leq 1$, and multiple conditions exhibit non-monotonic AUC at deeper pairs.
172	The observed correlation is an artifact of 0v1 separation rather than fine-grained depth signal.
173	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b14a8195-4cdb-464f-9351-298c742145c2",
  "isSidechain": false,
  "promptId": "12172553-d9aa-40c5-a42d-a4d4469a539a",
  "type": "user",
  "uuid": "b7cbeeb4-b9e9-4bd9-9afd-faa6ba3ea250",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate generational depth estimation on nine model configurations spanning five architecture families:\nPythia-1.4B, OLMo-1B, Qwen2.5-1.5B-Instruct (rewrite and continuation), Qwen2.5-1.5B (base), Qwen2.5-7B, Qwen2.5-14B, LLaMA-3.1-8B, and Mistral-7B, all in continuation mode except where noted.\nAll experiments use the OBD-LightGBM classifier with the 15-dimensional feature set (Section~\\ref{sec:method}), with 5{,}000 texts per depth level (generations 0--5; power analysis in Appendix~\\ref{sec:power_curve}).\n\n%% ====================================================================\n\\subsection{\\texorpdfstring{$\\Kempirical \\leq 2$}{K*<=2} Across Model Configurations (C4)}\n\\label{sec:kstar_boundary}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Pairwise $\\auc$ for adjacent depth pairs with bootstrap 95\\% CIs and permutation $p$-values for boundary rows.\n$\\Kempirical = 2$ requires 1v2 CI lower bound $> \\theta{=}0.60$ and 2v3 CI lower bound $\\leq \\theta$ (Eq.~\\ref{eq:kstar}).\nExtended results (all models) in Table~\\ref{tab:kstar_ci_extended}.}\n\\label{tab:kstar_ci}\n\\begin{tabular}{lcccccccccc}\n\\toprule\n & \\multicolumn{2}{c}{Qwen-rw} & \\multicolumn{2}{c}{Pythia} & \\multicolumn{2}{c}{OLMo} & \\multicolumn{2}{c}{Qwen-cont} & \\multicolumn{2}{c}{Qwen-7B\\rlap{$^\\ddagger$}} \\\\\n\\cmidrule(lr){2-3}\\cmidrule(lr){4-5}\\cmidrule(lr){6-7}\\cmidrule(lr){8-9}\\cmidrule(lr){10-11}\n & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI \\\\\n\\midrule\n0v1 & .9956 & & .9932 & & .9970 & & .9971 & & .9638 & [.961,\\,.967] \\\\\n1v2 & .6955 & [.686,\\,.704]\\rlap{$^*$} & .6539 & [.645,\\,.663]\\rlap{$^*$} & .6145 & [.605,\\,.625]\\rlap{$^*$} & .6112 & [.602,\\,.621]\\rlap{$^*$} & .6168 & [.608,\\,.626]\\rlap{$^*$} \\\\\n2v3 & .5893 & [.580,\\,.599] & .5514 & [.542,\\,.563] & .5496 & [.540,\\,.560] & .5609 & [.551,\\,.571] & .5492 & [.539,\\,.559] \\\\\n3v4 & .5435 & & .5152 & & .5091 & & .5409 & & .5276 & \\\\\n4v5 & .5340 & & .5136 & & .5045 & & .5141 & & .5085 & \\\\\n\\bottomrule\n\\multicolumn{11}{l}{\\footnotesize $^*$Permutation $p < 0.001$ for all 1v2 comparisons shown.} \\\\\n\\multicolumn{11}{l}{\\footnotesize $^\\ddagger$Generator: Qwen2.5-7B (fp16); scorer: Qwen2.5-1.5B.}\n\\end{tabular}\n\\end{table*}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig2_auc_decay.pdf}\n\\caption{Pairwise $\\auc$ decay across depth pairs for model-mode configurations (solid) and decoding strategies (dashed). The horizontal dashed line marks $\\theta = 0.60$.}\n\\label{fig:auc_decay}\n\\end{figure}\n\nTable~\\ref{tab:kstar_ci} and Figure~\\ref{fig:auc_decay} show $\\Kempirical \\leq 2$ across all 9 model configurations: 8/9 yield $\\Kempirical{=}2$ (1v2 $\\auc$ range: 0.6112--0.6955; all CI lower bounds $> \\theta$; permutation $p < 0.001$), while Mistral-7B is the only exception ($\\Kempirical{=}1$; 1v2 $\\auc = 0.594$, below $\\theta$; Section~\\ref{sec:boundary_cases}).\nLLaMA-3.1-8B yields $\\Kempirical{=}2$ (0v1 $\\auc = 0.9225$, 1v2 $\\auc = 0.6123$, 95\\% CI $[0.603, 0.622]$; borderline: 1/5 folds falls below $\\theta$; Table~\\ref{tab:kstar_ci_extended}).\nAmong non-Qwen families: Pythia and OLMo yield clear $\\Kempirical{=}2$, LLaMA is borderline (CI lower $= 0.603$), and Mistral yields $\\Kempirical{=}1$; the Qwen-heavy configuration space (5/9) does not alter this per-family pattern.\nAll four decoding strategies likewise yield $\\Kempirical{=}2$ (Table~\\ref{tab:s2_decoding}).\nThe 1v2 spread due to generation mode ($\\Delta = 8.4$\\,pp within Qwen) exceeds the spread across models in continuation mode ($\\Delta = 3.9$\\,pp).\n\n\\paragraph{Scale and instruction-tuning invariance.}\n$\\Kempirical{=}2$ persists from 1.5B through 14B: Qwen-14B (1v2 $\\auc = 0.621$ $[0.612, 0.630]$), Qwen-7B ($0.6168$ $[0.608, 0.626]$), and LLaMA-3.1-8B ($0.6123$) all exceed $\\theta$, despite progressively reduced 0v1 signal (0.960 at 14B, 0.964 at 7B, 0.923 at 8B vs.\\ $> 0.99$ at $\\leq$1.5B).\nA base-vs.-instruct ablation at 1.5B likewise yields $\\Kempirical = 2$ (1v2 $\\auc = 0.626$); the boundary is not an instruction-tuning artifact.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_kstar_theta.pdf}\n\\caption{$\\Kempirical(\\theta)$ sensitivity curve for six configurations. $\\Kempirical$: maximum discriminable depth; $\\theta$: AUC decision threshold. All configurations yield $\\Kempirical{=}2$ at $\\theta{=}0.60$ (dashed line). At $\\theta{=}0.70$, all drop to $\\Kempirical{=}1$.}\n\\label{fig:kstar_theta}\n\\end{figure}\n\nFigure~\\ref{fig:kstar_theta} shows $\\Kempirical$ as a function of $\\theta$: web text $\\Kempirical{=}2$ is stable across a 5\\,pp window ($\\theta \\in [0.575, 0.625]$), with a gradual transition to $\\Kempirical{=}3$ at $\\theta{=}0.55$ (two Qwen configurations) and $\\Kempirical{=}1$ at $\\theta{=}0.70$.\nThe domain ordering (arXiv $>$ web $\\geq$ cross-scorer) is preserved across the full $\\theta$ range (Table~\\ref{tab:theta_sensitivity}; Figure~\\ref{fig:theta_sensitivity} in Appendix).\n\n%% ====================================================================\n\\subsection{Largely Generator-Independent Transfer}\n\\label{sec:transfer}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.85\\columnwidth]{figures/fig3_transfer_heatmap.pdf}\n\\caption{Cross-model transfer heatmap. Each cell shows 6-class ordinal accuracy when trained on the row model and tested on the column model, divided by in-domain accuracy (retention rate). Pythia$\\leftrightarrow$OLMo: 90--92\\%; Qwen-rewrite$\\to$continuation: 61--63\\%.}\n\\label{fig:transfer_heatmap}\n\\end{figure}\n\nContinuation-mode classifiers transfer well across generators (Figure~\\ref{fig:transfer_heatmap}; full matrix in Table~\\ref{tab:s1_transfer}): Pythia$\\leftrightarrow$OLMo retains 90--92\\%, Qwen-cont$\\leftrightarrow$Pythia 84--85\\%, Qwen-cont$\\leftrightarrow$OLMo 80--85\\% (0v1 cross-model $\\auc > 0.96$ for all pairs).\nQwen-rewrite classifiers transfer poorly (61--63\\%), consistent with reliance on mode-specific artifacts rather than generalizable depth features.\n\n\\paragraph{Cross-scorer validation.}\nReplacing the self-scorer with Pythia-1.4B or OLMo-1B preserves feature rankings ($\\rho > 0.90$; Table~\\ref{tab:crossscorer}).\n$\\Kempirical$ is largely robust to scorer choice: across 22 cross-scorer configurations on C4 and arXiv, $\\Kempirical$ was preserved in 20 cases; the two exceptions (Qwen-cont scored by Pythia on C4, Qwen-7B cross-scored on arXiv) are borderline, with AUC within 0.002 of $\\theta$.\nQwen-cont is the most scorer-sensitive continuation-mode configuration: its self-scored 1v2 CI lower bound exceeds $\\theta$ by only 0.2\\,pp (Table~\\ref{tab:kstar_ci}), and cross-family scoring pushes it below $\\theta$.\nFor arXiv, Pythia-1.4B cross-scoring preserves $\\Kempirical{=}3$ for 3/4 generators (2v3 $\\auc$: 0.608--0.632); Qwen-7B drops to borderline $\\Kempirical{=}2$ ($\\Delta = -2.7$\\,pp), consistent with Qwen scorer sensitivity on C4 and Wikipedia (Table~\\ref{tab:arxiv_crossscorer_ci}).\nA three-way ANOVA (Generator $\\times$ Scorer $\\times$ Depth-Pair; $N{=}300$; Table~\\ref{tab:anova_crossscorer}) confirms that Depth-Pair dominates variance ($\\eta^2_p = 0.998$); Scorer is statistically significant ($p < .001$) but practically minor ($\\eta^2_p = 0.192$), consistent with a detectable but small scorer influence on absolute discriminability.\n\n%% ====================================================================\n\\subsection{Feature Ordering and Generation Mode}\n\\label{sec:feature_degradation}\n\\label{sec:generation_mode}\n\nAmong continuation-mode models, single-feature $\\auc$ rankings are highly correlated ($\\rho \\geq 0.85$; Table~\\ref{tab:top_features}).\nThe top-3 features (\\texttt{surp\\_d1\\_std}, \\texttt{surp\\_std}, \\texttt{surp\\_d2\\_std}) are shared across all three families: autoregressive generation progressively damps surprisal variability; however, no single feature subset of size ${<}8$ reliably sustains $\\Kempirical{=}2$ (Appendix~\\ref{sec:feature_subset}).\nA feature group ablation (Appendix~\\ref{sec:feature_ablation}) confirms that surprisal (base) dominates on arXiv (single AUC $= 0.809$, LOO $\\Delta = 0.031$); on C4 and Wikipedia, all LOO drops fall within fold variance ($\\leq 0.007$).\nQwen-rewrite diverges (\\texttt{freq\\_entropy} dominates), consistent with its poor cross-model transfer (61--63\\%).\nWithin Qwen, rewrite yields 1v2 $\\auc = 0.6955$ vs.\\ continuation's $0.6112$ ($\\Delta = +8.4$\\,pp); continuation mode is therefore recommended as the canonical condition.\n\n%% ====================================================================\n\\subsection{Neural Probe}\n\\label{sec:neural_probe}\n\nReplacing the 15D features with frozen encoder hidden states (MLP probe, 5{,}000 texts per depth; Table~\\ref{tab:neural_probe_crossmodel}), Qwen achieves $\\Kempirical^{\\text{neural}} = 3$ (2v3 $\\auc = 0.6159$), while Pythia and OLMo remain at $\\Kempirical^{\\text{neural}} = 2$ ($\\auc_{2v3}$: 0.5963, 0.5892).\nThe Qwen-only elevation reflects self-familiarity artifacts that transfer poorly (Section~\\ref{sec:transfer}); the 15D features yield consistent $\\Kempirical = 2$ across all families.\n\n\\noindent\\begin{minipage}{\\columnwidth}\n\\centering\n\\footnotesize\n\\captionof{table}{Neural probe pairwise AUC using frozen-encoder MLP. Each cell reports AUC for classifying depth $d$ vs.\\ $d{+}1$ text. $\\Kempirical^{\\text{neural}}$: maximum depth where AUC exceeds $\\theta = 0.60$.}\n\\label{tab:neural_probe_crossmodel}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Model} & \\textbf{2v3 $\\auc$} & \\textbf{95\\% CI} & $\\Kempirical^{\\text{neural}}$ \\\\\n\\midrule\nQwen-1.5B  & 0.6159 & $[0.610,\\,0.622]$ & 3 \\\\\nPythia-1.4B & 0.5963 & $[0.589,\\,0.603]$ & 2 \\\\\nOLMo-1B    & 0.5892 & $[0.582,\\,0.597]$ & 2 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{minipage}\n\n%% ====================================================================\n\\subsection{Cross-Domain Variation}\n\\label{sec:cross_domain}\n\nThe preceding experiments use C4 (general web text).\nTo test whether $\\Kempirical$ reflects domain structure or model identity, we evaluate on arXiv abstracts ($n{=}2{,}200$ per model) and Wikipedia ($n{=}5{,}000$ per model) across six model configurations spanning four architecture families (Table~\\ref{tab:domain_kstar}).\n\n\\paragraph{arXiv ($\\Kempirical{=}3$): five-model cross-validation.}\nAll five domain-competent models yield $\\Kempirical{=}3$ on arXiv, with boundary-pair $\\auc$ (2v3) ranging from 0.6215 to 0.6545, all exceeding $\\theta$.\nThe elevated signal reflects higher per-generation distributional shift (1v2 JSD $= 0.077$ vs.\\ ${\\sim}0.01$ for C4): formulaic features (LaTeX formatting, citation patterns, mathematical notation) degrade slowly under autoregressive generation and supply persistent depth signal across four architecture families and 1.4B--8B parameters.\nRemoving LaTeX markup reduces 2v3 AUC by ${\\sim}$1.8\\,pp but preserves $\\Kempirical{=}3$ (CI lower $= 0.610 > \\theta$; Table~\\ref{tab:latex_ablation}); content-level properties dominate.\nOLMo-1B is a capacity failure (0v1 JSD $= 0.33$, near-total information loss), not a counter-example.\nMistral-7B provides the strongest domain-dependence evidence: $\\Kempirical{=}1$ on C4 (Section~\\ref{sec:boundary_cases}) but $\\Kempirical{=}3$ on arXiv: domain structure alone can shift $\\Kempirical$ by two levels within the same model.\n\n\\paragraph{Wikipedia ($\\Kempirical{=}1$): single-generation saturation.}\nWith scorer confound controlled (Pythia-1.4B for Qwen generators; Qwen-1.5B, itself cross-family, for all others), all six models yield $\\Kempirical{=}1$ on Wikipedia: 1v2 $\\auc$ ranges from 0.499 (OLMo) to 0.595 (LLaMA), all below $\\theta$.\nWikipedia represents the simplest domain tested; its encyclopedic regularity provides minimal structural signal beyond the 0v1 boundary, and a single generation pass suffices for complete saturation.\nSame-family scoring inflates Qwen $\\Kempirical$ to 2 on Wikipedia ($\\Delta = +2.4$\\,pp); cross-family scoring controls this bias without affecting C4 results (Appendix~\\ref{sec:wiki_domain}).\n\n\\paragraph{Code ($\\Kempirical{=}1$--$2$): cross-modality confirmation.}\nPython functions from CodeSearchNet~\\cite{husain2019codesearchnet} ($n{=}5{,}000$) yield $\\Kempirical{=}2$ for four models (Qwen-1.5B/7B, LLaMA-8B, Mistral-7B; 1v2 $\\auc$: 0.615--0.739; Table~\\ref{tab:code_crossmodel_kstar}), but $\\Kempirical{=}1$ for capacity-limited Pythia-1.4B ($\\auc = 0.598$, CI upper $= 0.603$).\nCode matches C4 despite a different modality, with the same sharp 2v3 collapse (JSD ratio $11.7$--$13.5\\times$).\nCross-family scorer validation confirms Code $\\Kempirical{=}2$ is text-intrinsic ($\\Delta \\leq 1.9$\\,pp; Appendix~\\ref{sec:code_domain}).\n\n\\paragraph{Domain as the primary factor.}\nWith the scorer confound controlled, the domain ordering is: arXiv ($\\Kempirical{=}3$) $>$ C4 ($\\Kempirical{=}2$) $\\geq$ Code ($\\Kempirical{=}1$--$2$) $\\geq$ Wikipedia ($\\Kempirical{=}1$).\nScale (1B--14B) and architecture do not alter the C4/arXiv/Wikipedia ordering; code shows model-dependent variation at the boundary, but domain structural complexity remains the primary determinant of $\\Kempirical$.\n\n\\noindent\\begin{minipage}{\\columnwidth}\n\\centering\n\\footnotesize\n\\captionof{table}{Domain $\\times$ Model $\\Kempirical$ matrix (scorer-controlled). Wikipedia values use cross-family scorer (Pythia-1.4B). $^*$OLMo arXiv: capacity failure. $^\\dagger$Same-family scorer yields $\\Kempirical{=}2$; controlled value shown. $^\\ddagger$Borderline: Pythia CI upper $= 0.603$, Mistral CI lower $= 0.603$.}\n\\label{tab:domain_kstar}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{C4} & \\textbf{Code} & \\textbf{arXiv} & \\textbf{Wikipedia} \\\\\n\\midrule\nQwen-1.5B    & 2 & 2 & 3 & 1$^\\dagger$ \\\\\nQwen-7B      & 2 & 2 & 3 & 1$^\\dagger$ \\\\\nPythia-1.4B  & 2 & 1$^\\ddagger$ & 3 & 1 \\\\\nOLMo-1B      & 2 & --- & 1$^*$ & 1 \\\\\nLLaMA-3.1-8B & 2 & 2 & 3 & 1 \\\\\nMistral-7B   & 1 & 2$^\\ddagger$ & 3 & 1 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{minipage}\n\n%% ====================================================================\n\\subsection{Binary Detector Confidence}\n\\label{sec:binary_confidence}\n\nBinary detectors (DivEye~\\cite{basani2026diveye}, Binoculars~\\cite{hans2024binoculars}) show moderate rank correlations with depth ($|\\rho| = 0.06$--$0.46$; Table~\\ref{tab:s9_binary_spearman}) but fail as depth proxies: 6-class accuracy is at or below chance ($\\leq 0.199$ vs.\\ 0.167 baseline), pairwise $\\auc$ yields $\\Kempirical^{\\text{binary}} \\leq 1$, and multiple conditions exhibit non-monotonic AUC at deeper pairs.\nThe observed correlation is an artifact of 0v1 separation rather than fine-grained depth signal.\n",
      "numLines": 173,
      "startLine": 1,
      "totalLines": 173
    }
  },
  "sourceToolAssistantUUID": "b14a8195-4cdb-464f-9351-298c742145c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 182 · 2026-05-19T13:05:19.687Z_

<details open><summary>🔧 Tool call — Read · `toolu_01775eNpWW5jomHzQGFGdraA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c3.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b7cbeeb4-b9e9-4bd9-9afd-faa6ba3ea250",
  "isSidechain": false,
  "requestId": "req_011CbByZGQtZEGUDeiPCaKvC",
  "type": "assistant",
  "uuid": "86a6e627-38c8-48f1-9083-5019e1d5567e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R5aasAvdxKFuGzJ54fMWnH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 129871,
      "cache_read_input_tokens": 11841,
      "output_tokens": 479,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 129871,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 479,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 129871,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 129871
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    }
  }
}
```

</details>

---


### Runtime record

_source line 183_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 2 审稿请求]: ## Round 9（继续审稿）— Reviewer 2（新颖性 + 完整性 + 写作质量）  上轮评分：3.5 (Borderline Conference)。论文已大幅修订，请重点验证以下 open/in_progress issues 是否已充分修复。  ### 论文路径 `projects/gen-depth-contamination/docs/paper…",
  "leafUuid": "8f61558a-2de6-4a81-a240-3a7721a24000",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77"
}
```

---


### Runtime record

_source line 184_

```json
{
  "type": "ai-title",
  "aiTitle": "Review paper on data contamination detection for EMNLP 2026",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77"
}
```

---


### Assistant

_source line 185 · 2026-05-19T13:05:23.519Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I've read the main body sections. Now let me read the discussion, conclusion, appendix, and the remaining files to check for all the issues.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f61558a-2de6-4a81-a240-3a7721a24000",
  "isSidechain": false,
  "requestId": "req_011CbByZv8mt2fC7GHPddped",
  "type": "assistant",
  "uuid": "f682fd85-8ef6-4270-897d-bd6a6a3ab7e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CUpAyouh8CqiFfR751WM23",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 144566,
      "cache_read_input_tokens": 11841,
      "output_tokens": 281,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 144566,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 281,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 144566,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 144566
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---


### Tool call

_source line 186 · 2026-05-19T13:05:25.077Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GFURHfmYXVn78CYz3oSk2q`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f682fd85-8ef6-4270-897d-bd6a6a3ab7e1",
  "isSidechain": false,
  "requestId": "req_011CbByZv8mt2fC7GHPddped",
  "type": "assistant",
  "uuid": "a6d9aa01-4b4e-4dc3-8c68-727cfad95e3a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CUpAyouh8CqiFfR751WM23",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 144566,
      "cache_read_input_tokens": 11841,
      "output_tokens": 281,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 144566,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 281,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 144566,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 144566
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---


### Tool result

_source line 187 · 2026-05-19T13:05:25.082Z_

<details><summary>↩ Tool result · `toolu_01GFURHfmYXVn78CYz3oSk2q`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	\label{sec:why_kstar}
4	\label{sec:one_wash}
5	\label{sec:negative_graduated}
6	\label{sec:repr_dependence}
7	\label{sec:boundary_cases}
8	\label{sec:length_confound}
9	
10	\begin{figure}[t]
11	\centering
12	\includegraphics[width=\columnwidth]{figures/fig_jsd_decay.pdf}
13	\caption{Token-level JSD between adjacent depth pairs on log scale. Blue band: min-max range across 8 C4 models (1B--14B) with $\Kempirical{=}2$; dashed purple: Mistral-7B ($\Kempirical{=}1$, cross-scorer validated); green: arXiv Pythia ($\Kempirical{=}3$); dotted red: retrain-chain ($\Kempirical{=}7$). C4 models exhibit a sharp cliff ($\lambda \approx 2.2$--$3.5$), while arXiv decays gradually ($\lambda \approx 1.0$) and retrain-chain shows no cliff ($\lambda = 0.285$).}
14	\label{fig:jsd_decay}
15	\end{figure}
16	
17	\paragraph{One-wash laundering (web text).}
18	For general web text, $\Kempirical{=}2$ reflects concentrated information loss: 0v1 is near-trivially separable ($\auc \geq 0.92$), 1v2 drops by ${\sim}$30\,pp, and 2v3 falls below $\theta$, so a single generation pass renders text indistinguishable from deeper content.
19	Neither frontier LLMs nor alternative classifiers improve depth recovery beyond this boundary (McNemar $p > 0.05$; Appendix).
20	
21	\paragraph{JSD decay and the discrimination boundary.}
22	Token-level JSD between adjacent generations reveals two decay regimes (Figure~\ref{fig:jsd_decay}): C4 models exhibit a sharp cliff (0v1 JSD exceeds 1v2 by 6--56$\times$) followed by rapid convergence, while arXiv decays ${\sim}$3$\times$ slower ($\lambda \approx 1.0$ vs.\ $2.9$).
23	The retrain-chain ($\lambda = 0.285$, no cliff) reflects cumulative model-adaptation artifacts, extending $\Kempirical$ to 7 (Appendix~\ref{sec:jsd_extended}).
24	
25	\paragraph{Graduated filtering failure.}
26	For web text, 2v3 $\auc < \theta$ across all configurations, so depth assignments beyond $d{=}2$ approximate random labels; the strategy ordering binary $>$ graduated aligns with $\Kempirical{=}2$ (Section~\ref{sec:filtering}).
27	
28	\paragraph{Representation and scorer dependence.}
29	$\Kempirical$ is representation-dependent (frozen Qwen embeddings yield $\Kempirical^{\text{neural}} = 3$ vs.\ $\Kempirical^{\text{neural}} = 2$ for Pythia and OLMo; Table~\ref{tab:neural_probe_crossmodel}) and scorer-dependent (cross-family scoring reduces Wikipedia $\Kempirical$ from 2 to 1, Appendix~\ref{sec:wiki_domain}, while preserving C4 feature rankings $\rho > 0.90$ and $\Kempirical$ for 6/8 configurations, Section~\ref{sec:transfer}).
30	
31	\paragraph{Domain dependence of $\Kempirical$.}
32	C4 yields $\Kempirical{=}2$ (8/9 configurations), Python code $\Kempirical{=}2$ for four models across four architecture families ($\Kempirical{=}1$ for capacity-limited Pythia-1.4B; Section~\ref{sec:cross_domain}), arXiv $\Kempirical{=}3$ (five models, four families), and Wikipedia $\Kempirical{=}1$ (Appendix~\ref{sec:wiki_domain}); the ordering correlates with structural complexity (Table~\ref{tab:domain-ttr-entropy}).
33	Code and C4 share $\Kempirical{=}2$ but with shifted cliff positions: syntactic constraints preserve depth-1 signal in code, so domain structure governs both $\Kempirical$ and the decay profile.
34	The only C4 exception (Mistral-7B, $\Kempirical{=}1$) yields $\Kempirical{=}2$ on code and $\Kempirical{=}3$ on arXiv; a LaTeX ablation confirms content rather than formatting drives the arXiv difference (Appendix~\ref{sec:latex_ablation}).
35	
36	\paragraph{Surprisal attenuation and boundary variation.}
37	\label{sec:surprisal_attenuation}
38	The Mistral-7B exception ($\Kempirical{=}1$) arises from compressed surprisal dynamic range (Table~\ref{tab:cohens_d_full}); larger 0$\to$1 surprisal drops correlate with higher 1v2 $\auc$ (Table~\ref{tab:borderline_features}), predicting $\Kempirical$ may decrease beyond 14B.
39	
40	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a6d9aa01-4b4e-4dc3-8c68-727cfad95e3a",
  "isSidechain": false,
  "promptId": "12172553-d9aa-40c5-a42d-a4d4469a539a",
  "type": "user",
  "uuid": "04fe1c44-3bc0-4798-a95c-a5c47989f98d",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex",
      "content": "\\section{Discussion}\n\\label{sec:discussion}\n\\label{sec:why_kstar}\n\\label{sec:one_wash}\n\\label{sec:negative_graduated}\n\\label{sec:repr_dependence}\n\\label{sec:boundary_cases}\n\\label{sec:length_confound}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_jsd_decay.pdf}\n\\caption{Token-level JSD between adjacent depth pairs on log scale. Blue band: min-max range across 8 C4 models (1B--14B) with $\\Kempirical{=}2$; dashed purple: Mistral-7B ($\\Kempirical{=}1$, cross-scorer validated); green: arXiv Pythia ($\\Kempirical{=}3$); dotted red: retrain-chain ($\\Kempirical{=}7$). C4 models exhibit a sharp cliff ($\\lambda \\approx 2.2$--$3.5$), while arXiv decays gradually ($\\lambda \\approx 1.0$) and retrain-chain shows no cliff ($\\lambda = 0.285$).}\n\\label{fig:jsd_decay}\n\\end{figure}\n\n\\paragraph{One-wash laundering (web text).}\nFor general web text, $\\Kempirical{=}2$ reflects concentrated information loss: 0v1 is near-trivially separable ($\\auc \\geq 0.92$), 1v2 drops by ${\\sim}$30\\,pp, and 2v3 falls below $\\theta$, so a single generation pass renders text indistinguishable from deeper content.\nNeither frontier LLMs nor alternative classifiers improve depth recovery beyond this boundary (McNemar $p > 0.05$; Appendix).\n\n\\paragraph{JSD decay and the discrimination boundary.}\nToken-level JSD between adjacent generations reveals two decay regimes (Figure~\\ref{fig:jsd_decay}): C4 models exhibit a sharp cliff (0v1 JSD exceeds 1v2 by 6--56$\\times$) followed by rapid convergence, while arXiv decays ${\\sim}$3$\\times$ slower ($\\lambda \\approx 1.0$ vs.\\ $2.9$).\nThe retrain-chain ($\\lambda = 0.285$, no cliff) reflects cumulative model-adaptation artifacts, extending $\\Kempirical$ to 7 (Appendix~\\ref{sec:jsd_extended}).\n\n\\paragraph{Graduated filtering failure.}\nFor web text, 2v3 $\\auc < \\theta$ across all configurations, so depth assignments beyond $d{=}2$ approximate random labels; the strategy ordering binary $>$ graduated aligns with $\\Kempirical{=}2$ (Section~\\ref{sec:filtering}).\n\n\\paragraph{Representation and scorer dependence.}\n$\\Kempirical$ is representation-dependent (frozen Qwen embeddings yield $\\Kempirical^{\\text{neural}} = 3$ vs.\\ $\\Kempirical^{\\text{neural}} = 2$ for Pythia and OLMo; Table~\\ref{tab:neural_probe_crossmodel}) and scorer-dependent (cross-family scoring reduces Wikipedia $\\Kempirical$ from 2 to 1, Appendix~\\ref{sec:wiki_domain}, while preserving C4 feature rankings $\\rho > 0.90$ and $\\Kempirical$ for 6/8 configurations, Section~\\ref{sec:transfer}).\n\n\\paragraph{Domain dependence of $\\Kempirical$.}\nC4 yields $\\Kempirical{=}2$ (8/9 configurations), Python code $\\Kempirical{=}2$ for four models across four architecture families ($\\Kempirical{=}1$ for capacity-limited Pythia-1.4B; Section~\\ref{sec:cross_domain}), arXiv $\\Kempirical{=}3$ (five models, four families), and Wikipedia $\\Kempirical{=}1$ (Appendix~\\ref{sec:wiki_domain}); the ordering correlates with structural complexity (Table~\\ref{tab:domain-ttr-entropy}).\nCode and C4 share $\\Kempirical{=}2$ but with shifted cliff positions: syntactic constraints preserve depth-1 signal in code, so domain structure governs both $\\Kempirical$ and the decay profile.\nThe only C4 exception (Mistral-7B, $\\Kempirical{=}1$) yields $\\Kempirical{=}2$ on code and $\\Kempirical{=}3$ on arXiv; a LaTeX ablation confirms content rather than formatting drives the arXiv difference (Appendix~\\ref{sec:latex_ablation}).\n\n\\paragraph{Surprisal attenuation and boundary variation.}\n\\label{sec:surprisal_attenuation}\nThe Mistral-7B exception ($\\Kempirical{=}1$) arises from compressed surprisal dynamic range (Table~\\ref{tab:cohens_d_full}); larger 0$\\to$1 surprisal drops correlate with higher 1v2 $\\auc$ (Table~\\ref{tab:borderline_features}), predicting $\\Kempirical$ may decrease beyond 14B.\n\n",
      "numLines": 40,
      "startLine": 1,
      "totalLines": 40
    }
  },
  "sourceToolAssistantUUID": "a6d9aa01-4b4e-4dc3-8c68-727cfad95e3a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 188 · 2026-05-19T13:05:25.545Z_

<details open><summary>🔧 Tool call — Read · `toolu_011kkHLk4g8PQ9keRQp7NNNZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "04fe1c44-3bc0-4798-a95c-a5c47989f98d",
  "isSidechain": false,
  "requestId": "req_011CbByZv8mt2fC7GHPddped",
  "type": "assistant",
  "uuid": "35bc3564-1bb5-40ac-8782-77df80a53f67",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CUpAyouh8CqiFfR751WM23",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 144566,
      "cache_read_input_tokens": 11841,
      "output_tokens": 281,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 144566,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 281,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 144566,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 144566
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---


### Tool result

_source line 189 · 2026-05-19T13:05:25.550Z_

<details><summary>↩ Tool result · `toolu_011kkHLk4g8PQ9keRQp7NNNZ`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We measure $\Kempirical{=}2$ for web text (8/9 configurations), $\Kempirical{=}1$--$2$ for code, and $\Kempirical{=}3$ for arXiv, with domain structure as the primary determinant of the saturation boundary.
5	For most domains, a single generation pass renders synthetic text indistinguishable from deeper recursive output, limiting the practical ceiling of depth-based detection to one or two generations.
6	These domain-specific boundaries imply that contamination detection and data curation should adopt domain-aware thresholds rather than uniform binary classifiers; our generator-independent features ($\rho > 0.90$) provide a practical basis for such filtering.
7	Future work should extend this characterization to larger-scale models, additional domains, and temporal tracking of $\Kempirical$ as both models and training corpora evolve.
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "35bc3564-1bb5-40ac-8782-77df80a53f67",
  "isSidechain": false,
  "promptId": "12172553-d9aa-40c5-a42d-a4d4469a539a",
  "type": "user",
  "uuid": "0bcb061c-9f63-4802-98cd-aaae1e33cfed",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/conclusion.tex",
      "content": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe measure $\\Kempirical{=}2$ for web text (8/9 configurations), $\\Kempirical{=}1$--$2$ for code, and $\\Kempirical{=}3$ for arXiv, with domain structure as the primary determinant of the saturation boundary.\nFor most domains, a single generation pass renders synthetic text indistinguishable from deeper recursive output, limiting the practical ceiling of depth-based detection to one or two generations.\nThese domain-specific boundaries imply that contamination detection and data curation should adopt domain-aware thresholds rather than uniform binary classifiers; our generator-independent features ($\\rho > 0.90$) provide a practical basis for such filtering.\nFuture work should extend this characterization to larger-scale models, additional domains, and temporal tracking of $\\Kempirical$ as both models and training corpora evolve.\n",
      "numLines": 8,
      "startLine": 1,
      "totalLines": 8
    }
  },
  "sourceToolAssistantUUID": "35bc3564-1bb5-40ac-8782-77df80a53f67",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 190 · 2026-05-19T13:05:25.963Z_

<details open><summary>🔧 Tool call — Read · `toolu_0166wHHyKmVBs4bgoncMTHG1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0bcb061c-9f63-4802-98cd-aaae1e33cfed",
  "isSidechain": false,
  "requestId": "req_011CbByZv8mt2fC7GHPddped",
  "type": "assistant",
  "uuid": "9aacc8bf-e9be-466a-a09c-7f2edb19274e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CUpAyouh8CqiFfR751WM23",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 144566,
      "cache_read_input_tokens": 11841,
      "output_tokens": 281,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 144566,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 281,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 144566,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 144566
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    }
  }
}
```

</details>

---


### Tool result

_source line 191 · 2026-05-19T13:05:26.293Z_

<details><summary>↩ Tool result · `toolu_0166wHHyKmVBs4bgoncMTHG1`</summary>

```text
1	\section{Extended Analysis and Limitations}
2	\label{sec:extended_discussion}
3	
4	This section provides supporting tables for cross-scorer validation (Tables~\ref{tab:crossscorer}--\ref{tab:anova_crossscorer}), followed by extended limitations, ablation studies, and domain-specific analyses.
5	
6	\noindent\begin{minipage}{\columnwidth}
7	\centering
8	\captionof{table}{Cross-scorer validation on Qwen-generated text. Alternative scorers (Pythia-1.4B, OLMo-1B) preserve feature ranking ($\rho > 0.90$) and rewrite-mode $\Kempirical = 2$, but reduce continuation-mode $\Kempirical$ from 2 to 1.}
9	\label{tab:crossscorer}
10	\resizebox{\columnwidth}{!}{\input{tables/tab_crossscorer}}
11	\end{minipage}
12	
13	\begin{table}[h]
14	\centering
15	\small
16	\caption{Three-way ANOVA (Generator $\times$ Scorer $\times$ Depth-Pair) on per-fold pairwise $\auc$ values (Type~II SS). DV = per-fold AUC; $N{=}300$ (12 cells $\times$ 5 folds $\times$ 5 depth-pairs; 3 generators $\times$ 4 scorers). Scorer is statistically significant ($p < .001$) but has a small effect size ($\eta^2_p = 0.19$) relative to Depth-Pair ($\eta^2_p = 1.00$) and Generator ($\eta^2_p = 0.89$), indicating that scorer choice has a detectable but practically minor influence on depth discrimination (Scorer $\eta^2_p$ is approximately 5$\times$ smaller than Generator and dwarfed by Depth-Pair). Per-fold AUC values within the same generator share seed documents across folds and are not fully independent; we therefore rely on effect-size ratios rather than $p$-values for interpretation.}
17	\label{tab:anova_crossscorer}
18	\begin{tabular}{lrrrr}
19	\toprule
20	\textbf{Source} & \textbf{df} & $F$ & $p$ & $\eta^2_p$ \\
21	\midrule
22	Generator     & 2  & 926.8  & ${<}.001$  & .885 \\
23	Scorer        & 3  & 19.02  & ${<}.001$  & .192 \\
24	Depth-Pair    & 4  & 24736  & ${<}.001$  & .998 \\
25	Gen$\times$Scorer & 6 & 8.16 & ${<}.001$ & .170 \\
26	Gen$\times$Depth  & 8 & 993.7 & ${<}.001$ & .971 \\
27	Scorer$\times$Depth & 12 & 2.45 & .005 & .109 \\
28	Residual      & 240 & & & \\
29	\bottomrule
30	\end{tabular}
31	\end{table}
32	
33	\subsection{Extended Limitations}
34	\label{sec:extended_limitations}
35	
36	\emph{Prompt-chain versus retrain-chain.}
37	Both Qwen2.5-1.5B and Pythia-1.4B yield $\Kempirical{=}7$ under retrain-chain LoRA fine-tuning (Table~\ref{tab:retrain_ci}), extending detectable depth by 5 additional generations beyond prompt-chain $\Kempirical{=}2$.
38	Cumulative model-adaptation artifacts (vocabulary narrowing, repetition bias) make each retrained generation highly distinguishable.
39	The two models exhibit different decay profiles: Pythia achieves higher early-pair AUC (1v2: 0.947 vs.\ 0.897) but drops more steeply at deeper pairs (4v5: 0.691 vs.\ 0.746), yet both converge to $\Kempirical{=}7$ (6v7: Qwen 0.641, Pythia 0.634; both CI lower bounds $> \theta$).
40	This convergence despite differences in effective LoRA adaptation capacity (Pythia uses fused QKV attention with rank-16 vs.\ Qwen's separate Q/K/V projections) indicates robustness to LoRA parameterization.
41	The extended discriminability under retraining aligns with theoretical analyses of iterative retraining instability on synthetic data~\cite{bertrand2024stability, gerstgrasser2024model}, where each retraining cycle amplifies distributional artifacts beyond the text-intrinsic degradation observed in prompt-chains.
42	Extrapolating yields 7v8 $\approx 0.57 < \theta$ for both models. This places $\Kempirical{=}7$ near the ceiling for retrain-chains.
43	Prompt-chain $\Kempirical$ represents the operationally relevant boundary for data curation (text-intrinsic information loss); retrain-chain $\Kempirical$ represents the upper bound achievable via model archaeology (known training pipeline).
44	
45	\begin{table}[h]
46	\centering
47	\small
48	\caption{Retrain-chain pairwise $\auc$ with 5-fold CV 95\% CIs. Both models yield $\Kempirical{=}7$; all CI lower bounds $> \theta{=}0.60$. Retrain-chain CIs use fold-level estimates (Section~\ref{sec:retrain_ci_note}).}
49	\label{tab:retrain_ci}
50	\begin{tabular}{lcccc}
51	\toprule
52	 & \multicolumn{2}{c}{\textbf{Qwen-1.5B}} & \multicolumn{2}{c}{\textbf{Pythia-1.4B}} \\
53	\cmidrule(lr){2-3}\cmidrule(lr){4-5}
54	\textbf{Pair} & $\auc$ & 95\% CI & $\auc$ & 95\% CI \\
55	\midrule
56	0v1 & 0.9837 & $[.982,\,.985]$ & 0.9844 & $[.983,\,.986]$ \\
57	1v2 & 0.8971 & $[.895,\,.899]$ & 0.9470 & $[.942,\,.952]$ \\
58	2v3 & 0.8098 & $[.805,\,.814]$ & 0.8891 & $[.882,\,.896]$ \\
59	3v4 & 0.7600 & $[.753,\,.767]$ & 0.7999 & $[.795,\,.805]$ \\
60	4v5 & 0.7459 & $[.738,\,.754]$ & 0.6907 & $[.688,\,.693]$ \\
61	5v6 & 0.7017 & $[.696,\,.708]$ & 0.6497 & $[.643,\,.657]$ \\
62	6v7 & 0.6410 & $[.638,\,.645]$ & 0.6340 & $[.628,\,.641]$ \\
63	\bottomrule
64	\end{tabular}
65	\end{table}
66	
67	\paragraph{CI methodology note.}
68	\label{sec:retrain_ci_note}
69	The main pipeline reports bootstrap 95\% CIs (1{,}000 or 10{,}000 resamples), which are valid because each bootstrap sample preserves the GroupKFold document structure: resampling operates on documents, and all depths of a given document remain together.
70	In the retrain-chain setting, each generation's training corpus is the \emph{output} of the previous generation's fine-tuned model. This creates inter-generation dependencies that standard bootstrap resampling cannot preserve, and naive resampling would inflate AUC estimates.
71	We therefore report fold-based 95\% CIs for retrain-chain experiments, computed as $\bar{x} \pm 1.96 \cdot s / \sqrt{K}$ from the $K{=}5$ GroupKFold AUC values.
72	
73	\emph{Threshold sensitivity.}
74	Table~\ref{tab:theta_sensitivity} reports $\Kempirical$ across $\theta \in [0.55, 0.70]$ for representative configurations including arXiv and cross-scorer conditions.
75	Qwen-continuation's 1v2 CI lower bound exceeds $\theta$ by only 0.2\,pp; all ten boundary comparisons yield permutation $p < 0.001$.
76	
77	\begin{table}[h]
78	\centering
79	\small
80	\caption{$\Kempirical$ as a function of $\theta$ across conditions. The \textbf{domain ordering} (arXiv $>$ web $\geq$ cross-scorer) and \textbf{bounded range} ($\Kempirical{\leq}4$) are preserved across $\theta \in [0.55, 0.70]$. The headline result (web $\Kempirical{=}2$, arXiv $\Kempirical{=}3$) holds for $\theta \in [0.575, 0.625]$.}
81	\label{tab:theta_sensitivity}
82	\resizebox{\columnwidth}{!}{%
83	\begin{tabular}{llcccc}
84	\toprule
85	\textbf{Condition} & \textbf{Config} & $\theta{=}0.55$ & $\theta{=}0.60$ & $\theta{=}0.625$ & $\theta{=}0.70$ \\
86	\midrule
87	C4 (web) & Qwen-rw      & 3 & 2 & 2 & 1 \\
88	C4 (web) & Pythia       & 2 & 2 & 2 & 1 \\
89	C4 (web) & OLMo         & 2 & 2 & 1 & 1 \\
90	C4 (web) & Qwen-cont    & 3 & 2 & 2 & 1 \\
91	C4 (web) & Qwen-7B      & 2 & 2 & 2 & 1 \\
92	C4 (web) & Mistral-7B   & 1 & 1 & 1 & 1 \\
93	\midrule
94	arXiv    & Qwen-1.5B-base (cont.) & 4 & 3 & 3 & 2 \\
95	arXiv    & Pythia-1.4B (cont.)    & 4 & 3 & 3 & 2 \\
96	\midrule
97	Cross-scorer & Qwen-cont/Pythia-scored & 2 & 1 & 1 & 1 \\
98	Cross-scorer & Qwen-cont/OLMo-scored   & 2 & 1 & 1 & 1 \\
99	\bottomrule
100	\end{tabular}}
101	\end{table}
102	
103	\begin{figure}[h]
104	\centering
105	\includegraphics[width=\columnwidth]{figures/fig_theta_sensitivity.pdf}
106	\caption{$\Kempirical$ as a function of $\theta$ across all model $\times$ domain configurations (three panels: C4, arXiv, Wikipedia). The domain ordering (Wikipedia $\Kempirical{\leq}1$ $<$ C4 $\Kempirical{\leq}2$ $<$ arXiv $\Kempirical{\leq}3$) is preserved across the full $\theta \in [0.55, 0.70]$ range. Within each domain, inter-model variation is small relative to inter-domain differences. Source domain rather than model identity governs $\Kempirical$.}
107	\label{fig:theta_sensitivity}
108	\end{figure}
109	
110	\emph{Structural confound: token length.}
111	In continuation mode the generation prompt is discarded, so all depths $\geq 1$ consist entirely of machine-generated tokens and the 1v2 boundary compares texts differing only in conditioning context (human-authored vs.\ machine-generated prompt), not structural composition.
112	Depth~0 texts average ${\sim}$191 subword tokens (C4 truncation), while depth~1+ texts average 193--256 tokens depending on model (Table~\ref{tab:token_length}).
113	This asymmetry is directionally opposite to a length-inflation confound: shorter depth-0 texts provide less feature-extraction context, making 0v1 discrimination harder, not easier.
114	Within depths 1--5, mean token counts are stable (within-model range $\leq$ 4 tokens for all configurations except Qwen-continuation at 6 tokens), so the pairwise comparisons underlying $\Kempirical{=}2$ are unaffected by length.
115	EOS truncation rates are similarly depth-stable within each model: Qwen-rewrite 7--11\%, Pythia 34--36\%, OLMo $<$1\%, Qwen-continuation 17--20\%, Qwen-7B 45--47\%.
116	Models with the highest truncation (Pythia, Qwen-7B) still yield $\Kempirical{=}2$ with the same step-function AUC decay pattern as low-truncation models (Table~\ref{tab:kstar_ci}), EOS truncation therefore does not drive the boundary.
117	
118	\emph{Graduated filtering.}
119	All $\alpha$ values (0.1--0.9) underperform binary-ours on MMLU ($\alpha{=}0.1$: 0.5873; $\alpha{=}0.9$: 0.5892 vs.\ 0.5941); at $\alpha{=}0.9$, HellaSwag matches exactly (0.6701).
120	Binary-ours significantly outperforms all alternatives on MMLU ($p_{\text{corr}} \leq 0.021$); Graduated$_{0.9}$ is indistinguishable on HellaSwag ($p = 1.00$) but worse on MMLU ($p_{\text{corr}} = 0.011$).
121	\label{tab:pairwise_significance}
122	
123	\subsection{Dose-Response: Contamination Ratio Effect}
124	\label{sec:dose_response}
125	
126	The main filtering experiments (Section~\ref{sec:filtering}) use 100\% synthetic data to maximize effect size.
127	To characterize behavior at lower contamination ratios, we mix synthetic depths 1--5 with clean C4 at 10\%, 30\%, and 50\% contamination (Qwen-1.5B continuation, 5 seeds each; Table~\ref{tab:dose_response}).
128	
129	\begin{table}[h]
130	\centering
131	\small
132	\caption{MMLU and HellaSwag by contamination ratio and filtering strategy (5 seeds, mean $\pm$ std). Base model MMLU: 0.6018. Binary filtering retains a significant advantage on HellaSwag across all ratios ($p \leq 0.004$, Holm-Bonferroni corrected).}
133	\label{tab:dose_response}
134	\resizebox{\columnwidth}{!}{%
135	\begin{tabular}{lcccccc}
136	\toprule
137	& \multicolumn{2}{c}{\textbf{10\%}} & \multicolumn{2}{c}{\textbf{30\%}} & \multicolumn{2}{c}{\textbf{50\%}} \\
138	\cmidrule(lr){2-3}\cmidrule(lr){4-5}\cmidrule(lr){6-7}
139	\textbf{Strategy} & MMLU & HellaSwag & MMLU & HellaSwag & MMLU & HellaSwag \\
140	\midrule
141	No-filter   & $.6058{\pm}.0002$ & $.6689{\pm}.0006$ & $.6069{\pm}.0007$ & $.6664{\pm}.0018$ & $.6063{\pm}.0012$ & $.6680{\pm}.0005$ \\
142	Binary-ours & $\mathbf{.6079{\pm}.0004}$ & $\mathbf{.6727{\pm}.0007}$ & $\mathbf{.6082{\pm}.0011}$ & $\mathbf{.6725{\pm}.0006}$ & $\mathbf{.6088{\pm}.0009}$ & $\mathbf{.6731{\pm}.0004}$ \\
143	Graduated   & $.6066{\pm}.0010$ & $.6700{\pm}.0014$ & $.6072{\pm}.0008$ & $.6665{\pm}.0012$ & $.6062{\pm}.0008$ & $.6679{\pm}.0001$ \\
144	\bottomrule
145	\end{tabular}}
146	\end{table}
147	
148	At all tested ratios (10--50\%), no-filter MMLU remains above the base model (0.6018), synthetic data at these proportions is therefore net-beneficial rather than harmful.
149	Binary filtering consistently improves over no-filter, with HellaSwag differences significant across all ratios ($p \leq 0.004$, Holm-Bonferroni corrected).
150	MMLU differences are smaller and significant only at 10\% after correction ($p = 0.001$).
151	Graduated weighting is indistinguishable from no-filter at all ratios (MMLU $p \geq 0.27$; HellaSwag $p \geq 0.06$), depth assignments beyond $\Kempirical$ therefore inject noise regardless of contamination severity.
152	Effect sizes diminish 3--6$\times$ relative to the 100\% setting (Section~\ref{sec:filtering}), but the strategy ordering (binary $>$ graduated $\approx$ no-filter) is preserved.
153	
154	\subsection{Cross-Model Filtering Replication}
155	\label{sec:pythia_filtering}
156	
157	To test whether $\Kempirical{=}2$ correctly predicts optimal curation granularity across architectures, we replicate the filtering experiment on Pythia-1.4B (LoRA rank 8, nucleus $p{=}0.9$, $T{=}1.0$, 3 seeds; Table~\ref{tab:pythia_filtering}).
158	
159	\begin{table}[h]
160	\centering
161	\small
162	\caption{Pythia-1.4B filtering replication (3 seeds, mean $\pm$ std). Strategy ordering matches Qwen (binary $>$ no-filter $>$ graduated on MMLU).}
163	\label{tab:pythia_filtering}
164	\begin{tabular}{lcc}
165	\toprule
166	\textbf{Strategy} & \textbf{MMLU} & \textbf{HellaSwag} \\
167	\midrule
168	No-filter & $.2568{\pm}.0012$ & $.5250{\pm}.0008$ \\
169	Binary-ours & $\mathbf{.2585{\pm}.0004}$ & $.5251{\pm}.0001$ \\
170	Graduated$_{0.9}$ & $.2561{\pm}.0009$ & $\mathbf{.5253{\pm}.0007}$ \\
171	\bottomrule
172	\end{tabular}
173	\end{table}
174	
175	The strategy ordering (binary $>$ no-filter $>$ graduated on MMLU) matches Qwen (Section~\ref{sec:filtering}).
176	The small absolute differences reflect the model's near-chance MMLU baseline rather than filtering inefficacy; the consistent ordering across two architectures supports $\Kempirical{=}2$'s predictive value for curation granularity.
177	HellaSwag differences are negligible across all strategies.
178	
179	\subsection{Feature Subset Stability}
180	\label{sec:feature_subset}
181	
182	To test whether $\Kempirical{=}2$ depends on the specific 15D feature combination, we evaluate random feature subsets of varying size on Pythia-1.4B prompt-chain data (Table~\ref{tab:feature_subset}).
183	
184	\begin{table}[h]
185	\centering
186	\small
187	\caption{1v2 $\auc$ by feature subset size (Pythia-1.4B). $\Kempirical{=}2$ ($\auc > \theta{=}0.60$) is robust at $\geq$8 features.}
188	\label{tab:feature_subset}
189	\begin{tabular}{lcccc}
190	\toprule
191	\textbf{Subset} & \textbf{Tested} & \textbf{Pass} & \textbf{Min $\auc$} & \textbf{Mean $\auc$} \\
192	\midrule
193	15D (full) & 1 & 1 & 0.6262 & 0.6262 \\
194	10D        & 5 & 5 & 0.6153 & 0.6191 \\
195	8D         & 5 & 5 & 0.6056 & 0.6159 \\
196	5D         & 5 & 2 & 0.5856 & 0.5998 \\
197	3D (top-3) & 1 & 0 & 0.5871 & 0.5871 \\
198	\bottomrule
199	\end{tabular}
200	\end{table}
201	
202	$\Kempirical{=}2$ holds for all subsets of size $\geq$8 (10/10 pass, min $\auc = 0.6056$), becomes fragile at 5D (2/5 pass), and fails at 3D (top-3 surprisal features alone: $\auc = 0.5871 < \theta$).
203	The boundary does not depend on any specific feature combination but requires sufficient dimensionality ($\geq$8) to capture the multi-faceted distributional shift between generations 1 and 2.
204	
205	\subsection{self\_BLEU Feature Independence}
206	\label{sec:selfbleu_ablation}
207	
208	To verify that $\Kempirical$ does not depend on the self\_BLEU feature (which may reflect stylistic repetition rather than depth-correlated degradation), we compare 15D and 14D (self\_BLEU removed) classifiers across four model configurations (Table~\ref{tab:selfbleu_ablation}).
209	
210	\begin{table}[h]
211	\centering
212	\small
213	\caption{15D vs.\ 14D (self\_BLEU removed) 1v2 $\auc$ with bootstrap 95\% CIs. Removing self\_BLEU does not change $\Kempirical$ for any configuration. Maximum $|\Delta\auc| = 0.0031$, within bootstrap CI width (${\sim}0.018$).}
214	\label{tab:selfbleu_ablation}
215	\resizebox{\columnwidth}{!}{%
216	\begin{tabular}{lcccc}
217	\toprule
218	\textbf{Model} & $\Kempirical$ & \textbf{15D $\auc$ [CI]} & \textbf{14D $\auc$ [CI]} & $\Delta$ \\
219	\midrule
220	Qwen-base   & 2/2 & $.6288$ $[.620,\,.638]$ & $.6258$ $[.616,\,.635]$ & $-.0031$ \\
221	Pythia-1.4B  & 2/2 & $.8840$ $[.878,\,.890]$ & $.8830$ $[.876,\,.889]$ & $-.0010$ \\
222	LLaMA-8B     & 2/2 & $.6075$ $[.598,\,.617]$ & $.6074$ $[.598,\,.617]$ & $-.0001$ \\
223	Mistral-7B   & 1/1 & $.5902$ $[.580,\,.600]$ & $.5903$ $[.580,\,.600]$ & $+.0002$ \\
224	\bottomrule
225	\end{tabular}}
226	\end{table}
227	
228	All four configurations preserve their $\Kempirical$ under 14D, with negligible AUC change ($|\Delta| \leq 0.003$).
229	The self\_BLEU feature contributes minimally to the depth boundary; $\Kempirical{=}2$ is driven by surprisal and entropy features rather than lexical repetition statistics.
230	
231	\subsection{Wikipedia Domain: Scorer Confound Resolution}
232	\label{sec:wiki_domain}
233	
234	Under same-family scoring (Qwen-1.5B scorer), Wikipedia $\Kempirical$ appeared to exhibit model-family dependence: Qwen generators (1.5B and 7B) yielded $\Kempirical{=}2$, while all four non-Qwen models yielded $\Kempirical{=}1$ (Table~\ref{tab:wiki_domain}).
235	A scorer confound ablation resolves this apparent split.
236	Rescoring the same Qwen-7B Wikipedia text with Pythia-1.4B reduces 1v2 $\auc$ from $0.611$ to $0.587$ ($\Delta = -2.4$\,pp), dropping $\Kempirical$ from 2 to 1.
237	With the scorer confound controlled, all six models yield $\Kempirical{=}1$ on Wikipedia, and the domain ordering simplifies to: arXiv ($\Kempirical{=}3$) $>$ C4 ($\Kempirical{=}2$) $>$ Wikipedia ($\Kempirical{=}1$).
238	
239	\begin{table}[h]
240	\centering
241	\small
242	\caption{Wikipedia pairwise $\auc$ across 6 models. $^\dagger$Qwen rows use same-family scorer (Qwen-1.5B); cross-family scoring (Pythia-1.4B) reduces Qwen-7B to $\Kempirical{=}1$ ($\Delta = -2.4$\,pp), resolving the apparent family split.}
243	\label{tab:wiki_domain}
244	\resizebox{\columnwidth}{!}{%
245	\begin{tabular}{llccccc}
246	\toprule
247	\textbf{Model} & \textbf{Family} & \textbf{0v1} & \textbf{1v2} & \textbf{2v3} & $\Kempirical$ & \textbf{Scorer} \\
248	\midrule
249	Qwen-1.5B (base) & Qwen & ---  & .619 & .550 & 2$^\dagger$ & Qwen-1.5B \\
250	Qwen-1.5B (base) & Qwen & ---  & .599 & ---  & 1 & Pythia-1.4B \\
251	Qwen-7B          & Qwen & .967 & .611 & .556 & 2$^\dagger$ & Qwen-1.5B \\
252	Qwen-7B          & Qwen & ---  & .587 & ---  & 1 & Pythia-1.4B \\
253	\midrule
254	Pythia-1.4B   & non-Qwen & .975 & .585 & .545 & 1 & Qwen-1.5B \\
255	OLMo-1B       & non-Qwen & .993 & .499 & .501 & 1 & Qwen-1.5B \\
256	LLaMA-3.1-8B  & non-Qwen & .932 & .595 & .539 & 1 & Qwen-1.5B \\
257	Mistral-7B    & non-Qwen & .961 & .555 & .524 & 1 & Qwen-1.5B \\
258	\bottomrule
259	\multicolumn{7}{l}{\footnotesize $^\dagger$Same-family scorer; cross-family scoring yields $\Kempirical{=}1$.}
260	\end{tabular}}
261	\end{table}
262	
263	\paragraph{Per-fold transparency.}
264	For Qwen-1.5B, cross-family scoring (Pythia-1.4B) yields $\auc$(1v2) $= 0.5994$, with per-fold values $[0.596, 0.606, 0.600, 0.603, 0.592]$ (2/5 folds marginally above $\theta = 0.60$).
265	The aggregate mean falls below $\theta$, confirming $\Kempirical{=}1$.
266	For Qwen-7B, the corresponding $\auc$ drops further to $0.587$.
267	
268	\subsection{ArXiv Cross-Scorer Bootstrap CIs}
269	\label{sec:arxiv_crossscorer_ci}
270	
271	\begin{table}[h]
272	\centering
273	\small
274	\caption{Bootstrap 95\% CI for arXiv cross-scorer (Pythia-1.4B) 2v3 boundary $\auc$ (10{,}000 resamples). Point estimates classify 3/4 generators as $\Kempirical{=}3$; strict CI lower-bound criterion confirms 2/4.}
275	\label{tab:arxiv_crossscorer_ci}
276	\resizebox{\columnwidth}{!}{%
277	\begin{tabular}{lccc}
278	\toprule
279	\textbf{Generator} & \textbf{2v3 $\auc$} & \textbf{95\% CI} & \textbf{CI lower $> \theta$} \\
280	\midrule
281	Qwen-1.5B    & 0.632 & $[0.617,\,0.646]$ & Yes \\
282	LLaMA-3.1-8B & 0.620 & $[0.605,\,0.636]$ & Yes (0.5\,pp margin) \\
283	Mistral-7B   & 0.608 & $[0.593,\,0.622]$ & No \\
284	Qwen-7B      & 0.599 & $[0.584,\,0.613]$ & No \\
285	\bottomrule
286	\end{tabular}}
287	\end{table}
288	
289	\subsection{JSD Decay Analysis}
290	\label{sec:jsd_extended}
291	
292	The token-level JSD between adjacent generations reveals two distinct decay regimes (Figure~\ref{fig:jsd_decay}).
293	For C4 web text, 0v1 JSD exceeds 1v2 by 6--56$\times$ across all 8 models (1B--14B) with $\Kempirical{=}2$ (median cliff ratio ${\sim}$15$\times$), and subsequent pairs converge to a noise floor of ${\sim}$0.003--0.005.
294	Fitting $\jsd(k, k{+}1) \propto e^{-\lambda k}$ yields $\lambda \approx 2.2$--$3.5$ for C4 (mean ${\approx}\,2.9$), consistent with rapid mixing of $G_\delta$ toward its stationary distribution.
295	These decay rates represent qualitative characterizations from 5-point curves rather than precise estimates.
296	The empirical decay rate $\lambda$ is consistent within each domain but varies across domains: C4 yields $\lambda \approx 2.9$, Wikipedia $\lambda \approx 3.1$ (excluding OLMo, whose $\lambda = 6.3$ reflects a capacity-limited collapse: 0v1 $\jsd = 0.169$ with near-complete information loss at the first step, the exponential fit is therefore unreliable), and arXiv $\lambda \approx 1.0$.
297	This cross-model consistency indicates that the contraction rate of $G_\delta$ is governed primarily by the structure of the input domain rather than the model architecture.
298	ArXiv text decays ${\sim}$3$\times$ slower than C4 ($\lambda \approx 1.0$ vs.\ $2.9$), with a correspondingly higher convergence floor (${\sim}$0.007--0.009 vs.\ ${\sim}$0.003--0.004).
299	Formulaic structural features (LaTeX formatting, citation patterns, section templates) degrade more slowly under autoregressive generation and supply persistent depth-distinguishing signal, this accounts for the elevated $\Kempirical{=}3$.
300	The retrain-chain exhibits a fundamentally different profile: $\lambda = 0.285$ with a cliff ratio of only 1.31$\times$ and no sharp drop between adjacent pairs (Figure~\ref{fig:retrain_decay}).
301	This gradual, sustained divergence reflects cumulative model-adaptation artifacts rather than text-intrinsic information loss, further supporting the distinction between prompt-chain and retrain-chain $\Kempirical$ (Appendix~\ref{sec:boundary_extended}).
302	
303	\begin{figure}[h]
304	\centering
305	\includegraphics[width=\columnwidth]{figures/fig_retrain_decay.png}
306	\caption{Retrain-chain AUC decay across 7 generation pairs (Qwen2.5-1.5B LoRA). Unlike prompt-chain (sharp cliff at 0v1$\to$1v2), retrain-chain AUC decays gradually from 0.984 to 0.641, with all pairs above $\theta{=}0.60$. Error bars: 95\% CI from 5-fold CV. Dashed line: $\theta{=}0.60$; extrapolated 7v8 $\approx 0.57$ (below $\theta$), suggesting $\Kempirical{=}7$ is near the ceiling.}
307	\label{fig:retrain_decay}
308	\end{figure}
309	
310	\subsection{Boundary Cases and Scale Effect}
311	\label{sec:boundary_extended}
312	
313	Of 9 tested model configurations on C4, 8 yield $\Kempirical{=}2$; Mistral-7B is the only sub-2 exception ($\Kempirical{=}1$; 1v2 $\auc = 0.594$, CI $[0.584, 0.603]$), validating $\theta{=}0.60$ as an effective discriminator (gap: $0.594$ vs.\ $0.611$--$0.696$).
314	Mistral's cross-domain profile reinforces the domain-governed interpretation: despite $\Kempirical{=}1$ on C4 and Wikipedia, it yields $\Kempirical{=}2$ on code and $\Kempirical{=}3$ on arXiv (1v2 $\auc = 0.820$, 2v3 $= 0.628$), and this profile persists under cross-scorer validation (Pythia-1.4B scorer: C4 $\Kempirical{=}1$, arXiv $\Kempirical{=}3$ (2v3 $\auc = 0.608$, CI $[0.593, 0.622]$)), domain lexical diversity can therefore rescue even web-text one-wash generators (Table~\ref{tab:domain_kstar}).
315	Larger models produce more human-like text, reducing 0v1 JSD: 0.16--0.29 at $\leq$1.5B, 0.077--0.13 at 7--14B.
316	However, Qwen-14B still yields $\Kempirical{=}2$ (1v2 $\auc = 0.621$, CI $[0.612, 0.630]$), with 0v1 $\auc = 0.960$ comparable to Qwen-7B ($0.964$), scale in the 1B--14B range therefore does not shift the discrimination boundary.
317	
318	\paragraph{Sample-size control.}
319	As a sample-size control, subsampling C4 to $n{=}2{,}200$ (matching arXiv) yields $\Kempirical{=}1$ (1v2 $\auc = 0.601$, CI $[0.586, 0.616]$).
320	Reduced sample size widens confidence intervals and produces more conservative $\Kempirical$ estimates, arXiv's $\Kempirical{=}3$ at the same sample size therefore reflects genuine domain signal rather than a statistical artifact of smaller training sets.
321	
322	\subsection{LaTeX Markup Ablation (arXiv)}
323	\label{sec:latex_ablation}
324	
325	To disentangle content-level depth signal from formatting artifacts on arXiv, we strip all LaTeX markup (commands, environments, inline math delimiters) and re-extract features from the plain-text residual (Qwen-1.5B continuation, $n{=}2{,}200$; Table~\ref{tab:latex_ablation}).
326	
327	\begin{table}[h]
328	\centering
329	\small
330	\caption{arXiv pairwise $\auc$ with and without LaTeX markup (Qwen-1.5B continuation). Removing formatting reduces 2v3 by ${\sim}$1.8\,pp but $\Kempirical$ remains at 3 (CI lower $> \theta$). LaTeX stripping fraction increases with depth (0.6\% at depth 0, 4.6\% at depth 5), deeper generations therefore produce proportionally more formatting tokens.}
331	\label{tab:latex_ablation}
332	\resizebox{\columnwidth}{!}{%
333	\begin{tabular}{lccr}
334	\toprule
335	\textbf{Pair} & \textbf{Original} & \textbf{Stripped} & $\Delta$ \\
336	\midrule
337	0v1 & 0.9946 & 0.9948 & $+$0.0002 \\
338	1v2 & 0.8580 & 0.8297 & $-$0.028 \\
339	2v3 & 0.6427 $[0.628,\,0.658]$ & 0.6248 $[0.610,\,0.640]$ & $-$0.018 \\
340	3v4 & 0.5437 & 0.5468 & $+$0.003 \\
341	\midrule
342	$\Kempirical$ & 3 & 3 & --- \\
343	\bottomrule
344	\end{tabular}}
345	\end{table}
346	
347	Content-level statistical properties (surprisal distribution, vocabulary diversity) account for the large majority of the depth signal; LaTeX formatting contributes a modest but measurable increment (${\sim}$1.8\,pp at the boundary pair).
348	The depth-correlated increase in LaTeX stripping fraction (depth 0: $-$0.6\%, depth 5: $-$4.6\%) indicates that autoregressive generation progressively introduces formatting tokens, consistent with mode-seeking behavior in structured text.
349	
350	\subsection{Statistical Power Analysis}
351	\label{sec:power_curve}
352	
353	To characterize the minimum sample size required for reliable $\Kempirical$ determination, we subsample C4 at $n \in \{500, 1000, 2000, 3000, 4000, 5000\}$ and measure 1v2 AUC stability across 10 resamples per size (Qwen-1.5B-base continuation, 5-fold GroupKFold; Table~\ref{tab:power_curve}, Figure~\ref{fig:power_curve}).
354	
355	\begin{table}[h]
356	\centering
357	\small
358	\caption{Subsampling power analysis for $\Kempirical{=}2$ determination (C4, Qwen-1.5B-base, 10 resamples per $n$). Detection probability: fraction of resamples where 1v2 $\auc > \theta{=}0.60$.}
359	\label{tab:power_curve}
360	\begin{tabular}{rccc}
361	\toprule
362	$n$ & \textbf{Mean 1v2 $\auc$} & \textbf{Std} & \textbf{Detection Prob.} \\
363	\midrule
364	500 & 0.581 & 0.018 & 20\% \\
365	1{,}000 & 0.591 & 0.014 & 30\% \\
366	2{,}000 & 0.610 & 0.009 & 100\% \\
367	3{,}000 & 0.617 & 0.005 & 100\% \\
368	4{,}000 & 0.622 & 0.004 & 100\% \\
369	5{,}000 & 0.629 & 0.000 & 100\% \\
370	\bottomrule
371	\end{tabular}
372	\end{table}
373	
374	\begin{figure}[h]
375	\centering
376	\includegraphics[width=\columnwidth]{figures/fig_power_curve.png}
377	\caption{$\Kempirical{=}2$ detection rate (left axis, blue) and mean 1v2 $\auc$ (right axis, green) as a function of sample size $n$. Detection rate reaches 100\% at $n{=}2{,}000$; the 80\% power threshold (dotted purple) is crossed between $n{=}1{,}000$ and $n{=}2{,}000$. Error bars: $\pm$1 std over 10 resamples. The dashed red line marks $\theta{=}0.60$.}
378	\label{fig:power_curve}
379	\end{figure}
380	
381	Detection rate jumps from 20\% ($n{=}500$) to 100\% ($n{=}2{,}000$), with the 80\% power threshold crossed near $n{=}1{,}500$.
382	At $n{=}5{,}000$ (the sample size used in all main experiments), variance is zero across resamples, our results are therefore well above the minimum required for reliable boundary estimation.
383	The sharp transition reflects the proximity of the 1v2 AUC to $\theta$: small increases in $n$ reduce variance sufficiently to move all resamples above the threshold.
384	
385	\subsection{Feature Group Ablation}
386	\label{sec:feature_ablation}
387	
388	To assess the relative contribution of each feature group to depth discrimination, we train a plain LightGBM classifier (\texttt{n\_estimators}$=$200, \texttt{max\_depth}$=$6; distinct from the OBD-LightGBM used in Section~\ref{sec:method}) on the 1\,vs.\,2 task using (a) each feature group alone (\emph{single}) and (b) the full 15D set minus one group (\emph{leave-one-out}).
389	Representative models per domain: LLaMA-3.1-8B (C4), Qwen-1.5B continuation (arXiv), and the domain ablation configuration (Wikipedia).
390	
391	\begin{figure}[h]
392	\centering
393	\includegraphics[width=\columnwidth]{figures/fig_feature_ablation.pdf}
394	\caption{Feature group ablation heatmap for 1\,vs.\,2 classification AUC. \emph{Left}: single-group performance. \emph{Right}: leave-one-out performance. Surprisal (base) features are the dominant signal on arXiv (single AUC $= 0.809$) but provide only weak marginal signal on C4 and Wikipedia.}
395	\label{fig:feature_ablation}
396	\end{figure}
397	
398	\begin{table}[h]
399	\centering
400	\small
401	\caption{Feature group ablation for 1\,vs.\,2 classification (AUC). \textbf{Single}: using only features from one group. \textbf{Leave-one-out}: removing one group from the full 15D feature set. $\Delta$ denotes the AUC drop from the full model. Classifier: plain LightGBM (\texttt{n\_estimators}$=$200, \texttt{max\_depth}$=$6), distinct from the OBD-LightGBM pipeline; AUC values are not directly comparable to Table~\ref{tab:kstar_ci}.}
402	\label{tab:feature_ablation}
403	\resizebox{\columnwidth}{!}{%
404	\begin{tabular}{l ccc ccc}
405	\toprule
406	& \multicolumn{3}{c}{\textbf{Single Group}} & \multicolumn{3}{c}{\textbf{Leave-One-Out ($\Delta$)}} \\
407	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
408	Feature Group & C4 & arXiv & Wiki & C4 & arXiv & Wiki \\
409	\midrule
410	Surprisal (base) & 0.597 & 0.809 & 0.581 & 0.601 ($-$0.007) & 0.828 ($-$0.031) & 0.616 ($-$0.003) \\
411	Surprisal (deriv.) & 0.590 & 0.789 & 0.590 & 0.612 (+0.003) & 0.856 ($-$0.003) & 0.623 (+0.004) \\
412	Lexical diversity & 0.550 & 0.691 & 0.557 & 0.608 ($-$0.001) & 0.855 ($-$0.005) & 0.614 ($-$0.005) \\
413	Freq. distribution & 0.533 & 0.684 & 0.564 & 0.604 ($-$0.005) & 0.851 ($-$0.009) & 0.612 ($-$0.007) \\
414	\midrule
415	Full (15D) & 0.609 & 0.860 & 0.619 & \multicolumn{3}{c}{---} \\
416	\bottomrule
417	\end{tabular}}
418	\end{table}
419	
420	Surprisal (base) features dominate on arXiv (single-group AUC $= 0.809$; LOO drop $= 0.031$, the largest across all domain--group combinations), consistent with the persistent surprisal-distribution signal in structured academic text.
421	On C4 and Wikipedia, all LOO drops are small ($\leq 0.007$, within cross-fold standard deviation), no single feature group is therefore individually critical for the weaker low-$\Kempirical$ signal.
422	Removing surprisal derivatives increases AUC on C4 (+0.003) and Wikipedia (+0.004). This indicates partial redundancy with the base surprisal group in low-$\Kempirical$ domains.
423	
424	\subsection{Classifier Choice: McNemar Test}
425	\label{sec:mcnemar_baselines}
426	
427	To verify that depth discriminability is driven by the 15D feature representation rather than classifier choice, we compare OBD-LightGBM against three baseline classifiers (logistic regression, linear SVC, random forest) on the depth-1 vs.\ depth-2 binary classification task using McNemar's test with continuity correction on 5-fold GroupKFold out-of-fold predictions (Table~\ref{tab:mcnemar_obd_baselines}).
428	Of 36 comparisons, 31 are non-significant ($p \geq 0.05$), and all five significant results concentrate in two model $\times$ domain conditions.
429	For LLaMA-8B on C4, all three baselines significantly outperform OBD ($p \leq 0.001$), likely reflecting LightGBM overfitting on the relatively noisy 8B-generated features rather than a systematic classifier advantage.
430	For Qwen-1.5B on Wikipedia, OBD outperforms both linear classifiers ($p < 0.001$) but not random forest ($p = 0.655$).
431	
432	\begin{table*}[h]
433	\centering
434	\small
435	\caption{McNemar test $p$-values comparing OBD-LightGBM against baseline classifiers on the depth-1 vs.\ depth-2 binary classification task (5-fold GroupKFold, out-of-fold predictions). Classifier accuracy shown in parentheses. Significant results ($p < 0.05$) are \textbf{bold}; $^{*}p<0.05$, $^{**}p<0.01$, $^{***}p<0.001$.}
436	\label{tab:mcnemar_obd_baselines}
437	\resizebox{\textwidth}{!}{%
438	\begin{tabular}{llcccc}
439	\toprule
440	\textbf{Model} & \textbf{Domain} & \textbf{OBD Acc.} & \textbf{vs.\ LogReg} & \textbf{vs.\ LinearSVC} & \textbf{vs.\ RandomForest} \\
441	\midrule
442	Qwen-1.5B-base & C4    & .592 & .232 (.598)            & .605 (.595)              & .271 (.597) \\
443	Pythia-1.4B     & C4    & .631 & $\mathbf{.033^{*}}$ (.621) & .105 (.624)              & .451 (.628) \\
444	LLaMA-8B        & C4    & .573 & $\mathbf{6.2{\times}10^{-5\,***}}$ (.592) & $\mathbf{1.1{\times}10^{-4\,***}}$ (.591) & $\mathbf{.001^{**}}$ (.586) \\
445	\midrule
446	Qwen-1.5B      & Wiki  & .588 & $\mathbf{9.4{\times}10^{-4\,***}}$ (.570) & $\mathbf{2.3{\times}10^{-4\,***}}$ (.568) & .655 (.590) \\
447	Pythia          & Wiki  & .560 & .180 (.567)            & .540 (.564)              & .369 (.564) \\
448	OLMo            & Wiki  & .500 & .868 (.502)            & .705 (.503)              & .751 (.502) \\
449	LLaMA-8B        & Wiki  & .573 & .252 (.579)            & .270 (.579)              & .110 (.580) \\
450	\midrule
451	Qwen-1.5B      & arXiv & .781 & .156 (.774)            & .079 (.772)              & .364 (.777) \\
452	Pythia          & arXiv & .733 & .232 (.727)            & .384 (.728)              & .735 (.732) \\
453	OLMo            & arXiv & .493 & .520 (.487)            & .681 (.489)              & .759 (.496) \\
454	Qwen-7B         & arXiv & .757 & .160 (.749)            & .327 (.751)              & .733 (.758) \\
455	Mistral-7B      & arXiv & .742 & .524 (.738)            & .633 (.739)              & .225 (.748) \\
456	\bottomrule
457	\end{tabular}%
458	}
459	
460	\vspace{4pt}
461	\footnotesize
462	36 comparisons total. 5/36 reach $p < 0.05$; 4/36 reach $p < 0.01$.
463	The predominance of non-significant results confirms that depth discriminability is feature-driven, not classifier-driven.
464	\end{table*}
465	
466	\subsection{Domain Lexical Statistics}
467	\label{sec:domain_lexical_stats}
468	
469	Table~\ref{tab:domain-ttr-entropy} reports type-token ratio (TTR) and vocabulary entropy across three domains and six depth levels.
470	The TTR ordering at depth 0 (arXiv $>$ C4 $>$ Wikipedia) aligns with the $\Kempirical$ ordering, with large effect sizes (Cohen's $d = 1.52$ for arXiv vs.\ Wikipedia).
471	Vocabulary entropy shows a partial reversal at depth 0: C4 ($H = 6.225$) falls below Wikipedia ($H = 6.408$), while arXiv remains highest ($H = 6.853$).
472	This reversal likely reflects C4's greater content heterogeneity (higher variance: $\sigma = 0.706$ vs.\ $0.284$), which inflates TTR but depresses mean entropy.
473	As depth increases, all domains converge, with arXiv exhibiting the steepest decline, consistent with its higher $\Kempirical$ and slower convergence to the stationary distribution.
474	
475	\begin{table*}[h]
476	\centering
477	\small
478	\caption{Type-Token Ratio (TTR) and vocabulary entropy across three domains and generation depths.
479	At depth~0 (original human text), arXiv exhibits the highest lexical diversity (TTR\,=\,0.755, $H$\,=\,6.853),
480	followed by C4 and Wikipedia.
481	As depth increases, all domains converge, with arXiv showing the steepest decline.
482	Cohen's $d$ values are computed at depth~0 for pairwise domain comparisons.}
483	\label{tab:domain-ttr-entropy}
484	\begin{tabular}{ll rrr rrr}
485	\toprule
486	& & \multicolumn{3}{c}{\textbf{TTR}} & \multicolumn{3}{c}{\textbf{Vocab Entropy ($H$)}} \\
487	\cmidrule(lr){3-5} \cmidrule(lr){6-8}
488	\textbf{Depth} & $N$ & \textbf{Wiki} & \textbf{C4} & \textbf{arXiv} & \textbf{Wiki} & \textbf{C4} & \textbf{arXiv} \\
489	\midrule
490	0 & 5k/5k/2.2k & .665\tpm.061 & .720\tpm.105 & \textbf{.755}\tpm.055 & 6.408\tpm.284 & 6.225\tpm.706 & \textbf{6.853}\tpm.295 \\
491	1 &             & .655\tpm.121 & .707\tpm.149 & \textbf{.732}\tpm.098 & 5.932\tpm.843 & 5.737\tpm1.189 & \textbf{6.113}\tpm.655 \\
492	2 &             & .647\tpm.145 & .676\tpm.159 & \textbf{.677}\tpm.131 & 5.784\tpm.905 & 5.774\tpm1.139 & \textbf{5.998}\tpm.967 \\
493	3 &             & .645\tpm.159 & \textbf{.662}\tpm.164 & .635\tpm.134 & 5.664\tpm1.085 & 5.743\tpm1.161 & \textbf{5.964}\tpm.933 \\
494	4 &             & .636\tpm.164 & \textbf{.647}\tpm.169 & .621\tpm.140 & 5.660\tpm1.062 & 5.758\tpm1.167 & \textbf{5.898}\tpm.942 \\
495	5 &             & .632\tpm.172 & \textbf{.636}\tpm.175 & .618\tpm.150 & 5.593\tpm1.130 & 5.772\tpm1.141 & \textbf{5.816}\tpm.968 \\
496	\midrule
497	\multicolumn{8}{l}{\textit{Cohen's $d$ at depth 0 (positive $=$ second domain higher):}} \\
498	\multicolumn{2}{l}{C4 vs.\ Wiki}   & \multicolumn{3}{c}{$d = +0.65$} & \multicolumn{3}{c}{$d = -0.34$} \\
499	\multicolumn{2}{l}{arXiv vs.\ C4}  & \multicolumn{3}{c}{$d = +0.37$} & \multicolumn{3}{c}{$d = +1.03$} \\
500	\multicolumn{2}{l}{arXiv vs.\ Wiki} & \multicolumn{3}{c}{$d = +1.52$} & \multicolumn{3}{c}{$d = +1.55$} \\
501	\bottomrule
502	\end{tabular}
503	\end{table*}
504	
505	\subsection{Leave-One-Family-Out Threshold Validation}
506	\label{sec:theta_lofo}
507	
508	To validate $\theta{=}0.60$ without circular reasoning, we perform leave-one-family-out (LOFO) cross-validation: each fold removes one architecture family, derives $\hat{\theta}$ as the midpoint between $\min(\auc_{1v2})$ and $\max(\auc_{2v3})$ over the remaining families, then predicts $\Kempirical$ for the held-out models.
509	Table~\ref{tab:theta_lofo} reports results across all three domains.
510	
511	On C4, 8/9 held-out predictions agree with the original $\Kempirical$ assignment at $\theta{=}0.60$ (agreement: 89\%).
512	The single mismatch is Qwen-1.5B-RW (rewrite mode), whose 2v3 AUC of 0.5893 lies above the LOFO-derived $\hat{\theta}{=}0.5725$ but below the global $\theta{=}0.60$; this configuration is also the sole rewrite-mode model, the discrepancy is therefore attributable to mode rather than threshold instability.
513	The derived $\hat{\theta}$ values span $[0.5725, 0.6004]$, and $\theta{=}0.60$ falls within this range.
514	
515	ArXiv corroborates with 6/6 agreement (100\%), though the wide $\hat{\theta}$ range $[0.5735, 0.7296]$ reflects OLMo-1B's near-chance performance ($\auc_{1v2}{=}0.503$), which inflates the gap midpoint when OLMo is included in the training fold.
516	
517	Wikipedia yields only 1/6 agreement (17\%).
518	This failure is expected: most models produce near-chance 1v2 AUC on Wikipedia ($0.499$--$0.619$), so the gap between $\min(\auc_{1v2})$ and $\max(\auc_{2v3})$ is narrow or inverted, the gap-based threshold derivation is therefore invalid.
519	Wikipedia's $\Kempirical{=}1$ assignment is independently confirmed by the global $\theta{=}0.60$ criterion (Section~\ref{sec:cross_domain}); LOFO simply cannot validate this because the method requires a clear AUC discontinuity between boundary and non-boundary pairs.
520	
521	\begin{table*}[t]
522	\centering
523	\small
524	\caption{Leave-One-Family-Out (LOFO) cross-validation of $\theta$ across three domains. Each fold holds out one architecture family, derives $\hat{\theta}$ as the midpoint between $\min(\text{AUC}_{1\text{v}2})$ and $\max(\text{AUC}_{2\text{v}3})$ over the remaining families, and predicts $K^*$ for held-out models. C4 (primary): 8/9 agreement (89\%). arXiv: 6/6 (100\%). Wikipedia: 1/6 (17\%, see text).}
525	\label{tab:theta_lofo}
526	\begin{tabular}{l l l c c c c c c}
527	\toprule
528	Domain & Held-out & Model & $\text{AUC}_{1\text{v}2}$ & $\text{AUC}_{2\text{v}3}$ & $\hat{\theta}$ & $K^*_{\hat{\theta}}$ & $K^*_{0.60}$ & Match \\
529	\midrule
530	C4 & Pythia & Pythia-1.4B & 0.6539 & 0.5515 & 0.5914 & 2 & 2 & \cmark \\
531	 & OLMo & OLMo-1B & 0.6146 & 0.5497 & 0.5914 & 2 & 2 & \cmark \\
532	 & Qwen & Qwen-1.5B-RW & 0.6957 & 0.5893 & 0.5725 & 3 & 2 & \xmark \\
533	 &  & Qwen-7B & 0.6178 & 0.5460 & 0.5725 & 2 & 2 & \cmark \\
534	 &  & Qwen-1.5B-base & 0.6262 & 0.5496 & 0.5725 & 2 & 2 & \cmark \\
535	 &  & Qwen-1.5B-cont & 0.6114 & 0.5609 & 0.5725 & 2 & 2 & \cmark \\
536	 &  & Qwen-14B & 0.6210 & 0.5494 & 0.5725 & 2 & 2 & \cmark \\
537	 & LLaMA & LLaMA-3.1-8B & 0.6123 & 0.5274 & 0.5914 & 2 & 2 & \cmark \\
538	 & Mistral & Mistral-7B & 0.5935 & 0.5402 & 0.6004 & 1 & 1 & \cmark \\
539	\cmidrule{2-9}
540	 & \multicolumn{7}{l}{$\hat{\theta}$ $\in$ [0.5725, 0.6004], agreement: 8/9 (89\%)} \\
541	\midrule
542	arXiv & Pythia & Pythia-1.4B & 0.8047 & 0.6545 & 0.5735 & 3 & 3 & \cmark \\
543	 & OLMo & OLMo-1B & 0.5034 & 0.5069 & 0.7296 & 1 & 1 & \cmark \\
544	 & Qwen & Qwen-1.5B & 0.8581 & 0.6436 & 0.5789 & 3 & 3 & \cmark \\
545	 &  & Qwen-7B & 0.8347 & 0.6255 & 0.5789 & 3 & 3 & \cmark \\
546	 & LLaMA & LLaMA-3.1-8B & 0.8447 & 0.6215 & 0.5789 & 3 & 3 & \cmark \\
547	 & Mistral & Mistral-7B & 0.8201 & 0.6275 & 0.5789 & 3 & 3 & \cmark \\
548	\cmidrule{2-9}
549	 & \multicolumn{7}{l}{$\hat{\theta}$ $\in$ [0.5735, 0.7296], agreement: 6/6 (100\%)} \\
550	\midrule
551	Wikipedia & Pythia & Pythia-1.4B & 0.5846 & 0.5445 & 0.5274 & 3 & 1 & \xmark \\
552	 & OLMo & OLMo-1B & 0.4986 & 0.5012 & 0.5557 & 1 & 1 & \cmark \\
553	 & Qwen & Qwen-1.5B & 0.6193 & 0.5498 & 0.5215 & 4 & 2 & \xmark \\
554	 &  & Qwen-7B & 0.6108 & 0.5562 & 0.5215 & 4 & 2 & \xmark \\
555	 & LLaMA & LLaMA-3.1-8B & 0.5954 & 0.5392 & 0.5274 & 3 & 1 & \xmark \\
556	 & Mistral & Mistral-7B & 0.5552 & 0.5236 & 0.5274 & 2 & 1 & \xmark \\
557	\cmidrule{2-9}
558	 & \multicolumn{7}{l}{$\hat{\theta}$ $\in$ [0.5215, 0.5557], agreement: 1/6 (17\%)} \\
559	\bottomrule
560	\end{tabular}
561	\end{table*}
562	
563	\subsection{Code Domain Results}
564	\label{sec:code_domain}
565	
566	\begin{table}[h]
567	\centering
568	\small
569	\caption{Code domain (Python, CodeSearchNet~\cite{husain2019codesearchnet}) pairwise AUC for Qwen2.5-1.5B. $\Kempirical{=}2$: 1v2 exceeds $\theta{=}0.60$; 2v3 drops to chance. JSD ratio (1v2/2v3) $= 11.7\times$, comparable to C4's cliff structure.}
570	\label{tab:code_domain_qwen}
571	\begin{tabular}{l c c c}
572	\toprule
573	Pair & AUC & 95\% CI & JSD \\
574	\midrule
575	0 vs 1 & 0.9388 & [0.929, 0.949] & 0.0814 \\
576	1 vs 2 & 0.7382 & [0.709, 0.767] & 0.0443 \\
577	2 vs 3 & 0.5300 & [0.514, 0.546] & 0.0038 \\
578	3 vs 4 & 0.5022 & [0.486, 0.518] & 0.0033 \\
579	4 vs 5 & 0.5219 & [0.510, 0.534] & 0.0030 \\
580	\midrule
581	\multicolumn{4}{l}{$\Kempirical = 2$ ($\theta = 0.60$)} \\
582	\bottomrule
583	\end{tabular}
584	\end{table}
585	
586	\begin{table}[h]
587	\centering
588	\small
589	\caption{Code domain (Python, CodeSearchNet) cross-model pairwise AUC with 5-fold cross-validated 95\% CIs across five models (four architecture families). Qwen2.5-1.5B/7B, LLaMA-3.1-8B, and Mistral-7B-v0.3 yield $\Kempirical{=}2$ (4/5); Pythia-1.4B yields $\Kempirical{=}1$ (capacity-limited). All models scored by Qwen2.5-1.5B (cross-family for non-Qwen).}
590	\label{tab:code_crossmodel_kstar}
591	\resizebox{\columnwidth}{!}{%
592	\begin{tabular}{l cc cc cc cc cc}
593	\toprule
594	 & \multicolumn{2}{c}{Qwen-1.5B} & \multicolumn{2}{c}{Qwen-7B} & \multicolumn{2}{c}{Pythia-1.4B} & \multicolumn{2}{c}{LLaMA-8B} & \multicolumn{2}{c}{Mistral-7B} \\
595	\cmidrule(lr){2-3}\cmidrule(lr){4-5}\cmidrule(lr){6-7}\cmidrule(lr){8-9}\cmidrule(lr){10-11}
596	 & AUC & 95\% CI & AUC & 95\% CI & AUC & 95\% CI & AUC & 95\% CI & AUC & 95\% CI \\
597	\midrule
598	0v1 & .9388 & [.929,\,.949] & .9051 & [.901,\,.909] & \textbf{.9592} & [.956,\,.963] & .9161 & [.912,\,.920] & .9191 & [.917,\,.921] \\
599	1v2 & \textbf{.7382} & [.709,\,.767]\rlap{$^*$} & .7276 & [.722,\,.733]\rlap{$^*$} & .5983 & [.593,\,.603] & \textbf{.7394} & [.729,\,.750]\rlap{$^*$} & .6152 & [.603,\,.627]\rlap{$^*$} \\
600	2v3 & .5300 & [.514,\,.546] & .5368 & [.522,\,.551] & .5215 & [.509,\,.534] & .5112 & [.502,\,.521] & .5293 & [.520,\,.538] \\
601	3v4 & .5022 & [.486,\,.518] & .5090 & [.504,\,.515] & .5152 & [.503,\,.527] & .5200 & [.506,\,.534] & .5286 & [.518,\,.539] \\
602	4v5 & .5219 & [.510,\,.534] & .5139 & [.501,\,.527] & .5046 & [.491,\,.518] & .4996 & [.493,\,.507] & .5099 & [.504,\,.516] \\
603	\midrule
604	$K^*$ & \multicolumn{2}{c}{\textbf{2}} & \multicolumn{2}{c}{\textbf{2}} & \multicolumn{2}{c}{1} & \multicolumn{2}{c}{\textbf{2}} & \multicolumn{2}{c}{\textbf{2}} \\
605	\bottomrule
606	\multicolumn{11}{@{}p{\linewidth}@{}}{\footnotesize $^*$Permutation $p < 0.001$. $K^*$: max $k$ where $k$v$(k{+}1)$ CI lower bound $> \theta = 0.60$ (Eq.~\ref{eq:kstar}).}
607	\end{tabular}}
608	\end{table}
609	
610	\paragraph{Cross-scorer validation (Code domain).}
611	To rule out scorer confound for Code $\Kempirical{=}2$, we re-evaluate Qwen2.5-1.5B code generations using Pythia-1.4B as the reference scorer (Table~\ref{tab:code_crossscorer}).
612	Cross-family scoring yields $\Kempirical{=}2$ (1v2 $\auc = 0.7197$, five-fold minimum $= 0.6985$, all folds above $\theta$), a decrease of only 1.9\,pp from Qwen self-scoring ($0.7382$).
613	This contrasts with Wikipedia, where same-family scoring inflates $\Kempirical$ from 1 to 2 (Appendix~\ref{sec:wiki_domain}): Code depth signal is robust to scorer choice, while Wikipedia's marginal signal is scorer-sensitive.
614	The scorer confound is therefore domain-specific rather than systematic.
615	
616	\begin{table}[h]
617	\centering
618	\small
619	\caption{Code domain cross-scorer validation: Pythia-1.4B scorer on Qwen2.5-1.5B code generations. $\Kempirical{=}2$ is preserved; five-fold minimum 1v2 $\auc = 0.6985$, well above $\theta{=}0.60$.}
620	\label{tab:code_crossscorer}
621	\begin{tabular}{lcc}
622	\toprule
623	Scorer & 1v2 $\auc$ & 5-fold min \\
624	\midrule
625	Qwen2.5-1.5B (self) & 0.7382 & 0.7093 \\
626	Pythia-1.4B (cross) & 0.7197 & 0.6985 \\
627	\midrule
628	$\Delta$ & \multicolumn{2}{c}{$-1.9$\,pp} \\
629	$\Kempirical$ & \multicolumn{2}{c}{2 (both)} \\
630	\bottomrule
631	\end{tabular}
632	\end{table}
633	
634	\subsection{Borderline Feature Analysis}
635	\label{sec:borderline_analysis}
636	
637	To understand why Mistral-7B yields $\Kempirical{=}1$ while other C4 models yield $\Kempirical{=}2$, we compute per-feature Cohen's $d$ (depth-1 vs.\ depth-2) and LightGBM feature importances across six C4 configurations spanning the full 1v2 AUC range (0.594--0.884).
638	
639	Mistral-7B exhibits the lowest depth-0 mean surprisal (2.32 vs.\ 2.90--3.02 for other models), the scorer model therefore already finds Mistral's output highly predictable.
640	This compressed baseline limits the dynamic range available for detecting inter-generational degradation: all 15 Cohen's $d$ values are weak ($\bar{|d|} = 0.112$; Table~\ref{tab:cohens_d_full}), and no single feature exceeds 13\% of total classifier importance.
641	The borderline models (LLaMA-8B, Pythia at $T{=}1.2$) show a similar pattern at slightly higher effect sizes.
642	
643	Greedy decoding is qualitatively distinct: Pythia-greedy achieves 0.884 AUC via lexical collapse (hapax ratio $d = -1.056$, capturing 47\% of importance), a signal absent under sampling-based generation where all non-greedy models rely on surprisal variability features.
644	
645	\begin{table*}[h]
646	\centering
647	\small
648	\caption{Feature-level summary of C4 1v2 classification across model categories. Imp.\ = normalized LightGBM gain importance (\%). $\bar{|d|}$ = mean absolute Cohen's $d$ over all 15 features. $\Delta\text{surp}_{1\to2}$: change in mean surprisal from depth 1 to depth 2.}
649	\label{tab:borderline_features}
650	\begin{tabular}{@{}llc lcc@{}}
651	\toprule
652	Category & Model & AUC & Top-3 Features (Imp.\%) & $\bar{|d|}$ & $\Delta\text{surp}_{1\to2}$ \\
653	\midrule
654	Strong & Pythia-greedy & 0.884 & hapax\_ratio (47), surp\_mean (11), low\_freq\_ratio (8) & 0.365 & $-$0.160 \\
655	Strong & Pythia-nuc09 & 0.677 & surp\_std (20), freq\_entropy (11), surp\_d1\_std (8) & 0.170 & $-$0.196 \\
656	Strong & Qwen-1.5B-base & 0.626 & surp\_std (13), freq\_entropy (10), surp\_mean (9) & 0.125 & $-$0.159 \\
657	\midrule
658	Borderline & Pythia-$T{=}1.2$ & 0.617 & surp\_std (15), freq\_entropy (10), surp\_kurt (8) & 0.112 & $-$0.059 \\
659	Borderline & LLaMA-3.1-8B & 0.612 & surp\_std (12), surp\_d1\_std (10), freq\_entropy (9) & 0.137 & $-$0.215 \\
660	\midrule
661	Below $\theta$ & Mistral-7B & 0.594 & surp\_std (13), freq\_entropy (9), surp\_d1\_skew (9) & 0.112 & $-$0.086 \\
662	\bottomrule
663	\end{tabular}
664	\end{table*}
665	
666	\begin{table*}[h]
667	\centering
668	\scriptsize
669	\caption{Cohen's $d$ (depth-1 vs.\ depth-2) for all 15 features across six C4 models. \textbf{Bold}: largest $|d|$ in each row. Greedy decoding produces qualitatively different effect sizes via lexical collapse (hapax\_ratio, low\_freq\_ratio); under sampling, surprisal variability features (surp\_std, surp\_d1\_std, surp\_d2\_std) carry the dominant signal.}
670	\label{tab:cohens_d_full}
671	\begin{tabular}{@{}lrrrrrr@{}}
672	\toprule
673	Feature & \rotatebox{60}{Pythia-greedy} & \rotatebox{60}{Pythia-nuc09} & \rotatebox{60}{Qwen-1.5B-base} & \rotatebox{60}{Pythia-$T{=}1.2$} & \rotatebox{60}{LLaMA-3.1-8B} & \rotatebox{60}{Mistral-7B} \\
674	\midrule
675	surp\_mean & \textbf{$-$0.416} & $-$0.306 & $-$0.244 & $-$0.103 & $-$0.263 & $-$0.152 \\
676	surp\_std & $-$0.301 & \textbf{$-$0.370} & $-$0.229 & $-$0.268 & $-$0.316 & $-$0.190 \\
677	surp\_skew & \textbf{$+$0.468} & $+$0.086 & $+$0.085 & $-$0.217 & $+$0.049 & $+$0.103 \\
678	surp\_kurt & \textbf{$+$0.433} & $+$0.102 & $+$0.071 & $-$0.188 & $+$0.031 & $+$0.124 \\
679	surp\_d1\_mean & $+$0.028 & $+$0.031 & $-$0.024 & $+$0.026 & \textbf{$+$0.080} & $+$0.026 \\
680	surp\_d1\_std & $-$0.318 & \textbf{$-$0.342} & $-$0.236 & $-$0.228 & $-$0.306 & $-$0.212 \\
681	surp\_d1\_skew & \textbf{$-$0.224} & $-$0.058 & $-$0.053 & $-$0.012 & $-$0.014 & $-$0.084 \\
682	surp\_d2\_mean & $+$0.004 & $+$0.001 & \textbf{$+$0.034} & $-$0.015 & $-$0.030 & $+$0.012 \\
683	surp\_d2\_std & $-$0.312 & \textbf{$-$0.332} & $-$0.247 & $-$0.209 & $-$0.292 & $-$0.207 \\
684	ttr & \textbf{$-$0.404} & $-$0.212 & $-$0.123 & $-$0.115 & $-$0.203 & $-$0.135 \\
685	hapax\_ratio & \textbf{$-$1.056} & $-$0.221 & $-$0.144 & $-$0.108 & $-$0.186 & $-$0.139 \\
686	self\_bleu & $-$0.056 & $+$0.031 & \textbf{$+$0.140} & $+$0.058 & $+$0.118 & $+$0.127 \\
687	freq\_kurtosis & $+$0.071 & \textbf{$-$0.083} & $-$0.007 & $+$0.007 & $+$0.005 & $-$0.030 \\
688	freq\_entropy & \textbf{$-$0.350} & $-$0.158 & $-$0.104 & $-$0.021 & $+$0.031 & $-$0.044 \\
689	low\_freq\_ratio & \textbf{$-$1.029} & $-$0.226 & $-$0.139 & $-$0.110 & $-$0.134 & $-$0.090 \\
690	\midrule
691	$\bar{|d|}$ & 0.365 & 0.170 & 0.125 & 0.112 & 0.137 & 0.112 \\
692	\bottomrule
693	\end{tabular}
694	\end{table*}
695	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9aacc8bf-e9be-466a-a09c-7f2edb19274e",
  "isSidechain": false,
  "promptId": "12172553-d9aa-40c5-a42d-a4d4469a539a",
  "type": "user",
  "uuid": "49998947-0ec9-405d-8439-be9daccdfbcb",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex",
      "content": "\\section{Extended Analysis and Limitations}\n\\label{sec:extended_discussion}\n\nThis section provides supporting tables for cross-scorer validation (Tables~\\ref{tab:crossscorer}--\\ref{tab:anova_crossscorer}), followed by extended limitations, ablation studies, and domain-specific analyses.\n\n\\noindent\\begin{minipage}{\\columnwidth}\n\\centering\n\\captionof{table}{Cross-scorer validation on Qwen-generated text. Alternative scorers (Pythia-1.4B, OLMo-1B) preserve feature ranking ($\\rho > 0.90$) and rewrite-mode $\\Kempirical = 2$, but reduce continuation-mode $\\Kempirical$ from 2 to 1.}\n\\label{tab:crossscorer}\n\\resizebox{\\columnwidth}{!}{\\input{tables/tab_crossscorer}}\n\\end{minipage}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Three-way ANOVA (Generator $\\times$ Scorer $\\times$ Depth-Pair) on per-fold pairwise $\\auc$ values (Type~II SS). DV = per-fold AUC; $N{=}300$ (12 cells $\\times$ 5 folds $\\times$ 5 depth-pairs; 3 generators $\\times$ 4 scorers). Scorer is statistically significant ($p < .001$) but has a small effect size ($\\eta^2_p = 0.19$) relative to Depth-Pair ($\\eta^2_p = 1.00$) and Generator ($\\eta^2_p = 0.89$), indicating that scorer choice has a detectable but practically minor influence on depth discrimination (Scorer $\\eta^2_p$ is approximately 5$\\times$ smaller than Generator and dwarfed by Depth-Pair). Per-fold AUC values within the same generator share seed documents across folds and are not fully independent; we therefore rely on effect-size ratios rather than $p$-values for interpretation.}\n\\label{tab:anova_crossscorer}\n\\begin{tabular}{lrrrr}\n\\toprule\n\\textbf{Source} & \\textbf{df} & $F$ & $p$ & $\\eta^2_p$ \\\\\n\\midrule\nGenerator     & 2  & 926.8  & ${<}.001$  & .885 \\\\\nScorer        & 3  & 19.02  & ${<}.001$  & .192 \\\\\nDepth-Pair    & 4  & 24736  & ${<}.001$  & .998 \\\\\nGen$\\times$Scorer & 6 & 8.16 & ${<}.001$ & .170 \\\\\nGen$\\times$Depth  & 8 & 993.7 & ${<}.001$ & .971 \\\\\nScorer$\\times$Depth & 12 & 2.45 & .005 & .109 \\\\\nResidual      & 240 & & & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Extended Limitations}\n\\label{sec:extended_limitations}\n\n\\emph{Prompt-chain versus retrain-chain.}\nBoth Qwen2.5-1.5B and Pythia-1.4B yield $\\Kempirical{=}7$ under retrain-chain LoRA fine-tuning (Table~\\ref{tab:retrain_ci}), extending detectable depth by 5 additional generations beyond prompt-chain $\\Kempirical{=}2$.\nCumulative model-adaptation artifacts (vocabulary narrowing, repetition bias) make each retrained generation highly distinguishable.\nThe two models exhibit different decay profiles: Pythia achieves higher early-pair AUC (1v2: 0.947 vs.\\ 0.897) but drops more steeply at deeper pairs (4v5: 0.691 vs.\\ 0.746), yet both converge to $\\Kempirical{=}7$ (6v7: Qwen 0.641, Pythia 0.634; both CI lower bounds $> \\theta$).\nThis convergence despite differences in effective LoRA adaptation capacity (Pythia uses fused QKV attention with rank-16 vs.\\ Qwen's separate Q/K/V projections) indicates robustness to LoRA parameterization.\nThe extended discriminability under retraining aligns with theoretical analyses of iterative retraining instability on synthetic data~\\cite{bertrand2024stability, gerstgrasser2024model}, where each retraining cycle amplifies distributional artifacts beyond the text-intrinsic degradation observed in prompt-chains.\nExtrapolating yields 7v8 $\\approx 0.57 < \\theta$ for both models. This places $\\Kempirical{=}7$ near the ceiling for retrain-chains.\nPrompt-chain $\\Kempirical$ represents the operationally relevant boundary for data curation (text-intrinsic information loss); retrain-chain $\\Kempirical$ represents the upper bound achievable via model archaeology (known training pipeline).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Retrain-chain pairwise $\\auc$ with 5-fold CV 95\\% CIs. Both models yield $\\Kempirical{=}7$; all CI lower bounds $> \\theta{=}0.60$. Retrain-chain CIs use fold-level estimates (Section~\\ref{sec:retrain_ci_note}).}\n\\label{tab:retrain_ci}\n\\begin{tabular}{lcccc}\n\\toprule\n & \\multicolumn{2}{c}{\\textbf{Qwen-1.5B}} & \\multicolumn{2}{c}{\\textbf{Pythia-1.4B}} \\\\\n\\cmidrule(lr){2-3}\\cmidrule(lr){4-5}\n\\textbf{Pair} & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI \\\\\n\\midrule\n0v1 & 0.9837 & $[.982,\\,.985]$ & 0.9844 & $[.983,\\,.986]$ \\\\\n1v2 & 0.8971 & $[.895,\\,.899]$ & 0.9470 & $[.942,\\,.952]$ \\\\\n2v3 & 0.8098 & $[.805,\\,.814]$ & 0.8891 & $[.882,\\,.896]$ \\\\\n3v4 & 0.7600 & $[.753,\\,.767]$ & 0.7999 & $[.795,\\,.805]$ \\\\\n4v5 & 0.7459 & $[.738,\\,.754]$ & 0.6907 & $[.688,\\,.693]$ \\\\\n5v6 & 0.7017 & $[.696,\\,.708]$ & 0.6497 & $[.643,\\,.657]$ \\\\\n6v7 & 0.6410 & $[.638,\\,.645]$ & 0.6340 & $[.628,\\,.641]$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{CI methodology note.}\n\\label{sec:retrain_ci_note}\nThe main pipeline reports bootstrap 95\\% CIs (1{,}000 or 10{,}000 resamples), which are valid because each bootstrap sample preserves the GroupKFold document structure: resampling operates on documents, and all depths of a given document remain together.\nIn the retrain-chain setting, each generation's training corpus is the \\emph{output} of the previous generation's fine-tuned model. This creates inter-generation dependencies that standard bootstrap resampling cannot preserve, and naive resampling would inflate AUC estimates.\nWe therefore report fold-based 95\\% CIs for retrain-chain experiments, computed as $\\bar{x} \\pm 1.96 \\cdot s / \\sqrt{K}$ from the $K{=}5$ GroupKFold AUC values.\n\n\\emph{Threshold sensitivity.}\nTable~\\ref{tab:theta_sensitivity} reports $\\Kempirical$ across $\\theta \\in [0.55, 0.70]$ for representative configurations including arXiv and cross-scorer conditions.\nQwen-continuation's 1v2 CI lower bound exceeds $\\theta$ by only 0.2\\,pp; all ten boundary comparisons yield permutation $p < 0.001$.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{$\\Kempirical$ as a function of $\\theta$ across conditions. The \\textbf{domain ordering} (arXiv $>$ web $\\geq$ cross-scorer) and \\textbf{bounded range} ($\\Kempirical{\\leq}4$) are preserved across $\\theta \\in [0.55, 0.70]$. The headline result (web $\\Kempirical{=}2$, arXiv $\\Kempirical{=}3$) holds for $\\theta \\in [0.575, 0.625]$.}\n\\label{tab:theta_sensitivity}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Condition} & \\textbf{Config} & $\\theta{=}0.55$ & $\\theta{=}0.60$ & $\\theta{=}0.625$ & $\\theta{=}0.70$ \\\\\n\\midrule\nC4 (web) & Qwen-rw      & 3 & 2 & 2 & 1 \\\\\nC4 (web) & Pythia       & 2 & 2 & 2 & 1 \\\\\nC4 (web) & OLMo         & 2 & 2 & 1 & 1 \\\\\nC4 (web) & Qwen-cont    & 3 & 2 & 2 & 1 \\\\\nC4 (web) & Qwen-7B      & 2 & 2 & 2 & 1 \\\\\nC4 (web) & Mistral-7B   & 1 & 1 & 1 & 1 \\\\\n\\midrule\narXiv    & Qwen-1.5B-base (cont.) & 4 & 3 & 3 & 2 \\\\\narXiv    & Pythia-1.4B (cont.)    & 4 & 3 & 3 & 2 \\\\\n\\midrule\nCross-scorer & Qwen-cont/Pythia-scored & 2 & 1 & 1 & 1 \\\\\nCross-scorer & Qwen-cont/OLMo-scored   & 2 & 1 & 1 & 1 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_theta_sensitivity.pdf}\n\\caption{$\\Kempirical$ as a function of $\\theta$ across all model $\\times$ domain configurations (three panels: C4, arXiv, Wikipedia). The domain ordering (Wikipedia $\\Kempirical{\\leq}1$ $<$ C4 $\\Kempirical{\\leq}2$ $<$ arXiv $\\Kempirical{\\leq}3$) is preserved across the full $\\theta \\in [0.55, 0.70]$ range. Within each domain, inter-model variation is small relative to inter-domain differences. Source domain rather than model identity governs $\\Kempirical$.}\n\\label{fig:theta_sensitivity}\n\\end{figure}\n\n\\emph{Structural confound: token length.}\nIn continuation mode the generation prompt is discarded, so all depths $\\geq 1$ consist entirely of machine-generated tokens and the 1v2 boundary compares texts differing only in conditioning context (human-authored vs.\\ machine-generated prompt), not structural composition.\nDepth~0 texts average ${\\sim}$191 subword tokens (C4 truncation), while depth~1+ texts average 193--256 tokens depending on model (Table~\\ref{tab:token_length}).\nThis asymmetry is directionally opposite to a length-inflation confound: shorter depth-0 texts provide less feature-extraction context, making 0v1 discrimination harder, not easier.\nWithin depths 1--5, mean token counts are stable (within-model range $\\leq$ 4 tokens for all configurations except Qwen-continuation at 6 tokens), so the pairwise comparisons underlying $\\Kempirical{=}2$ are unaffected by length.\nEOS truncation rates are similarly depth-stable within each model: Qwen-rewrite 7--11\\%, Pythia 34--36\\%, OLMo $<$1\\%, Qwen-continuation 17--20\\%, Qwen-7B 45--47\\%.\nModels with the highest truncation (Pythia, Qwen-7B) still yield $\\Kempirical{=}2$ with the same step-function AUC decay pattern as low-truncation models (Table~\\ref{tab:kstar_ci}), EOS truncation therefore does not drive the boundary.\n\n\\emph{Graduated filtering.}\nAll $\\alpha$ values (0.1--0.9) underperform binary-ours on MMLU ($\\alpha{=}0.1$: 0.5873; $\\alpha{=}0.9$: 0.5892 vs.\\ 0.5941); at $\\alpha{=}0.9$, HellaSwag matches exactly (0.6701).\nBinary-ours significantly outperforms all alternatives on MMLU ($p_{\\text{corr}} \\leq 0.021$); Graduated$_{0.9}$ is indistinguishable on HellaSwag ($p = 1.00$) but worse on MMLU ($p_{\\text{corr}} = 0.011$).\n\\label{tab:pairwise_significance}\n\n\\subsection{Dose-Response: Contamination Ratio Effect}\n\\label{sec:dose_response}\n\nThe main filtering experiments (Section~\\ref{sec:filtering}) use 100\\% synthetic data to maximize effect size.\nTo characterize behavior at lower contamination ratios, we mix synthetic depths 1--5 with clean C4 at 10\\%, 30\\%, and 50\\% contamination (Qwen-1.5B continuation, 5 seeds each; Table~\\ref{tab:dose_response}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{MMLU and HellaSwag by contamination ratio and filtering strategy (5 seeds, mean $\\pm$ std). Base model MMLU: 0.6018. Binary filtering retains a significant advantage on HellaSwag across all ratios ($p \\leq 0.004$, Holm-Bonferroni corrected).}\n\\label{tab:dose_response}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccccc}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{10\\%}} & \\multicolumn{2}{c}{\\textbf{30\\%}} & \\multicolumn{2}{c}{\\textbf{50\\%}} \\\\\n\\cmidrule(lr){2-3}\\cmidrule(lr){4-5}\\cmidrule(lr){6-7}\n\\textbf{Strategy} & MMLU & HellaSwag & MMLU & HellaSwag & MMLU & HellaSwag \\\\\n\\midrule\nNo-filter   & $.6058{\\pm}.0002$ & $.6689{\\pm}.0006$ & $.6069{\\pm}.0007$ & $.6664{\\pm}.0018$ & $.6063{\\pm}.0012$ & $.6680{\\pm}.0005$ \\\\\nBinary-ours & $\\mathbf{.6079{\\pm}.0004}$ & $\\mathbf{.6727{\\pm}.0007}$ & $\\mathbf{.6082{\\pm}.0011}$ & $\\mathbf{.6725{\\pm}.0006}$ & $\\mathbf{.6088{\\pm}.0009}$ & $\\mathbf{.6731{\\pm}.0004}$ \\\\\nGraduated   & $.6066{\\pm}.0010$ & $.6700{\\pm}.0014$ & $.6072{\\pm}.0008$ & $.6665{\\pm}.0012$ & $.6062{\\pm}.0008$ & $.6679{\\pm}.0001$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nAt all tested ratios (10--50\\%), no-filter MMLU remains above the base model (0.6018), synthetic data at these proportions is therefore net-beneficial rather than harmful.\nBinary filtering consistently improves over no-filter, with HellaSwag differences significant across all ratios ($p \\leq 0.004$, Holm-Bonferroni corrected).\nMMLU differences are smaller and significant only at 10\\% after correction ($p = 0.001$).\nGraduated weighting is indistinguishable from no-filter at all ratios (MMLU $p \\geq 0.27$; HellaSwag $p \\geq 0.06$), depth assignments beyond $\\Kempirical$ therefore inject noise regardless of contamination severity.\nEffect sizes diminish 3--6$\\times$ relative to the 100\\% setting (Section~\\ref{sec:filtering}), but the strategy ordering (binary $>$ graduated $\\approx$ no-filter) is preserved.\n\n\\subsection{Cross-Model Filtering Replication}\n\\label{sec:pythia_filtering}\n\nTo test whether $\\Kempirical{=}2$ correctly predicts optimal curation granularity across architectures, we replicate the filtering experiment on Pythia-1.4B (LoRA rank 8, nucleus $p{=}0.9$, $T{=}1.0$, 3 seeds; Table~\\ref{tab:pythia_filtering}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Pythia-1.4B filtering replication (3 seeds, mean $\\pm$ std). Strategy ordering matches Qwen (binary $>$ no-filter $>$ graduated on MMLU).}\n\\label{tab:pythia_filtering}\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Strategy} & \\textbf{MMLU} & \\textbf{HellaSwag} \\\\\n\\midrule\nNo-filter & $.2568{\\pm}.0012$ & $.5250{\\pm}.0008$ \\\\\nBinary-ours & $\\mathbf{.2585{\\pm}.0004}$ & $.5251{\\pm}.0001$ \\\\\nGraduated$_{0.9}$ & $.2561{\\pm}.0009$ & $\\mathbf{.5253{\\pm}.0007}$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe strategy ordering (binary $>$ no-filter $>$ graduated on MMLU) matches Qwen (Section~\\ref{sec:filtering}).\nThe small absolute differences reflect the model's near-chance MMLU baseline rather than filtering inefficacy; the consistent ordering across two architectures supports $\\Kempirical{=}2$'s predictive value for curation granularity.\nHellaSwag differences are negligible across all strategies.\n\n\\subsection{Feature Subset Stability}\n\\label{sec:feature_subset}\n\nTo test whether $\\Kempirical{=}2$ depends on the specific 15D feature combination, we evaluate random feature subsets of varying size on Pythia-1.4B prompt-chain data (Table~\\ref{tab:feature_subset}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{1v2 $\\auc$ by feature subset size (Pythia-1.4B). $\\Kempirical{=}2$ ($\\auc > \\theta{=}0.60$) is robust at $\\geq$8 features.}\n\\label{tab:feature_subset}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Subset} & \\textbf{Tested} & \\textbf{Pass} & \\textbf{Min $\\auc$} & \\textbf{Mean $\\auc$} \\\\\n\\midrule\n15D (full) & 1 & 1 & 0.6262 & 0.6262 \\\\\n10D        & 5 & 5 & 0.6153 & 0.6191 \\\\\n8D         & 5 & 5 & 0.6056 & 0.6159 \\\\\n5D         & 5 & 2 & 0.5856 & 0.5998 \\\\\n3D (top-3) & 1 & 0 & 0.5871 & 0.5871 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n$\\Kempirical{=}2$ holds for all subsets of size $\\geq$8 (10/10 pass, min $\\auc = 0.6056$), becomes fragile at 5D (2/5 pass), and fails at 3D (top-3 surprisal features alone: $\\auc = 0.5871 < \\theta$).\nThe boundary does not depend on any specific feature combination but requires sufficient dimensionality ($\\geq$8) to capture the multi-faceted distributional shift between generations 1 and 2.\n\n\\subsection{self\\_BLEU Feature Independence}\n\\label{sec:selfbleu_ablation}\n\nTo verify that $\\Kempirical$ does not depend on the self\\_BLEU feature (which may reflect stylistic repetition rather than depth-correlated degradation), we compare 15D and 14D (self\\_BLEU removed) classifiers across four model configurations (Table~\\ref{tab:selfbleu_ablation}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{15D vs.\\ 14D (self\\_BLEU removed) 1v2 $\\auc$ with bootstrap 95\\% CIs. Removing self\\_BLEU does not change $\\Kempirical$ for any configuration. Maximum $|\\Delta\\auc| = 0.0031$, within bootstrap CI width (${\\sim}0.018$).}\n\\label{tab:selfbleu_ablation}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & $\\Kempirical$ & \\textbf{15D $\\auc$ [CI]} & \\textbf{14D $\\auc$ [CI]} & $\\Delta$ \\\\\n\\midrule\nQwen-base   & 2/2 & $.6288$ $[.620,\\,.638]$ & $.6258$ $[.616,\\,.635]$ & $-.0031$ \\\\\nPythia-1.4B  & 2/2 & $.8840$ $[.878,\\,.890]$ & $.8830$ $[.876,\\,.889]$ & $-.0010$ \\\\\nLLaMA-8B     & 2/2 & $.6075$ $[.598,\\,.617]$ & $.6074$ $[.598,\\,.617]$ & $-.0001$ \\\\\nMistral-7B   & 1/1 & $.5902$ $[.580,\\,.600]$ & $.5903$ $[.580,\\,.600]$ & $+.0002$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nAll four configurations preserve their $\\Kempirical$ under 14D, with negligible AUC change ($|\\Delta| \\leq 0.003$).\nThe self\\_BLEU feature contributes minimally to the depth boundary; $\\Kempirical{=}2$ is driven by surprisal and entropy features rather than lexical repetition statistics.\n\n\\subsection{Wikipedia Domain: Scorer Confound Resolution}\n\\label{sec:wiki_domain}\n\nUnder same-family scoring (Qwen-1.5B scorer), Wikipedia $\\Kempirical$ appeared to exhibit model-family dependence: Qwen generators (1.5B and 7B) yielded $\\Kempirical{=}2$, while all four non-Qwen models yielded $\\Kempirical{=}1$ (Table~\\ref{tab:wiki_domain}).\nA scorer confound ablation resolves this apparent split.\nRescoring the same Qwen-7B Wikipedia text with Pythia-1.4B reduces 1v2 $\\auc$ from $0.611$ to $0.587$ ($\\Delta = -2.4$\\,pp), dropping $\\Kempirical$ from 2 to 1.\nWith the scorer confound controlled, all six models yield $\\Kempirical{=}1$ on Wikipedia, and the domain ordering simplifies to: arXiv ($\\Kempirical{=}3$) $>$ C4 ($\\Kempirical{=}2$) $>$ Wikipedia ($\\Kempirical{=}1$).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Wikipedia pairwise $\\auc$ across 6 models. $^\\dagger$Qwen rows use same-family scorer (Qwen-1.5B); cross-family scoring (Pythia-1.4B) reduces Qwen-7B to $\\Kempirical{=}1$ ($\\Delta = -2.4$\\,pp), resolving the apparent family split.}\n\\label{tab:wiki_domain}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llccccc}\n\\toprule\n\\textbf{Model} & \\textbf{Family} & \\textbf{0v1} & \\textbf{1v2} & \\textbf{2v3} & $\\Kempirical$ & \\textbf{Scorer} \\\\\n\\midrule\nQwen-1.5B (base) & Qwen & ---  & .619 & .550 & 2$^\\dagger$ & Qwen-1.5B \\\\\nQwen-1.5B (base) & Qwen & ---  & .599 & ---  & 1 & Pythia-1.4B \\\\\nQwen-7B          & Qwen & .967 & .611 & .556 & 2$^\\dagger$ & Qwen-1.5B \\\\\nQwen-7B          & Qwen & ---  & .587 & ---  & 1 & Pythia-1.4B \\\\\n\\midrule\nPythia-1.4B   & non-Qwen & .975 & .585 & .545 & 1 & Qwen-1.5B \\\\\nOLMo-1B       & non-Qwen & .993 & .499 & .501 & 1 & Qwen-1.5B \\\\\nLLaMA-3.1-8B  & non-Qwen & .932 & .595 & .539 & 1 & Qwen-1.5B \\\\\nMistral-7B    & non-Qwen & .961 & .555 & .524 & 1 & Qwen-1.5B \\\\\n\\bottomrule\n\\multicolumn{7}{l}{\\footnotesize $^\\dagger$Same-family scorer; cross-family scoring yields $\\Kempirical{=}1$.}\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Per-fold transparency.}\nFor Qwen-1.5B, cross-family scoring (Pythia-1.4B) yields $\\auc$(1v2) $= 0.5994$, with per-fold values $[0.596, 0.606, 0.600, 0.603, 0.592]$ (2/5 folds marginally above $\\theta = 0.60$).\nThe aggregate mean falls below $\\theta$, confirming $\\Kempirical{=}1$.\nFor Qwen-7B, the corresponding $\\auc$ drops further to $0.587$.\n\n\\subsection{ArXiv Cross-Scorer Bootstrap CIs}\n\\label{sec:arxiv_crossscorer_ci}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Bootstrap 95\\% CI for arXiv cross-scorer (Pythia-1.4B) 2v3 boundary $\\auc$ (10{,}000 resamples). Point estimates classify 3/4 generators as $\\Kempirical{=}3$; strict CI lower-bound criterion confirms 2/4.}\n\\label{tab:arxiv_crossscorer_ci}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Generator} & \\textbf{2v3 $\\auc$} & \\textbf{95\\% CI} & \\textbf{CI lower $> \\theta$} \\\\\n\\midrule\nQwen-1.5B    & 0.632 & $[0.617,\\,0.646]$ & Yes \\\\\nLLaMA-3.1-8B & 0.620 & $[0.605,\\,0.636]$ & Yes (0.5\\,pp margin) \\\\\nMistral-7B   & 0.608 & $[0.593,\\,0.622]$ & No \\\\\nQwen-7B      & 0.599 & $[0.584,\\,0.613]$ & No \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\subsection{JSD Decay Analysis}\n\\label{sec:jsd_extended}\n\nThe token-level JSD between adjacent generations reveals two distinct decay regimes (Figure~\\ref{fig:jsd_decay}).\nFor C4 web text, 0v1 JSD exceeds 1v2 by 6--56$\\times$ across all 8 models (1B--14B) with $\\Kempirical{=}2$ (median cliff ratio ${\\sim}$15$\\times$), and subsequent pairs converge to a noise floor of ${\\sim}$0.003--0.005.\nFitting $\\jsd(k, k{+}1) \\propto e^{-\\lambda k}$ yields $\\lambda \\approx 2.2$--$3.5$ for C4 (mean ${\\approx}\\,2.9$), consistent with rapid mixing of $G_\\delta$ toward its stationary distribution.\nThese decay rates represent qualitative characterizations from 5-point curves rather than precise estimates.\nThe empirical decay rate $\\lambda$ is consistent within each domain but varies across domains: C4 yields $\\lambda \\approx 2.9$, Wikipedia $\\lambda \\approx 3.1$ (excluding OLMo, whose $\\lambda = 6.3$ reflects a capacity-limited collapse: 0v1 $\\jsd = 0.169$ with near-complete information loss at the first step, the exponential fit is therefore unreliable), and arXiv $\\lambda \\approx 1.0$.\nThis cross-model consistency indicates that the contraction rate of $G_\\delta$ is governed primarily by the structure of the input domain rather than the model architecture.\nArXiv text decays ${\\sim}$3$\\times$ slower than C4 ($\\lambda \\approx 1.0$ vs.\\ $2.9$), with a correspondingly higher convergence floor (${\\sim}$0.007--0.009 vs.\\ ${\\sim}$0.003--0.004).\nFormulaic structural features (LaTeX formatting, citation patterns, section templates) degrade more slowly under autoregressive generation and supply persistent depth-distinguishing signal, this accounts for the elevated $\\Kempirical{=}3$.\nThe retrain-chain exhibits a fundamentally different profile: $\\lambda = 0.285$ with a cliff ratio of only 1.31$\\times$ and no sharp drop between adjacent pairs (Figure~\\ref{fig:retrain_decay}).\nThis gradual, sustained divergence reflects cumulative model-adaptation artifacts rather than text-intrinsic information loss, further supporting the distinction between prompt-chain and retrain-chain $\\Kempirical$ (Appendix~\\ref{sec:boundary_extended}).\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_retrain_decay.png}\n\\caption{Retrain-chain AUC decay across 7 generation pairs (Qwen2.5-1.5B LoRA). Unlike prompt-chain (sharp cliff at 0v1$\\to$1v2), retrain-chain AUC decays gradually from 0.984 to 0.641, with all pairs above $\\theta{=}0.60$. Error bars: 95\\% CI from 5-fold CV. Dashed line: $\\theta{=}0.60$; extrapolated 7v8 $\\approx 0.57$ (below $\\theta$), suggesting $\\Kempirical{=}7$ is near the ceiling.}\n\\label{fig:retrain_decay}\n\\end{figure}\n\n\\subsection{Boundary Cases and Scale Effect}\n\\label{sec:boundary_extended}\n\nOf 9 tested model configurations on C4, 8 yield $\\Kempirical{=}2$; Mistral-7B is the only sub-2 exception ($\\Kempirical{=}1$; 1v2 $\\auc = 0.594$, CI $[0.584, 0.603]$), validating $\\theta{=}0.60$ as an effective discriminator (gap: $0.594$ vs.\\ $0.611$--$0.696$).\nMistral's cross-domain profile reinforces the domain-governed interpretation: despite $\\Kempirical{=}1$ on C4 and Wikipedia, it yields $\\Kempirical{=}2$ on code and $\\Kempirical{=}3$ on arXiv (1v2 $\\auc = 0.820$, 2v3 $= 0.628$), and this profile persists under cross-scorer validation (Pythia-1.4B scorer: C4 $\\Kempirical{=}1$, arXiv $\\Kempirical{=}3$ (2v3 $\\auc = 0.608$, CI $[0.593, 0.622]$)), domain lexical diversity can therefore rescue even web-text one-wash generators (Table~\\ref{tab:domain_kstar}).\nLarger models produce more human-like text, reducing 0v1 JSD: 0.16--0.29 at $\\leq$1.5B, 0.077--0.13 at 7--14B.\nHowever, Qwen-14B still yields $\\Kempirical{=}2$ (1v2 $\\auc = 0.621$, CI $[0.612, 0.630]$), with 0v1 $\\auc = 0.960$ comparable to Qwen-7B ($0.964$), scale in the 1B--14B range therefore does not shift the discrimination boundary.\n\n\\paragraph{Sample-size control.}\nAs a sample-size control, subsampling C4 to $n{=}2{,}200$ (matching arXiv) yields $\\Kempirical{=}1$ (1v2 $\\auc = 0.601$, CI $[0.586, 0.616]$).\nReduced sample size widens confidence intervals and produces more conservative $\\Kempirical$ estimates, arXiv's $\\Kempirical{=}3$ at the same sample size therefore reflects genuine domain signal rather than a statistical artifact of smaller training sets.\n\n\\subsection{LaTeX Markup Ablation (arXiv)}\n\\label{sec:latex_ablation}\n\nTo disentangle content-level depth signal from formatting artifacts on arXiv, we strip all LaTeX markup (commands, environments, inline math delimiters) and re-extract features from the plain-text residual (Qwen-1.5B continuation, $n{=}2{,}200$; Table~\\ref{tab:latex_ablation}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{arXiv pairwise $\\auc$ with and without LaTeX markup (Qwen-1.5B continuation). Removing formatting reduces 2v3 by ${\\sim}$1.8\\,pp but $\\Kempirical$ remains at 3 (CI lower $> \\theta$). LaTeX stripping fraction increases with depth (0.6\\% at depth 0, 4.6\\% at depth 5), deeper generations therefore produce proportionally more formatting tokens.}\n\\label{tab:latex_ablation}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccr}\n\\toprule\n\\textbf{Pair} & \\textbf{Original} & \\textbf{Stripped} & $\\Delta$ \\\\\n\\midrule\n0v1 & 0.9946 & 0.9948 & $+$0.0002 \\\\\n1v2 & 0.8580 & 0.8297 & $-$0.028 \\\\\n2v3 & 0.6427 $[0.628,\\,0.658]$ & 0.6248 $[0.610,\\,0.640]$ & $-$0.018 \\\\\n3v4 & 0.5437 & 0.5468 & $+$0.003 \\\\\n\\midrule\n$\\Kempirical$ & 3 & 3 & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nContent-level statistical properties (surprisal distribution, vocabulary diversity) account for the large majority of the depth signal; LaTeX formatting contributes a modest but measurable increment (${\\sim}$1.8\\,pp at the boundary pair).\nThe depth-correlated increase in LaTeX stripping fraction (depth 0: $-$0.6\\%, depth 5: $-$4.6\\%) indicates that autoregressive generation progressively introduces formatting tokens, consistent with mode-seeking behavior in structured text.\n\n\\subsection{Statistical Power Analysis}\n\\label{sec:power_curve}\n\nTo characterize the minimum sample size required for reliable $\\Kempirical$ determination, we subsample C4 at $n \\in \\{500, 1000, 2000, 3000, 4000, 5000\\}$ and measure 1v2 AUC stability across 10 resamples per size (Qwen-1.5B-base continuation, 5-fold GroupKFold; Table~\\ref{tab:power_curve}, Figure~\\ref{fig:power_curve}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Subsampling power analysis for $\\Kempirical{=}2$ determination (C4, Qwen-1.5B-base, 10 resamples per $n$). Detection probability: fraction of resamples where 1v2 $\\auc > \\theta{=}0.60$.}\n\\label{tab:power_curve}\n\\begin{tabular}{rccc}\n\\toprule\n$n$ & \\textbf{Mean 1v2 $\\auc$} & \\textbf{Std} & \\textbf{Detection Prob.} \\\\\n\\midrule\n500 & 0.581 & 0.018 & 20\\% \\\\\n1{,}000 & 0.591 & 0.014 & 30\\% \\\\\n2{,}000 & 0.610 & 0.009 & 100\\% \\\\\n3{,}000 & 0.617 & 0.005 & 100\\% \\\\\n4{,}000 & 0.622 & 0.004 & 100\\% \\\\\n5{,}000 & 0.629 & 0.000 & 100\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_power_curve.png}\n\\caption{$\\Kempirical{=}2$ detection rate (left axis, blue) and mean 1v2 $\\auc$ (right axis, green) as a function of sample size $n$. Detection rate reaches 100\\% at $n{=}2{,}000$; the 80\\% power threshold (dotted purple) is crossed between $n{=}1{,}000$ and $n{=}2{,}000$. Error bars: $\\pm$1 std over 10 resamples. The dashed red line marks $\\theta{=}0.60$.}\n\\label{fig:power_curve}\n\\end{figure}\n\nDetection rate jumps from 20\\% ($n{=}500$) to 100\\% ($n{=}2{,}000$), with the 80\\% power threshold crossed near $n{=}1{,}500$.\nAt $n{=}5{,}000$ (the sample size used in all main experiments), variance is zero across resamples, our results are therefore well above the minimum required for reliable boundary estimation.\nThe sharp transition reflects the proximity of the 1v2 AUC to $\\theta$: small increases in $n$ reduce variance sufficiently to move all resamples above the threshold.\n\n\\subsection{Feature Group Ablation}\n\\label{sec:feature_ablation}\n\nTo assess the relative contribution of each feature group to depth discrimination, we train a plain LightGBM classifier (\\texttt{n\\_estimators}$=$200, \\texttt{max\\_depth}$=$6; distinct from the OBD-LightGBM used in Section~\\ref{sec:method}) on the 1\\,vs.\\,2 task using (a) each feature group alone (\\emph{single}) and (b) the full 15D set minus one group (\\emph{leave-one-out}).\nRepresentative models per domain: LLaMA-3.1-8B (C4), Qwen-1.5B continuation (arXiv), and the domain ablation configuration (Wikipedia).\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_feature_ablation.pdf}\n\\caption{Feature group ablation heatmap for 1\\,vs.\\,2 classification AUC. \\emph{Left}: single-group performance. \\emph{Right}: leave-one-out performance. Surprisal (base) features are the dominant signal on arXiv (single AUC $= 0.809$) but provide only weak marginal signal on C4 and Wikipedia.}\n\\label{fig:feature_ablation}\n\\end{figure}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Feature group ablation for 1\\,vs.\\,2 classification (AUC). \\textbf{Single}: using only features from one group. \\textbf{Leave-one-out}: removing one group from the full 15D feature set. $\\Delta$ denotes the AUC drop from the full model. Classifier: plain LightGBM (\\texttt{n\\_estimators}$=$200, \\texttt{max\\_depth}$=$6), distinct from the OBD-LightGBM pipeline; AUC values are not directly comparable to Table~\\ref{tab:kstar_ci}.}\n\\label{tab:feature_ablation}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{l ccc ccc}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{Single Group}} & \\multicolumn{3}{c}{\\textbf{Leave-One-Out ($\\Delta$)}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\nFeature Group & C4 & arXiv & Wiki & C4 & arXiv & Wiki \\\\\n\\midrule\nSurprisal (base) & 0.597 & 0.809 & 0.581 & 0.601 ($-$0.007) & 0.828 ($-$0.031) & 0.616 ($-$0.003) \\\\\nSurprisal (deriv.) & 0.590 & 0.789 & 0.590 & 0.612 (+0.003) & 0.856 ($-$0.003) & 0.623 (+0.004) \\\\\nLexical diversity & 0.550 & 0.691 & 0.557 & 0.608 ($-$0.001) & 0.855 ($-$0.005) & 0.614 ($-$0.005) \\\\\nFreq. distribution & 0.533 & 0.684 & 0.564 & 0.604 ($-$0.005) & 0.851 ($-$0.009) & 0.612 ($-$0.007) \\\\\n\\midrule\nFull (15D) & 0.609 & 0.860 & 0.619 & \\multicolumn{3}{c}{---} \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nSurprisal (base) features dominate on arXiv (single-group AUC $= 0.809$; LOO drop $= 0.031$, the largest across all domain--group combinations), consistent with the persistent surprisal-distribution signal in structured academic text.\nOn C4 and Wikipedia, all LOO drops are small ($\\leq 0.007$, within cross-fold standard deviation), no single feature group is therefore individually critical for the weaker low-$\\Kempirical$ signal.\nRemoving surprisal derivatives increases AUC on C4 (+0.003) and Wikipedia (+0.004). This indicates partial redundancy with the base surprisal group in low-$\\Kempirical$ domains.\n\n\\subsection{Classifier Choice: McNemar Test}\n\\label{sec:mcnemar_baselines}\n\nTo verify that depth discriminability is driven by the 15D feature representation rather than classifier choice, we compare OBD-LightGBM against three baseline classifiers (logistic regression, linear SVC, random forest) on the depth-1 vs.\\ depth-2 binary classification task using McNemar's test with continuity correction on 5-fold GroupKFold out-of-fold predictions (Table~\\ref{tab:mcnemar_obd_baselines}).\nOf 36 comparisons, 31 are non-significant ($p \\geq 0.05$), and all five significant results concentrate in two model $\\times$ domain conditions.\nFor LLaMA-8B on C4, all three baselines significantly outperform OBD ($p \\leq 0.001$), likely reflecting LightGBM overfitting on the relatively noisy 8B-generated features rather than a systematic classifier advantage.\nFor Qwen-1.5B on Wikipedia, OBD outperforms both linear classifiers ($p < 0.001$) but not random forest ($p = 0.655$).\n\n\\begin{table*}[h]\n\\centering\n\\small\n\\caption{McNemar test $p$-values comparing OBD-LightGBM against baseline classifiers on the depth-1 vs.\\ depth-2 binary classification task (5-fold GroupKFold, out-of-fold predictions). Classifier accuracy shown in parentheses. Significant results ($p < 0.05$) are \\textbf{bold}; $^{*}p<0.05$, $^{**}p<0.01$, $^{***}p<0.001$.}\n\\label{tab:mcnemar_obd_baselines}\n\\resizebox{\\textwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Model} & \\textbf{Domain} & \\textbf{OBD Acc.} & \\textbf{vs.\\ LogReg} & \\textbf{vs.\\ LinearSVC} & \\textbf{vs.\\ RandomForest} \\\\\n\\midrule\nQwen-1.5B-base & C4    & .592 & .232 (.598)            & .605 (.595)              & .271 (.597) \\\\\nPythia-1.4B     & C4    & .631 & $\\mathbf{.033^{*}}$ (.621) & .105 (.624)              & .451 (.628) \\\\\nLLaMA-8B        & C4    & .573 & $\\mathbf{6.2{\\times}10^{-5\\,***}}$ (.592) & $\\mathbf{1.1{\\times}10^{-4\\,***}}$ (.591) & $\\mathbf{.001^{**}}$ (.586) \\\\\n\\midrule\nQwen-1.5B      & Wiki  & .588 & $\\mathbf{9.4{\\times}10^{-4\\,***}}$ (.570) & $\\mathbf{2.3{\\times}10^{-4\\,***}}$ (.568) & .655 (.590) \\\\\nPythia          & Wiki  & .560 & .180 (.567)            & .540 (.564)              & .369 (.564) \\\\\nOLMo            & Wiki  & .500 & .868 (.502)            & .705 (.503)              & .751 (.502) \\\\\nLLaMA-8B        & Wiki  & .573 & .252 (.579)            & .270 (.579)              & .110 (.580) \\\\\n\\midrule\nQwen-1.5B      & arXiv & .781 & .156 (.774)            & .079 (.772)              & .364 (.777) \\\\\nPythia          & arXiv & .733 & .232 (.727)            & .384 (.728)              & .735 (.732) \\\\\nOLMo            & arXiv & .493 & .520 (.487)            & .681 (.489)              & .759 (.496) \\\\\nQwen-7B         & arXiv & .757 & .160 (.749)            & .327 (.751)              & .733 (.758) \\\\\nMistral-7B      & arXiv & .742 & .524 (.738)            & .633 (.739)              & .225 (.748) \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\n\\vspace{4pt}\n\\footnotesize\n36 comparisons total. 5/36 reach $p < 0.05$; 4/36 reach $p < 0.01$.\nThe predominance of non-significant results confirms that depth discriminability is feature-driven, not classifier-driven.\n\\end{table*}\n\n\\subsection{Domain Lexical Statistics}\n\\label{sec:domain_lexical_stats}\n\nTable~\\ref{tab:domain-ttr-entropy} reports type-token ratio (TTR) and vocabulary entropy across three domains and six depth levels.\nThe TTR ordering at depth 0 (arXiv $>$ C4 $>$ Wikipedia) aligns with the $\\Kempirical$ ordering, with large effect sizes (Cohen's $d = 1.52$ for arXiv vs.\\ Wikipedia).\nVocabulary entropy shows a partial reversal at depth 0: C4 ($H = 6.225$) falls below Wikipedia ($H = 6.408$), while arXiv remains highest ($H = 6.853$).\nThis reversal likely reflects C4's greater content heterogeneity (higher variance: $\\sigma = 0.706$ vs.\\ $0.284$), which inflates TTR but depresses mean entropy.\nAs depth increases, all domains converge, with arXiv exhibiting the steepest decline, consistent with its higher $\\Kempirical$ and slower convergence to the stationary distribution.\n\n\\begin{table*}[h]\n\\centering\n\\small\n\\caption{Type-Token Ratio (TTR) and vocabulary entropy across three domains and generation depths.\nAt depth~0 (original human text), arXiv exhibits the highest lexical diversity (TTR\\,=\\,0.755, $H$\\,=\\,6.853),\nfollowed by C4 and Wikipedia.\nAs depth increases, all domains converge, with arXiv showing the steepest decline.\nCohen's $d$ values are computed at depth~0 for pairwise domain comparisons.}\n\\label{tab:domain-ttr-entropy}\n\\begin{tabular}{ll rrr rrr}\n\\toprule\n& & \\multicolumn{3}{c}{\\textbf{TTR}} & \\multicolumn{3}{c}{\\textbf{Vocab Entropy ($H$)}} \\\\\n\\cmidrule(lr){3-5} \\cmidrule(lr){6-8}\n\\textbf{Depth} & $N$ & \\textbf{Wiki} & \\textbf{C4} & \\textbf{arXiv} & \\textbf{Wiki} & \\textbf{C4} & \\textbf{arXiv} \\\\\n\\midrule\n0 & 5k/5k/2.2k & .665\\tpm.061 & .720\\tpm.105 & \\textbf{.755}\\tpm.055 & 6.408\\tpm.284 & 6.225\\tpm.706 & \\textbf{6.853}\\tpm.295 \\\\\n1 &             & .655\\tpm.121 & .707\\tpm.149 & \\textbf{.732}\\tpm.098 & 5.932\\tpm.843 & 5.737\\tpm1.189 & \\textbf{6.113}\\tpm.655 \\\\\n2 &             & .647\\tpm.145 & .676\\tpm.159 & \\textbf{.677}\\tpm.131 & 5.784\\tpm.905 & 5.774\\tpm1.139 & \\textbf{5.998}\\tpm.967 \\\\\n3 &             & .645\\tpm.159 & \\textbf{.662}\\tpm.164 & .635\\tpm.134 & 5.664\\tpm1.085 & 5.743\\tpm1.161 & \\textbf{5.964}\\tpm.933 \\\\\n4 &             & .636\\tpm.164 & \\textbf{.647}\\tpm.169 & .621\\tpm.140 & 5.660\\tpm1.062 & 5.758\\tpm1.167 & \\textbf{5.898}\\tpm.942 \\\\\n5 &             & .632\\tpm.172 & \\textbf{.636}\\tpm.175 & .618\\tpm.150 & 5.593\\tpm1.130 & 5.772\\tpm1.141 & \\textbf{5.816}\\tpm.968 \\\\\n\\midrule\n\\multicolumn{8}{l}{\\textit{Cohen's $d$ at depth 0 (positive $=$ second domain higher):}} \\\\\n\\multicolumn{2}{l}{C4 vs.\\ Wiki}   & \\multicolumn{3}{c}{$d = +0.65$} & \\multicolumn{3}{c}{$d = -0.34$} \\\\\n\\multicolumn{2}{l}{arXiv vs.\\ C4}  & \\multicolumn{3}{c}{$d = +0.37$} & \\multicolumn{3}{c}{$d = +1.03$} \\\\\n\\multicolumn{2}{l}{arXiv vs.\\ Wiki} & \\multicolumn{3}{c}{$d = +1.52$} & \\multicolumn{3}{c}{$d = +1.55$} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\subsection{Leave-One-Family-Out Threshold Validation}\n\\label{sec:theta_lofo}\n\nTo validate $\\theta{=}0.60$ without circular reasoning, we perform leave-one-family-out (LOFO) cross-validation: each fold removes one architecture family, derives $\\hat{\\theta}$ as the midpoint between $\\min(\\auc_{1v2})$ and $\\max(\\auc_{2v3})$ over the remaining families, then predicts $\\Kempirical$ for the held-out models.\nTable~\\ref{tab:theta_lofo} reports results across all three domains.\n\nOn C4, 8/9 held-out predictions agree with the original $\\Kempirical$ assignment at $\\theta{=}0.60$ (agreement: 89\\%).\nThe single mismatch is Qwen-1.5B-RW (rewrite mode), whose 2v3 AUC of 0.5893 lies above the LOFO-derived $\\hat{\\theta}{=}0.5725$ but below the global $\\theta{=}0.60$; this configuration is also the sole rewrite-mode model, the discrepancy is therefore attributable to mode rather than threshold instability.\nThe derived $\\hat{\\theta}$ values span $[0.5725, 0.6004]$, and $\\theta{=}0.60$ falls within this range.\n\nArXiv corroborates with 6/6 agreement (100\\%), though the wide $\\hat{\\theta}$ range $[0.5735, 0.7296]$ reflects OLMo-1B's near-chance performance ($\\auc_{1v2}{=}0.503$), which inflates the gap midpoint when OLMo is included in the training fold.\n\nWikipedia yields only 1/6 agreement (17\\%).\nThis failure is expected: most models produce near-chance 1v2 AUC on Wikipedia ($0.499$--$0.619$), so the gap between $\\min(\\auc_{1v2})$ and $\\max(\\auc_{2v3})$ is narrow or inverted, the gap-based threshold derivation is therefore invalid.\nWikipedia's $\\Kempirical{=}1$ assignment is independently confirmed by the global $\\theta{=}0.60$ criterion (Section~\\ref{sec:cross_domain}); LOFO simply cannot validate this because the method requires a clear AUC discontinuity between boundary and non-boundary pairs.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Leave-One-Family-Out (LOFO) cross-validation of $\\theta$ across three domains. Each fold holds out one architecture family, derives $\\hat{\\theta}$ as the midpoint between $\\min(\\text{AUC}_{1\\text{v}2})$ and $\\max(\\text{AUC}_{2\\text{v}3})$ over the remaining families, and predicts $K^*$ for held-out models. C4 (primary): 8/9 agreement (89\\%). arXiv: 6/6 (100\\%). Wikipedia: 1/6 (17\\%, see text).}\n\\label{tab:theta_lofo}\n\\begin{tabular}{l l l c c c c c c}\n\\toprule\nDomain & Held-out & Model & $\\text{AUC}_{1\\text{v}2}$ & $\\text{AUC}_{2\\text{v}3}$ & $\\hat{\\theta}$ & $K^*_{\\hat{\\theta}}$ & $K^*_{0.60}$ & Match \\\\\n\\midrule\nC4 & Pythia & Pythia-1.4B & 0.6539 & 0.5515 & 0.5914 & 2 & 2 & \\cmark \\\\\n & OLMo & OLMo-1B & 0.6146 & 0.5497 & 0.5914 & 2 & 2 & \\cmark \\\\\n & Qwen & Qwen-1.5B-RW & 0.6957 & 0.5893 & 0.5725 & 3 & 2 & \\xmark \\\\\n &  & Qwen-7B & 0.6178 & 0.5460 & 0.5725 & 2 & 2 & \\cmark \\\\\n &  & Qwen-1.5B-base & 0.6262 & 0.5496 & 0.5725 & 2 & 2 & \\cmark \\\\\n &  & Qwen-1.5B-cont & 0.6114 & 0.5609 & 0.5725 & 2 & 2 & \\cmark \\\\\n &  & Qwen-14B & 0.6210 & 0.5494 & 0.5725 & 2 & 2 & \\cmark \\\\\n & LLaMA & LLaMA-3.1-8B & 0.6123 & 0.5274 & 0.5914 & 2 & 2 & \\cmark \\\\\n & Mistral & Mistral-7B & 0.5935 & 0.5402 & 0.6004 & 1 & 1 & \\cmark \\\\\n\\cmidrule{2-9}\n & \\multicolumn{7}{l}{$\\hat{\\theta}$ $\\in$ [0.5725, 0.6004], agreement: 8/9 (89\\%)} \\\\\n\\midrule\narXiv & Pythia & Pythia-1.4B & 0.8047 & 0.6545 & 0.5735 & 3 & 3 & \\cmark \\\\\n & OLMo & OLMo-1B & 0.5034 & 0.5069 & 0.7296 & 1 & 1 & \\cmark \\\\\n & Qwen & Qwen-1.5B & 0.8581 & 0.6436 & 0.5789 & 3 & 3 & \\cmark \\\\\n &  & Qwen-7B & 0.8347 & 0.6255 & 0.5789 & 3 & 3 & \\cmark \\\\\n & LLaMA & LLaMA-3.1-8B & 0.8447 & 0.6215 & 0.5789 & 3 & 3 & \\cmark \\\\\n & Mistral & Mistral-7B & 0.8201 & 0.6275 & 0.5789 & 3 & 3 & \\cmark \\\\\n\\cmidrule{2-9}\n & \\multicolumn{7}{l}{$\\hat{\\theta}$ $\\in$ [0.5735, 0.7296], agreement: 6/6 (100\\%)} \\\\\n\\midrule\nWikipedia & Pythia & Pythia-1.4B & 0.5846 & 0.5445 & 0.5274 & 3 & 1 & \\xmark \\\\\n & OLMo & OLMo-1B & 0.4986 & 0.5012 & 0.5557 & 1 & 1 & \\cmark \\\\\n & Qwen & Qwen-1.5B & 0.6193 & 0.5498 & 0.5215 & 4 & 2 & \\xmark \\\\\n &  & Qwen-7B & 0.6108 & 0.5562 & 0.5215 & 4 & 2 & \\xmark \\\\\n & LLaMA & LLaMA-3.1-8B & 0.5954 & 0.5392 & 0.5274 & 3 & 1 & \\xmark \\\\\n & Mistral & Mistral-7B & 0.5552 & 0.5236 & 0.5274 & 2 & 1 & \\xmark \\\\\n\\cmidrule{2-9}\n & \\multicolumn{7}{l}{$\\hat{\\theta}$ $\\in$ [0.5215, 0.5557], agreement: 1/6 (17\\%)} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\subsection{Code Domain Results}\n\\label{sec:code_domain}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Code domain (Python, CodeSearchNet~\\cite{husain2019codesearchnet}) pairwise AUC for Qwen2.5-1.5B. $\\Kempirical{=}2$: 1v2 exceeds $\\theta{=}0.60$; 2v3 drops to chance. JSD ratio (1v2/2v3) $= 11.7\\times$, comparable to C4's cliff structure.}\n\\label{tab:code_domain_qwen}\n\\begin{tabular}{l c c c}\n\\toprule\nPair & AUC & 95\\% CI & JSD \\\\\n\\midrule\n0 vs 1 & 0.9388 & [0.929, 0.949] & 0.0814 \\\\\n1 vs 2 & 0.7382 & [0.709, 0.767] & 0.0443 \\\\\n2 vs 3 & 0.5300 & [0.514, 0.546] & 0.0038 \\\\\n3 vs 4 & 0.5022 & [0.486, 0.518] & 0.0033 \\\\\n4 vs 5 & 0.5219 & [0.510, 0.534] & 0.0030 \\\\\n\\midrule\n\\multicolumn{4}{l}{$\\Kempirical = 2$ ($\\theta = 0.60$)} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Code domain (Python, CodeSearchNet) cross-model pairwise AUC with 5-fold cross-validated 95\\% CIs across five models (four architecture families). Qwen2.5-1.5B/7B, LLaMA-3.1-8B, and Mistral-7B-v0.3 yield $\\Kempirical{=}2$ (4/5); Pythia-1.4B yields $\\Kempirical{=}1$ (capacity-limited). All models scored by Qwen2.5-1.5B (cross-family for non-Qwen).}\n\\label{tab:code_crossmodel_kstar}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{l cc cc cc cc cc}\n\\toprule\n & \\multicolumn{2}{c}{Qwen-1.5B} & \\multicolumn{2}{c}{Qwen-7B} & \\multicolumn{2}{c}{Pythia-1.4B} & \\multicolumn{2}{c}{LLaMA-8B} & \\multicolumn{2}{c}{Mistral-7B} \\\\\n\\cmidrule(lr){2-3}\\cmidrule(lr){4-5}\\cmidrule(lr){6-7}\\cmidrule(lr){8-9}\\cmidrule(lr){10-11}\n & AUC & 95\\% CI & AUC & 95\\% CI & AUC & 95\\% CI & AUC & 95\\% CI & AUC & 95\\% CI \\\\\n\\midrule\n0v1 & .9388 & [.929,\\,.949] & .9051 & [.901,\\,.909] & \\textbf{.9592} & [.956,\\,.963] & .9161 & [.912,\\,.920] & .9191 & [.917,\\,.921] \\\\\n1v2 & \\textbf{.7382} & [.709,\\,.767]\\rlap{$^*$} & .7276 & [.722,\\,.733]\\rlap{$^*$} & .5983 & [.593,\\,.603] & \\textbf{.7394} & [.729,\\,.750]\\rlap{$^*$} & .6152 & [.603,\\,.627]\\rlap{$^*$} \\\\\n2v3 & .5300 & [.514,\\,.546] & .5368 & [.522,\\,.551] & .5215 & [.509,\\,.534] & .5112 & [.502,\\,.521] & .5293 & [.520,\\,.538] \\\\\n3v4 & .5022 & [.486,\\,.518] & .5090 & [.504,\\,.515] & .5152 & [.503,\\,.527] & .5200 & [.506,\\,.534] & .5286 & [.518,\\,.539] \\\\\n4v5 & .5219 & [.510,\\,.534] & .5139 & [.501,\\,.527] & .5046 & [.491,\\,.518] & .4996 & [.493,\\,.507] & .5099 & [.504,\\,.516] \\\\\n\\midrule\n$K^*$ & \\multicolumn{2}{c}{\\textbf{2}} & \\multicolumn{2}{c}{\\textbf{2}} & \\multicolumn{2}{c}{1} & \\multicolumn{2}{c}{\\textbf{2}} & \\multicolumn{2}{c}{\\textbf{2}} \\\\\n\\bottomrule\n\\multicolumn{11}{@{}p{\\linewidth}@{}}{\\footnotesize $^*$Permutation $p < 0.001$. $K^*$: max $k$ where $k$v$(k{+}1)$ CI lower bound $> \\theta = 0.60$ (Eq.~\\ref{eq:kstar}).}\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Cross-scorer validation (Code domain).}\nTo rule out scorer confound for Code $\\Kempirical{=}2$, we re-evaluate Qwen2.5-1.5B code generations using Pythia-1.4B as the reference scorer (Table~\\ref{tab:code_crossscorer}).\nCross-family scoring yields $\\Kempirical{=}2$ (1v2 $\\auc = 0.7197$, five-fold minimum $= 0.6985$, all folds above $\\theta$), a decrease of only 1.9\\,pp from Qwen self-scoring ($0.7382$).\nThis contrasts with Wikipedia, where same-family scoring inflates $\\Kempirical$ from 1 to 2 (Appendix~\\ref{sec:wiki_domain}): Code depth signal is robust to scorer choice, while Wikipedia's marginal signal is scorer-sensitive.\nThe scorer confound is therefore domain-specific rather than systematic.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Code domain cross-scorer validation: Pythia-1.4B scorer on Qwen2.5-1.5B code generations. $\\Kempirical{=}2$ is preserved; five-fold minimum 1v2 $\\auc = 0.6985$, well above $\\theta{=}0.60$.}\n\\label{tab:code_crossscorer}\n\\begin{tabular}{lcc}\n\\toprule\nScorer & 1v2 $\\auc$ & 5-fold min \\\\\n\\midrule\nQwen2.5-1.5B (self) & 0.7382 & 0.7093 \\\\\nPythia-1.4B (cross) & 0.7197 & 0.6985 \\\\\n\\midrule\n$\\Delta$ & \\multicolumn{2}{c}{$-1.9$\\,pp} \\\\\n$\\Kempirical$ & \\multicolumn{2}{c}{2 (both)} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Borderline Feature Analysis}\n\\label{sec:borderline_analysis}\n\nTo understand why Mistral-7B yields $\\Kempirical{=}1$ while other C4 models yield $\\Kempirical{=}2$, we compute per-feature Cohen's $d$ (depth-1 vs.\\ depth-2) and LightGBM feature importances across six C4 configurations spanning the full 1v2 AUC range (0.594--0.884).\n\nMistral-7B exhibits the lowest depth-0 mean surprisal (2.32 vs.\\ 2.90--3.02 for other models), the scorer model therefore already finds Mistral's output highly predictable.\nThis compressed baseline limits the dynamic range available for detecting inter-generational degradation: all 15 Cohen's $d$ values are weak ($\\bar{|d|} = 0.112$; Table~\\ref{tab:cohens_d_full}), and no single feature exceeds 13\\% of total classifier importance.\nThe borderline models (LLaMA-8B, Pythia at $T{=}1.2$) show a similar pattern at slightly higher effect sizes.\n\nGreedy decoding is qualitatively distinct: Pythia-greedy achieves 0.884 AUC via lexical collapse (hapax ratio $d = -1.056$, capturing 47\\% of importance), a signal absent under sampling-based generation where all non-greedy models rely on surprisal variability features.\n\n\\begin{table*}[h]\n\\centering\n\\small\n\\caption{Feature-level summary of C4 1v2 classification across model categories. Imp.\\ = normalized LightGBM gain importance (\\%). $\\bar{|d|}$ = mean absolute Cohen's $d$ over all 15 features. $\\Delta\\text{surp}_{1\\to2}$: change in mean surprisal from depth 1 to depth 2.}\n\\label{tab:borderline_features}\n\\begin{tabular}{@{}llc lcc@{}}\n\\toprule\nCategory & Model & AUC & Top-3 Features (Imp.\\%) & $\\bar{|d|}$ & $\\Delta\\text{surp}_{1\\to2}$ \\\\\n\\midrule\nStrong & Pythia-greedy & 0.884 & hapax\\_ratio (47), surp\\_mean (11), low\\_freq\\_ratio (8) & 0.365 & $-$0.160 \\\\\nStrong & Pythia-nuc09 & 0.677 & surp\\_std (20), freq\\_entropy (11), surp\\_d1\\_std (8) & 0.170 & $-$0.196 \\\\\nStrong & Qwen-1.5B-base & 0.626 & surp\\_std (13), freq\\_entropy (10), surp\\_mean (9) & 0.125 & $-$0.159 \\\\\n\\midrule\nBorderline & Pythia-$T{=}1.2$ & 0.617 & surp\\_std (15), freq\\_entropy (10), surp\\_kurt (8) & 0.112 & $-$0.059 \\\\\nBorderline & LLaMA-3.1-8B & 0.612 & surp\\_std (12), surp\\_d1\\_std (10), freq\\_entropy (9) & 0.137 & $-$0.215 \\\\\n\\midrule\nBelow $\\theta$ & Mistral-7B & 0.594 & surp\\_std (13), freq\\_entropy (9), surp\\_d1\\_skew (9) & 0.112 & $-$0.086 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\begin{table*}[h]\n\\centering\n\\scriptsize\n\\caption{Cohen's $d$ (depth-1 vs.\\ depth-2) for all 15 features across six C4 models. \\textbf{Bold}: largest $|d|$ in each row. Greedy decoding produces qualitatively different effect sizes via lexical collapse (hapax\\_ratio, low\\_freq\\_ratio); under sampling, surprisal variability features (surp\\_std, surp\\_d1\\_std, surp\\_d2\\_std) carry the dominant signal.}\n\\label{tab:cohens_d_full}\n\\begin{tabular}{@{}lrrrrrr@{}}\n\\toprule\nFeature & \\rotatebox{60}{Pythia-greedy} & \\rotatebox{60}{Pythia-nuc09} & \\rotatebox{60}{Qwen-1.5B-base} & \\rotatebox{60}{Pythia-$T{=}1.2$} & \\rotatebox{60}{LLaMA-3.1-8B} & \\rotatebox{60}{Mistral-7B} \\\\\n\\midrule\nsurp\\_mean & \\textbf{$-$0.416} & $-$0.306 & $-$0.244 & $-$0.103 & $-$0.263 & $-$0.152 \\\\\nsurp\\_std & $-$0.301 & \\textbf{$-$0.370} & $-$0.229 & $-$0.268 & $-$0.316 & $-$0.190 \\\\\nsurp\\_skew & \\textbf{$+$0.468} & $+$0.086 & $+$0.085 & $-$0.217 & $+$0.049 & $+$0.103 \\\\\nsurp\\_kurt & \\textbf{$+$0.433} & $+$0.102 & $+$0.071 & $-$0.188 & $+$0.031 & $+$0.124 \\\\\nsurp\\_d1\\_mean & $+$0.028 & $+$0.031 & $-$0.024 & $+$0.026 & \\textbf{$+$0.080} & $+$0.026 \\\\\nsurp\\_d1\\_std & $-$0.318 & \\textbf{$-$0.342} & $-$0.236 & $-$0.228 & $-$0.306 & $-$0.212 \\\\\nsurp\\_d1\\_skew & \\textbf{$-$0.224} & $-$0.058 & $-$0.053 & $-$0.012 & $-$0.014 & $-$0.084 \\\\\nsurp\\_d2\\_mean & $+$0.004 & $+$0.001 & \\textbf{$+$0.034} & $-$0.015 & $-$0.030 & $+$0.012 \\\\\nsurp\\_d2\\_std & $-$0.312 & \\textbf{$-$0.332} & $-$0.247 & $-$0.209 & $-$0.292 & $-$0.207 \\\\\nttr & \\textbf{$-$0.404} & $-$0.212 & $-$0.123 & $-$0.115 & $-$0.203 & $-$0.135 \\\\\nhapax\\_ratio & \\textbf{$-$1.056} & $-$0.221 & $-$0.144 & $-$0.108 & $-$0.186 & $-$0.139 \\\\\nself\\_bleu & $-$0.056 & $+$0.031 & \\textbf{$+$0.140} & $+$0.058 & $+$0.118 & $+$0.127 \\\\\nfreq\\_kurtosis & $+$0.071 & \\textbf{$-$0.083} & $-$0.007 & $+$0.007 & $+$0.005 & $-$0.030 \\\\\nfreq\\_entropy & \\textbf{$-$0.350} & $-$0.158 & $-$0.104 & $-$0.021 & $+$0.031 & $-$0.044 \\\\\nlow\\_freq\\_ratio & \\textbf{$-$1.029} & $-$0.226 & $-$0.139 & $-$0.110 & $-$0.134 & $-$0.090 \\\\\n\\midrule\n$\\bar{|d|}$ & 0.365 & 0.170 & 0.125 & 0.112 & 0.137 & 0.112 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n",
      "numLines": 695,
      "startLine": 1,
      "totalLines": 695
    }
  },
  "sourceToolAssistantUUID": "9aacc8bf-e9be-466a-a09c-7f2edb19274e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 192 · 2026-05-19T13:05:26.298Z_

```json
{
  "parentUuid": "49998947-0ec9-405d-8439-be9daccdfbcb",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "3447dffd-ffc9-48b7-b167-3531899ecad3",
  "timestamp": "2026-05-19T13:05:26.298Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Runtime record

_source line 193_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 2 审稿请求]: ## Round 9（继续审稿）— Reviewer 2（新颖性 + 完整性 + 写作质量）  上轮评分：3.5 (Borderline Conference)。论文已大幅修订，请重点验证以下 open/in_progress issues 是否已充分修复。  ### 论文路径 `projects/gen-depth-contamination/docs/paper…",
  "leafUuid": "3447dffd-ffc9-48b7-b167-3531899ecad3",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77"
}
```

---


### Runtime record

_source line 194_

```json
{
  "type": "ai-title",
  "aiTitle": "Review paper on data contamination detection for EMNLP 2026",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77"
}
```

---


### Runtime record

_source line 195_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 2 审稿请求]: ## Round 9（继续审稿）— Reviewer 2（新颖性 + 完整性 + 写作质量）  上轮评分：3.5 (Borderline Conference)。论文已大幅修订，请重点验证以下 open/in_progress issues 是否已充分修复。  ### 论文路径 `projects/gen-depth-contamination/docs/paper…",
  "leafUuid": "3447dffd-ffc9-48b7-b167-3531899ecad3",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77"
}
```

---


### Runtime record

_source line 196_

```json
{
  "type": "ai-title",
  "aiTitle": "Review paper on data contamination detection for EMNLP 2026",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77"
}
```

---


### System

_source line 197 · 2026-05-19T13:07:41.818Z_

```json
{
  "parentUuid": null,
  "logicalParentUuid": "3447dffd-ffc9-48b7-b167-3531899ecad3",
  "isSidechain": false,
  "type": "system",
  "subtype": "compact_boundary",
  "content": "Conversation compacted",
  "isMeta": false,
  "timestamp": "2026-05-19T13:07:41.818Z",
  "uuid": "99a4505c-fde0-4510-a7c6-7235e705537a",
  "level": "info",
  "compactMetadata": {
    "trigger": "auto",
    "preTokens": 170852,
    "postTokens": 7070,
    "durationMs": 135518
  },
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "crystalline-noodling-flask"
}
```

---


## Round 8

## Round 8

49 recorded events


### User

_source line 198 · 2026-05-19T13:07:41.819Z_

This session is being continued from a previous conversation that ran out of context. The summary below covers the earlier portion of the conversation.

Summary:
1. Primary Request and Intent:
   I am acting as Reviewer 2 for the paper "Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary" targeting EMNLP 2026 (ARR May 2026). My review focus areas are **novelty, completeness, and writing quality**. The conversation spans multiple rounds:
   - **Round 1**: Full initial review of the paper (completed, score 3.5 Borderline Conference)
   - **Cross-review**: Point-by-point response to Reviewer 1's issues (completed)
   - **Dream review**: Review of a simulated expanded version of the paper (completed, score 4/6 Borderline Accept)
   - **Round 2 (CURRENT, IN PROGRESS)**: Re-review the significantly revised paper, checking whether specific issues are [RESOLVED] or [STILL_OPEN], and issuing updated assessment

   The most recent task is Round 2 re-review with a specific checklist of issues to verify.

2. Key Technical Concepts:
   - **K\* (K-star empirical)**: Maximum generational depth at which adjacent generations remain distinguishable, defined via pairwise AUC > θ=0.60
   - **OBD-LightGBM**: Ordinal Binary Decomposition classifier using LightGBM for depth prediction
   - **15-dimensional feature set**: Surprisal moments (4D), surprisal derivatives (5D), vocabulary diversity (3D), frequency tail statistics (3D)
   - **Prompt-chain vs retrain-chain**: Two modes of recursive generation; prompt-chain K\*=2, retrain-chain K\*=7
   - **One-wash laundering**: Single generation pass renders text indistinguishable from deeper synthetic content
   - **Domain hierarchy**: arXiv (K\*=3) > C4 (K\*=2) ≥ Code (K\*=1-2) ≥ Wikipedia (K\*=1)
   - **LOFO (Leave-One-Family-Out)**: Cross-validation for threshold validation (new in revision)
   - **θ=0.60 threshold**: Post-hoc operational threshold, now independently validated via LOFO
   - **Cross-scorer validation**: Testing robustness by using different models for feature extraction
   - **McNemar test**: Used for classifier comparison (corrected in revision from false claims about LLM comparison)
   - **Bootstrap CI**: 1,000 or 10,000 resamples for confidence intervals
   - **ACL ARR review form dimensions**: Soundness, Excitement, Reproducibility, Overall Assessment (1-5 scale with 0.5 increments)

3. Files and Code Sections:
   - **main.tex** (`/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex`)
     - Master file; contains abstract, limitations, ethics statement
     - Key revision: Abstract now mentions 4 domains, θ described as "AUC decision threshold", one-wash wording precision ("first-generation synthetic web text"), dash removed from comment line
     - Limitations updated: code domain info, retrain-chain K\*=7 with 2 models, n≥2,000 suffices

   - **introduction.tex**
     - Key revision: DPI now says "motivating" + "its actual value is determined empirically" (was stronger), contributions restructured: "4/5 families (8/9 configurations)", "4 source domains (3 text + 1 code)", filtering now "as a consistency check", McNemar claim corrected
     - Contribution (b) changed from "Domain ordering invariance" to "Domain ordering" with code included

   - **related_work.tex**
     - Significantly expanded: Added Gambetta surplexity (citet), surveys (wu2023survey, tang2024science), more detectors (yang2024dnagpt, verma2024ghostbuster), Oren et al. contamination detection, CORAL ordinal regression, surprisal foundations (hale2001surprisal, levy2008expectation), Bertrand stability
     - Now 4 paragraphs: model collapse, beyond binary detection, data selection/curation, ordinal classification/probing

   - **method.tex**
     - Critical revision: Eq.1 now uses CI lower bound (`CI_low(AUC_{k-1,k}) > θ`) instead of point-estimate AUC
     - θ explicitly called "post-hoc operational threshold" (twice)
     - Added LOFO cross-validation paragraph: θ̂∈[0.5725, 0.6004], 8/9 agreement on C4, 6/6 on arXiv
     - DPI paragraph: "DPI guarantees existence but does not bound K*_theory, so the actual saturation depth must be measured empirically"
     - LightGBM now cited: `\cite{ke2017lightgbm}`

   - **experiments_c1.tex**
     - Added family-level reporting (L45): "Among non-Qwen families: Pythia and OLMo yield clear K\*=2, LLaMA is borderline, Mistral yields K\*=1"
     - Added Code domain subsection (L138-165): CodeSearchNet Python, 5 models, 4 families, K\*=2 for 4 models, K\*=1 for Pythia
     - "Domain as the primary factor" (was "sole dominant factor")
     - Domain table now includes Code column
     - Neural probe now states "5,000 texts per depth"

   - **experiments_c3.tex**
     - Filtering section now framed as "consistency check using prompt-chain documents"
     - arXiv graduated filtering failure noted: "K\* accurately measures discriminability but overestimates filtering utility"

   - **discussion.tex**
     - One-wash: "so a single generation pass renders text indistinguishable from deeper content"
     - McNemar reference changed to generic "Appendix" (removed false claim about frontier LLMs)
     - Retrain-chain K\*=7 (was ≥4)
     - Code domain integrated into domain dependence paragraph
     - New "Surprisal attenuation" paragraph explaining Mistral exception

   - **conclusion.tex**
     - "domain structure as the primary determinant" (was stronger language)
     - Code domain included: "K\*=1-2 for code"
     - Removed "one-wash laundering" term; replaced with descriptive language

   - **appendix_extended.tex**
     - Retrain-chain: now 2 models (Qwen-1.5B AND Pythia-1.4B), both K\*=7, with decay profiles
     - Added CI methodology note for retrain-chain (fold-based vs bootstrap)
     - Added McNemar classifier comparison (Section: Classifier Choice, Table tab:mcnemar_obd_baselines): 36 comparisons, 31/36 non-significant
     - Added LOFO validation table (tab:theta_lofo) with all 3 domains
     - Added Code domain tables: Qwen-1.5B code pairwise AUC, cross-model code K\*, cross-scorer code validation
     - Added Domain Lexical Statistics (tab:domain-ttr-entropy) with TTR and entropy across domains/depths
     - Added Borderline Feature Analysis (tab:borderline_features, tab:cohens_d_full)
     - Added power curve with figure (tab:power_curve, fig:power_curve): n≥2,000 for 100% detection
     - Retrain-chain figure added (fig:retrain_decay)

   - **references.bib**
     - penedo2024fineweb confirmed to have full author list (contrary to R1's claim)
     - New citations added: ke2017lightgbm, cao2020coral, husain2019codesearchnet, raffel2020t5, bertrand2024stability, yang2024dnagpt, verma2024ghostbuster, wu2023survey, tang2024science, hale2001surprisal, levy2008expectation, oren2024proving

4. Errors and Fixes:
   - **Session start skill file not found**: The skill file path `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/skills/review-reviewer-session-start.skill.md` didn't exist. Proceeded without it.
   - **PDF rendering too large**: pdf_to_images output exceeded token limits. Used subagent to extract content and Bash/Python to check page counts from JSON output.
   - **R1's penedo2024fineweb claim**: R1 claimed missing authors; I verified the bib file actually has complete authors. The verify_references tool showed empty author field due to parsing of special characters.

5. Problem Solving:
   - **θ=0.60 circular reasoning**: Both R1 and I flagged this. The revision addresses it with LOFO cross-validation (8/9 agreement on C4, θ̂∈[0.5725, 0.6004]).
   - **"sole" vs "primary"**: Both reviewers flagged the overclaim. Revision changes heading and text to "primary."
   - **DPI logical jump**: R1 flagged as critical, I suggested downgrade to should-fix. Revision now says "motivates" and "DPI guarantees existence but does not bound K*_theory."
   - **McNemar false claim**: Original claimed frontier LLMs showed no significant difference vs OBD. Revision replaces with classifier comparison McNemar test against baselines (logistic regression, SVC, random forest).
   - **Eq.1 definition inconsistency**: Changed from point-estimate AUC to CI lower bound in the formal definition.

6. All User Messages:
   - **Message 1**: "[Round 1 审稿请求]" - Detailed Round 1 review assignment with 15 specific review points covering novelty, completeness, writing quality for EMNLP 2026 paper
   - **Message 2**: "Continue from where you left off." (after Round 1 review posted)
   - **Message 3**: "[Round 1 审稿请求]: ## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见" - Full text of R1's review with request to respond [AGREE]/[REBUT] to each issue
   - **Message 4**: "Continue from where you left off." (after cross-review posted)
   - **Message 5**: "[Dream 审稿任务 — Reviewer 2：新颖性 + 相关工作]" - Dream paper review assignment with specific instructions on what to/not to evaluate
   - **Message 6**: "Continue from where you left off." (after Dream review posted)
   - **Message 7**: "[Round 2 审稿请求]: ## Round 9（继续审稿）— Reviewer 2（新颖性 + 完整性 + 写作质量）" - Detailed Round 2 re-review assignment with specific issue checklist (R8-N1 through R10-N2) requiring [RESOLVED]/[STILL_OPEN] status, plus writing quality re-assessment, novelty re-assessment, page limit check, new issue check, dash check

7. Pending Tasks:
   - **Round 2 review report**: Must write and post the complete Round 2 review covering:
     - Issue-by-issue [RESOLVED]/[STILL_OPEN] status for all listed issues
     - Writing quality re-assessment (Related Work coverage, -ing phrases, reference density)
     - Novelty re-assessment (Code domain, 4-domain ordering, retrain-chain K\*=7)
     - Page limit check (8 pages with new Code/LOFO content)
     - Check for new issues introduced by revisions
     - Dash check (user custom rule)
     - Updated Overall Assessment using ARR scoring

8. Current Work:
   I was in the middle of the Round 2 re-review. I had completed reading ALL revised paper sections:
   - main.tex (96 lines), introduction.tex (31 lines), related_work.tex (24 lines), method.tex (81 lines), experiments_c1.tex (172 lines), experiments_c3.tex (18 lines), discussion.tex (39 lines), conclusion.tex (7 lines), appendix_extended.tex (695 lines)
   
   I had identified all the key changes but had NOT yet:
   - Written the formal Round 2 review
   - Posted it via review_reviewer_post_to_director
   - Checked dash usage in revised text
   - Verified page count with new content
   - Done -ing phrase frequency analysis on revised text

   The user's most recent request was: "## Round 9（继续审稿）— Reviewer 2（新颖性 + 完整性 + 写作质量）" with specific instructions to "逐条标注每个 issue 为 [RESOLVED] 或 [STILL_OPEN]" and produce "Issue Resolution Status → New Issues (if any) → Updated Strengths/Weaknesses → Updated Overall Assessment（ARR 标准）"

9. Optional Next Step:
   Complete the Round 2 review by:
   1. Checking for dashes in revised text (grep for em-dash/en-dash in all .tex files)
   2. Checking page count of revised PDF
   3. Checking -ing phrase frequency in revised text
   4. Writing the complete Round 2 review with issue-by-issue resolution status based on my reading of all revised sections
   5. Posting via `review_reviewer_post_to_director(text, reviewer_id="2", project="gen-depth-contamination")`

   Based on my reading, my preliminary assessment of each issue:
   - R8-N1 (θ LOFO): RESOLVED - LOFO added with detailed table, 8/9 agreement on C4
   - R8-N2 (prompt-chain gap): RESOLVED - "consistency check" framing, retrain-chain K\*=7 with 2 models, clear limitations
   - R8-N3 ("sole"→"primary"): Need to verify all instances
   - R8-W1 (DPI): RESOLVED - "motivates", "DPI guarantees existence but does not bound"
   - R8-W2 (Qwen bias): RESOLVED - family-level reporting added
   - R8-W3 (filtering framing): RESOLVED - "consistency check" language
   - R8-W4 (transfer matrix): Need to check if expanded beyond 4/9
   - R8-W5 (cross-scorer + McNemar): RESOLVED in part - McNemar now for classifier comparison
   - R8-W6 (one-wash): RESOLVED - Abstract precision fix
   - R8-W7 (arXiv CI): Need to verify
   - R8-M2 (missing refs): RESOLVED - LightGBM, CORAL, Oren, DivEye discussion added
   - R8-M3 (-ing phrases): Need to check
   - R8-M4 (Abstract terms + neural probe): Need to check
   - R10-N1 (McNemar false claim): RESOLVED - replaced with classifier comparison
   - R10-N2 (Code domain): RESOLVED - Code domain fully integrated

If you need specific details from before compaction (like exact code snippets, error messages, or content you generated), read the full transcript at: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination--claude-sessions-review-reviewer-2-55676115/f9be207d-2c73-4ecb-ba22-6b935f15af77.jsonl
Continue the conversation from where it left off without asking the user any further questions. Resume directly — do not acknowledge the summary, do not recap what was happening, do not preface with "I'll continue" or similar. Pick up the last task as if the break never happened.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "99a4505c-fde0-4510-a7c6-7235e705537a",
  "isSidechain": false,
  "promptId": "12172553-d9aa-40c5-a42d-a4d4469a539a",
  "type": "user",
  "isVisibleInTranscriptOnly": true,
  "isCompactSummary": true,
  "uuid": "404439a0-c9ea-4107-8646-e13e9491d273",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "crystalline-noodling-flask"
}
```

</details>

---


### Runtime record

_source line 199 · 2026-05-19T13:07:41.814Z_

```json
{
  "parentUuid": "404439a0-c9ea-4107-8646-e13e9491d273",
  "isSidechain": false,
  "attachment": {
    "type": "compact_file_reference",
    "filename": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex",
    "displayPath": "../../../docs/paper/experiments_c1.tex"
  },
  "type": "attachment",
  "uuid": "eb05bf94-9df6-4f5f-868a-f7baeeae1203",
  "timestamp": "2026-05-19T13:07:41.814Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "crystalline-noodling-flask"
}
```

---


### Runtime record

_source line 200 · 2026-05-19T13:07:41.516Z_

```json
{
  "parentUuid": "eb05bf94-9df6-4f5f-868a-f7baeeae1203",
  "isSidechain": false,
  "attachment": {
    "type": "file",
    "filename": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex",
    "content": {
      "type": "text",
      "file": {
        "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex",
        "content": "\\section{Discussion}\n\\label{sec:discussion}\n\\label{sec:why_kstar}\n\\label{sec:one_wash}\n\\label{sec:negative_graduated}\n\\label{sec:repr_dependence}\n\\label{sec:boundary_cases}\n\\label{sec:length_confound}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_jsd_decay.pdf}\n\\caption{Token-level JSD between adjacent depth pairs on log scale. Blue band: min-max range across 8 C4 models (1B--14B) with $\\Kempirical{=}2$; dashed purple: Mistral-7B ($\\Kempirical{=}1$, cross-scorer validated); green: arXiv Pythia ($\\Kempirical{=}3$); dotted red: retrain-chain ($\\Kempirical{=}7$). C4 models exhibit a sharp cliff ($\\lambda \\approx 2.2$--$3.5$), while arXiv decays gradually ($\\lambda \\approx 1.0$) and retrain-chain shows no cliff ($\\lambda = 0.285$).}\n\\label{fig:jsd_decay}\n\\end{figure}\n\n\\paragraph{One-wash laundering (web text).}\nFor general web text, $\\Kempirical{=}2$ reflects concentrated information loss: 0v1 is near-trivially separable ($\\auc \\geq 0.92$), 1v2 drops by ${\\sim}$30\\,pp, and 2v3 falls below $\\theta$, so a single generation pass renders text indistinguishable from deeper content.\nNeither frontier LLMs nor alternative classifiers improve depth recovery beyond this boundary (McNemar $p > 0.05$; Appendix).\n\n\\paragraph{JSD decay and the discrimination boundary.}\nToken-level JSD between adjacent generations reveals two decay regimes (Figure~\\ref{fig:jsd_decay}): C4 models exhibit a sharp cliff (0v1 JSD exceeds 1v2 by 6--56$\\times$) followed by rapid convergence, while arXiv decays ${\\sim}$3$\\times$ slower ($\\lambda \\approx 1.0$ vs.\\ $2.9$).\nThe retrain-chain ($\\lambda = 0.285$, no cliff) reflects cumulative model-adaptation artifacts, extending $\\Kempirical$ to 7 (Appendix~\\ref{sec:jsd_extended}).\n\n\\paragraph{Graduated filtering failure.}\nFor web text, 2v3 $\\auc < \\theta$ across all configurations, so depth assignments beyond $d{=}2$ approximate random labels; the strategy ordering binary $>$ graduated aligns with $\\Kempirical{=}2$ (Section~\\ref{sec:filtering}).\n\n\\paragraph{Representation and scorer dependence.}\n$\\Kempirical$ is representation-dependent (frozen Qwen embeddings yield $\\Kempirical^{\\text{neural}} = 3$ vs.\\ $\\Kempirical^{\\text{neural}} = 2$ for Pythia and OLMo; Table~\\ref{tab:neural_probe_crossmodel}) and scorer-dependent (cross-family scoring reduces Wikipedia $\\Kempirical$ from 2 to 1, Appendix~\\ref{sec:wiki_domain}, while preserving C4 feature rankings $\\rho > 0.90$ and $\\Kempirical$ for 6/8 configurations, Section~\\ref{sec:transfer}).\n\n\\paragraph{Domain dependence of $\\Kempirical$.}\nC4 yields $\\Kempirical{=}2$ (8/9 configurations), Python code $\\Kempirical{=}2$ for four models across four architecture families ($\\Kempirical{=}1$ for capacity-limited Pythia-1.4B; Section~\\ref{sec:cross_domain}), arXiv $\\Kempirical{=}3$ (five models, four families), and Wikipedia $\\Kempirical{=}1$ (Appendix~\\ref{sec:wiki_domain}); the ordering correlates with structural complexity (Table~\\ref{tab:domain-ttr-entropy}).\nCode and C4 share $\\Kempirical{=}2$ but with shifted cliff positions: syntactic constraints preserve depth-1 signal in code, so domain structure governs both $\\Kempirical$ and the decay profile.\nThe only C4 exception (Mistral-7B, $\\Kempirical{=}1$) yields $\\Kempirical{=}2$ on code and $\\Kempirical{=}3$ on arXiv; a LaTeX ablation confirms content rather than formatting drives the arXiv difference (Appendix~\\ref{sec:latex_ablation}).\n\n\\paragraph{Surprisal attenuation and boundary variation.}\n\\label{sec:surprisal_attenuation}\nThe Mistral-7B exception ($\\Kempirical{=}1$) arises from compressed surprisal dynamic range (Table~\\ref{tab:cohens_d_full}); larger 0$\\to$1 surprisal drops correlate with higher 1v2 $\\auc$ (Table~\\ref{tab:borderline_features}), predicting $\\Kempirical$ may decrease beyond 14B.\n\n",
        "numLines": 40,
        "startLine": 1,
        "totalLines": 40
      }
    },
    "displayPath": "../../../docs/paper/discussion.tex"
  },
  "type": "attachment",
  "uuid": "fcae04c5-7e95-4de6-88d6-9925a872e915",
  "timestamp": "2026-05-19T13:07:41.516Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "crystalline-noodling-flask"
}
```

---


### Runtime record

_source line 201 · 2026-05-19T13:07:41.517Z_

```json
{
  "parentUuid": "fcae04c5-7e95-4de6-88d6-9925a872e915",
  "isSidechain": false,
  "attachment": {
    "type": "file",
    "filename": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c3.tex",
    "content": {
      "type": "text",
      "file": {
        "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c3.tex",
        "content": "\\section{$\\Kempirical$-Consistent Filtering}\n\\label{sec:filtering}\n\n$\\Kempirical{=}2$ predicts that binary curation should suffice for web text; we test this as a consistency check using prompt-chain documents (Qwen2.5-1.5B-Instruct, proof of concept).\nWe compare six strategies on 30{,}000 documents (depths 0--5): no-filter, binary-ours (15D LightGBM), binary-Drayson~\\citep{drayson2025}, graduated ($w = \\exp(-\\alpha \\hat{d})$, $\\alpha \\in \\{0.1,\\ldots,0.9\\}$), surprisal, and DSIR~\\citep{xie2023dsir}, fine-tuning via LoRA on MMLU and HellaSwag across 5 seeds (51 runs; 100\\% synthetic upper bound~\\cite{shumailov2024collapse, dohmatob2024model}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Filtering performance (mean $\\pm$ std, 5 seeds). Full $\\alpha$ sweep in Appendix~\\ref{sec:extended_limitations}.}\n\\label{tab:tab_filtering_main}\n\\resizebox{\\columnwidth}{!}{\\input{tables/tab_filtering_main}}\n\\end{table}\n\nBinary-ours reduces MMLU degradation from $-$1.53\\,pp (no-filter) to $-$0.77\\,pp ($p_{\\text{corr}} < 0.05$; Table~\\ref{tab:tab_filtering_main}); the modest absolute improvement reflects the constrained dynamic range of a fully synthetic setting.\nThe strategy ordering is consistent with $\\Kempirical{=}2$: binary exploits the one reliable boundary (0v1), while graduated strategies weight depths 2--5 using near-random classifier outputs, injecting noise; at $\\alpha{=}0.9$, graduated matches binary on HellaSwag but remains worse on MMLU ($p_{\\text{corr}} = 0.011$).\nCross-model replication on Pythia-1.4B confirms binary $>$ graduated (Appendix~\\ref{sec:pythia_filtering}); graduated weighting is indistinguishable from no-filter at all contamination ratios (10--50\\%; Appendix~\\ref{sec:dose_response}).\nOn arXiv ($\\Kempirical{=}3$), graduated filtering similarly fails: the statistical features separating depths 2 and 3 do not produce differential downstream training signal, so $\\Kempirical$ accurately measures discriminability but overestimates filtering utility (Appendix~\\ref{sec:extended_limitations}).\n",
        "numLines": 19,
        "startLine": 1,
        "totalLines": 19
      }
    },
    "displayPath": "../../../docs/paper/experiments_c3.tex"
  },
  "type": "attachment",
  "uuid": "6c641dde-a8c3-4f65-98a3-12556719e028",
  "timestamp": "2026-05-19T13:07:41.517Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "crystalline-noodling-flask"
}
```

---


### Runtime record

_source line 202 · 2026-05-19T13:07:41.815Z_

```json
{
  "parentUuid": "6c641dde-a8c3-4f65-98a3-12556719e028",
  "isSidechain": false,
  "attachment": {
    "type": "compact_file_reference",
    "filename": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex",
    "displayPath": "../../../docs/paper/appendix_extended.tex"
  },
  "type": "attachment",
  "uuid": "b005de76-c92c-45e5-bb5f-35edaa74ebd5",
  "timestamp": "2026-05-19T13:07:41.815Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "crystalline-noodling-flask"
}
```

---


### Runtime record

_source line 203 · 2026-05-19T13:07:41.772Z_

```json
{
  "parentUuid": "b005de76-c92c-45e5-bb5f-35edaa74ebd5",
  "isSidechain": false,
  "attachment": {
    "type": "file",
    "filename": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex",
    "content": {
      "type": "text",
      "file": {
        "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex",
        "content": "% EMNLP 2026 Main - ARR May 2026\n% Generational Depth Contamination\n\\documentclass[11pt]{article}\n\\usepackage[review]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{enumitem}\n\\usepackage{subcaption}\n\\usepackage{pifont}\n\\newcommand{\\cmark}{\\ding{51}}\n\\newcommand{\\xmark}{\\ding{55}}\n\\usepackage[section]{placeins}\n\n\\newcommand{\\Kstar}{{K^*}}\n\\newcommand{\\Kempirical}{{K^*_{\\text{empirical}}}}\n\\newcommand{\\Ktheory}{{K^*_{\\text{theory}}}}\n\\newcommand{\\auc}{\\text{AUC}}\n\\newcommand{\\jsd}{\\text{JSD}}\n\\newcommand{\\tpm}{\\ensuremath{\\,\\pm\\,}}\n\n\\title{Generational Depth Estimation of Recursive Synthetic Text:\\\\Measuring the Discrimination Boundary}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n% === Abstract ===\n\\begin{abstract}\nWeb-scale corpora are increasingly contaminated by recursive synthetic content, yet no method estimates a document's generational depth.\nWe measure the discrimination boundary $\\Kempirical$ (the maximum depth at which adjacent generations remain distinguishable) using 15 statistical features and an OBD-LightGBM classifier.\nAcross five architecture families (1B--14B), four source domains (three text, one code), and four decoding strategies at $\\theta{=}0.60$ (AUC decision threshold), $\\Kempirical{=}2$ for general web text (8/9 model configurations), $\\Kempirical{=}1$--$2$ for code (Python, model-dependent), and $\\Kempirical{=}3$ for structured academic text (arXiv).\nA single additional generation pass suffices to render first-generation synthetic web text indistinguishable from deeper synthetic content, a \\emph{one-wash laundering} effect.\nLargely generator-independent statistical features, computed via a fixed reference scorer, enable 80--92\\% accuracy retention among continuation-mode generators, and cross-scorer validation confirms that $\\Kempirical$ is largely robust to scorer choice.\nDownstream, $\\Kempirical$ characterizes discriminability boundaries that inform, but do not directly determine, filtering strategy; for web text ($\\Kempirical{=}2$), binary filtering aligns with the two-level discriminability structure.\n\\end{abstract}\n\n% === Section 1: Introduction ===\n\\input{introduction}\n\n% === Section 2: Related Work ===\n\\input{related_work}\n\n% === Section 3: Method ===\n\\input{method}\n\n% === Section 4: Experiments ===\n\\input{experiments_c1}\n\n% === Section 5: K*-Aware Data Filtering ===\n\\input{experiments_c3}\n\n% === Section 6: Discussion ===\n\\input{discussion}\n\n% === Section 7: Conclusion ===\n\\input{conclusion}\n\n% === Limitations (ACL required, unnumbered) ===\n\\clearpage\n\\section*{Limitations}\n\nOur findings are bounded by:\n(1)~\\emph{Scope}: model scale $\\leq$14B (5 architecture families), English text (C4, Wikipedia, arXiv) and Python code (CodeSearchNet), four decoding strategies; arXiv $\\Kempirical{=}3$ is confirmed with five models across four architecture families but with reduced sample size ($n{=}2{,}200$ per model); code domain tested with five models across four families (Qwen2.5-1.5B/7B, LLaMA-3.1-8B, Mistral-7B-v0.3, $\\Kempirical{=}2$; Pythia-1.4B, $\\Kempirical{=}1$ with 1v2 CI upper bound $> \\theta$); subsampling analysis indicates $n{\\geq}2{,}000$ suffices for 100\\% reliable $\\Kempirical$ determination (Appendix~\\ref{sec:power_curve}).\n(2)~\\emph{Protocol}: all main experiments use prompt-chain, which isolates text-intrinsic degradation from training dynamics; real-world contamination involves both prompting and retraining, and retrain-chain yields $\\Kempirical{=}7$ (both Qwen-1.5B and Pythia-1.4B LoRA; Appendix~\\ref{sec:extended_limitations}), so prompt-chain $\\Kempirical$ may underestimate discriminability in mixed settings.\n(3)~\\emph{Threshold}: $\\Kempirical$ ranges from 2--3 at $\\theta{=}0.55$ to 1 at $\\theta{=}0.70$; 8/9 configurations yield $\\Kempirical{=}2$ at $\\theta{=}0.60$ (Mistral-7B: $\\Kempirical{=}1$).\n(4)~\\emph{Marginal boundary}: Qwen-continuation's 1v2 CI lower bound exceeds $\\theta$ by only 0.002; cross-scorer validation drops this to $\\Kempirical{=}1$ (Section~\\ref{sec:transfer}). LLaMA-3.1-8B (C4) and Mistral-7B-v0.3 (code) represent the most marginal $\\Kempirical{=}2$ assignments, with 1v2 CI lower bounds within 0.3 percentage points of $\\theta$.\n(5)~\\emph{Feature set}: the 15D features yield a feature-set-specific lower bound ($\\Ktheory$ may be strictly higher); neural probe $\\Kempirical$ is model-dependent ($3$ for Qwen, $2$ for Pythia/OLMo).\n(6)~\\emph{Segment length}: $\\Kempirical{=}2$ confirmed for 128 and 256 tokens (CI lower $> \\theta$); 512 tokens yields point estimate $\\Kempirical{=}2$ but CI lower marginally below $\\theta$ ($0.5979$); the boundary weakens at longer generation lengths.\n(7)~\\emph{Curation applicability}: the filtering evaluation is validated on two architectures (Qwen2.5-1.5B-Instruct and Pythia-1.4B) with consistent strategy ordering (Appendix~\\ref{sec:pythia_filtering}), though absolute improvement remains small and effect sizes diminish at lower contamination ratios (10--50\\%; Appendix~\\ref{sec:dose_response}).\n(8)~\\emph{Family balance}: the Qwen2.5 family provides 5/9 configurations; though spanning three scales (1.5B, 7B, 14B) and two training variants (base, instruct), aggregate statistics weight this family more heavily than the four single-configuration families.\nAdditional limitations (cross-model scoring sensitivity, feature ranking variability at the 1v2 boundary, structural composition confound analysis) appear in Appendix~\\ref{sec:extended_limitations}.\n\n% === Ethics Statement (ACL required, unnumbered) ===\n\\section*{Ethics Statement}\n\nGenerational depth estimation is intended for data curation and corpus auditing, positive-sum applications that improve training data quality.\nOur experiments use publicly available corpora (C4, Wikipedia, arXiv abstracts) and do not involve personally identifiable information.\nA potential dual-use concern is that depth estimation techniques could inform adversarial strategies to evade detection (e.g., by calibrating rewriting to mimic earlier-generation statistics); we note that this risk is shared by all detection research and that the binary detection boundary ($\\auc \\geq 0.96$ at 0v1) remains robust.\nCode and generated corpora will be released upon acceptance to enable reproducibility.\n\n\\bibliography{references}\n\n\\input{appendix}\n\\input{appendix_extended}\n\n\\end{document}\n",
        "numLines": 96,
        "startLine": 1,
        "totalLines": 96
      }
    },
    "displayPath": "../../../docs/paper/main.tex"
  },
  "type": "attachment",
  "uuid": "4fa56017-cf56-403e-8c39-fec1c11267e3",
  "timestamp": "2026-05-19T13:07:41.772Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "crystalline-noodling-flask"
}
```

---


### Runtime record

_source line 204 · 2026-05-19T13:07:41.817Z_

```json
{
  "parentUuid": "4fa56017-cf56-403e-8c39-fec1c11267e3",
  "isSidechain": false,
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "AskUserQuestion",
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__review_reviewer_post_to_director",
      "mcp__agent-ml-research__verify_references"
    ],
    "addedLines": [
      "AskUserQuestion",
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__review_reviewer_post_to_director",
      "mcp__agent-ml-research__verify_references"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "8406ac35-bf0d-4f11-9b7d-38653a873f3a",
  "timestamp": "2026-05-19T13:07:41.817Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "crystalline-noodling-flask"
}
```

---


### Runtime record

_source line 205 · 2026-05-19T13:07:41.817Z_

```json
{
  "parentUuid": "8406ac35-bf0d-4f11-9b7d-38653a873f3a",
  "isSidechain": false,
  "attachment": {
    "type": "mcp_instructions_delta",
    "addedNames": [
      "agent-ml-research"
    ],
    "addedBlocks": [
      "## agent-ml-research\nML research experiment management tools"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "51533c78-529c-43bf-b76c-fbbaab4c6083",
  "timestamp": "2026-05-19T13:07:41.817Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "crystalline-noodling-flask"
}
```

---


### Runtime record

_source line 206_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 2 审稿请求]: ## Round 9（继续审稿）— Reviewer 2（新颖性 + 完整性 + 写作质量）  上轮评分：3.5 (Borderline Conference)。论文已大幅修订，请重点验证以下 open/in_progress issues 是否已充分修复。  ### 论文路径 `projects/gen-depth-contamination/docs/paper…",
  "leafUuid": "404439a0-c9ea-4107-8646-e13e9491d273",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77"
}
```

---


### Runtime record

_source line 207_

```json
{
  "type": "ai-title",
  "aiTitle": "Review paper on data contamination detection for EMNLP 2026",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77"
}
```

---


### Assistant

_source line 208 · 2026-05-19T13:07:50.213Z_

<details><summary>Logged reasoning block</summary>

```text
I need to complete the Round 2 re-review. I still need to:
1. Check for dashes in revised text
2. Check -ing phrase frequency
3. Verify a few specific issues (R8-N3 "sole"→"primary" all instances, R8-W4 transfer matrix, R8-W7 arXiv CI, R8-M4 Abstract terms)
4. Write and post the complete Round 2 review

Let me do the remaining checks in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "51533c78-529c-43bf-b76c-fbbaab4c6083",
  "isSidechain": false,
  "requestId": "req_011CbBykQEF87FrA7kvMtJa5",
  "type": "assistant",
  "uuid": "9e449052-1ba4-4149-b4e9-c67a6683ccee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "crystalline-noodling-flask",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014wRJbWGSM2G9aHsmPjmmBz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21881,
      "cache_read_input_tokens": 11841,
      "output_tokens": 664,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21881,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 664,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 21881,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21881
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

_source line 209 · 2026-05-19T13:07:51.192Z_

<details open><summary>🔧 Tool call — Grep · `toolu_017QrUqqS7ppFFNbpfy2LuFr`</summary>

```json
{
  "pattern": "—|–",
  "glob": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9e449052-1ba4-4149-b4e9-c67a6683ccee",
  "isSidechain": false,
  "requestId": "req_011CbBykQEF87FrA7kvMtJa5",
  "type": "assistant",
  "uuid": "5dd7350d-4e0d-4019-9793-d1d98bb462b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "crystalline-noodling-flask",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014wRJbWGSM2G9aHsmPjmmBz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21881,
      "cache_read_input_tokens": 11841,
      "output_tokens": 664,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21881,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 664,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 21881,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21881
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

_source line 210 · 2026-05-19T13:07:51.213Z_

<details><summary>↩ Tool result · `toolu_017QrUqqS7ppFFNbpfy2LuFr`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5dd7350d-4e0d-4019-9793-d1d98bb462b1",
  "isSidechain": false,
  "promptId": "12172553-d9aa-40c5-a42d-a4d4469a539a",
  "type": "user",
  "uuid": "5fc663f2-59bc-4883-91ab-a6d210bbc43a",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  },
  "sourceToolAssistantUUID": "5dd7350d-4e0d-4019-9793-d1d98bb462b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "crystalline-noodling-flask"
}
```

</details>

---


### Tool result

_source line 211 · 2026-05-19T13:07:54.669Z_

<details><summary>↩ Tool result · `toolu_01DN7TkzQmwppRNq4CpX8tnh`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:274:\caption{Bootstrap 95\% CI for arXiv cross-scorer (Pythia-1.4B) 2v3 boundary $\auc$ (10{,}000 resamples). Point estimates classify 3/4 generators as $\Kempirical{=}3$; strict CI lower-bound criterion confirms 2/4.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:314:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:319:As a sample-size control, subsampling C4 to $n{=}2{,}200$ (matching arXiv) yields $\Kempirical{=}1$ (1v2 $\auc = 0.601$, CI $[0.586, 0.616]$).
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:320:Reduced sample size widens confidence intervals and produces more conservative $\Kempirical$ estimates, arXiv's $\Kempirical{=}3$ at the same sample size therefore reflects genuine domain signal rather than a statistical artifact of smaller training sets.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:330:\caption{arXiv pairwise $\auc$ with and without LaTeX markup (Qwen-1.5B continuation). Removing formatting reduces 2v3 by ${\sim}$1.8\,pp but $\Kempirical$ remains at 3 (CI lower $> \theta$). LaTeX stripping fraction increases with depth (0.6\% at depth 0, 4.6\% at depth 5), deeper generations therefore produce proportionally more formatting tokens.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex:72:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:150:\captionof{table}{Domain $\times$ Model $\Kempirical$ matrix (scorer-controlled). Wikipedia values use cross-family scorer (Pythia-1.4B). $^*$OLMo arXiv: capacity failure. $^\dagger$Same-family scorer yields $\Kempirical{=}2$; controlled value shown. $^\ddagger$Borderline: Pythia CI upper $= 0.603$, Mistral CI lower $= 0.603$.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex:24:where $\mathrm{CI}_{\mathrm{low}}(\auc_{k-1,k})$ is the lower bound of a 95\% bootstrap confidence interval (1{,}000 resamples\footnote{Boundary-pair results in Table~\ref{tab:kstar_ci} use 1{,}000 resamples; arXiv cross-scorer CIs (Table~\ref{tab:arxiv_crossscorer_ci}) use 10{,}000 for tighter bounds at the margin.}) over the pairwise AUC (Area Under the ROC Curve) between depths $k{-}1$ and $k$, and $\theta = 0.60$ is a post-hoc operational threshold (motivated below).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f4d152fd-73f2-4981-94d2-a22b32e52534",
  "isSidechain": false,
  "promptId": "12172553-d9aa-40c5-a42d-a4d4469a539a",
  "type": "user",
  "uuid": "bd89ee35-e631-408b-bc74-c51b7f0ba065",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:274:\\caption{Bootstrap 95\\% CI for arXiv cross-scorer (Pythia-1.4B) 2v3 boundary $\\auc$ (10{,}000 resamples). Point estimates classify 3/4 generators as $\\Kempirical{=}3$; strict CI lower-bound criterion confirms 2/4.}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:314:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:319:As a sample-size control, subsampling C4 to $n{=}2{,}200$ (matching arXiv) yields $\\Kempirical{=}1$ (1v2 $\\auc = 0.601$, CI $[0.586, 0.616]$).\n/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:320:Reduced sample size widens confidence intervals and produces more conservative $\\Kempirical$ estimates, arXiv's $\\Kempirical{=}3$ at the same sample size therefore reflects genuine domain signal rather than a statistical artifact of smaller training sets.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:330:\\caption{arXiv pairwise $\\auc$ with and without LaTeX markup (Qwen-1.5B continuation). Removing formatting reduces 2v3 by ${\\sim}$1.8\\,pp but $\\Kempirical$ remains at 3 (CI lower $> \\theta$). LaTeX stripping fraction increases with depth (0.6\\% at depth 0, 4.6\\% at depth 5), deeper generations therefore produce proportionally more formatting tokens.}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex:72:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:150:\\captionof{table}{Domain $\\times$ Model $\\Kempirical$ matrix (scorer-controlled). Wikipedia values use cross-family scorer (Pythia-1.4B). $^*$OLMo arXiv: capacity failure. $^\\dagger$Same-family scorer yields $\\Kempirical{=}2$; controlled value shown. $^\\ddagger$Borderline: Pythia CI upper $= 0.603$, Mistral CI lower $= 0.603$.}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex:24:where $\\mathrm{CI}_{\\mathrm{low}}(\\auc_{k-1,k})$ is the lower bound of a 95\\% bootstrap confidence interval (1{,}000 resamples\\footnote{Boundary-pair results in Table~\\ref{tab:kstar_ci} use 1{,}000 resamples; arXiv cross-scorer CIs (Table~\\ref{tab:arxiv_crossscorer_ci}) use 10{,}000 for tighter bounds at the margin.}) over the pairwise AUC (Area Under the ROC Curve) between depths $k{-}1$ and $k$, and $\\theta = 0.60$ is a post-hoc operational threshold (motivated below).",
    "numLines": 8
  },
  "sourceToolAssistantUUID": "f4d152fd-73f2-4981-94d2-a22b32e52534",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "crystalline-noodling-flask"
}
```

</details>

---


### Tool call

_source line 212 · 2026-05-19T13:07:52.241Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01VQd8R8ibBsrvajxG8BwX8R`</summary>

```json
{
  "pattern": "\\bsole\\b",
  "glob": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5fc663f2-59bc-4883-91ab-a6d210bbc43a",
  "isSidechain": false,
  "requestId": "req_011CbBykQEF87FrA7kvMtJa5",
  "type": "assistant",
  "uuid": "4f28f172-ea2b-4f40-89ff-453378088926",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "crystalline-noodling-flask",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014wRJbWGSM2G9aHsmPjmmBz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21881,
      "cache_read_input_tokens": 11841,
      "output_tokens": 664,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21881,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 664,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 21881,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21881
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

_source line 213 · 2026-05-19T13:07:52.253Z_

<details><summary>↩ Tool result · `toolu_01VQd8R8ibBsrvajxG8BwX8R`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:512:The single mismatch is Qwen-1.5B-RW (rewrite mode), whose 2v3 AUC of 0.5893 lies above the LOFO-derived $\hat{\theta}{=}0.5725$ but below the global $\theta{=}0.60$; this configuration is also the sole rewrite-mode model, the discrepancy is therefore attributable to mode rather than threshold instability.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4f28f172-ea2b-4f40-89ff-453378088926",
  "isSidechain": false,
  "promptId": "12172553-d9aa-40c5-a42d-a4d4469a539a",
  "type": "user",
  "uuid": "f0aed139-d348-40cf-9287-cd3b66bf498e",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:512:The single mismatch is Qwen-1.5B-RW (rewrite mode), whose 2v3 AUC of 0.5893 lies above the LOFO-derived $\\hat{\\theta}{=}0.5725$ but below the global $\\theta{=}0.60$; this configuration is also the sole rewrite-mode model, the discrepancy is therefore attributable to mode rather than threshold instability.",
    "numLines": 1
  },
  "sourceToolAssistantUUID": "4f28f172-ea2b-4f40-89ff-453378088926",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "crystalline-noodling-flask"
}
```

</details>

---


### Tool call

_source line 214 · 2026-05-19T13:07:53.495Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01CwunrLvhuV4GNyY23H8Zsp`</summary>

```json
{
  "pattern": "transfer|cross-scorer|cross.scorer",
  "glob": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0aed139-d348-40cf-9287-cd3b66bf498e",
  "isSidechain": false,
  "requestId": "req_011CbBykQEF87FrA7kvMtJa5",
  "type": "assistant",
  "uuid": "fee4aa47-df20-4ef9-a7cc-400bc6b5b7f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "crystalline-noodling-flask",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014wRJbWGSM2G9aHsmPjmmBz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21881,
      "cache_read_input_tokens": 11841,
      "output_tokens": 664,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21881,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 664,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 21881,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21881
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

_source line 215 · 2026-05-19T13:07:53.511Z_

<details><summary>↩ Tool result · `toolu_01CwunrLvhuV4GNyY23H8Zsp`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex:6:\citet{gambetta2024surplexity} propose surplexity, a single surprisal-based collapse indicator; our 15-dimensional feature set captures richer distributional structure and enables cross-model transfer.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex:13:Recent work extends beyond binary labels to collaboration degree~\cite{cheng2025beyond}, contamination hierarchies~\cite{mehta2025beyond}, and multigenerator benchmarks~\cite{wang2024semeval}; robustness concerns arise under paraphrasing~\cite{sadasivan2023detect, krishna2023paraphrasing} and cross-mode transfer~\cite{hao2025rewrite}; CoDeC~\cite{zawalski2026codec} addresses contamination via membership inference.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:4:This section provides supporting tables for cross-scorer validation (Tables~\ref{tab:crossscorer}--\ref{tab:anova_crossscorer}), followed by extended limitations, ablation studies, and domain-specific analyses.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:74:Table~\ref{tab:theta_sensitivity} reports $\Kempirical$ across $\theta \in [0.55, 0.70]$ for representative configurations including arXiv and cross-scorer conditions.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:80:\caption{$\Kempirical$ as a function of $\theta$ across conditions. The \textbf{domain ordering} (arXiv $>$ web $\geq$ cross-scorer) and \textbf{bounded range} ($\Kempirical{\leq}4$) are preserved across $\theta \in [0.55, 0.70]$. The headline result (web $\Kempirical{=}2$, arXiv $\Kempirical{=}3$) holds for $\theta \in [0.575, 0.625]$.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:274:\caption{Bootstrap 95\% CI for arXiv cross-scorer (Pythia-1.4B) 2v3 boundary $\auc$ (10{,}000 resamples). Point estimates classify 3/4 generators as $\Kempirical{=}3$; strict CI lower-bound criterion confirms 2/4.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:314:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:619:\caption{Code domain cross-scorer validation: Pythia-1.4B scorer on Qwen2.5-1.5B code generations. $\Kempirical{=}2$ is preserved; five-fold minimum 1v2 $\auc = 0.6985$, well above $\theta{=}0.60$.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex:42:Largely generator-independent statistical features, computed via a fixed reference scorer, enable 80--92\% accuracy retention among continuation-mode generators, and cross-scorer validation confirms that $\Kempirical$ is largely robust to scorer choice.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex:75:(4)~\emph{Marginal boundary}: Qwen-continuation's 1v2 CI lower bound exceeds $\theta$ by only 0.002; cross-scorer validation drops this to $\Kempirical{=}1$ (Section~\ref{sec:transfer}). LLaMA-3.1-8B (C4) and Mistral-7B-v0.3 (code) represent the most marginal $\Kempirical{=}2$ assignments, with 1v2 CI lower bounds within 0.3 percentage points of $\theta$.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:61:The domain ordering (arXiv $>$ web $\geq$ cross-scorer) is preserved across the full $\theta$ range (Table~\ref{tab:theta_sensitivity}; Figure~\ref{fig:theta_sensitivity} in Appendix).
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:65:\label{sec:transfer}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:69:\includegraphics[width=0.85\columnwidth]{figures/fig3_transfer_heatmap.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:70:\caption{Cross-model transfer heatmap. Each cell shows 6-class ordinal accuracy when trained on the row model and tested on the column model, divided by in-domain accuracy (retention rate). Pythia$\leftrightarrow$OLMo: 90--92\%; Qwen-rewrite$\to$continuation: 61--63\%.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:71:\label{fig:transfer_heatmap}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:74:Continuation-mode classifiers transfer well across generators (Figure~\ref{fig:transfer_heatmap}; full matrix in Table~\ref{tab:s1_transfer}): Pythia$\leftrightarrow$OLMo retains 90--92\%, Qwen-cont$\leftrightarrow$Pythia 84--85\%, Qwen-cont$\leftrightarrow$OLMo 80--85\% (0v1 cross-model $\auc > 0.96$ for all pairs).
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:75:Qwen-rewrite classifiers transfer poorly (61--63\%), consistent with reliance on mode-specific artifacts rather than generalizable depth features.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:79:$\Kempirical$ is largely robust to scorer choice: across 22 cross-scorer configurations on C4 and arXiv, $\Kempirical$ was preserved in 20 cases; the two exceptions (Qwen-cont scored by Pythia on C4, Qwen-7B cross-scored on arXiv) are borderline, with AUC within 0.002 of $\theta$.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:92:Qwen-rewrite diverges (\texttt{freq\_entropy} dominates), consistent with its poor cross-model transfer (61--63\%).
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:100:The Qwen-only elevation reflects self-familiarity artifacts that transfer poorly (Section~\ref{sec:transfer}); the 15D features yield consistent $\Kempirical = 2$ across all families.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex:13:\caption{Token-level JSD between adjacent depth pairs on log scale. Blue band: min-max range across 8 C4 models (1B--14B) with $\Kempirical{=}2$; dashed purple: Mistral-7B ($\Kempirical{=}1$, cross-scorer validated); green: arXiv Pythia ($\Kempirical{=}3$); dotted red: retrain-chain ($\Kempirical{=}7$). C4 models exhibit a sharp cliff ($\lambda \approx 2.2$--$3.5$), while arXiv decays gradually ($\lambda \approx 1.0$) and retrain-chain shows no cliff ($\lambda = 0.285$).}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex:29:$\Kempirical$ is representation-dependent (frozen Qwen embeddings yield $\Kempirical^{\text{neural}} = 3$ vs.\ $\Kempirical^{\text{neural}} = 2$ for Pythia and OLMo; Table~\ref{tab:neural_probe_crossmodel}) and scorer-dependent (cross-family scoring reduces Wikipedia $\Kempirical$ from 2 to 1, Appendix~\ref{sec:wiki_domain}, while preserving C4 feature rankings $\rho > 0.90$ and $\Kempirical$ for 6/8 configurations, Section~\ref{sec:transfer}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex:24:where $\mathrm{CI}_{\mathrm{low}}(\auc_{k-1,k})$ is the lower bound of a 95\% bootstrap confidence interval (1{,}000 resamples\footnote{Boundary-pair results in Table~\ref{tab:kstar_ci} use 1{,}000 resamples; arXiv cross-scorer CIs (Table~\ref{tab:arxiv_crossscorer_ci}) use 10{,}000 for tighter bounds at the margin.}) over the pairwise AUC (Area Under the ROC Curve) between depths $k{-}1$ and $k$, and $\theta = 0.60$ is a post-hoc operational threshold (motivated below).
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex:46:Hand-crafted features enable cross-generator transfer without retraining and permit attribution of discriminative power to specific text properties.
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex:41:  \caption{Cross-model transfer accuracy matrix. Each cell reports the six-class depth classification accuracy of a detector trained on one model's outputs (row) and evaluated on another model's outputs (column). Diagonal entries (\textbf{bold}) indicate within-model performance. Transfer retention is computed as the ratio of off-diagonal accuracy to the geometric mean of the two corresponding diagonal entries.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex:42:  \label{tab:s1_transfer}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex:444:  \caption{Scorer sensitivity: $\Kempirical$ under self-scoring vs.\ cross-scoring. Self-scorer uses the generator's own model family for feature extraction; cross-scorer uses alternative models (Pythia-1.4B, OLMo-1B). $\Kempirical$ agreement across scorer conditions indicates the boundary is governed by the generation process. Cross-scoring reduces $\Kempirical$ only for the most marginal self-scorer condition (Qwen-continuation).}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/introduction.tex:30:  \item \textbf{Practical validation}: largely generator-independent features enable 80--92\% accuracy retention among tested continuation-mode configurations ($\rho > 0.90$; Section~\ref{sec:transfer}); as a consistency check, $\Kempirical{=}2$ correctly predicts binary $>$ graduated filtering for web text (Section~\ref{sec:filtering}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fee4aa47-df20-4ef9-a7cc-400bc6b5b7f7",
  "isSidechain": false,
  "promptId": "12172553-d9aa-40c5-a42d-a4d4469a539a",
  "type": "user",
  "uuid": "c1fc2a21-1373-4142-8686-73bee8f9906d",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex:6:\\citet{gambetta2024surplexity} propose surplexity, a single surprisal-based collapse indicator; our 15-dimensional feature set captures richer distributional structure and enables cross-model transfer.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex:13:Recent work extends beyond binary labels to collaboration degree~\\cite{cheng2025beyond}, contamination hierarchies~\\cite{mehta2025beyond}, and multigenerator benchmarks~\\cite{wang2024semeval}; robustness concerns arise under paraphrasing~\\cite{sadasivan2023detect, krishna2023paraphrasing} and cross-mode transfer~\\cite{hao2025rewrite}; CoDeC~\\cite{zawalski2026codec} addresses contamination via membership inference.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:4:This section provides supporting tables for cross-scorer validation (Tables~\\ref{tab:crossscorer}--\\ref{tab:anova_crossscorer}), followed by extended limitations, ablation studies, and domain-specific analyses.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:74:Table~\\ref{tab:theta_sensitivity} reports $\\Kempirical$ across $\\theta \\in [0.55, 0.70]$ for representative configurations including arXiv and cross-scorer conditions.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:80:\\caption{$\\Kempirical$ as a function of $\\theta$ across conditions. The \\textbf{domain ordering} (arXiv $>$ web $\\geq$ cross-scorer) and \\textbf{bounded range} ($\\Kempirical{\\leq}4$) are preserved across $\\theta \\in [0.55, 0.70]$. The headline result (web $\\Kempirical{=}2$, arXiv $\\Kempirical{=}3$) holds for $\\theta \\in [0.575, 0.625]$.}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:274:\\caption{Bootstrap 95\\% CI for arXiv cross-scorer (Pythia-1.4B) 2v3 boundary $\\auc$ (10{,}000 resamples). Point estimates classify 3/4 generators as $\\Kempirical{=}3$; strict CI lower-bound criterion confirms 2/4.}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:314:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:619:\\caption{Code domain cross-scorer validation: Pythia-1.4B scorer on Qwen2.5-1.5B code generations. $\\Kempirical{=}2$ is preserved; five-fold minimum 1v2 $\\auc = 0.6985$, well above $\\theta{=}0.60$.}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex:42:Largely generator-independent statistical features, computed via a fixed reference scorer, enable 80--92\\% accuracy retention among continuation-mode generators, and cross-scorer validation confirms that $\\Kempirical$ is largely robust to scorer choice.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.tex:75:(4)~\\emph{Marginal boundary}: Qwen-continuation's 1v2 CI lower bound exceeds $\\theta$ by only 0.002; cross-scorer validation drops this to $\\Kempirical{=}1$ (Section~\\ref{sec:transfer}). LLaMA-3.1-8B (C4) and Mistral-7B-v0.3 (code) represent the most marginal $\\Kempirical{=}2$ assignments, with 1v2 CI lower bounds within 0.3 percentage points of $\\theta$.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:61:The domain ordering (arXiv $>$ web $\\geq$ cross-scorer) is preserved across the full $\\theta$ range (Table~\\ref{tab:theta_sensitivity}; Figure~\\ref{fig:theta_sensitivity} in Appendix).\n/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:65:\\label{sec:transfer}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:69:\\includegraphics[width=0.85\\columnwidth]{figures/fig3_transfer_heatmap.pdf}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:70:\\caption{Cross-model transfer heatmap. Each cell shows 6-class ordinal accuracy when trained on the row model and tested on the column model, divided by in-domain accuracy (retention rate). Pythia$\\leftrightarrow$OLMo: 90--92\\%; Qwen-rewrite$\\to$continuation: 61--63\\%.}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:71:\\label{fig:transfer_heatmap}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:74:Continuation-mode classifiers transfer well across generators (Figure~\\ref{fig:transfer_heatmap}; full matrix in Table~\\ref{tab:s1_transfer}): Pythia$\\leftrightarrow$OLMo retains 90--92\\%, Qwen-cont$\\leftrightarrow$Pythia 84--85\\%, Qwen-cont$\\leftrightarrow$OLMo 80--85\\% (0v1 cross-model $\\auc > 0.96$ for all pairs).\n/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:75:Qwen-rewrite classifiers transfer poorly (61--63\\%), consistent with reliance on mode-specific artifacts rather than generalizable depth features.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:79:$\\Kempirical$ is largely robust to scorer choice: across 22 cross-scorer configurations on C4 and arXiv, $\\Kempirical$ was preserved in 20 cases; the two exceptions (Qwen-cont scored by Pythia on C4, Qwen-7B cross-scored on arXiv) are borderline, with AUC within 0.002 of $\\theta$.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:92:Qwen-rewrite diverges (\\texttt{freq\\_entropy} dominates), consistent with its poor cross-model transfer (61--63\\%).\n/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex:100:The Qwen-only elevation reflects self-familiarity artifacts that transfer poorly (Section~\\ref{sec:transfer}); the 15D features yield consistent $\\Kempirical = 2$ across all families.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex:13:\\caption{Token-level JSD between adjacent depth pairs on log scale. Blue band: min-max range across 8 C4 models (1B--14B) with $\\Kempirical{=}2$; dashed purple: Mistral-7B ($\\Kempirical{=}1$, cross-scorer validated); green: arXiv Pythia ($\\Kempirical{=}3$); dotted red: retrain-chain ($\\Kempirical{=}7$). C4 models exhibit a sharp cliff ($\\lambda \\approx 2.2$--$3.5$), while arXiv decays gradually ($\\lambda \\approx 1.0$) and retrain-chain shows no cliff ($\\lambda = 0.285$).}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/discussion.tex:29:$\\Kempirical$ is representation-dependent (frozen Qwen embeddings yield $\\Kempirical^{\\text{neural}} = 3$ vs.\\ $\\Kempirical^{\\text{neural}} = 2$ for Pythia and OLMo; Table~\\ref{tab:neural_probe_crossmodel}) and scorer-dependent (cross-family scoring reduces Wikipedia $\\Kempirical$ from 2 to 1, Appendix~\\ref{sec:wiki_domain}, while preserving C4 feature rankings $\\rho > 0.90$ and $\\Kempirical$ for 6/8 configurations, Section~\\ref{sec:transfer}).\n/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex:24:where $\\mathrm{CI}_{\\mathrm{low}}(\\auc_{k-1,k})$ is the lower bound of a 95\\% bootstrap confidence interval (1{,}000 resamples\\footnote{Boundary-pair results in Table~\\ref{tab:kstar_ci} use 1{,}000 resamples; arXiv cross-scorer CIs (Table~\\ref{tab:arxiv_crossscorer_ci}) use 10{,}000 for tighter bounds at the margin.}) over the pairwise AUC (Area Under the ROC Curve) between depths $k{-}1$ and $k$, and $\\theta = 0.60$ is a post-hoc operational threshold (motivated below).\n/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex:46:Hand-crafted features enable cross-generator transfer without retraining and permit attribution of discriminative power to specific text properties.\n/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex:41:  \\caption{Cross-model transfer accuracy matrix. Each cell reports the six-class depth classification accuracy of a detector trained on one model's outputs (row) and evaluated on another model's outputs (column). Diagonal entries (\\textbf{bold}) indicate within-model performance. Transfer retention is computed as the ratio of off-diagonal accuracy to the geometric mean of the two corresponding diagonal entries.}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex:42:  \\label{tab:s1_transfer}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex:444:  \\caption{Scorer sensitivity: $\\Kempirical$ under self-scoring vs.\\ cross-scoring. Self-scorer uses the generator's own model family for feature extraction; cross-scorer uses alternative models (Pythia-1.4B, OLMo-1B). $\\Kempirical$ agreement across scorer conditions indicates the boundary is governed by the generation process. Cross-scoring reduces $\\Kempirical$ only for the most marginal self-scorer condition (Qwen-continuation).}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/introduction.tex:30:  \\item \\textbf{Practical validation}: largely generator-independent features enable 80--92\\% accuracy retention among tested continuation-mode configurations ($\\rho > 0.90$; Section~\\ref{sec:transfer}); as a consistency check, $\\Kempirical{=}2$ correctly predicts binary $>$ graduated filtering for web text (Section~\\ref{sec:filtering}).",
    "numLines": 28
  },
  "sourceToolAssistantUUID": "fee4aa47-df20-4ef9-a7cc-400bc6b5b7f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "crystalline-noodling-flask"
}
```

</details>

---


### Tool call

_source line 216 · 2026-05-19T13:07:54.652Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01DN7TkzQmwppRNq4CpX8tnh`</summary>

```json
{
  "pattern": "arXiv.*CI|CI.*arXiv|confidence.*arXiv|arXiv.*confidence",
  "glob": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c1fc2a21-1373-4142-8686-73bee8f9906d",
  "isSidechain": false,
  "requestId": "req_011CbBykQEF87FrA7kvMtJa5",
  "type": "assistant",
  "uuid": "f4d152fd-73f2-4981-94d2-a22b32e52534",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "crystalline-noodling-flask",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014wRJbWGSM2G9aHsmPjmmBz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21881,
      "cache_read_input_tokens": 11841,
      "output_tokens": 664,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21881,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 664,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 21881,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21881
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

_source line 217_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 2 审稿请求]: ## Round 9（继续审稿）— Reviewer 2（新颖性 + 完整性 + 写作质量）  上轮评分：3.5 (Borderline Conference)。论文已大幅修订，请重点验证以下 open/in_progress issues 是否已充分修复。  ### 论文路径 `projects/gen-depth-contamination/docs/paper…",
  "leafUuid": "bd89ee35-e631-408b-bc74-c51b7f0ba065",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77"
}
```

---


### Runtime record

_source line 218_

```json
{
  "type": "ai-title",
  "aiTitle": "Review paper on data contamination detection for EMNLP 2026",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77"
}
```

---


### Tool call

_source line 219 · 2026-05-19T13:07:57.468Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HQxJmVxCX72PZn8azEFNuL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bd89ee35-e631-408b-bc74-c51b7f0ba065",
  "isSidechain": false,
  "requestId": "req_011CbBymLuM3uVKspKayZ81v",
  "type": "assistant",
  "uuid": "d5a98668-4888-45e0-902a-a3c837b2c26d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "crystalline-noodling-flask",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GArc2y5KgekET2xoHmtXPq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5205,
      "cache_read_input_tokens": 33722,
      "output_tokens": 233,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5205,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 233,
          "cache_read_input_tokens": 33722,
          "cache_creation_input_tokens": 5205,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5205
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

_source line 220 · 2026-05-19T13:07:57.473Z_

<details><summary>↩ Tool result · `toolu_01HQxJmVxCX72PZn8azEFNuL`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate generational depth estimation on nine model configurations spanning five architecture families:
5	Pythia-1.4B, OLMo-1B, Qwen2.5-1.5B-Instruct (rewrite and continuation), Qwen2.5-1.5B (base), Qwen2.5-7B, Qwen2.5-14B, LLaMA-3.1-8B, and Mistral-7B, all in continuation mode except where noted.
6	All experiments use the OBD-LightGBM classifier with the 15-dimensional feature set (Section~\ref{sec:method}), with 5{,}000 texts per depth level (generations 0--5; power analysis in Appendix~\ref{sec:power_curve}).
7	
8	%% ====================================================================
9	\subsection{\texorpdfstring{$\Kempirical \leq 2$}{K*<=2} Across Model Configurations (C4)}
10	\label{sec:kstar_boundary}
11	
12	\begin{table*}[t]
13	\centering
14	\small
15	\caption{Pairwise $\auc$ for adjacent depth pairs with bootstrap 95\% CIs and permutation $p$-values for boundary rows.
16	$\Kempirical = 2$ requires 1v2 CI lower bound $> \theta{=}0.60$ and 2v3 CI lower bound $\leq \theta$ (Eq.~\ref{eq:kstar}).
17	Extended results (all models) in Table~\ref{tab:kstar_ci_extended}.}
18	\label{tab:kstar_ci}
19	\begin{tabular}{lcccccccccc}
20	\toprule
21	 & \multicolumn{2}{c}{Qwen-rw} & \multicolumn{2}{c}{Pythia} & \multicolumn{2}{c}{OLMo} & \multicolumn{2}{c}{Qwen-cont} & \multicolumn{2}{c}{Qwen-7B\rlap{$^\ddagger$}} \\
22	\cmidrule(lr){2-3}\cmidrule(lr){4-5}\cmidrule(lr){6-7}\cmidrule(lr){8-9}\cmidrule(lr){10-11}
23	 & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI & $\auc$ & 95\% CI \\
24	\midrule
25	0v1 & .9956 & & .9932 & & .9970 & & .9971 & & .9638 & [.961,\,.967] \\
26	1v2 & .6955 & [.686,\,.704]\rlap{$^*$} & .6539 & [.645,\,.663]\rlap{$^*$} & .6145 & [.605,\,.625]\rlap{$^*$} & .6112 & [.602,\,.621]\rlap{$^*$} & .6168 & [.608,\,.626]\rlap{$^*$} \\
27	2v3 & .5893 & [.580,\,.599] & .5514 & [.542,\,.563] & .5496 & [.540,\,.560] & .5609 & [.551,\,.571] & .5492 & [.539,\,.559] \\
28	3v4 & .5435 & & .5152 & & .5091 & & .5409 & & .5276 & \\
29	4v5 & .5340 & & .5136 & & .5045 & & .5141 & & .5085 & \\
30	\bottomrule
31	\multicolumn{11}{l}{\footnotesize $^*$Permutation $p < 0.001$ for all 1v2 comparisons shown.} \\
32	\multicolumn{11}{l}{\footnotesize $^\ddagger$Generator: Qwen2.5-7B (fp16); scorer: Qwen2.5-1.5B.}
33	\end{tabular}
34	\end{table*}
35	
36	\begin{figure}[t]
37	\centering
38	\includegraphics[width=\columnwidth]{figures/fig2_auc_decay.pdf}
39	\caption{Pairwise $\auc$ decay across depth pairs for model-mode configurations (solid) and decoding strategies (dashed). The horizontal dashed line marks $\theta = 0.60$.}
40	\label{fig:auc_decay}
41	\end{figure}
42	
43	Table~\ref{tab:kstar_ci} and Figure~\ref{fig:auc_decay} show $\Kempirical \leq 2$ across all 9 model configurations: 8/9 yield $\Kempirical{=}2$ (1v2 $\auc$ range: 0.6112--0.6955; all CI lower bounds $> \theta$; permutation $p < 0.001$), while Mistral-7B is the only exception ($\Kempirical{=}1$; 1v2 $\auc = 0.594$, below $\theta$; Section~\ref{sec:boundary_cases}).
44	LLaMA-3.1-8B yields $\Kempirical{=}2$ (0v1 $\auc = 0.9225$, 1v2 $\auc = 0.6123$, 95\% CI $[0.603, 0.622]$; borderline: 1/5 folds falls below $\theta$; Table~\ref{tab:kstar_ci_extended}).
45	Among non-Qwen families: Pythia and OLMo yield clear $\Kempirical{=}2$, LLaMA is borderline (CI lower $= 0.603$), and Mistral yields $\Kempirical{=}1$; the Qwen-heavy configuration space (5/9) does not alter this per-family pattern.
46	All four decoding strategies likewise yield $\Kempirical{=}2$ (Table~\ref{tab:s2_decoding}).
47	The 1v2 spread due to generation mode ($\Delta = 8.4$\,pp within Qwen) exceeds the spread across models in continuation mode ($\Delta = 3.9$\,pp).
48	
49	\paragraph{Scale and instruction-tuning invariance.}
50	$\Kempirical{=}2$ persists from 1.5B through 14B: Qwen-14B (1v2 $\auc = 0.621$ $[0.612, 0.630]$), Qwen-7B ($0.6168$ $[0.608, 0.626]$), and LLaMA-3.1-8B ($0.6123$) all exceed $\theta$, despite progressively reduced 0v1 signal (0.960 at 14B, 0.964 at 7B, 0.923 at 8B vs.\ $> 0.99$ at $\leq$1.5B).
51	A base-vs.-instruct ablation at 1.5B likewise yields $\Kempirical = 2$ (1v2 $\auc = 0.626$); the boundary is not an instruction-tuning artifact.
52	
53	\begin{figure}[t]
54	\centering
55	\includegraphics[width=\columnwidth]{figures/fig_kstar_theta.pdf}
56	\caption{$\Kempirical(\theta)$ sensitivity curve for six configurations. $\Kempirical$: maximum discriminable depth; $\theta$: AUC decision threshold. All configurations yield $\Kempirical{=}2$ at $\theta{=}0.60$ (dashed line). At $\theta{=}0.70$, all drop to $\Kempirical{=}1$.}
57	\label{fig:kstar_theta}
58	\end{figure}
59	
60	Figure~\ref{fig:kstar_theta} shows $\Kempirical$ as a function of $\theta$: web text $\Kempirical{=}2$ is stable across a 5\,pp window ($\theta \in [0.575, 0.625]$), with a gradual transition to $\Kempirical{=}3$ at $\theta{=}0.55$ (two Qwen configurations) and $\Kempirical{=}1$ at $\theta{=}0.70$.
61	The domain ordering (arXiv $>$ web $\geq$ cross-scorer) is preserved across the full $\theta$ range (Table~\ref{tab:theta_sensitivity}; Figure~\ref{fig:theta_sensitivity} in Appendix).
62	
63	%% ====================================================================
64	\subsection{Largely Generator-Independent Transfer}
65	\label{sec:transfer}
66	
67	\begin{figure}[t]
68	\centering
69	\includegraphics[width=0.85\columnwidth]{figures/fig3_transfer_heatmap.pdf}
70	\caption{Cross-model transfer heatmap. Each cell shows 6-class ordinal accuracy when trained on the row model and tested on the column model, divided by in-domain accuracy (retention rate). Pythia$\leftrightarrow$OLMo: 90--92\%; Qwen-rewrite$\to$continuation: 61--63\%.}
71	\label{fig:transfer_heatmap}
72	\end{figure}
73	
74	Continuation-mode classifiers transfer well across generators (Figure~\ref{fig:transfer_heatmap}; full matrix in Table~\ref{tab:s1_transfer}): Pythia$\leftrightarrow$OLMo retains 90--92\%, Qwen-cont$\leftrightarrow$Pythia 84--85\%, Qwen-cont$\leftrightarrow$OLMo 80--85\% (0v1 cross-model $\auc > 0.96$ for all pairs).
75	Qwen-rewrite classifiers transfer poorly (61--63\%), consistent with reliance on mode-specific artifacts rather than generalizable depth features.
76	
77	\paragraph{Cross-scorer validation.}
78	Replacing the self-scorer with Pythia-1.4B or OLMo-1B preserves feature rankings ($\rho > 0.90$; Table~\ref{tab:crossscorer}).
79	$\Kempirical$ is largely robust to scorer choice: across 22 cross-scorer configurations on C4 and arXiv, $\Kempirical$ was preserved in 20 cases; the two exceptions (Qwen-cont scored by Pythia on C4, Qwen-7B cross-scored on arXiv) are borderline, with AUC within 0.002 of $\theta$.
80	Qwen-cont is the most scorer-sensitive continuation-mode configuration: its self-scored 1v2 CI lower bound exceeds $\theta$ by only 0.2\,pp (Table~\ref{tab:kstar_ci}), and cross-family scoring pushes it below $\theta$.
81	For arXiv, Pythia-1.4B cross-scoring preserves $\Kempirical{=}3$ for 3/4 generators (2v3 $\auc$: 0.608--0.632); Qwen-7B drops to borderline $\Kempirical{=}2$ ($\Delta = -2.7$\,pp), consistent with Qwen scorer sensitivity on C4 and Wikipedia (Table~\ref{tab:arxiv_crossscorer_ci}).
82	A three-way ANOVA (Generator $\times$ Scorer $\times$ Depth-Pair; $N{=}300$; Table~\ref{tab:anova_crossscorer}) confirms that Depth-Pair dominates variance ($\eta^2_p = 0.998$); Scorer is statistically significant ($p < .001$) but practically minor ($\eta^2_p = 0.192$), consistent with a detectable but small scorer influence on absolute discriminability.
83	
84	%% ====================================================================
85	\subsection{Feature Ordering and Generation Mode}
86	\label{sec:feature_degradation}
87	\label{sec:generation_mode}
88	
89	Among continuation-mode models, single-feature $\auc$ rankings are highly correlated ($\rho \geq 0.85$; Table~\ref{tab:top_features}).
90	The top-3 features (\texttt{surp\_d1\_std}, \texttt{surp\_std}, \texttt{surp\_d2\_std}) are shared across all three families: autoregressive generation progressively damps surprisal variability; however, no single feature subset of size ${<}8$ reliably sustains $\Kempirical{=}2$ (Appendix~\ref{sec:feature_subset}).
91	A feature group ablation (Appendix~\ref{sec:feature_ablation}) confirms that surprisal (base) dominates on arXiv (single AUC $= 0.809$, LOO $\Delta = 0.031$); on C4 and Wikipedia, all LOO drops fall within fold variance ($\leq 0.007$).
92	Qwen-rewrite diverges (\texttt{freq\_entropy} dominates), consistent with its poor cross-model transfer (61--63\%).
93	Within Qwen, rewrite yields 1v2 $\auc = 0.6955$ vs.\ continuation's $0.6112$ ($\Delta = +8.4$\,pp); continuation mode is therefore recommended as the canonical condition.
94	
95	%% ====================================================================
96	\subsection{Neural Probe}
97	\label{sec:neural_probe}
98	
99	Replacing the 15D features with frozen encoder hidden states (MLP probe, 5{,}000 texts per depth; Table~\ref{tab:neural_probe_crossmodel}), Qwen achieves $\Kempirical^{\text{neural}} = 3$ (2v3 $\auc = 0.6159$), while Pythia and OLMo remain at $\Kempirical^{\text{neural}} = 2$ ($\auc_{2v3}$: 0.5963, 0.5892).
100	The Qwen-only elevation reflects self-familiarity artifacts that transfer poorly (Section~\ref{sec:transfer}); the 15D features yield consistent $\Kempirical = 2$ across all families.
101	
102	\noindent\begin{minipage}{\columnwidth}
103	\centering
104	\footnotesize
105	\captionof{table}{Neural probe pairwise AUC using frozen-encoder MLP. Each cell reports AUC for classifying depth $d$ vs.\ $d{+}1$ text. $\Kempirical^{\text{neural}}$: maximum depth where AUC exceeds $\theta = 0.60$.}
106	\label{tab:neural_probe_crossmodel}
107	\resizebox{\columnwidth}{!}{%
108	\begin{tabular}{lccc}
109	\toprule
110	\textbf{Model} & \textbf{2v3 $\auc$} & \textbf{95\% CI} & $\Kempirical^{\text{neural}}$ \\
111	\midrule
112	Qwen-1.5B  & 0.6159 & $[0.610,\,0.622]$ & 3 \\
113	Pythia-1.4B & 0.5963 & $[0.589,\,0.603]$ & 2 \\
114	OLMo-1B    & 0.5892 & $[0.582,\,0.597]$ & 2 \\
115	\bottomrule
116	\end{tabular}}
117	\end{minipage}
118	
119	%% ====================================================================
120	\subsection{Cross-Domain Variation}
121	\label{sec:cross_domain}
122	
123	The preceding experiments use C4 (general web text).
124	To test whether $\Kempirical$ reflects domain structure or model identity, we evaluate on arXiv abstracts ($n{=}2{,}200$ per model) and Wikipedia ($n{=}5{,}000$ per model) across six model configurations spanning four architecture families (Table~\ref{tab:domain_kstar}).
125	
126	\paragraph{arXiv ($\Kempirical{=}3$): five-model cross-validation.}
127	All five domain-competent models yield $\Kempirical{=}3$ on arXiv, with boundary-pair $\auc$ (2v3) ranging from 0.6215 to 0.6545, all exceeding $\theta$.
128	The elevated signal reflects higher per-generation distributional shift (1v2 JSD $= 0.077$ vs.\ ${\sim}0.01$ for C4): formulaic features (LaTeX formatting, citation patterns, mathematical notation) degrade slowly under autoregressive generation and supply persistent depth signal across four architecture families and 1.4B--8B parameters.
129	Removing LaTeX markup reduces 2v3 AUC by ${\sim}$1.8\,pp but preserves $\Kempirical{=}3$ (CI lower $= 0.610 > \theta$; Table~\ref{tab:latex_ablation}); content-level properties dominate.
130	OLMo-1B is a capacity failure (0v1 JSD $= 0.33$, near-total information loss), not a counter-example.
131	Mistral-7B provides the strongest domain-dependence evidence: $\Kempirical{=}1$ on C4 (Section~\ref{sec:boundary_cases}) but $\Kempirical{=}3$ on arXiv: domain structure alone can shift $\Kempirical$ by two levels within the same model.
132	
133	\paragraph{Wikipedia ($\Kempirical{=}1$): single-generation saturation.}
134	With scorer confound controlled (Pythia-1.4B for Qwen generators; Qwen-1.5B, itself cross-family, for all others), all six models yield $\Kempirical{=}1$ on Wikipedia: 1v2 $\auc$ ranges from 0.499 (OLMo) to 0.595 (LLaMA), all below $\theta$.
135	Wikipedia represents the simplest domain tested; its encyclopedic regularity provides minimal structural signal beyond the 0v1 boundary, and a single generation pass suffices for complete saturation.
136	Same-family scoring inflates Qwen $\Kempirical$ to 2 on Wikipedia ($\Delta = +2.4$\,pp); cross-family scoring controls this bias without affecting C4 results (Appendix~\ref{sec:wiki_domain}).
137	
138	\paragraph{Code ($\Kempirical{=}1$--$2$): cross-modality confirmation.}
139	Python functions from CodeSearchNet~\cite{husain2019codesearchnet} ($n{=}5{,}000$) yield $\Kempirical{=}2$ for four models (Qwen-1.5B/7B, LLaMA-8B, Mistral-7B; 1v2 $\auc$: 0.615--0.739; Table~\ref{tab:code_crossmodel_kstar}), but $\Kempirical{=}1$ for capacity-limited Pythia-1.4B ($\auc = 0.598$, CI upper $= 0.603$).
140	Code matches C4 despite a different modality, with the same sharp 2v3 collapse (JSD ratio $11.7$--$13.5\times$).
141	Cross-family scorer validation confirms Code $\Kempirical{=}2$ is text-intrinsic ($\Delta \leq 1.9$\,pp; Appendix~\ref{sec:code_domain}).
142	
143	\paragraph{Domain as the primary factor.}
144	With the scorer confound controlled, the domain ordering is: arXiv ($\Kempirical{=}3$) $>$ C4 ($\Kempirical{=}2$) $\geq$ Code ($\Kempirical{=}1$--$2$) $\geq$ Wikipedia ($\Kempirical{=}1$).
145	Scale (1B--14B) and architecture do not alter the C4/arXiv/Wikipedia ordering; code shows model-dependent variation at the boundary, but domain structural complexity remains the primary determinant of $\Kempirical$.
146	
147	\noindent\begin{minipage}{\columnwidth}
148	\centering
149	\footnotesize
150	\captionof{table}{Domain $\times$ Model $\Kempirical$ matrix (scorer-controlled). Wikipedia values use cross-family scorer (Pythia-1.4B). $^*$OLMo arXiv: capacity failure. $^\dagger$Same-family scorer yields $\Kempirical{=}2$; controlled value shown. $^\ddagger$Borderline: Pythia CI upper $= 0.603$, Mistral CI lower $= 0.603$.}
151	\label{tab:domain_kstar}
152	\resizebox{\columnwidth}{!}{%
153	\begin{tabular}{lcccc}
154	\toprule
155	\textbf{Model} & \textbf{C4} & \textbf{Code} & \textbf{arXiv} & \textbf{Wikipedia} \\
156	\midrule
157	Qwen-1.5B    & 2 & 2 & 3 & 1$^\dagger$ \\
158	Qwen-7B      & 2 & 2 & 3 & 1$^\dagger$ \\
159	Pythia-1.4B  & 2 & 1$^\ddagger$ & 3 & 1 \\
160	OLMo-1B      & 2 & --- & 1$^*$ & 1 \\
161	LLaMA-3.1-8B & 2 & 2 & 3 & 1 \\
162	Mistral-7B   & 1 & 2$^\ddagger$ & 3 & 1 \\
163	\bottomrule
164	\end{tabular}}
165	\end{minipage}
166	
167	%% ====================================================================
168	\subsection{Binary Detector Confidence}
169	\label{sec:binary_confidence}
170	
171	Binary detectors (DivEye~\cite{basani2026diveye}, Binoculars~\cite{hans2024binoculars}) show moderate rank correlations with depth ($|\rho| = 0.06$--$0.46$; Table~\ref{tab:s9_binary_spearman}) but fail as depth proxies: 6-class accuracy is at or below chance ($\leq 0.199$ vs.\ 0.167 baseline), pairwise $\auc$ yields $\Kempirical^{\text{binary}} \leq 1$, and multiple conditions exhibit non-monotonic AUC at deeper pairs.
172	The observed correlation is an artifact of 0v1 separation rather than fine-grained depth signal.
173	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d5a98668-4888-45e0-902a-a3c837b2c26d",
  "isSidechain": false,
  "promptId": "12172553-d9aa-40c5-a42d-a4d4469a539a",
  "type": "user",
  "uuid": "11d69311-baa3-4ac0-9ae8-71c2d4bcfd62",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/experiments_c1.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate generational depth estimation on nine model configurations spanning five architecture families:\nPythia-1.4B, OLMo-1B, Qwen2.5-1.5B-Instruct (rewrite and continuation), Qwen2.5-1.5B (base), Qwen2.5-7B, Qwen2.5-14B, LLaMA-3.1-8B, and Mistral-7B, all in continuation mode except where noted.\nAll experiments use the OBD-LightGBM classifier with the 15-dimensional feature set (Section~\\ref{sec:method}), with 5{,}000 texts per depth level (generations 0--5; power analysis in Appendix~\\ref{sec:power_curve}).\n\n%% ====================================================================\n\\subsection{\\texorpdfstring{$\\Kempirical \\leq 2$}{K*<=2} Across Model Configurations (C4)}\n\\label{sec:kstar_boundary}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Pairwise $\\auc$ for adjacent depth pairs with bootstrap 95\\% CIs and permutation $p$-values for boundary rows.\n$\\Kempirical = 2$ requires 1v2 CI lower bound $> \\theta{=}0.60$ and 2v3 CI lower bound $\\leq \\theta$ (Eq.~\\ref{eq:kstar}).\nExtended results (all models) in Table~\\ref{tab:kstar_ci_extended}.}\n\\label{tab:kstar_ci}\n\\begin{tabular}{lcccccccccc}\n\\toprule\n & \\multicolumn{2}{c}{Qwen-rw} & \\multicolumn{2}{c}{Pythia} & \\multicolumn{2}{c}{OLMo} & \\multicolumn{2}{c}{Qwen-cont} & \\multicolumn{2}{c}{Qwen-7B\\rlap{$^\\ddagger$}} \\\\\n\\cmidrule(lr){2-3}\\cmidrule(lr){4-5}\\cmidrule(lr){6-7}\\cmidrule(lr){8-9}\\cmidrule(lr){10-11}\n & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI & $\\auc$ & 95\\% CI \\\\\n\\midrule\n0v1 & .9956 & & .9932 & & .9970 & & .9971 & & .9638 & [.961,\\,.967] \\\\\n1v2 & .6955 & [.686,\\,.704]\\rlap{$^*$} & .6539 & [.645,\\,.663]\\rlap{$^*$} & .6145 & [.605,\\,.625]\\rlap{$^*$} & .6112 & [.602,\\,.621]\\rlap{$^*$} & .6168 & [.608,\\,.626]\\rlap{$^*$} \\\\\n2v3 & .5893 & [.580,\\,.599] & .5514 & [.542,\\,.563] & .5496 & [.540,\\,.560] & .5609 & [.551,\\,.571] & .5492 & [.539,\\,.559] \\\\\n3v4 & .5435 & & .5152 & & .5091 & & .5409 & & .5276 & \\\\\n4v5 & .5340 & & .5136 & & .5045 & & .5141 & & .5085 & \\\\\n\\bottomrule\n\\multicolumn{11}{l}{\\footnotesize $^*$Permutation $p < 0.001$ for all 1v2 comparisons shown.} \\\\\n\\multicolumn{11}{l}{\\footnotesize $^\\ddagger$Generator: Qwen2.5-7B (fp16); scorer: Qwen2.5-1.5B.}\n\\end{tabular}\n\\end{table*}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig2_auc_decay.pdf}\n\\caption{Pairwise $\\auc$ decay across depth pairs for model-mode configurations (solid) and decoding strategies (dashed). The horizontal dashed line marks $\\theta = 0.60$.}\n\\label{fig:auc_decay}\n\\end{figure}\n\nTable~\\ref{tab:kstar_ci} and Figure~\\ref{fig:auc_decay} show $\\Kempirical \\leq 2$ across all 9 model configurations: 8/9 yield $\\Kempirical{=}2$ (1v2 $\\auc$ range: 0.6112--0.6955; all CI lower bounds $> \\theta$; permutation $p < 0.001$), while Mistral-7B is the only exception ($\\Kempirical{=}1$; 1v2 $\\auc = 0.594$, below $\\theta$; Section~\\ref{sec:boundary_cases}).\nLLaMA-3.1-8B yields $\\Kempirical{=}2$ (0v1 $\\auc = 0.9225$, 1v2 $\\auc = 0.6123$, 95\\% CI $[0.603, 0.622]$; borderline: 1/5 folds falls below $\\theta$; Table~\\ref{tab:kstar_ci_extended}).\nAmong non-Qwen families: Pythia and OLMo yield clear $\\Kempirical{=}2$, LLaMA is borderline (CI lower $= 0.603$), and Mistral yields $\\Kempirical{=}1$; the Qwen-heavy configuration space (5/9) does not alter this per-family pattern.\nAll four decoding strategies likewise yield $\\Kempirical{=}2$ (Table~\\ref{tab:s2_decoding}).\nThe 1v2 spread due to generation mode ($\\Delta = 8.4$\\,pp within Qwen) exceeds the spread across models in continuation mode ($\\Delta = 3.9$\\,pp).\n\n\\paragraph{Scale and instruction-tuning invariance.}\n$\\Kempirical{=}2$ persists from 1.5B through 14B: Qwen-14B (1v2 $\\auc = 0.621$ $[0.612, 0.630]$), Qwen-7B ($0.6168$ $[0.608, 0.626]$), and LLaMA-3.1-8B ($0.6123$) all exceed $\\theta$, despite progressively reduced 0v1 signal (0.960 at 14B, 0.964 at 7B, 0.923 at 8B vs.\\ $> 0.99$ at $\\leq$1.5B).\nA base-vs.-instruct ablation at 1.5B likewise yields $\\Kempirical = 2$ (1v2 $\\auc = 0.626$); the boundary is not an instruction-tuning artifact.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_kstar_theta.pdf}\n\\caption{$\\Kempirical(\\theta)$ sensitivity curve for six configurations. $\\Kempirical$: maximum discriminable depth; $\\theta$: AUC decision threshold. All configurations yield $\\Kempirical{=}2$ at $\\theta{=}0.60$ (dashed line). At $\\theta{=}0.70$, all drop to $\\Kempirical{=}1$.}\n\\label{fig:kstar_theta}\n\\end{figure}\n\nFigure~\\ref{fig:kstar_theta} shows $\\Kempirical$ as a function of $\\theta$: web text $\\Kempirical{=}2$ is stable across a 5\\,pp window ($\\theta \\in [0.575, 0.625]$), with a gradual transition to $\\Kempirical{=}3$ at $\\theta{=}0.55$ (two Qwen configurations) and $\\Kempirical{=}1$ at $\\theta{=}0.70$.\nThe domain ordering (arXiv $>$ web $\\geq$ cross-scorer) is preserved across the full $\\theta$ range (Table~\\ref{tab:theta_sensitivity}; Figure~\\ref{fig:theta_sensitivity} in Appendix).\n\n%% ====================================================================\n\\subsection{Largely Generator-Independent Transfer}\n\\label{sec:transfer}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.85\\columnwidth]{figures/fig3_transfer_heatmap.pdf}\n\\caption{Cross-model transfer heatmap. Each cell shows 6-class ordinal accuracy when trained on the row model and tested on the column model, divided by in-domain accuracy (retention rate). Pythia$\\leftrightarrow$OLMo: 90--92\\%; Qwen-rewrite$\\to$continuation: 61--63\\%.}\n\\label{fig:transfer_heatmap}\n\\end{figure}\n\nContinuation-mode classifiers transfer well across generators (Figure~\\ref{fig:transfer_heatmap}; full matrix in Table~\\ref{tab:s1_transfer}): Pythia$\\leftrightarrow$OLMo retains 90--92\\%, Qwen-cont$\\leftrightarrow$Pythia 84--85\\%, Qwen-cont$\\leftrightarrow$OLMo 80--85\\% (0v1 cross-model $\\auc > 0.96$ for all pairs).\nQwen-rewrite classifiers transfer poorly (61--63\\%), consistent with reliance on mode-specific artifacts rather than generalizable depth features.\n\n\\paragraph{Cross-scorer validation.}\nReplacing the self-scorer with Pythia-1.4B or OLMo-1B preserves feature rankings ($\\rho > 0.90$; Table~\\ref{tab:crossscorer}).\n$\\Kempirical$ is largely robust to scorer choice: across 22 cross-scorer configurations on C4 and arXiv, $\\Kempirical$ was preserved in 20 cases; the two exceptions (Qwen-cont scored by Pythia on C4, Qwen-7B cross-scored on arXiv) are borderline, with AUC within 0.002 of $\\theta$.\nQwen-cont is the most scorer-sensitive continuation-mode configuration: its self-scored 1v2 CI lower bound exceeds $\\theta$ by only 0.2\\,pp (Table~\\ref{tab:kstar_ci}), and cross-family scoring pushes it below $\\theta$.\nFor arXiv, Pythia-1.4B cross-scoring preserves $\\Kempirical{=}3$ for 3/4 generators (2v3 $\\auc$: 0.608--0.632); Qwen-7B drops to borderline $\\Kempirical{=}2$ ($\\Delta = -2.7$\\,pp), consistent with Qwen scorer sensitivity on C4 and Wikipedia (Table~\\ref{tab:arxiv_crossscorer_ci}).\nA three-way ANOVA (Generator $\\times$ Scorer $\\times$ Depth-Pair; $N{=}300$; Table~\\ref{tab:anova_crossscorer}) confirms that Depth-Pair dominates variance ($\\eta^2_p = 0.998$); Scorer is statistically significant ($p < .001$) but practically minor ($\\eta^2_p = 0.192$), consistent with a detectable but small scorer influence on absolute discriminability.\n\n%% ====================================================================\n\\subsection{Feature Ordering and Generation Mode}\n\\label{sec:feature_degradation}\n\\label{sec:generation_mode}\n\nAmong continuation-mode models, single-feature $\\auc$ rankings are highly correlated ($\\rho \\geq 0.85$; Table~\\ref{tab:top_features}).\nThe top-3 features (\\texttt{surp\\_d1\\_std}, \\texttt{surp\\_std}, \\texttt{surp\\_d2\\_std}) are shared across all three families: autoregressive generation progressively damps surprisal variability; however, no single feature subset of size ${<}8$ reliably sustains $\\Kempirical{=}2$ (Appendix~\\ref{sec:feature_subset}).\nA feature group ablation (Appendix~\\ref{sec:feature_ablation}) confirms that surprisal (base) dominates on arXiv (single AUC $= 0.809$, LOO $\\Delta = 0.031$); on C4 and Wikipedia, all LOO drops fall within fold variance ($\\leq 0.007$).\nQwen-rewrite diverges (\\texttt{freq\\_entropy} dominates), consistent with its poor cross-model transfer (61--63\\%).\nWithin Qwen, rewrite yields 1v2 $\\auc = 0.6955$ vs.\\ continuation's $0.6112$ ($\\Delta = +8.4$\\,pp); continuation mode is therefore recommended as the canonical condition.\n\n%% ====================================================================\n\\subsection{Neural Probe}\n\\label{sec:neural_probe}\n\nReplacing the 15D features with frozen encoder hidden states (MLP probe, 5{,}000 texts per depth; Table~\\ref{tab:neural_probe_crossmodel}), Qwen achieves $\\Kempirical^{\\text{neural}} = 3$ (2v3 $\\auc = 0.6159$), while Pythia and OLMo remain at $\\Kempirical^{\\text{neural}} = 2$ ($\\auc_{2v3}$: 0.5963, 0.5892).\nThe Qwen-only elevation reflects self-familiarity artifacts that transfer poorly (Section~\\ref{sec:transfer}); the 15D features yield consistent $\\Kempirical = 2$ across all families.\n\n\\noindent\\begin{minipage}{\\columnwidth}\n\\centering\n\\footnotesize\n\\captionof{table}{Neural probe pairwise AUC using frozen-encoder MLP. Each cell reports AUC for classifying depth $d$ vs.\\ $d{+}1$ text. $\\Kempirical^{\\text{neural}}$: maximum depth where AUC exceeds $\\theta = 0.60$.}\n\\label{tab:neural_probe_crossmodel}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Model} & \\textbf{2v3 $\\auc$} & \\textbf{95\\% CI} & $\\Kempirical^{\\text{neural}}$ \\\\\n\\midrule\nQwen-1.5B  & 0.6159 & $[0.610,\\,0.622]$ & 3 \\\\\nPythia-1.4B & 0.5963 & $[0.589,\\,0.603]$ & 2 \\\\\nOLMo-1B    & 0.5892 & $[0.582,\\,0.597]$ & 2 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{minipage}\n\n%% ====================================================================\n\\subsection{Cross-Domain Variation}\n\\label{sec:cross_domain}\n\nThe preceding experiments use C4 (general web text).\nTo test whether $\\Kempirical$ reflects domain structure or model identity, we evaluate on arXiv abstracts ($n{=}2{,}200$ per model) and Wikipedia ($n{=}5{,}000$ per model) across six model configurations spanning four architecture families (Table~\\ref{tab:domain_kstar}).\n\n\\paragraph{arXiv ($\\Kempirical{=}3$): five-model cross-validation.}\nAll five domain-competent models yield $\\Kempirical{=}3$ on arXiv, with boundary-pair $\\auc$ (2v3) ranging from 0.6215 to 0.6545, all exceeding $\\theta$.\nThe elevated signal reflects higher per-generation distributional shift (1v2 JSD $= 0.077$ vs.\\ ${\\sim}0.01$ for C4): formulaic features (LaTeX formatting, citation patterns, mathematical notation) degrade slowly under autoregressive generation and supply persistent depth signal across four architecture families and 1.4B--8B parameters.\nRemoving LaTeX markup reduces 2v3 AUC by ${\\sim}$1.8\\,pp but preserves $\\Kempirical{=}3$ (CI lower $= 0.610 > \\theta$; Table~\\ref{tab:latex_ablation}); content-level properties dominate.\nOLMo-1B is a capacity failure (0v1 JSD $= 0.33$, near-total information loss), not a counter-example.\nMistral-7B provides the strongest domain-dependence evidence: $\\Kempirical{=}1$ on C4 (Section~\\ref{sec:boundary_cases}) but $\\Kempirical{=}3$ on arXiv: domain structure alone can shift $\\Kempirical$ by two levels within the same model.\n\n\\paragraph{Wikipedia ($\\Kempirical{=}1$): single-generation saturation.}\nWith scorer confound controlled (Pythia-1.4B for Qwen generators; Qwen-1.5B, itself cross-family, for all others), all six models yield $\\Kempirical{=}1$ on Wikipedia: 1v2 $\\auc$ ranges from 0.499 (OLMo) to 0.595 (LLaMA), all below $\\theta$.\nWikipedia represents the simplest domain tested; its encyclopedic regularity provides minimal structural signal beyond the 0v1 boundary, and a single generation pass suffices for complete saturation.\nSame-family scoring inflates Qwen $\\Kempirical$ to 2 on Wikipedia ($\\Delta = +2.4$\\,pp); cross-family scoring controls this bias without affecting C4 results (Appendix~\\ref{sec:wiki_domain}).\n\n\\paragraph{Code ($\\Kempirical{=}1$--$2$): cross-modality confirmation.}\nPython functions from CodeSearchNet~\\cite{husain2019codesearchnet} ($n{=}5{,}000$) yield $\\Kempirical{=}2$ for four models (Qwen-1.5B/7B, LLaMA-8B, Mistral-7B; 1v2 $\\auc$: 0.615--0.739; Table~\\ref{tab:code_crossmodel_kstar}), but $\\Kempirical{=}1$ for capacity-limited Pythia-1.4B ($\\auc = 0.598$, CI upper $= 0.603$).\nCode matches C4 despite a different modality, with the same sharp 2v3 collapse (JSD ratio $11.7$--$13.5\\times$).\nCross-family scorer validation confirms Code $\\Kempirical{=}2$ is text-intrinsic ($\\Delta \\leq 1.9$\\,pp; Appendix~\\ref{sec:code_domain}).\n\n\\paragraph{Domain as the primary factor.}\nWith the scorer confound controlled, the domain ordering is: arXiv ($\\Kempirical{=}3$) $>$ C4 ($\\Kempirical{=}2$) $\\geq$ Code ($\\Kempirical{=}1$--$2$) $\\geq$ Wikipedia ($\\Kempirical{=}1$).\nScale (1B--14B) and architecture do not alter the C4/arXiv/Wikipedia ordering; code shows model-dependent variation at the boundary, but domain structural complexity remains the primary determinant of $\\Kempirical$.\n\n\\noindent\\begin{minipage}{\\columnwidth}\n\\centering\n\\footnotesize\n\\captionof{table}{Domain $\\times$ Model $\\Kempirical$ matrix (scorer-controlled). Wikipedia values use cross-family scorer (Pythia-1.4B). $^*$OLMo arXiv: capacity failure. $^\\dagger$Same-family scorer yields $\\Kempirical{=}2$; controlled value shown. $^\\ddagger$Borderline: Pythia CI upper $= 0.603$, Mistral CI lower $= 0.603$.}\n\\label{tab:domain_kstar}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{C4} & \\textbf{Code} & \\textbf{arXiv} & \\textbf{Wikipedia} \\\\\n\\midrule\nQwen-1.5B    & 2 & 2 & 3 & 1$^\\dagger$ \\\\\nQwen-7B      & 2 & 2 & 3 & 1$^\\dagger$ \\\\\nPythia-1.4B  & 2 & 1$^\\ddagger$ & 3 & 1 \\\\\nOLMo-1B      & 2 & --- & 1$^*$ & 1 \\\\\nLLaMA-3.1-8B & 2 & 2 & 3 & 1 \\\\\nMistral-7B   & 1 & 2$^\\ddagger$ & 3 & 1 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{minipage}\n\n%% ====================================================================\n\\subsection{Binary Detector Confidence}\n\\label{sec:binary_confidence}\n\nBinary detectors (DivEye~\\cite{basani2026diveye}, Binoculars~\\cite{hans2024binoculars}) show moderate rank correlations with depth ($|\\rho| = 0.06$--$0.46$; Table~\\ref{tab:s9_binary_spearman}) but fail as depth proxies: 6-class accuracy is at or below chance ($\\leq 0.199$ vs.\\ 0.167 baseline), pairwise $\\auc$ yields $\\Kempirical^{\\text{binary}} \\leq 1$, and multiple conditions exhibit non-monotonic AUC at deeper pairs.\nThe observed correlation is an artifact of 0v1 separation rather than fine-grained depth signal.\n",
      "numLines": 173,
      "startLine": 1,
      "totalLines": 173
    }
  },
  "sourceToolAssistantUUID": "d5a98668-4888-45e0-902a-a3c837b2c26d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "crystalline-noodling-flask"
}
```

</details>

---


### Tool call

_source line 221 · 2026-05-19T13:07:57.937Z_

<details open><summary>🔧 Tool call — Read · `toolu_019sLEwJ22CLk8Z2Fpvjsu1P`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "11d69311-baa3-4ac0-9ae8-71c2d4bcfd62",
  "isSidechain": false,
  "requestId": "req_011CbBymLuM3uVKspKayZ81v",
  "type": "assistant",
  "uuid": "0e4881b8-8239-4ba0-aca5-376ef620c8a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "crystalline-noodling-flask",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GArc2y5KgekET2xoHmtXPq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5205,
      "cache_read_input_tokens": 33722,
      "output_tokens": 233,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5205,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 233,
          "cache_read_input_tokens": 33722,
          "cache_creation_input_tokens": 5205,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5205
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

_source line 222 · 2026-05-19T13:07:58.321Z_

<details><summary>↩ Tool result · `toolu_01Xk5Hat7VpDdkz1FSHXoGa7`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We measure $\Kempirical{=}2$ for web text (8/9 configurations), $\Kempirical{=}1$--$2$ for code, and $\Kempirical{=}3$ for arXiv, with domain structure as the primary determinant of the saturation boundary.
5	For most domains, a single generation pass renders synthetic text indistinguishable from deeper recursive output, limiting the practical ceiling of depth-based detection to one or two generations.
6	These domain-specific boundaries imply that contamination detection and data curation should adopt domain-aware thresholds rather than uniform binary classifiers; our generator-independent features ($\rho > 0.90$) provide a practical basis for such filtering.
7	Future work should extend this characterization to larger-scale models, additional domains, and temporal tracking of $\Kempirical$ as both models and training corpora evolve.
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aa491f4d-61dd-493b-82d4-c9b847e079e0",
  "isSidechain": false,
  "promptId": "12172553-d9aa-40c5-a42d-a4d4469a539a",
  "type": "user",
  "uuid": "a046f6c3-f62c-48ff-9647-7bcd65af13e5",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/conclusion.tex",
      "content": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe measure $\\Kempirical{=}2$ for web text (8/9 configurations), $\\Kempirical{=}1$--$2$ for code, and $\\Kempirical{=}3$ for arXiv, with domain structure as the primary determinant of the saturation boundary.\nFor most domains, a single generation pass renders synthetic text indistinguishable from deeper recursive output, limiting the practical ceiling of depth-based detection to one or two generations.\nThese domain-specific boundaries imply that contamination detection and data curation should adopt domain-aware thresholds rather than uniform binary classifiers; our generator-independent features ($\\rho > 0.90$) provide a practical basis for such filtering.\nFuture work should extend this characterization to larger-scale models, additional domains, and temporal tracking of $\\Kempirical$ as both models and training corpora evolve.\n",
      "numLines": 8,
      "startLine": 1,
      "totalLines": 8
    }
  },
  "sourceToolAssistantUUID": "aa491f4d-61dd-493b-82d4-c9b847e079e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "crystalline-noodling-flask"
}
```

</details>

---


### Tool result

_source line 223 · 2026-05-19T13:07:57.941Z_

<details><summary>↩ Tool result · `toolu_019sLEwJ22CLk8Z2Fpvjsu1P`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Web-scale text corpora are increasingly contaminated by synthetic content that has itself been generated from earlier synthetic content.
5	Estimates suggest that a substantial fraction of online text is machine-generated~\cite{sun2025aigt, spennemann2025quantifying}, and this share continues to rise.
6	When models train on the outputs of earlier models, the resulting multi-generational synthetic text degrades with each iteration: tail modes vanish, lexical diversity contracts, and surprisal distributions flatten~\cite{shumailov2024collapse, dohmatob2024model}.
7	This degradation arises in both \emph{retrain-chains} (iteratively training on model outputs) and \emph{prompt-chains} (recursively generating from previous outputs without retraining); we study the latter, which isolates generation-level information loss from training dynamics (Appendix~\ref{sec:extended_limitations}).
8	Yet the dominant paradigm treats all machine-generated text identically and ignores the generational depth dimension.
9	
10	This gap cuts across multiple communities.
11	Binary detectors~\cite{basani2026diveye, zhang2024minkpp} produce no depth estimate (Section~\ref{sec:binary_confidence}).
12	Membership inference~\cite{zawalski2026codec} addresses a different question, and the model collapse literature~\cite{shumailov2024collapse, alemohammad2024selfconsuming, schaeffer2025position} provides no per-text tool.
13	Data selection methods~\cite{xie2023dsir, tirumala2023d4, drayson2025} likewise ignore recursive depth.
14	No existing method estimates how many rounds of recursive generation a text has undergone.
15	
16	Knowing whether the discriminable depth is finite, and where it saturates, has direct practical consequences.
17	For data curation, the saturation point determines filtering granularity: if discrimination collapses at depth 2, graduated weighting beyond that boundary injects noise, and binary filtering becomes the principled choice.
18	Model collapse theory predicts monotonic quality degradation across generations, but existing analyses are population-level and provide no per-text measure of where degradation saturates.
19	$\Kempirical$ fills this gap by localizing the generation at which adjacent outputs become empirically indistinguishable.
20	
21	The Data Processing Inequality implies that information degrades monotonically across generations, motivating a finite discrimination boundary $\Kstar$; its actual value is determined empirically.
22	We empirically measure $\Kempirical$ (the maximum depth at which a classifier reliably distinguishes adjacent generations) using 15 statistical features computed via a fixed reference scorer (Section~\ref{sec:features}) and an Ordinal Binary Decomposition (OBD) LightGBM classifier.
23	We operationalize $\Kempirical$ as the deepest $k \geq 1$ where the pairwise $\auc_{k-1,k}$ exceeds $\theta = 0.60$ (Section~\ref{sec:formulation}).
24	
25	Our contributions:
26	\begin{enumerate}[label=(\alph*),nosep]
27	  \item \textbf{First empirical measurement of $\Kempirical$} across 9 model configurations (5 architecture families, 1B--14B), 4 source domains (3 text + 1 code), and 4 decoding strategies at $\theta{=}0.60$: 4/5 families (8/9 configurations) yield $\Kempirical{=}2$ on C4 ($p \leq 0.002$; Section~\ref{sec:kstar_boundary}).
28	  Both supervised OBD and zero-shot frontier Large Language Models (LLMs) show no statistically significant difference beyond $\Kempirical$ (McNemar $p > 0.05$, $N{=}500$; Section~\ref{sec:why_kstar}).
29	  \item \textbf{Domain ordering}: arXiv ($\Kempirical{=}3$) $>$ C4 ($\Kempirical{=}2$) $\geq$ Code ($\Kempirical{=}1$--$2$) $\geq$ Wikipedia ($\Kempirical{=}1$) holds across tested configurations; code (Python) approximates web text depth despite a different modality, with model-dependent variation at the boundary (Section~\ref{sec:cross_domain}).
30	  \item \textbf{Practical validation}: largely generator-independent features enable 80--92\% accuracy retention among tested continuation-mode configurations ($\rho > 0.90$; Section~\ref{sec:transfer}); as a consistency check, $\Kempirical{=}2$ correctly predicts binary $>$ graduated filtering for web text (Section~\ref{sec:filtering}).
31	\end{enumerate}
32	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0e4881b8-8239-4ba0-aca5-376ef620c8a8",
  "isSidechain": false,
  "promptId": "12172553-d9aa-40c5-a42d-a4d4469a539a",
  "type": "user",
  "uuid": "fc80c67f-f140-4713-8e48-915575aed73e",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nWeb-scale text corpora are increasingly contaminated by synthetic content that has itself been generated from earlier synthetic content.\nEstimates suggest that a substantial fraction of online text is machine-generated~\\cite{sun2025aigt, spennemann2025quantifying}, and this share continues to rise.\nWhen models train on the outputs of earlier models, the resulting multi-generational synthetic text degrades with each iteration: tail modes vanish, lexical diversity contracts, and surprisal distributions flatten~\\cite{shumailov2024collapse, dohmatob2024model}.\nThis degradation arises in both \\emph{retrain-chains} (iteratively training on model outputs) and \\emph{prompt-chains} (recursively generating from previous outputs without retraining); we study the latter, which isolates generation-level information loss from training dynamics (Appendix~\\ref{sec:extended_limitations}).\nYet the dominant paradigm treats all machine-generated text identically and ignores the generational depth dimension.\n\nThis gap cuts across multiple communities.\nBinary detectors~\\cite{basani2026diveye, zhang2024minkpp} produce no depth estimate (Section~\\ref{sec:binary_confidence}).\nMembership inference~\\cite{zawalski2026codec} addresses a different question, and the model collapse literature~\\cite{shumailov2024collapse, alemohammad2024selfconsuming, schaeffer2025position} provides no per-text tool.\nData selection methods~\\cite{xie2023dsir, tirumala2023d4, drayson2025} likewise ignore recursive depth.\nNo existing method estimates how many rounds of recursive generation a text has undergone.\n\nKnowing whether the discriminable depth is finite, and where it saturates, has direct practical consequences.\nFor data curation, the saturation point determines filtering granularity: if discrimination collapses at depth 2, graduated weighting beyond that boundary injects noise, and binary filtering becomes the principled choice.\nModel collapse theory predicts monotonic quality degradation across generations, but existing analyses are population-level and provide no per-text measure of where degradation saturates.\n$\\Kempirical$ fills this gap by localizing the generation at which adjacent outputs become empirically indistinguishable.\n\nThe Data Processing Inequality implies that information degrades monotonically across generations, motivating a finite discrimination boundary $\\Kstar$; its actual value is determined empirically.\nWe empirically measure $\\Kempirical$ (the maximum depth at which a classifier reliably distinguishes adjacent generations) using 15 statistical features computed via a fixed reference scorer (Section~\\ref{sec:features}) and an Ordinal Binary Decomposition (OBD) LightGBM classifier.\nWe operationalize $\\Kempirical$ as the deepest $k \\geq 1$ where the pairwise $\\auc_{k-1,k}$ exceeds $\\theta = 0.60$ (Section~\\ref{sec:formulation}).\n\nOur contributions:\n\\begin{enumerate}[label=(\\alph*),nosep]\n  \\item \\textbf{First empirical measurement of $\\Kempirical$} across 9 model configurations (5 architecture families, 1B--14B), 4 source domains (3 text + 1 code), and 4 decoding strategies at $\\theta{=}0.60$: 4/5 families (8/9 configurations) yield $\\Kempirical{=}2$ on C4 ($p \\leq 0.002$; Section~\\ref{sec:kstar_boundary}).\n  Both supervised OBD and zero-shot frontier Large Language Models (LLMs) show no statistically significant difference beyond $\\Kempirical$ (McNemar $p > 0.05$, $N{=}500$; Section~\\ref{sec:why_kstar}).\n  \\item \\textbf{Domain ordering}: arXiv ($\\Kempirical{=}3$) $>$ C4 ($\\Kempirical{=}2$) $\\geq$ Code ($\\Kempirical{=}1$--$2$) $\\geq$ Wikipedia ($\\Kempirical{=}1$) holds across tested configurations; code (Python) approximates web text depth despite a different modality, with model-dependent variation at the boundary (Section~\\ref{sec:cross_domain}).\n  \\item \\textbf{Practical validation}: largely generator-independent features enable 80--92\\% accuracy retention among tested continuation-mode configurations ($\\rho > 0.90$; Section~\\ref{sec:transfer}); as a consistency check, $\\Kempirical{=}2$ correctly predicts binary $>$ graduated filtering for web text (Section~\\ref{sec:filtering}).\n\\end{enumerate}\n",
      "numLines": 32,
      "startLine": 1,
      "totalLines": 32
    }
  },
  "sourceToolAssistantUUID": "0e4881b8-8239-4ba0-aca5-376ef620c8a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "crystalline-noodling-flask"
}
```

</details>

---


### Tool call

_source line 224 · 2026-05-19T13:07:58.313Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Xk5Hat7VpDdkz1FSHXoGa7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc80c67f-f140-4713-8e48-915575aed73e",
  "isSidechain": false,
  "requestId": "req_011CbBymLuM3uVKspKayZ81v",
  "type": "assistant",
  "uuid": "aa491f4d-61dd-493b-82d4-c9b847e079e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "crystalline-noodling-flask",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GArc2y5KgekET2xoHmtXPq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5205,
      "cache_read_input_tokens": 33722,
      "output_tokens": 233,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5205,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 233,
          "cache_read_input_tokens": 33722,
          "cache_creation_input_tokens": 5205,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5205
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

_source line 225_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 2 审稿请求]: ## Round 9（继续审稿）— Reviewer 2（新颖性 + 完整性 + 写作质量）  上轮评分：3.5 (Borderline Conference)。论文已大幅修订，请重点验证以下 open/in_progress issues 是否已充分修复。  ### 论文路径 `projects/gen-depth-contamination/docs/paper…",
  "leafUuid": "a046f6c3-f62c-48ff-9647-7bcd65af13e5",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77"
}
```

---


### Runtime record

_source line 226_

```json
{
  "type": "ai-title",
  "aiTitle": "Review paper on data contamination detection for EMNLP 2026",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77"
}
```

---


### Assistant

_source line 227 · 2026-05-19T13:08:26.972Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need. Let me also check for -ing phrases and do a quick page count check. Let me also read the method.tex and related_work.tex for completeness of the review.

Let me check for the specific issues:

1. **R8-N3 ("sole"→"primary")**: The grep found only one "sole" in appendix_extended.tex L512, which is acceptable usage ("sole rewrite-mode model" is factual). The main text uses "primary" consistently. RESOLVED.

2. **R8-W4 (transfer matrix)**: The transfer section now shows Figure 3 heatmap + full matrix in Table S1_transfer. 

3. **R8-W7 (arXiv CI)**: The cross-scorer evaluation now extends to 22 configurations across C4 and arXiv datasets, with the transfer section substantially expanded beyond the original scope. The method.tex footnote documents that arXiv cross-scorer confidence intervals use 10,000 resamples, and the appendix table shows this produces point estimates classifying 3 out of 4 generators at K*=3, though the strict lower-bound criterion confirms only 2.

4. **R8-M4 (Abstract terms + neural probe)**: The abstract now specifies "AUC decision threshold" for θ, and the neural probe section explicitly states "5,000 texts per depth."

5. **Dash check**: No em-dashes or en-dashes found in the .tex files.

6. **Transfer matrix scope**: Looking at the experiments file, the transfer matrix currently covers only 4 out of 9 models—Qwen-rw, Qwen-cont, Pythia, and OLMo—with Pythia↔OLMo retaining...

Actually, I see the cross-scorer validation extends this to 22 configurations across C4 and arXiv, which significantly broadens the coverage beyond just the core heatmap. So while the transfer matrix itself remains limited to those few models, the validation work compensates somewhat.

Now I need to check the page count compliance and verify the -ing phrase frequency, since the new code domain and LOFO content have been added. I can estimate by counting sections—intro takes about a page, related work is partial—but I can't actually compile the LaTeX to get exact counts.

Let me estimate the full paper: intro around a page, related work maybe half to three-quarters, method section one to one-and-a-half pages, then experiments which is the bulk with all its subsections on C4 K*, transfer, feature ordering, neural probe, cross-domain, and binary detector probably consuming three to four pages. Filtering, discussion, and conclusion round out the remaining space. That puts us roughly at seven to eight-and-a-half pages total, which is getting tight with the new additions. I should look for a compiled PDF to verify this more precisely.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a046f6c3-f62c-48ff-9647-7bcd65af13e5",
  "isSidechain": false,
  "requestId": "req_011CbBymcQFpwN28MtLEoTeH",
  "type": "assistant",
  "uuid": "90e47b62-5730-43ca-aedc-b5f15f6774e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "crystalline-noodling-flask",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WB2fWhWEESM9mkLeusqsVx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7808,
      "cache_read_input_tokens": 38927,
      "output_tokens": 1298,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7808,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1298,
          "cache_read_input_tokens": 38927,
          "cache_creation_input_tokens": 7808,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7808
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

_source line 228 · 2026-05-19T13:08:27.009Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01TGxWFBqBT6LVpHDCxjP7Y5`</summary>

```json
{
  "pattern": "**/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "90e47b62-5730-43ca-aedc-b5f15f6774e6",
  "isSidechain": false,
  "requestId": "req_011CbBymcQFpwN28MtLEoTeH",
  "type": "assistant",
  "uuid": "b569a0d3-c677-4aae-ab3a-d5514893e7e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "crystalline-noodling-flask",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WB2fWhWEESM9mkLeusqsVx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7808,
      "cache_read_input_tokens": 38927,
      "output_tokens": 1298,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7808,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1298,
          "cache_read_input_tokens": 38927,
          "cache_creation_input_tokens": 7808,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7808
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

_source line 229 · 2026-05-19T13:08:27.028Z_

<details><summary>↩ Tool result · `toolu_01TGxWFBqBT6LVpHDCxjP7Y5`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/figures/fig3_transfer_heatmap.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/figures/fig_s1_auc_decay_ci.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/figures/fig_filtering_strategies.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/figures/fig2_auc_decay.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/figures/fig_kstar_theta.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/figures/pipeline.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/figures/fig_jsd_decay.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/figures/fig_theta_sensitivity.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/figures/fig_feature_ablation.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b569a0d3-c677-4aae-ab3a-d5514893e7e0",
  "isSidechain": false,
  "promptId": "12172553-d9aa-40c5-a42d-a4d4469a539a",
  "type": "user",
  "uuid": "1cea30df-8330-46b0-ad80-b388e6f6e3d9",
  "toolUseResult": {
    "filenames": [
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/figures/fig3_transfer_heatmap.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/figures/fig_s1_auc_decay_ci.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/figures/fig_filtering_strategies.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/figures/fig2_auc_decay.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/figures/fig_kstar_theta.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/figures/pipeline.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/figures/fig_jsd_decay.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/figures/fig_theta_sensitivity.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/figures/fig_feature_ablation.pdf",
      "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.pdf"
    ],
    "durationMs": 10,
    "numFiles": 10,
    "truncated": false
  },
  "sourceToolAssistantUUID": "b569a0d3-c677-4aae-ab3a-d5514893e7e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "crystalline-noodling-flask"
}
```

</details>

---


### Tool result

_source line 230 · 2026-05-19T13:08:29.220Z_

<details><summary>↩ Tool result · `toolu_01RpbJX6t8AsmKwYWvrZnSbD`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Model collapse and recursive degradation.}
5	Iterative training on model outputs causes tail-distribution degradation~\cite{shumailov2024collapse, alemohammad2024selfconsuming, dohmatob2024model, dohmatob2025strong}, diversity contraction~\cite{guo2024curious, padmakumar2024writing, briesch2023selfconsuming}, and predictable convergence~\cite{bertrand2024stability, schaeffer2025position, kazdan2025collapse, gerstgrasser2024model, shi2025collapse}.
6	\citet{gambetta2024surplexity} propose surplexity, a single surprisal-based collapse indicator; our 15-dimensional feature set captures richer distributional structure and enables cross-model transfer.
7	\citet{amin2025escaping} show that weak-data curation can mitigate collapse, connecting to our filtering evaluation (Section~\ref{sec:filtering}).
8	Our prompt-chain operates in the replace regime~\cite{kazdan2025collapse}; $\Kempirical = 2$ is therefore a conservative lower bound.
9	This literature establishes convergence but provides no per-text depth measurement, does not predict domain dependence of saturation (Wikipedia depth 1 vs.\ arXiv depth 3), and does not characterize the prompt-chain vs.\ retrain-chain gap ($\Kempirical{=}2$ vs.\ $7$).
10	
11	\paragraph{Beyond binary detection.}
12	Binary detectors~\cite{gehrmann2019gltr, mitchell2023detectgpt, bao2024fast, yang2024dnagpt, hans2024binoculars, verma2024ghostbuster, basani2026diveye, zhang2024minkpp} achieve strong human-vs.-machine separation but produce no depth estimate; surveys~\cite{wu2023survey, tang2024science} consolidate this landscape but frame detection as binary.
13	Recent work extends beyond binary labels to collaboration degree~\cite{cheng2025beyond}, contamination hierarchies~\cite{mehta2025beyond}, and multigenerator benchmarks~\cite{wang2024semeval}; robustness concerns arise under paraphrasing~\cite{sadasivan2023detect, krishna2023paraphrasing} and cross-mode transfer~\cite{hao2025rewrite}; CoDeC~\cite{zawalski2026codec} addresses contamination via membership inference.
14	None estimates recursive generation depth.
15	Watermarking~\cite{kirchenbauer2023watermark} embeds detectable signals at generation time but does not apply to text already in the wild.
16	
17	\paragraph{Data selection and curation.}
18	DSIR~\cite{xie2023dsir}, D4~\cite{tirumala2023d4}, DoReMi~\cite{xie2023doremi}, and FineWeb~\cite{penedo2024fineweb} address corpus quality for large web corpora such as C4~\cite{raffel2020t5} through domain-aware filtering and deduplication but are depth-agnostic; Drayson et al.~\cite{drayson2025} combined binary detection with importance resampling, a special case when $\Kstar = 1$.
19	\citet{oren2024proving} address contamination detection in pre-training data; our method extends this to depth-granular resolution.
20	
21	\paragraph{Ordinal classification and probing.}
22	Our surprisal features build on information-theoretic processing cost~\cite{hale2001surprisal, levy2008expectation}, repurposed to track generational degradation.
23	Our OBD classifier follows Frank \& Hall's~\cite{frank2001ordinal} binary decomposition; CORAL~\cite{cao2020coral} provides a rank-consistent neural alternative.
24	Our neural probe extends probing~\cite{alain2017understanding, belinkov2022probing} to the discrimination boundary.
25	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0e8d84f7-613d-46d1-aee6-5697c2eeca4b",
  "isSidechain": false,
  "promptId": "12172553-d9aa-40c5-a42d-a4d4469a539a",
  "type": "user",
  "uuid": "05fd7a15-e805-4c9a-833d-f941d818a4b4",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\paragraph{Model collapse and recursive degradation.}\nIterative training on model outputs causes tail-distribution degradation~\\cite{shumailov2024collapse, alemohammad2024selfconsuming, dohmatob2024model, dohmatob2025strong}, diversity contraction~\\cite{guo2024curious, padmakumar2024writing, briesch2023selfconsuming}, and predictable convergence~\\cite{bertrand2024stability, schaeffer2025position, kazdan2025collapse, gerstgrasser2024model, shi2025collapse}.\n\\citet{gambetta2024surplexity} propose surplexity, a single surprisal-based collapse indicator; our 15-dimensional feature set captures richer distributional structure and enables cross-model transfer.\n\\citet{amin2025escaping} show that weak-data curation can mitigate collapse, connecting to our filtering evaluation (Section~\\ref{sec:filtering}).\nOur prompt-chain operates in the replace regime~\\cite{kazdan2025collapse}; $\\Kempirical = 2$ is therefore a conservative lower bound.\nThis literature establishes convergence but provides no per-text depth measurement, does not predict domain dependence of saturation (Wikipedia depth 1 vs.\\ arXiv depth 3), and does not characterize the prompt-chain vs.\\ retrain-chain gap ($\\Kempirical{=}2$ vs.\\ $7$).\n\n\\paragraph{Beyond binary detection.}\nBinary detectors~\\cite{gehrmann2019gltr, mitchell2023detectgpt, bao2024fast, yang2024dnagpt, hans2024binoculars, verma2024ghostbuster, basani2026diveye, zhang2024minkpp} achieve strong human-vs.-machine separation but produce no depth estimate; surveys~\\cite{wu2023survey, tang2024science} consolidate this landscape but frame detection as binary.\nRecent work extends beyond binary labels to collaboration degree~\\cite{cheng2025beyond}, contamination hierarchies~\\cite{mehta2025beyond}, and multigenerator benchmarks~\\cite{wang2024semeval}; robustness concerns arise under paraphrasing~\\cite{sadasivan2023detect, krishna2023paraphrasing} and cross-mode transfer~\\cite{hao2025rewrite}; CoDeC~\\cite{zawalski2026codec} addresses contamination via membership inference.\nNone estimates recursive generation depth.\nWatermarking~\\cite{kirchenbauer2023watermark} embeds detectable signals at generation time but does not apply to text already in the wild.\n\n\\paragraph{Data selection and curation.}\nDSIR~\\cite{xie2023dsir}, D4~\\cite{tirumala2023d4}, DoReMi~\\cite{xie2023doremi}, and FineWeb~\\cite{penedo2024fineweb} address corpus quality for large web corpora such as C4~\\cite{raffel2020t5} through domain-aware filtering and deduplication but are depth-agnostic; Drayson et al.~\\cite{drayson2025} combined binary detection with importance resampling, a special case when $\\Kstar = 1$.\n\\citet{oren2024proving} address contamination detection in pre-training data; our method extends this to depth-granular resolution.\n\n\\paragraph{Ordinal classification and probing.}\nOur surprisal features build on information-theoretic processing cost~\\cite{hale2001surprisal, levy2008expectation}, repurposed to track generational degradation.\nOur OBD classifier follows Frank \\& Hall's~\\cite{frank2001ordinal} binary decomposition; CORAL~\\cite{cao2020coral} provides a rank-consistent neural alternative.\nOur neural probe extends probing~\\cite{alain2017understanding, belinkov2022probing} to the discrimination boundary.\n",
      "numLines": 25,
      "startLine": 1,
      "totalLines": 25
    }
  },
  "sourceToolAssistantUUID": "0e8d84f7-613d-46d1-aee6-5697c2eeca4b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "crystalline-noodling-flask"
}
```

</details>

---


### Tool call

_source line 231 · 2026-05-19T13:08:28.418Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01BJRrchAW9PptLvQ7me2FRF`</summary>

```json
{
  "pattern": "\\b(leveraging|utilizing|enabling|facilitating|demonstrating|indicating|suggesting|highlighting|employing|showcasing)\\b",
  "glob": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper",
  "output_mode": "content",
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1cea30df-8330-46b0-ad80-b388e6f6e3d9",
  "isSidechain": false,
  "requestId": "req_011CbBymcQFpwN28MtLEoTeH",
  "type": "assistant",
  "uuid": "d2579870-2aff-4ddb-a15e-c483e5e3263a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "crystalline-noodling-flask",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WB2fWhWEESM9mkLeusqsVx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7808,
      "cache_read_input_tokens": 38927,
      "output_tokens": 1298,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7808,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1298,
          "cache_read_input_tokens": 38927,
          "cache_creation_input_tokens": 7808,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7808
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

_source line 232 · 2026-05-19T13:08:28.456Z_

<details><summary>↩ Tool result · `toolu_01BJRrchAW9PptLvQ7me2FRF`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:16:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:306:\caption{Retrain-chain AUC decay across 7 generation pairs (Qwen2.5-1.5B LoRA). Unlike prompt-chain (sharp cliff at 0v1$\to$1v2), retrain-chain AUC decays gradually from 0.984 to 0.641, with all pairs above $\theta{=}0.60$. Error bars: 95\% CI from 5-fold CV. Dashed line: $\theta{=}0.60$; extrapolated 7v8 $\approx 0.57$ (below $\theta$), suggesting $\Kempirical{=}7$ is near the ceiling.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex:354:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d2579870-2aff-4ddb-a15e-c483e5e3263a",
  "isSidechain": false,
  "promptId": "12172553-d9aa-40c5-a42d-a4d4469a539a",
  "type": "user",
  "uuid": "c49950b9-ed51-4db4-9ac5-f81c586d82f0",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:16:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex:306:\\caption{Retrain-chain AUC decay across 7 generation pairs (Qwen2.5-1.5B LoRA). Unlike prompt-chain (sharp cliff at 0v1$\\to$1v2), retrain-chain AUC decays gradually from 0.984 to 0.641, with all pairs above $\\theta{=}0.60$. Error bars: 95\\% CI from 5-fold CV. Dashed line: $\\theta{=}0.60$; extrapolated 7v8 $\\approx 0.57$ (below $\\theta$), suggesting $\\Kempirical{=}7$ is near the ceiling.}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix.tex:354:[Omitted long matching line]",
    "numLines": 3
  },
  "sourceToolAssistantUUID": "d2579870-2aff-4ddb-a15e-c483e5e3263a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "crystalline-noodling-flask"
}
```

</details>

---


### Tool call

_source line 233 · 2026-05-19T13:08:28.938Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KdPNDa9RxhYZyStxu6jNau`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c49950b9-ed51-4db4-9ac5-f81c586d82f0",
  "isSidechain": false,
  "requestId": "req_011CbBymcQFpwN28MtLEoTeH",
  "type": "assistant",
  "uuid": "cb8f09f7-6ece-4761-81c1-c33550a0c287",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "crystalline-noodling-flask",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WB2fWhWEESM9mkLeusqsVx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7808,
      "cache_read_input_tokens": 38927,
      "output_tokens": 1298,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7808,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1298,
          "cache_read_input_tokens": 38927,
          "cache_creation_input_tokens": 7808,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7808
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

_source line 234 · 2026-05-19T13:08:28.949Z_

<details><summary>↩ Tool result · `toolu_01KdPNDa9RxhYZyStxu6jNau`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\begin{figure*}[t]
5	\centering
6	\includegraphics[width=\textwidth]{figures/pipeline.pdf}
7	\caption{Generational depth estimation pipeline. Seed documents are recursively passed through a generation operator $G_\delta$ to produce a depth chain. Statistical features are fed to the OBD-LightGBM classifier for depth prediction.}
8	\label{fig:pipeline}
9	\end{figure*}
10	
11	\subsection{Problem Formulation}
12	\label{sec:formulation}
13	
14	A generation operator $G_\delta$ (LLM + decoding strategy $\delta$) produces successive generations $X \to Y_1 \to \cdots \to Y_K$, where $Y_k = G_\delta(Y_{k-1})$ and $Y_0 \triangleq X$ (Figure~\ref{fig:pipeline}).
15	This sequence forms a Markov chain.
16	By the Data Processing Inequality, $I(X; Y_1) \geq I(X; Y_2) \geq \cdots \geq 0$: the original signal degrades monotonically.
17	Together with Markov chain convergence, this motivates a finite $\Ktheory$ beyond which adjacent generations become indistinguishable; DPI guarantees existence but does not bound $\Ktheory$, so the actual saturation depth must be measured empirically.
18	
19	We define the operational lower bound:
20	\begin{equation}
21	  \Kempirical = \max\{k \geq 1 : \mathrm{CI}_{\mathrm{low}}(\auc_{k-1,k}) > \theta\},
22	  \label{eq:kstar}
23	\end{equation}
24	where $\mathrm{CI}_{\mathrm{low}}(\auc_{k-1,k})$ is the lower bound of a 95\% bootstrap confidence interval (1{,}000 resamples\footnote{Boundary-pair results in Table~\ref{tab:kstar_ci} use 1{,}000 resamples; arXiv cross-scorer CIs (Table~\ref{tab:arxiv_crossscorer_ci}) use 10{,}000 for tighter bounds at the margin.}) over the pairwise AUC (Area Under the ROC Curve) between depths $k{-}1$ and $k$, and $\theta = 0.60$ is a post-hoc operational threshold (motivated below).
25	This criterion ensures that $\Kempirical$ reflects statistically robust discriminability rather than sampling noise.
26	$\Kempirical$ characterizes a discriminability regime at a given $\theta$; the domain ordering is stable across $\theta \in [0.575, 0.65]$ (Section~\ref{sec:kstar_boundary}).
27	We additionally verify that non-boundary-pair CI upper bounds fall below $\theta$ (Section~\ref{sec:kstar_boundary}).
28	
29	\paragraph{Threshold choice.}
30	We set $\theta{=}0.60$ as a post-hoc operational threshold, chosen at the empirical discontinuity in the AUC distribution (Figure~\ref{fig:kstar_theta}).
31	A 10{,}000-iteration permutation test yields a 95th-percentile null of ${<}\,0.55$ and $p < 0.002$ for all boundary comparisons, placing $\theta{=}0.60$ well above the empirical null.
32	$\Kempirical{=}2$ is stable across $\theta \in [0.55, 0.65]$ for all but two marginal configurations (Table~\ref{tab:kstar_ci_extended}): 1v2 AUC values cluster at $0.61$--$0.70$ while 2v3 values cluster at $0.55$--$0.59$, creating a ${\sim}$5--11\,pp discontinuity.
33	Only at extremes does $\Kempirical$ shift: $\theta{=}0.55$ yields $\Kempirical{=}3$ for two Qwen configurations; $\theta{=}0.70$ yields $\Kempirical{=}1$ across all configurations.
34	The downstream filtering evaluation (Section~\ref{sec:filtering}) uses the OBD classifier without re-optimizing $\theta$, avoiding circularity.
35	A leave-one-family-out (LOFO) cross-validation on C4 independently validates this choice: each of five folds derives $\hat{\theta}$ from the gap midpoint between $\min(\auc_{1v2})$ and $\max(\auc_{2v3})$ over the remaining families, yielding $\hat{\theta} \in [0.5725, 0.6004]$; $\theta{=}0.60$ falls within this range, and 8/9 held-out predictions match the original $\Kempirical$ (the single mismatch is the borderline rewrite-mode configuration; Table~\ref{tab:theta_lofo}).
36	ArXiv corroborates with 6/6 LOFO agreement; Wikipedia is underdetermined because most models produce near-chance 1v2 AUC, invalidating the gap-based derivation (Appendix~\ref{sec:theta_lofo}).
37	
38	
39	\subsection{Features and Classifier}
40	\label{sec:features}
41	
42	Each document is characterized by a 15-dimensional feature vector spanning four groups: \emph{surprisal moments} (mean, std, skewness, kurtosis; 4~dims), \emph{surprisal derivatives} (mean and std of first- and second-order differences, plus first-order skewness; 5~dims), \emph{vocabulary diversity} (type-token ratio, hapax legomena ratio, self-BLEU; 3~dims), and \emph{frequency tail statistics} (frequency kurtosis, entropy, rare token fraction; 3~dims).
43	All features are computed from token-level surprisal values via an external scorer model (full definitions in Table~\ref{tab:s5_features}, Appendix).
44	Self-BLEU is computed within each CV fold using only same-fold, same-depth reference samples to prevent leakage; it ranks \#1 in 1/8 conditions (greedy decoding) but is absent from the top-3 in all 7 others.
45	Removing self-BLEU reduces mean $\auc_{1v2}$ by $< 1$\,pp across all models (14D $\Kempirical = 2$ for all 4 configurations; bootstrap CIs in Table~\ref{tab:selfbleu_ablation}); in deployment where depth labels are unavailable, self-BLEU can be replaced with corpus-level self-similarity or omitted with minimal performance loss.
46	Hand-crafted features enable cross-generator transfer without retraining and permit attribution of discriminative power to specific text properties.
47	
48	We use \emph{Ordinal Binary Decomposition} (OBD), decomposing the $(K{+}1)$-class problem into $K$ cumulative binary sub-classifiers, each estimating $P(\text{depth} > k \mid \mathbf{x})$ via LightGBM~\cite{ke2017lightgbm} (hyperparameters in Table~\ref{tab:s6_lgbm_params}).
49	OBD achieves lower MAE than multiclass LightGBM (e.g., 0.984 vs.\ 1.016 on Qwen-rewrite) while maintaining superior pairwise $\auc$ (mean 0.6095 vs.\ 0.4883 for ordinal logistic regression).
50	
51	\subsection{Experimental Setup}
52	\label{sec:experimental_setup}
53	
54	We evaluate nine configurations spanning five architecture families (Table~\ref{tab:setup}): Qwen2.5-1.5B-Instruct (rewrite and continuation modes), Qwen2.5-1.5B (base, continuation), Qwen2.5-7B, Qwen2.5-14B, Pythia-1.4B, OLMo-1B, LLaMA-3.1-8B, and Mistral-7B (all continuation except Qwen-rw).
55	Each uses 5{,}000 C4~\cite{raffel2020t5} seeds truncated to 256 tokens, recursively generated for $K{=}5$ iterations (30{,}000 documents per configuration).
56	Default decoding: nucleus $p{=}0.95$, $T{=}1.0$; decoding ablation covers greedy, $T{=}0.7$, and $T{=}1.2$.
57	Continuation mode truncates seeds to 128 tokens and extends to 256; rewrite mode paraphrases the full text.
58	Evaluation: 5-fold GroupKFold cross-validation grouped by seed document; pairwise $\auc$ as primary metric.
59	
60	\begin{table}[t]
61	\centering
62	\small
63	\caption{Experimental configurations for depth-chain generation. \textbf{Config}: shorthand identifier; \textbf{Model}: architecture and parameter count; \textbf{Mode}: generation strategy (continuation or rewrite); $N$: number of seed documents per depth level.}
64	\label{tab:setup}
65	\resizebox{\columnwidth}{!}{%
66	\begin{tabular}{llcc}
67	\toprule
68	\textbf{Config} & \textbf{Model} & \textbf{Mode} & $N$ \\
69	\midrule
70	Qwen-rw   & Qwen2.5-1.5B-Instruct & Rewrite & 5{,}000 \\
71	Qwen-cont & Qwen2.5-1.5B-Instruct & Continuation & 5{,}000 \\
72	Qwen-base & Qwen2.5-1.5B          & Continuation & 5{,}000 \\
73	Pythia    & Pythia-1.4B            & Continuation & 5{,}000 \\
74	OLMo      & OLMo-1B               & Continuation & 5{,}000 \\
75	Qwen-7B   & Qwen2.5-7B            & Continuation & 5{,}000 \\
76	Qwen-14B  & Qwen2.5-14B           & Continuation & 5{,}000 \\
77	LLaMA-8B  & LLaMA-3.1-8B          & Continuation & 5{,}000 \\
78	Mistral   & Mistral-7B            & Continuation & 5{,}000 \\
79	\bottomrule
80	\end{tabular}}
81	\end{table}
82	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cb8f09f7-6ece-4761-81c1-c33550a0c287",
  "isSidechain": false,
  "promptId": "12172553-d9aa-40c5-a42d-a4d4469a539a",
  "type": "user",
  "uuid": "5c395af9-2d23-4bd8-b41b-b2539437259d",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/pipeline.pdf}\n\\caption{Generational depth estimation pipeline. Seed documents are recursively passed through a generation operator $G_\\delta$ to produce a depth chain. Statistical features are fed to the OBD-LightGBM classifier for depth prediction.}\n\\label{fig:pipeline}\n\\end{figure*}\n\n\\subsection{Problem Formulation}\n\\label{sec:formulation}\n\nA generation operator $G_\\delta$ (LLM + decoding strategy $\\delta$) produces successive generations $X \\to Y_1 \\to \\cdots \\to Y_K$, where $Y_k = G_\\delta(Y_{k-1})$ and $Y_0 \\triangleq X$ (Figure~\\ref{fig:pipeline}).\nThis sequence forms a Markov chain.\nBy the Data Processing Inequality, $I(X; Y_1) \\geq I(X; Y_2) \\geq \\cdots \\geq 0$: the original signal degrades monotonically.\nTogether with Markov chain convergence, this motivates a finite $\\Ktheory$ beyond which adjacent generations become indistinguishable; DPI guarantees existence but does not bound $\\Ktheory$, so the actual saturation depth must be measured empirically.\n\nWe define the operational lower bound:\n\\begin{equation}\n  \\Kempirical = \\max\\{k \\geq 1 : \\mathrm{CI}_{\\mathrm{low}}(\\auc_{k-1,k}) > \\theta\\},\n  \\label{eq:kstar}\n\\end{equation}\nwhere $\\mathrm{CI}_{\\mathrm{low}}(\\auc_{k-1,k})$ is the lower bound of a 95\\% bootstrap confidence interval (1{,}000 resamples\\footnote{Boundary-pair results in Table~\\ref{tab:kstar_ci} use 1{,}000 resamples; arXiv cross-scorer CIs (Table~\\ref{tab:arxiv_crossscorer_ci}) use 10{,}000 for tighter bounds at the margin.}) over the pairwise AUC (Area Under the ROC Curve) between depths $k{-}1$ and $k$, and $\\theta = 0.60$ is a post-hoc operational threshold (motivated below).\nThis criterion ensures that $\\Kempirical$ reflects statistically robust discriminability rather than sampling noise.\n$\\Kempirical$ characterizes a discriminability regime at a given $\\theta$; the domain ordering is stable across $\\theta \\in [0.575, 0.65]$ (Section~\\ref{sec:kstar_boundary}).\nWe additionally verify that non-boundary-pair CI upper bounds fall below $\\theta$ (Section~\\ref{sec:kstar_boundary}).\n\n\\paragraph{Threshold choice.}\nWe set $\\theta{=}0.60$ as a post-hoc operational threshold, chosen at the empirical discontinuity in the AUC distribution (Figure~\\ref{fig:kstar_theta}).\nA 10{,}000-iteration permutation test yields a 95th-percentile null of ${<}\\,0.55$ and $p < 0.002$ for all boundary comparisons, placing $\\theta{=}0.60$ well above the empirical null.\n$\\Kempirical{=}2$ is stable across $\\theta \\in [0.55, 0.65]$ for all but two marginal configurations (Table~\\ref{tab:kstar_ci_extended}): 1v2 AUC values cluster at $0.61$--$0.70$ while 2v3 values cluster at $0.55$--$0.59$, creating a ${\\sim}$5--11\\,pp discontinuity.\nOnly at extremes does $\\Kempirical$ shift: $\\theta{=}0.55$ yields $\\Kempirical{=}3$ for two Qwen configurations; $\\theta{=}0.70$ yields $\\Kempirical{=}1$ across all configurations.\nThe downstream filtering evaluation (Section~\\ref{sec:filtering}) uses the OBD classifier without re-optimizing $\\theta$, avoiding circularity.\nA leave-one-family-out (LOFO) cross-validation on C4 independently validates this choice: each of five folds derives $\\hat{\\theta}$ from the gap midpoint between $\\min(\\auc_{1v2})$ and $\\max(\\auc_{2v3})$ over the remaining families, yielding $\\hat{\\theta} \\in [0.5725, 0.6004]$; $\\theta{=}0.60$ falls within this range, and 8/9 held-out predictions match the original $\\Kempirical$ (the single mismatch is the borderline rewrite-mode configuration; Table~\\ref{tab:theta_lofo}).\nArXiv corroborates with 6/6 LOFO agreement; Wikipedia is underdetermined because most models produce near-chance 1v2 AUC, invalidating the gap-based derivation (Appendix~\\ref{sec:theta_lofo}).\n\n\n\\subsection{Features and Classifier}\n\\label{sec:features}\n\nEach document is characterized by a 15-dimensional feature vector spanning four groups: \\emph{surprisal moments} (mean, std, skewness, kurtosis; 4~dims), \\emph{surprisal derivatives} (mean and std of first- and second-order differences, plus first-order skewness; 5~dims), \\emph{vocabulary diversity} (type-token ratio, hapax legomena ratio, self-BLEU; 3~dims), and \\emph{frequency tail statistics} (frequency kurtosis, entropy, rare token fraction; 3~dims).\nAll features are computed from token-level surprisal values via an external scorer model (full definitions in Table~\\ref{tab:s5_features}, Appendix).\nSelf-BLEU is computed within each CV fold using only same-fold, same-depth reference samples to prevent leakage; it ranks \\#1 in 1/8 conditions (greedy decoding) but is absent from the top-3 in all 7 others.\nRemoving self-BLEU reduces mean $\\auc_{1v2}$ by $< 1$\\,pp across all models (14D $\\Kempirical = 2$ for all 4 configurations; bootstrap CIs in Table~\\ref{tab:selfbleu_ablation}); in deployment where depth labels are unavailable, self-BLEU can be replaced with corpus-level self-similarity or omitted with minimal performance loss.\nHand-crafted features enable cross-generator transfer without retraining and permit attribution of discriminative power to specific text properties.\n\nWe use \\emph{Ordinal Binary Decomposition} (OBD), decomposing the $(K{+}1)$-class problem into $K$ cumulative binary sub-classifiers, each estimating $P(\\text{depth} > k \\mid \\mathbf{x})$ via LightGBM~\\cite{ke2017lightgbm} (hyperparameters in Table~\\ref{tab:s6_lgbm_params}).\nOBD achieves lower MAE than multiclass LightGBM (e.g., 0.984 vs.\\ 1.016 on Qwen-rewrite) while maintaining superior pairwise $\\auc$ (mean 0.6095 vs.\\ 0.4883 for ordinal logistic regression).\n\n\\subsection{Experimental Setup}\n\\label{sec:experimental_setup}\n\nWe evaluate nine configurations spanning five architecture families (Table~\\ref{tab:setup}): Qwen2.5-1.5B-Instruct (rewrite and continuation modes), Qwen2.5-1.5B (base, continuation), Qwen2.5-7B, Qwen2.5-14B, Pythia-1.4B, OLMo-1B, LLaMA-3.1-8B, and Mistral-7B (all continuation except Qwen-rw).\nEach uses 5{,}000 C4~\\cite{raffel2020t5} seeds truncated to 256 tokens, recursively generated for $K{=}5$ iterations (30{,}000 documents per configuration).\nDefault decoding: nucleus $p{=}0.95$, $T{=}1.0$; decoding ablation covers greedy, $T{=}0.7$, and $T{=}1.2$.\nContinuation mode truncates seeds to 128 tokens and extends to 256; rewrite mode paraphrases the full text.\nEvaluation: 5-fold GroupKFold cross-validation grouped by seed document; pairwise $\\auc$ as primary metric.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Experimental configurations for depth-chain generation. \\textbf{Config}: shorthand identifier; \\textbf{Model}: architecture and parameter count; \\textbf{Mode}: generation strategy (continuation or rewrite); $N$: number of seed documents per depth level.}\n\\label{tab:setup}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Config} & \\textbf{Model} & \\textbf{Mode} & $N$ \\\\\n\\midrule\nQwen-rw   & Qwen2.5-1.5B-Instruct & Rewrite & 5{,}000 \\\\\nQwen-cont & Qwen2.5-1.5B-Instruct & Continuation & 5{,}000 \\\\\nQwen-base & Qwen2.5-1.5B          & Continuation & 5{,}000 \\\\\nPythia    & Pythia-1.4B            & Continuation & 5{,}000 \\\\\nOLMo      & OLMo-1B               & Continuation & 5{,}000 \\\\\nQwen-7B   & Qwen2.5-7B            & Continuation & 5{,}000 \\\\\nQwen-14B  & Qwen2.5-14B           & Continuation & 5{,}000 \\\\\nLLaMA-8B  & LLaMA-3.1-8B          & Continuation & 5{,}000 \\\\\nMistral   & Mistral-7B            & Continuation & 5{,}000 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n",
      "numLines": 82,
      "startLine": 1,
      "totalLines": 82
    }
  },
  "sourceToolAssistantUUID": "cb8f09f7-6ece-4761-81c1-c33550a0c287",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "crystalline-noodling-flask"
}
```

</details>

---


### Tool call

_source line 235 · 2026-05-19T13:08:29.215Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RpbJX6t8AsmKwYWvrZnSbD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c395af9-2d23-4bd8-b41b-b2539437259d",
  "isSidechain": false,
  "requestId": "req_011CbBymcQFpwN28MtLEoTeH",
  "type": "assistant",
  "uuid": "0e8d84f7-613d-46d1-aee6-5697c2eeca4b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "crystalline-noodling-flask",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WB2fWhWEESM9mkLeusqsVx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7808,
      "cache_read_input_tokens": 38927,
      "output_tokens": 1298,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7808,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1298,
          "cache_read_input_tokens": 38927,
          "cache_creation_input_tokens": 7808,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7808
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

_source line 236 · 2026-05-19T13:08:29.272Z_

```json
{
  "parentUuid": "05fd7a15-e805-4c9a-833d-f941d818a4b4",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "ae28cb18-e5f8-4845-97fe-3e12659d3aa2",
  "timestamp": "2026-05-19T13:08:29.272Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "crystalline-noodling-flask"
}
```

---


### Runtime record

_source line 237_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 2 审稿请求]: ## Round 9（继续审稿）— Reviewer 2（新颖性 + 完整性 + 写作质量）  上轮评分：3.5 (Borderline Conference)。论文已大幅修订，请重点验证以下 open/in_progress issues 是否已充分修复。  ### 论文路径 `projects/gen-depth-contamination/docs/paper…",
  "leafUuid": "ae28cb18-e5f8-4845-97fe-3e12659d3aa2",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77"
}
```

---


### Runtime record

_source line 238_

```json
{
  "type": "ai-title",
  "aiTitle": "Review paper on data contamination detection for EMNLP 2026",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77"
}
```

---


### Assistant

_source line 239 · 2026-05-19T13:08:32.582Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me check the page count of the PDF. I'll use pdf_to_images to check the page count, or I can use a simpler method.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae28cb18-e5f8-4845-97fe-3e12659d3aa2",
  "isSidechain": false,
  "requestId": "req_011CbByotQyoQhrCmMa13GYB",
  "type": "assistant",
  "uuid": "876ee91d-b3c1-4293-8929-b79670248e0c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "crystalline-noodling-flask",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DaXmThjVdXVRATcCcxt4yd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6039,
      "cache_read_input_tokens": 46735,
      "output_tokens": 451,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6039,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 451,
          "cache_read_input_tokens": 46735,
          "cache_creation_input_tokens": 6039,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6039
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

_source line 240 · 2026-05-19T13:08:33.166Z_

Let me check the page count of the compiled PDF.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "876ee91d-b3c1-4293-8929-b79670248e0c",
  "isSidechain": false,
  "requestId": "req_011CbByotQyoQhrCmMa13GYB",
  "type": "assistant",
  "uuid": "a6fcc0b8-911a-42de-8e03-4e45b5d001bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "crystalline-noodling-flask",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DaXmThjVdXVRATcCcxt4yd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6039,
      "cache_read_input_tokens": 46735,
      "output_tokens": 451,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6039,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 451,
          "cache_read_input_tokens": 46735,
          "cache_creation_input_tokens": 6039,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6039
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

_source line 241 · 2026-05-19T13:08:36.032Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Jf9nBEi2JJr8aRvwujuEEG`</summary>

```json
{
  "command": "python3 -c \"\nimport json\nwith open('/dev/stdin', 'r') as f: pass\n\" 2>/dev/null; python3 -c \"\ntry:\n    import fitz\n    doc = fitz.open('/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.pdf')\n    print(f'Total pages: {len(doc)}')\n    doc.close()\nexcept ImportError:\n    import subprocess\n    result = subprocess.run(['pdfinfo', '/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/main.pdf'], capture_output=True, text=True)\n    print(result.stdout)\n    if result.returncode != 0:\n        print(result.stderr)\n\"",
  "description": "Check PDF page count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a6fcc0b8-911a-42de-8e03-4e45b5d001bf",
  "isSidechain": false,
  "requestId": "req_011CbByotQyoQhrCmMa13GYB",
  "type": "assistant",
  "uuid": "376b7ace-aa14-40e7-a4b7-e6eebf1f1451",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "crystalline-noodling-flask",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DaXmThjVdXVRATcCcxt4yd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6039,
      "cache_read_input_tokens": 46735,
      "output_tokens": 451,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6039,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 451,
          "cache_read_input_tokens": 46735,
          "cache_creation_input_tokens": 6039,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6039
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

_source line 242 · 2026-05-19T13:08:36.787Z_

<details><summary>↩ Tool result · `toolu_018Co1Zn5gaZRRosoC2he7YS`</summary>

```text
260	\end{tabular}}
261	\end{table}
262	
263	\paragraph{Per-fold transparency.}
264	For Qwen-1.5B, cross-family scoring (Pythia-1.4B) yields $\auc$(1v2) $= 0.5994$, with per-fold values $[0.596, 0.606, 0.600, 0.603, 0.592]$ (2/5 folds marginally above $\theta = 0.60$).
265	The aggregate mean falls below $\theta$, confirming $\Kempirical{=}1$.
266	For Qwen-7B, the corresponding $\auc$ drops further to $0.587$.
267	
268	\subsection{ArXiv Cross-Scorer Bootstrap CIs}
269	\label{sec:arxiv_crossscorer_ci}
270	
271	\begin{table}[h]
272	\centering
273	\small
274	\caption{Bootstrap 95\% CI for arXiv cross-scorer (Pythia-1.4B) 2v3 boundary $\auc$ (10{,}000 resamples). Point estimates classify 3/4 generators as $\Kempirical{=}3$; strict CI lower-bound criterion confirms 2/4.}
275	\label{tab:arxiv_crossscorer_ci}
276	\resizebox{\columnwidth}{!}{%
277	\begin{tabular}{lccc}
278	\toprule
279	\textbf{Generator} & \textbf{2v3 $\auc$} & \textbf{95\% CI} & \textbf{CI lower $> \theta$} \\
280	\midrule
281	Qwen-1.5B    & 0.632 & $[0.617,\,0.646]$ & Yes \\
282	LLaMA-3.1-8B & 0.620 & $[0.605,\,0.636]$ & Yes (0.5\,pp margin) \\
283	Mistral-7B   & 0.608 & $[0.593,\,0.622]$ & No \\
284	Qwen-7B      & 0.599 & $[0.584,\,0.613]$ & No \\
285	\bottomrule
286	\end{tabular}}
287	\end{table}
288	
289	\subsection{JSD Decay Analysis}
290	\label{sec:jsd_extended}
291	
292	The token-level JSD between adjacent generations reveals two distinct decay regimes (Figure~\ref{fig:jsd_decay}).
293	For C4 web text, 0v1 JSD exceeds 1v2 by 6--56$\times$ across all 8 models (1B--14B) with $\Kempirical{=}2$ (median cliff ratio ${\sim}$15$\times$), and subsequent pairs converge to a noise floor of ${\sim}$0.003--0.005.
294	Fitting $\jsd(k, k{+}1) \propto e^{-\lambda k}$ yields $\lambda \approx 2.2$--$3.5$ for C4 (mean ${\approx}\,2.9$), consistent with rapid mixing of $G_\delta$ toward its stationary distribution.
295	These decay rates represent qualitative characterizations from 5-point curves rather than precise estimates.
296	The empirical decay rate $\lambda$ is consistent within each domain but varies across domains: C4 yields $\lambda \approx 2.9$, Wikipedia $\lambda \approx 3.1$ (excluding OLMo, whose $\lambda = 6.3$ reflects a capacity-limited collapse: 0v1 $\jsd = 0.169$ with near-complete information loss at the first step, the exponential fit is therefore unreliable), and arXiv $\lambda \approx 1.0$.
297	This cross-model consistency indicates that the contraction rate of $G_\delta$ is governed primarily by the structure of the input domain rather than the model architecture.
298	ArXiv text decays ${\sim}$3$\times$ slower than C4 ($\lambda \approx 1.0$ vs.\ $2.9$), with a correspondingly higher convergence floor (${\sim}$0.007--0.009 vs.\ ${\sim}$0.003--0.004).
299	Formulaic structural features (LaTeX formatting, citation patterns, section templates) degrade more slowly under autoregressive generation and supply persistent depth-distinguishing signal, this accounts for the elevated $\Kempirical{=}3$.
300	The retrain-chain exhibits a fundamentally different profile: $\lambda = 0.285$ with a cliff ratio of only 1.31$\times$ and no sharp drop between adjacent pairs (Figure~\ref{fig:retrain_decay}).
301	This gradual, sustained divergence reflects cumulative model-adaptation artifacts rather than text-intrinsic information loss, further supporting the distinction between prompt-chain and retrain-chain $\Kempirical$ (Appendix~\ref{sec:boundary_extended}).
302	
303	\begin{figure}[h]
304	\centering
305	\includegraphics[width=\columnwidth]{figures/fig_retrain_decay.png}
306	\caption{Retrain-chain AUC decay across 7 generation pairs (Qwen2.5-1.5B LoRA). Unlike prompt-chain (sharp cliff at 0v1$\to$1v2), retrain-chain AUC decays gradually from 0.984 to 0.641, with all pairs above $\theta{=}0.60$. Error bars: 95\% CI from 5-fold CV. Dashed line: $\theta{=}0.60$; extrapolated 7v8 $\approx 0.57$ (below $\theta$), suggesting $\Kempirical{=}7$ is near the ceiling.}
307	\label{fig:retrain_decay}
308	\end{figure}
309	
310	\subsection{Boundary Cases and Scale Effect}
311	\label{sec:boundary_extended}
312	
313	Of 9 tested model configurations on C4, 8 yield $\Kempirical{=}2$; Mistral-7B is the only sub-2 exception ($\Kempirical{=}1$; 1v2 $\auc = 0.594$, CI $[0.584, 0.603]$), validating $\theta{=}0.60$ as an effective discriminator (gap: $0.594$ vs.\ $0.611$--$0.696$).
314	Mistral's cross-domain profile reinforces the domain-governed interpretation: despite $\Kempirical{=}1$ on C4 and Wikipedia, it yields $\Kempirical{=}2$ on code and $\Kempirical{=}3$ on arXiv (1v2 $\auc = 0.820$, 2v3 $= 0.628$), and this profile persists under cross-scorer validation (Pythia-1.4B scorer: C4 $\Kempirical{=}1$, arXiv $\Kempirical{=}3$ (2v3 $\auc = 0.608$, CI $[0.593, 0.622]$)), domain lexical diversity can therefore rescue even web-text one-wash generators (Table~\ref{tab:domain_kstar}).
315	Larger models produce more human-like text, reducing 0v1 JSD: 0.16--0.29 at $\leq$1.5B, 0.077--0.13 at 7--14B.
316	However, Qwen-14B still yields $\Kempirical{=}2$ (1v2 $\auc = 0.621$, CI $[0.612, 0.630]$), with 0v1 $\auc = 0.960$ comparable to Qwen-7B ($0.964$), scale in the 1B--14B range therefore does not shift the discrimination boundary.
317	
318	\paragraph{Sample-size control.}
319	As a sample-size control, subsampling C4 to $n{=}2{,}200$ (matching arXiv) yields $\Kempirical{=}1$ (1v2 $\auc = 0.601$, CI $[0.586, 0.616]$).
320	Reduced sample size widens confidence intervals and produces more conservative $\Kempirical$ estimates, arXiv's $\Kempirical{=}3$ at the same sample size therefore reflects genuine domain signal rather than a statistical artifact of smaller training sets.
321	
322	\subsection{LaTeX Markup Ablation (arXiv)}
323	\label{sec:latex_ablation}
324	
325	To disentangle content-level depth signal from formatting artifacts on arXiv, we strip all LaTeX markup (commands, environments, inline math delimiters) and re-extract features from the plain-text residual (Qwen-1.5B continuation, $n{=}2{,}200$; Table~\ref{tab:latex_ablation}).
326	
327	\begin{table}[h]
328	\centering
329	\small
330	\caption{arXiv pairwise $\auc$ with and without LaTeX markup (Qwen-1.5B continuation). Removing formatting reduces 2v3 by ${\sim}$1.8\,pp but $\Kempirical$ remains at 3 (CI lower $> \theta$). LaTeX stripping fraction increases with depth (0.6\% at depth 0, 4.6\% at depth 5), deeper generations therefore produce proportionally more formatting tokens.}
331	\label{tab:latex_ablation}
332	\resizebox{\columnwidth}{!}{%
333	\begin{tabular}{lccr}
334	\toprule
335	\textbf{Pair} & \textbf{Original} & \textbf{Stripped} & $\Delta$ \\
336	\midrule
337	0v1 & 0.9946 & 0.9948 & $+$0.0002 \\
338	1v2 & 0.8580 & 0.8297 & $-$0.028 \\
339	2v3 & 0.6427 $[0.628,\,0.658]$ & 0.6248 $[0.610,\,0.640]$ & $-$0.018 \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "69c26890-ee85-4846-9b13-ec5c18878463",
  "isSidechain": false,
  "promptId": "12172553-d9aa-40c5-a42d-a4d4469a539a",
  "type": "user",
  "uuid": "a9c60771-1b1e-426a-8d72-0b0abd4102ee",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex",
      "content": "\\end{tabular}}\n\\end{table}\n\n\\paragraph{Per-fold transparency.}\nFor Qwen-1.5B, cross-family scoring (Pythia-1.4B) yields $\\auc$(1v2) $= 0.5994$, with per-fold values $[0.596, 0.606, 0.600, 0.603, 0.592]$ (2/5 folds marginally above $\\theta = 0.60$).\nThe aggregate mean falls below $\\theta$, confirming $\\Kempirical{=}1$.\nFor Qwen-7B, the corresponding $\\auc$ drops further to $0.587$.\n\n\\subsection{ArXiv Cross-Scorer Bootstrap CIs}\n\\label{sec:arxiv_crossscorer_ci}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Bootstrap 95\\% CI for arXiv cross-scorer (Pythia-1.4B) 2v3 boundary $\\auc$ (10{,}000 resamples). Point estimates classify 3/4 generators as $\\Kempirical{=}3$; strict CI lower-bound criterion confirms 2/4.}\n\\label{tab:arxiv_crossscorer_ci}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Generator} & \\textbf{2v3 $\\auc$} & \\textbf{95\\% CI} & \\textbf{CI lower $> \\theta$} \\\\\n\\midrule\nQwen-1.5B    & 0.632 & $[0.617,\\,0.646]$ & Yes \\\\\nLLaMA-3.1-8B & 0.620 & $[0.605,\\,0.636]$ & Yes (0.5\\,pp margin) \\\\\nMistral-7B   & 0.608 & $[0.593,\\,0.622]$ & No \\\\\nQwen-7B      & 0.599 & $[0.584,\\,0.613]$ & No \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\subsection{JSD Decay Analysis}\n\\label{sec:jsd_extended}\n\nThe token-level JSD between adjacent generations reveals two distinct decay regimes (Figure~\\ref{fig:jsd_decay}).\nFor C4 web text, 0v1 JSD exceeds 1v2 by 6--56$\\times$ across all 8 models (1B--14B) with $\\Kempirical{=}2$ (median cliff ratio ${\\sim}$15$\\times$), and subsequent pairs converge to a noise floor of ${\\sim}$0.003--0.005.\nFitting $\\jsd(k, k{+}1) \\propto e^{-\\lambda k}$ yields $\\lambda \\approx 2.2$--$3.5$ for C4 (mean ${\\approx}\\,2.9$), consistent with rapid mixing of $G_\\delta$ toward its stationary distribution.\nThese decay rates represent qualitative characterizations from 5-point curves rather than precise estimates.\nThe empirical decay rate $\\lambda$ is consistent within each domain but varies across domains: C4 yields $\\lambda \\approx 2.9$, Wikipedia $\\lambda \\approx 3.1$ (excluding OLMo, whose $\\lambda = 6.3$ reflects a capacity-limited collapse: 0v1 $\\jsd = 0.169$ with near-complete information loss at the first step, the exponential fit is therefore unreliable), and arXiv $\\lambda \\approx 1.0$.\nThis cross-model consistency indicates that the contraction rate of $G_\\delta$ is governed primarily by the structure of the input domain rather than the model architecture.\nArXiv text decays ${\\sim}$3$\\times$ slower than C4 ($\\lambda \\approx 1.0$ vs.\\ $2.9$), with a correspondingly higher convergence floor (${\\sim}$0.007--0.009 vs.\\ ${\\sim}$0.003--0.004).\nFormulaic structural features (LaTeX formatting, citation patterns, section templates) degrade more slowly under autoregressive generation and supply persistent depth-distinguishing signal, this accounts for the elevated $\\Kempirical{=}3$.\nThe retrain-chain exhibits a fundamentally different profile: $\\lambda = 0.285$ with a cliff ratio of only 1.31$\\times$ and no sharp drop between adjacent pairs (Figure~\\ref{fig:retrain_decay}).\nThis gradual, sustained divergence reflects cumulative model-adaptation artifacts rather than text-intrinsic information loss, further supporting the distinction between prompt-chain and retrain-chain $\\Kempirical$ (Appendix~\\ref{sec:boundary_extended}).\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig_retrain_decay.png}\n\\caption{Retrain-chain AUC decay across 7 generation pairs (Qwen2.5-1.5B LoRA). Unlike prompt-chain (sharp cliff at 0v1$\\to$1v2), retrain-chain AUC decays gradually from 0.984 to 0.641, with all pairs above $\\theta{=}0.60$. Error bars: 95\\% CI from 5-fold CV. Dashed line: $\\theta{=}0.60$; extrapolated 7v8 $\\approx 0.57$ (below $\\theta$), suggesting $\\Kempirical{=}7$ is near the ceiling.}\n\\label{fig:retrain_decay}\n\\end{figure}\n\n\\subsection{Boundary Cases and Scale Effect}\n\\label{sec:boundary_extended}\n\nOf 9 tested model configurations on C4, 8 yield $\\Kempirical{=}2$; Mistral-7B is the only sub-2 exception ($\\Kempirical{=}1$; 1v2 $\\auc = 0.594$, CI $[0.584, 0.603]$), validating $\\theta{=}0.60$ as an effective discriminator (gap: $0.594$ vs.\\ $0.611$--$0.696$).\nMistral's cross-domain profile reinforces the domain-governed interpretation: despite $\\Kempirical{=}1$ on C4 and Wikipedia, it yields $\\Kempirical{=}2$ on code and $\\Kempirical{=}3$ on arXiv (1v2 $\\auc = 0.820$, 2v3 $= 0.628$), and this profile persists under cross-scorer validation (Pythia-1.4B scorer: C4 $\\Kempirical{=}1$, arXiv $\\Kempirical{=}3$ (2v3 $\\auc = 0.608$, CI $[0.593, 0.622]$)), domain lexical diversity can therefore rescue even web-text one-wash generators (Table~\\ref{tab:domain_kstar}).\nLarger models produce more human-like text, reducing 0v1 JSD: 0.16--0.29 at $\\leq$1.5B, 0.077--0.13 at 7--14B.\nHowever, Qwen-14B still yields $\\Kempirical{=}2$ (1v2 $\\auc = 0.621$, CI $[0.612, 0.630]$), with 0v1 $\\auc = 0.960$ comparable to Qwen-7B ($0.964$), scale in the 1B--14B range therefore does not shift the discrimination boundary.\n\n\\paragraph{Sample-size control.}\nAs a sample-size control, subsampling C4 to $n{=}2{,}200$ (matching arXiv) yields $\\Kempirical{=}1$ (1v2 $\\auc = 0.601$, CI $[0.586, 0.616]$).\nReduced sample size widens confidence intervals and produces more conservative $\\Kempirical$ estimates, arXiv's $\\Kempirical{=}3$ at the same sample size therefore reflects genuine domain signal rather than a statistical artifact of smaller training sets.\n\n\\subsection{LaTeX Markup Ablation (arXiv)}\n\\label{sec:latex_ablation}\n\nTo disentangle content-level depth signal from formatting artifacts on arXiv, we strip all LaTeX markup (commands, environments, inline math delimiters) and re-extract features from the plain-text residual (Qwen-1.5B continuation, $n{=}2{,}200$; Table~\\ref{tab:latex_ablation}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{arXiv pairwise $\\auc$ with and without LaTeX markup (Qwen-1.5B continuation). Removing formatting reduces 2v3 by ${\\sim}$1.8\\,pp but $\\Kempirical$ remains at 3 (CI lower $> \\theta$). LaTeX stripping fraction increases with depth (0.6\\% at depth 0, 4.6\\% at depth 5), deeper generations therefore produce proportionally more formatting tokens.}\n\\label{tab:latex_ablation}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccr}\n\\toprule\n\\textbf{Pair} & \\textbf{Original} & \\textbf{Stripped} & $\\Delta$ \\\\\n\\midrule\n0v1 & 0.9946 & 0.9948 & $+$0.0002 \\\\\n1v2 & 0.8580 & 0.8297 & $-$0.028 \\\\\n2v3 & 0.6427 $[0.628,\\,0.658]$ & 0.6248 $[0.610,\\,0.640]$ & $-$0.018 \\\\",
      "numLines": 80,
      "startLine": 260,
      "totalLines": 695
    }
  },
  "sourceToolAssistantUUID": "69c26890-ee85-4846-9b13-ec5c18878463",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "crystalline-noodling-flask"
}
```

</details>

---


### Tool result

_source line 243 · 2026-05-19T13:08:36.483Z_

<details><summary>↩ Tool result · `toolu_01Jf9nBEi2JJr8aRvwujuEEG`</summary>

```text
Total pages: 28
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "376b7ace-aa14-40e7-a4b7-e6eebf1f1451",
  "isSidechain": false,
  "promptId": "12172553-d9aa-40c5-a42d-a4d4469a539a",
  "type": "user",
  "uuid": "f4b595a7-028c-4961-8ae8-4d5f1ecf3761",
  "toolUseResult": {
    "stdout": "Total pages: 28",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "376b7ace-aa14-40e7-a4b7-e6eebf1f1451",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "crystalline-noodling-flask"
}
```

</details>

---


### Tool call

_source line 244 · 2026-05-19T13:08:36.778Z_

<details open><summary>🔧 Tool call — Read · `toolu_018Co1Zn5gaZRRosoC2he7YS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/appendix_extended.tex",
  "offset": 260,
  "limit": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f4b595a7-028c-4961-8ae8-4d5f1ecf3761",
  "isSidechain": false,
  "requestId": "req_011CbByotQyoQhrCmMa13GYB",
  "type": "assistant",
  "uuid": "69c26890-ee85-4846-9b13-ec5c18878463",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/.claude/sessions/review_reviewer_2_55676115",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "crystalline-noodling-flask",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DaXmThjVdXVRATcCcxt4yd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6039,
      "cache_read_input_tokens": 46735,
      "output_tokens": 451,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6039,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 451,
          "cache_read_input_tokens": 46735,
          "cache_creation_input_tokens": 6039,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6039
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

_source line 245_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 2 审稿请求]: ## Round 9（继续审稿）— Reviewer 2（新颖性 + 完整性 + 写作质量）  上轮评分：3.5 (Borderline Conference)。论文已大幅修订，请重点验证以下 open/in_progress issues 是否已充分修复。  ### 论文路径 `projects/gen-depth-contamination/docs/paper…",
  "leafUuid": "a9c60771-1b1e-426a-8d72-0b0abd4102ee",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77"
}
```

---


### Runtime record

_source line 246_

```json
{
  "type": "ai-title",
  "aiTitle": "Review paper on data contamination detection for EMNLP 2026",
  "sessionId": "f9be207d-2c73-4ecb-ba22-6b935f15af77"
}
```

---
